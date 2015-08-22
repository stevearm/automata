import random

import Image
import moviepy.editor as mpy
import numpy as np

def scale_2d_array(array_2d, new_min, new_max, current_min=None, current_max=None):
    """ Scale the given array values to the given range

    Args:
        array_2d (2D numpy array): Can contain any type of number
        new_min (number): The lowest value to be returned
        new_max (number): The highest value to be returned
        current_min (number): If specified, use as the current min (scale the array as if this was the lowest number)
        current_max (number): If specified, use as the current max (scale the array as if this was the highest number)
    """
    if current_min is None:
        current_min = array_2d.min()
    elif array_2d.min() < current_min:
        raise ValueError("Cannot specify a current_min of {} that is higher than the real min of {}".format(current_min, array_2d.min()))
    if current_max is None:
        current_max = array_2d.max()
    elif current_max < array_2d.max():
        raise ValueError("Cannot specify a current_max of {} that is lower than the real max of {}".format(current_max, array_2d.max()))
    zeroed = array_2d - array_2d.min() + new_min
    return zeroed * new_max / zeroed.max()

def convert_2d_array_to_rgb(array_2d):
    """ Convert the given array into an array of 8-bit RGB values

    Args:
        array_2d (2D numpy array): Must contain numbers between 0 and 512
    """
    # [Red, Green, Blue]
    #   0 is [0, 256, 0]
    # 256 is [0,   0, 0]
    # 512 is [256, 0, 0]
    red = np.maximum(256, array_2d) - 256
    green = (np.minimum(255, array_2d) * -1) + 256
    return np.dstack((red.astype(np.int8), green.astype(np.int8), (array_2d*0).astype(np.int8)))

def scale_and_convert_to_rgb(array_2d, current_min=None, current_max=None):
    return convert_2d_array_to_rgb(scale_2d_array(array_2d, 0, 511, current_min, current_max))

def make_video(get_frame, mp4_filename=None, gif_filename=None, seconds=25, fps=20):
    """ Make a video

    Args:
        get_frame (function): Called by passing in time, should return a single frame (a single 2d grid of rgb tuples)
    """
    animation = mpy.VideoClip(get_frame, duration=seconds)
    if mp4_filename:
        animation.write_videofile(mp4_filename, fps=fps)
    if gif_filename:
        # Writing an animated gif is very slow
        animation.write_gif(gif_filename, fps=fps)

def save_rgb_grid_as_image(rgb_grid, filename):
    """ Render the given grid as a png

    Args:
        rgb_grid (2d array): Must contain a tuple of three unsigned 8-bit values (RGB) in each array location
    """
    img = Image.fromarray(rgb_grid, "RGB")
    img.save(filename)

if __name__ == "__main__":
    length = 256
    data = np.zeros((length, length), dtype=np.int32)

    def make_frame(t):
        data[random.randrange(length),random.randrange(length)] = random.randrange(2048)
        return scale_and_convert_to_rgb(data)

    make_video(make_frame, mp4_filename="test.render.mp4", gif_filename="test.render.gif", seconds=5)

    length = 512
    data = np.zeros((length, length), dtype=np.int32)
    for x in range(length):
        for y in range(length):
            data[x,y] = x + y

    save_rgb_grid_as_image(scale_and_convert_to_rgb(data), filename="test.render.png")

    try:
        scale_2d_array(data, 0, 256, 0, 5)
        print "Should have thrown an exception"
    except ValueError, e:
        print "For passing an invalid max: {}".format(e)
        pass
    try:
        scale_2d_array(data, 0, 256, 5, 513)
        print "Should have thrown an exception"
    except ValueError, e:
        print "For passing an invalid min: {}".format(e)
        pass
