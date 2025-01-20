import grpc
from protos.runpod_pb2 import RunpodRequest
from protos.runpod_pb2_grpc import RunpodServiceStub


class RunpodClient:
    def __init__(self, host="localhost", port="50051"):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = RunpodServiceStub(self.channel)

    def create_request(
        self,
        text: str = None,
        image: bytes = None,
        image_format: str = None,
        parameters: dict = None,
    ) -> RunpodRequest:
        """Helper method to create a RunpodRequest with validation"""
        if not text and not image:
            raise ValueError("Either text or image must be provided")

        request = RunpodRequest()
        if text is not None:
            request.text = text
        if image is not None:
            if not image_format:
                raise ValueError("image_format must be provided when using image")
            request.image_data = image
            request.image_format = image_format
        if parameters:
            request.parameters.update(parameters)

        return request

    def process(self, request: RunpodRequest):
        """Process a request through the runpod service"""
        try:
            return self.stub.Inference(request)
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}: {e.details()}")
            raise

    def close(self):
        self.channel.close()

    def __del__(self):
        self.close()
