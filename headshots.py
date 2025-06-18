import cv2
import os
from picamera2 import Picamera2
name = 'Tristen' #replace with your name

folder_path = f"Datasets/{name}"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "RGB888", "size":(640, 480)}))
picam2.start()


cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    frame = picam2.capture_array()
    cv2.imshow("press space to take a photo", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("Escape hit, closing...")
        break
    elif key % 256 ==32:
        img_name = f"Datasets/{name}/image_{img_counter}.jpg"
        cv2.imwrite(img_name,frame)
        print(f"{img_name} written!")
        img_counter += 1
        
cv2.destroyAllWindows()
picam2.stop()
