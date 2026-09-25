---
claim_id: record_formation_clock_in_the_clause_the_field_aligned_menu_s_odds_do_not_depend_on_when_records_form_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: the Heisenberg point of the dynamics clause (the supplied companion construction), records acting as fields on their unrecorded neighbours (the supplied companion construction), the compression update with odds Tr(P_q rho) (the supplied selective projector update), and a formation clock (D-form): each unrecorded site carries a conditional-hazard clock whose rate is a function f of the site's conditional state rho = (1 + r.sigma)/2. Finite certificates. (i) Covariance: among polynomials of degree at most two in r, the invariant rate functions are spanned by {1, |r|^2} under every internal rotation, by {1, |r|^2, r.h, (r.h)^2} when a physical field axis h is present, and by {1, |r|^2, (r.n)^2} for an unordered antipodal menu axis n. (ii) An isolated site (all neighbours recorded) is a qubit in the field h of their contents; its Bloch vector precesses about h and r.h is conserved (to 2e-16); for four clocks (constant, |r|^2, (1 + r.p)/2, 2(r.p)^2) the recorded frequency of the aligned outcome on the menu along h, conditional on a record forming, equals (1 + r.h)/2 = 0.7826 to 2e-16, while on a menu tilted from h the four clocks give 0.8437, 0.8154, 0.8360, 0.8570 and conditional mean formation times 1.000, 1.562, 1.278, 1.565. (iii) For each fixed clock, menu and trajectory the recorded law is the trace rule of its formation-weighted state, a valid state (|r_f| at most 0.7209). (iv) With one unrecorded Heisenberg partner, r.h varies by 0.252 along the trajectory and the field-menu frequencies of the four clocks are 0.7197, 0.7204, 0.7242, 0.7535 against the isolated value 0.7826. (v) On a ring of six with clocks everywhere, field-aligned menus where a recorded neighbour exists and a supplied axis elsewhere, 60 trajectories per clock give aligned-outcome stack frequencies 0.481, 0.497, 0.521, 0.506, each with trajectory-level errors, and mean times to full recording 2.59, 12.91, 15.26, 44.00, as a finite diagnostic. No formation law, rate function or menu is derived or adopted; no physical reading is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/formation_clock_field_aligned_menu_odds_do_not_depend_on_when_records_form_2026_09_24.py
---

# A formation clock in the clause: the field-aligned menu's odds do not depend on when records form

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact identities with finite numerical diagnostics under supplied decision points; unaudited.

## Result

Admissibility leaves the formation site, probability and rate to downstream
suppliers. The landed formation-law notes of September, such as
`ADMISSIBILITY_RULE_FORMATION_RATE_IDENTITIES_AND_FINITE_WINDOW_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md`
and
`ADMISSIBILITY_RULE_HOW_RECORDS_FORM_STATIC_LAW_OUTSIDE_THE_HULL_OF_ADAPTED_FORMATION_LAWS_AND_CLAUSE_INDEPENDENCE_ON_A_CAUSAL_PREDECESSOR_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-09-20.md`,
treat clocks whose rates depend on the recorded values. The dynamics clause
brings a pre-record conditional state at every unrecorded site (the supplied constructions). This note supplies a clock whose rate depends on that
state, and asks when the answer to "when does the record form" changes the
record.
- **Covariance leaves few rate functions.** With no preferred axis, the rate
  can depend only on the purity `|r|²`. A physical axis, the field of the
  recorded neighbours, adds `r·ĥ` and `(r·ĥ)²`; an unordered menu axis adds
  only `(r·n)²`.
- **On the field-aligned menu, when does not matter.** For an isolated site,
  whose neighbours all carry records, the clause makes the site precess about
  the field `h` of their contents, so `r·ĥ` is conserved. The recorded odds
  on the menu along `ĥ` are `(1 + r·ĥ)/2` for every clock, whatever its rate
  function. The isolated-field construction reads the same odds from a stationary state; here no
  stationarity is needed.
- **Elsewhere, the clock enters.** On a menu tilted from the field the four
  clocks give four different frequencies, and a state-dependent rate changes
  the mean formation time. With an unrecorded neighbour the field no longer
  conserves `r·ĥ`, and the field-menu odds depend on the clock too.
- **The record law stays a trace rule.** For every clock and menu the recorded
  frequency is the Born odds of one formation-weighted state. Clocks differ
  only through that state.

