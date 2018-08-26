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
            # Handle multiple squares with the same population and choose between randomly
            newPeople = [self._peopleLocations[personNumber]]
            xRange = range(max(0, newPeople[0][0] - 1), min(newPeople[0][0] + 2, self._universe.shape[0]))
            yRange = range(max(0, newPeople[0][1] - 1), min(newPeople[0][1] + 2, self._universe.shape[1]))
            for x in xRange:
                for y in yRange:
                    if self._universe[x,y] < self._universe[newPeople[0]]:
                        newPeople = [(x,y)]
                    elif self._universe[x,y] == self._universe[newPeople[0]]:
                        newPeople.append((x,y))

            # If we had multiple options, choose one randomly
            newPerson = random.choice(newPeople)

            # Move to new square. This happens live, so person 2 will decide by seeing person 1's new location
            self._universe[self._peopleLocations[personNumber]] -= 1
            self._peopleLocations[personNumber] = newPerson
            self._universe[self._peopleLocations[personNumber]] += 1

        return self._universe
