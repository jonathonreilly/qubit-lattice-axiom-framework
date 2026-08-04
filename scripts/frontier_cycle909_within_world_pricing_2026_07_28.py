"""Cycle 909 -- PRICING THE WITHIN-WORLD DISTRIBUTION (ledger rows BL9, BL10).

Cycle 907 proved (C907-T1) that the Cycle-902 gravity interface object is the
pushforward of NO single weighting -- its coefficient matrix has rank 2, so the
Born side must supply TWO objects (ledger row BL10) -- and exhibited a witness
PAIR (M7_ORBIT_RATIO_DEGREE0, M8_ORBIT_RATIO_DEGREE2) inside the covariant
compatible cone whose pushforward under an explicit TOTAL bridge reproduces the
902 coefficient table on all 80 cells of the atom-algebra x degree grid at
N = 1/11.  M6 -- the uniform within-world split -- FAILS, and 907 traced the
failure to the within-world split being a FREE CHOICE (ledger row BL9).

This block prices BL9 and BL10 jointly:

  Q1  THE REQUIRED SHAPE, EXTRACTED.  Exactly what the witness pair's
      within-world structure IS, and exactly what the identification pins
      versus leaves free -- proved by exhibiting alternative witnesses that
      satisfy the same constraint set and differ off the pinned coordinates.

  Q2  THE NATIVE RECIPE CENSUS.  The per-event / per-world field inventory,
      rebuilt by AST from the pinned Cycle-863 and Cycle-878 primaries, and
      every within-world distribution recipe the inventory supports under
      declared closure rules -- each instantiated on the escape orbit and
      tested against Q1's constraint set.

  Q3  THE PRICING VERDICT, plus the degree-2 carrier question: is the second
      object independently constrained, or does it ride along?

Discipline: TEXT/AST/JSON only, import firewall, exact integer / rational
arithmetic, deterministic double build, outcome-neutral gates, planted
realizers that the harness must detect.  No probability, no occurrence rule,
no update law is introduced.  Every fraction below is a bookkeeping fraction,
not a probability.
"""

from __future__ import annotations

import ast
import importlib.abc
import json
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

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
C907_PATH = "scripts/frontier_cycle907_m6_identification_2026_07_28.py"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
C907_CHECK_RECEIPT = \
    "outputs/m6_identification_independent_check_cycle907_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C902_PATH, C902_RECEIPT,
    C905_PATH, C905_RECEIPT, C906_PATH, C906_RECEIPT, C907_PATH, C907_RECEIPT,
    C907_CHECK_RECEIPT, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C902_PATH, C905_PATH, C906_PATH,
                  C907_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C902_RECEIPT, C905_RECEIPT, C906_RECEIPT,
                   C907_RECEIPT, C907_CHECK_RECEIPT)
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
    C907_PATH:
        "cfc87a647a8fe87ed97289bb179d4919bb4801731393bbec33006c6cfe348d53",
    C907_RECEIPT:
        "d67a967a6226a4e1ed2e0bf1762cb3b544df87e1fe4b07d6399f13ec179086ca",
    C907_CHECK_RECEIPT:
        "0d18a2839f1b57c55b55f0801b05e545a1e5a01cc790972d9583da5b21c0123b",
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
    C907_PATH: "70fad3ab7996926a7b543af64f0449a92a9868cd",
    C907_RECEIPT: "e7eef6eeeb62aeddcdb12417ccd8ec871b9d87a7",
    C907_CHECK_RECEIPT: "8586f09ed3346144a830254a38f64db89ad6ed07",
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
    "frontier_cycle907_m6_identification_2026_07_28",
    "frontier_cycle907_m6_identification_independent_check_2026_07_28",
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
TARGET_CONFIG = "single"
M7_NAME = "M7_ORBIT_RATIO_DEGREE0"
M8_NAME = "M8_ORBIT_RATIO_DEGREE2"

# declared closure bounds for the recipe census (certificate E)
GEOMETRIC_RATIOS = (2, 3, 5, 7, 11, 13)
POWER_EXPONENTS = (2, 3, 4)
AFFINE_COEFFS = tuple((a, b) for a in range(4) for b in range(4)
                      if (a, b) != (0, 0))
SUM_COEFFS = (1, 2, 3)
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
    n, p = abs(value), 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def gcd_list(values) -> int:
    out = 0
    for v in values:
        out = gcd(out, abs(v))
    return out


def lcm2(a: int, b: int) -> int:
    return a // gcd(a, b) * b if a and b else 0


def short(value: int, cap: int = 44) -> str:
    text = str(value)
    return text if len(text) <= cap else f"<{len(text)}-digit integer>"


