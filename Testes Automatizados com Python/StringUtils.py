class StringUtils:
    def reverse_string(self, s):
        return s[::-1] # Corrigido


    def is_palindrome(self, s):
        return s == s[::-1]  # OK
