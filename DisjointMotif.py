f = open('rosalind_itwv.txt')

s = f.readline().strip()
ps = map(lambda x: x.strip(),f.readlines())
ps_len = 0
ps_list = []

for i in ps:
    ps_len += 1
    ps_list.append(i)

def interweave(seq,pos,m1,m2,p1,p2):
    if(p1 >= len(m1)):
        if(p2 >= len(m2)):
            return True
        elif(m2[p2] != seq[pos]):
            return False
        else:
            return interweave(seq,pos+1,m1,m2,p1,p2+1)
    if(p2 >= len(m2)):
        if(p1 >= len(m1)):
            return True
        elif(m1[p1] != seq[pos]):
            return False
        else:
            return interweave(seq,pos+1,m1,m2,p1+1,p2)
    if(pos >= len(seq)):
        return False
    if(m1[p1] == seq[pos]):
        if(interweave(seq,pos+1,m1,m2,p1+1,p2)):
            return True
    if(m2[p2] == seq[pos]):
        if(interweave(seq,pos+1,m1,m2,p1,p2+1)):
            return True
    return False

matches = [0] * (ps_len * ps_len)

for si1 in range(ps_len):
    for si2 in range(si1,ps_len):
        match = False
        for sp in range(len(s)):
            if(interweave(s,sp,ps_list[si1],ps_list[si2],0,0)):
                match = True
                break
        if(match):
            matches[si1 * ps_len + si2] = 1
            matches[si2 * ps_len + si1] = 1

for si1 in range(ps_len):
    print(" ".join(map(str,matches[(si1*ps_len):((si1+1)*ps_len)])))
