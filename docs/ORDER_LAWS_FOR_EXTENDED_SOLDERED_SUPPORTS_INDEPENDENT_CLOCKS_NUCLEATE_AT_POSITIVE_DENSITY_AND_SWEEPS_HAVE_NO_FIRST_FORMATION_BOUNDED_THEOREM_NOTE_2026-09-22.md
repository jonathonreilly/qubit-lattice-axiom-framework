---
claim_id: order_laws_for_extended_soldered_supports_independent_clocks_nucleate_at_positive_density_and_sweeps_have_no_first_formation_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading; the supplied parity-letter propagation rule (completion (1/8)^(k-1) for k nucleations) as the representative star-constrained support. Independent identically distributed atomless clocks (the uniform race) make each site a nucleation with probability 1/(1 + degree): exact E[k] over all orders of the 5-site path (2), the 3x3 plane (38/15) and the 2x2x2 cube (2); on Z^3 the density is 1/7, and m sites with disjoint closed neighbourhoods bound the skeleton's completion by 8(7/8)^m - 7(6/7)^m, which tends to 0. A translation-invariant nucleation set of zero intensity is empty almost surely; positive intensity alone does not imply decay, as a sweep/clock mixture shows. Lexicographic sweeps over the 48 signed frames give the separate finite control: one nucleation per cube, a rotation-invariant uniform mixture, certain completion with the same completed law for every frame; on Z^3 no nucleation and no first formation. No order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/order_laws_nucleation_density_and_sweep_laws_2026_09_22.py
---

# Order laws for extended soldered supports: independent clocks nucleate at positive density, and sweeps have no first formation

**Date:** 2026-09-22
**Type:** bounded_theorem
The results below concern explicitly supplied finite formation models.
Their parameters, alphabets, orders and sampling laws are conditions of the
calculation, not additional framework premises.

## Result up front

