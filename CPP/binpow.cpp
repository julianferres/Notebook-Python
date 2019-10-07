typedef long long ll;

ll binpow(ll a, ll b, ll m){
	/* a**b mod m, iterativa, O(log b) */
	ll res = 1;
	while(b>0){
		if(b&1) res = res*a % m;
		a = a*a % m;
		b >>= 1;
	}
	return res;
}