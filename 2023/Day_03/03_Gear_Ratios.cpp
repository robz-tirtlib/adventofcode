#include <bits/stdc++.h>
#include <math.h>

#define endl '\n'

using ll = long long;

using namespace std;

bool isSymbol(char candidate) {
    if (int(candidate) >= int('0') && int(candidate) <= int('9') || candidate == '.')
        return false;
    return true;
}

bool findSymbol(vector <string> &a, int row, int col) {
    vector <pair <int, int>> ds = {
        {-1, -1},
        {-1, 0},
        {-1, 1},
        {0, 1},
        {1, 1},
        {1, 0},
        {1, -1},
        {0, -1},
    };

    for (auto p : ds) {
        int drow = p.first, dcol = p.second;

        if (row + drow >= 0 && row + drow < a.size())
            if (col + dcol >= 0 && col + dcol < a[col].size())
                if (isSymbol(a[row + drow][col + dcol]))
                    return true;
    }
    return false;
}

void solve() {
    vector <string> a;
    string s;

    while (cin >> s) {
        a.push_back(s);
    }

    int res = 0;
    int cur_num = 0;
    int adj = false;

    for (int row = 0; row < a.size(); row++) {
        for (int col = 0; col < a[row].size(); col++) {
            char cur = a[row][col];
            if (int(cur) > int('9') || int(cur) < int('0')) {
                if (adj)
                    res += cur_num;
                cur_num = 0;
                adj = false;
                continue;
            }

            int cur_val = int(cur) - int('0');
            cur_num = cur_num * 10 + cur_val;

            if (findSymbol(a, row, col))
                adj = true;
        }
    }

    cout << res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

    freopen("input.txt", "rt", stdin);
	solve();

	return 0;
}
