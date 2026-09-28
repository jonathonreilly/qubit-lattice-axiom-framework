---
claim_id: a_lapse_set_by_record_events_at_linear_order_positive_record_kinetics_either_keep_einsteins_negative_scalar_or_add_a_scalar_graviton_the_closing_lapse_needs_the_dewitt_line_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Linear-order comparator lemmas bearing on the owner's reading 'time is the shifting or creation of records', read as a lapse (local tick rate) set by record events. (A) Restriction: with the Einstein-Hilbert scalar (transverse-trace) entry unchanged, adding a positive lapse sector of any size, with any bilinear couplings to that scalar and its momentum, leaves the quadratic form indefinite, and eliminating it lowers the entry. Direct changes to the scalar block itself (seagull, higher-curvature or other local terms) are outside this lemma. (B) The ADM scalar sector (kinetic K_ij K_ij - lambda K^2, shift solved), derived symbolically. The scalar kinetic coefficient is 2(3 lambda - 1)/(lambda - 1), and at lambda = 1 the shift equation freezes the scalar. With an auxiliary lapse (Lagrangian xi n R^(1) + alpha (dn)^2, no conjugate) the scalar has omega^2 = (lambda - 1)(2 - alpha) k^2/((3 lambda - 1) alpha), reproducing Blas-Pujolas-Sibiryakov: healthy iff (lambda > 1 or lambda < 1/3) and 0 < alpha < 2. The eliminated kernel is non-analytic and violates probe 11's identity. (C) The landed kinetic family alpha tr v^2 + beta (tr v)^2 is lambda = -beta/alpha. It is positive only for lambda < 1/3, while the landed lattice lapse bracket closes only on beta = -alpha, i.e. lambda = 1, which takes (-6, 2, 2) alpha on uniform strains (re-verified). E-H with the Hamiltonian constraint, in transverse gauge, keeps exactly the two TT tensors. (D) The momentum-rule qubit moves are non-abelian: 26 of the 30 overlapping translates of probe 10's 20-slot move fail to commute on constructed configurations, and the 4 axis neighbours commute. Hence, at linear order and within these comparators: positive record-like kinetics (lambda < 1/3) with an auxiliary lapse carry a healthy extra scalar graviton; the lapse whose lattice bracket closes needs the indefinite line lambda = 1. Not shown: nonlinear closure, a native record dynamics, whether the qubit moves can be first-class constraints, any bridge from records to a lapse, or which reading the axioms intend."
upstream_dependencies:
  - minimal_axioms
runner: scripts/a_lapse_set_by_record_events_physical_auxiliary_or_gauge_2026_09_28.py
---

# A lapse set by record events, at linear order: positive record kinetics either keep Einstein's negative scalar or add a scalar graviton; the closing lapse needs the DeWitt line

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** linear-order comparator lemmas, one symbolic ADM derivation, and
a fact about the qubit move algebra; unaudited. Independent checks are
recorded below. This is a narrowed revision: the first version overclaimed
(see Independent checks).

## In one paragraph

Probe 11 found that Einstein's graviton avoids helicity-1 partners only
through a negative scalar sector. The owner's reading, "time is the shifting
or creation of records", suggests a lapse set by record events. At linear
order, and in the standard comparators, this is what happens.
- **The kinetic energy decides most of it.** Record-like kinetic energy is
  positive. In the standard variables that means the DeWitt parameter
  λ < 1/3.
- **Positive kinetics with a lapse fixed by its own equation** (an auxiliary
  lapse). The negative scalar is repaired, but only by turning it into a
  healthy extra scalar graviton. This is the known Hořava / Blas–Pujolas–
  Sibiryakov result, re-derived here.
- **Einstein's mechanism** needs λ = 1: a kinetic energy with a negative
  part. There the momentum constraint freezes the scalar, and the landed
  lattice lapse bracket closes only on that line. No positive kinetic term
  lies on it.
- **Simply adding a positive "rate" sector** coupled to the scalar cannot
  repair it: that only lowers the scalar's energy.

