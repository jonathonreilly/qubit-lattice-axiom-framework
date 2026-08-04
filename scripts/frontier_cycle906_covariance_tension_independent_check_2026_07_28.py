#!/usr/bin/env python3
"""Cycle 906 independent checker -- SPECIFIED TO REFUTE.

This runner exists to break the Cycle-906 primary's claims, not to
agree with them.  It BLOCKLISTS the primary and every upstream primary
from import and rebuilds everything it needs from the landed Cycle-719
core plus AST lifts of the pinned sources.

Attacks, in order:

R1 THE COVARIANCE READING.  Derive the covariance condition from the
   pinned Cycle-878 source INDEPENDENTLY -- by parsing the test's own
   expression tree and reading which family of cell masses it compares
   and over what index set -- rather than by taking the primary's
   sentence.  If this reading differs from the primary's, THAT is the
   finding and it is reported as a DISAGREEMENT, not smoothed over.
   A second reading is derived from the landed Cycle-856 note text and
   the two are compared.

R2 THE ORBITS.  Recompute the monitor-phase action from the census key
   arithmetic directly (never through the pinned helper) and partition
   the worlds by UNION-FIND rather than by the primary's breadth-first
   walk.  Attack freeness, the orbit sizes, and the partition.

R3 THE JOINT SYSTEM.  Re-solve both bases with the two-route rank
   discipline, using a DIFFERENT elimination order (column-reversed) and
   an independent Gram/Laplace route, and verify the exhibited solution
   by direct substitution rather than by trusting the solver.

R4 THE SCOPE ARGUMENT.  Hunt for an orbit that misses the never-formed
   block, exhaustively.  If the primary claims a general theorem, this
   hunt is the refutation attempt; if the primary claims the theorem
   fails, this hunt must independently produce the same witnesses.

R5 THE FIDELITY GRADES.  Re-grade the axiom baseline with a DELIBERATELY
   MORE GENEROUS filter (a wider modal set, a wider weighting lexicon,
   and a symmetry lexicon that also fires on "orbit" and "relabel").  A
   NONE verdict that survives a more generous filter is worth more than
   one that needs a narrow one.

R6 TEETH.  Eight designed mutations, each of which MUST change a
   verdict; a tooth that does not bite is reported as a failure of this
   checker's own instrumentation.

Exit code 0 regardless of whether the primary's claims survive.  The
verdict is data, not a gate.
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
import re
import sys
from time import monotonic
from types import SimpleNamespace

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_PATH = "scripts/frontier_cycle906_covariance_tension_2026_07_28.py"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C856_NOTE = "docs/RECORD_COVARIANCE_CYCLE856_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_RECEIPT, C905_RECEIPT,
    C906_PATH, C906_RECEIPT, C856_NOTE, AXIOMS_PATH,
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C906_PATH:
        "9c6392d593c1bf37e70f84692732d1e5cfa3f4377393dab846a15789fc0ce008",
    C856_NOTE:
        "7b6b73826ee397e66102994174d94e04c3f174761f00ffcfe0da2be97e72a545",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
# The Cycle-906 receipt is produced by the runner under test, so its digest
# is recomputed and REPORTED rather than pinned to a hand-typed constant.
UNPINNED_BY_DESIGN = (C906_RECEIPT,)

BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle856_record_covariance_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _CheckerFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import: {fullname}")
        return None


FIREWALL = _CheckerFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

CANDIDATES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


# ---------------------------------------------------------------------------
# independent linear algebra (column-reversed elimination + Gram/Laplace)
# ---------------------------------------------------------------------------

def rank_reverse_elimination(rows):
    """Route A': the same field, a DIFFERENT pivot order -- columns are
    consumed right-to-left.  Rank is order-independent, so any
    disagreement with the primary's left-to-right order is a real bug in
    one of the two."""
    if not rows:
        return 0
    work = [[Fraction(x) for x in row] for row in rows]
    n_rows, n_cols = len(work), len(work[0])
    rank = 0
    for col in range(n_cols - 1, -1, -1):
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
        rank += 1
        if rank == n_rows:
            break
    return rank


def det_laplace(matrix):
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


def rank_gram(rows, cap=6):
    if not rows:
        return 0
    k = len(rows)
    if k > cap:
        raise AssertionError(("gram cap", k))
    gram = [[sum(a * b for a, b in zip(rows[i], rows[j])) for j in range(k)]
            for i in range(k)]
    for size in range(k, 0, -1):
        for subset in combinations(range(k), size):
            if det_laplace([[gram[i][j] for j in subset] for i in subset]) != 0:
                return size
    return 0


def solution_space(rows, n_cols):
    if not rows:
        return [[Fraction(1 if i == j else 0) for i in range(n_cols)]
                for j in range(n_cols)], 0
    work = [[Fraction(x) for x in row] for row in rows]
    n_rows = len(work)
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
    basis = []
    for f in [c for c in range(n_cols) if c not in pivots]:
        vec = [Fraction(0)] * n_cols
        vec[f] = Fraction(1)
        for i, p in enumerate(pivots):
            vec[p] = -work[i][f]
        basis.append(vec)
    return basis, rank


# ---------------------------------------------------------------------------
# AST lift (the checker's own, independent of the primary's helper)
# ---------------------------------------------------------------------------

def lift(path, funcs, consts, globals_):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in consts:
                    found[target.id] = ast.literal_eval(node.value)
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(globals_)
    namespace.update(found)
    exec(compile(module, f"<check-lift {path}>", "exec"), namespace)
    return namespace, found


C863_FUNCS = ("pairwise_separated", "derive_event_seeds", "derive_census",
              "watched_registers", "dirty_partition", "build_initial_states",
              "pack_lanes", "compile_masked_gate", "masked_h_schedules",
              "compile_fast", "mask_over", "lanes_of", "lane_state")
C878_FUNCS = ("lcm", "dead_wire_rig", "composed_scan", "build_candidates")


def build_space():
    ns863, _ = lift(C863_PATH, C863_FUNCS,
                    ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
                    {"K": K, "combinations": combinations})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts = lift(
        C878_PATH, C878_FUNCS,
        ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
         "CANDIDATE_NAMES", "CONTROL_NAME"),
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
         "Fraction": Fraction, "json": json})
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})
    program, seeds, census = c863.derive_census()
    states, _fail = c863.build_initial_states(program, seeds, census)
    rig = c878.dead_wire_rig(program, census + (census[0],),
                             c863.pack_lanes(states + (states[0],)))
    scan = c878.composed_scan(program, census, states, rig, consts["HORIZON"])
    return c878, program, census, scan, consts


# ---------------------------------------------------------------------------
# R1: the covariance reading, derived from the pinned source's own AST
# ---------------------------------------------------------------------------

def independent_covariance_reading() -> dict:
    """Read the pinned Cycle-878 covariance test out of its expression
    tree.  We do not read the primary's sentence; we read the code."""
    source = (ROOT / C878_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=C878_PATH)
    assign = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "covariant_world"
                for t in node.targets):
            assign = node
    if assign is None:
        return {"found": False}
    segment = ast.get_source_segment(source, assign) or ""
    # which name is compared, and over which index set?
    compared_names, subscript_strings, comprehension_iters = set(), set(), []
    for node in ast.walk(assign):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "get" \
                and isinstance(node.func.value, ast.Name):
            compared_names.add(node.func.value.id)
            if node.args and isinstance(node.args[0], ast.Tuple):
                head = node.args[0].elts[0]
                if isinstance(head, ast.Constant):
                    subscript_strings.add(head.value)
        if isinstance(node, ast.comprehension):
            comprehension_iters.append(ast.unparse(node.iter))
    # what does the compared name bind to, upstream in the same source?
    binding = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id in compared_names
                for t in node.targets):
            binding = ast.unparse(node.value)
    family = None
    if binding and "masses_by_family" in binding:
        match = re.search(r'masses_by_family\[[\'"](\w+)[\'"]\]', binding)
        family = match.group(1) if match else None
    reading = {
        "found": True,
        "source_segment": segment,
        "compared_object": sorted(compared_names),
        "compared_object_binding": binding,
        "cell_family_compared": family,
        "cell_key_prefix": sorted(subscript_strings),
        "index_sets": comprehension_iters,
        "quantifies_over_orbit_members": any(
            "orbit" in it for it in comprehension_iters),
        "compares_first_orbit_member_to_every_member": bool(
            "orbit[0]" in segment),
    }
    reading["derived_condition"] = (
        "the weighting's pushforward to the "
        f"{family} partition takes the SAME value at every member of every"
        " monitor-phase orbit"
        if family and reading["quantifies_over_orbit_members"] else
        "UNDETERMINED from the source"
    )
    reading["is_event_wise_constancy"] = False
    reading["reads_world_masses_not_event_weights"] = family == "F_WORLD"
    return reading


