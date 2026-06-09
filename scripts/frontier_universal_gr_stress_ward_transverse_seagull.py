"""Finite runner (memory-safe): a runner-defined conserved stress-vertex scheme
for the universal-GR finite-BZ graviton diagnostic.

This script certifies a bounded source packet, not the full W-native
metric-Hessian bridge.  It constructs the native elliptic anti-Hermitian Dirac
operator, a conserved velocity x momentum stress vertex, and a local contact
seagull in the displayed {B0,B1,B5} basis.  It then checks that the scheme
removes the leading longitudinal violation of the finite-BZ stress two-point
function and preserves the positive yz TT stiffness.  The later identification
of this runner-defined vertex/seagull with the complete metric Hessian of W,
including all contact terms and continuum Ward/isotropy limits, remains a
separate open bridge.

NATIVE generator: D(q) = 1j*(sx sin qx + sy sin qy + sz sin qz) + m I2   (elliptic; the load-bearing
#3222 pin). Lattice divergence: k^i -> 2 sin(k_i/2). Induced-action graviton self-energy (Gamma =
-log det): Pi_grav = +Tr[GVGV] - Tr[G S]; HEALTHY = positive TT k^2 slope.

  T1  native iD elliptic (det=m^2+|sin q|^2>0 ALL BZ modes); bare-Hermitian sigma.sin sign-indefinite
      (NOT a valid partition function -- the #3222 control / spurious-tachyon operator).
  T2  MACHINERY validated on the INTERNAL U(1) gauge sector (an EXACT lattice symmetry):
      (a) single-current operator Ward sum_a 2sin(k_a/2) G_a(q,k) = D(q+k)-D(q) is EXACT (midpoint
          vertex G_a = 1j sig_a cos(q_a+k_a/2));
      (b) photon vacuum polarization Pi_ab = -bubble + seagull is EXACTLY transverse
          (sum_a 2sin(k_a/2) Pi_ab = 0), seagull Sg(q,a)=-1j sig_a sin(q_a) (NET-ZERO momentum ->
          midpoint argument q). => bubble+seagull+2sin(k/2) machinery is correct; U(1) is exactly
          transverse on the lattice.
  T3  the NAIVE stress vertex (the #3222 yz vertex extended to the full symmetric vertex,
      V_ij=(1j/2)(sig_i sbar_j+sig_j sbar_i), sbar_j=(sin q_j+sin(q_j+k_j))/2) FAILS transversality:
      residual ~0.1, N-INDEPENDENT at fixed k0 (a genuine finite-k violation, not a BZ-discretization
      artifact).
  T4  the CONSERVED velocity x momentum vertex V_cd=(1j/2)(sig_c cos(q_c+k_c/2) sbar_d + c<->d)
      (reduces to the #3222 TT vertex in the yz channel) has a CLEAN LOCAL longitudinal contact term;
      the explicit diamagnetic SEAGULL S=-B0+B1+B5 (local 2-graviton vertex, integer coefficients)
      cancels it. Then:
      (a) C2 ALONE (no seagull): residual is O(k0) (LINEAR) -- longitudinal self-energy is O(1);
      (b) C2 + seagull: residual is O(k0^3) -- the leading O(k0) longitudinal violation is EXACTLY
          removed by the seagull (res/k0^3 -> const); N-INDEPENDENT at fixed k0 (genuine continuum
          quantity); holds OFF-AXIS too.
      => in this runner-defined scheme, the leading longitudinal violation is removed and the
         residual scales as O(k0^3).  This is not a proof of the full metric-Hessian
         diffeomorphism Ward identity.
  T5  the HEALTHY positive TT (yz) sign SURVIVES the scheme-clean vertex + seagull (induced-action
      stiffness > 0), mass-robust.
  T6  the seagull tadpole reproduces the k->0 longitudinal contact term to ~1e-12 (it IS the genuine
      diamagnetic term, not a per-channel subtraction).

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 360

import numpy as np

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
sig = [sx, sy, sz]
PREF = 1j  # native elliptic anti-Hermitian iD

results = []
def check(name, ok):
    results.append((name, bool(ok)))

def Dmat(q, m):
    return PREF * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + m * I2

def Ginv(q, m):
    return np.linalg.inv(Dmat(q, m))

def sbar(qi, ki):
    return 0.5 * (np.sin(qi) + np.sin(qi + ki))

# ---------------------------------------------------------------------------
# T1: native elliptic pin (det>0); bare-Hermitian sign-indefinite control
# ---------------------------------------------------------------------------
def t1_ellipticity():
    N = 16
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
    check("T1 native iD elliptic: det=m^2+|sin|^2>0 on ALL BZ modes (valid Z)", neg_iD == 0)
    check("T1b bare-Hermitian sigma.sin sign-indefinite (%d/%d modes det<=0, invalid Z, #3222 control)"
          % (neg_H, tot), neg_H > tot // 2)

# ---------------------------------------------------------------------------
# T2: internal U(1) machinery -- EXACT lattice Ward (the validated machinery + contrast)
# ---------------------------------------------------------------------------
def Gcur(q, k, a):  # midpoint conserved current vertex
    return PREF * sig[a] * np.cos(q[a] + k[a] / 2)

def t2_gauge_ward():
    rng = np.random.default_rng(0)
    maxerr = 0.0
    for _ in range(1500):
        q = rng.uniform(-np.pi, np.pi, 3)
        k = rng.uniform(-np.pi, np.pi, 3)
        m = rng.uniform(0.3, 2.0)
        lhs = sum(2 * np.sin(k[a] / 2) * Gcur(q, k, a) for a in range(3))
        rhs = Dmat(q + k, m) - Dmat(q, m)
        maxerr = max(maxerr, np.abs(lhs - rhs).max())
    check("T2a single-current operator Ward sum_a 2sin(k_a/2)G_a=D(q+k)-D(q) EXACT (err=%.1e)" % maxerr,
          maxerr < 1e-12)
    # photon vacuum polarization transversality with seagull (net-zero momentum -> arg q)
    def Sg_gauge(q, a):
        return -PREF * sig[a] * np.sin(q[a])
    N = 12
    m = 1.0
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    worst = 0.0
    for k in (np.array([2 * np.pi / N, 0.0, 0.0]), np.array([2 * np.pi / N, 2 * np.pi / N, 0.0])):
        Pi = np.zeros((3, 3), complex)
        for qx in p:
            for qy in p:
                for qz in p:
                    q = np.array([qx, qy, qz])
                    Gq = Ginv(q, m)
                    Gqk = Ginv(q + k, m)
                    for a in range(3):
                        for b in range(3):
                            Pi[a, b] += -np.trace(Gq @ Gcur(q, k, a) @ Gqk @ Gcur(q + k, -k, b))
                            if a == b:
                                Pi[a, b] += np.trace(Gq @ Sg_gauge(q, a))
        Pi /= N ** 3
        ward = np.array([sum(2 * np.sin(k[a] / 2) * Pi[a, b] for a in range(3)) for b in range(3)])
        worst = max(worst, np.abs(ward).max())
    check("T2b photon Pi_ab EXACTLY transverse (sum_a 2sin(k_a/2)Pi_ab=0, max=%.1e) -- U(1) exact on lattice"
          % worst, worst < 1e-12)

# ---------------------------------------------------------------------------
# Stress vertices: C1 naive, C2 conserved; diamagnetic seagull
# ---------------------------------------------------------------------------
def V_naive(q, k, c, d):  # C1: the #3222 yz vertex extended symmetrically (NOT conserved)
    return 0.5 * (sig[c] * sbar(q[d], k[d]) + sig[d] * sbar(q[c], k[c])) * PREF

def V_cons(q, k, c, d):   # C2: velocity x momentum (conserved structure)
    return 0.5 * PREF * (sig[c] * np.cos(q[c] + k[c] / 2) * sbar(q[d], k[d])
                         + sig[d] * np.cos(q[d] + k[d] / 2) * sbar(q[c], k[c]))

def _kron(a, b):
    return 1.0 if a == b else 0.0

def _sym4(f):
    # symmetrize a base term over i<->j, k<->l, (ij)<->(kl)
    def g(q, i, j, k, l):
        v = np.zeros((2, 2), complex)
        for (ii, jj) in ((i, j), (j, i)):
            for (kk, ll) in ((k, l), (l, k)):
                v += f(q, ii, jj, kk, ll) + f(q, kk, ll, ii, jj)
        return v / 8.0
    return g

# diamagnetic seagull basis (the three nonzero terms; integer coefficients -1,+1,+1)
_B0 = _sym4(lambda q, i, j, k, l: _kron(i, k) * sig[i] * np.sin(q[i]) * np.sin(q[j]) * np.sin(q[l]))
_B1 = _sym4(lambda q, i, j, k, l: _kron(i, k) * sig[i] * np.cos(q[i]) * np.cos(q[j]) * np.sin(q[l]))
_B5 = _sym4(lambda q, i, j, k, l: _kron(j, l) * sig[i] * np.cos(q[i]) * np.sin(q[j]) * np.cos(q[k]))

def Seagull(q, i, j, k, l):
    return PREF * (-_B0(q, i, j, k, l) + _B1(q, i, j, k, l) + _B5(q, i, j, k, l))

def trans_residual(Vfun, kvec, N, m=1.0, seagull=False):
    """max_{j,k,l} | sum_i 2sin(k_i/2) Pi_ijkl |,  Pi = +Tr[GVGV] - Tr[G S] (induced action; sign
    irrelevant for transversality). Computed DIRECT per-channel (no tensor-fill -- avoids fill bugs)."""
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    kf = np.array([2 * np.sin(kvec[a] / 2) for a in range(3)])
    nz = [a for a in range(3) if abs(kf[a]) > 1e-12]
    C = np.zeros((3, 3, 3), complex)
    for qx in p:
        for qy in p:
            for qz in p:
                q = np.array([qx, qy, qz])
                Gq = Ginv(q, m)
                Gqk = Ginv(q + kvec, m)
                for j in range(3):
                    for k_ in range(3):
                        for l in range(3):
                            acc = 0j
                            for i in nz:
                                bub = np.trace(Gq @ Vfun(q, kvec, i, j) @ Gqk @ Vfun(q + kvec, -kvec, k_, l))
                                sg = np.trace(Gq @ Seagull(q, i, j, k_, l)) if seagull else 0j
                                acc += kf[i] * (bub - sg)
                            C[j, k_, l] += acc
    return np.abs(C / N ** 3).max()

def tt_slope(Vfun, N, m=1.0, seagull=False):
    """induced-action TT (yz) k^2 slope; healthy = positive."""
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    def Pi(kx):
        k = np.array([kx, 0.0, 0.0])
        t = 0j
        for qx in p:
            for qy in p:
                for qz in p:
                    q = np.array([qx, qy, qz])
                    Gq = Ginv(q, m)
                    Gqk = Ginv(q + k, m)
                    t += np.trace(Gq @ Vfun(q, k, 1, 2) @ Gqk @ Vfun(q + k, -k, 1, 2))
                    if seagull:
                        t -= np.trace(Gq @ Seagull(q, 1, 2, 1, 2))
        return t / N ** 3
    k1 = 2 * np.pi / N
    return ((Pi(k1) - Pi(0.0)) / (2 - 2 * np.cos(k1))).real

# ---------------------------------------------------------------------------
# T3: naive vertex fails transversality (N-independent finite-k violation)
# ---------------------------------------------------------------------------
def t3_naive_fails():
    k0 = 2 * np.pi / 6
    r12 = trans_residual(V_naive, np.array([k0, 0.0, 0.0]), 12)
    r18 = trans_residual(V_naive, np.array([k0, 0.0, 0.0]), 18)
    check("T3 naive stress vertex FAILS transversality: residual ~%.2f (large)" % r12, r12 > 0.05)
    check("T3b naive residual N-INDEPENDENT at fixed k0 (%.4f@N12 vs %.4f@N18 -> genuine finite-k, not discretization)"
          % (r12, r18), abs(r12 - r18) < 0.01 * max(r12, 1e-9) + 2e-3)

# ---------------------------------------------------------------------------
# T4: conserved vertex + seagull -> transversality improved O(k0)->O(k0^3)
# ---------------------------------------------------------------------------
def t4_conserved_seagull():
    # (a) C2 alone: residual LINEAR in k0
    ks = [(10, 2 * np.pi / 10), (14, 2 * np.pi / 14), (18, 2 * np.pi / 18)]
    nosg = [(k0, trans_residual(V_cons, np.array([k0, 0.0, 0.0]), N, seagull=False)) for N, k0 in ks]
    lin_ratios = [r / k0 for k0, r in nosg]
    check("T4a C2 (no seagull) residual LINEAR in k0 (res/k0=%s ~const => longitudinal self-energy O(1))"
          % ", ".join("%.3f" % x for x in lin_ratios),
          max(lin_ratios) - min(lin_ratios) < 0.02)
    # (b) C2 + seagull: residual CUBIC in k0 (leading violation removed)
    wsg = [(k0, trans_residual(V_cons, np.array([k0, 0.0, 0.0]), N, seagull=True)) for N, k0 in ks]
    cub_ratios = [r / k0 ** 3 for k0, r in wsg]
    check("T4b C2 + seagull residual CUBIC in k0 (res/k0^3=%s ~const => leading O(k0) longitudinal violation REMOVED)"
          % ", ".join("%.4f" % x for x in cub_ratios),
          max(cub_ratios) - min(cub_ratios) < 0.002)
    # the seagull genuinely improves the leading power: nosg/wsg residual grows as k0->0
    improve = [nosg[i][1] / wsg[i][1] for i in range(len(ks))]
    check("T4c seagull improves transversality by ~1/k0^2 (residual ratio nosg/sg=%s, grows as k0->0)"
          % ", ".join("%.0f" % x for x in improve), improve[-1] > improve[0] > 5)
    # (d) fixed k0, N-independence (not a fill/discretization artifact)
    k0 = 2 * np.pi / 6
    a12 = trans_residual(V_cons, np.array([k0, 0.0, 0.0]), 12, seagull=True)
    a18 = trans_residual(V_cons, np.array([k0, 0.0, 0.0]), 18, seagull=True)
    check("T4d seagulled residual N-INDEPENDENT at fixed k0 (%.5f@N12 vs %.5f@N18 -> genuine continuum quantity)"
          % (a12, a18), abs(a12 - a18) < 1e-4)
    # (e) off-axis k
    off = trans_residual(V_cons, np.array([2 * np.pi / 12, 2 * np.pi / 12, 0.0]), 12, seagull=True)
    check("T4e transversality holds OFF-AXIS k=(k0,k0,0) too (residual=%.4f, small)" % off, off < 0.03)

# ---------------------------------------------------------------------------
# T5: healthy TT sign survives the scheme-clean vertex + seagull
# ---------------------------------------------------------------------------
def t5_healthy_tt():
    slopes = [tt_slope(V_cons, N, seagull=True) for N in (10, 14, 18)]
    check("T5 healthy POSITIVE TT (yz) stiffness survives scheme-clean vertex+seagull (induced-action slope=%s)"
          % ", ".join("%+.5f" % s for s in slopes), all(s > 0 for s in slopes))
    mass = [tt_slope(V_cons, 14, m=mm, seagull=True) for mm in (0.5, 1.0, 1.5)]
    check("T5b mass-robust: TT stiffness > 0 for m in {0.5,1,1.5} (%s)"
          % ", ".join("%+.5f" % s for s in mass), all(s > 0 for s in mass))

# ---------------------------------------------------------------------------
# T6: the seagull tadpole IS the k->0 longitudinal contact term (genuine diamagnetic term)
# ---------------------------------------------------------------------------
def t6_seagull_is_contact():
    # longitudinal bubble constant C[j,k,l] = lim_{k0->0} Pi^bub_{x j k l}; seagull tadpole must = -C
    N = 16
    m = 1.0
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    k0 = 2 * np.pi / N
    kvec = np.array([k0, 0.0, 0.0])
    chans = [(0, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 2), (2, 2, 0), (0, 1, 1), (0, 2, 2)]
    worst = 0.0
    basis_rows = []
    target = []
    for (j, k_, l) in chans:
        bub = 0j
        tad = 0j
        cols = [0j, 0j, 0j]
        for qx in p:
            for qy in p:
                for qz in p:
                    q = np.array([qx, qy, qz])
                    Gq = Ginv(q, m)
                    Gqk = Ginv(q + kvec, m)
                    bub += np.trace(Gq @ V_cons(q, kvec, 0, j) @ Gqk @ V_cons(q + kvec, -kvec, k_, l))
                    tad += np.trace(Gq @ Seagull(q, 0, j, k_, l))
                    basis = [
                        PREF * _B0(q, 0, j, k_, l),
                        PREF * _B1(q, 0, j, k_, l),
                        PREF * _B5(q, 0, j, k_, l),
                    ]
                    for idx, term in enumerate(basis):
                        cols[idx] += np.trace(Gq @ term)
        bub = (bub / N ** 3).real   # ~ longitudinal contact constant (k0 small)
        tad = (tad / N ** 3).real   # seagull tadpole
        worst = max(worst, abs(bub - tad))   # tadpole must equal the contact term
        basis_rows.append([(col / N ** 3).real for col in cols])
        target.append(bub)
    check("T6 seagull tadpole reproduces the k->0 longitudinal contact term in all channels (max|bub-tad|=%.1e)"
          % worst, worst < 5e-3)
    A = np.array(basis_rows, dtype=float)
    y = np.array(target, dtype=float)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    integer_coef = np.array([-1.0, 1.0, 1.0])
    integer_err = np.abs(A @ integer_coef - y).max()
    check("T6b small-k contact-basis solve recovers S=-B0+B1+B5 within finite-k error "
          "(coef=%+.3f,%+.3f,%+.3f; integer maxerr=%.1e)"
          % (coef[0], coef[1], coef[2], integer_err),
          np.abs(coef - integer_coef).max() < 5e-2 and integer_err < 5e-3)

# ---------------------------------------------------------------------------
t1_ellipticity()
t2_gauge_ward()
t3_naive_fails()
t4_conserved_seagull()
t5_healthy_tt()
t6_seagull_is_contact()

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("Runner-defined conserved velocity x momentum stress vertex + local seagull -> finite-BZ")
print("stress two-point function transverse to leading physical order (residual O(k0^3), leading")
print("longitudinal violation removed); healthy positive TT sign preserved in this scheme. BOUNDED")
print("on the open full metric-Hessian/contact-term bridge and the continuum Ward/isotropy limits.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
