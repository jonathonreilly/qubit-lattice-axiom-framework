---
claim_id: onsite_charge_conserving_endpoint_symmetric_common_hamiltonian_strict_qca_dichotomy_bounded_theorem_note_2026-07-12
claim_type: bounded_theorem
claim_scope: "Exact infinite-lattice dichotomy for a supplied onsite Pauli charge and one uniform endpoint-SWAP-symmetric Hermitian nearest-neighbor qubit density that conserves that charge. Up to a uniform onsite basis, h=c II+r(ZI+IZ)+g ZZ+J(XX+YY). The J=0 branch is the commuting strict-radius-at-most-one family. For J nonzero, the exact one-excitation propagator has infinite support at every nonzero real time, so the full automorphism is not a finite-radius QCA at any nonzero isolated time. A separate 16-mode doubled-chirality flat involution gives a fully proper-cubic, noncommuting, strict-radius-at-most-one Hamiltonian escape and prevents any broader no-go. The tensor carrier, charge axis, identical-edge ansatz, coefficients, and time are supplied. Finite-torus revivals, charge-nonconserving densities, other larger cells, multibody interactions, partitioned clocks, physical selection, probability, and continuum limits are not classified."
upstream_dependencies:
  - minimal_axioms
runner: scripts/onsite_charge_conserving_common_hamiltonian_strict_qca_dichotomy_2026_07_12.py
---

# Endpoint-Symmetric Onsite-Charge-Conserving Common-Hamiltonian Strict-QCA Dichotomy On One Qubit Per Site

**Date:** 2026-07-12

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/onsite_charge_conserving_common_hamiltonian_strict_qca_dichotomy_2026_07_12.py`](../scripts/onsite_charge_conserving_common_hamiltonian_strict_qca_dichotomy_2026_07_12.py)

**Cached output:**
[`logs/runner-cache/onsite_charge_conserving_common_hamiltonian_strict_qca_dichotomy_2026_07_12.txt`](../logs/runner-cache/onsite_charge_conserving_common_hamiltonian_strict_qca_dichotomy_2026_07_12.txt)

## Question and bounded answer

Can a noncommuting, transporting common nearest-neighbor qubit Hamiltonian
nevertheless become an exactly finite-radius QCA at one exceptional nonzero
time?

This note answers that question completely inside the endpoint-symmetric
onsite-charge-conserving class. Supply a Hermitian Pauli axis `N=n.sigma`,
`|n|=1`, and one Hermitian two-site density `h` satisfying

```text
SWAP h SWAP = h,
[h, N tensor I + I tensor N] = 0.                         (1)
```

Place the same `h` on every undirected nearest-neighbor edge of `Z^3`. Up to
one uniform onsite basis taking `N` to `Z`, every such density is exactly

```text
h = c II + r (ZI+IZ) + g ZZ + J (XX+YY),                 (2)
```

with real `c,r,g,J`. There is then an exact dichotomy.

1. If `J=0`, all edge terms commute. The induced infinite-lattice
   automorphism has strict graph radius at most one for every `t`, and exact
   radius one iff `sin(2gt) != 0`.
2. If `J!=0`, the one-excitation propagator has infinite spatial support for
   every real `t!=0`. Consequently the full spin automorphism is not a
   finite-radius QCA at any nonzero time. There is no isolated-time
   cancellation escape in this class.

The result is stronger than a generic Lieb--Robinson tail statement but much
narrower than an all-common-Hamiltonian classification. Charge-nonconserving
and larger-carrier special-time cancellations remain open.

## Existing-science reading gate

The actual current sources were read before fixing the theorem.

- The approved [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the cubic
  lattice and one-site `M_2(C)` presentation, but no tensor carrier,
  Hamiltonian, charge axis, time, probability rule, or dynamics selector.
- The preceding
  `docs/PAIRWISE_COMMUTING_ENDPOINT_SYMMETRIC_EDGE_HAMILTONIAN_CLASSIFICATION_AND_STRICT_QCA_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md`
  proves the `J=0` positive branch and explicitly leaves noncommuting and
  special-time common Hamiltonians open.
- The repository's
  `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`
  supplies `I-SWAP` as a lawful competitor interaction and derives its
  one-excitation cubic graph Laplacian. The corollary below recomputes that
  identification exactly.
- The
  `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`
  proves that an exact free reconstructed Hamiltonian can be exponentially
  quasilocal without being finite range. That is context for the distinction
  between strict support and tails, not proof authority here.
- The
  `docs/BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  exhibits distance-two leakage for one exponential nearest-neighbor tick.
  The Laurent proof below upgrades the relevant scalar-band statement from a
  sampled distance to every distance and every nonzero time.
