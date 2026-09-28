---
claim_id: the_lambda_one_question_the_dewitt_form_is_positive_on_the_momentum_sector_weak_invariance_adds_nothing_in_lifted_clock_encodings_finite_slots_need_a_non_additive_time_gauge_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Partial answer to the lambda = 1 question, on the landed tensor constraint complex (vector stencil G on the electric slots, scalar stencil S on the conjugate slots, G S^T = 0), at linear order. (A) For momentum k != 0, the DeWitt (lambda = 1) kinetic form M is positive semidefinite on the momentum-constraint sector ker G(k), with exactly one zero, the scalar-gauge direction. It is invariant under the scalar gauge only weakly (M(E+s) - M(E) = 2<GE, K>). No finite penalty U|G|^2 makes it positive off the sector. At k = 0 the uniform dilation lies in ker G and is negative, the homogeneous conformal mode. (B) For a kinetic energy that is a finite sum of characters (clock or compact electric slots), on the sector ker G, or mod N for clocks: characters are defined modulo im(G^T), e^{i r.s} does not depend on the representative, and weak invariance constrains every class with nonzero total weight. Under the landed regularity hypotheses (lifted exponents, translation invariance, uniform locality or summable moments), the landed O(k) kinetic bound therefore also holds for weak invariance. This closes only the lifted regular clock class; aliased characters, non-diagonal or nonlinear realisations and added fields remain open. The DeWitt polynomial is exactly invariant under the discrete integer shifts on integer sector states (rotor slots); only oscillator slots realise the continuous shift. (C) The adiabatic (cranking) inertia of a gapped positive system is a Gram form (standard). It cannot supply a physical negative dilation inertia. It does not obstruct a gauge-redundant DeWitt structure, whose negative direction is pure gauge. (D) In the canonical Weyl (clock) encoding on two-level slots (six slots per cell in the supplied model, not the axioms' one qubit per site), the landed scalar-gauge pattern (entries of magnitude 1 and 4 on tori of side >= 3) exists only mod 2, with the 4s aliased. (E) On a finite-dimensional slot no Hermitian generator shifts the electric value additively ([S, E] = i s 1 is traceless on the left, not on the right). So an exact continuous scalar gauge on finite records must act non-additively, as quantum-link models realise continuous gauge symmetry; whether a quantum-link realisation of the Hamiltonian constraint with DeWitt structure exists is open. The lambda = 1 question is therefore not decided."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
runner: scripts/the_lambda_one_question_what_the_dewitt_kinetic_structure_needs_on_the_tensor_complex_2026_09_28.py
---

# The λ = 1 question, in part: the DeWitt form is positive on the momentum sector; weak invariance adds nothing in lifted clock encodings; finite slots need a non-additive time gauge

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a partial answer; linear-order lemmas on the landed tensor
complex, with exact checks; unaudited. This is a narrowed revision. The
first version claimed that finite-dimensional records cannot carry λ = 1
locally. That overreached; see Independent checks.

## In one paragraph

Probe 12 left this question: Einstein's time constraint closes on the lattice
only at the DeWitt value λ = 1, while record-like kinetic energy has
λ < 1/3. Can positive record dynamics act like λ = 1? This note settles part
of it.
- **At nonzero momentum, positivity is not the obstacle.** On states obeying
  the momentum rule, the λ = 1 kinetic energy is non-negative; it is zero
  only on the direction the time constraint treats as gauge. The uniform
  (k = 0) dilation is the exception.
- **The DeWitt kinetic energy respects the time constraint only on those
  states** (weak invariance).
- **In the natural "clock" encodings of finite slots, weak invariance buys
  nothing.** The landed result then keeps the kinetic energy soft.
- **On any finite-dimensional slot, no continuous time symmetry can shift the
  electric value by a constant.** So a finite-record version would need a
  subtler, non-additive action, of the kind quantum-link models use for
  their exact continuous gauge symmetries.

Whether such a quantum-link version of Einstein's time constraint exists is
open. So λ = 1 for finite records is neither shown possible nor ruled out.

## Prior art

On main, read before this note:
- **The 2026-09-14 tensor note:** the constraint complex, the regular
  compact-character bound, and the Schrieffer–Wolff return words.
- **The 2026-09-24 oscillator note:** M s_r = G_r^T K, weak invariance, "a
  tested cosine replacement fails scalar invariance, without excluding every
  compact completion".
- **The 2026-09-24 synthesis note:** "They do not prohibit every compact
  completion".
- **The 2026-09-25 clock-profile note:** closure only on β = −α (λ = 1); the
  walker sea's adiabatic inertia is positive.
- **Probes 10–12 of this PR.**

External, reference only:
- B's group step is standard Pontryagin duality (annihilators) plus the
  linear independence of characters. Weak invariance on a stabilizer code
  space is the familiar coset structure of logical operators.
- C is the standard Inglis cranking formula (Ring–Schuck).
- The homogeneous conformal-mode negativity is Gibbons–Hawking–Perry.
- Chandrasekharan and Wiese (hep-lat/9609042) give quantum link models,
  with finite-dimensional links and exact continuous gauge invariance.
- Hořava and Melby-Thompson (2010) give a U(1) extension that removes the
  scalar graviton and forces λ = 1; da Silva (2011) extends it to any λ.
  These are local extra-field routes.

What is specific here:
- the application to the tensor complex;
- the closure of the lifted regular clock class;
- the trace lemma's consequence for finite records.

## Premises

- **The landed complex:**
  - electric slots E;
  - the vector stencil G (the momentum rule);
  - the scalar stencil S on the conjugate slots;
  - the DeWitt form M = diag(1,1,1,2,2,2) − vv^T/2;
  - the scalar-gauge E-shift S^T δ_y.
- **Linear order.**
- **B also assumes** the landed regularity hypotheses: lifted exponents,
  translation invariance, uniform locality or summable moments, and a
  smooth small-field expansion.

## A — for k ≠ 0 the DeWitt form is positive on the momentum sector (check A)

- Over 20 zone momenta, M s = G^T K and s·M·s = 0.
- On ker G(k) the eigenvalues are (0, positive, positive); the zero is the
  scalar-gauge direction. Rotated to k ∥ z, the form on ker G is
  (1/2)(E_xx − E_yy)^2 + 2E_xy^2 (sol).
- Off the sector, M + U G^T G keeps a negative eigenvalue that tends to 0
  from below (−0.42, −2e-3 and −2e-6 at U = 1, 10^3 and 10^6), as the
  landed determinant −J^2/2 requires.
- At k = 0 the uniform dilation lies in ker G with M-value −1/2 per unit
  norm: the homogeneous conformal mode. The positivity statement needs
  k ≠ 0.

## B — weak = strong, class by class, in lifted clock encodings (check B)

**Statement.** Let f = Σ_r a_r e^{i r·E} be a finite character sum. Work on
Λ = ker_Z G, or on the modular sector ker(G mod N) for clocks, or on a coset
E_0 + Λ of either (a static background).
- f is weakly invariant under the scalar gauge iff every sector class with
  nonzero total weight has e^{i r·s_y} = 1.
- On a coset, the class weight is phase-weighted: Σ_{r∈[r]} a_r e^{i r·E_0}.
- A class whose total weight is zero is unconstrained. For example,
  χ_r − χ_{r+G^Tξ} vanishes on the sector although χ_r alone is not
  invariant (check B).
- Under the landed regularity hypotheses, the class sums therefore obey the
  landed symbol bound, so the kinetic characters are O(k).

**Proof.**
1. Λ is saturated. Its annihilator is 2πZ^n + im_R G^T; for clocks, mod N,
   (ker A)^⊥ = im A^T by Pontryagin duality.
2. e^{i r·s} is class-independent, because G s = 0.
3. Distinct characters of Λ are linearly independent. ∎

**Checks.**
- G S^T = 0.
- On 200 integer sector states the DeWitt polynomial is exactly invariant
  under the discrete integer shifts. The real-space identity is
  M S^T = G^T W with S M S^T = 0.
- A cosine completion is not invariant.
- The class independence holds, including mod 101.

**Scope.** This closes the landed "every compact completion" question only
for lifted, regular, diagonal clock characters. Still open:
- aliased characters;
- infinite or non-regular sums;
- non-diagonal or nonlinear realisations;
- added fields.

On rotors the DeWitt polynomial is invariant under the discrete shifts only.
Only oscillator slots realise the continuous linear shift.

## C — cranking inertia is a Gram form (check C; standard)

For a gapped positive system with Hermitian collective forces X_a, the
adiabatic inertia `2 Σ_n Re⟨0|X_a|n⟩⟨n|X_b|0⟩/(E_n − E_0)^3` is positive
semidefinite. Over 50 random systems the smallest eigenvalue is 0.11.
- So it cannot supply a *physical* negative dilation inertia.
- DeWitt's negative direction is pure gauge (fixed by the Hamiltonian
  constraint), not a physical collective coordinate. So C does not obstruct
  a gauge-redundant DeWitt structure.
