#include <bits/stdc++.h>
#include <math.h>

#define endl '\n'

using ll = long long;

using namespace std;

void solveA() {
    ll res = 0;
    string s;

    while (cin >> s) {
        int cur = 0, i = 0;

        while (i < s.size() && !(int(s[i]) >= 48 && int(s[i]) <= 57))
            i++;

        cur += 10 * (int(s[i]) - 48);

        i = s.size() - 1;
        while (i >= 0 && !(int(s[i]) >= 48 && int(s[i]) <= 57))
            i--;
        cur += int(s[i]) - 48;
        res += cur;
    }
    cout << res;
}

void general(vector <int> &inds, map <int, int> &vals, string name, int val, string s) {
    int i = s.find_first_of(name);
    if (i != -1) {
        vals[i] = val;
        inds.push_back(i);
    }
    int j = s.find_last_of(name);
    if (j != -1) {
        vals[j] = val;
        inds.push_back(j);
    }
}

void solveB() {
    string s;
    map <string, int> name_to_val = {{"zero", 0}, 
                                    {"one", 1}, 
                                    {"two", 2},
                                    {"three", 3}, 
                                    {"four", 4},
                                    {"five", 5}, 
                                    {"six", 6},
                                    {"seven", 7}, 
                                    {"eight", 8},
                                    {"nine", 9}};

    while (cin >> s) {
        vector <int> inds;
        map <int, int> vals;
        for (auto p : name_to_val) {
            general(inds, vals, p.first, p.second, s);
            cout << p.first << ' ' << p.second << endl;
        }
        for (auto i : inds)
            cout << i << ' ';
    }
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

    freopen("input.txt", "rt", stdin);
	solveB();
    cout << endl;
    string s = "onetwothreeone";
    int i = s.find_last_of("eight");
    cout << i;

	return 0;
}
