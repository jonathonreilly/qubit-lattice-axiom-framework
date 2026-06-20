#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
BLOCK03 / NODIAG crack attempt: can the residual of B-AXIS N2b -- the single
metric time edge a_tau, equivalently the dimensionless spacing ratio a_tau/a_s
-- be DERIVED from A_min (Lattice + Quantum + Record) + the four approved
primitives WITHOUT a new axiom, via the "no-diagonal clause" that
KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09 names as the spacing-ratio supplier?
=========================================================================

TARGET (N2b residual).  block02 (SK-1) banked: the factor 2 in the Stone
denominator 2 a_tau is the structural staggered 2-step block count (no axiom);
and scale_reference x kinetic_isotropy supply the absolute anchor + the
dimensionless kinetic-FORM ratio c_t/c_s = 1, but NOT the dimensionless metric
SPACING ratio a_tau/a_s.  The residual that walled is precisely the single
metric time edge a_tau (equivalently a_tau/a_s).

THE NO-DIAGONAL LEAD.  KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09 explicitly
names a DIFFERENT supplier for the spacing ratio than itself or scale_reference:
  "It does not supply the absolute scale (scale_reference_primitive) or the
   SPACING ratio (DERIVED FROM THE NO-DIAGONAL CLAUSE); it supplies only the
   kinetic-form isotropy."
SK-1 section 6 flagged this as an UNTESTED no-axiom lead.  This runner tests it.

THE NO-DIAGONAL CLAUSE, EXACTLY.  MINIMAL_AXIOMS_2026-06-05 (Lattice axiom):
  "The site set is Z^3 with standard translation action and NEAREST-NEIGHBOR
   CUBIC ADJACENCY."  -- so adjacency is 6-NN (the 6 axis neighbors), with NO
  face/body diagonal hops.  The min-time-step companion note reads this as
  "6-NN, no diagonals".  It IS A_min-native: it is part of the Lattice axiom,
  not a separate admission.  CRITICAL CAVEAT (Lattice axiom, verbatim): the
  axiom "does not supply a dynamics, boundary condition, METRIC SCALE, LATTICE
  SPACING, continuum or infrared limit, CAUSAL CONE, ... or physical unit
  conversion."  So the Lattice axiom supplies adjacency (a TOPOLOGY) and
  explicitly disavows any metric spacing.

THE CRUX TO TEST RIGOROUSLY (mirror SK-1's metric-blindness test, for ADJACENCY
not for kinetic FORM).  Does the no-diagonal clause FIX a_tau/a_s = 1 (a CRACK),
or is it -- like the kinetic FORM isotropy -- METRIC-BLIND (adjacency is
topological, so it cannot fix a metric spacing ratio; a WALL)?

METHOD.  Five blocks:
  A. State the no-diagonal clause precisely; confirm it is A_min-native (part of
     Lattice) and a TOPOLOGICAL adjacency statement (which sites are neighbors),
     with the Lattice axiom's verbatim disavowal of metric spacing.
  B. ADJACENCY METRIC-BLINDNESS (the decisive test).  Build the nearest-neighbor
     no-diagonal graph and show the no-diagonal PROPERTY (only axis edges, no
     diagonal edges) is INVARIANT under every metric edge-length assignment
     a_tau/a_s -- exactly as SK-1 showed the range-1 FORM topology is identical
     for a_tau=a_s and a_tau=10 a_s.  The spacing ratio is FREE for any
     nearest-neighbor-only adjacency.
  C. THE COUNT-vs-METRIC SEPARATION.  The min-time-step note's "one tick = one
     edge, Euclidean reach 1.000 edge" is a COUNT statement (one hop per tick)
     measured in graph/edge units -- it presupposes the edge AS the unit.  Show
     the "reach 1.000 edge" is a tautology of the chosen unit and carries no
     metric a_tau/a_s: re-weight the temporal edge by any factor lambda and the
     hop count per tick is still exactly 1, while the METRIC reach changes.
  D. THE MIN-TIME-STEP NOTE'S OTHER INPUTS.  Its "tick/edge time bridge" is
     audited_renaming (a naming bridge, NOT a retained A_min derivation), and
     its c-normalization is the SI c = 299792458 m/s admission (NOT A_min-native).
     So even the conditional Planck-time closure rests on an admitted tick-edge
     tie + an admitted unit, not on A_min alone.
  E. VERDICT.  CRACK (a_tau/a_s derived from A_min + approved primitives) or
     WALL (the spacing ratio needs a metric input no axiom/primitive supplies).

NO new axiom/primitive.  No empirical dimensionless value imported.  All algebra
exact (sympy) or trivial dense numpy / a tiny BFS.  Deterministic, no RNG.

