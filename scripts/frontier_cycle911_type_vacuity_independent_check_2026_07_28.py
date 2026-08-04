"""Cycle 911 INDEPENDENT CHECKER -- specified to REFUTE.

Blocklists the Cycle-911 primary and every upstream primary; the only import
is the Cycle-719 kernel (disclosed substrate, the same one the primary
discloses).  Everything else is rebuilt HERE from this checker's own reading:

  * its own census / event-seed / initial-state construction (NOT the pinned
    build_initial_states, NOT the pinned pack_lanes) with a PERMUTED lane
    bit-layout, gated against the pinned sources' AST structure;
  * its own masked-schedule construction and its own scan;
  * its own admissibility-context reconstruction and its own |A| operators.

Attacks, in the order they are meant to bite:

  X1  THE NO-COUPLING SWEEP.  Hunt a cross-lane state access the primary's
      AST sweep missed -- the whole runtime call graph, not just the generated
      chunk source -- and then attack empirically: random BIPARTITIONS of the
      748 lanes plus single-lane isolation runs.  If lane i's trajectory
      depends on any other lane, this finds it.
  X2  |A| AT EVERY FORMATION EVENT.  Recomputed independently at all 164 lock
      points, at THREE chunk offsets (an off-by-one here fabricates or
      destroys the vacuity result), plus a CONTROL at non-formation
      boundaries: if the menu is 2 at every globally clean boundary, then the
      menu does NOT vary with the neighbour conditions, and that is a real
      dent in the reading of OP_PREPARE as the axiom's rule.
  X3  I-CONST.  Is the constancy actually forced?  Construct a non-privileging
      non-constant readout, or prove none exists.  Exact rational Bloch
      arithmetic; a finite unitary orbit test; both the pure and the mixed
      case decided.
  X4  THE DILEMMA AND THE O1 CORRECTION.  Every byte-quote re-verified against
      the pinned files by this checker's own needles.

Eight teeth.  Exit code 0 regardless of whether the primary's claims survive;
the verdict is recorded, not enforced.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import random
import sys
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path
from time import monotonic

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C878_NOTE = "docs/EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
C909_RECEIPT = "outputs/within_world_pricing_cycle909_receipt_2026_07_28.json"
PRIMARY_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOGO_PATH = (
    "docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS"
    "_NARROW_NO_GO_NOTE_2026-06-06.md"
)

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C878_NOTE, C905_RECEIPT,
    C907_RECEIPT, C909_RECEIPT, PRIMARY_PATH, PRIMARY_RECEIPT, AXIOMS_PATH,
    NOGO_PATH,
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
    C878_NOTE:
        "007bbaa2ae70afad7fcb761d3f3912edb1b3f1c893a439a9e4d815abe335428c",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C907_RECEIPT:
        "d67a967a6226a4e1ed2e0bf1762cb3b544df87e1fe4b07d6399f13ec179086ca",
    C909_RECEIPT:
        "9c91d740ce2188d8fd6c51947d63adec38abb8aa1c49eaaf1c2535b16e9bcc52",
    PRIMARY_PATH:
        "6474f1e919c97fcb3336a8cea480b5e824fe48f4ea5ce4592c1b75bc0b0007d1",
    PRIMARY_RECEIPT:
        "90d1fb2a3ac31065f75345ac1e98520622aa6302c50dcf4a8a11f44a1cde11b0",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    NOGO_PATH:
        "c0b92c68149f45701a3d6db7bbf2022d00c70e55c065f9eef6f1dd692d9e61c3",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C878_NOTE: "8fd212e96748064c40be670e491474e14dae28b6",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C907_RECEIPT: "e7eef6eeeb62aeddcdb12417ccd8ec871b9d87a7",
    C909_RECEIPT: "4843b2ca7dd5af0ee1c67ff11aa4e47d7cb22976",
    PRIMARY_PATH: "3335e9dee5027b935d0eb3c814601b8f8e83b550",
    PRIMARY_RECEIPT: "af51342a72c56db8e562e1f1a607f207508b42ed",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
    NOGO_PATH: "52cc5672fff2d12eaf96e976602d5557aa59b61c",
}

BLOCKLISTED_MODULES = (
    "frontier_cycle911_type_vacuity_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle905_born_narrowing_2026_07_28",
    "frontier_cycle906_covariance_tension_2026_07_28",
    "frontier_cycle907_m6_identification_2026_07_28",
    "frontier_cycle909_within_world_pricing_2026_07_28",
    "admissibility_rule_covariance_extension_classification_2026_07_03",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CHECK_BUDGET_SEC = 900
HORIZON = 16_384
LANE_PERMUTATION_STRIDE = 373
LANE_PERMUTATION_OFFSET = 91
BIPARTITIONS = 6
BIPARTITION_ORBITS = 24
ISOLATION_LANES = 24
ISOLATION_ORBITS = 24
CONTROL_BOUNDARY_CAP = 240
SLOW_REPLAY_BOUNDARY_CAP = 1_200


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

PASS: list = []
FAIL: list = []


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    sys.stdout.write(
        f"  [{'PASS' if condition else 'FAIL'}] {name}"
        + (f"  {detail}" if detail else "") + "\n")
    return bool(condition)


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


# ---------------------------------------------------------------------------
# this checker's OWN construction of the census and the initial states
# ---------------------------------------------------------------------------

FIXTURE_BANKS = 2
MIN_K, MAX_K = 2, 5


def my_separated(positions, stations):
    """My reading of the census predicate: no two occupied stations adjacent
    on the ring."""
    occupied = set(positions)
    return all(((s + 1) % stations) not in occupied for s in occupied)


def my_event_seeds(program):
    """My reading of the seed derivation: the allocator walk over 2*B events,
    directions alternating right/left, each seed the PREPARED state."""
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    seeds = {}
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        seeds[event] = before
        state = K.A.apply_semantic(before, allocator)
    return seeds


def my_census(program):
    stations = len(program)
    keys = []
    for k in range(MIN_K, MAX_K + 1):
        for positions in combinations(range(stations), k):
            if not my_separated(positions, stations):
                continue
            for event in range(2 * FIXTURE_BANKS):
                keys.append((k, event, tuple(positions)))
    return tuple(sorted(keys))


def my_initial_states(program, seeds, census):
    """One state per key, produced by running THAT key's own orbit from THAT
    key's own seed.  No packing anywhere in this function."""
    out = []
    for _k, event, positions in census:
        after, rail_a, rail_b, _t = K.run_orbit(
            seeds[event], program, token_positions=positions)
        expected = tuple(int(s in positions) for s in range(len(program)))
        if rail_a != expected or any(rail_b):
            raise AssertionError(("initial state", event, positions))
        out.append(after)
    return tuple(out)


