---
claim_id: the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied construction, not adopted, on the landed tensor complex: every slot is a spin S with the metric diagonal, h = S^z in the canonical slot coordinates. The scalar rule is an exact linear Gauss law on S^z; the momentum-rule (linearised diffeomorphism) gauge acts by quantum-link strings V_g along g = G^T delta, whose entries have magnitude 1, so any S >= 1/2 carries them. (A) The landed lattice Einstein-Hilbert form, assembled in real space on the 4^3 torus, obeys X G^T = 0 exactly, so X(S^z) commutes exactly with every string V_g and V_g^dag (the strings are non-unitary and do not commute among themselves, so no gauge group is shown); the Gauss law commutes with every V_g. (B) Re-verification of the landed 2026-09-14 E-character bound on a 2^3 box: every finitely supported r with S r = 0 has vanishing zeroth moments; first moments span 8 dimensions (3 gauge, TT-invisible; 5 TT-visible); an 8-slot +-1 witness exists. (C) For Hamiltonians of diagonal terms and Gauss-law-compatible shift moves (fixed range, uniform norms, term-by-term sector-preserving), the double-commutator identity holds in every eigenstate, and in a ground state the TT metric f-sum obeys m1(q) <= C_K q^2, two powers of q below the normalised non-compact DeWitt comparator's O(1); the box-kernel moves' kinematic form factor is of order q^2 (a form factor, not a ground-state expectation); with nonzero weight and finite m_-1, omega_min <= q sqrt(2 C_K / chi_h(q)). (D) In the specified harmonic comparators (integer box-kernel moves, U = 1), the swapped assignment and probe 14's assignment both give omega ~ q^2 on both TT modes (fitted exponents 2.00 +- 0.05 on axis, face, body and a generic direction); the non-compact DeWitt + E-H comparator gives omega = |K|. (E) At finite S the deformed momentum-rule strings do not commute among themselves; whether kinetic moves commute with them depends on S and the overlap (at spin 1/2 an overlapping 8-slot move commutes with V_g and V_g^dag by nilpotency); the commutant of the Y_g is not enumerated. (F) Re-verification of the landed 2026-09-14 'finite penalties' block: an energy penalty U (S h)^2 in place of the exact scalar law leaves E-H, in the tensor metric, with the eigenvalue -K^2 + O(U K^4) on the transverse-trace (conformal) mode in every direction, for every finite U. Pre-registered primary outcome: FAIL (no move with a TT-visible zeroth moment), expected from the landed lemma. Not claimed: that the swapped assignment has no light-cone graviton; not shown: a ground state, chi_h(q), quantum closure of the V strings, a phase, or any other encoding."
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
was then weakly invariant under the deformed time rule, and the potential
side was bounded two powers of q below the comparator's. This probe swaps the roles: the metric is the
diagonal variable.

Now Einstein's potential (the Einstein–Hilbert term) is exactly invariant,
and the time rule becomes an exact Gauss law of the ordinary kind. But
kinetic terms built from moves that respect that Gauss law have zero zeroth
moment. So the metric channel's f-sum, a bound on how strongly the kinetic
side can move the metric at long wavelength, is two powers of q below the
non-compact comparator's.

In the simplest (harmonic) version of each assignment, the transverse-
traceless (TT) harmonic mode's frequency grows as q², not q. This note does
not claim that no light-cone graviton exists in the swapped assignment. A strongly correlated state, a
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
- **Soft-graviton lattice models** (reference only; as reported by the
  referees and checked against the abstracts, not re-derived).
  - Xu and Hořava (arXiv:1003.0009): a lattice boson model whose Gauss-type
    constraints define a low-energy subspace through dominant penalty
    terms, not exact microscopic rules. The symmetric tensor there has
    three z = 2 modes (two TT and a scalar), and a trace constraint leaves
    two z = 3 modes. Their compact vector potential has an unbounded
    integer conjugate. So their premises differ from this note's (finite
    spins, exact rules), and no identification with probe 10's case is
    claimed.
  - Gu and Wen (arXiv:0907.1203): a qubit "L-type" model with only helicity
    ±2 at k³. They call their linear "N-type" result unreliable. The N-type
    model is itself compact and discrete.
  - Xu (2006) is named for completeness; its premises are not compared
    here.
