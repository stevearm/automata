import argparse
import random

import numpy as np

from utils import render

def main():
    parser = argparse.ArgumentParser(description="Simulate some things")
    parser.add_argument("--verbose", action="store_true", help="Print lots of messages")

    args = parser.parse_args()

    length = 512
    data = np.zeros((length, length), dtype=np.int8)

    def make_frame(t):
        data[random.randrange(length),random.randrange(length)] = random.randrange(2048)
        return render.convert_2d_array_to_rgb(data)

    render.make_video(make_frame, mp4_filename="output.mp4", seconds=5)
    render.save_rgb_grid_as_image(render.convert_2d_array_to_rgb(data), filename="output.png")

if __name__ == "__main__":
    main()
