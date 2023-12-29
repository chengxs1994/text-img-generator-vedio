import json
import whisperx


def download_subs(text_prompt, subs=None):
    audio_filepath = './output/audios/' + text_prompt.replace(' ', '_') + '.mp3'
    subs_filepath = './output/subs/' + text_prompt.replace(' ', '_') + '.json'

    if subs is None:
        model = whisperx.load_model(whisper_arch="base", compute_type="int8", device="cpu")
        subs = model.transcribe(audio_filepath, chunk_size=3)

    with open(subs_filepath, 'w', encoding='UTF-8') as subs_file:
        json.dump(subs, subs_file, ensure_ascii=False)
