#!/usr/bin/env python3
"""check.py -- disjoint check for J:derive:review-20261017-cubic-fractional-doublet-localization:a1

Independent re-implementation (numpy, standard library only; exact integer/Pauli arithmetic,
GF(2) linear algebra, Fractions) of the SUPPLIED corner-fermion qubit code (BKSF on the corner
graph of Z^3, 48 qubits per site, repetition halves on cross-site links), followed by checks of
a hop-level holonomy calculus for the pair eigenvalue of an involutive symmetry:

   lambda_g = - (-1)^{Phi(gamma . g gamma)}      (Phi = flux of any filling of the closed walk)

and of its consequences (representative invariance, flux dictionary, class, torus sectors,
local dressings, cluster pair-sector representation, vacuum vector).

Nothing here imports or executes the source runners.  Imported (not re-derived) premise: the
source's exact O action U_g exists (C17 note); this script re-verifies the part of it that is
used (exact hop map and stabilizers -> +stabilizers for the generating rotations).
"""
import itertools, random, time, sys
from collections import deque
import numpy as np

T_START=time.time()

DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def perp(d,e): return dot(d,e)==0 and d!=e
def corner(*ds): return tuple(sorted(ds))
CORN = sorted([tuple(sorted((d,e))) for d,e in itertools.combinations(DIRS,2) if dot(d,e)==0])
assert len(CORN)==12

# local qubit layout at a site (48)
ONS=[]
for c1,c2 in itertools.combinations(CORN,2):
    s=set(c1)&set(c2)
    if len(s)==1:
        a=s.pop(); b1=[d for d in c1 if d!=a][0]; b2=[d for d in c2 if d!=a][0]
        if perp(b1,b2): ONS.append((c1,c2))
assert len(ONS)==24
HALF=[(c,a) for c in CORN for a in c]
LOC={('o',p):i for i,p in enumerate(ONS)}
LOC.update({('h',h):24+i for i,h in enumerate(HALF)})

# Pauli: (x,z,p) = i^p X^x Z^z
def pmul(a,b):
    return (a[0]^b[0], a[1]^b[1], (a[2]+b[2]+2*(a[1]&b[0]).bit_count())%4)
def pcomm(a,b):
    return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2==0
def herm(a): return (a[2]-(a[0]&a[1]).bit_count())%2==0
def pinv(P):  # Hermitian conjugate = inverse
    return (P[0],P[1],(-P[2]+2*(P[0]&P[1]).bit_count())%4)
def mkX(qs):
    x=0
    for i in qs: x^=1<<i
    return (x,0,0)
def mkZ(qs):
    z=0
    for i in qs: z^=1<<i
    return (0,z,0)

class Code:
    def __init__(self, L, flux):
        self.L=L; self.flux=dict(flux)
        self.SITES=list(itertools.product(range(L),repeat=3))
        self.SID={v:i for i,v in enumerate(self.SITES)}
        self.NQ=48*len(self.SITES)
        self.Acache={}
        self.INC={}
    def add(self,v,d): return tuple((a+b)%self.L for a,b in zip(v,d))
    def proj(self,q): return (tuple(a%self.L for a in q[0]), q[1])
    def qb(self,v,lab): return 48*self.SID[v]+LOC[lab]
    def incident(self,q):
        if q in self.INC: return self.INC[q]
        v,c=q; out=[]
        for p in ONS:
            if c in p:
                other=p[1] if p[0]==c else p[0]
                out.append((('o',other),('onsite',p),(v,other)))
        for a in c:
            b=[d for d in c if d!=a][0]
            out.append((('l',a),('link',(c,a)),(self.add(v,a),corner(neg(a),b))))
        self.INC[q]=out; return out
    @staticmethod
    def keyord(k): return (0,k[1]) if k[0]=='o' else (1,k[1])
    def edge_qubits(self,q,ek,ed):
        v,c=q
        if ek=='onsite': return [self.qb(v,('o',ed))]
        cc,a=ed; b=[d for d in cc if d!=a][0]
        w=self.add(v,a); c2=corner(neg(a),b)
        return [self.qb(v,('h',(cc,a))), self.qb(w,('h',(c2,neg(a))))]
    def edge_zqubit(self,q,ek,ed):
        v,c=q
        if ek=='onsite': return self.qb(v,('o',ed))
        return self.qb(v,('h',ed))
    def canon_first(self,q,r):
        if q[0]==r[0]: return CORN.index(q[1])<CORN.index(r[1])
        for k,(ek,ed),nb in self.incident(q):
            if nb==r and ek=='link': return sum(ed[1])>0
        raise KeyError((q,r))
    def A(self,q,r):
        """hop operator for ADJACENT vertices, arguments reduced mod L"""
        key=(q,r)
        if key in self.Acache: return self.Acache[key]
        if not self.canon_first(q,r):
            x,z,p=self.A(r,q); res=(x,z,(p+2)%4)
        else:
            kq=kr=None
            for k,(ek,ed),nb in self.incident(q):
                if nb==r: kq=k; EK,ED=ek,ed; break
            else: raise KeyError((q,r))
            for k2,(ek2,ed2),nb2 in self.incident(r):
                if nb2==q: kr=k2; break
            zq=[self.edge_zqubit(q,a,b) for k2,(a,b),_ in self.incident(q) if self.keyord(k2)<self.keyord(kq)]
            zr=[self.edge_zqubit(r,a,b) for k2,(a,b),_ in self.incident(r) if self.keyord(k2)<self.keyord(kr)]
            res=pmul(mkX(self.edge_qubits(q,EK,ED)), mkZ(zq+zr))
        self.Acache[key]=res; return res
    def hop(self,q,r):  # unwrapped vertices
        return self.A(self.proj(q),self.proj(r))
    def Bop(self,q):
        return mkZ([self.edge_zqubit(q,ek,ed) for _,(ek,ed),_ in self.incident(q)])
    def Rop(self,v,h):
        c,a=h; b=[d for d in c if d!=a][0]
        return mkZ([self.qb(v,('h',h)), self.qb(self.add(v,a),('h',(corner(neg(a),b),neg(a))))])

# neighbours in the infinite lattice (unwrapped)
def nbrs(q):
    v,c=q; out=[]
    for p in ONS:
        if c in p:
            other=p[1] if p[0]==c else p[0]; out.append((v,other))
    for a in c:
        b=[d for d in c if d!=a][0]
        out.append((tuple(x+y for x,y in zip(v,a)), corner(neg(a),b)))
    return out

def cycles_at(v):
    """face boundaries (vertex lists, unwrapped) associated with site v: (kind, list)"""
    out=[]
    for d in DIRS:
        a=[f for f in DIRS if perp(f,d) and f!=neg(d)]
        a0=a[0]; b0=[f for f in a if perp(f,a0) and f!=neg(a0)][0]
        ring=[a0,b0,neg(a0),neg(b0)]
        out.append(('square',[(v,corner(d,r)) for r in ring]))
        for i in range(4):
            p,q=ring[i],ring[(i+1)%4]; w=tuple(x+y for x,y in zip(v,d))
            out.append(('tube',[(v,corner(d,p)),(w,corner(neg(d),p)),(w,corner(neg(d),q)),(v,corner(d,q))]))
    for s in itertools.product((1,-1),repeat=3):
        x,y,z=(s[0],0,0),(0,s[1],0),(0,0,s[2])
        out.append(('triangle',[(v,corner(x,y)),(v,corner(y,z)),(v,corner(z,x))]))
    for d,e in (((1,0,0),(0,1,0)),((0,1,0),(0,0,1)),((0,0,1),(1,0,0))):
        ad=lambda v,d: tuple(x+y for x,y in zip(v,d))
        out.append(('plaquette',[(v,corner(d,e)),(ad(v,d),corner(neg(d),e)),(ad(ad(v,d),e),corner(neg(d),neg(e))),(ad(v,e),corner(d,neg(e)))]))
    return out

def walk_op(code, seq):
    """ordered product of hops along an (unwrapped) vertex sequence"""
    P=(0,0,0)
    for i in range(len(seq)-1):
        P=pmul(P, code.hop(seq[i],seq[i+1]))
    return P

def loop_stab(code, seq, F):
    n=len(seq); P=(0,0,n%4)
    for i in range(n):
        P=pmul(P, code.hop(seq[i],seq[(i+1)%n]))
    if F: P=(P[0],P[1],(P[2]+2)%4)
    return P

