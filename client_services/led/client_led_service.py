"""
Client for led service. Utilizes ClientRpcChannel to send/receive and
serialize/deserialize messages
"""
from edgepirpc.protos import led_pb2 as led_pb
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel
from client.client_services.led.led_pb_enums import LEDPins

# pylint: disable=no-member
class ClientLEDService():
    """Client methods for LED service"""
    def __init__(self, transport):
        self.client_rpc_channel = ClientRpcChannel(transport)
        self.service_stub = led_pb.LEDService_Stub(self.client_rpc_channel)
        self.rpc_controller = None

    def turn_led_on(self, led_pin: LEDPins):
        """turn_on led method for sdk led module"""
        request = led_pb.LEDPin(
            led_pin = led_pin.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.turn_led_on(self.rpc_controller,request)

        return response.content

    def turn_led_off(self, led_pin: LEDPins):
        """turn_off led method for sdk led module"""
        request = led_pb.LEDPin(
            led_pin = led_pin.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.turn_led_off(self.rpc_controller,request)

        return response.content

    def toggle_led(self, led_pin: LEDPins):
        """toggle_led method for sdk led module"""
        request = led_pb.LEDPin(
            led_pin = led_pin.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.toggle_led(self.rpc_controller,request)

        return response.content
