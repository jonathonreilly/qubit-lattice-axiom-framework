# Repo search

The task-specific prior note is absent at the supplied pin. The November 8
repo-search digest concerns older ultraviolet targets, not KIN or the
checkerboard models. Its closest pointer, checked on PR 10114, is the
transfer-kernel positivity argument in `MASS_GAP_LOCAL_BLOCK_ASTRA.md`:
an existing input, not the cut reduction. Targeted searches of main and
PRs 10114, 10133, 10134, 10141 and 10144 found no duplicate of KIN or
the checkerboard factorization. Other close hits and limits are in test 6.

Writer: OpenAI / GPT-6 Astra / xhigh, row 1079. Source revision:
`51b7908da6e7f0e024cc9e38298b245c2b26296f`. Cross-provider research check of
Claude Fable 5.2 max's row 1076, not an audit. No status or mass gap is claimed.
This checks K1 only. It does not undertake P1/P2, verify the five GUIDE runs,
formalize anything in Lean, or check the entire posted O(4) proof.

## Checkpoint

- Source: `library/gap-bridge-vectors-max.md`, 499 lines, read in full.
- First six tests, in order: rotations; injectivity; Q8; Haar integral;
  primary O(4) estimate; branch overlap.
- Then the remaining K1 statements and the scoped FAILS verdicts.
- All mathematical decisions use written arguments, not computed spectra.
- Download directory: `/tmp/sa-gap-bridge-vectors-check-astra.zdORYI`.
  The outline and CA-I at `31a47c543775` were each fetched once.
- Completed: all six tests, then every named K1 statement and each step-5
  FAILS verdict. Corrections below do not edit row 1076 or grant standing.
- Next decision belongs to the lead: apply the corrections before using
  KIN-4, the checkerboard boundary statement or either downstream brief.
  The Wilson/heat comparison and singlet mixing remain open.

## Six tests, in the requested order

### 1. Rotations and commuting cut averages — HOLDS

Use the convention actually used in the proof: `rho_c(W)h(Phi)=h(w_c(W)Phi)`.
This is a pullback, hence an anti-representation. In one column,

\[
 (\rho_{n-1}(V_{n-1})\cdots\rho_1(V_1)h)(\Phi)
 =h(w_1(V_1)\cdots w_{n-1}(V_{n-1})\Phi).
\]

At site `k'` the product on the right is `V_1 ... V_(k'-1)`.
It is precisely the tree gauge `g_V`, in that order. No commuting of the
rotations was used. Rotations at different columns commute even when they
meet a link: they act by left and right multiplication.

For nested cuts at the same column write `J_c=J_A+J_d`, where A and d are
disjoint sets of sites. The Casimir of `J_d` commutes with every component
of `J_d` and with `J_A`. Thus `[C_c,C_d]=0`. To make this an operator
statement rather than only a formal commutator, decompose the finite-link
space into its finite-dimensional Peter–Weyl blocks. Each block is invariant
under every site rotation. The Casimirs are commuting self-adjoint matrices
there; their spectral projections therefore commute on the Hilbert direct
sum. Central averaging is scalar on each irreducible cut representation.
It follows that the bounded operators `M_c` strongly commute. The
anti-representation convention changes neither the Casimir nor its scalar
average, since the SU(2) weights and characters are inversion invariant.

K_Phi is scalar on each individual-link representation and commutes with
both endpoint actions. This proves all commuting claims needed in KIN(c).
The order in source line 317 is correct.

### 2. Injectivity and positivity in KIN-4 — HOLDS AFTER CORRECTION

For `b=beta_M>0`, the single-link Wilson convolution eigenvalue is
`I_(2j+1)(b)/I_1(b)`. Every term of the defining power series of `I_m(b)`
is positive. Thus every eigenvalue is positive. A finite tensor product of
these convolutions is injective, even though its inverse is unbounded.
Peter–Weyl expansion proves this without asserting a bounded inverse.

Write `E=exp(-V_f/2)`. The kernel of `E K_Phi E` is continuous and strictly
positive on the compact configuration space. Its top eigenvector Omega
can be chosen continuous and strictly positive: the positive integral
operator sends each nonzero nonnegative vector to a strictly positive
continuous function; compactness and the usual extremal-eigenvector argument
give simplicity. Uniqueness makes Omega G-invariant. Consequently
`chi=K_Phi E Omega=lambda_0 E^(-1) Omega` is continuous and strictly positive.
Subtracting the rotated equations and using injectivity is valid. It forces
`exp(-V_f)=exp(-V_f o w)` everywhere, first almost everywhere and then by
continuity and full support of Haar measure.

At the all-identity configuration the change in V_f is exactly
`beta_M d_x (1-tr(W)/2)`. All incident mixed plaquettes have the same sign
in this difference. Transverse plaquettes are unchanged by the site gauge
rotation. Choosing one column with `d_x>0` supplies the contradiction.

