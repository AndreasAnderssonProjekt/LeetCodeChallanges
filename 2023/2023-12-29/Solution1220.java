class Solution1220 {
   public int countVowelPermutation(int n) {
        // a = 0, e = 1, i = 2, o =3, u = 4.
        int vowels = 5;
        int mod = 1000000007;
        long[][] dp = new long[n][vowels];
        Map<Integer, int[]> map = new HashMap<>(){{
            put(0, new int[] {1, 2, 4});
            put(1, new int[] {0, 2});
            put(2, new int[] {1, 3});
            put(3, new int[] {2});
            put(4, new int[] {2, 3});
        }};

        for(int i = 0; i < vowels; i++){
            dp[0][i] = 1;
        }

        for(int i = 1; i < n; i++){
        	for(int j = 0; j < vowels; j++) {
        		for(int vowel : map.get(j)) {
        			dp[i][j] += dp[i-1][vowel];
        		}
                dp[i][j] = dp[i][j] % mod;
        	}
        }
        
        long res = 0;
        for(int i = 0; i < vowels; i++) {
        	res += dp[n-1][i];
        }
        return (int) (res % mod);

    }
}
