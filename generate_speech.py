from bark import generate_audio
from scipy.io.wavfile import write

# The text to be converted into speech
text_prompt = "[young scottish boy] Author of the danger trail, Philip Steels, etc. Not at this particular case, Tom, apologized Whittemore. For the twentieth time that evening the two men shook hands. Lord, but I'm glad to see you again, Phil."

audio_array = generate_audio(text_prompt)
write("bark_test_voice.wav", 22050, audio_array)

