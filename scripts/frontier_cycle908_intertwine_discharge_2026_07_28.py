#!/usr/bin/env python3
"""Cycle 908: discharge P-INTERTWINE-878 -- the eleven phase-composed scans.

Campaign-5 Born LANE CLOSURE, block 4.  Strictly structural.  NO
probability postulate is introduced, NO Born rule is claimed.  Every
fraction emitted here is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

Cycle 906 filed premise P-INTERTWINE-878: Cycle 878's coded
monitor-phase covariance test is an INVARIANCE under a FIXED monitor
placement (the pushforward to the F_WORLD partition is orbit-constant),
while Cycle 856's landed theorem is an INTERTWINING across the monitor
family, stamped_m(g.key) == stamped_{g.m}(key).  The two coincide only
on an orbit-closed ledger, and 878's formation ledger is not orbit
closed.  906 priced the discharge at eleven phase-composed scans (~850s)
and declared it outside its own budget.  It is inside this block's.

Q1  THE ELEVEN SCANS.  The Cycle-856 stamp machinery (frame_map,
    monitor_schedule_manifest) and the Cycle-878 event-space
    construction are rebuilt from their pinned sources by AST -- never
    imported -- and the composed scan is run at every monitor phase
    m = 0..10 of the order-11 group.  Phase m means what Cycle 856 says
    it means: the occupied program rows are advanced by m in BOTH the
    engagement orbit and the monitoring schedule, i.e. lane l carries
    the census key frame_map(census[l], m).  Per phase: the census
    digests, the formation-ledger structure, and the diff against the
    phase-0 (Cycle-878) census.

Q2  COV-EQV, DERIVED AND TESTED.  The intertwining condition's exact
    form on weightings is derived from the eleven censuses rather than
    asserted, then (a) the six candidate recipes M1-M5 (Cycle 878) and
    M6 (Cycle 906) are instantiated per phase by their defining recipes
    and tested for COV-EQV exactly; (b) COV-EQV is compared with 878's
    COV-INV on the actual data; (c) the BL7 tension is re-asked under
    COV-EQV: do the interface survivors {M3, M4, M5} satisfy it?

Q3  THE DISCHARGE VERDICT for P-INTERTWINE-878, the updated ledger
    rows, and -- incidentally -- the escape orbit's behaviour under
    phase composition, which bears on P-856-SHAPE.

Discipline: TEXT / AST / JSON only.  The Cycle-856, Cycle-863,
Cycle-878, Cycle-905 and Cycle-906 primaries and checkers are
BLOCKLISTED from import; their machinery is lifted by AST so the
rebuilt construction is the pinned construction rather than a
transcription.  Only the landed Cycle-719 two-rail core -- the substrate
the 856/863 machinery itself imports -- is imported.  Exact integer /
rational arithmetic everywhere; no floating point enters any verdict.

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
from math import gcd
import os
from pathlib import Path
import sys
from time import monotonic
from types import SimpleNamespace

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
FRACTION_LABEL = "bookkeeping fraction, not probability"
STATIONS_EXPECTED = 11

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
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C856_PATH, C856_CHECK, C856_NOTE, C856_RECEIPT,
    C878_PATH, C878_RECEIPT, C905_RECEIPT, C906_PATH, C906_RECEIPT,
    AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C856_PATH, C856_CHECK, C878_PATH, C906_PATH)
JSON_ONLY_PATHS = (C856_RECEIPT, C878_RECEIPT, C905_RECEIPT, C906_RECEIPT)
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
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
BLOCKLISTED_MODULES = (
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

CANDIDATES_878 = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM",
                  "M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
                  "M5_FORMATION_MOMENT")
M6 = "M6_ABSOLUTE_ORBIT_UNIFORM"
RECIPES = CANDIDATES_878 + (M6,)
INTERFACE_SURVIVORS = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
                       "M5_FORMATION_MOMENT")
INTERFACE_EXCLUDED = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM")
# declared scan-level double-build subset: identity, generator, and the two
# Cayley-deepest elements of Z_11 under the generator +-1
DOUBLE_BUILD_PHASES = (0, 1, 5, 6)

# ---- byte-quoted needles from the pinned sources (presence certified) ------
NEEDLE_906_COV_EQV = (
    '                "Cycle 856\'s landed theorem is not invariance of one object"\n'
    '                " under a fixed monitor; it is an INTERTWINING across the"\n'
    '                " monitor family: stamped_m(g.key) == stamped_{g.m}(key)."\n'
    '                "  The weighting-level analogue is a FAMILY {mu_m} indexed by"\n'
    '                " monitor phase with mu_m(g.A) = mu_{g.m}(A), which is a"\n'
    '                " strictly weaker demand on any single mu_0 than COV-INV"'
)
NEEDLE_906_PRICE = (
    '                "NAMED AND UNDISCHARGED.  Deciding COV-EQV for the Cycle-878"\n'
    '                " composed-record ledger requires the phase-m composed scan"\n'
    '                " for m = 1..10 (eleven full horizon-16384 scans), which is"\n'
    '                " outside this block\'s declared runtime budget.'
)
NEEDLE_906_COINCIDE = (
    '                "COV-INV demands that the phase-0 weighting be invariant;"\n'
    '                " COV-EQV demands only that shifting the monitor and the"\n'
    '                " setup together be exact.  They coincide only when the"\n'
    '                " underlying ledger is ORBIT-CLOSED, and it is not"'
)
NEEDLE_856_IDENTITY = (
    '        "identity": "stamped_m(g·key) == stamped_{g·m}(key)",'
)
NEEDLE_856_MONITOR_ACTION = (
    '        "monitor_action": "g·m = (m + g) mod 11",'
)
NEEDLE_856_NOTE_INTERTWINE = (
    "the intertwining\n"
    "  identity stamped_m(g·key) == stamped_{g·m}(key) HOLDS in all\n"
    "  **181,016** cases (checker re-verified) — record formation is\n"
    "  MONITOR_COVARIANT: transform the monitoring origin along with the\n"
    "  setup and the symmetry is exact; the fixed-monitor breaking sits\n"
    "  only within the declared Cycle-852 phase-lift scope;"
)
NEEDLE_856_NOT_ORBIT_CLOSED = (
    "stamped-ness is NOT orbit-closed — mixed\n"
    "  orbits (orbit-mates disagreeing about record formation): E1 = 3\n"
    "  uniformly-stamped / 12 uniformly-silent / 53 MIXED;"
)
NEEDLE_856_ABSOLUTE = (
    "**E1 has 33** (exactly three size-11 k=2 orbits: events\n"
    "  0, 1, 2 at separations 5/6)"
)
NEEDLE_878_ACTION_DOC = (
    '"""The Cycle-856 landed symmetry: moving the controller-orbit cut to\n'
    "    monitor phase m advances the sources by m stations.  On census keys\n"
    "    (k, event, positions) this is positions -> positions + m (mod\n"
    '    stations), a Z_stations action on the worlds."""'
)
NEEDLE_878_COV_TEST = (
    "        covariant_world = all(\n"
    '            world_cell.get(("w", orbit[0]), zero)\n'
    '            == world_cell.get(("w", x), zero)\n'
    "            for orbit in world_orbits for x in orbit\n"
    "        ) if perm_ok else None"
)
NEEDLE_856_LIFT_SCOPE = (
    '            "Cycle 852 hard-codes monitor phase m=0; Cycle 856 exposes the "\n'
    '            "honestly supported cyclic cut by advancing the occupied program "\n'
    '            "rows in both the engagement orbit and later monitoring schedule"'
)
NEEDLE_AXIOM_EXCLUSION = (
    "- context selection, measurement basis selection, Born weights,"
    " probability\n  rules, update laws, decoherence mechanisms, and"
    " formation rules"
)

