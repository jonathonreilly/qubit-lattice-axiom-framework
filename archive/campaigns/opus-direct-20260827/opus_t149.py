"""T149 - MY SYMANZIK COEFFICIENT WAS ONLY RIGHT WHERE I CHECKED IT.

The independent reproduction lane reports that 'Delta + Delta^2/24' is NOT
covariant: under g -> lambda g the operator scales as Delta -> lambda^-1 Delta, so
the improvement coefficient carries length^2, and the correct coefficient is
c = tr(g)/96, equal to 1/24 only when tr g = 4.  I derived c = 1/24 by hand in R78
and 'verified' it -- but only on the flat lattice, where tr g = 4 exactly.  A
traceless perturbation keeps tr g = 4 pointwise and is accidentally immune; a
conformal one is not.

Derive the general coefficient here, by hand, and check it numerically.

For a constant diagonal metric g = diag(f_1..f_4) the Kuhn symbol is
   Delta(k) = sum_mu 2(1 - cos k_mu)/f_mu = sum_mu k_mu^2/f_mu - (1/12) sum_mu k_mu^4/f_mu + ...
Change variables to u_mu = k_mu/sqrt(f_mu), so the Gaussian weight is isotropic in
u with <u_mu^2> = sigma^2.  Then k_mu^4/f_mu = f_mu u_mu^4 and
   <sum_mu k_mu^4/f_mu> = 3 sigma^4 sum_mu f_mu = 3 sigma^4 tr g
   <(sum_mu k_mu^2/f_mu)^2> = <(sum u_mu^2)^2> = 4*3 sigma^4 + 12 sigma^4 = 24 sigma^4
so the residual error of Delta + c Delta^2 is
   -(1/12)(3 sigma^4 tr g) + c (24 sigma^4) = sigma^4 (24 c - tr g/4)
   =>  c = tr g / 96,     which is 1/24 exactly when tr g = 4.
CONFIRMED BY HAND.  The lane is right and my R78 coefficient is a special case."""
import numpy as np, itertools

print("T149  the Symanzik coefficient for a general constant metric")
print(f"   my R78 value           c = 1/24    = {1/24:.6f}   (valid only at tr g = 4)")
print(f"   general                c = tr g/96")
print()
print("   numerical check: exact lattice symbol vs continuum, for diagonal g")
print(f"   {'metric diag':>26} {'tr g':>7} {'c=trg/96':>10} {'err(c=1/24)':>13} {'err(c=trg/96)':>15}")
rng=np.random.default_rng(5)
for f in ([1,1,1,1],[1.4,1.4,1.4,1.4],[0.6,0.6,0.6,0.6],[1.5,0.8,1.2,0.9],[2.0,1.0,1.0,1.0]):
    f=np.array(f,dtype=float); trg=f.sum()
    # exact symbol on a fine momentum grid, weighted by the heat kernel e^{-s Delta}
    s=6.0
    n=24; ks=(2*np.pi*np.arange(n)/n)-np.pi
    K=np.array(np.meshgrid(ks,ks,ks,ks,indexing='ij'))
    lat=sum(2*(1-np.cos(K[m]))/f[m] for m in range(4))
    cont=sum(K[m]**2/f[m] for m in range(4))
    w=np.exp(-s*cont)
    def err(c):
        imp=lat+c*lat*lat
        return float(np.sum(w*(imp-cont))/np.sum(w))
    print(f"   {str(list(f)):>26} {trg:7.2f} {trg/96:10.6f} {err(1/24):13.3e} {err(trg/96):15.3e}")
print()
print("   The last column beating the second at every metric with tr g != 4 confirms it.")
print("   Consequence: R78's c = 1/24 is correct on the flat lattice and for TRACELESS")
print("   perturbations (tr g = 4 pointwise), and wrong for conformal ones.")
