"""Full finite-k channel table of the W metric Hessian in the Ward-selected stress scheme
(native elliptic Dirac), with the vertex-identification bridge derived from log|det D[h]|.

BUILDS the named-open items of two landed rows:
  - UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K (yz TT bubble +; open: full Hessian/contact terms,
    full symmetric vertex + diffeomorphism Ward, E_g/T_2g spin-2 isotropy, magnitude, chiral control).
  - the conserved-vertex + diamagnetic-seagull runner (transversality O(k0)->O(k0^3); its stated open
    bridge: "identification of this runner-defined vertex/seagull with the complete metric Hessian of W").
And it asks whether the supplied opposite-signed curvature comparator of the degenerate-supermetric
no-go (#3220 row: V_trace=-k^2/2, V_TT=+k^2/2, SUPPLIED there) is INDUCED natively by W at finite k.

CHECKS:
  X0  convention pin: the declared position-space base operator has symbol i sigma.sin p + m (elliptic).
  X1  ellipticity pin (native iD elliptic; landed control).
  X2  IDENTIFICATION (load-bearing bridge DERIVED, not asserted): a DECLARED local vielbein link coupling
      D[h]: hop weight (sigma_nu + sum_alpha H_{alpha nu} h(x_mid) sigma_alpha)/2 forward, minus backward
      (h at link midpoints), has its EXACT second variation of W = log|det D[h]| (position space, explicit
      matrices, plus an independent log|det| second difference) EQUAL to the momentum-space bubble with the
      midpoint vertex V_H(q,k) = (i/2) sum_{alpha nu} H_{alpha nu} sigma_alpha sin(qbar_nu), qbar = q+k/2.
      => the naive-type stress vertex IS the exact W metric Hessian of a declared local metric coupling
      (linear coupling => NO seagull in this scheme).
  X3  SCHEME RELATION: V_cons - V_naive = (i/2) sum H_{alpha nu} sigma_alpha (cos(qbar_alpha)-1) sbar_nu,
      a LOCAL improvement term (numerically exact at random (q,k)); the declared-metric scheme FAILS
      transversality (landed T3 reproduced); conserved+seagull is O(k0^3)-transverse (landed T4
      reproduced). Ward-selected scheme = declared metric coupling + local improvement + local seagull
      (lattice analogue of Callan-Coleman-Jackiw stress improvement).
  X4  FULL CHANNEL TABLE (new): unit-Frobenius-norm channel slopes at finite k (k || x): TT {yz,
      (yy-zz)/sqrt2}, gauge-longitudinal {xy, xz, xx} (h = k_(a xi_b) for k||x), transverse trace
      (yy+zz)/sqrt2, full trace delta/sqrt3 -- in BOTH schemes.
  X5  spin-2 sector: BOTH TT channels positive in the conserved scheme; E_g/T_2g anisotropy MEASURED
      (named-open item): k-stable and persistent in the accessible scan, an honest negative.
  X6  diffeo direction: gauge-channel slopes are NOT suppressed in either scheme (measured lattice
      diffeo-breaking of the induced action at O(k^2); the seagull fixes the longitudinal CONTACT only).
  X7  the #3220 comparator: NOT induced -- trace stiffness positive (same sign as TT), and (X7b) the
      transverse trace-vs-shear splitting is ZERO at machine precision on checked grids. The tested
      one-loop W schemes do not induce the supplied GR sign comparator.
  X8  mass scan {0.5,1,1.5,2} + BZ-size convergence.
  X9  scheme-robustness of the TT sign + induced stiffness magnitude (lattice units; scale-reference
      primitive a^-1 = M_Pl gives the units bridge -- units remark only).

Comparators (Sakharov induced gravity; Adler-Zee; CCJ improvement) are cited as context; every number is
computed here. No PDG/fitted value.
"""
from __future__ import annotations
import warnings

