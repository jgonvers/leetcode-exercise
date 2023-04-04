#from itertools import combinations
#class Solution:
#    def combine(self, n: int, k: int) -> List[List[int]]:
#        return list(combinations(list(range(1,n+1)), k))

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1: return [[x] for x in range(1,n+1)]
        if k == n: return [list(range(1,n+1))]
        sol = []
        for x in range(n,0,-1):
            less = self.combine(x-1, k-1)
            for e in less:
                e.append(x)
            sol.extend(less)
        return sol
