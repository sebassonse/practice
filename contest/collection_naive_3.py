def get_dataset():
    [n, k] = list(map(int, input().split()))
    dataset = list(map(int, input().split()))
    return k, n, dataset


def zero_mask(k):
    return [0 for i in range(k)]


def zero_where(k):
    zerowhere = dict()
    for i in range(1, k+1):
        zerowhere[i] = []
    return zerowhere


def func(k, n, dataset):
    mask = zero_mask(k)
    where = zero_where(k)
    currseq = []
    minsum = float('inf')
    i = 0
    for el in dataset:
        print(currseq)
        if len(currseq) != 0 or el <= k:
            currseq.append(el)
        if el <= k:
            mask[el-1] += 1
            where[el].append(i)
            currel = el
            while 1:
                if len(currseq) > 1 and currel == currseq[0] and mask[currel-1] > 1:
                    where[currel].pop(0)
                    if i != n:
                        currseq = dataset[min(min(where.values())): i+1]
                    else:
                        currseq = dataset[min(min(where.values())): i]
                    mask[currel-1] -= 1
                else:
                    break

        if min(mask) == 1:
            minsum = min(sum(currseq), minsum)
        i += 1
    return minsum


# body
k, n, dataset = get_dataset()
ans = func(k, n, dataset)
print(ans)
