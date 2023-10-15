import torch, torchaudio
import os

files = [file for file in os.path.list("input") if file.endswith(".wav")]

pitch_range = 5

batch_size = 10

def loadBatch():
    for i in range(batch_size):
        

