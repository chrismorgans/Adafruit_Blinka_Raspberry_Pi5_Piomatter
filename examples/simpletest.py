#!/usr/bin/python3
"""
Display a static 64x64 image

This assumes two 64x32 matrix panels are hooked together in the "serpentine" configuration.

Run like this:

$ python simpletest.py

The image is displayed until the user hits enter to exit.
"""

import pathlib

import adafruit_raspberry_pi5_piomatter
import numpy as np
import PIL.Image as Image

geometry = adafruit_raspberry_pi5_piomatter.Geometry(width=64, height=64, n_addr_lines=4, rotation=adafruit_raspberry_pi5_piomatter.Orientation.Normal)
framebuffer = np.asarray(Image.open(pathlib.Path(__file__).parent / "blinka64x64.png"))
matrix = adafruit_raspberry_pi5_piomatter.AdafruitMatrixBonnetRGB888Packed(framebuffer, geometry)
matrix.show()

input("Hit enter to exit")
