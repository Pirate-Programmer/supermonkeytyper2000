from pynput import keyboard
from PIL import Image
import pytesseract as tess
from time import sleep
import os
from glob import glob

#works gud with short and medium paras on monkeytype
#for long and more text doesnt show up in single image
#try a theme where curson is barely visible and text is clear 
#could messup on punctuation


#Properties 

#path to tesseract.exe
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#adjust typing speed
delay = 0.02

#Path to Image directory
Path = r"C:\Users\Skeletron\Pictures\Screenshots".rstrip("\\/")



#looks for .png and .jpg file
#returns the most recent file in the dir
def fetchImage():
    if not os.path.isdir(Path):
        print("path: {Path} is not a directory")
        exit(1)
    
    file_list = glob(Path+"/*.png") + glob(Path+"/*.jpg")
    return None if len(file_list) == 0 else max(file_list,key=os.path.getctime)


#get text from screenshot
def get_text(img) -> str:
    if img is None:
        print("No image found D:")
        return ""
    
    print("Reading Text from Image...")
    img = Image.open(img)
    text = tess.image_to_string(img)
    return text

#smack em keys
def supermonkeytyper2000(text):
    strokeMaster = keyboard.Controller()
    for line in text.splitlines():
        for c in line:
            if c == " ":
                strokeMaster.tap(keyboard.Key.space)
            else:
                strokeMaster.tap(c)
            sleep(delay)
        strokeMaster.tap(keyboard.Key.space)


#setup Keyboard Listener thread

#check if f8 has been pressed
def on_press(key):
    if key == keyboard.Key.f8:
        sleep(0.5)
        img = fetchImage()
        text = get_text(img)
        print(text.splitlines())
        supermonkeytyper2000(text)

#exit listener when esc key hit
#note when controller is typing keystrokes, unable to exit
#gotta kill the script in such case
def on_release(key):
    return not key == keyboard.Key.esc
        
#threaderuni
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