For nontrivial spin j the inequality `chi_j/(2j+1)<1` holds on a
nonempty open set, which suffices for `lambda_j<1` against a strictly
positive weight. It need not hold at every nonidentity element: integer
spins also equal their dimension at -1. This corrects the parenthesis
in line 329 without changing the invariant-subspace argument.

**First failing assertion without a domain repair:** source line 329 says
`d_x >= 1`. A finite transverse rectangle can be a singleton. Then there
are no transverse links, K is one-dimensional, `V_f=0`, and `D=1` on K.
The claimed strict inequality is false. Replace the lemma's opening by:

> Assume the transverse graph has at least one edge, n >= 2, beta_M > 0,
> and finite beta_L (or heat time t > 0). Then D S Omega != S Omega,
> and lambda_0(beta_L) < lambda_0(infinity).

For the strict conclusion, suppose equality of the two top eigenvalues.
A maximizing eigenvector of `S* D S` must also maximize `S* S`, since
`0 <= S* D S <= S* S`. Simplicity identifies it with Omega, and equality
of its Rayleigh quotients implies `(1-D)^(1/2) S Omega=0`, contrary to
the preceding argument. This fills the final strictness step.

### 3. Q8 matrix and both asymptotic expansions — HOLDS AFTER CORRECTION

The Wilson endpoint counterexample HOLDS. Here is a derivation directly
from the character table, with no numerical eigenvalues. The conjugacy
classes have sizes `1,1,2,2,2`. In that order the five character rows are

\[
\begin{array}{c|rrrrr}
1&1&1&1&1&1\\
\sigma_i&1&1&1&-1&-1\\
\sigma_j&1&1&-1&1&-1\\
\sigma_k&1&1&-1&-1&1\\
\tau&2&-2&0&0&0
\end{array}
\]

The normalized indicator basis converts a character's value on a class C
to `sqrt(|C|/8) chi(C)`. Summing its rank-one projection with weights
`1,A,A,A,B` gives the displayed entries in the source, and also

\[
K_{11}=K_{00},\quad K_{01}=(1+3A-4B)/8,\quad K_{1a}=K_{0a}.
\]

The two differences of noncentral class indicators have eigenvalue A.
The remaining subspace is spanned by `e_0,e_1,f`. Thus after multiplication
by `diag(1,eps^2,eps,eps,eps)`, two eigenvalues are exactly `eps^2 A`.
Eliminating the e_0 coordinate in the three-dimensional block at an
eigenvalue `z=eps^2 y` gives, in the e_1,f coordinates, diagonal orders
`eps^4,eps^2` and off-diagonal order `eps^3`. The coefficient of the
second diagonal entry is

\[
F=K_{ff}-K_{0f}^{\,2}/K_{00}.
\]

For fixed `beta_L>0`, K is positive definite, so `K_00>0` and `F>0`.
The reduced characteristic polynomial divided by its leading power of
eps tends to `y(y-F)`. Hence the scaled top eigenvalue tends to K_00,
and the next eigenvalue divided by eps^2 tends to `max(F,A)`.
Analyticity of the entries in eps gives the source's stated error bounds;
only the limits are needed. The same calculation at `beta_L=infinity`
has `A,B -> 1`, so its gap is `beta_M+o(1)`.

Put `eta=exp(-beta_L)` and `d=1+6 eta+eta^2`. Directly from the table,

\[
A_L={(1-\eta)^4\over d^2}=1-16\eta+O(\eta^2),\qquad
B_L={(1-\eta^2)^2\over d^2}=1-12\eta+O(\eta^2).
\]

It follows that `K_00=1-12 eta+O(eta^2)`,
`K_ff=1-4 eta+O(eta^2)`, and `K_0f^2/K_00=O(eta^2)`.
Thus `F-A=12 eta+O(eta^2)>0` for small positive eta, and

\[
\delta(\beta_L)=\log K_{00}-\log F=-8\eta+O(\eta^2)<0.
\]

These are existence arguments with explicit order of choice: choose finite
beta_L sufficiently large for the last strict sign; then choose finite
beta_M sufficiently large that its gap difference is still negative.
This proves the box counterexample to Wilson endpoint (MON-L).

**FAILS, first unsupported inference at line 404:** the sentence concluding that the
heat-kernel `(FLUX-EXC)` fails does not follow from this Wilson calculation.
Wilson's Fourier eigenvalues are not one fixed exponential semigroup in
beta_L, and a finite group has no SU(2) Casimir. Replace that sentence by:

> The Wilson endpoint inequality fails on this Q8 box. The computation
> does not identify a heat-kernel generator or prove the separate
> heat-kernel (FLUX-EXC) statement false.

**FAILS, first unsupported necessity claim at line 416:** every proof must
use continuity of the group. That assertion is also
too strong. The result rules out a proof whose hypotheses include this Q8
example. It does not specify which additional SU(2) property a proof must
use. The 2T and window claims remain GUIDE; their runs were not checked.

### 4. GH2 Haar integral and non-mixture argument — HOLDS

