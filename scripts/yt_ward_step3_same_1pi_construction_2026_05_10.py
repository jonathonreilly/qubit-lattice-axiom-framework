#!/usr/bin/env python3
"""Bounded theorem checker for the YT_WARD Step 3 same-1PI construction.

The runner keeps load-bearing symbolic algebra separate from motivation-tier
note-text checks. It intentionally does not derive that the OGE and H_unit
representations are the same Green's function; SAME-1PI is checked only as a
named supplied premise.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import math
import re
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTE_PATH = (
    DOCS
    / "YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md"
)
WARD_IDENTITY_PATH = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"
EW_COLOR_PATH = DOCS / "YT_EW_COLOR_PROJECTION_THEOREM.md"

CLAIM_ID = "yt_ward_step3_same_1pi_construction_narrow_theorem_note_2026-05-10"
RUNNER_PATH = "scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py"

SAME_1PI_PREMISE = """SAME-1PI (named conditional premise): the OGE contraction and the H_unit
decomposition are SUPPLIED as two complete representations of the same
projected amputated 1PI Green's function on the scalar-singlet four-fermion
channel. Not derived: no Wick-level proof exists; equating the two projected
coefficients without that proof would assume the equality under review. The
open positive target is the Wick-level bridge."""

CONDITIONAL_CONSEQUENCES = """C_A = C_B.
c_S * g_bare^2 = 2 / N_iso.
At the Q_L = (2,3), c_S = +1 surface, g_bare^2 = 1."""

CANONICAL_SIGN_BLOCK = "N_c = 3, N_iso = 2, c_S = +1."
MOTIVATION_LABEL = "Evidence only; not load-bearing; no value below is consumed by any claim."

SOURCE_BOUNDARY_REQUIRED_PHRASES = [
    "Downstream source-boundary firewall",
    "Allowed downstream uses",
    "Forbidden downstream uses",
    "bounded coefficient-bookkeeping theorem",
    "SAME-1PI named as a supplied premise",
    "`c_S * g_bare^2 = 2 / N_iso` only under SAME-1PI",
    "`g_bare^2 = 1` only under SAME-1PI",
    "missing same-1PI bridge remains open",
    "closed same-1PI theorem",
    "gate equation as a closed theorem",
    "derivation of `g_bare = 1`",
    "top-Yukawa derivation",
    "Wick-level proof",
    "do not cite SAME-1PI as established",
    "the named premises may not be cited as derived",
]

DECLARED_AUTHORITIES = [
    "UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md",
    "G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md",
    "YT_WARD_IDENTITY_DERIVATION_THEOREM.md",
    "NATIVE_GAUGE_CLOSURE_NOTE.md",
]

DECLARATION = (
    "DECLARATION: SAME-1PI is supplied, not derived; no g_bare = 1 "
    "derivation, top-Yukawa derivation, or closed same-1PI theorem is claimed."
)

COUNTS = {
    "load-bearing": {"pass": 0, "fail": 0},
    "motivation-tier": {"pass": 0, "fail": 0},
}


def check(label: str, ok: bool, detail: str = "", tier: str = "load-bearing") -> None:
    if tier not in COUNTS:
        raise ValueError(f"unknown check tier: {tier}")
    tag = "PASS" if bool(ok) else "FAIL"
    key = "pass" if bool(ok) else "fail"
    COUNTS[tier][key] += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{tag}] [{tier}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


TEXT_BLOCK_RE = re.compile(r"```text\n(.*?)\n```", re.DOTALL)


def fenced_block_after(text: str, marker: str) -> str | None:
    start = text.find(marker)
    if start < 0:
        return None
    match = TEXT_BLOCK_RE.search(text, start)
    if not match:
        return None
    return match.group(1).strip()


def parse_sympy_expr(raw: str, symbols: dict[str, object]) -> sp.Expr:
    cleaned = raw.strip().rstrip(".,")
    cleaned = cleaned.replace("^", "**")
    return sp.sympify(cleaned, locals=symbols)


def last_rhs_expr(block: str, symbols: dict[str, object]) -> sp.Expr:
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    for line in reversed(lines):
        if "=" in line:
            return parse_sympy_expr(line.rsplit("=", 1)[1], symbols)
    raise ValueError(f"no equality found in block: {block!r}")


def active_text_before_history(text: str) -> str:
    marker = "\n## Audit history"
    idx = text.find(marker)
    return text if idx < 0 else text[:idx]


section("Part 1: load-bearing note contract")
note_text = NOTE_PATH.read_text(encoding="utf-8")
ward_identity_text = WARD_IDENTITY_PATH.read_text(encoding="utf-8")
ew_color_text = EW_COLOR_PATH.read_text(encoding="utf-8")
compact_note_text = " ".join(note_text.split())

for required in [
    f"claim_id: {CLAIM_ID}",
    "claim_type_author_hint: bounded_theorem",
    f"runner_path: {RUNNER_PATH}",
    "**Type:** bounded_theorem",
    "**Claim type:** bounded_theorem",
    "**Claim scope:** conditional bounded theorem",
    "WITHOUT SAME-1PI supplied",
    "same-1PI bridge remains",
    "Does **not** derive `g_bare = 1`",
    "not load-bearing dependencies",
]:
    check(f"note contains required scope text: {required}", required in note_text)

check("note contains SAME-1PI supplied-premise block", SAME_1PI_PREMISE in note_text)
check("note contains canonical supplied sign block", CANONICAL_SIGN_BLOCK in note_text)
check(
    "note says c_S sign is supplied, not sourced",
    "supplies only `|c_S| = 1`" in note_text
    and "does not derive the sign choice `c_S = +1`" in compact_note_text,
)
check("note contains exact conditional consequences", CONDITIONAL_CONSEQUENCES in note_text)
check(
    "claim scope states conditional structure",
    "under SAME-1PI as a named" in note_text
    and "without that premise" in note_text
    and "no-equality branch" in note_text,
)
for required in SOURCE_BOUNDARY_REQUIRED_PHRASES:
    check(f"note contains source-boundary text: {required}", required in note_text)
for authority in DECLARED_AUTHORITIES:
    check(f"declared dependency is cited: {authority}", authority in note_text)

active_note_text = active_text_before_history(note_text).lower()
for forbidden in [
    "DERIVED tree-level identity",
    "holds. The agreement is enforced",
    "target_claim_type: " + "positive_" + "theorem",
    "audited" + "_clean",
]:
    check(f"note avoids overclaim/status text: {forbidden}", forbidden not in note_text)
check("active note text avoids retained-status vocabulary", "retained" not in active_note_text)
check(
    "source-boundary forbids using the gate as same-1PI/top-Yukawa closure",
    "do not cite this diagnostic as a closed same-1PI theorem" in note_text
    and "do not cite this diagnostic as a derivation of `g_bare = 1`" in note_text
    and "do not cite this diagnostic as a top-Yukawa derivation" in note_text,
)
check(
    "source-boundary forbids citing SAME-1PI as derived",
    "the named premises may not be cited as derived" in note_text,
)
check(
    "note has no Markdown blockquote source quotations",
    not any(line.lstrip().startswith(">") for line in note_text.splitlines()),
)


section("Part 2: load-bearing source-support coherence")
d12_ward_link = "(YT_WARD_IDENTITY_DERIVATION_THEOREM.md)" in note_text
d12_attributed_to_ew = re.search(
    r"YT_EW_COLOR_PROJECTION_THEOREM\.md[\s\S]{0,160}D12"
    r"|D12[\s\S]{0,160}YT_EW_COLOR_PROJECTION_THEOREM\.md",
    note_text,
)
check("D12 authority is the Ward-identity derivation", d12_ward_link)
check("D12 is not attributed to the EW color-projection note", d12_attributed_to_ew is None)
check(
    "Ward-identity source contains the D12 singlet coefficient",
    "-1/(2 N_c)" in ward_identity_text,
)
check(
    "EW color-projection source does not carry the D12 singlet coefficient",
    "-1/(2 N_c)" not in ew_color_text,
)
check(
    "declared dependencies are linked for citation-graph extraction",
    all(f"({authority})" in note_text for authority in DECLARED_AUTHORITIES),
)


section("Part 3: load-bearing exact symbolic coefficient algebra")
g_bare = sp.symbols("g_bare", positive=True, real=True)
N_c = sp.symbols("N_c", positive=True, integer=True)
N_iso = sp.symbols("N_iso", positive=True, integer=True)
c_S = sp.symbols("c_S", positive=True, real=True)
SYMPY_LOCALS = {
    "g_bare": g_bare,
    "N_c": N_c,
    "N_iso": N_iso,
    "c_S": c_S,
    "sqrt": sp.sqrt,
}

C_A = c_S * g_bare**2 / (2 * N_c)
F_Htt0 = 1 / sp.sqrt(N_c * N_iso)
C_B = F_Htt0**2
residual = sp.factor(C_A - C_B)
expected_residual = (N_iso * c_S * g_bare**2 - 2) / (2 * N_c * N_iso)

check(
    "Rep A coefficient is c_S * g_bare^2 / (2 N_c)",
    sp.simplify(C_A - c_S * g_bare**2 / (2 * N_c)) == 0,
    detail=f"C_A={C_A}",
)
check(
    "Rep B coefficient is 1 / (N_c N_iso)",
    sp.simplify(C_B - 1 / (N_c * N_iso)) == 0,
    detail=f"C_B={sp.simplify(C_B)}",
)
check(
    "C_A - C_B residual has the expected gate factor",
    sp.simplify(residual - expected_residual) == 0,
    detail=f"residual={residual}",
)
check(
    "C_A and C_B are not identical as symbolic functions of g_bare",
    sp.simplify(residual) != 0 and g_bare in residual.free_symbols,
    detail=f"free_symbols={sorted(str(s) for s in residual.free_symbols)}",
)

gate_solution = sp.solve(sp.Eq(C_A, C_B), g_bare)
expected_gate = sp.sqrt(2 / (c_S * N_iso))
check(
    "Equating coefficients yields the positive gate branch",
    any(sp.simplify(sol - expected_gate) == 0 for sol in gate_solution),
    detail=f"solutions={gate_solution}",
)

canonical_residual = sp.simplify(residual.subs({N_c: 3, N_iso: 2, c_S: 1}))
check(
    "Canonical residual is (g_bare^2 - 1) / 6",
    sp.simplify(canonical_residual - (g_bare**2 - 1) / 6) == 0,
    detail=f"canonical_residual={canonical_residual}",
)
check("Canonical equality holds at g_bare = 1", canonical_residual.subs(g_bare, 1) == 0)
check(
    "Canonical equality fails off surface at g_bare = 2",
    canonical_residual.subs(g_bare, 2) == sp.Rational(1, 2),
    detail=f"residual(g=2)={canonical_residual.subs(g_bare, 2)}",
)


section("Part 4: load-bearing note-displayed formula consistency")
rep_a_block = fenced_block_after(note_text, "Rep A, the OGE projection, reduces to")
rep_b_block = fenced_block_after(note_text, "Rep B, the `H_unit` projection, reduces to")
residual_block = fenced_block_after(note_text, "Their exact residual is")
canonical_block = fenced_block_after(note_text, "At the framework surface")
counterexample_block = fenced_block_after(note_text, "The exact off-surface counterexample is")

check("note contains displayed Rep A formula block", rep_a_block is not None)
if rep_a_block is not None:
    note_rep_a = last_rhs_expr(rep_a_block, SYMPY_LOCALS)
    check("note Rep A formula matches computed value", sp.simplify(note_rep_a - C_A) == 0)

check("note contains displayed Rep B formula block", rep_b_block is not None)
if rep_b_block is not None:
    note_rep_b = last_rhs_expr(rep_b_block, SYMPY_LOCALS)
    check("note Rep B formula matches computed value", sp.simplify(note_rep_b - C_B) == 0)

check("note contains displayed residual formula block", residual_block is not None)
if residual_block is not None:
    note_residual = last_rhs_expr(residual_block, SYMPY_LOCALS)
    check(
        "note residual formula matches computed value",
        sp.simplify(note_residual - expected_residual) == 0,
    )

check("note contains displayed canonical-residual block", canonical_block is not None)
if canonical_block is not None:
    note_canonical = last_rhs_expr(canonical_block, SYMPY_LOCALS)
    check(
        "note canonical residual matches computed value",
        sp.simplify(note_canonical - canonical_residual) == 0,
    )

check("note contains displayed off-surface counterexample block", counterexample_block is not None)
if counterexample_block is not None:
    counter_match = re.search(
        r"g_bare\s*=\s*([0-9]+)\s+gives residual\s+(.+)",
        counterexample_block,
    )
    check("note counterexample line is parseable", counter_match is not None)
    if counter_match is not None:
        counter_g = sp.Integer(counter_match.group(1))
        note_counter = parse_sympy_expr(counter_match.group(2), SYMPY_LOCALS)
        computed_counter = sp.simplify(canonical_residual.subs(g_bare, counter_g))
        check(
            "note counterexample residual matches computed value",
            sp.simplify(note_counter - computed_counter) == 0,
            detail=f"g_bare={counter_g}, residual={computed_counter}",
        )


section("Part 5: load-bearing D12 SU(3) Fierz coefficient input")
l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / math.sqrt(3)
generators = [m / 2 for m in (l1, l2, l3, l4, l5, l6, l7, l8)]

norm_err = 0.0
for a in range(8):
    for b in range(8):
        expected = 0.5 if a == b else 0.0
        trace_value = np.trace(generators[a] @ generators[b]).real
        norm_err = max(norm_err, abs(trace_value - expected))
check(
    "Gell-Mann normalization Tr(Ta Tb) = delta_ab / 2",
    norm_err < 1e-12,
    f"err={norm_err:.2e}",
)

fierz_err = 0.0
projection_rows: list[list[float]] = []
projection_values: list[float] = []
for i, j, k, ell in product(range(3), repeat=4):
    lhs = sum(generators[a][i, j] * generators[a][k, ell] for a in range(8)).real
    exchange_tensor = (1.0 if i == ell else 0.0) * (1.0 if j == k else 0.0)
    singlet_tensor = (1.0 if i == j else 0.0) * (1.0 if k == ell else 0.0)
    rhs = 0.5 * (exchange_tensor - singlet_tensor / 3.0)
    fierz_err = max(fierz_err, abs(lhs - rhs))
    projection_rows.append([exchange_tensor, singlet_tensor])
    projection_values.append(lhs)
check(
    "D12 Fierz identity verified over all SU(3) index tuples",
    fierz_err < 1e-12,
    f"err={fierz_err:.2e}",
)

coeffs, *_ = np.linalg.lstsq(
    np.array(projection_rows, dtype=float),
    np.array(projection_values, dtype=float),
    rcond=None,
)
exchange_coeff, singlet_coeff = coeffs
check(
    "D12 exchange coefficient is computed as 1/2",
    abs(exchange_coeff - 0.5) < 1e-12,
    detail=f"coefficient={exchange_coeff:.12g}",
)
check(
    "D12 singlet coefficient is computed as -1/(2 N_c) = -1/6",
    abs(singlet_coeff + (1 / 6)) < 1e-12,
    detail=f"coefficient={singlet_coeff:.12g}",
)


section("Part 6: load-bearing H_unit normalization input")
N_total = 6
H_unit = sp.eye(N_total) / sp.sqrt(N_total)
diag_entries_ok = all(
    sp.simplify(H_unit[idx, idx] - 1 / sp.sqrt(N_total)) == 0
    for idx in range(N_total)
)
check("H_unit diagonal entries are 1/sqrt(6)", diag_entries_ok)
check("Tr(H_unit) = sqrt(6)", sp.simplify(sp.trace(H_unit) - sp.sqrt(6)) == 0)

wick_count = sum(
    1
    for alpha, a, beta, b in product(range(2), range(3), range(2), range(3))
    if alpha == beta and a == b
)
check("Diagonal Wick-contraction count on Q_L is N_iso * N_c = 6", wick_count == 6)
check(
    "H_unit Wick saturation normalizes the diagonal count to 1",
    sp.Rational(wick_count, N_total) == 1,
    detail=f"{wick_count}/{N_total}",
)


section("Part 7: motivation-tier exhibit labels and non-consuming replay")
for required in [
    "## Motivation exhibit",
    MOTIVATION_LABEL,
    "Any nearest-rational scan, live-value replay, or numerical coincidence",
    "motivation-tier only",
    "no PDG observed value, fitted selector, or admitted unit convention",
]:
    check(
        f"note contains motivation-tier label: {required}",
        required in compact_note_text,
        tier="motivation-tier",
    )

check(
    "motivation exhibit says no value is consumed by any claim",
    "no value below is consumed by any claim" in note_text,
    tier="motivation-tier",
)

load_pass = COUNTS["load-bearing"]["pass"]
load_fail = COUNTS["load-bearing"]["fail"]
motivation_pass = COUNTS["motivation-tier"]["pass"]
motivation_fail = COUNTS["motivation-tier"]["fail"]

print()
print(f"LOAD-BEARING: PASS={load_pass} FAIL={load_fail}")
print(f"MOTIVATION-TIER: PASS={motivation_pass} FAIL={motivation_fail}")
print("=" * 88)
print(f"TOTAL: PASS={load_pass} FAIL={load_fail}")
print("=" * 88)
print(DECLARATION)
sys.exit(1 if load_fail else 0)
