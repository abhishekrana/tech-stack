#!/bin/bash

set -e

# Install dev dependencies
task install:helm
task install:k3d
task install:k9s
task install:kubectl
task install:tilt

# Create k8s cluster
cd k8s/deployments/local
task delete-k3d
task create-k3d
task install-postgresql

# Run migrations
# Port forward postgresql
