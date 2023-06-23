"""
Client for led service. Utilizes ClientRpcChannel to send/receive and
serialize/deserialize messages
"""
from rpc_module.protos import led_pb2 as led_pb
from client.client_rpc_channel.client_rpc_channel import ClientRpcChannel
from client.client_services.led.led_pb_enums import LEDPins

SOCKET_ENDPOINT = "ipc:///tmp/edgepi.pipe"

# pylint: disable=no-member
class ClientLEDService():
    """Client methods for LED service"""
    def __init__(self):
        self.client_rpc_channel = ClientRpcChannel(SOCKET_ENDPOINT)
        self.service_stub = led_pb.LEDService_Stub(self.client_rpc_channel)
        self.rpc_controller = None

    def turn_led_on(self, led_name: LEDPins):
        """turn_on led method for sdk led module"""
        request = led_pb.LEDName(
            led_name = led_name.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.turn_on(self.rpc_controller,request)

        return response.content

    def turn_led_off(self, led_name: LEDPins):
        """turn_off led method for sdk led module"""
        request = led_pb.LEDName(
            led_name = led_name.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.turn_off(self.rpc_controller,request)

        return response.content

    def toggle_led(self, led_name: LEDPins):
        """toggle_led method for sdk led module"""
        request = led_pb.LEDName(
            led_name = led_name.value
        )
        # Call SDK method through rpc channel client
        response = self.service_stub.toggle_led(self.rpc_controller,request)

        return response.content
