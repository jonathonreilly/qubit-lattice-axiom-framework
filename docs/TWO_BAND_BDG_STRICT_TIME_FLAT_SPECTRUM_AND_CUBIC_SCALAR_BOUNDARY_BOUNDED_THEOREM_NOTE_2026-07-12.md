---
claim_id: two_band_bdg_strict_time_flat_spectrum_and_cubic_scalar_boundary_bounded_theorem_note_2026-07-12
claim_type: bounded_theorem
claim_scope: "Exact finite-Laurent two-band generator theorem and scalar one-mode proper-cubic nearest-neighbor BdG corollary. For any supplied 2x2 torus-Hermitian finite Laurent generator H and nonzero real t0, exp(-it0 H) is finite Laurent iff H has momentum-independent eigenvalues; equivalently strict once iff flat spectrum iff strict for every time. Separately, the endpoint-SWAP-symmetric parity-preserving two-qubit spin density is six-dimensional, with two charge-breaking pairing directions, but it is not identified with a local Z3 CAR/BdG density. On a separately supplied spinless one-mode CAR/Nambu carrier with ordinary scalar proper-cubic onsite action and nearest-neighbor range, odd pairing is killed and flatness forces the normal hopping to vanish, leaving only onsite flow. A lower-symmetry Kitaev involution and a doubled 16-mode spinorial-cubic flat involution are positive escapes; the latter is an honest cubic action only on the even/quadratic algebra. CAR/Nambu realization, particle-hole convention, generator, time, carrier dimension, range, symmetry action, physical selection, Record coupling, probability, and continuum scaling are supplied or open."
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

Does a separately supplied two-band Gaussian/Bogoliubov class adjacent to the
preceding onsite-charge theorem contain a dispersive Hamiltonian whose
exponential becomes an exactly finite-radius Gaussian QCA at one exceptional
nonzero time? This does not identify the literal charge-breaking qubit class
with local CAR dynamics.

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

A second result closes the smallest ordinary-scalar cubic pairing carrier. On a supplied
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
  `onsite-charge common-Hamiltonian dichotomy`
  classifies the full charge-preserving one-qubit edge density and explicitly
  leaves charge-breaking/BdG densities open. It also supplies the doubled
  `16`-mode flat-involution escape that prevents a broader noncommuting-tail
  no-go.
- The
  `scalar cubic CAR-QCA theorem`
  proves only the number-preserving scalar Laurent class and explicitly leaves
  Bogoliubov mixing and intermediate carrier dimensions open.
- The repository's Majorana/Nambu notes, including
  `the Nambu source principle`,
  use a finite local two-mode pseudospin/source grammar. They do not supply a
  translation-invariant local `Z^3` CAR dynamics or identify a two-qubit spin
  edge with a local BdG edge.
- The exact-log transfer sources distinguish finite range from exponential
  quasilocality. That distinction becomes decisive for the continuum campaign:
  a dispersive generator in the scoped class should not be required to have a
  strict exponential at a fixed supplied nonzero time parameter.

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

The right side has at most the Laurent range of `D` for every `t`, with the
non-onsite range collapsing whenever `sin(t rho)=0`; it is therefore strict
for all times. If `rho=0`, Hermiticity on the torus and `D^2=0` imply
`D=0`; the flow is an onsite phase. This proves (2)--(3), including all
degenerate cases.

When the two components are separately declared to be a Nambu carrier and the
Laurent coefficients satisfy the supplied particle-hole constraints, the
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
the proper cubic group uses an ordinary one-dimensional character `chi`. The
proper cubic group is `O isomorphic to S_4`; its commutator subgroup has order
`12`, so its abelianization is `C_2` and every such character has `chi^2=1`.
It therefore acts trivially on a pair. For each cubic
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

obeys the supplied spinless particle-hole relation. Equation (12) makes its
exponential a strict radius-at-most-one Bogoliubov automorphism for every time,
with exact radius one when `sin(t)!=0`. Thus
pairing plus noncommutation is fully compatible with strict flow; the cubic
scalar representation is load-bearing in the preceding corollary.

### 4.2 Spinorial cubic multicomponent escape

