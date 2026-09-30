# T17 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor). Date 2026-09-29.

## What is being tested

The gravity-lane statement (MAP:927-940 = viab_map.md lines ~925-940; L14-W13):
"On six axes, a scattering that conserves both momentum and angular momentum can
only swap contents. So exact momentum and angular-momentum books force records
that never scatter." This is stated for the supplied inertial clause (records
carry a direction-of-travel content; blocks 44 note 2026-09-20). It is the only
record dynamics in the repository that keeps momentum exactly and locally with
interactions.

Hidden premise I suspect: the statement is proved (implicitly) for BOND-LOCAL
two-record events. It may not hold for events on a cluster with more than one
bond (diagonal pair, 2x2 plaquette, 2x2x2 cube) that still keep one record per
site and fixed positions.

## Test A: cluster class census (script `A_cluster_classes.py`)

Objects: cluster S of lattice sites (positions fixed), occupancy subset with at
most one record per site, content c(x) in the six axis unit vectors (or the four
in-plane ones in 2D). Invariants of a configuration: N, P = sum c,
L = sum x cross c (positions inside the cluster; origin-independent given P).
A class = all configurations with the same occupied set and the same (P, L).
Any permutation inside a class is an event that keeps N, P, L exactly.
Energy is automatic (unit speeds).

Pre-registered predictions:
- A1 bond pair (adjacent sites, 3D): exactly one class of size >1 per ordering,
  the head-on pair (e,-e) <-> (-e,e) along the bond axis. No perpendicular or
  parallel-same-direction class of size >1. (If this fails, the map's lemma is
  misstated.) Corollary computed by hand: the clause's pass-through exchange of
  a perpendicular pair changes L by -s x s' (nonzero).
- A2 diagonal pair (planar, distance sqrt 2): classes of size >1 exist (hand
  example: (e_x at (0,0), -e_y at (1,1)) <-> (-e_y, e_x), a content swap that keeps
  both P and L).
- A3 plaquette 2x2 (2D contents): classes of size >1 exist that are NOT generated
  by pair-level moves (adjacent + diagonal pair events) alone.
- A4 cube 2x2x2 (3D contents): same, and more.

PASS reading (route alive): nontrivial (non-bond-swap) N,P,L-preserving events
exist on at least one cluster with one record per site. Then "records must never
scatter" is an artefact of restricting to bond-local events; exact P and L books
with scattering are available to a classical inertial clause with plaquette-local
collisions.
FAIL reading (route dead): the only size>1 classes are bond head-on swaps.

## Test B: spurious invariants (script `B_ergodic_2d.py`)

Clause V*: (S1) a record steps along its content into an empty site; (S2) if the
target is occupied by a parallel or antiparallel content, the two contents
exchange (pass-through); if perpendicular, nothing happens (blocked; this keeps
L exactly, the unmodified clause exchanges and does not); (C') any class
permutation on a bond, diagonal pair or plaquette (uniform choice within the
class). Configuration graph on the L x L torus (L=4), N records. Components of
the graph restricted to each (N, P) sector.

Pre-registered prediction: each (N, P) sector with 3 <= N <= 5 is ONE component
(no spurious invariant beyond N and P). FAIL reading: some sector splits into
several components => hidden extra conserved quantities (HPP-type), which would be
the cost of the route.
(L itself is not globally defined on a torus, so only N and P are compared.)

## Test C: quantum census (script `C_census.py`), run only if time allows

Two excluded records (the framework's own walker, block 78 compression), Z^2 torus
L=7, translation-invariant Hermitian charges of range <= r, exchange-symmetric,
inversion-odd, commuting with H2. Count non-trivial solutions.
Pre-registered: free Z^2 pair > 0 (controls), excluded Z^1 pair > 0, excluded Z^2
pair = 0 in the odd sector; a soft nearest-neighbour interaction without exclusion
also 0 (so exclusion is not special). FAIL reading: a nonzero odd charge for the
excluded Z^2 pair inside the ansatz.

## Deviations and additions recorded after the runs (post-hoc; the pre-registered text above is unchanged)

- Test B: the pre-registered reading "each (N,P) sector is ONE component" FAILED. V* splits every generic
  (N,P) sector into four pieces of nearly equal size on the 4x4 torus. Diagnosis after the fact: Lz mod 4 is
  conserved on the torus (streaming along the content and every class event leave it fixed, 0 changing events;
  the original clause changes it 186368 times at N=4). Amended check (B2, B4): components per (N,P,Lz mod 4);
  largest component holds 99.1% of the generic-sector states at N=4 (min sector 94.5%); the rest are small
  frozen pockets of aligned records. This amendment was chosen after seeing the failure.
- Added after the runs (not pre-registered): B3 (stationary measure, cost of blocking perpendicular exchange),
  A2 and A3 (existence of a compact symmetric lattice stress for every conserving event, 2D and 3D).
- Test C ansatz limits (one-body hops <= 2; two-body hops <= 1 in 2D, <= 2 in 1D; relative distance <= 2 scalar,
  <= 1 walker; torus 7 in 2D, 11 in 1D) are part of every C statement.
  1D first pass with two-body hops <= 1 found 1 (not 2) odd charge for hard-core scalar bosons because the
  Jordan-Wigner string of the range-2 hop needs a two-body hop of 2; widened ansatz gives 2 (= free).
