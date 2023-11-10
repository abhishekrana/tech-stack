#!/bin/bash

set -e

# Install dev dependencies
task install:helm
task install:k3d
task install:k9s
task install:kubectl
task install:tilt

# Generate helm charts
pushd k8s/charts/tech-stack
task update-dependency
popd

# Create k8s cluster
pushd k8s/deployments/local
task uninstall-k3d
task install-k3d
task install-dependencies
popd
