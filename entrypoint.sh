#!/bin/bash
set -e

# Source environment bawaan ROS 2
source "/opt/ros/humble/setup.bash"

# Source workspace jika sudah di-build
if [ -f "/ws/install/setup.bash" ]; then
    source "/ws/install/setup.bash"
fi

exec "$@"

