---
claim_id: a_quantum_link_deformation_of_the_linear_scalar_constraint_on_tensor_slots_of_spin_at_least_two_keeps_the_dewitt_kinetic_term_weakly_invariant_but_is_not_first_class_on_its_whole_constraint_surface_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied construction, not adopted, on the landed tensor complex (vector stencil G, scalar stencil S; 3^3 torus for the integer checks). Every slot is a spin S with E = S^z. For each site, T_y = prod (S^{sign s})^{|s|} over the landed scalar pattern s_y = S^T delta_y, and Y_y = i(T_y - T_y^dag). Y_y is a quantum-link deformation of the LINEAR scalar constraint (linearised R). It is not an ADM Hamiltonian constraint: it contains no DeWitt term, and no lapse or {H[N], H[M]} algebra is built. (A) T_y != 0 iff S >= 2 (pattern entries of magnitude 4). [G_row, T_y] = 0 exactly (G s_y = 0). exp(i beta Y_y) is a continuous finite-dimensional unitary moving S^z non-additively, so probe 13's trace lemma does not apply. (B) DW(m + s_y) - DW(m) = 2 (G m).w_y exactly (M s_y = G^T w_y, s_y.M.s_y = 0), so [DW, T_y] = T_y Delta_y(S^z) vanishes on the momentum sector. The six uniform components are conserved by every T_y and every finitely supported move; this is a superselection choice for these local operators, not implied by the momentum rule. In each fixed-label sector DW = const + a positive semidefinite form on ker G (26 zeros on the 3^3 torus); on all of ker G it is indefinite. (C) The principal classical (large-S) symbol at phi = 0, m = 0 is Y_y ~ -2 S^36 (s_y.phi), the landed linear constraint with the canonical slot vector q proportional to phi; not an exact finite-S identity. (D) Classically {Y_a, Y_b} vanishes on the regular branch (all spins interior), with structure functions singular at the poles. It does not close on the whole constraint surface: an explicit witness at a pole-stratum point of the 3^3 torus has G m = 0, every Y_c = 0 and {Y_0, Y_1} != 0. So the algebra is not first class on the whole surface; the pole strata are not classified. Quantum closure and physical states are not tested. (E) Probe 10's premises hold for Hamiltonians built from T_y, moves and diagonal terms (fixed range, uniformly bounded, term-by-term sector-preserving): every s_y has vanishing zeroth and first moments. So the double-commutator bound holds in every eigenstate; in a ground state with nonzero weight and finite m_-1, m1 <= C q^4 in the electric channel and omega_min <= q^2 sqrt(2 C_H / chi(q)). Softness needs chi bounded below, which is not established. Not shown: a Hamiltonian constraint, quantum closure, physical states, a phase, a light-cone graviton, or any other encoding."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
runner: scripts/a_quantum_link_deformation_of_the_linear_scalar_constraint_on_tensor_slots_of_spin_at_least_two_2026_09_28.py
---

# A quantum-link deformation of the linear scalar constraint on tensor slots of spin ≥ 2 keeps the DeWitt kinetic term weakly invariant but is not first class on its whole constraint surface

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a supplied construction with exact operator and integer checks,
classical-symbol checks and one explicit counterexample; unaudited. Revised
after the first referee's FAILS verdict; independent checks are recorded
below.

## In one paragraph

Probe 13 found that on finite slots a continuous version of Einstein's time
constraint would have to act non-additively, as in quantum-link models. This
probe builds the simplest candidate.

Make each tensor slot a spin S. For each site, multiply raising and lowering
operators along the landed pattern of the linear time (scalar) constraint,
and take the imaginary part. The result:
- generates a continuous symmetry;
- commutes exactly with the momentum rule;
- reduces, at small fields and large spin, to the landed linear constraint.

Einstein's DeWitt kinetic term respects this symmetry exactly on the
momentum-rule states. It is non-negative there once six conserved uniform
labels are fixed.

Three limits:
- It needs slots with at least five levels (spin ≥ 2), not one qubit.
- It is a deformation of the linear constraint, not Einstein's full time
  constraint.
