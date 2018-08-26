#!/usr/bin/env python

from distutils.core import setup

# pip install -e .

setup(  name="automata",
        version="1.0",
        description="Simulation experements",
        author="Steve Armstrong",
        author_email="steve@horsefire.com",
        url="https://github.com/stevearm/automata",
        license="Apache License 2.0",
        packages=[
            "automata",
        ],
        scripts=[
            "bin/automata"
        ],
     )
