class Solution {
    public String convertToTitle(int n) {
        int i = -1 , val = 0 ;
        char ch;
        StringBuilder cc = new StringBuilder();
        String c = new String();
        while(n != 0){
            n--;
            i = n % 26;
            val = i + 'A';
            ch = (char) val;
            cc.append(ch);
            n = n / 26;
        }
        c = cc.reverse().toString();
        return c;
    }
}
