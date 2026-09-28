---
claim_id: the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied construction, not adopted, on the landed tensor complex: every slot is a spin S with the metric diagonal, h = S^z in the canonical slot coordinates. The scalar rule is an exact linear Gauss law on S^z; the momentum-rule (linearised diffeomorphism) gauge acts by quantum-link strings V_g along g = G^T delta, whose entries have magnitude 1, so any S >= 1/2 carries them. (A) The landed lattice Einstein-Hilbert form, assembled in real space on the 4^3 torus, obeys X G^T = 0 exactly, so X(S^z) commutes exactly with every V_g; the Gauss law commutes with every V_g. (B) Re-verification of the landed 2026-09-14 E-character bound on a 2^3 box: every finitely supported r with S r = 0 has vanishing zeroth moments; first moments span 8 dimensions (3 gauge, TT-invisible; 5 TT-visible); an 8-slot +-1 witness exists. (C) For Hamiltonians of diagonal terms and Gauss-law-compatible shift moves (fixed range, uniform norms, term-by-term sector-preserving), the double-commutator identity holds in every eigenstate, and in a ground state the TT metric f-sum obeys m1(q) <= C_K q^2, two powers of q below the normalised non-compact DeWitt comparator's O(1); the box-kernel moves' kinematic form factor is of order q^2 (a form factor, not a ground-state expectation); with nonzero weight and finite m_-1, omega_min <= q sqrt(2 C_K / chi_h(q)). (D) In the specified harmonic comparators (integer box-kernel moves, U = 1), the swapped assignment and probe 14's assignment both give omega ~ q^2 on both TT modes (fitted exponents 2.00 +- 0.05 on axis, face, body and a generic direction); the non-compact DeWitt + E-H comparator gives omega = |K|. (E) At finite S the deformed momentum-rule strings do not commute among themselves; whether kinetic moves commute with them depends on S and the overlap (at spin 1/2 an overlapping 8-slot move commutes with V_g and V_g^dag by nilpotency); the commutant of the Y_g is not enumerated. (F) Re-verification of the landed 2026-09-14 'finite penalties' block: an energy penalty U (S h)^2 in place of the exact scalar law leaves E-H with a negative eigenvalue -c(n) K^2 + O(U K^4) for every finite U (c = 1, sqrt(3)/2, 5/6 on axis, face and body directions). Pre-registered primary outcome: FAIL (no move with a TT-visible zeroth moment), which the landed parent already implied. Not claimed: that the swapped assignment has no light-cone graviton; not shown: a ground state, chi_h(q), quantum closure of the V strings, a phase, or any other encoding."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - a_quantum_link_deformation_of_the_linear_scalar_constraint_on_tensor_slots_of_spin_at_least_two_keeps_the_dewitt_kinetic_term_weakly_invariant_but_its_classical_algebra_is_not_first_class_on_the_whole_constraint_surface_bounded_theorem_note_2026-09-28
runner: scripts/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.py
---

# The swapped quantum-link assignment (metric diagonal) makes Einstein–Hilbert exactly invariant, but the TT metric f-sum of Gauss-law-compatible moves is bounded by q²

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a supplied construction with exact integer and operator checks and
specified harmonic comparators; pre-registered; unaudited. Revised after the
first referee's FAILS verdict. Independent checks are recorded below.

## In one paragraph

Probe 14 made the momentum the diagonal variable. Einstein's kinetic term
then came out exactly right, and the potential side was bounded two powers
of q below the comparator's. This probe swaps the roles: the metric is the
diagonal variable.

Now Einstein's potential (the Einstein–Hilbert term) is exactly invariant,
and the time rule becomes an exact Gauss law of the ordinary kind. But
kinetic terms built from moves that respect that Gauss law have zero net
content. So the metric channel's f-sum, a bound on how strongly the kinetic
side can move the metric at long wavelength, is two powers of q below the
non-compact comparator's.

