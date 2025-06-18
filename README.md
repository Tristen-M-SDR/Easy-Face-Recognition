# Simple-Facial-Recognition
Perform simple facial recognition tasks using OpenCV and the widely used face-recognition Python library. 

## 1. Please begin by visiting the following the link to install face-recognition library and following steps



https://gist.github.com/mrpjevans/9885e853b603ed046cbc5326b9942991

**Step 1: Install dependancies**

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

**Step 2: Increase the swap file size so we can build dlib**

<pre>
  sudo nano /etc/dphys-swapfile
</pre>

Find `CONF_SWAPSIZE` and change its value from `100` to `1024`. Save and exit then run this command:

<pre>
  sudo /etc/init.d/dphys-swapfile restart
</pre>

**Step 3: Build and install dlib**
<pre>
  cd
  git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git
  cd ./dlib
  sudo python3 setup.py install --compiler-flags "-mfpu=neon"
</pre>

**Step 4: Revert the swap size**
<pre>
  sudo nano /etc/dphys-swapfile
</pre>
Find `CONF_SWAPSIZE` and change its value from `1024` to `100`. Save and exit then run this command:

<pre>
  sudo /etc/init.d/dphys-swapfile restart
</pre>

**Step 5: Install face_recognition and examples**

<pre>
  sudo pip3 install face_recognition
</pre>

## 2. Please run the following commands to install the following libaries: 

**Install PiCamera2 package**

<pre>
  sudo apt update
  sudo apt install -y python3-picamera2
</pre>  


**Install OpenCV package**

<pre>
  sudo pip3 install opencv-python --break-system-packages
</pre>

You can test if the **OpenCV** has been successfully installed with the following command: 

<pre>
  python3 -c "import cv2; print(cv2.__version__)"
</pre>

**Install imutils package**
<pre>
  sudo pip3 install imutils --break-system-packages
</pre>

You can test if **imutils** package installed properly by running the following command: 

<pre>
  python3 -c "import imutils; print('imutils imported successfully')"
</pre>

**Install libcamera for PiCamera**

<pre>
  sudo apt install libcamera-apps
</pre>

You can test the PiCamera using the following command:

<pre>
  libcamera-hello
</pre>

## 3. Open the **Datasets** folder and rename the **your_name** file to your name, and **delete** the dummy file inside. 

## 4. Open **headshots.py** code and change the name to your name.

## 5. Run the **headshots.py** and use the **space** bar to take pictures of your face from multiple angles. Close the frame by pressing the **"q"** key on your keyboard.

## 6. Run the train_model.py code.

## 7. Run the facial_rec_simple.py code and observe as it draws a bounding box around your face and labels it with your name. 
