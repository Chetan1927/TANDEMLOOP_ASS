def odd_series_2(a: int):
    n = a if a % 2 != 0 else a - 1
    return [i for i in range(1, 2*n, 2)]

print(odd_series_2(4)) 
print(odd_series_2(5))