In the simplest (harmonic) version of each assignment the graviton's
frequency grows as q², not q. This note does not claim that no light-cone
graviton exists in the swapped assignment. A strongly correlated state, a
composite metric, and other routes stay open (see the gate).

## Pre-registration

Written in the probe's scratch file before check D was built:
- **PASS (route open):** some local move compatible with the scalar Gauss
  law has a TT-visible zeroth moment. Then the metric channel's f-sum would
  be O(1), the comparator's order.
- **FAIL:** every such move has zero zeroth moment, so the f-sum is O(q²) or
  smaller.

The landed 2026-09-14 note already proves the zeroth-moment statement for
characters. So the pre-registration fixes how the outcome is read; it adds
no independent support.

**Outcome: FAIL.** The new content is:
- the quantum-link construction on spin slots;
- the f-sum form of the bound;
- the TT visibility of first moments (O(q²), not O(q⁴));
- the harmonic comparison of both assignments.

## Prior art

On main:
- **The 2026-09-14 tensor note, "Regular compact characters and derivative
  order."** Every invariant local E-character is O(k); every h-character is
  O(k²); with both compact all frequencies are O(k³). Its scope: lifted
  regular characters. Check B re-verifies the E-character statement on a
  box.
- **The same note, "Finite penalties and the scalar Jordan chain."**
  Penalties U|G|² + V S² leave the scalar potential block −g k² + 2V k⁴,
  negative at small k for every finite V. Check F re-verifies this.
- **The 2026-09-24 oscillator note.** It supplies the lattice Einstein–Hilbert
  symbol used here and the specified non-compact comparator,
  ω² ∝ Σ sin²(k/2). Its own scope leaves compact and nonlinear completions
  open.

Of this PR:
- probe 10 (the sum-rule machinery and the ker G moment lemma);
- probe 14 (the momentum-diagonal assignment);
- the gravity-records panel, same model family, whose lattice-gauge lens
  independently found the same exponent and an 8-slot ±1 move.

External, reference only:
- The energy-weighted (f-sum) double-commutator and single-mode bounds:
  Bijl–Feynman, Hohenberg–Brinkman.
- Chandrasekharan and Wiese (hep-lat/9609042): quantum links.
- Soft-graviton lattice rotor models: Xu (2006), Xu and Hořava (2010), Gu
  and Wen, whose linear "N-type" regime is uncontrolled. Their premises are
  not compared in detail here.
- Pretko (2017) and scalar-charge rank-2 U(1) models: linear modes, by
  replacing the momentum rule with ∂_i∂_jE_ij = 0, with helicity partners
  (probe 11).

All three landed or PR parents used here are unaudited. They are cited as
parents, not as retained authorities.

## Premises (supplied)

- **Slots.** Each is a spin S. The metric is h = S^z in the canonical slot
  coordinates q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz, 2h_xz).
- **The scalar rule.** C_y = (S S^z)_y, diagonal and linear: an exact Gauss
  law.
- **The momentum-rule gauge.** It shifts h along g = G^T δ. Its quantum-link
  strings are V_g = ∏ (S^{sign g})^{|g|}, with Y_g = i(V_g − V_g^dag).
- **Kinetic terms.** Shift monomials, with any diagonal prefactor, along
  patterns r with S r = 0, so that each commutes with the Gauss law.
- **Potential.** The landed lattice Einstein–Hilbert form X, as a
  polynomial in S^z.

## A — the construction (check A)

- The landed symbol is assembled into a real-space stencil: 75 entries, all
  real and in ½ℤ. On the 4³ torus X is symmetric, max |X G^T| = 9e-16, and
  it reproduces the symbol at a torus momentum.
- So X(m + g) = X(m) for every integer m and every gauge pattern. Hence
  [X(S^z), V_g] = 0: the invariance is strong, not only weak. This is
  checked for all 192 patterns.
