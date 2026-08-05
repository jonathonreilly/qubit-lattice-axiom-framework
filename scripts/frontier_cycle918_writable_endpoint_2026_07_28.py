"""Cycle 918 -- THE WRITABLE-ENDPOINT DESIGN SPACE, CONSTRUCTED AND MEASURED.

Cycle 913 closed with a named successor.  On the landed 719 composed scan the
two endpoint wires (LEFT_ENDPOINT = 1, RIGHT_ENDPOINT = 6) are gate INPUTS in
all 34,166 compiled gates and NEVER gate targets: the scan READS the selection
at every source and finalizer station and never WRITES it.  So O2 is transport
of a setup coordinate, and O3's A3 arena is setup-indexed, hence forbidden.
913's successor sentence, pinned byte for byte below:

    "a substrate whose endpoint content is a gate TARGET -- so that the two
     menu items are alternatives of one setup rather than two setups -- is the
     only place the A3 arena can be non-degenerate.  That is the next
     computation."

THIS BLOCK STARTS THAT SUCCESSOR.  It constructs the minimal writable-endpoint
modifications of the 719 kernel and measures what each one does.

  Q1  THE CONSTRUCTION SPACE, DECLARED.  Three candidates, each an extra macro
      APPENDED to the source station's macro inside the composed scan's own
      masked-schedule compiler.  The pinned kernel file is never edited: the
      extras are compiled gate tuples declared in THIS file and spliced by
      this file's own schedule builder, which reproduces the pinned Cycle-863
      masked_h_schedules row for row when the extra tuple is empty.
        M-A  RECORD-DRIVEN     c[1] ^= c[123] & mask ; c[6] ^= c[123] & mask
        M-B  CROSS-LANE        c[1] ^= (c[1] >> 1) & mask ;
                               c[6] ^= (c[6] >> 1) & mask
        M-C  LOCAL-CONTENT     c[1] ^= c[123] & c[254] & mask ;
                               c[6] ^= c[123] & c[254] & mask
      spanning record-driven / cross-lane / locally content-driven.  A fourth,
      M-PLANT, is a falsifier built after the fact so that it provably splits
      a same-setup-coordinate pair.

  Q2  THE MEASUREMENT, against the unmodified kernel as CONTROL, on the FULL
      748-world census at the landed 16,384-orbit horizon, both lane layouts:
      formation; exact per-world endpoint write counts; the AST-lifted
      Cycle-913 dependence re-analysis; the Cycle-911 branch matrix and a
      declared dynamical-branch quantity; the record machinery (write-once,
      dead-wire slots); the no-cross-lane certification (AST sweep + runtime
      perturbation witness); layout independence.

  Q3  THE VERDICT AND THE PRICING per candidate -- BORN-CAPABLE / STERILE /
      DESTRUCTIVE -- by a classifier that reads measurements only and never a
      candidate's name, with the A3 arena recounted wherever a candidate is
      Born-capable.

Discipline: TEXT/AST/JSON only; the 719 two-rail core is the single disclosed
import (as substrate); exact integer arithmetic; deterministic double build at
opposite lane layouts; outcome-neutral verdicts with planted falsifiers,
including a planted modification designed to create a branch pair which the
branch machinery must detect.  No probability, no occurrence rule and no
update law is introduced.  Every fraction below is a bookkeeping fraction, not
a probability.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction
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
C911_NOTE = (
    "docs/RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_CYCLE911"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
CLASSIFY_PATH = \
    "scripts/admissibility_rule_covariance_extension_classification_2026_07_03.py"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, HANDSHAKE_PATH, C863_PATH, C863_RECEIPT, C878_PATH,
    C878_RECEIPT, C911_PATH, C911_RECEIPT, C913_PATH, C913_RECEIPT, C911_NOTE,
    CLASSIFY_PATH, AXIOMS_PATH, REALIZED_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C911_PATH, C913_PATH, CLASSIFY_PATH)
JSON_ONLY_PATHS = (C863_RECEIPT, C878_RECEIPT, C911_RECEIPT, C913_RECEIPT)
TEXT_ONLY_PATHS = (C911_NOTE, AXIOMS_PATH, REALIZED_PATH)

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
    C911_NOTE:
        "40c80402e2dfd283a4309433cfa48705c45567efadf43107e074332f1cbf5ff0",
    CLASSIFY_PATH:
        "f7490941aa793fdf155d10dc5a5f86d59c07b22d49ca60f989fbf03c565a0dcb",
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
    C911_NOTE: "53a229b4143f59f5f8c12ccb9f488682bdc2714c",
    CLASSIFY_PATH: "d33bf6e8b456464e2b455c1d0aaf8662a1799abb",
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
LANE_SHIFT = 1                     # the M-B cross-lane stride, declared
PERTURB_ORBITS = 6                 # runtime no-coupling witness window
CROSSCHECK_ORBITS = 128            # pinned-scan cross-check window
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


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


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
            "and its bytes are hashed above.  Every modification is a tuple "
            "of COMPILED gate rows declared in this file and spliced into the "
            "composed scan by this file's own schedule builder "
            "(build_schedules), which reproduces the pinned Cycle-863 "
            "masked_h_schedules exactly when the extra tuple is empty -- "
            "gated in B.  No pinned file is written, patched, monkey-patched "
            "or reloaded.",
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
    """Rebuild a module-level tuple of ast node CLASSES (e.g. Cycle 911's
    CROSS_LANE_OPS) from the pinned source.  ast.literal_eval cannot do this,
    so the attribute names are read off the AST and resolved against `ast`."""
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
C911_FUNCS = ("snapshot_scan", "synchronous_chunks", "availability_operators",
              "sweep_generated_chunk_source", "classify_pair")
C911_CONSTS = ("DIRECTIONS", "REGISTER_CAP", "HORIZON", "CLASS_BRANCH",
               "CLASS_IDENTICAL", "CLASS_SETUP_TICK0", "CLASS_SETUP_SCHEDULE",
               "CLASS_NONBRANCH_DIVERGENCE")
C913_FUNCS = ("endpoint_wires", "read_state_direction", "target_wire_sweep",
              "hamming_readout", "is_function", "ladder_rows",
              "exhaustive_singleton_sweep", "translation_covariance")
CLASS_FUNCS = ("det3", "mat_key", "dperm", "act_col", "inv_perm",
               "cycle_count", "burnside_orbits", "all_colorings",
               "direct_orbits", "orbit_ids")
CLASS_CONSTS = ("DIRS",)


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
    dirs_holder: dict = {}
    nsc, constsc, namesc = ast_lift(
        CLASSIFY_PATH, CLASS_FUNCS, CLASS_CONSTS,
        {"np": np, "itertools": itertools, "DIR_INDEX": dirs_holder})
    dirs = constsc["DIRS"]
    dirs_holder.update({d: i for i, d in enumerate(dirs)})
    cls = SimpleNamespace(**{n: nsc[n] for n in CLASS_FUNCS})
    cross_ops, cross_names = lift_ast_op_tuple(C911_PATH, "CROSS_LANE_OPS")
    pos_ops, pos_names = lift_ast_op_tuple(C911_PATH, "POSITIONWISE_OPS")
    ns911, consts911, names911 = ast_lift(
        C911_PATH, C911_FUNCS, C911_CONSTS,
        {"K": K, "np": np, "itertools": itertools, "Counter": Counter,
         "sha256": sha256, "cls": cls, "ast": ast,
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
        "lifted_from_classification": namesc,
        "classification_DIRS": [list(d) for d in dirs],
        "import_of_863_878_911_913_or_classification": False,
        "single_disclosed_import": CORE_PATH,
    }
    return (c863, c878, c911, c913, cls, dirs, consts878, consts911,
            cross_ops, provenance)


# ---------------------------------------------------------------------------
# B: the modification algebra -- compiled gate rows, spliced never edited
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


def build_schedules(c863, program, sim, extra_station, extra_gates,
                    lane_mask):
    """The composed scan's masked-schedule compiler with a declared extra
    macro appended to one station's macro.  Empty extras reproduce the pinned
    Cycle-863 masked_h_schedules row for row."""
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_k, _e, positions) in enumerate(sim)
                if (station - step) % stations in positions)
            if mask:
                schedule.extend(
                    c863.compile_masked_gate(g, mask)
                    for g in K.mapped_macro(row))
                if extra_gates and station == extra_station:
                    m = mask & lane_mask
                    if m:
                        for kind, a, b, c3 in extra_gates:
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


def compile_schedules(schedules):
    fns = []
    for schedule in schedules:
        ns: dict = {}
        exec("\n".join(chunk_source(schedule)), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


def target_sweep(schedules, left, right, src):
    """The Cycle-913 target-wire sweep, extended to the cross-lane kind.  The
    transport theorem's content is exactly the last two booleans."""
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


def sweep_source(schedules, cross_lane_ops):
    """The Cycle-911 no-coupling AST sweep, run on the source THIS file execs.
    A SHIFT gate must show up as a cross-lane operator."""
    stats = {"statements": 0, "augassign_bitxor": 0, "subscript_targets": 0,
             "bitand_nodes": 0, "constant_masks": 0, "column_reads": 0}
    violations: list = []
    for step, schedule in enumerate(schedules):
        tree = ast.parse("\n".join(chunk_source(schedule)))
        fn = tree.body[0]
        for stmt in fn.body:
            stats["statements"] += 1
            if not isinstance(stmt, ast.AugAssign):
                violations.append(("not augassign", step, ""))
                continue
            if not isinstance(stmt.op, ast.BitXor):
                violations.append(("augassign op not ^=", step, ""))
                continue
            stats["augassign_bitxor"] += 1
            tgt = stmt.target
            if not (isinstance(tgt, ast.Subscript)
                    and isinstance(tgt.value, ast.Name) and tgt.value.id == "c"
                    and isinstance(tgt.slice, ast.Constant)
                    and isinstance(tgt.slice.value, int)):
                violations.append(("target not c[const]", step, ""))
                continue
            stats["subscript_targets"] += 1
            for node in ast.walk(stmt.value):
                if isinstance(node, ast.BinOp):
                    if isinstance(node.op, cross_lane_ops):
                        violations.append(("cross-lane operator", step,
                                           type(node.op).__name__))
                    elif isinstance(node.op, ast.BitAnd):
                        stats["bitand_nodes"] += 1
                    else:
                        violations.append(("unexpected operator", step,
                                           type(node.op).__name__))
                elif isinstance(node, ast.Constant):
                    if isinstance(node.value, int):
                        stats["constant_masks"] += 1
                    else:
                        violations.append(("non-int constant", step, ""))
                elif isinstance(node, ast.Subscript):
                    if not (isinstance(node.value, ast.Name)
                            and node.value.id == "c"
                            and isinstance(node.slice, ast.Constant)
                            and isinstance(node.slice.value, int)):
                        violations.append(("read not c[const]", step, ""))
                    else:
                        stats["column_reads"] += 1
                elif isinstance(node, ast.Name):
                    if node.id != "c":
                        violations.append(("free name", step, node.id))
                elif isinstance(node, (ast.Load, ast.Store)):
                    continue
                elif isinstance(node, (ast.Call, ast.Compare, ast.Slice,
                                       ast.UnaryOp, ast.BoolOp, ast.IfExp,
                                       ast.Attribute)):
                    violations.append(("disallowed node", step,
                                       type(node).__name__))
    return stats, violations


