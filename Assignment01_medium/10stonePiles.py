def stone_piles(n):
    piles = []
    cs = 1 if n % 2 != 0 else 2

    for i in range(n):
        piles.append(cs)
        cs += 2

    return piles


if __name__ == '__main__':
    n = int(input("Enter the number of stones in the first pile: "))
    result = stone_piles(n)
    print(f"The number of stones in each pile: {result}")
