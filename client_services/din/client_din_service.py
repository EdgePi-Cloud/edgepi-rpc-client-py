"""
Client for Din service. Utilizes ClientRpcChannel to send/receive and
serialize/deserialize messages
"""
from edgepirpc.protos import dout_pb2 as din_pb
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel
from client.client_services.dout.dout_pb_enums import DinPins


class clie