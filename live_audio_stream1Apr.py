import pyaudio
from  deepspeechAPI import model
import numpy as np
import time

text_so_far = ''
def process_audio(in_data, frame_count, time_info, status):
    global text_so_far
    data16 = np.frombuffer(in_data,dtype = np.int16)
    ds_stream.feedAudioContent(data16)
    text = ds_stream.intermediateDecode()

    if(text != text_so_far):
        print('intermin text = {} '.format(text))
        text_so_far = text
    return (in_data,pyaudio.paContinue)



ds_stream = model.createStream()   # deepspeech model object

audio = pyaudio.PyAudio()   # pyaudio object

stream = audio.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = 1024, 
                    stream_callback = process_audio)


print("start speaking ..... CTRL+C to cancel")

stream.start_stream()

try:
    while stream.is_active():
        time.sleep(0.1)

except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("finish recording .....")

    text = ds_stream.finishStream()
    print('text spoken are : ', text)