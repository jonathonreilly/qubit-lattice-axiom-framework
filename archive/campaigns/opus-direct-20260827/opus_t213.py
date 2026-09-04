"""
T213 - the same statement on the CONTINUOUS Bloch sphere, removing any
dependence on the finite menu used in T210-T212.

Records are null (R98) => the possibility domain is S^2.  An isotropic edge
potential is phi(v.v').  The single-site normaliser for two neighbours is
    Z(b,c) = int_{S^2} phi(v.b) phi(v.c) dOmega(v).
Legendre-expanding phi(t) = sum_l c_l P_l(t) and using the addition theorem
    int P_l(v.b) P_m(v.c) dOmega = delta_lm (4 pi/(2l+1)) P_l(b.c)
gives   Z(b,c) = sum_l c_l^2 (4 pi/(2l+1)) P_l(b.c),
so Z is CONSTANT iff c_l = 0 for every l >= 1, i.e. iff phi is constant --
no coupling.  Verified below by quadrature, not asserted.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

# Lebedev-free: product Gauss-Legendre in cos(theta) x uniform in phi is exact
# for band-limited integrands, which these are.
NT, NP = 64, 128
ct, wt = leggauss(NT)
ph = 2*np.pi*np.arange(NP)/NP
V = np.array([[np.sqrt(1-c*c)*np.cos(p), np.sqrt(1-c*c)*np.sin(p), c]
              for c in ct for p in ph])
W = np.array([w*(2*np.pi/NP) for w in wt for _ in ph])
print(f"quadrature: {len(V)} nodes, total weight {W.sum():.12f} (want {4*np.pi:.12f})")

def Zspread(phi, ngrid=12):
    """max-min of Z(b,c) = int phi(v.b) phi(v.c) over a grid of (b,c) pairs."""
    cs = np.linspace(-1, 1, ngrid)
    b = np.array([0.0, 0.0, 1.0])
    Zs = []
    for t in cs:
        c = np.array([np.sqrt(max(0, 1-t*t)), 0.0, t])
        Zs.append(np.sum(W*phi(V@b)*phi(V@c)))
    Zs = np.array(Zs)
    return Zs.max()-Zs.min(), Zs

print("\n  phi(t)                         spread(Z)      constant?")
cases = [("1                       ", lambda t: np.ones_like(t)),
         ("1 + 0.3 t               ", lambda t: 1+0.3*t),
         ("1 + 0.3 t  (lam=0.3)    ", lambda t: 1+0.3*t),
         ("1 + 0.05 t              ", lambda t: 1+0.05*t),
         ("1 + 0.3 t + 0.1 t^2     ", lambda t: 1+0.3*t+0.1*t*t),
         ("exp(0.3 t)              ", lambda t: np.exp(0.3*t))]
for name, f in cases:
    sp, _ = Zspread(f)
    print(f"  {name}  {sp:12.6e}   {'YES' if sp < 1e-12 else 'no'}")

print("\n=== the predicted law:  spread(Z) from the l>=1 Legendre content ===")
for lam in (0.05, 0.1, 0.2, 0.4):
    sp, _ = Zspread(lambda t, L=lam: 1+L*t)
    # c_1 = lam/3 in the P_l basis -> Z = 4pi[1 + (lam^2/3) P_1(b.c)/1]... check scaling
    print(f"  phi = 1 + {lam:4.2f} t :  spread(Z) = {sp:.6e}   "
          f"spread/lam^2 = {sp/lam**2:.6f}")
print("  constant ratio => spread(Z) is exactly O(lam^2), vanishing only at lam=0.")

print("\n=== so, on the full sphere: ===")
print("  Record consistency forces a product-over-edges rule;")
print("  convex-consistency forces its normaliser constant;")
print("  the normaliser is constant iff phi has no l>=1 content, i.e. no coupling.")
print("  => the two premises are jointly satisfiable ONLY by the trivial rule.")