- The site-license and 3D simultaneous-tick sources use the multivariable
  unimodular-Laurent machinery for strict ticks. Here the direction is
  complementary: exponentiating a nonconstant Hermitian Laurent generator
  produces an essential singularity, not a finite Laurent tick.

Those sources are context only. Equations
(1)--(10) below are proved self-containedly. The only declared graph
dependency is `minimal_axioms`.

## 1. Exact local normal form

Rotate the supplied axis to `N=Z` and use the ordered basis
`|00>,|01>,|10>,|11>`, with `Z|0>=|0>` and `Z|1>=-|1>`. Commutation with the
total charge `ZI+IZ` makes `h` block diagonal across the charge sectors
`+2,0,-2`. The endpoint SWAP is scalar on the two one-dimensional sectors
and is the Pauli `X` on `span{|01>,|10>}`. A Hermitian `2 x 2` matrix commuting
with that `X` is `a I+b X` with real `a,b`. Therefore

```text
h = diag(e_00, -, -, e_11),
h restricted to span{|01>,|10>} = [[a,b],[b,a]],           (3)
```

with four real parameters. The change of coordinates

```text
c = (e_00+e_11+2a)/4,     r = (e_00-e_11)/4,
g = (e_00+e_11-2a)/4,     J = b/2                         (4)
```

gives exactly (2). Direct substitution proves the converse. Thus (2) is the
complete class under (1), including all degeneracies.

## 2. Exact one-excitation restriction

Let `Omega` be the homogeneous all-`|0>` product reference. Every edge density
maps `|00>` to the scalar `e_00|00>`, so the vacuum state is invariant under
the interaction dynamics. Total charge conservation makes the one-excitation
space invariant. Identify the excitation at `x` with `|x>` in
`ell^2(Z^3)`.

On one incident edge, replacing `|00>` by `|10>` changes the diagonal energy
by

```text
(c-g) - (c+2r+g) = -2(r+g),                               (5)
```

and `J(XX+YY)` moves the excitation across that edge with matrix element
`2J`. Since the cubic lattice has degree six, after subtracting the vacuum
energy the exact one-particle generator is

```text
K = E_1 I + 2J A,       E_1=-12(r+g),                     (6)
```

where `A` is the cubic adjacency operator. Its Bloch symbol is

```text
epsilon(k) = E_1 + 4J sum_(mu=1)^3 cos(k_mu).             (7)
```

The interaction coefficient `g` is genuinely many-body away from this sector,
but inside the invariant one-excitation sector it contributes only the
constant in (6). It therefore cannot cancel the momentum dependence.

The transporting branch is also locally noncommuting. On three consecutive
sites, the outer-hop matrix elements of the exact overlap commutator are

```text
<100|[h_12,h_23]|001> = 4J^2,
<001|[h_12,h_23]|100> = -4J^2.                            (7a)
```

Thus every `J!=0` density exits the predecessor's pairwise-commuting class.

## 3. Laurent obstruction to every special time

Fix real `t!=0` and suppose the kernel of `exp(-itK)` had finite spatial
support. Its Bloch multiplier would then be a finite Laurent polynomial
`P(z_1,z_2,z_3)`. Equation (7) instead gives, on the unit torus,

```text
P(z_1,z_2,z_3)
 = exp(-it E_1)
   exp[-i 2Jt sum_mu (z_mu+z_mu^(-1))].                  (8)
```

