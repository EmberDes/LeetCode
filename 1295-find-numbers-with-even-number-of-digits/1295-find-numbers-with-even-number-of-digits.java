class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for(int number : nums){
            if (number<0){
                number = number * (-1);
            }
            if ((int)(Math.log10(number)+1)%2==0){
                count++;
            }
        }
        return count;
    }
}
