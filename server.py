from urllib import response

import grpc
import calculator_pb2
import calculator_pb2_grpc
import time

#import original calculator.py file
import calculator
from concurrent import futures

# create a class to define the server functions which is derived from calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServiceServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.CalcOutput()
        response.value = calculator.square_root(request.value)
        return response
        #return super().SquareRoot(request, context)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(CalculatorServicer(), server)

    print('Starting server. Listening on port 50052...')
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

    # try:
    #     while True:
    #         time.sleep(86400)

    # except KeyboardInterrupt:
    #     server.stop(0)
if __name__ == '__main__':
    main()