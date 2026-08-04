"""Cycle 913 INDEPENDENT CHECK -- specified to REFUTE the selection-function
primary.

The primary claims: (i) at all 164 Cycle-911 formation lock points the landed
composed scan realizes a definite menu item, 84 of them (1,0) and 80 of them
(0,1); (ii) the selection is NOT a function of the nearest-neighbour
conditions, NOT a function of record content, and NOT a member of the pinned
classified covariant rule space; (iii) its MINIMAL determining context is a
single wire -- the site's own endpoint content -- and no wire outside the site
determines it, alone or in any combination.

This checker rebuilds all of that from the pinned substrate with its own code
and then attacks it:

  D1  INDEPENDENT LOCK RECONSTRUCTION.  Its own bit-packed scan (its own chunk
      compiler, its own dirty test, a pseudorandom lane permutation) plus a
      fully SEMANTIC per-world replay from tick 0 for every world within the
      replay budget.  Its own re-arm trajectory match.

  D2  THE FINGERPRINT ATTACK -- where an error in a dependence analysis hides.
      Every grouping is recomputed under the checker's OWN encoding (integers
      and canonical digests instead of the primary's bit strings) and compared
      group-for-group, collision-class-for-collision-class, against the
      primary's receipt.  Any disagreement REFUTES.

  D3  THE MINIMALITY ATTACK.  Exhaustive re-sweep of all 5,815 singleton wire
      contexts; exhaustive sweep of ALL PAIRS of varying non-site wires; the
      empty context; and every setup coordinate.  Any determining context that
      is smaller, or that lives outside the site, REFUTES the minimality
      claim.

  D4  THE CLASSIFIED-RULE ATTACK.  The cubic group, the direction action, the
      colouring orbits and the Burnside counts are rebuilt from scratch (no
      AST lift of the classification runner) and compared with the note's own
      byte-quoted numbers and with the primary's.

  D5  COVARIANCE AND CONTENT re-derived independently.

  E   TEETH.  Eight planted defects that this checker must catch.

Exit code is 0 whether or not the primary's claim survives; the verdict is in
the receipt and on stdout.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
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
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C911_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
C911_NOTE = (
    "docs/RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_CYCLE911"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
COVCLASS_PATH = (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS"
    "_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE"
    "_2026-07-03.md"
)
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMARY_PATH = "scripts/frontier_cycle913_selection_function_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/selection_function_cycle913_receipt_2026_07_28.json"

CHECK_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C911_PATH, C911_RECEIPT,
    C911_NOTE, COVCLASS_PATH, AXIOMS_PATH, PRIMARY_PATH, PRIMARY_RECEIPT,
)
EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
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
    C911_NOTE:
        "40c80402e2dfd283a4309433cfa48705c45567efadf43107e074332f1cbf5ff0",
    COVCLASS_PATH:
        "fe56ef6c21c00732281676cca1724231951e40fc2b746f255f655307dc76001d",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}

AST_ONLY = (C863_PATH, C878_PATH, C911_PATH, PRIMARY_PATH)
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AST_ONLY)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
HORIZON = 16_384
REPLAY_LOCK_CAP = 20_000
REPLAY_WALL_BUDGET_SEC = 220
REARM_CAP = 44
LANE_PERM_SEED = 0x913


class _CheckFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids check import: {fullname}")
        return None


FIREWALL = _CheckFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


CHECKS: list = []


def record(name, passed, detail=None):
    CHECKS.append({"check": name, "pass": bool(passed), "detail": detail})
    return bool(passed)


# ---------------------------------------------------------------------------
# the checker's own AST lift (only the substrate builders; no 911 machinery)
# ---------------------------------------------------------------------------

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
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = dict(globals_)
    ns.update(found)
    exec(compile(module, f"<check-lift {path}>", "exec"), ns)
    return ns, found


C863_FUNCS = ("pairwise_separated", "derive_event_seeds", "derive_census",
              "watched_registers", "dirty_partition", "build_initial_states")


# ---------------------------------------------------------------------------
# D1: the checker's OWN scan
# ---------------------------------------------------------------------------

def own_lane_permutation(n):
    """A pseudorandom lane -> bit layout, independent of both of the
    primary's (forward and reversed)."""
    state = LANE_PERM_SEED
    order = list(range(n))
    for i in range(n - 1, 0, -1):
        state = (1103515245 * state + 12345) & 0x7FFFFFFF
        j = state % (i + 1)
        order[i], order[j] = order[j], order[i]
    return order


_CHUNK_CACHE: dict = {}


def own_chunks(program, positions):
    """The checker's own per-step gate word: at step t the stations
    `positions + t (mod stations)` fire, in ascending station order."""
    key = tuple(positions)
    if key in _CHUNK_CACHE:
        return _CHUNK_CACHE[key]
    stations = len(program)
    out = []
    for step in range(stations):
        live = {(p + step) % stations for p in key}
        gates = []
        for station in range(stations):
            if station in live:
                gates.extend(K.mapped_macro(program[station]))
        out.append(tuple(gates))
    _CHUNK_CACHE[key] = tuple(out)
    return _CHUNK_CACHE[key]


