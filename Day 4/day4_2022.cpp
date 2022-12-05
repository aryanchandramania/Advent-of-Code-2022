#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main()
{
    ifstream f("input.txt");
    int count = 0;
    string s;

    while(getline(f, s))
    {
        string elf1 = s.substr(0, s.find(','));
        string elf2 = s.substr(s.find(',')+1, s.size());
        int ll = stoi(elf1.substr(0, elf1.find('-'))), lr = stoi(elf1.substr(elf1.find('-')+1, elf1.size()));
        int rl = stoi(elf2.substr(0, elf2.find('-'))), rr = stoi(elf2.substr(elf2.find('-')+1, elf2.size()));        
        if(((ll <= rl && lr >= rl) || (ll >= rl && ll <= rr)) || ((rr <= lr && ll <= rr) || (lr <= rr && lr >= rl)))
            count++;
    }

    cout << count << endl;
}