1. **Independent clocks nucleate everywhere.** Under the uniform race
   (independent identically distributed atomless clocks, the uniform order law of the
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

3. **Stationarity alone does not imply decay.** A stationary nucleation
   set with zero one-site intensity is empty almost surely. Positive intensity
   alone does not supply the independent trials in the decay bound: a
   half-and-half mixture of a uniformly framed sweep and an independent-clock
   law is stationary and rotation invariant, has intensity 1/14, and retains
   at least half its finite-box completion probability through the sweep
   component. Thus positive intensity cannot be used as a general exclusion.

4. **Such order laws exist and are covariant.** A lexicographic sweep
   orders sites by (s.d1, s.d2, s.d3) for a signed frame of lattice
   directions. On the cube each of the 48 sweeps has exactly one
   nucleation, and their uniform mixture is invariant under all 24
   rotations, though no single sweep is. Under every sweep the skeleton
   completes with certainty, uniform over its 8 phases, and the completed
   law is the same for all 48 frames. On Z^3 each sweep is
   translation-invariant with no nucleation: site s is preceded by s - d1.

5. **Infinite orders are not initialized formation processes.** A
   lexicographic order on Z^3 has no least element. This defines an order, not
   a sequential simulation starting from an empty lattice. The finite cube
   completion result does not supply an infinite process or its initial phase.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "determine the stated conditional finite-model results without selecting a physical formation law"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "test extensions outside the declared finite models; a physical downstream consumer is not yet established"
conditional_surface_status: "formation reading; the soldered skeleton rule as the supplied representative support; order laws supplied; no order law adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the nucleation formula is exact by linearity and checked by complete enumeration of orders; the completion bound is an exact binomial computation; the stationary-set lemma is a short proof; the sweep results are exact enumerations"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the
sampling process studied here. Sequential draws use the declared conditional
law given the previously formed configuration, with fresh randomness at each
step; a chosen order is external to those draws. Correlated joint draws and
adaptive orders are separate models. Skipping a failed attempt and continuing,
or dropping its whole history, are supplied alternatives. Neither convention
follows from unreadability alone.


Formation orders of a window; a nucleation is a site formed before all its
in-window neighbours. The uniform race: independent identically distributed atomless clocks,
which induce the uniform law on orders. The soldered role-letter rule of
the parity-letter rule below, whose completion on an order with k nucleations is
(1/8)^(k-1): each nucleus draws a uniform letter, and clusters meeting at
a site conflict unless their phases agree. Lexicographic sweeps over the
48 signed frames. The Lattice axiom's sentence "No site is privileged" motivates, but does not select, a supplied
translation-invariant order law on Z^3.

## Relation to earlier work

This packet states its supplied models and finite calculations directly.
Earlier campaign comparisons are historical motivation, not imported proof,
physical authority, or an adopted formation law.

For a finite connected lattice window, the alphabet is {0,1}^3. A site
with no formed neighbour draws a uniform parity letter; otherwise each
recorded neighbour implies its letter by flipping the bond-axis bit. A
conflict leaves the site unrecorded. On a complete history the geometric
nuclei each draw an independent uniform phase phi=letter XOR site-parity.
All subsequent labels propagate these phases. Completion holds exactly when
all k nuclear phases agree: necessity follows from connectedness and checking
each edge at its later endpoint; sufficiency follows by induction along the
finite order. Hence completion is 8^(1-k). This proof applies to complete
histories even though failed histories can create later new draws.

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
is 0, and the set is empty almost surely. Positive rho alone gives neither independence nor the binomial bound.
As a counterexample, mix the independent-clock order with a uniformly framed
lexicographic sweep, each with probability 1/2. This stationary covariant law
has rho=1/14, yet on each rectangular finite box the sweep component has one
nucleus and completion one. Its mixture completion is therefore at least 1/2.
The decay theorem is restricted to independent atomless clocks (or the
explicit independent-trial hypothesis of Theorem 2).
The lexicographic sweep over a signed frame
realises this on Z^3 (site s is preceded by s - d1, and the order is
translation-invariant; checked on a 5x5x5 box). The uniform mixture over
the 48 frames is covariant as a law. On the cube each sweep has one
nucleation, and under each the skeleton completes with certainty, with
the same completed law for all 48.

## No-Go Discipline Gate

The negative scope is only the explicitly stated finite-model implication or
independent-clock bound. No general physical formation exclusion is claimed.

**N1 — Five distinct challenges.** Each is ATTEMPTED by the local argument
or the named finite computation, with its outcome kept explicit:

- **Independent clock trials (ATTEMPTED):** disjoint closed neighbourhoods give independent local minima and the binomial completion bound.
- **Arbitrary positive stationary intensity (ATTEMPTED):** the half-sweep/half-clock mixture is a counterexample to general decay; that broad claim is withdrawn.
- **Zero stationary intensity (ATTEMPTED):** countable union of zero-probability site events gives no nuclei almost surely.
- **Finite lexicographic sweep (ATTEMPTED):** all 48 cube frames have one nucleus and complete, a positive alternative to independent clocks.
- **Infinite lexicographic order (ATTEMPTED):** each site has an earlier neighbour, but no first event; the order does not initialize a formation process, whose existence remains open.

**N2 — Conditions.** The stated alphabet, sampling law and domain jointly
specify this model; no theorem counting independent physical walls is asserted.
Changing one condition does not automatically supply the other conditions.
Relations between alternative physical choices remain unclassified.

**N3 — Hidden-condition scan.** Fresh sequential randomness, finite supported
alphabets where used, declared orders, and the particular failure convention
are supplied conditions. No framework grant for them is claimed. Physical
encodings of abstract role labels remain separate from the finite calculations.

**N4 — Residual matching.** All negative implications used here are proved in
this note on the named domain. Historical comparisons are not invoked as
negative witnesses; no external residual is declared closed by analogy.

**N5 — Resolution.** The runner checks the finite elements/sites/windows
listed in its output. Universal implications are the source proofs; infinite
lattice formation, spectral modes and untested block correlations are not
executed or inferred from a finite sample.

**N6 — Partial routes.** Other alphabets, joint or correlated draws, adaptive
orders, retry conventions and other failure handling are not ruled out. No
new axiom is declared necessary. Scale and kinetic-form primitives have no
role in this finite calculation; they are not classified as missing inputs.

**N7 — Steelman.** A different process can evade a product-law bound by shared
randomness, evade an order comparison by conditioning on completion, or evade
a finite-support constancy statement by varying only off the reached support.
These are concrete reasons not to promote this packet to a physical no-go.
The result is restricted to the model whose hypotheses the proof actually uses.

**N8 — Cross-packet check.** The related formation packets distinguish dropped
histories, holes retained as absent sites, directional alphabets and joint
units. Those distinctions are preserved here. Neither a historical campaign
label nor a previous bounded conclusion grants a general exclusion.

## Falsifiers

- An order on a listed window whose nucleation mean differs from
  the degree formula, falsifies Theorem 1; a violation of the bound under its explicit independent-trial
  hypothesis falsifies Theorem 2.
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

## Author check record (original proposal)

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

## Landing review correction

Serial source review in one Codex session under the owner's no-subagent
instruction narrowed physical interpretations to supplied model conditions.
Original author check reports above are historical; they do not certify these
corrections. Current source-bound executions and independent controls are
recorded in the combined landing evidence. No independent audit is claimed.

## Verification

```bash
python3 scripts/order_laws_nucleation_density_and_sweep_laws_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=10 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/order_laws_nucleation_density_and_sweep_laws_2026_09_22.txt`.