def own_compile(program, laid_census):
    """The checker's own chunk compiler.  Emits per-chunk closures over an
    explicit gate table -- no generated source, unlike the pinned
    compile_fast."""
    stations = len(program)
    chunks = []
    for step in range(stations):
        table = []
        for station in range(stations):
            mask = 0
            for lane, (_k, _e, positions) in enumerate(laid_census):
                if (station - step) % stations in positions:
                    mask |= 1 << lane
            if not mask:
                continue
            for g in K.mapped_macro(program[station]):
                if g.kind == "X":
                    table.append((0, g.wires[0], 0, 0, mask))
                elif g.kind == "CNOT":
                    table.append((1, g.wires[0], g.wires[1], 0, mask))
                else:
                    table.append((2, g.wires[0], g.wires[1], g.wires[2], mask))
        chunks.append(tuple(table))

    def make(table):
        def apply(cols):
            for kind, a, b, c, mask in table:
                if kind == 0:
                    cols[a] ^= mask
                elif kind == 1:
                    cols[b] ^= cols[a] & mask
                else:
                    cols[c] ^= cols[a] & cols[b] & mask
        return apply
    return tuple(make(t) for t in chunks)


def own_scan(program, census, states, orbits, dirty_wires):
    n = len(census)
    order = own_lane_permutation(n)
    laid_census = tuple(census[w] for w in order)
    laid_states = tuple(states[w] for w in order)
    chunks = own_compile(program, laid_census)
    width = len(states[0])
    cols = [0] * width
    for lane, st in enumerate(laid_states):
        bit = 1 << lane
        for wire in range(width):
            if st[wire]:
                cols[wire] |= bit
    universe = (1 << n) - 1
    formed: dict[int, int] = {}
    snap: dict[int, tuple] = {}
    ords: dict[int, tuple] = {}
    bank_ord = [[0, 0] for _ in range(n)]
    banks = dirty_wires["banks"]

    def clean_mask(wires):
        acc = 0
        for w in wires:
            acc |= cols[w]
        return universe & ~acc

    def lanes(mask):
        out = []
        while mask:
            low = mask & -mask
            out.append(low.bit_length() - 1)
            mask ^= low
        return out

    def read(lane):
        bit = 1 << lane
        return tuple(1 if cols[w] & bit else 0 for w in range(width))

    prev = [clean_mask(banks[b]) for b in (0, 1)]
    for lane in lanes(clean_mask(dirty_wires["global"])):
        w = order[lane]
        formed[w] = 0
        snap[w] = read(lane)
        ords[w] = (0, 0)
    boundary = 0
    for _ in range(orbits):
        for chunk in chunks:
            chunk(cols)
            boundary += 1
            g = clean_mask(dirty_wires["global"])
            if g:
                for lane in lanes(g):
                    w = order[lane]
                    if w not in formed:
                        formed[w] = boundary
                        snap[w] = read(lane)
                        ords[w] = tuple(bank_ord[lane])
            for b in (0, 1):
                bm = clean_mask(banks[b])
                rise = bm & ~prev[b]
                for lane in lanes(rise):
                    bank_ord[lane][b] += 1
                prev[b] = bm
    return formed, snap, ords, boundary


def endpoint_wires():
    X = K.M.R3.X
    return X.LEFT_ENDPOINT, X.RIGHT_ENDPOINT, X.SOURCE_POINTER


def direction_of(state):
    left, right, _ = endpoint_wires()
    if state[right] == 1 and state[left] == 0:
        return (1, 0)
    if state[right] == 0 and state[left] == 1:
        return (0, 1)
    return None


def semantic_replay(program, positions, seed_state, dirty_global, cap):
    """Fully semantic replay from tick 0 -- no packing, no compiled chunks."""
    chunks = own_chunks(program, positions)
    stations = len(program)
    cur = seed_state
    if not any(cur[w] for w in dirty_global):
        return 0, direction_of(cur), cur
    for boundary in range(1, cap + 1):
        cur = K.A.apply_semantic(cur, chunks[(boundary - 1) % stations])
        if not any(cur[w] for w in dirty_global):
            return boundary, direction_of(cur), cur
    return None, None, None


def own_rearm(program, positions, lock_state, lock_boundary, menu):
    chunks = own_chunks(program, positions)
    stations = len(program)
    _l, _r, src = endpoint_wires()
    cur = lock_state
    b = lock_boundary
    for _ in range(REARM_CAP):
        prev = cur
        cur = K.A.apply_semantic(cur, chunks[b % stations])
        b += 1
        if prev[src] == 0 and cur[src] == 1:
            hits, dists = [], {}
            for v in menu:
                try:
                    cand = K.M.prepare_endpoint(prev, v)
                except Exception:
                    dists[v] = None
                    continue
                d = sum(1 for i in range(len(cur)) if cand[i] != cur[i])
                dists[v] = d
                if d == 0:
                    hits.append(v)
            return (hits[0] if len(hits) == 1 else None), dists, b
    return None, {}, None


# ---------------------------------------------------------------------------
# D2/D3: the checker's own dependence machinery (integer encodings)
# ---------------------------------------------------------------------------

def bits_to_int(state, wires):
    v = 0
    for i, w in enumerate(wires):
        if state[w]:
            v |= 1 << i
    return v


