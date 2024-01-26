/**
 * file: 102-zombie.c
 * Author: Brennan 
 */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>

/**
 * infinite while - Run an ifinite while loop
 *
 * Return: 0 Always
 */
int infinite_while(void)
{
	int i;
	while (i)
	{
		sleep(i);
	}
	return (0);
}

/**
 * main - write file for five zombie processes
 *
 * Return: 0 Always
 */
int main (void)
{
	pid_t pid;
	char num = 0;

	while (num < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			num++;
		}
		else
			exit (0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
