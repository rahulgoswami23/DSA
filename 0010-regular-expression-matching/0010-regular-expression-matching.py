class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dp(i, j):
            # Pattern is completely used
            if j == len(p):
                return i == len(s)

            # Already calculated
            if (i, j) in memo:
                return memo[(i, j)]

            # Check whether current characters match
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # If next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: use zero occurrences
                # Option 2: use one occurrence and stay on same pattern
                result = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )

            else:
                # Normal character or '.'
                result = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)