import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
SIG = [sx, sy, sz]
I2 = np.eye(2, dtype=complex)
PREF = 1j  # native elliptic anti-Hermitian iD (landed convention)


def Hmat(d):
    H = np.zeros((3, 3))
    for (a, b), v in d.items():
        H[a, b] += v
        if a != b:
            H[b, a] += v
    return H


# unit-Frobenius-norm channels (k along x)
CHANNELS = {
    "TT_yz":   Hmat({(1, 2): 1.0}) / np.sqrt(2),
    "TT_E":    Hmat({(1, 1): 1.0, (2, 2): -1.0}) / np.sqrt(2),
    "GAU_xy":  Hmat({(0, 1): 1.0}) / np.sqrt(2),
    "GAU_xz":  Hmat({(0, 2): 1.0}) / np.sqrt(2),
    "GAU_xx":  Hmat({(0, 0): 1.0}),
    "TR_S":    Hmat({(1, 1): 1.0, (2, 2): 1.0}) / np.sqrt(2),
    "TR_full": Hmat({(0, 0): 1.0, (1, 1): 1.0, (2, 2): 1.0}) / np.sqrt(3),
}


# ---------------------------------------------------------------- momentum-space machinery (vectorized)
def G_stack(q, m):
    s = np.sin(q)
    den = m * m + (s ** 2).sum(1)
    G = (m * I2)[None, :, :] - 1j * (s[:, 0, None, None] * sx + s[:, 1, None, None] * sy
                                     + s[:, 2, None, None] * sz)
    return G / den[:, None, None]


def V_H(q, k, H, scheme):
    """vertex for symmetric H: (i/2) sum_{alpha,nu} H[alpha,nu] sigma_alpha * factor(q,k).
    scheme 'mid':   factor = sin(qbar_nu)                        (declared midpoint vielbein coupling)
    scheme 'naive': factor = sbar_nu = sin(qbar_nu) cos(k_nu/2)  (declared end-average coupling; landed naive)
    scheme 'cons':  factor = cos(qbar_alpha) * sbar_nu           (landed conserved velocity x momentum)"""
    qb = q + 0.5 * k[None, :]
    sqb = np.sin(qb)
    sb = sqb * np.cos(0.5 * k)[None, :]
    cqb = np.cos(qb)
    out = np.zeros((q.shape[0], 2, 2), complex)
    for al in range(3):
        for nu in range(3):
            if H[al, nu] == 0.0:
                continue
            if scheme == "mid":
                f = sqb[:, nu]
            elif scheme == "naive":
                f = sb[:, nu]
            else:
                f = cqb[:, al] * sb[:, nu]
            out += (0.5 * PREF * H[al, nu]) * np.asarray(SIG[al])[None, :, :] * f[:, None, None]
    return out


# diamagnetic seagull (landed basis: S = PREF*(-B0+B1+B5)), vectorized, contracted with H twice
def _kron(a, b):
    return 1.0 if a == b else 0.0


def _term(q, kind, i, j, k, l):
    s, c = np.sin(q), np.cos(q)
    if kind == 0:
        return _kron(i, k) * np.asarray(SIG[i])[None, :, :] * (s[:, i] * s[:, j] * s[:, l])[:, None, None]
    if kind == 1:
        return _kron(i, k) * np.asarray(SIG[i])[None, :, :] * (c[:, i] * c[:, j] * s[:, l])[:, None, None]
    return _kron(j, l) * np.asarray(SIG[i])[None, :, :] * (c[:, i] * s[:, j] * c[:, k])[:, None, None]


def _sym4(q, kind, i, j, k, l):
    v = 0
    for (ii, jj) in ((i, j), (j, i)):
        for (kk, ll) in ((k, l), (l, k)):
            v = v + _term(q, kind, ii, jj, kk, ll) + _term(q, kind, kk, ll, ii, jj)
    return v / 8.0


