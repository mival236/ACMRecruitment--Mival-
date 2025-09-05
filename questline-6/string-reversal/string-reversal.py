
# Iterative method
def reverse_iterative(s):
    rev = ''
    for ch in s:
        rev = ch + rev  # prepend each character
    return rev

# Recursive method
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

if __name__ == "__main__":
    original = "hello"
    print("Original:", original)
    print("Iterative Reverse:", reverse_iterative(original))
    print("Recursive Reverse:", reverse_recursive(original))
