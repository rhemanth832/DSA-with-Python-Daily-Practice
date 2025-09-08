def totalFruit_brute(fruits):
    n = len(fruits)
    maxi = 0
    for i in range(n):
        basket = set()
        for j in range(i, n):
            basket.add(fruits[j])
            if len(basket) > 2:
                break
            maxi = max(maxi, j - i + 1)
    return maxi

print(totalFruit_brute([1,2,1,2,3]))  # Output: 4
