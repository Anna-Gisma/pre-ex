def str_search(S1, S2):
    s1 = list(S1)
    s2 = list(S2)
    N = len(s1)
    M = len(s2)
    f = 0
    if len(s2) == 0:
        return True
    else:
        for i in range(N - M):   
            f = True
            for k in range(M):
                if s1[i+k] != s2[k]:
                    f = False
            if f:
                break
        return f
