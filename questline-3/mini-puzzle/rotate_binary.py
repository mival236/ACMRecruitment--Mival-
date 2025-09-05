# rotate_binary.py

def rotate_and_convert(binary_str: str, k: int) -> int:
   
    n = len(binary_str)
    if n == 0:
        return 0
    
    # Normalize k (handle large rotations)
    k = k % n
    
    # Perform circular right rotation
    rotated = binary_str[-k:] + binary_str[:-k]
    
    # Convert to decimal
    return int(rotated, 2)


# Example usage
if __name__ == "__main__":
    examples = [
        ("1011", 2),  # 1011 → rotated 2 → 1110 → 14
        ("1011", 1),  # 1011 → rotated 1 → 1101 → 13
        ("1011", 4),  # Full rotation → 1011 → 11
        ("1100", 3),  # 1100 → rotated 3 → 0110 → 6
        ("1000", 0),  # No rotation → 1000 → 8
    ]
    
    for binary_str, k in examples:
        result = rotate_and_convert(binary_str, k)
        print(f"Binary: {binary_str}, Rotate: {k} → Decimal: {result}")
