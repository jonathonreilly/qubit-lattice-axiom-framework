"""T144 - the realizability threshold as a THEOREM, not a sample.

T143c measured p = 0 (95% bound 5.1e-6) up to q = 0.40 a^2 and first failures at
q = 0.45.  But 'p below my resolution' is not 'p = 0', and in a universe of 10^180
cells even p = 1e-6 means 10^174 non-geometric regions.  The question deserves an
exact answer, and it has one.

A simplex is realizable iff its Gram matrix G is positive definite.  On the flat
Kuhn lattice every simplex has some minimum Gram eigenvalue lam_min > 0.
Perturbing every squared edge length by at most eps changes G by
   |dG_ab| = |(1/2)(dl^2_{0a} + dl^2_{0b} - dl^2_{ab})| <= (3/2) eps
so ||dG||_2 <= ||dG||_F <= 4 (3/2) eps = 6 eps.  By Weyl, every eigenvalue moves
by at most 6 eps, so realizability is GUARANTEED whenever

        6 eps < lam_min      i.e., with eps = q/2 from grid snapping,   q < lam_min/3.

That is a sufficient condition holding for EVERY configuration, not almost all --
no sampling, no resolution floor.  Compute lam_min and compare to l_P^2."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t143b import prep, bad_fraction, IDX
l2,IJ,NT=prep(3)
M=l2[IJ].copy(); M[:,IDX,IDX]=0.0
G=0.5*(M[:,0:1,1:]+M[:,1:,0:1]-M[:,1:,1:])
w=np.linalg.eigvalsh(0.5*(G+np.transpose(G,(0,2,1))))
lmin=float(w[:,0].min())
print(f"T144  exact realizability bound")
print(f"   flat Kuhn lattice, {NT} simplices")
print(f"   minimum Gram eigenvalue over all simplices: lam_min = {lmin:.6f} a^2")
print(f"   distinct minimum eigenvalues present: {sorted(set(np.round(w[:,0],9)))[:6]}")
print()
print(f"   GUARANTEED realizable for every configuration when q < lam_min/3 = {lmin/3:.4f} a^2")
print(f"      -> length quantum  l_0 < {np.sqrt(lmin/3):.4f} a")
print(f"   measured first failures (T143c, sampling)        q ~ 0.45 a^2,  l_0 ~ 0.67 a")
print(f"   Planck quantum (R73)                             q = 0.195-0.265 a^2,  l_0 = 0.442-0.515 a")
print()
safe = lmin/3
for nm,q in (("l_P^2 spectral   ",0.195),("l_P^2 mode-count ",0.265)):
    print(f"   {nm}  q = {q:.3f} a^2   {'GUARANTEED SAFE' if q<safe else 'not covered by the exact bound'}"
          f"   (margin q*/q = {safe/q:.2f}x)")
print()
print("   The exact bound is conservative -- Weyl assumes the worst-case alignment of")
print("   the perturbation, while snapping errors are independent across edges.  It")
print("   brackets the sampled threshold from below, which is exactly what it should do.")
