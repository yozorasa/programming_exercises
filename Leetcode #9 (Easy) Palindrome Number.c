//Leetcode #9 Palindrome Number

#include <stdio.h>

void int2str(int x, char* s) {
    sprintf(s, "%d", x);
    return;
}

int isPalindrome(int x) {
    char sx[100], rx[100];
    int2str(x, sx);
    int i, j;
    for (i = 0, j = strlen(sx)-1; i < j; i++, j--) {
        if(sx[i] != sx[j])
            return 0;
    }
    return 1;
}

int main(void)
{
    int num = 0;
    printf("input a number: ");
    scanf_s("%d", &num);

    int ans = isPalindrome(num);
    ans == 1 ? printf("true\n") : printf("false\n");

    system("pause");
    return 0;
}

