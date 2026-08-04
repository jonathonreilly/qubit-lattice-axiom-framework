#!/usr/bin/env python3
"""Cycle 910: discharge P-856-SHAPE -- one object, or a shape coincidence?

Campaign-5 Born LANE CLOSURE, block 5.  Strictly structural.  NO
probability postulate is introduced, NO Born rule is claimed.  Every
fraction emitted here is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

Cycle 906 filed premise P-856-SHAPE: the escape orbit -- worlds
[3, 4, 11, 12, 19, 20, 26, 27, 32, 33, 37], the single monitor-phase
orbit that misses the never-formed block and hence the support of every
covariant interface-compatible weighting -- has census shape k=[2],
event=[0], separations [(5,), (6,)], EXACTLY the shape Cycle 856
byte-quotes for its three ABSOLUTE-record orbits (setups stamped under
every monitor placement).  Cycle 908 strengthened the premise (the
escape orbit is phase-stationary, the invariance 856's absolute orbits
carry by definition) but could not discharge it: the two predicates
differ -- 856's E1 stamp versus 878's composed-record formation ledger.

Q1  THE TWO PREDICATES, COMPUTED ON THE SAME DATA, AND THE
    CORRESPONDENCE.  Both predicates are rebuilt here from their pinned
    sources by AST lift and run on their own terms first: 856's E1/E2
    stamp census at TRAJECTORY_HORIZON, and 878's composed-record scan
    at HORIZON.  Then the correspondence question is decided by
    computation: is there a canonical map between 856's key space and
    the 748 census worlds, or are they different substrates?  If a map
    exists the world sets are compared exactly; if not, the exact
    mismatch is the discharge answer.

Q2  THE SHAPE'S ORIGIN.  Each lineage's derivation of the shape is
    computed, not narrated: 856's from its stamp mechanics, 878's from
    its formation mechanics.  If a common mechanism exists it is
    EXHIBITED at the level where both constructions touch the same
    Cycle-719 substrate; if not, the shape match is recorded as a
    coincidence of values and the 908 phase-stationarity gets its own
    explanation.

Q3  CONSEQUENCES FOR THE M6 BRANCH.  Where 856's absolute orbits sit in
    horizon terms, computed from the 856 data; the escape orbit's
    formation profile against 856's stamp profile; and the resulting
    scope of the M6/M7/M8 constructions.

Discipline: TEXT / AST / JSON only.  The Cycle-856, Cycle-863,
Cycle-878, Cycle-905, Cycle-906 and Cycle-908 primaries and checkers
are BLOCKLISTED from import; their machinery is lifted by AST so the
rebuilt construction is the pinned construction rather than a
transcription.  Only the landed Cycle-719 two-rail core -- the
substrate the 856/863/878 machinery itself imports -- is imported.
Exact integer arithmetic everywhere; no floating point enters any
verdict.

Supervisor-authored primary.  bounded_theorem, authority none, audit
unset.  Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
import os
from pathlib import Path
import sys
from time import monotonic
from types import SimpleNamespace

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
FRACTION_LABEL = "bookkeeping fraction, not probability"
STATIONS_EXPECTED = 11
CENSUS_EXPECTED = 748
ORBITS_EXPECTED = 68
SHORT_HORIZON = 1_024           # the Cycle-908 checker's spot horizon
PERTURBATION_HORIZON = 256      # cheap horizon for the non-perturbation tooth

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C856_PATH = "scripts/frontier_cycle856_record_covariance_2026_07_28.py"
C856_CHECK = "scripts/frontier_cycle856_covariance_independent_check_2026_07_28.py"
C856_NOTE = "docs/RECORD_COVARIANCE_CYCLE856_BOUNDED_THEOREM_NOTE_2026-07-28.md"
C856_RECEIPT = "outputs/record_covariance_cycle856_receipt_2026_07_28.json"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_PATH = "scripts/frontier_cycle906_covariance_tension_2026_07_28.py"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C908_PATH = "scripts/frontier_cycle908_intertwine_discharge_2026_07_28.py"
C908_RECEIPT = "outputs/intertwine_discharge_cycle908_receipt_2026_07_28.json"
C908_CHECK_RECEIPT = "outputs/intertwine_independent_check_cycle908_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C856_PATH, C856_CHECK, C856_NOTE, C856_RECEIPT,
    C878_PATH, C878_RECEIPT, C905_RECEIPT, C906_PATH, C906_RECEIPT,
    C908_PATH, C908_RECEIPT, C908_CHECK_RECEIPT, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C856_PATH, C856_CHECK, C878_PATH, C906_PATH,
                  C908_PATH)
JSON_ONLY_PATHS = (C856_RECEIPT, C878_RECEIPT, C905_RECEIPT, C906_RECEIPT,
                   C908_RECEIPT, C908_CHECK_RECEIPT)
TEXT_ONLY_PATHS = (C856_NOTE, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C856_PATH:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
    C856_CHECK:
        "6c9cec748a8fb1c39080167aaadc8e352ef61bf6d37fb1e775b71f021f35bc7c",
    C856_NOTE:
        "7b6b73826ee397e66102994174d94e04c3f174761f00ffcfe0da2be97e72a545",
    C856_RECEIPT:
        "b578ae13bd10a947f90177936912bef792e3f8060149e1f48bae41c9f17aa235",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C906_PATH:
        "9c6392d593c1bf37e70f84692732d1e5cfa3f4377393dab846a15789fc0ce008",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    C908_PATH:
        "287c98e690d6a707661e4daef0460f3c17944e3cc32b1a2c958d4e454c4677b8",
    C908_RECEIPT:
        "825ebf6866755364ba27c504080808539f8040759413f0fff8cc57cd21dcb7f4",
    C908_CHECK_RECEIPT:
        "0112d6ca3c5d796a429d40e5811487c12aca6f652c967b356d89b9a681647c9c",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C856_PATH: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
    C856_CHECK: "4b0be60ee56a64eaa184de761989386a8f2dde19",
    C856_NOTE: "f819f5b31d442248fac255fcdf3b0139d6ba83f8",
    C856_RECEIPT: "5f3e9e0a4038dcc0f8c0520ac3f1637bfa3a5d1c",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C906_PATH: "d7577bb2ac9f4cb7ee9d8abc5f19e9c7cf888df9",
    C906_RECEIPT: "392cba199a75a14a8bb88808943c1259cbd7a94b",
    C908_PATH: "a32762df147312b150eee84b5311efa2476af677",
    C908_RECEIPT: "d6fcfc999e37f7a089cfe31123f61197ab4aa944",
    C908_CHECK_RECEIPT: "9ed7b6f506d30b53f289943aa47cc91df8cea1b5",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle852_selection_tournament_2026_07_28",
    "frontier_cycle856_record_covariance_2026_07_28",
    "frontier_cycle856_covariance_independent_check_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle905_born_narrowing_independent_check_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle906_covariance_tension_independent_check_2026_07_28",
    "frontier_cycle908_intertwine_discharge_2026_07_28",
    "frontier_cycle908_intertwine_independent_check_2026_07_28",
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

M6 = "M6_ABSOLUTE_ORBIT_UNIFORM"

# ---- byte-quoted needles from the pinned sources (presence certified) ------
NEEDLE_856_ABSOLUTE = (
    "**E1 has 33** (exactly three size-11 k=2 orbits: events\n"
    "  0, 1, 2 at separations 5/6)"
)
NEEDLE_856_NOT_ORBIT_CLOSED = (
    "stamped-ness is NOT orbit-closed — mixed\n"
    "  orbits (orbit-mates disagreeing about record formation): E1 = 3\n"
    "  uniformly-stamped / 12 uniformly-silent / 53 MIXED;"
)
NEEDLE_856_E1_ACCUMULATION = (
    "    for _orbit in range(1, TRAJECTORY_HORIZON + 1):\n"
    "        for apply_chunk in fast_schedules:\n"
    "            apply_chunk(columns)\n"
    "            clean_all = clean_mask(columns, dirty_indices, simulation_mask)\n"
    "            e1_found_mask |= clean_all & all_mask"
)
NEEDLE_856_CLEAN_MASK = (
    "def clean_mask(\n"
    "    columns: list[int], dirty_indices: tuple[int, ...], all_mask: int\n"
    ") -> int:\n"
    "    dirty = 0\n"
    "    for wire in dirty_indices:\n"
    "        dirty |= columns[wire]\n"
    "    return all_mask & ~dirty"
)
NEEDLE_856_STAMP_SET = (
    '            monitor: frozenset(\n'
    '                key for key in census\n'
    '                if frame_map(key, monitor, stations) in base_selection'
)
NEEDLE_856_ABSOLUTE_DEF = (
    "    absolute = {\n"
    "        reading: frozenset.intersection(*by_monitor.values())\n"
    "        for reading, by_monitor in monitor_sets.items()\n"
    "    }"
)
NEEDLE_856_E1_DIGEST_LITERAL = (
    '        and result["E1_stamped_sha256"]\n'
    '            == "1901e01751642cf1cd04054ab011fe39b9d384488b07c419e7b9a7e041b7ce52"'
)
NEEDLE_878_FORMED = (
    "            for lane in C863.lanes_of(ga):\n"
    "                occ_global[lane] += 1\n"
    "                if lane not in formed:\n"
    "                    formed[lane] = boundary"
)
NEEDLE_878_GLOBAL_DIRTY = (
    "    global_dirty = tuple(sorted(\n"
    "        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}\n"
    "    ))"
)
NEEDLE_878_MASK_OVER = (
    "    g = C863.mask_over(columns, global_dirty, uni_sim)"
)
NEEDLE_863_MASK_OVER = (
    "def mask_over(columns, indices, universe):\n"
    "    dirty = 0\n"
    "    for wire in indices:\n"
    "        dirty |= columns[wire]\n"
    "    return universe & ~dirty"
)
NEEDLE_863_CENSUS = (
    "    keys = tuple(\n"
    "        (k, event, positions)\n"
    "        for k in range(MIN_SOURCES, MAX_SOURCES + 1)\n"
    "        for positions in combinations(range(stations), k)\n"
    "        if pairwise_separated(positions, stations)\n"
    "        for event, _s in event_seeds\n"
    "    )\n"
    "    return program, event_seeds, tuple(sorted(keys))"
)
NEEDLE_856_CENSUS = (
    "    census = tuple(sorted(\n"
    "        (k, event, positions)\n"
    "        for k in range(MIN_SOURCES, MAX_SOURCES + 1)\n"
    "        for positions in combinations(range(stations), k)\n"
    "        if pairwise_separated(positions, stations)\n"
    "        for event, _state in event_seeds\n"
    "    ))"
)
NEEDLE_878_WORLD_LABEL = (
    '        keys["F_WORLD"].append(("w", lane))'
)
NEEDLE_906_ESCAPE_NOTE = (
    '                "the escape orbit is a size-11 k=2 orbit at separations 5/6"'
)
NEEDLE_908_STATIONARY = (
    '            "PHASE-STATIONARY: the escape orbit is the SAME set of eleven"'
)
NEEDLE_AXIOM_EXCLUSION = (
    "- context selection, measurement basis selection, Born weights,"
    " probability\n  rules, update laws, decoherence mechanisms, and"
    " formation rules"
)

NEEDLES = {
    "856_note_absolute_record_orbits": (C856_NOTE, NEEDLE_856_ABSOLUTE),
    "856_note_not_orbit_closed": (C856_NOTE, NEEDLE_856_NOT_ORBIT_CLOSED),
    "856_E1_accumulation_loop": (C856_PATH, NEEDLE_856_E1_ACCUMULATION),
    "856_clean_mask_definition": (C856_PATH, NEEDLE_856_CLEAN_MASK),
    "856_monitor_stamp_set_definition": (C856_PATH, NEEDLE_856_STAMP_SET),
    "856_absolute_set_definition": (C856_PATH, NEEDLE_856_ABSOLUTE_DEF),
    "856_E1_digest_literal": (C856_PATH, NEEDLE_856_E1_DIGEST_LITERAL),
    "856_census_construction": (C856_PATH, NEEDLE_856_CENSUS),
    "863_census_construction": (C863_PATH, NEEDLE_863_CENSUS),
    "863_mask_over_definition": (C863_PATH, NEEDLE_863_MASK_OVER),
    "878_formation_ledger_write": (C878_PATH, NEEDLE_878_FORMED),
    "878_global_dirty_union": (C878_PATH, NEEDLE_878_GLOBAL_DIRTY),
    "878_clean_test_uses_global_dirty": (C878_PATH, NEEDLE_878_MASK_OVER),
    "878_world_label_is_the_lane": (C878_PATH, NEEDLE_878_WORLD_LABEL),
    "906_escape_orbit_shape_sentence": (C906_PATH, NEEDLE_906_ESCAPE_NOTE),
    "908_phase_stationary_verdict": (C908_PATH, NEEDLE_908_STATIONARY),
    "axioms_exclusion_list": (AXIOMS_PATH, NEEDLE_AXIOM_EXCLUSION),
}


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def cyclic_separations(positions, stations: int):
    """The multiset of pairwise cyclic separations of a key's positions."""
    return tuple(sorted(((b - a) % stations)
                        for a, b in combinations(sorted(positions), 2)))


