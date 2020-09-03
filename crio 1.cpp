#include<string.h>
#include<iostream.h>
#include<stdio.h>
#include<conio.h>
main()
{
    char a[10],b[5];
    int i,j,c,summin=0,summax=0;
    cout<<"Enter 5 integers seprated by space"<<endl;
    gets(a);
    for(i=0;i<10;i++)
    {
        for(j=0;j<5;j++)
        {
            if(i%2==0)
            {
                b[j]=a[i];
            }
            
        }
    }
    for (i = 0; i < 5-1; i++)
    {
        for (j = 0; j < 5-i-1; j++)
        {
            if (b[j] > b[j+1]
                {
                    c= b[j];
                    b[j] = b[j+1];
                    b[j+1] = c;
                }
        }
    }
    for(i=0;<i<4;i++)
    {
        summin+=b[i];
    }
    for(i=5;<i<1;i--)
    {
        summax+=b[i];
    }
    cout<<summin<<" "<<summax;
                
}