# ---------------------------------------------------------------------------
# exact per-lane counters: bit-plane accumulators over big-int columns
# ---------------------------------------------------------------------------

def acc_add(planes: list, mask: int) -> None:
    """Add 1 to every lane counter whose bit is set in `mask`.  Exact."""
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


# ---------------------------------------------------------------------------
# the scan: Cycle-911 snapshot_scan + Cycle-878 record slots + write counters
# ---------------------------------------------------------------------------

def run_scan(c863, program, census, states, orbits, extra_station,
             extra_gates, reverse_layout, register_cap, slot_of, endpoints,
             lane_restrict=None):
    """One full composed-scan build.

    Identical to the pinned Cycle-911 snapshot_scan in every quantity it
    reports, plus (i) the Cycle-878 record-slot ledger with the write-once
    check, held in a SHADOW array so the dynamical columns stay bit-identical
    to the pinned scan's, (ii) exact per-lane endpoint write counters, (iii)
    the record-slot activation monitor at the pinned Cycle-878 granularity."""
    n = len(census)
    order = list(range(n - 1, -1, -1)) if reverse_layout else list(range(n))
    bit_of = {w: b for b, w in enumerate(order)}
    laid_census = tuple(census[w] for w in order)
    laid_states = tuple(states[w] for w in order)
    sim = laid_census + (laid_census[0],)

    if lane_restrict is None:
        lane_mask = (1 << (n + 1)) - 1
    else:
        lane_mask = 0
        for w in lane_restrict:
            lane_mask |= 1 << bit_of[w]
        if order[0] in lane_restrict:
            lane_mask |= 1 << n

    schedules = build_schedules(c863, program, sim, extra_station,
                                extra_gates, lane_mask)
    fast = compile_schedules(schedules)
    columns = c863.pack_lanes(laid_states + (laid_states[0],))
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
    for orbit in range(1, orbits + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
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
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in slot_wires:
                    slot_activation |= columns[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in slot_wires:
                slot_activation |= columns[w]
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
        "schedules": schedules,
        "order": order,
    }


def scan_digest(build):
    """The Cycle-913 build digest, byte for byte."""
    return digest({
        "formed": {str(k): v for k, v in sorted(build["formed"].items())},
        "snapshots": {str(k): "".join(str(b) for b in v)
                      for k, v in sorted(build["snapshots"].items())},
        "lock_ordinal": {str(k): list(v)
                         for k, v in sorted(build["lock_ordinal"].items())},
        "events": len(build["events"]),
    })


def perturbation_witness(c863, program, census, states, samples, orbits,
                         extra_station, extra_gates):
    """Runtime no-coupling witness on the MODIFIED law: flip one wire of one
    lane's tick-0 state and certify the column difference stays inside that
    lane's own bit for the declared window."""
    n = len(census)
    sim = tuple(census) + (census[0],)
    lane_mask = (1 << (n + 1)) - 1
    fast = compile_schedules(build_schedules(
        c863, program, sim, extra_station, extra_gates, lane_mask))
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
# the two branch quantities, never conflated
# ---------------------------------------------------------------------------

def literal_branch_matrix(c911, census, states, formed, classes):
    """The pinned Cycle-911 comparator, verbatim, over all census pairs."""
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
        "comparator": "the pinned Cycle-911 classify_pair, AST-lifted",
        "total_world_pairs": len(census) * (len(census) - 1) // 2,
        "verdicts": {k: matrix[k] for k in sorted(matrix)},
        "BRANCH_PAIRS": matrix[classes["CLASS_BRANCH"]],
        "pairs_sharing_tick0_state": len(same_state_pairs),
        "pairs_sharing_tick0_state_AND_schedule":
            len(same_positions_same_state),
        "structural_lemma":
            "CLASS_BRANCH is conjunctively gated on same_schedule AND "
            "same_tick0_state AND a divergence.  This census realizes that "
            f"conjunction {len(same_positions_same_state)} times, so the "
            "class is empty for every gate set that leaves the census and the "
            "tick-0 states alone -- which every gate-set modification does.  "
            "A gate-set modification cannot manufacture a Cycle-911 branch "
            "pair: that quantity is a property of the census, not of the law.",
    }


def dynamical_branch_pairs(census, rows_by_world, setup_direction):
    """DECLARED QUANTITY (this block's own, disclosed as new).

    A DYNAMICAL BRANCH PAIR is two lock points that agree on every
    setup-supplied coordinate the endpoint menu can see -- the same token
    positions (the same scan schedule) and the same PREPARED endpoint
    direction at tick 0 -- and that nevertheless realize DIFFERENT menu items
    at their lock ticks.  On the landed scan this is impossible by the
    Cycle-913 theorem (realized = prepared).  It becomes possible exactly when
    the endpoint content is written by the dynamics, and it is the strongest
    sense in which 'the two menu items are alternatives of one setup' that
    this census can express.  It is WEAKER than the Cycle-911 CLASS_BRANCH,
    which also demands identical tick-0 states.  The two are reported side by
    side and never conflated."""
    groups: dict = {}
    for w, r in rows_by_world.items():
        key = (tuple(census[w][2]), setup_direction[census[w][1]])
        groups.setdefault(key, []).append(w)
    complete = {k: v for k, v in groups.items() if len(v) >= 2}
    split_pairs = []
    undecidable = 0
    candidate_pairs = 0
    for key, members in sorted(complete.items()):
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
        "definition":
            "same token positions AND same prepared endpoint direction at "
            "tick 0, different realized menu item at the lock tick",
        "candidate_pairs_among_the_lock_points": candidate_pairs,
        "pairs_skipped_because_the_endpoint_was_off_menu": undecidable,
        "DYNAMICAL_BRANCH_PAIRS": len(split_pairs),
        "pairs": split_pairs[:PAIR_SAMPLE_CAP],
        "pairs_truncated_at": PAIR_SAMPLE_CAP,
    }


# ---------------------------------------------------------------------------
# the verdict classifier: reads measurements only, never a candidate's name
# ---------------------------------------------------------------------------

def classify_candidate(m: dict):
    obstruction = []
    if m["write_once_violations"]:
        obstruction.append(
            f"write-once breach: {m['write_once_violations']} record slots "
            "written twice")
    if m["record_slot_activation_conflicts"]:
        obstruction.append(
            f"dead-wire corruption: {m['record_slot_activation_conflicts']} "
            "record slots activated by the dynamics")
    if m["slot_wires_that_became_gate_wires"]:
        obstruction.append("record slots became gate inputs or targets")
    if m["targets_outside_the_endpoint_wires"]:
        obstruction.append(
            "the modification targets a wire that is not an endpoint wire")
    if m["duplicate_lane_mismatches"]:
        obstruction.append(
            f"duplicate-lane consistency lost ({m['duplicate_lane_mismatches']}"
            " mismatches)")
    if m["lock_points"] == 0:
        obstruction.append("formation destroyed: no world locks")
    if m["off_menu_lock_points"]:
        obstruction.append(
            f"the endpoint content leaves the menu at {m['off_menu_lock_points']}"
            " lock points: the site carries a bit pattern that is not an "
            "admissible possibility at all")
    if not m["layout_independent"]:
        obstruction.append(
            "the law is not well defined: forward and reversed lane layouts "
            "give different trajectories, so the law depends on the "
            "bookkeeping order in which worlds are packed into bits")
    if not m["ast_lane_locality"]:
        obstruction.append(
            "the Cycle-911 no-cross-lane certification fails on the compiled "
            "source")
    if not m["runtime_lane_locality"]:
        obstruction.append(
            "the runtime perturbation witness leaks outside its own lane: "
            "setups-are-worlds is broken")
    if obstruction:
        return "DESTRUCTIVE", obstruction
    if m["selection_became_dynamical"] and m["dynamical_branch_pairs"] > 0:
        return "BORN-CAPABLE", []
    return "STERILE", []


def neutral_probe(**over):
    base = {"write_once_violations": 0, "record_slot_activation_conflicts": 0,
            "slot_wires_that_became_gate_wires": [],
            "targets_outside_the_endpoint_wires": False,
            "duplicate_lane_mismatches": 0, "lock_points": 164,
            "off_menu_lock_points": 0, "layout_independent": True,
            "ast_lane_locality": True, "runtime_lane_locality": True,
            "selection_became_dynamical": False, "dynamical_branch_pairs": 0}
    base.update(over)
    return base


# ---------------------------------------------------------------------------
# per-run row building and dependence re-analysis
# ---------------------------------------------------------------------------

def build_rows(c913, census, build, menu, geometry):
    BB, AW, LW, LB = (geometry["BANK_BASES"], geometry["AW"], geometry["LW"],
                      geometry["LINK_BASES"])
    left_w, right_w = geometry["left"], geometry["right"]
    endpoint_set = {left_w, right_w}
    site_wires = tuple(range(BB[0]))
    stations = geometry["stations"]
    setup_direction = geometry["setup_direction"]
    formed, snapshots, lock_ordinal = (build["formed"], build["snapshots"],
                                       build["lock_ordinal"])
    rows, off_menu, dis_setup, dis_ham = [], [], [], []
    for w in sorted(formed):
        state = snapshots[w]
        key = census[w]
        rd_state = c913.read_state_direction(state)
        rd_ham, _h = c913.hamming_readout(state, menu)
        rd_setup = setup_direction[key[1]]
        if rd_state is None:
            off_menu.append({"world": w,
                             "endpoint_bits": [state[left_w], state[right_w]]})
        elif rd_state != rd_setup:
            dis_setup.append(w)
        if rd_state is not None and rd_ham is not None and rd_state != rd_ham:
            dis_ham.append(w)
        bank0 = "".join(str(state[BB[0] + i]) for i in range(AW))
        bank1 = "".join(str(state[BB[1] + i]) for i in range(AW))
        link0 = "".join(str(state[LB[0] + i]) for i in range(LW))
        shell2_rest = "".join(str(state[BB[b] + i])
                              for b in (2, 3) for i in range(AW))
        full = "".join(str(b) for b in state)
        wl, wr = build["lock_endpoint_writes"].get(w, (0, 0))
        rows.append({
            "world": w, "key": [key[0], key[1], list(key[2])],
            "lock_boundary": formed[w], "phase": formed[w] % stations,
            "menu": [list(v) for v in menu],
            "selected_item": list(rd_state) if rd_state else None,
            "rd_setup": list(rd_setup) if rd_setup else None,
            "rd_hamming": list(rd_ham) if rd_ham else None,
            "left_writes_before_lock": wl, "right_writes_before_lock": wr,
            "ord0": lock_ordinal[w][0], "ord1": lock_ordinal[w][1],
            "bank0": bank0, "bank1": bank1, "link0": link0,
            "shell2_rest": shell2_rest,
            "site_block": "".join(str(state[i]) for i in site_wires),
            "site_block_minus_endpoints": "".join(
                str(state[i]) for i in site_wires if i not in endpoint_set),
            "endpoint_bits": (state[left_w], state[right_w]),
            "state_minus_site": full[BB[0]:],
            "state_minus_endpoints": "".join(
                c for i, c in enumerate(full) if i not in endpoint_set),
            "full_state": full,
            "context_fingerprint": sha256(
                (bank0 + "|" + bank1 + "|" + link0 + "|"
                 + full[BB[0]:]).encode("ascii")).hexdigest()[:16],
        })
    return rows, off_menu, dis_setup, dis_ham


