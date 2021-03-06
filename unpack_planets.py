#
# Utility to unpack planet.aei from old data structure.
# Data structure as:
#   e.g., planets/1/planet1.aei
#

import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--planets_old', '-old',
                    action='store',
                    dest='path_old')
parser.add_argument('--planets_new', '-new',
                    action='store',
                    dest='path_new')
args = parser.parse_args()

path_old = args.path_old
path_new = args.path_new

if not os.path.exists(path_new):
    os.mkdir(path_new)

for _dir in os.listdir(path_old):

    try:
        shutil.copy('{}/{}/planet1.aei'.format(path_old, _dir), '{}/{}-planet1.aei'.format(path_new, _dir))
    except FileNotFoundError:
        open('{}/{}-planet1_empty.aei'.format(path_new, _dir), 'a').close()

    try:
        shutil.copy('{}/{}/planet2.aei'.format(path_old, _dir), '{}/{}-planet2.aei'.format(path_new, _dir))
    except FileNotFoundError:
        open('{}/{}-planet1_empty.aei'.format(path_new, _dir), 'a').close()

