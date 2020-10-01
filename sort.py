from datetime import datetime

import html

import time

import random

import os

import pprint

import sys

# from os import 

todays_date = datetime.today()

# the year

year = datetime.today().year

# month
month = datetime.today().month
# day

day = datetime.today().day


time_24_hrs = time.strftime("%H:%M")

day_and_24 = time.strftime("%A:%H:%M:%p")



current = os.getcwd()
# env = os.environ
# pprint.pprint(env)
# getenv = os.getenv('USERNAME')

version = sys.version

plat = sys.platform


print(todays_date)
print(year)
print(month)
print(day)
print(time_24_hrs)
print(day_and_24)
# print(env)
# print(getenv)
# print(current)
print(version)
print(plat)
# print(pretty)

