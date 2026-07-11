#!/usr/bin/env python3
"""Source-inventory support for B-AXIS.3 physical-clock admission.

This runner enumerates the note's dated admission manifest live from the
packet sources: it recomputes the packet link closure, reads the axiom leg
through the stable minimal_axioms premise node (2026-06-29 memo), and computes
the admitted physical-clock list from per-criterion source evidence instead of
preset admission flags. It intentionally does not prove that commuting factor
transfers are mathematically impossible.
"""

from __future__ import annotations

import copy
import json
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md"
SINGLE_CLOCK = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PREMISE_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
RP2 = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
SC2 = ROOT / "docs" / "AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
STONE = ROOT / "docs" / "SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md"
POST_RECORD = ROOT / "docs" / "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md"

ADMISSION_CRITERIA = (
    "supplied_as_physical_transfer",
    "positivity_trivial_kernel",
    "clock_denominator",
    "packet_consumption",
)


@dataclass
class Check:
    ok: bool
    label: str
    detail: str = ""


checks: list[Check] = []


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append(Check(bool(ok), label, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {label}{suffix}")


def assert_contains(path: Path, needle: str, label: str | None = None) -> None:
    body = read(path)
    check(needle in body, label or f"{path.name} contains {needle!r}")


def flat(path: Path) -> str:
    return " ".join(read(path).split())


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def md_link_set(path: Path) -> set[str]:
    """Markdown .md link targets outside fenced blocks, as docs/<basename>."""
    targets = re.findall(r"\]\(([^)\s]+)\)", strip_fences(read(path)))
    out: set[str] = set()
    for target in targets:
        target = target.split("#")[0]
        if target.endswith(".md"):
            out.add("docs/" + target.split("/")[-1])
    return out


def extract_manifest(path: Path) -> dict:
    blocks = re.findall(r"```json\n(.*?)```", read(path), flags=re.S)
    check(len(blocks) == 1, "note carries exactly one fenced JSON manifest block",
          f"found={len(blocks)}")
    return json.loads(blocks[0])


def evaluate_candidate(candidate: dict, surface_paths: set[str]) -> tuple[bool, str]:
    """Compute physical-clock admission from per-criterion source evidence."""
    evidence = candidate.get("criteria_evidence", {})
    if set(evidence.keys()) != set(ADMISSION_CRITERIA):
        return False, "criteria evidence does not cover exactly the four admission criteria"
    for criterion in ADMISSION_CRITERIA:
        item = evidence[criterion]
        rel = str(item.get("path", ""))
        if rel not in surface_paths:
            return False, f"{criterion}: evidence path outside the enumerated packet surface"
        source = ROOT / rel
        if not source.exists():
            return False, f"{criterion}: evidence file missing"
        anchor = " ".join(str(item.get("anchor", "")).split())
        if not anchor or anchor not in flat(source):
            return False, f"{criterion}: anchor not found in source"
    return True, "all four criteria evidenced in packet sources"


def normalize_pair(first: str, second: str) -> str:
    s = f"{first},{second}".replace("`", "").replace(" ", "")
    s = s.replace("T̂²", "T_hat^2").replace("T̂^2", "T_hat^2")
    s = s.replace("τ", "tau").replace("²", "^2")
    return s


def opnorm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def positive_transfer(generator: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(generator)
    return vecs @ np.diag(np.exp(-tau * vals)) @ vecs.conj().T


def main() -> int:
    print("single-clock physical-clock admission inventory N5 support")
    print("=" * 72)

    # --- note scope anchors ---
    assert_contains(NOTE, "ADMITTED_PHYSICAL_CLOCK_TRANSFERS=1")
    assert_contains(NOTE, "MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE")
    assert_contains(NOTE, "Does not mathematically exclude independent commuting transfer factors")
    assert_contains(NOTE, "Does not add an axiom")
    assert_contains(NOTE, "**Claim boundary:** source-inventory support")
    assert_contains(NOTE, "No second physical-clock transfer is currently admitted.")
    assert_contains(NOTE, "## Admission Manifest (2026-07-10)")
    check("not a theorem over all positive operators" in read(NOTE),
          "note states why the support is source-inventory, not algebraic exclusion")

    # --- parent packet anchors ---
    assert_contains(SINGLE_CLOCK, "(B-AXIS.3)", "single-clock source names B-AXIS.3")
    assert_contains(SINGLE_CLOCK, "admitted\n    as a second physical clock",
                    "B-AXIS.3 is phrased as an admission statement")
    assert_contains(SINGLE_CLOCK, "(T̂², 2a_τ)",
                    "single-clock source names the sole supplied transfer/step pair")
    check("This note **complies** by declaring those clauses as (B-AXIS)" in flat(SINGLE_CLOCK),
          "single-clock source keeps B-AXIS declared")

    # --- axiom authority: cited 2026-06-29 memo supplies no clock ---
    minimal_flat = flat(MINIMAL)
    check("### Lattice / Physical Locality" in minimal_flat
          and "### Qubit / Site Possibility" in minimal_flat
          and "### Admissibility / Local Constraint" in minimal_flat
          and "### Record / Fixed Reality" in minimal_flat,
          "minimal 2026-06-29 memo names the four axioms")
    check("Admissibility is not a dynamics axiom." in minimal_flat,
          "minimal 2026-06-29: Admissibility is not a dynamics axiom")
    exclusion = ("choose a Hamiltonian or transfer operator, supply transition "
                 "probabilities or weights, select a scalar or nonzero kinetic branch, "
                 "assert a Dirac-square carrier, define a time metric, or provide a "
                 "record-production process or physical persistence dynamics.")
    check(exclusion in minimal_flat,
          "minimal 2026-06-29: dynamics-exclusion sentence covers transfer operator and time metric")
    check("time metric, and local observability of records" in minimal_flat,
          "minimal 2026-06-29: time metric listed among open gates outside axiom content")
    check("Probability, dynamics, readout contexts, and physical observable bridges remain downstream."
          in minimal_flat,
          "minimal 2026-06-29: probability/dynamics/bridges stay downstream")
    check("does not derive or enlarge the axiom set" in minimal_flat,
          "minimal axiom runner does not enlarge axioms")

    # --- stable premise-node registry: 06-05 path is an alias, not a second authority ---
    registry = json.loads(read(PREMISE_NODES))
    node = registry.get("nodes", {}).get("minimal_axioms", {})
    check("minimal_axioms" in registry.get("canonical_ids", []),
          "registry lists minimal_axioms as a canonical premise node")
    check(node.get("current_path") == "docs/MINIMAL_AXIOMS_2026-06-29.md",
          "registry current path for minimal_axioms is the 2026-06-29 memo")
    check("docs/MINIMAL_AXIOMS_2026-06-05.md" in node.get("aliased_paths", []),
          "registry aliases the 2026-06-05 path to the same premise node")

    # --- manifest: structure ---
    manifest = extract_manifest(NOTE)
    note_rel = "docs/" + NOTE.name
    parent_rel = "docs/" + SINGLE_CLOCK.name
    check(manifest.get("manifest_date") == "2026-07-10", "manifest is explicitly dated 2026-07-10")
    check(manifest.get("packet_notes") == [parent_rel, note_rel],
          "manifest packet is the parent theorem note plus this inventory note")
    authority = manifest.get("axiom_authority", {})
    check(authority.get("stable_id") == "minimal_axioms"
          and authority.get("current_path") == node.get("current_path")
          and authority.get("registry") == "docs/audit/data/axiom_premise_nodes.json",
          "manifest axiom authority matches the registry premise node")

    # --- manifest: closed enumeration recomputed live from the packet notes ---
    entries = manifest.get("entries", [])
    entry_paths = [e.get("path", "") for e in entries]
    parent_links = md_link_set(SINGLE_CLOCK)
    note_links = md_link_set(NOTE)
    union = parent_links | note_links
    check(len(entries) == 19, "manifest enumerates 19 packet documents", f"got={len(entries)}")
    check(len(entry_paths) == len(set(entry_paths)), "manifest entry paths are unique")
    missing = sorted(union - set(entry_paths))
    stale = sorted(set(entry_paths) - union)
    check(not missing and not stale,
          "closed enumeration: manifest entries equal the live packet link union",
          f"missing={missing} stale={stale}")

    provenance_mismatches = []
    title_mismatches = []
    for entry in entries:
        path = entry.get("path", "")
        want = set()
        if path in parent_links:
            want.add("parent")
        if path in note_links:
            want.add("n5")
        if set(entry.get("linked_by", [])) != want or not want:
            provenance_mismatches.append(path)
        source = ROOT / path
        first_line = read(source).splitlines()[0] if source.exists() else ""
        if first_line != "# " + str(entry.get("h1", "")):
            title_mismatches.append(path)
        if not str(entry.get("role", "")).strip():
            provenance_mismatches.append(path + " (empty role)")
    check(not provenance_mismatches,
          "per-entry linked_by matches live link provenance and every role is stated",
          f"mismatches={provenance_mismatches}")
    check(not title_mismatches,
          "per-entry h1 titles match the live document headers",
          f"mismatches={title_mismatches}")
    alias_rows = {e["path"]: e.get("alias_of") for e in entries if "alias_of" in e}
    check(set(alias_rows) == {"docs/MINIMAL_AXIOMS_2026-06-05.md", "docs/MINIMAL_AXIOMS_2026-06-29.md"}
          and set(alias_rows.values()) == {"minimal_axioms"},
          "exactly the two minimal-axiom paths are marked as aliases of minimal_axioms")
    aliased_ok = all(
        path == node.get("current_path") or path in node.get("aliased_paths", [])
        for path in alias_rows
    )
    check(aliased_ok, "every manifest alias row resolves inside the registry premise node")

    # --- computed admission: evaluate candidates against packet sources ---
    surface = set(entry_paths) | set(manifest.get("packet_notes", []))
    candidates = manifest.get("candidates", [])
    check(len(candidates) == 1, "manifest proposes exactly one physical-clock candidate")
    admitted = []
    for candidate in candidates:
        ok, why = evaluate_candidate(candidate, surface)
        check(ok, f"candidate {candidate.get('name')} evaluates as admitted from source evidence", why)
        if ok:
            admitted.append(candidate)
    check(len(admitted) == 1, "computed admitted physical-clock count is one", f"got={len(admitted)}")
    check(bool(admitted) and admitted[0].get("name") == "T_hat^2"
          and admitted[0].get("clock_denominator") == "2 a_tau",
          "the computed admitted transfer is T_hat^2 with denominator 2 a_tau")

    # --- counterfeit rejectors: the same evaluator must refuse broken candidates ---
    real = candidates[0]
    fake_anchor = copy.deepcopy(real)
    fake_anchor["criteria_evidence"]["positivity_trivial_kernel"]["anchor"] = (
        "counterfeit anchor text absent from every packet source")
    ok_fake, why_fake = evaluate_candidate(fake_anchor, surface)
    check(not ok_fake, "counterfeit rejector: fabricated anchor is not admitted", why_fake)
    fake_missing = copy.deepcopy(real)
    del fake_missing["criteria_evidence"]["packet_consumption"]
    ok_fake, why_fake = evaluate_candidate(fake_missing, surface)
    check(not ok_fake, "counterfeit rejector: missing packet-consumption criterion is not admitted",
          why_fake)
    fake_outside = copy.deepcopy(real)
    fake_outside["criteria_evidence"]["supplied_as_physical_transfer"]["path"] = (
        "docs/NOT_IN_PACKET_SURFACE_NOTE.md")
    ok_fake, why_fake = evaluate_candidate(fake_outside, surface)
    check(not ok_fake, "counterfeit rejector: evidence outside the enumerated surface is not admitted",
          why_fake)

    # --- sole-pair consumption grammar in the parent packet ---
    pair_pat = re.compile(r"\(([^(),]+),([^()]*a_(?:τ|tau)[^()]*)\)")
    pairs = [normalize_pair(a, b) for a, b in pair_pat.findall(read(SINGLE_CLOCK))]
    transfer_pairs = sorted({p for p in pairs if p.startswith("T_hat^2,")})
    check(transfer_pairs == ["T_hat^2,2a_tau"],
          "parent grammar: every consumed T_hat^2 transfer/step pair normalizes to (T_hat^2, 2 a_tau)",
          f"pairs={transfer_pairs}")

    # --- admitted-pair evidence sources keep their independent anchors ---
    assert_contains(RP2, "2-step blocked transfer matrix", "RP2 supplies the two-step transfer")
    assert_contains(RP2, "positive Hermitian", "RP2 supplies positivity")
    assert_contains(RP2, "single-step transfer operator is NOT positive",
                    "RP2 excludes the single-step object as the physical positive transfer")
    assert_contains(SC2, "2 a_τ", "SC2 supplies the blocked time denominator")
    assert_contains(SC2, "H  :=  -(1/(2 a_τ)) log(T_hat^2 / M_T)",
                    "SC2 supplies corrected log normalization")
    assert_contains(STONE, "given", "Stone note is transfer-relative")
    check("uniquely determined by `T`" in read(STONE), "Stone uniqueness does not add a transfer")
    assert_contains(POST_RECORD, "supplied clock map", "post-record rates require supplied clock map")
    assert_contains(POST_RECORD, "does not supply physical elapsed time",
                    "post-record layer does not derive a clock")

    # --- mathematical comparators exist (why the exclusion claim is NOT made) ---
    ident = np.eye(2)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]])
    h_a = 1.1 * ident + 0.2 * sigma_z
    h_b = 0.8 * ident + 0.3 * sigma_z
    t_a = np.kron(positive_transfer(h_a, 1.0), ident)
    t_b = np.kron(ident, positive_transfer(h_b, 1.4))

    check(np.min(np.linalg.eigvalsh(t_a)) > 0, "mathematical comparator T_A x I is positive")
    check(np.min(np.linalg.eigvalsh(t_b)) > 0, "mathematical comparator I x T_B is positive")
    check(opnorm(t_a @ t_b - t_b @ t_a) < 1e-13,
          "mathematical comparator transfers commute",
          f"resid={opnorm(t_a @ t_b - t_b @ t_a):.2e}")

    h_a_lift = np.kron(h_a, ident)
    h_b_lift = np.kron(ident, h_b)
    span_rank = np.linalg.matrix_rank(np.stack([h_a_lift.ravel(), h_b_lift.ravel()]), tol=1e-12)
    check(span_rank == 2, "factor comparator tangent space is two-dimensional", f"rank={span_rank}")

    passed = sum(1 for c in checks if c.ok)
    failed = sum(1 for c in checks if not c.ok)
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print(f"ADMITTED_PHYSICAL_CLOCK_TRANSFERS={len(admitted)}")
    print("B_AXIS_DERIVED=FALSE")
    print("MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
