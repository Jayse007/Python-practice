print(2*2)
print(18+12)
print(18*4)
print(18/4)
print(19//4)


def rounding(divisor, dividened):
    threshold = dividened / divisor
    compare = dividened // divisor

    value = threshold - compare
    print(value)
    if value >= 0.5:
        return int((dividened // divisor) + 1)
    
    else:
        return int(dividened // divisor)
    
print(rounding(4, 19.9))