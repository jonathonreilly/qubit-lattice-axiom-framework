# Coupled OS interior descent and subsequential infinite-time transfer

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; independent audit alone assigns retained status.
**Primary runner:** [`scripts/coupled_os_interior_descent_subsequential_infinite_time_transfer_2026_07_12.py`](../scripts/coupled_os_interior_descent_subsequential_infinite_time_transfer_2026_07_12.py)
**Cached output:** [`logs/runner-cache/coupled_os_interior_descent_subsequential_infinite_time_transfer_2026_07_12.txt`](../logs/runner-cache/coupled_os_interior_descent_subsequential_infinite_time_transfer_2026_07_12.txt)

## 0. Result

This note proves two related but deliberately distinct results for the finite
spatial-volume `SU(3)` Wilson--fundamental-staggered model supplied in the
[coupled two-seam reflected-Gram theorem](COUPLED_PERIODIC_TWO_SEAM_SU3_WILSON_STAGGERED_REFLECTED_GRAM_BOUNDED_THEOREM_NOTE_2026-07-12.md).

First, there is exact **finite-circle interior null descent**. On every
support-controlled core for which both the original observable and its
two-step translate remain in the required positive halves,

```text
B_2(F,G)=B_0(F,tau_2 G)                                               (0.1)
```

kills the `B_0` null space in either slot. Thus the adjacent form descends to
the corresponding OS quotient. Every finite-dimensional descended core has a
finite generalized-spectrum domination constant. It need not be a
contraction: in the exact `Z_3` finite-circle certificate,

```text
B_2(n_2,n_2)/B_0(n_2,n_2)=29/25>1.                                  (0.2)
```

Accordingly, no transfer operator on the broad finite thermal cylinder is
claimed.

Second, at fixed finite spatial volume and `m>0`, normalized local
correlators have bounds uniform in the even temporal circumference. A
diagonal subsequence as `L_t=2N -> infinity` therefore defines an infinite-time
Euclidean accumulation functional. Reflection positivity, two-step
translation invariance, and adjacent-form positivity pass to that limit. On
its OS quotient, `tau_2` descends to a **positive self-adjoint contraction**
`T_2`. On `(ker T_2)^perp`,

```text
H=-(2 a_tau)^(-1) log T_2 >= 0,      T_2=exp(-2 a_tau H),              (0.3)
```

and spectral calculus supplies the Euclidean semigroup and the unitary
real-time group `exp(-itH)` on that support.

The theorem is subsequential: it **does not prove uniqueness** or boundary
independence of the infinite-time limit. It proves neither the spatial
thermodynamic limit nor a continuum, Lorentz, interacting-QFT, Standard
Model, or gravitational limit. The Wilson-staggered action and its
spin/reflection structure remain supplied model content, not deductions from
the four axioms. No axiom-update stop is established.

## 1. Setting and dependency

Use exactly the finite cylinders, action, antiperiodic spin structure,
reflections `theta_j`, translations `tau_2`, and individually gauge-invariant
cylinder algebra of the coupled two-seam theorem, with

```text
beta>=0,   m>0,   L_t=2N,                                             (1.1)
```

and fixed finite bipartite spatial volume. The coupled periodic two-seam
reflected-Gram theorem is the sole load-bearing graph dependency: it supplies
`B_0>=0`, the adjacent identity, and `B_2>=0` on support-admissible cores. The older free two-step transfer
note is only a normalization benchmark; its free Fock construction is not
imported into this interacting proof. Likewise, the older fixed-background
gauge extension is not used because the gauge links here remain dynamical.

These supplied conditions matter. This note does not derive `SU(3)`, the
Wilson action, staggered fermions, `beta`, `m`, the reflection, the spin
structure, the observable algebra, or the two-step time unit from the axioms.

## 2. Finite-circle interior descent

Let `D_N` be any linear core inside the `theta_0` positive algebra such that
`tau_2 D_N` remains there and all translated supports also lie in the
`theta_1` positive algebra required by the adjacent identity. For example,
when `N>=3`, polynomials on the first positive boundary slice have a
two-step translate strictly inside the positive semicircle.

