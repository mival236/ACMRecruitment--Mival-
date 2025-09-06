
def to_twos_complement(n, bits=8):
    """Return the two's complement representation of n in 'bits' bits."""
    if n >= 0:
        return format(n, f'0{bits}b')
    else:
        return format((1 << bits) + n, f'0{bits}b')

if __name__ == "__main__":
    num = -42
    bits = 8
    representation = to_twos_complement(num, bits)

    print(f"Number: {num}")
    print(f"{bits}-bit 2's complement representation: {representation}")

