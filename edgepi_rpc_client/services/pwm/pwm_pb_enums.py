"""Client enums to protobuf PWM enums"""
from enum import Enum
from python_rpc.rpc_generated_protobufs import pwm_pb2 as pwm_pb

class PWMPins(Enum):
    """PWMPins Enum"""
    PWM1 = pwm_pb.PWMPins.PWM1
    PWM2 = pwm_pb.PWMPins.PWM2

class Polarity(Enum):
    """Polarity Enum"""
    NORMAL = pwm_pb.Polarity.NORMAL
    INVERSED = pwm_pb.Polarity.INVERSED
