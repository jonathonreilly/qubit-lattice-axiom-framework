# Independent rewrite (kill check): rule E (A={0,2,3,4}) on LxL sealed box, outside empty OR recorded wall.
# frozen: every empty site has exactly 1 recorded neighbour (counting wall if wall=1).
# reachable: reverse peel: remove any site whose current recorded-neighbour count (incl wall) is in A.
import sys, itertools
from functools import lru_cache
A={0,2,3,4}
def run(L, wall):
    sites=[(r,c) for r in range(L) for c in range(L)]
    def nb(s):
        r,c=s
        for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
            t=(r+dr,c+dc)
            yield t
    inbox=lambda t:0<=t[0]<L and 0<=t[1]<L
    frozen=[]
    # site-by-site DFS with pruning; check site (r-1,c) when (r,c) assigned, and last row at the end
    grid={}
    def occ(t):
        if inbox(t): return grid.get(t)
        return wall
    def k(t): return sum(1 for u in nb(t) if occ(u)==1)
    def rec(i):
        if i==L*L:
            # check last row and (nothing else pending)
            for c in range(L):
                t=(L-1,c)
                if grid[t]==0 and k(t)!=1: return
            frozen.append(frozenset(t for t in sites if grid[t]))
            return
        r,c=divmod(i,L)
        for v in (0,1):
            grid[(r,c)]=v
            ok=True
            # site (r-1,c) is now fully determined (its down neighbour is (r,c)); also (r,c-1) needs (r,c) as right nb but also needs (r+1,c-1): defer
            if r>0:
                t=(r-1,c)
                if grid[t]==0:
                    # neighbours: (r-2,c),(r,c),(r-1,c-1),(r-1,c+1): (r-1,c+1) assigned already (earlier row)
                    if k(t)!=1: ok=False
            if ok: rec(i+1)
            del grid[(r,c)]
    # grid.get for unassigned returns None -> fine since checks only touch assigned cells
    rec(0)
    # reachability by reverse peeling with component memo (translation-normalised, but wall breaks translation: use raw comps)
    def kk(t,S):
        return sum(1 for u in nb(t) if (u in S) or (not inbox(u) and wall==1))
    memo={}
    def peel(S):
        # S frozenset; returns True if peelable to empty
        if not S: return True
        if S in memo: return memo[S]
        res=False
        for v in S:
            if kk(v,S) in A:
                if peel(S-{v}):
                    res=True;break
        memo[S]=res
        return res
    # speed: split into components only when no wall (wall couples via boundary counts but is static) - just use plain memo with heuristic order
    return frozen, peel
if __name__=="__main__":
    wall=int(sys.argv[1]); Lmax=int(sys.argv[2])
    for L in range(2,Lmax+1):
        fr,peel=run(L,wall)
        n=sum(1 for s in fr if peel(s))
        print("wall",wall,"L",L,"frozen",len(fr),"reachable",n,flush=True)