Define

```text
<F,G>_0=B_0(F,G)=omega_N(theta_0(F)G),
q_N(F)=B_0(F,F),
N_N={F:q_N(F)=0}.                                                     (2.1)
```

The coupled periodic two-seam reflected-Gram identity gives (0.1). If
`F in N_N`, OS Cauchy--Schwarz gives

```text
|B_2(F,G)|^2=|B_0(F,tau_2 G)|^2
             <=q_N(F) q_N(tau_2 G)=0.                                (2.2)
```

Hermiticity of the positive form `B_2` kills the other slot. Hence `B_2`
defines a positive sesquilinear form on `D_N/(D_N cap N_N)`. This is null
descent of a form. It does not, by itself, define an invariant operator on a
completed finite-circle Hilbert space because repeated forward translation
eventually reaches the far seam.

For a finite-dimensional subcore with Gram matrices `G_0,G_2`, descent and
positivity imply a finite constant

```text
c_D=lambda_max(G_0^(-1/2) G_2 G_0^(-1/2)),
0<=G_2<=c_D G_0,                                                       (2.3)
```

where the inverse is taken on the support of `G_0`. Nothing here makes
`c_D<=1` or makes the constants uniform over increasing cores.

## 3. Exact finite-circle contraction boundary

The primary runner reuses the exact `L_t=6`, `Z_3`, three-color enumeration
from the coupled periodic two-seam reflected-Gram supplier. On the
six-observable first-boundary core

```text
{1,n_1,W_1,W_1 n_1,B_1,bar B_1},                                     (3.1)
```

the generalized spectrum of `(G_2,G_0)` is nonnegative with maximum `1`.
That is a finite-group check, not an `SU(3)` contraction proof.

On the broader eleven-observable multi-slice core, the generalized maximum
is approximately `191.4036`. More sharply, the gauge-invariant density
`n_2=bar chi_(2,0) chi_(2,0)` obeys the exact relation (0.2). Both reflected
forms remain positive. Thus two-plane reflection positivity, strict local
crossing kernels, and finite null descent do not imply `B_2<=B_0` on arbitrary
finite-circle multi-slice cores. A scalar normalization cannot repair this
while preserving the vacuum generalized eigenvalue `1`.

This counterexample blocks only the overbroad finite thermal claim. It does
not block an infinite-time OS reconstruction, whose norm argument uses
uniform bounds across all forward translates rather than finite-circle
contraction.

## 4. Uniform local-correlator bounds

Write the staggered matrix as

```text
D_N[U]=m I+M_N[U],     M_N[U]^dagger=-M_N[U].                          (4.1)
```

Therefore every singular value of `D_N` is at least `m` and

```text
||D_N[U]^(-1)||<=1/m                                                       (4.2)
```

uniformly in `N` and in every gauge configuration. Bipartite spectral pairing
at `m>0` gives a strictly positive determinant, so after integrating the
Grassmann variables the normalized gauge measure is a probability measure.
Every fixed-degree fermion correlator is a finite sum of Wick minors; a
degree-`2k` minor is bounded by a dimension-only multiple of `m^(-k)`.
Gauge-link polynomials are bounded on compact `SU(3)`. Consequently, for
every fixed local gauge-invariant polynomial `F`,

```text
sup_N |omega_N(F)| < infinity,                                        (4.3)
```

and the same bound holds for all time translates of `F`, independent of
their separation whenever the cylinder is large enough to contain them.

The runner exhaustively checks (4.2) in its finite-group supplier for
`m in {0.2,1,3}`. That enumeration is a certificate of implementation and
normalization; the anti-Hermitian argument above is the `SU(3)` proof.

## 5. Diagonal subsequence and inherited structure

Choose a countable basis `{P_r}` of finite-support gauge-invariant cylinder
polynomials with rational complex coefficients and all integer two-step
translates. By (4.3), each sequence `omega_N(P_r)` is bounded. Repeated
Bolzano--Weierstrass extraction and diagonalization produce

