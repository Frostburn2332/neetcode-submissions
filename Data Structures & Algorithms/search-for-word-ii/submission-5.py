class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at the leaf node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        # 2. Backtracking DFS with Trie traversal and node pruning
        def backtrack(r: int, c: int, parent: TrieNode):
            char = board[r][c]
            curr_node = parent.children.get(char)
            if not curr_node:
                return

            # Check if a complete word is matched
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Avoid duplicate additions

            # Mark cell as visited
            board[r][c] = "#"

            # Explore all 4 orthogonal neighbors
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    backtrack(nr, nc, curr_node)

            # Restore cell state
            board[r][c] = char

            # Optimization: prune leaf nodes to prevent re-traversing exhausted paths
            if not curr_node.children:
                del parent.children[char]

        # 3. Start DFS from every cell matching a root Trie prefix
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    backtrack(r, c, root)

        return res