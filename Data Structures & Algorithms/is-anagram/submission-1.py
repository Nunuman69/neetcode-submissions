class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hashset = {}
            for i in s:
                hashset[i] = hashset.get(i, 0) + 1

            for j in t:
                if j in hashset:
                    hashset[j] -= 1
                    if hashset[j] < 0:
                        return False
                else:
                    return False
                    
            return True
        return False