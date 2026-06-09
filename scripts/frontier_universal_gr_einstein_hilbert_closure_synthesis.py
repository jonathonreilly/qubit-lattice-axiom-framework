"""Class-A finite runner (memory-safe): synthesis diagnostic for the universal-GR Ward lane.

The runner verifies one bounded claim in one place: the supplied conserved
coupling D(P_eff) + sqrt(g) measure gives better finite-lattice Ward diagnostics
than the naive non-conserved control at both cubic and quartic order on L=6,8.

It does not identify the W-native induced graviton with the Einstein-Hilbert
action, prove all-order nonlinear diffeomorphism invariance, or derive G_Newton.

This consolidates the landed chain:
  - elliptic generator iD (det=m^2+|sin q|^2>0)            [cpt_exact_real_anti_hermitian_d, #3222]
  - 2-point Ward / transverse seagull                       [#3242]
  - operator-level stress Ward-Takahashi backbone           [#3325]
  - conserved coupling = momentum-reparametrization D(P_eff) [#3329]
  - CUBIC diffeomorphism Ward continuum closure              [#3342]
  - QUARTIC diffeomorphism Ward continuum closure            [#3353]

UNIFIED METHOD (tested here at n=3 and n=4): the n-point graviton diffeomorphism Ward diagnostic is the
(n-1)-fold cross term of the gauge variation dW/d(eps) under a lattice-consistent diffeomorphism
delta_xi h = (d_i xi_j + d_j xi_i) + Lie_xi h, with (n-1) distinct NON-COLLINEAR transverse-traceless
gravitons and the gauge field xi at the momentum closing the sum to zero. With the CONSERVED coupling
  D[h] = i sig_a[ Lm_a + Ch_a o d_a - 1/2 Lm_a o d_a^2 - 1/6 Ch_a o d_a^3 + 1/24 Lm_a o d_a^4 ] + m sqrt(g),
  d_a = sum_b (Wdens-I)_ab o Lm_b, Wdens=det(e)e^{-1}, e=sqrtm(I+h), o=Jordan-symmetric,
the residual normalized by the amplitude decreases over L=6 -> L=8 in this diagnostic; with the NAIVE
non-conserved coupling (vielbein on the hop amplitude) the contrast is worse.

  T0  elliptic pin: native iD det=m^2+|sin q|^2>0 on all BZ modes (the foundation; bare-Hermitian
      sigma.sin is sign-indefinite).
  T1  CUBIC (n=3) Ward diagnostic favors the conserved coupling: resid/amplitude decreases with k (L=6,8).
  T2  QUARTIC (n=4) Ward diagnostic favors the conserved coupling: resid/amplitude decreases with k (L=6,8).
  T3  UNIFIED conserved-vs-naive: at BOTH cubic and quartic order the conserved resid/amplitude is below
      the naive one and decreases faster -> the conserved velocity x momentum coupling is favored at
      both tested orders.

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 600

import numpy as np
from scipy.linalg import sqrtm
from pathlib import Path

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
sig = [sx, sy, sz]
I2 = np.eye(2, dtype=complex)

results = []
def check(name, ok):
    results.append((name, bool(ok)))

# ---------------------------------------------------------------------------
# T0: elliptic pin
# ---------------------------------------------------------------------------
def t0_elliptic():
    N = 14
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    m = 1.0
    neg_iD = neg_H = tot = 0
    for qx in p:
        for qy in p:
            for qz in p:
                s2 = np.sin(qx) ** 2 + np.sin(qy) ** 2 + np.sin(qz) ** 2
                if m * m + s2 <= 0:
                    neg_iD += 1
                if m * m - s2 <= 0:
                    neg_H += 1
                tot += 1
    check("T0 elliptic pin: native iD det=m^2+|sin|^2>0 on all %d BZ modes; bare-Herm sigma.sin sign-indefinite (%d/%d)"
          % (tot, neg_H, tot), neg_iD == 0 and neg_H > tot // 2)

# ---------------------------------------------------------------------------
# lattice machinery (conserved D(P_eff) to O(h^4) + sqrt(g); naive C1)
# ---------------------------------------------------------------------------
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
        da = dop(a); da2 = jord(da, da); da3 = jord(da, da2); da4 = jord(da, da3)
        spatial = (Lm[a] + jord(Ch[a], da) - 0.5 * jord(Lm[a], da2)
                   - (1 / 6.0) * jord(Ch[a], da3) + (1 / 24.0) * jord(Lm[a], da4))
        blk = 1j * spatial
        for x in sites:
            row = blk[sidx[x]]
            for iy in np.nonzero(np.abs(row) > 1e-14)[0]:
                D[2 * sidx[x]:2 * sidx[x] + 2, 2 * iy:2 * iy + 2] += sig[a] * row[iy]
    return D

def Dnaive(L, m, hfun, ctx):
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

# spatial axes and transverse-traceless (off-diagonal) polarizations
_AXES = [np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([0, 0, 1.0])]
def _TT(d):  # off-diagonal pol transverse to axis d (uses the other two axes)
    a, b = [i for i in range(3) if i != d]
    E = np.zeros((3, 3)); E[a, b] = E[b, a] = 1.0
    return E

def npoint_ward_ratio(L, Db, npt, m=1.0, amp=0.05, tau=1e-4):
    """(npt)-point graviton Ward = (npt-1)-fold cross term of dW/deps. npt in {3,4}."""
    ctx = build(L); kk = 2 * np.pi / L
    ng = npt - 1  # number of physical gravitons
    ks = [kk * _AXES[i] for i in range(ng)]
    Es = [_TT(i) for i in range(ng)]
    k1 = -sum(ks)  # gauge momentum closes the sum
    c = np.array([1.0, 0.6, 0.8])
    def xi_fun(x):
        return c * np.sin(k1 @ np.array(x))
    def F(signs):
        modes = [(signs[i] * amp, ks[i], Es[i]) for i in range(ng)]
        hf = make_h(L, modes)
        D0 = Db(L, m, hf, ctx); Di = np.linalg.inv(D0)
        out = {}
        for part in ('gauge', 'lie'):
            df = delta_xi(L, xi_fun, hf, part)
            Dp = Db(L, m, lambda x: hf(x) + tau * df(x), ctx)
            Dm = Db(L, m, lambda x: hf(x) - tau * df(x), ctx)
            out[part] = np.real(np.trace(Di @ ((Dp - Dm) / (2 * tau))))
        return out
    import itertools
    pts = {}
    for s in itertools.product((1, -1), repeat=ng):
        pts[s] = F(s)
    def cross(part):
        tot = 0.0
        for s in pts:
            tot += np.prod(s) * pts[s][part]
        return tot / (2 ** ng * amp ** ng)
    g = cross('gauge'); resid = g + cross('lie')
    return abs(resid) / abs(g), kk

# ---------------------------------------------------------------------------
t0_elliptic()

# T1 cubic (n=3), T2 quartic (n=4): conserved closes (resid/amp decreases L6->L8)
rc3 = {L: npoint_ward_ratio(L, Dcons, 3) for L in (6, 8)}
rc4 = {L: npoint_ward_ratio(L, Dcons, 4) for L in (6, 8)}
check("T1 CUBIC (n=3) Ward diagnostic: conserved resid/amplitude %.4f@k%.2f -> %.4f@k%.2f over L=6->8"
      % (rc3[6][0], rc3[6][1], rc3[8][0], rc3[8][1]), rc3[8][0] < rc3[6][0])
check("T2 QUARTIC (n=4) Ward diagnostic: conserved resid/amplitude %.4f@k%.2f -> %.4f@k%.2f over L=6->8"
      % (rc4[6][0], rc4[6][1], rc4[8][0], rc4[8][1]), rc4[8][0] < rc4[6][0])

# T3 unified conserved-vs-naive at both orders
rn3 = {L: npoint_ward_ratio(L, Dnaive, 3) for L in (6, 8)}
rn4 = {L: npoint_ward_ratio(L, Dnaive, 4) for L in (6, 8)}
cubic_better = rc3[8][0] < rn3[8][0] and (rc3[6][0] / rc3[8][0]) > (rn3[6][0] / rn3[8][0])
quartic_better = rc4[8][0] < rn4[8][0] and (rc4[6][0] / rc4[8][0]) > (rn4[6][0] / rn4[8][0])
check("T3 UNIFIED: at BOTH cubic and quartic order the conserved resid/amplitude is below the naive (cubic %.3f<%.3f, quartic %.3f<%.3f) and decreases faster -> conserved coupling favored at both tested orders"
      % (rc3[8][0], rn3[8][0], rc4[8][0], rn4[8][0]), cubic_better and quartic_better)

note = Path("docs/UNIVERSAL_GR_EINSTEIN_HILBERT_CLOSURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-06-08.md").read_text(encoding="utf-8")
guardrails = [
    "finite-lattice diagnostic",
    "no full Einstein-Hilbert action identification",
    "no all-order nonlinear diffeomorphism-invariance theorem",
    "no `G_Newton` magnitude",
    "no new primitive, axiom, or Tier-A admission",
]
check("T4 source note keeps synthesis diagnostic bounded", all(item in note for item in guardrails))

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("SYNTHESIS DIAGNOSTIC: the supplied conserved coupling D(P_eff) + sqrt(g) measure is favored over")
print("the naive non-conserved control in the runner-defined cubic and quartic finite-lattice Ward")
print("diagnostics on L=6,8. This consolidates the landed bounded Ward lane without claiming an")
print("Einstein-Hilbert action identification, all-order nonlinear diffeomorphism invariance, continuum")
print("coefficients, or G_Newton.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