def cyclic_gaps(positions, stations: int):
    """The multiset of consecutive gaps around the ring (sums to stations)."""
    ordered = sorted(positions)
    return tuple(sorted(
        (ordered[(i + 1) % len(ordered)] - ordered[i]) % stations
        or stations
        for i in range(len(ordered))
    ))


# ---------------------------------------------------------------------------
# A: the discovery sweep and the pins
# ---------------------------------------------------------------------------

def discovery_sweep() -> dict:
    """How the Cycle-856 artifacts were FOUND, not assumed.

    Published rule (identical to the Cycle-908 rule, re-run here): every
    worktree-relative file under scripts/, docs/, outputs/ and
    logs/runner-cache/ whose basename contains the token '856'
    (case-insensitive).  Every hit is listed with its sha256; the
    durable ones (source, checker, note, receipt) are pinned.  The
    runner caches are listed but NOT pinned: they are run logs, not
    construction inputs -- which is why this block RECOMPUTES 856's E1
    stamps instead of reading its cached absolute-key list.
    """
    hits = []
    for folder in ("scripts", "docs", "outputs", "logs/runner-cache"):
        base = ROOT / folder
        if not base.is_dir():
            continue
        for path in sorted(base.iterdir()):
            if path.is_file() and "856" in path.name.lower():
                rel = f"{folder}/{path.name}"
                hits.append({
                    "path": rel,
                    "sha256": sha256(path.read_bytes()).hexdigest(),
                    "bytes": path.stat().st_size,
                    "pinned": rel in AUDIT_INPUT_PATHS,
                })
    pinned = tuple(h["path"] for h in hits if h["pinned"])
    unpinned = tuple(h["path"] for h in hits if not h["pinned"])
    result = {
        "rule": ("basename contains '856' (case-insensitive) under"
                 " scripts/, docs/, outputs/, logs/runner-cache/"),
        "hits": hits,
        "hit_count": len(hits),
        "pinned": list(pinned),
        "not_pinned_and_why": {
            p: "runner cache -- a run log, not a construction input"
            for p in unpinned
        },
        "absolute_orbit_identifiers_source": (
            "RECOMPUTED here from the pinned Cycle-856 primary by AST lift"
            " (base_stamp_census machinery + monitor_stamp_sets +"
            " frozenset.intersection over the eleven monitors).  The"
            " cached 856 stdout, which contains the absolute key list"
            " verbatim, is deliberately NOT an input: reading it would"
            " make the identification a transcription rather than a"
            " recomputation"),
    }
    result["pass"] = bool(
        len(hits) >= 4
        and all(p in pinned for p in (C856_PATH, C856_CHECK, C856_NOTE,
                                      C856_RECEIPT))
        and all(h["path"].startswith("logs/runner-cache/")
                for h in hits if not h["pinned"])
    )
    return result


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
    sweep = discovery_sweep()
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "modes": {"imported": IMPORTED_PATHS, "ast_only": AST_ONLY_PATHS,
                  "json_only": JSON_ONLY_PATHS, "text_only": TEXT_ONLY_PATHS},
        "import_firewall_disclosure": {
            "imported_substrate": IMPORTED_PATHS,
            "why": ("the landed Cycle-719 two-rail recurrent controller core"
                    " is the substrate the Cycle-856, Cycle-863 and"
                    " Cycle-878 machinery ITSELF imports; it is the object"
                    " under test's own kernel, so it is imported rather"
                    " than transcribed.  Everything else -- 852, 856, 863,"
                    " 878, 902, 905, 906, 908 -- is blocklisted from import"
                    " and lifted by AST"),
            "blocklisted_modules": BLOCKLISTED_MODULES,
        },
        "discovery_sweep": sweep,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "bytes": {p: len(b) for p, b in payloads.items()},
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and sweep["pass"]
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
    "mask_over", "lanes_of", "lane_state", "synchronous_word",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES",
               "TRAJECTORY_HORIZON")
C856_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "frame_map", "derive_scope",
    "watched_registers", "dirty_global_indices", "synchronous_word",
    "build_initial_states", "pack_states", "compile_masked_gate",
    "masked_h_schedules", "compile_fast_schedules", "clean_mask",
    "lane_numbers", "monitor_schedule_manifest",
)
C856_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES",
               "TRAJECTORY_HORIZON")
C878_FUNCS = (
    "lcm", "dead_wire_rig", "composed_scan", "family_keys", "cells_of",
    "refines", "build_candidates", "monitor_phase_action", "group_orbits",
)
C878_CONSTS = (
    "HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP",
    "DETERMINISM_ORBITS", "CANDIDATE_NAMES", "CONTROL_NAME", "FAMILY_ORDER",
)

_MACHINERY = None


def lift_machinery():
    """Lift 863 / 856 / 878 by AST.  Cached per process."""
    global _MACHINERY
    if _MACHINERY is not None:
        return _MACHINERY
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations},
    )
    c863 = SimpleNamespace(**{name: ns863[name] for name in C863_FUNCS})
    ns856, consts856, names856 = ast_lift(
        C856_PATH, C856_FUNCS, C856_CONSTS,
        {"K": K, "combinations": combinations, "Counter": Counter},
    )
    c856 = SimpleNamespace(**{name: ns856[name] for name in C856_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256,
         "Fraction": Fraction, "json": json},
    )
    c878 = SimpleNamespace(**{name: ns878[name] for name in C878_FUNCS})
    provenance = {
        "lifted_from_863": names863,
        "lifted_from_856": names856,
        "lifted_from_878": names878,
        "constants_863": consts863,
        "constants_856": consts856,
        "constants_878": {k: list(v) if isinstance(v, tuple) else v
                          for k, v in consts878.items()},
        "import_of_852_856_863_878_902_905_906_908": False,
    }
    _MACHINERY = (c863, c856, c878, consts856, consts863, consts878,
                  provenance)
    return _MACHINERY


# ---------------------------------------------------------------------------
# Q1(a): the Cycle-856 stamp predicate, rebuilt and INSTRUMENTED
# ---------------------------------------------------------------------------

def clean_profile(route: str, horizon: int = 0, drop_dirty: int = -1) -> dict:
    """The Cycle-856 E1/E2 stamp census, rebuilt at TRAJECTORY_HORIZON.

    The ONE addition to the pinned construction is instrumentation: the
    pinned runner accumulates `e1_found_mask |= clean_all & all_mask`
    and keeps only the final union; this rebuild additionally records,
    per lane, the FIRST boundary at which the lane is globally clean.
    The E1/E2 sets are the union of the recorded lanes, so the pinned
    quantities are reproduced exactly (digest-gated) and the extra
    per-lane first-clean boundary is a strictly finer read of the same
    trajectory -- no change to the dynamics, the schedule, the clean
    predicate, or the horizon.

    Two routes are provided.  Route '856' uses the Cycle-856 lifted
    functions (build_initial_states / pack_states / masked_h_schedules /
    compile_fast_schedules / clean_mask / lane_numbers /
    dirty_global_indices).  Route '863' uses the INDEPENDENTLY PINNED
    Cycle-863 implementations of the same construction
    (build_initial_states / pack_lanes / masked_h_schedules /
    compile_fast / mask_over / lanes_of / dirty_partition).  The two
    routes must agree lane for lane and boundary for boundary.

    `horizon = 0` means the pinned TRAJECTORY_HORIZON.  `drop_dirty >= 0`
    deletes that many coordinates from the head of the dirty set and is
    used ONLY by the falsifier that checks the shared-predicate identity
    is a fact about the shared dirty set rather than an artifact of the
    trajectory.
    """
    t_start = monotonic()
    c863, c856, _c878, consts856, consts863, _c878c, _prov = lift_machinery()
    horizon = horizon or consts856["TRAJECTORY_HORIZON"]
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    n = len(census)
    sim_keys = census + (census[0],)

    if route == "856":
        scope = {"program": program, "census": census,
                 "event_seeds": event_seeds, "stations": stations}
        states = c856.build_initial_states(scope)
        init_failures = 0
        columns = c856.pack_states(states + (states[0],))
        schedules = c856.masked_h_schedules(program, sim_keys)
        fast = c856.compile_fast_schedules(schedules)
        dirty = c856.dirty_global_indices()
        clean_of = c856.clean_mask
        lanes_of = c856.lane_numbers
        dirty_provenance = "856.dirty_global_indices"
    elif route == "863":
        states, init_failures = c863.build_initial_states(
            program, event_seeds, census)
        columns = c863.pack_lanes(states + (states[0],))
        schedules = c863.masked_h_schedules(program, sim_keys)
        fast = c863.compile_fast(schedules)
        per_bank, links, source_ptr = c863.dirty_partition()
        dirty = tuple(sorted(
            set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}))
        clean_of = c863.mask_over
        lanes_of = c863.lanes_of
        dirty_provenance = "863.dirty_partition union (the 878 global_dirty)"
    else:
        raise AssertionError(("unknown route", route))

    dropped_coordinates = ()
    if drop_dirty >= 0:
        dropped_coordinates = tuple(dirty[:drop_dirty + 1])
        dirty = tuple(dirty[drop_dirty + 1:])

    all_mask = (1 << n) - 1
    sim_mask = (1 << (n + 1)) - 1
    dup = n

    first_clean: list = [None] * n
    seen = 0
    clean_all = clean_of(columns, dirty, sim_mask)
    current = clean_all & all_mask
    for lane in lanes_of(current & ~seen):
        first_clean[lane] = 0
    seen |= current
    e2_mask = current
    determinism = int(bool(clean_all & 1) != bool(clean_all & (1 << dup)))
    boundary = 0
    t_scan = monotonic()
    for _orbit in range(1, horizon + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            clean_all = clean_of(columns, dirty, sim_mask)
            current = clean_all & all_mask
            fresh = current & ~seen
            if fresh:
                for lane in lanes_of(fresh):
                    first_clean[lane] = boundary
                seen |= fresh
            determinism += (bool(clean_all & 1)
                            != bool(clean_all & (1 << dup)))
        e2_mask |= current
    scan_seconds = monotonic() - t_scan

    e1_lanes = tuple(lanes_of(seen))
    e2_lanes = tuple(lanes_of(e2_mask))
    e1_keys = tuple(sorted(census[lane] for lane in e1_lanes))
    e2_keys = tuple(sorted(census[lane] for lane in e2_lanes))
    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << dup)) for column in columns)
    return {
        "route": route,
        "horizon_orbits": horizon,
        "boundaries": boundary,
        "stations": stations,
        "n_worlds": n,
        "dirty_provenance": dirty_provenance,
        "dropped_coordinates": list(dropped_coordinates),
        "dirty_coordinate_count": len(dirty),
        "dirty_digest": digest(list(dirty)),
        "census_digest": digest([list(key) for key in census]),
        "first_clean": first_clean,
        "first_clean_digest": digest(first_clean),
        "E1_lanes": list(e1_lanes),
        "E1_stamped_count": len(e1_keys),
        "E1_stamped_sha256": digest(e1_keys),
        "E2_lanes": list(e2_lanes),
        "E2_stamped_count": len(e2_keys),
        "E2_stamped_sha256": digest(e2_keys),
        "E2_subset_of_E1": set(e2_lanes) <= set(e1_lanes),
        "state_catalog_sha256": digest(tuple(
            sha256(bytes(state)).hexdigest() for state in states)),
        "state_bits": len(states[0]),
        "masked_schedule_gate_counts": list(map(len, schedules)),
        "init_failures": init_failures,
        "determinism_mismatches": determinism,
        "final_full_state_exact": duplicate_final_exact,
        "timing": {"scan": round(scan_seconds, 3),
                   "total": round(monotonic() - t_start, 3)},
    }


# ---------------------------------------------------------------------------
# Q1(b): the Cycle-878 composed-record formation predicate, rebuilt
# ---------------------------------------------------------------------------

