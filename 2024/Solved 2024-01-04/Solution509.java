class Solution509 {
    public int fib(int n) {
        int[] opt = new int[n + 1];
        opt[0] = 0;
        if(n == 0) return opt[0];
        opt[1] = 1;

        for(int i = 2; i < n + 1; i++){
            opt[i] = opt[i - 1] + opt[i - 2];
        }

        return opt[n];
    }
}
