#include <stdio.h>

int main(void)
{
    int height = 0;
    printf("input the height of dimond (must be odd): ");
    scanf_s("%d", &height);
    height = height / 2;
    
    int i = 0;
    for (i = 0; i < height; i++)
    {
        int j = 0;
        for (j = 0; j < height - i; j++)
            printf(" ");
        for (j = 0; j < i * 2 + 1; j++)
            printf("*");
        printf("\n");
    }
    for (i = height; i >= 0; i--)
    {
        int j = 0;
        for (j = 0; j < height - i; j++)
            printf(" ");
        for (j = 0; j < i * 2 + 1; j++)
            printf("*");
        printf("\n");
    }

    system("pause");
    return 0;
}