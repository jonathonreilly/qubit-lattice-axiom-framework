"""Lane RC / C3, part 2.

(A) The O(kappa) {D,H} closure condition as a Fourier linear system, sub-family p_xi = 0
    (xi constant, which is a legitimate periodic smearing), N = exp(i p x_b).  Unknowns:
      C'(p), C_j(p)            structure functions, trig polynomials of degree <= r (shared by all q)
      Xi_comp(p, q)            the image of ANY E-linear completion P^(1)[xi; E -> S^T N]:
                               (1 - cos p) * (trig poly of degree <= r in p), ARBITRARY in the matter
                               momentum q (so more general than any local ansatz)
    (the h-linear completion T00^(1)[N; h -> ghat(xi)] is identically 0 at p_xi = 0)
    LHS = {P_tot_c, T00[N]} symbol: i (sin q1_c + sin q2_c) * T00~(q1, q2), q1 + q2 + p e_b = 0.
    We report the least-squares residual for r = 1..6, with and without the completion columns,
    for the L1 lattice scalar and for the continuum control (u = (m^2 + k^2)/2, i.e. symbols k, k^2).

(B) Dispersion scan: the boost-sector anomaly symbol A_c(k) = d^2 u / dk_c^2 - 1, u = omega^2/2.
    Any periodic u has BZ-average of d^2u/dk_c^2 equal to 0, so <A_c>_BZ = -1 exactly, whatever the
    stencil range r_m; improved stencils only push A_c into the UV (A_c = O(k^{2 r_m})).
    SLAC (u = k^2/2 on the lifted zone) has A_c = 0 except a zone-boundary delta of weight -2 pi.
"""
import numpy as np

rng = np.random.default_rng(20261011)
M2 = 0.3


# ---------------- two-momentum symbols of the L1 densities (plane waves e^{i q x}) -------------
def t00_symbols(q1, q2, cont=False):
    """returns (pipi, phiphi) symbols of T00 (symmetric in q1,q2)."""
    pipi = 0.5 * np.ones(q1.shape[:-1], dtype=complex)
    if cont:
        # continuum T00 = pi^2/2 + (grad phi)^2/2 + m^2 phi^2/2: (i q1)(i q2) -> -q1.q2
        phph = 0.5 * M2 + 0.5 * (-np.sum(q1 * q2, axis=-1))
        return pipi, phph.astype(complex)
    e1, e2 = np.exp(1j * q1), np.exp(1j * q2)
    phph = 0.5 * M2 + 0.25 * np.sum((e1 - 1) * (e2 - 1) + (1 - 1 / e1) * (1 - 1 / e2), axis=-1)
    return pipi, phph


def p_symbol(q1, q2, j, cont=False):
    """P_j symbol for pi_{q1} phi_{q2} (not symmetrised)."""
    if cont:
        return 1j * q2[..., j]
    return 0.5 * (1 + np.exp(1j * q1[..., j])) * (np.exp(1j * q2[..., j]) - 1)


def deriv_factor(q1, q2, c, cont=False):
    s = (lambda q: 1j * q[..., c]) if cont else (lambda q: 1j * np.sin(q[..., c]))
    return s(q1) + s(q2)


