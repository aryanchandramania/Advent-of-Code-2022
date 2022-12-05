#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main()
{
    fstream f;
    f.open("input.txt", ios::in);

    string line;
    string stack[10];
    while (getline(f, line))
    {
        if (isdigit(line[1]))
            break;

        for (int pos = 1, i = 0; pos < line.length(); ++i, pos += 4)
            if (isalpha(line[pos]))
                stack[i] += line[pos];
    }

    for (auto &s : stack)
        reverse(s.begin(), s.end());

    while (getline(f, line))
    {
        if (line.length() == 0)
            continue;

        int no_of_blocks, from, to;
        sscanf(line.c_str(), "move %lld from %lld to %lld", &no_of_blocks, &from, &to);

        from--, to--;

        for (int i = 0; i < no_of_blocks; ++i)
        {
            stack[to] += stack[from].back();
            stack[from].pop_back();
        }
    }

    string sol = "";
    for (auto &s : stack)
        if (s.length() > 0)
            sol += s.back();

    cout << sol << endl;
}