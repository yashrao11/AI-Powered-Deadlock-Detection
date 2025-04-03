import cv2
import pytesseract
import re
import numpy as np
import streamlit as st
from PIL import Image

class OCRProcessor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
    def process_image(self, image_file):
        try:
            # Preprocessing pipeline
            img = Image.open(image_file)
            img = np.array(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (3,3), 0)
            thresh = cv2.adaptiveThreshold(blur, 255, 
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            
            # OCR with enhanced config
            text = pytesseract.image_to_string(thresh,
                config='--psm 6 -c tessedit_char_whitelist=PR->0123456789')
            
            return self._parse_text(text)
        
        except Exception as e:
            st.error(f"OCR Error: {str(e)}")
            return []

    def _parse_text(self, text):
        relationships = []
        patterns = [
            r'(P\d+)\s*[-→>]+\s*(R\d+)',  # Process to Resource
            r'(R\d+)\s*[-→>]+\s*(P\d+)'   # Resource to Process
        ]
        
        for line in text.split('\n'):
            line = line.replace(" ", "").upper()
            for pattern in patterns:
                matches = re.findall(pattern, line)
                relationships.extend(matches)
        
        return relationships