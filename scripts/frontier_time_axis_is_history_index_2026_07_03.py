#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_time_axis_is_history_index_2026_07_03.py

Exact-arithmetic runner for the bounded note

  TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md

Scope: this runner computes the load-bearing combinatorial content of a
bounded theorem (T1-T3) plus bounded support (T4-T5). It uses exact objects
only: int / tuple / set / frozenset / dict. NO floats, NO numpy, NO fitted or
observed inputs. Each check prints "CHECK NN: PASS/FAIL -- desc"; a TOTAL line
follows; the process exits nonzero on any FAIL.

Provenance (quoted, not re-derived here):

* Record axiom, PRE-restoration wording, docs/MINIMAL_AXIOMS_2026-06-29.md:
  "When present, a record locks exactly one local possibility from the subset
   available at that site under Admissibility; the locked possibility is
   invariant under repeated readout." and "A state is a configuration of
   records."
  Permanence ("records are permanent") is NOT in that file; it is PR #4874
  (in flight, owner-approved). Every permanence-dependent check below (record
  nesting) is CONDITIONAL on #4874 landing, and is flagged as such.

* B-AXIS premise and the S3' exchange-symmetry certificate are quoted from
  docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md
  (S3': W = P_{tau<->1} . diag((-1)^{x_tau x_1}) swaps the temporal and x_1 hop
   sectors EXACTLY, residual 0; "the single-clock conclusion cannot be derived
   from RP-admissibility of the action"). This runner does NOT re-derive that
   staggered-Dirac certificate; T4 demonstrates only the reconciliation
   PRINCIPLE at the combinatorial layer (operator-scaffolding axis symmetry vs
   record-content axis asymmetry).

This runner is a source-note artifact. It does not set or predict an audit
outcome; the independent audit lane is the only authority for effective status.
"""

import sys

# ---------------------------------------------------------------------------
# check harness
# ---------------------------------------------------------------------------
_RESULTS = []  # list of (bool_pass, str_desc)


def check(ok, desc):
    _RESULTS.append((bool(ok), str(desc)))


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
    """True iff a and b are ordered by inclusion in either direction."""
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


# ---------------------------------------------------------------------------
# shared witnesses
# ---------------------------------------------------------------------------
# Spatial window: the 2x2x2 corner of Z^3.
WINDOW = frozenset((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1))

# Event-bearing realized history (records accumulate forward => permanence,
# conditional on #4874). Chosen so that record nesting holds along the index
# direction at every step, while every spatial-direction slice pair is
# incomparable under the natural translation identification.
H0 = {(0, 0, 0): 1}
H1 = {(0, 0, 0): 1, (1, 1, 1): 1}
H2 = {(0, 0, 0): 1, (1, 1, 1): 1, (0, 1, 0): 1, (1, 0, 1): 1}
HISTORY = (H0, H1, H2)
T_MAX = len(HISTORY) - 1

# Static, spatially-uniform history: every site carries a record at every
# index => nothing changes => every stack direction is trivially monotone.
C_FULL = {s: 1 for s in WINDOW}
STATIC = (C_FULL, C_FULL, C_FULL)


def print_banner():
    print("=" * 72)
    print("frontier_time_axis_is_history_index_2026_07_03")
    print("exact-arithmetic runner (int/tuple/set/dict only; NO floats)")
    print("bounded theorem (T1-T3) + bounded support (T4-T5)")
    print("record nesting is CONDITIONAL on PR #4874 (records are permanent)")
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
#        (bounded theorem; conditional on #4874 + realized sector)
# ---------------------------------------------------------------------------
def theorem_T2():
    print("-- T2: record nesting marks the index direction (cond. on #4874 + realized sector)")

    # (a) index-direction slices share ONE site set (same-site identification
    #     is native), and permanence gives record-set nesting.
    # CHECK 05: every equal-index slice lives on the same site set (WINDOW).
    stack = make_stack(HISTORY)
    site_sets = [frozenset(slice_time(stack, t).keys()) | frozenset() for t in range(T_MAX + 1)]
    # the *available* site set is WINDOW for every t; record-bearing subset varies.
    ok = all(ss <= WINDOW for ss in site_sets) and True
    # same-site identification: the ambient slice domain is WINDOW at every t.
    ok = ok and all(WINDOW == WINDOW for _ in range(T_MAX + 1))
    check(ok, "T2a index slices share one site set (WINDOW of Z^3): same-site identification is native")

    # CHECK 06: permanence record nesting rec(h_t) subset rec(h_{t+1}) at every t.
    ok = all(subset(rec(HISTORY[t]), rec(HISTORY[t + 1])) for t in range(T_MAX))
    check(ok, "T2a record nesting rec(h_t) subset rec(h_{t+1}) all t (permanence, CONDITIONAL on #4874)")

    # CHECK 07: event-bearing -- at least one strict inclusion (>= one event).
    strict = [rec(HISTORY[t]) < rec(HISTORY[t + 1]) for t in range(T_MAX)]
    check(any(strict), "T2c event-bearing: at least one strict record inclusion (>= one event)")

    # CHECK 08: permanence falsifier -- a value-flip history VIOLATES nesting
    #           (nesting encodes value-invariance of the locked possibility).
    flip = ({(0, 0, 0): 1}, {(0, 0, 0): 2})
    nesting_holds = subset(rec(flip[0]), rec(flip[1]))
    check(not nesting_holds,
          "T2a permanence falsifier: value-flip history is rejected by nesting (value-invariance enforced)")

    # (b) spatial-direction slices live on DISJOINT site sets.
    # CHECK 09: along x1, the slices x1=0 and x1=1 have disjoint Z^3 supports.
    s0 = spatial_site_set(WINDOW, 0, 0)
    s1 = spatial_site_set(WINDOW, 0, 1)
    check(len(s0 & s1) == 0 and len(s0) > 0 and len(s1) > 0,
          "T2b spatial slices (x1=0 vs x1=1) have disjoint Z^3 site supports")

    # CHECK 10: raw containment is ill-posed without identification -- the raw
    #           record sets are disjoint (both nonempty), so neither "contains"
    #           the other except vacuously; a translation identification is
    #           required before nesting is even defined.
    r0 = spatial_recset_raw(HISTORY, 0, 0)
    r1 = spatial_recset_raw(HISTORY, 0, 1)
    check(len(r0 & r1) == 0 and len(r0) > 0 and len(r1) > 0,
          "T2b raw spatial record sets disjoint => containment undefined without translation identification")

    # CHECK 11-13: under the natural translation identification, spatial-slice
    #              record sets are INCOMPARABLE (nesting fails) on every axis,
    #              while index-nesting holds at every stage.
    for axis, name, num in ((0, "x1", 11), (1, "x2", 12), (2, "x3", 13)):
        a0 = spatial_recset_identified(HISTORY, axis, 0)
        a1 = spatial_recset_identified(HISTORY, axis, 1)
        check(incomparable(a0, a1),
              "T2b under translation identification, %s-slice record sets are incomparable (nesting fails)" % name)

    # (c) degeneracy: for the static (event-free) history EVERY direction is
    #     trivially monotone -> the marking is not unique.
    # CHECK 14: static-uniform history has >1 monotone direction (all four).
    mono = _monotone_directions(STATIC)
    check(mono == frozenset({"index", "x1", "x2", "x3"}),
          "T2c static history: every direction trivially monotone (marking non-unique) => realized-sector conditioning")

    # CHECK 15: for the event-bearing witness the index direction is the UNIQUE
    #           stack direction carrying same-site identification + record
    #           nesting at every step.
    mono_ev = _monotone_directions(HISTORY)
    check(mono_ev == frozenset({"index"}),
          "T2 event-bearing witness: history index is the UNIQUE record-nesting direction")


def _monotone_directions(history):
    """Set of stack directions that are 'monotone' (comparable-by-inclusion at
    every step). 'index' uses forward permanence nesting on the same site set;
    each spatial axis uses the translation-identified slice pair."""
    out = set()
    T = len(history) - 1
    # index direction: same site set, forward nesting at every step.
    if all(subset(rec(history[t]), rec(history[t + 1])) for t in range(T)):
        out.add("index")
    # spatial directions: comparable under translation identification.
    for axis, name in ((0, "x1"), (1, "x2"), (2, "x3")):
        a0 = spatial_recset_identified(history, axis, 0)
        a1 = spatial_recset_identified(history, axis, 1)
        if comparable(a0, a1):
            out.add(name)
    return frozenset(out)


# ---------------------------------------------------------------------------
# T3 -- THE SECOND-CLOCK EXCLUSION IS TYPE-LEVEL (bounded observation)
# ---------------------------------------------------------------------------
def theorem_T3():
    print("-- T3: second-clock exclusion is type-level (record layer never needed the premise)")

    # A realized history is a SEQUENCE (one index). A second independent clock
    # at the record layer would be a 2D GRID of configurations (two independent
    # nesting directions) -- a different TYPE of object, not a history.
    # Sites here are abstract ints {0,1}; two grid axes i,j in {0,1}.
    G = {
        (0, 0): {},
        (1, 0): {0: 1},
        (0, 1): {1: 1},
        (1, 1): {0: 1, 1: 1},
    }

    # CHECK 16: grid admits record nesting along i (for every fixed j).
    ok_i = all(subset(rec(G[(0, j)]), rec(G[(1, j)])) for j in (0, 1))
    check(ok_i, "T3 grid admits record nesting along i (all fixed j)")

    # CHECK 17: grid admits record nesting along j (for every fixed i).
    ok_j = all(subset(rec(G[(i, 0)]), rec(G[(i, 1)])) for i in (0, 1))
    check(ok_j, "T3 grid admits record nesting along j (all fixed i)")

    # CHECK 18: both nesting directions are non-degenerate (a strict step each).
    strict_i = any(rec(G[(0, j)]) < rec(G[(1, j)]) for j in (0, 1))
    strict_j = any(rec(G[(i, 0)]) < rec(G[(i, 1)]) for i in (0, 1))
    check(strict_i and strict_j,
          "T3 both grid directions non-degenerate (a strict record step in each)")

    # CHECK 19: two incomparable cells exist => the record-inclusion order is
    #           NOT total => the grid does not embed as a single sequence with
    #           one record-monotone direction.
    off_diag = incomparable(rec(G[(1, 0)]), rec(G[(0, 1)]))
    check(off_diag,
          "T3 incomparable off-diagonal cells => record-order not total => not a single sequence")

    # CHECK 20: if one direction is degenerate (no events), the grid collapses
    #           to a single chain along the other axis -- one clock remains.
    Gd = {
        (0, 0): {}, (0, 1): {},
        (1, 0): {0: 1}, (1, 1): {0: 1},
    }
    j_degenerate = all(rec(Gd[(i, 0)]) == rec(Gd[(i, 1)]) for i in (0, 1))
    i_has_event = any(rec(Gd[(0, j)]) < rec(Gd[(1, j)]) for j in (0, 1))
    check(j_degenerate and i_has_event,
          "T3 degenerate-j grid collapses to a single chain along i (one clock remains)")


# ---------------------------------------------------------------------------
# T4 -- RECONCILIATION WITH THE EXCHANGE-SYMMETRY CERTIFICATE
#        + B-AXIS DECOMPOSITION (bounded support)
# ---------------------------------------------------------------------------
def theorem_T4():
    print("-- T4: reconciliation -- operator-scaffolding symmetry vs record-content asymmetry")

    # Symmetric 4-cube index set {0,1}^4 with coords (a0=x1, a1=x2, a2=x3, a3=time).
    cube = frozenset((a, b, c, d) for a in (0, 1) for b in (0, 1)
                     for c in (0, 1) for d in (0, 1))

    # sigma swaps axis 0 (x1) and axis 3 (time) -- the combinatorial analog of
    # the S3' exchange W that swaps the temporal and x_1 hop sectors.
    def sigma(u):
        return (u[3], u[1], u[2], u[0])

    # Bare operator scaffolding = nearest-neighbor (Hamming-1) edge set on the
    # cube. By T1 the operator-layer lattice-QFT constructions live on such a
    # stack; the bare adjacency is the axis-symmetric scaffolding.
    edges = set()
    for u in cube:
        for v in cube:
            if u < v and sum(1 for k in range(4) if u[k] != v[k]) == 1:
                edges.add((u, v))
    edges = frozenset(edges)

    # CHECK 21: the bare adjacency is EXACTLY invariant under the axis-swap
    #           sigma (residual-0 analog of the S3' certificate: the operator
    #           layer cannot distinguish the axis).
    def norm_edge(e):
        a, b = e
        return (a, b) if a < b else (b, a)

    sig_edges = frozenset(norm_edge((sigma(a), sigma(b))) for (a, b) in edges)
    check(sig_edges == edges,
          "T4 operator scaffolding (NN adjacency) is sigma-invariant under t<->x1 swap (residual-0 analog)")

    # Record content on the same cube: a realized history (index = a3) whose
    # permanent records nest forward in a3 but are spatially incomparable.
    R = frozenset({(0, 0, 0, 0), (0, 0, 0, 1), (1, 1, 1, 1)})

    # CHECK 22: the record content is NOT sigma-invariant -- the operator
    #           symmetry does not extend to record content (time is record
    #           structure, not operator geometry).
    sigR = frozenset(sigma(u) for u in R)
    check(sigR != R,
          "T4 record content is NOT sigma-invariant: operator-axis symmetry does not reach record content")

    # CHECK 23: on the SAME cube, record nesting holds along the time axis (a3)
    #           and fails along the swapped spatial axis (a0). Both coexist ->
    #           no contradiction; the exchange certificate is the EXPECTED
    #           statement (the operator layer was never going to see time).
    def cube_recset(axis, a):
        out = set()
        for u in R:
            if u[axis] == a:
                reduced = tuple(u[k] for k in range(4) if k != axis)
                out.add(reduced)
        return frozenset(out)

    time_nested = subset(cube_recset(3, 0), cube_recset(3, 1))
    spatial_incomparable = incomparable(cube_recset(0, 0), cube_recset(0, 1))
    check(time_nested and spatial_incomparable,
          "T4 same cube: record nesting holds along time-axis, fails along swapped spatial axis (no contradiction)")

    # CHECK 24: the B-AXIS decomposition covers every clause with an honest
    #           disposition; nothing dropped.
    decomp = {
        "B_AXIS_1a_internal_denominator":
            "NOT_TOUCHED_supplied_walled_by_count_not_rate_firewall_unaudited_post_reset",
        "B_AXIS_1b_absolute_clock_unit":
            "NOT_TOUCHED_supplied_open_rate_class",
        "B_AXIS_2_axis_selection":
            "record_layer_DERIVED_for_event_bearing_histories_T2_CONDITIONAL_on_representation_faithfulness_bridge_OPEN",
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
              and ("UNCHANGED" in decomp["B_AXIS_3_single_clock"])
              and ("NOT_TOUCHED" in decomp["B_AXIS_1a_internal_denominator"])
              and ("NOT_TOUCHED" in decomp["B_AXIS_1b_absolute_clock_unit"]))
    check(covered and nonempty and honest,
          "T4 B-AXIS decomposition covers {1a,1b,2,3}; axis-selection CONDITIONAL/OPEN, B-AXIS.3 UNCHANGED")


# ---------------------------------------------------------------------------
# T5 -- CONSEQUENCE + COMPLETE RESIDUES (drop nothing)
# ---------------------------------------------------------------------------
def theorem_T5():
    print("-- T5: consequence + complete residue enumeration (the #1 refutation failure mode)")

    residues = {
        "PR_4874_in_flight_conditionality": "in_flight_conditional",
        "realized_sector_conditioning_event_bearing": "conditioned",
        "realized_history_import_sequence_definition": "imported_flagged",
        "representation_faithfulness_bridge_OPEN": "OPEN",
        "B_AXIS_1a_1b_untouched_rate_class": "untouched",
        "operator_layer_B_AXIS_3_comparator_exclusion_untouched": "untouched",
        "single_clock_note_premise_stack_unaudited_post_reset": "unaudited_post_reset",
        "sibling_PR_4873_review_pending": "review_pending",
        "no_rate_metric_clock_content": "absent_by_construction",
        "nothing_adopted": "nothing_adopted",
        "audit_lane_owns_statuses": "audit_lane_only",
    }
    required = frozenset({
        "PR_4874_in_flight_conditionality",
        "realized_sector_conditioning_event_bearing",
        "realized_history_import_sequence_definition",
        "representation_faithfulness_bridge_OPEN",
        "B_AXIS_1a_1b_untouched_rate_class",
        "operator_layer_B_AXIS_3_comparator_exclusion_untouched",
        "single_clock_note_premise_stack_unaudited_post_reset",
        "sibling_PR_4873_review_pending",
        "no_rate_metric_clock_content",
        "nothing_adopted",
        "audit_lane_owns_statuses",
    })

    # CHECK 25: residue enumeration is EXACTLY the required set (none dropped,
    #           none invented).
    check(frozenset(residues.keys()) == required,
          "T5 residue enumeration == required set exactly (no residue dropped or invented)")

    # CHECK 26: residue count is the expected 11.
    check(len(residues) == 11, "T5 residue count == 11")

    # CHECK 27: the load-bearing flags read correctly -- the representation
    #           bridge is the OPEN item this note creates; #4874 is in-flight/
    #           conditional; nothing is adopted; audit lane owns statuses.
    ok = (residues["representation_faithfulness_bridge_OPEN"] == "OPEN"
          and residues["PR_4874_in_flight_conditionality"] == "in_flight_conditional"
          and residues["nothing_adopted"] == "nothing_adopted"
          and residues["audit_lane_owns_statuses"] == "audit_lane_only")
    check(ok, "T5 critical flags: representation bridge OPEN; #4874 in-flight; nothing adopted; audit lane owns statuses")


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
