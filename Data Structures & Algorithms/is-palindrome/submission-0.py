class Solution:
    def isPalindrome(self, s: str) -> bool:
        nl = list(s)
        sub_out = []
        for i in range(len(nl)):
            if nl[i].isalnum():
                sub_out.append(nl[i].lower())

        nl_rev = sub_out[::-1]
        if sub_out == nl_rev:
            return True

        return False