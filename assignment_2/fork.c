#include <stdio.h>
#include "unistd.h"

int main()
{
    // fork one process
    // Creating first child
    int child1 = fork();

    // fork another process
    // Creating second child. First child
    // also executes this line and creates
    // grandchild.
    int child2 = fork();

    // fork another process
    // creates third child
    // first and second child execute this line
    // creates grandchild and great-grandchild
    int child3 = fork();

    printf("Process created. ID: %d\n", getpid());

    return 0;
}
