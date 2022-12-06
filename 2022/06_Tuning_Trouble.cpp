#include <bits/stdc++.h>

using namespace std;

const int sizeA = 4, sizeB = 14; // Sizes of consequences of distinct characters for each part of task

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    getline(f, s);
    set <char> curr;
    int l = 0, r = 0;

    while (r < s.size()) {
        while (curr.size() < sizeB && curr.count(s[r]) == 0) {
            curr.insert(s[r]);
            r++;
        }

        if (curr.size() == sizeB) {
            cout << r;
            break;
        }

        while (s[l] != s[r]) {
            curr.erase(s[l]);
            l++;
        }
        curr.erase(s[l]);
        l++;
    }
}


int main(int argc, char *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	solve();
	
	return 0;
}