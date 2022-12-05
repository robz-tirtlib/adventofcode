#include <bits/stdc++.h>

using namespace std;

void parseStacks(vector <vector <char>> &a, string &s) {
    for (int i = 1; i <= 33; i += 4) {
        if (s[i] >= 'A' && s[i] <= 'Z')
            a[(i - 1) / 4].insert(a[(i - 1) / 4].begin(), s[i]);
    }
}

int power(int x, int p) {
    int num = 1;
    for (int i = 0; i < p; i++) num *= x;
    return num;
}

void movesA(vector <vector <char>> &a, vector <int> &m) {
    int from = m[1], to = m[2];
    for (int i = 0; i < m[0]; i++) {
        int tmp = a[from][a[from].size() - 1];
        a[to].push_back(tmp);
        a[from].pop_back();
    }
}

void movesB(vector <vector <char>> &a, vector <int> &m) {
    int amount = m[0], from = m[1], to = m[2];
    for (int i = amount; i > 0; i--) {
        a[to].push_back(a[from][a[from].size() - i]);
    }

    for (int i = 0; i < amount; i++) a[from].pop_back();
}

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    vector <vector <char>> a(9);
    bool ok = false;

    while (getline(f, s)) {
        if (s.size() == 0 || (s[1] >= '0' && s[1] <= '9')) {
            ok = true;
            continue;
        }

        if (!ok) {
            parseStacks(a, s);
            continue;
        }

        vector <int> m(3);

        int r = s.size() - 1;
        for (int j = 2; j >= 0; j--) {
            int i = r, tmp = 0;

            while (s[i] >= '0' && s[i] <= '9') {
                tmp += (s[i] - 48) * power(10, r - i);
                i--;
            }
            m[j] = tmp;

            while ((s[i] < '0' || s[i] > '9') && i > 0) i--;
            r = i;
        }
        m[2]--; m[1]--;

        //movesA(a, m); <- for A part
        movesB(a, m); // <- for B part
    }

    for (auto &stack : a) {
        for (auto &num : stack) cout << num << " ";
        cout << stack.size() << endl;
    }
}


int main(int argc, char *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	solve();
	
	return 0;
}