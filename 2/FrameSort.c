#include<stdio.h>
struct frame{
int num;
char str[20];
};
struct frame arr[10];
int n;

void sort() /*Bubble sort */
{
int i,j;
struct frame temp;
for(i=0;i<n-1;i++)

for(j=0;j<n-i-1;j++)

if(arr[j].num>arr[j+1].num)
{ temp=arr[j];
arr[j]=arr[j+1];
arr[j+1]=temp;

}

}

int main()
{
int i;
system("clear");
printf("Enter the number of frames\n");
scanf("%d",&n);
printf("Enter the frame sequence number and frame contents\n");
for(i=0;i<n;i++)
scanf("%d%s",&arr[i].num,&arr[i].str);
sort();
printf("The frame in sequences\n");
for(i=0;i<n;i++)
printf("%d\t%s\n",arr[i].num,arr[i].str);
}
