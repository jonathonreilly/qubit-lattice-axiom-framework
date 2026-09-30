import itertools, collections
L=3
dirs=[(mu,d) for mu in range(4) for d in (+1,-1)]
def shift(s,mu,d):
    t=list(s); t[mu]=(t[mu]+d)%L; return tuple(t)
cnt=collections.Counter()
start=(0,0,0,0)
for seq in itertools.product(dirs,repeat=4):
    pos=start; word=[]
    for mu,d in seq:
        if d==+1:
            link=(pos,mu); word.append((link,+1)); pos=shift(pos,mu,1)
        else:
            newpos=shift(pos,mu,-1); link=(newpos,mu); word.append((link,-1)); pos=newpos
    if pos!=start: continue
    # reduce
    st=[]
    for w in word:
        if st and st[-1][0]==w[0] and st[-1][1]==-w[1]: st.pop()
        else: st.append(w)
    cnt[len(st)]+=1
    if len(st)>0 and len(st)!=4:
        print("odd reduced word", st)
print(cnt)
