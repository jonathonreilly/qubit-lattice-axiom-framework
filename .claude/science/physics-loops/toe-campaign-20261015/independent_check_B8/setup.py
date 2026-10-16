"""Independent check B8: build signed binary-octahedral rep on 2x2x2 block corners,
covariant nearest-site walk ansatz, and emit exact unitarity equations."""
import itertools, sys, json
import numpy as np
import sympy as sp

corners = list(itertools.product([0,1],repeat=3))
cidx = {v:i for i,v in enumerate(corners)}
offs = list(itertools.product([-1,0,1],repeat=3))

Rz = np.array([[0,-1,0],[1,0,0],[0,0,1]])
Rx = np.array([[1,0,0],[0,0,-1],[0,1,0]])

def act_corner(R,v):
    w = R @ (2*np.array(v)-1)  # 2(v-c)
    return tuple(((w+1)//2).tolist())

def perm(R):
    P = np.zeros((8,8),dtype=int)
    for v in corners:
        P[cidx[act_corner(R,v)],cidx[v]] = 1
    return P

def gen_group(gens):
    I = (np.eye(3,dtype=int), np.eye(8,dtype=int))
    elems = {(I[0].tobytes(),I[1].tobytes()):I}
    frontier=[I]
    while frontier:
        nf=[]
        for (R,D) in frontier:
            for (Rg,Dg) in gens:
                R2=Rg@R; D2=Dg@D
                key=(R2.tobytes(),D2.tobytes())
                if key not in elems:
                    elems[key]=(R2,D2); nf.append((R2,D2))
        frontier=nf
        if len(elems)>200: return None
    return list(elems.values())

Pz, Px = perm(Rz), perm(Rx)
found=[]
for sz in itertools.product([1,-1],repeat=8):
    Dz = np.diag(sz)@Pz
    if not np.array_equal(np.linalg.matrix_power(Dz,4), -np.eye(8,dtype=int)): continue
    for sx in itertools.product([1,-1],repeat=8):
        Dx = np.diag(sx)@Px
        if not np.array_equal(np.linalg.matrix_power(Dx,4), -np.eye(8,dtype=int)): continue
        G = gen_group([(Rz,Dz),(Rx,Dx)])
        if G is None: continue
        if len(G)!=48: continue
        # check it is a projective lift: each R appears with D and -D
        found.append((sz,sx,G))
print("sign choices with D^4=-1 generating a 48-element group:",len(found))
# classify up to diagonal gauge S (D->S D S) : compute characters (trace of each element) as invariant
def chars(G):
    return tuple(sorted((tuple(R.flatten()),int(np.trace(D))) for R,D in G))
classes={}
for sz,sx,G in found:
    classes.setdefault(chars(G),[]).append((sz,sx,G))
print("distinct character tables:",len(classes))
for ch,lst in classes.items():
    print(" class size",len(lst))
if len(sys.argv)>2:
    want=(tuple(int(t) for t in sys.argv[2].split(',')),tuple(int(t) for t in sys.argv[3].split(',')))
    sz,sx,G=[f for f in found if (tuple(f[0]),tuple(f[1]))==want][0]
else:
    sz,sx,G = found[0]
print("using sz=",sz," sx=",sx)
# character of the 8-dim rep for info
tr = sorted(set((int(round(np.trace(R))),int(np.trace(D))) for R,D in G))
print("(tr R, tr D) pairs:",tr)

# Check genuine rep: map R->{D,-D}
from collections import defaultdict
lift=defaultdict(list)
for R,D in G: lift[R.tobytes()].append(D)
assert len(lift)==24 and all(len(v)==2 and np.array_equal(v[0],-v[1]) for v in lift.values())

# allowed entries
allowed=[]  # (n, vout, vin)
for n in offs:
    for vo in corners:
        for vi in corners:
            d = np.array(vo)-np.array(vi)-2*np.array(n)
            if np.all(np.abs(d)<=1): allowed.append((n,vo,vi))
print("allowed entries:",len(allowed))

# Linear covariance constraints on the 216 complex unknowns x[(n,vo,vi)]
idx={a:i for i,a in enumerate(allowed)}
N=len(allowed)
rows=[]
# A_{Rn}[a,b] = sum D[a,a'] A_n[a',b'] D[b,b']   (D real orthogonal so D^dagger = D^T)
for R,D in G:
    for n in offs:
        Rn = tuple((R@np.array(n)).tolist())
        for a in range(8):
            for b in range(8):
                row=[0]*N
                key=(Rn,corners[a],corners[b])
                lhs_allowed = key in idx
                if lhs_allowed: row[idx[key]]+=1
                for ap in range(8):
                    for bp in range(8):
                        c = D[a,ap]*D[b,bp]
                        if c==0: continue
                        k2=(n,corners[ap],corners[bp])
                        if k2 in idx: row[idx[k2]]-=c
                if any(row): rows.append(row)
M = sp.Matrix(rows)
ns = M.nullspace()
print("free complex parameters after covariance:",len(ns))
# make nice basis: rref of nullspace
B = sp.Matrix.hstack(*ns).T.rref()[0]
basis=[B.row(i) for i in range(B.rows)]
P=len(basis)
c = sp.symbols('c1:%d'%(P+1)); cb = sp.symbols('cb1:%d'%(P+1))
def Amat(n, conj=False):
    A = sp.zeros(8,8)
    for (nn,vo,vi),i in idx.items():
        if nn!=n: continue
        A[cidx[vo],cidx[vi]] = sum(basis[j][i]*(cb[j] if conj else c[j]) for j in range(P))
    return A
A = {n:Amat(n) for n in offs}
Ab = {n:Amat(n,True) for n in offs}
for n in offs:
    print(n, "nonzero entries:", sum(1 for e in A[n] if e!=0), "params:", sorted(set(str(s) for e in A[n] for s in e.free_symbols)))
# unitarity: sum_n A_n^dagger A_{n+m} = delta_{m0} I ; A_n^dagger = Ab_n^T
eqs=set()
for m in itertools.product(range(-2,3),repeat=3):
    S=sp.zeros(8,8)
    for n in offs:
        n2=tuple(a+b for a,b in zip(n,m))
        if n2 in A:
            S += Ab[n].T*A[n2]
    if m==(0,0,0): S -= sp.eye(8)
    for e in S:
        e=sp.expand(e)
        if e!=0: eqs.add(e)
eqs=sorted(eqs,key=str)
print("distinct unitarity polys:",len(eqs))
json.dump({'P':P,'eqs':[str(e) for e in eqs],
           'A':{str(n):[[str(A[n][i,j]) for j in range(8)] for i in range(8)] for n in offs},
           'sz':list(map(int,sz)),'sx':list(map(int,sx))}, open(sys.argv[1] if len(sys.argv)>1 else 'model.json','w'))
