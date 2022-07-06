
"""def comb(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0


def factorial(x, start=1):
    res = 1
    for i in range(start+1, x+1):
        res *= i
    return res


def perest(v):
    n = sum(v)
    m = max(v)
    inv = copy.deepcopy(v)
    inv.remove(max(v))
    underEq = 1
    for el in inv:
        underEq *= factorial(el)
    res = factorial(n, n-m) / underEq
    return res


def get_num_of_perest_comb(v, k):
    res = perest(v)
    return res


faces = list(map(int, input().split()))
k = int(input())

uniqEl = list(set(faces))
numOfAllVar = len(uniqEl)**k

ans = 0

maxPow = int((k + k % 2)/2 + 1)
for v1 in range(maxPow):
    for v2 in range(maxPow):
        for v3 in range(maxPow):
            for v4 in range(maxPow):
                for v5 in range(maxPow):
                    for v6 in range(maxPow):
                        for n in range(1, k + 1):
                            maxLocalPow = int((n + n % 2)/2 + 1)
                            if (v1+v2+v3+v4+v5+v6) == n \
                                    and v1 <= maxLocalPow \
                                    and v2 <= maxLocalPow \
                                    and v3 <= maxLocalPow \
                                    and v4 <= maxLocalPow \
                                    and v5 <= maxLocalPow \
                                    and v6 <= maxLocalPow:
                                sumEl = 0
                                multProbEl = 1
                                v = [v1, v2, v3, v4, v5, v6]
                                numOfLocVar = get_num_of_perest_comb(v, k)
                                for i in range(6):
                                    sumEl += faces[i] * v[i]
                                ans += sumEl * (1/6)**(k-2) * numOfLocVar / numOfAllVar
                                print(v, sumEl, numOfLocVar, numOfAllVar)

print(ans)
"""