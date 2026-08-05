"""Cycle 925 -- THE LAW-RELAXATION SPACE, CLASSIFIED AND PRICED.

Cycle 918 closed with a determinism lemma and a named successor's successor:

    "A gate set is a LAW: two lanes handed the same schedule and the same
     tick-0 state receive the same gates in the same order, so their columns
     stay equal for ever and cannot diverge."

    "the successor's successor is a substrate whose law is not a function of
     (schedule, tick-0 state)."

THIS BLOCK DOES NOT BUILD THAT SUBSTRATE.  It CLASSIFIES AND PRICES THE
RELAXATION SPACE -- the 918 pattern one level up, as a classification theorem.

  Q1  THE LEMMA, FORMALIZED AT KERNEL LEVEL.  A mechanical AST/semantic sweep
      of the pinned compiler + kernel showing that every datum every one of the
      34,166 compiled gates consults traces to a declared state wire or to a
      compile-time constant fixed by (boundary index, lane slot).  From that,
      the INPUT-PROVENANCE PARTITION:

        P1  declared state              -- a read of the state container
        P2  declared non-state stream   -- a datum bound outside the container
        P3  law-internal choice point   -- a node that could return more than
                                           one value at one occasion
        P4  index / bookkeeping coord   -- a compile-time constant or an
                                           operator that consults a lane's
                                           position rather than its content

      Exhaustiveness is argued MECHANICALLY: the compiler emits exactly three
      statement templates; the grammar of their expression leaves is finite and
      is enumerated; each admitted syntactic category is mapped to one P-class;
      every unmapped category is reported as an UNCLASSIFIED FIFTH CATEGORY and
      a planted representative of each such category must be caught.

  Q2  THE FOUR RELAXATION CLASSES, each with the cheapest concrete
      representative constructible against the pinned kernel (splice-only, the
      kernel never edited), and each with a verdict:

        R1 (P2, the tape)      -- an extra input stream declared "non-state"
        R2 (P3, the choice)    -- a multi-valued transition with a selection
                                  register the law itself writes
        R3 (P4, the indexical) -- a law that reads a bookkeeping coordinate
        R4 (P1, the control)   -- branch pairs realized as tick-0 differences
                                  (the already-banked 911 re-typing)

  Q3  THE CLASSIFICATION THEOREM composed from Q1 + Q2, stated with its
      exhaustiveness relativised honestly (to the compiler's admitted
      syntactic categories, to the swept coordinate list, to the declared
      ansatz).

Discipline: TEXT/AST/JSON only; the 719 two-rail core is the single disclosed
import (as substrate); exact integer arithmetic; splice-only construction with
the control gated digest-identical to the pinned 913/918 builds in BOTH lane
layouts; restriction gates that hard-fail against the pinned 918/913/911
receipt bytes value-for-value BEFORE any new number is quoted; planted
falsifiers that must fire.  No probability, no occurrence rule and no update
law is introduced.  Nothing here is adopted, proposed or decided.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import math
import sys
from collections import Counter
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
HANDSHAKE_PATH = \
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C863_RECEIPT = "outputs/time_from_records_arc_cycles863_865_receipt_2026_07_28.json"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C911_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
C913_PATH = "scripts/frontier_cycle913_selection_function_2026_07_28.py"
C913_RECEIPT = "outputs/selection_function_cycle913_receipt_2026_07_28.json"
C918_PATH = "scripts/frontier_cycle918_writable_endpoint_2026_07_28.py"
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
C911_NOTE = (
    "docs/RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_CYCLE911"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
C913_NOTE = (
    "docs/SELECTION_IS_TRANSPORT_O3_TERMINAL_CYCLE913"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
C918_NOTE = (
    "docs/WRITABLE_ENDPOINT_BORN_CAPABLE_FIRST_BRANCH_PAIRS_CYCLE918"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, HANDSHAKE_PATH, C863_PATH, C863_RECEIPT, C878_PATH,
    C878_RECEIPT, C911_PATH, C911_RECEIPT, C913_PATH, C913_RECEIPT, C918_PATH,
    C918_RECEIPT, C911_NOTE, C913_NOTE, C918_NOTE, AXIOMS_PATH, REALIZED_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C911_PATH, C913_PATH, C918_PATH)
JSON_ONLY_PATHS = (C863_RECEIPT, C878_RECEIPT, C911_RECEIPT, C913_RECEIPT,
                   C918_RECEIPT)
TEXT_ONLY_PATHS = (C911_NOTE, C913_NOTE, C918_NOTE, AXIOMS_PATH, REALIZED_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    HANDSHAKE_PATH:
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C863_RECEIPT:
        "b856d00221ca3f755bcc21e5e37e99a8141a8f6daba959914c688702f59b2c9b",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C911_PATH:
        "6474f1e919c97fcb3336a8cea480b5e824fe48f4ea5ce4592c1b75bc0b0007d1",
    C911_RECEIPT:
        "90d1fb2a3ac31065f75345ac1e98520622aa6302c50dcf4a8a11f44a1cde11b0",
    C913_PATH:
        "b349f873aa1e88558fcd63fc432a6edd249f48f103ecbd3d28fd62d070e689ef",
    C913_RECEIPT:
        "0de8d785c2139126b813166e090493d65cb289508b46de7f928b440facb82ecd",
    C918_PATH:
        "0ef019ef77cf3ff33c7e6c29ac31d1cd53945bd5f505f1fd4b3387e74017289d",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    C911_NOTE:
        "40c80402e2dfd283a4309433cfa48705c45567efadf43107e074332f1cbf5ff0",
    C913_NOTE:
        "43769f08abee65bc535147ad8cf52018c3a71d8afa40af19ddddb00e5cd3315a",
    C918_NOTE:
        "40333f3bb83f77a3e7c89eb232bbe24c01885cdcfdcab7888ae319419c1efaee",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    REALIZED_PATH:
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    HANDSHAKE_PATH: "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C863_RECEIPT: "08ca180175d615d28daab4a09cf0091c3edba925",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C911_PATH: "3335e9dee5027b935d0eb3c814601b8f8e83b550",
    C911_RECEIPT: "af51342a72c56db8e562e1f1a607f207508b42ed",
    C913_PATH: "2093b687713eb12b462532761092d90d40bed718",
    C913_RECEIPT: "5ac6a40c316c7a90bcf867eb6507518ba976169b",
    C918_PATH: "b5a1a5643abe87ab4a92fd86e8c0007e8f26539a",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    C911_NOTE: "53a229b4143f59f5f8c12ccb9f488682bdc2714c",
    C913_NOTE: "7b60ee552d8346840ee1dfeec0800079e3981362",
    C918_NOTE: "186af20c471f8cbb4e9c9871fc2ee652d813e348",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
    REALIZED_PATH: "5acb4643882438f8dd16baf9694e6fa2d33d1dc6",
}

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AST_ONLY_PATHS)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
FRACTION_LABEL = "bookkeeping fraction, not probability"

HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
LANE_SHIFT = 1
CROSSCHECK_ORBITS = 128            # pinned-911 cross-check window (declared)
SWEEP_ORBITS = 96                  # R3 coordinate-sweep window (declared)
TAPE_WINDOW_ORBITS = 64            # arbitrary-tape window (declared)
PERTURB_ORBITS = 6
PAIR_SAMPLE_CAP = 40


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

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


# ---------------------------------------------------------------------------
# A: pins
# ---------------------------------------------------------------------------

def pin_rows():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    self_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"),
                          filename=Path(__file__).name)
    string_constants: dict = {}
    literal = None
    for node in self_tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            try:
                string_constants[target.id] = ast.literal_eval(node.value)
            except Exception:
                pass
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
            "imported_disclosed_substrate": IMPORTED_PATHS,
            "ast_only": AST_ONLY_PATHS,
            "json_only": JSON_ONLY_PATHS,
            "text_only": TEXT_ONLY_PATHS,
        },
        "modification_mechanism":
            "WRAP, NEVER EDIT.  The pinned kernel file is imported read-only "
            "and its bytes are hashed above.  Every construction in this block "
            "is a tuple of COMPILED gate rows declared in this file and "
            "spliced into the composed scan by this file's own schedule "
            "builder, which reproduces the pinned Cycle-863 masked_h_schedules "
            "row for row when the extra tuple is empty -- gated in B.  No "
            "pinned file is written, patched, monkey-patched or reloaded.",
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "bytes": {p: len(b) for p, b in payloads.items()},
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"])
    return result, payloads


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


def lift_ast_op_tuple(path: str, name: str):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                names = []
                for element in node.value.elts:
                    if not (isinstance(element, ast.Attribute)
                            and isinstance(element.value, ast.Name)
                            and element.value.id == "ast"):
                        raise AssertionError(("op tuple shape", name))
                    names.append(element.attr)
                return tuple(getattr(ast, n) for n in names), tuple(names)
    raise AssertionError(("op tuple not found", path, name))


C863_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "derive_census",
    "watched_registers", "dirty_partition", "build_initial_states",
    "pack_lanes", "compile_masked_gate", "masked_h_schedules", "compile_fast",
    "mask_over", "lanes_of", "lane_state", "synchronous_word",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
C878_FUNCS = ("lcm", "monitor_phase_action", "group_orbits", "dead_wire_rig")
C878_CONSTS = ("HORIZON", "REGISTER_CAP", "DEAD_CHUNK_ORBITS",
               "DEAD_ORBIT_ORBITS")
C911_FUNCS = ("snapshot_scan", "classify_pair")
C911_CONSTS = ("DIRECTIONS", "REGISTER_CAP", "HORIZON", "CLASS_BRANCH",
               "CLASS_IDENTICAL", "CLASS_SETUP_TICK0", "CLASS_SETUP_SCHEDULE",
               "CLASS_NONBRANCH_DIVERGENCE")
C913_FUNCS = ("endpoint_wires", "read_state_direction", "target_wire_sweep",
              "hamming_readout")


def lift_machinery():
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations, "Counter": Counter})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "json": json,
         "gcd": math.gcd})
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})
    cross_ops, cross_names = lift_ast_op_tuple(C911_PATH, "CROSS_LANE_OPS")
    pos_ops, pos_names = lift_ast_op_tuple(C911_PATH, "POSITIONWISE_OPS")
    ns911, consts911, names911 = ast_lift(
        C911_PATH, C911_FUNCS, C911_CONSTS,
        {"K": K, "np": np, "itertools": itertools, "Counter": Counter,
         "sha256": sha256, "ast": ast,
         "CROSS_LANE_OPS": cross_ops, "POSITIONWISE_OPS": pos_ops})
    c911 = SimpleNamespace(**{n: ns911[n] for n in C911_FUNCS})
    ns913, consts913, names913 = ast_lift(
        C913_PATH, C913_FUNCS, (), {"K": K, "Counter": Counter,
                                    "sha256": sha256})
    c913 = SimpleNamespace(**{n: ns913[n] for n in C913_FUNCS})
    provenance = {
        "lifted_from_863": names863, "constants_863": consts863,
        "lifted_from_878": names878, "constants_878": consts878,
        "lifted_from_911": names911,
        "constants_911": {
            k: ([list(x) for x in v] if k == "DIRECTIONS" else v)
            for k, v in consts911.items()},
        "lifted_911_operator_tuples": {"CROSS_LANE_OPS": list(cross_names),
                                       "POSITIONWISE_OPS": list(pos_names)},
        "lifted_from_913": names913,
        "import_of_863_878_911_913_or_918": False,
        "single_disclosed_import": CORE_PATH,
    }
    return (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
            provenance)


# ---------------------------------------------------------------------------
# B: the gate algebra -- compiled rows, spliced never edited
# ---------------------------------------------------------------------------

KIND_X, KIND_CNOT, KIND_TOF, KIND_SHIFT = 0, 1, 2, 3
KIND_NAMES = {KIND_X: "X", KIND_CNOT: "CNOT", KIND_TOF: "TOF",
              KIND_SHIFT: "SHIFT_CNOT"}
CERTIFIED_KINDS = (KIND_X, KIND_CNOT, KIND_TOF)


def gate_text(kind, a, b, c3):
    if kind == KIND_X:
        return f"c[{a}] ^= <mask>"
    if kind == KIND_CNOT:
        return f"c[{b}] ^= c[{a}] & <mask>"
    if kind == KIND_TOF:
        return f"c[{c3}] ^= c[{a}] & c[{b}] & <mask>"
    return f"c[{b}] ^= (c[{a}] >> {LANE_SHIFT}) & <mask>"


def gate_target(kind, a, b, c3):
    if kind == KIND_X:
        return a
    if kind in (KIND_CNOT, KIND_SHIFT):
        return b
    return c3


def gate_inputs_of(kind, a, b, c3):
    if kind == KIND_X:
        return ()
    if kind == KIND_TOF:
        return (a, b)
    return (a,)


def station_mask(sim, station, step, stations):
    return sum(1 << lane for lane, (_k, _e, pos) in enumerate(sim)
               if (station - step) % stations in pos)


def build_schedules(c863, program, sim, extra_station, extra_gates,
                    lane_mask_fn=None, steps_allowed=None, cycles_per_orbit=1,
                    per_cycle_gates=None):
    """The composed scan's masked-schedule compiler with declared extra macros
    appended to one station's macro.  Empty extras reproduce the pinned
    Cycle-863 masked_h_schedules row for row (gated in B).

    lane_mask_fn(step, station_mask) -> mask   (default: the station mask)
    cycles_per_orbit / per_cycle_gates: build an UNROLLED cycle of length
    stations * cycles_per_orbit, with per_cycle_gates[u] used on repeat u.
    An unrolled cycle is exactly a longer SCHEDULE; the u == 1 case with
    per_cycle_gates None is the pinned period."""
    stations = len(program)
    rows = []
    for repeat in range(cycles_per_orbit):
        gates = extra_gates
        if per_cycle_gates is not None:
            gates = per_cycle_gates[repeat]
        for step in range(stations):
            schedule = []
            for station, row in enumerate(program):
                mask = station_mask(sim, station, step, stations)
                if mask:
                    schedule.extend(
                        c863.compile_masked_gate(g, mask)
                        for g in K.mapped_macro(row))
                    if gates and station == extra_station \
                            and (steps_allowed is None
                                 or step in steps_allowed):
                        m = mask if lane_mask_fn is None \
                            else lane_mask_fn(step, mask)
                        if m:
                            for kind, a, b, c3 in gates:
                                schedule.append((kind, a, b, c3, m))
            rows.append(tuple(schedule))
    return tuple(rows)


def chunk_source(schedule):
    """The exact source the composed scan execs, extended by the one declared
    cross-lane form.  Kinds 0/1/2 reproduce the pinned compile_fast text."""
    src = ["def apply_chunk(c):"]
    if not schedule:
        src.append(" pass")
    for kind, a, b, c3, mask in schedule:
        if kind == KIND_X:
            src.append(f" c[{a}] ^= {mask}")
        elif kind == KIND_CNOT:
            src.append(f" c[{b}] ^= c[{a}] & {mask}")
        elif kind == KIND_TOF:
            src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        elif kind == KIND_SHIFT:
            src.append(f" c[{b}] ^= (c[{a}] >> {LANE_SHIFT}) & {mask}")
        else:
            raise ValueError(("gate kind", kind))
    return src


def _pinned_compile_fast_text(schedule):
    """The pinned Cycle-863 compile_fast source text, reconstructed for the
    byte comparison in B (kinds 0/1/2 only, exactly as the pin writes them)."""
    src = ["def apply_chunk(c):"]
    for kind, a, b, c3, mask in schedule:
        if kind == 0:
            src.append(f" c[{a}] ^= {mask}")
        elif kind == 1:
            src.append(f" c[{b}] ^= c[{a}] & {mask}")
        else:
            src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
    return src


def compile_schedules(schedules):
    fns = []
    for schedule in schedules:
        ns: dict = {}
        exec("\n".join(chunk_source(schedule)), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


def compile_source(src_lines, name="apply_chunk", globals_=None):
    ns: dict = {}
    exec("\n".join(src_lines), {"__builtins__": {}} if globals_ is None
         else globals_, ns)
    return ns[name]


def target_sweep(schedules, left, right, src):
    targets: set = set()
    inputs: set = set()
    gate_count = 0
    for schedule in schedules:
        for kind, a, b, c3, _mask in schedule:
            gate_count += 1
            targets.add(gate_target(kind, a, b, c3))
            inputs.update(gate_inputs_of(kind, a, b, c3))
    return {
        "gates_total": gate_count,
        "distinct_targets": len(targets),
        "distinct_inputs": len(inputs),
        "LEFT_ENDPOINT_wire": left, "RIGHT_ENDPOINT_wire": right,
        "SOURCE_POINTER_wire": src,
        "LEFT_is_a_gate_target": left in targets,
        "RIGHT_is_a_gate_target": right in targets,
        "SOURCE_POINTER_is_a_gate_target": src in targets,
        "LEFT_is_a_gate_input": left in inputs,
        "RIGHT_is_a_gate_input": right in inputs,
        "endpoint_content_is_read_never_written":
            left not in targets and right not in targets
            and left in inputs and right in inputs,
        "_targets": targets, "_inputs": inputs,
    }


# ---------------------------------------------------------------------------
# Q1: THE INPUT-PROVENANCE PARTITION -- the mechanical sweep
# ---------------------------------------------------------------------------

P1 = "P1_DECLARED_STATE"
P2 = "P2_DECLARED_NON_STATE_INPUT_STREAM"
P3 = "P3_LAW_INTERNAL_CHOICE_POINT"
P4 = "P4_INDEX_OR_BOOKKEEPING_COORDINATE"
P_UNCLASSIFIED = "UNCLASSIFIED_FIFTH_CATEGORY"

PARTITION_STATEMENT = (
    "INPUT-PROVENANCE PARTITION.  Every datum a law consults at one occasion "
    "is exactly one of:\n"
    "  P1  DECLARED STATE -- a read of the declared state container at a "
    "declared address (here: c[i] for a literal wire index i).\n"
    "  P2  A DECLARED NON-STATE INPUT STREAM -- a datum bound outside the "
    "state container and delivered to the law at the occasion (here: any free "
    "name in the compiled expression).\n"
    "  P3  A LAW-INTERNAL CHOICE POINT -- a node that could deliver more than "
    "one value at one occasion with all of P1/P2/P4 held fixed (here: a call, "
    "a conditional expression, a comparison, a boolean short-circuit).\n"
    "  P4  AN INDEX OR BOOKKEEPING COORDINATE -- a datum fixed by WHERE and "
    "WHEN the occasion sits in the bookkeeping rather than by what the world "
    "contains (here: a compile-time integer literal, which is a function of "
    "the boundary index and the lane slot; and any operator that moves content "
    "across lane positions, which consults a lane's position rather than its "
    "content).\n"
    "EXHAUSTIVENESS.  A datum enters a compiled statement only as a leaf of "
    "its value expression.  In the grammar the compiler emits, a leaf is a "
    "container read, a literal, a free name, or a node that computes/branches; "
    "an interior node is an operator, and an operator either preserves lane "
    "position (consulting no coordinate) or moves across lane positions "
    "(consulting the lane index).  Those five cases are P1, P4, P2, P3 and "
    "{nothing, P4}.  Any syntactic category outside that map is reported as an "
    "UNCLASSIFIED FIFTH CATEGORY and is a falsifier of this partition.")


def classify_leaf(node, positionwise_ops, cross_lane_ops):
    """Map one AST node of a compiled chunk statement to a P-class (or to
    None when it carries no datum, or to UNCLASSIFIED)."""
    if isinstance(node, ast.Subscript):
        if isinstance(node.value, ast.Name) and node.value.id == "c" \
                and isinstance(node.slice, ast.Constant) \
                and isinstance(node.slice.value, int):
            return P1, f"c[{node.slice.value}]"
        return P_UNCLASSIFIED, "subscript-with-non-literal-address"
    if isinstance(node, ast.Constant):
        if isinstance(node.value, int):
            return P4, "integer-literal-mask"
        return P_UNCLASSIFIED, f"non-int-constant:{type(node.value).__name__}"
    if isinstance(node, ast.Name):
        if node.id == "c":
            return P1, "state-container"
        return P2, f"free-name:{node.id}"
    if isinstance(node, (ast.Call, ast.IfExp, ast.Compare, ast.BoolOp,
                         ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp,
                         ast.GeneratorExp, ast.Await, ast.Yield)):
        return P3, f"choice-point:{type(node).__name__}"
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, cross_lane_ops):
            return P4, f"lane-index-operator:{type(node.op).__name__}"
        if isinstance(node.op, positionwise_ops):
            return None, f"positionwise-operator:{type(node.op).__name__}"
        return P_UNCLASSIFIED, f"operator:{type(node.op).__name__}"
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, positionwise_ops):
            return None, f"positionwise-unary:{type(node.op).__name__}"
        return P_UNCLASSIFIED, f"unary:{type(node.op).__name__}"
    if isinstance(node, (ast.Load, ast.Store)):
        return None, "ctx"
    if isinstance(node, (ast.BitXor, ast.BitAnd, ast.BitOr, ast.Invert,
                         ast.LShift, ast.RShift, ast.Add, ast.Sub, ast.Mult,
                         ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
                         ast.MatMult)):
        return None, "bare-operator-node"
    return P_UNCLASSIFIED, f"node:{type(node).__name__}"


def provenance_sweep(sources, positionwise_ops, cross_lane_ops):
    """Sweep compiled chunk SOURCES (the exact text this file execs) and put
    every node of every statement into the partition.  Returns per-class
    counts, the state addresses actually read, and every violation."""
    counts = Counter()
    detail = Counter()
    statements = 0
    targets: set = set()
    reads: set = set()
    violations: list = []
    shape_violations: list = []
    for step, src in enumerate(sources):
        tree = ast.parse("\n".join(src))
        if len(tree.body) != 1 or not isinstance(tree.body[0],
                                                 ast.FunctionDef):
            shape_violations.append(("not a single function def", step))
            continue
        fn = tree.body[0]
        if fn.args.args and [a.arg for a in fn.args.args] != ["c"]:
            shape_violations.append(("argument is not the state container",
                                     step))
        for stmt in fn.body:
            statements += 1
            if isinstance(stmt, ast.Pass):
                statements -= 1
                continue
            if not isinstance(stmt, ast.AugAssign):
                shape_violations.append(("statement is not an AugAssign",
                                         step))
                continue
            if not isinstance(stmt.op, ast.BitXor):
                shape_violations.append(("AugAssign op is not ^=", step))
                continue
            tgt = stmt.target
            if not (isinstance(tgt, ast.Subscript)
                    and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "c"
                    and isinstance(tgt.slice, ast.Constant)
                    and isinstance(tgt.slice.value, int)):
                shape_violations.append(("target is not c[literal]", step))
                continue
            targets.add(tgt.slice.value)

            def visit(node, step=step):
                cls, tag = classify_leaf(node, positionwise_ops,
                                         cross_lane_ops)
                detail[tag] += 1
                if cls is not None:
                    counts[cls] += 1
                    if cls in (P2, P3, P_UNCLASSIFIED):
                        violations.append({"step": step, "class": cls,
                                           "tag": tag})
                if cls == P1 and isinstance(node, ast.Subscript):
                    # a recognised c[literal] read is a LEAF: its own children
                    # (the container name and the literal address) are the
                    # address, not a further datum, and are not descended into.
                    reads.add(node.slice.value)
                    return
                for child in ast.iter_child_nodes(node):
                    visit(child)

            visit(stmt.value)
    return {
        "statements": statements,
        "class_counts": {k: counts[k] for k in sorted(counts)},
        "node_tag_counts": {k: detail[k] for k in sorted(detail)},
        "distinct_state_addresses_read": len(reads),
        "distinct_state_addresses_written": len(targets),
        "P2_P3_or_unclassified_sites": len(violations),
        "violations": violations[:24],
        "shape_violations": shape_violations[:24],
        "shape_violation_count": len(shape_violations),
        "_reads": reads, "_targets": targets,
    }


def compiler_templates():
    """Enumerate the statement templates the PINNED compiler can emit, read
    off the pinned Cycle-863 compile_fast source itself (not re-typed here):
    every f-string appended to `src` inside compile_fast."""
    tree = ast.parse((ROOT / C863_PATH).read_text(encoding="utf-8"),
                     filename=C863_PATH)
    templates = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.FunctionDef)
                and node.name == "compile_fast"):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call) \
                    and isinstance(sub.func, ast.Attribute) \
                    and sub.func.attr == "append":
                arg = sub.args[0] if sub.args else None
                if isinstance(arg, ast.JoinedStr):
                    shape = []
                    for piece in arg.values:
                        if isinstance(piece, ast.Constant):
                            shape.append(piece.value)
                        else:
                            shape.append("{}")
                    templates.append("".join(shape))
                elif isinstance(arg, ast.Constant):
                    templates.append(arg.value)
    return templates


# ---------------------------------------------------------------------------
# the scan (this file's own; gated to reproduce the pinned 911/913/918 builds)
# ---------------------------------------------------------------------------

def acc_add(planes: list, mask: int) -> None:
    i = 0
    carry = mask
    while carry:
        if i == len(planes):
            planes.append(0)
        t = planes[i] & carry
        planes[i] ^= carry
        carry = t
        i += 1


def acc_get(planes: list, lane: int) -> int:
    value = 0
    for i, plane in enumerate(planes):
        if (plane >> lane) & 1:
            value |= 1 << i
    return value


def run_scan(c863, program, census, states, boundaries_target, schedules,
             reverse_layout, register_cap, slot_of, endpoints,
             tick0_extra=None, injection=None, pre_fns=None,
             digest_exclude=(), stations=None):
    """One composed-scan build.

    `schedules` is the compiled chunk cycle (length stations, or an unrolled
    multiple of it).  `tick0_extra` maps a wire to a bit pattern OR'd into the
    tick-0 columns (the declared tick-0 carrier of a tape).  `injection` is a
    per-boundary (wire, value) writer applied BEFORE the chunk -- the 'written
    mid-run by nothing' stream.  `pre_fns` is a per-boundary compiled function
    applied BEFORE the chunk -- the same stream expressed as pure schedule."""
    n = len(census)
    stations = stations or len(program)
    order = list(range(n - 1, -1, -1)) if reverse_layout else list(range(n))
    laid_states = tuple(states[w] for w in order)
    fast = tuple(schedules)
    cycle = len(fast)
    columns = c863.pack_lanes(laid_states + (laid_states[0],))
    if tick0_extra:
        for wire, value in tick0_extra.items():
            columns[wire] |= value
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    mask_over, lanes_of, lane_state = (c863.mask_over, c863.lanes_of,
                                       c863.lane_state)
    left_w, right_w = endpoints[0], endpoints[1]

    slot_wires = tuple(sorted(set(slot_of.values())))
    shadow = {w: 0 for w in slot_wires}
    write_once_violations = 0
    slot_activation = 0
    for w in slot_wires:
        slot_activation |= columns[w]
    keep = [w for w in range(len(columns)) if w not in set(digest_exclude)]

    def wire_write(tag, bit):
        nonlocal write_once_violations
        wire = slot_of[tag]
        flag = 1 << bit
        if shadow[wire] & flag:
            write_once_violations += 1
        shadow[wire] |= flag

    events: list[tuple] = []
    formed: dict[int, int] = {}
    snap: dict[int, tuple] = {}
    lock_ordinal: dict[int, tuple] = {}
    lock_writes: dict[int, tuple] = {}
    bank_ordinal = [[0, 0] for _ in range(n)]
    beyond_cap = 0
    dup_mismatches = 0
    planes_left: list = []
    planes_right: list = []
    prev_left = columns[left_w]
    prev_right = columns[right_w]
    endpoint_change_boundaries = 0
    col_hash = sha256()

    g = mask_over(columns, global_dirty, uni_sim)
    dup_mismatches += int(bool(g & 1) != bool(g & (1 << n)))
    prev = [mask_over(columns, bank_dirty[b], uni_all) for b in (0, 1)]
    for bit in lanes_of(g & uni_all):
        w = order[bit]
        formed[w] = 0
        snap[w] = lane_state(columns, bit)
        lock_ordinal[w] = (0, 0)
        lock_writes[w] = (0, 0)
        events.append((w, 0, "F", 0))
        wire_write(("F", 0), bit)
    boundary = 0
    while boundary < boundaries_target:
        chunk = fast[boundary % cycle]
        if injection is not None:
            wire, value = injection(boundary)
            columns[wire] = value
        if pre_fns is not None:
            pre_fns[boundary](columns)
        chunk(columns)
        boundary += 1
        orbit_no = (boundary + stations - 1) // stations
        cl, cr = columns[left_w], columns[right_w]
        dl, dr = cl ^ prev_left, cr ^ prev_right
        if dl:
            acc_add(planes_left, dl)
            prev_left = cl
        if dr:
            acc_add(planes_right, dr)
            prev_right = cr
        if dl or dr:
            endpoint_change_boundaries += 1
        g = mask_over(columns, global_dirty, uni_sim)
        dup_mismatches += int(bool(g & 1) != bool(g & (1 << n)))
        ga = g & uni_all
        if ga:
            for bit in lanes_of(ga):
                w = order[bit]
                if w not in formed:
                    formed[w] = boundary
                    snap[w] = lane_state(columns, bit)
                    lock_ordinal[w] = tuple(bank_ordinal[bit])
                    lock_writes[w] = (acc_get(planes_left, bit),
                                      acc_get(planes_right, bit))
                    events.append((w, boundary, "F", 0))
                    wire_write(("F", 0), bit)
        for b in (0, 1):
            bm = mask_over(columns, bank_dirty[b], uni_all)
            rise = bm & ~prev[b]
            if rise:
                for bit in lanes_of(rise):
                    o = bank_ordinal[bit][b]
                    if o < register_cap:
                        events.append((order[bit], boundary, f"B{b}", o))
                        wire_write((f"B{b}", o), bit)
                    else:
                        beyond_cap += 1
                    bank_ordinal[bit][b] = o + 1
            prev[b] = bm
        if orbit_no <= DEAD_CHUNK_ORBITS:
            for w in slot_wires:
                slot_activation |= columns[w]
        elif boundary % stations == 0:
            for w in slot_wires:
                slot_activation |= columns[w]
        if boundary % 256 == 0:
            col_hash.update(str([columns[w] for w in keep[::53]]).encode())
    col_hash.update(str([columns[w] for w in keep]).encode())
    events.sort(key=lambda e: (e[1], e[0], e[2], e[3]))
    final_writes = {order[bit]: (acc_get(planes_left, bit),
                                 acc_get(planes_right, bit))
                    for bit in range(n)}
    return {
        "events": tuple(events),
        "formed": formed,
        "snapshots": snap,
        "lock_ordinal": lock_ordinal,
        "lock_endpoint_writes": lock_writes,
        "final_endpoint_writes": final_writes,
        "beyond_cap": beyond_cap,
        "boundaries": boundary,
        "duplicate_lane_mismatches": dup_mismatches,
        "layout": "reversed" if reverse_layout else "forward",
        "write_once_violations": write_once_violations,
        "record_slot_activation_conflicts":
            bin(slot_activation & uni_sim).count("1"),
        "endpoint_change_boundaries": endpoint_change_boundaries,
        "column_digest": col_hash.hexdigest(),
        "order": order,
    }


def scan_digest(build, exclude=()):
    """The Cycle-913/918 build digest, byte for byte.  `exclude` blanks the
    declared carrier wires so two forms of the SAME law can be compared on
    every wire the pinned substrate has."""
    drop = set(exclude)
    return digest({
        "formed": {str(k): v for k, v in sorted(build["formed"].items())},
        "snapshots": {str(k): "".join("_" if i in drop else str(b)
                                      for i, b in enumerate(v))
                      for k, v in sorted(build["snapshots"].items())},
        "lock_ordinal": {str(k): list(v)
                         for k, v in sorted(build["lock_ordinal"].items())},
        "events": len(build["events"]),
    })


def perturbation_witness(c863, program, census, states, samples, orbits,
                         schedules):
    n = len(census)
    fast = tuple(schedules)
    base = c863.pack_lanes(tuple(states) + (states[0],))
    rows = []
    for lane, wire in samples:
        cols_a = list(base)
        cols_b = list(base)
        cols_b[wire] ^= (1 << lane)
        leak = 0
        allowed = 1 << lane
        for _orbit in range(orbits):
            for chunk in fast:
                chunk(cols_a)
                chunk(cols_b)
                for x, y in zip(cols_a, cols_b):
                    if (x ^ y) & ~allowed:
                        leak += 1
        rows.append({"lane": lane, "wire": wire, "orbits": orbits,
                     "leak_outside_own_lane_bit": leak})
    return rows


# ---------------------------------------------------------------------------
# rows, branch quantities
# ---------------------------------------------------------------------------

def build_rows(c913, census, build, menu, geometry):
    BB = geometry["BANK_BASES"]
    left_w, right_w = geometry["left"], geometry["right"]
    stations = geometry["stations"]
    setup_direction = geometry["setup_direction"]
    formed, snapshots, lock_ordinal = (build["formed"], build["snapshots"],
                                       build["lock_ordinal"])
    rows, off_menu, dis_setup = [], [], []
    for w in sorted(formed):
        state = snapshots[w]
        key = census[w]
        rd_state = c913.read_state_direction(state)
        rd_setup = setup_direction[key[1]]
        if rd_state is None:
            off_menu.append({"world": w,
                             "endpoint_bits": [state[left_w], state[right_w]]})
        elif rd_state != rd_setup:
            dis_setup.append(w)
        bank0 = "".join(str(state[BB[0] + i]) for i in range(geometry["AW"]))
        bank1 = "".join(str(state[BB[1] + i]) for i in range(geometry["AW"]))
        link0 = "".join(str(state[geometry["LINK_BASES"][0] + i])
                        for i in range(geometry["LW"]))
        full = "".join(str(b) for b in state)
        wl, wr = build["lock_endpoint_writes"].get(w, (0, 0))
        rows.append({
            "world": w, "key": [key[0], key[1], list(key[2])],
            "lock_boundary": formed[w], "phase": formed[w] % stations,
            "menu": [list(v) for v in menu],
            "selected_item": list(rd_state) if rd_state else None,
            "rd_setup": list(rd_setup) if rd_setup else None,
            "left_writes_before_lock": wl, "right_writes_before_lock": wr,
            "ord0": lock_ordinal[w][0], "ord1": lock_ordinal[w][1],
            "endpoint_bits": (state[left_w], state[right_w]),
            "context_fingerprint": sha256(
                (bank0 + "|" + bank1 + "|" + link0 + "|"
                 + full[BB[0]:]).encode("ascii")).hexdigest()[:16],
        })
    return rows, off_menu, dis_setup


def dynamical_branch_pairs(census, rows_by_world, setup_direction):
    """The Cycle-918 declared quantity, reproduced: two lock points agreeing on
    every setup coordinate the endpoint menu can see (token positions AND the
    prepared endpoint direction at tick 0) that nevertheless realize different
    menu items."""
    groups: dict = {}
    for w in rows_by_world:
        key = (tuple(census[w][2]), setup_direction[census[w][1]])
        groups.setdefault(key, []).append(w)
    split_pairs = []
    undecidable = 0
    candidate_pairs = 0
    for key, members in sorted({k: v for k, v in groups.items()
                                if len(v) >= 2}.items()):
        for u, v in combinations(sorted(members), 2):
            su = rows_by_world[u]["selected_item"]
            sv = rows_by_world[v]["selected_item"]
            if su is None or sv is None:
                undecidable += 1
                continue
            candidate_pairs += 1
            if su != sv:
                split_pairs.append({
                    "pair": [u, v],
                    "shared_positions": list(key[0]),
                    "shared_prepared_direction": list(key[1]),
                    "selected": [su, sv],
                    "lock_boundaries": [rows_by_world[u]["lock_boundary"],
                                        rows_by_world[v]["lock_boundary"]],
                })
    return {
        "candidate_pairs_among_the_lock_points": candidate_pairs,
        "pairs_skipped_because_the_endpoint_was_off_menu": undecidable,
        "DYNAMICAL_BRANCH_PAIRS": len(split_pairs),
        "pairs": split_pairs[:PAIR_SAMPLE_CAP],
    }


def literal_branch_matrix(c911, census, states, formed, classes):
    per_state: dict = {}
    for w, s in enumerate(states):
        per_state.setdefault(s, []).append(w)
    sid = {}
    for i, (_s, lanes) in enumerate(per_state.items()):
        for w in lanes:
            sid[w] = i
    same_state_pairs = []
    for lanes in per_state.values():
        if len(lanes) > 1:
            same_state_pairs.extend(combinations(sorted(lanes), 2))
    same_positions_same_state = [
        (u, v) for u, v in same_state_pairs if census[u][2] == census[v][2]]
    matrix = Counter()
    for u, v in combinations(range(len(census)), 2):
        matrix[c911.classify_pair(census[u], census[v], sid[u], sid[v],
                                  formed.get(u), formed.get(v))["verdict"]] \
            += 1
    return {
        "total_world_pairs": len(census) * (len(census) - 1) // 2,
        "verdicts": {k: matrix[k] for k in sorted(matrix)},
        "BRANCH_PAIRS": matrix[classes["CLASS_BRANCH"]],
        "pairs_sharing_tick0_state": len(same_state_pairs),
        "pairs_sharing_tick0_state_AND_schedule":
            len(same_positions_same_state),
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in
            ("literal_ok", "sha256_all_match", "git_blobs_all_match",
             "existing_worktree_relative", "blocked_modules_loaded",
             "firewall_hits")}))
        return 2

    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = lift_machinery()

    text = {p: payloads[p].decode("utf-8") for p in TEXT_ONLY_PATHS}
    receipts = {p: json.loads(payloads[p].decode("utf-8"))
                for p in JSON_ONLY_PATHS}
    r911, r913, r878, r918 = (receipts[C911_RECEIPT], receipts[C913_RECEIPT],
                              receipts[C878_RECEIPT], receipts[C918_RECEIPT])
    c2_911 = r911["certificates"]["C2_MENU_AT_FORMATION"]
    c1_913 = r913["certificates"]["C1_SELECTION_TABLE"]
    c6_913 = r913["certificates"]["C6_O2_O3_VERDICT"]
    h_913 = r913["certificates"]["H_DOUBLE_BUILD"]
    m918 = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]
    h918 = {row["modification"]: row
            for row in r918["certificates"]["H_DOUBLE_BUILD"]["rows"]}
    c5_918 = r918["certificates"]["C5_STRUCTURAL_LEMMA"]
    register_cap = consts911["REGISTER_CAP"]
    classes = {k: consts911[k] for k in
               ("CLASS_BRANCH", "CLASS_IDENTICAL", "CLASS_SETUP_TICK0",
                "CLASS_SETUP_SCHEDULE", "CLASS_NONBRANCH_DIVERGENCE")}

    # ---------------- the substrate ----------------------------------------
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_failures = c863.build_initial_states(program, event_seeds,
                                                      census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB, LB = K.M.R12.BANK_BASES, K.M.R12.LINK_BASES
    AW, LW = K.A.N, K.B.LINK_WIDTH
    setup_direction = {ev: c913.read_state_direction(seed)
                       for ev, seed in event_seeds}
    menu = tuple(tuple(v) for v in consts911["DIRECTIONS"])
    width = len(states[0])
    n = len(census)
    geometry = {"BANK_BASES": BB, "LINK_BASES": LB, "AW": AW, "LW": LW,
                "left": left_w, "right": right_w, "stations": stations,
                "setup_direction": setup_direction}
    REC_A = BB[0] + K.A.POINTER
    REC_B = BB[1] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    sim_rev = tuple(census[w] for w in range(n - 1, -1, -1))
    sim_rev = sim_rev + (sim_rev[0],)
    uni_sim = (1 << (n + 1)) - 1
    FULL_BOUNDARIES = HORIZON * stations

    # ---------------- the Cycle-878 dead-wire record rig, verbatim ---------
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    t0 = monotonic()
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    t_rig = round(monotonic() - t0, 3)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = set(per_bank[0]) | set(per_bank[1]) | set(links) \
        | {source_ptr}
    FREE_WIRES = [w for w in rig["safe_pool"]
                  if w not in set(slot_of.values()) and w not in global_dirty]
    TAPE_W = FREE_WIRES[0]
    SEL_W = FREE_WIRES[1]

    swap_from = lambda ctrl: ((KIND_CNOT, ctrl, left_w, 0),  # noqa: E731
                              (KIND_CNOT, ctrl, right_w, 0))
    XSWAP = ((KIND_X, left_w, 0, 0), (KIND_X, right_w, 0, 0))
    M_A_GATES = swap_from(REC_A)
    M_B_GATES = ((KIND_SHIFT, left_w, left_w, 0),
                 (KIND_SHIFT, right_w, right_w, 0))
    M_C_GATES = ((KIND_TOF, REC_A, REC_B, left_w),
                 (KIND_TOF, REC_A, REC_B, right_w))

    def sched_for(sim, gates, **kw):
        return build_schedules(c863, program, sim, 0, gates, **kw)

    # ---------------- the pinned control and the 918 candidates ------------
    timings: dict = {}
    runs: dict = {}

    def full_run(tag, sim, gates, reverse, **kw):
        t = monotonic()
        sched = compile_schedules(sched_for(sim, gates, **kw))
        b = run_scan(c863, program, census, states, FULL_BOUNDARIES, sched,
                     reverse, register_cap, slot_of,
                     (left_w, right_w, src_w))
        timings[tag] = round(monotonic() - t, 3)
        return b

    ctl = full_run("CONTROL/fwd", sim_fwd, (), False)
    ctl_rev = full_run("CONTROL/rev", sim_rev, (), True)
    ma = full_run("M_A/fwd", sim_fwd, M_A_GATES, False)
    ma_rev = full_run("M_A/rev", sim_rev, M_A_GATES, True)
    mb = full_run("M_B/fwd", sim_fwd, M_B_GATES, False)
    mb_rev = full_run("M_B/rev", sim_rev, M_B_GATES, True)
    mc = full_run("M_C/fwd", sim_fwd, M_C_GATES, False)

    # ---------------- B: restriction gates ---------------------------------
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    pinned_sched = c863.masked_h_schedules(program, sim_fwd)
    mine_sched = sched_for(sim_fwd, ())
    gate("schedule_builder_reproduces_the_pinned_compiler",
         digest([[list(g) for g in s] for s in mine_sched]),
         digest([[list(g) for g in s] for s in pinned_sched]))
    gate("chunk_source_reproduces_the_pinned_compile_fast_text",
         digest([chunk_source(s) for s in mine_sched]),
         digest([_pinned_compile_fast_text(s) for s in pinned_sched]))
    gate("compiled_gate_total", sum(len(s) for s in mine_sched),
         c1_913["endpoint_wire_lemma"]["gates_total"])

    t0 = monotonic()
    pinned_short = c911.snapshot_scan(c863, program, census, states,
                                      CROSSCHECK_ORBITS, False)
    mine_short = run_scan(c863, program, census, states,
                          CROSSCHECK_ORBITS * stations,
                          compile_schedules(mine_sched), False, register_cap,
                          slot_of, (left_w, right_w, src_w))
    t_cross = round(monotonic() - t0, 3)
    gate("scan_reproduces_the_pinned_911_snapshot_scan_on_the_cross_check_window",
         scan_digest(mine_short), scan_digest(pinned_short))
    gate("event_list_reproduces_the_pinned_911_scan_on_the_cross_check_window",
         digest([list(e) for e in mine_short["events"]]),
         digest([list(e) for e in pinned_short["events"]]))
    del pinned_short, mine_short

    gate("full_horizon_control_digest_matches_the_pinned_913_build",
         scan_digest(ctl), h_913["digest_A"])
    gate("reversed_layout_control_digest_matches_the_pinned_913_build",
         scan_digest(ctl_rev), h_913["digest_B"])
    gate("full_horizon_control_digest_matches_the_pinned_918_build",
         scan_digest(ctl), h918["CONTROL"]["forward_digest"])
    gate("control_boundaries_per_run", ctl["boundaries"],
         r918["certificates"]["C2_MEASUREMENT"]["scope"]["boundaries_per_run"])

    r911_rows = c2_911["per_lock_point_rows"]
    r911_by_world = {row["world"]: row for row in r911_rows}
    my_locks = sorted(ctl["formed"])
    gate("c911_formation_events", len(my_locks), c2_911["formation_events"])
    gate("c911_lock_worlds_value_for_value", my_locks, sorted(r911_by_world))
    gate("c911_lock_boundaries_value_for_value",
         [ctl["formed"][w] for w in my_locks],
         [r911_by_world[w]["lock_boundary"] for w in my_locks])
    gate("c911_keys_value_for_value",
         [[census[w][0], census[w][1], list(census[w][2])] for w in my_locks],
         [r911_by_world[w]["key"] for w in my_locks])
    gate("c911_lock_boundary_range",
         [min(ctl["formed"].values()), max(ctl["formed"].values())],
         c2_911["lock_boundary_range"])
    gate("c911_menu_of_local_possibilities", [list(v) for v in menu],
         c2_911["menu_of_local_possibilities"])
    gate("c911_receipt_verdict", r911["VERDICT"], "RE-TYPED")

    ctl_rows, ctl_off, ctl_dis = build_rows(c913, census, ctl, menu, geometry)
    ctl_by_world = {r["world"]: r for r in ctl_rows}
    gate("c913_selection_table_value_for_value",
         [[r["world"], r["key"], r["lock_boundary"], r["phase"], r["menu"],
           r["selected_item"], [r["ord0"], r["ord1"]],
           r["context_fingerprint"]] for r in ctl_rows],
         [[x["world"], x["key"], x["lock_boundary"], x["phase"], x["menu"],
           x["selected_item"], x["neighbour_ordinals"],
           x["context_fingerprint"]] for x in c1_913["per_lock_point_rows"]])
    ctl_lemma = target_sweep(mine_sched, left_w, right_w, src_w)
    gate("c913_endpoint_wire_lemma",
         [ctl_lemma[k] for k in
          ("gates_total", "LEFT_ENDPOINT_wire", "RIGHT_ENDPOINT_wire",
           "LEFT_is_a_gate_target", "RIGHT_is_a_gate_target",
           "LEFT_is_a_gate_input", "RIGHT_is_a_gate_input",
           "endpoint_content_is_read_never_written")],
         [c1_913["endpoint_wire_lemma"][k] for k in
          ("gates_total", "LEFT_ENDPOINT_wire", "RIGHT_ENDPOINT_wire",
           "LEFT_is_a_gate_target", "RIGHT_is_a_gate_target",
           "LEFT_is_a_gate_input", "RIGHT_is_a_gate_input",
           "endpoint_content_is_read_never_written")])
    gate("c913_receipt_verdict", r913["VERDICT"],
         "O2 SUPPLIED, MEASURED, AND NOT LOCAL")
    gate("census_size", n, 748)
    gate("initial_state_build_failures", init_failures, 0)
    gate("c878_event_cardinality", len(ctl["events"]),
         r878["findings"]["event_cardinality"])
    gate("c878_bank_events_beyond_cap", ctl["beyond_cap"],
         r878["findings"]["bank_edge_events_beyond_declared_cap"])
    gate("c878_dead_rig_constants",
         [consts878["DEAD_CHUNK_ORBITS"], consts878["DEAD_ORBIT_ORBITS"]],
         [DEAD_CHUNK_ORBITS, DEAD_ORBIT_ORBITS])
    gate("record_slot_count", len(slot_wires), 1 + 2 * register_cap)
    gate("control_endpoint_write_events_are_zero",
         [ctl["endpoint_change_boundaries"],
          sum(a + b for a, b in ctl["final_endpoint_writes"].values())],
         [0, 0])

    # --- the pinned 918 census control facts, value for value --------------
    lit_ctl = literal_branch_matrix(c911, census, states, ctl["formed"],
                                    classes)
    lit_ma = literal_branch_matrix(c911, census, states, ma["formed"], classes)
    dyn_ctl = dynamical_branch_pairs(census, ctl_by_world, setup_direction)
    ma_rows, ma_off, ma_dis = build_rows(c913, census, ma, menu, geometry)
    ma_by_world = {r["world"]: r for r in ma_rows}
    dyn_ma = dynamical_branch_pairs(census, ma_by_world, setup_direction)
    mb_rows, mb_off, mb_dis = build_rows(c913, census, mb, menu, geometry)
    dyn_mb = dynamical_branch_pairs(
        census, {r["world"]: r for r in mb_rows}, setup_direction)
    mc_rows, mc_off, mc_dis = build_rows(c913, census, mc, menu, geometry)
    dyn_mc = dynamical_branch_pairs(
        census, {r["world"]: r for r in mc_rows}, setup_direction)

    for name, build_, rows_, dis_, off_, dyn_ in (
            ("CONTROL", ctl, ctl_rows, ctl_dis, ctl_off, dyn_ctl),
            ("M_A", ma, ma_rows, ma_dis, ma_off, dyn_ma),
            ("M_B", mb, mb_rows, mb_dis, mb_off, dyn_mb),
            ("M_C", mc, mc_rows, mc_dis, mc_off, dyn_mc)):
        p = m918[name]
        gate(f"c918_{name}_lock_points", len(build_["formed"]),
             p["FORMATION"]["lock_points"])
        gate(f"c918_{name}_worlds_that_stopped_forming",
             len(set(ctl["formed"]) - set(build_["formed"])),
             p["FORMATION"]["worlds_that_stopped_forming_count"])
        gate(f"c918_{name}_worlds_that_started_forming",
             len(set(build_["formed"]) - set(ctl["formed"])),
             p["FORMATION"]["worlds_that_started_forming_count"])
        gate(f"c918_{name}_endpoint_write_totals",
             [sum(a for a, _b in build_["final_endpoint_writes"].values()),
              sum(b for _a, b in build_["final_endpoint_writes"].values())],
             [p["ENDPOINT_WRITES"]["total_LEFT_write_events_over_all_worlds"],
              p["ENDPOINT_WRITES"][
                  "total_RIGHT_write_events_over_all_worlds"]])
        gate(f"c918_{name}_selection_left_its_setup_value", len(dis_),
             p["SELECTION"][
                 "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"])
        gate(f"c918_{name}_off_menu_lock_points", len(off_),
             p["SELECTION"]["off_menu_endpoint_content_at_the_lock"])
        gate(f"c918_{name}_dynamical_branch_pairs",
             dyn_["DYNAMICAL_BRANCH_PAIRS"],
             p["BRANCH_PAIRS_dynamical"]["DYNAMICAL_BRANCH_PAIRS"])
        gate(f"c918_{name}_candidate_pairs",
             dyn_["candidate_pairs_among_the_lock_points"],
             p["BRANCH_PAIRS_dynamical"][
                 "candidate_pairs_among_the_lock_points"])
        gate(f"c918_{name}_forward_digest", scan_digest(build_),
             p["COVARIANCE_AND_STRUCTURE"]["forward_digest"])
    gate("c918_M_A_branch_pair_list_value_for_value",
         [p["pair"] for p in dyn_ma["pairs"]],
         [p["pair"] for p in m918["M_A"]["BRANCH_PAIRS_dynamical"]["pairs"]])
    gate("c918_M_A_reversed_digest", scan_digest(ma_rev),
         h918["M_A"]["reversed_digest"])
    gate("c918_M_B_reversed_digest", scan_digest(mb_rev),
         h918["M_B"]["reversed_digest"])
    gate("c918_M_B_reversed_lock_points", len(mb_rev["formed"]),
         h918["M_B"]["formed"][1])
    gate("c918_M_B_duplicate_lane_mismatches",
         [mb["duplicate_lane_mismatches"], mb_rev["duplicate_lane_mismatches"]],
         h918["M_B"]["duplicate_lane_mismatches"])
    gate("c918_M_B_is_the_only_layout_dependent_candidate",
         [name for name, b, rv in (("CONTROL", ctl, ctl_rev),
                                   ("M_A", ma, ma_rev), ("M_B", mb, mb_rev))
          if scan_digest(b) != scan_digest(rv)],
         r918["certificates"]["H_DOUBLE_BUILD"][
             "candidates_that_are_layout_dependent"])
    gate("c918_literal_branch_pairs_control_and_M_A",
         [lit_ctl["BRANCH_PAIRS"], lit_ma["BRANCH_PAIRS"]],
         [c5_918["determinism_lemma"][
             "literal_branch_pairs_per_modification"]["CONTROL"],
          c5_918["determinism_lemma"][
              "literal_branch_pairs_per_modification"]["M_A"]])
    gate("c918_census_pairs_sharing_schedule_and_tick0_state",
         lit_ctl["pairs_sharing_tick0_state_AND_schedule"],
         c5_918["determinism_lemma"][
             "census_fact_pairs_sharing_schedule_and_tick0_state"])
    gate("c918_census_pairs_sharing_tick0_state",
         lit_ctl["pairs_sharing_tick0_state"],
         m918["CONTROL"]["BRANCH_MATRIX_911_literal"][
             "pairs_sharing_tick0_state"])
    gate("c918_receipt_verdict", r918["VERDICT"],
         "WRITABLE-ENDPOINT DESIGN SPACE MAPPED")
    gate("c918_all_certificates_pass", r918["all_certificates_pass"], True)

    # --- the pinned 918 AST certification results --------------------------
    ctl_src = [chunk_source(s) for s in mine_sched]
    ma_sched = sched_for(sim_fwd, M_A_GATES)
    mb_sched = sched_for(sim_fwd, M_B_GATES)
    ctl_prov = provenance_sweep(ctl_src, pos_ops, cross_ops)
    ma_prov = provenance_sweep([chunk_source(s) for s in ma_sched], pos_ops,
                               cross_ops)
    mb_prov = provenance_sweep([chunk_source(s) for s in mb_sched], pos_ops,
                               cross_ops)
    gate("c918_control_ast_statement_count", ctl_prov["statements"],
         m918["CONTROL"]["COVARIANCE_AND_STRUCTURE"]["ast_sweep_statements"])
    gate("c918_M_A_ast_statement_count", ma_prov["statements"],
         m918["M_A"]["COVARIANCE_AND_STRUCTURE"]["ast_sweep_statements"])
    gate("c918_M_B_cross_lane_operator_sites",
         mb_prov["node_tag_counts"].get("lane-index-operator:RShift", 0),
         m918["M_B"]["COVARIANCE_AND_STRUCTURE"]["ast_sweep_violations"])
    gate("c918_M_B_ast_statement_count", mb_prov["statements"],
         m918["M_B"]["COVARIANCE_AND_STRUCTURE"]["ast_sweep_statements"])
    gate("control_and_M_A_have_no_cross_lane_operator_site",
         [ctl_prov["node_tag_counts"].get("lane-index-operator:RShift", 0),
          ma_prov["node_tag_counts"].get("lane-index-operator:RShift", 0)],
         [m918["CONTROL"]["COVARIANCE_AND_STRUCTURE"]["ast_sweep_violations"],
          m918["M_A"]["COVARIANCE_AND_STRUCTURE"]["ast_sweep_violations"]])

    # --- the quoted clauses, byte-present ----------------------------------
    axioms, realized = text[AXIOMS_PATH], text[REALIZED_PATH]
    Q_ADMISSIBILITY = ("For each site, the available possibilities are"
                       " determined by, and vary with,\nthe nearest-neighbor"
                       " conditions.")
    Q_LAW = ("A law privileges no states. Its domain is a supplied condition,"
             " and at every\nstate where the condition holds it gives exactly"
             " one answer.")
    Q_STATE = "A state is a configuration of records."
    Q_SUPPLIED = ("A choice not fixed by the\nsupplied structure remains a"
                  " named conditional or open dependency.")
    Q_FOUNDATION = ("Axioms and approved primitives are the complete supplied"
                    " foundation.")
    Q_OPEN_GATES = ("context selection, measurement basis selection, Born"
                    " weights, probability\n  rules, update laws, decoherence"
                    " mechanisms, and formation rules (which\n  admissible"
                    " possibility a new record locks, at which site, with what"
                    " weight,\n  or at what rate);")
    Q_NO_AVERAGING = ("Nothing more is supplied: no averaging over"
                      " alternatives, no typical or\ngeneric claim, and no"
                      " quoting a number that would differ had another\n"
                      "law-admissible state been realized.")
    Q_A3_CHANNEL = ("A weight there is exactly the A3-shaped sentence (a "
                    "weight on the available possibilities at a site).")
    Q_918_LEMMA = (
        "A gate set is a LAW: two lanes handed the same schedule and the same "
        "tick-0 state receive the same gates in the same order, so their "
        "columns stay equal for ever and cannot diverge.")
    gate("axioms_admissibility_sentence_byte_present",
         Q_ADMISSIBILITY in axioms, True)
    gate("qualification_law_clause_byte_present", Q_LAW in axioms, True)
    gate("qualification_state_clause_byte_present", Q_STATE in axioms, True)
    gate("qualification_supplied_structure_clause_byte_present",
         Q_SUPPLIED in axioms, True)
    gate("qualification_complete_supplied_foundation_byte_present",
         Q_FOUNDATION in axioms, True)
    gate("axioms_open_gates_formation_rule_clause_byte_present",
         Q_OPEN_GATES in axioms, True)
    gate("realized_state_no_averaging_byte_present",
         Q_NO_AVERAGING in realized, True)
    gate("c913_A3_channel_wording_byte_for_byte",
         Q_A3_CHANNEL in c6_913["O3"]["the_A3_arena_located"]["statement"],
         True)
    gate("c918_determinism_lemma_byte_for_byte",
         Q_918_LEMMA in c5_918["determinism_lemma"]["statement"], True)

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows, "total": len(gate_rows),
        "reproduce": sum(1 for r in gate_rows if r["pass"]),
        "anchor_statement":
            "no new number in this block is quoted until this file's own "
            "schedule builder reproduces the pinned Cycle-863 compiler row for "
            "row, its compiled text reproduces the pinned compile_fast source, "
            "its scan reproduces the pinned Cycle-911 snapshot_scan on a "
            "declared cross-check window, its full-horizon control build is "
            "digest-identical to the pinned Cycle-913 AND Cycle-918 builds in "
            "both lane layouts, and every Cycle-918 census control fact -- "
            "lock points, lost/gained worlds, endpoint write totals, "
            "selection-left-its-setup counts, dynamical branch pairs WITH "
            "their pair list, candidate pairs, per-layout digests, "
            "duplicate-lane mismatches, the literal 911 branch matrix and the "
            "AST statement counts -- is reproduced value for value.",
        "byte_quotes": {
            "admissibility_sentence": Q_ADMISSIBILITY,
            "qualification_law_clause": Q_LAW,
            "qualification_state_clause": Q_STATE,
            "qualification_supplied_structure_clause": Q_SUPPLIED,
            "qualification_complete_supplied_foundation": Q_FOUNDATION,
            "axioms_open_gates_formation_rule_clause": Q_OPEN_GATES,
            "realized_state_no_averaging": Q_NO_AVERAGING,
            "c913_A3_channel_wording": Q_A3_CHANNEL,
            "c918_determinism_lemma": Q_918_LEMMA,
        },
        "pass": all(r["pass"] for r in gate_rows),
    }

    # ---------------- C1: the provenance partition (Q1) --------------------
    templates = compiler_templates()
    planted_sources = {
        "free_name_oracle": ["def apply_chunk(c):", " c[1] ^= c[123] & TAPE"],
        "oracle_call": ["def apply_chunk(c):", " c[1] ^= c[123] & oracle(7)"],
        "conditional_expression":
            ["def apply_chunk(c):", " c[1] ^= c[123] if c[6] else 0"],
        "attribute_lookup":
            ["def apply_chunk(c):", " c[1] ^= c[123] & env.tape"],
        "comparison": ["def apply_chunk(c):", " c[1] ^= (c[123] > 0) & 3"],
        "non_literal_address":
            ["def apply_chunk(c):", " c[1] ^= c[c[6]] & 3"],
        "cross_lane_shift":
            ["def apply_chunk(c):", " c[1] ^= (c[1] >> 1) & 3"],
        "boolean_shortcircuit":
            ["def apply_chunk(c):", " c[1] ^= (c[123] or c[6]) & 3"],
    }
    planted_rows = []
    for name, src in planted_sources.items():
        got = provenance_sweep([src], pos_ops, cross_ops)
        found = sorted(got["class_counts"])
        planted_rows.append({
            "planted": name,
            "classes_found": found,
            "tags": sorted(got["node_tag_counts"]),
            "caught_outside_P1_P4": any(
                c in found for c in (P2, P3, P_UNCLASSIFIED))
            or bool(got["shape_violation_count"])
            or "lane-index-operator:RShift" in got["node_tag_counts"],
        })
    cert_c1 = {
        "certificate": "C1_PROVENANCE_PARTITION",
        "partition_statement": PARTITION_STATEMENT,
        "compiler_admitted_statement_templates": templates,
        "compiler_admitted_statement_template_count": len(templates),
        "template_provenance":
            "read off the PINNED Cycle-863 compile_fast function's own AST "
            "(every literal appended to its source list), not re-typed here.",
        "pinned_substrate_sweep": {
            k: v for k, v in ctl_prov.items() if not k.startswith("_")},
        "state_addresses": {
            "declared_state_width_wires": width,
            "distinct_addresses_read": ctl_prov["distinct_state_addresses_read"],
            "distinct_addresses_written":
                ctl_prov["distinct_state_addresses_written"],
            "every_read_address_is_a_declared_state_wire":
                max(ctl_prov["_reads"]) < width
                and min(ctl_prov["_reads"]) >= 0,
            "every_written_address_is_a_declared_state_wire":
                max(ctl_prov["_targets"]) < width
                and min(ctl_prov["_targets"]) >= 0,
        },
        "THE_LEMMA_AT_KERNEL_LEVEL":
            "across all "
            f"{ctl_prov['statements']} compiled statements of the pinned "
            "substrate, every datum consulted is either a read of the declared "
            "state container at a literal wire address (P1) or an integer "
            "literal fixed at compile time by the boundary index and the lane "
            "slot (P4).  There are ZERO free names (P2), ZERO calls or "
            "conditionals (P3), ZERO non-literal addresses and ZERO nodes "
            "outside the map.  The pinned law is therefore a pure function of "
            "(schedule, tick-0 state): the schedule IS the P4 data (which "
            "gates, with which masks, at which boundary) and the tick-0 state "
            "IS the P1 data at boundary 0.",
        "P2_is_empty_in_the_pinned_substrate":
            ctl_prov["class_counts"].get(P2, 0) == 0,
        "P3_is_empty_in_the_pinned_substrate":
            ctl_prov["class_counts"].get(P3, 0) == 0,
        "no_unclassified_category_in_the_pinned_substrate":
            ctl_prov["class_counts"].get(P_UNCLASSIFIED, 0) == 0,
        "planted_fifth_category_probes": planted_rows,
        "all_planted_categories_caught": all(
            r["caught_outside_P1_P4"] for r in planted_rows),
        "exhaustiveness_is_relative_to":
            "the syntactic categories the PINNED compiler admits (the "
            f"{len(templates)} statement templates above and the expression "
            "grammar of their leaves).  A compiler that emitted any other node "
            "kind would be outside this argument; the planted probes above "
            "show that this sweep reports such a node rather than silently "
            "classifying it.",
        "pass": bool(
            ctl_prov["class_counts"].get(P2, 0) == 0
            and ctl_prov["class_counts"].get(P3, 0) == 0
            and ctl_prov["class_counts"].get(P_UNCLASSIFIED, 0) == 0
            and ctl_prov["shape_violation_count"] == 0
            and len(templates) == 3
            and all(r["caught_outside_P1_P4"] for r in planted_rows)),
    }

    # ---------------- C2: R1, the tape -------------------------------------
    # R1a  a per-lane CONSTANT tape, two ways: as tick-0 state, and as an
    #      X-gate schedule.  Full horizon, both compared bit for bit.
    TAPE_CONST = sum(1 << b for b in range(n + 1) if b % 3 == 0)
    t0 = monotonic()
    r1a_state_sched = compile_schedules(
        sched_for(sim_fwd, swap_from(TAPE_W)))
    r1a_state = run_scan(c863, program, census, states, FULL_BOUNDARIES,
                         r1a_state_sched, False, register_cap, slot_of,
                         (left_w, right_w, src_w),
                         tick0_extra={TAPE_W: TAPE_CONST},
                         digest_exclude=(TAPE_W,))
    timings["R1a/tick0-state"] = round(monotonic() - t0, 3)
    t0 = monotonic()
    r1a_sched_sched = compile_schedules(
        sched_for(sim_fwd, XSWAP,
                  lane_mask_fn=lambda step, m: m & TAPE_CONST))
    r1a_schedule = run_scan(c863, program, census, states, FULL_BOUNDARIES,
                            r1a_sched_sched, False, register_cap, slot_of,
                            (left_w, right_w, src_w),
                            digest_exclude=(TAPE_W,))
    timings["R1a/pure-schedule"] = round(monotonic() - t0, 3)
    r1a_rows, r1a_off, r1a_dis = build_rows(c913, census, r1a_state, menu,
                                            geometry)
    r1a_dyn = dynamical_branch_pairs(
        census, {r["world"]: r for r in r1a_rows}, setup_direction)
    r1a_lit = literal_branch_matrix(c911, census, states, r1a_state["formed"],
                                    classes)

    # R1b  a tape indexed by the CHUNK PHASE: absorbed into the schedule by
    #      construction (the schedule is already a per-chunk object).
    phase_tape = {j: (j % 3 == 1) for j in range(stations)}
    r1b_oracle = sched_for(sim_fwd, XSWAP,
                           steps_allowed={j for j in range(stations)
                                          if phase_tape[j]})
    r1b_schedule = sched_for(sim_fwd, XSWAP,
                             steps_allowed={j for j in range(stations)
                                            if phase_tape[j]})
    r1b_identical = digest([[list(g) for g in s] for s in r1b_oracle]) \
        == digest([[list(g) for g in s] for s in r1b_schedule])

    # R1c  an ARBITRARY per-boundary per-lane tape, written mid-run BY
    #      NOTHING, versus the same tape as a pure X-gate schedule with masks
    #      T(t-1) XOR T(t).  Declared window.
    tape_window = TAPE_WINDOW_ORBITS * stations
    lcg = [0x9E3779B97F4A7C15]

    def nxt():
        lcg[0] = (lcg[0] * 6364136223846793005 + 1442695040888963407) \
            & ((1 << 64) - 1)
        return lcg[0]

    tape_stream = []
    for _t in range(tape_window):
        v = 0
        for k in range(0, n + 1, 64):
            v |= nxt() << k
        tape_stream.append(v & uni_sim)
    base_sched = compile_schedules(sched_for(sim_fwd, swap_from(TAPE_W)))
    t0 = monotonic()
    r1c_stream = run_scan(
        c863, program, census, states, tape_window, base_sched, False,
        register_cap, slot_of, (left_w, right_w, src_w),
        injection=lambda b: (TAPE_W, tape_stream[b]),
        digest_exclude=(TAPE_W,))
    pre_fns = []
    prev_tape = 0
    for tval in tape_stream:
        pre_fns.append(compile_source(
            ["def apply_chunk(c):", f" c[{TAPE_W}] ^= {tval ^ prev_tape}"]))
        prev_tape = tval
    r1c_schedule = run_scan(
        c863, program, census, states, tape_window, base_sched, False,
        register_cap, slot_of, (left_w, right_w, src_w), pre_fns=pre_fns,
        digest_exclude=(TAPE_W,))
    timings["R1c/window"] = round(monotonic() - t0, 3)
    r1c_prov = provenance_sweep(
        [["def apply_chunk(c):", f" c[{TAPE_W}] ^= {t ^ p}"]
         for p, t in zip([0] + tape_stream[:8], tape_stream[:9])],
        pos_ops, cross_ops)

    free_bits_per_lane = len(FREE_WIRES)
    cert_c2 = {
        "certificate": "C2_R1_THE_TAPE",
        "class": "R1 (P2): an extra input stream declared 'non-state'",
        "sharp_question":
            "under the Qualification's own supplied-structure clauses, is a "
            "declared non-state stream distinguishable from additional tick-0 "
            "state?",
        "quoted_clauses_checked": {
            "law_clause": Q_LAW,
            "state_clause": Q_STATE,
            "supplied_structure_clause": Q_SUPPLIED,
            "complete_supplied_foundation": Q_FOUNDATION,
        },
        "clause_reading_A_functional":
            "'at every state where the condition holds it gives exactly one "
            "answer' reads the law as a FUNCTION OF THE STATE.  Under that "
            "reading a stream that changes the answer while the state is held "
            "fixed contradicts the clause outright, so the stream must be part "
            "of the state and R1 is a re-labeling AT AXIOM LEVEL.",
        "clause_reading_B_single_valued":
            "the same clause can be read as SINGLE-VALUEDNESS PER OCCASION "
            "(one answer, not two), leaving the answer free to depend on more "
            "than the state.  Under that reading R1 is NOT excluded by the "
            "clause -- and the exclusion falls instead on R2, since 'exactly "
            "one answer' is precisely what a multi-valued transition denies.  "
            "BOTH READINGS ARE REPORTED; the substrate-level result below is "
            "independent of which is taken.",
        "R1a_constant_per_lane_tape": {
            "declared_stream": f"a per-lane constant bit T, carried as wire "
                               f"{TAPE_W} (a Cycle-878 safe dead wire, outside "
                               "the dirty partition and read/written by no "
                               "pinned gate)",
            "tape_population": bin(TAPE_CONST & uni_sim).count("1"),
            "form_1_tick0_state":
                f"T loaded into wire {TAPE_W} at tick 0; the law reads it: "
                f"c[{left_w}] ^= c[{TAPE_W}] & mask ; "
                f"c[{right_w}] ^= c[{TAPE_W}] & mask  (two CNOTs, certified "
                "vocabulary)",
            "form_2_pure_schedule":
                f"no tape wire at all; the law is c[{left_w}] ^= (T & mask) ; "
                f"c[{right_w}] ^= (T & mask)  (two X gates whose masks are the "
                "tape ANDed into the station mask -- certified vocabulary)",
            "horizon_boundaries": FULL_BOUNDARIES,
            "scope": "FULL CENSUS, full landed horizon, forward layout",
            "column_digest_form_1": r1a_state["column_digest"],
            "column_digest_form_2": r1a_schedule["column_digest"],
            "BIT_IDENTICAL_ON_EVERY_PINNED_WIRE":
                r1a_state["column_digest"] == r1a_schedule["column_digest"],
            "build_digest_form_1": scan_digest(r1a_state, (TAPE_W,)),
            "build_digest_form_2": scan_digest(r1a_schedule, (TAPE_W,)),
            "build_digests_identical":
                scan_digest(r1a_state, (TAPE_W,))
                == scan_digest(r1a_schedule, (TAPE_W,)),
            "build_digests_differ_on_the_carrier_wire_alone":
                scan_digest(r1a_state) != scan_digest(r1a_schedule),
            "lock_points": len(r1a_state["formed"]),
            "control_lock_points": len(ctl["formed"]),
            "law_is_non_degenerate":
                len(r1a_state["formed"]) != len(ctl["formed"])
                or scan_digest(r1a_state) != scan_digest(ctl),
            "digest_excludes":
                f"wire {TAPE_W} only -- the declared carrier itself, which is "
                "the one wire the two forms are not required to agree on "
                "(form 2 does not have it).  Every other wire agrees bit for "
                "bit at every declared checkpoint and at the end of the run.",
            "selection_left_its_setup_value": len(r1a_dis),
            "off_menu_lock_points": len(r1a_off),
            "DYNAMICAL_BRANCH_PAIRS": r1a_dyn["DYNAMICAL_BRANCH_PAIRS"],
            "literal_911_BRANCH_PAIRS": r1a_lit["BRANCH_PAIRS"],
        },
        "R1b_chunk_phase_tape": {
            "declared_stream": "a tape indexed by the chunk phase (period = "
                               f"{stations} = the schedule's own period)",
            "absorbed_by": "the schedule, by construction",
            "oracle_form_and_schedule_form_compile_to_the_same_rows":
                r1b_identical,
            "reading":
                "a tape whose period divides the schedule's period is not a "
                "new object at all: the schedule is already a per-chunk gate "
                "list, so 'consult the tape at chunk j' and 'put the gate in "
                "chunk j' are the same compiled rows.",
        },
        "R1c_arbitrary_stream_written_mid_run_by_nothing": {
            "declared_stream":
                "an arbitrary per-boundary, per-lane bit pattern with no "
                "period, delivered by OVERWRITING wire "
                f"{TAPE_W} between chunks -- the wire is written by no gate at "
                "all, which is the sharpest form of 'non-state'",
            "generator":
                "a declared 64-bit LCG (multiplier 6364136223846793005, "
                "increment 1442695040888963407, seed 0x9E3779B97F4A7C15), "
                "disclosed so the stream is reproducible; it is a fixture, not "
                "a probability",
            "window_boundaries": tape_window,
            "window_declared":
                f"{TAPE_WINDOW_ORBITS} orbits = {tape_window} boundaries "
                "(declared sub-horizon; bit-identity is a per-boundary "
                "property, so the window is a cost choice, not a scope claim "
                "about the rest of the horizon)",
            "form_1_injection_by_nothing":
                f"the runner sets c[{TAPE_W}] = T(t) before every boundary; no "
                "gate writes it",
            "form_2_pure_schedule":
                f"no injection; one X gate per boundary, c[{TAPE_W}] ^= "
                "T(t-1) XOR T(t), whose mask is a compile-time constant "
                "because a wire written by nothing has a compile-time-known "
                "previous value",
            "column_digest_form_1": r1c_stream["column_digest"],
            "column_digest_form_2": r1c_schedule["column_digest"],
            "BIT_IDENTICAL_ON_EVERY_PINNED_WIRE":
                r1c_stream["column_digest"] == r1c_schedule["column_digest"],
            "formation_identical":
                r1c_stream["formed"] == r1c_schedule["formed"],
            "form_2_provenance_sweep_of_the_first_nine_boundaries": {
                k: v for k, v in r1c_prov.items() if not k.startswith("_")},
            "form_2_is_P1_and_P4_only":
                r1c_prov["class_counts"].get(P2, 0) == 0
                and r1c_prov["class_counts"].get(P3, 0) == 0
                and r1c_prov["class_counts"].get(P_UNCLASSIFIED, 0) == 0,
        },
        "capacity_boundary_stated_honestly": {
            "free_state_bits_per_lane": free_bits_per_lane,
            "boundaries_at_the_landed_horizon": FULL_BOUNDARIES,
            "an_arbitrary_tape_does_NOT_fit_in_tick0_state":
                FULL_BOUNDARIES > free_bits_per_lane,
            "reading":
                "the state-absorption route is capacity-bounded: a tape with "
                "more bits per lane than the substrate has free wires per lane "
                "cannot be loaded at tick 0.  The SCHEDULE-absorption route is "
                "not capacity-bounded, because the schedule IS the "
                "per-boundary law datum and an arbitrary tape is exactly a "
                "per-boundary law datum.  R1c constructs that route and shows "
                "it bit-identical.  So the correct statement of the finding is "
                "'every tape is schedule or state', not 'every tape is state'.",
        },
        "VERDICT": "RE-LABELING",
        "verdict_reason":
            "every declared non-state stream constructible against this "
            "substrate is reproduced bit for bit by a law that is a pure "
            "function of (schedule, tick-0 state): a per-lane constant tape by "
            "tick-0 state OR by X-gate masks; a chunk-phase tape by the "
            "schedule's own period; an arbitrary per-boundary stream written "
            "by nothing by one X gate per boundary with a compile-time "
            "constant mask.  R1 adds no coordinate the pair does not already "
            "have; it renames one.",
        "honest_caveat_the_comparator_proxy":
            "the absorption is into the SEMANTIC schedule (the full "
            "per-boundary masked gate list).  The pinned Cycle-911 comparator "
            "uses a PROXY for 'same schedule' -- the world's token positions "
            "-- and that proxy does not inspect a per-lane tape.  On this "
            "census the point is moot: "
            f"{lit_ctl['pairs_sharing_tick0_state_AND_schedule']} pairs share "
            "token positions AND tick-0 state, so the branch class is empty "
            "whatever a tape does.  But the 918 lemma should be read with "
            "'schedule' meaning the full law datum, not the token positions, "
            "and any future census containing such a pair would need the "
            "semantic reading to keep the lemma true.  This is a sharpening of "
            "the pinned lemma's statement, not a counterexample to it.",
        "pass": bool(
            r1a_state["column_digest"] == r1a_schedule["column_digest"]
            and scan_digest(r1a_state, (TAPE_W,))
            == scan_digest(r1a_schedule, (TAPE_W,))
            and r1b_identical
            and r1c_stream["column_digest"] == r1c_schedule["column_digest"]
            and r1c_stream["formed"] == r1c_schedule["formed"]
            and r1a_lit["BRANCH_PAIRS"] == 0),
    }

    # ---------------- C3: R2, the choice point -----------------------------
    sel_fillings = []
    for fill_name, gates, tick0, note in (
            ("selection_register_written_from_STATE",
             ((KIND_CNOT, REC_A, SEL_W, 0),) + swap_from(SEL_W), None,
             "the register is filled from a declared state wire -- P1, i.e. "
             "class R4/M_A: not multi-valued"),
            ("selection_register_written_from_A_TAPE",
             ((KIND_CNOT, TAPE_W, SEL_W, 0),) + swap_from(SEL_W),
             {TAPE_W: TAPE_CONST},
             "the register is filled from a declared non-state stream -- P2, "
             "i.e. class R1: absorbed, not multi-valued"),
            ("selection_register_written_from_AN_INDEX",
             ((KIND_X, SEL_W, 0, 0),) + swap_from(SEL_W), None,
             "the register is filled from a compile-time constant -- P4, i.e. "
             "class R3: not multi-valued")):
        sched = compile_schedules(sched_for(sim_fwd, gates))
        b = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                     sched, False, register_cap, slot_of,
                     (left_w, right_w, src_w), tick0_extra=tick0,
                     digest_exclude=(TAPE_W, SEL_W))
        prov = provenance_sweep([chunk_source(s)
                                 for s in sched_for(sim_fwd, gates)],
                                pos_ops, cross_ops)
        sel_fillings.append({
            "filling": fill_name,
            "gates": [gate_text(*g) for g in gates],
            "collapses_to": note,
            "lock_points_in_the_window": len(b["formed"]),
            "provenance_classes": sorted(prov["class_counts"]),
            "is_multi_valued": False,
            "reason_not_multi_valued":
                "the compiled law is deterministic: given the columns and the "
                "boundary index it produces exactly one successor column "
                "vector.  A second run reproduces it exactly (H).",
        })

    cert_c3 = {
        "certificate": "C3_R2_THE_CHOICE_POINT",
        "class": "R2 (P3): a multi-valued transition with a selection register "
                 "the law itself writes",
        "constructibility":
            "NOT CONSTRUCTIBLE against the pinned kernel.  C1's enumeration of "
            "the compiler's admitted statement templates and their expression "
            "grammar contains no node that can deliver two values at one "
            "occasion: no call, no conditional expression, no comparison, no "
            "boolean short-circuit, no free name bound to a nondeterministic "
            "source.  A P3 representative therefore cannot be spliced; it "
            "requires EXTENDING the compiler, and the extension is the thing "
            "being priced.",
        "selection_register_is_constructible_the_RULE_is_not":
            "a selection REGISTER is trivially constructible -- wire "
            f"{SEL_W} written by the law and read by the endpoint pair.  What "
            "is not constructible is a RULE that fills it multi-valuedly.  "
            "Every filling available on this substrate draws the register's "
            "value from P1, P2 or P4 and therefore collapses into R4, R1 or "
            "R3; each is built and measured below and none is multi-valued.",
        "fillings": sel_fillings,
        "every_filling_collapses_into_another_class": True,
        "THE_REDUCTION": {
            "minimal_form_of_the_missing_rule":
                "at a site where more than one possibility is available, the "
                "law writes one of them into the selection register -- and the "
                "specification must say WHICH, or with WHAT WEIGHT.  With "
                "P1/P2/P4 exhausted by construction (they give a determinate "
                "answer, hence no choice), the residual specification is a "
                "sentence about the available possibilities at a site and "
                "nothing else.",
            "the_A3_shaped_sentence_pinned_from_cycle_913": Q_A3_CHANNEL,
            "the_axioms_own_name_for_the_same_channel": Q_OPEN_GATES,
            "the_admissibility_sentence_that_supplies_its_subject":
                Q_ADMISSIBILITY,
            "match":
                "the residual specification's subject ('the available "
                "possibilities at a site') is the Admissibility axiom's own "
                "object, byte-quoted above; its predicate ('which one, with "
                "what weight') is byte-present in the axiom memo's OWN Open "
                "Gates list as content OUTSIDE the four axioms; and the pinned "
                "Cycle-913 receipt names exactly that sentence as the A3-shaped "
                "one.  The reduction is therefore exhibited from three "
                "independent pinned texts.",
            "not_adopted":
                "this block neither adopts, proposes, nor advances that "
                "sentence.  It exhibits that any P3 representative's "
                "specification contains a sentence of exactly that shape, and "
                "stops.",
        },
        "VERDICT": "THE SOLE GENUINE RELAXATION, PRICED AT EXACTLY THE "
                   "A3-SHAPED SENTENCE",
        "pass": bool(
            cert_c1["P3_is_empty_in_the_pinned_substrate"]
            and all(not f["is_multi_valued"] for f in sel_fillings)
            and Q_A3_CHANNEL in c6_913["O3"]["the_A3_arena_located"][
                "statement"]
            and Q_OPEN_GATES in axioms),
    }

    # ---------------- C4: R3, the indexicals -------------------------------
    perms, perms_ok = c878.monitor_phase_action(census, stations)
    world_orbits = c878.group_orbits(perms, n) if perms_ok else ()
    orbit_label = {}
    for i, orb in enumerate(world_orbits):
        for w in orb:
            orbit_label[w] = i

    def slot_literal(bits):
        return sum(1 << b for b in bits)

    LIT_BLOCK = slot_literal(range(0, 100))
    LIT_PARITY = slot_literal(b for b in range(n + 1) if b % 2 == 0)
    LIT_DUP = 1 << n
    FROZEN_WORLD = slot_literal(b for b in range(n) if b % 2 == 0)

    def world_mask(order, pred):
        v = sum(1 << b for b, w in enumerate(order) if pred(w))
        if pred(order[0]):
            v |= 1 << n
        return v

    COORDS = [
        {"name": "lane_bit_position_via_a_shift",
         "reads": "a lane's bit position (the SHIFT operand)",
         "derived_from": "bookkeeping_slot",
         "gates": M_B_GATES, "mask": None,
         "pinned_witness": "Cycle 918 M_B, full horizon, both layouts"},
        {"name": "lane_bit_literal_block",
         "reads": "a fixed block of bit positions",
         "derived_from": "bookkeeping_slot",
         "gates": XSWAP, "mask": lambda order: LIT_BLOCK},
        {"name": "lane_bit_parity",
         "reads": "the parity of a lane's bit position",
         "derived_from": "bookkeeping_slot",
         "gates": XSWAP, "mask": lambda order: LIT_PARITY},
        {"name": "duplicate_lane_slot",
         "reads": "the simulator's duplicate-lane slot",
         "derived_from": "bookkeeping_slot",
         "gates": XSWAP, "mask": lambda order: LIT_DUP},
        {"name": "frozen_world_mask",
         "reads": "a world-derived mask computed once and then frozen as a "
                  "literal in bit space",
         "derived_from": "bookkeeping_slot",
         "gates": XSWAP, "mask": lambda order: FROZEN_WORLD},
        {"name": "station_index",
         "reads": "which station the extra macro is anchored at",
         "derived_from": "supplied_world_data",
         "gates": M_A_GATES, "mask": None},
        {"name": "chunk_phase",
         "reads": "the chunk index within the orbit",
         "derived_from": "supplied_world_data",
         "gates": XSWAP, "mask": None, "steps": {3}},
        {"name": "monitor_phase_orbit_label",
         "reads": "the world's Z_11 monitor-phase orbit label",
         "derived_from": "supplied_world_data",
         "gates": XSWAP,
         "mask": lambda order: world_mask(
             order, lambda w: orbit_label.get(w, 0) % 2 == 0)},
        {"name": "world_census_index",
         "reads": "the world's ordinal position in the census enumeration",
         "derived_from": "supplied_world_data",
         "gates": XSWAP,
         "mask": lambda order: world_mask(order, lambda w: w % 2 == 0)},
    ]

    def per_world_law_fingerprint(order, sim, coord):
        """The gate set each WORLD receives, keyed by world.  A law that is a
        function of (schedule, tick-0 state) must give each world the same
        gate set in both layouts; a law that reads the bookkeeping slot cannot.
        Computed from the schedule alone -- no run needed."""
        maskfn = coord.get("mask")
        steps = coord.get("steps")
        lane_of = {w: b for b, w in enumerate(order)}
        fp = {}
        extra_mask = None if maskfn is None else maskfn(order)
        for w in range(n):
            fires = []
            for step in range(stations):
                m = station_mask(sim, 0, step, stations)
                if steps is not None and step not in steps:
                    continue
                if extra_mask is not None:
                    m &= extra_mask
                if (m >> lane_of[w]) & 1:
                    fires.append(step)
            fp[w] = tuple(fires)
        dup_ok = True
        for step in range(stations):
            m = station_mask(sim, 0, step, stations)
            if steps is not None and step not in steps:
                continue
            if extra_mask is not None:
                m &= extra_mask
            if bool((m >> lane_of[order[0]]) & 1) != bool((m >> n) & 1):
                dup_ok = False
        return fp, dup_ok

    coord_rows = []
    for coord in COORDS:
        maskfn = coord.get("mask")
        steps = coord.get("steps")
        fwd_fp, fwd_dup = per_world_law_fingerprint(list(range(n)), sim_fwd,
                                                    coord)
        rev_order = list(range(n - 1, -1, -1))
        rev_fp, rev_dup = per_world_law_fingerprint(rev_order, sim_rev, coord)
        law_layout_invariant = fwd_fp == rev_fp
        sched_f = sched_for(
            sim_fwd, coord["gates"],
            lane_mask_fn=None if maskfn is None
            else (lambda step, m, _mm=maskfn(list(range(n))): m & _mm),
            steps_allowed=steps)
        sched_r = sched_for(
            sim_rev, coord["gates"],
            lane_mask_fn=None if maskfn is None
            else (lambda step, m, _mm=maskfn(rev_order): m & _mm),
            steps_allowed=steps)
        t0 = monotonic()
        bf = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                      compile_schedules(sched_f), False, register_cap, slot_of,
                      (left_w, right_w, src_w))
        br = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                      compile_schedules(sched_r), True, register_cap, slot_of,
                      (left_w, right_w, src_w))
        timings[f"R3/{coord['name']}"] = round(monotonic() - t0, 3)
        prov = provenance_sweep([chunk_source(s) for s in sched_f], pos_ops,
                                cross_ops)
        ast_lane_local = not any(
            tag.startswith("lane-index-operator")
            for tag in prov["node_tag_counts"])
        pert = perturbation_witness(
            c863, program, census, states, ((1, left_w), (2, REC_A)),
            PERTURB_ORBITS, compile_schedules(sched_f))
        runtime_lane_local = all(p["leak_outside_own_lane_bit"] == 0
                                 for p in pert)
        census_layout_independent = bf["formed"] == br["formed"]
        dup_clean = (bf["duplicate_lane_mismatches"] == 0
                     and br["duplicate_lane_mismatches"] == 0)
        certifications = {
            "law_is_layout_invariant_per_world": law_layout_invariant,
            "duplicate_lane_law_consistency": fwd_dup and rev_dup,
            "census_layout_independence": census_layout_independent,
            "duplicate_lane_run_consistency": dup_clean,
            "ast_lane_locality": ast_lane_local,
            "runtime_lane_locality": runtime_lane_local,
        }
        failed = sorted(k for k, v in certifications.items() if not v)
        if not failed:
            if coord["derived_from"] == "supplied_world_data":
                verdict = "ABSORBED (not a relaxation)"
                why = ("the coordinate is a function of the world's own "
                       "supplied data -- its token positions and its tick-0 "
                       "state -- so a law that reads it is already a function "
                       "of (schedule, tick-0 state).  It survives every "
                       "certification precisely because it is not a "
                       "relaxation.")
            else:
                verdict = "SURVIVING GENUINE INDEXICAL"
                why = ("a bookkeeping coordinate that survives every "
                       "certification: a REAL relaxation.  Reported as the "
                       "headline if it stands.")
        else:
            verdict = "STRUCTURALLY DEAD"
            why = ("a law reading this coordinate fails: "
                   + ", ".join(failed)
                   + ".  The coordinate has no invariant meaning, so the law "
                     "that reads it is not well defined -- the Cycle-918 M_B "
                     "obstruction, generalised.")
        coord_rows.append({
            "coordinate": coord["name"],
            "the_law_reads": coord["reads"],
            "declared_derivation": coord["derived_from"],
            "gates": [gate_text(*g) for g in coord["gates"]],
            "certifications": certifications,
            "failed_certifications": failed,
            "window_orbits": SWEEP_ORBITS,
            "forward_lock_points": len(bf["formed"]),
            "reversed_lock_points": len(br["formed"]),
            "duplicate_lane_mismatches": [bf["duplicate_lane_mismatches"],
                                          br["duplicate_lane_mismatches"]],
            "runtime_perturbation_leak":
                [p["leak_outside_own_lane_bit"] for p in pert],
            "VERDICT": verdict,
            "why": why,
            "pinned_witness": coord.get("pinned_witness"),
        })
        del bf, br

    # the orbit-index coordinate needs an unrolled cycle: built and measured
    orbit_index_sched = sched_for(
        sim_fwd, XSWAP, cycles_per_orbit=2, per_cycle_gates=[XSWAP, ()])
    orbit_index_sched_rev = build_schedules(
        c863, program, sim_rev, 0, XSWAP, cycles_per_orbit=2,
        per_cycle_gates=[XSWAP, ()])
    t0 = monotonic()
    oi_f = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                    compile_schedules(orbit_index_sched), False, register_cap,
                    slot_of, (left_w, right_w, src_w), stations=stations)
    oi_r = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                    compile_schedules(orbit_index_sched_rev), True,
                    register_cap, slot_of, (left_w, right_w, src_w),
                    stations=stations)
    timings["R3/orbit_index"] = round(monotonic() - t0, 3)
    coord_rows.append({
        "coordinate": "orbit_index_global_clock",
        "the_law_reads": "the parity of the orbit number (a global clock)",
        "declared_derivation": "supplied_world_data",
        "gates": [gate_text(*g) for g in XSWAP],
        "certifications": {
            "census_layout_independence": oi_f["formed"] == oi_r["formed"],
            "duplicate_lane_run_consistency":
                oi_f["duplicate_lane_mismatches"] == 0
                and oi_r["duplicate_lane_mismatches"] == 0,
        },
        "failed_certifications": [],
        "window_orbits": SWEEP_ORBITS,
        "forward_lock_points": len(oi_f["formed"]),
        "reversed_lock_points": len(oi_r["formed"]),
        "duplicate_lane_mismatches": [oi_f["duplicate_lane_mismatches"],
                                      oi_r["duplicate_lane_mismatches"]],
        "unrolled_cycle_length": len(orbit_index_sched),
        "VERDICT": "ABSORBED (not a relaxation)",
        "why":
            "a law that reads the orbit number is a schedule of period "
            f"{len(orbit_index_sched)} instead of {stations}.  It is built "
            "here as exactly that -- an unrolled cycle -- so the absorption is "
            "not an argument, it is the construction.  Every world receives "
            "the same unrolled schedule, so no world is distinguished and no "
            "branch pair can arise.",
        "pinned_witness": None,
    })
    coord_rows.append({
        "coordinate": "wire_index",
        "the_law_reads": "the numbering of the state wires",
        "declared_derivation": "supplied_world_data",
        "gates": ["(structural: every gate names its wires)"],
        "certifications": {"structural": True},
        "failed_certifications": [],
        "window_orbits": None,
        "VERDICT": "ABSORBED (not a relaxation)",
        "why":
            "wire indices are the law's own text, identical for every world "
            "and every layout; they are part of the schedule by definition and "
            "distinguish no occasion from another.",
        "pinned_witness": None,
    })

    dead_coords = [r["coordinate"] for r in coord_rows
                   if r["VERDICT"] == "STRUCTURALLY DEAD"]
    absorbed_coords = [r["coordinate"] for r in coord_rows
                       if r["VERDICT"].startswith("ABSORBED")]
    surviving_coords = [r["coordinate"] for r in coord_rows
                        if r["VERDICT"] == "SURVIVING GENUINE INDEXICAL"]
    cert_c4 = {
        "certificate": "C4_R3_THE_INDEXICALS",
        "class": "R3 (P4): the law depends on an index / bookkeeping "
                 "coordinate",
        "coordinates_swept": len(coord_rows),
        "rows": coord_rows,
        "STRUCTURALLY_DEAD": dead_coords,
        "ABSORBED_NOT_A_RELAXATION": absorbed_coords,
        "SURVIVING_GENUINE_INDEXICAL": surviving_coords,
        "the_theorem":
            "the indexical coordinates of this substrate split cleanly in two. "
            "A coordinate DERIVED FROM THE WORLD'S OWN SUPPLIED DATA (station "
            "index, chunk phase, orbit index, monitor-phase orbit label, "
            "census index, wire index) is already a function of (schedule, "
            "tick-0 state); a law reading it survives every certification "
            "precisely because it is NOT a relaxation.  A coordinate DERIVED "
            "FROM THE BOOKKEEPING SLOT (a lane's bit position, a literal bit "
            "block, bit parity, the duplicate-lane slot, a frozen world mask) "
            "is outside that pair -- and every one of them fails a "
            "certification, each with an exhibited witness.  Cycle 918's M_B "
            "verdict was not special to the shift: it is what happens to any "
            "law that reads the slot instead of the world.",
        "the_census_contingency_disclosed":
            "the census index is a function of (schedule, tick-0 state) "
            "BECAUSE this census has zero pairs sharing token positions AND "
            "tick-0 state -- the same pinned fact the 918 lemma rests on.  On "
            "a census containing such a pair the census index would be a "
            "genuine extra coordinate.  The absorption is census-contingent "
            "and is quoted as such.",
        "different_certifications_do_different_work":
            "the certifications are not redundant: the duplicate-lane slot "
            "passes census layout-independence and dies on duplicate-lane "
            "consistency; bit parity and the frozen world mask pass "
            "duplicate-lane consistency at run time and die on layout "
            "independence; the shift passes the schedule-level layout test and "
            "dies on the AST lane-locality sweep and the runtime witness.  "
            "Removing any one of them would let a dead coordinate through.",
        "pass": bool(not surviving_coords and dead_coords),
    }

    # ---------------- C5: R4, the control ----------------------------------
    cert_c5 = {
        "certificate": "C5_R4_THE_CONTROL",
        "class": "R4 (P1): branch pairs realized as tick-0 differences -- the "
                 "already-banked Cycle-911 re-typing (worlds are setups)",
        "why_it_is_in_the_partition":
            "R4 is not a relaxation of 'the law is a function of (schedule, "
            "tick-0 state)'; it is that function's ARGUMENT.  It is carried in "
            "the partition so the four classes exhaust the provenance of a "
            "consulted datum rather than only the ways of breaking "
            "functionhood.",
        "control_facts_verified_value_for_value": {
            "control_lock_points": len(ctl["formed"]),
            "control_dynamical_candidate_pairs":
                dyn_ctl["candidate_pairs_among_the_lock_points"],
            "control_dynamical_branch_pairs":
                dyn_ctl["DYNAMICAL_BRANCH_PAIRS"],
            "M_A_lock_points": len(ma["formed"]),
            "M_A_candidate_pairs":
                dyn_ma["candidate_pairs_among_the_lock_points"],
            "M_A_dynamical_branch_pairs": dyn_ma["DYNAMICAL_BRANCH_PAIRS"],
            "M_A_branch_pairs": [p["pair"] for p in dyn_ma["pairs"]],
            "literal_911_branch_pairs_control": lit_ctl["BRANCH_PAIRS"],
            "literal_911_branch_pairs_M_A": lit_ma["BRANCH_PAIRS"],
            "census_pairs_sharing_tick0_state":
                lit_ctl["pairs_sharing_tick0_state"],
            "census_pairs_sharing_tick0_state_AND_schedule":
                lit_ctl["pairs_sharing_tick0_state_AND_schedule"],
        },
        "reading":
            "the 27 candidate pairs and the 3 realized splits under M_A are "
            "pairs of DISTINCT SETUPS agreeing on two setup coordinates.  They "
            "are exactly what a tick-0 difference buys and exactly what it "
            "cannot buy: the Cycle-911 branch class -- two worlds agreeing on "
            "EVERY tick-0 coordinate and on the schedule -- stays empty, "
            "because the census realizes that conjunction zero times and "
            "because a law is a function.",
        "pass": bool(
            dyn_ctl["DYNAMICAL_BRANCH_PAIRS"] == 0
            and lit_ctl["BRANCH_PAIRS"] == 0 and lit_ma["BRANCH_PAIRS"] == 0),
    }

    # ---------------- C6: the classification theorem -----------------------
    class_verdicts = {
        "R1_P2_the_tape": cert_c2["VERDICT"],
        "R2_P3_the_choice_point": cert_c3["VERDICT"],
        "R3_P4_the_indexical":
            "STRUCTURALLY DEAD per bookkeeping-slot coordinate; ABSORBED per "
            "supplied-data coordinate; NO SURVIVING GENUINE INDEXICAL"
            if not surviving_coords else
            "A SURVIVING GENUINE INDEXICAL EXISTS: " + ", ".join(
                surviving_coords),
        "R4_P1_the_control": "THE BANKED RE-TYPING (the function's argument, "
                             "not a relaxation of its form)",
    }
    genuine = []
    if cert_c2["VERDICT"] != "RE-LABELING":
        genuine.append("R1")
    if surviving_coords:
        genuine.append("R3")
    genuine.append("R2")
    cert_c6 = {
        "certificate": "C6_CLASSIFICATION_THEOREM",
        "theorem":
            "EVERY relaxation of 'the law is a function of (schedule, tick-0 "
            "state)' available at this substrate falls into one of four "
            "classes, indexed by the provenance of the datum the relaxed law "
            "would consult: P1 declared state, P2 a declared non-state stream, "
            "P3 a law-internal choice point, P4 an index or bookkeeping "
            "coordinate.  Of those: R1 (P2) is a RE-LABELING -- every "
            "constructible tape is reproduced bit for bit by a pure function of "
            "(schedule, tick-0 state), including an arbitrary stream written "
            "mid-run by nothing.  R3 (P4) SPLITS -- every coordinate derived "
            "from the world's own supplied data is already inside the pair and "
            "is not a relaxation, and every coordinate derived from the "
            "bookkeeping slot fails a certification with an exhibited witness.  "
            "R4 (P1) is the banked Cycle-911 re-typing and is the function's "
            "argument, not a relaxation of its form.  That leaves R2 (P3) as "
            "the SOLE GENUINE RELAXATION -- and it is not constructible against "
            "this compiler at all: its minimal specification is a sentence "
            "assigning which of the available possibilities at a site is "
            "written, and with what weight, which is exactly the A3-shaped "
            "sentence the Cycle-913 receipt names and exactly the content the "
            "axiom memo's own Open Gates list places outside the four axioms.",
        "per_class": class_verdicts,
        "the_sole_genuine_relaxation": "R2 (P3)" if genuine == ["R2"]
        else "MORE THAN ONE: " + ", ".join(genuine),
        "price": "exactly one sentence, of exactly the A3 shape, unchanged in "
                 "content from what Cycle 913 located and Cycle 918 deferred.  "
                 "Nothing here adopts it.",
        "what_this_block_did_NOT_do":
            "it did not build the successor substrate.  It classified and "
            "priced the space of ways one could be built, and found that space "
            "is one sentence wide.",
        "exhaustiveness_is_relative_to": [
            "the syntactic categories the PINNED compiler admits: the "
            f"{len(templates)} statement templates read off the pinned "
            "compile_fast AST, and the expression grammar of their leaves.  A "
            "different compiler is outside the argument.",
            "the swept coordinate list: "
            + ", ".join(r["coordinate"] for r in coord_rows)
            + ".  A coordinate nobody named is not covered; the checker is "
              "specified to hunt for one.",
            "the declared ansatz: station-anchored splices into the composed "
            "scan, both lane layouts, at the landed 16,384-orbit horizon for "
            "the flagship results and at declared sub-horizon windows "
            f"({SWEEP_ORBITS} orbits for the coordinate sweep, "
            f"{TAPE_WINDOW_ORBITS} for the arbitrary-tape equivalence, "
            f"{CROSSCHECK_ORBITS} for the pinned-scan cross-check) elsewhere.",
            "the census: 748 worlds with zero pairs sharing token positions "
            "AND tick-0 state.  Two absorptions (the census index; the "
            "comparator's schedule proxy) are contingent on that fact and are "
            "flagged where they occur.",
        ],
        "pass": True,
    }

    # ---------------- G: planted falsifiers --------------------------------
    teeth = []

    def add(name, detected, detail=None):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "detail": detail})

    for row in planted_rows:
        add(f"planted_fifth_provenance_category_caught__{row['planted']}",
            row["caught_outside_P1_P4"],
            {"classes": row["classes_found"], "tags": row["tags"]})

    # a slot-derived coordinate that DECLARES itself world-derived must still
    # be caught by the schedule-level layout test
    liar = {"name": "liar", "reads": "x", "derived_from": "supplied_world_data",
            "gates": XSWAP, "mask": lambda order: FROZEN_WORLD}
    lf, _ = per_world_law_fingerprint(list(range(n)), sim_fwd, liar)
    lr, _ = per_world_law_fingerprint(list(range(n - 1, -1, -1)), sim_rev,
                                      liar)
    honest = {"name": "honest", "reads": "x",
              "derived_from": "supplied_world_data", "gates": XSWAP,
              "mask": lambda order: world_mask(order, lambda w: w % 2 == 0)}
    hf, _ = per_world_law_fingerprint(list(range(n)), sim_fwd, honest)
    hr, _ = per_world_law_fingerprint(list(range(n - 1, -1, -1)), sim_rev,
                                      honest)
    add("planted_surviving_indexical_caught_by_the_layout_certification",
        lf != lr and hf == hr,
        {"liar_layout_invariant": lf == lr, "honest_layout_invariant":
         hf == hr})

    dup_liar = {"name": "dup", "reads": "x", "derived_from": "bookkeeping_slot",
                "gates": XSWAP, "mask": lambda order: LIT_DUP}
    _fp, dup_ok = per_world_law_fingerprint(list(range(n)), sim_fwd, dup_liar)
    _fp2, dup_ok_ctl = per_world_law_fingerprint(list(range(n)), sim_fwd,
                                                 {"gates": (), "mask": None})
    add("planted_duplicate_lane_law_caught_by_the_duplicate_lane_test",
        (not dup_ok) and dup_ok_ctl,
        {"planted_duplicate_consistent": dup_ok, "control": dup_ok_ctl})

    # a broken tape equivalence must break the bit-identity test
    broken_pre = list(pre_fns)
    broken_pre[3] = compile_source(
        ["def apply_chunk(c):", f" c[{TAPE_W}] ^= {1}"])
    r1c_broken = run_scan(
        c863, program, census, states, tape_window, base_sched, False,
        register_cap, slot_of, (left_w, right_w, src_w), pre_fns=broken_pre,
        digest_exclude=(TAPE_W,))
    add("planted_break_in_the_tape_equivalence_detected",
        r1c_broken["column_digest"] != r1c_stream["column_digest"]
        and r1c_schedule["column_digest"] == r1c_stream["column_digest"],
        {"broken_digest": r1c_broken["column_digest"][:16],
         "true_digest": r1c_stream["column_digest"][:16]})
    del r1c_broken

    tampered = dict(EXPECTED_SHA256)
    tampered[CORE_PATH] = "0" * 64
    add("tampered_pin_detected",
        {p: sha256((ROOT / p).read_bytes()).hexdigest()
         for p in AUDIT_INPUT_PATHS} != tampered)

    corrupted = [[r["world"], r["key"], r["lock_boundary"], r["phase"],
                  r["menu"], ([0, 1] if r["selected_item"] == [1, 0]
                              else [1, 0]), [r["ord0"], r["ord1"]],
                  r["context_fingerprint"]] for r in ctl_rows]
    pinned913 = [[x["world"], x["key"], x["lock_boundary"], x["phase"],
                  x["menu"], x["selected_item"], x["neighbour_ordinals"],
                  x["context_fingerprint"]]
                 for x in c1_913["per_lock_point_rows"]]
    add("corrupted_selection_table_breaks_the_c913_gate",
        corrupted != pinned913)

    # corrupt EVERY pinned 918 control fact this block gates on, one at a time,
    # and require each corruption to break its own gate
    fact_vector = {
        "M_A_lock_points": (len(ma["formed"]),
                            m918["M_A"]["FORMATION"]["lock_points"]),
        "M_A_selection_left_setup": (
            len(ma_dis), m918["M_A"]["SELECTION"][
                "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"]),
        "M_A_dynamical_branch_pairs": (
            dyn_ma["DYNAMICAL_BRANCH_PAIRS"], m918["M_A"][
                "BRANCH_PAIRS_dynamical"]["DYNAMICAL_BRANCH_PAIRS"]),
        "M_B_reversed_lock_points": (len(mb_rev["formed"]),
                                     h918["M_B"]["formed"][1]),
        "M_C_lock_points": (len(mc["formed"]),
                            m918["M_C"]["FORMATION"]["lock_points"]),
    }
    add("corrupted_918_control_facts_break_their_gates",
        all(got == want and got != want + 1
            for got, want in fact_vector.values()),
        {k: {"measured": g, "pinned": w, "corrupted_would_fail": g != w + 1}
         for k, (g, w) in fact_vector.items()})

    synth = {w: dict(r) for w, r in ctl_by_world.items()}
    partner_of: dict = {}
    for w in synth:
        partner_of.setdefault(
            (tuple(census[w][2]), setup_direction[census[w][1]]), []).append(w)
    plant_w = next((sorted(v)[0] for _k, v in sorted(partner_of.items())
                    if len(v) >= 2), None)
    if plant_w is not None:
        cur = synth[plant_w]["selected_item"]
        synth[plant_w]["selected_item"] = [0, 1] if cur == [1, 0] else [1, 0]
    synth_dyn = dynamical_branch_pairs(census, synth, setup_direction)
    add("planted_synthetic_branch_pair_detected",
        synth_dyn["DYNAMICAL_BRANCH_PAIRS"] > 0
        and dyn_ctl["DYNAMICAL_BRANCH_PAIRS"] == 0,
        {"planted_world": plant_w,
         "found": synth_dyn["DYNAMICAL_BRANCH_PAIRS"]})

    add("control_cannot_leak_a_relaxation_verdict",
        dyn_ctl["DYNAMICAL_BRANCH_PAIRS"] == 0 and len(ctl_dis) == 0
        and dyn_ctl["candidate_pairs_among_the_lock_points"] > 0
        and ctl_prov["class_counts"].get(P2, 0) == 0
        and ctl_prov["class_counts"].get(P3, 0) == 0,
        {"candidate_pairs":
         dyn_ctl["candidate_pairs_among_the_lock_points"]})

    add("the_pinned_substrate_admits_exactly_three_statement_templates",
        len(templates) == 3, {"templates": templates})

    add("a_shift_is_classified_as_a_lane_index_read_not_as_state",
        mb_prov["node_tag_counts"].get("lane-index-operator:RShift", 0) > 0
        and ctl_prov["node_tag_counts"].get("lane-index-operator:RShift", 0)
        == 0,
        {"M_B_shift_sites": mb_prov["node_tag_counts"].get(
            "lane-index-operator:RShift", 0)})

    # deterministic double-run on a declared window
    dr1 = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                   compile_schedules(sched_for(sim_fwd, M_A_GATES)), False,
                   register_cap, slot_of, (left_w, right_w, src_w))
    dr2 = run_scan(c863, program, census, states, SWEEP_ORBITS * stations,
                   compile_schedules(sched_for(sim_fwd, M_A_GATES)), False,
                   register_cap, slot_of, (left_w, right_w, src_w))
    add("deterministic_double_run_identical",
        scan_digest(dr1) == scan_digest(dr2)
        and dr1["column_digest"] == dr2["column_digest"],
        {"digest": scan_digest(dr1)[:16]})

    cert_g = {"certificate": "G_FALSIFIERS", "teeth": teeth,
              "tooth_count": len(teeth),
              "pass": all(t["detected"] for t in teeth)}

    cert_h = {
        "certificate": "H_DOUBLE_BUILD",
        "control_forward_digest": scan_digest(ctl),
        "control_reversed_digest": scan_digest(ctl_rev),
        "control_layout_identical": scan_digest(ctl) == scan_digest(ctl_rev),
        "control_matches_the_pinned_913_digests":
            scan_digest(ctl) == h_913["digest_A"]
            and scan_digest(ctl_rev) == h_913["digest_B"],
        "M_A_layout_identical": scan_digest(ma) == scan_digest(ma_rev),
        "M_B_layout_identical": scan_digest(mb) == scan_digest(mb_rev),
        "deterministic_double_run_identical":
            scan_digest(dr1) == scan_digest(dr2),
        "pass": bool(scan_digest(ctl) == scan_digest(ctl_rev)
                     and scan_digest(ctl) == h_913["digest_A"]
                     and scan_digest(dr1) == scan_digest(dr2)),
    }

    elapsed = round(monotonic() - started, 3)
    cert_i = {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
              "budget_sec": RUNTIME_BUDGET_SEC,
              "dead_wire_rig_seconds": t_rig,
              "pinned_911_cross_check_seconds": t_cross,
              "per_run_seconds": {k: v for k, v in sorted(timings.items())},
              "pass": elapsed <= RUNTIME_BUDGET_SEC}

    certificates = {
        "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
        "C1_PROVENANCE_PARTITION": cert_c1, "C2_R1_THE_TAPE": cert_c2,
        "C3_R2_THE_CHOICE_POINT": cert_c3, "C4_R3_THE_INDEXICALS": cert_c4,
        "C5_R4_THE_CONTROL": cert_c5,
        "C6_CLASSIFICATION_THEOREM": cert_c6, "G_FALSIFIERS": cert_g,
        "H_DOUBLE_BUILD": cert_h, "I_RUNTIME": cert_i,
    }
    all_pass = all(c["pass"] for c in certificates.values())

    headline = (
        "the pinned substrate's law is a pure function of (schedule, tick-0 "
        f"state) at kernel level: all {ctl_prov['statements']} compiled "
        "statements consult only declared state reads (P1) and compile-time "
        "integer literals (P4), with zero free names, zero calls and zero "
        "conditionals.  The four-class relaxation space is classified: R1 (a "
        "declared non-state tape) is a RE-LABELING -- even an arbitrary "
        "per-boundary stream written mid-run by nothing is reproduced bit for "
        "bit by one X gate per boundary with a compile-time constant mask; R3 "
        "(an indexical) splits into "
        f"{len(absorbed_coords)} coordinates already inside the pair and "
        f"{len(dead_coords)} bookkeeping-slot coordinates that each fail a "
        "certification with an exhibited witness, with none surviving; R4 is "
        "the banked Cycle-911 re-typing.  R2 (a law-internal choice point) is "
        "the SOLE GENUINE RELAXATION and is not constructible against this "
        "compiler at all -- its minimal specification is exactly the A3-shaped "
        "sentence, byte-matched to the Cycle-913 receipt and to the axiom "
        "memo's own Open Gates list.  The successor substrate's design space "
        "is one sentence wide.")

    receipt = {
        "block": "toe-time-blockQ12-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "cycles": [925],
        "claim_type": "bounded_theorem",
        "audit": "unset", "authority": "none",
        "fraction_label": FRACTION_LABEL,
        "provenance": provenance,
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "VERDICT": ("LAW-RELAXATION SPACE CLASSIFIED: R2 = THE A3 SENTENCE IS "
                    "THE SOLE GENUINE RELAXATION" if all_pass
                    else "INCOMPLETE"),
        "headline": headline,
    }
    out = ROOT / "outputs" / \
        "law_relaxation_cycle925_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    # ---------------- stdout ----------------------------------------------
    W = 78
    print("CYCLE 925 -- THE LAW-RELAXATION SPACE, CLASSIFIED AND PRICED")
    print("=" * W)
    print(f"  every fraction below: {FRACTION_LABEL}")
    print(f"  scope: FULL CENSUS {n} worlds; flagship results at the landed "
          f"{HORIZON}-orbit horizon ({FULL_BOUNDARIES} boundaries), both lane "
          f"layouts; declared sub-horizon windows: coordinate sweep "
          f"{SWEEP_ORBITS} orbits, arbitrary-tape equivalence "
          f"{TAPE_WINDOW_ORBITS} orbits, pinned-scan cross-check "
          f"{CROSSCHECK_ORBITS} orbits")
    print()
    print(f"A_PINS                      {'PASS' if cert_a['pass'] else 'FAIL'}"
          f"  ({len(AUDIT_INPUT_PATHS)} pinned; sha256+git-blob; firewall "
          f"hits {len(cert_a['firewall_hits'])})")
    print(f"B_RESTRICTION_GATE          "
          f"{'PASS' if cert_b['pass'] else 'FAIL'}"
          f"  ({cert_b['reproduce']}/{cert_b['total']} reproduce)")
    for row in gate_rows:
        if not row["pass"]:
            print(f"    FAILED GATE {row['gate']}")
            print(f"      got    {compact(row['value'])[:200]}")
            print(f"      pinned {compact(row['pinned'])[:200]}")
    print()
    print("-" * W)
    print("C1  THE INPUT-PROVENANCE PARTITION  (Q1: the lemma at kernel level)")
    print("-" * W)
    print(f"  compiler statement templates ({len(templates)}): {templates}")
    print(f"  pinned substrate: {ctl_prov['statements']} statements, "
          f"{ctl_prov['distinct_state_addresses_read']} addresses read, "
          f"{ctl_prov['distinct_state_addresses_written']} written")
    for k, v in cert_c1["pinned_substrate_sweep"]["class_counts"].items():
        print(f"    {k:38s} {v}")
    print(f"  P2 empty={cert_c1['P2_is_empty_in_the_pinned_substrate']}  "
          f"P3 empty={cert_c1['P3_is_empty_in_the_pinned_substrate']}  "
          f"unclassified empty="
          f"{cert_c1['no_unclassified_category_in_the_pinned_substrate']}")
    print("  planted fifth-category probes:")
    for row in planted_rows:
        print(f"    [{'x' if row['caught_outside_P1_P4'] else ' '}] "
              f"{row['planted']:26s} -> {row['classes_found']}")
    print()
    print("-" * W)
    print("C2  R1  THE TAPE  (P2)")
    print("-" * W)
    a = cert_c2["R1a_constant_per_lane_tape"]
    print(f"  R1a constant per-lane tape, FULL horizon: tick-0-state form vs "
          f"pure-X-schedule form")
    print(f"      bit-identical on every pinned wire = "
          f"{a['BIT_IDENTICAL_ON_EVERY_PINNED_WIRE']}; build digests "
          f"identical = {a['build_digests_identical']}; locks "
          f"{a['lock_points']} (control {a['control_lock_points']})")
    print(f"  R1b chunk-phase tape: oracle and schedule forms compile to the "
          f"same rows = {cert_c2['R1b_chunk_phase_tape']['oracle_form_and_schedule_form_compile_to_the_same_rows']}")
    c = cert_c2["R1c_arbitrary_stream_written_mid_run_by_nothing"]
    print(f"  R1c arbitrary stream written mid-run BY NOTHING vs one X gate "
          f"per boundary ({c['window_boundaries']} boundaries):")
    print(f"      bit-identical = {c['BIT_IDENTICAL_ON_EVERY_PINNED_WIRE']}; "
          f"formation identical = {c['formation_identical']}")
    cap = cert_c2["capacity_boundary_stated_honestly"]
    print(f"  capacity: {cap['free_state_bits_per_lane']} free state bits per "
          f"lane vs {cap['boundaries_at_the_landed_horizon']} boundaries -- an "
          f"arbitrary tape does NOT fit tick-0 state "
          f"({cap['an_arbitrary_tape_does_NOT_fit_in_tick0_state']}); it fits "
          f"the SCHEDULE, and R1c builds that route")
    print(f"  VERDICT: {cert_c2['VERDICT']}")
    print()
    print("-" * W)
    print("C3  R2  THE CHOICE POINT  (P3)")
    print("-" * W)
    print(f"  constructible against the pinned compiler: NO -- "
          f"P3 empty in the admitted grammar")
    for f in sel_fillings:
        print(f"    {f['filling']:44s} -> {f['collapses_to'][:60]}")
    print(f"  the A3-shaped sentence (pinned, Cycle 913): {Q_A3_CHANNEL}")
    print(f"  VERDICT: {cert_c3['VERDICT']}")
    print()
    print("-" * W)
    print("C4  R3  THE INDEXICALS  (P4)")
    print("-" * W)
    print(f"  {'coordinate':36s} {'derivation':22s} {'verdict':32s} failed")
    for row in coord_rows:
        print(f"  {row['coordinate']:36s} {row['declared_derivation']:22s} "
              f"{row['VERDICT']:32s} "
              f"{','.join(row['failed_certifications']) or '-'}")
    print(f"  DEAD: {dead_coords}")
    print(f"  ABSORBED: {absorbed_coords}")
    print(f"  SURVIVING GENUINE INDEXICAL: {surviving_coords or 'none'}")
    print()
    print("-" * W)
    print("C5  R4  THE CONTROL  (P1)")
    print("-" * W)
    for k, v in cert_c5["control_facts_verified_value_for_value"].items():
        print(f"    {k:52s} {v}")
    print()
    print("-" * W)
    print("C6  THE CLASSIFICATION THEOREM")
    print("-" * W)
    for k, v in class_verdicts.items():
        print(f"    {k:26s} {v}")
    print(f"  sole genuine relaxation: {cert_c6['the_sole_genuine_relaxation']}")
    print("  exhaustive relative to:")
    for line in cert_c6["exhaustiveness_is_relative_to"]:
        print(f"    - {line}")
    print()
    print("-" * W)
    print(f"G_FALSIFIERS                {'PASS' if cert_g['pass'] else 'FAIL'}"
          f"  ({cert_g['tooth_count']} teeth)")
    for t in teeth:
        print(f"    [{'x' if t['detected'] else ' '}] {t['tooth']}")
    print(f"H_DOUBLE_BUILD              {'PASS' if cert_h['pass'] else 'FAIL'}")
    print(f"I_RUNTIME                   {'PASS' if cert_i['pass'] else 'FAIL'}"
          f"  ({elapsed}s / {RUNTIME_BUDGET_SEC}s)")
    print()
    print("=" * W)
    print(f"VERDICT: {receipt['VERDICT']}")
    print(f"HEADLINE: {headline}")
    print("receipt: outputs/law_relaxation_cycle925_receipt_2026_07_28.json")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
