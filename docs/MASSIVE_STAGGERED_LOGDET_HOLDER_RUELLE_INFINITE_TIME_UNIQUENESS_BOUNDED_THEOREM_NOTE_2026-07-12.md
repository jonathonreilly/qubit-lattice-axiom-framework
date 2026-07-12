# Massive staggered log-determinant Hölder/Ruelle infinite-time uniqueness

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; independent audit alone assigns retained status.
**Primary runner:** [`scripts/massive_staggered_logdet_holder_ruelle_uniqueness_2026_07_12.py`](../scripts/massive_staggered_logdet_holder_ruelle_uniqueness_2026_07_12.py)
**Cached output:** [`logs/runner-cache/massive_staggered_logdet_holder_ruelle_uniqueness_2026_07_12.txt`](../logs/runner-cache/massive_staggered_logdet_holder_ruelle_uniqueness_2026_07_12.txt)

## 0. Result

For every fixed finite bipartite spatial volume, `beta>=0`, and `m>0`, the
normalized `SU(3)` Wilson--fundamental-staggered Euclidean functionals on even
antiperiodic temporal circles have a **unique full-sequence infinite-time
limit** on the local gauge-invariant polynomial algebra. No subsequence is
needed. The limit is independent of antiperiodic-seam placement and of
uniformly bounded localized temporal boundary perturbations in the admissible
Ruelle boundary class.

In short, the result is **full-sequence infinite-time uniqueness** at fixed
spatial volume.

The proof does not posit an interacting transfer matrix. After Grassmann
integration, write

```text
D=mI+M,              M^dagger=-M,
A=D^dagger D=m^2 I-M^2,
c=m^2+16,
Q=I-A/c=(16I+M^2)/c.                                                   (0.1)
```

The four-dimensional staggered hop obeys `||M||<=4`, so

```text
0<=Q<=rI,             r=16/(m^2+16)<1.                                (0.2)
```

`Q` has lattice range two. Since `det D>0`, the exact convergent identities

```text
log det D = (1/2) Tr log A
          = (dim D/2) log c -(1/2) sum_(n>=1) Tr(Q^n)/n,               (0.3)

A^(-1)=c^(-1) sum_(n>=0) Q^n,
D^(-1)=A^(-1)D^dagger                                                   (0.4)
```

make both the determinant effective action and all fixed-degree Wick
insertions exponentially quasilocal in Euclidean time for every `m>0`.
After blocking the period-two staggered phases, the gauge marginal is a
Hölder potential on a compact two-slice gauge alphabet. The standard
compact-alphabet Ruelle--Perron--Frobenius theorem gives a unique Gibbs
functional. The proof uses uniqueness, not an asserted spectral gap of the
Ruelle operator.

Consequently all accumulation functionals in the
[coupled OS interior-descent/subsequential-transfer theorem](COUPLED_OS_INTERIOR_DESCENT_SUBSEQUENTIAL_INFINITE_TIME_TRANSFER_BOUNDED_THEOREM_NOTE_2026-07-12.md)
coincide. Its positive self-adjoint two-step contraction and logarithmic
Hamiltonian are therefore canonical for this supplied model at fixed finite
spatial volume.

This theorem does not derive the Wilson-staggered dynamics or Euclidean
weight from the Lattice, Qubit, Admissibility, and Record axioms; it **does not
derive the probability rule**.
In plain terms: this note does not derive the probability rule.
It **does not take the spatial thermodynamic limit**, prove a volume-uniform
rate, or establish a
continuum Lorentz/QFT, Standard Model, or GR limit. No axiom-update stop is
established.

## 1. Supplied model and temporal alphabet

Use the same finite spatial geometry, Wilson-staggered action, antiperiodic
spin structure, and gauge-invariant polynomial observables as the coupled OS
theorem. The spatial volume `Lambda_s` is fixed and finite; every periodic
spatial extent is even, or the corresponding direction is open. Temporal
circumference is `L_t=2N` and tends through even values to infinity.

Do not impose global temporal gauge. Group two adjacent time slices into one
block. One block contains finitely many spatial and temporal `SU(3)` links, so
its configuration space is a finite product

```text
X=(SU(3))^E_block,                                                       (1.1)
```

