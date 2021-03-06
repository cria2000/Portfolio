#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>

enum { STATE_A, STATE_B } state=STATE_A;
pthread_cond_t		condA = PTHREAD_COND_INITIALIZER;
pthread_cond_t		condB = PTHREAD_COND_INITIALIZER;
pthread_mutex_t		mutex = PTHREAD_MUTEX_INITIALIZER;

void *threadA()
{
	int i=0, rValue, loopNum;
	
	while(i<5)
	{
		pthread_mutex_lock(&mutex);
		while(state!=STATE_A)
			pthread_cond_wait(&condA,&mutex);
		pthread_mutex_unlock(&mutex);
		for(loopNum = 1; loopNum<=5; loopNum++)
			printf("Hello %d\n", loopNum);

		pthread_mutex_lock(&mutex);
		state = STATE_B;
		pthread_cond_signal(&condB);
		pthread_mutex_unlock(&mutex);

		i++;
	}
	return 0;
}
void *threadB()
{
	int n=0, rValue;

	while(n<5)
	{
		pthread_mutex_lock(&mutex);
		while(state!=STATE_B)
			pthread_cond_wait(&condB, &mutex);
		pthread_mutex_unlock(&mutex);

		printf("Goodbye\n");
		pthread_mutex_lock(&mutex);
		state=STATE_A;
		pthread_cond_signal(&condA);
		pthread_mutex_unlock(&mutex);

		n++;
	}
	return 0;
}
int main(int argc, char *argv[])
{
	pthread_t a, b;
	pthread_create(&a, NULL, threadA, NULL);
	pthread_create(&b, NULL, threadB, NULL);

	pthread_join(a,NULL);
	pthread_join(b,NULL);
}
