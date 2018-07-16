''' SCRIPT YANG DIGUNAKAN UNTUK INSTALL SERVICE WINDOWS '''
''' TERDAPAT BUGS NYANGKUT DI SERVISNYA '''
''' 
    Untuk install servis windowsnya : C:\Python27\webpy\web>c:\Python27\python.exe services.py install
    Untuk install start servisnya  : C:\Python27\webpy\web>c:\Python27\python.exe services.py start
    Untuk remove servis windowsnya : C:\Python27\webpy\web>c:\Python27\python.exe services.py remove
    Untuk kill PID : taskkill /F /PID <PID>
    Untuk lihat servisnya : sc queryex <service name>
    Untuk install autorun ketika komputer mati : C:\Python27\webpy\web>c:\Python27\python.exe services.py --wait=2000 --startup=auto install
'''

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

from mysite import start
from checkservice import stop_service
import web


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "scannertool32"
    _svc_display_name_ = "Twain Interface For Python"
    _svc_request_ = True

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        # kill webserver
        web.httpserver.server.interrupt = KeyboardInterrupt()

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        # start web server
        start()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)