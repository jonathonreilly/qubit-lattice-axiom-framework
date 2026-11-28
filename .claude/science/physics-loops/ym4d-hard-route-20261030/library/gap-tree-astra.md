# Repo search

**READ.** The pin is `619472ccd0702b20c2b5a753d3bc56eb47cfec91`.
`prior/gap-tree-astra.md` is absent. The lead's general record,
`prior/repo-search-2026-11-08.md`, concerns the earlier admission and
history tasks. Its nearest hit is the one-step transfer witness in
PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`. I read lines 89–166 at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. It proves a positive local
correlation, keeping the exterior normalizer. It does not estimate a
twist deficit. The related literature check, lines 105–135, already
records Ito and Seiler's common-interpolation objection. Both are reused,
not rebuilt.

**READ.** Main was fetched at `bb4ec020d5ada57c630dd89acc98a68397ade423`.
The prior-work inventories also point to
`docs/BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md`.
I read that note in full from main. It concerns SU(3), finite numerical
coefficient samples, and the missing higher-dimensional intertwiner
contraction. None of its numerical claims is used here. Its warning that
one-link character coefficients do not contract the full network applies.

**READ.** The close lane work is more specific. `gap-kappa-order.md:31–74`
already gives the signed surface expansion and some positive elementary
surface integrals. It explicitly leaves branching contractions unresolved.
`prior/gap-seed-lit.md:47–53` records Pfeiffer and Oeckl's signed dual
representation: positive plaquette coefficients do not give positive
spin-network contractions. Thus an attempted positive spin-foam measure
would redo an already diagnosed problem. This note instead tests an
operator-norm contraction after retaining the intertwiner spaces.
It does not attack the separately owned Pfaffian comparison (KP).

**READ.** Searches of `open-registry.md`, `open-core.md` and `l17c.md`
for this target, twist-deficit names, recoupling and singlet-projector
contraction located no competing owner. The source searches above, and
the searches of the SA index, are bounded vocabulary searches. They are
not an absence theorem. The general digest's four-PR search is credited
to its author; this run did not repeat that whole search.

**READ.** A narrow follow-up for the filter and icosahedral-moment
statements found no match outside this lane on main or the four PRs.
The additional fetched heads were PR 10133 `89faef229`, PR 10134
`1e70c7211`, and PR 10141 `fb99b4ddd`. The exact refs, queries and
complete outputs are retained in the run's scratch directory. A broader
singlet-projector search was only an inventory, not a full source review.

# A proof tree and a local Casimir-filter test

Author: **Codex gpt-6-astra max**, FINISH row 804, 2026-11-12.
Research text, not an audit; this grants no scientific status.
**READ** reports source content. **PROVED** means a hand argument here,
not an independent check. **ARGUED** is an inference with its scope stated.
**GUIDE** ranks a proposal; **OPEN** names a missing assertion.

**READ.** GOAL and the requested FINISH instructions were read first.
The RESULT entries of rows 783–802 were read; row 803 has no RESULT at
this pin. The source readings retain the corrections in rows 788, 791,
795, 798, 799 and 801. No audit or status file is changed.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as the
authors of their text**, for every outline/account input below. Credit
Claude Fable 5.2 for `gap-kappa-order.md`, and the named Codex authors
and Claude checkers for the earlier gap notes. The outline and CA-I at
`31a47c543775` were each fetched once into the new directory
`/tmp/sa-gap-tree-astra.XztH2L/`. No numerical run is used.

## Checkpoint

**OPEN, final checkpoint.** The two-filter contraction is proved, but it
is shared by the finite comparison group. Haar tensors first differ at
degree twelve; (G15) gives a charged filter that distinguishes both test
groups. Haar sewing cannot insert these filters for free, and winding
terms need not encounter their channels. The remaining task is the
resummed Wilson-block realization specified in section 6, with its
scalar cost. No (FQ), (V), or new strong-coupling seed is proved.
The next useful action is to construct that block comparison, not to
recompute the local filters or the moment table.

## 1. Consumer and short proof-tree sketch

**READ.** Use `gap-ext-astra.md:78–128`: on
`n=(a,a,c,d)`, `c,d in {a,2a}`, at fixed beta in a compact interval
`I` of positive couplings, put

\[
 R_{m,v}=Z^{m+v}/Z^m,\qquad F_{m,v}=-\log R_{m,v}.
 \tag{G1}
\]

Here m is spatial and v temporal in the chosen frame. The stronger
target (V) bounds F by `C a^p exp(-sigma a^2)` for the required pairs.
The weaker crossed-pair consumer is (FQ) in that source. Its available
witness gives `S_ev >= eta_*^a`; hence an exponential bound in a with
a sufficiently large rate would already suffice for that consumer.
All partition functions retain the original Wilson normalization.

**GUIDE — ranking before execution.** All three routes have low overall
prospects without a new Wilson estimate. The ranking is relative, not a
probability claim. The group tests below identify a proposed first failed step
of the proposed proof for the comparison group. They do not claim that
the comparison group's phase alone refutes a local lemma at beta=1.
Estimated chance of closing the twist bound: A, then B, then C.
Feasibility of a decisive hand test of the key step has the same order.

| Rank | Quantitatively new input, not a scalar rewrite of (G1) | U(1): first unavailable step | Binary icosahedral group: first unavailable step | Hand test |
|---|---|---|---|---|
| A, execute | Two incompatible pair-Casimir filters damp a center-odd boundary channel; an actual Wilson block must supply those filters with a controlled scalar factor. The new input is a boundary-operator inequality, for all vectors in a specified representation space. | A one-dimensional irreducible has no two incompatible singlet pairings; the explicit failure is below (G11). | Continuous SU(2) rotations cannot be flows inside the finite group. Execution finds this proposed distinction insufficient: (G7) is shared. The first successful distinguishing bound is instead (G15), which fails on the finite group's invariant subspace. | Exact two-dimensional calculation; then an exact Haar-tensor test. Best chance of a decisive local answer. |
| B | A bad-curvature form bound after integrating Wilson fields: local negative Hessian terms are paid by Hessian squares with a coefficient strictly below one, leaving a positive SU(2) Ricci margin. This must be proved for arbitrary gauge-invariant test functions, uniformly in volume. | The Ricci reserve of the abelian group is zero. | There is no positive-dimensional Haar manifold or corresponding integration-by-parts identity. | The existing pointwise curvature test already fails. The proposed integrated bound is substantially harder; not executed. |
| C | A genuine blocked-action estimate: on an order-one compact coupling interval, an explicit exact block map enters a convergent local-interaction norm ball after finitely many steps, with a summable norm bound on every generated interaction and the vacuum term. | The proposed nonabelian drift uses a nonzero adjoint bracket; it vanishes. | The small-field differential expansion and its unbounded SU(2) representation ladder terminate. | Finite-block identities are hand-checkable; a volume-uniform remainder theorem is not supplied. Lowest present prospect. |

**OPEN, precise extra input for B.** In the product of unit three-spheres,
write `S=beta sum_p(1-tr U_p/2)`. One possible sufficient inequality is

\[
 \int \operatorname{Hess}S(\nabla f,\nabla f)\,d\mu
 \ge -\theta\int\|\operatorname{Hess}f\|^2\,d\mu
       -(2-\kappa)\int|\nabla f|^2\,d\mu,
 \quad \theta<1,\ \kappa>0.                         \tag{G2}
\]

This is a proposed integrated local-energy estimate, not proved here.
It is stronger machinery than a twist estimate. Merely assuming the
resulting Poincare bound would return to the earlier (TU) continuation
route; that is discarded. No inference from (G2) to the twist consumer
is counted as complete without its spectral and normalization bridges.

**READ / discarded.** The following are not additional routes:

- Exterior reweighting without a new inequality is row 783 (26).
- Optimizing transport cost without a constructed estimate is (TR-F).
  Small moves and one-color finite-range moves meet (T7), (T9) and
  (S19)–(S24), respectively. Overlapping block maps remain outside those
  exclusions, but naming them proves no cost bound.
- Matching decimation parameters, or integrating their response without
  a new estimate, is (K-RESP). `gap-kanazawa-astra.md:458–494` explicitly
  permits any fine ratio in its inverse representation.
- A recursion in size without a Wilson gluing estimate and its seed is
  row 802's remaining obligation, not a new route.
- A positive measure of individual spin-foam channels is not assumed:
  the signed-contraction problem is already in the prior work above.
- Bare commutator contraction supplies neither Casimir damping nor a
  scalar-normalizer comparison; its value 1/4 is shared by the finite
  comparison group. An infinite representation ladder alone supplies
  neither estimate either.

**GUIDE.** The proof tree for A is now fixed:
`pair-filter contraction -> Wilson block realization -> charged-channel
propagation with boundary control -> original-normalization twist bound`.
Only the first arrow's local algebra has an immediate finite hand test.
The other arrows are obligations, not implications silently assumed.
The sketch ends here; the remainder executes A.

## 2. Published input reused, not re-derived

**READ.** The SA-index README, chunk-02 rows at 84–100 and their
neighbouring proof-dependency rows locate outline 2195–2281.
I read those source lines. Equations (GL3)–(GL4) prove, with normalized
Haar measure, the Wilson convolution eigenvalues and ratio bound

\[
 c_j=\frac{2e^{-\beta}}\beta I_{2j+1}(\beta),\qquad
 r_j=\frac{c_j}{c_0}=\frac{I_{2j+1}(\beta)}{I_1(\beta)},\qquad
 \frac{I_{n+1}(\beta)}{I_n(\beta)}
       \le\frac{\beta}{2(n+1)}.                       \tag{G3}
\]

Their positive Bessel series proves factorial decay; the subsequent
Clebsch–Gordan argument proves smooth conjugation. These are their
proved inputs. They are not new work of this note. In particular,

\[
 0<r_1\le\beta^2/24.                                  \tag{G4}
\]

**READ.** The index's mass-gap limitation is confirmed at outline
31860–31884: a positive spectral gap needs an additional interval
exclusion estimate. The account is not being credited with a confinement
bound. Searches of the 4.12–4.19 index for the present representation
objects locate no supplier; its Schur complements concern other operators.

## 3. Execution: two actual convolution filters

**PROVED, Lemma 1.** Let `V=C^2`, `H=V tensor V tensor V`, and let
`s=(e_+ tensor e_- - e_- tensor e_+)/sqrt(2)` be the unit singlet.
Define isometries and projections

\[
 J_{12}v=s\otimes v,\quad J_{23}v=v\otimes s,\qquad
 P=J_{12}J_{12}^*,\quad Q=J_{23}J_{23}^*.
 \tag{G5}
\]

All of H is center-odd under the simultaneous action of `-I`.
Let `k_beta(g)=exp(beta tr(g)/2)/z(beta)`, with `z` its Haar integral.
The following are pair rotations, not the three-link Wilson Gibbs law:

\[
 A=\int k_\beta(g)(g\otimes g\otimes I)\,dg,
 \qquad B=\int k_\beta(g)(I\otimes g\otimes g)\,dg.
 \tag{G6}
\]

Writing `t=r_1(beta)` from (G3),

\[
 A=P+t(I-P),\qquad B=Q+t(I-Q),\qquad
 \|AB\|\le\tfrac12+2t\le\tfrac7{12}
       \quad(0<\beta\le1).                            \tag{G7}
\]

For every finite positive beta, `0<t<1` and `||AB||<1`.

**PROVED, argument.** On `V tensor V`, the antisymmetric line is the
trivial representation, and its orthogonal symmetric complement is spin 1.
Schur's lemma and (G3) therefore give (G6)'s two stated spectral forms.
Direct contraction of the displayed singlets gives

\[
 J_{12}^*J_{23}=-\tfrac12 I_V,\quad PQP=\tfrac14 P,
 \quad \|PQ\|=\tfrac12.                               \tag{G8}
\]

For example, for `v=e_+`, the two tensors are
\((|+-+\rangle-|-++\rangle)/\sqrt2\) and
\((|++-\rangle-|+-+\rangle)/\sqrt2\).
Their only common basis word has coefficient product `-1/2`. The same
calculation for `e_-` gives `-1/2`, and the cross inner products vanish.

Now `||A-P||=||B-Q||=t` and `||A||=||B||=1`. Thus
`AB-PQ=(A-P)B+P(B-Q)` has norm at most `2t`.
Use (G4) for the rational bound in (G7).

For the strict bound at any finite beta, the central positive density
`k_beta` has full support. Equality in the norm of its average in a
nontrivial irreducible would require a vector fixed by every group
element. Thus `t<1`; positivity is (G3). If `||AB x||=||x||`, both
contractions must preserve norm. This forces `x in ran Q` and then
`x in ran P`. But (G8) gives `ran P intersect ran Q={0}`.
The unit sphere of finite-dimensional H is compact, so `||AB||<1`.

**PROVED, exact quantitative version.** The subspace
`M=ran P+ran Q` is four-dimensional. The isometry
`J_r=(2J_23+J_12)/sqrt(3)` is orthogonal to `J_12`.
On `M=(J_12 V) direct-sum (J_r V)`, suppressing the factor `I_V`,

\[
 P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 Q=\begin{pmatrix}1/4&-\sqrt3/4\\-\sqrt3/4&3/4\end{pmatrix}.
 \tag{G9}
\]

For each displayed two-dimensional block, the squared singular values
of AB have sum and product

\[
 T=2t^2+\frac{(1-t^2)^2}{4},\qquad t^4.
 \tag{G10}
\]

Indeed `A^2=t^2 I+(1-t^2)P`, and likewise for B. Take
`tr(A^2 B^2)`, using `tr P=tr Q=1`, `tr PQ=1/4`.
Also `det A=det B=t`. On `M^perp`, AB equals `t^2 I`.
The larger singular value on M is at least t and hence at least `t^2`.
Consequently

\[
 \|AB\|^2=\frac{T+\sqrt{T^2-4t^4}}2.
 \tag{G11}
\]

This is a two-dimensional hand calculation, not a numerical certificate.

**PROVED, U(1) control.** Restrict V to
`g_theta=diag(exp(i theta),exp(-i theta))` and form the same normalized
pair averages over U(1). The vector
`e_+ tensor e_- tensor e_+` has pair charge zero in positions 12
and 23. Both averages fix it, at every beta. Its total charge is one,
so it is center-odd. Hence the corresponding product has norm one.
The first failing step is the one-dimensional SU(2) singlet projection
in (G5): the U(1)-invariant pair space is two-dimensional and has a
common charged extension in the two positions.

**ARGUED, relevance and limit.** (G7) is a local contraction at an
order-one coupling. It is not an equivalent formula for a partition
function ratio. But the symbols A and B are new pair convolutions.
Haar integration at a Wilson link is a different operator. Their
realization cannot be supplied by the numerical value `7/12`.

## 4. Where SU(2) first differs from the finite comparison group

**PROVED, Lemma 2 (Haar tensors through degree eleven).** Let Gamma be
the binary icosahedral subgroup in its defining SU(2) representation V.
For `0<=n<=11`,

\[
 \frac1{120}\sum_{g\in\Gamma}g^{\otimes n}
       =\int_{SU(2)}g^{\otimes n}\,dg.                 \tag{G12}
\]

At `n=12`, the left side is the right side plus a rank-one orthogonal
projection, supported on `Sym^12 V` (spin 6). Thus a Haar-tensor test
of degree at most eleven cannot separate these two groups.
This assertion concerns unweighted Haar tensors, not their exact
Wilson-tilted laws at positive beta.

**PROVED, hand calculation.** The rotation group of the icosahedron
has one identity, 15 half-turns about opposite-edge axes, 20 rotations
by plus or minus `2 pi/3` about opposite-face axes, and 24 rotations
about opposite-vertex axes. The last split into 12 with angle
`2 pi/5` up to sign and 12 with angle `4 pi/5` up to sign.
The counts are `15*1`, `10*2`, and `6*4`; with the identity they total 60.
Gamma is their double cover.

Half-integer spin has no Gamma-invariant vector since `-I` acts as
minus the identity. For integer j, the character at rotation angle
theta is `1+2 sum_{r=1}^j cos(r theta)`. Its invariant multiplicity is

\[
 m_j=\frac{(2j+1)+15(-1)^j+20 b_j+12 d_j}{60},
 \quad b_j\in(1,0,-1)\text{ periodically in }j,
 \quad d_j=2-j+5\lfloor j/5\rfloor.                  \tag{G13}
\]

Here `b_j` is the character at `2 pi/3`. For the sum of the two
fifth-turn characters, each r not divisible by five contributes
`2(cos(2 pi r/5)+cos(4 pi r/5))=-1`; a multiple contributes 4.
This gives `d_j` without decimal trigonometry. The small table is

| j | 2j+1 | (-1)^j | b_j | d_j | 60 m_j |
|---|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 2 | 60 |
| 1 | 3 | -1 | 0 | 1 | 0 |
| 2 | 5 | 1 | -1 | 0 | 0 |
| 3 | 7 | -1 | 1 | -1 | 0 |
| 4 | 9 | 1 | 0 | -2 | 0 |
| 5 | 11 | -1 | -1 | 2 | 0 |
| 6 | 13 | 1 | 1 | 1 | 60 |

Iterated Clebsch–Gordan decomposition places only spins `j<=n/2`
in `V^tensor n`. For even n at most ten, (G13) leaves only its
SU(2)-trivial summands fixed by Gamma. For odd n, the center removes
all invariants. A compact-group average is the orthogonal projection
onto the invariant subspace: invariance follows by changing variables,
self-adjointness by inversion, and idempotence by averaging twice.
Thus the two averages have the same range and are equal for `n<=11`.
At n=12 the spin-6 summand occurs once, as the highest symmetric
power; (G13) adds exactly one invariant line there. This proves (G12).
Mixed V and conjugate-V tensors obey the same conclusion, since the
SU(2)-invariant alternating form identifies conjugate V with V.

**PROVED, why Lemma 1 is shared.** Restricted to Gamma, spin 1 is still
irreducible. Its character squared is `chi_0+chi_1+chi_2`, so (G13)
gives character norm squared one. With the finite-group Wilson density,
the pair convolution is therefore still `P+t_Gamma(I-P)`.
Its coefficient satisfies `0<t_Gamma<1` at every finite positive beta.
Positivity follows by expanding `exp(beta chi_V/2)`: each character
inner product is a nonnegative representation multiplicity, and the
quadratic term already contains spin 1. Strictness follows from full
support as in Lemma 1. Hence the same two-filter norm formula (G11)
holds. This defeats an attempted finite-group distinction based only
on the two incompatible low-spin singlets. The preliminary differential
argument in the sketch was not used by that calculation.

**PROVED, a distinguishing filter.** On `W=Sym^12 V`, put
`C_beta,W=int k_beta(g) D_W(g) dg`. For SU(2), (G3) gives

\[
 C_{\beta,W}=r_6 I_W,\qquad
 r_6\le\frac{(\beta/2)^{12}}{13!}.                   \tag{G14}
\]

The bound is the product of the twelve inequalities (G3) for
`I_13/I_1`; no coefficient is evaluated numerically. For Gamma the
same construction, with its own normalized Wilson density, fixes the
unit vector on the invariant line in W. Its norm is one. For U(1),
the zero-weight vector in W is fixed, so its norm is also one.
Thus (G14), as an operator-norm estimate for `0<beta<=1`, fails
for both comparison groups at an explicit invariant subspace.
The Wilson coefficient bound is Sussman and Alpoge's input; the finite
group comparison and its role here are the present hand argument.

**PROVED, charged version.** Let `H'=V tensor Sym^12 V`. It is
center-odd, and as an SU(2) module it is the sum of spins `11/2`
and `13/2`. For `0<beta<=1`, normalized convolution satisfies

