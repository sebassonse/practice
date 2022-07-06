def get_dataset():
    [n, k] = list(map(int, input().split()))
    dataset = list(map(int, input().split()))
    return k, n, dataset


def zero_mask(k):
    return [0 for i in range(k)]


def func(k, n, dataset):
    mask = zero_mask(k)
    currseq = []
    minsum = float('inf')
    i = 0
    f = 0
    
    while 1:
        if max(mask) != 0 or dataset[i] <= k:
            currseq.append(dataset[i])

        if dataset[i] <= k:
            mask[dataset[i]-1] += 1
            if sum(mask) == 1:
                f = i

        if min(mask) == 1:
            suma = sum(currseq)
            minsum = min(minsum, suma)
            mask = zero_mask(k)
            i = f
            currseq = []

        if i == n-1:
            break
        i += 1

    return minsum


# body
k, n, dataset = get_dataset()
ans = func(k, n, dataset)
print(ans)
