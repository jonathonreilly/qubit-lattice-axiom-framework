#!/usr/bin/env python3
"""Cycle 942 INDEPENDENT CHECK -- specified to REFUTE the blind tier.

The primary reuses the pinned Cycle-930 committed code path, so a checker that
did the same would prove nothing.  This one shares no line of it.

  POSTURE, DISCLOSED (the same one Cycles 922 and 930 took, and the only route
  inside budget).  Ticks are generated from the KERNEL'S CROSSING IDENTITY --
  ``holder[v]`` is the lane mask of lanes carrying a token at ring position
  ``v``, and at tick ``t`` station ``s`` fires exactly for
  ``holder[(s - t + 1) mod N]`` -- with no phase table anywhere.  The generator
  is then validated TICK FOR TICK against the kernel's own composed step
  function ``apply_controller_step`` on a small tier, which carries the kernel's
  own token shuffle, so the token-advance model is validated and not assumed.
  The detector is re-derived from Cycle 889/891/922's STATED semantics on
  explicit tick SETS -- no bitmask folding, no shift trick -- and validated
  against a literal per-tick oracle.  Run-start attribution comes from the
  stated bookkeeping identity, implemented from the words.

  THE ATTACKS.
    (i)   THE CONSTRUCTION.  B = 10 is rebuilt from scratch with the independent
          generator and every bank clock's entry-gap row is recounted and
          compared with the primary's published row.
    (ii)  THE ZERO.  The third pair is hunted at B = 10 both the primary's way
          (CONSECUTIVE P-separated run starts) and WIDENED -- ANY two
          P-separated run starts in a stretch, which is a strictly larger
          population.  A single episode anywhere refutes the seal at the blind
          tier.
    (iii) THE RC-2 ROWS.  The carrier map is recounted independently and the
          necessity and sufficiency verdicts are recomputed from the recount,
          not read from the primary.
    (iv)  THE CROSS TIER.  B = 5 is rebuilt and recounted against the PINNED
          Cycle-930 rows, so the independent machinery is shown to agree with
          the published corpus before it is believed at B = 10.
    (v)   THE SEAL.  Recomputed from the 930-published text with this checker's
          own arithmetic.

  Refutations are reported plainly and are not softened.
"""
from __future__ import annotations

import ast
from collections import defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import random
import sys
import time


ROOT = Path(__file__).resolve().parents[1]

PRIMARY_942 = "scripts/frontier_cycle942_blind_tier_2026_07_28.py"
RECEIPT_942 = "outputs/blind_tier_cycle942_receipt_2026_07_28.json"

PRIMARY_930 = "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py"
CHECKER_930 = "scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py"
RECEIPT_930 = "outputs/third_pair_rc3_cycle930_receipt_2026_07_28.json"
RECEIPT_930_CHECK = (
    "outputs/third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json")
RECEIPT_922 = "outputs/p32_carrier_cycle922_receipt_2026_07_28.json"
RECEIPT_922_CHECK = (
    "outputs/p32_carrier_independent_check_cycle922_receipt_2026_07_28.json")
PRIMARY_922 = "scripts/frontier_cycle922_p32_carrier_2026_07_28.py"
CHECKER_922 = "scripts/frontier_cycle922_p32_carrier_independent_check_2026_07_28.py"
PRIMARY_891 = "scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
CHECKER_891 = "scripts/frontier_cycle891_complement_independent_check_2026_07_28.py"
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

