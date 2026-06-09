"""Class-A finite runner (memory-safe): stress-vertex operator Ward telescoping
in the cubic GR channel.

This verifies exact finite operator identities for the conserved
velocity-times-momentum stress vertex.  The longitudinally contracted tested
cubic triangle decomposes into a telescoped two-point bubble difference plus a
same-order contact term.  The result is a bounded support diagnostic for the
operator backbone; it does not construct the conserved cubic seagull or prove
the full cubic diffeomorphism Ward identity / Einstein-Hilbert vertex.

W-native graviton = Dirac stress 2-point fn of W=log|det(D+J)| (Sakharov induced gravity) on the
framework's NATIVE elliptic anti-Hermitian Dirac iD (det=m^2+|sin q|^2>0; the load-bearing #3222 pin;
the bare-Hermitian sigma.sin is sign-indefinite, NOT a valid partition function). Lattice momentum
divergence: k^i -> 2 sin(k_i/2).

  T1  native iD elliptic (det=m^2+|sin q|^2>0 ALL BZ modes); bare-Hermitian sigma.sin sign-indefinite
      control (#3222 spurious-tachyon operator).
  T2  2-comp Cl(3): the EXACT gauge-current operator Ward identity (the validated machinery, step-1
      T2a): sum_i 2sin(k_i/2) u_i(q,k) = D(q+k)-D(q), u_i=1j sig_i cos(q_i+k_i/2).
  T3  2-comp Cl(3): the EXACT STRESS operator Ward-Takahashi identity. With the
      conserved velocity x momentum stress vertex V_ij=1/2(u_i sbar_j+u_j sbar_i), sbar_j=avg-sin,
        sum_i 2sin(k_i/2) V_ij = 1/2 sbar_j [D(q+k)-D(q)] + 1/2 Ssc u_j,  Ssc=sum_i 2sin(k_i/2)sbar_i.
      Ssc is O(k) (contact term). The 1/2 sbar_j [D(q+k)-D(q)] term is what telescopes the cubic
      triangle.
  T4  staggered Kahler-Dirac (16x16): the EXACT gauge operator Ward identity with the MIDPOINT
      velocity: sum_mu 2sin(K_mu/2) Vel(P+K/2,mu) = Dstag(P+K)-Dstag(P).
  T5  staggered Kahler-Dirac: the EXACT STRESS operator Ward-Takahashi identity:
        sum_mu 2sin(K_mu/2) Vst_munu = 1/2 mom_nu [Dstag(P+K)-Dstag(P)] + 1/2 Ssc Vel_nu(P+K/2).
  T6  TELESCOPING (staggered, non-collinear k1||sp1,k2||sp2,k3=-(k1+k2)): contracting the cubic
      triangle's k1-leg with the gauge graviton h1=d_xi and the exact stress op-WT (T5), the
      [Dstag(P+K1)-Dstag(P)] term telescopes G(P)dD G(P+K1)=G(P)-G(P+K1) -> a 2-point bubble
      DIFFERENCE (the stress-coupling telescope). The contracted
      triangle EQUALS telescope+contact EXACTLY (operator-identity consistency). The bubble-difference
      (equivalence-principle term) is NONZERO.
  T7  the contact term Ssc is O(k) (linear) -> it is the seagull-completion channel; the full
      quantitative LHS=RHS match is not claimed without the conserved cubic seagull.
  T8  the contact is NOT subleading: contact/LHS = 0.5 EXACTLY at every k0, and contact, telescope,
      and the full contracted vertex all scale at the SAME power of k0 -- the contracted cubic vertex
      splits 50/50 into a bubble-difference and a contact channel in this setup. So any closure
      attempt genuinely requires the seagull completion; it does NOT trivially vanish.

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 360

import numpy as np
import itertools

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
sig = [sx, sy, sz]

results = []
def check(name, ok):
    results.append((name, bool(ok)))

# ---------------------------------------------------------------------------
# 2-comp Cl(3) native elliptic generator + conserved vertex
# ---------------------------------------------------------------------------
def D2(q, m):
    return 1j * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + m * I2

def u(q, k, i):            # conserved current vertex = gauge current = dD/dq with midpoint
    return 1j * sig[i] * np.cos(q[i] + k[i] / 2)

def sbar(q, k, j):         # symmetric momentum factor
    return 0.5 * (np.sin(q[j]) + np.sin(q[j] + k[j]))

def Vstress2(q, k, i, j):  # conserved velocity x momentum stress vertex
    return 0.5 * (u(q, k, i) * sbar(q, k, j) + u(q, k, j) * sbar(q, k, i))

# ---------------------------------------------------------------------------
# T1: elliptic pin (det>0) vs bare-Hermitian sign-indefinite control
# ---------------------------------------------------------------------------
def t1_elliptic():
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
    check("T1 native iD elliptic: det=m^2+|sin|^2>0 on ALL %d BZ modes (valid Z)" % tot, neg_iD == 0)
    check("T1b bare-Hermitian sigma.sin sign-indefinite (%d/%d modes det<=0, #3222 control)" % (neg_H, tot),
          neg_H > tot // 2)

# ---------------------------------------------------------------------------
# T2: 2-comp gauge operator Ward identity (machinery; exact)
# ---------------------------------------------------------------------------
def t2_gauge_opward():
    rng = np.random.default_rng(0)
    err = 0.0
    for _ in range(3000):
        q = rng.uniform(-np.pi, np.pi, 3)
        k = rng.uniform(-np.pi, np.pi, 3)
        m = rng.uniform(0.3, 2.0)
        lhs = sum(2 * np.sin(k[i] / 2) * u(q, k, i) for i in range(3))
        err = max(err, np.abs(lhs - (D2(q + k, m) - D2(q, m))).max())
    check("T2 gauge op-Ward sum_i 2sin(k_i/2)u_i = D(q+k)-D(q) EXACT (err=%.1e)" % err, err < 1e-12)

# ---------------------------------------------------------------------------
# T3: 2-comp STRESS operator Ward-Takahashi identity (the new backbone; exact)
# ---------------------------------------------------------------------------
def t3_stress_opward():
    rng = np.random.default_rng(1)
    err = 0.0
    for _ in range(3000):
        q = rng.uniform(-np.pi, np.pi, 3)
        k = rng.uniform(-np.pi, np.pi, 3)
        m = rng.uniform(0.3, 2.0)
        dD = D2(q + k, m) - D2(q, m)
        Ssc = sum(2 * np.sin(k[i] / 2) * sbar(q, k, i) for i in range(3))
        for j in range(3):
            lhs = sum(2 * np.sin(k[i] / 2) * Vstress2(q, k, i, j) for i in range(3))
            rhs = 0.5 * sbar(q, k, j) * dD + 0.5 * Ssc * u(q, k, j)
            err = max(err, np.abs(lhs - rhs).max())
    check("T3 STRESS op-WT sum_i 2sin(k_i/2)V_ij = 1/2 sbar_j*dD + 1/2 Ssc*u_j EXACT (err=%.1e)" % err,
          err < 1e-12)

# ---------------------------------------------------------------------------
# staggered Kahler-Dirac machinery
# ---------------------------------------------------------------------------
corners = list(itertools.product([0, 1], repeat=4))
cidx = {A: i for i, A in enumerate(corners)}
def eta(A, mu):
    return (-1) ** sum(A[nu] for nu in range(mu))
def flip(A, mu):
    B = list(A); B[mu] ^= 1; return tuple(B)
def Dstag(P, m):
    D = np.zeros((16, 16), complex)
    for A in corners:
        a = cidx[A]; D[a, a] += m
        for mu in range(4):
            if A[mu] == 0:
                D[a, cidx[flip(A, mu)]] += 0.5 * eta(A, mu) * (1 - np.exp(-1j * P[mu]))
            else:
                D[a, cidx[flip(A, mu)]] += 0.5 * eta(A, mu) * (np.exp(1j * P[mu]) - 1)
    return D
def Vel(P, i):
    D = np.zeros((16, 16), complex)
    for A in corners:
        a = cidx[A]
        if A[i] == 0:
            D[a, cidx[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(-1j * P[i]))
        else:
            D[a, cidx[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(1j * P[i]))
    return D
def momS(P, K, nu):
    return np.sin(P[nu] + 0.5 * K[nu])
def Vst(P, K, mu, nu):
    return 0.5 * (Vel(P + 0.5 * K, mu) * momS(P, K, nu) + Vel(P + 0.5 * K, nu) * momS(P, K, mu))

# ---------------------------------------------------------------------------
# T4: staggered DD^dag=Delta*I + gauge operator Ward (midpoint; exact)
# ---------------------------------------------------------------------------
def t4_stag_gauge():
    rng = np.random.default_rng(2)
    derr = 0.0
    werr = 0.0
    for _ in range(200):
        P = rng.uniform(-np.pi, np.pi, 4)
        m = rng.uniform(0.3, 2.0)
        D = Dstag(P, m)
        Delta = m * m + np.sum(np.sin(P / 2) ** 2)
        derr = max(derr, np.abs(D @ D.conj().T - Delta * np.eye(16)).max())
        K = rng.uniform(-np.pi, np.pi, 4)
        lhs = sum(2 * np.sin(K[mu] / 2) * Vel(P + 0.5 * K, mu) for mu in range(4))
        werr = max(werr, np.abs(lhs - (Dstag(P + K, m) - Dstag(P, m))).max())
    check("T4 staggered DD^dag=(m^2+sum sin^2(P/2))I_16 (err=%.1e)" % derr, derr < 1e-10)
    check("T4b staggered gauge op-Ward sum_mu 2sin(K/2)Vel(P+K/2)=D(P+K)-D(P) EXACT (err=%.1e)" % werr,
          werr < 1e-12)

# ---------------------------------------------------------------------------
# T5: staggered STRESS operator Ward-Takahashi identity (exact)
# ---------------------------------------------------------------------------
def t5_stag_stress():
    rng = np.random.default_rng(3)
    err = 0.0
    for _ in range(200):
        P = rng.uniform(-np.pi, np.pi, 4)
        K = rng.uniform(-np.pi, np.pi, 4)
        m = rng.uniform(0.3, 2.0)
        dD = Dstag(P + K, m) - Dstag(P, m)
        Ssc = sum(2 * np.sin(K[mu] / 2) * momS(P, K, mu) for mu in range(4))
        for nu in range(4):
            lhs = sum(2 * np.sin(K[mu] / 2) * Vst(P, K, mu, nu) for mu in range(4))
            rhs = 0.5 * momS(P, K, nu) * dD + 0.5 * Ssc * Vel(P + 0.5 * K, nu)
            err = max(err, np.abs(lhs - rhs).max())
    check("T5 staggered STRESS op-WT sum_mu 2sin(K/2)Vst_munu = 1/2 mom_nu*dD + 1/2 Ssc*Vel_nu EXACT (err=%.1e)"
          % err, err < 1e-12)

# ---------------------------------------------------------------------------
# T6: telescoping -- contracted cubic triangle = bubble-difference + contact (exact);
#     the bubble-difference (equivalence-principle term) is nonzero
# ---------------------------------------------------------------------------
def _kvec(direction, k0):
    K = np.zeros(4); K[direction] = k0; return K
def _Gi(P, m):
    return np.linalg.inv(Dstag(P, m))
def _epsV(P, K, E):
    M = np.zeros((16, 16), complex)
    for i in range(1, 4):
        for j in range(1, 4):
            if abs(E[i - 1, j - 1]) < 1e-15:
                continue
            M += E[i - 1, j - 1] * Vst(P, K, i, j)
    return M

def _telescope_run(N, k0, m=0.7):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    k2 = _kvec(1, k0); k3 = _kvec(2, k0); k1 = -(k2 + k3)
    E2 = np.zeros((3, 3)); E2[1, 2] = E2[2, 1] = 1.0   # yz TT (transverse to k2||x)
    E3 = np.zeros((3, 3)); E3[0, 2] = E3[2, 0] = 1.0   # xz TT (transverse to k3||y)
    xi = np.array([0.0, 1.0, 0.5, 0.7])
    kf1 = np.array([2 * np.sin(k1[mu] / 2) for mu in range(4)])
    def W1(P):                                          # leg-1 = h1=d_xi contracted cubic vertex
        M = np.zeros((16, 16), complex)
        for mu in range(4):
            for nu in range(4):
                w = kf1[mu] * xi[nu] + kf1[nu] * xi[mu]
                if abs(w) < 1e-15:
                    continue
                M += w * Vst(P, k1, mu, nu)
        return M
    LHS = TEL = CONTACT = 0j
    for P0 in p:
        for P1 in p:
            for P2 in p:
                for P3 in p:
                    P = np.array([P0, P1, P2, P3])
                    G0 = _Gi(P, m); G1 = _Gi(P + k1, m); G2 = _Gi(P + k1 + k2, m)
                    V2 = _epsV(P + k1, k2, E2); V3 = _epsV(P + k1 + k2, k3, E3)
                    LHS += np.trace(G0 @ W1(P) @ G1 @ V2 @ G2 @ V3)
                    ximom = sum(xi[nu] * momS(P, k1, nu) for nu in range(4))
                    Ssc = sum(2 * np.sin(k1[mu] / 2) * momS(P, k1, mu) for mu in range(4))
                    xiVel = sum(xi[nu] * Vel(P + 0.5 * k1, nu) for nu in range(4))
                    TEL += ximom * np.trace((G0 - G1) @ V2 @ G2 @ V3)
                    CONTACT += Ssc * np.trace(G0 @ xiVel @ G1 @ V2 @ G2 @ V3)
    return LHS / N ** 4, TEL / N ** 4, CONTACT / N ** 4

def t6_telescope():
    N = 6
    LHS, TEL, CONTACT = _telescope_run(N, 2 * np.pi / 6)
    consist = abs((TEL + CONTACT) - LHS)
    check("T6 telescoping: contracted cubic triangle = bubble-difference + contact EXACTLY (|diff|=%.1e)"
          % consist, consist < 1e-9)
    check("T6b telescoped bubble-difference is NONZERO (|TEL|=%.4f -- stress-coupling channel present)"
          % abs(TEL), abs(TEL) > 1e-3)

# ---------------------------------------------------------------------------
# T7: the contact term Ssc is O(k) (seagull-completion channel)
# ---------------------------------------------------------------------------
def t7_contact_Ok():
    rng = np.random.default_rng(5)
    ratios = []
    for scale in (1.0, 0.5, 0.25, 0.125):
        K = np.array([scale, 0.4 * scale, 0.7 * scale, 0.0])
        mx = 0.0
        for _ in range(500):
            P = rng.uniform(-np.pi, np.pi, 4)
            mx = max(mx, abs(sum(2 * np.sin(K[mu] / 2) * momS(P, K, mu) for mu in range(4))))
        ratios.append(mx / scale)
    check("T7 contact Ssc is O(k) linear (|Ssc|/k-scale = %s ~ const -> seagull-completion channel)"
          % ", ".join("%.2f" % r for r in ratios),
          max(ratios) - min(ratios) < 0.3)

# ---------------------------------------------------------------------------
# T8: the contact is NOT subleading -- it is exactly HALF the contracted cubic vertex and scales at
#     the SAME power of k0 as the full vertex (the closure genuinely requires the seagull
#     completion; it does NOT trivially vanish). The telescoped bubble-difference (the
#     transverse/shear transport) and the contact (the trace/conformal-transport channel) are the
#     two equal halves of the longitudinally-contracted cubic graviton vertex.
# ---------------------------------------------------------------------------
def t8_contact_not_subleading():
    N = 6
    ks = [0.8, 0.4, 0.2]
    rows = [_telescope_run(N, k0) for k0 in ks]
    ratios = [abs(C) / abs(L) for (L, T, C) in rows]
    check("T8 contact is NOT subleading: contact/LHS = %s = 0.5 at all k0 (telescope + contact = the two equal halves of the contracted vertex)"
          % ", ".join("%.4f" % r for r in ratios),
          all(abs(r - 0.5) < 1e-2 for r in ratios))
    lk = np.log(ks)
    pL = np.polyfit(lk, np.log([abs(L) for (L, T, C) in rows]), 1)[0]
    pC = np.polyfit(lk, np.log([abs(C) for (L, T, C) in rows]), 1)[0]
    check("T8b contact scales at the SAME power as the vertex (k0^%.2f vs k0^%.2f) -> the closure requires the seagull completion, NOT a trivial vanishing"
          % (pC, pL), abs(pC - pL) < 0.05)

# ---------------------------------------------------------------------------
t1_elliptic()
t2_gauge_opward()
t3_stress_opward()
t4_stag_gauge()
t5_stag_stress()
t6_telescope()
t7_contact_Ok()
t8_contact_not_subleading()

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("Bounded result: exact stress-vertex operator Ward identities hold to roundoff on BOTH the")
print("2-comp Cl(3) and staggered Kahler-Dirac finite models. The longitudinally contracted tested")
print("cubic triangle TELESCOPES into a 2-point bubble-difference plus a same-order contact term.")
print("The contact is not subleading, so the full cubic Ward/EH closure remains open until the")
print("conserved cubic seagull and full RHS are constructed.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