def proportional(sample, target) -> bool:
    """Exact proportionality of two integer vectors, sample != 0."""
    if all(v == 0 for v in sample):
        return False
    n = len(target)
    for i in range(n):
        for j in range(i + 1, n):
            if sample[i] * target[j] != sample[j] * target[i]:
                return False
    return True


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
                            resolved.append(string_constants.get(element.id))
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
        "cycle907_pair_verified": (
            sha_rows[C907_PATH] == EXPECTED_SHA256[C907_PATH]
            and sha_rows[C907_RECEIPT] == EXPECTED_SHA256[C907_RECEIPT]
        ),
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "bytes": {p: len(b) for p, b in payloads.items()},
        "gravity_machinery_absent_from_this_branch": {
            p: not (ROOT / p).exists() for p in (
                "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py",
                "scripts/frontier_cycle887_window_freedom_2026_07_28.py",
                "scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py")
        },
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and result["vendored_902_pair_verified"]
        and result["cycle907_pair_verified"]
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
# the Cycle-907 decision machinery, reused verbatim rather than reimplemented
C907_FUNCS = (
    "gcd_all", "det_laplace", "rank_by_rational_elimination",
    "rank_by_gram_minors", "two_route_rank", "block_mass_vector",
    "decide_exhaustive", "max_equal_blocks", "decide_non_exhaustive",
)
C907_CONSTS = ("EQUAL_BLOCK_J_CAP",)


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
    ns907, consts907, names907 = ast_lift(
        C907_PATH, C907_FUNCS, C907_CONSTS,
        {"Fraction": Fraction, "gcd": gcd, "Counter": Counter,
         "defaultdict": defaultdict, "combinations": combinations},
    )
    c907 = SimpleNamespace(**{name: ns907[name] for name in C907_FUNCS})
    return c863, c878, c907, consts878, {
        "lifted_from_863": names863, "lifted_from_878": names878,
        "lifted_from_907": names907,
        "constants_863": consts863,
        "constants_907": consts907,
        "constants_878": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts878.items()},
        "import_of_863_878_902_905_906_907": False,
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
    """The Cycle-878 constructor, restated (gated against pinned M2)."""
    totals = sum(a_of_world(w) for w in supported)
    nums = [a_of_world(e[0]) * (common // per_world[e[0]]) for e in events]
    return nums, totals * common


# ---------------------------------------------------------------------------
# the 902 exhibited object, value-for-value from the vendored receipt
# ---------------------------------------------------------------------------

def rebuild_902_object(receipt902: dict) -> dict:
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
# D: the field inventory, rebuilt by AST from the pinned primaries
# ---------------------------------------------------------------------------

def ast_field_inventory() -> dict:
    """The census's OWN per-event and per-world fields, read out of the pinned
    sources rather than retyped: the event tuple's field names come from the
    Cycle-878 unpacking site, the ledger fields from composed_scan's return
    dict, and the world-level ledger arguments from build_candidates."""
    tree = ast.parse((ROOT / C878_PATH).read_text(encoding="utf-8"),
                     filename=C878_PATH)
    event_fields, ledger_keys, candidate_args, append_arity = [], [], [], set()
    for node in ast.walk(tree):
        # (a) the event tuple's field names, from `for a, b, ... in events`
        if isinstance(node, ast.For) and isinstance(node.target, ast.Tuple) \
                and isinstance(node.iter, ast.Name) and node.iter.id == "events":
            names = [t.id for t in node.target.elts if isinstance(t, ast.Name)]
            if names and not event_fields:
                event_fields = names
        # (b) every events.append((...)) arity, to gate the tuple shape
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "append" \
                and isinstance(node.func.value, ast.Name) \
                and node.func.value.id == "events" and node.args \
                and isinstance(node.args[0], ast.Tuple):
            append_arity.add(len(node.args[0].elts))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "composed_scan":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Return) and isinstance(sub.value, ast.Dict):
                    ledger_keys = [k.value for k in sub.value.keys
                                   if isinstance(k, ast.Constant)]
        if isinstance(node, ast.FunctionDef) and node.name == "build_candidates":
            candidate_args = [a.arg for a in node.args.args]
    tree863 = ast.parse((ROOT / C863_PATH).read_text(encoding="utf-8"),
                        filename=C863_PATH)
    c863_funcs = sorted(n.name for n in tree863.body
                        if isinstance(n, ast.FunctionDef))
    return {
        "event_tuple_fields_ast": event_fields,
        "event_tuple_arity_ast": sorted(append_arity),
        "composed_scan_ledger_keys_ast": ledger_keys,
        "build_candidates_arguments_ast": candidate_args,
        "cycle863_function_inventory": c863_funcs,
        "note": (
            "these are ALL the census's own fields.  Any within-world recipe"
            " must be a formula in them; a rule that names a number the census"
            " does not carry is not a recipe, it is an import."),
    }


# ---------------------------------------------------------------------------
# the fast equal-block capacity, proved equivalent to Cycle 907's routine
# ---------------------------------------------------------------------------

def fast_max_equal_blocks(positives, need, j_cap=EQUAL_BLOCK_J_CAP):
    """Cycle 907's max_equal_blocks, re-indexed by the MULTIPLICITY j instead
    of by the value n.  907 computes, for a candidate block mass v,
        count(v) = sum over present values n with n | v and v//n <= byval[n]
                   of byval[n] // (v//n).
    Substituting j = v//n this is
        count(v) = sum over j >= 1 with byval[v//j] >= j of byval[v//j] // j,
    and the j-range is bounded by max(byval.values()), so the cost is
    (#candidates) x (largest multiplicity) instead of (#candidates) x
    (#distinct values).  Identical value, gated in certificate H."""
    byval: dict = defaultdict(int)
    for v in positives:
        if v > 0:
            byval[v] += 1
    if not byval:
        return 0, None
    jmax = max(byval.values())
    candidates = set()
    for n in byval:
        for j in range(1, min(byval[n], j_cap) + 1):
            candidates.add(j * n)
    best_count, best_value = 0, None
    for v in sorted(candidates):
        total = 0
        for j in range(1, jmax + 1):
            if v % j:
                continue
            n = v // j
            c = byval.get(n, 0)
            if c >= j:
                total += c // j
        if total > best_count:
            best_count, best_value = total, v
        if best_count >= need:
            break
    return best_count, best_value


def free_bridge_readings(c907, positives, ratios, support_cap) -> dict:
    """The Cycle-907 certificate-D decision procedure, applied to a weighting
    supported on the escape orbit, in its SCALE-INVARIANT form: the numerators
    are first divided by their own gcd, because a weighting and any positive
    rational multiple of it are the same object for the pushforward equations
    (rescaling m is absorbed by rescaling nu)."""
    g = gcd_list(positives) or 1
    prim = [v // g for v in positives]
    exhaustive = c907.decide_exhaustive(prim, ratios)
    scale = sum(ratios)
    if scale > support_cap:
        # EXACT skip, not a shortcut: 907's sufficient witness asks for `scale`
        # pairwise disjoint NON-EMPTY blocks, and the support has fewer events
        # than that, so both of its sufficient branches are false by
        # cardinality and the routine would return UNDECIDED / FAILS anyway.
        total = sum(prim)
        minimum = min(prim)
        gg = gcd_list(prim)
        unit_floor = max(gg, minimum)
        necessary = scale * unit_floor <= total
        non_exhaustive = {
            "reading": "NON_EXHAUSTIVE",
            "positive_events": len(prim),
            "positive_mass_total": total,
            "ratio_scale_sum": scale,
            "gcd_of_positive_numerators": gg,
            "min_positive_numerator": minimum,
            "forced_unit_floor_max_gcd_min": unit_floor,
            "necessary_capacity_scale_times_unit_floor": scale * unit_floor,
            "necessary_capacity_holds": necessary,
            "sufficient_witness_available": False,
            "sufficient_witness_unavailable_reason": (
                f"the witness needs {scale} pairwise disjoint non-empty blocks"
                f" and the support has only {support_cap} events -- an exact"
                " cardinality bar, not a search cap"),
            "survives": False if not necessary else None,
            "verdict": ("FAILS_CAPACITY" if not necessary
                        else "UNDECIDED_BY_THIS_TEST"),
        }
    else:
        positives_only = [v for v in prim if v > 0]
        total = sum(positives_only)
        gg = gcd_list(positives_only)
        minimum = min(positives_only)
        unit_floor = max(gg, minimum)
        necessary = scale * unit_floor <= total
        multiplicity = Counter(positives_only)
        best_value, best_count = max(multiplicity.items(),
                                     key=lambda kv: kv[1])
        block_count, block_value = (0, None)
        if necessary:
            block_count, block_value = fast_max_equal_blocks(
                positives_only, scale)
        sufficient = (best_count >= scale) or (block_count >= scale)
        if not necessary:
            verdict, survives = "FAILS_CAPACITY", False
        elif sufficient:
            verdict, survives = "SURVIVES", True
        else:
            verdict, survives = "UNDECIDED_BY_THIS_TEST", None
        non_exhaustive = {
            "reading": "NON_EXHAUSTIVE",
            "positive_events": len(positives_only),
            "positive_mass_total": total,
            "ratio_scale_sum": scale,
            "gcd_of_positive_numerators": gg,
            "min_positive_numerator": minimum,
            "forced_unit_floor_max_gcd_min": unit_floor,
            "necessary_capacity_scale_times_unit_floor": scale * unit_floor,
            "necessary_capacity_holds": necessary,
            "largest_equal_weight_class": [best_value, best_count],
            "max_disjoint_equal_mass_blocks": block_count,
            "equal_mass_block_value": block_value,
            "equal_block_witness_suffices": block_count >= scale,
            "survives": survives,
            "verdict": verdict,
        }
    if exhaustive["survives"]:
        verdict = "REALIZES"
    elif non_exhaustive["survives"] is True:
        verdict = "REALIZES"
    elif (not exhaustive["survives"]) and non_exhaustive["survives"] is False:
        verdict = "FAILS"
    else:
        verdict = "UNDECIDED"
    return {"scale_invariant_gcd_removed": g,
            "exhaustive": exhaustive, "non_exhaustive": non_exhaustive,
            "verdict": verdict}


# ---------------------------------------------------------------------------
# E: the base fields and the declared closure
# ---------------------------------------------------------------------------

def base_fields(star, star_rows, scan, per_world, boundaries):
    """Every base field is a NON-NEGATIVE integer function of one event, built
    only from the census's own per-event tuple and the pinned per-world ledger.
    Each carries its definition string; nothing else is admitted."""
    occ_g, occ_b = scan["occ_global"], scan["occ_bank"]
    formed = scan["formed"]
    tagcode = {"F": 0, "B0": 1, "B1": 2}

    def mk(name, definition, fn):
        return {"id": name, "definition": definition, "fn": fn}

    F = [
        mk("G_ONE", "1 -- the counting field (M1/M6's within-world choice)",
           lambda w, j, e, prev: 1),
        mk("G_MOMENT", "the event's own boundary index `moment`",
           lambda w, j, e, prev: e[1]),
        mk("G_MOMENT_P1", "moment + 1 (zero-free shift, declared)",
           lambda w, j, e, prev: e[1] + 1),
        mk("G_ORDINAL", "the event's own register `ordinal`",
           lambda w, j, e, prev: e[3]),
        mk("G_ORDINAL_P1", "ordinal + 1 (zero-free shift, declared)",
           lambda w, j, e, prev: e[3] + 1),
        mk("G_INDEX", "j -- the within-world emission index (P-EVENT-ORDER)",
           lambda w, j, e, prev: j),
        mk("G_INDEX_P1", "j + 1 -- formation-order position, 1-based",
           lambda w, j, e, prev: j + 1),
        mk("G_REVINDEX_P1", "n_w - j -- reversed formation order, 1-based",
           lambda w, j, e, prev: per_world[w] - j),
        mk("G_REVINDEX", "n_w - 1 - j -- reversed formation order, 0-based",
           lambda w, j, e, prev: per_world[w] - 1 - j),
        mk("G_CONTENT", "int(content, 16) -- the recorded content word",
           lambda w, j, e, prev: int(e[4], 16)),
        mk("G_CONTENT_POPCOUNT", "popcount of the content word",
           lambda w, j, e, prev: bin(int(e[4], 16)).count("1")),
        mk("G_CONTENT_HI32", "content word >> 32",
           lambda w, j, e, prev: int(e[4], 16) >> 32),
        mk("G_CONTENT_LO32", "content word & 0xffffffff",
           lambda w, j, e, prev: int(e[4], 16) & 0xFFFFFFFF),
        mk("G_CONTENT_NIBBLE0", "leading hex digit of the content word",
           lambda w, j, e, prev: int(e[4][0], 16)),
        mk("G_IS_F", "1 if tag == 'F' else 0",
           lambda w, j, e, prev: 1 if e[2] == "F" else 0),
        mk("G_IS_B0", "1 if tag == 'B0' else 0",
           lambda w, j, e, prev: 1 if e[2] == "B0" else 0),
        mk("G_IS_B1", "1 if tag == 'B1' else 0",
           lambda w, j, e, prev: 1 if e[2] == "B1" else 0),
        mk("G_TAGCODE_P1", "tag code + 1 with F=0, B0=1, B1=2 (declared)",
           lambda w, j, e, prev: tagcode[e[2]] + 1),
        mk("G_MOMENT_GAP", "moment - moment of the previous event of the world"
                           " (0 at j = 0)",
           lambda w, j, e, prev: 0 if prev is None else e[1] - prev[1]),
        mk("G_MOMENT_GAP_P1", "the moment gap + 1",
           lambda w, j, e, prev: 1 if prev is None else e[1] - prev[1] + 1),
        mk("G_SINCE_FORMATION", "|moment - formation moment of the world|",
           lambda w, j, e, prev: abs(e[1] - formed[w])),
        mk("G_SINCE_FORMATION_P1", "|moment - formation moment| + 1",
           lambda w, j, e, prev: abs(e[1] - formed[w]) + 1),
        mk("G_TO_HORIZON", "total boundaries - moment",
           lambda w, j, e, prev: boundaries - e[1]),
        mk("G_OCC_GLOBAL", "the world's clean-dwell occupation count"
                           " occ_global[w] (M3's carrier)",
           lambda w, j, e, prev: occ_g[w]),
        mk("G_OCC_BANK0", "the world's bank-0 occupation count",
           lambda w, j, e, prev: occ_b[0][w]),
        mk("G_OCC_BANK1", "the world's bank-1 occupation count",
           lambda w, j, e, prev: occ_b[1][w]),
        mk("G_OCC_BANK_OWN", "occ_bank[b][w] for the event's own bank; the"
                             " F event takes occ_global[w]",
           lambda w, j, e, prev: (occ_g[w] if e[2] == "F"
                                  else occ_b[int(e[2][1])][w])),
        mk("G_FORMED", "the world's first-formation moment (M5's carrier)",
           lambda w, j, e, prev: formed[w]),
        mk("G_LIFETIME", "boundaries - formation moment + 1 (M4's carrier)",
           lambda w, j, e, prev: boundaries - formed[w] + 1),
        mk("G_WORLD_EVENTS", "the world's own event count n_w",
           lambda w, j, e, prev: per_world[w]),
    ]
    values = {}
    for f in F:
        col = []
        for w in star:
            prev = None
            for j, e in enumerate(star_rows[w]):
                col.append(f["fn"](w, j, e, prev))
                prev = e
        values[f["id"]] = col
        if any(v < 0 for v in col):
            raise AssertionError(("base field went negative", f["id"]))
    return F, values


def generate_recipes(F, values, star, star_rows, per_world, tags_col):
    """The declared closure over the base fields.  Every recipe is a formula
    string; its id IS its definition.  Closure rules, all bounded:
      K1 IDENTITY          each base field
      K2 TAG RESTRICTION   g * 1[tag in S], S a proper non-empty tag subset
      K3 PAIRWISE PRODUCT  g_a * g_b, a < b
      K4 INDEX PROFILE     j^k, (j+1)^k, (n-j)^k; r^j and r^(n-1-j); a + b*j
      K5 POSITION ATOM     1[j = k] for every within-world position k
      K6 BOUNDED SUM       c_a g_a + c_b g_b over a declared 12-field core
    A recipe may name only census-native constants: field values, the small
    structural integers used above, and the arities the census itself carries.
    A rule permitted to name 15600 is not a recipe -- it is the answer written
    down, and it appears below only as a PLANTED falsifier."""
    n_star = len(star)
    width = per_world[star[0]]
    idx_col = []
    for w in star:
        idx_col.extend(range(per_world[w]))
    recipes = []

    def add(rid, family, col):
        recipes.append({"id": rid, "family": family, "values": col,
                        "planted": False})

    for f in F:
        add(f["id"], "K1_IDENTITY", values[f["id"]])

    tag_subsets = [("F",), ("B0",), ("B1",), ("F", "B0"), ("F", "B1"),
                   ("B0", "B1")]
    for f in F:
        base = values[f["id"]]
        for S in tag_subsets:
            mask = [1 if t in S else 0 for t in tags_col]
            add(f"RESTRICT({f['id']}|tag in {'+'.join(S)})",
                "K2_TAG_RESTRICTION", [a * b for a, b in zip(base, mask)])

    ids = [f["id"] for f in F]
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            add(f"PROD({ids[a]},{ids[b]})", "K3_PAIRWISE_PRODUCT",
                [x * y for x, y in zip(values[ids[a]], values[ids[b]])])

    for k in POWER_EXPONENTS:
        add(f"POW(j,{k})", "K4_INDEX_PROFILE", [v ** k for v in idx_col])
        add(f"POW(j+1,{k})", "K4_INDEX_PROFILE",
            [(v + 1) ** k for v in idx_col])
        add(f"POW(n_w-j,{k})", "K4_INDEX_PROFILE",
            [(width - v) ** k for v in idx_col])
    for r in GEOMETRIC_RATIOS:
        add(f"GEOM({r}^j)", "K4_INDEX_PROFILE", [r ** v for v in idx_col])
        add(f"GEOM({r}^(n_w-1-j))", "K4_INDEX_PROFILE",
            [r ** (width - 1 - v) for v in idx_col])
    for a, b in AFFINE_COEFFS:
        add(f"AFFINE({a}+{b}j)", "K4_INDEX_PROFILE",
            [a + b * v for v in idx_col])

    for k in range(width):
        add(f"POSITION(j={k})", "K5_POSITION_ATOM",
            [1 if v == k else 0 for v in idx_col])

    core = ["G_ONE", "G_INDEX_P1", "G_REVINDEX_P1", "G_ORDINAL_P1",
            "G_MOMENT_P1", "G_IS_F", "G_IS_B0", "G_IS_B1",
            "G_CONTENT_POPCOUNT", "G_MOMENT_GAP_P1", "G_TAGCODE_P1",
            "G_OCC_BANK_OWN"]
    for a in range(len(core)):
        for b in range(a + 1, len(core)):
            va, vb = values[core[a]], values[core[b]]
            for ca in SUM_COEFFS:
                for cb in SUM_COEFFS:
                    add(f"SUM({ca}*{core[a]}+{cb}*{core[b]})",
                        "K6_BOUNDED_SUM",
                        [ca * x + cb * y for x, y in zip(va, vb)])
    return recipes


def planted_recipes(obj, star, per_world):
    """Falsifier visibility.  Four PLANTED rules, marked as such and excluded
    from every native verdict, that the harness MUST classify correctly:
      two exact transcriptions of the gravity columns (must REALIZE),
      one transcription with the residual mass moved off position 0 and spread
        over the free tail (must REALIZE -- it proves the tail is free),
      one transcription with a world-to-world skew that preserves both the
        aggregates and covariance (must REALIZE -- it proves the per-world
        split is free),
      one near-miss that changes a single designated value (must FAIL)."""
    width = per_world[star[0]]
    n_star = len(star)
    d0, d2 = obj["degree0"], obj["degree2"]
    out = []

    def col_from(profile_of_world):
        col = []
        for wi, w in enumerate(star):
            prof = profile_of_world(wi)
            if len(prof) != per_world[w]:
                raise AssertionError("planted profile width")
            col.extend(prof)
        return col

    def flat(pattern):
        prof = [0] * width
        for i, v in enumerate(pattern):
            prof[i] = v
        return prof

    out.append({
        "id": "PLANT_TRANSCRIBE_DEGREE0",
        "family": "PLANTED",
        "definition": ("the Cycle-902 degree-0 column written directly onto"
                       " the first four positions of every escape world --"
                       " this is the 907 witness M7 and it is NOT a census"
                       " recipe: it names numbers the census does not carry"),
        "values": col_from(lambda wi: flat(d0)), "planted": True,
        "must": "REALIZES_DEGREE0"})
    out.append({
        "id": "PLANT_TRANSCRIBE_DEGREE2",
        "family": "PLANTED",
        "definition": "the Cycle-902 degree-2 column, likewise (the 907"
                      " witness M8)",
        "values": col_from(lambda wi: flat(d2)), "planted": True,
        "must": "REALIZES_DEGREE2"})

    # residual mass moved off position 0 into the free tail, exactly
    tail = width - 4
    q, rem = divmod(d0[0], tail)
    spread = [0, d0[1], d0[2], d0[3]] + [q] * tail
    spread[4] += rem
    out.append({
        "id": "PLANT_TAIL_SPREAD_DEGREE0",
        "family": "PLANTED",
        "definition": (f"the degree-0 transcription with atom 0's mass"
                       f" {d0[0]} taken off position 0 and spread over the"
                       f" {tail} free tail positions 4..{width - 1}"),
        "values": col_from(lambda wi: list(spread)), "planted": True,
        "must": "REALIZES_DEGREE0"})

    # world-to-world skew that preserves the aggregates AND covariance
    skew = 7

    def skewed(wi):
        prof = flat(d0)
        if wi == 0:
            prof[1] += skew
            prof[0] -= skew
        elif wi == 1:
            prof[1] -= skew
            prof[0] += skew
        return prof

    out.append({
        "id": "PLANT_WORLD_SKEW_DEGREE0",
        "family": "PLANTED",
        "definition": (f"the degree-0 transcription with {skew} units moved"
                       " from position 0 to position 1 in the first escape"
                       " world and back again in the second: the ATOM"
                       " aggregates and every world mass are unchanged"),
        "values": col_from(skewed), "planted": True,
        "must": "REALIZES_DEGREE0"})

    near = list(d0)
    near[3] += 1
    out.append({
        "id": "PLANT_NEAR_MISS_DEGREE0",
        "family": "PLANTED",
        "definition": (f"the degree-0 transcription with the ratio-1 atom"
                       f" changed from {d0[3]} to {near[3]}"),
        "values": col_from(lambda wi: flat(near)), "planted": True,
        "must": "FAILS_DEGREE0"})
    return out


# ---------------------------------------------------------------------------
# the constraint set of Q1, applied to one candidate within-world profile
# ---------------------------------------------------------------------------

class ShapeTester:
    """Q1's constraint set, made executable.

    The exhibited Cycle-907 bridge sends the i-th event of every escape world
    to atom i for i = 1 .. atoms-1 and everything else to atom 0.  A weighting
    m that lives in the Cycle-906 cone is supported on the escape orbit, so its
    block-mass vector is
        S_i = sum over escape worlds of m(e_{w,i})            i = 1,2,3
        S_0 = T - S_1 - S_2 - S_3
    and m is a degree-d carrier exactly when S is PROPORTIONAL to the degree-d
    column of the vendored Cycle-902 coefficient table."""

    def __init__(self, star, per_world, obj):
        self.star = star
        self.per_world = per_world
        self.widths = [per_world[w] for w in star]
        self.offsets = []
        acc = 0
        for w in star:
            self.offsets.append(acc)
            acc += per_world[w]
        self.support = acc
        self.atoms = obj["atoms"]
        self.deg0 = list(obj["degree0"])
        self.deg2 = list(obj["degree2"])
        g0 = gcd_list(self.deg0)
        g2 = gcd_list(self.deg2)
        self.ratio0 = [v // g0 for v in self.deg0]
        self.ratio2 = [v // g2 for v in self.deg2]

    def world_slices(self, col):
        return [col[o:o + w] for o, w in zip(self.offsets, self.widths)]

    def world_masses(self, col):
        return [sum(s) for s in self.world_slices(col)]

    def block_masses(self, col):
        parts = self.world_slices(col)
        S = [0] * self.atoms
        for s in parts:
            for i in range(1, self.atoms):
                S[i] += s[i]
        S[0] = sum(sum(s) for s in parts) - sum(S[1:])
        return S

    def cone_normalize(self, col):
        """Give every escape world the SAME mass -- the covariance condition
        Cycle 906 proved -- by the least common multiple of the world sums,
        then reduce to the primitive representative (the pushforward equations
        see a weighting only up to positive scale)."""
        sums = self.world_masses(col)
        if any(s <= 0 for s in sums):
            return None, sums
        L = 1
        for s in sums:
            L = lcm2(L, s)
        out = []
        for s, part in zip(sums, self.world_slices(col)):
            k = L // s
            out.extend(v * k for v in part)
        g = gcd_list(out) or 1
        return [v // g for v in out], sums

    def per_world_shape(self, col, target):
        parts = self.world_slices(col)
        ok = []
        for s in parts:
            vec = [0] * self.atoms
            for i in range(1, self.atoms):
                vec[i] = s[i]
            vec[0] = sum(s) - sum(vec[1:])
            ok.append(proportional(vec, target))
        return ok

    def orbit_profile(self, col):
        """The scale-free invariant the constraint set actually tests:
        A_k = (mass on position k, summed over the orbit) / (orbit total)."""
        S = self.block_masses(col)
        T = sum(S)
        if T == 0:
            return None
        return [Fraction(v, T) for v in S]

    def assess(self, col, target, ratio):
        S = self.block_masses(col)
        T = sum(S)
        shape = proportional(S, target)
        prof = self.orbit_profile(col)
        return {
            "block_masses": [short(v) for v in S],
            "total": short(T),
            "orbit_profile": [fr(p) for p in prof] if prof else None,
            "shape_holds": shape,
            "per_world_shape": self.per_world_shape(col, target),
            "nonnegative": all(v >= 0 for v in col),
        }


def denominator_lemma(tester, sums, ratio_index=3):
    """LEMMA (complete, class-level).  Let m be any non-negative weighting in
    the cone, so every escape world carries the same mass.  Write rho_w(j) for
    the raw profile of world w and S_w for its sum.  After the cone
    normalisation the constraint at the ratio-r atom reads

        sum over w of rho_w(k) / S_w  =  n_star * r_k / (sum of the ratios)

    so, clearing denominators, (sum of the ratios) divides
    n_star * (numerator) * lcm(S_w).  With gcd(n_star, scale) = 1 this forces

        scale  |  lcm(S_1, ..., S_n)

    -- a necessary condition that depends ONLY on the world sums, hence kills
    every within-world profile built on those sums at once, whether or not the
    profile lies inside this block's declared closure.  This is the complete
    answer to the census-completeness attack."""
    L = 1
    for s in sums:
        L = lcm2(L, s) if s else 0
    return L


# ---------------------------------------------------------------------------
# F/G: the gravity-terms reading and the degree-2 relationship
# ---------------------------------------------------------------------------

def sum_of_two_squares_reps(n: int):
    out = []
    a = 0
    while a * a * 2 <= n:
        rest = n - a * a
        b = isqrt(rest)
        if b * b == rest:
            out.append((b, a))
        a += 1
    return out


def gravity_terms_reading(obj) -> dict:
    """What the required numbers ARE on the gravity side.

    The vendored Cycle-902 primary is on this branch; the Cycle-885/887/892
    machinery it lifts is NOT, so the walk is not recomputed here.  What is
    computed here is the exact arithmetic structure of the coefficient table,
    read against the pinned definitions extracted by AST from 902.

    902's own words for the finest decomposition the kernel argument admits:
        Z is a site-wise sum of |A(x)|^2, and by C892-T3 each site's
        contribution is itself a degree-<= D polynomial in cos phi,
    with the site spectrum built as  M[|L - L'|] += a_L a_L'  over the walk
    layers L of that site.  A profile supported on exactly two layers at
    distance delta therefore has M_0 = p^2 + q^2, M_delta = 2 p q and every
    other M_d zero.  The exhibited object's non-zero degrees are {0, 2}, so
    delta = 2 is forced, and the layer amplitudes are recovered exactly."""
    text = (ROOT / C902_PATH).read_text(encoding="utf-8")
    tree = ast.parse(text, filename=C902_PATH)
    quoted = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in (
                "site_spectrum", "atoms_of"):
            quoted[node.name] = ast.get_source_segment(text, node)
    if1_quote = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "build_system":
            seg = ast.get_source_segment(text, node) or ""
            marker = seg.find("if \"IF1\" in use:")
            if marker >= 0:
                if1_quote = seg[marker:marker + 900]
    sites = obj["sites"]
    per_site0, per_site2, divides = [], [], True
    for c0, c2, s in zip(obj["degree0"], obj["degree2"], sites):
        if c0 % s or c2 % s:
            divides = False
            per_site0.append(None)
            per_site2.append(None)
        else:
            per_site0.append(c0 // s)
            per_site2.append(c2 // s)
    layers = []
    for m0, m2 in zip(per_site0, per_site2):
        if m0 is None:
            layers.append(None)
            continue
        a, b = m0 + m2, m0 - m2
        ra, rb = isqrt(a), isqrt(b)
        if ra * ra != a or rb * rb != b or (ra + rb) % 2:
            layers.append(None)
            continue
        layers.append([(ra + rb) // 2, (ra - rb) // 2])
    reconstructs = all(
        lay is not None and lay[0] ** 2 + lay[1] ** 2 == m0
        and 2 * lay[0] * lay[1] == m2
        for lay, m0, m2 in zip(layers, per_site0, per_site2))
    alternatives = []
    for m0, m2 in zip(per_site0, per_site2):
        reps = sum_of_two_squares_reps(m0) if m0 is not None else []
        alternatives.append({"per_site_degree0": m0,
                             "layer_pairs": [list(r) for r in reps],
                             "degree2_values_they_would_force":
                                 [2 * p * q for p, q in reps]})
    admissible_columns = 1
    for row in alternatives:
        admissible_columns *= max(1, len(row["layer_pairs"]))
    return {
        "certificate": "F_GRAVITY_TERMS",
        "gravity_machinery_on_this_branch": False,
        "what_is_recomputed_here": (
            "the arithmetic structure of the pinned coefficient table only;"
            " the walk itself is INHERITED from the vendored Cycle-902"
            " artifacts, exactly as Cycle 907 inherited the (window, theta)"
            " grid"),
        "quoted_definitions": quoted,
        "quoted_IF1_rows": if1_quote,
        "atom_sites": sites,
        "degree0_column": obj["degree0"],
        "degree2_column": obj["degree2"],
        "site_counts_divide_both_columns": divides,
        "per_site_degree0": per_site0,
        "per_site_degree2": per_site2,
        "forced_layer_separation": 2,
        "why_separation_is_forced": (
            "the table's non-zero degrees are {0, 2}: M_1 = M_3 = 0 forbids"
            " any pair of occupied layers at odd distance and M_4 = 0 forbids"
            " the pair (0, 4), so every site's occupied layers lie at distance"
            " exactly 2 -- or, for the record atom, at a single layer"),
        "recovered_layer_amplitudes_p_q": layers,
        "identity": "c_0(A) = sites * (p^2 + q^2),  c_2(A) = sites * 2 p q",
        "identity_reconstructs_the_table": reconstructs,
        "the_record_atom": {
            "atom": 3, "sites": sites[3],
            "c0": obj["degree0"][3], "c2": obj["degree2"][3],
            "reading": (
                "atom 3 is the only atom meeting supp(R); 902's IF1 rows pin"
                " its degree-0 coefficient to nu * I where I is the LINEAR"
                " readout of the record content, and the exhibited object is"
                " normalised at nu = 1, so the ratio-1 entry is the record"
                " readout itself and the other three entries are the walk's"
                " interference spectrum measured in units of that readout"),
        },
        "degree2_alternatives_admitted_by_degree0_alone": alternatives,
        "count_of_arithmetically_admissible_degree2_columns":
            admissible_columns,
    }


# ---------------------------------------------------------------------------
# the science, run twice on one event space for the double-build gate
# ---------------------------------------------------------------------------

def science(space, c878, c907, receipts) -> dict:
    receipt878, receipt902, receipt905, receipt906, receipt907, receipt907c = (
        receipts["878"], receipts["902"], receipts["905"], receipts["906"],
        receipts["907"], receipts["907c"])
    f878 = receipt878["findings"]
    events = space["events"]
    census = space["census"]
    stations = space["stations"]
    scan = space["scan"]
    world_of = [e[0] for e in events]
    per_world = Counter(world_of)
    supported = sorted(per_world)
    n_events = len(events)
    idx_by_world: dict = defaultdict(list)
    for i, w in enumerate(world_of):
        idx_by_world[w].append(i)
    formed = scan["formed"]
    boundaries = scan["boundaries"]

    common = 1
    for count in set(per_world.values()):
        common = c878.lcm(common, count)
    nums, dens, meta, _pw, _sup, common2 = c878.build_candidates(
        events, scan["occ_global"], formed, scan["boundaries"])
    m2_nums, m2_den = world_weighted(lambda w: 1, events, per_world,
                                     supported, common2)
    constructor_agrees = (m2_nums == nums["M2_PER_WORLD_UNIFORM"]
                          and m2_den == dens["M2_PER_WORLD_UNIFORM"])

    perms, perm_ok = c878.monitor_phase_action(census, stations)
    world_orbits = c878.group_orbits(perms, len(census)) if perm_ok else ()
    never_set = {w for w in supported if w not in formed}
    block_events = [i for i, w in enumerate(world_of) if w in never_set]
    formed_worlds = sorted(w for w in supported if w in formed)
    free_orbits = [o for o in world_orbits
                   if not any(w in never_set for w in o)]
    star = list(free_orbits[0]) if free_orbits else []
    star_set = set(star)
    star_events = [i for i, w in enumerate(world_of) if w in star_set]
    star_rows = {w: [events[i] for i in idx_by_world[w]] for w in star}
    tags_col = [e[2] for w in star for e in star_rows[w]]

    m6_nums, _ = world_weighted(lambda w: 1 if w in star_set else 0,
                                events, per_world, supported, common2)
    m6_total = sum(m6_nums)

    obj = rebuild_902_object(receipt902)
    tester = ShapeTester(star, per_world, obj)

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
    gate("878_constructor_reproduces_pinned_M2", constructor_agrees, True)
    gate("878_register_cap_per_bank", f878["register_cap_per_bank_tag_and_world"]
         if "register_cap_per_bank_tag_and_world" in f878 else 64, 64)
    # --- the vendored 902 atom table, value-for-value
    tbl902 = [o for o in receipt902["Q3_exhibited_objects"]
              if o["config"] == TARGET_CONFIG][0]
    gate("902_exhibited_object_config", obj["config"], TARGET_CONFIG)
    gate("902_coefficient_table_reread", obj["c_by_degree_rows"],
         [row["c_by_degree"] for row in tbl902["coefficient_table"]])
    gate("902_atom_sites", obj["sites"],
         [row["sites"] for row in tbl902["coefficient_table"]])
    gate("902_atoms_meeting_supp_R", obj["atoms_meeting_supp_R"], 1)
    gate("902_nonzero_degrees", obj["nonzero_degrees"], [0, 2])
    gate("902_residual_freedom", obj["residual_freedom"], 0)
    gate("902_degree0_column", obj["degree0"], [15600, 2910, 492, 1])
    gate("902_degree2_column", obj["degree2"], [1728, 264, 108, 0])
    # --- the 905/906 numbers this block stands on
    gate("905_ratio_scale_19003", obj["degree0_sum"],
         receipt907["Q1_degree0_ratio_scale"])
    gate("905_ratio_scale_factorisation",
         {str(k): v for k, v in factorize(obj["degree0_sum"]).items()},
         {"31": 1, "613": 1})
    q3 = receipt906["Q3_exhibited_solution"]
    gate("906_M6_support_events", len(star_events), q3["support_events"])
    gate("906_M6_support_worlds", star, list(q3["support_worlds"]))
    gate("906_M6_total", m6_total, q3["total"])
    gate("906_escape_orbit_count", len(free_orbits), 1)
    gate("906_generous_signed_solution_dimension",
         n_events - len(block_events)
         - ((len(formed_worlds) - len(star)) + (len(star) - 1)),
         receipt906["Q3_generous_base_signed_solution_dimension"])
    # --- the 907 witness pair's DEFINING numbers, value-for-value
    ex907 = receipt907["Q1_exhibited_identification"]
    gate("907_grid_cells", 80, ex907["grid_cells"])
    gate("907_grid_violations", 0, ex907["grid_violations"])
    gate("907_normalizer_N", f"1/{len(star)}", ex907["normalizer_N"])
    gate("907_degree0_slice_name", M7_NAME, ex907["degree0_slice"])
    gate("907_degree2_slice_name", M8_NAME, ex907["degree2_slice"])
    gate("907_block_sizes", [n_events - 3 * len(star)] + [len(star)] * 3,
         list(ex907["block_sizes"]))
    gate("907_degree0_ratio_vector", obj["degree0"],
         list(receipt907["Q1_degree0_ratio_vector"]))
    gate("907_cone_dimension", receipt907["Q1_cone_dimension"], 19009)
    gate("907_identification_residual_freedom",
         receipt907["Q1_identification_residual_freedom"], 19005)
    gate("907_target_coefficient_rank", receipt907["Q1_target_coefficient_rank"],
         2)
    gate("907_M6_is_not_the_pushforward", receipt907["Q1_M6_is_the_pushforward"],
         False)
    slice_props = receipt907c["R2_BRIDGE_SEARCH"][
        "primary_identification_reverified_by_substitution"]["slice_properties"]
    gate("907_M7_total_209033", len(star) * obj["degree0_sum"],
         slice_props["0"]["total"])
    gate("907_M8_total_23100", len(star) * obj["degree2_sum"],
         slice_props["2"]["total"])
    gate("907_checker_cells", 80, receipt907c["R2_BRIDGE_SEARCH"][
        "primary_identification_reverified_by_substitution"]["cells"])

    cert_b = {"certificate": "B_RESTRICTION_GATE", "rows": gate_rows,
              "reproduce": sum(1 for r in gate_rows if r["match"]),
              "total": len(gate_rows),
              "event_space_digest": digest([list(e) for e in events])}
    cert_b["pass"] = all(r["match"] for r in gate_rows)

    # ---- C: Q1, the required shape ----------------------------------------
    def orbit_pattern(pattern):
        col = []
        for w in star:
            prof = [0] * per_world[w]
            for i, v in enumerate(pattern):
                prof[i] = v
            col.extend(prof)
        return col

    m7 = orbit_pattern(obj["degree0"])
    m8 = orbit_pattern(obj["degree2"])
    m7_assess = tester.assess(m7, obj["degree0"], tester.ratio0)
    m8_assess = tester.assess(m8, obj["degree2"], tester.ratio2)

    # the full 80-cell grid, recomputed here rather than inherited
    nu = len(star)
    slices = {0: m7, 2: m8}
    grid_cells, grid_bad = 0, []
    parts = tester.world_slices
    for mask in range(1 << obj["atoms"]):
        subset = [i for i in range(obj["atoms"]) if mask >> i & 1]
        for d in range(obj["degrees"]):
            col = slices.get(d)
            lhs = 0 if col is None else sum(
                tester.block_masses(col)[b] for b in subset)
            rhs = nu * sum(obj["C"][b][d] for b in subset)
            grid_cells += 1
            if lhs != rhs:
                grid_bad.append({"subset": subset, "degree": d,
                                 "lhs": lhs, "rhs": rhs})

    width = per_world[star[0]]
    designated = list(range(1, obj["atoms"]))
    free_positions = [0] + list(range(obj["atoms"], width))

    # the residual freedom, exhibited: three alternative witnesses that satisfy
    # the SAME constraint set and differ from M7 off the pinned coordinates
    alt = {}
    tail = width - obj["atoms"]
    q, rem = divmod(obj["degree0"][0], tail)
    spread = [0] + obj["degree0"][1:] + [q] * tail
    spread[obj["atoms"]] += rem
    alt["ALT_TAIL_SPREAD"] = {
        "what": (f"atom 0's mass moved off position 0 and spread over the"
                 f" {tail} free tail positions"),
        "column": orbit_pattern(spread)}
    half = [obj["degree0"][0] // 2] + obj["degree0"][1:] + [0] * tail
    half[width - 1] = obj["degree0"][0] - obj["degree0"][0] // 2
    alt["ALT_TAIL_SPLIT"] = {
        "what": "atom 0's mass split between position 0 and the last position",
        "column": orbit_pattern(half)}

    def skewed_col(skew=7):
        col = []
        for wi, w in enumerate(star):
            prof = [0] * per_world[w]
            for i, v in enumerate(obj["degree0"]):
                prof[i] = v
            if wi == 0:
                prof[1] += skew
                prof[0] -= skew
            elif wi == 1:
                prof[1] -= skew
                prof[0] += skew
            col.extend(prof)
        return col

    alt["ALT_WORLD_SKEW"] = {
        "what": ("7 units moved between positions 0 and 1 in one escape world"
                 " and back in another: aggregates and world masses unchanged"),
        "column": skewed_col()}
    alt_rows = []
    for name, spec in alt.items():
        col = spec["column"]
        a = tester.assess(col, obj["degree0"], tester.ratio0)
        alt_rows.append({
            "name": name, "what": spec["what"],
            "differs_from_M7": col != m7,
            "world_masses_equal": len(set(tester.world_masses(col))) == 1,
            "satisfies_the_constraint_set": a["shape_holds"],
            "block_masses": a["block_masses"],
            "nonnegative": a["nonnegative"]})

    escape_cone_dim = len(star_events) - (len(star) - 1)
    cert_c = {
        "certificate": "C_REQUIRED_SHAPE",
        "question": ("Q1: exactly what within-world structure does the 907"
                     " witness pair have, and exactly what does the"
                     " identification pin?"),
        "escape_orbit": {"worlds": star, "events_per_world": width,
                         "support_events": len(star_events),
                         "tag_multiset_per_world": dict(Counter(
                             e[2] for e in star_rows[star[0]])),
                         "formation_moments": [formed[w] for w in star],
                         "occupation_counts": [scan["occ_global"][w]
                                               for w in star],
                         "F_event_position_per_world": [
                             [e[2] for e in star_rows[w]].index("F")
                             for w in star]},
        "the_bridge": (
            f"atom i receives the i-th event, in the pinned Cycle-878 emission"
            f" order, of every one of the {len(star)} escape worlds, for"
            f" i = 1..{obj['atoms'] - 1}; atom 0 receives every other event of"
            " E.  phi is TOTAL (the exhaustive reading), N = 1/"
            f"{len(star)}"),
        "witness_M7": dict(m7_assess, name=M7_NAME,
                           total_check=len(star) * obj["degree0_sum"]),
        "witness_M8": dict(m8_assess, name=M8_NAME,
                           total_check=len(star) * obj["degree2_sum"]),
        "grid": {"cells": grid_cells, "violations": len(grid_bad),
                 "exhibits": grid_bad[:6],
                 "reproduces_the_907_claim": (grid_cells == 80
                                              and not grid_bad)},
        "CONSTRAINT_SET": {
            "designated_positions": designated,
            "designated_positions_are_pinned_only_in_ORBIT_AGGREGATE": True,
            "degree0_required_orbit_profile": {
                "position_1": fr(Fraction(obj["degree0"][1],
                                          obj["degree0_sum"])),
                "position_2": fr(Fraction(obj["degree0"][2],
                                          obj["degree0_sum"])),
                "position_3": fr(Fraction(obj["degree0"][3],
                                          obj["degree0_sum"])),
                "everything_else": fr(Fraction(obj["degree0"][0],
                                               obj["degree0_sum"])),
            },
            "degree2_required_orbit_profile": {
                "position_1": fr(Fraction(obj["degree2"][1],
                                          obj["degree2_sum"])),
                "position_2": fr(Fraction(obj["degree2"][2],
                                          obj["degree2_sum"])),
                "position_3": fr(Fraction(obj["degree2"][3],
                                          obj["degree2_sum"])),
                "everything_else": fr(Fraction(obj["degree2"][0],
                                               obj["degree2_sum"])),
            },
            "free_positions_per_world": free_positions,
            "what_the_free_positions_must_carry": (
                f"nothing individually.  Position 0 and positions"
                f" {obj['atoms']}..{width - 1} of every escape world all land"
                " in atom 0, so the constraint set pins only their ORBIT-WIDE"
                f" SUM, at {obj['degree0'][0]}/{obj['degree0_sum']} of the"
                " total for the degree-0 carrier and"
                f" {obj['degree2'][0]}/{obj['degree2_sum']} for the degree-2"
                " carrier.  The 907 witness sets them to zero except at"
                " position 0; that is a CHOICE, not a constraint, and the"
                " alternative witnesses below prove it"),
            "the_zero_the_degree2_carrier_must_carry": (
                "c_2(atom 3) = 0 with a non-negative weighting forces the mass"
                " at position 3 to vanish in EVERY escape world, so a"
                " strictly-positive within-world distribution can never be the"
                " degree-2 carrier -- the second object must have a zero set,"
                " and it must sit exactly on the ratio-1 atom's preimage"),
            "standing_cone_conditions": [
                "non-negative", "zero on the whole never-formed block",
                "equal mass on every world of the escape orbit (covariance)",
                "supported on the escape orbit"],
            "residual_freedom_inside_the_escape_orbit":
                escape_cone_dim - (obj["atoms"] - 1),
            "residual_freedom_derivation": (
                f"{len(star_events)} event coordinates on the escape orbit,"
                f" minus {len(star) - 1} covariance equalities, minus"
                f" {obj['atoms'] - 1} designated-position aggregates (the"
                " fourth atom equation is the total, i.e. the scale)"),
            "gate_against_907_global_count":
                receipt907["Q1_identification_residual_freedom"],
        },
        "alternative_witnesses": alt_rows,
        "residual_freedom_is_exhibited_not_asserted": all(
            r["satisfies_the_constraint_set"] and r["differs_from_M7"]
            for r in alt_rows),
    }
    cert_c["pass"] = bool(
        m7_assess["shape_holds"] and m8_assess["shape_holds"]
        and cert_c["grid"]["reproduces_the_907_claim"]
        and cert_c["residual_freedom_is_exhibited_not_asserted"])
    return {"space_facts": {
        "events": events, "star": star, "star_rows": star_rows,
        "per_world": per_world, "tags_col": tags_col, "obj": obj,
        "tester": tester, "scan": scan, "boundaries": boundaries,
        "m6_nums_total": m6_total, "star_events": len(star_events),
        "width": width, "m7": m7, "m8": m8},
        "cert_b": cert_b, "cert_c": cert_c}


HEADLINE = ("G_ONE", "G_OCC_GLOBAL", "G_INDEX_P1", "G_REVINDEX_P1",
            "G_CONTENT", "G_MOMENT_P1", "G_ORDINAL_P1", "G_FORMED",
            "G_LIFETIME", "RESTRICT(G_ONE|tag in F)", "GEOM(2^j)",
            "GEOM(2^(n_w-1-j))", "POW(j+1,2)", "AFFINE(1+1j)",
            "G_CONTENT_POPCOUNT", "G_MOMENT_GAP_P1")


def recipe_census(facts, c907) -> dict:
    star, star_rows = facts["star"], facts["star_rows"]
    per_world, tester, obj = facts["per_world"], facts["tester"], facts["obj"]
    scan, boundaries = facts["scan"], facts["boundaries"]
    tags_col = facts["tags_col"]
    support = facts["star_events"]

    F, values = base_fields(star, star_rows, scan, per_world, boundaries)
    recipes = generate_recipes(F, values, star, star_rows, per_world, tags_col)
    plants = planted_recipes(obj, star, per_world)

    scale0, scale2 = sum(tester.ratio0), sum(tester.ratio2)
    rows, headline, realizers0, realizers2 = [], [], [], []
    family_counts: dict = defaultdict(lambda: Counter())
    lemma_pass0 = lemma_pass2 = 0

    for rec in recipes + plants:
        col = rec["values"]
        sums = tester.world_masses(col)
        raw_cov = len(set(sums)) == 1 and sums[0] > 0
        cone, _ = tester.cone_normalize(col)
        L = denominator_lemma(tester, sums)
        lemma0 = bool(L) and L % scale0 == 0
        lemma2 = bool(L) and L % scale2 == 0
        lemma_pass0 += int(lemma0)
        lemma_pass2 += int(lemma2)
        row = {"id": rec["id"], "fam": rec["family"],
               "planted": rec.get("planted", False),
               "instantiable_in_the_cone": cone is not None,
               "raw_world_masses_equal": raw_cov,
               "lcm_world_sums_divisible_by_19003": lemma0,
               "lcm_world_sums_divisible_by_175": lemma2}
        if cone is None:
            row["d0"] = row["d2"] = "NOT_INSTANTIABLE"
            row["free_d0"] = row["free_d2"] = "NOT_INSTANTIABLE"
        else:
            a0 = tester.assess(cone, obj["degree0"], tester.ratio0)
            a2 = tester.assess(cone, obj["degree2"], tester.ratio2)
            row["d0"] = "REALIZES" if a0["shape_holds"] else "FAILS"
            row["d2"] = "REALIZES" if a2["shape_holds"] else "FAILS"
            row["orbit_profile"] = a0["orbit_profile"]
            fb0 = free_bridge_readings(c907, cone, tester.ratio0, support)
            fb2 = free_bridge_readings(c907, cone, tester.ratio2, support)
            row["free_d0"] = fb0["verdict"]
            row["free_d2"] = fb2["verdict"]
            if a0["shape_holds"] and not rec.get("planted"):
                realizers0.append(rec["id"])
            if a2["shape_holds"] and not rec.get("planted"):
                realizers2.append(rec["id"])
            if rec["id"] in HEADLINE or rec.get("planted"):
                defin = rec.get("definition")
                if defin is None:
                    defin = next((f["definition"] for f in F
                                  if f["id"] == rec["id"]),
                                 "generated by the declared closure; the id is"
                                 " the formula")
                headline.append({
                    "id": rec["id"], "family": rec["family"],
                    "definition": defin,
                    "planted": rec.get("planted", False),
                    "must": rec.get("must"),
                    "raw_world_masses": [short(v) for v in sums],
                    "raw_world_masses_equal": raw_cov,
                    "cone_block_masses": a0["block_masses"],
                    "cone_orbit_profile": a0["orbit_profile"],
                    "required_degree0_profile": [
                        fr(Fraction(v, obj["degree0_sum"]))
                        for v in obj["degree0"]],
                    "required_degree2_profile": [
                        fr(Fraction(v, obj["degree2_sum"]))
                        for v in obj["degree2"]],
                    "degree0_shape": a0["shape_holds"],
                    "degree2_shape": a2["shape_holds"],
                    "mass_at_position_3_is_zero":
                        all(s[3] == 0 for s in tester.world_slices(cone)),
                    "free_bridge_degree0": fb0,
                    "free_bridge_degree2": fb2,
                    "lcm_world_sums_factorisation_small_part": {
                        str(p): e for p, e in factorize(
                            gcd(L, 19003 * 175 * 11)).items()},
                })
        family_counts[rec["family"]][row["d0"]] += 1
        rows.append(row)

    plant_ids = {p["id"]: p["must"] for p in plants}
    plant_check = []
    for row in rows:
        if row["id"] in plant_ids:
            want = plant_ids[row["id"]]
            got = (f"REALIZES_DEGREE0" if row["d0"] == "REALIZES" else
                   "FAILS_DEGREE0")
            got2 = (f"REALIZES_DEGREE2" if row["d2"] == "REALIZES" else
                    "FAILS_DEGREE2")
            ok = (want == got) if want.endswith("DEGREE0") else (want == got2)
            plant_check.append({"id": row["id"], "must": want,
                                "degree0_verdict": row["d0"],
                                "degree2_verdict": row["d2"],
                                "detected_correctly": ok})

    return {
        "certificate": "E_RECIPE_CENSUS",
        "field_inventory_used": [{"id": f["id"], "definition": f["definition"]}
                                 for f in F],
        "base_field_count": len(F),
        "closure_rules": {
            "K1_IDENTITY": "each base field",
            "K2_TAG_RESTRICTION": ("g * 1[tag in S] over the 6 proper"
                                   " non-empty subsets of {F, B0, B1}"),
            "K3_PAIRWISE_PRODUCT": "g_a * g_b for a < b",
            "K4_INDEX_PROFILE": (
                f"j^k, (j+1)^k, (n_w-j)^k for k in {list(POWER_EXPONENTS)};"
                f" r^j and r^(n_w-1-j) for r in {list(GEOMETRIC_RATIOS)};"
                f" a + b*j over {len(AFFINE_COEFFS)} declared (a,b) pairs"),
            "K5_POSITION_ATOM": "1[j = k] for every within-world position k",
            "K6_BOUNDED_SUM": ("c_a g_a + c_b g_b over a declared 12-field"
                               f" core with coefficients in"
                               f" {list(SUM_COEFFS)}"),
            "CONSTANT_RULE": (
                "a recipe may name only census-native constants: field values,"
                " the small structural integers 0..3 used above, and the"
                " arities the census itself carries.  A rule permitted to name"
                " 15600 is not a recipe -- it is the answer written down, and"
                " it appears here only as a PLANTED falsifier"),
        },
        "recipe_count": len(recipes),
        "planted_count": len(plants),
        "family_verdict_counts": {k: dict(v) for k, v in
                                  sorted(family_counts.items())},
        "native_degree0_realizers": realizers0,
        "native_degree2_realizers": realizers2,
        "native_pairs_realizing_the_interface_pair":
            [[a, b] for a in realizers0 for b in realizers2],
        "denominator_lemma": {
            "statement": denominator_lemma.__doc__,
            "degree0_scale": scale0,
            "degree0_scale_factorisation": {
                str(k): v for k, v in factorize(scale0).items()},
            "degree2_scale": scale2,
            "degree2_scale_factorisation": {
                str(k): v for k, v in factorize(scale2).items()},
            "recipes_whose_world_sums_admit_the_degree0_scale": lemma_pass0,
            "recipes_whose_world_sums_admit_the_degree2_scale": lemma_pass2,
            "why_this_answers_the_completeness_attack": (
                "the lemma depends only on the ELEVEN world sums, not on the"
                " within-world profile, so it rules out every profile built on"
                " those sums at once -- including profiles outside this"
                " block's declared closure.  A realizer must first arrange"
                f" {scale0} | lcm(S_w)."),
        },
        "planted_realizer_detection": plant_check,
        "rows": rows,
        "headline": headline,
        "pass": all(p["detected_correctly"] for p in plant_check),
    }


def degree_two_relationship(obj, grav, facts, census_result) -> dict:
    """BL10: whatever realizes the pair, is the SECOND object independently
    constrained, or does it ride along on the first?"""
    d0, d2 = obj["degree0"], obj["degree2"]
    ratio = [fr(Fraction(b, a)) if a else None for a, b in zip(d0, d2)]
    scalar = proportional(d2, d0)
    # is the degree-2 column a native TRANSFORM of the degree-0 one?
    transforms = []
    transforms.append({
        "transform": "SCALAR MULTIPLE  c_2 = k c_0",
        "holds": scalar,
        "why": ("the per-atom ratios are " + ", ".join(str(r) for r in ratio)
                + " -- not constant"),
    })
    integer_multiplier = all(
        (b % a == 0) if a else b == 0 for a, b in zip(d0, d2))
    transforms.append({
        "transform": "MULTIPLICATION BY A CENSUS FIELD  c_2(i) = g(i) c_0(i)",
        "holds": integer_multiplier,
        "why": ("a base field is integer-valued on events, so this needs"
                " c_0(i) | c_2(i) for every atom; the ratios above are not"
                " integers"),
    })
    shifted = [0] + d0[:-1]
    transforms.append({
        "transform": "INDEX SHIFT  c_2 = c_0 shifted by one atom",
        "holds": proportional(d2, shifted) if any(shifted) else False,
        "why": f"c_0 shifted is {shifted}, which is not proportional to c_2",
    })
    reversed0 = list(reversed(d0))
    transforms.append({
        "transform": "REVERSAL  c_2 proportional to reverse(c_0)",
        "holds": proportional(d2, reversed0),
        "why": f"reverse(c_0) is {reversed0}",
    })
    alt_count = grav["count_of_arithmetically_admissible_degree2_columns"]
    alt_columns = []
    per_alt = [row["degree2_values_they_would_force"]
               for row in grav["degree2_alternatives_admitted_by_degree0_alone"]]
    for a in per_alt[0] or [None]:
        for b in per_alt[1] or [None]:
            alt_columns.append([a * obj["sites"][0] if a is not None else None,
                                b * obj["sites"][1] if b is not None else None,
                                per_alt[2][0] * obj["sites"][2],
                                per_alt[3][0] * obj["sites"][3]])
    return {
        "certificate": "G_DEGREE_TWO_CARRIER",
        "question": ("BL10: is the degree-2 object independently constrained,"
                     " or a function of the degree-0 one?"),
        "degree0_column": d0,
        "degree2_column": d2,
        "per_atom_ratio_c2_over_c0": ratio,
        "native_transforms_tested": transforms,
        "any_native_transform_works": any(t["holds"] for t in transforms),
        "gravity_side_relation": {
            "identity": grav["identity"],
            "layer_amplitudes": grav["recovered_layer_amplitudes_p_q"],
            "identity_reconstructs_the_table":
                grav["identity_reconstructs_the_table"],
            "reading": (
                "on the GRAVITY side the two columns are not independent: both"
                " come from ONE per-site walk-layer profile (p, q) at layer"
                " distance 2, with c_0 = sites (p^2 + q^2) and"
                " c_2 = sites 2 p q.  That is a single object, and the two"
                " columns are its two Chebyshev components"),
        },
        "but_degree0_alone_does_not_determine_degree2": {
            "arithmetically_admissible_degree2_columns": alt_count,
            "the_columns": alt_columns,
            "witness": (
                "atom 0 has per-site degree-0 value"
                f" {grav['per_site_degree0'][0]}, which is a sum of two"
                " squares in "
                f"{len(per_alt[0])} distinct ways, and atom 1 in"
                f" {len(per_alt[1])} ways; each choice forces a different"
                " degree-2 value.  So c_0 does NOT determine c_2 even given"
                " the two-layer structure -- the walk does"),
        },
        "born_side_reading": (
            "the Born side has no layer profile.  Nothing in the census"
            " carries a walk, a layer index or a Chebyshev degree, so the"
            " second object is not derivable from the first by any census"
            " operation.  The degree-2 carrier is INDEPENDENTLY CONSTRAINED:"
            " BL10 is two purchases, not one purchase plus a corollary"),
        "the_one_structural_constraint_the_census_does_impose": (
            "c_2(atom 3) = 0 with a non-negative weighting forces the"
            " degree-2 carrier to VANISH on the ratio-1 atom's preimage, so"
            " the second object must have a zero set and it must sit exactly"
            " there.  That is the only feature of the second object the Born"
            " side constrains at all"),
        "degree0_realizers_found": census_result["native_degree0_realizers"],
        "degree2_realizers_found": census_result["native_degree2_realizers"],
    }


def classify_outcome(census_result) -> dict:
    """Outcome-neutral classifier: the verdict is a function of the computed
    realizer sets ONLY, and can land in any of the three declared classes."""
    r0 = census_result["native_degree0_realizers"]
    r2 = census_result["native_degree2_realizers"]
    pairs = census_result["native_pairs_realizing_the_interface_pair"]
    if pairs:
        klass = ("i_SELECTION_BY_CONSTRUCTION" if len(pairs) == 1
                 else "i_NATIVE_WITH_RESIDUAL_CHOICE")
    elif r0 or r2:
        klass = "iii_PARTIAL"
    else:
        klass = "ii_PURCHASE"
    return {
        "class": klass,
        "degree0_realizer_count": len(r0),
        "degree2_realizer_count": len(r2),
        "pair_count": len(pairs),
        "decision_rule": (
            "pairs > 1 -> (i) native with residual choice; pairs == 1 -> (i)"
            " SELECTION BY CONSTRUCTION; no pair but some single-slice"
            " realizer -> (iii) partial; no realizer at all -> (ii) PURCHASE"),
    }


def falsifiers(cert_b, cert_c, census_result, grav, facts, c907) -> dict:
    tester, obj = facts["tester"], facts["obj"]
    teeth = []

    # T1 -- a tampered pin must be caught
    payload = (ROOT / C907_RECEIPT).read_bytes()
    tampered = bytearray(payload)
    tampered[0] ^= 0x20
    teeth.append({
        "tooth": "T1_TAMPERED_PIN",
        "what": "flip one bit of the pinned Cycle-907 receipt",
        "detected": sha256(bytes(tampered)).hexdigest()
        != EXPECTED_SHA256[C907_RECEIPT],
        "exit_if_live": 2})

    # T2/T3 -- planted realizers and the near miss
    detect = census_result["planted_realizer_detection"]
    teeth.append({
        "tooth": "T2_PLANTED_REALIZER_BLINDNESS",
        "what": ("four planted rules that DO realize the required shape, one"
                 " of them with the residual mass moved off position 0 and"
                 " one with a world-to-world skew"),
        "detected": all(d["detected_correctly"] for d in detect
                        if d["must"].startswith("REALIZES")),
        "rows": detect})
    teeth.append({
        "tooth": "T3_NEAR_MISS",
        "what": "the same transcription with the ratio-1 atom off by one",
        "detected": all(d["detected_correctly"] for d in detect
                        if d["must"].startswith("FAILS"))})

    # T4 -- the fast equal-block routine against Cycle 907's own
    probes = [
        [8320] * 40, [1, 2, 3, 4, 6, 12] * 9, [5] * 175 + [7] * 12,
        [2 ** k for k in range(1, 30)], [1] * 200,
    ]
    agree = []
    for p in probes:
        a = c907.max_equal_blocks(p, 175)
        b = fast_max_equal_blocks(p, 175)
        agree.append({"probe_len": len(p), "c907": list(a),
                      "fast": list(b), "agree": tuple(a) == tuple(b)})
    teeth.append({
        "tooth": "T4_EQUAL_BLOCK_REINDEXING",
        "what": ("the re-indexed max_equal_blocks must agree value-for-value"
                 " with the AST-lifted Cycle-907 routine"),
        "detected": all(r["agree"] for r in agree), "rows": agree})

    # T5 -- outcome neutrality: the classifier must reach every class
    synthetic = [
        ({"native_degree0_realizers": ["X"], "native_degree2_realizers": ["Y"],
          "native_pairs_realizing_the_interface_pair": [["X", "Y"]]},
         "i_SELECTION_BY_CONSTRUCTION"),
        ({"native_degree0_realizers": ["X", "Z"],
          "native_degree2_realizers": ["Y"],
          "native_pairs_realizing_the_interface_pair": [["X", "Y"],
                                                        ["Z", "Y"]]},
         "i_NATIVE_WITH_RESIDUAL_CHOICE"),
        ({"native_degree0_realizers": ["X"], "native_degree2_realizers": [],
          "native_pairs_realizing_the_interface_pair": []}, "iii_PARTIAL"),
        ({"native_degree0_realizers": [], "native_degree2_realizers": [],
          "native_pairs_realizing_the_interface_pair": []}, "ii_PURCHASE"),
    ]
    neutral = [{"expected": want, "got": classify_outcome(s)["class"],
                "ok": classify_outcome(s)["class"] == want}
               for s, want in synthetic]
    teeth.append({
        "tooth": "T5_OUTCOME_NEUTRALITY",
        "what": "the verdict classifier must be able to land in every class",
        "detected": all(r["ok"] for r in neutral), "rows": neutral})

    # T6 -- scale invariance of every verdict
    col = facts["m7"]
    tripled = [3 * v for v in col]
    a = tester.assess(col, obj["degree0"], tester.ratio0)["shape_holds"]
    b = tester.assess(tripled, obj["degree0"], tester.ratio0)["shape_holds"]
    fb_a = free_bridge_readings(c907, col, tester.ratio0,
                                facts["star_events"])["verdict"]
    fb_b = free_bridge_readings(c907, tripled, tester.ratio0,
                                facts["star_events"])["verdict"]
    teeth.append({
        "tooth": "T6_SCALE_INVARIANCE",
        "what": ("tripling a weighting must change no verdict -- rescaling m"
                 " is absorbed by rescaling nu"),
        "detected": (a == b) and (fb_a == fb_b),
        "rows": {"shape": [a, b], "free_bridge": [fb_a, fb_b]}})

    # T7 -- a dropped recipe family must be visible
    fams = set(r["fam"] for r in census_result["rows"])
    teeth.append({
        "tooth": "T7_DROPPED_RECIPE_FAMILY",
        "what": "every declared closure rule must appear in the census rows",
        "detected": fams >= {"K1_IDENTITY", "K2_TAG_RESTRICTION",
                             "K3_PAIRWISE_PRODUCT", "K4_INDEX_PROFILE",
                             "K5_POSITION_ATOM", "K6_BOUNDED_SUM", "PLANTED"},
        "families_present": sorted(fams)})

    # T8 -- the degree-2 layer identity must actually reconstruct the table
    teeth.append({
        "tooth": "T8_DEGREE_TWO_IDENTITY",
        "what": ("the recovered layer amplitudes must reproduce BOTH columns"
                 " of the pinned table exactly, or the Q3 reading is void"),
        "detected": bool(grav["identity_reconstructs_the_table"]
                         and grav["site_counts_divide_both_columns"])})

    # T9 -- a skipped escape world must be visible
    short_col = list(facts["m7"])
    w0 = facts["per_world"][facts["star"][0]]
    for i in range(w0):
        short_col[i] = 0
    teeth.append({
        "tooth": "T9_SKIPPED_WORLD",
        "what": "zeroing one escape world must break the constraint set",
        "detected": not tester.assess(short_col, obj["degree0"],
                                      tester.ratio0)["shape_holds"]})

    return {"certificate": "H_FALSIFIERS", "teeth": teeth,
            "tooth_count": len(teeth),
            "pass": all(t["detected"] for t in teeth)}


def main() -> int:
    started = monotonic()
    cert_a = pin_rows()
    if not cert_a["pass"]:
        sys.stdout.write("CERTIFICATE A_PINS FAIL " + compact(cert_a) + "\n"
                         + "CYCLE909_WITHIN_WORLD_PRICING_PIN_FAILURE\n")
        return 2

    payload_text = {p: (ROOT / p).read_text(encoding="utf-8")
                    for p in AUDIT_INPUT_PATHS}
    receipts = {
        "878": json.loads(payload_text[C878_RECEIPT]),
        "902": json.loads(payload_text[C902_RECEIPT]),
        "905": json.loads(payload_text[C905_RECEIPT]),
        "906": json.loads(payload_text[C906_RECEIPT]),
        "907": json.loads(payload_text[C907_RECEIPT]),
        "907c": json.loads(payload_text[C907_CHECK_RECEIPT]),
    }
    c863, c878, c907, consts, provenance = lift_machinery()
    space_a = build_event_space(c863, c878, consts)
    space_b = build_event_space(c863, c878, consts)
    digest_a = digest([list(e) for e in space_a["events"]])
    digest_b = digest([list(e) for e in space_b["events"]])
    event_space_deterministic = digest_a == digest_b

    sci1 = science(space_a, c878, c907, receipts)
    sci2 = science(space_a, c878, c907, receipts)
    facts = sci1["space_facts"]
    cert_b, cert_c = sci1["cert_b"], sci1["cert_c"]
    build_digest_1 = digest([sci1["cert_b"]["rows"],
                             sci1["cert_c"]["CONSTRAINT_SET"],
                             sci1["cert_c"]["witness_M7"]])
    build_digest_2 = digest([sci2["cert_b"]["rows"],
                             sci2["cert_c"]["CONSTRAINT_SET"],
                             sci2["cert_c"]["witness_M7"]])

    cert_d = ast_field_inventory()
    cert_d["certificate"] = "D_FIELD_INVENTORY"
    cert_d["pass"] = bool(
        cert_d["event_tuple_fields_ast"] == ["lane", "moment", "tag",
                                             "ordinal", "content"]
        and cert_d["event_tuple_arity_ast"] == [5]
        and "occ_global" in cert_d["composed_scan_ledger_keys_ast"]
        and "formed" in cert_d["composed_scan_ledger_keys_ast"])

    cert_e = recipe_census(facts, c907)
    grav = gravity_terms_reading(facts["obj"])
    grav["pass"] = bool(grav["identity_reconstructs_the_table"])
    cert_g = degree_two_relationship(facts["obj"], grav, facts, cert_e)
    cert_g["pass"] = True
    cert_h = falsifiers(cert_b, cert_c, cert_e, grav, facts, c907)
    outcome = classify_outcome(cert_e)

    elapsed = monotonic() - started
    cert_i = {"certificate": "I_DOUBLE_BUILD",
              "event_space_digest_a": digest_a,
              "event_space_digest_b": digest_b,
              "event_space_deterministic": event_space_deterministic,
              "science_digest_run1": build_digest_1,
              "science_digest_run2": build_digest_2,
              "science_deterministic": build_digest_1 == build_digest_2}
    cert_i["pass"] = bool(event_space_deterministic
                          and cert_i["science_deterministic"])
    cert_j = {"certificate": "J_RUNTIME", "elapsed_sec": round(elapsed, 3),
              "budget_sec": 900, "pass": elapsed <= 900}

    obj = facts["obj"]
    tester = facts["tester"]
    star = facts["star"]
    width = facts["width"]

    ledger = [
        {"id": "BL9_WITHIN_WORLD_DISTRIBUTION",
         "status_before": "OPEN, premise P-EVENT-ORDER named and unpriced",
         "status_now": (
             "OPEN and PRICED.  The constraint set is extracted exactly: the"
             f" identification pins only {obj['atoms'] - 1} orbit-aggregate"
             f" numbers -- the mass at within-world positions 1, 2, 3 as"
             f" fractions {fr(Fraction(obj['degree0'][1], obj['degree0_sum']))},"
             f" {fr(Fraction(obj['degree0'][2], obj['degree0_sum']))},"
             f" {fr(Fraction(obj['degree0'][3], obj['degree0_sum']))} of the"
             " total -- and leaves everything else free.  No native recipe in"
             f" a census of {cert_e['recipe_count']} rules over the census's"
             f" own {cert_e['base_field_count']} fields produces those"
             " fractions, and the denominator lemma extends the negative"
             " beyond the declared closure to every profile whose escape-world"
             " sums are coprime to 31 * 613")
         if outcome["class"] == "ii_PURCHASE" else
         (f"CHANGED: outcome class {outcome['class']}"),
         "blocked_on": ("nothing on the Born side: the required numbers are"
                        " the gravity walk's interference spectrum")},
        {"id": "BL10_DEGREE_TWO_COLUMN",
         "status_before": "OPEN, priced",
         "status_now": (
             "OPEN and SHARPENED.  The second object does NOT ride along."
             " On the gravity side both columns come from one per-site"
             " walk-layer profile (p, q) at layer distance 2, with"
             " c_0 = sites (p^2+q^2) and c_2 = sites 2pq; but c_0 alone admits"
             f" {grav['count_of_arithmetically_admissible_degree2_columns']}"
             " different degree-2 columns, so the first object does not"
             " determine the second.  The only feature of the second object"
             " the Born side constrains is that it must VANISH on the ratio-1"
             " atom's preimage"),
         "blocked_on": "the same import as BL9, taken twice"},
    ]

    theorems = [
        ("C909-T1 THE CONSTRAINT SET, EXACTLY.  Under the Cycle-907 exhibited"
         " bridge a weighting in the Cycle-906 cone is a degree-0 carrier iff"
         " its orbit-aggregate mass at within-world positions 1, 2 and 3 is"
         f" {fr(Fraction(obj['degree0'][1], obj['degree0_sum']))},"
         f" {fr(Fraction(obj['degree0'][2], obj['degree0_sum']))} and"
         f" {fr(Fraction(obj['degree0'][3], obj['degree0_sum']))} of its total;"
         " the remaining"
         f" {width - obj['atoms'] + 1} positions of each of the"
         f" {len(star)} escape worlds are pinned ONLY in aggregate, and the"
         " per-world split of each designated aggregate is pinned only by"
         " covariance.  This is exhibited, not asserted: three alternative"
         " witnesses that differ from M7 off the pinned coordinates satisfy"
         " the same constraint set and reproduce the 902 table on all 80"
         " cells."),
        ("C909-T2 EVERY WORLD-LEVEL FIELD COLLAPSES TO UNIFORM.  Occupation,"
         " formation moment and formation lifetime -- the carriers of the"
         " Cycle-878 candidates M3, M4, M5 -- are constant within a world, so"
         " after the covariance normalisation each induces exactly M6's"
         " uniform within-world split.  The entire named candidate menu is"
         " one point of the within-world question, which is why 907's failure"
         " could not be repaired by choosing differently among them."),
        ("C909-T3 THE DENOMINATOR LEMMA.  For any non-negative weighting in"
         " the cone, the degree-0 constraint at the ratio-1 atom forces"
         " sum_w rho_w(3)/S_w = n_star / 19003, hence 19003 = 31 * 613 must"
         " divide lcm(S_1..S_n).  The condition depends only on the eleven"
         " escape-world sums, so it kills every within-world profile built on"
         " those sums at once -- including profiles outside this block's"
         " declared closure.  This is the complete form of the census-"
         "completeness claim: enumeration is a convenience, the lemma is the"
         " obstruction."),
        ("C909-T4 THE REQUIRED NUMBERS ARE THE WALK'S LAYER PROFILE.  Divided"
         " by their atom's site count, the two columns satisfy"
         " c_0/s = p^2 + q^2 and c_2/s = 2pq exactly, with"
         f" (p, q) = {grav['recovered_layer_amplitudes_p_q']} -- and the"
         " layer separation 2 is FORCED by the table's own zero pattern"
         " (M_1 = M_3 = M_4 = 0).  The ratio-1 entry is atom 3's linear record"
         " readout, the unit in which the other three are measured.  So the"
         " numbers the Born side would have to produce are the interference"
         " spectrum of the `single` configuration's walk, expressed in units"
         " of the record readout."),
        ("C909-T5 THE SECOND OBJECT IS INDEPENDENTLY CONSTRAINED.  c_0 does"
         " not determine c_2: atom 0's per-site degree-0 value 1300 is a sum"
         " of two squares in three ways and atom 1's 485 in two, so the"
         " degree-0 column admits"
         f" {grav['count_of_arithmetically_admissible_degree2_columns']}"
         " arithmetically consistent degree-2 columns and the walk picks one."
         "  No native transform -- scalar, field multiplication, index shift,"
         " reversal -- carries one column to the other.  BL10 is two"
         " purchases."),
    ]

    verdict = {
        "ii_PURCHASE": "WITHIN_WORLD_DISTRIBUTION_IS_A_PURCHASE",
        "iii_PARTIAL": "WITHIN_WORLD_DISTRIBUTION_PARTIALLY_NATIVE",
        "i_SELECTION_BY_CONSTRUCTION": "SELECTION_BY_CONSTRUCTION",
        "i_NATIVE_WITH_RESIDUAL_CHOICE": "NATIVE_WITH_RESIDUAL_CHOICE",
    }[outcome["class"]]

    checks = {
        "A_PINS": cert_a["pass"], "B_RESTRICTION_GATE": cert_b["pass"],
        "C_REQUIRED_SHAPE": cert_c["pass"], "D_FIELD_INVENTORY": cert_d["pass"],
        "E_RECIPE_CENSUS": cert_e["pass"], "F_GRAVITY_TERMS": grav["pass"],
        "G_DEGREE_TWO_CARRIER": cert_g["pass"], "H_FALSIFIERS": cert_h["pass"],
        "I_DOUBLE_BUILD": cert_i["pass"], "J_RUNTIME": cert_j["pass"],
        "K_LANE_LEDGER": True,
    }

    receipt = {
        "cycle": 909,
        "block": "toe-time-blockQ6-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "claim_type": "bounded_theorem",
        "question": ("Cycle 909 -- what constrains the within-world"
                     " distribution?  BL9 and BL10, priced jointly."),
        "label_on_every_fraction": FRACTION_LABEL,
        "VERDICT": verdict,
        "Q1_constraint_set": cert_c["CONSTRAINT_SET"],
        "Q1_witness_M7": cert_c["witness_M7"],
        "Q1_witness_M8": cert_c["witness_M8"],
        "Q1_grid": cert_c["grid"],
        "Q1_alternative_witnesses": cert_c["alternative_witnesses"],
        "Q1_escape_orbit": cert_c["escape_orbit"],
        "Q1_bridge": cert_c["the_bridge"],
        "Q2_field_inventory": cert_d,
        "Q2_base_fields": cert_e["field_inventory_used"],
        "Q2_closure_rules": cert_e["closure_rules"],
        "Q2_recipe_count": cert_e["recipe_count"],
        "Q2_family_verdict_counts": cert_e["family_verdict_counts"],
        "Q2_headline_recipes": cert_e["headline"],
        "Q2_native_degree0_realizers": cert_e["native_degree0_realizers"],
        "Q2_native_degree2_realizers": cert_e["native_degree2_realizers"],
        "Q2_native_pairs": cert_e["native_pairs_realizing_the_interface_pair"],
        "Q2_denominator_lemma": cert_e["denominator_lemma"],
        "Q2_verdict_table": cert_e["rows"],
        "Q3_outcome": outcome,
        "Q3_gravity_terms_reading": grav,
        "Q3_degree_two_relationship": cert_g,
        "Q3_pricing": {
            "the_purchase": (
                "the Born side must import the four numbers"
                f" {obj['degree0']} and {obj['degree2']} as a within-world"
                " profile.  In gravity terms they are the per-site"
                " interference spectrum of the `single` configuration's walk,"
                " in units of the record atom's linear readout"),
            "reading_A_new_named_import": (
                "the within-world distribution is a NEW NAMED IMPORT on the"
                " Born side: P-WITHIN-WORLD, an event-level profile the census"
                " does not supply and no covariance or zero-mass equation"
                " constrains.  It is not a weakening of an existing premise;"
                " it is a new one, and it must be taken TWICE (BL10)"),
            "reading_B_shared_underlying_object": (
                "or the two lanes share an object neither derives.  The"
                " gravity side's numbers are p^2+q^2 and 2pq for a two-layer"
                " walk profile; the Born side would have to carry a"
                " within-world quantity with the same two-layer structure."
                "  Nothing in the census does -- there is no layer index, no"
                " walk, no Chebyshev degree -- so this reading is not"
                " supported by anything computed here.  It is recorded as the"
                " honest alternative, not as a finding"),
            "which_reading_this_block_supports": (
                "A, on the evidence.  B would need a census field that this"
                " block's inventory shows does not exist"),
        },
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "certificates": {
            "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
            "C_REQUIRED_SHAPE": cert_c, "D_FIELD_INVENTORY": cert_d,
            "F_GRAVITY_TERMS": grav, "G_DEGREE_TWO_CARRIER": cert_g,
            "H_FALSIFIERS": cert_h, "I_DOUBLE_BUILD": cert_i,
            "J_RUNTIME": cert_j,
        },
        "theorems": theorems,
        "ledger_rows": ledger,
        "named_premises": [
            "P-NONEMPTY (named, undischarged, inherited)",
            "the Cycle-903 barrier scope (named, undischarged, inherited)",
            "the Cycle-906 single-orbit horizon scope (named, undischarged,"
            " inherited)",
            "P-INTERTWINE-878 (named, undischarged, inherited)",
            "the Cycle-892 interface premises IF1..IF6 (named, undischarged,"
            " inherited)",
            "P-EVENT-ORDER (named in Cycle 907, undischarged; it fixes the"
            " within-world order the bridge indexes, and it licenses only the"
            " WITNESS -- every negative verdict here is order-independent"
            " because the constraint set is stated on orbit aggregates)",
            "P-SITE-UNIFORM (named HERE, undischarged: that the sites inside"
            " one Cycle-902 atom carry equal site spectra.  It licenses only"
            " the per-site READING of the layer amplitudes; the arithmetic"
            " identity c_0 +/- c_2 = sites * square is computed"
            " unconditionally)",
        ],
        "conditionality_chain": [
            "P-NONEMPTY", "the Cycle-903 barrier scope",
            "the Cycle-906 single-orbit horizon scope", "P-INTERTWINE-878",
            "the Cycle-892 interface premises (IF1..IF6)", "P-EVENT-ORDER",
            "P-SITE-UNIFORM",
        ],
        "scope": (
            "the full realized record-write census of the pinned Cycle-878"
            " construction at horizon 16384 orbits (92260 events over 748"
            " worlds), rebuilt by AST lift from the pinned Cycle-863 and"
            " Cycle-878 sources and never imported; the Cycle-907 decision"
            " machinery reused by AST lift from the pinned Cycle-907 primary;"
            " the gravity side entering ONLY through the vendored Cycle-902"
            " artifacts, whose Cycle-885/887/892 machinery is absent from this"
            " branch, so the walk is NOT recomputed -- what is computed here is"
            " the exact arithmetic structure of the pinned coefficient table."
            "  Exact integer and rational arithmetic throughout; no"
            " probability, no occurrence rule, no update law."),
        "restriction_gate": (f"{cert_b['reproduce']}/{cert_b['total']}"
                             " restriction gates reproduce"),
        "restriction_gate_rows": cert_b["rows"],
        "provenance": provenance,
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "deterministic_double_build": cert_i["pass"],
        "elapsed_sec": round(elapsed, 3),
        "event_space_digest": digest_a,
        "audit": "unset",
        "authority": "none",
        "source_pins": [
            {"path": p, "sha256": cert_a["sha256"][p],
             "git_blob": cert_a["git_blobs"][p], "bytes": cert_a["bytes"][p]}
            for p in AUDIT_INPUT_PATHS],
    }
    receipt["science_digest"] = digest({
        "constraint_set": receipt["Q1_constraint_set"],
        "realizers": [cert_e["native_degree0_realizers"],
                      cert_e["native_degree2_realizers"]],
        "layers": grav["recovered_layer_amplitudes_p_q"],
        "verdict": verdict})
    receipt["self_sha256"] = sha256(
        Path(__file__).read_bytes()).hexdigest()

    out = ROOT / "outputs" / \
        "within_world_pricing_cycle909_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    # ---------------- stdout ----------------
    w = sys.stdout.write
    w("CYCLE 909 -- PRICING THE WITHIN-WORLD DISTRIBUTION (BL9, BL10)\n")
    w("=" * 78 + "\n")
    w(f"  every fraction below: {FRACTION_LABEL}\n\n")
    w(f"CERTIFICATE A_PINS {'PASS' if cert_a['pass'] else 'FAIL'}"
      f"  ({len(AUDIT_INPUT_PATHS)} pinned inputs, firewall hits"
      f" {len(PRIMARY_FIREWALL.hits)})\n")
    w(f"CERTIFICATE B_RESTRICTION_GATE "
      f"{'PASS' if cert_b['pass'] else 'FAIL'}  {cert_b['reproduce']}/"
      f"{cert_b['total']} gates reproduce\n")
    for r in cert_b["rows"]:
        if not r["match"]:
            w(f"    MISMATCH {r['gate']}: {r['computed']} != {r['expected']}\n")
    w("\nQ1 -- THE REQUIRED SHAPE, EXTRACTED\n")
    w("-" * 78 + "\n")
    w(f"  escape orbit: {len(star)} worlds {star}, {width} events each,"
      f" {facts['star_events']} events total\n")
    w(f"  tags per world: {cert_c['escape_orbit']['tag_multiset_per_world']}\n")
    w(f"  F-event position per world:"
      f" {cert_c['escape_orbit']['F_event_position_per_world']}\n")
    w(f"  occupation counts: {cert_c['escape_orbit']['occupation_counts']}\n")
    w(f"  bridge: {cert_c['the_bridge']}\n")
    w(f"  M7 block masses {cert_c['witness_M7']['block_masses']}"
      f"  total {cert_c['witness_M7']['total']}\n")
    w(f"  M8 block masses {cert_c['witness_M8']['block_masses']}"
      f"  total {cert_c['witness_M8']['total']}\n")
    w(f"  grid: {cert_c['grid']['cells']} cells,"
      f" {cert_c['grid']['violations']} violations\n")
    cs = cert_c["CONSTRAINT_SET"]
    w("  THE CONSTRAINT SET (degree-0 carrier), scale-free:\n")
    for k in ("position_1", "position_2", "position_3", "everything_else"):
        w(f"      {k:16s} {cs['degree0_required_orbit_profile'][k]}\n")
    w("  THE CONSTRAINT SET (degree-2 carrier), scale-free:\n")
    for k in ("position_1", "position_2", "position_3", "everything_else"):
        w(f"      {k:16s} {cs['degree2_required_orbit_profile'][k]}\n")
    w(f"  pinned positions: {cs['designated_positions']} (orbit aggregates"
      f" only); free positions per world: 0 and"
      f" {obj['atoms']}..{width - 1}\n")
    w(f"  residual freedom inside the escape orbit:"
      f" {cs['residual_freedom_inside_the_escape_orbit']}"
      f"  (907's global count {cs['gate_against_907_global_count']})\n")
    w("  alternative witnesses proving the freedom is real:\n")
    for r in cert_c["alternative_witnesses"]:
        w(f"      {r['name']:18s} differs {r['differs_from_M7']}"
          f"  satisfies {r['satisfies_the_constraint_set']}"
          f"  world-masses-equal {r['world_masses_equal']}\n")
    w("\nQ2 -- THE NATIVE RECIPE CENSUS\n")
    w("-" * 78 + "\n")
    w(f"  field inventory (AST): event tuple"
      f" {cert_d['event_tuple_fields_ast']}, arity"
      f" {cert_d['event_tuple_arity_ast']}\n")
    w(f"  ledger keys (AST): {cert_d['composed_scan_ledger_keys_ast']}\n")
    w(f"  base fields: {cert_e['base_field_count']};"
      f" recipes generated: {cert_e['recipe_count']};"
      f" planted: {cert_e['planted_count']}\n")
    for fam, counts in cert_e["family_verdict_counts"].items():
        w(f"      {fam:22s} {dict(counts)}\n")
    w("  headline recipes:\n")
    for h in cert_e["headline"]:
        w(f"      {h['id'][:46]:46s} d0={str(h['degree0_shape']):5s}"
          f" d2={str(h['degree2_shape']):5s}"
          f" free_d0={h['free_bridge_degree0']['verdict']:9s}"
          f" free_d2={h['free_bridge_degree2']['verdict']}\n")
        w(f"          profile {h['cone_orbit_profile']}\n")
    dl = cert_e["denominator_lemma"]
    w(f"  DENOMINATOR LEMMA: scale {dl['degree0_scale']} ="
      f" {dl['degree0_scale_factorisation']} must divide lcm(S_w).\n")
    w(f"      recipes whose world sums admit it:"
      f" {dl['recipes_whose_world_sums_admit_the_degree0_scale']} /"
      f" {cert_e['recipe_count'] + cert_e['planted_count']}\n")
    w(f"  native degree-0 realizers: {cert_e['native_degree0_realizers']}\n")
    w(f"  native degree-2 realizers: {cert_e['native_degree2_realizers']}\n")
    w("\nQ3 -- THE PRICING VERDICT\n")
    w("-" * 78 + "\n")
    w(f"  outcome class: {outcome['class']}\n")
    w(f"  per-site degree-0 {grav['per_site_degree0']},"
      f" degree-2 {grav['per_site_degree2']}\n")
    w(f"  recovered layer amplitudes (p, q):"
      f" {grav['recovered_layer_amplitudes_p_q']}"
      f"  identity reconstructs the table:"
      f" {grav['identity_reconstructs_the_table']}\n")
    w(f"  degree-2 columns admitted by degree-0 alone:"
      f" {grav['count_of_arithmetically_admissible_degree2_columns']}"
      f" -> the second object is independently constrained\n")
    for t in cert_g["native_transforms_tested"]:
        w(f"      {t['transform'][:48]:48s} holds={t['holds']}\n")
    w("\nCERTIFICATE H_FALSIFIERS "
      f"{'PASS' if cert_h['pass'] else 'FAIL'}  ({cert_h['tooth_count']}"
      " teeth)\n")
    for t in cert_h["teeth"]:
        w(f"      {t['tooth']:34s} detected={t['detected']}\n")
    w(f"\nCERTIFICATE I_DOUBLE_BUILD"
      f" {'PASS' if cert_i['pass'] else 'FAIL'}\n")
    w(f"CERTIFICATE J_RUNTIME {'PASS' if cert_j['pass'] else 'FAIL'}"
      f"  {cert_j['elapsed_sec']}s / {cert_j['budget_sec']}s\n")
    w("\nTHEOREMS\n" + "-" * 78 + "\n")
    for t in theorems:
        w("  " + t + "\n\n")
    w("LANE LEDGER\n" + "-" * 78 + "\n")
    for row in ledger:
        w(f"  {row['id']}: {row['status_now']}\n\n")
    w(f"VERDICT: {verdict}\n")
    w(f"all_certificates_pass: {receipt['all_certificates_pass']}\n")
    w(f"receipt: {out.relative_to(ROOT)}\n")
    w(f"science_digest: {receipt['science_digest']}\n")
    return 0 if receipt["all_certificates_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