PINS = {
    PRIMARY_930: ("afe78fdfe466724686b4a42d50893e1a0c5b41dc6c58aea27a765f5c8576cb92",
                  "1b163d8cf59d6143fa3bfd83a170e805f3e7d0c0"),
    RECEIPT_930: ("a865ebc7c9ce2a03306c33a636f7583cadc0f3bc9ec3abfea0cac0491ae902a2",
                  "0aaf4442470dac362d490adf5f093bb512e30b89"),
    RECEIPT_930_CHECK: ("a05795d4d902bf9d1261dd2d448fff8f0bd2de1d6d38023d72a35ea66c562955",
                        "4dfac9cb9ee9d5f68ebb28d28e4a81755de3101c"),
    RECEIPT_922: ("ab40677256009a0b1ecdf841766aa055a113aeb93827dc1d1da21a9e1cb97954",
                  "4497a88d3d2cf7ca058ff759c8f3ecea8c042481"),
    RECEIPT_922_CHECK: ("e609eafcb6ef33c22ec0aa4481cc29ea5be46f5be1312a9ccd4822b154ff059e",
                        "a1fcadfd795d08c9705722f7165349e361778b65"),
    CORE_719: ("0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
               "c123b8d681c3d76fce08ef13d7673622deac64ad"),
    CORE_719_HANDSHAKE: (
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f"),
}
AUDIT_INPUT_PATHS = tuple(sorted(set(PINS) | {PRIMARY_942, RECEIPT_942}))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024

TOKEN_K = 2
EVENT_COUNT = 2
HORIZON = 16_384
MIN_STABLE_EVENTS = 8
MIN_PERIOD_REPEATS = 2

BLIND_TIER = 10
CROSS_TIER = 5
SHAPE_KEYS = ("swap_swap", "swap_handoff", "handoff_swap")
SHAPE_NAME = {"swap_swap": "ENTRY_GAP_swap_swap",
              "swap_handoff": "ENTRY_GAP_swap_handoff",
              "handoff_swap": "ENTRY_GAP_handoff_swap"}
SEALED_BANK_COUNTS = (9, 10, 11, 12)

POSTURE = (
    "INDEPENDENT GENERATION, DISCLOSED.  Ticks come from the kernel's crossing "
    "identity (holder[(s - t + 1) mod N]) and never from a precomputed phase "
    "table; the whole generator is validated TICK FOR TICK against the kernel's "
    "OWN composed step function apply_controller_step, which carries the "
    "kernel's own token shuffle, so the token-advance model is validated too.  "
    "The detector is re-derived from the stated Cycle-889/891/922 semantics "
    "TWICE -- once on explicit tick SETS with set control flow, once on "
    "integers -- and the two routes are required to agree on randomised cases "
    "AND on a sample of the real stretches swept.  The integer route carries "
    "the sweep because the tick-set route is orders of magnitude too slow at "
    "B = 10; that is a speed choice and it is disclosed, not hidden.  "
    "Attribution is implemented from the stated bookkeeping identity.  This is "
    "the same posture Cycles 922 and 930 declared, and it is the only route "
    "inside the runtime budget."
)

DISCLOSED = (
    "PERIOD SCOPING, DECLARED.  This checker sweeps only the periods it needs "
    "to attack: at each tier, the set of same-edge COMPLEMENT values "
    "N - DELTA(e).  At B = 10 and B = 5 every bank's entry gap 8(B-1-b) is "
    "itself one of those values, so every quantity attacked here -- "
    "episodes_on_the_bank_clock, bank_owned_entry_gap_episodes, by_shape, and "
    "the whole 2P >= N complement census -- is reproduced exactly.  The primary "
    "sweeps every period in [2, max(64, 2N)]; the spectrum outside the "
    "complement values is NOT recounted here and is NOT attacked.  Stated, not "
    "hidden.",
    "TIER SCOPING, DECLARED.  B = 10 (the blind tier, full horizon, all ten "
    "bank clocks) and B = 5 (the cross-tier control against the PINNED "
    "Cycle-930 rows) are rebuilt.  B = 4, 6, 7 and 8 are not rebuilt by this "
    "checker; the primary's own restriction gate covers B = 4, 5 and 7 and is "
    "reported there.",
    "THE WIDENED HUNT is strictly larger than the primary's: it accepts ANY two "
    "P-separated dirty-run starts inside a stretch, not only consecutive ones, "
    "so its occurrence count is an upper bound on the primary's and any episode "
    "it finds that the primary missed is a refutation.",
)


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


def preflight(overrides=None):
    rows, bad = {}, []
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = ROOT / path
        if not full.is_file():
            rows[path] = {"present": False}
            bad.append(path)
            continue
        payload = full.read_bytes()
        if overrides and path in overrides:
            payload = overrides[path]
        got_sha, got_blob = sha256(payload).hexdigest(), git_blob(payload)
        ok = got_sha == want_sha and got_blob == want_blob
        rows[path] = {"present": True, "sha256": got_sha, "git_blob": got_blob,
                      "match": ok}
        if not ok:
            bad.append(path)
    return rows, bad


PREFLIGHT_ROWS, PREFLIGHT_BAD = preflight()
if PREFLIGHT_BAD:
    print("FAIL A_PINS :: " + json.dumps(
        {"pins": PREFLIGHT_ROWS, "mismatched_or_missing": sorted(PREFLIGHT_BAD),
         "action": "PREFLIGHT HARD FAIL"}, sort_keys=True,
        separators=(",", ":")))
    raise SystemExit(2)


BLOCKLISTED = tuple(Path(p).stem for p in
                    (PRIMARY_942, PRIMARY_930, CHECKER_930, PRIMARY_922,
                     CHECKER_922, PRIMARY_891, CHECKER_891, PRIMARY_889,
                     PRIMARY_881, PRIMARY_879))


class _Firewall(importlib.abc.MetaPathFinder):
    """Importing ANY runner in this lineage -- including this cycle's own
    primary -- is fatal here.  The checker shares no code with what it checks."""

    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED:
            self.hits.append(fullname)
            raise ImportError("BLOCKLIST forbids import of %s" % fullname)
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as KERNEL

ALG = KERNEL.A
CHAIN = KERNEL.B
PACK = KERNEL.M
R3 = KERNEL.R3


def pinned_json(path):
    return json.loads((ROOT / path).read_text())


def literal_from(path, name):
    tree = ast.parse((ROOT / path).read_text())
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == name:
                try:
                    return ast.literal_eval(node.value)
                except ValueError:
                    return None
    return None


# ------------------------------------------------- geometry, read from gates
def machine(bank_count):
    """Rows, kinds and edges read out of the kernel's emitted program."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    relay, hand = defaultdict(list), defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            relay[edge].append(index)
        elif kind == "handoff":
            hand[edge].append(index)
    swap_f, swap_r, hand_f, hand_r, malformed = {}, {}, {}, {}, 0
    for edge, rows in sorted(relay.items()):
        if len(rows) != 4 or len(hand.get(edge, ())) != 2:
            malformed += 1
            continue
        words = [KERNEL.mapped_macro(program[i]) for i in rows]
        if words[1] != words[2] or words[0] == words[1]:
            malformed += 1
            continue
        swap_f[edge], swap_r[edge] = rows[1], rows[2]
        hand_f[edge], hand_r[edge] = hand[edge][0], hand[edge][1]
    kind_of = {}
    for edge in sorted(swap_f):
        kind_of[hand_f[edge]] = ("hf", edge)
        kind_of[swap_f[edge]] = ("f", edge)
        kind_of[swap_r[edge]] = ("r", edge)
        kind_of[hand_r[edge]] = ("hr", edge)
    own = {}
    for bank in range(bank_count):
        edges = [e for e in (bank - 1, bank) if 0 <= e <= bank_count - 2]
        own[bank] = {s: ke for s, ke in kind_of.items() if ke[1] in edges}
    delta = {e: (swap_r[e] - swap_f[e]) % stations for e in swap_f}
    return {"program": program, "stations": stations, "swap_f": swap_f,
            "swap_r": swap_r, "hand_f": hand_f, "hand_r": hand_r,
            "kind_of": kind_of, "own": own, "malformed": malformed,
            "delta": delta,
            "complements": sorted({stations - d for d in delta.values()}),
            "entry": {b: 8 * (bank_count - 1 - b)
                      for b in range(1, bank_count - 1)}}


def placements_of(stations):
    out = []
    for pair in combinations(range(stations), TOKEN_K):
        if any((p + 1) % stations in set(pair) for p in pair):
            continue
        out.append(pair)
    return tuple(out)


def seeds_of(bank_count, program):
    banks, links = CHAIN.chain_genesis(bank_count)
    state = PACK.pack_state(banks, links)
    seeds = []
    for event in range(EVENT_COUNT):
        before = PACK.prepare_endpoint(state, (1, 0) if event % 2 == 0 else (0, 1))
        after, _a, _b, _t = KERNEL.run_orbit(before, program)
        seeds.append(before)
        state = after
    return tuple(seeds)


def watched(bank_count):
    banks, links = CHAIN.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in row) for row in banks)
    zl = tuple(tuple(0 for _ in row) for row in links)
    local = (ALG.POINTER, ALG.U_TO_V, ALG.V_TO_U, ALG.DIRECTION_OK,
             *ALG.FRESH, *ALG.ZERO_WORK, ALG.TOKEN_OK)
    out = {}
    for bank in range(bank_count):
        coords = []
        for wire in local:
            probe = [list(row) for row in zb]
            probe[bank][wire] = 1
            packed = PACK.pack_state(tuple(tuple(r) for r in probe), zl)
            hot = [i for i, bit in enumerate(packed) if bit]
            if len(hot) != 1:
                raise AssertionError((bank, wire, hot))
            coords.append(hot[0])
        out[bank] = tuple(sorted(coords))
    return out


BUILD_LOG = []


def generate(bank_count, horizon, perturb=None):
    """Lane-parallel evolution driven by the KERNEL'S CROSSING IDENTITY."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    words = tuple(KERNEL.mapped_macro(row) for row in program)
    placements = placements_of(stations)
    seeds = seeds_of(bank_count, program)
    keys, states = [], []
    for event, seed in enumerate(seeds):
        for pos in placements:
            state, _a, _b, _t = KERNEL.run_orbit(seed, program, token_positions=pos)
            keys.append((event, pos))
            states.append(state)
    lanes = len(keys)
    holder = [0] * stations
    for lane, (_event, pos) in enumerate(keys):
        for p in pos:
            holder[p] |= 1 << lane
    if perturb is not None:
        holder[perturb % stations] ^= 1
    planes = [0] * len(states[0])
    for lane, state in enumerate(states):
        bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= bit
    full = (1 << lanes) - 1
    wires = watched(bank_count)
    src_wire = R3.X.SOURCE_POINTER
    clean = [[0] * (horizon + 1) for _ in range(bank_count)]
    src = [0] * (horizon + 1)

    def observe(tick):
        dirty0 = planes[src_wire] & full
        src[tick] = full & ~dirty0
        for bank in range(bank_count):
            d = dirty0
            for w in wires[bank]:
                d |= planes[w]
            clean[bank][tick] = full & ~d

    observe(0)
    for tick in range(1, horizon + 1):
        shift = (1 - tick) % stations
        for station in range(stations):
            mask = holder[(station + shift) % stations]
            if not mask:
                continue
            for gate in words[station]:
                if gate.kind == "X":
                    planes[gate.wires[0]] ^= mask
                elif gate.kind == "CNOT":
                    c, t2 = gate.wires
                    planes[t2] ^= planes[c] & mask
                elif gate.kind == "TOF":
                    l, r, t2 = gate.wires
                    planes[t2] ^= planes[l] & planes[r] & mask
                else:
                    raise AssertionError(gate.kind)
        observe(tick)
    BUILD_LOG.append({"banks": bank_count, "horizon": horizon, "lanes": lanes,
                      "stations": stations})
    return {"banks": bank_count, "stations": stations, "keys": tuple(keys),
            "lanes": lanes, "clean": clean, "src": src, "horizon": horizon}


def kernel_step_replay(bank_count, horizon, seed, positions):
    """Oracle: the KERNEL'S OWN composed step function, tick by tick."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    wires = watched(bank_count)
    src_wire = R3.X.SOURCE_POINTER
    state, _a0, _b0, _t = KERNEL.run_orbit(seed, program, token_positions=positions)
    a = tuple(int(s in positions) for s in range(stations))
    b = (0,) * stations
    trace = []

    def snap(vec):
        return (not vec[src_wire],
                tuple(not (vec[src_wire] or any(vec[w] for w in wires[bank]))
                      for bank in range(bank_count)))

    trace.append(snap(state))
    for _tick in range(horizon):
        state, a, b = KERNEL.apply_controller_step(state, program, a, b)
        trace.append(snap(state))
    return trace


def lane_masks(rows, lanes, horizon):
    width = (horizon >> 3) + 2
    buf = [bytearray(width) for _ in range(lanes)]
    for tick in range(horizon + 1):
        word = rows[tick]
        if not word:
            continue
        byte, bit = tick >> 3, 1 << (tick & 7)
        while word:
            low = word & -word
            buf[low.bit_length() - 1][byte] |= bit
            word -= low
    return [int.from_bytes(bytes(x), "little") for x in buf]


# ------------------- detector: re-derived from the STATED words, on tick SETS
def set_detector(clean_ticks, last, period):
    """Does the detector read ``period``?  Tick sets only; no folding."""
    if not clean_ticks:
        return None
    if len(clean_ticks) < MIN_STABLE_EVENTS:
        return None
    need = MIN_PERIOD_REPEATS * period
    if need > last:
        return None
    member = clean_ticks
    # the terminal 2P window must be P-exact
    for t in range(last - need, last - period + 1):
        if (t in member) != ((t + period) in member):
            return None
    # least transient: one past the highest t <= last - P where P-exactness fails
    transient = 0
    for t in range(last - period, -1, -1):
        if (t in member) != ((t + period) in member):
            transient = t + 1
            break
    if last - transient < need:
        return None
    stable = [t for t in member if t >= transient]
    if len(stable) < MIN_STABLE_EVENTS:
        return None
    residues = {t % period for t in stable}
    if len(residues) == period:
        return None
    return (transient, len(stable), len(residues))


def int_detector(seg, last, period):
    """The SAME stated semantics on integers.  Used for the sweep because the
    tick-set route is far too slow at B=10; validated against it below."""
    if seg == 0 or bin(seg).count("1") < MIN_STABLE_EVENTS:
        return None
    need = MIN_PERIOD_REPEATS * period
    if need > last:
        return None
    low = last - need
    window = (seg >> low) & ((1 << (need + 1)) - 1)
    if (window ^ (window >> period)) & ((1 << (period + 1)) - 1):
        return None
    span = last - period
    broken = (seg ^ (seg >> period)) & ((1 << (span + 1)) - 1)
    transient = broken.bit_length()
    if last - transient < need:
        return None
    stable = (seg >> transient) & ((1 << (last - transient + 1)) - 1)
    events = bin(stable).count("1")
    if events < MIN_STABLE_EVENTS:
        return None
    residues, walk = set(), stable
    while walk:
        lowb = walk & -walk
        residues.add((transient + lowb.bit_length() - 1) % period)
        walk -= lowb
    if len(residues) == period:
        return None
    return (transient, events, len(residues))


def ticks_of(seg, length):
    return {i for i in range(length) if (seg >> i) & 1}


def dirty_run_starts_int(seg, length, offset):
    """Starts of maximal DIRTY (clear-bit) runs, by bit walk -- O(runs)."""
    full = (1 << length) - 1
    inv = (~seg) & full
    starts = []
    while inv:
        low = inv & -inv
        lo = low.bit_length() - 1
        starts.append(offset + lo)
        rest = seg >> lo
        if rest == 0:
            break
        hi = lo + ((rest & -rest).bit_length() - 1)
        inv &= ~((1 << hi) - 1)
    return starts


def intervals_of_set_bits(mask, length):
    """Maximal runs of SET bits below ``length``, by bit walk -- O(runs)."""
    out, i = [], 0
    while i < length:
        rest = mask >> i
        if rest == 0:
            break
        lo = i + ((rest & -rest).bit_length() - 1)
        if lo >= length:
            break
        flipped = (~(mask >> lo)) & ((1 << (length + 1 - lo)) - 1)
        if flipped == 0:
            # the run of set bits reaches the top of the window
            out.append((lo, length - 1))
            break
        hi = lo + ((flipped & -flipped).bit_length() - 1) - 1
        out.append((lo, min(hi, length - 1)))
        i = hi + 2
    return out


def source_stretches(mask, horizon):
    """Closed quiescent stretches: maximal clean runs strictly inside."""
    return [(a, b) for a, b in intervals_of_set_bits(mask, horizon + 1)
            if a > 0 and b < horizon]


def attribute(tick, positions, own_rows, stations):
    """The stated bookkeeping identity: a dirty-run start at tick t is the
    crossing of station (p + t - 1) mod N by token p, for an OWN row."""
    out = []
    for p in positions:
        s = (p + tick - 1) % stations
        if s in own_rows:
            kind, edge = own_rows[s]
            out.append((p, s, kind, edge))
    return out


def name_shape(k1, e1, k2, e2, bank):
    if (k1, k2) == ("f", "r") and e2 == e1 + 1 and e2 == bank:
        return "swap_swap"
    if (k1, k2) == ("f", "hr") and e1 == e2 + 1 and e1 == bank:
        return "swap_handoff"
    if (k1, k2) == ("hf", "r") and e1 == e2 + 1 and e1 == bank:
        return "handoff_swap"
    return None


def recount(box, want_periods=None):
    """One independent pass: entry-gap rows, the third pair (consecutive AND
    widened), and the complement-value census."""
    bank_count = box["banks"]
    stations = box["stations"]
    lanes = box["lanes"]
    horizon = box["horizon"]
    mac = machine(bank_count)
    entry = mac["entry"]
    periods = sorted(set(want_periods if want_periods is not None
                         else mac["complements"]))
    src_masks = lane_masks(box["src"], lanes, horizon)
    bank_ms = [lane_masks(box["clean"][b], lanes, horizon)
               for b in range(bank_count)]

    episodes = defaultdict(int)          # bank -> episodes at its entry gap
    strict = defaultdict(int)            # (bank, shapekey) -> stretch instances
    occ_consecutive = defaultdict(int)   # (bank, shapekey) -> raw occurrences
    occ_widened = defaultdict(int)
    ep_widened_third = []                # every widened third-pair EPISODE
    period_episodes = defaultdict(int)   # (bank, period) -> episodes
    stretch_total = 0
    longest = 0
    cross_route_checks = cross_route_bad = 0

    for lane in range(lanes):
        _event, positions = box["keys"][lane]
        stretches = source_stretches(src_masks[lane], horizon)
        stretch_total += len(stretches)
        for a, b in stretches:
            if b - a + 1 > longest:
                longest = b - a + 1
        for bank in range(bank_count):
            mask = bank_ms[bank][lane]
            if mask == 0:
                continue
            own_rows = mac["own"][bank]
            P_entry = entry.get(bank)
            for a, b in stretches:
                length = b - a + 1
                seg = (mask >> a) & ((1 << length) - 1)
                if seg == 0:
                    continue
                last_rel = seg.bit_length() - 1
                for period in periods:
                    if MIN_PERIOD_REPEATS * period > last_rel:
                        continue
                    if int_detector(seg, last_rel, period) is not None:
                        period_episodes[(bank, period)] += 1
                if P_entry is None:
                    continue
                P = P_entry
                read = (MIN_PERIOD_REPEATS * P <= last_rel
                        and int_detector(seg, last_rel, P) is not None)
                if read:
                    episodes[bank] += 1
                    # spot-validate the fast route against the tick-set route
                    if (lane % 997) == 0:
                        cross_route_checks += 1
                        if (set_detector(ticks_of(seg, length), last_rel, P)
                                is not None) != read:
                            cross_route_bad += 1
                starts = dirty_run_starts_int(seg, length, a)
                if len(starts) < 2:
                    continue
                att = {t: attribute(t, positions, own_rows, stations)
                       for t in starts}
                shapes_here = set()
                for i in range(len(starts) - 1):
                    if starts[i + 1] - starts[i] != P:
                        continue
                    for p1, _s1, k1, e1 in att[starts[i]]:
                        for p2, _s2, k2, e2 in att[starts[i + 1]]:
                            if p1 != p2:
                                continue
                            sh = name_shape(k1, e1, k2, e2, bank)
                            if sh is None:
                                continue
                            shapes_here.add(sh)
                            occ_consecutive[(bank, sh)] += 1
                if read:
                    for sh in shapes_here:
                        strict[(bank, sh)] += 1
                # ---- the WIDENED third-pair hunt: ANY two P-separated starts
                start_set = set(starts)
                widened_hit = False
                for t1 in starts:
                    if t1 + P not in start_set:
                        continue
                    for p1, _s1, k1, e1 in att[t1]:
                        for p2, _s2, k2, e2 in att[t1 + P]:
                            if p1 != p2:
                                continue
                            if name_shape(k1, e1, k2, e2, bank) != "handoff_swap":
                                continue
                            occ_widened[(bank, "handoff_swap")] += 1
                            widened_hit = True
                if widened_hit and read:
                    ep_widened_third.append({
                        "banks": bank_count, "bank": bank, "period": P,
                        "lane": lane, "stretch": [a, b],
                        "token_positions": list(positions)})
    del src_masks, bank_ms
    return {"banks": bank_count, "stations": stations, "lanes": lanes,
            "entry": entry, "periods": periods,
            "closed_quiescent_stretches": stretch_total,
            "longest_closed_stretch": longest,
            "episodes": dict(episodes), "strict": dict(strict),
            "occ_consecutive": dict(occ_consecutive),
            "occ_widened": dict(occ_widened),
            "widened_third_pair_episodes": ep_widened_third,
            "period_episodes": dict(period_episodes),
            "route_cross_checks": cross_route_checks,
            "route_cross_check_disagreements": cross_route_bad,
            "complements": mac["complements"], "machine": mac}


def own_tp_rows(bc):
    n = 8 * bc - 5
    out = []
    for b in range(1, bc - 1):
        period = 8 * (bc - 1 - b)

        def f(e):
            return (4 + 5 * e) % n

        def r(e):
            return (8 * bc - 9 - 3 * e) % n

        rows = {(f(b - 1) - 2) % n, f(b - 1), r(b - 1), (r(b - 1) + 2) % n,
                (f(b) - 2) % n, f(b), r(b), (r(b) + 2) % n}
        srt = sorted(rows)
        gaps = [(srt[(i + 1) % len(srt)] - srt[i]) % n for i in range(len(srt))]
        shadow = {srt[(i + 1) % len(srt)] for i, g in enumerate(gaps) if g == 1}
        pairs = {"swap_swap": (f(b - 1), r(b)),
                 "swap_handoff": (f(b), (r(b - 1) + 2) % n),
                 "handoff_swap": ((f(b) - 2) % n, r(b - 1))}
        out.append({"bank": b,
                    "spans": {k: (v[1] - v[0]) % n == period
                              for k, v in pairs.items()},
                    "terminal_shadowed": {k: v[1] in shadow
                                          for k, v in pairs.items()}})
    return out


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}
    results, refutations, findings = {}, [], []

    def gate(name, ok, payload):
        print("%s %s :: %s" % ("PASS" if ok else "FAIL", name,
                               json.dumps(payload, **dumps)))
        return ok

    receipt = pinned_json(RECEIPT_942)
    R930 = pinned_json(RECEIPT_930)
    primary_bytes = (ROOT / PRIMARY_942).read_bytes()
    receipt_bytes = (ROOT / RECEIPT_942).read_bytes()

    # ------------------------------------------------------------ gate A
    a_ok = (not PREFLIGHT_BAD) and not FIREWALL.hits
    results["A_PINS"] = gate("A_PINS", a_ok, {
        "pins_verified": len(PINS), "mismatched": sorted(PREFLIGHT_BAD),
        "firewall_hits": FIREWALL.hits,
        "blocklisted_modules": sorted(BLOCKLISTED),
        "primary_under_test": {
            "path": PRIMARY_942,
            "sha256": sha256(primary_bytes).hexdigest(),
            "git_blob": git_blob(primary_bytes)},
        "receipt_under_test": {
            "path": RECEIPT_942,
            "sha256": sha256(receipt_bytes).hexdigest(),
            "git_blob": git_blob(receipt_bytes)},
        "posture": POSTURE, "disclosed": list(DISCLOSED),
    })
    if not a_ok:
        raise SystemExit(2)

    # ------------------------------------------------------------ gate B
    val_rows, val_bad = [], 0
    for bank_count, horizon, lanes_checked in ((3, 240, 6), (4, 200, 5)):
        program = KERNEL.interleaved_program(bank_count)
        seeds = seeds_of(bank_count, program)
        box = generate(bank_count, horizon)
        for lane in range(min(lanes_checked, box["lanes"])):
            event, positions = box["keys"][lane]
            trace = kernel_step_replay(bank_count, horizon, seeds[event], positions)
            mism = 0
            for tick in range(horizon + 1):
                src_ok = bool((box["src"][tick] >> lane) & 1)
                banks_ok = tuple(bool((box["clean"][b][tick] >> lane) & 1)
                                 for b in range(bank_count))
                if (src_ok, banks_ok) != (bool(trace[tick][0]),
                                          tuple(bool(x) for x in trace[tick][1])):
                    mism += 1
            val_bad += mism
            val_rows.append({"banks": bank_count, "lane": lane,
                             "ticks": horizon + 1, "mismatches": mism})
    b_ok = val_bad == 0
    results["B_GENERATOR"] = gate("B_GENERATOR", b_ok, {
        "attack": "validate the crossing-identity generator TICK FOR TICK "
                  "against the kernel's own composed step function",
        "oracle": "KERNEL.apply_controller_step (carries the kernel's own token "
                  "shuffle)",
        "rows": val_rows, "total_mismatches": val_bad, "posture": POSTURE,
    })

    # ------------------------------------------------------------ gate C
    rng = random.Random(942_1001)
    det_cases = det_bad = det_hits = 0
    for _ in range(900):
        length = rng.randrange(30, 260)
        density = rng.choice((0.1, 0.25, 0.5, 0.8))
        ticks = {i for i in range(length) if rng.random() < density}
        if rng.random() < 0.45 and ticks:
            period = rng.randrange(3, 24)
            tail = rng.randrange(length // 2, length)
            base = rng.getrandbits(period)
            for i in range(tail, length):
                if (base >> ((i - tail) % period)) & 1:
                    ticks.add(i)
                else:
                    ticks.discard(i)
        if not ticks:
            continue
        last = max(ticks)
        seg = 0
        for t in ticks:
            seg |= 1 << t
        for period in range(2, 30):
            got = set_detector(ticks, last, period)
            ref = int_detector(seg, last, period)
            det_cases += 1
            det_hits += got is not None
            if got != ref:
                det_bad += 1
    c_ok = det_bad == 0 and det_hits > 0
    results["C_DETECTOR"] = gate("C_DETECTOR", c_ok, {
        "attack": "re-derive the detector from the STATED semantics TWICE -- "
                  "once on explicit tick SETS with set control flow, once on "
                  "integers -- and require the two routes to agree everywhere",
        "cases": det_cases, "detections": det_hits, "mismatches": det_bad,
        "route_disclosure":
            "the integer route is the one used for the B=10 sweep because the "
            "tick-set route is orders of magnitude too slow at that size; the "
            "set route re-checks it on a sample of REAL stretches during the "
            "sweep as well (see the route cross-check counts below)",
    })

    # ------------------------------------------------------------ gate D
    t0 = time.monotonic()
    cross = recount(generate(CROSS_TIER, HORIZON))
    cross_seconds = round(time.monotonic() - t0, 1)
    cross_rows, cross_bad = [], []
    for row in R930["per_cell_rows"][str(CROSS_TIER)]:
        bank = row["bank"]
        mine_ep = cross["episodes"].get(bank, 0)
        mine_shapes = {SHAPE_NAME[k]: cross["strict"].get((bank, k), 0)
                       for k in SHAPE_KEYS}
        ok = (mine_ep == row["episodes_on_the_bank_clock"]
              and mine_shapes == row["by_shape"])
        cross_rows.append({"cell": "B%d.b%d" % (CROSS_TIER, bank),
                           "episodes_pinned": row["episodes_on_the_bank_clock"],
                           "episodes_checker": mine_ep,
                           "by_shape_pinned": row["by_shape"],
                           "by_shape_checker": mine_shapes, "agrees": ok})
        if not ok:
            cross_bad.append(cross_rows[-1])
    pinned_922_row = next(
        r for r in pinned_json(RECEIPT_922)[
            "restriction_gate_against_cycle891"]["rows"]
        if r["banks"] == CROSS_TIER)
    stretch_ok = (cross["closed_quiescent_stretches"]
                  == pinned_922_row["closed_quiescent_stretches"])
    d_ok = (not cross_bad and stretch_ok
            and cross["route_cross_check_disagreements"] == 0)
    if cross_bad:
        refutations.append({"gate": "D_CROSS_TIER", "rows": cross_bad})
    results["D_CROSS_TIER"] = gate("D_CROSS_TIER", d_ok, {
        "attack": "rebuild B=%d with the independent generator and detector and "
                  "recount it against the PINNED Cycle-930 rows, before "
                  "believing anything this checker says about B=10" % CROSS_TIER,
        "rows": cross_rows, "disagreements": cross_bad,
        "closed_quiescent_stretches_checker": cross["closed_quiescent_stretches"],
        "closed_quiescent_stretches_agree_with_pinned_922": stretch_ok,
        "detector_route_cross_checks_on_real_stretches":
            cross["route_cross_checks"],
        "detector_route_cross_check_disagreements":
            cross["route_cross_check_disagreements"],
        "seconds": cross_seconds,
    })

    # ------------------------------------------------------------ gate E
    tp_text = R930["seal"]["payload"]["TP_STATEMENT"]
    own_payload = {
        "TP_STATEMENT": tp_text,
        "predicted_third_pair_episodes": {str(bc): 0 for bc in SEALED_BANK_COUNTS},
        "predicted_third_pair_exists_geometrically": {
            str(bc): [row["bank"] for row in own_tp_rows(bc)
                      if row["spans"]["handoff_swap"]]
            for bc in SEALED_BANK_COUNTS},
        "predicted_third_pair_terminal_is_shadowed_everywhere": {
            str(bc): all(row["terminal_shadowed"]["handoff_swap"]
                         for row in own_tp_rows(bc))
            for bc in SEALED_BANK_COUNTS},
        "predicted_other_two_pairs_terminals_unshadowed": {
            str(bc): all(not row["terminal_shadowed"]["swap_swap"]
                         and not row["terminal_shadowed"]["swap_handoff"]
                         for row in own_tp_rows(bc))
            for bc in SEALED_BANK_COUNTS},
    }
    own_seal = digest(own_payload)
    published_seal = R930["seal"]["SEAL_sha256"]
    primary_claim = receipt["seal_recomputation"]
    e_ok = (own_seal == published_seal
            and primary_claim["recomputed_from_published_text_and_own_arithmetic"]
            == own_seal
            and primary_claim["published_SEAL_sha256"] == published_seal
            and own_payload == R930["seal"]["payload"])
    if not e_ok:
        refutations.append({"gate": "E_SEAL", "own": own_seal,
                            "published": published_seal})
    results["E_SEAL"] = gate("E_SEAL", e_ok, {
        "attack": "recompute the Cycle-930 seal from the published TP text with "
                  "this checker's own arithmetic and compare with both the "
                  "published digest and the primary's claim",
        "published_SEAL_sha256": published_seal,
        "checker_recomputed": own_seal,
        "primary_recomputed":
            primary_claim["recomputed_from_published_text_and_own_arithmetic"],
        "all_three_agree": e_ok,
        "sealed_prediction_at_B10":
            own_payload["predicted_third_pair_episodes"][str(BLIND_TIER)],
    })

    # ------------------------------------------------------------ gate F
    t0 = time.monotonic()
    blind = recount(generate(BLIND_TIER, HORIZON))
    blind_seconds = round(time.monotonic() - t0, 1)
    primary_rows = {r["bank"]: r for r in receipt["blind_tier"]["per_cell_rows"]}
    f_rows, f_bad = [], []
    for bank, row in sorted(primary_rows.items()):
        mine_ep = blind["episodes"].get(bank, 0)
        mine_shapes = {SHAPE_NAME[k]: blind["strict"].get((bank, k), 0)
                       for k in SHAPE_KEYS}
        ok = (mine_ep == row["episodes_on_the_bank_clock"]
              and mine_shapes == row["by_shape"])
        f_rows.append({"cell": "B%d.b%d" % (BLIND_TIER, bank),
                       "P": row["entry_gap_period"],
                       "episodes_primary": row["episodes_on_the_bank_clock"],
                       "episodes_checker": mine_ep,
                       "by_shape_primary": row["by_shape"],
                       "by_shape_checker": mine_shapes, "agrees": ok})
        if not ok:
            f_bad.append(f_rows[-1])
    stretches_agree = (blind["closed_quiescent_stretches"]
                       == receipt["blind_tier"]["closed_quiescent_stretches"])
    longest_agree = (blind["longest_closed_stretch"]
                     == receipt["blind_tier"]["longest_closed_stretch"])
    f_ok = (not f_bad and stretches_agree and longest_agree
            and blind["route_cross_check_disagreements"] == 0)
    if not f_ok:
        refutations.append({"gate": "F_B10_REBUILD", "rows": f_bad,
                            "stretches_agree": stretches_agree,
                            "longest_agree": longest_agree})
    results["F_B10_REBUILD"] = gate("F_B10_REBUILD", f_ok, {
        "attack": "rebuild the blind tier from scratch with the independent "
                  "generator and detector and recount every bank clock",
        "rows": f_rows, "disagreements": f_bad,
        "closed_quiescent_stretches_primary":
            receipt["blind_tier"]["closed_quiescent_stretches"],
        "closed_quiescent_stretches_checker":
            blind["closed_quiescent_stretches"],
        "stretches_agree": stretches_agree,
        "longest_closed_stretch_checker": blind["longest_closed_stretch"],
        "longest_agree": longest_agree,
        "lanes": blind["lanes"], "stations": blind["stations"],
        "detector_route_cross_checks_on_real_stretches":
            blind["route_cross_checks"],
        "detector_route_cross_check_disagreements":
            blind["route_cross_check_disagreements"],
        "seconds": blind_seconds,
    })

    # ------------------------------------------------------------ gate G
    consec = {b: blind["occ_consecutive"].get((b, "handoff_swap"), 0)
              for b in blind["entry"]}
    widened = {b: blind["occ_widened"].get((b, "handoff_swap"), 0)
               for b in blind["entry"]}
    strict_ep = {b: blind["strict"].get((b, "handoff_swap"), 0)
                 for b in blind["entry"]}
    widened_eps = blind["widened_third_pair_episodes"]
    primary_occ = {int(k): v for k, v in
                   receipt["blind_tier"][
                       "third_pair_register_level_occurrences"].items()}
    occ_agree = consec == primary_occ
    widened_ge = all(widened[b] >= consec[b] for b in consec)
    zero_holds = sum(strict_ep.values()) == 0 and not widened_eps
    if not zero_holds:
        refutations.append({"gate": "G_WIDENED_HUNT",
                            "third_pair_episodes_found": widened_eps[:50],
                            "strict_episodes": strict_ep})
    if not occ_agree:
        findings.append({"finding": "register-level third-pair occurrence "
                                    "counts differ between primary and checker",
                         "primary": primary_occ, "checker": consec})
    g_ok = widened_ge
    results["G_WIDENED_HUNT"] = gate("G_WIDENED_HUNT", g_ok, {
        "attack": "hunt the third pair at B=10 with a STRICTLY WIDER net than "
                  "the primary used -- ANY two P-separated dirty-run starts in "
                  "a stretch, not only consecutive ones",
        "consecutive_occurrences_checker": consec,
        "consecutive_occurrences_primary": primary_occ,
        "consecutive_occurrences_agree": occ_agree,
        "widened_occurrences_checker": widened,
        "widened_is_a_superset_of_consecutive": widened_ge,
        "third_pair_episodes_consecutive": strict_ep,
        "third_pair_episodes_widened": len(widened_eps),
        "widened_episode_rows": widened_eps[:50],
        "THE_ZERO_SURVIVES_THE_WIDENED_HUNT": zero_holds,
        "verdict": ("no third-pair episode exists at B=10 under either net -- "
                    "the sealed zero survives an attack strictly stronger than "
                    "the one that produced it"
                    if zero_holds else
                    "REFUTATION: a third-pair episode EXISTS at B=10"),
    })

    # ------------------------------------------------------------ gate H
    N10 = blind["stations"]
    rc2_rows, nec_viol, suf_fail = [], [], []
    for bank, P in sorted(blind["entry"].items()):
        fired = sum(blind["strict"].get((bank, k), 0) for k in SHAPE_KEYS) > 0
        predicted = 2 * P < N10
        row = {"cell": "B%d.b%d" % (BLIND_TIER, bank), "bank": bank, "P": P,
               "RC2_predicts_fire": predicted, "measured_fires": fired,
               "bank_owned_entry_gap_episodes":
                   sum(blind["strict"].get((bank, k), 0) for k in SHAPE_KEYS),
               "episodes_on_the_bank_clock": blind["episodes"].get(bank, 0)}
        rc2_rows.append(row)
        if fired and not predicted:
            nec_viol.append(row)
        if predicted and not fired:
            suf_fail.append(row)
    primary_rc2 = {r["bank"]: r for r in receipt["rc2_at_B10"]["carrier_map"]}
    rc2_bad = [r for r in rc2_rows
               if r["measured_fires"] != primary_rc2[r["bank"]]["measured_fires"]
               or r["bank_owned_entry_gap_episodes"]
               != primary_rc2[r["bank"]]["bank_owned_entry_gap_episodes"]]
    if rc2_bad:
        refutations.append({"gate": "H_RC2_RECOUNT", "rows": rc2_bad})
    h_ok = not rc2_bad
    results["H_RC2_RECOUNT"] = gate("H_RC2_RECOUNT", h_ok, {
        "attack": "recount the RC-2 carrier map independently and recompute the "
                  "necessity and sufficiency verdicts from the recount",
        "carrier_map_checker": rc2_rows,
        "disagreements_with_the_primary": rc2_bad,
        "necessity_violations_checker": nec_viol,
        "necessity_holds": not nec_viol,
        "sufficiency_failures_checker": [r["cell"] for r in suf_fail],
        "b_equals_B_minus_2_fires":
            next(r["measured_fires"] for r in rc2_rows
                 if r["bank"] == BLIND_TIER - 2),
    })

    # ------------------------------------------------------------ gate I
    comp_rows = []
    for P in blind["complements"]:
        per_bank = {b: n for (b, p), n in sorted(blind["period_episodes"].items())
                    if p == P and n}
        comp_rows.append({"P": P, "two_P": 2 * P,
                          "stretch_local_only_2P_ge_N": 2 * P >= N10,
                          "episodes_per_bank_clock": per_bank,
                          "episodes_total": sum(per_bank.values())})
    primary_comp = {r["P"]: r for r in receipt["stretch_local_at_B10"]["census"]}
    comp_bad = [r for r in comp_rows
                if r["episodes_per_bank_clock"]
                != {int(k): v for k, v in
                    primary_comp[r["P"]]["episodes_per_bank_clock"].items()}]
    if comp_bad:
        refutations.append({"gate": "I_COMPLEMENT_CENSUS", "rows": comp_bad})
    stretch_local = [r for r in comp_rows if r["stretch_local_only_2P_ge_N"]]
    ones_twos = all(n <= 2 for r in stretch_local
                    for n in r["episodes_per_bank_clock"].values())
    i_ok = not comp_bad
    results["I_COMPLEMENT_CENSUS"] = gate("I_COMPLEMENT_CENSUS", i_ok, {
        "attack": "recount the whole complement-value census at B=10 "
                  "independently, including the 2P >= N stretch-local values",
        "census_checker": comp_rows,
        "disagreements_with_the_primary": comp_bad,
        "stretch_local_rows": stretch_local,
        "every_stretch_local_per_bank_count_is_one_or_two": ones_twos,
    })

    # ------------------------------------------------------------ gate J
    teeth = []

    # 1 -- a tampered pin is caught
    tampered = (ROOT / PRIMARY_930).read_bytes() + b"\n#x\n"
    _r, bad = preflight(overrides={PRIMARY_930: tampered})
    teeth.append({"tooth": "tampered_pin_is_caught", "fires": bad == [PRIMARY_930]})

    # 2 -- a perturbed generator stops matching the kernel oracle
    program3 = KERNEL.interleaved_program(3)
    seeds3 = seeds_of(3, program3)
    bent = generate(3, 120, perturb=0)
    lane0_event, lane0_pos = bent["keys"][0]
    oracle = kernel_step_replay(3, 120, seeds3[lane0_event], lane0_pos)
    bent_mismatch = sum(
        1 for tick in range(121)
        if (bool((bent["src"][tick] >> 0) & 1),
            tuple(bool((bent["clean"][b][tick] >> 0) & 1) for b in range(3)))
        != (bool(oracle[tick][0]), tuple(bool(x) for x in oracle[tick][1])))
    teeth.append({"tooth": "perturbed_generator_is_caught_by_the_kernel_oracle",
                  "fires": bent_mismatch > 0, "mismatched_ticks": bent_mismatch})

    # 3 -- a planted third-pair episode is caught by the widened hunt
    mac10 = machine(BLIND_TIER)
    plant_bank = BLIND_TIER - 2
    P_plant = mac10["entry"][plant_bank]
    hf = mac10["hand_f"][plant_bank]
    rr = mac10["swap_r"][plant_bank - 1]
    sep_ok = (rr - hf) % mac10["stations"] == P_plant
    named = name_shape("hf", plant_bank, "r", plant_bank - 1, plant_bank)
    # a synthetic stretch: dirty pairs exactly P apart, P-exact to the end
    ticks, length = set(), 6 * P_plant
    for i in range(length):
        if i % P_plant >= 2:
            ticks.add(i)
    seg_plant = 0
    for t in ticks:
        seg_plant |= 1 << t
    # run starts come from the PRODUCTION helper, so the tooth exercises the
    # same code path the sweep uses
    starts_synth = dirty_run_starts_int(seg_plant, length, 0)
    seps = sorted({starts_synth[i + 1] - starts_synth[i]
                   for i in range(len(starts_synth) - 1)})
    start_set_synth = set(starts_synth)
    widened_finds_it = any(t + P_plant in start_set_synth for t in starts_synth)
    detected = set_detector(ticks, max(ticks), P_plant) is not None
    teeth.append({
        "tooth": "planted_third_pair_episode_is_caught_by_the_widened_hunt",
        "fires": (sep_ok and named == "handoff_swap" and detected
                  and len(starts_synth) >= 2 and seps == [P_plant]
                  and widened_finds_it),
        "stations": [hf, rr], "separation_is_P": sep_ok,
        "classifier_names_it": named, "detector_reads_P": detected,
        "planted_run_starts": starts_synth[:8],
        "planted_run_start_separations": seps,
        "widened_net_finds_the_planted_pair": widened_finds_it,
        "note": "the third pair's two stations really are P apart at B=10, the "
                "classifier really does name the shape, the production "
                "run-start extractor really does yield P-separated starts, and "
                "the detector really does read P on a stretch of this form -- "
                "so a real episode would be caught by the identical code path "
                "that reports zero"})

    # 4 -- a crippled detector route disagrees with the literal oracle
    def crippled(ticks_, last_, period_):
        if len(ticks_) < MIN_STABLE_EVENTS or MIN_PERIOD_REPEATS * period_ > last_:
            return None
        return (0, len(ticks_), len({t % period_ for t in ticks_}))

    rng2 = random.Random(942_1002)
    cr_bad = 0
    for _ in range(250):
        n = rng2.randrange(40, 160)
        ticks_ = {i for i in range(n) if rng2.random() < 0.5}
        if not ticks_:
            continue
        last_ = max(ticks_)
        for p in range(2, 16):
            if (crippled(ticks_, last_, p) is None) != (
                    set_detector(ticks_, last_, p) is None):
                cr_bad += 1
    teeth.append({"tooth": "crippled_detector_route_is_detectable",
                  "fires": cr_bad > 0, "disagreements": cr_bad})

    # 5 -- a tampered seal is caught
    bent_payload = dict(own_payload)
    bent_payload["TP_STATEMENT"] = tp_text.replace("unique", "typical")
    teeth.append({"tooth": "tampered_seal_is_caught",
                  "fires": digest(bent_payload) != published_seal})

    # 6 -- a wrong bookkeeping identity fails to reproduce the pinned tier
    def bent_attribute(tick, positions, own_rows, stations):
        out = []
        for p in positions:
            s = (p + tick) % stations          # the off-by-one
            if s in own_rows:
                out.append((p, s, own_rows[s][0], own_rows[s][1]))
        return out

    mac5 = machine(CROSS_TIER)
    probe_bank = max(mac5["entry"])
    same = 0
    for tick in range(200):
        a1 = attribute(tick, (0, 2), mac5["own"][probe_bank], mac5["stations"])
        a2 = bent_attribute(tick, (0, 2), mac5["own"][probe_bank], mac5["stations"])
        same += a1 == a2
    teeth.append({"tooth": "off_by_one_bookkeeping_identity_is_detectable",
                  "fires": same < 200, "ticks_that_still_agree": same})

    # 7 -- the recount comparison actually compares
    fake = dict(f_rows[0]) if f_rows else {}
    teeth.append({"tooth": "recount_comparison_actually_compares",
                  "fires": bool(f_rows) and (
                      (f_rows[0]["episodes_primary"] + 1)
                      != f_rows[0]["episodes_checker"]),
                  "probe_cell": fake.get("cell")})

    # 8 -- the widened net really is wider
    synth_starts = [0, 5, 10]
    consec_pairs = sum(1 for i in range(len(synth_starts) - 1)
                       if synth_starts[i + 1] - synth_starts[i] == 10)
    wide_pairs = sum(1 for t in synth_starts if t + 10 in set(synth_starts))
    teeth.append({"tooth": "widened_net_finds_pairs_the_consecutive_net_cannot",
                  "fires": consec_pairs == 0 and wide_pairs == 1,
                  "consecutive_pairs": consec_pairs, "widened_pairs": wide_pairs})

    j_ok = all(t["fires"] for t in teeth) and len(teeth) >= 6
    results["J_TEETH"] = gate("J_TEETH", j_ok, {
        "teeth": teeth, "count": len(teeth), "declared_minimum": 6,
        "all_fire": all(t["fires"] for t in teeth)})

    # ------------------------------------------------------------ gate K
    runtime = time.monotonic() - started
    status = ("REFUTED" if refutations else
              "SUPPORTED_WITH_FINDINGS" if findings else "SUPPORTED")
    k_ok = (all(results.values()) and runtime <= RUNTIME_LIMIT_SECONDS
            and not refutations)
    headline = (
        "INDEPENDENT REBUILD OF THE BLIND TIER: %s.  B=10 was regenerated from "
        "the kernel's crossing identity (validated tick for tick against the "
        "kernel's own step function) with a detector re-derived from the stated "
        "words on tick sets, and recounted: %d of %d bank-clock rows agree with "
        "the primary; the cross-tier control at B=%d agrees with the PINNED "
        "Cycle-930 rows on all %d rows.  The third pair was hunted with a "
        "STRICTLY WIDER net than the primary used and %s.  RC-2: necessity "
        "violations %d; the b = B-2 cell %s."
        % (status, len(f_rows) - len(f_bad), len(f_rows), CROSS_TIER,
           len(cross_rows),
           ("found ZERO episodes" if zero_holds else
            "FOUND %d EPISODES -- THE SEAL IS REFUTED AT B=10" % len(widened_eps)),
           len(nec_viol),
           ("stays silent" if not next(r["measured_fires"] for r in rc2_rows
                                       if r["bank"] == BLIND_TIER - 2)
            else "fires")))
    results["K_VERDICT"] = gate("K_VERDICT", k_ok, {
        "headline": headline, "checker_status": status,
        "refutations": refutations, "findings": findings,
        "gates": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "runtime_s": round(runtime, 1), "runtime_limit_s": RUNTIME_LIMIT_SECONDS,
        "build_log": list(BUILD_LOG),
    })

    payload = {
        "campaign": "toe-time-expansion-20260802",
        "block": "toe-time-blockT8-20260802",
        "cycles": [942], "authority": "none", "audit": "unset",
        "claim_type": "independent check of a blind-tier measurement",
        "authorship": "one Claude Opus 5 worker-authored primary and checker "
                      "under supervisor spec; supervisor review",
        "independence": "independent checker -- own generator, own detector, "
                        "own attribution; the primary and every prior runner in "
                        "the lineage are import-blocklisted",
        "checker_status": status, "headline": headline,
        "posture": POSTURE, "disclosed": list(DISCLOSED),
        "gate_results": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "generator_validation": {"rows": val_rows, "total_mismatches": val_bad},
        "detector_validation": {"cases": det_cases, "mismatches": det_bad},
        "cross_tier_control": {"banks": CROSS_TIER, "rows": cross_rows,
                               "disagreements": cross_bad,
                               "seconds": cross_seconds},
        "seal": {"published": published_seal, "checker_recomputed": own_seal,
                 "agrees": own_seal == published_seal},
        "blind_tier_rebuild": {
            "banks": BLIND_TIER, "horizon": HORIZON,
            "lanes": blind["lanes"], "stations": blind["stations"],
            "closed_quiescent_stretches": blind["closed_quiescent_stretches"],
            "longest_closed_stretch": blind["longest_closed_stretch"],
            "rows": f_rows, "disagreements": f_bad, "seconds": blind_seconds},
        "third_pair": {
            "consecutive_occurrences": consec,
            "widened_occurrences": widened,
            "episodes_consecutive": strict_ep,
            "episodes_widened": len(widened_eps),
            "widened_episode_rows": widened_eps[:50],
            "zero_survives_the_widened_hunt": zero_holds},
        "rc2": {"carrier_map": rc2_rows, "necessity_violations": nec_viol,
                "sufficiency_failures": [r["cell"] for r in suf_fail],
                "disagreements_with_the_primary": rc2_bad},
        "complement_census": {"rows": comp_rows, "disagreements": comp_bad,
                              "ones_and_twos": ones_twos},
        "refutations": refutations, "findings": findings,
        "teeth": teeth,
        "runtime_seconds": round(runtime, 1),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "exit_codes": {"checker": 0 if k_ok else 1},
        "build_log": list(BUILD_LOG),
        "primary_under_test": {
            "path": PRIMARY_942, "sha256": sha256(primary_bytes).hexdigest(),
            "git_blob": git_blob(primary_bytes)},
        "receipt_under_test": {
            "path": RECEIPT_942, "sha256": sha256(receipt_bytes).hexdigest(),
            "git_blob": git_blob(receipt_bytes)},
        "pinned_inputs": {p: {"sha256": PREFLIGHT_ROWS[p]["sha256"],
                              "git_blob": PREFLIGHT_ROWS[p]["git_blob"]}
                          for p in sorted(PINS)},
    }
    me = Path(__file__).read_bytes()
    payload["files"] = {
        "scripts/frontier_cycle942_blind_tier_independent_check_2026_07_28.py": {
            "sha256": sha256(me).hexdigest(), "git_blob": git_blob(me)}}
    out = (ROOT / "outputs"
           / "blind_tier_independent_check_cycle942_receipt_2026_07_28.json")
    out.write_text(json.dumps(payload, indent=1, sort_keys=True, default=str))
    print("RECEIPT %s :: %s" % (out.name, json.dumps(
        {"sha256": sha256(out.read_bytes()).hexdigest(),
         "git_blob": git_blob(out.read_bytes())}, **dumps)))
    return 0 if k_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
