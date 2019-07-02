#!/bin/sh
echo '{ "command": ["set_property", "pause", false] }' | socat - ~/mpvsocket
