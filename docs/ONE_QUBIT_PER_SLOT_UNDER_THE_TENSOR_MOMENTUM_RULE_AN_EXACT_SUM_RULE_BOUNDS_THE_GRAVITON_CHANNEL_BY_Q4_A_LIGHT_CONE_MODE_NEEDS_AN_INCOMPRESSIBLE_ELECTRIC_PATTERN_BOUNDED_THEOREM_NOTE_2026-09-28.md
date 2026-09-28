---
claim_id: one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied model, not adopted. It uses the landed tensor-electric slots and the integer vector (momentum) stencil G of the 2026-09-14 tensor note. Each slot is a finite-dimensional space on which the electric value is diagonal, with eigenvalues in a unit-step arithmetic progression (one qubit per slot: +-1/2). The Hamiltonian is any translation-invariant sum of terms of fixed finite range with volume-independent norms, each of which preserves the chosen exact sector G E = b. (T3, the new synthesis) For every eigenstate and every electric Fourier mode O_q, the double commutator obeys |<[O_q^dag,[H,O_q]]>| <= C_H |q|^4, where C_H = (1/4) times the sum over term types and ACTIVE change patterns m (G m = 0) of ||T_(a,m)|| mu_2(m)^2, a finite volume-independent constant. For a ground state, m1(O_q) <= C_H |q|^4. No small-field expansion or clock lifting is used. (T4) Take a ground state with nonzero positive weight in O_q and finite m_-1. The lowest excitation carrying that weight has omega_min <= q^2 sqrt(2 C_H / chi(q)). If that excitation has omega_min >= c|q|, then chi(q) <= 2 C_H q^2 / c^2, and hence S(q) <= C_H q^3 / c. This is a necessary condition only: gapped channels also meet it, and a linear mode above softer weight is not excluded. (T5) The landed linear comparator's TT stiffness is Theta(q^2), so no fixed, uniformly bounded, finite-range linear readout of the slots reproduces its electric sum rule at small q. (T6) The qubit move family (two 20-slot witnesses, 24 rotations, translations) stiffens all three physical modes at order q^4 in all 1503 sampled directions, with minimum leading coefficient 16 on the coordinate planes; the 3D witness supplies the axial cross shear. (T1, T2) The qubit moves (landed 2026-09-24) and the moment lemma (landed 2026-09-14) are re-verified, not new. Not computed: any qubit ground state, its chi(q), a phase, a graviton, box-free minimal moves, an analytic positivity certificate for every direction, or a model with chi = O(q^2)."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_qubit_per_slot_carries_the_tensor_momentum_rule_and_an_exact_q4_sum_rule_bounds_its_graviton_channel_2026_09_28.py
---

# One qubit per slot under the tensor momentum rule: an exact sum rule bounds the graviton channel by q^4; a light-cone lowest mode needs an incompressible electric pattern

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** supplied-model mathematics with exact checks; unaudited.
Independent checks: a Fable check (confirmed with corrections) and the
other-vendor gpt-5.6-sol referee (stands with corrections). Both are recorded
below, and this revision applies their corrections.

## In one paragraph

The owner asked whether gravity could be a pattern of qubit records obeying
a neighbourhood rule, the tensor version of the photon test. That test is
mostly on main already (see Prior art).
- **What main has.** Exact local tensor rules have harmonic comparators with
  soft graviton-like modes: frequencies grow like k^2 or k^3, not k. Main
  does not establish a graviton phase.
- **Main's bound.** It covers smooth small-field clock models, and it says
  itself that it is not a statement about qubits.
- **What this note adds.** An exact qubit-level form of the potential side of
  that bound.
  - Every change the momentum rule allows keeps both the total and the
    balance point of every electric pattern.
  - So in any state of any such model, the "push" available to the graviton
    channel at wavenumber q is at most a constant times q^4.
