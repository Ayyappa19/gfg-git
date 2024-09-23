//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> findTwoElement(vector<int>& arr) {
        // code here
        int maxx=arr[0];
        bool c=false;
        vector<int>ans;
        for( int i=1;i<arr.size();i++){
            if (arr[i]>maxx){
                maxx=arr[i];
            }
            
        }
        vector<int>v(maxx+1,0);
        for(int i=0;i<arr.size();i++){
            
                v[arr[i]]+=1;
        }
        for(int i=1;i<v.size();i++){
            // cout<<v[i]<<" "<<i<<" ";
            if (v[i]==2){
                // cout<<"HI";
                ans.push_back(i);
                
            }
        }
        for( int i=1;i<v.size();i++){
            if(v[i]==0){
                // cout<<"HI";
                c=true;
                ans.push_back(i);
                break;
                
            }
        }
        if(c==false)ans.push_back(maxx+1);
        return ans;
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findTwoElement(a);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}
// } Driver Code Ends