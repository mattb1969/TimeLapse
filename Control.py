################################################################################
#
#   T I M E   L A P S E   P H O T O G R A P H Y
#
#       Matthew Bennett
#
################################################################################
#
#   Take a picture every nnn seconds and create a video afterwards
#       nn is defined in the top of the file
#
################################################################################
#
#   To convert the images to a time lapse video use avconv.
#       This needs to be installed 'sudo apt-get install libav-tools'
#
#

# Import classes
from cl_DiskOperations import *
from cl_Photography import *

# Import functions
import time
from datetime import datetime
from datetime import timedelta

# Settings
time_lapse = 6 #3600       # The time in seconds between each picture being taken
start_time = datetime.strptime('05:00:00', "%H:%M:%S")
stop_time = datetime.strptime('22:10:00', "%H:%M:%S")
use_time = True

global img_counter
img_counter = 0

def within_time(time_now):
    """
    Function checks
        1. The use_time flag is set
            if False, return True
        2. Check the current time is within the time window selected.
            Returns True if within the window
    """
    if use_time:
        # Get the current time, set the date to 1/1/1900 because start and stop times default to this date
        just_now = time_now.replace(year=1900, month=1, day=1)
        #print("Checking time (start:now:stop) %s:%s:%s" % (start_time, just_now, stop_time))
        if just_now > start_time and just_now < stop_time:
            return True
    else:
        return True
    return False
   
def image_name_date(time_now):
    """
    Generate a unique time based on the time given
    """
    im_name = ("picture-%04d%02d%02d%02d%02d%02d.jpg" % 
        (time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second))
    return im_name_date

def image_name():
    """
    Generate the next image name.
    """
    global img_counter
    im_name = ("picture-%08d.jpg" % img_counter)
    img_counter = img_counter + 1
    while(DiskOperations.FileExists(im_name)):
        im_name = ("picture-%08d.jpg" % img_counter)
        img_counter = img_counter + 1
        #print("Finding first free filename")			# Added for Debug
    return im_name

def main():
    
    running = True          # Set to True when the routine is capturing images
    last_capture = datetime.now().replace(year=2000, month=1, day=1)
            # The time of the last capture, set to a really old date to force the first capture
    picture = Photography((1280,720),30)
    
    while (running == True):
        now = datetime.now()
        if within_time(now):
            # After time since last image taken
            if now - last_capture > timedelta(seconds = time_lapse):
                #img_name = image_name(now)
                img_name = image_name()
                # Take and store picture
                # start_preview
                picture.startpreview()
                picture.setiso = 400
                # wait a bit for the camera to settle
                picture.ledmode('off')
                time.sleep(3)
                picture.setshutterspeed = picture.readexposurespeed
                picture.setexposuremode('off')
                gain = picture.readawbgains()
                picture.setawbmode('off')
                picture.setawbgains(gain)
                # capture
                picture.takephoto(img_name)
                print("Image Captured:%s" % img_name)
                picture.__exit__()
                last_capture = datetime.now()
            else:
                # Need to wait a while before taking the next image
                next_pic = last_capture + timedelta(seconds=time_lapse)
                wait_time = next_pic - now
                #print("Wait Time:%s" % wait_time.seconds)
                delay_time = wait_time.seconds - 5              # Allows for the processing time
                if delay_time < 0.1:                            # If it is negative, make it a small number
                    delay_time = 0.1
                time.sleep(delay_time)
        else:
            # Need to wait until within time again.
            wait_time = start_time - datetime.now().replace(year=1900, month=1, day=1)
            #print("Overnight Wait Time:%s" % wait_time.seconds)
            delay_time = wait_time.seconds - 5              # Allows for the processing time
            if delay_time < 0.1:                            # If it is negative, make it a small number
                delay_time = 0.1
            time.sleep(delay_time)
                

        # Need an exit routine to set running = False
        #   keyboard input
        #   disk space
        #   close
        DiskOperations.KeepDiskSpaceFree(1024)
    
    return

if __name__ == '__main__':
    main()
