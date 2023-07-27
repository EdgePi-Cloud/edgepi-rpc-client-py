"""
Client for Dout service. Utilizes ClientRpcChannel to send/receive and
serialize/deserialize messages
"""
from rpc_module.protos import dout_pb2 as dout_pb
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel
from client.client_services.dout.dout_pb_enums import DoutPins

SOCKET_ENDPOINT = "ipc:///tmp/edgepi.pipe"

# pylint: disable=no-member
class ClientDoutService():
    """Client methods for Dout service"""
    def __init__(self):
        self.client_rpc_channel = ClientRpcChannel(SOCKET_ENDPOINT)
        self.service_stub = dout_pb.LEDService_Stub(self.client_rpc_channel)
        self.rpc_controller = None

    def set_dout_state(self, dout_pin: DoutPins):
        """set_dout_state method for sdk dout module"""
        request = dout_pb.PinAndState(
            dout_pin = dout_pin.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.set_dout_state(self.rpc_controller,request)

        return response.content