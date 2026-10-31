#!/usr/bin/env python3
"""The weight in `Nest coercivity` of `library/fibre-propagator.md`, on pure gauge modes at U = 1. Consumer: that lemma, Theorem F-D with layers.

Written before running. The note claimed || H/s ||^2 <= C (||d H||^2 + ||P_N D^* H||^2) with C absolute, s the local constraint scale up to the wall. A hostile estimate says this is false: take H = D omega with omega in ker r_N, P_N X omega =: psi at the coarse scale L s on the Y side. omega has gradient g about L s |psi| at the wall, the flux enters the first fine block of Omega and is absorbed there, so ||D omega / s||^2 on Omega is about g^2 s / s^2 per unit of wall, against ||psi||^2 about L s. The ratio is L. The proposed correct weight is s^# := the larger scale within a patch of the wall, so that a factor L at most is lost against the fine weight, once per wall.

The model. One-dimensional ring, or d = 2 with Fourier along the wall at zero transverse momentum, which is the same operator plus nothing: so d = 1. Fine sites; n_Y blocks of Ls fine sites (Y) and n_O blocks of s fine sites (Omega), filling the ring; r_N: the mean on each block. P_N: the orthogonal projector on functions of zero mean on each block. For omega in ker r_N, the ratio

 Rho[w] := sup || w D omega ||^2 / || P_N X omega ||^2,

for a weight w on bonds. Weights: w_1 := 1/s on Omega bonds, 1/(L s) on Y bonds. w_2 := 1/(L s) within L s of a wall on the Omega side too, and otherwise as w_1, with at least one Y block's length of Omega kept at w_2.

PRE-STATED criteria, at s = 5, L = 3, 5, 7, 9, 13, 17, 25, with n_Y = 2 and Omega long enough to hold 6 L s fine sites.
 N1. Rho[w_1] grows with L: Rho[w_1](25) >= 3 Rho[w_1](5). If this fails, the hostile estimate is wrong and the original weight may stand.
 N2. Rho[w_1](L) / L stays within a factor 3 over L >= 5: the predicted power is 1.
 N3. Rho[w_2] is bounded: Rho[w_2](25) <= 1.5 Rho[w_2](5).
 N4. Control: with s = 7, Rho[w_2](9) within a factor 1.3 of its value at s = 5, so the fine spacing does not matter.
FAIL if N3 or N4 fails. N1, N2 decide between the two statements.

First run, recorded: N1, N2 true, N3 false, with Rho[w_2] growing like 0.034 L. Diagnosed from the top mode: the numerator sat on bonds next to one wall, which my code had given the fine weight, since it took the minimum of |x - i| over Y sites before wrapping around the ring. This is an error of the check, not of the statement, as w_2 was not what the criterion names. Fixed, with the criteria unchanged, and run again.

Limits. Pure gauge modes at U = 1, d = 1. The co-closed sector is Lemma D-coer. RSS guard 2 GB.
"""
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def build(L, s):
    Ls = L * s
    n_y, n_o = 2, 6 * L
    blocks = [Ls] * n_y + [s] * n_o
    n = sum(blocks)
    block_of = np.concatenate([np.full(b, i) for i, b in enumerate(blocks)])
    is_y = block_of < n_y
    return n, blocks, block_of, is_y


def rho(L, s, weight):
    n, blocks, block_of, is_y = build(L, s)
    Ls = L * s
    # Basis of ker r_N: on each block, differences.
    rows = []
    start = 0
    B = np.zeros((n, n - len(blocks)))
    col = 0
    for b in blocks:
        # Orthonormal basis of zero mean vectors on the block.
        Q = np.linalg.qr(np.eye(b) - np.ones((b, b)) / b)[0][:, : b - 1]
        B[start : start + b, col : col + b - 1] = Q
        start += b
        col += b - 1
    D = np.roll(np.eye(n), -1, axis=1) - np.eye(n)  # (D f)(x) = f(x + 1) - f(x), bond x -> x + 1.
    X = D.T @ D
    if weight == 1:
        w = np.where(is_y & np.roll(is_y, -1), 1.0 / Ls, 1.0 / s)
    else:
        w = np.where(is_y & np.roll(is_y, -1), 1.0 / Ls, 1.0 / s)
        # Bonds of Omega within L s of a wall take the coarse weight.
        idx = np.where(is_y)[0]
        dd = np.abs(np.subtract.outer(np.arange(n), idx))
        d = np.min(np.minimum(dd, n - dd), axis=1)
        w = np.where(d <= Ls, 1.0 / Ls, w)
    A = B.T @ (D.T @ (w[:, None] ** 2 * D)) @ B
    PX = B.T @ X @ B  # P_N X on ker r_N, in the basis.
    C = PX.T @ PX
    # Generalised eigenvalue: largest of A v = lam C v.
    lc, Vc = np.linalg.eigh(C)
    Ci = (Vc / np.sqrt(lc)) @ Vc.T
    return float(np.linalg.eigvalsh(Ci @ A @ Ci)[-1])


def main():
    ok = True
    Ls = (3, 5, 7, 9, 13, 17, 25)
    r1, r2 = {}, {}
    for L in Ls:
        r1[L], r2[L] = rho(L, 5, 1), rho(L, 5, 2)
        print(f" s=5 L={L}: Rho[w_1]={r1[L]:.4f} Rho[w_1]/L={r1[L] / L:.4f} Rho[w_2]={r2[L]:.4f} rss={rss_gb():.2f}GB", flush=True)
        if rss_gb() > 2:
            raise SystemExit("RSS above 2 GB")
    n1 = r1[25] >= 3 * r1[5]
    vals = [r1[L] / L for L in Ls if L >= 5]
    n2 = max(vals) <= 3 * min(vals)
    n3 = r2[25] <= 1.5 * r2[5]
    v7 = rho(9, 7, 2)
    n4 = abs(v7 / r2[9] - 1) <= 0.3
    print(f" N1 {n1}; N2 {n2}; N3 {n3}; N4 s=7 L=9 Rho[w_2]={v7:.4f} against {r2[9]:.4f}: {n4}")
    ok = n3 and n4
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
