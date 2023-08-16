"""
Client for adc service
"""
import logging
from edgepirpc.protos import adc_pb2 as adc_pb
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel
from client.client_services.adc.adc_pb_enums import (
    AnalogIn,
    ConvMode,
    ADC1DataRate,
    ADC2DataRate,
    FilterMode
)

_logger = logging.getLogger(__name__)

# pylint: disable=no-member
class ClientAdcService():
    """Client Methods for Adc Service"""
    def __init__(self, transport):
        self.client_rpc_channel = ClientAdcService(transport)
        self.service_stub = adc_pb.AdcService_stub(self.client_rpc_channel)
        self.rpc_controller = None

    