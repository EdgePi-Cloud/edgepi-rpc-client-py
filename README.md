![Image](https://user-images.githubusercontent.com/3793563/207438826-bb656ca5-f19d-4699-8cb4-35acccb2ce58.svg)

# EdgePi RPC Client

The RPC client exposes functionality of the EdgePi Python SDK to be used over either a network connection or on local sockets, allowing for potential remote control of the EdgePi.

Since the client directly mirrors the SDK, you can take advantage of the user-friendly SDK functionality with the flexibility of different connection protocols depending on your specific use case.

You can learn more about the Python SDK [here](https://github.com/EdgePi-Cloud/edgepi-python-sdk).

# Using the RPC Client

Install the RPC client through the terminal:

```
$ python3 -m pip install edgepi-rpc-client
```

Once installed, you can control the modules of the EdgePi directly through the SDK's wide functionality.

For example, from a remote connection with address `localhost` and port `5555`, initialize a client module as:

```python
from edgepi_rpc_client.services.adc.client_adc_service import ClientAdcService
from edgepi_rpc_client.services.adc.adc_pb_enums import ADCChannel, ConvMode

# initialize ADC Client
adc_client = ClientAdcService('tcp://localhost:5555')

# configure ADC to sample input pin 4 (the input pins are 0-indexed)
adc_client.set_config(adc_1_analog_in=ADCChannel.AIN3, conversion_mode=ConvMode.CONTINUOUS)

# send command to start automatic conversions
adc_client.start_conversions()

# perform 10 voltage reads
for _ in range(10):
  out = adc_client.read_voltage()
  print(out)

# stop automatic conversions
adc_client.stop_conversions()
```

Once the client is initialized you can control the EdgePi exactly as you would through the SDK.

For details about available modules visit the SDK GitHub repository linked above.