- **What follows for speed, and only conditionally.** Suppose the electric
  pattern's static susceptibility stays bounded below at long wavelengths, as
  it does in every comparator examined. Then the lowest mode carrying
  electric weight has frequency at most ∝ q^2.
- **What a light-cone lowest mode would need.** A susceptibility vanishing
  like q^2: an electric pattern that is incompressible at long wavelengths.
  - This is necessary, not sufficient. Gapped channels meet it too.
  - No model on main or here is known to meet it with a gapless mode.

## Prior art on main (read in full before this note)

- [LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md](LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md)
  supplies:
  - the slots and stencil;
  - the vector and scalar constraint complex;
  - the linear comparator H_N;
  - the regular compact-character bound.
  - Its "Quantitative spatial-moment proof" already states the moment lemma
    at the lattice level, with midpoint offsets and the same bound
    |m(k)| <= |k|^2 mu_2/2. **T2 here is a re-verification of that lemma.**
  - Its own words on its bound: "This is not a no-go for qubits".
- [TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md](TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  gives the comparator's exact lattice symbol, omega^2 = J g t with
  t = sum 4 sin^2(k_i/2).
- [DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md](DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  gives the ten-slot planar move and the radius-two MILP.
- [DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_AND_SLOT_FIELDS_GENERATE_THE_LANDED_TENSOR_FIELD_S_CURVATURE_MOVES_AT_TWELFTH_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md](DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_AND_SLOT_FIELDS_GENERATE_THE_LANDED_TENSOR_FIELD_S_CURVATURE_MOVES_AT_TWELFTH_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  gives:
  - the radius-two unit-entry search with support twenty;
  - the planar twenty-slot pattern and the spatial patterns;
  - a selected cosine comparator with omega^2 = 2 J g lambda(k), O(k^2),
    one branch vanishing on coordinate planes.
  - **T1 here re-verifies these moves.**
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
  gives:
  - the diagonal-operator double-commutator identity;
  - the U(1) m1 = 2 u s^2;
  - the moment chain used in T4.
- External, for reference only:
  - Gu and Wen (arXiv:0907.1203) and Xu and Horava (arXiv:1003.0009): soft
    gravitons from tensor constraints;
  - Pretko (arXiv:1604.05329): the mobility of vector charges.

**What is new here.**
- **T3** puts two landed ingredients together:
  - the ring note's diagonal double-commutator identity;
  - the tensor note's moment bound.
  The result is an exact eigenstate sum rule for the tensor rule, valid for
  every finite slot dimension with unit-step electric spectra, one qubit
  included. It has an explicit norm constant for arbitrary change components.
  This is a synthesis, not a new mechanism.
- **T4 and T5** are its consequences.
- **T6** adds that the 3D qubit move stiffens the axial cross shear, which
  planar moves leave soft.

## Premises and declared objects

- **Slots.** These are the landed tensor-electric slots. The diagonal slot jj
  sits at doubled position 2x, the face slot ij at 2x + e_i + e_j, and the
  row j at 2x + e_j. Physical position is r = (doubled position)/2.
  - Each slot is finite-dimensional. Its electric value E_s is diagonal, and
    all E_s commute.
  - The eigenvalues form a unit-step arithmetic progression, with no
    wrap-around. One qubit per slot has E_s = +-1/2.
- **Rule.** The landed stencil is
  `(G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i != j}[p_ij(x) - p_ij(x-e_i)]`.
  Fix a sector G E = b, where b is a static background (b = 0 in the checks).
- **Hamiltonian.** H = sum_x sum_a T_(a,x) is a translation-invariant sum.
  - Each term has fixed finite range and a norm independent of the volume.
  - Each term individually preserves the chosen sector.
  - Each term splits uniquely into electric-change components T_(a,m), with
    E_s T_(a,m) = T_(a,m)(E_s + m_s) and m an integer vector.
  - Sector preservation by the term makes every component that acts in the
    sector satisfy G m = 0. These are the **active** components; only they
    enter below.
- **Probe mode.**
  `O_q = N^(-1/2) sum_s exp(i q.r_s) eps_c(s) E_s`, with |eps| = 1 in the
  six-component slot space and N the number of coarse cells.
- **Spectral moments** in an eigenstate |0>:
  `m_j(O) = sum_n (E_n - E_0)^j |<n|O|0>|^2` over n with E_n != E_0.
  The static susceptibility is chi = 2 m_-1 and the centred structure factor
  is S = m_0.
- **Records.** Reading slot values as record contents is supplied, not
  derived. A move changes several contents together, which conflicts with
  the Record axiom's permanence. This is the same wall as in the landed link
  and tensor models. Nothing below uses the records reading.

## T1 — re-verification of the landed stencil and qubit moves (checks A, B)

- The landed ten-slot planar move is in ker G. The coefficient-bound-2 MILP
  in the radius-2 box reproduces minimum support 10.
- With coefficient bound 1 there is no move in the radius-1 box. In the
  radius-2 box the minimum support is 20, from both a diagonal and a face
  anchor.
- The two 20-slot witnesses are verified row by row: a 3D move, and the 2x2
  planar block (four landed planar moves whose +-2 entries cancel).
- These results are landed (2026-09-24). The searches are solver-reported
  and box-bounded.

## T2 — re-verification of the landed moment lemma (check C)

**Statement.** Every finitely supported m with G m = 0 has zero zeroth and
first spatial moments, component by component at the declared positions.

**Proof** (the landed parent's, restated).
1. G^T of gauge vectors that are polynomials of degree at most 2 in the row
   positions gives every constant and every linear symmetric strain pattern.
2. Therefore `<m, s> = <m, G^T xi> = <G m, xi> = 0` for each such pattern s.
3. Taylor's remainder then gives `|m_hat(q)| <= mu_2(m) |q|^2 / 2`, where
   `mu_2(m) = sum_s |m_s| |r_s - r_0|^2` for any centre r_0.

Check C reproduces the 24 strain patterns to residual 2e-14 and confirms zero
moments on the witnesses and on random integer combinations. Both independent
checkers also confirmed it on kernel vectors built without the witnesses.

## T3 — the exact sum rule (check D)

**Statement.** For every eigenstate |0> and every q:

`<0|[O_q^dag,[H,O_q]]|0> = m1(O_q) + m1(O_q^dag)`, and
`|<0|[O_q^dag,[H,O_q]]|0>| <= C_H |q|^4`,
with `C_H = (1/4) sum_a sum_(active m) ||T_(a,m)|| mu_2(m)^2` per unit cell,
where components are regrouped by change pattern m.

For a ground state, m1(O_q^dag) >= 0, so `m1(O_q) <= C_H |q|^4`.

**Proof.**
1. For an active component, with w(m) =
   N^(-1/2) sum_s exp(i q.r_s) eps_c(s) m_s:
   `[T_m, O] = -w(m) T_m` and `[O^dag, [T_m, O]] = -|w(m)|^2 T_m`.
   A common offset of the electric spectrum cancels in these commutators.
2. Sum over the N translates of each pattern:
   `sum_x |w(m_x)|^2 = |m_hat(q).eps|^2 <= |m_hat(q)|^2`.
3. So the expectation is bounded by `sum_(a,m) |m_hat(q)|^2 ||T_(a,m)||`,
   which is at most C_H |q|^4 by T2.
4. The first identity is the standard f-sum, obtained by expanding in the
   eigenbasis.

The fixed range and uniform norms make C_H finite and volume-independent. No
small-field expansion, clock character or lifting condition enters.

**Checks.**
- Check D verifies the operator identity and the eigenstate sum rule on
  10 qubits (dense), to residual 2e-14.
- The Fable check repeated it with spin-1 slots, +-2 shifts, E-dependent
  prefactors and complex couplings.

**Contrast with U(1).** A U(1) ring move keeps its first moment, the oriented
area. So its sum rule is O(q^2), consistent with a linear photon (check F).
The tensor rule removes the first moment too.

## T4 — what the sum rule allows (check G)

Take a ground state with nonzero positive weight in O_q and finite m_-1. The
landed exact chain gives, for the lowest excitation carrying that weight,

`omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0`,

and with T3:

`omega_min(q) <= q^2 sqrt(2 C_H / chi(q))`  and  `omega_min(q) <= C_H q^4 / S(q)`.

- **If chi(q) >= chi_0 > 0 at small q.** Then omega_min = O(q^2). This is
  the case in the linear comparator (chi = 1/J) and in every other
  comparator examined. It is an assumption about the state, not something
  proved for any qubit model.
- **If S is flat, as at a Rokhsar–Kivelson-type point.** Then
  omega_min = O(q^4).
- **If omega_min >= c|q|.** Then `chi(q) <= 2 C_H q^2 / c^2`. The bound
  `S(q) <= C_H q^3 / c` then follows, since S^2 <= m1 chi/2; it is not a
  separate condition.
  - That is two powers faster than the comparator's S ∝ q.
  - The electric weight of such a mode is O(q^3).
- **Limits.**
  - These are necessary conditions on the lowest weighted excitation. They
    do not establish a quasiparticle.
  - A suppressed chi is not sufficient for a light cone; a gapped channel
    has chi = O(q^4).
  - A linear mode above softer weight is not excluded.
- **Check G** illustrates this with Gaussian models on the qubit family's
  stiffness. Fixed chi gives omega ~ q^2 (fitted exponent 1.999).
  J(q) = 1/t gives omega ~ q (0.999), with S ~ q^3 and chi ~ q^2.
  The Gaussian corollary needs a positive, bounded, nonsingular electric
  stiffness.

## T5 — the linear comparator's sum rule is out of reach (check F)

The landed linear comparator H_N is quadratic, so its double commutator is a
c-number. On the TT modes it is g times the potential symbol, which is
Theta(t) = Theta(q^2). In the slot metric, the TT restriction of X_r over t
converges to 0.531 and 0.840. Its identities G_r X_r = 0 and
X_r M X_r = t X_r + s s^T/2 are re-verified.

Let pi = L E be a fixed, uniformly bounded, finite-range linear readout, so
that ||L(q)|| <= ||L||_1. Then `m1(eps.pi_q) <= ||L||_1^2 C_H |q|^4`. No such
readout reproduces the comparator's electric sum rule at small q. Check F
finds the ratio of the two stiffnesses falling with log-log slope 1.995.

The comparator's momentum could still be carried by any of these, all
outside the premises:
- a nonlinear or composite operator;
- an operator outside the diagonal-electric algebra;
- a non-local or size-dependent readout;
- size- or regulator-dependent couplings, which make C_H diverge;
- non-commuting or non-unit-spaced slots;
- a rule that holds only emergently or modulo N.

## T6 — the qubit family stiffens every physical mode as q^4 in the sampled directions (check E)

- **Family.** The two 20-slot witnesses, all 24 proper rotations and all
  translations.
- **Sampled directions.** On ker G(q) (three modes), all eigenvalues divided
  by q^4 converge and are positive in the 1503 directions sampled (a
  Fibonacci sphere plus the axes). The minimum leading coefficient is 16,
  reached on the coordinate planes.
  - The Fable check found the same minimum over 4010 directions plus local
    minimisation. The sol check found no zero in 5000 directions.
  - There is no analytic positivity certificate for every direction.
- **At q = 0.025:**
  - axis: 16, 128, 128;
  - face: 16, 80, 96;
  - body: 42.7, 42.7, 80;
  - generic: 20.2, 80.8, 91.8.
- **Along an axis, each family alone reaches only part.**
  - The planar block family stiffens only the plus shear and the scalar
    (rank 2), consistent with the landed "one branch vanishes on coordinate
    planes".
  - The 3D family stiffens only the cross shear (rank 1).

## What this means

Established:
- With one qubit per slot and the exact momentum rule, every term moves the
  electric pattern only at order q^2 per unit amplitude.
- The graviton channel's sum rule is therefore at most C_H q^4, in every
  eigenstate.
- The sampled move family stiffens all three physical modes at exactly that
  order.
- The potential side of the landed large-slot bound therefore has an exact
  qubit counterpart.
- The frequency conclusion still depends on the state, through chi.

Open routes. For a light-cone lowest mode under these premises, the
long-wavelength electric susceptibility must vanish like q^2. Otherwise:
- a light-cone mode must sit above softer electric weight;
- or the premises must fail: the exits listed in T5, a soft (energetic)
  rule, or clock aliasing.

None of these is excluded here. None is known to produce a light-cone
graviton on main.

Speculation, not consequence:
- **Incompressibility.** In a Gaussian comparator, chi ~ q^2 means an
  electric energy growing like 1/q^2. One conceivable local mechanism is the
  electric tensor sourcing a further long-range field. Outside the Gaussian
  ansatz, a vanishing chi can also come from selection rules or overlap
  suppression.
- **The owner's reading "time is the shifting or creation of records".**
  Reading the moves as record events has no bridge here, and conflicts with
  permanence. Whether a record-event clock (the lapse) could affect chi is
  an untested question. In the landed class, the energy rule lowers the
  frequencies further.

## No-Go Discipline Gate

The bounded negative claim: under the stated premises, the ground state's
lowest excitation carrying electric weight at small q obeys
omega_min <= q^2 sqrt(2 C_H/chi(q)). So a light-cone lowest mode requires
chi(q) = O(q^2).

- **N1 — attack routes against the stated implication.** Seven distinct
  routes. Each was either attempted here or is closed by a landed parent.
  1. *A kernel move with a surviving first moment.* It would make some
     active component O(q), and T3 would fail. ATTEMPTED. T2's proof, check C
     on witnesses and random combinations, and both referees' independent
     kernel vectors (nullspace, curl-curl, discrete-Airy) all have zero
     moments. The route fails.
  2. *A failure of the double-commutator identity beyond one qubit.* This
     means larger slots, E-dependent prefactors or complex couplings.
     ATTEMPTED: check D on 10 qubits, and the Fable check with spin-1 slots
     and +-2 shifts. The identity holds; the route fails.
  3. *Hidden size growth in C_H through the translation sum.* ATTEMPTED. The
     translates' phases cancel exactly (T3, step 2), and the Taylor bound
     holds on a zone grid for every sampled image (check E). With a fixed
     range and uniform norms, C_H is volume-independent. The route fails
     inside the premises.
  4. *A breakdown of the moment chain.* RULED OUT BY PRIOR: the landed
     2026-09-25 ring note proves the chain for any positive spectral measure
     with nonzero weight. Its hypotheses (nonzero weight, finite m_-1) are
     stated in T4.
  5. *A soft (energetic) rule in place of the exact one.* ATTEMPTED (check
     C). A single-slot change is not in ker G and keeps |m_hat|^2 = 1 as
     q -> 0, so the bound needs the exact term-by-term rule. The route
     escapes the domain; it is not a counterexample inside it.
  6. *Clock slots with a mod-N rule (aliasing).* RULED OUT BY PRIOR as a
     domain limit: the 2026-09-14 note shows that aliased characters need not
     lift. Unit-step spectra without wrap-around exclude it here.
  7. *Unbounded (oscillator) slots.* RULED OUT BY PRIOR as a domain limit:
     the 2026-09-24 oscillator note shows the linear comparator needs
     noncompact slots. It is outside the finite-dimensional premise.

  **Open routes the claim leaves.** These are consistent with it; they are
  not attacks on it.
  - (a) An incompressible gapless state inside the domain, chi = O(q^2).
  - (b) A linear mode above softer electric weight.
  - (c) A graviton momentum that is composite, non-diagonal or non-local
    (see T5).
- **N2 — pairwise table.** Four conditions.
  - W_a: chi bounded below. This is a property of the state, used only for
    omega_min = O(q^2).
  - W_b: the exact rule, term by term.
  - W_c: commuting, unit-step slots.
  - W_d: uniform finite C_H.

  | Pair | Closing the first closes the second? | Closing the second closes the first? | Relation |
  | --- | --- | --- | --- |
  | W_a, W_b | no: chi bounded below says nothing about which terms act, and soft-rule models can have it | unresolved: a counterexample would need an exact-rule model with nonzero weight and chi -> 0 (for example a gapped channel, where the chain gives chi <= 2 m1/Delta^2 = O(q^4)); none is constructed here. Diverging chi (RK type) satisfies W_a and does not decide this | unresolved |
  | W_a, W_c | no: the linear comparator has chi = 1/J with non-compact slots | unresolved, for the same reason | unresolved |
  | W_a, W_d | no: chi bounded below does not bound range or norms | unresolved, for the same reason | unresolved |
  | W_b, W_c | no: an exact rule can act on clock or oscillator slots | no: unit-step slots allow soft rules (route 5) | independent |
  | W_b, W_d | no: exact-rule terms can have unbounded range | no: bounded terms can violate the rule | independent |
  | W_c, W_d | no | no | independent |

  The collapsed set is three mutually independent domain premises (W_b, W_c,
  W_d) and one state condition (W_a). The state condition does not imply the
  premises. Whether the premises force chi to be bounded below is unresolved;
  a gapped exact-rule qubit model with nonzero weight would settle it in the
  negative. The theorem needs neither direction: W_a enters only the
  conditional omega_min = O(q^2). The negative conclusion itself has no
  further walls.
- **N3 — hidden conditions.** Several are now explicit in the premises and
  T4: term-by-term sector preservation, active components, volume-independent
  norms, and nonzero weight with finite m_-1. The Gaussian check G is an
  illustration and not load-bearing.
- **N4 — residual matching.**

  | Cited parent | Residual it supplies | Match for this use |
  | --- | --- | --- |
  | 2026-09-14 note | moment lemma | yes, reused as T2 |
  | 2026-09-14 note | its O(k^3) frequency bound (small-field class) | not used as a witness |
  | 2026-09-25 ring note | moment chain, a general spectral inequality | yes |
  | 2026-09-24 oscillator note | comparator symbol | yes, for T5 |
  | 2026-09-24 twelfth-order note | qubit moves | yes, for T1 |

- **N5 — rhetoric audit.** For "bounded by q^4":
  - per_element (each change pattern): tested;
  - per_site (the placement): tested;
  - per_mode (every unit polarisation and q): proved, and sampled;
  - per_block (dense 10-qubit and MILP boxes): tested;
  - lattice_wide: holds per unit cell whenever C_H is uniform; no phase is
    tested.

  "Light-cone mode needs incompressibility" is narrowed to the lowest mode
  carrying electric weight. The "one route left" wording of the first
  version is withdrawn.
- **N6 — partial closure.** The residual chi = O(q^2) is a dynamical property
  of a state. No labelling convention or reframing closes it. No primitive
  is invoked.
- **N7 — steelman.** The bound speaks only to the potential side and the
  lowest weighted mode. A linear graviton could exist with O(q^3) electric
  weight, or above softer modes, or not be carried by the slots' electric
  field at all. All three stay open.
- **N8 — cross-cycle echo.** Similar prior walls, and whether they were
  retired:
  - **The landed 2026-09-14 tensor note's linear-graviton wall.** Not
    retired. The 2026-09-24 oscillator note sharpened it to "both canonical
    variables noncompact"; T3 extends its potential side to qubits. There is
    no retirement mechanism to reuse.
  - **The U(1) lane's pure spin-1/2 photon wall** (#7959: omega about k^2 at
    L <= 12). It is not retired either. The mechanism it names for a
    retirement is an electric stiffness U > 0 supplied by matter or by
    larger link spin. That mechanism does not transfer. In U(1) a finite
    electric stiffness plus an O(q^2) sum rule gives a linear photon. Here
    the same finite stiffness plus an O(q^4) sum rule gives omega ~ q^2
    (T4). The tensor case needs the opposite, a vanishing electric
    susceptibility.
  - **Probe 6's naturalness wall** (a member on a fixed lattice). Different
    in kind; not applicable.
- **Outcome:** PASS as scoped. It is a bounded theorem with the open
  routes (a)–(c), not a closure of gravity as a pattern.

## What this does not show

It does not show any of these:
- a qubit ground state, or its chi(q) or S(q);
- a phase or a graviton;
- a box-free minimal move;
- an analytic positivity certificate for every direction;
- a model with chi = O(q^2);
- anything about the scalar (energy) rule beyond the landed results;
- anything about matter coupling;
- any link to the Admissibility axiom.

## Independent checks

- **Fable check** (Claude Fable 5.1): "CONFIRMED WITH CORRECTIONS".
  - It independently reproduced:
    - T2, on nullspace and curl-curl kernel vectors;
    - T3, including with spin-1 slots;
    - the T4 algebra;
    - the T5 identities;
    - T6, with minimum 16 over 4010 directions.
  - Its corrections, all applied:
    - "two powers faster", not three;
    - T2 labelled a re-verification of the landed lemma;
    - C_H regrouped by active change pattern;
    - "closes that gap" and "exact counterpart" narrowed to the potential
      side;
    - "necessary, not diagnostic".
- **Codex `gpt-5.6-sol`, first round: "STANDS WITH CORRECTIONS".**
  - It independently reproduced the witnesses, T2 (on discrete-Airy kernel
    vectors), the T3 algebra and constant, and T6's numbers, finding no zero
    in 5000 directions.
  - Its corrections, all applied:
    - T2 is landed prior art;
    - T3's hypotheses tightened: affine unit-step spectra, term-by-term
      sector preservation, active components, uniform C_H;
    - T4's S condition follows from chi, and the limits are stated;
    - T5 limited to fixed, uniformly bounded readouts, with the escapes
      listed;
    - T6 kept to the sampled directions;
    - the novelty stated as a synthesis;
    - the plain-language conclusions ("gravitons", "crawl", "one route
      left", the Coulomb reading, the record-event and time readings)
      narrowed or marked as speculation;
    - the No-Go gate rewritten in the required form.
- **Codex `gpt-5.6-sol`, second round: "NOT YET".**
  - Seven of its eight findings were resolved.
  - What remained was the gate's form: N1 needed five routes marked
    ATTEMPTED or RULED OUT BY PRIOR, N2 needed the pairwise table, and N8
    needed dispositions.
  - All three are now supplied. N1 has seven routes, and the open routes are
    listed separately. The soft-rule route was added to check C.
- **Codex `gpt-5.6-sol`, third round: "NOT YET".**
  - N1 and N8 are resolved.
  - In N2, its point was that diverging chi satisfies "chi bounded below",
    so it could not show that the premises fail to imply W_a.
  - Those three directions are now marked unresolved, with what would
    settle them, and no independence is claimed for them.

## Reproduction

`python3 scripts/one_qubit_per_slot_carries_the_tensor_momentum_rule_and_an_exact_q4_sum_rule_bounds_its_graviton_channel_2026_09_28.py`.
It prints 7 checks, A–G, the N5 lines and TOTAL, in about 35 s. The canonical
cache is at
logs/runner-cache/one_qubit_per_slot_carries_the_tensor_momentum_rule_and_an_exact_q4_sum_rule_bounds_its_graviton_channel_2026_09_28.txt.