a compact metric alphabet with normalized product Haar measure of full
support. The Wilson action is a bounded continuous finite-range potential on
`X^Z`. The staggered phases repeat under the two-step shift.

All model choices in this paragraph are supplied. In particular, uniqueness
of the resulting state does not select this action from the axioms.

## 2. Exact massive contraction calculus

### 2.1 Hop norm and determinant positivity

In each of four lattice directions the covariant staggered difference has
operator norm at most one: it is `(S_mu-S_mu^dagger)/2` up to a unit phase,
with `S_mu` unitary on a periodic block and a contraction for an open edge.
The triangle inequality gives

```text
||M||<=4.                                                               (2.1)
```

The bipartite sign `epsilon` anticommutes with `M`. Hence every nonzero
eigenvalue `i lambda` of the anti-Hermitian `M` is paired with `-i lambda`,
and for `m>0`

```text
det(mI+M)=m^z product_(lambda>0)(m^2+lambda^2)>0.                        (2.2)
```

Thus the real logarithm is unambiguous and

```text
log det D=(1/2)log det(D^dagger D)=(1/2)Tr log A.                       (2.3)
```

### 2.2 The exact `Q` series

Anti-Hermiticity gives `A=m^2I-M^2`. Equation (2.1) yields

```text
m^2 I<=A<=cI,                 c=m^2+16.                                (2.4)
```

Therefore `Q=I-A/c` is positive, self-adjoint, range two, and satisfies
`||Q||<=r<1` with `r` in (0.2). Functional calculus for the scalar geometric
and logarithmic series now gives (0.3)--(0.4) in operator norm. This is not a
large-mass hopping expansion: `r<1` for every strictly positive `m`, although
the rate becomes slow as `m` approaches zero.

The primary runner verifies the identities on a finite nonuniform `1+1`
`SU(3)` certificate, including anti-Hermiticity, bipartite pairing, the
spectrum of `A`, positivity and strict contraction of `Q`, determinant
equality, and convergence of both series. The theorem's `3+1` bound is the
analytic four-direction estimate `||M||<=4`; the reduced runner does not by
itself prove the `3+1` theorem.

## 3. Exponentially Hölder determinant interaction

Let `P_k` project onto the color-site degrees of freedom in temporal block
`k`, and let `d_b=rank P_k`, finite because `Lambda_s` is fixed. Define the
block-anchored fermion effective potential

```text
Phi_k^F(U)=(d_b/2)log c
           -(1/2)sum_(n>=1) Tr(P_k Q[U]^n P_k)/n.                       (3.1)
```

On a finite circle, summing (3.1) over `k` gives `log det D` exactly.
On the infinite block line it defines the corresponding quasilocal
interaction.

Suppose histories `U,V` agree on every gauge block within block distance `R`
of `k`. Since `Q` has range two lattice spacings, the diagonal block of
`Q^n` cannot see beyond a distance proportional to `n`. All terms below
`n_R=floor((R-1)/2)` agree. For the tail,

```text
|Phi_k^F(U)-Phi_k^F(V)|
 <=d_b sum_(n>=n_R) r^n/n
 <=C(Lambda_s,m) r^n_R.                                                 (3.2)
```

Thus the variations decay exponentially. The total two-step potential

```text
Phi=Phi^Wilson+Phi^F                                                   (3.3)
```

is translation invariant and Hölder on the two-sided full shift `X^Z`. The
Wilson part is finite range; all infinite memory comes from the explicitly
controlled determinant tail.

Hölder control also holds inside each compact-group symbol, not only in the
cylinder tail. On fixed finite `Lambda_s`, the polynomial link dependence of
`Q` is uniformly Lipschitz, and

```text
Q(U)^n-Q(V)^n
 =sum_(j=0)^(n-1) Q(U)^j (Q(U)-Q(V)) Q(V)^(n-1-j),                    (3.4)
```

so its norm is at most `n r^(n-1)||Q(U)-Q(V)||`. The `1/n` in (3.1)
cancels the factor `n`, and `sum r^(n-1)` converges. Hence the potential
is Lipschitz in the finite-dimensional link metric and exponentially Hölder
in the history metric.

