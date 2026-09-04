"""
T257 - the framework's low-energy spectrum, stated as a prediction.

R151: the ordered CP^3 record field breaks SU(4) -> U(3): 15 - 9 = 6 broken
generators.  R161: six soft modes measured.  But Goldstone modes are EXACTLY
massless only if the broken symmetry is EXACT -- an approximate symmetry gives
pseudo-Goldstones with small but non-zero masses.

So the question the packet has never asked: is the Born weight's SU(4) symmetry
exact, or only approximate?  If exact, the framework predicts SIX EXACTLY
MASSLESS SCALARS, which is a hard, falsifiable statement about the world.
"""
import numpy as np
rng = np.random.default_rng(401)

def haar(n):
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    Q,R = np.linalg.qr(A); return Q*(np.diag(R)/np.abs(np.diag(R)))
def st(n):
    z = rng.normal(size=n)+1j*rng.normal(size=n); return z/np.linalg.norm(z)

n = 4
print("=== 1. is the SU(4) symmetry of the Born weight EXACT? ===")
worst = 0.0
for _ in range(20000):
    a, b = st(n), st(n); V = haar(n)
    worst = max(worst, abs(abs(np.vdot(a,b))**2 - abs(np.vdot(V@a, V@b))**2))
print(f"    max |phi(psi,psi') - phi(V psi, V psi')| over 20000 random V: {worst:.2e}")
print(f"    -> exact to machine precision.  No symmetry-breaking term exists in")
print(f"       the weight, because R136 derived its FORM and nothing else is there.")

print("\n=== 2. could anything else give the Goldstones a mass? ===")
print("    (a) an explicit breaking term in the measure  -> none: R136 fixes the")
print("        form to prod phi(v.v') and R148 fixes phi; there is no extra term.")
print("    (b) the U(1) gauge coupling eating one          -> already accounted:")
print("        CP^3 = S^7/U(1), so the phase is quotiented out BEFORE counting.")
print("        dim CP^3 = 6 is the count AFTER the U(1) is removed.")
print("    (c) quantum corrections                         -> Goldstone's theorem")
print("        protects them to all orders while the symmetry is exact.")

print("\n=== 3. the prediction ===")
print(f"    broken generators : dim SU(4) - dim U(3) = {15} - {9} = {15-9}")
print(f"    dim CP^3          : {2*(4-1)}   (agrees)")
print(f"    R161 measured     : 6 soft modes, 9 massive, 11x gap in S")
print("""
    => the framework's low-energy spectrum is
           SIX EXACTLY MASSLESS SCALARS  +  gravity  ( + at most one U(1) )
       and nothing else: no fermions (R163), no non-abelian gauge (R170),
       and its only particle is a Planck-scale boson (R164/R165).

    This is a HARD prediction, not a gap.  Exactly massless scalars mediate
    unscreened long-range forces.  Six of them are not observed.""")
