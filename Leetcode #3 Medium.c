//Leetcode #3 Longest Substring Without Repeating Characters

#include <stdio.h>

int lengthOfLongestSubstring(char* s) {
    int i = 0, start=0;
    int j = 0, end = 0;
    int ans = 0;
    int len = strlen(s);
    char sub[50000];
    while (i < len && j < len) {
        int m = i, n = 0;
        for (m = i; m < j; m++)
            sub[n++] = s[m];
        sub[n] = '\0';
        if (charIncludeString(sub, s[j]) == 0) {
            j++;
            if (j - i > ans) {
                ans = j - i;
                start = i, end = j;
            }
        }
        else {
            i++;
        }
    }

    int m = start, n = 0;
    for (m = start; m <= end; m++)
        sub[n++] = s[m];
    sub[n] = '\0';
    //printf("Longest Substring Without Repeating Characters: num = %d  str = %s\n", ans, sub);
    return ans;
}

int charIncludeString(char *s, char *c) {
    int i = 0;
    for (i = 0; i < strlen(s); i++) {
        if (s[i] == c) {
            return 1;
        }
    }
    return 0;
}

int main(void)
{
    char s[50000];
    printf("input a string: ");
    scanf_s("%s", s);

    int ans = 0;
    ans = lengthOfLongestSubstring(s);

    system("pause");
    return 0;
}

