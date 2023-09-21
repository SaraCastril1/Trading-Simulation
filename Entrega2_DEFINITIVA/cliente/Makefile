.PHONY = pb2
SHELL := /bin/bash

cliente:
	pip3 install grpcio grpcio-tools

	python3 -m grpc_tools.protoc -I ./protobufs --python_out=./src --pyi_out=./src --grpc_python_out=./src ./protobufs/moneda.proto
