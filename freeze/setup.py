# used to tell dist_me how to distribute

from cx_Freeze import setup, Executable

setup(name='urlParse',
      version='0.1',
      executables=[Executable("dist_me.py")])