```text
N_l -> infinity,
omega_infinity(P_r)=lim_(l->infinity) omega_(N_l)(P_r)                 (5.1)
```

simultaneously for all `r`. Linearity defines the subsequential infinite-time
functional on the local polynomial algebra.

Every reflection-positivity and adjacent-positivity test is a finite Gram
inequality involving finitely many local polynomials. For sufficiently large
`N_l`, its supports do not encounter the remote seam. Taking the limit
preserves

```text
omega_infinity(1)=1,
omega_infinity(tau_2 F)=omega_infinity(F),
omega_infinity(theta_0(F)F)>=0,
omega_infinity(theta_0(F)tau_2(F))>=0.                                (5.2)
```

The reflected mixed identities and Hermiticity pass to the limit in the same
way. This construction proves existence of at least one accumulation
functional. It does not show that distinct subsequences agree.

## 6. Infinite-time OS quotient and transfer

Let `A_+^loc` be the positive-time local polynomial algebra, quotient by

```text
N={F:omega_infinity(theta_0(F)F)=0},                                  (6.1)
```

and complete it to `H_OS`. Define initially on local equivalence classes

```text
T_2[F]=[tau_2 F].                                                      (6.2)
```

Unlike on a finite semicircle, every forward two-step translate remains in
`A_+^loc`. Reflection covariance and translation invariance give

```text
<F,T_2G>=<T_2F,G>.                                                     (6.3)
```

If `F in N`, then for every local `G`, (6.3) and OS Cauchy--Schwarz give
`<G,T_2F>=<T_2G,F>=0`; hence (6.2) is well defined. Adjacent positivity gives

```text
<F,T_2F> >= 0                                                         (6.4)
```

so `T_2` is positive and symmetric on the dense local domain.

For fixed local `F`, put

```text
a_n=||T_2^n F||^2.                                                     (6.5)
```

Uniform translated-correlator bounds make `{a_n}` bounded. Cauchy--Schwarz
and symmetry give

```text
a_n^2<=a_(n-1) a_(n+1),                                               (6.6)
```

so it is a bounded log-convex nonnegative sequence. Its nonzero successive
ratios are nondecreasing; boundedness forbids any ratio greater than one.
Zeros are handled by (6.6). Therefore `a_(n+1)<=a_n`, in particular

```text
||T_2F||<=||F||.                                                       (6.7)
```

The operator extends uniquely to a bounded positive self-adjoint contraction
on `H_OS`. Spectral calculus on `H_0=(ker T_2)^perp` defines (0.3), possibly
with unbounded `H`, and gives

```text
exp(-sH), s>=0,              exp(-itH), t in R.                        (6.8)
```

The first is a strongly continuous contraction semigroup and the second a
unitary group on `H_0`. This is a fixed-spatial-volume, subsequential
infinite-time reconstruction. It is not yet a continuum Lorentzian QFT.

## 7. Runner contract

Run:

```bash
python3 scripts/coupled_os_interior_descent_subsequential_infinite_time_transfer_2026_07_12.py
```

The runner checks the boundary-core generalized spectrum, the exact `29/25`
counterexample, broad-core noncontraction, the massive resolvent bound in the
finite-group supplier, a bounded log-convex spectral-moment example, a finite
null-descent model, and the source-note boundary contract. Its finite-group
data do not replace the analytic `SU(3)` arguments.

## 8. Honest boundary and next theorem

This note proves existence, not canonicity. It does not prove uniqueness of
the `L_t -> infinity` functional, convergence without subsequences,
boundary-condition independence, a unique vacuum, a gap, clustering, a
spatial thermodynamic limit, or any continuum limit. It also does not derive
the supplied Wilson-staggered dynamics or probability law from the four
axioms.

The highest-leverage next theorem is a coupled two-step kernel or quantitative
mixing theorem that makes the infinite-time state unique and removes the
subsequence. Only after that should the campaign attempt the spatial
thermodynamic and controlled continuum limits.

## 9. No-Go Discipline N1--N8

