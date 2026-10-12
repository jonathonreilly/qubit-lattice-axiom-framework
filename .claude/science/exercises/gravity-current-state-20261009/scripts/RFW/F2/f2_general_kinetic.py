"""F2 (lane RFW), part 3: (a) forward on-shell stress lemma; (b) the 1-jet system for other
local scalar kinetic terms (matter range R = 1..3, two-step, non-separable plaquette term).

(a) LEMMA (from the O(kappa) identity alone): at k1 = p on shell, k2 = -p - Q, Q -> 0, the
    identity  E(k1)L(Q,k2)+E(k2)L(Q,k1) = 1/2 sum_ordered dh_mn(Q) T_mn(k1,k2)  gives at O(Q)
    (n.Q)(i xi.f(p)) = i sum_mn Q_m xi_n T0_mn,  n = grad E(p), so  T0_mn = n_m f_n  for ANY local
    symmetric stress T paired with pseudo-translation symbol i f (f = lambda n for symmetry).
    Checked here exactly for K2's T: T0_mn = 2 sin p_m sin p_n (n = 2 sin p, f = sin p).
(b) For a local kinetic symbol A(k) with f = grad A / 2 (the K2-type choice; exact local
    Lie-derivative and symmetric T exist by K2's Killing-cokernel corollary), the jet system is
      sum_mu t_mu M_mu^T WT0 = i (t . grad f_c(p)) WT0,  WT0 = W*(n (x) f),  t.n = 0,
    after (Z) forces A0 = 0 (checked: the T0(p) span C^10).  Unknowns M_mu[:,a] (40 per a).
"""
import numpy as np
from f2_common import *

rng = np.random.default_rng(99)
c_dir = 0

# ---------------------------------------------------------------- (a) forward-stress lemma check
worst = 0.0
for m2 in (0.0, 0.5, 2.0):
    for _ in range(50):
        p = shell_point(rng, m2, True)
        T0 = T_lat_cross(p, -p, m2)
        pred = np.array([2 * np.sin(p[m]) * np.sin(p[n]) for (m, n) in COMPS])
        worst = max(worst, np.abs(T0 - pred).max() / np.abs(pred).max())
print(f"(a) K2 stress on shell, forward: max rel |T0_mn - 2 sin p_m sin p_n| = {worst:.2e}")
# off shell it is NOT of that form (control)
p = rng.normal(size=4) + 0.3j * rng.normal(size=4)
T0 = T_lat_cross(p, -p, 1.0)
pred = np.array([2 * np.sin(p[m]) * np.sin(p[n]) for (m, n) in COMPS])
print(f"    control off shell: rel deviation = {np.abs(T0 - pred).max() / np.abs(pred).max():.2e}")


# ---------------------------------------------------------------- (b) kinetic families
def sep_family(coef):
    """A(k) = sum_mu sum_n coef[n] (2 - 2 cos n k_mu) + m2 (separable, range max n)."""
    def A(k, m2):
        return sum(c * np.sum(2 - 2 * np.cos(n * k), axis=-1) for n, c in coef.items()) + m2

    def solve3(k, m2):
        # a(k3) = -(sum_{j<3} a(k_j) + m2); a(k) = sum c_n (2 - 2 T_n(x)), x = cos k
        tgt = -(sum(c * np.sum(2 - 2 * np.cos(n * k[:3])) for n, c in coef.items()) + m2)
        N = max(coef)
        poly = np.zeros(N + 1, dtype=complex)       # in Chebyshev basis -> power basis
        cheb = np.zeros(N + 1, dtype=complex)
        cheb[0] = sum(2 * c for c in coef.values()) - tgt
        for n, c in coef.items():
            cheb[n] += -2 * c
        poly = np.polynomial.chebyshev.cheb2poly(cheb)
        roots = np.roots(poly[::-1])
        x = roots[rng.integers(len(roots))]
        return np.arccos(x + 0j) * rng.choice([-1, 1])
    return A, solve3