- Its classical algebra closes where no spin sits at an end of its range,
  but not everywhere its constraints hold. Check D gives an explicit point
  where a shared spin sits at an end: all constraints vanish there, and two
  of them do not close.

On the potential side nothing changes. Hamiltonians built from these
operators still obey probe 10's sum rule. So in any compressible ground
state (with nonzero weight in the channel) the lowest such mode is soft.

## Prior art

On main:
- the landed tensor complex, compact bound and oscillator note (2026-09-14,
  2026-09-24);
- the U(1) lane's spin-1/2 quantum links, which realise a linear Gauss law,
  not a time constraint;
- block 112 and the 2026-09-25 clock-profile note (closure on λ = 1).

Of this PR: probe 10 (sum rule), probe 13 (trace lemma, lifted clocks).

A search of main found no quantum-link tensor or Hamiltonian-constraint
construction.

External, reference only. None of these is this fixed-spin construction, so
no novelty is claimed beyond the specific operators.
- Chandrasekharan and Wiese (hep-lat/9609042): quantum link models.
- Thiemann (gr-qc/9606089): a Hamiltonian constraint on spin networks, whose
  algebra closes only on a restricted space of states.
- Bonzom and Freidel (arXiv:1101.3524): a discrete 3D Hamiltonian
  constraint.
- Gu and Wen (gr-qc/0606100, arXiv:0907.1203), Xu and Hořava
  (arXiv:1003.0009): lattice spin and boson graviton models.

A limited search found no published quantum-link realisation of the 4D
ADM/DeWitt constraint; that is not an absence theorem.

## Premises (supplied)

- **Slots.** Each is a spin S with E = S^z, integer-spaced, in the landed
  placement (six slots per cell).
- **The momentum rule.** Exact, G S^z = 0 on the sector. Its generators
  G_row = Σ g S^z rotate the slots about z.
- **The scalar operators.** For each site y:
  - `T_y = ∏ (S^{sign s})^{|s|}` over s_y = S^T δ_y;
  - `Y_y = i(T_y − T_y^dag)`.
- **The kinetic term.** DW(S^z) = S^z · M · S^z, with the landed
  M = diag(1,1,1,2,2,2) − vv^T/2 per cell.

## A — the construction (check A)

- The scalar pattern's entries have magnitude 1 and 4. So T_y ≠ 0 iff
  (S^−)^4 ≠ 0, i.e. S ≥ 2.
- G s_y = 0 for all 27 sites, so `[G_row, T_y] = (G_row · s_y) T_y = 0`.
  This is checked as an operator identity on 3 spin-2 slots, with a
  non-commuting control.
- The ordering identity `[f(S^z), T] = T (f(S^z + s) − f(S^z))` is checked
  on the same slots for a random quadratic f.
- exp(iβY) is a continuous unitary. On one spin-2 slot it changes S^z by
  more than a multiple of the identity (non-additive).

## B — DeWitt is exactly weakly invariant; positive in each label sector (check B)

- For every pattern, M s_y = G^T w_y and s_y · M · s_y = 0. So, exactly for
  all integer m, `DW(m + s_y) − DW(m) = 2 (G m) · w_y ≡ Δ_y(m)`.
- Hence `[DW, T_y] = T_y Δ_y(S^z)`. It vanishes on the momentum sector,
  which T_y preserves (G s_y = 0). States that T_y annihilates cause no
  exception.
- **Uniform labels.**
  - The six uniform components have zero sum in every s_y, and in every
    finitely supported move (probe 10 T2), so every T_y and every local move
    conserves them.
  - Fixing them is a superselection choice for these local operators. The
    momentum rule does not imply it.
- **Positivity.**
  - DW(u + r) = DW(u) + DW(r) for u uniform and r with zero uniform part
    (no cross term, checked). So in each sector DW is a constant plus a form
    on the non-uniform part of ker G.
  - That form is positive semidefinite: 78 dimensions on the 3^3 torus, 26
    zeros.
  - On all of ker G, DW is indefinite: the uniform dilation has value −0.5.

## C — linearisation (check C)

- The classical symbol is `Y_y = −2 ∏(S^2 − m^2)^{|s|/2} sin(s_y · φ)`.
- At φ = 0, m = 0 its φ-gradient is −2 S^n s_y, with n = Σ|s| = 36, and its
  m-gradient is zero.
