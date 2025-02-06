//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;


// } Driver Code Ends
class Solution {
  public:
    // Function to find the maximum money the thief can get.
    int findMaxSum(vector<int>& arr) {
        // Your code here
        vector<int>dp(arr.size()+1,0);
        int n=arr.size();
        dp[0]=arr[0];
        dp[1]=max(arr[0], arr[1]);
        for(int i=2;i<arr.size();i++){
            
            dp[i]=max(dp[i -2] + arr[i], dp[i - 1]);
        }
        return dp[n-1];
    }
};

// 9 4 11 12 6  12
// 9 9 20 21 26 33




//{ Driver Code Starts.

int main() {

    // taking total testcases
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        // calling function findMaxSum()
        cout << ob.findMaxSum(arr) << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends