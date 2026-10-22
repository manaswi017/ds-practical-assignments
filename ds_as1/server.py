from concurrent import futures
import grpc

import distributed_systems_code.ds_as1.chat_pb2 as chat_pb2
import distributed_systems_code.ds_as1.chat_pb2_grpc as chat_pb2_grpc


class Chat(chat_pb2_grpc.ChatServiceServicer):

    def SendMessage(self, request, context):
        print("Client says:", request.message)

        return chat_pb2.MessageReply(
            reply="Hello Client! Message received."
        )


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=5)
    )

    chat_pb2_grpc.add_ChatServiceServicer_to_server(
        Chat(),
        server
    )

    server.add_insecure_port("[::]:50051")

    server.start()

    print("Server started...")
    print("Waiting for client...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()