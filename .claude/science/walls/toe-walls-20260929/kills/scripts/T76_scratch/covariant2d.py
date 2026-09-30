# Kill check: ALL rotation-covariant nearest-neighbour formation rules on Z^2 (not only count-threshold).
# Neighbour occupancy pattern (N,E,S,W) 4-bit; classes under proper rotations C4: 
#  c0 none, c1 single, c2a two adjacent, c2o two opposite, c3 three, c4 four.  Rule = subset of the 6 classes.
# Gadget search (sealed windows) as in attack, generalised: sealed = for every subset J of outside neighbours, class(in|J) not in R.
import sys, itertools, time
def cls(p):  # p: 4-bit tuple order N,E,S,W
    k=sum(p)
    if k==0: return 0
    if k==1: return 1
    if k==2:
        return 3 if (p[0]==p[2]) else 2   # opposite (N&S or E&W) -> 3 ; adjacent -> 2
    if k==3: return 4
    return 5
NAMES=['0','1','2adj','2opp','3','4']
DIRS=[(-1,0),(0,1),(1,0),(0,-1)]
def make_window(a,b):
    sites=[(r,c) for r in range(a) for c in range(b)]
    idx={s:i for i,s in enumerate(sites)}
    nb=[[idx.get((r+dr,c+dc),-1) for dr,dc in DIRS] for r,c in sites]
    return sites,nb
def find(a,b,R,need=2,cap=400000,budget=30000):
    sites,nb=make_window(a,b); n=len(sites)
    Rset=set(R)
    # sealed table: for site v, given inside occupancy of its inside neighbours (tuple with None for outside) -> ok?
    def sealed_ok(v,occ):
        outs=[i for i in range(4) if nb[v][i]==-1]
        for J in itertools.product((0,1),repeat=len(outs)):
            p=[0]*4
            for i in range(4):
                if nb[v][i]!=-1: p[i]=occ(nb[v][i])
            for i,j in zip(outs,J): p[i]=j
            if cls(p) in Rset: return False
        return True
    ready=[[] for _ in range(n)]
    for v in range(n): ready[max([v]+[u for u in nb[v] if u!=-1])].append(v)
    good=[];leaves=[0];capped=[False]
    def peel(mask):
        # reverse peel with component memo: remove v with class(current nbrs) in R
        memo={}; cnt=[0]
        class B(Exception):pass
        def comps(S):
            S=set(S);out=[]
            while S:
                s=S.pop();comp={s};st=[s]
                while st:
                    x=st.pop()
                    for y in nb[x]:
                        if y!=-1 and y in S:S.discard(y);comp.add(y);st.append(y)
                out.append(frozenset(comp))
            return out
        def rc(comp):
            if comp in memo:return memo[comp]
            cnt[0]+=1
            if cnt[0]>budget: raise B()
            ok=False
            for v in comp:
                p=[1 if (nb[v][i]!=-1 and nb[v][i] in comp) else 0 for i in range(4)]
                if cls(p) in Rset:
                    if all(rc(c) for c in comps(comp-{v})): ok=True;break
            memo[comp]=ok;return ok
        S={v for v in range(n) if (mask>>v)&1}
        try: return all(rc(c) for c in comps(S))
        except B: return None
    unk=[0]
    def rec(i,mask):
        if capped[0] or len(good)>=need:return
        if i==n:
            leaves[0]+=1
            if leaves[0]>cap:capped[0]=True;return
            r=True if mask==0 else peel(mask)
            if r:good.append(mask)
            elif r is None:unk[0]+=1
            return
        for val in (1,0):
            m2=mask|(val<<i);ok=True
            for v in ready[i]:
                if not (m2>>v)&1:
                    if not sealed_ok(v,lambda u:(m2>>u)&1): ok=False;break
            if ok: rec(i+1,m2)
    rec(0,0)
    return good,leaves[0],unk[0],capped[0]
if __name__=="__main__":
    maxside=int(sys.argv[1]); maxvol=int(sys.argv[2])
    shapes=[(a,b) for a in range(1,maxside+1) for b in range(a,maxside+1) if a*b<=maxvol]
    shapes.sort(key=lambda s:s[0]*s[1])
    for bits in range(1<<6):
        R=[i for i in range(6) if (bits>>i)&1]
        cnt_thr = None
        if 0 not in R:
            continue
        if len(R)==6: continue
        # is it count-threshold? (2adj and 2opp both in or both out)
        ct=((2 in R)==(3 in R))
        res="NOGADGET_upto"
        for sh in shapes:
            g,lv,unk,cp=find(sh[0],sh[1],R)
            if len(g)>=2:
                res=f"GADGET {sh}"; break
            if cp or unk: res=f"UNRESOLVED at {sh} (cap={cp},unk={unk})"; 
        print("R=",[NAMES[i] for i in R],"count-threshold" if ct else "NEW-covariant",res,flush=True)
