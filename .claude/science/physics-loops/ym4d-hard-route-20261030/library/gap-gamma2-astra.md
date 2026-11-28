# Repo search

**READ.** This lane is pinned at `cddbe1345d102c225e5e98be8556842e4caad413`.
`prior/gap-gamma2-astra.md` is absent. The lead's November 8 digest
concerns earlier RG targets. Its relevant screening hits are the periodic
finite-clock Villain covariance note on main and a one-step transfer
witness on PR 10114. Neither states the proposed Wilson SU(2) curvature
bound. The closer source is `gap-tu-retry.md`, which already proves the
circle locality bridge and states the Villain obstruction. They are reused.

**READ.** Searches of `open-registry.md`, `open-core.md`, and `l17c.md`
located no competing owner for this integrated-curvature target. Row 812
assigns it here; row 813 owns its literature search. No work on the joint
surface resummation of row 811 is attempted.

**READ.** Main and PRs 10114, 10133, 10134 and 10141 were fetched for a
targeted curvature search. Their heads were respectively `bb4ec020d`,
`f76f6c649`, `89faef229`, `1e70c7211`, and `fb99b4ddd`.
The query was `Bakry|Bochner|Langevin|integrated curvature|Hessian.square`,
on Markdown and TeX outside this lane. Complete output and full hashes
are in `/tmp/sa-gap-gamma2-astra.CcLzXy/repo-search.json` and its companion
search logs. Broad Bochner hits include unrelated integration theorems;
the mathematical scope checks used these bounded primary passages:

| READ: source and lines | Closeness to this target |
|---|---|
| Main, `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:1–100` | Finite-clock covariance and observable masslessness. This is the earlier Fröhlich–Spencer-method input behind the reused U(1) theorem, not a Wilson SU(2) bound. |
| Main, `docs/HYBRID_GENERATORS_INTEGRATED_RATES_AND_CURVATURE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md:1–135` | A different clock hybrid generator. Its pointwise-curvature test explicitly leaves integrated estimates separate. |
| PR 10114, `S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166` | Positive one-step loop correlation, with its exterior normalizer retained. It gives no uniform gap. |
| PR 10114, `S/checks/review_massgap_block_literature.md:26–43` | Existing primary-source reading of Shen–Zhu–Zhu: strong-coupling functional inequalities, with Wilson normalization `beta<1/12` for SU(2). This record is reused as literature context, not an imported proof. |
| PR 10114, `S/LCONV55.md:176–207`, `S/NODEA_RES55.md:258–287` | Pointwise/chart Hessian obstructions and missing convexity hypotheses for other RG measures. Their machine certificates are not used. Neither passage proves (G2). |

