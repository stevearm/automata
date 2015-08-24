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
