def longest_palindromic_substring(s: str) -> str:
    if not s or len(s) == 1:
        return s
    
    start, max_len = 0, 0

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start, max_len = left, right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindrome (center at i)
        expand_around_center(i, i)
        # Even-length palindrome (center between i and i+1)
        expand_around_center(i, i + 1)

    return s[start:start + max_len]
print(longest_palindromic_substring("babad"))  # "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # "bb"
print(longest_palindromic_substring("a"))      # "a"
print(longest_palindromic_substring("ac"))     # "a" or "c"
