from functools import cmp_to_key
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(a,b):
            i = order.index(a)
            j = order.index(b)
            if i < j: return -1
            if i == j: return 0
            return 1
        
        def compare_words(w1, w2):
            if w1 == w2: return 0
            l1 = len(w1)
            l2 = len(w2)
            if l1 <= l2:  comp = -1
            else: comp = 1
            for i in range(min(l1,l2)):
                if w1[i] != w2[i]:
                    comp = compare(w1[i], w2[i])
                    break
            return comp
        
        sorted_list = sorted(words, key=cmp_to_key(compare_words))
        return sorted_list == words
                