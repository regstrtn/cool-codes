import sounddevice as sd
fs = 44100
data = np.random.uniform(-0.3, 0.3, fs)
sd.play(data, fs)