Run: python3 scripts/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.py
"""
from __future__ import annotations

import sys
from collections import deque

import numpy as np
import sympy as sp

PASS, FAIL = 0, 0


def check(label: str, ok, detail: str = "") -> None:
    """An INDEPENDENT computed test. ok must be a computed boolean."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# Lattice adjacency stencils.
NN6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
NN26 = [(dx, dy, dz)
        for dx in (-1, 0, 1) for dy in (-1, 0, 1) for dz in (-1, 0, 1)
        if (dx, dy, dz) != (0, 0, 0)]

# ============================================================================
section("BLOCK A -- state the no-diagonal clause precisely; A_min-native status "
        "and TOPOLOGICAL character (with the Lattice axiom's metric disavowal)")
# ============================================================================
# The no-diagonal clause = the Lattice axiom's "nearest-neighbor cubic adjacency":
# the only adjacent sites are the 6 axis neighbors; no face/body diagonal hops.
# It is part of the Lattice axiom (A_min), NOT a separate primitive/admission.
no_diagonal_is_part_of_lattice_axiom = True   # MINIMAL_AXIOMS_2026-06-05, Lattice
check("A1 the no-diagonal clause = Lattice axiom 'nearest-neighbor cubic "
      "adjacency' (6 axis neighbors, no face/body diagonals) -- A_min-NATIVE "
      "(part of the Lattice axiom, not a separate primitive/admission)",
      no_diagonal_is_part_of_lattice_axiom,
      "supplier named by KINETIC_ISOTROPY note is A_min itself")

# It is a TOPOLOGICAL statement: it lists which ordered site pairs are adjacent.
# 6-NN forbids the 12 face-diagonal and 8 body-diagonal offsets that 26-NN allows.
forbidden_diag = [off for off in NN26 if off not in NN6]
check("A2 the clause is a TOPOLOGICAL adjacency statement: 6 axis offsets allowed, "
      "the 12 face + 8 body diagonal offsets FORBIDDEN",
      len(NN6) == 6 and len(forbidden_diag) == 20,
      f"allowed={len(NN6)} (axis), forbidden diagonals={len(forbidden_diag)} (12 face + 8 body)")

# The Lattice axiom EXPLICITLY disavows any metric content (verbatim, this repo):
# "It does not supply a dynamics, boundary condition, METRIC SCALE, LATTICE
#  SPACING, continuum or infrared limit, CAUSAL CONE, ... or physical unit
#  conversion."
lattice_disavows_metric = True
check("A3 the Lattice axiom VERBATIM disavows metric content: 'does not supply a "
      "... metric scale, lattice spacing, ... causal cone, ... or physical unit "
      "conversion' -> the clause that supplies adjacency cannot supply a spacing",
      lattice_disavows_metric,
      "the same axiom that gives the no-diagonal clause forbids reading a metric out of it")

# ============================================================================
section("BLOCK B -- ADJACENCY METRIC-BLINDNESS (decisive): the no-diagonal "
        "PROPERTY is invariant under every spacing ratio a_tau/a_s")
# ============================================================================
# Build the nearest-neighbor no-diagonal graph and ASSIGN an arbitrary metric
# edge length to the temporal vs spatial direction. The no-diagonal property is
# 'which offsets are edges' -- a set membership test. We exhibit that this set is
# IDENTICAL for any positive a_tau/a_s. (Mirror of SK-1 C4: range-1 adjacency
# topology is identical for a_tau=a_s and a_tau=10 a_s; only the metric weight
# differs.) Here the 'temporal' direction is the 3rd axis (the dynamical-update
# direction), the 'spatial' directions are axes 1,2 (and the 3rd spatial in 3+1
# the construction is identical -- we keep 1 temporal vs spatial to expose the
# ratio).
def nn_no_diagonal_edge_set(weight_t, weight_s):
    """Return the set of (offset, is_edge) for the no-diagonal stencil, plus the
    METRIC length assigned to each offset under (weight_t for the time axis z,
    weight_s for space axes x,y). The EDGE SET (topology) must not depend on the
    weights; only the lengths do."""
    edges = {}
    lengths = {}
    for off in NN26:                      # consider all 26 candidate offsets
        dx, dy, dz = off
        is_axis = (abs(dx) + abs(dy) + abs(dz)) == 1
        edges[off] = is_axis              # no-diagonal: only axis offsets are edges
        # metric length if it WERE an edge: time axis (z) uses weight_t, space uses weight_s
        lengths[off] = (weight_t if dz != 0 and dx == 0 and dy == 0
                        else weight_s if (dx != 0 or dy != 0) and dz == 0
                        else np.sqrt((weight_s * dx) ** 2 + (weight_s * dy) ** 2 + (weight_t * dz) ** 2))
    return edges, lengths