The note contains two negative boundaries: the supplied positive forms do not
logically imply contraction on every finite-circle core, and the present
construction does not prove a unique infinite-time limit. The full discipline
keeps both statements at the resolutions actually tested.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it does not close the remaining boundary / authority surface |
|---|---|---|---|
| Direct generalized spectrum on a broad finite core | `ATTEMPTED` | The primary runner computes the direct `G_0,G_2` pair and obtains `29/25` on `n_2` and maximum `191.4036`. | This is an exact `L_t=6` `Z_3` analogue, so it proves a countermodel to implication from the named premises, not an `SU(3)` noncontraction theorem. |
| Restrict to the first-boundary core | `ATTEMPTED` | The same direct computation gives spectrum in `[0,1]` with maximum `1`. | This succeeds partially and forces the negative statement to exclude a universal boundary-core failure. |
| Scalar normalization preserving the vacuum | `ATTEMPTED` | The runner checks the vacuum generalized eigenvalue is `1`; a common normalization cancels from `G_2/G_0`. | Scaling enough to remove `29/25` would move the vacuum eigenvalue away from `1`. |
| Finite quotient domination | `ATTEMPTED` | Equation (2.3) gives a finite Riesz constant on every finite descended core. | It closes boundedness core by core but gives neither `c_D<=1` nor a cutoff-uniform constant. |
| Strict positive seam kernel | `ATTEMPTED` | The supplier's exact `Z_3` seam spectrum is `{1,1,4}`, yet the density ratio is `29/25`. | Kernel faithfulness alone does not imply global finite-circle contraction after side integration. |
| Uniform massive bounds followed by infinite time | `ATTEMPTED` | Sections 4--6 prove subsequential extraction and a positive contraction on the resulting infinite-time OS quotient. | This retires the need for finite-circle contraction along one subsequence, but it does not prove full-sequence uniqueness. |
| Exact interacting two-step kernel plus positivity-improving Perron theorem | `ATTEMPTED` | The existing free and fixed-gauge-background transfer sources were read; neither constructs the dynamical gauge-integrated kernel required here. | This remains the strongest uniqueness route and requires a new exact representation rather than a citation. |
| Direct boundary comparison, cluster expansion, or one-dimensional Gibbs uniqueness | `ATTEMPTED` | The current uniform bounds give precompactness but no decay, Cauchy estimate, Dobrushin constant, or spectral gap. | Any of these estimates could upgrade subsequential existence in a controlled parameter region; none is proved by the current artifacts. |

The two successful partial routes are retained in the theorem. The unresolved
conclusion is “uniqueness not proved,” never “uniqueness is impossible.”

### N2 — wall-independence audit

