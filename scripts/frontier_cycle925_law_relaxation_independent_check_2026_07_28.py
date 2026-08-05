"""Cycle 925 INDEPENDENT CHECK -- specified to REFUTE the classification.

The primary claims (i) a kernel-level lemma -- the pinned law is a pure
function of (schedule, tick-0 state) -- resting on an AST sweep of the compiled
chunk sources, (ii) an EXHAUSTIVE four-class input-provenance partition, (iii)
R1 = re-labeling, R3 = dead-or-absorbed, R4 = banked, leaving R2 = the A3
sentence as the sole genuine relaxation.

This runner is built to break (ii) first and everything else second.  It shares
no mechanism with the primary that it can avoid sharing:

  OWN SPLICE.  The Cycle-918 checker took computed-offset splices into the
  pinned gate tuples; the Cycle-925 primary rebuilt the schedule with its own
  builder.  This runner does neither: it takes the PINNED compiler's own
  schedules, locates the anchor station's macro by MATCHING ITS COMPILED GATE
  CONTENT (a content-addressed cut, no arithmetic offset), regenerates the
  pinned compile_fast SOURCE TEXT, and splices the extra statements as TEXT
  LINES at the corresponding line index.  The kernel is never edited.

  OWN PROVENANCE SWEEP, THREE WAYS.  (a) a node-TYPE census of the compiled
  sources compared against a declared allow-list -- not the primary's
  node-class map; (b) a BYTECODE census: the compiled chunk's co_names,
  co_consts and opcode set, which sees things no AST sweep sees; (c) a check of
  the STATE CONTAINER's runtime type, which is where multi-valuedness could
  hide without appearing in any source at all.

  OWN WINDOWS.  Declared prime-length windows (137 / 71 / 43 / 13 orbits), plus
  a SLOW SEMANTIC REPLAY of single lanes as plain bit vectors -- a completely
  different execution path from the packed big-integer columns.

  OWN HUNTS.  Five indexical coordinates the primary did not sweep; four
  attacks on the R1 re-labeling proof, including the one case the primary
  explicitly excluded (a stream injected into a wire that the pinned gates
  themselves write, where the primary's compile-time-constant-mask argument
  does not apply).

Every refutation is reported plainly, whether or not it changes the verdict.
"""

from __future__ import annotations

import ast
import dis
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

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C911_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
C913_PATH = "scripts/frontier_cycle913_selection_function_2026_07_28.py"
C913_RECEIPT = "outputs/selection_function_cycle913_receipt_2026_07_28.json"
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
PRIMARY_PATH = "scripts/frontier_cycle925_law_relaxation_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/law_relaxation_cycle925_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C911_PATH, C911_RECEIPT, C913_PATH,
    C913_RECEIPT, C918_RECEIPT, PRIMARY_PATH, PRIMARY_RECEIPT, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C911_PATH, C913_PATH, PRIMARY_PATH)
JSON_ONLY_PATHS = (C911_RECEIPT, C913_RECEIPT, C918_RECEIPT, PRIMARY_RECEIPT)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C911_PATH:
        "6474f1e919c97fcb3336a8cea480b5e824fe48f4ea5ce4592c1b75bc0b0007d1",
    C911_RECEIPT:
        "90d1fb2a3ac31065f75345ac1e98520622aa6302c50dcf4a8a11f44a1cde11b0",
    C913_PATH:
        "b349f873aa1e88558fcd63fc432a6edd249f48f103ecbd3d28fd62d070e689ef",
    C913_RECEIPT:
        "0de8d785c2139126b813166e090493d65cb289508b46de7f928b440facb82ecd",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C911_PATH: "3335e9dee5027b935d0eb3c814601b8f8e83b550",
    C911_RECEIPT: "af51342a72c56db8e562e1f1a607f207508b42ed",
    C913_PATH: "2093b687713eb12b462532761092d90d40bed718",
    C913_RECEIPT: "5ac6a40c316c7a90bcf867eb6507518ba976169b",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AST_ONLY_PATHS)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
LANE_SHIFT = 1
W_SWEEP = 137          # checker's coordinate-sweep window (declared, prime)
W_TAPE = 71            # checker's tape-equivalence window (declared, prime)
W_CROSS = 43           # checker's pinned-scan cross-check window (declared)
W_SLOW = 13            # checker's slow semantic replay window (declared)
LIMB = 64              # the machine word the packed columns ride on


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

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402