def plaq_family(beta):
    def A(k, m2):
        s = 2 - 2 * np.cos(k)
        return np.sum(s) + beta / 4 * sum(s[i] * s[j] for i in range(4) for j in range(i + 1, 4)) + m2

    def solve3(k, m2):
        s = 2 - 2 * np.cos(k[:3])
        lin = 1 + beta / 4 * np.sum(s)
        const = np.sum(s) + beta / 4 * (s[0] * s[1] + s[0] * s[2] + s[1] * s[2]) + m2
        s3 = -const / lin
        return np.arccos(1 - s3 / 2 + 0j) * rng.choice([-1, 1])
    return A, solve3


def cont_family():
    def A(k, m2):
        return np.sum(k * k) + m2

    def solve3(k, m2):
        return np.sqrt(-(np.sum(k[:3] ** 2) + m2) + 0j) * rng.choice([-1, 1])
    return A, solve3


def grad(A, k, m2, eps=1e-4):
    g = np.zeros(4, dtype=complex)
    for mu in range(4):
        e = np.zeros(4); e[mu] = eps
        g[mu] = (-A(k + 2 * e, m2) + 8 * A(k + e, m2) - 8 * A(k - e, m2) + A(k - 2 * e, m2)) / (12 * eps)
    return g


def hess(A, k, m2, eps=1e-3):
    H = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        e = np.zeros(4); e[mu] = eps
        H[:, mu] = (-grad(A, k + 2 * e, m2) + 8 * grad(A, k + e, m2) - 8 * grad(A, k - e, m2)
                    + grad(A, k - 2 * e, m2)) / (12 * eps)
    return H


def jet_residual(fam, m2, npts=160):
    A, solve3 = fam
    rows = [[] for _ in range(NC)]; rhs = [[] for _ in range(NC)]
    T0s = []
    for _ in range(npts):
        k = rng.normal(size=4) * 0.9 + 0.35j * rng.normal(size=4)
        k[3] = solve3(k, m2)
        assert abs(A(k, m2)) < 1e-8 * (1 + abs(m2)), A(k, m2)
        n = grad(A, k, m2); f = n / 2
        Hf = hess(A, k, m2) / 2                      # d f_nu / d k_mu
        T0 = W * np.array([n[m] * f[nn] for (m, nn) in COMPS])
        T0s.append(T0)
        sc = 1 / np.linalg.norm(T0)
        for t in tangent_basis(n, rng):
            g = Hf[c_dir, :] @ t
            for a in range(NC):
                r = np.zeros(40, dtype=complex)
                for mu in range(4):
                    r[10 * mu: 10 * mu + 10] = t[mu] * T0
                rows[a].append(r * sc); rhs[a].append(1j * g * T0[a] * sc)
    span = np.linalg.matrix_rank(np.array(T0s), tol=1e-8 * np.abs(np.array(T0s)).max())
    num = den = 0.0
    for a in range(NC):
        G, b = np.array(rows[a]), np.array(rhs[a])
        u, *_ = np.linalg.lstsq(G, b, rcond=None)
        num += np.linalg.norm(G @ u - b) ** 2; den += np.linalg.norm(b) ** 2
    return np.sqrt(num / den), span


print("\n(b) 1-jet residual of the O(kappa^2) translation-Killing condition (any field-dependent completion)")
fams = [
    ("continuum / SLAC symbols  A = k^2 + m^2", cont_family()),
    ("K2 nearest neighbour (R=1)", sep_family({1: 1.0})),
    ("improved O(a^4) (R=2)", sep_family({1: 4 / 3, 2: -1 / 12})),
    ("improved O(a^6) (R=3)", sep_family({1: 3 / 2, 2: -3 / 20, 3: 1 / 90})),
    ("two-step sin^2 k (R=2, doubled)", sep_family({2: 1 / 4})),
    ("non-separable plaquette beta=0.5 (R=1)", plaq_family(0.5)),
]
for name, fam in fams:
    out = []
    for m2 in (0.25, 1.0):
        res, span = jet_residual(fam, m2)
        out.append(f"m2={m2}: residual={res:.3e} (span T0 = {span}/10)")
    print(f"  {name:42s} " + "   ".join(out), flush=True)
