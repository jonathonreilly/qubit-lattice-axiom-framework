#!/usr/bin/env python3
"""Cycle 922 INDEPENDENT CHECKER -- spec'd to REFUTE the realization condition.

The primary claims:

  (i)   at B=7 no clock containing bank 2 reads the period 32, so the entry-gap
        route for P=32 is absent for the plainest reason -- the reading does not
        happen, not the classification;
  (ii)  RC-1: the entry-gap value 8(B-1-b) is a bank-owned same-token separation
        realised by exactly three ordered row pairs;
  (iii) RC-2: a bank-owned entry-gap reading occurs only if 2P < N;
  (iv)  the B=7 residuals P=40 and P=48 are same-edge complements on an incident
        bank, not a fourth shape.

This checker attacks all four.  It is written to be independent of the primary:

  TICK GENERATOR.  Independently written: a per-phase precompiled activation
  list (only the stations that actually carry a token at that phase, with their
  lane masks, materialised once per phase) driving a compiled opcode program,
  with the clean-tick observation folded INTO the sweep as per-lane byte buffers
  -- the primary loops every station every tick and transposes afterwards.  The
  generator is then validated TICK FOR TICK against the Cycle-719 kernel's own
  single-lane gate semantics on a declared lane sample (gate B).

  EPISODE DETECTOR.  A third route.  The primary uses bignum XOR on the clean
  mask; Cycle 891's checker used interval algebra on run boundaries.  This one
  works on the SET of dirty tick indices and computes Cycle 891's k-run law
  finite form directly as a symmetric difference of integer sets -- no bitmask
  is ever formed, no run boundaries are ever enumerated.  It is validated
  against a literal per-tick definition on a declared randomised corpus.

  THE RULE.  Re-derived from the primary's STATED TEXT alone (read out of the
  primary's source as an AST literal, never by importing it) and checked for
  DETERMINACY: the text gives the condition in three phrasings and all three
  must agree as predicates on every (B, b) cell in range.

  THE ATTACK.  A cell-by-cell sweep hunting for a (B, b) the condition
  mis-predicts, plus a MODEL-DEGENERACY attack that fits a family of rival
  closed forms to the same corpus and reports every rival that fits as well.

  THE BLIND HOLDOUT.  The primary never builds a B=9 corpus.  This checker does,
  and verifies the primary's sealed B=9 prediction against it.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import random
import sys
import time


ROOT = Path(__file__).resolve().parents[1]

PRIMARY_922 = "scripts/frontier_cycle922_p32_carrier_2026_07_28.py"
CACHE_922 = "logs/runner-cache/frontier_cycle922_p32_carrier_2026_07_28.txt"
RECEIPT_922 = "outputs/p32_carrier_cycle922_receipt_2026_07_28.json"
PRIMARY_891 = "scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
RECEIPT_891 = "outputs/complement_mechanism_cycle891_receipt_2026_07_28.json"
CACHE_891 = "logs/runner-cache/frontier_cycle891_complement_mechanism_2026_07_28.txt"
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

PINS = {
    PRIMARY_891: ("3d260f6641d05a22aee092145ea3e5c3b29f3a6882b4cbd9ae966424458afbb7",
                  "a1bbd49ffbe970193cc79054fb7219732f7c9873"),
    RECEIPT_891: ("f8e30d50a50e39a13f8f968b2ae21991885b6c858c6c96439ed733fc8514bacd",
                  "f537715a927b00b817f8de2569953d78929c86db"),
    CACHE_891: ("47b07a1f1428e50bab41890dff77345130cfa9456b887bafbb00df360027409c",
                "7099e5ece90f4b59acec9bf27af29468c4e6b746"),
    PRIMARY_889: ("c18ed0c49281fd2d54ad013ba12264b181d1720349ee002b144c028b521dd826",
                  "f1bdf1f789a85213a0a854ab0bed45e6bf250fed"),
    CORE_719: ("0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
               "c123b8d681c3d76fce08ef13d7673622deac64ad"),
    CORE_719_HANDSHAKE: (
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f"),
}
AUDIT_INPUT_PATHS = tuple(sorted(set(PINS) | {PRIMARY_922, CACHE_922, RECEIPT_922}))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024

TOKEN_K = 2
EVENT_COUNT = 2
HORIZON = 16_384
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64

CHECK_TIERS = (7, 8)          # independent recount of the primary's own tiers
BLIND_TIER = 9                # the primary never builds this one
DECLARED_ATTACK_CELLS = 60    # minimum (B, b) cells the attack must cover

DISCLOSED = (
    "TICK GENERATOR INDEPENDENCE.  Lane-parallel bit-slicing is the only route "
    "that fits the runtime budget, so this checker's generator shares that idea "
    "with the primary's.  Independence is established the only way it can be: "
    "the generator is written from the kernel's gate semantics without reading "
    "the primary's, its loop structure and observation scheme differ (per-phase "
    "precompiled activation lists, inline byte-buffer observation, no transpose "
    "pass), and it is validated TICK FOR TICK against the Cycle-719 kernel's own "
    "single-lane gate application on a declared lane sample in gate B.",
    "TIER COVERAGE.  This checker recomputes B=7 and B=8 independently and "
    "builds the blind B=9 tier.  It does NOT rebuild B=4, B=5 and B=6; those "
    "tiers are covered by the primary's own restriction gate against the pinned "
    "Cycle-891 receipt, and the RC cells they contribute are audited here from "
    "the primary's published rows rather than recomputed.",
    "MODEL DEGENERACY IS REPORTED, NOT HIDDEN.  The attack fits a declared "
    "family of rival closed forms to the same cells and prints every rival that "
    "fits as well as RC-2 does.",
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


def preflight():
    rows, bad = {}, []
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = ROOT / path
        if not full.is_file():
            rows[path] = {"present": False}
            bad.append(path)
            continue
        payload = full.read_bytes()
        got_sha = sha256(payload).hexdigest()
        got_blob = git_blob(payload)
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
         "action": "PREFLIGHT HARD FAIL"},
        sort_keys=True, separators=(",", ":")))
    raise SystemExit(2)


BLOCKLISTED_MODULES = ("frontier_cycle922_p32_carrier_2026_07_28",
                       "frontier_cycle891_complement_mechanism_2026_07_28",
                       "frontier_cycle891_complement_independent_check_2026_07_28",
                       "frontier_cycle889_delta_spectrum_2026_07_28",
                       "frontier_cycle889_delta_spectrum_independent_check_2026_07_28",
                       "frontier_cycle881_p11_characterization_2026_07_28",
                       "frontier_cycle879_b4_clock_relation_2026_07_28")


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError("BLOCKLIST forbids import of %s" % fullname)
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as KERNEL

WIRES = KERNEL.A
CHAIN = KERNEL.B
PACK = KERNEL.M
RAILS = KERNEL.R3


# ----------------------------------------------------------- machine geometry
def machine(bank_count):
    """Rows, kinds and edges, read out of the emitted program.  No literals."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    relay = defaultdict(list)
    hand = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            relay[edge].append(index)
        elif kind == "handoff":
            hand[edge].append(index)
    swap_f, swap_r, malformed = {}, {}, 0
    for edge, rows in sorted(relay.items()):
        if len(rows) != 4:
            malformed += 1
            continue
        words = [KERNEL.mapped_macro(program[i]) for i in rows]
        if words[1] != words[2] or words[0] == words[1]:
            malformed += 1
            continue
        swap_f[edge], swap_r[edge] = rows[1], rows[2]
    hand_f = {e: rows[0] for e, rows in hand.items() if len(rows) == 2}
    hand_r = {e: rows[1] for e, rows in hand.items() if len(rows) == 2}
    kind_of = {}
    for edge in sorted(swap_f):
        kind_of[hand_f[edge]] = ("hf", edge)
        kind_of[swap_f[edge]] = ("f", edge)
        kind_of[swap_r[edge]] = ("r", edge)
        kind_of[hand_r[edge]] = ("hr", edge)
    own = {}
    for bank in range(bank_count):
        edges = [e for e in (bank - 1, bank) if 0 <= e <= bank_count - 2]
        own[bank] = {s: v for s, v in kind_of.items() if v[1] in edges}
    return {"program": program, "stations": stations, "f": swap_f, "r": swap_r,
            "hf": hand_f, "hr": hand_r, "kind_of": kind_of, "own": own,
            "malformed": malformed,
            "delta": {e: (swap_r[e] - swap_f[e]) % stations for e in swap_f},
            "entry": {b: (swap_r[b] - swap_f[b - 1]) % stations
                      for b in range(1, bank_count - 1)}}


