# -*- coding: utf-8 -*-
"""
Created on Sun May 26 01:40:25 2019

@author: Sarva
"""

import grpc

import calculator_pb2
import calculator_pb2_grpc

channel=grpc.insecure_channel('localhost:50051')

stub=calculator_pb2_grpc.CalculatorStub(channel)

number=calculator_pb2.Number(value=16)

response= stub.SquareRoot(number)

print (response.value)