"""T164 - THE BORN FORM AS LIGHT-CONE GEOMETRY, AND WHY IT PICKS A FRAME.

The repo scorecard's Root A is the readout/Born price: why the Born FORM.  R98
supplies new geometry to attack it with -- pure states are NULL VECTORS on the
light cone of the site's own Minkowski structure.  So ask what the Born
probability IS geometrically, and whether Lorentz invariance forces it.

Two pure states rho = (1/2)(I + n.sigma), rho' = (1/2)(I + n'.sigma) have
   Tr(rho rho') = (1/2)(1 + n.n')  = |<psi|phi>|^2
and as 4-vectors p = (1/2, n/2), q = (1/2, n'/2) the MINKOWSKI product is
   p.q = t t' - v.v' = (1/4)(1 - n.n')
so   |<psi|phi>|^2 = 1 - 2 (p.q).   The Born weight is AFFINE in the Minkowski
inner product of the two null vectors.

The tempting next step is: 'Lorentz invariance then forces the Born form'.  TEST
THAT, because it looks too easy.  Lorentz acts transitively on pairs of distinct
null RAYS, so there is NO nonconstant Lorentz-invariant function of two pure
states -- which would mean invariance forces nothing, and instead that the Born
rule DEPENDS on a frame.

The frame is not mysterious if so: normalisation Tr rho = 1 fixes t = 1/2, i.e.
picks a time slice, exactly as R93 found when normalisation froze the trace
channel.  Then the prediction is sharp and falsifiable:
   * on the t = 1/2 slice, Tr(rho rho') = 1 - 2 p.q exactly;
   * a BOOST changes Tr(rho rho') for the same pair of null RAYS, because it
     moves them off the slice and renormalising is not a Lorentz operation;
   * a ROTATION does not.
If the boost column moves and the rotation column does not, then PROBABILITY
SELECTS A REST FRAME -- a structural statement about Root A."""
import numpy as np
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
def pure(n): 
    n=np.array(n,dtype=float); n/=np.linalg.norm(n)
    return 0.5*(I2+sum(n[i]*S[i] for i in range(3)))
def tv(r): return np.trace(r).real/2, np.array([np.trace(r@S[i]).real/2 for i in range(3)])
def mink(p,q): return p[0]*q[0]-p[1]@q[1]
def boost(th,i): return np.cosh(th/2)*I2+np.sinh(th/2)*S[i]
def rot(th,i):   return np.cos(th/2)*I2-1j*np.sin(th/2)*S[i]
print("T164  the Born weight as light-cone geometry")
print()
rng=np.random.default_rng(12)
w=0.0
for _ in range(3000):
    a=pure(rng.normal(size=3)); b=pure(rng.normal(size=3))
    born=np.trace(a@b).real
    w=max(w,abs(born-(1-2*mink(tv(a),tv(b)))))
print(f"(1) |Tr(rho rho') - (1 - 2 p.q)| over 3000 random pure pairs: max {w:.2e}")
print()
print("(2) is there a nonconstant Lorentz-invariant function of two null RAYS?")
print("    Lorentz acts transitively on such pairs, so any invariant is constant.")
print("    Test: boost two null rays and compare their Minkowski product AFTER")
print("    renormalising each back to t = 1/2 (which is what a state requires).")
a=pure([1,0,0]); b=pure([0.3,0.9,0.2])
print("    %7s %22s %21s" % ("theta","BOOST: Tr(rho rho')","ROT: Tr(rho rho')"))
for th in (0.0,0.4,0.9,1.6):
    B=boost(th,2); ra=B@a@B.conj().T; rb=B@b@B.conj().T
    ra=ra/np.trace(ra).real; rb=rb/np.trace(rb).real          # renormalise: back to the slice
    R=rot(th,2); qa=R@a@R.conj().T; qb=R@b@R.conj().T
    print(f"    {th:7.2f} {np.trace(ra@rb).real:22.8f} {np.trace(qa@qb).real:21.8f}")
print(f"    at theta=0 the value is {np.trace(a@b).real:.8f}  (both columns must start here)")
print()
print("(3) the raw Minkowski product of the boosted rays, WITHOUT renormalising:")
for th in (0.0,0.4,0.9,1.6):
    B=boost(th,2); ra=B@a@B.conj().T; rb=B@b@B.conj().T
    print(f"    theta={th:5.2f}   p.q = {mink(tv(ra),tv(rb)):.8f}   "
          f"t_a = {tv(ra)[0]:.5f}, t_b = {tv(rb)[0]:.5f}")
print()
print("   If the boost column in (2) MOVES while the rotation column does not, the")
print("   Born weight is not boost invariant, and normalisation -- Tr rho = 1, the")
print("   same condition that froze the trace channel in R93 -- SELECTS A REST FRAME.")
