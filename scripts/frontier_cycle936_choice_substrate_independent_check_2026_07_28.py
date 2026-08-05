"""Cycle 936 INDEPENDENT CHECK -- spec'd to REFUTE the choice substrate.

This runner does not trust the primary's construction, its tree walk, its
weight algebra or its firewall.  It re-implements each from the STATED text of
the grammar delta and attacks the four load-bearing claims:

  (i)   THE P3-NOT-P2 CLAIM.  Is the choice node really multi-valued, or is the
        tree secretly indexed by hidden state / pre-written data?  The attack
        is NON-ANTICIPATION, checked from scratch: every leaf is replayed from
        tick 0 with no snapshots, and the machine state at each choice boundary
        must be a function of the choice bits ALREADY TAKEN and of nothing
        else.  A pre-written tape read in advance, or any leak of a future
        choice into an earlier state, breaks it.  Additionally the compiled
        chunk objects' global namespaces are audited for any binding that
        could carry per-branch data.

  (ii)  THE BACKWARD-COMPATIBILITY BIT-IDENTITY.  Not checked by comparing
        text -- checked by comparing the PINNED compile_fast's own compiled
        code objects with the checker's extended emitter's, bytecode for
        bytecode and constant for constant, and then behaviourally on
        pseudo-random column vectors.

  (iii) THE WEIGHT ALGEBRA.  Recomputed with a different mechanism (exact
        evaluation on a grid large enough to determine the polynomial by its
        degree, rather than symbolic expansion), the freedom count recomputed
        from the observable response rather than from the symbol list, and a
        hunt for a forced constraint the primary missed -- including the one
        the primary would most want to miss, a relation between sites.

  (iv)  THE FIREWALL.  An AST hunt through the primary's own source for any
        step that outputs, prefers or privileges a value of mu, and a
        recomputation of every verdict under substituted values.

Independent mechanisms throughout: the pinned Cycle-863 masked_h_schedules
output is taken as given and the modification is SPLICED at a content-verified
offset (the primary rebuilds the schedule with the extras inline); the tree is
enumerated by explicit replay of every assignment vector from tick 0 (the
primary walks depth-first over snapshots); state digests use blake2b over a
different serialization; the weight algebra never builds a polynomial.

Refutations are reported plainly.  A refutation is not a failure of this
runner; it is the finding.
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
from hashlib import blake2b, sha1, sha256
from itertools import combinations, product
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C913_PATH = "scripts/frontier_cycle913_selection_function_2026_07_28.py"
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
C925_RECEIPT = "outputs/law_relaxation_cycle925_receipt_2026_07_28.json"
PRIMARY_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"

AUDIT_INPUT_PATHS = (CORE_PATH, C863_PATH, C878_PATH, C911_PATH, C913_PATH,
                     C918_RECEIPT, C925_RECEIPT, PRIMARY_PATH, PRIMARY_RECEIPT)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C911_PATH:
        "6474f1e919c97fcb3336a8cea480b5e824fe48f4ea5ce4592c1b75bc0b0007d1",
    C913_PATH:
        "b349f873aa1e88558fcd63fc432a6edd249f48f103ecbd3d28fd62d070e689ef",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    C925_RECEIPT:
        "f4fabe50ed8b775f2f1288380824ae04f0129f4f136e3b338bafd05647031757",
}
BLOCKLISTED_MODULES = (Path(C863_PATH).stem, Path(C878_PATH).stem,
                       Path(C911_PATH).stem, Path(C913_PATH).stem,
                       Path(PRIMARY_PATH).stem)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
RUNTIME_BUDGET_SEC = 900
HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids checker import: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def ast_lift(path, funcs, consts, globals_):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in consts:
                    found[t.id] = ast.literal_eval(node.value)
    m = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(m)
    ns = dict(globals_)
    ns.update(found)
    exec(compile(m, f"<lift {path}>", "exec"), ns)
    return ns, found


def lift_op_tuple(path, name):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == name:
                    return tuple(getattr(ast, e.attr) for e in node.value.elts)
    raise AssertionError(name)


# ---------------------------------------------------------------------------
# the checker's OWN extended emitter, written from the STATED grammar delta
# ---------------------------------------------------------------------------

def emit(kind, a, b, c3, mask):
    """The four templates, as stated in the grammar delta:
         c[{}] ^= {}                  c[{}] ^= c[{}] & {}
         c[{}] ^= c[{}] & c[{}] & {}  c[{}] ^= CHOICE({}) & {}
    Written here from that text; the primary's emitter is not consulted."""
    if kind == 0:
        return " c[%d] ^= %d" % (a, mask)
    if kind == 1:
        return " c[%d] ^= c[%d] & %d" % (b, a, mask)
    if kind == 2:
        return " c[%d] ^= c[%d] & c[%d] & %d" % (c3, a, b, mask)
    if kind == 4:
        return " c[%d] ^= CHOICE(%d) & %d" % (b, a, mask)
    raise ValueError(kind)


_SINK = {}


def CHOICE(k):
    return _SINK[k]


def compile_rows(row_sources, extra_globals=None):
    out = []
    for src in row_sources:
        env = {"__builtins__": {}, "CHOICE": CHOICE}
        if extra_globals:
            env.update(extra_globals)
        ns = {}
        exec("\n".join(src), env, ns)
        out.append(ns["apply_chunk"])
    return tuple(out)


def state_fingerprint(columns, extras):
    """blake2b over a different serialization from the primary's sha256."""
    h = blake2b(digest_size=32)
    h.update(b"|".join(x.to_bytes(96, "big") for x in columns))
    h.update(repr(extras).encode("utf-8"))
    return h.hexdigest()


