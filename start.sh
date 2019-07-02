#!/bin/sh
if [ $# -eq 0 ]; then
    echo "Starts an mpv media server, playing the supplied file"
    echo "Usage: start.sh <media file>"
    exit 1
fi
mpv --playlist=$1 --loop=inf --shuffle --input-ipc-server=~/mpvsocket
