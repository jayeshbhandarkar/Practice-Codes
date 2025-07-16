def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in map_st:
            if map_st[char_s] != char_t:
                return False
        else:
            map_st[char_s] = char_t

        if char_t in map_ts:
            if map_ts[char_t] != char_s:
                return False
        else:
            map_ts[char_t] = char_s

    return True