- Its content is only this: in a positive system the dilation must be
  gauge-frozen, not given negative inertia.

## D — the canonical Weyl encoding on two-level slots aliases the scalar constraint (check D)

- The landed scalar-gauge pattern has entries of magnitude 1 and 4 on tori of
  side ≥ 3; side 2 degenerates.
- In the canonical Weyl (clock) encoding on two-level slots, the 4s alias to
  zero mod 2 and 24 of 27 entries survive.
- This is one encoding of six slots per cell. It is not the axioms' one qubit
  per site, and it does not exclude other qubit realisations.

## E — finite slots cannot shift the electric value additively (check E)

- On a d-dimensional slot, [S, E] = i s·1 is impossible for Hermitian S: the
  left side is traceless, the right side has trace i s d.
- So an exact continuous scalar gauge on finite records cannot act by the
  additive shifts E → E + βs that the DeWitt weak-invariance identity uses.
- It must act non-additively, as in quantum link models, where [E, U] = U
  with U a raising operator.
- Rotors give only discrete integer shifts.

## What this means

For the owner's λ = 1 question:
- **A:** positivity is not the obstruction on the constraint sector (k ≠ 0).
- **B:** the natural clock encodings cannot carry the DeWitt structure, even
  weakly.
- **E:** a finite-record realisation of Einstein's time constraint would have
  to act non-additively, quantum-link style.

