"""Client to use for integration tests"""
import logging
import google.protobuf.service as service
import zmq
from rpc_module.protos import rpc_pb2 as rpc_pb

_logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"
)

class ClientRpcChannel(service.RpcChannel):
    """
    Client class that utilizes google's abstract RpcChannel interfce. 
    - The RpcChannel represents a comunication line to a service and can 
    be used to call that service's methods. 
    - This class handles connecting to the RPC server, as well as serializing/deserializing
    messages to and from the server when service methods are called from the client side.
    """

    def __init__(self, socket_endpoint):
        self.socket_enpdpoint = socket_endpoint
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        try:
            self.socket.connect(self.socket_enpdpoint)
        # pylint: disable=broad-except, broad-exception-caught
        except Exception as exc:
            _logger.error(exc)

    # pylint: disable=no-member
    def _get_rpc_request(self, method, client_request):
        # Wrap client's request msg in an RPC message
        rpc_request = rpc_pb.RpcRequest()
        # Set rpc request to client's request as byte string
        rpc_request.request_proto = client_request.SerializeToString()
        # Set rpc service and method name
        rpc_request.service_name = method.containing_service.name
        rpc_request.method_name = method.name

        return rpc_request

    def _send_rpc_request(self, rpc_request):
        # Serialize RPC protocol message
        rpc_request_data = rpc_request.SerializeToString()
        # Send over socket
        try:
            self.socket.send(rpc_request_data)
        # pylint: disable=broad-except, broad-exception-caught
        except Exception as exc:
            _logger.error(exc)

    #pylint: disable=no-member
    def _get_rpc_response(self):
        # Receive rpc response data from socket
        rpc_response_data = self.socket.recv()
        # Return the rpc response message
        rpc_response = rpc_pb.RpcResponse()
        rpc_response = rpc_response.FromString(rpc_response_data)
        return rpc_response

    def _get_server_response(self,rpc_response,server_response_class):
        # Get server response from rpc message and deserialize
        server_response_data = rpc_response.response_proto
        server_response = server_response_class.FromString(server_response_data)

        return server_response

    # pylint: disable=too-many-arguments
    def CallMethod(self, method_descriptor, rpc_controller, request, response_class, done):
        _logger.debug("Request message object: {%s}", request)
        # Create rpc request
        rpc_request = self._get_rpc_request(method_descriptor,request)
        _logger.debug("RPC Request message object: %s", rpc_request)
        # Send rpc service request over socket
        self._send_rpc_request(rpc_request)
        # Get the rpc response from socket
        rpc_response = self._get_rpc_response()
        _logger.debug("deserialized RPC response object: {%s}", rpc_response)
        # Get server reponse from rpc message
        server_response = self._get_server_response(rpc_response,response_class)
        _logger.debug("deserialized server response object: {%s}", server_response)
        # Return server response message
        return server_response
