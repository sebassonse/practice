"""def get_clear_seq(seq):
    newSeq = []
    if len(seq) != 0:
        newSeq += [seq[0]]
        for i in range(1, len(seq)):
            if seq[i] != seq[i-1]:
                newSeq.append(seq[i])
    return newSeq"""


def comb(n, k):
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


def recursion(currSeq, uniqEl, probEl, k):
    if len(currSeq) == 0:
        for el in uniqEl:
            recursion(currSeq + [el], uniqEl, probEl, k)
    elif len(currSeq) < k:
        for el in uniqEl:
            if el != currSeq[-1]:
                recursion(currSeq + [el], uniqEl, probEl, k)

    global ans
    sumEl = 0
    multProbEl = 1
    numOfVar = comb(k, len(currSeq))

    for el in currSeq:
        sumEl += el
        multProbEl *= probEl[el]
    ans += sumEl * multProbEl * numOfVar / k


# input
faces = list(map(int, input().split()))
k = int(input())

uniqEl = list(set(faces))
probEl = dict()
numOfAllVar = len(uniqEl)**k

for el in uniqEl:
    num = 0
    for i in faces:
        if el == i:
            num += 1
    probEl[el] = num/6

ans = 0
num = 0

recursion([], uniqEl, probEl, k)

print(ans)
