# Massive Wilson--staggered Dobrushin spatial-uniqueness wedge

**Date:** 2026-07-12  
**Type:** bounded_theorem  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/massive_wilson_staggered_dobrushin_spatial_uniqueness_wedge_2026_07_12.py`](../scripts/massive_wilson_staggered_dobrushin_spatial_uniqueness_wedge_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/massive_wilson_staggered_dobrushin_spatial_uniqueness_wedge_2026_07_12.txt`](../logs/runner-cache/massive_wilson_staggered_dobrushin_spatial_uniqueness_wedge_2026_07_12.txt)

## 0. Result

Fix the supplied four-dimensional `SU(3)` Wilson--fundamental-staggered
Euclidean model and lattice spacing. Put

```text
kappa=14/(m^2+2),
alpha_F=(3/2) kappa^2(2-kappa)/(1-kappa)^2,
alpha=18 beta+alpha_F.                                                 (0.1)
```

If

```text
m>sqrt(12),                 alpha<1,                                  (0.2)
```

then the full-four-dimensional Wilson--staggered gauge DLR state is unique.
Every admissible periodic van Hove sequence, and every finite-volume sequence
built from the infinite interaction's DLR kernels with arbitrary exterior
link configurations, converges on local gauge-invariant gauge--fermion
polynomials to that same state, without a spatial subsequence. Every cofinal
periodic regulator order whose wrap tails vanish has the same local
functional. Gauge and fixed-degree massive fermion observables have
exponential boundary mixing and exponential connected clustering.

The unique Euclidean functional is time-reflection positive and
adjacent-form positive. Its OS quotient therefore has one boundary- and
subsequence-independent positive self-adjoint two-step contraction and
logarithmic Hamiltonian at the supplied lattice spacing. On the reconstructed
gauge-invariant OS Hilbert space, the invariant vacuum is one-dimensional and
the Hamiltonian has a strictly positive spectral gap above it. “One” here
means for this supplied action and parameter point; it does not select the
microscopic action from the axioms or construct and compare every charged
superselection sector.

The wedge is explicit and nonempty:

| `m` | `kappa` | `alpha_F` | sufficient `beta` interval |
|---:|---:|---:|---:|
| `6` | `0.368421` | `0.832785` | `0<=beta<0.0092897` |
| `8` | `0.212121` | `0.194392` | `0<=beta<0.0447560` |
| `10` | `0.137255` | `0.070719` | `0<=beta<0.0516267` |

At `beta=0`, condition (0.2) begins at `m>5.8090575...`. These are coarse
sufficient bounds, not phase-transition locations. Failure of (0.2) says
nothing about nonuniqueness.

The theorem does not reach `beta=6`, light or massless fermions, a continuum
limit, Lorentz/QFT recovery, the Standard Model, or GR. It does not derive the
Euclidean or physical probability rule. No axiom-update stop is established.

## 1. Supplied model and direct dependency

Use the same Wilson action, staggered phases, Haar link measure,
antiperiodic temporal spin structure, reflection-compatible regulator family,
and local gauge-invariant polynomial algebra as the
[massive spatial DLR accumulation and OS-transfer theorem](MASSIVE_WILSON_STAGGERED_SPATIAL_DLR_ACCUMULATION_OS_TRANSFER_BOUNDED_THEOREM_NOTE_2026-07-12.md).
That theorem is the sole direct in-repo science dependency. It supplies DLR
existence, volume-uniform massive Wick locality, and the state-specific OS
passage for all `beta>=0,m>0`. The present note adds a strict influence bound
which collapses all of those accumulation states inside (0.2).

The Wilson-staggered action, `SU(3)`, `beta`, `m`, lattice spacing, spin
structure, and boundary/exhaustion class remain supplied inputs. The four
named axioms are Lattice, Qubit, Admissibility, and Record; they do not select
those model inputs.

Periodic approximants have every extent at least four. This excludes only the
irrelevant extent-two wrap degeneracy in the two-hop path split below.

## 2. Exact nonbacktracking two-hop expansion

At one infinite-lattice site the anti-Hermitian staggered hop `M` has eight
oriented nearest-neighbor terms, each of block norm `1/2`. In `M^2`, every
oriented first hop has one immediate reverse. Each reverse pair contributes
`-I_3/4`, so the eight reversals sum to `-2I_3`. The other
`8(8-1)=56` ordered two-hop paths are nonbacktracking. Hence

```text
M^2=-2I+R,                                                            (2.1)
```

where `R` has zero diagonal and absolute color-block row sum at most

```text
56/4=14.                                                              (2.2)
```

