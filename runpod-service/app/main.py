import grpc
from concurrent import futures
from app.config import GRPC_PORT
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
            response.success = True

            # Process text if present
            if request.text:
                logger.info(f"Processing text: {request.text}")
                response.text_result = f"Processed text: {request.text}"

            # Process image if present
            if request.image_data:
                logger.info(f"Processing image with format: {request.image_format}")
                response.image_data = request.image_data
                response.image_format = request.image_format

            logger.info("Request processed successfully")
            return response

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}", exc_info=True)
            response = RunpodResponse(success=False, error_message=str(e))
            return response


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
