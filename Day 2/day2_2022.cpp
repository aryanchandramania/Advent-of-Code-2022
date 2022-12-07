/* The one with Rock, Paper, Scissors */

#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main()
{
    ifstream f("input.txt");
    string x;
    int score = 0;
    map<char, int> mappy;
    mappy['X'] = 1, mappy['Y'] = 2, mappy['Z'] = 3;
    map<string, int> scorer;
    scorer["A Y"] = 1+3, scorer["A Z"] = 2+6, scorer["A X"] = 3+0;
    scorer["B X"] = 1+0, scorer["B Y"] = 2+3, scorer["B Z"] = 3+6;
    scorer["C Z"] = 1+6, scorer["C X"] = 2+0, scorer["C Y"] = 3+3;

    while(getline(f, x))
    {
        cout << x << endl;
        char opp = x[0], you = x[2];
        // score += mappy[you];
        score += scorer[x];
    }

    cout << score << endl;
}