So inside the clause, the menu on which the record's odds are independent of
its formation time is guaranteed on the field-aligned menu of an isolated site. This is a sufficient case in which "how fast records form" is separable from
"which record forms".

## Setting and decision points

- **D-dyn, at the Heisenberg point (the supplied companion construction).** Between records,
  unrecorded neighbours interact by `J s·s`, the coupling that possibility
  covariance leaves. `J = 1` here.
- **Records as fields (the supplied companion construction).** A bond to a recorded site with content
  `q` becomes the field `(J/4) q·σ` on the unrecorded site. Two recorded
  neighbours with the same content give `H = (1/2) h·σ` with `h = J q`.
- **D-perm and D-tr (the supplied selective projector update).** A record `q` forms with odds
  `Tr(P_q ρ)` and compresses the state by `P_q`.
- **D-menu.** Where a recorded neighbour exists, the menu is antipodal along
  the field direction `ĥ`; elsewhere a supplied axis `z`.
- **D-form (supplied here).** Each unrecorded site carries a conditional-hazard clock
  with rate `f(ρ)`, a function of its conditional state. The four clocks
  used: constant; purity `|r|²`; the aligned odds `(1 + r·p)/2`; the
  alignment `2 (r·p)²`, where `p` is the menu axis.

None is adopted.

## Theorem 1 — covariance classifies the rate functions

Among polynomials of degree at most two in the Bloch vector `r`, computed by
Reynolds averaging over the relevant group:
- invariant under every internal rotation: dimension 2, spanned by
  `{1, |r|²}`;
- invariant under rotations about a physical axis `h`: dimension 4,
  `{1, |r|², r·ĥ, (r·ĥ)²}`;
- invariant under rotations about a menu axis `n` together with the flip
  `n → −n` of an unordered antipodal menu: dimension 3, `{1, |r|², (r·n)²}`.

So a rate odd in `r·p` needs a physical axis, not just a menu. ∎

## Theorem 2 — an isolated site's field menu is clock-independent

Take the supplied two-record field example (or a six-neighbour configuration with the same resultant), so `H = (1/2) h·σ`
with `h = J q`, and a conditional Bloch vector `r₀` of length 0.8 at
`r₀·ĥ = 0.565`.
- **Precession.** `[H, ĥ·σ] = 0`; the Bloch vector rotates about `ĥ` at
  angular frequency `|h|` (checked against the exact propagator to 1e-16),
  and `r·ĥ` is conserved to 2e-16.
- **The formation density.** For a clock of rate `f(t) = f(ρ(t))` the record
  forms at time `τ` with density `f(τ) exp(−∫₀^τ f)`; frequencies below are
  conditional on a record forming before `T = 60`, where the survival is at
  most 2e-15.
- **Field menu.** For all four clocks the recorded frequency of `+ĥ` equals
  `(1 + r₀·ĥ)/2 = 0.7826` to 2e-16.
- **Tilted menu.** On the menu `p ∝ ĥ + 0.9 ê⊥`, the four clocks give 0.8437,
  0.8154, 0.8360 and 0.8570 (spread 0.0417).
- **Formation times.** The conditional mean formation times are 1.000, 1.562,
  1.278 and 1.565: a state-dependent rate changes when, and on the tilted
  menu also what, is recorded.

The field-menu identity holds for any rate function of the trajectory,
covariant or not, because the odds on that menu are constant in time. ∎

## Theorem 3 — the recorded law is a trace rule of the formation-weighted state

For a fixed clock, menu and trajectory, averaging the instantaneous trace probabilities gives
`Tr(P_p ρ_f)` with `ρ_f = ∫_0^T f(t) exp(-∫_0^t f) ρ(t) dt / (1-exp(-∫_0^T f))`, a valid state (`|r_f|` at most
0.7209 over the clocks and menus here; the identity holds to 1e-12). Clocks
differ only through `ρ_f`; a constant rate gives the exponential-window
average of the trajectory, independent of the menu. ∎

## Theorem 4 — an unrecorded neighbour brings the clock back in

Take site `A` in the field `h` of its recorded neighbours and one unrecorded
partner `B` coupled by the Heisenberg bond, with `B` at Bloch length 0.9.
Then `r_A·ĥ` varies by 0.252 along the trajectory, and the field-menu
frequencies of the four clocks are 0.7197, 0.7204, 0.7242 and 0.7535
(spread 0.0338), all away from the isolated value 0.7826. So the
clock-independence of Theorem 2 is illustrated by the isolated-site case, without establishing necessity or an Admissibility law. ∎

