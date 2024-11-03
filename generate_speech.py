from bark import generate_audio
from scipy.io.wavfile import write
import numpy as np

sentences = [
    "It is not a concern.",
    "We can figure this out.",
    "I wanted to tell you about this."
]
speaker_tag = "[Book narrator]"

all_audio = np.array([])
for sentence in sentences:
    text_prompt = f"{speaker_tag} {sentence}"
    audio_array = generate_audio(text_prompt)
    all_audio = np.concatenate((all_audio, audio_array))
write("bark_combined_test.wav", 22050, all_audio)

