def find_pairs(lst, K):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == K:
                result.append((lst[i], lst[j]))  # inside append() method pass tuple paranthesis '()' inside this tuple store sum pair(5, 7) ,(3, 9)
    print(result)
    return result
lst = [1, 5, 3, 7, 9]
K = 12
print(find_pairs(lst, K))