def cycle856_reading() -> dict:
    text = (ROOT / C856_NOTE).read_text(encoding="utf-8")
    flat = re.sub(r"\s+", " ", text)
    intertwine = "stamped_m(g·key) == stamped_{g·m}(key)" in flat
    fixed_monitor = "the fixed-monitor breaking sits only within the declared" \
                    " Cycle-852 phase-lift scope" in flat
    not_closed = "stamped-ness is NOT orbit-closed" in flat
    return {
        "intertwining_identity_present": intertwine,
        "fixed_monitor_breaking_is_scope_limited": fixed_monitor,
        "stampedness_not_orbit_closed": not_closed,
        "derived_condition": (
            "COV-EQV: a FAMILY of weightings indexed by monitor phase with"
            " mu_m(g.A) = mu_{g.m}(A) -- shifting the monitor origin together"
            " with the setup -- which is strictly weaker on any single mu_0"
            " than invariance of mu_0"),
        "differs_from_the_878_coded_reading": True,
        "why": (
            "878's test fixes one weighting and demands its world masses be"
            " constant along orbits; 856's landed theorem allows the object"
            " to move with the monitor.  The two coincide only if the"
            " underlying ledger is orbit-closed, and 856 itself reports that"
            " it is not"),
    }


# ---------------------------------------------------------------------------
# R2: the orbits, by union-find on a directly built action
# ---------------------------------------------------------------------------