The density (3.1) is gauge invariant: `A[U^g]=G A[U]G^dagger`, and the local
color trace is unchanged. Working on redundant link variables causes no
physical multiplicity. The unique measure constructed below is gauge
invariant, and its restriction to the gauge-invariant algebra is unique.

## 4. Compact-alphabet Ruelle theorem

Use the standard two-sided-to-one-sided Hölder cohomology lemma to replace
`Phi` by a cohomologous one-sided Hölder potential without changing its DLR
Gibbs measures or local expectations. For a compact metric alphabet with a
full-support a priori probability measure, the compact-alphabet
Ruelle--Perron--Frobenius theorem for a Hölder potential supplies:

1. a positive eigenfunction/eigenprobability for the normalized potential;
2. uniqueness of the eigenprobability under the Bowen condition, which the
   exponential variation bound (3.2) satisfies;
3. equivalence of that eigenprobability with the one-dimensional DLR Gibbs
   probability.

Every compactness accumulation point of the finite-circle measures is a DLR
measure for this interaction. Uniqueness makes all such accumulation points
equal and therefore gives full-sequence convergence. This proof does not need
to assert compactness or a spectral gap for the Ruelle operator on an
uncountable alphabet.

The external mathematical machinery is explicit. The RPF theorem is external mathematical machinery.
The compact-alphabet RPF
theorem is used at the same level as Peter--Weyl or the spectral theorem; it is
not a framework axiom or a supplied physical law. The load-bearing physics
work here is the exact reduction (0.1)--(0.4) proving that the actual massive
staggered determinant satisfies the theorem's Hölder hypothesis.

There is **no Ruelle spectral gap claimed** by this note; uniqueness of the
Bowen eigenprobability/DLR state is sufficient for full-sequence convergence.

Useful primary references are Cioletti--Silva, *Nonlinearity* **29** (2016)
2253, DOI `10.1088/0951-7715/29/8/2253`, for the compact-alphabet Hölder/Walters
Ruelle theorem and spectral properties, and Cioletti--Lopes--Stadlbauer,
*Discrete and Continuous Dynamical Systems* **40** (2020), DOI
`10.3934/dcds.2020195`, for compact-alphabet eigenprobability/DLR equivalence
and uniqueness criteria.

## 5. Antiperiodic seam and full-sequence convergence

The antiperiodic sign changes only the temporal hopping blocks at one seam.
Although `log det D` is not finite range after Grassmann integration, (0.3)
controls the finite-circle correction term by term. For order `n` much smaller
than `N`, only `O(n)` diagonal centers can detect the twisted bond, while the
coefficient is bounded by `r^n/n`; their total is `O(r^n)`. For orders
comparable to `N`, the bound is `O(N r^n/n)`, whose tail vanishes
exponentially in `N`. Hence the total seam interaction is uniformly bounded,
and its dependence on a block at distance `R` is `O(r^{R/2})`. Moving the seam
is another perturbation in the same class.

The same reasoning covers fixed uniformly bounded modifications supported on
finitely many temporal boundary blocks. It does not cover boundary vectors or
weights with zero overlap with the positive Ruelle eigenfunction, nor boundary
terms whose norm grows with `L_t`.

DLR/Ruelle uniqueness therefore gives, for every local gauge observable `F`,

```text
lim_(N->infinity) omega_(2N)(F)=omega_infinity(F),                      (5.1)
```

with no subsequence, independent of seam placement and of the stated
admissible boundary class. The small-`m` rate may be very slow because
`r->1`; existence and uniqueness nevertheless hold for each fixed `m>0`.

## 6. Full local gauge--fermion functional

The theorem is not limited to the gauge marginal. From (0.4), a propagator
entry is a convergent sum of finite-range terms. If a gauge history is changed
far from fixed endpoints, the low powers agree and the tail obeys

```text
variation_R D^(-1)
 <=C'(m) r^floor((R-2)/2).                                              (6.1)
```

Every fixed-degree Grassmann expectation is a finite sum of Wick minors of
`D^(-1)`. Determinants of fixed size preserve boundedness and Hölder
dependence. Multiplying by a local Wilson-loop, meson, or baryon polynomial
therefore produces a Hölder observable of the gauge history.

