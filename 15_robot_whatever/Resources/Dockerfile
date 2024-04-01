# Use an official Ubuntu base image
FROM ubuntu:latest

# Avoid prompts from apt during build
ARG DEBIAN_FRONTEND=noninteractive

# Update packages and install Dirb
RUN apt-get update && \
    apt-get install -y dirb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the Dirb script into the container
COPY run_dirb.sh /usr/local/bin/run_dirb.sh
COPY common_path.txt /usr/local/bin/common_path.txt

# Make the script executable
RUN chmod +x /usr/local/bin/run_dirb.sh

# Default command to execute when the container starts
CMD ["/usr/local/bin/run_dirb.sh"]
