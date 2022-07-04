Hi, my name is Krishay, and I'm building the security camera using Raspberry Pi

-----

File info:

- **camera.py**: This file contains code for the camera module, and the main class in this file, `VideoCamera`, has some methods for object detection. For example, the `get_object()` method returns an image and a boolean that says whether the object was found or not.

- **facial_recognition_model.xml**: In this file, there is just some data stored for detecting faces.

- **mail.py**: Here, there is code for emailing security updates. Whenever something is detected through the feed, the `sendEmail()` method runs. First, it starts to build the email, and it adds the image of the object as well as a title for the email. After that, it logs in to the sending email account and sends the message to the specified address.

- **main.py**: To use the security camera, this file should be ran by typing `python main.py`. First, it defines some variables and imports packages such as OpenCV for object detection and BasicAuth for enforcing access to websites (needed for logging into Gmail).<br><br>One of the methods in this file is the `check_for_objects()` method. It determines if something was detected and whether an email was sent previously in a given time interval. If the object was detected and no message was sent recently, then it sends the email with the information.
