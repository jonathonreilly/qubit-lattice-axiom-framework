# Exact factor-two gauge blocking and Schur/OS semigroup for the massive Wilson--staggered model

**Date:** 2026-07-12  
**Type:** bounded_theorem  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/massive_wilson_staggered_factor_two_gauge_block_schur_os_semigroup_2026_07_12.py`](../scripts/massive_wilson_staggered_factor_two_gauge_block_schur_os_semigroup_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/massive_wilson_staggered_factor_two_gauge_block_schur_os_semigroup_2026_07_12.txt`](../logs/runner-cache/massive_wilson_staggered_factor_two_gauge_block_schur_os_semigroup_2026_07_12.txt)

## 0. Result

This note constructs one exact coarse-graining step for the supplied
four-dimensional `SU(3)` Wilson--staggered model. It is a controlled
configuration, measure, and OS-semigroup map. It is not yet a closed
action-space renormalization-group flow.

On an even reflection-compatible regulator, keep the supplied periodic gauge
links and antiperiodic temporal fermion seam, let the coarse sites be
`K=(2Z)^4`, and define the declared straight-link block map

```text
B(U)_(X,mu)=U_(2X,mu) U_(2X+e_mu,mu).                                (0.1)
```

Retain the staggered variables `psi_X=chi_(2X)` and integrate the complement
`I=Lambda\K`. With the fine Dirac matrix split as

```text
D=[D_KK D_KI; D_IK D_II],
S[U]=D_KK-D_KI D_II^(-1)D_IK,                                       (0.2)
```

the following statements are exact for every `beta>=0,m>0`:

1. `B` is continuous, surjective, factor-two semigroup-compatible, and gauge
   covariant. Its skeleton Haar variables disintegrate with no Jacobian.
2. `D_II` is invertible, `det D_II>0`, and Grassmann integration gives

   ```text
   integral_I exp(-bar chi D chi)
    =det(D_II) exp(-bar psi S[U] psi).                                (0.3)
   ```

3. `S[U]` is gauge covariant, `det D=det D_II det S`, and
   `(D^(-1))_KK=S^(-1)`.
4. At fixed fine gauge background, `D_II^(-1)` and `S[U]` are exponentially
   quasilocal for every `m>0`, with decay ratio

   ```text
   r(m)=16/(m^2+16)<1.                                                (0.4)
   ```

5. Fully integrating the fermions and hidden gauge variables gives a strictly
   positive continuous coarse gauge density `w_c(V)` with exact partition and
   observable pullback identities.