- So `Y_y / (−2S^n) ≈ s_y · φ`. This is the landed linear scalar constraint
  S q with the canonical slot vector q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz,
  2h_xz) ∝ φ. There it generates an additive shift of m along s_y.
- This is a principal classical (large-S) symbol, not an exact finite-S
  identity.

## D — classical closure holds on the regular branch, not on the whole surface (check D)

- **D1, regular branch** (every spin interior, amplitudes nonzero).
  - {Y_a, Y_b} carries factors sin(s·φ). It vanishes on sin(s_a·φ) =
    sin(s_b·φ) = 0 (to 3e-16 normalised) and not off it.
  - This is closure with structure functions, which are singular where an
    amplitude vanishes.
  - {G, Y} = 0.
- **D2, pole strata** (the witness).
  - Slot 4 is shared by patterns 0 and 1 with coefficients −1 and +1. Put it
    at its pole (m = S).
  - Choose m in ker G with every other |m| ≤ 0.2 S (by a linear program).
  - Choose phases with sin(s_c·φ) = 0 for every pattern that does not touch
    slot 4. The four patterns that do touch it vanish by amplitude.
  - Then G m = 0 and every Y_c = 0 (to 6e-15 of S^36).
  - Yet {Y_0, Y_1}/S^71 = −1.145, from the Lie–Poisson bracket on the
    spheres. The implementation is cross-checked against the canonical
    (φ, m) bracket at a regular point.
- So the Y algebra is not first class on the whole constraint surface. At
  the witness point no smooth combination of the constraints equals the
  bracket, since all of them vanish and it does not. This is one explicit
  pole-stratum point; the pole strata are not classified.
- Quantum closure (operator ordering, the joint kernel) is not tested.
  Whether it over-constrains the extreme-weight states is open.

## E — probe 10's premises hold; softness is conditional (check E)

- Every s_y is a finitely supported pattern in ker G, with vanishing zeroth
  and first moments (second moments nonzero). So |ŝ(q)| = O(q²), with
  |ŝ(q)|/q² between 1.29 and 1.41 over 40 directions.
- Take a Hamiltonian built from T_y, moves and diagonal terms, with fixed
  range, uniformly bounded norms and term-by-term sector preservation. It
  meets probe 10's premises. So probe 10's double-commutator bound holds
  in every eigenstate, and in a ground state the electric channel's f-sum
  is m1(q) ≤ C_H q^4.
- By probe 10's T4, in a ground state with nonzero weight in the channel
  and finite m_−1, the lowest electrically weighted state has
  `ω_min ≤ q² √(2 C_H / χ(q))`.
- ω_min = O(q²) (soft) follows only if χ(q) is bounded below (a
  compressible state). The DeWitt term does not establish that, and nothing
  here shows the lowest weighted state is a transverse-traceless graviton.

The first version's two illustrations are withdrawn:
- a quadratic form under a uniform z-rotation, which is not a G-row gauge
  transformation or an Einstein–Hilbert polynomial;
- a Gaussian exponent fit, which was tautological.

## What this means

On finite slots, a continuous, non-additive deformation of the linear scalar
constraint can be built. It commutes with the momentum rule and keeps
Einstein's kinetic term weakly invariant. This removes probe 13's
kinetic-side objection for spins of at least 2.

It does not give Einstein's time constraint:
- its classical algebra is not first class on its whole constraint surface
  (an explicit pole-stratum point);
- no lapse algebra is built;
- the potential side is still bound by probe 10's sum rule.

A conjecture, not checked here: in quantum-link encodings the variable on
which a constraint acts diagonally can carry polynomial terms, and its
conjugate cannot.

Next tests:
1. the swapped assignment (the metric diagonal);
2. quantum closure and the joint kernel of the Y's, including extreme-weight
   states;
3. a large-S route in which both variables become approximately polynomial.

## No-Go Discipline Gate

The bounded negative claims, both inside the premises above:
- (a) the classical Y algebra is not first class on the whole constraint
  surface (an existence witness);
- (b) Hamiltonians built from these operators obey
  ω_min ≤ q² √(2 C_H / χ(q)) (probe 10 applied).