The finite-circle propagator differs from its infinite-line quasilocal
observable only by the same exponentially remote seam terms. Applying (5.1)
to the limiting Wick observable and using the uniform tail bound gives

```text
lim_(N->infinity) omega_(2N)(F)=omega_infinity(F)                       (6.2)
```

for every fixed local gauge-invariant gauge--fermion polynomial `F`. This is
the claimed full local Euclidean functional convergence.

## 7. Canonical fixed-volume OS reconstruction

Finite-circle reflection positivity, two-step translation invariance, and
adjacent-form positivity were proved on the supplied model before taking the
limit. They pass through the full limit exactly as they passed through the
subsequence in the coupled OS theorem.

Because the limit is unique, every diagonal accumulation functional used
there equals `omega_infinity`. Its OS Hilbert space, positive self-adjoint
two-step contraction `T_2`, Hamiltonian

```text
H=-(2a_tau)^(-1)log T_2                                                  (7.1)
```

on `(ker T_2)^perp`, Euclidean semigroup, and spectral unitary group are now
canonical at fixed spatial volume for the supplied Wilson-staggered model.

“Canonical” here means independent of the temporal subsequence and admissible
temporal boundary data. It does not mean derived from the four axioms, unique
under changing the microscopic action, or already controlled under spatial
volume or lattice-spacing limits.

## 8. Runner contract

Run:

```bash
python3 scripts/massive_staggered_logdet_holder_ruelle_uniqueness_2026_07_12.py
```

The runner checks the hop algebra, `A,Q` spectral bounds, exact determinant
identity, convergence of the logarithm and inverse series, finite propagation
of low powers, decay of the antiperiodic seam on local densities and inverse
entries, the all-`m>0` radius, and the source boundary/N1--N8 contract. The
compact-alphabet RPF theorem is mathematical machinery, not a numerical
claim, so the runner checks its model-specific Hölder premises rather than
sampling uniqueness.

## 9. Honest boundary and next theorem

The theorem fixes `Lambda_s`, `beta`, `m`, and lattice spacing. Constants may
deteriorate with spatial volume and as `m->0`. It does not establish a
spatially infinite Gibbs state, a uniform mass gap, continuum existence,
Euclidean rotational/Lorentz restoration, interacting QFT/Standard Model
universality, or dynamical geometry/GR. It also does not prove a simple vacuum
across charged superselection sectors or an OS-Hilbert spectral gap.

The highest-leverage next step is the spatial thermodynamic limit with bounds
uniform in `Lambda_s`, followed by a single controlled continuum scaling. The
exact `Q` calculus supplies a useful fermionic locality estimate for that next
campaign but does not solve the gauge-sector infrared problem.

## 10. No-Go Discipline N1--N8

This positive theorem retires the “subsequence only” wall but retains several
named downstream walls. No-Go Discipline prevents those walls from becoming
claims of impossibility.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it does not close more than claimed |
|---|---|---|---|
| Exact `Q`-series plus compact-alphabet RPF | `ATTEMPTED` | Equations (0.1)--(0.4) prove exponential variations for every `m>0`; RPF closes fixed-volume uniqueness. | It gives no spatial-volume-uniform rate and selects no microscopic action. |
| Exact enlarged gauge--Fock transfer kernel | `ATTEMPTED` | The older mixed assembly was read; it proves `W^dagger W` only after the full representation is supplied. | The missing all-observable coherent-state representation remains unnecessary for uniqueness but open as an operator identification. |
| Pure-gauge positivity-improving Perron route | `ATTEMPTED` | The Wilson kernel is pointwise positive and its character coefficients are positive. | Pure gauge does not include the full spacetime fermion determinant as a one-slice multiplier. |
| Fixed-background fermion transfer | `ATTEMPTED` | It gives a uniform matter contraction on static backgrounds. | A time-varying dynamical gauge history is not one fixed background. |
| High-mass hopping/cluster expansion | `ATTEMPTED` | The usual expansion would require `m>4`. | The exact positive `Q` expansion supersedes it and works for all `m>0`. |
| Direct boundary comparison | `ATTEMPTED` | The `Q` tails directly show seam influence is summable. | To turn local tail control into normalized full-sequence convergence, one still uses one-dimensional Gibbs/RPF uniqueness. |
| Matrix-cone positivity-improving transfer theorem | `ATTEMPTED` | Conserved fermion sectors and the missing common cone were identified. | No strict cone theorem is needed or proved here. |
| Exact finite-group analogue | `ATTEMPTED` | The `Z_3` supplier admits a trace-equivalent positive two-step spectral realization with a unique top eigenvalue. The exact `n_2` ratio `29/25` is a thermal-image channel: it is `1` at `L_t=8` and below `1` thereafter. | No observable-insertion intertwiner or larger-circumference full eleven-observable generalized spectrum was constructed; finite-group support cannot prove the `SU(3)` theorem. |

