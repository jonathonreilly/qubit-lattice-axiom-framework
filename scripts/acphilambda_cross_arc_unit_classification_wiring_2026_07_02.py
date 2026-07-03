#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
import subprocess
from fractions import Fraction
from pathlib import Path

PASS = 0; FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_CROSS_ARC_UNIT_CLASSIFICATION_WIRING_2026-07-02.md"
SELF = ROOT / "scripts" / "acphilambda_cross_arc_unit_classification_wiring_2026_07_02.py"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

KOIDE = DOCS / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
BRANNEN = DOCS / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
RETA_ALG = DOCS / "RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md"
RETA_MAG = DOCS / "RETA_MAGNITUDE_IS_CONTINUUM_INDEX_THEOREM_LATTICE_INDEX_IS_INTEGER_BOUNDED_NOTE_2026-06-12.md"
RECORD = DOCS / "RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md"

EXPECTED_LINKS = {
    "../scripts/acphilambda_cross_arc_unit_classification_wiring_2026_07_02.py",
    "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
    "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
    "RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md",
}


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_landed_doc(filename: str) -> str:
    path = DOCS / filename
    if path.exists():
        return read(path)
    return subprocess.check_output(
        ["git", "show", f"origin/main:docs/{filename}"], cwd=ROOT, text=True
    )


def norm(text: str) -> str:
    text = text.replace("\\|", "|")
    return re.sub(r"\s+", " ", text).strip()


def ledger_row(rows: dict, note_path: str) -> dict:
    matches = [row for row in rows.values() if row.get("note_path") == note_path]
    if len(matches) != 1:
        raise AssertionError(f"ledger path match count for {note_path}: {len(matches)}")
    return matches[0]


def links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def table_rows(text: str) -> list[str]:
    block = text.split("## The Wiring Table", 1)[1].split("## Convergent Verdicts", 1)[0]
    rows = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        if line.startswith("|---") or "Arc B path-2 item" in line:
            continue
        rows.append(line)
    return rows


def source_texts() -> dict[str, str]:
    return {
        "pr4783": read_landed_doc("ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"),
        "pr4788": read_landed_doc("ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"),
        "pr4794": read_landed_doc("ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md"),
        "pr4831": read_landed_doc("ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md"),
        "pr4835": read_landed_doc("ACPHILAMBDA_K1_STAGGERED_K_BLINDNESS_REAL_LIFT_2026-07-02.md"),
        "pr4837": read_landed_doc("ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md"),
        "pr4840": read_landed_doc("ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md"),
        "koide": read(KOIDE),
        "brannen": read(BRANNEN),
        "record": read(RECORD),
    }


PINS = [
    ("determinant class", "pr4788", "arg det(b C) = 3 delta."),
    ("homogeneous clauses", "pr4783", "Homogeneous record/covariance/consistency clauses can therefore at most force `I = 0`; they can never single out a specific nonzero unit"),
    ("count normalization", "pr4783", "c = u / L = 1 / (2/9) = 9/2  !=  1"),
    ("angular rigidity", "pr4783", "registered unordered spectrum `{x_k}` is preserved for all offsets `delta` iff `c = +1` or `c = -1`"),
    ("vacuous convention", "pr4783", "while `delta -> c*delta` moves registered ratios"),
    ("Born normalization", "pr4783", "Projective normalization `sum p = 1` is satisfiable for every `c`"),
    ("cross-lane transport", "pr4783", "transport propagates one global `c` but cannot pin its value"),
    ("ratio bypass", "pr4783", "does not port to an additive angular offset"),
    ("flux constant term", "pr4794", "flux enters the fluxed-ring characteristic polynomial only through the constant term"),
    ("canonical spectral members", "pr4794", "canonical members checked here are monotone on `(0, pi)` and have no interior stationary point"),
    ("scalar K-blindness", "pr4831", "the scalar ambient equivariant surface is K-blind: conjugate-sector traces coincide for every real function of the scalar Laplacian"),
    ("staggered K-blindness", "pr4835", "The one-component staggered surface, in both retained kinetic classes and with the full `U(1)` frame freedom allowed by the retained scope, cannot source the K-breaking registered content that off-locus selection requires."),
    ("torsion phases", "pr4837", "Torsion/root-of-unity phases are `q*pi` Type-A objects."),
    ("radian qpi", "koide", "every such phase is of the form `q*pi` with `q in Q`"),
    ("doubler cancellation", "pr4837", "On even diagonal grids, `kappa -> kappa + pi` is a bijection, the sine flips sign, and the two branches swap. The imaginary parts cancel pairwise for all flux."),
    ("retained row from PR", "pr4840", "The retained row conserves `(r, delta)` under record-preserving dynamics"),
    ("retained row file", "record", "the within-sector measure `(r, delta)` is neither produced nor relaxed by the record-preserving dynamics."),
    ("K-odd target kill", "pr4840", "at `Phi = 2/3`, `sin(2/3) != 0` and `cos(2/3) != 0`."),
    ("tuned b tell", "pr4840", "requires tuned `|b| = (2/9)/(2 sqrt(3) sin(2/9))`."),
    ("pi-free strobe", "pr4840", "It gives `2 pi Q` values, while `2/9` is rational and pi-free."),
]


