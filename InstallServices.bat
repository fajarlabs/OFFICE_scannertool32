:: Edit regedit agar service twain tidak cepat mati saat di start
REG ADD HKLM\SYSTEM\CurrentControlSet\Control /v ServicesPipeTimeout /t REG_DWORD /d 180000

:: Edit regedit via path
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_SZ /d "%PATH%;C:\ScannerTool;C:\ScannerTool\tesseract;C:\ScannerTool\Library\bin;C:\ScannerTool\Scripts;C:\ScannerTool\Lib\site-packages\win32;C:\ScannerTool\Lib\site-packages\pywin32_system32;C:\ScannerTool\Scripts;" /f

:: Edit regedit TESSDATA_PREFIX
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v TESSDATA_PREFIX /t REG_SZ /d "C:\ScannerTool"

:: Edit regedit PYTHON_PATH
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PYTHONPATH /t REG_SZ /d "C:\ScannerTool"

:: Start services scannertool32
"C:\ScannerTool\python.exe" "C:\ScannerTool\webpy\web\services.py" install
"C:\ScannerTool\python.exe" "C:\ScannerTool\webpy\web\services.py" start