## Diagnostic — a ring of six with clocks everywhere

Six qubits on a ring, a fixed random initial state, clocks at every site,
field-aligned menus where a recorded neighbour exists and the `z` axis
elsewhere, the compression update at each record, run to full recording; 60
trajectories per clock. The stack frequencies of the aligned outcome are
0.481, 0.497, 0.521 and 0.506, each with trajectory-level standard errors in the current runner, so within Monte Carlo error of
each other at this size, while the mean times to full recording are 2.59,
12.91, 15.26 and 44.00. This is a finite diagnostic of a supplied model; no
bias is claimed from it.

## What this means for the lanes

- **Record formation.** Inside the clause, "when a record forms" is a
  separate decision point from "which record forms" on the
  field-aligned menu of an isolated site. In other examples the two can be
  coupled through the formation-weighted state.
- **The Admissibility sentence.** Clock independence still depends on the supplied initial component `r_0·ĥ`. It does not show that neighbour records alone determine the odds. A separate preparation rule would be required.
- **The tick.** A constant rate makes formation Poisson with mean interval
  `1/f`, independent of the state; the state-dependent clocks change the
  mean interval by up to a factor 17 in the ring diagnostic. Which rate
  function the framework uses remains supplied.

## What stays open

- Which rate function, if any, the axioms favour. Covariance alone leaves arbitrary functions of `|r|²` without an axis; the degree-two class is `a+b|r|²`, restricted to nonnegative rates.
- The many-site record law beyond isolated sites, where the clock enters.
- Whether the formation-weighted state of Theorem 3 can be read as the
  conditional state of the Admissibility distribution.

## Prior art

Ghirardi, Rimini and Weber 1986 and Diósi 1989 (spontaneous localization
with state-dependent rates); Gisin 1984 and 1989 (stochastic state reduction
and no-signalling); Dalibard, Castin and Mølmer 1992 (quantum jumps at
state-dependent rates); Zurek 2003 (pointer states). All cited as prior art,
not as premises.

## Checks

The runner has five check families; the paired output records current results and runtime.

| Check | Result |
|---|---|
| Rate functions | Invariant dimensions 2, 4, 3 for no axis, a field axis, an unordered menu axis. |
| Isolated site | `[H, ĥ·σ] = 0`; `r·ĥ` conserved to 2e-16; field-menu odds 0.7826 for all four clocks to 2e-16; tilted-menu odds 0.8437, 0.8154, 0.8360, 0.8570; mean formation times 1.000, 1.562, 1.278, 1.565; survival at `T = 60` at most 2e-15. |
| Formation-weighted state | `|r_f|` at most 0.7209; trace-rule identity to 1e-12. |
| Unrecorded neighbour | `r_A·ĥ` varies by 0.252; field-menu odds 0.7197, 0.7204, 0.7242, 0.7535. |
| Ring of six | Aligned-outcome frequencies 0.481, 0.497, 0.521, 0.506 (with trajectory-level standard errors in the current runner); mean times to full recording 2.59, 12.91, 15.26, 44.00. |

## Independent check

Current source review and independent algebra/finite controls are recorded in the landing evidence. Historical author diagnostics are superseded by the paired current output.

## What this does not do

- It adopts no clause, update, menu or clock; the rate function is supplied.
- It does not derive when records form, or claim the constant-rate clock is
  preferred; it shows on which menu the choice of clock is invisible.
- It gives exact identities for supplied one- and two-site trajectories, evaluates time integrals numerically, and simulates six sites with a finite time step and small Monte Carlo sample.

## Exact boundary of the clock calculation

Here the bond is `J sigma_i.sigma_j/4`; earlier Pauli-bond notes use a coefficient multiplying `sigma_i.sigma_j` directly. Thus this J is four times that coefficient. The isolated numerical example has two equal recorded neighbours; six equal records with the same bond coefficient would give a field three times larger. The nonzero field direction and positive probability of formation are required; a zero-rate clock has no conditional recorded law. The rate may depend on state and menu, so the averaged state is generally `rho_f(p)` and the map from an initial state to recorded probabilities need not be affine. A common menu-independent averaged state follows only for a menu-independent hazard and trajectory.