def system_residual(r, b, c, cont=False, with_completion=True, nq=24, npts=48, ir_only=False):
    """least-squares residual of the {D,H} condition at p_xi = 0, N = e^{i p x_b}.
    Sampling: a coarse grid over the zone plus 16 points with |p| <= 0.1 (the IR, where the
    obstruction lives).  ir_only=True reports the residual restricted to those IR rows."""
    ps = np.concatenate([np.linspace(-np.pi, np.pi, npts, endpoint=False) + 0.013,
                         np.linspace(-0.1, 0.1, 16)])
    if cont:
        ps = ps / 4.0          # continuum control: same structure, no zone
    qs = rng.uniform(-np.pi, np.pi, (nq, 3))
    if cont:
        qs = qs / 2.0
    nC = 2 * r + 1
    harm = np.arange(-r, r + 1)
    # unknown blocks: C' (nC), C_j (3 nC), Xi_pipi, Xi_phph, Xi_piph (each nq*nC)
    n_unk = 4 * nC + (3 * nq * nC if with_completion else 0)
    rows, rhs = [], []
    for iq, q1 in enumerate(qs):
        for p in ps:
            pv = np.zeros(3); pv[b] = p
            q2 = -q1 - pv
            Q1, Q2 = q1[None, :], q2[None, :]
            fac = deriv_factor(Q1, Q2, c, cont)[0]
            # LHS components: pipi and phiphi symmetrised, piphi from nothing (T00 has no pi phi)
            pp, ff = t00_symbols(Q1, Q2, cont)
            lhs = {"pp": fac * pp[0], "ff": fac * ff[0], "pf": 0.0 + 0j}
            # RHS basis at total momentum p: T00~(q1,q2), P~_j(q1,q2) (pi_q1 phi_q2) -- same q1,q2
            basis_t = {"pp": pp[0], "ff": ff[0], "pf": 0.0}
            basis_p = [{"pp": 0.0, "ff": 0.0, "pf": p_symbol(Q1, Q2, j, cont)[0]} for j in range(3)]
            fourier = np.exp(1j * harm * p) if not cont else p ** (harm + r)   # polynomial basis for the continuum
            gate = (1 - np.cos(p)) if not cont else p * p / 2
            for ic, comp in enumerate(("pp", "ff", "pf")):
                row = np.zeros(n_unk, dtype=complex)
                row[0:nC] = basis_t[comp] * fourier
                for j in range(3):
                    row[nC * (1 + j):nC * (2 + j)] = basis_p[j][comp] * fourier
                if with_completion:
                    off = 4 * nC + (ic * nq + iq) * nC
                    row[off:off + nC] = gate * fourier
                rows.append(row); rhs.append(lhs[comp])
    A = np.array(rows); y = np.array(rhs)
    if np.max(np.abs(y)) == 0:
        return 0.0, None, None, A.shape, 0.0, 0.0
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = np.linalg.norm(A @ coef - y) / np.linalg.norm(y)
    # IR rows: last 16 p values of each q block, 3 components each
    npp = len(ps)
    irmask = np.zeros(len(y), bool)
    for iq in range(nq):
        for ip in range(npp - 16, npp):
            base = (iq * npp + ip) * 3
            irmask[base:base + 3] = True
    res_ir = np.linalg.norm((A @ coef - y)[irmask]) / np.linalg.norm(y[irmask])
    xi_norm = np.max(np.abs(coef[4 * nC:])) if with_completion else 0.0
    rk = np.linalg.matrix_rank(A, tol=1e-9)
    rk_aug = np.linalg.matrix_rank(np.column_stack([A, y]), tol=1e-9)
    return res, rk, rk_aug, A.shape, res_ir, xi_norm


print("=== (A) Fourier linear system for the O(kappa) {D,H} condition, p_xi = 0, N = e^{i p x_b} ===")
print("    columns: structure functions (deg<=r) + completion image (1-cos p)*Xi(p,q), Xi arbitrary in q, deg<=r in p")
for (b, c) in [(0, 0), (0, 1)]:
    for cont in (False, True):
        for r in (1, 2, 4, 8, 12, 16):
            if cont and r > 4:
                continue
            res, rk, rka, shp, rir, xin = system_residual(r, b, c, cont=cont)
            res0 = system_residual(r, b, c, cont=cont, with_completion=False)[0]
            tag = "continuum" if cont else "lattice L1"
            if rk is None:
                print(f"(b,c)=({b},{c}) {tag:10s}: LHS identically 0 (b != c), nothing to close"); break
            print(f"(b,c)=({b},{c}) {tag:10s} r={r:2d}: residual all-p {res:.3e} | IR rows |p|<=0.1 {rir:.3e} "
                  f"| no completion {res0:.3e}; rank A={rk}, rank[A|b]={rka}; max|Xi coef|={xin:.1e}")