def Seagull_comp(q, i, j, k, l):
    return PREF * (-_sym4(q, 0, i, j, k, l) + _sym4(q, 1, i, j, k, l) + _sym4(q, 2, i, j, k, l))


def Seagull_H(q, H):
    out = np.zeros((q.shape[0], 2, 2), complex)
    for i in range(3):
        for j in range(3):
            if H[i, j] == 0.0:
                continue
            for k in range(3):
                for l in range(3):
                    if H[k, l] == 0.0:
                        continue
                    out += H[i, j] * H[k, l] * Seagull_comp(q, i, j, k, l)
    return out


def bz(N):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    QX, QY, QZ = np.meshgrid(p, p, p, indexing="ij")
    return np.stack([QX.ravel(), QY.ravel(), QZ.ravel()], axis=1)


def Pi_H(H, kx, m, N, scheme, seagull):
    q = bz(N)
    k = np.array([kx, 0.0, 0.0])
    Gq = G_stack(q, m)
    Gqk = G_stack(q + k[None, :], m)
    VA = V_H(q, k, H, scheme)
    VB = V_H(q + k[None, :], -k, H, scheme)
    t = np.einsum("mij,mjk,mkl,mli->", Gq, VA, Gqk, VB)
    if seagull:
        t = t - np.einsum("mij,mji->", Gq, Seagull_H(q, H))
    return t / N ** 3


def slope_H(H, m, N, scheme, seagull, nk=1):
    k1 = nk * 2 * np.pi / N
    return ((Pi_H(H, k1, m, N, scheme, seagull) - Pi_H(H, 0.0, m, N, scheme, seagull))
            / (2 - 2 * np.cos(k1))).real


# ---------------------------------------------------------------- landed component-convention reproduction
def V_landed(q, k, c, d, scheme):
    """landed component vertices (their exact formulas; diagonal doubled relative to V_H with E_cc)."""
    H = Hmat({(min(c, d), max(c, d)): 1.0})
    if c == d:
        H = H * 2.0  # their V(c,c) = PREF sigma_c (.) = 2x the single-H_cc entry of V_H
    return V_H(q, k, H, scheme)


def trans_residual(kvec, N, m=1.0, scheme="cons", seagull=False):
    q = bz(N)
    kf = np.array([2 * np.sin(kvec[a] / 2) for a in range(3)])
    nzi = [a for a in range(3) if abs(kf[a]) > 1e-12]
    Gq = G_stack(q, m)
    Gqk = G_stack(q + kvec[None, :], m)
    worst = 0.0
    for j in range(3):
        for k_ in range(3):
            for l in range(3):
                acc = 0j
                for i in nzi:
                    VA = V_landed(q, kvec, i, j, scheme)
                    VB = V_landed(q + kvec[None, :], -kvec, k_, l, scheme)
                    bub = np.einsum("mij,mjk,mkl,mli->", Gq, VA, Gqk, VB)
                    sg = 0j
                    if seagull:
                        # verbatim landed pairing: one component seagull per (ij),(kl) channel pair
                        sg = np.einsum("mij,mji->", Gq, Seagull_comp(q, i, j, k_, l))
                    acc += kf[i] * (bub - sg)
                worst = max(worst, abs(acc) / N ** 3)
    return worst


