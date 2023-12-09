Sclass Solution {
    public double myPow(double x, long n) {
        if(n < 0) {
			n = -n;
			x = 1/x;
		}
        if(n == 1) return x;
        if(n == 0) return 1;
        if(x == 0) return 0;
		
        double res = 0;
		if(n % 2 == 0){
            res = myPow(x,n/2);
            return res * res;
        }
		else {
            res = myPow(x,(n-1)/2);
            return  res * res * x;
        }
    }
}
