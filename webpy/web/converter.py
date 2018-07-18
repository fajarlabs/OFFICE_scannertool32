from PIL import Image
import os

# function to convert image to pdf
# return boolean if TRUE is success and otherwise
def convertImageToPdf(path,output=None):
	result = False
	try :
		# extract absolute path
		head,tail = os.path.split(path)
		filename, extension = os.path.splitext(tail)
		# open image file
		im = Image.open(path)
		if(output == None):
			output = head+"/"+filename+".pdf"
		# convert to output pdf
		Image.Image.save(im, output, "PDF", resoultion=100.0)
		result = True
	except Exception as e :
		print "Error Message : "+str(e.message)
	return result

convertImageToPdf("D:\\PYTHON\\OCR\\webpy\\web\\upload\\0c5497cc2cc9488a863a025305866b34.JPG")