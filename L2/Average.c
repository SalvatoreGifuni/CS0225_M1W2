#include <stdio.h>

int main() {
    int sum = 0;
    float average;
    int nums[] = {22, 55, 66, 88};
    int nums_length = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < nums_length + 1; i++) {
        sum += nums[i];
    };

    average = sum/nums_length;
    printf("The average of %d, %d, %d, %d is: %2.2f", nums[0], nums[1], nums[2], nums[3], average);
    return 0;

}