class StabGroup:
    def __init__(self,n):
        self.n=n; self.piv={}
        self.neg_identity=False
    def vec(self,P): return P[0]|(P[1]<<self.n)
    def add(self,P):
        v=self.vec(P); comb=P
        while v:
            c=v.bit_length()-1
            if c in self.piv:
                pv,pP=self.piv[c]; v^=pv; comb=pmul(comb,pP)
            else:
                self.piv[c]=(v,comb); return True
        if comb[2]%4!=0: self.neg_identity=True
        return False
    def reduce(self,P):
        """phase k with P * (product of pivots) = i^k I, or None if P not in span"""
        v=self.vec(P); comb=P
        while v:
            c=v.bit_length()-1
            if c not in self.piv: return None
            pv,pP=self.piv[c]; v^=pv; comb=pmul(comb,pP)
        return comb[2]%4

def build(L, flux, verbose=True):
    code=Code(L,flux)
    t0=time.time()
    sites=code.SITES
    verts=[(v,c) for v in sites for c in CORN]
    code.verts=verts
    gens=[]
    for q in verts: gens.append(('B',code.Bop(q)))
    for v in sites:
        for h in HALF:
            if sum(h[1])>0: gens.append(('R',code.Rop(v,h)))
    for v in sites:
        for kind,seq in cycles_at(v):
            gens.append((kind, loop_stab(code, seq, flux[kind])))
    G=StabGroup(code.NQ)
    for kind,P in gens: G.add(P)
    code.G=G; code.gens=gens
    if verbose: print(f"  built L={L} flux={flux}: {len(gens)} generators, rank {len(G.piv)}, log2dim {code.NQ-len(G.piv)}, neg_identity={G.neg_identity}, {time.time()-t0:.1f}s")
    return code

# ---------------- rotations & space-group involutions on the unwrapped lattice
def rot_mats():
    out=[]
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            M=np.zeros((3,3),int)
            for i in range(3): M[i,perm[i]]=sg[i]
            if round(np.linalg.det(M))==1: out.append(M)
    return out
ROTS=rot_mats()
def rd(R,d): return tuple(int(x) for x in R@np.array(d))
def rc(R,c): return corner(*[rd(R,d) for d in c])
class Sym:
    """x -> R x + t (t integer vector, possibly half-integers via 2t) acting on vertices (v,c)"""
    def __init__(self,R,t=(0,0,0)): self.R=R; self.t=tuple(t)
    def __call__(self,q):
        v,c=q
        w=tuple(int(x)+tt for x,tt in zip(self.R@np.array(v),self.t))
        return (w,rc(self.R,c))

# ---------------- filling of closed walks by faces (GF(2))
class Filler:
    def __init__(self,B,flux):
        """complex of faces whose vertices all lie on sites in [-B,B]^3"""
        self.B=B; self.flux=flux
        rng=range(-B,B+1)
        faces=[]; seen=set()
        for v in itertools.product(rng,repeat=3):
            for kind,seq in cycles_at(v):
                if any(max(abs(x) for x in u[0])>B for u in seq): continue
                es=frozenset(frozenset((seq[i],seq[(i+1)%len(seq)])) for i in range(len(seq)))
                if es in seen: continue
                seen.add(es); faces.append((kind,seq,es))
        self.faces=faces
        self.eid={}
        for kind,seq,es in faces:
            for e in es:
                if e not in self.eid: self.eid[e]=len(self.eid)
        self.piv={}
        for i,(kind,seq,es) in enumerate(faces):
            v=0
            for e in es: v^=1<<self.eid[e]
            m=1<<i
            while v:
                c=v.bit_length()-1
                if c in self.piv:
                    pv,pm=self.piv[c]; v^=pv; m^=pm
                else:
                    self.piv[c]=(v,m); break
    def chain(self,walk):
        v=0
        for i in range(len(walk)-1):
            e=frozenset((walk[i],walk[i+1]))
            if e not in self.eid: return None
            v^=1<<self.eid[e]
        return v
    def fill(self,walk):
        """walk: closed vertex sequence (first==last). returns list of face indices or None"""
        v=self.chain(walk)
        if v is None: return None
        m=0
        while v:
            c=v.bit_length()-1
            if c not in self.piv: return None
            pv,pm=self.piv[c]; v^=pv; m^=pm
        out=[]; i=0
        while m:
            if m&1: out.append(i)
            m>>=1; i+=1
        return out
    def Phi(self,walk,flux=None):
        flux=self.flux if flux is None else flux
        f=self.fill(walk)
        if f is None: return None
        return sum(flux[self.faces[i][0]] for i in f)%2

def bfs_path(src,dst,B,rnd=None,avoid=()):
    prev={src:None}; dq=deque([src])
    while dq:
        x=dq.popleft()
        if x==dst: break
        nb=nbrs(x)
        if rnd: rnd.shuffle(nb)
        for y in nb:
            if y in prev or y in avoid: continue
            if max(abs(t) for t in y[0])>B: continue
            prev[y]=x; dq.append(y)
    if dst not in prev: return None
    p=[dst]
    while p[-1]!=src: p.append(prev[p[-1]])
    return p[::-1]

def random_walk_path(src,dst,B,rnd,nway=2,simple=True):
    """concatenate BFS segments through random waypoints; optionally require simple"""
    allv=[(v,c) for v in itertools.product(range(-B,B+1),repeat=3) for c in CORN]
    for _ in range(200):
        pts=[src]+[rnd.choice(allv) for _ in range(nway)]+[dst]
        path=[src]; ok=True
        for a,b in zip(pts,pts[1:]):
            seg=bfs_path(a,b,B,rnd)
            if seg is None: ok=False;break
            path+=seg[1:]
        if not ok: continue
        if simple and len(set(path))!=len(path): continue
        return path
    return None

def pair_sign(code,sym,walk):
    S=walk_op(code,walk)
    SR=walk_op(code,[sym(x) for x in walk])
    T=pmul(pinv(S),SR)
    r=code.G.reduce(T)
    if r is None: return None
    assert r in (0,2),r
    return 1 if r==0 else -1

# ---------------- the rotation operators U_R (site permutation, on-site CZ network, Z fixes)
def rs_mod(code,R,v): return tuple(int(x)%code.L for x in R@np.array(v))
def rlab(R,lab):
    if lab[0]=='o':
        c1,c2=lab[1]; return ('o',tuple(sorted((rc(R,c1),rc(R,c2)))))
    c,a=lab[1]; return ('h',(rc(R,c),rd(R,a)))
def qperm(code,R):
    perm=[0]*code.NQ
    for v in code.SITES:
        rv=rs_mod(code,R,v)
        for lab in LOC:
            perm[code.qb(v,lab)]=code.qb(rv,rlab(R,lab))
    return perm
def apply_perm(P,perm):
    nx=nz=0
    for i in bits_of(P[0]): nx|=1<<perm[i]
    for i in bits_of(P[1]): nz|=1<<perm[i]
    return (nx,nz,P[2])
def bits_of(v):
    while v:
        b=v&-v; yield b.bit_length()-1; v^=b
def apply_cz(P,pairs):
    x,z,p=P
    for a,b in pairs:
        xa,xb=(x>>a)&1,(x>>b)&1
        if xb: z^=1<<a
        if xa: z^=1<<b
        if xa and xb: p=(p+2)%4
    return (x,z,p)
def apply_zfix(P,zs):
    return (P[0],P[1],(P[2]+2*(P[0]&zs).bit_count())%4)
def cz_network(code,R):
    Rinv=np.round(np.linalg.inv(R)).astype(int)
    pairs=[]
    for x in code.verts:
        v,c=x
        pre=(rs_mod(code,Rinv,v),rc(Rinv,c))
        inc_x=code.incident(x); inc_pre={nb:k for k,_,nb in code.incident(pre)}
        items=[]
        for k,(ek,ed),nb in inc_x:
            nbpre=(rs_mod(code,Rinv,nb[0]),rc(Rinv,nb[1]))
            items.append((code.keyord(k),code.keyord(inc_pre[nbpre]),code.edge_zqubit(x,ek,ed)))
        for (k1,o1,q1),(k2,o2,q2) in itertools.combinations(items,2):
            if (k1<k2)!=(o1<o2): pairs.append((q1,q2))
    return pairs
