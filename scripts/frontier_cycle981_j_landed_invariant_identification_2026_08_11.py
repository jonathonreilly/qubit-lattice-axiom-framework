#!/usr/bin/env python3
"""Cycle 981: bounded identification census for the witness invariant J.

The runner reads six pinned source bodies through ``git show``.  A repository-
wide path/token index is used only to declare the bounded search surface; AST
inspection is confined to the two Python bodies among the six reads.  The
science outcome is never a PASS condition: a coincidence, disagreement, or
clean non-comparability all pass when the inventory and comparison bookkeeping
reconcile.
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 981
AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000

PINNED_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"
PINNED_CYCLE980_COMMIT = "c186c8ba7f44f2245cf38e59fc429ce90a6e0d7d"
PINNED_SOURCE_READS = (
    (
        PINNED_CYCLE980_COMMIT,
        "scripts/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py",
    ),
    (
        PINNED_MAIN_COMMIT,
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    ),
    (
        PINNED_MAIN_COMMIT,
        "docs/OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md",
    ),
    (
        PINNED_MAIN_COMMIT,
        "docs/historic_intake/HISTORIC_PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026_08_04_INTAKE_NOTE_2026-08-05.md",
    ),
    (
        PINNED_MAIN_COMMIT,
        "docs/historic_intake/HISTORIC_PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026_08_04_INTAKE_NOTE_2026-08-05.md",
    ),
    (
        PINNED_MAIN_COMMIT,
        "docs/historic_intake/HISTORIC_PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026_08_05_INTAKE_NOTE_2026-08-05.md",
    ),
)
EXPECTED_SOURCE_SHA256 = {
    PINNED_SOURCE_READS[0]: "a6508e92cdd0b9885c08b2a8757fe9cfaf6eedc4f2ac349d6c7713a9aa2f0305",
    PINNED_SOURCE_READS[1]: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PINNED_SOURCE_READS[2]: "37192bf117112da608ba3c0f077867b5bf0375c488bb84d114cbb291a6b42329",
    PINNED_SOURCE_READS[3]: "fe03ac2155e0e295440b1277c8933f7802807a4eca4f10909a9aaec9dc740c30",
    PINNED_SOURCE_READS[4]: "39470439a04d9ace2bfed9d187d5cac0add60be45ace8b8fe204769d3788c63a",
    PINNED_SOURCE_READS[5]: "95b7a36aac1a693e815f20614f04f34f59923c423359e701a850524579849b95",
}
EXPECTED_SOURCE_BLOBS = {
    PINNED_SOURCE_READS[0]: "5bded2470ec361453f168a68a120d0e4feba9b83",
    PINNED_SOURCE_READS[1]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PINNED_SOURCE_READS[2]: "316ca3f058c3608025d2481f27a18cfb7d9dcde6",
    PINNED_SOURCE_READS[3]: "c1124cd601eeae013ba5ce71efaf6be80353e5ff",
    PINNED_SOURCE_READS[4]: "5c18bbbaf1609214bba32fff04e3a383840bb37e",
    PINNED_SOURCE_READS[5]: "896f834c3fd7e9122f4634a1b93396bc67df11d5",
}

TOKEN_INDEX_REGEX = (
    "charge[- ]space|three[- ]parity|parity law|control[-_ ]sum|"
    "control.{0,40}sum|squared[- ]norm|norm[- ]squared|"
    "cell[- ]cut|least-cost cutting|cover|leverage|local word|local configuration"
)
EXACT_J_REGEX = (
    "control_sum_norm_squared|centre-relative control displacement|"
    "norm2\\(sum_controls\\)|\\|\\|[[:space:]]*sum_i[[:space:]]+c_i[[:space:]]*\\|\\||"
    "sum_i c_i.{0,30}(norm|squared)|J\\(w\\).{0,50}(control|norm)"
)
REQUESTED_BUT_UNLANDED_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md",
    "docs/PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_CYCLE752_NOTE_2026-08-09.md",
    "docs/PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_CYCLE753_NOTE_2026-08-09.md",
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09.md",
    "docs/PHYSICAL_CELL_CUTTING_COVER_GRAM_SPECTRUM_CYCLE761_NOTE_2026-08-10.md",
)

PRIMARY_PATH = "scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py"
RECEIPT_PATH = "outputs/j_landed_invariant_identification_cycle981_receipt_2026_08_11.json"

DIRECTIONS = (
    ("+x", (1, 0, 0)),
    ("-x", (-1, 0, 0)),
    ("+y", (0, 1, 0)),
    ("-y", (0, -1, 0)),
    ("+z", (0, 0, 1)),
    ("-z", (0, 0, -1)),
)
WITNESS_SCHEMA = "target-centred-radius-one-gate-word"


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def git_show(commit: str, relative: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def git_path_exists(commit: str, relative: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{commit}:{relative}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
    ).returncode == 0


def git_grep_paths(commit: str, expression: str) -> tuple[str, ...]:
    result = subprocess.run(
        [
            "git", "grep", "-i", "-l", "-E", expression, commit, "--",
            "docs/*.md", "docs/**/*.md", "scripts/*.py",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip())
    prefix = commit + ":"
    return tuple(sorted(
        line[len(prefix):] if line.startswith(prefix) else line
        for line in result.stdout.splitlines() if line
    ))


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def ast_has_sum_name(tree: ast.Module, name: str) -> bool:
    return any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sum"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == name
        for node in ast.walk(tree)
    )


def ast_has_two_rail_sum(tree: ast.Module) -> bool:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Compare) or len(node.ops) != 1:
            continue
        if not isinstance(node.ops[0], ast.Eq) or len(node.comparators) != 1:
            continue
        if not isinstance(node.comparators[0], ast.Constant) or node.comparators[0].value != 2:
            continue
        names = {
            child.args[0].id
            for child in ast.walk(node.left)
            if isinstance(child, ast.Call)
            and isinstance(child.func, ast.Name)
            and child.func.id == "sum"
            and child.args
            and isinstance(child.args[0], ast.Name)
        }
        if names == {"da", "db"}:
            return True
    return False


def pinned_source_controls() -> tuple[dict, dict]:
    payloads = {spec: git_show(*spec) for spec in PINNED_SOURCE_READS}
    sha_rows = {"@".join(spec): sha256(payload).hexdigest() for spec, payload in payloads.items()}
    blob_rows = {"@".join(spec): git_blob(payload) for spec, payload in payloads.items()}
    expected_sha = {"@".join(spec): value for spec, value in EXPECTED_SOURCE_SHA256.items()}
    expected_blobs = {"@".join(spec): value for spec, value in EXPECTED_SOURCE_BLOBS.items()}
    controls = {
        "pinned_main_commit": PINNED_MAIN_COMMIT,
        "pinned_cycle980_commit": PINNED_CYCLE980_COMMIT,
        "literal_source_reads": [list(spec) for spec in PINNED_SOURCE_READS],
        "literal_source_read_count": len(PINNED_SOURCE_READS),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == expected_sha,
        "blob_pins_match": blob_rows == expected_blobs,
        "head_descends_from_pinned_main": subprocess.run(
            ["git", "merge-base", "--is-ancestor", PINNED_MAIN_COMMIT, "HEAD"],
            cwd=ROOT,
            check=False,
            capture_output=True,
        ).returncode == 0,
    }
    return controls, payloads


def declared_witnesses() -> tuple[dict, ...]:
    rows = []
    for name, vector in DIRECTIONS:
        rows.append({
            "name": f"CNOT({name}->C)",
            "kind": "CNOT",
            "controls": (vector,),
        })
    for (left_name, left), (right_name, right) in combinations(DIRECTIONS, 2):
        rows.append({
            "name": f"TOF({left_name},{right_name}->C)",
            "kind": "TOF",
            "controls": (left, right),
        })
    return tuple(rows)


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def witness_values(row: dict) -> dict[str, int]:
    controls = row["controls"]
    vector_sum = tuple(sum(vector[axis] for vector in controls) for axis in range(3))
    gram_sum = sum(
        dot(controls[left], controls[right])
        for left in range(len(controls))
        for right in range(left + 1, len(controls))
    )
    return {
        "J": dot(vector_sum, vector_sum),
        "control_arity": len(controls),
        "off_diagonal_control_gram_sum": gram_sum,
    }


def candidate_inventory(payloads: dict) -> tuple[list[dict], dict]:
    c980_text = payloads[PINNED_SOURCE_READS[0]].decode()
    c719_text = payloads[PINNED_SOURCE_READS[1]].decode()
    leverage = payloads[PINNED_SOURCE_READS[2]].decode().lower()
    c732 = payloads[PINNED_SOURCE_READS[3]].decode().lower()
    c733 = payloads[PINNED_SOURCE_READS[4]].decode().lower()
    c735 = payloads[PINNED_SOURCE_READS[5]].decode().lower()
    c980_tree = ast.parse(c980_text, filename=PINNED_SOURCE_READS[0][1])
    c719_tree = ast.parse(c719_text, filename=PINNED_SOURCE_READS[1][1])
    c980_constants = {
        node.value for node in ast.walk(c980_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }

    extraction_evidence = {
        "cycle980_nearby_ast_keys": all(key in c980_constants for key in (
            "control_arity", "control_sum_norm_squared", "off_diagonal_control_gram",
        )),
        "cycle719_sum_b_ast": ast_has_sum_name(c719_tree, "b"),
        "cycle719_two_rail_sum_ast": ast_has_two_rail_sum(c719_tree),
        "oh_leverage_tokens": all(token in leverage for token in (
            "seven-site-star", "shell leverage", "3/2",
        )),
        "cycle732_tokens": all(token in c732 for token in (
            "eleven even integers", "108", "128", "228 sample points",
        )),
        "cycle733_tokens": all(token in c733 for token in (
            "eleven non-trivial column-subset costs", "ten obey a parity law",
        )),
        "cycle735_tokens": all(token in c735 for token in (
            "gf(2) weight", "sum over pieces", "7704", "8096",
        )),
    }

    def candidate(
        candidate_id: str,
        source: str,
        domain_schema: str,
        codomain: str,
        spectrum: str,
        formula: str,
        landed_at_pin: bool,
        extraction_key: str,
    ) -> dict:
        return {
            "candidate_id": candidate_id,
            "source": source,
            "domain_schema": domain_schema,
            "codomain": codomain,
            "small_spectrum": spectrum,
            "normalization": "source-native; no affine rescaling or relabeling",
            "formula_or_definition": formula,
            "landed_at_pinned_main": landed_at_pin,
            "extraction_evidence": extraction_key,
        }

    candidates = [
        candidate(
            "cycle980_control_arity",
            f"{PINNED_CYCLE980_COMMIT}:{PINNED_SOURCE_READS[0][1]}",
            WITNESS_SCHEMA, "integer", "{1,2}", "number of controls",
            False, "cycle980_nearby_ast_keys",
        ),
        candidate(
            "cycle980_off_diagonal_control_gram_sum",
            f"{PINNED_CYCLE980_COMMIT}:{PINNED_SOURCE_READS[0][1]}",
            WITNESS_SCHEMA, "integer", "{-1,0}",
            "sum over unordered control pairs (upper-triangular control-Gram entries)",
            False, "cycle980_nearby_ast_keys",
        ),
        candidate(
            "cycle719_controller_b_rail_occupation_sum",
            PINNED_SOURCE_READS[1][1],
            "cycle719-controller-trace", "integer", "finite rail occupancy",
            "sum(b) appended to the controller trace",
            True, "cycle719_sum_b_ast",
        ),
        candidate(
            "cycle719_two_rail_token_total",
            PINNED_SOURCE_READS[1][1],
            "cycle719-two-rail-controller-state", "integer", "{2} on the declared code",
            "sum(da)+sum(db)",
            True, "cycle719_two_rail_sum_ast",
        ),
        candidate(
            "oh_star_shell_leverage",
            PINNED_SOURCE_READS[2][1],
            "six-arm-oh-representation", "rational constant", "{3/2}",
            "P_T1(arm,arm)/P_E(arm,arm)",
            True, "oh_leverage_tokens",
        ),
        candidate(
            "cycle732_cell_adjacency_cost",
            PINNED_SOURCE_READS[3][1],
            "one-cell-least-volume-dissection", "integer",
            "{108,110,...,128}", "sum of piece adjacency charges",
            True, "cycle732_tokens",
        ),
        candidate(
            "cycle732_cover_certificate_parity",
            PINNED_SOURCE_READS[3][1],
            "one-cell-least-volume-dissection", "integer mod 2", "{0}",
            "228-point cover certificate forces adjacency cost mod 2",
            True, "cycle732_tokens",
        ),
        candidate(
            "cycle733_column_subset_cost_parity_law",
            PINNED_SOURCE_READS[4][1],
            "one-cell-piece-or-dissection-with-column-subset", "integer mod 2",
            "ten proper-subset parity laws; full subset is the exception",
            "certificate parity of each column-subset cost",
            True, "cycle733_tokens",
        ),
        candidate(
            "cycle735_piece_borne_gf2_charge",
            PINNED_SOURCE_READS[5][1],
            "one-cell-least-cost-cutting", "integer mod 2", "{0,1}",
            "sum of the GF(2) weights of a cutting's 24 pieces",
            True, "cycle735_tokens",
        ),
    ]
    return candidates, extraction_evidence


def compare_candidates(candidates: list[dict], witnesses: tuple[dict, ...]) -> list[dict]:
    value_rows = [(row["name"], witness_values(row)) for row in witnesses]
    results = []
    same_domain_keys = {
        "cycle980_control_arity": "control_arity",
        "cycle980_off_diagonal_control_gram_sum": "off_diagonal_control_gram_sum",
    }
    for candidate in candidates:
        row = {
            "candidate_id": candidate["candidate_id"],
            "landed_at_pinned_main": candidate["landed_at_pinned_main"],
            "candidate_domain_schema": candidate["domain_schema"],
            "J_domain_schema": WITNESS_SCHEMA,
            "normalization": candidate["normalization"],
        }
        key = same_domain_keys.get(candidate["candidate_id"])
        if candidate["domain_schema"] != WITNESS_SCHEMA:
            row.update({
                "outcome": "NOT_COMPARABLE",
                "reason": (
                    f"domain/type mismatch: {candidate['domain_schema']} -> "
                    f"{candidate['codomain']}, not {WITNESS_SCHEMA} -> integer"
                ),
                "shared_input_count": 0,
            })
        else:
            table = [
                {"word": name, "J": values["J"], "candidate": values[key]}
                for name, values in value_rows
            ]
            disagreements = [item for item in table if item["J"] != item["candidate"]]
            row.update({
                "outcome": "DISAGREES" if disagreements else "COINCIDES",
                "shared_input_count": len(table),
                "agreement_count": len(table) - len(disagreements),
                "first_witness": disagreements[0] if disagreements else None,
                "exact_agreement_table": table if not disagreements else None,
            })
        results.append(row)
    return results


def orbit_table(witnesses: tuple[dict, ...]) -> list[dict]:
    grouped = {}
    for row in witnesses:
        values = witness_values(row)
        key = (row["kind"], values["J"])
        grouped.setdefault(key, {"count": 0, "values": values})["count"] += 1
    labels = {
        ("CNOT", 1): "CNOT",
        ("TOF", 2): "TOF_PERPENDICULAR_CONTROLS",
        ("TOF", 0): "TOF_OPPOSITE_CONTROLS",
    }
    return [
        {
            "class": labels.get(key, compact(key)),
            "member_count": grouped[key]["count"],
            **grouped[key]["values"],
        }
        for key in sorted(grouped, key=lambda item: (item[0], -item[1]))
    ]


def science_measurement(payloads: dict) -> dict:
    token_paths = git_grep_paths(PINNED_MAIN_COMMIT, TOKEN_INDEX_REGEX)
    exact_j_paths = git_grep_paths(PINNED_MAIN_COMMIT, EXACT_J_REGEX)
    absent_probes = {
        path: git_path_exists(PINNED_MAIN_COMMIT, path)
        for path in REQUESTED_BUT_UNLANDED_PATHS
    }
    candidates, evidence = candidate_inventory(payloads)
    witnesses = declared_witnesses()
    comparisons = compare_candidates(candidates, witnesses)
    coincident_landed = [
        row["candidate_id"] for row in comparisons
        if row["landed_at_pinned_main"] and row["outcome"] == "COINCIDES"
    ]
    inventory_completeness_established = False
    verdict = (
        "COINCIDES_WITH_LANDED_CANDIDATE"
        if coincident_landed
        else "NO_COINCIDENCE_IN_ENUMERATED_INVENTORY__LANDED_NEWNESS_OPEN"
    )
    return {
        "search_design": {
            "snapshot": PINNED_MAIN_COMMIT,
            "path_scope": ["docs/**/*.md", "scripts/**/*.py"],
            "token_index_regex": TOKEN_INDEX_REGEX,
            "token_index_hit_file_count": len(token_paths),
            "token_index_hit_digest": digest(token_paths),
            "exact_J_formula_regex": EXACT_J_REGEX,
            "exact_J_formula_hit_paths": list(exact_j_paths),
            "body_read_design": (
                "six pinned git-show bodies: two Python ASTs plus four markdown token windows"
            ),
            "body_read_count": len(PINNED_SOURCE_READS),
            "candidate_filter": (
                "named integer/small-spectrum local-word or local-configuration quantities, "
                "plus requested norm/control-sum/cover/leverage near-misses retained for explicit type rejection"
            ),
        },
        "requested_surface_presence_at_pin": absent_probes,
        "extraction_evidence": evidence,
        "candidate_inventory": candidates,
        "witness_count": len(witnesses),
        "witness_digest": digest([
            [row["name"], row["kind"], row["controls"]] for row in witnesses
        ]),
        "orbit_value_table": orbit_table(witnesses),
        "identification_tests": comparisons,
        "coincident_landed_candidates": coincident_landed,
        "inventory_completeness_established": inventory_completeness_established,
        "verdict": verdict,
        "verdict_scope": (
            "the nine classified candidates extracted from the pinned origin/main token/AST search; "
            "the 2539-file token index is not exhaustively classified, so corpus-wide landed-newness is open"
        ),
        "physics_identification_established": False,
        "physics_identification_limit": (
            "even an exact numeric agreement would identify functions only on the shared finite domain, "
            "not their physical interpretation"
        ),
    }


def identification_bookkeeping(findings: dict) -> bool:
    candidates = {row["candidate_id"]: row for row in findings["candidate_inventory"]}
    tests = {row["candidate_id"]: row for row in findings["identification_tests"]}
    if set(candidates) != set(tests):
        return False
    witnesses = declared_witnesses()
    values = {row["name"]: witness_values(row) for row in witnesses}
    key_for = {
        "cycle980_control_arity": "control_arity",
        "cycle980_off_diagonal_control_gram_sum": "off_diagonal_control_gram_sum",
    }
    for candidate_id, candidate in candidates.items():
        test = tests[candidate_id]
        if candidate["domain_schema"] != WITNESS_SCHEMA:
            if test["outcome"] != "NOT_COMPARABLE" or test["shared_input_count"] != 0:
                return False
            continue
        key = key_for[candidate_id]
        mismatches = [
            {"word": name, "J": row["J"], "candidate": row[key]}
            for name, row in values.items() if row["J"] != row[key]
        ]
        expected_outcome = "DISAGREES" if mismatches else "COINCIDES"
        if test["outcome"] != expected_outcome:
            return False
        if test["first_witness"] != (mismatches[0] if mismatches else None):
            return False
    return True


def verdict_bookkeeping(findings: dict) -> bool:
    coincidences = sorted(
        row["candidate_id"] for row in findings["identification_tests"]
        if row["landed_at_pinned_main"] and row["outcome"] == "COINCIDES"
    )
    expected = (
        "COINCIDES_WITH_LANDED_CANDIDATE"
        if coincidences
        else "NO_COINCIDENCE_IN_ENUMERATED_INVENTORY__LANDED_NEWNESS_OPEN"
    )
    return bool(
        coincidences == sorted(findings["coincident_landed_candidates"])
        and findings["inventory_completeness_established"] is False
        and findings["verdict"] == expected
    )


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    checks = receipt["checks"]
    outcomes = {
        outcome: sum(row["outcome"] == outcome for row in findings["identification_tests"])
        for outcome in ("COINCIDES", "DISAGREES", "NOT_COMPARABLE")
    }
    first_witnesses = {
        row["candidate_id"]: row.get("first_witness")
        for row in findings["identification_tests"] if row["outcome"] == "DISAGREES"
    }
    rows = [
        "CYCLE981_J_LANDED_INVARIANT_IDENTIFICATION",
        "A_CANDIDATE_ENUMERATION " + ("PASS" if checks["A_CANDIDATE_ENUMERATION"] else "FAIL")
        + f" :: pin={PINNED_MAIN_COMMIT}; pinned_full_bodies={findings['search_design']['body_read_count']}<=6;"
        + f" token_files={findings['search_design']['token_index_hit_file_count']};"
        + f" candidates={len(findings['candidate_inventory'])};"
        + f" exact_J_hits={len(findings['search_design']['exact_J_formula_hit_paths'])};"
        + f" requested_nonmain_present={sum(findings['requested_surface_presence_at_pin'].values())}",
        "B_IDENTIFICATION_TEST " + ("PASS" if checks["B_IDENTIFICATION_TEST"] else "FAIL")
        + f" :: outcomes={compact(outcomes)}; first_witnesses={compact(first_witnesses)}",
        "C_VERDICT " + ("PASS" if checks["C_VERDICT"] else "FAIL")
        + f" :: {findings['verdict']}; coincident_landed={compact(findings['coincident_landed_candidates'])};"
        + " physics_identification=false",
        "D_CONTROLS " + ("PASS" if checks["D_CONTROLS"] else "FAIL")
        + f" :: sha_pins={receipt['controls']['sha_pins_match']};"
        + f" blob_pins={receipt['controls']['blob_pins_match']};"
        + f" determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_s={receipt['controls']['runtime_seconds']:.3f}<300;"
        + f" stdout_bytes={receipt['controls']['stdout_bytes']}<6000<150000",
    ]
    rows.append(f"TOTAL: PASS={sum(checks.values())} FAIL={sum(not value for value in checks.values())}")
    return "\n".join(rows) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls, payloads = pinned_source_controls()
    first = science_measurement(payloads)
    second = science_measurement(payloads)
    deterministic = first == second
    expected_candidate_ids = {
        "cycle980_control_arity",
        "cycle980_off_diagonal_control_gram_sum",
        "cycle719_controller_b_rail_occupation_sum",
        "cycle719_two_rail_token_total",
        "oh_star_shell_leverage",
        "cycle732_cell_adjacency_cost",
        "cycle732_cover_certificate_parity",
        "cycle733_column_subset_cost_parity_law",
        "cycle735_piece_borne_gf2_charge",
    }
    a_bookkeeping = bool(
        first["search_design"]["snapshot"] == PINNED_MAIN_COMMIT
        and first["search_design"]["body_read_count"] <= 6
        and set(row["candidate_id"] for row in first["candidate_inventory"])
        == expected_candidate_ids
        and all(first["extraction_evidence"].values())
        and all(
            first["extraction_evidence"][row["extraction_evidence"]]
            for row in first["candidate_inventory"]
        )
        and not any(first["requested_surface_presence_at_pin"].values())
    )
    b_bookkeeping = identification_bookkeeping(first)
    c_bookkeeping = verdict_bookkeeping(first)
    controls.update({
        "determinism_replay": deterministic,
        "runtime_seconds": monotonic() - started,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_bytes": 0,
    })
    receipt = {
        "cycle": CYCLE,
        "artifact": "J landed-invariant bounded identification census primary",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate source identity, extraction, comparison, and verdict reconciliation only; "
            "COINCIDES, DISAGREES, and NOT_COMPARABLE are equally reportable"
        ),
        "findings": first,
        "science_digest": digest(first),
        "controls": controls,
        "checks": {
            "A_CANDIDATE_ENUMERATION": a_bookkeeping,
            "B_IDENTIFICATION_TEST": b_bookkeeping,
            "C_VERDICT": c_bookkeeping,
            "D_CONTROLS": False,
        },
    }
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    receipt["checks"]["D_CONTROLS"] = bool(
        controls["literal_source_read_count"] <= 6
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and controls["head_descends_from_pinned_main"] and deterministic
        and controls["runtime_seconds"] < AUDIT_TIMEOUT_SEC
        and len(stdout.encode()) < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["primary_source_sha256"] = sha256((ROOT / PRIMARY_PATH).read_bytes()).hexdigest()
    receipt["stdout_sha256"] = sha256(stdout.encode()).hexdigest()
    return receipt, stdout


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit(f"usage: {Path(__file__).name}")
    receipt, stdout = run()
    receipt_path = ROOT / RECEIPT_PATH
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
