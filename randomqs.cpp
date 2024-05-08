#include<iostream>
#include<vector>

using namespace std;

int swapcost = 0;
void quickSort(int (&nums)[], int start, int end, int n){
    if(start >= end || start<0 || start > n || end>n || end < n){
        return;
    }
    int pivotel = nums[start];
    int s=start,e=end;
    while(start <= end ){
        while(nums[start] <= pivotel && start<n){
            start+= 1;
        }
        cout<<"end element - "<<nums[end];
        while(nums[end] > pivotel){
            end -= 1;
        }
        cout<<endl<<"end val - "<<end<<endl;
        if(start < end){
            swap(nums[start],nums[end]);
            swapcost += 1;
        }
    }
    cout<<"start end pair "<<start<<' '<<end<<endl;
    cout<<endl;
    
    cout<<endl;
    swap(nums[s],nums[end]);
    for(int i =0; i<6 ;i++){
        cout<<nums[i]<<" ";
    }
    swapcost += 1;
    quickSort(nums,s,end-1,n);
    quickSort(nums,end +1,e,n);
    return;
}

int main(){
    // int nums[] = {5,4,3,2,1};
    int nums[] = {4,10,45,67,0,3};
    for(auto a : nums){
        cout<<a<<" ";
    }
    cout<<endl;
    quickSort(nums,0,5,5);
    for(auto a : nums){
        cout<<a<<" ";
    }
}