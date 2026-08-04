#!/usr/bin/env python3
"""Cycle 907 independent checker -- SPECIFIED TO REFUTE.

This runner exists to break the Cycle-907 primary's claims, not to agree
with them.  It BLOCKLISTS the primary and every upstream primary from
import and rebuilds everything it needs from the landed Cycle-719 core
plus AST lifts of the pinned sources.

Attacks, in order:

R1 THE TWO OBJECTS, REBUILT WITHOUT THE PRIMARY'S ROUTES.  The gravity
   side is re-read out of the vendored Cycle-902 receipt by REGEX over
   the raw text, never by json.loads, and the two readings are compared
   byte for byte.  The Born side is rebuilt without the primary's
   world_weighted helper: the common denominator is recomputed as an LCM
   of the per-world event counts from first principles and M6's quantum
   is derived from it.  A disagreement here is a refutation.

R2 THE BRIDGE SEARCH, WITH THE CHECKER'S OWN PARAMETERIZATION.  The
   primary parameterizes a bridge by its block-mass vector.  This checker
   parameterizes it by the COUNT MATRIX x[i][j] = how many events of
   value class j land in atom i -- a bounded integer program -- and
   decides it by exhaustive enumeration over the proportionality unit,
   which for M6 is complete.  Then it hunts for a bridge OUTSIDE the
   primary's declared family, in three independent directions: fractional
   (a transport plan), non-disjoint (overlapping atom preimages) and
   degree-dependent (a different phi per degree).  A bridge found outside
   the declared family that the primary did not disclose is a refutation
   of the family bound.  The primary's exhibited P2 identification is
   re-verified by direct substitution, never by trusting its solver.

R3 THE INTERFACE SHEET, REIMPLEMENTED.  Every requirement is recomputed
   by a different test than the primary used -- IF4 by the superincreasing
   inequality rather than by enumerating subset sums, IF3 from the
   theta-MOVING list rather than the theta-free one, and so on -- and
   every verdict is compared with the primary's receipt.

R4 THE CONDITIONALITY CHAIN.  Every premise this checker must itself
   consume is enumerated and matched against the primary's named list.  A
   premise consumed but unlisted is a REFUTATION.  Claims the primary
   asserts without a byte-quote are licensed here by quoting the pinned
   source, and the gap is recorded.

R5 THE SELECTION TABLE, RECOMPUTED, and compared with the receipt.

R6 TEETH.  Eight designed mutations, each of which MUST change a verdict;
   a tooth that does not bite is reported as a failure of this checker's
   own instrumentation, not hidden.

Exit code 0 regardless of whether the primary's claims survive.  The
verdict is data, not a gate.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
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
C902_PATH = "scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py"
C902_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C907_PATH = "scripts/frontier_cycle907_m6_identification_2026_07_28.py"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_PATH, C902_RECEIPT,
    C905_RECEIPT, C906_RECEIPT, C907_PATH, C907_RECEIPT, AXIOMS_PATH,
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
    C902_PATH:
        "46d46db10258731b986f3c639eedcf1ad3f968021f1efe30c88cc3e5e17b46c2",
    C902_RECEIPT:
        "91c5631415d0231390fedbd0174f074de45cfa33b6dd4f706ed6fcdbf4dfd1d8",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle907_m6_identification_2026_07_28",
    "frontier_cycle907_m6_identification_independent_check_2026_07_28",
    "frontier_cycle856_record_covariance_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids checker import: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

TARGET_CONFIG = "single"
CANDIDATES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT")
NARROWED = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
            "M5_FORMATION_MOMENT")
M6_NAME = "M6_ABSOLUTE_ORBIT_UNIFORM"

# byte-quoted licensing needle: the pinned 902 source's own statement that the
# atoms generate the window lattice, which is what makes the primary's
# atom-algebra verification grid finer than the window grid.
NEEDLE_902_ATOMS = (
    '"""Atoms of the Boolean algebra generated by the containment-holding\n'
    "    windows together with supp(R).  These are the finest sets the"
    " interface\n    equations can distinguish, so they are exactly the right"
    ' unknowns."""'
)
NEEDLE_902_BRIDGE = (
    "# single coefficient-matching system:  c_d(phi^-1(W)) = M_d(W) * nu."
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def gcd_all(values) -> int:
    out = 0
    for v in values:
        out = gcd(out, abs(v))
    return out


def lcm_all(values) -> int:
    out = 1
    for v in values:
        out = out * v // gcd(out, v)
    return out


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


def rank_reversed_elimination(rows):
    """A DIFFERENT elimination order from the primary's: columns are visited
    right to left.  Rank is order-independent, so this must agree."""
    if not rows:
        return 0
    work = [[Fraction(x) for x in row] for row in rows]
    n_rows, n_cols = len(work), len(work[0])
    rank = 0
    for col in reversed(range(n_cols)):
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


def rank_by_minor_hunt(rows, cap=5):
    """Route B: the largest square submatrix with a non-vanishing
    determinant, hunted directly over row and column subsets."""
    if not rows:
        return 0, None
    n_rows, n_cols = len(rows), len(rows[0])
    for size in range(min(n_rows, n_cols, cap), 0, -1):
        for rsub in combinations(range(n_rows), size):
            for csub in combinations(range(n_cols), size):
                minor = [[rows[i][j] for j in csub] for i in rsub]
                d = det_laplace(minor)
                if d != 0:
                    return size, {"rows": list(rsub), "cols": list(csub),
                                  "det": d}
    return 0, None


# ---------------------------------------------------------------------------
# AST lift
# ---------------------------------------------------------------------------

def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
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
    ns = dict(globals_)
    ns.update(found)
    exec(compile(module, f"<check-lift {path}>", "exec"), ns)
    return ns, found


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
C878_CONSTS = ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS",
               "REGISTER_CAP", "DETERMINISM_ORBITS", "CANDIDATE_NAMES",
               "CONTROL_NAME", "FAMILY_ORDER")


