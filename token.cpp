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
    cout << "Enter Number of steps to simulate:  ";
    cin >> nop;
    cout << "\nEnter "<< nop << " values of input data: ";
    for (i=0;i<nop;i++){
        cin >> a[i];
    }
    int incr = 0;
    i=0;         
    while(i<nop){//
        if (tokens<Bsize ){
            int temp = tokens+tokenRate;
            if( Bsize>temp){
                incr = tokenRate;
            }else{
                incr = Bsize-tokens;
            }
            cout << "\n" << incr << " tokens added";
            tokens+=incr;
        }else
            cout << "\nBucket is full";
        if(a[i] > tokens){
            if(a[i]<=Bsize){
                cout << "\nInsufficient Tokens.. Packet waiting..";
            }else if (a[i]>Bsize){
                if(Bsize > tokens){
                    cout << "\nData bigger than bucket size.. waiting till bucket is full..";
                }if(Bsize == tokens){
                    cout << "\nTransmitted Data: " << Bsize <<"Mb... Loss: " << a[i]-Bsize <<"Mb\n";
                    i++;
                    tokens=0;
                }
            }
        }
        else{
            tokens-=a[i];
            cout << "\nData of size "<< a[i]<< "Mb Transmitted \n";
            i++;
        }
        
        sleep(1);
    }
    return 0;
}
