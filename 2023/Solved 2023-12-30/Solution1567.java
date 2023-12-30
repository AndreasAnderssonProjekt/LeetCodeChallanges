class Solution1567 {
    public int getMaxLen(int[] nums) {
        int res = 0;
        int neg = 0, pos = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                pos = 0;
                neg = 0;
            }
            else if(nums[i] > 0){
                pos += 1;
                neg = (neg == 0) ? 0 : neg + 1;
            }
            else{
                int temp = pos;
                pos = (neg == 0) ? 0 : neg + 1;
                neg = temp + 1;
            }
            res = Math.max(res, pos);
        }
        return res;
    }
}
