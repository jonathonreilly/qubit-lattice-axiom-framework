---
claim_id: the_lambda_one_question_finite_dimensional_records_cannot_carry_einsteins_dewitt_kinetic_term_locally_it_could_only_be_emergent_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "On the landed tensor constraint complex (vector stencil G on electric slots, scalar stencil S on the conjugate slots, G S^T = 0), at linear order. (A) The DeWitt (lambda = 1) kinetic form M satisfies M s = G^T K and s.M.s = 0. On the momentum-constraint sector ker G(k) it is positive semidefinite, with exactly one zero, the scalar-gauge direction. Off the sector no finite penalty U|G|^2 makes it positive (landed determinant -J^2/2). So its obstacle is not positivity: it is invariant under the scalar (Hamiltonian-constraint) gauge only weakly. (B) Let the kinetic energy be a periodic function of the electric slots, a finite sum of characters (clock or compact slots). On the sector Lambda = ker_Z G, characters are defined modulo im(G^T), and e^{i r.s} does not depend on the representative. Distinct sector characters are independent, so weak invariance equals invariance of every character present. With lifted exponents, the landed symbol bound then gives kinetic characters of order k even for weak invariance, and the DeWitt form has no such realisation; this closes, under lifting, the landed 'every compact completion' question. For unbounded integer (rotor) electric values the DeWitt polynomial is exactly weakly invariant (checked on 200 integer sector states); a cosine completion is not. (C) The adiabatic (cranking) inertia of any positive system is a Gram form, positive semidefinite for any collective coordinates, so a collective metric's dilation inertia is never DeWitt's negative value. (D) One qubit per slot: the landed scalar-gauge pattern has entries of magnitude 1 and 4, so on two-level slots the exact scalar constraint exists only mod 2, with the 4s aliased away. Hence: the lambda = 1 kinetic structure needs unbounded local electric values, which one qubit per site does not have. With finite-dimensional records it could arise only as an emergent coarse-grained structure, with an emergent continuous Hamiltonian-constraint symmetry; that is neither constructed nor excluded here. Not shown: aliased (non-lifted) characters, non-perturbative or gapless-mediated effective theories, nonlinear order, the potential side beyond the landed bound."
upstream_dependencies:
  - minimal_axioms
runner: scripts/the_lambda_one_question_compact_records_cannot_carry_the_dewitt_structure_2026_09_28.py
---

# The λ = 1 question: finite-dimensional records cannot carry Einstein's DeWitt kinetic term locally; it could only be emergent

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** linear-order theorems on the landed constraint complex, with exact
checks; unaudited. Independent checks are recorded below.

## In one paragraph

Probe 12 left one question: Einstein's time constraint closes on the lattice
only at the DeWitt value λ = 1, while record-like kinetic energy has
λ < 1/3. Can positive record dynamics act like λ = 1?

- **Positivity is not the obstacle.** On the states that obey the momentum
  rule, Einstein's λ = 1 kinetic energy is already non-negative. It is zero
  only on the direction that the time constraint treats as pure gauge.
- **The obstacle is the kind of invariance.** That kinetic energy respects
  the time constraint only on those states, not everywhere. Such "weak"
  invariance needs unbounded local values: an integer per slot that can grow
  without limit.
- **On slots with a finite number of values, weak invariance collapses to
  full invariance.** The landed result then forces the kinetic energy to be
  soft. So λ = 1 cannot be written down locally on finite slots.
- **A collective version cannot come from ordinary inertia.** Averaging over
  a positive system always gives positive inertia.
- **On one qubit per slot, Einstein's time constraint exists only in a
  scrambled, mod-2 form.**

So λ = 1 is not impossible for records, but it cannot be local and
microscopic. It could only emerge at a coarse scale, together with an
emergent time-constraint symmetry. Whether records can do that is the open
question this narrows to.

## Prior art

On main, read before this note:
- **The 2026-09-14 tensor note:** the constraint complex G, S, G S^T = 0, and
  the regular compact-character bound. Its words: "A periodic replacement
  must be checked as its own Hamiltonian".
- **The 2026-09-24 oscillator note:** M s_r = G_r^T K, and the DeWitt form's
  weak invariance; "a tested cosine replacement fails scalar invariance,
  without excluding every compact completion".
- **The 2026-09-24 synthesis note:** "They do not prohibit every compact
  completion".
- **The 2026-09-25 clock-profile note:** closure only on β = −α (λ = 1). T4
  there shows the walker sea's adiabatic inertia is positive, a concrete
  case of C here.
