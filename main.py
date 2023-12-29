from generator import audio, pics, subs, video


def main():
    texts_input = 'example'
    pics_input = 'example'

    # pics.adjust(pics_input)
    #
    # audio.text_to_audio(texts_input)

    video.audio_to_video(texts_input, pics_input)

    # subs.download_subs(texts_input)

    video.attach_subs(texts_input)


if __name__ == "__main__":
    main()
