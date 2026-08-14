"""Independent checker for the Cycle 755 finite isotypic-overlap theorem.

The checker imports no Cycle 755 primary symbols.  It live-replays the current
Cycle 754 independent reconstruction, then uses exact character inner products,
ordered-pair orbitals, two modular residual-rank calculations, and a separate
exact signed-orbit span calculation.
"""
import contextlib
import copy
import hashlib
import io
import json
import runpy
import sys
from pathlib import Path

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_2026_08_09.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_BLIND_SPACE_SYMMETRY_"
    "CYCLE755_NOTE_2026-08-09.md"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_blind_space_symmetry_cycle755_"
    "2026_08_09_receipt_2026-08-09.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_blind_space_symmetry_cycle755_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
C754_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_"
    "CYCLE754_NOTE_2026-08-09.md"
)
C754_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py"
)
C754_CHECKER_PATH = (
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "independent_check_2026_08_09.py"
)
C754_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "2026_08_09_receipt_2026-08-09.json"
)
C754_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_BLIND_SPACE_SYMMETRY_CYCLE755_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_2026_08_09.py",
    "outputs/physical_cell_cutting_blind_space_symmetry_cycle755_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py",
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_independent_check_2026_08_09_receipt_2026-08-09.json",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded.get(path) == sha256(path)
        for path in recorded
    )


def write_failure(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-isotypic-overlap-cycle755-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cycle754_contract(primary, independent):
    return (
        primary.get("schema") == "physical-cell-cutting-shadow-rank-cycle754-v2"
        and primary.get("status") == "pass"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C754_PRIMARY_PATH)
        and inputs_current(primary)
        and primary.get("rational_shadow", {}).get("rank") == 88
        and primary.get("rational_shadow", {}).get("kernel_dimension") == 104
        and independent.get("schema")
        == "physical-cell-cutting-shadow-rank-cycle754-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C754_CHECKER_PATH)
        and inputs_current(independent)
        and independent.get("rational_shadow", {}).get("rank") == 88
        and independent.get("rational_shadow", {}).get("kernel_dimension") == 104
    )


def primary_contract(receipt):
    finite = receipt.get("finite_object", {})
    overlap = receipt.get("character_overlap", {})
    commutant = receipt.get("commutant", {})
    exchange = receipt.get("least_exchange_orbit", {})
    boundary = receipt.get("boundary", {})
    dependency = receipt.get("direct_dependencies", {}).get("cycle754", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-isotypic-overlap-cycle755-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and dependency.get("contract_current") is True
        and dependency.get("receipt_sha256") == sha256(C754_RECEIPT_PATH)
        and dependency.get("independent_receipt_sha256")
        == sha256(C754_INDEPENDENT_RECEIPT_PATH)
        and finite.get("group_order") == 384
        and finite.get("sharing_rank") == 88
        and finite.get("blind_dimension") == 104
        and finite.get("blind_invariant_under_group") is True
        and overlap == {
            "seen_seen": 29,
            "seen_blind": 21,
            "blind_blind": 33,
            "endomorphism_dimension": 104,
            "blind_is_sum_of_complete_isotypic_components": False,
            "rank_88_derived_from_group_fixed_point_characters": False,
        }
        and commutant.get("ordered_pair_orbits") == 104
        and commutant.get("residual_rank_mod_prime") == 21
        and commutant.get("blind_preserving_dimension") == 83
        and commutant.get("individual_orbital_matrices_preserving_blind") == 2
        and exchange.get("signed_images") == 192
        and exchange.get("span_dimension") == 60
        and exchange.get("blind_complement_dimension") == 44
        and boundary.get("blind_space_is_group_invariant") is True
        and boundary.get("all_symmetry_or_incidence_routes_to_rank_excluded") is False
        and boundary.get("all_support_eight_blind_vectors_classified") is False
        and boundary.get("remaining_44_dimensions_generated") is False
    )


def rank_mod(matrix, prime):
    array = np.asarray(matrix, dtype=np.int64).copy() % prime
    row = 0
    for column in range(array.shape[1]):
        candidates = np.flatnonzero(array[row:, column])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        if pivot != row:
            array[[row, pivot]] = array[[pivot, row]]
        array[row] = (array[row] * pow(int(array[row, column]), -1, prime)) % prime
        factors = array[row + 1:, column].copy()
        nonzero = np.flatnonzero(factors)
        if len(nonzero):
            array[row + 1 + nonzero] = (
                array[row + 1 + nonzero]
                - np.outer(factors[nonzero], array[row])
            ) % prime
        row += 1
        if row == array.shape[0]:
            break
    return row


passed = 0
failed = 0
gates = {}


def gate(name, condition, detail):
    global passed, failed
    ok = bool(condition)
    gates[name] = "PASS" if ok else "FAIL"
    passed += int(ok)
    failed += int(not ok)
    compact = detail if len(detail) <= 116 else detail[:113] + "..."
    print(("PASS " if ok else "FAIL ") + name + "  " + compact, flush=True)


