#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int n = 0, startIndex, minY = INT_MAX;
    cout<<"enter the number of coordinates "<<endl;
    cin>>n;
    vector<pair<int,int>> coordinates(n); 
    for(int i = 0; i<n; i++){
        int a, b;
        cout<<" enter a coordinate "<<endl;
        cin>>a>>b;
        coordinates.push_back({a,b});
        if(b < minY){
            minY = b;
            startIndex = i;
        }
    } 
    
}