Still open:
- a quantum-link realisation of the tensor complex's Hamiltonian constraint
  with DeWitt structure;
- local extra-field routes of the Hořava–Melby-Thompson kind;
- aliased or non-regular realisations;
- collective emergence (for example large-spin, semiclassical).

The next test this points to: build the quantum-link version of the
scalar constraint on the tensor complex, and ask whether its linearisation
has the DeWitt kinetic structure.

## No-Go Discipline Gate

The bounded negative claims:
- (B) in lifted regular clock encodings, weak scalar invariance adds nothing
  beyond class-wise strong invariance, so the landed O(k) bound holds;
- (E) no finite-dimensional Hermitian generator shifts E additively.

- **N1 — attack routes.**
  1. *A periodic completion invariant only on the sector.* ATTEMPTED (B):
     the class theorem and a cosine counterexample.
  2. *Zero-total-weight classes.* ATTEMPTED (B): unconstrained, but they
     vanish on the sector, so they carry no kinetic energy there.
  3. *The clock (mod N) sector.* ATTEMPTED (B): Pontryagin version, checked
     mod 101.
  4. *Energetically enforced constraints* (return words). RULED OUT BY PRIOR
     (2026-09-14): the return words commute exactly, and B adds that weak
     commutation gains nothing in this class.
  5. *An additive continuous generator on finite slots.* ATTEMPTED (E):
     impossible, by trace.

  **Open routes left:** quantum-link (non-additive) realisations; aliased
  characters; local extra fields; collective emergence.
