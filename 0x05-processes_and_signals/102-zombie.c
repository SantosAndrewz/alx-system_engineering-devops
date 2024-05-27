#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - indefinately runs
 * Return: 0 on sucess.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point to the program creating 5 zombie processes
 * Return: 0 when successful.
 */
int main(void)
{
	int processes_chld = 0;
	pid_t pid;

	while (processes_chld < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %d\n", (int)(pid));
		processes_chld++;
	}
	if (pid != 0)
		infinite_while();
	return (0);

}
