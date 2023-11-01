"""Client for PWM service"""
import logging
from edgepirpc.protos import pwm_pb2 as pwm_pb
from edgepi_rpc_client.client_rpc_channel import ClientRpcChannel
from edgepi_rpc_client.util.helpers import (
    filter_arg_values, create_config_request_from_args, get_server_response
)
from edgepi_rpc_client.services.pwm.pwm_pb_enums import PWMPins, Polarity

_logger = logging.getLogger(__name__)

# pylint: disable=no-member
class ClientPWMService():
    """Client Methods for PWM Service"""
    def __init__(self, transport):
        self.client_rpc_channel = ClientRpcChannel(transport)
        self.service_stub = pwm_pb.PWMService_Stub(self.client_rpc_channel)
        self.rpc_controller = None

    # pylint: disable=unused-argument
    def set_config(self, pwm_num: PWMPins,
                   frequency: float = None,
                   duty_cycle: float = None,
                   polarity: Polarity = None):
        """set_config method for SDK PWM module"""
        config_args_dict = filter_arg_values(locals(), 'self', None)
        config_msg = pwm_pb.Config()
        arg_msg = pwm_pb.Config().ConfArg()

        request = create_config_request_from_args(config_msg, arg_msg, config_args_dict)
        rpc_response = self.service_stub.set_config(self.rpc_controller,request)
        response = get_server_response(rpc_response, pwm_pb.SuccessMsg)
        return response.content

    def enable(self, pwm_num: PWMPins):
        """enable method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.enable(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.SuccessMsg)
        return response.content

    def disable(self, pwm_num: PWMPins):
        """disable method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.disable(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.SuccessMsg)
        return response.content

    def close(self, pwm_num: PWMPins):
        """close method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.close(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.SuccessMsg)
        return response.content

    def init_pwm(self, pwm_num: PWMPins):
        """init_pwm method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.init_pwm(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.SuccessMsg)
        return response.content

    def get_frequency(self, pwm_num: PWMPins):
        """get_frequency method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.get_frequency(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.GetFrequency)
        return response.frequency

    def get_duty_cycle(self, pwm_num: PWMPins):
        """get_duty_cycle method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.get_duty_cycle(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.GetDutyCycle)
        return response.duty_cycle

    def get_polarity(self, pwm_num: PWMPins):
        """get_polarity method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)

        rpc_response = self.service_stub.get_polarity(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.GetPolarity)
        return Polarity(response.polarity)

    def get_enabled(self, pwm_num: PWMPins):
        """get_enabled method for SDK PWM module"""
        request = pwm_pb.PWM(pwm_num = pwm_num.value)
        rpc_response = self.service_stub.get_enabled(self.rpc_controller, request)
        response = get_server_response(rpc_response, pwm_pb.GetEnabled)
        return response.enabled