A stationary state gives clock-independent odds on every menu, including tilted menus. An interacting stationary or maximally mixed joint state supplies another exception. Hence isolation and field alignment are sufficient, not necessary, conditions. This does not remove the dependence on the supplied initial component `r_0.hhat`, and does not derive an Admissibility law from neighbour records alone. Quadratic invariant dimensions follow by writing a polynomial as `a+b.r+r^T C r`: full rotations force b=0 and C proportional to identity; axial rotations permit b along the axis and two quadratic coefficients; axis reversal removes the linear term. Random group averaging is a numerical control, not the proof.

The ring is a fixed-step simulation with dt=0.05, Bernoulli rate*dt firing and at most one selected event per step, capped at time 400. It is not an exact simulation of continuous hazards: simultaneous proposed events are discarded. No time-step convergence or continuous-time accuracy is established. Frequencies use six outcomes per trajectory; errors must be estimated across independent trajectories, not as if all six outcomes were independent. The current runner verifies completion and reports the trajectory standard error. No-click evolution is the supplied unitary trajectory; no quantum-jump measurement consistency is inferred from a phenomenological state-dependent hazard.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [formation_clock_field_aligned_menu_odds_do_not_depend_on_when_records_form_2026_09_24.py](../scripts/formation_clock_field_aligned_menu_odds_do_not_depend_on_when_records_form_2026_09_24.py). Paired output: [current runner output](../logs/runner-cache/formation_clock_field_aligned_menu_odds_do_not_depend_on_when_records_form_2026_09_24.txt). All numerical historical figures above describe the declared finite setup; current tolerances and diagnostics are in this paired output.

## No-Go Discipline Gate

This section bounds the negative subclaims; it grants neither a retained grade nor an exhaustive search over physical alternatives.

### N1 — Alternative routes

- **ATTEMPTED — Polynomial symmetry.** Obtain another degree-two rate invariant in the stated symmetry class. The linear and quadratic coefficient classification gives dimensions two, four and three.
- **ATTEMPTED — Aligned conservation.** Change constant instantaneous field-menu odds by changing a nonnegative hazard. Normalized time weighting leaves a constant unchanged whenever formation probability is positive.
- **ATTEMPTED — Tilted precession.** Extend clock independence to arbitrary menus. Weighted transverse precession gives different odds for different constant rates, so the extension fails.
- **ATTEMPTED — Interacting neighbour.** Extend conserved local field projection to arbitrary coupled states. The supplied two-site example violates that conservation; stationary joint states remain exceptions.
- **ATTEMPTED — Menu-dependent hazard.** Represent every menu by one common weighted state despite a menu-dependent hazard. Each menu has its own weighted state in general; a common state requires the extra menu-independent weighting condition.

These are the actual formulations tested in the argument and controls above. Successful escapes narrow the rejected broader claim; they are not counted as failed physical alternatives.

### N2 — Conditional structure

No count of independent physical walls is asserted. Dynamics, preparation and readout are supplied jointly; implication relations between possible derivations of them remain unresolved. The scoped results use their explicit hypotheses rather than an asserted wall-independence theorem.

### N3 — Hidden assumptions

The stated Hamiltonian, state preparation, record compression and readout are conditional mathematical inputs, not additions to the axioms. Numerical tolerances and finite graph sizes are diagnostics, not exact or thermodynamic proofs.

### N4 — Residual matching

No prior no-go is used to close an additional residual. Linked companion notes supply only their displayed covariance, projector or probability identities. The examples above do not certify other formation laws or physical models.

### N5 — Resolution

- `per_element:` Degree-two rate invariants and weighted trace probabilities are tested.
- `per_site:` Isolated precession and clock-weighted local menus are tested.
- `per_mode:` checked and not executed — no normal-mode or continuum clock limit is claimed.
- `per_block:` One- and two-site trajectories and finite-step six-site samples are tested.
- `lattice_wide:` checked and not executed — no many-site continuous-time limit or formation law is derived.

### N6 — Partial closure

Choosing the stated supplied model yields the conditional theorem without adopting a new axiom. A convention cannot by itself select its state, dynamics or probability law. No claim that a new axiom is necessary is made.

### N7 — Strongest counter-route

Choose a stationary joint state: every menu then has constant instantaneous odds even with interacting neighbours. Alternatively let the hazard depend on the menu, producing different averaged states across settings. These mechanisms refute necessity of isolation and a universal common-state inference. The retained identity is for one fixed clock, menu and trajectory with positive formation probability.

### N8 — Related work

The linked companion sources are the relevant nearby arguments rechecked for this result. Their conditional boundaries are preserved here. Similar wording or a prior finite computation does not supply a universal obstruction.