- **N1 — attack routes against (a) and (b).** Six distinct routes. Each was
  attempted here or is closed by a parent.
  1. *Exclude the poles from phase space (regular branch only).* ATTEMPTED
     (D2). The pole points satisfy every constraint of the stated
     construction. Removing them changes the phase space, and the flows of
     the momentum-rule and scalar gauges pass through them. The route
     changes the premises; it is not a repair inside them.
  2. *Smooth structure functions.* ATTEMPTED (D2). At the witness every
     constraint vanishes and the bracket does not. So no identity
     {Y_a, Y_b} = Σ C_c Y_c + Σ D·(G m) with finite coefficients can hold
     there. The route fails.
  3. *Include the momentum constraints in the ideal.* ATTEMPTED (D2): G m = 0
     at the witness as well. The route fails.
  4. *A different operator ordering.* ATTEMPTED. The witness is classical,
     so it is independent of any ordering with the same principal symbol.
     The route fails for (a). Quantum closure stays open.
  5. *Y-built terms that escape the sum rule.* ATTEMPTED (E). Every s_y has
     vanishing zeroth and first moments, so its terms obey probe 10's T2/T3.
     The route fails.
  6. *Large S with couplings scaled with S.* ATTEMPTED (argument here). The
     norm of each T_y grows like S^36, so C_H is uniform only at fixed S.
     Letting S → ∞ leaves the fixed-S domain, which is where W1 sits. The
     route escapes the premises; it is not a counterexample inside them.

  **Open routes the claims leave.** These are consistent with them, not
  attacks on them.
  - (i) An incompressible state, with χ(q) = O(q²).
  - (ii) The swapped assignment.
  - (iii) A quantum joint kernel that avoids the pole strata. This would be
    a habitat restriction, as in Thiemann's construction.
  - (iv) A different non-additive scalar constraint.
- **N2 — pairwise table.** Four domain walls and one state condition.
  - W1: fixed finite S ≥ 2.
  - W2: the exact momentum rule, term by term, on S^z.
  - W3: the product form of Y along s_y.
  - W4: fixed range and uniform norms.
  - W5 (state): a ground state with nonzero weight in the channel, finite
    m_−1, and χ(q) ≥ χ_0 > 0. It is used only in (b)'s softness step.

  (a) uses W1 and W3. (b)'s bound uses W1, W2 and W4, and its softness step
  adds W5.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: finite spin allows soft rules | no: exact rules act on rotors | independent |
  | W1, W3 | no | no: products of S^± exist at any S but vanish for S < 2 | independent (W3 is non-trivial only with S ≥ 2) |
  | W1, W4 | no | no | independent |
  | W1, W5 | no: finite spin says nothing about χ | no | independent |
  | W2, W3 | no | yes: G s_y = 0 makes each T_y rule-preserving | W3 is compatible with W2; it does not imply W2 for other terms |
  | W2, W4 | no | no | independent |
  | W2, W5 | no | unresolved: whether an exact-rule ground state can have χ → 0 is probe 10's open route (a) | unresolved |
  | W3, W4 | no | no | independent |
  | W3, W5 | no | no | independent |
  | W4, W5 | no: bounded terms do not fix χ | no | independent |

  The collapsed set is W1, W2, W4, and W3 as the construction; W5 is a
  property of a state, and none of W1–W4 is shown to imply it.
- **N3 — hidden conditions.** Now explicit:
  - S ≥ 2;
  - the 3^3 torus for the integer checks and the witness (the identities
    and the witness are local);
  - classical symbols for C and D;
  - the superselection of uniform labels for B's positivity;
  - χ bounded below for softness.