- **Probes 10–12 of this PR.**

T2 of this note (B) closes, under lifting, the landed notes' open "every
compact completion" question. The rest re-expresses or generalises landed
facts.

Reference only: Dirac/Bergmann constraint theory; the Inglis cranking
formula.

## Premises

- **The landed tensor complex** on the doubled lattice: electric slots E, the
  vector stencil G (the momentum rule), the scalar stencil S (the
  Hamiltonian-constraint density on the conjugate slots), and the DeWitt
  form M = diag(1,1,1,2,2,2) − vv^T/2.
  - The scalar-gauge shift of E generated by exp(iβ S·q) is S^T δ_y.
- **Linear order.**
- **Compact/clock slots:** the kinetic energy is a finite sum of characters
  e^{i r·E}. *Lifted* means the exponent bounds of the landed note, so that
  invariance modulo 2π implies exact invariance.
- **Rotor slots:** E integer and unbounded.

## A — the DeWitt form is positive on the sector; only its invariance is weak (check A)

Over 20 random zone momenta:
- M s = G^T K and s·M·s = 0;
- on ker G(k) (three dimensions), M has eigenvalues (0, positive, positive).
  The zero is the scalar-gauge direction; at q = (0.3, 0.2, 0.4) they are
  (0, 1.264, 1.787);
- off the sector, M + U G^T G has a negative eigenvalue for U = 1, 10^3 and
  10^6 (−0.42, −2e-3, −2e-6), which tends to 0 from below, as the landed
  determinant −J^2/2 requires.

So on physical (momentum-rule) states the λ = 1 kinetic term is positive;
its indefiniteness lives off the sector. Its scalar-gauge invariance,
M(E + s) − M(E) = 2⟨G E, K⟩, holds only on the sector: weak invariance.

## B — weak = strong for periodic kinetic energies (check B)

**Statement.** Let f(E) = Σ_r a_r e^{i r·E} be a finite character sum, and
let Λ = ker_Z G, or a coset of it for a static background.

f is weakly invariant, meaning f(E + s_y) = f(E) for all E ∈ Λ and every
scalar pattern s_y, **iff** every sector class [r] with nonzero total
weight satisfies e^{i r·s_y} = 1.

With lifted exponents, the landed symbol argument then applies to those
characters: (k^2 δ − kk):r(k) = 0 forces r(0) = 0. So the kinetic
characters are O(k), exactly as for strong invariance.

**Proof.**
1. On Λ, e^{i r·E} depends only on the class
   r mod (2πZ^n + im_R G^T), because Λ is saturated and its dual is the
   projection of Z^n.
2. e^{i r·s} is class-independent, since G s = 0.
3. Distinct characters of the abelian group Λ are linearly independent.
4. So f(E + s) − f(E) = Σ_[r] A_[r] e^{i r·E}(e^{i r·s} − 1) vanishes on Λ
   iff each class term vanishes. ∎

**Checks** (3^3 torus, landed stencils).
- G S^T = 0.
- 200 integer sector states, built from 108 kernel generators (planar moves
  and scalar patterns).
- The DeWitt polynomial is exactly invariant: max |DW(E+s) − DW(E)| = 0.
  That is a rotor (unbounded integer) realisation.
- A cosine completion at θ = 2π/101 is not invariant (difference 351).
- Representative-independence of e^{i r·s} and e^{i r·E} holds.

**Consequence.** The λ = 1 kinetic structure has no local realisation on
compact slots with lifted characters, even weakly. It needs unbounded local
electric values (rotor or oscillator slots). One qubit per site (M_2(C))
has none.

## C — collective inertia is positive (check C)

For any positive system and collective coordinates X_a, the adiabatic
inertia `M_ab = 2 Σ_n Re⟨0|X_a|n⟩⟨n|X_b|0⟩/(E_n − E_0)^3` is a Gram form,
so it is positive semidefinite. Across 50 random Hamiltonians with 4
coordinates each, the smallest eigenvalue is 0.093.

So a collective metric's dilation inertia is ≥ 0. It is never DeWitt's
3α + 9β = −6α (at β = −α).

The landed walker-sea inertia (2026-09-25, T4) is one instance.

A collective λ = 1 would therefore have to freeze the dilation (an emergent
constraint), not give it negative inertia.

## D — one qubit per slot aliases the scalar constraint (check D)

