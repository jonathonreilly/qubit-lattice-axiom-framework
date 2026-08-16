# Finite incidence-orbit cancellation begins on pairs — Cycle 766

Date: 2026-08-09

Authority: none; self-contained finite construction proposed for independent audit.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [`physical_cell_cutting_incidence_cancellation_cycle766_2026_08_09.py`](../scripts/physical_cell_cutting_incidence_cancellation_cycle766_2026_08_09.py)

Direct scientific dependencies: none.

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## Trace and status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_incidence_cancellation_cycle766_note_2026-08-09
target_blocker_text: "locate the finite rank loss among subsums of the four reconstructed incidence orbits"
source_of_blocker_text: frontier_question
reachability_to_target: "direct finite exhaustive construction"
artifact_role: "bounded finite incidence theorem candidate"
next_trace_action: "independent audit of the landed source and runner evidence"
conditional_surface_status: "the target domain is the declared finite incidence object"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact rank theorem for explicitly reconstructed finite integer matrices"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

On the finite object defined below, the four cover-piece orbit indicators whose
sum is the reconstructed cover table each have exact rational rank `144`. The
exact ranks of their fifteen nonempty subsums are the singleton, pair, triple,
and quadruple lists displayed below. Replacing incidence-orbit slot `0` by orbit
`5` gives exact rational rank `144`, as does adding orbit `5` to all four. The
blind spaces of the cover table and the replacement witness meet in dimension
`12` and span dimension `123`.

The theorem's domain is this labelled finite incidence object. The modular
per-part levels and one-swap neighbourhood census are diagnostics with the
one-sided interpretation stated in the Boundary section; they are not promoted
to exact-rank census claims.

## Historical motivation and self-containment

Earlier cycle branches motivated the question of where the rank difference `39`
appears, but they are not authority or dependencies for this note. The primary
runner rebuilds the pieces, cuttings, covers, symmetry action, central
decomposition, twenty-part reduction, ceiling, floor, and every target matrix
from the definitions in this packet. It reads no earlier-cycle source, data, or
result.

The cover table is the sum of 4 whole cell orbits. That makes the question finite
and sharp: is each of those four orbits already deficient, or are they
individually maximal and the deficiency created only when they are added? This
cycle answers it, then locates the loss on the lattice of sub-sums, and measures
how far the cover table sits from the ceiling in its own one-exchange
neighbourhood.

## The object

The unit four-cube on sixteen corners, cut into least-volume pieces at the
adjacency-cost floor: 2672 candidate pieces of determinant one, 400 of them at
cost floor 6, 15800 cuttings of 24 pieces, 192 pieces actually used and 192
eight-piece covers.

The symmetry permutes the four coordinates and flips any of them: 384 maps,
closed over all 147456 products, acting transitively on the 192 pieces and on the
192 covers. It has 104 orbits on ordered pairs of pieces, 120 on ordered pairs of
covers and 96 on the cells of the cover-by-piece square. By exact rational
arithmetic the cutting table has rank 88 with kernel 104, and the cover table has
rank 105 with kernel 87.

The locally reconstructed reduction shows that a covariant table acts on part
`i` as one `mc_i` by `m_i` matrix tensored with an identity, so its rank is
`sum_i d_i rank(beta_i)`; the coefficient map from the 96 cell orbits to the
twenty small matrices is one-to-one and onto (stacked width 96, rank 96). Five of
the twenty parts carry no matrix at all, so 15 parts are active.

## The four incidence orbits are each at the ceiling

Each of the 4 cell orbits summing to the cover table has, on its own, exact
rational rank 144 — the derived ceiling — and its modular rank agrees. Read part
by part, all 60 single-orbit small matrices meet their own allowance
`min(m, mc)`, with 0 short.

This settles the dichotomy the cycle opened with, and it settles it the strong
way. **None of these four finite incidence-orbit matrices is individually below
rank 144.** Every one of the eight per-part drops that make up the `39` therefore
appears only in a sum of orbit matrices; it is absent from each singleton.

## Where the loss is born: the sub-sum lattice

All 15 non-empty sub-sums of the four incidence orbits, by exact rational rank
(no modulus enters this block):

