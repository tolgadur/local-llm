import grpc
from concurrent import futures
from app.config import Config
from shared.runpod import runpod_pb2
from shared.runpod import runpod_pb2_grpc


class RunpodServicer(runpod_pb2_grpc.RunpodServiceServicer):
    def Process(self, request, context):
        try:
            # Initialize response
            response = runpod_pb2.RunpodResponse()
            response.success = True

            # Process text if present
            if request.text:
                # TODO: Implement actual text processing logic
                response.text_result = f"Processed text: {request.text}"

            # Process image if present
            if request.image_data:
                # TODO: Implement actual image processing logic
                response.image_data = request.image_data
                response.image_format = request.image_format

            return response

        except Exception as e:
            response = runpod_pb2.RunpodResponse(success=False, error_message=str(e))
            return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    runpod_pb2_grpc.add_RunpodServiceServicer_to_server(RunpodServicer(), server)
    server.add_insecure_port(f"[::]:{Config.GRPC_PORT}")
    server.start()
    print(f"Server started on port {Config.GRPC_PORT}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