- Pretko (2017) and scalar-charge rank-2 U(1) models: linear modes, by
  replacing the momentum rule with ∂_i∂_jE_ij = 0, with helicity partners
  (probe 11).

All four landed or PR parents used here are unaudited. They are cited as
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
  X(S^z) commutes with every string V_g and V_g^dag, and not only on a
  sector. This is checked for all 192 patterns. The strings themselves are
  non-unitary and do not commute among themselves (E), so no gauge group is
  shown.
- S G^T = 0 exactly, so the Gauss law commutes with every V_g.
- Gauge patterns have entries of magnitude 1, so V_g needs only S ≥ ½.

## B — the dual moment lemma (check B; re-verifies the 2026-09-14 bound)

On a box of 2³ cells, with the rule enforced at every site that touches the
box, the integer kernel of S has 14 generators.
- **Zeroth moments.** Every generator has vanishing zeroth moments. The
  leading symbol of S has six linearly independent quadratic components, so
  no finite pattern escapes.
- **First moments.** The cubic identity they must satisfy has rank 10 of
  18, so they span at most 8 dimensions, and the box attains 8 (Fable
  check). So 8 is a theorem:
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
- The box-kernel moves' kinematic form factor is of order q². Its value
  depends on the kernel basis, so none is quoted. It is a form factor, not
  a ground-state expectation: whether a given state reaches the bound is not
  shown.
- The comparison: the normalised non-compact DeWitt comparator has
  m1 = O(1), because its kinetic term π·M·π is ultralocal.
- With nonzero weight and finite m_−1, probe 10's chain gives
  `ω_min ≤ q √(2 C_K / χ_h(q))`.
  - If χ_h ≳ 1/q², the harmonic value set by the Einstein–Hilbert stiffness,
    then ω_min = O(q²). In the tensor metric the TT stiffness is exactly K²
    per unit norm, in both polarisations and every direction, whatever the
    kinetic term.
  - A light-cone lowest mode would need χ_h = O(1).
  - In the subclass whose potential is exactly invariant under the momentum
    strings, it vanishes at q = 0, because the first-order gauge images span
    all six slots (Fable check). So no stable harmonic model in that
    subclass has χ_h = O(1).
  - C's full class also allows diagonal terms that do not commute with the
    strings (E leaves the commutant open). An on-site metric mass is in the
    class and gives χ_h = O(1), at the price of breaking the momentum
    gauge. So route (i) needs either strong correlation or a broken
    momentum rule (sol, second round).

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
the orders, and the bound in C does not rest on them. The finite-slot
prefactors depend on the move basis and are not quoted; ω = |K| for the
non-compact comparator is a normalisation (J = g = 1).

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
- In the tensor metric, Einstein–Hilbert plus the penalty has the
  eigenvalue −K² + O(U K⁴) for every finite U, in every sampled direction.
  The first version quoted values 1, √3/2, 5/6 and 0.87; those were
  q-coordinate artefacts.
- The eigenvector is the transverse-trace (conformal) mode, with overlap
  1.000.

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