Both sides are holomorphic on `(C*)^3`; applying the one-variable identity
theorem successively extends equality off the unit torus. Set `z_2=z_3=1`.
The left side remains a finite Laurent polynomial in `z=z_1`, whereas the
right side is a nonzero constant times

```text
exp[-i 2Jt (z+z^(-1))].                                  (9)
```

For `Jt!=0`, (9) has an essential singularity at `z=0` from the `z^(-1)`
term and at infinity from the `z` term. A Laurent polynomial has only finite
order poles at zero and infinity. This is a contradiction. Hence the kernel
has infinite support for every `J!=0` and `t!=0`.

Equivalently, Jacobi--Anger gives the explicit kernel

```text
<x|exp(-itK)|0>
 = exp(-itE_1) product_mu [(-i)^(x_mu) BesselJ_(x_mu)(4Jt)].  (10)
```

Individual Bessel functions can vanish at special arguments, but no common
finite cutoff of all orders is possible: such a cutoff would make their
generating function (9) Laurent polynomial, contradicting the same essential
singularity. There is also a direct eventual-nonzero certificate. Relative to
the leading term `(x/2)^n/n!` in `BesselJ_n(x)`, the absolute sum of all later
terms is at most

```text
exp[x^2/(4(n+1))]-1.
```

It is strictly below one once `n+1>x^2/(4 log 2)`, so every sufficiently large
order is nonzero for each fixed real `x!=0`. This closes the apparent
isolated-time/Bessel-zero escape rather than merely sampling it.

## 4. From one-particle tails to failure of strict QCA locality

Let `alpha_t` be the quasi-local automorphism generated by the finite-range
interaction, and let `S^-_0=|1><0|` create one excitation at the origin. If
`alpha_t` had finite radius `R`, then `alpha_t(S^-_0)` would be supported in
the finite graph ball `B_R(0)`. Acting on the invariant vacuum would produce
a one-excitation vector supported inside that same ball. But this vector is,
up to the harmless vacuum phase, `exp(itK)|0>`, whose support is infinite by
Section 3 (replace `t` by `-t`). Contradiction.

Therefore the `J!=0` branch is not a finite-radius QCA at any nonzero time.
Failure on one invariant sector is sufficient; no cancellation in higher
excitation sectors can repair locality of the full automorphism.

For `J=0`, equation (2) is the commuting common-axis family. Direct
conjugation of a transverse onsite ladder gives a product of six neighbor
factors `exp(+-i2gtN_y)`. Thus the radius is at most one, and it is zero
exactly when every neighbor factor is scalar, `sin(2gt)=0`; otherwise it is
exactly one. This completes the dichotomy.

## 5. Exact `I-SWAP` / graph-Laplacian corollary

The repository's kinetic competitor uses

```text
Phi = I-SWAP
    = (1/2)II -(1/2)ZZ -(1/2)(XX+YY).                    (11)
```

Hence `(c,r,g,J)=(1/2,0,-1/2,-1/2)`. Equations (6)--(7) give

```text
K_Phi = 6I-A,
epsilon_Phi(k)=6-2 sum_mu cos(k_mu)
              =2 sum_mu (1-cos(k_mu)),                   (12)
```

exactly the cubic graph Laplacian and symbol used in the existing source.
Because `J=-1/2` is nonzero, its continuous-time common-Hamiltonian flow is
not a strict finite-radius QCA for any `t!=0`, even though its Hamiltonian
interaction is nearest-neighbor and its propagation obeys a Lieb--Robinson
bound.

## 6. Infinite lattice versus finite tori

The theorem is an infinite-`Z^3` or uniform thermodynamic-family statement.
On one fixed finite torus every operator has finite support in the vacuous
sense that the whole torus is finite, and discrete spectra may permit exact
revivals. Such a revival does not provide a radius bound independent of the
torus size and is not a strict local automorphism of the infinite lattice.

The Laurent proof may equivalently be read as excluding a fixed finite radius
uniformly over arbitrarily large tori: once the torus exceeds the alleged
support ball, its finite Fourier data would have to agree with the impossible
finite Laurent multiplier (8).

