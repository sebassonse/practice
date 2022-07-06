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
    f = 0

    for el in dataset:
        if len(currseq) != 0 or el <= k:
            currseq.append(el)
            if el <= k:
                mask[el - 1] += 1
            if el == currseq[0] and len(currseq) > 1:
                currseq.pop(0)
                mask[el - 1] -= 1
                while 1:
                    if len(currseq) != 1:
                        if currseq[0] > k:
                            currseq.pop(0)
                        elif currseq[0] <= k and mask[currseq[0] - 1] > 1:
                            mask[currseq[0] - 1] -= 1
                            currseq.pop(0)
                        else:
                            break
                    else:
                        break

        if min(mask) == 1:
            minsum = min(sum(currseq), minsum)

    return minsum


# body
k, n, dataset = get_dataset()
ans = func(k, n, dataset)
print(ans)

" ЭТА ПРОГРАММА НЕ РАБОТАЕТ, В НЕКОТОРЫХ СЛУЧАЯХ ВЫДАЕТ ОШИБКУ"