So record-like positive kinetics and the lapse that closes on the lattice
sit on opposite sides of the DeWitt line. That is a sharp version of the
problem. It is not a verdict on the owner's reading: nothing here bridges
records to a lapse, and nonlinear or collective effects are untested.

## Prior art

On main, read before this note:
- **Block 112 (2026-09-24),**
  [ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md](ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
  At flat strain and linear in canonical momentum, the member's lapse
  bracket closes into relabellings for every lapse pair iff β = −α with
  symmetric face timing.
- **The 2026-09-25 clock-profile note,**
  [ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md](ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md).
  - The closing line is indefinite and admits no positive kinetic term.
  - For the stipulated walker-only placements, exact closure fails at third
    order in the lapses' wavenumbers.
  - That note leaves higher orders and the full coupled cross bracket open.
- **The 2026-09-14 tensor note:** the compact bound.
- **Probes 10 and 11 of this PR.**

External, reference only; B re-derives what it uses:
- Hořava (2009);
- Blas, Pujolas and Sibiryakov (arXiv:0909.3525): their eqs. 12 and 19 give
  the scalar kinetic coefficient and speed reproduced in B;
- Henneaux, Kleinschmidt and Lucena Gómez (2010), on the Hamiltonian
  constraint when λ ≠ 1;
- Jacobson's Einstein–aether and khronometric theories. These have a
  physical preferred-frame field together with a gauge lapse, so "physical
  rate" and "Hamiltonian constraint" are not exclusive readings.

## Premises

- **Linear order around flat space; Gaussian comparators.**
- **The ADM Lagrangian.** K_ij K_ij − λK² + ξR + α a_i a_i, with
  K_ij = (1/2)(ḣ_ij − ∂_i N_j − ∂_j N_i) and a_i = ∂_i ln N.
  - The scalar sector is h_ij = 2ζ δ_ij, N_i = ∂_i B (gauge E = 0),
    N = 1 + n.
  - An auxiliary lapse has no conjugate and is fixed by its own equation.
- **The landed kinetic family** α tr v^2 + β (tr v)^2 corresponds to
  λ = −β/α.
- **The qubit moves** are probe 10's 20-slot witness and its translates,
  with `h_m = T_m + T_m^dag`.

## A — restriction lemma (check A)

**Statement.** Let Q be a quadratic form on (scalar amplitude, its momentum,
lapse sector). Suppose the scalar–scalar entry is E-H's transverse-trace
value, −(1/2)k^2, and the lapse block W is positive. Then Q is indefinite:
restricting to the scalar direction gives a negative value. Eliminating W
(the Schur complement) lowers the scalar entry by g^† W^{-1} g ≥ 0.

**Check.** Over 3000 random positive lapse sectors of 1–4 components, with
couplings to both the scalar and its momentum, the smallest eigenvalue is
always ≤ −0.5 k^2. ∎

**Scope.** This excludes only stable extra variables mixed into an unchanged
E-H scalar block. Local terms that change the block itself (seagull,
higher-curvature, background-dependent) are not excluded. If they make the
whole potential positive, probe 11's identity applies to the new form.

## B — the ADM scalar sector (check B, symbolic)

- **Kinetic term.** With the shift solved, the kinetic term is
  `2(3λ − 1)/(λ − 1) ζ̇^2`. At λ = 1 the shift equation is `−4k^2 ζ̇ = 0`:
  the scalar is frozen, and does not propagate.
- **Auxiliary lapse.** Take the Lagrangian terms ξ n R^(1) + α(∂n)^2, with
  R^(1) = 4k^2 ζ. The lapse's own equation gives n = −2ξζ/α, and the
  potential becomes `2ξ k^2 ζ^2 (1 − 2ξ/α)`.
- **Dispersion** (ξ = 1):
  `ω^2 = (λ − 1)(2 − α) k^2 / ((3λ − 1) α)`. This is Blas–Pujolas–
  Sibiryakov's result.
- **Health.** No ghost and no tachyon iff (λ > 1 or λ < 1/3) and
  0 < α < 2. The samples agree: healthy at (λ, α) = (0, 1), (0.2, 0.5) and
  (2, 1); unhealthy at (0, 2.5) and (0.5, 1).
- **Positive (record-like) kinetics.** These need λ < 1/3. So with an
  auxiliary lapse they carry a healthy extra scalar graviton; at λ = 0 and
  α = 1 its speed equals the TT speed.
- **α → 0** is the constraint limit. It is singular, a strong-coupling limit
  in the literature, and not a demonstrated smooth decoupling.
- **The eliminated lapse kernel** `c^2 R_lin^2/(4αk^2)` is not a quadratic
  form in k: the least-squares residual on a fixed tensor is 0.29. So the
  effective potential escapes probe 11's analyticity premise. On the
  spin-2 compression, (v2, v1, v0) = (1/2, 0, 1/6) and 4v1 − v2 − 3v0 = −1.

## C — the lapse that closes on the lattice sits on the indefinite line (check C)

- The landed family's dilation value is 3α(1 − 3λ). Positivity needs
  λ < 1/3: true at β = −0.3, −0.2 and 0, false at β = −0.5.
- The landed closing line β = −α is λ = 1. There the family takes
  (−6, 2, 2)α on the dilation, E and T strains (re-verified).
- With the Hamiltonian constraint (R_lin = 0) and in transverse gauge, the
  E-H comparator keeps exactly the two TT tensors, both at +1/2 k^2.
- So, within the landed lattice results, the lapse bracket that closes needs
  λ = 1. Positive record-like kinetics have λ < 1/3.
- That GR's own kinetic energy is indefinite (DeWitt) is a continuum fact.
  The lattice result is that closure picks that same line.

## D — the momentum-rule moves are non-abelian (check D)

- Take the 30 translates of probe 10's 20-slot move within radius 2 that
  share slots with it. On configurations built so that one move acts and
  then the other, 26 fail to commute. The 4 axis neighbours ±e_x and ±e_y
  commute.
- This is a fact about the move algebra only. Non-commutation neither
  proves nor excludes that local event rates are physical: GR's constraints
  do not commute, yet its lapse is gauge.
- Whether the moves, or the records' energy densities, could form
  first-class constraints is not tested.

## What this means for the owner's reading

At linear order and in these comparators:
- **Positive record-like kinetics** (λ < 1/3) and a lapse fixed by its own
  equation give GR's two tensor polarisations plus a healthy extra scalar
  graviton, with no helicity-1 partners.
- **A lapse whose lattice bracket closes** sits on the indefinite line
  λ = 1. There the scalar is frozen and only the two TT modes remain, but no
  positive kinetic term lies there.

Whether "time is the shifting or creation of records" selects either option
is not decided here. The axioms supply no time metric or rate. Collective
(strongly interacting) record dynamics could behave differently from these
comparators.

The concrete open question: can a positive record dynamics generate,
collectively, an effective DeWitt (λ = 1) kinetic structure with a closing
lapse bracket? Or can the extra scalar of the λ < 1/3 route be tolerated or
removed?

## No-Go Discipline Gate

The bounded negative claims:
- (A) a positive lapse sector with bilinear couplings cannot make the
  unchanged E-H scalar block positive;
- (C) within the landed lattice results, the closing lapse needs λ = 1,
  where no positive kinetic term lies.

Everything else is positive or derived (B, D).

- **N1 — attack routes.**
  1. *A positive lapse field with its own conjugate.* ATTEMPTED (A).
     Indefinite.
  2. *A fast positive lapse.* ATTEMPTED (A). It lowers the entry.
  3. *A multi-component lapse sector with couplings to the momentum.*
     ATTEMPTED (A). Still indefinite.
  4. *An auxiliary lapse.* ATTEMPTED (B). It works, with an extra healthy
     scalar for λ < 1/3.
  5. *A closing lapse with positive kinetics.* RULED OUT BY PRIOR within its
     scope (block 112; 2026-09-25 T3).
  6. *Changing the scalar block directly* (seagull or higher-curvature
     terms). Outside (A); open. If the result is positive, probe 11 applies.
  7. *Collective effective λ = 1.* Open.
- **N2 — conditions.**
  - Positivity of the kinetic term (λ < 1/3) and lattice closure (λ = 1)
    are disjoint in the landed family. That is a direct computation, not an
    independence claim.
  - Whether a collective dynamics can evade both is unresolved.
- **N3 — hidden conditions.** Linear order; flat background; the gauge
  E = 0; ξ = 1; the landed family's isotropic form (the cubic γ term is
  excluded by the landed T2).
