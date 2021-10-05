import pyaudio
import wave

CHUNK = 1024

path = '\Users\User\Desktop\python folder\output.wav'

with wave.open(path, 'rb') as f:
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
    channels = f.getnchannels(),
    rate = f.getframerate(),
    output = True)

    data = f.readframes(CHUNK)
    while data:
        stream.write(data)
        data = f.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()