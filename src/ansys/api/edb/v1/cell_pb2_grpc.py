# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cell_pb2 as cell__pb2
import edb_messages_pb2 as edb__messages__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class CellServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/ansys.api.edb.v1.CellService/Create',
        request_serializer=cell__pb2.CellCreationMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )
    self.GetLayout = channel.unary_unary(
        '/ansys.api.edb.v1.CellService/GetLayout',
        request_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )
    self.SetHfssExtents = channel.unary_unary(
        '/ansys.api.edb.v1.CellService/SetHfssExtents',
        request_serializer=cell__pb2.CellHfssExtentsMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
        )


class CellServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    """Creates a cell
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLayout(self, request, context):
    """Gets the layout of the provided cell
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetHfssExtents(self, request, context):
    """Sets HFSS extents on cell
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CellServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=cell__pb2.CellCreationMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
      'GetLayout': grpc.unary_unary_rpc_method_handler(
          servicer.GetLayout,
          request_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
      'SetHfssExtents': grpc.unary_unary_rpc_method_handler(
          servicer.SetHfssExtents,
          request_deserializer=cell__pb2.CellHfssExtentsMessage.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ansys.api.edb.v1.CellService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
