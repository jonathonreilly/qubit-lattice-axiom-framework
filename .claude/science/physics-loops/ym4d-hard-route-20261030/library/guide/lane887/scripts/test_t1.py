# Refutation test (GUIDE-level; proves nothing) of Lemma T0 / Lemma B / Lemma T1 at g = 2, L = 8, rule M_min.
# For random cycles gamma on (Z/8)^3: compute the clean boxes from the definition (all minimal relative
# fillings of the box and of each of its 27 core-boxes, all pairs, hereditary 1/4 smallness), then test by
# GF(2) linear algebra whether a 2-chain D exists with (dD)(e) = gamma(e) on every edge interior to a clean box.
# Lemma T1 says it always exists. Also: class != 0 must give an unclean box.
import itertools, random, sys, time
import numpy as np
L=8; g=2
MODE=sys.argv[2] if len(sys.argv)>2 else 'her14'   # her14 is the definition of the note; the others are deliberately wrong (power check)
def E(x,y,z,d): return (((x%L)*L+(y%L))*L+(z%L))*3+d
def P(x,y,z,k): return (((x%L)*L+(y%L))*L+(z%L))*3+k
def C(x,y,z): return ((x%L)*L+(y%L))*L+(z%L)
def unit(d): return tuple(1 if i==d else 0 for i in range(3))
def add(s,t): return tuple(a+b for a,b in zip(s,t))
def plaq_edges(s,k):
    a,b=[i for i in range(3) if i!=k]
    return [E(*s,a),E(*s,b),E(*add(s,unit(b)),a),E(*add(s,unit(a)),b)]
def plaq_cubes(s,k):  # the two cubes at the plaquette (global corners)
    t=list(s); t[k]-=1
    return C(*s),C(*t)
RANGES=[(0,1),(2,3),(0,3)]
def sub_ranges(r): return [q for q in RANGES if q[0]>=r[0] and q[1]<=r[1]]
class Box:
    def __init__(self,o,rng):
        self.o=o; self.rng=rng
        self.edges=[]; self.plaqs=[]; self.cubes=[]
        R=[range(lo,hi+1) for lo,hi in rng]
        for u in itertools.product(*R):
            s=add(o,u)
            for d in range(3):
                if u[d]<=rng[d][1]-1 and all(rng[c][0]<u[c]<rng[c][1] for c in range(3) if c!=d):
                    self.edges.append(E(*s,d))
            for k in range(3):
                if all(u[c]<=rng[c][1]-1 for c in range(3) if c!=k) and rng[k][0]<u[k]<rng[k][1]:
                    self.plaqs.append((s,k))
            if all(u[c]<=rng[c][1]-1 for c in range(3)):
                self.cubes.append(C(*s))
        self.pidx=[P(*s,k) for s,k in self.plaqs]
        self.cpos={c:i for i,c in enumerate(self.cubes)}
        self.pc=[tuple(self.cpos[c] for c in plaq_cubes(s,k)) for s,k in self.plaqs]  # both cubes are in the box
        self.pe=[plaq_edges(s,k) for s,k in self.plaqs]
        self.eset=set(self.edges)
        self.subs=None
    def core_boxes(self):
        if self.subs is None:
            self.subs=[Box(self.o,r) for r in itertools.product(*[sub_ranges(q) for q in self.rng])]
        return self.subs
def particular(box,gam):
    # solve d_rel D = gamma_B over GF(2): unknowns = interior plaquettes
    n=len(box.plaqs); rows=[]
    for e in box.edges:
        m=0
        for i,pe in enumerate(box.pe):
            if e in pe: m|=1<<i
        rows.append([m,gam[e]])
    piv={}
    for m,b in rows:
        for bit,(pm,pb) in list(piv.items()):
            if m>>bit&1: m^=pm; b^=pb
        if m:
            bit=m.bit_length()-1
            for k2 in list(piv):
                pm,pb=piv[k2]
                if pm>>bit&1: piv[k2]=(pm^m,pb^b)
            piv[bit]=(m,b)
        else:
            assert b==0, "gamma_B is not a relative boundary?"
    x=0
    for bit,(pm,pb) in piv.items():
        if pb: x|=1<<bit
    return x   # free variables 0; pivots reduced
