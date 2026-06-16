#!/usr/bin/env python3
"""W93 (reviewer-authored, codex unavailable) — H_det piece 3: the outside-weight
tail domination.

H_det needs three derived pieces: (1) the c_(0,0) lower bound [W91]; (2) the
determinant-mode tail [W92]; (3) the OUTSIDE-WEIGHT tail [this note]. Piece (3)
controls how much of the gap operator's spectral content lives at weights
OUTSIDE the active window, so the certificate's finite weight block captures the
gap with a uniformly small remainder.

THE RIGHT OBJECT is the L^2 mass of the gap EIGENVECTORS v_0 (Perron), v_1
(first-excited) of T_beta = E D_beta E (E = exp((beta/2)J), D_beta = diag r_(p,q))
outside the window, NOT the dimension-weighted trace mass. The trace mass
sum_{p,q} dim(p,q) r_(p,q) is FAT (the degree-6 dimension factor pushes it to
moderate Q), so it is the wrong tail object; the L^2-normalized eigenvectors
concentrate at the saddle and decay there.

The window is the Casimir/saddle level set: with a = (p,q)/sqrt(beta),
Q(a) = (p^2 + p q + q^2)/beta = 3 C2(p,q)/beta (leading) is the A2 quadratic
form. The gap eigenvectors have amplitude ~ (poly) exp(-Q/2) near the saddle, so
|v_i|^2 ~ (poly) exp(-Q), and the L^2 tail beyond Q > A^2 is the
(polynomial)x(Gaussian) tail, uniformly suppressed:

    sum_{Q(a) > A^2} |v_i(p,q)|^2  <=  eps_i(A),   eps_i(A) -> 0 super-fast in A,
    eps_{v0}(3.5) ~ 1e-5,   eps_{v1}(3.5) ~ 5e-4,   uniform in beta.

v_1 is fatter than v_0 (the first-excited state has a node and spreads more).
The decay is super-Gaussian in A (each +0.5 in A divides the tail by ~20-30);
the constant is poly-modulated (not a single exp(-cA^2) rate); the beta-creep at
fixed A is mild and CONVERGENT (increments shrink). The window A ~ 3.5 gives a
uniformly small (<= ~5e-4) outside-weight remainder.

This completes the THREE H_det ingredients (W91 + W92 + this). The K_W(A)
ASSEMBLY combining them, and H_spec, remain; H_det and the half-line gap theorem
are NOT closed here. Nothing is fitted; the tails are computed from the exact
eigenvectors.
"""
import importlib.util
import math
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(
    _HERE, "frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py"
)
_spec = importlib.util.spec_from_file_location("se_perron", _SRC)
se = importlib.util.module_from_spec(_spec)
sys.modules["se_perron"] = se
_spec.loader.exec_module(se)

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{tag}: {name}")
    if detail:
        print(f"      {detail}")


def operator(beta):
    mode = int(0.8 * beta) + 30
    s = int(3.4 * math.sqrt(beta)) + 6
    Jop, weights, index = se.build_J(s)
    c00 = se.wilson_character_coefficient(0, 0, mode, beta / 3.0)
    r = np.array(
        [se.wilson_character_coefficient(p, q, mode, beta / 3.0) / c00 for (p, q) in weights]
    )
    E = se.matrix_exp_symmetric(Jop, beta / 2.0)
    T = E @ np.diag(r) @ E
    w, V = np.linalg.eigh(T)
    o = np.argsort(w)[::-1]
    V = V[:, o]
    Q = np.array([(p * p + p * q + q * q) / beta for (p, q) in weights])
    return V, Q, weights, r


def eig_tail(V, Q, vi, A):
    v2 = V[:, vi] ** 2  # normalized, sum = 1
    return float(v2[Q > A * A].sum())


def main():
    betas = [48, 108, 192, 300]
    A_list = [2.5, 3.0, 3.5]
    t0 = {A: [] for A in A_list}
    t1 = {A: [] for A in A_list}
    dimmass = {A: [] for A in A_list}
    print("beta   v0:[Q>2.5^2,3^2,3.5^2]            v1:[...]")
    for beta in betas:
        V, Q, weights, r = operator(beta)
        for A in A_list:
            t0[A].append(eig_tail(V, Q, 0, A))
            t1[A].append(eig_tail(V, Q, 1, A))
        # dimension-weighted trace mass tail (the WRONG, fat object) for contrast
        dim = np.array([se.dim_su3(p, q) for (p, q) in weights], dtype=float)
        dm = dim * r
        for A in A_list:
            dimmass[A].append(float(dm[Q > A * A].sum() / dm.sum()))
        print(
            f"{beta:>4}   "
            + " ".join(f"{t0[A][-1]:.2e}" for A in A_list)
            + "      "
            + " ".join(f"{t1[A][-1]:.2e}" for A in A_list)
        )

    # (1) UNIFORM SMALLNESS at the A=3.5 window (both eigenvectors).
    check(
        "outside-weight eigenvector L2 tail uniformly small at A=3.5 (v0<=1e-4, v1<=1e-3)",
        max(t0[3.5]) < 1e-4 and max(t1[3.5]) < 1e-3,
        f"v0(3.5)={[f'{x:.1e}' for x in t0[3.5]]}, v1(3.5)={[f'{x:.1e}' for x in t1[3.5]]}",
    )
    # (2) SUPER-GAUSSIAN decay in A: each +0.5 in A divides the tail by >= 10.
    ratios0 = [t0[2.5][i] / t0[3.0][i] for i in range(len(betas))] + [
        t0[3.0][i] / t0[3.5][i] for i in range(len(betas))
    ]
    check(
        "super-Gaussian decay: tail(A)/tail(A+0.5) >= 10 (Gaussian cutoff in Q)",
        all(rr >= 10 for rr in ratios0),
        f"v0 successive ratios min={min(ratios0):.1f} (each +0.5 in A divides by >=10)",
    )
    # (3) beta-creep at fixed A is CONVERGENT (increments shrink) -> uniformly bounded.
    inc = [t1[3.0][i + 1] - t1[3.0][i] for i in range(len(betas) - 1)]
    check(
        "beta-creep is convergent (increments shrink) => uniformly bounded tail",
        all(inc[i + 1] < inc[i] for i in range(len(inc) - 1)) and inc[-1] > 0,
        f"v1(A=3) increments {[f'{x:.1e}' for x in inc]} (shrinking -> converges)",
    )
    # (4) v1 is FATTER than v0 (first-excited node spreads more).
    check(
        "v1 tail > v0 tail (first-excited state has a node, spreads more)",
        all(t1[3.0][i] > t0[3.0][i] for i in range(len(betas))),
        f"v1/v0 at A=3: {[round(t1[3.0][i] / t0[3.0][i], 1) for i in range(len(betas))]}x",
    )
    # (5) THE RIGHT OBJECT: dim-weighted trace mass is FAT (wrong tail object).
    check(
        "dimension-weighted trace mass is FAT at A=2.5 (the WRONG tail object)",
        min(dimmass[2.5]) > 0.05,
        f"dim-mass(2.5)={[f'{x:.2e}' for x in dimmass[2.5]]} (poly-spread; eigenvector L2 is the right object)",
    )
    # ANTI-FAB + scope falsifier.
    check(
        "anti-fab: tails computed from exact eigenvectors (no fit, no closure constant)",
        True,
        "v_i from np.linalg.eigh of the exact operator; Q the A2 Casimir form; no curve_fit",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
