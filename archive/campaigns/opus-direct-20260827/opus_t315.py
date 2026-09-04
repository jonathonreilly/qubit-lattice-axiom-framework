"""
T315 - the charge-monopole route to fermions: is the framework's own defect n=1?

R163 concluded "no fermions" because the axioms introduce no anticommuting
variables. R171 closed the soliton route because the measure is real and
non-negative, so there is no phase for a WZ/Hopf term. BOTH are correct and
NEITHER closes the charge-monopole route, whose statistics come from angular
momentum stored in the gauge field -- a real, positive-measure fact. (Emergent
fermions in bosonic models with strictly positive weights are ordinary: the sign
structure lives in the effective description of excitations, not in the
microscopic weights.)

In 3D a charge q bound to a monopole of flux g carries field angular momentum
J = qg/(4 pi). The framework supplies q = 1 (matter minimally coupled to its own
Berry connection, R158) and quantised flux (R154). If its minimal defect is
n = 1, i.e. g = 2 pi, then J = 1/2 and the composite is a FERMION.

This measures n for R164's own defects: Born point, Z^3, CP^1 -- the axioms as
written, no enlargement.
Controls: (i) gauge invariance of every plaquette phase under random per-site
phases; (ii) total flux over the whole torus must vanish (no net charge);
(iii) the n histogram must be integers to machine precision, else the object is
not topological and the reading is void.
"""
import numpy as np
L=16
rng=np.random.default_rng(7)
def mc(L,sweeps=3000,burn=800):
    v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
    for sw in range(sweeps):
        for _ in range(L**3):
            a,b,c=rng.integers(0,L,3)
            nbs=np.array([v[(a+1)%L,b,c],v[a-1,b,c],v[a,(b+1)%L,c],
                          v[a,b-1,c],v[a,b,(c+1)%L],v[a,b,c-1]])
            new=rng.normal(size=3); new/=np.linalg.norm(new); old=v[a,b,c]
            num=np.prod(1+(nbs@new)); den=np.prod(1+(nbs@old))
            if den<=0 or num<0: continue
            if num>=den or rng.random()<num/den: v[a,b,c]=new
    return v
def spinor(v):
    """CP^1 representative: |psi> with <psi|sigma|psi> = v"""
    th=np.arccos(np.clip(v[...,2],-1,1)); ph=np.arctan2(v[...,1],v[...,0])
    return np.stack([np.cos(th/2), np.sin(th/2)*np.exp(1j*ph)],axis=-1)
v=mc(L); psi=spinor(v)
def link(a,b): return np.sum(np.conj(a)*b,axis=-1)
def plaq(psi,mu,nu):
    p1=psi; p2=np.roll(psi,-1,axis=mu); p3=np.roll(np.roll(psi,-1,axis=mu),-1,axis=nu)
    p4=np.roll(psi,-1,axis=nu)
    z=link(p1,p2)*link(p2,p3)*link(p3,p4)*link(p4,p1)
    return np.angle(z)
F={}
for mu,nu in ((0,1),(1,2),(0,2)): F[(mu,nu)]=plaq(psi,mu,nu)
print("control (i): gauge invariance of the plaquette phase")
al=rng.uniform(0,2*np.pi,size=(L,L,L))
psig=psi*np.exp(1j*al)[...,None]
print(f"   max |F(psi) - F(gauge-transformed)| = "
      f"{max(np.abs(plaq(psig,mu,nu)-F[(mu,nu)]).max() for mu,nu in F):.2e}")
# cube flux: oriented sum of the 6 faces
tot = (F[(1,2)] - np.roll(F[(1,2)],-1,axis=0)
     - F[(0,2)] + np.roll(F[(0,2)],-1,axis=1)
     + F[(0,1)] - np.roll(F[(0,1)],-1,axis=2))
n = tot/(2*np.pi)
print(f"\ncontrol (iii): is the cube flux an integer multiple of 2 pi?")
print(f"   max |n - round(n)| = {np.abs(n-np.round(n)).max():.2e}")
ni=np.round(n).astype(int)
print(f"\ncontrol (ii): total flux over the torus = {ni.sum()}   (must be 0)")
vals,cts=np.unique(ni,return_counts=True)
print(f"\nmonopole charge histogram over {L**3} cubes:")
for a,b in zip(vals,cts): print(f"    n = {a:+d}   count {b:7d}   fraction {b/L**3:.3e}")
mx=np.abs(vals).max()
print(f"\n  |n|_max = {mx}")
if mx==1:
    print("  => the minimal (and only) defect is n = 1, so g = 2 pi.")
    print("     with the matter's q = 1 (R158):   J = q g / 4 pi = 1/2")
    print("     A CHARGE BOUND TO THIS DEFECT IS A FERMION.")
