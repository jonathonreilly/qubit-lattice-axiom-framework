---
claim_id: a_quantum_link_time_constraint_on_the_tensor_complex_carries_the_dewitt_kinetic_term_exactly_but_the_potential_side_stays_soft_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied construction, not adopted, on the landed tensor complex (vector stencil G, scalar stencil S, 3^3 torus for the integer checks). Every slot is a spin S with E = S^z; for each site, T_y = prod (S^{sign s})^{|s|} over the landed scalar pattern s_y = S^T delta_y, and Y_y = i(T_y - T_y^dag). (A) T_y is nonzero iff S >= 2, because the pattern has entries of magnitude 4. G s_y = 0, so every T_y commutes exactly with the momentum-rule generators (operator identity checked on spin-2 slots, with a non-commuting control). exp(i beta Y_y) is a continuous finite-dimensional unitary moving S^z non-additively, so probe 13's trace lemma does not apply. (B) The DeWitt kinetic term DW(S^z) is exactly weakly invariant: DW(m + s_y) - DW(m) = 2 (G m).w_y with M s_y = G^T w_y and s_y.M.s_y = 0, so [DW, T_y] vanishes on the momentum sector. The six uniform components are conserved labels, and on ker G with them fixed DW is positive semidefinite (26 zeros on the 3^3 torus). (C) Near phi = 0, m = 0 the classical symbol of Y_y is -2 S^n (s_y.phi) + ..., the landed linear scalar constraint with h ~ phi, generating an additive shift of m along s_y there. (D) Classically the Y's commute with G and their brackets vanish on the joint constraint surface (non-abelian, closing with structure functions); quantum closure and the physical Hilbert space are not tested. (E) The potential side is not changed: with the momentum rule exact on S^z, every invariant potential is move-built and probe 10's sum rule (O(q^4)) applies, so a compressible graviton channel stays soft (omega ~ q^2). The momentum-rule gauge acts on the large-S metric proxy S^y/S non-additively, so an Einstein-Hilbert polynomial in it is not exactly invariant (an illustration, not a proof for all such polynomials). The Gaussian exponent check is illustrative. Not shown: quantum closure, physical states, a phase, a light-cone graviton, or any other encoding."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
runner: scripts/a_quantum_link_time_constraint_on_the_tensor_complex_2026_09_28.py
---

# A quantum-link time constraint on the tensor complex carries the DeWitt kinetic term exactly, but the potential side stays soft

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a supplied construction with exact operator and integer checks,
plus classical-symbol checks; unaudited. Independent checks are recorded
below.

## In one paragraph

Probe 13 found that on finite slots a continuous version of Einstein's time
constraint would have to act non-additively, the way quantum-link models
realise gauge symmetry. This probe builds it.

Make each tensor slot a spin S, and for each site take the product of
raising and lowering operators along the landed time-constraint pattern.
The imaginary part of that product then:
- generates a continuous symmetry;
- commutes exactly with the momentum rule;
- reduces at small fields to the landed linear time constraint.

Einstein's DeWitt kinetic term respects it exactly on the momentum-rule
states, and is non-negative there. So the kinetic-side obstruction of probes
12 and 13 is removed, but only for slots with at least five levels (spin ≥ 2),
not for one qubit per slot.

The potential side is not changed. With the momentum rule exact, every
allowed potential is built from moves, and probe 10's sum rule keeps a
compressible graviton soft. The obstruction has moved; it has not been
removed.

## Prior art

On main:
- the landed tensor complex, compact bound and oscillator note
  (2026-09-14 and 2026-09-24);
- the U(1) lane's spin-1/2 quantum links, which realise the Gauss law, not a
  time constraint;
- block 112 and the 2026-09-25 clock-profile note (closure on λ = 1).

Of this PR: probe 10 (sum rule), probe 13 (trace lemma, lifted clocks).

A search of main found no quantum-link tensor or Hamiltonian-constraint
construction.

External, reference only:
- Chandrasekharan and Wiese (hep-lat/9609042): quantum link models;
- Holstein–Primakoff.

## Premises (supplied)

- **Slots.** Each is a spin S with E = S^z, integer-spaced. The six slots per
  cell are the landed placement.
- **The momentum rule.** Exact: G S^z = 0 on the sector. Its generators
  G_row = Σ g S^z rotate the slots about z.
- **The time constraint.** For each site y, `T_y = ∏ (S^{sign s})^{|s|}` over
  s_y = S^T δ_y, and `Y_y = i(T_y − T_y^dag)`.
- **The kinetic term.** DW(S^z) = S^z · M · S^z, with the landed
  M = diag(1,1,1,2,2,2) − vv^T/2 per cell.

## A — the construction (check A)

- The scalar pattern's entries have magnitude 1 and 4. So T_y ≠ 0 iff
  (S^−)^4 ≠ 0, i.e. S ≥ 2. The norm of (S^−)^4 is 0 for S = 1/2, 1 and 3/2,
  and 24 for S = 2.
- G s_y = 0 for all 27 sites, so `[G_row, T_y] = (G_row · s_y) T_y = 0`. This
  is checked as an operator identity on 3 spin-2 slots (dimension 125), with
  a control where g·s ≠ 0.
- exp(iβY) is a continuous unitary. On one spin-2 slot it changes S^z by more
  than a multiple of the identity. The action is non-additive, as probe 13's
  trace lemma requires.

