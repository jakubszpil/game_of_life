# Game Of Life

## Get started

To create & start using python venv:

```cmd
python -m venv venv
source venv/bin/activate
```

Install required modules with pip:

```cmd
pip install pygame
pip install numpy
```

## Requirements

1.  Make simulation real time

2.  Add pause / resume logic

3.  Add save / load logic

## High-level logic

1.  Create and init the simulation grid

2.  Start the simulation with a tick interval of <n> seconds

3.  At each tick:

    - Update the grid - loop over each element of the board

    - Render new generation

## General approach

1.  Plan & write down the general workflow

    - Define Input&Output

    - Consider adding validation

2.  Separate the main algorithms / actors in the code. Try to abstract as much common code as possible

3.  Define communication between the objects

4.  List the patterns you could apply

5.  Build PoCs (Proof of concepts). Try to separate implementation of specific steps. Prepare smaller modules

and combine them into a complete application

6.  Refine if needed