Inside the strict
[massive Wilson--staggered Dobrushin spatial-uniqueness wedge](MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the infinite-volume gauge marginal is unique. Its iterated image measures

```text
nu_n=(B^n)_* mu_(beta,m)                                              (0.5)
```

form an exact coarse-measure semigroup. Gauge invariance, blocked translations,
proper spatial cubic symmetry, time reflection positivity, and exponential
mixing pass by pullback. On the blocked gauge-invariant OS Hilbert space, one
coarse time step is the fine two-step transfer:

```text
T'_1 = T_2 restricted to H_block^gauge,
a'_tau=2a_tau,
H'=-(a'_tau)^(-1)log T'_1
  =H restricted to [H_block^gauge intersect (ker T_2)^perp]           (0.6)
```

where the logarithm is taken on `(ker T'_1)^perp`.

Thus the already-constructed positive self-adjoint evolution and its physical
energy normalization survive this exact blocking step.

The boundary is equally important. Retaining one even site per `2^4` cell is
not a taste-faithful staggered block: every retained site has even staggered
parity, and the Schur action migrates away from the nearest-neighbor staggered
form. The gauge-fiber integral is a mixture of background-dependent Grassmann
Gaussians and can generate arbitrary gauge loops and higher fermion monomials.
No quasilocal coarse potential, finite Wilson--staggered coupling flow, beta
function, contraction, fixed point, critical exponent, Lorentz limit, QFT
limit, Standard Model limit, or GR limit is claimed.

No axiom-update stop is established. The missing object is a normed
gauge-invariant effective-action/polymer space containing the generated terms,
together with rescaling, counterterm extraction, and a uniform one-step
stability estimate.

## 1. Declared gauge block and exact Haar disintegration

Let `Lambda=(Z/LZ)^4`, with even reflection-compatible `L`, periodic gauge
links, and the supplied antiperiodic temporal fermion seam, and let
`Lambda'=(Z/(L/2)Z)^4`. The retained coarse fermion consequently remains
antiperiodic in coarse time. For every positive-oriented coarse link use the
two fine links in (0.1). These skeleton paths are link-disjoint.

For one path write `A=U_(2X,mu)`, `C=U_(2X+e_mu,mu)`, and `V=AC`. Bi-invariance
of normalized Haar measure gives

```text
dA dC=dA dV,                 C=A^(-1)V.                              (1.1)
```

Taking the product over the disjoint skeleton proves exact disintegration of
fine Haar measure into coarse links `V`, hidden skeleton links `A`, and all
nonskeleton links. It also proves surjectivity: for any `V`, choose `A=1`,
`C=V`, and assign the unused links arbitrarily.

Under a fine gauge transformation `g_x`, the intermediate factor cancels:

```text
B(U^g)_(X,mu)
 =g_(2X) B(U)_(X,mu) g_(2X+2e_mu)^(-1).                              (1.2)
```

With `h_X=g_(2X)`, this is exactly the coarse-link transformation law.
Straight paths also commute with even translations, proper spatial cubic
rotations, and the compatible `theta_0:t->-t` reflection preserving the even
time sublattice.

Iteration is literal path concatenation. `B^n(U)_(X,mu)` is the ordered
product along the straight fine path of length `2^n`; hence
`B^(n+k)=B^n after B^k` after the canonical lattice rescaling. On a finite
torus the required extents must be divisible by `2^(n+k)`; on `Z^4` there is
no divisibility endpoint.

The blocking convention is declared regulator data. Neither the axioms nor
this theorem select straight paths over other gauge-covariant block kernels.

## 2. Exact fermion Schur elimination

Write the staggered matrix as

```text
D=mI+M,                    M^dagger=-M,
epsilon M epsilon=-M,      ||M||<=4.                                 (2.1)
```

Because the site projection onto `I` commutes with diagonal `epsilon`, the
principal compression `M_II` remains anti-Hermitian and anticommutes with
`epsilon_I`. Its eigenvalues are paired `+i lambda,-i lambda`, with possible
zeros. Therefore, for every `m>0`,

```text
D_II=mI+M_II is invertible,
||D_II^(-1)||<=1/m,
det D_II=m^z product_(lambda>0)(m^2+lambda^2)>0.                      (2.2)
```

Finite-dimensional Berezin integration proves (0.3). Ordinary block Gaussian
elimination gives

```text
det D=det D_II det S,
(D^(-1))_KK=S^(-1).                                                   (2.3)
```

If `G_K,G_I` are the site-diagonal gauge matrices, then

```text
D_II(U^g)=G_I D_II(U)G_I^(-1),
S(U^g)=G_K S(U)G_K^(-1).                                             (2.4)
```

Thus the determinant factor is gauge invariant and the retained fermion
kernel is gauge covariant.

This exact decimation is not a projection onto one physical taste. All sites
in `K` have `epsilon=+1`, so the original even/odd staggered nearest-neighbor
form cannot be preserved on `K`. Equation (0.2) is the actual migrated form.

## 3. All-mass fixed-background locality

Set

```text
c=m^2+16,
Q_I=(16I+M_II^2)/c.                                                   (3.1)
```

Since `M_II` is anti-Hermitian and `||M_II||<=4`,

```text
0<=Q_I<=rI,                  r=16/c<1.                               (3.2)
```

The exact inverse series is

```text
D_II^(-1)=c^(-1) sum_(n>=0) Q_I^n (m-M_II).                          (3.3)
```

`Q_I` has range at most two and `m-M_II` has range at most one. If `d_I(x,y)`
is the fine graph distance through the eliminated induced subgraph `I`, then

```text
||(D_II^(-1))_(x,y)||
 <=(m+4)/m^2 r^ceil((d_I(x,y)-1)_+/2).                               (3.4)
```

Sandwiching with the one-hop blocks in (0.2) gives the safe coarse-site bound

```text
||S_(X,Y)-m delta_(X,Y)||
 <=16(m+4)/m^2 r^ceil((d(2X,2Y)-3)_+/2).                             (3.5)
```

The constant is deliberately coarse: each retained site has eight fine
neighbors and every hop block has norm `1/2`.

The positive factor `det D_II` has the parallel local series

```text
log det D_II
 =(|I| dim_color/2)log c -(1/2)sum_(n>=1)Tr(Q_I^n)/n.                 (3.6)
```

The operator trace remainder after order `N` is bounded by
`dim(D_II) r^(N+1)/[2(N+1)(1-r)]`. Together with (3.4), this gives a
convergent finite-regulator determinant representation and an exponentially
local fixed-background Schur kernel. It does not, by operator norm alone,
construct a site-anchored absolutely summable interaction for `log det D_II`.
Equations (3.4)--(3.6) are fixed-background statements. They do not prove
locality of the later gauge-integrated coarse action.

## 4. Exact finite coarse weights

Let `dH` denote all hidden gauge Haar variables after (1.1). The retained
Grassmann weight is

```text
W_c(V,bar psi,psi)
 =integral dH exp[-S_W(U)] det D_II(U)
             exp[-bar psi S(U)psi].                                 (4.1)
```

It is a finite Grassmann polynomial, gauge invariant under simultaneous
coarse transformations of `V,bar psi,psi`, and exactly reproduces every
observable in the retained coarse algebra.

Fully integrating the retained fermions gives

```text
w_c(V)=integral dH exp[-S_W(U)] det D(U)>0,                           (4.2)
Z_L=integral product_(X,mu)dV_(X,mu) w_c(V).                         (4.3)
```

For `m>0`, `det D(U)>0`. The hidden domain is compact and the integrand is
continuous and strictly positive. Hence `w_c` is continuous and strictly
positive, and

```text
S_c(V)=-log w_c(V)                                                    (4.4)
```

is a real continuous finite-volume coarse gauge action. No Faddeev--Popov
factor or gauge fixing was introduced.

For every bounded coarse gauge observable `F`, normalized expectations obey

```text
omega_(c,L)(F)=omega_L(F after B).                                   (4.5)
```

Equation (4.5), not a fitted coupling, is the exact one-step matching law.

## 5. Infinite-volume image semigroup, mixing, and OS time

Inside the direct dependency's strict wedge, let `mu` be the unique
infinite-volume gauge marginal. Because `B^n` is continuous and local,
`nu_n=(B^n)_*mu` is a normalized probability measure on the spacing-`2^n a`
coarse links and

```text
nu_n(F)=mu(F after B^n).                                              (5.1)
```

Gauge invariance and every symmetry intertwined by `B` pass immediately.
The image family is semigroup-compatible by path concatenation.

If the fine state has connected gauge-correlation bound
`C exp(-lambda dist_fine)`, then

```text
|Cov_(nu_n)(F,G)|
 <=C_(F,G,n) exp[-lambda dist_fine(supp(F after B^n),
                                   supp(G after B^n))].              (5.2)
```

For translated fixed-shape local supports whose coarse anchor sites are at
distance `d`, there is an explicit support-radius constant `c_(F,G)` such that

```text
dist_fine>=2^n[d-c_(F,G)].                                            (5.3)
```

Thus exponential mixing survives quantitatively. This is correlation control
for the image measure, not a proof that `S_c` has a uniformly quasilocal
infinite-volume potential.

Let `iota(F)=F after B` on the coarse gauge-observable positive-time algebra.
Straight factor-two blocking obeys

```text
iota theta'=theta iota,
iota tau'_1=tau_2 iota.                                              (5.4)
```

Writing `B'_0` and `B_0` for the coarse and fine reflection forms, respectively,

```text
B'_0(F,G)=nu_1(theta'F G)=B_0(iota F,iota G).                         (5.5)
```

Thus `iota` descends through the OS null quotients. Its continuous extension
is an isometry with closed range `H_block^gauge` in the fine gauge-invariant
OS Hilbert space. That subspace is invariant, hence reducing, for the positive
self-adjoint `T_2`. Functional calculus proves (0.6) on
`(ker T'_1)^perp=H_block^gauge intersect (ker T_2)^perp`. In particular,
coarse blocking does not import a new time law or probability rule: it
restricts the already constructed OS semigroup to the blocked gauge-observable
sector. Retained fermion composites in (4.1) are not included in this OS
restriction theorem.

## 6. Why this is not yet a constructive RG trajectory

Two fine backgrounds in the same `B` fiber can have different Schur kernels
`S[U]`; the runner supplies an explicit reduced-carrier witness. Therefore the
fixed-background Schur kernel does not descend to a function of straight
coarse links alone.

More generally, a gauge-fiber average of
`exp[-bar psi S(U)psi]` is a mixture of Grassmann Gaussians. Such mixtures
generically contain quartic and higher cumulants. The exact Haar second moment
already exposes the allowed quartic mechanism:

```text
integral_SU(3) dU
 (bar psi_x U psi_y)(bar psi_y U^dagger psi_x)
 =(1/3)bar psi_x^a psi_y^b bar psi_y^b psi_x^a.                       (6.1)
```

The Wilson part similarly produces general coarse Wilson loops and multiloop
interactions after hidden links are integrated. The theorem therefore refuses
to replace (4.1) by a nearest-neighbor staggered bilinear plus one Wilson
plaquette coupling.

This is an exact block-functional and coarse-measure step, not an action-space
contraction. An iterable constructive theorem still requires:

- a gauge-invariant normed space containing generated loops, polymers,
  multi-fermion monomials, and sources;
- a proof that constrained fiber integration maps that space into itself;
- relevant-coordinate extraction, field/coupling rescaling, and counterterms;
- uniform small-field/large-field and polymer stability estimates;
- a tuned trajectory with nonzero tight renormalized observables.

Balaban pure-gauge, scalar rigorous-RG, three-dimensional QED, and free-chain
Schur constructions are method context only. None is imported as a theorem for
this coupled four-dimensional model.

## 7. Runner contract

Run:

```bash
python3 scripts/massive_wilson_staggered_factor_two_gauge_block_schur_os_semigroup_2026_07_12.py
```

The runner uses a disclosed reduced `SU(3)` staggered carrier to check
anti-Hermiticity/parity, determinant and inverse Schur identities, positivity,
gauge covariance of `V` and `S`, factor-two semigroup composition, the `Q_I`
inverse series, same-fiber Schur variation, a Gaussian-mixture quartic
diagnostic, the exact `SU(3)` first-moment twirl, OS energy rescaling, and the
source/N1--N8 boundary. Four-dimensional locality and the infinite-volume
comparison/OS implications are analytic statements, not numerical extrapolations.

## 8. No-Go Discipline N1--N8

This is a positive bounded theorem with a named nonclosure boundary. The gate
tests that boundary without declaring constructive RG impossible.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it remains live outside the claim |
|---|---|---|---|
| Straight-link gauge pushforward | `ATTEMPTED` | Sections 1, 4, and 5 construct it exactly. | It is the positive route closed here. |
| Fixed-background fermion Schur decimation | `ATTEMPTED` | Sections 2--3 prove exactness and exponential locality. | It migrates form rather than selecting physical tastes. |
| Gauge-covariant spin--taste hypercube blocking | `ATTEMPTED` | One-site decimation does not provide it. | A larger coarse multiplet and path symmetrization can retain tastes. |
| Quasilocal coarse-potential reconstruction | `ATTEMPTED` | Image mixing alone does not construct a potential norm. | High-temperature image-Gibbs theorems or a direct polymer proof remain live. |
| Dobrushin--Shlosman block criterion | `ATTEMPTED` | The present map is not an optimized block influence calculation. | A block criterion can enlarge and stabilize the controlled region. |
| Polymer/cluster effective action | `ATTEMPTED` | Generated loops and fermion monomials are not normed here. | An enlarged polymer space is the immediate constructive target. |
| Balaban/Dimock multiscale route | `ATTEMPTED` | Existing primary results do not cover this coupled 4d model. | Their small/large-field architecture can be adapted rather than imported. |
| Alternative block kernels or tensor networks | `ATTEMPTED` | Straight paths are declared, not selected. | Other local gauge-covariant maps can improve taste/symmetry behavior. |

### N2 — wall-independence audit

After collapsing downstream requirements, the three open conditions are:
`taste-faithful coarse fermion variables`, `controlled action-space RG
theorem`, and `physical critical trajectory/observable identification`.

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| taste-faithful coarse fermion variables | controlled action-space RG theorem | No | No | Yes |
| taste-faithful coarse fermion variables | physical critical trajectory/observable identification | No | No | Yes |
| controlled action-space RG theorem | physical critical trajectory/observable identification | No | No | Yes |

Rescaling, counterterms, polymer norms, and uniform stability are components of
the single controlled action-space RG condition, not inflated independent walls.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Fixed gauge background is an explicit theorem variable, not a hidden condition. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | Canonical lattice rescaling in Section 1 is a coordinate identification, not a physical selector. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Massive Wilson--staggered Dobrushin spatial-uniqueness wedge](MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Unique mixing gauge marginal and positive fixed-lattice OS gap in its strict wedge | Infinite-volume image measure, inherited mixing, and blocked OS restriction | Yes | Sole direct dependency. |
| Free-chain Schur decimation | Fixed-energy free one-dimensional downfolding | Coupled four-dimensional gauge-fiber blocking | No | Context only. |
| Abstract Banach contraction theorem | Contraction consequences after a map/norm are supplied | Construction of the missing coupled map/norm | No | Context only. |
| Balaban/Dimock literature | Pure gauge, scalar, or 3d QED constructive architectures | Coupled 4d `SU(3)` staggered theorem | No | External context only. |

The finite-volume block, Schur, locality, and positivity statements are proved
self-containedly. The direct dependency is consumed only for the infinite
unique-state mixing and OS conclusions.

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| One two-link gauge block | Yes | Exact Haar disintegration and covariance. |
| One finite periodic regulator | Yes | Exact Schur and positive coarse gauge density. |
| Fixed fine gauge background | Yes | Exponentially local Schur kernel. |
| Gauge-integrated coarse action | Partly | Exists and is continuous at finite volume; no locality claim. |
| Infinite unique gauge marginal in the strict Dobrushin wedge | Yes | Exact image semigroup and inherited mixing. |
| Gauge-observable blocked OS sector | Yes | Positive transfer restriction and unchanged physical energy normalization on the nonzero-transfer subspace. |
| Taste-faithful full fermion theory | No | One-site decimation is explicitly not taste faithful. |
| Action-space contraction or continuum fixed point | No | No RG-flow or continuum-existence claim. |

### N6 — partial-closure and primitive scan

The block kernel is declared regulator data and the theorem then derives its
consequences. A future symmetry/taste argument could narrow the kernel without
changing an axiom. The approved Lattice, Qubit, Admissibility, Record,
scale-reference, kinetic-isotropy, and realized-state premises are not enlarged.
No new probability law, time law, action, or primitive is inserted.

The positive partial-closure path is explicit: enlarge the effective-action
space, prove a one-step norm estimate, and tune a trajectory. This is ordinary
mathematical construction, not an axiom-update requirement.

### N7 — hostile steelman

A hostile reviewer should call (0.5) “only image-measure bookkeeping,” not a
constructive RG theorem. That objection correctly blocks any claim of a running
coupling, action-space contraction, or continuum fixed point. It does not undo
the exact content established here: a gauge-covariant surjective local block,
positive coarse measure, exact observable intertwining, inherited exponential
mixing, fixed-background Schur locality, and a gauge-observable OS semigroup
restriction with the correct doubled time spacing. The note adopts the
narrower classification.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Lesson here |
|---|---|---|
| Free-chain Schur decimation | Exact downfolding migrated out of the original action form | Form migration is recorded rather than renamed as closure. |
| Block-qubit CP compression | A coarse channel need not be an algebra morphism | The present map acts on field configurations/measures and claims no qubit-site morphism. |
| Compact-interior continuum boundary | Uniform mixing survives but gives only a massive/ultralocal scaling class | Blocking a massive state is not a critical trajectory. |
| Certificate-boundary non-identification | Loss of one proof envelope is not criticality | A real block map still needs action-space and trajectory control. |

No similar wall was retired by relabeling. Exact Schur algebra closes one rung;
the remaining RG theorem needs new estimates.

**No-Go Discipline status: PASS.** All eight checks are answered, eight routes
are tested, and the negative boundary is restricted to what this exact step
does not establish. No RG formalism, continuum route, or axiom family is
declared closed.
