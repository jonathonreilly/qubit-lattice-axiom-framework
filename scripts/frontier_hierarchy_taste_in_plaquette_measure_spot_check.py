#!/usr/bin/env python3
"""Spot-check runner: tastes in the plaquette measure and the hierarchy readout.

Companion to the 2026-09-30 corrigenda on

    docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md
    docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md

Claims reproduced here (all SAME-FAMILY checks, small lattice; none of them
is a certificate, a retained result, or an audit verdict):

  [A] The declared readout map  v(P) = M_Pl (7/8)^(1/4) (1/(4 pi))^16 P^(-4)
      has elasticity -4.  A plaquette shift dP moves the readout by
      -4 dP / P to first order, so any |dP| above ~0.004 moves it by more
      than 100 times the quoted +0.0255 % comparator residual.

  [P] Plaquette point estimate from the repository's own April 2026
      production ensembles (outputs/alpha_s_wilson_loop_production/,
      12^3x24, 16^3x32, 24^3x48, 500 configurations each, beta = 6, 1x1
      space-time Wilson loops = plaquettes on 3 of the 6 plane
      orientations): recomputed here with a Madras-Sokal error.  It lies
      about 3e-4 above the licensed 0.5934.  This is a POINT ESTIMATE with
      its source, not a certificate (no infinite-volume fit, no grade-4
      budget) and not a replacement of the license.

  [C] Counting: the u_0-degree 16 of the minimal-block determinant equals
      the number of Grassmann components per colour of ONE staggered field
      (16 = 4 spin x 4 taste).  Attaching one coupling factor per Dirac
      flavour (taste) would give exponent 4, not 16.

  [G] Exact gauge-algebra checks that fix the sign and size of the
      determinant's coupling to the plaquette (hopping expansion:
      ln det(m + K) contains + (1/(8 m^4)) sum_p Re Tr U_p, so the
      leading local heavy-mass plaquette term has positive coefficient; on L=4 a winding term also contributes).

  [M] Monte Carlo spot check (own code; NOT the wall-campaign HMC): SU(3)
      Wilson gauge beta = 6 on a periodic 4^4 lattice, with fermion time APBC, quenched Metropolis
      ensemble re-weighted by det(D)^Ns of the one-component staggered
      operator (Ns = 1 is ONE staggered field = 4 tastes, unrooted;
      Ns = 1/4 and 1/2 are 1 and 2 tastes by rooting).  Reports the
      first-order slope cov(P, ln det) per staggered field, the
      re-weighted plaquette shift dP at 1 and 2 tastes, and the readout
      v(0.5934 + dP).  Re-weighting is NOT reliable at 4 tastes on this
      lattice (effective sample ~ 1), so the 4-taste row is the linear
      response only; the wall-campaign HMC value (dP = +0.0212(11), 214 GeV)
      is quoted for reference and not rerun.  Scope: 4^4 only, m = 0.1, dP is
      a same-volume difference added to the quoted infinite-volume value; the
      infinite-volume shift, the rooting, and the light-mass limit are NOT
      checked here.

Deterministic (fixed seeds); sections [A], [P], [C] need numpy only, sections
[G] and [M] also need numba and scipy.  Runtime about two minutes.
Exit code 0 iff FAIL=0.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "outputs/alpha_s_wilson_loop_production/ensemble_12x12x12x24_unsmeared.json",
    "outputs/alpha_s_wilson_loop_production/ensemble_16x16x16x32_unsmeared.json",
    "outputs/alpha_s_wilson_loop_production/ensemble_24x24x24x48_unsmeared.json",
)

REPO_ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(tag: str, name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{'PASS' if cond else 'FAIL'}][{tag}] {name}" + (f"  ({detail})" if detail else ""))
    return cond


# ---------------------------------------------------------------------------
# Declared inputs (mirrors the honest-status note's B1/B2/B3b/D1)
# ---------------------------------------------------------------------------
P_LICENSED = 0.5934            # B1 licensed reuse number
M_PL = 1.2209e19               # B2 anchor (GeV)
N_EXP = 16                     # B3b exponent
ALPHA_BARE = 1.0 / (4.0 * math.pi)
QUOTED_RESIDUAL = 2.5513e-4    # the note's stated readout-vs-comparator residual (fraction)


def v_of_p(p: float) -> float:
    a_lm = ALPHA_BARE / p ** 0.25
    return M_PL * (7.0 / 8.0) ** 0.25 * a_lm ** N_EXP


# ---------------------------------------------------------------------------
# [A] readout arithmetic
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- [A] readout arithmetic (declared map; no data) ---")
    v0 = v_of_p(P_LICENSED)
    check("A", "v(0.5934) reproduces the note's C1 readout 246.282818 GeV",
          abs(v0 - 246.282818290129) < 1e-6, f"v = {v0:.9f}")
    h = 1e-6
    el = (math.log(v_of_p(P_LICENSED * (1 + h))) - math.log(v_of_p(P_LICENSED * (1 - h)))) / (
        math.log(1 + h) - math.log(1 - h))
    check("A", "elasticity d ln v / d ln P = -4", abs(el + 4.0) < 1e-6, f"{el:.9f}")
    # smallest |dP| that moves the readout by 100x the quoted residual (exact inversion)
    target = 100.0 * QUOTED_RESIDUAL
    dp_min = P_LICENSED * ((1.0 - target) ** (-0.25) - 1.0)
    check("A", "a plaquette shift of only ~0.004 already moves the readout by 100x the quoted residual",
          0.003 < dp_min < 0.005 and abs(v_of_p(P_LICENSED + dp_min) / v0 - (1 - target)) < 1e-12,
          f"dP_min = {dp_min:.5f}")
    # the B1 window of the note: +-0.0337 % on v <-> +-5e-5 on P
    win = abs(v_of_p(P_LICENSED + 5e-5) / v0 - 1.0)
    check("A", "the licensed 4-decimal half-step (5e-5) corresponds to a readout window of ~0.034 %",
          abs(win - 3.37e-4) < 2e-6, f"{win * 100:.4f} %")


# ---------------------------------------------------------------------------
# [P] repository April ensembles
# ---------------------------------------------------------------------------
def ms_error(w: np.ndarray) -> tuple[float, float, float]:
    n = len(w)
    a = w - w.mean()
    f = np.fft.rfft(a, 2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:n]
    ac /= ac[0]
    t = 0.5
    for k in range(1, n):
        t += ac[k]
        if k >= 5 * t:
            break
    err = w.std(ddof=1) / math.sqrt(n) * math.sqrt(max(2.0 * t, 1.0))
    return float(w.mean()), float(err), float(t)


def section_p():
    print("\n--- [P] plaquette point estimate from the repository's April 2026 ensembles ---")
    base = REPO_ROOT / "outputs" / "alpha_s_wilson_loop_production"
    res = []
    for tag in ("12x12x12x24", "16x16x16x32", "24x24x24x48"):
        path = base / f"ensemble_{tag}_unsmeared.json"
        if not path.exists():
            check("P", f"ensemble file present: {path.name}", False)
            return None
        d = json.loads(path.read_text())
        w = np.array(d["raw_wilson_loops"])[:, 0, 0]  # R = 1, T = 1
        ok_meta = abs(d["beta"] - 6.0) < 1e-12 and len(w) == 500
        m, e, t = ms_error(w)
        check("P", f"{tag}: 500 configurations at beta = 6; W(1,1) = {m:.6f} +/- {e:.6f} (tau_int {t:.2f})", ok_meta)
        res.append((m, e))
    mm = np.array([r[0] for r in res])
    ee = np.array([r[1] for r in res])
    wt = 1.0 / ee ** 2
    mean = float((wt * mm).sum() / wt.sum())
    err = float(1.0 / math.sqrt(wt.sum()))
    chi2 = float((wt * (mm - mean) ** 2).sum())
    sig = (mean - P_LICENSED) / err
    check("P", "three volumes agree (chi^2 < 6 for 2 dof)", chi2 < 6.0, f"chi^2 = {chi2:.2f}")
    check("P", "weighted mean is 0.59369(2)", abs(mean - 0.59369) < 5e-5 and 1e-5 < err < 4e-5,
          f"{mean:.6f} +/- {err:.6f}")
    check("P", "the point estimate lies above 0.5934 by ~3e-4 (> 8 sigma of its own error)",
          2.0e-4 < mean - P_LICENSED < 4.0e-4 and sig > 8.0, f"offset {mean - P_LICENSED:+.2e} = {sig:.1f} sigma")
    v = v_of_p(mean)
    shift = v / v_of_p(P_LICENSED) - 1.0
    print(f"        readout at this point estimate: {v:.3f} GeV ({shift * 100:+.3f} % vs the licensed-P readout)")
    check("P", "readout at the point estimate is ~0.2 % below the licensed-P readout, i.e. ~8x the quoted residual",
          -0.0025 < shift < -0.0015 and 6.0 < abs(shift) / QUOTED_RESIDUAL < 9.0)
    return mean, err


# ---------------------------------------------------------------------------
# [C] Grassmann-component counting on the minimal 2^4 block
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- [C] counting: what the u_0-degree 16 counts ---")
    sites = list(itertools.product((0, 1), repeat=4))
    idx = {s: i for i, s in enumerate(sites)}
    D = np.zeros((16, 16))
    for s in sites:
        for mu in range(4):
            eta = (-1) ** sum(s[:mu])
            for direction in (+1, -1):
                t = list(s)
                t[mu] += direction
                wrapped = t[mu] < 0 or t[mu] > 1
                t[mu] %= 2
                D[idx[s], idx[tuple(t)]] += direction * eta * (-1 if wrapped else 1) * 0.5
    check("C", "2^4 block operator (eta phases, all-antiperiodic): D^2 = -4 I", np.allclose(D @ D, -4 * np.eye(16)))
    m = 0.37
    ok = True
    degs = []
    for u in (0.5, 0.8, 1.3):
        ok &= abs(np.linalg.det(u * D + m * np.eye(16)) - (m * m + 4 * u * u) ** 8) < 1e-9 * (m * m + 4 * u * u) ** 8
    check("C", "det(u_0 D + m) = (m^2 + 4 u_0^2)^8", ok)
    d1 = abs(np.linalg.det(0.9 * D))
    d2 = abs(np.linalg.det(1.8 * D))
    deg = math.log(d2 / d1) / math.log(2.0)
    check("C", "u_0-degree of |det| at m = 0 is 16 = number of block sites = Grassmann components per colour",
          abs(deg - 16.0) < 1e-9 and D.shape[0] == 16, f"degree = {deg:.9f}")
    # free staggered operator on a periodic L = 4 torus: number of exact zero modes at m = 0
    L = 4
    n = L ** 4
    K = np.zeros((n, n))

    def ix(x):
        return (((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)) * L + (x[3] % L)

    for x in itertools.product(range(L), repeat=4):
        for mu in range(4):
            eta = (-1) ** sum(x[:mu])
            y = list(x)
            y[mu] += 1
            z = list(x)
            z[mu] -= 1
            K[ix(x), ix(y)] += 0.5 * eta
            K[ix(x), ix(z)] -= 0.5 * eta
    ev = np.linalg.eigvals(K)
    nzero = int(np.sum(np.abs(ev) < 1e-9))
    check("C", "free one-component staggered operator (periodic 4^4, m = 0) has exactly 16 zero modes",
          nzero == 16, f"{nzero} zero modes")
    n_spin = 2 ** (4 // 2)
    n_taste = nzero // n_spin
    check("C", "16 low-energy components = 4 spin components x 4 tastes (one staggered field = 4 Dirac flavours)",
          n_taste == 4 and n_spin * n_taste == 16, f"tastes = {n_taste}")
    print("        consequence: one coupling factor per Dirac flavour gives exponent 4 = 16/4, not 16;"
          " exponent 16 needs a factor per Grassmann component (the open B4 attachment, unchanged).")


# ---------------------------------------------------------------------------
# Lattice machinery for [G] and [M]  (own code)
# ---------------------------------------------------------------------------
try:
    from numba import njit

    HAVE_NUMBA = True
except Exception:  # pragma: no cover
    HAVE_NUMBA = False

    def njit(*a, **k):  # type: ignore
        def deco(f):
            return f

        return deco if not (len(a) == 1 and callable(a[0])) else a[0]


L4 = 4


@njit
def _shift(x, mu, s, L):
    y = x.copy()
    y[mu] = (y[mu] + s) % L
    return y


@njit
def _mm(A, B):
    C = np.zeros((3, 3), dtype=np.complex128)
    for i in range(3):
        for j in range(3):
            s = 0j
            for k in range(3):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C


@njit
def _dag(A):
    C = np.zeros((3, 3), dtype=np.complex128)
    for i in range(3):
        for j in range(3):
            C[i, j] = np.conj(A[j, i])
    return C


@njit
def _retr(A, B):
    s = 0.0
    for i in range(3):
        for k in range(3):
            s += (A[i, k] * B[k, i]).real
    return s


@njit
def _reunit(M):
    r0 = M[0].copy()
    r0 = r0 / np.sqrt(np.sum(np.abs(r0) ** 2))
    r1 = M[1] - np.sum(np.conj(r0) * M[1]) * r0
    r1 = r1 / np.sqrt(np.sum(np.abs(r1) ** 2))
    r2 = np.conj(np.cross(r0, r1))
    out = np.zeros((3, 3), dtype=np.complex128)
    out[0] = r0
    out[1] = r1
    out[2] = r2
    return out


@njit
def _staples(U, x, mu, L):
    A = np.zeros((3, 3), dtype=np.complex128)
    for nu in range(4):
        if nu == mu:
            continue
        xm = _shift(x, mu, 1, L)
        xn = _shift(x, nu, 1, L)
        xmn = _shift(xm, nu, -1, L)
        xnm = _shift(x, nu, -1, L)
        a = _mm(_mm(U[xm[0], xm[1], xm[2], xm[3], nu], _dag(U[xn[0], xn[1], xn[2], xn[3], mu])),
                _dag(U[x[0], x[1], x[2], x[3], nu]))
        b = _mm(_mm(_dag(U[xmn[0], xmn[1], xmn[2], xmn[3], nu]), _dag(U[xnm[0], xnm[1], xnm[2], xnm[3], mu])),
                U[xnm[0], xnm[1], xnm[2], xnm[3], nu])
        A += a + b
    return A


@njit
def _sweep(U, T, beta, nhit, L):
    nT = T.shape[0]
    x = np.zeros(4, dtype=np.int64)
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    x[0] = x0
                    x[1] = x1
                    x[2] = x2
                    x[3] = x3
                    for mu in range(4):
                        A = _staples(U, x, mu, L)
                        Uc = U[x0, x1, x2, x3, mu].copy()
                        for h in range(nhit):
                            k = np.random.randint(nT)
                            Un = _mm(T[k], Uc)
                            dS = (beta / 3.0) * (_retr(Un, A) - _retr(Uc, A))
                            if dS >= 0.0 or np.random.random() < np.exp(dS):
                                Uc = Un
                        U[x0, x1, x2, x3, mu] = _reunit(Uc)


@njit
def _avg_plaq(U, L):
    s = 0.0
    n = 0
    x = np.zeros(4, dtype=np.int64)
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    x[0] = x0
                    x[1] = x1
                    x[2] = x2
                    x[3] = x3
                    for mu in range(4):
                        for nu in range(mu + 1, 4):
                            xm = _shift(x, mu, 1, L)
                            xn = _shift(x, nu, 1, L)
                            a = _mm(U[x0, x1, x2, x3, mu], U[xm[0], xm[1], xm[2], xm[3], nu])
                            b = _mm(_dag(U[xn[0], xn[1], xn[2], xn[3], mu]), _dag(U[x0, x1, x2, x3, nu]))
                            s += _retr(a, b) / 3.0
                            n += 1
    return s / n


@njit
def _seed(s):
    np.random.seed(s)


@njit
def _build_K(U, L):
    N = 3 * L ** 4
    K = np.zeros((N, N), dtype=np.complex128)
    x = np.zeros(4, dtype=np.int64)
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    x[0] = x0
                    x[1] = x1
                    x[2] = x2
                    x[3] = x3
                    s = ((x0 * L + x1) * L + x2) * L + x3
                    for mu in range(4):
                        par = 0
                        for j in range(mu):
                            par += x[j]
                        eta = 1.0 if par % 2 == 0 else -1.0
                        xf = _shift(x, mu, 1, L)
                        t = ((xf[0] * L + xf[1]) * L + xf[2]) * L + xf[3]
                        bc = 1.0
                        if mu == 3 and x[3] == L - 1:
                            bc = -1.0  # antiperiodic in direction 3
                        Um = U[x0, x1, x2, x3, mu]
                        for a in range(3):
                            for b in range(3):
                                K[3 * s + a, 3 * t + b] += 0.5 * eta * bc * Um[a, b]
                                K[3 * t + b, 3 * s + a] -= 0.5 * eta * bc * np.conj(Um[a, b])
    return K


def random_table(n_pairs, eps, rng):
    import scipy.linalg as sla

    lam = np.zeros((8, 3, 3), dtype=complex)
    lam[0] = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    lam[1] = [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]
    lam[2] = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    lam[3] = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    lam[4] = [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]
    lam[5] = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    lam[6] = [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]
    lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    T = np.zeros((2 * n_pairs, 3, 3), dtype=complex)
    for i in range(n_pairs):
        a = rng.normal(size=8)
        V = sla.expm(1j * eps * sum(a[j] * lam[j] for j in range(8)))
        T[2 * i] = V
        T[2 * i + 1] = V.conj().T
    return T


def ln_det(U, m):
    K = _build_K(U, L4)
    sign, ld = np.linalg.slogdet(K + m * np.eye(K.shape[0]))
    return float(ld), complex(sign)


def thermalised_config(seed, nsweep, beta=6.0, hot=False):
    rng = np.random.default_rng(seed)
    T = random_table(100, 0.24, rng)
    _seed(seed)
    U = np.zeros((L4, L4, L4, L4, 4, 3, 3), dtype=np.complex128)
    if hot:
        for idx in np.ndindex(L4, L4, L4, L4, 4):
            M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
            U[idx] = _reunit(M)
    else:
        U[..., :, :] = np.eye(3)
    for _ in range(nsweep):
        _sweep(U, T, beta, 4, L4)
    return U, T


# ---------------------------------------------------------------------------
# [G] exact gauge-algebra checks
# ---------------------------------------------------------------------------
def sum_plaq_retr(U):
    return float(_avg_plaq(U, L4)) * 3.0 * 6 * L4 ** 4


def section_g():
    print("\n--- [G] exact gauge-algebra checks of the determinant's coupling to the plaquette ---")
    if not HAVE_NUMBA:
        check("DEPENDENCY", "numba required for decisive gauge/MC controls", False, "section unexecuted")
        return
    Ua, _ = thermalised_config(11, 40)
    Ub, _ = thermalised_config(12, 5, hot=True)
    Ka, Kb = _build_K(Ua, L4), _build_K(Ub, L4)
    check("G", "K = hopping part of D is anti-Hermitian", np.abs(Ka + Ka.conj().T).max() < 1e-13)
    # gauge invariance of ln det
    rng = np.random.default_rng(3)
    G = np.zeros((L4, L4, L4, L4, 3, 3), dtype=complex)
    for idx in np.ndindex(L4, L4, L4, L4):
        G[idx] = _reunit(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    Ug = np.zeros_like(Ua)
    for idx in np.ndindex(L4, L4, L4, L4):
        for mu in range(4):
            y = list(idx)
            y[mu] = (y[mu] + 1) % L4
            Ug[idx + (mu,)] = G[idx] @ Ua[idx + (mu,)] @ G[tuple(y)].conj().T
    l0, s0 = ln_det(Ua, 0.1)
    l1, _ = ln_det(Ug, 0.1)
    check("G", "ln det(m + K) is gauge invariant; det is real positive", abs(l0 - l1) < 1e-9 and abs(s0 - 1) < 1e-9,
          f"{l0:.9f} vs {l1:.9f}")
    # free-field ln det against the analytic momentum sum
    Uf = np.zeros_like(Ua)
    Uf[..., :, :] = np.eye(3)
    lf, _ = ln_det(Uf, 0.1)
    ks = [2 * np.pi * np.arange(L4) / L4] * 3 + [2 * np.pi * (np.arange(L4) + 0.5) / L4]
    tot = 0.0
    for a in ks[0]:
        for b in ks[1]:
            for c in ks[2]:
                for d in ks[3]:
                    tot += math.log(0.01 + math.sin(a) ** 2 + math.sin(b) ** 2 + math.sin(c) ** 2 + math.sin(d) ** 2)
    check("G", "free-field ln det matches (3 colours) x (1/2) sum_k ln(m^2 + sum sin^2 k)", abs(lf - 1.5 * tot) < 1e-8,
          f"{lf:.8f} vs {1.5 * tot:.8f}")
    # Tr K^4 = const - (1/2) sum_p Re Tr U_p + (1/2) sum_lines s_mu Re Tr P_line, where the last term is the
    # four-step closed path that winds once around a periodic L = 4 direction (s_mu = -1 in the antiperiodic
    # direction); it is absent for L > 4 and irrelevant for the plaquette coefficient.
    def poly_sum(U):
        tot = 0.0
        for mu in range(4):
            sgn = -1.0 if mu == 3 else 1.0
            others = [i for i in range(4) if i != mu]
            for tr in itertools.product(range(L4), repeat=3):
                x = [0] * 4
                for i, o in enumerate(others):
                    x[o] = tr[i]
                P = np.eye(3, dtype=complex)
                for k in range(L4):
                    x[mu] = k
                    P = P @ U[tuple(x) + (mu,)]
                tot += sgn * np.trace(P).real
        return tot

    t4a = float(np.trace(np.linalg.matrix_power(Ka, 4)).real)
    t4b = float(np.trace(np.linalg.matrix_power(Kb, 4)).real)
    spa, spb = sum_plaq_retr(Ua), sum_plaq_retr(Ub)
    pa, pb = poly_sum(Ua), poly_sum(Ub)
    lhs = t4a - t4b
    rhs = -0.5 * (spa - spb) + 0.5 * (pa - pb)
    check("G", "Tr K^4 differs between two configurations by -(1/2) d(sum_p Re Tr U_p) + (1/2) d(winding Polyakov term)",
          abs(lhs - rhs) < 1e-8 * max(1.0, abs(lhs)), f"lhs {lhs:.6f}, rhs {rhs:.6f}")
    # large-mass regression: ln det(m + K) against the leading hopping-expansion form
    # (1/(8 m^4)) [ sum_p Re Tr U_p - winding Polyakov term ] over a small ensemble of configurations
    rng2 = np.random.default_rng(5)
    T2 = random_table(100, 0.24, rng2)
    _seed(5)
    Uc = np.zeros((L4, L4, L4, L4, 4, 3, 3), dtype=np.complex128)
    Uc[..., :, :] = np.eye(3)
    for _ in range(120):
        _sweep(Uc, T2, 6.0, 4, L4)
    mbig = 20.0
    lead, lds = [], []
    for _ in range(60):
        for _ in range(10):
            _sweep(Uc, T2, 6.0, 4, L4)
        lead.append((sum_plaq_retr(Uc) - poly_sum(Uc)) / (8.0 * mbig ** 4))
        lds.append(ln_det(Uc, mbig)[0])
    A = np.vstack([np.array(lead), np.ones(len(lead))]).T
    slope = float(np.linalg.lstsq(A, np.array(lds), rcond=None)[0][0])
    check("G", "at m = 20 the regression slope of ln det on the leading hopping-expansion form is 1 (corrections O(m^-2))",
          0.97 < slope < 1.01, f"slope = {slope:.4f}")
    print("        => at heavy mass, ln det(m + K) = const + [plaquette - signed winding]/(8 m^4) + O(m^-6).")
    print("        The local plaquette coefficient is positive; this is not all-mass monotonicity.")


# ---------------------------------------------------------------------------
# [M] Monte Carlo spot check
# ---------------------------------------------------------------------------
def jackknife(fun, arrays, blocks):
    n = len(arrays[0])
    full = fun(*arrays)
    vals = []
    for b in blocks:
        mask = np.ones(n, bool)
        mask[b] = False
        vals.append(fun(*[a[mask] for a in arrays]))
    vals = np.array(vals)
    nb = len(blocks)
    return float(full), float(math.sqrt((nb - 1) / nb * np.sum((vals - vals.mean()) ** 2)))


def section_m(n_chain=3, n_meas=500, spacing=10, mass=0.1):
    print("\n--- [M] Monte Carlo spot check (own code): quenched 4^4 ensemble re-weighted by det(D)^Ns ---")
    if not HAVE_NUMBA:
        check("DEPENDENCY", "numba required for decisive gauge/MC controls", False, "section unexecuted")
        return None
    t0 = time.time()
    Pch, Lch = [], []
    for c in range(n_chain):
        U, T = thermalised_config(2000 + c, 300, hot=(c % 2 == 1))
        P, LD = [], []
        for i in range(n_meas):
            for _ in range(spacing):
                _sweep(U, T, 6.0, 4, L4)
            P.append(_avg_plaq(U, L4))
            LD.append(ln_det(U, mass)[0])
        Pch.append(np.array(P[10:]))
        Lch.append(np.array(LD[10:]))
    print(f"        {n_chain} chains x {n_meas} configurations, spacing {spacing} sweeps, m = {mass}, "
          f"{time.time() - t0:.0f} s")
    P = np.concatenate(Pch)
    Lc = np.concatenate(Lch)
    blocks = []
    off = 0
    for a in Pch:
        edges = np.linspace(0, len(a), 21).astype(int)
        for i in range(20):
            blocks.append(np.arange(off + edges[i], off + edges[i + 1]))
        off += len(a)
    pq, pq_e = jackknife(lambda p: p.mean(), [P], blocks)
    check("M", "quenched 4^4 plaquette in the range of the earlier codes (0.5960-0.5985)", 0.5960 < pq < 0.5985,
          f"{pq:.5f} +/- {pq_e:.5f}")
    def chain_mean_err(a):
        nb_ = 10
        parts = np.array_split(a, nb_)
        return a.mean(), float(np.std([q.mean() for q in parts], ddof=1) / math.sqrt(nb_))

    (m0, e0), (m1, e1_) = chain_mean_err(Pch[0]), chain_mean_err(Pch[1])
    diff = abs(m0 - m1)
    comb = math.sqrt(e0 ** 2 + e1_ ** 2)
    check("M", "cold-start and hot-start chains agree within 3 combined sigma", diff < 3.0 * comb,
          f"|diff| = {diff:.2e}, combined sigma = {comb:.2e}")
    slope, se = jackknife(lambda p, l: np.cov(p, l)[0, 1], [P, Lc], blocks)
    check("M", "first-order slope cov(P, ln det) per staggered field is positive at > 4 sigma", slope > 4 * se,
          f"{slope:.4f} +/- {se:.4f}")
    out = {}
    for Ns, label in ((0.25, "1 taste (rooted)"), (0.5, "2 tastes (rooted)")):
        def dp(p, l, Ns=Ns):
            w = np.exp(Ns * (l - l.mean()))
            return (p * w).sum() / w.sum() - p.mean()

        val, e = jackknife(dp, [P, Lc], blocks)
        w = np.exp(Ns * (Lc - Lc.mean()))
        ess = w.sum() ** 2 / (w ** 2).sum()
        v = v_of_p(P_LICENSED + val)
        shift = v / v_of_p(P_LICENSED) - 1.0
        print(f"        Ns = {Ns:<4} {label:20s} dP = {val:+.4f} +/- {e:.4f}  (ESS {ess:.0f}/{len(Lc)})"
              f"   readout v(0.5934 + dP) = {v:.1f} GeV ({shift * 100:+.1f} %)")
        out[Ns] = (val, e, v, shift, ess)
    # 4 tastes = one full staggered field: re-weighting from the quenched ensemble is NOT reliable here
    # (effective sample size ~ 1), so only the linear-response value is reported.
    v_lin = v_of_p(P_LICENSED + slope)
    print(f"        Ns = 1    4 tastes (unrooted)  linear response only: dP ~ {slope:+.4f}"
          f"   readout {v_lin:.1f} GeV ({(v_lin / v_of_p(P_LICENSED) - 1) * 100:+.1f} %)"
          "  [re-weighting unreliable at Ns = 1; the wall-campaign HMC gives dP = +0.0212(11) -> 214 GeV, not rerun here]")
    dp1, e1, v1, s1, ess1 = out[0.25]
    dp2, e2, v2, s2, ess2 = out[0.5]
    check("M", "1 taste: dP is positive at > 5 sigma and the readout shift exceeds 100x the quoted residual",
          dp1 > 5 * e1 and abs(s1) > 100 * QUOTED_RESIDUAL, f"{dp1:+.4f} +/- {e1:.4f}, {v1:.1f} GeV")
    print(f"        (2-taste re-weighting has effective sample {ess2:.0f} of {len(Lc)} here: informational only, no gate;"
          " the 19,840-configuration run of the correction gave +0.0119(11), readout 227 GeV)")
    check("M", "the Ns=0 slope extrapolation at Ns=1 exceeds 100x the residual; not a controlled four-taste estimate or bound",
          abs(v_lin / v_of_p(P_LICENSED) - 1.0) > 100 * QUOTED_RESIDUAL, f"{v_lin:.1f} GeV")
    return out


def main():
    print("Spot check: tastes in the plaquette measure and the hierarchy readout")
    print("(same-family check on a small lattice; not a certificate, no audit status)")
    section_a()
    section_p()
    section_c()
    section_g()
    section_m()
    print("\nSCOPE: 4^4 lattice, m = 0.1, dP is a same-volume difference; infinite-volume shift, rooting and the")
    print("       light-mass limit are not checked here; the April ensembles give a point estimate, not a certificate.")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
