# SuperMonkeyTyper2000

Script to auto-type text from Monkeytype using screenshots + OCR.

---

## Usage
- **F8** → take screenshot (make sure Monkeytype window is active).  
- **Esc** → stop the listener.  

---

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
   
3. 
```python
#Set path in script if on Windows:

#blah .... some code

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Adjust crop values in script for your screen resolution:
crop = (150, 530, 1800, 710)

#blah.... some code
#set this delay to adjust typing speed (in supermonkeytyper2000 function)
sleep(0.1) 
```