The collapsed residual set uses descriptive scientific names. “Action
selection” includes the probability-bearing Euclidean weight; it is not split
again into a downstream normalization wall.

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? | Witness |
|---|---|---|---|---|---|
| supplied action and dynamics | supplied spin and reflection | No | No | Yes | An action does not select a temporal spin realization; a reflection convention does not select an action. |
| supplied action and dynamics | unique boundary-independent infinite-time state | No | No | Yes | A fixed action may have phases; state uniqueness would not derive that action from the axioms. |
| supplied action and dynamics | spatial thermodynamic limit | No | No | Yes | Finite-volume dynamics and spatial infrared control are distinct. |
| supplied action and dynamics | controlled Lorentz, QFT, and Standard Model continuum | No | No | Yes | A microscopic action need not have the desired universality class, and a continuum description need not select its regulator. |
| supplied action and dynamics | dynamical gravity and GR limit | No | No | Yes | Matter dynamics does not supply a dynamical metric; a GR limit does not select this matter regulator. |
| supplied spin and reflection | unique boundary-independent infinite-time state | No | No | Yes | Positivity does not imply mixing, and uniqueness does not fix the reflection convention. |
| supplied spin and reflection | spatial thermodynamic limit | No | No | Yes | Spin structure and spatial infrared control are logically separate. |
| supplied spin and reflection | controlled Lorentz, QFT, and Standard Model continuum | No | No | Yes | Reflection positivity is reconstruction input, not a universality theorem; a continuum theory does not uniquely choose lattice spin data. |
| supplied spin and reflection | dynamical gravity and GR limit | No | No | Yes | Temporal reflection data and gravitational dynamics supply different content. |
| unique boundary-independent infinite-time state | spatial thermodynamic limit | No | No | Yes | Fixed spatial volume can have a unique temporal state while the spatial limit has phases, and conversely. |
| unique boundary-independent infinite-time state | controlled Lorentz, QFT, and Standard Model continuum | No | No | Yes | Vacuum uniqueness does not prove renormalized convergence, and a controlled continuum need not prove uniqueness of every finite-regulator boundary limit. |
| unique boundary-independent infinite-time state | dynamical gravity and GR limit | No | No | Yes | State uniqueness and dynamical geometry are distinct. |
| spatial thermodynamic limit | controlled Lorentz, QFT, and Standard Model continuum | No | No | Yes | An infinite lattice state may lack a nontrivial relativistic continuum, while a finite-volume continuum construction does not by itself establish the thermodynamic state. |
| spatial thermodynamic limit | dynamical gravity and GR limit | No | No | Yes | Spatial-volume control neither derives nor follows from Einstein dynamics. |
| controlled Lorentz, QFT, and Standard Model continuum | dynamical gravity and GR limit | No | No | Yes | A controlled matter QFT limit does not recover GR; a gravity limit does not derive the Standard Model. |

All fifteen pairs are bidirectionally negative; no residual is downstream of
another strongly enough to collapse the set further.

### N3 — hidden-condition phrase scan

The mandated phrases were scanned in this note, the sole load-bearing parent,
and the two contextual transfer notes:

| Mandated phrase | Hits and classification |
|---|---|
| `we assume` | No load-bearing hit in this note. |
| `by construction` | No use in this note as a proof substitute. |
| `as is standard` | No hit in this note. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | The two `fixed-background` hits in Sections 1 and N4 classify an older source as non-load-bearing context; they grant no premise. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No hit used to grant a premise. |
| `canonical` | Hits occur only in the older free contextual note's supplied staggered-phase language; that source is not load bearing here. |

A second rhetoric scan covered “only,” “cannot,” “forces,” “therefore
unique,” “the transfer matrix,” “the vacuum,” and “the continuum.” Every live
claim is restricted by finite spatial volume, `m>0`, support control, the
finite-group analogue, or a named subsequence.

### N4 — citation/residual matching

| Cited witness and location | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---|---|
| [Coupled periodic two-seam reflected-Gram theorem](COUPLED_PERIODIC_TWO_SEAM_SU3_WILSON_STAGGERED_REFLECTED_GRAM_BOUNDED_THEOREM_NOTE_2026-07-12.md), §0 equation (0.2) and §7 | Positive `B_0,B_2` and adjacent identity, with descent/contraction open | Descend the form and reconstruct an infinite-time contraction | Yes | Sole load-bearing dependency; partially closed here. |
| `docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`, claim and Steps 3--4 | Free action-derived decaying transfer channel | Dynamical gauge-integrated interacting reconstruction | No | Context only; dropped from graph dependencies. |
| `docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`, claim and gauge-case boundary | Fixed/static gauge-background transfer positivity | Gauge-integrated coupled transfer and state uniqueness | No | Context only; dropped from graph dependencies. |
| Coupled reflected-Gram theorem, §7 exact two-form countermodels | Abstract positivity does not imply null descent or contraction | Logical sufficiency of two-plane positivity alone | Yes | Exact logical witness; the present support identity closes descent but not universal finite-circle contraction. |

The determinant, resolvent, compactness, diagonal extraction, and log-convex
arguments are proved in this note rather than carried by a mismatched source.

### N5 — rhetoric and resolution audit