Here `S/` is `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
The PR 10133 search repeats those soft-route locators. No new source read
from PRs 10134 or 10141 supplies this target. These are bounded search
findings, not an exhaustive absence theorem. The local input closest to
a positive result is the already checked chord estimate in
`gap-vmf-lip.md`; section 3 reuses it without repeating its proof.

# Integrated curvature for the Wilson link diffusion

Proof item, FINISH row 812. Author: **Codex gpt-6-astra max**.
Research text, not an audit; this grants no status.
**READ** reports a source; **PROVED** means a hand argument in this note,
not an independent check; **ARGUED** marks an inference;
**GUIDE** marks a proposed test; **OPEN** marks a missing assertion.

**READ.** The requested GOAL and FINISH passages and the corrected route B
were read first. Credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text, for the outline/account scope statements.
Their files at `31a47c543775` were each downloaded once into the fresh
directory `/tmp/sa-gap-gamma2-astra.CcLzXy/`.
The index led to outline 9536–9577 and 31860–31884. The former proves
constrained classical decay, explicitly “not a physical Yang--Mills mass
gap.” The latter proves that polynomial decay does not exclude spectral
support near zero. These are proved scope limitations, not a sketch of
(G2). CA-I 47617–47635 concerns
coercivity at a trivial prepared background, not the Gibbs diffusion.
No theorem from those passages supplies (G2).

## Checkpoint

**OPEN, final checkpoint, 2026-11-12.** The order-one estimate is not
established. The source pin is unchanged. Sections 1–4 give the
equivalence, the beta-below-2/9 result, and the locality bridge.
Section 5 records the failed pointwise route, the sharp failure of
worst-exterior chord contraction, and the two test-function probes.
The next decision is how to estimate the joint form (27), or construct
a collective slow-mode family. No numerical proof step, audit, or status
change is used. Only this output file was written in the checkout;
it remains local and uncommitted on `research/gap-gamma2-astra-cddbe1345`.

## 1. The precise statement and the spectral consequence

**PROVED — conventions and Bochner identity.** Let
`Lambda = product_(mu=1)^4 Z/n_mu Z`, with `n_mu >= 2`.
Keep one positively oriented link variable per bond and one plaquette
per `(x,mu,nu)`, `mu<nu`. The configuration manifold is
`M_Lambda=(S^3)^E`, with the unit round metric on each factor.
Normalized sphere volume is Haar measure. Put

\[
 q_p=\tfrac12\operatorname{tr}U_p,\quad
 S_\beta=\beta\sum_p(1-q_p),\quad
 d\mu_\beta=Z_\beta^{-1}e^{-S_\beta}\prod_e d\sigma(U_e),\quad
 L_\beta=-\Delta+\langle\nabla S_\beta,\nabla\cdot\rangle.
 \tag{1}
\]

The generator has positive sign: `P_t=exp(-t L_beta)` is the diffusion
semigroup. Gauge transformations act by isometries and preserve the law.
Thus the closed subspace of gauge-invariant functions reduces `L_beta`.
All test functions below are real and smooth. Define

\[
 E(f)=\mu_\beta(|\nabla f|^2),\quad
 H(f)=\mu_\beta(\|\nabla^2 f\|_{\rm HS}^2),\quad
 C(f)=\mu_\beta(\nabla^2 S_\beta(\nabla f,\nabla f)),\quad
 Q(f)=\mu_\beta((L_\beta f)^2).
 \tag{2}
\]

The Hessian includes every mixed pair of links, with ordered pairs in
its Hilbert–Schmidt norm. Each sphere has Ricci tensor `2g`; the product
has Ricci tensor `2g_product`, not `2|E|g_product`.
The weighted Bochner identity is

\[
                         Q=H+2E+C.                    \tag{3}
\]

Indeed the scalar identity for `A=-L_beta` is
`A|grad f|^2/2 - <grad f,grad Af>
= ||Hess f||^2 + (Ric+Hess S_beta)(grad f,grad f)`.
It follows in a normal orthonormal frame by differentiating twice;
commuting the two covariant derivatives of `df` gives `Ric`.
Integrate against `mu_beta`. The first term integrates to zero.
Weighted integration by parts gives
`-mu(<grad f,grad Af>)=mu((Af)^2)`, proving (3).

**OPEN — the target (G2), with its quantifiers.** Fix a compact interval
`I=[b_-,b_+]` with `0<b_-<=b_+<infinity`. There should exist constants
`0<=theta<1` and `kappa>0`, independent of the periods and beta, such that
every gauge-invariant smooth `f` satisfies

\[
 C(f)\ge-\theta H(f)-(2-\kappa)E(f),
 \qquad \beta\in I.                                  \tag{G2}
\]

Allowing negative theta would only strengthen the requirement; replacing
it by zero loses no existence assertion. The inequalities here concern
the full periodic Wilson probability law, without a gauge slice or a
small-field restriction. A center-twisted version replaces `q_p` by
`epsilon_p q_p`, with fixed `epsilon_p in {+1,-1}`, and is a separate
uniformity requirement at order one.

**PROVED — spectral implication.** From (3), (G2) is exactly

\[
                   Q\ge(1-\theta)H+\kappa E.           \tag{4}
\]

On each finite product, `L_beta` is elliptic, symmetric and nonnegative.
Its kernel consists of constants: integration by parts gives `E(f)=0`
for a kernel element, and the manifold is connected. Compactness gives
discrete spectrum and smooth eigenfunctions. These statements also hold
on its invariant subspace, by the commuting gauge projection.
For a nonconstant invariant eigenfunction `Lf=lambda f`,
`Q=lambda E`, so (4) gives `lambda>=kappa`. Expanding a centered
invariant function in that eigenbasis proves

\[
 \operatorname{Var}_{\mu_\beta} f\le\kappa^{-1}E(f),\qquad
 \gamma_{\rm inv}(\beta,\Lambda)\ge\kappa.              \tag{5}
\]

This is the gap of an auxiliary diffusion. It is not the transfer
Hamiltonian by definition. Section 4 supplies the decay bridge.
The metric in `gap-ac-lat.md` is four times this one, so its Laplacian,
gap and Ricci endomorphism are one quarter of the present values.

## 2. Bounded Hessians make (G2) equivalent to a uniform gap

**PROVED — the Wilson Hessian bound.** For one plaquette and a product
geodesic with link velocities `v_e`, multilinearity of quaternion
multiplication gives

\[
 |\nabla^2(1-q_p)(v,v)|
 \le \sum_{e\in p}|v_e|^2+
                  2\sum_{e<e'\in p}|v_e||v_{e'}|
 \le4\sum_{e\in p}|v_e|^2.
 \tag{6}
\]

A diagonal derivative is `q_p |v_e|^2`, since a unit-sphere geodesic
has ambient acceleration `-|v_e|^2 U_e`. Each mixed derivative is the
real part of a product containing the two tangent insertions. The norm
of that product is `|v_e||v_e'|`. Inversion is an isometry and changes
none of these bounds. There are six plaquette occurrences at each link.
Consequently, including arbitrary fixed center signs,

