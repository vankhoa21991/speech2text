from transformers import VitsModel, VitsTokenizer
import torch

model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = VitsTokenizer.from_pretrained("facebook/mms-tts-eng")

text = "fuck you!"
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    data = model(**inputs).waveform.cpu().numpy()  

from io import BytesIO
import scipy
import numpy as np
sample_rate = 16000

buffer = BytesIO()
data_int16 = (data * np.iinfo(np.int16).max).astype(np.int16)
scipy.io.wavfile.write(buffer, rate=sample_rate, data=data_int16.squeeze())
data_wav = buffer.getbuffer().tobytes()
with open("hello_world.wav", "wb") as f:
    f.write(data_wav)