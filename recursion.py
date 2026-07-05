def fact(n):
    print("Calling fact(", n, ")")

    if n == 1:
        print("Returning 1")
        return 1

    ans = n * fact(n - 1)
    print("Returning", ans, "for", n)
    return ans

print(fact(5))