class Solution {
    public int findPeakElement(int[] nums) {
        // Single element array
        if(nums.length == 1) return 0;
        // Bidirectional search
        for(int i = 0 ; i <= nums.length / 2 ; i++){
            if(i == 0){
                if(nums[i] > nums[i + 1]) return i; // LHS
                if(nums[nums.length - 1] > nums[nums.length - 2]) return nums.length - 1; // RHS
            }
            if(nums[i] > nums[i + 1] && nums[i] > nums[i - 1]) return i; // LHS
            if(nums[nums.length - 1 - i] > nums[nums.length - 2 - i] && nums[nums.length - 1 - i] > nums[nums.length - i]) return nums.length - 1 - i; // RHS
        }
        return -1;
    }
}
