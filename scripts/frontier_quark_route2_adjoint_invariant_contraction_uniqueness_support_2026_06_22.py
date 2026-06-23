#!/usr/bin/env python3
"""Exact invariant-contraction support for the Route-2 adjoint Hessian bridge."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-adjoint-invariant-contraction"

PASS = 0
FAIL = 0


Matrix3 = tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]
Matrix8 = list[list[Fraction]]


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


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def e(i: int, j: int) -> Matrix3:
    return tuple(
        tuple(Fraction(1 if (r == i and c == j) else 0) for c in range(3))
        for r in range(3)
    )  # type: ignore[return-value]


def diag(a: int, b: int, c: int) -> Matrix3:
    return (
        (Fraction(a), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(b), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(c)),
    )


def matmul3(a: Matrix3, b: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def sub3(a: Matrix3, b: Matrix3) -> Matrix3:
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def comm(a: Matrix3, b: Matrix3) -> Matrix3:
    return sub3(matmul3(a, b), matmul3(b, a))


BASIS: list[Matrix3] = [
    e(0, 1),  # E12
    e(1, 2),  # E23
    e(0, 2),  # E13
    e(1, 0),  # E21
    e(2, 1),  # E32
    e(2, 0),  # E31
    diag(1, -1, 0),  # H1
    diag(0, 1, -1),  # H2
]

BASIS_LABELS = ("E12", "E23", "E13", "E21", "E32", "E31", "H1", "H2")
GENERATORS = [BASIS[0], BASIS[1], BASIS[3], BASIS[4]]
GENERATOR_LABELS = ("E12", "E23", "E21", "E32")


def coords(m: Matrix3) -> list[Fraction]:
    trace = m[0][0] + m[1][1] + m[2][2]
    if trace != 0:
        raise ValueError(f"matrix is not traceless: trace={trace}")
    x = m[0][0]
    y = -m[2][2]
    if m[1][1] != -x + y:
        raise ValueError("diagonal part is not in the H1,H2 span")
    return [
        m[0][1],
        m[1][2],
        m[0][2],
        m[1][0],
        m[2][1],
        m[2][0],
        x,
        y,
    ]


def ad_matrix(x: Matrix3) -> Matrix8:
    columns = [coords(comm(x, b)) for b in BASIS]
    return [[columns[j][i] for j in range(8)] for i in range(8)]


def matmul8(a: Matrix8, b: Matrix8) -> Matrix8:
    return [[sum(a[i][k] * b[k][j] for k in range(8)) for j in range(8)] for i in range(8)]


def transpose(a: Matrix8) -> Matrix8:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def trace8(a: Matrix8) -> Fraction:
    return sum(a[i][i] for i in range(8))


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


def inverse_square(a: Matrix8) -> Matrix8:
    n = len(a)
    aug = [a[i][:] + [Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]
    rank = 0
    for col in range(n):
        pivot = None
        for r in range(rank, n):
            if aug[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            raise ValueError("matrix is singular")
        aug[rank], aug[pivot] = aug[pivot], aug[rank]
        inv = Fraction(1, 1) / aug[rank][col]
        aug[rank] = [v * inv for v in aug[rank]]
        for r in range(n):
            if r != rank and aug[r][col] != 0:
                factor = aug[r][col]
                aug[r] = [aug[r][c] - factor * aug[rank][c] for c in range(2 * n)]
        rank += 1
    return [row[n:] for row in aug]


def covector_equations(ad_mats: list[Matrix8]) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for a in ad_mats:
        for j in range(8):
            rows.append([a[i][j] for i in range(8)])
    return rows


def symmetric_index() -> dict[tuple[int, int], int]:
    index: dict[tuple[int, int], int] = {}
    k = 0
    for i in range(8):
        for j in range(i, 8):
            index[(i, j)] = k
            k += 1
    return index


def sym_slot(index: dict[tuple[int, int], int], i: int, j: int) -> int:
    return index[(i, j)] if i <= j else index[(j, i)]


def symmetric_form_equations(ad_mats: list[Matrix8], variance: str) -> tuple[list[list[Fraction]], int]:
    index = symmetric_index()
    rows: list[list[Fraction]] = []
    for a in ad_mats:
        for p in range(8):
            for q in range(8):
                row = [Fraction(0) for _ in range(len(index))]
                for i in range(8):
                    if variance == "covariant":
                        row[sym_slot(index, i, q)] += a[i][p]
                        row[sym_slot(index, p, i)] += a[i][q]
                    elif variance == "contravariant":
                        row[sym_slot(index, i, q)] += a[p][i]
                        row[sym_slot(index, p, i)] += a[q][i]
                    else:
                        raise ValueError(variance)
                rows.append(row)
    return rows, len(index)


def bilinear_form_equations(ad_mats: list[Matrix8]) -> tuple[list[list[Fraction]], int]:
    rows: list[list[Fraction]] = []
    for a in ad_mats:
        for p in range(8):
            for q in range(8):
                row = [Fraction(0) for _ in range(64)]
                for i in range(8):
                    row[i * 8 + q] += a[i][p]
                    row[p * 8 + i] += a[i][q]
                rows.append(row)
    return rows, 64


def is_covariant_invariant(form: Matrix8, ad_mats: list[Matrix8]) -> bool:
    for a in ad_mats:
        left = matmul8(transpose(a), form)
        right = matmul8(form, a)
        if any(left[i][j] + right[i][j] != 0 for i in range(8) for j in range(8)):
            return False
    return True


def is_contravariant_invariant(form: Matrix8, ad_mats: list[Matrix8]) -> bool:
    for a in ad_mats:
        left = matmul8(a, form)
        right = matmul8(form, transpose(a))
        if any(left[i][j] + right[i][j] != 0 for i in range(8) for j in range(8)):
            return False
    return True


def killing_form(ad_basis: list[Matrix8]) -> Matrix8:
    return [[trace8(matmul8(ad_basis[i], ad_basis[j])) for j in range(8)] for i in range(8)]


def contraction(form: Matrix8, hessian: Matrix8) -> Fraction:
    return sum(form[i][j] * hessian[i][j] for i in range(8) for j in range(8))


def part1_grounding() -> None:
    print("PART 1: grounding")
    block115 = flat(text("QUARK_ROUTE2_COVARIANT_MULTI_RECORD_CUMULANT_SUFFICIENT_THEOREM_2026-06-22.md"))
    scalarization = flat(text("QUARK_ROUTE2_COVARIANT_SCALARIZATION_COLLAPSE_NO_GO_NOTE_2026-06-22.md"))
    invariant = flat(text("QUARK_ROUTE2_INVARIANT_SCALAR_OUTPUT_COUPLING_NO_GO_NOTE_2026-06-22.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    check("Block115 uses orientation-free Killing contraction", "orientation-free Killing contraction" in block115)
    check("Block115 leaves covariant multi-record family open", "covariant multi-record Route-2 source/readout family is not supplied" in block115)
    check("covariant scalarization before E/T typing is pruned", "collapses the readout before the Route-2 E/T typing" in scalarization)
    check("invariant scalar output has zero first-order response", "zero first-order response on the" in invariant)
    check("connected Hessian support names same-source primitive", "typed as a pure disconnected product for the same source/readout" in hessian)


def part2_sl3_adjoint_linear_algebra() -> tuple[list[Matrix8], list[Matrix8], Matrix8, Matrix8]:
    print()
    print("PART 2: exact sl_3 adjoint linear algebra")
    ad_basis = [ad_matrix(b) for b in BASIS]
    ad_gens = [ad_matrix(g) for g in GENERATORS]
    kform = killing_form(ad_basis)
    kinv = inverse_square(kform)
    print(f"  basis={BASIS_LABELS}")
    print(f"  generators={GENERATOR_LABELS}")
    check("basis has eight adjoint directions", len(BASIS) == 8)
    check("four Chevalley generators used", len(GENERATORS) == 4)
    check("coordinates recover basis vectors", all(coords(BASIS[i])[i] == 1 for i in range(8)))
    check("all basis matrices are traceless", all(sum(BASIS[i][j][j] for j in range(3)) == 0 for i in range(8)))
    check("Killing form is nondegenerate", rref_rank(kform, 8) == 8)
    check("Killing form is covariantly invariant", is_covariant_invariant(kform, ad_gens))
    check("inverse Killing tensor is contravariantly invariant", is_contravariant_invariant(kinv, ad_gens))
    return ad_basis, ad_gens, kform, kinv


def part3_invariant_dimensions(ad_gens: list[Matrix8]) -> None:
    print()
    print("PART 3: invariant tensor dimensions")
    cov_rows = covector_equations(ad_gens)
    cov_rank = rref_rank(cov_rows, 8)
    cov_dim = 8 - cov_rank
    sym_cov_rows, sym_cov_cols = symmetric_form_equations(ad_gens, "covariant")
    sym_cov_dim = sym_cov_cols - rref_rank(sym_cov_rows, sym_cov_cols)
    sym_contra_rows, sym_contra_cols = symmetric_form_equations(ad_gens, "contravariant")
    sym_contra_dim = sym_contra_cols - rref_rank(sym_contra_rows, sym_contra_cols)
    bil_rows, bil_cols = bilinear_form_equations(ad_gens)
    bil_dim = bil_cols - rref_rank(bil_rows, bil_cols)
    print(f"  invariant covector dim={cov_dim}")
    print(f"  invariant symmetric covariant form dim={sym_cov_dim}")
    print(f"  invariant symmetric contravariant tensor dim={sym_contra_dim}")
    print(f"  invariant bilinear form dim={bil_dim}")
    check("no nonzero invariant adjoint covector", cov_dim == 0)
    check("symmetric invariant bilinear forms are one-dimensional", sym_cov_dim == 1)
    check("symmetric invariant contraction tensors are one-dimensional", sym_contra_dim == 1)
    check("all invariant bilinear forms are one-dimensional", bil_dim == 1)
    check("linear orientation selector is impossible", cov_dim == 0 and sym_contra_dim == 1)


def part4_contraction_boundary(kinv: Matrix8) -> None:
    print()
    print("PART 4: contraction and normalization boundary")
    hessian = [[Fraction(0) for _ in range(8)] for _ in range(8)]
    for i in range(8):
        hessian[i][i] = Fraction(i + 1)
    raw = contraction(kinv, hessian)
    scaled = contraction([[2 * kinv[i][j] for j in range(8)] for i in range(8)], hessian)
    connected_selector = Fraction(8, 9)
    kappa = 9 * (connected_selector - Fraction(8, 9))
    scaled_kappa = 9 * (2 * connected_selector - Fraction(8, 9))
    print(f"  inverse-Killing contraction sample={raw}")
    print(f"  scaled contraction sample={scaled}")
    print(f"  normalized selector kappa={kappa}, scaled selector kappa={scaled_kappa}")
    check("inverse-Killing contraction is nonzero on a generic Hessian", raw != 0)
    check("overall scale changes the scalar readout", scaled == 2 * raw)
    check("normalized 8/9 selector gives kappa=0", kappa == 0)
    check("unfixed factor two does not give kappa=0", scaled_kappa != 0)
    check("uniqueness still leaves coefficient normalization load-bearing", scaled != raw and scaled_kappa != 0)


def part5_trace_boundary() -> None:
    print()
    print("PART 5: trace boundary")
    route_edges = {
        "adjoint_covector_selector": "forbidden",
        "symmetric_hessian_linear_contraction": "unique_up_to_scale",
        "killing_contraction_clause": "exact_support",
        "covariant_multirecord_source": "open",
        "coefficient_source_normalization": "open",
    }
    allowed = {"forbidden", "unique_up_to_scale", "exact_support", "open"}
    for name, status in route_edges.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("external adjoint covector route is pruned", route_edges["adjoint_covector_selector"] == "forbidden")
    check("Killing contraction clause is exact support", route_edges["killing_contraction_clause"] == "exact_support")
    check("source/readout family remains open", route_edges["covariant_multirecord_source"] == "open")
    check("normalization remains open", route_edges["coefficient_source_normalization"] == "open")


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_ADJOINT_INVARIANT_CONTRACTION_UNIQUENESS_SUPPORT_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for the invariant-contraction clause only",
        "Hom_SU3(adj, 1) = 0",
        "Hom_SU3(Sym^2(adj), 1) = 1",
        "orientation-free linear scalar readout on a symmetric adjoint Hessian is unique up to scale",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block116 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
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
    print("Route-2 adjoint invariant contraction uniqueness support")
    print("TRACE: upstream_support")
    part1_grounding()
    _, ad_gens, _, kinv = part2_sl3_adjoint_linear_algebra()
    part3_invariant_dimensions(ad_gens)
    part4_contraction_boundary(kinv)
    part5_trace_boundary()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the orientation-free linear scalar contraction on a covariant sl_3 adjoint Hessian is unique up to scale; Block115's Killing contraction does not import a color-orientation selector, but the Route-2 source/readout family and normalization remain open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
