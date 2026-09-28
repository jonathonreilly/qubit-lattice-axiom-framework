---
claim_id: the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_move_built_kinetic_terms_are_two_powers_of_q_below_einsteins_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied construction, not adopted, on the landed tensor complex: every slot is a spin S with the metric diagonal, h = S^z in the canonical slot coordinates. The scalar rule is an exact linear Gauss law on S^z; the momentum-rule (linearised diffeomorphism) gauge acts by quantum-link strings V_g along g = G^T delta, whose entries have magnitude 1, so any S >= 1/2 carries them. (A) The landed lattice Einstein-Hilbert form, assembled in real space on the 4^3 torus, obeys X G^T = 0 exactly, so X(S^z) commutes exactly with every V_g; the Gauss law commutes with every V_g. (B) Re-verification of the landed 2026-09-14 E-character bound on a 2^3 box: every finitely supported r with S r = 0 has vanishing zeroth moments; first moments span 8 dimensions (3 gauge, TT-invisible; 5 TT-visible); an 8-slot +-1 witness exists. (C) For Hamiltonians of diagonal terms and Gauss-law-compatible shift moves (fixed range, uniform norms, term-by-term sector-preserving), the double-commutator identity holds in every eigenstate, and in a ground state the TT metric f-sum obeys m1(q) <= C_K q^2, two powers of q below Einstein's O(1); with nonzero weight and finite m_-1, omega_min <= q sqrt(2 C_K / chi_h(q)). (D) In the specified harmonic comparators (integer box-kernel moves, U = 1), the swapped assignment and probe 14's assignment both give omega ~ q^2 on both TT modes (fitted exponents 2.00 +- 0.05 on axis, face, body and a generic direction); the non-compact DeWitt + E-H comparator gives omega = |K|. (E) At finite S (toys), overlapping gauge strings do not commute, and a monomial move sharing a slot with a gauge string does not commute with both V_g and V_g^dag; sums commuting with Y_g are not enumerated. (F) Re-verification of the landed 2026-09-14 'finite penalties' block (B_tt = -g k^2 + 2 V k^4): an energy penalty U (S h)^2 in place of the exact scalar law leaves E-H with a negative eigenvalue ~ -0.87 K^2 at small q for every finite U. Pre-registered primary outcome: FAIL (no move with a TT-visible zeroth moment). Not shown: a ground state, chi_h(q), quantum closure of the V strings, a phase, or any other encoding."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
runner: scripts/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.py
---

# The swapped quantum-link assignment (metric diagonal) makes Einstein–Hilbert exactly invariant, but move-built kinetic terms are two powers of q below Einstein's

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** supplied construction with exact integer and operator checks and
specified harmonic comparators; pre-registered; unaudited. Independent checks
are recorded below.

## In one paragraph

Probe 14 made the momentum the diagonal variable. Einstein's kinetic term
then came out exactly right, and the potential side was two powers of q too
weak. This probe swaps the roles: the metric is the diagonal variable.

Now Einstein's potential (the Einstein–Hilbert term) is exactly invariant,
and the time rule becomes an exact Gauss law of the ordinary kind. But the
kinetic side must now be built from moves that respect that Gauss law. Every
such move has zero net content, so the kinetic term is two powers of q
weaker than Einstein's.

In the simplest (harmonic) versions of both assignments the graviton's
frequency grows as q², not q. The obstruction moves; it does not go away.

## Pre-registration

Written in the probe's scratch file before check D was built:
- **PASS (route open):** some local move compatible with the scalar Gauss
  law has a TT-visible zeroth moment. Then the metric channel's f-sum would
  be O(1), Einstein's order.
- **FAIL (obstruction moves):** every such move has zero zeroth moment, so
  the f-sum is O(q²) or smaller.

The landed 2026-09-14 note already proves the zeroth-moment statement for
characters, so FAIL was expected. The new content is:
- the quantum-link construction on spin slots;
- the f-sum form of the bound;
- the TT visibility of first moments (so O(q²), not O(q⁴));
- the harmonic comparison of both assignments.

Check F (the soft scalar law) re-verifies a landed result; it is not new.

**Outcome: FAIL.**

## Prior art

