#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long sum = 0, mx = -1;
    string no;
    vector<long long> v;
    ifstream f("input.txt");

    while(getline(f, no))
    {
        if(no == "")
        {
            v.push_back(-sum);
            sum = 0;    
        }
        else
            sum += (long long) stoi(no);
    }
    sort(v.begin(), v.end());
    cout << -v[0] -v[1] -v[2] << endl;
}