write_failure("checker has not completed")
C754 = load(C754_RECEIPT_PATH)
C754I = load(C754_INDEPENDENT_RECEIPT_PATH)
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C754_OK = cycle754_contract(C754, C754I)
gate("independent.cycle754_contract", C754_OK,
     "current Cycle 754 receipts bind rank 88, kernel dimension 104, and the least exchange")

# Replay the independent predecessor without overwriting its canonical receipt.
old_exit = sys.exit
old_write_text = Path.write_text
dependency_receipt = (ROOT / C754_INDEPENDENT_RECEIPT_PATH).resolve()


def guarded_write_text(self, data, *args, **kwargs):
    if self.resolve() == dependency_receipt:
        return len(data)
    return old_write_text(self, data, *args, **kwargs)


sys.exit = lambda _code=0: None
Path.write_text = guarded_write_text
capture = io.StringIO()
try:
    with contextlib.redirect_stdout(capture):
        predecessor = runpy.run_path(str(ROOT / C754_CHECKER_PATH), run_name="__main__")
finally:
    Path.write_text = old_write_text
    sys.exit = old_exit

predecessor_stdout = capture.getvalue()
gate(
    "independent.cycle754_live_replay",
    predecessor.get("failed") == 0
    and "FAIL " not in predecessor_stdout
    and "TOTAL: PASS=15 FAIL=0" in predecessor_stdout,
    "the independent Cycle 754 reconstruction completes live with all fifteen gates",
)

incidence = np.asarray(predecessor["incidence"], dtype=np.int64)
gram = np.asarray(predecessor["gram"], dtype=np.int64)
kernel = np.asarray(predecessor["kernel"], dtype=np.int64)
group = [np.asarray(permutation, dtype=np.int64) for permutation in predecessor["group"]]
n = incidence.shape[1]
k = kernel.shape[0]

free = [-1] * k
identity = np.eye(k, dtype=np.int64)
for column in range(n):
    matches = np.flatnonzero(np.all(kernel[:, column, None] == identity, axis=0))
    if len(matches) == 1:
        free[int(matches[0])] = column
gate(
    "independent.reconstruction",
    incidence.shape == (15800, 192)
    and kernel.shape == (104, 192)
    and len(group) == 384
    and min(free) >= 0
    and np.array_equal(kernel[:, free], identity),
    "the predecessor supplies the exact incidence, 104-row free-column kernel basis, and 384 symmetries",
)

fixed_character = [int(np.count_nonzero(permutation == np.arange(n))) for permutation in group]
blind_character = [int(np.trace(kernel[:, permutation][:, free])) for permutation in group]
seen_character = [fixed_character[index] - blind_character[index] for index in range(len(group))]


def character_inner(left, right):
    total = sum(a * b for a, b in zip(left, right))
    quotient, remainder = divmod(total, len(group))
    return quotient, remainder


seen_seen = character_inner(seen_character, seen_character)
seen_blind = character_inner(seen_character, blind_character)
blind_blind = character_inner(blind_character, blind_character)
fixed_fixed = character_inner(fixed_character, fixed_character)
gate(
    "independent.characters",
    seen_seen == (29, 0)
    and seen_blind == (21, 0)
    and blind_blind == (33, 0)
    and fixed_fixed == (104, 0)
    and seen_seen[0] + 2 * seen_blind[0] + blind_blind[0] == fixed_fixed[0],
    "exact character inner products are 29, 21, 33 and rebuild the 104-dimensional endomorphism algebra",
)

# Build ordered-pair orbitals directly, then impose Gram*A*kernel^T = 0.
group_array = np.asarray(group, dtype=np.int64)
labels = np.full(n * n, -1, dtype=np.int64)
orbit_count = 0
for pair in range(n * n):
    if labels[pair] >= 0:
        continue
    left, right = divmod(pair, n)
    labels[group_array[:, left] * n + group_array[:, right]] = orbit_count
    orbit_count += 1
label_matrix = labels.reshape(n, n)
residual_vectors = []
residual_maxima = []
preserving = []
group_set = {tuple(int(value) for value in permutation) for permutation in group}
preserving_are_group_permutations = True
for orbital in range(orbit_count):
    matrix = (label_matrix == orbital).astype(np.int64)
    residual = gram @ (matrix @ kernel.T)
    maximum = int(np.abs(residual).max())
    residual_maxima.append(maximum)
    residual_vectors.append(residual.reshape(-1))
    if maximum == 0:
        preserving.append(orbital)
        if not (np.all(matrix.sum(axis=0) == 1) and np.all(matrix.sum(axis=1) == 1)):
            preserving_are_group_permutations = False
        else:
            permutation = tuple(int(np.flatnonzero(matrix[row])[0]) for row in range(n))
            preserving_are_group_permutations &= permutation in group_set
