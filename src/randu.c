#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

static const char file_name[] = "dat/randu.dat"; //data file name

//long for current value of randu
long randu_value;

//constants to use in randu
long a = pow(2,16) + 3;
long m = pow(2,31);

//plant a seed for following randu numbers
void randu_init(double seed) {

	randu_value = seed;
}

//get next randu number
double randu_getnumber() {

	randu_value = ( (a * randu_value) % m);
	return (double) randu_value / m;
}


int main(void) {

	randu_init(time(NULL)); // init randu with current time as seed

	FILE *file = fopen(file_name, "w"); // open output file

	for (int i = 0; i < 10000; i++) {

		for (int j = 0; j < 3; j++) { // generate triple for 3D coords

			fprintf(file, "%f", randu_getnumber() );
			if(j < 2) fprintf(file, "\t"); // seperator only behind the first and second value
		}

		fprintf(file, "\n"); // new line after third value
	}

	fclose(file);

}
