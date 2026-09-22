class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            while (l < r && !isAlpha(s.charAt(l))) {
                l++;
            }
            while (r > l && !isAlpha(s.charAt(r))) {
                r--;
            }
            char lChar = Character.toLowerCase(s.charAt(l));
            char rChar = Character.toLowerCase(s.charAt(r));

            if (lChar != rChar) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    private boolean isAlpha(char c) {
        return 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' || '0' <= c && c <= '9';
    }
}
