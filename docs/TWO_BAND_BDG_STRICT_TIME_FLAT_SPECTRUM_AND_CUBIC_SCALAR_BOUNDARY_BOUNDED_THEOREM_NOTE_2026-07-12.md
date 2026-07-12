---
claim_id: two_band_bdg_strict_time_flat_spectrum_and_cubic_scalar_boundary_bounded_theorem_note_2026-07-12
claim_type: bounded_theorem
claim_scope: "Exact finite-Laurent two-band generator theorem and scalar one-mode proper-cubic nearest-neighbor BdG corollary. For any supplied 2x2 torus-Hermitian finite Laurent generator H and nonzero real t0, exp(-it0 H) is finite Laurent iff H has momentum-independent eigenvalues; equivalently strict once iff flat spectrum iff strict for every time. Separately, the endpoint-SWAP-symmetric parity-preserving two-qubit spin density is six-dimensional, with two charge-breaking pairing directions, but it is not identified with a local Z3 CAR/BdG density. On a separately supplied spinless one-mode CAR/Nambu carrier with scalar proper-cubic onsite action and nearest-neighbor range, odd pairing is killed and flatness forces the normal hopping to vanish, leaving only onsite flow. A lower-symmetry Kitaev involution and the existing doubled 16-mode cubic flat involution are positive escapes. CAR/Nambu realization, particle-hole convention, generator, time, carrier dimension, range, symmetry action, physical selection, Record coupling, probability, and continuum scaling are supplied or open."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_band_bdg_strict_time_flat_spectrum_2026_07_12.py
---

# Two-Band BdG Strict-Time Flat-Spectrum and Cubic-Scalar Boundary

**Date:** 2026-07-12

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/two_band_bdg_strict_time_flat_spectrum_2026_07_12.py`](../scripts/two_band_bdg_strict_time_flat_spectrum_2026_07_12.py)

**Cached output:**
[`logs/runner-cache/two_band_bdg_strict_time_flat_spectrum_2026_07_12.txt`](../logs/runner-cache/two_band_bdg_strict_time_flat_spectrum_2026_07_12.txt)

## Question and exact bounded answer

Does the charge-breaking/Bogoliubov complement of the preceding
onsite-charge theorem contain a dispersive two-band Hamiltonian whose
exponential becomes an exactly finite-radius Gaussian QCA at one exceptional
nonzero time?

For the complete `2 x 2` finite-Laurent generator class, the answer is no.
Let

```text
H(z) in M_2(C[z_1^+-1,z_2^+-1,z_3^+-1])                 (1)
```

be Hermitian on the unit three-torus, and let `t_0` be real and nonzero. Then

```text
exp(-i t_0 H(z)) is finite Laurent
    iff H(z) has momentum-independent eigenvalues
    iff exp(-i t H(z)) is finite Laurent for every real t. (2)
```

Thus, inside this supplied two-band Gaussian class,

```text
strict once  <=>  flat two-band spectrum  <=>  strict for all times. (3)
```

There is no isolated strict time. Flat-band Hamiltonians are the exact positive
escape, not an exception hidden by the proof.

A second result closes the smallest fully cubic pairing carrier. On a supplied
spinless one-mode CAR algebra per simple-cubic site, with scalar onsite action
of all `24` proper cubic rotations and nearest-neighbor range, fermionic
antisymmetry and cubic covariance kill every pairing coefficient. The surviving
cubic normal hopping is dispersive unless it vanishes. Therefore a strict
finite-time exponential in this minimal class is onsite only.

Neither result is a theorem about all endpoint-symmetric qubit Hamiltonians,
all multiband BdG systems, interacting QCAs, partitioned ticks, or quasilocal
continuum flows.

## Existing-science reading gate

The actual branch and current repo sources were read before selecting this
target.

- The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the cubic lattice
  and one-site `M_2(C)` presentation, but no global CAR algebra, Jordan--Wigner
  convention, Hamiltonian, Nambu doubling, particle-hole law, time, or dynamics
  selector.
- The preceding
  [onsite-charge common-Hamiltonian dichotomy](ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  classifies the full charge-preserving one-qubit edge density and explicitly
  leaves charge-breaking/BdG densities open. It also supplies the doubled
  `16`-mode flat-involution escape that prevents a broader noncommuting-tail
  no-go.
- The
  [scalar cubic CAR-QCA theorem](SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  proves only the number-preserving scalar Laurent class and explicitly leaves
  Bogoliubov mixing and intermediate carrier dimensions open.
- The repository's Majorana/Nambu notes, including
  [the Nambu source principle](NEUTRINO_MAJORANA_NAMBU_SOURCE_PRINCIPLE_NOTE.md),
  use a finite local two-mode pseudospin/source grammar. They do not supply a
  translation-invariant local `Z^3` CAR dynamics or identify a two-qubit spin
  edge with a local BdG edge.
- The exact-log transfer sources distinguish finite range from exponential
  quasilocality. That distinction becomes decisive for the continuum campaign:
  a dispersive relativistic generator should not be required to have a strict
  exponential at finite physical time.

Those sources determine the category boundary and the open residual. Equations
(1)--(16) below are self-contained. The only declared graph dependency is
`minimal_axioms`; all CAR/BdG structure is a named conditional input.

## 1. Spin-edge parity class: six real directions, not yet BdG

First classify what the literal two-qubit tensor carrier says. Rotate a supplied
parity axis to `Z` and impose

```text
SWAP h SWAP = h,                 [h, Z tensor Z] = 0.      (4)
```

The parity-even basis states are `|00>,|11>` and the parity-odd states are
`|01>,|10>`. Endpoint SWAP is the identity on the even block and Pauli `X` on
the odd block. Hence the even block is an arbitrary Hermitian `2 x 2` matrix
(`4` real coordinates), while the odd block is the real span of `I,X`
(`2` coordinates). Equivalently every density under (4) is uniquely

```text
h = c II + r(ZI+IZ) + g ZZ + J(XX+YY)
      + Delta_1(XX-YY) + Delta_2(XY+YX),                  (5)
