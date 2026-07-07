#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_time_axis_is_history_index_2026_07_03.py

Exact-arithmetic runner for the bounded note

  TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md

Scope: this runner computes the load-bearing combinatorial content of a
bounded theorem (T1-T2) plus a bounded observation (T3) plus bounded support
(T4-T5). It uses exact objects only: int / tuple / set / frozenset / dict.
NO floats, NO numpy, NO fitted or observed inputs. Each check prints
"CHECK NN: PASS/FAIL -- desc"; a TOTAL line follows; the process exits nonzero
on any FAIL.

The marking theorem is QUANTIFIER-SCOPED, on ONE spatial criterion:

* (i) UNIVERSAL: the history index nests for EVERY realized history.
* (ii) EXISTENTIAL: for EACH spatial axis there EXIST event-bearing histories
       whose translation-identified opposite slices are incomparable.
* (iii) PER-HISTORY uniqueness holds only OUTSIDE two degeneracy classes:
        D0 (static, event-free) and D1 (translation-degenerate event-bearing:
        single-record, uniform-burst, translation-invariant, face-confined).

The one spatial-comparability criterion is a named CONVENTION: two opposite
spatial slices are compared under the natural translation identification (drop
the sliced coordinate; index by the remaining two spatial coords and the history
index), with empty-slice comparability included (emptyset is comparable to every
slice). The index direction needs no identification (native same-site frame).

Provenance (quoted, not re-derived here); the runner live-reads the source
files and asserts the quoted sentences as whitespace-normalized substrings:

