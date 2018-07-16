import wmi

# fungsi untuk melihat servicenya tersedia atau tidak
def get_service(NameService = ""):
	c = wmi.WMI()
	srv = c.Win32_Service(Name=NameService)
	if srv != []:
		return True
	return False

def stop_service(NameService = ""):
	c = wmi.WMI()
	for service in c.Win32_Service(Name=NameService):
	  result, = service.StopService()
	  if result == 0:
	  	# success deleted
	    return 0
	  else:
	  	# something went wrong
	    return 1
	  break
	else:
		# service not found
		return 2