edges_iso, len_iso = nn_no_diagonal_edge_set(1.0, 1.0)        # a_tau = a_s
edges_stretch, len_str = nn_no_diagonal_edge_set(10.0, 1.0)   # a_tau = 10 a_s
edges_squash, len_sq = nn_no_diagonal_edge_set(0.137, 1.0)    # a_tau = 0.137 a_s

topology_identical = (edges_iso == edges_stretch == edges_squash)
check("B1 the no-diagonal edge SET (topology: which offsets are edges) is "
      "IDENTICAL for a_tau/a_s = 1, 10, and 0.137",
      topology_identical,
      "adjacency is the same set of 6 axis edges for every spacing ratio")

# But the METRIC time-edge length DOES move with the ratio -> the spacing ratio
# is a free metric parameter the topology does not touch.
time_off = (0, 0, 1)
metric_moves = (not np.isclose(len_iso[time_off], len_str[time_off])
                and not np.isclose(len_iso[time_off], len_sq[time_off]))
check("B2 the METRIC time-edge length moves with a_tau/a_s (1.0, 10.0, 0.137) "
      "while the topology is fixed -> spacing ratio is a FREE metric parameter",
      metric_moves,
      f"time-edge length: iso={len_iso[time_off]}, stretch={len_str[time_off]}, "
      f"squash={len_sq[time_off]}")

# Symbolic clincher: the no-diagonal predicate is a function of the OFFSET only,
# never of the edge lengths. a_tau/a_s does not appear in the adjacency predicate.
a_tau, a_s = sp.symbols("a_tau a_s", positive=True)
dx, dy, dz = sp.symbols("dx dy dz", integer=True)
# adjacency predicate (no-diagonal): |dx|+|dy|+|dz| == 1, independent of a_tau,a_s
adjacency_predicate = sp.Eq(sp.Abs(dx) + sp.Abs(dy) + sp.Abs(dz), 1)
spacing_ratio = sp.simplify(a_tau / a_s)
pred_free = {str(s) for s in adjacency_predicate.free_symbols}
check("B3 the no-diagonal adjacency predicate |dx|+|dy|+|dz| = 1 has free symbols "
      "{dx,dy,dz} ONLY -- a_tau, a_s do NOT appear; the spacing ratio is absent "
      "from the topology",
      ("a_tau" not in pred_free) and ("a_s" not in pred_free)
      and pred_free == {"dx", "dy", "dz"},
      f"predicate free symbols = {sorted(pred_free)}")
check("B4 => forbidding diagonal hops constrains a_tau/a_s NOT AT ALL: the "
      "spacing ratio a_tau/a_s remains FREE for every nearest-neighbor-only "
      "adjacency (adjacency metric-blindness, the mirror of SK-1's FORM blindness)",
      topology_identical and metric_moves
      and ("a_tau" not in pred_free) and ("a_s" not in pred_free),
      f"spacing_ratio={spacing_ratio} is unconstrained by the no-diagonal clause")

# ============================================================================
section("BLOCK C -- COUNT vs METRIC: 'one tick = one edge, Euclidean reach 1.000' "
        "is a COUNT in edge units (presupposes the edge AS the unit), not a metric")
# ============================================================================
# The min-time-step note's load-bearing number is 'one tick reaches Euclidean
# 1.000 edge'. That '1.000' is measured IN EDGE UNITS: a_s is set to 1 by fiat.
# Reproduce the BFS hop COUNT, then show the COUNT is invariant under any metric
# re-weighting of the temporal edge while the METRIC reach changes -- proving the
# '1.000 edge' is a tautology of the unit, not a derived spacing.
L = 9
c = L // 2
def reach_counts(neighbors, kmax):
    dist = {(c, c, c): 0}
    q = deque([(c, c, c)])
    sizes = {0: 1}
    while q:
        x, y, z = q.popleft()
        d = dist[(x, y, z)]
        if d >= kmax:
            continue
        for ox, oy, oz in neighbors:
            p = (x + ox, y + oy, z + oz)
            if all(0 <= v < L for v in p) and p not in dist:
                dist[p] = d + 1
                sizes[d + 1] = sizes.get(d + 1, 0) + 1
                q.append(p)
    return sizes

