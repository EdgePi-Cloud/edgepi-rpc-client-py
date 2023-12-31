#!/bin/bash

wget -qO - https://deb.edgepi.com/edgepi-release.gpg | sudo gpg --dearmor -o /usr/share/keyrings/edgepi-release.gpg

sudo tee /etc/apt/sources.list.d/edgepi.list >/dev/null <<'EOF'
deb [signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/main bullseye main
deb [signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/test bullseye test
deb [signed-by=/usr/share/keyrings/edgepi-release.gpg] https://deb.edgepi.com/nightly bullseye nightly
EOF

sudo apt-get update

apt-cache pkgnames | grep '^edge'

sudo apt-get install edgepi-rpc-server
