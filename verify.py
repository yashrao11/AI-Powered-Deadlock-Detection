import pytesseract
import platform

def verify_tesseract():
    try:
        if platform.system() == "Windows":
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            
        print("Tesseract version:", pytesseract.get_tesseract_version())
        print("Installation Path:", pytesseract.pytesseract.tesseract_cmd)
        print("Status: OK")
    except Exception as e:
        print("Verification Failed:", str(e))

if __name__ == "__main__":
    verify_tesseract()