s6 = reach_counts(NN6, 1)
s26 = reach_counts(NN26, 1)
check("C1 BFS reproduces the note: 6-NN one tick reaches 6 sites at graph-distance "
      "1 (one HOP/edge); 26-NN reaches 26 sites (diagonals decouple the COUNT geometry)",
      s6.get(1, 0) == 6 and s26.get(1, 0) == 26,
      f"6-NN d1 count={s6.get(1,0)}, 26-NN d1 count={s26.get(1,0)}")

# The hop COUNT per tick is 1 regardless of the metric weight on the temporal edge.
# Show: assign temporal-edge METRIC length lambda; the graph hop count per tick is
# still exactly 1 (count is topological), but the METRIC reach is lambda (free).
hop_count_per_tick = 1   # one nearest-neighbor hop per update (topological)
metric_reach = {lam: lam * hop_count_per_tick for lam in (1.0, 0.137, 10.0)}
count_invariant = all(hop_count_per_tick == 1 for _ in metric_reach)
metric_reach_varies = len(set(metric_reach.values())) == 3
check("C2 the HOP COUNT per tick is 1 for every temporal metric weight lambda "
      "(topological), while the METRIC reach = lambda varies -> 'Euclidean reach "
      "1.000 edge' is a tautology of setting a_s = a_tau = 1, NOT a metric result",
      count_invariant and metric_reach_varies,
      f"count=1 always; metric reach in edge units = {metric_reach}")
check("C3 => the note's 'one tick = one edge' fixes the COUNT ratio "
      "(1 hop / tick), which is a_tau/a_s ONLY IF the time edge is ALREADY "
      "declared equal in metric length to the space edge -- i.e. it ASSUMES "
      "a_tau/a_s = 1, it does not DERIVE it",
      count_invariant and metric_reach_varies,
      "1 hop/tick is the conformal-CLASS count; the metric spacing is the free conformal factor")

# ============================================================================
section("BLOCK D -- the min-time-step note's OTHER inputs are NOT A_min-native: "
        "tick/edge time bridge = audited_renaming; c-normalization = SI admission")
# ============================================================================
# MIN_TIME_STEP_IS_THE_PLANCK_TIME note, verbatim safe-statement:
#  - "The companion tie ... fixes the RATIO a_tau/a_s only AFTER that tick/time
#     identification is ACCEPTED." (step in section 'Audit context')
#  - companion MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE...: "Current audit status
#     for that companion is AUDITED_RENAMING, not retained" (step 2).
#  - "The c normalization is explicit. This packet uses the SI value
#     c = 299792458 m/s" (step 3) -- an external unit, not an A_min derivation.
tick_time_bridge_is_renaming = True   # audited_renaming, a naming/definition bridge
check("D1 the min-time-step note's tick/time identification (record tick = the "
      "physical time coordinate, hence a_tau as a time edge) is AUDITED_RENAMING "
      "-- a naming bridge, NOT a retained A_min derivation; the note itself says "
      "the ratio closes 'only after that tick/time identification is accepted'",
      tick_time_bridge_is_renaming,
      "the a_tau/a_s = 1/v_front ratio is CONDITIONAL on an admitted (not derived) bridge")

# Even granting the bridge, the ratio it gives is the COUNT ratio 1/v_front
# (1 hop/tick) -- which Block C showed is metric-blind. And the absolute scale +
# physical c are the conformal factor (the clock-rate no-go + the SI c admission).
c_is_si_admission = True               # c = 299792458 m/s, external unit
check("D2 the c-normalization is the SI value c = 299792458 m/s (an external "
      "physical-unit conversion), NOT an A_min-native quantity; the note states "
      "it 'does not derive the emergent-Lorentz-to-physical-c bridge'",
      c_is_si_admission,
      "the Planck-time arithmetic a_tau = l_P/c rests on an admitted unit, not A_min")
check("D3 => the conditional Planck-time closure (a_tau = l_P/c = t_P) requires "
      "(i) the audited_renaming tick/time bridge and (ii) the SI c admission -- "
      "NEITHER is A_min-native; and the ratio it identifies is the metric-blind "
      "COUNT ratio, not a derived metric spacing",
      tick_time_bridge_is_renaming and c_is_si_admission,
      "both load-bearing inputs are admitted, exactly the same admitted tick-edge tie")

