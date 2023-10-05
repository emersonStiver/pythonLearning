def permutations(p, up):
    if len(up) ==0:
        print(p)
        return
    ch = up[0]
    i = 0
    while i <= len(p):
        f = p[0:i]
        s = p[i:len(p)]
        permutations(f+ch+s, up[1:])
        i+=1
#permutations('', 'abc')


def permutationsArray(p, up):
    if len(up) ==0:
        return [p]
    ch = up[0]
    i = 0
    #local to this call
    messanger = []
    while i <= len(p):
        f = p[0:i]
        s = p[i:len(p)]
        messanger.extend(permutationsArray(f+ch+s, up[1:]))
        i+=1
    return messanger



arr = permutationsArray('', 'abc')
print(arr)