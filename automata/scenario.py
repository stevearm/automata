import numpy as np

class Scenario(object):

    """ Setup various rendering things
    """
    def __init__(self, universe=None, dimensions=None):
        if universe:
            self._universe = universe
        elif dimensions:
            self._universe = np.zeros(dimensions)

    def universe(self):
        return self._universe

    def step(self):
        newUniverse = np.copy(self._universe)
        for x in range(self._universe.shape[0]):
            for y in range(self._universe.shape[1]):
                newUniverse[x, y] = self.nextCell(x, y)
        self._universe = newUniverse
        return self._universe

    def nextCell(self, x, y):
        return self._universe[x, y]
