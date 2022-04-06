# import generated classes

import grpc
import calculator_pb2_grpc
import calculator_pb2

def run():
    # open grpc channel
    with grpc.insecure_channel('localhost:50052') as channel:

        # create a stub (client)
        stub = calculator_pb2_grpc.CalculatorServiceStub(channel)

        # create a valid request message
        request = calculator_pb2.CalcInput(value=16)

        # make the call
        response = stub.SquareRoot(request)

        print(response.value)
        
if __name__ == '__main__':
    run()

