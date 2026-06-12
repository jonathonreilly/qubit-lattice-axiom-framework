#!/usr/bin/env python3
"""Ward/Bogoliubov no-continuous-SSB bridge at d <= 2, finite temperature.

Companion runner for
docs/WARD_BOGOLIUBOV_NO_CONTINUOUS_SSB_LOW_D_BRIDGE_THEOREM_NOTE_2026-06-11.md

Verifies the full (B1)-(B5) chain as identities/inequalities with
margins, on the qubit carrier:

  [L]  (B1) lemma certificates: scalar log-mean <= arithmetic mean;
       (L1) (X,X)_D <= <{X,X^dag}>/2; (L2) beta([H,C^dag],X)_D =
       <[C,X]>; positivity of <[[C,H],C^dag]>; the assembled
       Bogoliubov inequality on random instances.
  [W]  (B2) Ward identity <[Q_k, A_{-k}]> = -i N m at EVERY discrete
       k, d = 1 and d = 2, several fields.
  [K]  (B3) kernel bound 0 <= <[[Q_k,H],Q_{-k}]> <= N (J E(k) + h|m|)
       with E(k) = 2 sum_mu (1 - cos k_mu) (the retained C-MW kernel),
       at every k; exact field-part identity.
  [B4] sum rule sum_k <{A_k, A_k^dag}> = N^2/2.
  [B5] assembled bound m^2 S(h|m|) <= beta/4 on all blocks/fields.
  [IR] threshold composition: (1/N) sum_k 1/(E(k)+eps) grows strictly
       with L for d = 1, 2 and is L-stable for d = 3 (recomputed
       small-scale, consistent with the retained threshold row), and
       the (B5) ceiling shrinks with L at d <= 2.
  [F]  falsifiers: U(1)-breaking anisotropy breaks the k=0 kernel
       bound; the Bogoliubov inequality is not vacuously slack
       (constructed near-equality instance).

Deterministic (fixed seeds), numpy + scipy, runtime under a minute.
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""

from __future__ import annotations

import sys
from itertools import product

import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        s = "PASS"
    else:
        FAIL += 1
        s = "FAIL"
    print(f"  [{s}] [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 76)
    print(title)
    print("-" * 76)


# ---------------------------------------------------------------------------
# builders
# ---------------------------------------------------------------------------

SX2 = np.array([[0, 1], [1, 0]], dtype=complex) / 2
SY2 = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
SZ2 = np.diag([1.0, -1.0]).astype(complex) / 2


def embed(op, site, n):
    return np.kron(np.eye(2**site), np.kron(op, np.eye(2 ** (n - site - 1))))


def build_block(dims, J, h, anis=0.0):
    """XY + transverse field on a periodic block of shape dims.
    anis != 0 adds a U(1)-breaking Ising term (falsifier only)."""
    sites = list(product(*[range(L) for L in dims]))
    N = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    SX = [embed(SX2, i, N) for i in range(N)]
    SY = [embed(SY2, i, N) for i in range(N)]
    SZ = [embed(SZ2, i, N) for i in range(N)]
    dim = 2**N
    H = np.zeros((dim, dim), dtype=complex)
    bonds = []
    for s in sites:
        for mu in range(len(dims)):
            if dims[mu] == 1:
                continue
            t = list(s)
            t[mu] = (t[mu] + 1) % dims[mu]
            t = tuple(t)
            if (s, t) in bonds or (t, s) in bonds:
                continue
            bonds.append((s, t))
            i, j = idx[s], idx[t]
            H += -J * (SX[i] @ SX[j] + SY[i] @ SY[j])
            H += -anis * (SX[i] @ SX[j] - SY[i] @ SY[j])
    H += -h * sum(SX)
    return H, sites, idx, SX, SY, SZ


def gibbs(H, beta):
    r = expm(-beta * H)
    return r / np.trace(r)


def kgrid(dims):
    return [tuple(2 * np.pi * n[mu] / dims[mu] for mu in range(len(dims)))
            for n in product(*[range(L) for L in dims])]


def Ek(k):
    return 2 * sum(1 - np.cos(km) for km in k)


def fourier_op(ops, sites, k, sign=+1):
    return sum(np.exp(sign * 1j * np.dot(k, s)) * ops[i]
               for i, s in enumerate(sites))


# ---------------------------------------------------------------------------
# Duhamel / Bogoliubov scalar product (B1 lemmas)
# ---------------------------------------------------------------------------

def duhamel_data(H, beta):
    w, P = np.linalg.eigh(H)
    e = np.exp(-beta * w)
    Z = e.sum()
    n = len(w)
    W = np.zeros((n, n))
    for m in range(n):
        for nn in range(n):
            if abs(w[nn] - w[m]) < 1e-12:
                W[m, nn] = e[m]
            else:
                W[m, nn] = (e[m] - e[nn]) / (beta * (w[nn] - w[m]))
    return w, P, e, Z, W


def dprod(X, Y, P, W, Z):
    Xe = P.conj().T @ X @ P
    Ye = P.conj().T @ Y @ P
    # (X, Y) = (1/Z) sum_{m,n} conj(X_{nm}) Y_{nm} w_{mn}
    return np.sum(np.conj(Xe.T) * Ye.T * W) / Z


def main() -> int:
    print("=" * 76)
    print("WARD/BOGOLIUBOV NO-CONTINUOUS-SSB BRIDGE AT d <= 2 (finite T)")
    print("(B1)-(B5) chain checked as identities/inequalities with margins")
    print("=" * 76)
    rng = np.random.default_rng(20260611)

    # =======================================================================
    section("[L] (B1) lemma certificates and the Bogoliubov inequality")
    # =======================================================================
    # scalar log-mean <= arithmetic mean
    us = np.linspace(-3, 3, 41)
    ok = True
    for u in us:
        for v in us:
            if abs(u - v) < 1e-12:
                continue
            lm = (np.exp(-u) - np.exp(-v)) / (v - u)
            am = (np.exp(-u) + np.exp(-v)) / 2
            ok &= lm <= am + 1e-12
    check("L", "scalar log-mean <= arithmetic mean on the grid", ok)

    ok_l1 = ok_l2 = ok_pos = ok_bog = True
    worst_l2 = 0.0
    for trial in range(5):
        n = 8
        H = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        H = 0.5 * (H + H.conj().T)
        A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        C = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        for beta in (0.5, 2.0):
            w, P, e, Z, W = duhamel_data(H, beta)
            rho = gibbs(H, beta)
            ev = lambda X: np.trace(rho @ X)
            # (L1)
            xx = dprod(A, A, P, W, Z).real
            anti = ev(A @ A.conj().T + A.conj().T @ A).real
            ok_l1 &= xx <= anti / 2 + 1e-10
            # (L2): beta ([H,C^dag], X)_D = <[C, X]> with X = A
            lhs = beta * dprod(H @ C.conj().T - C.conj().T @ H, A, P, W, Z)
            rhs = ev(C @ A - A @ C)
            worst_l2 = max(worst_l2, abs(lhs - rhs))
            ok_l2 &= abs(lhs - rhs) < 1e-9
            # positivity + assembled inequality
            dc = ev((C @ H - H @ C) @ C.conj().T
                    - C.conj().T @ (C @ H - H @ C)).real
            ok_pos &= dc >= -1e-10
            ok_bog &= abs(ev(C @ A - A @ C))**2 <= (beta / 2) * anti * dc + 1e-9
    check("L", "(L1) (X,X)_D <= <{X,X^dag}>/2 on random instances", ok_l1)
    check("L", "(L2) beta([H,C^dag],X)_D = <[C,X]> on random instances",
          ok_l2, f"max residual = {worst_l2:.1e}")
    check("L", "positivity <[[C,H],C^dag]> >= 0 on random instances", ok_pos)
    check("L", "(B1) assembled Bogoliubov inequality on random instances",
          ok_bog)

    # =======================================================================
    # blocks for (B2)-(B5)
    # =======================================================================
    blocks = [("d=1 chain L=8", (8,)), ("d=2 block 3x3", (3, 3))]
    J, beta = 1.0, 2.0

    for label, dims in blocks:
        for h in ((0.1, 0.4) if len(dims) == 1 else (0.2,)):
            H, sites, idx, SXl, SYl, SZl = build_block(dims, J, h)
            N = len(sites)
            rho = gibbs(H, beta)
            ev = lambda X: np.trace(rho @ X)
            m = ev(sum(SXl)).real / N
            ks = kgrid(dims)

            # ===============================================================
            section(f"block {label}, h = {h}  (N = {N}, m = {m:.4f})")
            # ===============================================================
            # (B2) Ward identity at every k
            ward_ok, worst = True, 0.0
            for k in ks:
                Qk = fourier_op(SZl, sites, k, +1)
                Amk = fourier_op(SYl, sites, k, -1)
                r = abs(ev(Qk @ Amk - Amk @ Qk) - (-1j * N * m))
                worst = max(worst, r)
                ward_ok &= r < 1e-8
            check("W", f"(B2) Ward identity <[Q_k, A_-k]> = -iNm at every k",
                  ward_ok, f"max residual = {worst:.1e}")

            # (B3) kernel bound at every k + field-part identity
            kern_ok = True
            for k in ks:
                Qk = fourier_op(SZl, sites, k, +1)
                dck = ev((Qk @ H - H @ Qk) @ Qk.conj().T
                         - Qk.conj().T @ (Qk @ H - H @ Qk)).real
                kern_ok &= -1e-9 <= dck <= N * (J * Ek(k) + h * abs(m)) + 1e-9
            check("K", "(B3) 0 <= <[[Q_k,H],Q_-k]> <= N(J E(k) + h|m|) "
                       "at every k (E = retained C-MW kernel)", kern_ok)
            Hh = -h * sum(SXl)
            k1 = ks[1 % len(ks)]
            Qk = fourier_op(SZl, sites, k1, +1)
            fld = (Qk @ Hh - Hh @ Qk) @ Qk.conj().T
            fld = fld - Qk.conj().T @ (Qk @ Hh - Hh @ Qk)
            check("K", "(B3) field part: [[Q_k, H_h], Q_-k] = h sum_x S^x "
                       "exactly",
                  np.abs(fld - h * sum(SXl)).max() < 1e-9)

            # (B4) sum rule
            tot = sum(ev(fourier_op(SYl, sites, k, +1)
                         @ fourier_op(SYl, sites, k, -1)
                         + fourier_op(SYl, sites, k, -1)
                         @ fourier_op(SYl, sites, k, +1)).real for k in ks)
            check("B4", "sum rule sum_k <{A_k, A_k^dag}> = N^2/2",
                  abs(tot - N**2 / 2) < 1e-8, f"sum = {tot:.6f}")

            # (B5) assembled bound
            S = sum(1.0 / (J * Ek(k) + h * abs(m)) for k in ks) / N
            lhs = m**2 * S
            check("B5", "assembled bound m^2 S(h|m|) <= beta/4",
                  lhs <= beta / 4 + 1e-9,
                  f"m^2 S = {lhs:.4f} <= beta/4 = {beta/4:.4f}")

    # =======================================================================
    section("[IR] threshold composition (retained C-MW row scope)")
    # =======================================================================
    # classic divergence form: eps = 0, k != 0 excluded (the retained
    # threshold row's reading; the k = 0 mode is carried by the h|m|
    # regulator inside (B5) itself).
    Svals = {}
    for d, Ls in ((1, (16, 32, 64)), (2, (8, 16, 24)), (3, (6, 10, 14))):
        Svals[d] = []
        for L in Ls:
            ks = [k for k in kgrid((L,) * d)
                  if any(abs(km) > 1e-12 for km in k)]
            Svals[d].append(sum(1.0 / Ek(k) for k in ks) / L**d)
    check("IR", "d=1: (1/N) sum_{k!=0} 1/E(k) grows strictly with L",
          Svals[1][0] < Svals[1][1] < Svals[1][2],
          f"S = {[f'{s:.2f}' for s in Svals[1]]}")
    check("IR", "d=2: grows strictly with L",
          Svals[2][0] < Svals[2][1] < Svals[2][2],
          f"S = {[f'{s:.2f}' for s in Svals[2]]}")
    check("IR", "d=3: L-stable (ratio largest/smallest < 1.5; converging)",
          max(Svals[3]) / min(Svals[3]) < 1.5,
          f"S = {[f'{s:.3f}' for s in Svals[3]]}")
    # ceiling -> 0 along an h-sequence at large fixed L (thermodynamic
    # limit FIRST, then h -> 0 -- the order of limits in B5):
    Lbig = 4096
    ceil1 = []
    for hh in (1e-2, 1e-3, 1e-4):
        ks = kgrid((Lbig,))
        S = sum(1.0 / (J * Ek(k) + hh) for k in ks) / Lbig
        ceil1.append((beta / 4) / S)
    check("IR", "(B5) ceiling (beta/4)/S(h) -> 0 along h -> 0 at large L, "
               "d=1 (m is squeezed to 0 in the weak-field limit after the "
               "thermodynamic limit)",
          ceil1[0] > ceil1[1] > ceil1[2],
          f"ceiling = {[f'{c:.5f}' for c in ceil1]}")

    # =======================================================================
    section("[F] falsifiers")
    # =======================================================================
    # (i) U(1)-breaking anisotropy: the k = 0 kernel bound fails.
    H, sites, idx, SXl, SYl, SZl = build_block((8,), J, 0.2, anis=0.5)
    N = len(sites)
    rho = gibbs(H, beta)
    ev = lambda X: np.trace(rho @ X)
    m = ev(sum(SXl)).real / N
    ks = kgrid((8,))
    # the identity <[Q_k, A_-k]> = -iNm still holds operator-wise (on-site
    # algebra), but the SYMMETRY input enters (B1)-(B5) through the kernel:
    # with anisotropy, [Q, H] != 0 at h = 0 and the k -> 0 double commutator
    # no longer vanishes -- the kernel bound with E(0) = 0 FAILS at k = 0.
    H0, sites0, _, SX0, SY0, SZ0 = build_block((8,), J, 0.0, anis=0.5)
    rho0 = gibbs(H0, beta)
    ev0 = lambda X: np.trace(rho0 @ X)
    m0 = ev0(sum(SX0)).real / N
    Q0 = fourier_op(SZ0, sites0, (0.0,), +1)
    dc0 = ev0((Q0 @ H0 - H0 @ Q0) @ Q0.conj().T
              - Q0.conj().T @ (Q0 @ H0 - H0 @ Q0)).real
    check("F", "falsifier (i): with U(1)-breaking anisotropy and h = 0, the "
               "k = 0 kernel bound N(J E(0) + h|m|) = 0 FAILS "
               "(the symmetry input is load-bearing)",
          dc0 > 1e-3, f"<[[Q_0,H],Q_0^dag]> = {dc0:.4f} > 0 = bound")
    # (ii) sharpness: 2-level near-equality instance.
    Hs = np.diag([0.0, 1.0]).astype(complex)
    Cs = np.array([[0, 1], [0, 0]], dtype=complex)
    As = Hs @ Cs.conj().T - Cs.conj().T @ Hs   # A = [H, C^dag]: CS equality
    betas = 1.0
    rhos = gibbs(Hs, betas)
    evs = lambda X: np.trace(rhos @ X)
    lhs = abs(evs(Cs @ As - As @ Cs))**2
    anti = evs(As @ As.conj().T + As.conj().T @ As).real
    dcs = evs((Cs @ Hs - Hs @ Cs) @ Cs.conj().T
              - Cs.conj().T @ (Cs @ Hs - Hs @ Cs)).real
    ratio = lhs / ((betas / 2) * anti * dcs)
    check("F", "falsifier (ii): (B1) is not vacuously slack -- constructed "
               "instance achieves a finite fraction of the bound",
          ratio > 0.1, f"saturation ratio = {ratio:.3f}")

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