The landed scalar-gauge pattern S^T δ has 27 nonzero entries, of magnitude
1 and 4 (the centre's three diagonal slots carry −4).

On two-level slots the shift by it is unitary only as a Z_2 (mod-2) clock
operator. There the three −4 entries alias to zero, and 24 entries remain.
The landed lifting condition (N > 36M) fails.

So on one qubit per slot the continuous Hamiltonian constraint cannot be
imposed exactly. Only a discrete, aliased version exists.

## What this means

For the owner's question: positive record dynamics cannot act like λ = 1
locally.
- The DeWitt kinetic term needs unbounded local values (B).
- Collective inertia cannot supply it (C).
- One-qubit slots cannot even carry the continuous time constraint (D).

What remains is emergence: a coarse-grained description in which
- the electric variables are effectively unbounded;
- a continuous Hamiltonian-constraint symmetry emerges;
- the dilation is frozen by it (A shows that positivity then costs nothing).

Emergent gauge structure from finite-dimensional systems is common: the
emergent U(1) photon of spin ice is an example. An emergent *time*
(Hamiltonian-constraint) symmetry from records is not known, and is not
constructed here.

Remark, not claimed: at linear order, positive kinetics together with
*second-class* scalar constraints also leave only the TT modes. But the
transverse-traceless projection is non-local, so that route trades λ = 1
for non-locality.

## No-Go Discipline Gate

The bounded negative claims:
- (B) on compact slots with lifted characters, no kinetic energy is weakly
  but not strongly scalar-invariant on the momentum sector, so the DeWitt
  form has no local compact realisation;
- (C) collective adiabatic inertia of a positive system cannot be DeWitt's.

- **N1 — attack routes.**
  1. *A periodic completion that is invariant only on the sector.*
     ATTEMPTED (B): the theorem, plus a cosine counterexample.
  2. *Unbounded integer (rotor) slots.* ATTEMPTED (B): the DeWitt
     polynomial works. Outside the finite-dimensional premise.
  3. *Collective inertia from integrating out a positive sector.* ATTEMPTED
     (C): a Gram form, so positive.
  4. *Energetically enforced constraints* (Schrieffer–Wolff return words).
     RULED OUT BY PRIOR (2026-09-14): the return words commute with the
     constraints exactly, and B shows weak invariance adds nothing.
  5. *The time constraint on one-qubit slots.* ATTEMPTED (D): it exists
     only mod 2.

  **Open routes left** (not attacks on the claims):
  - aliased (non-lifted) characters;
  - non-perturbative or gapless-mediated non-local effective theories;
  - an emergent continuous Hamiltonian-constraint symmetry at a coarse
    scale;
  - second-class scalar constraints with a non-local TT projection.
- **N2 — conditions.**
  - Lifting and finite range are the premises of B. Positivity is the
    premise of C. The premises are independent: rotors violate B's
    compactness but satisfy C's positivity.
  - Whether emergence can evade both is unresolved.
- **N3 — hidden conditions.** Linear order; the landed stencils; a 3^3
  torus for the integer checks (the theorem itself is general); lifted
  exponents.
- **N4 — residual matching.**
  - The landed symbol bound: used for lifted characters. Match yes.
  - The landed return-word statement: used for route 4. Match yes.
  - The landed walker-sea inertia: an instance of C. Match yes.
- **N5 — rhetoric audit.**
  - "Cannot carry locally" is scoped to compact slots with lifted
    characters (per element: each character; lattice-wide: the class
    theorem).
  - "Could only be emergent" names the open route, not a proof of
    impossibility.
- **N6 — partial closure.** No convention supplies unbounded local values
  or an emergent time symmetry.
- **N7 — steelman.** A strongly interacting record phase might have
  effectively unbounded coarse electric fields and an emergent continuous
  time-constraint symmetry, as spin ice has an emergent U(1). This is the
  open route; it is not excluded.
- **N8 — cross-cycle echo.**
  - Landed: the compact bound; "every compact completion" (closed under
    lifting here); the sea's inertia.
  - Probe 12: the lapse on λ = 1.
- **Outcome:** PASS as scoped.

## What this does not show

It does not show any of these:
- that emergent λ = 1 is impossible;
- anything about aliased characters, non-perturbative phases or nonlinear
  order;
- the potential (Einstein–Hilbert) side beyond the landed bound;
- matter coupling;
- which reading the axioms intend.

## Independent checks

Pending.

## Reproduction

`python3 scripts/the_lambda_one_question_compact_records_cannot_carry_the_dewitt_structure_2026_09_28.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in under 1 s. The canonical
cache is at
logs/runner-cache/the_lambda_one_question_compact_records_cannot_carry_the_dewitt_structure_2026_09_28.txt.
