# The Composite Link Under Two Named Record Instruments: Pointer/Erased Split, Exact Slaving, and the Instrument Footprint

**Date:** 2026-06-09
**Type:** bounded theorem (instrument-conditional pointer/erased characterization + exact slaving structure for the matter-induced composite link under repeated record steps), containing an exact single-edge mode decomposition and an instrument-dependence exhibit
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_record_instrument_composite_link_erasure_slaving_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_record_instrument_composite_link_erasure_slaving_2026_06_09.txt`
**Status:** source proposal. All statements are finite-dimensional exact algebra
checked by the runner (`PASS=40 FAIL=0`). Authority role: source proposal; the
audit lane sets status.

## The named residual this addresses

The gauge-dynamics convergence note
(`ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08`;
`unaudited` on the live ledger at drafting time) reduces the interacting-gauge
foundation's undelivered input to a continuous-time gauge-link /
color-einselection dynamics. The sibling induced-trajectory note
([`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md),
on main, no ledger row at drafting time) showed that the matter dynamics induces a
locally covariant composite-link trajectory `U_eff(t) = polar(M(x,y;t))` that
is **not autonomous** in the link variable: the increment consumes matter data
the link compression discards (chord bilinears; the positive part `Q`). Its
named not-foreclosed routes included record-coupled matter dynamics — route
R-B. This note works that route **bounded-by-design**: what do repeated record
steps on the matter sector do to the induced composite link?

## The admission, named honestly (this is NOT a derivation)

The formation rule/process is not supplied by the axioms
(`record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06`,
post-append narrowed scope). Any concrete record instrument is therefore
a **named admission**. This note names two, chosen to flank the admission
space at the per-site occupancy level; Lueders instruments of this class have
a framework-side Stinespring construction
(`persistent_record_instrument_construction_narrow_theorem_note_2026-05-22`,
ledger `retained_bounded` at drafting time), so well-formedness is not the
issue — **which** instrument acts, and at what strength/schedule, is the
admitted content:

- **I-A — per-site occupation-basis dephasing instrument.** Lueders projectors
  onto joint eigenspaces of `(n_{x,1}, n_{x,2}, n_{x,3})` in the supplied
  per-site `C^3` color basis (8 projectors per site): the **finest** per-site
  occupancy readout. It **names a color frame at every site** — exactly
  ADM-1-shaped content, supplied by hand, visibly.
- **I-B — per-site total-occupation Lueders instrument.** Projectors onto the
  eigenspaces of `N_x = sum_i n_{x,i}` (4 per site): the **coarsest**
  non-trivial per-site occupancy readout. It is **color-blind** (`N_x`
  commutes with every local color-frame rotation), so it names **no** frame.

Both act at partial strength `lam in [0,1]`
(`rho -> (1-lam) rho + lam sum_P P rho P`), interleaved with exact Hamiltonian
steps `e^{-iH tau}` of the sibling note's model Hamiltonians (uniform
quadratic nearest-neighbor hopping; free `V = 1` and frozen-generic-`SU(3)`
background `V`). The strength `lam` and period `tau` are admission parameters;
nothing here derives that records form, which instrument acts, or at what
rate.

## Setting and conditionality (load-bearing, named)

Every statement is conditional on all of: (1) the **supplied `C^3` color
carrier** (`color_su3_matter_realization_residual_map_2026-06-05`, ledger
`meta`; nothing here derives color); (2) **the named model Hamiltonians** (the
covariant-hopping "connection" reading,
`matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08`,
is `unaudited` on the live ledger and is **not** consumed — the background `V`
is just a named model coefficient); (3) **the named instruments I-A/I-B with
admitted `(lam, tau)`**; (4) the **>= 3-occupied-mode / rank-3 precondition**
of the composite-link construction
(`color_link_index_routing_via_cross_site_matter_bilinear_unitarization_bounded_theorem_note_2026-06-08`,
`unaudited` on the live ledger; consumed as the definition under study).
States are one-body densities `0 <= rho <= 1`; `M(x,y)` is the cross-site
one-body block. The Fock-level anchor (Part A of the runner) verifies on a
6-mode Jordan-Wigner space with **non-Gaussian** states that both instruments'
adjoints preserve the one-body operator span, so the one-body data evolves
autonomously and exactly under instrument + quadratic-Hamiltonian
interleaving; all dynamics statements below are at that level, exact.