On main:
- **The 2026-09-14 tensor note** ("Regular compact characters and derivative
  order"). Every invariant local E-character is O(k); every h-character is
  O(k²); with both compact all frequencies are O(k³). Its scope: lifted
  regular characters. Check B re-verifies the E-character statement on a
  box.
- **The 2026-09-14 note, "Finite penalties and the scalar Jordan chain".**
  Penalties U|G|² + V S² leave the scalar potential block −g k² + 2V k⁴,
  negative at small k for every finite V. Check F re-verifies this.
- **The 2026-09-24 oscillator note.** It supplies the lattice Einstein–Hilbert
  symbol used here and the non-compact comparator, ω² ∝ Σ sin²(k/2).

Of this PR:
- probe 10 (the sum-rule machinery and the ker G moment lemma);
- probe 14 (the momentum-diagonal assignment);
- the gravity-records panel, same family, whose lattice-gauge lens
  independently found the same exponent and an 8-slot ±1 move.

External, reference only:
- Chandrasekharan and Wiese (hep-lat/9609042): quantum links.
- Xu (2006), Gu and Wen, Xu and Hořava: soft gravitons in rotor models.
- Pretko (2017), and scalar-charge rank-2 U(1) models: linear modes by
  replacing the momentum rule with ∂_i∂_jE_ij = 0, with helicity partners
  (probe 11).

## Premises (supplied)

- **Slots.** Each is a spin S. The metric is h = S^z in the canonical slot
  coordinates q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz, 2h_xz).
- **The scalar rule.** C_y = (S S^z)_y, diagonal and linear: an exact Gauss
  law.
- **The momentum-rule gauge.** It shifts h along g = G^T δ. Its quantum-link
  strings are V_g = ∏ (S^{sign g})^{|g|}, with Y_g = i(V_g − V_g^dag).
- **Kinetic terms.** Shift monomials (with any diagonal prefactor) along
  patterns r with S r = 0, so that each commutes with the Gauss law.
- **Potential.** The landed lattice Einstein–Hilbert form X, as a
  polynomial in S^z.

## A — the construction (check A)

- The landed symbol is assembled into a real-space stencil: 75 entries, all
  real and in ½ℤ. On the 4³ torus X is symmetric, and
  max |X G^T| = 9e-16. It reproduces the symbol at a torus momentum.
- So X(m + g) = X(m) for every integer m and every gauge pattern. Hence
  [X(S^z), V_g] = 0: the invariance is strong, not only weak. This is checked
  for all 192 patterns.
- S G^T = 0 exactly, so the Gauss law commutes with every V_g.
- Gauge patterns have entries of magnitude 1, so V_g needs only S ≥ ½.

## B — the dual moment lemma (check B; re-verifies the 2026-09-14 bound)

On a box of 2³ cells, with the rule enforced at every site that touches the
box, the integer kernel of S has 14 generators.
- Every one has vanishing zeroth moments.
- Their first moments span 8 dimensions:
  - 3 are the gauge patterns, invisible in the TT channel;
  - 5 are TT-visible in every sampled direction (min-of-max 0.70). These are
    the lattice symmetric curls.
- A qubit-carriable witness exists: an 8-slot pattern with entries ±1,
  S r = 0 on the open lattice, zero zeroth moments and TT first moment √2.
  It was found by an integer program and is hard-coded in the runner.

## C — the dual sum rule (check C)

- For a shift monomial T along r and a diagonal observable A = a·S^z,
  `[[T + T^dag, A], A^dag] = |a·r|² (T + T^dag)`. This is checked on spin-½
  and spin-1 toys. It is probe 10's identity with the roles swapped, and
  diagonal prefactors do not change it.
- So a Hamiltonian of diagonal terms and Gauss-law-compatible moves has
  double commutators bounded by C_K Σ |w·r̂(q)|² in every eigenstate.
- By B, |w·r̂(q)| = O(q). So in a ground state the TT metric f-sum is
  `m1(q) ≤ C_K q²`, and the q² term is attained: max |w·r̂|²/q² = 3.45 on the
  box kernel.
- Einstein's canonical graviton has m1 = O(1), because its kinetic term
  π·M·π is ultralocal.
