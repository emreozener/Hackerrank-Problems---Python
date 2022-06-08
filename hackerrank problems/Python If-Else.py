#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

if n % 2 == 1 or n in range(6,21):
    print("Weird")
else:
    print("Not Weird")

# prints weird or not weird according to given input
