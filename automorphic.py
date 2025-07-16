def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

n = int(input())
if is_automorphic(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