- With nonzero weight and finite m_−1, probe 10's chain gives
  `ω_min ≤ q √(2 C_K / χ_h(q))`.
  - If χ_h ≳ 1/q², which is the harmonic value set by the Einstein–Hilbert
    stiffness, then ω_min = O(q²).
  - A light-cone mode would need χ_h = O(1).

## D — harmonic comparators (check D)

Each comparator is reduced exactly to the two TT modes. The moves are the
integer box kernels, with U = 1.

| Model | Kinetic | Potential | Fitted exponent of ω in \|K\| |
| --- | --- | --- | --- |
| swapped (this probe) | moves in ker S (O(q²)) | Einstein–Hilbert (O(q²)) | 2.00 ± 0.001 |
| probe 14's assignment | DeWitt (O(1)) | moves in ker G (O(q⁴)) | 2.00 ± 0.001 |
| non-compact comparator | DeWitt (O(1)) | Einstein–Hilbert (O(q²)) | 1.000, with ω = \|K\| |

Directions: axis, face diagonal, body diagonal and a generic one, at
|k| = 0.2 … 0.025. In both finite-slot assignments the product of the two
orders is q⁴, against Einstein's q².

## E — the gauge side at finite S (check E, toys)

- Gauge strings that overlap with opposite signs do not commute, although
  linearised diffeomorphisms do.
- A monomial move sharing a slot with a gauge string fails to commute with
  V_g or with V_g^dag.
- A diagonal form invariant under the shift commutes exactly.

So monomial kinetic moves are invariant under both V_g and V_g^dag only
where they avoid the gauge supports, or in the rotor limit. Sums of
monomials commuting with Y_g are not enumerated.

## F — a soft scalar law does not rescue it (check F; re-verifies the landed penalty block)

If the scalar law were only an energy penalty U (S h)², single-slot moves
would be allowed, and the kinetic term could be O(1).
- But Einstein–Hilbert has a negative scalar (conformal) block of order q²,
  and the penalty is of order U q⁴.
- For every finite U, X + U SᵀS has a negative eigenvalue −0.87 K² below
  |q| ~ 10⁻² / √U.
- This is the landed 2026-09-14 penalty block, B_tt = −g k² + 2V k⁴,
  checked here in the swapped setting. It mirrors probe 13's statement for
  the DeWitt form.

## What this means

On finite slots with exact rules, one canonical variable is diagonal and
polynomial, and the other side is built from moves in the kernel of the
diagonal rule.
- Momentum diagonal (probe 14): the potential is q² weaker than Einstein's.
- Metric diagonal (this probe): the kinetic term is q² weaker than
  Einstein's.

In the harmonic comparators both give ω ∝ q². This is the finite-slot form
of the landed "both canonical variables must be non-compact".

Three routes remain; this probe does not close them:
- a strongly correlated state with χ_h(q) = O(1);
- a graviton not carried by S^z (composite);
- non-compact (oscillator) slots, which is a change to the finite local
  dimension, not a construction inside it.

Six spin slots per cell also test finite local dimension, not the axioms'
one qubit per site.

## No-Go Discipline Gate

The bounded negative claims, inside the premises:
- (a) Gauss-law-compatible moves have zero zeroth moments, so the TT metric
  f-sum is ≤ C_K q² in a ground state, with the conditional ω_min bound;
- (b) in the harmonic comparators both assignments give ω ∝ q²;
- (c) a soft scalar law leaves a long-wavelength negative mode.