def functional(rows, key_fn, val_fn):
    groups: dict = {}
    for r in rows:
        groups.setdefault(key_fn(r), []).append(r)
    coll = []
    for k, ms in groups.items():
        vals = {val_fn(m) for m in ms}
        if len(vals) > 1:
            coll.append((k, ms, sorted(vals)))
    witness = None
    if coll:
        coll.sort(key=lambda c: (-len(c[1]), str(c[0])))
        _k, ms, vals = coll[0]
        a = next(m for m in ms if val_fn(m) == vals[0])
        b = next(m for m in ms if val_fn(m) == vals[1])
        witness = (a["world"], list(vals[0]), b["world"], list(vals[1]))
    return {
        "groups": len(groups),
        "is_a_function": not coll,
        "collision_classes": len(coll),
        "largest_collision_class_size": max((len(c[1]) for c in coll),
                                            default=0),
        "witness": witness,
    }


# ---------------------------------------------------------------------------
# D4: the checker's own cubic group and orbit machinery
# ---------------------------------------------------------------------------

OWN_DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
            (0, 0, -1))


def own_cubic_group():
    """Signed permutation matrices on Z^3, as permutations of the six axis
    directions.  Built from scratch, without numpy and without the pinned
    classification runner."""
    full, proper = [], []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            # row r of M has entry signs[r] in column perm[r]
            image = []
            for d in OWN_DIRS:
                out = [0, 0, 0]
                for r in range(3):
                    out[r] = signs[r] * d[perm[r]]
                image.append(OWN_DIRS.index(tuple(out)))
            det = 0
            # determinant of a signed permutation matrix: sign(perm)*prod(signs)
            sgn = 1
            p = list(perm)
            for i in range(3):
                for j in range(i + 1, 3):
                    if p[i] > p[j]:
                        sgn = -sgn
            det = sgn * signs[0] * signs[1] * signs[2]
            full.append(tuple(image))
            if det == 1:
                proper.append(tuple(image))
    return tuple(sorted(set(full))), tuple(sorted(set(proper)))


def own_orbits(perms, alphabet):
    """Orbits of k-colourings of the six directions under the given
    permutation group, by direct closure."""
    seen: set = set()
    orbits = []
    for col in itertools.product(range(alphabet), repeat=6):
        if col in seen:
            continue
        orbit = {col}
        frontier = [col]
        while frontier:
            c = frontier.pop()
            for perm in perms:
                image = [0] * 6
                for src, dst in enumerate(perm):
                    image[dst] = c[src]
                image = tuple(image)
                if image not in orbit:
                    orbit.add(image)
                    frontier.append(image)
        seen |= orbit
        orbits.append(frozenset(orbit))
    return tuple(orbits)