- S G^T = 0 exactly, so the Gauss law commutes with every V_g.
- Gauge patterns have entries of magnitude 1, so V_g needs only S ≥ ½.

## B — the dual moment lemma (check B; re-verifies the 2026-09-14 bound)

On a box of 2³ cells, with the rule enforced at every site that touches the
box, the integer kernel of S has 14 generators.
- **Zeroth moments.** Every generator has vanishing zeroth moments. The
  leading symbol of S has six linearly independent quadratic components, so
  no finite pattern escapes.
- **First moments.** They span 8 dimensions:
  - 3 are the gauge patterns, invisible in the TT channel;
  - 5 are TT-visible in every sampled direction (min-of-max 0.70). These
    are the lattice symmetric curls.
- **A qubit-carriable witness.** An 8-slot pattern with entries ±1 has
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
  `m1(q) ≤ C_K q²`.
- The box-kernel moves' kinematic form factor is of order q²
  (max |w·r̂|²/q² = 3.45). That is a form factor, not a ground-state
  expectation: whether a given state reaches the bound is not shown.
- The comparison: the normalised non-compact DeWitt comparator has
  m1 = O(1), because its kinetic term π·M·π is ultralocal.
- With nonzero weight and finite m_−1, probe 10's chain gives
  `ω_min ≤ q √(2 C_K / χ_h(q))`.
  - If χ_h ≳ 1/q², the harmonic value set by the Einstein–Hilbert stiffness,
    then ω_min = O(q²).
  - A light-cone lowest mode would need χ_h = O(1). Whether any Gauss-law
    ground state has that is open.

## D — harmonic comparators (check D)

Each comparator is reduced exactly to the two TT modes. The moves are the
integer box kernels, with U = 1.

| Model | Kinetic | Potential | Fitted exponent of ω in \|K\| |
| --- | --- | --- | --- |
| swapped (this probe) | moves in ker S | Einstein–Hilbert | 2.00 ± 0.001 |
| probe 14's assignment | DeWitt | moves in ker G | 2.00 ± 0.001 |
| non-compact comparator | DeWitt | Einstein–Hilbert | 1.000, with ω = \|K\| |

Directions: axis, face diagonal, body diagonal and a generic one, each at
four momenta |k| = 0.2 … 0.025. These are specified models. They illustrate
the orders; the bound in C does not rest on them.

## E — the gauge side at finite S (check E)

- Gauge strings that overlap with opposite signs do not commute, although
  linearised diffeomorphisms do. The deformed momentum-rule algebra is
  non-abelian.
- A diagonal form invariant under the shift commutes exactly.
- Whether kinetic moves commute with the strings depends on S and on the
  overlap.
  - The first referee's example: the 8-slot move W8 and the gauge row at
    (0,1,0), j = 0 overlap on two slots, with equal and opposite signs.
  - At spin ½ nilpotency makes W8 commute with both V_g and V_g^dag.
  - The first version's claim that overlapping monomials cannot commute
    with both is withdrawn.
- The commutant of the Y_g is not enumerated.

## F — a soft scalar law (check F; re-verifies the landed penalty block)

If the scalar law were only an energy penalty U (S h)², single-slot moves
would be allowed and the kinetic term could be O(1). But:
- Einstein–Hilbert plus the penalty has a negative eigenvalue
  −c(n) K² + O(U K⁴) for every finite U.
- c(n) depends on direction: 1 on the axis, √3/2 on the face diagonal, 5/6
  on the body diagonal, and 0.874 in the sampled generic direction.
- The negative direction is the long-wavelength conformal mode.

This is the landed 2026-09-14 block, B_tt = −g k² + 2V k⁴, re-checked in the
swapped setting.

## What this means

For the two constructed finite-slot assignments with exact rules, one
canonical variable is diagonal and polynomial, and the other side is built
from moves in the kernel of the diagonal rule. The f-sum of the diagonal
variable is then bounded two powers of q below the non-compact comparator's:
- momentum diagonal (probe 10 and probe 14): the electric f-sum;
- metric diagonal (this probe): the metric f-sum.