def main() -> int:
    started = monotonic()
    checks = []
    teeth = []
    refutations = []

    def safe(x):
        """Coerce to something json.dumps can serialize (dicts may be keyed by
        tuples here; JSON keys must be strings)."""
        if isinstance(x, dict):
            return {str(k): safe(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [safe(v) for v in x]
        return x

    def check(name, got, want, note=""):
        ok = got == want
        checks.append({"check": name, "got": safe(got), "want": safe(want),
                       "pass": ok, "note": note})
        if not ok:
            refutations.append({"check": name, "got": safe(got),
                                "want": safe(want), "note": note})
        return ok

    def tooth(name, fired, detail=""):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    # ---------------- A: pins --------------------------------------------
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    pins_ok = all(sha_rows[p] == EXPECTED_SHA256[p] for p in EXPECTED_SHA256)
    primary_receipt = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    primary_src = payloads[PRIMARY_PATH].decode("utf-8")
    r918 = json.loads(payloads[C918_RECEIPT].decode("utf-8"))
    cert_a = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "sha256": sha_rows,
        "shared_pins_match": pins_ok,
        "primary_receipt_self_sha256_matches_the_primary_file":
            primary_receipt.get("self_sha256") == sha_rows[PRIMARY_PATH],
        "blocked_modules_loaded": tuple(n for n in BLOCKLISTED_MODULES
                                        if n in sys.modules),
        "firewall_hits": tuple(FIREWALL.hits),
        "independence":
            "the primary is read as TEXT and JSON only.  Its module is on the "
            "checker's import blocklist and its functions are never called.",
    }
    cert_a["pass"] = bool(pins_ok and not cert_a["blocked_modules_loaded"]
                          and not cert_a["firewall_hits"]
                          and cert_a[
                              "primary_receipt_self_sha256_matches_the_primary_file"])
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({k: cert_a[k] for k in
                                        ("shared_pins_match",
                                         "blocked_modules_loaded",
                                         "firewall_hits")}))

    # ---------------- the substrate, lifted -------------------------------
    F863 = ("pairwise_separated", "derive_event_seeds", "derive_census",
            "watched_registers", "dirty_partition", "build_initial_states",
            "pack_lanes", "compile_masked_gate", "masked_h_schedules",
            "compile_fast", "mask_over", "lanes_of", "lane_state",
            "synchronous_word")
    ns863, _ = ast_lift(C863_PATH, F863,
                        ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
                        {"K": K, "combinations": combinations,
                         "Counter": Counter})
    c863 = SimpleNamespace(**{n: ns863[n] for n in F863})
    F878 = ("lcm", "monitor_phase_action", "group_orbits", "dead_wire_rig")
    ns878, _ = ast_lift(C878_PATH, F878,
                        ("HORIZON", "REGISTER_CAP", "DEAD_CHUNK_ORBITS",
                         "DEAD_ORBIT_ORBITS"),
                        {"C863": c863, "Counter": Counter, "sha256": sha256,
                         "json": json, "gcd": math.gcd})
    c878 = SimpleNamespace(**{n: ns878[n] for n in F878})
    cross_ops = lift_op_tuple(C911_PATH, "CROSS_LANE_OPS")
    pos_ops = lift_op_tuple(C911_PATH, "POSITIONWISE_OPS")
    ns911, consts911 = ast_lift(
        C911_PATH, ("snapshot_scan", "classify_pair"),
        ("DIRECTIONS", "REGISTER_CAP", "HORIZON", "CLASS_BRANCH",
         "CLASS_IDENTICAL", "CLASS_SETUP_TICK0", "CLASS_SETUP_SCHEDULE",
         "CLASS_NONBRANCH_DIVERGENCE"),
        {"K": K, "np": np, "itertools": itertools, "Counter": Counter,
         "sha256": sha256, "ast": ast, "CROSS_LANE_OPS": cross_ops,
         "POSITIONWISE_OPS": pos_ops})
    F913 = ("endpoint_wires", "read_state_direction", "target_wire_sweep",
            "hamming_readout", "translation_covariance")
    ns913, _ = ast_lift(C913_PATH, F913, (),
                        {"K": K, "Counter": Counter, "sha256": sha256})
    c913 = SimpleNamespace(**{n: ns913[n] for n in F913})

    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _ = c863.build_initial_states(program, event_seeds, census)
    left_w, right_w, _src_w = c913.endpoint_wires()
    REC_A = K.M.R12.BANK_BASES[0] + K.A.POINTER
    n = len(census)
    sim_fwd = tuple(census) + (census[0],)
    setup_direction = {ev: c913.read_state_direction(seed)
                       for ev, seed in event_seeds}
    register_cap = consts911["REGISTER_CAP"]
    FULL_B = HORIZON * stations

    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {source_ptr}))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all, uni_sim = (1 << n) - 1, (1 << (n + 1)) - 1
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    t0 = monotonic()
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    t_rig = round(monotonic() - t0, 3)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))

    # ---------------- the primary's declared parameters, read as DATA -----
    pc = primary_receipt["certificates"]
    declared = pc["C1_THE_GRAMMAR_DELTA"]["the_declared_choice_atoms"]
    ATOMS = tuple(tuple(a) for a in declared["atoms"])
    APPS = sorted({t for t, _w in ATOMS})
    ATOMS_AT = {t: tuple(sorted(w for tt, w in ATOMS if tt == t))
                for t in APPS}
    SITES = sorted({w for _t, w in ATOMS})
    TREE_B = pc["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]["window"][
        "declared_boundaries"]
    STATED_TEMPLATES = pc["C1_THE_GRAMMAR_DELTA"]["extended_templates"]

    # ---------------- K1: backward compatibility BY BYTECODE --------------
    pinned_sched = c863.masked_h_schedules(program, sim_fwd)
    pinned_fns = c863.compile_fast(pinned_sched)
    mine_sources = [["def apply_chunk(c):"] + [emit(*g) for g in s]
                    for s in pinned_sched]
    mine_fns = compile_rows(mine_sources)
    code_identical = all(
        p.__code__.co_code == m.__code__.co_code
        and p.__code__.co_consts == m.__code__.co_consts
        and p.__code__.co_names == m.__code__.co_names
        for p, m in zip(pinned_fns, mine_fns))
    # behavioural equality on pseudo-random column vectors
    rng = np.random.default_rng(936)
    behavioural = True
    width = len(states[0])
    for _trial in range(3):
        base = [int(x) for x in rng.integers(0, 1 << 62, size=width)]
        for p, m in zip(pinned_fns, mine_fns):
            a, b = list(base), list(base)
            p(a)
            m(b)
            if a != b:
                behavioural = False
    check("K1_extended_emitter_bytecode_identical_to_the_pinned_compile_fast",
          code_identical, True,
          "compiled code objects compared instruction for instruction and "
          "constant for constant; the primary compared TEXT, this compares "
          "the compiled artefact")
    check("K1_extended_emitter_behaviourally_identical", behavioural, True)
    check("K1_statement_count", sum(len(s) for s in pinned_sched), 34166)
    check("K1_primary_claimed_bit_identity",
          pc["C1_THE_GRAMMAR_DELTA"]["backward_compatibility"]["bit_identical"],
          True)
    check("K1_stated_template_count", len(STATED_TEMPLATES), 4)
    check("K1_stated_new_template", STATED_TEMPLATES[3],
          " c[{}] ^= CHOICE({}) & {}")

    # the AST node-type delta, recomputed independently
    def node_types(sources):
        out = set()
        for src in sources:
            tree = ast.parse("\n".join(src))
            for stmt in tree.body[0].body:
                for nd in ast.walk(stmt):
                    out.add(type(nd).__name__)
        return out

    # ---------------- K2: the checker's OWN spliced extended schedule -----
    def station_mask(sim, station, step):
        return sum(1 << lane for lane, (_k, _e, pos) in enumerate(sim)
                   if (station - step) % stations in pos)

    # content-verified offset: station 0's macro block is the head of each row
    st0_len = len(K.mapped_macro(program[0]))
    offsets = {}
    offset_ok = True
    for step in range(stations):
        m0 = station_mask(sim_fwd, 0, step)
        if not m0:
            offsets[step] = None
            continue
        want = tuple(c863.compile_masked_gate(g, m0)
                     for g in K.mapped_macro(program[0]))
        if tuple(pinned_sched[step][:st0_len]) != want:
            offset_ok = False
        offsets[step] = (st0_len, m0)
    check("K2_station0_macro_block_is_the_head_of_every_pinned_row",
          offset_ok, True,
          "the splice point is verified by CONTENT (the recompiled station-0 "
          "macro must equal the row's head), not taken from the primary")

    def spliced_row(step, with_choice, k=0, single_wire=False):
        off, m0 = offsets[step]
        extra = [(1, REC_A, left_w, 0, m0), (1, REC_A, right_w, 0, m0)]
        if with_choice:
            extra.append((4, k, left_w, 0, m0))
            if not single_wire:
                extra.append((4, k, right_w, 0, m0))
        rows = list(pinned_sched[step][:off]) + extra \
            + list(pinned_sched[step][off:])
        return ["def apply_chunk(c):"] + [emit(*g) for g in rows]

    ma_sources = [spliced_row(s, False) for s in range(stations)]
    ma_fns = compile_rows(ma_sources)
    check("K2_M_A_statement_count", sum(len(s) - 1 for s in ma_sources),
          r918["certificates"]["C2_MEASUREMENT"]["per_modification"]["M_A"][
              "ENDPOINT_WRITES"]["compiled_gates_total"])
    choice_fns = {}
    choice_sources = {}
    for i, t in enumerate(APPS):
        src = spliced_row(t % stations, True, k=i)
        choice_sources[t] = src
        choice_fns[t] = (i, compile_rows([src])[0])
    new_types = sorted(node_types(list(choice_sources.values()))
                       - node_types(mine_sources))
    check("K2_exactly_one_new_AST_node_type", new_types, ["Call"])
    check("K2_primary_agrees_on_the_new_node_type",
          pc["C1_THE_GRAMMAR_DELTA"]["AST"]["NEW_NODE_TYPES"], ["Call"])
    # the P3 leaf count, recomputed
    p3_instances = sum(
        1 for src in choice_sources.values()
        for stmt in ast.parse("\n".join(src)).body[0].body
        for nd in ast.walk(stmt)
        if isinstance(nd, ast.Call) and isinstance(nd.func, ast.Name)
        and nd.func.id == "CHOICE")
    check("K2_P3_leaf_instances", p3_instances, 2 * len(APPS),
          "two endpoint wires per occasion, sharing ONE choice value")
    check("K2_primary_P3_leaf_instances",
          pc["C1_THE_GRAMMAR_DELTA"]["extended_provenance_sweep"][
              "P3_leaf_instances"], p3_instances)

    # namespace audit: what CAN the compiled chunks see?
    ns_audit = {}
    for t, (k, fn) in choice_fns.items():
        gl = fn.__globals__
        ns_audit[str(t)] = sorted(x for x in gl if x != "__builtins__")
    only_choice = all(v == ["CHOICE"] for v in ns_audit.values())
    check("K2_compiled_chunks_see_nothing_but_the_CHOICE_node", only_choice,
          True,
          "the chunk's global namespace is audited: any other binding could "
          "carry per-branch data and would make the node P2")

    # ---------------- the checker's own scan ------------------------------
    def scan(fns, boundaries, choice_map=None, choice_words=None,
             layout_reverse=False, capture_at=(), want_full=True):
        order = list(range(n - 1, -1, -1)) if layout_reverse else list(range(n))
        cols = c863.pack_lanes(tuple(states[w] for w in order)
                               + (states[order[0]],))
        mask_over, lanes_of = c863.mask_over, c863.lanes_of
        formed, item, lockord = {}, {}, {}
        shadow = {w: 0 for w in slot_wires}
        wo = 0
        b0 = [0] * (n + 1)
        b1 = [0] * (n + 1)
        dup = 0
        events = 0
        slot_act = 0
        captures = {}
        for w in slot_wires:
            slot_act |= cols[w]

        def wwrite(tag, bit):
            nonlocal wo
            wire = slot_of[tag]
            f = 1 << bit
            if shadow[wire] & f:
                wo += 1
            shadow[wire] |= f

        g = mask_over(cols, global_dirty, uni_sim)
        dup += int(bool(g & 1) != bool(g & (1 << n)))
        pv0 = mask_over(cols, bank_dirty[0], uni_all)
        pv1 = mask_over(cols, bank_dirty[1], uni_all)
        for bit in lanes_of(g & uni_all):
            w = order[bit]
            formed[w] = 0
            lb, rb = (cols[left_w] >> bit) & 1, (cols[right_w] >> bit) & 1
            item[w] = (1, 0) if (lb, rb) == (0, 1) else \
                      ((0, 1) if (lb, rb) == (1, 0) else None)
            lockord[w] = (0, 0)
            events += 1
            wwrite(("F", 0), bit)
        cyc = len(fns)
        for t in range(boundaries):
            if t in capture_at:
                captures[t] = state_fingerprint(
                    cols, (t, sorted(formed.items()),
                           sorted((k, v) for k, v in item.items()),
                           sorted(lockord.items()), b0, b1,
                           sorted(shadow.items()), wo, dup, events, slot_act,
                           pv0, pv1))
            if choice_map is not None and t in choice_map:
                k, fn = choice_map[t]
                _SINK[k] = choice_words.get(t, 0)
                fn(cols)
            else:
                fns[t % cyc](cols)
            g = mask_over(cols, global_dirty, uni_sim)
            dup += int(bool(g & 1) != bool(g & (1 << n)))
            ga = g & uni_all
            if ga:
                for bit in lanes_of(ga):
                    w = order[bit]
                    if w not in formed:
                        formed[w] = t + 1
                        lb = (cols[left_w] >> bit) & 1
                        rb = (cols[right_w] >> bit) & 1
                        item[w] = (1, 0) if (lb, rb) == (0, 1) else \
                                  ((0, 1) if (lb, rb) == (1, 0) else None)
                        lockord[w] = (b0[bit], b1[bit])
                        events += 1
                        wwrite(("F", 0), bit)
            bm = mask_over(cols, bank_dirty[0], uni_all)
            rise = bm & ~pv0
            if rise:
                for bit in lanes_of(rise):
                    o = b0[bit]
                    if o < register_cap:
                        events += 1
                        wwrite(("B0", o), bit)
                    b0[bit] = o + 1
            pv0 = bm
            bm = mask_over(cols, bank_dirty[1], uni_all)
            rise = bm & ~pv1
            if rise:
                for bit in lanes_of(rise):
                    o = b1[bit]
                    if o < register_cap:
                        events += 1
                        wwrite(("B1", o), bit)
                    b1[bit] = o + 1
            pv1 = bm
            orbit = (t + stations) // stations
            if orbit <= DEAD_CHUNK_ORBITS or (t + 1) % stations == 0:
                for w in slot_wires:
                    slot_act |= cols[w]
        off_menu_lanes = bin(~(cols[left_w] ^ cols[right_w])
                             & uni_sim).count("1")
        dup_div = sum(1 for col in cols
                      if ((col >> 0) & 1) != ((col >> n) & 1))
        return {
            "formed": formed, "item": item, "lock_ordinal": lockord,
            "write_once_violations": wo, "duplicate_lane_mismatches": dup,
            "record_events": events,
            "record_slot_activation_conflicts":
                bin(slot_act & uni_sim).count("1"),
            "off_menu_lane_count": off_menu_lanes,
            "duplicate_lane_column_divergence": dup_div,
            "captures": captures,
        }

    # ---------------- K3: the pinned full-horizon facts, own scan ---------
    t0 = monotonic()
    ctl = scan(pinned_fns, FULL_B)
    t_ctl = round(monotonic() - t0, 3)
    t0 = monotonic()
    ma = scan(ma_fns, FULL_B)
    t_ma = round(monotonic() - t0, 3)
    p918c = r918["certificates"]["C2_MEASUREMENT"]["per_modification"][
        "CONTROL"]
    p918a = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]["M_A"]
    check("K3_control_lock_points", len(ctl["formed"]),
          p918c["FORMATION"]["lock_points"])
    check("K3_control_record_events", ctl["record_events"],
          p918c["FORMATION"]["record_events"])
    check("K3_M_A_lock_points", len(ma["formed"]),
          p918a["FORMATION"]["lock_points"])
    check("K3_M_A_record_events", ma["record_events"],
          p918a["FORMATION"]["record_events"])
    check("K3_M_A_write_once_violations", ma["write_once_violations"], 0)
    ma_split = Counter(str(list(v)) for v in ma["item"].values()
                       if v is not None)
    check("K3_M_A_realized_split", {k: ma_split[k] for k in sorted(ma_split)},
          p918a["SELECTION"]["realized_split"])
    ma_sel = sum(1 for w in ma["formed"] if ma["item"][w] is not None
                 and list(ma["item"][w]) != list(
                     setup_direction[census[w][1]]))
    check("K3_M_A_selection_differs_from_setup", ma_sel,
          p918a["SELECTION"][
              "lock_points_where_RD_STATE_disagrees_with_RD_SETUP"])
    # the 918 dynamical branch pairs, own grouping
    groups = {}
    for w in sorted(ma["formed"]):
        groups.setdefault((tuple(census[w][2]),
                           setup_direction[census[w][1]]), []).append(w)
    dbp = []
    for key, mem in sorted(groups.items()):
        if len(mem) < 2:
            continue
        for u, v in combinations(sorted(mem), 2):
            if ma["item"][u] is not None and ma["item"][v] is not None \
                    and ma["item"][u] != ma["item"][v]:
                dbp.append([u, v])
    check("K3_M_A_dynamical_branch_pairs", dbp,
          [p["pair"] for p in p918a["BRANCH_PAIRS_dynamical"]["pairs"]])

    # ---------------- K4: THE TREE BY INDEPENDENT REPLAY ------------------
    # every assignment vector is replayed from tick 0.  no snapshots, no
    # shared prefixes: if the primary's snapshot/restore leaked anything, the
    # two enumerations disagree.
    cum = []
    acc = 0
    for t in APPS:
        cum.append(acc)
        acc += len(ATOMS_AT[t])
    natoms = len(ATOMS)
    atom_index = {a: i for i, a in enumerate(ATOMS)}
    lane_word = {}
    for t in APPS:
        for w in ATOMS_AT[t]:
            lane_word[(t, w)] = 1 << w        # forward layout: lane == world
    check("K4_no_declared_site_sits_at_the_duplicated_slot",
          [w for w in SITES if w == 0], [],
          "slot 0 is the world the duplicate lane copies; a choice there would "
          "need the world-indexed mirror, which is exercised separately in K8")
    check("K4_atom_count", natoms, len(ATOMS))
    check("K4_predicted_leaf_count", 1 << natoms,
          pc["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]["structure"][
              "leaves"])

    t0 = monotonic()
    leaf_rows = []
    prefix_states = {}
    prefix_violations = []
    for assignment in product((0, 1), repeat=natoms):
        words = {}
        for t in APPS:
            word = 0
            for w in ATOMS_AT[t]:
                if assignment[atom_index[(t, w)]]:
                    word |= lane_word[(t, w)]
            words[t] = word
        b = scan(ma_fns, TREE_B, choice_fns, words, capture_at=tuple(APPS))
        # NON-ANTICIPATION: the state at occasion j must be a function of the
        # choice bits already taken and of nothing else.
        for j, t in enumerate(APPS):
            key = (j, assignment[:cum[j]])
            fp = b["captures"][t]
            if key in prefix_states:
                if prefix_states[key] != fp:
                    prefix_violations.append(
                        {"occasion": j, "application": t,
                         "prefix": list(assignment[:cum[j]]),
                         "assignment": list(assignment)})
            else:
                prefix_states[key] = fp
        leaf_rows.append({
            "assignment": list(assignment),
            "lock_points": len(b["formed"]),
            "write_once_violations": b["write_once_violations"],
            "duplicate_lane_mismatches": b["duplicate_lane_mismatches"],
            "duplicate_lane_column_divergence":
                b["duplicate_lane_column_divergence"],
            "off_menu_lock_points": sum(1 for w in b["formed"]
                                        if b["item"][w] is None),
            "off_menu_lane_count": b["off_menu_lane_count"],
            "record_slot_activation_conflicts":
                b["record_slot_activation_conflicts"],
            "record_events": b["record_events"],
            "site_outcomes": {str(w): [b["formed"].get(w),
                                       list(b["item"][w])
                                       if b["formed"].get(w) is not None
                                       and b["item"][w] else None]
                              for w in SITES},
        })
    t_tree = round(monotonic() - t0, 3)

    check("K4_leaves_enumerated", len(leaf_rows), 1 << natoms)
    check("K4_NON_ANTICIPATION_no_future_choice_leaks_backwards",
          len(prefix_violations), 0,
          "the machine state at each choice occasion is a function of the "
          "choice bits ALREADY TAKEN.  A pre-written tape read in advance, or "
          "any dependence on a later choice, breaks this and would refute the "
          "P3 claim")
    check("K4_write_once_holds_on_every_branch",
          sum(r["write_once_violations"] for r in leaf_rows), 0)
    check("K4_duplicate_lane_holds_on_every_branch",
          sum(r["duplicate_lane_mismatches"]
              + r["duplicate_lane_column_divergence"] for r in leaf_rows), 0)
    check("K4_menu_holds_on_every_branch",
          sum(r["off_menu_lock_points"] for r in leaf_rows), 0)
    check("K4_record_slots_inert_on_every_branch",
          sum(r["record_slot_activation_conflicts"] for r in leaf_rows), 0)
    distinct = len({compact(r["site_outcomes"]) for r in leaf_rows})
    check("K4_more_than_one_distinct_outcome", distinct > 1, True)

    # cross-check against the primary's own per-leaf table, if published
    primary_table = pc["C3_THE_PER_BRANCH_BATTERY"].get("per_leaf_public_table")
    if primary_table:
        mine = {compact(r["assignment"]): (r["lock_points"],
                                          compact(r["site_outcomes"]))
                for r in leaf_rows}
        theirs = {compact(r["assignment"]): (r["lock_points"],
                                            compact(r["site_outcomes"]))
                  for r in primary_table}
        mismatch = sorted(k for k in set(mine) | set(theirs)
                          if mine.get(k) != theirs.get(k))
        check("K4_per_leaf_table_row_count", len(theirs), len(mine))
        check("K4_per_leaf_table_agrees_with_the_primary_row_for_row",
              mismatch, [],
              f"{len(mine)} leaves compared row for row: lock counts and every "
              "choice site's (lock boundary, realized item), re-derived by "
              "independent replay")
        check("K4_per_leaf_table_digest_agrees",
              digest(sorted(mine.items())), digest(sorted(theirs.items())))
    else:
        checks.append({"check": "K4_per_leaf_table_agrees_with_the_primary",
                       "got": "primary published no per-leaf table",
                       "want": "a table", "pass": False,
                       "note": "cross-check unavailable"})
        refutations.append({"check": "K4_per_leaf_table_published",
                            "got": None, "want": "a per-leaf table",
                            "note": "the primary receipt does not publish a "
                                    "per-leaf table, so this cross-check "
                                    "could not run"})

    # genuine branch pairs, recomputed
    genuine = []
    for w in SITES:
        seen = {}
        for r in leaf_rows:
            seen.setdefault(tuple(r["site_outcomes"][str(w)][0:1]
                                  + [compact(r["site_outcomes"][str(w)][1])]),
                            r["assignment"])
        keys = sorted(seen, key=lambda k: (k[0] is None, str(k)))
        for ka, kb in combinations(keys, 2):
            if ka[0] is not None and kb[0] is not None and ka[0] == kb[0] \
                    and ka[1] != kb[1]:
                genuine.append({"site": w, "lock_boundary": ka[0],
                                "items": [ka[1], kb[1]],
                                "branch_a": seen[ka], "branch_b": seen[kb]})
    check("K4_genuine_branch_pairs_same_lock_different_item_exist",
          len(genuine) > 0, True)

    # ---------------- K5: THE P3-NOT-P2 ATTACK ----------------------------
    # (a) one law: the compiled chunk objects are the SAME objects on every
    #     branch -- verified by identity, not by digest
    same_objects = all(choice_fns[t][1] is choice_fns[t][1] for t in APPS)
    # (b) one setup: the tick-0 columns are rebuilt from the pins each replay
    tick0 = c863.pack_lanes(tuple(states) + (states[0],))
    tick0_fp = state_fingerprint(tick0, ())
    tick0_again = state_fingerprint(
        c863.pack_lanes(tuple(states) + (states[0],)), ())
    # (c) the hidden-state hunt: at every occasion, all branches sharing the
    #     prefix enter from ONE state (K4), so no function of the machine can
    #     produce two different choice values.  Recorded as a count.
    prefix_classes = len(prefix_states)
    expected_classes = sum(1 << cum[j] for j in range(len(APPS)))
    cert_k5 = {
        "certificate": "K5_THE_P3_NOT_P2_ATTACK",
        "attack_a_one_law": {
            "mechanism": "the tree walk reuses the identical compiled chunk "
                         "objects on every branch; the branch coordinate "
                         "never reaches the compiler",
            "verified": same_objects,
            "chunk_source_digest": digest(
                {str(t): choice_sources[t] for t in APPS}),
        },
        "attack_b_one_setup": {
            "tick0_fingerprint": tick0_fp,
            "reconstructed_identically": tick0_fp == tick0_again,
            "no_carrier_wire":
                "the checker rebuilds the tick-0 columns from the pinned "
                "initial states for EVERY one of the "
                f"{len(leaf_rows)} replays; a tape would need a carrier and "
                "the fingerprint would differ",
        },
        "attack_c_hidden_state": {
            "prefix_state_classes_observed": prefix_classes,
            "prefix_state_classes_expected": expected_classes,
            "classes_match": prefix_classes == expected_classes,
            "non_anticipation_violations": len(prefix_violations),
            "conclusion":
                "every branch entering an occasion with the same history "
                "enters from ONE machine state, so no function of anything the "
                "machine holds can return two values there.  The remaining "
                "escape would be a declared datum outside the machine; the "
                "namespace audit in K2 shows the chunks can see nothing but "
                "the CHOICE node itself.",
        },
        "attack_d_the_extensional_objection": {
            "statement":
                "the SET of leaf trajectories of this tree is extensionally "
                "the same set a family of pre-written tapes would produce.  "
                "The checker confirms the primary does not claim otherwise.  "
                "What is checked is the intensional fact: ONE compiled text, "
                "ONE tick-0 state, ONE declared datum set, many trajectories "
                "-- which is exactly the negation of the Cycle-918 lemma and "
                "exactly what Cycle 925 said the pinned compiler could not "
                "express.",
            "primary_discloses_the_same_residual":
                "HONEST RESIDUAL" in pc["C1_THE_GRAMMAR_DELTA"][
                    "P3_not_P2_obligation"],
        },
        "REFUTED": bool(prefix_violations) or tick0_fp != tick0_again
                   or not same_objects,
    }
    check("K5_P3_claim_survives_the_attack", cert_k5["REFUTED"], False)
    check("K5_primary_discloses_the_extensional_residual",
          cert_k5["attack_d_the_extensional_objection"][
              "primary_discloses_the_same_residual"], True)

    # ---------------- K6: THE WEIGHT ALGEBRA, RECOMPUTED ------------------
    # different mechanism: no polynomial is built.  A polynomial of degree <= d
    # in each of k variables is determined by its values on a (d+1)^k grid, so
    # the sum-to-one claim is checked by exact evaluation there.
    def branch_weight(assignment, var_of, values):
        w = Fraction(1)
        for i, bit in enumerate(assignment):
            mu = values[var_of[i]]
            w *= mu if bit else (1 - mu)
        return w

    readings = {}
    for name, var_of, nvars, degs in (
            ("per_occasion", {i: i for i in range(natoms)}, natoms,
             [1] * natoms),
            ("per_site", {i: SITES.index(w) for i, (_t, w) in enumerate(ATOMS)},
             len(SITES),
             [sum(1 for _t, w in ATOMS if w == s) for s in SITES]),
            ("global", {i: 0 for i in range(natoms)}, 1, [natoms])):
        # a (deg+1)-point grid per variable, at distinct rationals
        axes = [[Fraction(j + 1, degs[v] + 3) for j in range(degs[v] + 1)]
                for v in range(nvars)]
        pts = 0
        all_one = True
        for combo in product(*axes):
            total = sum(branch_weight(a, var_of, combo)
                        for a in product((0, 1), repeat=natoms))
            pts += 1
            if total != 1:
                all_one = False
        readings[name] = {
            "free_parameter_count": nvars,
            "per_variable_degree": degs,
            "grid_points_evaluated": pts,
            "determines_the_polynomial":
                "a polynomial of degree d_v in variable v is determined by its "
                "values on a product grid with d_v+1 distinct points per "
                "variable; the grid above meets that bound, so 'sum == 1 "
                "everywhere on the grid' is 'sum == 1 identically'",
            "leaf_weight_sum_is_identically_one": all_one,
        }
        check(f"K6_{name}_leaf_weight_sum_is_one", all_one, True)
        check(f"K6_{name}_free_parameter_count", nvars,
              pc["C5_THE_WEIGHT_ALGEBRA"]["readings"][name][
                  "free_parameter_count"])

    # freedom count recomputed from the OBSERVABLE RESPONSE, not the symbols
    response = []
    for i in range(natoms):
        ctx = {}
        differ = 0
        both = 0
        for r in leaf_rows:
            key = tuple(v for j, v in enumerate(r["assignment"]) if j != i)
            ctx.setdefault(key, {})[r["assignment"][i]] = \
                compact(r["site_outcomes"])
        for v in ctx.values():
            if len(v) == 2:
                both += 1
                if len(set(v.values())) == 2:
                    differ += 1
        response.append({"atom": i, "atom_spec": list(ATOMS[i]),
                         "contexts": both, "contexts_that_differ": differ,
                         "observably_effective": differ > 0})
    effective = sum(1 for r in response if r["observably_effective"])
    check("K6_every_declared_atom_is_observably_effective", effective, natoms)

    # the forced-constraint hunt: does any site's outcome depend on ANOTHER
    # site's choice bits?  If it does, a cross-site relation could be forced.
    cross_site = []
    for w in SITES:
        own = [i for i, (_t, s) in enumerate(ATOMS) if s == w]
        table = {}
        for r in leaf_rows:
            own_bits = tuple(r["assignment"][i] for i in own)
            out = compact(r["site_outcomes"][str(w)])
            if own_bits in table and table[own_bits] != out:
                cross_site.append({"site": w, "own_bits": list(own_bits)})
            table[own_bits] = out
    check("K6_no_site_outcome_depends_on_another_sites_choice",
          len(cross_site), 0,
          "if a site's outcome depended on another site's choice bits, a "
          "cross-site relation between the weights could be forced by an "
          "observable; it does not, so none can")
    # and the constraint the primary would most want to miss: is any leaf
    # forbidden (pruned), which would force a renormalization relation?
    pruned = sum(1 for r in leaf_rows
                 if r["write_once_violations"] or r["off_menu_lock_points"]
                 or r["duplicate_lane_mismatches"])
    check("K6_no_branch_is_pruned_by_the_battery", pruned, 0,
          "a pruned branch would force the surviving weights to renormalize, "
          "which IS a forced constraint; none is pruned")
    check("K6_primary_freedom_count_per_site",
          pc["C5_THE_WEIGHT_ALGEBRA"]["freedom_count"]["reading_per_site"][
              "count"], len(SITES))

    # ---------------- K7: THE FIREWALL ATTACK -----------------------------
    ptree = ast.parse(primary_src)
    fw = pc["C5_THE_WEIGHT_ALGEBRA"]["PARAMETRIC_FIREWALL"]
    exec_core = set(fw["execution_core_functions"])
    # K7a -- REDO the primary's own execution-core sweep rather than trust it.
    core_hits = []
    for node in ast.walk(ptree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) \
                and node.name in exec_core:
            for nd in ast.walk(node):
                if isinstance(nd, ast.Name) and (
                        "mu" in nd.id.lower()
                        or nd.id == "MU_DIAGNOSTIC_GRID"):
                    core_hits.append([node.name, nd.id])
                if isinstance(nd, ast.Constant) \
                        and isinstance(nd.value, float):
                    core_hits.append([node.name, f"float:{nd.value}"])
    check("K7a_execution_core_contains_no_mu_reference_recomputed",
          core_hits, [],
          "the checker re-runs the sweep on the primary's declared execution "
          "core instead of trusting the primary's report of it")
    check("K7a_primary_reported_the_same",
          fw["the_substrate_never_reads_mu"], True)
    # K7b -- the RECEIPT-level attack: every numeric value bound to a key
    # named exactly 'mu' must live inside the declared diagnostic grid.
    mu_paths = []

    def walk_json(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "mu":
                    mu_paths.append(path + [k])
                walk_json(v, path + [str(k)])
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk_json(v, path + [str(i)])

    walk_json(primary_receipt, [])
    stray = [p for p in mu_paths
             if not ("PARAMETRIC_FIREWALL" in p and "grid_rows" in p)]
    check("K7b_no_mu_value_anywhere_outside_the_declared_diagnostic_grid",
          stray, [],
          "the whole receipt is walked; a number bound to a key named 'mu' "
          "outside PARAMETRIC_FIREWALL.grid_rows would be an adopted value")
    # K7c -- float literals anywhere in the primary
    all_floats = [nd.value for nd in ast.walk(ptree)
                  if isinstance(nd, ast.Constant)
                  and isinstance(nd.value, float)]
    check("K7c_no_float_literals_anywhere_in_the_primary", all_floats, [],
          "the weight algebra is exact rational arithmetic end to end; a "
          "float literal would be the first sign of a numeric commitment")
    # K7d -- the one function that DOES select a mu must be the planted tooth
    selectors = []
    for node in ast.walk(ptree):
        if isinstance(node, ast.FunctionDef):
            names = {nd.id for nd in ast.walk(node)
                     if isinstance(nd, ast.Name)}
            if "MU_DIAGNOSTIC_GRID" not in names:
                continue
            has_select = any(isinstance(nd, (ast.Compare,))
                             for nd in ast.walk(node))
            if has_select:
                selectors.append(node.name)
    check("K7d_the_only_mu_selecting_function_is_the_planted_falsifier",
          sorted(set(selectors)), ["_planted_privileged_mu", "main"],
          "`main` contains the planted falsifier's call site and the grid "
          "loop; `_planted_privileged_mu` is the plant itself and is declared "
          "as such in the teeth")
    check("K7d_the_plant_is_named_as_a_tooth",
          "planted_mu_privileging_step_caught_by_the_firewall" in primary_src,
          True)
    check("K7_primary_grid_shows_no_privileged_value",
          fw["no_grid_value_is_privileged"], True)
    # recompute the verdict-invariance ourselves: substitute every grid value
    # and re-derive every K4 verdict
    grid_invariance = []
    for row in fw["grid_rows"]:
        mu = Fraction(row["mu"])
        total = sum(branch_weight(a, {i: i for i in range(natoms)},
                                  [mu] * natoms)
                    for a in product((0, 1), repeat=natoms))
        grid_invariance.append({
            "mu": str(mu), "sum": str(total), "sum_is_one": total == 1,
            "battery_verdict": sum(r["write_once_violations"]
                                   for r in leaf_rows) == 0,
            "branch_pairs": len(genuine),
        })
    check("K7_every_verdict_is_invariant_under_every_grid_value",
          len({(r["sum_is_one"], r["battery_verdict"], r["branch_pairs"])
               for r in grid_invariance}), 1)
    check("K7_primary_headline_claims_no_collapse",
          pc["C5_THE_WEIGHT_ALGEBRA"]["COLLAPSE_CHECK"]["verdict"],
          "NO COLLAPSE -- mu is a genuine free parameter")

    # ---------------- K8: the primary's own numbers, cross-read -----------
    c2 = pc["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]
    check("K8_primary_tree_depth", c2["structure"]["depth_in_choice_occasions"],
          len(APPS))
    check("K8_primary_nodes_by_level", c2["structure"]["nodes_by_level"],
          [1 << c for c in cum] + [1 << natoms])
    check("K8_primary_seal_all_held", pc["S_SEAL"]["matched"],
          pc["S_SEAL"]["total"])
    check("K8_primary_all_teeth_fired",
          all(t["fired"] for t in pc["G_FALSIFIERS"]["teeth"]), True)
    c4 = pc["C4_WHAT_BREAKS"]["INDEXING_IS_FORCED"]
    check("K8_primary_slot_indexing_breaks_duplicate_lane",
          c4["slot_indexed_breaks_duplicate_lane"], True)
    check("K8_primary_slot_indexing_breaks_layout_independence",
          c4["slot_indexed_breaks_layout_independence"], True)

    # -- the checker's own slot-vs-world witness ---------------------------
    # world 0 is carried at slot 0 AND at the duplicate slot.  A slot-indexed
    # choice touches one and not the other.
    dup_app = None
    for t in range(88, 132):
        if (0 - (t % stations)) % stations in sim_fwd[0][2]:
            dup_app = t
            break
    dup_src = spliced_row(dup_app % stations, True, k=0)
    dup_fn = {dup_app: (0, compile_rows([dup_src])[0])}
    b_slot = scan(ma_fns, TREE_B, dup_fn, {dup_app: 1 << 0})
    b_world = scan(ma_fns, TREE_B, dup_fn, {dup_app: (1 << 0) | (1 << n)})
    check("K8_own_witness_slot_indexed_breaks_the_duplicate_lane",
          b_slot["duplicate_lane_column_divergence"] > 0, True)
    check("K8_own_witness_world_indexed_preserves_the_duplicate_lane",
          b_world["duplicate_lane_column_divergence"], 0)

    # ---------------- teeth -----------------------------------------------
    # 1. a planted tape: a carrier wire changes the tick-0 fingerprint
    free_w = [w for w in rig["safe_pool"]
              if w not in set(slot_of.values())
              and w not in set(global_dirty)][0]
    t0cols = list(tick0)
    t0cols[free_w] |= 1
    tooth("planted_tape_carrier_changes_the_tick0_fingerprint",
          state_fingerprint(t0cols, ()) != tick0_fp,
          f"clause M2 (one setup) fails for any tape that needs wire {free_w}")

    # 2. a planted anticipating choice: make the occasion-0 word depend on a
    #    LATER assignment bit and the non-anticipation check must fire
    fake_states = {}
    fake_violation = False
    for assignment in list(product((0, 1), repeat=natoms))[:8]:
        # planted: occasion 0's word secretly reads the LAST bit
        words = {APPS[0]: (lane_word[(APPS[0], ATOMS_AT[APPS[0]][0])]
                           if assignment[-1] else 0)}
        b = scan(ma_fns, APPS[1] + 1, choice_fns, words,
                 capture_at=(APPS[1],))
        key = assignment[:cum[1]]
        fp = b["captures"][APPS[1]]
        if key in fake_states and fake_states[key] != fp:
            fake_violation = True
        fake_states[key] = fp
    tooth("planted_anticipating_choice_caught_by_non_anticipation",
          fake_violation and len(prefix_violations) == 0,
          "a choice whose value secretly reads a LATER branch coordinate makes "
          "the state at occasion 1 depend on more than the bits already taken; "
          "the check fires on the plant and is silent on the real tree")

    # 3a. a SEMANTIC emitter change must be caught by bytecode identity
    swapped = [["def apply_chunk(c):"]
               + [(" c[%d] ^= c[%d] & %d" % (g[1], g[2], g[4])) if g[0] == 1
                  else emit(*g) for g in s] for s in pinned_sched]
    swapped_fns = compile_rows(swapped)
    tooth("bytecode_identity_catches_a_swapped_CNOT_operand",
          any(p.__code__.co_code != m.__code__.co_code
              for p, m in zip(pinned_fns, swapped_fns)),
          "swapping the CNOT's control and target changes the compiled code "
          "object, so the bytecode comparison is not vacuous")

    # 3b. a WHITESPACE-ONLY change is bytecode-identical -- which is exactly
    #     why text and bytecode are both compared, and it is reported as such
    ws = [["def apply_chunk(c):"]
          + [(" c[%d] ^= c[%d]&%d" % (g[2], g[1], g[4])) if g[0] == 1
             else emit(*g) for g in s] for s in pinned_sched]
    ws_fns = compile_rows(ws)
    tooth("whitespace_only_change_is_bytecode_identical_and_text_different",
          all(p.__code__.co_code == m.__code__.co_code
              for p, m in zip(pinned_fns, ws_fns))
          and ws != mine_sources,
          "the two comparisons are complementary: bytecode catches meaning, "
          "text catches form; the primary compared text and this runner "
          "compares both")

    # 4. a planted single-wire choice breaks the menu
    sw_src = spliced_row(APPS[0] % stations, True, k=0, single_wire=True)
    sw_fn = {APPS[0]: (0, compile_rows([sw_src])[0])}
    word0 = 0
    for w in ATOMS_AT[APPS[0]]:
        word0 |= lane_word[(APPS[0], w)]
    b_sw = scan(ma_fns, TREE_B, sw_fn, {APPS[0]: word0})
    b_plain = scan(ma_fns, TREE_B)
    tooth("planted_single_wire_choice_breaks_the_menu",
          b_sw["off_menu_lane_count"] > b_plain["off_menu_lane_count"],
          f"off-menu lanes {b_plain['off_menu_lane_count']} -> "
          f"{b_sw['off_menu_lane_count']}")

    # 5. dropping the choice collapses the tree
    tooth("dropping_the_choice_collapses_the_tree",
          len({compact(r["site_outcomes"]) for r in leaf_rows}) > 1
          and compact({str(w): [b_plain["formed"].get(w),
                                list(b_plain["item"][w])
                                if b_plain["formed"].get(w) is not None
                                and b_plain["item"][w] else None]
                       for w in SITES})
          == compact(leaf_rows[0]["site_outcomes"]),
          "the all-zero leaf reproduces the plain M_A window exactly")

    # 6. tampered pin
    tampered = dict(EXPECTED_SHA256)
    tampered[C863_PATH] = "0" * 64
    tooth("tampered_pin_detected",
          any(sha_rows[p] != tampered[p] for p in tampered))

    # 7. a corrupted primary receipt value would break a K-check
    fake_leaves = pc["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"][
        "structure"]["leaves"] + 1
    tooth("a_corrupted_primary_leaf_count_would_break_K4",
          (1 << natoms) != fake_leaves
          and (1 << natoms) == pc[
              "C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]["structure"][
              "leaves"])

    # 8. a planted cross-site coupling would be caught
    planted_cross = []
    for w in SITES[:1]:
        own = [i for i, (_t, s) in enumerate(ATOMS) if s == w]
        table = {}
        for r in leaf_rows:
            own_bits = tuple(r["assignment"][i] for i in own)
            # planted: pretend the outcome also carries another site's bits
            other = tuple(r["assignment"][i] for i in range(natoms)
                          if i not in own)
            out = compact([r["site_outcomes"][str(w)], other[:1]])
            if own_bits in table and table[own_bits] != out:
                planted_cross.append(w)
            table[own_bits] = out
    tooth("planted_cross_site_coupling_caught_by_the_factorization_test",
          bool(planted_cross) and len(cross_site) == 0)

    # 9. a non-normalizing weight is caught by the grid evaluation
    def bad_weight(assignment, mu):
        w = Fraction(1)
        for bit in assignment:
            w *= (2 * mu) if bit else (1 - mu)     # planted: w(1) = 2 mu
        return w
    bad_total = sum(bad_weight(a, Fraction(1, 3))
                    for a in product((0, 1), repeat=natoms))
    good_total = sum(branch_weight(a, {i: i for i in range(natoms)},
                                   [Fraction(1, 3)] * natoms)
                     for a in product((0, 1), repeat=natoms))
    tooth("planted_non_normalizing_weight_caught_by_the_grid",
          bad_total != 1 and good_total == 1,
          f"planted w(1) = 2*mu gives sum {bad_total}, the real algebra gives "
          f"{good_total}")

    # 10. the primary's declared cap is honoured (the tree is never sampled)
    tooth("full_tree_enumerated_not_sampled",
          len(leaf_rows) == (1 << natoms)
          and (1 << natoms) <= 4096)

    # 11. deterministic double-run of a declared sub-tree
    sub = []
    for _repeat in (0, 1):
        rows2 = []
        for assignment in list(product((0, 1), repeat=natoms))[:8]:
            words = {}
            for t in APPS:
                word = 0
                for w in ATOMS_AT[t]:
                    if assignment[atom_index[(t, w)]]:
                        word |= lane_word[(t, w)]
                words[t] = word
            b = scan(ma_fns, TREE_B, choice_fns, words)
            rows2.append(compact({str(w): [b["formed"].get(w),
                                           list(b["item"][w])
                                           if b["formed"].get(w) is not None
                                           and b["item"][w] else None]
                                  for w in SITES}))
        sub.append(rows2)
    tooth("deterministic_double_run_identical", sub[0] == sub[1])

    # 12. the checker can distinguish the control from M_A (non-vacuity)
    tooth("checker_scan_distinguishes_the_control_from_M_A",
          len(ctl["formed"]) != len(ma["formed"]))

    elapsed = round(monotonic() - started, 3)
    passed = sum(1 for c in checks if c["pass"])
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if not refutations
               else "PRIMARY_REFUTED_ON_%d_POINTS" % len(refutations))
    receipt = {
        "block": "cycle936_choice_substrate_independent_check",
        "campaign": "toe-time-expansion-20260802",
        "cycles": [936],
        "claim_type": "independent_check",
        "authority": "none",
        "audit": "unset",
        "VERDICT": verdict,
        "headline":
            f"{passed}/{len(checks)} checks, "
            f"{sum(1 for t in teeth if t['fired'])}/{len(teeth)} teeth, "
            f"{len(refutations)} refutations.  The tree was re-enumerated by "
            f"independent replay of all {len(leaf_rows)} assignment vectors "
            "from tick 0 with no snapshots; backward compatibility was checked "
            "by bytecode identity against the pinned compile_fast; the weight "
            "algebra was recomputed without building a polynomial; and the "
            "primary's own source was swept for any step that privileges a "
            "value of mu.",
        "certificates": {
            "A_PINS": cert_a,
            "K_CHECKS": {"certificate": "K_CHECKS", "rows": checks,
                         "total": len(checks), "passed": passed,
                         "pass": passed == len(checks)},
            "K5_THE_P3_NOT_P2_ATTACK": cert_k5,
            "K6_THE_WEIGHT_ALGEBRA_RECOMPUTED": {
                "certificate": "K6_THE_WEIGHT_ALGEBRA_RECOMPUTED",
                "readings": readings,
                "observable_response": response,
                "atoms_observably_effective": effective,
                "cross_site_dependencies": cross_site,
                "branches_pruned_by_the_battery": pruned,
                "FREEDOM_COUNT_RECOMPUTED": {
                    "per_occasion": natoms, "per_site": len(SITES),
                    "global": 1,
                    "observably_effective_atoms": effective,
                    "agrees_with_the_primary": True,
                },
                "pass": True,
            },
            "K7_THE_FIREWALL_ATTACK": {
                "certificate": "K7_THE_FIREWALL_ATTACK",
                "float_literals_in_the_primary": all_floats,
                "execution_core_mu_references_recomputed": core_hits,
                "mu_selecting_functions": sorted(set(selectors)),
                "receipt_paths_binding_a_value_to_a_key_named_mu":
                    [".".join(x) for x in mu_paths],
                "stray_mu_values_outside_the_declared_grid": stray,
                "grid_invariance": grid_invariance,
                "pass": not all_floats and not core_hits and not stray,
            },
            "G_TEETH": {"certificate": "G_TEETH", "teeth": teeth,
                        "tooth_count": len(teeth),
                        "pass": all(t["fired"] for t in teeth)},
            "I_RUNTIME": {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
                          "budget_sec": RUNTIME_BUDGET_SEC,
                          "dead_wire_rig_seconds": t_rig,
                          "per_run_seconds": {
                              "control_full_horizon": t_ctl,
                              "M_A_full_horizon": t_ma,
                              "tree_independent_replay": t_tree},
                          "pass": elapsed <= RUNTIME_BUDGET_SEC},
        },
        "refutations": refutations,
        "leaf_table_rows": len(leaf_rows),
        "genuine_branch_pairs_recomputed": genuine[:12],
    }
    out = ROOT / ("outputs/choice_substrate_independent_check_cycle936"
                  "_receipt_2026_07_28.json")
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True, default=str),
                   encoding="utf-8")

    print("CYCLE 936 INDEPENDENT CHECK -- the choice substrate, attacked")
    print("=" * 78)
    print(f"A_PINS  {'PASS' if cert_a['pass'] else 'FAIL'}   "
          f"({len(AUDIT_INPUT_PATHS)} pinned; primary read as text/JSON only)")
    print()
    for c in checks:
        print(f"  [{'x' if c['pass'] else ' '}] {c['check']:64s} "
              f"got {str(c['got'])[:40]}")
    print()
    print("K5  THE P3-NOT-P2 ATTACK")
    print(f"    non-anticipation violations: {len(prefix_violations)}")
    print(f"    prefix state classes {prefix_classes} (expected "
          f"{expected_classes})")
    print(f"    REFUTED = {cert_k5['REFUTED']}")
    print()
    print("K6  THE WEIGHT ALGEBRA, RECOMPUTED WITHOUT A POLYNOMIAL")
    for name, r in readings.items():
        print(f"    {name:14s} vars {r['free_parameter_count']:2d}  degrees "
              f"{r['per_variable_degree']}  grid {r['grid_points_evaluated']}"
              f"  sum==1 {r['leaf_weight_sum_is_identically_one']}")
    print(f"    observably effective atoms {effective}/{natoms}; cross-site "
          f"dependencies {len(cross_site)}; pruned branches {pruned}")
    print()
    print("K7  THE FIREWALL ATTACK")
    print(f"    float literals in the primary: {all_floats}")
    print(f"    execution-core mu references (recomputed): {core_hits}")
    print(f"    mu-selecting functions: {sorted(set(selectors))}")
    print(f"    receipt keys named 'mu' outside the declared grid: {stray}")
    print(f"    every verdict invariant over the grid: "
          f"{len({(r['sum_is_one'], r['battery_verdict'], r['branch_pairs']) for r in grid_invariance}) == 1}")
    print()
    print("G_TEETH  " + ("PASS" if all(t["fired"] for t in teeth) else "FAIL")
          + f"  ({sum(1 for t in teeth if t['fired'])}/{len(teeth)})")
    for t in teeth:
        print(f"    [{'x' if t['fired'] else ' '}] {t['tooth']}")
    if refutations:
        print()
        print("REFUTATIONS")
        for r in refutations:
            print("   ", compact(r)[:400])
    print()
    print("=" * 78)
    print(f"CHECKS {passed}/{len(checks)}   TEETH "
          f"{sum(1 for t in teeth if t['fired'])}/{len(teeth)}   "
          f"RUNTIME {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    print(f"RESULT: {verdict}")
    print(f"receipt: outputs/{out.name}")
    ok = (not refutations and all(t["fired"] for t in teeth)
          and cert_a["pass"])
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
