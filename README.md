WallClock
=========

Python half of a two part system to have an Arduino Board drive an LED matrix as a wall clock and weather display

Works in tandem with a C code running on the Arduino itself, which is essentially waiting for information to be pushed to it from this python code.  It then calls on a separate library to generate the LED images on the matrix.
