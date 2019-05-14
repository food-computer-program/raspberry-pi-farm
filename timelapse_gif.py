# import libraries
from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
# change the camera resolution so that it won't take too long to process
# when we compile all of our photos into a gif
camera.resolution = (1024, 768)

# preview what we can see from our camera module
camera.start_preview()

# write a for loop to capture several photos in a row
# in this example, we're taking 5 photos and stitching them together into a gif
for i in range(5):
    # the next line allows us to save and take ("capture") the photo
    # and save each photo with a different naming convention so that we can save all of them
    camera.capture(‘/home/pi/Desktop/photo{0:04d}.jpg’.format(i))
    # we "sleep" for 3 seconds in between each photo
    sleep(3)
# turn off the camera module preview after we've taken all 5 photos
camera.stop_preview()

# stitch all of our photos together in a continuous loop ( -loop 0)
# showing each photo for 10 milliseconds each (-delay 10)
# then save it as "animation.gif"
system(‘convert –delay 10 –loop 0 /home/pi/Desktop/photo*.jpg /home/pi/Desktop/animation.gif’)

# print out a statement to let us know that our gif is finished!
print(‘check out your gif!’)