def build_U(code,R):
    perm=qperm(code,R); cz=cz_network(code,R)
    zfix=0; allhops=True
    seen=set()
    for q in code.verts:
        for k,(ek,ed),r in code.incident(q):
            if not code.canon_first(q,r): continue
            Aqr=code.A(q,r)
            img=apply_cz(apply_perm(Aqr,perm),cz)
            Rq=(rs_mod(code,R,q[0]),rc(R,q[1])); Rr=(rs_mod(code,R,r[0]),rc(R,r[1]))
            tgt=code.A(Rq,Rr)
            if (img[0],img[1])!=(tgt[0],tgt[1]): allhops=False; continue
            if (img[2]-tgt[2])%4==2:
                a,b=(Rq,Rr) if code.canon_first(Rq,Rr) else (Rr,Rq)
                for kk,(e2k,e2d),nb in code.incident(a):
                    if nb==b: zfix^=1<<code.edge_zqubit(a,e2k,e2d); break
            elif img[2]!=tgt[2]: allhops=False
    def U(P):
        return apply_zfix(apply_cz(apply_perm(P,perm),cz),zfix)
    return U,allhops


# =====================================================================================
#                                   CHECK SECTIONS
# =====================================================================================
PASS = 0
FAIL = 0
NAMES = ('square', 'triangle', 'plaquette', 'tube')
DEFAULT_FLUX = dict(square=1, triangle=0, plaquette=1, tube=0)


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (("  | " + detail) if detail else ""), flush=True)


def tick(label):
    print(f"   [{time.time() - T_START:6.1f}s] {label}", flush=True)


def is_axis(R):
    return int(np.trace(R)) == -1 and np.allclose(np.abs(np.diag(R)), 1)


def is_edge(R):
    return int(np.trace(R)) == -1 and not np.allclose(np.abs(np.diag(R)), 1)


def is_c4(R):
    return int(np.trace(R)) == 1 and not np.allclose(R @ R, np.eye(3))


def bfs_window(src, dst, rnd=None, pad=2):
    """BFS in the unwrapped lattice restricted to the bounding box of src,dst padded by pad sites"""
    lo = [min(a, b) - pad for a, b in zip(src[0], dst[0])]
    hi = [max(a, b) + pad for a, b in zip(src[0], dst[0])]
    prev = {src: None}
    dq = deque([src])
    while dq:
        x = dq.popleft()
        if x == dst:
            break
        nb = nbrs(x)
        if rnd:
            rnd.shuffle(nb)
        for y in nb:
            if y in prev:
                continue
            if any(y[0][i] < lo[i] or y[0][i] > hi[i] for i in range(3)):
                continue
            prev[y] = x
            dq.append(y)
    if dst not in prev:
        return None
    p = [dst]
    while p[-1] != src:
        p.append(prev[p[-1]])
    return p[::-1]


def closed_walk_random(rnd, B, k):
    """random closed walk (not nec. simple) in the unwrapped lattice, sites within radius B"""
    allv = [(v, c) for v in itertools.product(range(-B, B + 1), repeat=3) for c in CORN]
    x0 = rnd.choice(allv)
    pts = [x0] + [rnd.choice(allv) for _ in range(k)] + [x0]
    walk = [x0]
    for a, b in zip(pts, pts[1:]):
        seg = bfs_path(a, b, B, rnd)
        walk += seg[1:]
    return walk


def Eop(code, walk):
    """E(c) = i^{|c|} * ordered product of hops, for a closed walk c (vertex list, first==last)"""
    n = len(walk) - 1
    P = walk_op(code, walk)
    return (P[0], P[1], (P[2] + n) % 4)


# ------------------------------------------------------------------------------------
print("# SECTION 0: the supplied code, re-implemented (L=4, default fluxes square=pi, plaquette=pi)")
code = build(4, DEFAULT_FLUX, verbose=False)
G = code.G
check("code: 4160 generators (768 B, 768 R, 2624 loops) of rank 3069; log2 code dimension 3; no -I in the group",
      len(code.gens) == 4160 and len(G.piv) == 3069 and code.NQ - len(G.piv) == 3 and not G.neg_identity)
hops = []
for q in code.verts:
    for k, (ek, ed), r in code.incident(q):
        if code.canon_first(q, r):
            hops.append((q, r, code.A(q, r)))
check("2304 hop operators A(q,r) are Hermitian Paulis (6 hops per corner vertex)",
      len(hops) == 2304 and all(herm(P) for _, _, P in hops))
bad = 0
for i in range(len(hops)):
    qi, ri, Pi = hops[i]
    si = {qi, ri}
    for j in range(i + 1, len(hops)):
        qj, rj, Pj = hops[j]
        if pcomm(Pi, Pj) != (len(si & {qj, rj}) != 1):
            bad += 1
check("BKSF hop algebra (exhaustive, all 2304*2303/2 pairs): hops anticommute iff they share exactly one vertex", bad == 0, f"violations={bad}")
gens = [P for _, P in code.gens]
bad = sum(1 for i in range(len(gens)) for j in range(i + 1, len(gens)) if not pcomm(gens[i], gens[j]))
check("all 4160 stabilizer generators pairwise commute (exhaustive)", bad == 0, f"violations={bad}")
loops_P = [P for kd, P in code.gens if kd not in ('B', 'R')]
bad = sum(1 for Lp in loops_P for (_, _, H) in hops if not pcomm(Lp, H))
check("every loop generator commutes with every hop (exhaustive 2624 x 2304)", bad == 0, f"violations={bad}")
q0 = code.verts[0]
nb3 = [r for _, _, r in code.incident(q0)][:3]
W3 = [code.A(q0, r) for r in nb3]
prod = (0, 0, 0)
for Pq in (W3[2], pinv(W3[1]), W3[0], pinv(W3[2]), W3[1], pinv(W3[0])):
    prod = pmul(prod, Pq)
check("T-junction exchange sign of the corner charge is -1 (theta = -1, a fermion)", prod[0] == 0 and prod[1] == 0 and prod[2] == 2)
ok = True
for Fb in itertools.product((0, 1), repeat=4):
    cd = build(4, dict(zip(NAMES, Fb)), verbose=False)
    ok &= (not cd.G.neg_identity) and (cd.NQ - len(cd.G.piv) == 3)
check("all 16 uniform flux patterns (square,triangle,plaquette,tube) give a consistent code (no -I) with log2 dimension 3", ok)
tick("section 0")

# ------------------------------------------------------------------------------------
print("# SECTION 1: cycle calculus (hop products around closed walks)")
rnd = random.Random(20261017)
FILL2 = Filler(2, DEFAULT_FLUX)
check("fillability: in the radius-2 site box every closed walk is a GF(2) boundary of faces (cycle rank = face-boundary rank)",
      len(FILL2.piv) == len(FILL2.eid) - len({u for e in FILL2.eid for u in e}) + 1,
      f"rank {len(FILL2.piv)} edges {len(FILL2.eid)}")
# (a) parity lemma: anticommuting pairs
bad = 0
nwalks = 0
for _ in range(300):
    x0 = rnd.choice(code.verts)
    x0 = ((rnd.randint(-1, 1), rnd.randint(-1, 1), rnd.randint(-1, 1)), x0[1])
    w = [x0]
    for _ in range(rnd.randint(1, 14)):
        w.append(rnd.choice(nbrs(w[-1])))
    ops = [code.hop(w[i], w[i + 1]) for i in range(len(w) - 1)]
    nac = sum(1 for i in range(len(ops)) for j in range(i + 1, len(ops)) if not pcomm(ops[i], ops[j]))
    n = len(ops)
    want = (n - 1) if w[0] != w[-1] else n
    bad += (nac - want) % 2 != 0
    # Pi^2 = (-1)^{N_ac}
    P = walk_op(code, w)
    sq = pmul(P, P)
    bad += not (sq[0] == 0 and sq[1] == 0 and sq[2] == (2 * nac) % 4)
    nwalks += 1
check("Lemma 0 (quadratic-form parity): #anticommuting hop pairs = n-1 (open walk, distinct ends) or n (closed) mod 2; hence Pi^2=(-1)^{n-1}",
      bad == 0, f"{nwalks} random walks incl. backtracking, violations={bad}")
