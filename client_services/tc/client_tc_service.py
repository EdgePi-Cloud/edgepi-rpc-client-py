"""
Client for tc service. Utilizes ClientRpcChannel to send/recieve
 and serialize/deserialize messages.
 """
import logging
from enum import Enum
from rpc_module.protos import tc_pb2 as tc_pb
from rpc_module.rpc_controller import RpcController
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel
from client.client_services.tc.tc_pb_enums import (
    AvgMode,
    CJHighMask,
    CJLowMask,
    CJMode,
    ConvMode,
    DecBits4,
    DecBits6,
    FaultMode,
    NoiseFilterMode,
    OpenCircuitMode,
    OpenMask,
    OvuvMask,
    TCHighMask,
    TCLowMask,
    TCType,
    VoltageMode,
)

_logger = logging.getLogger(__name__)

SOCKET_ENDPOINT = "ipc:///tmp/edgepi.pipe"

# pylint: disable=no-member
class ClientTcService():
    """Client Methods for Tc Service"""
    def __init__(self):
        self.client_rpc_channel = ClientRpcChannel(SOCKET_ENDPOINT)
        self.service_stub = tc_pb.TcService_Stub(self.client_rpc_channel)
        self.rpc_controller = RpcController()

    def _create_config_arg_msg(self, arg_name, arg_value):
        """Create a config protobuf message with the config argument name and value"""
        arg_msg = tc_pb.Config().ConfArg()
        # Do not access enum value if it's the argument is not an enum
        setattr(
            arg_msg, arg_name, arg_value if not isinstance(arg_value,Enum) else \
            arg_value.value
        )
        return arg_msg

    def _filter_arg_values(self, dictionary, filter_key, filter_value):
        """
        Gets a dictionary of arguments and filters unwanted keys by key or value. Returns a new
        dictionary
        """
        filtered_args_list = {
            key:value for (key,value) in dictionary.items()
                            if key != filter_key and value != filter_value
        }
        return filtered_args_list

    def _create_config_request_from_args(self,config_args_dict):
        # Create the set_config request message (Message with repeated arguments)
        request = tc_pb.Config()
        # Append each config argument message to the config message
        for arg_name,arg_value in config_args_dict.items():
            request_argument = self._create_config_arg_msg(arg_name,arg_value)
            _logger.debug("Config argument message: %s", request_argument)
            request.conf_arg.append(request_argument)

        return request

    def _generate_faults_dict(self, faults_msg):
        faults_dict = {}

        for fault_msg in faults_msg.fault:
            faults_dict[fault_msg.fault_type] = {
                'Fault Type': fault_msg.fault_type,
                'At Fault': fault_msg.at_fault,
                'Fault Message': fault_msg.err_msg,
                'Fault Masked': fault_msg.is_masked
            }

        return faults_dict
            


    # pylint: disable=unused-argument, too-many-arguments
    def set_config(self, conversion_mode: ConvMode = None,
        open_circuit_mode: OpenCircuitMode = None,
        cold_junction_mode: CJMode = None,
        fault_mode: FaultMode = None,
        noise_filter_mode: NoiseFilterMode = None,
        average_mode: AvgMode = None,
        tc_type: TCType = None,
        voltage_mode: VoltageMode = None,
        cj_high_mask: CJHighMask = None,
        cj_low_mask: CJLowMask = None,
        tc_high_mask: TCHighMask = None,
        tc_low_mask: TCLowMask = None,
        ovuv_mask: OvuvMask = None,
        open_mask: OpenMask = None,
        cj_high_threshold: int = None,
        cj_low_threshold: int = None,
        lt_high_threshold: int = None,
        lt_high_threshold_decimals: DecBits4 = None,
        lt_low_threshold: int = None,
        lt_low_threshold_decimals: DecBits4 = None,
        cj_offset: int = None,
        cj_offset_decimals: DecBits4 = None,
        cj_temp: int = None,
        cj_temp_decimals: DecBits6 = None,
    ):
        """set_config method for sdk tc module."""
        # Get a dictionary of arguments that are not None.
        config_args_dict= self._filter_arg_values(locals(), 'self', None)
        _logger.debug("Config argument dictionary: %s", config_args_dict)
        request = self._create_config_request_from_args(config_args_dict=config_args_dict)
        # Call the SDK method through the rpc channel client
        response = self.service_stub.set_config(self.rpc_controller,request)
        return response.content

    def single_sample(self):
        """single_sample method for sdk tc module"""
        request = tc_pb.EmptyMsg()
        # call the SDK method through rpc channel client
        response = self.service_stub.single_sample(self.rpc_controller,request)

        temps = (response.cj_temp, response.lin_temp)

        return temps

    def read_temperatures(self):
        """read_temperatures method for sdk tc module"""
        request = tc_pb.EmptyMsg()
        # Call SDK method through rpc channel client
        response = self.service_stub.read_temperatures(self.rpc_controller,request)

        temps = (response.cj_temp, response.lin_temp)

        return temps
    
    def read_faults(self,filter_at_fault = True):
        """read_faults method for sdk tc module"""
        request = tc_pb.FilterFaults()
        request.filter_at_fault = filter_at_fault

        # Call SDK method through rpc channel client
        response = self.service_stub.read_faults(self.rpc_controller,request)

        result_dict = self._generate_faults_dict(response)

        return result_dict

    def clear_faults(self):
        """clear_faults method for sdk tc module"""
        request = tc_pb.EmptyMsg()

        # Call SDK method through rpc channel client
        response = self.service_stub.clear_faults(self.rpc_controller,request)

        return response.content

