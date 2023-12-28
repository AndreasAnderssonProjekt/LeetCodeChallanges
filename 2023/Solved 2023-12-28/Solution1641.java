class Solution1641 {
    public int countVowelStrings(int n) {
        int vowels = 5;
        int[][] opt = new int[n+1][vowels + 1];
        //initial conditions.
        for(int i = 0; i < opt[0].length; i++) opt[1][i] = i;

        for(int i = 2; i < opt.length; i++){
            for(int j = 1; j < opt[0].length; j++){
                for(int k = 1; k <= j; k++){
                    opt[i][j] += opt[i-1][k];
                }
            }
        }
        return opt[opt.length - 1][opt[0].length - 1];
    }
}
