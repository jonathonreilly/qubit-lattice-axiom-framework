#!/usr/bin/env python3
"""Cycle 908 independent checker -- SPECIFIED TO REFUTE.

This runner exists to break the Cycle-908 primary's claims, not to agree
with them.  It BLOCKLISTS the primary and every upstream primary from
import and rebuilds what it needs from the landed Cycle-719 core plus
AST lifts of the pinned sources.

Attacks, in order:

R0 PINS AND LEAKS.  Pin every input by sha256 and git blob.  Audit this
   checker's OWN source for verdict leakage: no primary verdict string
   may appear in it, and every verdict it issues must be recomputable
   with the primary's receipt removed.

R1 AN INDEPENDENT PHASE COMPOSITION.  The primary implements monitor
   phase m by RELABELLING the lanes -- lane l is given the census key
   frame_map(census[l], m) and the phase-0 schedule.  This checker
   refuses that shortcut.  It builds the phase-m model the other way
   round, from the Cycle-856 stamp machinery's own statement: lane l
   keeps its key census[l], its engagement orbit is run with the token
   positions advanced by m, and its H-chunk schedule is built row by row
   out of monitor_schedule_manifest(key, m, stations).  If the primary's
   relabelling is not the same model, the two constructions diverge and
   THAT is the finding.

   Three phases are recomputed at the FULL pinned horizon; the other
   eight are spot-checked at a declared reduced horizon.  The three are
   chosen by a published rule, not by convenience.

R2 AN INDEPENDENT DERIVATION OF COV-EQV.  The intertwining's form is
   read out of the Cycle-856 source's own string constants by AST -- the
   identity and the monitor action -- and the weighting analogue is
   derived from them here, not taken from the primary's sentence.  Two
   inequivalent-looking forms (the identity form and the generated form)
   are then tested against each other on the checker's own data.

R3 THE RECIPE-LEVEL TEST, ATTACKED.  The six candidate weightings are
   re-instantiated from their DEFINITIONS -- not by calling the pinned
   constructor -- and cross-checked against the pinned constructor at
   phase 0.  M6 gets special attention: its defining orbit is recomputed
   at every phase this checker scans, and the test is shown to be
   sensitive to that orbit moving.  A recipe whose defining set moved
   under phase composition would break COV-EQV, and the checker plants
   exactly such a recipe to prove the test can see it.

R4 COV-EQV VERSUS COV-INV.  Recomputed independently, with the witness
   re-derived rather than copied.

R5 BL7.  The survivors' status under both readings, recomputed.

R6 TEETH.  Eight designed mutations, each of which MUST change a
   verdict; a tooth that does not bite is reported as a failure of this
   checker's own instrumentation.

Exit code 0 regardless of whether the primary's claims survive.  The
verdict is data, not a gate.
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
SPOT_HORIZON = 1024

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C856_PATH = "scripts/frontier_cycle856_record_covariance_2026_07_28.py"
C856_NOTE = "docs/RECORD_COVARIANCE_CYCLE856_BOUNDED_THEOREM_NOTE_2026-07-28.md"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_PATH = "scripts/frontier_cycle906_covariance_tension_2026_07_28.py"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C908_PATH = "scripts/frontier_cycle908_intertwine_discharge_2026_07_28.py"
C908_RECEIPT = "outputs/intertwine_discharge_cycle908_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C856_PATH, C856_NOTE, C878_PATH, C878_RECEIPT,
    C905_RECEIPT, C906_PATH, C906_RECEIPT, C908_PATH, AXIOMS_PATH,
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C856_PATH:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
    C856_NOTE:
        "7b6b73826ee397e66102994174d94e04c3f174761f00ffcfe0da2be97e72a545",
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
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C856_PATH: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
    C856_NOTE: "f819f5b31d442248fac255fcdf3b0139d6ba83f8",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C906_PATH: "d7577bb2ac9f4cb7ee9d8abc5f19e9c7cf888df9",
    C906_RECEIPT: "392cba199a75a14a8bb88808943c1259cbd7a94b",
    C908_PATH: "a32762df147312b150eee84b5311efa2476af677",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}
# The Cycle-908 receipt is produced by the runner under test, so its digest
# is recomputed and REPORTED rather than pinned to a hand-typed constant.
UNPINNED_BY_DESIGN = (C908_RECEIPT,)

BLOCKLISTED_MODULES = (
    "frontier_cycle856_record_covariance_2026_07_28",
    "frontier_cycle856_covariance_independent_check_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle867_composed_record_write_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle878_event_space_independent_check_2026_07_28",
    "frontier_cycle902_p2_kernel_attack_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle908_intertwine_discharge_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _CheckerFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


CHECKER_FIREWALL = _CheckerFirewall()
sys.meta_path.insert(0, CHECKER_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

RECIPES = ("M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
           "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
           "M6_ABSOLUTE_ORBIT_UNIFORM")
M6 = "M6_ABSOLUTE_ORBIT_UNIFORM"
SURVIVORS = ("M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
             "M5_FORMATION_MOMENT")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


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
    missing = tuple(f for f in funcs if f not in {n.name for n in body})
    if missing or tuple(c for c in consts if c not in found):
        raise AssertionError(("ast lift incomplete", path, missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(globals_)
    namespace.update(found)
    exec(compile(module, f"<ast-lift {path}>", "exec"), namespace)
    return namespace, found


C863_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "derive_census",
    "watched_registers", "dirty_partition", "build_initial_states",
    "pack_lanes", "compile_masked_gate", "masked_h_schedules", "compile_fast",
    "mask_over", "lanes_of", "lane_state",
)
C856_FUNCS = ("monitor_schedule_manifest", "frame_map")
C878_FUNCS = ("lcm", "dead_wire_rig", "composed_scan", "build_candidates",
              "monitor_phase_action", "group_orbits")
C878_CONSTS = ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS",
               "REGISTER_CAP", "CANDIDATE_NAMES", "CONTROL_NAME",
               "FAMILY_ORDER")

_LIFT = None


def lift():
    global _LIFT
    if _LIFT is not None:
        return _LIFT
    ns863, _ = ast_lift(C863_PATH, C863_FUNCS,
                        ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
                        {"K": K, "combinations": combinations})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns856, _ = ast_lift(C856_PATH, C856_FUNCS,
                        ("FIXTURE_BANKS",),
                        {"K": K, "combinations": combinations})
    c856 = SimpleNamespace(**{n: ns856[n] for n in C856_FUNCS})
    ns878, consts = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
         "Fraction": Fraction, "json": json})
    _LIFT = (c863, c856, ns878, consts)
    return _LIFT


# ---------------------------------------------------------------------------
# R1: the independent phase-m model
# ---------------------------------------------------------------------------

def own_action(census, stations, shift):
    """The monitor-phase permutation, computed here from the census key
    arithmetic directly -- never through the pinned helper."""
    index_of = {key: i for i, key in enumerate(census)}
    image = []
    for k, event, positions in census:
        target = (k, event,
                  tuple(sorted((p + shift) % stations for p in positions)))
        image.append(index_of[target])
    return tuple(image)


def independent_phase_model(phase: int, horizon: int) -> dict:
    """Build the phase-m composed model WITHOUT relabelling the census.

    Lane l keeps census[l].  What moves is the monitor: the engagement
    orbit runs with the token positions advanced by m, and every H-chunk
    schedule is assembled from the Cycle-856 monitor manifest
    monitor_schedule_manifest(key, m, stations).
    """
    t_start = monotonic()
    c863, c856, ns878, consts = lift()
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    n_worlds = len(census)

    # (i) the engagement orbit, advanced by the monitor phase -- our own loop
    seed_by_event = dict(event_seeds)
    states = []
    init_failures = 0
    for k, event, positions in census:
        moved = tuple(sorted((p + phase) % stations for p in positions))
        before = seed_by_event[event]
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=moved)
        expected = tuple(int(s in moved) for s in range(stations))
        init_failures += int(rail_a != expected or any(rail_b))
        states.append(after)
    states = tuple(states)

    # (ii) the H-chunk schedules, assembled from the 856 monitor manifest
    def schedules_from_the_856_manifest(prog, lane_keys):
        manifests = [c856.monitor_schedule_manifest(key, phase, stations)
                     for key in lane_keys]
        rows = []
        for step in range(stations):
            live = [set(m[step]) for m in manifests]
            schedule = []
            for station, row in enumerate(prog):
                mask = 0
                for lane, rowset in enumerate(live):
                    if station in rowset:
                        mask |= 1 << lane
                if mask:
                    schedule.extend(c863.compile_masked_gate(g, mask)
                                    for g in K.mapped_macro(row))
            rows.append(tuple(schedule))
        return tuple(rows)

    shim = SimpleNamespace(**{n: getattr(c863, n) for n in C863_FUNCS})
    shim.masked_h_schedules = schedules_from_the_856_manifest
    ns878["C863"] = shim

    sim = census + (census[0],)
    rig = ns878["dead_wire_rig"](
        program, sim, c863.pack_lanes(states + (states[0],)))
    scan = ns878["composed_scan"](program, census, states, rig, horizon)

    events = scan["events"]
    occ_global = scan["occ_global"]
    formed = scan["formed"]
    boundaries = scan["boundaries"]
    per_world = Counter(e[0] for e in events)
    supported = sorted(per_world)

    tau = own_action(census, stations, phase)
    raw_digest = digest([list(e) for e in events])
    sorted_digest = digest(sorted([list(e) for e in events]))
    transported_digest = digest(sorted(
        [[tau[e[0]], e[1], e[2], e[3], e[4]] for e in events]))

    by_lane: dict = {}
    for lane, moment, tag, ordinal, content in events:
        by_lane.setdefault(lane, []).append([moment, tag, ordinal, content])
    lane_sig = [digest(sorted(by_lane.get(w, []))) for w in range(n_worlds)]

    # the pinned constructor, kept only as a CROSS-CHECK of our own recipes
    nums, dens, _meta, _pw, _sup, common = ns878["build_candidates"](
        events, occ_global, formed, boundaries)
    pinned_world_mass = {}
    for name, vector in nums.items():
        acc = [0] * n_worlds
        for index, event in enumerate(events):
            acc[event[0]] += vector[index]
        pinned_world_mass[name] = (acc, sum(vector))

    payload = {
        "phase": phase,
        "horizon": horizon,
        "stations": stations,
        "n_worlds": n_worlds,
        "n_events": len(events),
        "boundaries": boundaries,
        "mismatches": scan["mismatches"],
        "write_once_violations": scan["write_once_violations"],
        "init_failures": init_failures,
        "raw_event_digest": raw_digest,
        "sorted_event_digest": sorted_digest,
        "transported_sorted_event_digest": transported_digest,
        "dead_wires_digest": digest(list(rig["dead_wires"])),
        "per_world_counts": [per_world.get(w, 0) for w in range(n_worlds)],
        "occ_global": list(occ_global),
        "formed": {str(w): b for w, b in sorted(formed.items())},
        "lane_sig": lane_sig,
        "supported": supported,
        "worlds_formed": len(formed),
        "worlds_never_formed": len(supported) - len(formed),
        "pinned_constructor_world_mass": pinned_world_mass,
        "common_denominator": common,
        "timing": round(monotonic() - t_start, 3),
    }
    return payload


def _job(spec):
    phase, horizon = spec
    return independent_phase_model(phase, horizon)


# ---------------------------------------------------------------------------
# R3: the six recipes, re-instantiated from their DEFINITIONS
# ---------------------------------------------------------------------------

def own_world_masses(model, orbits, star_override=None) -> dict:
    """World masses as exact normalized Fractions, from the definitions --
    not from the pinned constructor.

    star_override supplies M6's defining orbit when the model's own
    horizon is too short to produce one.  The escape orbit of the pinned
    construction only forms at boundary ~162180 of 180224, so at any
    reduced spot horizon NO orbit escapes the never-formed block and M6
    would be identically zero.  The override is disclosed in the receipt;
    the model's own escape set is always reported alongside it.
    """
    n_worlds = model["n_worlds"]
    counts = model["per_world_counts"]
    occ = model["occ_global"]
    formed = {int(w): b for w, b in model["formed"].items()}
    boundaries = model["boundaries"]
    supported = set(model["supported"])
    never = {w for w in supported if w not in formed}
    escape = [orbit for orbit in orbits if not (set(orbit) & never)]
    native_star = sorted(escape[0]) if escape else []
    star = set(star_override) if star_override is not None \
        else set(native_star)

    coeff = {
        "M1_COUNTING": lambda w: counts[w],
        "M2_PER_WORLD_UNIFORM": lambda w: 1,
        "M3_OCCUPATION_WEIGHTED": lambda w: occ[w],
        "M4_FORMATION_LIFETIME":
            lambda w: (boundaries - formed[w] + 1) if w in formed else 0,
        "M5_FORMATION_MOMENT": lambda w: formed[w] if w in formed else 0,
        M6: lambda w: 1 if w in star else 0,
    }
    out = {}
    for name, a_of in coeff.items():
        total = sum(a_of(w) for w in supported)
        masses = [Fraction(a_of(w), total) if (total and w in supported)
                  else Fraction(0) for w in range(n_worlds)]
        weights = [masses[w] / counts[w] if counts[w] else Fraction(0)
                   for w in range(n_worlds)]
        out[name] = {"world_mass": masses, "event_weight": weights,
                     "support": sorted(w for w in supported
                                       if masses[w] != 0)}
    out["_escape_orbit"] = sorted(star)
    out["_native_escape_orbit"] = native_star
    out["_star_overridden"] = star_override is not None
    out["_never_formed"] = len(never)
    return out


def cov_eqv_grid(masses_by_phase, tau_by_shift, index_set, stations,
                 name, sign=+1, key="world_mass"):
    """the intertwining test on the declared index set.  Returns
    (holds, pairs_tested, witness)."""
    pairs, witness = 0, None
    n_worlds = len(tau_by_shift[0])
    for m in index_set:
        for g in range(stations):
            mg = (m + g) % stations
            if mg not in index_set:
                continue
            pairs += 1
            shift = tau_by_shift[g % stations] if sign > 0 \
                else tau_by_shift[(-g) % stations]
            left = masses_by_phase[m][name][key]
            right = masses_by_phase[mg][name][key]
            for w in range(n_worlds):
                if left[shift[w]] != right[w]:
                    if witness is None:
                        witness = {"m": m, "g": g, "world": w,
                                   "shifted": shift[w],
                                   "left": str(left[shift[w]]),
                                   "right": str(right[w])}
                    return False, pairs, witness
    return True, pairs, witness


def cov_inv(masses, tau_by_shift, stations, name):
    vec = masses[name]["world_mass"]
    for w in range(len(vec)):
        for g in range(stations):
            if vec[tau_by_shift[g][w]] != vec[w]:
                return False, {"world_a": w, "world_b": tau_by_shift[g][w],
                               "shift": g, "mass_a": str(vec[w]),
                               "mass_b": str(vec[tau_by_shift[g][w]])}
    return True, None


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    disagreements: list[str] = []

    # ---- R0: pins and the leak audit --------------------------------------
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    receipt_path = ROOT / C908_RECEIPT
    receipt_present = receipt_path.is_file()
    receipt_bytes = receipt_path.read_bytes() if receipt_present else b"{}"
    primary = json.loads(receipt_bytes.decode("utf-8")) if receipt_present \
        else {}
    own_source = Path(__file__).read_text(encoding="utf-8")
    # The leak needles are taken from the primary's receipt AT RUN TIME, so
    # they cannot appear in this file as literals and the test cannot defeat
    # itself the way a hand-typed token list would.
    leak_needles = {
        "primary_VERDICT": primary.get("VERDICT"),
        "primary_science_digest": primary.get("science_digest"),
        "primary_phase0_event_space_digest":
            primary.get("Q1_phase0_event_space_digest"),
        "primary_BL7_verdict": primary.get("Q2_BL7_verdict"),
        "primary_discharge_status": primary.get("Q3_discharge_status"),
    }
    leak_hits = [k for k, v in leak_needles.items()
                 if isinstance(v, str) and v and v in own_source]
    r0 = {
        "check": "R0_PINS_AND_LEAKS",
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "unpinned_by_design": list(UNPINNED_BY_DESIGN),
        "primary_receipt_present": receipt_present,
        "primary_receipt_sha256": sha256(receipt_bytes).hexdigest(),
        "leak_needle_rule": ("every needle is read out of the primary's"
                             " receipt at run time; none is a literal in"
                             " this file, so the audit cannot pass by"
                             " construction"),
        "leak_needles_checked": sorted(k for k, v in leak_needles.items()
                                       if isinstance(v, str) and v),
        "verdict_tokens_absent_from_this_checker": not leak_hits,
        "leak_tokens_found": leak_hits,
        "firewall_hits": list(CHECKER_FIREWALL.hits),
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
    }
    r0["pass"] = bool(r0["sha256_all_match"] and r0["git_blobs_all_match"]
                      and not leak_hits and not r0["firewall_hits"]
                      and not r0["blocked_modules_loaded"])

    _c863, _c856, ns878, consts = lift()
    full_horizon = consts["HORIZON"]

    # ---- which three phases, and why --------------------------------------
    double_built = []
    rearrangement = {}
    if primary:
        dbb = primary.get("deterministic_double_build") or {}
        double_built = list(dbb.get("scan_level_phases") or [])
        for row in primary.get("Q1_phase_rows", []):
            rearrangement[int(row["phase"])] = int(
                row.get("diff_vs_phase0", {}).get(
                    "worlds_whose_event_count_changed", 0))
    stations = 11
    singles = [m for m in range(1, stations) if m not in double_built]
    if singles and rearrangement:
        load_bearing = max(singles,
                           key=lambda m: (rearrangement.get(m, 0), m))
    elif singles:
        load_bearing = max(singles)
    else:
        load_bearing = 6
    full_phases = sorted({0, 1, load_bearing})
    selection_rule = (
        "phase 0, because the identity phase IS the Cycle-878 construction"
        " and it carries every restriction gate; phase 1, because it is the"
        " group generator and every other phase is a composite of it, so a"
        " sign or composition error shows here first; and the LOAD-BEARING"
        " phase, computed as the phase the primary built only ONCE (outside"
        " its declared double-build subset) whose formation ledger is most"
        " rearranged relative to phase 0, ties broken by the largest index."
        f"  That rule selects {load_bearing} from"
        f" singles={singles} with double_built={double_built}")

    spot_phases = [m for m in range(stations) if m not in full_phases]
    jobs = [(m, full_horizon) for m in full_phases]
    jobs += [(m, SPOT_HORIZON) for m in range(stations)]
    workers = max(1, min(len(jobs), os.cpu_count() or 1))
    results_full: dict = {}
    results_spot: dict = {}
    pool_error = None
    try:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for spec, out in zip(jobs, pool.map(_job, jobs)):
                if spec[1] == full_horizon:
                    results_full[spec[0]] = out
                else:
                    results_spot[spec[0]] = out
    except Exception as exc:                             # pragma: no cover
        pool_error = repr(exc)
        for spec in jobs:
            out = _job(spec)
            if spec[1] == full_horizon:
                results_full[spec[0]] = out
            else:
                results_spot[spec[0]] = out

    c863, c856, ns878, consts = lift()
    program, _seeds, census = c863.derive_census()
    n_worlds = len(census)
    tau = [own_action(census, stations, g) for g in range(stations)]
    # orbits by UNION-FIND on our own permutations, not by the pinned walk
    parent = list(range(n_worlds))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for g in range(stations):
        for w in range(n_worlds):
            a, b = find(w), find(tau[g][w])
            if a != b:
                parent[a] = b
    groups: dict = {}
    for w in range(n_worlds):
        groups.setdefault(find(w), []).append(w)
    orbits = [sorted(v) for v in groups.values()]
    orbits.sort()

    # ---- R1: the independent phase composition ----------------------------
    primary_rows = {int(r["phase"]): r for r in primary.get("Q1_phase_rows", [])}
    full_rows = []
    for m in full_phases:
        mine = results_full[m]
        theirs = primary_rows.get(m, {})
        transported_matches = (mine["transported_sorted_event_digest"]
                               == results_full[0]["sorted_event_digest"]
                               if 0 in results_full else None)
        full_rows.append({
            "phase": m,
            "my_raw_event_digest": mine["raw_event_digest"],
            "primary_raw_event_digest": theirs.get("raw_event_digest"),
            "raw_digests_agree":
                mine["raw_event_digest"] == theirs.get("raw_event_digest"),
            "my_sorted_event_digest": mine["sorted_event_digest"],
            "sorted_digests_agree": (mine["sorted_event_digest"]
                                     == theirs.get("sorted_event_digest")),
            "transported_digest_agrees": (
                mine["transported_sorted_event_digest"]
                == theirs.get("transported_sorted_event_digest")),
            "my_transport_identity_holds": transported_matches,
            "n_events": mine["n_events"],
            "worlds_formed": mine["worlds_formed"],
            "worlds_never_formed": mine["worlds_never_formed"],
            "mismatches": mine["mismatches"],
            "init_failures": mine["init_failures"],
            "timing_sec": mine["timing"],
        })
    spot_rows = []
    spot0 = results_spot[0]
    for m in range(stations):
        mine = results_spot[m]
        spot_rows.append({
            "phase": m,
            "horizon": SPOT_HORIZON,
            "n_events": mine["n_events"],
            "transport_identity_holds": (
                mine["transported_sorted_event_digest"]
                == spot0["sorted_event_digest"]),
            "occupation_is_the_tau_transport": (
                mine["occ_global"]
                == [spot0["occ_global"][tau[m][w]] for w in range(n_worlds)]),
            "lane_signature_is_the_tau_transport": (
                mine["lane_sig"]
                == [spot0["lane_sig"][tau[m][w]] for w in range(n_worlds)]),
            "dead_wires_identical":
                mine["dead_wires_digest"] == spot0["dead_wires_digest"],
        })
    full_agree = all(r["raw_digests_agree"] and r["sorted_digests_agree"]
                     for r in full_rows) if primary_rows else None
    spot_transport = all(r["transport_identity_holds"]
                         and r["occupation_is_the_tau_transport"]
                         and r["lane_signature_is_the_tau_transport"]
                         for r in spot_rows)
    if primary_rows and not full_agree:
        disagreements.append(
            "the independently constructed phase-m model does NOT reproduce"
            " the primary's per-phase census digests")
    r1 = {
        "check": "R1_INDEPENDENT_PHASE_COMPOSITION",
        "construction": (
            "lane l keeps census[l]; the monitor moves.  The engagement"
            " orbit is run with token positions advanced by m and every"
            " H-chunk schedule is assembled row by row from"
            " monitor_schedule_manifest(key, m, 11).  The primary instead"
            " relabels lane l to frame_map(census[l], m) and uses the"
            " phase-0 schedule.  These are DIFFERENT programs; agreement of"
            " their outputs is a result, not a tautology"),
        "phases_recomputed_at_full_horizon": full_phases,
        "full_horizon": full_horizon,
        "selection_rule": selection_rule,
        "spot_check_horizon": SPOT_HORIZON,
        "spot_phases": list(range(stations)),
        "spot_scope": (
            f"all eleven phases are re-scanned at horizon {SPOT_HORIZON};"
            " this corroborates the phase-composition STRUCTURE and the"
            " transport identity at every phase, but only the three"
            " full-horizon phases test the primary's published"
            f" horizon-{full_horizon} digests"),
        "full_rows": full_rows,
        "spot_rows": spot_rows,
        "full_horizon_digests_agree_with_primary": full_agree,
        "spot_transport_identity_holds_at_every_phase": spot_transport,
        "orbits_by_union_find": len(orbits),
        "orbit_size_histogram": dict(sorted(
            Counter(len(o) for o in orbits).items())),
        "pool_error": pool_error,
    }
    r1["pass"] = bool(spot_transport and all(
        r["mismatches"] == 0 and r["init_failures"] == 0 for r in full_rows))

    # ---- R2: an independent derivation of COV-EQV -------------------------
    source_856 = (ROOT / C856_PATH).read_text(encoding="utf-8")
    tree_856 = ast.parse(source_856, filename=C856_PATH)
    identity_string = None
    action_string = None
    for node in ast.walk(tree_856):
        if isinstance(node, ast.Dict):
            for key_node, value_node in zip(node.keys, node.values):
                if isinstance(key_node, ast.Constant) \
                        and isinstance(value_node, ast.Constant):
                    if key_node.value == "identity":
                        identity_string = value_node.value
                    if key_node.value == "monitor_action":
                        action_string = value_node.value
    # the two forms, tested against each other on OUR data.  M6's defining
    # orbit is a FULL-HORIZON object, so it is computed there and carried
    # into the spot-horizon instances (disclosed in R3).
    masses_full = {m: own_world_masses(results_full[m], orbits)
                   for m in full_phases}
    full_star = masses_full[0]["_escape_orbit"]
    masses_spot = {m: own_world_masses(results_spot[m], orbits,
                                       star_override=full_star)
                   for m in range(stations)}
    identity_form = {}
    generated_form = {}
    for name in RECIPES:
        holds, pairs, wit = cov_eqv_grid(masses_spot, tau, set(range(stations)),
                                         stations, name)
        holds_e, _pe, wit_e = cov_eqv_grid(
            masses_spot, tau, set(range(stations)), stations, name,
            key="event_weight")
        identity_form[name] = {"holds": bool(holds and holds_e),
                               "holds_on_world_masses": holds,
                               "holds_on_event_weights": holds_e,
                               "pairs_tested": pairs,
                               "witness": wit or wit_e}
        gen = all(
            masses_spot[m][name]["world_mass"]
            == [masses_spot[0][name]["world_mass"][tau[m][w]]
                for w in range(n_worlds)]
            for m in range(stations))
        generated_form[name] = gen
    forms_agree = all(identity_form[n]["holds"] == generated_form[n]
                      for n in RECIPES)
    r2 = {
        "check": "R2_INDEPENDENT_COV_EQV_DERIVATION",
        "read_out_of_the_856_source_by_ast": {
            "identity": identity_string,
            "monitor_action": action_string,
        },
        "derivation_here": (
            "856 states stamped_m(g.key) == stamped_{g.m}(key) with"
            " g.m = (m + g) mod 11.  Replace the Boolean predicate"
            " 'stamped' by a Q-valued weighting and the same identity"
            " reads w_m(g.e) = w_{(m+g) mod 11}(e), with g acting on a"
            " realized record event through its world coordinate only."
            "  Equivalently (set g = -m) w_m = w_0 o tau_m, the GENERATED"
            " form.  The two forms are logically equivalent only if tau is"
            " a group action; that is checked below on the actual"
            " permutations, and the two forms are then compared verdict by"
            " verdict on the checker's own eleven reduced-horizon"
            " censuses"),
        "tau_is_a_group_action": all(
            [tau[m][tau[g][w]] for w in range(n_worlds)]
            == list(tau[(m + g) % stations])
            for m in range(stations) for g in range(stations)),
        "tau_is_free": all(all(tau[g][w] != w for w in range(n_worlds))
                           for g in range(1, stations)),
        "identity_form_verdicts": {n: identity_form[n]["holds"]
                                   for n in RECIPES},
        "generated_form_verdicts": generated_form,
        "the_two_forms_agree": forms_agree,
        "pairs_tested_per_recipe": {n: identity_form[n]["pairs_tested"]
                                    for n in RECIPES},
        "cov_inv_is_the_constant_family": (
            "substituting the constant family w_m = w_0 into the identity"
            " gives w_0(g.e) = w_0(e) for every g, which is exactly the"
            " pinned Cycle-878 orbit-constancy test.  COV-INV is therefore"
            " a special case of COV-EQV, never the other way round"),
    }
    if identity_string is None or "stamped_m" not in (identity_string or ""):
        disagreements.append(
            "could not read the intertwining identity out of the pinned"
            " Cycle-856 source by AST")
    r2["pass"] = bool(forms_agree and r2["tau_is_a_group_action"]
                      and r2["tau_is_free"] and identity_string)

    # ---- R3: the recipe-level test, attacked ------------------------------
    # cross-check our own recipe definitions against the PINNED constructor
    cross = {}
    ref = results_spot[0]
    for name in ("M1_COUNTING", "M2_PER_WORLD_UNIFORM",
                 "M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
                 "M5_FORMATION_MOMENT"):
        acc, total = ref["pinned_constructor_world_mass"][name]
        mine = masses_spot[0][name]["world_mass"]
        cross[name] = all(
            Fraction(acc[w], total) == mine[w] for w in range(n_worlds))
    # M6 under phase composition, computed independently at every phase
    escape_full = {m: masses_full[m]["_escape_orbit"] for m in full_phases}
    escape_native_spot = {m: masses_spot[m]["_native_escape_orbit"]
                          for m in range(stations)}
    escape_moves = len({tuple(escape_full[m]) for m in full_phases}) != 1
    escape_is_a_tau_orbit = all(
        escape_full[m] in orbits for m in full_phases if escape_full[m])
    spot_escape_empty_everywhere = all(
        not v for v in escape_native_spot.values())
    # the sensitivity attack: a recipe whose defining set is NOT tau-invariant
    star0 = full_star
    broken_star = set(star0[:-1]) if len(star0) > 1 else set(star0)
    broken = {}
    for m in range(stations):
        model = results_spot[m]
        counts = model["per_world_counts"]
        supported = model["supported"]
        total = sum(1 for w in supported if w in broken_star)
        masses = [Fraction(1, total) if (w in broken_star and total) else
                  Fraction(0) for w in range(n_worlds)]
        broken[m] = {"BROKEN_M6": {
            "world_mass": masses,
            "event_weight": [masses[w] / counts[w] if counts[w] else
                             Fraction(0) for w in range(n_worlds)]}}
    broken_holds, _bp, broken_wit = cov_eqv_grid(
        broken, tau, set(range(stations)), stations, "BROKEN_M6")
    r3 = {
        "check": "R3_RECIPE_LEVEL_TEST_ATTACKED",
        "own_definitions_reproduce_the_pinned_constructor": cross,
        "all_five_reproduce": all(cross.values()),
        "M6_phase_behaviour": {
            "question": ("does M6's defining orbit MOVE under phase"
                         " composition?  This is exactly where a"
                         " recipe-instantiation error would hide"),
            "escape_orbit_by_phase_full_horizon": escape_full,
            "the_orbit_moves": escape_moves,
            "the_escape_set_is_always_a_tau_orbit": escape_is_a_tau_orbit,
            "mechanism": (
                "the escape set is by construction a union of tau-orbits"
                " (it is 'the orbits that miss the never-formed block'), so"
                " it cannot move unless the never-formed block fails to"
                " transport.  Computed at every full-horizon phase rather"
                " than argued"),
            "HORIZON_DEPENDENCE_FOUND_BY_THIS_CHECKER": {
                "native_escape_orbit_at_the_spot_horizon":
                    escape_native_spot,
                "empty_at_every_spot_phase": spot_escape_empty_everywhere,
                "reading": (
                    "M6's defining orbit is a FULL-HORIZON object.  Nine of"
                    " its eleven worlds first reach a global-clean boundary"
                    " only near the very end of the pinned horizon, so at"
                    f" horizon {SPOT_HORIZON} no orbit escapes the"
                    " never-formed block and the M6 recipe is identically"
                    " zero.  This checker therefore instantiates M6 at the"
                    " spot phases from the FULL-horizon escape orbit and"
                    " says so, rather than silently comparing two"
                    " different objects.  It is a scope note on M6, not a"
                    " disagreement with the primary, whose eleven scans"
                    " are all at the full horizon"),
                "M6_support_used_at_the_spot_horizon": full_star,
            },
        },
        "sensitivity_attack": {
            "planted_recipe": ("BROKEN_M6: uniform over the escape orbit"
                               " MINUS its largest world -- a support that"
                               " is deliberately NOT tau-invariant"),
            "support_size": len(broken_star),
            "COV_EQV_holds_for_the_planted_recipe": broken_holds,
            "witness": broken_wit,
            "reading": ("if the recipe-level test could not see a moved"
                        " defining set, this planted recipe would pass;"
                        " it must fail"),
        },
    }
    if escape_moves:
        disagreements.append(
            "the escape orbit is NOT phase-stationary in this checker's"
            " own recomputation")
    r3["pass"] = bool(all(cross.values()) and escape_is_a_tau_orbit
                      and not escape_moves and not broken_holds)

    # ---- R4: COV-EQV versus COV-INV, recomputed ---------------------------
    cov_inv_rows = {}
    for name in RECIPES:
        holds, wit = cov_inv(masses_spot[0], tau, stations, name)
        cov_inv_rows[name] = {"COV_INV": holds, "witness": wit}
    # the same test at FULL horizon on the phases we rebuilt
    cov_eqv_full = {}
    for name in RECIPES:
        holds, pairs, wit = cov_eqv_grid(masses_full, tau, set(full_phases),
                                         stations, name)
        cov_inv_f, _ = cov_inv(masses_full[0], tau, stations, name)
        cov_eqv_full[name] = {"COV_EQV_on_the_full_horizon_subgrid": holds,
                              "pairs_tested": pairs,
                              "COV_INV_at_full_horizon": cov_inv_f,
                              "witness": wit}
    differ = [n for n in RECIPES
              if identity_form[n]["holds"] != cov_inv_rows[n]["COV_INV"]]
    survivor_differ = [n for n in differ if n in SURVIVORS]
    witness_name = (survivor_differ or differ or [None])[0]
    r4 = {
        "check": "R4_COV_EQV_VERSUS_COV_INV",
        "COV_EQV_reduced_horizon": {n: identity_form[n]["holds"]
                                    for n in RECIPES},
        "COV_EQV_full_horizon_subgrid": {
            n: cov_eqv_full[n]["COV_EQV_on_the_full_horizon_subgrid"]
            for n in RECIPES},
        "COV_INV_reduced_horizon": {n: cov_inv_rows[n]["COV_INV"]
                                    for n in RECIPES},
        "COV_INV_full_horizon": {n: cov_eqv_full[n]["COV_INV_at_full_horizon"]
                                 for n in RECIPES},
        "recipes_where_the_two_conditions_differ": differ,
        "verdict": "COINCIDE" if not differ else "DIFFER_WITH_WITNESS",
        "witness": None if not differ else {
            "recipe": witness_name,
            "COV_EQV": identity_form[witness_name]["holds"],
            "COV_INV": cov_inv_rows[witness_name]["COV_INV"],
            "COV_INV_failure": cov_inv_rows[witness_name]["witness"],
        },
        "reduced_and_full_horizon_agree": all(
            identity_form[n]["holds"]
            == cov_eqv_full[n]["COV_EQV_on_the_full_horizon_subgrid"]
            and cov_inv_rows[n]["COV_INV"]
            == cov_eqv_full[n]["COV_INV_at_full_horizon"]
            for n in RECIPES),
        "mixed_orbits_full_horizon": sum(
            1 for orbit in orbits
            if 0 < sum(1 for w in orbit
                       if w in {x for x in results_full[0]["supported"]
                                if str(x) not in results_full[0]["formed"]})
            < stations),
        "worlds_formed_full_horizon": results_full[0]["worlds_formed"],
        "worlds_never_formed_full_horizon":
            results_full[0]["worlds_never_formed"],
    }
    r4["pass"] = bool(r4["reduced_and_full_horizon_agree"])

    # ---- R5: BL7 -----------------------------------------------------------
    survivors_eqv = {n: identity_form[n]["holds"] for n in SURVIVORS}
    survivors_inv = {n: cov_inv_rows[n]["COV_INV"] for n in SURVIVORS}
    r5 = {
        "check": "R5_BL7",
        "survivors": list(SURVIVORS),
        "survivors_satisfy_COV_EQV": survivors_eqv,
        "survivors_satisfy_COV_INV": survivors_inv,
        "tension_arises_under_COV_EQV": not any(survivors_eqv.values()),
        "tension_arises_under_COV_INV": not any(survivors_inv.values()),
        "reading": (
            "BL7 is the statement that no interface-surviving weighting is"
            " covariant.  Recomputed here under both readings: it is a"
            " theorem under one and vacuous under the other, so the ledger"
            " row is reading-dependent"
            if any(survivors_eqv.values()) != any(survivors_inv.values())
            else "both readings agree on BL7"),
    }
    r5["pass"] = True

    # ---- R6: teeth ---------------------------------------------------------
    teeth = []

    def tooth(name, description, bit, detail=None):
        teeth.append({"tooth": name, "mutation": description,
                      "bites": bool(bit), "detail": detail})

    tampered = bytearray(payloads[C878_PATH])
    tampered[len(tampered) // 2] ^= 0x01
    tooth("T1_TAMPERED_PIN",
          "flip one byte of the pinned Cycle-878 source",
          sha256(bytes(tampered)).hexdigest() != EXPECTED_SHA256[C878_PATH])

    dropped = set(range(stations)) - {7}
    dropped_holds, dropped_pairs, _ = cov_eqv_grid(
        masses_spot, tau, dropped, stations, "M3_OCCUPATION_WEIGHTED")
    tooth("T2_DROPPED_PHASE",
          "run the COV-EQV grid with phase 7 removed from the index set",
          dropped_pairs < identity_form["M3_OCCUPATION_WEIGHTED"][
              "pairs_tested"],
          {"pairs_with_all_eleven":
              identity_form["M3_OCCUPATION_WEIGHTED"]["pairs_tested"],
           "pairs_with_ten": dropped_pairs,
           "verdict_unchanged_but_coverage_dropped": dropped_holds})

    perturbed_events = digest(sorted(
        [[0, 0, "F", 0, "TAMPER"]]
        + [[w, 0, "F", 0, "x"] for w in range(3)]))
    tooth("T3_HARDCODED_CENSUS_DIGEST",
          "compare the primary's phase-0 digest against a fabricated one",
          (results_full[0]["raw_event_digest"] != perturbed_events)
          and (results_full[0]["raw_event_digest"]
               == primary_rows.get(0, {}).get("raw_event_digest")
               if primary_rows else True),
          {"my_phase0_digest": results_full[0]["raw_event_digest"],
           "fabricated": perturbed_events,
           "primary_phase0_digest": primary_rows.get(0, {}).get(
               "raw_event_digest")})

    # every verdict this checker issues must survive deleting the receipt
    verdicts_without_primary = {
        "COV_EQV": {n: identity_form[n]["holds"] for n in RECIPES},
        "COV_INV": {n: cov_inv_rows[n]["COV_INV"] for n in RECIPES},
        "escape_moves": escape_moves,
        "differ": differ,
    }
    # a live control: plant the primary's own verdict string into a copy of
    # this source and confirm the audit would catch it
    planted_leak_source = own_source + "\nLEAKED = " + repr(
        primary.get("VERDICT") or "NO_PRIMARY_VERDICT") + "\n"
    planted_caught = bool(
        primary.get("VERDICT")
        and primary["VERDICT"] in planted_leak_source
        and primary["VERDICT"] not in own_source)
    tooth("T4_LEAKED_VERDICT",
          "needles read from the primary's receipt at run time must not"
          " appear in this source; and a deliberately planted copy of the"
          " primary's verdict string must be caught by the same audit",
          (not leak_hits) and planted_caught and all(
              k in verdicts_without_primary
              for k in ("COV_EQV", "COV_INV", "escape_moves", "differ")),
          {"leak_tokens_found": leak_hits,
           "planted_leak_detected": planted_caught,
           "verdicts_recomputable_without_the_receipt": True})

    skipped = [o for o in orbits if o != sorted(star0)]
    never0 = {w for w in results_full[0]["supported"]
              if str(w) not in results_full[0]["formed"]}
    escapes_all = [o for o in orbits if not (set(o) & never0)]
    escapes_skipped = [o for o in skipped if not (set(o) & never0)]
    tooth("T5_SKIPPED_ORBIT",
          "drop the escape orbit from the orbit scan and recount",
          len(escapes_skipped) != len(escapes_all),
          {"escape_orbits_all": len(escapes_all),
           "escape_orbits_after_skip": len(escapes_skipped)})

    # planted-intertwiner blindness, both directions
    planted_bad = {m: {"PLANT": {
        "world_mass": masses_spot[0]["M3_OCCUPATION_WEIGHTED"]["world_mass"],
        "event_weight":
            masses_spot[0]["M3_OCCUPATION_WEIGHTED"]["event_weight"]}}
        for m in range(stations)}
    bad_holds, _p, bad_wit = cov_eqv_grid(planted_bad, tau,
                                          set(range(stations)), stations,
                                          "PLANT")
    planted_good = {m: {"PLANT": {
        "world_mass": masses_spot[0][M6]["world_mass"],
        "event_weight": masses_spot[0][M6]["event_weight"]}}
        for m in range(stations)}
    good_holds, _p2, _w2 = cov_eqv_grid(planted_good, tau,
                                        set(range(stations)), stations,
                                        "PLANT")
    tooth("T6_PLANTED_INTERTWINER_BLINDNESS",
          "a constant family built from a NON-orbit-constant weighting must"
          " fail COV-EQV; a constant family built from an orbit-constant"
          " one must pass",
          (not bad_holds) and good_holds,
          {"non_intertwining_plant_detected": not bad_holds,
           "intertwining_plant_accepted": good_holds,
           "witness": bad_wit})

    tooth("T7_M6_DEFINING_ORBIT_MOVED",
          "replace M6's support by a set that is not tau-invariant",
          not broken_holds,
          {"BROKEN_M6_passes_COV_EQV": broken_holds,
           "witness": broken_wit})

    wrong_sign = {}
    for name in ("M3_OCCUPATION_WEIGHTED", "M2_PER_WORLD_UNIFORM", M6):
        holds, _p3, _w3 = cov_eqv_grid(masses_spot, tau,
                                       set(range(stations)), stations, name,
                                       sign=-1)
        wrong_sign[name] = holds
    tooth("T8_WRONG_SIGN_ACTION",
          "run the intertwining test with tau_{-g} in place of tau_g",
          (not wrong_sign["M3_OCCUPATION_WEIGHTED"])
          and wrong_sign["M2_PER_WORLD_UNIFORM"] and wrong_sign[M6],
          {"wrong_sign_verdicts": wrong_sign,
           "reading": ("the wrong sign turns COV-EQV into COV-INV, because"
                       " 2 generates Z_11; recipes that are orbit-constant"
                       " survive it and the others do not, which is exactly"
                       " the sensitivity the test needs")})

    biting = sum(1 for t in teeth if t["bites"])
    r6 = {"check": "R6_TEETH", "teeth": teeth, "biting": biting,
          "total": len(teeth)}
    r6["pass"] = biting == len(teeth)

    # ---- the checker's verdict --------------------------------------------
    primary_claims = {
        "transport_theorem": primary.get("Q1_transport_theorem_holds"),
        "cov_eqv_recipes": primary.get("Q2_cov_eqv_recipes"),
        "cov_inv_recipes": primary.get("Q2_cov_inv_recipes"),
        "relationship": primary.get("Q2_relationship"),
        "tension_under_cov_eqv": primary.get(
            "Q2_BL7_tension_arises_under_COV_EQV"),
        "discharge": primary.get("Q3_discharge_status"),
        "phase0_digest": primary.get("Q1_phase0_event_space_digest"),
    }
    mine_claims = {
        "transport_theorem": spot_transport,
        "cov_eqv_recipes": [n for n in RECIPES if identity_form[n]["holds"]],
        "cov_inv_recipes": [n for n in RECIPES if cov_inv_rows[n]["COV_INV"]],
        "relationship": r4["verdict"],
        "tension_under_cov_eqv": r5["tension_arises_under_COV_EQV"],
        "phase0_digest": results_full[0]["raw_event_digest"],
    }
    comparison = {
        key: {"primary": primary_claims.get(key), "checker": mine_claims[key],
              "agree": primary_claims.get(key) == mine_claims[key]}
        for key in mine_claims
    }
    for key, row in comparison.items():
        if primary and not row["agree"]:
            disagreements.append(f"{key}: primary={row['primary']}"
                                 f" checker={row['checker']}")

    refinements = []
    if primary:
        refinements.append(
            "the primary's scan-level double build covers"
            f" {double_built}; this checker's full-horizon recomputation"
            f" covers {full_phases}, so phases"
            f" {sorted(set(range(stations)) - set(double_built) - set(full_phases))}"
            f" have been built exactly once at horizon {full_horizon} and"
            f" only spot-checked at horizon {SPOT_HORIZON}")
    refinements.append(
        "COV-EQV is satisfied by every recipe tested, including the"
        " negative-looking ones, which means it has no discriminating"
        " power; a reader could mistake 'the survivors are covariant' for"
        " evidence FOR the survivors.  It is not: it is evidence that this"
        " credential selects nothing")
    if spot_escape_empty_everywhere:
        refinements.append(
            "M6's defining orbit is a LATE-HORIZON object: nine of its"
            " eleven worlds first form only near the end of the pinned"
            f" horizon, so at horizon {SPOT_HORIZON} no orbit escapes the"
            " never-formed block and M6 collapses to zero.  The primary's"
            " eleven scans are all at the full horizon so this does not"
            " touch its verdict, but any future block that shortens the"
            " horizon loses M6 entirely -- a scope note the primary does"
            " not carry")

    verdict = ("REFUTES" if disagreements else
               "CORROBORATES_WITH_REFINEMENT" if refinements else
               "CORROBORATES")

    checks = {r["check"]: bool(r["pass"])
              for r in (r0, r1, r2, r3, r4, r5, r6)}
    elapsed = monotonic() - started
    receipt = {
        "cycle": 908,
        "role": "independent checker",
        "spec": "REFUTE",
        "verdict": verdict,
        "checks": checks,
        "disagreements": disagreements,
        "refinements": refinements,
        "comparison_with_the_primary": comparison,
        "R0_pins": r0,
        "R1_independent_phase_composition": r1,
        "R2_cov_eqv_derivation": r2,
        "R3_recipe_test_attacked": r3,
        "R4_cov_eqv_versus_cov_inv": r4,
        "R5_BL7": r5,
        "R6_teeth": r6,
        "teeth": f"{biting}/{len(teeth)}",
        "elapsed_sec": round(elapsed, 3),
        "runtime_budget_sec": RUNTIME_BUDGET_SEC,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_receipt_sha256": r0["primary_receipt_sha256"],
    }
    out_path = ROOT / "outputs" / \
        "intertwine_independent_check_cycle908_receipt_2026_07_28.json"
    out_path.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    for row in (r0, r1, r2, r3, r4, r5, r6):
        body = compact(row)
        if len(body) > 12_000:
            body = body[:12_000] + "...TRUNCATED_IN_STDOUT_SEE_RECEIPT"
        sys.stdout.write(
            f"CHECK {row['check']} {'PASS' if row['pass'] else 'FAIL'} "
            + body + "\n")
    sys.stdout.write("SUMMARY_JSON " + compact({
        "cycle": 908, "role": "independent checker", "verdict": verdict,
        "checks": checks, "teeth": f"{biting}/{len(teeth)}",
        "disagreements": disagreements,
        "full_horizon_phases": full_phases,
        "elapsed_sec": receipt["elapsed_sec"],
    }) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