| Statement / resolution | Tested? | Result and permitted wording |
|---|---|---|
| One observable in the `L_t=6` finite-group analogue | Yes | `n_2` gives the exact ratio `29/25`; this is an observable-level counterexample. |
| Six-observable first-boundary core | Yes | It contracts; no boundary-core no-go is permitted. |
| Eleven-observable multi-slice core | Yes | It is positive and noncontractive; finite-core logical non-implication is permitted. |
| Full gauge-invariant positive-half algebra | No | No claim that every core fails contraction. |
| Dynamical `SU(3)` finite circle | No | The `Z_3` result is not called an `SU(3)` noncontraction theorem. |
| Larger temporal circumferences | No in the primary certificate | No circumference-uniform finite-circle no-go is claimed. |
| Infinite-time OS quotient along a diagonal subsequence | Yes analytically | A positive self-adjoint contraction is proved only here. |
| Full-sequence infinite-time limit | No | The note says subsequential and does not prove uniqueness. |
| Spatial thermodynamic or continuum limit | No | No Lorentz, scattering, Standard Model, or GR conclusion is attached. |

“Unitary” refers only to the spectral group on `(ker T_2)^perp`. The
finite-circle result is called null descent and finite domination, never a
global finite thermal transfer matrix.

### N6 — partial-closure, convention, reframe, and primitive scan

| Candidate path | Status | What it closes |
|---|---|---|
| `docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md` | Existing free bounded theorem | Free two-step normalization only; not interacting uniqueness. |
| `docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md` | Existing fixed-background bounded source | Per-background fermion transfer only; not dynamical gauge integration. |
| Coupled periodic two-seam reflected-Gram theorem | Existing unaudited bounded candidate | Full finite-circle reflected forms and adjacent positivity; descent is partially closed here. |
| Reframe an accumulation functional as “the vacuum” | Rejected convention-only relabeling | Would hide rather than close boundary independence. |
| Exact interacting kernel or quantitative mixing estimate | Live derivation route | Could prove full-sequence uniqueness without a new primitive. |

The approved primitive registry supplies no probability law or dynamics and
is not enlarged here. Partial closure is material: an actual infinite-time OS
contraction and Hamiltonian exist along at least one subsequence. **No
axiom-update stop** is triggered.

### N7 — hostile steelman

Against the finite-circle negative boundary: the `Z_3` analogue is not the
`SU(3)` theory, the natural first-boundary core actually contracts, and no
larger circumference is tested by the primary certificate. An exact
gauge-integrated `SU(3)` kernel could therefore prove contraction on the
physical boundary algebra. This objection succeeds against any `SU(3)` or
all-core no-go, so those claims are absent. It does not erase the exact logical
counterexample: the named abstract positivity premises alone admit the
`29/25` finite-group realization.

Against the uniqueness boundary: fixed finite spatial volume makes time a
one-dimensional finite-range statistical system, so a compact
positivity-improving kernel or direct mixing estimate may make the normalized
limit unique. This is the strongest next route and is why the present result
is “not proved,” not a uniqueness no-go.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Retirement mechanism and applicability here |
|---|---|---|
| Free periodic staggered-circle repair | Finite thermal images obstruct an exact vacuum Gram | Correct antiperiodic spin/reflection data and increasing circumference suppress the images; motivates changing geometry before naming a vacuum operator. |
| Coupled periodic two-seam reflected-Gram theorem | Adjacent positivity without quotient descent | The support identity plus OS Cauchy--Schwarz closes interior descent here; repeated translation still requires infinite time. |
| Free two-step transfer theorem | Single-step positivity fails but a blocked positive channel exists | Exact action-derived decaying-channel selection retires the free wall; an interacting analogue remains a live route. |
| Fixed-gauge-background extension | Per-configuration positivity does not integrate the dynamical gauge field | Full coupled reflected-Gram integration replaces that static route, but does not yet supply a unique transfer kernel. |

The recurring successful mechanism is to narrow the domain, correct the
temporal structure, and then derive the operator rather than name it. This
cycle applies that mechanism by taking a subsequential infinite-time limit.
The next cycle must test kernel-based or mixing-based uniqueness there instead
of repeating the refuted premise that local seam positivity alone supplies
finite-circle contraction.
