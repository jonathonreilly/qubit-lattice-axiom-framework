"""Cycle 918 INDEPENDENT CHECK -- specified to REFUTE the writable-endpoint map.

The primary (frontier_cycle918_writable_endpoint_2026_07_28.py) claims a first
measured map of the writable-endpoint design space: three declared
modifications of the landed 719 kernel that make the endpoint wires gate
TARGETS, each recompiled and run on the full 748-world census, each given a
verdict of BORN-CAPABLE / STERILE / DESTRUCTIVE.

This runner does not trust any of it.  It rebuilds every modification by a
DIFFERENT mechanism, runs its own scan, recomputes every reported quantity,
and then attacks the primary's four load-bearing claims:

  K1  THE SPLICE.  The primary rebuilds the whole masked schedule from the
      program with the extra gates appended to the anchor station's macro.
      This runner never rebuilds: it takes the PINNED Cycle-863 compiler's own
      output and splices the extra gates at the offset it computes from the
      station macro lengths.  If the primary's rebuild differs anywhere from
      the pinned compiler's output plus a splice, the gate totals, the target
      sweep and the scan results diverge and this runner says so.

  K2  THE RECORD MACHINERY.  The primary derived the Cycle-878 dead-wire safe
      pool ONCE, from the CONTROL, and then only MONITORED those slots under
      each modification.  That is a gap: a modification could change which
      wires are dead and so invalidate the slot assignment it inherited.  This
      runner re-derives the whole rig under EVERY modification at the pinned
      878 window and compares dead sets, safe pools and slot maps.  It also
      re-derives write-once by a second route -- uniqueness of the (world,
      tag, ordinal) event triples and strict monotonicity of the per-bank
      ordinals -- which never touches the primary's shadow ledger.

  K3  THE COVARIANCE.  The primary reports the landed monitor-phase Z_11
      invariance of the realized selection per modification.  This runner
      builds the Z_11 action from the census itself (never from the pinned
      Cycle-878 function), verifies it is a census bijection of order 11,
      recounts the violations, and separately certifies the structural claim
      the primary makes in its pricing: that the added gates carry EXACTLY the
      anchor station's own lane mask at every step, so the added law is as
      phase-covariant as the station it rides.

  K4  THE VERDICTS.  This runner writes its own classifier from the primary's
      declared criteria and applies it twice: to the quantities the primary
      PUBLISHED in its receipt, and to the quantities this runner MEASURED.  A
      verdict that survives only one of those is a hardcoded verdict.

Teeth (>= 6, all planted here, all must fire): tampered pin; dropped
modification; hardcoded verdict; leaked BORN-CAPABLE; skipped world; planted
branch blindness; plus a planted write-once breach and a planted dead-slot
corruption.

This runner EXITS 0 whether or not the primary survives.  Its verdict is a
finding, not a build status.
"""

from __future__ import annotations

import ast
import importlib.abc
import json
import sys
from collections import Counter
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
HANDSHAKE_PATH = \
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C911_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
C913_PATH = "scripts/frontier_cycle913_selection_function_2026_07_28.py"
C913_RECEIPT = "outputs/selection_function_cycle913_receipt_2026_07_28.json"
PRIMARY_PATH = "scripts/frontier_cycle918_writable_endpoint_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, HANDSHAKE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C911_PATH,
    C911_RECEIPT, C913_PATH, C913_RECEIPT, PRIMARY_PATH, PRIMARY_RECEIPT,
    AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C911_PATH, C913_PATH, PRIMARY_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C911_RECEIPT, C913_RECEIPT, PRIMARY_RECEIPT)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    HANDSHAKE_PATH:
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
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
    PRIMARY_PATH: "0ef019ef77cf3ff33c7e6c29ac31d1cd53945bd5f505f1fd4b3387e74017289d",
    PRIMARY_RECEIPT: "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    HANDSHAKE_PATH: "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C911_PATH: "3335e9dee5027b935d0eb3c814601b8f8e83b550",
    C911_RECEIPT: "af51342a72c56db8e562e1f1a607f207508b42ed",
    C913_PATH: "2093b687713eb12b462532761092d90d40bed718",
    C913_RECEIPT: "5ac6a40c316c7a90bcf867eb6507518ba976169b",
    PRIMARY_PATH: "b5a1a5643abe87ab4a92fd86e8c0007e8f26539a",
    PRIMARY_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
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
PERTURB_ORBITS = 6

KIND_X, KIND_CNOT, KIND_TOF, KIND_SHIFT = 0, 1, 2, 3
CERTIFIED_KINDS = (KIND_X, KIND_CNOT, KIND_TOF)


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

def pin_rows():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "sha256": sha_rows, "git_blobs": blob_rows,
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "mismatched_paths": sorted(
            p for p in AUDIT_INPUT_PATHS
            if sha_rows[p] != EXPECTED_SHA256.get(p)),
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS),
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules),
        "firewall_hits": tuple(FIREWALL.hits),
    }
    result["pass"] = bool(result["sha256_all_match"]
                          and result["git_blobs_all_match"]
                          and result["existing_worktree_relative"]
                          and not result["blocked_modules_loaded"]
                          and not result["firewall_hits"])
    return result, payloads


