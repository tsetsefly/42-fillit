#!/usr/bin/env python
from __future__ import print_function

tet_shapes = [
	'####\n....\n....\n....\n',
	'#...\n#...\n#...\n#...\n',
	'#...\n###.\n....\n....\n',
	'##..\n#...\n#...\n....\n',
	'###.\n..#.\n....\n....\n',
	'.#..\n.#..\n##..\n....\n',
	'..#.\n###.\n....\n....\n',
	'#...\n#...\n##..\n....\n',
	'###.\n#...\n....\n....\n',
	'##..\n.#..\n.#..\n....\n',
	'##..\n##..\n....\n....\n',
	'.##.\n##..\n....\n....\n',
	'#...\n##..\n.#..\n....\n',
	'.#..\n###.\n....\n....\n',
	'#...\n##..\n#...\n....\n',
	'###.\n.#..\n....\n....\n',
	'.#..\n##..\n.#..\n....\n',
	'##..\n.##.\n....\n....\n',
	'.#..\n##..\n#...\n....\n',
]

import pickle
import argparse
import random
import os
import StringIO

parser = argparse.ArgumentParser(description="Generate random fillit problems")
parser.add_argument('count', metavar="count", type=int, default=10, nargs='?',
		help="number of tetrominoes to output")
parser.add_argument('--seed', type=int, default=None,
		help="mt_rand seed (to reproduce problems)")

args = parser.parse_args()

seed = args.seed
if seed is None:
	seed = random.SystemRandom().randint(0, 2**19937-1)

random.seed(seed)

tets = [tet_shapes[random.randrange(len(tet_shapes))] for x in range(args.count)]

[print(x, end=("" if i == len(tets) - 1 else "\n")) for i, x in enumerate(tets)]
#print tets
#print args
#print args.count
#print args.seed