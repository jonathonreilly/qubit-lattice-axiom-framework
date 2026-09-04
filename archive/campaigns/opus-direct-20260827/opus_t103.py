"""T103 - REFLECTION POSITIVITY ON THE COMPLEX: does the framework have a quantum theory?
Everything this campaign has built is spectra and actions.  What makes a
Euclidean theory a QUANTUM one -- a Hilbert space of states and a positive
self-adjoint transfer operator e^{-H} -- is Osterwalder-Schrader reflection
positivity.  This campaign tried it once, in Result 22, and it failed: no
candidate reflection made the form positive on either branch.  But that attempt
was on the RIGID LATTICE, the arena that subsequently failed at everything else
(Results 19-22), and the exterior algebra was attached per-site rather than
living on the complex.

Redo it on the arena that works: the CUBICAL COCHAIN complex of Results 33-47.
The reflection theta about a time slice maps a k-cell to its mirror image, with
a sign from how many of its directions are temporal.  The OS form on fields
supported at positive times must be positive semidefinite.

  PSD  -> the framework has a Hilbert space and a positive transfer operator:
          a quantum theory, on the arena that carries gravity and matter.
  not  -> and the failure is now arena-independent, which is a much stronger
          negative than Result 22's."""
import numpy as np, itertools
d=3          # 1 time + 2 space, small enough to be exact
L=4
sites=list(itertools.product(range(L),repeat=d))
cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
for s in sites:
    for k in range(d+1):
        for S in itertools.combinations(range(d),k):
            cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
def shift(s,a):
    t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
Ds=[]
for k in range(d):
    D=np.zeros((len(cells[k+1]),len(cells[k])))
    for (s,S),j in cidx[k+1].items():
        for pos,a in enumerate(S):
            T=tuple(x for x in S if x!=a); sg=(-1)**pos
            D[j,cidx[k][(s,T)]]+=-sg; D[j,cidx[k][(shift(s,a),T)]]+=sg
    Ds.append(D)
dims=[len(c) for c in cells]; N=sum(dims); off=[0]
for x in dims: off.append(off[-1]+x)
D=np.zeros((N,N))
for k in range(d):
    D[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
    D[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
m=0.7
G=np.linalg.inv(m*np.eye(N)+D)          # the propagator
print(f"T103  cubical cochain complex, d={d}, L={L}: {N} cells, mass {m}")
# global index of a cell
def gidx(s,S): return off[len(S)]+cidx[len(S)][(s,S)]
# reflection about the t=0 slice: t -> -t.  A cell (s,S) maps to (s',S) with
# s' the mirrored base point; cells whose S contains the time direction 0 pick up
# a sign, and their base point shifts because the cell spans [t, t+1].
def reflect(s,S):
    t=s[0]
    if 0 in S: tp=(-t-1)%L
    else:      tp=(-t)%L
    sp=(tp,)+s[1:]
    sgn=-1.0 if 0 in S else 1.0
    return sp,S,sgn
pos=[(s,S) for s in sites for k in range(d+1) for S in itertools.combinations(range(d),k)
     if 1<=s[0]<=L//2-1]
print(f"     {len(pos)} cells at strictly positive times")
M=np.zeros((len(pos),len(pos)))
for A,(s,S) in enumerate(pos):
    sp,Sp,sg=reflect(s,S)
    for B,(s2,S2) in enumerate(pos):
        M[A,B]=sg*G[gidx(sp,Sp),gidx(s2,S2)]
Msym=0.5*(M+M.T)
ev=np.linalg.eigvalsh(Msym)
print(f"     OS form: hermitian to {np.max(np.abs(M-M.T)):.2e}")
print(f"     eigenvalues: min {ev.min():+.6f}  max {ev.max():+.6f}")
print(f"     negative eigenvalues: {int(np.sum(ev<-1e-9))} of {len(ev)}")
print(f"     REFLECTION POSITIVE: {bool(np.all(ev>-1e-9))}")
print()
print("   also trying the reflection WITHOUT the temporal sign, as a control:")
M2=np.zeros((len(pos),len(pos)))
for A,(s,S) in enumerate(pos):
    sp,Sp,sg=reflect(s,S)
    for B,(s2,S2) in enumerate(pos):
        M2[A,B]=G[gidx(sp,Sp),gidx(s2,S2)]
ev2=np.linalg.eigvalsh(0.5*(M2+M2.T))
print(f"     negative eigenvalues: {int(np.sum(ev2<-1e-9))} of {len(ev2)}   "
      f"PSD: {bool(np.all(ev2>-1e-9))}")
