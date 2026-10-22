import grpc
import distributed_systems_code.ds_as1.chat_pb2 as chat_pb2
import distributed_systems_code.ds_as1.chat_pb2_grpc as chat_pb2_grpc

def run():
    # Attempt to connect to the server
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = chat_pb2_grpc.ChatServiceStub(channel)
        
        print("Connected to gRPC server successfully!")
        print("Type 'exit' or send 3 messages to quit.\n")
        
        # Requirement: Exchange at least three messages
        for i in range(1, 4):
            message = input(f"Enter message {i}: ")
            
            if message.lower() == 'exit':
                break
                
            # Send message via gRPC
            response = stub.SendMessage(
                chat_pb2.MessageRequest(message=message)
            )
            print("Server replied:", response.reply)
            print("-" * 30)
            
        channel.close()
        print("Connection terminated gracefully.")

    except grpc.RpcError as e:
        # Requirement: Handle the case in which the server is unavailable
        print("\n[Error] Could not connect to the server. Make sure 'server.py' is running!")
        print(f"Details: {e.details()}")

if __name__ == "__main__":
    run()