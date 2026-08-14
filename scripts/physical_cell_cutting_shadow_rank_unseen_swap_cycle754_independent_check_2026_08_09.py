"""Independent Cycle 754 incidence-shadow and exchange checker.

This checker imports no Cycle 754 primary symbols.  It live-replays the
structurally independent Cycle 753 helper and uses that reconstruction of the
finite incidence object.  New work uses SymPy exact nullspace arithmetic,
fixed modular signatures, direct integer comparisons, and SHA-512 buckets
with exact collision confirmation rather than the primary's elimination,
polynomial-moment, float32, and SHA-256 routes.
"""
import contextlib
import copy
import hashlib
import io
import itertools
import json
import math
import runpy
import sys
from pathlib import Path

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "independent_check_2026_08_09.py"
)
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_"
    "CYCLE754_NOTE_2026-08-09.md"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "2026_08_09_receipt_2026-08-09.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
C753_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_"
    "CYCLE753_NOTE_2026-08-09.md"
)
C753_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09.py"
)
C753_CHECKER_PATH = (
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_"
    "independent_check_2026_08_09.py"
)
C753_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_"
    "2026_08_09_receipt_2026-08-09.json"
)
C753_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py",
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09_receipt_2026-08-09.json",
    "docs/PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_CYCLE753_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09.py",
    "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_shared_count_variance_law_cycle753_independent_check_2026_08_09_receipt_2026-08-09.json",
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
        "schema": "physical-cell-cutting-shadow-rank-cycle754-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


passed = 0
failed = 0
gates = {}


def gate(name, condition, detail):
    global passed, failed
    ok = bool(condition)
    gates[name] = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    else:
        failed += 1
    compact = detail if len(detail) <= 116 else detail[:113] + "..."
    print(("PASS " if ok else "FAIL ") + name + "  " + compact, flush=True)


def cycle753_contract(primary, independent):
    forced = primary.get("forced_mean_identity", {})
    floor = primary.get("parity_floor", {})
    independent_forced = independent.get("forced_mean_identity", {})
    independent_floor = independent.get("parity_floor", {})
    return (
        primary.get("schema")
        == "physical-cell-cutting-shared-count-variance-cycle753-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C753_PRIMARY_PATH)
        and inputs_current(primary)
        and forced.get("induced_q4_count") == 59736
        and forced.get("total_meetings") == 31600
        and floor.get("derived_lower_bound") == 18632
        and floor.get("minimum_carrier_total") == 19640
        and independent.get("schema")
        == "physical-cell-cutting-shared-count-variance-cycle753-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("claim_type") == "bounded_theorem"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C753_CHECKER_PATH)
        and inputs_current(independent)
        and independent_forced.get("total_meetings") == 31600
        and independent_forced.get("identity_failures") == 0
        and independent_floor.get("derived_lower_bound") == 18632
        and independent_floor.get("minimum_carrier_total") == 19640
    )


def primary_contract(receipt):
    shadow = receipt.get("rational_shadow", {})
    exchange = receipt.get("exchange_boundary", {})
    collisions = receipt.get("multiplicity_collisions", {})
    binary = receipt.get("binary_shadow", {})
    localization = receipt.get("localization", {})
    boundary = receipt.get("boundary", {})
    dependency = receipt.get("direct_dependencies", {}).get("cycle753", {})
    return (
        receipt.get("schema") == "physical-cell-cutting-shadow-rank-cycle754-v2"
        and receipt.get("status") == "pass"
        and receipt.get("claim_type") == "bounded_theorem"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and dependency.get("contract_current") is True
        and dependency.get("receipt_sha256") == sha256(C753_RECEIPT_PATH)
        and dependency.get("independent_receipt_sha256")
        == sha256(C753_INDEPENDENT_RECEIPT_PATH)
        and shadow.get("rank") == 88
        and shadow.get("kernel_dimension") == 104
        and shadow.get("every_kernel_basis_vector_balanced") is True
        and shadow.get("reported_basis_is_free_column_rref_basis") is True
        and exchange.get("dependent_pairs") == 0
        and exchange.get("dependent_triples") == 0
        and exchange.get("two_for_two_or_three_for_three_exchanges") == 0
        and exchange.get("four_for_four_witness")
        == {"positive": [4, 5, 10, 11], "negative": [1, 3, 7, 9]}
        and exchange.get("witness_orbit_size") == 96
        and collisions.get("minimum_carriers") == 132
        and collisions.get("carrier_vectors") == 108
        and collisions.get("induced_q4_sets") == 59736
        and collisions.get("induced_q4_vectors") == 53632
        and binary.get("row_rank") == 88
        and binary.get("column_rank") == 88
        and binary.get("named_readings_reached") == 8
        and localization.get("four_reading_parity_floor_from_cycle753") == 18632
        and localization.get("minimum_carrier_total") == 19640
        and boundary.get("two_cover_zero_one_feasibility_decided") is False
        and boundary.get("arbitrary_pairwise_invariants_factor_through_multiplicity_claimed") is False
        and boundary.get("basis_support_histogram_is_basis_invariant_claimed") is False
    )