- **N2 — conditions.** Lifting and regularity (for B) and finite dimension
  (for E) are independent premises. Rotors escape E but only have discrete
  shifts. No independence claim is made about the open routes.
- **N3 — hidden conditions.** Linear order; k ≠ 0 for A; the landed
  stencils; tori of side ≥ 3 for D.
- **N4 — residual matching.**
  - The landed symbol bound: used only under its own hypotheses.
  - The landed return words: route 4.
  - The walker-sea inertia: an instance of C.
- **N5 — rhetoric audit.**
  - The title's "adds nothing" is scoped to lifted clock encodings.
  - "Need a non-additive time gauge" is the trace lemma.
  - No impossibility claim is made for finite records.
- **N6 — partial closure.** No convention supplies a non-additive time gauge;
  that is a construction question.
- **N7 — steelman.** Quantum-link models have exact continuous gauge
  invariance with finite links. A quantum-link Hamiltonian constraint on the
  tensor complex might carry the DeWitt structure. This is open, and it is
  the next test.
- **N8 — cross-cycle echo.**
  - The landed "every compact completion" question: closed here for lifted
    regular clocks only.
  - The U(1) lane already uses quantum links for the momentum-type (Gauss)
    rule.
- **Outcome:** PASS as scoped.

## What this does not show

It does not show any of these:
- that λ = 1 is impossible for finite records;
- anything about quantum-link, aliased or collective realisations;
- nonlinear order;
- the Einstein–Hilbert potential side beyond the landed bound;
- matter coupling.

## Independent checks

- **First version** (d1ddd4ce10), titled "finite-dimensional records cannot
  carry Einstein's DeWitt kinetic term locally; it could only be emergent".
  - **Codex `gpt-5.6-sol`: "FAILS".** Its critical point: the headline did
    not follow. Finite records are not necessarily diagonal clock
    characters, and quantum-link models realise exact continuous gauge
    symmetry with finite links. It also required:
    - k ≠ 0 in A;
    - "modulo the sector-null ideal" in B;
    - the landed regularity hypotheses for the O(k) inheritance, so only the
      lifted regular class is closed;
    - the rotor claim restricted to discrete shifts;
    - C scoped: it does not obstruct a gauge-redundant DeWitt structure;
    - D scoped as one encoding, torus-size dependent;
    - the dependency list and novelty statements corrected.
  - **Fable check (Claude Fable 5.1): "CONFIRMED WITH CORRECTIONS".** Its
    points:
    - the k = 0 dilation is negative;
    - the class-weight counterexample;
    - the clock (mod N) version of B;
    - rotors carry the DeWitt polynomial but not the λ = 1 structure;
    - the 108 generators span 60 of the 84 kernel dimensions;
    - C is a tautology of the Inglis formula;
    - D is size-independent for L ≥ 3, and one encoding only;
    - the quantum-link route and Hořava–Melby-Thompson / da Silva are
      unnamed.
- **This revision.** It applies all of the above, adds the trace lemma (E),
  and retitles the note to the partial answer.

- **Codex `gpt-5.6-sol`, second round: "NOT YET".** Seven of its eight
  findings were resolved, and check E was "valid as scoped". The remaining
  item: on a coset, the class weight must carry the background phase. That
  is now stated in B.

## Reproduction

`python3 scripts/the_lambda_one_question_what_the_dewitt_kinetic_structure_needs_on_the_tensor_complex_2026_09_28.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in under 1 s. The canonical
cache is at
logs/runner-cache/the_lambda_one_question_what_the_dewitt_kinetic_structure_needs_on_the_tensor_complex_2026_09_28.txt.
