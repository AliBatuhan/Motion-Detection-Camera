# Motion Detection Camera
This code captures video feed from a laptop camera and performs motion detection by comparing each frame of the video feed to a reference frame, which is the first frame of the video. If there is any movement within the frame, the code will save a snapshot of the frame and send it to a designated email address.

## Requirements
* cv2 (OpenCV)
* time
* emailing (email sending module)
* glob
* os
* threading
## Usage
Connect a laptop camera or external webcam to your device.
Run the code using a Python environment.
The code will start capturing video feed from the camera.
If there is any movement within the frame, the code will save a snapshot of the frame and send it to a designated email address.
To exit the code, press the "q" key on your keyboard.
## Note
The code is set to send an email with the snapshot of the frame if movement is detected, but the email sending function needs to be implemented in the emailing module.
The code is set to detect objects with a minimum contour area of 10000 pixels. This value can be adjusted to suit your needs.