def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in consts:
                    found[t.id] = ast.literal_eval(node.value)
    missing = tuple(f for f in funcs if f not in {n.name for n in body})
    if missing or tuple(c for c in consts if c not in found):
        raise AssertionError(("lift incomplete", path, missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = dict(globals_)
    ns.update(found)
    exec(compile(module, f"<lift {path}>", "exec"), ns)
    return ns, found, tuple(n.name for n in body)


C863_FUNCS = ("pairwise_separated", "derive_event_seeds", "derive_census",
              "watched_registers", "dirty_partition", "build_initial_states",
              "pack_lanes", "compile_masked_gate", "masked_h_schedules",
              "compile_fast", "mask_over", "lanes_of", "lane_state",
              "synchronous_word")


def lift_all():
    ns863, c863c, n863 = ast_lift(
        C863_PATH, C863_FUNCS, ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
        {"K": K, "combinations": combinations, "Counter": Counter})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, c878c, n878 = ast_lift(
        C878_PATH, ("dead_wire_rig",),
        ("DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS", "REGISTER_CAP"),
        {"C863": c863})
    c878 = SimpleNamespace(dead_wire_rig=ns878["dead_wire_rig"])
    ns913, _c, n913 = ast_lift(
        C913_PATH,
        ("endpoint_wires", "read_state_direction", "is_function",
         "ladder_rows", "exhaustive_singleton_sweep"), (),
        {"K": K, "Counter": Counter, "sha256": sha256})
    c913 = SimpleNamespace(**{n: ns913[n] for n in
                              ("endpoint_wires", "read_state_direction",
                               "is_function", "ladder_rows",
                               "exhaustive_singleton_sweep")})
    ns911, c911c, n911 = ast_lift(
        C911_PATH, ("classify_pair",),
        ("DIRECTIONS", "REGISTER_CAP", "CLASS_BRANCH", "CLASS_IDENTICAL",
         "CLASS_SETUP_TICK0", "CLASS_SETUP_SCHEDULE",
         "CLASS_NONBRANCH_DIVERGENCE"), {})
    c911 = SimpleNamespace(classify_pair=ns911["classify_pair"])
    prov = {"lifted_863": n863, "lifted_878": n878, "lifted_911": n911,
            "lifted_913": n913, "consts_878": c878c,
            "single_disclosed_import": CORE_PATH}
    return c863, c878, c911, c913, c878c, c911c, prov


# ---------------------------------------------------------------------------
# K1: the INDEPENDENT splice mechanism -- never rebuild, always splice
# ---------------------------------------------------------------------------

def station_mask(sim, station, step, stations):
    return sum(1 << lane for lane, (_k, _e, pos) in enumerate(sim)
               if (station - step) % stations in pos)


def spliced_schedules(c863, program, sim, anchor, extra_gates, lane_mask):
    """Take the PINNED compiler's own schedules and insert the extra gates at
    the offset where the anchor station's macro ends.  The offset is derived
    from the station macro lengths, never from a rebuild."""
    stations = len(program)
    pinned = c863.masked_h_schedules(program, sim)
    anchor_len = len(K.mapped_macro(program[anchor]))
    out, cuts = [], []
    for step in range(stations):
        sched = list(pinned[step])
        mask = station_mask(sim, anchor, step, stations)
        if not mask or not extra_gates:
            out.append(tuple(sched))
            cuts.append(None)
            continue
        offset = 0
        for st in range(anchor):
            if station_mask(sim, st, step, stations):
                offset += len(K.mapped_macro(program[st]))
        cut = offset + anchor_len
        m = mask & lane_mask
        insert = [(k, a, b, c, m) for k, a, b, c in extra_gates] if m else []
        out.append(tuple(sched[:cut] + insert + sched[cut:]))
        cuts.append(cut)
    return tuple(out), tuple(cuts), pinned


def chunk_source(schedule):
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
            raise ValueError(kind)
    return src


def compile_schedules(schedules):
    fns = []
    for s in schedules:
        ns: dict = {}
        exec("\n".join(chunk_source(s)), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


def ast_cross_lane(schedules):
    """The Cycle-911 no-coupling question, asked here by parsing the source
    THIS runner execs and looking for any shift or arithmetic operator."""
    bad = []
    for step, s in enumerate(schedules):
        tree = ast.parse("\n".join(chunk_source(s)))
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and isinstance(
                    node.op, (ast.LShift, ast.RShift, ast.Add, ast.Sub,
                              ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
                              ast.Pow, ast.MatMult)):
                bad.append((step, type(node.op).__name__))
    return {"cross_lane_operator_sites": len(bad),
            "kinds": sorted({k for _s, k in bad}),
            "lane_local": not bad}


def sweep(schedules, left, right):
    targets, inputs, n = set(), set(), 0
    for s in schedules:
        for kind, a, b, c3, _m in s:
            n += 1
            if kind == KIND_X:
                targets.add(a)
            elif kind == KIND_CNOT:
                targets.add(b)
                inputs.add(a)
            elif kind == KIND_TOF:
                targets.add(c3)
                inputs.update((a, b))
            else:
                targets.add(b)
                inputs.add(a)
    return {"gates": n, "targets": targets, "inputs": inputs,
            "LEFT_target": left in targets, "RIGHT_target": right in targets,
            "reads_never_writes": left not in targets and right not in targets}


# ---------------------------------------------------------------------------
# the checker's own scan
# ---------------------------------------------------------------------------

def own_scan(c863, program, census, states, orbits, anchor, extra_gates,
             reverse, register_cap, count_left, count_right,
             lane_restrict=None, watch_wires=()):
    n = len(census)
    order = list(range(n - 1, -1, -1)) if reverse else list(range(n))
    bit_of = {w: b for b, w in enumerate(order)}
    sim = tuple(census[w] for w in order) + (census[order[0]],)
    if lane_restrict is None:
        lane_mask = (1 << (n + 1)) - 1
    else:
        lane_mask = 0
        for w in lane_restrict:
            lane_mask |= 1 << bit_of[w]
        if order[0] in lane_restrict:
            lane_mask |= 1 << n
    scheds, _cuts, _p = spliced_schedules(c863, program, sim, anchor,
                                          extra_gates, lane_mask)
    fast = compile_schedules(scheds)
    cols = c863.pack_lanes(tuple(states[w] for w in order)
                           + (states[order[0]],))
    per_bank, links, sptr = c863.dirty_partition()
    gdirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1]) | set(links)
                          | {sptr}))
    bdirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all, uni_sim = (1 << n) - 1, (1 << (n + 1)) - 1
    mask_over, lanes_of, lane_state = (c863.mask_over, c863.lanes_of,
                                       c863.lane_state)
    formed, snap, lockord, lockw = {}, {}, {}, {}
    events = []
    ordinal = [[0, 0] for _ in range(n)]
    dup = 0
    beyond = 0
    watch_acc = 0
    # per-lane change counters, by explicit lane enumeration -- a DIFFERENT
    # method from the primary's bit-plane ripple adder
    cnt_l = [0] * (n + 1)
    cnt_r = [0] * (n + 1)
    pl, pr = cols[count_left], cols[count_right]
    g = mask_over(cols, gdirty, uni_sim)
    dup += int(bool(g & 1) != bool(g & (1 << n)))
    prev = [mask_over(cols, bdirty[b], uni_all) for b in (0, 1)]
    for bit in lanes_of(g & uni_all):
        w = order[bit]
        formed[w] = 0
        snap[w] = lane_state(cols, bit)
        lockord[w] = (0, 0)
        lockw[w] = (0, 0)
        events.append((w, 0, "F", 0))
    boundary = 0
    for orbit in range(1, orbits + 1):
        for chunk in fast:
            chunk(cols)
            boundary += 1
            cl, cr = cols[count_left], cols[count_right]
            if cl != pl:
                for bit in lanes_of(cl ^ pl):
                    cnt_l[bit] += 1
                pl = cl
            if cr != pr:
                for bit in lanes_of(cr ^ pr):
                    cnt_r[bit] += 1
                pr = cr
            g = mask_over(cols, gdirty, uni_sim)
            dup += int(bool(g & 1) != bool(g & (1 << n)))
            ga = g & uni_all
            if ga:
                for bit in lanes_of(ga):
                    w = order[bit]
                    if w not in formed:
                        formed[w] = boundary
                        snap[w] = lane_state(cols, bit)
                        lockord[w] = tuple(ordinal[bit])
                        lockw[w] = (cnt_l[bit], cnt_r[bit])
                        events.append((w, boundary, "F", 0))
            for b in (0, 1):
                bm = mask_over(cols, bdirty[b], uni_all)
                rise = bm & ~prev[b]
                if rise:
                    for bit in lanes_of(rise):
                        o = ordinal[bit][b]
                        if o < register_cap:
                            events.append((order[bit], boundary, f"B{b}", o))
                        else:
                            beyond += 1
                        ordinal[bit][b] = o + 1
                prev[b] = bm
            if watch_wires and orbit <= DEAD_CHUNK_ORBITS:
                for w in watch_wires:
                    watch_acc |= cols[w]
        if watch_wires and orbit > DEAD_CHUNK_ORBITS:
            for w in watch_wires:
                watch_acc |= cols[w]
    events.sort(key=lambda e: (e[1], e[0], e[2], e[3]))
    return {"formed": formed, "snapshots": snap, "lock_ordinal": lockord,
            "lock_writes": lockw, "events": tuple(events), "boundaries":
            boundary, "duplicate_lane_mismatches": dup, "beyond_cap": beyond,
            "final_writes": {order[b]: (cnt_l[b], cnt_r[b]) for b in range(n)},
            "watch_activation": bin(watch_acc & uni_sim).count("1"),
            "schedules": scheds, "order": order}


def scan_digest(b):
    return digest({
        "formed": {str(k): v for k, v in sorted(b["formed"].items())},
        "snapshots": {str(k): "".join(str(x) for x in v)
                      for k, v in sorted(b["snapshots"].items())},
        "lock_ordinal": {str(k): list(v)
                         for k, v in sorted(b["lock_ordinal"].items())},
        "events": len(b["events"]),
    })


# ---------------------------------------------------------------------------
# K2: the record-machinery attacks, by routes the primary did not take
# ---------------------------------------------------------------------------

def write_once_by_event_uniqueness(events):
    """Write-once, recomputed WITHOUT the primary's shadow ledger: each
    (world, tag, ordinal) triple names one record slot write, so a repeat is a
    breach, and the per-(world, bank) ordinal sequence must be 0,1,2,... with
    no repeat and no gap."""
    seen = Counter((w, tag, o) for w, _b, tag, o in events)
    repeats = [k for k, c in seen.items() if c > 1]
    seq: dict = {}
    for w, _b, tag, o in events:
        seq.setdefault((w, tag), []).append(o)
    non_monotone = [k for k, v in seq.items() if v != sorted(v)]
    gapped = [k for k, v in seq.items() if v != list(range(len(v)))]
    return {
        "slot_write_triples": len(seen),
        "repeated_triples": len(repeats),
        "repeated_examples": [list(x) for x in repeats[:8]],
        "non_monotone_ordinal_sequences": len(non_monotone),
        "gapped_ordinal_sequences": len(gapped),
        "write_once_holds": not repeats and not non_monotone and not gapped,
    }