def rank_mod(matrix, prime):
    """Exact rank over one finite field, using a route unlike rational RREF."""
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
        for lower in range(row + 1, array.shape[0]):
            factor = int(array[lower, column])
            if factor:
                array[lower] = (array[lower] - factor * array[row]) % prime
        row += 1
        if row == array.shape[0]:
            break
    return row


def modular_weights(length, prime, seed):
    values = np.empty(length, dtype=np.int64)
    state = seed
    for index in range(length):
        state = (48271 * state + 12820163) % prime
        values[index] = state
    return values


def exact_exchange_sweep(incidence, size, column_signatures, primes):
    """Necessary modular sift followed by exact comparison of every collision."""
    first = {}
    exact_hits = 0
    signature_ties = 0
    covered = 0
    for choice in itertools.combinations(range(incidence.shape[1]), size):
        signature = tuple(
            sum(int(column_signatures[k][column]) for column in choice) % primes[k]
            for k in range(len(primes))
        )
        previous = first.get(signature)
        if previous is None:
            first[signature] = choice
        else:
            signature_ties += 1
            left = incidence[:, previous].sum(axis=1)
            right = incidence[:, choice].sum(axis=1)
            exact_hits += int(np.array_equal(left, right) and set(previous).isdisjoint(choice))
        covered += 1
    return covered, len(first), signature_ties, exact_hits


def packed_rank(vectors):
    basis = {}
    for vector in vectors:
        value = int.from_bytes(np.packbits(np.asarray(vector, dtype=np.uint8)).tobytes(), "big")
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis), [basis[pivot] for pivot in sorted(basis, reverse=True)]


def reduces_to_zero(vector, basis):
    value = int.from_bytes(np.packbits(np.asarray(vector, dtype=np.uint8)).tobytes(), "big")
    for pivot in basis:
        value = min(value, value ^ pivot)
    return value == 0


write_failure("checker has not completed")
C753 = load(C753_RECEIPT_PATH)
C753I = load(C753_INDEPENDENT_RECEIPT_PATH)
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C753_OK = cycle753_contract(C753, C753I)
gate("independent.cycle753_contract", C753_OK,
     "current Cycle 753 primary and helper bind the complete forced-mean finite-object boundary")

# Live-replay the current predecessor helper without overwriting its canonical receipt.
old_exit = sys.exit
old_write_text = Path.write_text
dependency_receipt = (ROOT / C753_INDEPENDENT_RECEIPT_PATH).resolve()


def guarded_write_text(self, data, *args, **kwargs):
    if self.resolve() == dependency_receipt:
        return len(data)
    return old_write_text(self, data, *args, **kwargs)


sys.exit = lambda _code=0: None
Path.write_text = guarded_write_text
capture = io.StringIO()
try:
    with contextlib.redirect_stdout(capture):
        predecessor = runpy.run_path(str(ROOT / C753_CHECKER_PATH), run_name="__main__")
finally:
    Path.write_text = old_write_text
    sys.exit = old_exit

predecessor_stdout = capture.getvalue()
gate(
    "independent.cycle753_live_replay",
    predecessor.get("failed") == 0
    and "FAIL " not in predecessor_stdout
    and "TOTAL: PASS=13 FAIL=0" in predecessor_stdout,
    "the independent Cycle 753 reconstruction completes live with all thirteen gates",
)

