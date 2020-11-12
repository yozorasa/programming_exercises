//Leetcode #5 Longest Palindromic Substring

#include <stdio.h>

int palindromic(char *s, int start, int end) {
    int i = start, j = end;
    for (i = start, j = end; i<j; i++, j--) {
        if (s[i] != s[j])
            return 0;
    }
    return 1;
}

void copyStr(char *str2, char *str1, int start, int end){
    int i = start, n = 0;
    for (i = start; i <= end; i++)
        str2[n++] = str1[i];
    str2[n] = '\0';
    return;
}

char * longestPalindrome(char * s){
    int i = 0, j = 0;
    int posi = 0, posj = 0;
    char *ans = malloc((strlen(s)+1)*sizeof(char));
    int maxlen = 0;
    for(i = 0; i < strlen(s); i++) {
        for(j = i+maxlen; j < strlen(s); j++) {
            if (palindromic(s, i, j) == 1 && j-i>maxlen) {
                maxlen = j-i;
                posi = i;
                posj = j;
            }
        }
    }
    copyStr(ans, s, posi, posj);
    return ans;
}

int main(void)
{
    char s[1000];
    printf("input a string: ");
    scanf_s("%s", s);

    char *ans = longestPalindrome(s);
    printf("Longest Palindromic Substring: %s\n", ans);

    system("pause");
    return 0;
}