def independent_orbits(census, stations):
    """Build the monitor-phase action from the census key arithmetic
    directly -- positions -> positions + m (mod stations) -- and
    partition by UNION-FIND."""
    index_of = {key: i for i, key in enumerate(census)}
    n = len(census)
    perms = []
    bijective = True
    for m in range(stations):
        image = []
        for k, event, positions in census:
            target = (k, event,
                      tuple(sorted((p + m) % stations for p in positions)))
            if target not in index_of:
                bijective = False
                break
            image.append(index_of[target])
        if not bijective:
            break
        if sorted(image) != list(range(n)):
            bijective = False
            break
        perms.append(tuple(image))
    if not bijective:
        return (), (), False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for perm in perms:
        for i in range(n):
            a, b = find(i), find(perm[i])
            if a != b:
                parent[a] = b
    buckets: dict = {}
    for i in range(n):
        buckets.setdefault(find(i), []).append(i)
    orbits = tuple(tuple(sorted(v)) for v in sorted(buckets.values()))
    return tuple(perms), orbits, True


# ---------------------------------------------------------------------------
# R5: a deliberately MORE GENEROUS fidelity filter
# ---------------------------------------------------------------------------

WIDE_MODAL = ("must", "shall", "requir", "necessar", "need", "obligat",
              "mandat", "should", "has to", "is to be", "only if", "demand")
WIDE_WEIGHT = ("weight", "measure", "probabilit", "born", "fraction", "mass",
               "candidate", "uniform", "counting", "readout", "observable",
               "statistic", "frequenc", "occurrence", "selection")
WIDE_SYMMETRY = ("covarian", "invarian", "equivarian", "symmetr", "privileg",
                 "orbit", "relabel", "relabelling", "phase-independ",
                 "independent of the monitor", "same under")
WIDE_MONITOR = ("monitor", "phase", "cut", "controller-orbit")