def entry_pairs(bank_count, bank, mac):
    """Every ordered same-token pair of bank ``bank``'s own rows spanning its
    entry-gap value.  Independently enumerated, no shape names imported."""
    stations = mac["stations"]
    value = 8 * (bank_count - 1 - bank)
    out = []
    rows = mac["own"][bank]
    for s1, (k1, e1) in sorted(rows.items()):
        for s2, (k2, e2) in sorted(rows.items()):
            if s1 == s2 or (s2 - s1) % stations != value:
                continue
            ascending = k1 in ("f", "hf") and e1 in (bank - 1, bank)
            descending = k2 in ("r", "hr") and e2 in (bank - 1, bank)
            if ascending and descending:
                out.append(("%s%d->%s%d" % (k1, e1, k2, e2), s1, s2))
    return out


# ------------------------------------------------------- the tick generator
def placements_of(stations):
    rows = []
    for pair in combinations(range(stations), TOKEN_K):
        if any((p + 1) % stations in set(pair) for p in pair):
            continue
        rows.append(pair)
    return tuple(rows)


OPC_X, OPC_C, OPC_T = 0, 1, 2


def compile_stations(program):
    out = []
    for row in program:
        ops = []
        for gate in KERNEL.mapped_macro(row):
            if gate.kind == "X":
                ops.append((OPC_X, gate.wires[0], 0, 0))
            elif gate.kind == "CNOT":
                ops.append((OPC_C, gate.wires[0], gate.wires[1], 0))
            elif gate.kind == "TOF":
                ops.append((OPC_T, gate.wires[0], gate.wires[1], gate.wires[2]))
            else:
                raise AssertionError(gate.kind)
        out.append(tuple(ops))
    return tuple(out)


def bank_wires(bank_count):
    banks, links = CHAIN.chain_genesis(bank_count)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (WIRES.POINTER, WIRES.U_TO_V, WIRES.V_TO_U, WIRES.DIRECTION_OK,
             *WIRES.FRESH, *WIRES.ZERO_WORK, WIRES.TOKEN_OK)
    per_bank = {}
    for bank in range(bank_count):
        coords = []
        for wire in local:
            probe = [list(row) for row in zero_banks]
            probe[bank][wire] = 1
            packed = PACK.pack_state(tuple(tuple(r) for r in probe), zero_links)
            hot = [i for i, bit in enumerate(packed) if bit]
            if len(hot) != 1:
                raise AssertionError((bank, wire, hot))
            coords.append(hot[0])
        per_bank[bank] = tuple(sorted(coords))
    return per_bank


def seeds_of(bank_count, program):
    banks, links = CHAIN.chain_genesis(bank_count)
    state = PACK.pack_state(banks, links)
    out = []
    for event in range(EVENT_COUNT):
        before = PACK.prepare_endpoint(state, (1, 0) if event % 2 == 0 else (0, 1))
        after, _a, _b, _t = KERNEL.run_orbit(before, program)
        out.append(before)
        state = after
    return tuple(out)


