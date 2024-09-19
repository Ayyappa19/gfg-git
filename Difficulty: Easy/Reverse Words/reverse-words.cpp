//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to reverse words in a given string.
    vector<string> s;
    void splitting (string sss){
        string ss;
        for( int i=0;i<sss.size();i++){
            if (sss[i]=='.'){
                s.push_back(ss);
                ss="";
            }
            else{
                ss+=sss[i];
            }
        }
        s.push_back(ss);
    }
    string reverseWords(string str) {
        // code here
        splitting(str);
        string v="";
        int i=s.size();
        for(i=s.size()-1;i>0;i--){
            v+=s[i];
            v+='.';
        }
        v+=s[i];
        return v;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution obj;
        cout << obj.reverseWords(s) << endl;
    }
}
// } Driver Code Ends