The runner also rechecks the preceding doubled-Clifford construction. Six
bond Clifford generators plus one onsite generator produce a radius-one flat
involution. The irreducible `8`-mode version has an orientation obstruction
for half of the `24` proper cubic rotations; doubling opposite Clifford
chiralities to `16` modes supplies a unitary intertwiner for every rotation.
Those intertwiners close only projectively: commuting spatial pi rotations can
anticommute on odd CAR generators. Their conjugation action is an honest cubic
action on the even/quadratic observable algebra, not an ordinary `24`-element
action on the full odd CAR generators. The exponential is strict for every
time. Therefore no claim extends from the scalar one-mode corollary to
multicomponent spinorial-cubic Gaussian carriers.

## 5. Continuum consequence

This block closes the separately supplied two-band Gaussian special-time route,
not the literal charge-breaking qubit class or any multiband class. It does not
select the physical microscopic carrier. Its main forward
consequence is methodological and exact:

> A dispersive two-band Hamiltonian in this supplied finite-Laurent
> common-generator class cannot have an exactly strict exponential at a fixed
> nonzero supplied time parameter.

If the controlled continuum campaign keeps this two-band common-generator
class, it must therefore permit quasilocal tails or use a shrinking step with a
stated convergence topology. Multiband isolated-time constructions,
interacting flows, and fundamental partitioned ticks remain open alternatives.
The repository's massive staggered
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
nearest-neighbor scalar one-mode ordinary proper-cubic BdG class.

### N1 -- alternative route enumeration

| attack route | marker | test and outcome | proof/authority surface |
|---|---|---|---|
| hide momentum dependence in `tr H` while making the determinant finite Laurent | `ATTEMPTED` | scalar Laurent unitarity plus the global logarithm makes every determinant winding zero and fixes `tr H` | current source equations (8)--(9), lines 152--171; runner `B01--B03` |
| keep constant trace but a nonconstant band splitting | `ATTEMPTED` | a generic monomial slice turns nonconstant `s` into a pole, and nonpolynomial-entire `F(s)` into an essential singularity | current source equations (10)--(11), lines 173--196; runner `B04--B06` |
| tune one exceptional time so the sine coefficient cancels transport | `ATTEMPTED` | finite support at that time already forces flat spectrum; sine-zero times then collapse a flat family onsite rather than create an isolated dispersive point | current source equation (12), lines 198--211; runner `M01` |
| use the literal parity-even two-qubit pairing directions as local cubic BdG terms | `ATTEMPTED` | the six spin directions are classified, but no local `Z^3` spin-to-CAR bridge is supplied; this route remains outside the BdG theorem rather than being falsely ruled out | current source equations (4)--(5), lines 99--130; runner `A01--A07` |
| use spinless one-mode nearest-neighbor cubic pairing | `ATTEMPTED` | ordinary scalar cubic covariance plus antisymmetry kills pairing, and flat normal spectrum forces `J=0` | current source equations (13)--(15), lines 220--255; runner `C01--C06` |
| drop ordinary scalar cubic symmetry | `ATTEMPTED` | succeeds as a positive scope guard: the one-dimensional Kitaev involution is strict at radius at most one | current source equation (16), lines 265--275; runner `D01--D04` |
| enlarge the carrier or use spinorial cubic symmetry | `ATTEMPTED` | succeeds as a positive scope guard on the even/quadratic algebra; it does not falsify the two-band theorem | current source lines 277--290; runner `F01--F06` |

The route count is seven. No route is marked `RULED OUT BY PRIOR`; the exact
negative authority is proved self-containedly in this cycle, while prior notes
only locate the question. Multiband, interacting, time-dependent, partitioned,
and quasilocal alternatives are untested outside-class routes recorded in N5
and N7, not mislabeled as attempted routes.

### N2 -- open-condition independence

Collapse the scope to six conditions:

- `C1`: a torus-Hermitian `2 x 2` finite-Laurent, time-independent generator;
- `C2`: exact finite support at one supplied nonzero time on the infinite lattice;
- `C3`: a separately supplied CAR/Nambu realization for the BdG reading;
- `C4`: one spinless mode, nearest-neighbor range, and an ordinary scalar
  proper-cubic onsite action for the minimal corollary;
