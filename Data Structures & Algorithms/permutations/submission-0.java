class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), result, new boolean[nums.length]);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> perm, List<List<Integer>> result, boolean[] used) {
        if (perm.size() == nums.length) {
            result.add(new ArrayList<>(perm));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            //choose here
            perm.add(nums[i]);
            //backtrack
            backtrack(nums, perm, result, used);
            //remove chosen
            perm.remove(perm.size() - 1);
            used[i] = false;
        }
    }
}
