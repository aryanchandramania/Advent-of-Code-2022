#include <bits/stdc++.h>
using namespace std;
#define int long long

int add(char repeat)
{
    if (islower(repeat))
        return (repeat - 'a' + 1);
    else
        return (repeat - 'A' + 27);
}

int32_t main()
{
    int sum = 0;
    string s1, s2, s3;

    ifstream f("input.txt");
    while (getline(f, s1))
    {
        string m, string_intersection;
        getline(f, s2);
        getline(f, s3);
        char repeat;
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        sort(s3.begin(), s3.end());
        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(m));
        set_intersection(m.begin(), m.end(), s3.begin(), s3.end(), back_inserter(string_intersection));
        repeat = string_intersection[0];
        sum += add(repeat);
    }

    cout << sum << endl;
}