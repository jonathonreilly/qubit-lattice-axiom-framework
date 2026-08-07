#!/usr/bin/env python3
"""Koide real-rep block-count route: permitted-not-forced.

The listed retained real-structure constraints (CPT antilinear Theta +
signed/det_R readout + real-rep C_3 decomposition + reality of D) do NOT forbid
the (1,2) dimension weighting on the generation operator space span{I, J-I}, so
they do not force the (1,1) block-count that would give Q=2/3. Reproduces five
computations:

  1. C_3-rotation invariance fixes the Gram to diag(g00, g11, g11) with the
     singlet:doublet ratio FREE (the 2-parameter isotype-split cone).
  2. The antilinear Theta = diag(1,1,-1) reality condition imposes ZERO extra
     constraint on that cone (isometry + self-adjointness residuals = 0).
  3. The Hermitian doublet eigenvalues are two independent real numbers (no
     conjugate pair), so the det_R rotation-block fusion is inapplicable.
  4. The signed/Brannen Q = (1+2r)/3 is (1,2)-compatible: Q=1 at r=1 with valid
     all-real Hermitian spectra; it presupposes r=1/2.
  5. det_R(alpha P_singlet + beta P_doublet) = alpha * beta^2 (a genuine real
     determinant carrying the (1,2) weighting); WITNESS diag(3,6,6) is invariant.
"""

from __future__ import annotations

import numpy as np
from sympy import (Matrix, Rational, cos, eye, pi, simplify, sin, sqrt, symbols,
                   zeros)

AUDIT_TIMEOUT_SEC = 120

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)


