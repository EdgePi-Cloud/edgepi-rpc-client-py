"""Client Build Integration Test"""
import subprocess
import os

def test_rpc_client_install():
    """Test client import"""
    # Build the wheel
    subprocess.check_call(["pip3", "install", "build"])
    subprocess.check_call(["python", "-m", "build"])

    # Locate the wheel in the dist directory
    wheel_file = next((file for file in os.listdir("dist") if file.endswith(".whl")), None)
    assert wheel_file, "Wheel file not found"

    # Install the wheel
    subprocess.check_call(["pip3", "install", os.path.join("dist", wheel_file)])

    # Check imports
    # pylint: disable=import-outside-toplevel, unused-import
    from edgepi_rpc_client.services.led.client_led_service import ClientLEDService
    from edgepi_rpc_client.services.led.led_pb_enums import LEDPins