# ---------------- (B) dispersion scan --------------------------------------------------------
print("\n=== (B) boost-sector anomaly symbol A(k) = u''(k) - 1 along an axis, u = omega^2/2 ===")
cn = [1.0, 1 / 12, 1 / 90, 1 / 560, 1 / 3150]


def w2_imp(k, rm):
    s2 = (2 * np.sin(k / 2)) ** 2
    return sum(cn[n] * s2 ** (n + 1) for n in range(rm))


kk = np.linspace(-np.pi, np.pi, 200001)
dk = kk[1] - kk[0]
for rm in (1, 2, 3, 4, 5):
    u = 0.5 * w2_imp(kk, rm)
    upp = np.gradient(np.gradient(u, dk), dk)
    A = upp - 1
    avg = np.trapezoid(upp, kk) / (2 * np.pi)
    ir = [np.max(np.abs(A[np.abs(kk) < kap])) for kap in (0.1, 0.3, 1.0)]
    print(f"stencil range r_m={rm}: <u''>_BZ = {avg:+.2e} (so <A>_BZ = -1); max|A| on |k|<0.1,0.3,1: "
          f"{ir[0]:.2e} {ir[1]:.2e} {ir[2]:.2e}; A(pi) = {A[-1]:+.3f}")
# IR exponent
for rm in (1, 2, 3):
    k1, k2 = 0.05, 0.1
    def Aof(k):
        h = 1e-3
        return 0.5 * (w2_imp(k + h, rm) - 2 * w2_imp(k, rm) + w2_imp(k - h, rm)) / h**2 - 1
    print(f"   r_m={rm}: IR exponent log|A(0.1)/A(0.05)|/log2 = {np.log(abs(Aof(k2) / Aof(k1))) / np.log(2):.2f} (expected {2 * rm})")

print("\nrandom cubic-symmetric local dispersions (range 3, random positive hop weights, incl. face/body hops):")
def rand_u(K, w):
    # u = 1/2 [m^2 + sum_n w_n (cubic orbit sum of 1 - cos(n.k))]
    orbits = [np.array(v) for v in ([1, 0, 0], [2, 0, 0], [3, 0, 0], [1, 1, 0], [1, 1, 1], [2, 1, 0])]
    tot = 0.5 * M2
    for wn, v in zip(w, orbits):
        import itertools
        seen = set()
        for perm in itertools.permutations(range(3)):
            for sg in itertools.product((1, -1), repeat=3):
                vv = tuple(int(sg[i] * v[perm[i]]) for i in range(3))
                if vv in seen or tuple(-x for x in vv) in seen:
                    continue
                seen.add(vv)
                tot = tot + wn * (1 - np.cos(K @ np.array(vv, float)))
    return 0.5 * tot * 2
g16 = 2 * np.pi * np.arange(16) / 16
Ks = np.array(np.meshgrid(g16, g16, g16, indexing='ij')).reshape(3, -1).T   # uniform grid: exact BZ average for these trig polys
for trial in range(4):
    w = rng.uniform(0.05, 1.0, 6)
    h = 1e-3
    E = np.eye(3)
    H = np.array([[ (rand_u(Ks + h*E[a] + h*E[bq], w) - rand_u(Ks + h*E[a] - h*E[bq], w)
                    - rand_u(Ks - h*E[a] + h*E[bq], w) + rand_u(Ks - h*E[a] - h*E[bq], w)) / (4*h*h)
                   for bq in range(3)] for a in range(3)])        # 3x3xNk Hessian
    Cbest = H.mean(axis=2)                                         # best constant fit
    rel = np.linalg.norm(H - Cbest[:, :, None]) / np.linalg.norm(H)
    print(f"  trial {trial}: <Hess u>_BZ (exact grid) diag = {np.round(np.diag(Cbest), 3)} ; "
          f"relative non-constancy of Hess u = {rel:.3f}")

print("\nSLAC control (u = k^2/2 on (-pi,pi], periodic): u'' = 1 everywhere inside the zone; "
      "periodicity is paid by u' jumping 2 pi -> delta of weight -2 pi at k = pi.")