# ---------------------------------------------------------------- position-space exact (X2)
def build_D_pos(L, m, H, kx, amp):
    """D[h] with h_{alpha nu}(x_mid) = amp * H[alpha,nu] * cos(kx * x_mid), midpoint scheme.
    Base: hop weight +sigma_nu/2 forward, -sigma_nu/2 backward (=> D(p) = i sigma.sin p + m, elliptic).
    Amplitude convention: each e^{+-ikx} Fourier component then carries amplitude amp*H/2, matching the
    momentum vertex V_H per unit Fourier amplitude => d2W/damp2 = -2 L^3 Pi_H(k) exactly."""
    Nn = L ** 3
    D = np.zeros((Nn, 2, Nn, 2), complex)
    def idx(x, y, z):
        return ((x % L) * L + (y % L)) * L + (z % L)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x, y, z)
                D[i, :, i, :] += m * I2
                for nu, dv in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                    jp = idx(x + dv[0], y + dv[1], z + dv[2])
                    jm = idx(x - dv[0], y - dv[1], z - dv[2])
                    xm_p = x + (0.5 if nu == 0 else 0.0)
                    xm_m = (x - dv[0]) + (0.5 if nu == 0 else 0.0)
                    Wp = SIG[nu].astype(complex).copy()
                    Wm = SIG[nu].astype(complex).copy()
                    for al in range(3):
                        if H[al, nu] != 0.0:
                            Wp = Wp + amp * H[al, nu] * np.cos(kx * xm_p) * SIG[al]
                            Wm = Wm + amp * H[al, nu] * np.cos(kx * xm_m) * SIG[al]
                    D[i, :, jp, :] += 0.5 * Wp
                    D[i, :, jm, :] += -0.5 * Wm
    return D.reshape(2 * Nn, 2 * Nn)


def exact_hessian_pos(L, m, H, kx):
    D0 = build_D_pos(L, m, H, kx, 0.0)
    dD = build_D_pos(L, m, H, kx, 1.0) - D0
    G = np.linalg.inv(D0)
    M = G @ dD
    h_tr = -np.trace(M @ M).real
    eps = 1e-4
    def lad(amp):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            s, ld = np.linalg.slogdet(build_D_pos(L, m, H, kx, amp))
        return ld
    h_fd = (lad(eps) - 2 * lad(0.0) + lad(-eps)) / eps ** 2
    return h_tr, h_fd


