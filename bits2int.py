def get_bit():
    x = input("Enter a binary digit (0 or 1): ")
    
    if x == '0':
        return 0
    elif x == '1':
        return 1
    else:
        return -1

def bits2int():
    number = 0
    currBit = get_bit()
    
    while currBit != -1:
        number = number << 1
        number = currBit + number
        currBit = get_bit()
    
    return number

# Example usage:
result = bits2int()

print("Result:", result)
