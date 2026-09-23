---
claim_id: order_laws_for_extended_soldered_supports_independent_clocks_nucleate_at_positive_density_and_sweeps_have_no_first_formation_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading; the soldered role-letter rule of open PR 8669 (completion (1/8)^(k-1) for k nucleations) as the representative star-constrained support. Independent identical clocks (the uniform race) make each site a nucleation with probability 1/(1 + degree): exact E[k] over all orders of the 5-site path (2), the 3x3 plane (38/15) and the 2x2x2 cube (2); on Z^3 the density is 1/7, and m sites with disjoint closed neighbourhoods bound the skeleton's completion by 8(7/8)^m - 7(6/7)^m, which tends to 0. A translation-invariant order law on Z^3 has nucleation density 0 only if no site nucleates, so defect-free formation of the skeleton needs order laws in which every formation is preceded by a neighbour's. Lexicographic sweeps over the 48 signed frames realise this: one nucleation per cube, a rotation-invariant uniform mixture, certain completion with the same completed law for every frame; on Z^3 no nucleation and no first formation. No order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - formation_order_covariance_and_isotropic_binary_order_blind_classification_bounded_theorem_note_2026-09-13
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/order_laws_nucleation_density_and_sweep_laws_2026_09_22.py
---

# Order laws for extended soldered supports: independent clocks nucleate at positive density, and sweeps have no first formation

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The previous blocks reduced the recorded
decisions behind downstream gravity to the order law and soldering (open
PR 8669). A soldered star-constrained support, the parity-role skeleton,
completes with probability exactly (1/8)^(k-1) for k independent
nucleations. This block asks which order laws let such supports form on
large windows, and what that requires of the order itself.

## Result up front

1. **Independent clocks nucleate everywhere.** Under the uniform race
   (independent identical clocks, the uniform order law of the
   clock-and-rate block), a site is a nucleation exactly when it forms
   before all its neighbours, with probability 1/(1 + degree). The
   expected nucleation count is the sum of 1/(1 + degree), confirmed over
   all orders: 2 on the 5-site path, 38/15 on the 3x3 plane, 2 on the
   2x2x2 cube. On Z^3 the density is 1/7 per site.

2. **So independent clocks cannot form extended soldered supports.**
   Sites whose closed neighbourhoods are disjoint nucleate independently,
   so m of them bound the skeleton's completion by
   8(7/8)^m - 7(6/7)^m. This tends to 0, and is below 1/100 at m = 60,
   a window of about 1600 sites. On the cube the bound 121/128 sits above
   the exact 599/2048.

3. **Defect-free formation needs formation without a first event.** The
   Lattice axiom says no site is privileged, so an order law on Z^3 is
   translation-invariant, and its nucleations form a translation-invariant
   random set. Such a set with density 0 is empty. So completion with
   probability bounded away from 0 on growing windows needs an order law
   in which no site nucleates: every formation is preceded by a
   neighbour's, and there is no first formation anywhere.

4. **Such order laws exist and are covariant.** A lexicographic sweep
   orders sites by (s.d1, s.d2, s.d3) for a signed frame of lattice
   directions. On the cube each of the 48 sweeps has exactly one
   nucleation, and their uniform mixture is invariant under all 24
   rotations, though no single sweep is. Under every sweep the skeleton
   completes with certainty, uniform over its 8 phases, and the completed
   law is the same for all 48 frames. On Z^3 each sweep is
   translation-invariant with no nucleation: site s is preceded by s - d1.

5. **What this adds to the order-law decision.** Extended soldered
   supports, the route that the roles and the ice support need, are
   formed by covariant order laws that proceed as a front with no first
   formation. Each realisation carries a frame of lattice directions,
   which the completed records do not show. Independent local clocks
   (positive nucleation density) are excluded for this purpose. Which
   front-like law holds, and whether every nucleation-free covariant law
   fixes a direction in each realisation, remain open.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the decisions behind downstream gravity reduce to the order law and soldering; determine which order laws form star-constrained soldered supports on large windows"
