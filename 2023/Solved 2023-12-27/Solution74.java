class Solution74 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int low = 0;
        int high = matrix.length * matrix[0].length - 1;

        while(low <= high){
            int mid = low + (high - low) / 2;
            int col = mid % matrix[0].length;
            int row = (mid) / matrix[0].length ;
            int number = matrix[row][col];
            if(number == target) return true;

            else if(number < target) low = mid + 1;
            else high = mid - 1;
        }
        return false;
    } 
}
