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
   
3. Edit properties
```python
#blah .... some code

#Set path in script if on Windows:
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Adjust crop values in script for your screen resolution:
crop = (150, 530, 1800, 710)

#set this delay to adjust typing speed
delay = 0.1

#blah.... some code
```
4. Run da script ;D



