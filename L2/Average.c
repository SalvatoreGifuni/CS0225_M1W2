#include <stdio.h>

int main() {
    float sum = 0;
    float average;
    float nums[] = {22.8, 55.3, 66.9, 88};
    float nums_length = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < nums_length + 1; i++) {
        sum += nums[i];
    };

    average = sum/nums_length;
    printf("The average of %2.2f, %2.2f, %2.2f, %2.2f is: %2.2f", nums[0], nums[1], nums[2], nums[3], average);
    return 0;

}