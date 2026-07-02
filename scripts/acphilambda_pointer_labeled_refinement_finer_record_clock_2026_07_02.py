#!/usr/bin/env python3
"""Exact checks for the pointer-labeled refinement and finer-record clock."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md"
SELF = ROOT / "scripts" / "acphilambda_pointer_labeled_refinement_finer_record_clock_2026_07_02.py"
BRANNEN = ROOT / "docs" / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
RECORD = ROOT / "docs" / "RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md"
KOIDE = ROOT / "docs" / "KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"[FAIL] {name}" + (f" -- {detail}" if detail else ""))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def exact(expr):
    return sp.simplify(sp.expand_trig(expr))


def exact_matrix(mat):
    return mat.applyfunc(exact)


def is_zero_matrix(mat) -> bool:
    return exact_matrix(mat) == sp.zeros(*mat.shape)


def has_all(text: str, pins: list[str]) -> bool:
    return all(pin in text for pin in pins)


def section_a_sources() -> tuple[str, str, str, str]:
    paths = [BRANNEN, RECORD, KOIDE, AXIOMS, NOTE, SELF]
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    brannen = read(BRANNEN)
    record = read(RECORD)
    koide = read(KOIDE)
    note = read(NOTE)

    check("Brannen pins: circulant form and couplings", has_all(brannen, [
        "has the circulant form",
        "real couplings, written as `(a, |b|, delta)`",
    ]))
    check("record-preservation pins: dephasing and finer record", has_all(record, [
        "dephasing onto `{P_singlet, P_doublet}`",
        "only a finer character-basis record would touch it.",
    ]))
    check("record-preservation pin: supplied sector dial", "The couplings (a, |b|, delta) are the supplied sector dial." in record)
    check("Koide modulus pin: degenerate stationary candidates", "its stationary candidates are degenerate" in koide)
    return brannen, record, koide, note


def algebra_setup():
    i = sp.I
    sqrt3 = sp.sqrt(3)
    omega = -sp.Rational(1, 2) + i * sqrt3 / 2
    a, rho_b, delta = sp.symbols("a rho_b delta", real=True)
    ell = sp.symbols("lambda_scale", real=True)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    b = rho_b * (sp.cos(delta) + i * sp.sin(delta))
    H = a * I3 + b * C + sp.conjugate(b) * C.T

    def chi(k: int) -> sp.Matrix:
        return sp.Matrix([omega ** (k * j) for j in range(3)]) / sp.sqrt(3)

    chis = [chi(k) for k in range(3)]
    P = [v * v.conjugate().T for v in chis]
    B = sp.Matrix.hstack(*chis)
    S = C + C ** 2
    lambdas = [exact((H * chis[k])[0] / chis[k][0]) for k in range(3)]
    return i, sqrt3, a, rho_b, delta, ell, C, I3, H, chis, P, B, S, lambdas


def section_b_labeled_refinement():
    i, sqrt3, a, rho_b, delta, _ell, C, _I3, H, chis, _P, B, S, lambdas = algebra_setup()
    check("omega character basis is unitary", is_zero_matrix(B.conjugate().T * B - sp.eye(3)))

    C_eigs = [1, (-sp.Rational(1, 2) - i * sqrt3 / 2), (-sp.Rational(1, 2) + i * sqrt3 / 2)]
    S_eigs = [2, -1, -1]
    for k in range(3):
        check(f"C chi_{k} eigenrelation", is_zero_matrix(C * chis[k] - C_eigs[k] * chis[k]))
        check(f"H chi_{k} eigenrelation", is_zero_matrix(H * chis[k] - lambdas[k] * chis[k]))
        check(f"S chi_{k} pointer eigenvalue", is_zero_matrix(S * chis[k] - S_eigs[k] * chis[k]))

    lam_s = lambdas[0]
    lam_d1 = lambdas[2]
    lam_d2 = lambdas[1]
    check("convention: singlet is chi_0", exact(lam_s - a - 2 * rho_b * sp.cos(delta)) == 0)
    check("convention: ordered doublet d1=chi_2, d2=chi_1", exact(lam_d2 - lam_d1 - 2 * sqrt3 * rho_b * sp.sin(delta)) == 0)
    check("W6-A singlet identity", exact(lam_s - a - 2 * rho_b * sp.cos(delta)) == 0)
    check("W6-A doublet sum identity", exact(lam_d1 + lam_d2 - 2 * a + 2 * rho_b * sp.cos(delta)) == 0)
    check("W6-A sign-free splitting identity", exact((lam_d2 - lam_d1) ** 2 - 12 * rho_b ** 2 * sp.sin(delta) ** 2) == 0)
    check("wrong coefficient rejector: sqrt(2) impostor fails", exact((lam_d2 - lam_d1) ** 2 - 8 * rho_b ** 2 * sp.sin(delta) ** 2) != 0)

    da = sp.Rational(2, 9)
    db = 2 * sp.pi / 3 - da
    check("injectivity pair has equal bare cos(3 delta)", exact(sp.cos(3 * da) - sp.cos(3 * db)) == 0)
    check("injectivity pair is ordered inside [0, pi]", bool(sp.ask(sp.Q.positive(db - da)) and sp.ask(sp.Q.positive(da)) and sp.ask(sp.Q.positive(sp.pi - db))))
    cos_gap = exact(sp.cos(da) - sp.cos(db))
    sin_gap = exact(sp.sin(db) - sp.sin(da))
    check("labeled cos delta data distinguish the pair", bool(sp.ask(sp.Q.positive(cos_gap))))
    check("labeled |sin delta| data distinguish the pair", bool(sp.ask(sp.Q.positive(sin_gap))))
    check("bare multiset discriminator is strict", exact(cos_gap) != 0 and exact(sin_gap) != 0)

    return lambdas


def section_c_record_map():
    _i, _sqrt3, a, rho_b, delta, _ell, C, _I3, H, chis, P, B, _S, _lambdas = algebra_setup()
    for k, Pk in enumerate(P):
        check(f"finer character projector P_{k} commutes with H", is_zero_matrix(Pk * H - H * Pk))

    site0 = sp.diag(1, 0, 0)
    site_comm = exact_matrix((site0 * H - H * site0).subs({a: 0, rho_b: 1, delta: sp.Rational(1, 7)}))
    check("discriminator: site-basis projector is demolition-generic", site_comm != sp.zeros(3))

    xs = sp.symbols("x00:03 x10:13 x20:23")
    R = sp.Matrix(3, 3, xs)
    P_s = P[0]
    P_d = P[1] + P[2]

    def D_chi(M):
        out = sp.zeros(3)
        for Pk in P:
            out += Pk * M * Pk
        return exact_matrix(out)

    def D_S(M):
        return exact_matrix(P_s * M * P_s + P_d * M * P_d)

    D = D_chi(R)
    check("D_chi trace preserving", exact(sp.trace(D) - sp.trace(R)) == 0)
    check("D_chi idempotent", is_zero_matrix(D_chi(D) - D))
    check("D_chi after D_S equals D_chi", is_zero_matrix(D_chi(D_S(R)) - D))
    check("D_S after D_chi equals D_chi", is_zero_matrix(D_S(D) - D))

    character_before = exact_matrix(B.conjugate().T * R * B)
    character_after = exact_matrix(B.conjugate().T * D * B)
    for row in range(3):
        for col in range(3):
            if row != col:
                check(f"D_chi erases character off-diagonal {row}{col}", exact(character_after[row, col]) == 0)
    for k in range(3):
        check(f"D_chi preserves character occupancy {k}", exact(character_after[k, k] - character_before[k, k]) == 0)
    check("partial-erasure rejector: chi_1-chi_2 entry is identically zero", exact(character_after[1, 2]) == 0 and "x" not in str(character_after[1, 2]))
    check("partial-erasure rejector: chi_2-chi_1 entry is identically zero", exact(character_after[2, 1]) == 0 and "x" not in str(character_after[2, 1]))


def section_d_doublet_clock():
    i, sqrt3, _a, rho_b, delta, ell, _C, _I3, _H, _chis, P, B, _S, lambdas = algebra_setup()
    U = sp.zeros(3)
    for k, Pk in enumerate(P):
        U += sp.exp(-i * lambdas[k]) * Pk
    D = exact_matrix(B.conjugate().T * U * B)
    target_diag = sp.diag(*[sp.exp(-i * lam) for lam in lambdas])
    check("U is built by exact spectral decomposition", is_zero_matrix(D - target_diag))

    ys = sp.symbols("y00:03 y10:13 y20:23")
    M = sp.Matrix(3, 3, ys)
    evolved = exact_matrix(D * M * D.conjugate().T)
    lam_d1 = lambdas[2]
    lam_d2 = lambdas[1]
    ratio = exact(evolved[2, 1] / M[2, 1])
    rate = exact(lam_d2 - lam_d1)
    check("doublet coherence ratio is exp(i(lambda_d2-lambda_d1))", exact(ratio - sp.exp(i * (lam_d2 - lam_d1))) == 0)
    check("per-step phase rate is 2 sqrt(3) rho_b sin(delta)", exact(rate - 2 * sqrt3 * rho_b * sp.sin(delta)) == 0)
    check("registrable magnitude square is 12 rho_b^2 sin^2(delta)", exact(rate ** 2 - 12 * rho_b ** 2 * sp.sin(delta) ** 2) == 0)
    check("zero-clock at delta=0", exact(rate.subs(delta, 0)) == 0)
    check("zero-clock at delta=pi", exact(rate.subs(delta, sp.pi)) == 0)
    check("cos(3 delta)=+1 at delta=0", exact(sp.cos(3 * 0) - 1) == 0)
    check("cos(3 delta)=-1 at delta=pi", exact(sp.cos(3 * sp.pi) + 1) == 0)
    check("clock runs at delta=2/9 by exact positivity", bool(sp.ask(sp.Q.positive(sp.sin(sp.Rational(2, 9))))))
    dimensionless = exact(rate / rho_b)
    check("dimensionless rate removes the |b| unit", rho_b not in dimensionless.free_symbols)
    check("dimensionless rate at 2/9 is well-defined and nonzero", bool(sp.ask(sp.Q.positive(dimensionless.subs(delta, sp.Rational(2, 9))))))
    rescaled = rate.subs(rho_b, ell * rho_b)
    check("PR #4783 rescale obstruction persists on the clock normalization", exact(rescaled - ell * rate) == 0)
    check(
        "singlet-doublet rate to d1 is 2 sqrt(3) rho sin(delta + pi/3)",
        exact(lambdas[0] - lambdas[2] - 2 * sqrt3 * rho_b * sp.sin(delta + sp.pi / 3)) == 0,
    )
    check(
        "singlet-doublet rate to d2 is 2 sqrt(3) rho sin(pi/3 - delta)",
        exact(lambdas[0] - lambdas[1] - 2 * sqrt3 * rho_b * sp.sin(sp.pi / 3 - delta)) == 0,
    )


def section_e_note_discipline(note: str) -> None:
    required = [
        "the pointer-labeled registrable content is `|delta|`: the distinguished singlet removes the `2 pi/3`-relabel quotient of the bare multiset",
        "the within-doublet phase advances by exactly `2 sqrt(3) |b| sin delta` per native step",
        "the K-real locus is exactly the zero-clock set",
        "not a terminal no-go",
    ]
    for phrase in required:
        check(f"note contains required phrase: {phrase[:42]}", phrase in note)
    for n in range(1, 9):
        check(f"note contains N{n} gate header", f"### N{n}" in note)

    forbidden = [
        "only " + "route",
        "last " + "route",
        "exhau" + "sted",
        "closes " + "the route",
        "P" + "DG",
        "new " + "wall",
        "r=1/2 is " + "forced",
        "occurrence " + "probability",
    ]
    lowered = note.lower()
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase.lower() not in lowered)

    allowed_walls = {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}
    seen_walls = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    check("W_ labels are whitelisted", seen_walls <= allowed_walls, detail=", ".join(sorted(seen_walls)))

    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    doc_links = [Path(target).name for target in links if Path(target).suffix == ".md"]
    expected_docs = sorted([BRANNEN.name, RECORD.name, KOIDE.name])
    check("markdown dependency links are exactly the three retained origins", sorted(doc_links) == expected_docs and len(doc_links) == 3)
    check("primary runner is markdown-linked", any(Path(target).name == SELF.name for target in links))

    inflight = [
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01",
        "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01",
        "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01",
        "ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01",
        "ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02",
    ]
    for name in inflight:
        check(f"in-flight name appears as backticked context: {name[:34]}", f"`{name}`" in note)
        check(f"in-flight name is not a link target: {name[:34]}", all(name not in target for target in links))

    check("status-authority standard present", "**Status authority:** independent audit lane only." in note)
    grade_tokens = ["retained_" + "bounded", "retained_" + "no_go", "audited_" + "clean"]
    check("no retained audit-grade tokens", all(token not in note for token in grade_tokens))
    check("standard non-retirement text present", "does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement" in note)
    check("runner command names this script", f"python3 scripts/{SELF.name}" in note)
    check("verification section has measured total", re.search(r"TOTAL: PASS=\d+ FAIL=0", note) is not None)

    leakage = [
        "Acceptance " + "contract",
        "PRESERVE " + "VERBATIM",
        "MUST " + "BE ABSENT",
        "Files " + "to produce",
        "ANTI-" + "FABRICATION",
        "derived and verified by the " + "reviewer",
        "execute " + "it exactly",
        "Spec " + "CLOCK",
    ]
    for phrase in leakage:
        check(f"source-instruction phrase absent: {phrase}", phrase not in note)


def main() -> int:
    _brannen, _record, _koide, note = section_a_sources()
    section_b_labeled_refinement()
    section_c_record_map()
    section_d_doublet_clock()
    section_e_note_discipline(note)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