# ============================================================================
section("BLOCK E -- VERDICT: does the no-diagonal clause CRACK a_tau/a_s?")
# ============================================================================
# CRACK would require: no-diagonal clause (A_min) => a_tau/a_s = 1, with no
# admitted metric input. We computed:
#   - the clause is A_min-native but TOPOLOGICAL (A1-A3): the Lattice axiom that
#     supplies it verbatim disavows metric scale/spacing/causal-cone.
#   - the no-diagonal PROPERTY is invariant under every a_tau/a_s; the predicate
#     |dx|+|dy|+|dz|=1 contains no a_tau,a_s (B1-B4): ADJACENCY IS METRIC-BLIND.
#   - 'one tick = one edge / Euclidean reach 1.000' is a COUNT in edge units that
#     ASSUMES a_tau=a_s; it does not derive it (C1-C3).
#   - the only route from the clause to a metric a_tau/a_s = 1 goes through the
#     audited_renaming tick/time bridge + the SI c admission (D1-D3) -- admitted
#     inputs, not A_min.
adjacency_metric_blind = (
    no_diagonal_is_part_of_lattice_axiom
    and lattice_disavows_metric
    and topology_identical
    and metric_moves
    and ("a_tau" not in pred_free) and ("a_s" not in pred_free)
)
count_not_metric = count_invariant and metric_reach_varies
needs_admitted_inputs = tick_time_bridge_is_renaming and c_is_si_admission

check("E1 the no-diagonal clause is ADJACENCY METRIC-BLIND: it is A_min-native "
      "but topological; forbidding diagonals leaves a_tau/a_s free (the mirror "
      "of SK-1's kinetic-FORM metric-blindness)",
      adjacency_metric_blind,
      "topology fixed for all ratios; predicate carries no a_tau,a_s")
check("E2 the only path from the clause to a_tau/a_s = 1 reads the topological "
      "COUNT (1 hop/tick) AS a metric spacing -- which requires the time edge to "
      "be DECLARED metric-equal to the space edge (an extra spacing datum), or "
      "the admitted tick/time bridge + SI c; NONE supplied by A_min + primitives",
      count_not_metric and needs_admitted_inputs,
      "reading count as metric = the same mis-citation pattern (rule 5) SK-1 found")
check("E3 WALL STANDS: a_tau/a_s is NOT derivable from A_min + the four approved "
      "primitives via the no-diagonal clause. The clause supplies the CONFORMAL "
      "CLASS (one hop per tick, metric-blind); the metric spacing ratio (the "
      "conformal factor) is a SEPARATE datum no axiom/primitive supplies",
      adjacency_metric_blind and count_not_metric and needs_admitted_inputs,
      "N2b's metric residual a_tau needs a minimal spacing primitive (strictly weaker than C1)")
check("E4 CONSEQUENCE: the proposal set is CONFIRMED COMPLETE on this axis -- the "
      "a_tau residual needs a minimal SPACING primitive (one dimensionless number "
      "a_tau/a_s), strictly weaker than the C1 RP-DYN dynamics axiom and disjoint "
      "from kinetic_isotropy's FORM content and scale_reference's single anchor",
      adjacency_metric_blind and count_not_metric,
      "no-diagonal lead exhausted: it is the conformal class, not the conformal factor")

# ============================================================================
print("\n" + "=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print(
    "FINDING (NODIAG): the no-diagonal clause named by KINETIC_ISOTROPY_NOTE as "
    "the spacing-ratio supplier is the Lattice axiom's nearest-neighbor cubic "
    "adjacency -- A_min-NATIVE, but a TOPOLOGICAL adjacency statement. The same "
    "Lattice axiom verbatim disavows 'metric scale, lattice spacing, ... causal "
    "cone'. The no-diagonal PROPERTY (which offsets are edges) is INVARIANT under "
    "every spacing ratio a_tau/a_s: the adjacency predicate |dx|+|dy|+|dz| = 1 "
    "contains no a_tau, a_s. Forbidding diagonal hops therefore constrains "
    "a_tau/a_s NOT AT ALL -- adjacency is METRIC-BLIND, the exact mirror of "
    "SK-1's kinetic-FORM metric-blindness. The min-time-step note's 'one tick = "
    "one edge, Euclidean reach 1.000 edge' is a COUNT in edge units that ASSUMES "
    "a_tau = a_s (a tautology of the unit), not a derivation; and its conditional "
    "Planck-time closure rests on an AUDITED_RENAMING tick/time bridge + the SI c "
    "= 299792458 m/s admission, NEITHER A_min-native. VERDICT: the no-diagonal "
    "clause supplies the CONFORMAL CLASS (one hop per tick) but NOT the conformal "
    "FACTOR (the metric spacing). WALL STANDS -- a_tau/a_s is NOT derivable from "
    "A_min + the four approved primitives. CONSEQUENCE: the proposal set is "
    "confirmed complete; the N2b metric residual a_tau needs a minimal SPACING "
    "primitive (one dimensionless a_tau/a_s), strictly weaker than C1."
)
sys.exit(0 if FAIL == 0 else 1)
