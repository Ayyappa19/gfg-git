//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int maxPathSum(vector<int> &nums1, vector<int> &nums2) {
        // Code here
        int n = nums1.size();
        int m = nums2.size();
        int i = 0, j = 0;
        int sum1 = 0, sum2 = 0, result = 0;

        while (i < n && j < m) {
            if (nums1[i] == nums2[j]) {
                result += max(sum1, sum2) + nums1[i];
                sum1 = 0;
                sum2 = 0;
                i++;
                j++;
            } else if (nums1[i] < nums2[j]) {
                sum1 += nums1[i];
                i++;
            } else {
                sum2 += nums2[j];
                j++;
            }
        }
        while (i < n) {
            sum1 += nums1[i++];
        }
        while (j < m) {
            sum2 += nums2[j++];
        }

        result += max(sum1, sum2);

        return result;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr1;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr1.push_back(number);
        }
        vector<int> arr2;
        string input2;
        getline(cin, input2);
        stringstream ss2(input2);
        int number2;
        while (ss2 >> number2) {
            arr2.push_back(number2);
        }
        Solution ob;
        long long ans = ob.maxPathSum(arr1, arr2);
        cout << ans << endl;
    }
    return 0;
}
// } Driver Code Ends