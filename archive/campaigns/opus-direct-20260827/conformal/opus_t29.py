"""T29 - INDUCED GRAVITY IN 3+1 DIMENSIONS.  The physical-dimension version of T27.
2D has no gravity (the Einstein tensor vanishes identically there), so the T27
structure had to be re-run in d=4 before it means anything.  d=4, L=4, fibre 16,
operator 4096x4096.  Volume-preserving (traceless) metric perturbation
g = I + h f_s E, tr E = 0; response  dW/dh = tr(Q^-1 dQ/dh),  dQ/dh built
analytically from  d(g^-1)/dh = -f_s E.
Predictions if this is gravity:
  uniform matter, isotropic point defect        -> 0
  matter stretched along mu vs along nu, E = diag with +1 at mu, -1 at nu
                                                -> equal and OPPOSITE
  90-degree lattice rotation of the matter      -> the response rotates with it
     (this is a REAL covariance test: 90-degree rotations ARE lattice symmetries)"""
import numpy as np, itertools, time
D=4
BAS=[]
for k in range(D+1): BAS += [tuple(c) for c in itertools.combinations(range(D),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def epsm(a):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        if a in Sx: continue
        T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
    return M
def iota(a,gi):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
    return M
EPS=[epsm(a) for a in range(D)]
L=4; m0=0.9
sites=list(itertools.product(range(L),repeat=D)); sid={s:i for i,s in enumerate(sites)}; NS=len(sites)
print(f"d={D} L={L}: {NS} sites, fibre {NF}, operator {NF*NS}x{NF*NS}", flush=True)
def nb(s,a,sgn):
    t=list(s); t[a]=(t[a]+sgn)%L; return tuple(t)
def Qmat(m_site,prof,h,E):
    Q=np.zeros((NF*NS,NF*NS))
    gi={s:np.linalg.inv(np.eye(D)+h*prof[s]*E) for s in sites}
    IOT={s:[iota(a,gi[s]) for a in range(D)] for s in sites}
    for s in sites:
        i=sid[s]*NF; Q[i:i+NF,i:i+NF]+=m_site[s]*np.eye(NF)
        for a in range(D):
            for sgn in (+1,-1):
                r=nb(s,a,sgn); j=sid[r]*NF
                Q[i:i+NF,j:j+NF]+=0.25*sgn*(2*EPS[a]+IOT[s][a]+IOT[r][a])
    return Q
def dQmat(prof,E):
    dQ=np.zeros((NF*NS,NF*NS)); IE=[iota(a,-E) for a in range(D)]
    for s in sites:
        i=sid[s]*NF
        for a in range(D):
            for sgn in (+1,-1):
                r=nb(s,a,sgn); j=sid[r]*NF
                dQ[i:i+NF,j:j+NF]+=0.25*sgn*(prof[s]+prof[r])*IE[a]
    return dQ
zc=(2,2,2,2)
prof={s:(1.0 if s==zc else 0.0) for s in sites}
def E_mn(mu,nu,off=False):
    E=np.zeros((D,D))
    if off: E[mu,nu]=E[nu,mu]=1.0
    else:   E[mu,mu]=1.0; E[nu,nu]=-1.0
    return E
def pair(mu,delta=0.3):
    m={s:m0 for s in sites}
    a=list(zc); a[mu]=(a[mu]-1)%L; b=list(zc); b[mu]=(b[mu]+1)%L
    m[tuple(a)]+=delta; m[tuple(b)]+=delta
    return m
CFG={"uniform":{s:m0 for s in sites}, "point defect":{**{s:m0 for s in sites}, zc:m0+0.3},
     "pair along t (mu=0)":pair(0), "pair along x (mu=1)":pair(1),
     "pair along y (mu=2)":pair(2), "pair along z (mu=3)":pair(3)}
ES={"E=diag(1,-1,0,0) [t,x]":E_mn(0,1), "E=diag(0,1,-1,0) [x,y]":E_mn(1,2),
    "E=offdiag(x,y)":E_mn(1,2,off=True)}
dQs={nm:dQmat(prof,E) for nm,E in ES.items()}
print()
hdr=f"     {'matter':22s}" + "".join(f"{nm:>26s}" for nm in ES)
print(hdr, flush=True)
for cname,m_ in CFG.items():
    t0=time.time(); Qi=np.linalg.inv(Qmat(m_,prof,0.0,np.zeros((D,D))))
    row=f"     {cname:22s}"
    for nm in ES:
        row += f"{float(np.einsum('ij,ji->',Qi,dQs[nm])):+26.6e}"
    print(row + f"   [{time.time()-t0:.0f}s]", flush=True)
print()
print("   90-degree lattice-rotation covariance (x <-> y is an exact lattice symmetry):")
print("   pair along x with E=diag(0,1,-1,0) must be MINUS pair along y with the same E.")
print()
print("   linearity of the [t,x] anisotropy response:")
for delta in (0.05,0.15,0.3,0.6):
    Qt=np.linalg.inv(Qmat(pair(0,delta),prof,0.0,np.zeros((D,D))))
    Qx=np.linalg.inv(Qmat(pair(1,delta),prof,0.0,np.zeros((D,D))))
    rt=float(np.einsum('ij,ji->',Qt,dQs["E=diag(1,-1,0,0) [t,x]"]))
    rx=float(np.einsum('ij,ji->',Qx,dQs["E=diag(1,-1,0,0) [t,x]"]))
    print(f"     delta={delta:<5} t-pair={rt:+.6e}  x-pair={rx:+.6e}  "
          f"anisotropy={rt-rx:+.6e}  /delta={(rt-rx)/delta:+.6f}", flush=True)
