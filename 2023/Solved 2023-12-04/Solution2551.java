class Solution2551 {
  //LeetCode Ex.2551 https://leetcode.com/problems/put-marbles-in-bags/description/?source=submission-noac
    public long putMarbles(int[] weights, int k) {
        
        PriorityQueue<Bar> min_pq = new PriorityQueue<>(weights.length, new minBarComparator());
        PriorityQueue<Bar> max_pq = new PriorityQueue<>(weights.length, new maxBarComparator());
        for(int i = 1; i < weights.length; i++){
        	int diff = weights[i] + weights[i-1];
        	min_pq.add(new Bar(diff,i));
        	max_pq.add(new Bar(diff,i));
        }
        
        long min_res = weights[0] + weights[weights.length-1];
        long max_res = weights[0] + weights[weights.length-1];
        
        for(int i = 0; i < k-1 ; i++) {
        	int min_i = min_pq.poll().getIndex();
            int max_i = max_pq.poll().getIndex();
        	min_res += (long) weights[min_i-1] + weights[min_i];
        	max_res += (long) weights[max_i-1] + weights[max_i];
        }
        return  max_res - min_res;
    }

    private static class Bar{
		private int diff;
		private int index;
		
		public Bar(int diff, int index) {
			this.diff = diff;
			this.index = index;
		}
		
		public int getIndex() {
			return this.index;
		}
		
		public int getDiff() {
			return this.diff;
		}
		
	}
	
	private static class minBarComparator implements Comparator<Bar>{

		@Override
		public int compare(Bar o1, Bar o2) {
			if(o1.diff > o2.diff) return 1;
			if(o1.diff < o2.diff) return -1;
			return 0;
		}
		
	}
	
	private static class maxBarComparator implements Comparator<Bar>{

		@Override
		public int compare(Bar o1, Bar o2) {
			if(o1.diff < o2.diff) return 1;
			if(o1.diff > o2.diff) return -1;
			return 0;
		}
		
	}
}
