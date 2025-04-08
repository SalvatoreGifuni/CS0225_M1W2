#include <stdio.h>

int main() {
    float num1;
    float num2;

    printf("Please, enter first number (float): ");
    scanf("%f", &num1);

    printf("Please, enter second number(float): ");
    scanf("%f", &num2);

    float product = num1*num2;
    printf("Product of %3.2f*%3.2f = %3.2f", num1, num2, product);
    return 0;
}