#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char* argv[])
{
    int source_file;
    int destination_file;
    int read_byte;
    int write_byte;
    char buff_size [4096];

    /*Verify correct formatting of command*/
    if(argc != 3)
    {
        printf("incorrect amount of arguments, ./FileCopy.c {source} {destination}");
        return -1;
    }

    /* opens source file*/
    source_file = open(argv[1], O_RDONLY);
    if (source_file == -1)
    {
        printf("Could not open source file");
        return -1;
    }

    /*open destination file*/
    destination_file = open(argv[2], O_CREAT | O_WRONLY | O_SYNC | O_TRUNC, S_IRUSR | S_IWUSR);
    if (destination_file == -1)
    {
        printf("Could not open destination file");
        close(source_file);
        return -1;
    }

    /*Data transfer from source file to destination file */
    while((read_byte = read(source_file, buff_size, read_byte)) > 0)
    {
        write_byte = write(destination_file, buff_size, read_byte);
        if (write_byte != read_byte)
        {
            printf("Error copying source file to destination");
            close(source_file);
            close(destination_file);
            return -1;
        }
    }
    if (read_byte == -1)
    {
        printf ("Error reading source file");
        close(source_file);
        close(destination_file);
        return -1;
    }
    printf("Successfully copied contents of source file to destination file");
    close(source_file);
    close(destination_file);
    return 0;
}
