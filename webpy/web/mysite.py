from scanner import scan_process,get_devices
from ocr import read_file_from_data_uri,read_file
from checkservice import get_service

import json
import web

# router controller
urls = (
    '/', 'MainController'
)

# controller untuk router URL web services
class MainController:

	# method GET
	def GET(self):

		# dapatkan parameter web
		userdata = web.input(act="",deviceid="",scale="",ocr=0,capability=1)

		# -----------------------------------------------------------------------------------
		# Fungsi untuk menampilkan semua device yang terhubung dengan PC / Komputer tersebut
		# -----------------------------------------------------------------------------------
		if(userdata.act == "get_devices"):
			web.header('Access-Control-Allow-Origin',      '*')
			web.header('Access-Control-Allow-Credentials', 'true')
			web.header('Content-Type', 'application/json')
			devices = get_devices()
			device_data = []
			try :
				for d in devices :
					device_data.append(d)
	        	
	        	# print to json
				return str(json.dumps(device_data))
			except (Exception) as e : 
				return ''
		
		# ---------------------------------------------------------------------------------------
		# Fungsi untuk mulai scanning pada printer berdasarkan index urutan printer yang dipilih
		# ---------------------------------------------------------------------------------------
		elif(userdata.act == "start_scanning"):
			web.header('Access-Control-Allow-Origin','*')
			web.header('Access-Control-Allow-Credentials','true')
			web.header('Content-Type', 'application/json')
			try :
				# dapatkan ID dari pilihan SCANNER pada method get_devices()
				deviceid = int(userdata.deviceid)
				# dapatkan ukuran hasilnya 
				capability = int(userdata.capability)
				# dapatkan scale warna
				color_scale = str(userdata.scale)
				# start scanning process by device id
				scn_result = scan_process(deviceid,color_scale,capability)
				# get result data from scanner
				nme_result = str(scn_result[0]) # file name
				b64_result = "data:image/jpeg;base64,"+str(scn_result[1]) # image base64
				# kumpulkan data
				data = []
				data.append(nme_result)
				data.append(b64_result)

				ocr = int(userdata.ocr)
				if(ocr == 1):
					data.append(read_file_from_data_uri(b64_result))
				else:
					data.append("")
				# print to json
				return str(json.dumps(data))
			except (Exception) as e : 
				print e
				return ''

		# ---------------------------------------------------------------------------------------
		# Fungsi untuk nilai default jika value salah
		# ---------------------------------------------------------------------------------------
		else:
			return str(json.dumps({"status":"ok"}))

# ---------------------------------------------------------------------------------------
# Class untuk override PORT
# ---------------------------------------------------------------------------------------
class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

# ---------------------------------------------------------------------------------------
# Fungsi untuk menyalakan servis
# ---------------------------------------------------------------------------------------

def start():
    app = MyApplication(urls, globals())
    app.run(port=8888)

# ---------------------------------------------------------------------------------------
# Fungsi program utama ketika dijalan dengan python main.py
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
	if(get_service('scannertool32') == True) :
		print 'Service name "scannertool32" is found, please check in windows service'
	else :
		print 'Service name "scannertool32" not found, this running manually' 
		start()
# ---------------------------------------------------------------------------------------
# untuk mematikan webserver webpy gunakan interrupt kode dibawah ini
# web.httpserver.server.interrupt = KeyboardInterrupt()
# link disini https://stackoverflow.com/questions/26408147/how-to-stop-web-py-server-which-run-as-windows-service
# ---------------------------------------------------------------------------------------