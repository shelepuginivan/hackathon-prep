def fizz_buzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"

    if n % 3 == 0:
        return "fizz"

    if n % 5 == 0:
        return "bazz"

    return ""


for i in range(40):
    print(i, fizz_buzz(i))

