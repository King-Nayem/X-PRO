import os, platform
os.system('git pull')
os.system('clear')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import NAYEM64.cpython-311.so
elif bit == '32bit':
    import NAYEM32.cpython-311.so
