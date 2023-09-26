#!/bin/bash

echo "before key"

wget -qO - https://deb.edgepi.com/edgepi-release.gpg | sudo gpg --dearmor -o /usr/share/keyrings/edgepi-release.gpg

echo "before repo"

sudo tee /etc/apt/sources.list.d/edgepi.list >/dev/null <<'EOF'
deb [signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/main bullseye main
deb [signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/test bullseye test
deb [signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/nightly bullseye nightly
EOF

echo "before update"
sudo apt-get update

echo "dumping repo contents"

apt-cache pkgnames | grep '^edge'

echo "before policy"

apt-cache policy apt
apt-cache policy edgepi-rpc-server

apt-cache policy edgepi-linux-config
apt-cache policy edgepi-aws-iot
apt-cache policy edgepi-data-collector
apt-cache policy edgepi-data-aggregator
apt-cache policy edgepi-device-manager

echo "before install"

sudo apt-get install edgepi-rpc-server
