# Real Time speech to text 

We use python pyaudio api and deep speech models to perform real time speech to text process.
The Python version uses 3.8.5 and uses any Python 3+ version. <br>

# Project Structure:<br>
	|--models<br>
	   |--deepspeech-0.9.3-models.pbmm<br>
	   |--deepspeech-0.9.3-models.scorer<br>
	|--deepspeechAPI.py<br>
	|--live_audio_stream.py<br>

    • models  folder contain 2  deep speech models .  <br>
    • deepspeechAPI.py contains creating the model object and adding the external scorer.<br>
    • Live_audio_stream.py contains live audio capture and conversion into text.<br>

# To run the project:<br>

To run the project just call the file  live_audio_stream.py <br>
	
# $ python3 live_audio_stream.py
<br>

# Requirements:<br>

pip install deepspeech==0.8.2  <br>
pip install numpy==1.20.2  <br>
pip install PyAudio== 0.2.11 <br>
pip install wheel==0.36.2 <br>



# Link referenced: <br>
	https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3   <br>
https://medium.com/slanglabs/how-to-build-python-transcriber-using-mozilla-deepspeech-5485b8d234cf