- `C5`: a physical carrier selector;
- `C6`: a continuum convergence topology.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `C1,C2` | no: a generator class does not grant strictness | no: a strict tick need not be an exponential of `C1` | yes |
| `C1,C3` | no: matrix Laurent data do not supply CAR | no: CAR does not force two bands or finite range | yes |
| `C1,C4` | no: the general theorem has no cubic scalar action | no: `C4` does not fix a generator or spectrum | yes |
| `C1,C5` | no: a supplied matrix is not physically selected | no: a selector need not choose `C1` | yes |
| `C1,C6` | no: a generator class does not choose convergence | no: a topology need not choose `C1` | yes |
| `C2,C3` | no: strict matrix support does not supply CAR | no: CAR does not grant strict time evolution | yes |
| `C2,C4` | no: strictness does not impose the minimal carrier | no: the minimal carrier can have dispersive tails | yes |
| `C2,C5` | no: strictness does not select the physical carrier | no: a selector may choose a nonstrict flow | yes |
| `C2,C6` | no: strictness does not choose continuum convergence | no: a continuum topology may allow quasilocal flow | yes |
| `C3,C4` | no: general CAR allows larger representations | no: the minimal representation still needs a CAR bridge | yes |
| `C3,C5` | no: CAR does not select the realized carrier | no: a selector could choose another category | yes |
| `C3,C6` | no: CAR supplies no convergence theorem | no: a topology need not use CAR | yes |
| `C4,C5` | no: the minimal class is not physically selected | no: a selector does not force one scalar mode | yes |
| `C4,C6` | no: the minimal class supplies no topology | no: continuum control does not force one scalar mode | yes |
| `C5,C6` | no: selecting a carrier proves no convergence | no: convergence does not select the realized carrier | yes |

No condition collapses into another. The theorem closes `C1+C2`; the cubic
corollary adds `C3+C4`; `C5` and `C6` stay independently open.

### N3 -- hidden-condition scan

| phrase hit | classification | disposition |
|---|---|---|
| `Assume now, separately` (line 134) | hidden condition made explicit | this is `C1`, not framework content |
| `supplied particle-hole constraints` (line 215) | explicit condition | part of `C3`; not used by the general matrix theorem |
| `supplied spinless particle-hole relation` (line 271) | explicit condition | positive Kitaev control only |
| `registered` primitive language (section 6) | cited registry context | primitive registry checked; no primitive supplies dynamics |
| existing-science `context` / `current candidate` language | non-load-bearing context | code-formatted pointers create no graph dependency and prove no theorem step |

The scan found no remaining `we assume`, `by construction`, `as is standard`,
`framework provides`, `bridge context`, `background`, `naturally`, `obviously`,
`standard QFT`, or `canonical` phrase carrying hidden claim weight.

### N4 -- residual matching

| witness | witness residual | residual claimed closed here | match? |
|---|---|---|---|
| `docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md:272-282` | all charge-breaking/BdG and larger-carrier common-H routes | finite-Laurent two-band Gaussian isolated-time route | no; question provenance only, dropped as proof authority |
| `docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md:4,247-258` | number-preserving scalar CAR tick and its category boundary | two-band generator exponential and one-mode BdG pairing | no; category context only, dropped as proof authority |
| `docs/NEUTRINO_MAJORANA_NAMBU_SOURCE_PRINCIPLE_NOTE.md:60-123` | finite local two-mode source grammar | translation-invariant Laurent dynamics | no; category context only, dropped as proof authority |
| `docs/TWO_BAND_BDG_STRICT_TIME_FLAT_SPECTRUM_AND_CUBIC_SCALAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md:134-255` plus paired runner | exactly the `C1+C2` matrix residual and `C3+C4` minimal corollary | same | yes; sole load-bearing proof surface |

After dropping the three nonmatching contextual witnesses, the claim remains
supported because its proof is self-contained. The literal charge-breaking
qubit class, physical carrier selection, and continuum control are not claimed
closed.

### N5 -- rhetoric and resolution audit