- singletons: 144, 144, 144, 144
- pairs: 72, 93, 117, 129, 144, 144
- triples: 114, 130, 142, 142
- all four: 105

Two facts here are new and neither was anticipated.

First, **the cancellation starts immediately**: one pair already drops to 72, half
the ceiling, while two other pairs are still at 144. The pair spectrum is wide,
so the four orbits are not interchangeable with respect to each other.

Second, **the quadruple sits below every triple**. The least triple is 114 and the
cover table's 105 is below it. Rank on this lattice is not monotone under adding
orbits, and the cover table is exactly where the non-monotonicity bites: the
fourth incidence orbit destroys rank that the first three already had. The 39
acquires a location, not just a size.

Part by part, every one of the 8 rank-losing parts first goes short on a **pair**,
never on a single orbit, with 0 at size one. So the loss is born at the smallest
size where cancellation is possible at all.

## Rank loss is not monotone, part by part either

The design for this cycle predicted that a part goes short on a proper sub-sum if
and only if it is one of the eight drop parts. That prediction is false, and the
runner reports the measurement rather than the prediction.

**3 further parts go short on a pair yet meet `min(m, mc)` on all four**, with
`d/m/mc` equal to 3/1/3, 4/2/1 and 8/4/2. These parts lose rank on a pair and get
it back when the remaining orbits are added. Their recovery is not inferred from
the drop bookkeeping; the second prime rebuilds their four-orbit matrices from
scratch and confirms that each meets its allowance there too.

So non-monotone behaviour is not a curiosity of the top of the lattice. It occurs
on individual parts, in both directions, and any account of the 39 that treats
rank as accumulating monotonically along a chain of orbits is wrong.

The whole level computation is reproduced at the second prime: 15 active parts
compared, 0 differ, 30 short sub-sums found at those sizes. The primes are
1000003 and 1000033.

## The cover table in its own neighbourhood

Replace one of the four incidence orbits by any other cell orbit: 368
substitutions. By the small-matrix reduction their values run from 72 to 144,
with 53 at the ceiling, 1 equal to 105, and 9 lower. So of the 368 one-exchange
neighbours, 53 are already maximal and just 9 are worse than the cover table
itself: the cover table sits near the bottom of its own neighbourhood.

A named exact witness: **slot 0 taking orbit 5** lifts the exact rational rank of
the four-orbit table from 105 to 144. That substitution was found by search over
the neighbourhood, not assumed, and both its rank and the unswapped table's 105
are confirmed by exact rational arithmetic.

Adding rather than exchanging does the same thing: the five-orbit table formed by
the four incidence orbits together with that same orbit has exact rank 144. One
extra orbit is enough to reach the ceiling from 105.

## The two blind spaces barely overlap

The cover table's blind space has dimension 87; a table at the ceiling has blind
space of dimension 48, the floor. Exactly, by stacking the two tables and taking
one rational rank:

- they meet in dimension 12,
- they span 123 together,
- the smaller does **not** sit inside the larger.

Two independent routes to the intersection agree. So the 39 of extra blindness is
not a matter of the cover table being blind to everything a maximal table is
blind to plus a little more. The two blind spaces are largely transverse: the
cover table sees things a ceiling table misses, and is blind to a great deal that
a ceiling table sees.

## Runner

`physical_cell_cutting_incidence_cancellation_cycle766_2026_08_09.py` has 46
fail-closed gates. Every target number above is printed by a gate. Group
construction, orbit decomposition, the central decomposition into twenty parts,
the ceiling and floor, and the small-matrix reduction are re-derived from the
pieces on every run, not read from a file. The sub-sum lattice, per-part levels,
neighbourhood scan, and blind-space comparison are computed in the same process.

## Inputs, imports, and primitive-registry result

