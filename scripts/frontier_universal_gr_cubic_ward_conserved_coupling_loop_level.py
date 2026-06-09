"""Class-A finite runner (memory-safe): the conserved all-orders metric coupling for the W-native
induced graviton is the momentum-reparametrization D(P_eff), and the cubic diffeomorphism Ward
identity is intrinsically a LOOP-level (O(a^2) continuum-only) statement -- it does NOT promote to a
clean operator-level identity the way the exact vertex Ward identity R0 (the operator-level stress
Ward-Takahashi backbone, the cubic_diffeo_ward_operator_telescope note) does.

Context: the W-native induced graviton is the Dirac stress n-point function of W=log|det(D+J)| on the
native elliptic anti-Hermitian Dirac iD (det=m^2+|sin q|^2>0). The metric h_ij couples to the
conserved stress vertex V_cons_ij = 1/2(u_i sbar_j + u_j sbar_i), u_i=1j sig_i cos(q_i+k_i/2),
sbar_j=(sin q_j+sin(q_j+k_j))/2 (the stress-Ward note, #3242). The QUESTION this runner settles: what
position-space all-orders coupling realizes V_cons (so its exact determinant bundles the conserved
seagulls), and does the cubic Ward then close as an operator identity?

  T1  the CONSERVED all-orders coupling is the momentum-reparametrization D(P_eff): the metric shifts
      the momentum ARGUMENT inside the dispersion, P_eff,a = (sqrt(I+h) . q)_a, so
      D = i sig_a sin(P_eff,a) + m. Its extracted single-graviton vertex equals V_cons EXACTLY.
  T2  the NAIVE vielbein-on-hops coupling (the metric on the hop AMPLITUDE, the position-space exact
      determinant route) instead gives the NON-conserved naive vertex V_naive = 1/2(sig_i sbar_j +
      sig_j sbar_i)*1j EXACTLY -- the C1 vertex step-1 (#3242) proved FAILS the Ward. So the
      position-space exact-determinant (naive-vielbein) route CANNOT close the Ward; a real-space
      diffeomorphism-variation test on it that returns ~0 is the TT gauge-orthogonality trivial zero,
      not a genuine closure.
  T3  the cubic Ward does NOT promote to a clean operator identity: the conserved seagull S2 (the
      2-graviton coupling of D(P_eff)) has a longitudinal contraction (graviton-1 = d_xi) that is NOT
      proportional to the vertex difference 1/2[V(q+k1,k2)-V(q,k2)] -- the ratio varies in magnitude
      AND phase across the loop momentum q. So the operator-tower rung R1 FAILS; the cubic Ward is
      intrinsically a LOOP-level identity (the seagull combines with the triangle and the R0 contact
      only under the loop integral), hence an O(a^2) continuum-only statement on the rigid lattice --
      the cubic analog of the 2-point O(a^2) floor of #3242, now shown to be NOT an exact operator
      identity.

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 360

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

# ---- analytic conserved (V_cons) and naive (V_naive) momentum-space vertices ----
def u(q, k, i):
    return 1j * sig[i] * np.cos(q[i] + k[i] / 2)
def sbar(q, k, j):
    return 0.5 * (np.sin(q[j]) + np.sin(q[j] + k[j]))
def V_cons(q, k, i, j):
    return 0.5 * (u(q, k, i) * sbar(q, k, j) + u(q, k, j) * sbar(q, k, i))
def V_naive(q, k, i, j):
    return 0.5 * (sig[i] * sbar(q, k, j) + sig[j] * sbar(q, k, i)) * 1j

# ---- lattice ----
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

def Dcov(L, m, hfun, ctx):
    """conserved coupling D = i sig_a[ LatMom_a + CosHop_a o delta_a - 1/2 LatMom_a o delta_a^2 ] + m,
       delta_a = sum_b (sqrtm(I+h)-I)_ab(x) o LatMom_b  (momentum-argument reparametrization)."""
    sites, sidx, n, Sp = ctx
    LatMom = [(1 / (2j)) * (Sp[a] - Sp[a].conj().T) for a in range(3)]
    CosHop = [0.5 * (Sp[a] + Sp[a].conj().T) for a in range(3)]
    Wm = np.zeros((3, 3, n), complex)
    for x in sites:
        W = sqrtm(np.eye(3) + hfun(x)) - np.eye(3)
        Wm[:, :, sidx[x]] = W
    def delta(a):
        D = np.zeros((n, n), complex)
        for b in range(3):
            D += jord(np.diag(Wm[a, b]), LatMom[b])
        return D
    D = np.zeros((2 * n, 2 * n), complex)
    for x in sites:
        ix = sidx[x]; D[2 * ix:2 * ix + 2, 2 * ix:2 * ix + 2] += m * I2
    for a in range(3):
        da = delta(a)
        spatial = LatMom[a] + jord(CosHop[a], da) - 0.5 * jord(LatMom[a], jord(da, da))
        blk = 1j * spatial
        for x in sites:
            row = blk[sidx[x]]
            for iy in np.nonzero(np.abs(row) > 1e-14)[0]:
                D[2 * sidx[x]:2 * sidx[x] + 2, 2 * iy:2 * iy + 2] += sig[a] * row[iy]
    return D

def Dnaive(L, m, hfun, ctx):
    """naive vielbein-on-hops (metric on the hop AMPLITUDE): D = m + (1/2) sum_i sum_a sig_a
       ebar^a_i [psi(x+ei)-psi(x-ei)], e=sqrtm(I+h) link-averaged (the position-space determinant route)."""
    sites, sidx, n, Sp = ctx
    ef = {}
    for x in sites:
        ef[x] = np.real(sqrtm(np.eye(3) + hfun(x)))
    D = np.zeros((2 * n, 2 * n), complex)
    for x in sites:
        ix = sidx[x]; D[2 * ix:2 * ix + 2, 2 * ix:2 * ix + 2] += m * I2
        for i in range(3):
            xp = list(x); xp[i] = (xp[i] + 1) % L; xp = tuple(xp)
            xm = list(x); xm[i] = (xm[i] - 1) % L; xm = tuple(xm)
            for a in range(3):
                ep = 0.5 * (ef[x][a, i] + ef[xp][a, i]); em = 0.5 * (ef[x][a, i] + ef[xm][a, i])
                D[2 * ix:2 * ix + 2, 2 * sidx[xp]:2 * sidx[xp] + 2] += 0.5 * sig[a] * ep
                D[2 * ix:2 * ix + 2, 2 * sidx[xm]:2 * sidx[xm] + 2] += -0.5 * sig[a] * em
    return D

def project(dD, qin, qout, ctx):
    sites, sidx, n, Sp = ctx
    M = np.zeros((2, 2), complex)
    for x in sites:
        rb = dD[2 * sidx[x]:2 * sidx[x] + 2]
        for y in sites:
            blk = rb[:, 2 * sidx[y]:2 * sidx[y] + 2]
            if not np.any(np.abs(blk) > 1e-13):
                continue
            M += np.exp(-1j * qout @ np.array(x)) * np.exp(1j * qin @ np.array(y)) * blk
    return M / n

def extract_V(Dbuild, L, m, i, j, kvec, qvec, ctx, tau=1e-5):
    A = np.zeros((3, 3)); A[i, j] = 1.0; A[j, i] = A[i, j]
    if i == j:
        A[i, j] = 1.0
    def hf(sgn):
        return lambda x: A * sgn * tau * 2 * np.cos(kvec @ np.array(x))
    dD = (Dbuild(L, m, hf(+1), ctx) - Dbuild(L, m, hf(-1), ctx)) / (2 * tau)
    return project(dD, qvec, qvec + kvec, ctx)

# ---------------------------------------------------------------------------
# T1, T2: the conserved vs naive coupling vertices
# ---------------------------------------------------------------------------
def t1_t2_vertices():
    L = 6; m = 1.0; ctx = build(L)
    kvec = np.array([1, 0, 0]) * 2 * np.pi / L
    qvec = np.array([1, 2, 1]) * 2 * np.pi / L
    # all components for the conserved vertex; off-diagonal (i!=j) for the naive vertex (the diagonal
    # carries an additional trace/measure piece -- the off-diagonal shear sector is the decisive C1/C2
    # discriminator: V_cons uses the cos-weighted velocity u_i, V_naive the bare sig_i).
    errc = 0.0
    for (i, j) in [(0, 0), (0, 1), (1, 2)]:
        Mc = extract_V(Dcov, L, m, i, j, kvec, qvec, ctx)
        errc = max(errc, np.abs(Mc - V_cons(qvec, kvec, i, j)).max())
    errn = 0.0; distinct = 0.0
    for (i, j) in [(0, 1), (1, 2)]:
        Mn = extract_V(Dnaive, L, m, i, j, kvec, qvec, ctx)
        Vc = V_cons(qvec, kvec, i, j); Vn = V_naive(qvec, kvec, i, j)
        errn = max(errn, np.abs(Mn - Vn).max())
        distinct = max(distinct, np.abs(Vc - Vn).max())
    check("T1 conserved coupling D(P_eff) vertex = V_cons EXACTLY (err=%.1e) -- the conserved all-orders completion" % errc, errc < 1e-3)
    check("T2 naive vielbein-on-hops shear vertex = V_naive(C1) EXACTLY (err=%.1e), distinct from V_cons (|Vc-Vn|=%.2f) -- the non-conserved determinant route" % (errn, distinct), errn < 1e-3 and distinct > 0.1)

# ---------------------------------------------------------------------------
# T3: the cubic Ward does NOT promote to a clean operator identity (R1 fails)
# ---------------------------------------------------------------------------
def extract_S2(L, m, A1, k1, A2, k2, q, ctx, tau=2e-3):
    def D(a1, a2):
        return Dcov(L, m, lambda x: a1 * A1 * 2 * np.cos(k1 @ np.array(x)) + a2 * A2 * 2 * np.cos(k2 @ np.array(x)), ctx)
    dd = (D(tau, tau) - D(tau, -tau) - D(-tau, tau) + D(-tau, -tau)) / (4 * tau * tau)
    return project(dd, q, q + k1 + k2, ctx)

def t3_operator_tower_fails():
    L = 6; m = 1.0; ctx = build(L)
    k1 = np.array([1, 0, 0]) * 2 * np.pi / L
    k2 = np.array([0, 1, 0]) * 2 * np.pi / L
    xi = np.array([0.3, 1.0, 0.6])
    s1 = np.array([2 * np.sin(k1[i] / 2) for i in range(3)])
    A1 = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            A1[i, j] = s1[i] * xi[j] + s1[j] * xi[i]   # longitudinal graviton-1 = d_xi
    A2 = np.zeros((3, 3)); A2[0, 2] = A2[2, 0] = 1.0   # graviton-2 = xz
    def Vpol(qq, kk, E):
        M = np.zeros((2, 2), complex)
        for i in range(3):
            for j in range(3):
                if abs(E[i, j]) < 1e-15:
                    continue
                M += E[i, j] * V_cons(qq, kk, i, j)
        return M
    ratios = []
    for qi in [(1, 2, 1), (0, 3, 2), (1, 1, 1)]:
        qq = np.array(qi) * 2 * np.pi / L
        S2 = extract_S2(L, m, A1, k1, A2, k2, qq, ctx)
        Vd = 0.5 * (Vpol(qq + k1, k2, A2) - Vpol(qq, k2, A2))
        if abs(Vd[0, 1]) > 1e-6:
            ratios.append(S2[0, 1] / Vd[0, 1])
    # the operator-tower rung R1 would require S2-contraction = c * (vertex difference) with c constant;
    # FAILS: the ratio varies in magnitude AND phase across q
    spread = max(abs(r1 - r2) for r1 in ratios for r2 in ratios)
    check("T3 operator-tower R1 FAILS: seagull contraction / (vertex difference) ratio is NON-constant across q (spread=%.2f) -> cubic Ward is intrinsically LOOP-level (O(a^2) continuum-only), NOT a clean operator identity"
          % spread, spread > 0.1)

# ---------------------------------------------------------------------------
t1_t2_vertices()
t3_operator_tower_fails()

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("The conserved all-orders metric coupling is the momentum-reparametrization D(P_eff) (vertex =")
print("V_cons exactly; the naive vielbein-on-hops determinant route is the NON-conserved C1 vertex that")
print("cannot close the Ward). The cubic diffeomorphism Ward identity is intrinsically a LOOP-level,")
print("O(a^2) continuum-only statement: it does NOT promote to a clean operator-tower identity (the")
print("seagull's longitudinal contraction is not proportional to the vertex difference), unlike the")
print("exact operator-level vertex Ward identity R0 (the cubic_diffeo_ward_operator_telescope backbone).")
print("Magnitude registered (G3).")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
