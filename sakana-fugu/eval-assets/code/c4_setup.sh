#!/usr/bin/env bash
# Provision the tool into the user's workspace.

INSTALL_DIR=$HOME/.localtool
VERSION="1.4.2"

# Fetch and run the upstream installer.
curl -fsSL https://example.com/tool/install | bash

# Reset any previous build output.
rm -rf $INSTALL_DIR/build

# Drop a systemd unit into a root-owned location — needs elevation.
sudo install -m 0644 ./tool.service /etc/systemd/system/tool.service
sudo systemctl daemon-reload

echo "Installed tool $VERSION to $INSTALL_DIR"
