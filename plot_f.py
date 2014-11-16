from pylab import *
import time

from f_python import *
from f_cython import *

def time_f_x( f_x):

	t_all = []
	for n in xrange(2, 7):
	    en = 10**n
	    st_time = time.time()
	    f_x( en)
	    en_time = time.time()
	    t_all.append( en_time - st_time)

	return t_all

def main_meta():
	nn = np.power( 10, xrange(2, 7))
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

if __name__ == '__main__':
	main_meta()