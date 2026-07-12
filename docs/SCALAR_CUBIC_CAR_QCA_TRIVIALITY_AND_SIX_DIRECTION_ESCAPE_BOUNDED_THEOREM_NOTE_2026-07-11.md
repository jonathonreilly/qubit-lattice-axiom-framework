---
claim_id: scalar_cubic_car_qca_triviality_and_six_direction_escape_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact Gaussian/CAR category bridge and one-mode classification with a six-mode escape. A supplied finite-range translation-invariant Laurent unitary lifts to a locality-preserving number-conserving CAR automorphism with an equally local inverse. With one fermionic mode per simple-cubic site, scalar unitarity makes the symbol a Laurent monomial and full proper-cubic covariance forces its winding to vanish, leaving only an onsite phase. A six-direction internal-mode permutation gives a nontrivial radius-one fully cubic CAR-QCA escape with zero total determinant winding. No classification or minimum is claimed for internal dimensions two through five, Bogoliubov/interacting qubit QCAs, record-forming processes, physical tick selection, clocks, or continuum limits."
upstream_dependencies:
  - minimal_axioms
runner: scripts/scalar_cubic_car_qca_triviality_six_direction_escape_2026_07_11.py
---

# Scalar Cubic CAR-QCA Triviality And The Six-Direction Carrier Escape

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
approved primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/scalar_cubic_car_qca_triviality_six_direction_escape_2026_07_11.py`](../scripts/scalar_cubic_car_qca_triviality_six_direction_escape_2026_07_11.py)

**Cached output:**
[`logs/runner-cache/scalar_cubic_car_qca_triviality_six_direction_escape_2026_07_11.txt`](../logs/runner-cache/scalar_cubic_car_qca_triviality_six_direction_escape_2026_07_11.txt)

## Question

The existing three-dimensional tick lane studies finite Laurent-unitary Bloch
matrices. When does such a one-particle tick define an actual local many-body
automorphism, and what does full proper-cubic covariance allow on the minimal
one-mode carrier?

The answer has two exact parts:

1. every finite-range unitary Laurent symbol has a canonical local
   number-conserving CAR-automorphism lift;
2. on one fermionic mode per simple-cubic site, full proper-cubic covariance
   makes that strict scalar tick transport-trivial.

A six-direction internal carrier then gives a nontrivial strict cubic escape.
Thus the result classifies the one-mode Gaussian/CAR carrier and supplies one
six-mode escape without pretending to classify intermediate carrier sizes or
all interacting qubit QCAs.

## Existing-science reading gate

The actual tick sources, runners, and live authority graph were read before
this attack.

- The approved
  [`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) provide the simple-cubic
  nearest-neighbor graph, proper cubic rotations, translations, and one-site
  `M_2(C)` possibility algebra. They provide no global tensor/CAR algebra,
  tick, automorphism, record-production process, or clock.
- The context-only
  `KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  and its runner were replayed at `PASS=20 FAIL=0`. Its exact results concern
  an `8 x 8` one-particle Bloch cell; its linear endpoint sweep is explicitly
  non-exhaustive and it is not a many-body QCA theorem.
- The later context-only
  `ETA_TWISTED_WALK_FAMILY_RIGID_DRIFT_DISCOVERY_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  exhibits curved dispersive one-particle walks under a twisted axis-permutation
  action. It remains unaudited and does not establish all 24 proper-cubic
  rotations or a CAR/QCA lift.
- The one-axis and all-finite-period tick dichotomies are exact conditional
  Laurent results but are unaudited and explicitly leave three-dimensional
  simultaneity and multicomponent carriers open.
- The audited-conditional tick/Admissibility rows still assume their physical
  realization predicate. No retained row selects a global coherent tick or
  computes a many-body QCA index.
- The preceding context-only
  `RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`
  classifies a Hermitian response symbol, not a strict unitary tick. It already
  warns that exponentiation generally spreads beyond one edge.

No prior negative tick result is imported as proof authority below. The CAR
lift, scalar classification, and carrier escape are proved directly.

## 1. Finite Laurent unitary to local CAR automorphism

Supply `s` fermionic modes per site on `Z^3`, with CAR generators
`a_(x,r)`, and a finite set `S subset Z^3`. Let

```text
U(k) = sum_(h in S) U_h exp(i k dot h),
U(k)^dag U(k) = U(k) U(k)^dag = I_s.                       (1)
```

Define

```text
alpha(a_(x,r))
 = sum_(h in S) sum_t (U_h)_(t r) a_(x+h,t).               (2)
```

Fourier coefficient comparison in (1) gives

```text
sum_h U_h^dag U_(h+delta) = delta_(delta,0) I_s,
sum_h U_h U_(h+delta)^dag = delta_(delta,0) I_s.            (3)
```

The first identity in (3) preserves the generator CAR and gives a star
endomorphism. The second is the coisometry/surjectivity identity; together
they make the endomorphism an automorphism. Its inverse has coefficients

```text
(U_inverse)_h = U_(-h)^dag,                                (4)
```

so if `S` has graph radius `R`, both `alpha` and `alpha_inverse` have radius
`R`. On a finite torus the coefficient matrix is an ordinary unitary and its
fermionic second quantization implements the same automorphism. On the
infinite lattice this statement is algebraic; it does not assume a global Fock
unitary in a chosen representation.

This is the category bridge missing from the older Bloch-only tick surfaces.
It is conditional on a supplied CAR realization. The local isomorphism between
one fermionic mode and `M_2(C)` does not derive the global graded CAR structure
from the Qubit axiom.

## 2. Scalar Laurent-unitary lemma

For one fermionic mode per site, `U(k)=u(k)` is scalar. If a finite Laurent
polynomial has modulus one on the connected torus, then it is a monomial:

```text
u(k) = exp(i phi) exp(i k dot w),       w in Z^3.            (5)
```

One proof fixes two torus variables. The remaining one-variable Laurent
polynomial is unimodular and hence a monomial. Its exponent is integer-valued
and locally constant in the fixed variables, hence constant on their connected
torus. Iterating over all variables leaves (5). Equivalently, the extreme
Fourier coefficients of `u conjugate(u)=1` give the same support collapse.

Equation (5) is an onsite phase followed by a rigid lattice translation. It is
already an exhaustive classification of finite-range translation-invariant
number-preserving Gaussian ticks on one mode per site.

## 3. Proper-cubic covariance kills scalar transport

For a scalar carrier, full proper-cubic covariance is

```text
u(R k) = u(k)                 for every R in O,              (6)
```

where `O` is the 24-element orientation-preserving cubic group. Substituting
(5) into (6) forces

```text
R^T w = w                 for every R in O.                 (7)
```

The proper-cubic vector representation has no nonzero invariant vector. The
runner stacks every exact integer matrix `R-I` and obtains rank three and zero
nullity. Therefore `w=0` and

```text
u(k)=exp(i phi),
alpha(a_x)=exp(i phi) a_x.                                 (8)
```

This is the exact one-mode scalar theorem:

> A finite-range, translation-invariant, number-preserving Gaussian/CAR tick
> with one fermionic mode per simple-cubic site and full proper-cubic
> covariance is an onsite phase and transports no support.

If onsite terms are disallowed, no such scalar unitary exists. Dropping cubic
covariance restores the six axis shifts. Dropping exact unitarity restores
nearest-neighbor scalar blends, but they are not ticks.

## 4. Determinant winding is only a coarse invariant

For an `s x s` finite Laurent unitary, the scalar monomial lemma applied to
the determinant gives

```text
det U(k) = exp(i Phi) exp(i k dot W),       W in Z^3.        (9)
```

Full proper-cubic covariance again forces `W=0`. This does not imply no
transport when `s>1`: the two-band symbol

```text
diag(exp(i k_1), exp(-i k_1))                              (10)
```

has determinant one and two oppositely moving bands. Thus total determinant
winding cannot replace a normal-form or carrier classification.

## 5. Six-direction strict cubic escape

Let the internal labels be the six directed nearest-neighbor vectors

```text
D={+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.                        (11)
```

Define the one-particle tick and its CAR lift by

```text
U |x,d> = |x+d,d>,
alpha(a_(x,d)) = a_(x+d,d).                                (12)
```

This update and its inverse have exact graph radius one. Translations commute
with it. Every proper cubic rotation acts by

```text
G_R |x,d> = |R x,R d>,
G_R U G_R^(-1)=U,                                          (13)
```

so (12) is a nontrivial simultaneous, translation- and proper-cubic-covariant
CAR QCA. Its six bands have windings `d in D`; their sum and determinant
winding vanish, but every band transports.

The orbit of any nearest-neighbor direction under the proper cubic group is
all six directions. Consequently six is the minimum internal multiplicity in
this transitive direction-permutation construction. Six fermionic modes have
local Fock dimension `2^6=64`, not the one-qubit dimension two. This is an
explicit larger-carrier escape, not a claim that every cubic CAR QCA needs six
modes. Spinor, staggered-cell, interacting, partitioned-circuit, and non-Gaussian
routes are outside this orbit-permutation lemma.

## 6. What is and is not closed

The exact finite hierarchy is

```text
one scalar mode + finite range + translations + full cubic covariance
  -> onsite phase only;

six direction-permuted modes + the same spatial symmetries
  -> nontrivial strict radius-one transport.                (14)
```

This establishes a carrier-cost fork. It does not select the six-direction
law, derive its internal labels, or prove that the framework must enlarge the
one-site carrier. Several live alternatives do not satisfy the scalar-Gaussian
hypotheses.

## Boundaries

- The lattice geometry comes from the minimal axioms; the global CAR algebra,
  mode count, linearity, number preservation, Laurent form, and physical tick
  interpretation are explicit conditional inputs.
- The supplied CAR realization is not inferred from the one-site `M_2(C)`
  presentation.
- The six-mode construction is a mathematical carrier escape, not a framework
  Record realization and not a selected matter law.
- The theorem does not classify all qubit QCAs, interacting fermionic QCAs,
  general Clifford QCAs, Margolus circuits, staggered `2^3` cells, aperiodic
  updates, CP instruments, or Hamiltonian exponentials.
- It does not derive the physical tick, probability rule, event rate, clock,
  arrow, QFT vacuum, statistics, Hamiltonian, action, or continuum limit.
- It does not establish that an axiom update is necessary. Direct
  Admissibility-to-update realization, partitioned circuits, larger cells,
  interacting automorphisms, and record-instrument dilations remain live.

## Falsifiers

- A non-monomial scalar finite Laurent polynomial of unit modulus on `T^3`.
- A nonzero integer vector fixed by all 24 proper cubic rotations.
- A scalar one-mode tick satisfying all hypotheses and transporting support.
- Failure of (2) to preserve CAR for a finite Laurent unitary.
- A proper cubic rotation or translation under which (12) is not covariant.
- A nonzero cubic displacement orbit with fewer than six elements, which would
  refute the stated orbit-permutation carrier minimum.

## Reproduction

```bash
python3 scripts/scalar_cubic_car_qca_triviality_six_direction_escape_2026_07_11.py
```

## Literature context, not a dependency

The external
[isotropic-quantum-walk classification](https://arxiv.org/abs/1708.00826)
finds the two cell-dimension-two three-dimensional Weyl walks on the
body-centered-cubic Cayley graph. A separate
[Gram-matrix paper](https://arxiv.org/abs/1703.05890) starts from that
body-centered-cubic graph and rederives the two automata; it is not an
independent selection of the graph. This context is consistent with the
carrier/adjacency fork here, but no external classification is used in the
proof.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  the simple-cubic lattice, nearest-neighbor adjacency, translations, proper
  cubic rotations, and one-site Qubit presentation. Every dynamical/CAR input
  is named separately above.

Context only: the existing 1D/all-period tick notes, the `2^3` simultaneous
Bloch-tick note, the eta-twisted discovery family, the July tick/Admissibility
conditional rows, and the cubic neighbor-response classifier. None is proof
authority for equations (1)--(14).