```

with six real coefficients. The first four terms conserve `ZI+IZ`. The last
two preserve parity but change the charge by two and are the two real pairing
directions.

Equation (5) is a spin-tensor theorem only. In one spatial dimension a chosen
Jordan--Wigner order can turn selected spin strings into local CAR terms. On
`Z^3`, no such local qubit-to-CAR identification is supplied by the axioms or
by the current repository. An arbitrary placement of (5) on cubic spin edges
must therefore not be called a local BdG Hamiltonian without a separately
declared graded carrier and locality bridge.

## 2. Two-band finite-Laurent theorem

Assume now, separately, a supplied two-component Laurent carrier. No
particle-hole condition is needed for the matrix theorem itself. Write

```text
a(z) = (1/2) tr H(z),             D(z) = H(z)-a(z)I,
s(z) = (1/2) tr(D(z)^2).                                  (6)
```

Then `D` is traceless. Cayley--Hamilton gives

```text
D(z)^2 = s(z) I.                                          (7)
```

On the unit torus, Hermiticity makes `a` real and `s>=0`.

### 2.1 Finite exponential forces constant trace

Suppose `U_0(z)=exp(-i t_0 H(z))` is finite Laurent. Its determinant is a
scalar Laurent polynomial of unit modulus on the torus. A scalar
multivariable Laurent polynomial unimodular on the torus is a phase times a
monomial:

```text
det U_0(z) = e^(i phi) z_1^n1 z_2^n2 z_3^n3.              (8)
```

But also

```text
det U_0(z) = exp(-i t_0 tr H(z)).                          (9)
```

The right side has the global continuous periodic logarithm
`-t_0 tr H`. Its winding along every torus cycle is zero, so every `n_j` in
(8) is zero. Equation (9) is constant. Continuity then prevents
`tr H` from jumping among different logarithm branches, so `a(z)=a` is
constant.

### 2.2 Finite trace forces constant band splitting

Using (7), the centered exponential has trace

```text
tr exp(-i t_0 D(z)) = 2 F(s(z)),
F(w) = cos(t_0 sqrt(w))
     = sum_n>=0 (-1)^n t_0^(2n) w^n/(2n)!.                (10)
```

`F` is an entire, nonpolynomial function of `w` because `t_0!=0`. Since
`U_0` is finite Laurent and the center phase is constant, `F(s(z))` is finite
Laurent.

If the Laurent polynomial `s` were nonconstant, choose a generic monomial
one-variable slice of `(C*)^3` on which `s` remains nonconstant. The restricted
`s(w)` has a pole at `w=0` or `w=infinity`. Composition of a nonpolynomial
entire function with a pole has an essential singularity there. But a finite
Laurent polynomial has only a finite-order pole. This contradiction proves

```text
s(z) = rho^2 = constant.                                  (11)
```

The two eigenvalues are therefore the constants `a+-rho`.

### 2.3 Converse and the zero-splitting case

If (11) holds with `rho>0`, equations (7) and (10) give the exact identity

```text
exp(-i t H(z)) = e^(-iat)
 [ cos(t rho) I - i sin(t rho) D(z)/rho ].                (12)
