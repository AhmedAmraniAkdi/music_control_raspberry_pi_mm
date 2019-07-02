#!/bin/sh
echo 'quit' | socat - ~/mpvsocket
pkill mpv