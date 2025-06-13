//{ Driver Code Starts
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

/* Linked list Node */
struct Node {
    int data;
    struct Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

Node* buildList() {
    vector<int> arr;
    string input;
    getline(cin, input);
    stringstream ss(input);
    int number;
    while (ss >> number) {
        arr.push_back(number);
    }
    if (arr.empty()) {
        return NULL;
    }
    int val = arr[0];
    int size = arr.size();

    Node* head = new Node(val);
    Node* tail = head;

    for (int i = 1; i < size; i++) {
        val = arr[i];
        tail->next = new Node(val);
        tail = tail->next;
    }

    return head;
}

void printList(Node* n) {
    while (n) {
        cout << n->data << " ";
        n = n->next;
    }
    cout << endl;
}


// } Driver Code Ends
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution {
  public:
    Node* reverseLL(Node* head)
    {
        if(head==NULL)  return NULL;
        Node* curr=head,*prev=NULL,*next=NULL;
        while(curr!=NULL)
        {
            next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        return prev; 
    }
    Node* addTwoLists(Node* l1, Node* l2) {
        // code here
        l1=reverseLL(l1);
        l2=reverseLL(l2);
        Node* temp1=l1,*temp2=l2;
        Node* dummyNode=new Node(-1);
        dummyNode->next=NULL;
        Node* temp=dummyNode;
        int carry=0,sum=0;
        while(l1!=NULL || l2!=NULL || carry>0)
        {
            sum=carry;
            if(l1!=NULL)
            {
                sum+=l1->data;
                l1=l1->next;
            }
            if(l2!=NULL)
            {
                sum+=l2->data;
                l2=l2->next;
            }
            temp->next=new Node(sum%10);
            temp=temp->next;
            carry=sum/10;
        }
        dummyNode=dummyNode->next;
        Node* final=reverseLL(dummyNode);
        while(final && final->data==0)
            final=final->next; 
        return final;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To ignore the newline character after the integer input

    while (t--) {
        Node* num1 = buildList();
        Node* num2 = buildList();
        Solution ob;
        Node* res = ob.addTwoLists(num1, num2);
        printList(res);
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends