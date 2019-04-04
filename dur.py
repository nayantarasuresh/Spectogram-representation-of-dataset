

import wave

import glob

files = glob.glob('/home/user/Documents/serin/afull/neww/*')

l = []
for pth in files:	
	f = wave.open(pth, 'r')
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames / float(rate)
	f.close()
	l.append(duration)
print(l)
	




"""

name = '2.hello.mp3-pad.wav'

f = wave.open(name, 'r')
frames = f.getnframes()
rate = f.getframerate()
duration = frames / float(rate)
f.close()
print(duration)
"""
