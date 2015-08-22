I want a simple economic simulation. Cellular automata was my first guess, but now trying agent-based modelling.

## Data layers

1. Wealth
2. Goods owned
3. Goods for sale
3. Goods sale price

## Simulation steps

1. Interest - World - Multiply wealth by the interest rate
2. Bounty   - World - Randomly add between 0 and 100 goods to owned
3. Sell     - Agent - Put some owned goods. Move from owned to for-sale
4. Buy      - Agent - For any of the border cells, up to their for-sale count, move your own wealth to that cell's wealth
5. Eat      - World - Remove X from owned
6. Spoil    - World - Reduce owned to 0

## Getting it working
Got it working with the following steps:

1. virtualenv env
2. . env/bin/activate
3. pip install -r requirements
4. pip install -e .

## Known issues
If you get

    IOError: encoder zip not available

it's because `zlib1g-dev` is missing. It should have been installed when you installed Pillow, but: destroy the virtualenv, install that using apt-get, then re-setup the virtualenv
