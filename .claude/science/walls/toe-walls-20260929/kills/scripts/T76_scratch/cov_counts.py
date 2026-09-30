# exact frozen and reachable counts, LxL sealed box, outside unrecorded, for a covariant rule R (set of class ids 0..5)
import sys, math
from covariant2d import cls, NAMES, DIRS
def counts(L,R,wall=0):
    Rset=set(R); grid={}
    def occ(t):
        r,c=t
        if 0<=r<L and 0<=c<L: return grid.get(t)
        return wall
    def pat(t):
        r,c=t
        return [1 if occ((r+dr,c+dc))==1 else 0 for dr,dc in DIRS]
    frozen=[]
    def rec(i):
        if i==L*L:
            for c in range(L):
                t=(L-1,c)
                if grid[t]==0 and cls(pat(t)) in Rset: return
            frozen.append(frozenset(t for t,v in grid.items() if v)); return
        r,c=divmod(i,L)
        for v in (0,1):
            grid[(r,c)]=v; ok=True
            if r>0 and grid[(r-1,c)]==0 and cls(pat((r-1,c))) in Rset: ok=False
            if ok: rec(i+1)
            del grid[(r,c)]
    # NB: pat() of (r-1,c) uses (r-1,c+1) assigned, (r,c) assigned, ok
    rec(0)
    memo={}
    def pc(t,S):
        r,c=t
        return [1 if ((r+dr,c+dc) in S or (wall==1 and not(0<=r+dr<L and 0<=c+dc<L))) else 0 for dr,dc in DIRS]
    def comps(S):
        S=set(S);out=[]
        while S:
            s=S.pop();comp={s};st=[s]
            while st:
                x=st.pop()
                for dr,dc in DIRS:
                    y=(x[0]+dr,x[1]+dc)
                    if y in S:S.discard(y);comp.add(y);st.append(y)
            out.append(frozenset(comp))
        return out
    def peel(S):
        if not S: return True
        if S in memo: return memo[S]
        res=False
        for v in S:
            if cls(pc(v,S)) in Rset:
                if all(peel(c) for c in comps(S-{v})): res=True;break
        memo[S]=res;return res
    if wall==0:
        n=sum(1 for s in frozen if all(peel(c) for c in comps(s)))
    else:
        n=sum(1 for s in frozen if peel(s))
    return len(frozen),n
if __name__=="__main__":
    R=[NAMES.index(x) for x in sys.argv[1].split(",")]; Lmax=int(sys.argv[2]); wall=int(sys.argv[3]) if len(sys.argv)>3 else 0
    for L in range(2,Lmax+1):
        f,n=counts(L,R,wall)
        print(sys.argv[1],"wall",wall,"L",L,"frozen",f,"reach",n,"lnN/L %.3f lnN/L^2 %.4f"%((math.log(n)/L,math.log(n)/L**2) if n>0 else (0,0)),flush=True)
