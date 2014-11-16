# import numpy as np
from pylab import *
import time

from f_python import *
from f_cython import *

def time_f_pyton():

	t_all = []
	for n in range(7):
	    en = 10**n
	    st_time = time.time()
	    f_python( en)
	    en_time = time.time()
	    t_all.append( en_time - st_time)

	return t_all


def time_f_numba():

	t_all = []
	for n in range(7):
	    en = 10**n
	    st_time = time.time()
	    f_numba( en)
	    en_time = time.time()
	    t_all.append( en_time - st_time)

	return t_all

def time_f_x( f_x):

	t_all = []
	for n in range(7):
	    en = 10**n
	    st_time = time.time()
	    f_x( en)
	    en_time = time.time()
	    t_all.append( en_time - st_time)

	return t_all

def main_meta():
	nn = np.power( 10, xrange(7))
	ll = []
	for mode in ["python", "cython", "numba"]:
		f_x = eval( "f_%s" % mode)
		t_f_x = time_f_x( f_x)

		l, = plt.loglog( nn, t_f_x, '.-', label=mode);
		ll.append( l)

	plt.legend( ll, loc = 0)
	plt.xlabel("Interation: n")
	plt.ylabel("Processing time: t")
	plt.grid()

	plt.show()

def main_org():
	t_f_python = time_f_pyton()
	t_f_numba = time_f_numba()
	t_f_cython = time_f_x( f_cython)

	nn = np.power( 10, xrange(7))
	l_python, = plt.loglog( nn, t_f_python, '.-', label='Python');
	l_numba, = plt.loglog( nn, t_f_numba, '.-', label='Numba');

	plt.xlabel("Interation: n")
	plt.ylabel("Processing time: t")
	plt.grid()
	plt.legend([l_python, l_numba], loc = 0)

	plt.show()

if __name__ == '__main__':
	#Meta main is peformed
	print( "Meta_main is invoked for testing.")
	meta_main()