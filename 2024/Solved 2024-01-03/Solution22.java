class Solution22 {
    public List<String> generateParenthesis(int n) {
        List<String> l = new LinkedList<>();
       backtrack(l, new StringBuilder(), 0, 0, n);
       return l;
    }

    public void backtrack(List<String> l, StringBuilder p, int left, int right, int n){
        if(p.length() == 2 * n){
            l.add(p.toString());
        }

        if(left < n){
            StringBuilder p1 = new StringBuilder(p.toString());
             p1.append("(");
             backtrack(l, p1, left+1, right, n);
        }
        
        if(right < n && left > right){
            StringBuilder p2 = new StringBuilder(p.toString());
            p2.append(")");
            backtrack(l, p2, left, right + 1, n);
        }  
    }
}