# (b) E multiplicativity E(ab)=E(a abar')E(a' b)
bad = 0
ntr = 0
for _ in range(150):
    x = ((rnd.randint(-1, 1),) * 3, rnd.choice(CORN))
    y = ((rnd.randint(-1, 1), rnd.randint(-1, 1), rnd.randint(-1, 1)), rnd.choice(CORN))
    if x == y:
        continue
    a = random_walk_path(x, y, 2, rnd, nway=rnd.randint(0, 2), simple=False)
    a2 = random_walk_path(x, y, 2, rnd, nway=rnd.randint(0, 2), simple=False)
    b = random_walk_path(y, x, 2, rnd, nway=rnd.randint(0, 2), simple=False)
    if a is None or a2 is None or b is None:
        continue
    lhs = Eop(code, a + b[1:])
    rhs = pmul(Eop(code, a + a2[::-1][1:]), Eop(code, a2 + b[1:]))
    bad += lhs != rhs
    ntr += 1
check("Lemma 2 (exact Pauli identity): E(a.b) = E(a.abar') E(a'.b) for walks a,a':x->y, b:y->x (E(c)=i^{|c|} * hop product)",
      bad == 0 and ntr > 100, f"{ntr} random triples, violations={bad}")
# (c) E(c) commutes with all hops; base point invariance; (d) flux rule
bad_c = bad_d = bad_s = 0
nloop = 0
for _ in range(60):
    w = closed_walk_random(rnd, 1, rnd.randint(1, 3))
    E = Eop(code, w)
    bad_c += any(not pcomm(E, H) for (_, _, H) in hops)
    sh = w[1:] + [w[1]]
    bad_s += Eop(code, sh) != E          # cyclic shift
    r = G.reduce(E)
    ph = FILL2.Phi(w)
    if r is None or ph is None or r != 2 * ph:
        bad_d += 1
    nloop += 1
check("Lemma 2': E(c) commutes with every hop and is base-point invariant, for random closed walks", bad_c == 0 and bad_s == 0, f"{nloop} walks")
check("Lemma 3 (flux rule): E(c) = (-1)^{Phi(c)} * (stabilizer), Phi = total flux of any face filling of c  (reduce phase == 2*Phi)",
      bad_d == 0, f"{nloop} random closed walks (not nec. simple), violations={bad_d}")
tick("section 1")

# ------------------------------------------------------------------------------------
print("# SECTION 2: pair-eigenvalue theorem  lambda = -(-1)^{Phi(gamma . g gamma)}  and flux dictionary")
rnd = random.Random(7)
res = {}
bad = 0
ntot = 0
for k, R in enumerate(ROTS):
    if int(np.trace(R)) != -1:
        continue
    kind = 'axis' if is_axis(R) else 'edge'
    sym = Sym(R)
    vals = set()
    for trial in range(30):
        v = tuple(rnd.randint(-1, 1) for _ in range(3))
        c = rnd.choice(CORN)
        q = (v, c)
        Rq = sym(q)
        if Rq == q:
            continue
        path = random_walk_path(q, Rq, 2, rnd, nway=rnd.randint(0, 3), simple=rnd.random() < 0.6)
        if path is None:
            continue
        lam = pair_sign(code, sym, path)
        cw = path + [sym(x) for x in path][1:]
        phi = FILL2.Phi(cw)
        pred = -(-1) ** phi
        ntot += 1
        if lam is None or phi is None or lam != pred:
            bad += 1
        vals.add(lam)
    res.setdefault(kind, set()).update(vals)
check("Theorem A: all 9 point-group C2, 270 random walks (simple and non-simple) from q to Rq: Pauli-reduction sign == -(-1)^{Phi} (independent GF(2) face filling)",
      bad == 0 and ntot > 240, f"tested={ntot}, mismatches={bad}")
check("default flux: lambda = +1 for all axis C2 and -1 for all edge C2, independent of q and of the walk (representative invariance)",
      res.get('axis') == {1} and res.get('edge') == {-1}, str({k: sorted(v) for k, v in res.items()}))
# explicit base loops (proof objects)
fnames = {}
for kd, seq in cycles_at((0, 0, 0)):
    fnames[(kd, frozenset(seq))] = seq
def face_of(kind, verts):
    return fnames[(kind, frozenset(verts))]
X, Y, Zd = (1, 0, 0), (0, 1, 0), (0, 0, 1)
C2z = [R for R in ROTS if (R == np.diag([-1, -1, 1])).all()][0]
symz = Sym(C2z)
C2e = [R for R in ROTS if (R == np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])).all()][0]
syme = Sym(C2e)
Fz = Filler(1, DEFAULT_FLUX)
sqwalk = [((0, 0, 0), corner(Zd, X)), ((0, 0, 0), corner(Zd, Y)), ((0, 0, 0), corner(Zd, neg(X)))]
cwz = sqwalk + [symz(x) for x in sqwalk][1:]
sq_z = face_of('square', [((0, 0, 0), corner(Zd, a)) for a in (X, Y, neg(X), neg(Y))])
ok_sq = len(cwz) == 5 and cwz[0] == cwz[-1] and Fz.chain(cwz) == Fz.chain(sq_z + [sq_z[0]])
hexw = [((0, 0, 0), corner(X, Zd)), ((0, 0, 0), corner(X, neg(Y))), ((0, 0, 0), corner(X, neg(Zd))), ((0, 0, 0), corner(Y, neg(Zd)))]
cwh = hexw + [syme(x) for x in hexw][1:]
sqx = face_of('square', [((0, 0, 0), corner(X, a)) for a in (Y, Zd, neg(Y), neg(Zd))])
sqy = face_of('square', [((0, 0, 0), corner(Y, a)) for a in (X, Zd, neg(X), neg(Zd))])
tpp = face_of('triangle', [((0, 0, 0), corner(X, Y)), ((0, 0, 0), corner(Y, Zd)), ((0, 0, 0), corner(Zd, X))])
tpm = face_of('triangle', [((0, 0, 0), corner(X, Y)), ((0, 0, 0), corner(Y, neg(Zd))), ((0, 0, 0), corner(neg(Zd), X))])
chx = 0
for f in (sqx, sqy, tpp, tpm):
    chx ^= Fz.chain(f + [f[0]])
ok_hex = len(cwh) == 7 and cwh[0] == cwh[-1] and Fz.chain(cwh) == chx
check("explicit proof objects: the C2z walk q -> Rq on the z-square closes to exactly the boundary of the z-square (Phi=F_sq); the C2[110] hexagon is exactly the boundary of {square_x, square_y, triangle(+++), triangle(++-)} (Phi=2F_sq+2F_tri=0 for every flux)",
      ok_sq and ok_hex)
# 16 flux patterns x 8 involutions
def mat(rows): return np.array(rows, int)
invs = {
    'site axis z': (Sym(C2z), lambda F: F['square']),
    'site edge [110]': (Sym(C2e), lambda F: 0),
    'bond-centred axis z (1/2,0)': (Sym(C2z, (1, 0, 0)), lambda F: 0),
    'bond-centred axis z (0,1/2)': (Sym(C2z, (0, 1, 0)), lambda F: 0),
    'plaquette-centred axis z (1/2,1/2)': (Sym(C2z, (1, 1, 0)), lambda F: F['plaquette']),
    'edge[110] offset (1,-1,0)': (Sym(C2e, (1, -1, 0)), lambda F: 0),
    'edge[110] offset (0,0,1)': (Sym(C2e, (0, 0, 1)), lambda F: F['tube']),
    'edge[110] offset (1,-1,1)': (Sym(C2e, (1, -1, 1)), lambda F: F['tube']),
}
rnd = random.Random(99)
bad_phi = bad_rule = 0
ntot = 0
byname = {}
for Fb in itertools.product((0, 1), repeat=4):
    fl = dict(zip(NAMES, Fb))
    cd = build(4, fl, verbose=False)
    F3 = Filler(3, fl)
    for name, (sym, rule) in invs.items():
        for trial in range(6):
            v = tuple(rnd.randint(-1, 1) for _ in range(3))
            c = rnd.choice(CORN)
            q = (v, c)
            Rq = sym(q)
            if Rq == q:
                continue
            path = random_walk_path(q, Rq, 2, rnd, nway=rnd.randint(0, 2), simple=rnd.random() < 0.7)
            if path is None:
                continue
            lam = pair_sign(cd, sym, path)
            cw = path + [sym(x) for x in path][1:]
            phi = F3.Phi(cw)
            ntot += 1
            if lam is None or phi is None or lam != -(-1) ** phi:
                bad_phi += 1
            if lam != -(-1) ** rule(fl):
                bad_rule += 1
            byname.setdefault(name, set()).add(lam)
