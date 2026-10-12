"""F2 (lane RFW), part 5: also let the O(kappa) data move within the same nearest-neighbour
scalar action: dressed pseudo-translation f_nu = lambda(p) * 2 sin p_nu (lambda an even local
trig polynomial normalised ON SHELL at the rest point p* = (0,0,0,iE_m): lambda(p*) = 1/2, so
f ~ p in the IR of the shell [first version normalised at p = 0 off shell; its only solution was
lambda = 0 on the whole shell (f a trivial symmetry): see f2_dressed_inspect.out]; the symmetric stress then exists by
K2's corollary and its forward value is T0 = n (x) f = lambda n (x) n by the forward lemma).
The 1-jet condition  sum_mu t_mu M_mu^T W(n(x)n) = i (t.grad f_c) W(n(x)n)  is LINEAR in
(M, beta) where lambda = 1/2 + sum_j beta_j (g_j - g_j(0)).  Joint least squares over all 10
components (beta shared)."""
import numpy as np, itertools
from f2_common import *

rng = np.random.default_rng(314)
c_dir = 0
# basis of even local functions g_j(p) (value, gradient)
def basis(p):
    c, s = np.cos(p), np.sin(p)
    out = []
    for mu in range(4):                                   # cos p_mu
        g = np.zeros(4, complex); g[mu] = -s[mu]; out.append((c[mu] - 1, g))
    for mu in range(4):                                   # cos 2 p_mu
        g = np.zeros(4, complex); g[mu] = -2 * np.sin(2 * p[mu]); out.append((np.cos(2 * p[mu]) - 1, g))
    for mu, nu in itertools.combinations(range(4), 2):    # cos p_mu cos p_nu
        g = np.zeros(4, complex); g[mu] = -s[mu] * c[nu]; g[nu] = -c[mu] * s[nu]
        out.append((c[mu] * c[nu] - 1, g))
    for trip in itertools.combinations(range(4), 3):      # triple products
        val = np.prod(c[list(trip)]); g = np.zeros(4, complex)
        for mu in trip:
            g[mu] = -s[mu] * np.prod([c[x] for x in trip if x != mu])
        out.append((val - 1, g))
    val = np.prod(c); g = np.array([-s[mu] * np.prod([c[x] for x in range(4) if x != mu]) for mu in range(4)])
    out.append((val - 1, g))
    return out

def rest_point(m2):
    return np.array([0, 0, 0, 1j * np.arccosh(1 + m2 / 2)])


def run(m2, npts=250, use_beta=True, ref=None):
    nb = len(basis(np.zeros(4)))
    pref = np.zeros(4, complex) if ref is None else ref
    gref = np.array([val for (val, gr) in basis(pref)])
    nM = 400
    rows, rhs = [], []
    for _ in range(npts):
        p = shell_point(rng, m2, True)
        n = 2 * np.sin(p)
        dn_c = np.zeros(4, complex); dn_c[c_dir] = 2 * np.cos(p[c_dir])     # grad n_c
        N0 = W * np.array([n[m] * n[k] for (m, k) in COMPS])
        sc = 1 / np.linalg.norm(N0)
        B = basis(p)
        for t in tangent_basis(n, rng):
            # t.grad f_c = (t.grad lambda) n_c + lambda (t.dn_c),  lambda = 1/2 + sum beta_j (g_j - g_j(0))
            const = 0.5 * (t @ dn_c)
            coefs = np.array([(gr @ t) * n[c_dir] + (val - gv) * (t @ dn_c) for (val, gr), gv in zip(B, gref)])
            for a in range(NC):
                r = np.zeros(nM + nb, complex)
                for mu in range(4):
                    r[a * 40 + 10 * mu: a * 40 + 10 * mu + 10] = t[mu] * N0
                if use_beta:
                    r[nM:] = -1j * coefs * N0[a]
                rows.append(r * sc); rhs.append(1j * const * N0[a] * sc)
    G, b = np.array(rows), np.array(rhs)
    if not use_beta:
        G = G[:, :nM]
    u, _, rank, _ = np.linalg.lstsq(G, b, rcond=None)
    lam_vals = None
    if use_beta:
        beta = u[nM:]
        lam_vals = []
        for _ in range(200):
            p = shell_point(rng, m2, True)
            lam_vals.append(0.5 + sum(bv * (val - gv) for bv, (val, gr), gv in zip(beta, basis(p), gref)))
        lam_vals = np.abs(np.array(lam_vals))
    return np.linalg.norm(G @ u - b) / np.linalg.norm(b), rank, G.shape[1], lam_vals

print("== NN scalar, dressed pseudo-translation f = lambda(p) grad A ==")
for m2 in (0.25, 1.0):
    r0, k0, n0, _ = run(m2, use_beta=False)
    r1, k1, n1, l1 = run(m2, use_beta=True)
    r2, k2, n2, l2 = run(m2, use_beta=True, ref=rest_point(m2))
    print(f"m2={m2}: lambda = 1/2 (K2): residual {r0:.3e} (rank {k0}/{n0})")
    print(f"        lambda(0)=1/2 off shell (19-dim even basis): residual {r1:.3e}; |lambda| on shell: "
          f"max {l1.max():.1e}  -> degenerate (f = 0 on shell, trivial translation)")
    print(f"        lambda(p*)=1/2 on shell (rest point):       residual {r2:.3e}; |lambda| on shell: "
          f"min {l2.min():.2f} max {l2.max():.2f}")
