---
claim_id: one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied model, not adopted: the landed tensor-electric slots and integer vector (momentum) stencil G of the 2026-09-14 tensor note, each slot a finite-dimensional space on which the electric value is diagonal with unit-spaced eigenvalues (one qubit per slot: +-1/2), and any Hamiltonian that is a translation-invariant sum of finite-range terms preserving the exact integer rule G = 0. (T2) Every finitely supported integer kernel move has vanishing zeroth and first spatial moments (proof by pairing with polynomial gauge vectors; checked). (T3) For every eigenstate and every electric Fourier mode O_q, the double commutator obeys |<[O_q^dag,[H,O_q]]>| <= C_H |q|^4 with C_H = (1/4) sum over term types and change patterns of ||T_(a,m)|| mu_2(m)^2; for the ground state m1(O_q) <= C_H |q|^4. No small-field expansion or clock lifting is used. (T4) With the exact spectral-moment chain of the landed ring-model note, the lowest excitation coupled to O_q has omega_min <= q^2 sqrt(2 C_H / chi(q)) and omega_min <= C_H q^4 / S(q); a mode with omega >= c|q| that is the lowest in that channel requires chi(q) <= 2 C_H q^2/c^2 and S(q) <= C_H q^3/c (an incompressible electric pattern). (T5) The landed linear comparator's TT stiffness is order q^2 (its symbol identities re-verified), so no finite-range linear readout of the slots reproduces its electric sum rule at small q. (T1, T6) Re-verifications and one addition: the qubit-carriable 20-slot moves (landed 2026-09-24) are recomputed; a 3D qubit move stiffens the axial cross shear, and with the 2x2 planar block all three physical modes are stiffened in the sampled directions, each as q^4. Not computed: any qubit ground state, its chi(q), a phase, box-free minimal moves, or a model realising an incompressible electric pattern."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_qubit_per_slot_carries_the_tensor_momentum_rule_and_an_exact_q4_sum_rule_bounds_its_graviton_channel_2026_09_28.py
---

# One qubit per slot under the tensor momentum rule: an exact sum rule bounds the graviton channel by q^4; a light-cone mode needs an incompressible electric pattern

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** supplied-model mathematics with exact checks; unaudited.
Independent checks are recorded below.

## In one paragraph

The owner asked whether gravity could be a pattern of qubit records obeying
a neighbourhood rule, the tensor version of the photon test. Most of that
test is already on main (see Prior art). Main's result:
- exact local tensor rules give gravitons, but their frequencies grow like
  k^2 or k^3, not like k;
- a light-cone graviton needs local variables that can grow without bound.

That result assumes a smooth small-field regime, which a single qubit does
not have. This note closes that gap for qubits with one exact statement:
- **The rule.** Under the momentum rule, every allowed record change leaves
  the total and the balance point of every record pattern unchanged.
- **The consequence.** A long smooth pattern can only change through its
  curvature. So the graviton channel's total "push" at wavenumber q is at
  most a constant times q^4, in every state of every such qubit model.
- **What follows for speed.** If smooth patterns are as easy to push as they
  are in every phase examined so far, the lowest waves crawl: frequency at most ∝ q^2. A
  wave on light's cone would need the smooth pattern to be incompressible,
  with an energy that grows as the pattern gets smoother. Nothing built here
  or on main has that.

## Prior art on main (read in full before this note)

- [LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md](LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md)
  supplies:
  - the slots and the stencil G used here;
  - the vector and scalar constraint complex;
  - the linear comparator H_N;
  - the regular compact-character bound. With both rules, lifted clock
    characters and a smooth small-field expansion, every frequency is
    O(k^3). Its moment argument, that a compactly supported invariant
    character is O(k^2), is the classical ancestor of T2 here. Its own words:
    "This is not a no-go for qubits".
