#!/usr/bin/env python3

#import gi
#gi.require_version('Notify', '0.7')
#from gi.repository import Notify
import os
import time

def main():
    #Notify.init("Test")
    
    while True:

        os.system("echo ceva >> /home/$USER/Desktop/test.txt")
    
    #    notification = Notify.Notification.new(
    #        "Notificarea ta din 20 in 20 de secunde", 
    #        "┗(＾0＾)┓"   
    #    )
    #    notification.set_urgency(0)
    #    notification.show()/home/pavel/Desktop/test.txt 

        time.sleep(20)

    #Notify.uninit("Test")

if __name__ == "__main__":
    main()