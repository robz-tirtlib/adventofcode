#include <bits/stdc++.h>

using namespace std;

int getScore(int op, int me) {
    return me + ((me - op + 4) % 3) * 3 + 1;
}

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    int totalA = 0, totalB = 0;

    while (getline(f, s)) {
        int op = (s[0] + 1) % 3, me = (s[2] + 2) % 3;
        totalA += getScore(op, me);
        totalB += getScore(op, (op + me + 2) % 3);
    }

    cout << totalA << endl;
    cout << totalB;
}


int main(int argc, char *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	solve();
	
	return 0;
}