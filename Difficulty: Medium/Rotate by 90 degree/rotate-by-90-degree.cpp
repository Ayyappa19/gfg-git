//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

/* matrix : given input matrix, you are require
 to change it in place without using extra space */
void rotate(vector<vector<int> >& a) {
    // Your code goes here
    int n=a.size();
        int k=n;
        vector<vector<int>>v(n,vector<int>(n,0));
        for(int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                v[j][n-i-1]=a[i][j];
            }
        }
        for (int i=0;i<n;i++){
            for( int j=0;j<n;j++){
            a[i][j]=v[i][j];}
        }
        
    }



//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int> > matrix(n);
        for (int i = 0; i < n; i++) {
            matrix[i].resize(n);
            for (int j = 0; j < n; j++)
                cin >> matrix[i][j];
        }
        rotate(matrix);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; j++)
                cout << matrix[i][j] << " ";
            cout << "\n";
        }

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends