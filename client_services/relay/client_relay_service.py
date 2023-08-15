"""
Client for Relay Service
"""
from edgepirpc.protos import relay_pb2 as relay_pb
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel


# pylint: disable=no-member
class ClientRelayService():
    """Client methods for relay service"""
    def __init__(self, transport):
        self.client_rpc_channel = ClientRpcChannel(transport)
        self.service_stub = relay_pb.RelayService_Stub(self.client_rpc_channel)
        self.rpc_controller = None

    def open_relay(self):
        """open_relay method for sdk relay module"""
        request = relay_pb.EmptyMsg()

        # Call SDK method through rpc channel client
        response = self.service_stub.open_relay(self.rpc_controller,request)

        return response.content

    def close_relay(self):
        """close_relay method for sdk relay module"""
        request = relay_pb.EmptyMsg()

        # Call SDK method through rpc channel client
        response = self.service_stub.close_relay(self.rpc_controller,request)

        return response.content
    
    def get_state_relay(self):
        """get_state_relay method for sdk relay module"""
        request = relay_pb.EmptyMsg()

        # Call SDK method through rpc channel client
        response = self.service_stub.get_state_relay(self.rpc_controller,request)

        return response.state_bool