\[
                -24\beta g\preceq\nabla^2S_\beta
                         \preceq24\beta g.             \tag{7}
\]

Multiplicity counts also cover periods two. No plaquette repeats a link
variable when every period is at least two.

**PROVED — equivalence.** Suppose instead that the invariant gap is
at least `lambda_*>0` on all the volumes and couplings in `I`.
The spectral expansion gives `Q>=lambda_* E`. Equations (3) and (7)
give `Q>=H-24 b_+ E`, where dropping the positive `2E` is harmless.
Set

\[
 \delta=\frac{\lambda_*}{2(\lambda_*+24b_+)},\qquad
 \theta=1-\delta,\qquad \kappa=\lambda_*/2.
 \tag{8}
\]

Take `delta` times the second lower bound and `1-delta` times the first.
This gives
`Q >= delta H + ((1-delta)lambda_*-24b_+delta) E
= delta H + (lambda_*/2)E`, exactly (4).
Together with (5), this proves the equivalence of the two existence
statements, with constants uniform in volume and beta.

**PROVED — what a counterexample would need.** A single fixed torus
always has some positive invariant gap, hence some constants in (G2).
On a compact beta interval its density has positive upper and lower
bounds uniform in beta. Comparison with the Haar Poincare inequality
therefore also makes that fixed-volume gap uniform on the interval.
Thus a finite-volume test cannot refute the existential statement with
unspecified theta and kappa. A refutation on `I` requires a sequence
`(Lambda_j,beta_j)` with `beta_j in I` and invariant Rayleigh quotients
tending to zero. Fixed constants can, of course, be tested at one volume.

**ARGUED.** The integrated criterion can outperform pointwise curvature.
But, on this compact coupling interval, asserting the existence of its
constants has exactly the content of the uniform diffusion gap.
The new proof input must be an estimate that establishes those constants.
Writing (G2) alone does not supply such an estimate or continue them in beta.

## 3. A hand proof in the existing strong-coupling range

### 3.1 A conditional sphere identity

**PROVED.** For any `h in R^4`, let `dnu_h` on the unit sphere be
proportional to `exp(h.x) d sigma(x)`. Its potential is `V=-h.x`.
For any smooth `u`, put `a=grad V`, `v=grad u`, `T=Hess u`.
The identities `Hess V=(h.x)g` and `Delta V=3h.x` give

\[
 3\nu_h(\nabla^2V(v,v))
 =\nu_h(|a|^2|v|^2-2T(a,v))
 =\nu_h(\|T-a\otimes v\|^2-\|T\|^2).
 \tag{9}
\]