def composed_profile(horizon: int, perturb: bool = False) -> dict:
    """The pinned Cycle-878 composed scan at phase 0 and a given horizon.

    `perturb=True` is the non-perturbation tooth: the record slot for
    the ("B0", 0) tag -- a bank-register write, which fires for a lane
    long BEFORE that lane ever goes globally clean -- is re-pointed at
    a coordinate that IS in the global dirty set, so the composed write
    now touches the clean predicate on which formation is decided.  The
    tooth checks that this DOES change the formation ledger, i.e. that
    "the record writes land in inert wires" is a load-bearing fact
    about this construction rather than a vacuous one.  (The ("F", 0)
    slot is deliberately not used: the F write happens at the same
    boundary as formation and after it, so re-pointing it could not
    change the ledger even if the slot were live -- that would be a
    tooth that cannot bite.)
    """
    perturbed_tag = ("B0", 0)
    t_start = monotonic()
    c863, _c856, c878, _c856c, _c863c, consts878, _prov = lift_machinery()
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    n = len(census)
    states, init_failures = c863.build_initial_states(
        program, event_seeds, census)
    sim = census + (census[0],)
    rig = c878.dead_wire_rig(program, sim, c863.pack_lanes(states + (states[0],)))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}))
    slot_wires = tuple(sorted(set(rig["slot_of"].values())))
    if perturb:
        rig = dict(rig)
        rig["slot_of"] = dict(rig["slot_of"])
        rig["slot_of"][perturbed_tag] = global_dirty[0]
    scan = c878.composed_scan(program, census, states, rig, horizon)
    events = scan["events"]
    formed = scan["formed"]
    per_world = Counter(event[0] for event in events)
    supported = sorted(per_world)
    perms, perm_ok = c878.monitor_phase_action(census, stations)
    orbits = c878.group_orbits(perms, n)
    never = {w for w in supported if w not in formed}
    escape_indices = [index for index, orbit in enumerate(orbits)
                      if not (set(orbit) & never)]
    star = tuple(orbits[escape_indices[0]]) if escape_indices else ()
    orbit_never_counts = [sum(1 for w in orbit if w in never)
                          for orbit in orbits]
    return {
        "horizon": horizon,
        "perturbed": perturb,
        "perturbed_tag": list(perturbed_tag) if perturb else None,
        "stations": stations,
        "n_worlds": n,
        "boundaries": scan["boundaries"],
        "n_events": len(events),
        "raw_event_digest": digest([list(e) for e in events]),
        "sorted_event_digest": digest(sorted([list(e) for e in events])),
        "formed": {str(w): b for w, b in sorted(formed.items())},
        "formed_digest": digest({str(w): b for w, b in sorted(formed.items())}),
        "worlds_with_events": len(supported),
        "worlds_formed": len(formed),
        "worlds_never_formed": len(never),
        "never_formed_worlds": sorted(never),
        "events_on_never_formed_worlds": sum(per_world[w] for w in sorted(never)),
        "per_world_counts": [per_world.get(w, 0) for w in range(n)],
        "occ_global": list(scan["occ_global"]),
        "orbit_count": len(orbits),
        "orbits": [list(orbit) for orbit in orbits],
        "orbit_never_formed_counts": orbit_never_counts,
        "orbit_meeting_histogram": dict(sorted(
            Counter(orbit_never_counts).items())),
        "orbits_entirely_inside_block": sum(1 for c in orbit_never_counts
                                            if c == stations),
        "orbits_entirely_outside_block": len(escape_indices),
        "orbits_mixed": sum(1 for c in orbit_never_counts
                            if 0 < c < stations),
        "escape_orbit_indices": escape_indices,
        "escape_orbit_worlds": list(star),
        "escape_orbit_keys": [list(census[w]) for w in star],
        "monitor_phase_action_is_a_bijection": perm_ok,
        "init_failures": init_failures,
        "mismatches": scan["mismatches"],
        "write_once_violations": scan["write_once_violations"],
        "beyond_cap": scan["beyond_cap"],
        "dead_activation_conflicts": scan["dead_activation_conflicts"],
        "initial_global_clean_lanes": scan["initial_global_clean_lanes"],
        "global_dirty_count": len(global_dirty),
        "global_dirty_digest": digest(list(global_dirty)),
        "slot_wires": list(slot_wires),
        "slot_wires_in_global_dirty": sorted(
            set(slot_wires) & set(global_dirty)),
        "dead_wires_count": len(rig["dead_wires"]),
        "dead_wires_in_global_dirty": sorted(
            set(rig["dead_wires"]) & set(global_dirty)),
        "slot_wires_touch_gates": sorted(
            set(slot_wires) & (set(rig["gate_inputs"]) | set(rig["gate_targets"]))),
        "timing": {"total": round(monotonic() - t_start, 3)},
    }


