#include <bits/stdc++.h>
#include <math.h>

#define endl '\n'

using ll = long long;

using namespace std;

bool isNum(char candidate) {
    if (int(candidate) >= int('0') && int(candidate) <= int('9'))
        return true;
    return false;
}

int parseNum(vector <string> &a, int row, int col) {
    int res = 0;
    int i = col;

    while (i > 0 && isNum(a[row][i - 1]))
        i--;

    while (i < a[row].size() && isNum(a[row][i])) {
        res = res * 10 + int(a[row][i]) - int('0');
        i++;
    }

    return res;
}

int findSymbol(vector <string> &a, int row, int col) {
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

    bool prev_found = false;
    int prev_row = -1;
    int res = 1;
    int nums_count = 0;

    for (auto p : ds) {
        int drow = p.first, dcol = p.second;

        if (row + drow >= 0 && row + drow < a.size())
            if (col + dcol >= 0 && col + dcol < a[col].size()) {
                if (!isNum(a[row + drow][col + dcol])) {
                    prev_row = -1;
                    prev_found = false;
                    continue;
                }

                if (prev_found && prev_row == (row + drow))
                    continue;

                prev_row = row + drow;
                int num = parseNum(a, row + drow, col + dcol);
                nums_count++;
                res *= num;
                prev_found = true;
            }
    }
    return (nums_count == 2 ? res : 0);
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

            if (cur != '*')
                continue;

            res += findSymbol(a, row, col);
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