def min_fillings(box,gam,cap=4000):
    n=len(box.cubes); npl=len(box.plaqs)
    dref=particular(box,gam)
    if npl==0: return [0]
    if not any(gam[e] for e in box.edges): return [0]
    states=np.arange(1<<n,dtype=np.uint32) if n<=9 else None
    if n<=9:
        area=np.zeros(1<<n,dtype=np.int32); bits=[]
        for i,(a,b) in enumerate(box.pc):
            v=((states>>a)^(states>>b)^((dref>>i)&1))&1
            bits.append(v); area+=v
        mn=area.min(); res=set()
        for w in np.nonzero(area==mn)[0]:
            m=0
            for i in range(npl):
                if bits[i][w]: m|=1<<i
            res.add(m)
        return sorted(res)
    # n == 27: layer DP along the last coordinate of the cube ordering (cubes listed with z fastest)
    assert n==27
    lay=[[c for c in range(27) if c%3==z] for z in range(3)]
    pos={c:(c%3, lay[c%3].index(c)) for c in range(27)}
    S=np.arange(512,dtype=np.uint16)
    intra=[np.zeros(512,dtype=np.int16) for _ in range(3)]
    inter=[np.zeros((512,512),dtype=np.int16) for _ in range(2)]
    for i,(a,b) in enumerate(box.pc):
        (za,ia),(zb,ib)=pos[a],pos[b]; r=(dref>>i)&1
        if za==zb: intra[za]+=(((S>>ia)^(S>>ib)^r)&1).astype(np.int16)
        else:
            if za>zb: (za,ia),(zb,ib)=(zb,ib),(za,ia)
            assert zb==za+1
            inter[za]+=((((S>>ia)&1)[:,None]^((S>>ib)&1)[None,:]^r)).astype(np.int16)
    E01=intra[0][:,None]+inter[0]; m1=E01.min(axis=0)
    E12=(m1+intra[1])[:,None]+inter[1]+intra[2][None,:]
    mn=E12.min(); res=set(); cnt=0
    for s1,s2 in zip(*np.nonzero(E12==mn)):
        for s0 in np.nonzero(E01[:,s1]==m1[s1])[0]:
            cnt+=1
            if cnt>cap: return None
            w=[0]*27
            for z,s in ((0,s0),(1,s1),(2,s2)):
                for j,c in enumerate(lay[z]): w[c]=(int(s)>>j)&1
            m=0
            for i,(a,b) in enumerate(box.pc):
                if w[a]^w[b]^((dref>>i)&1): m|=1<<i
            res.add(m)
    return sorted(res)
def small_exists(B,S):
    # S: bitmask over B.plaqs, a relative cycle; find W with d_rel W = S; is W or its complement small?
    n=len(B.cubes); w=[None]*n; w[0]=0; st=[0]
    adj=[[] for _ in range(n)]
    for i,(a,b) in enumerate(B.pc): adj[a].append((b,i)); adj[b].append((a,i))
    while st:
        u=st.pop()
        for v,i in adj[u]:
            val=w[u]^((S>>i)&1)
            if w[v] is None: w[v]=val; st.append(v)
            else: assert w[v]==val, "S is not a relative boundary"
    assert all(v is not None for v in w)
    for flip in (0,1):
        ok=True
        subs=B.core_boxes() if MODE!='box12' else [B]
        for Bp in subs:
            cnt=sum(w[B.cpos[c]]^flip for c in Bp.cubes)
            if MODE=='her14' and 4*cnt>=len(Bp.cubes): ok=False; break
            if MODE in('her12','box12') and 2*cnt>=len(Bp.cubes): ok=False; break
            if MODE=='her34' and 4*cnt>=3*len(Bp.cubes): ok=False; break
        if ok: return True
    return False
