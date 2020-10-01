#include <bits/stdc++.h>

#define int long long
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> v(n), v1(n), v2(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    int cnt = 0;
    for (int i = 0; i < n;) {
        if (v[i] == 1) {
            int j = i + 1;
            while (j < n and v[j] != 1) {
                j++;
            }
            if (j == n or (j - i) % 2 == 0) {
                cnt++;
                v[i] = -1;
                i = j;
            } else {
                i = j + 1;
            }
        } else {
            i++;
        }
    }
    cout << n - cnt << '\n';
    for (auto &i : v) {
        if (i != -1)
            cout << i << ' ';
    }
    cout << '\n';
}

signed main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
