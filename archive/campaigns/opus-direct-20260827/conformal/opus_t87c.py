"""T87 - A CLOSED LOOP: does the operator's vacuum energy set the size of the universe?
Two of this campaign's own results can be joined:
  * Result 31: the Regge field equation with a cosmological term SELECTS a size,
      s* = sqrt( K / (2 Lambda V1) ),  verified to ten digits.
  * Result 32's leftover: the operator's spectral action has a VOLUME term --
      dW = -24.0 * dVol with R^2 = 0.946 -- an INDUCED cosmological constant.
If the operator supplies Lambda and the field equation converts Lambda into a
size, the chain closes: the matter operator would set the scale of the geometry.

The honest question is whether that induced Lambda is a framework NUMBER or a
mesh artefact.  Result 32 established that the CURVATURE term is UV-obstructed;
the volume term is the leading term and may be better behaved.  Measure it:
  (a) at several lattice sizes -- does the coefficient per unit volume converge?
  (b) at several masses -- does it depend on m the way a vacuum energy should?
  (c) with an IR-safe spectral action versus the full one -- does the answer
      depend on which, as the curvature term did?"""
import numpy as np, itertools
def fem_cubical(L,scale,m,d=4,nmodes=40,full=False):
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    g=np.array([scale]*d)**2
    W=[]
    for k in range(d+1):
        w=np.zeros(len(cells[k]))
        vol=float(np.prod(np.sqrt(g)))
        for (s,S),i in cidx[k].items():
            w[i]=vol/np.prod([g[a] for a in S]) if S else vol
        W.append(w)
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])))
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sgn=(-1)**pos
                D[j,cidx[k][(s,T)]]+=-sgn; D[j,cidx[k][(shift(s,a),T)]]+=sgn
        Ds.append(np.diag(np.sqrt(W[k+1]))@D@np.diag(1.0/np.sqrt(W[k])))
    dims=[len(c) for c in cells]; N=sum(dims); off=[0]
    for k in range(d+1): off.append(off[-1]+dims[k])
    Df=np.zeros((N,N))
    for k in range(d):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
    ev=np.abs(np.linalg.eigvalsh(Df))
    ev=np.sort(ev)
    totvol=float(np.sum(W[0]))
    if full:  W_=float(np.sum(np.log(ev+m)))
    else:     W_=float(np.sum(np.log(ev[:nmodes]+m)))
    return W_, totvol
print("T87c  the m -> 0 limit of the induced cosmological term.")
print("      A vacuum energy set by the FIELD would vanish with the field's mass.")
print("      A finite nonzero limit means it is set by the CUTOFF instead -- which")
print("      is precisely the cosmological constant problem, appearing here.")
print()
print(f"   {'m':>7} {'L=3':>13} {'L=4':>13}")
for m in (2.0,1.0,0.5,0.25,0.1,0.03,0.01):
    row=[]
    for L in (3,4):
        e=2e-3
        Wp,Vp=fem_cubical(L,1.0+e,m,full=True)
        Wm,Vm=fem_cubical(L,1.0-e,m,full=True)
        row.append(((Wp-Wm)/(2*e))/((Vp-Vm)/(2*e)))
    print(f"   {m:7.3f} {row[0]:13.6f} {row[1]:13.6f}", flush=True)
print()
print("   value flattening to a nonzero constant as m -> 0  =>  cutoff-dominated:")
print("   the framework reproduces the cosmological constant problem rather than")
print("   solving it.  Value going to zero  =>  the vacuum energy is set by matter.")