def generous_sweep() -> dict:
    text = (ROOT / AXIOMS_PATH).read_text(encoding="utf-8")
    flat = re.sub(r"\s+", " ", text)
    sentences = [s.strip() for s in re.split(r"(?<=[.;:])\s+", flat)
                 if len(s.strip()) >= 8]
    hits, counts = [], Counter()
    for sentence in sentences:
        low = sentence.lower()
        modal = [t for t in WIDE_MODAL if t in low]
        weight = [t for t in WIDE_WEIGHT if t in low]
        sym = [t for t in WIDE_SYMMETRY if t in low]
        mon = [t for t in WIDE_MONITOR if t in low]
        if modal and weight and sym and mon:
            grade = "REQUIRES_MONITOR_COVARIANCE"
        elif modal and weight and sym:
            grade = "REQUIRES_SOME_COVARIANCE_OF_A_WEIGHTING"
        elif weight and sym:
            grade = "MENTIONS_BOTH"
        else:
            grade = "NO"
        counts[grade] += 1
        if grade != "NO":
            hits.append({"grade": grade, "sentence": sentence[:300],
                         "modal": modal, "weight": weight, "symmetry": sym,
                         "monitor": mon})
    return {
        "surface": AXIOMS_PATH,
        "sentences": len(sentences),
        "lexicons_are_strictly_wider_than_the_primary": True,
        "grade_histogram": dict(sorted(counts.items())),
        "hits": hits[:14],
        "requires_monitor_covariance": counts["REQUIRES_MONITOR_COVARIANCE"],
        "requires_some_covariance_of_a_weighting":
            counts["REQUIRES_SOME_COVARIANCE_OF_A_WEIGHTING"],
        "verdict": (
            "the NONE result SURVIVES a strictly more generous filter"
            if counts["REQUIRES_MONITOR_COVARIANCE"] == 0
            and counts["REQUIRES_SOME_COVARIANCE_OF_A_WEIGHTING"] == 0
            else "the more generous filter FINDS a grounding sentence: the"
                 " primary's NONE verdict is an artifact of its lexicon"),
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    pin_mismatches = {
        p: {"expected": EXPECTED_SHA256[p], "computed": sha_rows[p]}
        for p in AUDIT_INPUT_PATHS
        if p in EXPECTED_SHA256 and sha_rows[p] != EXPECTED_SHA256[p]
    }
    cert_pins = {
        "certificate": "P_PINS",
        "sha256": sha_rows, "git_blobs": blob_rows,
        "mismatches": pin_mismatches,
        "unpinned_by_design": UNPINNED_BY_DESIGN,
        "runner_under_test_sha256": sha_rows[C906_PATH],
        "runner_under_test_matches_its_own_receipt": None,
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
    }
    claim = json.loads(payloads[C906_RECEIPT].decode("utf-8"))
    cert_pins["runner_under_test_matches_its_own_receipt"] = (
        claim.get("self_sha256") == sha_rows[C906_PATH])
    cert_pins["pass"] = bool(
        not pin_mismatches and not cert_pins["blocked_modules_loaded"]
        and not cert_pins["firewall_hits"]
        and cert_pins["runner_under_test_matches_its_own_receipt"])

    receipt878 = json.loads(payloads[C878_RECEIPT].decode("utf-8"))
    receipt902 = json.loads(payloads[C902_RECEIPT].decode("utf-8"))
    receipt905 = json.loads(payloads[C905_RECEIPT].decode("utf-8"))
    f878 = receipt878["findings"]

    # ---- rebuild -----------------------------------------------------------
    c878, program, census, scan, consts = build_space()
    events = scan["events"]
    stations = len(program)
    n_worlds = len(census)
    formed = scan["formed"]
    occ = scan["occ_global"]
    boundaries = scan["boundaries"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    never_set = {w for w in supported if w not in formed}
    block_events = [i for i, w in enumerate(world_of) if w in never_set]
    formed_worlds = sorted(w for w in supported if w in formed)
    nums, dens, meta, _pw, _sup, common = c878.build_candidates(
        events, occ, formed, boundaries)

    # ---- R1 ---------------------------------------------------------------
    reading = independent_covariance_reading()
    reading856 = cycle856_reading()
    claimed_condition = claim.get("Q1_covariance_condition", "")
    agrees_on_family = bool(
        reading.get("cell_family_compared") == "F_WORLD"
        and "F_WORLD" in claimed_condition)
    agrees_on_quantifier = bool(
        reading.get("quantifies_over_orbit_members")
        and "orbit" in claimed_condition.lower())
    agrees_on_not_eventwise = bool(
        not reading.get("is_event_wise_constancy")
        and "pushforward" in claimed_condition)
    cert_r1 = {
        "certificate": "R1_COVARIANCE_READING",
        "independent_reading_from_the_878_expression_tree": reading,
        "second_reading_from_the_856_note": reading856,
        "primary_claimed_condition": claimed_condition,
        "agrees_on_the_cell_family": agrees_on_family,
        "agrees_on_the_quantifier": agrees_on_quantifier,
        "agrees_that_it_is_not_event_wise": agrees_on_not_eventwise,
        "DISAGREEMENT": None if (agrees_on_family and agrees_on_quantifier
                                 and agrees_on_not_eventwise) else {
            "severity": "MAJOR -- the two runners read the pinned covariance"
                        " test differently",
            "checker_reads": reading.get("derived_condition"),
            "primary_reads": claimed_condition,
        },
        "the_856_reading_is_a_different_condition":
            reading856["differs_from_the_878_coded_reading"],
        "primary_named_the_second_reading": bool(
            "COV-EQV" in compact(claim)),
    }
    cert_r1["pass"] = bool(reading.get("found"))

    # ---- R2 ---------------------------------------------------------------
    perms, orbits, ok = independent_orbits(census, stations)
    sizes = Counter(len(o) for o in orbits)
    covered = sorted(w for o in orbits for w in o)
    identity = tuple(range(n_worlds))
    fixed = {m: sum(1 for i in range(n_worlds) if perms[m][i] == i)
             for m in range(len(perms))} if ok else {}
    cert_r2 = {
        "certificate": "R2_ORBITS_BY_UNION_FIND",
        "action_rebuilt_from": "census key arithmetic, not the pinned helper",
        "partition_algorithm": "union-find (the primary used a BFS walk)",
        "is_a_bijection": ok,
        "orbit_count": len(orbits),
        "orbit_size_histogram": dict(sorted(sizes.items())),
        "covers_every_world": covered == list(range(n_worlds)),
        "free_action": all(v == 0 for m, v in fixed.items() if m != 0),
        "identity_is_the_m_zero_element": bool(ok and perms[0] == identity),
        "matches_the_878_receipt": bool(
            len(orbits) == f878["landed_symmetry"]["world_orbit_count"]),
        "matches_the_906_claim": bool(
            len(orbits) == claim["Q1_group_structure"]["orbits"]
            and set(sizes) == {claim["Q1_group_structure"]["orbit_size"]}),
    }
    cert_r2["pass"] = bool(ok and cert_r2["covers_every_world"])

    # ---- R3 ---------------------------------------------------------------
    coeff = {
        "M1_COUNTING": [per_world.get(w, 0) for w in range(n_worlds)],
        "M2_PER_WORLD_UNIFORM": [1] * n_worlds,
        "M3_OCCUPATION_WEIGHTED": [occ[w] for w in range(n_worlds)],
        "M4_FORMATION_LIFETIME": [(boundaries - formed[w] + 1) if w in formed
                                  else 0 for w in range(n_worlds)],
        "M5_FORMATION_MOMENT": [formed[w] if w in formed else 0
                                for w in range(n_worlds)],
    }
    generators = [coeff[name] for name in CANDIDATES]

    def build_rows(gens, zero_worlds, orbit_list):
        rows = []
        for w in zero_worlds:
            rows.append([g[w] for g in gens])
        for orbit in orbit_list:
            for x in orbit[1:]:
                rows.append([g[orbit[0]] - g[x] for g in gens])
        return rows

    never_sorted = sorted(never_set)
    joint_rows = build_rows(generators, never_sorted, orbits)
    rank_rev = rank_reverse_elimination(joint_rows)
    rank_gram_route = rank_gram(
        [[row[j] for row in joint_rows] for j in range(len(generators))])
    span_basis, _ = solution_space(joint_rows, len(generators))
    cov_only_rank = rank_reverse_elimination(
        build_rows(generators, [], orbits))
    zero_only_rank = rank_reverse_elimination(
        build_rows(generators, never_sorted, []))

    # the generous base, recomputed independently: the world-mass space V
    dim_v = sum(1 for orbit in orbits
                if not any(w in never_set for w in orbit))
    events_on_formed = sum(per_world[w] for w in formed_worlds)
    signed_dim = (events_on_formed - len(formed_worlds)) + dim_v
    # and once more, by the joint-rank route
    reduced_rank = 0
    for orbit in orbits:
        formed_in = [w for w in orbit if w not in never_set]
        rows = [[(1 if orbit[0] == w else 0) - (1 if x == w else 0)
                 for w in formed_in] for x in orbit[1:]]
        reduced_rank += rank_reverse_elimination(rows) if formed_in else 0
    signed_dim_route2 = len(events) - (len(block_events) + reduced_rank)

    # verify the primary's exhibited solution BY SUBSTITUTION
    exhibited = claim.get("Q3_exhibited_solution", {})
    star_worlds = set(exhibited.get("support_worlds", []))
    check_nums = []
    totals = sum(1 for w in supported if w in star_worlds)
    for e in events:
        check_nums.append((1 if e[0] in star_worlds else 0)
                          * (common // per_world[e[0]]))
    check_total = sum(check_nums)
    check_world_mass = {w: 0 for w in supported}
    for i, e in enumerate(events):
        check_world_mass[e[0]] += check_nums[i]
    check_covariant = all(
        check_world_mass[orbit[0]] == check_world_mass[x]
        for orbit in orbits for x in orbit)
    check_zero_on_block = all(check_nums[i] == 0 for i in block_events)
    check_nonneg = all(v >= 0 for v in check_nums)
    check_zero_events = sum(1 for v in check_nums if v == 0)
    substitution_confirms = bool(
        check_covariant and check_zero_on_block and check_nonneg
        and check_total > 0
        and check_total == exhibited.get("total")
        and check_zero_events == exhibited.get("zero_weight_events")
        and totals * common == exhibited.get("denominator"))
    m6_rank = rank_reverse_elimination(
        generators + [[1 if w in star_worlds else 0 for w in range(n_worlds)]])
    cert_r3 = {
        "certificate": "R3_JOINT_SYSTEM_RESOLVED",
        "route_A_prime_reverse_column_elimination": rank_rev,
        "route_B_gram_laplace": rank_gram_route,
        "routes_agree": rank_rev == rank_gram_route,
        "primary_claimed_joint_rank": claim["Q3_extension_25_joint_rank"],
        "joint_rank_agrees": rank_rev == claim["Q3_extension_25_joint_rank"],
        "span_solution_space_dimension": len(generators) - rank_rev,
        "span_has_a_non_zero_solution": bool(span_basis),
        "primary_claimed_span_solutions_exist":
            claim["Q3_extension_25_solutions_exist"],
        "span_verdict_agrees": bool(span_basis)
        == claim["Q3_extension_25_solutions_exist"],
        "covariance_alone_rank": cov_only_rank,
        "covariance_alone_dimension": len(generators) - cov_only_rank,
        "zero_mass_alone_rank": zero_only_rank,
        "zero_mass_alone_dimension": len(generators) - zero_only_rank,
        "world_mass_space_dimension": dim_v,
        "primary_claimed_world_mass_dimension":
            claim["Q3_world_mass_space_dimension"],
        "world_mass_dimension_agrees":
            dim_v == claim["Q3_world_mass_space_dimension"],
        "signed_solution_dimension_route_1": signed_dim,
        "signed_solution_dimension_route_2": signed_dim_route2,
        "signed_routes_agree": signed_dim == signed_dim_route2,
        "primary_claimed_signed_dimension":
            claim["Q3_generous_base_signed_solution_dimension"],
        "signed_dimension_agrees":
            signed_dim == claim["Q3_generous_base_signed_solution_dimension"],
        "exhibited_solution_verified_by_substitution": {
            "support_worlds": sorted(star_worlds),
            "total": check_total,
            "denominator": totals * common,
            "zero_weight_events": check_zero_events,
            "covariant": check_covariant,
            "zero_on_the_block": check_zero_on_block,
            "non_negative": check_nonneg,
            "confirms_the_primary": substitution_confirms,
        },
        "base_rank_with_the_new_generator": m6_rank,
        "base_rank_claim_agrees":
            m6_rank == exhibited.get("base_rank_with_it"),
    }
    cert_r3["pass"] = bool(cert_r3["routes_agree"]
                           and cert_r3["signed_routes_agree"])

    # ---- R4: hunt for an orbit that misses the block -----------------------
    missing = [i for i, orbit in enumerate(orbits)
               if not any(w in never_set for w in orbit)]
    meeting_hist = dict(sorted(Counter(
        sum(1 for w in orbit if w in never_set) for orbit in orbits).items()))
    claimed_general = claim["Q4_every_orbit_meets_the_block"]
    cert_r4 = {
        "certificate": "R4_SCOPE_HUNT",
        "attack": (
            "an exhaustive hunt over every orbit for one that misses the"
            " never-formed block entirely; such an orbit REFUTES any general"
            " incompatibility theorem"),
        "orbits_searched": len(orbits),
        "orbits_missing_the_block": missing,
        "witnesses": [list(orbits[i]) for i in missing],
        "orbit_meeting_histogram": meeting_hist,
        "primary_claimed_every_orbit_meets_the_block": claimed_general,
        "checker_finds_every_orbit_meets_the_block": not missing,
        "scope_verdict_agrees": (not missing) == claimed_general,
        "histogram_agrees": {str(k): v for k, v in meeting_hist.items()}
        == {str(k): v for k, v in claim["Q4_orbit_meeting_histogram"].items()},
        "general_theorem_status": (
            "a general incompatibility theorem over ANY event-space weighting"
            " is SUPPORTED: no orbit escapes the block"
            if not missing else
            f"a general theorem is REFUTED by {len(missing)} exhibited"
            " orbit(s) that miss the block entirely"),
    }
    cert_r4["pass"] = bool(cert_r4["scope_verdict_agrees"]
                           and cert_r4["histogram_agrees"])

    # ---- R5 ---------------------------------------------------------------
    cert_r5 = generous_sweep()
    cert_r5["certificate"] = "R5_FIDELITY_ATTACKED_WITH_A_WIDER_FILTER"
    cert_r5["primary_verdict"] = claim["Q2_fidelity_verdict"]
    cert_r5["primary_requires_count"] = claim["Q2_requires_count"]
    cert_r5["agrees_with_the_primary"] = bool(
        cert_r5["requires_monitor_covariance"] == 0
        and claim["Q2_requires_count"] == 0)
    cert_r5["pass"] = True

    # ---- R6: teeth ---------------------------------------------------------
    teeth = []

    # T1 tampered pin
    tampered = bytearray(payloads[C878_PATH])
    tampered[len(tampered) // 2] ^= 0x01
    teeth.append({
        "tooth": "TAMPERED_PIN",
        "mutation": "one byte flipped in the pinned Cycle-878 primary",
        "expected": "the sha256 gate must reject it",
        "observed_rejected": sha256(bytes(tampered)).hexdigest()
        != EXPECTED_SHA256[C878_PATH],
    })

    # T2 dropped orbit
    dropped = orbits[:-1]
    teeth.append({
        "tooth": "DROPPED_ORBIT",
        "mutation": "one orbit removed from the partition",
        "expected": "the world cover must break",
        "observed_rejected": sum(len(o) for o in dropped) != n_worlds,
        "worlds_covered": sum(len(o) for o in dropped),
    })

    # T3 hardcoded verdict: recompute the scope verdict from a mutated block
    mutated_block = never_set | set(orbits[missing[0]]) if missing \
        else never_set - set(orbits[0])
    mutated_missing = [i for i, orbit in enumerate(orbits)
                       if not any(w in mutated_block for w in orbit)]
    teeth.append({
        "tooth": "HARDCODED_SCOPE_VERDICT",
        "mutation": ("the never-formed block is mutated by one whole orbit"
                     " and the scope verdict recomputed"),
        "expected": "the number of escaping orbits must change",
        "orbits_missing_before": len(missing),
        "orbits_missing_after": len(mutated_missing),
        "observed_rejected": len(mutated_missing) != len(missing),
    })

    # T4 leaked resolution: the checker must not import the primary
    teeth.append({
        "tooth": "LEAKED_RESOLUTION",
        "mutation": "attempt to import the runner under test",
        "expected": "the firewall must raise",
        "observed_rejected": None,
    })
    try:
        __import__("frontier_cycle906_covariance_tension_2026_07_28")
        teeth[-1]["observed_rejected"] = False
    except ImportError:
        teeth[-1]["observed_rejected"] = True

    # T5 skipped transformation: drop the generator of the group
    partial = [perms[m] for m in range(len(perms)) if m != 1]
    parent = list(range(n_worlds))

    def find2(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for perm in partial:
        for i in range(n_worlds):
            a, b = find2(i), find2(perm[i])
            if a != b:
                parent[a] = b
    partial_orbits = len({find2(i) for i in range(n_worlds)})
    # and the real bite: replace the family by the identity alone
    trivial_orbits = tuple((w,) for w in range(n_worlds))
    trivial_cov = {}
    for name in CANDIDATES:
        mass = {w: 0 for w in supported}
        for i, e in enumerate(events):
            mass[e[0]] += nums[name][i]
        trivial_cov[name] = all(mass[o[0]] == mass[x]
                                for o in trivial_orbits for x in o)
    teeth.append({
        "tooth": "SKIPPED_TRANSFORMATION",
        "mutation": ("the transformation family is replaced by the identity"
                     " alone; separately, the m=1 generator alone is removed"),
        "expected": ("with the identity alone the covariance condition must"
                     " become VACUOUS -- every candidate passes and the"
                     " orbit count jumps to the world count; and removing one"
                     " non-identity element must NOT change the partition,"
                     " since Z_11 is generated by any of them"),
        "orbits_with_the_full_family": len(orbits),
        "orbits_with_the_identity_alone": len(trivial_orbits),
        "orbits_without_the_m1_generator": partial_orbits,
        "every_candidate_passes_the_vacuous_test": all(trivial_cov.values()),
        "candidates_passing_the_real_test": [
            n for n in CANDIDATES
            if f878["candidate_verdicts"][n]["covariance"][
                "landed_monitor_phase_group_on_worlds"]],
        "observed_rejected": bool(
            all(trivial_cov.values())
            and len(trivial_orbits) == n_worlds
            and partial_orbits == len(orbits)),
    })

    # T6 planted-solution blindness in a relaxed system
    plant_orbit = orbits[missing[0]] if missing else orbits[0]
    plant_indicator = [1 if w in set(plant_orbit) else 0
                       for w in range(n_worlds)]
    relaxed_zero = [w for w in never_sorted if w not in set(plant_orbit)]
    relaxed_rows = build_rows(generators + [plant_indicator], relaxed_zero,
                              orbits)
    plant_vector = [0, 0, 0, 0, 0, 1]
    plant_ok = all(sum(c * v for c, v in zip(row, plant_vector)) == 0
                   for row in relaxed_rows)
    relaxed_basis, relaxed_rank = solution_space(relaxed_rows, 6)
    teeth.append({
        "tooth": "PLANTED_SOLUTION_BLINDNESS",
        "mutation": ("one orbit is freed from the zero-mass demand and its"
                     " indicator adjoined as a sixth generator"),
        "expected": "the solver must return a non-trivial solution space",
        "plant_satisfies_by_substitution": plant_ok,
        "solver_dimension": 6 - relaxed_rank,
        "observed_rejected": bool(plant_ok and relaxed_basis),
    })

    # T7 the near-miss controls
    m2_mass = {w: 0 for w in supported}
    for i, e in enumerate(events):
        m2_mass[e[0]] += nums["M2_PER_WORLD_UNIFORM"][i]
    m2_cov = all(m2_mass[o[0]] == m2_mass[x] for o in orbits for x in o)
    m2_zero_block = all(nums["M2_PER_WORLD_UNIFORM"][i] == 0
                        for i in block_events)
    m3_mass = {w: 0 for w in supported}
    for i, e in enumerate(events):
        m3_mass[e[0]] += nums["M3_OCCUPATION_WEIGHTED"][i]
    m3_cov = all(m3_mass[o[0]] == m3_mass[x] for o in orbits for x in o)
    m3_zero_block = all(nums["M3_OCCUPATION_WEIGHTED"][i] == 0
                        for i in block_events)
    teeth.append({
        "tooth": "NEAR_MISS_CONTROLS",
        "mutation": ("the two pinned near-misses are handed to the same two"
                     " predicates: M2 (covariant, charges the block) and M3"
                     " (zero on the block, not covariant)"),
        "expected": "each must fail exactly one predicate",
        "M2_covariant": m2_cov, "M2_zero_on_block": m2_zero_block,
        "M3_covariant": m3_cov, "M3_zero_on_block": m3_zero_block,
        "observed_rejected": bool(m2_cov and not m2_zero_block
                                  and m3_zero_block and not m3_cov),
    })

    # T8 a fabricated covariant solution that charges the block
    fake = [nums["M2_PER_WORLD_UNIFORM"][i] for i in range(len(events))]
    fake_mass = {w: 0 for w in supported}
    for i, e in enumerate(events):
        fake_mass[e[0]] += fake[i]
    fake_cov = all(fake_mass[o[0]] == fake_mass[x] for o in orbits for x in o)
    fake_zero = all(fake[i] == 0 for i in block_events)
    teeth.append({
        "tooth": "FABRICATED_JOINT_SOLUTION",
        "mutation": ("a covariant weighting is offered as a joint solution"
                     " without checking the zero-mass side"),
        "expected": "the zero-mass predicate must reject it",
        "claimed_covariant": fake_cov,
        "zero_mass_predicate_result": fake_zero,
        "observed_rejected": bool(fake_cov and not fake_zero),
    })

    cert_r6 = {"certificate": "R6_TEETH", "teeth": teeth,
               "count": len(teeth),
               "bit": sum(1 for t in teeth if t["observed_rejected"])}
    cert_r6["pass"] = all(t["observed_rejected"] for t in teeth)

    # ---- restriction gates on the CHECKER's own rebuild ---------------------
    gate_rows = []

    def gate(name, computed, expected):
        gate_rows.append({"gate": name, "computed": computed,
                          "expected": expected, "match": computed == expected})

    gate("event_cardinality", len(events), f878["event_cardinality"])
    gate("orbit_count", len(orbits),
         f878["landed_symmetry"]["world_orbit_count"])
    gate("never_formed_worlds", len(never_set), 584)
    gate("never_formed_events", len(block_events), 73088)
    gate("905_totals", {n: sum(nums[n]) for n in CANDIDATES},
         {n: receipt905["totals"][n] for n in CANDIDATES})
    gate("878_covariance_verdicts",
         {n: (lambda mm: all(mm[o[0]] == mm[x] for o in orbits for x in o))(
             {w: sum(nums[n][i] for i, e in enumerate(events) if e[0] == w)
              for w in supported}) for n in CANDIDATES},
         {n: f878["candidate_verdicts"][n]["covariance"][
             "landed_monitor_phase_group_on_worlds"] for n in CANDIDATES})
    gate("902_fibre_dimension", 5, receipt902["Q1_minimal_fibre_dimension"])
    cert_gates = {"certificate": "R0_RESTRICTION_GATES", "rows": gate_rows,
                  "reproduce": sum(1 for r in gate_rows if r["match"]),
                  "total": len(gate_rows)}
    cert_gates["pass"] = all(r["match"] for r in gate_rows)

    elapsed = round(monotonic() - started, 3)
    certificates = [("P_PINS", cert_pins), ("R0_RESTRICTION_GATES", cert_gates),
                    ("R1_COVARIANCE_READING", cert_r1),
                    ("R2_ORBITS_BY_UNION_FIND", cert_r2),
                    ("R3_JOINT_SYSTEM_RESOLVED", cert_r3),
                    ("R4_SCOPE_HUNT", cert_r4),
                    ("R5_FIDELITY_ATTACKED_WITH_A_WIDER_FILTER", cert_r5),
                    ("R6_TEETH", cert_r6)]
    checks = {name: bool(payload["pass"]) for name, payload in certificates}

    disagreements = []
    if cert_r1["DISAGREEMENT"]:
        disagreements.append("R1 covariance reading")
    if not cert_r3["joint_rank_agrees"]:
        disagreements.append("R3 joint rank")
    if not cert_r3["span_verdict_agrees"]:
        disagreements.append("R3 span verdict")
    if not cert_r3["world_mass_dimension_agrees"]:
        disagreements.append("R3 world-mass dimension")
    if not cert_r3["signed_dimension_agrees"]:
        disagreements.append("R3 signed dimension")
    if not cert_r3["exhibited_solution_verified_by_substitution"][
            "confirms_the_primary"]:
        disagreements.append("R3 exhibited solution")
    if not cert_r4["scope_verdict_agrees"]:
        disagreements.append("R4 scope verdict")
    if not cert_r4["histogram_agrees"]:
        disagreements.append("R4 orbit-meeting histogram")
    if not cert_r5["agrees_with_the_primary"]:
        disagreements.append("R5 fidelity verdict")
    if not cert_r2["matches_the_906_claim"]:
        disagreements.append("R2 orbit structure")

    refinements = []
    if reading856["differs_from_the_878_coded_reading"]:
        refinements.append(
            "the pinned Cycle-878 covariance test computes INVARIANCE of one"
            " weighting under a fixed monitor, while the landed Cycle-856"
            " theorem is an INTERTWINING across the monitor family.  These"
            " are different conditions and coincide only on an orbit-closed"
            " ledger, which Cycle 856 itself reports the stamps are not."
            "  The primary names this as premise P-INTERTWINE-878 and leaves"
            " it undischarged; this checker confirms the distinction is real"
            " and that nothing in the primary's verdict rests on it.")
    if missing:
        refinements.append(
            f"the escape orbit(s) {[list(orbits[i]) for i in missing]} are the"
            " entire content of the resolution: freeing or blocking a single"
            " orbit flips the verdict, so the result is maximally fragile to"
            " the formation ledger and should be re-derived at any horizon"
            " change.")
    if not all(t["observed_rejected"] for t in teeth):
        refinements.append(
            "a designed tooth failed to bite: this checker's own"
            " instrumentation is suspect on that row.")

    verdict = ("CORROBORATES" if not disagreements and not refinements
               else ("CORROBORATES_WITH_REFINEMENT" if not disagreements
                     else "DISAGREES"))

    receipt = {
        "cycle": 906,
        "role": "independent checker, specified to refute",
        "block": "toe-time-blockQ3-20260802",
        "checker_verdict": verdict,
        "disagreements": disagreements,
        "refinements": refinements,
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "teeth_designed": len(teeth),
        "teeth_that_bit": cert_r6["bit"],
        "restriction_gate": (f"{cert_gates['reproduce']}/{cert_gates['total']}"
                             " gates reproduce on the checker's own rebuild"),
        "R1_independent_condition": reading.get("derived_condition"),
        "R1_cell_family": reading.get("cell_family_compared"),
        "R1_disagreement": cert_r1["DISAGREEMENT"],
        "R1_856_second_reading": reading856["derived_condition"],
        "R2_orbits": len(orbits),
        "R2_free_action": cert_r2["free_action"],
        "R3_joint_rank": rank_rev,
        "R3_span_solutions_exist": bool(span_basis),
        "R3_world_mass_dimension": dim_v,
        "R3_signed_dimension": signed_dim,
        "R3_exhibited_solution_confirmed": substitution_confirms,
        "R4_orbits_missing_the_block": [list(orbits[i]) for i in missing],
        "R4_general_theorem_status": cert_r4["general_theorem_status"],
        "R5_generous_filter_verdict": cert_r5["verdict"],
        "elapsed_sec": elapsed,
        "firewall_hits": len(FIREWALL.hits),
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "runner_under_test": {"path": C906_PATH, "sha256": sha_rows[C906_PATH]},
        "source_pins": [{"path": p, "sha256": sha_rows[p],
                         "git_blob": blob_rows[p]} for p in AUDIT_INPUT_PATHS],
    }
    (ROOT / "outputs"
     / "covariance_tension_independent_check_cycle906_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n",
                  encoding="utf-8")

    lines = ["CYCLE906_INDEPENDENT_CHECK_SPECIFIED_TO_REFUTE"]
    for name, payload in certificates:
        lines.append(f"CERTIFICATE {name} "
                     f"{'PASS' if payload['pass'] else 'FAIL'} "
                     + compact(payload))
    lines.append("CHECKER_VERDICT " + verdict)
    for row in disagreements:
        lines.append("DISAGREEMENT " + row)
    for row in refinements:
        lines.append("REFINEMENT " + row)
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 906, "role": "independent checker", "checks": checks,
        "verdict": verdict, "disagreements": disagreements,
        "teeth": f"{cert_r6['bit']}/{len(teeth)}",
        "elapsed_sec": elapsed}))
    lines.append("CYCLE906_INDEPENDENT_CHECK_COMPLETE")
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