Normalized Haar measure on SU(2) pushes its real part x to
`(2/pi) sqrt(1-x^2) dx` on `[-1,1]`. Its even moments, from the beta
integral (or integration by parts), are

\[
\mathbb E x^{2k}={(2k)!\over4^k k!(k+1)!},\qquad
\mathbb E x^{2k+1}=0.
\]

Expansion of the exponential, justified by uniform convergence on compact
s-sets, gives

\[
\int e^{s x}\,dU=\sum_{k\ge0}{(s^2/4)^k\over k!(k+1)!}
={2I_1(s)\over s},\qquad \omega(0)=1.
\]

Quaternion norm expansion gives exactly the source's formula for s^2.
Cyclic invariance of the real part identifies its cross term with
`Re(rho_ij(u) rho_ij(u')^(-1))`; there is no conjugation error.
The multinomial expansion has nonnegative coefficients when `beta_i>=0`.

For n=2 write `F(z)=omega(sqrt(a+c z))`,
`a=beta_1^2+beta_2^2`, `c=2 beta_1 beta_2`. The displayed power series
defines F as an entire function, independently of a square-root branch.
For `c>0`, on `|z|<=R` it is bounded by
`exp(sqrt(a+cR))`. On the positive real axis, integrating over
`x>=1/2` gives `F(R)>=p exp(sqrt(a+cR)/2)` with a fixed `p>0`.
These two bounds prove entire order exactly 1/2.

More directly, suppose `F(t)=int_[0,b] exp(v t) dnu(v)` for a finite
positive measure nu. Equality on `[-1,1]` extends to entire functions.
If nu assigns positive mass to any `[epsilon,b]`, its value at R grows
at least as `nu([epsilon,b]) exp(epsilon R)`, contradicting the upper
bound. If all that mass is zero, nu is supported at 0 and F is constant,
also impossible when c>0. This proves the non-mixture claim without a
complex growth theorem. The zero-coupling constant exception is excluded.

For equal positive couplings b, differentiation gives
`d log f(t)/dt=(b/s) I_2(bs)/I_1(bs)`, `s=sqrt(2+2t)`.
At t=1 it is below b/2: `I_2(z)/I_1(z)` is the mean real part in the
strictly positive tilted Haar law, and that mean is strictly below 1.
At s=0 the expression is understood by its power-series limit.
“Haar distributed” here means that the link integration has Haar reference
measure and no L-plaquette factor; it does not mean the link is conditionally
uniform once the Higgs fields have been fixed.

### 5. CB-CH against the primary O(4) text — HOLDS AFTER CORRECTION, GIVEN (3.61)

