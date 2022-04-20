# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import edb_messages_pb2 as edb__messages__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import layer_collection_pb2 as layer__collection__pb2


class LayerCollectionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Cleanup = channel.unary_unary(
        '/ansys.api.edb.v1.LayerCollectionService/Cleanup',
        request_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Create = channel.unary_unary(
        '/ansys.api.edb.v1.LayerCollectionService/Create',
        request_serializer=layer__collection__pb2.LayerCollectionCreateMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )
    self.AddLayers = channel.unary_unary(
        '/ansys.api.edb.v1.LayerCollectionService/AddLayers',
        request_serializer=layer__collection__pb2.AddLayersMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
        )
    self.FindByName = channel.unary_unary(
        '/ansys.api.edb.v1.LayerCollectionService/FindByName',
        request_serializer=layer__collection__pb2.FindLayerByNameMessage.SerializeToString,
        response_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
        )


class LayerCollectionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Cleanup(self, request, context):
    """Clean up the layer pointer
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates an empty LayerCollection
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLayers(self, request, context):
    """Adds the provided layers to the LayerCollection
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindByName(self, request, context):
    """Finds a layer with the given name in the layer collection
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LayerCollectionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Cleanup': grpc.unary_unary_rpc_method_handler(
          servicer.Cleanup,
          request_deserializer=edb__messages__pb2.EDBObjMessage.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=layer__collection__pb2.LayerCollectionCreateMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
      'AddLayers': grpc.unary_unary_rpc_method_handler(
          servicer.AddLayers,
          request_deserializer=layer__collection__pb2.AddLayersMessage.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
      ),
      'FindByName': grpc.unary_unary_rpc_method_handler(
          servicer.FindByName,
          request_deserializer=layer__collection__pb2.FindLayerByNameMessage.FromString,
          response_serializer=edb__messages__pb2.EDBObjMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ansys.api.edb.v1.LayerCollectionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
