# replaces things like os.system

'''
# This tutorial is best followed in a shell / command prompt.
# Open yours up, type python, or python3, and then follow.
import subprocess

# Say you are on windows:
# module  call command in the shell
# you can change that if you'd like, eventually.
# IF YOU ARE NOT IN A SHELL, YOU WILL SEE NO OUTPUT!
subprocess.call('dir', shell=True)
subprocess.call('echo dir', shell=True)
print(output)


 subprocess.call('python module_subprocess.py "bla bla"', shell=True)
  subprocess.check_output('python module_subprocess.py "bla bla"' )
'''
import sys

print(sys.argv[1])