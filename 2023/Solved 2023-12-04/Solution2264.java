class Solution2264 {
  //Solution to LeetCode Ex.2264 https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2023-12-04
    public String largestGoodInteger(String num) {
        int start = -1;
        int end = -1;
        char prev = ' ';
        String largestGoodInt = "";
        for(int i = 0; i < num.length(); i++){
            if(start == -1) start = i;
            if(num.charAt(i) == prev || prev == ' ') end = i;
            else{
                start = i;
                end = -1;
            }
            if(end - start == 2 && end != -1){
                String goodInt = num.substring(start,end+1);
                if(largestGoodInt != ""){
                    if(Integer.parseInt(largestGoodInt) < Integer.parseInt(goodInt)) largestGoodInt = goodInt; 
                }
                else largestGoodInt = goodInt;
            }
            prev = num.charAt(i);
        }
        return largestGoodInt;
    }
    
}