## Verdict (four exact findings)

### 1. Dephasing structure: the link carrier is erased content under BOTH instruments

The exact one-body action (Fock-verified at `lam = 1` and `lam = 0.4`,
deviation `< 1e-12`, non-Gaussian state):

```
  I-A at site x:  M(x,x) -> (1-lam) M(x,x) + lam diag M(x,x)
                  M(x,y) -> (1-lam)   M(x,y)   (each instrumented endpoint)
  I-B at site x:  M(x,x) -> M(x,x)   (preserved in full)
                  M(x,y) -> (1-lam)   M(x,y)
```

so with both endpoints instrumented the link carrier damps as
`M(x,y) -> (1-lam)^2 M(x,y)` per step under **either** instrument, and at
`lam = 1` it is **erased exactly** (both `lam=1` maps are idempotent pointer
projections). Pointer content: under I-A, the named-frame occupation vector
`diag M(x,x)`; under I-B, the **full** local color density `M(x,x)`. Exactly
conserved by both instrument maps: `tr M(x,x)` (the gauge-invariant local
occupation). The composite link `U_eff = polar(M(x,y))` is therefore **not
pointer content of local occupancy records** — it lives in the erased sector
for both named instruments. (Scope: the two named instruments; a coarser
partition of the `N_x` spectrum, e.g. `{0,1} vs {2,3}`, would erase only part
of the cross-site coherence — no all-instrument claim is made.)

### 2. Covariance of the surviving content: exact split, instrument-inherited

- **I-B is exactly color-blind:** the Fock channel commutes with every local
  color rotation (`7.97e-18`), the registered content `M(x,x)` transforms in
  the Ad-class (`M(x,x) -> g_x M(x,x) g_x^dag`; its spectrum is invariant
  registered data), and the **entire instrumented link trajectory** retains
  the sibling note's joint local covariance
  `U_eff(t) -> g_x U_eff(t) g_y^dag` **exactly** (`1.3e-14` along interleaved
  trajectories).
- **I-A breaks it, order 1:** the channel does not commute with local
  rotations (violation `3.96e-3` at Fock scale vs `7.97e-18` for I-B), the
  registered occupation vector is frame-dependent (not stable under generic
  local `g`), the local-density spectrum is changed by the instrument
  (`0.231`), and the instrumented trajectory's joint local covariance fails at
  order 1 (`1.32`).

The covariance of the I-B pointer sector is **inherited from the instrument
choice**, not derived: the instrument-dependence exhibit (Finding 4) shows an
equally admissible instrument registers non-covariant content. No
einselection-selection is discharged.

### 3. Increment structure under interleaving: the non-autonomy is STRUCTURED — hidden-data channels are exactly the damped modes, and the link becomes slaved, not closed

**Single edge: exactly solvable.** With `V` unitary and unit hopping
normalization (`kappa = 1`; general `kappa` rescales `tau`), `H_edge^2 = 1`,
so `e^{-iH tau} = cos(tau) - i sin(tau) H` exactly and the composite step has
exact block identities (runner `< 1e-13`):

```
  M(x,x)' = cos^2(tau) M(x,x) + sin^2(tau) V M(y,y) V^dag
            - i sin(tau)cos(tau) (V M^dag - M V^dag)
  M' = eta [ cos^2(tau) M + sin(tau)cos(tau) s + sin^2(tau) V M^dag V ],
       eta = (1-lam)^2,    s = -i( V M(y,y) - M(x,x) V ).
```

Because `V s^dag V = -s` for **every** Hermitian density pair (exact identity,
`4.5e-15`), the cross-block sector decomposes exactly:

