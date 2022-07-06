while True:
    def dict_from_str(string):
        d = dict()
        for char in str(string):
            if char not in d.keys():
                d[char] = 0
            d[char] += 1
        return d


    def set_val_null(currdict):
        for k in currdict.keys():
            currdict[k] = 0
        return currdict

    numchars, lentext = map(int, input().split())
    chars = dict_from_str(input())
    text = input()

    ans = 0
    mask = set_val_null(chars)
    curr = mask

    for i in range(lentext):
        print(curr[text[i]] + 1, curr[text[i]])
        if text[i] not in chars.keys() or (curr[text[i]] + 1 > curr[text[i]]):
            curr = mask
        else:
            curr[text[i - numchars]] -= 1
            curr[text[i]] += 1
        if curr == chars:
            ans += 1
        print(curr, chars, '', sep='\n')
