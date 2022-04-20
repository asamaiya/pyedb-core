# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import edb_messages_pb2 as edb__messages__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import rectangle_pb2 as rectangle__pb2


class RectangleServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/ansys.api.edb.v1.RectangleService/Create',
        request_serializer=rectangle__pb2.RectangleCreationMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )
    self.GetParameters = channel.unary_unary(
        '/ansys.api.edb.v1.RectangleService/GetParameters',
        request_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
        response_deserializer=rectangle__pb2.RectangleParametersMessage.FromString,
        )
    self.SetParameters = channel.unary_unary(
        '/ansys.api.edb.v1.RectangleService/SetParameters',
        request_serializer=rectangle__pb2.SetRectangleParametersMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
        )
    self.Render = channel.unary_unary(
        '/ansys.api.edb.v1.RectangleService/Render',
        request_serializer=rectangle__pb2.RectanglePolygonDataMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )


class RectangleServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    """Create a rectangle
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetParameters(self, request, context):
    """Return Rectangle Parameters
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetParameters(self, request, context):
    """Recieve Rectangle Parameters
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Render(self, request, context):
    """Render Geometry PolygonData
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RectangleServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=rectangle__pb2.RectangleCreationMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
      'GetParameters': grpc.unary_unary_rpc_method_handler(
          servicer.GetParameters,
          request_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
          response_serializer=rectangle__pb2.RectangleParametersMessage.SerializeToString,
      ),
      'SetParameters': grpc.unary_unary_rpc_method_handler(
          servicer.SetParameters,
          request_deserializer=rectangle__pb2.SetRectangleParametersMessage.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
      ),
      'Render': grpc.unary_unary_rpc_method_handler(
          servicer.Render,
          request_deserializer=rectangle__pb2.RectanglePolygonDataMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ansys.api.edb.v1.RectangleService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
