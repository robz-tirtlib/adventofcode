#include <bits/stdc++.h>

using namespace std;

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    int res = 0;

    while (getline(f, s)) {
        set <char> l, r, intersection;
        for (int i = 0; i < s.size() / 2; i++) l.insert(s[i]);
        for (int i = s.size() / 2; i < s.size(); i++) r.insert(s[i]);
        set_intersection(l.begin(), l.end(), r.begin(), r.end(), inserter(intersection, intersection.begin()));

        for (auto &letter : intersection) res += letter - (letter >= 97 ? 'a' : 'A' - 26) + 1;
        cout << res << endl;
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