- **N4 — residual matching.**
  - Block 112 and the 2026-09-25 note: closure on β = −α, at flat strain
    and linear in canonical momentum. Match yes, within that scope.
  - BPS: the dispersion is re-derived. Match yes.
- **N5 — rhetoric audit.**
  - "Either keep Einstein's negative scalar or add a scalar graviton" holds
    for positive kinetics with the lapse readings tested (A, B), at linear
    order.
  - "The closing lapse needs the DeWitt line" is the landed lattice result,
    re-expressed.
  - No statement is made about which reading the axioms intend.
- **N6 — partial closure.** No convention supplies an effective λ = 1.
  Which reading is intended is the owner's decision.
- **N7 — steelman.** A strongly interacting record system might produce an
  effective indefinite (λ = 1) kinetic term for its collective metric, with
  a closing constraint algebra, while every microscopic term stays positive.
  GR itself is positive-energy on physical states. This is open.
- **N8 — cross-cycle echo.** The member's clock algebra (landed) is the same
  wall. No retirement mechanism applies.
- **Outcome:** PASS as scoped.

## What this does not show

It does not show any of these:
- nonlinear closure, strong coupling, or any collective record dynamics;
- a bridge from record events to a lapse;
- whether the qubit moves can be first-class constraints;
- which reading the axioms intend;
- anything about matter coupling beyond the landed notes.