\[
 \|C_{\beta,H'}^{SU(2)}\|
       \le\frac{(\beta/2)^{11}}{12!}.                 \tag{G15}
\]

The two factorial bounds from (G3) are
`(beta/2)^11/12!` and `(beta/2)^13/14!`; the latter is no larger
when beta<=1. Thus their maximum gives the displayed operator norm.

For Gamma, tensor its invariant line in W with V. This is a copy of V,
which is irreducible since `chi_V^2=chi_0+chi_1` and (G13) gives
character norm one. On that copy the convolution eigenvalue is

\[
 r_V^\Gamma
 =\frac{\mathbb E_\Gamma[\chi_V e^{\beta\chi_V/2}]}
              {2\mathbb E_\Gamma[e^{\beta\chi_V/2}]}
 \ge\frac{\beta}{4e^\beta}>\frac{\beta}{12}.
 \tag{G16}
\]

Every coefficient of the numerator's power series is nonnegative:
`E_Gamma chi_V^(k+1)` is an invariant multiplicity. Its linear term
is `beta/2`, since `E_Gamma chi_V^2=1`. The denominator's expectation
is at most `e^beta`. Finally `e<3`, for example by comparing `1/n!`
with `1/2^(n-1)` for n at least two, with strict inequality at n=3.
This proves (G16). For U(1), H' has a weight-one vector. Its eigenvalue is
`E[cos(theta) exp(beta cos(theta))]/E[exp(beta cos(theta))]`.
Expand the numerator: odd moments vanish, the others are nonnegative,
and the first term is `beta E cos^2(theta)=beta/2`.
The denominator is at most `e^beta`, so the eigenvalue exceeds
`beta/6`. Both lower bounds exceed
(G15). This is a distinction on an explicitly center-odd space.

**PROVED, normalization caution.** Formula (G12) does not say that
finite-group Wilson expectations equal SU(2) expectations. For instance,
with `z_G(beta)=E_G exp(beta chi_V/2)`, it implies precisely

\[
 z_\Gamma(\beta)-z_{SU(2)}(\beta)
   =\frac{\beta^{12}}{2^{12}12!}+O(\beta^{14})
       \quad(\beta\longrightarrow0).                \tag{G17}
\]

Indeed `E chi_V^n` is the invariant dimension of `V^tensor n`.
The first difference is one at n=12; odd terms vanish. The Taylor
series converge absolutely since `|chi_V|<=2`. This also explains why
a low-degree unweighted test cannot supply an all-beta comparison.

**PROVED, extension to any compact interval.** The distinction is not
restricted to beta<=1. Identify `Sym^12 V` with degree-twelve binary
forms, using the invariant alternating form to identify V with its
dual. Let h be a nonzero Gamma-invariant form supplied by Lemma 2.
The polynomial `h^k` is nonzero and Gamma-invariant in `Sym^(12k) V`.
For each k>=1 the SU(2) convolution on this space obeys

\[
 r_{6k}(\beta)\le\frac{(\beta/2)^{12k}}{(12k+1)!},
 \tag{G17a}
\]

whereas the Gamma convolution fixes `h^k`; U(1) again fixes a
zero-weight vector. For a fixed compact `I=[beta_-,beta_+]`, choose k
large enough that the factorial bound is below one throughout I.
This is an explicit existence choice: the ratio of successive upper
bounds is `(beta_+/2)^12/[(12k+2)...(12k+13)]`, which tends to zero.

On the center-odd space `V tensor Sym^(12k) V`, the SU(2) eigenvalues
are `r_(6k-1/2)` and `r_(6k+1/2)`. The sum of their two factorial
upper bounds tends uniformly to zero on I. In contrast, Gamma has
the copy `V tensor span(h^k)` with eigenvalue at least
`beta_-/(4 exp(beta_+))`; U(1) has a weight-one eigenvalue at least
`beta_-/(2 exp(beta_+))`. Choose k so that the SU(2) bound is below
half the former number. Thus a quantitative charged local distinction
is available on every such I. What is absent is its Wilson exposure.

## 5. Execution on Wilson tensors: two failed realization lemmas

### 5.1 Haar sewing does not supply the two filters

**PROVED, Proposition 3.** The following proposed local lemma is false:

> After extracting the positive Wilson face coefficients, every
> four-fundamental link tensor in a charged boundary channel factors
> through the two filters of Lemma 1 with comparison norm at most one.

Take one four-dimensional lattice link with four incident plaquettes
labelled spin `1/2` and its other two incident plaquettes labelled zero.
Leave its boundary indices open. Since V is self-dual, unitary
identifications turn its oriented Haar tensor into

\[
 H_4=\int_{SU(2)}g^{\otimes4}\,dg
    =P_{\operatorname{Inv}(V^{\otimes4})}.             \tag{G18}
\]

The invariant space has dimension two: pair the first two factors
into spin 0 or spin 1 and do the same with the last two; each equal
pair has one total singlet. In particular
`h=s_12 tensor s_34` has norm one and `H_4 h=h`.
This is the literal Haar tensor in the Wilson character expansion.
Its four nontrivial face coefficients are positive for every beta>0.
No zero or forbidden coefficient is used.

Identify this invariant space with the multiplicity space
`Hom_SU(2)(V,V^tensor 3)`, by adjoining a dual fourth factor and
contracting it with the output of an intertwiner. Use normalized
Hilbert–Schmidt inner product so this identification is an isometry.
The first three strands carry center-odd charge. The pair filters
in section 3 act on this space with the matrices (G9); call their
product `K`. The Haar tensor restricted here is the identity, whereas
`||K||<=7/12` for `0<beta<=1`.

Consequently any proposed exact factorization, even allowing an error,
obeys the necessary inequality

\[
 I=\alpha LKR+E,\quad \|L\|\|R\|\le1,\quad\|E\|\le\epsilon
 \quad\Longrightarrow\quad
 1\le |\alpha|\,\|K\|+\epsilon.                     \tag{G19}
\]

For zero error the scalar cost is at least `1/||K||`, hence at least
`12/7` in the stated interval. A factor of `7/12` cannot be extracted
for free from this link tensor. The cost exactly defeats that local
contraction. The proof is just the operator norm of the displayed
identity, tested on its two-dimensional invariant space.

**ARGUED, scope.** This refutes an all-boundary, termwise sewing rule
after the face weights have been extracted. It does not refute an
inequality for a full resummed Wilson block. Face coefficients still
pay for occupied plaquettes; the statement does not remove their
strong-coupling gain. Nor does it assert that one individual tensor
is a normalized Gibbs law or a counterexample to confinement.
The exact failed step is identifying a Haar projection with a product
of two non-Haar convolution filters at no scalar cost.

### 5.2 Charged propagation need not reach the distinguishing spins

**PROVED, Proposition 4.** Neither center-odd charge nor an arbitrarily
large number of fundamental strands forces the high-spin channel of
(G15). For each integer k>=1 the map

\[
 J_k:V\longrightarrow V^{\otimes(2k+1)},\qquad
 J_k v=s^{\otimes k}\otimes v                         \tag{G20}
\]

is an SU(2)-equivariant isometry. Its image is spin `1/2`, is
center-odd, and has the same Casimir as V, independently of k.
Equivariance follows because every singlet factor is invariant;
isometry follows because each has unit norm. Thus even very large
charged tensors can retain a low-spin channel. They cannot all be
bounded by the high-spin eigenvalue in (G15). Pairing many strands
is not the same operation as projecting onto their symmetric power.

**READ plus PROVED application to an actual Wilson term.** Use the
already proved torus/disc calculation of `gap-kappa-order.md:66–74`.
Choose a single flat, wrapping `(r,i)` plane of A plaquettes. Assign
spin `1/2` to every plaquette of that plane and zero to every other
plaquette. The closed surface has no branching edge, and it pairs
oddly with the complementary twist sheet. Every occupied link has
only two fundamental strands, with a single Haar singlet contraction.
No spin-6 face, thirteen-strand symmetric channel, or competing
pair of four-strand singlets is present.

In the normalized character expansion

\[
 \frac{e^{\beta\operatorname{tr}g/2}}{z(\beta)}
     =\sum_j d_j r_j(\beta)\chi_j(g),
 \tag{G21}
\]

the scalar contribution of this plane is exactly `r_(1/2)^A>0`.
Indeed the cited torus integral for normalized fundamental traces
is `4^(-A)`; replacing each trace by `chi_(1/2)=2x` makes the
integral `2^(-A)`. The face factors in (G21) contribute
`(2r_(1/2))^A`, leaving `r_(1/2)^A`. A twist reverses its sign.
Thus the term makes a nonzero contribution `2r_(1/2)^A` to the
untwisted-minus-twisted expansion, without ever using (G14) or (G15).
This expansion has divided both partition functions by the same
one-plaquette vacuum factor `(exp(-beta) z(beta))^N_p`. It has not
divided by the full untwisted partition function. No bound on the
original ratio is inferred from this single term.

This refutes the stronger proposed exposure statement:

> Every center-odd winding term must encounter the distinguishing
> high-spin filter, or a positive density of incompatible pair filters.

The same example works for arbitrarily large periods, so increasing
the box size does not repair that termwise assertion.

**ARGUED, scope.** The single plane already has an area-small weight
at fixed beta. It is not an obstruction to an area bound for the whole
sum. It shows only that the new SU(2)-specific channel cannot be made
mandatory term by term. Controlling the number of low-spin surfaces,
their interactions and their scalar normalization remains essential.
This is different from the known sign obstruction: it persists even
for this single positive, unbranched surface.

## 6. What remains, and what this attempt changes

**OPEN — Wilson realization of the filters.** A usable version of
route A must construct an exact block operator from the original
Wilson integral, on its actual charged boundary space. If its proposed
factorization is `M_B=alpha_B L_B K_B R_B+E_B`, the missing estimate is

\[
 |\alpha_B|\,\|L_B\|\,\|K_B\|\,\|R_B\|
       +\|E_B\| < 1,                                \tag{G22}
\]

in one explicitly specified boundary norm, after resumming the block's
representation labels. Its scalar factor must be the one supplied by
that same integral and reference measure. It cannot be chosen after
normalizing the odd and even sectors separately. The block construction
must then give controlled repeated exposures of winding charge and
bound the accumulated boundary comparisons and scalar factors. Neither
the construction nor these estimates have been supplied here.

**PROVED / limitation.** Proposition 3 says that (G22) fails for the
bare four-strand Haar tensor with `K_B` the proposed two-filter product.
Proposition 4 says that exposure cannot be certified just by counting
strands or by requiring every winding term to meet the high-spin space.
These are two exact failures of the attempted realization. They do not
exclude (G22) after an honest block resummation. Proving such a stronger
boundary-operator estimate would be a new input, rather than another
identity for the unknown scalar deficit.

**ARGUED — decision.** The useful salvage is the explicit local
distinction (G12)–(G16), not the numerical size of a free contraction.
Low-degree Haar recoupling and the two-singlet geometry are shared with
the binary icosahedral group. A distinguishing continuous-group input
is available at higher spin, including in a center-odd space, but
singlet pairing allows charged low-spin channels to persist. Any further
attempt along A must handle those channels inside the actual Wilson
sum, not discard them. The unchanged original deficit remains the
consumer; no weaker scalar reformulation has been advertised as progress.

**READ, delivery.** The note remains an uncommitted local file on
`research/gap-tree-astra-20261112`, based on the requested pin. No PR,
commit, push, ledger edit or independent check was made by this run.

**READ / not executed.** Routes B and C remain proposals. The
pointwise Bakry–Emery obstruction and the existing (TU) work are not
repeated. Nor are the checked seed below beta=2/9, the commutator norm,
(LC), or the conditional Theorem R. The present operator `7/12` is not
an improved Wilson seed. There was no numerical run and no independent
check of this note. A future check can focus on (G7)–(G20) and the
distinction between the local tensors and a resummed normalized block.

**READ, source and search limits.** The SA source intervals used are
outline 2195–2281 and 31860–31884, and CA-I 2700–2716, whose Theorem 0
scope explicitly excludes a mass gap. Index lookups preceded the
outline reads; the 4.12–4.19 index supplied no matching filter theorem.
No Balaban PDF or OCR formula is an input. Fresh local searches for
recoupling, singlet projectors, degree-twelve moments, and icosahedral
invariants found no matching supplied lemma or other registry owner.
The corresponding main-branch moment search had three unrelated word
matches, inspected and excluded. These searches make no literature-wide
novelty claim; the group theory is elementary and is proved here for
this route. Only this assigned output file was written in the checkout.

RESULT: OPEN — a two-filter contraction and a higher-spin charged filter that distinguishes SU(2) from both comparison groups are proved by hand; free insertion of the filters and mandatory high-spin exposure are refuted for the stated Wilson tensors and winding terms. The missing input is a resummed Wilson-block comparison satisfying (G22), with its scalar cost and repeated-exposure control at the original normalization; (FQ) and (V) remain unproved.
