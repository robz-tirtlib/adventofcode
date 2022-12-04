#include <bits/stdc++.h>

using namespace std;

int getNum(string &s, int st, int nd) {
    string ans;
    for (int i = st; i < nd; i++) ans += s[i];
    return stoi(ans);
}

void solve() {
    ifstream f;
    f.open("input.txt");
    string s;
    int resA = 0, resB = 0;

    while (getline(f, s)) {
        int prev = 0;
        vector <int> nums(4);
        for (int j = 0; j < 4; j++) {
            int i = prev;

            while (s[i] >= '0' && s[i] <= '9') i++;
            nums[j] = getNum(s, prev, i);
            prev = ++i;
        }
        if (nums[0] <= nums[2] && nums[1] >= nums[3] || nums[0] >= nums[2] && nums[1] <= nums[3]) resA++;
        if (nums[1] >= nums[2] && nums[1] <= nums[3] || nums[3] >= nums[0] && nums[3] <= nums[1]) resB++;
    }

    cout << resA << endl;
    cout << resB << endl;
}


int main(int argc, char *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	solve();
	
	return 0;
}