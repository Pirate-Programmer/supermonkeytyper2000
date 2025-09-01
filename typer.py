from pynput import keyboard
from PIL import Image,ImageGrab
import pytesseract as tess
from time import sleep


#works gud with short and medium paras on monkeytype
#for long and more text doesnt show up in single image
#try a theme where curson is barely visible and text is clear (tested with theme 'iv clover')



#Properties 

#path to tesseract.exe
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#top left (x,y) , bottom right (x,y)
crop = (150,530,1800,710)

#adjust typing speed
delay = 0.1


#capture screenshot
def screenshot() -> None:
    print("grabing screenshot...")
    screen = ImageGrab.grab()
    screen = screen.crop(crop) #crop size can vary according to screen res
    screen.save("screen.png")

#get text from screenshot
def get_text(img) -> str:
    print("Reading Text from screenshot...")
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
    print("hehe")


#setup Keyboard Listener thread

#check if f8 has been pressed
def on_press(key):
    if key == keyboard.Key.f8:
        sleep(0.5)
        screenshot()
        text = get_text("screen.png")
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