PRESERVE = [
    "arc B's path 2 is answered at the classification level by the landed unit-classification arc, with all audit statuses pending",
    "the shared remaining frontier is a single target: a registrable `C3`-covariant holonomy or eta-invariant whose registered datum is provably the fixed-locus density",
    "this note wires the two arcs together; it derives nothing new and edits nothing",
    "not a terminal no-go",
]


def qomega_mul(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    a, b = left
    c, d = right
    # (a+b*w)(c+d*w), with w^2 = -w - 1.
    return (a * c - b * d, a * d + b * c - b * d)


def main() -> int:
    print("=" * 88)
    print("ACPHILAMBDA CROSS-ARC UNIT-CLASSIFICATION WIRING CHECK")
    print("=" * 88)

    note = read(NOTE)
    note_n = norm(note)
    rows = json.loads(read(LEDGER))["rows"]
    sources = source_texts()

    section("A: dependency files, ledger authority, and Arc B pins")
    for path in [NOTE, SELF, KOIDE, BRANNEN, RETA_ALG, RETA_MAG, RECORD, LEDGER]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    krow = ledger_row(rows, "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md")
    brow = ledger_row(rows, "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md")
    rrow = ledger_row(rows, "docs/RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md")
    check("KOIDE ledger status retained_no_go", krow.get("effective_status") == "retained_no_go")
    check("BRANNEN ledger status retained_bounded", brow.get("effective_status") == "retained_bounded")
    check("conservation ledger status retained_bounded", rrow.get("effective_status") == "retained_bounded")
    for label, row in [("KOIDE", krow), ("BRANNEN", brow), ("conservation", rrow)]:
        scope = row["claim_scope"]
        check(f"{label} ledger scope quoted exactly", scope in note)
    check("KOIDE source pins present", "a Type-B rational-to-radian observable law is still missing" in sources["koide"] and "same Type-B-to-radian map as the remaining primitive" in sources["koide"])
    check("BRANNEN source pins present", "circulant form" in sources["brannen"] and "(a, |b|, delta)" in sources["brannen"])

    alg = read(RETA_ALG)
    mag = read(RETA_MAG)
    path2 = "Classify registrable conversion-factor sources beyond the determinant class to fix the unit."
    genuine = "is a genuine readout admission"
    check("true I7 path-2 sentence in Arc B algebra note", norm(path2) in norm(alg))
    check("true I7 path-2 sentence quoted in wiring note", path2 in note)
    check("genuine admission phrasing in Arc B algebra note", genuine in alg)
    check("genuine admission phrasing quoted in wiring note", "genuine readout admission" in note)
    for phrase in ["lattice operator index is integer", "not `2/9`", "geometric rotation number", "continuum Atiyah-Bott"]:
        check(f"magnitude face pin: {phrase}", norm(phrase) in norm(mag))
    for basename in [
        "`RETA_MAGNITUDE_CONTINUUM_INDEX_THEOREM_2026_06_12`",
        "`RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12`",
    ]:
        check(f"Arc B basename backticked: {basename}", basename in note)

    section("B: wiring table and source-pin integrity")
    wiring = table_rows(note)
    check("wiring table has 15 rows", len(wiring) == 15, detail=f"rows={len(wiring)}")
    check("each table row carries Source pin text", sum("Source pin" in row or "Source pins" in row for row in wiring) == 15)
    for pr in ["4783", "4788", "4794", "4831", "4835", "4837", "4840"]:
        check(f"Where cell includes backticked PR #{pr}", f"`PR #{pr}`" in note)
    for label, source_key, quote in PINS:
        check(f"source contains pin: {label}", norm(quote) in norm(sources[source_key]))
        check(f"note contains pin: {label}", norm(quote) in note_n)

    section("C: convergence arithmetic spot checks")
    check("9/2 = 1/(2/9)", Fraction(9, 2) == Fraction(1, 1) / Fraction(2, 9))
    check("sin(2/3) and cos(2/3) are both nonzero", abs(math.sin(2 / 3)) > 1e-12 and abs(math.cos(2 / 3)) > 1e-12)
    omega_minus_1 = (Fraction(-1), Fraction(1))
    omega2_minus_1 = (Fraction(-2), Fraction(-1))
    product = qomega_mul(omega_minus_1, omega2_minus_1)
    check("(omega-1)(omega^2-1) = 3 in Q[omega]", product == (Fraction(3), Fraction(0)), detail=str(product))
    check("L3 = 2/9 = (1/3)(2/3)", Fraction(2, 9) == Fraction(1, 3) * Fraction(2, 3))

    section("D: note discipline")
    check("Type metadata is bounded_theorem", "**Type:** bounded_theorem" in note)
    check("Claim type metadata is canonical bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("scope boundary blocks value and registry claims", "Cross-arc unit-classification wiring only" in note and "no derivation of `delta = 2/9`, `Phi = 2/3`, R-eta, a value equation" in note and "registry/publication edit" in note)
    check("audit boundary is independent-lane only", "**Audit boundary:** independent audit lane only" in note)
    check("legacy status-authority metadata absent", "**Status authority:**" not in note)
    for sentence in PRESERVE:
        check(f"preserve sentence embedded: {sentence[:42]}", sentence in note)
    for i in range(1, 9):
        check(f"N{i} present", f"**N{i}" in note)
    forbidden = ["only route", "last route", "exhausted", "closes the route", "PDG", "new wall"]
    for token in forbidden:
        check(f"forbidden phrase absent: {token}", token.lower() not in note.lower())
    wall_names = set(re.findall(r"\bW_[A-Za-z0-9_]+", note))
    check("W_ names are whitelisted", wall_names <= {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}, detail=str(sorted(wall_names)))
    got_links = set(links(note))
    check("markdown link inventory exactly three deps plus runner", got_links == EXPECTED_LINKS, detail=str(sorted(got_links)))
    check("no linked in-flight or Arc B note target", all("ACPHILAMBDA_" not in link and "RETA_" not in link for link in got_links if link.endswith(".md")))
    check("audit-grade authorship absent", not re.search(r"audited_(clean|conditional|failed)|grade prediction|audit grade", note, re.I))
    leaks = ["PRESERVE VERBATIM", "MUST BE ABSENT", "Acceptance contract", "Content to encode", "RULES (binding)", "/tmp/spec-crossarc"]
    check("instruction-language leakage absent from note", not any(item in note for item in leaks))
    check("no unaudited item linked statement present", "No unaudited/in-flight item is linked; audit statuses pending on all of them." in note)
    check("three retained dependency scopes statement present", "The three retained dependency scopes remain exactly the ledger scopes quoted above." in note)
    check("Audit Consequence names classification-answered pending audit", "classification-answered pending audit" in note)
    check("note line count in requested band", 150 <= len(note.splitlines()) <= 190, detail=f"lines={len(note.splitlines())}")
    check("runner line count in requested band", 180 <= len(read(SELF).splitlines()) <= 240, detail=f"lines={len(read(SELF).splitlines())}")
    displayed = re.search(r"Measured local close: `TOTAL: PASS=(\d+) FAIL=0`", note)
    check("verification line has measured close", displayed is not None)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 45 else 1


if __name__ == "__main__":
    raise SystemExit(main())
