import json
from mutagen.mp3 import MP3
from moviepy import editor
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import generator.pics as pics


def audio_to_video(text_input, pics_input):
    audio_filepath = './output/audios/' + text_input.replace(' ', '_') + '.mp3'
    video_filepath = './output/videos/' + text_input.replace(' ', '_') + '.mp4'
    pics_dir = './output/pics/' + pics_input.replace(' ', '_')

    list_of_images = pics.preprocess_pics(pics_dir)

    audio = MP3(audio_filepath)
    audio_length = audio.info.length
    fps = len(list_of_images) / audio_length

    # 生成视频
    video = editor.ImageSequenceClip(pics_dir, fps=fps)
    audio = editor.AudioFileClip(audio_filepath)
    final_video = video.set_audio(audio)

    final_video.write_videofile(video_filepath, codec="libx264", fps=10)


def create_subtitle_clips(
        subtitles,
        videosize,
        fontsize=65,
        font='Arial',
        color='yellow'):

    subtitle_clips = []
    for subtitle in subtitles:
        start_time = subtitle['start']
        end_time = subtitle['end']
        duration = end_time - start_time

        video_width, video_height = videosize

        text_clip = TextClip(
            subtitle['text'],
            fontsize=fontsize,
            font=font,
            color=color,
            bg_color='black',
            size=(video_width * 3 / 4, None),
            method='caption') .set_start(start_time).set_duration(duration)

        subtitle_x_pos = 'center'
        subtitle_y_pos = video_height * 4 / 5

        text_clip = text_clip.set_position((subtitle_x_pos, subtitle_y_pos))
        subtitle_clips.append(text_clip)

    return subtitle_clips


def attach_subs(text_prompt, font='Arial', fontsize=36):
    video_filepath = './output/videos/' + text_prompt.replace(' ', '_') + '.mp4'
    shorts_filepath = './output/shorts/' + text_prompt.replace(' ', '_') + '.mp4'
    subs_filepath = './output/subs/' + text_prompt.replace(' ', '_') + '.json'

    subtitles = None
    with open(subs_filepath, 'r', encoding='UTF-8') as subs_file:
        subtitles = json.load(subs_file)['segments']

    video = VideoFileClip(video_filepath)
    subtitle_clips = create_subtitle_clips(subtitles, video.size, font=font, fontsize=fontsize)

    final_video = CompositeVideoClip([video] + subtitle_clips)
    duration = final_video.duration

    final_video.subclip(0, duration - 0.5).write_videofile(shorts_filepath)