### N2 — wall-independence audit

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? | Witness |
|---|---|---|---|---|---|
| supplied Wilson-staggered dynamics | strictly positive fermion mass | No | No | Yes | An action family includes mass choices; positivity of a mass does not select the action. |
| supplied Wilson-staggered dynamics | fixed finite spatial volume | No | No | Yes | Dynamics and infrared volume control are distinct. |
| supplied Wilson-staggered dynamics | unique infinite-time functional | No | No | Yes | A supplied action need not have a unique state; uniqueness does not derive the action. |
| supplied Wilson-staggered dynamics | spatial thermodynamic limit | No | No | Yes | A finite regulator action does not establish its infinite-volume state, and an infinite-volume state does not select this action. |
| supplied Wilson-staggered dynamics | controlled continuum, Standard Model, and GR limits | No | No | Yes | A microscopic action is not a universality/GR theorem, and a continuum target does not select one regulator. |
| strictly positive fermion mass | fixed finite spatial volume | No | No | Yes | A mass gap condition and a volume restriction supply different content. |
| strictly positive fermion mass | unique infinite-time functional | No | No | Yes | Positive mass enables the proof but does not imply uniqueness for arbitrary actions; uniqueness need not force positive mass. |
| strictly positive fermion mass | spatial thermodynamic limit | No | No | Yes | Fermion locality does not control gauge infrared volume, and a thermodynamic limit can exist at zero mass. |
| strictly positive fermion mass | controlled continuum, Standard Model, and GR limits | No | No | Yes | A regulator mass does not prove the desired continuum, and continuum theories need not fix this bare mass. |
| fixed finite spatial volume | unique infinite-time functional | No | No | Yes | Finite width permits the RPF route but uniqueness still needs Hölder/non-null structure; uniqueness can also hold in infinite width. |
| fixed finite spatial volume | spatial thermodynamic limit | No | No | Yes | Fixing volume is not taking its limit, and existence of a limit does not erase finite-volume analysis. |
| fixed finite spatial volume | controlled continuum, Standard Model, and GR limits | No | No | Yes | Finite volume is neither sufficient nor necessary for continuum closure. |
| unique infinite-time functional | spatial thermodynamic limit | No | No | Yes | Unique time at each finite width does not prevent spatial phases; a chosen infinite-volume phase need not imply finite-width uniqueness by itself. |
| unique infinite-time functional | controlled continuum, Standard Model, and GR limits | No | No | Yes | State uniqueness is not renormalized continuum convergence, and a continuum construction may have several phases. |
| spatial thermodynamic limit | controlled continuum, Standard Model, and GR limits | No | No | Yes | An infinite lattice state can lack a nontrivial continuum; continuum control needs additional scaling and universality estimates. |

### N3 — hidden-condition phrase scan

| Mandated phrase | Hits and classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No use as a proof substitute. |
| `as is standard` | No hit; the RPF theorem is named and sourced explicitly. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Fixed-background transfer appears only as a tested non-load-bearing alternative route. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No hit used to grant a premise. |
| `canonical` | Defined narrowly in Section 7 as subsequence/boundary independence at fixed volume; it grants no axiom or continuum fact. |

### N4 — citation/residual matching