## 7. Result boundary

This theorem does not classify:

- endpoint-symmetric densities that fail to conserve a supplied onsite
  charge, including pairing/Bogoliubov sectors;
- charge-conserving endpoint-asymmetric densities, whose one-excitation
  restriction need not reduce to the single scalar band used here;
- multiband or larger-cell Hamiltonians, compact localized bands, flat-band
  interference, or internal clock/control carriers;
- multibody interactions or nonuniform edge densities;
- matching, Margolus, finite-depth, or explicitly time-dependent protocols;
- generic special-time cancellations outside the scalar one-particle band;
- selection of `N,c,r,g,J`, a tick duration, or a physical clock;
- probability, Record realization, continuum, QFT, Standard Model, or GR
  limits.

The number-nonconserving and multibody routes are live, and the larger-carrier
flat escape is constructed next. Therefore this bounded theorem does not
establish that an axiom or primitive update is necessary.

## 8. Bounded N7 positive escape and exact carrier correction

The scalar-band obstruction must not be promoted to an all-common-Hamiltonian
no-go. A flat matrix-valued involution supplies an exact escape. Let
`Gamma_0,...,Gamma_6` be seven pairwise-anticommuting Hermitian gamma matrices
and define

```text
q(p) = a Gamma_0
     + (b/sqrt(3)) sum_(mu=1)^3
       [cos(p_mu) Gamma_(2mu-1) + sin(p_mu) Gamma_(2mu)],
a^2+b^2=1.                                                (13)
```

Clifford anticommutation gives `q(p)^2=I` exactly, hence

```text
exp[-itq(p)] = cos(t) I - i sin(t) q(p).                  (14)
```

The right side has only onsite and nearest-neighbor Laurent coefficients, so
it is a strict radius-at-most-one tick for every `t`, and exact radius one
when `b sin(t)!=0`. For `ab!=0`, the onsite term and each bond term have a
nonzero commutator. Thus noncommuting, time-independent, finite-range
Hamiltonians can exponentiate to strict QCAs; the one-band Laurent
obstruction is not universal.

There is a load-bearing carrier correction. In one irreducible `8 x 8`
representation, the Cl(7) volume element is a nonzero central scalar. The 24
proper cubic rotations act on the six bond gammas by signed pair
permutations. Twelve induced maps have determinant `+1` and twelve have
determinant `-1`. An odd map that fixes `Gamma_0` reverses the seven-gamma
orientation and would flip the central volume scalar, so it cannot be
implemented by onsite unitary conjugation. Therefore the `8`-mode formula
with `ab!=0` is strict and noncommuting but is **not** fully proper-cubic
covariant on one irreducible carrier.

The exact repair is a `16`-mode doubled-chirality carrier:

```text
G_0 = diag(Gamma_0,-Gamma_0),
G_j = diag(Gamma_j, Gamma_j),   j=1,...,6.                (15)
```

Even signed-pair maps act block diagonally by their Pin intertwiner; odd maps
act by the same intertwiner followed by exchange of the two chirality blocks.
This fixes `G_0`, implements every signed-pair action on `G_1,...,G_6`, and
preserves (13)--(14). The runner constructs and verifies all 24 proper cubic
rotations. Thus a fully cubic, noncommuting, strict common-Hamiltonian escape
exists after a supplied carrier enlargement from the headline one-qubit class
to 16 modes. Its two eigenbands are flat, so it is not a transporting-cone
solution. It is a mathematical competitor, not a framework selector or a
derived physical realization.

To make the QCA statement explicit, supply 16 CAR modes `a_(x,r)` per site
and let `Q_h` be the finitely many Laurent coefficients of the doubled symbol
`q`. The Hermiticity relation `Q_(-h)=Q_h^dagger` defines the finite-range
quadratic interaction

```text
H_flat = sum_(x,h,r,s) (Q_h)_(sr) a_(x,r)^dagger a_(x+h,s).              (16)
```

Its one-particle exponential has coefficients

```text
U_(t,0) = cos(t) I - i sin(t) Q_0,
U_(t,h) =             - i sin(t) Q_h,  h!=0.                            (17)
```