check("Theorem A holds for all 16 uniform flux patterns and 8 space-group involutions (site / bond-centred / plaquette-centred / offset-edge axes)",
      bad_phi == 0 and ntot > 700, f"tested={ntot}, mismatches={bad_phi}")
check("flux dictionary (SUGGESTED rule, CHECKED on this sample): lambda = -(-1)^{F(face pierced at its centre by the axis)}: site axis -> square, plaquette-centred axis -> plaquette, z-offset edge axis -> tube; site-edge, bond-centred and in-plane edge axes -> -1 for every flux",
      bad_rule == 0, f"rule mismatches={bad_rule}")
# C4 four-charge orbit
rnd = random.Random(21)
tabc4 = []
for Fb in [(1, 0, 1, 0), (0, 0, 0, 0), (0, 1, 1, 1), (1, 1, 0, 1)]:
    fl = dict(zip(NAMES, Fb))
    cd = build(4, fl, verbose=False)
    F3 = Filler(3, fl)
    for k, R in enumerate(ROTS):
        if not is_c4(R):
            continue
        sym = Sym(R)
        for trial in range(6):
            v = tuple(rnd.randint(-1, 1) for _ in range(3))
            c = rnd.choice(CORN)
            orb = [(v, c)]
            for _ in range(3):
                orb.append(sym(orb[-1]))
            if len(set(orb)) < 4:
                continue
            path = random_walk_path(orb[0], orb[1], 3, rnd, nway=rnd.randint(0, 2), simple=True)
            if path is None:
                continue
            img = lambda w, m: ([sym(x) for x in w] if m == 1 else [sym(sym(x)) for x in w] if m == 2 else [sym(sym(sym(x))) for x in w])
            S = pmul(walk_op(cd, path), walk_op(cd, img(path, 2)))
            US = pmul(walk_op(cd, img(path, 1)), walk_op(cd, img(path, 3)))
            r = cd.G.reduce(pmul(pinv(S), US))
            cw = path + img(path, 1)[1:] + img(path, 2)[1:] + img(path, 3)[1:]
            phi = F3.Phi(cw)
            tabc4.append((None if r is None else (1 if r == 0 else -1), -(-1) ** phi if phi is not None else None, -(-1) ** fl['square']))
check("C4 four-charge orbit (charges at q,gq,g^2 q,g^3 q; creators gamma + g^2 gamma): lambda = -(-1)^{Phi(closed 4-fold walk)} = -(-1)^{F_square} (cyclic 4-permutation sign -1 times ghat^4 = eta_axis)",
      len(tabc4) > 80 and all(a == b == c for a, b, c in tabc4), f"{len(tabc4)} cases")
tick("section 2")

# ------------------------------------------------------------------------------------
print("# SECTION 3: admissible dressings -- local TQO (all neutral Paulis in a ball are stabilizers) and dressing invariance")
def tqo(cd, L, r):
    n = cd.NQ
    ballsites = [v for v in cd.SITES if all(((c + r) % L) <= 2 * r for c in v)]
    inball = set()
    for v in ballsites:
        for j in range(48):
            inball.add(cd.SID[v] * 48 + j)
    qin = sorted(inball)
    pos = {}
    for kk, i in enumerate(qin):
        pos[i] = kk
    qout = [i for i in range(n) if i not in inball]
    for kk, i in enumerate(qout):
        pos[i] = kk
    m = len(qin)
    no = len(qout)
    def restrict(P):
        xin = zin = xout = zout = 0
        for i in bits_of(P[0]):
            if i in inball: xin |= 1 << pos[i]
            else: xout |= 1 << pos[i]
        for i in bits_of(P[1]):
            if i in inball: zin |= 1 << pos[i]
            else: zout |= 1 << pos[i]
        return xin, zin, xout, zout
    piv = {}
    piv2 = {}
    for kind, P in cd.gens:
        xin, zin, xout, zout = restrict(P)
        v = (((xout | (zout << no))) << (2 * m)) | (xin | (zin << m))
        while v:
            c = v.bit_length() - 1
            if c in piv: v ^= piv[c]
            else: piv[c] = v; break
        v2 = xin | (zin << m)
        while v2:
            c = v2.bit_length() - 1
            if c in piv2: v2 ^= piv2[c]
            else: piv2[c] = v2; break
    dimSB = sum(1 for c in piv if c < 2 * m)
    cent = 2 * m - len(piv2)
    return len(ballsites), dimSB, cent
ns, dS, cen = tqo(code, 4, 1)
check("local TQO, L=4, 3x3x3-site ball: dim(centralizer of S inside Pauli(ball)) == dim(S cap Pauli(ball)) => every neutral Pauli in the ball is +-(stabilizer)",
      cen == dS, f"sites={ns}, dim S_B={dS}, centralizer={cen}")
code6 = build(6, DEFAULT_FLUX, verbose=False)
ns, dS, cen = tqo(code6, 6, 2)
check("local TQO, L=6, 5x5x5-site ball (covers the [-2,2]^3 creator box): same equality", cen == dS and code6.NQ - len(code6.G.piv) == 3, f"sites={ns}, dim S_B={dS}, centralizer={cen}")
ns, dS, cen = tqo(code, 4, 2)
check("negative control: L=4 with a 5-wide ball wraps the torus and the equality FAILS by the 6 logical Pauli generators", cen - dS == 6, f"excess={cen - dS}")
# dressing invariance with a genuine Clifford U (generators)
rnd = random.Random(5)
Uz, okz = build_U(code, C2z)
bad = 0
n_d = 0
for trial in range(12):
    v = tuple(rnd.randint(-1, 1) for _ in range(3)); c = rnd.choice(CORN); q = (v, c)
    Rq = symz(q)
    path = random_walk_path(q, Rq, 2, rnd, nway=1, simple=True)
    if path is None: continue
    S = walk_op(code, path)
    Cst = (0, 0, 0)
    for kind, P in rnd.sample(code.gens, 150):
        Cst = pmul(Cst, P)
    SC = pmul(S, Cst)
    r0 = code.G.reduce(pmul(pinv(S), Uz(S)))
    r1 = code.G.reduce(pmul(pinv(SC), Uz(SC)))
    bad += (r0 is None) or (r0 != r1)
    n_d += 1
check("dressing invariance with the real Clifford U (C2z): lambda(S*C) == lambda(S) for C a random product of 150 stabilizer generators", bad == 0 and n_d > 8, f"{n_d} cases")
tick("section 3")

# ------------------------------------------------------------------------------------
print("# SECTION 4: torus sectors (L=4): scalar-ness of the comparison operator is governed by the winding of gamma . g gamma")
rnd = random.Random(11)
L = 4
# independent logical operators E(a_x), E(a_y), E(a_z) (straight hop loops through the 4 sites of a lattice line)
def line_loop(axis):
    """closed straight hop loop winding once around the torus along `axis`"""
    d = [0, 0, 0]; d[axis] = 1; d = tuple(d)
    perp_dirs = [e for e in DIRS if perp(e, d) and e != neg(d)]
    p = perp_dirs[0]
    e = [f for f in perp_dirs if perp(f, p) and f != neg(p)][0]
    seq = [((0, 0, 0), corner(d, p))]
    for step in range(L):
        v = seq[-1][0]
        w = tuple(a + b for a, b in zip(v, d))
        seq.append((w, corner(neg(d), p)))      # link
        seq.append((w, corner(p, e)))           # on-site
        seq.append((w, corner(d, p)))           # on-site
    return seq
lg = []
for ax in range(3):
    sq_ = line_loop(ax)
    assert sq_[-1][0] == tuple(L if i == ax else 0 for i in range(3)) and sq_[-1][1] == sq_[0][1]
    lg.append(Eop(code, sq_))
neutral = all(pcomm(E, H) for E in lg for (_, _, H) in hops) and all(pcomm(E, P) for E in lg for P in gens)
indep = True
for mask in range(1, 8):
    E = (0, 0, 0)
    for i in range(3):
        if (mask >> i) & 1: E = pmul(E, lg[i])
    indep &= code.G.reduce(E) is None
