import random

import Image
import moviepy.editor as mpy
import numpy as np

def main():
    length = 512
    data = np.zeros((length, length, 3),
                    dtype=np.uint8)

    def make_frame(t):
        data[   random.randrange(length),random.randrange(length)] = [
                random.randrange(255),
                random.randrange(255),
                random.randrange(255)]
        return data

    make_video(make_frame)

def make_video(get_frame, mp4_filename="output.mp4", gif_filename=None, seconds=25):
    """ Make a video

    Args:
        get_frame (function): Called by passing in time, should return a single frame
    """
    animation = mpy.VideoClip(get_frame, duration=seconds)
    if mp4_filename:
        animation.write_videofile(mp4_filename, fps=20)
    if gif_filename:
        # Writing an animated gif is very slow
        animation.write_gif(gif_filename, fps=15)

def save_as_image(data, filename="output.png"):
    img = Image.fromarray(data, "RGB")
    img.save(filename)

if __name__ == "__main__":
    main()
