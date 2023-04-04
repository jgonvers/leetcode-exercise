class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def possibilities(char):
            if char in string.digits:
                return [char]
            return [char.lower(), char.upper()]
        if len(s) == 1: return possibilities(s)
        cur_pos = possibilities(s[0])
        pos = self.letterCasePermutation(s[1:])
        sol = []
        for x in pos:
            for y in cur_pos:
                sol.append(y+x)
        return sol
    