#!/usr/bin/env python3
"""Canonical two-cell family / generation CTX discharge / EW instance verifier.

Bounded support runner for
docs/CTX_CANONICAL_TWO_CELL_FAMILY_GENERATION_DISCHARGE_EW_INSTANCE_BOUNDED_NOTE_2026-07-02.md.

Scope (finite, exact arithmetic; Python3 stdlib only). This runner checks only:

  * source guards: the landed C3 canonical-context Definition sentences, the
    ratified two-namings sentence, the parent kappa note's Pi_phys family and
    8/9 count sentence, and the current axiom memo's two distinction clauses
    plus its content-determination clause are present (whitespace-normalized);
  * T1: the canonical two-cell frame on the supplied hw=1 C3 circulant span --
    Hilbert-Schmidt norms ||I||^2 = 3, ||B||^2 = 6, <I,B> = 0 with
    B = J - I = U + U^2, and every supplied slot-relabeling *-automorphism
    (all six S3 permutation matrices) fixes the unit I and preserves B;
  * T2: the common factor N = 3 identity (channel energies = 3 x registered
    weights) and the invariance of every equal-cell condition under that
    factor, on exact rational samples;
  * T3: the EW color instance on M_3(C) with the HS inner product -- Tr(I_3)=3,
    HS norm^2(I_3)=3, dim(traceless)=3^2-1=8 (exact rank over Q of an exhibited
    traceless basis), I_3 HS-orthogonal to the traceless subspace, the exact
    fraction 8/9 = (3^2-1)/3^2, and conjugation by all six 3x3 permutation
    matrices fixing I_3, preserving tracelessness, and preserving pairwise HS
    inner products;
  * T3/T4: the block11 additive normal form Pi = x_C + kappa*x_S is content
    determined, its equal-cell-content ratios are kappa-independent, and its
    off-diagonal ratios are kappa-sensitive (the honest load-bearing premise);
  * boundary greps confirming the generated note carries its no-verdict/
    no-closure/review-pending/instance-premise firewall language.

It does NOT close the kappa wall, claim any value of kappa_EW, adjudicate any
review-pending block (08/11/16/17/18), set or predict audit status, or modify
any axiom, primitive, policy, or registry surface. The T3 EW instance is a
named premise for which finite witnesses are exhibited, not a ruling.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import itertools
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
C3_NOTE = DOCS / "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md"
KAPPA_NOTE = DOCS / "EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md"
AXIOM_MEMO = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_POLICY = DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md"
THIS_NOTE = DOCS / "CTX_CANONICAL_TWO_CELL_FAMILY_GENERATION_DISCHARGE_EW_INSTANCE_BOUNDED_NOTE_2026-07-02.md"

PASS = 0
FAIL = 0
_N = 0


def check(desc: str, ok: bool, detail: str = "") -> bool:
    """Emit one CHECK NN: PASS/FAIL -- <desc> line and tally."""
    global PASS, FAIL, _N
    _N += 1
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" [{detail}]" if detail else ""
    print(f"CHECK {_N:02d}: {tag} -- {desc}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def squash(text: str) -> str:
    """Whitespace-normalized text for robust containment tests."""
    return " ".join(text.split())


# --------------------------------------------------------------------------
# exact real-matrix helpers (all matrices here are integer/rational, so the
# adjoint * coincides with the transpose and HS<A,B> = Tr(A^T B) = sum A_ij B_ij)
# --------------------------------------------------------------------------
def mat_mul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def hs(A, B):
    """Hilbert-Schmidt inner product Tr(A^T B) for real matrices."""
    return sum(A[i][j] * B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def conj_by(P, X):
    """*-automorphism X -> P X P^{-1}; P a permutation matrix so P^{-1}=P^T."""
    return mat_mul(mat_mul(P, X), transpose(P))


def rank_q(rows):
    """Exact rank over Q of a list of row vectors (Fraction Gaussian elim)."""
    M = [[Fraction(v) for v in r] for r in rows]
    n_rows = len(M)
    n_cols = len(M[0]) if M else 0
    rank = 0
    pivot_col = 0
    for _ in range(n_rows):
        if pivot_col >= n_cols:
            break
        # find a pivot
        piv = None
        for r in range(rank, n_rows):
            if M[r][pivot_col] != 0:
                piv = r
                break
        if piv is None:
            pivot_col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = M[rank][pivot_col]
        M[rank] = [x / inv for x in M[rank]]
        for r in range(n_rows):
            if r != rank and M[r][pivot_col] != 0:
                f = M[r][pivot_col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
        pivot_col += 1
    return rank


def permutation_matrices_3():
    """The six 3x3 permutation matrices (S_3), including the cyclic shifts."""
    mats = []
    for p in itertools.permutations(range(3)):
        P = [[1 if p[i] == j else 0 for j in range(3)] for i in range(3)]
        mats.append(P)
    return mats


# --------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print("CTX CANONICAL TWO-CELL FAMILY / GENERATION DISCHARGE / EW INSTANCE")
    print("bounded support runner -- exact arithmetic, stdlib only")
    print("=" * 78)

    c3 = squash(C3_NOTE.read_text(encoding="utf-8"))
    kap = squash(KAPPA_NOTE.read_text(encoding="utf-8"))
    ax = squash(AXIOM_MEMO.read_text(encoding="utf-8"))

    # ----------------------------------------------------------------------
    section("Source guards (landed on-main docs; whitespace-normalized)")

    check(
        "C3 note: singlet-cell Definition sentence present",
        "the **singlet cell**: the algebra unit direction" in c3,
    )
    check(
        "C3 note: doublet-cell Definition sentence present",
        "the **doublet cell**: the Hilbert-Schmidt orthocomplement" in c3,
    )
    check(
        "C3 note: HS normalization ||I||^2 = 3 present",
        "||I||^2 = 3" in c3,
    )
    check(
        "C3 note: common-factor cancellation sentence present",
        "same quadratic contents up to the common factor" in c3,
    )
    check(
        "C3 note: ratified two-namings-of-the-same-two-cells sentence present",
        "two namings of the same two cells of this one context, not two independent structures"
        in c3,
    )
    check(
        "kappa note: Pi_phys = C + kappa_EW S family present",
        "Pi_phys = C + kappa_EW S" in kap,
    )
    check(
        "kappa note: 8/9 central-sector cardinality-count sentence present",
        "central-sector partition gives the cardinality count `8/9`" in kap,
    )
    check(
        "axiom memo: both distinction clauses + content-determination clause present",
        ("Sites are distinguished by the supplied lattice structure alone" in ax)
        and ("Possibilities are distinguished by the supplied algebraic structure alone" in ax)
        and ("A readout value is determined by record content alone" in ax),
    )

    # ----------------------------------------------------------------------
    section("T1 -- canonical two-cell frame on the supplied hw=1 C3 circulant")

    I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    U = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]  # cyclic shift, U^3 = I
    U2 = mat_mul(U, U)
    J = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]  # all-ones circulant = I + U + U^2
    B = [[J[i][j] - I3[i][j] for j in range(3)] for i in range(3)]  # doublet cell

    b_is_uu2 = B == [[U[i][j] + U2[i][j] for j in range(3)] for i in range(3)]
    check(
        "C3 unit cell: HS norm^2 of the unit direction I equals 3",
        hs(I3, I3) == 3,
        detail=f"||I||^2={hs(I3, I3)}",
    )
    check(
        "C3 doublet cell = HS-orthocomplement of unit: B=J-I=U+U^2, ||B||^2=6, <I,B>=0",
        b_is_uu2 and hs(B, B) == 6 and hs(I3, B) == 0,
        detail=f"||B||^2={hs(B, B)}, <I,B>={hs(I3, B)}",
    )

    perms = permutation_matrices_3()
    frame_fixed = True
    for P in perms:
        if conj_by(P, I3) != I3 or conj_by(P, B) != B:
            frame_fixed = False
            break
    check(
        "C3 frame is supplied-structure-carried: all 6 slot-relabeling "
        "*-automorphisms fix the unit I and preserve the doublet B",
        frame_fixed,
        detail=f"{len(perms)} permutation-matrix automorphisms",
    )

    # ----------------------------------------------------------------------
    section("T2 -- common factor N=3 and equal-cell-condition invariance")

    # channel energies (3a^2, 6|b|^2) = 3 * registered weights (a^2, 2|b|^2),
    # |b|^2 = br^2 + bi^2 (complex b as a pair of exact Fractions).
    samples_ab = [
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(1), Fraction(1)),
        (Fraction(3, 2), Fraction(-1, 2), Fraction(2, 3)),
        (Fraction(-5, 3), Fraction(4), Fraction(-1)),
        (Fraction(0), Fraction(7, 4), Fraction(0)),
    ]
    factor_ok = True
    for a, br, bi in samples_ab:
        b2 = br * br + bi * bi
        weights = (a * a, 2 * b2)
        energies = (3 * a * a, 6 * b2)
        if energies != (3 * weights[0], 3 * weights[1]):
            factor_ok = False
            break
    check(
        "channel energies (3a^2, 6|b|^2) = 3*(a^2, 2|b|^2) exactly on rational samples",
        factor_ok,
        detail=f"{len(samples_ab)} samples, |b|^2 = br^2 + bi^2",
    )

    # equal-cell condition a^2 = 2|b|^2 iff 3a^2 = 6|b|^2 (factor cancels)
    equal_cell_samples = [
        (Fraction(2), Fraction(1), Fraction(1)),      # 4 == 2*2 -> equal
        (Fraction(2), Fraction(-1), Fraction(1)),     # 4 == 2*2 -> equal
        (Fraction(1), Fraction(1), Fraction(0)),      # 1 != 2   -> unequal
        (Fraction(3), Fraction(1), Fraction(2)),      # 9 != 10  -> unequal
    ]
    biconditional_ok = True
    for a, br, bi in equal_cell_samples:
        b2 = br * br + bi * bi
        cond_weight = (a * a == 2 * b2)
        cond_energy = (3 * a * a == 6 * b2)
        if cond_weight != cond_energy:
            biconditional_ok = False
            break
    check(
        "equal-cell condition invariant under the N=3 factor: (a^2=2|b|^2) iff (3a^2=6|b|^2)",
        biconditional_ok,
        detail=f"{len(equal_cell_samples)} samples (equal and unequal cases)",
    )

    # ----------------------------------------------------------------------
    section("T3 -- EW color instance: M_3(C) with the HS inner product")

    check(
        "M_3 unit: Tr(I_3) = 3 and HS norm^2(I_3) = 3",
        trace(I3) == 3 and hs(I3, I3) == 3,
        detail=f"Tr(I_3)={trace(I3)}, ||I_3||^2={hs(I3, I3)}",
    )

    # exhibit 8 exact linearly-independent traceless matrices in M_3
    traceless = []
    for i in range(3):
        for j in range(3):
            if i != j:
                E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                E[i][j] = 1
                traceless.append(E)  # 6 off-diagonal matrix units
    traceless.append([[1, 0, 0], [0, -1, 0], [0, 0, 0]])   # diag(1,-1,0)
    traceless.append([[0, 0, 0], [0, 1, 0], [0, 0, -1]])   # diag(0,1,-1)
    all_traceless = all(trace(T) == 0 for T in traceless)
    coord = [[T[i][j] for i in range(3) for j in range(3)] for T in traceless]
    r = rank_q(coord)
    check(
        "dim(traceless subspace) = 3^2 - 1 = 8: 8 exhibited traceless matrices, exact rank over Q = 8",
        len(traceless) == 8 and all_traceless and r == 8,
        detail=f"count={len(traceless)}, rank_Q={r}",
    )

    # I_3 HS-orthogonal to the traceless subspace: basis + random rational combos
    ortho_basis = all(hs(I3, T) == 0 for T in traceless)
    combos_ok = True
    combo_coeffs = [
        [Fraction(1, 2), Fraction(-3), Fraction(0), Fraction(5, 4), Fraction(2),
         Fraction(-1), Fraction(7, 3), Fraction(-2, 5)],
        [Fraction(-4), Fraction(1), Fraction(6, 7), Fraction(0), Fraction(-9, 2),
         Fraction(3), Fraction(1, 8), Fraction(11)],
    ]
    for coeffs in combo_coeffs:
        Tcomb = [[sum(coeffs[k] * traceless[k][i][j] for k in range(8)) for j in range(3)] for i in range(3)]
        if trace(Tcomb) != 0 or hs(I3, Tcomb) != 0:
            combos_ok = False
            break
    check(
        "I_3 is HS-orthogonal to the traceless subspace: Tr(I_3^* T)=0 on the 8 basis + random rational combos",
        ortho_basis and combos_ok,
    )

    check(
        "cardinality fraction 8/9 = (3^2 - 1)/3^2 exactly (parent's own count; ledger's own formula)",
        Fraction(8, 9) == Fraction(3 ** 2 - 1, 3 ** 2),
    )

    fix_unit = all(conj_by(P, I3) == I3 for P in perms)
    check(
        "automorphism-canonical unit: conjugation by all 6 permutation matrices fixes I_3",
        fix_unit,
        detail=f"{len(perms)} permutations",
    )

    preserve_traceless = True
    for P in perms:
        for T in traceless:
            if trace(conj_by(P, T)) != 0:
                preserve_traceless = False
                break
        if not preserve_traceless:
            break
    check(
        "automorphism-canonical complement: all 6 permutation conjugations preserve tracelessness",
        preserve_traceless,
    )

    # HS inner-product preservation under conjugation, on a sampled set
    sample_set = [
        I3,
        B,
        traceless[0], traceless[1], traceless[6], traceless[7],
        [[1, 2, 3], [0, -1, 4], [5, 6, 0]],   # generic integer matrix
        [[2, -1, 0], [3, 1, -2], [1, 0, -3]],
    ]
    hs_preserved = True
    for P in perms:
        for X in sample_set:
            for Y in sample_set:
                if hs(conj_by(P, X), conj_by(P, Y)) != hs(X, Y):
                    hs_preserved = False
                    break
            if not hs_preserved:
                break
        if not hs_preserved:
            break
    check(
        "HS inner product preserved by all 6 permutation conjugations on the sampled set (exact integer)",
        hs_preserved,
        detail=f"{len(sample_set)} sampled matrices",
    )

    # ----------------------------------------------------------------------
    section("T3/T4 -- block11 normal form Pi = x_C + kappa*x_S on the instance")

    def pi(xc, xs, kappa):
        return xc + kappa * xs

    # content-determined additive form: linear superposition in (x_C, x_S),
    # and the count-level toggle Pi(0)=C, Pi(1)=C+S at kappa=1.
    linear_ok = True
    kappas = [Fraction(0), Fraction(1), Fraction(3), Fraction(-2, 5), Fraction(7, 3)]
    lin_samples = [
        (Fraction(1), Fraction(2), Fraction(3), Fraction(-1), Fraction(2), Fraction(5)),
        (Fraction(-3, 2), Fraction(4), Fraction(1, 3), Fraction(5), Fraction(-1, 4), Fraction(2)),
    ]
    for k in kappas:
        for xc1, xs1, xc2, xs2, al, be in lin_samples:
            lhs = pi(al * xc1 + be * xc2, al * xs1 + be * xs2, k)
            rhs = al * pi(xc1, xs1, k) + be * pi(xc2, xs2, k)
            if lhs != rhs:
                linear_ok = False
    # count-level toggle at kappa = 1: Pi(0)=C, Pi(1)=C+S
    Cval, Sval = Fraction(11, 4), Fraction(-7, 3)
    toggle_ok = (pi(Cval, Fraction(0), Fraction(1)) == Cval) and (pi(Cval, Sval, Fraction(1)) == Cval + Sval)
    check(
        "block11 normal form Pi = x_C + kappa*x_S is content-determined/additive and "
        "reproduces the count toggle Pi(0)=C, Pi(1)=C+S at kappa=1",
        linear_ok and toggle_ok,
    )

    # equal-cell-content states (x_C = x_S): ratio kappa-independent for >=3 kappas
    eq_states = [(Fraction(3), Fraction(3)), (Fraction(-5, 2), Fraction(-5, 2)), (Fraction(4, 7), Fraction(4, 7))]
    diag_kappas = [Fraction(0), Fraction(1), Fraction(3), Fraction(9, 2)]
    diag_ok = True
    for (a1, s1), (a2, s2) in itertools.combinations(eq_states, 2):
        ratios = set()
        for k in diag_kappas:
            d = pi(a2, s2, k)
            if d == 0:
                continue
            ratios.add(pi(a1, s1, k) / d)
        if len(ratios) != 1:
            diag_ok = False
            break
    check(
        "diagonal (equal-cell-content x_C=x_S) ratios are kappa-independent across >=3 kappa values "
        "(parent's own K_EW-cancellation structure)",
        diag_ok,
        detail=f"{len(diag_kappas)} kappa values",
    )

    # off-diagonal (x_C != x_S): ratio is genuinely kappa-sensitive (honest premise)
    s_a, s_b = (Fraction(1), Fraction(2)), (Fraction(3), Fraction(1))  # unequal contents
    off_ratios = set()
    for k in [Fraction(0), Fraction(1), Fraction(3)]:
        d = pi(s_b[0], s_b[1], k)
        off_ratios.add(pi(s_a[0], s_a[1], k) / d)
    check(
        "off-diagonal (x_C != x_S) ratio is kappa-sensitive: the honest load-bearing premise "
        "(off-diagonal evaluation carries w's content)",
        len(off_ratios) >= 2,
        detail=f"{len(off_ratios)} distinct ratios",
    )

    # ----------------------------------------------------------------------
    section("Boundary greps on the generated note (firewall language)")

    if THIS_NOTE.exists():
        note_raw = THIS_NOTE.read_text(encoding="utf-8")
        note = squash(note_raw)
        needed = ["nothing is adjudicated", "not closed", "review-pending", "instance premise", "one named premise rung"]
        missing = [s for s in needed if s not in note]
        check(
            "note carries firewall phrases: 'nothing is adjudicated', 'not closed', "
            "'review-pending', 'instance premise'",
            not missing,
            detail="all present" if not missing else f"missing: {missing}",
        )
        check(
            "note metadata uses canonical Type/Claim type and audit boundary, with no legacy status-authority fields",
            ("**Type:** bounded_theorem" in note_raw)
            and ("**Claim type:** bounded_theorem" in note_raw)
            and ("**Audit boundary:** independent audit lane only" in note_raw)
            and ("**Scope boundary:**" in note_raw)
            and ("**Status authority:**" not in note_raw)
            and ("**Actual current surface status:**" not in note_raw),
        )
        dependency_links = [
            "[`docs/C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`](C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md)",
            "[`docs/EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)",
            "[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)",
            "[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)",
        ]
        check(
            "load-bearing dependency surfaces are markdown links for citation-graph seeding",
            all(link in note_raw for link in dependency_links),
        )
        linked_siblings = [
            token for token in ("#4823", "#4826", "#4846", "#4849", "#4852")
            if f"]({token}" in note_raw or f"](.{token}" in note_raw
        ]
        check(
            "review-pending sibling PRs are PR-number context only, not markdown dependency links",
            ("Review-pending PR-number context only" in note_raw) and not linked_siblings,
            detail="none linked" if not linked_siblings else f"linked: {linked_siblings}",
        )
    else:
        check(
            "note carries firewall phrases (note file present)",
            False,
            detail=f"note not found at {THIS_NOTE.name}",
        )

    # Post-refutation guards (checks 25-26)
    import json
    ledger_path = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
    ledger_ok = False
    try:
        data = json.loads(ledger_path.read_text(encoding="utf-8"))
        rows = data if isinstance(data, list) else data.get("rows", data.get("claims", []))
        if isinstance(rows, dict):
            rows = list(rows.values())
        for row in rows:
            rid = str(row.get("claim_id", row.get("id", "")))
            if "ew_kappa_weighting_not_axiom_derivable" in rid:
                ledger_ok = "8/9 = (3^2 - 1)/3^2" in str(row.get("verdict_rationale", ""))
                break
    except Exception:
        ledger_ok = False
    check(
        "ledger guard: the parent kappa row's rationale spells 8/9 = (3^2 - 1)/3^2",
        ledger_ok,
    )
    policy_text = AXIOM_POLICY.read_text(encoding="utf-8")
    check(
        "ratification-record guard: policy section 6 names the C3 canonical definition note",
        "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md" in policy_text,
    )

    # ----------------------------------------------------------------------
    print()
    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
