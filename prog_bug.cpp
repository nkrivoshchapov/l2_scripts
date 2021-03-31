#include <mpi.h>
#include <stdio.h>
#include <list>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

char* to_string(int a) {
        char* res=new char[5];
        sprintf(res,"%d",a);
        return res;
}

int main (int argc, char** argv) {
        MPI_Init(NULL, NULL);

        char *str = new char[200];
        for(int i =0;i<200;++i)
                str[i]='\0';

        int world_size;
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);

        int world_rank;
        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

        char processor_name[MPI_MAX_PROCESSOR_NAME];
        int name_len;
        MPI_Get_processor_name(processor_name, &name_len);

        printf("Hello world from processor %s, rank %d out of %d processors\n",processor_name, world_rank, world_size);
        string namel;

        namel += "python prep_bug.py ";
        namel += to_string(world_rank);
        namel += " ";
        namel += to_string(world_size);
        strcpy(str, namel.c_str());
        printf("Starting script with %s", str);
        system(str);

        MPI_Finalize();
}
