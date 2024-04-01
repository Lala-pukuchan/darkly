FROM ubuntu:latest

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install hydra
RUN apt-get update && apt-get install -y hydra

# Copy the hydra command script into the container
COPY run_hydra.sh /usr/local/bin/run_hydra.sh

# Give execution rights on the script
RUN chmod +x /usr/local/bin/run_hydra.sh

# Set the entrypoint to the hydra script
# This can be overridden if necessary
ENTRYPOINT ["/usr/local/bin/run_hydra.sh"]