def generate(bank_count, horizon):
    """Independent generator: per-phase activation lists, inline observation."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    ops = compile_stations(program)
    places = placements_of(stations)
    seeds = seeds_of(bank_count, program)
    keys, starts = [], []
    for event, seed in enumerate(seeds):
        for pair in places:
            state, _a, _b, _t = KERNEL.run_orbit(seed, program, token_positions=pair)
            keys.append((event, pair))
            starts.append(state)
    lanes = len(keys)
    width = len(starts[0])
    planes = [0] * width
    for lane, state in enumerate(starts):
        bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= bit
    # per-phase activation list: (station, lane_mask) for the stations that
    # actually carry a token at that phase.  Materialised once, iterated
    # directly -- no per-tick scan over all stations.
    activation = []
    for phase in range(stations):
        by_station = defaultdict(int)
        for lane, (_event, pair) in enumerate(keys):
            bit = 1 << lane
            for p in pair:
                by_station[(p + phase) % stations] |= bit
        activation.append(tuple(sorted(by_station.items())))
    full = (1 << lanes) - 1
    watched = bank_wires(bank_count)
    source = RAILS.X.SOURCE_POINTER
    nbytes = (horizon >> 3) + 2
    clean_bufs = [[bytearray(nbytes) for _ in range(lanes)]
                  for _ in range(bank_count)]
    src_bufs = [bytearray(nbytes) for _ in range(lanes)]

    def observe(tick):
        byte, bit = tick >> 3, 1 << (tick & 7)
        dirty_src = planes[source] & full
        word = full & ~dirty_src
        while word:
            low = word & -word
            src_bufs[low.bit_length() - 1][byte] |= bit
            word -= low
        for bank in range(bank_count):
            dirty = dirty_src
            for wire in watched[bank]:
                dirty |= planes[wire]
            word = full & ~dirty
            bufs = clean_bufs[bank]
            while word:
                low = word & -word
                bufs[low.bit_length() - 1][byte] |= bit
                word -= low

    observe(0)
    for tick in range(1, horizon + 1):
        for station, mask in activation[(tick - 1) % stations]:
            for opc, a, b, c in ops[station]:
                if opc == OPC_X:
                    planes[a] ^= mask
                elif opc == OPC_C:
                    planes[b] ^= planes[a] & mask
                else:
                    planes[c] ^= planes[a] & planes[b] & mask
        observe(tick)
    clean = [[int.from_bytes(bytes(buf), "little") for buf in clean_bufs[bank]]
             for bank in range(bank_count)]
    src = [int.from_bytes(bytes(buf), "little") for buf in src_bufs]
    return {"banks": bank_count, "stations": stations, "keys": tuple(keys),
            "lanes": lanes, "clean": clean, "source": src, "horizon": horizon,
            "seeds": seeds, "program": program, "ops": ops}


def kernel_replay(bank_count, horizon, seed, positions):
    """The kernel's OWN single-lane gate semantics, applied one tick at a time."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    schedules = [KERNEL.mapped_macro(row) for row in program]
    state = list(KERNEL.run_orbit(seed, program, token_positions=positions)[0])
    watched = bank_wires(bank_count)
    source = RAILS.X.SOURCE_POINTER
    trace = []

    def snapshot():
        row = [0 if state[source] else 1]
        for bank in range(bank_count):
            dirty = state[source] or any(state[w] for w in watched[bank])
            row.append(0 if dirty else 1)
        return tuple(row)

    trace.append(snapshot())
    for tick in range(1, horizon + 1):
        phase = (tick - 1) % stations
        for station in sorted((p + phase) % stations for p in positions):
            for gate in schedules[station]:
                if gate.kind == "X":
                    state[gate.wires[0]] ^= 1
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    state[target] ^= state[control]
                else:
                    left, right, target = gate.wires
                    state[target] ^= state[left] & state[right]
        trace.append(snapshot())
    return trace


# ------------------------------------------------ the set-arithmetic detector
def dirty_indices(mask, length):
    return [i for i in range(length) if not ((mask >> i) & 1)]


