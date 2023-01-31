#include<bits/stdc++.h>

using namespace std;

int main()
{
    int bucket_size,op_rate,time_steps,cur_size=0;
    cout<<"Enter the bucket size: ";
    cin>>bucket_size;
    cout<<"Enter the steps to simulate:";
    cin>>time_steps;
    cout<<"Enter the variable input rates for "<<time_steps<<" seconds: ";
    int ip_rate[time_steps];
    for(int i=0;i<time_steps;i++)
        cin>>ip_rate[i];
    cout<<"Enter the output rate:";
    cin>>op_rate;
    for(int i=0;i<time_steps;i++)
    {
        int space_left=bucket_size-cur_size;
        int loss=0;
        if(ip_rate[i]<=space_left)
            cur_size+=ip_rate[i];
        else
        {
            loss=ip_rate[i]-space_left;
            cur_size=bucket_size;
        }
        if(cur_size>op_rate)
            cur_size-=op_rate;
        else
            cur_size=0;    
        cout<<"Time="<<i<<"s | Bucket/Buffer status:"<<cur_size<<"/"<<bucket_size<<", Packet loss= "<<loss<<endl;
    }
}
