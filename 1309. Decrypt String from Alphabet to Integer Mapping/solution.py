class Solution:
    def freqAlphabets(self, s: str) -> str:
        start_char = 96 #start at 1 so start_char+1 = "a"
        for i in range(10,27):
            code = f"{i}#"
            s = s.replace(code, chr(start_char+i))
        for i in range(1,10):
            s = s.replace(str(i), chr(start_char+i))
        return s
    