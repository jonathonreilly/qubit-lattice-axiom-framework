#!/usr/bin/env python3
"""Cycle 676: synchronization / renewal and proper-time law tournament.

Tests LAW-LEVEL chain semantics for co-registered tick clocks: rate-constancy
synchronization, ratio transitivity, offset prediction, renewal (blank-bank
exhaust + one refill) invariance, stream reversal, piecewise proper-time
additivity, missing-shared-event refusal, malformed co-registration refusal,
and a no-ordinal decoder-discipline assertion.  Pure Python data structures;
no matter dynamics (numpy not needed).

Model.  A clock is a stream of tick events at an ideal signed rate nu.  Its
event chain is a list of predecessor-linked cells carrying a K16 rotor (one
increment per admitted tick, a carry receipt on each 15->0 wrap) and a finite
blank bank (exhaust + one refill).  The decoder

    Delta-tau(A, B) = 16 * (carries_B - carries_A) + (rotor_B - rotor_A)

is evaluated along verified lineage (B reachable from A by predecessor links)
and NEVER reads a loop ordinal (570/610 semantics): the bank's loop position
resets on refill, but the carry receipt persists, so the decoded count is
renewal-invariant.  Ticks occur at crossings of nu*s through integers over a
shared abstract parameter s in [0, 4096).

Firewalls:
  - the shared parameter s is generator bookkeeping, NOT time; it is asserted
    never to enter any decoder (signature + source discipline, check 9);
  - the decoded ratios r_AB, r_BC, r_AC are relational candidates, NOT proper
    time; nothing here identifies a tick count with an interval of proper time;
  - a co-registration cell is a conditional candidate Record, not a physical
    simultaneity claim; the acyclicity/refusal results are finite declared-code
    statements, not lattice-wide theorems.

Acceptance tests for the physical side to rerun:
  - reproduce rate-constancy across (S1,S2)/(S2,S3)/(S3,S4) under real detector
    jitter, within the two-tick bound 2/min-interval-count;
  - reproduce renewal invariance on real blank-bank hardware forced to exhaust
    and refill once inside (S2,S3);
  - confirm the physical decoder firmware reads no loop ordinal and no s.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import copy
import inspect
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FROZEN_CONTRACT_SHA256 = "bbbe6148679b865958d16180c9b800b7a48f1733e1191d754f41f04a8ec0513b"

RECEIPT = ROOT / (
    "outputs/physical_synchronization_renewal_proper_time_law_tournament_"
    "cycle676_receipt_2026_07_23.json"
)

# Frozen contract constants ---------------------------------------------------
NU_A = -0.4736
NU_B = -0.3125
NU_C = -0.2296
NU_D1 = -0.4736          # clock D, piecewise segment 1
NU_D2 = -0.3125          # clock D, piecewise segment 2
S_MAX = 4096
S_SPLIT = 2048           # clock D rate-change parameter
S_COREG = {"S1": 512, "S2": 1500, "S3": 2600, "S4": 3800}
K16 = 16
BANK_LARGE = 10 ** 9     # control bank: never exhausts
BANK_TEST_B = 700        # forces exactly one exhaust+refill inside (S2,S3)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


# ----------------------------------------------------------------------------
# Chain data structures.
# ----------------------------------------------------------------------------

class Cell:
    """A predecessor-linked event cell.

    rotor/carries are the decodable chain state.  loop_ordinal and s_debug are
    bookkeeping the decoder is forbidden to read (checks 4 and 9).
    """

    __slots__ = ("index", "pred", "rotor", "carries", "loop_ordinal",
                 "tag", "s_debug")

    def __init__(self, index, pred, rotor, carries, loop_ordinal, tag, s_debug):
        self.index = index
        self.pred = pred
        self.rotor = rotor              # K16 rotor value, 0..15
        self.carries = carries          # persistent carry receipts (never reset)
        self.loop_ordinal = loop_ordinal  # bank-loop position; NOT decodable
        self.tag = tag                  # "tick" or a co-registration name
        self.s_debug = s_debug          # generator s; NOT decodable


class EventChain:
    """A stream of admitted tick/co-registration cells with a K16 rotor and a
    finite blank bank (exhaust + a bounded number of refills)."""

    def __init__(self, bank_capacity: int, refills_allowed: int):
        self.cells: list[Cell] = []
        self.marks: dict[str, int] = {}   # co-registration name -> cell index
        self.rotor = 0
        self.carries = 0
        self.loop_ordinal = 0
        self.bank_capacity = bank_capacity
        self.blanks_left = bank_capacity
        self.refills_allowed = refills_allowed
        self.refills_used = 0
        self.refill_at: list[int] = []    # cell counts at which a refill fired

    def _consume_blank(self) -> None:
        if self.blanks_left == 0:
            if self.refills_used >= self.refills_allowed:
                raise RuntimeError("blank bank over budget (extra refill needed)")
            self.blanks_left = self.bank_capacity
            self.refills_used += 1
            self.loop_ordinal = 0          # loop resets; carries do NOT
            self.refill_at.append(len(self.cells))
        self.blanks_left -= 1
        self.loop_ordinal += 1

    def admit_tick(self, s_debug: float) -> None:
        self._consume_blank()
        self.rotor += 1
        if self.rotor == K16:              # carry receipt on 15->0 wrap
            self.rotor = 0
            self.carries += 1
        pred = self.cells[-1] if self.cells else None
        self.cells.append(Cell(len(self.cells), pred, self.rotor, self.carries,
                               self.loop_ordinal, "tick", s_debug))

    def admit_coreg(self, tag: str, s_debug: float) -> None:
        # A co-registration is a labeled read of chain state: it snapshots the
        # current rotor/carries without advancing them or drawing a blank.
        pred = self.cells[-1] if self.cells else None
        cell = Cell(len(self.cells), pred, self.rotor, self.carries,
                    self.loop_ordinal, tag, s_debug)
        self.cells.append(cell)
        self.marks[tag] = cell.index


# ----------------------------------------------------------------------------
# Decoders.  Signature discipline (check 9): they take only chain state.
# ----------------------------------------------------------------------------

def decode_position(chain, tag):
    """Absolute decoded count at a named co-registration, from chain state."""
    idx = chain.marks.get(tag)
    if idx is None:
        return None
    cell = chain.cells[idx]
    return K16 * cell.carries + cell.rotor


def decode_interval(chain, tag_a, tag_b):
    """Delta-tau along verified lineage; None (never zero) if lineage broken."""
    idx_a = chain.marks.get(tag_a)
    idx_b = chain.marks.get(tag_b)
    if idx_a is None or idx_b is None:
        return None
    cell_a = chain.cells[idx_a]
    cell_b = chain.cells[idx_b]
    later = cell_b if cell_b.index >= cell_a.index else cell_a
    earlier = cell_a if cell_b.index >= cell_a.index else cell_b
    node = later
    verified = False
    while node is not None:
        if node is earlier:
            verified = True
            break
        node = node.pred
    if not verified:
        return None
    pos_a = K16 * cell_a.carries + cell_a.rotor
    pos_b = K16 * cell_b.carries + cell_b.rotor
    return pos_b - pos_a


def ratio(chain_num, chain_den, tag_a, tag_b):
    num = decode_interval(chain_num, tag_a, tag_b)
    den = decode_interval(chain_den, tag_a, tag_b)
    if num is None or den is None or den == 0:
        return None
    return num / den


def two_tick_bound(*counts) -> float:
    vals = [abs(c) for c in counts if c is not None and c != 0]
    return 2.0 / min(vals) if vals else float("inf")


# ----------------------------------------------------------------------------
# Tick-stream generation (s is generator bookkeeping only).
# ----------------------------------------------------------------------------

def piecewise_tick_s(segments, s_max):
    """s-values of integer crossings of the accumulated |phase| across a list
    of (rate, s_start, s_end) segments (phase is continuous across breaks)."""
    ticks: list[float] = []
    phase0 = 0.0            # accumulated |phase| at the start of the segment
    level = 1              # next integer crossing not yet emitted
    guard = 0
    for rate, s0, s1 in segments:
        r = abs(rate)
        seg_end = min(float(s1), float(s_max))
        while True:
            guard += 1
            if guard > 10_000_000:
                raise RuntimeError("tick generation guard tripped")
            s_cross = s0 + (level - phase0) / r
            if s0 - 1e-9 <= s_cross < seg_end - 1e-9:
                ticks.append(s_cross)
                level += 1
            else:
                break
        phase0 += r * (seg_end - s0)
        if seg_end >= float(s_max) - 1e-9:
            break
    return ticks


def constant_tick_s(nu, s_max):
    return piecewise_tick_s([(nu, 0.0, float(s_max))], s_max)


def order_events(tick_s_list, coreg_map, reverse=False):
    events = [(s, 0, "tick", None) for s in tick_s_list]
    events += [(s, 1, "coreg", tag) for tag, s in coreg_map.items()]
    if not reverse:
        # forward: ascending s; at a tie a tick precedes a co-registration
        events.sort(key=lambda e: (e[0], e[1]))
    else:
        # reversed: descending s; at a tie a co-registration precedes a tick
        events.sort(key=lambda e: (-e[0], -e[1]))
    return events


def build_chain(tick_s_list, coreg_map, bank_capacity, refills, reverse=False):
    chain = EventChain(bank_capacity, refills)
    for s, _prio, kind, tag in order_events(tick_s_list, coreg_map, reverse):
        if kind == "tick":
            chain.admit_tick(s)
        else:
            chain.admit_coreg(tag, s)
    return chain


# ----------------------------------------------------------------------------
# Cross-order co-registration rule (612 JointOrder pattern, three devices).
# ----------------------------------------------------------------------------

class JointOrder:
    """Per-device chains plus shared co-registration events.  A shared event is
    admitted only if its per-device position strictly follows every previously
    shared event's position in EVERY device (locally checkable cross-order)."""

    def __init__(self, devices):
        self.chains = {d: [] for d in devices}
        self.shared: list[dict] = []

    def admit_local(self, device, identity):
        self.chains[device].append(identity)

    def admit_shared(self, identity):
        pos = {d: len(self.chains[d]) for d in self.chains}
        for prev in self.shared:
            if not all(prev[d] < pos[d] for d in self.chains):
                return "refused_inverted"
        for d in self.chains:
            self.chains[d].append(identity)
        self.shared.append(pos)
        return "admitted"

    def force_shared(self, identity, pos):
        """Adversary: inject an identification bypassing the cross-order rule."""
        self.shared.append(dict(pos))


