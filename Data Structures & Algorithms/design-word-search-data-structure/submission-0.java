class TrieNode {
    HashMap<Character, TrieNode> children = new HashMap<>();
    Boolean word = false;
}

class WordDictionary {
    TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode cur = root;

        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
        }
        cur.word = true;
    }

    public boolean search(String word) {
        return dfs(word, root, 0);
    }

    private boolean dfs(String word, TrieNode node, int i) {
        if (i == word.length()) {
            return node.word;
        }

        if (node == null) {
            return false;
        }

        char c = word.charAt(i);

        if (c == '.') {
            Set<Character> keys = node.children.keySet();
            for (char ch : keys) {
                TrieNode temp = node.children.get(ch);
                if (dfs(word, temp, i + 1)) {
                    return true;
                }
            }
            return false;
        }
        else if (!node.children.containsKey(c)) {
            return false;
        }
        else {
            return dfs(word, node.children.get(c), i + 1);
        }
    }
}
