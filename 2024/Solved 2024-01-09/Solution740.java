class Solution {
    public int deleteAndEarn(int[] nums) {
    	Arrays.sort(nums);
    	return deleteAndEarn(nums, 0, new int[nums.length]);
    }
    
    public int deleteAndEarn(int[] nums, int i, int[] memo) {
    	if(i == nums.length) return 0;
    	
    	//Delete i and earn its yield. If we choose to delete and earn element i
    	//we add all other elements of the same value.

        if(memo[i] == 0){
        int earn = nums[i];
    	int skipTo = i + 1;
    	for(int j = skipTo; j < nums.length; j++) {
    		if(nums[j] == nums[i]) earn += nums[j];
    		else break;
            skipTo += 1;
    	}
    	
    	//Skip elements that is equal to nums[i] + 1.
    	for(int j = skipTo; j < nums.length; j++) {
            if(nums[j] != nums[i] + 1) break;
            skipTo += 1;
    	}
    	
    	earn += deleteAndEarn(nums, skipTo, memo);
    	
    	int skipped = deleteAndEarn(nums, i + 1, memo);

        memo[i] = Math.max(earn, skipped);
        }    	
    	return memo[i];
    }
}
