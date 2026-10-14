"""BLEAK-1 identity checks (PREREG Method 4 and the U^alpha extraction)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from b1_core import shat, chalf, vertex, U_alpha, kernel_parts

rng = np.random.default_rng(20261014)
n = 400

print("== (i) K2 Ward identity: shat_mu(p1+p2) V_mn(p1,p2) = -1/2[G^-1(p1) s_n(p2) c_n(p1) + G^-1(p2) s_n(p1) c_n(p2)] ==")
for m2 in (0.0, 0.3):
    p1 = rng.uniform(-np.pi, np.pi, (4, n)); p2 = rng.uniform(-np.pi, np.pi, (4, n))
    k = p1 + p2
    for d2 in (False, True):
        V = vertex(p1, p2, m2, d2)
        lhs = np.einsum('mn,mvn->vn', shat(k), V)
        Gi1 = np.sum(shat(p1) ** 2, 0) + m2; Gi2 = np.sum(shat(p2) ** 2, 0) + m2
        rhs = -0.5 * (Gi1 * shat(p2) * chalf(p1) + Gi2 * shat(p1) * chalf(p2))
        print("  m2=%.1f %s: max |lhs-rhs| = %.2e   (max|lhs| = %.2f)" % (m2, "D2" if d2 else "K2", np.abs(lhs - rhs).max(), np.abs(lhs).max()))
print("  -> K2 exact off shell (Ward residual ~1e-15); D2 violates it by O(1) at lattice momenta (the dim-6 term).")

print("\n== (ii) D_fol = W_TT + W_inst equals D_GR on lattice-conserved sources (R19-33's 1.8e-12) ==")
k = rng.uniform(-np.pi, np.pi, (4, n)); s = shat(k)
def conserved(s):
    X = rng.normal(size=(4, 4, s.shape[1])); X = X + X.transpose(1, 0, 2)
    S2 = np.sum(s * s, 0)
    Pt = np.eye(4)[:, :, None] - s[:, None, :] * s[None, :, :] / S2
    return np.einsum('abn,bcn,cdn->adn', Pt, X, Pt)
J1, J2 = conserved(s), conserved(s)
WTT, Wi, WGR = kernel_parts(J1, J2, k)
print("  bilinear, both conserved: max rel |WTT+Winst-WGR| = %.2e" % (np.abs(WTT + Wi - WGR) / np.abs(WGR).max()).max())
X = rng.normal(size=(4, 4, n)); X = X + X.transpose(1, 0, 2)
WTT, Wi, WGR = kernel_parts(J1, X, k)
print("  one conserved, one generic: max |WTT+Winst-WGR| / max|WGR| = %.2e   (not an identity)" % (np.abs(WTT + Wi - WGR).max() / np.abs(WGR).max()))

print("\n== (iii) U^alpha = d/dp1_alpha V(p1,k)|_{p1=0} (m=0) vs central finite difference; D2 extra term has zero derivative ==")
k = rng.uniform(-np.pi, np.pi, (4, n)); eps = 1e-6
for alpha in range(4):
    e = np.zeros((4, 1)); e[alpha] = eps
    for d2 in (False, True):
        fd = (vertex(np.zeros((4, n)) + e, k, 0.0, d2) - vertex(np.zeros((4, n)) - e, k, 0.0, d2)) / (2 * eps)
        print("  alpha=%d %s: max |U - FD| = %.2e" % (alpha, "D2" if d2 else "K2", np.abs(U_alpha(k, alpha) - fd).max()))
print("  V(0,k) at m=0: max |V| = %.1e (K2), %.1e (D2)" % (np.abs(vertex(np.zeros((4, n)), k)).max(), np.abs(vertex(np.zeros((4, n)), k, 0.0, True)).max()))
print("  U^alpha(-k) = -U^alpha(k): max dev %.1e" % max(np.abs(U_alpha(-k, a) + U_alpha(k, a)).max() for a in range(4)))
print("  divergence of U^alpha: shat_mu U^a_mn = -1/2 G^-1(k) delta_an c_n(k)? max dev %.1e" %
      max(np.abs(np.einsum('mn,mvn->vn', shat(k), U_alpha(k, a)) + 0.5 * np.sum(shat(k) ** 2, 0) * np.eye(4)[a][:, None] * chalf(k)).max() for a in range(4)))

print("\n== (iv) symmetry of the integrands f_alpha(k) = D_k(U^a,U^a)/shat^2 ==")
def f(k, a, which):
    U = U_alpha(k, a); WTT, Wi, WGR = kernel_parts(U, U, k); S2 = np.sum(shat(k) ** 2, 0)
    return {'GR': WGR, 'fol': WTT + Wi, 'TT': WTT, 'inst': Wi}[which] / S2
for which in ('GR', 'fol'):
    devs = []
    for mu in range(4):
        kr = k.copy(); kr[mu] *= -1
        devs.append(max(np.abs(f(kr, a, which) - f(k, a, which)).max() / np.abs(f(k, a, which)).max() for a in range(4)))
    sw = k[[3, 1, 2, 0]]
    d14 = np.abs(f(sw, 3, which) - f(k, 0, which)).max() / np.abs(f(k, 0, which)).max()
    sw23 = k[[0, 2, 1, 3]]
    d23 = np.abs(f(sw23, 2, which) - f(k, 1, which)).max() / np.abs(f(k, 1, which)).max()
    print("  %-3s: reflection k_mu->-k_mu max rel dev %s ; 1<->4 swap (f_4(Pk) vs f_1(k)) %.1e ; 2<->3 swap %.1e" % (which, ["%.0e" % d for d in devs], d14, d23))
print("  -> integrands even in each k_mu (so [0,pi]^4 suffices); D_GR integrand W(B4)-covariant; D_fol only W(B3)xZ2^T.")