The identity `q^2=I` gives both convolution identities
`U_t^dagger U_t=U_t U_t^dagger=I`. Hence
`alpha_t(a_(x,r))=sum_(h,s)(U_(t,h))_(sr)a_(x+h,s)` preserves the CAR and has
inverse `alpha_(-t)` with the same radius. This is a strict Gaussian CAR-QCA,
not merely a one-particle matrix. The cubic intertwiners lift by onsite second
quantization. The local Fock dimension is `2^16`, making the carrier
enlargement from one qubit explicit. Finally,
`[dGamma(A),dGamma(B)]=dGamma([A,B])`, so the nonzero onsite/bond matrix
commutator is also a nonzero commutator of local quadratic Hamiltonian pieces.
The transpose in (16) is load-bearing: the CAR identity
`[a_i^dagger a_j,a_l]=-delta_(il)a_j` gives
`d alpha_t(a_(x,r))/dt|_(t=0)=-i sum_(h,s)(Q_h)_(sr)a_(x+h,s)`, exactly the
derivative of (17). The runner checks this infinitesimal convention directly.

## No-Go Discipline Gate

**Status: PASS for the narrow `J!=0` negative branch.** The claim is only that
the supplied onsite-charge-conserving endpoint-symmetric one-band class has no
nonzero finite-time strict-QCA point.

### N1 -- alternative routes

| Route | Status | Exact outcome |
|---|---|---|
| isolated Bessel zeros | `ATTEMPTED` | individual orders may vanish, but a finite common cutoff would make the essential-singularity generating function Laurent |
| tune `r` or `g` against hopping | `ATTEMPTED` | both enter the one-particle restriction only through the scalar `E_1` and cannot remove `k` dependence |
| many-body interaction cancellation | `ATTEMPTED` | the invariant one-excitation tail already falsifies full-automorphism locality |
| finite-torus revival | `ATTEMPTED / OUTSIDE` | no radius uniform in torus size and no infinite-lattice QCA follows |
| zero hopping `J=0` | `ATTEMPTED / POSITIVE BRANCH` | exact positive commuting radius-at-most-one branch |
| charge-nonconserving/BdG density | `ATTEMPTED / OUTSIDE CLASS` | changes the invariant sector and scalar Laurent symbol; no conclusion imported |
| larger cell or internal band | `ATTEMPTED / POSITIVE ESCAPE` | the doubled 16-mode flat involution is a fully cubic noncommuting strict-radius-at-most-one escape |
| partitioned/time-dependent clock | `ATTEMPTED / OUTSIDE CLASS` | not a single time-independent common Hamiltonian of form (2) |

### N2 -- wall independence

There is one negative residual: exact finite propagation at nonzero time in
the `J!=0` branch under the explicit class inputs (1). Charge conservation,
endpoint symmetry, identical nearest-neighbor density, infinite lattice, and
the supplied tensor carrier define the theorem class; none is recast as a
derived framework premise.

### N3 -- hidden-wall scan

The onsite charge, homogeneous product vacuum, infinite quasi-local carrier,
identical edge density, and time-independent Hamiltonian are explicit. The
vacuum is not a framework Record or selected physical state. "Strict" means
exact finite support, not an exponentially small Lieb--Robinson tail.

### N4 -- residual matching

The exact current residual is `R*`: every `J!=0` member of class (1) has no
finite-radius point at any real `t!=0` on infinite `Z^3`.