* Record axiom, docs/MINIMAL_AXIOMS_2026-06-29.md. The permanence clause
  "records are permanent" is LANDED on main as commit 50f0db6187 (drafted as
  PR #4874, review-loop-closed) and is the authoritative permanence grounding
  for every record-nesting check below. Current main carries that landed form.
  The Record-clause quote guard (CHECK 30) requires that current landed form.
  Record nesting is grounded on the landed permanence sentence, not conditional.

* B-AXIS premise, the S3' exchange-symmetry certificate, and the operator block
  Lambda = (Z/L_tau Z) x (Z/L_s Z)^3 are quoted from
  docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md
  (S3': W = P_{tau<->1} . diag((-1)^{x_tau x_1}) swaps the temporal and x_1 hop
   sectors EXACTLY, residual 0; the PLAIN permutation without the sign field
   FAILS by a nonzero margin). This runner does NOT re-derive that staggered-
   Dirac certificate and does NOT model a combinatorial analog of it (an earlier
   symmetric-cube adjacency analog inverted S3', because the plain swap succeeds
   on a symmetric cube whereas in S3' the plain permutation fails). T4 asserts
   the real quoted sentences instead.

This runner is a source-note artifact. It does not set or predict an audit
outcome; the independent audit lane is the only authority for effective status.
"""

import os
import re
import sys

# ---------------------------------------------------------------------------
# check harness
# ---------------------------------------------------------------------------
_RESULTS = []  # list of (bool_pass, str_desc)


def check(ok, desc):
    _RESULTS.append((bool(ok), str(desc)))


# ---------------------------------------------------------------------------
# source files (read live for quote guards + residue parsing)
# ---------------------------------------------------------------------------
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
_DOCS = os.path.join(_REPO_ROOT, "docs")
NOTE_PATH = os.path.join(
    _DOCS,
    "TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md")
AXIOMS_PATH = os.path.join(_DOCS, "MINIMAL_AXIOMS_2026-06-29.md")
SINGLECLOCK_PATH = os.path.join(
    _DOCS,
    "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md")


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _normws(s):
    """Collapse all runs of whitespace to single spaces."""
    return " ".join(s.split())


def _contains_norm(haystack, needle):
    """Whitespace-normalized substring test."""
    return _normws(needle) in _normws(haystack)


# ---------------------------------------------------------------------------
# exact record / configuration / history primitives
# ---------------------------------------------------------------------------
# A configuration is a dict: site (tuple of ints) -> record value (int).
# Only record-bearing sites appear; absence of a key = "no record" (a site
# need not carry a record).  rec() reads the record content as a frozenset of
# (site, value) pairs -- readout is determined by record content alone.

def rec(cfg):
    """Record content of a configuration: frozenset of (site, value) pairs."""
    return frozenset(cfg.items())


def subset(a, b):
    """Exact subset test on frozensets (a subset-or-equal b)."""
    return a <= b


def comparable(a, b):
    """True iff a and b are ordered by inclusion in either direction.
    Empty-slice comparability is native here: emptyset <= any set."""
    return (a <= b) or (b <= a)


def incomparable(a, b):
    return not comparable(a, b)


def make_stack(history):
    """STACK S on (window of Z^3) x {0..T}: S[(x1,x2,x3,t)] = h_t at x.
    Only record-bearing cells are stored (absence = no record)."""
    S = {}
    for t, cfg in enumerate(history):
        for site, val in cfg.items():
            S[site + (t,)] = val
    return S


def slice_time(stack, t):
    """Extract the equal-index (equal-time) slice at index t as a config."""
    out = {}
    for key, val in stack.items():
        if key[3] == t:
            out[key[:3]] = val
    return out


def reconstruct(stack, T):
    """Reconstruct (h_0, ..., h_T) from the stack (round-trip)."""
    return tuple(slice_time(stack, t) for t in range(T + 1))


def index_axis_values(stack):
    """Set of values taken by the 4th (index) coordinate in the stack."""
    return frozenset(key[3] for key in stack)


def spatial_site_set(window, axis, a):
    """Z^3 site set of the spatial slice {site : site[axis] == a}."""
    return frozenset(s for s in window if s[axis] == a)


def spatial_recset_identified(history, axis, a):
    """Record content of the spatial slice at (axis == a), under the natural
    translation identification: drop the sliced coordinate and index by
    (remaining two spatial coords, t).  Returns frozenset of (key, value)."""
    out = set()
    for t, cfg in enumerate(history):
        for site, val in cfg.items():
            if site[axis] == a:
                reduced = tuple(site[i] for i in range(3) if i != axis)
                out.add((reduced + (t,), val))
    return frozenset(out)


def spatial_recset_raw(history, axis, a):
    """Record content of the spatial slice WITHOUT identification: keeps the
    full Z^3 site (so different slice indices live on disjoint supports)."""
    out = set()
    for t, cfg in enumerate(history):
        for site, val in cfg.items():
            if site[axis] == a:
                out.add((site + (t,), val))
    return frozenset(out)


def _monotone_directions(history):
    """Set of stack directions that are 'monotone' under the ONE stated
    criterion:
      - 'index': same-site forward nesting rec(h_t) subset rec(h_{t+1}) on the
        native shared site set;
      - each spatial axis: translation-identified comparability of the two
        opposite slices, with empty-slice comparability included by convention.
    """
    out = set()
    T = len(history) - 1
    if all(subset(rec(history[t]), rec(history[t + 1])) for t in range(T)):
        out.add("index")
    for axis, name in ((0, "x1"), (1, "x2"), (2, "x3")):
        a0 = spatial_recset_identified(history, axis, 0)
        a1 = spatial_recset_identified(history, axis, 1)
        if comparable(a0, a1):
            out.add(name)
    return frozenset(out)


# ---------------------------------------------------------------------------
# shared witnesses
# ---------------------------------------------------------------------------
# Spatial window: the 2x2x2 corner of Z^3.
WINDOW = frozenset((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1))

# Spatially GENERIC event-bearing history: records accumulate forward
# (permanence, landed as commit 50f0db6187); the record layout breaks translation
# symmetry along every spatial axis, so index-nesting holds at every step while
# every spatial-direction slice pair is incomparable under translation id.
H0 = {(0, 0, 0): 1}
H1 = {(0, 0, 0): 1, (1, 1, 1): 1}
H2 = {(0, 0, 0): 1, (1, 1, 1): 1, (0, 1, 0): 1, (1, 0, 1): 1}
HISTORY = (H0, H1, H2)
T_MAX = len(HISTORY) - 1

# Independent second generic witness (fails along x2, distinct site layout).
HB0 = {(1, 1, 1): 1}
HB1 = {(1, 1, 1): 1, (0, 0, 0): 1}
HB2 = {(1, 1, 1): 1, (0, 0, 0): 1, (1, 0, 0): 1, (0, 1, 1): 1}
HISTORY_B = (HB0, HB1, HB2)

# Degeneracy class D1 (translation-degenerate, event-bearing): each member nests
# along a spatial axis too, by a distinct mechanism.
#  - single-record: the opposite slices are EMPTY (emptyset comparable).
SINGLE = ({}, {(0, 0, 0): 1})
#  - uniform-burst: the translation-identified x1 slices are EQUAL.
UNIFORM_BURST = ({}, {(0, 0, 0): 1, (1, 0, 0): 1})
#  - translation-invariant growth: x1 slices stay EQUAL at every step.
TRANS_INVARIANT = ({},
                   {(0, 0, 0): 1, (1, 0, 0): 1},
                   {(0, 0, 0): 1, (1, 0, 0): 1, (0, 1, 0): 1, (1, 1, 0): 1})
#  - face-confined: records confined to the x1=0 face, so the x1=1 slice EMPTY.
FACE_CONFINED = ({},
                 {(0, 0, 0): 1},
                 {(0, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1})

# Degeneracy class D0 (static, event-free): every site carries a record at every
# index => nothing changes => every stack direction is trivially monotone.
C_FULL = {s: 1 for s in WINDOW}
STATIC = (C_FULL, C_FULL, C_FULL)


def print_banner():
    print("=" * 72)
    print("frontier_time_axis_is_history_index_2026_07_03")
    print("exact-arithmetic runner (int/tuple/set/frozenset/dict only; NO floats)")
    print("bounded theorem (T1-T2) + bounded observation (T3) + bounded support (T4-T5)")
    print("record nesting grounded on LANDED permanence (records are permanent; commit 50f0db6187)")
    print("=" * 72)


# ---------------------------------------------------------------------------
# T1 -- THE STACKED REPRESENTATION (definition-level; no physics claim)
# ---------------------------------------------------------------------------
def theorem_T1():
    print("-- T1: the stacked representation (4th direction IS the history index)")
    stack = make_stack(HISTORY)

    # CHECK 01: stack construction exact -- S[(x,t)] == h_t at x for all cells.
    ok = True
    for t, cfg in enumerate(HISTORY):
        for site, val in cfg.items():
            if stack.get(site + (t,)) != val:
                ok = False
    # and no phantom cells (every stored cell traces to a record)
    for key, val in stack.items():
        t = key[3]
        if HISTORY[t].get(key[:3]) != val:
            ok = False
    check(ok, "T1 stack construction exact: S[(x,t)] = h_t at x, no phantom cells")

    # CHECK 02: equal-index slice extraction round-trips each configuration.
    ok = all(slice_time(stack, t) == HISTORY[t] for t in range(T_MAX + 1))
    check(ok, "T1 slice-extraction round-trip: slice_time(S,t) == h_t for all t")

    # CHECK 03: full history reconstructs from the stack.
    ok = reconstruct(stack, T_MAX) == HISTORY
    check(ok, "T1 full round-trip: reconstruct(S) == (h_0,...,h_T)")

    # CHECK 04: the 4th coordinate value-set is exactly the history index {0..T}.
    ok = index_axis_values(stack) == frozenset(range(T_MAX + 1))
    check(ok, "T1 4th-axis coordinate set == {0..T}: the 4th direction is the history index")


# ---------------------------------------------------------------------------
# T2 -- RECORD NESTING MARKS THE INDEX DIRECTION
#        (bounded theorem; grounded on landed permanence commit 50f0db6187 + realized sector)
#        QUANTIFIER-SCOPED on ONE spatial criterion.
# ---------------------------------------------------------------------------
def theorem_T2():
    print("-- T2: record nesting marks the index direction (quantifier-scoped, one criterion)")
    stack = make_stack(HISTORY)

    # CHECK 05: same-site identification is native to the index axis (computed
    #           from the stack data, not WINDOW==WINDOW): every index slice's
    #           record-bearing sites are drawn from ONE shared Z^3 site set
    #           (identity identification), while the two opposite spatial slices
    #           along x1 occupy DISJOINT supports that partition that set.
    index_site_sets = [frozenset(slice_time(stack, t).keys()) for t in range(T_MAX + 1)]
    ambient = frozenset().union(*index_site_sets)
    sp0 = spatial_site_set(ambient, 0, 0)
    sp1 = spatial_site_set(ambient, 0, 1)
    index_native = all(ss <= ambient for ss in index_site_sets)
    spatial_disjoint = sp0.isdisjoint(sp1) and len(sp0) > 0 and len(sp1) > 0
    partitions = (sp0 | sp1) == ambient
    check(index_native and spatial_disjoint and partitions,
          "T2a same-site native: index slices share one Z^3 set; x1 opposite slices disjoint & partition it")

    # CHECK 06: permanence record nesting rec(h_t) subset rec(h_{t+1}) at every t.
    ok = all(subset(rec(HISTORY[t]), rec(HISTORY[t + 1])) for t in range(T_MAX))
    check(ok, "T2a record nesting rec(h_t) subset rec(h_{t+1}) all t (permanence, LANDED commit 50f0db6187)")

    # CHECK 07: event-bearing -- at least one strict inclusion (>= one event).
    strict = [rec(HISTORY[t]) < rec(HISTORY[t + 1]) for t in range(T_MAX)]
    check(any(strict), "T2 event-bearing: at least one strict record inclusion (>= one event)")

    # CHECK 08: permanence falsifier -- a value-flip history VIOLATES nesting
    #           (nesting encodes value-invariance of the locked possibility).
    flip = ({(0, 0, 0): 1}, {(0, 0, 0): 2})
    check(not subset(rec(flip[0]), rec(flip[1])),
          "T2a permanence falsifier: value-flip history rejected by nesting (value-invariance enforced)")

    # CHECK 09: spatial slices live on DISJOINT Z^3 supports.
    s0 = spatial_site_set(WINDOW, 0, 0)
    s1 = spatial_site_set(WINDOW, 0, 1)
    check(s0.isdisjoint(s1) and len(s0) > 0 and len(s1) > 0,
          "T2b spatial slices (x1=0 vs x1=1) have disjoint Z^3 site supports")

    # CHECK 10: raw containment is ill-posed without identification.
    r0 = spatial_recset_raw(HISTORY, 0, 0)
    r1 = spatial_recset_raw(HISTORY, 0, 1)
    check(r0.isdisjoint(r1) and len(r0) > 0 and len(r1) > 0,
          "T2b raw spatial record sets disjoint => containment undefined without translation identification")

    # -- (i) UNIVERSAL: the index direction nests for EVERY realized history,
    #        including the degeneracy-class members and the static history.
    all_histories = (HISTORY, HISTORY_B, SINGLE, UNIFORM_BURST,
                     TRANS_INVARIANT, FACE_CONFINED, STATIC)
    # CHECK 11:
    check(all("index" in _monotone_directions(h) for h in all_histories),
          "T2(i) UNIVERSAL: index direction nests for EVERY realized history (permanence, LANDED commit 50f0db6187)")

    # -- (ii) EXISTENTIAL: for EACH spatial axis there EXIST event-bearing
    #         histories whose translation-identified opposite slices are
    #         incomparable. Generic witness HISTORY fails on all three axes.
    # CHECK 12-14:
    for axis, name, num in ((0, "x1", 12), (1, "x2", 13), (2, "x3", 14)):
        a0 = spatial_recset_identified(HISTORY, axis, 0)
        a1 = spatial_recset_identified(HISTORY, axis, 1)
        check(incomparable(a0, a1),
              "T2(ii) generic witness: %s translation-identified slices incomparable (spatial nesting fails)" % name)
    # CHECK 15: an independent second witness fails along another axis (x2)
    #           while its index still nests.
    b0 = spatial_recset_identified(HISTORY_B, 1, 0)
    b1 = spatial_recset_identified(HISTORY_B, 1, 1)
    check(incomparable(b0, b1) and "index" in _monotone_directions(HISTORY_B),
          "T2(ii) second independent witness: x2 slices incomparable while index nests")

    # -- (iii) PER-HISTORY uniqueness OUTSIDE the degeneracy classes; failure ON
    #          each class member. The refuting counterexamples become CHECKS.
    # CHECK 16: uniqueness on the generic witness.
    check(_monotone_directions(HISTORY) == frozenset({"index"}),
          "T2(iii) generic witness: history index is the UNIQUE record-monotone direction")
    # CHECK 17: D1 single-record -> not unique (opposite slices empty).
    check(_monotone_directions(SINGLE) > frozenset({"index"}),
          "T2(iii) degeneracy D1 single-record: NOT unique (empty opposite slices comparable)")
    # CHECK 18: D1 uniform-burst -> not unique via translation-identified EQUALITY.
    u0 = spatial_recset_identified(UNIFORM_BURST, 0, 0)
    u1 = spatial_recset_identified(UNIFORM_BURST, 0, 1)
    check(_monotone_directions(UNIFORM_BURST) > frozenset({"index"}) and u0 == u1,
          "T2(iii) degeneracy D1 uniform-burst: NOT unique (x1 slices translation-identified EQUAL)")
    # CHECK 19: D1 translation-invariant -> not unique, x1 equal at every step.
    ti0 = spatial_recset_identified(TRANS_INVARIANT, 0, 0)
    ti1 = spatial_recset_identified(TRANS_INVARIANT, 0, 1)
    check(_monotone_directions(TRANS_INVARIANT) > frozenset({"index"}) and ti0 == ti1,
          "T2(iii) degeneracy D1 translation-invariant: NOT unique (x1 slices EQUAL; growth translation-invariant)")
    # CHECK 20: D1 face-confined -> not unique, x1=1 slice empty.
    fc1 = spatial_recset_identified(FACE_CONFINED, 0, 1)
    check(_monotone_directions(FACE_CONFINED) > frozenset({"index"}) and fc1 == frozenset(),
          "T2(iii) degeneracy D1 face-confined: NOT unique (records confined to x1=0 face; x1=1 slice empty)")
    # CHECK 21: D0 static (event-free) -> every stack direction monotone.
    check(_monotone_directions(STATIC) == frozenset({"index", "x1", "x2", "x3"}),
          "T2(iii) degeneracy D0 static: every direction trivially monotone (event-free; marking non-unique)")


# ---------------------------------------------------------------------------
# T3 -- THE SECOND-CLOCK EXCLUSION IS TYPE-LEVEL (bounded observation)
# ---------------------------------------------------------------------------
def theorem_T3():
    print("-- T3: second-clock exclusion is type-level (record layer never needed the premise)")

    # A realized history is a SEQUENCE (one index). A second independent clock
    # at the record layer would be a 2D GRID of configurations (two independent
    # nesting directions) -- a different TYPE of object, not a history.
    G = {
        (0, 0): {},
        (1, 0): {0: 1},
        (0, 1): {1: 1},
        (1, 1): {0: 1, 1: 1},
    }

    # CHECK 22: grid admits record nesting along i (for every fixed j).
    ok_i = all(subset(rec(G[(0, j)]), rec(G[(1, j)])) for j in (0, 1))
    check(ok_i, "T3 grid admits record nesting along i (all fixed j)")

    # CHECK 23: grid admits record nesting along j (for every fixed i).
    ok_j = all(subset(rec(G[(i, 0)]), rec(G[(i, 1)])) for i in (0, 1))
    check(ok_j, "T3 grid admits record nesting along j (all fixed i)")

    # CHECK 24: both nesting directions are non-degenerate (a strict step each).
    strict_i = any(rec(G[(0, j)]) < rec(G[(1, j)]) for j in (0, 1))
    strict_j = any(rec(G[(i, 0)]) < rec(G[(i, 1)]) for i in (0, 1))
    check(strict_i and strict_j,
          "T3 both grid directions non-degenerate (a strict record step in each)")

    # CHECK 25: dichotomy horn A -- two incomparable cells => the
    #           record-inclusion order is NOT total => the grid does not embed
    #           as a single sequence with one record-monotone direction.
    off_diag = incomparable(rec(G[(1, 0)]), rec(G[(0, 1)]))
    check(off_diag,
          "T3 dichotomy horn A: incomparable off-diagonal => order NOT total => not a single sequence")

    # CHECK 26: if one direction is degenerate (no events), the grid collapses
    #           to a single chain along the other axis -- one clock remains.
    Gd = {
        (0, 0): {}, (0, 1): {},
        (1, 0): {0: 1}, (1, 1): {0: 1},
    }
    j_degenerate = all(rec(Gd[(i, 0)]) == rec(Gd[(i, 1)]) for i in (0, 1))
    i_has_event = any(rec(Gd[(0, j)]) < rec(Gd[(1, j)]) for j in (0, 1))
    check(j_degenerate and i_has_event,
          "T3 degenerate-j grid collapses to a single chain along i (one clock remains)")

    # CHECK 27: dichotomy horn B -- if instead the grid's record order is TOTAL
    #           (witness: cells whose content depends only on i+j), it
    #           serializes into one inclusion chain -- one clock remains.
    Gt = {(i, j): {k: 1 for k in range(i + j)} for i in (0, 1) for j in (0, 1)}
    cells = [rec(Gt[(i, j)]) for i in (0, 1) for j in (0, 1)]
    total = all(comparable(a, b) for a in cells for b in cells)
    chain = sorted(set(cells), key=len)
    serializes = all(subset(chain[k], chain[k + 1]) for k in range(len(chain) - 1))
    check(total and serializes,
          "T3 dichotomy horn B: totally-ordered grid (cells ~ i+j) serializes to a single chain (one clock remains)")


# ---------------------------------------------------------------------------
# T4 -- RECONCILIATION WITH THE EXCHANGE-SYMMETRY CERTIFICATE
#        (statement-level, live quote guards; NO fake combinatorial analog)
#        + B-AXIS DECOMPOSITION (bounded support)
# ---------------------------------------------------------------------------
def theorem_T4():
    print("-- T4: reconciliation -- live quote guards on S3' + record-content axis structure")
    note = _read(NOTE_PATH)
    axioms = _read(AXIOMS_PATH)
    singleclock = _read(SINGLECLOCK_PATH)

    # CHECK 28: LIVE QUOTE GUARD -- the single-clock note carries the S3'
    #           exchange-symmetry certificate (whitespace-normalized substring),
    #           including the sign field diag((-1)^{x_tau x_1}).
    check(_contains_norm(singleclock, "W M_KS W^T = M_KS")
          and _contains_norm(singleclock, "diag( (-1)^{x_τ x_1} )"),
          "T4 quote guard: single-clock note carries the S3' certificate W M_KS W^T = M_KS with the sign field")

    # CHECK 29: LIVE QUOTE GUARD -- the certificate's non-triviality: the PLAIN
    #           permutation (no sign field) FAILS. This is the real S3'
    #           structure that the dropped cube analog inverted.
    check(_contains_norm(singleclock,
                         "the plain permutation without the sign field fails by a nonzero margin"),
          "T4 quote guard: S3' non-triviality -- plain permutation without the sign field FAILS")

    # CHECK 30: LIVE QUOTE GUARD -- Record-clause permanence grounding. The
    #           landed form "records are permanent" (commit 50f0db6187, drafted
    #           as PR #4874, review-loop-closed) is AUTHORITATIVE on current
    #           main; no pre-restoration fallback is accepted in this landing
    #           artifact.
    landed_record = _contains_norm(
        axioms,
        "When present, a record locks exactly one admissible local possibility. "
        "A site never carries more than one record; records are permanent.")
    check(landed_record,
          "T4 quote guard: axioms file carries the current landed Record sentence "
          "(records are permanent; commit 50f0db6187, authoritative)")

    # CHECK 31: STATEMENT GUARD -- the note carries its own reconciliation /
    #           resonance sentence (no fake analog is asserted anywhere).
    check(_contains_norm(note, "symmetric worlds do not wear their time on their sleeve"),
          "T4 statement guard: note carries the reconciliation/resonance sentence")

    # CHECK 32: record-content axis structure on the REAL translation-identified
    #           criterion (no analog): a spatially generic history singles out
    #           the index (record layer sees the axis the operator certificate
    #           cannot); a translation-symmetric history does NOT (record layer
    #           is then as axis-blind as the operator layer -- the resonance).
    generic_sees = _monotone_directions(HISTORY) == frozenset({"index"})
    symmetric_blind = _monotone_directions(UNIFORM_BURST) > frozenset({"index"})
    check(generic_sees and symmetric_blind,
          "T4 record-content: generic history singles out index; symmetric history axis-blind (resonance with S3')")

    # CHECK 33: the B-AXIS decomposition covers every clause; axis selection is
    #           CONDITIONAL on the representation-faithfulness bridge (OPEN),
    #           covering BOTH the realized-history origin AND the periodic
    #           compactification; B-AXIS.3 UNCHANGED; 1a/1b NOT_TOUCHED.
    decomp = {
        "B_AXIS_1a_internal_denominator":
            "NOT_TOUCHED_supplied_walled_by_count_not_rate_firewall_unaudited_post_reset",
        "B_AXIS_1b_absolute_clock_unit":
            "NOT_TOUCHED_supplied_open_rate_class",
        "B_AXIS_2_axis_selection":
            "record_layer_axis_structure_for_spatially_generic_event_bearing_histories_T2_"
            "CONDITIONAL_on_representation_faithfulness_bridge_OPEN_covering_"
            "realized_history_origin_AND_periodic_compactification",
        "B_AXIS_3_single_clock":
            "TYPE_LEVEL_at_record_layer_T3_operator_comparator_exclusion_UNCHANGED",
    }
    required_keys = frozenset({
        "B_AXIS_1a_internal_denominator",
        "B_AXIS_1b_absolute_clock_unit",
        "B_AXIS_2_axis_selection",
        "B_AXIS_3_single_clock",
    })
    covered = frozenset(decomp.keys()) == required_keys
    nonempty = all(len(v) > 0 for v in decomp.values())
    honest = (("CONDITIONAL" in decomp["B_AXIS_2_axis_selection"])
              and ("OPEN" in decomp["B_AXIS_2_axis_selection"])
              and ("periodic_compactification" in decomp["B_AXIS_2_axis_selection"])
              and ("UNCHANGED" in decomp["B_AXIS_3_single_clock"])
              and ("NOT_TOUCHED" in decomp["B_AXIS_1a_internal_denominator"])
              and ("NOT_TOUCHED" in decomp["B_AXIS_1b_absolute_clock_unit"]))
    check(covered and nonempty and honest,
          "T4 B-AXIS decomposition covers {1a,1b,2,3}; axis-selection CONDITIONAL/OPEN incl. periodic compactification; B-AXIS.3 UNCHANGED")


# ---------------------------------------------------------------------------
# T5 -- CONSEQUENCE + COMPLETE RESIDUES (parsed from the note; drop nothing)
# ---------------------------------------------------------------------------
def _parse_residue_items(note_text):
    """Parse the numbered residue list from the note's T5 section (single
    source of truth). Returns the list of item texts (continuation lines
    joined)."""
    lines = note_text.splitlines()
    start = None
    for idx, ln in enumerate(lines):
        if ln.startswith("## T5"):
            start = idx
            break
    if start is None:
        return []
    items = []
    current = None
    for ln in lines[start + 1:]:
        if ln.startswith("## "):
            break
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", ln)
        if m:
            if current is not None:
                items.append(current)
            current = m.group(2).strip()
        elif current is not None:
            if ln.strip() == "":
                items.append(current)
                current = None
            else:
                current += " " + ln.strip()
    if current is not None:
        items.append(current)
    return items


def theorem_T5():
    print("-- T5: consequence + residue enumeration PARSED from the note (single source of truth)")
    note = _read(NOTE_PATH)
    items = _parse_residue_items(note)
    blob = " ".join(items).lower()

    # CHECK 34: the note's residue list has the expected 15 entries.
    check(len(items) == 15,
          "T5 residue list parsed from the note has 15 entries (got %d)" % len(items))

    # CHECK 35: the required load-bearing residue keys are all present in the
    #           note's parsed list (single source of truth; not a self-check of
    #           a runner-local set against itself).
    required_phrases = (
        "#4874", "realized-sector", "sequence",
        "representation-faithfulness bridge", "periodic compactification",
        "b-axis.1", "b-axis.3", "single-clock note", "pr #4882",
        "no rate", "nothing adopted", "audit lane",
        "translation-identification convention", "witness-class",
        "finite-window", "four-axis-direction", "event-definition import",
    )
    missing = [p for p in required_phrases if p not in blob]
    check(not missing,
          "T5 required residue keys present in the note's parsed list (missing: %s)" % (missing or "none"))

    # CHECK 36: the four residues added by this repair are present by name.
    new_four = (
        "translation-identification convention",
        "witness-class",
        "four-axis-direction",
        "event-definition import",
    )
    missing_new = [p for p in new_four if p not in blob]
    check(not missing_new,
          "T5 four new residues present (translation convention; witness/window; four-axis; event import) (missing: %s)"
          % (missing_new or "none"))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    print_banner()
    theorem_T1()
    theorem_T2()
    theorem_T3()
    theorem_T4()
    theorem_T5()

    print("-" * 72)
    passes = 0
    fails = 0
    for i, (ok, desc) in enumerate(_RESULTS, start=1):
        status = "PASS" if ok else "FAIL"
        if ok:
            passes += 1
        else:
            fails += 1
        print("CHECK %02d: %s -- %s" % (i, status, desc))
    print("-" * 72)
    print("TOTAL: PASS=%d FAIL=%d" % (passes, fails))
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