def main() -> int:
    print("FULL FINITE-k CHANNEL TABLE OF THE W METRIC HESSIAN (Ward-selected scheme), native elliptic Dirac")
    print("=" * 100)
    m = 1.0

    # ---- X0 convention pin: position-space base operator IS the elliptic iD (symbol check) ----
    L = 4
    D0 = build_D_pos(L, m, np.zeros((3, 3)), 0.0, 0.0)
    p0 = np.array([2 * np.pi / L, 0.0, 0.0])
    phase = np.zeros(L ** 3, complex)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                phase[((x % L) * L + (y % L)) * L + (z % L)] = np.exp(1j * p0[0] * x)
    Dsym = 1j * sx * np.sin(p0[0]) + m * I2
    ok_x0 = True
    for s_ in range(2):
        e = np.zeros(2, complex); e[s_] = 1.0
        w = (phase[:, None] * e[None, :]).reshape(-1)
        r = (D0 @ w).reshape(L ** 3, 2)
        pred = phase[:, None] * Dsym[:, s_][None, :]
        if not np.allclose(r, pred, atol=1e-12):
            ok_x0 = False
    check("X0 (convention pin): the declared position-space base operator has symbol i sigma.sin p + m "
          "(the native ELLIPTIC operator; a spurious i on the hop would silently build the non-elliptic "
          "landed control)", ok_x0, "plane-wave symbol check exact at p=(2pi/L,0,0), both spin components")

    # ---- X1: ellipticity pin ----
    q = bz(16)
    s2 = (np.sin(q) ** 2).sum(1)
    check("X1 (landed pin): native iD elliptic, det = m^2 + |sin q|^2 > 0 on all BZ modes",
          float((m * m + s2).min()) > 0, f"min det factor = {float((m*m+s2).min()):.3f}")

    # ---- X2: identification -- exact position-space Hessian == midpoint-vertex bubble ----
    L = 6
    kx = 2 * np.pi / L
    ok_all = True
    det_lines = []
    for nm in ["TT_yz", "GAU_xy", "TT_E"]:
        H = CHANNELS[nm]
        h_tr, h_fd = exact_hessian_pos(L, m, H, kx)
        # momentum prediction: d2W/damp2 = -2 * L^3 * Pi_mid(k)  (cos-mode cross terms; 2k != 0 mod 2pi)
        pred = (-2.0 * (L ** 3) * Pi_H(H, kx, m, L, "mid", seagull=False)).real
        okA = abs(h_tr - h_fd) < 1e-4 * max(1.0, abs(h_tr))
        okB = abs(h_tr - pred) < 1e-8 * max(1.0, abs(h_tr))
        ok_all = ok_all and okA and okB
        det_lines.append(f"{nm}: exactTr={h_tr:+.6f} logdetFD={h_fd:+.6f} momPred={pred:+.6f}")
    check("X2 (IDENTIFICATION, the load-bearing bridge DERIVED): exact second variation of W=log|det D[h]| "
          "for the DECLARED local vielbein link coupling (position space; explicit -Tr(GdDGdD) AND an "
          "independent log|det| second difference) EQUALS the momentum-space bubble with the midpoint "
          "vertex V_H = (i/2) sum H_{alpha nu} sigma_alpha sin(qbar_nu) -- the naive-type vertex IS the "
          "exact W metric Hessian of a declared local metric coupling (linear => NO seagull in this scheme)",
          ok_all, "; ".join(det_lines))

    # ---- X3: scheme relation + landed Ward facts ----
    rng = np.random.default_rng(7)
    worst = 0.0
    for _ in range(100):
        qq = rng.uniform(-np.pi, np.pi, (1, 3))
        kk = rng.uniform(-np.pi, np.pi, 3)
        H = rng.uniform(-1, 1, (3, 3)); H = (H + H.T) / 2
        lhs = V_H(qq, kk, H, "cons") - V_H(qq, kk, H, "naive")
        qb = qq + 0.5 * kk[None, :]
        sb = np.sin(qb) * np.cos(0.5 * kk)[None, :]
        rhs = np.zeros((1, 2, 2), complex)
        for al in range(3):
            for nu in range(3):
                rhs += (0.5 * PREF * H[al, nu]) * np.asarray(SIG[al])[None, :, :] * \
                       ((np.cos(qb[:, al]) - 1.0) * sb[:, nu])[:, None, None]
        worst = max(worst, float(np.abs(lhs - rhs).max()))
    r_naive = trans_residual(np.array([2 * np.pi / 6, 0, 0]), 12, scheme="naive")
    cubs = []
    for k0 in (2 * np.pi / 12, 2 * np.pi / 9, 2 * np.pi / 6):
        r = trans_residual(np.array([k0, 0, 0]), 12, scheme="cons", seagull=True)
        cubs.append(r / k0 ** 3)
    check("X3 (scheme relation): V_cons - V_naive = local improvement (i/2) sum H sigma_alpha "
          "(cos(qbar_alpha)-1) sbar_nu (exact at random (q,k,H)); naive FAILS transversality (landed T3 "
          "reproduced); cons+seagull residual is CUBIC in k0 (landed T4 reproduced, absolute spread "
          "tolerance 0.002 as landed) -- Ward-selected scheme = declared metric coupling + LOCAL "
          "improvement + LOCAL seagull (lattice CCJ improvement)",
          worst < 1e-12 and r_naive > 0.05 and (max(cubs) - min(cubs)) < 0.002,
          f"improvement-identity err={worst:.1e}; naive residual={r_naive:.3f}; "
          f"cons+sg res/k0^3: {', '.join('%.4f' % c for c in cubs)} (~const)")

    # ---- X4: FULL CHANNEL TABLE (the seagull is k-independent => cancels exactly in slopes) ----
    N = 16
    sg_with = slope_H(CHANNELS["TT_yz"], m, N, "cons", True)
    sg_wout = slope_H(CHANNELS["TT_yz"], m, N, "cons", False)
    tab_c = {nm: slope_H(H, m, N, "cons", False) for nm, H in CHANNELS.items()}
    tab_n = {nm: slope_H(H, m, N, "naive", False) for nm, H in CHANNELS.items()}
    print("\n  unit-Frobenius-norm channel slopes at k=2pi/16, m=1 (induced action; healthy TT = positive):")
    print("    channel       Ward-selected     naive(metric)")
    for nm in CHANNELS:
        print(f"    {nm:8s}    {tab_c[nm]:+12.6f}     {tab_n[nm]:+12.6f}")
    check("X4 (the full finite-k channel table): computed in BOTH schemes; the local seagull is "
          "k-independent and cancels EXACTLY in slope differences Pi(k)-Pi(0) (verified), so the slope "
          "table is seagull-normalization-independent",
          all(np.isfinite(v) for v in tab_c.values()) and all(np.isfinite(v) for v in tab_n.values())
          and abs(sg_with - sg_wout) < 1e-12,
          f"slope(seagull on) - slope(off) = {sg_with - sg_wout:.2e}")

    # ---- X5: spin-2 pair + isotropy trend ----
    tt1, tt2 = tab_c["TT_yz"], tab_c["TT_E"]
    check("X5a (spin-2 sector beyond the landed yz channel): BOTH unit-norm TT channels positive "
          "(Ward-selected scheme)", tt1 > 0 and tt2 > 0, f"yz={tt1:+.6f}, (yy-zz)/sqrt2={tt2:+.6f}")
    ksplits = []
    for NN in (16, 24, 32):
        a = slope_H(CHANNELS["TT_yz"], m, NN, "cons", False)
        b = slope_H(CHANNELS["TT_E"], m, NN, "cons", False)
        ksplits.append((2 * np.pi / NN, abs(a - b) / max(abs(a), abs(b))))
    k_stable = max(s for _, s in ksplits) - min(s for _, s in ksplits) < 0.05
    msplits = []
    for mm, NN in ((1.0, 16), (0.5, 24), (0.25, 48)):
        a = slope_H(CHANNELS["TT_yz"], mm, NN, "cons", False)
        b = slope_H(CHANNELS["TT_E"], mm, NN, "cons", False)
        msplits.append((mm, abs(a - b) / max(abs(a), abs(b))))
    m_persists = all(s > 0.3 for _, s in msplits)
    check("X5b (E_g/T_2g spin-2 isotropy, named-open item, MEASURED -- an honest negative): the "
          "T_2g(yz)-vs-E_g((yy-zz)) split is k-STABLE (a property of the O(k^2) stiffness constants -- "
          "genuine cubic anisotropy of the tested 'elastic' constants, NOT a small finite-k artifact) and "
          "PERSISTS (even grows) toward lighter mass at accessible lattice sizes: the tested spin-2 "
          "stiffness has O(1) cubic anisotropy -- the induced action does NOT "
          "deliver an emergent-SO(3)-isotropic graviton kinetic term by itself. (Deep continuum scaling "
          "k << m << 1 with q_min << m is beyond this runner -- bounded statement.)",
          k_stable and m_persists,
          "k-scan(m=1): " + "; ".join(f"k={k0:.3f}: {s:.3f}" for k0, s in ksplits)
          + " | m-scan: " + "; ".join(f"m={mm}: {s:.3f}" for mm, s in msplits))

    # ---- X6: gauge channels (measured diffeo-breaking at the slope level) ----
    g_c = max(abs(tab_c["GAU_xy"]), abs(tab_c["GAU_xz"]), abs(tab_c["GAU_xx"]))
    g_n = max(abs(tab_n["GAU_xy"]), abs(tab_n["GAU_xz"]), abs(tab_n["GAU_xx"]))
    gauge_ratio_c = g_c / abs(tt1)
    gauge_ratio_n = g_n / abs(tab_n["TT_yz"])
    check("X6 (diffeo direction, MEASURED -- an honest negative): pure-gauge channels {xx,xy,xz} "
          "(h=k_(a xi_b), k||x) are NOT suppressed relative to TT in EITHER scheme at the slope level. "
          "The Ward selection fixes the longitudinal CONTACT structure of Pi (transversality residual "
          "O(k0^3), X3), but the gauge-channel k^2 slopes remain O(TT): this is the measured lattice "
          "diffeomorphism-breaking of the induced action at O(k^2) -- the finite-k face of the missing "
          "emergent-diffeo bridge, now quantified",
          gauge_ratio_c > 0.5 and gauge_ratio_n > 0.05,
          f"Ward-selected: max|gauge|/TT = {gauge_ratio_c:.3f}; naive(metric): {gauge_ratio_n:.3f}")

    # ---- X7: the #3220 comparator -- the supplied pattern is NOT induced (sharpening) ----
    same_sign = (tt1 > 0) and (tab_c["TR_S"] > 0) and (tab_c["TR_full"] > 0)
    check("X7 (the #3220 comparator question ANSWERED, a finite-k SHARPENING of the no-go): the "
          "degenerate-supermetric no-go SUPPLIED an opposite-signed pair (V_TT>0, V_trace<0). The induced "
          "finite-k table in the Ward-selected scheme gives trace stiffness POSITIVE -- SAME sign as TT. "
          "So the k=0 trace=shear same-sign degeneracy persists on the checked finite-k grids: the "
          "opposite-signed GR (Lichnerowicz) channel pair is NOT induced by the one-loop W in this "
          "tested scheme, and the no-go's "
          "supplied comparator remains supplied (the curvature-sign structure must come from elsewhere, "
          "e.g. the geometric/Regge route). The naive-scheme full-trace negative is gauge-contaminated "
          "(full trace contains the pure-gauge xx at k||x), not a counter-example.",
          same_sign,
          f"Ward-selected: TT={tt1:+.6f}, transverse-trace={tab_c['TR_S']:+.6f}, "
          f"full-trace={tab_c['TR_full']:+.6f} (all same sign); naive full-trace={tab_n['TR_full']:+.6f}")
    # X7b: the transverse trace-vs-shear SPLITTING (the structure GR needs) -- measured directly.
    # Within the k-transverse 2x2 scalar block {E=(yy-zz)/sqrt2, S=(yy+zz)/sqrt2}, GR/Lichnerowicz needs a
    # LARGE OPPOSITE-SIGNED splitting; the splitting here = 2 x (cross stiffness Pi_{yy,zz} slope).
    split_c = tab_c["TR_S"] - tab_c["TT_E"]
    split_n = tab_n["TR_S"] - tab_n["TT_E"]
    split_c2 = (slope_H(CHANNELS["TR_S"], 0.7, 12, "cons", False, nk=2)
                - slope_H(CHANNELS["TT_E"], 0.7, 12, "cons", False, nk=2))
    check("X7b (transverse trace-vs-shear splitting, the GR-needed structure, MEASURED): in the conserved "
          "scheme the splitting is ZERO at MACHINE precision and at a second independent (N,m,k) point -- "
          "the k=0 trace=shear DEGENERACY persists on the checked finite-k grids (not just same-sign). "
          "Mechanism: the conserved vertex's per-component cos(qbar)*sin(qbar) factor is pi-periodic, "
          "so the compatible-grid q_y -> q_y + pi BZ shift flips the cross-term integrand sign and "
          "cancels Pi_{yy,zz}; the naive "
          "scheme's sin(qbar) factor is not pi-periodic, hence its small nonzero splitting (the contrast "
          "confirms the mechanism). In NEITHER scheme does the splitting approach the GR-required large "
          "opposite-sign structure.",
          abs(split_c) < 1e-12 and abs(split_c2) < 1e-12,
          f"conserved (TR_S - TT_E) = {split_c:+.2e} at (N16,m1,k=2pi/16) and {split_c2:+.2e} at "
          f"(N12,m0.7,k=4pi/12) (vs channel {tab_c['TT_E']:+.6f}); naive = {split_n:+.2e}")

    # ---- X8: mass scan + convergence ----
    mscan = [slope_H(CHANNELS["TT_yz"], mm, 14, "cons", False) for mm in (0.5, 1.0, 1.5, 2.0)]
    conv = [slope_H(CHANNELS["TT_yz"], 1.0, NN, "cons", False) for NN in (12, 16, 20)]
    check("X8 (mass scan + BZ convergence): Ward-selected TT slope positive for m in {0.5,1,1.5,2}, stable "
          "over N in {12,16,20}",
          all(s > 0 for s in mscan) and all(s > 0 for s in conv)
          and (max(conv) - min(conv)) < 0.1 * abs(np.mean(conv)),
          f"mass {['%+.5f' % s for s in mscan]}; BZ {['%+.5f' % s for s in conv]}")

    # ---- X9: scheme robustness + magnitude ----
    check("X9 (scheme robustness + magnitude): TT sign positive in BOTH the declared-metric and the "
          "Ward-selected schemes (sign scheme-robust; gauge/longitudinal channels scheme-sensitive); "
          "induced TT stiffness c_TT/a^2 in lattice units (scale-reference primitive a^-1 = M_Pl gives "
          "the units bridge; units remark only, no dimensionless physics granted)",
          tab_n["TT_yz"] > 0 and tt1 > 0,
          f"c_TT(Ward-selected, m=1) = {tt1:+.6f}; c_TT(naive/metric) = {tab_n['TT_yz']:+.6f}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (three findings, all bounded):\n"
        "  (1) IDENTIFICATION BRIDGE DERIVED: the naive-type vertex IS the exact W metric Hessian of a\n"
        "      declared local vielbein link coupling (verified against explicit log|det D[h]| in position\n"
        "      space, two independent ways); the Ward-selected conserved scheme = that coupling + an\n"
        "      exhibited LOCAL improvement term + the local seagull (lattice analogue of stress-tensor\n"
        "      improvement). The 'runner-defined vertex' mystery of the landed rows is resolved.\n"
        "  (2) SPIN-2 SECTOR EXTENDED, WITH AN HONEST NEGATIVE: both TT channels positive (scheme-robust,\n"
        "      mass-robust, BZ-convergent), BUT the E_g/T_2g stiffness anisotropy is O(1), k-STABLE, and\n"
        "      PERSISTS toward lighter mass -- the tested stiffness has O(1) cubic anisotropy, not an\n"
        "      emergent-isotropic graviton kinetic term.\n"
        "  (3) THE #3220 COMPARATOR IS NOT INDUCED (sharpening): the conserved-scheme induced trace\n"
        "      stiffness is POSITIVE -- same sign as TT -- and the transverse trace-vs-shear splitting is\n"
        "      ZERO at machine precision on checked grids: the k=0 trace=shear DEGENERACY persists in\n"
        "      this finite-BZ check. The opposite-signed GR/Lichnerowicz channel pair is not induced by\n"
        "      the one-loop W action in this tested scheme; the curvature-sign structure must come from\n"
        "      elsewhere, such as a geometric/Regge route, and the gauge channels are NOT suppressed at\n"
        "      the slope level in this finite-BZ check.\n"
        "  NET: in the tested native one-loop W schemes the induced action is a healthy-positive but\n"
        "      ANISOTROPIC, SAME-SIGN, gauge-unsuppressed elastic stiffness -- it does not reproduce the\n"
        "      Einstein/Lichnerowicz opposite-sign trace/TT comparator in this tested class.\n"
        "Scope: finite-BZ stiffness signs of the induced action for the native elliptic operator; NOT a\n"
        "continuum dispersion law; NOT a unique-coupling theorem (local improvement freedom exhibited, not\n"
        "eliminated); NOT full GR closure. No PDG/fitted value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
