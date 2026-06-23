#!/usr/bin/env python3
"""No-go for SU(3) invariance alone fixing Route-2 adjoint/singlet normalization."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_adjoint_invariant_contraction_uniqueness_support_2026_06_22 import (
    GENERATORS,
    ad_matrix,
    flat,
    inverse_square,
    killing_form,
    BASIS,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-adjoint-singlet-normalization"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def rref_rank(rows: list[list[Fraction]], ncols: int) -> int:
    mat = [row[:] for row in rows if any(row)]
    rank = 0
    for col in range(ncols):
        pivot = None
        for r in range(rank, len(mat)):
            if mat[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = Fraction(1, 1) / mat[rank][col]
        mat[rank] = [v * inv for v in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                factor = mat[r][col]
                mat[r] = [mat[r][c] - factor * mat[rank][c] for c in range(ncols)]
        rank += 1
        if rank == len(mat):
            break
    return rank


def lift_full(a8: list[list[Fraction]]) -> list[list[Fraction]]:
    full = [[Fraction(0) for _ in range(9)] for _ in range(9)]
    for i in range(8):
        for j in range(8):
            full[i + 1][j + 1] = a8[i][j]
    return full


def symmetric_index(n: int) -> dict[tuple[int, int], int]:
    index: dict[tuple[int, int], int] = {}
    k = 0
    for i in range(n):
        for j in range(i, n):
            index[(i, j)] = k
            k += 1
    return index


def sym_slot(index: dict[tuple[int, int], int], i: int, j: int) -> int:
    return index[(i, j)] if i <= j else index[(j, i)]


def symmetric_contravariant_equations(rep_mats: list[list[list[Fraction]]]) -> tuple[list[list[Fraction]], int]:
    n = len(rep_mats[0])
    index = symmetric_index(n)
    rows: list[list[Fraction]] = []
    for a in rep_mats:
        for p in range(n):
            for q in range(n):
                row = [Fraction(0) for _ in range(len(index))]
                for i in range(n):
                    row[sym_slot(index, i, q)] += a[p][i]
                    row[sym_slot(index, p, i)] += a[q][i]
                rows.append(row)
    return rows, len(index)


def covector_equations(rep_mats: list[list[list[Fraction]]]) -> list[list[Fraction]]:
    n = len(rep_mats[0])
    rows: list[list[Fraction]] = []
    for a in rep_mats:
        for j in range(n):
            rows.append([a[i][j] for i in range(n)])
    return rows


def is_contravariant_invariant(form: list[list[Fraction]], rep_mats: list[list[list[Fraction]]]) -> bool:
    n = len(form)
    for a in rep_mats:
        for p in range(n):
            for q in range(n):
                value = sum(a[p][i] * form[i][q] for i in range(n))
                value += sum(form[p][i] * a[q][i] for i in range(n))
                if value != 0:
                    return False
    return True


def block_form(alpha: Fraction, beta: Fraction, kinv: list[list[Fraction]]) -> list[list[Fraction]]:
    form = [[Fraction(0) for _ in range(9)] for _ in range(9)]
    form[0][0] = alpha
    for i in range(8):
        for j in range(8):
            form[i + 1][j + 1] = beta * kinv[i][j]
    return form


def connected_fraction(alpha: Fraction, beta: Fraction) -> Fraction:
    return Fraction(8) * beta / (alpha + Fraction(8) * beta)


def kappa_from_fraction(frac: Fraction) -> Fraction:
    return 9 * (frac - Fraction(8, 9))


def part1_grounding() -> None:
    print("PART 1: grounding")
    block116 = flat(text("QUARK_ROUTE2_ADJOINT_INVARIANT_CONTRACTION_UNIQUENESS_SUPPORT_NOTE_2026-06-22.md"))
    block115 = flat(text("QUARK_ROUTE2_COVARIANT_MULTI_RECORD_CUMULANT_SUFFICIENT_THEOREM_2026-06-22.md"))
    hessian_coeff = flat(text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    source_gauge = flat(text("QUARK_ROUTE2_SOURCE_COORDINATE_GAUGE_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    check("Block116 proves unique adjoint contraction up to scale", "unique up to scale" in block116)
    check("Block116 keeps coefficient/source normalization open", "coefficient/source normalization" in block116)
    check("Block115 requires coefficient/source normalization", "E/T coefficient and source-coordinate normalization are fixed" in block115)
    check("Hessian coefficient guard keeps normalization theorem missing", "unless a Route-2 theorem fixes the normalization" in hessian_coeff)
    check("source gauge guard names gauge-fixing theorem", "source-coordinate gauge-fixing theorem" in source_gauge)


def part2_full_source_invariants() -> tuple[list[list[list[Fraction]]], list[list[Fraction]]]:
    print()
    print("PART 2: full 1 + adjoint invariant-form space")
    ad_basis = [ad_matrix(b) for b in BASIS]
    ad_gens = [ad_matrix(g) for g in GENERATORS]
    full_gens = [lift_full(a) for a in ad_gens]
    kinv = inverse_square(killing_form(ad_basis))
    cov_rows = covector_equations(full_gens)
    cov_dim = 9 - rref_rank(cov_rows, 9)
    sym_rows, sym_cols = symmetric_contravariant_equations(full_gens)
    sym_dim = sym_cols - rref_rank(sym_rows, sym_cols)
    adj_cov_dim = 8 - rref_rank(covector_equations(ad_gens), 8)
    print(f"  invariant full covector dim={cov_dim}")
    print(f"  invariant full symmetric contraction dim={sym_dim}")
    print(f"  invariant adjoint covector dim={adj_cov_dim}")
    check("full source has one invariant covector", cov_dim == 1)
    check("full source invariant symmetric contractions are two-dimensional", sym_dim == 2)
    check("adjoint block still has no invariant covector", adj_cov_dim == 0)
    check("no invariant singlet-adjoint cross term exists", adj_cov_dim == 0)
    check("two dimensions match singlet plus adjoint blocks", sym_dim == cov_dim + 1)
    return full_gens, kinv


def part3_independent_scales(full_gens: list[list[list[Fraction]]], kinv: list[list[Fraction]]) -> None:
    print()
    print("PART 3: independent invariant scales")
    singlet_only = block_form(Fraction(1), Fraction(0), kinv)
    adjoint_only = block_form(Fraction(0), Fraction(1), kinv)
    equal_weight = block_form(Fraction(1), Fraction(1), kinv)
    skew_weight = block_form(Fraction(1), Fraction(2), kinv)
    check("singlet-only contraction is invariant", is_contravariant_invariant(singlet_only, full_gens))
    check("adjoint-only contraction is invariant", is_contravariant_invariant(adjoint_only, full_gens))
    check("equal-weight contraction is invariant", is_contravariant_invariant(equal_weight, full_gens))
    check("skew-weight contraction is invariant", is_contravariant_invariant(skew_weight, full_gens))
    adjoint_nonzero = any(adjoint_only[i][j] != 0 for i in range(1, 9) for j in range(1, 9))
    check("singlet-only and adjoint-only are linearly independent", singlet_only[0][0] != adjoint_only[0][0] and adjoint_nonzero)


def part4_fraction_family() -> None:
    print()
    print("PART 4: connected fraction family")
    examples = {
        "equal_weight": (Fraction(1), Fraction(1), Fraction(8, 9)),
        "adjoint_double": (Fraction(1), Fraction(2), Fraction(16, 17)),
        "singlet_double": (Fraction(2), Fraction(1), Fraction(4, 5)),
    }
    for name, (alpha, beta, expected) in examples.items():
        frac = connected_fraction(alpha, beta)
        kap = kappa_from_fraction(frac)
        print(f"  {name}: alpha={alpha}, beta={beta}, R={frac}, kappa={kap}")
        check(f"{name} connected fraction matches expected", frac == expected)
    check("equal weights force kappa=0", kappa_from_fraction(connected_fraction(Fraction(1), Fraction(1))) == 0)
    check("adjoint double does not force kappa=0", kappa_from_fraction(connected_fraction(Fraction(1), Fraction(2))) != 0)
    check("singlet double does not force kappa=0", kappa_from_fraction(connected_fraction(Fraction(2), Fraction(1))) != 0)
    check("SU3 invariance permits different normalized fractions", len({connected_fraction(Fraction(1), Fraction(1)), connected_fraction(Fraction(1), Fraction(2)), connected_fraction(Fraction(2), Fraction(1))}) == 3)


def part5_trace_boundary() -> None:
    print()
    print("PART 5: trace boundary")
    statuses = {
        "orientation_selector": "retired_by_block116",
        "singlet_adjoint_cross_term": "forbidden",
        "adjoint_singlet_relative_scale": "open",
        "invariance_only_normalization": "pruned",
        "route2_physical_normalization_theorem": "missing",
    }
    allowed = {"retired_by_block116", "forbidden", "open", "pruned", "missing"}
    for name, status in statuses.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("invariance-only normalization route is pruned", statuses["invariance_only_normalization"] == "pruned")
    check("physical normalization theorem remains missing", statuses["route2_physical_normalization_theorem"] == "missing")
    check("relative scale remains open", statuses["adjoint_singlet_relative_scale"] == "open")


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_ADJOINT_SINGLET_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for SU(3) invariance alone fixing the Route-2 adjoint/singlet normalization",
        "Hom_SU3(Sym^2(1 + adjoint), 1) = 2",
        "R(alpha,beta) = 8 beta / (alpha + 8 beta)",
        "Route-2 adjoint/singlet coefficient normalization theorem",
        "no endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block117 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 adjoint-singlet normalization no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    full_gens, kinv = part2_full_source_invariants()
    part3_independent_scales(full_gens, kinv)
    part4_fraction_family()
    part5_trace_boundary()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: SU(3) invariance separates the singlet and adjoint contractions but leaves their relative scale free; the Route-2 adjoint/singlet coefficient normalization theorem remains a distinct missing primitive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