For the first equality integrate the divergence of
`exp(-V)|grad u|^2 grad V` on the closed sphere. The second is the
expansion of a tensor square; symmetry of `a tensor v` is unnecessary.
In particular

\[
 \nu_h(\nabla^2V(\nabla u,\nabla u))
       \ge-\tfrac13\nu_h(\|\nabla^2u\|^2),\qquad
 \operatorname{Var}_{\nu_h}u\le\tfrac12\nu_h(|\nabla u|^2).
 \tag{10}
\]

For the second assertion use the sphere Bochner identity and (9), giving
`nu_h((L_h u)^2)>= (2/3)nu_h(||Hess u||^2)+2nu_h(|grad u|^2)`.
The finite-dimensional spectral argument of section 1 gives the gap two.
This estimate is uniform in the field `h`; no lower bound on a density
over the whole lattice has been used.

Conditioning Wilson's law on all links except `e` gives exactly `nu_h`,
where `h` is beta times the sum of six unit staples. Thus (10) applies
with every exterior configuration and also with center signs.

**PROVED — direct integrated gain.** Write `H=H_d+H_m`, for the diagonal
and mixed Hessian blocks, and split `C=C_d+C_m` similarly.
Equation (9), conditionally in each link, gives `C_d>=-H_d/3`.
Each off-diagonal Hessian block contributed by one plaquette has operator
norm at most beta. Its absolute block row sum is at most `18 beta`.
Using `2xy<=x^2+y^2` gives

\[
 Q\ge\tfrac23H_d+H_m+(2-18\beta)E
     \ge\tfrac23H+(2-18\beta)E.                        \tag{11}
\]

Hence (G2) holds with `theta=1/3`, `kappa=2-18b_+` when `b_+<1/9`.
Unlike the pointwise test, this uses a square that pays for negative
single-link curvature at arbitrarily large conditional field strength.

### 3.2 Reuse the existing chord influence, then compare generators

**READ — prior input, not re-derived.** `gap-vmf-lip.md` Theorem V and
section 2, especially (7), (9), (10), and Lemma INF (13), prove

