# Simple-Facial-Recognition
Perform simple facial recognition tasks using OpenCV and the widely used face-recognition Python library. 

1. Please begin by visiting the following the link to install face-recognition library and following steps

https://gist.github.com/mrpjevans/9885e853b603ed046cbc5326b9942991


2. Please run the following commands to install the following libaries: 



**Install Opencv package**
<pre>
sudo pip3 install opencv-python --break-system-packages
</pre>
You can test if the OpenCV has been successfully installed with the following command: 
<pre> 
python3 -c "import cv2; print(cv2.__version__)"
</pre>

**Install imutils package**

sudo pip3 install imutils --break-system-packages

python3 -c "import imutils; print('imutils imported successfully')"

**Install libcamera for PiCamera**

sudo apt update
sudo apt install libcamera-apps


2. Open the Datasets folder and rename the your_name file to your name, and delete the dummy file inside. 

3. Open headshots.py code and change the name to your name.

4. Run the headshots.py and use the **space** bar to take pictures of your face from multiple angles. Close the frame by pressing the **"q"** key on your keyboard.

5. Run the train_model.py code.

6. Run the facial_rec_simple.py code and observe as it draws a bounding box around your face and labels it with your name. 
