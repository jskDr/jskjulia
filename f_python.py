#This is python code
def f_python(n):
	s = 0
	for i in range( n):
		s += i/2.0
	return s

#This is numba version
from numba import double
from numba.decorators import jit, autojit
#from numba.decorators import autojit

f_numba = autojit(f_python)