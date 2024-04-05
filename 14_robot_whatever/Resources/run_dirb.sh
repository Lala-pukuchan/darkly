#!/bin/bash

# Example Dirb command. Replace the URL with the one you wish to scan.
# Note: Running Dirb against websites without permission is illegal.
dirb http://192.168.56.101 ./common_path.txt

# Keep the container running (optional)
# tail -f /dev/null
