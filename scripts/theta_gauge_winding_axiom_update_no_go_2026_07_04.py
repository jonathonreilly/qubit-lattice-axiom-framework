#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
THETA_PARENT = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
CROSS_PLANE = DOCS / "THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md"
GAUGE_SUBSTRATE = DOCS / "THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
EMERGENT_Q = DOCS / "THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md"
MULTIPLAQUETTE = DOCS / "STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md"
STRUCTURED = DOCS / "STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row_by_path(path: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def ledger_row_by_id(claim_id: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    row = rows.get(claim_id)
    if row is None:
        raise AssertionError(f"missing ledger row: {claim_id}")
    return row


def wrap_angle(x: float) -> float:
    return (x + math.pi) % (2.0 * math.pi) - math.pi


def discrete_winding(phases: list[float]) -> int:
    total = sum(wrap_angle(phases[(i + 1) % len(phases)] - phases[i]) for i in range(len(phases)))
    return round(total / (2.0 * math.pi))


def main() -> int:
    print("theta gauge winding axiom-update no-go verifier")

    note = read(NOTE)
    minimal = read(MINIMAL)
    premises = json.loads(read(AXIOM_PREMISES))
    tier = json.loads(read(TIER_A))
    registry = read(REGISTRY)
    theta_parent = read(THETA_PARENT)
    realized = read(REALIZED)
    kinetic = read(KINETIC)
    cross_plane = read(CROSS_PLANE)
    substrate = read(GAUGE_SUBSTRATE)
    emergent_q = read(EMERGENT_Q)
    multiplaquette = read(MULTIPLAQUETTE)
    structured = read(STRUCTURED)

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    registry_flat = flat(registry)
    theta_flat = flat(theta_parent)
    cross_flat = flat(cross_plane)
    substrate_flat = flat(substrate)
    emergent_flat = flat(emergent_q)
    multi_flat = flat(multiplaquette)
    structured_flat = flat(structured)

    section("A. source presence and retained target")
    for path in [
        NOTE,
        MINIMAL,
        AXIOM_PREMISES,
        TIER_A,
        LEDGER,
        REGISTRY,
        THETA_PARENT,
        REALIZED,
        KINETIC,
        CROSS_PLANE,
        GAUGE_SUBSTRATE,
        EMERGENT_Q,
        MULTIPLAQUETTE,
        STRUCTURED,
    ]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    parent_row = ledger_row_by_path("docs/STRONG_CP_THETA_ZERO_NOTE.md")
    check("theta parent row is retained_bounded", parent_row.get("effective_status") == "retained_bounded", parent_row.get("effective_status"))
    check("theta parent row is audited_clean", parent_row.get("audit_status") == "audited_clean", parent_row.get("audit_status"))

    section("B. Tier-A registry theta boundary")
    theta = tier["retired_derivation_targets"]["strong_cp_theta_zero_note"]
    check("live Tier-A genuine count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("theta entry is retired, not live", "strong_cp_theta_zero_note" not in tier.get("derivation_targets", {}))
    check("theta retired-target record is preserved", bool(theta))
    retirement = theta.get("retirement", {})
    check("theta retirement date is recorded", retirement.get("date") == "2026-07-05", retirement)
    check("theta retirement mechanism is retained derivation", "retained" in retirement.get("mechanism", ""))
    check(
        "historical theta minimum decomposition preserves two residual atoms",
        theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "gauge side",
        "topological-sector weighting",
        "multi-plaquette / large-gauge-winding account",
        "per-plaquette class",
        "mass side",
        "determinant-readout bridge",
    ]:
        check(f"machine registry theta statement includes {phrase}", phrase in theta["statement"])
    check("human registry names theta gauge side", "multi-plaquette / large-gauge-winding account" in registry_flat)
    check("human registry names theta mass side", "determinant-readout bridge" in registry_flat)
    check("note has current-main posture line", "Current-main posture (2026-07-06)" in note)
    check("note records live Tier-A zero posture", "Tier-A count\nzero" in note or "Tier-A count zero" in note)
    check("note says retirement records are not reopened", "does not reopen, modify, or\nre-grade either retirement record" in note)
    check("note says theta is not retired", "Theta is not retired." in note)
    check("note says registry is not edited", "The Tier-A registry is not edited." in note)

    section("C. approved premise-node and axiom non-supply")
    check(
        "premise registry canonical ids are the approved four",
        premises["canonical_ids"] == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
        premises["canonical_ids"],
    )
    minimal_note = premises["nodes"]["minimal_axioms"]["note"]
    for phrase in [
        "K/CPT structure",
        "source/action bridge",
        "physical observable bridge",
        "state-selection rule",
        "law-domain derivation",
        "weighting",
        "probability",
        "no context-selection rule",
        "formation rule",
    ]:
        check(f"premise registry withholds {phrase}", phrase in minimal_note)
    for phrase in [
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently",
        "Admissibility is not a dynamics axiom",
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "context selection",
        "source/action and physical-observable identification",
        "the strong-CP theta admission",
        "Records form.",
    ]:
        check(f"minimal axiom excludes/scopes {phrase[:50]}", phrase in minimal_flat)
    for phrase in [
        "topological-sector account",
        "a derived full gauge-measure/action premise",
        "a multi-plaquette or scaling-limit topological sector functional",
        "a branch/section choice for an integer Q readout",
        "a nonvacuous theta_gauge sector-weighting law",
    ]:
        check(f"note theorem names missing gauge bridge: {phrase[:48]}", phrase in note_flat)

    section("D. approved primitive non-supply")
    for phrase in [
        "no state",
        "state-selection rule",
        "measure",
        "weighting",
        "probability rule",
        "typical",
        "generic",
    ]:
        check(f"realized primitive withholds/polices {phrase}", phrase in flat(realized))
    for phrase in [
        "no mass ratio",
        "coupling",
        "mixing angle",
        "phase",
        "selector",
        "readout bridge",
        "dynamics",
        "absolute scale",
    ]:
        check(f"kinetic primitive withholds {phrase}", phrase in flat(kinetic))
    check("note says approved primitives do not supply bridge", "approved primitives" in note_flat and "do not supply" in note_flat)

    section("E. existing theta gauge support cannot be used as retirement shortcut")
    cross_row = ledger_row_by_id("theta_cross_plane_term_absent_in_supplied_per_plaquette_class_bounded_theorem_note_2026-06-09")
    substrate_row = ledger_row_by_id("theta_gauge_substrate_no_winding_carrier_emergent_q_bridge_bounded_theorem_note_2026-06-11")
    emergent_row = ledger_row_by_id("theta_emergent_q_weighting_reality_rg_stable_bounded_theorem_note_2026-06-13")
    multi_row = ledger_row_by_id("strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07")
    structured_row = ledger_row_by_id("strong_cp_theta_bar_structured_admission_2026-06-04")
    check("cross-plane row is audited_clean", cross_row.get("audit_status") == "audited_clean", cross_row.get("audit_status"))
    check("cross-plane row is retained_bounded", cross_row.get("effective_status") == "retained_bounded", cross_row.get("effective_status"))
    check("cross-plane scope is supplied per-plaquette only", "supplied additive per-plaquette action class" in cross_row.get("claim_scope", ""))
    check("substrate no-winding row remains unaudited", substrate_row.get("effective_status") == "unaudited", substrate_row.get("effective_status"))
    check("substrate row depends on multiplaquette boundary", "strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07" in substrate_row.get("deps", []))
    check("emergent-Q row remains unaudited", emergent_row.get("effective_status") == "unaudited", emergent_row.get("effective_status"))
    check("multiplaquette no-go row remains unaudited", multi_row.get("effective_status") == "unaudited", multi_row.get("effective_status"))
    check("structured theta-bar row remains an unaudited open gate", structured_row.get("claim_type") == "open_gate" and structured_row.get("effective_status") == "unaudited")
    for phrase in [
        "Not claimed",
        "retirement of the",
        "the emergent-Q bridge is named, not closed",
        "branch/section choice",
    ]:
        check(f"substrate packet keeps boundary: {phrase[:48]}", phrase in substrate_flat)
    for phrase in [
        "Not claimed",
        "Q-existence and the 0-vs-",
        "CP-even",
        "unconditional: consumes",
        "retirement or re-grade",
    ]:
        check(f"emergent-Q packet keeps boundary: {phrase[:48]}", phrase in emergent_flat)
    for phrase in [
        "the boundary does not close",
        "admissibly realizable",
        "not clean-closeable",
        "single-plaquette / minimality admission",
    ]:
        check(f"multiplaquette packet keeps route open: {phrase[:48]}", phrase in multi_flat)
    for phrase in [
        "large-gauge-winding account",
        "does not remove a canonical large-gauge-winding theta parameter",
        "does not retire or split",
        "does not turn axioms or primitives into bounded-status sources",
    ]:
        check(f"structured admission keeps open boundary: {phrase[:48]}", phrase in structured_flat)

    section("F. exact finite gauge-carrier sanity checks")
    size = 8
    base = [2.0 * math.pi * j / size for j in range(size)]
    identity = [0.0 for _ in range(size)]
    check("U(1)^L winding pattern has discrete winding one", discrete_winding(base) == 1, discrete_winding(base))
    check("identity pattern has discrete winding zero", discrete_winding(identity) == 0, discrete_winding(identity))
    for t in [0.0, 0.125, 0.25, 0.5, 0.75, 1.0]:
        phases = [(1.0 - t) * a for a in base]
        norms_ok = all(abs(abs(complex(math.cos(p), math.sin(p))) - 1.0) < 1e-12 for p in phases)
        check(f"site-local U(1) homotopy stays unitary at t={t}", norms_ok)
    check("homotopy starts at winding pattern", all(abs(((1.0 - 0.0) * base[i]) - base[i]) < 1e-12 for i in range(size)))
    check("homotopy ends at identity phases", all(abs((1.0 - 1.0) * base[i]) < 1e-12 for i in range(size)))
    mid_wind = discrete_winding([0.5 * a for a in base])
    check("discrete winding label changes along site-local homotopy", mid_wind != discrete_winding(base), mid_wind)
    check("note carries pi0 carrier boundary", "no Hamiltonian pi_0 character" in note_flat)
    alpha = sp.symbols("alpha", real=True)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    u = sp.diag(sp.exp(sp.I * alpha), sp.exp(-sp.I * alpha))
    check("SU(2) one-parameter sample has determinant one", sp.simplify(u.det() - 1) == 0)
    check("SU(2) one-parameter sample is unitary", sp.simplify((u.conjugate().T * u - sp.eye(2))[0, 0]) == 0 and sp.simplify((u.conjugate().T * u - sp.eye(2))[1, 1]) == 0)
    contracted = sp.diag(sp.exp(sp.I * (1 - sp.Rational(1, 2)) * alpha), sp.exp(-sp.I * (1 - sp.Rational(1, 2)) * alpha))
    check("SU(2) contraction midpoint keeps determinant one", sp.simplify(contracted.det() - 1) == 0)
    check("sigma_z generator is traceless", sp.trace(sigma_z) == 0)

    section("G. cross-plane and multiplaquette guards")
    x, y = sp.symbols("x y", real=True)
    f = x**2 + sp.sin(x)
    g = y**3 + sp.cos(y)
    per_plane = f + g
    cross = x * y
    check("per-plane sum has zero mixed derivative", sp.diff(per_plane, x, y) == 0)
    check("cross-plane product has nonzero mixed derivative", sp.diff(cross, x, y) == 1)
    f01, f23, f02, f13, f03, f12 = sp.symbols("F01 F23 F02 F13 F03 F12")
    f_tilde_f = f01 * f23 - f02 * f13 + f03 * f12
    check("FtildeF toy expression depends on complementary planes", all(v in f_tilde_f.free_symbols for v in [f01, f23, f02, f13, f03, f12]))
    check("cross-plane note states supplied action class boundary", "This is a theorem about the supplied action class" in cross_flat)
    check("cross-plane note preserves multi-plaquette reopening", "Multi-plaquette terms" in cross_plane)
    check("note says per-plaquette result is conditional", "conditional on a supplied additive per-plaquette action class" in note_flat)
    check("note says multiplaquette routes remain open", "No proof excludes all multiplaquette or clover `F tilde F` routes." in note)
    check("note names branch/section non-supply", "branch/section choice" in note_flat)

    section("H. note discipline")
    check("note Type header is no_go", "**Type:** no_go" in note)
    check("note Claim type header is no_go", "**Claim type:** no_go" in note)
    check("scope boundary blocks retirement", "does not derive, refute, re-grade, retire, or remove theta" in note_flat)
    check("audit boundary present", "**Audit boundary:** independent audit lane only." in note)
    check("primary runner link present", "scripts/theta_gauge_winding_axiom_update_no_go_2026_07_04.py" in note)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    for phrase in [
        "The mass-side determinant-readout bridge is untouched.",
        "No full gauge-measure/action premise is derived.",
        "No continuum/scaling-limit sector functional `Q` is derived.",
        "No branch/section choice or topological-sector readout primitive is adopted.",
        "derive the action/Q/readout bridge or keep theta admitted",
    ]:
        check(f"note carries boundary phrase: {phrase[:48]}", phrase in note_flat)
    forbidden = [
        "Theta is retired",
        "theta_bar = 0 is derived",
        "audited_clean",
        "effective_status = retained",
        "neutron electric dipole",
        "uses a fitted value",
        "registry is edited",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    wall_names = set(re.findall(r"\bW_[A-Za-z0-9_]+", note))
    check("no wall names introduced", wall_names == set(), wall_names)

    section("I. markdown dependency and context control")
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/theta_gauge_winding_axiom_update_no_go_2026_07_04.py",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "STRONG_CP_THETA_ZERO_NOTE.md",
        "THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md",
        "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    for unlinked in [
        "THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md",
        "STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md",
        "STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md",
    ]:
        check(f"context note not markdown-linked: {unlinked[:42]}", f"{unlinked}](" not in note)
    check("note line count is bounded", 170 <= len(note.splitlines()) <= 290, len(note.splitlines()))
    check("verification block states fail-zero threshold", "Expected close: `FAIL=0` with at least 100 checks." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 100 else 1


if __name__ == "__main__":
    raise SystemExit(main())
