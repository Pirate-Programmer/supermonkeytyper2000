# SuperMonkeyTyper2000

Script to auto-type text from Monkeytype using screenshots + OCR.

---
# Note
Use it at your own risk if You get banned or something goes wrong you have been warned. This script is only for "educational purpose"


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

   

<img width="1000" height="750" alt="Infinite Speed monkeytype image" src="https://github.com/user-attachments/assets/7acf1364-94a5-4e9b-9301-8d60d900c536" />
<pre>I have achieved singularity. The machines no longer test me I test them
                                                             -Sun tzu art of war</pre>






