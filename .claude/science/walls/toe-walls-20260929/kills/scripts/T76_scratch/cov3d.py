# 3D: rule = forbid ONE neighbour-pattern class (all others incl. 0 allowed); classes = orbits of 6-bit patterns under proper cubic rotations (24)
import itertools, math, sys
D=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def rotations():
    import numpy as np
    mats=[]
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            M=[[0]*3 for _ in range(3)]
            for i in range(3): M[i][perm[i]]=sg[i]
            det=round(np.linalg.det(np.array(M)))
            if det==1: mats.append(M)
    return mats
mats=rotations(); assert len(mats)==24
perms=[]
for M in mats:
    p=[]
    for d in D:
        v=tuple(sum(M[i][j]*d[j] for j in range(3)) for i in range(3))
        p.append(D.index(v))
    perms.append(p)
def canon(bits):
    best=None
    for p in perms:
        b=0
        for i in range(6):
            if (bits>>i)&1: b|=1<<p[i]
        best=b if best is None or b<best else best
    return best
classes=sorted({canon(b) for b in range(64)})
print("number of rotation classes:",len(classes))
cid={c:i for i,c in enumerate(classes)}
cl=[cid[canon(b)] for b in range(64)]
def desc(i):
    c=classes[i]; return bin(c).count("1"), i
def counts(L,forbid):
    grid={}
    def occ(t):
        if all(0<=x<L for x in t): return grid.get(t)
        return 0
    def bits(t,S=None):
        b=0
        for i,d in enumerate(D):
            u=(t[0]+d[0],t[1]+d[1],t[2]+d[2])
            v = (occ(u)==1) if S is None else (u in S)
            if v: b|=1<<i
        return b
    frozen=[]
    N=L**3
    def rec(i):
        if i==N:
            for x in range(L):
              for y in range(L):
                t=(x,y,L-1)
                if grid[t]==0 and cl[bits(t)]==forbid: pass
                elif grid[t]==0: return
            frozen.append(frozenset(t for t,v in grid.items() if v));return
        x,rem=divmod(i,L*L);y,z=divmod(rem,L)
        for v in (0,1):
            grid[(x,y,z)]=v; ok=True
            if z>0 and grid[(x,y,z-1)]==0 and cl[bits((x,y,z-1))]!=forbid: ok=False
            if ok: rec(i+1)
            del grid[(x,y,z)]
    rec(0)
    return frozen,bits
def reach(frozen,bits,forbid):
    memo={}
    def comps(S):
        S=set(S);out=[]
        while S:
            s=S.pop();comp={s};st=[s]
            while st:
                x=st.pop()
                for d in D:
                    y=(x[0]+d[0],x[1]+d[1],x[2]+d[2])
                    if y in S:S.discard(y);comp.add(y);st.append(y)
            out.append(frozenset(comp))
        return out
    def peel(S):
        if not S:return True
        if S in memo:return memo[S]
        r=False
        for v in S:
            if cl[bits(v,S)]!=forbid:
                if all(peel(c) for c in comps(S-{v})): r=True;break
        memo[S]=r;return r
    return sum(1 for s in frozen if all(peel(c) for c in comps(s)))
if __name__=="__main__":
    # find class id of "2 opposite" = bits +x,-x
    two_opp=cl[0b000011]
    print("2opp class id",two_opp)
    for L in range(2,int(sys.argv[1])+1):
        fr,bits=counts(L,two_opp)
        n=reach(fr,bits,two_opp)
        print("3D forbid 2opp only: L",L,"frozen",len(fr),"reach",n,"ln N %.3f"%math.log(n) if n else "",flush=True)