- **N1 — attack routes against (a)–(c).** Five in-domain routes, all
  ATTEMPTED here, plus two domain escapes recorded separately.
  1. *A Gauss-law-compatible move with a nonzero zeroth moment.* Attempted in
     B: the integer box kernel, plus the leading-symbol argument (six
     independent quadratic components). Fails.
  2. *Diagonal prefactors or larger spins changing the double commutator.*
     Attempted in C: the identity holds for spin ½ and 1 with any diagonal
     prefactor. Fails.
  3. *A soft scalar law.* Attempted in F, which re-runs the landed penalty
     block in this setting: the conformal eigenvalue −K² for every finite U
     in four directions. Fails.
  4. *Hidden growth of C_K through translation sums.* Attempted as an
     argument: each term has fixed range and a uniformly bounded norm, so
     the per-term bound sums to a volume-independent constant (probe 10's T3
     argument with roles swapped). Fails inside the premises.
  5. *Global moves: uniform or winding patterns in ker S.* Attempted as an
     argument. The uniform shifts lie in ker S, since S is a second
     difference, but they carry weight only at q = 0, and fixed range
     excludes winding patterns. Fails for the q ≠ 0 TT channel.

  **Domain escapes** (not attacks inside W1–W3):
  - *Rotor slots (S → ∞, unbounded integers):* the bound persists (probe
    17).
  - *Non-compact conjugate variables:* ω = |K| (D, third row). This leaves
    the finite-slot premise.

  **Open routes (consistent with (a)–(c)):**
  - (i) χ_h(q) = O(1) in some ground state;
  - (ii) a composite or non-diagonal metric;
  - (iii) the commutant of the Y_g, including nilpotent overlaps (E);
  - (iv) emergent, approximate rules (the panel's large-S route);
  - (v) mixed assignments.
- **N2 — pairwise table.**
  - W1: finite S, unit-spaced S^z.
  - W2: the exact scalar Gauss law. It holds term by term automatically: a
    diagonal linear Gauss law grades shift monomials, so a sum preserves the
    sector iff each term does (Fable check).
  - W3: fixed range and uniform norms.
  - W4a (state): a ground state exists.
  - W4b (state): nonzero weight in the TT metric channel.
  - W4c (state): finite m_−1.
  - W4d (state): χ_h ≳ 1/q², needed only for the softness step. With
    probe 10's convention χ = 2 m_−1.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: finite spin allows soft laws | no: exact laws act on rotors | independent |
  | W1, W3 | no: finite spin allows long-range terms | no: bounded terms can act on rotors | independent |
  | W1, W4a | yes on a finite torus (a finite Hilbert space has a ground state); no in infinite volume | no | dependent in finite volume only |
  | W1, W4b | no: the channel weight is a state property | no | independent |
  | W1, W4c | no: even on a finite torus a degenerate ground space with TT weight makes m_−1 infinite | no | independent |
  | W1, W4d | no | no | independent |
  | W2, W3 | no: an exact law allows long-range terms | no: bounded local terms can break it | independent |
  | W2, W4a | no | no | independent |
  | W2, W4b | no | no | independent |
  | W2, W4c | no | no | independent |
  | W2, W4d | no | unresolved: open route (i) | unresolved |
  | W3, W4a | no | no | independent |
  | W3, W4b | no | no | independent |
  | W3, W4c | no | no | independent |
  | W3, W4d | no | no: an on-site mass is bounded and local and gives χ_h = O(1) | independent |
  | W4a, W4b | no | no | independent |
  | W4a, W4c | no | no | independent |
  | W4a, W4d | no | no | independent |
  | W4b, W4c | no | no | independent |
  | W4b, W4d | no | yes: χ = 2 m_−1 ≳ 1/q² > 0 requires nonzero weight | W4d implies W4b |
  | W4c, W4d | no: a finite m_−1 allows either scaling of χ_h | no: a lower bound does not make it finite | independent |

  The collapsed set is:
  - W1–W3 (domain);
  - W4c (the chain), with W4a implied by W1 in finite volume and W4b by
    W4d; W4c needs a gap or no zero-frequency weight, and is kept
    separate;
  - W4d (softness).

  In the subclass exactly invariant under the momentum strings, a stable
  harmonic model forces W4d (C).

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
  | 2026-09-14 note (docs/LOCAL_FINITE_CLOCK_TENSOR_..._2026-09-14.md):186 | an invariant E-character with nonzero zeroth moment | re-verified on spin slots (B), not newly closed | yes |
  | same note:260 | a finite scalar penalty stabilising the scalar block | re-verified (F), not newly closed | yes |
  | 2026-09-24 note (docs/TENSOR_LINEAR_DISPERSION_..._2026-09-24.md):36 | the lattice E-H symbol and the specified comparator | re-verified (A assembles and checks X), not newly closed | yes |
  | probe 10 note (docs/ONE_QUBIT_PER_SLOT_..._2026-09-28.md):150, 186 | the double-commutator identity and the chain | (a)'s form, roles swapped | yes: C re-checks the identity |

  All are unaudited parents, not retained authorities.
- **N5 — rhetoric audit.** Each phrase at the five resolutions.

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "two powers of q below" (f-sum) | each move's moments (B) | the rule at every site touching the box | 60 direction–polarisation pairs | the 2³ box kernel | holds per term for fixed range and uniform norms; no state is tested |
  | "ω ∝ q² in both assignments" | not applicable (a Fourier-space comparator has no per-element content) | not applicable (translation-invariant symbol) | two TT modes, four directions, four momenta | the box kernels as moves | untested: the negative holds only for the specified comparators, not for states |
  | "E-H exactly invariant" | each of 192 gauge patterns (integer identity) | every torus site | the symbol at a torus momentum | the 4³ torus | an identity, so it holds lattice-wide; no gauge group is claimed |

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
  5. **F's coefficient is direction-dependent in q-coordinates.** Now
     stated in the tensor metric, where it is −K² in every direction (the
     Fable check), and checked in four directions.
  6. **Dependencies and prior art.** Probes 10 and 14 are added as
     upstream, with the f-sum literature and the rotor-model comparators.
- **Fable check (same family as the supervisor), on the first version:
  STANDS WITH CORRECTIONS.** No mathematical error. It rebuilt X from the
  continuum h:R(h), G and S in real space, the box kernel, and a dual-basis
  TT reduction, and found exponents 2.00, 2.00 and 1.00. Its corrections,
  applied here:
  - cite the 2026-09-24 comparator result, not a landed wall;
  - F's eigenvalue is −K² in the tensor metric (the q-coordinate values
    were artefacts);
  - the basis-dependent prefactors (3.45, ω/K²) are dropped;
  - probe 14's kinetic statement is scoped;
  - the pre-registration is "expected from the landed lemma";
  - "exactly invariant" means commutation with each string.
  Its sharpenings are also added:
  - term-by-term preservation is automatic;
  - X(0) = 0 forces χ_h ≳ 1/K² in every harmonic model of the class;
  - the first-moment dimension 8 is a theorem.
