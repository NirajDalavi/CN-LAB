#include <iostream>

#include <unistd.h>
using namespace std;

int main(){
    int i,tokenRate,tokens=0,Bsize,nop=3;
    int a[nop];


    cout << "Enter Token Rate:  ";
    cin >> tokenRate;
    cout << "Enter Bucket Size:  ";
    cin >> Bsize;
    cout << "Enter Initial Tokens:  ";
    cin >> tokens;
    
    cout << "\nEnter "<< nop << " values of input data: ";
    for (i=0;i<nop;i++){
        cin >> a[i];
    }
    int incr = 0;//  Bsize  = 10 , tr =2 ,  init t = 4
    i=0;   
    int flag=0;      
    ///cout << "\nTOkens : " << tokens;          // 3
    while(i<nop){//
        if (tokens<Bsize ){
            incr=0;
            int temp = tokens+tokenRate;
            if( Bsize>temp){
                //cout << "Here tokens = "<< tokens;
                incr = tokenRate;
            }else{
                incr = Bsize-tokens;
            }
            cout << "\n" << incr << " tokens added";
            tokens+=incr;
        }else
            cout << "Bucket is full";
        if(a[i] > tokens){
            if(a[i]<Bsize){
                cout << "\nInsufficient Tokens.. Packet waiting..";
                goto last;
            }else if (a[i]>Bsize){
                if(Bsize > tokens){
                    cout << "\nData bigger than bucket size.. waiting till bucket is full..";
                    goto last;
                }if(Bsize == tokens){
                    cout << "\nTransmitted Data: " << Bsize <<"Mb... Loss: " << a[i]-Bsize <<"\n";
                    i++;
                    tokens-=Bsize;
                }
            }
            last:
            continue;
        }
        if(a[i]<=tokens){
            tokens-=a[i];
            cout << "\n Data of size "<< a[i]<< "Mb Transmitted \n";
            i++;
        }
        
        sleep(1);
    }
    return 0;
}