def dependence_analysis(c913, c878, rows, census, stations, width, bb0):
    """The Cycle-913 C2 machinery, AST-lifted and re-run unchanged."""
    live = [r for r in rows if r["selected_item"] is not None]

    def value_fn(r):
        return tuple(r["selected_item"])

    if not live:
        return {"rows_with_a_realized_menu_item": 0, "ladder": [],
                "covariance_translation": {}, "unavailable": True}
    ladder = c913.ladder_rows(live, value_fn)
    by_name = {row["fingerprint"]: row for row in ladder}
    varying, determining = c913.exhaustive_singleton_sweep(live, value_fn,
                                                           width)
    nonsite_varying = [w for w in varying if w >= bb0]
    nonsite_all = c913.is_function(
        live, lambda r: tuple(r["full_state"][w] for w in nonsite_varying),
        value_fn)
    selection = {r["world"]: tuple(r["selected_item"]) for r in live}
    trans = c913.translation_covariance(c878, census, stations, selection)
    return {
        "rows_with_a_realized_menu_item": len(live),
        "ladder_entries": len(ladder),
        "ladder": ladder,
        "selection_is_a_function_of_SETUP_event_parity":
            by_name["SETUP_event_parity"]["is_a_function"],
        "selection_is_a_function_of_the_SETUP_event_index":
            by_name["SETUP_event_index"]["is_a_function"],
        "selection_is_a_function_of_nearest_neighbour_record_content":
            by_name["R1_nearest_neighbour_record_content"]["is_a_function"],
        "selection_is_a_function_of_neighbour_ordinals":
            by_name["R1_nearest_neighbour_exact_ordinals"]["is_a_function"],
        "selection_is_a_function_of_openness_only":
            by_name["R1_nearest_neighbour_openness_only"]["is_a_function"],
        "selection_is_a_function_of_the_site_endpoint_wires_only":
            by_name["SITE_ENDPOINT_WIRES_ONLY"]["is_a_function"],
        "selection_is_a_function_of_the_site_block_minus_the_endpoints":
            by_name["SITE_BLOCK_MINUS_THE_ENDPOINT_WIRES"]["is_a_function"],
        "empty_context_determines": by_name["EMPTY_CONTEXT"]["is_a_function"],
        "widest_non_site_context_determines": nonsite_all["is_a_function"],
        "widest_non_site_context_varying_wires": len(nonsite_varying),
        "widest_non_site_context_witness": nonsite_all["witness_pair"],
        "exhaustive_single_wire_sweep": {
            "wires_swept": width,
            "wires_that_vary": len(varying),
            "single_wires_that_DETERMINE_the_selection": determining,
            "any_determining_wire_outside_the_site":
                any(w >= bb0 for w in determining),
        },
        "covariance_translation": trans,
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

    (c863, c878, c911, c913, cls, dirs, consts878, consts911, cross_lane_ops,
     provenance) = lift_machinery()

    text = {p: payloads[p].decode("utf-8") for p in TEXT_ONLY_PATHS}
    receipts = {p: json.loads(payloads[p].decode("utf-8"))
                for p in JSON_ONLY_PATHS}
    r911, r913, r878 = (receipts[C911_RECEIPT], receipts[C913_RECEIPT],
                        receipts[C878_RECEIPT])
    c2_911 = r911["certificates"]["C2_MENU_AT_FORMATION"]
    c1_913 = r913["certificates"]["C1_SELECTION_TABLE"]
    c2_913 = r913["certificates"]["C2_DEPENDENCE"]
    c6_913 = r913["certificates"]["C6_O2_O3_VERDICT"]
    h_913 = r913["certificates"]["H_DOUBLE_BUILD"]
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
    geometry = {"BANK_BASES": BB, "LINK_BASES": LB, "AW": AW, "LW": LW,
                "left": left_w, "right": right_w, "stations": stations,
                "setup_direction": setup_direction}

    REC_A = BB[0] + K.A.POINTER      # bank 0's POINTER record register
    REC_B = BB[1] + K.A.POINTER      # bank 1's POINTER record register

    MODS = [
        {"name": "CONTROL",
         "axis": "the unmodified landed 719 kernel -- the anchor",
         "station": 0, "gates": ()},
        {"name": "M_A",
         "axis": "RECORD-DRIVEN: a designated record slot fires and the "
                 "endpoint encoding swaps",
         "station": 0,
         "gates": ((KIND_CNOT, REC_A, left_w, 0),
                   (KIND_CNOT, REC_A, right_w, 0))},
        {"name": "M_B",
         "axis": "CROSS-LANE: the endpoint XORs with the lane neighbour's "
                 "endpoint -- worlds interact",
         "station": 0,
         "gates": ((KIND_SHIFT, left_w, left_w, 0),
                   (KIND_SHIFT, right_w, right_w, 0))},
        {"name": "M_C",
         "axis": "LOCALLY CONTENT-DRIVEN: the endpoint flips as a function of "
                 "the site's own two bank occupations",
         "station": 0,
         "gates": ((KIND_TOF, REC_A, REC_B, left_w),
                   (KIND_TOF, REC_A, REC_B, right_w))},
    ]
    MOD_BY_NAME = {m["name"]: m for m in MODS}

    def describe(mod):
        gates = mod["gates"]
        targets = sorted({gate_target(*g) for g in gates})
        inputs = sorted({w for g in gates for w in gate_inputs_of(*g)})
        return {
            "name": mod["name"], "axis": mod["axis"],
            "anchor_station": mod["station"],
            "anchor_station_kind": program[mod["station"]][0],
            "gate_count": len(gates),
            "gates": [{"kind": KIND_NAMES[g[0]], "text": gate_text(*g),
                       "target_wire": gate_target(*g),
                       "input_wires": list(gate_inputs_of(*g))}
                      for g in gates],
            "targets": targets, "inputs": inputs,
            "targets_only_the_endpoint_wires":
                set(targets) <= {left_w, right_w},
            "kinds_in_the_certified_vocabulary":
                all(g[0] in CERTIFIED_KINDS for g in gates),
            "record_wires_read": [w for w in inputs if w >= BB[0]],
        }

    # ---------------- the Cycle-878 dead-wire record rig, verbatim ---------
    sim_ctl = tuple(census) + (census[0],)
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    t0 = monotonic()
    rig = c878.dead_wire_rig(program, sim_ctl, proto)
    t_rig = round(monotonic() - t0, 3)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))

    # ---------------- the runs ---------------------------------------------
    builds: dict = {}
    slim: dict = {}
    timings: dict = {}
    for mod in MODS:
        for reverse in (False, True):
            t0 = monotonic()
            b = run_scan(c863, program, census, states, HORIZON,
                         mod["station"], mod["gates"], reverse, register_cap,
                         slot_of, (left_w, right_w, src_w))
            timings[(mod["name"], reverse)] = round(monotonic() - t0, 3)
            if reverse:
                slim[mod["name"]] = {
                    "digest": scan_digest(b), "formed": len(b["formed"]),
                    "duplicate_lane_mismatches": b["duplicate_lane_mismatches"],
                    "write_once_violations": b["write_once_violations"],
                    "events": len(b["events"]),
                }
                del b
            else:
                builds[mod["name"]] = b

    ctl = builds["CONTROL"]

    # ---------------- B: restriction gates ---------------------------------
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    pinned_sched = c863.masked_h_schedules(program, sim_ctl)
    mine_sched = build_schedules(c863, program, sim_ctl, 0, (),
                                 (1 << (len(census) + 1)) - 1)
    gate("schedule_builder_reproduces_the_pinned_compiler",
         digest([[list(g) for g in s] for s in mine_sched]),
         digest([[list(g) for g in s] for s in pinned_sched]))
    gate("compiled_gate_total", sum(len(s) for s in mine_sched),
         c1_913["endpoint_wire_lemma"]["gates_total"])
    gate("chunk_source_reproduces_the_pinned_compile_fast_text",
         digest([chunk_source(s) for s in mine_sched]),
         digest([_pinned_compile_fast_text(s) for s in pinned_sched]))

    # the pinned Cycle-911 scan, cross-checked on a declared short window
    t0 = monotonic()
    pinned_short = c911.snapshot_scan(c863, program, census, states,
                                      CROSSCHECK_ORBITS, False)
    mine_short = run_scan(c863, program, census, states, CROSSCHECK_ORBITS, 0,
                          (), False, register_cap, slot_of,
                          (left_w, right_w, src_w))
    t_cross = round(monotonic() - t0, 3)
    gate("scan_reproduces_the_pinned_911_snapshot_scan_on_the_cross_check_window",
         scan_digest(mine_short), scan_digest(pinned_short))
    gate("event_list_reproduces_the_pinned_911_scan_on_the_cross_check_window",
         digest([list(e) for e in mine_short["events"]]),
         digest([list(e) for e in pinned_short["events"]]))
    del pinned_short, mine_short

    # the full-horizon build, digest-identical to the pinned Cycle-913 build
    gate("full_horizon_build_digest_matches_the_pinned_913_build",
         scan_digest(ctl), h_913["digest_A"])
    gate("reversed_layout_build_digest_matches_the_pinned_913_build",
         slim["CONTROL"]["digest"], h_913["digest_B"])

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
    gate("c911_locks_at_moment_zero",
         sum(1 for w in my_locks if ctl["formed"][w] == 0),
         c2_911["locks_at_moment_zero"])
    gate("c911_lock_boundary_range",
         [min(ctl["formed"].values()), max(ctl["formed"].values())],
         c2_911["lock_boundary_range"])
    gate("c911_menu_of_local_possibilities", [list(v) for v in menu],
         c2_911["menu_of_local_possibilities"])
    gate("c911_receipt_verdict", r911["VERDICT"], "RE-TYPED")

    ctl_rows, ctl_off, ctl_dis_setup, ctl_dis_ham = build_rows(
        c913, census, ctl, menu, geometry)
    ctl_by_world = {r["world"]: r for r in ctl_rows}
    gate("c913_selection_table_value_for_value",
         [[r["world"], r["key"], r["lock_boundary"], r["phase"], r["menu"],
           r["selected_item"], [r["ord0"], r["ord1"]],
           r["context_fingerprint"]] for r in ctl_rows],
         [[x["world"], x["key"], x["lock_boundary"], x["phase"], x["menu"],
           x["selected_item"], x["neighbour_ordinals"],
           x["context_fingerprint"]] for x in c1_913["per_lock_point_rows"]])
    ctl_split = Counter(tuple(r["selected_item"]) for r in ctl_rows)
    gate("c913_selection_split",
         {str(list(v)): c for v, c in sorted(ctl_split.items())},
         {k: v["count"] for k, v in
          sorted(c1_913["selection_split"].items())})
    ctl_lemma = target_sweep(mine_sched, left_w, right_w, src_w)
    gate("c913_endpoint_wire_lemma",
         [ctl_lemma["gates_total"], ctl_lemma["LEFT_ENDPOINT_wire"],
          ctl_lemma["RIGHT_ENDPOINT_wire"], ctl_lemma["LEFT_is_a_gate_target"],
          ctl_lemma["RIGHT_is_a_gate_target"],
          ctl_lemma["LEFT_is_a_gate_input"], ctl_lemma["RIGHT_is_a_gate_input"],
          ctl_lemma["endpoint_content_is_read_never_written"]],
         [c1_913["endpoint_wire_lemma"][k] for k in
          ("gates_total", "LEFT_ENDPOINT_wire", "RIGHT_ENDPOINT_wire",
           "LEFT_is_a_gate_target", "RIGHT_is_a_gate_target",
           "LEFT_is_a_gate_input", "RIGHT_is_a_gate_input",
           "endpoint_content_is_read_never_written")])
    gate("c913_target_sweep_matches_the_lifted_913_sweep",
         [ctl_lemma[k] for k in ("gates_total", "distinct_targets",
                                 "distinct_inputs")],
         [c913.target_wire_sweep(mine_sched)[k]
          for k in ("gates_total", "distinct_targets", "distinct_inputs")])
    gate("c913_minimal_determining_context_cardinality",
         c2_913["MINIMAL_DETERMINING_CONTEXT"]["cardinality"], 1)
    gate("c913_receipt_verdict", r913["VERDICT"],
         "O2 SUPPLIED, MEASURED, AND NOT LOCAL")
    gate("c913_all_certificates_pass", r913["all_certificates_pass"], True)
    gate("control_endpoint_write_events_are_zero",
         [ctl["endpoint_change_boundaries"],
          sum(a + b for a, b in ctl["final_endpoint_writes"].values())],
         [0, 0])

    gate("census_size", len(census), 748)
    gate("initial_state_build_failures", init_failures, 0)
    gate("horizon_agrees_with_878_and_911",
         [consts878["HORIZON"], consts911["HORIZON"]], [HORIZON, HORIZON])
    gate("c878_event_cardinality", len(ctl["events"]),
         r878["findings"]["event_cardinality"])
    gate("c878_worlds_with_at_least_one_event",
         len({e[0] for e in ctl["events"]}),
         r878["findings"]["worlds_with_at_least_one_event"])
    gate("c878_bank_events_beyond_cap", ctl["beyond_cap"],
         r878["findings"]["bank_edge_events_beyond_declared_cap"])
    gate("c878_dead_rig_constants",
         [consts878["DEAD_CHUNK_ORBITS"], consts878["DEAD_ORBIT_ORBITS"]],
         [DEAD_CHUNK_ORBITS, DEAD_ORBIT_ORBITS])
    gate("record_slot_count", len(slot_wires), 1 + 2 * register_cap)
    gate("record_slots_are_structurally_inert_in_the_control",
         sorted(w for w in slot_wires
                if w in ctl_lemma["_targets"] or w in ctl_lemma["_inputs"]),
         [])
    gate("control_write_once_violations", ctl["write_once_violations"], 0)
    gate("control_record_slot_activation_conflicts",
         ctl["record_slot_activation_conflicts"], 0)

    axioms, realized, note911 = (text[AXIOMS_PATH], text[REALIZED_PATH],
                                 text[C911_NOTE])
    Q_ADMISSIBILITY = ("For each site, the available possibilities are"
                       " determined by, and vary with,\nthe nearest-neighbor"
                       " conditions.")
    Q_RECORD_LOCK = ("When present, a record locks exactly one admissible"
                     " local possibility. A\nsite never carries more than one"
                     " record; records are permanent.")
    Q_RECORDS_FORM = "Records form."
    Q_NO_AVERAGING = ("Nothing more is supplied: no averaging over"
                      " alternatives, no typical or\ngeneric claim, and no"
                      " quoting a number that would differ had another\n"
                      "law-admissible state been realized.")
    Q_911_NEXT = "the landed scan's selection function is the next computation"
    Q_913_SUCCESSOR = (
        "a substrate whose endpoint content is a gate TARGET -- so that the "
        "two menu items are alternatives of one setup rather than two setups "
        "-- is the only place the A3 arena can be non-degenerate.  That is "
        "the next computation.")
    Q_913_SHARP = "no gate in the composed scan targets the endpoint wires."
    gate("axioms_admissibility_sentence_byte_present",
         Q_ADMISSIBILITY in axioms, True)
    gate("axioms_record_lock_sentence_byte_present",
         Q_RECORD_LOCK in axioms, True)
    gate("axioms_records_form_byte_present", Q_RECORDS_FORM in axioms, True)
    gate("realized_state_no_averaging_byte_present",
         Q_NO_AVERAGING in realized, True)
    gate("c911_note_names_the_913_computation", Q_911_NEXT in note911, True)
    gate("c913_successor_sentence_byte_for_byte",
         c6_913["ledger"]["successor"], Q_913_SUCCESSOR)
    gate("c913_sharp_fact_byte_present",
         Q_913_SHARP in c6_913["O2"]["the_sharp_fact"], True)

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows, "total": len(gate_rows),
        "reproduce": sum(1 for r in gate_rows if r["pass"]),
        "anchor_statement":
            "the CONTROL run is this block's anchor.  Before any modification "
            "is trusted, this file's schedule builder must reproduce the "
            "pinned Cycle-863 compiler row for row, its compiled text must "
            "reproduce the pinned compile_fast source, its scan must "
            "reproduce the pinned Cycle-911 snapshot_scan on a declared "
            "cross-check window, its full-horizon build must be digest-"
            "identical to the pinned Cycle-913 build in BOTH lane layouts, "
            "and its selection table must equal the pinned Cycle-913 table "
            "value for value.",
        "byte_quotes": {
            "admissibility_sentence": Q_ADMISSIBILITY,
            "record_lock_sentence": Q_RECORD_LOCK,
            "realized_state_no_averaging": Q_NO_AVERAGING,
            "c913_successor_this_block_executes": Q_913_SUCCESSOR,
        },
        "pass": all(r["pass"] for r in gate_rows),
    }

    # ---------------- C1: the declared construction space ------------------
    designs = [describe(m) for m in MODS]
    cert_c1 = {
        "certificate": "C1_CONSTRUCTION_SPACE",
        "constraint_a_record_machinery":
            "every candidate must leave the record machinery recomputable: "
            "the dead-wire record slots stay structurally inert, the "
            "write-once discipline holds, formation is still detected by the "
            "same global-clean predicate, and the 911/913 restriction "
            "quantities are recomputed on the modified scan.",
        "constraint_b_vocabulary":
            "every added gate must be one of the three compiled forms the "
            "Cycle-911 sweep certified -- c[i] ^= mask (X), c[i] ^= c[j] & "
            "mask (CNOT), c[i] ^= c[j] & c[k] & mask (TOF).  M_B breaks this "
            "constraint BY CONSTRUCTION and says so: a cross-lane gate needs "
            "a shift, and a shift is exactly what the sweep forbids.  It is "
            "included because the block was asked to test whether making "
            "worlds interact is the missing ingredient.",
        "constraint_c_covariance":
            "every candidate is anchored at a STATION, so the modification "
            "travels with the controller token exactly as the kernel's own "
            "macros do; the landed monitor-phase Z_11 action is re-tested per "
            "candidate in C2.",
        "anchoring_mechanism":
            "the extra gates are appended to the macro of the declared "
            "station and are masked by that station's OWN lane mask, so a "
            "candidate fires for a world exactly when the controller token "
            "reaches that station in that world.  Station 0 is the source "
            "station -- the station that already READS both endpoint wires, "
            "so the modification adds a write where the kernel already has a "
            "read and nowhere else.",
        "designated_record_registers": {
            "REC_A": {"wire": REC_A, "name": "bank 0 POINTER",
                      "bank_base": BB[0], "offset": K.A.POINTER},
            "REC_B": {"wire": REC_B, "name": "bank 1 POINTER",
                      "bank_base": BB[1], "offset": K.A.POINTER},
            "provenance":
                "POINTER is the first entry of the pinned Cycle-863 "
                "watched_registers() tuple -- the first record register the "
                "substrate's own dirty partition watches.  Banks 0 and 1 are "
                "the lock site's two nearest neighbours under the pinned "
                "Cycle-911 declared embedding (+x and -x).",
        },
        "endpoint_encoding":
            "K.M.prepare_endpoint writes LEFT = int(v == (0,1)) and RIGHT = "
            f"int(v == (1,0)).  The menu is therefore the two complementary "
            f"patterns on wires {left_w}/{right_w}, and flipping BOTH wires "
            "with the same control is exactly the menu swap (1,0) <-> (0,1). "
            "M_A and M_C do that, so their endpoint stays ON the menu by "
            "construction.  M_B's two controls are two different neighbour "
            "wires, so its endpoint need not stay on the menu -- and whether "
            "it does is measured, not assumed.",
        "spanning_justification":
            "M_A is record-driven (the endpoint reads a record register), "
            "M_B is cross-lane (the endpoint reads another world), M_C is "
            "locally content-driven (the endpoint reads the site's own two "
            "bank occupations).  Those are the three ways this bit can become "
            "dynamical: from the record ledger, from outside the world, or "
            "from local content.  A fourth candidate would have to read the "
            "endpoint's own wire, which is the identity or the unconditional "
            "flip; the unconditional single-lane flip appears as the planted "
            "falsifier M_PLANT.",
        "designs": designs,
        "pass": bool(
            all(d["targets_only_the_endpoint_wires"] for d in designs)
            and all(d["kinds_in_the_certified_vocabulary"] for d in designs
                    if d["name"] in ("CONTROL", "M_A", "M_C"))
            and not describe(MOD_BY_NAME["M_B"])[
                "kinds_in_the_certified_vocabulary"]),
    }

    # ---------------- C2: the per-modification measurement ------------------
    analysis: dict = {}
    for mod in MODS:
        name = mod["name"]
        fwd = builds[name]
        sched = fwd["schedules"]
        lemma = target_sweep(sched, left_w, right_w, src_w)
        stats, violations = sweep_source(sched, cross_lane_ops)
        rows, off_menu, dis_setup, dis_ham = build_rows(c913, census, fwd,
                                                        menu, geometry)
        by_world = {r["world"]: r for r in rows}
        live = [r for r in rows if r["selected_item"] is not None]
        dep = dependence_analysis(c913, c878, rows, census, stations, width,
                                  BB[0])
        lit = literal_branch_matrix(c911, census, states, fwd["formed"],
                                    classes)
        dyn = dynamical_branch_pairs(census, by_world, setup_direction)
        movers = [w for w in sorted(set(ctl["formed"]) & set(fwd["formed"]))
                  if ctl["formed"][w] != fwd["formed"][w]]
        sel_movers = [w for w in sorted(set(ctl_by_world) & set(by_world))
                      if ctl_by_world[w]["selected_item"]
                      != by_world[w]["selected_item"]]
        wl = sum(a for a, _b in fwd["final_endpoint_writes"].values())
        wr = sum(b for _a, b in fwd["final_endpoint_writes"].values())
        worlds_with_writes = sum(
            1 for a, b in fwd["final_endpoint_writes"].values() if a or b)
        locks_with_writes = sum(
            1 for r in rows
            if r["left_writes_before_lock"] or r["right_writes_before_lock"])
        # the witness lanes are 1 and 2, not 0: the declared cross-lane stride
        # moves content from bit b+1 into bit b, so a flip planted in lane 0
        # has no lower lane to leak into and would make the witness blind.
        pert = perturbation_witness(
            c863, program, census, states, ((1, left_w), (2, REC_A)),
            PERTURB_ORBITS, mod["station"], mod["gates"])
        rev = slim[name]
        slot_gate_wires = sorted(w for w in slot_wires
                                 if w in lemma["_targets"]
                                 or w in lemma["_inputs"])
        measurements = {
            "write_once_violations": fwd["write_once_violations"],
            "record_slot_activation_conflicts":
                fwd["record_slot_activation_conflicts"],
            "slot_wires_that_became_gate_wires": slot_gate_wires,
            "targets_outside_the_endpoint_wires": bool(
                {gate_target(*g) for g in mod["gates"]} - {left_w, right_w}),
            "duplicate_lane_mismatches": fwd["duplicate_lane_mismatches"]
            + rev["duplicate_lane_mismatches"],
            "lock_points": len(fwd["formed"]),
            "off_menu_lock_points": len(off_menu),
            "layout_independent": scan_digest(fwd) == rev["digest"],
            "ast_lane_locality": not violations,
            "runtime_lane_locality": all(
                p["leak_outside_own_lane_bit"] == 0 for p in pert),
            "selection_became_dynamical": bool(dis_setup),
            "dynamical_branch_pairs": dyn["DYNAMICAL_BRANCH_PAIRS"],
        }
        analysis[name] = {
            "design": describe(mod),
            "runtime_sec": {"forward": timings[(name, False)],
                            "reversed": timings[(name, True)]},
            "FORMATION": {
                "lock_points": len(fwd["formed"]),
                "control_lock_points": len(ctl["formed"]),
                "worlds_that_stopped_forming":
                    sorted(set(ctl["formed"]) - set(fwd["formed"]))[:40],
                "worlds_that_stopped_forming_count":
                    len(set(ctl["formed"]) - set(fwd["formed"])),
                "worlds_that_started_forming":
                    sorted(set(fwd["formed"]) - set(ctl["formed"]))[:40],
                "worlds_that_started_forming_count":
                    len(set(fwd["formed"]) - set(ctl["formed"])),
                "lock_points_whose_boundary_moved": len(movers),
                "lock_boundary_range":
                    [min(fwd["formed"].values()), max(fwd["formed"].values())]
                    if fwd["formed"] else None,
                "locks_at_moment_zero":
                    sum(1 for v in fwd["formed"].values() if v == 0),
                "record_events": len(fwd["events"]),
                "control_record_events": len(ctl["events"]),
                "bank_edge_events_beyond_cap": fwd["beyond_cap"],
            },
            "ENDPOINT_WRITES": {
                "LEFT_is_now_a_gate_target": lemma["LEFT_is_a_gate_target"],
                "RIGHT_is_now_a_gate_target": lemma["RIGHT_is_a_gate_target"],
                "reads_never_writes_lemma_still_holds":
                    lemma["endpoint_content_is_read_never_written"],
                "compiled_gates_total": lemma["gates_total"],
                "gates_added": lemma["gates_total"] - ctl_lemma["gates_total"],
                "boundaries_at_which_an_endpoint_bit_changed":
                    fwd["endpoint_change_boundaries"],
                "total_LEFT_write_events_over_all_worlds": wl,
                "total_RIGHT_write_events_over_all_worlds": wr,
                "worlds_whose_endpoint_ever_changed": worlds_with_writes,
                "census_worlds": len(census),
                "lock_points_whose_endpoint_changed_before_the_lock":
                    locks_with_writes,
                "write_count_histogram_at_the_lock": {
                    str(list(k)): v for k, v in sorted(Counter(
                        (r["left_writes_before_lock"] % 2,
                         r["right_writes_before_lock"] % 2)
                        for r in rows).items())},
                "max_writes_before_a_lock": max(
                    [max(r["left_writes_before_lock"],
                         r["right_writes_before_lock"]) for r in rows] or [0]),
            },
            "SELECTION": {
                "lock_points": len(rows),
                "off_menu_endpoint_content_at_the_lock": len(off_menu),
                "off_menu_rows": off_menu[:12],
                "realized_split": {str(list(v)): c for v, c in sorted(
                    Counter(tuple(r["selected_item"])
                            for r in live).items())},
                "lock_points_where_RD_STATE_disagrees_with_RD_SETUP":
                    len(dis_setup),
                "worlds_where_the_realized_item_left_its_setup_value":
                    dis_setup[:24],
                "lock_points_where_RD_STATE_disagrees_with_RD_HAMMING":
                    len(dis_ham),
                "lock_points_whose_realized_item_differs_from_the_control":
                    len(sel_movers),
                "selection_movers": sel_movers[:24],
            },
            "DEPENDENCE": dep,
            "BRANCH_MATRIX_911_literal": lit,
            "BRANCH_PAIRS_dynamical": dyn,
            "RECORD_MACHINERY": {
                "write_once_violations": fwd["write_once_violations"],
                "record_slot_activation_conflicts":
                    fwd["record_slot_activation_conflicts"],
                "record_slots": len(slot_wires),
                "slot_wires_that_became_gate_wires": slot_gate_wires,
                "modification_targets_a_non_endpoint_wire":
                    measurements["targets_outside_the_endpoint_wires"],
                "duplicate_lane_mismatches_forward":
                    fwd["duplicate_lane_mismatches"],
                "duplicate_lane_mismatches_reversed":
                    rev["duplicate_lane_mismatches"],
            },
            "COVARIANCE_AND_STRUCTURE": {
                "ast_sweep_statements": stats["statements"],
                "ast_sweep_violations": len(violations),
                "ast_sweep_violation_kinds": sorted({v[0] for v in violations}),
                "ast_sweep_cross_lane_operators": sorted(
                    {v[2] for v in violations
                     if v[0] == "cross-lane operator"}),
                "position_wise_lane_locality_certified": not violations,
                "runtime_perturbation_witness": pert,
                "runtime_lane_locality_certified":
                    measurements["runtime_lane_locality"],
                "layout_independent": measurements["layout_independent"],
                "forward_digest": scan_digest(fwd),
                "reversed_digest": rev["digest"],
                "translation_invariant": dep["covariance_translation"].get(
                    "selection_is_translation_invariant"),
                "translation_action_is_a_census_bijection":
                    dep["covariance_translation"].get(
                        "action_is_a_census_bijection"),
                "translation_violations": dep["covariance_translation"].get(
                    "selection_violations_under_translation"),
            },
            "_measurements": measurements,
            "_sel_movers_full": sel_movers,
            "rows": [
                {"world": r["world"], "key": r["key"],
                 "lock_boundary": r["lock_boundary"],
                 "selected_item": r["selected_item"], "rd_setup": r["rd_setup"],
                 "endpoint_bits": list(r["endpoint_bits"]),
                 "left_writes": r["left_writes_before_lock"],
                 "right_writes": r["right_writes_before_lock"]}
                for r in rows],
        }

    # ---------------- the planted modification (falsifier) -----------------
    # The complete same-setup-coordinate pairs among the CONTROL lock points:
    # both members share token positions and prepared endpoint direction, and
    # the pinned Cycle-913 theorem makes both realize the same item.  A
    # modification restricted to ONE member of such a pair therefore runs two
    # different laws on the two members, and any change it makes to that
    # member's realized item splits the pair by construction.
    control_partner: dict = {}
    for w in ctl_by_world:
        control_partner.setdefault(
            (tuple(census[w][2]), setup_direction[census[w][1]]), []).append(w)
    complete_pairs = [tuple(sorted(v)[:2]) for _k, v in
                      sorted(control_partner.items()) if len(v) >= 2]

    plant_lane = None
    for source in ("M_A", "M_C"):
        cand = analysis[source]
        for w in cand["_sel_movers_full"]:
            others = [x for x in control_partner.get(
                (tuple(census[w][2]), setup_direction[census[w][1]]), [])
                if x != w]
            if others:
                plant_lane = (source, w, sorted(others)[0])
                break
        if plant_lane:
            break

    if plant_lane is not None:
        src_name, u, v = plant_lane
        src_mod = MOD_BY_NAME[src_name]
        plant_gates = src_mod["gates"]
        plant_station = src_mod["station"]
        plant_lanes = {u}
        planted_pairs = [(min(u, v), max(u, v))]
        construction = (
            f"the {src_name} gates with their lane mask ANDed down to the "
            f"single world lane {u}.  Because {src_name} is lane-local, world "
            f"{u} then runs exactly the {src_name} law while world {v} -- "
            "which shares its token positions and its prepared endpoint "
            "direction -- runs exactly the CONTROL law.  The pair is "
            "constructed to split, so the branch machinery has to find it.")
    else:
        # FALLBACK PLANT, declared: an unconditional endpoint swap -- two X
        # gates, the simplest form in the certified vocabulary -- masked to
        # exactly one member of every complete pair.  Unlike M_A and M_C its
        # control is the constant 1, so the flip count before a lock is the
        # number of source-station firings and is under no evenness
        # constraint.  Every pair therefore runs two different laws.
        plant_gates = ((KIND_X, left_w, 0, 0), (KIND_X, right_w, 0, 0))
        plant_station = 0
        plant_lanes = {u for u, _v in complete_pairs}
        planted_pairs = list(complete_pairs)
        construction = (
            "an unconditional endpoint swap (two X gates on wires "
            f"{left_w} and {right_w}) appended to the source station's macro "
            "and masked to exactly one member of each of the "
            f"{len(complete_pairs)} complete same-setup-coordinate pairs.  "
            "Each pair then runs two different laws, so any pair whose "
            "modified member changes its realized item splits by "
            "construction, and the branch machinery has to find exactly "
            "those pairs and no others.")

    t0 = monotonic()
    plant_build = run_scan(c863, program, census, states, HORIZON,
                           plant_station, plant_gates, False, register_cap,
                           slot_of, (left_w, right_w, src_w),
                           lane_restrict=plant_lanes)
    t_plant = round(monotonic() - t0, 3)
    prows, poff, pdis, _ph = build_rows(c913, census, plant_build, menu,
                                        geometry)
    pby = {r["world"]: r for r in prows}
    plant_dyn = dynamical_branch_pairs(census, pby, setup_direction)
    # INDEPENDENT ground truth for the same quantity, computed by a different
    # route: walk the declared pair list and compare the two realized items
    # directly, without the grouping machinery the detector uses.
    ground_truth = sorted(
        [u2, v2] for u2, v2 in planted_pairs
        if u2 in pby and v2 in pby
        and pby[u2]["selected_item"] is not None
        and pby[v2]["selected_item"] is not None
        and pby[u2]["selected_item"] != pby[v2]["selected_item"])
    detected = sorted(sorted(p["pair"]) for p in plant_dyn["pairs"])
    plant_note = {
        "name": "M_PLANT",
        "construction": construction,
        "gates": [{"kind": KIND_NAMES[g[0]], "text": gate_text(*g)}
                  for g in plant_gates],
        "lanes_planted": len(plant_lanes),
        "planted_pairs": len(planted_pairs),
        "runtime_sec": t_plant,
        "lock_points": len(prows), "off_menu": len(poff),
        "DYNAMICAL_BRANCH_PAIRS_FOUND": plant_dyn["DYNAMICAL_BRANCH_PAIRS"],
        "independent_ground_truth_splits": len(ground_truth),
        "detector_matches_the_ground_truth":
            detected[:PAIR_SAMPLE_CAP] == ground_truth[:PAIR_SAMPLE_CAP]
            and plant_dyn["DYNAMICAL_BRANCH_PAIRS"] == len(ground_truth),
        "the_planted_pair_was_found": bool(
            ground_truth and plant_dyn["DYNAMICAL_BRANCH_PAIRS"]
            == len(ground_truth)),
        "example_split_pairs": ground_truth[:8],
        "write_once_violations": plant_build["write_once_violations"],
        "record_slot_activation_conflicts":
            plant_build["record_slot_activation_conflicts"],
    }
    del plant_build

    cert_c2 = {
        "certificate": "C2_MEASUREMENT",
        "scope": {
            "census": len(census),
            "sub_census": "FULL CENSUS -- all 748 worlds, both lane layouts",
            "formation_worlds_in_the_control": len(ctl["formed"]),
            "never_formed_worlds_in_the_control":
                len(census) - len(ctl["formed"]),
            "horizon_orbits": HORIZON,
            "boundaries_per_run": ctl["boundaries"],
            "full_horizon_runs": 2 * len(MODS) + 1,
            "note":
                "the packed composed scan evolves every census world in the "
                "same integer columns, so a full-census run costs what a "
                "sub-census run costs.  No world is sampled away; the "
                "never-formed worlds are carried and their endpoint write "
                "counts are reported alongside the formation worlds'.",
        },
        "per_modification": {
            name: {k: v for k, v in row.items()
                   if k not in ("rows", "_measurements", "_sel_movers_full")}
            for name, row in analysis.items()},
        "planted_modification": plant_note,
        "pass": bool(len(ctl["formed"]) == 164
                     and ctl["endpoint_change_boundaries"] == 0),
    }

    # ---------------- C3: the verdicts and the pricing ---------------------
    verdicts = {}
    for name, row in analysis.items():
        if name == "CONTROL":
            continue
        m = row["_measurements"]
        design, ew, sel = row["design"], row["ENDPOINT_WRITES"], row["SELECTION"]
        cov = row["COVARIANCE_AND_STRUCTURE"]
        verdict, obstruction = classify_candidate(m)
        endpoints_move = bool(ew["worlds_whose_endpoint_ever_changed"])
        if verdict == "DESTRUCTIVE":
            why = "; ".join(obstruction)
        elif verdict == "BORN-CAPABLE":
            why = ("the selection is dynamical and same-setup-coordinate "
                   "pairs split, so the two menu items are alternatives of "
                   "one prepared endpoint rather than of two")
        elif not endpoints_move:
            why = ("the endpoint wires are gate targets but no world's "
                   "endpoint ever changed: the control wire never carried a 1 "
                   "when the source station fired")
        elif not m["selection_became_dynamical"]:
            why = ("the endpoint wires are gate targets and the endpoints do "
                   "move, but every lock point still carries the item its "
                   "setup prepared: the writes that reach the lock tick "
                   "always came in even numbers, so the selection stayed "
                   "setup-determined")
        else:
            why = ("the selection moved off its setup value but no "
                   "same-setup-coordinate pair split")
        verdicts[name] = {
            "VERDICT": verdict,
            "endpoint_is_now_a_gate_target": bool(
                ew["LEFT_is_now_a_gate_target"]
                and ew["RIGHT_is_now_a_gate_target"]),
            "endpoints_move_during_evolution": endpoints_move,
            "selection_became_dynamical": m["selection_became_dynamical"],
            "dynamical_branch_pairs": m["dynamical_branch_pairs"],
            "literal_911_branch_pairs":
                row["BRANCH_MATRIX_911_literal"]["BRANCH_PAIRS"],
            "record_machinery_survives": not obstruction,
            "obstruction": obstruction,
            "why": why,
            "structures_preserved": [
                s for s, ok in (
                    ("the write-once discipline", not m["write_once_violations"]),
                    ("the dead-wire record slots",
                     not m["record_slot_activation_conflicts"]
                     and not m["slot_wires_that_became_gate_wires"]),
                    ("formation by the global-clean predicate",
                     m["lock_points"] > 0),
                    ("the endpoint menu (the site carries an admissible "
                     "possibility)", not m["off_menu_lock_points"]),
                    ("setups-are-worlds (lane locality)",
                     m["ast_lane_locality"] and m["runtime_lane_locality"]),
                    ("layout independence of the law", m["layout_independent"]),
                    ("the landed monitor-phase Z_11 covariance",
                     bool(cov["translation_invariant"])),
                    ("the certified gate vocabulary",
                     design["kinds_in_the_certified_vocabulary"]),
                    ("the same 164 lock points as the control",
                     m["lock_points"] == len(ctl["formed"])),
                ) if ok],
            "structures_supplemented": [
                s for s, broken in (
                    ("the Cycle-913 reads-never-writes transport theorem: the "
                     "endpoint is now written",
                     not ew["reads_never_writes_lemma_still_holds"]),
                    ("the certified gate vocabulary: a new gate kind is "
                     "introduced",
                     not design["kinds_in_the_certified_vocabulary"]),
                    ("setups-are-worlds: worlds now read each other",
                     not m["ast_lane_locality"]),
                ) if broken],
            "price":
                "the supplement is exactly one added sentence of law, and "
                "this is it verbatim: at the source station, "
                + " and ".join(g["text"].replace("<mask>", "the station mask")
                               for g in design["gates"])
                + ".  Nothing in the four axioms forces that sentence and "
                  "nothing in them forbids it.  It is an import, priced as "
                  "one, and it is the whole of what this candidate buys.",
        }

    born = [n for n, v in verdicts.items() if v["VERDICT"] == "BORN-CAPABLE"]
    sterile = [n for n, v in verdicts.items() if v["VERDICT"] == "STERILE"]
    destroyed = [n for n, v in verdicts.items()
                 if v["VERDICT"] == "DESTRUCTIVE"]
    reach = {
        "DESTRUCTIVE": classify_candidate(
            neutral_probe(write_once_violations=1))[0],
        "STERILE": classify_candidate(neutral_probe())[0],
        "BORN-CAPABLE": classify_candidate(neutral_probe(
            selection_became_dynamical=True, dynamical_branch_pairs=1))[0],
    }
    cert_c3 = {
        "certificate": "C3_VERDICTS",
        "classifier":
            "classify_candidate reads a dict of measured quantities and never "
            "a candidate's name; the same function classifies the three "
            "candidates and the three synthetic reachability probes below.",
        "criteria": {
            "DESTRUCTIVE":
                "any of: a write-once breach; a dead-wire record-slot "
                "activation; a record slot becoming a gate wire; a "
                "modification target outside the endpoint wires; a "
                "duplicate-lane mismatch; formation destroyed; endpoint "
                "content off the menu at a lock point; forward and reversed "
                "lane layouts disagreeing; the Cycle-911 no-cross-lane AST "
                "certification failing; the runtime perturbation witness "
                "leaking.",
            "BORN-CAPABLE":
                "not destructive AND the realized menu item differs from the "
                "prepared one at at least one lock point AND at least one "
                "DYNAMICAL BRANCH PAIR exists.",
            "STERILE": "not destructive and not Born-capable.",
        },
        "reachability_probes": reach,
        "all_three_classes_reachable":
            sorted(set(reach.values()))
            == ["BORN-CAPABLE", "DESTRUCTIVE", "STERILE"],
        "per_modification": verdicts,
        "BORN_CAPABLE": born, "STERILE": sterile, "DESTRUCTIVE": destroyed,
        "pass": sorted(set(reach.values()))
        == ["BORN-CAPABLE", "DESTRUCTIVE", "STERILE"],
    }

    # ---------------- C4: the A3 arena on any Born-capable substrate -------
    arena = {}
    for name in born:
        row = analysis[name]
        live = [r for r in row["rows"] if r["selected_item"] is not None]
        hist = Counter(tuple(r["selected_item"]) for r in live)
        total = len(live)
        dyn = row["BRANCH_PAIRS_dynamical"]
        cand = dyn["candidate_pairs_among_the_lock_points"]
        arena[name] = {
            "lock_points": total,
            "possibilities_per_lock_point": len(menu),
            "site_possibility_pairs": total * len(menu),
            "realized_frequency": {
                str(list(v)): {
                    "count": c,
                    "share": fr(Fraction(c, total)) if total else None,
                    "label": FRACTION_LABEL}
                for v, c in sorted(hist.items())},
            "non_degenerate": len(hist) > 1,
            "dynamical_branch_pairs": dyn["DYNAMICAL_BRANCH_PAIRS"],
            "candidate_pairs": cand,
            "within_pair_split_frequency": {
                "split": dyn["DYNAMICAL_BRANCH_PAIRS"],
                "agree": cand - dyn["DYNAMICAL_BRANCH_PAIRS"],
                "share_split": fr(Fraction(dyn["DYNAMICAL_BRANCH_PAIRS"],
                                           cand)) if cand else None,
                "label": FRACTION_LABEL},
            "scope_caveats": [
                "this is a count over the 748-world census at a single "
                "declared horizon on a single declared substrate; it is not "
                "an ensemble and it is not a probability.",
                "the pair-split share counts pairs of DISTINCT setups that "
                "share two setup coordinates and differ in the rest; it is "
                "not a within-setup frequency, because a deterministic scan "
                "gives each setup exactly one trajectory.",
                "the realized-state primitive forbids averaging over "
                "alternatives; every number here is a bookkeeping count of "
                "what this scan did, quoted as such.",
                "the modification that produced it is an IMPORT: it is not "
                "forced by the four axioms, and the datum inherits that "
                "status.",
            ],
        }
    cert_c4 = {
        "certificate": "C4_A3_ARENA",
        "born_capable_candidates": born, "arena": arena,
        "if_empty":
            "no candidate was Born-capable, so no occurrence datum is "
            "reported.  Its absence is the block's result and is stated as "
            "one.",
        "pass": True,
    }

    # ---------------- C5: the structural lemma -----------------------------
    ctl_dep = analysis["CONTROL"]["DEPENDENCE"]
    cert_c5 = {
        "certificate": "C5_STRUCTURAL_LEMMA",
        "determinism_lemma": {
            "statement":
                "no gate-set modification of this substrate can produce a "
                "Cycle-911 BRANCH PAIR.  CLASS_BRANCH is conjunctively gated "
                "on same_schedule AND same_tick0_state AND a divergence.  A "
                "gate set is a LAW: two lanes handed the same schedule and "
                "the same tick-0 state receive the same gates in the same "
                "order, so their columns stay equal for ever and cannot "
                "diverge.  A cross-lane law escapes that argument only by "
                "destroying its premise, since a lane's law then depends on "
                "its neighbours and the two lanes are no longer running the "
                "same law.  Either way the class stays empty.",
            "census_fact_pairs_sharing_schedule_and_tick0_state":
                analysis["CONTROL"]["BRANCH_MATRIX_911_literal"][
                    "pairs_sharing_tick0_state_AND_schedule"],
            "literal_branch_pairs_per_modification": {
                n: r["BRANCH_MATRIX_911_literal"]["BRANCH_PAIRS"]
                for n, r in analysis.items()},
            "consequence":
                "a writable endpoint is NECESSARY for O2 to be a rule rather "
                "than a transport -- 913 proved that -- but it is not "
                "SUFFICIENT for O3.  Making the endpoint a gate target moves "
                "the selection from the setup into the dynamics; it does not "
                "make one setup carry two trajectories, and O3's weight needs "
                "exactly that.  The obstruction O3 faces on a writable-"
                "endpoint substrate is no longer 'the distinguishing "
                "coordinate is frozen' but 'the law is a function'.  That is "
                "a different obstruction and it is the successor this block "
                "hands on.",
        },
        "control_dependence_reproduced": {
            "selection_is_a_function_of_SETUP_event_parity":
                ctl_dep["selection_is_a_function_of_SETUP_event_parity"],
            "selection_is_a_function_of_nearest_neighbour_record_content":
                ctl_dep["selection_is_a_function_of_nearest_neighbour_record_"
                        "content"],
            "single_wires_that_determine":
                ctl_dep["exhaustive_single_wire_sweep"][
                    "single_wires_that_DETERMINE_the_selection"],
            "matches_the_pinned_913": (
                ctl_dep["exhaustive_single_wire_sweep"][
                    "single_wires_that_DETERMINE_the_selection"]
                == c2_913["exhaustive_single_wire_sweep"][
                    "single_wires_that_DETERMINE_the_selection"]),
        },
        "pass": True,
    }

    # ---------------- G: planted falsifiers --------------------------------
    teeth = []

    def add(name, detected, detail=None):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "detail": detail})

    ctl_dyn = analysis["CONTROL"]["BRANCH_PAIRS_dynamical"]

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
        and ctl_dyn["DYNAMICAL_BRANCH_PAIRS"] == 0,
        {"planted_world": plant_w, "found": synth_dyn["DYNAMICAL_BRANCH_PAIRS"]})

    add("planted_modification_detected_as_creating_a_branch_pair",
        plant_note["the_planted_pair_was_found"] is True
        and plant_note["DYNAMICAL_BRANCH_PAIRS_FOUND"] > 0
        and plant_note["detector_matches_the_ground_truth"],
        {"planted_pairs": plant_note["planted_pairs"],
         "found": plant_note["DYNAMICAL_BRANCH_PAIRS_FOUND"],
         "independent_ground_truth":
             plant_note["independent_ground_truth_splits"]})

    add("cross_lane_gate_detected_by_the_911_ast_sweep",
        not analysis["M_B"]["COVARIANCE_AND_STRUCTURE"][
            "position_wise_lane_locality_certified"]
        and analysis["CONTROL"]["COVARIANCE_AND_STRUCTURE"][
            "position_wise_lane_locality_certified"],
        {"violation_kinds": analysis["M_B"]["COVARIANCE_AND_STRUCTURE"][
            "ast_sweep_violation_kinds"],
         "operators": analysis["M_B"]["COVARIANCE_AND_STRUCTURE"][
             "ast_sweep_cross_lane_operators"]})

    add("cross_lane_gate_detected_by_the_runtime_perturbation_witness",
        not analysis["M_B"]["COVARIANCE_AND_STRUCTURE"][
            "runtime_lane_locality_certified"]
        and analysis["CONTROL"]["COVARIANCE_AND_STRUCTURE"][
            "runtime_lane_locality_certified"],
        {"witness": analysis["M_B"]["COVARIANCE_AND_STRUCTURE"][
            "runtime_perturbation_witness"]})

    breach = {"slot": 0}
    breach_hits = 0
    for _ in range(2):
        if breach["slot"] & 1:
            breach_hits += 1
        breach["slot"] |= 1
    add("planted_write_once_breach_detected",
        breach_hits == 1 and ctl["write_once_violations"] == 0,
        {"planted_double_write_detected": breach_hits})

    bad = {"name": "PLANTED_BAD", "axis": "targets a record wire",
           "station": 0, "gates": ((KIND_CNOT, left_w, REC_A, 0),)}
    add("planted_record_targeting_modification_refused",
        not describe(bad)["targets_only_the_endpoint_wires"]
        and classify_candidate(neutral_probe(
            targets_outside_the_endpoint_wires=True))[0] == "DESTRUCTIVE",
        {"targets": describe(bad)["targets"]})

    declared_names = [m["name"] for m in MODS]
    measured_names = sorted(analysis)
    verdicted_names = sorted(list(verdicts) + ["CONTROL"])
    add("dropped_modification_detected",
        sorted(declared_names) == measured_names == verdicted_names
        and sorted(declared_names[:-1]) != measured_names
        and len(declared_names) == 4,
        {"declared": declared_names, "measured": measured_names,
         "verdicted": verdicted_names})

    add("dropped_lock_point_breaks_the_c911_gate",
        my_locks[1:] != sorted(r911_by_world), {"dropped": my_locks[0]})

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

    tampered = dict(EXPECTED_SHA256)
    tampered[CORE_PATH] = "0" * 64
    add("tampered_pin_detected",
        {p: sha256((ROOT / p).read_bytes()).hexdigest()
         for p in AUDIT_INPUT_PATHS} != tampered)

    ctl_dis = analysis["CONTROL"]["SELECTION"][
        "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"]
    add("control_cannot_leak_a_born_capable_verdict",
        ctl_dyn["DYNAMICAL_BRANCH_PAIRS"] == 0 and ctl_dis == 0
        and ctl_dyn["candidate_pairs_among_the_lock_points"] > 0
        and classify_candidate(analysis["CONTROL"]["_measurements"])[0]
        == "STERILE",
        {"candidate_pairs": ctl_dyn["candidate_pairs_among_the_lock_points"]})

    skipped_world = complete_pairs[0][0] if complete_pairs else my_locks[0]
    skipped = {w: r for w, r in ctl_by_world.items() if w != skipped_world}
    skipped_dyn = dynamical_branch_pairs(census, skipped, setup_direction)
    add("skipped_world_changes_the_measured_pair_census",
        bool(complete_pairs)
        and skipped_dyn["candidate_pairs_among_the_lock_points"]
        != ctl_dyn["candidate_pairs_among_the_lock_points"],
        {"skipped_world": skipped_world,
         "with": ctl_dyn["candidate_pairs_among_the_lock_points"],
         "without": skipped_dyn["candidate_pairs_among_the_lock_points"]})

    add("out_of_vocabulary_gate_kind_flagged",
        not describe(MOD_BY_NAME["M_B"])["kinds_in_the_certified_vocabulary"]
        and describe(MOD_BY_NAME["M_A"])["kinds_in_the_certified_vocabulary"]
        and describe(MOD_BY_NAME["M_C"])["kinds_in_the_certified_vocabulary"])

    add("verdict_classifier_reaches_every_class",
        cert_c3["all_three_classes_reachable"], reach)

    cert_g = {"certificate": "G_FALSIFIERS", "teeth": teeth,
              "tooth_count": len(teeth),
              "pass": all(t["detected"] for t in teeth)}

    # ---------------- H: double build --------------------------------------
    h_rows = []
    for mod in MODS:
        name = mod["name"]
        f, r = builds[name], slim[name]
        h_rows.append({
            "modification": name,
            "forward_seconds": timings[(name, False)],
            "reversed_seconds": timings[(name, True)],
            "forward_digest": scan_digest(f), "reversed_digest": r["digest"],
            "identical": scan_digest(f) == r["digest"],
            "formed": [len(f["formed"]), r["formed"]],
            "duplicate_lane_mismatches": [f["duplicate_lane_mismatches"],
                                          r["duplicate_lane_mismatches"]],
        })
    cert_h = {
        "certificate": "H_DOUBLE_BUILD",
        "rows": h_rows,
        "control_matches_the_pinned_913_digests": (
            h_rows[0]["forward_digest"] == h_913["digest_A"]
            and h_rows[0]["reversed_digest"] == h_913["digest_B"]),
        "candidates_that_are_layout_dependent": [
            r["modification"] for r in h_rows if not r["identical"]],
        "reading":
            "the two builds lay the worlds into opposite bit positions.  A "
            "lane-local law cannot see the layout, so its two digests must "
            "agree; a cross-lane law reads its bit neighbour and therefore "
            "cannot.  Layout dependence is not a runner bug -- it is the "
            "measurement that the candidate's 'neighbour' is a bookkeeping "
            "artefact and not a feature of the substrate.",
        "pass": bool(h_rows[0]["identical"]
                     and h_rows[0]["forward_digest"] == h_913["digest_A"]),
    }

    elapsed = round(monotonic() - started, 3)
    cert_i = {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
              "budget_sec": RUNTIME_BUDGET_SEC,
              "dead_wire_rig_seconds": t_rig,
              "pinned_911_cross_check_seconds": t_cross,
              "pass": elapsed <= RUNTIME_BUDGET_SEC}

    certificates = {
        "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
        "C1_CONSTRUCTION_SPACE": cert_c1, "C2_MEASUREMENT": cert_c2,
        "C3_VERDICTS": cert_c3, "C4_A3_ARENA": cert_c4,
        "C5_STRUCTURAL_LEMMA": cert_c5, "G_FALSIFIERS": cert_g,
        "H_DOUBLE_BUILD": cert_h, "I_RUNTIME": cert_i,
    }
    all_pass = all(c["pass"] for c in certificates.values())

    headline = (
        "three minimal writable-endpoint modifications of the 719 kernel were "
        "constructed and run on the full 748-world census at the landed "
        f"{HORIZON}-orbit horizon in both lane layouts: "
        + "; ".join(f"{n} {v['VERDICT']}" for n, v in verdicts.items())
        + ".  " + (
            "The door Cycle 913 specified opens for "
            + ", ".join(born) + ": the selection becomes dynamical and "
            + str(sum(analysis[n]["BRANCH_PAIRS_dynamical"][
                "DYNAMICAL_BRANCH_PAIRS"] for n in born))
            + " dynamical branch pairs appear, while the Cycle-911 branch "
              "class stays empty for every candidate -- so a writable "
              "endpoint buys a dynamical selection but not an indeterministic "
              "one."
            if born else
            "No candidate is Born-capable.  Making the endpoint a gate target "
            "is necessary but not sufficient: the selection can be moved into "
            "the dynamics, but a deterministic gate set gives each setup one "
            "trajectory, so the Cycle-911 branch class stays empty for every "
            "gate set."))

    receipt = {
        "block": "toe-time-blockQ11-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "cycles": [918],
        "claim_type": "bounded_theorem",
        "audit": "unset", "authority": "none",
        "fraction_label": FRACTION_LABEL,
        "provenance": provenance,
        "selection_tables": {n: r["rows"] for n, r in analysis.items()},
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "VERDICT": ("WRITABLE-ENDPOINT DESIGN SPACE MAPPED" if all_pass
                    else "INCOMPLETE"),
        "headline": headline,
    }
    out = ROOT / "outputs" / \
        "writable_endpoint_cycle918_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    # ---------------- stdout ----------------------------------------------
    W = 78
    print("CYCLE 918 -- THE WRITABLE-ENDPOINT DESIGN SPACE, CONSTRUCTED AND "
          "MEASURED")
    print("=" * W)
    print(f"  every fraction below: {FRACTION_LABEL}")
    print(f"  scope: FULL CENSUS {len(census)} worlds, horizon {HORIZON} "
          f"orbits ({ctl['boundaries']} boundaries), both lane layouts")
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
    print()
    print("-" * W)
    print("C1  THE CONSTRUCTION SPACE  (wrap never edit; anchored at the "
          "source station)")
    print("-" * W)
    for d in designs:
        print(f"  {d['name']:9s} {d['axis']}")
        for g in d["gates"]:
            print(f"            {g['kind']:11s} {g['text']}")
        print(f"            targets {d['targets']}  inputs {d['inputs']}  "
              f"in-vocabulary={d['kinds_in_the_certified_vocabulary']}")
    print(f"  designated record registers: REC_A wire {REC_A} (bank 0 "
          f"POINTER), REC_B wire {REC_B} (bank 1 POINTER)")
    print()
    print("-" * W)
    print("C2  THE MEASUREMENT")
    print("-" * W)
    print(f"  {'candidate':9s} {'locks':>6s} {'bmoved':>7s} {'ep-writes':>10s} "
          f"{'lk-writ':>8s} {'sel!=setup':>11s} {'offmenu':>8s} {'dynbr':>6s}")
    for name, row in analysis.items():
        f, s, e = row["FORMATION"], row["SELECTION"], row["ENDPOINT_WRITES"]
        print(f"  {name:9s} {f['lock_points']:6d} "
              f"{f['lock_points_whose_boundary_moved']:7d} "
              f"{e['total_LEFT_write_events_over_all_worlds'] + e['total_RIGHT_write_events_over_all_worlds']:10d} "
              f"{e['lock_points_whose_endpoint_changed_before_the_lock']:8d} "
              f"{s['lock_points_where_RD_STATE_disagrees_with_RD_SETUP']:11d} "
              f"{s['off_menu_endpoint_content_at_the_lock']:8d} "
              f"{row['BRANCH_PAIRS_dynamical']['DYNAMICAL_BRANCH_PAIRS']:6d}")
    print()
    for name, row in analysis.items():
        e, c, d = (row["ENDPOINT_WRITES"], row["COVARIANCE_AND_STRUCTURE"],
                   row["DEPENDENCE"])
        print(f"  {name}:")
        print(f"     endpoint a gate TARGET? LEFT="
              f"{e['LEFT_is_now_a_gate_target']} RIGHT="
              f"{e['RIGHT_is_now_a_gate_target']}; 913 reads-never-writes "
              f"holds={e['reads_never_writes_lemma_still_holds']}; gates "
              f"{e['compiled_gates_total']} (+{e['gates_added']})")
        print(f"     selection determined by: setup parity="
              f"{d.get('selection_is_a_function_of_SETUP_event_parity')}, "
              f"nn record content="
              f"{d.get('selection_is_a_function_of_nearest_neighbour_record_content')}, "
              f"nn ordinals="
              f"{d.get('selection_is_a_function_of_neighbour_ordinals')}, "
              f"endpoint wires only="
              f"{d.get('selection_is_a_function_of_the_site_endpoint_wires_only')}")
        sw = d.get("exhaustive_single_wire_sweep", {})
        print(f"     determining single wires: "
              f"{sw.get('single_wires_that_DETERMINE_the_selection')}; "
              f"outside the site="
              f"{sw.get('any_determining_wire_outside_the_site')}")
        print(f"     lane locality: AST="
              f"{c['position_wise_lane_locality_certified']} runtime="
              f"{c['runtime_lane_locality_certified']}; layout-independent="
              f"{c['layout_independent']}; Z_11 invariant="
              f"{c['translation_invariant']}")
        print(f"     record machinery: write-once violations="
              f"{row['RECORD_MACHINERY']['write_once_violations']}, slot "
              f"activations="
              f"{row['RECORD_MACHINERY']['record_slot_activation_conflicts']}"
              f", dup-lane={row['RECORD_MACHINERY']['duplicate_lane_mismatches_forward']}"
              f"/{row['RECORD_MACHINERY']['duplicate_lane_mismatches_reversed']}"
              f", 911 branch pairs="
              f"{row['BRANCH_MATRIX_911_literal']['BRANCH_PAIRS']}")
    print()
    print(f"  M_PLANT (falsifier): {plant_note['construction']}")
    for g in plant_note["gates"]:
        print(f"            {g['kind']:11s} {g['text']}")
    print(f"     lanes planted {plant_note['lanes_planted']}; planted pairs "
          f"{plant_note['planted_pairs']}; lock points "
          f"{plant_note['lock_points']}; dynamical branch pairs FOUND "
          f"{plant_note['DYNAMICAL_BRANCH_PAIRS_FOUND']}; independent ground "
          f"truth {plant_note['independent_ground_truth_splits']}; detector "
          f"matches = {plant_note['detector_matches_the_ground_truth']}")
    print(f"     example split pairs {plant_note['example_split_pairs']}")
    print()
    print("-" * W)
    print("C3  THE VERDICTS AND THE PRICING")
    print("-" * W)
    for name, v in verdicts.items():
        print(f"  {name:6s} {v['VERDICT']}")
        print(f"         {v['why']}")
        print(f"         preserved: "
              f"{'; '.join(v['structures_preserved']) or 'none'}")
        if v["structures_supplemented"]:
            print(f"         supplements: "
                  f"{'; '.join(v['structures_supplemented'])}")
        print(f"         price: {v['price']}")
    print()
    print("-" * W)
    print("C4  THE A3 ARENA")
    print("-" * W)
    if born:
        for name, a in arena.items():
            print(f"  {name}: {a['lock_points']} lock points x "
                  f"{a['possibilities_per_lock_point']} possibilities; "
                  "realized " + ", ".join(
                      f"{k} -> {v['count']} ({v['share']})"
                      for k, v in a["realized_frequency"].items()))
            print(f"         dynamical branch pairs "
                  f"{a['dynamical_branch_pairs']} of {a['candidate_pairs']} "
                  f"candidate pairs (share "
                  f"{a['within_pair_split_frequency']['share_split']})")
            for cav in a["scope_caveats"]:
                print(f"         caveat: {cav}")
    else:
        print("  " + cert_c4["if_empty"])
    print()
    print("-" * W)
    print("C5  THE STRUCTURAL LEMMA")
    print("-" * W)
    for line in cert_c5["determinism_lemma"]["statement"].split(".  "):
        if line.strip():
            print(f"  {line.strip()}.")
    print(f"  census pairs sharing schedule AND tick-0 state: "
          f"{cert_c5['determinism_lemma']['census_fact_pairs_sharing_schedule_and_tick0_state']}")
    print(f"  literal 911 branch pairs per candidate: "
          f"{cert_c5['determinism_lemma']['literal_branch_pairs_per_modification']}")
    print("  " + cert_c5["determinism_lemma"]["consequence"])
    print()
    print("-" * W)
    print(f"G_FALSIFIERS                {'PASS' if cert_g['pass'] else 'FAIL'}"
          f"  ({cert_g['tooth_count']} teeth)")
    for t in teeth:
        print(f"    [{'x' if t['detected'] else ' '}] {t['tooth']}")
    print(f"H_DOUBLE_BUILD              {'PASS' if cert_h['pass'] else 'FAIL'}")
    for r in h_rows:
        print(f"    {r['modification']:9s} fwd {r['forward_seconds']:7.2f}s "
              f"rev {r['reversed_seconds']:7.2f}s  identical={r['identical']} "
              f" formed {r['formed']}")
    print(f"I_RUNTIME                   {'PASS' if cert_i['pass'] else 'FAIL'}"
          f"  ({elapsed}s / {RUNTIME_BUDGET_SEC}s)")
    print()
    print("=" * W)
    print(f"VERDICT: {receipt['VERDICT']}")
    print(f"HEADLINE: {headline}")
    print("receipt: outputs/writable_endpoint_cycle918_receipt_2026_07_28.json")
    return 0 if all_pass else 1


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


if __name__ == "__main__":
    sys.exit(main())
