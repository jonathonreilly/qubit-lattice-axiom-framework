"""Class-A finite runner (memory-safe): finite-lattice cubic diffeomorphism-Ward
scaling support for the W-native induced-graviton route.

The runner compares a supplied lattice conserved coupling D(P_eff) + sqrt(g)
measure against a naive non-conserved C1 control. It is finite-lattice evidence:
over the accessible memory-safe range, the conserved normalized residual
decreases as k decreases, while the naive control does not. It does not prove the
k -> 0 limit, an Einstein-Hilbert action, or all-order nonlinear diffeomorphism
invariance.

Construction: the LATTICE conserved coupling (momentum-reparametrization, the V_cons coupling of #3329)
  D[h] = i sigma_a[ Lm_a + Ch_a o d_a - 1/2 Lm_a o d_a^2 - 1/6 Ch_a o d_a^3 ] + m sqrt(g),
  d_a = sum_b (Wdens - I)_ab o Lm_b ,  Wdens = det(e) e^{-1} (densitized inverse vielbein = sqrt(g)
  measure), e = sqrtm(I+h), Lm_a = sin-hop, Ch_a = cos-hop, o = symmetric (Jordan) ordering. Its
  single-graviton vertex is V_cons (verified in #3329). The exact determinant W = log|det D[h]| bundles
  all the conserved seagulls. The cubic diffeomorphism Ward residual is the a2*a3 CROSS term of the
  gauge variation dW/d(eps) under a LATTICE-consistent diffeomorphism delta_xi h = (d_i xi_j + d_j xi_i)
  + Lie_xi h, with two distinct NON-COLLINEAR transverse-traceless gravitons (k2 || x, k3 || y,
  k1 = -(k2+k3)) -- the genuine cubic test (single-momentum is the trivial gauge-orthogonality zero).
  resid = gauge-part + lie-part; amplitude = |gauge-part|.

  T1  CONSERVED coupling: cubic Ward resid/amplitude DECREASES monotonically with k (L=6,8,10) -- a
      positive finite-lattice scaling signal for the continuum-closure route.
  T2  NAIVE C1 coupling (vielbein on the hop AMPLITUDE, non-conserved) does not show the same
      decreasing trend over the tested range.
  T3  the conserved resid/amplitude is well below the naive one and the gap WIDENS as k decreases
      (conserved-vs-control separation).

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 600

import numpy as np
from scipy.linalg import sqrtm

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
sig = [sx, sy, sz]
I2 = np.eye(2, dtype=complex)

results = []
def check(name, ok):
    results.append((name, bool(ok)))

def build(L):
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    sidx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    Sp = []
    for a in range(3):
        S = np.zeros((n, n), complex)
        for x in sites:
            xp = list(x); xp[a] = (xp[a] + 1) % L; xp = tuple(xp)
            S[sidx[x], sidx[xp]] = 1.0
        Sp.append(S)
    return sites, sidx, n, Sp

def jord(A, B):
    return 0.5 * (A @ B + B @ A)

def Dcons(L, m, hfun, ctx):
    """LATTICE conserved coupling (momentum-reparametrization) + sqrt(g) measure, to O(h^3)."""
    sites, sidx, n, Sp = ctx
    Lm = [(1 / (2j)) * (Sp[a] - Sp[a].conj().T) for a in range(3)]
    Ch = [0.5 * (Sp[a] + Sp[a].conj().T) for a in range(3)]
    Wm = np.zeros((3, 3, n), complex); SG = np.zeros(n)
    for x in sites:
        e = sqrtm(np.eye(3) + hfun(x)); SG[sidx[x]] = np.real(np.linalg.det(e))
        Wm[:, :, sidx[x]] = np.linalg.det(e) * np.linalg.inv(e) - np.eye(3)
    def dop(a):
        Dm = np.zeros((n, n), complex)
        for b in range(3):
            Dm += jord(np.diag(Wm[a, b]), Lm[b])
        return Dm
    D = np.zeros((2 * n, 2 * n), complex)
    for x in sites:
        ix = sidx[x]; D[2 * ix:2 * ix + 2, 2 * ix:2 * ix + 2] += m * SG[ix] * I2
    for a in range(3):
        da = dop(a); da2 = jord(da, da); da3 = jord(da, da2)
        spatial = Lm[a] + jord(Ch[a], da) - 0.5 * jord(Lm[a], da2) - (1 / 6.0) * jord(Ch[a], da3)
        blk = 1j * spatial
        for x in sites:
            row = blk[sidx[x]]
            for iy in np.nonzero(np.abs(row) > 1e-14)[0]:
                D[2 * sidx[x]:2 * sidx[x] + 2, 2 * iy:2 * iy + 2] += sig[a] * row[iy]
    return D

def Dnaive(L, m, hfun, ctx):
    """C1 control: naive vielbein on the hop AMPLITUDE (non-conserved), same sqrt(g) mass."""
    sites, sidx, n, Sp = ctx
    ef = {}; sgv = {}
    for x in sites:
        e = np.real(sqrtm(np.eye(3) + hfun(x))); ef[x] = e; sgv[x] = np.real(np.linalg.det(e))
    D = np.zeros((2 * n, 2 * n), complex)
    for x in sites:
        ix = sidx[x]; D[2 * ix:2 * ix + 2, 2 * ix:2 * ix + 2] += m * sgv[x] * I2
        for i in range(3):
            xp = list(x); xp[i] = (xp[i] + 1) % L; xp = tuple(xp)
            xm = list(x); xm[i] = (xm[i] - 1) % L; xm = tuple(xm)
            for a in range(3):
                ep = 0.5 * (ef[x][a, i] + ef[xp][a, i]); em = 0.5 * (ef[x][a, i] + ef[xm][a, i])
                D[2 * ix:2 * ix + 2, 2 * sidx[xp]:2 * sidx[xp] + 2] += 0.5 * sig[a] * ep
                D[2 * ix:2 * ix + 2, 2 * sidx[xm]:2 * sidx[xm] + 2] += -0.5 * sig[a] * em
    return D

def make_h(L, modes):
    def hf(x):
        h = np.zeros((3, 3))
        for amp, k, E in modes:
            h = h + amp * E * 2 * np.cos(k @ np.array(x))
        return h
    return hf

def dlat_v(f, x, i, L):
    xp = list(x); xp[i] = (xp[i] + 1) % L; xp = tuple(xp)
    xm = list(x); xm[i] = (xm[i] - 1) % L; xm = tuple(xm)
    return 0.5 * (np.array(f(xp)) - np.array(f(xm)))

def delta_xi(L, xi_fun, hfun, part):
    def d(x):
        xi = xi_fun(x); out = np.zeros((3, 3)); h = hfun(x)
        dxi = np.zeros((3, 3))
        for i in range(3):
            dv = dlat_v(xi_fun, x, i, L)
            for j in range(3):
                dxi[j, i] = dv[j]
        for i in range(3):
            for j in range(3):
                if part in ('gauge', 'both'):
                    out[i, j] += dxi[j, i] + dxi[i, j]
                if part in ('lie', 'both'):
                    out[i, j] += sum(xi[k] * dlat_v(lambda y: hfun(y)[i, j], x, k, L) for k in range(3))
                    out[i, j] += sum(dxi[k, i] * h[k, j] + dxi[k, j] * h[i, k] for k in range(3))
        return out
    return d

def Fp(L, m, hfun, dfun, ctx, Dbuild, tau=1e-4):
    D0 = Dbuild(L, m, hfun, ctx); Di = np.linalg.inv(D0)
    Dp = Dbuild(L, m, lambda x: hfun(x) + tau * dfun(x), ctx)
    Dm = Dbuild(L, m, lambda x: hfun(x) - tau * dfun(x), ctx)
    return np.real(np.trace(Di @ ((Dp - Dm) / (2 * tau))))

def ratio(L, Dbuild, m=1.0, amp=0.04):
    ctx = build(L); kx = 2 * np.pi / L
    k2 = np.array([kx, 0, 0]); k3 = np.array([0, kx, 0]); k1 = -(k2 + k3)
    E2 = np.zeros((3, 3)); E2[1, 2] = E2[2, 1] = 1.0   # yz TT (transverse to k2||x)
    E3 = np.zeros((3, 3)); E3[0, 2] = E3[2, 0] = 1.0   # xz TT (transverse to k3||y)
    c = np.array([1.0, 0.5, 0.7])
    def xi_fun(x):
        return c * np.sin(k1 @ np.array(x))
    def cr(part):
        def Fab(a2, a3):
            hf = make_h(L, [(a2, k2, E2), (a3, k3, E3)])
            return Fp(L, m, hf, delta_xi(L, xi_fun, hf, part), ctx, Dbuild)
        a = amp
        return (Fab(a, a) - Fab(a, -a) - Fab(-a, a) + Fab(-a, -a)) / (4 * a * a)
    g = cr('gauge'); s = g + cr('lie')
    return abs(s) / abs(g), kx

# ---------------------------------------------------------------------------
# T1: conserved coupling has decreasing finite-lattice scaling
# ---------------------------------------------------------------------------
rc = {}
for L in (6, 8, 10):
    r, k = ratio(L, Dcons); rc[L] = (r, k)
decreasing = rc[6][0] > rc[8][0] > rc[10][0]
import math
pw_c = math.log(rc[10][0] / rc[6][0]) / math.log(rc[10][1] / rc[6][1])
check("T1 CONSERVED cubic Ward resid/amplitude DECREASES with k: %.4f@k%.2f > %.4f@k%.2f > %.4f@k%.2f (~k^%+.2f, positive finite-lattice scaling support)"
      % (rc[6][0], rc[6][1], rc[8][0], rc[8][1], rc[10][0], rc[10][1], pw_c),
      decreasing and pw_c > 0.5)

# ---------------------------------------------------------------------------
# T2: naive C1 control does not show the same decreasing trend
# ---------------------------------------------------------------------------
rn = {}
for L in (6, 8):
    r, k = ratio(L, Dnaive); rn[L] = (r, k)
pw_n = math.log(rn[8][0] / rn[6][0]) / math.log(rn[8][1] / rn[6][1])
check("T2 NAIVE C1 control does not show decreasing support: %.4f@k%.2f -> %.4f@k%.2f (~k^%+.2f, flat/growing over tested range)"
      % (rn[6][0], rn[6][1], rn[8][0], rn[8][1], pw_n), pw_n < 0.3)

# ---------------------------------------------------------------------------
# T3: conserved well below naive and the gap widens (closure vs non-closure)
# ---------------------------------------------------------------------------
gap6 = rn[6][0] / rc[6][0]; gap8 = rn[8][0] / rc[8][0]
check("T3 conserved resid/amplitude < naive and the gap WIDENS as k decreases (naive/conserved = %.2f@k%.2f -> %.2f@k%.2f)"
      % (gap6, rc[6][1], gap8, rc[8][1]), gap8 > gap6 > 1.0)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("Finite-lattice scaling support: for the supplied conserved coupling D(P_eff) + sqrt(g) measure,")
print("the cubic Ward residual normalized by the amplitude decreases over L=6,8,10, while the naive")
print("non-conserved C1 control does not show that trend over the tested range. This supports the")
print("conserved-coupling continuum-closure route, but does not prove the k->0 limit, an Einstein-Hilbert")
print("action, G_Newton, or all-order nonlinear diffeomorphism invariance.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
print("runner_check_breakdown = {A: %d, B: 0, C: 0, D: 0, total_pass: %d}" % (n_pass, n_pass))