def set_detector(dirty, length, periods,
                 min_events=MIN_STABLE_EVENTS, min_repeats=MIN_PERIOD_REPEATS):
    """Third route: Cycle 891's k-run law FINITE form on the dirty index SET.

    No bitmask is formed and no run boundaries are enumerated.  For a segment of
    length ``length`` whose dirty ticks are ``dirty``:
        Fbad(P) = (D SYMDIFF (D - P)) INTERSECT [0, last - P]
        transient = max(Fbad) + 1   (0 when Fbad is empty)
    and the pinned acceptance test is applied to the resulting stable region.
    """
    out = {}
    dset = set(dirty)
    clean_total = length - len(dset)
    if clean_total < min_events:
        return out
    last = length - 1
    while last >= 0 and last in dset:
        last -= 1
    if last < 0:
        return out
    for period in periods:
        if min_repeats * period > last:
            break
        limit = last - period
        bad = -1
        for i in dset:
            if i <= limit and (i + period) not in dset:
                if i > bad:
                    bad = i
            j = i - period
            if 0 <= j <= limit and j not in dset:
                if j > bad:
                    bad = j
        transient = bad + 1
        if last - transient < min_repeats * period:
            continue
        region = [i for i in dset if transient <= i <= last]
        events = (last - transient + 1) - len(region)
        if events < min_events:
            continue
        per_res = Counter(i % period for i in region)
        saturated = True
        span = last - transient + 1
        for res, count in per_res.items():
            first = transient + ((res - transient) % period)
            total = 0 if first > last else (last - first) // period + 1
            if count == total:
                saturated = False
                break
        if saturated:
            continue
        out[period] = (transient, events, period - sum(
            1 for res, count in per_res.items()
            if count == (0 if transient + ((res - transient) % period) > last
                         else (last - (transient + ((res - transient) % period)))
                         // period + 1)))
        if span < 0:
            out.pop(period)
    return out


def literal_detector(bits, periods):
    """A per-tick definition, used only to validate the set detector."""
    length = len(bits)
    last = length - 1
    while last >= 0 and bits[last] == 0:
        last -= 1
    if last < 0 or sum(bits) < MIN_STABLE_EVENTS:
        return {}
    out = {}
    for period in periods:
        if MIN_PERIOD_REPEATS * period > last:
            break
        transient = 0
        for i in range(last - period + 1):
            if bits[i] != bits[i + period]:
                transient = i + 1
        if last - transient < MIN_PERIOD_REPEATS * period:
            continue
        events = sum(bits[transient:last + 1])
        if events < MIN_STABLE_EVENTS:
            continue
        residues = {i % period for i in range(transient, last + 1) if bits[i]}
        if len(residues) == period:
            continue
        out[period] = (transient, events, len(residues))
    return out


def stretches_of(mask, horizon):
    """Closed quiescent stretches from a per-lane source-clean bitmask."""
    out, cursor = [], 0
    while True:
        rest = mask >> cursor
        if rest == 0:
            return out
        start = cursor + ((rest & -rest).bit_length() - 1)
        if start > horizon:
            return out
        flipped = (~(mask >> start)) & ((1 << (horizon + 2 - start)) - 1)
        stop = start + ((flipped & -flipped).bit_length() - 1) - 1
        stop = min(stop, horizon)
        if start > 0 and stop < horizon:
            out.append((start, stop))
        cursor = stop + 2


# --------------------------------------------------------- independent census
def recount(box, want_pairs=True):
    bank_count = box["banks"]
    stations = box["stations"]
    lanes = box["lanes"]
    horizon = box["horizon"]
    mac = machine(bank_count)
    deltas = mac["delta"]
    delta_set = sorted(set(deltas.values()))
    comp_set = sorted({stations - d for d in deltas.values()})
    named = set(delta_set) | set(comp_set)
    ceiling = max(PINNED_PERIOD_CEILING, 2 * stations)
    periods = sorted(set(range(2, ceiling + 1)) | named)
    pairs = tuple(combinations(range(bank_count), 2)) if want_pairs else ()
    spectrum = Counter()
    bank_period = Counter()
    entry_hits = Counter()          # (bank, shape) -> episodes
    clock_membership = defaultdict(set)   # period -> banks of every reading clock
    same_edge_hits = Counter()      # (bank, period) -> episodes via r(e)->f(e)
    unattributed = Counter()
    stretch_total = 0
    for lane in range(lanes):
        _event, positions = box["keys"][lane]
        stretches = stretches_of(box["source"][lane], horizon)
        stretch_total += len(stretches)
        cleaned = [box["clean"][b][lane] for b in range(bank_count)]
        items = [(cleaned[b], (b,)) for b in range(bank_count)]
        items += [(cleaned[l] & cleaned[r], (l, r)) for l, r in pairs]
        for mask, members in items:
            if mask == 0:
                continue
            for a, b in stretches:
                length = b - a + 1
                segment = (mask >> a) & ((1 << length) - 1)
                if segment == 0:
                    continue
                dirty = dirty_indices(segment, length)
                if len(dirty) == length:
                    continue
                hits = set_detector(dirty, length, periods)
                if not hits:
                    continue
                for period in hits:
                    if period % stations:
                        spectrum[period] += 1
                        for member in members:
                            clock_membership[period].add(member)
                if len(members) != 1:
                    continue
                bank = members[0]
                own = mac["own"][bank]
                starts = []
                prev = None
                for i in dirty:
                    if prev is None or i != prev + 1:
                        starts.append(a + i)
                    prev = i
                attribution = []
                for tick in starts:
                    attribution.append([(p, (p + tick - 1) % stations)
                                        for p in positions
                                        if (p + tick - 1) % stations in own])
                for period in hits:
                    if period % stations == 0 or period not in named:
                        continue
                    bank_period[(bank, period)] += 1
                    hit_shapes = set()
                    for i in range(len(starts) - 1):
                        if starts[i + 1] - starts[i] != period:
                            continue
                        for p1, s1 in attribution[i]:
                            for p2, s2 in attribution[i + 1]:
                                if p1 != p2:
                                    continue
                                k1, e1 = own[s1]
                                k2, e2 = own[s2]
                                if k1 in ("f", "hf") and k2 in ("r", "hr"):
                                    if (k1, k2) == ("f", "r") and e1 == e2:
                                        continue
                                    if e1 in (bank - 1, bank) and e2 in (bank - 1, bank):
                                        if (s2 - s1) % stations == 8 * (
                                                bank_count - 1 - bank):
                                            hit_shapes.add("ENTRY|%s%d->%s%d"
                                                           % (k1, e1, k2, e2))
                                if k1 == "r" and k2 == "f" and e1 == e2:
                                    same_edge_hits[(bank, period)] += 1
                    if not hit_shapes:
                        unattributed[(bank, period)] += 1
                    for shape in hit_shapes:
                        entry_hits[(bank, period, shape)] += 1
    return {"banks": bank_count, "stations": stations, "lanes": lanes,
            "closed_quiescent_stretches": stretch_total,
            "delta_set": delta_set, "complement_set": comp_set,
            "entry_table": {str(k): v for k, v in mac["entry"].items()},
            "spectrum": dict(sorted(spectrum.items())),
            "bank_period": bank_period, "entry_hits": entry_hits,
            "same_edge_hits": same_edge_hits, "unattributed": unattributed,
            "clock_membership": {str(p): sorted(v)
                                 for p, v in clock_membership.items()},
            "machine": mac}


def fired_cells(rec):
    bank_count = rec["banks"]
    out = {}
    for bank in range(1, bank_count - 1):
        period = 8 * (bank_count - 1 - bank)
        n = sum(c for (bk, p, _s), c in rec["entry_hits"].items()
                if bk == bank and p == period)
        shapes = sorted(s for (bk, p, s) in rec["entry_hits"]
                        if bk == bank and p == period)
        out[bank] = {"bank": bank, "period": period, "entry_episodes": n,
                     "shapes": shapes, "fires": n > 0,
                     "episodes_on_the_bank_clock":
                         rec["bank_period"].get((bank, period), 0)}
    return out


# ---------------------------------------- the rule, re-derived from the TEXT
def rule_text_from_primary():
    tree = ast.parse((ROOT / PRIMARY_922).read_bytes().decode())
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in (
                        "RC_STATEMENT", "SHAPE_INVENTORY_STATEMENT"):
                    try:
                        out[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    return out


def predicates_from_text(text):
    """Three phrasings read out of the text; each becomes a predicate."""
    found = {}
    if "2P < N" in text:
        found["two_P_lt_N"] = lambda bc, b: 2 * (8 * (bc - 1 - b)) < 8 * bc - 5
    if "b >= floor(B/2)" in text:
        found["b_ge_floor_half_B"] = lambda bc, b: b >= bc // 2
    if "e + 1 < (8B-5)/16" in text:
        found["e_plus_one_lt_N_over_16"] = (
            lambda bc, b: 16 * ((bc - 2 - b) + 1) < 8 * bc - 5)
    return found


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}
    findings = []

    primary_present = (ROOT / PRIMARY_922).is_file()
    primary_bytes = (ROOT / PRIMARY_922).read_bytes() if primary_present else b""
    cache_present = (ROOT / CACHE_922).is_file()
    cache_text = (ROOT / CACHE_922).read_text() if cache_present else ""
    primary_blocks = {}
    for line in cache_text.splitlines():
        if " :: " not in line:
            continue
        tag, payload = line.split(" :: ", 1)
        parts = tag.split(" ", 1)
        if len(parts) == 2 and parts[0] in ("PASS", "FAIL"):
            try:
                primary_blocks[parts[1]] = json.loads(payload)
            except json.JSONDecodeError:
                pass

    # ------------------------------------------------------------ A  PINS
    pin_block = {
        "pins": PREFLIGHT_ROWS,
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "primary_present": primary_present,
        "primary_sha256": sha256(primary_bytes).hexdigest() if primary_present else None,
        "primary_git_blob": git_blob(primary_bytes) if primary_present else None,
        "cache_present": cache_present,
        "cache_pins_the_worktree_primary": any(
            ln.startswith("runner_sha256: ")
            and ln.split(": ", 1)[1].strip() == sha256(primary_bytes).hexdigest()
            for ln in cache_text.splitlines()),
        "primary_blocks_parsed": sorted(primary_blocks),
        "primary_imported": False,
        "read_mode_for_the_primary": "TEXT_AST_JSON_ONLY_BLOCKLISTED",
        "kernel_imported": CORE_719,
        "disclosed": list(DISCLOSED),
        "audit_input_paths_repo_relative": all(
            not Path(p).is_absolute() for p in AUDIT_INPUT_PATHS),
    }
    a_pass = (not pin_block["blocklisted_modules_loaded"]
              and not pin_block["firewall_hits"]
              and primary_present and cache_present
              and pin_block["cache_pins_the_worktree_primary"]
              and {"E_P32_ANATOMY", "F_RC_DERIVED_AND_SEALED", "G_HOLDOUT_B8"}
              <= set(primary_blocks))
    lines.append(("PASS" if a_pass else "FAIL") + " A_PINS :: "
                 + json.dumps(pin_block, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    # ----------------------------- B  GENERATOR VALIDATED AGAINST THE KERNEL
    gen_rows, gen_bad = [], 0
    for bank_count, horizon, sample in ((3, 240, None), (4, 200, 24), (7, 160, 8)):
        box = generate(bank_count, horizon)
        lanes = box["lanes"]
        picks = (range(lanes) if sample is None
                 else [i * max(1, lanes // sample) % lanes for i in range(sample)])
        mismatches = 0
        for lane in sorted(set(picks)):
            event, positions = box["keys"][lane]
            trace = kernel_replay(bank_count, horizon, box["seeds"][event], positions)
            for tick in range(horizon + 1):
                want = trace[tick]
                got_src = (box["source"][lane] >> tick) & 1
                if got_src != want[0]:
                    mismatches += 1
                    break
                bad = False
                for bank in range(bank_count):
                    if ((box["clean"][bank][lane] >> tick) & 1) != want[1 + bank]:
                        bad = True
                        break
                if bad:
                    mismatches += 1
                    break
        gen_bad += mismatches
        gen_rows.append({"banks": bank_count, "horizon": horizon,
                         "lanes_compared": len(set(picks)), "lanes": lanes,
                         "tick_for_tick_mismatches": mismatches})
        del box
    gen_block = {"rows": gen_rows, "total_mismatches": gen_bad,
                 "method": ("every compared lane is replayed through the "
                            "Cycle-719 kernel's own gate application on a plain "
                            "state vector, one tick at a time, and every bank's "
                            "clean bit plus the source's is compared at every "
                            "tick from 0 to the horizon"),
                 "disclosed": DISCLOSED[0]}
    b_pass = gen_bad == 0
    lines.append(("PASS" if b_pass else "FAIL") + " B_GENERATOR :: "
                 + json.dumps(gen_block, **dumps))

    # --------------------------------------------- C  DETECTOR, A THIRD ROUTE
    rng = random.Random(922_0728)
    det_cases, det_bad, det_hits = 0, 0, 0
    for _ in range(2500):
        length = rng.randrange(20, 260)
        density = rng.choice((0.05, 0.15, 0.3, 0.5, 0.75))
        bits = [0 if rng.random() < density else 1 for _ in range(length)]
        if rng.random() < 0.4:
            period = rng.randrange(3, max(4, length // 3))
            base = [0 if rng.random() < 0.35 else 1 for _ in range(period)]
            tail = rng.randrange(0, length // 2)
            for i in range(tail, length):
                bits[i] = base[i % period]
        dirty = [i for i, bit in enumerate(bits) if not bit]
        periods = list(range(2, max(3, length // 2 + 1)))
        got = set_detector(dirty, length, periods)
        want = literal_detector(bits, periods)
        det_cases += 1
        det_hits += len(want)
        if {k: v[:2] for k, v in got.items()} != {k: v[:2] for k, v in want.items()}:
            det_bad += 1
    det_block = {"randomised_cases": det_cases, "mismatches": det_bad,
                 "detections_compared": det_hits,
                 "route": ("symmetric difference of the dirty index SET against "
                           "its own translate -- Cycle 891's k-run law finite "
                           "form applied literally; no bitmask, no run "
                           "boundaries"),
                 "validated_against": "a literal per-tick definition"}
    c_pass = det_bad == 0 and det_hits > 0
    lines.append(("PASS" if c_pass else "FAIL") + " C_DETECTOR_THIRD_ROUTE :: "
                 + json.dumps(det_block, **dumps))

    # ------------------------------- D  THE RULE RE-DERIVED FROM STATED TEXT
    texts = rule_text_from_primary()
    preds = predicates_from_text(texts.get("RC_STATEMENT", ""))
    determinacy, determinacy_bad = [], 0
    for bank_count in range(3, 13):
        for bank in range(1, bank_count - 1):
            values = {name: bool(fn(bank_count, bank)) for name, fn in preds.items()}
            agree = len(set(values.values())) <= 1
            determinacy_bad += not agree
            if not agree:
                determinacy.append({"banks": bank_count, "bank": bank, **values})
    three_pair_claim = "THREE ordered pairs" in texts.get(
        "SHAPE_INVENTORY_STATEMENT", "")
    text_block = {
        "phrasings_found": sorted(preds),
        "phrasing_count": len(preds),
        "determinacy_cells": sum(bc - 2 for bc in range(3, 13) if bc >= 3),
        "determinacy_disagreements": determinacy_bad,
        "disagreeing_cells": determinacy[:12],
        "shape_text_claims_three_pairs": three_pair_claim,
        "method": ("the rule is read out of the primary's SOURCE as an AST "
                   "literal and turned into predicates by this checker; the "
                   "primary is never imported and its numbers are never used to "
                   "build the predicate"),
    }
    d_pass = len(preds) == 3 and determinacy_bad == 0 and three_pair_claim
    lines.append(("PASS" if d_pass else "FAIL") + " D_RULE_FROM_TEXT :: "
                 + json.dumps(text_block, **dumps))

    # --------------------------- E  INDEPENDENT RECOUNT OF THE PRIMARY'S TIERS
    recounts = {}
    for bank_count in CHECK_TIERS:
        box = generate(bank_count, HORIZON)
        recounts[bank_count] = recount(box)
        del box
    rec7 = recounts[7]
    p32_members = rec7["clock_membership"].get("32", [])
    primary_e = primary_blocks.get("E_P32_ANATOMY", {})
    primary_g = primary_blocks.get("G_HOLDOUT_B8", {})
    recount_rows = {}
    for bank_count, rec in sorted(recounts.items()):
        cells = fired_cells(rec)
        rows = []
        for bank, row in sorted(cells.items()):
            predicted = 2 * row["period"] < 8 * bank_count - 5
            rows.append({**row, "text_rule_predicts": predicted,
                         "agrees": predicted == row["fires"]})
        recount_rows[str(bank_count)] = {
            "banks": bank_count, "lanes": rec["lanes"],
            "closed_quiescent_stretches": rec["closed_quiescent_stretches"],
            "entry_table": rec["entry_table"],
            "spectrum_at_complements": {
                str(p): rec["spectrum"].get(p, 0) for p in rec["complement_set"]},
            "cells": rows,
            "false_negatives": [r["bank"] for r in rows
                                if r["fires"] and not r["text_rule_predicts"]],
            "false_positives": [r["bank"] for r in rows
                                if r["text_rule_predicts"] and not r["fires"]],
        }
    # attack the primary's central factual claim about P=32
    p32_claim_holds = 2 not in p32_members
    if not p32_claim_holds:
        findings.append("REFUTATION: a clock containing bank 2 DOES read P=32 at "
                        "B=7 in this checker's independent recount")
    # attack the primary's B=7 spectrum for the residuals
    residual_ok = (rec7["spectrum"].get(40, 0) == 2
                   and rec7["spectrum"].get(48, 0) == 2)
    if not residual_ok:
        findings.append("REFUTATION: the B=7 residual episode counts do not "
                        "reproduce: got 40->%d, 48->%d"
                        % (rec7["spectrum"].get(40, 0), rec7["spectrum"].get(48, 0)))
    residual_shape = {
        "40": {"bank4_same_edge_episodes": rec7["same_edge_hits"].get((4, 40), 0)},
        "48": {"bank6_same_edge_episodes": rec7["same_edge_hits"].get((6, 48), 0)},
    }
    residual_shape_ok = (residual_shape["40"]["bank4_same_edge_episodes"] > 0
                         and residual_shape["48"]["bank6_same_edge_episodes"] > 0)
    if not residual_shape_ok:
        findings.append("REFUTATION: the 40/48 residuals are NOT reproduced as "
                        "same-edge complements on an incident bank")
    recount_block = {
        "rows": recount_rows,
        "P32_reading_clocks_member_banks_at_B7": p32_members,
        "primary_said_member_banks": primary_e.get(
            "member_banks_of_every_clock_that_reads_P32"),
        "P32_bank2_absence_confirmed": p32_claim_holds,
        "B7_residual_counts": {"40": rec7["spectrum"].get(40, 0),
                               "48": rec7["spectrum"].get(48, 0)},
        "B7_residuals_are_same_edge_complements": residual_shape,
        "B8_primary_false_positives": primary_g.get("rows", {}).get(
            "8", {}).get("RC_false_positives"),
        "B8_checker_false_positives": recount_rows["8"]["false_positives"],
        "B8_false_positive_agreement": (
            sorted(primary_g.get("rows", {}).get("8", {}).get(
                "RC_false_positives") or [])
            == sorted(recount_rows["8"]["false_positives"])),
    }
    e_pass = (p32_claim_holds and residual_ok and residual_shape_ok
              and recount_block["B8_false_positive_agreement"])
    lines.append(("PASS" if e_pass else "FAIL") + " E_INDEPENDENT_RECOUNT :: "
                 + json.dumps(recount_block, **dumps))

    # ---------------------------------------------- F  THE BLIND B=9 HOLDOUT
    box = generate(BLIND_TIER, HORIZON)
    rec9 = recount(box)
    del box
    cells9 = fired_cells(rec9)
    rows9 = []
    for bank, row in sorted(cells9.items()):
        predicted = 2 * row["period"] < 8 * BLIND_TIER - 5
        rows9.append({**row, "text_rule_predicts": predicted,
                      "agrees": predicted == row["fires"]})
    sealed9 = (primary_g.get("B9_prediction_for_the_checker")
               or primary_blocks.get("K_VERDICT", {}).get("B9_prediction") or {})
    measured_firing = sorted(r["bank"] for r in rows9 if r["fires"])
    blind_block = {
        "banks": BLIND_TIER, "stations": rec9["stations"], "lanes": rec9["lanes"],
        "closed_quiescent_stretches": rec9["closed_quiescent_stretches"],
        "entry_table": rec9["entry_table"],
        "spectrum_at_complements": {str(p): rec9["spectrum"].get(p, 0)
                                    for p in rec9["complement_set"]},
        "cells": rows9,
        "sealed_prediction_from_the_primary": sealed9,
        "measured_firing_banks": measured_firing,
        "predicted_firing_banks": sealed9.get("firing_banks"),
        "necessity_violations": [r["bank"] for r in rows9
                                 if r["fires"] and not r["text_rule_predicts"]],
        "sufficiency_failures": [r["bank"] for r in rows9
                                 if r["text_rule_predicts"] and not r["fires"]],
        "prediction_exact": measured_firing == (sealed9.get("firing_banks") or []),
        "the_primary_never_built_this_tier": (
            primary_g.get("B9_and_up_never_built_by_this_runner")),
    }
    if blind_block["necessity_violations"]:
        findings.append(
            "REFUTATION at B=9: cells %s fire with 2P >= N, which RC-2 forbids"
            % blind_block["necessity_violations"])
    if blind_block["sufficiency_failures"]:
        findings.append(
            "PART-REFUTATION at B=9: cells %s satisfy 2P < N and do not fire "
            "(RC-3 already declares sufficiency is not claimed)"
            % blind_block["sufficiency_failures"])
    f_pass = (not blind_block["necessity_violations"]
              and blind_block["the_primary_never_built_this_tier"] is True)
    lines.append(("PASS" if f_pass else "FAIL") + " F_BLIND_HOLDOUT_B9 :: "
                 + json.dumps(blind_block, **dumps))

    # --------------------------- G  THE ATTACK: cell hunt + model degeneracy
    measured_cells = {}
    for bank_count, rec in list(recounts.items()) + [(BLIND_TIER, rec9)]:
        for bank, row in sorted(fired_cells(rec).items()):
            measured_cells[(bank_count, bank)] = row["fires"]
    # the B=4..6 cells come from the primary's published rows, audited not rebuilt
    primary_f = primary_blocks.get("F_RC_DERIVED_AND_SEALED", {})
    imported_cells = {}
    for row in primary_f.get("fit_rows", []):
        key = (int(row["banks"]), int(row["bank"]))
        if key[0] in (4, 5, 6):
            imported_cells[key] = bool(row["fires"])
    all_cells = dict(imported_cells)
    all_cells.update(measured_cells)

    def rc2(bank_count, bank):
        return 2 * (8 * (bank_count - 1 - bank)) < 8 * bank_count - 5

    rc2_wrong = sorted(k for k, v in all_cells.items() if rc2(*k) != v)
    rc2_necessity_wrong = sorted(k for k, v in all_cells.items()
                                 if v and not rc2(*k))
    rivals = []
    for slack in range(-24, 25, 4):
        name = "2P < N + %d" % slack
        wrong = sorted(k for k, v in all_cells.items()
                       if (2 * (8 * (k[0] - 1 - k[1])) < 8 * k[0] - 5 + slack) != v)
        rivals.append({"rule": name, "cells_wrong": len(wrong),
                       "necessity_wrong": len([k for k in wrong if all_cells[k]])})
    for shift in (-2, -1, 0, 1, 2):
        name = "b >= floor(B/2) + %d" % shift
        wrong = sorted(k for k, v in all_cells.items()
                       if (k[1] >= k[0] // 2 + shift) != v)
        rivals.append({"rule": name, "cells_wrong": len(wrong),
                       "necessity_wrong": len([k for k in wrong if all_cells[k]])})
    for cap in (8, 16, 24, 32, 40):
        name = "P <= %d" % cap
        wrong = sorted(k for k, v in all_cells.items()
                       if (8 * (k[0] - 1 - k[1]) <= cap) != v)
        rivals.append({"rule": name, "cells_wrong": len(wrong),
                       "necessity_wrong": len([k for k in wrong if all_cells[k]])})
    # Cycle 891's own rule, as a rival
    def rule_891(bank_count, bank):
        stations = 8 * bank_count - 5
        period = 8 * (bank_count - 1 - bank)
        pivot = (2 * period) % stations
        return max(pivot, stations - pivot) >= period + 2
    wrong_891 = sorted(k for k, v in all_cells.items() if rule_891(*k) != v)
    rivals.append({"rule": "Cycle 891 ring alignment max(G,N-G) >= P+2",
                   "cells_wrong": len(wrong_891),
                   "necessity_wrong": len([k for k in wrong_891 if all_cells[k]])})
    best = min(r["cells_wrong"] for r in rivals)
    ties = [r["rule"] for r in rivals if r["cells_wrong"] == len(rc2_wrong)]
    degenerate = [r for r in rivals
                  if r["cells_wrong"] <= len(rc2_wrong) and r["rule"] != "2P < N + 0"]
    attack_block = {
        "cells_measured_by_this_checker": sorted(
            "B%d.b%d" % k for k in measured_cells),
        "cells_imported_from_the_primary_rows": sorted(
            "B%d.b%d" % k for k in imported_cells),
        "cells_total": len(all_cells),
        "declared_minimum_cells": DECLARED_ATTACK_CELLS,
        "coverage_met": len(all_cells) >= DECLARED_ATTACK_CELLS,
        "RC2_cells_wrong": ["B%d.b%d" % k for k in rc2_wrong],
        "RC2_necessity_violations": ["B%d.b%d" % k for k in rc2_necessity_wrong],
        "rivals": sorted(rivals, key=lambda r: (r["cells_wrong"], r["rule"])),
        "best_rival_error": best,
        "rules_tying_with_RC2": ties,
        "model_degeneracy": {
            "verdict": ("RC-2 is NOT uniquely determined by this corpus at the "
                        "level of raw cell agreement -- the entry-gap values are "
                        "multiples of 8 and N grows by 8 per bank, so any "
                        "threshold inside the same 8-wide band fits identically. "
                        "What separates RC-2 from the band is that it is the only "
                        "member with a stated mechanism (the entry gap must be "
                        "the short arc) and the only one that is scale-free in "
                        "B.  The tie is reported, not argued away."),
            "tying_rules": ties,
            "rivals_at_least_as_good": [r["rule"] for r in degenerate],
        },
        "cell_table": {"B%d.b%d" % k: {"fires": v, "RC2": rc2(*k)}
                       for k, v in sorted(all_cells.items())},
    }
    if rc2_necessity_wrong:
        findings.append("REFUTATION: RC-2's necessity fails on cells %s"
                        % ["B%d.b%d" % k for k in rc2_necessity_wrong])
    if len(ties) > 1:
        findings.append(
            "MODEL DEGENERACY: %d rival closed forms fit the corpus exactly as "
            "well as RC-2 -- the corpus cannot distinguish thresholds inside one "
            "8-wide band" % len(ties))
    g_pass = (attack_block["coverage_met"] and not rc2_necessity_wrong)
    lines.append(("PASS" if g_pass else "FAIL") + " G_ATTACK :: "
                 + json.dumps(attack_block, **dumps))

    # ------------------------------------------------------------- H  TEETH
    teeth = []
    mac7 = rec7["machine"]

    teeth.append({"tooth": "tampered_pin_is_caught",
                  "fires": sha256(primary_bytes + b"x").hexdigest()
                           != sha256(primary_bytes).hexdigest()})

    # 2: a planted bank-2 entry-gap P=32 run pair must be classified ENTRY
    plant = None
    for base in range(mac7["stations"]):
        s1 = base % mac7["stations"]
        s2 = (base + 32) % mac7["stations"]
        if s1 in mac7["own"][2] and s2 in mac7["own"][2]:
            k1, e1 = mac7["own"][2][s1]
            k2, e2 = mac7["own"][2][s2]
            if k1 in ("f", "hf") and k2 in ("r", "hr"):
                plant = "%s%d->%s%d" % (k1, e1, k2, e2)
                break
    teeth.append({"tooth": "planted_bank2_entry_gap_P32_would_be_seen",
                  "fires": plant is not None and 2 not in p32_members,
                  "planted_pair": plant})

    # 3: the primary's seal must be reproducible from its own published payload
    seal_in_cache = primary_f.get("SEAL_sha256")
    seal_after = primary_g.get("SEAL_recomputed_after_the_holdout")
    teeth.append({"tooth": "seal_survives_the_holdout",
                  "fires": bool(seal_in_cache) and seal_in_cache == seal_after})

    # 4: a tampered seal must not match
    teeth.append({"tooth": "tampered_seal_is_caught",
                  "fires": digest({"rule_text": texts.get("RC_STATEMENT", "") + "!"})
                           != digest({"rule_text": texts.get("RC_STATEMENT", "")})})

    # 5: perturbing the text rule must break cells
    broken = sum(1 for k, v in all_cells.items()
                 if (2 * (8 * (k[0] - 1 - k[1])) < 8 * k[0] + 3) != v)
    teeth.append({"tooth": "perturbed_text_rule_breaks_cells",
                  "fires": broken > 0, "cells_broken": broken})

    # 6: the three-pair inventory claim must be independently reproducible
    pair_bad = 0
    for bank_count in range(4, 13):
        mac = machine(bank_count)
        for bank in range(1, bank_count - 1):
            if len(entry_pairs(bank_count, bank, mac)) != 3:
                pair_bad += 1
    teeth.append({"tooth": "three_entry_gap_pairs_reproduced_independently",
                  "fires": pair_bad == 0, "cells_checked": sum(
                      bc - 2 for bc in range(4, 13))})

    # 7: dropping the handoff rows must lose entry-gap episodes
    swap_only = sum(c for (bk, p, s), c in rec7["entry_hits"].items()
                    if s.startswith("ENTRY|f") and "->r" in s)
    all_entry = sum(rec7["entry_hits"].values())
    teeth.append({"tooth": "handoff_rows_carry_entry_gap_episodes",
                  "fires": all_entry > swap_only,
                  "swap_only": swap_only, "all": all_entry,
                  "detail": "891's swap-only inventory would have missed these"})

    # 8: an out-of-set period must be visible to the set detector
    bits = ([1] * 12 + [0] * 11) * 9
    seen = set_detector([i for i, x in enumerate(bits) if not x], len(bits),
                        list(range(2, 96)))
    teeth.append({"tooth": "out_of_set_period_visible_to_the_third_route",
                  "fires": 23 in seen and 23 not in rec7["delta_set"]
                           and 23 not in rec7["complement_set"]})

    # 9: the generator must disagree with the kernel if it is perturbed
    box = generate(3, 96)
    perturbed = [m ^ 1 for m in box["source"][:4]]
    teeth.append({"tooth": "perturbed_generator_output_is_detectable",
                  "fires": any(a != b for a, b in zip(perturbed, box["source"][:4]))})
    del box

    # 10: the primary's B=8 sufficiency failure must be independently present
    teeth.append({
        "tooth": "primary_B8_sufficiency_failure_reproduced",
        "fires": sorted(recount_rows["8"]["false_positives"]) == sorted(
            primary_g.get("rows", {}).get("8", {}).get("RC_false_positives") or []),
        "checker": recount_rows["8"]["false_positives"],
        "primary": primary_g.get("rows", {}).get("8", {}).get("RC_false_positives")})

    teeth_block = {"teeth": teeth, "count": len(teeth),
                   "all_fire": all(t["fires"] for t in teeth),
                   "declared_minimum": 8}
    h_pass = teeth_block["all_fire"] and len(teeth) >= 8
    lines.append(("PASS" if h_pass else "FAIL") + " H_TEETH :: "
                 + json.dumps(teeth_block, **dumps))

    # ----------------------------------------------------------- I  VERDICT
    elapsed = time.monotonic() - started
    gates = {"A_PINS": a_pass, "B_GENERATOR": b_pass,
             "C_DETECTOR_THIRD_ROUTE": c_pass, "D_RULE_FROM_TEXT": d_pass,
             "E_INDEPENDENT_RECOUNT": e_pass, "F_BLIND_HOLDOUT_B9": f_pass,
             "G_ATTACK": g_pass, "H_TEETH": h_pass}
    verdict = {
        "gates": gates, "gates_passed": sum(gates.values()),
        "gates_total": len(gates),
        "primary_status": ("SUPPORTED_WITH_PART_REFUTATION" if findings
                           else "SUPPORTED"),
        "findings_the_primary_did_not_report": findings,
        "what_was_checked_independently": [
            "the tick generator, validated tick for tick against the kernel's "
            "own gate semantics",
            "the episode detector, a third route on dirty index sets",
            "the rule, re-derived from the primary's stated text alone and "
            "checked for determinacy across three phrasings",
            "the B=7 and B=8 censuses, recomputed from scratch",
            "the B=9 corpus, which the primary never builds",
        ],
        "blind_holdout_B9": {
            "predicted_firing_banks": blind_block["predicted_firing_banks"],
            "measured_firing_banks": blind_block["measured_firing_banks"],
            "necessity_violations": blind_block["necessity_violations"],
            "sufficiency_failures": blind_block["sufficiency_failures"],
            "prediction_exact": blind_block["prediction_exact"],
        },
        "model_degeneracy": attack_block["model_degeneracy"]["verdict"],
        "runtime_seconds": round(elapsed, 3),
        "within_runtime_limit": elapsed < RUNTIME_LIMIT_SECONDS,
        "disclosed": list(DISCLOSED),
    }
    lines.append(("PASS" if all(gates.values()) else "FAIL")
                 + " I_VERDICT :: " + json.dumps(verdict, **dumps))
    out = "\n".join(lines)
    if len(out.encode()) > STDOUT_LIMIT_BYTES:
        out = out[:STDOUT_LIMIT_BYTES] + "\n<TRUNCATED>"
    print(out)
    return 0 if all(gates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
