"""T108 - IS THE RECORD WEIGHT AUTOMATICALLY A PROBABILITY ON THE COMPLEX?
The Bridge memo (.claude/science/physics-loops/AXIOM_MEMO_20260822.md) proposes
one probabilistic postulate:

   "the normalized slice-Gram weight of a class equals the limiting relative
    frequency of its record"

and records four closed doors -- additivity/Gleason, stationarity, the stationary
law mu*, counting -- all of which attack the EQUALITY from the probability side.
Its mu* door is the sharp one: the unique stationary law exists but "is NOT a
law: signed off-region, positive only on a bounded disconnected box, and
UNDEFINED at the zero-shear class."

That is a statement about mu* on the RIGID-LATTICE carrier.  This campaign built
a different arena, and the weight side can be asked there:

   is the framework's record weight -- the trace-normalised diagonal of
   herm(Q^-1) -- automatically POSITIVE and NORMALISED on the complex?

If it is positive by construction there, then on this arena the weight side of
the bridge is a genuine probability with no axiom needed, and what the axiom must
assert shrinks to the equality with frequency alone.  If it goes signed here too,
that is the mu* pathology reproduced on a second carrier, which is a much
stronger statement than one carrier can give."""
import numpy as np, itertools
def cubical(L,d,gfun=None,m=0.8):
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    W=[]
    for k in range(d+1):
        w=np.zeros(len(cells[k]))
        for (s,S),i in cidx[k].items():
            g=np.ones(d) if gfun is None else gfun(s)
            vol=float(np.prod(np.sqrt(g)))
            w[i]=vol/np.prod([g[a] for a in S]) if S else vol
        W.append(w)
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])))
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sg=(-1)**pos
                D[j,cidx[k][(s,T)]]+=-sg; D[j,cidx[k][(shift(s,a),T)]]+=sg
        Ds.append(np.diag(np.sqrt(W[k+1]))@D@np.diag(1.0/np.sqrt(W[k])))
    dims=[len(c) for c in cells]; N=sum(dims); off=[0]
    for x in dims: off.append(off[-1]+x)
    Df=np.zeros((N,N))
    for k in range(d):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
    Q=m*np.eye(N)+Df
    return Q,dims
def record_weight(Q):
    """the framework's W9 object: trace-normalised diagonal of herm(Q^-1)"""
    Gi=np.linalg.inv(Q)
    H=0.5*(Gi+Gi.T)
    dg=np.diag(H)
    return dg/np.sum(dg), H
print("T108c  MAPPING THE POSITIVITY REGION of the record weight in m")
print("       (as m -> infinity, Q^-1 -> (1/m) I, which is positive, so any")
print("        negativity must live in an intermediate BAND -- the memo's")
print("        'bounded box' shape, on a second carrier)")
print()
ms=[0.02,0.1,0.3,0.6,1.0,1.5,2.0,3.0,5.0,10.0,30.0,100.0]
print(f"   {'d':>2} {'L':>2} " + "".join(f"{m:>8g}" for m in ms))
for d,L in ((2,4),(2,6),(3,3),(3,4)):
    row=f"   {d:2d} {L:2d} "
    for m in ms:
        Q,dims=cubical(L,d,gfun=None,m=m)
        w,H=record_weight(Q)
        n=int(np.sum(w<0))
        row+=f"{('.' if n==0 else str(n)):>8}"
    print(row, flush=True)
print()
print("   '.' = all weights positive;  a number = how many are negative.")
print("   A band of negativity with positivity on BOTH sides is the memo's mu*")
print("   pathology reproduced on this campaign's carrier: the record weight is a")
print("   probability only in a region, not structurally.")
print()
for d,L in ((2,6),(3,3)):
    Q,dims=cubical(L,d,gfun=None,m=1.0)
    ev=np.linalg.eigvalsh(Q-np.eye(Q.shape[0]))
    print(f"   d={d} L={L}: spec(D) spans [{ev.min():.4f},{ev.max():.4f}];  Q is PSD only for m > {abs(ev.min()):.4f}")
