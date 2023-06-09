import logging
from rpc_module.protos import tc_pb2 as tc_pb
from rpc_module.rpc_controller import RpcController
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel

_logger = logging.getLogger(__name__)

SOCKET_ENDPOINT = "ipc:///tmp/edgepi.pipe"

class ClientTcService():
    """ """
    def __init__(self):
        self.client_rpc_channel = ClientRpcChannel(SOCKET_ENDPOINT)
        self.service_stub = tc_pb.TcService_Stub(self.client_rpc_channel)
        self.rpc_controller = RpcController()


    def single_sample(self):
        request = tc_pb.EmptyMsg()
        _logger.debug("Single sample request object created: {%s}", request)
        # call the SDK method through rpc channel client
        response = self.service_stub.single_sample(self.rpc_controller,request)
        temps = (response.cj_temp, response.lin_temp)
        return temps