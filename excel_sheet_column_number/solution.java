class Solution {
    public int titleToNumber(String columnTitle) {
        int len = columnTitle.length();
        int no = 0 , temp = 0;
        for(int i = len - 1 ; i >= 0 ; i--){
            temp = (int) (columnTitle.charAt(i) - 'A'); // Difference of ASCII value as column letters will always be capital
            temp++; // Buffer due to 1 of 'A' being subtracted
            no += temp * Math.pow(26 , len - i - 1); // Number system of 26
        }
        return no;
    }
}