The operator spectrum gives the same safe norm: `spec(M^2) subset [-16,0]`,
so `spec(R) subset [-14,2]` and `||R||<=14`.

Now

```text
A=D^dagger D=m^2I-M^2=(m^2+2)I-R,
K=R/(m^2+2).                                                          (2.3)
```

For `m>sqrt(12)`, both the operator norm and the absolute path-row norm of
`K` are bounded by `kappa<1`. The real determinant therefore has the exact
absolutely path-convergent expansion

```text
log det D
 =(dim D/2)log(m^2+2) -(1/2)sum_(n>=1)Tr(K^n)/n.                      (2.4)
```

There is no order-one gauge interaction because `Tr K=0`: a nonbacktracking
two-hop path cannot close on the infinite cubic lattice. Periodic extents at
least four have the same property.

Pair every oriented closed path with its reverse/conjugate. This makes each
interaction real and gauge invariant. Triangle inequalities below count both
members, so no cancellation is used.

## 3. One-link Dobrushin comparison lemma

Treat every positive-oriented gauge link as one compact spin with normalized
Haar a priori measure. For an interaction energy `Psi_X`, use the sup norm
`||Psi_X||_infinity`. If exterior configurations differ only at link `f`, the
change in the one-link energy at `e` is a real function `h(U_e)` with

```text
osc h<=4 sum_(X contains e,f)||Psi_X||_infinity.                       (3.1)
```

For two normalized densities whose log ratio has oscillation `delta`, the
elementary likelihood-ratio extremum gives

```text
||gamma_e(.|eta)-gamma_e(.|eta')||_TV<=tanh(delta/4).                  (3.2)
```

Combining (3.1), (3.2), and `tanh x<=x` gives the safe influence bound

```text
c_(e,f)<=sum_(X contains e,f)||Psi_X||_infinity,
sum_f c_(e,f)
 <=sum_(X contains e)(|X|-1)||Psi_X||_infinity.                       (3.3)
```

No factor is hidden in the total-variation convention: here
`||mu-nu||_TV=sup_A|mu(A)-nu(A)|=(1/2)||dmu-dnu||_1`.

