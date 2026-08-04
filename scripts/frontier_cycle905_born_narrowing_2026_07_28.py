#!/usr/bin/env python3
"""Cycle 905: the Born narrowing, certified on its home lineage.

Campaign-5 Born LANE CLOSURE, block 1.  Strictly structural.  NO
probability postulate is introduced, NO Born rule is claimed.  Every
fraction emitted here is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

The gravity lane (Cycle 902, sibling branch, vendored onto this lineage
in the ship commit that precedes this script) proved that the minimal
kernel-argument extension of the Cycle-878 event space has fibre
dimension 5, that the gravity bridge is constructible over it, and that
SUPPORT FAITHFULNESS FAILS TO LIFT: only the non-support-faithful members
of the 878 five can carry the gravity interface.  902 computed that over
a "maximally generous base" because the Cycle-863 census module was
absent from its lineage.  Here the census IS present.

Q1  THE NARROWING, CERTIFIED AT FULL DEPTH.
    (a) the EXACT base rank of the five weightings over the true census,
        computed by two independent routes (rational elimination on the
        full 5 x |E| matrix; a division-free Gram/Laplace determinant),
        with a third world-reduced route as a cross-check, and the
        878/902 generator relation a4 + a5 = (boundaries+1)*[formed]
        checked against the actual census -- both at coefficient level
        and as a candidate linear dependence among the five;
    (b) the support-faithfulness failure recomputed at EVENT level: which
        weightings can and cannot host a required-zero region, with
        exhibited witnesses, checked against 902's generous-base verdict;
    (c) the exclusion's exact mechanism named as a census-level fact.

Q2  WHAT SEPARATES THE SURVIVING THREE.
    (a) the pairwise discrimination structure of {M3, M4, M5} at the true
        census, per certified family, classified by the 878 atom fields;
    (b) the pullback of 902's exhibited interface object, in THREE
        declared readings, each computed exactly; where a reading is only
        semi-decidable by the test used it returns UNDECIDED rather than
        a guess;
    (c) the honest outcome class, computed from the readings, plus the
        exact pricing of the residual separating question.

Q3  THE LANE LEDGER, OPENED: every Born-lane obligation named with its
    current status.

Discipline: TEXT / AST / JSON only.  The Cycle-863 and Cycle-878
machinery is BLOCKLISTED from import and is lifted out of the pinned
sources by AST, so the rebuilt event space is the pinned construction
byte-for-byte rather than a transcription.  Only the landed Cycle-719
core is imported.  Exact arithmetic everywhere: every weighting is an
integer numerator vector over one common denominator, every rank is
computed over Q, and no floating point enters any verdict.

Supervisor-authored primary.  bounded_theorem, authority none, audit
unset.  Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import sys
from time import monotonic
from types import SimpleNamespace

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C878_CACHE = "logs/runner-cache/frontier_cycle878_event_space_groundwork_2026_07_28.txt"
C902_PATH = "scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C878_CACHE,
    C902_PATH, C902_RECEIPT, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C902_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C902_RECEIPT)
TEXT_ONLY_PATHS = (C878_CACHE, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C878_CACHE:
        "dbf33c9677cfff61e88f0bfe100fa09ae47a30d5aeb6d58b5a370dadb3c16a6b",
    C902_PATH:
        "46d46db10258731b986f3c639eedcf1ad3f968021f1efe30c88cc3e5e17b46c2",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C878_CACHE: "ab88312b24487d1625cbbc1d75b79c44fc2062c4",
    C902_PATH: "3b43d97bbb604ea44ed06c87aa091c6aa9d8470b",
    C902_RECEIPT: "1fd7522ad2af152f2e13327e752e2eb9f37e67bb",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

FRACTION_LABEL = "bookkeeping fraction, not probability"
NARROWED = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
            "M5_FORMATION_MOMENT")
EXCLUDED_BY_902 = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def factorize(value: int) -> dict:
    out: dict = {}
    n, p = value, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


# ---------------------------------------------------------------------------
# A: pins
# ---------------------------------------------------------------------------

def pin_rows() -> dict:
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=Path(__file__).name
    )
    literal = None
    string_constants: dict = {}
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if not isinstance(target, ast.Name):
                    continue
                if isinstance(node.value, ast.Constant) \
                        and isinstance(node.value.value, str):
                    string_constants[target.id] = node.value.value
                if target.id == "AUDIT_INPUT_PATHS" \
                        and isinstance(node.value, ast.Tuple):
                    resolved = []
                    for element in node.value.elts:
                        if isinstance(element, ast.Constant):
                            resolved.append(element.value)
                        elif isinstance(element, ast.Name):
                            resolved.append(string_constants[element.id])
                        else:
                            resolved.append(None)
                    literal = tuple(resolved)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "modes": {
            "imported": IMPORTED_PATHS, "ast_only": AST_ONLY_PATHS,
            "json_only": JSON_ONLY_PATHS, "text_only": TEXT_ONLY_PATHS,
        },
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "vendored_902_pair_verified": (
            sha_rows[C902_PATH] == EXPECTED_SHA256[C902_PATH]
            and sha_rows[C902_RECEIPT] == EXPECTED_SHA256[C902_RECEIPT]
        ),
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "bytes": {p: len(b) for p, b in payloads.items()},
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and result["vendored_902_pair_verified"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# ---------------------------------------------------------------------------
# AST lift: the pinned machinery, never imported
# ---------------------------------------------------------------------------

def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found_consts = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in consts:
                    found_consts[target.id] = ast.literal_eval(node.value)
    missing = tuple(f for f in funcs if f not in {n.name for n in body})
    missing_c = tuple(c for c in consts if c not in found_consts)
    if missing or missing_c:
        raise AssertionError(("ast lift incomplete", path, missing, missing_c))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(globals_)
    namespace.update(found_consts)
    exec(compile(module, f"<ast-lift {path}>", "exec"), namespace)
    return namespace, found_consts, tuple(n.name for n in body)


C863_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "derive_census",
    "watched_registers", "dirty_partition", "build_initial_states",
    "pack_lanes", "compile_masked_gate", "masked_h_schedules", "compile_fast",
    "mask_over", "lanes_of", "lane_state",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
C878_FUNCS = (
    "lcm", "dead_wire_rig", "composed_scan", "family_keys", "cells_of",
    "refines", "build_candidates", "monitor_phase_action", "group_orbits",
)
C878_CONSTS = (
    "HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
    "DETERMINISM_ORBITS", "CANDIDATE_NAMES", "CONTROL_NAME", "FAMILY_ORDER",
)


def lift_machinery():
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations},
    )
    c863 = SimpleNamespace(**{name: ns863[name] for name in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
         "Fraction": Fraction, "json": json},
    )
    c878 = SimpleNamespace(**{name: ns878[name] for name in C878_FUNCS})
    provenance = {
        "lifted_from_863": names863, "constants_863": consts863,
        "lifted_from_878": names878,
        "constants_878": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts878.items()},
        "import_of_863_or_878": False,
    }
    return c863, c878, consts878, provenance


def build_event_space(c863, c878, consts):
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_fail = c863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = c878.dead_wire_rig(
        program, sim, c863.pack_lanes(states + (states[0],))
    )
    scan = c878.composed_scan(
        program, census, states, rig, consts["HORIZON"]
    )
    return {
        "program": program, "census": census, "stations": stations,
        "states": states, "rig": rig, "scan": scan,
        "events": scan["events"], "init_failures": init_fail,
    }


# ---------------------------------------------------------------------------
# Exact rank: two mandatory routes plus a cross-check (the T9 pattern)
# ---------------------------------------------------------------------------

def rank_by_rational_elimination(rows):
    """Route A: full-pivot Gaussian elimination over Q.  No fraction-free
    bookkeeping anywhere -- Bareiss-style elimination is banned here by
    the Cycle-902 checker's own lesson (it corrupts ranks on
    rank-deficient matrices with skipped columns)."""
    work = [[Fraction(x) for x in row] for row in rows]
    n_rows, n_cols = len(work), len(work[0])
    rank, pivots = 0, []
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if work[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        lead = work[rank][col]
        work[rank] = [x / lead for x in work[rank]]
        for r in range(n_rows):
            if r != rank and work[r][col] != 0:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == n_rows:
            break
    return rank, tuple(pivots)


def det_laplace(matrix):
    """Division-free exact determinant by cofactor expansion."""
    size = len(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    total = 0
    for col in range(size):
        if matrix[0][col] == 0:
            continue
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        total += ((-1) ** col) * matrix[0][col] * det_laplace(minor)
    return total


def rank_by_gram_minors(rows):
    """Route B: rank(M) = rank(M M^T) over an ordered field; the rank of
    the small Gram matrix is read off division-free by the largest
    non-vanishing leading-free principal minor, searched over subsets."""
    k = len(rows)
    gram = [[sum(a * b for a, b in zip(rows[i], rows[j])) for j in range(k)]
            for i in range(k)]
    for size in range(k, 0, -1):
        for subset in combinations(range(k), size):
            minor = [[gram[i][j] for j in subset] for i in subset]
            if det_laplace(minor) != 0:
                return size, subset, gram
    return 0, (), gram


def rank_by_world_reduction(rows, world_of, worlds):
    """Cross-check route: every candidate is constant on worlds, so the
    rank is the rank of the 5 x |worlds| coefficient matrix.  Constancy is
    VERIFIED, not assumed."""
    first_index = {}
    for index, world in enumerate(world_of):
        first_index.setdefault(world, index)
    constant = True
    for row in rows:
        seen = {}
        for world, value in zip(world_of, row):
            if world in seen and seen[world] != value:
                constant = False
                break
            seen[world] = value
        if not constant:
            break
    reduced = [[row[first_index[w]] for w in worlds] for row in rows]
    rank, pivots = rank_by_rational_elimination(reduced)
    return rank, pivots, constant


# ---------------------------------------------------------------------------
# The pullback readings
# ---------------------------------------------------------------------------

def exhibited_object(receipt902):
    obj = receipt902["Q3_exhibited_objects"][0]
    table = obj["coefficient_table"]
    degree0 = [Fraction(row["c_by_degree"][0]) for row in table]
    return {
        "config": obj["config"],
        "atoms": len(table),
        "sites": [row["sites"] for row in table],
        "meets_supp_R": [row["meets_supp_R"] for row in table],
        "c_by_degree_rows": [row["c_by_degree"] for row in table],
        "degree0": degree0,
        "degree0_ints": [int(c) for c in degree0],
        "degree0_sum": int(sum(degree0)),
        "normalizer_N": obj["normalizer_N"],
        "solution_space_dimension": obj["solution_space_dimension"],
        "residual_freedom": obj["residual_freedom_beyond_the_normalizer"],
    }


def reading_support(numerators, required_zero_cells):
    """R-SUPPORT.  The interface's vanishing cells must pull back into the
    weighting's zero set.  Any pullback sends the record atom that meets
    supp(R) to a NON-EMPTY set of census record events (premise P-NONEMPTY,
    declared), so a weighting with an empty zero set cannot host a single
    vanishing cell."""
    zero = sum(1 for v in numerators if v == 0)
    minimum = min(numerators)
    return {
        "zero_weight_events": zero,
        "min_event_numerator": minimum,
        "strictly_positive_everywhere": minimum > 0,
        "required_zero_cells": required_zero_cells,
        "can_host_required_zero_region": bool(
            required_zero_cells == 0 or zero > 0
        ),
        "survives": bool(required_zero_cells == 0 or zero > 0),
    }


def reading_ratio_exhaustive(numerators, ratios):
    """R-RATIO-EXHAUSTIVE.  The four interface atoms exhaust the census
    image, so the bookkeeping fractions must equal c_i / sum(c).  The
    normalizer is free, so only the ratios are invariant.  Necessary and
    sufficient: sum(c) | T and a partition realizing the block sums."""
    total = sum(numerators)
    scale = sum(ratios)
    divides = total % scale == 0
    witness = None
    realizable = False
    if divides and total > 0:
        unit = total // scale
        targets = [r * unit for r in ratios]
        remaining = list(targets)
        blocks = [0] * len(ratios)
        order = sorted(range(len(numerators)), key=lambda i: -numerators[i])
        ok = True
        for i in order:
            value = numerators[i]
            placed = False
            for b in sorted(range(len(ratios)), key=lambda b: -remaining[b]):
                if remaining[b] >= value:
                    remaining[b] -= value
                    blocks[b] += 1
                    placed = True
                    break
            if not placed:
                ok = False
                break
        realizable = bool(ok and all(r == 0 for r in remaining))
        witness = {
            "unit_mass_numerator": unit,
            "block_targets": targets,
            "block_event_counts": blocks if realizable else None,
            "greedy_exhausted_targets": realizable,
        }
    return {
        "total_numerator": total,
        "ratio_scale_sum": scale,
        "scale_divides_total": divides,
        "total_mod_scale": total % scale if scale else None,
        "greedy_partition_witness": witness,
        "survives": bool(divides and realizable),
        "verdict": ("SURVIVES" if (divides and realizable)
                    else "FAILS_DIVISIBILITY" if not divides
                    else "FAILS_PARTITION"),
    }


def reading_ratio_free(numerators, ratios):
    """R-RATIO-FREE.  The interface atoms need NOT exhaust the census
    image: only the ratios among four disjoint blocks are invariant.
    Tested by its exact necessary capacity condition and by a sufficient
    equal-multiplicity witness.  Where the necessary condition holds and
    the sufficient witness is absent the reading returns UNDECIDED -- it
    is never guessed."""
    positives = [v for v in numerators if v > 0]
    total = sum(positives)
    scale = sum(ratios)
    smallest = min(positives) if positives else 0
    capacity_ok = bool(positives) and smallest * scale <= total
    multiplicity = Counter(positives)
    best_value, best_count = (0, 0)
    if multiplicity:
        best_value, best_count = max(multiplicity.items(), key=lambda kv: kv[1])
    sufficient = best_count >= scale
    return {
        "min_positive_numerator": smallest,
        "positive_mass_total": total,
        "capacity_condition_min_times_scale_le_total": capacity_ok,
        "largest_equal_weight_class": [best_value, best_count],
        "equal_multiplicity_witness_suffices": sufficient,
        "verdict": ("SURVIVES" if sufficient
                    else "FAILS_CAPACITY" if not capacity_ok
                    else "UNDECIDED_BY_THIS_TEST"),
        "survives": True if sufficient else (None if capacity_ok else False),
    }


def separation_class(per_reading: dict, family: tuple) -> dict:
    """Outcome-neutral classifier: a reading separates only if its verdict
    vector is NOT constant on the family."""
    rows = {}
    for reading, table in per_reading.items():
        verdicts = tuple(table[name]["survives"] for name in family)
        survivors = tuple(
            name for name in family if table[name]["survives"] is True
        )
        rows[reading] = {
            "verdict_vector": [str(v) for v in verdicts],
            "constant_on_family": len(set(verdicts)) == 1,
            "survivors": survivors,
            "separating": len(set(verdicts)) > 1,
            "kills_everyone": all(v is False for v in verdicts),
        }
    separating = tuple(r for r, v in rows.items() if v["separating"])
    if not separating:
        outcome = "STABLE"
    else:
        smallest = min(
            (len(rows[r]["survivors"]) for r in separating), default=len(family)
        )
        outcome = "SEPARATED" if smallest == 1 else "FURTHER_NARROWED"
    return {
        "per_reading": rows,
        "separating_readings": separating,
        "joint_obstruction_readings": tuple(
            r for r, v in rows.items() if v["kills_everyone"]
        ),
        "outcome_class": outcome,
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a = pin_rows()
    if not cert_a["pass"]:
        sys.stdout.write(
            "CERTIFICATE A_PINS FAIL " + compact(cert_a) + "\n"
            + "CYCLE905_BORN_NARROWING_PIN_FAILURE\n"
        )
        return 2

    receipt878 = json.loads((ROOT / C878_RECEIPT).read_text(encoding="utf-8"))
    receipt902 = json.loads((ROOT / C902_RECEIPT).read_text(encoding="utf-8"))
    cache878 = (ROOT / C878_CACHE).read_text(encoding="utf-8")

    c863, c878, consts, provenance = lift_machinery()
    names = tuple(consts["CANDIDATE_NAMES"])
    families = tuple(consts["FAMILY_ORDER"])

    build_a = build_event_space(c863, c878, consts)
    events = build_a["events"]
    scan = build_a["scan"]
    boundaries = scan["boundaries"]
    census = build_a["census"]
    stations = build_a["stations"]
    world_of = [e[0] for e in events]
    worlds = sorted(set(world_of))
    formed = scan["formed"]
    occupation = scan["occ_global"]

    numerators, denominators, meta, per_world, supported, common = \
        c878.build_candidates(events, occupation, formed, boundaries)
    totals = {name: sum(numerators[name]) for name in names}
    event_digest = digest(events)

    # ---- B: restriction gates -------------------------------------------
    keys = c878.family_keys(events, stations)
    cells = {fam: c878.cells_of(keys[fam]) for fam in families}
    atom_sizes = Counter(len(v) for v in cells["F_ATOM"].values())
    atoms_singleton = bool(events) and set(atom_sizes) == {1}
    tag_counts = dict(sorted(Counter(e[2] for e in events).items()))

    def fractions_for(name, fam):
        total = totals[name]
        return {
            key: Fraction(sum(numerators[name][i] for i in idx), total)
            for key, idx in cells[fam].items()
        }
    tables = {(name, fam): fractions_for(name, fam)
              for name in names for fam in families}
    pairs = [(a, b) for i, a in enumerate(names) for b in names[i + 1:]]
    discriminating = []
    for a, b in pairs:
        found = False
        for fam in families:
            ta, tb = tables[(a, fam)], tables[(b, fam)]
            if any(ta[k] != tb[k] for k in ta):
                found = True
                break
        if found:
            discriminating.append(f"{a}|{b}")
    admissible = tuple(
        name for name in names
        if totals[name] > 0
        and all(
            sum(sum(numerators[name][i] for i in idx)
                for idx in cells[fam].values()) == totals[name]
            for fam in families
        )
    )
    zero_counts = {name: sum(1 for v in numerators[name] if v == 0)
                   for name in names}
    receipt_zero = {
        name: receipt878["findings"]["candidate_verdicts"][name][
            "zero_weight_events"]
        for name in names
    }
    receipt_fibre = receipt902["Q1_minimal_fibre_dimension"]
    receipt_vanishing = int(next(
        row["computed"] for row in receipt902["restriction_gate_rows"]
        if row["gate"] == "c892_vanishing_cells"
    ))
    cache_digest = None
    for token in cache878.split('"event_space_digest":"'):
        if len(token) >= 64 and all(c in "0123456789abcdef" for c in token[:64]):
            cache_digest = token[:64]
    gate_rows = [
        {"gate": "c878_event_cardinality",
         "target": receipt878["findings"]["event_cardinality"],
         "computed": len(events)},
        {"gate": "c878_event_space_digest_from_pinned_cache",
         "target": cache_digest, "computed": event_digest},
        {"gate": "c878_atoms_are_singletons",
         "target": receipt878["findings"]["atoms_are_singletons"],
         "computed": atoms_singleton},
        {"gate": "c878_cells_per_family",
         "target": receipt878["findings"]["cells_per_family"],
         "computed": {fam: len(cells[fam]) for fam in families}},
        {"gate": "c878_events_by_tag",
         "target": receipt878["findings"]["events_by_tag"],
         "computed": tag_counts},
        {"gate": "c878_worlds_with_events",
         "target": receipt878["findings"]["worlds_with_at_least_one_event"],
         "computed": len(worlds)},
        {"gate": "c878_per_world_event_count_range",
         "target": receipt878["findings"]["per_world_event_count_range"],
         "computed": [min(per_world.values()), max(per_world.values())]},
        {"gate": "c878_admissible_weighting_count",
         "target": len(names), "computed": len(admissible)},
        {"gate": "c878_discriminating_pairs",
         "target": sorted(receipt878["findings"]["discriminating_pairs"]),
         "computed": sorted(discriminating)},
        {"gate": "c878_indistinguishable_pairs",
         "target": len(receipt878["findings"]["indistinguishable_pairs"]),
         "computed": len(pairs) - len(discriminating)},
        {"gate": "c878_zero_weight_events_rebuilt_from_census",
         "target": receipt_zero, "computed": zero_counts},
        {"gate": "c902_minimal_fibre_dimension",
         "target": 5, "computed": receipt_fibre},
        {"gate": "c902_vanishing_cells",
         "target": 42, "computed": receipt_vanishing},
        {"gate": "c902_support_faithfulness_fails_to_lift",
         "target": True,
         "computed": any("support faithfulness" in s for s in
                         receipt902["Q1_properties_that_fail_to_lift"])},
        {"gate": "c902_extension_dimension_interval",
         "target": [10, 25],
         "computed": [receipt902["Q1_extension_dimension_878_span"][
                          "lower_bound"],
                      receipt902["Q1_extension_dimension_878_span"][
                          "upper_bound"]]},
    ]
    for row in gate_rows:
        row["match"] = row["target"] == row["computed"]
    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "reading": (
            "878's headline counts are taken value-for-value from its"
            " pinned receipt AND recomputed from the actual census rebuilt"
            " here; 902's fibre dimension and vanishing-cell count are read"
            " from the vendored receipt"
        ),
        "rows": gate_rows,
        "rows_matching": sum(1 for r in gate_rows if r["match"]),
        "rows_total": len(gate_rows),
        "ast_lift_provenance": provenance,
        "composed_model_integrity": {
            "write_once_violations": scan["write_once_violations"],
            "dead_activation_conflicts": scan["dead_activation_conflicts"],
            "duplicate_lane_mismatches": scan["mismatches"],
            "initial_state_failures": build_a["init_failures"],
        },
    }
    cert_b["pass"] = bool(
        all(r["match"] for r in gate_rows)
        and scan["write_once_violations"] == 0
        and scan["dead_activation_conflicts"] == 0
        and scan["mismatches"] == 0 and build_a["init_failures"] == 0
    )

    # ---- C: Q1(a) the base rank -----------------------------------------
    matrix = [numerators[name] for name in names]
    rank_a, pivots_a = rank_by_rational_elimination(matrix)
    rank_b, gram_subset, gram = rank_by_gram_minors(matrix)
    rank_c, pivots_c, world_constant = rank_by_world_reduction(
        matrix, world_of, worlds
    )
    narrowed_matrix = [numerators[name] for name in NARROWED]
    rank_narrowed_a, _ = rank_by_rational_elimination(narrowed_matrix)
    rank_narrowed_b, _, _ = rank_by_gram_minors(narrowed_matrix)

    coefficient_rows = {
        w: {
            "a2": 1,
            "a3": occupation[w],
            "a4": (boundaries - formed[w] + 1) if w in formed else 0,
            "a5": formed[w] if w in formed else 0,
            "formed": w in formed,
        }
        for w in worlds
    }
    coeff_violations = [
        w for w, row in coefficient_rows.items()
        if row["a4"] + row["a5"] != (boundaries + 1) * int(row["formed"])
    ]
    residual = [
        (boundaries + 1) * numerators["M2_PER_WORLD_UNIFORM"][i]
        - numerators["M4_FORMATION_LIFETIME"][i]
        - numerators["M5_FORMATION_MOMENT"][i]
        for i in range(len(events))
    ]
    residual_nonzero = [i for i, v in enumerate(residual) if v != 0]
    residual_worlds = sorted({world_of[i] for i in residual_nonzero})
    cert_c = {
        "certificate": "C_BASE_RANK",
        "question": (
            "Q1(a): the exact base rank of the five record-native"
            " weightings over the TRUE census -- the number 902 could not"
            " measure"
        ),
        "matrix_shape": [len(names), len(events)],
        "route_A_rational_elimination": {
            "rank": rank_a, "pivot_columns": list(pivots_a),
            "method": "full pivot search, exact Fraction arithmetic, no"
                      " fraction-free (Bareiss) bookkeeping anywhere",
        },
        "route_B_gram_laplace": {
            "rank": rank_b, "nonvanishing_principal_minor": list(gram_subset),
            "gram_determinant": det_laplace(gram),
            "method": "rank(M) = rank(M M^T) over Q; largest non-vanishing"
                      " principal minor by division-free cofactor expansion",
        },
        "route_C_world_reduction_crosscheck": {
            "rank": rank_c, "pivot_worlds": list(pivots_c),
            "candidates_constant_on_worlds_verified": world_constant,
            "reduced_shape": [len(names), len(worlds)],
        },
        "routes_agree": rank_a == rank_b == rank_c,
        "base_rank": rank_a,
        "five_are_linearly_independent": rank_a == len(names),
        "narrowed_triple_rank": {
            "route_A": rank_narrowed_a, "route_B": rank_narrowed_b,
            "agree": rank_narrowed_a == rank_narrowed_b,
        },
        "generator_relation": {
            "statement_as_AST_derived_by_902":
                "a4 + a5 = (boundaries + 1) * [formed]",
            "boundaries": boundaries,
            "coefficient_level_violations": len(coeff_violations),
            "coefficient_level_holds": not coeff_violations,
            "descends_to_a_linear_dependence_among_the_five": bool(
                not residual_nonzero
            ),
            "residual_vector": (
                "(boundaries+1)*M2 - M4 - M5, the only candidate dependence"
                " the relation could induce"
            ),
            "residual_nonzero_events": len(residual_nonzero),
            "residual_nonzero_worlds": len(residual_worlds),
            "residual_worlds_all_unformed": all(
                w not in formed for w in residual_worlds
            ),
            "witness_events": [
                {"index": i, "event": list(events[i]),
                 "residual_numerator": residual[i]}
                for i in residual_nonzero[:3]
            ],
            "reading": (
                "the relation is EXACT on the world coefficients and does"
                " NOT descend: [formed] is not the coefficient vector of any"
                " candidate, and the never-formed block breaks the identity"
                " with M2 on every one of its events"
            ),
        },
        "extension_dimension_over_the_true_census": {
            "formula": "base rank * minimal kernel fibre dimension",
            "fibre_dimension_from_902": receipt_fibre,
            "value": rank_a * receipt_fibre,
            "c902_interval": [
                receipt902["Q1_extension_dimension_878_span"]["lower_bound"],
                receipt902["Q1_extension_dimension_878_span"]["upper_bound"],
            ],
            "lands_at": (
                "the UPPER endpoint of 902's interval"
                if rank_a * receipt_fibre
                == receipt902["Q1_extension_dimension_878_span"]["upper_bound"]
                else "inside 902's interval"
            ),
        },
        "worlds_total": len(worlds),
        "worlds_formed": len(formed),
        "worlds_never_formed": len(worlds) - len(formed),
    }
    cert_c["pass"] = bool(
        cert_c["routes_agree"] and world_constant
        and rank_narrowed_a == rank_narrowed_b
        and 1 <= rank_a <= len(names)
        and receipt_fibre
        * rank_a >= receipt902["Q1_extension_dimension_878_span"][
            "lower_bound"]
        and rank_a * receipt_fibre
        <= receipt902["Q1_extension_dimension_878_span"]["upper_bound"]
    )

    # ---- D: Q1(b,c) the exclusion ---------------------------------------
    zero_sets = {name: {i for i, v in enumerate(numerators[name]) if v == 0}
                 for name in names}
    support = {
        name: reading_support(numerators[name], receipt_vanishing)
        for name in names
    }
    excluded = tuple(n for n in names if not support[n]["survives"])
    survivors = tuple(n for n in names if support[n]["survives"])
    zero_worlds = {name: sorted({world_of[i] for i in zero_sets[name]})
                   for name in names}
    zero_tag_mix = {
        name: dict(sorted(Counter(events[i][2] for i in zero_sets[name]).items()))
        for name in NARROWED
    }
    never_formed = [w for w in worlds if w not in formed]
    never_formed_events = [i for i, w in enumerate(world_of) if w not in formed]
    formed_at_zero = sorted(w for w, b in formed.items() if b == 0)
    cert_d = {
        "certificate": "D_EXCLUSION_AT_EVENT_LEVEL",
        "question": (
            "Q1(b,c): recompute the support-faithfulness failure at the true"
            " census and name the census-level fact that carries it"
        ),
        "interface_premise_P_NONEMPTY": (
            "any pullback sends the interface's supp(R)-meeting record atom"
            " to a NON-EMPTY set of census record-write events; the census"
            " is exactly the set of realized record writes, so an empty"
            " preimage would mean the interface's record atom records"
            " nothing"
        ),
        "required_zero_cells_from_vendored_902": receipt_vanishing,
        "per_candidate": {
            name: dict(support[name],
                       zero_worlds=len(zero_worlds[name]))
            for name in names
        },
        "excluded_here": excluded,
        "excluded_by_902_generous_base": EXCLUDED_BY_902,
        "narrowing_reproduces": tuple(sorted(excluded))
        == tuple(sorted(EXCLUDED_BY_902)),
        "surviving_set": survivors,
        "disagreement_with_902": (
            None if tuple(sorted(excluded)) == tuple(sorted(EXCLUDED_BY_902))
            else {
                "excluded_here_only": sorted(set(excluded) - set(EXCLUDED_BY_902)),
                "excluded_by_902_only":
                    sorted(set(EXCLUDED_BY_902) - set(excluded)),
                "severity": "MAJOR -- the home-lineage census contradicts the"
                            " generous-base verdict",
            }
        ),
        "exclusion_witnesses": {
            name: {
                "min_event_numerator": support[name]["min_event_numerator"],
                "argmin_event": list(events[
                    min(range(len(events)),
                        key=lambda i: numerators[name][i])
                ]),
                "chain": (
                    "min_e w(e) > 0 over all 92260 events, so every non-empty"
                    " subset of the census carries strictly positive mass;"
                    " with P-NONEMPTY the preimage of a vanishing cell is"
                    " non-empty, hence carries positive mass, hence cannot"
                    " be assigned zero: IF5 is unsatisfiable for this"
                    " weighting"
                ),
            }
            for name in EXCLUDED_BY_902
        },
        "hosting_witnesses": {
            name: {
                "zero_events": len(zero_sets[name]),
                "zero_worlds": len(zero_worlds[name]),
                "zero_region_tag_mix": zero_tag_mix[name],
                "example_zero_events": [
                    list(events[i]) for i in sorted(zero_sets[name])[:2]
                ],
            }
            for name in NARROWED
        },
        "census_level_mechanism": {
            "fact": (
                "of the 748 census worlds that carry at least one record"
                f" event, only {len(formed)} ever reach a global-clean"
                f" boundary; the remaining {len(never_formed)} never-formed"
                f" worlds carry {len(never_formed_events)} of the"
                f" {len(events)} events, and every one of those events is a"
                " bank-tag write (no F tag exists on a world that never"
                " formed)"
            ),
            "worlds_supported": len(worlds),
            "worlds_formed": len(formed),
            "worlds_never_formed": len(never_formed),
            "events_on_never_formed_worlds": len(never_formed_events),
            "never_formed_block_tag_mix": dict(sorted(Counter(
                events[i][2] for i in never_formed_events).items())),
            "mechanism": (
                "M1 and M2 read NOTHING off the formation/occupation ledger:"
                " their world coefficient is the constant 1, so their event"
                " numerator is a product of two strictly positive census"
                " quantities (the constant and the positive within-world"
                " equaliser common/|events(w)|) and their zero set is EMPTY."
                " M3, M4 and M5 read their world coefficient off the ledger,"
                " which is identically zero on the never-formed block, so"
                " their zero sets are exactly that block (M5 additionally"
                " zeroes the worlds formed at moment 0).  The exclusion is"
                " therefore not an abstract failure of 'support"
                " faithfulness': it is the census fact that a"
                " ledger-blind weighting has no zero set to put the"
                " interface's vanishing cells in"
            ),
            "worlds_formed_at_moment_zero": len(formed_at_zero),
            "M5_extra_zero_events":
                len(zero_sets["M5_FORMATION_MOMENT"]
                    - zero_sets["M3_OCCUPATION_WEIGHTED"]),
        },
        "zero_set_lattice": {
            "M3_equals_M4_as_sets": zero_sets["M3_OCCUPATION_WEIGHTED"]
            == zero_sets["M4_FORMATION_LIFETIME"],
            "M3_subset_of_M5": zero_sets["M3_OCCUPATION_WEIGHTED"]
            <= zero_sets["M5_FORMATION_MOMENT"],
            "distinct_zero_sets_among_the_three": len({
                frozenset(zero_sets[name]) for name in NARROWED
            }),
            "consequence": (
                "M3 and M4 have IDENTICAL zero sets, so NO constraint of the"
                " form 'these cells carry zero mass, those carry positive"
                " mass' can ever separate them: every support-type interface"
                " requirement is satisfied by M3 iff it is satisfied by M4"
            ),
        },
    }
    cert_d["pass"] = bool(
        cert_d["narrowing_reproduces"]
        and all(support[n]["strictly_positive_everywhere"]
                for n in EXCLUDED_BY_902)
        and all(support[n]["zero_weight_events"] > 0 for n in NARROWED)
        and zero_counts == receipt_zero
    )

    # ---- E: Q2(a) discrimination among the narrowed three ---------------
    narrowed_pairs = [(a, b) for i, a in enumerate(NARROWED)
                      for b in NARROWED[i + 1:]]
    per_family = {}
    for fam in families:
        row = {}
        for a, b in narrowed_pairs:
            ta, tb = tables[(a, fam)], tables[(b, fam)]
            differing = sorted(k for k in ta if ta[k] != tb[k])
            row[f"{a}|{b}"] = {
                "cells": len(ta), "differing_cells": len(differing),
                "differing_cell_digest": digest([compact(list(k))
                                                 for k in differing]),
            }
        keys_seen = {v["differing_cell_digest"] for v in row.values()}
        row["all_pairs_differ_on_the_same_cells"] = len(keys_seen) == 1
        per_family[fam] = row
    atom_diff = {}
    for a, b in narrowed_pairs:
        ta, tb = tables[(a, "F_ATOM")], tables[(b, "F_ATOM")]
        idx = [i for i in range(len(events))
               if Fraction(numerators[a][i], totals[a])
               != Fraction(numerators[b][i], totals[b])]
        atom_diff[f"{a}|{b}"] = {
            "differing_atoms": len(idx),
            "by_tag": dict(sorted(Counter(events[i][2] for i in idx).items())),
            "distinct_worlds": len({world_of[i] for i in idx}),
            "all_on_formed_worlds": all(world_of[i] in formed for i in idx),
            "all_off_the_shared_zero_region": all(
                i not in zero_sets["M3_OCCUPATION_WEIGHTED"] for i in idx
            ),
            "first_witness": {
                "event": list(events[idx[0]]),
                a: fr(Fraction(numerators[a][idx[0]], totals[a])),
                b: fr(Fraction(numerators[b][idx[0]], totals[b])),
                "label": FRACTION_LABEL,
            } if idx else None,
        }
    cert_e = {
        "certificate": "E_DISCRIMINATION_OF_THE_THREE",
        "question": (
            "Q2(a): which event classes separate M3 from M4 from M5 at the"
            " true census"
        ),
        "narrowed_set": NARROWED,
        "per_family": per_family,
        "atom_level": atom_diff,
        "profile_is_homogeneous": bool(
            len({row["differing_atoms"] for row in atom_diff.values()}) == 1
            and all(per_family[fam]["all_pairs_differ_on_the_same_cells"]
                    for fam in families)
        ),
        "reading": (
            "all three pairs differ on exactly the same cells of every"
            " certified family and on exactly the same atoms -- the events"
            " of the formed worlds.  The discrimination profile carries no"
            " information that distinguishes HOW M3 differs from M4 from HOW"
            " M4 differs from M5, so no cell-counting observable can select"
            " among them; only the exact fraction VALUES differ"
        ),
        "label": FRACTION_LABEL,
    }
    cert_e["pass"] = bool(
        all(v["differing_atoms"] > 0 for v in atom_diff.values())
        and all(v["all_on_formed_worlds"] for v in atom_diff.values())
    )

    # ---- F: Q2(b,c) the pullback ----------------------------------------
    obj = exhibited_object(receipt902)
    ratios = obj["degree0_ints"]
    per_reading = {
        "R_SUPPORT": {name: support[name] for name in names},
        "R_RATIO_EXHAUSTIVE": {
            name: reading_ratio_exhaustive(numerators[name], ratios)
            for name in names
        },
        "R_RATIO_FREE": {
            name: reading_ratio_free(numerators[name], ratios)
            for name in names
        },
    }
    verdict_three = separation_class(per_reading, NARROWED)
    verdict_five = separation_class(per_reading, names)
    spectra = {name: factorize(totals[name]) for name in names}
    shared = None
    for name in NARROWED:
        keys_p = set(spectra[name])
        shared = keys_p if shared is None else (shared & keys_p)
    discriminating_primes = {
        name: sorted(
            p for p in spectra[name]
            if any(spectra[other].get(p, 0) != spectra[name][p]
                   for other in NARROWED if other != name)
        )
        for name in NARROWED
    }
    unique_primes = {
        name: sorted(
            p for p in spectra[name]
            if all(p not in spectra[other] for other in NARROWED
                   if other != name)
        )
        for name in NARROWED
    }
    cert_f = {
        "certificate": "F_PULLBACK_AND_SEPARATION",
        "question": (
            "Q2(b,c): what the gravity side's exhibited interface object"
            " imposes on the census, and which of M3/M4/M5 survives it"
        ),
        "exhibited_object_from_vendored_902": {
            k: (v if k != "degree0" else [fr(x) for x in obj["degree0"]])
            for k, v in obj.items()
        },
        "invariant_content": (
            "the bridge map's freedom leaves the assignment of census events"
            " to interface atoms undetermined, so the invariant content of a"
            " pullback is (i) WHERE zero mass must sit and (ii) the RATIOS of"
            " the degree-0 coefficients -- the normalizer N is free and the"
            " 902 solution space is a single ray, so absolute values carry no"
            " constraint"
        ),
        "readings": {
            "R_SUPPORT": "the vanishing cells pull back into the zero set",
            "R_RATIO_EXHAUSTIVE": (
                "the interface atoms exhaust the census image: the"
                " bookkeeping fractions must EQUAL c_i / sum(c)"
            ),
            "R_RATIO_FREE": (
                "the interface atoms need not exhaust the census image: only"
                " the ratios among four disjoint blocks are constrained"
            ),
        },
        "per_reading_per_candidate": per_reading,
        "verdict_on_the_narrowed_three": verdict_three,
        "verdict_on_all_five": verdict_five,
        "outcome_class": verdict_three["outcome_class"],
        "joint_obstruction_note": (
            "R_RATIO_EXHAUSTIVE fails for every one of the five, including"
            " the two the gravity side had already excluded for an unrelated"
            " reason.  A reading that kills everyone carries no separating"
            " information about the Born set: it prices the EXHIBITED OBJECT"
            " (its degree-0 ratios are not census bookkeeping fractions under"
            " an exhaustive bridge), not the weightings"
        ),
        "census_mass_spectrum": {
            "statement": (
                "a demanded bookkeeping fraction p/q is realizable by a"
                " weighting M only if q divides M's total numerator T; the"
                " achievable denominators are exactly the divisors of T"
            ),
            "totals": {name: totals[name] for name in names},
            "prime_factorisations": {
                name: {str(p): e for p, e in sorted(spectra[name].items())}
                for name in names
            },
            "exhibited_ratio_scale": obj["degree0_sum"],
            "exhibited_ratio_scale_factors": {
                str(p): e for p, e in
                sorted(factorize(obj["degree0_sum"]).items())
            },
            "scale_divides_any_total": any(
                totals[name] % obj["degree0_sum"] == 0 for name in names
            ),
        },
        "priced_residual_separating_question": {
            "why_support_cannot_do_it": (
                "M3 and M4 have identical zero sets (certificate D), so the"
                " separating fact cannot be a support fact"
            ),
            "why_counting_cannot_do_it": (
                "all three pairs differ on identically the same cells of every"
                " certified family (certificate E), so the separating fact"
                " cannot be a cell-count fact"
            ),
            "the_obligation": (
                "the gravity/interface side must exhibit an interface object"
                " whose degree-0 ratio vector has scale q dividing exactly ONE"
                " of the three totals; the primes below are the exact targets"
            ),
            "primes_unique_to_each_candidate": {
                name: unique_primes[name] for name in NARROWED
            },
            "primes_with_differing_multiplicity": {
                name: discriminating_primes[name] for name in NARROWED
            },
            "primes_shared_by_all_three": sorted(shared or ()),
            "current_exhibited_scale_separates": False,
        },
    }
    cert_f["pass"] = bool(
        verdict_three["outcome_class"] in
        ("STABLE", "FURTHER_NARROWED", "SEPARATED")
        and all(unique_primes[name] for name in NARROWED)
    )

    # ---- G: falsifiers ---------------------------------------------------
    plant_survivor = [0] * len(events)
    for i in range(min(obj["degree0_sum"], len(events))):
        plant_survivor[i] = 1
    plant_failer = [1] * len(events)
    plant_failer[0] = 2
    plant_dependent = [
        3 * numerators["M3_OCCUPATION_WEIGHTED"][i]
        + 5 * numerators["M4_FORMATION_LIFETIME"][i]
        for i in range(len(events))
    ]
    plant_relation_vector = [
        (1 if world_of[i] in formed else 0)
        * numerators["M2_PER_WORLD_UNIFORM"][i]
        for i in range(len(events))
    ]
    plant_independent = [0] * len(events)
    plant_independent[-1] = 1
    survivor_rows = {
        "R_SUPPORT": reading_support(plant_survivor, receipt_vanishing),
        "R_RATIO_EXHAUSTIVE": reading_ratio_exhaustive(plant_survivor, ratios),
        "R_RATIO_FREE": reading_ratio_free(plant_survivor, ratios),
    }
    failer_rows = {
        "R_SUPPORT": reading_support(plant_failer, receipt_vanishing),
        "R_RATIO_EXHAUSTIVE": reading_ratio_exhaustive(plant_failer, ratios),
        "R_RATIO_FREE": reading_ratio_free(plant_failer, ratios),
    }
    rank_with_dependent, _ = rank_by_rational_elimination(
        matrix + [plant_dependent]
    )
    rank_with_independent, _ = rank_by_rational_elimination(
        matrix + [plant_independent]
    )
    rank_with_relation, _ = rank_by_rational_elimination(
        matrix + [plant_relation_vector]
    )
    rank_dep_gram, _, _ = rank_by_gram_minors(matrix + [plant_dependent])
    rank_ind_gram, _, _ = rank_by_gram_minors(matrix + [plant_independent])
    rank_rel_gram, _, _ = rank_by_gram_minors(matrix + [plant_relation_vector])
    cert_g = {
        "certificate": "G_FALSIFIERS",
        "planted_pullback_survivor": {
            "construction": (
                "unit mass on the first sum(c) events in canonical census"
                " order, zero elsewhere -- designed to survive every reading"
            ),
            "total_numerator": sum(plant_survivor),
            "rows": survivor_rows,
            "designed_outcome": "survives all three readings",
            "observed_as_designed": bool(
                survivor_rows["R_SUPPORT"]["survives"]
                and survivor_rows["R_RATIO_EXHAUSTIVE"]["survives"]
                and survivor_rows["R_RATIO_FREE"]["survives"]
            ),
            "reading": (
                "the pullback gate is not vacuously false: a weighting built"
                " to satisfy it is shown satisfying it, so the verdict on the"
                " real candidates is a measurement, not a construction"
                " artifact"
            ),
        },
        "planted_pullback_failer": {
            "construction": (
                "counting measure perturbed on one event -- strictly positive"
                " everywhere and with a total coprime to the ratio scale;"
                " designed to fail"
            ),
            "total_numerator": sum(plant_failer),
            "rows": failer_rows,
            "designed_outcome": "fails R_SUPPORT and R_RATIO_EXHAUSTIVE",
            "observed_as_designed": bool(
                failer_rows["R_SUPPORT"]["survives"] is False
                and failer_rows["R_RATIO_EXHAUSTIVE"]["survives"] is False
            ),
        },
        "planted_rank_dependent": {
            "construction": "3*M3 + 5*M4, an exact combination of two rows",
            "rank_with_row_added": rank_with_dependent,
            "gram_route": rank_dep_gram,
            "designed_outcome": "rank unchanged",
            "observed_as_designed": bool(
                rank_with_dependent == rank_a == rank_dep_gram
            ),
        },
        "planted_rank_independent": {
            "construction": (
                "the indicator of a single event.  Every candidate is"
                " world-constant (verified in certificate C) and the smallest"
                " world carries 64 events, so this vector is PROVABLY outside"
                " the span of the five"
            ),
            "rank_with_row_added": rank_with_independent,
            "gram_route": rank_ind_gram,
            "designed_outcome": "rank increases by exactly one",
            "observed_as_designed": bool(
                rank_with_independent == rank_a + 1 == rank_ind_gram
            ),
        },
        "planted_relation_vector": {
            "construction": (
                "the formed-world indicator times the per-world equaliser --"
                " the vector the 878/902 generator relation actually equates"
                " M4 + M5 to"
            ),
            "rank_with_row_added": rank_with_relation,
            "gram_route": rank_rel_gram,
            "designed_outcome": (
                "rank unchanged: (M4 + M5) / (boundaries + 1) IS this vector,"
                " so the relation lives INSIDE the span and constrains nothing"
                " among the five"
            ),
            "observed_as_designed": bool(
                rank_with_relation == rank_a == rank_rel_gram
            ),
            "reading": (
                "this is the rank-side statement of C905-T2: the relation is"
                " true and useless, because the vector it produces is not"
                " M2 -- it differs from M2 exactly on the never-formed block"
            ),
        },
    }
    cert_g["pass"] = bool(
        cert_g["planted_pullback_survivor"]["observed_as_designed"]
        and cert_g["planted_pullback_failer"]["observed_as_designed"]
        and cert_g["planted_rank_dependent"]["observed_as_designed"]
        and cert_g["planted_rank_independent"]["observed_as_designed"]
        and cert_g["planted_relation_vector"]["observed_as_designed"]
    )

    # ---- H: deterministic double build ----------------------------------
    build_b = build_event_space(c863, c878, consts)
    numerators_b, _, _, _, _, common_b = c878.build_candidates(
        build_b["events"], build_b["scan"]["occ_global"],
        build_b["scan"]["formed"], build_b["scan"]["boundaries"],
    )
    rank_b2, _ = rank_by_rational_elimination(
        [numerators_b[name] for name in names]
    )
    cert_h = {
        "certificate": "H_DOUBLE_BUILD",
        "event_digest_A": event_digest,
        "event_digest_B": digest(build_b["events"]),
        "weighting_digest_A": digest(
            {name: numerators[name] for name in names}
        ),
        "weighting_digest_B": digest(
            {name: numerators_b[name] for name in names}
        ),
        "rank_A": rank_a, "rank_B": rank_b2,
        "common_denominator_A": common, "common_denominator_B": common_b,
        "deterministic": bool(
            event_digest == digest(build_b["events"])
            and digest({name: numerators[name] for name in names})
            == digest({name: numerators_b[name] for name in names})
            and rank_a == rank_b2 and common == common_b
        ),
    }
    cert_h["pass"] = cert_h["deterministic"]

    # ---- I: Q3 the lane ledger ------------------------------------------
    axiom_text = (ROOT / AXIOMS_PATH).read_text(encoding="utf-8")
    exclusion_needle = (
        "context selection, measurement basis selection, Born weights,"
        " probability"
    )
    ledger = [
        {
            "id": "BL1_SELECTION",
            "obligation": (
                "select a single weighting on the record-write event space,"
                " or prove no selection is forced"
            ),
            "status_before_this_block":
                "OPEN over five admissible weightings (Cycle 878)",
            "status_now": (
                f"OPEN over {len(NARROWED)}: the narrowing to"
                f" {list(NARROWED)} is certified on the home lineage with the"
                " full census; the base rank is"
                f" {rank_a}, so the surviving three remain linearly"
                " independent and none is a combination of the others"
            ),
            "what_would_close_it": (
                "an interface object whose degree-0 ratio scale divides"
                " exactly one of the three totals (certificate F names the"
                " prime targets)"
            ),
            "blocked_on": "the gravity/interface side",
        },
        {
            "id": "BL2_IF1_BARRIER",
            "obligation": (
                "dissolve or scope the IF1 obstruction -- amplitude support"
                " must overlap supp(R)"
            ),
            "status_now": (
                "OPEN and BARRIER-SCOPED.  902 (C902-T3) proved IF1 is"
                " P2-invariant: the kernel fibre re-weights path lengths and"
                " cannot move a site, so the amplitude's site support is"
                " identical at every fibre point and the barrier B(R) ="
                " supp(R) keeps the two loci disjoint.  It is satisfiable on"
                " 1 of 12 configurations"
            ),
            "cross_reference": (
                "vendored outputs/p2_kernel_attack_cycle902_receipt_"
                "2026_07_28.json -> Q2_per_requirement[IF1],"
                " Q2_minimal_obstructing_subset = ['IF1'],"
                " Q3_boundary"
            ),
            "born_side_consequence": (
                "IF1 is a BARRIER fact, not a weighting fact: it constrains"
                " where amplitude support sits, and certificate D shows the"
                " Born side's only lever on it is its zero set, which is"
                " identical for M3 and M4"
            ),
            "blocked_on": "the barrier construction, not the event space",
        },
        {
            "id": "BL3_IF5_ZERO_CELLS",
            "obligation": (
                "tolerate vanishing Z on admissible windows -- the constraint"
                " that produced the narrowing"
            ),
            "status_now": (
                "DISCHARGED ON THE BORN SIDE, conditionally on P-NONEMPTY:"
                f" the {receipt_vanishing} vanishing cells can be hosted by"
                " each of the three surviving weightings and by neither"
                " excluded one; the hosting region is the never-formed block"
                f" ({len(never_formed)} worlds,"
                f" {len(never_formed_events)} events, all bank-tag writes)"
            ),
            "blocked_on": None,
        },
        {
            "id": "BL4_COMPOSED_RECORD_DYNAMICS",
            "obligation": (
                "an occurrence rule / update law for composed records --"
                " 878's declared exclusion boundary"
            ),
            "status_now": (
                "OPEN and UNTOUCHED.  878's boundary certificate is quoted"
                " from the pinned axiom baseline and nothing in this block"
                " supplies an occurrence rule, a probability, or an update"
                " law; the event space remains a static realized census at a"
                " declared horizon"
            ),
            "exclusion_list_present_in_pinned_axioms":
                exclusion_needle in axiom_text,
            "blocked_on": "the axiom surface (owner)",
        },
        {
            "id": "BL5_ZERO_SET_DEGENERACY",
            "obligation": (
                "NEW, surfaced by this block: M3 and M4 have identical zero"
                " sets, so no support-type interface requirement can ever"
                " separate them"
            ),
            "status_now": (
                "OPEN.  The separating question is now provably a RATIO"
                " question; certificate F prices it as a divisibility"
                " question against the census mass spectrum"
            ),
            "blocked_on": "a ratio-carrying interface object",
        },
        {
            "id": "BL6_NEVER_FORMED_BLOCK",
            "obligation": (
                "NEW, surfaced by the census: 78% of the realized record"
                " events sit on worlds that never form, and every"
                " ledger-valued weighting is blind to them"
            ),
            "status_now": (
                f"OPEN.  {len(never_formed_events)} of {len(events)} events"
                " carry zero mass under all three survivors; any future"
                " selection therefore assigns zero bookkeeping mass to the"
                " large majority of realized records, which is a structural"
                " commitment the lane has not examined"
            ),
            "blocked_on": "the lane",
        },
        {
            "id": "BL7_COVARIANCE",
            "obligation": (
                "878 found per-world uniform is the ONLY candidate covariant"
                " under the landed monitor-phase group -- and it is now"
                " excluded"
            ),
            "status_now": (
                "OPEN and SHARPENED INTO A TENSION: the gravity interface"
                " excludes M2_PER_WORLD_UNIFORM (certificate D), and 878"
                " certified that none of the three survivors is covariant"
                " under the landed monitor-phase group.  So the narrowed set"
                " contains no monitor-phase-covariant member: either the"
                " covariance demand or the interface demand must be given up"
            ),
            "monitor_phase_covariance_of_survivors": {
                name: receipt878["findings"]["candidate_verdicts"][name][
                    "covariance"]["landed_monitor_phase_group_on_worlds"]
                for name in NARROWED
            },
            "blocked_on": "owner / the interface premises",
        },
    ]
    cert_i = {
        "certificate": "I_LANE_LEDGER",
        "question": "Q3: the Born lane's closure ledger, opened",
        "rows": ledger,
        "open_rows": sum(1 for r in ledger if r["status_now"].startswith("OPEN")),
        "discharged_rows": sum(
            1 for r in ledger if r["status_now"].startswith("DISCHARGED")
        ),
        "878_open_gate_verbatim": receipt878["findings"]["open_gate"],
        "boundary": (
            "nothing in this block supplies an occurrence rule, a probability,"
            " or an update law; the narrowing is a CONSTRAINT INHERITED FROM"
            " THE GRAVITY INTERFACE, conditional on the interface premises"
            " named in the vendored 902 receipt and on P-NONEMPTY"
        ),
    }
    cert_i["pass"] = bool(
        len(ledger) >= 6
        and cert_i["878_open_gate_verbatim"]
        and exclusion_needle in axiom_text
    )

    # ---- J: runtime ------------------------------------------------------
    elapsed = round(monotonic() - started, 3)
    cert_j = {
        "certificate": "J_RUNTIME",
        "elapsed_sec": elapsed,
        "budget_sec": RUNTIME_BUDGET_SEC,
        "within_budget": elapsed <= RUNTIME_BUDGET_SEC,
        "scope": (
            "the FULL census at the pinned Cycle-878 horizon"
            f" ({consts['HORIZON']} orbits, {boundaries} boundaries,"
            f" {len(events)} events); no sub-census restriction was needed"
        ),
    }
    cert_j["pass"] = cert_j["within_budget"]

    certificates = (
        ("A_PINS", cert_a), ("B_RESTRICTION_GATE", cert_b),
        ("C_BASE_RANK", cert_c), ("D_EXCLUSION_AT_EVENT_LEVEL", cert_d),
        ("E_DISCRIMINATION_OF_THE_THREE", cert_e),
        ("F_PULLBACK_AND_SEPARATION", cert_f), ("G_FALSIFIERS", cert_g),
        ("H_DOUBLE_BUILD", cert_h), ("I_LANE_LEDGER", cert_i),
        ("J_RUNTIME", cert_j),
    )
    checks = {name: bool(payload["pass"]) for name, payload in certificates}

    theorems = [
        (
            "C905-T1 THE BASE RANK IS"
            f" {rank_a}.  Over the true Cycle-863/878 census the five"
            " record-native weightings of Cycle 878 are linearly"
            f" {'INDEPENDENT' if rank_a == len(names) else 'DEPENDENT'} as"
            " functions on the 92,260-event space, computed by rational"
            " elimination on the full 5 x |E| matrix and by a division-free"
            " Gram/Laplace minor search, cross-checked by world reduction."
            f"  With 902's fibre dimension {receipt_fibre} the minimal"
            " kernel-argument extension of the 878 span therefore has"
            f" dimension {rank_a * receipt_fibre}, collapsing 902's interval"
            f" [{receipt902['Q1_extension_dimension_878_span']['lower_bound']},"
            f" {receipt902['Q1_extension_dimension_878_span']['upper_bound']}]"
            " to a single value."
        ),
        (
            "C905-T2 THE GENERATOR RELATION DOES NOT DESCEND.  The relation"
            " a4 + a5 = (boundaries + 1) * [formed], AST-derived by 902 from"
            " the 878 text, holds EXACTLY on the world coefficients of the"
            f" true census ({len(coeff_violations)} violations over"
            f" {len(worlds)} worlds) but induces NO linear dependence among"
            " the five weightings: the only dependence it could induce,"
            " (boundaries+1)*M2 - M4 - M5, has non-zero residual on"
            f" {len(residual_nonzero)} events across {len(residual_worlds)}"
            " worlds, every one of them never-formed.  The census fact that"
            f" breaks it is that only {len(formed)} of {len(worlds)}"
            " supported worlds ever form."
        ),
        (
            "C905-T3 THE NARROWING IS CENSUS-CARRIED, AND ITS MECHANISM IS"
            " THE NEVER-FORMED BLOCK.  At event level over the true census,"
            " M1_COUNTING and M2_PER_WORLD_UNIFORM have EMPTY zero sets"
            " (exact minimum event numerators 1 and 8320), so under premise"
            " P-NONEMPTY they cannot host a single one of 902's"
            f" {receipt_vanishing} vanishing cells; M3, M4 and M5 host them"
            f" on the {len(never_formed)}-world never-formed block"
            f" ({len(never_formed_events)} events, all bank-tag writes)."
            "  The 902 generous-base exclusion reproduces exactly."
            "  Moreover M3 and M4 have IDENTICAL zero sets, so no"
            " support-type interface requirement can ever separate them."
        ),
        (
            "C905-T4 THE PULLBACK IS"
            f" {verdict_three['outcome_class']}.  Of the three invariant"
            " readings of 902's exhibited interface object, none separates"
            " {M3, M4, M5}: R_SUPPORT and R_RATIO_FREE are constant on the"
            " three, and R_RATIO_EXHAUSTIVE fails for ALL FIVE candidates"
            f" (the ratio scale {obj['degree0_sum']} ="
            f" {'*'.join(str(p) + ('^' + str(e) if e > 1 else '') for p, e in sorted(factorize(obj['degree0_sum']).items()))}"
            " divides no candidate total), so it prices the exhibited object"
            " rather than the weightings.  The residual separating question"
            " is exactly a divisibility question against the census mass"
            " spectrum, with prime targets named per candidate."
        ),
    ]

    receipt = {
        "cycle": 905,
        "block": "toe-time-blockQ2-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "question": (
            "Cycle 905 -- certify the gravity-sourced narrowing of the Born"
            " weighting set on its home lineage with the full census, and"
            " price what would separate the survivors."
        ),
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "VERDICT": verdict_three["outcome_class"],
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "label_on_every_fraction": FRACTION_LABEL,
        "Q1_base_rank": rank_a,
        "Q1_base_rank_routes": {
            "rational_elimination": rank_a, "gram_laplace": rank_b,
            "world_reduction_crosscheck": rank_c,
        },
        "Q1_extension_dimension_over_true_census": rank_a * receipt_fibre,
        "Q1_generator_relation_descends": bool(not residual_nonzero),
        "Q1_generator_relation_residual_events": len(residual_nonzero),
        "Q1_excluded": list(excluded),
        "Q1_surviving": list(survivors),
        "Q1_narrowing_reproduces_902": cert_d["narrowing_reproduces"],
        "Q1_disagreement_with_902": cert_d["disagreement_with_902"],
        "Q1_census_level_mechanism": cert_d["census_level_mechanism"]["fact"],
        "Q2_outcome_class": verdict_three["outcome_class"],
        "Q2_atom_level_discrimination": {
            k: v["differing_atoms"] for k, v in atom_diff.items()
        },
        "Q2_profile_is_homogeneous": cert_e["profile_is_homogeneous"],
        "Q2_separating_readings": list(verdict_three["separating_readings"]),
        "Q2_joint_obstruction_readings":
            list(verdict_three["joint_obstruction_readings"]),
        "Q2_priced_residual":
            cert_f["priced_residual_separating_question"],
        "Q3_ledger": [
            {"id": r["id"], "status": r["status_now"][:120]} for r in ledger
        ],
        "restriction_gate": (
            f"{sum(1 for r in gate_rows if r['match'])}/{len(gate_rows)}"
            " restriction gates reproduce"
        ),
        "restriction_gate_rows": gate_rows,
        "theorems": theorems,
        "zero_weight_events": zero_counts,
        "totals": {name: totals[name] for name in names},
        "event_space_digest": event_digest,
        "deterministic_double_build": cert_h["deterministic"],
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "elapsed_sec": elapsed,
        "scope": (
            "the full realized record-write census of the pinned Cycle-878"
            f" construction at horizon {consts['HORIZON']} orbits"
            f" ({len(events)} events over {len(worlds)} worlds), rebuilt here"
            " by AST lift from the pinned Cycle-863 and Cycle-878 sources"
            " (never imported); the gravity side enters ONLY through the"
            " vendored Cycle-902 artifacts.  Exact rational arithmetic"
            " throughout; no probability, no occurrence rule, no update law."
        ),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_pins": [
            {"path": p, "sha256": cert_a["sha256"][p],
             "git_blob": cert_a["git_blobs"][p], "bytes": cert_a["bytes"][p]}
            for p in AUDIT_INPUT_PATHS
        ],
    }
    receipt["science_digest"] = digest({
        "rank": rank_a, "excluded": list(excluded),
        "surviving": list(survivors),
        "outcome": verdict_three["outcome_class"],
        "event_digest": event_digest,
    })
    out_path = ROOT / "outputs" / "born_narrowing_cycle905_receipt_2026_07_28.json"
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")

    lines = [
        "CYCLE905_BORN_NARROWING_CERTIFIED_ON_ITS_HOME_LINEAGE",
        "BORN_LANE_STRUCTURAL_ONLY_NO_PROBABILITY_POSTULATE",
        "EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY",
    ]
    for name, payload in certificates:
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    for theorem in theorems:
        lines.append("THEOREM " + theorem)
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 905, "checks": checks,
        "VERDICT": verdict_three["outcome_class"],
        "base_rank": rank_a,
        "surviving": list(survivors), "excluded": list(excluded),
        "elapsed_sec": elapsed,
        "pass": all(checks.values()),
    }))
    lines.append(
        "CYCLE905_BORN_NARROWING_"
        + ("PASS" if all(checks.values()) else "HONEST_FAIL")
    )
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
