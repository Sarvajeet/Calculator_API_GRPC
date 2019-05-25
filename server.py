# -*- coding: utf-8 -*-
"""
Created on Sun May 26 01:24:19 2019

@author: Sarva
"""

import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc

import calculator

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    
    def SquareRoot(self, request, context):
        response=calculator_pb2.Number();
        response.value=calculator.squareRoot(request.value)
        return response
    

server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(),server)

print('Starting server. Listening on prot 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86000)
except KeyboardInterrupt:
    server.stop(0)