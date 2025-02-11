from fastapi import FastAPI, HTTPException
from app.models import LOCAL_MODEL_CPU
import uvicorn
from app.runpod_client import RunpodClient
from app.api_types import (
    InternalGenerateRequest,
    InternalRunpodRequest,
    InternalRunpodResponse,
)
from app.config import RUNPOD_HOST, RUNPOD_PORT
import grpc

app = FastAPI(title="Local LLM API")
runpod_client = RunpodClient(host=RUNPOD_HOST, port=RUNPOD_PORT)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/generate")
def generate_text(request: InternalGenerateRequest):
    try:
        response = LOCAL_MODEL_CPU(request.prompt, max_new_tokens=request.max_tokens)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/runpod/process")
async def process_with_runpod(request: InternalRunpodRequest) -> InternalRunpodResponse:
    """Forward request to runpod service."""
    try:
        grpcRequest = runpod_client.create_request(
            text=request.text,
            image=request.image,
            image_format=request.image_format,
            parameters=request.parameters,
        )
        grpcResponse = runpod_client.process(grpcRequest)

        # Convert response to dict
        response = InternalRunpodResponse(
            success=True,
            text_result=grpcResponse.text_result,
            image_data=grpcResponse.image_data,
            image_format=grpcResponse.image_format,
        )
        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except grpc.RpcError as e:
        error_msg = f"gRPC error: code={e.code()}, details={e.details()}"
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            error_msg += (
                f" (Failed to connect to gRPC server at {runpod_client.address})"
            )
        raise HTTPException(status_code=500, detail=error_msg)
    except Exception as e:
        return InternalRunpodResponse(success=False, error_message=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
