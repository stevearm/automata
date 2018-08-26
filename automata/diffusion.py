import random

import numpy as np

def seed():
    field_size = 128
    populated_spots = 100
    people_per_spot_range = (800,1000)

    field = np.zeros((field_size, field_size), dtype=np.int32)

    # Fill squares with people
    for i in range(populated_spots):
        add_people(field, people_per_spot_range)

    def get_field_as_rgb():
        return automata.utils.render.scale_and_convert_to_rgb(field, 0, people_per_spot_range[1] + 1)

    # automata.utils.render.save_rgb_grid_as_image(get_field_as_rgb(), filename="output.start.png")

    def make_frame(t):
        move_people(field, people)
        return get_field_as_rgb()

    # automata.utils.render.make_video(make_frame, mp4_filename="output.mp4", seconds=5, fps=10)
    # automata.utils.render.make_video(make_frame, gif_filename="output.gif", seconds=5, fps=4)

    # automata.utils.render.save_rgb_grid_as_image(get_field_as_rgb(), filename="output.end.png")

    for i in range(20):
        for times in range(3):
            move_people(field, people)
        automata.utils.render.save_rgb_grid_as_image(get_field_as_rgb(), filename="output.{0:03}.png".format(i))

def add_people(field, people_count_range):
    x_max = len(field)
    y_max = len(field[0])
    people_count = random.randrange(*people_count_range)
    while True:
        x = random.randrange(x_max)
        y = random.randrange(y_max)
        if field[x,y] == 0:
            field[x,y] = people_count
            return

def step(x, y, universe):
    return universe[x, y]

def move_people(field, people):
    for person in people:
        move_person(field, person)

def move_person(field, person):
    my_x = person["x"]
    my_y = person["y"]
    x_max = len(field)
    y_max = len(field[0])
    current_density = field[my_x, my_y]
    new_x = my_x
    new_y = my_y
    for x in range(max(0,my_x-1), min(x_max,my_x+2)):
        for y in range(max(0,my_y-1), min(y_max,my_y+2)):
            if field[x,y] < field[new_x, new_y]:
                new_x = x
                new_y = y
    field[my_x, my_y] -= 1
    field[new_x, new_y] += 1
    person["x"] = new_x
    person["y"] = new_y
