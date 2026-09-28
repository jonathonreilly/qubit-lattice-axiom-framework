---
claim_id: a_lapse_set_by_record_events_a_physical_rate_cannot_remove_einsteins_negative_scalar_sector_only_a_gauge_lapse_can_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Tests the owner's reading 'time is the shifting or creation of records' as a lapse (local tick rate) set by record events, against probe 11's obstacle (Einstein's graviton meets the helicity identity only through a negative scalar sector). (T1) A lapse that is a local operator on finite-dimensional record slots gives an ordinary bounded local Hamiltonian with a ground state, so probe 11 applies: under the momentum rule with cubic symmetry there is no first-order helicity-2 sum rule. (T2) In the Gaussian Einstein-Hilbert comparator, a lapse field with a positive quadratic form, coupled through the Hamiltonian-constraint density, leaves the scalar block indefinite for every coupling and stiffness. Eliminating it fast lowers the scalar potential (Schur). (T3) An auxiliary lapse, fixed instantaneously by its own equation with a negative gradient term -alpha k^2 n^2 (Horava / Blas-Pujolas-Sibiryakov type), makes the transverse trace positive for alpha < c^2 and leaves TT unchanged. It adds a propagating helicity-0 mode with speed^2 = c^2/alpha - 1 (TT speed 1), through a non-analytic kernel that violates probe 11's identity; alpha -> 0 is the constraint limit. (T4) A gauge lapse is GR's Hamiltonian constraint. The E-H comparator with it keeps exactly the two TT modes, both positive. Its lattice cost is landed (block 112 and the 2026-09-25 clock-profile note: closure only on an indefinite kinetic line, taking (-6, 2, 2) alpha on uniform strains, re-verified here; walker content breaks exact closure at cubic order; the 2026-09-14 compact bound). (T5) For records as local events: exactly commuting local generators never spread a local operator; overlapping momentum-rule qubit moves (probe 10's witness and 26 of 30 overlapping translates) fail to commute on constructed configurations. So event rates are physical unless the moves are first-class constraints, which is not constructed here. Gaussian comparators for T2-T4; no native record dynamics, constraint algebra or phase."
upstream_dependencies:
  - minimal_axioms
runner: scripts/a_lapse_set_by_record_events_physical_auxiliary_or_gauge_2026_09_28.py
---

# A lapse set by record events: a physical rate cannot remove Einstein's negative scalar sector; only a gauge lapse can

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** theorems on Gaussian comparators, an operator-level corollary of
probe 11, and explicit qubit-move checks; unaudited. Independent checks are
recorded below.

## In one paragraph

Probe 11 found that Einstein's graviton avoids the helicity-1 partners only
because its scalar sector has negative energy. GR's time constraint
removes that sector. The owner's reading, "time is the shifting or creation
of records", suggests a lapse set by the records: the local tick rate is the
local rate of record events. There are three ways that can be meant.
- **The rate is a physical property of the records.** It cannot remove the
  negative sector (T1, T2). A physical lapse is just part of an ordinary
  energy with a ground state, and that is exactly where probe 11's obstacle
  holds. Coupling a physical rate to the scalar only lowers its energy.