- the **s-parallel mode** is driven, with the **exact** slaved coefficient
  `alpha = eta sin(tau)cos(tau) / (1 - eta cos(2 tau))` (fixed-point identity
  `3e-20`);
- **every s-orthogonal cross mode contracts at the instrument rate ~ eta per
  step** (an exact operator-norm bound — the homogeneous cross-map
  `m -> eta[cos^2 m + sin^2 V m^dag V]` has norm `<= eta` by the triangle
  inequality; measured `0.009973` vs `eta = 0.01`).

Consequences, all measured exactly:

- **Slaving:** on the record-dominated slow manifold `U_eff = polar(s)` — a
  function of **pointer content + the frozen background only** (`2.4e-14`
  after burn-in; same for free hopping `V = 1`, `1.6e-14`). At `lam = 0` the
  deviation is order 1 (`2.15`): without records there is no slaving.
- **The slaved link is a constant of the relaxation:** `s' = cos(2 tau) s +
  O(eta)` feedback per step (per-step deviation `1e-4`, bound
  `5 eta/(1-eta)`), so the source contracts **along its own direction** — the
  registered link direction is frozen (drift `5.5e-9` over 2000 steps) while
  the pointer sector relaxes toward the link-transported balance
  `M(x,x) = V M(y,y) V^dag` at the second-order rate `sin^2(tau)` per step.
  The pointer flow **is closed at leading order (autonomous in the registered
  data)**:
  `Delta M(x,x) = -sin^2(tau)( M(x,x) - V M(y,y) V^dag ) + O(eta)` feedback
  (max rel err `0.0199`, exactly the `eta/(1-eta) = 0.0101` feedback scale;
  the I-A analogue is closed on its dephased occupations, `0.0198`).
- **4-cycle (chords present):** the slaving holds at leading order
  (`7.7e-4` at `lam = 0.9, tau = 0.02`, shrinking `>= 3x` under `tau`-halving
  to `1.9e-4`) and the **chord channel is damped out of the slaved
  direction**: `polar(s_chordful) = polar(s_local)` to `1.5e-5`, three orders
  below the leading deviation — records **localize** the slaved link. The
  `lam = 0` baseline is order 1 (`3.15`).
- **The block-01 exhibit under records:** the two states with identical
  `U_eff(0)`, identical local densities, different positive parts — which
  separate at `lam = 0` (max `0.342`, reproducing the sibling exhibit) —
  are suppressed **monotonically** in record strength
  (`0.342 > 0.105 > 0.058 > 0.017` across `lam = 0, 0.3, 0.7, 0.95`) and
  **converge** in the record-dominated regime (final separation `0.0046 <
  5%` of the `lam = 0` max): the records damp exactly the hidden-`Q`
  channel that defeated link-autonomy. Mechanism (elementary, from the exact
  step): the difference of two states with identical pointer content is a
  pure cross-block perturbation whose common drive cancels, so it evolves
  under the homogeneous cross-map and contracts at rate `<= eta` per step,
  up to the `O(tau |delta|)` pointer feedback visible as the small transient.

So the sibling note's non-autonomy neither persists unchanged nor is repaired
into a link-level generator: it is **structured**. The hidden-data channels
(chords, `Q`-deformations) are exactly the eta-damped modes; what survives is
a link **slaved** to registered pointer content plus the frozen background. In
the record-dominated regime the link stops being an independent dynamical
variable at all — the closed object is the **pointer-sector flow**, with
`U_eff` a dependent functional of it. This is a relocation of the dynamics
question to the compression level, not a delivery of a link generator (the
background `V` does not evolve here; nothing supplies its dynamics).

### 4. Instrument-dependence teeth: what is and is not the admission's footprint

**Instrument-independent across the two named instruments** (and only across
these two): the link carrier `M(x,y)` is erased content; `tr M(x,x)` is exact
pointer content; the slow/fast slaving structure exists with the same exact
rates (`eta` damping, `sin^2(tau)` pointer flow); the exhibit pair converges.

