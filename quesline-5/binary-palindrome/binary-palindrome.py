
def is_binary_palindrome(n):
    
    b = bin(n)[2:]  # convert to binary string without '0b'
    return b == b[::-1]

if __name__ == "__main__":
    numbers = [9, 10]  # test with the two numbers from manual check
    for num in numbers:
        result = is_binary_palindrome(num)
        print(f"{num} in binary = {bin(num)[2:]}, Palindrome? {result}")