| input | class and provenance | role and sensitivity |
| --- | --- | --- |
| labelled unit four-cube, determinant-one simplex rule, adjacency cost, cutting and cover definitions | declared finite-model data in this note and runner | define the theorem's object; changing one defines another object |
| coordinate permutations and flips | declared finite action | defines the orbit partition used by the target |
| cell-orbit labels selected by the reconstructed cover table | deterministic outputs of the finite construction | define the four target summands; the runner checks their reconstruction of the cover table |
| replacement label `5` and slot `0` | deterministic witness found by the declared exhaustive one-swap scan | define the advertised replacement and five-orbit witnesses; exact ranks are recomputed independently of the modular scan |
| primes `1,000,003` and `1,000,033` | computational diagnostics | support only the explicitly modular per-part and neighbourhood measurements |
| Python integer/rational arithmetic and NumPy integer arrays | implementation substrate | exact recomputation, cross-prime controls, and independent review cover load-bearing operations |

The primitive-registry check defined by
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` returns an empty
premise dependency set for this target. The axiom and approved-primitive
registries contribute no numerical or structural input. The runner declares no
`AUDIT_INPUT_PATHS` because it reads no data file; its own source bytes are bound
by the runner-cache execution identity.

## Proof-obligation graph

The exact target closes through this acyclic graph:

1. the declared corner, determinant, cost, cutting, and cover definitions fix the finite search domain;
2. C0-C3 reconstruct the pieces, cuttings, cover table, group action, and exact primary ranks;
3. C4-C10 reconstruct the orbit algebra and its twenty-part decomposition, while C11-C13 establish the rank ceiling `144`, blind-space floor `48`, measured difference `39`, and an exact ceiling witness;
4. C28-C33 rebuild the local part table at two primes and verify that the small-matrix reduction reproduces direct table ranks on deterministic controls;
5. C34-C36 compute all fifteen subsum ranks exactly and prove that every singleton has rank `144` while the four-orbit sum has rank `105`;
6. C40-C41 identify the replacement witness and recompute its exact rational rank `144`;
7. C42 recomputes the blind-space intersection and span dimensions exactly and checks the five-orbit rank `144`.

The per-part first-loss levels and one-swap census are modular diagnostics. The
second prime is an independent-construction control for those diagnostics, not an
exact-rank proof.

## Controls and execution contract

The runner declares `AUDIT_TIMEOUT_SEC = 600` and `MEMORY_LIMIT_MB = 2500`,
uses a monotonic clock, and converts `ru_maxrss` by platform convention. Synthetic
values immediately below and above the memory limit exercise both Linux KiB and
Darwin byte conversions. Every failed gate contributes to the final `FAIL` count
and causes a nonzero process exit after closed stdout accounting.

## Review-preparation record

The self-contained salvage excludes the unlanded ancestor manifest and uses no
earlier-cycle artifact as authority. It removes an ungated side corollary from the
target surface, labels modular counts as one-sided diagnostics, inventories the
finite and computational inputs, and makes the runner's resource and failure
contracts explicit. Independent scientific review remains required.

## Boundary

- The sub-sum lattice of 15 exact rational ranks carries no modulus. The pair,
  triple and quadruple values, the singleton value 144, the witness rank 144, the
  five-orbit rank 144, and the intersection dimension 12 are all exact.
- The per-part levels and the neighbourhood values are modular ranks, and a
  modular rank can only fall. So a measured level is a lower bound on the true
  level, the count of 53 neighbours at the ceiling is a lower bound, and the
  counts of 1 equal to 105 and 9 below it are upper bounds. The second prime
  agreeing on all 15
  active parts is an independent-construction control, not a proof.
- That a table at rank 144 has every part at its own allowance is forced
  arithmetic once the ceiling theorem is in hand, not evidence. It is used here
  only as a consistency check on the witness.
- The three non-monotone parts are reported exactly as measured, against the
  cycle's own prior expectation.
- Nothing here says which geometric feature distinguishes the incidence orbits
  from the orbit that repairs them. That stratification of the 96 cell orbits, and
  the question of which pairs are responsible for the deficiency, are the next
  units and are named here so the boundary is honest about what was left.
- The symmetry used throughout is the full symmetry of the four-cube, which
  permutes the four coordinates and flips any of them. Its use here has no
  premise edge to a framework covariance claim; it acts only on the finite
  combinatorial object declared in this note.
- No axiom, primitive, registry entry, effective status or framework claim changes
  here. This is finite exact linear algebra on a fixed finite object.
