import random

import numpy as np

import automata.scenario

class Diffusion(automata.scenario.Scenario):

    def __init__(self, dimensions=[128,128], populatedSquares=100, populationRange=(800, 1000)):
        super(Diffusion, self).__init__(universe=np.zeros(dimensions, dtype=np.int32))

        # Fill squares with people
        self._peopleLocations = []
        for i in range(populatedSquares):
            self.addPeople(populationRange)

    """ Populate a random empty square. If field is full this will loop forever
    """
    def addPeople(self, peopleCountRange):
        xMax = len(self._universe)
        yMax = len(self._universe[0])
        peopleCount = random.randrange(*peopleCountRange)
        while True:
            x = random.randrange(xMax)
            y = random.randrange(yMax)
            if self._universe[x,y] == 0:
                self._universe[x,y] = peopleCount
                for i in range(peopleCount):
                    self._peopleLocations.append((x,y))
                return

    def step(self):
        for personNumber in range(len(self._peopleLocations)):
            # Choose an adjacent square with lower population
            newPerson = self._peopleLocations[personNumber]
            xRange = range(max(0, newPerson[0] - 1), min(newPerson[0] + 2, self._universe.shape[0]))
            yRange = range(max(0, newPerson[1] - 1), min(newPerson[1] + 2, self._universe.shape[1]))
            for x in xRange:
                for y in yRange:
                    if self._universe[x,y] < self._universe[newPerson]:
                        newPerson = (x,y)

            # Move to new square. This happens live, so person 2 will decide by seeing person 1's new location
            self._universe[self._peopleLocations[personNumber]] -= 1
            self._peopleLocations[personNumber] = newPerson
            self._universe[self._peopleLocations[personNumber]] += 1

        return self._universe