In the harmonic comparators both give ω ∝ q², against ω = |K| for the
non-compact comparator. This is consistent with the landed 2026-09-24
statement for its specified comparator, which leaves compact and nonlinear
completions open.

What this does not decide:
- other assignments, such as mixed ones where some slots carry the metric
  and others the momentum;
- strongly correlated states with χ_h(q) = O(1);
- a composite or non-diagonal metric;
- the commutant of the strings;
- emergent (approximate) rules.

Six spin slots per cell also test finite local dimension, not the axioms'
one qubit per site.

## No-Go Discipline Gate

The bounded negative claims, inside the premises:
- (a) Gauss-law-compatible moves have zero zeroth moments, so the TT metric
  f-sum of move-built Hamiltonians is ≤ C_K q² in a ground state, with the
  conditional ω_min bound;
- (b) in the two specified harmonic comparators both assignments give
  ω ∝ q²;
- (c) a soft scalar law leaves a long-wavelength negative mode (a
  re-verification).

Not claimed: that the swapped assignment admits no light-cone graviton.
N7's steelman is convincing against that broader statement, so it is
withheld.

- **N1 — attack routes against (a)–(c).** Six distinct routes, all
  ATTEMPTED here.
  1. *A Gauss-law-compatible move with a nonzero zeroth moment.* Attempted in
     B: the integer box kernel, plus the leading-symbol argument (six
     independent quadratic components). Fails.
  2. *Diagonal prefactors or larger spins changing the double commutator.*
     Attempted in C: the identity holds for spin ½ and 1 with any diagonal
     prefactor. Fails.
  3. *A soft scalar law.* Attempted in F, which re-runs the landed penalty
     block in this setting: a negative conformal eigenvalue for every
     finite U in four directions. Fails.
  4. *Hidden growth of C_K through translation sums.* Attempted as an
     argument: each term is fixed-range with a uniformly bounded norm, so
     the per-term bound sums to a volume-independent constant. This is the
     argument of probe 10's T3 with roles swapped. Fails inside the
     premises.
  5. *The rotor (S → ∞) limit.* Attempted as an argument: with compact
     conjugate angles the moves are characters e^{ir·φ} with S r = 0, and
     B's moment statement applies to them unchanged. Fails.
  6. *Non-compact conjugate variables.* Attempted in D, third row:
     ω = |K|. This escapes the finite-slot premise; it is not a
     counterexample inside it.

  **Open routes (consistent with (a)–(c)):**
  - (i) χ_h(q) = O(1) in some ground state;
  - (ii) a composite or non-diagonal metric;
  - (iii) the commutant of the Y_g, including nilpotent overlaps (E);
  - (iv) emergent, approximate rules (the panel's large-S route);
  - (v) mixed assignments.
- **N2 — pairwise table.**
  - W1: finite S, unit-spaced S^z.
  - W2: the exact scalar Gauss law, term by term.
  - W3: fixed range and uniform norms.
  - W4 (state): a ground state with nonzero weight and finite m_−1, and
    χ_h ≳ 1/q² for the softness step.

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
    U = 1), used as illustrations;
  - the TT reduction uses the lattice K̂, which is exact because TT(K) lies
    in ker S(q);
  - C's form factor is not a ground-state expectation.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual claimed closed here | Match |
  | --- | --- | --- | --- |
  | 2026-09-14 note (docs/LOCAL_FINITE_CLOCK_TENSOR_..._2026-09-14.md):186 | an invariant E-character with nonzero zeroth moment | none; B re-verifies it on spin slots | yes |
  | same note:260 | a finite scalar penalty stabilising the scalar block | none; F re-verifies it | yes |
  | 2026-09-24 note (docs/TENSOR_LINEAR_DISPERSION_..._2026-09-24.md):36 | the lattice E-H symbol and the specified comparator | none; A assembles and checks X | yes |
  | probe 10 note (docs/ONE_QUBIT_PER_SLOT_..._2026-09-28.md):150, 186 | the double-commutator identity and the chain | (a)'s form, roles swapped | yes: C re-checks the identity |

  All are unaudited parents, not retained authorities.
