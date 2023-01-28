#include<bits/stdc++.h>

using namespace std;

int main()
{
    int bucket_size,ip_rate,op_rate,time_steps,cur_size=0;
    cout<<"Enter the bucket size: ";
    cin>>bucket_size;
    cout<<"Enter input rate:";
    cin>>ip_rate;
    cout<<"Enter the output rate:";
    cin>>op_rate;
    cout<<"Enter the steps to simulate:";
    cin>>time_steps;
    for(int i=0;i<time_steps;i++)
    {
        int space_left=bucket_size-cur_size;
        int loss=0;
        if(ip_rate<=space_left)
            cur_size+=ip_rate;
        else
        {
            loss=ip_rate-space_left;
            cur_size=bucket_size;
        }
        cur_size-=op_rate;
        cout<<"Time="<<i<<"s | Bucket/Buffer status:"<<cur_size<<"/"<<bucket_size<<", Packet loss= "<<loss<<endl;
    }
}