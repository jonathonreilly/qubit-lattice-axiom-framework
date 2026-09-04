"""T99 - THE CHIRAL ANOMALY: does the index follow the flux?
Two of this campaign's results collide productively.  Result 25/30: the operator
has an index theorem -- the chirality G = (-1)^degree gives Str = chi, and the
kernel carries the Betti numbers.  Result 40: the framework carries a U(1) gauge
field whose flux is quantised.  Put them together and there is a prediction:

    in two dimensions the index of the Dirac operator in a U(1) background is
    EXACTLY the flux quantum number  (Atiyah-Singer).

That is the chiral anomaly, and it is the sharpest physical statement available
from what this campaign has built -- a number the framework must produce, not a
structure it may admit.

Measured: the kernel of D_A on a 2-torus at each flux, split by chirality, and
        index = n_+ - n_-
against the flux quantum number n."""
import numpy as np, itertools
def build(L,n):
    d=2
    def U(s,a):
        if a==1: return np.exp(2j*np.pi*n*s[0]/L)
        return np.exp(-2j*np.pi*n*s[1]) if s[0]==L-1 else 1.0+0j
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
        D=np.zeros((len(cells[k+1]),len(cells[k])),dtype=complex)
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sg=(-1)**pos
                D[j,cidx[k][(s,T)]]      += -sg
                D[j,cidx[k][(shift(s,a),T)]] += sg*U(s,a)
        Ds.append(D)
    dims=[len(c) for c in cells]; N=sum(dims); off=[0]
    for x in dims: off.append(off[-1]+x)
    Df=np.zeros((N,N),dtype=complex); G=np.zeros(N)
    for k in range(d+1): G[off[k]:off[k+1]]=(-1)**k
    for k in range(d):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].conj().T
    return Df,G,dims
print("T99  index of the framework's operator vs U(1) flux, on a 2-torus")
print("     prediction (Atiyah-Singer in d=2): index = flux quantum number n")
print(f"   {'L':>3} {'n':>4} {'kernel dim':>11} {'n_+':>5} {'n_-':>5} {'index':>7} {'predicted':>10}")
for L in (4,6):
    for n in range(0,5):
        Df,G,dims=build(L,n)
        ev,U_=np.linalg.eigh(Df)
        ker=np.abs(ev)<1e-8
        gexp=np.einsum("ij,i,ij->j",U_.conj(),G,U_).real
        npos=float(np.sum(np.clip(gexp[ker],0,None)))
        nneg=float(-np.sum(np.clip(gexp[ker],None,0)))
        idx=npos-nneg
        print(f"   {L:3d} {n:4d} {int(ker.sum()):11d} {npos:5.1f} {nneg:5.1f} {idx:7.2f} {n:10d}",
              flush=True)
    print()
print("   index tracking n would be the chiral anomaly, reproduced by the framework.")
print("   index stuck at the flux-free value means the lattice operator does not")
print("   carry the anomaly -- which is the known difficulty with naive lattice")
print("   fermions, and would be an honest negative rather than a surprise.")