| Cited witness and location | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---|---|
| [Coupled OS subsequential-transfer theorem](COUPLED_OS_INTERIOR_DESCENT_SUBSEQUENTIAL_INFINITE_TIME_TRANSFER_BOUNDED_THEOREM_NOTE_2026-07-12.md), §§4--8 | At least one infinite-time accumulation functional; uniqueness open | Show every accumulation functional agrees | Yes | Sole in-repo load-bearing dependency; completed here. |
| `docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md` | Fixed-background single-particle log-transfer quasilocality | Gauge-integrated determinant interaction and state uniqueness | No | Methodological precursor only; not a graph dependency. |
| `docs/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md` | Pure-gauge convolution positivity | Dynamical gauge--fermion Gibbs uniqueness | No | Pure-gauge context only. |
| `docs/RP_MIXED_OBSERVABLE_SINGLE_TRANSFER_MATRIX_NARROW_THEOREM_NOTE_2026-05-29.md` | Algebraic positivity after a transfer representation is supplied | Noncircular all-observable uniqueness without that representation | No | Dropped as a premise. |
| Compact-alphabet RPF theorem, Cioletti--Silva and Cioletti--Lopes--Stadlbauer | Hölder potential on compact full shift has unique Gibbs/eigenprobability and boundary convergence | The exact potential proved in Sections 2--3 | Yes | Explicit external mathematical theorem, not physical input. |

### N5 — rhetoric and resolution audit

| Statement / resolution | Tested? | Permitted conclusion |
|---|---|---|
| One fixed local gauge polynomial | Yes | Full-sequence convergence. |
| Fixed-degree local fermion polynomial | Yes via (0.4) and Wick | Full-sequence convergence. |
| Full local gauge-invariant polynomial algebra | Yes element by element | One unique Euclidean functional. |
| Arbitrary nonlocal or degree-growing insertions | No | No uniform claim. |
| Antiperiodic seam placement | Yes analytically and in the runner | Same bulk limit. |
| Uniformly bounded localized boundary perturbations | Yes through one-dimensional DLR uniqueness | Same bulk limit for the stated admissible boundary class. |
| Arbitrary boundary states with zero positive-eigenfunction overlap | No | Explicitly excluded. |
| Every fixed `m>0` | Yes | Uniqueness, with a rate that may vanish as `m->0`. |
| `m=0` | No | No massless uniqueness claim. |
| Spatial-volume-uniform family | No | No thermodynamic conclusion. |

### N6 — partial-closure, convention, reframe, and primitive scan

The determinant-Hölder route closes a real mathematical wall; it is not a
renaming. The antiperiodic seam is supplied spin-structure data, and moving it
is a boundary equivalence rather than a new axiom. The old exact-transfer
route remains useful for operator identification but is no longer needed for
state uniqueness. No approved primitive supplies dynamics, weighting, or a
probability rule, and none is enlarged here. **No axiom-update stop** is
triggered.

### N7 — hostile steelman

A hostile reviewer should object that `log det D` is not literally a local
two-slice action and that compactness of each time slice alone does not forbid
one-dimensional long-range phase transitions. That objection is correct
against a naive Perron argument. Equations (0.1)--(0.4) answer it at the needed
resolution: the infinite memory is explicit, its variations decay as
`r^{R/2}`, and the potential is Hölder, not merely continuous or summable.
The RPF theorem is applied on the history space, not on a falsely local
one-slice kernel.

A second objection is that `r` approaches one at small mass. This prevents a
uniform massless or spatial-volume estimate but not the fixed-`m>0` theorem,
because `r` remains strictly below one.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Retirement mechanism and applicability |
|---|---|---|
| Free periodic-circle repair | Thermal images obstruct exact finite-circle vacuum Grams | Correct the spin structure and take infinite time; the present RPF proof controls the full limit. |
| Coupled reflected-Gram theorem | Positive adjacent form without an operator | OS quotient construction closed the operator along subsequences. |
| Coupled OS subsequential theorem | Uniform bounds gave compactness but not uniqueness | Exponential determinant/Wick variations plus RPF collapse all subsequences. |
| Fixed-background Combes--Thomas note | Gauge-background kernels are quasilocal but gauge correlations remained open | Apply the gap to the exact determinant effective action and then the gauge-history Gibbs theorem. |
| Pure-gauge Perron note | Strict positivity gives a unique pure-gauge temporal state | Fermions are included here through the exact log-determinant Hölder potential, not a scalar one-slice multiplier. |

The repeated successful mechanism is to expose the actual nonlocal tail and
bound it, rather than naming a transfer operator or declaring the tail an
irreducible wall.
