"""Audit companion runner for the substep-4 AC_phi trace-equipartition
bridge narrow theorem (2026-05-17).

Verifies via sympy exact symbolic arithmetic that, for the standard
3 x 3 cyclic permutation matrix C and the Hermitian ansatz
H = a * I + b * C + bbar * C^2 with a in R and b in C,

  (P1) [H, C] = 0 (commutation, holds for all a, b);
       H = H^dagger (Hermiticity);
       a generic non-circulant Hermitian violates [H_bad, C] = 0
       (counter-example uniqueness check).
  (P2) the three diagonal entries <e_alpha | H | e_alpha> all equal a;
       pairwise differences are exactly zero.
  (P3) Tr(H) = 3 a; equivalently each diagonal entry = Tr(H) / 3.
  (P4) eigenvalues match the formula
         lambda_k = a + b * omega^k + bbar * omega^(-k),
       are pairwise distinct for generic b != 0,
       and the diagonal-entry set {a, a, a} is not equal to the
       eigenvalue set as a multiset.
  (counter-examples) non-Hermitian commuter, b = 0 maximally
       degenerate case.

Expected output: PASS=N FAIL=0 with N >= 12.
"""

from __future__ import annotations

import sympy as sp


def main() -> int:
    fails: list[str] = []
    passes: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        if ok:
            passes.append(label)
            print(f"  PASS  {label}" + (f" :: {detail}" if detail else ""))
        else:
            fails.append(label)
            print(f"  FAIL  {label}" + (f" :: {detail}" if detail else ""))

    # ----- Setup: cyclic matrix and symbolic Hermitian -----
    a = sp.symbols("a", real=True)
    b1, b2 = sp.symbols("b1 b2", real=True)
    b = b1 + sp.I * b2
    bbar = b1 - sp.I * b2

    I3 = sp.eye(3)
    C = sp.Matrix(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ]
    )
    C2 = C * C
    Cdagger = C.T  # real entries, so dagger = transpose
    # H = a I + b C + bbar C^2
    H = a * I3 + b * C + bbar * C2

    omega = sp.exp(2 * sp.pi * sp.I / 3)

    print("=== Substep-4 AC_phi trace-equipartition bridge ===")

    # ----- (P1) cyclic identity C^3 = I -----
    print("\n[P1] cyclic and circulant structure")
    check(
        "C^3 = I",
        sp.simplify(C ** 3 - I3) == sp.zeros(3, 3),
    )

    # ----- (P1) [H, C] = 0 -----
    commHC = sp.expand(H * C - C * H)
    commHC_simplified = sp.Matrix(
        [[sp.simplify(commHC[i, j]) for j in range(3)] for i in range(3)]
    )
    check(
        "[H, C] = 0 for circulant Hermitian ansatz",
        commHC_simplified == sp.zeros(3, 3),
        detail=f"[H,C] = {commHC_simplified.tolist()}",
    )

    # ----- (P1) Hermiticity H = H^dagger -----
    Hdagger = sp.Matrix(
        [[sp.conjugate(H[j, i]) for j in range(3)] for i in range(3)]
    )
    # substitute that a is real and b = b1 + I*b2
    diff_herm = sp.simplify(H - Hdagger)
    # rewrite conjugates using a real, b1, b2 real
    diff_herm = sp.Matrix(
        [
            [
                sp.simplify(
                    sp.expand(diff_herm[i, j]).rewrite(sp.exp).subs(
                        {sp.conjugate(a): a, sp.conjugate(b1): b1, sp.conjugate(b2): b2}
                    )
                )
                for j in range(3)
            ]
            for i in range(3)
        ]
    )
    check(
        "H = H^dagger (Hermiticity of ansatz)",
        diff_herm == sp.zeros(3, 3),
        detail=f"H - H^dagger = {diff_herm.tolist()}",
    )

    # ----- (P1) counter-example: a non-circulant Hermitian violates [H_bad, C] = 0 -----
    # Take H_bad = diag(0, 1, 2) — clearly Hermitian, not C-circulant
    H_bad = sp.diag(0, 1, 2)
    comm_bad = sp.expand(H_bad * C - C * H_bad)
    comm_bad_nonzero = comm_bad != sp.zeros(3, 3)
    check(
        "non-circulant Hermitian counter-example: [H_bad, C] != 0",
        comm_bad_nonzero,
        detail=f"[diag(0,1,2), C] = {comm_bad.tolist()}",
    )

    # ----- (P2) Diagonal entries all equal a -----
    print("\n[P2] diagonal-entry equality")
    diag_entries = [sp.simplify(H[i, i]) for i in range(3)]
    for i, d in enumerate(diag_entries):
        check(
            f"<e_{i+1} | H | e_{i+1}> = a",
            sp.simplify(d - a) == 0,
            detail=f"diag entry = {d}",
        )

    # ----- (P2) Pairwise differences zero -----
    for i in range(3):
        for j in range(i + 1, 3):
            diff = sp.simplify(diag_entries[i] - diag_entries[j])
            check(
                f"<e_{i+1}|H|e_{i+1}> - <e_{j+1}|H|e_{j+1}> = 0",
                diff == 0,
                detail=f"diff = {diff}",
            )

    # ----- (P3) Trace identity Tr(H) = 3 a -----
    print("\n[P3] trace identity")
    trH = sp.simplify(sp.Trace(H).doit())
    check("Tr(H) = 3 a", sp.simplify(trH - 3 * a) == 0, detail=f"Tr(H) = {trH}")
    for i in range(3):
        check(
            f"<e_{i+1}|H|e_{i+1}> = Tr(H) / 3",
            sp.simplify(diag_entries[i] - trH / 3) == 0,
        )

    # ----- (P4) Eigenvalue formula -----
    print("\n[P4] eigenvalue formula and spectrum vs diagonal separation")
    # Compute eigenvalues symbolically by characteristic polynomial
    eigvals = list(H.eigenvals().keys())

    # Expected eigenvalues: lambda_k = a + b * omega^k + bbar * omega^(-k)
    expected = []
    for k in range(3):
        lam_k = a + b * omega ** k + bbar * omega ** (-k)
        lam_k = sp.simplify(sp.expand(lam_k, complex=True))
        expected.append(lam_k)

    # The characteristic polynomial of H should be
    # prod_k (x - lambda_k)
    x = sp.symbols("x")
    char = sp.expand(H.charpoly(x).as_expr())
    expected_char = sp.expand(
        sp.prod([x - lam for lam in expected])
    )
    diff_char = sp.simplify(char - expected_char)
    # diff may still have I/conjugate forms; rewrite using b1, b2 real
    diff_char = sp.simplify(
        diff_char.subs({sp.conjugate(b1): b1, sp.conjugate(b2): b2}).rewrite(sp.cos)
    )
    diff_char = sp.simplify(diff_char)
    check(
        "char poly of H = prod_k (x - (a + b*omega^k + bbar*omega^(-k)))",
        diff_char == 0,
        detail=f"diff = {diff_char}",
    )

    # ----- (P4) Pairwise distinctness for a generic b -----
    # Substitute b = 1 + I/2 (so b1 = 1, b2 = 1/2, |b| = sqrt(5)/2 != 0)
    a_val, b1_val, b2_val = sp.Rational(3, 7), sp.Integer(1), sp.Rational(1, 2)
    subs_map = {a: a_val, b1: b1_val, b2: b2_val}
    H_num = H.subs(subs_map)
    eigvals_num = list(H_num.eigenvals().keys())
    eigvals_num_simplified = [sp.nsimplify(sp.simplify(ev), rational=False) for ev in eigvals_num]
    # check pairwise distinct
    all_distinct = True
    for i in range(len(eigvals_num_simplified)):
        for j in range(i + 1, len(eigvals_num_simplified)):
            if sp.simplify(eigvals_num_simplified[i] - eigvals_num_simplified[j]) == 0:
                all_distinct = False
    check(
        "three eigenvalues pairwise distinct at a = 3/7, b = 1 + I/2",
        all_distinct and len(set(eigvals_num_simplified)) == 3,
        detail=f"eigvals = {[sp.simplify(ev) for ev in eigvals_num_simplified]}",
    )

    # ----- (P4) Diagonal-vs-eigenvalue separation -----
    # diagonal entries at the same numerical (a, b): all equal a = 3/7
    diag_num = [sp.simplify(d.subs(subs_map)) for d in diag_entries]
    diag_set = set(diag_num)
    eig_set = set(eigvals_num_simplified)
    check(
        "diagonal set {a,a,a} != eigenvalue set for generic b != 0",
        diag_set != eig_set,
        detail=f"diag = {diag_num}; eigs = {sorted([sp.simplify(ev) for ev in eigvals_num_simplified], key=lambda z: sp.re(z))}",
    )

    # ----- counter-example: non-Hermitian commuter -----
    print("\n[counter-examples]")
    # Take H_nh = b * C + b' * C^2 with b' arbitrary != bbar (so not Hermitian
    # pairing). For concreteness b = 1, b' = 2 (real distinct).
    H_nh = 1 * C + 2 * C2
    comm_nh = sp.expand(H_nh * C - C * H_nh)
    nh_hermitian = H_nh.equals(H_nh.T.conjugate())
    check(
        "non-Hermitian commuter: [H_nh, C] = 0 but H_nh != H_nh^dagger",
        comm_nh == sp.zeros(3, 3) and not nh_hermitian,
        detail=f"[H_nh, C] = {comm_nh.tolist()}; Hermitian? {nh_hermitian}",
    )

    # ----- coincidence at b = 0 -----
    H_b0 = H.subs({b1: 0, b2: 0})
    eigvals_b0 = list(H_b0.eigenvals().keys())
    eigvals_b0_multiplicities = H_b0.eigenvals()
    # Expect single eigenvalue a with multiplicity 3
    check(
        "at b = 0: H has single eigenvalue a with multiplicity 3",
        len(eigvals_b0) == 1
        and sp.simplify(eigvals_b0[0] - a) == 0
        and eigvals_b0_multiplicities[eigvals_b0[0]] == 3,
        detail=f"eigvals(b=0) = {eigvals_b0_multiplicities}",
    )

    # ----- Summary -----
    print("\n=== Summary ===")
    print(f"PASS={len(passes)} FAIL={len(fails)}")
    if fails:
        print("Failures:")
        for f in fails:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