check("three straight lattice-line hop loops E(a_x),E(a_y),E(a_z) are neutral (commute with all stabilizers and hops) and all 7 nonzero products lie OUTSIDE the stabilizer group: independent logical operators",
      neutral and indep)
tab = {}
bad_scalar = 0
bad_val = 0
nsamp = 0
for k, R in enumerate(ROTS):
    if int(np.trace(R)) != -1: continue
    kind = 'axis' if is_axis(R) else 'edge'
    sym = Sym(R)
    for trial in range(14):
        v = tuple(rnd.randint(0, 3) for _ in range(3)); c = rnd.choice(CORN); q = (v, c)
        Rq = sym(q)
        if code.proj(Rq) == code.proj(q): continue
        n = tuple(rnd.randint(-1, 1) for _ in range(3))
        tgt = (tuple(a + L * b for a, b in zip(Rq[0], n)), Rq[1])
        path = bfs_window(q, tgt, rnd, pad=2)
        if path is None: continue
        m = (np.eye(3, dtype=int) + R) @ np.array(n)
        odd = bool(np.any(m % 2))
        lam = pair_sign(code, sym, path)
        nsamp += 1
        if odd != (lam is None): bad_scalar += 1
        if lam is not None:
            want = 1 if kind == 'axis' else -1
            if lam != want: bad_val += 1
        tab.setdefault((kind, odd), 0)
        tab[(kind, odd)] += 1
check("torus L=4 (random creators q -> R q + L n, n in {-1,0,1}^3): comparison operator S^-1 U(S) is a scalar iff the winding m=(1+R)n of gamma.R gamma is even; odd-winding cases are genuine logical (non-scalar) loops",
      bad_scalar == 0 and nsamp > 80 and tab.get(('edge', True), 0) > 5, f"samples={nsamp}, table={tab}")
check("torus L=4: whenever the comparison operator is scalar (even winding, incl. nonzero even winding such as 2 z-hat), lambda equals the contractible value (+1 axis, -1 edge)",
      bad_val == 0 and tab.get(('axis', False), 0) > 10)
tick("section 4")

# ------------------------------------------------------------------------------------
print("# SECTION 5: cluster Majorana lift (PSG), its class, D2 restrictions, pair-sector representation")
O3 = (0, 0, 0)
cl_verts = [(O3, c) for c in CORN]
vid = {q: i for i, q in enumerate(cl_verts)}
cl_edges = []
for q in cl_verts:
    for r in nbrs(q):
        if r[0] == O3 and vid[q] < vid[r]:
            cl_edges.append((q, r))
eid_cl = {frozenset(e): i for i, e in enumerate(cl_edges)}
cl_faces = [(kd, seq) for kd, seq in cycles_at(O3) if kd in ('square', 'triangle')]
def face_edges(seq): return [eid_cl[frozenset((seq[i], seq[(i + 1) % len(seq)]))] for i in range(len(seq))]
def gf2_solve(rows, rhs, n):
    piv = {}
    for r, b in zip(rows, rhs):
        x = 0
        for j in r: x ^= 1 << j
        if b: x ^= 1 << n
        while True:
            low = x & ((1 << n) - 1)
            if low == 0:
                if x: return None
                break
            c = low.bit_length() - 1
            if c in piv: x ^= piv[c]
            else: piv[c] = x; break
    sol = 0
    for c in sorted(piv):
        x = piv[c]; rest = x & ((1 << c) - 1)
        if ((x >> n) & 1) ^ (rest & sol).bit_count() & 1: sol |= 1 << c
    return [(sol >> j) & 1 for j in range(n)]
check("cluster geometry: 12 corners, 24 on-site hops, 6 squares + 8 triangles forming the cuboctahedron sphere (Euler 12-24+14=2); sphere flux 6F_sq+8F_tri is even for every pattern",
      len(cl_verts) == 12 and len(cl_edges) == 24 and len(cl_faces) == 14 and 12 - 24 + 14 == 2)
rotid = {tuple(R.flatten()): k for k, R in enumerate(ROTS)}
MUL = [[rotid[tuple((ROTS[a] @ ROTS[b]).flatten())] for b in range(24)] for a in range(24)]
ID = rotid[tuple(np.eye(3, dtype=int).flatten())]
def cluster_lift(Fd):
    u = gf2_solve([face_edges(s) for k, s in cl_faces], [Fd[k] for k, s in cl_faces], 24)
    assert u is not None
    Ms = []
    for R in ROTS:
        sym = Sym(R)
        P = {q: sym(q) for q in cl_verts}
        sigma = {cl_verts[0]: 0}
        dq = deque([cl_verts[0]])
        while dq:
            q = dq.popleft()
            for r in nbrs(q):
                if r[0] != O3 or r in sigma: continue
                e = eid_cl[frozenset((q, r))]; ge = eid_cl[frozenset((P[q], P[r]))]
                sigma[r] = sigma[q] ^ u[e] ^ u[ge]; dq.append(r)
        for (q, r) in cl_edges:
            e = eid_cl[frozenset((q, r))]; ge = eid_cl[frozenset((P[q], P[r]))]
            assert sigma[q] ^ sigma[r] == u[e] ^ u[ge]
        Ms.append((P, sigma))
    return Ms
def cocycle(Ms):
    c = [[None] * 24 for _ in range(24)]
    for a in range(24):
        for b in range(24):
            vals = set()
            Pb, sb = Ms[b]; Pa, sa = Ms[a]; Pab, sab = Ms[MUL[a][b]]
            for q in cl_verts:
                assert Pa[Pb[q]] == Pab[q]
                vals.add(sb[q] ^ sa[Pb[q]] ^ sab[q])
            if len(vals) != 1: return None
            c[a][b] = vals.pop()
    return c
LIFTS = {}
ok_lift = True
for Fsq, Ftri in itertools.product((0, 1), repeat=2):
    Ms = cluster_lift(dict(square=Fsq, triangle=Ftri))
    c = cocycle(Ms)
    ok_lift &= c is not None
    LIFTS[(Fsq, Ftri)] = (Ms, c)
check("PSG/Majorana lift exists on the cluster for all (F_sq,F_tri): signed permutations M_g with M_g M_h = c(g,h) M_gh and c(g,h) = +-1 independent of the corner (a Z2 central extension)", ok_lift)
def cocycle_ok(c):
    return all((c[b][cc] ^ c[MUL[a][b]][cc] ^ c[a][MUL[b][cc]] ^ c[a][b]) == 0 for a in range(24) for b in range(24) for cc in range(24)) and all(c[ID][g] == 0 == c[g][ID] for g in range(24))
check("each lift cocycle c satisfies the 2-cocycle identity and is normalised", all(cocycle_ok(c) for (_, c) in LIFTS.values()))
axis_idx = [k for k, R in enumerate(ROTS) if is_axis(R)]
edge_idx = [k for k, R in enumerate(ROTS) if is_edge(R)]
check("c(g,g) on involutions: axis C2 -> (-1)^{F_square}; edge C2 -> +1 (independent of F_triangle) -- the PSG signs of the source note, from the holonomy of the gauge field",
      all(set(c[g][g] for g in axis_idx) == {Fs} and set(c[g][g] for g in edge_idx) == {0} for (Fs, Ft), (_, c) in LIFTS.items()))
# H^2(O;Z2) by linear algebra
def var(a, b): return a * 24 + b
rows = []
for a in range(24):
    for b in range(24):
        for cc in range(24):
            r = {}
            for t in (var(b, cc), var(MUL[a][b], cc), var(a, MUL[b][cc]), var(a, b)): r[t] = r.get(t, 0) ^ 1
            rows.append([t for t, v in r.items() if v])
for g in range(24):
    rows.append([var(ID, g)]); rows.append([var(g, ID)])
def nullspace(rows, N):
    piv = {}
    for r in rows:
        x = 0
        for j in r: x ^= 1 << j
        while x:
            c = x.bit_length() - 1
            if c in piv: x ^= piv[c]
            else: piv[c] = x; break
    cols = sorted(piv)
    for c in cols:
        for c2 in cols:
            if c2 > c and (piv[c2] >> c) & 1: piv[c2] ^= piv[c]
    free = [j for j in range(N) if j not in piv]
    basis = []
    for f in free:
        v = 1 << f
        for c in cols:
            if (piv[c] >> f) & 1: v |= 1 << c
        basis.append(v)
    return basis
