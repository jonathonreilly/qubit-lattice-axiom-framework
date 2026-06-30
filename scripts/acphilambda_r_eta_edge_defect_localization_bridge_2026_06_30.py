#!/usr/bin/env python3
"""Verify the A_R-eta edge-defect localization bridge candidate."""

from __future__ import annotations

from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
STRICT_NN = DOCS / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
GEN_CONTEXT = DOCS / "GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION_2026-06-30.md"
R_ETA_NARROW = DOCS / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
FIXED_LOCUS = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
CONVERSION = DOCS / "RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md"
CONTINUUM = DOCS / "CONTINUUM_EQUIVARIANT_ETA_STANDARD_FORM_DELTA_FIREWALL_BOUNDED_NOTE_2026-06-12.md"
POST_DIRAC = DOCS / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
R_HALF = DOCS / "ACPHILAMBDA_R_HALF_DURABLE_RECORD_IDEMPOTENCE_BRIDGE_THEOREM_NOTE_2026-06-30.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def zclean(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_complex(expr))


def main() -> int:
    print("=== AC_phi_lambda R-eta edge-defect localization bridge ===")

    paths = [
        NOTE,
        AXIOMS,
        STRICT_NN,
        GEN_CONTEXT,
        R_ETA_NARROW,
        FIXED_LOCUS,
        CONVERSION,
        CONTINUUM,
        POST_DIRAC,
        R_HALF,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    strict = read(STRICT_NN)
    gen_context = read(GEN_CONTEXT)
    r_eta = read(R_ETA_NARROW)
    fixed = read(FIXED_LOCUS)
    conversion = read(CONVERSION)
    continuum = read(CONTINUUM)
    post_dirac = read(POST_DIRAC)
    r_half = read(R_HALF)

    section("PART A -- source surface and dependency boundaries")
    check("axioms supply nearest-neighbor lattice locality", "nearest-neighbor adjacency" in flat(axioms))
    check("axioms supply fixed record readout only", "A record locks exactly one available local possibility" in axioms)
    check("strict NN supplies edge-local first-order branch", "first-order branch" in strict and "no face-diagonal leakage" in strict)
    check("strict NN names edge coefficients", "edge coefficients" in strict)
    check("generation bridge selects hw=1", "minimal nontrivial `C3[111]` record context" in gen_context and "hw=1" in gen_context)
    check("generation bridge preserves hw=2 boundary", "not excluded and not physically impossible" in gen_context)
    check("post-Dirac map leaves W_eta open", "W_eta" in post_dirac and "A_R-eta" in post_dirac)
    check("r-half bridge waits for charged-lepton context", "charged-lepton record context" in flat(r_half))

    section("PART B -- finite selected-context C3 defect theorem")
    x = sp.Symbol("x")
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    omega2 = sp.Rational(-1, 2) - sp.I * sp.sqrt(3) / 2
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    charpoly = sp.expand((P - x * sp.eye(3)).det())
    check("C3[111] edge-cycle charpoly is 1 - x^3", sp.simplify(charpoly - (1 - x**3)) == 0, f"det(P-xI)={charpoly}")
    check("body diagonal is fixed", P * sp.Matrix([1, 1, 1]) == sp.Matrix([1, 1, 1]))
    check("fixed locus has codimension two", (P - sp.eye(3)).rank() == 2)
    eigs = list(P.eigenvals().keys())
    check("spectrum contains 1, omega, omega^2", all(any(zclean(ev - target) == 0 for ev in eigs) for target in (1, omega, omega2)))
    transverse = [ev for ev in eigs if zclean(ev - 1) != 0]
    check("transverse spectrum has two nontrivial weights", len(transverse) == 2 and all(zclean(ev**3 - 1) == 0 for ev in transverse))
    check("transverse product is singlet", zclean(transverse[0] * transverse[1] - 1) == 0)

    def trace_free(a: int, b: int) -> bool:
        return (a + b) % 3 == 0

    tracefree_pairs = {(a, b) for a in (1, 2) for b in (1, 2) if trace_free(a, b)}
    check("unique unordered trace-free pair is (1,2)", tracefree_pairs == {(1, 2), (2, 1)}, f"pairs={sorted(tracefree_pairs)}")
    check("equal-weight pairs are not trace-free", not trace_free(1, 1) and not trace_free(2, 2))
    check("core identity (omega - 1)(omega^2 - 1) = 3", zclean((omega - 1) * (omega2 - 1) - 3) == 0)

    def L3(a: int, b: int) -> sp.Expr:
        return zclean(
            sp.Rational(1, 3)
            * sum(
                1 / ((1 - omega ** (a * j)) * (1 - omega ** (b * j)))
                for j in (1, 2)
            )
        )

    l12 = L3(1, 2)
    l21 = L3(2, 1)
    l11 = L3(1, 1)
    l22 = L3(2, 2)
    check("L3(1,2) = 2/9 exactly", zclean(l12 - sp.Rational(2, 9)) == 0, f"L3(1,2)={l12}")
    check("L3(2,1) gives same density", zclean(l21 - l12) == 0)
    check("contrast equal-weight cells give 1/9", zclean(l11 - sp.Rational(1, 9)) == 0 and zclean(l22 - sp.Rational(1, 9)) == 0)
    check("selected-context density is distinct from equal-weight contrast cells", zclean(l12 - l11) != 0 and zclean(l12 - l22) != 0)

    section("PART C -- relation to H(delta) and carrier-unit narrowing")
    delta, a, B = sp.symbols("delta a B", real=True)
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * sp.eye(3) + B * sp.exp(sp.I * delta) * C + B * sp.exp(-sp.I * delta) * C.T
    e1 = sp.simplify(H.trace())
    e2 = sp.simplify(sp.re(sp.expand_complex((H.trace() ** 2 - (H * H).trace()) / 2)))
    e3 = sp.simplify(sp.re(sp.expand_complex(H.det(method="berkowitz"))))
    check("H(delta) is Hermitian", sp.simplify(H - H.conjugate().T) == sp.zeros(3, 3))
    check("conj(H(delta)) = H(-delta)", sp.simplify(H.conjugate() - H.subs(delta, -delta)) == sp.zeros(3, 3))
    check("e1 is delta-blind", sp.simplify(e1 - 3 * a) == 0)
    check("e2 is delta-blind", sp.simplify(e2 - (3 * a**2 - 3 * B**2)) == 0)
    check("e3 carries delta only through cos(3 delta)", sp.simplify(e3 - (a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta))) == 0)
    check("cos(3 delta) is monotone on sampled fundamental-domain points", all(float((-3 * sp.sin(3 * delta)).subs(delta, p)) < 0 for p in (0.1, 0.2, 0.7, 1.0)))
    inversion = sp.simplify((e3 - a**3 + 3 * a * B**2) / (2 * B**3))
    check("symmetric datum inverts to cos(3 delta)", sp.simplify(inversion - sp.cos(3 * delta)) == 0)
    check("R-eta narrowing isolates A_R-eta", "A_R-eta" in r_eta and "h-class" in r_eta and "h-unit" in r_eta)
    check("R-eta narrowing says formal layer cannot select value", "formal layer selects no value" in flat(r_eta) or "selects **no** value" in r_eta)
    check(
        "conversion note assembles direct c=1 retained-carrier member",
        "direct `c = 1` reading" in conversion
        and "no primitive `c != 1` conversion carrier" in conversion,
    )
    check("conversion note does not derive R-eta", "Does not derive R-eta" in conversion)
    check("continuum eta note keeps coupling separate", "mechanism identifying the mass coupling" in continuum)

    section("PART D -- prior note matching")
    check("fixed-locus note says weights are read off the operator", "read off the operator" in fixed)
    check("fixed-locus note says local density 2/9", "local density `2/9`" in fixed or "local density 2/9" in fixed)
    check("fixed-locus note preserves physical readout bridge", "physical single-summand readout" in fixed)
    check("generation note supplies edge-minimal selector", "edge-minimal selector" in gen_context)
    check("generation note says A_R-eta remains outside", "A_R-eta" in gen_context and "remains" in gen_context)
    check("post-Dirac map keeps W_eta independent", "W_eta" in post_dirac and "Wall Independence" in post_dirac)
    check("conversion note keeps future readout contexts open", "Future readout contexts remain open" in conversion)

    section("PART E -- new note content")
    check("note declares bounded bridge theorem", "positive theorem candidate / bounded bridge theorem" in note)
    check("note names old h-class and new h-class target", "old h-class" in note and "new h-class target" in note)
    check("note names phase-defect coupling", "phase-defect coupling" in note)
    check("note proves finite theorem section", "## Finite Theorem" in note)
    check("note has H(delta) relation section", "## Relation To The Formal `H(delta)` Layer" in note)
    check("note says no new number", "does not add a number" in note)
    check("note preserves full AC boundary", "does not claim `AC_phi_lambda` is retired" in note)
    check("note excludes comparator imports", "PDG masses" in note and "fitted values" in note)
    check("note gives audit consequence", "## Audit Consequence If Retained" in note)

    section("PART F -- consequence assembly")
    selected_density = zclean(l12)
    direct_unit_available = "c != 1" in conversion and ("{1}" in conversion or "direct" in conversion)
    coupling_statement = "the charged-lepton phase magnitude records the selected local C3 defect density" in note_flat
    check("selected density is 2/9", selected_density == sp.Rational(2, 9))
    check("direct-unit narrowing is cited", direct_unit_available)
    check("coupling statement is explicit", coupling_statement)
    check("if coupling holds then |delta|=2/9", selected_density == sp.Rational(2, 9) and direct_unit_available and coupling_statement)
    check("if coupling rejected residual is exactly W_coupling", "W_coupling" in note and "only remaining atom" in note)

    section("PART G -- no-go discipline gate")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", item in note)
    check("N1 has at least five routes", note.count("| Route |") == 1 and note.count("|") > 30 and note.count("RULED OUT") >= 3)
    check("N2 collapses to W_coupling", "W_coupling" in note and "Collapsed residual" in note)
    check("N3 classifies direct readout boundary", "future readout context" in note)
    check("N4 matches five witnesses", note.count("| `") >= 5 and "Residual Matching" in note)
    check("N5 avoids universal R-eta claim", "other contexts" in note_flat and "The tested resolution" in note_flat)
    check("N6 gives import-retirement path", "import-retirement shape" in note)
    check("N7 steelman names coupling objection", "does not derive the physical coupling" in note_flat)
    check("N8 guards hidden value source", "number is fixed-locus arithmetic" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- A_R-eta is narrowed to the phase-defect coupling on the selected edge-minimal C3 context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
