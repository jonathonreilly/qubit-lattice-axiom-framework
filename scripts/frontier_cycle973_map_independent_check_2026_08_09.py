#!/usr/bin/env python3
"""Independent abstract-semantic refutation check for the Cycle 973 map.

The checker does not import the primary.  It carries a separately expressed
semantic-case catalog, reconstructs the path set from an independent pinned
blob-ID catalog, derives abstract strict-strength labels by truth-table
entailment, and reports every class disagreement as a verbatim finding.  The
row-specific mode catalog is a declared manual oracle; it is attacked for
logical consistency, not independently proved from row physics.  Findings are
scientific output, never an integrity-gate target.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import ast
import json
from pathlib import Path
import re
import subprocess

import runner_cache


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 20_000
PINNED_SNAPSHOT_COMMIT = "323d7fc32d77598f74ea6cd4d30c38dda0fe5070"
EXPECTED_PATH_DIGEST = "3241f04f3b1ffe136c5b2b20bc76ab5acdb6d3c6f9c8cb66b718f3288acfdd01"
PRIMARY_RECEIPT = ROOT / "outputs/axiom_edit_repair_map_cycle973_receipt_2026_08_09.json"
PRIMARY_CACHE = ROOT / "logs/runner-cache/frontier_cycle973_repair_map_2026_08_09.txt"
CHECK_RECEIPT = ROOT / "outputs/axiom_edit_repair_map_cycle973_independent_check_receipt_2026_08_09.json"
RUNNER_REL = "scripts/frontier_cycle973_map_independent_check_2026_08_09.py"
RECEIPT_REL = "outputs/axiom_edit_repair_map_cycle973_independent_check_receipt_2026_08_09.json"
MINIMAL_AXIOMS_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
MINIMAL_AXIOMS_PATH = ROOT / MINIMAL_AXIOMS_REL
AUDIT_INPUT_PATHS = (
    "scripts/runner_cache.py",
    "scripts/frontier_cycle973_repair_map_2026_08_09.py",
    "logs/runner-cache/frontier_cycle973_repair_map_2026_08_09.txt",
    "outputs/axiom_edit_repair_map_cycle973_receipt_2026_08_09.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
INDEPENDENT_BLOB_IDS = (
    "20955a2e976f7d3a1f38fed55cd0b1bdd91f82b4",
    "d7cc44c356540791412a11f708774a55bee5d069",
    "754e98cb997dcd667986fd3e35b36ad49320a72d",
    "5dcff503dc34b95976a270af7a1620e3dfe1747e",
    "e0fadcaf294d5c6c0057e45962947bc1c963bcd3",
    "06c0893e6bf6e7307ff2c554f9f725cc28cfd225",
    "060ca434261c21da36c836069059abb1305f3da7",
    "8f03421ca7dd22e62820670c918c2e8f388c6013",
    "b3beee9be28d84631acb35af0139ec1848a6fd46",
    "63ad3f8ec9faf6a50174cdb8c90686f31a53947a",
    "355ae2f6920a07f941750294b80da86b9739ad5a",
    "de2d33ef647fc3e0acaf8acfc10e56d3b858afb0",
    "960274498dc869044f87012300d23516dd5c6c81",
    "6de6f80c7c1a4ef98275079df4f5b871ee0d0c90",
    "7dac7b1df9ce0a1d58dac77c93e920c0d851b07a",
    "9bf32ce61d1b3397c258c98425d7bbc77a5fd481",
    "0e1ca9482fffb927eb70985cfbc8bd02d773bce6",
    "7a2c857e57e407e559be5948bda7ffffd32d6ca0",
    "717f145739244195da6db7bf05a8ff75b59bc980",
    "2091031b26d477d23fc79a4b2bb49d7968edb76f",
    "613f6f2107bb562c240048f4eab2ee707212fe7b",
    "7a71e88cd1965889b4d001fc4f15c028be29d470",
    "1749ddaaa5066f32fad13942fe27ba55bc0a8a97",
    "fb255c2ed3b7def6e8adb9239e005d6a9910596f",
    "7e368d061f3776e780a04844cdc75960a881280e",
    "f7cf8e9c1ce96a390a821f2086fc16b2c5b11e7d",
)
INDEPENDENT_BEARING_PATHS = {
    "docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md",
    "docs/TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md",
    "docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
}

# Modes are an independent adjudication grammar, not copied delta labels.
# premise: old S, new P; selector: old S=>C, new P=>C;
# countermodel: old S&!C, new P&!C; with S=>P.
# typed and ambiguous are refutation outcomes outside truth-table comparison.
INDEPENDENT_CASES = {
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md": ("typed", "rule-value codomain is not identified with a probability simplex"),
    "docs/BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md": ("typed", "support-set chirality and probability-law chirality require an explicit lift"),
    "docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md": ("premise", "neighbor-dependent support implies distribution dependence but not conversely"),
    "docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md": ("premise", "support-indexed adjacency is stronger than conditional probability dependence"),
    "docs/DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md": ("typed", "the exhibited set rule does not define a probability law"),
    "docs/FROZEN_REGION_RECORD_SATURATION_LOCAL_FINALITY_BOUNDARY_INFLUENCE_BOUNDED_NOTE_2026-07-03.md": ("typed", "monotone set containment is not a statement about weights"),
    "docs/KINETIC_ISOTROPY_3D_FACTORIZED_PROTOCOL_SELECTION_ON_ANALYZED_CLASSES_BOUNDED_THEOREM_NOTE_2026-07-09.md": ("typed", "factor-support and distribution variation are different filters without the realization bridge"),
    "docs/MATTER_REALIZATION_ARENA_SPLIT_PRESERVATION_UNDER_AXIS_COUPLED_FRAMES_BOUNDED_THEOREM_NOTE_2026-07-06.md": ("premise", "the foundation-context assertion loses support nonconstancy"),
    "docs/MATTER_REALIZATION_KS_HOP_BRIDGE_EDGE_DIAG_MEMBERSHIP_BOUNDED_THEOREM_NOTE_2026-07-06.md": ("premise", "positive-support membership is stronger than weight variation"),
    "docs/MATTER_REALIZATION_QUBIT_LEVEL_CROSS_SITE_BILINEAR_FROM_K1_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-06.md": ("selector", "a weaker distribution premise is asked to select the same K1 conclusion"),
    "docs/PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md": ("typed", "carrier reachability is not probability-support identification"),
    "docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md": ("selector", "constant support does not exclude neighbor-dependent K0 weights"),
    "docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md": ("ambiguous", "conditioning and marginalization resolution is unstated"),
    "docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md": ("selector", "same-support K0 weight changes attack K1-only selection"),
    "docs/REALIZED_KINETIC_BRANCH_SELECTION_FRAME_CLASS_TRANSPORT_NARROW_THEOREM_NOTE_2026-07-02.md": ("selector", "frame transport does not remove same-support K0 weight changes"),
    "docs/REALIZED_KINETIC_BRANCH_SELECTION_GAUGED_BACKGROUND_INVARIANCE_NARROW_THEOREM_NOTE_2026-07-02.md": ("selector", "qubit algebra gaps do not classify conditional weight changes"),
    "docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md": ("ambiguous", "the supplied bridge names both formation support and weights"),
    "docs/RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md": ("ambiguous", "the declared set rule has no declared probabilities"),
    "docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md": ("countermodel", "a support-changing countermodel can be lifted to the weaker distribution premise"),
    "docs/THETA_DEFECT_CLOSURE_FROM_ADMISSIBILITY_TEST_BOUNDED_NOTE_2026-07-03.md": ("countermodel", "the availability counterexample can satisfy a weaker distribution premise"),
    "docs/TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md": ("selector", "distribution variation need not imply nonzero off-site tick support"),
    "docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md": ("ambiguous", "the number of positive-mass alternatives and the marginal are unstated"),
    "docs/work_history/repo/review_feedback/TWELVE_HOUR_TOE_FRAMEWORK_CAMPAIGN_DIAGNOSIS_2026-07-16.md": ("premise", "neighbor-dependent distribution is weaker than neighbor-dependent support"),
    "scripts/frontier_record_local_finite_atom_availability_2026_06_17.py": ("ambiguous", "the axiom guard and the executable set control test different objects"),
    "scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py": ("selector", "the executable selector has no K0 conditional-weight exclusion"),
    "scripts/realized_kinetic_branch_selection_gauged_background_invariance_2026_07_02.py": ("selector", "the gauged executable selector has no conditional-weight model"),
}

MODE_CLASS = {
    "typed": "ORTHOGONAL_RESTATEMENT",
    "ambiguous": "UNDERDETERMINED_BY_TEXT",
}
DELTA_VOCABULARY = (
    "STRICTLY_WEAKER",
    "STRICTLY_STRONGER",
    "ORTHOGONAL_RESTATEMENT",
    "UNDERDETERMINED_BY_TEXT",
)
SEMANTIC_PATTERNS = (
    re.compile(r"available\s+possibilities.{0,260}(?:vary|depend).{0,260}(?:neighbor|neighbour)", re.I | re.S),
    re.compile(r"(?:neighbor|neighbour)[- ]dependent availability", re.I),
    re.compile(r"availability[- ]variation", re.I),
    re.compile(r"availability.{0,220}(?:vary|depend).{0,220}(?:neighbor|neighbour)", re.I | re.S),
    re.compile(r"varying availability", re.I),
    re.compile(r"available\s+possibilities.{0,220}depend.{0,120}NN conditions", re.I | re.S),
)

FAMILIES = {
    "independent_row_family": "separate 26-blob pinned membership catalog plus manual semantic-mode catalog",
    "logical_model_family": "abstract truth-table worlds (support variation S, distribution variation P, conclusion C) constrained by S=>P",
    "typed_attack_family": "support/carrier/rule-value objects versus probability distributions",
    "ambiguity_attack_family": "mixed support/weight or state-resolved/marginal text",
    "quote_attack_family": "pinned substring or Python-AST-constant verification",
}
CAPS = {
    "row_catalog_exact": 26,
    "logical_world_cap": 6,
    "pinned_blob_reads_exact": 26,
    "working_tree_corpus_reads": 0,
    "delta_vocabulary_size": 4,
    "reported_finding_cap": 26,
    "audit_input_path_cap": 5,
}


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ("git", *args), cwd=ROOT, check=True, capture_output=True
    ).stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", errors="replace")


def formula(mode: str, old: bool, s: bool, p: bool, c: bool) -> bool:
    if mode == "premise":
        return s if old else p
    if mode == "selector":
        antecedent = s if old else p
        return (not antecedent) or c
    if mode == "countermodel":
        antecedent = s if old else p
        return antecedent and not c
    raise AssertionError(mode)


def truth_table_class(mode: str) -> tuple[str, list[dict]]:
    if mode in MODE_CLASS:
        return MODE_CLASS[mode], []
    worlds = [
        (s, p, c)
        for s in (False, True)
        for p in (False, True)
        for c in (False, True)
        if (not s) or p
    ]
    rows = [
        {"S": s, "P": p, "C": c, "old": formula(mode, True, s, p, c), "new": formula(mode, False, s, p, c)}
        for s, p, c in worlds
    ]
    old_implies_new = all((not row["old"]) or row["new"] for row in rows)
    new_implies_old = all((not row["new"]) or row["old"] for row in rows)
    if old_implies_new and not new_implies_old:
        return "STRICTLY_WEAKER", rows
    if new_implies_old and not old_implies_new:
        return "STRICTLY_STRONGER", rows
    raise AssertionError(f"non-strict truth-table relation for {mode}: {rows}")


def independent_same_support_control() -> dict:
    left = {"up": 2.0 / 3.0, "down": 1.0 / 3.0}
    right = {"up": 1.0 / 3.0, "down": 2.0 / 3.0}
    return {
        "normalized": abs(sum(left.values()) - 1.0) < 1e-15 and abs(sum(right.values()) - 1.0) < 1e-15,
        "same_support": {key for key, value in left.items() if value > 0.0} == {key for key, value in right.items() if value > 0.0},
        "distribution_changed": left != right,
        "mu_0": left,
        "mu_1": right,
    }


def independent_current_axiom_boundary() -> dict[str, object]:
    body_bytes = MINIMAL_AXIOMS_PATH.read_bytes()
    body = body_bytes.decode("utf-8")
    record_match = re.search(
        r"^### Record / Fixed Reality\s*$\n(?P<body>.*?)(?=^## )",
        body,
        flags=re.MULTILINE | re.DOTALL,
    )
    if record_match is None:
        raise AssertionError("current Record section not found")
    record = record_match.group("body")
    checks = {
        "distribution_clause_present": bool(re.search(
            r"probability distribution over the possibilities.*?varies with, "
            r"the nearest-neighbor conditions",
            body,
            flags=re.DOTALL,
        )),
        "record_lock_clause_present": (
            "locks exactly one admissible local possibility" in record
        ),
        "unreadable_absence_clause_present": (
            "site with no record cannot be read" in record
        ),
        "named_scalar_I_absent_from_record": "`I`" not in record,
        "finite_additivity_absent_from_record": "finite additivity" not in record.lower(),
        "I_empty_absent_from_record": "I(empty)" not in record,
    }
    return {
        "path": MINIMAL_AXIOMS_REL,
        "sha256": sha256(body_bytes).hexdigest(),
        "checks": checks,
    }


def reconstruct_paths_from_blob_ids() -> tuple[list[str], dict[str, str]]:
    listing = git_text("ls-tree", "-r", PINNED_SNAPSHOT_COMMIT, "--", "docs", "scripts")
    paths_by_blob: dict[str, list[str]] = {}
    for line in listing.splitlines():
        metadata, path = line.split("\t", 1)
        blob_id = metadata.split()[2]
        paths_by_blob.setdefault(blob_id, []).append(path)
    resolved = {}
    for blob_id in INDEPENDENT_BLOB_IDS:
        matches = paths_by_blob.get(blob_id, [])
        if len(matches) != 1:
            raise AssertionError(f"independent blob {blob_id} resolved to {matches}")
        resolved[blob_id] = matches[0]
    return sorted(resolved.values()), resolved


def source_has_old_semantic_consumption(path: str, body: str) -> bool:
    if any(pattern.search(body) for pattern in SEMANTIC_PATTERNS):
        return True
    if path.endswith(".py"):
        tree = ast.parse(body, filename=path)
        strings = "\n".join(
            node.value for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        )
        return any(pattern.search(strings) for pattern in SEMANTIC_PATTERNS)
    return False


def exact_quote_matches(row: dict, body: str) -> bool:
    quote = row["quoted_old_semantics_consumption"]["exact_quoted_source_block"]
    extraction = row["quoted_old_semantics_consumption"]["quote_extraction"]
    if extraction.startswith("exact Python AST"):
        tree = ast.parse(body, filename=row["path"])
        return any(
            isinstance(node, ast.Constant) and node.value == quote
            for node in ast.walk(tree)
        )
    return quote in body


def delta_findings(primary_rows: dict[str, dict], independent_classes: dict[str, str]) -> list[dict]:
    findings = []
    for path in sorted(set(primary_rows) | set(independent_classes)):
        primary_class = primary_rows.get(path, {}).get("delta_class", "MISSING")
        independent_class = independent_classes.get(path, "MISSING")
        if primary_class != independent_class:
            attack = INDEPENDENT_CASES.get(path, ("missing", "path absent from independent catalog"))[1]
            verbatim = (
                f"FINDING DELTA_CLASS_DISPUTE path={path} "
                f"primary={primary_class} independent={independent_class} "
                f"attack={json.dumps(attack, ensure_ascii=False)}"
            )
            findings.append({
                "path": path,
                "primary_class": primary_class,
                "independent_class": independent_class,
                "attack": attack,
                "verbatim": verbatim,
            })
    return findings


def main() -> int:
    primary_receipt_text = PRIMARY_RECEIPT.read_text(encoding="utf-8")
    primary = json.loads(primary_receipt_text)
    primary_rows = {row["path"]: row for row in primary["rows"]}
    independent_paths, paths_by_blob = reconstruct_paths_from_blob_ids()
    tree_paths = set(git_text(
        "ls-tree", "-r", "--name-only", PINNED_SNAPSHOT_COMMIT, "--", "docs", "scripts"
    ).splitlines())

    semantic_rows = []
    body_by_path: dict[str, str] = {}
    for path in independent_paths:
        body = git_text("show", f"{PINNED_SNAPSHOT_COMMIT}:{path}")
        body_by_path[path] = body
        semantic_rows.append({
            "path": path,
            "mode": INDEPENDENT_CASES[path][0],
            "attack": INDEPENDENT_CASES[path][1],
            "old_semantic_consumption_rederived": source_has_old_semantic_consumption(path, body),
        })

    path_digest = digest(independent_paths)
    independent_control = independent_same_support_control()
    current_axiom_boundary = independent_current_axiom_boundary()
    recomputed_primary_map_digest = digest({
        "pin": primary["pinned_snapshot_commit"],
        "vocabulary": primary["delta_vocabulary"],
        "rows": primary["rows"],
    })
    independent_classes = {}
    truth_tables = {}
    for path, (mode, _attack) in INDEPENDENT_CASES.items():
        derived, table = truth_table_class(mode)
        independent_classes[path] = derived
        if table:
            truth_tables.setdefault(mode, table)

    findings = delta_findings(primary_rows, independent_classes)
    mutant_rows = {path: dict(row) for path, row in primary_rows.items()}
    mutant_path = sorted(mutant_rows)[0]
    mutant_rows[mutant_path]["delta_class"] = "STRICTLY_WEAKER"
    mutation_findings = delta_findings(mutant_rows, independent_classes)
    all_mutant_rows = {path: dict(row) for path, row in primary_rows.items()}
    for path, independent_class in independent_classes.items():
        all_mutant_rows[path]["delta_class"] = next(
            label for label in DELTA_VOCABULARY if label != independent_class
        )
    all_mutation_findings = delta_findings(all_mutant_rows, independent_classes)
    all_mutation_payload_bytes = len(
        " || ".join(finding["verbatim"] for finding in all_mutation_findings).encode()
    )

    bearing_findings = []
    for path in independent_paths:
        independent_bearing = "BEARS" if path in INDEPENDENT_BEARING_PATHS else "SILENT"
        primary_bearing = primary_rows[path]["cycle970_972_witness"]
        if independent_bearing != primary_bearing:
            bearing_findings.append(
                f"FINDING WITNESS_BEARING_DISPUTE path={path} "
                f"primary={primary_bearing} independent={independent_bearing}"
            )

    quote_checks = {
        path: exact_quote_matches(primary_rows[path], body_by_path[path])
        for path in independent_paths
        if path in primary_rows
    }
    integrity = {
        "literal_pin_matches_primary": primary["pinned_snapshot_commit"] == PINNED_SNAPSHOT_COMMIT,
        "independent_catalog_has_26_rows": len(independent_paths) == CAPS["row_catalog_exact"],
        "independent_blob_catalog_has_26_unique_ids": len(INDEPENDENT_BLOB_IDS) == len(set(INDEPENDENT_BLOB_IDS)) == 26,
        "independent_blob_catalog_resolves_uniquely": len(paths_by_blob) == 26,
        "independent_paths_have_cycle971_digest": path_digest == EXPECTED_PATH_DIGEST,
        "independent_paths_exist_at_pin": set(independent_paths) <= tree_paths,
        "all_rows_rederive_old_semantic_consumption": all(
            row["old_semantic_consumption_rederived"] for row in semantic_rows
        ),
        "primary_and_independent_path_sets_match": set(primary_rows) == set(independent_paths),
        "all_primary_quotes_match_pinned_blobs": len(quote_checks) == 26 and all(quote_checks.values()),
        "independent_classes_use_closed_vocabulary": set(independent_classes.values()) <= set(DELTA_VOCABULARY),
        "truth_table_world_cap_respected": all(len(table) <= CAPS["logical_world_cap"] for table in truth_tables.values()),
        "independent_same_support_control": all(independent_control[key] for key in ("normalized", "same_support", "distribution_changed")),
        "primary_map_digest_recomputed": recomputed_primary_map_digest == primary["map_digest"],
        "current_axiom_boundary_independently_checked": all(
            current_axiom_boundary["checks"].values()
        ),
        "primary_current_axiom_boundary_matches": (
            primary.get("current_axiom_boundary", {}).get("sha256")
            == current_axiom_boundary["sha256"]
        ),
        "primary_cache_is_canonical_and_current": runner_cache.cache_status(
            "scripts/frontier_cycle973_repair_map_2026_08_09.py"
        ) == "fresh",
        "audit_input_path_cap_respected": len(AUDIT_INPUT_PATHS) <= CAPS["audit_input_path_cap"],
        "literal_audit_input_paths": tuple(AUDIT_INPUT_PATHS) == (
            "scripts/runner_cache.py",
            "scripts/frontier_cycle973_repair_map_2026_08_09.py",
            "logs/runner-cache/frontier_cycle973_repair_map_2026_08_09.txt",
            "outputs/axiom_edit_repair_map_cycle973_receipt_2026_08_09.json",
            MINIMAL_AXIOMS_REL,
        ),
        "delta_dispute_mutation_probe_active": (
            len(mutation_findings) == 1
            and mutation_findings[0]["path"] == mutant_path
            and mutation_findings[0]["verbatim"].startswith("FINDING DELTA_CLASS_DISPUTE ")
        ),
        "all_delta_dispute_mutation_probe_active": len(all_mutation_findings) == 26,
        "all_delta_dispute_payload_fits_output_cap": (
            all_mutation_payload_bytes < HOUSE_STDOUT_LIMIT_BYTES
        ),
    }
    if not all(integrity.values()):
        raise AssertionError(f"integrity failure: {integrity}")

    histogram = Counter(independent_classes.values())
    receipt = {
        "artifact": "Cycle 973 independent abstract-semantic repair-map attack",
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "families": FAMILIES,
        "caps": CAPS,
        "delta_vocabulary": list(DELTA_VOCABULARY),
        "logical_relation": "abstract S implies P; P does not imply S by the independently printed same-support control",
        "semantic_scope": "manual per-row mode oracle; abstract logical consistency attack only; row-specific physics hypotheses are not re-proved",
        "independent_same_support_control": independent_control,
        "current_axiom_boundary": current_axiom_boundary,
        "independent_blob_ids": list(INDEPENDENT_BLOB_IDS),
        "resolved_paths_by_blob": paths_by_blob,
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "truth_tables": truth_tables,
        "independent_path_digest": path_digest,
        "independent_rows": semantic_rows,
        "independent_delta_histogram": dict(sorted(histogram.items())),
        "primary_map_digest_checked": recomputed_primary_map_digest,
        "disputed_row_count": len(findings),
        "disputed_rows": [finding["path"] for finding in findings],
        "findings_verbatim": [finding["verbatim"] for finding in findings],
        "findings": findings,
        "delta_dispute_mutation_probe": {
            "mutated_path": mutant_path,
            "mutated_class": mutant_rows[mutant_path]["delta_class"],
            "findings_verbatim": [finding["verbatim"] for finding in mutation_findings],
            "active": True,
            "all_dispute_count": len(all_mutation_findings),
            "all_dispute_payload_bytes": all_mutation_payload_bytes,
            "output_cap_bytes": HOUSE_STDOUT_LIMIT_BYTES,
            "all_dispute_payload_fits_output_cap": True,
        },
        "witness_bearing_findings_verbatim": bearing_findings,
        "refutation_outcome": (
            "PRIMARY_SURVIVES_INDEPENDENT_ABSTRACT_DELTA_ATTACK"
            if not findings else "ABSTRACT_DELTA_CLASS_FINDINGS_REPORTED_VERBATIM"
        ),
        "integrity": integrity,
        "execution_caps": {
            "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
        },
        "cache_contract": {
            "format": "canonical scripts/runner_cache.py envelope",
            "runner": RUNNER_REL,
            "receipt": RECEIPT_REL,
            "writer": "scripts/runner_cache.py",
            "deterministic_stdout": True,
        },
    }
    receipt["checker_digest"] = digest({
        "pin": PINNED_SNAPSHOT_COMMIT,
        "paths": independent_paths,
        "classes": independent_classes,
        "findings": findings,
        "primary_map_digest": recomputed_primary_map_digest,
    })
    receipt_text = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    CHECK_RECEIPT.write_text(receipt_text, encoding="utf-8")

    finding_text = "none" if not findings else " || ".join(f["verbatim"] for f in findings)
    bearing_finding_text = "none" if not bearing_findings else " || ".join(bearing_findings)
    cache_lines = [
        f"PASS R0_REFUTE_PIN_AND_ROW_SET :: pin={PINNED_SNAPSHOT_COMMIT}; independently_resolved_blobs={len(paths_by_blob)}; rows={len(independent_paths)}; path_digest={path_digest}; working_tree_corpus_reads=0",
        f"PASS R1_REFUTE_OLD_SEMANTIC_CONSUMPTION :: independently_matched={sum(r['old_semantic_consumption_rederived'] for r in semantic_rows)}/26; exact_primary_quotes_at_pin={sum(quote_checks.values())}/26",
        f"PASS R2_ATTACK_ABSTRACT_DELTA_CLASSES :: independent_histogram={compact(dict(sorted(histogram.items())))}; disputes={len(findings)}; findings_verbatim={json.dumps(finding_text, ensure_ascii=False)}",
        f"PASS R3_CONTROLS :: truth_table_modes={sorted(truth_tables)}; logical_worlds_per_mode={compact({key: len(value) for key, value in truth_tables.items()})}; same_support_control=True; primary_map_digest_recomputed=True; delta_dispute_mutation_probe=True; all_delta_disputes_payload_bytes={all_mutation_payload_bytes}; bearing_disputes={len(bearing_findings)}; bearing_findings_verbatim={json.dumps(bearing_finding_text, ensure_ascii=False)}; checker_digest={receipt['checker_digest']}",
        f"PASS R4_CURRENT_AXIOM_BOUNDARY :: path={MINIMAL_AXIOMS_REL}; sha256={current_axiom_boundary['sha256']}; independently_checked=True; primary_boundary_matches=True; Record_has_no_scalar_I_finite_additivity_or_I_empty=True",
        f"VERDICT: {receipt['refutation_outcome']}",
        "TOTAL: PASS=5 FAIL=0",
    ]
    cache = "\n".join(cache_lines) + "\n"
    if len(cache.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        raise AssertionError("checker stdout exceeds house cap")
    print(cache, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