BOXES={X:Box(tuple(g*c for c in X),((0,3),(0,3),(0,3))) for X in itertools.product(range(L//g),repeat=3)}
def clean(N,gam):
    if not any(gam[e] for e in N.edges): return True     # all fillings empty, W = 0
    DN=min_fillings(N,gam)
    if DN is None: return None
    pmap={p:i for i,p in enumerate(N.pidx)}
    for B in N.core_boxes():
        DB=min_fillings(B,gam)
        proj=[pmap[p] for p in B.pidx]
        for D in DN:
            DBr=0
            for i,j in enumerate(proj):
                if D>>j&1: DBr|=1<<i
            for Dp in DB:
                if not small_exists(B,DBr^Dp): return False
    return True
def add_plaq(gam,s,k):
    for e in plaq_edges(s,k): gam[e]^=1
def random_cycle(rs):
    gam=[0]*(3*L**3); cx=tuple(rs.randrange(L) for _ in range(3))
    for _ in range(rs.randint(0,6)):
        s=tuple((cx[i]+rs.randint(-2,2))%L for i in range(3)) if rs.random()<0.7 else tuple(rs.randrange(L) for _ in range(3))
        add_plaq(gam,s,rs.randrange(3))
    for _ in range(rs.choice([0,0,1,1,2])):
        d=rs.randrange(3); a,b=[i for i in range(3) if i!=d]; base=[rs.randrange(L) for _ in range(3)]
        for t in range(L):
            s=list(base); s[d]=t; gam[E(*s,d)]^=1
        for _ in range(rs.randint(0,3)):                    # jogs
            s=list(base); s[d]=rs.randrange(L); add_plaq(gam,tuple(s),rs.choice([a,b]))
    return gam
def cls(gam):
    out=[]
    for d in range(3):
        c=0
        for u in itertools.product(range(L),repeat=2):
            s=[0,0,0]; oth=[i for i in range(3) if i!=d]; s[oth[0]],s[oth[1]]=u; s[d]=0
            c^=gam[E(*s,d)]
        out.append(c)
    return tuple(out)
ALLP=[(s,k) for s in itertools.product(range(L),repeat=3) for k in range(3)]
PE={P(*s,k):plaq_edges(s,k) for s,k in ALLP}
EP={}
for p,es in PE.items():
    for e in es: EP.setdefault(e,[]).append(p)
def solvable(R,gam):
    piv={}
    for e in R:
        m=0
        for p in EP[e]: m|=1<<p
        b=gam[e]
        while m:
            bit=m.bit_length()-1
            if bit in piv: pm,pb=piv[bit]; m^=pm; b^=pb
            else: piv[bit]=(m,b); break
        else:
            if b: return False
    return True
rs=random.Random(887); t=time.time()
stats=dict(trials=0,skipped=0,cls_nonzero=0,nontrivial_clean=0,unclean_boxes=0,fail_solv=0,fail_top=0)
NTR=int(sys.argv[1]) if len(sys.argv)>1 else 60
for tr in range(NTR):
    gam=random_cycle(rs)
    if not any(gam): continue
    cl={}; bad=False
    for X,N in BOXES.items():
        c=clean(N,gam)
        if c is None: bad=True; break
        cl[X]=c
    if bad: stats['skipped']+=1; continue
    stats['trials']+=1
    R=set()
    for X,N in BOXES.items():
        if cl[X]:
            R|=N.eset
            if any(gam[e] for e in N.edges): stats['nontrivial_clean']+=1
        else: stats['unclean_boxes']+=1
    c=cls(gam)
    if any(c):
        stats['cls_nonzero']+=1
        if all(cl.values()): stats['fail_top']+=1
    if not solvable(sorted(R),gam): stats['fail_solv']+=1
print(MODE,stats,"time %.1fs"%(time.time()-t))
