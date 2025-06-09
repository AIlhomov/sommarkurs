#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

#define ll long long
#define inf 1e9

void fastio()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int main()
{

    fastio();

    int n;
    cin >> n;

    string s;
    cin >> s;
    
    int ans = 0;
    int coffee = 0;

    for (int i=0; i<n; i++){

        if (s[i] == '1'){
            ans++;
            coffee = 2;
        }
        else{
            if (coffee > 0){
                ans++;
                coffee--;
            }
        }
    }
    cout << ans << endl;


    return 0;
}