- **N4 — residual matching.**

  | Citation (path:line) | Residual the witness attacks | Residual claimed closed here | Match |
  | --- | --- | --- | --- |
  | probe 10 note (docs/ONE_QUBIT_PER_SLOT_..._2026-09-28.md):134 (T2) | nonzero low moments of kernel moves | none; E re-checks the moments of s_y directly | yes |
  | same:150 (T3) | an f-sum growing faster than q^4 | (b)'s bound, for Hamiltonians meeting its premises | yes: premises checked in E |
  | same:186 (T4) | a ground-state chain without weight or finite m_−1 | (b)'s conditional ω_min | yes: W5 stated |
  | probe 13 note (docs/THE_LAMBDA_ONE_QUESTION_..._2026-09-28.md):159 (E, trace lemma) | an additive finite-slot scalar gauge | none; A shows non-additivity evades it | yes |
  | 2026-09-24 oscillator note (docs/TENSOR_LINEAR_DISPERSION_..._2026-09-24.md):36 | the non-compact comparator | none; cited only for context in N8 | yes |

  Probe 10 and probe 13 are unaudited notes of this PR; they are cited as
  parents, not as retained authorities.
- **N5 — rhetoric audit.**
  - "Keeps DeWitt weakly invariant" means B's operator identity on the
    momentum sector.
  - "Positive" holds in fixed-label sectors only.
  - "Not first class on its whole constraint surface" rests on one explicit
    pole-stratum witness; the pole strata are not classified.
  - "Soft" is conditional on χ. The certificate lines are in the runner
    output.
- **N6 — partial closure.** The pole strata might be removed by a reframing:
  restricting to states with every spin interior. This is route (iii) and
  untested. No primitive is invoked.
- **N7 — steelman.** Quantum mechanically, T_y annihilates extreme-weight
  states. So the joint kernel of the Y's may be a large, consistent space,
  whatever the classical pole strata do, in the way loop quantum gravity's
  constraint closes on its habitat. And a different non-additive scalar
  operator might avoid pole strata altogether. Both are open. They are the
  natural next tests, not refutations of (a) or (b).
- **N8 — cross-cycle echo.**
  - **The landed "both canonical variables must be non-compact" wall**
    (2026-09-24). Not retired. This construction leaves the potential side
    compact, and E's bound is its finite form.
  - **The U(1) lane's quantum-link Gauss law.** It is first class because it
    is linear in E. That mechanism does not transfer: probe 13's trace lemma
    forces a non-additive scalar constraint, and non-additivity is what
    creates the pole strata.
  - **Probe 13's lifted-clock wall.** Retired here for spin ≥ 2 by
    non-additivity, the mechanism its own statement named.
- **Outcome:** PASS as scoped, with (b) conditional on its parent, probe 10,
  which is unaudited. The negative content is a witness, (a), and a
  conditional corollary, (b). Open routes (i)–(iv) remain.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** Its findings, and how
  this version answers each:
  1. **Classical closure fails on pole strata** (critical). Confirmed and
     now check D2.
  2. **Y is not an ADM time constraint carrying DeWitt** (critical).
     Retitled as a deformation of the linear scalar constraint.
  3. **E overclaimed ω ~ q²** (high). Now the conditional ω_min bound.
  4. **Positivity holds only at fixed uniform labels; operator ordering**
     (high). Both corrected.
  5. **C is a principal symbol** (medium). Scoped as such, with its
     normalisation.
  6. **The illustrations were not evidence** (medium). Withdrawn and
     replaced by the moment check.
  7. **The gate did not follow its rules** (medium). Rewritten.
  8. **Prior art** (medium). Added.
- **gpt-5.6-sol, second round: STANDS WITH CORRECTIONS.** Findings 1, 2, 4,
  5, 6 and 8 resolved. It rebuilt the witness independently (another phase
  choice, {Y_0, Y_1}/S^71 = −0.388). Three corrections, applied here:
  - the m1 bound and the ω_min chain need a ground state with nonzero
    weight and finite m_−1;
  - the gate's N1 route 6, N2 (χ and the state hypotheses) and N4
    (path:line, witnessed versus claimed residuals);
  - "pole strata are second class" narrowed to one explicit pole-stratum
    point, with the title changed to "not first class on its whole
    constraint surface".
- Fable check: pending.

## Reproduction

`python3 scripts/a_quantum_link_deformation_of_the_linear_scalar_constraint_on_tensor_slots_of_spin_at_least_two_2026_09_28.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in under 1 s. The canonical
cache is at
logs/runner-cache/a_quantum_link_deformation_of_the_linear_scalar_constraint_on_tensor_slots_of_spin_at_least_two_2026_09_28.txt.