```

The right side has exactly the Laurent range of `D` for every `t`, so it is
strict for all times. If `rho=0`, Hermiticity on the torus and `D^2=0` imply
`D=0`; the flow is an onsite phase. This proves (2)--(3), including all
degenerate cases.

When the two components are separately declared to be a Nambu carrier and the
Laurent coefficients satisfy the canonical particle-hole constraints, the
finite Laurent `U_t` and its finite Laurent inverse lift to a strict Gaussian
Bogoliubov automorphism of the CAR algebra. That lift is conditional category
data, not a consequence of the Qubit axiom.

## 3. Minimal scalar proper-cubic BdG corollary

Supply one spinless CAR mode per site and the Nambu symbol

```text
H_BdG(k) = [[xi(k), Delta(k)],
            [Delta(k)*, -xi(-k)]].                        (13)
```

Fermionic antisymmetry requires `Delta(-k)=-Delta(k)`. At nearest-neighbor
range, its coefficient data are an odd cubic vector. A scalar onsite action of
the proper cubic group can carry only a one-dimensional character `chi`; every
such character has `chi^2=1`, so it acts trivially on a pair. For each cubic
axis there is a proper `pi` rotation taking the positive bond to the negative
bond. Covariance and antisymmetry then give

```text
Delta_(+e_j) = Delta_(-e_j) = -Delta_(+e_j),
therefore Delta = 0.                                      (14)
```

Hermiticity and the same cubic symmetry reduce the normal nearest-neighbor
symbol to

```text
xi(k) = mu + 2J[cos(k_x)+cos(k_y)+cos(k_z)].              (15)
```

Its two eigenvalues are `+-|xi(k)|`. Evaluating `xi^2` at
`(0,0,0)`, `(pi,0,0)`, and `(pi,pi,pi)` shows that constant `xi^2` forces
`J=0`. By the two-band theorem, a finite-Laurent exponential at any nonzero
time therefore forces onsite flow in this minimal scalar cubic class.

This is a carrier-minimum theorem. It does not say cubic BdG pairing is
impossible with spin, orbital, sublattice, directed-mode, or other internal
representations.

## 4. Exact positive escapes

Two controls prevent overreading the negative corollary.

### 4.1 Lower-symmetry two-band escape

In one dimension,

```text
q(k) = cos(k) Z + sin(k) Y,        q(k)^2=I,              (16)
```

obeys the standard spinless particle-hole relation. Equation (12) makes its
exponential a strict radius-one Bogoliubov automorphism for every time. Thus
pairing plus noncommutation is fully compatible with strict flow; the cubic
scalar representation is load-bearing in the preceding corollary.

### 4.2 Fully cubic multicomponent escape

The runner also rechecks the preceding doubled-Clifford construction. Six
bond Clifford generators plus one onsite generator produce a radius-one flat
involution. The irreducible `8`-mode version has an orientation obstruction
for half of the `24` proper cubic rotations; doubling opposite Clifford
chiralities to `16` modes restores covariance. Its exponential is strict for
every time. Therefore no claim extends from the scalar one-mode corollary to
multicomponent cubic Gaussian carriers.

## 5. Continuum consequence

This block closes the obvious charge-breaking two-band special-time loophole,
but it does not select the physical microscopic carrier. Its main forward
consequence is methodological and exact:

> A dispersive relativistic two-band Hamiltonian cannot simultaneously be a
> finite-Laurent generator and have an exactly strict exponential at a fixed
> nonzero physical time.

The controlled continuum campaign must therefore permit quasilocal tails,
use a shrinking step with a stated convergence topology, or begin from a
fundamental partitioned tick rather than impose strict support on
`exp(-itH)` at finite physical time. The repository's massive staggered
two-step transfer family is the strongest current candidate for that next
campaign because it already has separate positivity, dispersion,
exact-log-quasilocality, covariance, and Gaussian convergence packets. Those
packets still need a single same-object scaling theorem; nothing here treats
their current conditional or unaudited statements as retained authority.

## 6. Assumptions, imports, and primitive registry

The theorem supplies mathematics on named carriers. It does not supply those
carriers physically.

| item | status here |
|---|---|
| cubic lattice and onsite `M_2(C)` presentation | from `minimal_axioms` |
| endpoint-symmetric parity spin density | supplied finite tensor class |
| global CAR algebra / Nambu carrier | supplied, not derived |
| particle-hole convention and cubic onsite representation | supplied |
| finite range, generator coefficients, and nonzero time | supplied |
| physical carrier selector, Record coupling, probability, and rate | open |
| continuum scaling family and convergence topology | open |

The live approved registry contains `minimal_axioms`, the units-only
`scale_reference_primitive`, the form-only `kinetic_isotropy_primitive`, and
the point-evaluation-only `realized_state_primitive`. None supplies a CAR
carrier, BdG generator, time law, probability rule, physical selector, or
continuum theorem. No proposed primitive is used, and this result requests no
registry change.

## 7. Negative-claim discipline N1--N8

The scoped negative claims are: no isolated strict time for finite-Laurent
two-band generators, and no non-onsite strict common flow in the supplied
nearest-neighbor scalar one-mode proper-cubic BdG class.

**N1 -- alternative routes.** The general two-band matrix route is handled by
the determinant/trace/essential-singularity proof; the literal parity-even
spin edge is classified but kept outside CAR until a locality bridge is
supplied; the lower-symmetry flat Kitaev route is positive; the multicomponent
fully cubic flat route is positive; partitioned/time-dependent ticks,
interacting qubit QCAs, and quasilocal shrinking-step continuum flows remain
open; dimensions at least four are not classified by the two-band theorem.

**N2 -- open-condition independence.** Two-band size, finite Laurent range,
Hermiticity, nonzero time, CAR/Nambu realization, scalar cubic onsite action,
and nearest-neighbor range do separate work. Dropping cubic scalar symmetry
allows (16); enlarging the carrier allows the doubled-Clifford escape; dropping
strict support admits the dispersive quasilocal continuum route.

**N3 -- hidden-condition scan.** `BdG` means a separately supplied graded
Nambu carrier, not an arbitrary two-qubit matrix. `Strict` means finite Laurent
support on the infinite lattice, not finite-volume recurrence or numerical
smallness. `Two-band`, `nearest-neighbor`, `scalar onsite action`, and
`proper-cubic` are all headline scope conditions.

**N4 -- residual matching.** The preceding onsite-charge theorem explicitly
left charge-breaking/Bogoliubov special-time flow open. Equations (2)--(3)
close that special-time question for every two-band finite-Laurent generator;
equations (13)--(15) close the smallest scalar cubic pairing carrier. Physical
carrier selection and continuum control are different residuals and are not
claimed closed.

**N5 -- rhetoric audit.** `No isolated strict time` is restricted to the
two-band finite-Laurent generator class. `Onsite only` is restricted to the
spinless one-mode scalar proper-cubic nearest-neighbor BdG corollary. No phrase
such as `all BdG`, `all common Hamiltonians`, or `all QCAs` is used as a
conclusion.

**N6 -- partial-closure and primitive scan.** A supplied-carrier continuum
theorem remains a valid partial-closure route. Approved scale, kinetic-form,
and realized-state primitives are not obstructions and are not inflated into
dynamics. No unapproved primitive receives claim weight. The result narrows a
class; it does not imply an axiom update.

**N7 -- steelman.** The strongest objection is that flat-band and larger
carriers give strict noncommuting cubic flows, while a fixed supplied
dispersive carrier can enter continuum analysis without waiting for a unique
microscopic selector. Both points are correct: the positive escapes are
explicit, and Campaign 6 may now proceed conditionally on one supplied
same-object scaling family.

**N8 -- cross-cycle echo.** `No cone at this density` was escaped by twisted or
larger cells; scalar CAR triviality was escaped by six modes; a broad
noncommuting-tail claim was escaped by the `16`-mode flat involution. This block
therefore keeps its negative result at two bands and its cubic corollary at one
scalar mode.

## 8. What this does not establish

- no physical derivation of CAR statistics, Nambu doubling, or a BdG carrier;
- no classification of `4 x 4` or larger finite-Laurent generators;
- no classification of general interacting or time-dependent qubit QCAs;
- no physical tick, clock duration, dimensionful rate, probability rule, or
  framework-Record formation law;
- no Lorentz, QFT, Standard Model, gravity, or continuum-limit theorem;
- no axiom, primitive, or audit-status change.

## 9. Reproduction

```bash
python3 scripts/two_band_bdg_strict_time_flat_spectrum_2026_07_12.py
```

Expected scorecard:

```text
SUMMARY PASS=31 FAIL=0
```

The runner checks the six-dimensional parity spin class, exact
Cayley--Hamilton identities, the nonterminating entire-function/pole
mechanism, all `24` proper cubic rotations, the scalar nearest-neighbor
flatness kill, the lower-symmetry particle-hole flat involution, strict CAR
coefficient convolution, dispersive Bessel tails, and the doubled `16`-mode
cubic escape.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or contextual source. Independent audit is the
only status authority.
