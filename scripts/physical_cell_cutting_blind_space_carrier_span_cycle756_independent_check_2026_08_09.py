#!/usr/bin/env python3
"""Independent exact checker for the bounded Cycle 756 incidence theorem.

The primary runner is executed live to rebuild the explicitly supplied finite
fixture.  This checker then uses SymPy exact domain-matrix elimination instead
of the primary's modular row reduction, and NetworkX maximal-clique enumeration
instead of the primary's fixed-depth carrier recursion.  Fixture construction
is shared and declared; the load-bearing rank and carrier algorithms are not.
"""
from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import runpy
import sys
import time
from pathlib import Path

import networkx as nx
import numpy as np
from sympy import ZZ, isprime
from sympy.polys.matrices import DomainMatrix


AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_2026_08_09.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_BLIND_SPACE_CARRIER_SPAN_CYCLE756_"
    "NOTE_2026-08-09.md"
)
RECEIPT_RELATIVE = (
    "outputs/physical_cell_cutting_blind_space_carrier_span_cycle756_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
RECEIPT_PATH = ROOT / RECEIPT_RELATIVE
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_BLIND_SPACE_CARRIER_SPAN_CYCLE756_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_2026_08_09.py",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(relative_path):
    """Return the SHA-256 digest of one repository-relative file."""
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def write_failure(reason):
    """Leave a fail-closed receipt if execution stops before finalization."""
    RECEIPT_PATH.write_text(
        json.dumps(
            {
                "schema": "physical-cell-cutting-carrier-span-cycle756-independent-v1",
                "status": "fail",
                "claim_type": "bounded_theorem",
                "reason": reason,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


write_failure("checker has not completed")

passed = 0
failed = 0
gates = {}
started = time.monotonic()


def gate(name, condition, detail):
    """Record and print one fail-closed checker gate."""
    global passed, failed
    ok = bool(condition)
    gates[name] = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    else:
        failed += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


def exact_rank(matrix):
    """Compute the characteristic-zero rank with exact integer elimination."""
    rows = [[int(value) for value in row] for row in np.asarray(matrix)]
    return int(DomainMatrix.from_list(rows, ZZ).rank())


primary_stdout = io.StringIO()
try:
    with contextlib.redirect_stdout(primary_stdout):
        primary = runpy.run_path(
            str(ROOT / PRIMARY_PATH),
            run_name="__cycle756_primary_live_replay__",
        )
except BaseException as exc:
    write_failure("primary live replay failed: {0}".format(type(exc).__name__))
    print("FAIL independent.primary_live_replay  primary execution raised " + type(exc).__name__)
    print("TOTAL: PASS=0 FAIL=1")
    raise SystemExit(1) from exc

primary_text = primary_stdout.getvalue()
gate(
    "independent.primary_live_replay",
    primary.get("PF") == [10, 0]
    and "FAIL " not in primary_text
    and "TOTAL: PASS=10 FAIL=0\n" in primary_text,
    "the primary rebuild executes live with ten gates and fail-closed status",
)

MM = primary["MM"]
IV = primary["IV"]
identity4 = np.eye(4, dtype=np.int64)
inverse_products = all(
    np.array_equal(MM[index] @ IV[index], identity4)
    and np.array_equal(IV[index] @ MM[index], identity4)
    for index in range(len(MM))
)
rotations = primary["ROT"]
group = primary["G"]
action_keys = {tuple(int(value) for value in entry[2]) for entry in group}
determinant_profile = {
    sign: sum(
        int(primary["det3"](rotation)) * (-1 if reflected else 1) == sign
        for rotation, reflected, _ in group
    )
    for sign in (-1, 1)
}
gate(
    "independent.fixture_integrity",
    inverse_products
    and primary["coll"] == 0
    and primary["face"] == 0
    and len(rotations) == 24
    and len(group) == len(action_keys) == 48
    and determinant_profile == {-1: 24, 1: 24},
    "exact inverses, encoder integrity, and the precisely named 48-element action agree",
)

INC = primary["INC"]
INCL = primary["INCL"]
W = primary["W"]
SH = primary["SH"]
D4 = primary["D4"]
GR = primary["GR"]

row_weights = INC.sum(axis=1)
column_weights = INC.sum(axis=0)
gate(
    "independent.incidence_census",
    INC.shape == (15800, 192)
    and set(int(value) for value in row_weights) == {24}
    and set(int(value) for value in column_weights) == {1975}
    and int(row_weights.sum()) == int(column_weights.sum()) == 379200,
    "the rebuilt integer incidence object has the declared complete census",
)

zero_graph = nx.Graph()
zero_graph.add_nodes_from(range(GR.shape[0]))
zero_graph.add_edges_from(
    (left, right)
    for left in range(GR.shape[0])
    for right in range(left + 1, GR.shape[1])
    if int(GR[left, right]) == 0
)
maximal_cliques = [
    tuple(sorted(int(value) for value in row))
    for row in nx.find_cliques(zero_graph)
]
size_eight_cliques = {
    frozenset(row) for row in maximal_cliques if len(row) == 8
}
primary_carriers = {frozenset(int(value) for value in row) for row in primary["CLQ"]}
gate(
    "independent.maximal_cliques",
    len(maximal_cliques) == 768
    and max(len(row) for row in maximal_cliques) == 8
    and len(size_eight_cliques) == 192
    and size_eight_cliques == primary_carriers,
    "NetworkX independently enumerates exactly the same 192 size-eight maximal cliques",
)

carrier_images = INCL @ W.T
support_sizes = np.abs(D4).sum(axis=1)
gate(
    "independent.carrier_images",
    np.array_equal(carrier_images, np.ones_like(carrier_images))
    and np.array_equal(INCL @ D4.T, np.zeros((len(INCL), len(D4)), dtype=np.int64))
    and set(int(value) for value in support_sizes) == {8},
    "direct integer multiplication verifies every carrier image and 384 "
    "support-eight kernel witnesses",
)

# For an integer matrix M, rank_Q(M) equals rank_Q(M^T M).  The Gram form
# keeps exact elimination bounded to 192-by-192 matrices while preserving rank.
incidence_rank = exact_rank(GR)
carrier_rank = exact_rank(W.T @ W)
difference_rows = W[1:] - W[0]
difference_rank = exact_rank(difference_rows.T @ difference_rows)
gate(
    "independent.exact_ranks",
    (incidence_rank, carrier_rank, difference_rank) == (88, 105, 104),
    "SymPy domain matrices give exact characteristic-zero ranks 88, 105, and 104",
)

overlap_counts = {}
overlap_ranks = {}
for overlap in (0, 1, 2, 4):
    pairs = [
        (left, right)
        for left in range(len(W))
        for right in range(left + 1, len(W))
        if int(SH[left, right]) == overlap
    ]
    differences = W[[left for left, _ in pairs]] - W[[right for _, right in pairs]]
    overlap_counts[str(overlap)] = len(pairs)
    overlap_ranks[str(overlap)] = exact_rank(differences.T @ differences)
gate(
    "independent.overlap_classes",
    overlap_counts == {"0": 15072, "1": 1920, "2": 960, "4": 384}
    and overlap_ranks == {"0": 104, "1": 104, "2": 104, "4": 104},
    "exact elimination verifies the full overlap profile and rank 104 for every populated class",
)

big_prime = int(primary["BIGP"])
small_prime = int(primary["SMLP"])
int64_safe = 192 * (big_prime - 1) ** 2 < int(np.iinfo(np.int64).max)
gate(
    "independent.modular_arithmetic_contract",
    isprime(big_prime) and isprime(small_prime) and int64_safe,
    "both declared moduli are prime and the elimination dot products fit signed int64",
)

input_hashes = {path: sha256(path) for path in AUDIT_INPUT_PATHS}
receipt = {
    "schema": "physical-cell-cutting-carrier-span-cycle756-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": input_hashes,
    "method": {
        "fixture": "shared live primary construction",
        "carrier_enumeration": "NetworkX maximal-clique enumeration",
        "rank": "SymPy exact DomainMatrix rank of integer Gram matrices",
    },
    "finite_object": {
        "incidence_shape": [int(value) for value in INC.shape],
        "maximal_cliques": len(maximal_cliques),
        "size_eight_carriers": len(size_eight_cliques),
        "support_eight_kernel_witnesses": len(D4),
        "overlap_counts": overlap_counts,
        "group_order": len(group),
        "four_coordinate_determinant_profile": {
            str(key): value for key, value in determinant_profile.items()
        },
    },
    "exact_ranks": {
        "incidence": incidence_rank,
        "carriers": carrier_rank,
        "carrier_differences": difference_rank,
        "overlap_classes": overlap_ranks,
    },
}


def receipt_contract(candidate):
    """Validate all load-bearing receipt fields against current repository bytes."""
    return (
        candidate.get("schema")
        == "physical-cell-cutting-carrier-span-cycle756-independent-v1"
        and candidate.get("status") == "pass"
        and candidate.get("claim_type") == "bounded_theorem"
        and candidate.get("checker_sha256") == sha256(CHECKER_PATH)
        and candidate.get("input_sha256")
        == {path: sha256(path) for path in AUDIT_INPUT_PATHS}
        and candidate.get("finite_object", {}).get("incidence_shape") == [15800, 192]
        and candidate.get("finite_object", {}).get("size_eight_carriers") == 192
        and candidate.get("finite_object", {}).get("support_eight_kernel_witnesses") == 384
        and candidate.get("exact_ranks", {}).get("incidence") == 88
        and candidate.get("exact_ranks", {}).get("carriers") == 105
        and candidate.get("exact_ranks", {}).get("carrier_differences") == 104
        and candidate.get("exact_ranks", {}).get("overlap_classes")
        == {"0": 104, "1": 104, "2": 104, "4": 104}
    )


gate(
    "receipt.current_contract",
    receipt_contract(receipt),
    "the receipt schema, exact results, checker digest, and all declared inputs are current",
)
altered_rank = copy.deepcopy(receipt)
altered_rank["exact_ranks"]["incidence"] = 87
gate(
    "hostile.receipt_rank",
    not receipt_contract(altered_rank),
    "the receipt contract detects an altered exact incidence rank",
)
altered_input = copy.deepcopy(receipt)
altered_input["input_sha256"][PRIMARY_PATH] = "0" * 64
gate(
    "hostile.receipt_input",
    not receipt_contract(altered_input),
    "the receipt contract detects an altered primary-source digest",
)
gate(
    "independent.runtime_contract",
    time.monotonic() - started < AUDIT_TIMEOUT_SEC,
    "the complete live replay and independent checks satisfy the 900-second contract",
)

receipt["status"] = "pass" if failed == 0 else "fail"
receipt["gates"] = {"pass": passed, "fail": failed, "named": gates}
RECEIPT_PATH.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print("RECEIPT " + RECEIPT_RELATIVE, flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
raise SystemExit(0 if failed == 0 else 1)