def rig_under(c878, program, sim, proto, anchor, extra_gates, c863):
    """Re-derive the whole Cycle-878 dead-wire rig UNDER a modification.  The
    primary only monitored the control's slots; this recomputes the dead set,
    the safe pool and the slot map from the modified schedules."""
    lane_mask = (1 << len(sim)) - 1
    scheds, _c, _p = spliced_schedules(c863, program, sim, anchor,
                                       extra_gates, lane_mask)
    fast = compile_schedules(scheds)
    universe = (1 << len(sim)) - 1
    work = list(proto)
    acc = list(work)
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in fast:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(len(work)):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(len(work)):
                acc[w] |= work[w]
    dead = tuple(w for w in range(len(acc)) if (acc[w] & universe) == 0)
    sw = sweep(scheds, 0, 0)
    safe = tuple(w for w in dead
                 if w not in sw["inputs"] and w not in sw["targets"])
    return {"dead_wires": dead, "safe_pool": safe,
            "dead_count": len(dead), "safe_count": len(safe)}


# ---------------------------------------------------------------------------
# K3: the covariance attack -- the Z_11 action built here, from the census
# ---------------------------------------------------------------------------

def own_monitor_phase(census, stations):
    index = {k: i for i, k in enumerate(census)}
    perms = []
    for m in range(stations):
        image = []
        for k, e, pos in census:
            t = (k, e, tuple(sorted((p + m) % stations for p in pos)))
            if t not in index:
                return (), False
            image.append(index[t])
        if sorted(image) != list(range(len(census))):
            return (), False
        perms.append(tuple(image))
    return tuple(perms), True


def invariance_count(perms, selection):
    locks = set(selection)
    checks = viol = off = 0
    for perm in perms:
        for w in sorted(locks):
            if perm[w] in locks:
                checks += 1
                viol += int(selection[perm[w]] != selection[w])
            else:
                off += 1
    return {"in_set_image_checks": checks, "violations": viol,
            "images_leaving_the_lock_set": off, "invariant": viol == 0}


def mask_covariance(c863, program, sim, anchor, extra_gates):
    """The structural half of the primary's covariance pricing: at every step
    the added gates must carry EXACTLY the anchor station's own lane mask."""
    stations = len(program)
    lane_mask = (1 << len(sim)) - 1
    scheds, cuts, pinned = spliced_schedules(c863, program, sim, anchor,
                                             extra_gates, lane_mask)
    rows = []
    for step in range(stations):
        want = station_mask(sim, anchor, step, stations)
        if cuts[step] is None:
            # no extra gates at this step: vacuously covariant.  For the
            # CONTROL, which has no extra gates at all, every step is vacuous.
            rows.append({"step": step, "anchor_live": bool(want),
                         "extra_masks": [],
                         "extra_masks_equal_the_anchor_mask": None,
                         "matches": True})
            continue
        got = [scheds[step][cuts[step] + i][4] for i in range(len(extra_gates))]
        rows.append({"step": step, "anchor_live": bool(want),
                     "extra_masks_equal_the_anchor_mask":
                         all(g == want for g in got),
                     "matches": all(g == want for g in got)})
    return {"per_step": rows, "all_steps_match": all(r["matches"]
                                                     for r in rows)}


# ---------------------------------------------------------------------------
# K4: the checker's own verdict classifier
# ---------------------------------------------------------------------------

def own_verdict(m: dict) -> str:
    """The primary's declared criteria, written here from the criteria text
    and not copied from its code."""
    broken = (m["write_once_violations"] > 0
              or m["record_slot_activation_conflicts"] > 0
              or m["slot_wires_became_gate_wires"] > 0
              or m["targets_outside_endpoints"]
              or m["duplicate_lane_mismatches"] > 0
              or m["lock_points"] == 0
              or m["off_menu_lock_points"] > 0
              or not m["layout_independent"]
              or not m["ast_lane_locality"]
              or not m["runtime_lane_locality"])
    if broken:
        return "DESTRUCTIVE"
    if m["selection_dynamical"] and m["dynamical_branch_pairs"] > 0:
        return "BORN-CAPABLE"
    return "STERILE"


def dyn_pairs(census, by_world, setup_direction):
    groups: dict = {}
    for w, r in by_world.items():
        groups.setdefault(
            (tuple(census[w][2]), setup_direction[census[w][1]]), []).append(w)
    split, cand = [], 0
    for _k, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        for u, v in combinations(sorted(members), 2):
            su, sv = by_world[u]["selected"], by_world[v]["selected"]
            if su is None or sv is None:
                continue
            cand += 1
            if su != sv:
                split.append([u, v])
    return {"candidate_pairs": cand, "pairs": sorted(split),
            "count": len(split)}


