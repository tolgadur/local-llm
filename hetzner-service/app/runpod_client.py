import grpc
from pathlib import Path
from app.config import Config
from app.types import RunpodRequest, RunpodResponse
from shared.runpod import runpod_pb2
from shared.runpod import runpod_pb2_grpc


class RunpodClient:
    def __init__(self, host: str = None, port: str = None):
        self.host = host or Config.RUNPOD_HOST
        self.port = port or Config.RUNPOD_PORT
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = runpod_pb2_grpc.RunpodServiceStub(self.channel)

    def process(self, request: RunpodRequest) -> RunpodResponse:
        """
        Process text and/or image through the runpod service.

        Args:
            request: RunpodRequest containing text and/or image data to process

        Returns:
            RunpodResponse containing the processing results and status
        """
        try:
            # Prepare gRPC request
            grpc_request = runpod_pb2.RunpodRequest()

            if request.text is not None:
                grpc_request.text = request.text

            if request.image_data is not None:
                if not request.image_format:
                    raise ValueError(
                        "image_format must be provided when using image_data"
                    )
                grpc_request.image_data = request.image_data
                grpc_request.image_format = request.image_format

            if request.parameters:
                grpc_request.parameters.update(request.parameters)

            # Make the call
            response = self.stub.Process(grpc_request)

            return RunpodResponse(
                success=response.success,
                error_message=response.error_message,
                text_result=(
                    response.text_result if response.HasField("text_result") else None
                ),
                image_data=(
                    response.image_data if response.HasField("image_data") else None
                ),
                image_format=(
                    response.image_format if response.HasField("image_format") else None
                ),
            )

        except Exception as e:
            return RunpodResponse(success=False, error_message=str(e))

    @classmethod
    def from_image_path(cls, image_path: str, parameters: dict = None) -> RunpodRequest:
        """Helper method to create a request from an image file path."""
        with open(image_path, "rb") as f:
            image_data = f.read()
        return RunpodRequest(
            image_data=image_data,
            image_format=Path(image_path).suffix[1:],  # Remove the dot
            parameters=parameters,
        )

    def close(self):
        """Close the gRPC channel."""
        self.channel.close()