The Dobrushin uniqueness/comparison theorem says that
`sup_e sum_f c_(e,f)<1` gives one DLR state and boundary-condition
convergence. Its exponentially weighted comparison form gives exponential
boundary influence and covariance decay when the corresponding weighted row
norm is below one. The external mathematical reference for this
uniqueness/regularity machinery is R. L. Dobrushin, *Theory of Probability and
Its Applications* **13** (1968) 197--224, DOI
[`10.1137/1113026`](https://doi.org/10.1137/1113026). The work specific to
this model is the Wilson and rooted-loop evaluation of (3.3).

## 4. Wilson row bound

One link belongs to `2(4-1)=6` plaquettes in four dimensions. Each plaquette
contains three other link spins, and

```text
Psi_p^W=-(beta/3)Re Tr U_p,             ||Psi_p^W||_infinity<=beta.   (4.1)
```

Equation (3.3) therefore gives

```text
alpha_W<=6*3*beta=18beta.                                      (4.2)
```

The bound deliberately uses the sup norm, not the smaller oscillation range
of `Re Tr` on `SU(3)`. It is coarse but convention-safe.

## 5. Fermion rooted-loop incidence bound

At logarithm order `n`, root `x`, the sum of the norms of all closed-path
terms is at most

```text
(3/(2n))kappa^n.                                                       (5.1)
```

The factor three bounds the color trace, `1/(2n)` is the coefficient in
(2.4), and the absolute `K` path-row sum is at most `kappa`.

Each order-`n` path traverses `2n` gauge-link occurrences and has interaction
support of cardinality at most `2n`. Sum occurrence-weighted path norms over
all roots first on equal-extent periodic four-cubes, or directly on `Z^4`.
Translation invariance and the hypercubic coordinate-permutation bijections of
the absolute path family distribute the `2n` occurrences equally over the
four positive-link orientations. Dividing by the four links per site gives,
for every fixed positive-oriented link `e`,

```text
sum_(order-n paths p: e in support p)||Psi_p||_infinity
 <=3 kappa^n/4.                                                        (5.2)
```

Using `|support p|-1<=2n-1<=2n` in (3.3), and recalling that order one
vanishes, gives

```text
alpha_F
 <=(3/2)sum_(n>=2)n kappa^n
 =(3/2) kappa^2(2-kappa)/(1-kappa)^2.                                 (5.3)
```

This is a mass-transport/incidence estimate, not a claim that every path has
`2n` distinct links. Repetitions only reduce the support factor. The resulting
infinite-lattice per-link bound is exhaustion-independent; unequal finite
rectangles are not assigned a coordinate-permutation symmetry they lack.
Closed-path cancellations would improve (5.3) but are not used.

Adding (4.2) and (5.3) proves `sup_e sum_f c_(e,f)<=alpha`. Condition (0.2)
is therefore a sufficient Dobrushin uniqueness criterion.

## 6. Full-sequence gauge--fermion and OS consequences

The spatial accumulation theorem proves that every periodic van Hove sequence
has DLR accumulation points. Dobrushin uniqueness makes all of them equal, so
the full sequence converges. The comparison theorem also gives convergence
for the infinite interaction's finite-volume DLR kernels uniformly over
arbitrary exterior link configurations. This does not silently identify those
kernels with an unproved open-boundary finite Dirac determinant.

Regulator-order interchange uses the same accumulation argument, not only a
formal exchange of limits. For joint cofinal periodic four-tori, the uniform
interaction and wrap-tail bounds make every accumulation point a DLR state of
the infinite specification. For the spatial-first order, take the spatial DLR
limit at each fixed temporal circle and then let the antiperiodic circumference
grow; the seam and wrap contributions to any fixed local conditional identity
vanish exponentially. Every accumulation point is again a DLR state of the
same infinite specification. Uniqueness identifies all these accumulation
points with the time-first state and upgrades each compactness statement to
full-sequence local convergence.

The strict wedge actually implies `m>5.809...>4`. Hence the direct hopping
series converges absolutely and gives the off-diagonal bound

```text
|(D^(-1))_(x,y)|
 <=[m(1-4/m)]^(-1)(4/m)^dist(x,y).                                   (6.1)
```

Every fixed-degree Wick insertion is an exponentially quasilocal function of
the gauge field. Gauge-marginal uniqueness therefore gives one full local
gauge--fermion functional, not only one gauge measure.

The interaction influence has an exponential moment. Indeed insert a factor
`exp(lambda dist(e,f))` into (3.3). The Wilson term remains finite and the
fermion sum is bounded by the same polynomial series with
`kappa exp(2lambda)` in place of `kappa`. Since `alpha<1` strictly, a small
`lambda>0` keeps the weighted row sum below one. The Dobrushin comparison
bound then gives exponential boundary mixing and connected clustering for
local gauge functions. For two distant fermion polynomials, expand the joint
Wick determinant into contractions internal to each support plus cross-support
contractions. The cross contractions obey (6.1); the internal pieces are
exponentially quasilocal gauge functions and their connected gauge covariance
obeys the weighted Dobrushin bound. Truncating their gauge tails and combining
the two errors proves exponential connected clustering for every fixed-degree
local gauge--fermion pair.

Reflection positivity, adjacent positivity, and the contraction inequalities
hold on every finite regulator and pass to the unique limit. The OS transfer
and Hamiltonian constructed in the spatial accumulation theorem are therefore
independent of spatial subsequences and admissible boundaries inside the
wedge.

There is also a spectral corollary on this reconstructed gauge-invariant
Hilbert space. Let `Omega=[1]` and let `v=[F-omega(F)]` be a centered local OS
vector. The common weighted Dobrushin rate and the cross-Wick argument give

```text
0<=<v,T_2^n v><=C_v rho^n,             0<rho<1,                       (6.2)
```

with one `rho` valid for the dense local algebra. Because `T_2` is positive
self-adjoint, its spectral measure for `v` is positive. Equation (6.2) forces
that measure to be supported in `[0,rho]`: any mass above `rho+epsilon` would
eventually violate the bound. Centered local vectors are dense in
`Omega^perp`, so

```text
spec(T_2|_(Omega^perp)) subset [0,rho].                               (6.3)
```

Thus `Omega` spans the `T_2=1` eigenspace and

```text
Delta_OS>=-(2a_tau)^(-1)log rho>0.                                   (6.4)
```

This is a gap for the supplied gauge-invariant OS reconstruction. It is not a
continuum Yang--Mills mass-gap theorem and says nothing about unconstructed
charged-sector Hilbert spaces.

## 7. Runner contract

Run:

```bash
python3 scripts/massive_wilson_staggered_dobrushin_spatial_uniqueness_wedge_2026_07_12.py
```

The runner independently enumerates the eight oriented hops and 56
nonbacktracking two-hop words, checks the `-2I+R` split on finite random-link
carriers, verifies the absolute row norm `14`, enumerates low-order closed
rooted paths to test orientation-incidence symmetry, checks the Dobrushin
oscillation/TV lemma on sampled finite distributions, evaluates the analytic
row sums and thresholds, and enforces the source boundary/N1--N8 contract.
The uniqueness theorem is external mathematics; the runner checks the actual
model-specific influence hypotheses.

The random finite matrix certificate uses a four-dimensional scalar `U(1)`
link carrier. The actual `SU(3)` dependence is analytic: unitary color-block
norm for each hop and the explicit color-trace factor three in (5.1). The
four-dimensional constants are carried by the exact eight-hop/56-word
enumeration and the four-orientation incidence proof, not inferred from the
abelian sample.

## 8. Honest boundary and next theorem

This theorem supplies a controlled full-sequence infinite-volume region, but
the region is far from `beta=6` and from light fermions. It is a constructive
base point for a lattice-spacing/RG campaign, not a Standard Model continuum
limit.

The next leverage target is to choose a scaling trajectory that remains
inside a rigorously controlled region while sending the lattice spacing to
zero, then determine whether the limit is nontrivial or Gaussian. If every
controlled trajectory is trivial, that is a continuum-analysis result, not an
axiom-update result unless all live regulator/action routes are also closed.

## 9. No-Go Discipline N1--N8

This positive uniqueness theorem names large open regions. The checklist
prevents failure of the sufficient criterion from being called a no-go.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it does not close more than claimed |
|---|---|---|---|
| Nonbacktracking `R`-loop Dobrushin bound | `ATTEMPTED` | Equations (2.1)--(5.3) give the explicit nonempty wedge. | It is only sufficient and intentionally coarse. |
| Original massive `Q`-loop Dobrushin bound | `ATTEMPTED` | Its absolute path-row radius is `32/(m^2+16)`, requiring `m>4` and producing a looser but live wedge. | It does not extend to light mass or `beta=6`. |
| Pure-gauge polymer/Kotecky--Preiss expansion | `ATTEMPTED` | Existing repo science gives a small-`beta` pure-gauge floor. | The dynamical determinant needs its own polymer accounting. |
| Dobrushin--Shlosman block criterion | `ATTEMPTED` | Block influences can improve a failed one-link bound. | No optimized block computation is supplied here. |
| Reflection/chessboard estimates | `ATTEMPTED` | Reflection positivity survives and this route remains live. | No phase-selecting chessboard inequality for this action is proved. |
| Positivity-improving transfer/Perron route | `ATTEMPTED` | Finite-volume simplicity is available in related gauge kernels. | It gives no uniform spatial gap by itself. |
| Constructive RG | `ATTEMPTED` | The exact massive loop interaction is a valid local RG input. | No running-coupling or continuum bound is supplied. |
| Numerical finite-size scaling | `ATTEMPTED` | It could map a larger empirical phase region. | It cannot replace the theorem-grade uniform comparison bound. |

### N2 — wall-independence audit

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? | Witness |
|---|---|---:|---:|---:|---|
| supplied Wilson-staggered action | strict Dobrushin inequality | No | No | Yes | Action selection and a parameter estimate are distinct. |
| supplied Wilson-staggered action | positive mass | No | No | Yes | The action family includes multiple masses. |
| supplied Wilson-staggered action | spatial uniqueness | No | No | Yes | A supplied action can have phases. |
| supplied Wilson-staggered action | continuum/SM/GR closure | No | No | Yes | Regulator choice does not establish universality or dynamical geometry. |
| strict Dobrushin inequality | positive mass | No | No | Yes | The inequality uses mass but positive mass alone does not imply it; other criteria can work without it. |
| strict Dobrushin inequality | spatial uniqueness | Yes | No | No | Dobrushin is the sufficient mechanism proving uniqueness here; do not count these as independent walls. |
| strict Dobrushin inequality | continuum/SM/GR closure | No | No | Yes | A unique lattice state need not have the target continuum. |
| positive mass | spatial uniqueness | No | No | Yes | Massive matter does not exclude gauge phases. |
| positive mass | continuum/SM/GR closure | No | No | Yes | A fixed bare mass is not a continuum theorem. |
| spatial uniqueness | continuum/SM/GR closure | No | No | Yes | Phase uniqueness and scaling/universality are distinct. |

The collapsed independent downstream wall set is action selection plus
continuum/universality/dynamical-geometry closure. Spatial uniqueness is the
conclusion inside the Dobrushin condition, not an extra wall there.

### N3 — hidden-condition phrase scan

| Mandated phrase | Hits and classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No use as a proof substitute. |
| `as is standard` | No hit; Dobrushin is named and sourced. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Boundary backgrounds are explicit DLR variables, not hidden premises. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No hit used to grant a premise. |
| `canonical` | Avoided as an unqualified claim; boundary/subsequence independence is stated only inside the wedge for the supplied action. |

### N4 — citation/residual matching

| Cited witness and location | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Massive spatial DLR accumulation and OS transfer](MASSIVE_WILSON_STAGGERED_SPATIAL_DLR_ACCUMULATION_OS_TRANSFER_BOUNDED_THEOREM_NOTE_2026-07-12.md), Sections 2--6 | DLR/OS accumulation states exist; spatial uniqueness open | Collapse every accumulation state in an explicit parameter wedge | Yes | Sole direct in-repo dependency. |
| Massive fixed-spatial-volume Ruelle uniqueness | Temporal-history uniqueness at finite spatial width | Three-dimensional spatial phase uniqueness | No | Transitive context only. |
| Pure-gauge strong-coupling floor | Small-`beta` gauge polymers without dynamical determinant | Coupled Wilson-staggered uniqueness | No | Context only. |
| Finite-volume pure-gauge Perron theorem | Simple finite-volume top state | Uniform spatial thermodynamic uniqueness | No | Context only. |
| Dobrushin 1968 uniqueness and weighted comparison/regularity theorem | Unweighted influence row below one gives one Gibbs field and boundary convergence; a weighted row below one gives the exponential comparison/covariance decay used in (6.2) | Equations (3.3)--(5.3) verify the unweighted row, Section 6 verifies a nearby exponential weight remains below one, and the internal positive-spectral-measure argument converts decay to the OS gap | Yes | Explicit external mathematics. |

