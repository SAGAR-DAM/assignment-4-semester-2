/*Problem 4 assignment 4
exponential random number in c
NAME: SAGAR DAM;  DNAP*/

//including library functions
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//function for making exponential distribution....
float f(float x);

//main function
int main()
{
	int n= 10000,i ; 
	double  random[n], exprandom[n];
 
 	for (i = 1; i <= n; i++) 
  	{
    		random[i] = rand()/(double)RAND_MAX; //generating uniform normaized random numbers
       		if(random[i] !=0)
    		{
     		  	exprandom[i] = f(random[i]); //generating exponential random numbers
    		}
    		else
    		{
    			exprandom[i]=0;
    		}
	  }
/*printing data in file::*/
  FILE *data;
  data = fopen("data of problem 4.txt","w");
  for(i = 1;i<= n; i++)
  {
  	fprintf(data, "%f\n",exprandom[i]);
  }
  	return 0;
}

//making exponential distributed data
float f(float x)
{
	float z;
	z=-2.0* log((double)x);
	return(z);
}