Read the open PDF at OpenAI's commit
`4eaee87548250b2682affda7d05d947c05554bae`, pp. 13–14 and 25–30.
The requested pp. 28–30 were read, and the rendered p. 28 was inspected.
Source: [Sharp mass bounds for the two-dimensional O(4) model](https://raw.githubusercontent.com/openai/math/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf).
The copy is in `/tmp/o4-gap-bridge-vectors-check-astra.m2smwK`.
This is a check of the interface to the posted estimate, not its proof.

**Twist side.** The paper uses `Re(q_y U_e q_x^(-1))`, with fixed U_e,
and common LEFT rotations. Set `q_u=Phi_i(u)^(-1)` and
`U_(u,u')=a(u,u')^(-1)`. Then

\[
\operatorname{Re}(q_{u'}U_e q_u^{-1})
=\operatorname{Re}(\Phi_i(u)^{-1}a(u,u')\Phi_i(u')),
\]

by taking the inverse inside the real trace. The far-end action
`Phi_i -> Phi_i k` becomes `q -> k^(-1)q`. Thus the conditional sheet
has exactly the required twist convention and centering, with the other
fields fixed. The conditional independence of the Higgs species given a
is read directly from the GH2 density.

**Pins.** The paper starts with square-boundary pins, then uses pinned
coarse boundaries and collars. It does not explicitly state an arbitrary
interior finite-set pin theorem. The source's direct application after
pinning only `supp H` therefore needs justification. There is a repair
using boundary pins alone. Condition additionally on Phi_i outside a
union of coarse cells forming a neighborhood of `supp F`, contained in
its r/2 neighborhood. H is now fixed. The cell boundary is at distance
at least `r/2-C s(b)` from `supp F`. Cells meeting a free wall are padded
with zero bonds, as on p. 29. Apply the argument for (3.61) to this union.
Disconnected components and holes merely supply additional boundary seeds:
each interior star retains its full collar, the bounded-degree path count
is unchanged, and each path to any seed has the stated minimum length.
There is no change to the local estimate. The centering identity still
holds pointwise with every conditioned field fixed, since all Phi_i
variables on which F depends are inside the region.

The resulting bound is `C ||F|| ||H|| |A| exp(-c r/s(b))` after changing
absolute constants. For `r<=C s(b)` use `|E FH|<=||F||||H||` and increase
C. This removes the undefined r_0 in the source. For finite tori retain
the paper's requirement that each periodic side is at least `C s(b)`;
free boxes and their unpinned infinite-volume limits are the setting here.
Externally imposed symmetry-breaking pins near F would have to enter the
distance and are not included in this statement.

**Replacement text:**

> Given the posted charged estimate (3.61) and its cell-boundary form,
> GH2_n with free longitudinal boundary, 0<=beta_i<=b and
> 0<=beta_L<=infinity satisfies
> `|E FH| <= C ||F||_infty ||H||_infty |supp F| exp(-c r/s(b))`
> whenever the far-end average of F in one species vanishes identically.
> The estimate is uniform in the law of a. For bounded continuous local
> F,H it passes to weak limits of the free-box measures. This implication
> imports (3.61); it proves no singlet mixing.

The primary text expressly restricts its subsequent arbitrary-observable
step to untwisted ferromagnets. The conditional twisted sheet above does
not meet that restriction. The separation from (SING) is correct.

### 6. Repository overlap — no duplicate of either target found

Fetched the requested PR heads, plus #10144 named by FINISH's rule.
These are the fixed revisions searched:

| Ref | Revision |
|---|---|
| main | `8b11ae2bb95e641494fe75ed83d108ee712fa3a9` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `a2f6a430e251aa47bc3eb4f67a1dca2a88530116` |
| PR 10144 | `1f20846b8057f6346ebab6c0dbebdabbd9e472a4` |

Searched plain copies of Markdown/TeX in both YM4D science folders,
`research/ym4d/`, and docs paths containing Yang, Wilson, mass_gap, su2,
ym4, transfer or gauge. Deduplicated equal blobs: 1,828 files, about 47 MB.
`repo-manifest.json`, `repo-target-hits.txt` and `repo-method-hits.txt` in
the SA scratch directory preserve the path/ref map and full searches.
Queries included the lemma names, checkerboard, partial/total colour
charges, Casimir near cut, longitudinal electric, axial transfer and
Gauss-law/electric-energy variants. Broad word hits are locators, not a
claim of semantic exhaustiveness.

The nearest passages were opened at the fetched revisions:

| Source and range | Comparison |
|---|---|
| PR 10114, `.../ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–155` (same blob on 10133) | Already supplies the Wilson convolution, its fundamental coefficient, and a positive one-step loop witness. It does not remove longitudinal links or form nested cut Casimirs. Credit the earlier Codex/Astra work; do not count that positivity input as new. |
| main, `docs/GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md:25–40,83–118` | A supplied SU(3) Hamiltonian, static endpoint sectors and a dressed-coordinate assumption. Different operator and conclusion; no KIN identity. |
| main, `docs/HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md:43–90` | Checkerboard boson occupation in a spin-half ice model. No GH2/P4 factorization. |
| PR 10114, `.../ym4d-proof/BFT_A.md:1342–1360` | Checkerboard residual in a multiscale Gaussian norm counterexample. No checkerboard coupling family. |

The November 8 digest's other hits concern ultraviolet construction, not
these targets. No KIN/checkerboard owner was found in the pinned registry.
The separate descent-sign and literature rows do not own this K1 check.
Neither stopping condition was met. This is a bounded search result,
not a novelty theorem.

**Sussman–Alpoge source use.** Read the index README, matched chunk-02
rows 85–102 and neighboring obligation rows before the source excerpts.
SA 2195–2257 already proves the positive Bessel coefficients and product
kernel; SA 2313–2335 supplies the gauge-projected transfer representation.
Those are existing inputs, credited to Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text. The cut reduction checked
here is not in these passages. SA 588–599 separately explains why ordinary
decay alone supplies no spectral gap. The CA-I download and its
4.12–4.19 index yielded no needed target passage; no CA-I theorem is used.

## Remaining line-by-line decisions

Line numbers below refer to row 1076 at the supplied pin. The positive
gap eigenvalues are assumed to exist: finite positive beta_M, positive
beta_L or finite heat time, and a nontrivial transverse link graph.
Zero-coupling limits can have zero second eigenvalue; use extended gaps
there rather than take the logarithm of zero.

### KIN and its consequences

| Statement | Verdict and reason |
|---|---|
| KIN(a), 310,315 | HOLDS. Test 1 establishes strong commutation, including G and K_Phi. |
| KIN(b), 311,316 | HOLDS AFTER CORRECTION. Literal evaluation on the Haar-null slice a=1 is undefined for an arbitrary L2 equivalence class. Define R first on continuous invariant functions, then extend the isometry; equivalently use the inverse J defined below. |
| KIN(c), 312,317 | HOLDS with that definition of R. Test 1 checks the noncommutative order. Fubini applies to finitely many probability integrals of bounded operators; the identity extends from continuous functions by density. |
| KIN(d), 313,318 | HOLDS for the stated Wilson/heat weights. The character bound gives only `|lambda_j|<=1`; positivity comes from GL3/the heat eigenvalues, not from that bound. |
| KIN-1, 322 | HOLDS with its explicit Wilson Bessel-monotonicity premise retained. It is not a proof of that recalled premise. Heat-time monotonicity is unconditional. |
| KIN-2, 324 | HOLDS for the displayed inequality. The following claim of volume growth remains ARGUED: no additive local formula for the pressure difference is proved here. |
| KIN-3, 326 | HOLDS. Equality on Omega fixes the top eigenvalue; min–max bounds the second. |
| KIN-4, 328–330 | HOLDS AFTER CORRECTION of the no-edge case, as in test 2. |
| KIN-5, 332 | HOLDS for t>0 and simple positive eigenvalues on the stated interval. It is a heat-semigroup identity, not a Wilson-coupling identity. |
| KIN-6, 334 | HOLDS AFTER CORRECTION of the interval: take m>0 and `0<=t<=m/(a-c)`. At later times the ordered gap is `|m-t(a-c)|`. The decreasing interval alone disproves the abstract implication. |
| KIN-D, 336 | HOLDS, with boundary values defined by spectral calculus and the zero-coupling endpoint understood as a limit. |
| KIN-CVX, 338 | HOLDS whenever the two eigenvalues are positive. |

For KIN(b), define

\[
(Jh)(a,\Phi)=h(g_a\Phi),\qquad R=J^{-1}.
\]

The transformation `(a,Phi)->(a,g_a Phi)` preserves product Haar measure.
Gauge transformations trivial at the bottom vertices act transitively on
a and leave the second coordinate fixed. Their invariant L2 functions
therefore depend only on that coordinate. The remaining bottom rotations
give exactly G-invariance. This proves that J is onto H^G as well as an
isometry. It also proves the extension is independent of representatives.

For KIN-1, `0<=D<=1` gives `S*DS<=S*S`; min–max applies on the
same G-invariant space. For KIN-2 the entire inequality is
`log(lambda_0(L)/lambda_1(L)) >= log(lambda_0(L)/lambda_1(infinity))`.
KIN-3 sets `lambda_0(L)=lambda_0(infinity)` by evaluating on Omega
and applying the same order bound. No comparison of eigenvalue ratios
is inferred from min–max alone.

For KIN(d), Wilson probability concentrates at the identity as beta_L
tends to infinity: outside any identity neighborhood its continuous
character x has maximum strictly below 1, while a smaller neighborhood
has x closer to 1. Comparing the two integrals gives exponential decay
of the outside probability. Thus each normalized character integral
tends to 1. Joint spectral expansion and bounded convergence give
`D -> 1` strongly. The heat case follows directly from `exp(-tN)`.

The unrestricted phrase “real nonnegative class function” in the setting
cannot be used to infer positive convolution for other weights. For
example `w=1-epsilon chi_(1/2)`, `0<epsilon<1/2`, is positive with
integral 1, but its spin-1/2 eigenvalue is `-epsilon/2`. KIN's order
consequences are restricted to its specified positive-Fourier weights.

For KIN-5 set `Q=SS*`, `A_t=exp(-tN/2)`, so `B_t=A_t Q A_t`.
For t>0, `N^k A_t` is bounded for every integer k. A nonzero eigenvector
of B_t is in the range of A_t and hence in Dom N. Norm differentiation
on every compact t-interval in `(0,infinity)` gives

\[
B_t'=-\tfrac12(NB_t+B_tN),\qquad
\lambda_i' =\langle\phi_i,B_t'\phi_i\rangle
=-\lambda_i\langle\phi_i,N\phi_i\rangle.
\]

This proves the logarithmic derivative and `m'=n_1-n_0`.
The equal nonzero spectra follow from `X*X` and `XX*`, with `X=A_t S`.
At eigenvalue crossings the source's simple-branch argument does not
assert differentiability. No Wilson-to-heat action comparison is supplied.

For KIN-D the joint spectrum satisfies `4N=sum_c 4j_c(j_c+1)`, an integer.
For `|w|<1` the spectral-series tail is bounded by
`||S||^2 |w|^(K+1)`, establishing norm analyticity. On the unit circle
use the bounded diagonal operator `sum w^k P_k`; its strong spectral
sum is well defined. In fact S is compact, so its sandwich converges in
norm there too. Cauchy–Schwarz in the direct sum gives

\[
\left|\sum_k w^k\langle P_k Sf,P_k Sg\rangle\right|
\le\left(\sum_k|w|^k\|P_k Sf\|^2\right)^{1/2}
     \left(\sum_k|w|^k\|P_k Sg\|^2\right)^{1/2}.
\]

For KIN-CVX, Hölder's inequality proves log-convexity of each scalar
Laplace transform. Taking its supremum preserves the inequality:
`sup_f u_f(t_theta) <= (sup_f u_f(t_0))^(1-theta)
(sup_f u_f(t_1))^theta`. Replace the space by its second exterior power
and N by `N tensor 1 + 1 tensor N` to obtain the second assertion.
Both transforms decrease in t. Their difference need not do so, as
KIN-6 already shows.

**Required downstream replacement (185,346,446–447):**

> KIN expresses longitudinal descent as a cut-charge operator family.
> For the heat action, (FLUX-EXC) is equivalent to monotonicity on a
> simple-eigenvalue interval. That is stronger than comparison only with
> the face. A Wilson endpoint comparison is a separate statement;
> KIN-5 alone does not reduce it to this fixed-N sign.

### Checkerboard statements

| Statement | Verdict |
|---|---|
| CB-L, 352–358 | HOLDS in the gauge-fixed representative measure, with the shared rigid invariance of observables retained exactly as the note says. |
| CB-T, 360–361 | HOLDS AFTER CORRECTION at free transverse boundaries: components are P4 blocks **and isolated single sheets** on links belonging to no active plaquette. |
| P4-ORB, 363–365 | HOLDS for one longitudinal site. It does not classify multi-site invariants. |
| GH2-0, 367–371 | HOLDS with omega(0)=1 and the positive-coupling qualification for non-mixture, as in test 4. |
| CB-CH, 373–375 | HOLDS AFTER CORRECTION, GIVEN the posted (3.61), as in test 5. |

For CB-L, tree gauge fixing on each frozen, simply connected longitudinal
plane makes every longitudinal link 1. Haar change of variables preserves
the link measures. At beta_T=0, every remaining term involves exactly one
sheet and its unfrozen endpoint planes. The factor graph in the statement
therefore has disjoint variable sets across its components, including their
normalizing constants. On the even-frozen square lattice each link has
exactly one odd endpoint. Taking inverses on incoming sheets and using
`Re U=Re U^(-1)` gives the displayed GH2 action. Shared rigid groups
constrain observable invariance, not this factorization of the density.

For CB-T, different black squares share no links. The product density
factorizes over their four-link sets. But a boundary link adjacent only
to a white square is in no black-square set. Its mixed action remains
one independent O(4) sheet. A rectangle consisting of one white square
already disproves “each component is P4” at line 360. Replace it by:

> Every component containing an active plaquette is P4. Each link
> incident to no active plaquette is an independent single sheet.
> On the infinite checkerboard, every link belongs to one P4 block.

For P4-ORB take `g_1=1`, `g_2=Phi_1`, `g_3=Phi_1 Phi_2`,
`g_4=Phi_1 Phi_2 Phi_3^(-1)`. The four transformed links are
`1,1,1,H^(-1)`. Residual transformations conjugate H. Two SU(2)
elements are conjugate exactly when their traces agree, completing
both directions of the orbit classification.

### SWAP, LOCK and the quadratic FLAT calculation

**SWAP (190): HOLDS.** For a coupling variation v, the second derivative
of `log Z(beta+t v)` is the variance of `v dot X`, which is nonnegative.
The coordinate permutation preserves Haar measure and the equal-sided
box and interchanges L and T. Applying convexity at the midpoint of the
two exchanged couplings proves the inequality. It passes to any common
pointwise subsequential limit of pressures.

**LOCK (220): HOLDS on each fixed finite box.** For every ordinary link
write the layers as a base link and N-1 successive relative group elements.
Product Haar measure is preserved. The normalized locking weight is a
product of approximate identities in these relative elements. Concentration
at their identities follows from the same compact maximum comparison
used for KIN(d). The remaining finite Wilson density is bounded, positive
and continuous. Its integrals therefore converge to their diagonal values,
including the nonzero denominator. On that diagonal the N plaquette
actions add to coupling Nb. At beta_5=0 product Haar and the separate
actions give independent copies. Free fifth-direction ends remove every
fifth-link variable by tree gauge; no fifth holonomy remains. This proves
finite-volume weak convergence, with no uniform clustering estimate.

**FLAT algebra (342): HOLDS AFTER CORRECTION.** Use lattice momenta
`p_mu=2 sin(k_mu/2)` in midpoint Fourier convention, or explicitly take
the continuum quadratic approximation if using k_mu itself. For each
colour the quadratic action is

\[
Q=\tfrac{\beta_L}{2}|p_0A_1-p_1A_0|^2
 +\tfrac{\beta_M}{2}\sum_{i=0,1;\,\mu=2,3}|p_iA_\mu-p_\mu A_i|^2
 +\tfrac{\beta_T}{2}|p_2A_3-p_3A_2|^2.
\]

For `kappa=|(p_2,p_3)|>0`, decompose a into its parallel/perpendicular
parts and put `B_i=A_i-(p_i/kappa)a_parallel`. Orthogonal decomposition
then gives exactly

\[
Q=\tfrac12[\beta_M(p_0^2+p_1^2)+\beta_T\kappa^2]|a_\perp|^2
 +\tfrac{\beta_M\kappa^2}{2}(|B_0|^2+|B_1|^2)
 +\tfrac{\beta_L}{2}|p_0B_1-p_1B_0|^2.
\]

Thus the two displayed mass-squared ratios are correct for positive
beta_L,beta_M. At kappa=0 the parallel decomposition is undefined: both
A_2,A_3 have the two-dimensional kinetic term and F_23 vanishes.
For kappa>0 the plaquette curvature is proportional to `kappa a_perp`,
not a_perp itself. This colour component is invariant under the linearized
gradient gauge transformations; it is not a gauge-invariant SU(2) scalar
observable. Replace that identification at line 342 accordingly.
The claimed nonperturbative size and location of a gap increase remain
beliefs. The quadratic calculation proves neither.

## Step 5: check of every FAILS verdict

Here “the verdict holds” can mean only that the written proposal supplies
no bridge. Failure to supply an estimate does not refute that estimate.
The following table preserves that distinction.

| Vector | Check verdict | Exact disposition |
|---|---|---|
| VB-1, 163–170 | HOLDS AFTER CORRECTION | The zero-free transport method is prior work; no dominance estimate is supplied. But spectral dominance is not literally the partition-zero condition of Route Z. Use the distinction below. |
| VB-2, 172–177 | HOLDS | No implication from the displayed flux ratio to the whole observable clustering target is supplied. This is a missing consumer, not a proof that none can exist. |
| VB-3, 179–186 | HOLDS AFTER CORRECTION | The heat-time sign is a restatement of heat-time monotonicity on simple branches. It is not equivalent to the weaker endpoint comparison, nor to the Wilson comparison. The Wilson Q8 endpoint failure holds; see tests 2–3 for the other corrections. |
| VB-4, 188–192 | HOLDS AFTER CORRECTION | SWAP holds and supplies no spectral ratio bound. The explanation claiming symmetry of the fixed-direction gap fails at 192; replace it as below. |
| VB-5, 194–197 | HOLDS AFTER CORRECTION | The chi-square bound is a stronger sufficient clustering input. Equivalence and the claimed ordinary replica-gluing formula are not established. The proposal supplies no estimate for this stronger quantity. |
| VB-6, 199–202 | HOLDS | KIN-CVX is true; a difference of its convex functions has no forced derivative sign. KIN-6 is an explicit check of that failure. |
| VB-7, 204–207 | HOLDS as a bounded search report | No comparison inequality is provided by the listed proposals. This is not a no-go theorem for correlation inequalities. The recalled literature families were not independently surveyed here. |
| VB-8, 209–211 | HOLDS at the stated scope | The specific half-plane Lee–Yang proposal is already refuted by LYP/LYP2. Neither those results nor this check refutes all Higgs paths or every tube about the real axis. |
| VB-9, 213–216 | HOLDS as “no completed reduction” | The adjoint carry is missing. A centre-only start need not kill a path whose later step uses SU(2). The proposed path itself is OPEN; the recalled K7 line is not a proved obstruction to it. |
| VB-10, 218–222 | HOLDS AFTER CORRECTION | LAYER includes the clustering endpoint, so no weaker sufficient input was produced. LOCK gives only finite-volume convergence. The Wilson/Villain test at 222 is not a valid theorem-grade refutation. |
| VB-12, 234–236 | HOLDS as “no completed reduction” | A solvable beta_M=0 start is not the missing quantitative carry to beta_M=beta. No such carry is supplied or refuted here. |
| VB-14, 242–245 | HOLDS AFTER CORRECTION | A tail theorem with matched observables, prefactors and a common positive physical rate would supply a continuum input. It is not proved to be logically stronger than a fixed-window lattice theorem. The latter does not concern the tail. The theorem-grade U(1) test also needs the matching action. |
| VB-16, 251–254 | HOLDS as “not a supplied route” | Conditional sheet geometry alone does not prove mixing of the joint law. No contraction estimate is provided. |

VB-13 and VB-15 are called “Found”/“No vector” in step 5, not FAILS.
The later summary at 471 should retain those labels rather than turn
prior occurrence into a mathematical refutation. VB-11 and VB-18 remain
test settings with their carries open, as the source says.

### Corrections that change an argument

**VB-1, first failing identification at 168–170.** Route ZB in
`gap-zero-transport.md:85–105` asks for nonzero `Tr(T(z)^k)` throughout
one domain for every sufficiently large k. Dominance alone is different.
For example `T(z)=diag(1,z,z)` has one simple eigenvalue of strictly
largest modulus throughout `|z|<1`, but `Tr T(z)^k=1+2z^k` has zeros
inside that disc for every k. This is finite algebra, not a numerical
test. Replace “the open statement is Z6 in another variable” by:

> This reuses Route Z's complex transport strategy, with an unproved
> spectral-dominance input. No equivalence with its partition-zero
> hypothesis has been shown.

The known corrections of Route ZB's domain geometry are not rechecked
here; they are not needed for this distinction.

**VB-4, first failing inference at 192.** Pair exchange maps the
direction-0 transfer problem at `(beta_L,beta_M,beta_T)` to the
direction-2 problem at `(beta_T,beta_M,beta_L)`. It does not assert
`m_0(beta_L,beta_M,beta_T)=m_0(beta_T,beta_M,beta_L)`.
Also, KIN-CVX concerns heat time, not the SWAP line in Wilson couplings.
Replace that explanation by:

> Pressure convexity and pair exchange give no estimate of the
> excited-to-ground eigenvalue ratio. The exchange also changes the
> transfer direction. No gap comparison follows from SWAP alone.

**VB-5, first unsupported formula at 196.** Let
`h=dmu_AB/d(mu_A tensor mu_B)`. For centered L2 functions f,g,

\[
|\mathbb E(fg)|
=\left|\int(h-1)f g\,d\mu_A d\mu_B\right|
\le\sqrt{\chi^2}\,\|f\|_2\|g\|_2.
\]

If `I_2<=C exp(-mr)`, then
`chi^2=exp(I_2)-1<=C exp(C) exp(-mr)`. The resulting covariance rate
is m/2, with the displayed prefactor. When the conditional expectation
operator is Hilbert–Schmidt, chi-square is the sum of the squared
singular values on the centered spaces. This proves sufficiency, not
equivalence to bounded-local-observable clustering.

With densities p relative to product reference measures the exact
replica expression is `int p_AB^2/(p_A p_B)`. Ordinary double-copy
gluing instead gives collision integrals and does not create these
pointwise reciprocal marginals. For the binary joint law
`[[1/2,1/4],[0,1/4]]`, the former is 4/3, whereas the usual collision
ratio `sum p_AB^2 / [(sum p_A^2)(sum p_B^2)]` is 6/5. Thus the claim
that this simply amounts to coupling 2 beta on the glued set has not
been derived. Replacement:

> An exponentially small chi-square information would suffice, with
> half its exponent, for normalized L2 correlation decay. This is a
> stronger unproved input, not an established equivalent reformulation.
> No replica formula with only doubled local couplings is supplied.

**VB-8, source scope.** Read `gap-outside-box-max.md:236–295`.
LYP's SU(2) character series has positive fourth powers on the imaginary
axis and a nonconstant even entire partition function of exponential
type. Its zero-free-entire alternative would force a constant by
Borel–Carathéodory and Cauchy estimates. This is the already-written
one-plaquette refutation of the half-plane hypothesis. LYP2 extends
that particular obstruction at small coupling. Its own text expressly
does not rule out a narrower zero-free tube. Credit row 1004; this check
does not claim a new Lee–Yang result.

**VB-9/10/12/14, common scope repair.** A group-blind starting estimate
does not disqualify a proof whose subsequent carry is selective. No such
carry is supplied in these proposals. That is the justified stopping
verdict. In particular, LOCK multiplies Wilson weights:
`[exp(b cos theta)]^N=exp(Nb cos theta)`. It does not produce a Villain
weight. A Coulomb theorem for a Villain endpoint cannot refute that
Wilson family without a comparison theorem. Nor does “all large beta”
by itself supply that action matching. Replace the theorem-grade
applications at 222 and 245 by:

> A group-blind carry whose verified class includes the massless
> Villain endpoint would fail there. For the Wilson families written
> here, this is a comparison constraint or belief, not that theorem's
> direct counterexample.

The common-physical-rate and observable-matching qualification for
VB-14 is also required by `gap-aniso-check-astra.md:180` and the
fixed-window warning in `gap-finishline-opus.md:198–199`. A fixed
coupling alone does not supply the cutoff carry.

## Scope and delivery record

This checks every K1 item in the pinned row 1076, line by line. The
mathematical paths include the character-table reconstruction, Haar moments,
joint finite-dimensional representation blocks and the primary PDF's twist
convention. No numerical spectrum, machine enumeration or formal checker
discharges a step. No new attack was undertaken.

Not covered: the five GUIDE runs, a fresh literature survey, the full
O(4) proof behind (3.61), the separate (TM) premise, Wilson Bessel-ratio
monotonicity, Orland's papers, Balaban's papers, Remark TOR, Remark RATE,
or a proof of (FLUX-EXC), (SING), either full mixing conjecture, or a
continuum mass gap. The Q8 conclusion is finite-box and Wilson only.
The posted O(4) theorem remains an imported premise here.

Source SHA-256:
`9740149dd10b4ce5e594831a08f984fde881dd8894903d9f72c9d3e0c796cfa9`.
The source was compared byte-for-byte with `51b7908da` and is unchanged.
Only this output file was written in the checkout. No registry, FINISH,
audit record or other author's source was edited. Work is local on
`check/gap-bridge-vectors-astra-51b7908da`, uncommitted and unpushed.
No external post was authorized or made.

RESULT: Row 1079, GPT-6 Astra xhigh: K1 checked; the core KIN operator identities, SWAP, LOCK, GH2-0 and the finite-box Wilson Q8 counterexample hold with the stated domain and boundary repairs; CB-CH holds after the conditioning repair GIVEN OpenAI's (3.61); the Wilson-to-heat inference, mandatory-continuity claim, spectral-dominance/zero-free identification, fixed-direction gap symmetry and ordinary chi-square replica formula fail as written; the remaining kill verdicts hold only at their corrected scopes; no mass gap or status is claimed, and (W) does not move.
