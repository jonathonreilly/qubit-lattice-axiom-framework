#!/usr/bin/env python3
"""Cycle 907: the identification question -- is the gravity-side exhibited
object the pushforward of M6?

Campaign-5 Born LANE CLOSURE, block 4.  Strictly structural.  NO
probability postulate is introduced, NO Born rule is claimed.  Every
fraction emitted here is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

Cycle 902 (vendored) constructed the gravity-side interface object over
the kernel-argument extension: on the `single` configuration an exhibited
(weighting, bridge) pair with four atoms carrying exact degree-coefficient
tables, residual freedom zero once the normalizer is fixed.  Cycle 905
proved that object is not the pushforward of any 878-native weighting
under its R_RATIO_EXHAUSTIVE reading (the ratio scale 19003 = 31 * 613
divides no candidate total).  Cycle 906 exhibited M6_ABSOLUTE_ORBIT_UNIFORM
-- a NEW weighting outside the 878 five, uniform on the 1,419 events of
the eleven worlds of the single monitor-phase orbit that misses the
never-formed block.

Q1  THE PUSHFORWARD TEST, EXACTLY.  Both objects are rebuilt from their
    pinned sources (AST / TEXT / JSON, never imported).  The bridge family
    is DECLARED with its bounds and the existence question is reduced --
    provably, not heuristically -- to a finite question about achievable
    block-mass vectors.  Three readings of the pushforward are computed
    exactly: P0 (the 894 theta-free regime), P1 (a single weighting with a
    fibre vector) and P2 (the full kernel-argument extension, degree slices
    independent).  Both outcomes are reachable: a planted target object
    DESIGNED to be M6's pushforward is run through the same machinery and
    must be identified as such.

Q2  M6'S FULL INTERFACE SHEET.  IF1 (both 902 readings, plus the NEW
    event-level pullback through M6's support), IF2, IF3, IF4, IF5, IF6 --
    each with a witness, each requirement statement read from the vendored
    Cycle-902 receipt rather than retyped.

Q3  THE SELECTION QUESTION OVER {M3, M4, M5, M6}, restated with Q1 and Q2
    in hand, plus the updated lane ledger.

Discipline: TEXT / AST / JSON only.  The Cycle-863, -878, -902, -905 and
-906 machinery is BLOCKLISTED from import and the census machinery is
lifted out of the pinned sources by AST, so the rebuilt event space is the
pinned construction rather than a transcription.  Only the landed
Cycle-719 core is imported.  Exact arithmetic everywhere; every rank is
computed by two independent routes (the T9 discipline); no floating point
enters any verdict.

Supervisor-authored primary.  bounded_theorem, authority none, audit
unset.  Independent audit still required.
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
C905_PATH = "scripts/frontier_cycle905_born_narrowing_2026_07_28.py"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_PATH = "scripts/frontier_cycle906_covariance_tension_2026_07_28.py"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_PATH, C902_RECEIPT,
    C905_PATH, C905_RECEIPT, C906_PATH, C906_RECEIPT, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C902_PATH, C905_PATH, C906_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C902_RECEIPT, C905_RECEIPT, C906_RECEIPT)
TEXT_ONLY_PATHS = (AXIOMS_PATH,)

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
    C905_PATH:
        "83429f35312e0df16d3d11e65685cb87b8e732b19299e1078ddaea1e1444afb3",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C906_PATH:
        "9c6392d593c1bf37e70f84692732d1e5cfa3f4377393dab846a15789fc0ce008",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C902_PATH: "3b43d97bbb604ea44ed06c87aa091c6aa9d8470b",
    C902_RECEIPT: "1fd7522ad2af152f2e13327e752e2eb9f37e67bb",
    C905_PATH: "f9f2171602bddf7d6164261dc13a2ee4f7e3046c",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C906_PATH: "d7577bb2ac9f4cb7ee9d8abc5f19e9c7cf888df9",
    C906_RECEIPT: "392cba199a75a14a8bb88808943c1259cbd7a94b",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle905_born_narrowing_independent_check_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle906_covariance_tension_independent_check_2026_07_28",
    "frontier_cycle856_record_covariance_2026_07_28",
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
CANDIDATES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
              "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT")
NARROWED = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
            "M5_FORMATION_MOMENT")
M6_NAME = "M6_ABSOLUTE_ORBIT_UNIFORM"
M7_NAME = "M7_ORBIT_RATIO_DEGREE0"
M8_NAME = "M8_ORBIT_RATIO_DEGREE2"
TARGET_CONFIG = "single"
# the equal-block sufficient witness caps the multiplicity it will fold into
# one block; the cap is declared, and the witness is SUFFICIENT only, so the
# cap can never turn a YES into a NO -- only a YES into an UNDECIDED.
EQUAL_BLOCK_J_CAP = 64


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


def gcd_all(values) -> int:
    out = 0
    for v in values:
        out = gcd(out, abs(v))
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
        "cycle906_pair_verified": (
            sha_rows[C906_PATH] == EXPECTED_SHA256[C906_PATH]
            and sha_rows[C906_RECEIPT] == EXPECTED_SHA256[C906_RECEIPT]
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
        and result["cycle906_pair_verified"]
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
    return c863, c878, consts878, {
        "lifted_from_863": names863, "lifted_from_878": names878,
        "constants_863": consts863,
        "constants_878": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts878.items()},
        "import_of_863_878_902_905_906": False,
    }


def build_event_space(c863, c878, consts):
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_fail = c863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = c878.dead_wire_rig(
        program, sim, c863.pack_lanes(states + (states[0],))
    )
    scan = c878.composed_scan(program, census, states, rig, consts["HORIZON"])
    return {"program": program, "census": census, "stations": stations,
            "scan": scan, "events": scan["events"], "init_failures": init_fail}


def world_weighted(a_of_world, events, per_world, supported, common):
    """The Cycle-878 construction, restated: world coefficient a(w) spread
    uniformly over that world's own events over one common denominator.
    Validated against the pinned M2 numerators before use."""
    totals = sum(a_of_world(w) for w in supported)
    nums = [a_of_world(e[0]) * (common // per_world[e[0]]) for e in events]
    return nums, totals * common


# ---------------------------------------------------------------------------
# Exact rank: the T9 two-route discipline
# ---------------------------------------------------------------------------

def rank_by_rational_elimination(rows):
    """Route A: full-pivot Gaussian elimination over Q."""
    if not rows:
        return 0, ()
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


def rank_by_gram_minors(rows, cap=8):
    """Route B: rank(M) = rank(M M^T) over an ordered field; the Gram rank is
    read off division-free by the largest non-vanishing principal minor."""
    if not rows:
        return 0, ()
    k = len(rows)
    if k > cap:
        raise AssertionError(("gram route row cap exceeded", k, cap))
    gram = [[sum(a * b for a, b in zip(rows[i], rows[j])) for j in range(k)]
            for i in range(k)]
    for size in range(k, 0, -1):
        for subset in combinations(range(k), size):
            minor = [[gram[i][j] for j in subset] for i in subset]
            if det_laplace(minor) != 0:
                return size, subset
    return 0, ()


def two_route_rank(rows, label: str) -> dict:
    a, pivots = rank_by_rational_elimination(rows)
    b, subset = rank_by_gram_minors(rows)
    return {"label": label, "rows": len(rows),
            "cols": len(rows[0]) if rows else 0,
            "rank_route_A_rational_elimination": a,
            "rank_route_B_gram_laplace": b,
            "routes_agree": a == b, "pivots": list(pivots),
            "gram_minor_subset": list(subset)}


# ---------------------------------------------------------------------------
# The two objects, rebuilt from their pinned sources
# ---------------------------------------------------------------------------

def rebuild_902_object(receipt902: dict) -> dict:
    """The gravity-side exhibited object, value-for-value from the vendored
    receipt.  Nothing is retyped: every number is read out of the JSON."""
    objs = receipt902["Q3_exhibited_objects"]
    obj = [o for o in objs if o["config"] == TARGET_CONFIG][0]
    table = obj["coefficient_table"]
    degrees = len(table[0]["c_by_degree"])
    C = [[Fraction(cell) for cell in row["c_by_degree"]] for row in table]
    integral = all(x.denominator == 1 for row in C for x in row)
    Cint = [[int(x) for x in row] for row in C]
    columns = [[Cint[i][d] for i in range(len(Cint))] for d in range(degrees)]
    nonzero_degrees = [d for d in range(degrees) if any(columns[d])]
    return {
        "config": obj["config"],
        "atoms": len(table),
        "degrees": degrees,
        "sites": [row["sites"] for row in table],
        "meets_supp_R": [bool(row["meets_supp_R"]) for row in table],
        "c_by_degree_rows": [list(row["c_by_degree"]) for row in table],
        "C": Cint,
        "coefficients_are_integers": integral,
        "columns": columns,
        "nonzero_degrees": nonzero_degrees,
        "degree0": columns[0],
        "degree0_sum": sum(columns[0]),
        "degree2": columns[2] if degrees > 2 else [],
        "degree2_sum": sum(columns[2]) if degrees > 2 else 0,
        "normalizer_N": obj["normalizer_N"],
        "solution_space_dimension": obj["solution_space_dimension"],
        "residual_freedom": obj["residual_freedom_beyond_the_normalizer"],
        "rows_checked": obj["rows_checked"],
        "row_violations": obj["row_violations"],
        "atoms_meeting_supp_R": sum(1 for row in table if row["meets_supp_R"]),
    }


# ---------------------------------------------------------------------------
# The bridge family, DECLARED, and the reduction that makes it searchable
# ---------------------------------------------------------------------------

BRIDGE_FAMILY = {
    "name": "B_894_902_INTEGRAL",
    "definition": (
        "a bridge is a pair (phi, N) with phi a MAP from the Cycle-878 event"
        " space E to the gravity-side atom set of the target configuration,"
        " phi: E -> {A_0, ..., A_{k-1}}, together with a non-zero rational"
        " normalizer N; nu = 1/N.  The pushforward condition is the"
        " Cycle-894 / Cycle-902 condition mu(phi^-1(A)) = Z(A)/N read degree"
        " by degree: c_d(phi^-1(A_i)) = nu * C[i][d] for every atom i and"
        " every degree d <= D."
    ),
    "direction_derivation": (
        "the direction is FORCED by the two objects' types and is not a"
        " choice: mu / c_d are set functions on the Born-side event space E,"
        " while Z and the coefficient table C live on the gravity-side site"
        " algebra.  phi^-1 must therefore carry gravity-side sets to"
        " Born-side sets, so phi runs E -> atoms.  This is exactly the"
        " orientation Cycle 894 used in mu(phi^-1(W)) = Z/N and Cycle 902"
        " re-used in c_d(phi^-1(W)) = M_d(W)/N."
    ),
    "bounds": {
        "phi_is_total": (
            "two readings are computed and reported separately.  EXHAUSTIVE:"
            " phi is total on E, so the four atoms exhaust the census image"
            " -- this is Cycle 905's R_RATIO_EXHAUSTIVE.  NON-EXHAUSTIVE: a"
            " discard symbol is adjoined, phi: E -> atoms + {bottom}, so the"
            " atoms need only carry a sub-part of the census -- this is"
            " Cycle 905's R_RATIO_FREE."),
        "phi_is_integral": (
            "phi is a MAP: every event lands in exactly one atom.  The"
            " fractional relaxation -- a transport plan splitting one event's"
            " mass across several atoms -- is OUTSIDE this family because it"
            " is not a phi with a preimage, and the pinned 894/902"
            " formulation is written with phi^-1.  Its consequences are"
            " computed and disclosed below rather than hidden."),
        "N_free": "N ranges over the non-zero rationals; nu = 1/N.",
        "cardinality": (
            "the family is not enumerable by brute force: |atoms|^|E| ="
            " 4^92260 maps in the exhaustive reading.  The search below is"
            " therefore ALGEBRAIC, via a reduction proved in certificate D,"
            " and is complete over the whole family -- never a sample."),
    },
    "fibre_lift_readings": {
        "P0_THETA_FREE": (
            "the Cycle-894 regime: the Born-side object carries no kernel"
            " argument, so c_0 = m and c_d = 0 for every d >= 1."),
        "P1_SINGLE_WEIGHTING": (
            "one base weighting m with a fibre vector lambda in Q^{D+1}:"
            " c_d = lambda_d * m.  This is the minimal kernel-argument"
            " extension of the LINE through m -- the extension of a single"
            " candidate, which is what 'the pushforward of M6' means."),
        "P2_EXTENSION": (
            "the full Cycle-902 extension: an element of (weightings on E)"
            " tensor (degree-<= D coefficient functionals), so the degree"
            " slices c_0, ..., c_D may be DIFFERENT weightings.  This is the"
            " weakest reading the pinned extension supports."),
    },
}


def block_mass_vector(numerators, blocks):
    return [sum(numerators[i] for i in block) for block in blocks]


def decide_exhaustive(numerators, ratios) -> dict:
    """Cycle 905's R_RATIO_EXHAUSTIVE, recomputed: phi total, so the block
    masses must be exactly (T/scale) * ratios.  Necessary and sufficient:
    scale | T, plus a partition realizing the block sums."""
    total = sum(numerators)
    scale = sum(ratios)
    divides = scale != 0 and total % scale == 0
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
        witness = {"unit_mass_numerator": unit, "block_targets": targets,
                   "block_event_counts": blocks if realizable else None,
                   "greedy_exhausted_targets": realizable}
    return {"reading": "EXHAUSTIVE", "total_numerator": total,
            "ratio_scale_sum": scale, "scale_divides_total": divides,
            "total_mod_scale": total % scale if scale else None,
            "greedy_partition_witness": witness,
            "survives": bool(divides and realizable),
            "verdict": ("SURVIVES" if (divides and realizable)
                        else "FAILS_DIVISIBILITY" if not divides
                        else "FAILS_PARTITION")}


def max_equal_blocks(numerators, need, j_cap=EQUAL_BLOCK_J_CAP):
    """SUFFICIENT witness, strictly stronger than Cycle 905's equal-
    multiplicity witness: the largest number of pairwise disjoint blocks of
    EQUAL mass v that the numerator multiset supports, searched over the
    block masses v that are realizable inside a single equal-value class.
    Sufficiency: given `scale` disjoint blocks of equal mass, hand r_i of
    them to atom i and the block masses land in ratio r."""
    byval: dict = defaultdict(int)
    for v in numerators:
        if v > 0:
            byval[v] += 1
    vals = sorted(byval)
    candidates = set()
    for n in vals:
        for j in range(1, min(byval[n], j_cap) + 1):
            candidates.add(j * n)
    best_count, best_value = 0, None
    for v in sorted(candidates):
        total = 0
        for n in vals:
            if v % n == 0:
                j = v // n
                if j <= byval[n]:
                    total += byval[n] // j
        if total > best_count:
            best_count, best_value = total, v
        if best_count >= need:
            break
    return best_count, best_value


def decide_non_exhaustive(numerators, ratios) -> dict:
    """The NON-EXHAUSTIVE reading, decided as far as exact argument reaches.

    NECESSARY (decides NO): every block mass is a multiple of g = gcd of the
    positive numerators, and gcd(ratios) = 1, so g | t where t is the
    proportionality unit; the block whose ratio is the minimum positive one
    is non-empty, so t >= min positive numerator; and the blocks are
    disjoint, so scale * t <= T.  Hence scale * max(g, min_positive) <= T is
    NECESSARY.  Violated => NO, decided.

    SUFFICIENT (decides YES): `scale` pairwise disjoint equal-mass blocks.

    Otherwise UNDECIDED_BY_THIS_TEST -- never guessed.
    """
    positives = [v for v in numerators if v > 0]
    total = sum(positives)
    scale = sum(ratios)
    if not positives or scale == 0:
        return {"reading": "NON_EXHAUSTIVE", "positive_events": 0,
                "survives": False, "verdict": "FAILS_EMPTY_SUPPORT",
                "positive_mass_total": total, "ratio_scale_sum": scale}
    g = gcd_all(positives)
    minimum = min(positives)
    unit_floor = max(g, minimum)
    necessary = scale * unit_floor <= total
    multiplicity = Counter(positives)
    best_value, best_count = max(multiplicity.items(), key=lambda kv: kv[1])
    block_count, block_value = (0, None)
    if necessary:
        block_count, block_value = max_equal_blocks(positives, scale)
    sufficient_905 = best_count >= scale
    sufficient_blocks = block_count >= scale
    sufficient = sufficient_905 or sufficient_blocks
    if not necessary:
        verdict, survives = "FAILS_CAPACITY", False
    elif sufficient:
        verdict, survives = "SURVIVES", True
    else:
        verdict, survives = "UNDECIDED_BY_THIS_TEST", None
    return {
        "reading": "NON_EXHAUSTIVE",
        "positive_events": len(positives),
        "positive_mass_total": total,
        "ratio_scale_sum": scale,
        "gcd_of_positive_numerators": g,
        "min_positive_numerator": minimum,
        "forced_unit_floor_max_gcd_min": unit_floor,
        "necessary_capacity_scale_times_unit_floor": scale * unit_floor,
        "necessary_capacity_holds": necessary,
        "largest_equal_weight_class": [best_value, best_count],
        "cycle905_equal_multiplicity_witness_suffices": sufficient_905,
        "max_disjoint_equal_mass_blocks": block_count,
        "equal_mass_block_value": block_value,
        "equal_block_witness_suffices": sufficient_blocks,
        "survives": survives,
        "verdict": verdict,
    }


def pushforward_readings(name, numerators, C, blocks_hint=None) -> dict:
    """The three declared readings, computed for one base weighting."""
    degrees = len(C[0])
    columns = [[C[i][d] for i in range(len(C))] for d in range(degrees)]
    nonzero = [d for d in range(degrees) if any(columns[d])]
    rank_rows = [list(row) for row in C]
    rank_info = two_route_rank(rank_rows, f"coefficient_matrix_of_target")
    rank_C = rank_info["rank_route_A_rational_elimination"]

    # P0: theta-free.  Requires every degree >= 1 column to vanish.
    p0_ok = all(not any(columns[d]) for d in range(1, degrees))

    # P1: a single weighting with a fibre vector -> C = lambda (x) S, rank <= 1
    p1_rank_ok = rank_C <= 1

    degree0 = columns[0]
    unit = gcd_all(degree0)
    ratios = [v // unit for v in degree0] if unit else degree0
    exhaustive = decide_exhaustive(numerators, ratios)
    non_exhaustive = decide_non_exhaustive(numerators, ratios)
    degree0_ok = bool(exhaustive["survives"]) or (non_exhaustive["survives"]
                                                  is True)
    degree0_decided_no = (not exhaustive["survives"]) and (
        non_exhaustive["survives"] is False)
    return {
        "candidate": name,
        "target_rank": rank_info,
        "target_rank_value": rank_C,
        "target_nonzero_degrees": nonzero,
        "P0_THETA_FREE": {
            "requires": "every degree >= 1 column of the target must vanish",
            "holds": p0_ok,
            "witness_nonzero_degrees": [d for d in nonzero if d >= 1],
        },
        "P1_SINGLE_WEIGHTING": {
            "requires": (
                "C = lambda (x) S with S the block-mass vector, so"
                " rank(C) <= 1"),
            "rank_condition_holds": p1_rank_ok,
            "degree0_ratio_vector": ratios,
            "degree0_ratio_scale": sum(ratios),
            "exhaustive": exhaustive,
            "non_exhaustive": non_exhaustive,
            "degree0_realizable": degree0_ok,
            "degree0_decided_negative": degree0_decided_no,
            "identifies": bool(p1_rank_ok and degree0_ok),
        },
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
            + "CYCLE907_M6_IDENTIFICATION_PIN_FAILURE\n")
        return 2

    payload_text = {p: (ROOT / p).read_text(encoding="utf-8")
                    for p in AUDIT_INPUT_PATHS}
    receipt878 = json.loads(payload_text[C878_RECEIPT])
    receipt902 = json.loads(payload_text[C902_RECEIPT])
    receipt905 = json.loads(payload_text[C905_RECEIPT])
    receipt906 = json.loads(payload_text[C906_RECEIPT])
    f878 = receipt878["findings"]

    c863, c878, consts, provenance = lift_machinery()
    space = build_event_space(c863, c878, consts)
    events = space["events"]
    census = space["census"]
    stations = space["stations"]
    scan = space["scan"]
    n_worlds = len(census)
    formed = scan["formed"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    n_events = len(events)
    event_digest = digest([list(e) for e in events])

    idx_by_world: dict = defaultdict(list)
    for i, w in enumerate(world_of):
        idx_by_world[w].append(i)

    nums, dens, meta, _pw878, _sup878, common = c878.build_candidates(
        events, scan["occ_global"], formed, scan["boundaries"])
    totals = {name: sum(nums[name]) for name in CANDIDATES}
    zero_counts = {name: sum(1 for v in nums[name] if v == 0)
                   for name in CANDIDATES}
    m2_nums, m2_den = world_weighted(lambda w: 1, events, per_world,
                                     supported, common)
    constructor_agrees = (m2_nums == nums["M2_PER_WORLD_UNIFORM"]
                          and m2_den == dens["M2_PER_WORLD_UNIFORM"])

    perms, perm_ok = c878.monitor_phase_action(census, stations)
    world_orbits = c878.group_orbits(perms, n_worlds) if perm_ok else ()
    never_formed = sorted(w for w in supported if w not in formed)
    never_set = set(never_formed)
    block_events = [i for i, w in enumerate(world_of) if w in never_set]
    formed_worlds = sorted(w for w in supported if w in formed)
    free_orbits = [o for o in world_orbits
                   if not any(w in never_set for w in o)]
    star = list(free_orbits[0]) if free_orbits else []
    star_set = set(star)
    star_events = [i for i, w in enumerate(world_of) if w in star_set]

    m6_nums, m6_den = world_weighted(lambda w: 1 if w in star_set else 0,
                                     events, per_world, supported, common)
    m6_total = sum(m6_nums)
    m6_zero = sum(1 for v in m6_nums if v == 0)
    m6_positive_values = sorted({v for v in m6_nums if v > 0})

    obj = rebuild_902_object(receipt902)

    # ---- B: restriction gates ---------------------------------------------
    gate_rows = []

    def gate(name, computed, expected):
        gate_rows.append({"gate": name, "computed": computed,
                          "expected": expected, "match": computed == expected})

    gate("878_event_cardinality", n_events, f878["event_cardinality"])
    gate("878_worlds_with_events", len(supported),
         f878["worlds_with_at_least_one_event"])
    gate("878_world_orbit_count", len(world_orbits),
         f878["landed_symmetry"]["world_orbit_count"])
    gate("878_action_is_a_census_bijection", bool(perm_ok),
         f878["landed_symmetry"]["action_is_a_census_bijection"])
    gate("878_atoms_are_singletons", bool(f878["atoms_are_singletons"]), True)
    for name in CANDIDATES:
        gate(f"905_total_{name}", totals[name], receipt905["totals"][name])
        gate(f"905_zero_weight_events_{name}", zero_counts[name],
             receipt905["zero_weight_events"][name])
    # --- the 902 exhibited object, value-for-value out of its own receipt
    gate("902_exhibited_object_config", obj["config"], TARGET_CONFIG)
    gate("902_joint_satisfiable_configs", [obj["config"]],
         receipt902["Q2_joint_satisfiable_configs"])
    gate("902_nonzero_degrees", obj["nonzero_degrees"], [0, 2])
    gate("902_atom_count", obj["atoms"], 4)
    gate("902_atom_sites", obj["sites"],
         [row["sites"] for row in
          [o for o in receipt902["Q3_exhibited_objects"]
           if o["config"] == TARGET_CONFIG][0]["coefficient_table"]])
    gate("902_atoms_meeting_supp_R", obj["atoms_meeting_supp_R"], 1)
    gate("902_coefficient_table_reread", obj["c_by_degree_rows"],
         [row["c_by_degree"] for row in
          [o for o in receipt902["Q3_exhibited_objects"]
           if o["config"] == TARGET_CONFIG][0]["coefficient_table"]])
    gate("902_solution_space_dimension", obj["solution_space_dimension"], 1)
    gate("902_residual_freedom", obj["residual_freedom"], 0)
    gate("902_row_violations", obj["row_violations"], 0)
    gate("902_minimal_fibre_dimension", obj["degrees"],
         receipt902["Q1_minimal_fibre_dimension"])
    gate("902_bridge_violations", receipt902["Q3_bridge_violations"], 0)
    # the row-system SHAPE, derived rather than retyped: the 902 scope names 9
    # containment-holding windows; the bridge contributes windows x degrees
    # rows, IF1 contributes one readout row plus (degrees - 1) theta-free rows
    # for the single atom that meets supp(R), and `single` has no vanishing
    # window so IF5 contributes none.
    scope_tokens = receipt902["scope"].split()
    holding_windows = int(
        scope_tokens[scope_tokens.index("containment-holding") - 1])
    derived_rows = (holding_windows * obj["degrees"]
                    + 1 + (obj["degrees"] - 1) * obj["atoms_meeting_supp_R"])
    gate("902_row_system_shape_derived", derived_rows, obj["rows_checked"])
    gate("902_grid_points", receipt902["Q3_grid_points"],
         12 * holding_windows * 6)
    # --- 905's ratio scale and its failure rows
    ratio_scale = obj["degree0_sum"]
    gate("905_ratio_scale_19003", ratio_scale, 19003)
    gate("905_ratio_scale_factorisation",
         {str(k): v for k, v in factorize(ratio_scale).items()},
         {"31": 1, "613": 1})
    gate("905_R_RATIO_EXHAUSTIVE_is_the_joint_obstruction",
         list(receipt905["Q2_joint_obstruction_readings"]),
         ["R_RATIO_EXHAUSTIVE"])
    for name in CANDIDATES:
        gate(f"905_R_RATIO_EXHAUSTIVE_fails_{name}",
             totals[name] % ratio_scale != 0, True)
    # --- 906's M6, value-for-value out of the 906 receipt
    q3 = receipt906["Q3_exhibited_solution"]
    m6_quantum_expected = q3["total"] // q3["support_events"]
    gate("906_M6_support_events", len(star_events), q3["support_events"])
    gate("906_M6_support_worlds", star, list(q3["support_worlds"]))
    gate("906_M6_total", m6_total, q3["total"])
    gate("906_M6_zero_weight_events", m6_zero, q3["zero_weight_events"])
    gate("906_M6_event_numerator_uniform", m6_positive_values,
         [m6_quantum_expected])
    gate("906_M6_quantum_times_support_is_the_total",
         m6_quantum_expected * q3["support_events"], q3["total"])
    gate("906_M6_zero_on_block",
         all(m6_nums[i] == 0 for i in block_events), True)
    gate("906_world_mass_space_dimension",
         receipt906["Q3_world_mass_space_dimension"], 1)
    gate("906_generous_signed_solution_dimension",
         len(events) - len(block_events)
         - ((len(formed_worlds) - len(star)) + (len(star) - 1)),
         receipt906["Q3_generous_base_signed_solution_dimension"])
    gate("906_escape_orbit_count", len(free_orbits), 1)
    # the never-formed block counts are read back OUT of the pinned 905
    # receipt's own census-level sentence, not retyped here
    mech_numbers = [int(t) for t in
                    re.findall(r"\d+", receipt905["Q1_census_level_mechanism"])]
    gate("905_mechanism_sentence_numbers", mech_numbers,
         [748, 164, 584, 73088, 92260])
    gate("905_worlds_never_formed", len(never_formed), mech_numbers[2])
    gate("905_events_on_never_formed_worlds", len(block_events),
         mech_numbers[3])
    gate("905_worlds_formed", len(formed_worlds), mech_numbers[1])

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows,
        "reproduce": sum(1 for r in gate_rows if r["match"]),
        "total": len(gate_rows),
        "constructor_reproduces_pinned_M2": constructor_agrees,
        "event_space_digest": event_digest,
    }
    cert_b["pass"] = bool(all(r["match"] for r in gate_rows)
                          and constructor_agrees)

    # ---- C: the two objects, rebuilt --------------------------------------
    rank_C = two_route_rank([list(r) for r in obj["C"]],
                            "902_coefficient_matrix_4x5")
    minor = [[obj["C"][0][0], obj["C"][0][2]],
             [obj["C"][1][0], obj["C"][1][2]]]
    minor_det = det_laplace(minor)
    cert_c = {
        "certificate": "C_OBJECT_REBUILD",
        "gravity_side": {
            "config": obj["config"], "atoms": obj["atoms"],
            "degrees": obj["degrees"], "sites": obj["sites"],
            "meets_supp_R": obj["meets_supp_R"],
            "coefficient_table": obj["c_by_degree_rows"],
            "coefficients_are_integers": obj["coefficients_are_integers"],
            "degree_columns": obj["columns"],
            "nonzero_degrees": obj["nonzero_degrees"],
            "degree0_vector": obj["degree0"],
            "degree0_sum_is_the_ratio_scale": obj["degree0_sum"],
            "degree2_vector": obj["degree2"],
            "degree2_sum": obj["degree2_sum"],
            "rank": rank_C,
            "exhibited_2x2_minor": minor,
            "exhibited_minor_determinant": minor_det,
            "rank_is_two": rank_C["rank_route_A_rational_elimination"] == 2,
        },
        "born_side": {
            "name": M6_NAME,
            "definition": (
                "each world of the unique monitor-phase orbit that misses the"
                " never-formed block gets equal mass, spread uniformly over"
                " its own events; every other world gets zero -- the"
                " Cycle-906 exhibited solution, rebuilt here through the"
                " Cycle-878 world_weighted constructor"),
            "support_worlds": star,
            "support_events": len(star_events),
            "events_per_support_world": sorted(
                {per_world[w] for w in star}),
            "event_numerator_on_support": m6_positive_values,
            "total_numerator": m6_total,
            "denominator": m6_den,
            "zero_weight_events": m6_zero,
            "gcd_of_positive_numerators": gcd_all(
                [v for v in m6_nums if v > 0]),
            "total_over_gcd": m6_total // gcd_all(
                [v for v in m6_nums if v > 0]),
            "total_factorisation": {str(k): v
                                    for k, v in factorize(m6_total).items()},
        },
        "constructor_reproduces_pinned_M2": constructor_agrees,
    }
    cert_c["pass"] = bool(
        rank_C["routes_agree"] and obj["coefficients_are_integers"]
        and minor_det != 0 and constructor_agrees
        and cert_c["born_side"]["event_numerator_on_support"] == [8320])

    # ---- D: the bridge family and the reduction ---------------------------
    reduction = (
        "REDUCTION (complete, not a sample).  Fix a base weighting m and a"
        " fibre lift.  A bridge phi determines, and is determined for the"
        " purposes of the pushforward equations by, its block-mass vector"
        " S_i = m(phi^-1(A_i)); the equations c_d(phi^-1(A_i)) = nu * C[i][d]"
        " see phi ONLY through the numbers c_d(phi^-1(A_i)).  So a bridge in"
        " the declared family exists iff there is an ACHIEVABLE block-mass"
        " vector satisfying the equations, where achievable means realized by"
        " some family of pairwise disjoint blocks of E (exhaustive: the"
        " blocks partition E).  The search over 4^92260 maps is therefore"
        " replaced by an exact question about achievable block masses, and"
        " the replacement is an equivalence, not an approximation."
    )
    cert_d = {
        "certificate": "D_BRIDGE_FAMILY",
        "family": BRIDGE_FAMILY,
        "reduction": reduction,
        "reduction_is_an_equivalence": True,
        "readings_computed": ["P0_THETA_FREE", "P1_SINGLE_WEIGHTING",
                              "P2_EXTENSION"],
        "decision_procedure": {
            "exhaustive": (
                "scale | T is NECESSARY and, with a realizing partition,"
                " SUFFICIENT -- Cycle 905's R_RATIO_EXHAUSTIVE, recomputed"),
            "non_exhaustive_necessary": (
                "scale * max(gcd of positive numerators, min positive"
                " numerator) <= T.  Derivation: gcd(ratios) = 1 forces g | t;"
                " the ratio-1 block is non-empty so t >= min positive"
                " numerator; the blocks are disjoint so scale * t <= T"),
            "non_exhaustive_sufficient": (
                "scale pairwise disjoint blocks of EQUAL mass -- a strict"
                " strengthening of Cycle 905's equal-multiplicity witness,"
                " which is the special case of one event per block"),
            "otherwise": "UNDECIDED_BY_THIS_TEST, never guessed",
        },
    }
    cert_d["pass"] = True

    # ---- E: Q1, the pushforward test --------------------------------------
    # the degree-0 ratio vector, reduced by its own gcd; this is the invariant
    # the pushforward equations actually see, because nu is free
    degree0_gcd = gcd_all(obj["degree0"])
    ratios0 = ([v // degree0_gcd for v in obj["degree0"]] if degree0_gcd
               else list(obj["degree0"]))

    readings = {}
    all_candidates = dict(nums)
    all_candidates[M6_NAME] = m6_nums
    for name, vec in all_candidates.items():
        readings[name] = pushforward_readings(name, vec, obj["C"])

    m6_read = readings[M6_NAME]

    # --- the universal rank obstruction, stated once
    rank_value = rank_C["rank_route_A_rational_elimination"]
    universal_rank_obstruction = {
        "statement": (
            "under reading P1 the pushforward of ANY single base weighting m"
            " with any fibre vector lambda has coefficient matrix"
            " C[i][d] = lambda_d * S_i, a rank-<= 1 matrix.  The Cycle-902"
            f" exhibited object has rank {rank_value}, certified by two"
            " routes and by an exhibited non-vanishing 2x2 minor.  So NO"
            " single weighting -- not M6, not any of the Cycle-878 five, not"
            " any element of the covariant-and-compatible cone, not any"
            " weighting whatsoever on any event space -- is its pushforward."),
        "target_rank": rank_value,
        "rank_bound_for_a_single_weighting": 1,
        "obstruction_holds": rank_value > 1,
        "the_two_independent_columns": {"degree_0": obj["degree0"],
                                        "degree_2": obj["degree2"]},
        "exhibited_minor_determinant": minor_det,
        "it_is_the_894_obstruction_at_event_level": (
            "this is not a new fact wearing a new name: a rank-1 pushforward"
            " whose fibre vector has a single non-zero entry is exactly the"
            " theta-free regime, and IF3's own text says a theta-FREE"
            " weighting forces M_d = 0 for every d >= 1, which holds only on"
            " the five frozen configurations.  `single` is theta-MOVING, so"
            " its degree-2 column is non-zero and the same obstruction shows"
            " up as rank 2.  The degree obstruction and the 894 theta-free"
            " obstruction are ONE fact."),
        "survives_the_fractional_relaxation": (
            "yes.  A transport plan that splits an event's mass across atoms"
            " still yields C = lambda (x) S, so the rank bound is untouched."
            "  Relaxing integrality repairs the degree-0 reading only."),
    }

    # --- the fractional relaxation, disclosed
    m6_positive_min = min(v for v in m6_nums if v > 0)
    fractional = {
        "what_it_is": (
            "the declared family's integrality bound, relaxed: a transport"
            " plan splitting one event's mass across several atoms"),
        "outside_the_declared_family": True,
        "degree0_condition_under_the_relaxation": (
            "any non-negative block-mass vector with sum <= T is achievable,"
            " so proportionality to the degree-0 ratio vector needs only"
            " scale * t <= T for some t > 0, i.e. T > 0"),
        "M6_degree0_would_pass": m6_total > 0,
        "M6_unit_it_would_need": fr(Fraction(m6_total, ratio_scale)),
        "unit_is_not_an_integer_multiple_of_the_quantum": (
            Fraction(m6_total, ratio_scale) % m6_positive_min != 0),
        "but_the_rank_obstruction_survives": True,
        "why_it_is_not_licensed_here": (
            "the pinned 894/902 formulation is written with phi^-1, which"
            " presupposes a map.  Splitting an event's recorded mass across"
            " gravity-side atoms is a different object and would need its own"
            " licensing; it is reported, not used."),
    }

    # --- the covariant-and-compatible cone, and the exhibited identification
    # M7 and M8: the degree-0 and degree-2 slices, built inside the cone
    def orbit_pattern_weighting(pattern):
        """Put `pattern` on the first len(pattern) events of each escape world
        in the pinned Cycle-878 emission order, zero everywhere else."""
        vec = [0] * n_events
        for w in star:
            ids = idx_by_world[w]
            for j, value in enumerate(pattern):
                vec[ids[j]] = value
        return vec

    # one slice per NON-ZERO degree column, built generically; the zero
    # columns need no slice, and the grid below checks them all the same
    slices = {d: orbit_pattern_weighting(obj["columns"][d])
              for d in obj["nonzero_degrees"]}
    m7_nums = slices[0]
    m8_nums = slices[2]

    def world_mass_of(vec):
        return {w: sum(vec[i] for i in idx_by_world[w]) for w in supported}

    def is_covariant(vec):
        masses = world_mass_of(vec)
        return all(len({masses[x] for x in orbit if x in masses}) <= 1
                   for orbit in world_orbits)

    # the exhibited bridge: atom i receives the i-th event of every escape
    # world for i >= 1; atom 0 receives everything else.  phi is TOTAL.
    phi = [0] * n_events
    for w in star:
        ids = idx_by_world[w]
        for j in range(1, obj["atoms"]):
            phi[ids[j]] = j
    blocks = [[i for i in range(n_events) if phi[i] == b]
              for b in range(obj["atoms"])]
    blocks_disjoint = sum(len(b) for b in blocks) == n_events

    nu = len(star)
    # verification grid: EVERY element of the Boolean algebra the atoms
    # generate (2^atoms subsets) x every degree -- strictly finer than the
    # 9 windows the 902 rows use, because every window is a union of atoms.
    grid_cells, grid_bad = 0, []
    for mask in range(1 << obj["atoms"]):
        subset = [i for i in range(obj["atoms"]) if mask >> i & 1]
        preimage_mass = {}
        for d in range(obj["degrees"]):
            vec = slices.get(d)
            lhs = 0 if vec is None else sum(
                sum(vec[i] for i in blocks[b]) for b in subset)
            rhs = nu * sum(obj["C"][b][d] for b in subset)
            grid_cells += 1
            if lhs != rhs:
                grid_bad.append({"subset": subset, "degree": d,
                                 "lhs": lhs, "rhs": rhs})
            preimage_mass[d] = lhs
    identification_verified = not grid_bad

    m7_world_masses = sorted(set(world_mass_of(m7_nums).values()))
    m8_world_masses = sorted(set(world_mass_of(m8_nums).values()))
    cone_membership = {
        M7_NAME: {
            "role": "the degree-0 slice c_0",
            "total_numerator": sum(m7_nums),
            "support_events": sum(1 for v in m7_nums if v != 0),
            "zero_weight_events": sum(1 for v in m7_nums if v == 0),
            "distinct_world_masses": m7_world_masses,
            "monitor_phase_covariant": is_covariant(m7_nums),
            "zero_on_the_never_formed_block":
                all(m7_nums[i] == 0 for i in block_events),
            "non_negative": all(v >= 0 for v in m7_nums),
            "normalizable": sum(m7_nums) > 0,
            "finitely_additive": True,
            "supported_on_the_escape_orbit": all(
                world_of[i] in star_set for i, v in enumerate(m7_nums) if v),
        },
        M8_NAME: {
            "role": "the degree-2 slice c_2",
            "total_numerator": sum(m8_nums),
            "support_events": sum(1 for v in m8_nums if v != 0),
            "zero_weight_events": sum(1 for v in m8_nums if v == 0),
            "distinct_world_masses": m8_world_masses,
            "monitor_phase_covariant": is_covariant(m8_nums),
            "zero_on_the_never_formed_block":
                all(m8_nums[i] == 0 for i in block_events),
            "non_negative": all(v >= 0 for v in m8_nums),
            "normalizable": sum(m8_nums) > 0,
            "finitely_additive": True,
            "supported_on_the_escape_orbit": all(
                world_of[i] in star_set for i, v in enumerate(m8_nums) if v),
        },
    }

    # --- the residual freedom of the identification, priced by two routes
    events_on_formed = n_events - len(block_events)
    non_escape_formed = len(formed_worlds) - len(star)
    covariance_reduced_rank = non_escape_formed + (len(star) - 1)
    cone_dim_route_a = events_on_formed - covariance_reduced_rank
    # route B: the four block functionals restricted to the cone, by an
    # exhibited minor.  The four directions below lie in the cone (each has
    # constant world mass on every orbit and vanishes on the block).
    directions = []
    for j in range(obj["atoms"]):
        vec = [0] * n_events
        for w in star:
            vec[idx_by_world[w][j]] = 1
        directions.append(vec)
    functional_matrix = [[sum(vec[i] for i in blocks[b])
                          for b in range(obj["atoms"])] for vec in directions]
    functional_det = det_laplace(functional_matrix)
    block_functional_rank = two_route_rank(functional_matrix,
                                           "block_functionals_on_the_cone")
    identification_residual_freedom = cone_dim_route_a - obj["atoms"]
    directions_in_cone = all(
        is_covariant(v) and all(v[i] == 0 for i in block_events)
        for v in directions)

    covariant_generalisation = {
        "question": (
            "can ANY monitor-phase covariant, interface-zero-compatible"
            " weighting push forward to the Cycle-902 object?"),
        "the_cone": (
            "Cycle 906 computed it: covariance forces the world masses to be"
            " constant on orbits, the zero-mass requirement forces every"
            " orbit that meets the never-formed block to carry world mass"
            " zero, and exactly one orbit misses the block.  So a"
            " non-negative covariant compatible weighting is supported on the"
            f" {len(star_events)} events of the {len(star)} escape worlds,"
            " with those worlds carrying EQUAL mass and the split WITHIN each"
            " world entirely free -- 906's own words: 'the remaining freedom"
            " is entirely WITHIN worlds ... which no covariance or zero-mass"
            " equation constrains'"),
        "degree0_answer": "YES, and it is exhibited",
        "degree0_witness": M7_NAME,
        "degree2_answer": "YES, and it is exhibited",
        "degree2_witness": M8_NAME,
        "full_object_answer_under_P2": bool(identification_verified),
        "full_object_answer_under_P1": False,
        "why_M6_is_not_the_witness": (
            "M6 differs from the witness ONLY in its within-world split:"
            " 906 chose the uniform split, which is a free choice no equation"
            " forces.  The uniform split makes every positive numerator equal"
            f" to {m6_positive_min}, so every achievable block mass is a"
            f" multiple of {m6_positive_min} and the ratio vector needs"
            f" {ratio_scale} such quanta while the support has only"
            f" {len(star_events)} events."),
        "M2_line_status": {
            "covariant": True,
            "interface_zero_compatible": False,
            "why": ("Cycle 905/906: M2 has an EMPTY zero set (minimum event"
                    " numerator 8320 > 0), so it cannot host a single"
                    " vanishing cell under P-NONEMPTY"),
            "degree0_exhaustive": decide_exhaustive(
                nums["M2_PER_WORLD_UNIFORM"], ratios0)["verdict"],
            "degree0_non_exhaustive": decide_non_exhaustive(
                nums["M2_PER_WORLD_UNIFORM"], ratios0)["verdict"],
            "reading": (
                "the covariant LINE of the Cycle-878 span passes the"
                " non-exhaustive degree-0 reading and fails the exhaustive"
                " one, but it is excluded from the interface upstream, on the"
                " zero-mass requirement, so it never reaches the bridge"),
        },
    }

    m6_identifies = bool(m6_read["P1_SINGLE_WEIGHTING"]["identifies"])
    cert_e = {
        "certificate": "E_PUSHFORWARD_TEST",
        "question": (
            "Q1: is the Cycle-902 gravity-side exhibited object the"
            " pushforward of M6_ABSOLUTE_ORBIT_UNIFORM under any bridge"
            " (phi, N) of the declared family?"),
        "verdict": "NO" if not m6_identifies else "YES",
        "M6_readings": m6_read,
        "M6_obstruction_layers": [
            {"layer": "DEGREE / RANK (universal)",
             "reading": "P1_SINGLE_WEIGHTING",
             "what_fails": (
                 f"the target has rank {rank_value}; a single weighting's"
                 " pushforward has rank <= 1"),
             "jointly_unsatisfiable_conditions": (
                 "lambda_2 * S_i = nu * C[i][2] for i = 0..3 together with"
                 " lambda_0 * S_i = nu * C[i][0].  Atom 3 forces S_3 = 0 from"
                 " the degree-2 rows (C[3][2] = 0) and S_3 != 0 from the"
                 " degree-0 rows (C[3][0] != 0) whenever lambda_0, lambda_2"
                 " and nu are all non-zero; setting lambda_2 = 0 then forces"
                 " nu * C[0][2] = 0 with C[0][2] != 0, hence nu = 0"),
             "kills": "every single weighting on every event space"},
            {"layer": "DEGREE-0 EXHAUSTIVE (M6-specific)",
             "reading": "R_RATIO_EXHAUSTIVE of Cycle 905",
             "what_fails": (
                 f"the ratio scale {ratio_scale} = 31 * 613 does not divide"
                 f" M6's total {m6_total};"
                 f" remainder {m6_total % ratio_scale}"),
             "kills": "M6 under a total bridge"},
            {"layer": "DEGREE-0 NON-EXHAUSTIVE (M6-specific)",
             "reading": "R_RATIO_FREE of Cycle 905",
             "what_fails": (
                 f"M6's positive numerators are all equal to"
                 f" {m6_positive_min}, so its gcd is {m6_positive_min} and"
                 f" the necessary capacity condition reads"
                 f" {ratio_scale} * {m6_positive_min} ="
                 f" {ratio_scale * m6_positive_min} <= {m6_total}, which is"
                 " FALSE.  Equivalently: the ratio vector demands a block"
                 f" {obj['degree0'][0]} times the mass of the smallest block,"
                 f" i.e. at least {ratio_scale} quanta, and M6's support has"
                 f" only {len(star_events)} events"),
             "kills": "M6 under a partial bridge too -- the reading is"
                      " DECIDED negative, not merely undecided"},
        ],
        "universal_rank_obstruction": universal_rank_obstruction,
        "fractional_relaxation_disclosure": fractional,
        "covariant_space_generalisation": covariant_generalisation,
        "P2_exhibited_identification": {
            "reading": "P2_EXTENSION",
            "claim": (
                "the Cycle-902 exhibited object IS the pushforward, under an"
                " explicit bridge (phi, N), of an element of the"
                " kernel-argument extension whose degree-0 and degree-2"
                " slices are BOTH monitor-phase covariant, BOTH zero on the"
                " never-formed block, BOTH non-negative and BOTH supported on"
                " the escape orbit -- but whose degree-0 slice is NOT M6"),
            "bridge_phi": (
                f"atom i receives the i-th event of every one of the"
                f" {len(star)} escape worlds for i = 1..{obj['atoms'] - 1};"
                " atom 0 receives every other event of E.  phi is TOTAL, so"
                " this is the EXHAUSTIVE reading"),
            "within_world_order": (
                "the pinned Cycle-878 event emission order restricted to a"
                " world -- premise P-EVENT-ORDER, named and undischarged"),
            "block_sizes": [len(b) for b in blocks],
            "blocks_partition_E": blocks_disjoint,
            "normalizer_N": fr(Fraction(1, nu)),
            "nu": nu,
            "degree_slices": {"0": M7_NAME, "2": M8_NAME,
                              "1_3_4": "the zero weighting"},
            "cone_membership": cone_membership,
            "block_masses": {
                M7_NAME: block_mass_vector(m7_nums, blocks),
                M8_NAME: block_mass_vector(m8_nums, blocks),
                "target_degree0_times_nu": [nu * v for v in obj["degree0"]],
                "target_degree2_times_nu": [nu * v for v in obj["degree2"]],
            },
            "verification_grid": {
                "what": ("every element of the Boolean algebra the atoms"
                         " generate x every degree -- strictly finer than the"
                         " 9 windows of the 902 rows, because every window is"
                         " a union of atoms"),
                "cells": grid_cells,
                "expected_cells": (1 << obj["atoms"]) * obj["degrees"],
                "violations": len(grid_bad),
                "violation_exhibits": grid_bad[:8],
                "verified": identification_verified,
            },
            "window_theta_grid_status": (
                "NOT recomputed here and not claimed: the Cycle-892/885/887"
                " machinery is absent from this branch, so the (window,"
                f" theta) grid check is INHERITED from the pinned Cycle-902"
                f" certificate G ({receipt902['Q3_grid_points']} points, 0"
                " violations).  What is recomputed here is strictly finer on"
                " the atom algebra and strictly silent on Z itself"),
        },
        "identification_pricing": {
            "gravity_side_residual_freedom": obj["residual_freedom"],
            "born_side_cone_dimension_route_A_structural": cone_dim_route_a,
            "born_side_cone_dimension_derivation": (
                f"{events_on_formed} events on formed worlds, minus"
                f" {covariance_reduced_rank} independent covariance"
                f" conditions after the {len(block_events)} block equations"
                " are eliminated as coordinate projections"
                f" ({non_escape_formed} formed worlds outside the escape"
                f" orbit forced to zero mass, plus {len(star) - 1} equalities"
                " inside it)"),
            "born_side_cone_dimension_gate_against_906":
                receipt906["Q3_generous_base_signed_solution_dimension"],
            "block_functionals_rank": block_functional_rank,
            "block_functional_minor": functional_matrix,
            "block_functional_determinant": functional_det,
            "directions_lie_in_the_cone": directions_in_cone,
            "identification_residual_freedom":
                identification_residual_freedom,
            "reading": (
                "the gravity side pins its object to residual freedom"
                f" {obj['residual_freedom']} once N is fixed; the Born-side"
                f" preimage of that same object has residual freedom"
                f" {identification_residual_freedom}.  The interface object"
                f" constrains a covariant compatible weighting by exactly"
                f" {obj['atoms']} numbers per degree slice and by nothing"
                " else.  The identification is UNDERDETERMINED, not"
                " obstructed -- except for the named candidates, every one of"
                " which it excludes"),
        },
        "conditionality_chain": [
            {"premise": "P-NONEMPTY",
             "origin": "inherited from Cycle 905",
             "what_it_licenses": (
                 "that any bridge sends the record atom meeting supp(R) to a"
                 " NON-EMPTY set of census events, so a weighting with an"
                 " empty zero set cannot host a vanishing cell and the"
                 " ratio-1 block is non-empty"),
             "used_in": ["E_PUSHFORWARD_TEST (the t >= min positive numerator"
                         " step of the non-exhaustive necessary condition)",
                         "F_INTERFACE_SHEET (IF1, IF5)"],
             "status": "named, undischarged"},
            {"premise": "the Cycle-903 barrier scope",
             "origin": "the gravity 903, entering only through the vendored"
                       " 902 artifacts",
             "what_it_licenses": (
                 "that IF1's readout-versus-seed-mass comparison is a"
                 " property of the barrier B(R) = supp(R) and is"
                 " P2-invariant (C902-T3), so the surviving sub-grid is"
                 " exactly `single`"),
             "used_in": ["B_RESTRICTION_GATE", "E_PUSHFORWARD_TEST",
                         "F_INTERFACE_SHEET"],
             "status": "named, undischarged, inherited"},
            {"premise": "the Cycle-906 single-orbit horizon scope",
             "origin": "Cycle 906",
             "what_it_licenses": (
                 "that exactly one of the 68 covariance orbits misses the"
                 " never-formed block AT THE PINNED HORIZON; the escape hatch"
                 " is a horizon-dependent census fact, not a theorem"),
             "used_in": ["C_OBJECT_REBUILD", "E_PUSHFORWARD_TEST"],
             "status": "named, undischarged, inherited"},
            {"premise": "P-INTERTWINE-878",
             "origin": "Cycle 906, named there",
             "what_it_licenses": "the covariance condition's second reading",
             "used_in": ["E_PUSHFORWARD_TEST (the cone)"],
             "status": "named, undischarged, inherited"},
            {"premise": "the Cycle-892 interface premises (IF1..IF6)",
             "origin": "read from the vendored Cycle-902 receipt",
             "what_it_licenses": (
                 "that these six requirements are what the gravity side"
                 " demands of a measurement weighting"),
             "used_in": ["F_INTERFACE_SHEET"],
             "status": "named, undischarged, inherited"},
            {"premise": "P-EVENT-ORDER",
             "origin": "NAMED HERE",
             "what_it_licenses": (
                 "that the within-world order used to build the exhibited"
                 " degree slices is the pinned Cycle-878 emission order.  It"
                 " licenses only the WITNESS, never a no-go: every negative"
                 " verdict in this block is order-independent"),
             "used_in": ["E_PUSHFORWARD_TEST (the P2 witness only)"],
             "status": "named here, undischarged"},
            {"premise": "P-856-SHAPE",
             "origin": "Cycle 906, named there",
             "what_it_licenses": "the escape orbit's absolute-record shape",
             "used_in": ["not consumed by any verdict in this block"],
             "status": "named, undischarged, inherited, unused"},
        ],
    }
    cert_e["pass"] = bool(
        cert_c["pass"]
        and m6_read["P1_SINGLE_WEIGHTING"]["identifies"] is False
        and universal_rank_obstruction["obstruction_holds"]
        and identification_verified
        and blocks_disjoint
        and directions_in_cone
        and functional_det != 0
        and cone_dim_route_a
        == receipt906["Q3_generous_base_signed_solution_dimension"]
        and all(row["monitor_phase_covariant"]
                and row["zero_on_the_never_formed_block"]
                and row["non_negative"] and row["normalizable"]
                for row in cone_membership.values())
    )

    # ---- F: Q2, M6's full interface sheet ---------------------------------
    per_req = {row["id"]: row for row in receipt902["Q2_per_requirement"]}
    if1_two = receipt902["Q2_IF1_two_readings"]
    theta_free_configs = receipt902["Q2_subset_tables"]["C894_THETA_FREE"][
        "configs"]
    theta_moving = receipt902["Q2_c894_reproduction"][
        "theta_moving_configs_on_the_fine_grid"]

    # IF4, computed: a degree-0-only pushforward makes the window an argument
    # iff the degree-0 vector separates the atom algebra.  Superincreasing is
    # COMPUTED, not assumed.
    def subset_sums_distinct(vector):
        sums = []
        for mask in range(1 << len(vector)):
            sums.append(sum(vector[i] for i in range(len(vector))
                            if mask >> i & 1))
        return len(set(sums)) == len(sums), len(sums), len(set(sums))

    target_sep, target_n, target_u = subset_sums_distinct(obj["degree0"])
    exhibited_bridge_masses = block_mass_vector(m6_nums, blocks)
    exh_sep, exh_n, exh_u = subset_sums_distinct(exhibited_bridge_masses)
    # a bridge for M6 that DOES separate: split the support superincreasingly
    if1_counts = [1000, 300, 100, 19]
    witness_ok = sum(if1_counts) == len(star_events)
    witness_masses = [c * m6_positive_min for c in if1_counts]
    wit_sep, wit_n, wit_u = subset_sums_distinct(witness_masses)

    # IF1 at event level, for every candidate: the ratio vector's realizability
    if1_event_level = {}
    for name, vec in all_candidates.items():
        ex = decide_exhaustive(vec, ratios0)
        ne = decide_non_exhaustive(vec, ratios0)
        decided = (True if (ex["survives"] or ne["survives"] is True)
                   else (False if ne["survives"] is False else None))
        if1_event_level[name] = {
            "exhaustive_verdict": ex["verdict"],
            "non_exhaustive_verdict": ne["verdict"],
            "decided": decided,
            "min_positive_numerator": ne.get("min_positive_numerator"),
            "gcd_of_positive_numerators": ne.get("gcd_of_positive_numerators"),
            "necessary_capacity_holds": ne.get("necessary_capacity_holds"),
            "largest_equal_weight_class": ne.get("largest_equal_weight_class"),
        }

    sheet = [
        {"id": "IF1", "reading": "WEAK (support overlap), config level",
         "requirement": per_req["IF1"]["requirement"],
         "M6_verdict": "PASS",
         "witness": (
             f"`{TARGET_CONFIG}` is one of the {if1_two['weak_count']}"
             " configurations whose amplitude support meets supp(R); this is"
             " a property of the configuration, not of the weighting, so the"
             " Born side neither adds to it nor takes from it"),
         "computed_from": "the vendored 902 receipt's own two-reading table"},
        {"id": "IF1", "reading": "STRONG (pointwise identification), config"
                                 " level",
         "requirement": per_req["IF1"]["requirement"],
         "M6_verdict": "PASS",
         "witness": (
             f"`{TARGET_CONFIG}` is the sole member of the"
             f" {if1_two['strong_count']}-element strong list: its linear"
             " readout equals the seed mass C892-T1 confines inside supp(R)"),
         "computed_from": "the vendored 902 receipt"},
        {"id": "IF1", "reading": "EVENT-LEVEL PULLBACK through M6's support"
                                 " (NEW, computed here)",
         "requirement": (
             "the IF1 rows read c_0(A_i) = nu * I(A_i) with the readout"
             " vector fixed by the exhibited object, so the Born side must"
             " produce disjoint blocks whose masses stand in the exact ratio"
             f" {ratios0}"),
         "M6_verdict": "FAIL",
         "witness": {
             "exhaustive": if1_event_level[M6_NAME]["exhaustive_verdict"],
             "non_exhaustive":
                 if1_event_level[M6_NAME]["non_exhaustive_verdict"],
             "why": (
                 f"M6's mass quantum is {m6_positive_min} on every one of its"
                 f" {len(star_events)} support events, so the ratio vector"
                 f" would need {ratio_scale} quanta and only"
                 f" {len(star_events)} exist"),
         },
         "computed_from": "this block"},
        {"id": "IF2", "reading": "single",
         "requirement": per_req["IF2"]["requirement"],
         "M6_verdict": "PASS",
         "witness": (
             "the Cycle-878 atoms are singletons (gate reproduced), so an"
             " event-level weighting is finitely additive over every disjoint"
             " family by construction"),
         "computed_from": "the 878 receipt gate plus construction"},
        {"id": "IF3", "reading": "single",
         "requirement": per_req["IF3"]["requirement"],
         "M6_verdict": "FAIL on the target configuration",
         "witness": {
             "M6_is_theta_free": True,
             "theta_free_passes_on": theta_free_configs,
             "target_in_that_list": TARGET_CONFIG in theta_free_configs,
             "theta_moving_configs": theta_moving,
             "target_is_theta_moving": TARGET_CONFIG in theta_moving,
             "count": f"{len(theta_free_configs)}/12",
             "why": (
                 "902's own text: with a theta-FREE weighting the bridge"
                 " forces M_d = 0 for every d >= 1, which holds only on the"
                 " frozen walks.  M6 carries no kernel argument, so it is in"
                 f" the 894 regime, and `{TARGET_CONFIG}` is theta-MOVING"),
         },
         "computed_from": "the vendored 902 receipt's own subset tables"},
        {"id": "IF4", "reading": "single",
         "requirement": per_req["IF4"]["requirement"],
         "M6_verdict": "PASS (bridge-dependent; a separating bridge exists)",
         "witness": {
             "criterion": (
                 "a degree-0-only pushforward makes the window an argument"
                 " iff the degree-0 block-mass vector gives all"
                 f" {1 << obj['atoms']} atom-subsets distinct mass; distinct"
                 " windows are distinct unions of atoms"),
             "target_object_separates": target_sep,
             "target_subset_sums": [target_n, target_u],
             "under_the_exhibited_orbit_symmetric_bridge": {
                 "block_masses": exhibited_bridge_masses,
                 "separates": exh_sep,
                 "distinct_of_total": [exh_u, exh_n],
                 "why_not": ("that bridge gives atoms 1, 2 and 3 the same"
                             " mass, because M6 is uniform and each of those"
                             " atoms receives exactly one event per escape"
                             " world"),
             },
             "separating_bridge_witness": {
                 "block_event_counts": if1_counts,
                 "counts_exhaust_the_support": witness_ok,
                 "block_masses": witness_masses,
                 "separates": wit_sep,
                 "distinct_of_total": [wit_u, wit_n],
             },
             "reading": (
                 "IF4 is a property of the BRIDGE, not of the weighting, and"
                 " it is satisfiable for M6.  It is the only requirement on"
                 " this sheet that M6 can buy by choosing phi"),
         },
         "computed_from": "this block"},
        {"id": "IF5", "reading": "single",
         "requirement": per_req["IF5"]["requirement"],
         "M6_verdict": "PASS, conditional on P-NONEMPTY",
         "witness": {
             "zero_weight_events": m6_zero,
             "of_events": n_events,
             "vanishing_cells_to_host": 42,
             "support_faithful": m6_zero == 0,
             "can_host": m6_zero > 0,
             "why": ("IF5 is satisfiable only by giving up support"
                     " faithfulness (902 certificate D); M6 gives it up"
                     " maximally"),
         },
         "computed_from": "this block"},
        {"id": "IF6", "reading": "single",
         "requirement": per_req["IF6"]["requirement"],
         "M6_verdict": "PASS, but vacuously",
         "witness": {
             "M6_pushforward_degree": 0,
             "bound_D": obj["degrees"] - 1,
             "why_vacuous": (
                 "M6's pushforward is a degree-0 polynomial in cos phi, which"
                 " is trivially of degree <= D.  Passing IF6 by being"
                 " degree-0 is EXACTLY what fails IF3, so this PASS carries"
                 " no information: it is the same fact as the IF3 FAIL, read"
                 " with the opposite sign"),
         },
         "computed_from": "this block"},
    ]
    fails = [row for row in sheet if row["M6_verdict"].startswith("FAIL")]
    passes = [row for row in sheet if row["M6_verdict"].startswith("PASS")]

    if1_gap_comparison = {
        "question": (
            "does the IF1 gap behave differently on M6's support than on the"
            " survivors'?"),
        "config_level_gap_on_the_target": (
            f"CLOSED: `{TARGET_CONFIG}` is the sole configuration whose"
            " readout equals its seed mass, which is why it is the whole"
            " surviving sub-grid"),
        "event_level_rows": if1_event_level,
        "answer": (
            "YES.  At configuration level the gap is closed on the target for"
            " every weighting alike -- it is a barrier fact.  At event level"
            " the pullback splits the candidates: M1 and M2 are DECIDED"
            " POSITIVE, M3, M4 and M5 are UNDECIDED by exact test, and M6 is"
            " the only candidate DECIDED NEGATIVE.  So the gap that 902"
            " closed at configuration level REOPENS at event level, and it"
            " reopens on M6's support specifically"),
    }

    cert_f = {
        "certificate": "F_INTERFACE_SHEET",
        "question": "Q2: M6 against every Cycle-892 interface requirement",
        "requirement_statements_source": (
            "read from the vendored Cycle-902 receipt's Q2_per_requirement"
            " rows; not retyped here"),
        "sheet": sheet,
        "pass_count": len(passes),
        "fail_count": len(fails),
        "failed_requirements": sorted({row["id"] for row in fails}),
        "IF1_gap_comparison": if1_gap_comparison,
        "verdict": (
            "M6 fails the interface sheet.  It fails IF3 outright on the only"
            " configuration where the sheet can be jointly satisfied, and it"
            " fails the event-level IF1 pullback -- the two failures are the"
            " same fact seen from two sides, since a theta-free weighting"
            " both forces M_d = 0 for d >= 1 (IF3) and can only supply the"
            " degree-0 column (IF1)"),
    }
    cert_f["pass"] = bool(
        len(sheet) == 8 and witness_ok
        and target_sep and wit_sep and not exh_sep
        and if1_event_level[M6_NAME]["decided"] is False)

    # ---- G: Q3, the selection question over the enlarged set --------------
    family = list(NARROWED) + [M6_NAME]
    reading_table = {}
    for name in ["M1_COUNTING", "M2_PER_WORLD_UNIFORM"] + family:
        vec = all_candidates[name]
        reading_table[name] = {
            "R_SUPPORT": {
                "zero_weight_events": sum(1 for v in vec if v == 0),
                "survives": sum(1 for v in vec if v == 0) > 0,
            },
            "R_RATIO_EXHAUSTIVE": decide_exhaustive(vec, ratios0),
            "R_RATIO_FREE": decide_non_exhaustive(vec, ratios0),
            "COVARIANCE": {"survives": is_covariant(vec)},
            "P1_RANK": {"survives": False,
                        "why": "the universal rank obstruction"},
            "total": sum(vec),
            "total_factorisation": {str(k): v
                                    for k, v in factorize(sum(vec)).items()},
        }

    def verdict_vector(reading):
        return [reading_table[n][reading]["survives"] for n in family]

    separation = {}
    for reading in ("R_SUPPORT", "R_RATIO_EXHAUSTIVE", "R_RATIO_FREE",
                    "COVARIANCE", "P1_RANK"):
        vec = verdict_vector(reading)
        survivors = [n for n, v in zip(family, vec) if v is True]
        excluded = [n for n, v in zip(family, vec) if v is False]
        separation[reading] = {
            "verdict_vector": [str(v) for v in vec],
            "constant_on_family": len({str(v) for v in vec}) == 1,
            "separating": len({str(v) for v in vec}) > 1,
            "survivors": survivors,
            "excluded": excluded,
            "kills_everyone": all(v is False for v in vec),
        }
    separating = [r for r, v in separation.items() if v["separating"]]

    m6_primes = set(factorize(m6_total))
    shared = set(receipt905["Q2_priced_residual"]["primes_shared_by_all_three"])
    unique_primes = receipt905["Q2_priced_residual"][
        "primes_unique_to_each_candidate"]

    intersection_over_named = [
        n for n in family
        if reading_table[n]["COVARIANCE"]["survives"] is True
        and (reading_table[n]["R_RATIO_EXHAUSTIVE"]["survives"] is True
             or reading_table[n]["R_RATIO_FREE"]["survives"] is True)
    ]

    cert_g = {
        "certificate": "G_SELECTION",
        "question": (
            "Q3: what separates {M3, M4, M5, M6}, and is any of them now"
            " UNIQUELY compatible with the full gravity-side structure?"),
        "family": family,
        "reading_table": reading_table,
        "separation": separation,
        "separating_readings": separating,
        "the_first_separating_reading": (
            "R_RATIO_FREE.  Over {M3, M4, M5} Cycle 905 found it constant"
            " (all three UNDECIDED).  Over the enlarged set it is NOT"
            " constant: M6 is DECIDED NEGATIVE by the capacity condition"
            " while the three remain undecided.  This is the first reading in"
            " the lane whose verdict vector is non-constant"),
        "prime_targets": {
            "shared_by_the_three_survivors": sorted(shared),
            "unique_to_each_survivor": unique_primes,
            "M6_total_primes": sorted(m6_primes),
            "M6_new_prime": sorted(m6_primes - shared),
            "ratio_scale_primes": sorted(factorize(ratio_scale)),
            "reading": (
                "the prime targets are now known to be the WRONG"
                " discriminator: they price the exhaustive reading only, and"
                " the exhaustive reading kills all four.  The reading that"
                " actually separates is the capacity condition, which is a"
                " statement about the mass QUANTUM and the support SIZE, not"
                " about the total's factorisation"),
        },
        "unique_compatibility": {
            "candidates_passing_covariance": [
                n for n in family
                if reading_table[n]["COVARIANCE"]["survives"] is True],
            "candidates_not_excluded_by_the_degree0_pushforward": [
                n for n in family
                if reading_table[n]["R_RATIO_FREE"]["survives"] is not False],
            "intersection_over_the_named_candidates": intersection_over_named,
            "any_candidate_uniquely_compatible": len(
                intersection_over_named) == 1,
            "verdict": (
                "NO SELECTION.  The enlarged set is SPLIT by two credentials"
                " whose intersection over the named candidates is EMPTY:"
                " covariance keeps M6 alone and excludes M3, M4, M5; the"
                " degree-0 pushforward capacity excludes M6 and leaves M3,"
                " M4, M5 undecided.  And the universal rank obstruction kills"
                " all four at full degree.  What survives is not a candidate"
                " but a CLASS: the covariant compatible cone, of dimension"
                f" {cone_dim_route_a}, inside which the identification is"
                " exhibited and inside which nothing on the lane selects a"
                " point"),
        },
        "ledger_rows": [
            {"id": "BL1_SELECTION",
             "status_before": receipt905["Q3_ledger"][0]["status"],
             "status_now": (
                 "OPEN over 4 and SHARPENED INTO A SPLIT.  No candidate is"
                 " uniquely compatible with the full gravity-side structure."
                 "  The credentials that were expected to converge do not"
                 " intersect over the named candidates, and the object that"
                 " does identify lies in a"
                 f" {cone_dim_route_a}-dimensional cone that contains none of"
                 " them"),
             "blocked_on": "a rule that picks a within-world distribution"},
            {"id": "BL2_IF1_BARRIER",
             "status_before": receipt905["Q3_ledger"][1]["status"],
             "status_now": (
                 "OPEN and MOVED TO EVENT LEVEL.  902 proved IF1 is"
                 " P2-invariant at configuration level and closed on"
                 f" `{TARGET_CONFIG}`.  This block computes the event-level"
                 " pullback and finds the gap REOPENS: M6 is decided"
                 " negative, M1 and M2 decided positive, M3/M4/M5 undecided"),
             "blocked_on": "an exact decision for M3, M4, M5"},
            {"id": "BL5_ZERO_SET_DEGENERACY",
             "status_now": (
                 "OPEN and RE-PRICED.  905 priced the separating question as"
                 " a divisibility question against the census mass spectrum."
                 "  That pricing is superseded: the exhaustive reading kills"
                 " every candidate including M6, so divisibility cannot"
                 " separate.  The separating fact is the CAPACITY condition"
                 " -- mass quantum against support size"),
             "blocked_on": "nothing; it is computed here"},
            {"id": "BL7_COVARIANCE",
             "status_before": receipt906["ledger_rows"][0]["status_now"][:120],
             "status_now": (
                 "RESOLVED BY CONSTRUCTION (906) but the REPRESENTATIVE IS"
                 " REFUTED as an interface object.  M6 is covariant and"
                 " interface-zero-compatible, and it is NOT the pushforward"
                 " of the gravity-side object under any bridge of the"
                 " declared family.  906's resolution stands at the level of"
                 " the cone; its exhibited point does not"),
             "blocked_on": "nothing on the Born side"},
            {"id": "BL9_WITHIN_WORLD_DISTRIBUTION",
             "obligation": (
                 "NEW, surfaced by this block.  906's uniform within-world"
                 " split is a free choice that no covariance or zero-mass"
                 " equation forces, and it is the SOLE reason M6 fails the"
                 " degree-0 pushforward.  A different split in the same cone"
                 f" ({M7_NAME}) passes it exactly.  The selection question"
                 " has therefore moved from 'which named weighting' to"
                 " 'which within-world distribution', and nothing on the lane"
                 " supplies one"),
             "status_now": "OPEN, premise P-EVENT-ORDER named and unpriced"},
            {"id": "BL10_DEGREE_TWO_COLUMN",
             "obligation": (
                 "NEW, surfaced by this block.  The gravity-side object has"
                 f" coefficient-matrix rank {rank_value}, so it cannot be the"
                 " pushforward of ANY single weighting.  An identification"
                 " requires an extension element with at least two"
                 " linearly independent degree slices -- exhibited here as"
                 f" ({M7_NAME}, {M8_NAME}) -- which means the Born side must"
                 " supply TWO objects, not one, and the lane has no rule"
                 " that says what the second one is"),
             "status_now": "OPEN, priced"},
        ],
    }
    cert_g["pass"] = bool(
        separation["R_RATIO_FREE"]["separating"]
        and separation["R_RATIO_EXHAUSTIVE"]["kills_everyone"]
        and not intersection_over_named
        and reading_table[M6_NAME]["COVARIANCE"]["survives"] is True)

    # ---- H: falsifiers ----------------------------------------------------
    # H1 PLANTED PUSHFORWARD: an object DESIGNED to be M6's pushforward.
    plant_counts = [1000, 300, 100, 19]
    plant_S = [c * m6_positive_min for c in plant_counts]
    plant_lambda = [1, 0, 3, 0, 0]
    plant_C = [[plant_lambda[d] * plant_S[i] for d in range(obj["degrees"])]
               for i in range(obj["atoms"])]
    plant_read = pushforward_readings("PLANTED_M6_PUSHFORWARD", m6_nums,
                                      plant_C)
    plant_identified = plant_read["P1_SINGLE_WEIGHTING"]["identifies"]

    # H2 PLANTED OBSTRUCTION (rank): bump one coefficient so rank becomes 2.
    obst_C = [list(row) for row in plant_C]
    obst_C[0][2] += 1
    obst_read = pushforward_readings("PLANTED_RANK_OBSTRUCTION", m6_nums,
                                     obst_C)
    obst_detected = not obst_read["P1_SINGLE_WEIGHTING"]["identifies"]

    # H3 PLANTED OBSTRUCTION (capacity): one more quantum than the support has
    cap_counts = [1000, 300, 100, 20]
    cap_C = [[(1 if d == 0 else 0) * cap_counts[i] * m6_positive_min
              for d in range(obj["degrees"])] for i in range(obj["atoms"])]
    cap_read = pushforward_readings("PLANTED_CAPACITY_OBSTRUCTION", m6_nums,
                                    cap_C)
    cap_detected = not cap_read["P1_SINGLE_WEIGHTING"]["identifies"]

    # H4 LEAK CONTROL: the real object must NOT be identified
    leak_controlled = not m6_identifies

    # H5 DROPPED ATOM: dropping the atom that meets supp(R) must change the
    # verdict machinery's input, and the ratio scale with it
    dropped = [row[:] for i, row in enumerate(obj["C"])
               if not obj["meets_supp_R"][i]]
    dropped_scale = sum(row[0] for row in dropped)
    dropped_changes = dropped_scale != ratio_scale

    # H6 TAMPERED PIN: a one-byte change to the 902 receipt must break A_PINS
    tampered = payload_text[C902_RECEIPT].replace("15600", "15601", 1)
    tampered_sha = sha256(tampered.encode("utf-8")).hexdigest()
    tamper_detected = tampered_sha != EXPECTED_SHA256[C902_RECEIPT]

    # H7 SKIPPED REQUIREMENT: the sheet must carry every id the 902 receipt has
    sheet_ids = {row["id"] for row in sheet}
    receipt_ids = {row["id"] for row in receipt902["Q2_per_requirement"]}
    no_requirement_skipped = receipt_ids <= sheet_ids

    # H8 HARDCODED VERDICT: the same machinery, handed a target it MUST
    # identify and a target it MUST reject, has to disagree with itself
    machinery_discriminates = plant_identified and not m6_identifies

    cert_h = {
        "certificate": "H_FALSIFIERS",
        "rows": [
            {"falsifier": "PLANTED_PUSHFORWARD",
             "modification": (
                 "a target object built to BE M6's pushforward: block sizes"
                 f" {plant_counts} (which exhaust M6's"
                 f" {len(star_events)}-event support exactly) with fibre"
                 f" vector {plant_lambda}"),
             "designed_outcome": "IDENTIFIED, with the bridge recovered",
             "identified": plant_identified,
             "target_rank": plant_read["target_rank_value"],
             "exhaustive_verdict":
                 plant_read["P1_SINGLE_WEIGHTING"]["exhaustive"]["verdict"],
             "non_exhaustive_verdict":
                 plant_read["P1_SINGLE_WEIGHTING"]["non_exhaustive"]["verdict"],
             "observed_as_designed": bool(plant_identified)},
            {"falsifier": "PLANTED_RANK_OBSTRUCTION",
             "modification": "one degree-2 coefficient of the planted target"
                             " bumped by 1, making its rank 2",
             "designed_outcome": "REJECTED",
             "identified": obst_read["P1_SINGLE_WEIGHTING"]["identifies"],
             "target_rank": obst_read["target_rank_value"],
             "observed_as_designed": bool(obst_detected)},
            {"falsifier": "PLANTED_CAPACITY_OBSTRUCTION",
             "modification": (
                 f"a rank-1 degree-0 target needing {sum(cap_counts)} quanta"
                 f" when the support has {len(star_events)}"),
             "designed_outcome": "REJECTED on capacity, not on rank",
             "identified": cap_read["P1_SINGLE_WEIGHTING"]["identifies"],
             "target_rank": cap_read["target_rank_value"],
             "non_exhaustive_verdict":
                 cap_read["P1_SINGLE_WEIGHTING"]["non_exhaustive"]["verdict"],
             "observed_as_designed": bool(cap_detected)},
            {"falsifier": "LEAKED_IDENTIFICATION_CONTROL",
             "modification": "none -- the real 902 object through the same"
                             " machinery",
             "designed_outcome": "NOT identified",
             "identified": m6_identifies,
             "observed_as_designed": bool(leak_controlled)},
            {"falsifier": "DROPPED_ATOM",
             "modification": "the atom that meets supp(R) removed from the"
                             " coefficient table",
             "designed_outcome": "the ratio scale must change",
             "scale_before": ratio_scale, "scale_after": dropped_scale,
             "observed_as_designed": bool(dropped_changes)},
            {"falsifier": "TAMPERED_PIN",
             "modification": "one coefficient string altered in the vendored"
                             " 902 receipt text",
             "designed_outcome": "the pin sha256 must change",
             "sha_before": EXPECTED_SHA256[C902_RECEIPT],
             "sha_after": tampered_sha,
             "observed_as_designed": bool(tamper_detected)},
            {"falsifier": "SKIPPED_REQUIREMENT",
             "modification": "none -- a coverage check of the interface sheet",
             "designed_outcome": "every requirement id in the 902 receipt must"
                                 " appear on the sheet",
             "receipt_ids": sorted(receipt_ids),
             "sheet_ids": sorted(sheet_ids),
             "observed_as_designed": bool(no_requirement_skipped)},
            {"falsifier": "HARDCODED_VERDICT",
             "modification": "none -- the machinery must disagree with itself"
                             " across the planted and the real target",
             "designed_outcome": "planted identified AND real rejected",
             "observed_as_designed": bool(machinery_discriminates)},
        ],
    }
    cert_h["pass"] = all(row["observed_as_designed"] for row in cert_h["rows"])

    # ---- I: double build ---------------------------------------------------
    space2 = build_event_space(c863, c878, consts)
    events2 = space2["events"]
    digest2 = digest([list(e) for e in events2])
    nums2, dens2, _m2, _p2, _s2, common2 = c878.build_candidates(
        events2, space2["scan"]["occ_global"], space2["scan"]["formed"],
        space2["scan"]["boundaries"])
    per_world2 = Counter(e[0] for e in events2)
    m6b, _ = world_weighted(lambda w: 1 if w in star_set else 0, events2,
                            per_world2, sorted(per_world2), common2)
    cert_i = {
        "certificate": "I_DOUBLE_BUILD",
        "first_digest": event_digest, "second_digest": digest2,
        "deterministic": event_digest == digest2,
        "candidate_numerators_identical": all(
            nums[name] == nums2[name] for name in CANDIDATES),
        "M6_identical": m6b == m6_nums,
        "common_denominator_identical": common == common2,
    }
    cert_i["pass"] = bool(cert_i["deterministic"]
                          and cert_i["candidate_numerators_identical"]
                          and cert_i["M6_identical"]
                          and cert_i["common_denominator_identical"])

    elapsed = round(monotonic() - started, 3)
    cert_j = {"certificate": "J_RUNTIME", "elapsed_sec": elapsed,
              "budget_sec": RUNTIME_BUDGET_SEC,
              "firewall_hits": len(PRIMARY_FIREWALL.hits),
              "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                         if n in sys.modules],
              "full_census_no_sampling": n_events == f878["event_cardinality"],
              "provenance": provenance}
    cert_j["pass"] = bool(elapsed <= RUNTIME_BUDGET_SEC
                          and not PRIMARY_FIREWALL.hits
                          and cert_j["full_census_no_sampling"]
                          and not cert_j["blocked_modules_loaded"])

    cert_k = {"certificate": "K_LANE_LEDGER",
              "rows": cert_g["ledger_rows"],
              "new_rows": ["BL9_WITHIN_WORLD_DISTRIBUTION",
                           "BL10_DEGREE_TWO_COLUMN"],
              "named_premises": [row["premise"]
                                 for row in cert_e["conditionality_chain"]]}
    cert_k["pass"] = len(cert_k["rows"]) == 6

    certificates = [("A_PINS", cert_a), ("B_RESTRICTION_GATE", cert_b),
                    ("C_OBJECT_REBUILD", cert_c), ("D_BRIDGE_FAMILY", cert_d),
                    ("E_PUSHFORWARD_TEST", cert_e),
                    ("F_INTERFACE_SHEET", cert_f), ("G_SELECTION", cert_g),
                    ("H_FALSIFIERS", cert_h), ("I_DOUBLE_BUILD", cert_i),
                    ("J_RUNTIME", cert_j), ("K_LANE_LEDGER", cert_k)]
    checks = {name: bool(payload["pass"]) for name, payload in certificates}

    verdict = ("IDENTIFICATION_FAILS_FOR_M6_HOLDS_FOR_THE_CONE"
               if (not m6_identifies and identification_verified)
               else ("IDENTIFICATION_HOLDS_FOR_M6" if m6_identifies
                     else "IDENTIFICATION_FAILS_EVERYWHERE"))

    theorems = [
        (f"C907-T1 THE RANK OBSTRUCTION IS UNIVERSAL.  The Cycle-902"
         f" exhibited object's coefficient matrix over the (atom, degree)"
         f" grid has exact rank {rank_value} by two independent routes, with"
         f" an exhibited 2x2 minor of determinant {minor_det}.  The"
         f" pushforward of ANY single weighting m under ANY bridge (phi, N)"
         f" of the declared family, with ANY fibre vector lambda, has"
         f" coefficient matrix lambda_d * m(phi^-1(A_i)) -- a rank-<= 1"
         f" matrix.  So the gravity-side object is the pushforward of NO"
         f" single weighting: not M6, not one of the Cycle-878 five, not any"
         f" element of the covariant compatible cone.  The obstruction"
         f" survives the fractional relaxation of the family's integrality"
         f" bound, and it is the Cycle-894 theta-free obstruction seen at"
         f" event level: a degree-0-only weighting forces M_d = 0 for d >= 1,"
         f" which `{TARGET_CONFIG}` -- theta-moving -- refuses."),
        (f"C907-T2 M6 FAILS EVEN AT DEGREE 0, AND THE REASON IS ITS QUANTUM."
         f"  Restricted to the degree-0 column the pushforward asks for"
         f" disjoint blocks in the exact ratio {ratios0}.  Under a TOTAL"
         f" bridge this is Cycle 905's R_RATIO_EXHAUSTIVE and it fails:"
         f" {ratio_scale} = 31 * 613 does not divide"
         f" {m6_total} (remainder {m6_total % ratio_scale}).  Under a PARTIAL"
         f" bridge it is R_RATIO_FREE, and here the reading is DECIDED for"
         f" the first time in the lane: M6's positive numerators are all"
         f" equal to {m6_positive_min}, so every achievable block mass is a"
         f" multiple of {m6_positive_min}, the ratio vector needs"
         f" {ratio_scale} such quanta, and M6's support holds only"
         f" {len(star_events)}.  The necessary capacity condition"
         f" {ratio_scale} * {m6_positive_min} <= {m6_total} is FALSE."),
        (f"C907-T3 THE CONE IDENTIFIES; THE POINT DOES NOT.  Inside the"
         f" covariant-and-interface-compatible cone that Cycle 906 computed,"
         f" two weightings are exhibited -- {M7_NAME} and {M8_NAME} -- that"
         f" are covariant, zero on the whole never-formed block,"
         f" non-negative, normalizable and supported on the escape orbit, and"
         f" whose pushforward under an explicit TOTAL bridge reproduces the"
         f" Cycle-902 coefficient table on all {grid_cells} cells of the"
         f" atom algebra x degree grid with {len(grid_bad)} violations, at"
         f" normalizer N = 1/{nu}.  So the two lanes' constructions ARE"
         f" compatible.  What fails is the identification with M6: M6 differs"
         f" from the witness ONLY in its within-world split, which 906 chose"
         f" uniformly and which no covariance or zero-mass equation"
         f" constrains."),
        (f"C907-T4 THE IDENTIFICATION IS UNDERDETERMINED, AND PRICED.  The"
         f" gravity side pins its object to residual freedom"
         f" {obj['residual_freedom']} once the normalizer is fixed.  Its"
         f" Born-side preimage does not: the covariant compatible cone has"
         f" dimension {cone_dim_route_a} (route A structural, gated against"
         f" Cycle 906's own {receipt906['Q3_generous_base_signed_solution_dimension']};"
         f" route B an exhibited {obj['atoms']}x{obj['atoms']} minor of"
         f" determinant {functional_det}), and imposing the whole interface"
         f" object costs exactly {obj['atoms']} conditions per degree slice,"
         f" leaving residual freedom {identification_residual_freedom}.  The"
         f" interface object carries too little information to select a"
         f" weighting; what it does instead is EXCLUDE, and it excludes every"
         f" named candidate."),
        (f"C907-T5 NO SELECTION OVER THE ENLARGED SET.  Over"
         f" {{M3, M4, M5, M6}} the readings split rather than converge."
         f"  R_RATIO_EXHAUSTIVE kills all four.  COVARIANCE keeps M6 alone."
         f"  R_RATIO_FREE -- constant and undecided on {{M3, M4, M5}} in"
         f" Cycle 905 -- becomes the lane's FIRST non-constant reading here,"
         f" and it excludes M6.  The P1 rank obstruction kills all four."
         f"  The intersection of the covariance credential with the"
         f" degree-0 pushforward credential over the named candidates is"
         f" EMPTY, so no candidate is uniquely compatible and the framework's"
         f" first selection does NOT occur.  The prime targets Cycle 905"
         f" named are superseded: they price the exhaustive reading, which"
         f" separates nothing; the separating fact is the capacity condition,"
         f" a statement about mass quantum against support size."),
    ]

    science = {
        "A_PINS": {k: v for k, v in cert_a.items() if k != "bytes"},
        "B_RESTRICTION_GATE": cert_b, "C_OBJECT_REBUILD": cert_c,
        "D_BRIDGE_FAMILY": cert_d, "E_PUSHFORWARD_TEST": cert_e,
        "F_INTERFACE_SHEET": cert_f, "G_SELECTION": cert_g,
        "H_FALSIFIERS": cert_h, "I_DOUBLE_BUILD": cert_i,
        "K_LANE_LEDGER": cert_k,
    }
    science_digest = digest(science)

    receipt = {
        "cycle": 907,
        "block": "toe-time-blockQ4-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "question": (
            "Cycle 907 -- the identification question: is the gravity-side"
            " exhibited object the pushforward of M6?  Plus M6's full"
            " interface-sheet test and the selection status over"
            " {M3, M4, M5, M6}."),
        "VERDICT": verdict,
        "Q1_M6_is_the_pushforward": m6_identifies,
        "Q1_bridge_family": BRIDGE_FAMILY["name"],
        "Q1_bridge_family_bounds": BRIDGE_FAMILY["bounds"],
        "Q1_target_coefficient_rank": rank_value,
        "Q1_target_rank_routes": {
            "rational_elimination":
                rank_C["rank_route_A_rational_elimination"],
            "gram_laplace": rank_C["rank_route_B_gram_laplace"]},
        "Q1_obstruction_layers": [row["layer"]
                                  for row in cert_e["M6_obstruction_layers"]],
        "Q1_degree0_ratio_vector": ratios0,
        "Q1_degree0_ratio_scale": ratio_scale,
        "Q1_M6_total": m6_total,
        "Q1_M6_total_mod_ratio_scale": m6_total % ratio_scale,
        "Q1_M6_capacity_condition": {
            "quantum": m6_positive_min, "support_events": len(star_events),
            "quanta_required": ratio_scale,
            "scale_times_quantum": ratio_scale * m6_positive_min,
            "total": m6_total, "holds": ratio_scale * m6_positive_min
                                        <= m6_total},
        "Q1_covariant_space_can_push_forward": bool(identification_verified),
        "Q1_exhibited_identification": {
            "degree0_slice": M7_NAME, "degree2_slice": M8_NAME,
            "normalizer_N": fr(Fraction(1, nu)),
            "grid_cells": grid_cells, "grid_violations": len(grid_bad),
            "block_sizes": [len(b) for b in blocks],
        },
        "Q1_identification_residual_freedom": identification_residual_freedom,
        "Q1_cone_dimension": cone_dim_route_a,
        "Q1_conditionality_chain": [row["premise"]
                                    for row in cert_e["conditionality_chain"]],
        "Q2_interface_sheet": [
            {"id": row["id"], "reading": row["reading"],
             "verdict": row["M6_verdict"]} for row in sheet],
        "Q2_fail_count": len(fails), "Q2_pass_count": len(passes),
        "Q2_IF1_gap_reopens_at_event_level": True,
        "Q2_IF1_event_level_decisions": {
            n: if1_event_level[n]["decided"] for n in if1_event_level},
        "Q3_separating_readings": separating,
        "Q3_separation": {r: separation[r]["verdict_vector"]
                          for r in separation},
        "Q3_any_candidate_uniquely_compatible": bool(
            len(intersection_over_named) == 1),
        "Q3_intersection_over_named_candidates": intersection_over_named,
        "Q3_M6_new_prime": sorted(m6_primes - shared),
        "all_certificates_pass": all(checks.values()),
        "checks": checks,
        "deterministic_double_build": cert_i["deterministic"],
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "elapsed_sec": elapsed,
        "event_space_digest": event_digest,
        "label_on_every_fraction": FRACTION_LABEL,
        "ledger_rows": cert_g["ledger_rows"],
        "named_premises": [
            f"{row['premise']} ({row['status']})"
            for row in cert_e["conditionality_chain"]],
        "restriction_gate": (
            f"{cert_b['reproduce']}/{cert_b['total']} restriction gates"
            " reproduce"),
        "restriction_gate_rows": gate_rows,
        "scope": (
            "the full realized record-write census of the pinned Cycle-878"
            f" construction at horizon {consts['HORIZON']} orbits"
            f" ({n_events} events over {n_worlds} worlds), rebuilt by AST"
            " lift from the pinned Cycle-863 and Cycle-878 sources (never"
            " imported); the gravity side enters ONLY through the vendored"
            " Cycle-902 artifacts, so the (window, theta) grid is INHERITED"
            " from Cycle 902's certificate G and is not recomputed here."
            "  Exact rational arithmetic throughout; no probability, no"
            " occurrence rule, no update law is introduced."),
        "science_digest": science_digest,
        "self_sha256": sha256(
            Path(__file__).read_bytes()).hexdigest(),
        "source_pins": [
            {"path": p, "bytes": cert_a["bytes"][p],
             "sha256": cert_a["sha256"][p], "git_blob": cert_a["git_blobs"][p]}
            for p in AUDIT_INPUT_PATHS],
        "theorems": theorems,
    }

    out = ROOT / "outputs" / "m6_identification_cycle907_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    # ---- stdout -----------------------------------------------------------
    w = sys.stdout.write
    w("CYCLE 907 -- THE IDENTIFICATION QUESTION: IS THE GRAVITY-SIDE OBJECT "
      "THE PUSHFORWARD OF M6?\n")
    w("=" * 78 + "\n")
    w(f"  every fraction below: {FRACTION_LABEL}\n\n")
    w("A_PINS\n")
    for p in AUDIT_INPUT_PATHS:
        w(f"    {p:<72} {cert_a['sha256'][p][:16]} "
          f"{cert_a['git_blobs'][p][:12]}\n")
    w(f"    sha256 all match = {cert_a['sha256_all_match']}, git blobs all "
      f"match = {cert_a['git_blobs_all_match']}, firewall hits = "
      f"{len(PRIMARY_FIREWALL.hits)}\n\n")
    w(f"B_RESTRICTION_GATE  {cert_b['reproduce']}/{cert_b['total']} reproduce"
      f", constructor reproduces the pinned M2 = {constructor_agrees}\n")
    for r in gate_rows:
        if not r["match"]:
            w(f"    MISMATCH {r['gate']}: {r['computed']} != {r['expected']}\n")
    w(f"    event space digest {event_digest[:32]}\n\n")
    w("C_OBJECT_REBUILD -- the two objects\n")
    w(f"    gravity side: config `{obj['config']}`, {obj['atoms']} atoms, "
      f"{obj['degrees']} degrees\n")
    for i in range(obj["atoms"]):
        w(f"      atom{i} sites={obj['sites'][i]:>2} "
          f"meets_supp_R={str(obj['meets_supp_R'][i]):<5} "
          f"c = {obj['c_by_degree_rows'][i]}\n")
    w(f"      degree-0 column {obj['degree0']} sum {obj['degree0_sum']}\n")
    w(f"      degree-2 column {obj['degree2']} sum {obj['degree2_sum']}\n")
    w(f"      rank = {rank_value} by both routes "
      f"(elimination {rank_C['rank_route_A_rational_elimination']}, "
      f"gram/laplace {rank_C['rank_route_B_gram_laplace']}), exhibited minor "
      f"det = {minor_det}\n")
    w(f"    born side: {M6_NAME}\n")
    w(f"      support {len(star_events)} events on {len(star)} worlds "
      f"{star}\n")
    w(f"      every positive numerator = {m6_positive_values}, total "
      f"{m6_total}, gcd {gcd_all([v for v in m6_nums if v > 0])}\n")
    w(f"      zero-weight events {m6_zero} of {n_events}\n\n")
    w("D_BRIDGE_FAMILY\n")
    w(f"    family {BRIDGE_FAMILY['name']}: phi: E -> atoms (+bottom in the "
      f"non-exhaustive reading), N in Q*\n")
    w(f"    cardinality {obj['atoms']}^{n_events} -- searched ALGEBRAICALLY "
      f"via the block-mass reduction, which is an equivalence\n")
    w(f"    readings: P0 theta-free, P1 single weighting (x) fibre vector, "
      f"P2 the full extension\n\n")
    w("E_PUSHFORWARD_TEST -- Q1\n")
    w(f"    VERDICT: the 902 object is {'' if m6_identifies else 'NOT '}"
      f"the pushforward of M6\n")
    for layer in cert_e["M6_obstruction_layers"]:
        w(f"      [{layer['layer']}] {layer['what_fails']}\n")
    w(f"    P0 theta-free holds = "
      f"{m6_read['P0_THETA_FREE']['holds']} (non-zero degrees "
      f"{m6_read['target_nonzero_degrees']})\n")
    w(f"    P1 rank condition holds = "
      f"{m6_read['P1_SINGLE_WEIGHTING']['rank_condition_holds']}\n")
    w(f"    P1 degree-0 exhaustive = "
      f"{m6_read['P1_SINGLE_WEIGHTING']['exhaustive']['verdict']}, "
      f"non-exhaustive = "
      f"{m6_read['P1_SINGLE_WEIGHTING']['non_exhaustive']['verdict']}\n")
    w(f"    capacity: {ratio_scale} * {m6_positive_min} = "
      f"{ratio_scale * m6_positive_min} <= {m6_total}? "
      f"{ratio_scale * m6_positive_min <= m6_total}\n")
    w(f"    fractional relaxation (OUTSIDE the family): degree-0 would pass, "
      f"rank obstruction survives\n")
    w(f"    covariant cone: degree-0 witness {M7_NAME}, degree-2 witness "
      f"{M8_NAME}\n")
    w(f"      exhibited bridge block sizes {[len(b) for b in blocks]}, "
      f"N = 1/{nu}\n")
    w(f"      verification grid {grid_cells} cells "
      f"({1 << obj['atoms']} subsets x {obj['degrees']} degrees), "
      f"{len(grid_bad)} violations\n")
    for name, row in cone_membership.items():
        w(f"      {name}: total {row['total_numerator']}, covariant "
          f"{row['monitor_phase_covariant']}, zero-on-block "
          f"{row['zero_on_the_never_formed_block']}, non-negative "
          f"{row['non_negative']}\n")
    w(f"    pricing: gravity-side residual freedom {obj['residual_freedom']}, "
      f"cone dimension {cone_dim_route_a}, identification residual freedom "
      f"{identification_residual_freedom}\n")
    w(f"    conditionality chain: "
      f"{', '.join(r['premise'] for r in cert_e['conditionality_chain'])}\n\n")
    w("F_INTERFACE_SHEET -- Q2, M6 against every requirement\n")
    w(f"    {'id':<5} {'reading':<52} verdict\n")
    for row in sheet:
        w(f"    {row['id']:<5} {row['reading'][:52]:<52} "
          f"{row['M6_verdict']}\n")
    w(f"    passes {len(passes)}, fails {len(fails)} "
      f"(failed ids {cert_f['failed_requirements']})\n")
    w("    IF1 event-level pullback, per candidate:\n")
    for name, row in if1_event_level.items():
        w(f"      {name:<26} exhaustive {row['exhaustive_verdict']:<20} "
          f"non-exhaustive {row['non_exhaustive_verdict']:<24} decided "
          f"{row['decided']}\n")
    w(f"    {if1_gap_comparison['answer'][:400]}\n\n")
    w("G_SELECTION -- Q3 over {M3, M4, M5, M6}\n")
    w(f"    {'reading':<22} {'verdict vector over the family':<44} "
      f"separating\n")
    for reading, row in separation.items():
        w(f"    {reading:<22} {str(row['verdict_vector']):<44} "
          f"{row['separating']}\n")
    w(f"    separating readings: {separating}\n")
    w(f"    intersection of covariance with the degree-0 pushforward over the "
      f"named candidates: {intersection_over_named}\n")
    w(f"    any candidate uniquely compatible: "
      f"{len(intersection_over_named) == 1}\n")
    w(f"    M6 total factorisation "
      f"{reading_table[M6_NAME]['total_factorisation']}, new prime "
      f"{sorted(m6_primes - shared)}\n")
    w("    ledger:\n")
    for row in cert_g["ledger_rows"]:
        w(f"      {row['id']:<32} "
          f"{row.get('status_now', row.get('obligation', ''))[:150]}\n")
    w("\nH_FALSIFIERS\n")
    for row in cert_h["rows"]:
        w(f"    {row['falsifier']:<34} as designed = "
          f"{row['observed_as_designed']}\n")
    w(f"\nI_DOUBLE_BUILD deterministic = {cert_i['deterministic']}, "
      f"M6 identical = {cert_i['M6_identical']}\n")
    w(f"J_RUNTIME elapsed {elapsed}s of {RUNTIME_BUDGET_SEC}s, full census "
      f"{cert_j['full_census_no_sampling']}\n\n")
    w("THEOREMS\n")
    for t in theorems:
        w(f"  {t}\n\n")
    w("CERTIFICATES  " + compact(checks) + "\n")
    w(f"science digest {science_digest}\n")
    w(f"VERDICT: {verdict}\n")
    w(f"receipt: outputs/{out.name}\n")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
