''' SCRIPT TESTING '''
''' SCRIPT YANG DIGUNAKAN UNTUK MELAKUKAN TEST UJI PRINTER SCANNER '''
import twain
from PIL import Image
from StringIO import StringIO

# jika ingin menggunakan feeder set TRUE jika ingin 
# menggunakan single scanner set FALSE
feeder = True

if(feeder == False) :
	# sumber data dari scanner
	sm = twain.SourceManager(0)
	ss = sm.OpenSource()
	ss.RequestAcquire(0,0)

	# set capability
	try:    
		ss.SetCapability(twain.ICAP_YRESOLUTION,twain.TWTY_FIX32, 200.0)
		ss.SetCapability(twain.ICAP_XRESOLUTION,twain.TWTY_FIX32, 200.0)
	except Exception as e:
	    print str(e.message)

	rv = ss.XferImageNatively()
	if rv:
		(handle, count) = rv
		str_image = twain.DIBToBMFile(handle) 
		twain.GlobalHandleFree(handle)
		# tampilkan object file di command prompt
		print Image.open(StringIO(str_image))
elif(feeder == True):
	index = 0;

	def next(ss):
	    try:
	    	# cetak image info
	        # tidak ditampilkan hanya sebagai checking image saja
	        ss.GetImageInfo()
	        return True
	    except:
	        return False

	def capture(ss):
	    global index
	    result = False
	    try :
		    rv = ss.XferImageNatively()
		    fileName = str(index) + '_image.bmp';
		    index+=1;
		    #print rv;
		    if rv:
		        (handle, count) = rv
		        # simpan gambar kedalam file
		        str_image = twain.DIBToBMFile(handle)
		        # tampilkan object file di command prompt
		        print Image.open(StringIO(str_image))
		    result = True
	    except Exception as e :
	    	print str(e.message)

	    return result

	sm = twain.SourceManager(0)
	ss = sm.OpenSource()

	try:    
	    ss.SetCapability( twain.CAP_FEEDERENABLED, twain.TWTY_BOOL, True)
	    ss.SetCapability(twain.ICAP_YRESOLUTION,twain.TWTY_FIX32, 300.0)
	    ss.SetCapability(twain.ICAP_XRESOLUTION,twain.TWTY_FIX32, 300.0)
	except Exception as e :
	    print str(e.message)

	#print "acquire image"
	ss.RequestAcquire(0,0)

	# looping untuk memeriksa apakah masih ada
	# file / document pada feeder
	while next(ss):
		# jika error maka akan keluar dari loop scanner
		if(capture(ss) != True):
			break

	print('Done')