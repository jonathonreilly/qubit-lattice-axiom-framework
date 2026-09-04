"""T176 - THE HARMONIC CAP: how large can the distribution's mean be at each l_max?

This is the computation R109 named as the highest-value open item.  R108 showed
the DIPOLE-ONLY family caps the distribution's mean at |v| <= 1/6, and R109 showed
that cap forces alpha <= 1/3 -- exactly R99's CP optimum.  But R103 showed the
axioms permit l=2 and beyond.  So: does the cap rise once higher harmonics are
allowed, and by how much?

If the cap rises above 1/3, the alpha = 1/3 coincidence loses its second footing
and is CP alone.  If it stays at 1/3, alpha = 1/3 gains real support.

THE COMPUTATION.  A density on S^2 band-limited to degree L is a polynomial of
degree <= L in the components of n.  Maximise the mean
        |v| = (1/2) | integral n f(n) dOmega |
subject to   f >= 0 pointwise   and   integral f dOmega = 1.
That is a linear program: linear objective, linear equality, and one nonnegativity
constraint per grid direction.  Solve it for L = 1..6 and watch the cap.

KNOWN ANCHORS that make this checkable rather than trusted:
   L = 1  must give exactly 1/6 = 0.16667   (R108, derived by hand)
   L -> infinity must approach 1/2          (a point mass, a pure record)
If the solver reproduces both, the intermediate values are trustworthy."""
import numpy as np, itertools
from scipy.optimize import linprog
def sphere_grid(n):
    # near-uniform Fibonacci sphere
    i=np.arange(n)+0.5
    phi=np.arccos(1-2*i/n); th=np.pi*(1+5**0.5)*i
    return np.stack([np.cos(th)*np.sin(phi),np.sin(th)*np.sin(phi),np.cos(phi)],axis=1)
def monomials(L):
    out=[]
    for tot in range(L+1):
        for a in range(tot+1):
            for b in range(tot-a+1):
                out.append((a,b,tot-a-b))
    return out
G=sphere_grid(4000); W=4*np.pi/len(G)     # equal-weight quadrature
print("T176  maximum distribution mean vs harmonic degree L")
print(f"      grid: {len(G)} directions, equal weights")
print()
print(f"   {'L':>3} {'#basis':>7} {'max |v|':>11} {'vs 1/6':>9} {'vs 1/2':>9} {'implied alpha cap':>19}")
prev=None
for L in range(1,7):
    M=monomials(L)
    A=np.array([[np.prod(g**np.array(m)) for m in M] for g in G])   # (grid, basis)
    norm=W*A.sum(axis=0)                       # integral of each basis function
    obj=-0.5*W*(A*G[:,2:3]).sum(axis=0)        # maximise (1/2)*int n_z f
    res=linprog(c=obj,A_ub=-A,b_ub=np.zeros(len(G)),
                A_eq=norm.reshape(1,-1),b_eq=[1.0],
                bounds=[(None,None)]*len(M),method='highs')
    if not res.success:
        print(f"   {L:3d}  solver failed: {res.message}"); continue
    v=-res.fun
    print(f"   {L:3d} {len(M):7d} {v:11.6f} {v/(1/6):9.3f} {v/0.5:9.3f} {v/0.5:19.4f}")
    prev=v
print()
print("   ANCHORS")
print(f"      L=1 must be 1/6 = {1/6:.6f}")
print(f"      L->inf must approach 1/2 = {0.5:.6f}  (point mass)")
print()
print("   the implied alpha cap is (max|v|)/(|V|/6) with |V|=3 for six aligned")
print("   records, i.e. (max|v|)/0.5.  R99's CP optimum is alpha = 1/3 = 0.3333.")