- **N1 — attack routes.** Six distinct routes.
  1. *A Gauss-law-compatible move with a nonzero zeroth moment.* ATTEMPTED
     (B): the integer box kernel. The leading symbol of S has six linearly
     independent quadratic components, so no finite pattern escapes. The
     route fails.
  2. *Diagonal prefactors or larger spins changing the double commutator.*
     ATTEMPTED (C): the identity holds for spin ½ and 1 with any diagonal
     prefactor. The route fails.
  3. *A soft scalar law.* RULED OUT BY PRIOR, via the landed 2026-09-14
     penalty block, which is unaudited and so a parent, not a retained
     authority. F re-checks it here: long-wavelength instability for every
     finite U. The route fails.
  4. *Moves whose first moments are all TT-invisible, so the bound would be
     q⁴ and a different structure.* ATTEMPTED (B): 5 TT-visible directions
     and a ±1 witness. This does not weaken (a); it shows the bound is
     attained.
  5. *The rotor (S → ∞) limit.* ATTEMPTED (argument). With compact φ, the
     moves are characters e^{ir·φ} with S r = 0. The landed O(k) bound
     applies to them unchanged, so the order is the same.
  6. *Non-compact φ (oscillator slots).* ATTEMPTED (D, third row): ω = |K|.
     This escapes the finite-slot premise. It is the axiom-change route, not
     a counterexample inside the domain.

  **Open routes (consistent with the claims):**
  - (i) χ_h(q) = O(1) in some ground state;
  - (ii) a composite or non-diagonal metric;
  - (iii) sums of monomials commuting with Y_g (the commutant);
  - (iv) the large-S emergent route with approximate gauge invariance (the
    panel's T4).
- **N2 — pairwise table.**
  - W1: finite S, unit-spaced S^z.
  - W2: the exact scalar Gauss law, term by term.
  - W3: fixed range and uniform norms.
  - W4 (state): a ground state with nonzero weight and finite m_−1, and
    χ_h ≳ 1/q² for softness.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no | no: exact laws act on rotors | independent |
  | W1, W3 | no | no | independent |
  | W1, W4 | no | no | independent |
  | W2, W3 | no | no | independent |
  | W2, W4 | no | unresolved: whether an exact-law ground state can have χ_h = O(1) is open route (i) | unresolved |
  | W3, W4 | no | no | independent |

  The collapsed set is W1–W3 (domain) and W4 (state).
- **N3 — hidden conditions.** All now explicit:
  - box sizes (2³ for S, 3³ for G);
  - the harmonic comparators are specified models (integer box kernels,
    U = 1); their exponents illustrate (a), and (a) does not rest on them;
  - the TT reduction uses the lattice K̂, which is exact because TT(K) lies
    in ker S(q).
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual claimed closed here | Match |
  | --- | --- | --- | --- |
  | 2026-09-14 note (docs/LOCAL_FINITE_CLOCK_TENSOR_..._2026-09-14.md):186 | an invariant E-character with nonzero zeroth moment | none; B re-verifies it on spin slots | yes |
  | 2026-09-24 note (docs/TENSOR_LINEAR_DISPERSION_..._2026-09-24.md):36 | the lattice E-H symbol and the non-compact comparator | none; A assembles and checks X | yes |
  | probe 10 note (docs/ONE_QUBIT_PER_SLOT_..._2026-09-28.md):150, 186 | the double-commutator identity and the chain | (a)'s form, with roles swapped | yes: C re-checks the identity |

  All three are unaudited, so they are cited as parents, not as retained
  authorities.
- **N5 — rhetoric audit.**
  - "Two powers of q below Einstein's" means the TT metric f-sum O(q²)
    against O(1).
  - "The obstruction moves" means the harmonic comparators.
  - The certificate lines are in the runner output.
- **N6 — partial closure.** None. No primitive is invoked.
- **N7 — steelman.** A strongly correlated Gauss-law state could have a
  bounded χ_h and a linear TT mode, with its long-range static metric
  response carried by something other than the Einstein–Hilbert stiffness.
  Or the physical metric could be a composite of the S^z records. Both are
  open and would need a model; neither is refuted here.
- **N8 — cross-cycle echo.**
  - **Probe 10's potential-side wall:** mirrored here, not retired.
  - **The landed O(k³) wall** (both sides compact): not retired. This probe
    sits between it and the comparator; with one side polynomial the order
    is k².
  - **The landed "both non-compact" wall:** reaffirmed in finite form.
  - **The U(1) photon's retirement mechanism** (an ultralocal electric
    stiffness): it does not transfer. The exact scalar law forbids an
    ultralocal kinetic term (B), and softening the law destabilises the
    conformal mode (F).
- **Outcome:** PASS as scoped. The pre-registered primary outcome is FAIL,
  and open routes (i)–(iv) remain.

## Independent checks

Pending.

## Reproduction

`python3 scripts/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.py`
prints 6 checks, A–F, the N5 lines and TOTAL, in about 2 s. The canonical
cache is at
logs/runner-cache/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.txt.
