"""T43b - the matter-coupled refinement gate, with the mode pairing done right.
T43's route (2) paired eigenvalues with np.sort_complex, which orders by real
part first; every eigenvalue here has real part near m, so the ordering scrambled
and the reported gaps came out as near-integers -- i.e. it was comparing mode n
against mode m, a sorting artefact, not physics.  Pair by ENERGY instead: sort
|Im(lambda)| ascending, compare element by element, and report Re separately.

Same physical system, four choppings of the same interval, matter a function of
PROPER position.  If the cell construction is reparametrisation covariant the
energies must agree between choppings and converge together as L grows."""
import numpy as np
NF=2
EPSm=np.array([[0.,0.],[1.,0.]]); IOTm=np.array([[0.,1.],[0.,0.]]); GAM=EPSm+IOTm
def centres(l):
    e=np.concatenate([[0.0],np.cumsum(l)]); return e[:-1]+l/2
def Q_of(l,mv):
    L=len(l); Q=np.zeros((L*NF,L*NF))
    for x in range(L):
        i=x*NF; Q[i:i+NF,i:i+NF]+=mv[x]*np.eye(NF)
        for sgn in (+1,-1):
            y=(x+sgn)%L; Q[i:i+NF,y*NF:y*NF+NF]+=sgn*0.5*(1.0/l[x])*GAM
    return Q
def chop(L,T,kind,amp=0.6):
    if kind=="uniform": l=np.ones(L)
    elif kind=="wave":  l=1.0+amp*np.cos(2*np.pi*np.arange(L)/L)
    elif kind=="wave3": l=1.0+amp*np.cos(2*np.pi*3*np.arange(L)/L)
    elif kind=="ramp":  l=1.0+amp*(np.arange(L)/L-0.5)*2
    l=np.abs(l); return l*(T/l.sum())
T=2*np.pi
def energies(l,mfun,k=6):
    ev=np.linalg.eigvals(Q_of(l,[mfun(c) for c in centres(l)]))
    im=np.sort(np.abs(ev.imag)); re=np.sort(ev.real)
    return im[:2*k], re
for label,mfun in (("FREE  m(s) = 0.7", lambda s: 0.7),
                   ("MATTER m(s) = 0.7 + 0.45 cos(s)", lambda s: 0.7+0.45*np.cos(s))):
    print(f"=== {label}")
    print(f"   {'L':>5}  {'chopping':>9}  {'energies |Im| (lowest 6 distinct)':<52} {'max gap vs uniform':>19}")
    for L in (32,64,128,256,512):
        base,_=energies(chop(L,T,"uniform"),mfun)
        def show(v):
            out=[]
            for z in v:
                if not out or abs(z-out[-1])>1e-6: out.append(z)
            return out[:6]
        print(f"   {L:5d}  {'uniform':>9}  {str([f'{z:.6f}' for z in show(base)]):<52} {'--':>19}")
        for kind in ("wave","wave3","ramp"):
            e,_=energies(chop(L,T,kind),mfun)
            gap=float(np.max(np.abs(e-base)))
            print(f"   {L:5d}  {kind:>9}  {str([f'{z:.6f}' for z in show(e)]):<52} {gap:19.4e}", flush=True)
        print(flush=True)
print("READING: gaps falling like 1/L^2 across ALL choppings = the same geometry")
print("chopped differently gives the same physics = the refinement gate passes,")
print("with matter.  This is the test the rigid-lattice construction failed by 54%.")