cycle752 = predecessor["predecessor"]
incidence = np.asarray(cycle752["incidence"], dtype=np.int64)
pair_counts = np.asarray(cycle752["pair_counts"], dtype=np.int64)
shapes = sorted(tuple(int(value) for value in shape) for shape in cycle752["shapes"])
carriers = [tuple(sorted(int(value) for value in carrier)) for carrier in cycle752["census"]]
group = [np.asarray(permutation, dtype=np.int64) for permutation in cycle752["group"]]
targets = cycle752["target_vectors"]

row_weights = incidence.sum(axis=1)
column_weights = incidence.sum(axis=0)
gram = incidence.T @ incidence
gate(
    "independent.incidence",
    incidence.shape == (15800, 192)
    and np.all(row_weights == 24)
    and np.all(column_weights == 1975)
    and np.array_equal(np.diag(gram), column_weights),
    "the replayed 15800-by-192 incidence has row weight 24 and column weight 1975",
)

# SymPy's exact nullspace route supplies an upper bound, while two modular
# minors supply independent lower bounds on rational rank.
nullspace = sp.Matrix(gram.tolist()).nullspace()
integer_basis = []
for vector in nullspace:
    denominators = [int(value.q) for value in vector]
    scale = math.lcm(*denominators)
    values = [int(value * scale) for value in vector]
    divisor = math.gcd(*[abs(value) for value in values if value])
    integer_basis.append([value // divisor for value in values])
kernel = np.asarray(integer_basis, dtype=np.int64)
rank_1 = rank_mod(gram, 1000003)
rank_2 = rank_mod(gram, 1000033)
kernel_zero = np.array_equal(incidence @ kernel.T, np.zeros((15800, len(kernel)), dtype=np.int64))
kernel_rank = rank_mod(kernel, 1000003)
balanced = bool(np.all(kernel.sum(axis=1) == 0))
gate(
    "independent.rational_shadow",
    len(nullspace) == 104
    and rank_1 == rank_2 == 88
    and kernel_rank == 104
    and kernel_zero
    and balanced,
    "SymPy gives 104 exact balanced kernel vectors and two modular minors give rank 88",
)

entry_values = sorted(int(value) for value in np.unique(kernel))
supports = np.count_nonzero(kernel, axis=1)
support_values, support_counts = np.unique(supports, return_counts=True)
support_histogram = {int(size): int(count) for size, count in zip(support_values, support_counts)}
gate(
    "independent.free_basis_profile",
    entry_values == [-1, 0, 1]
    and support_histogram == {8: 38, 12: 30, 14: 14, 16: 13, 18: 3, 20: 6},
    "the independent exact free-column basis reproduces the reported basis-dependent support profile",
)

primes = (1000003, 1000033, 1000037)
column_signatures = []
for index, prime in enumerate(primes):
    weights = modular_weights(incidence.shape[0], prime, 754 + 31 * index)
    column_signatures.append((weights @ incidence) % prime)
pair_sweep = exact_exchange_sweep(incidence, 2, column_signatures, primes)
triple_sweep = exact_exchange_sweep(incidence, 3, column_signatures, primes)
gate(
    "independent.small_exchanges",
    pair_sweep[0] == math.comb(192, 2)
    and triple_sweep[0] == math.comb(192, 3)
    and pair_sweep[3] == triple_sweep[3] == 0,
    "fixed modular signatures cover every pair and triple; exact checks find no 2-for-2 or 3-for-3 exchange",
)

positive = [4, 5, 10, 11]
negative = [1, 3, 7, 9]
witness_gap = int(np.abs(
    incidence[:, positive].sum(axis=1) - incidence[:, negative].sum(axis=1)
).max())
witness_orbit = set()
for permutation in group:
    left = tuple(sorted(int(permutation[value]) for value in positive))
    right = tuple(sorted(int(permutation[value]) for value in negative))
    witness_orbit.add((left, right) if left < right else (right, left))
gram_fixed = all(np.array_equal(gram[np.ix_(permutation, permutation)], gram)
                 for permutation in group)
gate(
    "independent.four_exchange",
    witness_gap == 0 and len(group) == 384 and len(witness_orbit) == 96 and gram_fixed,
    "the direct four-for-four witness is exact, has orbit 96, and all 384 symmetries preserve the Gram table",
)

carrier_groups = {}
carrier_vectors = []
for index, carrier in enumerate(carriers):
    vector = incidence[:, carrier].sum(axis=1).astype(np.int8)
    carrier_vectors.append(vector)
    carrier_groups.setdefault(vector.tobytes(), []).append(index)
collision_groups = [indices for indices in carrier_groups.values() if len(indices) > 1]
collision_pairs_disjoint = all(
    len(indices) == 2 and set(carriers[indices[0]]).isdisjoint(carriers[indices[1]])
    for indices in collision_groups
)
gate(
    "independent.carrier_collisions",
    len(carriers) == 132
    and len(carrier_groups) == 108
    and len(collision_groups) == 24
    and collision_pairs_disjoint,
    "the 132 minimum carriers give 108 exact vectors and 24 disjoint colliding pairs",
)

# Count exact Q4 multiplicity vectors.  SHA-512 is only a bucket key: every
# repeated digest is confirmed against a recomputed representative vector, so
# a digest collision cannot change the count.
shape_index = np.asarray(shapes, dtype=np.int64)
digest_buckets = {}
distinct_shape_vectors = 0
digest_collisions_checked = 0
batch_size = 500
incidence16 = incidence.astype(np.int16)
for lower in range(0, len(shapes), batch_size):
    upper = min(lower + batch_size, len(shapes))
    selected = shape_index[lower:upper]
    indicator = np.zeros((192, len(selected)), dtype=np.int16)
    indicator[selected.ravel(), np.repeat(np.arange(len(selected)), 16)] = 1
    multiplicities = (incidence16 @ indicator).T.astype(np.int8)
    for local, vector in enumerate(multiplicities):
        shape_number = lower + local
        digest = hashlib.sha512(vector.tobytes()).digest()
        representatives = digest_buckets.get(digest)
        if representatives is None:
            digest_buckets[digest] = [shape_number]
            distinct_shape_vectors += 1
            continue
        matched = False
        for representative in representatives:
            candidate = incidence[:, shape_index[representative]].sum(axis=1).astype(np.int8)
            digest_collisions_checked += 1
            if np.array_equal(vector, candidate):
                matched = True
                break
        if not matched:
            representatives.append(shape_number)
            distinct_shape_vectors += 1
gate(
    "independent.q4_collisions",
    len(shapes) == 59736
    and distinct_shape_vectors == 53632
    and digest_collisions_checked >= len(shapes) - distinct_shape_vectors,
    "all 59736 Q4 shapes give 53632 vectors; every repeated SHA-512 bucket is checked exactly",
)

column_rank, column_basis = packed_rank(incidence.T)
row_rank, _row_basis = packed_rank(incidence)
named_reached = sum(reduces_to_zero(np.asarray(vector, dtype=np.uint8), column_basis)
                    for vector in targets.values())
gate(
    "independent.binary_shadow",
    column_rank == row_rank == 88
    and 192 - column_rank == 104
    and named_reached == len(targets) == 8,
    "independent packed elimination gives GF(2) row/column rank 88 and reaches all eight readings",
)

carrier_totals = []
local_identity_failures = 0
route_failures = 0
at_baseline = 0
for carrier, multiplicity in zip(carriers, carrier_vectors):
    indices = np.asarray(carrier, dtype=np.int64)
    total = int(pair_counts[np.ix_(indices, indices)].sum() // 2)
    local_pair = pair_counts[np.ix_(indices, indices)].sum(axis=1) - 1975
    local_incidence = np.asarray([
        int(multiplicity[incidence[:, piece] == 1].sum()) - 2 * 1975
        for piece in carrier
    ], dtype=np.int64)
    carrier_totals.append(total)
    local_identity_failures += int(int(local_pair.sum()) != 2 * (total - 15800))
    route_failures += int(not np.array_equal(local_pair, local_incidence))
    at_baseline += int(np.all(local_pair == 0))
gate(
    "independent.localization",
    len(carrier_totals) == 132
    and local_identity_failures == 0
    and route_failures == 0
    and at_baseline == 0
    and min(carrier_totals) == 19640,
    "both local routes agree on all 132 carriers; none reaches baseline and the minimum is 19640",
)

PRIMARY_OK = primary_contract(PRIMARY)
gate("independent.primary_contract", C753_OK and PRIMARY_OK,
     "the Cycle 754 primary receipt matches the independent shadow and collision reconstruction")
bad_primary = copy.deepcopy(PRIMARY)
bad_primary.setdefault("rational_shadow", {})["rank"] = 87
gate("hostile.primary_rank", not primary_contract(bad_primary),
     "a one-unit reversion of the primary rational rank is rejected")
bad_boundary = copy.deepcopy(PRIMARY)
bad_boundary.setdefault("boundary", {})["two_cover_zero_one_feasibility_decided"] = True
gate("hostile.primary_boundary", not primary_contract(bad_boundary),
     "a reversion that turns rank-route failure into a two-cover verdict is rejected")
bad_cycle753 = copy.deepcopy(C753I)
bad_cycle753["status"] = "fail"
gate("hostile.cycle753_status", not cycle753_contract(C753, bad_cycle753),
     "a failed direct predecessor certificate is rejected")

print("per_element: checked -- all 192 piece columns enter the independent exact shadow checks", flush=True)
print("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- this finite binary incidence object has no modal decomposition", flush=True)
print("per_block: checked -- all 15800 cutting rows enter the independent rank and collision reconstruction", flush=True)
print("lattice_wide: checked and not executed -- no multicell, infinite-lattice, causal, or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-shadow-rank-cycle754-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {
        "cycle753": {
            "receipt_sha256": sha256(C753_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C753_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C753_OK,
            "live_replay_passed": predecessor.get("failed") == 0,
        },
    },
    "independent_reconstruction": {
        "cuttings": incidence.shape[0],
        "support_columns": incidence.shape[1],
        "induced_q4_sets": len(shapes),
        "minimum_carriers": len(carriers),
        "method": "Cycle753 helper replay; SymPy nullspace; modular signatures; exact SHA-512 buckets",
    },
    "rational_shadow": {
        "rank": rank_1,
        "second_modular_rank": rank_2,
        "kernel_dimension": len(nullspace),
        "kernel_rank": kernel_rank,
        "kernel_exact_zero": kernel_zero,
        "every_kernel_basis_vector_balanced": balanced,
        "basis_entry_values": entry_values,
        "basis_support_histogram": {str(key): value for key, value in support_histogram.items()},
    },
    "exchange_boundary": {
        "pair_subsets_checked": pair_sweep[0],
        "triple_subsets_checked": triple_sweep[0],
        "pair_exact_exchanges": pair_sweep[3],
        "triple_exact_exchanges": triple_sweep[3],
        "four_for_four_witness": {"positive": positive, "negative": negative},
        "witness_exact_max_gap": witness_gap,
        "witness_orbit_size": len(witness_orbit),
    },
    "multiplicity_collisions": {
        "minimum_carriers": len(carriers),
        "carrier_vectors": len(carrier_groups),
        "carrier_collision_pairs": len(collision_groups),
        "carrier_collisions_disjoint": collision_pairs_disjoint,
        "induced_q4_sets": len(shapes),
        "induced_q4_vectors": distinct_shape_vectors,
        "digest_collisions_checked_exactly": digest_collisions_checked,
    },
    "binary_shadow": {
        "row_rank": row_rank,
        "column_rank": column_rank,
        "kernel_dimension": 192 - column_rank,
        "named_readings_reached": named_reached,
        "named_readings_total": len(targets),
    },
    "localization": {
        "universal_sixteen_set_baseline": 15800,
        "four_reading_parity_floor_from_cycle753": 18632,
        "minimum_carrier_total": min(carrier_totals),
        "minimum_carriers_checked": len(carrier_totals),
        "local_sum_identity_failures": local_identity_failures,
        "route_failures": route_failures,
        "carriers_at_universal_baseline": at_baseline,
    },
    "no_go_discipline": {
        "status": "PASS",
        "n5_execution_certificate": [
            "per_element checked",
            "per_site checked and not executed",
            "per_mode checked and not executed",
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
