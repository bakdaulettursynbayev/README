
#include <iostream>
using namespace std;

bool canFit(int side, int w, int h, int n) {
    return (side/w)*(side/h)>= n;
}

int main() {
    int w,h,n;
    cin>>w>>h>>n;

    int left=0, right=1;
    
    while (!canFit(right,w,h,n)) {
        right *= 2;
    }

    while (right>left + 1) {
        int mid = (left+right)/2;
        if (canFit(mid,w,h,n)) {
            right = mid; 
        } else {
            left = mid;
        }
    }

    cout<<right<<endl;
    return 0;
}
