# Simple-Facial-Recognition
Perform simple facial recognition tasks using OpenCV and the widely used face-recognition Python library. 

## 1. Install Face-Recognition Library: 

**Step 1:** Install dependancies

<pre>
  sudo apt -y update && sudo apt -y full-upgrade
  sudo apt install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip \
    python3-picamera2
</pre>

**Step 2:** Increase the swap file size so we can build dlib

<pre>
  sudo nano /etc/dphys-swapfile
</pre>

Find `CONF_SWAPSIZE` and change its value from `100` to `1024` by navigating using the arrow keys. Save and exit (Use `Ctrl+O` to save, press `ENTER`, and `Ctrl+X` to exit) then run this command:

<pre>
  sudo /etc/init.d/dphys-swapfile restart
</pre>

**Step 3:** Build and install dlib
<pre>
  cd
  git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git
  cd ./dlib
  sudo python3 setup.py install --compiler-flags "-mfpu=neon"
</pre>

Note: You should see something about "is_alive"

**Step 4:** Revert the swap size
<pre>
  sudo nano /etc/dphys-swapfile
</pre>
Find `CONF_SWAPSIZE` and change its value from `1024` to `100` by navigating using the arrow keys. Save and exit (Use `Ctrl+O` to save, press `ENTER`, and `Ctrl+X` to exit) then run this command:

<pre>
  sudo /etc/init.d/dphys-swapfile restart
</pre>

**Step 5:** Install face_recognition

<pre>
  sudo pip3 install face_recognition --break-system-packages
</pre>

## 2. Install Additional Libaries: 

**Step 1:** Install PiCamera2 package

<pre>
  sudo apt update
  sudo apt install -y python3-picamera2
</pre>  


**Step 2:** Install OpenCV package

<pre>
  sudo pip3 install opencv-python --break-system-packages
</pre>

You can test if the **OpenCV** has been successfully installed with the following command: 

<pre>
  python3 -c "import cv2; print(cv2.__version__)"
</pre>

**Step 3:** Install imutils package
<pre>
  sudo pip3 install imutils --break-system-packages
</pre>

You can test if **imutils** package installed properly by running the following command: 

<pre>
  python3 -c "import imutils; print('imutils imported successfully')"
</pre>

**Step 4:** Install libcamera for PiCamera

<pre>
  sudo apt install libcamera-apps
</pre>

You can test the PiCamera using the following command:

<pre>
  libcamera-hello
</pre>

## 3. Setting up the Real-Time Face-Recognition
**Step 1:** Download the zip file, you can do this by clicking on the "Code" drop down menu, and then select download zip file.

**Step 2:** You want to navigate to your Downloads folder and extract the downloaded zip file.

**Step 3:** Open the Datasets folder and rename the your_name file to your name, and delete the dummy file inside. 

**Step 4:** Open `headshots.py` code and change the name to your name. Save it. 

**Step 5:** Run the headshots.py and use the **space bar** to take pictures of your face from multiple angles. Close the frame by pressing the **"q"** key on your keyboard. You can run `headshots.py` using the following command:

<pre>
  python3 headshots.py
</pre>

**Step 6:** Run the `train_model.py` code. You can run `train_model.py` using the following command:

<pre>
  python3 train_model.py
</pre>


**Step 7:** Run the facial_rec_simple.py code and observe as it draws a bounding box around your face and labels it with your name. You can run `facial_rec_simple.py` using the following command:

<pre>
  python3 facial_rec_simple.py
</pre>