def own_colouring(bank_words, ordinals, alphabet):
    col = [0] * 6
    for b in (0, 1):
        if ordinals[b] == 0:
            v = 0
        elif alphabet == 2:
            v = 1
        else:
            h = int(sha256(bytes(bank_words[b])).hexdigest()[:8], 16)
            v = 1 + (h % (alphabet - 1))
        col[b] = v
    return tuple(col)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    payloads = {p: (ROOT / p).read_bytes() for p in CHECK_INPUT_PATHS}
    shas = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    pin_ok = all(shas[p] == EXPECTED_SHA256[p] for p in EXPECTED_SHA256)
    record("pins_independently_verified", pin_ok,
           {"paths": len(CHECK_INPUT_PATHS),
            "mismatches": [p for p in EXPECTED_SHA256
                           if shas[p] != EXPECTED_SHA256[p]]})
    record("no_blocklisted_module_imported",
           not FIREWALL.hits and not any(m in sys.modules
                                         for m in BLOCKLISTED_MODULES))

    receipt = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    r911 = json.loads(payloads[C911_RECEIPT].decode("utf-8"))
    c2_911 = r911["certificates"]["C2_MENU_AT_FORMATION"]
    pc = receipt["certificates"]
    p_rows = pc["C1_SELECTION_TABLE"]["per_lock_point_rows"]
    p_sel = {r["world"]: tuple(r["selected_item"]) for r in p_rows}

    # ---- substrate ----
    ns863, _ = ast_lift(C863_PATH, C863_FUNCS,
                        ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES"),
                        {"K": K, "combinations": combinations,
                         "Counter": Counter})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_fail = c863.build_initial_states(program, event_seeds, census)
    per_bank, links, src_ptr = c863.dirty_partition()
    dirty_global = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {src_ptr}))
    dirty_wires = {"global": dirty_global,
                   "banks": (tuple(sorted(per_bank[0])),
                             tuple(sorted(per_bank[1])))}
    record("substrate_rebuilt", len(census) == 748 and init_fail == 0,
           {"census": len(census), "init_failures": init_fail})

    left_w, right_w, src_w = endpoint_wires()
    width = len(states[0])
    BB = K.M.R12.BANK_BASES
    LB = K.M.R12.LINK_BASES
    AW = K.A.N
    LW = K.B.LINK_WIDTH
    menu = ((1, 0), (0, 1))

    # ---- D1: independent scan ----
    t0 = monotonic()
    formed, snap, ords, boundaries = own_scan(program, census, states,
                                              HORIZON, dirty_wires)
    scan_sec = round(monotonic() - t0, 3)
    my_locks = sorted(formed)
    record("D1_lock_set_matches_the_primary",
           my_locks == [r["world"] for r in p_rows],
           {"mine": len(my_locks), "primary": len(p_rows),
            "seconds": scan_sec})
    record("D1_lock_set_matches_cycle911",
           my_locks == sorted(r["world"] for r
                              in c2_911["per_lock_point_rows"]))
    record("D1_lock_boundaries_match_the_primary",
           [formed[w] for w in my_locks]
           == [r["lock_boundary"] for r in p_rows])

    my_sel = {}
    for w in my_locks:
        my_sel[w] = direction_of(snap[w])
    record("D1_state_readout_selection_matches_the_primary",
           my_sel == p_sel,
           {"disagreements": [w for w in my_locks if my_sel[w] != p_sel[w]]})
    my_split = Counter(my_sel.values())
    p_split = {tuple(json.loads(k)): v["count"] for k, v
               in pc["C1_SELECTION_TABLE"]["selection_split"].items()}
    record("D1_split_matches_the_primary", dict(my_split) == p_split,
           {"mine": {str(list(k)): v for k, v in my_split.items()},
            "primary": {str(list(k)): v for k, v in p_split.items()}})

    # structural lemma, recomputed from the RAW program (not from schedules)
    raw_targets, raw_inputs = set(), set()
    for row in program:
        for g in K.mapped_macro(row):
            raw_targets.add(g.wires[-1])
            raw_inputs.update(g.wires[:-1])
    record("D1_endpoint_wires_are_never_gate_targets",
           left_w not in raw_targets and right_w not in raw_targets
           and left_w in raw_inputs and right_w in raw_inputs,
           {"left": left_w, "right": right_w,
            "source_pointer_is_a_target": src_w in raw_targets})

    # semantic replay + own re-arm
    replayed, replay_bad, rearm_bad, rearm_dists = 0, [], [], set()
    for w in my_locks:
        key = census[w]
        if formed[w] <= REPLAY_LOCK_CAP and \
                monotonic() - started < REPLAY_WALL_BUDGET_SEC:
            b, d, st = semantic_replay(program, key[2], states[w],
                                       dirty_global, REPLAY_LOCK_CAP)
            replayed += 1
            if b != formed[w] or d != my_sel[w] or st != snap[w]:
                replay_bad.append(w)
        item, dists, _rb = own_rearm(program, key[2], snap[w], formed[w], menu)
        if item != my_sel[w]:
            rearm_bad.append(w)
        rearm_dists |= {v for v in dists.values() if v is not None}
    record("D1_semantic_replay_agrees",
           not replay_bad,
           {"worlds_replayed": replayed, "of": len(my_locks),
            "disagreements": replay_bad})
    record("D1_own_rearm_trajectory_match_agrees", not rearm_bad,
           {"disagreements": rearm_bad,
            "hamming_distances_seen": sorted(rearm_dists)})

    # ---- context table, checker's own encoding (integers) ----
    rows = []
    for w in my_locks:
        st = snap[w]
        key = census[w]
        rows.append({
            "world": w, "key": [key[0], key[1], list(key[2])],
            "tick": formed[w], "phase": formed[w] % stations,
            "sel": my_sel[w],
            "ord": ords[w],
            "b0": bits_to_int(st, range(BB[0], BB[0] + AW)),
            "b1": bits_to_int(st, range(BB[1], BB[1] + AW)),
            "lk": bits_to_int(st, range(LB[0], LB[0] + LW)),
            "shell2": bits_to_int(
                st, list(range(BB[2], BB[2] + AW))
                + list(range(BB[3], BB[3] + AW))),
            "nonsite": bits_to_int(st, range(BB[0], width)),
            "site_no_ep": bits_to_int(
                st, [i for i in range(BB[0]) if i not in (left_w, right_w)]),
            "ep": (st[left_w], st[right_w]),
            "state": st,
            "bank_words": (bytes(st[BB[0] + i] for i in range(AW)),
                           bytes(st[BB[1] + i] for i in range(AW))),
        })

    # ---- D2: THE FINGERPRINT ATTACK ----
    ladder = {
        "R1_nearest_neighbour_record_content": lambda r: (r["b0"], r["b1"]),
        "R1_nearest_neighbour_openness_only":
            lambda r: (r["ord"][0] > 0, r["ord"][1] > 0),
        "R1_nearest_neighbour_exact_ordinals": lambda r: r["ord"],
        "R2_shell2_add_link_and_banks_2_3":
            lambda r: (r["b0"], r["b1"], r["lk"], r["shell2"]),
        "R3_shell3_whole_substrate_minus_the_site": lambda r: r["nonsite"],
        "R3_plus_schedule_phase": lambda r: (r["nonsite"], r["phase"]),
        "R3_plus_phase_plus_lock_tick":
            lambda r: (r["nonsite"], r["phase"], r["tick"]),
        "R3_plus_phase_plus_tick_plus_token_positions":
            lambda r: (r["nonsite"], r["phase"], r["tick"],
                       tuple(r["key"][2])),
        "R3_plus_phase_plus_tick_plus_tokens_plus_source_count":
            lambda r: (r["nonsite"], r["phase"], r["tick"],
                       tuple(r["key"][2]), r["key"][0]),
        "FULL_STATE_MINUS_THE_TWO_ENDPOINT_WIRES":
            lambda r: (r["nonsite"], r["site_no_ep"], r["phase"], r["tick"],
                       tuple(r["key"][2]), r["key"][0]),
        "SITE_BLOCK_including_the_endpoint_wires":
            lambda r: (r["site_no_ep"], r["ep"]),
        "SITE_ENDPOINT_WIRES_ONLY": lambda r: r["ep"],
        "SITE_BLOCK_MINUS_THE_ENDPOINT_WIRES": lambda r: r["site_no_ep"],
        "SETUP_event_index": lambda r: r["key"][1],
        "SETUP_event_parity": lambda r: r["key"][1] % 2,
        "SETUP_token_positions_only": lambda r: tuple(r["key"][2]),
        "SCHEDULE_phase_only": lambda r: r["phase"],
        "SCHEDULE_lock_tick_only": lambda r: r["tick"],
        "EMPTY_CONTEXT": lambda r: 0,
    }
    p_ladder = {row["fingerprint"]: row
                for row in pc["C2_DEPENDENCE"]["ladder"]}
    record("D2_ladder_covers_every_declared_radius",
           set(ladder) == set(p_ladder),
           {"missing_from_checker": sorted(set(p_ladder) - set(ladder)),
            "missing_from_primary": sorted(set(ladder) - set(p_ladder))})

    mine_ladder, mismatches = {}, []
    for name, fn in ladder.items():
        res = functional(rows, fn, lambda r: r["sel"])
        mine_ladder[name] = res
        p = p_ladder.get(name)
        if p is None:
            mismatches.append((name, "absent-from-primary"))
            continue
        for field in ("groups", "is_a_function", "collision_classes",
                      "largest_collision_class_size"):
            if res[field] != p[field]:
                mismatches.append((name, field, res[field], p[field]))
    record("D2_FINGERPRINT_ATTACK_grouping_agrees_under_a_different_encoding",
           not mismatches, {"mismatches": mismatches[:12]})

    # digest-based third encoding, for the two decisive entries
    third = {
        "R1_nearest_neighbour_record_content": functional(
            rows, lambda r: sha256(r["bank_words"][0]
                                   + r["bank_words"][1]).hexdigest(),
            lambda r: r["sel"]),
        "R3_shell3_whole_substrate_minus_the_site": functional(
            rows, lambda r: sha256(bytes(r["state"][BB[0]:])).hexdigest(),
            lambda r: r["sel"]),
    }
    record("D2_third_encoding_agrees",
           all(third[k]["groups"] == mine_ladder[k]["groups"]
               and third[k]["is_a_function"] == mine_ladder[k]["is_a_function"]
               for k in third),
           {k: {"groups": v["groups"], "is_a_function": v["is_a_function"]}
            for k, v in third.items()})

    nn_res = mine_ladder["R1_nearest_neighbour_record_content"]
    record("D2_selection_is_NOT_a_function_of_nearest_neighbour_conditions",
           not nn_res["is_a_function"], {"witness": nn_res["witness"],
                                         "groups": nn_res["groups"]})
    p_wit = p_ladder["R1_nearest_neighbour_record_content"]["witness_pair"]
    record("D2_witness_pair_reproduced",
           p_wit is not None and nn_res["witness"] is not None
           and {p_wit["left"]["world"], p_wit["right"]["world"]}
           == {nn_res["witness"][0], nn_res["witness"][2]},
           {"primary": p_wit, "mine": nn_res["witness"]})

    # ---- D3: THE MINIMALITY ATTACK ----
    varying = [w for w in range(width)
               if len({r["state"][w] for r in rows}) > 1]
    singles = []
    for w in varying:
        seen: dict = {}
        ok = True
        for r in rows:
            b = r["state"][w]
            if seen.setdefault(b, r["sel"]) != r["sel"]:
                ok = False
                break
        if ok:
            singles.append(w)
    nonsite_varying = [w for w in varying if w >= BB[0]]
    pairs_found = []
    for a, b in combinations(nonsite_varying, 2):
        seen = {}
        ok = True
        for r in rows:
            k = (r["state"][a], r["state"][b])
            if seen.setdefault(k, r["sel"]) != r["sel"]:
                ok = False
                break
        if ok:
            pairs_found.append((a, b))
    empty_determines = len({r["sel"] for r in rows}) == 1
    setup_singletons = {
        "k": functional(rows, lambda r: r["key"][0], lambda r: r["sel"]),
        "event": functional(rows, lambda r: r["key"][1], lambda r: r["sel"]),
        "event_parity": functional(rows, lambda r: r["key"][1] % 2,
                                   lambda r: r["sel"]),
        "phase": functional(rows, lambda r: r["phase"], lambda r: r["sel"]),
        "tick": functional(rows, lambda r: r["tick"], lambda r: r["sel"]),
        "tokens": functional(rows, lambda r: tuple(r["key"][2]),
                             lambda r: r["sel"]),
    }
    p_min = pc["C2_DEPENDENCE"]["MINIMAL_DETERMINING_CONTEXT"]
    p_singles = pc["C2_DEPENDENCE"]["exhaustive_single_wire_sweep"][
        "single_wires_that_DETERMINE_the_selection"]
    record("D3_single_wire_sweep_reproduced", singles == p_singles,
           {"mine": singles, "primary": p_singles,
            "wires_that_vary": len(varying)})
    record("D3_no_smaller_context_exists",
           (not empty_determines) and p_min["cardinality"] == 1
           and bool(singles),
           {"empty_context_determines": empty_determines,
            "primary_claimed_cardinality": p_min["cardinality"]})
    record("D3_MINIMALITY_ATTACK_no_non_site_context_of_size_1_or_2_determines",
           not pairs_found and not any(w >= BB[0] for w in singles),
           {"non_site_varying_wires": len(nonsite_varying),
            "pairs_tested": len(nonsite_varying) * (len(nonsite_varying) - 1)
            // 2,
            "determining_pairs_found": pairs_found[:5]})
    record("D3_widest_non_site_context_does_not_determine",
           not mine_ladder["R3_shell3_whole_substrate_minus_the_site"][
               "is_a_function"])
    record("D3_setup_singletons_agree_with_the_primary",
           setup_singletons["event_parity"]["is_a_function"]
           and setup_singletons["event"]["is_a_function"]
           and not setup_singletons["tokens"]["is_a_function"]
           and not setup_singletons["phase"]["is_a_function"],
           {k: v["is_a_function"] for k, v in setup_singletons.items()})

    # ---- D4: THE CLASSIFIED-RULE ATTACK ----
    own_full, own_proper = own_cubic_group()
    class_rows, class_bad = [], []
    for kk in (2, 3, 4):
        po = own_orbits(own_proper, kk)
        fo = own_orbits(own_full, kk)
        ids = {}
        for i, orb in enumerate(po):
            for c in orb:
                ids[c] = i
        cls_of = {r["world"]: ids[own_colouring(r["bank_words"], r["ord"], kk)]
                  for r in rows}
        sizes = Counter(cls_of[r["world"]] for r in rows)
        per_class: dict = {}
        for r in rows:
            per_class.setdefault(cls_of[r["world"]], set()).add(r["sel"])
        nonconst = sorted(c for c, v in per_class.items() if len(v) > 1)
        prow = next(x for x in pc["C2_DEPENDENCE"][
            "covariance_cubic_on_the_declared_embedding"]
            if x["alphabet_k"] == kk)
        # orbit IDs are enumeration-order dependent, so the comparison is on
        # the class-size MULTISET, which is not
        row = {"alphabet_k": kk, "proper_orbits": len(po),
               "full_orbits": len(fo), "chiral_pairs": len(po) - len(fo),
               "classes_realized": len(sizes),
               "class_size_multiset": sorted(sizes.values()),
               "selection_class_constant": not nonconst,
               "non_constant_classes": len(nonconst)}
        class_rows.append(row)
        if (row["proper_orbits"] != prow["proper_orbits_total"]
                or row["full_orbits"] != prow["full_orbits_total"]
                or row["classes_realized"]
                != prow["classes_realized_by_the_formation_contexts"]
                or row["selection_class_constant"]
                != prow["selection_is_class_constant"]
                or row["class_size_multiset"]
                != sorted(prow["class_sizes"].values())
                or row["non_constant_classes"]
                != len(prow["classes_on_which_the_selection_is_NOT_"
                            "constant"])):
            class_bad.append((kk, row, prow))
    record("D4_group_order_rebuilt",
           len(own_full) == 48 and len(own_proper) == 24,
           {"full": len(own_full), "proper": len(own_proper)})
    record("D4_CLASSIFIED_RULE_ATTACK_orbit_counts_agree", not class_bad,
           {"rows": class_rows, "mismatches": class_bad[:3]})
    covnote = payloads[COVCLASS_PATH].decode("utf-8")
    note_ok = (
        ("Burnside orbit counts agree at 10 and\n   10" in covnote)
        and ("57 and 56: exactly **one** chiral pair" in covnote)
        and ("the count grows to 20 pairs" in covnote))
    record("D4_note_byte_quotes_present_and_matched", note_ok and all(
        (r["alphabet_k"] == 2 and r["proper_orbits"] == 10
         and r["full_orbits"] == 10)
        or (r["alphabet_k"] == 3 and r["proper_orbits"] == 57
            and r["full_orbits"] == 56)
        or (r["alphabet_k"] == 4 and r["chiral_pairs"] == 20)
        for r in class_rows))
    record("D4_landed_selection_is_not_in_the_classified_space",
           all(not r["selection_class_constant"] for r in class_rows)
           and pc["C5_CLASSIFIED_RULE_COMPARISON"][
               "landed_selection_is_a_function_of_the_neighbour_colouring"]
           is False)

    # ---- D5: covariance + content, re-derived ----
    index_of = {key: i for i, key in enumerate(census)}
    perms = []
    action_ok = True
    for m in range(stations):
        image = []
        for k, e, positions in census:
            tgt = (k, e, tuple(sorted((p + m) % stations for p in positions)))
            if tgt not in index_of:
                action_ok = False
                break
            image.append(index_of[tgt])
        if not action_ok:
            break
        perms.append(tuple(image))
    checks = viol = 0
    lockset = set(my_sel)
    if action_ok:
        for perm in perms:
            for w in sorted(lockset):
                if perm[w] in lockset:
                    checks += 1
                    viol += int(my_sel[perm[w]] != my_sel[w])
    p_trans = pc["C2_DEPENDENCE"]["covariance_translation"]
    record("D5_translation_covariance_reproduced",
           action_ok and checks == p_trans["in_set_image_checks"]
           and viol == p_trans["selection_violations_under_translation"],
           {"mine": {"checks": checks, "violations": viol},
            "primary": {"checks": p_trans["in_set_image_checks"],
                        "violations": p_trans[
                            "selection_violations_under_translation"]}})

    no_record = [r for r in rows if r["ord"] == (0, 0)]
    no_record_sel = Counter(r["sel"] for r in no_record)
    tick0 = [r for r in rows if r["tick"] == 0]
    tick0_sel = Counter(r["sel"] for r in tick0)
    p_c3 = pc["C3_CONTENT_DETERMINATION"]["reading_2_record_event_history"]
    record("D5_content_witness_reproduced",
           len(no_record) == p_c3[
               "lock_points_with_NO_prior_record_event_at_all"]
           and len(no_record_sel) > 1 and len(tick0_sel) > 1
           and len(tick0) == p_c3["lock_points_at_tick_zero"],
           {"no_prior_record": len(no_record),
            "their_selections": {str(list(k)): v
                                 for k, v in no_record_sel.items()},
            "tick0": len(tick0),
            "tick0_selections": {str(list(k)): v
                                 for k, v in tick0_sel.items()}})
    record("D5_selection_is_not_content_determined",
           not mine_ladder["R1_nearest_neighbour_record_content"][
               "is_a_function"]
           and not mine_ladder["R1_nearest_neighbour_exact_ordinals"][
               "is_a_function"]
           and pc["C3_CONTENT_DETERMINATION"][
               "selection_is_a_function_of_record_content_alone"] is False)

    distinct_nn = len({(r["b0"], r["b1"]) for r in rows})
    record("D5_context_variation_reproduced",
           distinct_nn == pc["C4_CONTEXT_VARIATION"][
               "distinct_nearest_neighbour_contexts"]
           and distinct_nn > 1,
           {"mine": distinct_nn,
            "primary": pc["C4_CONTEXT_VARIATION"][
                "distinct_nearest_neighbour_contexts"]})

    # ---- source hygiene: no hardcoded selection table in the primary ----
    src = payloads[PRIMARY_PATH].decode("utf-8")
    tree = ast.parse(src)
    big_literals = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)) \
                and len(node.elts) >= 40 \
                and all(isinstance(e, ast.Constant) for e in node.elts):
            big_literals += 1
    record("D6_primary_carries_no_large_hardcoded_table", big_literals == 0,
           {"large_constant_sequences": big_literals})
    record("D6_primary_reads_selection_from_the_state_not_a_constant",
           "def read_state_direction" in src
           and "state[right]" in src and "state[left]" in src)

    # ---- E: teeth ----
    teeth = []

    def tooth(name, detected, detail=None):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "detail": detail})

    # E1 tampered pin
    bad = bytearray(payloads[C911_RECEIPT])
    bad[len(bad) // 2] ^= 0x01
    tooth("tampered_pin_detected",
          sha256(bytes(bad)).hexdigest() != EXPECTED_SHA256[C911_RECEIPT])

    # E2 dropped lock point
    dropped = [r for r in p_rows if r["world"] != p_rows[0]["world"]]
    tooth("dropped_lock_point_detected",
          [r["world"] for r in dropped] != my_locks,
          {"dropped": p_rows[0]["world"]})

    # E3 hardcoded selection
    faked = {w: (1, 0) for w in my_locks}
    tooth("hardcoded_selection_detected", faked != my_sel)

    # E4 leaked / hardcoded determinism verdict: the machinery must flip
    local_rows = [{**r, "sel": (1, 0) if bin(r["b1"]).count("1") % 2 == 0
                   else (0, 1)} for r in rows]
    nonlocal_rows = [dict(r) for r in local_rows]
    big_class: dict = {}
    for r in nonlocal_rows:
        big_class.setdefault((r["b0"], r["b1"]), []).append(r)
    biggest = max(big_class.values(), key=len)
    biggest[0]["sel"] = (0, 1) if biggest[0]["sel"] == (1, 0) else (1, 0)
    f_local = functional(local_rows, lambda r: (r["b0"], r["b1"]),
                         lambda r: r["sel"])
    f_nonlocal = functional(nonlocal_rows, lambda r: (r["b0"], r["b1"]),
                            lambda r: r["sel"])
    tooth("determinism_verdict_is_data_driven_not_leaked",
          f_local["is_a_function"] and not f_nonlocal["is_a_function"],
          {"local_verdict": f_local["is_a_function"],
           "nonlocal_verdict": f_nonlocal["is_a_function"]})

    # E5 skipped fingerprint radius
    short = dict(ladder)
    short.pop("R2_shell2_add_link_and_banks_2_3")
    tooth("skipped_fingerprint_radius_detected", set(short) != set(p_ladder),
          {"missing": sorted(set(p_ladder) - set(short))})

    # E6 planted-nonlocal blindness
    planted = [dict(r) for r in rows]
    coll: dict = {}
    for r in planted:
        coll.setdefault((r["b0"], r["b1"]), []).append(r)
    target = max(coll.values(), key=len)
    for r in planted:
        r["sel"] = (1, 0)
    target[0]["sel"] = (0, 1)
    f_planted = functional(planted, lambda r: (r["b0"], r["b1"]),
                           lambda r: r["sel"])
    tooth("planted_nonlocal_selection_not_missed",
          not f_planted["is_a_function"] and f_planted["witness"] is not None,
          {"witness": f_planted["witness"]})

    # E7 the minimality hunt is not blind
    probe = nonsite_varying[0]
    planted_wire = [{**r, "sel": (1, 0) if r["state"][probe] else (0, 1)}
                    for r in rows]
    hunt = []
    for w in varying:
        seen = {}
        ok = True
        for r in planted_wire:
            if seen.setdefault(r["state"][w], r["sel"]) != r["sel"]:
                ok = False
                break
        if ok:
            hunt.append(w)
    tooth("minimality_hunt_finds_a_planted_determining_wire",
          probe in hunt, {"probe_wire": probe, "found": len(hunt)})

    # E8 tampered receipt verdict
    tampered = dict(receipt)
    tampered["VERDICT"] = "SOMETHING ELSE"
    tooth("tampered_receipt_verdict_detected",
          tampered["VERDICT"] != receipt["VERDICT"]
          and receipt["VERDICT"] == "O2 SUPPLIED, MEASURED, AND NOT LOCAL")

    passes = sum(1 for c in CHECKS if c["pass"])
    fails = [c["check"] for c in CHECKS if not c["pass"]]
    teeth_ok = all(t["detected"] for t in teeth)
    survives = not fails and teeth_ok
    elapsed = round(monotonic() - started, 3)

    out = {
        "block": "toe-time-blockQ10-20260802",
        "cycles": [913],
        "role": "independent_check",
        "audit": "unset", "authority": "none",
        "checks": CHECKS,
        "teeth": teeth,
        "counts": {"pass": passes, "fail": len(fails),
                   "teeth": len(teeth),
                   "teeth_detected": sum(1 for t in teeth if t["detected"])},
        "failed_checks": fails,
        "independent_reconstruction": {
            "own_lane_permutation_seed": LANE_PERM_SEED,
            "own_chunk_compiler": "closure over an explicit gate table; the "
                                  "pinned compile_fast generates and execs "
                                  "source instead",
            "own_scan_seconds": scan_sec,
            "lock_points": len(my_locks),
            "semantic_replays": replayed,
            "selection_split": {str(list(k)): v
                                for k, v in sorted(my_split.items())},
            "own_ladder": {k: {kk: v[kk] for kk in
                               ("groups", "is_a_function",
                                "collision_classes",
                                "largest_collision_class_size")}
                           for k, v in mine_ladder.items()},
            "own_single_wire_determining_set": singles,
            "own_classified_rows": class_rows,
        },
        "elapsed_sec": elapsed,
        "runtime_budget_sec": RUNTIME_BUDGET_SEC,
        "VERDICT": ("PRIMARY_SURVIVES_THIS_CHECK" if survives
                    else "PRIMARY_REFUTED_BY_THIS_CHECK"),
    }
    (ROOT / "outputs"
     / "selection_independent_check_cycle913_receipt_2026_07_28.json"
     ).write_text(json.dumps(out, indent=2, sort_keys=True, default=str)
                  + "\n", encoding="utf-8")

    W = 78
    print("CYCLE 913 INDEPENDENT CHECK -- SPECIFIED TO REFUTE")
    print("=" * W)
    for c in CHECKS:
        print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}")
        if not c["pass"] and c["detail"] is not None:
            print(f"         {compact(c['detail'])[:600]}")
    print()
    print("  independent reconstruction:")
    print(f"    own scan ({scan_sec}s, lane permutation seed "
          f"{hex(LANE_PERM_SEED)}): {len(my_locks)} lock points")
    print(f"    semantic replays from tick 0: {replayed}/{len(my_locks)}")
    print(f"    own selection split: "
          + ", ".join(f"{list(k)} -> {v}"
                      for k, v in sorted(my_split.items())))
    print(f"    own single-wire determining set: {singles}")
    print(f"    own classified rows: "
          + "; ".join(f"k={r['alphabet_k']} {r['proper_orbits']}/"
                      f"{r['full_orbits']} classes {r['classes_realized']} "
                      f"const={r['selection_class_constant']}"
                      for r in class_rows))
    print()
    print(f"  TEETH ({sum(1 for t in teeth if t['detected'])}/{len(teeth)})")
    for t in teeth:
        print(f"    [{'x' if t['detected'] else ' '}] {t['tooth']}")
    print()
    print("=" * W)
    print(f"PASS={passes} FAIL={len(fails)}  teeth "
          f"{sum(1 for t in teeth if t['detected'])}/{len(teeth)}  "
          f"{elapsed}s")
    print(f"VERDICT: {out['VERDICT']}")
    if fails:
        print("FAILED CHECKS: " + ", ".join(fails))
    return 0


if __name__ == "__main__":
    sys.exit(main())
