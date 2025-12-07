class Solution {
    public int countPartitions(int[] nums, int k) {
        int m = 1000000007 , n = nums.length , l = 0;

        int [] dp = new int [n + 1]; // ways to partition elements before indices
        int [] p = new int [n + 2]; // cumsum of dp
        dp[0] = 1;
        p[1] = 1;

        Deque <Integer> min = new ArrayDeque<>();
        Deque <Integer> max = new ArrayDeque<>();

        for (int i = 0 ; i < n ; i++){
            // Maintain max value indices in desc order of values
            while (!max.isEmpty() && nums[max.peekLast()] <= nums[i])
                max.pollLast();
            max.addLast(i);
            // Maintain min value indices in asc order of values
            while (!min.isEmpty() && nums[min.peekLast()] >= nums[i])
                min.pollLast();
            min.addLast(i);

            // Window validity checking segment
            while(nums[max.peekFirst()] - nums[min.peekFirst()] > k) {
                if(max.peekFirst() == l) max.pollFirst();
                if(min.peekFirst() == l) min.pollFirst();
                l++;
            }

            // Setting dp value as sum of dp values from left to i
            dp[i + 1] = (p[i + 1] - p[l] + m) % m;
            p[i + 2] = (p[i + 1] + dp[i + 1]) % m;
        }
        return dp[n];
    }
}
