#!/usr/bin/env python3

# Based on: https://github.com/chicolucio/truth-table-generator/blob/master/ttg/ttg.py
# TODO: Finish this today

"""
truth-table-generator main file
"""

import itertools
import re
from prettytable import PrettyTable
import pyparsing
import pandas as pd
import numpy as np
from tabulate import tabulate
from distutils.util import strtobool

# bool ops
OPERATIONS = {
	  'not':      (lambda x: not x),
    '-':        (lambda x: not x),
    '~':        (lambda x: not x),

    'or':       (lambda x, y: x or y),
    'nor':      (lambda x, y: not (x or y)),
    'xor':      (lambda x, y: x != y),

    'and':      (lambda x, y: x and y),
    'nand':     (lambda x, y: not (x and y)),

    '=>':       (lambda x, y: (not x) or y),
    'implies':  (lambda x, y: (not x) or y),

    '=':        (lambda x, y: x == y),
    '!=':       (lambda x, y: x != y),
}

def recursive_map(func, data): 
	""" recusively applies a map function to a list and all sublists"""

	if isinstance(data, list):
		return [recursive_map(func, elem) for elem in data]
	else:
		return func(data)
	
def sting_to_bool(string):
	try:
		string = bool(strtobool(string))
	except ValueError:
		pass
	return string

def solve_phrases(phrase):
	if isinstance(phrase, bool):
		return phrase
	if isinstance(phrase, list):
		if len(phrase) == 1:
			return solve_phrases(phrase[0])
		
		if len(phrase == 2):
			return OPERATIONS[phrase[0](solve_phrase(phrase[1]))]
		else:
			return OPERATIONS[phrase[1]](solve_phrase(phrase[0]),
																							  phrase[2])
		

