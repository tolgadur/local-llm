import grpc
from concurrent import futures
import io
from PIL import Image
from app.config import GRPC_PORT
from app.models import LLAMA11B_TEXT, LLAMA11B_VISION
from protos.runpod_pb2 import RunpodResponse
from protos.runpod_pb2_grpc import (
    RunpodServiceServicer,
    add_RunpodServiceServicer_to_server,
)
from grpc_reflection.v1alpha import reflection
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class RunpodServicer(RunpodServiceServicer):
    def Inference(self, request, context):
        try:
            logger.info(
                "Received inference request: "
                f"text='{request.text}', "
                f"has_image={bool(request.image_data)}"
            )

            # Initialize response
            response = RunpodResponse()

            # Check if we have text (required)
            if not request.text:
                error_msg = "Text input is required for inference"
                logger.error(error_msg)
                return RunpodResponse(success=False, error_message=error_msg)

            try:
                # Run inference with the model
                logger.info("=== Starting Inference ===")

                # Set up model parameters
                model_kwargs = {
                    "max_new_tokens": 512,
                    "do_sample": True,
                    "temperature": 0.7,
                }

                # Initialize result variable
                result = None

                if request.image_data:
                    # Use vision pipeline for image + text
                    try:
                        image = Image.open(io.BytesIO(request.image_data))
                        logger.info(f"✓ Image loaded (format: {request.image_format})")

                        logger.info("Running vision model inference...")
                        result = LLAMA11B_VISION(
                            text=request.text, images=image, **model_kwargs
                        )
                        logger.info("✓ Vision inference complete")
                    except Exception as img_error:
                        error_msg = f"Failed to process image: {str(img_error)}"
                        logger.error(error_msg, exc_info=True)
                        return RunpodResponse(success=False, error_message=error_msg)
                else:
                    # Use text-only pipeline
                    logger.info("Running text-only inference...")
                    result = LLAMA11B_TEXT(text_inputs=request.text, **model_kwargs)
                    logger.info("✓ Text inference complete")

                if result is None:
                    error_msg = "Model inference failed to produce a result"
                    logger.error(error_msg)
                    return RunpodResponse(success=False, error_message=error_msg)

                # Extract the generated text
                response.text_result = result[0]["generated_text"]
                response.success = True
                logger.info("=== Inference Complete ===\n")

            except Exception as model_error:
                error_msg = f"Model inference failed: {str(model_error)}"
                logger.error(error_msg, exc_info=True)
                return RunpodResponse(success=False, error_message=error_msg)

            logger.info("Request processed successfully")
            return response

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}", exc_info=True)
            return RunpodResponse(success=False, error_message=str(e))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RunpodServiceServicer_to_server(RunpodServicer(), server)

    # Add reflection service
    SERVICE_NAMES = (
        "runpod.RunpodService",
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(f"[::]:{GRPC_PORT}")
    server.start()
    logger.info(f"Server started on port {GRPC_PORT}")
    logger.info(f"Registered services: {', '.join(SERVICE_NAMES)}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
