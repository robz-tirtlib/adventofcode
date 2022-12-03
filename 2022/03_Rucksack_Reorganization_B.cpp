#include <bits/stdc++.h>

using namespace std;

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    vector <set<char>> sts(3);
    int res = 0, j = 0;

    while (getline(f, s)) {
        for (int i = 0; i < s.size(); i++) sts[j].insert(s[i]);
        j++;

        if (j == 3) {
            set <char> tmp;
            set_intersection(sts[0].begin(), sts[0].end(), sts[1].begin(), sts[1].end(), inserter(tmp, tmp.begin()));
            sts[0].clear();
            set_intersection(sts[2].begin(), sts[2].end(), tmp.begin(), tmp.end(), inserter(sts[0], sts[0].begin()));

            res += *(sts[0].begin()) - (*(sts[0].begin()) >= 97 ? 'a' : 'A' - 26) + 1;

            for (int i = 0; i < 3; i++) sts[i].clear();
            j = 0;
        }
    }

    cout << res;
}


int main(int argc, char *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	solve();
	
	return 0;
}