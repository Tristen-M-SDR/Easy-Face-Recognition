# Simple-Facial-Recognition

Perform simple facial recognition tasks using OpenCV and the widely used face-recognition Python library for **Raspberry Pi OS (Bookworm)**. 

## 1. Install Face-Recognition Library: 


**Step 1:** Create Virtual Environment
<pre>
  mkdir face_rec
  python3 -m venv my_env --system-site-packages
  source my_env/bin/activate
</pre>
  
**Step 2:** Install dependancies

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
    libopenblas-dev \
    libblas-dev \
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


**Step 2:** Build and install dlib
<pre>
  cd
  git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git
  cd ./dlib
  sudo python3 setup.py install --compiler-flags "-mfpu=neon"
  cd
</pre>

Note: You should see something about "is_alive".


**Step 3:** Install face_recognition

<pre>
  pip3 install face_recognition 
    opencv-python \
    imutils \
    numpy==1.24.4 
</pre>

## 2. Install Additional Libaries: 

**Step 1:** Install PiCamera2 package

<pre>
  sudo apt update
  sudo apt install -y python3-picamera2
</pre>  

**Step 2:** Install rpicam for PiCamera

<pre>
  sudo apt install rpicam-apps
</pre>

You can test the PiCamera using the following command:

<pre>
  rpicam-hello
</pre>

## 3. Setting up the Real-Time Face-Recognition
**Step 1:** Download and navigate to the files using the following command:

<pre>
  cd Downloads/
  git clone https://github.com/Tristen-M-SDR/Easy-Face-Recognition
  cd Easy-Face-Recognition/
</pre>

**Step 2:** Open the Datasets folder and delete the dummy file inside by running this command:

<pre>
  cd Datasets/rename
  rm delete_this.png
  cd ..
</pre>

**Step 3:** Rename the "**rename**" file to your name by copy/pasting this command in the Terminal and the replacing `type_in_your_name_here` with your name.

<pre>
  mv rename type_in_your_name_here
</pre>


**Step 4:** Open `headshots.py` code by running this command:

<pre>
  cd ..
  nano headshots.py
</pre>

and change the name to your name by navigating using the arrow keys. Save and exit (Use `Ctrl+O` to save, press `ENTER`, and `Ctrl+X` to exit).

**Step 5:** Run the headshots.py and use the "**space bar**" to take pictures of your face from multiple angles. Close the frame by pressing the **"q"** key on your keyboard. You can run `headshots.py` using the following command:

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
