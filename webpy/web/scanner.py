#!D:/PYTHON/OCR/env2/Scripts/python

from imagescanner import ImageScanner
from config import baseurl

import uuid
import base64
import twain
import cv2

folder_upload = baseurl()+'webpy\\web\\upload\\'

# function create unique number
def name_unique() :
	unique_filename = str(uuid.uuid4().hex)
	return unique_filename

def get_devices():
	sm = twain.SourceManager(0)
	devices = sm.GetSourceList()
	return devices

def get_ocr():
	pass

# function multi scan
def next(ss):
    try:
    	# cetak image info
        # tidak ditampilkan hanya sebagai checking image saja
        ss.GetImageInfo()
        return True
    except:
        return False

def multi_scan(deviceId='',color='gray', capability=1):
	pass

# function to start scanner 
def scan_process(deviceId='',color='gray', capability=1):
	# create filename unique
	filename = name_unique() + ".bmp"
	# lokasi file
	loc_file = folder_upload+filename

	sm = twain.SourceManager(0)
	devices = sm.GetSourceList()
	ss = sm.OpenSource(devices[deviceId])
	ss.RequestAcquire(0,0)
	# set output pixel twain
	# ini berfungsi agar OCR bisa membaca lebih jelas
	# jika kurang dari 1500px maka tidak akan jelas
	if(capability == 2):
		ss.SetCapability(twain.ICAP_YRESOLUTION,twain.TWTY_FIX32, 300.0)
		ss.SetCapability(twain.ICAP_XRESOLUTION,twain.TWTY_FIX32, 300.0)
	if(capability == 1):
		ss.SetCapability(twain.ICAP_YRESOLUTION,twain.TWTY_FIX32, 200.0)
		ss.SetCapability(twain.ICAP_XRESOLUTION,twain.TWTY_FIX32, 200.0)
	if(capability == 0):
		ss.SetCapability(twain.ICAP_YRESOLUTION,twain.TWTY_FIX32, 100.0)
		ss.SetCapability(twain.ICAP_XRESOLUTION,twain.TWTY_FIX32, 100.0)

	rv = ss.XferImageNatively()
	if rv:
		(handle, count) = rv
		twain.DIBToBMFile(handle, loc_file) 

	color = color.lower()
	if color == 'color':
		pass
	if color == 'gray':
		# convert to grayscale
		image = cv2.imread(loc_file)
		im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		cv2.imwrite(loc_file, im_gray)
	if color == 'black_white':
		# convert to grayscale
		image = cv2.imread(loc_file)
		im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		cv2.imwrite(loc_file, im_bw)

	# encode to base64
	imagebase64 = convert_to_base64(loc_file)
	return [filename,imagebase64]

def convert_to_base64(filename_ext=''):
	str = ''
	with open(filename_ext, "rb") as imageFile:
	    str += base64.b64encode(imageFile.read())
	return str

# start main program
if __name__ == "__main__":
	get_devices()