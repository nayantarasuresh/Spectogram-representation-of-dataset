import wave
from pydub import AudioSegment
import glob
length= 5.09387755102
#length = 1.48897959184
files = glob.glob('/home/user/Documents/serin/afull/copydata/*')

l = []
i = 1
for pth in files:	
	f = wave.open(pth, 'r')
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames / float(rate)
	f.close()
	dur = length - duration
	pad_ms = dur*1000
	silence = AudioSegment.silent(duration=pad_ms)
	audio = AudioSegment.from_wav(pth)

	padded = audio + silence 
	padded.export(str(i)+'pad.wav', format='wav')
	i+=1





