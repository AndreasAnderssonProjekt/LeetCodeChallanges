class Solution852 {
    public int peakIndexInMountainArray(int[] arr) {
       int lo = 0;
       int hi = arr.length-1;
       int peak = -1;
       while(lo <= hi){
        int mid = lo + (hi-lo)/2;
        if(arr[mid] > arr[mid+1]) {
            peak = mid;
            hi = mid - 1;
        }
        else if(arr[mid] < arr[mid+1]) lo = mid + 1;
       }
       return peak;
       
        
		
    }

    
}
