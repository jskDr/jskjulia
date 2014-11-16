#include <stdio.h>

float f_c(int n){
	float s = 0;
	int i;
	for( i=0; i<n; i++) {
		// printf( "%d \n", i);
		s += i/2.0;
		// printf( "%f \n", s);
	}
	return s;
}

void main( int argn, char* argv[]){
	int n = atoi( argv[1]);
	float s = f_c( n);
	printf("%f\n", s);	
}

