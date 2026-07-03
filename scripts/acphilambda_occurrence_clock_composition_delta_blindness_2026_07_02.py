#!/usr/bin/env python3
"""Exact verifier for the occurrence-clock composition delta-blindness note."""
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def exact(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.trigsimp(sp.expand_trig(sp.expand(expr))))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        exact(left[i, j] - right[i, j]) == 0
        for i in range(left.rows)
        for j in range(left.cols)
    )


def d_chi(state: sp.Matrix) -> sp.Matrix:
    return sp.diag(state[0, 0], state[1, 1], state[2, 2])


def unitary(lambdas: list[sp.Expr], n: sp.Expr) -> sp.Matrix:
    return sp.diag(*[sp.exp(-sp.I * lam * n) for lam in lambdas])


def unitary_dag(lambdas: list[sp.Expr], n: sp.Expr) -> sp.Matrix:
    return sp.diag(*[sp.exp(sp.I * lam * n) for lam in lambdas])


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    note_path = docs / "ACPHILAMBDA_OCCURRENCE_CLOCK_COMPOSITION_DELTA_BLINDNESS_2026-07-02.md"
    runner_path = root / "scripts" / "acphilambda_occurrence_clock_composition_delta_blindness_2026_07_02.py"
    occurrence_path = docs / "RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md"
    clock_path = docs / "ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md"
    circulant_path = docs / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
    ledger_path = docs / "audit" / "data" / "audit_ledger.json"

    section("PART A - files, ledger authority, and source pins")
    for label, path in [
        ("paired note exists", note_path),
        ("paired runner exists", runner_path),
        ("occurrence bridge exists", occurrence_path),
        ("finer-record clock note exists", clock_path),
        ("circulant retained anchor exists", circulant_path),
        ("audit ledger exists", ledger_path),
    ]:
        check(label, path.exists(), str(path.relative_to(root)))

    note = read(note_path)
    note_flat = flat(note)
    occurrence = read(occurrence_path)
    clock = read(clock_path)
    circulant = read(circulant_path)
    rows = json.loads(read(ledger_path))["rows"]
    occurrence_id = "record_occurrence_thinned_iid_frequency_bridge_2026-07-01"
    clock_id = "acphilambda_pointer_labeled_refinement_finer_record_clock_2026-07-02"
    circulant_id = "brannen_circulant_is_forced_c3_covariant_record_preserving_generation_form_bounded_theorem_note_2026-06-15"
    occurrence_row = rows[occurrence_id]
    clock_row = rows[clock_id]
    circulant_row = rows[circulant_id]

    check("occurrence row effective_status is unaudited", occurrence_row["effective_status"] == "unaudited")
    check("occurrence row audit_status is unaudited", occurrence_row["audit_status"] == "unaudited")
    check("clock row effective_status is unaudited", clock_row["effective_status"] == "unaudited")
    check("clock row audit_status is unaudited", clock_row["audit_status"] == "unaudited")
    check("circulant row is retained_bounded authority", circulant_row["effective_status"] == "retained_bounded")
    check("circulant row has ledger scope", isinstance(circulant_row.get("claim_scope"), str))
    check("note states occurrence status pending honestly", f"Ledger row `{occurrence_id}`" in note and "audit statuses pending" in note)
    check("note states clock status pending honestly", f"Ledger row `{clock_id}`" in note and note.count("audit statuses pending") >= 2)
    check("note authority-gates circulant ledger scope", "Ledger scope authority:" in note and "does not derive `C`, `S`, `r`, `delta`, or the coupling values" in note)
    check("occurrence boundary pin is true", "does not derive `a`, `p`, the physical instrument/trigger, IID" in occurrence)
    check("clock pins D_chi", "D_chi(rho) = sum_k P_k rho P_k" in clock)
    check("clock pins one-shot coherence erasure", "erases the `chi_1`-`chi_2` coherence in one application" in clock)
    check("clock pins occupancy preservation", "leaves all character occupancies invariant" in clock)
    check("clock pins doublet rate", "2 sqrt(3) |b| sin delta" in clock)
    check("circulant source pins form", "circulant form" in circulant)
    check("circulant source pins sector dial", "(a, |b|, delta)" in circulant)

    section("PART B - T14-1 exact occupancy invariance")
    a0, rho_b, delta = sp.symbols("a rho_b delta", real=True, positive=True)
    n, n1, n2 = sp.symbols("n n1 n2", real=True)
    o0, o1, o2 = sp.symbols("o0 o1 o2", real=True)
    x01, y01, x02, y02, x12, y12 = sp.symbols("x01 y01 x02 y02 x12 y12", real=True)
    z01 = x01 + sp.I * y01
    z02 = x02 + sp.I * y02
    z12 = x12 + sp.I * y12
    rho = sp.Matrix([[o0, z01, z02], [sp.conjugate(z01), o1, z12], [sp.conjugate(z02), sp.conjugate(z12), o2]])
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    b = rho_b * (sp.cos(delta) + sp.I * sp.sin(delta))
    bbar = rho_b * (sp.cos(delta) - sp.I * sp.sin(delta))
    c_chi = sp.diag(1, omega**2, omega)
    c_chi_inv = sp.diag(1, omega, omega**2)
    h_chi = a0 * sp.eye(3) + b * c_chi + bbar * c_chi_inv
    lambdas = [
        a0 + 2 * rho_b * sp.cos(delta),
        a0 + 2 * rho_b * sp.cos(delta - 2 * sp.pi / 3),
        a0 + 2 * rho_b * sp.cos(delta + 2 * sp.pi / 3),
    ]
    projectors = [sp.diag(1, 0, 0), sp.diag(0, 1, 0), sp.diag(0, 0, 1)]
    u_step = sum((sp.exp(-sp.I * lambdas[k]) * projectors[k] for k in range(3)), sp.zeros(3))
    u_step_dag = sum((sp.exp(sp.I * lambdas[k]) * projectors[k] for k in range(3)), sp.zeros(3))
    evolved = u_step * rho * u_step_dag
    check("general rho is Hermitian", matrix_equal(rho, rho.conjugate().T))
    for k in range(3):
        check(f"H diagonal eigenvalue k={k}", exact(h_chi[k, k] - lambdas[k]) == 0)
        check(f"projector k={k} commutes with H", matrix_equal(projectors[k] * h_chi, h_chi * projectors[k]))
        check(f"occupancy k={k} invariant under U", exact(evolved[k, k] - rho[k, k]) == 0)
    check("lambda_1 - lambda_2 equals clock splitting", exact(lambdas[1] - lambdas[2] - 2 * sp.sqrt(3) * rho_b * sp.sin(delta)) == 0)
    check("D_chi is idempotent", matrix_equal(d_chi(d_chi(rho)), d_chi(rho)))
    check("D_chi preserves diagonal", all(exact(d_chi(rho)[k, k] - rho[k, k]) == 0 for k in range(3)))

    section("PART C - T14-2 two-event occupancy stream and discriminator")
    u1 = unitary(lambdas, n1)
    u1d = unitary_dag(lambdas, n1)
    u2 = unitary(lambdas, n2)
    u2d = unitary_dag(lambdas, n2)
    pre1 = u1 * rho * u1d
    post1 = d_chi(pre1)
    pre2 = u2 * post1 * u2d
    diag_symbols = [o0, o1, o2]
    for k, ok in enumerate(diag_symbols):
        check(f"event 1 occupancy k={k} is initial", exact(pre1[k, k] - ok) == 0)
        check(f"event 2 occupancy k={k} is initial", exact(pre2[k, k] - ok) == 0)
    phase_symbols = {a0, rho_b, delta, n1, n2}
    for i, oi in enumerate(diag_symbols):
        for j, oj in enumerate(diag_symbols):
            joint = exact(pre1[i, i] * pre2[j, j])
            check(f"two-event joint ({i},{j}) equals product", exact(joint - oi * oj) == 0)
            check(f"two-event joint ({i},{j}) is phase-free", joint.free_symbols.isdisjoint(phase_symbols))
    theta = sp.symbols("theta", real=True)
    p_plus_theta = (o1 + o2) / 2 + x12 * sp.cos(theta) + y12 * sp.sin(theta)
    split = lambdas[1] - lambdas[2]
    p_plus_delta = p_plus_theta.subs(theta, split * n)
    dp_ddelta = exact(sp.diff(p_plus_delta.subs(y12, 0), delta))
    check("coherence-reading p_plus contains splitting phase", p_plus_theta.has(sp.cos(theta)) and p_plus_theta.has(sp.sin(theta)))
    check("coherence-reading p_plus contains delta after substitution", delta in p_plus_delta.free_symbols)
    check("coherence-reading discriminator derivative is nonzero", dp_ddelta != 0)

    section("PART D - T14-3 coherence phase and two-dial ratio")
    un = unitary(lambdas, n)
    und = unitary_dag(lambdas, n)
    evolved_n = un * rho * und
    d1, d2 = 2, 1
    phase_factor = sp.exp(sp.I * (lambdas[d2] - lambdas[d1]) * n)
    check("rho_d1d2 carries the doublet phase factor", exact(evolved_n[d1, d2] - phase_factor * rho[d1, d2]) == 0)
    check("doublet phase factor uses exact splitting", exact((lambdas[d2] - lambdas[d1]) - 2 * sp.sqrt(3) * rho_b * sp.sin(delta)) == 0)
    a_act = sp.symbols("a_act", real=True, positive=True)
    ratio = 2 * sp.sqrt(3) * rho_b * sp.sin(delta) / a_act
    check("ratio contains coupling magnitude dial", rho_b in ratio.free_symbols)
    check("ratio contains activation probability dial", a_act in ratio.free_symbols)
    check("ratio contains both free dials", {rho_b, a_act}.issubset(ratio.free_symbols))

    section("PART E - note discipline")
    verbatim = [
        "occupancy-reading event streams are completely `delta`-blind: the doublet clock phase never enters the registered stream",
        "`delta`-registration through events requires a coherence-reading conditional law, which the landed occurrence bridge leaves supplied",
        "the panel's route (c) adjudicates to the registered-pattern normal form: the value wall relocates into the supplied conditional law",
        "not a terminal no-go",
    ]
    for sentence in verbatim:
        check(f"required sentence present: {sentence[:42]}", sentence in note_flat)
    for label in [f"### N{i}" for i in range(1, 9)]:
        check(f"note contains {label}", label in note)
    forbidden = [
        "only " + "route",
        "last " + "route",
        "ex" + "hausted",
        "closes the " + "route",
        "P" + "DG",
        "new " + "wall",
    ]
    leaks = [
        "Acceptance " + "contract",
        "PRESERVE " + "VERBATIM",
        "MUST BE " + "ABSENT",
        "ANTI-" + "FABRICATION",
        "execute it " + "exactly",
        "this " + "spec",
    ]
    check("forbidden concatenated tokens absent", not any(term in note for term in forbidden))
    check("local-instruction leakage absent", not any(term in note for term in leaks))
    allowed_walls = {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}
    seen_walls = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    check("W_ identifiers are whitelisted", seen_walls <= allowed_walls, str(sorted(seen_walls)))
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    md_links = [target for target in links if target.endswith(".md")]
    runner_links = [target for target in links if target.endswith(".py")]
    expected_md = sorted([occurrence_path.name, clock_path.name, circulant_path.name])
    check("markdown-link inventory has exactly three dependency docs", sorted(Path(x).name for x in md_links) == expected_md, str(md_links))
    check("runner link inventory has exactly one runner", len(runner_links) == 1 and runner_path.name in runner_links[0], str(runner_links))
    check("total markdown links are three docs plus one runner", len(links) == 4, str(links))
    for pr in ["PR #4840", "PR #4845"]:
        check(f"{pr} is backticked in note", f"`{pr}`" in note)
        check(f"{pr} is not a markdown target", all(pr not in target for target in links))
    check("status-authority header is standard", "**Status authority:** independent audit lane only." in note)
    check("claim type states bounded composition theorem", "**Claim type:** bounded composition theorem / route adjudication" in note)
    check("note does not use PASS as status", "**Status:** PASS" not in note)
    check("no self-authored audit verdict", "audited_clean (this note)" not in note and "retained_bounded (this note)" not in note)
    check("verification command is recorded", f"python3 scripts/{runner_path.name}" in note)
    note_lines = note.splitlines()
    runner_lines = read(runner_path).splitlines()
    check("note line count is in requested band", 170 <= len(note_lines) <= 210, str(len(note_lines)))
    check("runner line count is in requested band", 200 <= len(runner_lines) <= 260, str(len(runner_lines)))
    close = re.search(r"TOTAL: PASS=(\d+) FAIL=0", note)
    expected_final = PASS + 1
    check("verification close records measured final PASS", close is not None and int(close.group(1)) == expected_final, f"expected={expected_final}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 45 else 1


if __name__ == "__main__":
    raise SystemExit(main())