| resolution | tested? | narrow result |
|---|---|---|
| one two-qubit spin edge | yes | six-dimensional parity-preserving class; no CAR identification |
| one spinless CAR mode/site, nearest-neighbor cubic block | yes | pairing killed and strict common-generator flow onsite only |
| arbitrary two-band Laurent momentum block | yes | strict once iff flat spectrum iff strict all times |
| lattice-wide two-band Gaussian automorphism | conditional | finite Laurent lift is strict only after the CAR/Nambu carrier and particle-hole data are supplied |
| `4 x 4` or larger momentum block | no | open; no isolated-time claim |
| interacting/multibody full CAR or qubit algebra | no | open; no no-go claim |
| physical lattice process / Record formation | no | open; no selection or occurrence claim |

Accordingly `no isolated strict time` always means the `2 x 2`
finite-Laurent common-generator class, and `onsite only` always means the
ordinary-scalar one-mode nearest-neighbor proper-cubic corollary.

### N6 -- partial-closure and primitive scan

| candidate path | live status | what it can close |
|---|---|---|
| current two-band theorem and scalar cubic corollary | bounded candidate, audit pending | closes only `C1+C2` and `C3+C4` |
| lower-symmetry Kitaev involution | exact positive control in current runner | shows flat pairing can be strict |
| doubled `16`-mode spinorial-cubic involution | exact positive control in current runner | shows larger carriers evade the scalar corollary on the even/quadratic algebra |
| `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md` | `unaudited` in the live ledger | candidate quasilocal generator path without strict finite range |
| massive free staggered same-object scaling family | not yet assembled | could close the first controlled continuum commuting diagram on a supplied carrier |
| `scale_reference_primitive` | approved, units only | closes units conversion only; no dynamics or selector |
| `kinetic_isotropy_primitive` | approved, form only | closes structural `c_t=c_s` only; no Lorentz or dynamics theorem |
| `realized_state_primitive` | approved, point evaluation only | closes no state selection, measure, or probability rule |

The primitive registry contains no admission class and no unapproved primitive
receives weight. A bounded supplied-carrier theorem followed by an
import-retirement audit is a valid path; no new axiom is inferred.

### N7 -- steelman

A hostile reviewer should say: this is only a `2 x 2` theorem. Larger matrices
can have flat or specially phased subblocks; a fundamental partitioned tick
need not be `exp(-itH)`; and a continuum flow can be exponentially quasilocal
rather than strict. The strongest concrete authority is the flat-involution
construction in
`docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md:289-359`, corrected here to a projective spinorial action on odd CAR generators
and an honest cubic action on the even/quadratic algebra. This steelman defeats
every broader BdG/common-H/QCA no-go, but it does not defeat equations
(8)--(12). The result therefore stays bounded to two bands and one ordinary
scalar cubic mode.

### N8 -- cross-cycle echo

| prior path | live status | later escape/change mechanism | implication here |
|---|---|---|---|
| `docs/KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md` | `unaudited` | eta-twisted/larger classes escaped the analyzed no-cone surface | do not generalize a carrier-density result |
| `docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md` | branch-local / audit pending | six modes escaped scalar CAR transport triviality | keep the one-mode qualifier |
| `docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md` | branch-local / audit pending | flat `16`-mode spinorial construction escaped the one-qubit tail pattern | keep the two-band qualifier and projective-action guard |
| `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md` | `unaudited` | strict finite range was replaced by a quasilocal positive theorem | allow quasilocal continuum dynamics |

Each similar negative was retired or narrowed by enlarging the carrier,
changing symmetry realization, or weakening strict support to controlled
quasilocality. All three mechanisms remain explicit open conditions here.

**No-Go Discipline verdict:** `PASS` for the narrow two-band theorem and
ordinary-scalar one-mode corollary. It is `FAIL` for any exhaustive BdG,
all-common-Hamiltonian, all-QCA, or axiom-update conclusion; none is shipped.

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
SUMMARY PASS=33 FAIL=0
```

The runner checks the six-dimensional parity spin class, exact
Cayley--Hamilton identities, the nonterminating entire-function/pole
mechanism, all `24` proper cubic rotations, the scalar nearest-neighbor
flatness kill, the lower-symmetry particle-hole flat involution, strict CAR
coefficient convolution, dispersive Bessel tails, the proper-cubic
commutator subgroup, and the doubled `16`-mode spinorial/projective cubic
escape including its nontrivial cocycle.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or contextual source. Independent audit is the
only status authority.
