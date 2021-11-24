from math import gcd
from functools import reduce
import numpy as np

def find_gcd(vec):
    x = reduce(gcd, vec)
    return x

def make_coprime(vec):
	scale = find_gcd(vec)
	vec = np.divide(vec, scale)
	if vec[0] < 0:
		vec *= -1
	return vec