### N5 — rhetoric and resolution audit

| Statement / resolution | Tested? | Permitted conclusion |
|---|---:|---|
| One link conditional influence | Yes | Row bound (0.1). |
| All links on the infinite lattice | Yes by translation/orientation incidence | Uniform Dobrushin constant. |
| Every local gauge polynomial | Yes | Full-sequence convergence and exponential mixing. |
| Every fixed-degree local gauge--fermion polynomial | Yes via massive Wick quasilocality | Same unique functional and clustering. |
| Reconstructed gauge-invariant OS Hilbert space | Yes via weighted clustering and positive spectral measures | One invariant vacuum and a positive gap at fixed lattice spacing. |
| Unconstructed charged superselection sectors | No | No cross-sector vacuum or gap claim. |
| Volume-growing/nonlocal observables | No | No convergence claim. |
| Points satisfying strict (0.2) | Yes | Unique DLR/OS functional. |
| Points failing (0.2) | No | No claim of coexistence or nonuniqueness. |
| `beta=6` or light/massless fermions | No | Explicitly open. |
| Continuum trajectories | No | No Lorentz/QFT/SM/GR claim. |

### N6 — partial-closure, convention, reframe, and primitive scan

The wedge and the gauge-invariant OS gap are analytic consequences, not a convention or new
premise. The approved primitives supply no Wilson action, coupling, mass,
Euclidean weight, probability rule, or Dobrushin constant. No primitive is
enlarged. Block criteria, polymer expansions, chessboard estimates, and RG
remain live outside the wedge. **No axiom-update stop** is triggered.