# ----------------------------------------------------------------------------
# Main.
# ----------------------------------------------------------------------------

def main() -> int:
    start = time.time()
    receipt: dict[str, object] = {
        "cycle": 676,
        "authority": "none",
        "audit": "unset",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "rates": {"nu_A": NU_A, "nu_B": NU_B, "nu_C": NU_C,
                  "nu_D1": NU_D1, "nu_D2": NU_D2},
        "s_coreg": S_COREG,
        "s_max": S_MAX,
        "s_split": S_SPLIT,
        "K16": K16,
    }

    # Standard forward chains (large bank: no refills).
    ticks_A = constant_tick_s(NU_A, S_MAX)
    ticks_B = constant_tick_s(NU_B, S_MAX)
    ticks_C = constant_tick_s(NU_C, S_MAX)
    chain_A = build_chain(ticks_A, S_COREG, BANK_LARGE, 1)
    chain_B = build_chain(ticks_B, S_COREG, BANK_LARGE, 1)
    chain_C = build_chain(ticks_C, S_COREG, BANK_LARGE, 1)
    segs = [("S1", "S2"), ("S2", "S3"), ("S3", "S4")]
    pairs = [("S1", "S2"), ("S2", "S3"), ("S3", "S4"),
             ("S1", "S3"), ("S2", "S4"), ("S1", "S4")]

    # ---- 1. Rate-constancy synchronization theorem.
    r_AB = [ratio(chain_B, chain_A, a, b) for a, b in segs]
    r_BC = [ratio(chain_C, chain_B, a, b) for a, b in segs]
    counts_AB = [decode_interval(ch, a, b)
                 for ch in (chain_A, chain_B) for a, b in segs]
    counts_BC = [decode_interval(ch, a, b)
                 for ch in (chain_B, chain_C) for a, b in segs]
    bound_AB = two_tick_bound(*counts_AB)
    bound_BC = two_tick_bound(*counts_BC)
    spread_AB = max(r_AB) - min(r_AB)
    spread_BC = max(r_BC) - min(r_BC)
    check(
        "rate-constancy sync: r_AB and r_BC are constant across (S1,S2), "
        "(S2,S3), (S3,S4) within the two-tick bound 2/min-interval-count",
        spread_AB <= bound_AB and spread_BC <= bound_BC,
        {"r_AB": r_AB, "spread_AB": spread_AB, "bound_AB": bound_AB,
         "r_BC": r_BC, "spread_BC": spread_BC, "bound_BC": bound_BC},
    )

    # ---- 2. Transitivity r_AB * r_BC = r_AC (full-range for stability).
    r_AB_full = ratio(chain_B, chain_A, "S1", "S4")
    r_BC_full = ratio(chain_C, chain_B, "S1", "S4")
    r_AC_full = ratio(chain_C, chain_A, "S1", "S4")
    counts_full = [decode_interval(ch, "S1", "S4")
                   for ch in (chain_A, chain_B, chain_C)]
    bound_t = two_tick_bound(*counts_full)
    trans_resid = abs(r_AB_full * r_BC_full - r_AC_full)
    check(
        "transitivity: r_AB * r_BC equals r_AC within the propagated two-tick "
        "bound",
        trans_resid <= bound_t,
        {"r_AB": r_AB_full, "r_BC": r_BC_full, "r_AC": r_AC_full,
         "residual": trans_resid, "bound": bound_t},
    )

    # ---- 3. Offset synchronization (predict B at S3 from a calibration ratio).
    pos_B_S1 = decode_position(chain_B, "S1")
    pos_B_S3 = decode_position(chain_B, "S3")
    a_int_13 = decode_interval(chain_A, "S1", "S3")
    b_int_13 = decode_interval(chain_B, "S1", "S3")
    r_AB_cal = ratio(chain_B, chain_A, "S1", "S2")     # different interval
    predicted_B_S3 = pos_B_S1 + r_AB_cal * a_int_13
    offset_err = abs(predicted_B_S3 - pos_B_S3)
    r_unc = two_tick_bound(decode_interval(chain_A, "S1", "S2"),
                           decode_interval(chain_B, "S1", "S2"))
    bound_off = 2.0 + r_unc * a_int_13
    check(
        "offset sync: B's decoded count at S3 predicted from B at S1 plus "
        "r_AB * A's decoded (S1,S3) interval matches within bound",
        offset_err <= bound_off,
        {"predicted": predicted_B_S3, "actual": pos_B_S3,
         "error": offset_err, "bound": bound_off},
    )

    # ---- 4. Renewal invariance (exhaust + one refill inside (S2,S3) for B).
    chain_B_test = build_chain(ticks_B, S_COREG, BANK_TEST_B, 1)
    chain_B_ctrl = build_chain(ticks_B, S_COREG, BANK_LARGE, 1)
    intervals_equal = all(
        decode_interval(chain_B_test, a, b) == decode_interval(chain_B_ctrl, a, b)
        for a, b in pairs
    )
    ratios_equal = all(
        ratio(chain_B_test, chain_A, a, b) == ratio(chain_B_ctrl, chain_A, a, b)
        for a, b in pairs
    )
    one_refill = chain_B_test.refills_used == 1
    refill_idx = chain_B_test.refill_at[0] if chain_B_test.refill_at else -1
    refill_inside = (chain_B_test.marks["S2"] < refill_idx
                     < chain_B_test.marks["S3"])
    check(
        "renewal invariance: forcing one blank-bank exhaust+refill inside "
        "(S2,S3) for B leaves every decoded interval and ratio identical to a "
        "large-bank control (carry receipt persists; loop ordinal ignored)",
        intervals_equal and ratios_equal and one_refill and refill_inside,
        {"intervals_equal": intervals_equal, "ratios_equal": ratios_equal,
         "refills_used": chain_B_test.refills_used, "refill_at": refill_idx,
         "refill_inside_S2_S3": refill_inside},
    )

    # ---- 5. Reversal (negate stream direction): r invariant, intervals negate.
    rev_A = build_chain(ticks_A, S_COREG, BANK_LARGE, 1, reverse=True)
    rev_B = build_chain(ticks_B, S_COREG, BANK_LARGE, 1, reverse=True)
    rev_C = build_chain(ticks_C, S_COREG, BANK_LARGE, 1, reverse=True)
    intervals_negate = all(
        decode_interval(rev, a, b) == -decode_interval(fwd, a, b)
        for fwd, rev in ((chain_A, rev_A), (chain_B, rev_B), (chain_C, rev_C))
        for a, b in pairs
    )
    r_AB_rev = ratio(rev_B, rev_A, "S1", "S4")
    r_BC_rev = ratio(rev_C, rev_B, "S1", "S4")
    ratios_invariant = (abs(r_AB_rev - r_AB_full) < 1e-12
                        and abs(r_BC_rev - r_BC_full) < 1e-12)
    check(
        "reversal: under reversed streams every decoded interval negates while "
        "every ratio is invariant (orientation-consistent)",
        intervals_negate and ratios_invariant,
        {"intervals_negate": intervals_negate,
         "r_AB_rev": r_AB_rev, "r_BC_rev": r_BC_rev},
    )

    # ---- 6. Piecewise proper-time composition (clock D).
    ticks_D = piecewise_tick_s(
        [(NU_D1, 0.0, float(S_SPLIT)), (NU_D2, float(S_SPLIT), float(S_MAX))],
        S_MAX,
    )
    coreg_D = {"SD0": 0.0, "SD": float(S_SPLIT), "SDE": float(S_MAX)}
    chain_D = build_chain(ticks_D, coreg_D, BANK_LARGE, 1)
    d_first = decode_interval(chain_D, "SD0", "SD")
    d_second = decode_interval(chain_D, "SD", "SDE")
    d_total = decode_interval(chain_D, "SD0", "SDE")
    additive = (d_first + d_second == d_total)
    phase_split = abs(NU_D1) * S_SPLIT
    phase_end = phase_split + abs(NU_D2) * (S_MAX - S_SPLIT)
    pred_first = int(math.floor(phase_split + 1e-9))
    pred_total = int(math.floor(phase_end + 1e-9))
    pred_second = pred_total - pred_first
    naive_second = int(math.floor(abs(NU_D2) * (S_MAX - S_SPLIT) + 1e-9))
    floor_ok = (d_first == pred_first and d_second == pred_second
                and d_total == pred_total)
    boundary_frac = phase_split - math.floor(phase_split)
    boundary_note = (
        "boundary |phase(2048)|=%.4f (frac %.4f, non-integer): the straddling "
        "tick is assigned to segment 2; an integer boundary phase would move "
        "one tick to segment 1 (+-1 honest)" % (phase_split, boundary_frac)
    )
    check(
        "piecewise proper-time: decoded total = decoded(first)+decoded(second) "
        "exactly, and matches the integer tick-count prediction floor-"
        "consistently with the +-1 boundary tick reported honestly",
        additive and floor_ok,
        {"first": d_first, "second": d_second, "total": d_total,
         "pred_first": pred_first, "pred_second": pred_second,
         "pred_total": pred_total, "naive_second": naive_second,
         "boundary": boundary_note},
    )

    # ---- 7. Missing shared event: delete S2 from a copy of B's chain.
    chain_B_del = copy.deepcopy(chain_B)
    saved_13 = decode_interval(chain_B_del, "S1", "S3")
    del chain_B_del.marks["S2"]
    undef = [decode_interval(chain_B_del, a, b)
             for a, b in (("S1", "S2"), ("S2", "S3"), ("S2", "S4"))]
    still_13 = decode_interval(chain_B_del, "S1", "S3")
    sync_13 = ratio(chain_B_del, chain_A, "S1", "S3")
    never_zero = all(x is None for x in undef)   # undefined, never zero
    check(
        "missing shared event: deleting S2 makes every interval terminating at "
        "S2 undefined (None, never zero) while (S1,S3) is unchanged and sync "
        "via (S1,S3) still works",
        never_zero and still_13 == saved_13 and still_13 is not None
        and sync_13 is not None,
        {"undefined_at_S2": undef, "interval_S1_S3": still_13,
         "sync_ratio_S1_S3": sync_13},
    )

    # ---- 8. Malformed co-registration refused (cross-order rule).
    jo = JointOrder(["A", "B", "C"])
    for i in range(2):
        for d in ("A", "B", "C"):
            jo.admit_local(d, i)
    admitted = [jo.admit_shared(t) for t in ("S1", "S2", "S3", "S4")]
    all_admitted = all(x == "admitted" for x in admitted)
    adv = JointOrder(["A", "B", "C"])
    for i in range(4):
        for d in ("A", "B", "C"):
            adv.admit_local(d, i)
    first = adv.admit_shared("S1")
    adv.force_shared("Sx", {"A": 1, "B": 9, "C": 1})   # inverted in B
    refusal = adv.admit_shared("S2")
    check(
        "malformed co-registration: an inverted shared admission (position not "
        "after an earlier shared event in every device) is refused (612 rule)",
        all_admitted and first == "admitted"
        and refusal == "refused_inverted",
        {"consistent_admitted": admitted, "inverted_refused": refusal},
    )

    # ---- 9. No-ordinal decoder discipline (signature + source).
    sig_pos = list(inspect.signature(decode_position).parameters)
    sig_int = list(inspect.signature(decode_interval).parameters)
    sig_ok = (sig_pos == ["chain", "tag"]
              and sig_int == ["chain", "tag_a", "tag_b"])
    src = inspect.getsource(decode_position) + inspect.getsource(decode_interval)
    forbidden = ("loop_ordinal", "s_debug", "blanks_left", "refill",
                 "bank", "generator", "_prio")
    src_ok = all(tok not in src for tok in forbidden)
    check(
        "no-ordinal assertion: the decoders take only chain state "
        "(chain, tag[, tag]) and reference no loop ordinal and no s "
        "(provable by signature + source discipline)",
        sig_ok and src_ok,
        {"sig_position": sig_pos, "sig_interval": sig_int,
         "forbidden_tokens_absent": src_ok},
    )

    # ---- Receipt.
    receipt["tick_counts"] = {
        "A": len(ticks_A), "B": len(ticks_B), "C": len(ticks_C),
        "D": len(ticks_D),
    }
    receipt["decoded_positions"] = {
        clock: {tag: decode_position(ch, tag) for tag in S_COREG}
        for clock, ch in (("A", chain_A), ("B", chain_B), ("C", chain_C))
    }
    receipt["ratios"] = {
        "r_AB_segments": r_AB, "r_BC_segments": r_BC,
        "r_AB_full": r_AB_full, "r_BC_full": r_BC_full, "r_AC_full": r_AC_full,
        "transitivity_residual": trans_resid,
        "nu_ratio_AB": abs(NU_B / NU_A), "nu_ratio_BC": abs(NU_C / NU_B),
        "nu_ratio_AC": abs(NU_C / NU_A),
    }
    receipt["piecewise"] = {
        "first": d_first, "second": d_second, "total": d_total,
        "phase_split": phase_split, "phase_end": phase_end,
        "boundary_frac": boundary_frac,
    }
    receipt["interpretation_firewall"] = [
        "s is generator bookkeeping, not time; the decoders provably never read "
        "it (check 9)",
        "r_AB, r_BC, r_AC are relational rate candidates, not proper time; a "
        "tick count is not identified with a proper-time interval",
        "renewal invariance is a property of the carry-receipt decoder, not a "
        "claim about physical clock stability; loop ordinals are non-decodable",
        "the cross-order refusal is a finite declared-code statement, not a "
        "lattice-wide simultaneity theorem",
    ]

    elapsed = time.time() - start
    receipt["elapsed_seconds"] = elapsed
    receipt["pass_count"] = PASS
    receipt["fail_count"] = FAIL
    receipt["pass"] = FAIL == 0
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=1, default=float) + "\n", encoding="utf-8"
    )
    print("RESULT", PASS, FAIL, "elapsed", round(elapsed, 2), "s")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
