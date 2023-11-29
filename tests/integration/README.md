## Necessary environment for running the integration tests:

The EdgePi RPC server must be installed on the EdgePi for the integration tests to run.

Check if the server is installed:

```
sudo systemctl status edgepi-rpc-server
```

If not already installed, install the server through the following commands:

```
wget -qO - https://deb.edgepi.com/edgepi-release.gpg | sudo gpg --dearmor -o /usr/share/keyrings/edgepi-release.gpg

sudo tee /etc/apt/sources.list.d/edgepi.list >/dev/null <<'EOF'
deb [arch=arm64, signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/main bullseye main
#deb [arch=arm64, signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/test bullseye test
#deb [arch=arm64, signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/nightly bullseye nightly
EOF

sudo apt update

sudo apt install edgepi-rpc-server

sudo reboot
```