## B — DeWitt is exactly weakly invariant, and positive on the physical sector (check B)

- For every pattern, M s_y = G^T w_y and s_y · M · s_y = 0. Hence, as an
  exact identity for all integer m,
  `DW(m + s_y) − DW(m) = 2 (G m) · w_y`.
- Since T_y shifts S^z by exactly s_y,
  `[DW, T_y] = (DW(m + s_y) − DW(m)) T_y`, which vanishes on the momentum
  sector.
- The six uniform components have zero moment in every s_y, so they are
  conserved labels. The uniform dilation, whose DW value is negative, is a
  label and not a dynamical direction.
- On ker G (84-dimensional on the 3^3 torus) with the uniform parts removed
  (78 dimensions), DW is positive semidefinite, with 26 zeros.

## C — linearisation (check C)

- The classical symbol is `Y_y = −2 ∏(S^2 − m^2)^{|s|/2} sin(s_y · φ)`.
- At φ = 0, m = 0 its φ-gradient is −2 S^n s_y, with n = Σ|s| = 36, and its
  m-gradient is zero.
- So Y_y ≈ −2S^n (s_y · φ), the landed linear scalar constraint with h ∼ φ.
  There it generates an additive shift of m along s_y.

## D — classical closure (check D)

- {Y_a, Y_b} vanishes on the joint surface sin(s_a·φ) = sin(s_b·φ) = 0, to
  2e-16 normalised, and not off it (≥ 2.5e-3).
- So the algebra is non-abelian and closes with structure functions, as GR's
  does.
- {G, Y} = 0.
- Quantum closure (operator ordering) and the physical Hilbert space are not
  tested.

## E — the potential side stays soft (check E)

- With the momentum rule exact on S^z, every exactly invariant potential is
  built from moves (change patterns in ker G). Probe 10's sum rule then gives
  m1(E_q) ≤ C q^4 for these unit-spaced slots.
- The DeWitt kinetic term gives the electric channel a finite
  susceptibility. So by probe 10's T4 the lowest TT excitation has
  ω = O(q^2). The Gaussian exponent check (2.000) is only an illustration.
- The obvious polynomial proxy for the metric at large S, h = S^y/S, is moved
  non-additively by the momentum-rule gauge (z-rotations). A quadratic form
  in it changes at second order (illustrated). So an Einstein–Hilbert
  polynomial in that proxy is not exactly invariant; this is shown by
  example only.

## What this means

The time-constraint side of Einstein's structure can be built on finite
slots: spins of at least five levels, with a quantum-link action. The
obstruction of probes 12 and 13 on that side is removed.

What remains is the obstruction probe 10 found on the potential side. In
quantum-link encodings, the variable on which a constraint acts diagonally
(here S^z) can carry polynomial terms. Its conjugate cannot.
- Here the kinetic side is polynomial and the potential side is not.
- Swapping the roles would plausibly reverse them. That is a conjecture, not
  checked here.

The natural next tests:
1. the swapped assignment;
2. quantum closure and the physical Hilbert space of the Y constraints;
3. a large-S route in which both variables become approximately polynomial.

## No-Go Discipline Gate

The bounded negative claim: with the momentum rule exact on S^z, the graviton
channel's sum rule is O(q^4), so the construction's graviton is soft in any
compressible state.

- **N1 — attack routes.**
  1. *A polynomial Einstein–Hilbert potential in S^y/S.* ATTEMPTED (E,
     illustration): not exactly invariant.
  2. *Move-built potentials.* RULED OUT BY PRIOR (probe 10 T3, T4): O(q^4)
     sum rule.
  3. *Incompressible electric pattern.* Open; probe 10 / 11's route.
  4. *Swapped assignment.* Open (conjecture above).
  5. *Large S with approximate invariance.* Open.
- **N2 — conditions.** The positive results (A–D) and the negative one (E)
  have separate premises. E's premise is the exact momentum rule on S^z.
- **N3 — hidden conditions.**
  - S ≥ 2.
  - The 3^3 torus for the integer checks; the identities are local.
  - Classical symbols for C and D.
  - E's polynomial-proxy statement is an illustration, not a theorem.
- **N4 — residual matching.**
  - Probe 10's sum rule applies to unit-spaced diagonal slots. Match yes.
  - Probe 13's trace lemma is evaded by the non-additive action, as its own
    statement anticipates.
- **N5 — rhetoric audit.**
  - "Carries the DeWitt kinetic term exactly" is the weak invariance (B) as
    an operator identity on the sector.
  - "Stays soft" is conditional on a compressible channel (probe 10 T4).
- **N6 — partial closure.** None. The construction is supplied.
- **N7 — steelman.** The swapped or large-S assignments might make both sides
  polynomial enough, or an incompressible state might exist. All open.
- **N8 — cross-cycle echo.** The landed "both canonical variables must be
  non-compact" reappears in finite form: one quantum-link side is
  polynomial, the other is not.
- **Outcome:** PASS as scoped.

## Independent checks

Pending.

## Reproduction

`python3 scripts/a_quantum_link_time_constraint_on_the_tensor_complex_2026_09_28.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in under 1 s. The canonical
cache is at
logs/runner-cache/a_quantum_link_time_constraint_on_the_tensor_complex_2026_09_28.txt.