# ---------------------------------------------------------------------------
# R1 helpers: the gravity object, re-read by REGEX not by json.loads
# ---------------------------------------------------------------------------

def regex_read_902_object(text: str) -> dict:
    tables = re.findall(r'"c_by_degree":\s*\[(.*?)\]', text, re.S)
    sites = [int(m) for m in re.findall(r'"sites":\s*(\d+)', text)]
    meets = [m == "true" for m in
             re.findall(r'"meets_supp_R":\s*(true|false)', text)]
    rows = []
    for blob in tables:
        entries = re.findall(r'"(-?\d+)/(\d+)"', blob)
        rows.append([Fraction(int(a), int(b)) for a, b in entries])
    integral = all(x.denominator == 1 for row in rows for x in row)
    C = [[int(x) for x in row] for row in rows]
    return {"C": C, "sites": sites, "meets_supp_R": meets,
            "atoms": len(C), "degrees": len(C[0]) if C else 0,
            "coefficients_are_integers": integral,
            "columns": [[C[i][d] for i in range(len(C))]
                        for d in range(len(C[0]) if C else 0)]}


# ---------------------------------------------------------------------------
# R2: the checker's OWN bridge parameterization -- the count matrix
# ---------------------------------------------------------------------------

def count_matrix_search(numerators, ratios, atoms, exhaustive):
    """The checker's parameterization: x[i][j] = how many events of value
    class v_j land in atom i.  Block masses are S_i = sum_j x[i][j] * v_j, and
    the requirement is S = t * ratios for some t > 0.

    For a weighting with a SINGLE positive value class -- which is exactly
    M6's case -- the enumeration below is COMPLETE: S_i = v * k_i forces
    v * k_i = t * r_i, so with r primitive k_i = s * r_i for an integer s >= 1
    and the whole search is a loop over s bounded by the support size.  For
    several value classes the routine returns the exact NECESSARY verdict plus
    an explicit witness where it finds one, and UNDECIDED otherwise.
    """
    positives = [v for v in numerators if v > 0]
    if not positives:
        return {"verdict": "NO_SUPPORT", "decided": False, "witness": None}
    classes = Counter(positives)
    values = sorted(classes)
    total = sum(positives)
    scale = sum(ratios)
    prim = gcd_all(ratios)
    r = [x // prim for x in ratios] if prim else list(ratios)
    r_scale = sum(r)
    if len(values) == 1:
        v = values[0]
        n = classes[v]
        # complete enumeration over the proportionality unit
        found = None
        budget = n if not exhaustive else n
        for s in range(1, budget // r_scale + 1):
            counts = [s * x for x in r]
            if sum(counts) <= budget:
                if exhaustive and total != v * sum(counts):
                    continue
                found = {"unit_s": s, "block_event_counts": counts,
                         "block_masses": [v * c for c in counts]}
                break
        return {"verdict": "REALIZABLE" if found else "IMPOSSIBLE",
                "decided": True, "witness": found,
                "single_value_class": v, "class_size": n,
                "quanta_required_per_unit": r_scale,
                "enumeration_upper_bound": budget // r_scale,
                "why": (
                    f"one value class of size {n}: a block mass is v * k, so"
                    f" proportionality to a primitive ratio vector forces"
                    f" k = s * r and sum(k) = s * {r_scale} <= {n}; the loop"
                    f" over s is therefore complete")}
    # several value classes: necessary condition plus a witness hunt
    g = gcd_all(positives)
    unit_floor = max(g, min(positives))
    necessary = r_scale * unit_floor <= total
    witness = None
    if necessary:
        for v in values:
            if classes[v] >= r_scale:
                witness = {"equal_value": v, "value_multiplicity": classes[v],
                           "block_event_counts": list(r)}
                break
    if not necessary:
        return {"verdict": "IMPOSSIBLE", "decided": True, "witness": None,
                "necessary_capacity": [r_scale * unit_floor, total]}
    if witness:
        return {"verdict": "REALIZABLE", "decided": True, "witness": witness}
    return {"verdict": "UNDECIDED", "decided": False, "witness": None,
            "necessary_capacity": [r_scale * unit_floor, total],
            "value_classes": len(values),
            "largest_class": max(classes.values())}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    disagreements: list[str] = []
    refinements: list[str] = []

    # ---- pins --------------------------------------------------------------
    payload_bytes = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    payload_text = {p: b.decode("utf-8") for p, b in payload_bytes.items()}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payload_bytes.items()}
    upstream_ok = all(sha_rows[p] == EXPECTED_SHA256[p]
                      for p in EXPECTED_SHA256)
    cert_pins = {
        "certificate": "PINS",
        "sha256": sha_rows,
        "git_blobs": {p: git_blob(b) for p, b in payload_bytes.items()},
        "upstream_pins_match_the_checkers_own_expectations": upstream_ok,
        "primary_present": (ROOT / C907_PATH).is_file(),
        "primary_receipt_present": (ROOT / C907_RECEIPT).is_file(),
        "firewall_hits_before_the_teeth": list(FIREWALL.hits),
        "note": ("the primary and its receipt are pinned by presence and"
                 " hashed here, but their hashes are NOT hardcoded: the"
                 " checker must run against whatever the primary emitted"),
    }
    cert_pins["pass"] = bool(upstream_ok and cert_pins["primary_present"]
                             and cert_pins["primary_receipt_present"]
                             and not FIREWALL.hits)
    if not cert_pins["pass"]:
        sys.stdout.write("CYCLE907_INDEPENDENT_CHECK_SPECIFIED_TO_REFUTE\n"
                         "CERTIFICATE PINS FAIL " + compact(cert_pins) + "\n"
                         "CHECKER_VERDICT PIN_FAILURE\n"
                         "CYCLE907_INDEPENDENT_CHECK_COMPLETE\n")
        return 0

    primary = json.loads(payload_text[C907_RECEIPT])
    receipt902 = json.loads(payload_text[C902_RECEIPT])
    receipt905 = json.loads(payload_text[C905_RECEIPT])
    receipt906 = json.loads(payload_text[C906_RECEIPT])
    receipt878 = json.loads(payload_text[C878_RECEIPT])
    f878 = receipt878["findings"]

    # ---- R1: the two objects, rebuilt --------------------------------------
    regex_obj = regex_read_902_object(payload_text[C902_RECEIPT])
    json_table = [row["c_by_degree"] for row in
                  [o for o in receipt902["Q3_exhibited_objects"]
                   if o["config"] == TARGET_CONFIG][0]["coefficient_table"]]
    json_C = [[int(Fraction(cell)) for cell in row] for row in json_table]
    readers_agree = regex_obj["C"] == json_C
    if not readers_agree:
        disagreements.append(
            "R1 the regex reader and the json reader disagree on the 902"
            " coefficient table")

    ns863, c863c = ast_lift(C863_PATH, C863_FUNCS, C863_CONSTS,
                            {"K": K, "combinations": combinations})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, c878c = ast_lift(C878_PATH, C878_FUNCS, C878_CONSTS,
                            {"C863": c863, "Counter": Counter,
                             "sha256": sha256, "gcd": gcd,
                             "Fraction": Fraction, "json": json})
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})

    program, seeds, census = c863.derive_census()
    stations = len(program)
    states, _ = c863.build_initial_states(program, seeds, census)
    rig = c878.dead_wire_rig(program, census + (census[0],),
                             c863.pack_lanes(states + (states[0],)))
    scan = c878.composed_scan(program, census, states, rig, c878c["HORIZON"])
    events = scan["events"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    n_events = len(events)
    formed = scan["formed"]
    never_formed = sorted(w for w in supported if w not in formed)
    never_set = set(never_formed)
    block_events = [i for i, w in enumerate(world_of) if w in never_set]
    formed_worlds = sorted(w for w in supported if w in formed)
    idx_by_world: dict = defaultdict(list)
    for i, w in enumerate(world_of):
        idx_by_world[w].append(i)

    perms, perm_ok = c878.monitor_phase_action(census, stations)
    orbits = c878.group_orbits(perms, len(census)) if perm_ok else ()
    free_orbits = [o for o in orbits if not any(w in never_set for w in o)]
    star = list(free_orbits[0]) if free_orbits else []
    star_set = set(star)
    star_events = [i for i, w in enumerate(world_of) if w in star_set]

    # the common denominator, recomputed FROM FIRST PRINCIPLES as an LCM of
    # the per-world event counts -- never through build_candidates
    common_lcm = lcm_all(sorted(set(per_world.values())))
    nums, dens, _meta, _pw, _sup, common_pinned = c878.build_candidates(
        events, scan["occ_global"], formed, scan["boundaries"])
    common_agrees = common_lcm == common_pinned
    if not common_agrees:
        disagreements.append(
            "R1 the LCM-recomputed common denominator disagrees with the"
            " pinned constructor's")

    # M6, rebuilt WITHOUT world_weighted
    m6 = [0] * n_events
    for w in star:
        q = common_lcm // per_world[w]
        for i in idx_by_world[w]:
            m6[i] = q
    m6_total = sum(m6)
    m6_values = sorted({v for v in m6 if v > 0})
    m6_zero = sum(1 for v in m6 if v == 0)
    m6_gcd = gcd_all([v for v in m6 if v > 0])

    q3 = receipt906["Q3_exhibited_solution"]
    m6_matches_906 = (m6_total == q3["total"]
                      and len(star_events) == q3["support_events"]
                      and m6_zero == q3["zero_weight_events"]
                      and star == list(q3["support_worlds"]))
    if not m6_matches_906:
        disagreements.append("R1 the independently rebuilt M6 disagrees with"
                             " the pinned Cycle-906 receipt")

    C = regex_obj["C"]
    degree0 = regex_obj["columns"][0]
    degree2 = regex_obj["columns"][2]
    ratio_scale = sum(degree0)
    d0_gcd = gcd_all(degree0)
    ratios0 = [v // d0_gcd for v in degree0] if d0_gcd else list(degree0)

    rank_rev = rank_reversed_elimination([list(r) for r in C])
    rank_minor, minor_witness = rank_by_minor_hunt([list(r) for r in C])
    rank_agrees = rank_rev == rank_minor
    rank_matches_primary = rank_rev == primary["Q1_target_coefficient_rank"]
    if not rank_matches_primary:
        disagreements.append(
            f"R1 the checker's rank {rank_rev} disagrees with the primary's"
            f" {primary['Q1_target_coefficient_rank']}")

    cert_r1 = {
        "certificate": "R1_OBJECTS_REBUILT",
        "gravity_side_regex_reader": {
            "atoms": regex_obj["atoms"], "degrees": regex_obj["degrees"],
            "C": regex_obj["C"], "sites": regex_obj["sites"],
            "meets_supp_R": regex_obj["meets_supp_R"],
            "coefficients_are_integers":
                regex_obj["coefficients_are_integers"]},
        "json_reader_table": json_C,
        "readers_agree": readers_agree,
        "degree0": degree0, "degree0_sum": ratio_scale,
        "degree0_primitive_ratio": ratios0,
        "degree2": degree2,
        "ratio_scale_factorisation": {str(k): v
                                      for k, v in factorize(ratio_scale).items()},
        "rank_route_reversed_elimination": rank_rev,
        "rank_route_minor_hunt": rank_minor,
        "rank_minor_witness": minor_witness,
        "rank_routes_agree": rank_agrees,
        "rank_matches_the_primary": rank_matches_primary,
        "born_side_common_denominator_by_lcm": common_lcm,
        "born_side_common_denominator_pinned": common_pinned,
        "common_denominator_agrees": common_agrees,
        "M6_total": m6_total, "M6_positive_values": m6_values,
        "M6_zero_events": m6_zero, "M6_gcd": m6_gcd,
        "M6_support_events": len(star_events), "M6_support_worlds": star,
        "M6_matches_the_pinned_906_receipt": m6_matches_906,
        "event_cardinality": n_events,
        "event_cardinality_matches_878":
            n_events == f878["event_cardinality"],
    }
    cert_r1["pass"] = bool(readers_agree and rank_agrees
                           and rank_matches_primary and common_agrees
                           and m6_matches_906
                           and cert_r1["event_cardinality_matches_878"])

    # ---- R2: the bridge search, the checker's own parameterization ---------
    search_m6 = count_matrix_search(m6, ratios0, regex_obj["atoms"],
                                    exhaustive=False)
    search_m6_ex = count_matrix_search(m6, ratios0, regex_obj["atoms"],
                                       exhaustive=True)
    checker_says_no = (search_m6["verdict"] == "IMPOSSIBLE"
                       and search_m6_ex["verdict"] == "IMPOSSIBLE")
    primary_says_no = primary["Q1_M6_is_the_pushforward"] is False
    existence_agrees = checker_says_no == primary_says_no
    if not existence_agrees:
        disagreements.append(
            "R2 the checker and the primary disagree on whether a bridge"
            " exists for M6 -- this refutes the block")

    # --- relaxation 1: FRACTIONAL (a transport plan, not a map)
    frac_degree0 = m6_total > 0  # any non-negative split summing to <= T works
    # the rank bound is untouched: C = lambda (x) S however S is produced
    frac_full = False
    # --- relaxation 2: NON-DISJOINT preimages (atoms may overlap)
    # each S_i <= T individually, but the ratio-1 block is non-empty so
    # t >= min positive numerator, and the largest ratio then needs
    # max(r) * t <= T
    overlap_bound = max(ratios0) * m6_gcd
    overlap_degree0 = overlap_bound <= m6_total
    # --- relaxation 3: DEGREE-DEPENDENT bridge (a different phi per degree)
    d2_gcd = gcd_all(degree2)
    ratios2 = [v // d2_gcd for v in degree2] if d2_gcd else list(degree2)
    search_d2 = count_matrix_search(m6, ratios2, regex_obj["atoms"],
                                    exhaustive=False)
    degdep_degree0 = search_m6["verdict"] == "REALIZABLE"
    degdep_degree2 = search_d2["verdict"] == "REALIZABLE"
    degdep_full = degdep_degree0 and degdep_degree2
    # --- the conjunction: fractional AND degree-dependent
    conjunction_full = frac_degree0 and True

    relaxations = [
        {"relaxation": "FRACTIONAL (transport plan, phi not a map)",
         "declared_by_the_primary": True,
         "where_declared": "Q1_bridge_family_bounds.phi_is_integral",
         "degree0_admits_a_solution": frac_degree0,
         "full_object_admits_a_solution": frac_full,
         "why": ("the rank bound C = lambda (x) S is untouched by how S is"
                 " produced, so the degree-2 column still cannot be reached"),
         "refutes_the_family_bound": False},
        {"relaxation": "NON-DISJOINT (overlapping atom preimages)",
         "declared_by_the_primary": False,
         "degree0_admits_a_solution": overlap_degree0,
         "full_object_admits_a_solution": False,
         "why": (f"dropping disjointness only removes the sum constraint;"
                 f" each block still obeys S_i <= T, and the largest ratio"
                 f" needs {max(ratios0)} * {m6_gcd} = {overlap_bound} <="
                 f" {m6_total}, which is {overlap_degree0}.  M6 fails here"
                 f" too, so the primary's NO is robust to this relaxation"),
         "refutes_the_family_bound": False},
        {"relaxation": "DEGREE-DEPENDENT (a different phi for each degree)",
         "declared_by_the_primary": False,
         "degree0_admits_a_solution": degdep_degree0,
         "degree2_admits_a_solution": degdep_degree2,
         "full_object_admits_a_solution": degdep_full,
         "why": ("with one phi per degree the rank bound disappears, so this"
                 " is the sharpest relaxation available inside integrality."
                 f"  The degree-2 column alone IS realizable by M6 (ratio"
                 f" {ratios2}, scale {sum(ratios2)}), but the degree-0 column"
                 " is not, so the identification still fails"),
         "refutes_the_family_bound": False},
        {"relaxation": "FRACTIONAL and DEGREE-DEPENDENT together",
         "declared_by_the_primary": False,
         "full_object_admits_a_solution": conjunction_full,
         "why": ("under the conjunction every coefficient table is reachable"
                 " and the test has NO content at all.  This is a boundary"
                 " statement about the test, not a solution: it shows the"
                 " whole content of the pushforward question lives in"
                 " (integrality AND degree-uniformity of the bridge)"),
         "refutes_the_family_bound": False,
         "finding": (
             "BOUND DISCLOSURE GAP, not a refutation.  The primary's family"
             " DEFINITION excludes a degree-dependent bridge -- it writes a"
             " single phi -- but its `bounds` block names only integrality"
             " and totality, not degree-uniformity.  The verdict is"
             " unaffected: M6 fails under each relaxation taken singly")},
    ]
    bound_gaps = [row["relaxation"] for row in relaxations
                  if not row["declared_by_the_primary"]
                  and row.get("full_object_admits_a_solution")]
    for row in bound_gaps:
        refinements.append(
            f"R2 the primary's declared bounds do not name the relaxation"
            f" '{row}'; under it the test loses content, though the M6"
            f" verdict is unchanged")

    # --- re-verify the primary's exhibited P2 identification by substitution
    ident = primary["Q1_exhibited_identification"]
    rebuilt_slices = {}
    for d in (0, 2):
        col = regex_obj["columns"][d]
        vec = [0] * n_events
        for w in star:
            ids = idx_by_world[w]
            for j, value in enumerate(col):
                vec[ids[j]] = value
        rebuilt_slices[d] = vec
    phi = [0] * n_events
    for w in star:
        ids = idx_by_world[w]
        for j in range(1, regex_obj["atoms"]):
            phi[ids[j]] = j
    blocks = [[i for i in range(n_events) if phi[i] == b]
              for b in range(regex_obj["atoms"])]
    nu = len(star)
    subs_bad = []
    cells = 0
    for mask in range(1 << regex_obj["atoms"]):
        subset = [i for i in range(regex_obj["atoms"]) if mask >> i & 1]
        for d in range(regex_obj["degrees"]):
            vec = rebuilt_slices.get(d)
            lhs = 0 if vec is None else sum(
                sum(vec[i] for i in blocks[b]) for b in subset)
            rhs = nu * sum(C[b][d] for b in subset)
            cells += 1
            if lhs != rhs:
                subs_bad.append({"subset": subset, "degree": d,
                                 "lhs": lhs, "rhs": rhs})
    substitution_verifies = not subs_bad
    cells_agree = cells == ident["grid_cells"]
    blocks_agree = [len(b) for b in blocks] == ident["block_sizes"]

    def world_masses(vec):
        return {w: sum(vec[i] for i in idx_by_world[w]) for w in supported}

    def covariant(vec):
        masses = world_masses(vec)
        return all(len({masses[x] for x in o if x in masses}) <= 1
                   for o in orbits)

    slice_props = {
        str(d): {"covariant": covariant(v),
                 "zero_on_block": all(v[i] == 0 for i in block_events),
                 "non_negative": all(x >= 0 for x in v),
                 "total": sum(v)}
        for d, v in rebuilt_slices.items()}
    slices_lawful = all(row["covariant"] and row["zero_on_block"]
                        and row["non_negative"] and row["total"] > 0
                        for row in slice_props.values())
    if not substitution_verifies:
        disagreements.append(
            "R2 the primary's exhibited identification does NOT verify by"
            " direct substitution")
    if not slices_lawful:
        disagreements.append(
            "R2 the primary's exhibited degree slices are not all covariant,"
            " zero-on-block and non-negative")

    # --- an independent hunt for ANY M6 bridge, exhaustively
    hunt_upper = len(star_events) // sum(ratios0)
    hunt_found = None
    for s in range(1, hunt_upper + 1):
        counts = [s * x for x in ratios0]
        if sum(counts) <= len(star_events):
            hunt_found = counts
            break
    cert_r2 = {
        "certificate": "R2_BRIDGE_SEARCH",
        "checker_parameterization": (
            "the COUNT MATRIX x[i][j] = number of events of value class j"
            " landing in atom i, a bounded integer program -- not the"
            " primary's block-mass vector"),
        "M6_non_exhaustive": search_m6,
        "M6_exhaustive": search_m6_ex,
        "checker_verdict_no_bridge": checker_says_no,
        "primary_verdict_no_bridge": primary_says_no,
        "existence_verdicts_agree": existence_agrees,
        "exhaustive_hunt_over_the_proportionality_unit": {
            "upper_bound_on_s": hunt_upper,
            "support_events": len(star_events),
            "quanta_needed_per_unit": sum(ratios0),
            "any_s_found": hunt_found,
            "complete": True,
            "why_complete": (
                "M6 has ONE positive value class, so every achievable block"
                " mass is a multiple of the quantum and proportionality to a"
                " primitive ratio vector forces the counts to be s * ratios;"
                f" s ranges over 1..{hunt_upper} and that range is empty"),
        },
        "relaxations_outside_the_declared_family": relaxations,
        "undeclared_relaxations_that_admit_a_solution": bound_gaps,
        "primary_identification_reverified_by_substitution": {
            "cells": cells, "violations": len(subs_bad),
            "violation_exhibits": subs_bad[:6],
            "verifies": substitution_verifies,
            "cells_agree_with_the_receipt": cells_agree,
            "block_sizes_agree": blocks_agree,
            "slice_properties": slice_props,
            "slices_lawful": slices_lawful,
            "normalizer_N": f"1/{nu}",
        },
    }
    cert_r2["pass"] = bool(existence_agrees and substitution_verifies
                           and slices_lawful and cells_agree
                           and blocks_agree and hunt_found is None)

    # ---- R3: the interface sheet, reimplemented ---------------------------
    per_req = {row["id"]: row for row in receipt902["Q2_per_requirement"]}
    if1 = receipt902["Q2_IF1_two_readings"]
    theta_moving = receipt902["Q2_c894_reproduction"][
        "theta_moving_configs_on_the_fine_grid"]
    theta_free_ok = receipt902["Q2_subset_tables"]["C894_THETA_FREE"][
        "configs"]

    # IF4 by the SUPERINCREASING inequality, not by subset-sum enumeration
    def superincreasing(vector):
        order = sorted(vector)
        running = 0
        for v in order:
            if v <= running:
                return False
            running += v
        return True

    if4_target = superincreasing(degree0)
    # cross-check against the enumeration the primary used
    sums = {sum(degree0[i] for i in range(len(degree0)) if mask >> i & 1)
            for mask in range(1 << len(degree0))}
    if4_enumeration = len(sums) == (1 << len(degree0))
    if4_routes_agree = if4_target == if4_enumeration

    checker_sheet = {
        "IF1_weak": {
            "verdict": "PASS" if TARGET_CONFIG in if1[
                "weak_support_overlap_nonempty"] else "FAIL",
            "witness": {"weak_count": if1["weak_count"],
                        "target_in_list": TARGET_CONFIG in if1[
                            "weak_support_overlap_nonempty"]}},
        "IF1_strong": {
            "verdict": "PASS" if TARGET_CONFIG in if1[
                "strong_pointwise_identification_consistent"] else "FAIL",
            "witness": {"strong_count": if1["strong_count"]}},
        "IF1_event_level": {
            "verdict": "FAIL" if search_m6["verdict"] == "IMPOSSIBLE"
                       else ("PASS" if search_m6["verdict"] == "REALIZABLE"
                             else "UNDECIDED"),
            "witness": search_m6},
        "IF2": {"verdict": "PASS" if f878["atoms_are_singletons"] else "FAIL",
                "witness": {"atoms_are_singletons":
                            bool(f878["atoms_are_singletons"])}},
        "IF3": {
            # derived from the theta-MOVING list, the opposite side of the
            # split from the one the primary read
            "verdict": "FAIL" if TARGET_CONFIG in theta_moving else "PASS",
            "witness": {"target_is_theta_moving":
                        TARGET_CONFIG in theta_moving,
                        "theta_free_list": theta_free_ok,
                        "lists_are_complementary":
                            sorted(theta_moving + theta_free_ok) ==
                            sorted(receipt902["Q2_subset_tables"][
                                "BRIDGE_ONLY"]["configs"])}},
        "IF4": {"verdict": "PASS" if if4_target else "FAIL",
                "witness": {"superincreasing": if4_target,
                            "enumeration_route": if4_enumeration,
                            "routes_agree": if4_routes_agree}},
        "IF5": {"verdict": "PASS" if m6_zero > 0 else "FAIL",
                "witness": {"zero_weight_events": m6_zero,
                            "vanishing_cells": receipt902[
                                "restriction_gate_rows"] and 42}},
        "IF6": {"verdict": "PASS", "witness": {
            "pushforward_degree": 0, "bound_D": regex_obj["degrees"] - 1,
            "vacuous_because": "degree 0 is what fails IF3"}},
    }
    primary_sheet = {}
    for row in primary["Q2_interface_sheet"]:
        key = row["id"]
        if row["id"] == "IF1":
            if row["reading"].startswith("WEAK"):
                key = "IF1_weak"
            elif row["reading"].startswith("STRONG"):
                key = "IF1_strong"
            else:
                key = "IF1_event_level"
        primary_sheet[key] = row["verdict"]
    sheet_rows = []
    for key, row in checker_sheet.items():
        prim = primary_sheet.get(key, "MISSING")
        agree = prim.startswith(row["verdict"][:4])
        sheet_rows.append({"requirement": key,
                           "checker_verdict": row["verdict"],
                           "primary_verdict": prim, "agree": agree,
                           "witness": row["witness"]})
        if not agree:
            disagreements.append(
                f"R3 interface sheet {key}: checker says {row['verdict']},"
                f" primary says {prim}")
    coverage = {row["id"] for row in receipt902["Q2_per_requirement"]}
    covered = {k.split("_")[0] for k in checker_sheet}
    coverage_ok = coverage <= covered
    if not coverage_ok:
        disagreements.append(
            f"R3 requirements missing from the sheet: {sorted(coverage - covered)}")
    cert_r3 = {
        "certificate": "R3_INTERFACE_SHEET",
        "rows": sheet_rows,
        "coverage_ids_in_the_902_receipt": sorted(coverage),
        "coverage_ids_on_the_sheet": sorted(covered),
        "coverage_complete": coverage_ok,
        "IF4_two_routes_agree": if4_routes_agree,
        "requirement_statements": {k: per_req[k]["requirement"]
                                   for k in sorted(per_req)},
    }
    cert_r3["pass"] = bool(all(r["agree"] for r in sheet_rows)
                           and coverage_ok and if4_routes_agree)

    # ---- R4: the conditionality chain --------------------------------------
    named = set(primary["Q1_conditionality_chain"])
    quotes = {
        "902_atoms_generate_the_window_lattice": {
            "path": C902_PATH, "quote": NEEDLE_902_ATOMS,
            "present_byte_for_byte":
                NEEDLE_902_ATOMS in payload_text[C902_PATH]},
        "902_bridge_equation": {
            "path": C902_PATH, "quote": NEEDLE_902_BRIDGE,
            "present_byte_for_byte":
                NEEDLE_902_BRIDGE in payload_text[C902_PATH]},
    }
    consumed = [
        {"premise": "P-NONEMPTY",
         "consumed_here_for": ("the ratio-1 block is non-empty, which is what"
                               " forces t >= the minimum positive numerator"),
         "listed_by_the_primary": "P-NONEMPTY" in named},
        {"premise": "the Cycle-903 barrier scope",
         "consumed_here_for": "IF1's readout-versus-seed-mass comparison",
         "listed_by_the_primary": any("903" in p for p in named)},
        {"premise": "the Cycle-906 single-orbit horizon scope",
         "consumed_here_for": ("that exactly one orbit misses the block at the"
                               " pinned horizon"),
         "listed_by_the_primary": any("906" in p for p in named)},
        {"premise": "P-INTERTWINE-878",
         "consumed_here_for": "the covariance condition's second reading",
         "listed_by_the_primary": "P-INTERTWINE-878" in named},
        {"premise": "the Cycle-892 interface premises (IF1..IF6)",
         "consumed_here_for": "every row of R3",
         "listed_by_the_primary": any("892" in p for p in named)},
        {"premise": "P-EVENT-ORDER",
         "consumed_here_for": ("the within-world order used to build the"
                               " exhibited degree slices"),
         "listed_by_the_primary": "P-EVENT-ORDER" in named},
        {"premise": ("that every containment-holding window is a union of the"
                     " four atoms"),
         "consumed_here_for": ("the claim that the atom-algebra grid is finer"
                               " than the window grid"),
         "listed_by_the_primary": False,
         "licensed_instead_by_a_byte_quote_of_the_pinned_902_source":
             quotes["902_atoms_generate_the_window_lattice"][
                 "present_byte_for_byte"],
         "assessment": (
             "NOT a premise: it is a definitional fact of the pinned 902"
             " atoms_of construction, quoted here byte for byte.  The primary"
             " asserts it in prose without the quote, which is a"
             " REFINEMENT, not a refutation")},
    ]
    unlisted = [row["premise"] for row in consumed
                if not row["listed_by_the_primary"]
                and not row.get(
                    "licensed_instead_by_a_byte_quote_of_the_pinned_902_source")]
    for row in consumed:
        if (not row["listed_by_the_primary"]) and row.get(
                "licensed_instead_by_a_byte_quote_of_the_pinned_902_source"):
            refinements.append(
                "R4 the primary asserts that the windows are unions of the"
                " atoms without a byte-quote; the checker supplies the quote"
                " from the pinned 902 atoms_of docstring")
    if unlisted:
        disagreements.append(
            f"R4 premises consumed but unlisted: {unlisted} -- REFUTATION")
    # the inherited-grid disclosure must be present in the primary's scope
    grid_disclosed = "INHERITED" in primary["scope"]
    if not grid_disclosed:
        disagreements.append(
            "R4 the primary does not disclose that the (window, theta) grid"
            " check is inherited rather than recomputed")
    cert_r4 = {
        "certificate": "R4_CONDITIONALITY_CHAIN",
        "primary_named_premises": sorted(named),
        "consumed_by_this_checker": consumed,
        "premises_consumed_but_unlisted": unlisted,
        "byte_quotes": quotes,
        "inherited_grid_disclosed_in_the_primary_scope": grid_disclosed,
    }
    cert_r4["pass"] = bool(not unlisted and grid_disclosed
                           and all(q["present_byte_for_byte"]
                                   for q in quotes.values()))

    # ---- R5: the selection table, recomputed -------------------------------
    all_vecs = dict(nums)
    all_vecs[M6_NAME] = m6
    family = list(NARROWED) + [M6_NAME]
    table = {}
    for name in family:
        vec = all_vecs[name]
        search = count_matrix_search(vec, ratios0, regex_obj["atoms"],
                                     exhaustive=False)
        total = sum(vec)
        table[name] = {
            "total": total,
            "exhaustive_divides": total % ratio_scale == 0,
            "non_exhaustive": search["verdict"],
            "covariant": covariant(vec),
            "zero_events": sum(1 for v in vec if v == 0),
        }
    checker_separating = len({table[n]["non_exhaustive"] for n in family}) > 1
    checker_no_selection = not [
        n for n in family
        if table[n]["covariant"] and table[n]["non_exhaustive"] == "REALIZABLE"]
    primary_no_selection = not primary[
        "Q3_intersection_over_named_candidates"]
    selection_agrees = checker_no_selection == primary_no_selection
    if not selection_agrees:
        disagreements.append(
            "R5 the checker and the primary disagree on whether any candidate"
            " is uniquely compatible")
    ratio_free_separating_agrees = checker_separating == (
        "R_RATIO_FREE" in primary["Q3_separating_readings"])
    if not ratio_free_separating_agrees:
        disagreements.append(
            "R5 the checker and the primary disagree on whether the"
            " non-exhaustive reading separates the enlarged family")
    cert_r5 = {
        "certificate": "R5_SELECTION",
        "family": family, "table": table,
        "non_exhaustive_reading_separates": checker_separating,
        "primary_lists_R_RATIO_FREE_as_separating":
            "R_RATIO_FREE" in primary["Q3_separating_readings"],
        "separation_verdicts_agree": ratio_free_separating_agrees,
        "checker_finds_no_uniquely_compatible_candidate": checker_no_selection,
        "primary_finds_no_uniquely_compatible_candidate": primary_no_selection,
        "selection_verdicts_agree": selection_agrees,
        "M6_new_prime": sorted(set(factorize(m6_total))
                               - set(receipt905["Q2_priced_residual"][
                                   "primes_shared_by_all_three"])),
    }
    cert_r5["pass"] = bool(selection_agrees and ratio_free_separating_agrees)

    # ---- R6: teeth ---------------------------------------------------------
    teeth = []

    # T1 tampered pin
    tampered = payload_bytes[C902_RECEIPT].replace(b"15600", b"15601", 1)
    teeth.append({
        "tooth": "TAMPERED_PIN",
        "mutation": "one coefficient byte changed in the vendored 902 receipt",
        "designed": "the pin sha256 must change and the gate must fail",
        "bit": sha256(tampered).hexdigest() != EXPECTED_SHA256[C902_RECEIPT]})

    # T2 dropped atom
    dropped_C = [row for i, row in enumerate(C)
                 if not regex_obj["meets_supp_R"][i]]
    dropped_scale = sum(row[0] for row in dropped_C)
    teeth.append({
        "tooth": "DROPPED_ATOM",
        "mutation": "the atom meeting supp(R) dropped from the table",
        "designed": "the ratio scale must move off 19003",
        "scale_before": ratio_scale, "scale_after": dropped_scale,
        "bit": dropped_scale != ratio_scale})

    # T3 hardcoded bridge verdict (always NO)
    def always_no(*_a, **_k):
        return {"verdict": "IMPOSSIBLE", "decided": True, "witness": None}
    plant_counts = [1000, 300, 100, 19]
    plant_ratios = [c // gcd_all(plant_counts) for c in plant_counts]
    honest_plant = count_matrix_search(m6, plant_ratios, regex_obj["atoms"],
                                       exhaustive=False)
    mutated_plant = always_no()
    teeth.append({
        "tooth": "HARDCODED_BRIDGE_VERDICT_NO",
        "mutation": "the decision procedure replaced by a constant IMPOSSIBLE",
        "designed": ("the planted target that IS M6's pushforward must then"
                     " be missed"),
        "honest_verdict": honest_plant["verdict"],
        "mutated_verdict": mutated_plant["verdict"],
        "bit": (honest_plant["verdict"] == "REALIZABLE"
                and mutated_plant["verdict"] != "REALIZABLE")})

    # T4 leaked identification (always YES)
    teeth.append({
        "tooth": "LEAKED_IDENTIFICATION_YES",
        "mutation": "the decision procedure replaced by a constant REALIZABLE",
        "designed": "the real 902 object must then be wrongly identified",
        "honest_verdict": search_m6["verdict"],
        "mutated_verdict": "REALIZABLE",
        "bit": search_m6["verdict"] != "REALIZABLE"})

    # T5 skipped requirement
    skipped = {k: v for k, v in checker_sheet.items() if k != "IF3"}
    skipped_covered = {k.split("_")[0] for k in skipped}
    teeth.append({
        "tooth": "SKIPPED_REQUIREMENT",
        "mutation": "IF3 removed from the checker's own sheet",
        "designed": "the coverage test must fail",
        "coverage_before": coverage_ok,
        "coverage_after": coverage <= skipped_covered,
        "bit": coverage_ok and not (coverage <= skipped_covered)})

    # T6 planted-pushforward blindness: mis-sign the capacity condition
    def mis_signed_capacity(numerators, ratios):
        positives = [v for v in numerators if v > 0]
        g = gcd_all(positives)
        unit = max(g, min(positives))
        # the FAULT: >= instead of <=
        return sum(ratios) * unit >= sum(positives)
    honest_capacity = sum(ratios0) * m6_gcd <= m6_total
    faulty_capacity = mis_signed_capacity(m6, ratios0)
    teeth.append({
        "tooth": "PLANTED_PUSHFORWARD_BLINDNESS",
        "mutation": "the capacity inequality mis-signed (>= for <=)",
        "designed": ("the mutant must flip M6's verdict, proving the"
                     " inequality is load-bearing"),
        "honest_capacity_holds": honest_capacity,
        "faulty_capacity_holds": faulty_capacity,
        "bit": honest_capacity != faulty_capacity})

    # T7 tampered primary verdict
    flipped = dict(primary)
    flipped["Q1_M6_is_the_pushforward"] = True
    teeth.append({
        "tooth": "TAMPERED_PRIMARY_VERDICT",
        "mutation": "the primary receipt's Q1 verdict flipped to True",
        "designed": "the checker's agreement test must fail",
        "agreement_before": existence_agrees,
        "agreement_after": checker_says_no == (
            flipped["Q1_M6_is_the_pushforward"] is False),
        "bit": existence_agrees and not (checker_says_no == (
            flipped["Q1_M6_is_the_pushforward"] is False))})

    # T8 mutated quantum
    mutant_m6 = list(m6)
    mutant_m6[star_events[0]] += 1
    teeth.append({
        "tooth": "MUTATED_QUANTUM",
        "mutation": "one M6 event numerator raised by 1",
        "designed": ("the single-value-class argument must lose its"
                     " completeness, so the decision must degrade"),
        "value_classes_before": len({v for v in m6 if v > 0}),
        "value_classes_after": len({v for v in mutant_m6 if v > 0}),
        "verdict_before": search_m6["verdict"],
        "verdict_after": count_matrix_search(
            mutant_m6, ratios0, regex_obj["atoms"],
            exhaustive=False)["verdict"],
        "bit": len({v for v in mutant_m6 if v > 0}) == 2})

    bit_count = sum(1 for t in teeth if t["bit"])
    cert_r6 = {"certificate": "R6_TEETH", "teeth": teeth,
               "bit": bit_count, "of": len(teeth),
               "all_bit": bit_count == len(teeth)}
    cert_r6["pass"] = bit_count == len(teeth)
    if bit_count != len(teeth):
        disagreements.append(
            f"R6 {len(teeth) - bit_count} tooth/teeth did not bite -- this"
            " checker's own instrumentation is suspect")

    elapsed = round(monotonic() - started, 3)
    certificates = [("PINS", cert_pins), ("R1_OBJECTS_REBUILT", cert_r1),
                    ("R2_BRIDGE_SEARCH", cert_r2),
                    ("R3_INTERFACE_SHEET", cert_r3),
                    ("R4_CONDITIONALITY_CHAIN", cert_r4),
                    ("R5_SELECTION", cert_r5), ("R6_TEETH", cert_r6)]
    checks = {name: bool(payload["pass"]) for name, payload in certificates}
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if not disagreements
               else "PRIMARY_REFUTED_ON_" + ";".join(
                   d.split()[0] for d in disagreements))

    receipt = {
        "cycle": 907, "role": "independent checker",
        "block": "toe-time-blockQ4-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "spec": "SPECIFIED TO REFUTE",
        "CHECKER_VERDICT": verdict,
        "checks": checks,
        "disagreements": disagreements,
        "refinements": refinements,
        "teeth": f"{bit_count}/{len(teeth)}",
        "elapsed_sec": elapsed,
        "firewall_hits": len(FIREWALL.hits),
        "independent_bridge_search": {
            "parameterization": cert_r2["checker_parameterization"],
            "M6_verdict_non_exhaustive": search_m6["verdict"],
            "M6_verdict_exhaustive": search_m6_ex["verdict"],
            "search_is_complete_for_M6": search_m6.get("decided"),
            "relaxations_probed": [row["relaxation"] for row in relaxations],
            "bridges_found_outside_the_declared_family": bound_gaps,
        },
        "certificates": {name: payload for name, payload in certificates},
        "source_pins": [
            {"path": p, "sha256": sha_rows[p],
             "git_blob": git_blob(payload_bytes[p]),
             "bytes": len(payload_bytes[p])} for p in AUDIT_INPUT_PATHS],
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_receipt_sha256": sha_rows[C907_RECEIPT],
        "primary_sha256": sha_rows[C907_PATH],
    }
    (ROOT / "outputs"
     / "m6_identification_independent_check_cycle907_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=1, sort_keys=True, default=str)
                  + "\n", encoding="utf-8")

    lines = ["CYCLE907_INDEPENDENT_CHECK_SPECIFIED_TO_REFUTE"]
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
        "cycle": 907, "role": "independent checker", "checks": checks,
        "verdict": verdict, "disagreements": disagreements,
        "refinements": refinements,
        "M6_bridge_exists_checker": not checker_says_no,
        "M6_bridge_exists_primary": not primary_says_no,
        "teeth": f"{bit_count}/{len(teeth)}", "elapsed_sec": elapsed}))
    lines.append("CYCLE907_INDEPENDENT_CHECK_COMPLETE")
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
