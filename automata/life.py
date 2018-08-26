import numpy as np

import automata.scenario

seeds = {
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}

class Life(automata.scenario.Scenario):

    def __init__(self, dimensions=[100,100], seed="infinite", seed_position=[40,40]):
        super(Life, self).__init__(dimensions=dimensions)
        x_start, y_start = seed_position[0], seed_position[1]
        seed_array = np.array(seeds[seed])
        x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]
        self._universe[x_start:x_end, y_start:y_end] = seed_array

    def nextCell(self, x, y):
        num_neighbours = np.sum(self._universe[x - 1 : x + 2, y - 1 : y + 2]) - self._universe[x, y]
        if self._universe[x, y] and not 2 <= num_neighbours <= 3:
            return 0
        if num_neighbours == 3:
            return 1
        return self._universe[x, y]