| Source/status | Prior residual actually stated | Current residual claimed | Use | Match? |
|---|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:106`, approved premise | Admissibility supplies no Hamiltonian, weights, time metric, or record process | `R*` | sole authority boundary | no; premise only |
| `docs/PAIRWISE_COMMUTING_ENDPOINT_SYMMETRIC_EDGE_HAMILTONIAN_CLASSIFICATION_AND_STRICT_QCA_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md:38`, context only | commuting single-axis family is strict and nontransporting | `R*` | `J=0` complement, rederived here | no |
| `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:172`, `unaudited` | `I-SWAP` supplies a graph-Laplacian kinetic competitor | `R*` | exact instance comparator | partial instance, not witness |
| `docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md:261`, `unaudited` | finite-range H gives an LR/quasilocal cone | `R*` | tails-compatible context | no |
| `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md:191`, `unaudited` | one reconstructed free generator is quasilocal, not finite range | `R*` | different symbol/residual | no |
| `docs/BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md:75`, `unaudited` | one exponential tick leaks beyond radius one | `R*` | single-generator partial echo | no exact match |
| `docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md:96`, context only | a strict scalar Laurent unitary is a monomial | `R*` | category guard; proof recomputed | no |
| `docs/SYMMETRIC_TWO_QUBIT_CLIFFORD_CUBIC_MATCHING_QCA_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:125`, context only | complete layers can cancel without local commutation | `R*` | stroboscopic scope guard | no |

All load-bearing local, Laurent, Bessel, and flat-involution algebra is
recomputed here. No context row is promoted or used as theorem
authority. Required prior proof-witness count for `R*`: zero.

### N5 -- resolution audit

The local two-qubit class, infinite one-particle sector, every real nonzero
time, and full automorphism implication are proved. Finite tori, multi-band
cells, charge-nonconserving densities, and all common Hamiltonians are not
claimed. "No isolated-time escape" is always qualified by the class (1).

### N6 -- positive and partial closure paths

The `J=0` branch is a positive exact strict family. Generic `J!=0` dynamics
remains a positive quasilocal/Lieb--Robinson route even though it is not
strict. The 16-mode doubled-chirality involution is an exact fully cubic
noncommuting strict-radius-at-most-one escape. Number-nonconserving,
multibody, and partitioned routes remain legitimate next attacks. No new
axiom is requested.

### N7 -- steelman

A hostile reviewer should point to the explicit doubled 16-mode involution:
its onsite and bond pieces do not commute, yet `q^2=I` truncates the full
exponential to strict radius at most one (exactly one at generic time) and the
doubled chirality implements all 24 proper cubic rotations. This defeats any
all-common-Hamiltonian extrapolation.
The headline theorem remains complete only after the supplied onsite-charge
condition reduces the transport witness to one scalar band. It does not
exclude BdG, larger-cell, clocked, or multibody special-time constructions.

### N8 -- cross-cycle echo

| Prior surface/status | Retired? | Change mechanism | Application here |
|---|---:|---|---|
| `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md:191`, `unaudited` | strict finite-range form only | quasilocal exponential-tail repair | preserve the positive `J!=0` LR/quasilocal flow |
| `docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md:245`, context only | scalar scope only | larger-mode transport escape | construct the explicit 16-mode flat escape |
| `docs/SYMMETRIC_TWO_QUBIT_CLIFFORD_CUBIC_MATCHING_QCA_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:125`, context only | no | complete-layer cancellation beyond local test | keep stroboscopic grammars live outside class (1) |

No unconsidered convention change, primitive ratification, or premise
retirement applies to `R*`.

## Falsifiers

- A density satisfying (1) that cannot be written in form (2).
- A mismatch between the one-excitation generator and (6).
- A nonzero `J,t` for which (8) is a finite Laurent polynomial.
- A finite-radius image of `S^-_0` despite the infinite one-particle kernel.
- A `J=0` radius outside the predecessor formula.
- A mismatch between `I-SWAP` and equations (11)--(12).
- Failure of `q^2=I`, radius-one truncation, the 8-mode orientation
  obstruction, or any of the 24 doubled-carrier covariance checks.

## Reproduction

```bash
python3 scripts/onsite_charge_conserving_common_hamiltonian_strict_qca_dichotomy_2026_07_12.py
```

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  cubic geometry, spatial symmetry, and the one-site algebra boundary.

Context only: the pairwise-commuting common-edge classification,
minimal-surface `I-SWAP` kinetic competitor, transfer-log quasilocality,
B--W leakage, site-license, and 3D simultaneous-tick notes. None supplies a
load-bearing step of the local classification or Laurent proof.
