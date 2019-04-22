#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef struct dynarray{
    size_t* array;
    size_t used;
    size_t size;
} dynarray;

void initArray(dynarray* a, size_t initialSize){
    if (initialSize <= 0) initialSize = 1;
    a->array = (size_t* ) malloc (initialSize * sizeof(size_t));
    a->used = 0;
    a->size = initialSize;
}

void insertArray(dynarray* a, size_t element){
    if (a->used == a->size){
        a->size *= 2;
        a->array = (size_t* ) realloc(a->array, a->size * sizeof(size_t));
    }
    a->array[a->used++] = element;
}

void freeArray(dynarray* a){
    free(a->array);
    a->array = NULL;
    a->used = a->size = 0;
}

int checkPrime(size_t i){
    for(size_t k = 2; k <= sqrt(i); k++) if (i%k == 0) return 0;
    return 1;
}

void checkAllPrimes(size_t n){
    dynarray primes;
    initArray(&primes, 10);
    insertArray(&primes, 2);

    for(size_t i = 2; i <= n; i++){
        if (checkPrime(i)) insertArray(&primes, i);
    }

    char fileName[100];
    snprintf(fileName, sizeof(fileName), "primes-%d.txt", n);
    FILE* f = fopen(fileName, "w");

    if (f == NULL){
        printf("Erreur lors de l'ouverture du fichier");
        exit(1);
    }
    
    for(size_t i = 0; i < primes.used; i++){
            fprintf(f, "%d\n", primes.array[i]);
    }

    fclose(f);

    freeArray(&primes);
}

int main(){
    size_t n = 0;
    printf("Entrez le nombre d'itérations : ");
    if(scanf("%d", &n)){
        checkAllPrimes(n);
    }
    else{
        printf("L'entrée n'est pas un nombre");
    }
    
    return 0;
}