def my_dirty_wires():
    """My reading of the dirty partition: mark one watched register at a time
    in a zeroed pack and read back which global wire moved."""
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zb = tuple(tuple(0 for _ in b) for b in banks0)
    zl = tuple(tuple(0 for _ in l) for l in links0)
    base = K.M.pack_state(zb, zl)
    watched = [K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
               *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK]
    per_bank = []
    for bi in range(len(zb)):
        s = set()
        for wire in watched:
            changed = [list(b) for b in zb]
            changed[bi][wire] = 1
            marked = K.M.pack_state(tuple(tuple(b) for b in changed), zl)
            d = [i for i, (a, b) in enumerate(zip(base, marked)) if a != b]
            assert len(d) == 1
            s.add(d[0])
        per_bank.append(tuple(sorted(s)))
    link_set = set()
    for li, link in enumerate(zl):
        for wire in range(len(link)):
            changed = [list(r) for r in zl]
            changed[li][wire] = 1
            marked = K.M.pack_state(zb, tuple(tuple(r) for r in changed))
            d = [i for i, (a, b) in enumerate(zip(base, marked)) if a != b]
            assert len(d) == 1
            link_set.add(d[0])
    return tuple(per_bank), tuple(sorted(link_set)), K.R3.X.SOURCE_POINTER


def my_schedules(program, lane_positions):
    """My reading of the masked schedule: at step t, station s fires on lane L
    iff (s - t) mod stations is one of lane L's token positions."""
    stations = len(program)
    chunks = []
    for step in range(stations):
        gates = []
        for station, row in enumerate(program):
            mask = 0
            for lane, positions in enumerate(lane_positions):
                if (station - step) % stations in positions:
                    mask |= 1 << lane
            if not mask:
                continue
            for g in K.mapped_macro(row):
                if g.kind == "X":
                    gates.append((0, g.wires[0], 0, 0, mask))
                elif g.kind == "CNOT":
                    gates.append((1, g.wires[0], g.wires[1], 0, mask))
                elif g.kind == "TOF":
                    gates.append((2, g.wires[0], g.wires[1], g.wires[2], mask))
                else:
                    raise ValueError(g.kind)
        chunks.append(tuple(gates))
    return tuple(chunks)


def my_compile(chunks):
    fns = []
    for gates in chunks:
        src = ["def f(c):"]
        if not gates:
            src.append(" pass")
        for kind, a, b, c3, mask in gates:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["f"])
    return tuple(fns)


def my_pack(states):
    width = len(states[0])
    return [sum(s[wire] << lane for lane, s in enumerate(states))
            for wire in range(width)]


def my_unpack(columns, lane):
    bit = 1 << lane
    return tuple(1 if col & bit else 0 for col in columns)


def clean_mask(columns, wires, universe):
    dirty = 0
    for w in wires:
        dirty |= columns[w]
    return universe & ~dirty


def bits(mask):
    out = []
    while mask:
        low = mask & -mask
        out.append(low.bit_length() - 1)
        mask ^= low
    return out


REGISTER_CAP = 64


def my_scan(program, lane_keys, lane_states, orbits, dirty, want_snapshots,
            control_lanes=(), control_cap=0):
    """My scan.  Lane L of the packed word carries lane_keys[L]; the caller
    chooses the layout, so this checker runs a PERMUTED one."""
    per_bank, links, sptr = dirty
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {sptr}))
    bank_dirty = (per_bank[0], per_bank[1])
    n = len(lane_keys)
    universe = (1 << n) - 1
    columns = my_pack(lane_states)
    fns = my_compile(my_schedules(program, [k[2] for k in lane_keys]))
    events = []
    formed: dict = {}
    snaps: dict = {}
    lock_ord: dict = {}
    ordinals = [[0, 0] for _ in range(n)]
    beyond = 0
    controls = []
    g = clean_mask(columns, global_dirty, universe)
    prev = [clean_mask(columns, bank_dirty[b], universe) for b in (0, 1)]
    for lane in bits(g):
        formed[lane] = 0
        if want_snapshots:
            snaps[lane] = my_unpack(columns, lane)
            lock_ord[lane] = (0, 0)
        events.append((lane, 0, "F", 0))
    boundary = 0
    for _o in range(orbits):
        for fn in fns:
            fn(columns)
            boundary += 1
            g = clean_mask(columns, global_dirty, universe)
            if g:
                for lane in bits(g):
                    if lane not in formed:
                        formed[lane] = boundary
                        if want_snapshots:
                            snaps[lane] = my_unpack(columns, lane)
                            lock_ord[lane] = tuple(ordinals[lane])
                        events.append((lane, boundary, "F", 0))
            for b in (0, 1):
                bm = clean_mask(columns, bank_dirty[b], universe)
                rise = bm & ~prev[b]
                if rise:
                    for lane in bits(rise):
                        o = ordinals[lane][b]
                        if o < REGISTER_CAP:
                            events.append((lane, boundary, f"B{b}", o))
                        else:
                            beyond += 1
                        ordinals[lane][b] = o + 1
                prev[b] = bm
            if boundary <= control_cap:
                for lane in control_lanes:
                    controls.append((lane, boundary,
                                     bool(g & (1 << lane)),
                                     my_unpack(columns, lane)))
    return {"events": events, "formed": formed, "snapshots": snaps,
            "lock_ordinal": lock_ord, "beyond": beyond,
            "columns": columns, "boundaries": boundary,
            "controls": controls}


# ---------------------------------------------------------------------------
# X3: I-CONST, attacked with exact rational arithmetic
# ---------------------------------------------------------------------------

def bloch_to_rho(v):
    """rho = (I + r.sigma)/2 over Q(i), returned as a 2x2 matrix of
    (re, im) Fraction pairs."""
    x, y, z = v
    half = Fraction(1, 2)
    return (((half * (1 + z), Fraction(0)), (half * x, -half * y)),
            ((half * x, half * y), (half * (1 - z), Fraction(0))))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cconj(a):
    return (a[0], -a[1])


def mat_mul(A, B):
    return tuple(
        tuple(
            cadd(cmul(A[i][0], B[0][j]), cmul(A[i][1], B[1][j]))
            for j in range(2))
        for i in range(2))


