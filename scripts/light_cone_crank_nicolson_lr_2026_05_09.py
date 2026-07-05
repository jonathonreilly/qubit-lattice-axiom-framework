#!/usr/bin/env python3
"""Crank-Nicolson light-cone bridge: cone inheritance with quantified defect.

Companion to docs/LIGHT_CONE_CRANK_NICOLSON_LIEB_ROBINSON_BRIDGE_NOTE_2026-05-09.md
(2026-06-11 audit-failed repair revision).

The 2026-06-11 audit failed the prior revision: the claimed
submultiplicativity W_mu(H^n) <= W_mu(H)^n is false (disconnected
supports), so the quasilocal-overlap bound for
H_CN = (2/a) arctan(a H/2) and the fixed-step LR envelope built on it
do not hold. This rewrite verifies the corrected content:

  [A]  Cayley unitarity + the spectral generator identity
       U_CN = exp(-i a H_CN) (eigenphase match).

  [W]  WITHDRAWAL WITNESSES (the old claim is false):
       (i)  commuting three-site H = Z_a + Z_b + Z_c: H_CN carries the
            three-site term c_3 Z Z Z with the distance-independent
            closed-form coefficient
            c_3 = (1/(2a)) [arctan(3a/2) - 3 arctan(a/2)] != 0,
            so W_mu(H_CN) >= |c_3| e^{mu diam} is unbounded in the
            configuration diameter.
       (ii) on a generic finite-range chain, the directly computed
            Pauli-decomposition overlap weight W_mu(H_CN) EXCEEDS the
            old claimed bound (2/a) artanh((a/2) W_mu(H)) — numerical
            falsification of the withdrawn inequality.
       (iii) flat far tails: the one-step CN commutator at maximal
            distance is NOT exponentially small relative to mid-chain,
            so the withdrawn volume-independent fixed-step envelope is
            unavailable; the tail plateau scales like a^3 under step
            refinement.

  [C'] CONE-INHERITANCE THEOREM (corrected load-bearing content), all
       checked as inequalities with margins:
       (a) per-step defect ||a_CN(A) - a_exact(A)|| <= zeta with
           zeta = a ||[H,A]|| y^2/(1-y^2), y = a||H||/2 < 1,
           on an (L, a) grid;
       (b) flow invariance ||[H, alpha_s(A)]|| = ||[H, A]||;
       (c) n-step telescoping <= n zeta;
       (d) cone transfer:
           ||[a_CN^n(A_x), B_y]|| <= ||[a_t(A_x), B_y]|| + 2||B|| n zeta;
       (e) fixed-t O(a^2) convergence of the n-step defect.

  [D]  small-step agreement of CN and continuous commutators.

Deterministic (fixed seeds), numpy + scipy, runtime well under one
minute. Exit code 0 iff TOTAL: PASS=n FAIL=0.
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

PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]], dtype=complex)
PZ = np.diag([1.0, -1.0]).astype(complex)
P1 = {"I": np.eye(2, dtype=complex), "X": PX, "Y": PY, "Z": PZ}


def chain_H(L: int, J: float, seed: int) -> np.ndarray:
    """Random NN chain, each bond term with operator norm exactly J."""
    rng = np.random.default_rng(seed)
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    for z in range(L - 1):
        hh = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        hh = 0.5 * (hh + hh.conj().T)
        hh *= J / np.linalg.norm(hh, 2)
        H += np.kron(np.eye(2**z), np.kron(hh, np.eye(2 ** (L - z - 2))))
    return H


def site_op(L: int, s: int, op: np.ndarray) -> np.ndarray:
    return np.kron(np.eye(2**s), np.kron(op, np.eye(2 ** (L - s - 1))))


def cayley(H: np.ndarray, a: float) -> np.ndarray:
    """U_CN = (I - i a H/2)(I + i a H/2)^{-1}  (note convention)."""
    dim = H.shape[0]
    return (np.eye(dim) - 0.5j * a * H) @ np.linalg.inv(np.eye(dim) + 0.5j * a * H)


def opn(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def comm(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def pauli_string(ops: str) -> np.ndarray:
    M = P1[ops[0]]
    for ch in ops[1:]:
        M = np.kron(M, P1[ch])
    return M


def weighted_overlap(Hmat: np.ndarray, L: int, mu: float) -> float:
    """W_mu of the Pauli support family of Hmat: per-site sum of
    |coeff| * exp(mu * diam(support)) over strings containing the site,
    maximized over sites."""
    dim = 2**L
    per_site = np.zeros(L)
    for ops in product("IXYZ", repeat=L):
        s = "".join(ops)
        supp = [k for k, ch in enumerate(s) if ch != "I"]
        if not supp:
            continue
        c = abs(np.einsum("ij,ji->", pauli_string(s), Hmat)) / dim
        if c < 1e-14:
            continue
        wgt = c * np.exp(mu * (max(supp) - min(supp)))
        for k in supp:
            per_site[k] += wgt
    return float(per_site.max())


def main() -> int:
    print("=" * 76)
    print("CRANK-NICOLSON LIGHT-CONE BRIDGE -- cone inheritance + withdrawal")
    print("(2026-06-11 audit-failed repair: W_mu(H^n) <= W_mu(H)^n is FALSE;")
    print(" corrected content = cone-inheritance theorem CN-C')")
    print("=" * 76)

    # =======================================================================
    section("[A] Cayley unitarity + spectral generator identity")
    # =======================================================================
    for L, seed in ((8, 7), (8, 11)):
        H = chain_H(L, 1.0, seed)
        dim = 2**L
        a = 0.1
        U = cayley(H, a)
        check("A", f"unitarity (L={L}, seed={seed})",
              opn(U.conj().T @ U - np.eye(dim)) < 1e-12)
        w, P = np.linalg.eigh(H)
        U_spec = P @ np.diag(np.exp(-2j * np.arctan(a * w / 2))) @ P.conj().T
        check("A", f"U_CN = exp(-i a H_CN) spectrally (L={L}, seed={seed})",
              opn(U - U_spec) < 1e-11)

    # =======================================================================
    section("[W] withdrawal witnesses -- the old quasilocality claim is false")
    # =======================================================================
    # (i) commuting three-site decomposition with distance-independent c_3.
    a = 0.2
    Z3sites = [site_op(3, k, PZ) for k in range(3)]
    Hc = sum(Z3sites)
    w, P = np.linalg.eigh(Hc)
    Hcn = P @ np.diag((2 / a) * np.arctan(a * w / 2)) @ P.conj().T
    ZZZ = Z3sites[0] @ Z3sites[1] @ Z3sites[2]
    c3 = float(np.real(np.einsum("ij,ji->", ZZZ, Hcn)) / 8.0)
    c3_closed = (np.arctan(3 * a / 2) - 3 * np.arctan(a / 2)) / (2 * a)
    check("W", "three-site commuting H: c_3 matches the closed form "
               "(1/(2a))[arctan(3a/2) - 3 arctan(a/2)]",
          abs(c3 - c3_closed) < 1e-12, f"c_3 = {c3:.8f}")
    check("W", "c_3 != 0 (arctan strictly concave) -> H_CN has a genuine "
               "3-site term at ANY mutual distances; W_mu(H_CN) >= |c_3| "
               "e^{mu diam} is unbounded in the diameter",
          abs(c3) > 1e-4, f"|c_3| = {abs(c3):.6f}")
    c1 = float(np.real(np.einsum("ij,ji->", Z3sites[0], Hcn)) / 8.0)
    resid = opn(Hcn - c1 * Hc - c3 * ZZZ)
    check("W", "exact decomposition H_CN = c_1 (Z+Z+Z) + c_3 ZZZ "
               "(no other terms for the commuting model)",
          resid < 1e-12, f"residual = {resid:.1e}")

    # (ii) direct numerical falsification of the old artanh bound.
    L6, a6, mu = 6, 0.2, 0.5
    H6 = chain_H(L6, 1.0, seed=7)
    w6, P6 = np.linalg.eigh(H6)
    H6cn = P6 @ np.diag((2 / a6) * np.arctan(a6 * w6 / 2)) @ P6.conj().T
    WmuH = weighted_overlap(H6, L6, mu)
    WmuHcn = weighted_overlap(H6cn, L6, mu)
    x_mu = (a6 / 2) * WmuH
    old_bound = (2 / a6) * np.arctanh(x_mu) if x_mu < 1 else float("inf")
    check("W", "subcritical x_mu < 1 (the old bound's own premise holds here)",
          x_mu < 1, f"x_mu = {x_mu:.4f}")
    check("W", "FALSIFIED: computed W_mu(H_CN) EXCEEDS the old claimed bound "
               "(2/a) artanh(x_mu)",
          WmuHcn > old_bound,
          f"W_mu(H_CN) = {WmuHcn:.4f} > old bound = {old_bound:.4f}")

    # (iii) flat far tails at fixed a; tail plateau ~ a^3.
    L = 10
    H = chain_H(L, 1.0, seed=7)
    A0 = site_op(L, 0, PZ)
    tails = {}
    for aa in (0.2, 0.1):
        U = cayley(H, aa)
        AH = U.conj().T @ A0 @ U
        tails[aa] = {d: opn(comm(AH, site_op(L, d, PX))) for d in (4, 9)}
    check("W", "withdrawn fixed-step envelope is unavailable: far tail (d=9) "
               "is NOT small relative to mid-chain (d=4) at a = 0.2",
          tails[0.2][9] > 0.25 * tails[0.2][4],
          f"d=9: {tails[0.2][9]:.3e} vs d=4: {tails[0.2][4]:.3e}")
    ratio = tails[0.2][9] / tails[0.1][9]
    check("W", "tail plateau scales like a^3 under refinement "
               "(a=0.2 -> 0.1 gives ratio ~ 8)",
          4.0 < ratio < 16.0, f"ratio = {ratio:.2f}")

    # =======================================================================
    section("[C'] cone-inheritance theorem (corrected content), with margins")
    # =======================================================================
    # (a) per-step defect <= zeta on an (L, a) grid.
    all_y_sub = True
    for L in (8, 10):
        H = chain_H(L, 1.0, seed=7)
        dim = 2**L
        A0 = site_op(L, 0, PZ)
        nH = opn(H)
        cHA = opn(comm(H, A0))
        for aa in (0.2, 0.1, 0.05):
            y = aa * nH / 2
            all_y_sub &= y < 1
            zeta = aa * cHA * y**2 / (1 - y**2)
            U = cayley(H, aa)
            V = expm(-1j * aa * H)
            d = opn(U.conj().T @ A0 @ U - V.conj().T @ A0 @ V)
            check("C'", f"(a) per-step defect <= zeta  (L={L}, a={aa})",
                  d <= zeta, f"defect = {d:.3e}, zeta = {zeta:.3e}")
    check("C'", "(a) subcriticality y = a||H||/2 < 1 on the whole grid",
          all_y_sub)

    # (b) flow invariance ||[H, alpha_s(A)]|| = ||[H, A]||.
    L = 10
    H = chain_H(L, 1.0, seed=7)
    A0 = site_op(L, 0, PZ)
    cHA = opn(comm(H, A0))
    for s in (0.05, 0.1):
        Bs = expm(1j * s * H) @ A0 @ expm(-1j * s * H)
        check("C'", f"(b) ||[H, alpha_s(A)]|| = ||[H, A]|| at s = {s}",
              abs(opn(comm(H, Bs)) - cHA) < 1e-9,
              f"|delta| = {abs(opn(comm(H, Bs)) - cHA):.1e}")

    # (c) n-step telescoping.
    aa = 0.1
    nH = opn(H)
    y = aa * nH / 2
    zeta = aa * cHA * y**2 / (1 - y**2)
    U = cayley(H, aa)
    V = expm(-1j * aa * H)
    for n in (5, 10, 20):
        Un = np.linalg.matrix_power(U, n)
        Vn = np.linalg.matrix_power(V, n)
        dn = opn(Un.conj().T @ A0 @ Un - Vn.conj().T @ A0 @ Vn)
        check("C'", f"(c) n-step defect <= n zeta  (n = {n})",
              dn <= n * zeta, f"{dn:.3e} <= {n * zeta:.3e}")

    # (d) cone transfer at n = 10.
    n = 10
    Un = np.linalg.matrix_power(U, n)
    Vn = np.linalg.matrix_power(V, n)
    Acn = Un.conj().T @ A0 @ Un
    Aex = Vn.conj().T @ A0 @ Vn
    ok_all = True
    worst = ""
    for d in (2, 4, 6, 8, 9):
        B = site_op(L, d, PX)
        lhs = opn(comm(Acn, B))
        rhs = opn(comm(Aex, B)) + 2 * opn(B) * n * zeta
        if lhs > rhs + 1e-12:
            ok_all = False
            worst = f"violated at d={d}"
    check("C'", "(d) cone transfer ||[a_CN^n(A),B_d]|| <= ||[a_t(A),B_d]|| "
                "+ 2||B|| n zeta at every distance (n = 10, t = 1)",
          ok_all, worst or "all distances satisfied")

    # (e) fixed-t O(a^2) convergence of the n-step defect.
    t = 1.0
    dn_by_a = {}
    for aa2 in (0.1, 0.05):
        n2 = int(round(t / aa2))
        U2 = np.linalg.matrix_power(cayley(H, aa2), n2)
        V2 = np.linalg.matrix_power(expm(-1j * aa2 * H), n2)
        dn_by_a[aa2] = opn(U2.conj().T @ A0 @ U2 - V2.conj().T @ A0 @ V2)
    conv_ratio = dn_by_a[0.1] / dn_by_a[0.05]
    check("C'", "(e) fixed-t defect is O(a^2): halving a quarters the "
                "n-step defect (ratio in [3, 6])",
          3.0 < conv_ratio < 6.0,
          f"defect(a=0.1)/defect(a=0.05) = {conv_ratio:.2f}")

    # =======================================================================
    section("[D] small-step agreement of CN and continuous commutators")
    # =======================================================================
    aa3, n3 = 0.002, 50  # t = 0.1
    U3 = np.linalg.matrix_power(cayley(H, aa3), n3)
    V3 = expm(-1j * aa3 * n3 * H)
    A3 = U3.conj().T @ A0 @ U3
    A3e = V3.conj().T @ A0 @ V3
    check("D", "U_CN^n -> exp(-itH) on observables at small a (t = 0.1)",
          opn(A3 - A3e) < 1e-4, f"defect = {opn(A3 - A3e):.2e}")
    B2 = site_op(L, 2, PX)
    check("D", "CN and continuous commutators agree at small a",
          abs(opn(comm(A3, B2)) - opn(comm(A3e, B2))) < 1e-4,
          f"|delta| = {abs(opn(comm(A3, B2)) - opn(comm(A3e, B2))):.2e}")

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
