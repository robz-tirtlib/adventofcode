#include <bits/stdc++.h>

using namespace std;

int power(int x, int p) {
    int num = 1;
    for (int i = 0; i < p; i++) num *= x;
    return num;
}

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    long long res = 0;

    while (getline(f, s)) {
        long long r = 0, i = s.size() - 1, tmp = 0;

        while ((s[i] < '0' || s[i] > '9') && i >= 0) i--;
        r = i;

        while (i >= 0 && s[i] >= '0' && s[i] <= '9') {
            tmp += (s[i] - 48) * power(10, r - i);
            i--;
        }

        if (tmp <= 100000) res += tmp;
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