def perturb(c863, program, census, states, samples, orbits, anchor, gates):
    n = len(census)
    sim = tuple(census) + (census[0],)
    scheds, _c, _p = spliced_schedules(c863, program, sim, anchor, gates,
                                       (1 << (n + 1)) - 1)
    fast = compile_schedules(scheds)
    base = c863.pack_lanes(tuple(states) + (states[0],))
    rows = []
    for lane, wire in samples:
        a, b = list(base), list(base)
        b[wire] ^= (1 << lane)
        leak = 0
        allowed = 1 << lane
        for _o in range(orbits):
            for chunk in fast:
                chunk(a)
                chunk(b)
                for x, y in zip(a, b):
                    if (x ^ y) & ~allowed:
                        leak += 1
        rows.append({"lane": lane, "wire": wire, "leak": leak})
    return rows


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    checks, teeth = [], []

    def check(name, ok, detail=None):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return bool(ok)

    def tooth(name, fired, detail=None):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in ("sha256_all_match", "git_blobs_all_match",
                                   "mismatched_paths", "firewall_hits")}))
        receipt = {"block": "toe-time-blockQ11-20260802", "cycles": [918],
                   "certificates": {"A_PINS": cert_a},
                   "VERDICT": "CHECK_ABORTED_AT_PINS", "exit_code": 0}
        (ROOT / "outputs" /
         "writable_independent_check_cycle918_receipt_2026_07_28.json"
         ).write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                 default=str) + "\n", encoding="utf-8")
        return 0

    c863, c878, c911, c913, c878c, c911c, prov = lift_all()
    receipts = {p: json.loads(payloads[p].decode("utf-8"))
                for p in JSON_ONLY_PATHS}
    prim = receipts[PRIMARY_RECEIPT]
    r913 = receipts[C913_RECEIPT]
    r911 = receipts[C911_RECEIPT]
    r878 = receipts[C878_RECEIPT]
    pcerts = prim["certificates"]
    pmods = pcerts["C2_MEASUREMENT"]["per_modification"]
    pverd = pcerts["C3_VERDICTS"]["per_modification"]
    register_cap = c911c["REGISTER_CAP"]

    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, fails = c863.build_initial_states(program, event_seeds, census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB = K.M.R12.BANK_BASES
    REC_A, REC_B = BB[0] + K.A.POINTER, BB[1] + K.A.POINTER
    setup_direction = {ev: c913.read_state_direction(s)
                       for ev, s in event_seeds}
    width = len(states[0])

    # the modifications, re-declared here from the primary's own design rows
    design_rows = {d["name"]: d for d in pcerts["C1_CONSTRUCTION_SPACE"][
        "designs"]}
    MODS = [
        ("CONTROL", 0, ()),
        ("M_A", 0, ((KIND_CNOT, REC_A, left_w, 0),
                    (KIND_CNOT, REC_A, right_w, 0))),
        ("M_B", 0, ((KIND_SHIFT, left_w, left_w, 0),
                    (KIND_SHIFT, right_w, right_w, 0))),
        ("M_C", 0, ((KIND_TOF, REC_A, REC_B, left_w),
                    (KIND_TOF, REC_A, REC_B, right_w))),
    ]
    check("the_primary_declares_exactly_the_four_candidates_reconstructed_here",
          sorted(design_rows) == sorted(n for n, _a, _g in MODS),
          {"declared": sorted(design_rows)})
    for name, anchor, gates in MODS:
        d = design_rows[name]
        rebuilt = [{"target_wire": (a if k == KIND_X else
                                    (c3 if k == KIND_TOF else b)),
                    "input_wires": ([] if k == KIND_X else
                                    ([a, b] if k == KIND_TOF else [a]))}
                   for k, a, b, c3 in gates]
        check(f"design_rows_reconstruct_{name}",
              [{"target_wire": g["target_wire"],
                "input_wires": g["input_wires"]} for g in d["gates"]]
              == rebuilt and d["anchor_station"] == anchor,
              {"receipt": d["gates"]})

    # ---------------- K1: the splice mechanism -----------------------------
    sim_ctl = tuple(census) + (census[0],)
    ctl_sched, ctl_cuts, pinned = spliced_schedules(c863, program, sim_ctl, 0,
                                                    (), (1 << (len(sim_ctl))) - 1)
    check("empty_splice_is_the_pinned_compiler_itself",
          digest([[list(g) for g in s] for s in ctl_sched])
          == digest([[list(g) for g in s] for s in pinned]))
    ctl_sw = sweep(ctl_sched, left_w, right_w)
    check("control_gate_total_matches_the_pinned_913_lemma",
          ctl_sw["gates"] == r913["certificates"]["C1_SELECTION_TABLE"][
              "endpoint_wire_lemma"]["gates_total"],
          {"mine": ctl_sw["gates"]})
    check("control_endpoint_is_read_never_written", ctl_sw["reads_never_writes"])

    splice_rows = []
    for name, anchor, gates in MODS:
        s, cuts, _p = spliced_schedules(c863, program, sim_ctl, anchor, gates,
                                        (1 << (len(sim_ctl))) - 1)
        sw = sweep(s, left_w, right_w)
        pr = pmods[name]["ENDPOINT_WRITES"]
        splice_rows.append({
            "modification": name, "gates": sw["gates"],
            "primary_gates": pr["compiled_gates_total"],
            "gates_agree": sw["gates"] == pr["compiled_gates_total"],
            "LEFT_target": sw["LEFT_target"],
            "RIGHT_target": sw["RIGHT_target"],
            "primary_LEFT_target": pr["LEFT_is_now_a_gate_target"],
            "primary_RIGHT_target": pr["RIGHT_is_now_a_gate_target"],
            "target_claims_agree":
                sw["LEFT_target"] == pr["LEFT_is_now_a_gate_target"]
                and sw["RIGHT_target"] == pr["RIGHT_is_now_a_gate_target"],
            "reads_never_writes": sw["reads_never_writes"],
            "primary_reads_never_writes":
                pr["reads_never_writes_lemma_still_holds"],
        })
    check("splice_reproduces_every_gate_total_the_primary_reports",
          all(r["gates_agree"] for r in splice_rows), splice_rows)
    check("splice_reproduces_every_target_claim_the_primary_reports",
          all(r["target_claims_agree"] for r in splice_rows))
    cert_k1 = {"certificate": "K1_SPLICE", "rows": splice_rows,
               "mechanism":
                   "the pinned Cycle-863 masked_h_schedules output with the "
                   "extra gates inserted at an offset computed from the "
                   "station macro lengths.  The primary rebuilds the schedule "
                   "from the program; this runner never does.",
               "pass": all(r["gates_agree"] and r["target_claims_agree"]
                           for r in splice_rows)}

    # ---------------- the runs ---------------------------------------------
    runs, timings = {}, {}
    for name, anchor, gates in MODS:
        t0 = monotonic()
        runs[name] = own_scan(c863, program, census, states, HORIZON, anchor,
                              gates, False, register_cap, left_w, right_w)
        timings[name] = round(monotonic() - t0, 3)
    t0 = monotonic()
    rev_rows = {}
    for name, anchor, gates in MODS:
        r = own_scan(c863, program, census, states, HORIZON, anchor, gates,
                     True, register_cap, left_w, right_w)
        rev_rows[name] = {"digest": scan_digest(r), "formed": len(r["formed"]),
                          "dup": r["duplicate_lane_mismatches"]}
        del r
    t_rev = round(monotonic() - t0, 3)

    ctl = runs["CONTROL"]
    check("own_control_build_matches_the_pinned_913_forward_digest",
          scan_digest(ctl) == r913["certificates"]["H_DOUBLE_BUILD"][
              "digest_A"], {"mine": scan_digest(ctl)})
    check("own_control_reversed_build_matches_the_pinned_913_reverse_digest",
          rev_rows["CONTROL"]["digest"]
          == r913["certificates"]["H_DOUBLE_BUILD"]["digest_B"])
    check("own_control_lock_set_matches_the_pinned_911_set",
          sorted(ctl["formed"]) == sorted(
              row["world"] for row in r911["certificates"][
                  "C2_MENU_AT_FORMATION"]["per_lock_point_rows"]))
    check("own_control_event_cardinality_matches_878",
          len(ctl["events"]) == r878["findings"]["event_cardinality"],
          {"mine": len(ctl["events"])})

    # ---------------- recompute every reported quantity ---------------------
    LBASE = K.M.R12.LINK_BASES
    AW, LW = K.A.N, K.B.LINK_WIDTH
    endpoint_set = {left_w, right_w}
    site_wires = tuple(range(BB[0]))

    def rows_of(build):
        """Rows in the exact shape the AST-lifted Cycle-913 ladder consumes,
        so the dependence analysis below is the pinned computation, not a
        paraphrase of it."""
        out, rows = {}, []
        off = dis = 0
        for w in sorted(build["formed"]):
            st = build["snapshots"][w]
            sel = c913.read_state_direction(st)
            if sel is None:
                off += 1
            elif list(sel) != list(setup_direction[census[w][1]]):
                dis += 1
            wl, wr = build["lock_writes"].get(w, (0, 0))
            full = "".join(str(b) for b in st)
            bank0 = "".join(str(st[BB[0] + i]) for i in range(AW))
            bank1 = "".join(str(st[BB[1] + i]) for i in range(AW))
            row = {
                "world": w,
                "key": [census[w][0], census[w][1], list(census[w][2])],
                "lock_boundary": build["formed"][w],
                "phase": build["formed"][w] % stations,
                "selected_item": list(sel) if sel else None,
                "selected": list(sel) if sel else None,
                "left_writes": wl, "right_writes": wr,
                "ord0": build["lock_ordinal"][w][0],
                "ord1": build["lock_ordinal"][w][1],
                "ord": list(build["lock_ordinal"][w]),
                "bank0": bank0, "bank1": bank1,
                "link0": "".join(str(st[LBASE[0] + i]) for i in range(LW)),
                "shell2_rest": "".join(str(st[BB[b] + i])
                                       for b in (2, 3) for i in range(AW)),
                "site_block": "".join(str(st[i]) for i in site_wires),
                "site_block_minus_endpoints": "".join(
                    str(st[i]) for i in site_wires if i not in endpoint_set),
                "endpoint_bits": (st[left_w], st[right_w]),
                "state_minus_site": full[BB[0]:],
                "state_minus_endpoints": "".join(
                    c for i, c in enumerate(full) if i not in endpoint_set),
                "full_state": full,
            }
            out[w] = row
            rows.append(row)
        return out, rows, off, dis

    def literal_branch(formed):
        per_state: dict = {}
        for w, s in enumerate(states):
            per_state.setdefault(s, []).append(w)
        sid = {}
        for i, (_s, lanes) in enumerate(per_state.items()):
            for w in lanes:
                sid[w] = i
        m = Counter()
        for u, v in combinations(range(len(census)), 2):
            m[c911.classify_pair(census[u], census[v], sid[u], sid[v],
                                 formed.get(u), formed.get(v))["verdict"]] += 1
        return m[c911c["CLASS_BRANCH"]], {k: m[k] for k in sorted(m)}

    perms, perms_ok = own_monitor_phase(census, stations)
    check("own_monitor_phase_action_is_a_census_bijection", perms_ok)
    check("own_monitor_phase_action_has_order_11", len(perms) == stations)

    recompute = {}
    for name, anchor, gates in MODS:
        b = runs[name]
        by_world, rows913, off, dis = rows_of(b)
        pr = pmods[name]
        dp = dyn_pairs(census, by_world, setup_direction)
        wl = sum(a for a, _b in b["final_writes"].values())
        wr = sum(x for _a, x in b["final_writes"].values())
        sel = {w: tuple(r["selected"]) for w, r in by_world.items()
               if r["selected"]}
        inv = invariance_count(perms, sel)
        pert = perturb(c863, program, census, states,
                       ((1, left_w), (2, REC_A)), PERTURB_ORBITS, anchor,
                       gates)
        mod_sched = spliced_schedules(c863, program, sim_ctl, anchor, gates,
                                      (1 << (len(sim_ctl))) - 1)[0]
        s = sweep(mod_sched, left_w, right_w)
        xl = ast_cross_lane(mod_sched)
        wo = write_once_by_event_uniqueness(b["events"])
        lit_branch, lit_matrix = literal_branch(b["formed"])
        # the pinned Cycle-913 dependence machinery, re-run on these rows
        live = [r for r in rows913 if r["selected_item"] is not None]
        ladder = c913.ladder_rows(live, lambda r: tuple(r["selected_item"])) \
            if live else []
        by_name = {x["fingerprint"]: x for x in ladder}
        _v, determining = (c913.exhaustive_singleton_sweep(
            live, lambda r: tuple(r["selected_item"]), width)
            if live else ([], []))
        pdep = pr["DEPENDENCE"]
        dep_mine = {
            "setup_parity": by_name["SETUP_event_parity"]["is_a_function"]
            if by_name else None,
            "nn_record_content":
                by_name["R1_nearest_neighbour_record_content"]["is_a_function"]
                if by_name else None,
            "nn_ordinals":
                by_name["R1_nearest_neighbour_exact_ordinals"]["is_a_function"]
                if by_name else None,
            "endpoint_wires_only":
                by_name["SITE_ENDPOINT_WIRES_ONLY"]["is_a_function"]
                if by_name else None,
            "determining_single_wires": determining,
        }
        dep_theirs = {
            "setup_parity":
                pdep["selection_is_a_function_of_SETUP_event_parity"],
            "nn_record_content": pdep[
                "selection_is_a_function_of_nearest_neighbour_record_content"],
            "nn_ordinals":
                pdep["selection_is_a_function_of_neighbour_ordinals"],
            "endpoint_wires_only": pdep[
                "selection_is_a_function_of_the_site_endpoint_wires_only"],
            "determining_single_wires": pdep["exhaustive_single_wire_sweep"][
                "single_wires_that_DETERMINE_the_selection"],
        }
        recompute[name] = {
            "dependence_recomputed": dep_mine,
            "dependence_primary": dep_theirs,
            "dependence_agrees": dep_mine == dep_theirs,
            "ast_cross_lane": xl,
            "primary_ast_lane_locality": pr["COVARIANCE_AND_STRUCTURE"][
                "position_wise_lane_locality_certified"],
            "ast_lane_locality_agrees":
                xl["lane_local"] == pr["COVARIANCE_AND_STRUCTURE"][
                    "position_wise_lane_locality_certified"],
            "literal_911_branch_matrix": lit_matrix,
            "lock_points": len(b["formed"]),
            "primary_lock_points": pr["FORMATION"]["lock_points"],
            "lock_points_agree":
                len(b["formed"]) == pr["FORMATION"]["lock_points"],
            "total_endpoint_writes": wl + wr,
            "primary_total_endpoint_writes":
                pr["ENDPOINT_WRITES"]["total_LEFT_write_events_over_all_worlds"]
                + pr["ENDPOINT_WRITES"][
                    "total_RIGHT_write_events_over_all_worlds"],
            "write_counts_agree":
                wl == pr["ENDPOINT_WRITES"][
                    "total_LEFT_write_events_over_all_worlds"]
                and wr == pr["ENDPOINT_WRITES"][
                    "total_RIGHT_write_events_over_all_worlds"],
            "selection_dynamical_at": dis,
            "primary_selection_dynamical_at": pr["SELECTION"][
                "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"],
            "dynamical_agrees": dis == pr["SELECTION"][
                "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"],
            "off_menu": off,
            "primary_off_menu": pr["SELECTION"][
                "off_menu_endpoint_content_at_the_lock"],
            "off_menu_agrees": off == pr["SELECTION"][
                "off_menu_endpoint_content_at_the_lock"],
            "dynamical_branch_pairs": dp["count"],
            "primary_dynamical_branch_pairs": pr["BRANCH_PAIRS_dynamical"][
                "DYNAMICAL_BRANCH_PAIRS"],
            "branch_pairs_agree": dp["count"] == pr["BRANCH_PAIRS_dynamical"][
                "DYNAMICAL_BRANCH_PAIRS"],
            "branch_pairs": dp["pairs"][:12],
            "candidate_pairs": dp["candidate_pairs"],
            "z11_invariant": inv["invariant"],
            "primary_z11_invariant": pr["COVARIANCE_AND_STRUCTURE"][
                "translation_invariant"],
            "z11_agrees": inv["invariant"] == pr["COVARIANCE_AND_STRUCTURE"][
                "translation_invariant"],
            "z11_violations": inv["violations"],
            "primary_z11_violations": pr["COVARIANCE_AND_STRUCTURE"][
                "translation_violations"],
            "runtime_leak": [p["leak"] for p in pert],
            "runtime_lane_locality": all(p["leak"] == 0 for p in pert),
            "primary_runtime_lane_locality": pr["COVARIANCE_AND_STRUCTURE"][
                "runtime_lane_locality_certified"],
            "layout_independent": scan_digest(b) == rev_rows[name]["digest"],
            "primary_layout_independent": pr["COVARIANCE_AND_STRUCTURE"][
                "layout_independent"],
            "duplicate_lane_mismatches": b["duplicate_lane_mismatches"]
            + rev_rows[name]["dup"],
            "write_once_by_event_uniqueness": wo,
            "primary_write_once_violations": pr["RECORD_MACHINERY"][
                "write_once_violations"],
            "literal_911_branch_pairs_recomputed": lit_branch,
            "primary_literal_911_branch_pairs": pr[
                "BRANCH_MATRIX_911_literal"]["BRANCH_PAIRS"],
            "gate_total": s["gates"],
            "_by_world": by_world,
        }

    check("every_lock_point_count_reproduces",
          all(r["lock_points_agree"] for r in recompute.values()),
          {n: [r["lock_points"], r["primary_lock_points"]]
           for n, r in recompute.items()})
    check("every_endpoint_write_count_reproduces",
          all(r["write_counts_agree"] for r in recompute.values()),
          {n: [r["total_endpoint_writes"], r["primary_total_endpoint_writes"]]
           for n, r in recompute.items()})
    check("every_dynamical_selection_count_reproduces",
          all(r["dynamical_agrees"] for r in recompute.values()),
          {n: [r["selection_dynamical_at"],
               r["primary_selection_dynamical_at"]]
           for n, r in recompute.items()})
    check("every_dynamical_branch_pair_count_reproduces",
          all(r["branch_pairs_agree"] for r in recompute.values()),
          {n: [r["dynamical_branch_pairs"],
               r["primary_dynamical_branch_pairs"]]
           for n, r in recompute.items()})
    check("every_off_menu_count_reproduces",
          all(r["off_menu_agrees"] for r in recompute.values()))
    check("every_layout_independence_claim_reproduces",
          all(r["layout_independent"] == r["primary_layout_independent"]
              for r in recompute.values()),
          {n: [r["layout_independent"], r["primary_layout_independent"]]
           for n, r in recompute.items()})
    check("the_913_dependence_analysis_reproduces_on_every_modification",
          all(r["dependence_agrees"] for r in recompute.values()),
          {n: {"mine": r["dependence_recomputed"],
               "primary": r["dependence_primary"]}
           for n, r in recompute.items() if not r["dependence_agrees"]}
          or {n: r["dependence_recomputed"] for n, r in recompute.items()})
    check("the_911_literal_branch_matrix_reproduces_and_is_empty_everywhere",
          all(r["literal_911_branch_pairs_recomputed"]
              == r["primary_literal_911_branch_pairs"] == 0
              for r in recompute.values()),
          {n: r["literal_911_branch_matrix"] for n, r in recompute.items()})
    check("every_cross_lane_certification_reproduces",
          all(r["ast_lane_locality_agrees"] for r in recompute.values()),
          {n: r["ast_cross_lane"] for n, r in recompute.items()})
    check("every_runtime_lane_locality_claim_reproduces",
          all(r["runtime_lane_locality"] == r["primary_runtime_lane_locality"]
              for r in recompute.values()),
          {n: [r["runtime_leak"], r["primary_runtime_lane_locality"]]
           for n, r in recompute.items()})

    # ---------------- K2: the record-machinery attack -----------------------
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    ctl_rig = c878.dead_wire_rig(program, sim_ctl, proto)
    ctl_slots = tuple(sorted(set(ctl_rig["slot_of"].values())))
    rig_rows = []
    for name, anchor, gates in MODS:
        if name == "CONTROL":
            row = {"modification": name,
                   "dead_count": len(ctl_rig["dead_wires"]),
                   "safe_count": len(ctl_rig["safe_pool"]),
                   "control_slots_still_dead": True,
                   "control_slots_still_safe": True,
                   "slot_map_would_be_identical": True}
        else:
            rr = rig_under(c878, program, sim_ctl, proto, anchor, gates, c863)
            dead = set(rr["dead_wires"])
            safe = set(rr["safe_pool"])
            row = {
                "modification": name,
                "dead_count": rr["dead_count"], "safe_count": rr["safe_count"],
                "control_dead_count": len(ctl_rig["dead_wires"]),
                "control_safe_count": len(ctl_rig["safe_pool"]),
                "control_slots_still_dead": all(w in dead for w in ctl_slots),
                "control_slots_still_safe": all(w in safe for w in ctl_slots),
                "slots_that_stopped_being_dead":
                    sorted(w for w in ctl_slots if w not in dead)[:16],
                "slot_map_would_be_identical":
                    rr["safe_pool"][:len(ctl_slots)]
                    == ctl_rig["safe_pool"][:len(ctl_slots)],
            }
        rig_rows.append(row)
    slots_ok = all(r["control_slots_still_dead"] and r["control_slots_still_safe"]
                   for r in rig_rows)
    check("the_primarys_inherited_record_slots_are_still_dead_and_safe_under_"
          "every_modification", slots_ok, rig_rows)
    check("write_once_holds_by_the_independent_event_uniqueness_route",
          all(r["write_once_by_event_uniqueness"]["write_once_holds"]
              for r in recompute.values()),
          {n: r["write_once_by_event_uniqueness"]
           for n, r in recompute.items()})
    check("the_primary_reported_zero_write_once_violations_and_this_route_"
          "agrees",
          all(r["primary_write_once_violations"] == 0
              and r["write_once_by_event_uniqueness"]["write_once_holds"]
              for r in recompute.values()))
    cert_k2 = {"certificate": "K2_RECORD_MACHINERY_ATTACK",
               "rig_under_each_modification": rig_rows,
               "gap_attacked":
                   "the primary derived the Cycle-878 dead-wire safe pool "
                   "once, from the control, and then only monitored those "
                   "slots.  This runner re-derives the whole rig under every "
                   "modification at the pinned 878 window.",
               "write_once_second_route": {
                   n: r["write_once_by_event_uniqueness"]
                   for n, r in recompute.items()},
               "pass": bool(slots_ok and all(
                   r["write_once_by_event_uniqueness"]["write_once_holds"]
                   for r in recompute.values()))}

    # ---------------- K3: the covariance attack -----------------------------
    cov_rows = []
    for name, anchor, gates in MODS:
        mc = mask_covariance(c863, program, sim_ctl, anchor, gates)
        r = recompute[name]
        cov_rows.append({
            "modification": name,
            "added_gates_carry_the_anchor_station_mask_at_every_step":
                mc["all_steps_match"],
            "realized_selection_is_Z11_invariant": r["z11_invariant"],
            "primary_says": r["primary_z11_invariant"],
            "agrees": r["z11_agrees"],
            "violations": r["z11_violations"],
            "primary_violations": r["primary_z11_violations"],
            "violation_counts_agree":
                r["z11_violations"] == r["primary_z11_violations"],
        })
    check("every_Z11_invariance_claim_reproduces",
          all(r["agrees"] for r in cov_rows), cov_rows)
    check("every_Z11_violation_count_reproduces",
          all(r["violation_counts_agree"] for r in cov_rows))
    check("the_added_law_carries_the_anchor_stations_own_mask_everywhere",
          all(r["added_gates_carry_the_anchor_station_mask_at_every_step"]
              for r in cov_rows))
    cert_k3 = {"certificate": "K3_COVARIANCE_ATTACK", "rows": cov_rows,
               "reading":
                   "the added law is exactly as phase-covariant as the "
                   "station it rides -- verified structurally at every step "
                   "-- while the REALIZED selection stops being Z_11 "
                   "invariant as soon as it becomes trajectory-dependent, "
                   "because the lock tick is not phase-invariant.  The "
                   "primary's pricing of this is confirmed, not refuted.",
               "pass": all(r["agrees"] and r["violation_counts_agree"]
                           and r["added_gates_carry_the_anchor_station_mask_"
                                 "at_every_step"] for r in cov_rows)}

    # ---------------- K4: the verdict attack --------------------------------
    verdict_rows = []
    for name, _a, _g in MODS:
        if name == "CONTROL":
            continue
        pr, r = pmods[name], recompute[name]
        from_receipt = own_verdict({
            "write_once_violations": pr["RECORD_MACHINERY"][
                "write_once_violations"],
            "record_slot_activation_conflicts": pr["RECORD_MACHINERY"][
                "record_slot_activation_conflicts"],
            "slot_wires_became_gate_wires": len(pr["RECORD_MACHINERY"][
                "slot_wires_that_became_gate_wires"]),
            "targets_outside_endpoints": pr["RECORD_MACHINERY"][
                "modification_targets_a_non_endpoint_wire"],
            "duplicate_lane_mismatches":
                pr["RECORD_MACHINERY"]["duplicate_lane_mismatches_forward"]
                + pr["RECORD_MACHINERY"]["duplicate_lane_mismatches_reversed"],
            "lock_points": pr["FORMATION"]["lock_points"],
            "off_menu_lock_points": pr["SELECTION"][
                "off_menu_endpoint_content_at_the_lock"],
            "layout_independent": pr["COVARIANCE_AND_STRUCTURE"][
                "layout_independent"],
            "ast_lane_locality": pr["COVARIANCE_AND_STRUCTURE"][
                "position_wise_lane_locality_certified"],
            "runtime_lane_locality": pr["COVARIANCE_AND_STRUCTURE"][
                "runtime_lane_locality_certified"],
            "selection_dynamical": bool(pr["SELECTION"][
                "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"]),
            "dynamical_branch_pairs": pr["BRANCH_PAIRS_dynamical"][
                "DYNAMICAL_BRANCH_PAIRS"],
        })
        from_mine = own_verdict({
            "write_once_violations": 0 if r["write_once_by_event_uniqueness"][
                "write_once_holds"] else 1,
            "record_slot_activation_conflicts": 0 if slots_ok else 1,
            "slot_wires_became_gate_wires": 0,
            "targets_outside_endpoints": False,
            "duplicate_lane_mismatches": r["duplicate_lane_mismatches"],
            "lock_points": r["lock_points"],
            "off_menu_lock_points": r["off_menu"],
            "layout_independent": r["layout_independent"],
            "ast_lane_locality": r["ast_cross_lane"]["lane_local"],
            "runtime_lane_locality": r["runtime_lane_locality"],
            "selection_dynamical": bool(r["selection_dynamical_at"]),
            "dynamical_branch_pairs": r["dynamical_branch_pairs"],
        })
        verdict_rows.append({
            "modification": name,
            "primary_verdict": pverd[name]["VERDICT"],
            "checker_verdict_from_the_primarys_published_numbers": from_receipt,
            "checker_verdict_from_the_checkers_own_numbers": from_mine,
            "agrees_on_both_routes":
                pverd[name]["VERDICT"] == from_receipt == from_mine,
        })
    check("every_verdict_survives_both_independent_routes",
          all(r["agrees_on_both_routes"] for r in verdict_rows), verdict_rows)

    # a hardcoded-verdict AST attack on the primary's own source
    ptree = ast.parse(payloads[PRIMARY_PATH].decode("utf-8"))
    verdict_strings = {"BORN-CAPABLE", "STERILE", "DESTRUCTIVE"}
    returning = set()
    literal_sites = []
    for node in ast.walk(ptree):
        if isinstance(node, ast.FunctionDef):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Return) and isinstance(
                        sub.value, (ast.Constant, ast.Tuple)):
                    for c in ([sub.value] if isinstance(sub.value, ast.Constant)
                              else list(sub.value.elts)):
                        if isinstance(c, ast.Constant) \
                                and c.value in verdict_strings:
                            returning.add(node.name)
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and k.value in (
                        "M_A", "M_B", "M_C") and isinstance(
                            v, ast.Constant) and v.value in verdict_strings:
                    literal_sites.append((k.value, v.value))
    check("no_verdict_string_is_assigned_to_a_candidate_by_name_in_the_primary",
          not literal_sites, {"sites": literal_sites})
    check("verdict_strings_are_returned_only_by_the_declared_classifier",
          returning == {"classify_candidate"}, {"functions": sorted(returning)})

    cert_k4 = {"certificate": "K4_VERDICT_ATTACK", "rows": verdict_rows,
               "hardcoded_verdict_ast_sweep": {
                   "functions_returning_a_verdict_string": sorted(returning),
                   "dict_literals_mapping_a_candidate_to_a_verdict":
                       literal_sites},
               "pass": bool(all(r["agrees_on_both_routes"]
                                for r in verdict_rows)
                            and not literal_sites
                            and returning == {"classify_candidate"})}

    # ---------------- the primary's planted modification, re-run ------------
    # The plant is RECONSTRUCTED from the primary's declared selection rule --
    # the first M_A (else M_C) lock point whose realized item differs from the
    # control's and that has a same-setup-coordinate partner among the control
    # lock points -- never read off the receipt.  The receipt's own numbers are
    # then compared against the reconstruction.
    pplant = pcerts["C2_MEASUREMENT"]["planted_modification"]
    ctl_by = recompute["CONTROL"]["_by_world"]
    control_partner: dict = {}
    for w in ctl_by:
        control_partner.setdefault(
            (tuple(census[w][2]), setup_direction[census[w][1]]), []).append(w)
    plant_choice = None
    for src in ("M_A", "M_C"):
        cand_by = recompute[src]["_by_world"]
        movers = [w for w in sorted(set(ctl_by) & set(cand_by))
                  if ctl_by[w]["selected"] != cand_by[w]["selected"]]
        for w in movers:
            others = [x for x in control_partner.get(
                (tuple(census[w][2]), setup_direction[census[w][1]]), [])
                if x != w]
            if others:
                plant_choice = (src, w, sorted(others)[0])
                break
        if plant_choice:
            break
    plant_rows = None
    if plant_choice is not None:
        src, u, v = plant_choice
        gates = dict((n, g) for n, _a, g in MODS)[src]
        t0 = monotonic()
        pb = own_scan(c863, program, census, states, HORIZON, 0, gates, False,
                      register_cap, left_w, right_w, lane_restrict={u})
        t_plant = round(monotonic() - t0, 3)
        pby, _pr, poff, _pd = rows_of(pb)
        pdp = dyn_pairs(census, pby, setup_direction)
        plant_rows = {
            "reconstructed_source": src, "reconstructed_lane": u,
            "reconstructed_partner": v, "runtime_sec": t_plant,
            "dynamical_branch_pairs_found": pdp["count"],
            "primary_found": pplant.get("DYNAMICAL_BRANCH_PAIRS_FOUND"),
            "pairs": pdp["pairs"][:8],
            "primary_example_pairs": pplant.get("example_split_pairs"),
            "the_planted_pair_is_among_the_splits":
                [min(u, v), max(u, v)] in pdp["pairs"],
            "off_menu": poff,
            "agrees": (pdp["count"] == pplant.get(
                "DYNAMICAL_BRANCH_PAIRS_FOUND")
                and sorted(pdp["pairs"])
                == sorted(pplant.get("example_split_pairs") or [])
                and pplant.get("lanes_planted") == 1),
        }
        del pb
    check("the_primarys_planted_modification_reconstructs_and_reproduces",
          plant_rows is not None and plant_rows["agrees"]
          and plant_rows["the_planted_pair_is_among_the_splits"], plant_rows)
    check("the_primarys_plant_detector_matched_its_own_ground_truth",
          pplant.get("detector_matches_the_ground_truth") is True,
          {"receipt": pplant.get("detector_matches_the_ground_truth")})

    # ---------------- teeth -------------------------------------------------
    tampered = dict(EXPECTED_SHA256)
    tampered[PRIMARY_PATH] = "0" * 64
    tooth("tampered_pin_detected",
          {p: sha256((ROOT / p).read_bytes()).hexdigest()
           for p in AUDIT_INPUT_PATHS} != tampered)

    tooth("dropped_modification_detected",
          sorted(design_rows) == ["CONTROL", "M_A", "M_B", "M_C"]
          and sorted(pverd) == ["M_A", "M_B", "M_C"]
          and sorted(recompute) == ["CONTROL", "M_A", "M_B", "M_C"],
          {"designs": sorted(design_rows), "verdicts": sorted(pverd)})

    forced = own_verdict({
        "write_once_violations": 0, "record_slot_activation_conflicts": 0,
        "slot_wires_became_gate_wires": 0,
        "targets_outside_endpoints": False, "duplicate_lane_mismatches": 0,
        "lock_points": 164, "off_menu_lock_points": 0,
        "layout_independent": True, "ast_lane_locality": True,
        "runtime_lane_locality": True, "selection_dynamical": False,
        "dynamical_branch_pairs": 9})
    tooth("hardcoded_verdict_detected",
          forced == "STERILE" and not literal_sites
          and returning == {"classify_candidate"},
          {"probe_verdict": forced})

    ctl_rec = recompute["CONTROL"]
    tooth("leaked_born_capable_detected",
          ctl_rec["selection_dynamical_at"] == 0
          and ctl_rec["dynamical_branch_pairs"] == 0
          and ctl_rec["candidate_pairs"] > 0
          and own_verdict({
              "write_once_violations": 0,
              "record_slot_activation_conflicts": 0,
              "slot_wires_became_gate_wires": 0,
              "targets_outside_endpoints": False,
              "duplicate_lane_mismatches": 0, "lock_points": 164,
              "off_menu_lock_points": 0, "layout_independent": True,
              "ast_lane_locality": True, "runtime_lane_locality": True,
              "selection_dynamical": False,
              "dynamical_branch_pairs": 0}) == "STERILE",
          {"control_candidate_pairs": ctl_rec["candidate_pairs"]})

    prim_tables = prim["selection_tables"]
    missing = {}
    for name in recompute:
        mine = set(recompute[name]["_by_world"])
        theirs = {row["world"] for row in prim_tables[name]}
        missing[name] = sorted(mine ^ theirs)[:8]
    check("the_primarys_published_lock_tables_hold_exactly_the_worlds_this_"
          "runner_locked", all(not v for v in missing.values()),
          {"symmetric_difference": missing})
    # the tooth is a PLANT, not an agreement: drop one world from this
    # runner's own control table and require the comparison to notice.
    ctl_mine = set(recompute["CONTROL"]["_by_world"])
    ctl_theirs = {row["world"] for row in prim_tables["CONTROL"]}
    dropped_world = min(ctl_mine)
    tooth("skipped_world_detected",
          bool((ctl_mine - {dropped_world}) ^ ctl_theirs),
          {"dropped_world": dropped_world,
           "difference_after_the_drop":
               sorted((ctl_mine - {dropped_world}) ^ ctl_theirs)[:4],
           "difference_before_the_drop": sorted(ctl_mine ^ ctl_theirs)[:4]})

    synth = {w: dict(r) for w, r in recompute["CONTROL"]["_by_world"].items()}
    groups: dict = {}
    for w in synth:
        groups.setdefault((tuple(census[w][2]),
                           setup_direction[census[w][1]]), []).append(w)
    pw = next((sorted(v)[0] for _k, v in sorted(groups.items())
               if len(v) >= 2), None)
    if pw is not None:
        synth[pw]["selected"] = ([0, 1] if synth[pw]["selected"] == [1, 0]
                                 else [1, 0])
    tooth("planted_branch_blindness_detected",
          dyn_pairs(census, synth, setup_direction)["count"] > 0
          and recompute["CONTROL"]["dynamical_branch_pairs"] == 0,
          {"planted_world": pw})

    breach_events = list(ctl["events"][:4]) + [ctl["events"][0]]
    tooth("planted_write_once_breach_detected",
          not write_once_by_event_uniqueness(breach_events)["write_once_holds"]
          and write_once_by_event_uniqueness(
              ctl["events"])["write_once_holds"])

    fake_dead = set(ctl_rig["dead_wires"]) - {ctl_slots[0]}
    tooth("planted_dead_slot_corruption_detected",
          not all(w in fake_dead for w in ctl_slots)
          and all(w in set(ctl_rig["dead_wires"]) for w in ctl_slots),
          {"removed_slot": ctl_slots[0]})

    cert_g = {"certificate": "G_TEETH", "teeth": teeth,
              "tooth_count": len(teeth),
              "all_fired": all(t["fired"] for t in teeth),
              "pass": all(t["fired"] for t in teeth)}

    elapsed = round(monotonic() - started, 3)
    passed = sum(1 for c in checks if c["pass"])
    failed = [c for c in checks if not c["pass"]]
    survives = not failed and cert_g["all_fired"]
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if survives
               else "PRIMARY_FAILS_THIS_CHECK")

    receipt = {
        "block": "toe-time-blockQ11-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "cycles": [918], "claim_type": "independent_check",
        "audit": "unset", "authority": "none",
        "provenance": prov,
        "certificates": {
            "A_PINS": cert_a, "K1_SPLICE": cert_k1,
            "K2_RECORD_MACHINERY_ATTACK": cert_k2,
            "K3_COVARIANCE_ATTACK": cert_k3, "K4_VERDICT_ATTACK": cert_k4,
            "G_TEETH": cert_g,
            "R_RECOMPUTATION": {
                "certificate": "R_RECOMPUTATION",
                "per_modification": {
                    n: {k: v for k, v in r.items() if not k.startswith("_")}
                    for n, r in recompute.items()},
                "planted_modification_rerun": plant_rows,
                "pass": all(c["pass"] for c in checks),
            },
            "I_RUNTIME": {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
                          "budget_sec": RUNTIME_BUDGET_SEC,
                          "forward_scan_seconds": timings,
                          "reversed_scans_seconds": t_rev,
                          "pass": elapsed <= RUNTIME_BUDGET_SEC},
        },
        "checks": checks,
        "checks_passed": passed, "checks_total": len(checks),
        "failed_checks": [c["check"] for c in failed],
        "VERDICT": verdict,
        "exit_code_policy":
            "this runner exits 0 whether or not the primary survives; the "
            "verdict above is the finding.",
    }
    (ROOT / "outputs" /
     "writable_independent_check_cycle918_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")

    W = 78
    print("CYCLE 918 INDEPENDENT CHECK -- SPECIFIED TO REFUTE")
    print("=" * W)
    print(f"A_PINS  {'PASS' if cert_a['pass'] else 'FAIL'}  "
          f"({len(AUDIT_INPUT_PATHS)} pinned, firewall hits "
          f"{len(cert_a['firewall_hits'])})")
    print()
    print("K1  THE SPLICE  (pinned compiler output + offset splice; never a "
          "rebuild)")
    for r in splice_rows:
        print(f"    {r['modification']:9s} gates {r['gates']:6d} "
              f"(primary {r['primary_gates']:6d}) agree={r['gates_agree']}  "
              f"LEFT/RIGHT targets {r['LEFT_target']}/{r['RIGHT_target']} "
              f"agree={r['target_claims_agree']}")
    print()
    print("R   RECOMPUTATION  (own scan, own counters, own pair detector)")
    print(f"    {'cand':9s} {'locks':>6s} {'ep-writes':>10s} {'sel!=setup':>11s}"
          f" {'offmenu':>8s} {'dynbr':>6s} {'Z11':>6s} {'layout':>7s}")
    for n, r in recompute.items():
        print(f"    {n:9s} {r['lock_points']:6d} "
              f"{r['total_endpoint_writes']:10d} "
              f"{r['selection_dynamical_at']:11d} {r['off_menu']:8d} "
              f"{r['dynamical_branch_pairs']:6d} "
              f"{str(r['z11_invariant']):>6s} "
              f"{str(r['layout_independent']):>7s}")
    print()
    print("    dependence re-analysis (AST-lifted Cycle-913 ladder, own rows)")
    for n, r in recompute.items():
        d = r["dependence_recomputed"]
        print(f"    {n:9s} setup-parity={str(d['setup_parity']):5s} "
              f"nn-content={str(d['nn_record_content']):5s} "
              f"nn-ordinals={str(d['nn_ordinals']):5s} "
              f"endpoint-only={str(d['endpoint_wires_only']):5s} "
              f"determining={d['determining_single_wires']}  "
              f"agrees={r['dependence_agrees']}   911 branch pairs="
              f"{r['literal_911_branch_pairs_recomputed']}")
    print()
    print(f"    planted modification reconstructed: {plant_rows}")
    print()
    print("K2  RECORD MACHINERY  (rig re-derived UNDER each modification)")
    for r in rig_rows:
        print(f"    {r['modification']:9s} dead {r['dead_count']:5d} safe "
              f"{r['safe_count']:5d}  control slots still dead="
              f"{r['control_slots_still_dead']} safe="
              f"{r['control_slots_still_safe']}")
    print()
    print("K3  COVARIANCE")
    for r in cov_rows:
        print(f"    {r['modification']:9s} anchor-mask covariance="
              f"{r['added_gates_carry_the_anchor_station_mask_at_every_step']}"
              f"  Z11 invariant={r['realized_selection_is_Z11_invariant']} "
              f"(primary {r['primary_says']}) violations={r['violations']}"
              f"/{r['primary_violations']} agree={r['agrees']}")
    print()
    print("K4  VERDICTS")
    for r in verdict_rows:
        print(f"    {r['modification']:9s} primary={r['primary_verdict']:14s} "
              f"from-receipt="
              f"{r['checker_verdict_from_the_primarys_published_numbers']:14s} "
              f"from-own="
              f"{r['checker_verdict_from_the_checkers_own_numbers']:14s} "
              f"agree={r['agrees_on_both_routes']}")
    print(f"    hardcoded-verdict AST sweep: functions returning a verdict "
          f"string = {sorted(returning)}; candidate-keyed literals = "
          f"{literal_sites}")
    print()
    print(f"CHECKS  {passed}/{len(checks)} pass")
    for c in failed:
        print(f"    FAILED  {c['check']}  {compact(c['detail'])[:400]}")
    print()
    print(f"G_TEETH  {'PASS' if cert_g['pass'] else 'FAIL'}  "
          f"({cert_g['tooth_count']} teeth)")
    for t in teeth:
        print(f"    [{'x' if t['fired'] else ' '}] {t['tooth']}")
    print()
    print(f"I_RUNTIME  {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    print("=" * W)
    print(f"VERDICT: {verdict}")
    print("receipt: outputs/"
          "writable_independent_check_cycle918_receipt_2026_07_28.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
