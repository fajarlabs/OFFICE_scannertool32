
############################################################
# LETAK FILE INI
############################################################
Taruh lokasi file ini di dalam folder "webpy/web"

############################################################
# DOWNLOAD PYTHON
############################################################
download pada link berikut ini : https://www.python.org/downloads/
Taruh python pada drive C: bedakan antara versi 2 dan 3 dengan menggunakan folder sendiri-sendiri

############################################################
# Pasang virtual environment
############################################################
install dengan menggunakan perintah berikut ini : 
> pip install virtualenv

untuk membuat virtual environment baru ketikan berikut ini : 
> virtualenv --python=C:\Python3.6.5\python.exe env   <-- env adalah nama virtual environment yg dibuat
untuk menyalakannya masuk ke folder env/Scripts/activate.bat dan untuk mematikannya env/Scripts/deactivate.bat

############################################################
# OCR
############################################################

1.) Pasang terlebih dahulu library python berikut ini
pip install pillow
pip install pytesseract

contoh script : https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

2.) Download tesseract excecutable disini
https://github.com/tesseract-ocr/tesseract/wiki/Downloads, dan sesuaikan sesuai sistem operasi masing-masing

3.) Download library training bahasa disini
https://github.com/tesseract-ocr/tessdata

pada environment variable

#pasang environment tesseract
PATH=D:\PYTHON\OCR\tesseract

#pasang environment test data, harus parent foldernya
TESSDATA_PREFIX=D:\PYTHON\OCR


############################################################
# SCANNNER 
############################################################
Untuk install scanner perlu library berikut, ketik pada command prompt :

> easy_install --find-links http://www.pythonware.com/products/pil/ Imaging

# lalu install image scanner

> pip install imagescanner

https://www.lfd.uci.edu/~gohlke/pythonlibs/ download library twain whl disini

############################################################
# FLASK
############################################################
untuk instalasi flask, keluar dari virtual environment terlebih dahulu
lalu install dengan mengetikan kode berikut ini, 

> pip install flask

lalu kembali ke virtualenv aplikasi

############################################################
# Download PIL ImageScanner
############################################################
http://www.pythonware.com/products/pil/
