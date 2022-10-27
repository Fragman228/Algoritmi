def sumBase(self, y: int, k: int) -> int:
    a = 0
    while y:
        y, x = divmod(y, k)
        a += x
    return a