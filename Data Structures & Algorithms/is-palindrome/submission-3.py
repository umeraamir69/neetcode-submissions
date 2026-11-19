class Solution:
    def isPalindrome(self, s: str) -> bool:
        pA , pB = 0 , len(s)-1

        while pA < pB:
            if not s[pA].isalnum():
                pA +=1
                continue

            if not s[pB].isalnum():
                pB -=1
                continue

            if s[pA].lower() != s[pB].lower():
                return False

            pA +=1
            pB -=1
        
        return True


        