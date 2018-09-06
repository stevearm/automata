# automata
Misc simulations

Got it working with the following steps:

1. virtualenv env
2. . env/bin/activate
3. pip install -r requirements
4. pip install -e .

If you get

    IOError: encoder zip not available

it's because `zlib1g-dev` is missing. It should have been installed when you installed Pillow, but: destroy the virtualenv, install that using apt-get, then re-setup the virtualenv

# Notes
* [pyplot.imshow()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html) takes in `norm`, an instance of [matplotlib.colors.Normalize](https://matplotlib.org/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize) which it uses to transform the values at a given spot in the matrix to \[0.0..1.0\]. It then feeds this value into `cmap`, an instance of [matplotlib.colors.Colormap](https://matplotlib.org/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap), to determine what pixel to show
