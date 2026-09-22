class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> mySet = new HashSet<>();

        for (int num : nums) {
            mySet.add(num);
        }

        int maxLen = 0;

        for (int num : nums) {
            int length = 1;

            if (!mySet.contains(num - 1)) {
                while (mySet.contains(num + length)) {
                    length++;
                }
                maxLen = Math.max(maxLen, length);
            }

        }

        return maxLen;
    }
}