- **gpt-5.6-sol, third round: STANDS WITH CORRECTIONS.** Findings 1 and 7
  resolved; no new algebraic error. It asked for:
  - W4a split into its three conditions;
  - N5's blank cells dispositioned;
  - the "no net content" gloss removed;
  - the rotor-model comparison given;
  - "now fixed" softened.
- **gpt-5.6-sol, sixth round: CONFIRMED AS REVISED.** The fifth round's one remaining item (the W1/W4c row) was fixed, and no new error was found.
- **gpt-5.6-sol, fourth round: STANDS WITH CORRECTIONS.**
  - Resolved: 3 (the wording) and N5.
  - Addressed in this version:
    - N2 now lists every pair, with W4d ⇒ W4b and a finite-volume
      qualifier on W1 ⇒ W4a;
    - the rotor-model paragraph is corrected (Xu–Hořava's constraints are
      penalty-defined; Gu–Wen's N-type model is compact; Xu 2006 only
      named);
    - this history no longer calls those items done before a referee
      confirms them.
- **gpt-5.6-sol, second round: STANDS WITH CORRECTIONS.**
  - Resolved: the ground-state and form-factor wording (4) and the
    tensor-metric −K² (5).
  - Partly resolved, and addressed here as follows:
    - the runner docstring still carried the withdrawn monomial claim;
    - the gate (in-domain routes separated from domain escapes, W4 split,
      N4 wording, the full N5 table);
    - "zero net content" and "graviton" in the plain paragraph;
    - "all three" should read all four parents;
    - the rotor-model comparison is now stated as not done.
  - New and applied: the X(0) = 0 conclusion holds only for potentials
    exactly invariant under the momentum strings (an on-site mass is in C's
    class).
  - It confirmed the first-moment dimension 8 independently.

## Reproduction

`python3 scripts/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.py`
prints 6 checks, A–F, the N5 lines and TOTAL, in about 2 s. The canonical
cache is at
logs/runner-cache/the_swapped_quantum_link_assignment_metric_diagonal_on_the_tensor_complex_2026_09_28.txt.
