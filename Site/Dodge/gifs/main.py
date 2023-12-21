from moviepy.editor import VideoFileClip

def video_to_gif(input_path, output_path, fps=20):
    clip = VideoFileClip(input_path)
    clip.write_gif(output_path, fps=fps)

# مسیر ویدیو و مسیر خروجی را جایگزین کنید
video_path = "/home/ubuntu/رومیزی/Mini-Projects/Dodge/gifs/BackGif1.mp4"
gif_path = "1tput.gif"

# تبدیل ویدیو به GIF با فریم در ثانیه 10
video_to_gif(video_path, gif_path, fps=20)
