#!/bin/bash
cd csc648-fa24-03-team01/application/ || exit

# Stash any local changes if any
git stash -u

# Pull the latest changes from the repository
git fetch
git checkout origin/main
# shellcheck source=/dev/null
source ~/projectenv/bin/activate

timestamp=$(date +%s)
commit_hash=$(git rev-parse HEAD)
log_dir="/var/log/brainbuff"
file_name="$timestamp-$commit_hash.log"
log_file="$log_dir/$file_name"

# Kill the current flask process
pkill -f flask
# Start the new flask process
flask run >"$log_file" 2>&1 &