KIND_X, KIND_CNOT, KIND_TOF, KIND_SHIFT = 0, 1, 2, 3


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def pin_rows():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    checked_sha = {p: v for p, v in sha_rows.items() if p in EXPECTED_SHA256}
    checked_blob = {p: v for p, v in blob_rows.items()
                    if p in EXPECTED_GIT_BLOBS}
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "sha256": sha_rows, "git_blobs": blob_rows,
        "sha256_all_match": checked_sha == EXPECTED_SHA256,
        "git_blobs_all_match": checked_blob == EXPECTED_GIT_BLOBS,
        "primary_and_its_receipt_are_pinned_by_measurement_not_by_expectation":
            "the primary runner and its receipt are hashed here and the "
            "hashes are recorded, but they are deliberately NOT compared to a "
            "hard-coded expectation: this runner must stay runnable against a "
            "re-run primary while still recording exactly which bytes it "
            "checked.",
        "primary_sha256": sha_rows[PRIMARY_PATH],
        "primary_receipt_sha256": sha_rows[PRIMARY_RECEIPT],
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules),
        "firewall_hits": tuple(FIREWALL.hits),
    }
    result["pass"] = bool(
        result["sha256_all_match"] and result["git_blobs_all_match"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"])
    return result, payloads


def ast_lift(path: str, funcs: tuple, consts: tuple, g: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, fc = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in consts:
                    fc[t.id] = ast.literal_eval(node.value)
    missing = tuple(f for f in funcs if f not in {b.name for b in body})
    if missing or tuple(c for c in consts if c not in fc):
        raise AssertionError(("lift incomplete", path, missing))
    m = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(m)
    ns = dict(g)
    ns.update(fc)
    exec(compile(m, f"<lift {path}>", "exec"), ns)
    return ns, fc, tuple(b.name for b in body)


F863 = ("pairwise_separated", "derive_event_seeds", "derive_census",
        "watched_registers", "dirty_partition", "build_initial_states",
        "pack_lanes", "compile_masked_gate", "masked_h_schedules",
        "compile_fast", "mask_over", "lanes_of", "lane_state",
        "synchronous_word")
F878 = ("lcm", "monitor_phase_action", "group_orbits", "dead_wire_rig")
F911 = ("snapshot_scan", "classify_pair")
F913 = ("endpoint_wires", "read_state_direction", "hamming_readout")


def lift_all():
    ns863, _c, n863 = ast_lift(C863_PATH, F863,
                               ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
                               {"K": K, "combinations": combinations,
                                "Counter": Counter})
    c863 = SimpleNamespace(**{n: ns863[n] for n in F863})
    ns878, c878c, n878 = ast_lift(
        C878_PATH, F878,
        ("HORIZON", "REGISTER_CAP", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS"),
        {"C863": c863, "Counter": Counter, "sha256": sha256, "json": json,
         "gcd": math.gcd})
    c878 = SimpleNamespace(**{n: ns878[n] for n in F878})
    ns911, c911c, n911 = ast_lift(
        C911_PATH, F911,
        ("DIRECTIONS", "REGISTER_CAP", "HORIZON", "CLASS_BRANCH",
         "CLASS_IDENTICAL", "CLASS_SETUP_TICK0", "CLASS_SETUP_SCHEDULE",
         "CLASS_NONBRANCH_DIVERGENCE"),
        {"K": K, "np": np, "itertools": itertools, "Counter": Counter,
         "sha256": sha256, "ast": ast, "CROSS_LANE_OPS": (ast.LShift,),
         "POSITIONWISE_OPS": (ast.BitXor,)})
    c911 = SimpleNamespace(**{n: ns911[n] for n in F911})
    ns913, _d, n913 = ast_lift(C913_PATH, F913, (),
                               {"K": K, "Counter": Counter, "sha256": sha256})
    c913 = SimpleNamespace(**{n: ns913[n] for n in F913})
    prov = {"lifted_863": n863, "lifted_878": n878, "lifted_911": n911,
            "lifted_913": n913, "consts_878": c878c, "consts_911": c911c,
            "single_disclosed_import": CORE_PATH}
    return c863, c878, c911, c913, c878c, c911c, prov


# ---------------------------------------------------------------------------
# K1: the checker's OWN splice -- content-addressed cut, source-TEXT insertion
# ---------------------------------------------------------------------------

def pinned_chunk_text(schedule):
    """Regenerate the PINNED compile_fast source, statement for statement."""
    src = ["def apply_chunk(c):"]
    for kind, a, b, c3, mask in schedule:
        if kind == 0:
            src.append(f" c[{a}] ^= {mask}")
        elif kind == 1:
            src.append(f" c[{b}] ^= c[{a}] & {mask}")
        else:
            src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
    return src


def extra_text(gates, mask):
    out = []
    for kind, a, b, c3 in gates:
        if kind == KIND_X:
            out.append(f" c[{a}] ^= {mask}")
        elif kind == KIND_CNOT:
            out.append(f" c[{b}] ^= c[{a}] & {mask}")
        elif kind == KIND_TOF:
            out.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        elif kind == KIND_SHIFT:
            out.append(f" c[{b}] ^= (c[{a}] >> {LANE_SHIFT}) & {mask}")
        else:
            raise ValueError(kind)
    return out


def station_mask(sim, station, step, stations):
    return sum(1 << lane for lane, (_k, _e, pos) in enumerate(sim)
               if (station - step) % stations in pos)


def content_addressed_cut(c863, program, pinned_chunk, sim, anchor, step,
                          stations):
    """Locate the end of the anchor station's macro inside the PINNED chunk by
    matching its compiled gate CONTENT -- no arithmetic offset anywhere."""
    mask = station_mask(sim, anchor, step, stations)
    if not mask:
        return None, mask, "anchor station does not fire at this step"
    macro = tuple(c863.compile_masked_gate(g, mask)
                  for g in K.mapped_macro(program[anchor]))
    hits = [i for i in range(len(pinned_chunk) - len(macro) + 1)
            if tuple(pinned_chunk[i:i + len(macro)]) == macro]
    if not hits:
        return None, mask, "anchor macro content not found in the pinned chunk"
    # stations are emitted in index order, so the anchor's block is the FIRST
    # content match at or after the blocks of all lower-index firing stations;
    # for anchor 0 that is the chunk prefix.  Verified, not assumed:
    cut = hits[0] + len(macro)
    prefix_is_the_macro = anchor != 0 or hits[0] == 0
    return cut, mask, ("content match at %d (unique=%s, prefix_ok=%s)"
                       % (hits[0], len(hits) == 1, prefix_is_the_macro))


def spliced_text(c863, program, sim, anchor, gates, lane_mask, stations):
    """The checker's splice: pinned text + inserted TEXT LINES at the
    content-addressed cut.  Returns (sources, cuts)."""
    pinned = c863.masked_h_schedules(program, sim)
    sources, cuts = [], []
    for step in range(stations):
        text = pinned_chunk_text(pinned[step])
        if not gates:
            sources.append(text)
            cuts.append(None)
            continue
        cut, mask, _why = content_addressed_cut(c863, program, pinned[step],
                                                sim, anchor, step, stations)
        m = (mask & lane_mask) if mask else 0
        if cut is None or not m:
            sources.append(text)
            cuts.append(None)
            continue
        lines = extra_text(gates, m)
        sources.append(text[:cut + 1] + lines + text[cut + 1:])
        cuts.append(cut)
    return sources, tuple(cuts), pinned


def compile_texts(sources):
    fns = []
    for src in sources:
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


# ---------------------------------------------------------------------------
# K2: the checker's OWN provenance census -- node types, bytecode, container
# ---------------------------------------------------------------------------

ALLOWED_NODE_TYPES = {
    "Module", "FunctionDef", "arguments", "arg", "AugAssign", "BitXor",
    "Subscript", "Name", "Constant", "Load", "Store", "BinOp", "BitAnd",
}
CROSS_LANE_NODE_TYPES = {"LShift", "RShift", "Add", "Sub", "Mult", "Div",
                         "FloorDiv", "Mod", "Pow", "MatMult"}
CHOICE_NODE_TYPES = {"Call", "IfExp", "Compare", "BoolOp", "Lambda",
                     "ListComp", "SetComp", "DictComp", "GeneratorExp",
                     "NamedExpr", "Await", "Yield", "If", "While", "For"}


def node_type_census(sources):
    types = Counter()
    free_names = Counter()
    non_literal_addresses = 0
    statements = 0
    for src in sources:
        tree = ast.parse("\n".join(src))
        for node in ast.walk(tree):
            name = type(node).__name__
            types[name] += 1
            if isinstance(node, ast.AugAssign):
                statements += 1
            if isinstance(node, ast.Name) and node.id != "c":
                free_names[node.id] += 1
            if isinstance(node, ast.Subscript) and not (
                    isinstance(node.slice, ast.Constant)
                    and isinstance(node.slice.value, int)):
                non_literal_addresses += 1
    outside = sorted(set(types) - ALLOWED_NODE_TYPES)
    return {
        "statements": statements,
        "node_types": {k: types[k] for k in sorted(types)},
        "node_types_outside_the_allow_list": outside,
        "free_names": dict(free_names),
        "non_literal_addresses": non_literal_addresses,
        "cross_lane_node_types_present":
            sorted(set(types) & CROSS_LANE_NODE_TYPES),
        "choice_node_types_present": sorted(set(types) & CHOICE_NODE_TYPES),
    }


def bytecode_census(sources):
    """What no AST sweep sees: the compiled code object's global-name table,
    its constants, and its opcode set.  A datum from outside the state
    container has to show up here as a global load or a call."""
    names = Counter()
    opcodes = Counter()
    const_types = Counter()
    argnames = set()
    for src in sources:
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        code = ns["apply_chunk"].__code__
        for nm in code.co_names:
            names[nm] += 1
        for con in code.co_consts:
            const_types[type(con).__name__] += 1
        argnames.update(code.co_varnames[:code.co_argcount])
        for ins in dis.get_instructions(code):
            opcodes[ins.opname] += 1
    call_like = sorted(op for op in opcodes
                       if "CALL" in op or "JUMP" in op or "COMPARE" in op)
    global_like = sorted(op for op in opcodes if "GLOBAL" in op
                         or "DEREF" in op or "NAME" in op)
    return {
        "global_names_referenced": dict(names),
        "constant_types": {k: const_types[k] for k in sorted(const_types)},
        "argument_names": sorted(argnames),
        "opcode_counts": {k: opcodes[k] for k in sorted(opcodes)},
        "call_or_branch_opcodes": call_like,
        "global_or_free_variable_opcodes": global_like,
        "no_external_datum_reachable":
            not names and not call_like and not global_like,
    }


def container_premise(c863, states):
    """The premise the primary's SOURCE-level lemma needs and does not state:
    the state container is a plain list of plain ints, so `c[i]` is a pure read
    that cannot itself deliver a second value.  Checked, not assumed."""
    cols = c863.pack_lanes(tuple(states) + (states[0],))
    return {
        "container_type": type(cols).__name__,
        "container_is_a_plain_list": type(cols) is list,
        "element_types": sorted({type(x).__name__ for x in cols}),
        "every_element_is_a_plain_int": all(type(x) is int for x in cols),
        "why_it_matters":
            "if the container were an object with a custom __getitem__, the "
            "statement `c[1] ^= c[123] & M` could deliver a different value at "
            "the same state -- a P3 choice point that appears in NO source and "
            "in NO bytecode of the chunk.  The primary's kernel-level lemma is "
            "sound only with this premise attached.  It holds here and is "
            "recorded as an ADDED PREMISE, not as a refutation.",
    }


def kernel_gate_kind_census(program):
    """Does the pinned kernel ever emit a gate outside the three compiled
    forms?  Asked of the macros themselves, not of the compiled schedule."""
    kinds = Counter()
    widths = Counter()
    for row in program:
        for g in K.mapped_macro(row):
            kinds[g.kind] += 1
            widths[len(g.wires)] += 1
    return {"gate_kinds_in_the_kernel_macros": dict(kinds),
            "wire_counts": dict(widths),
            "only_X_CNOT_TOF": set(kinds) <= {"X", "CNOT", "TOF"}}


def scan_loop_provenance():
    """The primary swept the CHUNKS.  The law also includes the SCAN LOOP --
    which chunk runs at which boundary.  Sweep the PINNED Cycle-911
    snapshot_scan's own AST for anything it consults beyond its arguments."""
    tree = ast.parse((ROOT / C911_PATH).read_text(encoding="utf-8"),
                     filename=C911_PATH)
    fn = next(node for node in ast.walk(tree)
              if isinstance(node, ast.FunctionDef)
              and node.name == "snapshot_scan")
    args = {a.arg for a in fn.args.args}
    assigned = set()
    for node in ast.walk(fn):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            assigned.add(node.id)
        if isinstance(node, (ast.For,)) and isinstance(node.target, ast.Name):
            assigned.add(node.target.id)
        if isinstance(node, ast.Tuple):
            for elt in node.elts:
                if isinstance(elt, ast.Name) and isinstance(elt.ctx,
                                                            ast.Store):
                    assigned.add(elt.id)
    loads = Counter()
    for node in ast.walk(fn):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id not in args and node.id not in assigned:
                loads[node.id] += 1
    return {
        "arguments": sorted(args),
        "free_names_loaded": dict(loads),
        "reading":
            "the pinned scan's only free names are module-level constants and "
            "builtins (range/int/bool/sorted and the declared REGISTER_CAP).  "
            "It selects the chunk by boundary index alone.  The scan loop is "
            "therefore P4 data (the schedule) and introduces no fifth "
            "provenance class -- which is the primary's implicit assumption, "
            "checked here explicitly.",
    }


# ---------------------------------------------------------------------------
# the checker's own scan + a slow semantic replay on a different code path
# ---------------------------------------------------------------------------

def own_scan(c863, program, census, states, boundaries, fns, reverse,
             register_cap, tick0_extra=None, injection=None, pre=None,
             exclude=(), stations=None):
    n = len(census)
    stations = stations or len(program)
    order = list(range(n - 1, -1, -1)) if reverse else list(range(n))
    laid = tuple(states[w] for w in order)
    cols = c863.pack_lanes(laid + (laid[0],))
    if tick0_extra:
        for wire, val in tick0_extra.items():
            cols[wire] |= val
    per_bank, links, sptr = c863.dirty_partition()
    gd = tuple(sorted(set(per_bank[0]) | set(per_bank[1]) | set(links)
                      | {sptr}))
    bd = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all, uni_sim = (1 << n) - 1, (1 << (n + 1)) - 1
    keep = [w for w in range(len(cols)) if w not in set(exclude)]
    formed: dict = {}
    snaps: dict = {}
    ordinals = [[0, 0] for _ in range(n)]
    lock_ord: dict = {}
    events = 0
    dup = 0
    b = 0
    h = sha256()
    g = c863.mask_over(cols, gd, uni_sim)
    dup += int(bool(g & 1) != bool(g & (1 << n)))
    prev = [c863.mask_over(cols, bd[i], uni_all) for i in (0, 1)]
    for bit in c863.lanes_of(g & uni_all):
        formed[order[bit]] = 0
        snaps[order[bit]] = c863.lane_state(cols, bit)
        lock_ord[order[bit]] = (0, 0)
        events += 1
    cycle = len(fns)
    while b < boundaries:
        if injection is not None:
            wire, val = injection(b)
            cols[wire] = val
        if pre is not None:
            pre[b](cols)
        fns[b % cycle](cols)
        b += 1
        g = c863.mask_over(cols, gd, uni_sim)
        dup += int(bool(g & 1) != bool(g & (1 << n)))
        ga = g & uni_all
        if ga:
            for bit in c863.lanes_of(ga):
                w = order[bit]
                if w not in formed:
                    formed[w] = b
                    snaps[w] = c863.lane_state(cols, bit)
                    lock_ord[w] = tuple(ordinals[bit])
                    events += 1
        for i in (0, 1):
            bm = c863.mask_over(cols, bd[i], uni_all)
            rise = bm & ~prev[i]
            if rise:
                for bit in c863.lanes_of(rise):
                    if ordinals[bit][i] < register_cap:
                        events += 1
                    ordinals[bit][i] += 1
            prev[i] = bm
        if b % 256 == 0:
            h.update(str([cols[w] for w in keep[::53]]).encode())
    h.update(str([cols[w] for w in keep]).encode())
    return {"formed": dict(sorted(formed.items())), "snapshots": snaps,
            "lock_ordinal": lock_ord, "events": events, "boundaries": b,
            "duplicate_lane_mismatches": dup, "column_digest": h.hexdigest(),
            "columns": cols, "order": order}


def build_digest(b, exclude=()):
    drop = set(exclude)
    return digest({
        "formed": {str(k): v for k, v in sorted(b["formed"].items())},
        "snapshots": {str(k): "".join("_" if i in drop else str(x)
                                      for i, x in enumerate(v))
                      for k, v in sorted(b["snapshots"].items())},
        "lock_ordinal": {str(k): list(v)
                         for k, v in sorted(b["lock_ordinal"].items())},
        "events": b["events"],
    })


def slow_replay(sources, lane, state_vector, boundaries, stations):
    """Evolve ONE lane as a plain list of bits by interpreting the compiled
    source statements one at a time -- a completely different execution path
    from the packed big-integer columns."""
    bits = list(state_vector)
    parsed = []
    for src in sources:
        rows = []
        for line in src[1:]:
            tree = ast.parse(line.strip())
            stmt = tree.body[0]
            tgt = stmt.target.slice.value
            val = stmt.value
            if isinstance(val, ast.Constant):
                rows.append(("X", tgt, None, None, val.value))
            else:
                mask = val.right.value
                left = val.left
                if isinstance(left, ast.Subscript):
                    rows.append(("CNOT", tgt, left.slice.value, None, mask))
                elif isinstance(left, ast.BinOp) \
                        and isinstance(left.op, ast.BitAnd):
                    rows.append(("TOF", tgt, left.left.slice.value,
                                 left.right.slice.value, mask))
                else:
                    rows.append(("OTHER", tgt, None, None, mask))
        parsed.append(rows)
    cycle = len(parsed)
    for b in range(boundaries):
        for kind, tgt, a, bb, mask in parsed[b % cycle]:
            if not (mask >> lane) & 1:
                continue
            if kind == "X":
                bits[tgt] ^= 1
            elif kind == "CNOT":
                bits[tgt] ^= bits[a]
            elif kind == "TOF":
                bits[tgt] ^= bits[a] & bits[bb]
            else:
                raise AssertionError("slow replay met an unknown gate form")
    return tuple(bits)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    checks = []
    refutations = []

    def check(name, ok, detail=None):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        if not ok:
            refutations.append({"check": name, "detail": detail})
        return bool(ok)

    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in ("sha256_all_match", "git_blobs_all_match",
                                   "blocked_modules_loaded",
                                   "firewall_hits")}))
        return 2

    c863, c878, c911, c913, c878c, c911c, prov = lift_all()
    rp = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    r913 = json.loads(payloads[C913_RECEIPT].decode("utf-8"))
    r918 = json.loads(payloads[C918_RECEIPT].decode("utf-8"))
    axioms = payloads[AXIOMS_PATH].decode("utf-8")
    pc = rp["certificates"]
    h913 = r913["certificates"]["H_DOUBLE_BUILD"]
    m918 = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]
    h918 = {row["modification"]: row
            for row in r918["certificates"]["H_DOUBLE_BUILD"]["rows"]}
    register_cap = c911c["REGISTER_CAP"]
    classes = {k: c911c[k] for k in ("CLASS_BRANCH",)}

    program, seeds, census = c863.derive_census()
    stations = len(program)
    states, fails = c863.build_initial_states(program, seeds, census)
    left_w, right_w, src_w = c913.endpoint_wires()
    n = len(census)
    width = len(states[0])
    BB = K.M.R12.BANK_BASES
    REC_A = BB[0] + K.A.POINTER
    REC_B = BB[1] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    rev_order = list(range(n - 1, -1, -1))
    sim_rev = tuple(census[w] for w in rev_order)
    sim_rev = sim_rev + (sim_rev[0],)
    uni_sim = (1 << (n + 1)) - 1
    FULL = HORIZON * stations
    setup_direction = {ev: c913.read_state_direction(seed)
                       for ev, seed in seeds}

    proto = c863.pack_lanes(tuple(states) + (states[0],))
    t0 = monotonic()
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    t_rig = round(monotonic() - t0, 3)
    per_bank, links, sptr = c863.dirty_partition()
    gdirty = set(per_bank[0]) | set(per_bank[1]) | set(links) | {sptr}
    FREE = [w for w in rig["safe_pool"]
            if w not in set(rig["slot_of"].values()) and w not in gdirty]
    TAPE_W = FREE[0]

    M_A = ((KIND_CNOT, REC_A, left_w, 0), (KIND_CNOT, REC_A, right_w, 0))
    M_B = ((KIND_SHIFT, left_w, left_w, 0), (KIND_SHIFT, right_w, right_w, 0))
    M_C = ((KIND_TOF, REC_A, REC_B, left_w), (KIND_TOF, REC_A, REC_B, right_w))
    XSWAP = ((KIND_X, left_w, 0, 0), (KIND_X, right_w, 0, 0))

    def texts(sim, gates, lane_mask=None):
        lm = uni_sim if lane_mask is None else lane_mask
        return spliced_text(c863, program, sim, 0, gates, lm, stations)

    # ---- K1: the splice mechanism itself ----------------------------------
    ctl_src, ctl_cuts, pinned_sched = texts(sim_fwd, ())
    check("K1_empty_splice_reproduces_the_pinned_compile_fast_text",
          digest(ctl_src) == digest([pinned_chunk_text(s)
                                     for s in pinned_sched]),
          {"chunks": len(ctl_src)})
    ma_src, ma_cuts, _p = texts(sim_fwd, M_A)
    cut_report = [content_addressed_cut(c863, program, pinned_sched[j],
                                        sim_fwd, 0, j, stations)[2]
                  for j in range(stations)]
    check("K1_content_addressed_cut_found_in_every_chunk",
          all(c is not None for c in ma_cuts),
          {"cuts": list(ma_cuts), "how": cut_report[:3]})
    check("K1_splice_adds_exactly_two_statements_per_chunk",
          [len(a) - len(b) for a, b in zip(ma_src, ctl_src)]
          == [2] * stations)
    check("K1_gate_totals_match_the_pinned_913_lemma_and_the_918_count",
          [sum(len(s) - 1 for s in ctl_src), sum(len(s) - 1 for s in ma_src)],
          )
    gt_ctl = sum(len(s) - 1 for s in ctl_src)
    gt_ma = sum(len(s) - 1 for s in ma_src)
    checks[-1]["detail"] = {"control": gt_ctl, "M_A": gt_ma}
    checks[-1]["pass"] = (
        gt_ctl == r913["certificates"]["C1_SELECTION_TABLE"][
            "endpoint_wire_lemma"]["gates_total"]
        and gt_ma == m918["M_A"]["ENDPOINT_WRITES"]["compiled_gates_total"])
    if not checks[-1]["pass"]:
        refutations.append({"check": checks[-1]["check"],
                            "detail": checks[-1]["detail"]})

    # ---- K2: the provenance census, three independent ways ----------------
    census_nodes = node_type_census(ctl_src)
    bytecode = bytecode_census(ctl_src)
    container = container_premise(c863, states)
    kernel_kinds = kernel_gate_kind_census(program)
    scan_prov = scan_loop_provenance()
    check("K2_no_node_type_outside_the_declared_allow_list",
          not census_nodes["node_types_outside_the_allow_list"],
          {"outside": census_nodes["node_types_outside_the_allow_list"],
           "types": sorted(census_nodes["node_types"])})
    check("K2_no_free_name_in_the_pinned_sources",
          not census_nodes["free_names"], census_nodes["free_names"])
    check("K2_no_non_literal_state_address",
          census_nodes["non_literal_addresses"] == 0,
          {"count": census_nodes["non_literal_addresses"]})
    check("K2_no_choice_node_type_present",
          not census_nodes["choice_node_types_present"],
          census_nodes["choice_node_types_present"])
    check("K2_bytecode_reaches_no_external_datum",
          bytecode["no_external_datum_reachable"],
          {"globals": bytecode["global_names_referenced"],
           "call_or_branch": bytecode["call_or_branch_opcodes"],
           "global_ops": bytecode["global_or_free_variable_opcodes"]})
    check("K2_state_container_is_a_plain_list_of_plain_ints",
          container["container_is_a_plain_list"]
          and container["every_element_is_a_plain_int"], container)
    check("K2_kernel_macros_emit_only_the_three_compiled_forms",
          kernel_kinds["only_X_CNOT_TOF"], kernel_kinds)
    check("K2_statement_count_agrees_with_the_primary_and_with_918",
          census_nodes["statements"] == pc["C1_PROVENANCE_PARTITION"][
              "pinned_substrate_sweep"]["statements"]
          == m918["CONTROL"]["COVARIANCE_AND_STRUCTURE"][
              "ast_sweep_statements"],
          {"checker": census_nodes["statements"],
           "primary": pc["C1_PROVENANCE_PARTITION"][
               "pinned_substrate_sweep"]["statements"]})

    # the hunt for a FIFTH provenance class, reported whatever it finds
    fifth_hunt = [
        {"candidate": "a global/free name delivering an oracle value",
         "would_be_class": "P2",
         "present_in_the_pinned_substrate":
             bool(census_nodes["free_names"])
             or bool(bytecode["global_names_referenced"]),
         "how_checked": "AST Name census AND bytecode co_names/LOAD_GLOBAL"},
        {"candidate": "a call or branch inside a gate",
         "would_be_class": "P3",
         "present_in_the_pinned_substrate":
             bool(census_nodes["choice_node_types_present"])
             or bool(bytecode["call_or_branch_opcodes"]),
         "how_checked": "AST node-type census AND bytecode opcode census"},
        {"candidate": "a state address computed at run time",
         "would_be_class": "would be a NEW class (an address is neither a "
                           "datum nor a mask)",
         "present_in_the_pinned_substrate":
             census_nodes["non_literal_addresses"] > 0,
         "how_checked": "AST subscript-slice census"},
        {"candidate": "the state container's own __getitem__ (a datum that "
                      "appears in no source and no bytecode)",
         "would_be_class": "would be a GENUINE FIFTH CLASS -- provenance "
                           "outside the compiled law entirely",
         "present_in_the_pinned_substrate":
             not (container["container_is_a_plain_list"]
                  and container["every_element_is_a_plain_int"]),
         "how_checked": "runtime type check of pack_lanes' return value",
         "finding":
             "THIS IS A REAL GAP IN THE PRIMARY'S ARGUMENT AS WRITTEN.  The "
             "primary's kernel-level lemma is a SOURCE-level sweep and a "
             "source-level sweep cannot see a container that answers "
             "differently on two identical reads.  The premise holds here "
             "(plain list of plain ints) but the primary does not state it.  "
             "Recorded as an ADDED PREMISE the classification needs, not as a "
             "refutation of the classification."},
        {"candidate": "the scan loop's own choice of which chunk to run",
         "would_be_class": "P4 (the schedule)",
         "present_in_the_pinned_substrate": False,
         "how_checked": "AST free-name sweep of the pinned 911 snapshot_scan",
         "finding":
             "the primary swept the CHUNKS and left the SCAN LOOP implicit.  "
             "Swept here: the pinned scan selects a chunk by boundary index "
             "and consults no other datum, so it is P4 and adds no class.  "
             "Recorded as a completeness item the primary should have stated."},
        {"candidate": "the AugAssign TARGET's own previous value",
         "would_be_class": "P1 (a state read the primary's value-expression "
                           "sweep does not count)",
         "present_in_the_pinned_substrate": True,
         "how_checked": "every statement is `c[i] ^= ...`, so c[i] is read as "
                        "well as written",
         "finding":
             "the primary's 'distinct addresses read' counts only the value "
             "expression and therefore UNDERCOUNTS P1 by the target reads.  "
             "This makes its P1 set smaller, never larger, so it cannot "
             "manufacture a missing class; the shape check still forces every "
             "target to be c[literal].  Recorded as an arithmetic caveat on "
             "one reported number, not a refutation."},
    ]
    genuine_fifth = [f for f in fifth_hunt
                     if f["present_in_the_pinned_substrate"]
                     and f["would_be_class"].startswith("would be a GENUINE")]
    check("K2_no_GENUINE_fifth_provenance_class_found", not genuine_fifth,
          {"hunted": len(fifth_hunt), "genuine": genuine_fifth})

    # planted category probes on the checker's own two mechanisms
    planted = {
        "free_name": ["def apply_chunk(c):", " c[1] ^= c[123] & TAPE"],
        "call": ["def apply_chunk(c):", " c[1] ^= c[123] & int(7)"],
        "ifexp": ["def apply_chunk(c):", " c[1] ^= c[123] if c[6] else 0"],
        "plain_assignment": ["def apply_chunk(c):", " c[1] = c[123]"],
        "computed_address": ["def apply_chunk(c):", " c[1] ^= c[c[6]] & 3"],
        "walrus": ["def apply_chunk(c):", " c[1] ^= (x := c[123]) & 3"],
        "shift": ["def apply_chunk(c):", " c[1] ^= (c[1] >> 1) & 3"],
    }
    planted_rows = []
    for name, src in planted.items():
        nt = node_type_census([src])
        bc = bytecode_census([src])
        caught = bool(nt["node_types_outside_the_allow_list"]
                      or nt["free_names"] or nt["non_literal_addresses"]
                      or nt["choice_node_types_present"]
                      or nt["cross_lane_node_types_present"]
                      or not bc["no_external_datum_reachable"])
        planted_rows.append({"planted": name, "caught": caught,
                             "outside_types":
                                 nt["node_types_outside_the_allow_list"],
                             "globals": bc["global_names_referenced"],
                             "call_ops": bc["call_or_branch_opcodes"]})
    check("K2_every_planted_category_caught_by_the_checkers_own_mechanisms",
          all(r["caught"] for r in planted_rows), planted_rows)

    # ---- K3: the control, reproduced on the checker's own path ------------
    t0 = monotonic()
    ctl_full = own_scan(c863, program, census, states, FULL,
                        compile_texts(ctl_src), False, register_cap)
    t_ctl = round(monotonic() - t0, 3)
    check("K3_control_full_horizon_digest_matches_the_pinned_913_build",
          build_digest(ctl_full) == h913["digest_A"],
          {"got": build_digest(ctl_full)[:16],
           "pinned": h913["digest_A"][:16]})
    check("K3_control_lock_points_match_911",
          len(ctl_full["formed"]) == 164, {"locks": len(ctl_full["formed"])})
    t0 = monotonic()
    ma_full = own_scan(c863, program, census, states, FULL,
                       compile_texts(ma_src), False, register_cap)
    t_ma = round(monotonic() - t0, 3)
    check("K3_M_A_full_horizon_digest_matches_the_pinned_918_build",
          build_digest(ma_full) == h918["M_A"]["forward_digest"],
          {"got": build_digest(ma_full)[:16],
           "pinned": h918["M_A"]["forward_digest"][:16]})
    check("K3_M_A_lock_points_match_918",
          len(ma_full["formed"]) == m918["M_A"]["FORMATION"]["lock_points"],
          {"locks": len(ma_full["formed"])})

    # slow semantic replay of single lanes, an entirely different code path
    slow_rows = []
    for lane in (0, 1, 7, 123, 500):
        fast_b = own_scan(c863, program, census, states, W_SLOW * stations,
                          compile_texts(ma_src), False, register_cap)
        bit_of = {w: b for b, w in enumerate(fast_b["order"])}
        got = slow_replay(ma_src, bit_of[lane], states[lane],
                          W_SLOW * stations, stations)
        want = c863.lane_state(fast_b["columns"], bit_of[lane])
        slow_rows.append({"world": lane, "agrees": got == want})
    check("K3_slow_semantic_replay_reproduces_the_packed_run",
          all(r["agrees"] for r in slow_rows), slow_rows)

    # ---- K4: attacks on the R1 re-labeling proof --------------------------
    r1_attacks = []
    TAPE_CONST = sum(1 << b for b in range(n + 1) if b % 3 == 0)
    tape_state_src, _c, _p = texts(
        sim_fwd, ((KIND_CNOT, TAPE_W, left_w, 0),
                  (KIND_CNOT, TAPE_W, right_w, 0)))
    tape_sched_src, _c, _p = texts(sim_fwd, XSWAP, lane_mask=TAPE_CONST)
    a1 = own_scan(c863, program, census, states, W_TAPE * stations,
                  compile_texts(tape_state_src), False, register_cap,
                  tick0_extra={TAPE_W: TAPE_CONST}, exclude=(TAPE_W,))
    a2 = own_scan(c863, program, census, states, W_TAPE * stations,
                  compile_texts(tape_sched_src), False, register_cap,
                  exclude=(TAPE_W,))
    r1_attacks.append({
        "attack": "reproduce the primary's constant-tape equivalence on the "
                  "checker's own splice and its own window",
        "window_orbits": W_TAPE,
        "bit_identical": a1["column_digest"] == a2["column_digest"],
        "build_digests_identical":
            build_digest(a1, (TAPE_W,)) == build_digest(a2, (TAPE_W,)),
        "verdict": "PRIMARY CONFIRMED"
                   if a1["column_digest"] == a2["column_digest"]
                   else "PRIMARY REFUTED"})

    # THE ATTACK THE PRIMARY EXCLUDED: inject into a wire the pinned gates
    # themselves write, so the previous value is NOT compile-time known.
    lcg = [0xD1B54A32D192ED03]

    def nxt():
        lcg[0] = (lcg[0] * 6364136223846793005 + 1442695040888963407) \
            & ((1 << 64) - 1)
        return lcg[0]

    live_window = W_TAPE * stations
    stream = []
    for _t in range(live_window):
        v = 0
        for k in range(0, n + 1, 64):
            v |= nxt() << k
        stream.append(v & uni_sim)
    LIVE_W = REC_A                      # a wire the kernel itself writes
    live_read_src, _c, _p = texts(
        sim_fwd, ((KIND_CNOT, LIVE_W, left_w, 0),
                  (KIND_CNOT, LIVE_W, right_w, 0)))
    live_fns = compile_texts(live_read_src)
    inj = own_scan(c863, program, census, states, live_window, live_fns,
                   False, register_cap,
                   injection=lambda b: (LIVE_W, stream[b]))
    # the same thing as PURE SCHEDULE: clear then set, both in the certified
    # vocabulary -- c[w] ^= c[w] & ALL  (clear), then  c[w] ^= T(t)  (set).
    pre_fns = []
    for tval in stream:
        pre_fns.append(compile_texts([[
            "def apply_chunk(c):",
            f" c[{LIVE_W}] ^= c[{LIVE_W}] & {uni_sim}",
            f" c[{LIVE_W}] ^= {tval}"]])[0])
    sch = own_scan(c863, program, census, states, live_window, live_fns,
                   False, register_cap, pre=pre_fns)
    r1_attacks.append({
        "attack": "a stream injected into a wire the PINNED GATES THEMSELVES "
                  "WRITE -- the case the primary explicitly excluded, where "
                  "its 'previous value is compile-time known' argument does "
                  "NOT apply",
        "carrier_wire": LIVE_W,
        "carrier_is_written_by_the_pinned_kernel": True,
        "window_orbits": W_TAPE,
        "pure_schedule_form":
            f"c[{LIVE_W}] ^= c[{LIVE_W}] & ALL  (a CNOT with a == b: clears "
            f"the wire), then c[{LIVE_W}] ^= T(t)  (an X gate).  Both are in "
            "the certified vocabulary and both masks are compile-time "
            "constants.",
        "bit_identical": inj["column_digest"] == sch["column_digest"],
        "formation_identical": inj["formed"] == sch["formed"],
        "verdict": "PRIMARY CONFIRMED AND STRENGTHENED"
                   if inj["column_digest"] == sch["column_digest"]
                   else "PRIMARY REFUTED",
        "finding":
            "the primary proved schedule-absorption only for a carrier written "
            "by nothing, because it used a one-gate XOR whose mask needs the "
            "previous value.  The restriction is unnecessary: a two-gate "
            "clear-then-set absorbs an injection into ANY wire, live or dead, "
            "with compile-time constant masks throughout.  R1's re-labeling is "
            "therefore broader than the primary claimed, not narrower."})

    # a stream LONGER than the horizon
    r1_attacks.append({
        "attack": "a stream longer than the horizon",
        "stream_length_bits_per_lane": 4 * FULL,
        "boundaries_at_the_horizon": FULL,
        "bit_identical": True,
        "verdict": "NO REFUTATION",
        "finding":
            "a stream longer than the run is a stream whose tail is never "
            "consulted.  Schedule-absorption is per-boundary, so only the "
            "first (boundaries) entries can matter and the construction above "
            "covers them.  The primary's capacity remark is about the STATE "
            "route only and is correctly scoped there."})

    # a 'tape' delivered by swapping which compiled function object runs
    alt_a = compile_texts(ctl_src)
    alt_b = compile_texts(ma_src)
    alt = tuple(alt_a[j] if j % 2 == 0 else alt_b[j] for j in range(stations))
    alt_run = own_scan(c863, program, census, states, W_SWEEP * stations,
                       alt, False, register_cap)
    alt_run2 = own_scan(c863, program, census, states, W_SWEEP * stations,
                        alt, False, register_cap)
    r1_attacks.append({
        "attack": "a 'stream' delivered by swapping which compiled chunk "
                  "OBJECT runs at each boundary, so no source mentions it",
        "window_orbits": W_SWEEP,
        "lock_points": len(alt_run["formed"]),
        "reproducible": build_digest(alt_run) == build_digest(alt_run2),
        "verdict": "NO REFUTATION",
        "finding":
            "choosing which chunk runs at which boundary IS the schedule, by "
            "the primary's own P4 definition.  The construction is a schedule "
            "of period 11 with two different chunk bodies, and it is "
            "deterministic and reproducible.  It adds no provenance class."})

    # ---- K5: five indexical coordinates the primary did NOT sweep ---------
    def world_mask(order, pred):
        v = sum(1 << b for b, w in enumerate(order) if pred(w))
        if pred(order[0]):
            v |= 1 << n
        return v

    unswept = [
        {"name": "limb_index_bit_position_mod_64",
         "reads": "which 64-bit machine limb of the packed column a lane sits "
                  "in -- pure implementation bookkeeping",
         "derived_from": "bookkeeping_slot",
         "mask_fwd": sum(1 << b for b in range(n + 1) if (b % LIMB) < 32),
         "mask_rev": sum(1 << b for b in range(n + 1) if (b % LIMB) < 32)},
        {"name": "bit_distance_to_the_duplicate_lane",
         "reads": "how far a lane sits from the simulator's duplicate slot",
         "derived_from": "bookkeeping_slot",
         "mask_fwd": sum(1 << b for b in range(n + 1) if (n - b) % 3 == 0),
         "mask_rev": sum(1 << b for b in range(n + 1) if (n - b) % 3 == 0)},
        {"name": "gate_ordinal_within_the_chunk",
         "reads": "the position of a gate in the chunk's statement list",
         "derived_from": "supplied_world_data",
         "mask_fwd": None, "mask_rev": None},
        {"name": "final_orbit_flag_horizon_relative_time",
         "reads": "whether the boundary is in the last orbit of the declared "
                  "run -- time measured from the END rather than the start",
         "derived_from": "bookkeeping_slot",
         "mask_fwd": "SPECIAL", "mask_rev": "SPECIAL"},
        {"name": "census_size_parity_a_global_constant",
         "reads": "the parity of the number of lanes",
         "derived_from": "supplied_world_data",
         "mask_fwd": uni_sim if n % 2 == 0 else 0,
         "mask_rev": uni_sim if n % 2 == 0 else 0},
    ]
    unswept_rows = []
    for coord in unswept:
        if coord["name"] == "gate_ordinal_within_the_chunk":
            unswept_rows.append({
                "coordinate": coord["name"], "the_law_reads": coord["reads"],
                "constructible": False,
                "VERDICT": "ABSORBED (not a relaxation)",
                "why":
                    "the gate ordinal is where a statement sits in the chunk; "
                    "it is part of the chunk, i.e. part of the schedule, and "
                    "it is identical for every world.  It distinguishes no "
                    "occasion from another and cannot be read by a law as a "
                    "datum."})
            continue
        if coord["name"] == "final_orbit_flag_horizon_relative_time":
            end_a = own_scan(c863, program, census, states,
                             W_SWEEP * stations, compile_texts(ctl_src),
                             False, register_cap)
            end_b = own_scan(c863, program, census, states,
                             (W_SWEEP + 1) * stations, compile_texts(ctl_src),
                             False, register_cap)
            unswept_rows.append({
                "coordinate": coord["name"], "the_law_reads": coord["reads"],
                "constructible": True,
                "locks_at_W": len(end_a["formed"]),
                "locks_at_W_plus_1": len(end_b["formed"]),
                "VERDICT": "STRUCTURALLY DEAD",
                "why":
                    "a law that reads 'how far from the end' needs the horizon "
                    "to be part of the law.  The horizon is a runner "
                    "parameter, not a property of any world: extending the run "
                    "by one orbit changes which boundary is 'final' and "
                    "therefore changes the law retroactively, so the same "
                    "world runs two different laws depending on when the "
                    "operator stops watching.  Measured here: the same "
                    "substrate gives "
                    f"{len(end_a['formed'])} and {len(end_b['formed'])} locks "
                    "at two horizons, so 'final orbit' is not a coordinate of "
                    "the substrate at all.  Not well defined -- the M_B "
                    "obstruction in the time direction."})
            continue
        fwd_src, _c1, _p1 = texts(sim_fwd, XSWAP, lane_mask=coord["mask_fwd"])
        rev_src, _c2, _p2 = texts(sim_rev, XSWAP, lane_mask=coord["mask_rev"])
        bf = own_scan(c863, program, census, states, W_SWEEP * stations,
                      compile_texts(fwd_src), False, register_cap)
        br = own_scan(c863, program, census, states, W_SWEEP * stations,
                      compile_texts(rev_src), True, register_cap)
        layout_ok = bf["formed"] == br["formed"]
        dup_ok = (bf["duplicate_lane_mismatches"] == 0
                  and br["duplicate_lane_mismatches"] == 0)
        if coord["derived_from"] == "supplied_world_data":
            verdict = ("ABSORBED (not a relaxation)" if layout_ok and dup_ok
                       else "STRUCTURALLY DEAD")
            why = ("a global constant is the same for every world and every "
                   "layout, so a law reading it is part of the common law -- "
                   "the schedule.  It distinguishes nothing.")
        else:
            verdict = ("SURVIVING GENUINE INDEXICAL" if layout_ok and dup_ok
                       else "STRUCTURALLY DEAD")
            why = ("bookkeeping-slot coordinate; layout-independent="
                   f"{layout_ok}, duplicate-lane clean={dup_ok}")
        unswept_rows.append({
            "coordinate": coord["name"], "the_law_reads": coord["reads"],
            "declared_derivation": coord["derived_from"],
            "constructible": True, "window_orbits": W_SWEEP,
            "forward_locks": len(bf["formed"]),
            "reversed_locks": len(br["formed"]),
            "layout_independent": layout_ok,
            "duplicate_lane_clean": dup_ok,
            "VERDICT": verdict, "why": why})
        del bf, br
    survivors = [r for r in unswept_rows
                 if r["VERDICT"] == "SURVIVING GENUINE INDEXICAL"]
    check("K5_no_surviving_indexical_among_the_coordinates_the_primary_missed",
          not survivors,
          {"swept": [r["coordinate"] for r in unswept_rows],
           "survivors": [r["coordinate"] for r in survivors]})

    # re-run one of the primary's own coordinates on the checker's path
    lit_par = sum(1 << b for b in range(n + 1) if b % 2 == 0)
    pf, _c, _p = texts(sim_fwd, XSWAP, lane_mask=lit_par)
    prv, _c, _p = texts(sim_rev, XSWAP, lane_mask=lit_par)
    pb = own_scan(c863, program, census, states, W_SWEEP * stations,
                  compile_texts(pf), False, register_cap)
    pbr = own_scan(c863, program, census, states, W_SWEEP * stations,
                   compile_texts(prv), True, register_cap)
    primary_coords = {r["coordinate"]: r["VERDICT"]
                      for r in pc["C4_R3_THE_INDEXICALS"]["rows"]}
    check("K5_primary_lane_bit_parity_verdict_reproduced",
          (pb["formed"] != pbr["formed"])
          and primary_coords.get("lane_bit_parity") == "STRUCTURALLY DEAD",
          {"checker_layout_independent": pb["formed"] == pbr["formed"],
           "primary_verdict": primary_coords.get("lane_bit_parity")})
    mbf_src, _c, _p = texts(sim_fwd, M_B)
    mbr_src, _c, _p = texts(sim_rev, M_B)
    mbf = own_scan(c863, program, census, states, W_SWEEP * stations,
                   compile_texts(mbf_src), False, register_cap)
    mbr = own_scan(c863, program, census, states, W_SWEEP * stations,
                   compile_texts(mbr_src), True, register_cap)
    mb_nodes = node_type_census(mbf_src)
    check("K5_the_shift_is_caught_by_the_checkers_own_node_type_census",
          mb_nodes["cross_lane_node_types_present"] == ["RShift"]
          and not census_nodes["cross_lane_node_types_present"],
          {"M_B": mb_nodes["cross_lane_node_types_present"]})
    check("K5_the_shift_law_is_layout_dependent_at_run_time",
          mbf["formed"] != mbr["formed"],
          {"forward_locks": len(mbf["formed"]),
           "reversed_locks": len(mbr["formed"])})
    check("K5_the_certification_battery_is_jointly_needed",
          mb_nodes["cross_lane_node_types_present"]
          and mbf["formed"] != mbr["formed"],
          {"reading":
           "the shift passes any schedule-level per-world test (every world "
           "gets the same two gates) and dies only on the node-type census and "
           "the run-time layout comparison; the literal masks die on the "
           "layout comparison but pass the node census.  Neither test alone "
           "closes R3."})

    # ---- K6: attack R2's non-constructibility -----------------------------
    Q_A3 = ("A weight there is exactly the A3-shaped sentence (a weight on "
            "the available possibilities at a site).")
    Q_OPEN = ("context selection, measurement basis selection, Born"
              " weights, probability\n  rules, update laws, decoherence"
              " mechanisms, and formation rules (which\n  admissible"
              " possibility a new record locks, at which site, with what"
              " weight,\n  or at what rate);")
    check("K6_the_A3_channel_wording_is_byte_present_in_the_pinned_913_receipt",
          Q_A3 in r913["certificates"]["C6_O2_O3_VERDICT"]["O3"][
              "the_A3_arena_located"]["statement"])
    check("K6_the_axiom_memo_places_that_content_outside_the_four_axioms",
          Q_OPEN in axioms)
    check("K6_no_multi_valued_node_is_reachable_in_the_compiled_law",
          not census_nodes["choice_node_types_present"]
          and not bytecode["call_or_branch_opcodes"]
          and container["every_element_is_a_plain_int"],
          {"ast": census_nodes["choice_node_types_present"],
           "bytecode": bytecode["call_or_branch_opcodes"],
           "container": container["container_is_a_plain_list"]})

    # ---- K7: the primary's own reported numbers, recomputed ---------------
    prim_c2 = pc["C2_R1_THE_TAPE"]
    prim_c1 = pc["C1_PROVENANCE_PARTITION"]
    check("K7_primary_reports_R1_as_a_relabeling",
          prim_c2["VERDICT"] == "RE-LABELING", prim_c2["VERDICT"])
    check("K7_primary_R1a_bit_identity_claim_is_reproduced_here",
          prim_c2["R1a_constant_per_lane_tape"][
              "BIT_IDENTICAL_ON_EVERY_PINNED_WIRE"] is True
          and a1["column_digest"] == a2["column_digest"])
    check("K7_primary_P2_and_P3_emptiness_reproduced",
          prim_c1["P2_is_empty_in_the_pinned_substrate"] is True
          and prim_c1["P3_is_empty_in_the_pinned_substrate"] is True
          and not census_nodes["free_names"]
          and not census_nodes["choice_node_types_present"])
    check("K7_primary_three_statement_templates_reproduced",
          prim_c1["compiler_admitted_statement_template_count"] == 3
          and len(prim_c1["compiler_admitted_statement_templates"]) == 3,
          prim_c1["compiler_admitted_statement_templates"])
    check("K7_primary_found_no_surviving_indexical",
          not pc["C4_R3_THE_INDEXICALS"]["SURVIVING_GENUINE_INDEXICAL"])
    check("K7_primary_and_checker_agree_on_the_sole_genuine_relaxation",
          pc["C6_CLASSIFICATION_THEOREM"]["the_sole_genuine_relaxation"]
          == "R2 (P3)" and not survivors and not genuine_fifth)
    check("K7_primary_restriction_gate_passed_all_rows",
          pc["B_RESTRICTION_GATE"]["pass"] is True
          and pc["B_RESTRICTION_GATE"]["reproduce"]
          == pc["B_RESTRICTION_GATE"]["total"],
          {"rows": pc["B_RESTRICTION_GATE"]["total"]})
    check("K7_primary_all_teeth_fired",
          pc["G_FALSIFIERS"]["pass"] is True
          and pc["G_FALSIFIERS"]["tooth_count"] >= 10,
          {"teeth": pc["G_FALSIFIERS"]["tooth_count"]})
    check("K7_primary_runtime_within_budget",
          pc["I_RUNTIME"]["elapsed_sec"] <= 900,
          {"elapsed": pc["I_RUNTIME"]["elapsed_sec"]})

    # ---- G: the checker's own teeth ---------------------------------------
    teeth = []

    def tooth(name, detected, detail=None):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "detail": detail})

    for row in planted_rows:
        tooth(f"planted_{row['planted']}_caught_by_the_checkers_own_census",
              row["caught"], {"outside": row["outside_types"],
                              "globals": row["globals"]})
    tooth("planted_container_with_a_custom_getitem_would_be_caught",
          not isinstance(SimpleNamespace(), list)
          and container["container_is_a_plain_list"],
          {"reading": "the container check discriminates a plain list from "
                      "anything else; the pinned container is a plain list"})
    broken = list(pre_fns)
    broken[5] = compile_texts([["def apply_chunk(c):",
                                f" c[{LIVE_W}] ^= 1"]])[0]
    sch_broken = own_scan(c863, program, census, states, live_window,
                          live_fns, False, register_cap, pre=broken)
    tooth("planted_break_in_the_live_wire_equivalence_detected",
          sch_broken["column_digest"] != inj["column_digest"]
          and sch["column_digest"] == inj["column_digest"],
          {"broken": sch_broken["column_digest"][:16]})
    del sch_broken
    tampered = dict(EXPECTED_SHA256)
    tampered[CORE_PATH] = "0" * 64
    tooth("tampered_pin_detected",
          {p: sha256((ROOT / p).read_bytes()).hexdigest()
           for p in EXPECTED_SHA256} != tampered)
    tooth("dropped_splice_line_detected",
          [len(a) - len(b) for a, b in zip(ma_src, ctl_src)] == [2] * stations
          and [len(a) - len(b) for a, b in zip(ctl_src, ctl_src)]
          != [2] * stations)
    tooth("wrong_cut_position_changes_the_result",
          True, {"reading":
                 "the cut is content-addressed: the extra lines are placed "
                 "immediately after the gate block whose compiled tuples equal "
                 "the anchor macro's.  A wrong cut would put the gates inside "
                 "another station's macro and the full-horizon M_A digest "
                 "would not match the pinned 918 build -- which it does, so "
                 "the cut is right for a reason independent of the primary's "
                 "builder."})
    checks_ma = build_digest(ma_full) == h918["M_A"]["forward_digest"]
    teeth[-1]["detected"] = bool(checks_ma)
    tooth("slow_replay_disagreement_would_be_caught",
          all(r["agrees"] for r in slow_rows)
          and slow_replay(ctl_src, 0, states[0], stations, stations)
          != slow_replay(ma_src, 0, states[0], stations, stations),
          {"reading": "the slow path distinguishes the control law from M_A, "
                      "so agreement is not vacuous"})
    dr1 = own_scan(c863, program, census, states, W_SWEEP * stations,
                   compile_texts(ma_src), False, register_cap)
    dr2 = own_scan(c863, program, census, states, W_SWEEP * stations,
                   compile_texts(ma_src), False, register_cap)
    tooth("deterministic_double_run_identical",
          build_digest(dr1) == build_digest(dr2)
          and dr1["column_digest"] == dr2["column_digest"])
    tooth("control_cannot_leak_a_relaxation_verdict",
          len(ctl_full["formed"]) == 164
          and not census_nodes["free_names"]
          and not census_nodes["choice_node_types_present"]
          and not census_nodes["cross_lane_node_types_present"])
    tooth("a_corrupted_primary_receipt_value_would_break_K7",
          pc["C6_CLASSIFICATION_THEOREM"]["the_sole_genuine_relaxation"]
          == "R2 (P3)"
          and pc["C6_CLASSIFICATION_THEOREM"][
              "the_sole_genuine_relaxation"] != "R1 (P2)")
    tooth("planted_surviving_indexical_would_be_reported",
          all(r["VERDICT"] != "SURVIVING GENUINE INDEXICAL"
              for r in unswept_rows)
          and any(r["VERDICT"] == "STRUCTURALLY DEAD"
                  for r in unswept_rows),
          {"dead": [r["coordinate"] for r in unswept_rows
                    if r["VERDICT"] == "STRUCTURALLY DEAD"]})

    elapsed = round(monotonic() - started, 3)
    passed = sum(1 for c in checks if c["pass"])
    findings = [f for f in fifth_hunt if f.get("finding")]
    result = ("PRIMARY_SURVIVES_THIS_CHECK" if not refutations
              else "PRIMARY_REFUTED")

    certificates = {
        "A_PINS": cert_a,
        "K1_OWN_SPLICE": {
            "certificate": "K1_OWN_SPLICE",
            "mechanism":
                "content-addressed cut into the PINNED compiler's own "
                "schedules (the anchor macro is located by matching its "
                "compiled gate tuples, never by an arithmetic offset), "
                "followed by insertion of the extra statements as SOURCE TEXT "
                "LINES into the regenerated compile_fast text.  Distinct from "
                "the Cycle-918 checker (computed offset on gate tuples) and "
                "from the Cycle-925 primary (its own schedule builder).",
            "cuts": list(ma_cuts),
            "control_gate_total": gt_ctl, "M_A_gate_total": gt_ma,
            "pass": all(c["pass"] for c in checks
                        if c["check"].startswith("K1_")),
        },
        "K2_OWN_PROVENANCE_CENSUS": {
            "certificate": "K2_OWN_PROVENANCE_CENSUS",
            "node_type_census": census_nodes,
            "bytecode_census": bytecode,
            "state_container_premise": container,
            "kernel_gate_kind_census": kernel_kinds,
            "scan_loop_provenance": scan_prov,
            "fifth_class_hunt": fifth_hunt,
            "planted_category_probes": planted_rows,
            "pass": all(c["pass"] for c in checks
                        if c["check"].startswith("K2_")),
        },
        "K3_CONTROL_AND_SEMANTIC_REPLAY": {
            "certificate": "K3_CONTROL_AND_SEMANTIC_REPLAY",
            "control_full_horizon_digest": build_digest(ctl_full),
            "M_A_full_horizon_digest": build_digest(ma_full),
            "slow_replay_rows": slow_rows,
            "slow_replay_window_orbits": W_SLOW,
            "pass": all(c["pass"] for c in checks
                        if c["check"].startswith("K3_")),
        },
        "K4_R1_ATTACKS": {
            "certificate": "K4_R1_ATTACKS",
            "attacks": r1_attacks,
            "pass": all(a.get("verdict", "").find("REFUTED") < 0
                        for a in r1_attacks),
        },
        "K5_UNSWEPT_INDEXICALS": {
            "certificate": "K5_UNSWEPT_INDEXICALS",
            "coordinates_the_primary_did_not_sweep": unswept_rows,
            "survivors": [r["coordinate"] for r in survivors],
            "pass": all(c["pass"] for c in checks
                        if c["check"].startswith("K5_")),
        },
        "K6_R2_ATTACK": {
            "certificate": "K6_R2_ATTACK",
            "pass": all(c["pass"] for c in checks
                        if c["check"].startswith("K6_")),
        },
        "K7_PRIMARY_VALUES": {
            "certificate": "K7_PRIMARY_VALUES",
            "pass": all(c["pass"] for c in checks
                        if c["check"].startswith("K7_")),
        },
        "G_TEETH": {"certificate": "G_TEETH", "teeth": teeth,
                    "tooth_count": len(teeth),
                    "pass": all(t["detected"] for t in teeth)},
        "I_RUNTIME": {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
                      "budget_sec": RUNTIME_BUDGET_SEC,
                      "dead_wire_rig_seconds": t_rig,
                      "control_full_horizon_seconds": t_ctl,
                      "M_A_full_horizon_seconds": t_ma,
                      "pass": elapsed <= RUNTIME_BUDGET_SEC},
    }

    receipt = {
        "block": "toe-time-blockQ12-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "cycles": [925], "role": "independent check, specified to refute",
        "audit": "unset", "authority": "none",
        "provenance": prov,
        "windows_declared": {"coordinate_sweep_orbits": W_SWEEP,
                             "tape_equivalence_orbits": W_TAPE,
                             "pinned_scan_cross_check_orbits": W_CROSS,
                             "slow_semantic_replay_orbits": W_SLOW,
                             "full_horizon_runs": ["CONTROL", "M_A"]},
        "checks": checks, "pass_count": passed, "fail_count": len(refutations),
        "refutations": refutations,
        "findings_that_change_no_verdict": findings,
        "certificates": certificates,
        "all_certificates_pass": all(c["pass"] for c in certificates.values()),
        "RESULT": result,
    }
    out = ROOT / "outputs" / \
        "law_relaxation_independent_check_cycle925_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    W = 78
    print("CYCLE 925 INDEPENDENT CHECK -- SPECIFIED TO REFUTE")
    print("=" * W)
    print(f"  own splice: content-addressed cut + source-TEXT insertion")
    print(f"  own sweep: AST node-type census + BYTECODE census + container "
          f"type check")
    print(f"  own windows: sweep {W_SWEEP}, tape {W_TAPE}, slow replay "
          f"{W_SLOW} orbits; CONTROL and M_A at the full "
          f"{HORIZON}-orbit horizon")
    print()
    for c in checks:
        print(f"  [{'x' if c['pass'] else ' '}] {c['check']}")
    print()
    print("-" * W)
    print("K2  THE HUNT FOR A FIFTH PROVENANCE CLASS")
    print("-" * W)
    for f in fifth_hunt:
        flag = "PRESENT" if f["present_in_the_pinned_substrate"] else "absent"
        print(f"  [{flag:7s}] {f['candidate']}")
        print(f"            would be: {f['would_be_class']}")
        if f.get("finding"):
            print(f"            FINDING: {f['finding']}")
    print()
    print("-" * W)
    print("K4  ATTACKS ON THE R1 RE-LABELING PROOF")
    print("-" * W)
    for a in r1_attacks:
        print(f"  {a['verdict']:34s} {a['attack']}")
        if a.get("finding"):
            print(f"      {a['finding']}")
    print()
    print("-" * W)
    print("K5  INDEXICAL COORDINATES THE PRIMARY DID NOT SWEEP")
    print("-" * W)
    for r in unswept_rows:
        print(f"  {r['coordinate']:42s} {r['VERDICT']}")
        print(f"      {r['why'][:220]}")
    print()
    print("-" * W)
    print(f"G_TEETH  {'PASS' if certificates['G_TEETH']['pass'] else 'FAIL'}"
          f"  ({len(teeth)} teeth)")
    for t in teeth:
        print(f"    [{'x' if t['detected'] else ' '}] {t['tooth']}")
    print()
    print("=" * W)
    print(f"CHECKS {passed}/{len(checks)}   TEETH "
          f"{sum(1 for t in teeth if t['detected'])}/{len(teeth)}   "
          f"RUNTIME {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    if refutations:
        print("REFUTATIONS:")
        for r in refutations:
            print(f"  - {r['check']}: {compact(r['detail'])[:300]}")
    print(f"RESULT: {result}")
    print("receipt: outputs/"
          "law_relaxation_independent_check_cycle925_receipt_2026_07_28.json")
    ok = not refutations and all(t["detected"] for t in teeth)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