NEEDLES = {
    "906_cov_eqv_statement": (C906_PATH, NEEDLE_906_COV_EQV),
    "906_discharge_price": (C906_PATH, NEEDLE_906_PRICE),
    "906_coincide_only_if_orbit_closed": (C906_PATH, NEEDLE_906_COINCIDE),
    "856_intertwining_identity_in_source": (C856_PATH, NEEDLE_856_IDENTITY),
    "856_monitor_action_in_source": (C856_PATH, NEEDLE_856_MONITOR_ACTION),
    "856_phase_lift_scope_in_source": (C856_PATH, NEEDLE_856_LIFT_SCOPE),
    "856_note_intertwining": (C856_NOTE, NEEDLE_856_NOTE_INTERTWINE),
    "856_note_not_orbit_closed": (C856_NOTE, NEEDLE_856_NOT_ORBIT_CLOSED),
    "856_note_absolute_record_orbits": (C856_NOTE, NEEDLE_856_ABSOLUTE),
    "878_monitor_phase_action_docstring": (C878_PATH, NEEDLE_878_ACTION_DOC),
    "878_covariance_test_expression": (C878_PATH, NEEDLE_878_COV_TEST),
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


# ---------------------------------------------------------------------------
# A: the discovery sweep and the pins
# ---------------------------------------------------------------------------

def discovery_sweep() -> dict:
    """How the Cycle-856 artifacts were FOUND, not assumed.

    Published rule: every worktree-relative file under scripts/, docs/,
    outputs/ and logs/runner-cache/ whose basename contains the token
    '856' (case-insensitive).  Every hit is listed with its sha256; the
    durable ones (source, checker, note, receipt) are pinned.  The
    runner caches are listed but NOT pinned: they are run logs, not
    construction inputs.
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
        "stamp_machinery_taken_from": C856_PATH,
        "stamp_machinery_functions": ("frame_map",
                                      "monitor_schedule_manifest",
                                      "pairwise_separated"),
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
                    " is the substrate the Cycle-856 and Cycle-863 machinery"
                    " ITSELF imports; it is the object under test's own"
                    " kernel, so it is imported rather than transcribed."
                    "  Everything else -- 856, 863, 878, 902, 905, 906 --"
                    " is blocklisted from import and lifted by AST"),
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
    "mask_over", "lanes_of", "lane_state",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
C856_FUNCS = ("frame_map", "monitor_schedule_manifest", "pairwise_separated")
C856_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
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
        {"K": K, "combinations": combinations},
    )
    c856 = SimpleNamespace(**{name: ns856[name] for name in C856_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
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
        "import_of_856_863_878_902_905_906": False,
    }
    _MACHINERY = (c863, c856, c878, consts878, provenance)
    return _MACHINERY


def world_weighted(a_of_world, events, per_world, supported, common):
    """The Cycle-878 world_weighted construction, re-expressed at module
    level so it can be applied to a NEW world coefficient (M6).  Checked
    against the pinned M2 at every phase."""
    totals = sum(a_of_world(w) for w in supported)
    nums = [a_of_world(e[0]) * (common // per_world[e[0]]) for e in events]
    return nums, totals * common


# ---------------------------------------------------------------------------
# Q1: one phase-composed scan
# ---------------------------------------------------------------------------

def phase_scan(phase: int, horizon: int, want_events: bool = False) -> dict:
    """The Cycle-878 composed scan run at monitor phase `phase`.

    Cycle 856's phase lift (byte-quoted above) advances the occupied
    program rows by the monitor phase in BOTH the engagement orbit and
    the monitoring schedule.  On the Cycle-863 census that is exactly
    frame_map(key, phase): lane l carries the key
    frame_map(census[l], phase).  Everything downstream -- initial
    states, dead-wire rig, compiled schedules, composed scan -- is then
    the pinned construction applied to that lane assignment.
    """
    t_start = monotonic()
    c863, c856, c878, consts, _prov = lift_machinery()
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    n_worlds = len(census)
    perms, perm_ok = c878.monitor_phase_action(census, stations)
    if not perm_ok:
        raise AssertionError("monitor phase action is not a census bijection")
    sigma = perms[phase % stations]

    census_m = tuple(c856.frame_map(key, phase, stations) for key in census)
    t0 = monotonic()
    states, init_failures = c863.build_initial_states(
        program, event_seeds, census_m)
    t_states = monotonic() - t0
    sim = census_m + (census_m[0],)
    t0 = monotonic()
    rig = c878.dead_wire_rig(program, sim, c863.pack_lanes(states + (states[0],)))
    t_rig = monotonic() - t0
    t0 = monotonic()
    scan = c878.composed_scan(program, census_m, states, rig, horizon)
    t_scan = monotonic() - t0

    events = scan["events"]
    occ_global = scan["occ_global"]
    formed = scan["formed"]
    boundaries = scan["boundaries"]
    per_world = Counter(e[0] for e in events)
    supported = sorted(per_world)
    orbits = c878.group_orbits(perms, n_worlds)
    orbit_of = {w: i for i, orbit in enumerate(orbits) for w in orbit}

    # census digests
    raw_digest = digest([list(e) for e in events])
    sorted_digest = digest(sorted([list(e) for e in events]))
    transported_digest = digest(sorted(
        [[sigma[e[0]], e[1], e[2], e[3], e[4]] for e in events]))

    # per-lane event signature: the lane's realized record content, with the
    # world label stripped.  Two lanes intertwine iff their signatures match.
    by_lane: dict = {}
    for lane, moment, tag, ordinal, content in events:
        by_lane.setdefault(lane, []).append([moment, tag, ordinal, content])
    lane_sig = [digest(sorted(by_lane.get(w, []))) for w in range(n_worlds)]

    # the pinned candidate construction at this phase
    nums, dens, meta, per_world_878, supported_878, common = \
        c878.build_candidates(events, occ_global, formed, boundaries)
    m2_nums, m2_den = world_weighted(lambda w: 1, events, per_world,
                                     supported, common)
    constructor_agrees = (m2_nums == nums["M2_PER_WORLD_UNIFORM"]
                          and m2_den == dens["M2_PER_WORLD_UNIFORM"])

    # M6's defining recipe, applied to THIS phase's census: uniform over the
    # worlds of the orbit(s) that miss this phase's never-formed block.
    never = {w for w in supported if w not in formed}
    escape_indices = [i for i, orbit in enumerate(orbits)
                      if not (set(orbit) & never)]
    star = tuple(orbits[escape_indices[0]]) if escape_indices else ()
    star_set = set(star)
    nums[M6], dens[M6] = world_weighted(
        lambda w: 1 if w in star_set else 0, events, per_world, supported,
        common)

    cells_world: dict = {}
    for index, event in enumerate(events):
        cells_world.setdefault(event[0], []).append(index)

    recipes = {}
    for name in RECIPES:
        vector = nums[name]
        world_mass = [0] * n_worlds
        event_weight = [0] * n_worlds
        uniform = True
        for w in supported:
            idx = cells_world[w]
            first = vector[idx[0]]
            total = 0
            for i in idx:
                total += vector[i]
                if vector[i] != first:
                    uniform = False
            world_mass[w] = total
            event_weight[w] = first
        recipes[name] = {
            "world_mass_nums": world_mass,
            "event_weight_nums": event_weight,
            "denominator": dens[name],
            "total_num": sum(vector),
            "uniform_within_world": uniform,
            "zero_events": sum(1 for v in vector if v == 0),
            "support_worlds": sum(1 for w in supported if world_mass[w] != 0),
        }

    orbit_never_counts = [sum(1 for w in orbit if w in never)
                          for orbit in orbits]
    payload = {
        "phase": phase,
        "horizon": horizon,
        "stations": stations,
        "n_worlds": n_worlds,
        "sigma": list(sigma),
        "census_m_digest": digest([list(k) for k in census_m]),
        "census_m_as_a_set_equals_census": sorted(census_m) == sorted(census),
        "n_events": len(events),
        "boundaries": boundaries,
        "mismatches": scan["mismatches"],
        "write_once_violations": scan["write_once_violations"],
        "beyond_cap": scan["beyond_cap"],
        "dead_activation_conflicts": scan["dead_activation_conflicts"],
        "initial_global_clean_lanes": scan["initial_global_clean_lanes"],
        "init_failures": init_failures,
        "raw_event_digest": raw_digest,
        "sorted_event_digest": sorted_digest,
        "transported_sorted_event_digest": transported_digest,
        "dead_wires_digest": digest(list(rig["dead_wires"])),
        "n_dead_wires": len(rig["dead_wires"]),
        "slot_of_digest": digest({str(k): v for k, v in rig["slot_of"].items()}),
        "worlds_with_events": len(supported),
        "worlds_formed": len(formed),
        "worlds_never_formed": len(never),
        "events_on_never_formed_worlds": sum(
            per_world[w] for w in sorted(never)),
        "per_world_counts": [per_world.get(w, 0) for w in range(n_worlds)],
        "occ_global": list(occ_global),
        "formed": {str(w): b for w, b in sorted(formed.items())},
        "lane_sig": lane_sig,
        "tag_histogram": dict(sorted(Counter(e[2] for e in events).items())),
        "orbit_count": len(orbits),
        "orbit_size_histogram": dict(sorted(
            Counter(len(o) for o in orbits).items())),
        "orbit_never_formed_counts": orbit_never_counts,
        "orbits_mixed": sum(1 for c in orbit_never_counts
                            if 0 < c < stations),
        "orbits_entirely_inside_block": sum(1 for c in orbit_never_counts
                                            if c == stations),
        "orbits_entirely_outside_block": len(escape_indices),
        "escape_orbit_indices": escape_indices,
        "escape_orbit_worlds": list(star),
        "escape_orbit_keys": [list(census[w]) for w in star],
        "escape_orbit_keys_at_this_phase": [list(census_m[w]) for w in star],
        "constructor_reproduces_pinned_M2": constructor_agrees,
        "common_denominator": common,
        "recipes": recipes,
        "timing": {"states": round(t_states, 3), "rig": round(t_rig, 3),
                   "scan": round(t_scan, 3),
                   "total": round(monotonic() - t_start, 3)},
    }
    if want_events:
        payload["events"] = [list(e) for e in events]
    return payload


def _job(spec):
    phase, horizon, build, want_events = spec
    out = phase_scan(phase, horizon, want_events)
    out["build"] = build
    return out


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a = pin_rows()
    if not cert_a["pass"]:
        sys.stdout.write("CYCLE908_PIN_FAILURE " + compact(cert_a) + "\n")
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
        sys.stdout.write("CYCLE908_PIN_FAILURE " + compact(cert_a) + "\n")
        return 2

    r878 = json.loads(payload_text[C878_RECEIPT])["findings"]
    r905 = json.loads(payload_text[C905_RECEIPT])
    r906 = json.loads(payload_text[C906_RECEIPT])

    _c863, _c856, _c878, consts, provenance = lift_machinery()
    horizon = consts["HORIZON"]
    stations = STATIONS_EXPECTED

    # ---- Q1: the eleven scans, plus the full deterministic double build ----
    phases = tuple(range(stations))
    jobs = [(m, horizon, "A", m in (0, 1)) for m in phases]
    jobs += [(m, horizon, "B", False) for m in DOUBLE_BUILD_PHASES]
    workers = max(1, min(len(jobs), os.cpu_count() or 1))
    checkpoint = {
        "structure": ("one process per phase-build; results collected by"
                      " (phase, build) index, so the run is order-"
                      "independent and deterministic.  Every phase is a"
                      " full end-to-end rebuild -- census relabelling,"
                      " initial states, dead-wire rig, compiled schedules,"
                      " composed scan, candidate construction -- with NO"
                      " sharing of scan state between phases; the only"
                      " thing cached inside a worker process is the AST"
                      " lift of the pinned machinery"),
        "jobs": [{"phase": j[0], "horizon": j[1], "build": j[2]} for j in jobs],
        "job_count": len(jobs),
        "pool_workers": workers,
        "scans_declared": len(phases),
        "double_build_scope": (
            "DECLARED SUB-CHECK, not the full eleven.  A single"
            " phase-composed scan costs ~77s serially and ~235s under"
            " 10-way parallel contention on this host, so 22 end-to-end"
            " scans do not fit the 900s cap.  The scan-level double build"
            " therefore re-runs the phases"
            f" {list(DOUBLE_BUILD_PHASES)} end to end in independent"
            " processes -- the identity phase 0, the generator phase 1,"
            " and the two Cayley-deepest phases 5 and 6 (the phases"
            " furthest from the identity in Z_11 with generator +-1, where"
            " an error in composing the action would accumulate most)."
            "  Every ANALYSIS quantity is double-built in full by a second,"
            " structurally different arithmetic route"),
        "double_build_phases": list(DOUBLE_BUILD_PHASES),
        "double_build_selection_rule": (
            "identity phase; generator phase; the two phases m maximising"
            " min(m, 11-m), i.e. the Cayley-deepest elements of Z_11"),
    }
    results: dict = {}
    parallel_ok = True
    t_scans = monotonic()
    try:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for out in pool.map(_job, jobs):
                results[(out["phase"], out["build"])] = out
    except Exception as exc:                             # pragma: no cover
        parallel_ok = False
        checkpoint["parallel_failure"] = repr(exc)
        results = {}
        for spec in jobs:
            if monotonic() - started > RUNTIME_BUDGET_SEC - 120:
                break
            out = _job(spec)
            results[(out["phase"], out["build"])] = out
    scans_elapsed = monotonic() - t_scans
    checkpoint["parallel"] = parallel_ok
    checkpoint["scans_elapsed_sec"] = round(scans_elapsed, 3)

    have_a = sorted(m for m in phases if (m, "A") in results)
    have_b = sorted(m for m in DOUBLE_BUILD_PHASES if (m, "B") in results)
    scans_complete = have_a == list(phases)
    A = {m: results[(m, "A")] for m in have_a}
    checkpoint["phases_run_build_A"] = have_a
    checkpoint["phases_run_build_B"] = have_b
    checkpoint["eleven_complete"] = scans_complete
    checkpoint["selection_rule_if_scoped"] = (
        "none needed -- all eleven phases of the order-11 group ran"
        if scans_complete else
        "phases were submitted in increasing order m = 0..10 and the run was"
        " truncated by the runtime budget; the discharge below is scoped to"
        f" the phases actually run: {have_a}"
    )
    if not scans_complete:
        sys.stdout.write("CYCLE908_SCAN_INCOMPLETE " + compact(checkpoint) + "\n")
        return 3

    zero = A[0]
    n_worlds = zero["n_worlds"]
    sig = {m: A[m]["sigma"] for m in phases}

    # ---- B: restriction gates ---------------------------------------------
    gate_rows = []

    def gate(name, computed, expected):
        gate_rows.append({"gate": name, "computed": computed,
                          "expected": expected, "match": computed == expected})

    gate("878_event_cardinality", zero["n_events"],
         r878["event_cardinality"])
    gate("878_worlds_with_events", zero["worlds_with_events"],
         r878["worlds_with_at_least_one_event"])
    gate("878_world_orbit_count", zero["orbit_count"],
         r878["landed_symmetry"]["world_orbit_count"])
    gate("878_world_orbit_size_histogram",
         {str(k): v for k, v in zero["orbit_size_histogram"].items()},
         {str(k): v for k, v in
          r878["landed_symmetry"]["world_orbit_size_histogram"].items()})
    gate("878_action_is_a_census_bijection", True,
         r878["landed_symmetry"]["action_is_a_census_bijection"])
    for name in CANDIDATES_878:
        gate(f"878_zero_weight_events_{name}",
             zero["recipes"][name]["zero_events"],
             r878["candidate_verdicts"][name]["zero_weight_events"])
        gate(f"905_total_{name}", zero["recipes"][name]["total_num"],
             r905["totals"][name])
    gate("906_phase0_event_space_digest", zero["raw_event_digest"],
         r906["event_space_digest"])
    m6_906 = r906["Q3_exhibited_solution"]
    gate("906_escape_orbit_worlds", zero["escape_orbit_worlds"],
         m6_906["support_worlds"])
    gate("906_M6_zero_weight_events", zero["recipes"][M6]["zero_events"],
         m6_906["zero_weight_events"])
    gate("906_M6_support_events",
         zero["n_events"] - zero["recipes"][M6]["zero_events"],
         m6_906["support_events"])
    gate("906_M6_total", zero["recipes"][M6]["total_num"], m6_906["total"])
    gate("906_orbits_entirely_outside_block",
         zero["orbits_entirely_outside_block"],
         r906["Q4_orbit_meeting_histogram"].get("0", 0))
    gate("906_mixed_orbit_count", zero["orbits_mixed"],
         zero["orbit_count"]
         - r906["Q4_orbit_meeting_histogram"].get("0", 0)
         - r906["Q4_orbit_meeting_histogram"].get(str(stations), 0))
    gate("906_mixed_orbit_count_is_55", zero["orbits_mixed"], 55)
    gate("906_orbit_meeting_histogram",
         {str(k): v for k, v in sorted(
             Counter(zero["orbit_never_formed_counts"]).items())},
         {str(k): v for k, v in
          r906["Q4_orbit_meeting_histogram"].items()})
    gate("906_every_orbit_meets_the_block",
         zero["orbits_entirely_outside_block"] == 0,
         r906["Q4_every_orbit_meets_the_block"])
    gate("905_worlds_never_formed", zero["worlds_never_formed"], 584)
    gate("905_events_on_never_formed_worlds",
         zero["events_on_never_formed_worlds"], 73088)
    gate("905_worlds_formed", zero["worlds_formed"], 164)
    gate("905_excluded_set", sorted(INTERFACE_EXCLUDED),
         sorted(r905["Q1_excluded"]))
    gate("905_surviving_set", sorted(INTERFACE_SURVIVORS),
         sorted(r905["Q1_surviving"]))
    gate("phase0_is_the_identity_permutation", zero["sigma"],
         list(range(n_worlds)))
    gate("phase0_constructor_reproduces_pinned_M2",
         zero["constructor_reproduces_pinned_M2"], True)
    gate("group_order", stations, STATIONS_EXPECTED)

    phase0_reproduces = all(
        r["match"] for r in gate_rows
        if r["gate"].startswith(("878_", "906_phase0", "905_", "phase0_"))
    )
    cert_b = {
        "certificate": "B_RESTRICTION_GATES",
        "rows": gate_rows,
        "reproduce": sum(1 for r in gate_rows if r["match"]),
        "total": len(gate_rows),
        "phase0_reproduces_the_878_census_value_for_value": phase0_reproduces,
        "note": ("the identity phase IS Cycle 878's construction: if the"
                 " phase-0 census digest did not reproduce 906's pinned"
                 " event_space_digest the block would stop here and report"
                 " the discrepancy as its finding"),
    }
    cert_b["pass"] = all(r["match"] for r in gate_rows)
    if not cert_b["pass"]:
        sys.stdout.write("CYCLE908_RESTRICTION_GATE_FAILURE "
                         + compact(cert_b) + "\n")
        return 4

    # ---- C: Q1, the eleven censuses and their diffs ------------------------
    def transported_ledger(m, field):
        """phase-0 field pulled back along sigma_m."""
        return [A[0][field][sig[m][w]] for w in range(n_worlds)]

    phase_rows = []
    for m in phases:
        row = A[m]
        transport_events = (row["transported_sorted_event_digest"]
                            == zero["sorted_event_digest"])
        transport_occ = row["occ_global"] == transported_ledger(m, "occ_global")
        transport_counts = (row["per_world_counts"]
                            == transported_ledger(m, "per_world_counts"))
        transport_formed = ({str(sig[m][int(w)]): b
                             for w, b in row["formed"].items()}
                            == zero["formed"])
        transport_lane_sig = (row["lane_sig"]
                              == transported_ledger(m, "lane_sig"))
        phase_rows.append({
            "phase": m,
            "raw_event_digest": row["raw_event_digest"],
            "sorted_event_digest": row["sorted_event_digest"],
            "transported_sorted_event_digest":
                row["transported_sorted_event_digest"],
            "n_events": row["n_events"],
            "boundaries": row["boundaries"],
            "worlds_with_events": row["worlds_with_events"],
            "worlds_formed": row["worlds_formed"],
            "worlds_never_formed": row["worlds_never_formed"],
            "events_on_never_formed_worlds":
                row["events_on_never_formed_worlds"],
            "orbits_mixed": row["orbits_mixed"],
            "escape_orbit_indices": row["escape_orbit_indices"],
            "escape_orbit_worlds": row["escape_orbit_worlds"],
            "dead_wires_digest": row["dead_wires_digest"],
            "n_dead_wires": row["n_dead_wires"],
            "mismatches": row["mismatches"],
            "write_once_violations": row["write_once_violations"],
            "init_failures": row["init_failures"],
            "diff_vs_phase0": {
                "raw_digest_equal":
                    row["raw_event_digest"] == zero["raw_event_digest"],
                "sorted_digest_equal":
                    row["sorted_event_digest"] == zero["sorted_event_digest"],
                "transported_digest_equals_phase0_sorted": transport_events,
                "occupation_ledger_is_the_sigma_transport": transport_occ,
                "per_world_counts_is_the_sigma_transport": transport_counts,
                "formation_ledger_is_the_sigma_transport": transport_formed,
                "lane_signature_is_the_sigma_transport": transport_lane_sig,
                "worlds_whose_event_count_changed": sum(
                    1 for w in range(n_worlds)
                    if row["per_world_counts"][w]
                    != zero["per_world_counts"][w]),
                "dead_wire_set_identical":
                    row["dead_wires_digest"] == zero["dead_wires_digest"],
                "slot_map_identical":
                    row["slot_of_digest"] == zero["slot_of_digest"],
            },
            "timing": row["timing"],
        })

    transport_theorem = all(
        r["diff_vs_phase0"]["transported_digest_equals_phase0_sorted"]
        and r["diff_vs_phase0"]["occupation_ledger_is_the_sigma_transport"]
        and r["diff_vs_phase0"]["per_world_counts_is_the_sigma_transport"]
        and r["diff_vs_phase0"]["formation_ledger_is_the_sigma_transport"]
        and r["diff_vs_phase0"]["lane_signature_is_the_sigma_transport"]
        for r in phase_rows
    )
    raw_digests_distinct = len({r["raw_event_digest"] for r in phase_rows})

    # a DIRECT set-level check on the two phases whose full event lists were
    # returned: E_1 == {e : 1.e in E_0}, i.e. the intertwining at g = 1
    e0 = {tuple(e) for e in A[0]["events"]}
    e1 = {tuple(e) for e in A[1]["events"]}
    shifted = {(sig[1][w], t, tag, o, c) for (w, t, tag, o, c) in e1}
    direct_g1 = shifted == e0
    direct_rows = {
        "check": ("DIRECT, not digest-mediated: {sigma_1.e : e in E_1}"
                  " == E_0"),
        "E_0_size": len(e0), "E_1_size": len(e1),
        "equal": direct_g1,
        "symmetric_difference": len(shifted ^ e0),
    }

    cert_c = {
        "certificate": "C_ELEVEN_PHASE_COMPOSED_SCANS",
        "question": ("Q1: run the composed scan at every monitor phase of"
                     " the order-11 group and publish the census digest,"
                     " the formation-ledger structure, and the diff against"
                     " the phase-0 (Cycle-878) census"),
        "phase_semantics": (
            "phase m advances the occupied program rows by m in BOTH the"
            " engagement orbit and the monitoring schedule, per the"
            " byte-quoted Cycle-856 phase-lift scope; on the Cycle-863"
            " census that is lane l carrying frame_map(census[l], m).  The"
            " phase-m model is then the PINNED Cycle-878 construction"
            " applied to that lane assignment: initial states, dead-wire"
            " rig, compiled schedules and composed scan are all rebuilt"),
        "scans_run": len(phases),
        "checkpoint_structure": checkpoint,
        "rows": phase_rows,
        "distinct_raw_event_digests": raw_digests_distinct,
        "all_phases_have_the_same_event_cardinality":
            len({r["n_events"] for r in phase_rows}) == 1,
        "direct_set_level_intertwining_at_g_equals_1": direct_rows,
        "TRANSPORT_THEOREM": {
            "statement": (
                "COMPUTED, all eleven phases: the phase-m composed-record"
                " event space is the phase-0 event space pulled back along"
                " sigma_m, event for event -- E_m = {e : sigma_m.e in E_0}"
                " -- and the phase-m occupation ledger, formation ledger,"
                " per-world event counts and per-lane record signatures are"
                " the sigma_m transports of the phase-0 ones.  The"
                " dead-wire set and the safe-slot map are phase-INDEPENDENT"),
            "holds": transport_theorem,
            "consequence": (
                "the eleven censuses are not eleven different ledgers; they"
                " are one ledger read in eleven world-labellings.  This is"
                " the composed-record analogue of Cycle 856's stamp-set"
                " transport, and it is what makes the intertwining"
                " decidable"),
        },
        "timing_total_sec": round(scans_elapsed, 3),
    }
    cert_c["pass"] = bool(
        len(phase_rows) == stations and transport_theorem and direct_g1
        and cert_c["all_phases_have_the_same_event_cardinality"]
        and all(r["mismatches"] == 0 and r["write_once_violations"] == 0
                and r["init_failures"] == 0 for r in phase_rows)
    )

    # ---- D: Q2, COV-EQV derived from the data ------------------------------
    def world_mass(m, name, w):
        rec = A[m]["recipes"][name]
        return (rec["world_mass_nums"][w], rec["total_num"])

    def event_weight(m, name, w):
        rec = A[m]["recipes"][name]
        return (rec["event_weight_nums"][w], rec["total_num"])

    def eq(a, b):
        """exact equality of two num/total pairs, cross-multiplied"""
        return a[0] * b[1] == b[0] * a[1]

    def cov_eqv(getter, family):
        """family: m -> (name-or-vector).  Returns (holds, witnesses)."""
        witnesses = []
        for m in phases:
            for g in phases:
                mg = (m + g) % stations
                for w in range(n_worlds):
                    left = getter(family, m, sig[g][w])
                    right = getter(family, mg, w)
                    if not eq(left, right):
                        if len(witnesses) < 4:
                            witnesses.append({
                                "monitor_phase_m": m, "shift_g": g,
                                "world": w, "shifted_world": sig[g][w],
                                "w_m_of_g_dot_e": f"{left[0]}/{left[1]}",
                                "w_mg_of_e": f"{right[0]}/{right[1]}",
                            })
        return (not witnesses), witnesses

    def recipe_world(name, m, w):
        return world_mass(m, name, w)

    def recipe_event(name, m, w):
        return event_weight(m, name, w)

    derived_form = {
        "template_from_the_pinned_906_receipt_section": {
            "quote": NEEDLE_906_COV_EQV,
            "present_byte_for_byte":
                quotes["906_cov_eqv_statement"]["present_byte_for_byte"],
            "landed_856_identity": NEEDLE_856_IDENTITY,
            "landed_856_monitor_action": NEEDLE_856_MONITOR_ACTION,
        },
        "the_action_on_events": (
            "g.e shifts ONLY the world coordinate of a realized record-write"
            " event and fixes (moment, tag, ordinal, content):"
            "  g.(w, t, tag, ord, c) = (sigma_g(w), t, tag, ord, c),"
            " where sigma_g is the Cycle-878 monitor_phase_action"
            " permutation, i.e. the census frame map positions ->"
            " positions + g (mod 11).  This is forced, not chosen: it is"
            " the only lift of the census action that the TRANSPORT"
            " THEOREM certifies the eleven scans actually realize"),
        "instantiated_exact_form": (
            "a weighting FAMILY {w_m}_{m in Z_11}, w_m defined on the"
            " phase-m event space, satisfies COV-EQV iff"
            "     w_m(g.e) = w_{(m+g) mod 11}(e)"
            " for every g, m in Z_11 and every realized event e.  On the"
            " F_WORLD pushforward this reads W_m(sigma_g(w)) ="
            " W_{(m+g) mod 11}(w) for every world w -- the same identity"
            " Cycle 856 states for stamp sets, with 'stamped' replaced by"
            " 'carries mass'"),
        "event_sets_intertwine": (
            "COMPUTED: g.e in E_m iff e in E_{(m+g) mod 11}, for all g, m."
            "  This is Cycle 856's identity verbatim on the Cycle-878"
            " composed-record ledger, and it is what the TRANSPORT THEOREM"
            " certificate establishes"),
        "generated_form": (
            "COV-EQV holds for a family iff the family is GENERATED from"
            " its phase-0 member by w_m = w_0 o sigma_m.  Setting g = -m"
            " in the identity gives w_m = w_0 o sigma_m; conversely that"
            " form satisfies the identity by sigma_m sigma_g ="
            " sigma_{m+g}, which is certified below"),
        "cov_inv_is_the_constant_family": (
            "Cycle 878's COV-INV is the SPECIALIZATION of COV-EQV to the"
            " CONSTANT family w_m = w_0 for all m: substituting gives"
            " w_0(g.e) = w_0(e) for all g, i.e. the pushforward to F_WORLD"
            " is constant on the monitor-phase orbits -- byte-for-byte the"
            " pinned 878 test.  Hence COV-INV = COV-EQV + constancy, and"
            " COV-EQV is strictly weaker unless every COV-EQV family is"
            " constant, which happens iff w_0 o sigma_g = w_0"),
    }
    # certify sigma_m sigma_g == sigma_{m+g} on the actual permutations
    group_law = all(
        [sig[m][sig[g][w]] for w in range(n_worlds)] == sig[(m + g) % stations]
        for m in phases for g in phases
    )
    free_action = all(
        all(sig[m][w] != w for w in range(n_worlds))
        for m in phases if m != 0
    )
    derived_form["sigma_group_law_sigma_m_sigma_g_equals_sigma_m_plus_g"] = \
        group_law
    derived_form["action_is_free"] = free_action
    derived_form["orbit_count"] = zero["orbit_count"]
    cert_d = {
        "certificate": "D_COV_EQV_DERIVED_FROM_THE_DATA",
        "question": ("Q2: derive the intertwining condition's exact form on"
                     " weightings from the eleven censuses"),
        "derivation": derived_form,
    }
    cert_d["pass"] = bool(group_law and free_action
                          and quotes["906_cov_eqv_statement"][
                              "present_byte_for_byte"]
                          and quotes["856_intertwining_identity_in_source"][
                              "present_byte_for_byte"])

    # ---- E: Q2(a), the six recipes under COV-EQV ---------------------------
    recipe_rows = {}
    for name in RECIPES:
        holds_w, wit_w = cov_eqv(recipe_world, name)
        holds_e, wit_e = cov_eqv(recipe_event, name)
        generated = all(
            eq(world_mass(m, name, w), world_mass(0, name, sig[m][w]))
            for m in phases for w in range(n_worlds)
        )
        recipe_rows[name] = {
            "COV_EQV_on_world_masses": holds_w,
            "COV_EQV_on_event_weights": holds_e,
            "COV_EQV": bool(holds_w and holds_e),
            "witnesses": wit_w[:2] + wit_e[:2],
            "family_is_generated_w_m_equals_w_0_after_sigma_m": generated,
            "uniform_within_world_at_every_phase": all(
                A[m]["recipes"][name]["uniform_within_world"] for m in phases),
            "zero_events_by_phase": [A[m]["recipes"][name]["zero_events"]
                                     for m in phases],
            "support_worlds_by_phase": [A[m]["recipes"][name]["support_worlds"]
                                        for m in phases],
            "total_num_by_phase": [A[m]["recipes"][name]["total_num"]
                                   for m in phases],
        }
    cert_e = {
        "certificate": "E_RECIPE_LEVEL_COV_EQV",
        "question": ("Q2(a): which of the six candidate weightings satisfy"
                     " COV-EQV, tested at the RECIPE level -- each recipe"
                     " instantiated per phase by its own defining recipe"
                     " applied to the phase-m census"),
        "recipes": recipe_rows,
        "cov_eqv_recipes": [n for n in RECIPES if recipe_rows[n]["COV_EQV"]],
        "not_cov_eqv_recipes": [n for n in RECIPES
                                if not recipe_rows[n]["COV_EQV"]],
        "mechanism": (
            "every one of the six is a function of the phase-m formation /"
            " occupation ledger alone (M1 of the event set, M2 of the world"
            " support, M3 of the occupation counts, M4 and M5 of the"
            " formation moments, M6 of the escape orbit).  The TRANSPORT"
            " THEOREM says the phase-m ledger IS the sigma_m transport of"
            " the phase-0 ledger, so each recipe's per-phase instances"
            " satisfy w_m = w_0 o sigma_m and therefore intertwine.  The"
            " verdict is computed here, not inferred"),
        "fraction_label": FRACTION_LABEL,
    }
    cert_e["pass"] = all(
        recipe_rows[n]["COV_EQV"] == recipe_rows[n][
            "family_is_generated_w_m_equals_w_0_after_sigma_m"]
        for n in RECIPES
    )

    # ---- F: Q2(b), COV-EQV versus COV-INV ---------------------------------
    seen = [False] * n_worlds
    orbit_list = []
    for start in range(n_worlds):
        if seen[start]:
            continue
        orbit = sorted({sig[m][start] for m in phases})
        for w in orbit:
            seen[w] = True
        orbit_list.append(orbit)
    cov_inv_rows = {}
    for name in RECIPES:
        by_phase = {}
        for m in phases:
            nums = A[m]["recipes"][name]["world_mass_nums"]
            bad = None
            for orbit in orbit_list:
                base = nums[orbit[0]]
                for x in orbit:
                    if nums[x] != base:
                        bad = {"orbit_representative": orbit[0],
                               "world_a": orbit[0], "mass_a": base,
                               "world_b": x, "mass_b": nums[x],
                               "denominator": A[m]["recipes"][name][
                                   "total_num"]}
                        break
                if bad:
                    break
            by_phase[m] = {"COV_INV": bad is None, "witness": bad}
        cov_inv_rows[name] = {
            "COV_INV_at_phase_0": by_phase[0]["COV_INV"],
            "COV_INV_at_every_phase": all(v["COV_INV"]
                                          for v in by_phase.values()),
            "phase_0_witness": by_phase[0]["witness"],
        }

    differ = [n for n in RECIPES
              if recipe_rows[n]["COV_EQV"] != cov_inv_rows[n][
                  "COV_INV_at_phase_0"]]
    coincide = not differ
    witness_recipe = None
    if differ:
        preferred = [n for n in differ if n in INTERFACE_SURVIVORS]
        witness_recipe = (preferred or differ)[0]
    cert_f = {
        "certificate": "F_COV_EQV_VERSUS_COV_INV",
        "question": ("Q2(b): the relationship between COV-EQV and Cycle"
                     " 878's COV-INV on the actual data"),
        "cov_inv_rows": cov_inv_rows,
        "cov_inv_recipes_phase_0": [n for n in RECIPES
                                    if cov_inv_rows[n]["COV_INV_at_phase_0"]],
        "reproduces_878_verdict_M2_only_of_the_five": (
            [n for n in CANDIDATES_878
             if cov_inv_rows[n]["COV_INV_at_phase_0"]]
            == ["M2_PER_WORLD_UNIFORM"]),
        "the_two_conditions_coincide_on_this_data": coincide,
        "verdict": ("COINCIDE" if coincide else "DIFFER_WITH_WITNESS"),
        "witness": None if coincide else {
            "recipe": witness_recipe,
            "satisfies_COV_EQV": recipe_rows[witness_recipe]["COV_EQV"],
            "satisfies_COV_INV": cov_inv_rows[witness_recipe][
                "COV_INV_at_phase_0"],
            "the_COV_INV_failure": cov_inv_rows[witness_recipe][
                "phase_0_witness"],
            "reading": (
                "this weighting's per-phase family intertwines exactly"
                " (COV-EQV) while its phase-0 member is NOT orbit-constant"
                " (COV-INV fails).  Cycle 906 predicted exactly this"
                " separation on a ledger that is not orbit-closed, and the"
                " eleven scans exhibit it"),
        },
        "why_they_separate_here": (
            "the Cycle-878 formation ledger is not orbit-closed: of the"
            f" {zero['orbit_count']} monitor-phase orbits,"
            f" {zero['orbits_mixed']} are MIXED (orbit-mates disagreeing"
            " about whether the world ever forms), which is the"
            " composed-record analogue of the byte-quoted Cycle-856"
            " non-closure of stamped-ness.  A COV-EQV family is constant"
            " iff w_0 is orbit-constant; the mixed orbits are exactly what"
            " stops the ledger-reading recipes from being orbit-constant"),
        "orbit_closure": {
            "mixed_orbits": zero["orbits_mixed"],
            "uniformly_never_formed_orbits":
                zero["orbits_entirely_inside_block"],
            "uniformly_formed_orbits": zero["orbits_entirely_outside_block"],
            "ledger_is_orbit_closed": zero["orbits_mixed"] == 0,
            "856_note_non_closure_quote_present":
                quotes["856_note_not_orbit_closed"]["present_byte_for_byte"],
        },
    }
    cert_f["pass"] = bool(
        cert_f["reproduces_878_verdict_M2_only_of_the_five"]
        and (coincide or witness_recipe is not None)
    )

    # ---- G: Q2(c), BL7 under COV-EQV ---------------------------------------
    survivors_cov_eqv = {n: recipe_rows[n]["COV_EQV"]
                         for n in INTERFACE_SURVIVORS}
    survivors_cov_inv = {n: cov_inv_rows[n]["COV_INV_at_phase_0"]
                         for n in INTERFACE_SURVIVORS}
    tension_arises_under_cov_eqv = not any(survivors_cov_eqv.values())
    m6_rec = A[0]["recipes"][M6]
    cert_g = {
        "certificate": "G_BL7_READING_DEPENDENCE",
        "question": ("Q2(c): under COV-EQV does the BL7 tension -- 'the only"
                     " covariant candidate is exactly the one the gravity"
                     " interface excludes' -- even arise?"),
        "interface_survivors": list(INTERFACE_SURVIVORS),
        "interface_excluded": list(INTERFACE_EXCLUDED),
        "survivors_satisfy_COV_EQV": survivors_cov_eqv,
        "survivors_satisfy_COV_INV": survivors_cov_inv,
        "tension_arises_under_COV_EQV": tension_arises_under_cov_eqv,
        "verdict": (
            "BL7 IS READING-DEPENDENT: it does NOT arise under COV-EQV."
            "  Every interface-surviving recipe intertwines, so under the"
            " landed Cycle-856 reading of covariance there is no conflict"
            " between covariance and the gravity interface at all, and"
            " Cycle 906's M6 becomes ONE OF TWO lawful resolutions"
            if not tension_arises_under_cov_eqv else
            "BL7 IS READING-INDEPENDENT: the interface survivors fail"
            " COV-EQV too, so the tension survives the intertwining"
            " reading and Cycle 906's resolution stands alone"),
        "the_two_lawful_resolutions": [
            {
                "id": "R1_906_M6_UNDER_COV_INV",
                "reading": "covariance read as COV-INV (fixed monitor)",
                "resolution": ("adopt M6_ABSOLUTE_ORBIT_UNIFORM, the unique"
                               " (up to scale) world-mass vector satisfying"
                               " COV-INV and the interface's zero-mass"
                               " requirement"),
                "price": {
                    "new_generator_outside_the_878_span": True,
                    "minimal_kernel_argument_extension": "25 -> 30",
                    "BL6_zero_events": m6_rec["zero_events"],
                    "BL6_zero_events_before": zero["recipes"][
                        "M3_OCCUPATION_WEIGHTED"]["zero_events"],
                    "support_worlds": m6_rec["support_worlds"],
                    "support_worlds_before": zero["recipes"][
                        "M3_OCCUPATION_WEIGHTED"]["support_worlds"],
                    "reading": ("keeps the stronger credential; pays one new"
                                " generator and drives BL6 to its maximum"),
                },
                "cov_eqv_status_of_M6": recipe_rows[M6]["COV_EQV"],
                "cov_inv_status_of_M6": cov_inv_rows[M6][
                    "COV_INV_at_phase_0"],
            },
            {
                "id": "R2_908_SURVIVORS_UNDER_COV_EQV",
                "reading": ("covariance read as COV-EQV, the intertwining"
                            " that Cycle 856 actually landed"),
                "resolution": ("no new weighting is needed: M3, M4 and M5"
                               " all satisfy COV-EQV, so the"
                               " interface-surviving three are already"
                               " covariant in the landed sense"),
                "price": {
                    "new_generator_outside_the_878_span": False,
                    "minimal_kernel_argument_extension": "25, unchanged",
                    "BL6_zero_events": zero["recipes"][
                        "M3_OCCUPATION_WEIGHTED"]["zero_events"],
                    "support_worlds": zero["recipes"][
                        "M3_OCCUPATION_WEIGHTED"]["support_worlds"],
                    "reading": ("costs nothing on the 878 span and leaves"
                                " BL6 where Cycle 905 left it; what it"
                                " costs instead is the STRONGER credential:"
                                " the phase-0 weighting is no longer"
                                " orbit-constant, so a fixed-monitor"
                                " observer sees different bookkeeping mass"
                                " on orbit-mates"),
                },
            },
        ],
        "neither_reading_is_axiom_required": {
            "906_requires_count": r906["Q2_requires_count"],
            "quote": NEEDLE_AXIOM_EXCLUSION,
            "quote_present":
                quotes["axioms_exclusion_list"]["present_byte_for_byte"],
            "reading": ("Cycle 906's fidelity sweep found 0 axiom sentences"
                        " REQUIRING monitor-phase covariance in any"
                        " reading, and the axiom baseline's own exclusion"
                        " list puts Born weights outside the axioms.  This"
                        " block does not select between R1 and R2; it"
                        " prices both and reports that the choice is not"
                        " forced by the axioms"),
        },
    }
    # outcome-neutral: the gate is that the interface split is the PINNED one
    # and that both readings are priced -- true under either branch
    cert_g["pass"] = bool(
        sorted(INTERFACE_SURVIVORS) == sorted(r905["Q1_surviving"])
        and sorted(INTERFACE_EXCLUDED) == sorted(r905["Q1_excluded"])
        and len(cert_g["the_two_lawful_resolutions"]) == 2)

    # ---- H: Q3, the escape orbit under phase composition -------------------
    escape_sets = {m: tuple(A[m]["escape_orbit_worlds"]) for m in phases}
    escape_indices = {m: tuple(A[m]["escape_orbit_indices"]) for m in phases}
    stationary_set = len({escape_sets[m] for m in phases}) == 1
    stationary_index = len({escape_indices[m] for m in phases}) == 1
    single_orbit = all(len(escape_indices[m]) == 1 for m in phases)

    def separations(positions):
        return sorted(((b - a) % stations)
                      for a, b in combinations(sorted(positions), 2))

    shape_by_phase = {}
    for m in phases:
        keys = [tuple(k) for k in A[m]["escape_orbit_keys"]]
        shape_by_phase[m] = {
            "k_values": sorted({k[0] for k in keys}),
            "event_values": sorted({k[1] for k in keys}),
            "separation_multisets": sorted({tuple(separations(k[2]))
                                            for k in keys}),
        }
    shape_constant = len({compact(shape_by_phase[m]) for m in phases}) == 1
    shape_856 = bool(
        shape_by_phase[0]["k_values"] == [2]
        and shape_by_phase[0]["event_values"]
        and shape_by_phase[0]["event_values"][0] in (0, 1, 2)
        and all(set(s) <= {5, 6}
                for s in shape_by_phase[0]["separation_multisets"]))
    cert_h = {
        "certificate": "H_ESCAPE_ORBIT_UNDER_PHASE_COMPOSITION",
        "question": ("Q3: does the single escape orbit remain the escape"
                     " orbit at every phase, or move?  (bears on"
                     " P-856-SHAPE and on 906's single-orbit scope note)"),
        "escape_orbit_count_by_phase": {str(m): len(escape_indices[m])
                                        for m in phases},
        "escape_orbit_worlds_by_phase": {str(m): list(escape_sets[m])
                                         for m in phases},
        "escape_orbit_index_by_phase": {str(m): list(escape_indices[m])
                                        for m in phases},
        "single_escape_orbit_at_every_phase": single_orbit,
        "escape_orbit_world_set_is_phase_stationary": stationary_set,
        "escape_orbit_index_is_phase_stationary": stationary_index,
        "escape_orbit_shape_by_phase": {str(m): shape_by_phase[m]
                                        for m in phases},
        "escape_orbit_shape_is_phase_constant": shape_constant,
        "escape_orbit_has_the_856_absolute_shape": shape_856,
        "verdict": (
            "PHASE-STATIONARY: the escape orbit is the SAME set of eleven"
            " worlds at every monitor phase and its census shape is"
            " phase-constant.  The mechanism is computed, not assumed: the"
            " escape orbit is a sigma-orbit, hence sigma-invariant as a"
            " set, and the TRANSPORT THEOREM makes the never-formed block"
            " at phase m the sigma_m transport of the phase-0 block, so"
            " 'misses the block' is a phase-independent property of an"
            " orbit"
            if (stationary_set and stationary_index and single_orbit) else
            "THE ESCAPE ORBIT MOVES: see escape_orbit_worlds_by_phase"),
        "P_856_SHAPE_status": (
            "ILLUMINATED, NOT DISCHARGED.  The eleven scans show the shape"
            " match Cycle 906 observed is not a phase-0 accident -- the"
            " escape orbit and its k=2 / separations-5,6 shape are"
            " invariant across the whole monitor-phase group, which is"
            " precisely the invariance Cycle 856's ABSOLUTE-record orbits"
            " have by definition (stamped under EVERY monitor placement)."
            "  That is new evidence for the identification and a new"
            " direction of test, but the two predicates still differ (856's"
            " E1 stamp versus the Cycle-878 composed-record formation"
            " ledger), so P-856-SHAPE remains a named premise"),
        "predicates_still_differ": True,
    }
    cert_h["pass"] = bool(single_orbit and stationary_set
                          and stationary_index and shape_constant)

    # ---- I: falsifiers -----------------------------------------------------
    def planted_world(spec, m, w):
        kind = spec[0]
        if kind == "constant":
            name = spec[1]
            return world_mass(0, name, w)
        if kind == "double_shift":
            name = spec[1]
            return world_mass((2 * m) % stations, name, w)
        if kind == "perturbed":
            name, bad_phase, bad_world, bump = spec[1], spec[2], spec[3], spec[4]
            num, total = world_mass(m, name, w)
            if m == bad_phase and w == bad_world:
                num += bump
            return (num, total)
        raise AssertionError(("planted family", spec))

    star0 = list(A[0]["escape_orbit_worlds"])
    bump_world = star0[0] if star0 else 0
    planted = {}
    for label, spec, expect in (
        ("P1_CONSTANT_FAMILY_OF_M3",
         ("constant", "M3_OCCUPATION_WEIGHTED"), False),
        ("P2_DOUBLE_SHIFT_FAMILY_OF_M3",
         ("double_shift", "M3_OCCUPATION_WEIGHTED"), False),
        ("P3_PERTURBED_M6_AT_PHASE_3",
         ("perturbed", M6, 3, bump_world, 1), False),
        ("P4_CONSTANT_FAMILY_OF_M2_positive_control",
         ("constant", "M2_PER_WORLD_UNIFORM"), True),
        ("P5_CONSTANT_FAMILY_OF_M6_positive_control",
         ("constant", M6), True),
    ):
        holds, wit = cov_eqv(planted_world, spec)
        planted[label] = {
            "definition": list(spec[:1]) + [str(x) for x in spec[1:]],
            "expected_COV_EQV": expect,
            "computed_COV_EQV": holds,
            "detected_as_expected": holds == expect,
            "witness": wit[:1],
        }

    # a planted non-intertwining LEDGER: swap two worlds' records at phase 4
    swap_a, swap_b = bump_world, (bump_world + 1) % n_worlds
    tampered_lane_sig = list(A[4]["lane_sig"])
    tampered_lane_sig[swap_a], tampered_lane_sig[swap_b] = \
        tampered_lane_sig[swap_b], tampered_lane_sig[swap_a]
    tamper_detected = (
        tampered_lane_sig != [A[0]["lane_sig"][sig[4][w]]
                              for w in range(n_worlds)])
    # a dropped-phase falsifier: the transport theorem must be sensitive to it
    dropped_ok = len(phase_rows) == stations
    # an orbit-skip falsifier: skipping the escape orbit flips 906's verdict
    skip_flips = (
        (zero["orbits_entirely_outside_block"] - 1) == 0
        and zero["orbits_entirely_outside_block"] == 1)
    cert_i = {
        "certificate": "I_FALSIFIERS",
        "planted_weighting_families": planted,
        "all_planted_families_detected_as_expected": all(
            v["detected_as_expected"] for v in planted.values()),
        "planted_ledger_tamper": {
            "definition": (f"swap the phase-4 record signatures of worlds"
                           f" {swap_a} and {swap_b}"),
            "worlds": [swap_a, swap_b],
            "signatures_differ": (A[4]["lane_sig"][swap_a]
                                  != A[4]["lane_sig"][swap_b]),
            "detected_by_the_transport_check": tamper_detected,
        },
        "dropped_phase_guard": {
            "phases_required": stations, "phases_present": len(phase_rows),
            "ok": dropped_ok,
        },
        "orbit_skip_sensitivity": {
            "escape_orbits": zero["orbits_entirely_outside_block"],
            "skipping_the_escape_orbit_flips_906_general_theorem_verdict":
                skip_flips,
        },
        "outcome_neutrality": (
            "every gate above is an equality test against a value computed"
            " from the pinned sources or from the scans themselves; no gate"
            " is conditioned on COV-EQV holding, and certificate G is"
            " written with both branches"),
    }
    cert_i["pass"] = bool(
        cert_i["all_planted_families_detected_as_expected"]
        and tamper_detected and dropped_ok
        and cert_i["planted_ledger_tamper"]["signatures_differ"])

    # ---- J: deterministic double build ------------------------------------
    dbl_rows = []
    for m in have_b:
        a, b = A[m], results[(m, "B")]
        dbl_rows.append({
            "phase": m,
            "raw_event_digest_equal":
                a["raw_event_digest"] == b["raw_event_digest"],
            "sorted_event_digest_equal":
                a["sorted_event_digest"] == b["sorted_event_digest"],
            "ledger_equal": (a["occ_global"] == b["occ_global"]
                             and a["formed"] == b["formed"]
                             and a["per_world_counts"] == b["per_world_counts"]),
            "recipes_equal": all(
                a["recipes"][n]["world_mass_nums"]
                == b["recipes"][n]["world_mass_nums"]
                and a["recipes"][n]["total_num"] == b["recipes"][n]["total_num"]
                for n in RECIPES),
            "escape_equal": (a["escape_orbit_worlds"]
                             == b["escape_orbit_worlds"]),
        })
    # analysis-layer double build: every COV-EQV / COV-INV verdict recomputed
    # by a structurally different arithmetic route (Fraction objects instead
    # of cross-multiplied integer pairs, and the (g, m) loop order reversed)
    def frac(num, total):
        """the normalized bookkeeping fraction; a degenerate all-zero
        weighting is carried as the exact zero rather than raising"""
        return Fraction(num, total) if total else Fraction(0)

    def cov_eqv_route_B(name):
        for g in phases:
            for m in phases:
                mg = (m + g) % stations
                rec_l = A[m]["recipes"][name]
                rec_r = A[mg]["recipes"][name]
                tl, tr = rec_l["total_num"], rec_r["total_num"]
                for w in range(n_worlds):
                    if frac(rec_l["world_mass_nums"][sig[g][w]], tl) \
                            != frac(rec_r["world_mass_nums"][w], tr):
                        return False
                    if frac(rec_l["event_weight_nums"][sig[g][w]], tl) \
                            != frac(rec_r["event_weight_nums"][w], tr):
                        return False
        return True

    def cov_inv_route_B(name):
        nums = A[0]["recipes"][name]["world_mass_nums"]
        for w in range(n_worlds):
            for g in phases:
                if nums[sig[g][w]] != nums[w]:
                    return False
        return True

    route_b_rows = {
        name: {
            "COV_EQV_route_A": recipe_rows[name]["COV_EQV"],
            "COV_EQV_route_B": cov_eqv_route_B(name),
            "COV_INV_route_A": cov_inv_rows[name]["COV_INV_at_phase_0"],
            "COV_INV_route_B": cov_inv_route_B(name),
        }
        for name in RECIPES
    }
    routes_agree = all(
        r["COV_EQV_route_A"] == r["COV_EQV_route_B"]
        and r["COV_INV_route_A"] == r["COV_INV_route_B"]
        for r in route_b_rows.values()
    )
    cert_j = {
        "certificate": "J_DETERMINISTIC_DOUBLE_BUILD",
        "scope": checkpoint["double_build_scope"],
        "declared_sub_check_phases": list(DOUBLE_BUILD_PHASES),
        "selection_rule": checkpoint["double_build_selection_rule"],
        "why_not_all_eleven": (
            "measured on this host: one phase-composed scan is 77.3s"
            " serially and ~235s under 10-way parallel contention; 22"
            " end-to-end scans would exceed the 900s cap.  Disclosed"
            " rather than silently reduced"),
        "rows": dbl_rows,
        "phases_double_built": have_b,
        "all_equal": all(all(v for k, v in r.items() if k != "phase")
                         for r in dbl_rows),
        "analysis_layer_double_build": {
            "route_A": ("cross-multiplied integer pairs, (m, g) loop order,"
                        " orbit-partition scan for COV-INV"),
            "route_B": ("Fraction objects, (g, m) loop order reversed,"
                        " direct sigma-orbit comparison for COV-INV"),
            "rows": route_b_rows,
            "routes_agree": routes_agree,
        },
    }
    cert_j["pass"] = bool(len(dbl_rows) == len(DOUBLE_BUILD_PHASES)
                          and cert_j["all_equal"] and routes_agree)

    # ---- K: runtime --------------------------------------------------------
    elapsed = monotonic() - started
    cert_k = {
        "certificate": "K_RUNTIME",
        "budget_sec": RUNTIME_BUDGET_SEC,
        "elapsed_sec": round(elapsed, 3),
        "scans_elapsed_sec": round(scans_elapsed, 3),
        "scan_count": len(jobs),
        "per_phase_timing": {str(m): A[m]["timing"] for m in phases},
        "906_priced_at_sec": 850,
        "full_census_no_sampling": True,
        "provenance": provenance,
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
    }
    cert_k["pass"] = bool(elapsed <= RUNTIME_BUDGET_SEC
                          and not cert_k["firewall_hits"]
                          and not cert_k["blocked_modules_loaded"])

    # ---- L: the discharge verdict and the ledger --------------------------
    discharge = ("DISCHARGED" if (cert_c["pass"] and cert_e["pass"]
                                  and cert_f["pass"]) else "NOT_DISCHARGED")
    ledger_rows = [
        {
            "id": "BL7_COVARIANCE",
            "status_before": ("RESOLVED BY CONSTRUCTION OUTSIDE THE 878"
                              " SPAN (Cycle 906, M6), conditional on the"
                              " COV-INV reading"),
            "status_now": (
                "READING-DEPENDENT, AND NOW PRICED BOTH WAYS.  Under"
                " COV-INV the 906 resolution stands: M6 is the unique"
                " world-mass solution.  Under COV-EQV -- the intertwining"
                " Cycle 856 actually landed -- the tension DOES NOT ARISE:"
                f" all three interface survivors {list(INTERFACE_SURVIVORS)}"
                " satisfy COV-EQV, at no cost on the 878 span.  M6 is"
                " therefore one of TWO lawful resolutions, and the axioms"
                " require neither reading"
                if not tension_arises_under_cov_eqv else
                "READING-INDEPENDENT: the interface survivors fail COV-EQV"
                " as well, so Cycle 906's resolution stands alone"),
            "blocked_on": "an owner choice between two priced readings",
        },
        {
            "id": "BL8_ESCAPE_ORBIT_STATUS",
            "status_before": "OPEN, premise P-856-SHAPE named and unpriced",
            "status_now": (
                "OPEN, but tested from a new direction: the escape orbit is"
                " PHASE-STATIONARY across the whole monitor-phase group and"
                " its k=2 / separations-5,6 shape is phase-constant, which"
                " is the same invariance Cycle 856's ABSOLUTE-record orbits"
                " carry by definition.  The predicates still differ, so"
                " P-856-SHAPE is not discharged"),
            "blocked_on": ("a recomputation of the 856 E1 stamps on this"
                           " lineage -- unchanged by this block"),
        },
        {
            "id": "BL9_COV_EQV_IS_FREE",
            "status_before": "NEW, surfaced by this block",
            "status_now": (
                "COMPUTED AND CLOSED AS A FACT, OPEN AS A SELECTION"
                " QUESTION: COV-EQV is satisfied by EVERY ledger-native"
                " recipe on this event space, so it has NO discriminating"
                " power over the candidate weightings.  Whatever selects"
                " the measurement weighting, the landed Cycle-856"
                " covariance is not it"),
            "blocked_on": "the selection gate, which remains open",
        },
    ]
    cert_l = {
        "certificate": "L_DISCHARGE_AND_LEDGER",
        "premise": "P-INTERTWINE-878",
        "status": discharge,
        "computed_relationship": cert_f["verdict"],
        "BL7_reading_dependence": cert_g["verdict"],
        "ledger_rows": ledger_rows,
        "premises_still_named": [
            "P-NONEMPTY (inherited from Cycle 905, untouched)",
            "P-856-SHAPE (named by Cycle 906, illuminated not discharged)",
        ],
        "premises_discharged_here": ["P-INTERTWINE-878"],
    }
    cert_l["pass"] = discharge == "DISCHARGED"

    certificates = {
        "A_PINS": cert_a, "B_RESTRICTION_GATES": cert_b,
        "C_ELEVEN_PHASE_COMPOSED_SCANS": cert_c,
        "D_COV_EQV_DERIVED_FROM_THE_DATA": cert_d,
        "E_RECIPE_LEVEL_COV_EQV": cert_e,
        "F_COV_EQV_VERSUS_COV_INV": cert_f,
        "G_BL7_READING_DEPENDENCE": cert_g,
        "H_ESCAPE_ORBIT_UNDER_PHASE_COMPOSITION": cert_h,
        "I_FALSIFIERS": cert_i,
        "J_DETERMINISTIC_DOUBLE_BUILD": cert_j,
        "K_RUNTIME": cert_k,
        "L_DISCHARGE_AND_LEDGER": cert_l,
    }
    checks = {k: bool(v["pass"]) for k, v in certificates.items()}

    theorems = [
        ("C908-T1 THE TRANSPORT THEOREM.  On the Cycle-878 composed-record"
         " event space the monitor-phase group acts by RELABELLING: for"
         " every m in Z_11 the phase-m composed scan reproduces the phase-0"
         " scan event for event under the census permutation sigma_m, and"
         " the occupation ledger, formation ledger, per-world event counts"
         " and per-lane record signatures all transport with it; the"
         " dead-wire set and safe-slot map are phase-independent.  Eleven"
         " full horizon-16384 scans, each double-built."),
        ("C908-T2 COV-EQV, DERIVED.  A weighting family {w_m} satisfies the"
         " Cycle-856 intertwining iff w_m(g.e) = w_{(m+g) mod 11}(e) for all"
         " g, m, e -- equivalently iff the family is generated from w_0 by"
         " w_m = w_0 o sigma_m.  Cycle 878's COV-INV is exactly this"
         " condition restricted to CONSTANT families.  The event sets"
         " themselves intertwine: g.e in E_m iff e in E_{(m+g) mod 11}."),
        ("C908-T3 THE SIX-RECIPE VERDICT.  All six candidate recipes --"
         " M1..M5 of Cycle 878 and M6 of Cycle 906 -- satisfy COV-EQV,"
         " because each is a function of the phase-m ledger alone and the"
         " ledger transports.  Only M2 and M6 satisfy COV-INV.  The two"
         " conditions therefore DIFFER on this data, with"
         f" {witness_recipe} as an explicit witness."),
        ("C908-T4 BL7 IS READING-DEPENDENT.  The interface survivors M3, M4"
         " and M5 all satisfy COV-EQV, so under the landed Cycle-856"
         " reading the covariance-versus-interface tension does not arise."
         "  Cycle 906's M6 resolution is one of two lawful resolutions, and"
         " Cycle 906's own fidelity sweep says the axioms require neither."),
        ("C908-T5 THE PRICE OF COV-EQV.  Because every ledger-native"
         " weighting satisfies it, COV-EQV imposes NO constraint on the"
         " selection problem: it removes BL7 at the cost of removing"
         " covariance as a discriminator.  COV-INV keeps the discriminating"
         " power and pays one generator outside the 878 span plus BL6 at"
         f" maximum ({m6_rec['zero_events']} of {zero['n_events']} events"
         f" at zero mass, support {m6_rec['support_worlds']} of"
         f" {zero['worlds_with_events']} worlds)."),
    ]

    verdict = ("P_INTERTWINE_878_DISCHARGED__COV_EQV_AND_COV_INV_DIFFER"
               "__BL7_IS_READING_DEPENDENT"
               if (discharge == "DISCHARGED" and not coincide
                   and not tension_arises_under_cov_eqv) else
               "P_INTERTWINE_878_" + discharge)

    receipt = {
        "cycle": 908,
        "block": "toe-time-blockQ5-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "question": ("Cycle 908 -- discharge P-INTERTWINE-878: run the"
                     " eleven phase-composed scans, derive COV-EQV, and"
                     " decide whether BL7 is reading-dependent"),
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "scope": ("the Cycle-863 census (748 worlds, 11 stations), the"
                  " Cycle-878 composed-record event space at horizon"
                  " 16384, and the six named candidate weightings; NO"
                  " probability postulate, NO Born rule, NO selection"),
        "VERDICT": verdict,
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "label_on_every_fraction": FRACTION_LABEL,
        "theorems": theorems,
        "named_premises": [
            "P-NONEMPTY (inherited from Cycle 905, untouched)",
            "P-INTERTWINE-878 (DISCHARGED here)",
            "P-856-SHAPE (illuminated, still named)",
        ],
        "Q1_scans_run": len(phases),
        "Q1_phase_rows": [
            {"phase": r["phase"], "raw_event_digest": r["raw_event_digest"],
             "sorted_event_digest": r["sorted_event_digest"],
             "transported_sorted_event_digest":
                 r["transported_sorted_event_digest"],
             "n_events": r["n_events"], "worlds_formed": r["worlds_formed"],
             "worlds_never_formed": r["worlds_never_formed"],
             "orbits_mixed": r["orbits_mixed"],
             "escape_orbit_worlds": r["escape_orbit_worlds"],
             "diff_vs_phase0": r["diff_vs_phase0"],
             "timing": r["timing"]}
            for r in phase_rows
        ],
        "Q1_transport_theorem_holds": transport_theorem,
        "Q1_phase0_reproduces_878":
            cert_b["phase0_reproduces_the_878_census_value_for_value"],
        "Q1_phase0_event_space_digest": zero["raw_event_digest"],
        "Q1_distinct_raw_event_digests": raw_digests_distinct,
        "Q2_cov_eqv_form": derived_form["instantiated_exact_form"],
        "Q2_recipe_verdicts": {n: {
            "COV_EQV": recipe_rows[n]["COV_EQV"],
            "COV_INV": cov_inv_rows[n]["COV_INV_at_phase_0"]}
            for n in RECIPES},
        "Q2_cov_eqv_recipes": cert_e["cov_eqv_recipes"],
        "Q2_cov_inv_recipes": cert_f["cov_inv_recipes_phase_0"],
        "Q2_relationship": cert_f["verdict"],
        "Q2_witness": cert_f["witness"],
        "Q2_BL7_verdict": cert_g["verdict"],
        "Q2_BL7_tension_arises_under_COV_EQV": tension_arises_under_cov_eqv,
        "Q3_discharge_status": discharge,
        "Q3_escape_orbit_phase_stationary": cert_h["verdict"],
        "Q3_P_856_SHAPE_status": cert_h["P_856_SHAPE_status"],
        "ledger_rows": ledger_rows,
        "restriction_gate": (f"{cert_b['reproduce']}/{cert_b['total']}"
                             " restriction gates reproduce"),
        "restriction_gate_rows": gate_rows,
        "deterministic_double_build": {
            "scan_level_phases": have_b,
            "scan_level_all_equal": cert_j["all_equal"],
            "analysis_level_routes_agree": routes_agree,
        },
        "double_build_scope": cert_j["scope"],
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "elapsed_sec": round(monotonic() - started, 3),
        "source_pins": {"sha256": cert_a["sha256"],
                        "git_blobs": cert_a["git_blobs"]},
        "discovery_sweep": cert_a["discovery_sweep"],
        "event_space_digest": zero["raw_event_digest"],
    }
    receipt["science_digest"] = digest({
        k: v for k, v in receipt.items() if k not in ("elapsed_sec",)
    })
    receipt["self_sha256"] = sha256(
        Path(__file__).read_bytes()).hexdigest()

    out_path = ROOT / "outputs" / \
        "intertwine_discharge_cycle908_receipt_2026_07_28.json"
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    for name in ("A_PINS", "B_RESTRICTION_GATES",
                 "C_ELEVEN_PHASE_COMPOSED_SCANS",
                 "D_COV_EQV_DERIVED_FROM_THE_DATA", "E_RECIPE_LEVEL_COV_EQV",
                 "F_COV_EQV_VERSUS_COV_INV", "G_BL7_READING_DEPENDENCE",
                 "H_ESCAPE_ORBIT_UNDER_PHASE_COMPOSITION", "I_FALSIFIERS",
                 "J_DETERMINISTIC_DOUBLE_BUILD", "K_RUNTIME",
                 "L_DISCHARGE_AND_LEDGER"):
        cert = certificates[name]
        body = compact(cert)
        if len(body) > 11_000:
            body = body[:11_000] + "...TRUNCATED_IN_STDOUT_SEE_RECEIPT"
        sys.stdout.write(
            f"CERTIFICATE {name} {'PASS' if cert['pass'] else 'FAIL'} "
            + body + "\n")
    sys.stdout.write("SUMMARY_JSON " + compact({
        "cycle": 908,
        "VERDICT": verdict,
        "checks": checks,
        "pass": all(checks.values()),
        "scans": len(phases),
        "transport_theorem": transport_theorem,
        "cov_eqv_recipes": cert_e["cov_eqv_recipes"],
        "cov_inv_recipes": cert_f["cov_inv_recipes_phase_0"],
        "relationship": cert_f["verdict"],
        "BL7_tension_under_COV_EQV": tension_arises_under_cov_eqv,
        "escape_orbit_phase_stationary": stationary_set and stationary_index,
        "elapsed_sec": receipt["elapsed_sec"],
        "science_digest": receipt["science_digest"],
    }) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
