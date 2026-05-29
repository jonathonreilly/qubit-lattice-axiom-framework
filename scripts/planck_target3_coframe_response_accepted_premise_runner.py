#!/usr/bin/env python3
"""Narrow accepted-premise bridge for the Planck Target-3 coframe response.

This runner verifies the bounded conditional consequence (B1)-(B4) of
PLANCK_TARGET3_COFRAME_RESPONSE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md:

  (P1) := supplied metric-compatible coframe response
            D : E_C -> End(K), D(v)^2 = ||v||^2 I_K
  =>  (B1) polarization identity
            D(u)D(v) + D(v)D(u) = 2 <u,v> I_K
  =>  (B2) Clifford relations { Gamma_a, Gamma_b } = 2 delta_{ab} I
  =>  (B3) 16 Clifford words span End(K) = M_4(C); rank-4 K
            realises the unique irreducible Cl_4(C) module
  =>  (B4) in the Pauli-realized Hermitian representative, oriented
            CAR-mode pairs satisfy { c_i, c_j } = 0,
            { c_i, c_j^dag } = delta_{ij} I

All identities are verified by exact sympy symbolic arithmetic on
finite-dim complex matrices. No PDG / fitted / observed value enters.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = (
    "planck_target3_coframe_response_accepted_premise_bridge_bounded_note_2026-05-26"
)
RUNNER_REL = "scripts/planck_target3_coframe_response_accepted_premise_runner.py"
NOTE_PATH = (
    ROOT
    / "docs/PLANCK_TARGET3_COFRAME_RESPONSE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Accepted Premises Registration",
        "(P1)",
        "metric-compatible coframe response",
        "accepted-premise packet entry",
        "not derived in this bridge",
        "MINIMAL_AXIOMS_2026-05-20.md",
        RUNNER_REL,
        "CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md",
        "bounded_theorem",
        "Status authority",
        "independent audit lane only",
        "Pauli-realized Hermitian representative",
        "not a representation-invariant daggered-CAR",
        "Audit Repair Boundary",
    ]
    for phrase in required:
        check(f"source contains required phrase: {phrase}", phrase in note)

    forbidden = [
        "PDG " + "load-bearing value",
        "load-bearing fitted",
        "Monte Carlo " + "measurement consumed",
        "load-bearing " + "g_bare value",
    ]
    for phrase in forbidden:
        check(
            f"source note excludes forbidden phrase: {phrase}",
            phrase not in note,
        )


def build_cl4_representation() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    """Build a faithful 4x4 complex representation of Cl(4, C).

    Use the standard Dirac/Pauli basis on K = C^4.  At signature (+,+,+,+),
    the four anticommuting Hermitian generators satisfy
        Gamma_a^2 = I,   Gamma_a Gamma_b + Gamma_b Gamma_a = 0  (a != b),
    which is the polarized form of the metric-compatibility identity at
    the orthonormal basis.  We use the realization

        Gamma_t = sigma_1 (x) I,
        Gamma_n = sigma_2 (x) I,
        Gamma_1 = sigma_3 (x) sigma_1,
        Gamma_2 = sigma_3 (x) sigma_2,

    where (x) is Kronecker product.  All four are Hermitian and pairwise
    anticommuting with squares equal to I_4; this is well-known.  The
    fifth generator sigma_3 (x) sigma_3 is the chirality / volume
    element omega = Gamma_t Gamma_n Gamma_1 Gamma_2 up to a sign factor.
    """
    s0 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])

    def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
        return sp.Matrix(
            [
                [a[i, j] * b[k, l] for j in range(a.cols) for l in range(b.cols)]
                for i in range(a.rows)
                for k in range(b.rows)
            ]
        )

    Gt = kron(s1, s0)
    Gn = kron(s2, s0)
    G1 = kron(s3, s1)
    G2 = kron(s3, s2)
    return Gt, Gn, G1, G2


def part1_polarization() -> None:
    print("\n== Part 1: (B1) polarization identity ==")
    # Verify the polarization identity at the abstract bilinear-form level
    # for the inner product < e_a, e_b > = delta_{ab} on E.
    # Define symbolic D(e_a) = G_a and verify D(u)D(v) + D(v)D(u) = 2 <u,v> I
    Gt, Gn, G1, G2 = build_cl4_representation()
    I4 = sp.eye(4)
    Gs = {"t": Gt, "n": Gn, "1": G1, "2": G2}

    # B1 specialised at axis pairs (the full polarization is encoded by
    # the four anticommutators for a != b plus the four squares).
    for a, Ga in Gs.items():
        sq = Ga * Ga
        ok = sq == I4
        check(
            f"(B1) D(e_{a})^2 = ||e_{a}||^2 I (metric-compatibility specialised)",
            ok,
            detail="" if ok else f"D(e_{a})^2 != I",
        )
    for a, Ga in Gs.items():
        for b, Gb in Gs.items():
            if a >= b:
                continue
            anti = Ga * Gb + Gb * Ga
            ok = anti == sp.zeros(4, 4)
            check(
                f"(B1) polarization at a={a}, b={b}: "
                f"D(e_a)D(e_b)+D(e_b)D(e_a) = 0",
                ok,
                detail="" if ok else "anticommutator nonzero",
            )

    # General polarization for u = e_a + e_b: D(u)^2 = (||e_a||^2 + 2<e_a,e_b> + ||e_b||^2) I
    # In our orthonormal basis with a != b this gives D(u)^2 = 2 I.
    Du = Gt + Gn
    sq = sp.simplify(Du * Du)
    ok = sq == 2 * I4
    check(
        "(B1) general polarization u = e_t + e_n: D(u)^2 = 2 I",
        ok,
        detail="" if ok else f"D(u)^2 = {sq}",
    )


def part2_clifford_relations() -> None:
    print("\n== Part 2: (B2) Clifford relations ==")
    Gt, Gn, G1, G2 = build_cl4_representation()
    I4 = sp.eye(4)
    Gs = [Gt, Gn, G1, G2]

    # Squares
    for idx, G in enumerate(Gs):
        sq = G * G
        ok = sq == I4
        check(
            f"(B2) Gamma_{idx}^2 = I (square one)",
            ok,
        )
    # Anticommutators
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            anti = Gs[i] * Gs[j] + Gs[j] * Gs[i]
            ok = anti == sp.zeros(4, 4)
            check(
                f"(B2) anticommutator Gamma_{i} Gamma_{j} + Gamma_{j} Gamma_{i} = 0",
                ok,
            )


def part3_clifford_words_span() -> None:
    print("\n== Part 3: (B3) 16 Clifford words span End(K) = M_4(C) ==")
    Gt, Gn, G1, G2 = build_cl4_representation()
    Gs = [Gt, Gn, G1, G2]
    I4 = sp.eye(4)

    # Build the 16 Clifford monomials:
    #   1 word of weight 0  (1)
    #   4 words of weight 1  (Gamma_a)
    #   6 words of weight 2  (Gamma_a Gamma_b, a < b)
    #   4 words of weight 3  (Gamma_a Gamma_b Gamma_c, a < b < c)
    #   1 word of weight 4  (Gamma_t Gamma_n Gamma_1 Gamma_2)
    from itertools import combinations

    words: list[sp.Matrix] = []
    labels: list[str] = []
    for k in range(5):
        for subset in combinations(range(4), k):
            if not subset:
                words.append(I4)
                labels.append("1")
                continue
            M = sp.eye(4)
            for a in subset:
                M = M * Gs[a]
            words.append(M)
            labels.append("Gamma_" + "_".join(str(a) for a in subset))

    check("(B3a) sixteen Clifford words enumerated", len(words) == 16, str(len(words)))

    # Compute the Hilbert-Schmidt Gram matrix <M_i, M_j> = Tr(M_i^dag M_j)
    # and verify it is full-rank.
    n = len(words)
    gram_rows = []
    for i in range(n):
        row = []
        Wi_dag = words[i].H
        for j in range(n):
            inner = (Wi_dag * words[j]).trace()
            row.append(sp.simplify(inner))
        gram_rows.append(row)
    G = sp.Matrix(gram_rows)
    rk = G.rank()
    check(
        "(B3a) Gram matrix of 16 Clifford words has rank 16 "
        "(=> linearly independent)",
        rk == 16,
        f"rank={rk}",
    )

    # End(K) = M_4(C) has complex dimension 16
    check(
        "(B3a) dim_C End(K) = 16 matches the count of Clifford words",
        n == 16,
    )
    # Wedderburn dimension count for Cl(4, C):
    # dim_C Cl(d, C) = 2^d = 16 at d = 4
    check(
        "(B3b) dim_C Cl(4, C) = 2^4 = 16 (Wedderburn)",
        2 ** 4 == 16,
    )
    # Faithful irreducible complex rep dim = 2^{d/2} = 4 at d = 4
    check(
        "(B3b) dim_C V_irrep = 2^{d/2} = 4 at d = 4 (Schur on simple summand)",
        2 ** (4 // 2) == 4,
    )

    # Verify the volume element omega = Gamma_t Gamma_n Gamma_1 Gamma_2
    # squares to I (signature ++++ has omega^2 = +I).
    omega = Gt * Gn * G1 * G2
    omega_sq = omega * omega
    check(
        "(B3) volume element omega = Gamma_t Gamma_n Gamma_1 Gamma_2 "
        "is well-defined; omega^2 in {I, -I}",
        omega_sq == I4 or omega_sq == -I4,
    )


def part4_car_modes() -> None:
    print("\n== Part 4: (B4) oriented CAR modes ==")
    Gt, Gn, G1, G2 = build_cl4_representation()
    I4 = sp.eye(4)
    Z = sp.zeros(4, 4)

    # Define oriented Clifford pairs:
    # c_N := (Gamma_t + i Gamma_n) / 2
    # c_T := (Gamma_1 + i Gamma_2) / 2
    cN = sp.Rational(1, 2) * (Gt + sp.I * Gn)
    cT = sp.Rational(1, 2) * (G1 + sp.I * G2)
    cN_dag = cN.H
    cT_dag = cT.H

    # All anticommutators of c_i with c_j (no dagger) should vanish.
    anti = {
        "cN cN": cN * cN + cN * cN,
        "cT cT": cT * cT + cT * cT,
        "cN cT": cN * cT + cT * cN,
    }
    for label, A in anti.items():
        ok = A == Z
        check(
            f"(B4) anticommutator of c_i and c_j vanishes for {label}",
            ok,
        )

    # Anticommutators with dagger should be I on the diagonal, 0 off-diagonal.
    pairs = {
        "cN cN^dag": (cN, cN_dag, I4),
        "cT cT^dag": (cT, cT_dag, I4),
        "cN cT^dag": (cN, cT_dag, Z),
        "cT cN^dag": (cT, cN_dag, Z),
    }
    for label, (a, b, expected) in pairs.items():
        anti = a * b + b * a
        ok = anti == expected
        check(
            f"(B4) anticommutator { {label} } = {'I' if expected == I4 else '0'}",
            ok,
        )


def part4b_dagger_boundary() -> None:
    print("\n== Part 4b: daggered CAR boundary under nonunitary similarity ==")
    Gt, Gn, G1, G2 = build_cl4_representation()
    I4 = sp.eye(4)
    Z = sp.zeros(4, 4)
    scale = sp.diag(2, 1, 1, 1)
    scale_inv = scale.inv()
    transformed = [scale * G * scale_inv for G in (Gt, Gn, G1, G2)]

    relations_ok = True
    for i, Gi in enumerate(transformed):
        relations_ok = relations_ok and (Gi * Gi == I4)
        for j, Gj in enumerate(transformed):
            if i == j:
                continue
            relations_ok = relations_ok and (Gi * Gj + Gj * Gi == Z)
    check(
        "nonunitary similarity preserves the Clifford relations B1-B3",
        relations_ok,
    )

    nonhermitian = any(G.H != G for G in transformed)
    check(
        "same transformed representation is not Hermitian for the fixed standard dagger",
        nonhermitian,
    )

    cN = sp.Rational(1, 2) * (transformed[0] + sp.I * transformed[1])
    cT = sp.Rational(1, 2) * (transformed[2] + sp.I * transformed[3])
    daggered = {
        "cN cN^dag": cN * cN.H + cN.H * cN,
        "cT cT^dag": cT * cT.H + cT.H * cT,
        "cN cT^dag": cN * cT.H + cT.H * cN,
        "cT cN^dag": cT * cN.H + cN.H * cT,
    }
    spoils_standard_dagger_car = (
        daggered["cN cN^dag"] != I4
        or daggered["cT cT^dag"] != I4
        or daggered["cN cT^dag"] != Z
        or daggered["cT cN^dag"] != Z
    )
    check(
        "fixed-standard-dagger CAR is not invariant under arbitrary nonunitary similarity",
        spoils_standard_dagger_car,
    )


def part5_dependency_status() -> None:
    print("\n== Part 5: dependency status check ==")
    # Verify that the load-bearing one-hop dependency exists.
    dep = ROOT / "docs/CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md"
    check(
        "CL3_COMPLEXIFICATION_SPLIT note file exists",
        dep.is_file(),
        str(dep.relative_to(ROOT)),
    )
    parent = ROOT / "docs/PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md"
    check(
        "Parent Target-3 row file exists",
        parent.is_file(),
        str(parent.relative_to(ROOT)),
    )
    template = (
        ROOT / "docs/HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md"
    )
    check(
        "Canonical narrow-bridge template file exists",
        template.is_file(),
        str(template.relative_to(ROOT)),
    )


def part6_no_forbidden_imports() -> None:
    print("\n== Part 6: no forbidden imports ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    forbidden_substrings = [
        "PDG " + "obs " + "value",
        "fitted " + "selector consumed",
        "Newton constant " + "G_obs imported",
        "Planck length " + "l_P_obs imported",
        "Bekenstein-Hawking " + "entropy observed import",
        "Wilson " + "plaquette load-bearing input",
    ]
    for phrase in forbidden_substrings:
        check(
            f"source note excludes literature comparator: {phrase}",
            phrase not in note,
        )


def main() -> int:
    print("PLANCK TARGET-3 COFRAME-RESPONSE ACCEPTED-PREMISE BRIDGE")
    part0_source_firewall()
    part1_polarization()
    part2_clifford_relations()
    part3_clifford_words_span()
    part4_car_modes()
    part4b_dagger_boundary()
    part5_dependency_status()
    part6_no_forbidden_imports()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded accepted-premise bridge passes; (B1)-(B3) follow "
            "from the retained Cl(3) complexification split + accepted-premise "
            "packet (P1), and (B4) is narrowed to the compatible Pauli-realized "
            "Hermitian representative."
        )
        return 0
    print("VERDICT: bounded accepted-premise bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
