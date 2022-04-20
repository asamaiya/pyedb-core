# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import edb_messages_pb2 as edb__messages__pb2
import point_term_pb2 as point__term__pb2


class PointTerminalServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/ansys.api.edb.v1.PointTerminalService/Create',
        request_serializer=point__term__pb2.PointTermCreationMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )


class PointTerminalServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    """Create a point term
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PointTerminalServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=point__term__pb2.PointTermCreationMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ansys.api.edb.v1.PointTerminalService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
