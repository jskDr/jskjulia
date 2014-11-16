#This is cython code
def f_cython(n):
	cdef float s = 0
	for i in range( n):
		s += i/2.0
	return s

def f_cython_alldef(int n):
	cdef float s = 0
	cdef int i	
	for i in range( n):
		s += i/2.0
	return s

