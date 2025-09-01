# SuperMonkeyTyper2000

Script to auto-type text from Monkeytype using screenshots + OCR.

---
#Note
Use it at your own risk if You get banned or something goes wrong you have been warned. This script is only for "educational purpose"

---
## Usage
- **F8** → take screenshot (make sure Monkeytype window is active).  
- **Esc** → stop the listener.  

---

## Setup
1. Clone repo
   ```bash
   git clone https://github.com/Pirate-Programmer/supermonkeytyper2000.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
   
4. Edit properties
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
5. Run da script ;D





