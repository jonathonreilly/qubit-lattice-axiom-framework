#!/usr/bin/env python3
"""Cycle 400: grade/Record and shared-middle law synthesis.

Cold-executes Cycles 394--397 and checks physical menu rank, local table
admission, typed-Record grade evaluation, shared-middle response, the
law-completeness ledger, and the full N1--N8 boundary.

No numerical law, probability, actuality, source, gravity, time, shared
obstruction, or axiom pressure is selected. Authority is none; audit is unset.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GRADE_RECORD_AND_SHARED_MIDDLE_LAW_"
    "SYNTHESIS_CYCLE400_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "menu_rank",
        "physical_higher_outcome_overlap_menu_fixed_carrier_cycle394_2026_07_18.py",
        "PASS 8\nFAIL 0",
        "RESULT PHYSICAL_HIGHER_OUTCOME_OVERLAP_MENU_FIXED_CARRIER_EXACT_RANK_GAIN",
    ),
    (
        "table_admission",
        "physical_nn_grade_table_admission_cycle395_2026_07_18.py",
        "SUMMARY PASS=6 FAIL=0",
        None,
    ),
    (
        "shared_middle",
        "physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18.py",
        "SUMMARY {'pass': 15, 'fail': 0}",
        "RESULT SHARED_MIDDLE_THREE_CELL_SOURCE_COMPILER_CERTIFIED",
    ),
    (
        "record_grade",
        "physical_nn_record_grade_ledger_cycle397_2026_07_18.py",
        "SUMMARY PASS=6 FAIL=0",
        None,
    ),
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-400 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "47 installed presentations",
        "exact incidence rank 31",
        "a totals 264 and b totals 269",
        "no silent reindexing connects them",
        "shared middle factor installed once rather than duplicated",
        "l3 rejects as a periodic-wrap control",
        "not physical energy, stress, source, gravity, time, occurrence, or record",
        "no route-independent obstruction",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the four positive interfaces, registry boundary, imports, and semantic firewall",
        not missing,
        missing,
    )


def cold_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}

    def execute(route):
        name, filename, pass_line, result_line = route
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / filename)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        return name, pass_line, result_line, completed

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = tuple(pool.map(execute, ROUTES))
    rows = []
    for name, pass_line, result_line, completed in results:
        output = completed.stdout + completed.stderr
        outputs[name] = output
        rows.append(
            {
                "route": name,
                "exit": completed.returncode,
                "pass": pass_line in output,
                "result": result_line is None or result_line in output,
                "lines": len(output.splitlines()),
            }
        )
    check(
        "all four numerical/source routes cold-execute green",
        all(row["exit"] == 0 and row["pass"] and row["result"] for row in rows),
        rows,
    )
    return outputs


def numerical_controls(outputs: dict[str, str]) -> None:
    rank = outputs["menu_rank"]
    admission = outputs["table_admission"]
    ledger = outputs["record_grade"]
    check(
        "physical rank 31, local A/B admission, and preserved typed-Record grade evaluation are exact",
        "'installed_menus': 47" in rank
        and "'effect_classes_after': 55" in rank
        and "'rank_after_Cycle394': 31" in rank
        and "'all_overlap_row_deletion_ranks': (30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30)" in rank
        and "'candidate_admission_bits': (1, 0, 0, 1)" in admission
        and "'one_bit_false_admissions': 0" in admission
        and "'A_aggregate': 264" in ledger
        and "'B_aggregate': 269" in ledger
        and "'A_B_discriminator': (0, 1)" in ledger
        and "'Record_payload_failures': 0" in ledger
        and "'Record_identity_failures': 0" in ledger
        and "'routed_primitives': 2367865" in ledger
        and "'Cycle390_registry_classes': 55" in ledger
        and "'Cycle395_registry_classes': 9" in ledger
        and "'Cycle390_registry_silently_reindexed': False" in ledger
        and "'Born_law': None" in ledger,
        "finite physical interfaces; numerical selection and registry bridge remain open",
    )


def source_controls(outputs: dict[str, str]) -> None:
    output = outputs["shared_middle"]
    check(
        "both operational source-vertex routes compile on one held shared-middle seam with reciprocal response",
        "'physical_matter_cells': 3" in output
        and "'naive_two_edge_endpoint_slots': 4" in output
        and "'middle_cell_multiplicity': 1" in output
        and "'L3_order_Gram_raw_maxima': (0.04472135954999576" in output
        and "'E_G_minus_Gphysical_E': 9.757364575248792e-15" in output
        and "'unit_weight': (5.958479723237607e-06, 5.958479723237605e-06)" in output
        and "'coefficient_two': (3.0046754132975383e-05, 3.004675413297537e-05)" in output
        and "'proper_cubic_frames': 24" in output
        and "'mass_fixture': 0.4534056541748851" in output
        and "'Q2_collision_configurations_in_declared_code': 0" in output
        and "'interpretation': 'dimensionless response; not physical energy/stress/source/gravity/time/occurrence/Record'" in output
        and "'axiom_pressure': False" in output,
        "strict held two-edge response; Q2, sparse primitives, source and metric identification remain open",
    )


def ledger_controls() -> None:
    text = normalized(NOTE)
    fields = (
        "domain", "state", "context", "atomic_law", "continuation",
        "availability", "concurrency", "record", "actuality", "statistics",
        "resource", "source/response",
    )
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("84/44/99", "53/33/91", "78/38/99", "49/23/80", "59/31/99")
    check(
        "the 12-field contract, six-wall ledger, and evidence-weighted lane scores are explicit",
        all(f"| {field} |" in text for field in fields)
        and all(f"| {wall} |" in text for wall in walls)
        and all(score in text for score in scores)
        and "planning estimates, not truth probabilities" in text,
        {"fields": fields, "walls": walls, "scores": scores},
    )


def no_go_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "original 36-menu physical overlap graph",
        "eleven additional fixed-carrier overlap menus",
        "exhaustive declared finite partition grammar",
        "nine-class a/b code-space normalization",
        "nine-class local table admission",
        "nine-class typed-record grade ledger",
        "55-class numerical table and record ledger",
        "autonomous table/menu selector and genesis",
        "actual-member sampler and frequency theorem",
        "strict shared-middle unit-weight route",
        "strict shared-middle coefficient-two route",
        "q2 collision and primitive-sparse source compiler",
        "common source-response/record-clock interface",
        "physical source identification and metric/clock response",
    )
    walls = ("o_menu", "o_grade", "o_actual", "o_source", "o_metric")
    pair_count = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks global no-go, minimum-content, shared-obstruction, and axiom-pressure promotion",
        all(sections)
        and all(route in text for route in routes)
        and pair_count == 10
        and "fail / do not ship a global born no-go" in text,
        {"sections": sections, "routes": len(routes), "wall_pairs": pair_count},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 400: GRADE/RECORD AND SHARED-MIDDLE LAW SYNTHESIS")
    print("authority=none; audit=unset; no selected grade, source, gravity, time, or axiom pressure")
    note_contract()
    outputs = cold_certificates()
    numerical_controls(outputs)
    source_controls(outputs)
    ledger_controls()
    no_go_controls()
    check(
        "Cycle 400 retains exact bounded gains and routes the remaining law bridges constructively",
        FAIL == 0,
        {
            "numerical_law_selected": None,
            "actuality_or_frequency": None,
            "physical_source_or_gravity": None,
            "time_law": None,
            "shared_substrate_obstruction": None,
            "axiom_pressure": None,
            "authority": "none",
            "audit": "unset",
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_GRADE_RECORD_SHARED_MIDDLE_LAW_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_GRADE_RECORD_SHARED_MIDDLE_LAW_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