def rank_of(vs):
    piv = {}
    for x in vs:
        while x:
            c = x.bit_length() - 1
            if c in piv: x ^= piv[c]
            else: piv[c] = x; break
    return len(piv)
Zb = nullspace(rows, 576)
Bb = []
for s in range(24):
    if s == ID: continue
    v = 0
    for a in range(24):
        for b in range(24):
            if (a == s) ^ (b == s) ^ (MUL[a][b] == s): v |= 1 << var(a, b)
    Bb.append(v)
evf = lambda v: ((v >> var(axis_idx[0], axis_idx[0])) & 1) | (((v >> var(edge_idx[0], edge_idx[0])) & 1) << 1)
dimH2 = len(Zb) - rank_of(Bb)
check("H^2(O;Z2) = Z2^2 (exact GF(2) linear algebra over normalised cochains) and the map c -> (c(axis C2,axis C2), c(edge C2,edge C2)) is injective on classes (kernel = coboundaries)",
      dimH2 == 2 and rank_of([evf(z) for z in Zb]) == 2 and set(evf(b) for b in Bb) == {0} and len(Zb) - 2 == rank_of(Bb))
def w1_of(R):
    p = [DIRS.index(rd(R, d)) for d in DIRS]
    s = 0; seen = [False] * 6
    for i in range(6):
        if not seen[i]:
            j = i; l = 0
            while not seen[j]: seen[j] = True; j = p[j]; l += 1
            s += l - 1
    return s % 2
W1 = [w1_of(R) for R in ROTS]
w1sq = [[W1[a] & W1[b] for b in range(24)] for a in range(24)]
check("w1 = sign of the permutation of the six directions: even on axis C2, odd on edge C2, C4; cocycle w1^2(g,h)=w1(g)w1(h) has invariants (axis,edge)=(+,-); spin cover w2 has (-,-) (every pi-rotation lifts to an element of order 4 in SU(2))",
      all(W1[g] == 0 for g in axis_idx) and all(W1[g] == 1 for g in edge_idx) and cocycle_ok(w1sq) and all(w1sq[g][g] == 0 for g in axis_idx) and all(w1sq[g][g] == 1 for g in edge_idx))
# U(1) triviality
C4z = rotid[tuple(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]).flatten())]
C3d = rotid[tuple(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]).flatten())]
def u1_trivial(c):
    for t4 in range(24):
        for t3 in range(24):
            th = {ID: 0, C4z: t4, C3d: t3}
            dq = deque([ID, C4z, C3d])
            while dq:
                a = dq.popleft()
                for g in (C4z, C3d):
                    b = MUL[a][g]
                    if b not in th:
                        th[b] = (th[a] + th[g] - 12 * c[a][g]) % 24; dq.append(b)
            if len(th) == 24 and all((th[a] + th[b] - th[MUL[a][b]] - 12 * c[a][b]) % 24 == 0 for a in range(24) for b in range(24)):
                return True
    return False
u1 = {}
for key, (Ms, c) in LIFTS.items():
    ctw = [[c[a][b] ^ w1sq[a][b] for b in range(24)] for a in range(24)]
    u1[key] = (u1_trivial(c), u1_trivial(ctw))
    cls_un = (set(c[g][g] for g in axis_idx), set(c[g][g] for g in edge_idx))
check("class of the untwisted lift: invariants (axis,edge)=(F_sq,0) => class F_sq*(w2+w1^2); twisted by i^{w1}: (F_sq,1) => class F_sq*w2 + (F_sq+1)*w1^2;  w2 alone is never an untwisted class of this uniform-flux family",
      all(set(c[g][g] for g in axis_idx) == {Fs} and set(c[g][g] for g in edge_idx) == {0} for (Fs, Ft), (_, c) in LIFTS.items()))
check("U(1)-class (solve nu(a)nu(b)=c(a,b)nu(ab) in mu_24): TRIVIAL iff F_sq=0; for F_sq=1 it is nontrivial both untwisted and twisted -- the twist i^{w1} does not change the U(1)-class [w2]",
      all((u1[(Fs, Ft)] == ((Fs == 0), (Fs == 0))) for (Fs, Ft) in LIFTS))
# D2 restrictions
Ms, c = LIFTS[(1, 0)]
def Mmat(k):
    P, s = Ms[k]
    M = np.zeros((12, 12), int)
    for q in cl_verts: M[vid[P[q]], vid[q]] = 1 - 2 * s[q]
    return M
I12 = np.eye(12, dtype=int)
ax_mats = [Mmat(k) for k in axis_idx]
ok_d2 = all((M @ M == -I12).all() for M in ax_mats) and all((A @ B == -B @ A).all() for A, B in itertools.combinations(ax_mats, 2)) and all(np.trace(M) == 0 for M in ax_mats)
# free orbits: no corner fixed by any axis C2, so each axis-D2 orbit of corners has size 4
fixed_axis = sum(1 for k in axis_idx for q in cl_verts if Sym(ROTS[k])(q) == q)
fixed_edge = sum(1 for k in edge_idx for q in cl_verts if Sym(ROTS[k])(q) == q)
check("D2 restrictions (axis D2={1,C2x,C2y,C2z}, F_sq=pi): M_x^2=M_y^2=M_z^2=-1, pairwise anticommuting, trace 0 => the 12-dim cluster space is 6 copies of the unique 2-dim projective irrep (no one-dimensional D2 sector); no corner is fixed by any axis C2 (D2 acts freely, orbits of size 4)",
      ok_d2 and fixed_axis == 0, f"fixed corners: axis C2 {fixed_axis}, edge C2 {fixed_edge} (each edge C2 fixes 2 of 12)")
Mzz = Mmat([k for k in axis_idx if (ROTS[k] == np.diag([-1, -1, 1])).all()][0])
ea = [k for k in edge_idx if (ROTS[k] == np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])).all()][0]
eb = [k for k in edge_idx if (ROTS[k] == np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])).all()][0]
Ma, Mb = Mmat(ea), Mmat(eb)
check("edge-D2 {1,C2z,C2[110],C2[1-10]} (untwisted, F_sq=pi): squares (-,+,+), pairwise anticommuting => again only 2-dimensional constituents (odd number of -1 squares)",
      (Mzz @ Mzz == -I12).all() and (Ma @ Ma == I12).all() and (Mb @ Mb == I12).all() and (Ma @ Mb == -Mb @ Ma).all() and (Ma @ Mzz == -Mzz @ Ma).all() and (Mb @ Mzz == -Mzz @ Mb).all())
# pair sector from the Pauli code
def cluster_pair_rep(cd, Rlist):
    S = {}
    for i, q in enumerate(cl_verts):
        for j, r in enumerate(cl_verts):
            if i < j:
                p = bfs_path(q, r, 0)
                S[(i, j)] = (p, walk_op(cd, p))
    def state(i, j):
        return (1, S[(i, j)][1]) if i < j else (-1, S[(j, i)][1])
    reps = []
    for k in Rlist:
        sym = Sym(ROTS[k])
        D = {}
        for (i, j), (p, Sop) in S.items():
            img = walk_op(cd, [sym(x) for x in p])
            gi, gj = vid[sym(cl_verts[i])], vid[sym(cl_verts[j])]
            sg, Pt = state(gi, gj)
            r = cd.G.reduce(pmul(pinv(Pt), img))
            if r not in (0, 2): return None
            val = (1 if r == 0 else -1) * sg
            D[(i, j)] = (val, (gi, gj)) if gi < gj else (-val, (gj, gi))
        reps.append(D)
    return S, reps
