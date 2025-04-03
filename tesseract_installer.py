import os
import sys
import platform
import webbrowser
import streamlit as st  # Add this import

def install_tesseract():
    """Guide user through Tesseract installation"""
    system = platform.system()
    
    st.error("Tesseract OCR not found! Follow these installation steps:")
    
    if system == "Windows":
        st.markdown("""
        1. Download Windows installer from [this link](https://github.com/UB-Mannheim/tesseract/wiki)
        2. Run the installer with default settings
        3. Add Tesseract to PATH during installation
        4. Restart your computer
        """)
        webbrowser.open("https://github.com/UB-Mannheim/tesseract/wiki")
        
    elif system == "Linux":
        st.markdown("Run in terminal: `sudo apt install tesseract-ocr`")
        
    elif system == "Darwin":
        st.markdown("Run in terminal: `brew install tesseract`")
        
    st.stop()

def verify_installation():
    try:
        import pytesseract
        pytesseract.get_tesseract_version()
        return True
    except Exception as e:
        st.error(f"Tesseract verification failed: {str(e)}")
        return False
