import pyaudio
import wave

CHUNK = 1024

path = '/Users/macbook-air/Desktop/coding/인공지능수학수업/output.wav'

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