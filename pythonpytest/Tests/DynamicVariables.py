import os
import random
import time
import math

USER = os.getlogin()
RANDOM_INT = random.randint(0,10)
CURRENT_TIME = time.asctime()
AFTERNOON = None
if CURRENT_TIME[3]>12:
    AFTERNOON = True
else:
    AFTERNOON = False

def get_area(d):
    r=d/2
    return math.pi*r**2

AREA = get_area(5)