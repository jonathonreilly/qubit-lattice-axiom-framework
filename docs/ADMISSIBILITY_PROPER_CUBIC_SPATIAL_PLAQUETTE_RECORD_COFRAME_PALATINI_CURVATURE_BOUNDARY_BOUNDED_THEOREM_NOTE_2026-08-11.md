---
claim_id: admissibility_proper_cubic_spatial_plaquette_record_coframe_palatini_curvature_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "On one supplied finite Euclidean cube law, all twenty-four based loops in the proper-cubic orbit of an elementary spatial plaquette, twelve SO(4) links, eight GL+(4) coframes, ten projective Record rays, transported positive edge factors, coframe and derived-normal compatibility, torsion control, and a triad-derived intrinsic spatial Einstein--Cartan bivector linear in sine holonomy form one local-frame and proper-cubic covariant normalized joint weight. A two-parameter equivariant link field numerically solves all seventy-two intrinsic link equations; supplied coercive Gram wells numerically complete coframe stationarity. Record stress and contact, transport, coframe compatibility, torsion, and curvature are separately load-bearing. The sine chart is explicitly not a global holonomy coordinate. This is a finite spatial Einstein--Cartan precursor, not a gravity derivation, selected physical law, lattice Bianchi or Einstein theorem, full-Z3 phase, Lorentzian result, axiom-necessity result, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_local_geometry_record_bond_transfer_reflection_response_connection_boundary_bounded_theorem_note_2026-08-11
  - admissibility_ten_ray_coframe_link_local_frame_ward_stationarity_connection_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_proper_cubic_spatial_plaquette_record_coframe_palatini_curvature_boundary_2026_08_11.py
---

# Proper-Cubic Spatial Plaquette Record/Coframe Palatini Curvature Boundary

**Date:** 2026-08-11
**Type:** `bounded_theorem`
**Role:** execute the Block-36 closed-plaquette target on the smallest complete
proper-cubic spatial cell and isolate the law-selection and increasing-region
gravity boundary.
**Scope:** one Euclidean cube, eight coframes, twelve constrained links, ten
Record-ray labels per vertex, all six faces and all twenty-four based oriented
plaquette loops, one supplied positive joint law, and one supplied numerical
stationary witness.
**Audit-status authority:** independent audit lane only. This source note
authors no audit verdict and predicts none.

**Primary runner:**
[admissibility_proper_cubic_spatial_plaquette_record_coframe_palatini_curvature_boundary_2026_08_11.py](../scripts/admissibility_proper_cubic_spatial_plaquette_record_coframe_palatini_curvature_boundary_2026_08_11.py)

## Result Up Front

Block 36 asks for one closed coframe-compatible spatial plaquette and its full
proper-cubic orbit, nontrivial holonomy, torsion/compatibility control, a term
linear rather than quadratic in curvature, and Record contact that is
load-bearing in the same normalized law. This block supplies one finite law
that meets all of those bounded obligations simultaneously.

The construction is not a one-face or symmetry-reduced stationarity check.
It contains:

1. the eight vertices, twelve edges, and six faces of one cube;
2. all twenty-four distinct based oriented plaquette loops generated from one
   face by the orientation-preserving cubic group;
3. one shared ten-valued Record label at each vertex across its three incident
   faces, rather than an independent face label;
4. positive transported-projector factors on all twelve edges;
5. coframe and derived-normal compatibility, plaquette torsion, and a
   triad-derived intrinsic spatial Einstein--Cartan contraction with
   antisymmetric loop holonomy;
6. a finite, strictly positive, normalizable joint weight on
   `GL+(4)^8 x SO(4)^12 x {1,...,10}^8`;
7. a nonflat, normal-compatible proper-cubic link background that is
   numerically stationary in all seventy-two independent intrinsic link
   tangents, not only in its two-parameter ansatz;
8. a numerically coframe-stationary completion by explicit positive-definite
   quartic Gram wells; and
9. an exact `10^8`-branch Record contraction whose intrinsic scale response is
   microscopic contact minus connected covariance.

The central numerical certificate is

```text
link parameters (spatial, normal-mix)   0.323988455, 1.094e-12
maximum / norm of 72-link gradient      1.776e-09 / 2.512e-09
face holonomy gap                       1.802069 on every based face
intrinsic EC curvature signal           0.963037 on every based face
plaquette torsion norm                   0.369390 on every based face
maximum transported-normal error         1.547e-12
minimum target-Gram eigenvalue           1.025111
maximum coframe gradient                 7.994e-09
exact contracted Record partition        823039502.694778
Record contact / covariance              2.746612820 / 0.010195374
complete / numerical scale response      2.736417446 / 2.736417493
```

The bounded coexistence obstruction is therefore retired at one complete
elementary spatial cube: Record loading, compatible transport, torsion control,
and an intrinsic spatial Einstein--Cartan curvature term can coexist in one
normalized, covariant, numerically stationary finite model. An adversarial
index test also corrects a material earlier draft error: on a three-dimensional
base, `star[(e s_1) wedge (e s_2)]` detects normal-mixing rather than intrinsic
face rotation. The correct spatial contraction uses the internal normal
derived from the three coframe columns and the complementary triad direction.
What remains is physical selection and extension:
the axioms do not select the coframe/link carrier, continuous measure,
coefficients, reverse-engineered Gram wells, increasing-region law, Einstein
regime, or Lorentzian permanent-Record update. No fixed TOE percentage moves
from this supplied finite witness alone.