def main() -> int:
    section("Check 1 - C_3-rotation invariance fixes Gram to diag(g00,g11,g11)")
    # Coordinates (a, b_re, b_im); C_3 acts as singlet fixed, doublet rotated 2pi/3.
    c, s = cos(2 * pi / 3), sin(2 * pi / 3)
    R = Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])
    g00, g01, g02, g11, g12, g22 = symbols("g00 g01 g02 g11 g12 g22")
    G = Matrix([[g00, g01, g02], [g01, g11, g12], [g02, g12, g22]])
    inv = simplify(R.T * G * R - G)
    sol = __import__("sympy").solve([inv[i, j] for i in range(3) for j in range(3)],
                                    [g01, g02, g12, g22], dict=True)
    s0 = sol[0]
    cone_ok = (s0.get(g01) == 0 and s0.get(g02) == 0 and s0.get(g12) == 0
               and simplify(s0.get(g22) - g11) == 0)
    check("rotation-invariant Gram = diag(g00, g11, g11), ratio g00:g11 free", cone_ok,
          f"sol={ {k: s0[k] for k in s0} }")

    section("Check 2 - antilinear Theta = diag(1,1,-1) imposes ZERO extra constraint")
    Th = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    Gcone = Matrix([[g00, 0, 0], [0, g11, 0], [0, 0, g11]])
    iso = simplify(Th.T * Gcone * Th - Gcone)          # isometry residual
    sa = simplify(Gcone * Th - (Gcone * Th).T)         # self-adjointness residual
    check("Theta isometry residual = 0 on the whole cone", iso == zeros(3))
    check("Theta self-adjointness residual = 0 on the whole cone", sa == zeros(3))

    section("Check 3 - Hermitian doublet eigenvalues are two independent reals")
    a, br, bi = symbols("a b_re b_im", real=True)
    b = br + __import__("sympy").I * bi
    Csym = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    Msym = a * eye(3) + b * Csym + b.conjugate() * (Csym * Csym)
    eigs = Msym.eigenvals()
    eig_list = []
    for ev, mult in eigs.items():
        eig_list.extend([simplify(ev)] * mult)
    all_real = all(simplify(__import__("sympy").im(ev)) == 0 for ev in eig_list)
    check("all three Hermitian-circulant eigenvalues are real", all_real)
    # the two doublet eigenvalues depend on b_re and b_im independently
    doublet = [ev for ev in eig_list if simplify(ev - (a + 2 * br)) != 0]
    indep = (len(set(simplify(ev) for ev in doublet)) == 2
             and any(simplify(__import__("sympy").diff(ev, bi)) != 0 for ev in doublet))
    check("the two doublet eigenvalues are independent reals (not a conjugate pair)", indep,
          f"doublet={[str(simplify(ev)) for ev in doublet]}")
    # contrast: a generic NON-Hermitian real circulant gives a conjugate pair
    cc = 0.3  # coeff(C^2) independent of conj(b); real here for a clean contrast
    Mnh = 1.0 * I3 + (0.5) * C + cc * C2
    ev_nh = np.linalg.eigvals(Mnh)
    has_complex_pair = np.max(np.abs(ev_nh.imag)) > 1e-9
    check("a NON-Hermitian real circulant DOES give a complex-conjugate pair", has_complex_pair,
          f"max|Im|={np.max(np.abs(ev_nh.imag)):.2f}")

    section("Check 4 - signed/Brannen Q = (1+2r)/3 is (1,2)-compatible (Q=1 at r=1)")
    for r_target, theta in [(0.5, 0.0), (1.0, 0.0), (1.0, 0.7), (1.0, 1.3)]:
        bval = (r_target ** 0.5) * np.exp(1j * theta)
        Mn = I3 + bval * C + np.conj(bval) * C2
        lam = np.linalg.eigvalsh(Mn)  # Hermitian -> real signed eigenvalues
        Q = float(np.sum(lam ** 2) / (np.sum(lam) ** 2))
        expect = (1 + 2 * r_target) / 3
        check(f"r={r_target:g}, theta={theta:g}: Q=(1+2r)/3={expect:.4f}, real spectrum",
              abs(Q - expect) < 1e-9 and np.max(np.abs(lam.imag)) < 1e-12, f"Q={Q:.6f}")

    section("Check 5 - det_R(alpha P_s + beta P_d) = alpha*beta^2; witness diag(3,6,6)")
    Ps = (I3 + C + C2) / 3.0
    Pd = I3 - Ps
    check("P_singlet rank 1, P_doublet rank 2", round(np.trace(Ps).real) == 1 and round(np.trace(Pd).real) == 2)
    for al, be in [(2.0, 3.0), (1.0, 0.5), (4.0, 1.5)]:
        d = np.linalg.det(al * Ps + be * Pd).real
        check(f"det_R(alpha={al}, beta={be}) = alpha*beta^2 = {al*be*be:.3f}", abs(d - al * be * be) < 1e-9,
              f"det={d:.3f}")
    # the (1,2) witness: HS Gram diag(3,6,6) is real, PD, rotation- and Theta-invariant
    HS = np.diag([3.0, 6.0, 6.0])
    Rn = np.array([[1, 0, 0], [0, np.cos(2 * np.pi / 3), -np.sin(2 * np.pi / 3)],
                   [0, np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)]])
    Thn = np.diag([1.0, 1.0, -1.0])
    witness_ok = (np.all(np.linalg.eigvalsh(HS) > 0)
                  and np.max(np.abs(Rn.T @ HS @ Rn - HS)) < 1e-9
                  and np.max(np.abs(Thn.T @ HS @ Thn - HS)) < 1e-9)
    check("WITNESS diag(3,6,6) [the (1,2) weighting] is PD, C_3- and Theta-invariant", witness_ok)

    section("N5 execution certificate - what this runner resolves")
    print(
        "  per_element: resolved, and it is how the freedom is located. The Gram is carried "
        "as six independent symbols and the C_3-invariance condition is imposed on all nine "
        "entries of R^T G R - G, then solved, which is what forces g01, g02 and g12 to zero "
        "and g22 to equal g11 while leaving the single ratio g00 : g11 free. The two "
        "antilinear-Theta residuals are likewise required to be zeros(3) entry by entry "
        "across the whole cone."
    )
    print(
        "  per_site: checked and not executed — no lattice, position index or neighbour "
        "term appears. The arena is one three-dimensional coordinate space (a, b_re, b_im) "
        "over a single generation operator span, and the question is which inner products "
        "on that one space survive the listed real-structure constraints. Nothing about "
        "that survives or fails differently at another site, because no other site exists "
        "here."
    )
    print(
        "  per_mode: resolved, and it is what disqualifies the fusion argument. The three "
        "eigenvalues of the Hermitian circulant are computed symbolically and all shown "
        "real, and the two doublet eigenvalues are then shown to be genuinely independent "
        "reals, distinct from one another and with nonzero derivative in b_im, rather than "
        "a complex-conjugate pair. The contrast case is run explicitly: a non-Hermitian "
        "real circulant does produce a conjugate pair with clearly nonzero imaginary parts."
    )
    print(
        "  per_block: resolved — the singlet and doublet projectors are built and their "
        "ranks confirmed as 1 and 2, the real determinant of a block-diagonal combination "
        "is verified to factor as alpha times beta squared at three separate (alpha, beta) "
        "pairs, exhibiting the (1, 2) weighting inside a genuine real determinant, and the "
        "block Gram diag(3, 6, 6) is checked positive-definite and invariant under both the "
        "C_3 rotation and Theta."
    )
    print(
        "  lattice_wide: checked and not executed — no volume, site sum or limit is formed, "
        "and the logical shape of the claim makes one unnecessary. This is a "
        "permitted-not-forced result, established by exhibiting one explicit object, the "
        "diag(3, 6, 6) witness, that satisfies every listed constraint while carrying the "
        "(1, 2) weighting. A single surviving witness cannot be removed by extending the "
        "system; only an additional constraint could remove it, which is the open handle "
        "the note names."
    )

    section("Summary")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("The listed real-structure constraints do NOT forbid (1,2); (1,1) is permitted-not-forced.")
    print("Remaining open handle named by the note: SO(2)/U(1)_b doublet-frame quotient.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
