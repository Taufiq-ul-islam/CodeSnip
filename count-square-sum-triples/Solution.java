class Solution {
    public int countTriples(int n) {
        int sq = 0 , c = 0;
        double rt = 0.0 , dec = 0.0;
        for (int i = 2 ; i < n - 1 ; i++){
            for (int j = i + 1 ; j < n ; j++){
                sq = i * i + j * j;
                rt = Math.sqrt(sq);
                if (rt > n) continue;
                dec = rt - Math.floor(rt); // frac(rt)
                if (dec == 0.0) c += 2; // two tuples : (i , j , rt) , (j , i , rt); checking for rt being a perfect square
            }
        }
        return c;
    }
}