## Inputs And Non-Imports

| input | used here | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | the `Z^3` base, proper-cubic covariance, one-site possibility domain, nearest-neighbour Admissibility distribution, and permanent Records | coframes, links, `SO(4)`, Haar/Lebesgue measure, plaquette action, coefficients, phase, Einstein equation, or dynamics |
| [Block 35 local geometry law](ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the ordered ten rays, their two proper-cubic orbit weights, and the demand for a local normalized joint law | its four-state transfer law, decoder curvature, fugacity, or finite-cylinder phase |
| [Block 36 local-frame law](ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | continuous coframes and endpoint-transforming `SO(4)` links, the ray-projector transport pattern, and the exact next-target contract | its two-site wells, nonuniform background, multiplier extension, KKT Hessian, or an inherited curvature law |

No observed constant, Newton coefficient, cosmological coefficient, continuum
Einstein equation, literature value, target-fitted gravity datum, canonical
axiom edit, audit verdict, or `review-loop` is used.

## 1. Cube, Proper-Cubic Orbit, And Projective Record Rays

Use the cube vertices

```text
V={(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
   (-1,-1, 1),(1,-1, 1),(1,1, 1),(-1,1, 1)}.       (1)
```

Join nearest vertices differing in one sign, giving twelve unoriented edges.
The seed outward-oriented `+x` face is

```text
(1,-1,-1) -> (1,1,-1) -> (1,1,1) -> (1,-1,1).     (2)
```

Acting on (2) with all determinant-`+1` signed permutation matrices produces
twenty-four distinct based loops: four cyclic base points on each of six
geometric faces. Thus every face and every base point enters; no spatial plane
or distinguished face is selected.

The ten directions inherited from Block 35 are

```text
(1, 1, 1,0), (1, 1,-1,0), (1,-1, 1,0), (1,-1,-1,0),
(1, 0, 0,1), (-1,0, 0,1),
(0, 1, 0,1), (0,-1, 0,1),
(0, 0, 1,1), (0, 0,-1,1).                           (3)
```

Only their rank-one projectors are transported:

```text
P_vr = (e_v d_r)(e_v d_r)^T / ||e_v d_r||^2.       (4)
```

Projective signs therefore agree. Exact enumeration shows that the
twenty-four proper-cubic rotations permute the ten projectors with zero
floating residual. The orbit weights

```text
a_r=(3,3,3,3,4,4,4,4,4,4)                          (5)
```

are invariant under the same action. This is a finite proper-cubic Record
carrier. It is not a continuous label representation; the continuous local
frame acts on `e_v d_r`, as in Block 36.

## 2. One Microscopic Record/Coframe/Link Weight

At each vertex take `e_v in GL+(4,R)`. On every stored edge `(v,w)` take
`U_vw in SO(4)` and set `U_wv=U_vw^T`. Define `g_v=e_v^T e_v`. The positive
transport kernel is

```text
K_vw(r,s)
 = exp[-(beta/2)||P_vr-U_vw P_ws U_vw^T||_F^2],
beta=1/5.                                             (6)
```

For a based plaquette `p=(v,v_1,v_2,v_3)`, let

```text
s_1=(v_1-v)/2,  s_2=(v_3-v)/2,
H_p=U_vv1 U_v1v2 U_v2v3 U_v3v,
F_p^sin=(H_p-H_p^T)/2.                               (7)
```

Embed the spatial steps as four-vectors with zero fourth component. Write the
three spatial coframe columns as `E_vi=e_v hat{i}` and derive the oriented unit
internal normal

```text
n_v^I=-epsilon^I_JKL E_vx^J E_vy^K E_vz^L
      /||epsilon(E_vx,E_vy,E_vz)||,
c_p=s_1 cross s_2,
B_p^EC(e_v)=star[n_v wedge e_v(c_p,0)],
phi_p=(1/2) B_p^EC:F_p^sin.                           (8)
```

Equation (8) is the intrinsic three-dimensional Einstein--Cartan index
pattern obtained by splitting a four-dimensional internal frame into its
spatial triad and triad-derived normal. For an `xy` face it couples to the
intrinsic `xy` rotation. The tempting replacement
`star[(e_v s_1) wedge (e_v s_2)]` instead couples that face to the complementary
normal-mixing generator; it is a coframe-dressed BF/four-dimensional-face-like
term, not the desired intrinsic spatial contraction. The runner executes both
index probes: the corrected bivector gives intrinsic/normal-mixing signals
`0.000070711 / 0`, while the rejected dual-face bivector gives
`0 / 0.000070711`. This correction is load-bearing. The result remains only a
spatial precursor because the base has three directions; an internal normal
does not manufacture a fourth base direction.

The ray incidence and the shared-label curvature load at vertex `v` are

```text
iota_rp=(d_r^spatial dot s_1)^2+(d_r^spatial dot s_2)^2,
ell_vr=sum_{p based at v} iota_rp phi_p.              (9)
```

Each vertex is the base of three incident faces. For one Record assignment
`r=(r_v)`, its positive microscopic weight is

```text
w(e,U,r)
 = exp[-C(e,U)-N(e,U)-T(e,U)-W(e)]
   product_v {a_rv exp[-||e_v d_rv||^2/2
                       +(sigma/3) ell_v,rv]}
   product_(v,w) K_vw(r_v,r_w),

eta=1/5, kappa_n=1/5, tau=3/10,
sigma=1/2, alpha=16,                                  (10)
```

where

```text
C=(eta/2) sum_(v,w) ||e_v-U_vw e_w||_F^2,            (11)

N=(kappa_n/2) sum_(v,w) ||n_v-U_vw n_w||^2,          (12)

T=(tau/8) sum_p ||
   [U_vv1 e_v1 s_2-e_v s_2]
  -[U_vv3 e_v3 s_1-e_v s_1] ||^2,                   (13)

W=(alpha/4) sum_v ||e_v^T e_v-Q_v||_F^2.             (14)
```

The `1/3` in (10) is a fixed elementary face-incidence coefficient. On this
one cube, where every vertex meets three faces, it is numerically an incidence
average rather than a tripled one-face coefficient. It must not be recomputed
from the degree of a larger finite region; the two-cube extension tests that
adaptive interpretation separately. The same label `r_v` appears in the site
weight, all incident edge kernels, and all three incident curvature loads.
Thus the Palatini scalar is inside each occupied Record branch; it is not a
post hoc additive spectator outside the Record sum.

Summing the labels gives

```text
Z_R(e,U;sigma)=sum_{r_0,...,r_7=1}^{10}
 product_v q_v(r_v;sigma) product_(v,w) K_vw(r_v,r_w),
F_R=-log Z_R.                                         (15)
```

The runner contracts the nominal `10^8` assignments exactly as a four-index
lower-face tensor, a four-index upper-face tensor, and four vertical edge
transfers. It never enumerates a dense `10^8` array.

For bookkeeping, the effective action is written as

```text
Gamma=C+N+T+W+F_R(e,U;sigma)
     =C+N+T+W+F_R(e,U;0)
      +[F_R(e,U;sigma)-F_R(e,U;0)].                  (16)
```

The last two terms expose the base Record and curvature-loaded contributions,
but their sum is the free energy of the single microscopic law (10).

## 3. Strictly Positive Finite Normalization

The complete finite-region normalizer is

```text
Ncal = integral_{GL+(4)^8} product_v d e_v
    integral_{SO(4)^12} product_e d_H U_e
    Z_R(e,U;sigma) exp[-C-N-T-W].                     (17)
```

Here `d e_v` is the restriction of sixteen-dimensional Lebesgue measure to
the positive-determinant component, and `d_H U_e` is normalized Haar measure.
No measure is inferred from the four axioms; both are declared parts of the
supplied finite law.

Normalization follows directly:

- the Record sum has only `10^8` positive branches;
- every projector kernel is positive and uniformly bounded, and `SO(4)^12`
  is compact with finite normalized Haar measure;
- for fixed links, all site scores grow quadratically and each normalized-
  normal EC load grows at most linearly in the coframe entries;
- `C`, `N`, and `T` are nonnegative; and
- the positive quartic leading term in (14) dominates every quadratic Record
  exponent in every coframe direction.

Consequently the integrand is bounded above by a finite sum of integrable
quartic-tail functions. It is positive on a nonempty open subset, so
`0<Ncal<infinity`. This proves one finite normalizable joint law. It does not
prove a thermodynamic limit or select Lebesgue/Haar measure physically.

## 4. Local-Frame And Proper-Cubic Covariance

For independent `L_v in SO(4)`, set

```text
e_v -> L_v e_v,
U_vw -> L_v U_vw L_w^T.                              (18)
```

Then `g_v`, the site scores, and `W` are invariant; `n_v -> L_v n_v`;
projectors and transported projectors transform together; every compatibility
norm is invariant; `H_p`, `F_p^sin`, `B_p^EC`, and the torsion vector transform
at the base vertex.
Thus every microscopic branch of (10), not merely its label sum, is invariant.
One independent finite rotation at every vertex gives action error `0.000e+00`
at printed precision.

For a proper-cubic rotation `R`, lift it as `Rhat=diag(R,1)`, permute sites and
edges, and transform

```text
e_Rv'=Rhat e_v Rhat^T,
U_Rv,Rw'=Rhat U_vw Rhat^T,
Q_Rv'=Rhat Q_v Rhat^T,                                (19)
```

with transposition when the stored edge orientation reverses. Equation (3)
closes projectively and the full twenty-four-loop sum is invariant. The runner
checks all twenty-four transforms with maximum action error `0.000e+00` at
printed precision. Retaining only faces with one fixed normal changes an
anisotropic probe action by `0.004620`, while the complete orbit remains
invariant. The full orbit is therefore load-bearing rather than decorative.

## 5. A Nonflat Stationary Proper-Cubic Link Field

Set every witness coframe to

```text
e_v*=diag(1,1,1,5/4).                                 (20)
```

For a positive-coordinate edge with unit direction `u` and midpoint `m`, let
`t=(0,0,0,1)` and declare the two proper-cubic algebra tensors

```text
X_vw(a,b)=-a [u wedge m]-b [(u cross m) wedge t],
U_vw(a,b)=exp X_vw(a,b).                              (21)
```

The first generator is purely spatial; the second mixes the triad with the
internal normal. Both coefficients and all action coefficients in (10) are
declared before the numerical stationary solve. Solving the two reduced
finite-difference equations gives

```text
a=0.323988455,  b=1.094e-12,
maximum reduced residual=0.000e+00 at printed precision. (22)
```

Thus the selected branch is spatial and preserves the derived normals; the
normal-mixing coefficient is zero to numerical resolution and the maximum
transported-normal mismatch is `1.547e-12`. The reduced solve is not used as
the stationarity certificate. Each of the
twelve `SO(4)` links has six independent left-invariant tangents. Centered
finite differences of the complete action (16), without the coframe wells
which do not depend on links, give

```text
maximum over all 72 tangents =1.776e-09,
Euclidean norm               =2.512e-09.              (23)
```

These are numerical finite-difference residuals, not an interval or symbolic
existence certificate. All links have determinant one and orthogonality error
below `1.310e-16`; their proper-cubic equivariance residual is below
`1.758e-16`. Every based face has

```text
||H_p-I||_F=1.802069,
phi_p=0.963037,
||torsion_p||=0.369390.                               (24)
```

The witness is deliberately not torsionless. The torsion penalty is a
load-bearing control term, not an assertion that the independent connection
has already been eliminated to Levi-Civita form.

## 6. Coframe Stationarity And The Supplied-Well Boundary

Let `G_v` be the complete non-well coframe gradient of
`C+N+T+F_R(e,U;sigma)` at (20)--(22). Proper-cubic symmetry makes
`e_v^{-1}G_v` symmetric to numerical error. Define

```text
Q_v=e_v^T e_v + sym(e_v^{-1}G_v)/alpha.               (25)
```

The derivative of (14) is then `-G_v`, so the complete coframe equation is
numerically stationary. This is a transparent reverse-engineered numerical
completion, not a symbolic existence proof or physical selection argument.
The runner checks:

```text
maximum antisymmetric reduced stress   0.000e+00
minimum eigenvalue among all Q_v       1.025111
proper-cubic target equivariance       0.000e+00
maximum over all 128 coframe entries   7.994e-09.      (26)
```

Positive definiteness of `Q_v` is not needed for quartic coercivity but makes
the supplied wells ordinary positive target Grams. A later derivation must
remove or select (25); reverse engineering is the largest local-law wall left
by this finite witness.

## 7. Record Contact Minus Connected Covariance

Scale one coframe intrinsically by `e_0(t)=(1+t)e_0*`, holding links fixed.
Its normalized projectors, derived normal, and every adjacent edge kernel
remain unchanged. Its ray score scales as `(1+t)^2`, while the complementary-
triad EC load scales as `(1+t)`. For branch label `r`, the microscopic action
derivatives satisfy

```text
A_r'=||e_0 d_r||^2-(sigma/3) ell_0r,
A_r''=||e_0 d_r||^2.                                  (27)
```

Therefore the exact finite-sum identity is

```text
d^2 F_R/dt^2 = <A''>-Cov(A',A').                     (28)
```

The tensor contraction gives

```text
Z_R                    =823039502.694778,
<A''>                  =2.746612820,
Cov(A',A')             =0.010195374,
<A''>-Cov(A',A')       =2.736417446,
independent finite diff=2.736417493,
response without contact=-0.010195374.                (29)
```

Thus the Record contribution is not merely present in an invariant action:
its microscopic contact and connected covariance are separately nonzero in
the intrinsic scale response of this supplied finite free energy, and the
curvature load occurs in the same branch observable. Omitting contact even
reverses the sign. No continuum stress tensor or physical response law is
claimed.

## 8. Curvature Discriminator And Destructive Controls

For `H(epsilon)=exp(epsilon K)` with `K` parallel to the intrinsic EC
bivector,
compare only the two displayed local functions

```text
P(epsilon)=(1/2) B^EC:[H-H^T]/2,
W_0(epsilon)=4-tr H.                                  (30)
```

At `epsilon=10^-4`, doubling gives

```text
P(2 epsilon)/P(epsilon)=1.999999995,
W_0(2 epsilon)/W_0(epsilon)=4.000000000,              (31)
```

and reversal gives `P(-epsilon)/P(epsilon)=-1` while
`W_0(-epsilon)/W_0(epsilon)=+1`. Equation (31) establishes that the chosen
intrinsic EC term is odd and linear in infinitesimal curvature, unlike this
coframe-independent Wilson comparator, which is even and quadratic. It is not
a no-go for Wilson actions or a uniqueness theorem for gravity. It is also
chart-local: at a nonidentity pi holonomy, `||H-I||_F=2.828427125`, the sine
coordinate and EC signal vanish while `4-tr(H)=4`. The theorem therefore does
not treat sine holonomy as a global curvature coordinate.

The runner also executes the following controls without refitting the witness:

| mutation or control | result |
|---|---|
| old dual-face bivector on intrinsic vs normal-mixing generators | `0 / 0.000070711`, opposite to corrected EC `0.000070711 / 0` |
| pure-gauge coframes and links | maximum holonomy/curvature/torsion residual `4.022e-16 / 2.776e-17 / 2.487e-16` |
| identity links with incompatible rotated coframes | zero holonomy and curvature, but torsion `0.210836` |
| compensated vs uncompensated site-frame rotation | complete action error `0`; uncompensated change `0.006691` |
| delete one edge / one closing factor | eight based loops invalidated; open contraction changes `0.035899` under compensated frames |
| replace EC load by `4-tr(H)` inside the same Record branches | positive covariant `Z_R=25986289661.931770`; EC/Wilson coframe-load derivatives `12.482382 / 0`; unrefitted link residual `1.882414` |
| closest-frame polar link elimination on a noncommuting coframe probe | covariant with error `7.224e-15`; holonomy `0.020692..0.027071`, EC `-0.017757..-0.011304`, torsion `0.017766..0.044293`; this is not a selected Levi-Civita theorem |
| one-link normal-mixing mutation | transported-normal mismatch `0.099958`; normal-compatibility penalty `0.000999167` |
| delete all Record free energy | coframe-gradient norm `2.888604` |
| delete only curvature loading | coframe-gradient norm `0.724711`; maximum link residual `0.148042` |
| delete torsion penalty | maximum link residual `0.022884` |
| delete coframe compatibility | maximum link residual `0.125108` |
| delete ray-projector transport (`beta=0`) | maximum link residual `0.002135` |
| retain one face-normal family | proper-cubic action mismatch `0.004620` |

These mutations separate flatness from compatibility, expose the rejected
index contraction, show that the named Record/coframe, EC/coframe, torsion,
coframe-compatibility, and transport sectors affect a stationary equation,
and prevent the coframe wells from hiding deletion of Record or curvature.
The normal-compatibility penalty vanishes at this witness and is certified by
its normal-mixing mutation; it is not falsely called load-bearing there. No
ambient orthogonality multiplier is used: links are parameterized intrinsically
on `SO(4)`, so the Block-36 constraint-multiple mutation is inapplicable rather
than silently omitted.

## 9. Gravity And Axiom Boundary

This block materially advances the gravity lane: it retires the bounded
question of whether a complete elementary spatial cube can carry nontrivial
intrinsic spatial EC curvature, transported Records, derived-normal and
coframe compatibility, torsion control, normalization, and full numerical
intrinsic stationarity at once. It does not select that law. It also identifies
and repairs the precise index error that made the earlier dual-face draft probe
normal-mixing curvature rather than spatial face rotation.

The four framework axioms state a base lattice, local possibility domain, one
fixed covariant Admissibility distribution, and permanent Records. They do not
specify the extensional distribution used in (10), a map from `M_2(C)` Record
content to coframes and links, Lebesgue/Haar measure, the six coefficients,
the two link tensors, or the eight target Grams. The approved premise registry
also supplies no such gravity law. That scope observation is not a proof that
a fifth axiom is necessary: a downstream derivation, explicit bounded import
followed by retirement, carrier refinement, or realization theorem remains
possible.

The strongest sufficient downstream interface now has a concrete target:

> From the existing local possibility and permanent-Record content, define a
> translation-compatible coframe/link observable or equivalent discrete
> carrier and one normalized finite-range joint specification. Derive its
> site, edge, normal/coframe compatibility, torsion, and intrinsic EC
> curvature factors from the same Admissibility law, including the measure and
> coefficients. Show that
> overlapping cubes share one set of variables and conditionals, admit an
> increasing-region phase, and yield the required displacement/Bianchi,
> weak-curvature Einstein, and Lorentzian Record-update limits.

If that interface is derived within the existing possibility domain, no
ontology amendment follows. If every such route fails and a new local
possibility type is shown necessary, an axiom-governance fork would become
appropriate. This note proves neither premise. **No fifth ontology axiom** is
adopted or shown necessary.

## No-Go Discipline Gate

The narrow negative eligible to ship is:

> This one supplied Euclidean cube witness does not derive or physically
> select gravity from the four axioms, and it cannot by itself establish an
> increasing-region/full-`Z^3`, lattice-Bianchi/Einstein, or Lorentzian
> permanent-Record theorem. Its carrier, measure, coefficients, stationary
> link ansatz, and coframe wells are explicit finite-law inputs.

This is not a gravity no-go, an emergent-geometry no-go, or an axiom-necessity
claim. The constructive witness makes every broader negative premature.

### N1 — Normalized Alternative-Route Enumeration

The five counted route families differ in primary object, load-bearing
invariant, or terminal proof obligation under the proof-search governance
tuple. Every counted route was actually executed by the primary runner in
this cycle. `ATTEMPTED` does not mean a family is ruled out in general.

| normalized family | attempted mechanism and terminal obligation | why it does not defeat the narrow finite-input boundary | marker / evidence |
|---|---|---|---|
| independent-connection intrinsic spatial EC law | derive the internal normal from the triad, contract its complementary-triad bivector with sine holonomy inside each Record branch, and solve the complete cube equations | succeeds as the bounded construction, but its carrier, coefficients, measure, wells, and region extension remain supplied | `ATTEMPTED`; the 21-check runner, especially derived-normal, 72-tangent, normalization, and mutation certificates; matched Block-36 target at `docs/ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:690-716` |
| coframe-dressed dual-face BF-like contraction | use `star[(e s_1) wedge (e s_2)]` as the bivector and require it to detect intrinsic spatial face curvature | the executed index probe falsifies that terminal obligation: it is blind to intrinsic face rotation and detects normal-mixing instead | `ATTEMPTED`; Section 2 and the runner's `derived-normal-intrinsic-einstein-cartan-index-control` |
| closest-frame polar connection elimination | derive each link as the closest proper rotation between neighboring coframes, then ask whether geometry alone fixes a covariant curved connection | the construction is covariant and curved on the probe, so it remains live, but the polar prescription and coframe law are supplied and it neither enforces zero torsion nor selects a measure | `ATTEMPTED`; Section 8 and `polar-coframe-derived-link-elimination-attempt` |
| Record-induced effective action | integrate the shared Record labels so curvature loading and the scale response arise from `-log Z_R`, with contact/covariance as the selection mechanism | the mechanism succeeds and omitting contact changes the sign, but `sigma`, incidence, orbit weights, edge kernel, geometry carrier, and measure remain declared | `ATTEMPTED`; equations (10), (15), and (27)--(29), plus `normalized-record-contact-covariance-response` |
| same-law Wilson substitution | replace only the EC scalar by `4-tr(H)` inside the identical positive Record branches and test whether covariance/normalization alone selects the curvature form | positivity and frame covariance survive, while explicit coframe-curvature response vanishes and the unrefitted link residual is `1.882414`; covariance therefore does not select EC over Wilson | `ATTEMPTED`; Section 8 and `same-law-wilson-curvature-substitution` |

Regge dual-hinge, independent constrained BF/Plebanski, a refitted
teleparallel law, overlapping-cube/DLR extension, and Lorentzian causal-update
families remain live but unexecuted here; they are listed in N6 and are not
miscounted as `ATTEMPTED`. Therefore the only defensible negative is the narrow
statement that this finite supplied fixture does not itself perform law
selection or an increasing-region/Lorentzian proof.

### N2 — Wall-Independence Audit

After collapsing duplicate language, the remaining obligations are:

- `W1`: derive or explicitly retire the import of a Record-to-coframe/link (or
  equivalent discrete geometry) carrier;
- `W2`: derive or physically select the normalized joint measure, incidence
  law, coefficients, and stationary geometry potential rather than supply
  them;
- `W3`: glue overlapping cubes into one translation-compatible finite-range
  specification, execute its ordered-product lattice Bianchi identities, and
  select/control an increasing-region full-`Z^3` phase;
- `W4`: derive base-lattice displacement/diffeomorphism Ward content beyond
  kinematical connection identities;
- `W5`: derive the weak-curvature Einstein/two-derivative regime, universal
  source coupling, constraint algebra, signature, and physical modes; and
- `W6`: derive a Lorentzian causal update compatible with permanent Records.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| W1 / W2 | no | no | yes |
| W1 / W3 | no | no | yes |
| W1 / W4 | no | no | yes |
| W1 / W5 | no | no | yes |
| W1 / W6 | no | no | yes |
| W2 / W3 | no | no | yes |
| W2 / W4 | no | no | yes |
| W2 / W5 | no | no | yes |
| W2 / W6 | no | no | yes |
| W3 / W4 | no | no | yes |
| W3 / W5 | no | no | yes |
| W3 / W6 | no | no | yes |
| W4 / W5 | no | no | yes |
| W4 / W6 | no | no | yes |
| W5 / W6 | no | no | yes |

A carrier does not fix its probability law; a local probability law need not
have a controlled thermodynamic phase; an infinite-volume Gibbs
specification need not have a displacement redundancy; a kinematical lattice
Bianchi identity does not select Einstein dynamics; an Einstein-like
Euclidean quadratic regime does not supply a causal permanent-Record update;
and none of the downstream results derives the upstream carrier or law in the
reverse direction. No pair collapses.

### N3 — Hidden-Condition Scan

| phrase or construction | classification |
|---|---|
| “framework provides” | restricted to the four items quoted from the canonical axiom memo; all geometry and law data are listed as non-imports |
| “Record ray” | Block-35 supplied metric-probe dictionary, not an ontological claim that the rays exhaust `M_2(C)` |
| “Einstein--Cartan” / “Palatini-like” | derived-normal complementary-triad index pattern and small-holonomy statement only; no continuum, uniqueness, or Einstein-equation claim |
| “derived normal” | algebraic unit normal of the three supplied spatial coframe columns; not a fourth base direction, time normal, or signature selector |
| “background” / “witness” | explicit supplied point (20)--(25), not a selected vacuum or phase |
| “numerically stationary” | centered finite differences cover all 72 intrinsic link and 128 ambient coframe coordinates on one finite cube; no interval certificate or infinite-lattice solution |
| “exact `10^8` sum” | exact tensor contraction of the finite label sum using floating elementary weights; not exact symbolic arithmetic |
| “coercive” | positive quartic tail in the declared finite Lebesgue integral; not reflection positivity or Lorentzian stability |
| “SO(4)” | internal Euclidean frame group on a spatial base; not the Lorentz group or lattice diffeomorphism group |
| “gravity discriminator” | distinguishes the corrected intrinsic EC index/linear term from the rejected dual-face index and displayed Wilson comparator only |
| “sine curvature” | a chart-local antisymmetric holonomy coordinate; the executed pi-holonomy control forbids a global-coordinate reading |
| “joint law” | one finite supplied extensional weight and measure; not an axiom-selected Admissibility distribution or DLR limit |
| “canonical” / “registered” | premise-registry status only; no canonical axiom or primitive is modified |

The carrier, measure, coefficients, link ansatz, Gram targets, Euclidean
signature, cube boundary, and finite-volume scope are explicit inputs rather
than hidden assumptions. The scan found no load-bearing “as is standard,”
“naturally,” “obviously,” “standard QFT,” or “bridge context” step.

### N4 — Residual Matching

| cited witness (path:line) | residual attacked by the witness | residual claimed closed here | match? |
|---|---|---|---|
| `docs/ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:690-716` | build the full proper-cubic closed spatial plaquette orbit with holonomy, compatibility/torsion, linear curvature, one normalized Record law, and load-bearing contact | bounded existence of exactly that supplied elementary-cube package | yes; this is the primary matched parent residual |
| `docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:111-120` | derive a Record geometry carrier, full-`Z^3` phase, Ward theorem, and Lorentzian update | one supplied elementary spatial curvature law | no; broader campaign context only, dropped as direct closure support |
| `docs/ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:236-267` | complete source/generator/connection data for a reconstructed Regge branch | Record-loaded coframe/link cube stationarity | no; method-shape only, dropped as Regge or gravity closure support |
| `docs/CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md:75-87` | match a supplied Regge second variation to a linearized target operator | select the present microscopic Record/coframe/link law | no; useful alternate route, not evidence for current-law selection |

After dropping the three nonmatches, the bounded claim retains one directly
parent residual and the landing runner supplies its direct certificate. The
result matches the bounded construction obligations; it is not an exact
symbolic stationarity or universal-law theorem. No Regge, continuum-Einstein,
or axiom residual is borrowed.

### N5 — Resolution And Rhetoric Audit

| resolution | executed | not executed / negative wording permitted |
|---|---|---|
| per element | all ten projective rays and both proper-cubic ray orbits | no claim over every element of `M_2(C)` |
| per site | all eight coframes, shared Record labels, twelve edge transports, and independent endpoint frames | no generic six-neighbour infinite-lattice conditional theorem |
| per mode | not executed: coordinates are not modes | no Bloch, continuum, graviton, or Lorentzian mode decomposition; the runner separately checks 128 coframe coordinates and 72 link tangents |
| per face/edge | all six faces, twenty-four based loops, and twelve links | no arbitrary complex or refinement theorem |
| per block | one supplied normalizable cube law plus pure-gauge, zero-holonomy, Wilson, and deletion controls | no uniqueness or physical action selector |
| lattice wide | not executed: one complete cube orbit is still one block | explicitly not an increasing-region/full-`Z^3` phase, lattice-Bianchi/Einstein regime, `Z^3 x Z_tau` spacetime law, or Lorentzian update |

Accordingly “not a gravity derivation” means that the tested finite supplied
law does not derive/select gravity. It never means that gravity cannot emerge
per site, per mode, per block, or lattice-wide. The primary runner emits these
five substantive resolution lines into its cached stdout, using “checked and
not executed” for the two unexercised resolution classes.

### N6 — Partial-Closure And Primitive Scan

The required registry check was executed against
`docs/audit/data/axiom_premise_nodes.json` and all three approved primitive
source notes. Approved primitives are premises, not walls; proposed or absent
primitives receive no premise weight.

| candidate path | current status | what it closes, and what it does not |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:35-84,88-130,169-186` | canonical registered axiom node | supplies lattice, local possibility, Admissibility-distribution, and Record scope while leaving extensional weights, dynamics, source/action, and gravity self-consistency downstream |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` | approved registered primitive | closes units conversion only; supplies no dimensionless coframe/link carrier, joint measure, curvature law, or dynamics |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | approved registered primitive | supplies only equal-form OS0 kinetic graining `c_t=c_s`; no dynamics, gravity action, or Lorentz-closure theorem |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | approved registered primitive | permits evaluation at a supplied law-admissible state; supplies no state, weights, law, or selector |
| Block-35 local geometry carrier | stacked bounded construction | demonstrates that carrier refinement can retire an apparent ontology wall; does not derive the continuous coframe/link law |
| Block-36 coframe/link lift | stacked bounded construction | supplies a concrete continuous carrier and local-frame identity; does not select curvature or an increasing-region law |
| this Block-37 cube law | supplied bounded construction | retires finite-cube coexistence and normalization; provides an explicit import-retirement target for W1/W2, not their derivation |
| translation-invariant finite-range Gibbs/DLR extension | live downstream route, not yet a premise | could close W3 without a new ontology axiom if overlapping-cube consistency, tightness, and phase control are proved |
| spatial Regge dual-hinge route (`docs/CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md:104-109`) | live source-note route; no audit status asserted here and not executed this cycle | can replace links by length/deficit data, but still needs a Record-loaded shared-hinge law and physical selector |
| `Z^3 x Z_tau` Regge route (`docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md:34-40,97-101`) | live source-note route; no audit status asserted here and not executed this cycle | can test the spacetime area/deficit index structure after a causal carrier is justified; it is not supplied by this spatial block |
| independent constrained BF/Plebanski route | live and unexecuted | could impose simplicity on an independent bivector carrier; needs that carrier, constraint law, measure, and selection mechanism |
| refitted teleparallel route | live and unexecuted | could move response from curvature to torsion/transport; the present deletion control tests only the current unrefitted law |

Existing positive paths include deriving collective coframes from Record
correlations, defining transport from nearest-neighbour conditionals, deriving
coefficients by an extremal or consistency principle already downstream of
Admissibility, translating the cube potential to a compatible finite-range
specification, and later retiring each explicit import. None is exhausted.
No convention-only rename supplies gravity, but neither is a new axiom proven
necessary.

### N7 — Steelman

> **Hostile reviewer:** The finite boundary is not yet evidence for an axiom
> wall. The four axioms permit one fixed covariant Admissibility distribution,
> and the runner has exhibited a positive, coercive cube potential with the
> correct local-frame and proper-cubic covariance. Its particular stationary
> link ansatz depends on edge midpoints relative to this cube's center, so do
> not merely copy that witness. First place two face-sharing cubes on one
> coordinate lattice, share their Record/coframe/link variables, and solve for
> a translation-compatible connection—beginning with a homogeneous or
> period-two link field—under one common potential and one common Gram rule.
> Count each geometric face and edge once, prove the overlap conditionals are
> restrictions of a single finite-range specification, and only then use the
> quartic tail plus compact Haar sector for increasing regions. The terminal
> obligation is a shared-link stationary two-cube solution followed by an
> `L^3` sequence with compatible conditionals, ordered-product Bianchi
> identities, and a weak-curvature Hessian with the required gauge null space.
> Until that explicit translation-compatible construction fails, neither a
> gravity no-go nor a fifth-axiom claim is credible.

This is a concrete unclosed mechanism with a terminal obligation. It defeats
every broad no-go and becomes the next campaign target. It does not change the
literal fact that the present one-cube inputs are supplied and no increasing-
region theorem has yet been executed.

### N8 — Cross-Cycle Echo

The required phrase search across `docs/` and walk of physics-loop
`NO_GO_LEDGER.md` files found these closest wall shapes.

| prior wall (path:line) | retired/status and mechanism | present wall | can the mechanism apply? |
|---|---|---|---|
| `.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md:282-294` — slice-global geometry carrier | retired locally by Block 35's sitewise field; carrier refinement, not an axiom edit | W1 | yes; derive a collective coframe/link observable or equivalent discrete carrier before proposing ontology enlargement |
| `docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:592-599` — no continuous local-frame or curvature carrier | partially retired by Blocks 36 and 37 through successively richer supplied local laws | W1 / W2 | yes as import-retirement strategy; now derive rather than further decorate the carrier |
| `docs/ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:690-716` — closed proper-cubic Palatini/Record cube target | retired at bounded finite-cube existence by this block | old curvature-existence part of W2 | yes; the same constructive escalation now moves to overlaps and coefficient selection |
| `.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md:145-159` — missing joint source/generator/connection law | partially reframed by full-action Ward bookkeeping in Block 36 and one joint curvature law here; physical selection remains live | W2 / W4 / W5 | yes for bookkeeping, not as physical selection evidence |
| `.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md:23` — source convention, Noether/Ward, dynamics, and field-equation routes live | still live; finite fixtures separate but do not close these obligations | W4 / W5 | a translated shared-variable law and displacement theorem may close W4; weak-curvature/source analysis is separately needed for W5 |
| `.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md:294` — OS reconstruction and permanent-Record causal dilation | live | W6 | carrier refinement alone is insufficient; a causal update and reconstruction argument remain required |

The repeated lesson is constructive: walls previously described at ontology
level have often been retired by refining the carrier or completing one joint
law. That same mechanism has not yet been exhausted for W1--W3, so broad
negative or axiom-necessity language would be premature.

**N1--N8 status:** `PASS` for the narrow statement that this supplied finite
cube is not itself a law-selection, increasing-region, Einstein, Lorentzian,
or axiom-necessity theorem. `FAIL` for a gravity no-go or fifth-axiom necessity
claim, neither of which ships.

## Reproduction

Run:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_proper_cubic_spatial_plaquette_record_coframe_palatini_curvature_boundary_2026_08_11.py
```

Expected final line:

```text
TOTAL: PASS=21 FAIL=0
```

The runner generates the full cube and proper-cubic orbit, numerically solves
the two equivariant parameters, checks all seventy-two intrinsic link
derivatives and all 128 coframe entries, contracts the `10^8` Record
assignments tensorially, and runs the stated covariance, index, chart-boundary,
alternative-law, derived-link, and destructive controls. It creates no dense
lattice transfer or `10^8` array.

## Exact Next Target

Do not add another one-cell term first. Rebuild the exact microscopic weight
(10) on **two face-sharing cubes** with one shared Record label and coframe per
common vertex, one shared link per common edge, and one count per geometric
face. The current midpoint-dependent stationary link ansatz is cube-centered
and may not simply be translated; solve instead for a homogeneous, period-two,
or otherwise translation-compatible shared-link field. Require both one-cube
marginals/conditionals to agree with a single finite-range specification after
boundary factors are named. Then:

1. test whether overlap consistency constrains or removes `sigma`, `beta`,
   `eta`, `tau`, the orbit weights, or the reverse-engineered Gram targets;
2. solve the full shared-link and shared-coframe stationary equations without
   fitting separate wells per cube;
3. execute the elementary ordered-product lattice Bianchi identity and
   distinguish it from a base-displacement/diffeomorphism Ward identity;
4. extend to periodic `L^3` regions with a uniform coercive bound and check
   phase/tightness and finite-size Hessian scaling; and
5. only after a common weak-curvature phase exists, test the two-derivative
   Einstein tensor structure, universal Record source coupling, physical
   modes, and the separately declared `Z^3 x Z_tau`/Lorentzian update.

In parallel, attempt to derive the shared carrier and coefficients from the
existing Admissibility/Record law. If overlap and derivation succeed, W1--W3
can close downstream without an axiom edit. If they fail, the failure must name
the exact incompatible condition before any axiom amendment is proposed.