residual_matrix = np.asarray(residual_vectors, dtype=np.int64)
residual_rank_1 = rank_mod(residual_matrix, 1000003)
residual_rank_2 = rank_mod(residual_matrix, 1000033)
gate(
    "independent.orbital_residual",
    orbit_count == 104
    and residual_rank_1 == residual_rank_2 == 21
    and len(preserving) == 2
    and preserving_are_group_permutations
    and max(residual_maxima) == 12738,
    "104 ordered-pair orbitals give residual rank 21 twice; 2 individual orbitals preserve the kernel",
)

seed = np.zeros(n, dtype=np.int64)
seed[[4, 5, 10, 11]] = 1
seed[[1, 3, 7, 9]] = -1
signed_orbit = sorted({tuple(int(value) for value in seed[permutation]) for permutation in group})
orbit_matrix = np.asarray(signed_orbit, dtype=np.int64)
orbit_rank_exact = int(sp.Matrix(orbit_matrix.tolist()).rank())
orbit_rank_1 = rank_mod(orbit_matrix, 1000003)
orbit_rank_2 = rank_mod(orbit_matrix, 1000033)
gate(
    "independent.exchange_orbit",
    len(signed_orbit) == 192
    and np.array_equal(incidence @ orbit_matrix.T, np.zeros((15800, 192), dtype=np.int64))
    and orbit_rank_exact == orbit_rank_1 == orbit_rank_2 == 60,
    "the signed four-for-four orbit has 192 exact blind vectors and exact/modular span dimension 60",
)

PRIMARY_OK = primary_contract(PRIMARY)
gate("independent.primary_contract", C754_OK and PRIMARY_OK,
     "the Cycle 755 primary receipt matches the independent character, commutant, and exchange calculations")
bad_overlap = copy.deepcopy(PRIMARY)
bad_overlap.setdefault("character_overlap", {})["seen_blind"] = 20
gate("hostile.primary_overlap", not primary_contract(bad_overlap),
     "a one-unit reversion of the isotypic multiplicity overlap is rejected")
bad_boundary = copy.deepcopy(PRIMARY)
bad_boundary.setdefault("boundary", {})["all_symmetry_or_incidence_routes_to_rank_excluded"] = True
gate("hostile.primary_boundary", not primary_contract(bad_boundary),
     "a reversion from the named character-route result to a universal rank no-go is rejected")
bad_dependency = copy.deepcopy(C754I)
bad_dependency["status"] = "fail"
gate("hostile.cycle754_status", not cycle754_contract(C754, bad_dependency),
     "a failed direct-predecessor helper receipt is rejected")

print("per_element: checked -- all 192 piece coordinates enter the independent exact kernel and orbital checks", flush=True)
print("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only", flush=True)
print("per_mode: checked -- exact character inner products resolve seen/blind irreducible multiplicity overlap", flush=True)
print("per_block: checked -- the blind, seen, orbital-residual, and signed-exchange blocks are reconstructed", flush=True)
print("lattice_wide: checked and not executed -- no multicell, infinite-lattice, causal, or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-isotypic-overlap-cycle755-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {
        "cycle754": {
            "receipt_sha256": sha256(C754_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C754_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C754_OK,
            "live_replay_passed": predecessor.get("failed") == 0,
        },
    },
    "independent_reconstruction": {
        "method": "Cycle754 helper replay; exact characters; ordered-pair orbitals; dual modular ranks; SymPy orbit rank",
        "cuttings": incidence.shape[0],
        "piece_coordinates": n,
        "group_order": len(group),
        "kernel_dimension": k,
    },
    "character_overlap": {
        "seen_seen": seen_seen[0],
        "seen_blind": seen_blind[0],
        "blind_blind": blind_blind[0],
        "endomorphism_dimension": fixed_fixed[0],
    },
    "commutant": {
        "ordered_pair_orbits": orbit_count,
        "residual_rank_prime_1": residual_rank_1,
        "residual_rank_prime_2": residual_rank_2,
        "blind_preserving_dimension": orbit_count - residual_rank_1,
        "individual_orbital_matrices_preserving_blind": len(preserving),
        "largest_nonzero_residual_entry": max(residual_maxima),
    },
    "least_exchange_orbit": {
        "signed_images": len(signed_orbit),
        "span_rank_exact": orbit_rank_exact,
        "span_rank_prime_1": orbit_rank_1,
        "span_rank_prime_2": orbit_rank_2,
        "blind_complement_dimension": k - orbit_rank_exact,
    },
    "boundary": {
        "blind_space_is_group_invariant": True,
        "blind_space_is_sum_of_complete_isotypic_components": False,
        "all_symmetry_or_incidence_routes_to_rank_excluded": False,
        "remaining_44_dimensions_generated": False,
    },
    "no_go_discipline": {
        "status": "PASS",
        "n5_execution_certificate": [
            "per_element checked",
            "per_site checked and not executed",
            "per_mode checked",
            "per_block checked",
            "lattice_wide checked and not executed",
        ],
    },
    "gates": {"pass": passed, "fail": failed, "named": gates},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(0 if failed == 0 else 1)
