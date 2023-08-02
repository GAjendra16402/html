#include <stdio.h>

int main() {
    int base = 2;

    while (base <= 10) {
        int multiplier = 1;

        while (multiplier <= 10) {
            printf("%d x %d = %d\n", base, multiplier, base * multiplier);
            multiplier++;
        }

        printf("\n");
        base++;
    }

    return 0;
}

