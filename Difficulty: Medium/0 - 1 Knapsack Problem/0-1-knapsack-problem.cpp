//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to return max value that can be put in knapsack of capacity W.
    vector<int> l;

    void fun(int W, const vector<int>& wt, const vector<int>& val, int s, int i, int x) {
        if (x > W) {
            return;
        }
        if (i >= wt.size()) {
            l.push_back(s);
            return;
        }
        fun(W, wt, val, s + val[i], i + 1, x + wt[i]);
        fun(W, wt, val, s, i + 1, x);
    }

    int knapSack(int W, const vector<int>& wt, const vector<int>& val) {
        l.clear(); 
        fun(W, wt, val, 0, 0, 0);
        if (l.empty()) {
            return 0; 
        }
        return *max_element(l.begin(), l.end());
    }
};

//{ Driver Code Starts.

int main() {
    // taking total testcases
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        // reading number of elements and weight
        int n, w;
        vector<int> arr, val, wt, drr;
        string ip;
        int number;
        getline(cin, ip);
        stringstream ss(ip);

        while (ss >> number) {
            arr.push_back(number);
        }

        getline(cin, ip);
        ss.clear();
        ss.str(ip);

        while (ss >> number) {
            val.push_back(number);
        }

        w = arr[0];
        n = val.size();
        getline(cin, ip);
        ss.clear();
        ss.str(ip);

        while (ss >> number) {
            wt.push_back(number);
        }
        Solution ob;
        cout << ob.knapSack(w, wt, val) << endl;
    }
    return 0;
}
// } Driver Code Ends