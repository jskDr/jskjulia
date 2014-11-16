#include <stdio.h>
#include <time.h>

float f_c(int n){
	float s = 0;
	int i;
	for( i=0; i<n; i++) {
		s += i/2.0;
	}
	return s;
}

void main( int argn, char* argv[]){
	int n; 
	clock_t launch, done;
	double diff;
	float s;

	// Processing time is calculated
	launch = clock();
	n = atoi( argv[1]);
	s = f_c( n);
	printf("%f\n", s);	
	done = clock();
	diff = (done - launch) / (double) CLOCKS_PER_SEC;
	printf("TIME: %f \n", diff);
}