def find_secret(x, y):
    # Using XOR property: if N ^ x = y, then N = y ^ x
    return y ^ x

if __name__ == "__main__":
    x = 23
    y = 45
    secret = find_secret(x, y)
    print(f"Secret number N = {secret}")

    # Verification step
    print(f"Check: {secret} XOR {x} = {secret ^ x}")
