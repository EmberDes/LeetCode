class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxAverage=Double.MIN_VALUE;
        //sum of First K Size Window
        double sum = 0 ;
        for(int i = 0; i<k;i++){
            sum +=nums[i];
        }
        maxAverage =  sum/k;
        //remaining window Average
        
        for ( int i = k ; i < nums.length ; i++){
            sum = sum + nums[i]-nums[i-k];
            maxAverage = Math.max(maxAverage,sum/k);
            
        }
        return maxAverage;
        
    }
}