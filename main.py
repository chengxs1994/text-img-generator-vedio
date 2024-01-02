from generator import audio, pics, subs, video


def main():
    texts_input = 'example'
    pics_input = 'example'

    # 图片分辨率预处理
    pics.adjust(pics_input)

    # 文字转语音
    audio.text_to_audio(texts_input)

    # 语音转视频
    video.audio_to_video(texts_input, pics_input)

    # 生成字幕
    subs.download_subs(texts_input)

    # 生成字幕视频
    video.attach_subs(texts_input)


if __name__ == "__main__":
    main()