- **N5 — rhetoric audit.**

  | Phrase | Resolutions tested | Holds at untested ones? |
  | --- | --- | --- |
  | "two powers of q below" | per_mode (60 direction-polarisation pairs), per_block (box kernels) | a bound on the f-sum only; not a statement about a state |
  | "ω ∝ q² in both assignments" | per_mode (two TT modes, four directions, four momenta) | only for the specified comparators |
  | "E-H exactly invariant" | per_element (all 192 gauge patterns, integer identity) | yes: it is an identity |

  The runner prints the certificate lines.
- **N6 — partial closure and primitive scan.**
  - The registry (docs/audit/data/axiom_premise_nodes.json) lists
    minimal_axioms, whose Qubit axiom fixes M₂(C) per site, and three
    unrelated primitives.
  - No registered primitive supplies non-compact local variables. The
    construction's spin-S slots are themselves supplied, outside the Qubit
    axiom.
  - A search of open PRs for non-compact or local-dimension proposals found
    none besides this one.
  - No labelling convention closes (a)–(c).
- **N7 — steelman.** A strongly correlated Gauss-law state could have a
  bounded χ_h and a linear TT mode, with its long-range static metric
  response carried by something other than the Einstein–Hilbert stiffness.
  Or the physical metric could be a composite of the S^z records, or the
  commutant could hold useful non-monomial kinetic operators. This is
  convincing against a broad no-go. So none is claimed, and routes (i)–(v)
  are the next targets.
- **N8 — cross-cycle echo.**
  - **Probe 10's potential-side bound:** mirrored here, not retired.
  - **The landed O(k³) statement for lifted regular characters** (both
    sides compact): not retired. With one side polynomial the order is k².
  - **The landed 2026-09-24 specified-comparator statement:** consistent
    with it. Its compact and nonlinear completions stay open, as here.
  - **The U(1) photon's mechanism** (an ultralocal electric stiffness): it
    does not transfer to (a), because the exact scalar law forbids
    ultralocal moves (B). Softening the law meets the landed penalty block
    (F).
- **Outcome.** PASS as scoped for (a)–(c) only. The broader no-go is
  withheld by N7. The pre-registered primary outcome is FAIL.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** It confirmed A, B, C's
  identity, D's pairing, and ω = |K| symbolically. Its six findings, and how
  this version answers each:
  1. **E's monomial claim was false.** It gave the W8 counterexample.
     Withdrawn; E is rewritten, with the example as a check.
  2. **The gate did not follow its contract.** Rewritten:
     - six attempted routes;
     - no RULED OUT BY PRIOR on unaudited parents;
     - an N5 table and the corrected certificate;
     - an N6 primitive scan;
     - N7 withholds the broad no-go;
     - N8 matches the 2026-09-24 scope.
  3. **Title and synthesis overclaimed.** Retitled to the f-sum bound, and
     the synthesis is scoped to the two constructed assignments. The
     pre-registration is described as adding no support.
  4. **C's "attained" and "Einstein's m1".** Now a form factor, and the
     normalised non-compact comparator.
  5. **F's coefficient is direction-dependent.** Now −c(n)K², checked in
     four directions.
  6. **Dependencies and prior art.** Probes 10 and 14 are added as
     upstream, with the f-sum literature and the rotor-model comparators.
- Fable check: pending.

## Reproduction

`python3 scripts/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.py`
prints 6 checks, A–F, the N5 lines and TOTAL, in about 2 s. The canonical
cache is at
logs/runner-cache/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.txt.
