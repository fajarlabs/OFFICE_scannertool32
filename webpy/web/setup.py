''' SCRIPT INI DIPAKAI UNTUK MEMBUAT PAKET EXE DENGAN MENGGUNAKAN cx_Freeze'''
''' MASIH FAILED KARENA LIBRARY TWAIN TIDAK BISA DIGUNAKAN '''
import sys
from cx_Freeze import setup, Executable


# include dengan __init
additional_mods = ['numpy.core._methods', 'numpy.lib.format']
# include yang library tanpa __init
packages = ['pkg_resources._vendor','idna','os','sys']
#include files
includefiles = []
setup(name='general_software', 
      version='0.1', 
      description='Setup Installer For Scanner',
      options = {'build_exe': {'include_files':includefiles,'packages':packages,'includes': additional_mods}},
      executables = [Executable('Main.py')]
    )
