import random

import numpy as np

import automata.scenario

class Segregation(automata.scenario.Scenario):

    def __init__(self, dimensions=[100,100], population=[500,500], neighborhood=1):
        super(Segregation, self).__init__(universe=np.array(dimensions, 0.5))

        # Fill squares with people
        for i in range(population[0]):
            self.addPerson(0.0)
        for i in range(population[1]):
            self.addPerson(1.0)

        self._neighborhood = neighborhood

    """ Populate a random empty square. If field is full this will loop forever
    """
    def addPerson(self, personType):
        xMax = len(self._universe)
        yMax = len(self._universe[0])
        while True:
            x = random.randrange(xMax)
            y = random.randrange(yMax)
            if self._universe[x,y] == 0.5:
                self._universe[x,y] = personType
                return

    def step(self):
        # Pass through once and find anyone who wants to move
        # Then for each person who wants to move have them swap with a random person who wants to move
        # This allows for a full map
        return self._universe
