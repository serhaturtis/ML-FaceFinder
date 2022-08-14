#!/bin/bash

if [ -z "$1" ] && [ -z "$2" ]
then
	echo "Usage: find.sh <workspace> <threshold>"
else
	HOST_WORKSPACE="$(cd "$(dirname "$1")"; pwd)/$(basename "$1")"
	echo "Workspace path: ${HOST_WORKSPACE}"

	docker context use rootless
	docker run --volume $HOST_WORKSPACE:/workspace \
	--workdir /workspace \
	face_finder python3 /workspace/face_finder.py -t /workspace/target -s /workspace/search -p $2
fi
