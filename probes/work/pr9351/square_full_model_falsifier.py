#!/usr/bin/env python3
"""J:falsifier:PR9351 -- square microscopic spectral certificate: does the Schur reduction describe the microscopic model, and do the certificates hold?

Target claims (PR #9351, note SQUARE_MICROSCOPIC_SPECTRAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-27; supplied model of the parent note LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT):
 (1) the microscopic energies E of the two-record square sector (Hamiltonian H = delta eps^-4 [W + eps T_S + eps^2 C_S], eps^2 = x = delta/(K C), C = S(S+1)) solve
     F(E) psi = 0, F(E) = 4 K n^2 - delta Z^T R(E)^-1 Z - E (1 + 4x - lam), lam = x^2 E / delta, R_m = (1 - lam)(2 - lam) - 4 x d_m, d_m = 1 - m(m+1)/C,
     and the number of microscopic eigenvalues below E is the number of negative eigenvalues of F(E) (for lam < 1, (1 - lam)(2 - lam) > 4x);
 (2) the first-order operator has H0(n,n) = 4Kn^2 - 4 delta, H0(n+1,n) = -2 delta, H1(n,n) = 8 delta - 8 K n^2, H1(n+1,n) = 4 delta + 4 K n (n + 1);
 (3) for 0 <= x < 1/4, 4K(1 - 4x) ||n psi||^2 - 8 delta ||psi||^2 <= <psi, (H0 + x H1) psi> <= 4K ||n psi||^2; the tail resolvent obeys 0 <= Sigma(E) <= beta(E) Pi_boundary,
     beta = 4 delta^2 / (t_L - E) for H0 (t_L = 4K(L+1)^2 - 8 delta) and beta = t_L^2 / [4K(1 - 4x)(L+1)^2 - 8 delta - E] for H0 + x H1;
 (4) for K = 1 and delta = 1 or 15803623/500000, S = 20, 50, 120, the maximum absolute error over the first six excitation gaps of H0 + x H1 against the microscopic model is bounded by
     0.004987235265, 0.000136754425, 0.000004229203 (delta = 1) and 6.647658236470, 0.281239142371, 0.009192992163 (delta = 15803623/500000).
Machinery disjoint from the PR's runner (exact Fraction LDL counts on the reduced equation): (a) the full microscopic Hamiltonian is built here as an explicit matrix from the parent's
definitions (matter words, Gauss law, hop amplitudes sqrt(1 - E(E - 1)/C), F_a, C_S = sum_a [F_a^T F_a - D_(a,S) + D_(a,inf)] Q_a computed from those matrices, no use of the note's Schur block form),
and diagonalised; (b) the reduced equation (1) is solved independently by floating-point negative-eigenvalue counts and bisection; (c) (2) is checked symbolically from (1) with sympy; (d) the form bounds
and tail sandwiches are tested as matrix inequalities. Beyond the note's sizes: S up to 960 on the reduced equation, S = 240 on the full matrix. Floating point is labelled. Prints SUMMARY: and, only if a falsifier
fires, HIT:.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
import sympy as sp
from scipy.linalg import eigh, eigvalsh_tridiagonal

T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv
DELTAS = (1.0, 15803623 / 500000)
TABLE = {(1.0, 20): 0.004987235265, (1.0, 50): 0.000136754425, (1.0, 120): 0.000004229203,
         (15803623 / 500000, 20): 6.647658236470, (15803623 / 500000, 50): 0.281239142371, (15803623 / 500000, 120): 0.009192992163}


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def fire(msg):
    FIRED.append(msg)


# ------------------------------------------------------------------------------------------------ (a) the full microscopic Hamiltonian
def full_model(S, K, delta):
    """Two positive records on the 4-cycle A = {0, 2}, B = {1, 3}, edges oriented A -> B: e0 = (0,1), e1 = (0,3), e2 = (2,1), e3 = (2,3). Fields E = (E01, E03, E21, E23) in [-S, S], Gauss law
    div E = q - 1_A (outflow q_a - 1 at A, inflow -q_b at B). H = delta eps^-4 [W + eps T + eps^2 C_S] with T = -sum_a (F_a + F_a^T) and C_S from its definition."""
    C = S * (S + 1)
    x = delta / (K * C)                                    # eps^2
    A = (0, 2); edges = [(0, 1), (0, 3), (2, 1), (2, 3)]
    states = []
    for q in itertools.product((0, 1), repeat=4):
        if sum(q) != 2:
            continue
        for n in range(-S, S + 1):
            E = (n, q[0] - 1 - n, -q[1] - n, q[2] - 1 + q[1] + n)
            # Gauss law at all four vertices
            assert E[0] + E[1] == q[0] - 1 and E[2] + E[3] == q[2] - 1 and E[0] + E[2] == -q[1] and E[1] + E[3] == -q[3]
            if all(-S <= e <= S for e in E):
                states.append((q, E))
    idx = {s: i for i, s in enumerate(states)}
    N = len(states)
    F = {a: np.zeros((N, N)) for a in A}                   # F[a][j, i]: amplitude of |j> in F_a |i>
    Ddiag = {a: np.zeros(N) for a in A}; Dinf = {a: np.zeros(N) for a in A}
    Wd = np.zeros(N); Q = {a: np.ones(N) for a in A}
    for i, (q, E) in enumerate(states):
        Wd[i] = sum(1 - q[a] for a in A)
        for a in A:
            other = [c for c in A if c != a]                # graph distance 2 in the 4-cycle: the other A vertex is within distance two
            Q[a][i] = float(np.prod([q[c] for c in other]))
            Dinf[a][i] = q[a] * sum(1 - q[b] for (aa, b) in edges if aa == a)
        for k, (a, b) in enumerate(edges):
            if q[a] == 1 and q[b] == 0:
                amp2 = 1 - E[k] * (E[k] - 1) / C            # k = -q_a = -1 for the tail of the oriented edge
                Ddiag[a][i] += amp2
                if amp2 > 1e-14:
                    q2 = list(q); q2[a] = 0; q2[b] = 1; E2 = list(E); E2[k] -= 1
                    F[a][idx[(tuple(q2), tuple(E2))], i] += np.sqrt(amp2)
    T = -sum(F[a] + F[a].T for a in A)
    Cs = sum((F[a].T @ F[a] - np.diag(Ddiag[a]) + np.diag(Dinf[a])) @ np.diag(Q[a]) for a in A)
    H = (delta / x ** 2) * (np.diag(Wd) + np.sqrt(x) * T + x * Cs)
    return H, Cs, Wd, N


# ------------------------------------------------------------------------------------------------ (b) the reduced equation (1)
def F_tridiag(E, S, K, delta):
    C = S * (S + 1); x = delta / (K * C); lam = x * x * E / delta
    m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
    R = (1 - lam) * (2 - lam) - 4 * x * dm
    assert lam < 1 and R.min() > 0
    n = np.arange(-S, S + 1)
    dg = 4 * K * n.astype(float) ** 2 - E * (1 + 4 * x - lam)
    q = 4 * delta * dm ** 2 / R
    dg[m + S] -= q; dg[m + S + 1] -= q
    return dg, -q


def count_F(E, S, K, delta):
    dg, off = F_tridiag(E, S, K, delta)
    return int((eigvalsh_tridiagonal(dg, off) < 0).sum())


def reduced_levels(S, K, delta, nev=7):
    out = []
    for j in range(nev):
        b = -6 * delta - 5; step = 0.5
        while count_F(b, S, K, delta) < j + 1:
            b += step
        a = b - step
        while count_F(a, S, K, delta) >= j + 1:
            a -= step
        for _ in range(64):
            mid = (a + b) / 2
            if count_F(mid, S, K, delta) >= j + 1:
                b = mid
            else:
                a = mid
        out.append((a + b) / 2)
    return np.array(out)


def first_order_levels(S, K, delta, L=150, nev=7, rotor=False):
    C = S * (S + 1); x = 0.0 if rotor else delta / (K * C)
    n = np.arange(-L, L + 1).astype(float)
    dg = 4 * K * n ** 2 - 4 * delta + x * (8 * delta - 8 * K * n ** 2)
    off = -2 * delta + x * (4 * delta + 4 * K * n[:-1] * (n[:-1] + 1))
    return eigvalsh_tridiagonal(dg, off, select="i", select_range=(0, nev - 1))


def first_order_matrix(K, delta, x, N):
    n = np.arange(-N, N + 1).astype(float)
    dg = 4 * K * n ** 2 - 4 * delta + x * (8 * delta - 8 * K * n ** 2)
    off = -2 * delta + x * (4 * delta + 4 * K * n[:-1] * (n[:-1] + 1))
    return np.diag(dg) + np.diag(off, 1) + np.diag(off, -1), n


def run():
    K = 1.0
    # ---- (2) exact: first-order coefficients from (1)
    nn, x, Ks, dl, E = sp.symbols("n x K delta E")
    C = dl / (Ks * x)
    d = lambda m: 1 - m * (m + 1) / C
    lam = x ** 2 * E / dl
    R = lambda m: (1 - lam) * (2 - lam) - 4 * x * d(m)
    diag = 4 * (d(nn - 1) ** 2 / R(nn - 1) + d(nn) ** 2 / R(nn))              # (Z^T R^-1 Z)(n, n)
    adj = 4 * d(nn) ** 2 / R(nn)                                             # (Z^T R^-1 Z)(n, n + 1)
    scale = 1 + 4 * x - lam
    H_diag = sp.series((4 * Ks * nn ** 2 - dl * diag) / scale, x, 0, 2).removeO()
    H_adj = sp.series((-dl * adj) / scale, x, 0, 2).removeO()
    e_diag = sp.expand(H_diag - ((4 * Ks * nn ** 2 - 4 * dl) + x * (8 * dl - 8 * Ks * nn ** 2)))
    e_adj = sp.expand(H_adj - (-2 * dl + x * (4 * dl + 4 * Ks * nn * (nn + 1))))
    N0d = sp.series(4 * (d(nn - 1) ** 2 + d(nn) ** 2), x, 0, 2).removeO()
    e_N = sp.expand(N0d - (8 + x * (-16 * (Ks / dl) * nn ** 2)))
    e_Na = sp.expand(sp.series(4 * d(nn) ** 2, x, 0, 2).removeO() - (4 + x * (-8 * (Ks / dl) * nn * (nn + 1))))
    ok2 = e_diag.subs(E, 0) == 0 and e_adj.subs(E, 0) == 0 and sp.simplify(e_diag) == 0 and sp.simplify(e_adj) == 0 and e_N == 0 and e_Na == 0
    check("(2) exact (sympy): expanding the reduced equation (1) to first order in x at fixed n (E fixed, lam = O(x^2)) gives H0 + x H1 with H0(n,n) = 4Kn^2 - 4 delta, H0(n+1,n) = -2 delta, "
          "H1(n,n) = 8 delta - 8 K n^2, H1(n+1,n) = 4 delta + 4 K n(n+1), and N = Z^T Z = N0 + x N1 with N0 = (8, 4), N1 = (-16 (K/delta) n^2, -8 (K/delta) n(n+1))", ok2,
          f"residuals: diag {sp.simplify(e_diag)}, adjacent {sp.simplify(e_adj)}, N diag {e_N}, N adjacent {e_Na}; {time.time() - T0:.0f} s")
    if not ok2:
        fire("(2) first-order coefficients differ from the expansion of (1)")

    # ---- full model against (1)
    cases = [(dl_, S) for S in (20, 50) for dl_ in DELTAS] + ([] if DRY else [(dl_, 120) for dl_ in DELTAS])
    cache = {}
    okC, parts = True, []
    for dl_, S in cases:
        H, Cs, Wd, N = full_model(S, K, dl_)
        onP = np.abs(Cs[Wd == 0][:, Wd == 0] - 4 * np.eye(int((Wd == 0).sum()))).max()
        offP = np.abs(Cs[Wd > 0]).max() if (Wd > 0).any() else 0.0
        offP = max(offP, np.abs(Cs[:, Wd > 0]).max())
        ev = eigh(H, eigvals_only=True, subset_by_index=(0, 6))
        er = reduced_levels(S, K, dl_)
        d_ = float(np.abs(ev - er).max())
        cache[(dl_, S)] = (ev, er, H)
        tol = 2e-8 if S <= 50 else 2e-6
        okC &= onP < 1e-12 and offP < 1e-12 and d_ < tol
        parts.append(f"delta {dl_:.6g}, S {S}: dim {N}, C_S = 4 on W = 0 (dev {onP:.0e}) and 0 elsewhere (dev {offP:.0e}), first seven levels full vs reduced max difference {d_:.1e} (float noise limit of the large-entry full matrix)")
    check("(1a) the explicit full microscopic matrix (built from the parent's definitions, C_S computed as sum_a [F_a^T F_a - D_S + D_inf] Q_a) has C_S = 4 on W = 0 and 0 on W = 1, 2, and its lowest seven eigenvalues equal "
          "the reduced equation's roots", okC, "; ".join(parts) + f"; {time.time() - T0:.0f} s")
    if not okC:
        fire("the full microscopic matrix and the reduced equation disagree")
    # inertia: count_F(E) = number of eigenvalues below E of the full matrix, on a grid of E away from eigenvalues
    okI, nchk, worst = True, 0, 0.0
    for dl_, S in cases[:4]:
        ev_all = eigh(cache[(dl_, S)][2], eigvals_only=True)
        for Eg in np.linspace(-6 * dl_ - 3, 40.0, 220 if not DRY else 60):
            if np.min(np.abs(ev_all - Eg)) < 1e-6:
                continue
            c_full = int((ev_all < Eg).sum())
            c_red = count_F(Eg, S, K, dl_)
            nchk += 1
            if c_full != c_red:
                okI = False; worst = Eg
    check(f"(1b) the negative index of F(E) equals the number of eigenvalues of the full matrix below E at {nchk} test energies (S = 20, 50, both delta)", okI, f"mismatch at E = {worst}" if not okI else "no mismatch")
    if not okI:
        fire("negative index of F(E) differs from the eigenvalue count of the full matrix")

    # ---- (4) the table
    okT, rows = True, []
    for (dl_, S), bound in TABLE.items():
        if DRY and S == 120:
            continue
        er = reduced_levels(S, K, dl_)
        ea = first_order_levels(S, K, dl_, 150); ea2 = first_order_levels(S, K, dl_, 250)
        conv = float(np.abs(ea - ea2).max())
        err = float(np.abs((er[1:] - er[0]) - (ea[1:] - ea[0])).max())
        slack = bound - err
        okT &= conv < 1e-10 and slack >= -1e-9 and slack < 2e-8
        rows.append(f"delta {dl_:.6g} S {S}: error {err:.12f} <= bound {bound:.12f} (slack {slack:.1e})")
    check("(4) the six certified bounds: the maximum error over the first six excitation gaps of H0 + x H1 (independent floating-point roots of (1)) is at most the stated bound, with slack below 2e-8 "
          "(the intervals are 2e-9 and 4e-9 wide)", okT, "; ".join(rows) + f"; {time.time() - T0:.0f} s")
    if not okT:
        fire("a stated error bound is violated or not tight to the stated interval widths")

    # ---- (3) form bounds and tail sandwiches
    worst_lo = worst_hi = np.inf
    for K_, dl_ in ((1, 1), (1, 31.607246), (1, 0.1), (1, 1000.0), (0.01, 1)):
        for x_ in (1e-4, 1e-3, 0.01, 0.05, 0.1, 0.2, 0.24, 0.2499):
            Hm, n_ = first_order_matrix(K_, dl_, x_, 120)
            worst_lo = min(worst_lo, float(np.linalg.eigvalsh(Hm - np.diag(4 * K_ * (1 - 4 * x_) * n_ ** 2 - 8 * dl_)).min()) / (4 * K_ + 8 * dl_))
            worst_hi = min(worst_hi, float(np.linalg.eigvalsh(np.diag(4 * K_ * n_ ** 2) - Hm).min()) / (4 * K_ + 8 * dl_))
    check("(3a) the form bounds 4K(1 - 4x) n^2 - 8 delta <= H0 + x H1 <= 4K n^2 hold as matrix inequalities on 241-site truncations for 40 (K, delta, x) with x up to 0.2499", worst_lo > -1e-10 and worst_hi > -1e-10,
          f"smallest eigenvalue of (H - lower) / scale {worst_lo:.2e}, of (upper - H) / scale {worst_hi:.2e}")
    if not (worst_lo > -1e-10 and worst_hi > -1e-10):
        fire("a form bound of the note fails as a matrix inequality")
    okS, worst_s = True, []
    for dl_ in DELTAS:
        for S in (20, 50):
            C_ = S * (S + 1); x_ = dl_ / (K * C_)
            for corrected in (False, True):
                xx = x_ if corrected else 0.0
                Nmax = 400
                n_ = np.arange(-Nmax, Nmax + 1).astype(float)
                dg = 4 * K * n_ ** 2 - 4 * dl_ + xx * (8 * dl_ - 8 * K * n_ ** 2)
                off = -2 * dl_ + xx * (4 * dl_ + 4 * K * n_[:-1] * (n_[:-1] + 1))
                lev = first_order_levels(S, K, dl_, 200, rotor=not corrected)
                L = 20 if not corrected else 30
                keep = np.abs(n_) <= L
                # tail on the positive side: sites n = L + 1 .. Nmax; coupling t_L = off[index of (n = L)] between n = L and L + 1
                ip = int(np.where(n_ == L)[0][0])
                t_L = off[ip]
                tail = np.diag(dg[ip + 1:]) + np.diag(off[ip + 1:], 1) + np.diag(off[ip + 1:], -1)
                low = (4 * K * (1 - 4 * xx) * (L + 1) ** 2 - 8 * dl_) if corrected else (4 * K * (L + 1) ** 2 - 8 * dl_)
                for Ev in lev[:7]:
                    Sg = t_L ** 2 * np.linalg.solve(tail - Ev * np.eye(len(tail)), np.eye(len(tail))[:, 0])[0]
                    beta = (t_L ** 2 if corrected else 4 * dl_ ** 2) / (low - Ev)
                    okS &= (Sg >= -1e-12) and (Sg <= beta * (1 + 1e-9))
                    worst_s.append(Sg / beta)
    check("(3b) the tail sandwich 0 <= Sigma(E) <= beta(E) holds at the first seven levels of H0 (L = 20) and of H0 + x H1 (L = 30), S = 20, 50, both delta, with the note's beta (tail truncated at |n| = 400)",
          okS, f"largest Sigma/beta over all tested levels {max(worst_s):.4f}")
    if not okS:
        fire("the tail sandwich bound is violated")
    # certificate criterion in floats: counts of retained H_L - E and H_L - E - beta Pi agree at E_j +- 1e-9 (L = 20 rotor, L = 30 corrected)
    okK, nfail = True, 0
    for dl_ in DELTAS:
        for S in (20, 50) + (() if DRY else (120,)):
            C_ = S * (S + 1); x_ = dl_ / (K * C_)
            for corrected in (False, True):
                xx = x_ if corrected else 0.0
                L = 30 if corrected else 20
                n_ = np.arange(-L, L + 1).astype(float)
                dg = 4 * K * n_ ** 2 - 4 * dl_ + xx * (8 * dl_ - 8 * K * n_ ** 2)
                off = -2 * dl_ + xx * (4 * dl_ + 4 * K * n_[:-1] * (n_[:-1] + 1))
                Hm = np.diag(dg) + np.diag(off, 1) + np.diag(off, -1)
                lev = first_order_levels(S, K, dl_, 200, rotor=not corrected)
                t_L = -2 * dl_ * (1 - 2 * xx) + 4 * K * xx * L * (L + 1)
                low = (4 * K * (1 - 4 * xx) * (L + 1) ** 2 - 8 * dl_) if corrected else (4 * K * (L + 1) ** 2 - 8 * dl_)
                for j, Ev in enumerate(lev):
                    for sgn, expect in ((-1, j), (+1, j + 1)):
                        Ee = Ev + sgn * 1e-9
                        beta = (t_L ** 2 if corrected else 4 * dl_ ** 2) / (low - Ee)
                        Pi = np.zeros_like(Hm); Pi[0, 0] = Pi[-1, -1] = beta
                        c_lo = int((np.linalg.eigvalsh(Hm - Ee * np.eye(len(n_))) < 0).sum())
                        c_hi = int((np.linalg.eigvalsh(Hm - Ee * np.eye(len(n_)) - Pi) < 0).sum())
                        if not (c_lo == c_hi == expect):
                            okK = False; nfail += 1
    check("(3c) the infinite-rotor certificate criterion, in floats: at E_j -+ 1e-9 the negative indices of the retained matrices H_L - E and H_L - E - beta Pi agree and equal j and j + 1 (L = 20 for H0, L = 30 for H0 + x H1), "
          "for the six cases and the first seven levels", okK, f"{nfail} disagreements; {time.time() - T0:.0f} s")
    if not okK:
        fire("the retained-matrix count criterion fails at some endpoint")

    # ---- beyond the note's sizes
    Ss = (120, 240, 480, 960) if not DRY else (120, 240)
    okB, txt = True, []
    for dl_ in DELTAS:
        xs, e1, e0 = [], [], []
        for S in Ss:
            er = reduced_levels(S, K, dl_)
            ea = first_order_levels(S, K, dl_, 200); e_r = first_order_levels(S, K, dl_, 200, rotor=True)
            gm = er[1:] - er[0]
            xs.append(dl_ / (K * S * (S + 1)))
            e1.append(float(np.abs(gm - (ea[1:] - ea[0])).max())); e0.append(float(np.abs(gm - (e_r[1:] - e_r[0])).max()))
        k = min(len(xs), 3)
        s1 = np.polyfit(np.log(xs[:k]), np.log(e1[:k]), 1)[0]; s0 = np.polyfit(np.log(xs), np.log(e0), 1)[0]
        okB &= 1.9 < s1 < 2.1 and 0.9 < s0 < 1.1
        txt.append(f"delta {dl_:.6g}: S {Ss}: corrected-operator error slope in x {s1:.3f} (first {k} sizes; expected 2), rotor error slope {s0:.3f} (expected 1); errors {['%.3e' % v for v in e1]}")
    check("(5) beyond the note's sizes (S up to 960 on the reduced equation): the error of H0 + x H1 scales as x^2 and the error of the rotor H0 as x, as a first-order correction should", okB, "; ".join(txt) + f"; {time.time() - T0:.0f} s")
    if not okB:
        fire("scaling of the first-order error is not x^2")
    S2 = 240
    if not DRY:
        for dl_ in DELTAS:
            H, Cs, Wd, N = full_model(S2, K, dl_)
            ev = eigh(H, eigvals_only=True, subset_by_index=(0, 6))
            er = reduced_levels(S2, K, dl_)
            dd = float(np.abs(ev - er).max())
            check(f"(1c) beyond the note's size: the full microscopic matrix at S = 240, delta = {dl_:.6g} (dimension {N}) has its lowest seven eigenvalues equal to the reduced equation's roots", dd < 1e-5, f"max difference {dd:.1e}; {time.time() - T0:.0f} s")
            if dd >= 1e-5:
                fire(f"S = 240 full matrix disagrees with the reduced equation ({dd:.1e})")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9351 claim fails: " + "; ".join(FIRED))
        sys.exit(1)
    print("SUMMARY: no falsifier fired: an explicit full microscopic matrix built from the parent definitions reproduces the reduced equation's energies and eigenvalue counts, the first-order coefficients follow exactly "
          "from the reduced equation, the six stated error bounds hold with slack below the interval widths, the form bounds and tail sandwiches hold as matrix inequalities, and beyond the note's sizes "
          "the first-order error scales as x^2")


if __name__ == "__main__":
    run()
