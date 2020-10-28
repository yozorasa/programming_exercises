//Leetcode #1480 Running Sum of 1d Array

void printArr(int* arr, int len){
	int i = 0;
	printf("[%d", arr[0]);
	for (i = 1; i < len; i++)
		printf(", %d", arr[i]);
	printf("]\n");
}

int* runningSum(int* nums, int numsSize, int* returnSize){
    int i = 0;
    int* ans = nums;
    for (i = 1; i < numsSize; i++)
        ans[i] += ans[i-1];
    //*returnSize = numsSize;
    return ans;
}

int main(void)
{
    int len = 0;
    printf("number of array: ");
    scanf("%d", &len);
    int i = 0;
    int* nums = malloc(len*sizeof(int));
    for (i = 0; i < len; i++){
        printf("arr[%d] = ", i);
        scanf("%d", &nums[i]);
    }
    printf("nums = ");
    printArr(nums, len);

    int numsSize = len;
    int* returnSize;
    int* ans = runningSum(nums, numsSize, returnSize);
    printf("ans = ");
    printArr(ans, len);

    system("pause");
    return 0;
}
