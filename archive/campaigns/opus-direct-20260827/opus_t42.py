"""T42 - GEOMETRY IN THE COMPLEX, AND THE REFINEMENT GATE.
Result 22 closed the metric-field-on-a-rigid-lattice class and said where to go:
put the geometry in the CELLS, where the framework already puts it, and replace
the diffeomorphism gate with a refinement/reparametrisation gate.  This is that.

The complex: a periodic chain of L cells with INDEPENDENT lengths l_x summing to
a fixed total T.  The geometry is the list of lengths -- there is no metric field
and no fixed coordinate step.  Fields live at cell centres, the inner product is
   <phi, psi> = sum_x l_x phi_x psi_x
and the skew-adjoint derivative with respect to THAT inner product is

     (D psi)_x = (1 / l_x) * (1/2) (psi_(x+1) - psi_(x-1))

(skew is immediate: <phi, D psi> = (1/2) sum_x phi_x (psi_(x+1) - psi_(x-1)),
which is manifestly antisymmetric under relabelling -- the cell volume cancels).
That is the discrete form of  (1/sqrt(g)) d , i.e. d/d(proper length).
Operator:  Q = m + gamma D,  gamma = eps + iota on the exterior algebra of R^1.

THE GATE.  A flat interval of total length T chopped UNIFORMLY, versus the SAME
interval chopped NON-UNIFORMLY, is exactly the coordinate change that broke every
construction in Results 19-22.  If the cell construction is reparametrisation
covariant, the two must agree on physics:
   (a) the low-lying spectrum must converge to the same continuum values
       lambda = m +- i 2 pi n / T, for both choppings;
   (b) the convergence must be to the SAME limit, not merely each to its own."""
import numpy as np
NF=2                      # exterior algebra of R^1: basis (), (0)
EPSm=np.array([[0.,0.],[1.,0.]])          # eps: () -> (0)
IOTm=np.array([[0.,1.],[0.,0.]])          # iota: (0) -> ()
GAM=EPSm+IOTm                              # gamma^2 = I
def Q_of(lengths,m):
    L=len(lengths); Q=np.zeros((L*NF,L*NF))
    for x in range(L):
        i=x*NF
        Q[i:i+NF,i:i+NF]+=m*np.eye(NF)
        for sgn in (+1,-1):
            y=(x+sgn)%L
            Q[i:i+NF,y*NF:y*NF+NF]+= sgn*0.5*(1.0/lengths[x])*GAM
    return Q
def spectrum(lengths,m,k=6):
    ev=np.linalg.eigvals(Q_of(lengths,m))
    ev=sorted(ev,key=lambda z:(abs(z.imag),abs(z.real)))
    return np.array(ev[:2*k])
def chop(L,T,kind,amp=0.6,n=1):
    if kind=="uniform": l=np.ones(L)
    elif kind=="wave":  l=1.0+amp*np.cos(2*np.pi*n*np.arange(L)/L)
    elif kind=="wave2": l=1.0+amp*np.cos(2*np.pi*2*np.arange(L)/L)+0.3*np.sin(2*np.pi*np.arange(L)/L)
    elif kind=="random":
        rng=np.random.default_rng(11); l=1.0+amp*(rng.random(L)-0.5)*2
    l=np.abs(l)+1e-3
    return l*(T/l.sum())
T=2*np.pi; m=0.7
print("T42  cell-complex chain, total length T = 2 pi, m = 0.7")
print("     continuum spectrum: lambda = m +- i n,  n = 0,1,2,...  (since 2 pi n / T = n)")
print()
for kind in ("uniform","wave","wave2","random"):
    print(f"  chopping = {kind}")
    for L in (16,32,64,128,256):
        l=chop(L,T,kind)
        ev=spectrum(l,m,k=4)
        im=sorted({round(abs(z.imag),6) for z in ev})[:4]
        re=sorted({round(z.real,6) for z in ev})
        pred=[0.0,1.0,2.0,3.0]
        err=max(abs(a-b) for a,b in zip(im,pred[:len(im)]))
        print(f"    L={L:4d}  Im(lambda) = {[f'{v:.6f}' for v in im]}   "
              f"Re = {[f'{v:.5f}' for v in re[:3]]}   max|Im - n| = {err:.3e}", flush=True)
    print(flush=True)
print("  READING: if every chopping converges to Im = 0,1,2,3 and Re = m, the cell")
print("  construction is reparametrisation covariant -- the same geometry chopped")
print("  differently gives the same physics.  That is the refinement gate passing.")