## Independent checks

- **First version** (commit 9c30cabe03), titled "a physical rate cannot
  remove Einstein's negative scalar sector; only a gauge lapse can".
  - **Codex `gpt-5.6-sol`: "FAILS".** Its points:
    - T1 did not establish probe 11's hypotheses for an arbitrary operator
      lapse. It ignored state-dependent, stochastic and non-Hermitian
      rates.
    - T2's scope was too broad.
    - T3's BPS identification was only schematic.
    - T4 overstated both GR and the landed lattice cost: "breaks exactly
      once matter is added" was false; the cubic-order defect is
      walker-only, and the cross terms are open.
    - T5 inferred observability of rates from non-commutation.
    - The title and the owner-facing conclusion overreached.
  - **Fable check (Claude Fable 5.1): "CONFIRMED WITH CORRECTIONS".** Its
    derivation of the ADM scalar sector showed that T3's propagating scalar
    and its speed came from an ad hoc positive kinetic term. BPS's actual
    result is reproduced here in B, and at λ = 1 the scalar is frozen. It
    also flagged:
    - T5(b) was a non sequitur;
    - T4's lattice cost was misattributed;
    - check C used a gauge condition as the momentum constraint;
    - the title's "only" was contradicted by T3;
    - T2 can be stated by restriction.
- **This revision.** It drops the operator-lapse theorem and the
  commuting-events lemma, and restates D as a fact. It re-derives the ADM
  scalar sector symbolically (B), states A as a restriction lemma with its
  scope, attributes the lattice results precisely (C), and narrows the
  title and conclusions.

Second round: pending.

## Reproduction

`python3 scripts/a_lapse_set_by_record_events_physical_auxiliary_or_gauge_2026_09_28.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in about 0.3 s. The canonical
cache is at
logs/runner-cache/a_lapse_set_by_record_events_physical_auxiliary_or_gauge_2026_09_28.txt.
