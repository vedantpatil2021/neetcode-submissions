class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        lower = clean_text.lower()
        if lower == lower[::-1]:
            return True
        else:
            return False