#include<stdio.h>
int main()
{
	int i,a;
	printf("enter the desired number: ");
	scanf("%d",&i);
	for(a=1;a<=10;a++)
	{
		int b=i*a;
		printf("%d\n",b);
	}
}