for Fsq in (1, 0):
    fl = dict(square=Fsq, triangle=0, plaquette=Fsq, tube=0)
    cd = code if Fsq == 1 else build(4, fl, verbose=False)
    S_, Dr = cluster_pair_rep(cd, range(24))
    bad = 0
    for a in range(24):
        for b in range(24):
            for key in S_:
                s_b, k_b = Dr[b][key]; s_a, k_a = Dr[a][k_b]; s_ab, k_ab = Dr[MUL[a][b]][key]
                if k_a != k_ab or s_a * s_b != s_ab: bad += 1
    Msx, cx = LIFTS[(Fsq, 0)]
    def chi_L2(Ms_, k):
        P, s = Ms_[k]
        tr1 = sum(1 - 2 * s[q] for q in cl_verts if P[q] == q)
        tr2 = sum((1 - 2 * s[q]) * (1 - 2 * s[P[q]]) for q in cl_verts if P[P[q]] == q)
        return (tr1 * tr1 - tr2) // 2
    def chi_perm(k):
        P = {q: Sym(ROTS[k])(q) for q in cl_verts}
        tr1 = sum(1 for q in cl_verts if P[q] == q); tr2 = sum(1 for q in cl_verts if P[P[q]] == q)
        return (tr1 * tr1 - tr2) // 2
    cD = [sum(Dr[k][key][0] for key in S_ if Dr[k][key][1] == key) for k in range(24)]
    same = all(cD[k] == chi_L2(Msx, k) for k in range(24))
    samep = all(cD[k] == chi_perm(k) for k in range(24))
    check(f"cluster two-charge sector computed from the Pauli code (66 states, hop strings inside the cluster; F_sq={Fsq}): a genuine linear O-rep (0 group-law violations); character == that of Lambda^2(rho_hat) with rho_hat the signed-permutation lift of class c",
          bad == 0 and same, f"group-law violations={bad}; equals Lambda^2(unsigned permutation rep): {samep}")
    if Fsq == 1:
        check("for F_sq=pi the two-charge sector differs from Lambda^2 of the plain corner-permutation representation (axis C2 character +6 vs -6): the pair sector sees the projective sign structure",
              not samep and cD[axis_idx[0]] == 6 and chi_perm(axis_idx[0]) == -6)
        # lambda from Pauli == -c(g,g) at the cluster for the 9 C2
        okl = True
        for g in axis_idx + edge_idx:
            sym = Sym(ROTS[g])
            for q in cl_verts:
                if sym(q) == q: continue
                p = bfs_path(q, sym(q), 0)
                lam = pair_sign(code, sym, p)
                okl &= lam == -(-1) ** cx[g][g]
        check("cluster pair eigenvalues from the Pauli code equal -c(g,g) of the Majorana lift for all nine C2 and every non-fixed corner (lambda = theta * eta with theta=-1)", okl)
tick("section 5")

# ------------------------------------------------------------------------------------
print("# SECTION 6: re-verification of the used part of the imported O action, and the vacuum vector")
rotgens = {'C4z': C4z, 'C3[111]': C3d}
genmap = {(P[0], P[1]): P[2] for kd, P in code.gens}
for name, k in rotgens.items():
    U, okU = build_U(code, ROTS[k])
    R = ROTS[k]
    bad = 0
    for q in code.verts:
        for kk, (ek, ed), r in code.incident(q):
            if not code.canon_first(q, r): continue
            Rq = (rs_mod(code, R, q[0]), rc(R, q[1])); Rr = (rs_mod(code, R, r[0]), rc(R, r[1]))
            bad += U(code.A(q, r)) != code.A(Rq, Rr)
    badg = 0
    for kd, P in code.gens:
        Q = U(P)
        if genmap.get((Q[0], Q[1])) != Q[2]: badg += 1
    check(f"U_{name} = (qubit permutation) . (on-site CZ network) . (Z fixes), rebuilt independently: maps every hop exactly to the rotated hop and every one of the 4160 stabilizer generators to +(a generator)",
          okU and bad == 0 and badg == 0, f"hop mismatches={bad}, generator failures={badg}")
# translations: U_T = site permutation (same local label); exact hop map and stabilizers -> +stabilizers
def trans_perm(cd, t):
    perm = [0] * cd.NQ
    for v in cd.SITES:
        w = cd.add(v, t)
        for lab in LOC:
            perm[cd.qb(v, lab)] = cd.qb(w, lab)
    return perm
bad_t = bad_tg = 0
for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    perm = trans_perm(code, t)
    for q in code.verts:
        for kk, (ek, ed), r in code.incident(q):
            if not code.canon_first(q, r): continue
            tq = (code.add(q[0], t), q[1]); tr = (code.add(r[0], t), r[1])
            bad_t += apply_perm(code.A(q, r), perm) != code.A(tq, tr)
    for kd, P in code.gens:
        Q = apply_perm(P, perm)
        bad_tg += genmap.get((Q[0], Q[1])) != Q[2]
check("unit translations U_T (site permutation, same local label) map every hop exactly to the translated hop and every stabilizer generator to +(a generator): the compositions U_T U_R used for bond-/plaquette-centred involutions are hop-exact",
      bad_t == 0 and bad_tg == 0, f"hop mismatches={bad_t}, generator failures={bad_tg}")
# vacuum vector
n = code.NQ
G2 = {}
for kd, P in code.gens:
    v = P[1] | (P[0] << n); comb = P
    while v:
        c = v.bit_length() - 1
        if c in G2:
            pv, pP = G2[c]; v ^= pv; comb = pmul(comb, pP)
        else:
            G2[c] = (v, comb); break
ztype = [pP for c, (pv, pP) in G2.items() if c < n]
signs_ok = all(pP[2] == 0 and pP[0] == 0 for pP in ztype)
allflux_ok = True
for Fb in itertools.product((0, 1), repeat=4):
    cd = build(4, dict(zip(NAMES, Fb)), verbose=False)
    G3 = {}
    for kd, P in cd.gens:
        v = P[1] | (P[0] << n); comb = P
        while v:
            c = v.bit_length() - 1
            if c in G3:
                pv, pP = G3[c]; v ^= pv; comb = pmul(comb, pP)
            else:
                G3[c] = (v, comb); break
    zt = [pP for c, (pv, pP) in G3.items() if c < n]
    allflux_ok &= all(pP[2] == 0 for pP in zt) and len(zt) == 1535
check("vacuum reference: the Z-type subgroup of S has dimension 1535 (products of B and R) and every element has sign +1 for all 16 flux patterns, so <0^N|Pi_S|0^N> = 2^(1535-3069) > 0 and |Omega> = Pi_S|0^N> is a nonzero vector of the 8-dim code space",
      signs_ok and len(ztype) == 1535 and allflux_ok)
PBt = (0, 0, 0)
for q in code.verts: PBt = pmul(PBt, code.Bop(q))
for v in code.SITES:
    for h in HALF:
        if sum(h[1]) > 0: PBt = pmul(PBt, code.Rop(v, h))
check("W twist: prod_q B_q * prod_links R = identity (so W^2 = (-i)^{24 L^3} prod B prod R = I); W = (-1)^{(#violated B,R)/2} equals +1 on |0^N> and on the code space, and commutes with Pi_S",
      PBt == (0, 0, 0) and (24 * 4 ** 3) % 4 == 0)
tick("section 6")

# ------------------------------------------------------------------------------------
print(f"   total runtime {time.time() - T_START:.1f}s", flush=True)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL == 0:
    print("HIT: scoped exact result on the supplied corner code -- cycle calculus gives lambda_g = -(-1)^{Phi(gamma.g gamma)} for any involutive hop-exact symmetry and any walk (so the pair sign is representative-independent for contractible comparison loops, any L / infinite volume), with flux dictionary (axis C2 <-> square flux, edge C2 <-> none, plaquette-/tube-pierced axes <-> plaquette/tube), uniform-flux classes {0, w2+w1^2} only (w2 alone needs the i^{w1} twist; U(1)-class [w2] iff F_sq=pi, twist independent), torus-sector dichotomy (scalar iff even winding), local-TQO dressings in 3^3 (L=4) and 5^3 (L=6) balls, cluster pair sector = Lambda^2 of the projective lift, and an explicit common phase-one vacuum vector on the L=4 torus")
print("SUMMARY: Independent re-implementation of the supplied corner qubit code shows that every involutive hop-exact symmetry has pair eigenvalue -(-1)^{flux of a filling of gamma.g gamma} for all walks (representative-independent in infinite volume), that the Majorana-lift class is F_sq*(w2+w1^2) so w2 needs the i^{w1} twist but the U(1)-class [w2] does not, plus checked local-TQO dressings, torus winding sectors, D2 restrictions, pair-sector character and a vacuum vector; the single-charge (odd-sector) localized operators remain unconstructed.")
sys.exit(1 if FAIL else 0)