- **The rate is fixed instantly by its own equation, with a negative
  stiffness** (Hořava's route). This does remove the negative sector, but it
  adds a new scalar graviton with its own speed (T3). Only in the limit of
  zero stiffness does it become Einstein's constraint.
- **The rate has no physical meaning at all.** Time is only the order of
  record events. That is exactly Einstein's constraint (T4), and it works.
  On the lattice, the repository has already found its price: it needs a
  kinetic energy with a negative part, and it breaks exactly once matter is
  added.

A record-native check (T5): if record events all commuted, so that their
order never mattered, nothing would ever propagate. The momentum-rule qubit
moves do not commute when they overlap. So with those moves, event order
and event rates are physical, unless the moves are turned into constraints
of Einstein's kind, which this note does not construct.

## Prior art

On main, read before this note:
- **Block 112 (2026-09-24),**
  [ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md](ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
  The member's lapse constraints close into relabellings exactly, for every
  lapse pair, iff β = −α with symmetric face timing.
- **The 2026-09-25 clock-profile note,**
  [ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md](ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md).
  - Every clock profile forces the whole momentum constraint.
  - The closing line is indefinite, (−6, 2, 2)α, and admits no positive
    kinetic term.
  - The walker sea's positive inertia takes the member off the line.
  - Walker content breaks exact closure at cubic order in the lapses'
    wavenumbers, and no local placement of its energy fixes that.
- **The 2026-09-14 tensor note:** the compact bound (k^3 with both
  constraints in the regular compact class).
- **Probes 10 and 11 of this PR.**

This note's T4 is the landed member programme restated as the gauge reading
of the owner's clock. It adds nothing new there beyond the re-verification
in check C.

Reference only, and re-derived nothing:
- Hořava (2009); Blas, Pujolas and Sibiryakov (2010): the non-projectable
  "healthy extension" with lapse-gradient terms and an extra scalar
  graviton;
- Jacobson's Einstein–aether and khronometric theories;
- Lieb and Robinson (1972);
- Page–Wootters and Barbour on relational time.

## Premises

- **Comparators.** The linearised Einstein–Hilbert (E-H) spatial form on
  symmetric tensors, as in probe 11. The Hamiltonian-constraint density is
  𝓗_1 = c·R_lin(h), with `R_lin = k.h.k − k^2 tr h`. The kinetic term is
  unit and positive where a speed is quoted.
- **Readings of the lapse n = N − 1:**
  - *physical*: a local operator on the records, or a field with a positive
    quadratic form, possibly with its own conjugate;
  - *auxiliary*: no conjugate, fixed by its own equation, with a quadratic
    term −α k^2 n^2;
  - *gauge*: a Lagrange multiplier, i.e. the Hamiltonian constraint.
- **Records as events:** probe 10's momentum-rule qubit moves as local
  generators `h_m = T_m + T_m^dag`.

## T1 — a physical record-event lapse is ordinary dynamics

**Statement.** Let N̂(x) be any local operator on finite-dimensional record
slots, such as the local rate of moves, and set
`H = sum_x (1/2){N̂(x), ĥ(x)}`. Then H is Hermitian, of finite range and
bounded, with ‖H‖ ≤ sum ‖N̂‖‖ĥ‖ per site. It has a ground state, so probe 11's
P1 holds.
- Under the momentum rule and cubic symmetry, probe 11 (check C2) gives
  v2 = 0 at order q^2. There is no first-order (compressible) helicity-2
  sum rule, so no compressible light-cone graviton.

**Proof.** Finite-dimensional local operators and finite range. ∎

## T2 — a physical lapse field lowers, never raises, the scalar block (check A)

**Statement.** On the transverse trace (δ − k̂k̂)/√2, the E-H form is
−(1/2)k^2. Add a lapse sector whose quadratic form W is positive, coupled
through 𝓗_1. The 2×2 block [[V_s, c R/2], [c R/2, W]] is indefinite for every
coupling c and every W > 0, since its determinant is V_s W − (cR/2)^2 < 0.
Eliminating a fast lapse (its Schur complement) gives
V_s − (cR/2)^2/W ≤ V_s.

**Check.** Over 2000 random couplings and positive stiffnesses the smallest
eigenvalue is always negative, and every Schur complement is at most the bare
value. ∎

## T3 — an instantaneous, negative-stiffness lapse: the Hořava route (check B)

**Statement.** Take the lapse terms `c n R_lin(h) − α k^2 n^2` with no
conjugate for n. At its stationary point n = cR/(2αk^2), which adds
`+c^2 R_lin^2/(4αk^2)`.
- **TT:** R_lin = 0, so unchanged, with speed^2 1 (unit kinetic).
- **Transverse trace:** `(−1/2 + c^2/(2α)) k^2`, positive iff α < c^2. It
  propagates with speed^2 = c^2/α − 1: 3, 1 and 0.111 at α = 0.25, 0.5 and
  0.9, and unstable at 1.2.
- **α → 0:** the speed diverges, the mode leaves the low-energy spectrum,
  and this is the constraint limit (GR).
- **Helicity 1 and the longitudinal direction:** zero, as gauge.
- **The kernel is non-analytic.** On a fixed tensor it is not a quadratic
  form in k: the least-squares residual is 0.32. The effective form
  therefore violates probe 11's identity: at α = 0.5,
  (v2, v1, v0) = (1/2, 0, 1/6) and 4v1 − v2 − 3v0 = −1. That is how this
  route evades the obstacle: through P3, not P1.
- **The price:**
  - an extra gapless helicity-0 graviton with its own speed;
  - a lapse with negative stiffness and no dynamics of its own, which is not
    a physical rate of anything. Its determination is instantaneous
    (non-local).

## T4 — a gauge lapse is Einstein's constraint (check C)

- With the scalar (Hamiltonian) constraint and the momentum constraint, the
  E-H comparator keeps exactly the two TT tensors, each at +1/2 k^2 (check
  C).
- This is the working mechanism.
- Its lattice form is landed:
  - block 112's closure holds exactly for every lapse pair only on the line
    β = −α, which takes (−6, 2, 2)α on the dilation, E and T strains
    (re-verified in check C). That line is indefinite and admits no positive
    kinetic term;
  - walker content breaks exact closure at cubic order (2026-09-25, T5);
  - in compact variables the scalar constraint forces k^3 (2026-09-14).

## T5 — records as events (check D)

**(a) Commuting events carry nothing.** If the local generators commute,
`e^{iHt} = ∏ e^{i h_x t}`. Every factor not overlapping a local operator A
commutes with A, so A(t) stays supported within one interaction range of A
for all t: zero propagation. Check D compares a pairwise-commuting cluster
chain, with |[A(t), B_far]| ≤ 7e-15 at t = 1, 5 and 20, against an XY chain,
with 0.71 at t = 5. ∎
- So "the order of record events never matters", taken literally, gives no
  waves and no graviton.

**(b) The momentum-rule moves do not commute.** Take probe 10's 20-slot move
and its translates within radius 2 that share slots with it. On configurations
built so that one move acts and then the other, 26 of 30 fail to commute
(first witness: shift (−2, 0, −1), one shared slot).
- So with these moves, the order of events matters, and so do the local
  rates. They are physical unless the moves are made first-class
  constraints of GR's kind. This note does not construct that; block 112
  and the 2026-09-25 note show what it costs for the member.

## What this means for the owner's reading

The reading "time is the shifting or creation of records" can give
Einstein's graviton only in its strictly relational form:
- Time is nothing but the order of record events.
- The rate of events relative to anything else has no physical meaning.
- The records' local generators are constraints that satisfy GR's
  hypersurface algebra weakly.

The other readings fail, or trade the problem for another:
- A physical event rate (T1, T2) cannot remove the negative scalar sector.
- A negative-stiffness instantaneous rate (T3) replaces it with an extra
  scalar graviton.
- Events whose order never matters (T5a) propagate nothing.

In the relational form, the lattice obstacles are those already found for
the member. Closure needs an indefinite kinetic term, it breaks exactly once
matter is added, and compact slots force k^3.

So the reading is consistent with Einstein's mechanism, but does not supply
it. What would have to be built:
- a record dynamics whose local event generators are first-class constraints
  closing weakly into the momentum rule;
- with collectively non-compact variables;
- and matter that keeps the closure beyond cubic order.

## No-Go Discipline Gate

The bounded negative claim: in the Gaussian comparator a physical lapse
(positive form) cannot make the scalar block positive; and in a local
bounded record dynamics a lapse that is a local operator leaves probe 11's
obstacle in force.

- **N1 — attack routes.**
  1. *A physical lapse with its own conjugate.* ATTEMPTED (check A): a
     positive form. The Hamiltonian stays indefinite (Schur).
  2. *A fast physical lapse* (eliminated). ATTEMPTED (check A): it lowers
     the scalar potential.
  3. *A lapse as a local operator.* ATTEMPTED (T1): an ordinary Hamiltonian,
     so probe 11 applies.
  4. *A negative-stiffness instantaneous lapse.* ATTEMPTED (check B). It
     works, with an extra scalar graviton. Outside the physical-lapse
     premise.
  5. *A gauge lapse.* RULED OUT BY PRIOR as a counterexample to the physical
     claim; it is GR's constraint, and its lattice form is landed (block
     112; the 2026-09-25 note).
  6. *Commuting events.* ATTEMPTED (check D(a)): no propagation.
  7. *Non-commuting qubit moves as constraints.* Not constructed. This is
     the open route.
- **N2 — conditions.** The walls are the physical/auxiliary/gauge
  classification (a premise distinction) and first-class closure for the
  qubit moves (open). Closing the qubit-move algebra would not make a
  physical rate work; the two are independent.
- **N3 — hidden conditions.** A, B and C are Gaussian comparators. A unit
  kinetic term is used for speeds. The E-H comparator itself is the landed
  continuum form.
- **N4 — residual matching.**
  - Block 112 and the 2026-09-25 note: the lattice gauge closure, used for
    T4. Match: yes.
  - The 2026-09-14 bound (k^3): match yes.
  - Probe 11 C2: T1. Match yes.
- **N5 — rhetoric audit.**
  - "Cannot remove" holds for every positive lapse form at the Gaussian
    level (per mode, tested), and for local-operator lapses via probe 11
    (lattice-wide, under its premises).
  - "Only a gauge lapse can": the auxiliary route also removes the negative
    sector, but adds a scalar graviton. The title's "can" means "can
    without an extra graviton".
- **N6 — partial closure.** No convention makes a physical rate gauge. The
  relational reading is a choice about what the axioms mean. It is the
  owner's to make, and not a derivation.
- **N7 — steelman.** A strongly interacting record dynamics might realise
  first-class constraints collectively, with non-compact collective
  variables, so that the qubit moves' non-commutation is absorbed weakly.
  That is route 7, open.
- **N8 — cross-cycle echo.** The member's clock algebra (landed) is the same
  wall, reached from the gauge side. No retirement mechanism applies.
- **Outcome:** PASS as scoped.

## What this does not show

It does not show any of these:
- a native record dynamics, or a first-class constraint algebra for the
  qubit moves;
- whether a strongly interacting record system can realise weak closure
  collectively;
- anything beyond the Gaussian comparators for T2–T4;
- matter coupling;
- which reading the axioms intend (the owner's decision).

## Independent checks

Pending.

## Reproduction

`python3 scripts/a_lapse_set_by_record_events_physical_auxiliary_or_gauge_2026_09_28.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in about 5 s. The canonical
cache is at
logs/runner-cache/a_lapse_set_by_record_events_physical_auxiliary_or_gauge_2026_09_28.txt.
