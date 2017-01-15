try:
      import Image
except ImportError:
      from PIL import Image
import pytesseract
from translate import translator
import cv2

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
 
def get_image():
 retval, im = camera.read()
 return im
 
for i in range(ramp_frames):
 temp = get_image()
print("Taking image...")
camera_capture = get_image()
file = "test_image.png"

cv2.imwrite(file, camera_capture)
del(camera)

im = Image.open('test_image.png')
print(pytesseract.image_to_string(im))
#english=pytesseract.image_to_string(Image.open('test_image.png'))
print(translator('en','hi',"Hello World"))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
