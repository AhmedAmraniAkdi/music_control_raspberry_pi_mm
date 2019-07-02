# Program that detects when an usb is plugged, makes a playlist of all mp3 files in it and starts playing music.
# I used it with magic mirror + google assistant to be able to control the music by voice commands.
# Ahmed Amrani

import pyudev
import psutil
import time
import os
import glob

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

mountpoint = ''


def loop():
    loop_control1 = 0
    loop_control2 = 0
    pathname = ''
    number_songs = 0
    for dev in iter(monitor.poll, None):
    #while(True):
    #   action,dev = monitor.receive_device()
        if dev.action == 'add' and loop_control1 == 0:
            loop_control1 = 1
            loop_control2 = 0
            print("USB inserted\n")
            print("start sleep")
            time.sleep(3)
            print("stop sleep")
            partitions = [dev.device_node for dev in context.list_devices(subsystem='block', DEVTYPE='partition', parent=dev)]
            print("All removable partitions: {}".format(", ".join(partitions)))
            for p in psutil.disk_partitions():
                if p.device in partitions:
                    print("  {}: {}".format(p.device, p.mountpoint))
                    number_songs,pathname = playlistMaker(p.mountpoint)
                    print(pathname)
                    time.sleep(3)
            if number_songs > 0:
                print('playing music')
                os.system("/home/pi/mpv-control/start.sh" +" "+ pathname +" &")
                print('start')
        if dev.action == 'remove' and loop_control2 == 0:
            loop_control1 = 0
            loop_control2 = 1
            print("USB detached\n")
            print("quitting music")
            os.system("/home/pi/mpv-control/quit.sh")
            #os.system("pkill mpv")
            

#def music_files(mountpoint):
#    for file in os.listdir(mountpoint):
#        if file.endswith(".mp3"):
#            print (os.path.join(mountpoint,file))
#            os.system("/home/pi/mpv-control/start.sh" +" "+ os.path.join(mountpoint,file))
#            time.sleep(50)

def playlistMaker(mountpoint):
    number_songs = 0
    for (path, subdirs, files) in os.walk(mountpoint):
        os.chdir(path)
        if glob.glob("*.mp3") != []:
            pathname = os.path.split(path)[1] + ".m3u"
            _m3u = open( os.path.split(path)[1] + ".m3u" , "w" )
            for song in glob.glob("*.mp3"):
                number_songs = number_songs + 1
                _m3u.write(song + "\n")
            _m3u.close()
        return number_songs,pathname

#mountpoint = loop()
#print("{}:".format(mountpoint))
#playlistMaker(mountpoint)

def main():
    loop()

if __name__ == '__main__':
    main()
