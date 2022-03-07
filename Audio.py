import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv 
  
freq = 44100  
duration = 5
sd.default.samplerate = freq
sd.default.channels = 2
recording = sd.rec(int(duration * freq))
  
sd.wait() 
  
write("recording0.wav", freq, recording) 
  
wv.write("recording1.wav", recording, freq, sampwidth=2)