\[
 d_{\rm Lip}(\nu_h,\nu_{h'})\le|h-h'|/4,\qquad
 C_{ee'}\le\beta n_{ee'}/4,\qquad
 \max_e\sum_{e'}C_{ee'}\le\alpha:=9\beta/2.             \tag{12}
\]

Here `n_ee'` counts shared plaquettes. The source treats periods at least
three, where that multiplicity is at most one. For period two, the same
telescoping staple estimate sums the occurrences; the row count remains
18. This is the only extension of that input made here.
Credit its Codex author, Claude Opus 5.5's check in
`gap-vmf-lip-check-opus.md` sections 1–4, and Dobrushin's method.
The input already gives a twist seed for beta below 2/9. No new seed
or larger coupling range is claimed in this section.

**PROVED — the diffusion consequence of that input.** Let `Pi_e` be
conditional expectation in link `e`, `N=|E|`, and
`K=N^(-1) sum_e Pi_e`. Each `Pi_e` is an orthogonal projection in
`L^2(mu_beta)`, so `K` is a positive self-adjoint contraction.
For the sum `D_ch(f)` of coordinate chord-Lipschitz seminorms, the
already proved iteration (10) in that source gives

\[
 \operatorname{osc}(K^t f)\le2q^tD_{\rm ch}(f),\qquad
 q=1-(1-\alpha)/N<1.                                  \tag{13}
\]

For centered smooth `f`, stationarity makes its left side bound
`||K^t f||_infinity`. Thus
`0<=<f,K^t f><=2||f||_1 D_ch(f) q^t`.
The spectral measure of `f` for `K` is positive. If it assigned positive
mass to `[q+epsilon,1]`, its `t`-th moment would eventually exceed that
bound. It assigns none. Smooth functions are dense, so on constants'
orthogonal complement `K<=q I`. It follows that

\[
 \sum_e\mu_\beta(\operatorname{Var}_e f)
 =N\langle f,(I-K)f\rangle
 \ge(1-\alpha)\operatorname{Var}_{\mu_\beta} f.
 \tag{14}
\]

Integrate the conditional estimate (10) and sum in `e`. Then

\[
 E(f)\ge2\sum_e\mu_\beta(\operatorname{Var}_e f)
       \ge(2-9\beta)\operatorname{Var}_{\mu_\beta} f.
 \tag{15}
\]

This holds even without gauge invariance. Consequently (8) supplies
(G2) on every compact interval with `b_+<2/9`, using
`lambda_*=2-9b_+`. It also covers fixed center-twisted measures.
For example, throughout `0<=beta<=1/5`, valid constants are

\[
                  \theta=49/50,\qquad \kappa=1/10.      \tag{16}
\]

The larger direct Poincare lower bound there is `1/5`.
These are exact rational bounds, with no numerical evaluation.

## 4. The locality bridge and the precise downstream scope

**READ.** `gap-tu-retry.md` Lemma L, section 2, proves the circle version
by finite propagation of derivatives and an `L^2` mixing remainder.
The following is its product-sphere extension, with the same covariance
identity. Credit that Codex proof. It supplies the missing locality part
of the “end” of (TU) in `gap-ac-lat.md:132`; no continuation in beta is used.

**PROVED — sphere version of Lemma L.** Join two links when they occur
in a common plaquette. Write `r(X,Y)` for this graph distance and put

\[
 D(F)=\sum_e\|\nabla_eF\|_\infty,\qquad
 B_{ee'}=\sup_U\|\nabla_e\nabla_{e'}S_\beta\|_{\rm op},\qquad
 v=\max(1,24\mathrm e\,b_+).
 \tag{17}
\]

Here the diagonal block has its covariant meaning. By (6), `B` is
symmetric and nonnegative, is zero beyond graph distance one, and has
row sums at most `24b_+`. Suppose the invariant gap is at least `kappa`.
For smooth invariant `F,G` supported on `X,Y`, respectively,

\[
 |\operatorname{Cov}(F,G)|
 \le v^{-1}D(F)D(G)e^{-r(X,Y)/2}
   +\|F\|_\infty\|G\|_\infty
                      e^{-\kappa r(X,Y)/(2v)}.
 \tag{18}
\]

To prove the derivative bound needed here, set `u_t=P_tF` and
`w_e=grad_e u_t`. Differentiating its equation gives the partial
Bochner identity

\[
 (\partial_t+L)|w_e|^2
 =-2\sum_j|\nabla_jw_e|^2-4|w_e|^2
       -2\sum_j\nabla_e\nabla_jS_\beta(w_e,w_j).
 \tag{19}
\]

The `-4` is twice the single-link Ricci endomorphism. Apply the scalar
chain rule to `(|w_e|^2+epsilon^2)^(1/2)`. The gradient terms have
nonpositive sum by Cauchy–Schwarz; the Ricci term is nonpositive too.
The remaining right side is at most
`sum_j B_ej (|w_j|^2+epsilon^2)^(1/2)`.
The maximum principle on the compact product, followed by `epsilon -> 0`,
therefore gives

\[
 \|\nabla_eP_tF\|_\infty
 \le\sum_i(e^{tB})_{ei}\|\nabla_iF\|_\infty.
 \tag{20}
\]

For completeness, compare with the spatially constant vector
`z(t)=exp(tB) z(0)`, with `z_e(0)=||grad_e F||_infinity+epsilon`.
At a first positive maximum of the difference, the nonnegative
off-diagonal coefficients and the scalar maximum principle prevent a
crossing. This proves the comparison used in (20).

A term in `(B^k)_ei` follows a path of at most `k` edges, while its
row sum is at most `(24b_+)^k`. Expanding the exponential thus gives
`sum_i exp(r(e,i))(exp(tB))_ei <= exp(24 e b_+ t) <= exp(vt)`.
In particular
`||grad_e P_tF||_infinity <= D(F) exp(-r(e,X)+vt)`.

Weighted integration by parts supplies the same identity as Lemma L:

\[
 \operatorname{Cov}(F,G)
 =\int_0^T\mu(\langle\nabla P_tF,\nabla G\rangle)\,dt
                      +\operatorname{Cov}(P_TF,G).
 \tag{21}
\]

For `r=r(X,Y)>0`, take `T=r/(2v)`. The integral is bounded by
`D(F)D(G)e^(-r)(e^(vT)-1)/v`, hence by the first term in (18).
Gauge invariance is preserved by `P_t`, so its invariant spectral gap
bounds the remainder by
`e^(-kappa T) sqrt(Var F Var G)`. This is the second term in (18).
For overlapping supports use `T=0` and Cauchy–Schwarz instead.
Disconnected components follow by sending their distance to infinity
in the path bound. This proves (18).

**PROVED — fixed-spacing implication, with its reconstruction premise.**
Every local limit of the periodic measures inherits (18). The constants
are independent of the periods. Lattice separation is comparable to this
link graph distance, since one step moves an anchor by at most one in
each coordinate. Thus smooth local invariant correlations decay
exponentially with a positive rate depending only on `kappa,b_+`.
No square-root-of-gap rate is asserted.

Suppose the limiting state is reflection positive and its positive transfer
contraction is reconstructed from the full local invariant algebra.
For any centered positive-time cylinder vector, (18) bounds its transfer
matrix element at time `n` by `C_F exp(-m n)`, for one common `m>0`.
The transfer spectral measure is positive. Its moment bound excludes
mass on `(exp(-m),1]`, by the same argument used after (13).
Centered local vectors are dense in this reconstruction, so its
Hamiltonian has no spectrum in `(0,m)` and no additional zero-energy vector.
This is the elementary spectral implication, conditional on that
reflection-positive reconstruction; it is not an identification of
the stochastic time with Euclidean time. No continuum gap follows
without a lower bound in physical units along the cutoff trajectory.

**READ / OPEN — the alternative twist consumer.** `gap-ext-astra.md`
section 1 defines `R_m(v)=Z^(m+v)/Z^m`,
`Q_F=max_(crossed pairs)(1-R_m(v))/2`, and requires
`8Q_F<=K(a)sqrt(S_ev)`, `Q_F<1/192`, with polynomial `K(a)`.
Equation (18) is a same-measure covariance estimate. It does not compare
those normalizers or give that rate relative to `S_ev`.
Thus this note takes the lattice-gap branch of the requested bridge.
It proves no new (FQ) or (V) estimate. An order-one application to the
twisted (TU) family also needs (G2) uniformly in that family, not merely
in the untwisted state. The strong-coupling proof above does have that
extra uniformity.

## 5. Hand tests and the exact loss at order one

### 5.1 Pointwise failure does not refute the integrated statement

**PROVED.** On a torus with even periods at least four, set
`U_mu(x)=(-1)^(sum_(nu<mu) x_nu) I`. Every plaquette is `-I`.
Perturb along `U_mu(x)exp(t X_mu(x))`, identifying the Lie algebra
with imaginary unit quaternions. Expanding a plaquette trace at this
central configuration gives

\[
             \nabla^2S_\beta(X,X)=-\beta\sum_p|(dX)_p|^2.
 \tag{22}
\]

Choose a unit imaginary quaternion `T`,
`X_mu(x)=(-1)^(x_1+x_2+x_3+x_4)a_mu T`, and `a=(1,-1,0,0)`.
Then `(dX)_mu,nu=2(-1)^(sum x)(a_mu-a_nu)T`.
The six squared differences sum to eight, while `sum_mu a_mu^2=2`.
Hence `sum_p|dX|^2=16 sum_e|X_e|^2`, and

\[
 (\operatorname{Ric}+\nabla^2S_\beta)(X,X)
                         =(2-16\beta)|X|^2.            \tag{23}
\]

It is negative when `beta>1/8`. This gives an explicit meaning to the
lane's approximate pointwise threshold; no assertion of the optimal
threshold is needed. In particular (16) holds at beta `1/5`, where
pointwise positive curvature fails.

This is a tangent-vector test, not a counterexample to (G2).
At that central configuration all invariant gradients vanish: global
conjugation fixes the configuration and rotates each tangent copy of
`R^3`, which has no invariant vector. Also (G2) integrates against the
full probability law and retains Hessian squares. Neither feature may
be removed in a purported counterexample.

### 5.2 The one-link comparison has an actual sharp stopping point

**PROVED — a local consequence of the existing chord estimate.** For
periods at least four, fix a link `e`. Set its 18 neighbours to central
values, with three of its six opposite parallel links equal to `-I`
and all other links in its six plaquettes equal to `I`. Its six staples
are three `+I` and three `-I`, so its conditional field is zero.

Each neighbour belongs to only one of those plaquettes. Varying it along
a unit geodesic changes the conditional field with derivative of norm
beta. Under Haar sphere measure, `mu(x_a x_b)=delta_ab/4`.
Testing the conditional mean against the unit linear function in that
derivative direction gives derivative `beta/4`. The chord displacement
of the changed neighbour divided by the geodesic parameter tends to one.
Thus its optimal uniform influence coefficient is at least `beta/4`.
The upper bound (12) is exactly attained in this infinitesimal sense.
For every row the optimal sum is therefore

\[
                              \alpha=9\beta/2.          \tag{24}
\]

Consequently the worst-exterior one-link chord contraction cannot be
continued past `beta=2/9` by improving that single-link constant.
This refutes that sufficient condition there, not (G2) or the Wilson gap.
The same background need not be typical. A worst-exterior criterion
must nevertheless include it.

### 5.3 Direct collective and local test functions

**PROVED — the plaquette test does not give a vanishing Rayleigh quotient.**
For `f=q_p`, sphere differentiation gives pointwise
`|grad f|^2=4(1-q_p^2)`. Condition on all links except one edge of `p`.
Its field has norm at most `6beta`, so the conditional density relative
to Haar is at least `exp(-12beta)`. Under that Haar integral
`mu(q_p^2)=1/4`. Hence
`E(q_p)>=3exp(-12beta)` and `Var(q_p)<=1`.
This particular family has Rayleigh quotient at least
`3exp(-12b_+)` in every volume. It cannot refute uniform coercivity
on a bounded interval by producing slow modes.

**PROVED — what the extensive energy test asks for.** Put
`A=sum_p(1-q_p)` and `p_Lambda(beta)=|P|^(-1)log int exp(beta sum_p q_p)dU`.
Since each plaquette has four link factors, `Delta A=12 sum_p q_p`.
Integrating `L_beta A` gives

\[
 \mu(|\nabla A|^2)=\frac{12|P|}{\beta}p_\Lambda'(\beta),\qquad
 \operatorname{Var}(A)=|P|p_\Lambda''(\beta),\qquad
 \frac{E(A)}{\operatorname{Var}(A)}
              =\frac{12p_\Lambda'(\beta)}{\beta p_\Lambda''(\beta)}.
 \tag{25}
\]

These identities hold for `beta>0`; variance is positive in finite volume.
Thus (G2) would bound the specific heat by
`p_Lambda''<=12p_Lambda'/(beta kappa)`. This is a necessary test, not a
proof of the gap. No volume-diverging susceptibility is proved here.

**PROVED — the retained-square identity.** The single-link calculation
can be retained instead of discarded. With

\[
 R=\sum_e\mu\bigl(\|\nabla_e^2 f-
                    \nabla_eS_\beta\otimes\nabla_e f\|^2\bigr),
 \qquad C_m=\sum_{e\ne j}
        \mu\bigl(\nabla_e\nabla_jS_\beta(\nabla_e f,\nabla_j f)\bigr),
\]

equations (3) and (9) read

\[
                 Q=\tfrac23H_d+H_m+\tfrac13R+2E+C_m.
 \tag{26}
\]

**OPEN — the missing joint estimate.** To prove (G2) through this identity,
one needs, for some
`0<delta<1`, `kappa>0`, uniformly on the desired order-one interval,

\[
 C_m+\tfrac13R\ge
  -(\tfrac23-\delta)H_d-(1-\delta)H_m-(2-\kappa)E
 \quad\text{for every invariant }f.                    \tag{27}
\]

This is exactly the remaining joint estimate, not a new solved reduction.
The absolute mixed-Hessian bound gives only (11). The sharp worst-exterior
comparison gives only (15). The plaquette and extensive-energy tests above
do not supply a counterexample or the missing cancellations.
No probability estimate for a bad configuration can replace (27): its
weights depend on the arbitrary test function's gradient.
The weakest sufficient spectral assertion is simply
`Q>=lambda_* E`, with a volume-uniform `lambda_*>0`.
Section 2 shows that asking for the Hessian reserve costs no additional
existence assumption once that assertion has actually been proved.

## 6. The two comparison groups

**READ / PROVED implication — U(1).** On unit circles Ricci is zero.
The correctly matched analogue is

\[
 \mu(\nabla^2S(\nabla f,\nabla f))
                  \ge-\theta\mu(\|\nabla^2 f\|^2)
                            +\kappa\mu(|\nabla f|^2).
 \tag{28}
\]

Row 805 already corrects the beta-zero test: the Fourier inequality
`H>=E` permits (28) with `0<kappa<=theta<1` at product Haar.
Zero Ricci is therefore not a refutation.

For the large-beta periodic Villain law, use `gap-tu-retry.md` Theorem V:
at fixed `beta>=2^14`, its invariant diffusion gaps `gamma_M` tend to zero.
That theorem is reused at its stated proof status; it is not rebuilt here.
Let `f_M` be a smooth invariant gap eigenfunction. For the Villain
potential `S=-sum_p log phi_beta((d theta)_p)`, circle Bochner gives
`C=Q-H=gamma_M E-H`. Thus

\[
 C+\theta H-\kappa E
       =(\gamma_M-\kappa)E-(1-\theta)H<0
       \quad\text{once }\gamma_M<\kappa.                \tag{29}
\]

This identifies the failing step: the integrated coercivity inequality
itself fails on slow gauge-invariant modes. The locality bridge does
not fail. Theorem V also excludes the weakest assertion `Q>=kappa E`.
It is a Villain theorem. As section 4 of that source states, its
Wilson-cosine specialization is not proved there; it is not silently
imported here. Freezing a large-beta Villain potential and multiplying it
by `b in [b_s,1]` gives the genuine fixed-action continuation obstruction
already proved in that source's section 3.

**PROVED — binary icosahedral scope.** Counting Haar measure on the
120-element subgroup has no sphere tangent vectors, Levi-Civita Hessian,
or unit-sphere Laplacian. Equations (3) and (9) cannot be written for
that measure. Restricting a smooth ambient function to the group does
not fix this: its derivatives depend on the chosen extension, while
the restricted function does not. A jump generator would require a
different Dirichlet form and a different curvature identity.
Thus this route does not transfer to that group. This is inapplicability
of the differential structure, not a theorem about its phase diagram.

## 7. Result and next obligation

**PROVED, not independently checked here.** (G2) is equivalent to a
volume-uniform invariant Langevin gap on a bounded beta interval.
The conditional identity (9), together with the already proved
chord-influence input, establishes (G2) for `beta<2/9` and gives the
explicit example (16). The sphere extension of Lemma L proves
exponential covariance decay from such a gap, with a stated rate.
The pointwise and optimal chord-comparison tests (23), (24) identify
why those two sufficient methods stop. The Villain failure is exactly
(29), conditional on the existing Theorem V.

**OPEN.** A positive volume-uniform invariant diffusion gap, equivalently
(G2), on a compact interval reaching the requested order-one regime.
No such bound or SU(2) counterexample is supplied. Equation (27) is the
precise missing estimate for this single-link decomposition. A useful
next attempt must estimate its mixed terms with the retained squares,
or construct a genuinely collective low-Rayleigh family. Improving the
constant `1/4` in the worst-exterior single-link comparison cannot do it.
No continuum gap, new twist seed, (FQ), (V), or scientific status is claimed.

**READ — verification boundary.** The author reread the complete output
and its constants. This is a self-check, not an independent check.
Mechanical checks found balanced display delimiters, unique equation
numbers, and one final RESULT line; the diff check emitted no whitespace
diagnostics. The receipt is
`/tmp/sa-gap-gamma2-astra.CcLzXy/text-verification.txt`.
No numerical experiment, proof assistant, or audit was run.

RESULT: OPEN at order one; proved (G2) in the existing beta<2/9 range, its equivalence to a uniform invariant Langevin gap, and the sphere locality bridge; the joint estimate (27) remains missing.
