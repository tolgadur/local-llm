import grpc
from protos.runpod_pb2 import RunpodRequest
from protos.runpod_pb2_grpc import RunpodServiceStub


def test_grpc_connection():
    # Create a channel to the server
    channel = grpc.insecure_channel("localhost:50051")

    # Create a stub (client)
    stub = RunpodServiceStub(channel)

    # Create a test request
    request = RunpodRequest(text="Hello, gRPC!")

    try:
        # Make the call
        response = stub.Inference(request)
        print("Connection successful!")
        print(f"Response received: {response.text_result}")
        print(f"Success status: {response.success}")

    except grpc.RpcError as e:
        print(f"RPC failed: {e}")

    finally:
        channel.close()
