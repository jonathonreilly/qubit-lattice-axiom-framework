"""Independent core: star, cubic group O, Pauli strings, actions, commutation, torus rank with -1 check."""
import itertools, numpy as np

POS = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
PIDX = {p:i for i,p in enumerate(POS)}
# labels 0=I,1=X,2=Y,3=Z ; binary (x,z)
LX = [0,1,1,0]; LZ = [0,0,1,1]
def lab(xb,zb): return [[0,3],[1,2]][xb][zb]

def group_O():
    G=[]
    for perm in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            R=np.zeros((3,3),int)
            for a in range(3): R[perm[a],a]=s[a]   # R e_a = s_a e_perm(a)
            if round(np.linalg.det(R))==1: G.append(R)
    assert len(G)==24
    return G
O = group_O()

def act(R, S, soldered=True):
    """S: tuple of 21 labels (site-major, qubit a). returns (sign, newS)."""
    out=[0]*21; sign=1
    for i,p in enumerate(POS):
        q = tuple(int(v) for v in R.dot(p)); j=PIDX[q]
        for a in range(3):
            L=S[3*i+a]
            if L==0: continue
            pa = int(np.nonzero(R[:,a])[0][0])          # qubit a -> qubit pi(a)
            if soldered:
                b=L-1; pb=int(np.nonzero(R[:,b])[0][0]); sign*=int(R[pb,b]); NL=pb+1
            else: NL=L
            out[3*j+pa]=NL
    return sign, tuple(out)

def symp(L1,L2): return (LX[L1]*LZ[L2]+LZ[L1]*LX[L2])&1

TRANS = sorted({tuple(np.subtract(p,q)) for p in POS for q in POS})
def overlaps(t):
    """pairs (i,j): site i of S at POS[i] == POS[j]+t (site j of translated S')."""
    return [(i,PIDX[tuple(np.subtract(POS[i],t))]) for i in range(7) if tuple(np.subtract(POS[i],t)) in PIDX]
OVL = {t:overlaps(t) for t in TRANS}

def commute_all_translates(S,T):
    for t,pr in OVL.items():
        s=0
        for i,j in pr:
            for a in range(3): s^=symp(S[3*i+a],T[3*j+a])
        if s: return False
    return True

# ---------- torus machinery with phase ----------
def to_op(S, sign, L, shift=(0,0,0)):
    n=3*L**3; x=0; z=0; ny=0
    for i,p in enumerate(POS):
        r=[(p[k]+shift[k])%L for k in range(3)]
        base=((r[0]*L+r[1])*L+r[2])*3
        for a in range(3):
            l=S[3*i+a]
            if LX[l]: x|=1<<(base+a)
            if LZ[l]: z|=1<<(base+a)
            if l==2: ny+=1
    ph=(ny + (0 if sign==1 else 2))%4     # op = i^ph X^x Z^z
    return [x,z,ph]

def mul(A,B):
    return [A[0]^B[0], A[1]^B[1], (A[2]+B[2]+2*bin(A[1]&B[0]).count('1'))%4]

def eliminate(ops, nbits):
    """ops: list of [x,z,ph]. Returns rank, and list of bad relation phases (ph!=0 when reduced to identity)."""
    piv={}; bad=[]
    for op in ops:
        v=list(op)
        while True:
            key=(v[0]<<nbits)|v[1]
            if key==0:
                if v[2]!=0: bad.append(v[2])
                break
            hb=key.bit_length()-1
            if hb in piv: v=mul(v,piv[hb])
            else: piv[hb]=v; break
    return len(piv), bad

def local_basis(signed_list):
    """signed_list: [(sign,S)] on star. Return basis ops (as (sign-phase op on 'infinite' star)) and local bad phases."""
    # use a big L to avoid wrapping: L=5 places star without wrap (coords -1..1 mod 5 distinct)
    ops=[to_op(S,s,5) for s,S in signed_list]
    piv={}; bad=[]
    nb=375
    for op in ops:
        v=list(op)
        while True:
            key=(v[0]<<nb)|v[1]
            if key==0:
                if v[2]!=0: bad.append(v[2])
                break
            hb=key.bit_length()-1
            if hb in piv: v=mul(v,piv[hb])
            else: piv[hb]=v; break
    # convert basis ops back to star strings with sign
    basis=[]
    for v in piv.values():
        S=[0]*21; ny=0
        for i,p in enumerate(POS):
            r=[p[k]%5 for k in range(3)]; base=((r[0]*5+r[1])*5+r[2])*3
            for a in range(3):
                xb=(v[0]>>(base+a))&1; zb=(v[1]>>(base+a))&1
                S[3*i+a]=lab(xb,zb); ny+= (xb and zb)
        ph=(v[2]-ny)%4
        assert ph in (0,2), ph
        basis.append((1 if ph==0 else -1, tuple(S)))
    return basis, bad

def torus_dim(basis, L):
    n=3*L**3
    ops=[to_op(S,s,L,(tx,ty,tz)) for s,S in basis for tx in range(L) for ty in range(L) for tz in range(L)]
    rk,bad=eliminate(ops,n)
    return n-rk, bad
