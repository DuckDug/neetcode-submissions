class Solution {
    public boolean isValid(String s) {
        Stack<Character> sta = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(')', '(');
        map.put(']', '[');

        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                if (!sta.isEmpty() && sta.peek() == map.get(c)) {
                    sta.pop();
                }
                else {
                    return false;
                }
            }
            else {
                sta.push(c);
            }
        }

        return sta.isEmpty();
    }
}
