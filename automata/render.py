import matplotlib
matplotlib.use('Agg')

import matplotlib.colors
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimatedGif:

    """ Setup various rendering things
    """
    def __init__(self, dpi=100, colors="Purples"):
        self.frames = []
        self.fig = plt.figure(dpi=dpi)
        plt.axis("off")
        self.colors = colors
        self.normalize = matplotlib.colors.Normalize()
        self.dimensions = None

    def append(self, universe):
        if not self.dimensions:
            if len(universe.shape) != 2 and not (len(universe.shape) == 3 and universe.shape[2] in [3, 4]):
                raise ValueError("Only handles 2D arrays of numbers, or 2D arrays of RGB(A) values")
            self.dimensions = universe.shape
        if self.dimensions != universe.shape:
            raise ValueError("Shape changed from {} to {}".format(self.dimensions, universe.shape))

        self.frames.append((plt.imshow(universe, norm=self.normalize, cmap=self.colors),))

    def render(self, filename, interval=300):
        im_ani = animation.ArtistAnimation(
            self.fig, self.frames, interval=interval, repeat_delay=3000, blit=True
        )
        im_ani.save(filename, writer="imagemagick")
