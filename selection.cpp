#include <bits/stdc++.h>
using namespace std;
void swap(int *f,int *l){
    int temp=*f;
    *f=*l;
    *l=temp;

}
void selectionSort(int arr[], int n){
    int i=0,min_idx,j;

    for(i=0; i<n-1;i++){
        min_idx=i;
         for(j=i+1;j<n;j++){
             if(arr[j]<arr[min_idx]){
                 min_idx=j;
             }
         }
       swap(&arr[min_idx],&arr[i]);
    }
}
void printArray(int arr[],int size){
    int i;
    for(i=0;i<size;i++){
        cout<<arr[i]<<" ";
        cout<<endl;
    }

}
//Driver program
int main(){
    int n,k=0,arr[10];
    cout<<"Enter the length of the array: "<<endl;
    cin>>n;
    cout<<"Enter the  array: "<<endl;
    for(k=0;k<n;k++){
        cin>>arr[k];
    }
    selectionSort(arr,n);
    cout<<"Sorted array \n";
    printArray(arr,n);
    return 0;
}