### N7 — hostile steelman

A hostile reviewer should attack the factor `3/4` in (5.2): bounding the
total path weight from one root does not by itself bound paths through one
fixed link. The required extra step is mass transport over all roots. Every
closed order-`n` path has `2n` link occurrences; translation invariance and
absolute coordinate-permutation symmetry distribute their total equally over
the four positive orientations. Multiplying the per-root bound
`3kappa^n/(2n)` by `2n/4` gives `3kappa^n/4`. Without that symmetry/incidence
step the claimed wedge would be unsupported.

A second hostile reviewer should note that Dobrushin failure is common near
interesting critical regions. Correct: (0.2) is only a certified uniqueness
wedge. It neither estimates the physical phase boundary nor gives evidence of
multiple phases outside it.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Retirement mechanism and applicability |
|---|---|---|
| Massive temporal Ruelle uniqueness | A strict contraction made a one-dimensional Gibbs state unique | Here a strict link-influence row makes the four-dimensional state unique only in a parameter wedge. |
| Spatial DLR accumulation theorem | Compactness/locality proved existence but permitted phases | Dobrushin comparison collapses those phases where (0.2) holds. |
| Pure-gauge strong-coupling work | Polymer smallness produced a controlled gauge region | The present loop expansion includes the actual massive determinant. |
| Finite-volume Perron work | Finite simplicity did not control infinite volume | A volume-uniform conditional-influence estimate supplies the missing thermodynamic comparison. |
| Beta-six plaquette work | Exact local data did not determine one bulk observable | This wedge does not reach beta six and does not overread existence as value uniqueness there. |

The result retires one controlled-region phase-selection wall and leaves the
physically broader region open.
