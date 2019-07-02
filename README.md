# music_control_raspberry_pi_mm

These are some scripts to play music on your Rasperry Pi / Magic Mirror, you can even program your google assistant to run these scripts
with the personalised traits.

https://developers.google.com/assistant/sdk/guides/library/python/extend/custom-actions

To use it this your need mpv and socat, to install them run on your Raspberry Pi terminal

sudo apt-get install mpv

sudo apt-get install socat

There are the music.py python scripts that detects when an usb is plugged and start playing music with a playlist it mades, and the bash scripts
to start music, quit , pause, unpause, next and previous songs.
