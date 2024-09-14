//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
  public:

    void rearrange(vector<int> &arr) {
        // code here
        vector<int>pos;
        vector<int>neg;
        for(int i=0;i<arr.size();i++){
            if(arr[i]<0){
                neg.push_back(arr[i]);
            }
            else pos.push_back(arr[i]);
            
        }
        int ne=neg.size();
        int po=pos.size();
        vector<int>ans;
        // for(int i=0;i<arr.size();i++){
        
            
        // }
        int i=0;
        int j=0;
        while(i<ne and j<po){
            ans.push_back(pos[j]);
            ans.push_back(neg[i]);
            i++;
            j++;
        }
        while(i<ne){
            ans.push_back(neg[i]);
            i++;
        }
        while(j<po){
            ans.push_back(pos[j]);
            j++;
        }
        for( int i=0;i<ans.size();i++){
            arr[i]=ans[i];
        }
        
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        int num;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            arr.push_back(num);
        }
        Solution ob;
        ob.rearrange(arr);
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends