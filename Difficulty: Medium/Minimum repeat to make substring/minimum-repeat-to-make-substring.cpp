//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int minRepeats(string& s1, string& s2) {
        // code here
       
        string s3 = s1;
        int cnt = 1;
        
        
        while (s3.length() < s2.length()) {
            s3 += s1;
            cnt++;
        }
        
        
        if (s3.find(s2) != string::npos) return cnt;
    
        
        s3 += s1;
        cnt++;
    
        
        if (s3.find(s2) != std::string::npos) return cnt;
    
       
        return -1;

    }
};

//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {
        string A, B;
        getline(cin, A);
        getline(cin, B);

        Solution ob;
        cout << ob.minRepeats(A, B) << endl;
    }
    return 0;
}
// } Driver Code Ends