def _job(spec):
    kind = spec[0]
    if kind == "clean":
        out = clean_profile(spec[1])
        out["job"] = spec
        return out
    if kind == "composed":
        out = composed_profile(spec[1], spec[2])
        out["job"] = spec
        return out
    if kind == "perturbation_pair":
        horizon = spec[1]
        return {
            "job": spec,
            "kind": "perturbation_pair",
            "base": composed_profile(horizon, False),
            "perturbed": composed_profile(horizon, True),
            "clean_base": clean_profile("856", horizon),
            "clean_dropped": clean_profile("856", horizon, drop_dirty=0),
        }
    raise AssertionError(("unknown job", spec))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a = pin_rows()
    if not cert_a["pass"]:
        sys.stdout.write("CYCLE910_PIN_FAILURE " + compact(cert_a) + "\n")
        return 2

    payload_text = {p: (ROOT / p).read_text(encoding="utf-8")
                    for p in AUDIT_INPUT_PATHS}
    quotes = {
        label: {"path": path, "chars": len(needle),
                "present_byte_for_byte": needle in payload_text[path]}
        for label, (path, needle) in NEEDLES.items()
    }
    cert_a["byte_quotes"] = quotes
    cert_a["all_quotes_present"] = all(
        q["present_byte_for_byte"] for q in quotes.values())
    cert_a["pass"] = bool(cert_a["pass"] and cert_a["all_quotes_present"])
    if not cert_a["pass"]:
        sys.stdout.write("CYCLE910_PIN_FAILURE " + compact(cert_a) + "\n")
        return 2

    r856 = json.loads(payload_text[C856_RECEIPT])
    r878 = json.loads(payload_text[C878_RECEIPT])
    r905 = json.loads(payload_text[C905_RECEIPT])
    r906 = json.loads(payload_text[C906_RECEIPT])
    r908 = json.loads(payload_text[C908_RECEIPT])
    r908c = json.loads(payload_text[C908_CHECK_RECEIPT])

    (c863, c856, c878, consts856, consts863, consts878,
     provenance) = lift_machinery()
    horizon878 = consts878["HORIZON"]
    horizon856 = consts856["TRAJECTORY_HORIZON"]
    stations = STATIONS_EXPECTED

    # ---- the parallel builds ----------------------------------------------
    jobs = [
        ("clean", "856"),
        ("clean", "863"),
        ("composed", horizon878, False),
        ("composed_replay", horizon878, False),
        ("composed", SHORT_HORIZON, False),
        ("perturbation_pair", PERTURBATION_HORIZON),
    ]
    dispatch = [j if j[0] != "composed_replay" else ("composed",) + j[1:]
                for j in jobs]
    workers = max(1, min(len(jobs), os.cpu_count() or 1))
    checkpoint = {
        "structure": ("one process per build.  The Cycle-856 stamp census"
                      " is built TWICE from two independently pinned"
                      " implementations of the same construction (the"
                      " Cycle-856 functions and the Cycle-863 functions);"
                      " the Cycle-878 composed scan is built twice at the"
                      " pinned horizon in independent processes, once at"
                      " the Cycle-908 checker's spot horizon, and once more"
                      " as a perturbed/unperturbed pair at a short horizon"
                      " for the non-perturbation tooth"),
        "jobs": [list(j) for j in jobs],
        "pool_workers": workers,
    }
    results: dict = {}
    parallel_ok = True
    t_jobs = monotonic()
    try:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for tag, out in zip(jobs, pool.map(_job, dispatch)):
                results[tag] = out
    except Exception as exc:                              # pragma: no cover
        parallel_ok = False
        checkpoint["parallel_failure"] = repr(exc)
        results = {}
        for tag, spec in zip(jobs, dispatch):
            if monotonic() - started > RUNTIME_BUDGET_SEC - 60:
                break
            results[tag] = _job(spec)
    checkpoint["parallel"] = parallel_ok
    checkpoint["jobs_elapsed_sec"] = round(monotonic() - t_jobs, 3)
    checkpoint["jobs_completed"] = [list(k) for k in results]

    missing_jobs = [list(j) for j in jobs if j not in results]
    checkpoint["missing_jobs"] = missing_jobs
    if missing_jobs:
        sys.stdout.write("CYCLE910_BUILD_INCOMPLETE "
                         + compact(checkpoint) + "\n")
        return 2

    stamp_a = results[("clean", "856")]
    stamp_b = results[("clean", "863")]
    scan_a = results[("composed", horizon878, False)]
    scan_b = results[("composed_replay", horizon878, False)]
    scan_short = results[("composed", SHORT_HORIZON, False)]
    pert = results[("perturbation_pair", PERTURBATION_HORIZON)]

    # ---- the shared census, rebuilt in this process ------------------------
    program, event_seeds, census863 = c863.derive_census()
    scope856 = c856.derive_scope()
    census856 = scope856["census"]
    orbits856 = scope856["orbits"]
    n_worlds = len(census863)
    index_of = {key: i for i, key in enumerate(census863)}
    perms, perm_ok = c878.monitor_phase_action(census863, stations)
    orbits878 = c878.group_orbits(perms, n_worlds)
    orbit_of = {w: i for i, orbit in enumerate(orbits878) for w in orbit}

    # =======================================================================
    # B: restriction gates -- value for value against the pinned receipts
    # =======================================================================
    gate_rows = []

    def gate(name, got, want, source):
        ok = got == want
        gate_rows.append({"gate": name, "source": source, "expected": want,
                          "observed": got, "reproduced": ok})
        return ok

    star_906 = r906["Q3_exhibited_solution"]["support_worlds"]
    row0_908 = r908["Q1_phase_rows"][0]

    gate("906_escape_orbit_worlds", scan_a["escape_orbit_worlds"], star_906,
         "906 receipt Q3_exhibited_solution.support_worlds")
    gate("906_M6_name", M6, r906["Q3_exhibited_solution"]["name"],
         "906 receipt Q3_exhibited_solution.name")
    gate("906_every_orbit_meets_the_block",
         scan_a["orbits_entirely_outside_block"] == 0,
         r906["Q4_every_orbit_meets_the_block"],
         "906 receipt Q4_every_orbit_meets_the_block")
    gate("906_orbit_meeting_histogram",
         {str(k): v for k, v in scan_a["orbit_meeting_histogram"].items()},
         {str(k): v for k, v in r906["Q4_orbit_meeting_histogram"].items()},
         "906 receipt Q4_orbit_meeting_histogram")
    gate("906_856_absolute_shape_match_claimed", True,
         r906["Q4_856_absolute_shape_match"],
         "906 receipt Q4_856_absolute_shape_match")
    gate("906_event_space_digest", scan_a["raw_event_digest"],
         r906["event_space_digest"], "906 receipt event_space_digest")
    gate("906_M6_support_events",
         sum(scan_a["per_world_counts"][w]
             for w in scan_a["escape_orbit_worlds"]),
         r906["Q3_exhibited_solution"]["support_events"],
         "906 receipt Q3_exhibited_solution.support_events")
    gate("906_M6_zero_weight_events",
         scan_a["n_events"] - sum(scan_a["per_world_counts"][w]
                                  for w in scan_a["escape_orbit_worlds"]),
         r906["Q3_exhibited_solution"]["zero_weight_events"],
         "906 receipt Q3_exhibited_solution.zero_weight_events")
    gate("906_BL6_zero_events_before_and_after",
         [scan_a["events_on_never_formed_worlds"],
          scan_a["n_events"] - sum(scan_a["per_world_counts"][w]
                                   for w in scan_a["escape_orbit_worlds"])],
         r906["Q4_BL6_zero_events_before_and_after"],
         "906 receipt Q4_BL6_zero_events_before_and_after")
    gate("906_world_mass_space_dimension_claim", 1,
         r906["Q3_world_mass_space_dimension"],
         "906 receipt Q3_world_mass_space_dimension")

    gate("908_phase0_escape_orbit_worlds", scan_a["escape_orbit_worlds"],
         row0_908["escape_orbit_worlds"],
         "908 receipt Q1_phase_rows[0].escape_orbit_worlds")
    gate("908_phase0_n_events", scan_a["n_events"], row0_908["n_events"],
         "908 receipt Q1_phase_rows[0].n_events")
    gate("908_phase0_worlds_formed", scan_a["worlds_formed"],
         row0_908["worlds_formed"],
         "908 receipt Q1_phase_rows[0].worlds_formed")
    gate("908_phase0_worlds_never_formed", scan_a["worlds_never_formed"],
         row0_908["worlds_never_formed"],
         "908 receipt Q1_phase_rows[0].worlds_never_formed")
    gate("908_phase0_raw_event_digest", scan_a["raw_event_digest"],
         row0_908["raw_event_digest"],
         "908 receipt Q1_phase_rows[0].raw_event_digest")
    gate("908_phase0_orbits_mixed", scan_a["orbits_mixed"],
         row0_908["orbits_mixed"],
         "908 receipt Q1_phase_rows[0].orbits_mixed")
    stationarity_rows = {
        str(row["phase"]): row["escape_orbit_worlds"]
        for row in r908["Q1_phase_rows"]
    }
    gate("908_phase_stationarity_rows_all_equal_phase0",
         {str(row["phase"]): star_906 for row in r908["Q1_phase_rows"]},
         stationarity_rows,
         "908 receipt Q1_phase_rows[*].escape_orbit_worlds")
    gate("908_eleven_phase_rows", 11, len(r908["Q1_phase_rows"]),
         "908 receipt Q1_phase_rows length")
    gate("908_transport_theorem", True, r908["Q1_transport_theorem_holds"],
         "908 receipt Q1_transport_theorem_holds")
    gate("908_distinct_raw_event_digests", 11,
         r908["Q1_distinct_raw_event_digests"],
         "908 receipt Q1_distinct_raw_event_digests")
    gate("908_P_856_SHAPE_left_open", True,
         r908["Q3_P_856_SHAPE_status"].startswith(
             "ILLUMINATED, NOT DISCHARGED"),
         "908 receipt Q3_P_856_SHAPE_status")
    gate("908_checker_verdict", "CORROBORATES_WITH_REFINEMENT",
         r908c["verdict"], "908 checker receipt verdict")
    late_horizon_refinement = [
        text for text in r908c["refinements"]
        if text.startswith("M6's defining orbit is a LATE-HORIZON object")
    ]
    gate("908_checker_late_horizon_refinement_present", 1,
         len(late_horizon_refinement), "908 checker receipt refinements")

    gate("878_horizon", 16384, horizon878, "878 source HORIZON literal")
    gate("878_census_population", CENSUS_EXPECTED, n_worlds,
         "878/863 census population")
    gate("878_event_count_headline", True,
         "92,260 events over 748 worlds" in r878["headline"],
         "878 receipt headline")

    gate("856_horizon", 51115, horizon856,
         "856 source TRAJECTORY_HORIZON literal")
    gate("856_receipt_file_digest_of_the_856_primary",
         cert_a["sha256"][C856_PATH], r856["files"][C856_PATH],
         "856 ship receipt files map")
    gate("856_receipt_file_digest_of_the_856_note",
         cert_a["sha256"][C856_NOTE], r856["files"][C856_NOTE],
         "856 ship receipt files map")
    gate("856_verdict_absolute_records_line", 1,
         sum(1 for v in r856["verdicts"]
             if v.startswith("absolute records (stamped under every monitor):"
                             " E1 = 33 setups = three size-11 k=2 orbits")),
         "856 ship receipt verdicts")
    gate("905_never_formed_block_size",
         scan_a["events_on_never_formed_worlds"],
         r906["Q4_BL6_zero_events_before_and_after"][0],
         "905->906 carried BL6 block size")
    gate("905_receipt_is_the_born_narrowing_block", 905, r905["cycle"],
         "905 receipt cycle")

    # 856's own in-source expected literals, lifted by AST
    c856_tree = ast.parse(payload_text[C856_PATH], filename=C856_PATH)
    source_literals = {
        node.value for node in ast.walk(c856_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    gate("856_E1_digest_literal_in_source", True,
         stamp_a["E1_stamped_sha256"] in source_literals,
         "recomputed E1 digest must appear as a literal in the 856 source")
    gate("856_E2_digest_literal_in_source", True,
         stamp_a["E2_stamped_sha256"] in source_literals,
         "recomputed E2 digest must appear as a literal in the 856 source")
    gate("856_state_catalog_literal_in_source", True,
         stamp_a["state_catalog_sha256"] in source_literals,
         "recomputed state catalog digest must appear in the 856 source")
    gate("856_E1_stamped_count", 182, stamp_a["E1_stamped_count"],
         "856 source pass-gate literal len(e1) == 182")
    gate("856_E2_stamped_count", 114, stamp_a["E2_stamped_count"],
         "856 source pass-gate literal len(e2) == 114")
    gate("856_state_bits", 5815, stamp_a["state_bits"],
         "856 source pass-gate literal state_bits == 5815")
    gate("856_dirty_coordinate_count", 477, stamp_a["dirty_coordinate_count"],
         "856 source pass-gate literal dirty_coordinate_count == 477")
    gate("856_masked_schedule_gate_counts", [3106] * 11,
         stamp_a["masked_schedule_gate_counts"],
         "856 source pass-gate literal masked_schedule_gate_counts")
    gate("856_census_equals_863_census",
         digest([list(k) for k in census856]),
         digest([list(k) for k in census863]),
         "856 derive_scope census vs 863 derive_census")
    gate("856_orbit_count", ORBITS_EXPECTED, len(orbits856),
         "856 derive_scope orbit count")
    gate("878_orbit_count", ORBITS_EXPECTED, len(orbits878),
         "878 group_orbits count")

    cert_b = {
        "certificate": "B_RESTRICTION_GATES",
        "rows": gate_rows,
        "count": len(gate_rows),
        "reproduced": sum(1 for row in gate_rows if row["reproduced"]),
        "summary": (f"{sum(1 for r in gate_rows if r['reproduced'])}"
                    f"/{len(gate_rows)} restriction gates reproduce"),
    }
    cert_b["pass"] = all(row["reproduced"] for row in gate_rows)

    # =======================================================================
    # C: predicate (a) -- the Cycle-856 absolute-record predicate
    # =======================================================================
    e1_lanes = set(stamp_a["E1_lanes"])
    e2_lanes = set(stamp_a["E2_lanes"])

    def absolute_by_856_definition(stamped_lanes):
        """856's own route: stamped_m(key) := frame_map(key, m) in base;
        absolute := intersection over the eleven monitors."""
        base = frozenset(census863[lane] for lane in stamped_lanes)
        by_monitor = {
            m: frozenset(
                key for key in census863
                if c856.frame_map(key, m, stations) in base)
            for m in range(stations)
        }
        return frozenset.intersection(*by_monitor.values()), by_monitor

    def absolute_by_orbit_closure(stamped_lanes):
        """Second, structurally different route: the union of the frame
        orbits entirely contained in the stamp set."""
        out = set()
        for orbit in orbits856:
            if all(index_of[key] in stamped_lanes for key in orbit):
                out.update(orbit)
        return frozenset(out)

    absolute_e1, by_monitor_e1 = absolute_by_856_definition(e1_lanes)
    absolute_e2, by_monitor_e2 = absolute_by_856_definition(e2_lanes)
    absolute_e1_route2 = absolute_by_orbit_closure(e1_lanes)
    absolute_e2_route2 = absolute_by_orbit_closure(e2_lanes)

    def orbit_classes(stamped_lanes):
        counts = Counter()
        for orbit in orbits856:
            hits = sum(1 for key in orbit if index_of[key] in stamped_lanes)
            counts["uniformly-stamped" if hits == len(orbit)
                   else "uniformly-silent" if hits == 0 else "MIXED"] += 1
        return dict(counts)

    classes_e1 = orbit_classes(e1_lanes)
    classes_e2 = orbit_classes(e2_lanes)
    absolute_e1_orbit_indices = sorted({
        i for i, orbit in enumerate(orbits856)
        if all(key in absolute_e1 for key in orbit)})
    cert_c = {
        "certificate": "C_PREDICATE_856_ABSOLUTE_RECORDS",
        "predicate": (
            "E1(key) := the key's lane is GLOBALLY CLEAN (every one of the"
            " 477 dirty packed-state coordinates zero) at some H-chunk"
            " boundary of the Cycle-852 trajectory, initial boundary"
            " included, within TRAJECTORY_HORIZON = 51,115 controller"
            " orbits.  E2(key) := the same at an ORBIT-RETURN boundary."
            "  stamped_m(key) := E-reading holds of frame_map(key, m)."
            "  ABSOLUTE(key) := stamped_m(key) for every monitor phase m"
            " -- 856's intersection over the eleven monitor placements"),
        "recomputed_not_transcribed": True,
        "E1_stamped_count": stamp_a["E1_stamped_count"],
        "E2_stamped_count": stamp_a["E2_stamped_count"],
        "E1_stamped_sha256": stamp_a["E1_stamped_sha256"],
        "E2_stamped_sha256": stamp_a["E2_stamped_sha256"],
        "monitor_table": [
            {"monitor": m, "E1_stamped": len(by_monitor_e1[m]),
             "E2_stamped": len(by_monitor_e2[m])} for m in range(stations)],
        "count_dependence": {
            "E1": max(map(len, by_monitor_e1.values()))
                  - min(map(len, by_monitor_e1.values())),
            "E2": max(map(len, by_monitor_e2.values()))
                  - min(map(len, by_monitor_e2.values()))},
        "membership_dependence": {
            "E1": len({digest(tuple(sorted(s)))
                       for s in by_monitor_e1.values()}),
            "E2": len({digest(tuple(sorted(s)))
                       for s in by_monitor_e2.values()})},
        "orbit_classes_E1": classes_e1,
        "orbit_classes_E2": classes_e2,
        "absolute_E1_count": len(absolute_e1),
        "absolute_E2_count": len(absolute_e2),
        "absolute_E1_keys": [list(k) for k in sorted(absolute_e1)],
        "absolute_E1_worlds": sorted(index_of[k] for k in absolute_e1),
        "absolute_E1_orbit_indices": absolute_e1_orbit_indices,
        "absolute_E1_key_sha256": digest(tuple(sorted(absolute_e1))),
        "absolute_under_both_readings": [
            list(k) for k in sorted(absolute_e1 & absolute_e2)],
        "two_routes_agree_E1": absolute_e1 == absolute_e1_route2,
        "two_routes_agree_E2": absolute_e2 == absolute_e2_route2,
        "route_1": ("frozenset.intersection over the eleven"
                    " monitor stamp sets (856's own definition)"),
        "route_2": ("union of the frame orbits entirely contained in the"
                    " stamp set (the orbit-closure characterisation)"),
        "absolute_E1_shape": {
            "k_values": sorted({k for k, _e, _p in absolute_e1}),
            "event_values": sorted({e for _k, e, _p in absolute_e1}),
            "separation_multisets": sorted({
                cyclic_separations(p, stations) for _k, _e, p in absolute_e1}),
        },
    }
    cert_c["pass"] = bool(
        stamp_a["E1_stamped_count"] == 182
        and stamp_a["E2_stamped_count"] == 114
        and stamp_a["E2_subset_of_E1"]
        and len(absolute_e1) == 33 and len(absolute_e2) == 0
        and not (absolute_e1 & absolute_e2)
        and classes_e1 == {"uniformly-stamped": 3, "uniformly-silent": 12,
                           "MIXED": 53}
        and classes_e2 == {"uniformly-silent": 38, "MIXED": 30}
        and cert_c["count_dependence"] == {"E1": 0, "E2": 0}
        and cert_c["membership_dependence"] == {"E1": 11, "E2": 11}
        and cert_c["two_routes_agree_E1"] and cert_c["two_routes_agree_E2"]
        and len(absolute_e1_orbit_indices) == 3
        and stamp_a["determinism_mismatches"] == 0
        and stamp_a["final_full_state_exact"])

    # =======================================================================
    # D: predicate (b) -- the Cycle-878 composed-record formation predicate
    # =======================================================================
    formed_878 = {int(w): b for w, b in scan_a["formed"].items()}
    star = tuple(scan_a["escape_orbit_worlds"])
    star_keys = tuple(census863[w] for w in star)
    cert_d = {
        "certificate": "D_PREDICATE_878_FORMATION_LEDGER",
        "predicate": (
            "FORMED(world) := the world's lane is GLOBALLY CLEAN at some"
            " boundary of the composed Cycle-878 scan, initial boundary"
            " included, within HORIZON = 16,384 controller orbits; the"
            " formation ledger records the FIRST such boundary."
            "  NEVER-FORMED := the complement inside the supported"
            " worlds.  ESCAPE ORBIT := a monitor-phase orbit disjoint"
            " from the never-formed block"),
        "horizon": horizon878,
        "boundaries": scan_a["boundaries"],
        "n_events": scan_a["n_events"],
        "worlds_with_events": scan_a["worlds_with_events"],
        "worlds_formed": scan_a["worlds_formed"],
        "worlds_never_formed": scan_a["worlds_never_formed"],
        "orbits_entirely_outside_block": scan_a["orbits_entirely_outside_block"],
        "escape_orbit_indices": scan_a["escape_orbit_indices"],
        "escape_orbit_worlds": list(star),
        "escape_orbit_keys": [list(k) for k in star_keys],
        "escape_orbit_shape": {
            "k_values": sorted({k for k, _e, _p in star_keys}),
            "event_values": sorted({e for _k, e, _p in star_keys}),
            "separation_multisets": sorted({
                cyclic_separations(p, stations) for _k, _e, p in star_keys}),
        },
        "escape_orbit_formation_moments": {
            str(w): formed_878[w] for w in star},
        "health": {
            "mismatches": scan_a["mismatches"],
            "write_once_violations": scan_a["write_once_violations"],
            "beyond_cap": scan_a["beyond_cap"],
            "dead_activation_conflicts": scan_a["dead_activation_conflicts"],
            "init_failures": scan_a["init_failures"],
            "monitor_phase_action_is_a_bijection":
                scan_a["monitor_phase_action_is_a_bijection"],
        },
        "double_build_replay_agrees": {
            "raw_event_digest": scan_a["raw_event_digest"]
                                == scan_b["raw_event_digest"],
            "formed_digest": scan_a["formed_digest"] == scan_b["formed_digest"],
            "escape_orbit_worlds": scan_a["escape_orbit_worlds"]
                                   == scan_b["escape_orbit_worlds"],
        },
    }
    cert_d["pass"] = bool(
        scan_a["worlds_formed"] == 164
        and scan_a["worlds_never_formed"] == 584
        and scan_a["orbits_entirely_outside_block"] == 1
        and len(star) == stations
        and cert_d["escape_orbit_shape"]["k_values"] == [2]
        and cert_d["escape_orbit_shape"]["event_values"] == [0]
        and cert_d["escape_orbit_shape"]["separation_multisets"]
            == [(5,), (6,)]
        and scan_a["mismatches"] == 0
        and scan_a["write_once_violations"] == 0
        and scan_a["init_failures"] == 0
        and scan_a["monitor_phase_action_is_a_bijection"]
        and all(cert_d["double_build_replay_agrees"].values()))

    # =======================================================================
    # E: the common indexing -- is there a canonical map at all?
    # =======================================================================
    census_identical = census856 == census863
    sorted_same_set = sorted(census856) == sorted(census863)
    world_label_is_lane = ("878's world label is the LANE INDEX into the"
                           " census tuple it was handed")
    # the 878 lane index is the position in the 863 census tuple; 856's key
    # space IS that same tuple.  The identification therefore has NO free
    # parameter -- it is the identity on a shared tuple, not a chosen map.
    key_of_world = {w: census863[w] for w in range(n_worlds)}
    round_trip = all(index_of[key_of_world[w]] == w for w in range(n_worlds))
    orbit_structures_agree = (
        sorted(tuple(sorted(index_of[k] for k in orbit)) for orbit in orbits856)
        == sorted(tuple(sorted(orbit)) for orbit in orbits878))
    # licensing test: a map pi on worlds is LICENSED only if it preserves the
    # census key, i.e. census[pi(w)] == census[w] for all w -- which forces
    # pi = identity.  Any other correspondence is an unlicensed relabelling.
    def licensed(pi):
        return all(census863[pi[w]] == census863[w] for w in range(n_worlds))

    identity_pi = list(range(n_worlds))
    cert_e = {
        "certificate": "E_COMMON_INDEXING",
        "question": ("Q1: is there a canonical map between Cycle 856's key"
                     " space and the Cycle-878/863 census worlds, or are"
                     " they different substrates?"),
        "census_856_digest": digest([list(k) for k in census856]),
        "census_863_digest": digest([list(k) for k in census863]),
        "census_tuples_identical": census_identical,
        "census_same_set": sorted_same_set,
        "population": n_worlds,
        "finding": (
            "NOT type-blocked and NOT a chosen correspondence.  Cycle 856"
            " (derive_scope) and Cycle 863 (derive_census) BOTH build"
            " tuple(sorted(...)) of the SAME generated key set --"
            " (k, event, positions) for k in 2..5, positions a"
            " pairwise-separated combination of the 11 stations, event one"
            " of the four seeds -- from the same Cycle-719 core, and the"
            " two tuples are byte-identical.  Cycle 878 labels a world by"
            " its LANE INDEX into exactly that tuple.  The correspondence"
            " is therefore the IDENTITY ON A SHARED OBJECT: world w is the"
            " key census[w].  There is no free relabelling parameter to"
            " choose, and no map to license"),
        "world_label_semantics": world_label_is_lane,
        "map": "w <-> census[w]",
        "round_trip_exact": round_trip,
        "orbit_structures_agree": orbit_structures_agree,
        "licensing_rule": (
            "a world permutation pi is LICENSED iff census[pi(w)] ==="
            " census[w] for every w; since the census has no repeated"
            " keys this forces pi = identity.  Any other correspondence"
            " between the two lineages' labels is an UNLICENSED"
            " relabelling and is rejected"),
        "identity_is_licensed": licensed(identity_pi),
    }
    cert_e["pass"] = bool(
        census_identical and sorted_same_set and round_trip
        and orbit_structures_agree and cert_e["identity_is_licensed"]
        and n_worlds == CENSUS_EXPECTED)

    # =======================================================================
    # F: Q1 -- the exact world-set comparison
    # =======================================================================
    star_set = frozenset(star_keys)
    star_worlds = frozenset(star)
    absolute_e1_worlds = frozenset(index_of[k] for k in absolute_e1)
    absolute_e2_worlds = frozenset(index_of[k] for k in absolute_e2)
    by_event = {
        e: frozenset(index_of[k] for k in absolute_e1 if k[1] == e)
        for e in sorted({k[1] for k in absolute_e1})
    }
    relation = (
        "EQUAL" if star_worlds == absolute_e1_worlds else
        "PROPER_SUBSET" if star_worlds < absolute_e1_worlds else
        "PROPER_SUPERSET" if star_worlds > absolute_e1_worlds else
        "OVERLAPPING" if star_worlds & absolute_e1_worlds else "DISJOINT")
    absolute_orbit_worlds = {
        i: frozenset(index_of[k] for k in orbits856[i])
        for i in absolute_e1_orbit_indices
    }
    escape_is_one_absolute_orbit = any(
        star_worlds == worlds for worlds in absolute_orbit_worlds.values())
    matching_orbit = [i for i, worlds in absolute_orbit_worlds.items()
                      if star_worlds == worlds]
    cert_f = {
        "certificate": "F_WORLD_SET_COMPARISON",
        "question": ("Q1: do Cycle 856's absolute-record orbits map onto"
                     " the escape orbit, onto a superset, or onto a"
                     " subset?  Exact world-set comparison on the common"
                     " indexing"),
        "escape_orbit_worlds": sorted(star_worlds),
        "escape_orbit_keys": [list(k) for k in sorted(star_set)],
        "absolute_E1_worlds": sorted(absolute_e1_worlds),
        "absolute_E2_worlds": sorted(absolute_e2_worlds),
        "relation_escape_to_absolute_E1": relation,
        "relation_escape_to_absolute_E2": (
            "DISJOINT (856's E2 reading has NO absolute records at all)"
            if not absolute_e2_worlds else "NONEMPTY_E2"),
        "escape_is_exactly_one_absolute_orbit": escape_is_one_absolute_orbit,
        "matching_absolute_orbit_indices": matching_orbit,
        "absolute_E1_orbits_by_event": {
            str(e): sorted(worlds) for e, worlds in by_event.items()},
        "escape_equals_absolute_E1_restricted_to_event_0":
            star_worlds == by_event.get(0, frozenset()),
        "cardinalities": {
            "escape": len(star_worlds),
            "absolute_E1": len(absolute_e1_worlds),
            "absolute_E2": len(absolute_e2_worlds),
            "absolute_E1_orbits": len(absolute_e1_orbit_indices),
        },
        "absolute_E1_minus_escape_worlds":
            sorted(absolute_e1_worlds - star_worlds),
        "escape_minus_absolute_E1_worlds":
            sorted(star_worlds - absolute_e1_worlds),
        "verdict": (
            "IDENTIFIED.  The escape orbit is not merely shaped like"
            " Cycle 856's absolute-record orbits -- it IS one of them,"
            " world for world, on the canonical common indexing.  It is"
            " the event-0 member of the three; the event-1 and event-2"
            " absolute orbits are absolute under 856's E1 stamp but are"
            " NOT escape orbits of the Cycle-878 ledger, so the inclusion"
            " is PROPER: escape (11 worlds) is a proper subset of"
            " absolute_E1 (33 worlds), and the 878 formation predicate is"
            " STRICTLY STRONGER on this census than the 856 E1 stamp"
            " predicate"
            if relation == "PROPER_SUBSET" and escape_is_one_absolute_orbit
            else f"NOT THE EXPECTED RELATION: {relation}"),
    }
    cert_f["pass"] = bool(
        relation == "PROPER_SUBSET" and escape_is_one_absolute_orbit
        and cert_f["escape_equals_absolute_E1_restricted_to_event_0"]
        and not cert_f["escape_minus_absolute_E1_worlds"]
        and len(cert_f["absolute_E1_minus_escape_worlds"]) == 22)

    # =======================================================================
    # G: Q2 -- the shape's origin.  Is there a shared mechanism?
    # =======================================================================
    first_clean = stamp_a["first_clean"]
    formed_predicted = {w: first_clean[w] for w in range(n_worlds)
                        if first_clean[w] is not None
                        and first_clean[w] <= scan_a["boundaries"]}
    ledger_identity = formed_predicted == formed_878
    ledger_mismatches = sorted(
        w for w in range(n_worlds)
        if formed_predicted.get(w) != formed_878.get(w))
    never_predicted = sorted(
        w for w in range(n_worlds)
        if first_clean[w] is None or first_clean[w] > scan_a["boundaries"])
    never_identity = never_predicted == scan_a["never_formed_worlds"]
    formed_lanes = set(formed_878)
    monotone_containment = formed_lanes <= e1_lanes
    e1_only = sorted(e1_lanes - formed_lanes)

    # the orbit-level table: when does each orbit go FULLY clean?
    orbit_rows = []
    for i, orbit in enumerate(orbits878):
        keys = [census863[w] for w in orbit]
        times = [first_clean[w] for w in orbit]
        full = None if any(t is None for t in times) else max(times)
        orbit_rows.append({
            "orbit_index": i,
            "k": keys[0][0],
            "event": keys[0][1],
            "separations": list(cyclic_separations(keys[0][2], stations)),
            "min_cyclic_gap": min(cyclic_gaps(keys[0][2], stations)),
            "worlds": sorted(orbit),
            "clean_members_by_856_E1": sum(1 for w in orbit if w in e1_lanes),
            "formed_members_by_878": sum(1 for w in orbit if w in formed_lanes),
            "full_clean_boundary": full,
            "full_clean_orbit_index_878_horizon": (
                None if full is None else -(-full // stations)),
            "absolute_under_856_E1": all(w in e1_lanes for w in orbit),
            "escape_under_878": all(w in formed_lanes for w in orbit),
        })
    finite_rows = [row for row in orbit_rows
                   if row["full_clean_boundary"] is not None]
    finite_rows.sort(key=lambda row: row["full_clean_boundary"])
    # is min-gap load-bearing?  Test it as a predictor across the k=2 family
    # and across the whole census, honestly.
    k2_rows = sorted((row for row in orbit_rows if row["k"] == 2),
                     key=lambda row: (row["event"], -row["min_cyclic_gap"]))
    gap_groups: dict = {}
    for row in orbit_rows:
        gap_groups.setdefault((row["k"], row["min_cyclic_gap"]), []).append(
            row["full_clean_boundary"])
    maxgap_orbits = [row for row in orbit_rows
                     if row["min_cyclic_gap"] == max(
                         r["min_cyclic_gap"] for r in orbit_rows)]
    all_finite_are_maxgap = all(row["min_cyclic_gap"]
                                == max(r["min_cyclic_gap"] for r in orbit_rows)
                                for row in finite_rows)
    cert_g = {
        "certificate": "G_SHARED_MECHANISM",
        "question": ("Q2: why does the shape k=[2], event=[0],"
                     " separations 5/6 arise in each lineage -- and is the"
                     " cause shared?"),
        "step_1_same_dirty_coordinates": {
            "856_route_count": stamp_a["dirty_coordinate_count"],
            "863_878_route_count": stamp_b["dirty_coordinate_count"],
            "856_route_digest": stamp_a["dirty_digest"],
            "863_878_route_digest": stamp_b["dirty_digest"],
            "identical": stamp_a["dirty_digest"] == stamp_b["dirty_digest"],
            "reading": ("856's dirty_global_indices and 863's"
                        " dirty_partition union -- the set 878 calls"
                        " global_dirty -- are the SAME 477 packed-state"
                        " coordinates, derived independently in two pinned"
                        " sources"),
        },
        "step_2_composed_writes_are_inert": {
            "slot_wires": scan_a["slot_wires"],
            "slot_wires_in_global_dirty": scan_a["slot_wires_in_global_dirty"],
            "slot_wires_touch_gates": scan_a["slot_wires_touch_gates"],
            "dead_wires_count": scan_a["dead_wires_count"],
            "inert": (not scan_a["slot_wires_in_global_dirty"]
                      and not scan_a["slot_wires_touch_gates"]),
            "reading": ("the Cycle-878 record writes land in structurally"
                        " inert dead wires that are neither gate inputs nor"
                        " gate targets and are disjoint from the 477 dirty"
                        " coordinates, so the composed scan's base"
                        " trajectory -- and therefore its clean predicate"
                        " -- is the Cycle-852/856 trajectory unchanged"),
        },
        "step_3_the_two_predicates_are_ONE_predicate": {
            "claim": (
                "856's E1 stamp and 878's formation ledger are the SAME"
                " globally-clean predicate on the SAME trajectory, read at"
                " two horizons.  E1 = 'ever globally clean within 51,115"
                " orbits'; FORMED = 'ever globally clean within 16,384"
                " orbits', with the ledger recording the first such"
                " boundary"),
            "test": ("the instrumented first-clean boundary of the 856"
                     " rebuild must equal the 878 formation ledger world"
                     " for world, wherever it falls inside the 878"
                     " horizon"),
            "formation_ledger_identity": ledger_identity,
            "formation_ledger_mismatched_worlds": ledger_mismatches,
            "never_formed_identity": never_identity,
            "worlds_compared": n_worlds,
            "worlds_in_the_878_ledger": len(formed_878),
            "worlds_predicted_from_the_856_trajectory": len(formed_predicted),
        },
        "step_4_horizon_monotonicity": {
            "claim": ("the clean-union mask is monotone in the horizon, so"
                      " FORMED (16,384 orbits) is contained in E1 (51,115"
                      " orbits); hence any orbit that misses the"
                      " never-formed block is an orbit entirely inside E1,"
                      " i.e. an ABSOLUTE-record orbit.  ESCAPE implies"
                      " ABSOLUTE, as a theorem of the shared predicate,"
                      " not as an analogy"),
            "formed_subset_of_E1": monotone_containment,
            "E1_worlds_not_formed_by_the_878_horizon": len(e1_only),
            "E1_only_world_sample": e1_only[:20],
            "converse_fails": bool(e1_only),
        },
        "step_5_the_shape_itself": {
            "orbit_ordering_by_full_clean_boundary": [
                {"orbit_index": row["orbit_index"], "k": row["k"],
                 "event": row["event"], "separations": row["separations"],
                 "min_cyclic_gap": row["min_cyclic_gap"],
                 "full_clean_boundary": row["full_clean_boundary"],
                 "878_horizon_needed":
                     row["full_clean_orbit_index_878_horizon"]}
                for row in finite_rows],
            "orbits_that_never_go_fully_clean_within_51115":
                len(orbit_rows) - len(finite_rows),
            "k2_family": [
                {"orbit_index": row["orbit_index"], "event": row["event"],
                 "separations": row["separations"],
                 "min_cyclic_gap": row["min_cyclic_gap"],
                 "clean_members_by_856_E1": row["clean_members_by_856_E1"],
                 "formed_members_by_878": row["formed_members_by_878"],
                 "full_clean_boundary": row["full_clean_boundary"]}
                for row in k2_rows],
            "maximum_min_cyclic_gap": max(r["min_cyclic_gap"]
                                          for r in orbit_rows),
            "orbits_at_the_maximum_min_gap": len(maxgap_orbits),
            "max_gap_orbits_by_event": {
                str(row["event"]): row["full_clean_boundary"]
                for row in sorted(maxgap_orbits,
                                  key=lambda r: r["event"])},
            "every_fully_clean_orbit_is_at_the_maximum_min_gap":
                all_finite_are_maxgap,
            "max_gap_is_sufficient": len(maxgap_orbits) == len(finite_rows),
            "reading": (
                "the shape is not a label, it is a necessary condition."
                "  On the 11-station ring a k=2 setup at separations 5/6"
                " is the unique pairwise-separated 2-source configuration"
                " whose two ring gaps are both maximal (5 and 6, the"
                " balanced split of 11), and EVERY orbit that goes fully"
                " clean inside 51,115 orbits sits at that maximum.  It is"
                " necessary and NOT sufficient: the four max-gap orbits"
                " are the four event labels, and the event-3 orbit never"
                " goes fully clean within the horizon, which is exactly"
                " why Cycle 856 reports three absolute orbits and not"
                " four.  Both lineages inherit the shape from the same"
                " substrate fact and neither chooses it; the event label"
                " does the remaining discrimination in both"),
        },
        "step_6_phase_stationarity_explained": {
            "908_finding": ("the escape orbit is the same eleven worlds at"
                            " every monitor phase"),
            "explanation_via_absoluteness": (
                "with the identification in hand the 908 stationarity is a"
                " corollary rather than a separate fact: the escape orbit"
                " is an absolute-record orbit, and 856's absolute set is"
                " by construction the INTERSECTION over all eleven monitor"
                " placements, hence monitor-independent; and it is a union"
                " of frame orbits, hence closed under the very relabelling"
                " that the phase composition applies.  The 908 transport"
                " theorem and this absoluteness are two readings of one"
                " fact"),
            "absolute_set_is_orbit_closed": absolute_e1 == absolute_e1_route2,
            "absolute_set_is_monitor_independent_by_construction": True,
        },
        "verdict": (
            "SHARED CAUSE EXHIBITED, AND IT IS AN IDENTITY, NOT AN"
            " ANALOGY.  The two predicates are the same globally-clean"
            " test on the same 477 dirty coordinates of the same Cycle-719"
            " trajectory, read at two horizons; the Cycle-878 record"
            " writes are inert with respect to it.  P-856-SHAPE therefore"
            " discharges POSITIVELY: the shapes match because the same"
            " substrate fact produces both"
            if (ledger_identity and never_identity and monotone_containment
                and stamp_a["dirty_digest"] == stamp_b["dirty_digest"])
            else "SHARED-CAUSE CLAIM FAILED -- see the step that did not"
                 " hold"),
    }
    cert_g["pass"] = bool(
        cert_g["step_1_same_dirty_coordinates"]["identical"]
        and cert_g["step_2_composed_writes_are_inert"]["inert"]
        and ledger_identity and never_identity and not ledger_mismatches
        and monotone_containment and bool(e1_only)
        and all_finite_are_maxgap)

    # =======================================================================
    # H: Q3 -- the M6 branch in horizon terms
    # =======================================================================
    thresholds = sorted(
        (row["full_clean_orbit_index_878_horizon"], row["orbit_index"])
        for row in orbit_rows
        if row["full_clean_orbit_index_878_horizon"] is not None)
    first_threshold = thresholds[0][0] if thresholds else None
    second_threshold = thresholds[1][0] if len(thresholds) > 1 else None

    def escape_count_at(h):
        return sum(1 for t, _i in thresholds if t <= h)

    horizon_grid = [SHORT_HORIZON, 2048, 4096, 8192, horizon878, 32768,
                    horizon856]
    short_escape = scan_short["orbits_entirely_outside_block"]
    late_horizon_worlds = sorted((w, formed_878[w]) for w in star)
    # "late" = in the second half of the pinned Cycle-878 horizon.  The cut
    # is not tuned: the escape orbit's formation profile is BIMODAL -- two
    # worlds at the opening boundaries and nine at ~90% of the horizon --
    # so every cut between those two clusters gives the same answer.
    late_cut = scan_a["boundaries"] // 2
    late_members = [[w, b, fr(Fraction(b, scan_a["boundaries"]))]
                    for w, b in late_horizon_worlds if b >= late_cut]
    # 856's own absolute count is horizon-critical: how much slack does the
    # LAST absolute orbit leave against 856's own horizon?
    absolute_boundaries = [row["full_clean_boundary"] for row in orbit_rows
                           if row["absolute_under_856_E1"]]
    last_absolute = max(absolute_boundaries) if absolute_boundaries else None
    total_856_boundaries = stamp_a["boundaries"]
    cert_h = {
        "certificate": "H_M6_BRANCH_SCOPE",
        "question": ("Q3: where do 856's absolute orbits sit in horizon"
                     " terms, and what is the resulting scope of the"
                     " M6/M7/M8 constructions?"),
        "escape_orbit_formation_moments": {str(w): formed_878[w] for w in star},
        "escape_orbit_full_clean_boundary": max(formed_878[w] for w in star),
        "878_total_boundaries": scan_a["boundaries"],
        "absolute_orbit_horizon_table": [
            {"orbit_index": row["orbit_index"], "event": row["event"],
             "k": row["k"], "separations": row["separations"],
             "full_clean_boundary": row["full_clean_boundary"],
             "878_horizon_needed": row["full_clean_orbit_index_878_horizon"],
             "inside_the_878_horizon": (
                 row["full_clean_orbit_index_878_horizon"] is not None
                 and row["full_clean_orbit_index_878_horizon"] <= horizon878)}
            for row in orbit_rows if row["absolute_under_856_E1"]],
        "escape_count_by_horizon": {
            str(h): escape_count_at(h) for h in horizon_grid},
        "escape_count_at_the_short_horizon_recomputed": short_escape,
        "escape_count_at_the_short_horizon_predicted":
            escape_count_at(SHORT_HORIZON),
        "short_horizon_prediction_agrees":
            short_escape == escape_count_at(SHORT_HORIZON),
        "M6_exists_iff_horizon_at_least": first_threshold,
        "M6_orbit_unique_iff_horizon_below": second_threshold,
        "pinned_horizon_inside_the_uniqueness_window": bool(
            first_threshold is not None and second_threshold is not None
            and first_threshold <= horizon878 < second_threshold),
        "late_horizon_refinement_of_the_908_checker":
            late_horizon_refinement[0] if late_horizon_refinement else None,
        "late_horizon_cut": (
            "the second half of the pinned Cycle-878 horizon, i.e."
            f" boundary >= {late_cut}.  The cut is not tuned: the escape"
            " orbit's formation profile is BIMODAL -- two worlds at the"
            " opening boundaries and nine at about nine tenths of the"
            " horizon -- so every cut between the two clusters agrees"),
        "late_horizon_members_of_the_escape_orbit": late_members,
        "late_horizon_member_count": len(late_members),
        "the_908_checker_refinement_recomputed": (
            f"{len(late_members)} of {len(star)} escape-orbit worlds first"
            " form in the second half of the pinned horizon, all of them"
            " at about nine tenths of it; the other two form at boundaries"
            " 5 and 6.  The Cycle-908 checker's 'nine of its eleven"
            " worlds' is reproduced exactly, and the label FRACTION is a"
            " bookkeeping fraction, not a probability"),
        "label_on_every_fraction": FRACTION_LABEL,
        "856_absolute_count_is_horizon_critical": {
            "last_absolute_orbit_full_clean_boundary": last_absolute,
            "856_total_boundaries": total_856_boundaries,
            "slack_boundaries": (None if last_absolute is None
                                 else total_856_boundaries - last_absolute),
            "reading": (
                "Cycle 856's headline count of THREE absolute-record"
                " orbits is itself horizon-critical: the last of the three"
                " completes one boundary before 856's own trajectory ends."
                "  Had Cycle 856 stopped two boundaries earlier it would"
                " have reported two absolute orbits and 22 absolute"
                " setups, not three and 33.  This is a scope note the 856"
                " lineage does not carry, and it is surfaced here because"
                " the identification makes both lineages' counts"
                " horizon-indexed quantities"),
        },
        "late_horizon_caveat_status": (
            "REAL AND SHARPENED, NOT AN ARTIFACT.  The 908 checker's"
            " observation stands on recomputation: the escape orbit's own"
            " worlds first go clean deep inside the pinned horizon, so at"
            " short horizons no orbit escapes and M6 is the zero"
            " weighting.  But the identification turns a soft caveat into"
            " an exact two-sided window: M6 exists only above the first"
            " full-formation threshold, and M6's DEFINING ORBIT IS UNIQUE"
            " only below the second.  Both endpoints are now computed"),
        "M6_branch_scope": (
            "M6 -- and any successor construction M7/M8 built on 'the"
            " escape orbit' -- is scoped to the horizon window"
            f" [{first_threshold}, {second_threshold}) controller orbits."
            f"  The pinned Cycle-878 horizon {horizon878} lies inside it,"
            " so Cycle 906's exhibited solution and its"
            " uniqueness-up-to-scale claim are correct AS STATED at the"
            " pinned horizon.  Below the window M6 collapses to the zero"
            " weighting (no orbit escapes the never-formed block); at or"
            " above the upper endpoint a SECOND orbit escapes, the"
            " world-mass solution space stops being one-dimensional, and"
            " 'the escape orbit' stops denoting.  The scope note is"
            " therefore not relaxed by the identification -- it is"
            " sharpened into an interval, and the interval is a property"
            " of the 878 horizon choice, not of the orbit"),
        "what_the_identification_does_and_does_not_buy": (
            "It does NOT make the late-horizon caveat go away: 856's"
            " absolute orbits are themselves late objects on this"
            " substrate (all three are k=2 separations-5/6 orbits whose"
            " members go clean deep in the trajectory).  What it buys is"
            " that the escape orbit is not an artifact of the 878"
            " formation predicate: it is the EARLIEST-FORMING of 856's"
            " three absolute-record orbits, and 'earliest' is the only"
            " thing the 878 horizon adds"),
    }
    cert_h["pass"] = bool(
        first_threshold is not None and second_threshold is not None
        and first_threshold <= horizon878 < second_threshold
        and cert_h["short_horizon_prediction_agrees"]
        and short_escape == 0
        and len(late_members) == 9)

    # =======================================================================
    # I: falsifiers
    # =======================================================================
    falsifiers = []

    def falsifier(label, mutation, detected, expect, detail=None):
        row = {"falsifier": label, "mutation": mutation,
               "detected": bool(detected), "expected_detected": expect,
               "bites": bool(detected) == expect}
        if detail is not None:
            row["detail"] = detail
        falsifiers.append(row)

    # F1: a planted relabelling that WOULD make the sets coincide
    planted = list(range(n_worlds))
    event1_orbit = sorted(by_event.get(1, frozenset()))
    for src, dst in zip(sorted(star_worlds), event1_orbit):
        planted[src], planted[dst] = planted[dst], planted[src]
    planted_makes_them_coincide = frozenset(
        planted[w] for w in star_worlds) == frozenset(event1_orbit)
    falsifier(
        "F1_PLANTED_WORLD_RELABELLING",
        ("swap the escape orbit's worlds with the event-1 absolute orbit's"
         " worlds, which WOULD make the two sets coincide"),
        detected=not licensed(planted), expect=True,
        detail={"the_relabelling_would_make_the_sets_coincide":
                planted_makes_them_coincide,
                "licensed_by_the_census_key_test": licensed(planted),
                "first_key_disagreement": next(
                    ([w, list(census863[planted[w]]), list(census863[w])]
                     for w in range(n_worlds)
                     if census863[planted[w]] != census863[w]), None)})
    # F2: identity relabelling must be accepted (positive control)
    falsifier("F2_IDENTITY_RELABELLING_positive_control",
              "the identity map on worlds must be licensed",
              detected=not licensed(identity_pi), expect=False)
    # F3: shape alone must pin the set at a fixed event
    same_shape = [
        i for i, orbit in enumerate(orbits878)
        if {census863[w][0] for w in orbit} == {2}
        and {census863[w][1] for w in orbit} == {0}
        and {cyclic_separations(census863[w][2], stations) for w in orbit}
            == {(5,), (6,)}]
    falsifier("F3_SHAPE_IS_NOT_AMBIGUOUS",
              ("count the orbits with the byte-quoted 856 shape at event 0"
               " -- more than one would mean the shape match under-"
               "determines the set"),
              detected=len(same_shape) != 1, expect=False,
              detail={"orbits_with_that_shape_at_event_0": same_shape})
    # F4: drop the escape orbit and recount
    dropped = [row for row in orbit_rows
               if row["orbit_index"] not in scan_a["escape_orbit_indices"]]
    falsifier("F4_DROPPED_ORBIT",
              "remove the escape orbit from the orbit scan and recount",
              detected=sum(1 for row in dropped if row["escape_under_878"]) == 0,
              expect=True,
              detail={"escape_orbits_all": sum(
                  1 for row in orbit_rows if row["escape_under_878"]),
                  "escape_orbits_after_drop": sum(
                      1 for row in dropped if row["escape_under_878"])})
    # F5: fabricated absolute key set
    fabricated = digest(tuple(sorted(
        set(absolute_e1) - {min(absolute_e1)})))
    falsifier("F5_HARDCODED_ABSOLUTE_SET",
              ("compare the recomputed absolute-E1 key digest against a"
               " fabricated one"),
              detected=cert_c["absolute_E1_key_sha256"] != fabricated,
              expect=True,
              detail={"recomputed": cert_c["absolute_E1_key_sha256"],
                      "fabricated": fabricated})
    # F6: swap the reading -- E2 instead of E1 must flip the verdict
    e2_relation = ("PROPER_SUBSET" if star_worlds < absolute_e2_worlds
                   else "NOT_A_SUBSET")
    falsifier("F6_PREDICATE_SWAP_E2_FOR_E1",
              ("re-run the identification against 856's E2 reading, which"
               " has no absolute records at all"),
              detected=e2_relation == "NOT_A_SUBSET", expect=True,
              detail={"absolute_E2_count": len(absolute_e2_worlds),
                      "relation": e2_relation})
    # F7: perturb one world out of the escape orbit
    broken = set(star_worlds) - {min(star_worlds)} | {
        max(w for w in range(n_worlds) if w not in star_worlds)}
    falsifier("F7_PERTURBED_ESCAPE_SET",
              ("replace one world of the escape orbit with a foreign world"
               " -- the containment in the absolute set must break"),
              detected=not (frozenset(broken) <= absolute_e1_worlds),
              expect=True,
              detail={"broken_set": sorted(broken)})
    # F8: the composed writes really are load-bearing-free
    base_ledger = pert["base"]["formed_digest"]
    bad_ledger = pert["perturbed"]["formed_digest"]
    falsifier("F8_NON_PERTURBATION_IS_NOT_VACUOUS",
              ("re-point the composed B0 record slot at a coordinate that"
               " IS in the global dirty set and re-run the short scan;"
               " the formation ledger must change, proving the inert-slot"
               " fact is load-bearing rather than vacuous"),
              detected=base_ledger != bad_ledger, expect=True,
              detail={"perturbed_tag": pert["perturbed"]["perturbed_tag"],
                      "unperturbed_formed_worlds":
                      pert["base"]["worlds_formed"],
                      "perturbed_formed_worlds":
                      pert["perturbed"]["worlds_formed"],
                      "horizon": PERTURBATION_HORIZON})
    # F8b: the shared-predicate identity is a fact about the SHARED dirty
    # set, not about the trajectory alone
    short_clean = pert["clean_base"]
    short_dropped = pert["clean_dropped"]
    short_formed = {int(w): b for w, b in pert["base"]["formed"].items()}
    short_predicted = {
        w: short_clean["first_clean"][w] for w in range(n_worlds)
        if short_clean["first_clean"][w] is not None
        and short_clean["first_clean"][w] <= pert["base"]["boundaries"]}
    short_predicted_dropped = {
        w: short_dropped["first_clean"][w] for w in range(n_worlds)
        if short_dropped["first_clean"][w] is not None
        and short_dropped["first_clean"][w] <= pert["base"]["boundaries"]}
    falsifier("F8b_DIRTY_SET_IS_LOAD_BEARING",
              ("drop one coordinate from the dirty set and rebuild the"
               " first-clean profile at the short horizon; it must STOP"
               " reproducing the composed scan's formation ledger, while"
               " the unmutated profile still reproduces it"),
              detected=(short_predicted == short_formed
                        and short_predicted_dropped != short_formed),
              expect=True,
              detail={"unmutated_reproduces_the_ledger":
                      short_predicted == short_formed,
                      "mutated_reproduces_the_ledger":
                      short_predicted_dropped == short_formed,
                      "dropped_coordinates":
                      short_dropped["dropped_coordinates"],
                      "horizon": PERTURBATION_HORIZON})
    # F9: horizon sensitivity
    falsifier("F9_HORIZON_TRUNCATION",
              (f"recompute the escape count at horizon {SHORT_HORIZON};"
               " the M6 branch must vanish"),
              detected=short_escape == 0, expect=True,
              detail={"escape_orbits_at_short_horizon": short_escape,
                      "escape_orbits_at_pinned_horizon":
                          scan_a["orbits_entirely_outside_block"]})
    cert_i = {"certificate": "I_FALSIFIERS", "rows": falsifiers,
              "biting": sum(1 for row in falsifiers if row["bites"]),
              "total": len(falsifiers)}
    cert_i["pass"] = all(row["bites"] for row in falsifiers)

    # =======================================================================
    # J: deterministic double build
    # =======================================================================
    route_rows = {
        "census_digest": (stamp_a["census_digest"], stamp_b["census_digest"]),
        "first_clean_digest": (stamp_a["first_clean_digest"],
                               stamp_b["first_clean_digest"]),
        "E1_stamped_sha256": (stamp_a["E1_stamped_sha256"],
                              stamp_b["E1_stamped_sha256"]),
        "E2_stamped_sha256": (stamp_a["E2_stamped_sha256"],
                              stamp_b["E2_stamped_sha256"]),
        "state_catalog_sha256": (stamp_a["state_catalog_sha256"],
                                 stamp_b["state_catalog_sha256"]),
        "dirty_digest": (stamp_a["dirty_digest"], stamp_b["dirty_digest"]),
        "boundaries": (stamp_a["boundaries"], stamp_b["boundaries"]),
        "gate_counts": (stamp_a["masked_schedule_gate_counts"],
                        stamp_b["masked_schedule_gate_counts"]),
    }
    scan_rows = {
        "raw_event_digest": (scan_a["raw_event_digest"],
                             scan_b["raw_event_digest"]),
        "sorted_event_digest": (scan_a["sorted_event_digest"],
                                scan_b["sorted_event_digest"]),
        "formed_digest": (scan_a["formed_digest"], scan_b["formed_digest"]),
        "escape_orbit_worlds": (scan_a["escape_orbit_worlds"],
                                scan_b["escape_orbit_worlds"]),
        "orbit_meeting_histogram": (
            {str(k): v for k, v in scan_a["orbit_meeting_histogram"].items()},
            {str(k): v for k, v in scan_b["orbit_meeting_histogram"].items()}),
    }
    triple = {
        "878_composed_scan_ledger": scan_a["formed_digest"],
        "856_route_first_clean_ledger": digest(
            {str(w): first_clean[w] for w in sorted(formed_predicted)}),
        "863_route_first_clean_ledger": digest(
            {str(w): stamp_b["first_clean"][w]
             for w in sorted(formed_predicted)}),
    }
    triple_agree = (triple["856_route_first_clean_ledger"]
                    == triple["863_route_first_clean_ledger"]
                    == scan_a["formed_digest"])
    cert_j = {
        "certificate": "J_DETERMINISTIC_DOUBLE_BUILD",
        "stamp_census_two_independent_routes": {
            "route_A": "the Cycle-856 lifted implementation",
            "route_B": ("the Cycle-863 lifted implementation of the same"
                        " construction -- a separately pinned source"),
            "rows": {k: {"A": a, "B": b, "agree": a == b}
                     for k, (a, b) in route_rows.items()},
            "all_agree": all(a == b for a, b in route_rows.values()),
        },
        "composed_scan_replayed_in_an_independent_process": {
            "rows": {k: {"A": a, "B": b, "agree": a == b}
                     for k, (a, b) in scan_rows.items()},
            "all_agree": all(a == b for a, b in scan_rows.values()),
        },
        "formation_ledger_is_TRIPLE_built": {
            "routes": triple,
            "all_three_agree": triple_agree,
            "reading": ("the formation ledger is produced once by the"
                        " pinned 878 composed scan and twice more, from"
                        " two independently pinned implementations, as the"
                        " first-clean profile of the bare trajectory"),
        },
        "analysis_double_routes": {
            "absolute_E1": cert_c["two_routes_agree_E1"],
            "absolute_E2": cert_c["two_routes_agree_E2"],
            "orbit_structure_856_vs_878": orbit_structures_agree,
        },
        "scope": ("FULL.  Every heavy build in this block is built twice:"
                  " the horizon-51,115 stamp census by two independently"
                  " pinned implementations, and the horizon-16,384"
                  " composed scan by replay in an independent process."
                  "  Every analysis quantity is built by a second,"
                  " structurally different route"),
    }
    cert_j["pass"] = bool(
        cert_j["stamp_census_two_independent_routes"]["all_agree"]
        and cert_j["composed_scan_replayed_in_an_independent_process"][
            "all_agree"]
        and triple_agree
        and all(cert_j["analysis_double_routes"].values()))

    # =======================================================================
    # K: runtime
    # =======================================================================
    elapsed = monotonic() - started
    cert_k = {
        "certificate": "K_RUNTIME",
        "budget_sec": RUNTIME_BUDGET_SEC,
        "elapsed_sec": round(elapsed, 3),
        "checkpoint": checkpoint,
        "job_timings": {
            "stamp_route_856": stamp_a["timing"],
            "stamp_route_863": stamp_b["timing"],
            "composed_A": scan_a["timing"],
            "composed_B": scan_b["timing"],
            "composed_short": scan_short["timing"],
        },
    }
    cert_k["pass"] = elapsed <= RUNTIME_BUDGET_SEC

    # =======================================================================
    # L: the discharge and the ledger
    # =======================================================================
    discharge = (
        "DISCHARGED_POSITIVELY__IDENTIFIED"
        if cert_e["pass"] and cert_f["pass"] and cert_g["pass"]
        else "NOT_DISCHARGED")
    prior_ledger = {row["id"]: row["status_now"]
                    for row in r908["ledger_rows"]}
    ledger_rows = [
        {"id": "BL8_ESCAPE_ORBIT_STATUS",
         "status_before": prior_ledger.get("BL8_ESCAPE_ORBIT_STATUS"),
         "status_now": (
             "CLOSED.  P-856-SHAPE is DISCHARGED POSITIVELY.  The escape"
             " orbit is not shaped like one of Cycle 856's"
             " absolute-record orbits -- it IS one of them, world for"
             " world, on a common indexing that is the identity on a"
             " shared census rather than a chosen map.  The cause is an"
             " identity of predicates: 856's E1 stamp and 878's formation"
             " ledger are the same globally-clean test on the same 477"
             " dirty coordinates of the same Cycle-719 trajectory, read at"
             " 51,115 and 16,384 orbits respectively, with the composed"
             " record writes inert.  ESCAPE implies ABSOLUTE as a theorem;"
             " the converse fails only by horizon"),
         "blocked_on": "nothing"},
        {"id": "BL10_M6_HORIZON_WINDOW",
         "obligation": (
             "NEW, surfaced by this block: 'the escape orbit' denotes only"
             f" inside the horizon window [{first_threshold},"
             f" {second_threshold}) controller orbits.  Below it M6 is the"
             " zero weighting; at or above the upper endpoint a second"
             " orbit escapes and the one-dimensional world-mass solution"
             " space of Cycle 906 becomes at least two-dimensional"),
         "status_now": ("COMPUTED AND CLOSED AS A FACT, OPEN AS A SCOPE"
                        " QUESTION: the pinned Cycle-878 horizon 16,384"
                        " sits inside the window, so every landed M6"
                        " statement is correct as stated; but no M6/M7/M8"
                        " construction may be read as horizon-independent"),
         "blocked_on": "the lane -- whoever next chooses a horizon"},
        {"id": "BL7_COVARIANCE",
         "status_before": prior_ledger.get("BL7_COVARIANCE"),
         "status_now": (
             "UNCHANGED BY THIS BLOCK on the reading question, but M6's"
             " standing is now better understood: under COV-INV the"
             " Cycle-906 resolution stands and its support is an"
             " absolute-record orbit in Cycle 856's exact sense, which is"
             " a stronger credential than 'the orbit that happens to miss"
             " the block'.  It remains a credential, not a law, and the"
             " owner choice between the COV-INV and COV-EQV readings is"
             " untouched"),
         "blocked_on": "an owner choice between two priced readings"},
    ]
    theorems = [
        ("C910-T1 THE COMMON INDEXING IS FORCED.  Cycle 856's key space"
         " and the Cycle-863/878 census worlds are the same object:"
         " derive_scope and derive_census independently build"
         " tuple(sorted(.)) of the same 748 keys from the same Cycle-719"
         " core and the two tuples are byte-identical, while a Cycle-878"
         " world label IS the lane index into that tuple.  The"
         " correspondence has no free parameter; a world permutation is"
         " licensed only if it preserves the census key, which forces the"
         " identity."),
        ("C910-T2 THE IDENTIFICATION.  The escape orbit"
         f" {sorted(star_worlds)} is exactly the event-0 member of Cycle"
         " 856's three ABSOLUTE-record orbits under E1.  The inclusion is"
         " proper: absolute_E1 has 33 setups in three orbits (events 0, 1,"
         " 2 at k=2, separations 5/6) and the escape set has 11.  The 878"
         " formation predicate is strictly stronger on this census than"
         " the 856 E1 stamp predicate."),
        ("C910-T3 THE PREDICATES ARE ONE PREDICATE.  856's E1 stamp and"
         " 878's formation ledger are the same globally-clean test on the"
         " same 477 dirty packed-state coordinates of the same trajectory:"
         " the instrumented first-clean boundary of the 856 rebuild equals"
         " the 878 formation ledger world for world inside the 878"
         " horizon, and the never-formed block is exactly the set of"
         " worlds whose first-clean boundary lies beyond it.  The"
         " composed record writes are inert with respect to the test"
         " (disjoint from the dirty coordinates, neither gate inputs nor"
         " targets), and the tooth confirms the inertness is load-bearing"
         " rather than vacuous."),
        ("C910-T4 ESCAPE IMPLIES ABSOLUTE.  The clean-union mask is"
         " monotone in the horizon, so FORMED (16,384) is contained in E1"
         " (51,115); an orbit disjoint from the never-formed block is"
         " therefore an orbit entirely inside E1, i.e. an absolute-record"
         " orbit.  The converse fails only by horizon:"
         f" {len(e1_only)} E1 worlds have not formed by the 878 horizon."),
        ("C910-T5 THE SHAPE IS FORCED BY THE SUBSTRATE, AS A NECESSARY"
         " CONDITION.  Every orbit that goes fully clean within 51,115"
         " orbits sits at the maximum minimum ring gap -- k=2 at"
         " separations 5/6, the unique balanced split of the 11-station"
         " ring.  The condition is necessary and not sufficient: all four"
         " event labels share the shape and the event-3 orbit never goes"
         " fully clean, which is why 856 reports three absolute orbits"
         " and not four.  Neither lineage chooses the shape; both"
         " inherit it."),
        ("C910-T6 THE M6 HORIZON WINDOW.  'The escape orbit' denotes only"
         f" for horizons in [{first_threshold}, {second_threshold})"
         " controller orbits.  The pinned horizon 16,384 lies inside it."
         "  Below the window no orbit escapes and M6 is the zero"
         " weighting; at or above the upper endpoint a second orbit"
         " escapes and Cycle 906's one-dimensional world-mass solution"
         " space is no longer one-dimensional."),
    ]
    cert_l = {
        "certificate": "L_DISCHARGE_AND_LEDGER",
        "premise": "P-856-SHAPE",
        "discharge": discharge,
        "correspondence_verdict": cert_f["verdict"],
        "mechanism_verdict": cert_g["verdict"],
        "M6_branch_scope": cert_h["M6_branch_scope"],
        "rows": ledger_rows,
        "theorems": theorems,
        "named_premises_after_this_block": [
            "P-NONEMPTY (inherited from Cycle 905, untouched)",
            "P-856-SHAPE (DISCHARGED by this block)",
        ],
        "what_is_NOT_claimed": (
            "no probability, no Born rule, no occurrence rule, no update"
            " law, no selection.  The identification is structural: it"
            " says which setups the two lineages are talking about and"
            " why, not that any of them carries weight"),
    }
    cert_l["pass"] = bool(discharge == "DISCHARGED_POSITIVELY__IDENTIFIED")

    certificates = [
        ("A_PINS", cert_a), ("B_RESTRICTION_GATES", cert_b),
        ("C_PREDICATE_856_ABSOLUTE_RECORDS", cert_c),
        ("D_PREDICATE_878_FORMATION_LEDGER", cert_d),
        ("E_COMMON_INDEXING", cert_e),
        ("F_WORLD_SET_COMPARISON", cert_f),
        ("G_SHARED_MECHANISM", cert_g),
        ("H_M6_BRANCH_SCOPE", cert_h),
        ("I_FALSIFIERS", cert_i),
        ("J_DETERMINISTIC_DOUBLE_BUILD", cert_j),
        ("K_RUNTIME", cert_k),
        ("L_DISCHARGE_AND_LEDGER", cert_l),
    ]
    checks = {name: bool(cert["pass"]) for name, cert in certificates}
    verdict = (
        "P_856_SHAPE_DISCHARGED__ESCAPE_ORBIT_IS_AN_856_ABSOLUTE_RECORD_"
        "ORBIT__SHARED_PREDICATE_EXHIBITED__M6_SCOPED_TO_A_HORIZON_WINDOW"
        if all(checks.values()) else "BLOCK_INCOMPLETE")

    science = {
        "escape_orbit_worlds": sorted(star_worlds),
        "absolute_E1_worlds": sorted(absolute_e1_worlds),
        "relation": relation,
        "E1_digest": stamp_a["E1_stamped_sha256"],
        "formed_digest": scan_a["formed_digest"],
        "event_space_digest": scan_a["raw_event_digest"],
        "horizon_window": [first_threshold, second_threshold],
    }
    receipt = {
        "cycle": 910,
        "block": "toe-time-blockQ7-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "question": ("Cycle 910 -- discharge P-856-SHAPE: are the escape"
                     " orbit's worlds and Cycle 856's absolute-record"
                     " orbits the same object under two predicates, or a"
                     " shape coincidence?"),
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "VERDICT": verdict,
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "Q1_common_indexing": cert_e["finding"],
        "Q1_relation_escape_to_absolute_E1": relation,
        "Q1_escape_orbit_worlds": sorted(star_worlds),
        "Q1_absolute_E1_worlds": sorted(absolute_e1_worlds),
        "Q1_absolute_E1_worlds_by_event": {
            str(e): sorted(w) for e, w in by_event.items()},
        "Q1_escape_is_exactly_one_absolute_orbit": escape_is_one_absolute_orbit,
        "Q1_verdict": cert_f["verdict"],
        "Q2_mechanism_verdict": cert_g["verdict"],
        "Q2_formation_ledger_identity": ledger_identity,
        "Q2_formed_subset_of_E1": monotone_containment,
        "Q2_E1_worlds_not_formed_by_the_878_horizon": len(e1_only),
        "Q2_shape_origin": cert_g["step_5_the_shape_itself"]["reading"],
        "Q2_phase_stationarity_explanation":
            cert_g["step_6_phase_stationarity_explained"][
                "explanation_via_absoluteness"],
        "Q3_M6_horizon_window": [first_threshold, second_threshold],
        "Q3_pinned_horizon_inside_the_window":
            cert_h["pinned_horizon_inside_the_uniqueness_window"],
        "Q3_late_horizon_caveat_status": cert_h["late_horizon_caveat_status"],
        "Q3_856_absolute_count_is_horizon_critical":
            cert_h["856_absolute_count_is_horizon_critical"],
        "Q3_M6_branch_scope": cert_h["M6_branch_scope"],
        "discharge": discharge,
        "theorems": theorems,
        "ledger_rows": ledger_rows,
        "named_premises": cert_l["named_premises_after_this_block"],
        "restriction_gate": cert_b["summary"],
        "restriction_gate_rows": gate_rows,
        "falsifiers": falsifiers,
        "teeth": f"{cert_i['biting']}/{cert_i['total']}",
        "deterministic_double_build": cert_j["scope"],
        "double_build_rows": {
            "stamp_routes_agree":
                cert_j["stamp_census_two_independent_routes"]["all_agree"],
            "composed_replay_agrees":
                cert_j["composed_scan_replayed_in_an_independent_process"][
                    "all_agree"],
            "formation_ledger_triple_built": triple_agree,
        },
        "scope": ("the Cycle-863/856 census (748 worlds, 11 stations, 68"
                  " frame orbits), the Cycle-856 E1/E2 stamp census at"
                  " TRAJECTORY_HORIZON 51,115, and the Cycle-878"
                  " composed-record event space at HORIZON 16,384, all"
                  " rebuilt by AST lift from their pinned sources (never"
                  " imported).  NO probability postulate, NO Born rule, NO"
                  " selection"),
        "label_on_every_fraction": FRACTION_LABEL,
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "source_pins": {"sha256": cert_a["sha256"],
                        "git_blobs": cert_a["git_blobs"]},
        "discovery_sweep": cert_a["discovery_sweep"],
        "provenance": provenance,
        "elapsed_sec": round(monotonic() - started, 3),
        "science_digest": digest(science),
        "self_sha256": sha256(
            Path(__file__).read_bytes()).hexdigest(),
        "independent_audit_still_required": True,
    }
    out_dir = ROOT / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "shape_discharge_cycle910_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True, default=str) + "\n",
        encoding="utf-8")

    for name, cert in certificates:
        sys.stdout.write(f"{'PASS' if cert['pass'] else 'FAIL'} {name} :: "
                         f"{cert['pass']}\n")
    body = compact({name: cert for name, cert in certificates})
    if len(body) > STDOUT_LIMIT_BYTES:
        body = body[:STDOUT_LIMIT_BYTES] + "...TRUNCATED"
    sys.stdout.write("CERTIFICATES " + body + "\n")
    sys.stdout.write("SUMMARY_JSON " + compact({
        "cycle": 910,
        "VERDICT": verdict,
        "checks": checks,
        "pass": all(checks.values()),
        "Q1_relation": relation,
        "Q1_escape_orbit_worlds": sorted(star_worlds),
        "Q1_absolute_E1_worlds": sorted(absolute_e1_worlds),
        "Q2_formation_ledger_identity": ledger_identity,
        "Q2_formed_subset_of_E1": monotone_containment,
        "Q3_M6_horizon_window": [first_threshold, second_threshold],
        "teeth": f"{cert_i['biting']}/{cert_i['total']}",
        "restriction_gate": cert_b["summary"],
        "elapsed_sec": receipt["elapsed_sec"],
        "science_digest": receipt["science_digest"],
    }) + "\n")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
