import random

import Image
import moviepy.editor as mpy
import numpy as np

def convert_2d_array_to_rgb(array_2d):
    zeroed = array_2d - array_2d.min()
    scaled_512 = zeroed * 512 / zeroed.max()
    pos_neg_255 = scaled_512 - 255
    red = np.maximum(0, pos_neg_255)
    green = np.maximum(0, pos_neg_255 * -1)
    return np.dstack((red, green, array_2d*0))

def make_video(get_frame, mp4_filename=None, gif_filename=None, seconds=25):
    """ Make a video

    Args:
        get_frame (function): Called by passing in time, should return a single frame (a single 2d grid of rgb tuples)
    """
    animation = mpy.VideoClip(get_frame, duration=seconds)
    if mp4_filename:
        animation.write_videofile(mp4_filename, fps=20)
    if gif_filename:
        # Writing an animated gif is very slow
        animation.write_gif(gif_filename, fps=15)

def save_rgb_grid_as_image(rgb_grid, filename):
    img = Image.fromarray(rgb_grid, "RGB")
    img.save(filename)

if __name__ == "__main__":
    length = 512
    data = np.zeros((length, length), dtype=np.int8)

    def make_frame(t):
        data[random.randrange(length),random.randrange(length)] = random.randrange(2048)
        return convert_2d_array_to_rgb(data)

    make_video(make_frame, mp4_filename="test.render.mp4", gif_filename="test.render.gif", seconds=5)
    save_rgb_grid_as_image(convert_2d_array_to_rgb(data), filename="test.render.png")