- [TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md](TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  gives:
  - the comparator's exact lattice symbol, omega^2 = J g t with
    t = sum 4 sin^2(k_i/2);
  - the identities re-verified in check F.
- [DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md](DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  gives:
  - the two-site freeze;
  - the ten-slot planar kernel move (entries up to 2);
  - the radius-two MILP.
- [DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_AND_SLOT_FIELDS_GENERATE_THE_LANDED_TENSOR_FIELD_S_CURVATURE_MOVES_AT_TWELFTH_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md](DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_AND_SLOT_FIELDS_GENERATE_THE_LANDED_TENSOR_FIELD_S_CURVATURE_MOVES_AT_TWELFTH_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  gives:
  - the radius-two unit-entry search with support twenty;
  - the explicit planar twenty-slot pattern and the spatial patterns;
  - a selected cosine comparator with omega^2 = 2 J g lambda(k), O(k^2),
    in which one branch vanishes on coordinate planes.
  - **T1 here re-verifies these qubit moves; they are not new.**
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
  gives:
  - the U(1) ring model's exact first moment, m1 = 2 u s^2;
  - the chain omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0, used in T4.
  - T3 is the tensor analogue of that m1 computation, made general.
- External, for reference only and re-derived nothing:
  - Gu and Wen (arXiv:0907.1203) and Xu and Horava (arXiv:1003.0009):
    soft gravitons from tensor constraints;
  - Pretko (arXiv:1604.05329): the mobility of vector charges.

**What is new here.**
- T3, the exact operator sum rule for integer-valued slots of any finite
  dimension (one qubit included), with no small-field expansion.
- Its consequences T4 and T5.
- A small addition to T6: the 3D qubit moves stiffen the axial cross shear
  that planar moves leave soft.

## Premises and declared objects

- **Slots.** These are the landed tensor-electric slots on the doubled
  lattice. The diagonal slot jj sits at 2x and the face slot ij at
  2x + e_i + e_j; the row j sits at 2x + e_j. Physical positions are
  r = (doubled position)/2.
  - Each slot is a finite-dimensional space. Its electric value E_s is
    diagonal with unit-spaced eigenvalues (spin type, no wrap-around).
  - One qubit per slot means E_s = +-1/2.
- **Rule.** The landed integer stencil is
  `(G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i != j}[p_ij(x) - p_ij(x-e_i)]`.
  The sector is G E = 0, or any fixed static background.
- **Hamiltonian.** H = sum_x sum_a T_(a,x) is a translation-invariant sum of
  finite-range terms that preserve the sector.
  - Each term splits uniquely into electric-change components T_(a,m).
    Here E_s T_(a,m) = T_(a,m)(E_s + m_s), and the change pattern m is an
    integer vector.
  - Preserving the sector forces G m = 0 for every component that acts in
    it.
- **Probe mode.**
  `O_q = N^(-1/2) sum_s exp(i q.r_s) eps_c(s) E_s`, with |eps| = 1 in the
  six-component slot space.
- **Spectral moments** in an eigenstate |0>:
  `m_j(O) = sum_n (E_n - E_0)^j |<n|O|0>|^2` over n with E_n != E_0.
  The static susceptibility is chi = 2 m_-1 and the centred structure factor
  is S = m_0.
- **Records.** Slot values are record contents, and a move changes several
  of them together. This conflicts with permanence under the Record axiom,
  exactly as it does in the landed link and tensor models.

## T1 — re-verification of the landed stencil and qubit moves (checks A, B)

- The landed ten-slot planar move is in ker G. The coefficient-bound-2 MILP
  in the radius-2 box reproduces minimum support 10 (A).
- With coefficient bound 1 there is no move in the radius-1 box. In the
  radius-2 box the minimum support is 20, from both a diagonal and a face
  anchor (B).
- The two 20-slot witnesses are checked row by row: a 3D move, and the 2x2
  planar block. The block is four landed planar moves whose +-2 entries
  cancel.
- These reproduce the landed 2026-09-24 results. The box-bounded searches
  are solver-reported, not box-free minimum theorems.

## T2 — the moment lemma (check C)

**Statement.** Take any finitely supported integer (or real) m with G m = 0.
Its zeroth and first spatial moments, component by component and at the
declared slot positions, vanish:
`sum_s m_s = 0` and `sum_s m_s r_s = 0`, for each component.

**Proof.**
1. The vector gauge map is G^T, since the rule generates electric-conjugate
   shifts by the transpose.
2. Applied to gauge vectors xi whose entries are polynomials of degree at
   most 2 in the row positions, G^T produces every constant and every
   linear symmetric strain pattern on the slots. The midpoint differences
   are exact on quadratics.
3. For such a strain pattern s = G^T xi, the pairing is
   `<m, s> = <m, G^T xi> = <G m, xi> = 0`. The pairing is legitimate
   because m has finite support and only rows touching that support enter.
4. Pairing with constant strains gives the zeroth moments. Pairing with
   linear strains gives the first moments.

The runner reproduces all 24 strain patterns (6 constant, 18 linear) by
G^T xi, to residual 2e-14. It confirms zero moments on the witnesses and on
20 random integer combinations of rotated and translated moves.

**Consequence (Taylor).** Let `mu_2(m) = sum_s |m_s| |r_s - r_0|^2` for any
centre r_0. Then `|m_hat(q)| <= mu_2(m) |q|^2 / 2` at every q. This is
checked on a zone grid (E).

## T3 — the exact sum rule (check D)

**Statement.** For every eigenstate |0> and every q:

`<0|[O_q^dag,[H,O_q]]|0> = m1(O_q) + m1(O_q^dag)`, and
`|<0|[O_q^dag,[H,O_q]]|0>| <= C_H |q|^4`,
with `C_H = (1/4) sum_a sum_m ||T_(a,m)|| mu_2(m)^2` (per unit cell).

For the ground state, m1(O_q^dag) >= 0, so `m1(O_q) <= C_H |q|^4`.

**Proof.**
1. For a component T_m and the diagonal O, write w(m) =
   N^(-1/2) sum_s exp(i q.r_s) eps_c(s) m_s. Then `[T_m, O] = -w(m) T_m`
   and `[O^dag, [T_m, O]] = -|w(m)|^2 T_m`.
2. Sum over the N translates of each component. The phases drop out, giving
   `sum_x |w(m_x)|^2 = |m_hat(q).eps|^2 <= |m_hat(q)|^2`.
3. Then `|<0|[O^dag,[H,O]]|0>| <= sum_(a,m) |m_hat(q)|^2 ||T_(a,m)||`,
   which is at most C_H |q|^4 by T2.
4. The identity relating the double commutator to m1(O) + m1(O^dag) is the
   standard f-sum: expand in the eigenbasis.

No small-field expansion, no clock character and no lifting condition
enters. The only inputs are that E is diagonal with integer-spaced values,
that the rule is exact, and that the terms have finite range.

Check D verifies the operator identity and the eigenstate sum rule by dense
diagonalisation of 10 qubits:
- 12 random shift patterns plus a random diagonal part;
- operator residual 2e-14;
- sum rule checked in three eigenstates;
- the ground-state double commutator is 0.50 of the norm bound.

**Contrast with U(1).** A U(1) ring move is a closed loop. Its zeroth moment
vanishes but its first moment, the oriented area, does not. So the U(1)
first moment is O(q^2), which is the landed m1 = 2 u s^2, and it permits a
linear photon (check F). The tensor rule removes the first moment as well,
and that is the whole difference.

## T4 — what the sum rule allows (check G)

This uses the exact chain from the landed ring-model note:
`omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0`,
for the lowest excitation that carries weight in O_q. With T3 it gives

`omega_min(q) <= q^2 sqrt(2 C_H / chi(q))`  and  `omega_min(q) <= C_H q^4 / S(q)`.

- **Compressible electric pattern** (chi(q) >= chi_0 > 0 at small q, as in
  the linear comparator, chi = 1/J). The graviton channel has an excitation
  with omega = O(q^2): the lowest wave crawls.
- **The special point** (flat S, as at a Rokhsar–Kivelson point). Then
  omega_min = O(q^4).
- **Light cone.** A mode with omega >= c|q| that is the lowest in that
  channel requires both of these:
  - `chi(q) <= 2 C_H q^2 / c^2`, so the long-wavelength electric pattern is
    incompressible;
  - `S(q) <= C_H q^3 / c`, so the equal-time electric fluctuations vanish
    three powers faster than a harmonic graviton's.
  - The mode's weight in the electric channel is then O(q^3).
- Check G illustrates this with Gaussian models on the qubit family's
  stiffness. A fixed chi gives omega ~ q^2 (fitted exponent 1.999). An
  electric energy J(q) = 1/t, which grows like 1/q^2, gives omega ~ q
  (0.999), with S ~ q^3 (2.998) and chi ~ q^2 (1.999).

These are necessary conditions on the lowest mode in the channel. A faster
mode above a softer one is not excluded. It would not be the long-wavelength
end of the channel, and the softer modes would couple wherever the electric
field couples.

## T5 — the linear comparator's sum rule is out of reach (check F)

The landed linear comparator H_N is quadratic, so its double commutator is a
c-number. On the TT modes it equals g times the potential symbol, which is
order t = O(q^2). In the slot metric, the TT restriction of X_r divided by t
converges to the positive pair 0.531 and 0.840. Its identities G_r X_r = 0
and X_r M X_r = t X_r + s s^T/2 are re-verified.

Let pi = L E be any finite-range linear readout of the slots, with
pi_q = L(q) E_q and ||L(q)|| <= ||L||_1. Then
`m1(eps.pi_q) <= ||L||_1^2 C_H |q|^4`. So no such readout reproduces the
comparator's electric sum rule at small q.

In check F, the ratio of the qubit family's stiffness to t falls with
log-log slope 1.995. The comparator's canonical momentum is therefore not a
local linear function of qubit slots obeying the exact rule. It would have
to be one of:
- a composite (nonlinear) operator;
- a non-local readout (L(q) ~ 1/q);
- the momentum of a model outside the premises.

## T6 — the qubit family stiffens every physical mode as q^4 (check E)

- **Family.** The two 20-slot witnesses, all 24 proper rotations and all
  translations.
- **Result.** On the physical subspace ker G(q) (three modes), all three
  eigenvalues divided by q^4 converge, and are positive along an axis, a
  face diagonal, the body diagonal and a generic direction. At q = 0.025:
  - axis: 16, 128, 128;
  - face: 16, 80, 96;
  - body: 42.7, 42.7, 80;
  - generic: 20.2, 80.8, 91.8.
- **Along an axis, each family alone reaches only part.**
  - The planar block family stiffens only the plus shear and the scalar
    (rank 2). This matches the landed "one branch vanishes on coordinate
    planes".
  - The 3D family stiffens only the cross shear (rank 1).
  - One qubit per slot therefore reaches every polarisation. A Gaussian
    model with any finite electric stiffness then has three branches, the
    two shears and the scalar, each with omega ∝ q^2.

## What this means

**For gravity as a pattern of records.**
- With one qubit per slot and the exact momentum rule, the soft-graviton
  structure is complete: every polarisation is stiffened, and only as q^4.
- The landed large-slot bound now has an exact qubit counterpart. It does not
  depend on a small-field regime.
- The one route left to a light-cone graviton is an incompressible
  long-wavelength electric pattern: an electric energy that grows as
  patterns get smoother.
  - In a Gaussian comparator that is a non-local 1/q^2 electric energy.
  - A local qubit model could only produce it collectively. One conceivable
    way (a reading, not constructed) is for the electric tensor itself to
    source a further long-range field, so that smooth electric patterns cost
    Coulomb-like energy.
  - The phases examined on main and here (the Rokhsar–Kivelson point, the
    harmonic comparators, the landed large-slot class) are compressible or
    softer.
- The other exits are the ones main already names:
  - a nonlinear or composite graviton;
  - a non-local readout;
  - an inexact, emergent rule. The bound applies to its exact-rule
    effective Hamiltonian if that is local;
  - clock aliasing, where the rule holds only mod N;
  - infinite-range terms.

**For the owner's reading "time is the shifting or creation of records".**
- Here the record events are the moves. T2 says each event conserves the
  total and the balance point of every electric pattern, so smooth patterns
  change only through curvature.
- GR's second (energy) constraint, the lapse, would make local time a
  pattern. In the landed class it pushes the frequencies further down, to
  k^3.
- Whether a record-event clock can instead supply the missing
  incompressibility is the natural next question. It is not tested here.

## No-Go Discipline Gate

- **N1 (routes examined).**
  - (i) Finite-range Hamiltonians on integer-valued commuting slots with the
    exact rule: T3 bound.
  - (ii) The landed linear comparator: order q^2, outside (i) because its
    variables are unbounded.
  - (iii) The U(1) ring: order q^2, because its moves keep a first moment.
  - (iv) Gaussian compressible and incompressible illustrations.
  - (v) The qubit move family's stiffness.
  - Not examined: nonlinear or composite readouts, non-local readouts,
    emergent rules, clock aliasing, infinite range, non-commuting electric
    slots.
- **N2 (independence).** T3 and T4 are one argument: sum rule plus moment
  chain. T5 is a corollary of T3. T6 is a separate finite computation. The
  landed large-slot bound and T3 are different theorems about overlapping
  classes, not two independent walls.
- **N3 (supplied).** The slots, the rule, the finite-range Hamiltonian class
  and the reading of slot values as records are supplied. None is derived
  from the axioms.
- **N4 (parents).** The landed tensor notes govern the stencil, the planar
  and qubit moves and the comparator. The landed ring-model note governs the
  moment chain. Nothing unlanded is a premise.
- **N5 (resolutions).** Four are printed by the runner:
  1. qubit moves exist, re-verified;
  2. the sum rule is exact, with no small-field expansion;
  3. moment vanishing;
  4. the comparator's order-q^2 stiffness is unreachable by finite-range
     linear readouts, and a light-cone mode needs chi = O(q^2).
- **N6 (live routes).**
  - An incompressible electric pattern in a local qubit model; none is known
    or constructed.
  - A composite graviton.
  - An emergent rule with non-local effective terms.
  - None is declared impossible.
- **N7 (strongest objection).** The bound concerns the lowest mode coupled
  to the electric channel. A linear mode could exist above softer modes, or
  with electric weight O(q^3) in an incompressible state. Both are kept
  explicit.
- **N8 (prior art).**
  - The stencil, the planar and qubit moves and the comparator are landed.
  - The moment chain is landed (U(1)).
  - The soft-graviton phenomenology is in Gu–Wen and Xu–Horava.
  - New are the exact tensor sum rule for integer-valued slots and its
    corollaries.

## What this does not show

It does not show any of these:
- a qubit ground state, or its chi(q) or S(q);
- a phase or its stability;
- that gravitons exist in any such model;
- a box-free minimal move;
- a model with an incompressible electric pattern;
- anything about the scalar (energy) rule beyond the landed results;
- anything about matter coupling or sources;
- any link to the Admissibility axiom beyond the supplied reading.

## Independent checks

Pending.

## Reproduction

`python3 scripts/one_qubit_per_slot_carries_the_tensor_momentum_rule_and_an_exact_q4_sum_rule_bounds_its_graviton_channel_2026_09_28.py`.
It prints 7 checks, A–G, the N5 lines and TOTAL, in about 30 s. The
canonical cache is at
logs/runner-cache/one_qubit_per_slot_carries_the_tensor_momentum_rule_and_an_exact_q4_sum_rule_bounds_its_graviton_channel_2026_09_28.txt.