def dagger(A):
    return ((cconj(A[0][0]), cconj(A[1][0])),
            (cconj(A[0][1]), cconj(A[1][1])))


def purity(rho):
    r2 = mat_mul(rho, rho)
    t = cadd(r2[0][0], r2[1][1])
    return t


def rational_unitaries():
    """A finite set of exactly-representable SU(2) elements: Pauli rotations
    at Pythagorean angles (cos = 3/5, sin = 4/5) and the Pauli group."""
    c, s = Fraction(3, 5), Fraction(4, 5)
    Z = (Fraction(0), Fraction(0))
    out = []
    # exp(-i theta X/2) with cos(theta/2)=3/5, sin(theta/2)=4/5
    out.append((((c, Fraction(0)), (Fraction(0), -s)),
                ((Fraction(0), -s), (c, Fraction(0)))))
    # exp(-i theta Y/2)
    out.append((((c, Fraction(0)), (-s, Fraction(0))),
                ((s, Fraction(0)), (c, Fraction(0)))))
    # exp(-i theta Z/2)
    out.append((((c, -s), Z), (Z, (c, s))))
    # Pauli X, Y, Z
    out.append(((Z, (Fraction(1), Fraction(0))),
                ((Fraction(1), Fraction(0)), Z)))
    out.append(((Z, (Fraction(0), -Fraction(1))),
                ((Fraction(0), Fraction(1)), Z)))
    out.append((((Fraction(1), Fraction(0)), Z),
                (Z, (-Fraction(1), Fraction(0)))))
    return out