source_of_blocker_text: open_pr_8669
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "re-assemble with the order-law decision sharpened (nucleation-free front laws for extended soldered supports); classify nucleation-free covariant order laws; test whether every one fixes a direction per realisation"
conditional_surface_status: "formation reading; the soldered skeleton rule as the supplied representative support; order laws supplied; no order law adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the nucleation formula is exact by linearity and checked by complete enumeration of orders; the completion bound is an exact binomial computation; the stationary-set lemma is a short proof; the sweep results are exact enumerations"
```

## Premises and declared objects

Formation orders of a window; a nucleation is a site formed before all its
in-window neighbours. The uniform race: independent identical clocks,
which induce the uniform law on orders. The soldered role-letter rule of
open PR 8669, whose completion on an order with k nucleations is
(1/8)^(k-1): each nucleus draws a uniform letter, and clusters meeting at
a site conflict unless their phases agree. Lexicographic sweeps over the
48 signed frames. The Lattice axiom's sentence "No site is privileged",
read as translation invariance of any order law on Z^3.

## Prior art and what is new

- Landed binary classification note (2026-09-13), Lemma C: no total order
  on Z^3 is invariant under a proper cubic rotation. New here: the
  covariant mixture over the 48 sweeps is invariant as a law with every
  realisation non-invariant, and it is nucleation-free on Z^3.
- Open PR 8669: completion (1/8)^(k-1). New here: nucleation densities of
  order laws, the decay bound for independent clocks, and the sweep laws.
- Open clock-and-rate PR 8641: the uniform race and eager clocks. New
  here: every clock law with positive nucleation density fails for
  extended soldered supports.

## Theorem 1 — Nucleation density of independent clocks

Under the uniform race a site s nucleates exactly when its clock is the
smallest in its closed neighbourhood, probability 1/(1 + deg(s)). By
linearity E[k] is the sum over sites; checked over all orders on the
5-site path (2), the 3x3 plane (38/15) and the 2x2x2 cube (2). On Z^3 the
density is 1/7. Sites with disjoint closed neighbourhoods nucleate
independently; for the two antipodal cube corners both nucleate in
exactly 1/16 of the 40320 orders.

## Theorem 2 — The completion bound

Let m sites of a window have pairwise disjoint closed neighbourhoods, each
nucleating independently with probability p. Since k is at least the
number k_I of those that nucleate, and completion is (1/8)^(k-1),
completion <= E[(1/8)^(max(k_I, 1) - 1)] = 8(1 - 7p/8)^m - 7(1 - p)^m.
At p = 1/7 this is 8(7/8)^m - 7(6/7)^m, which is 1 at m = 1 and below
1/100 at m = 60. Such m sites fit in a window of about 27m sites. On the
cube (m = 2, p = 1/4) the bound is 121/128, above the exact 599/2048.

## Theorem 3 — Nucleation-free order laws

Let an order law on Z^3 be translation-invariant. Its nucleation set is a
translation-invariant random set, so every site nucleates with the same
probability rho. If rho = 0 the expected number of nucleations in any box
is 0, and the set is empty almost surely. If rho > 0, Theorem 2 applies
to growing windows, and the skeleton's completion tends to 0. So
completion bounded away from 0 on growing windows needs rho = 0, that is
no nucleation at all: every formation is preceded by a neighbour's, and
no formation is first. The lexicographic sweep over a signed frame
realises this on Z^3 (site s is preceded by s - d1, and the order is
translation-invariant; checked on a 5x5x5 box). The uniform mixture over
the 48 frames is covariant as a law. On the cube each sweep has one
nucleation, and under each the skeleton completes with certainty, with
the same completed law for all 48.

## No-Go Discipline Gate

The negative content is scoped: under an order law with positive
nucleation density, the soldered skeleton's completion tends to 0 on
growing windows.

- **N1 alternative routes.** Other nucleation-free order laws, other
  supports whose completion is not (1/8)^(k-1), and joint formation
  units are not classified here.
- **N2 wall independence.** Order statistics and exact counting; no
  dynamics or spectral input.
- **N3 hidden walls.** Translation invariance of the order law is read
  from "No site is privileged"; the stationary-set lemma is standard
  probability, stated with its short proof.
- **N4 residual matching.** The order-law decision's residual: which
  nucleation-free law, and whether it fixes a direction per realisation.
- **N5 rhetoric audit.** "Excluded" refers only to extended soldered
  supports under positive nucleation density; no claim about time in
  general.
- **N6 partial-closure paths.** Classifying nucleation-free covariant
  order laws is open.
- **N7 steelman.** For independent clocks: they are the simplest
  covariant law and may carry other physics. Against them here: extended
  soldered supports fail with probability tending to 1. The trade-off is
  stated, not resolved.
- **N8 cross-cycle echo.** Lemma C and the completion formula are cited.

## Falsifiers

- An order on a listed window whose nucleation mean differs from
  the degree formula, or a translation-invariant order law with positive
  nucleation density under which the skeleton completes on growing
  windows with probability bounded away from 0, falsifies Theorems 1-3.
- A sweep with more than one nucleation on the cube, a non-invariant
  sweep mixture, or a sweep under which the skeleton fails to complete
  falsifies Theorem 3.

## Boundaries and non-claims

No order law is adopted. The skeleton rule is the representative support;
the argument applies to any support whose completion decays with the
number of independent nucleations, which is not claimed for all
supports here. No claim is made that time has no beginning physically;
the statement concerns formation orders of this model. Nothing here
grades, unlocks or audits any other claim.

## Imports

The Lattice axiom sentence quoted; Lemma C and the completion formula
cited; standard probability for stationary random sets. No audit grade,
no new axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) nucleation means computed by complete
  enumeration of orders and compared with the degree formula; (ii) the
  independence of disjoint-neighbourhood nucleations checked by counting
  (2520 of 40320 orders); (iii) sweep completions computed by the exact
  finished-state programme and compared as sets with the skeleton phases
  built from the parity definition.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| nucleation counts the first site only | test replaced | caught (3 FAILs) |
| degree formula off by one | 1/(1+deg) to 1/(2+deg) | caught (3 FAILs) |
| bound drops the 7/8 factor | (1 - 7p/8) to (1 - p) | caught (1 FAIL) |
| frames allow parallel axes | orthogonality partly dropped | caught (1 FAIL) |
| broadcast ignores the bond axis | letter copied unflipped | caught (1 FAIL) |
| cube symmetry about the corner | centring removed | caught (1 FAIL) |
| sweep keys reversed | frame read backwards | missed; diagnosed non-defect (a reversed frame is another of the 48 frames, so the sweep set is unchanged) |
| earlier neighbour taken as s + d1 | wrong neighbour | caught (1 FAIL) |

  Seven of seven defect mutants are caught; the eighth is a relabelling.
- **Vacuity guard:** each exact mean is compared with a formula computed
  separately; the sweep checks compare sets and laws, not sizes.
- **Budget:** 10 checks, stdout 1564 characters (ceiling 6000), about
  0.9 s (ceiling 900 s), exact Fractions; largest enumeration 9! orders.

## Verification

```bash
python3 scripts/order_laws_nucleation_density_and_sweep_laws_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=10 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/order_laws_nucleation_density_and_sweep_laws_2026_09_22.txt`.
