"""T27 - THE FIELD EQUATION IN THE SECTOR THE SELECTOR LEAVES OPEN.
T26 found dW/dh != 0 even for uniform matter under a CONFORMAL bump.  That is
correct and expected: a conformal bump changes the cell volume, and the volume
is exactly what the selector V^2 = det g FIXES.  So the physical variation is
the one that preserves det g -- the TRACELESS (shear) part.  At first order a
traceless perturbation  g = flat + h f_s E,  tr E = 0,  leaves det g unchanged.
Prediction if this is gravity:
  (a) uniform matter          -> dW/dh = 0   (flat vacuum is a solution)
  (b) ISOTROPIC point defect  -> dW/dh = 0   (no preferred axis to shear along)
  (c) ANISOTROPIC matter      -> dW/dh != 0, tracking the anisotropy
That is the traceless Einstein equation's signature: shear is sourced by
anisotropic stress, not by energy density."""
import numpy as np
D=2; BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}; NF=4
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
def build(L, m_site, prof, h, E):
    sites=[(t,x) for t in range(L) for x in range(L)]; sid={s:i for i,s in enumerate(sites)}
    Q=np.zeros((NF*len(sites),)*2)
    for s in sites: Q[sid[s]*NF:(sid[s]+1)*NF, sid[s]*NF:(sid[s]+1)*NF]+=m_site[s]*np.eye(NF)
    def gam(s,a):
        g=np.eye(D)+h*prof[s]*E
        return EPS[a]+iota(a, np.linalg.inv(g))
    for s in sites:
        for a in range(D):
            for sgn,r in ((+1,((s[0]+(a==0))%L,(s[1]+(a==1))%L)),(-1,((s[0]-(a==0))%L,(s[1]-(a==1))%L))):
                Q[sid[s]*NF:(sid[s]+1)*NF, sid[r]*NF:(sid[r]+1)*NF]+=0.25*sgn*(gam(s,a)+gam(r,a))
    return Q
def dW(L, m_site, prof, E, e=1e-5):
    return (np.linalg.slogdet(build(L,m_site,prof,e,E))[1]
          - np.linalg.slogdet(build(L,m_site,prof,-e,E))[1])/(2*e)
L=6; m0=0.8; zc=(3,3)
sites=[(t,x) for t in range(L) for x in range(L)]
prof_pt={s:(1.0 if s==zc else 0.0) for s in sites}
prof_g={}
for s in sites:
    dt=min((s[0]-zc[0])%L,(zc[0]-s[0])%L); dx=min((s[1]-zc[1])%L,(zc[1]-s[1])%L)
    prof_g[s]=float(np.exp(-(dt*dt+dx*dx)/(2*1.2**2)))
E_diag=np.array([[1.,0.],[0.,-1.]]); E_off=np.array([[0.,1.],[1.,0.]])
E_conf=np.eye(2)
def matter(kind, delta):
    m={s:m0 for s in sites}
    if kind=="uniform": pass
    elif kind=="point":  m[zc]+=delta
    elif kind=="t-pair": m[(2,3)]+=delta; m[(4,3)]+=delta          # stretched along t
    elif kind=="x-pair": m[(3,2)]+=delta; m[(3,4)]+=delta          # stretched along x
    elif kind=="t-line":
        for t in range(L): m[(t,3)]+=delta                          # a worldline along t
    elif kind=="x-line":
        for x in range(L): m[(3,x)]+=delta
    return m
print("T27  L=6 m0=0.8   dW/dh for a VOLUME-PRESERVING (traceless) metric perturbation")
print("     E = diag(1,-1)  [shear], profile = point bump at (3,3), delta = 0.3")
print()
for kind in ("uniform","point","t-pair","x-pair","t-line","x-line"):
    m=matter(kind,0.3)
    a=dW(L,m,prof_pt,E_diag); b=dW(L,m,prof_pt,E_off); c=dW(L,m,prof_pt,E_conf)
    print(f"   matter={kind:8s}  d/dh[E=diag(1,-1)]={a:+.6e}   d/dh[E=offdiag]={b:+.6e}"
          f"   d/dh[E=conformal]={c:+.6e}", flush=True)
print()
print("     linearity of the shear response in the matter anisotropy (t-pair minus x-pair):")
for delta in (0.05,0.1,0.2,0.4):
    at=dW(L,matter("t-pair",delta),prof_pt,E_diag); ax=dW(L,matter("x-pair",delta),prof_pt,E_diag)
    print(f"   delta={delta:<5}  t-pair={at:+.6e}  x-pair={ax:+.6e}  anisotropy={at-ax:+.6e}"
          f"  /delta={(at-ax)/delta:+.6f}", flush=True)
print()
print("     same with a SMOOTH (Gaussian) metric profile:")
for kind in ("uniform","point","t-pair","x-pair"):
    m=matter(kind,0.3)
    print(f"   matter={kind:8s}  d/dh[E=diag(1,-1)]={dW(L,m,prof_g,E_diag):+.6e}", flush=True)