**Instrument-dependent (the admission's footprint, exhibited):** WHICH
on-site content is registered (frame-diagonal occupations vs the full
Ad-covariant density — spectrum preserved by I-B, deformed by I-A at `0.231`);
the covariance of the instrumented trajectory (exact vs order-1 broken); and
the **slaved link value itself**: from the same initial state,
`|U_slaved(I-A) - U_slaved(I-B)|_F = 2.10` — order 1. An observer of the
record-dominated composite link sees data that depends on which instrument
was admitted. The frame-naming instrument I-A is precisely an ADM-1-shaped
admission made visible; the existence of the color-blind alternative I-B shows
the frame-naming is **not forced** by the record route — and the existence of
I-A shows covariant registration is not forced either. The selection between
them is the undischarged einselection hat, exhibited as a two-point admission
space.

## What the runner verifies (`PASS=40 FAIL=0`)

Part A (11): Jordan-Wigner CAR; one-body closure on a non-Gaussian state; both
projector families (resolution of identity, idempotent, Hermitian); the exact
one-body rules for I-A and I-B at full and partial strength; site-composition
order-independence; the Fock intertwiner; I-B channel covariance exact / I-A
violation (teeth); `tr M(x,x)` conservation.
Part B (5): `lam = 1` pointer/erased split for both instruments; idempotence;
spectrum preserved (I-B) vs changed (I-A); Ad-covariance of I-B pointer
content vs frame-dependence of I-A's.
Part C (12): `H^2 = 1` + exact polynomial exponential; exact one-step block
identities; `V s^dag V = -s`; the exact slaved coefficient `alpha`;
record-dominated slaving `U_eff = polar(s)` (cov and free `H`); exact
`eta`-contraction of s-orthogonal modes; frozen slaved link along relaxation;
`cos(2 tau)` source contraction with `O(eta)` feedback window; leading-order
closed pointer flow (I-B and I-A); `lam = 0` order-1 contrast.
Part D (7): 4-cycle leading-order slaving with `tau`-scaling; chord
localization; rank health; `lam = 0` baseline; joint local covariance of the
instrumented trajectory exact (I-B) / broken (I-A).
Part E (5): exhibit pair validity; `lam = 0` separation; monotone suppression;
record-dominated convergence; the order-1 instrument footprint on the slaved
link.

## Honest boundaries — what this does NOT establish

- **No discharge of any gate.** ADM-1 (local color-frame redundancy), the R1
  link generator, the R2 mixing regime, and the blocking-isometry/einselection
  selection are all untouched. In particular this note does **not** show that
  einselection selects gauge-invariant (or any) content: the covariant pointer
  sector under I-B is put in by choosing a color-blind instrument, and I-A
  registers frame-dependent content with equal admissibility. Which instrument
  is realized is exactly the open selection question, here exhibited, not
  answered.
- **Formation rule/process is not derived.** Both instruments, their strength
  `lam`, and their schedule `tau` are named admissions, consistent with the
  post-append narrowed boundary; nothing here fixes which instrument realizes,
  which record locks, or at what rate. No arrow or rate is derived (the `R-C`
  layer is untouched).
- **Not a link dynamics.** The slaving result removes the link's independent
  dynamics in the record-dominated regime rather than supplying one: `U_eff`
  becomes a dependent functional of pointer content and the **frozen**
  background `V`, whose own dynamics nothing here supplies. R1 remains
  undelivered; this bounds where it can live (weak-record regimes, where the
  sibling non-autonomy rules, or carriers beyond the matter compression).
- **Two named instruments only.** "Instrument-independent" statements
  quantify over I-A and I-B, not over all instruments (coarser `N_x`
  partitions would erase only part of the cross-site coherence; instruments on
  non-occupancy data are not touched).
- **Finite exact model.** 2-site edge and 4-cycle, one-body level (anchored at
  Fock level for the rules), sampled `(lam, tau)` grids; no continuum,
  thermodynamic, or mixing/CLT statement (R2 is shaped only in that the
  slaved regime names a compression level; no step statistics are claimed).
  The leading-order statements carry measured `O(eta)`/`O(tau)` windows;
  the exact identities (block step, `V s^dag V = -s`, `alpha`, erasure rules)
  are the load-bearing content. Quantitative magnitudes (`2.10`, `0.342`,
  `0.231`, ...) are seed-specific.

## Relation to the wall

The same-wall convergence note left one undelivered input with four hats. This
block moves the **einselection hat conditionally and honestly**: under a named
local occupancy instrument, the registered content of the composite link
construction is characterized exactly (erased carrier; instrument-dependent
on-site pointer content; `tr M(x,x)` always registered), and the
**instrument footprint is the exhibited residual** — the ADM-1-shaped frame
choice reappears as WHICH instrument acts. For the R1 hat it adds a sharpened
boundary from the record side: interleaving records with the derived matter
dynamics does not produce a link-level generator; it produces an exactly
solvable slow/fast split in which the link is slaved and only the pointer
sector carries an autonomous (registered-data-only) flow at leading order.
Within this two-instrument finite model, any genuine link dynamics on this
record route would have to live where records are weak (where the sibling
non-autonomy obstruction governs) or on carriers the matter compression does
not reach.

## Negative-boundary discipline

This is a bounded dependency map, not a no-go against all record-coupled gauge
dynamics.

- Alternative routes left open: a different record instrument; a derived
  einselection rule selecting one instrument; weak-record dynamics before the
  slaving limit; a carrier beyond one-body matter compression; and an
  independent dynamics for the frozen background `V`.
- Wall independence: record formation, instrument selection, color carrier,
  Hamiltonian/model choice, and rank/precondition inputs are independent
  admissions here. Closing one does not close the others.
- Hidden-wall scan: strength `lam`, schedule `tau`, supplied `C^3` carrier,
  frozen background `V`, finite edge/4-cycle geometry, and rank health are all
  explicit inputs, not silent derivations.
- Residual matching: the claim targets only the sibling composite-link
  non-autonomy residual under two named record instruments. It does not target
  ADM-1, R1, R2, record formation, arrow/rate, or general einselection.
- Rhetoric resolution: "instrument-independent" quantifies only over I-A and
  I-B; "erased" means erased by the named local occupancy instruments; "closed
  pointer flow" is leading-order in the stated record-dominated windows.
- Partial-closure scan: I-B supplies a conditional covariant pointer sector,
  but that is an admitted instrument choice, not a selection theorem.
- Steelman: a future retained einselection theorem could select a covariant
  instrument and thereby remove the two-point footprint exhibited here. This
  note leaves that route open.
- Cross-cycle echo: prior overbroad record-route claims were repaired by making
  the supplied readout context explicit. This note follows that pattern by
  treating the instruments as admitted context rather than consequences of
  Record.

## Cross-references

- Sibling induced-trajectory note (construction + non-autonomy exhibit reused):
  [`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  (on main; no ledger row at drafting time)
- The composite-link construction (consumed as the definition under study):
  [`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  (`unaudited` at drafting time)
- The admission's ground:
  [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
  (`retained_no_go` at drafting time)
- Instrument-class constructibility:
  [`PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22`](PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md)
  (`retained_bounded` at drafting time)
- Record-side dynamics boundaries (respected): `record_classical_semigroup_boundary_2026-06-06`
  (`retained`), `record_markov_generator_embeddability_boundary_2026-06-06`
  (`retained_no_go`)
- The supplied color carrier (conditionality inherited):
  [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md)
  (`meta`)
- The dynamics wall (the residual being shaped):
  `ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08`
  (`unaudited` at drafting time)
- The covariant-hopping connection reading (NOT consumed; named for scope):
  `matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08`
  (`unaudited` at drafting time)
- Color algebra dependency: [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  (`retained`)

Ledger statuses cited above were verified against the live audit ledger at
drafting time; consult the ledger for current statuses — this source note does
not set or update any of them.

- Standard math cited for method only: Jordan-Wigner representation, Lueders
  instruments / operator-sum maps, polar decomposition, involution identity
  `e^{-iH tau} = cos(tau) - i sin(tau) H` for `H^2 = 1`.