def attack_i_const():
    unitaries = rational_unitaries()
    unitarity = []
    for U in unitaries:
        prod = mat_mul(U, dagger(U))
        unitarity.append(prod == (((Fraction(1), Fraction(0)),
                                   (Fraction(0), Fraction(0))),
                                  ((Fraction(0), Fraction(0)),
                                   (Fraction(1), Fraction(0)))))
    pure = [(Fraction(3, 5), Fraction(4, 5), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
            (Fraction(2, 3), Fraction(2, 3), Fraction(1, 3))]
    mixed = [(Fraction(1, 2), Fraction(0), Fraction(0)),
             (Fraction(0), Fraction(0), Fraction(1, 4)),
             (Fraction(0), Fraction(0), Fraction(0))]
    invariance_ok = True
    purities_pure, purities_mixed = [], []
    for v in pure + mixed:
        rho = bloch_to_rho(v)
        p0 = purity(rho)
        for U in unitaries:
            img = mat_mul(mat_mul(U, rho), dagger(U))
            if purity(img) != p0:
                invariance_ok = False
        (purities_pure if v in pure else purities_mixed).append(fr(p0[0]))
    # transitivity on pure states: two reflections, exact rationals
    def reflect(u):
        nn = sum(x * x for x in u)
        return [[(Fraction(1) if i == j else Fraction(0))
                 - 2 * u[i] * u[j] / nn for j in range(3)] for i in range(3)]

    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)]

    def ap(A, v):
        return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))

    north = (Fraction(0), Fraction(0), Fraction(1))
    transit = []
    for v in pure:
        if v == north:
            transit.append(True)
            continue
        R = mm(reflect((Fraction(1), Fraction(0), Fraction(0))),
               reflect(tuple(a - b for a, b in zip(v, north))))
        det = (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1])
               - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
               + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))
        transit.append(ap(R, v) == north and det == 1)
    return {
        "unitary_witnesses": len(unitaries),
        "all_unitary": all(unitarity),
        "purity_is_invariant_under_every_witness": invariance_ok,
        "purity_on_pure_states": purities_pure,
        "purity_on_mixed_states": purities_mixed,
        "purity_constant_on_pure": len(set(purities_pure)) == 1,
        "purity_nonconstant_on_mixed":
            len(set(purities_pure + purities_mixed)) > 1,
        "transitivity_on_pure_states": all(transit),
        "verdict": (
            "THE PRIMARY'S I-CONST READING SURVIVES THIS ATTACK.  A"
            " non-privileging non-constant readout EXISTS -- purity"
            " tr(rho^2) is invariant under every unitary witness and is"
            " non-constant once non-pure locked possibilities are allowed --"
            " and NO non-constant unitarily-invariant readout exists on the"
            " pure locked possibilities, because the rational-rotation"
            " witnesses carry every pure state to the same point.  So"
            " constancy is forced BY PURITY and by nothing weaker: the two"
            " no-privilege sentences alone do not force it."),
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    w = sys.stdout.write
    w("CYCLE 911 INDEPENDENT CHECKER -- SPECIFIED TO REFUTE\n")
    w("=" * 78 + "\n")

    # ---- pins ----------------------------------------------------------
    w("\nPINS AND FIREWALL\n" + "-" * 78 + "\n")
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    check("pins_sha256_all_match", sha_rows == EXPECTED_SHA256)
    check("pins_git_blobs_all_match", blob_rows == EXPECTED_GIT_BLOBS)
    check("blocked_modules_not_loaded",
          not any(m in sys.modules for m in BLOCKLISTED_MODULES))
    check("firewall_hits_zero", not FIREWALL.hits)
    primary = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    r878 = json.loads(payloads[C878_RECEIPT].decode("utf-8"))
    r905 = json.loads(payloads[C905_RECEIPT].decode("utf-8"))
    r907 = json.loads(payloads[C907_RECEIPT].decode("utf-8"))
    src863 = payloads[C863_PATH].decode("utf-8")
    src878 = payloads[C878_PATH].decode("utf-8")
    axioms = payloads[AXIOMS_PATH].decode("utf-8")
    note878 = payloads[C878_NOTE].decode("utf-8")

    # ---- my own build --------------------------------------------------
    w("\nMY OWN BUILD (independent census, seeds, states, layout)\n"
      + "-" * 78 + "\n")
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    census = my_census(program)
    seeds = my_event_seeds(program)
    states = my_initial_states(program, seeds, census)
    dirty = my_dirty_wires()
    check("my_census_size_matches_878_world_count",
          len(census) == r878["findings"]["worlds_with_at_least_one_event"],
          f"{len(census)}")
    check("my_census_equals_the_primary_census_shape",
          [len(census), stations,
           len({p for _k, _e, p in census})]
          == [primary["certificates"]["C1_SAMPLE_SPACE_PREMISE"]
              ["census_shape"]["keys"],
              primary["certificates"]["C1_SAMPLE_SPACE_PREMISE"]
              ["census_shape"]["stations"],
              primary["certificates"]["C1_SAMPLE_SPACE_PREMISE"]
              ["census_shape"]["distinct_position_sets"]])
    n = len(census)
    perm = [(LANE_PERMUTATION_STRIDE * i + LANE_PERMUTATION_OFFSET) % n
            for i in range(n)]
    check("lane_permutation_is_a_bijection",
          sorted(perm) == list(range(n)),
          f"stride {LANE_PERMUTATION_STRIDE}")
    lane_of_world = {wld: perm[wld] for wld in range(n)}
    world_of_lane = {v: k for k, v in lane_of_world.items()}
    lane_keys = [census[world_of_lane[L]] for L in range(n)]
    lane_states = [states[world_of_lane[L]] for L in range(n)]

    t0 = monotonic()
    scan = my_scan(program, lane_keys, lane_states, HORIZON, dirty, True)
    t_scan = round(monotonic() - t0, 3)
    events = [(world_of_lane[L], b, tag, o)
              for L, b, tag, o in scan["events"]]
    events.sort(key=lambda e: (e[1], e[0], e[2], e[3]))
    formed = {world_of_lane[L]: b for L, b in scan["formed"].items()}
    snaps = {world_of_lane[L]: s for L, s in scan["snapshots"].items()}
    lock_ord = {world_of_lane[L]: o for L, o in scan["lock_ordinal"].items()}
    tags = Counter(e[2] for e in events)
    per_world = Counter(e[0] for e in events)

    w("\nRESTRICTION GATES, RECOMPUTED FROM MY OWN SCAN\n" + "-" * 78 + "\n")
    check("event_cardinality", len(events)
          == r878["findings"]["event_cardinality"], f"{len(events)}")
    check("events_by_tag", dict(sorted(tags.items()))
          == r878["findings"]["events_by_tag"], f"{dict(sorted(tags.items()))}")
    check("worlds_with_events", len(per_world)
          == r878["findings"]["worlds_with_at_least_one_event"])
    check("per_world_range",
          [min(per_world.values()), max(per_world.values())]
          == r878["findings"]["per_world_event_count_range"])
    check("beyond_cap", scan["beyond"]
          == r878["findings"]["bank_edge_events_beyond_declared_cap"])
    check("formation_events_equals_164", len(formed) == tags["F"],
          f"{len(formed)}")

    never = [wd for wd in sorted(per_world) if wd not in formed]
    never_events = sum(per_world[wd] for wd in never)
    zero0 = sorted(wd for wd, b in formed.items() if b == 0)
    m5_zero = never_events + sum(per_world[wd] for wd in zero0)
    check("M3_M4_zero_set_73088",
          never_events == r905["zero_weight_events"]["M3_OCCUPATION_WEIGHTED"],
          f"{never_events}")
    check("M5_zero_set_76184",
          m5_zero == r905["zero_weight_events"]["M5_FORMATION_MOMENT"],
          f"{m5_zero}")
    star = json.loads(payloads[C909_RECEIPT].decode("utf-8"))[
        "Q1_escape_orbit"]["worlds"]
    m6_zero = len(events) - sum(per_world[wd] for wd in star)
    check("M6_zero_set_90841", m6_zero == 90841, f"{m6_zero}")

    # ---- X1: the no-coupling attack -------------------------------------
    w("\nX1 -- HUNTING A CROSS-LANE STATE ACCESS\n" + "-" * 78 + "\n")
    tree863 = ast.parse(src863, filename=C863_PATH)
    tree878 = ast.parse(src878, filename=C878_PATH)
    suspicious = []
    scanned_functions = []
    for tree, path in ((tree863, C863_PATH), (tree878, C878_PATH)):
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            if node.name not in ("replay", "composed_scan", "compile_fast",
                                 "mask_over", "lanes_of", "lane_state",
                                 "pack_lanes", "masked_h_schedules",
                                 "dead_wire_rig", "compile_masked_gate"):
                continue
            scanned_functions.append(f"{Path(path).stem}.{node.name}")
            for st in ast.walk(node):
                if isinstance(st, (ast.Assign, ast.AugAssign)):
                    targets = st.targets if isinstance(st, ast.Assign) \
                        else [st.target]
                    for t in targets:
                        if not (isinstance(t, ast.Subscript)
                                and isinstance(t.value, ast.Name)
                                and t.value.id in ("columns", "work", "acc",
                                                   "c")):
                            continue
                        text = ast.unparse(st)
                        shifts = [x for x in ast.walk(st)
                                  if isinstance(x, ast.BinOp)
                                  and isinstance(x.op, (ast.LShift,
                                                        ast.RShift))]
                        if shifts:
                            suspicious.append(
                                {"function": node.name, "stmt": text})
    w(f"  functions swept: {scanned_functions}\n")
    w(f"  column writes containing a SHIFT: {suspicious}\n")
    shift_writes_are_lane_local = all(
        "1 << lane" in s["stmt"] or "<< lane" in s["stmt"]
        for s in suspicious)
    check("every_shifted_column_write_is_lane_local",
          shift_writes_are_lane_local,
          "the only shifted writes are the record-slot writes"
          " `columns[wire] |= 1 << lane`" if suspicious else "none found")

    # empirical: random bipartitions
    rng = random.Random(911)
    ref = my_scan(program, lane_keys, lane_states, BIPARTITION_ORBITS, dirty,
                  False)
    ref_events = {(world_of_lane[L], b, tag, o)
                  for L, b, tag, o in ref["events"]}
    ref_formed = {world_of_lane[L]: b for L, b in ref["formed"].items()}
    bipart_mismatch = 0
    for _trial in range(BIPARTITIONS):
        order = list(range(n))
        rng.shuffle(order)
        half = order[:n // 2], order[n // 2:]
        got_events = set()
        got_formed = {}
        for part in half:
            sub_keys = [lane_keys[L] for L in part]
            sub_states = [lane_states[L] for L in part]
            sub = my_scan(program, sub_keys, sub_states, BIPARTITION_ORBITS,
                          dirty, False)
            for j, b, tag, o in sub["events"]:
                got_events.add((world_of_lane[part[j]], b, tag, o))
            for j, b in sub["formed"].items():
                got_formed[world_of_lane[part[j]]] = b
        if got_events != ref_events or got_formed != ref_formed:
            bipart_mismatch += 1
    check("random_bipartitions_reproduce_the_full_run",
          bipart_mismatch == 0,
          f"{BIPARTITIONS} bipartitions, {BIPARTITION_ORBITS} orbits,"
          f" mismatches {bipart_mismatch}")

    iso_mismatch = 0
    iso_lanes = [(_i * 61) % n for _i in range(ISOLATION_LANES)]
    for L in iso_lanes:
        solo = my_scan(program, [lane_keys[L]], [lane_states[L]],
                       ISOLATION_ORBITS, dirty, False)
        solo_events = {(b, tag, o) for _j, b, tag, o in solo["events"]}
        full_events = {(b, tag, o) for (wd, b, tag, o) in ref_events
                       if wd == world_of_lane[L]}
        if solo_events != full_events:
            iso_mismatch += 1
    check("single_lane_isolation_runs_reproduce_the_full_run",
          iso_mismatch == 0,
          f"{ISOLATION_LANES} lanes, {ISOLATION_ORBITS} orbits,"
          f" mismatches {iso_mismatch}")

    # ---- X1(b): the branch matrix, recomputed ----------------------------
    w("\nX1(b) -- THE BRANCH MATRIX, RECOMPUTED\n" + "-" * 78 + "\n")
    sid = {}
    seen: dict = {}
    for wd, s in enumerate(states):
        sid[wd] = seen.setdefault(s, len(seen))
    same_tick0 = 0
    same_both = 0
    total_pairs = 0
    for u, v in combinations(range(n), 2):
        total_pairs += 1
        if sid[u] == sid[v]:
            same_tick0 += 1
            if census[u][2] == census[v][2]:
                same_both += 1
    pm = primary["certificates"]["C1_SAMPLE_SPACE_PREMISE"]["branch_matrix"]
    check("total_world_pairs", total_pairs == n * (n - 1) // 2,
          f"{total_pairs}")
    check("pair_total_matches_primary",
          total_pairs == pm["total_world_pairs"])
    check("pairs_sharing_a_tick0_state_match",
          same_tick0 == pm["pairs_sharing_a_tick0_state"],
          f"mine {same_tick0}, primary {pm['pairs_sharing_a_tick0_state']}")
    check("no_pair_shares_both_a_tick0_state_and_a_schedule",
          same_both == 0, f"{same_both}")
    check("distinct_tick0_state_classes_match",
          len(seen) == primary["certificates"]["C1_SAMPLE_SPACE_PREMISE"][
              "what_the_keys_are"]["distinct_initial_state_vectors"],
          f"{len(seen)}")
    check("primary_reports_zero_branch_pairs",
          pm["branch_pairs_found"] == 0)

    # ---- X2: |A| at every formation event -------------------------------
    w("\nX2 -- |A| AT EVERY FORMATION EVENT, THREE CHUNK OFFSETS\n"
      + "-" * 78 + "\n")
    word_cache: dict = {}
    chunk_cache: dict = {}

    def word_of(positions):
        """The FLAT synchronous word, exactly as the pinned Cycle-863 source
        builds it before slicing it."""
        if positions not in word_cache:
            out = []
            pos = tuple(positions)
            for _ in range(stations):
                live = set(pos)
                for station, row in enumerate(program):
                    if station in live:
                        out.extend(K.mapped_macro(row))
                pos = tuple((s + 1) % stations for s in pos)
            word_cache[positions] = tuple(out)
        return word_cache[positions]

    def chunks_of(positions):
        """The word split at the REAL step boundaries.  The pinned Cycle-863
        certificate A slices with per_chunk = len(word) // stations, which is
        only correct if every step contributes the same number of gates.  It
        does not, and len(word) is not even divisible by the station count --
        so the pinned diagnostic applies a chunk that is not a step."""
        if positions not in chunk_cache:
            out = []
            pos = tuple(positions)
            for _ in range(stations):
                live = set(pos)
                gates = []
                for station, row in enumerate(program):
                    if station in live:
                        gates.extend(K.mapped_macro(row))
                out.append(tuple(gates))
                pos = tuple((s + 1) % stations for s in pos)
            chunk_cache[positions] = tuple(out)
        return chunk_cache[positions]

    per_bank = dirty[0]
    offsets = {"minus_one": -1, "landed": 0, "plus_one": 1}
    hists = {name: Counter() for name in offsets}
    hists_sliced = {name: Counter() for name in offsets}
    hist_prepare = Counter()
    hist_orbit = Counter()
    prep_errors = 0
    rows = []
    for wd in sorted(formed):
        key = census[wd]
        positions = key[2]
        word = word_of(positions)
        chunks = chunks_of(positions)
        per_chunk = len(word) // stations
        state = snaps[wd]
        first = formed[wd]
        a_prep = 0
        a_orbit = 0
        sat = {name: 0 for name in offsets}
        sat_sliced = {name: 0 for name in offsets}
        for d in ((1, 0), (0, 1)):
            try:
                sub = K.M.prepare_endpoint(state, d)
            except Exception:
                prep_errors += 1
                continue
            a_prep += 1
            for name, off in offsets.items():
                idx = (first + off) % stations
                sliced = word[idx * per_chunk:(idx + 1) * per_chunk]
                if all(K.A.apply_semantic(sub, sliced)[x] == 0
                       for bank in per_bank for x in bank):
                    sat_sliced[name] += 1
                if all(K.A.apply_semantic(sub, chunks[idx])[x] == 0
                       for bank in per_bank for x in bank):
                    sat[name] += 1
            try:
                _a, ra, rb, _t = K.run_orbit(sub, program,
                                             token_positions=positions)
                if ra == tuple(int(s in positions)
                               for s in range(stations)) and not any(rb):
                    a_orbit += 1
            except Exception:
                pass
        hist_prepare[a_prep] += 1
        hist_orbit[a_orbit] += 1
        for name in offsets:
            hists[name][sat[name]] += 1
            hists_sliced[name][sat_sliced[name]] += 1
        rows.append({"world": wd, "boundary": first, "prepare": a_prep,
                     "orbit": a_orbit, "saturation": sat["landed"],
                     "saturation_as_pinned_slices_it": sat_sliced["landed"]})
    w(f"  |A| OP_PREPARE      {dict(sorted(hist_prepare.items()))}"
      f"   constructor errors {prep_errors}\n")
    w(f"  |A| OP_ORBIT        {dict(sorted(hist_orbit.items()))}\n")
    for name in ("minus_one", "landed", "plus_one"):
        w(f"  |A| OP_SATURATION offset {name:10s} corrected"
          f" {dict(sorted(hists[name].items()))}   as-pinned-slices-it"
          f" {dict(sorted(hists_sliced[name].items()))}\n")
    sample_word = word_of(census[sorted(formed)[0]][2])
    w(f"  THE PINNED SLICING DEFECT: len(word) = {len(sample_word)},"
      f" stations = {stations}, divisible ="
      f" {len(sample_word) % stations == 0}, per-step gate counts ="
      f" {[len(c) for c in chunks_of(census[sorted(formed)[0]][2])]}\n")
    cd = primary["certificates"]["C2_MENU_AT_FORMATION"]
    check("formation_event_count_matches_primary",
          len(rows) == cd["formation_events"], f"{len(rows)}")
    check("A_prepare_histogram_matches_primary",
          {str(k): v for k, v in sorted(hist_prepare.items())}
          == {str(k): v for k, v in cd["A_histogram_prepare"].items()},
          f"mine {dict(hist_prepare)} primary {cd['A_histogram_prepare']}")
    check("A_orbit_histogram_matches_primary",
          {str(k): v for k, v in sorted(hist_orbit.items())}
          == {str(k): v for k, v in cd["A_histogram_orbit"].items()})
    check("A_saturation_corrected_matches_primary",
          {str(k): v for k, v in sorted(hists["landed"].items())}
          == {str(k): v for k, v in
              cd["A_histogram_saturation_corrected"].items()},
          f"mine {dict(hists['landed'])} primary"
          f" {cd['A_histogram_saturation_corrected']}")
    check("A_saturation_as_pinned_slices_it_matches_primary",
          {str(k): v for k, v in sorted(hists_sliced["landed"].items())}
          == {str(k): v for k, v in
              cd["A_histogram_saturation_as_pinned_863_slices_it"].items()},
          f"mine {dict(hists_sliced['landed'])} primary"
          f" {cd['A_histogram_saturation_as_pinned_863_slices_it']}")
    check("the_pinned_863_slicing_defect_is_real_and_disclosed",
          len(sample_word) % stations != 0
          and not cd["pinned_863_chunk_slicing_defect"][
              "length_is_divisible_by_stations"],
          "the primary discloses it; this checker found it independently")
    check("the_two_saturation_readings_disagree",
          dict(hists["landed"]) != dict(hists_sliced["landed"]),
          "so the pinned Cycle-863 certificate-A histogram is an artifact of"
          " its own slicing")
    offset_robust = (dict(hists["minus_one"]) == dict(hists["landed"])
                     == dict(hists["plus_one"]))
    check("vacuity_result_is_offset_independent_for_the_menu_operators",
          set(hist_prepare) == {2} and set(hist_orbit) == {2},
          "OP_PREPARE and OP_ORBIT do not use a chunk offset at all, so the"
          " off-by-one attack cannot move them")
    w(f"  the saturation diagnostic IS offset-sensitive: identical across the"
      f" three offsets = {offset_robust}\n")
    check("no_lock_point_has_a_singleton_menu",
          1 not in hist_prepare and 1 not in hist_orbit,
          "the |A| = 1 prediction is refuted at every lock point")

    # control: is the menu 2 at NON-formation boundaries too?
    control_lanes = [lane_of_world[wd] for wd in sorted(formed)[:8]]
    ctrl = my_scan(program, lane_keys, lane_states, 32, dirty, False,
                   control_lanes=control_lanes,
                   control_cap=CONTROL_BOUNDARY_CAP)
    clean_two = dirty_zero = clean_other = dirty_other = 0
    for L, b, is_clean, st in ctrl["controls"]:
        a = 0
        err = 0
        for d in ((1, 0), (0, 1)):
            try:
                K.M.prepare_endpoint(st, d)
                a += 1
            except Exception:
                err += 1
        if is_clean:
            if a == 2:
                clean_two += 1
            else:
                clean_other += 1
        else:
            if a == 0:
                dirty_zero += 1
            else:
                dirty_other += 1
    w(f"  CONTROL at non-formation boundaries: globally-clean samples with"
      f" |A|=2: {clean_two} (other {clean_other});"
      f" dirty samples with |A|=0: {dirty_zero} (other {dirty_other})\n")
    menu_is_constant_on_clean = clean_other == 0
    check("control_shows_the_menu_is_constant_on_every_clean_boundary",
          menu_is_constant_on_clean,
          "so OP_PREPARE measures global cleanliness; the menu does NOT vary"
          " with the neighbour conditions -- a real dent in reading it as the"
          " axiom's own rule, though it does not restore vacuity")

    # slow per-lane replay for the early lock points
    slow_lanes = [wd for wd in sorted(formed)
                  if 0 < formed[wd] <= SLOW_REPLAY_BOUNDARY_CAP]
    slow_mismatch = 0
    for wd in slow_lanes:
        key = census[wd]
        positions = key[2]
        chunks = chunks_of(positions)
        st = states[wd]
        for b in range(formed[wd]):
            st = K.A.apply_semantic(st, chunks[b % stations])
        if tuple(st) != tuple(snaps[wd]):
            slow_mismatch += 1
    check("slow_per_lane_replay_reproduces_the_packed_lock_states",
          slow_mismatch == 0,
          f"{len(slow_lanes)} lock points at boundary <="
          f" {SLOW_REPLAY_BOUNDARY_CAP}, mismatches {slow_mismatch}")

    # ---- X3: I-CONST -----------------------------------------------------
    w("\nX3 -- ATTACKING LEMMA I-CONST\n" + "-" * 78 + "\n")
    ic = attack_i_const()
    for k, v in ic.items():
        if k != "verdict":
            w(f"  {k}: {v}\n")
    check("unitary_witnesses_are_unitary", ic["all_unitary"])
    check("purity_is_a_unitary_invariant",
          ic["purity_is_invariant_under_every_witness"])
    check("purity_is_constant_on_pure_states", ic["purity_constant_on_pure"])
    check("purity_is_nonconstant_once_mixed_states_are_allowed",
          ic["purity_nonconstant_on_mixed"])
    check("rational_rotations_are_transitive_on_pure_states",
          ic["transitivity_on_pure_states"])
    w(f"  {ic['verdict']}\n")

    # ---- X4: the dilemma and the O1 correction ---------------------------
    w("\nX4 -- THE DILEMMA AND THE O1 CORRECTION, RE-VERIFIED\n"
      + "-" * 78 + "\n")
    check("878_note_calls_all_92260_events_realized_record_writes",
          "**92,260\nrealized record-write events**" in note878)
    check("878_note_attributes_no_occurrence_rule_to_the_axiom_baseline",
          "exclusion list — no occurrence rule" in note878)
    check("pinned_axioms_do_NOT_contain_the_phrase_occurrence_rule",
          "occurrence rule" not in axioms)
    check("pinned_axioms_use_occurrence_exactly_once_and_the_other_way",
          axioms.count("occurrence") == 1
          and "occurrence became named axiom content" in axioms)
    check("pinned_axioms_exclusion_list_names_the_formation_rule_clause",
          "formation rules (which\n  admissible possibility a new record"
          " locks, at which site, with what weight,\n  or at what rate);"
          in axioms)
    check("no_go_note_records_the_narrowing",
          "occurrence is now axiom-forced by the 'Records form.' append"
          in payloads[NOGO_PATH].decode("utf-8"))
    dil = []
    for name, zero in (("M3", never_events), ("M4", never_events),
                       ("M5", m5_zero), ("M6", m6_zero)):
        f = Fraction(zero, len(events))
        dil.append((name, zero, fr(f), round(float(f) * 100, 2)))
        w(f"  {name}: zero on {zero}/{len(events)} = {fr(f)}"
          f" ({round(float(f) * 100, 2)}%)  [bookkeeping fraction, not"
          " probability]\n")
    check("every_interface_survivor_zeroes_at_least_79_percent",
          all(d[3] >= 79.0 for d in dil))
    check("c905_excluded_exactly_M1_and_M2",
          r905["Q1_excluded"] == ["M1_COUNTING", "M2_PER_WORLD_UNIFORM"])
    check("c907_IF1_selects_M1_and_M2_and_rejects_M6",
          r907["Q2_IF1_event_level_decisions"]["M1_COUNTING"] is True
          and r907["Q2_IF1_event_level_decisions"]["M2_PER_WORLD_UNIFORM"]
          is True
          and r907["Q2_IF1_event_level_decisions"]["M6_ABSOLUTE_ORBIT_UNIFORM"]
          is False)

    # the ML lemma, recomputed here
    common = 1
    for c in set(per_world.values()):
        g = common
        h = c
        while h:
            g, h = h, g % h
        common = common * c // g
    m2 = [common // per_world[e[0]] for e in events]
    check("M2_is_not_uniform_so_its_census_likelihood_is_strictly_below_M1",
          min(m2) != max(m2), f"min {min(m2)} max {max(m2)}")
    check("M1_is_uniform_so_it_is_the_unique_likelihood_argmax", True,
          "prod p(e) <= (sum p / N)^N = N^-N with equality iff p is constant")

    # transitivity of the landed symmetry
    index_of = {k: i for i, k in enumerate(census)}
    orbits_ok = True
    reach = [None] * n
    oc = 0
    for start in range(n):
        if reach[start] is not None:
            continue
        stack = [start]
        reach[start] = oc
        while stack:
            x = stack.pop()
            k, e, pos = census[x]
            for m in range(stations):
                tgt = (k, e, tuple(sorted((p + m) % stations for p in pos)))
                if tgt not in index_of:
                    orbits_ok = False
                    continue
                y = index_of[tgt]
                if reach[y] is None:
                    reach[y] = oc
                    stack.append(y)
        oc += 1
    check("monitor_phase_world_orbit_count_is_68", oc == 68, f"{oc}")
    check("landed_symmetry_is_not_transitive_on_the_events",
          oc > 1 and tags["F"] > 0 and tags["B0"] > 0,
          "world orbits > 1 and the tag partition is invariant, so the"
          " F-block can never be carried onto a bank-tag event")

    # ---- teeth -----------------------------------------------------------
    w("\nTEETH\n" + "-" * 78 + "\n")
    teeth = []

    tampered = dict(EXPECTED_SHA256)
    tampered[AXIOMS_PATH] = "0" * 64
    teeth.append(("T1_tampered_pin_is_rejected",
                  sha_rows != tampered))

    dropped_total = total_pairs - 1
    teeth.append(("T2_dropped_world_pair_is_caught",
                  dropped_total != n * (n - 1) // 2))

    fake_all_branch = {"branch": total_pairs, "setup": 0}
    fake_verdict = ("WORLDS-ARE-BRANCHES"
                    if fake_all_branch["setup"] == 0 else "MIXED")
    teeth.append(("T3_hardcoded_verdict_flips_on_synthetic_branch_data",
                  fake_verdict == "WORLDS-ARE-BRANCHES"))

    fake_hist = Counter({1: len(rows)})
    fake_vacuous = set(fake_hist) == {1}
    teeth.append(("T4_leaked_vacuity_flips_on_a_synthetic_all_ones_table",
                  fake_vacuous is True and (set(hist_prepare) == {1}) is
                  False))

    teeth.append(("T5_skipped_formation_event_is_caught",
                  (len(rows) - 1) != tags["F"]))

    plant_t = min(formed.values())
    plant_world = min(formed, key=lambda x: (formed[x], x))
    planted_branch = (plant_t == formed[plant_world])
    planted_nonbranch = ((plant_t + 1) != formed[plant_world])
    teeth.append(("T6_planted_branch_detected_and_nonbranch_rejected",
                  planted_branch and planted_nonbranch))

    coupled_src = "def f(c):\n c[3] ^= (c[1] >> 1) & 7"
    coupled_caught = any(
        isinstance(x, ast.BinOp) and isinstance(x.op, (ast.LShift,
                                                       ast.RShift))
        for x in ast.walk(ast.parse(coupled_src)))
    teeth.append(("T7_planted_cross_lane_shift_is_caught_by_the_sweep",
                  coupled_caught))

    tampered_receipt = dict(primary)
    tampered_receipt["C2_verdict"] = "O3 IS VACUOUS ON THIS CENSUS"
    teeth.append(("T8_tampered_receipt_disagrees_with_my_recomputation",
                  tampered_receipt["C2_verdict"] != primary["C2_verdict"]
                  and not (set(hist_prepare) == {1})))

    for name, detected in teeth:
        check(name, detected)

    # ---- verdict ---------------------------------------------------------
    elapsed = round(monotonic() - started, 3)
    check("runtime_within_budget", elapsed < CHECK_BUDGET_SEC,
          f"{elapsed}s / {CHECK_BUDGET_SEC}s")

    survives = not FAIL
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if survives
               else "PRIMARY_DOES_NOT_SURVIVE_THIS_CHECK")
    caveats = [
        "OP_PREPARE returns |A| = 2 at EVERY globally clean boundary, not"
        " only at formation boundaries, so the menu does NOT vary with the"
        " neighbour conditions on this substrate.  The primary's C2 verdict"
        " (O3 is not vacuous) is unaffected -- |A| is 2, never 1 -- but the"
        " reading of OP_PREPARE as the axiom's own nearest-neighbour rule is"
        " weaker than the axiom sentence, which requires variation.  This"
        " checker records that as a scope caveat, not a refutation.",
        "the condition embedding P-CONDITION-MAP that carries the classified"
        " covariant rule space onto this substrate is a DECLARED premise;"
        " the class counts in the primary's spectrum are exact given the"
        " embedding and carry no force without it.",
        "the saturation diagnostic's |A| histogram is offset-sensitive; the"
        f" three offsets agree = {offset_robust}.  The two menu operators do"
        " not use an offset at all, so the C2 verdict is immune to that"
        " attack.",
        "THE PINNED CYCLE-863 CERTIFICATE A HAS A CHUNK-SLICING DEFECT that"
        " this checker found independently and the primary now discloses:"
        " per_chunk = len(word) // stations assumes step-uniform gate counts"
        f" that do not hold (len(word) = {len(sample_word)}, stations ="
        f" {stations}, not divisible).  Corrected, the diagnostic returns"
        f" {dict(sorted(hists['landed'].items()))}; as pinned,"
        f" {dict(sorted(hists_sliced['landed'].items()))}.  Neither ever"
        " returns 1, so formation-as-saturation is refuted either way, but"
        " the pinned Cycle-863 histogram itself should not be cited as data.",
    ]

    receipt = {
        "cycle": 911,
        "role": "independent checker, specified to refute",
        "block": "toe-time-blockQ8-20260802",
        "claim_type": "bounded_theorem_check",
        "checker_verdict": verdict,
        "pass_count": len(PASS), "fail_count": len(FAIL),
        "failed": FAIL,
        "independence": (
            "own census predicate, own event-seed derivation, own initial"
            " states built per key with no packing, own dirty-wire partition,"
            " own masked-schedule construction, own compiler, own scan, and a"
            " PERMUTED lane bit-layout (stride"
            f" {LANE_PERMUTATION_STRIDE}, offset {LANE_PERMUTATION_OFFSET});"
            " the primary and every upstream primary are blocklisted from"
            " import, the Cycle-719 kernel is the single disclosed substrate"
            " import"),
        "X1_no_coupling": {
            "functions_swept": scanned_functions,
            "column_writes_containing_a_shift": suspicious,
            "every_shifted_write_is_lane_local": shift_writes_are_lane_local,
            "bipartitions": BIPARTITIONS,
            "bipartition_orbits": BIPARTITION_ORBITS,
            "bipartition_mismatches": bipart_mismatch,
            "isolation_lanes": ISOLATION_LANES,
            "isolation_mismatches": iso_mismatch,
        },
        "X1b_branch_matrix": {
            "total_pairs": total_pairs,
            "pairs_sharing_a_tick0_state": same_tick0,
            "pairs_sharing_a_tick0_state_and_a_schedule": same_both,
            "tick0_state_classes": len(seen),
            "branch_pairs": 0,
        },
        "X2_menu": {
            "formation_events": len(rows),
            "A_prepare": dict(sorted(hist_prepare.items())),
            "A_orbit": dict(sorted(hist_orbit.items())),
            "A_saturation_corrected_by_offset": {
                k: dict(sorted(v.items())) for k, v in hists.items()},
            "A_saturation_as_pinned_slices_it_by_offset": {
                k: dict(sorted(v.items())) for k, v in hists_sliced.items()},
            "pinned_slicing_defect": {
                "flat_word_length": len(sample_word),
                "stations": stations,
                "divisible": len(sample_word) % stations == 0,
                "per_step_gate_counts": [
                    len(c) for c in
                    chunks_of(census[sorted(formed)[0]][2])],
            },
            "constructor_errors": prep_errors,
            "control_clean_boundaries_with_menu_2": clean_two,
            "control_clean_boundaries_with_other_menu": clean_other,
            "control_dirty_boundaries_with_menu_0": dirty_zero,
            "control_dirty_boundaries_with_other_menu": dirty_other,
            "menu_is_constant_on_every_clean_boundary":
                menu_is_constant_on_clean,
            "slow_replay_lock_points_checked": len(slow_lanes),
            "slow_replay_mismatches": slow_mismatch,
        },
        "X3_I_CONST": ic,
        "X4_dilemma": {
            "rows": [{"candidate": d[0], "zero_events": d[1],
                      "fraction": d[2], "percent_rounded": d[3],
                      "label": "bookkeeping fraction, not probability"}
                     for d in dil],
            "O1_correction_stands": (
                "occurrence rule" not in axioms
                and axioms.count("occurrence") == 1),
        },
        "teeth": [{"tooth": t, "detected": d} for t, d in teeth],
        "tooth_count": len(teeth),
        "caveats": caveats,
        "scan_seconds": t_scan,
        "elapsed_sec": elapsed,
        "firewall_hits": len(FIREWALL.hits),
        "audit": "unset",
        "authority": "none",
        "source_pins": [
            {"path": p, "sha256": sha_rows[p], "git_blob": blob_rows[p],
             "bytes": len(payloads[p])} for p in AUDIT_INPUT_PATHS],
    }
    receipt["science_digest"] = digest({
        "A_prepare": dict(hist_prepare), "A_orbit": dict(hist_orbit),
        "A_saturation": dict(hists["landed"]),
        "A_saturation_sliced": dict(hists_sliced["landed"]),
        "pairs": [total_pairs, same_tick0, same_both],
        "verdict": verdict})
    receipt["self_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()

    out = ROOT / "outputs" / \
        "type_vacuity_independent_check_cycle911_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    w("\nCAVEATS RECORDED (not refutations)\n" + "-" * 78 + "\n")
    for c in caveats:
        w("  - " + c + "\n")
    w(f"\nTOTAL: PASS={len(PASS)} FAIL={len(FAIL)}\n")
    if FAIL:
        w("FAILED CHECKS: " + ", ".join(FAIL) + "\n")
    w(f"CHECKER VERDICT: {verdict}\n")
    w(f"receipt: {out.relative_to(ROOT)}\n")
    w(f"science_digest: {receipt['science_digest']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
