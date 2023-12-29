from gtts import gTTS
from pydub import AudioSegment


def text_to_audio(text_prompt, lang='zh-TW'):
    text_filepath = './input/texts/' + text_prompt.replace(' ', '_') + '.txt'

    text = None
    with open(text_filepath, 'r', encoding='UTF-8') as text_file:
        text = text_file.read()

    audio_filepath = './output/audios/' + text_prompt.replace(' ', '_') + '.mp3'
    audio_obj = gTTS(text=text, lang=lang, slow=False)
    audio_obj.save(audio_filepath)

    speed = 1.25
    sound = AudioSegment.from_file(audio_filepath)

    speedup = sound.speedup(speed)
    speedup.export(audio_filepath, format='mp3')
