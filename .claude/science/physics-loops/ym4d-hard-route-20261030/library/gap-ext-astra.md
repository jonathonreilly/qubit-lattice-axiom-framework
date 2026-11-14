# Repo search

The lead's `prior/repo-search-2026-11-08.md` covers earlier
large-field and history targets. Its local transfer witness is
related, but does not estimate a twisted partition-function ratio.
I read PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166` and
`checks/review_massgap_block_literature.md:105–130`, relative to
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
The former supplies the finite-beta witness already used by
`gap-fusion-astra.md`. The latter records Ito and Seiler's warning:
separate interpolations do not supply a common twisted endpoint.
These are prior results, not new work here.

A fresh search outside this lane, on main and the four requested
PR heads, for `Tomboulis`, `Kanazawa` and `vortex.free.energy`
found that review on PRs 10114 and 10133. No supplier appeared
in that search. The broader `weighted.exterior` inventory was
not fully read and supplies no premise. A small-commutator
search also found PR 10114's `NONLINEAR_CHART_ACTIVITY_ASTRA.md`
at 82–108 and the sibling `ym4d-existence/EXISTENCE_session6_snapshot.md`
at 2268–2295. I read those ranges: they concern covariance
patching and noise in block averages, respectively. Neither
estimates a centre-twist ratio. No numerical result from the
snapshot is imported.

Read revisions:

| Ref | Commit |
|---|---|
| main | `bb4ec020d5ada57c630dd89acc98a68397ade423` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `fb99b4dddc7254e6124ac124887d58eeb3a77802` |

The target-specific `prior/gap-ext-astra.md` is absent at the pin.
Searches of `open-registry.md`, `open-core.md` and `l17c.md` for
the target, vortex, electric flux and the named inequalities found
no competing owner. Row 789 explicitly follows rows 783 and 788.
Their exact identity and fixed-fibre obstruction are reused.
They are not re-proved here. The broader fusion and light-group
tasks retain their existing owners.

## Contract and checkpoint

Author: **Codex gpt-6-astra max**, FINISH row 789, 2026-11-12.
Source pin: `3b5f2007efb4e5ac55c25e27cc2f22580e618a86`.
Research text, not an audit; this grants no status.
**PROVED** means an author hand proof, not an independent check.
**ARGUED** marks an unverified argument or a literature import.
**GUIDE** decides nothing. **OPEN** names an unproved statement.

Read first: GOAL, the requested FINISH sections,
`gap-cf-astra.md` and its Opus check in full,
`gap-vortex-astra.md` Sections 4–8, `gap-fusion-astra.md`
Section 5, and `gap-skeleton-final.md` Sections 13.16–13.20.
Credit Codex for the reduction and commutator results, Claude
Opus 5.5 for their check, and the named authors of the prior work.
Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text**, for all outline/account material used.

The outline and CA-I were fetched once at `31a47c543775`, into
the new private scratch directory
`/tmp/gap-ext-astra-20261112.ib8L4G/`.
No numerical run or computer-assisted proof is used.

**OPEN — final checkpoint.** The weighted exterior estimate (26)
and its weaker consumer (FQ) remain unproved. Sections 2–3
give the exact limits of sheet averaging and reflection positivity.
Section 4 proves a size-uniform positive lower and upper bound
on rank-four classical action, and the exact group input (LC).
The latter fails in both comparison groups. Section 5 gives a
normalizer-preserving transport test; complete centre-orbit
randomization cannot meet its exponential tolerance. The missing
step is the Wilson-weighted action-and-entropy control (E22)
for a correlated deformation, as specified at the end.

## 1. The consumer and the measure

**PROVED inputs, reused from rows 778, 783 and 788.** Let
`n=(a,a,c,d)`, with `a>=3` and `c,d in {a,2a}`. Write
`s_p(U)=tr(U_p)/2` and `N_p=6a^2cd`. Let m be a spatial
twist in the chosen time frame. For a closed sign cocycle
`eta_m` representing it, use

\[
 S_m(U)=\beta\sum_p(1-\eta_{m,p}s_p(U)),\qquad
 d\mu_m=Z_m^{-1}e^{-S_m(U)}dU.
 \tag{E1}
\]

Here `Z_m=e^{-beta N_p}Z^m`, so all partition-function ratios
agree with the earlier convention. Haar measure is normalized.
For a representative `Sigma` of a temporal twist `v=v_ri`, put

\[
 X_\Sigma^m=2\beta\sum_{p\in\Sigma}\eta_{m,p}s_p,
 \quad W_\Sigma^m=e^{-X_\Sigma^m},\quad
 R_m(v)=\mathbb E_{\mu_m}W_\Sigma^m,
 \quad F_m(v)=-\log R_m(v).
 \tag{E2}
\]

For the admissible pairs, `0<R_m(v)<=1`. For `(0,v_34)`
the insertion is exterior-measurable for row 783's selection.
Thus (E2) is exactly its (26), by disintegration, with the
same `B_0 d xi/Z^0`. Working on full link space permits
fibre-mixing maps without replacing that measure.

**OPEN target.** On a fixed compact interval
`I=[beta_-,beta_+]` inside `(0,infinity)`, bound every required
`F_m(v)` by `C a^p exp(-sigma a^2)`. The equivalence with
(V), up to constants, is row 778 (1)–(3), not a new result.

**OPEN weaker sufficient input, reused.** The fusion consumer
needs only the crossed pairs in frame 1:

\[
 Q_F=\max_{m_2=0,\ i=3,4}\frac{1-R_m(v_{1i})}{2},\qquad
 8Q_F\le K(a)\sqrt{S_{\rm ev}(a;(a,c,d))},\quad
 Q_F<1/192,\quad K(a)\le C_1a^{p_1}.
 \tag{FQ}
\]

This is row 778's weakest consumer, with its original name.
It does not require the area exponent. The prior witness gives
`S_ev>=eta_*^a` on `I`, for a fixed `eta_*>0`.
No estimate below verifies (FQ) at order-one coupling.

## 2. Moving the sheet: exact algebra, no averaging gain

### 2.1 Representative changes retain the weighted measure

**PROVED; standard centre-substitution identity, credited.**
For a link sign cochain `b`, let `(T_bU)_e=(-1)^{b_e}U_e`.
This preserves product Haar measure, and

\[
 S_\eta(T_bU)=S_{\eta(-1)^{\delta b}}(U).
 \tag{E3}
\]

The identity follows because each link sign contributes once
to the plaquette coboundary. Thus `Z_eta` depends only on
the class of `eta`. This is the centre-substitution algebra
used by Takuya Kanazawa, Section 2, Lemma 1 of
[arXiv:0808.3442v3](https://arxiv.org/html/0808.3442v3#S2).
It is not a new confinement mechanism.

In particular, for any field-independent probability `pi` on
representatives of `v`,

\[
 \mathbb E_{\mu_m}\sum_\Sigma\pi(\Sigma)W_\Sigma^m=R_m(v).
 \tag{E4}
\]

Neither (E3) nor (E4) says that `T_b` preserves `mu_m`.
Its density changes by the action difference. A field-dependent
choice of sheet also needs its change-of-measure factors;
(E4) does not license deleting them.

### 2.2 Disjoint sheets are not independent trials

**PROVED consequence of the standard insertion algebra.** Choose
`M>=2` pairwise plaquette-disjoint representatives of the same
class `v`. For `v_34`, all `n_3 n_4` translated flat stacks
are such a family. At background `m`, write their insertions
as `W_1,...,W_M` and their common expectation as `R`.
For each subset `A` of indices,

\[
 \mathbb E_{\mu_m}\prod_{j\in A}W_j
 =\begin{cases}1,&|A|\text{ even},\\R,&|A|\text{ odd}.
 \end{cases}
 \tag{E5}
\]

Indeed disjoint supports make the product exactly the insertion
on their union. Its cocycle class is `(|A| mod 2)v`.
Equation (E3) then gives (E5). The disjointness qualification
is essential; a square of the same insertion is different.

Consequently, for `j!=k`,

\[
 \operatorname{Cov}_{\mu_m}(W_j,W_k)=1-R^2,
\]
\[
 \operatorname{Var}_{\mu_m}\!\left(M^{-1}\sum_jW_j\right)
 =M^{-2}\sum_j\operatorname{Var}_{\mu_m}(W_j)
       +(1-M^{-1})(1-R^2).
 \tag{E6}
\]

Thus taking many disjoint positions does not divide the unknown
deficit by their number. There is an exact common covariance.
For `P_j=(1-W_j)/2`, expansion of (E5) likewise gives
`E product_{j in A} P_j=(1-R)/2` for every nonempty `A`.
These are flux-projector identities in expectation. `P_j` need
not be pointwise nonnegative. Treating them as independent
Bernoulli events would change the mathematics.

### 2.3 Shape averaging still has a pointwise obstruction

**PROVED, narrowly scoped.** For `m=0`, any positive normalized
average of the insertions in (E4) is small near the identity
configuration, regardless of how many shapes it includes.

Every representative of `v_34` meets each coordinate 34-torus
an odd number of times. There are `a^2` disjoint such tori,
indexed by `(x_1,x_2)`. Hence it contains at least `a^2`
34-plaquettes. On the open set where all plaquette traces
satisfy `s_p>1/2`,

\[
 W_\Sigma^0<e^{-\beta a^2},\qquad
 \sum_\Sigma\pi(\Sigma)W_\Sigma^0<e^{-\beta a^2}.
 \tag{E7}
\]

That set contains the identity and has positive Haar and Wilson
measure. All cocycles on the finite lattice are covered at once.
Thus positive representative averaging cannot give a pointwise
lower bound tending to one. This extends the test to sheet
positions and shapes; it does **not** bound their integrated
expectation away from one. Nor does it exclude a transport
with a nontrivial density or a weighted exceptional-set argument.

## 3. Reflection positivity and the light group

### 3.1 What the published inequalities actually supply

**ARGUED literature input, not discharged here.** E. T. Tomboulis
and L. G. Yaffe's inequality, in Kanazawa's Theorems 1–2, gives

\[
 |\langle W(C)\rangle|\le 2q^{A_C/(n_rn_i)},\qquad
 q=\tfrac12(1-Z^{v_{ri}}/Z^0).
 \tag{E8}
\]

Here take rectangle sides `ell_r,ell_i`, with
`n_r=2^u ell_r`, `n_i=2^w ell_i` for positive integers u,w,
as in the printed proof, and `A_C=ell_r ell_i`. Its site-reflection
positivity acts on insertions in the untwisted measure.
The input is a small `q`; the inequality does not estimate it
from above. This direction is already recorded in row 778.
The source is
[Kanazawa, Section 2](https://arxiv.org/html/0808.3442v3#S2).

**PROVED limitation of this inference.** Rearranging (E8) gives
`q >= (|<W(C)>|/2)^(n_r n_i/A_C)`, a lower bound.
An upper bound on the commutator word of row 778 cannot reverse
this inequality. That word also has zero winding centre charge.

Equations (E5) give the same obstruction to a naive reflected
product argument: two separated flux insertions have expectation
`q`, not `q^2`. Gluing alone inserts no strict contraction.
An inequality with a new quantitative input might do so;
none follows here from repeated Cauchy–Schwarz.

### 3.2 A twist is not a positive crossing kernel in every cut

**PROVED diagnostic; not a denial of site-reflection positivity.**
On `L^2(SU(2))` consider convolution with
`K_beta(g)=exp(beta tr(g)/2)`. Let `f(g)=tr(g)`.
Schur averaging gives the eigenvalue

\[
 c_\beta=\int s(g)e^{\beta s(g)}dg
          =\int s(g)\sinh(\beta s(g))dg>0
 \quad(\beta>0)
 \tag{E9}
\]

on the fundamental coefficient space. The equality uses
Haar invariance under `g -> -g`; the strict sign holds off
the Haar-null set `s=0`. The centre-twisted crossing kernel is
`K_beta(-g)=K_{-beta}(g)`. Since `f(-g)=-f(g)`, its eigenvalue
on `f` is `-c_beta`. Hence

\[
 \iint\overline{f(U)}K_\beta(-UV^{-1})f(V)\,dU\,dV
 =-c_\beta\|f\|_2^2<0.
 \tag{E10}
\]

Pointwise positivity of the Boltzmann factor therefore does not
make this link-crossing form positive. Spatially twisted positive
transfer operators, and valid site reflections, remain available.
A temporal centre insertion has to stay in its actual location
in the positive trace; it cannot be relabelled a positive operator
on the odd sector. This rules out that particular shortcut.

### 3.3 Theorem R consumes the missing quantitative information

**PROVED input, reused.** Claude Fable 5.2's R1–R3 and Theorem R,
checked by Codex in row 744, apply with the definitions in
`gap-means-max.md` Sections 4.1–4.6. On `(a,a,c,d)`, they give

\[
 \sum_xp_x(1-p_x)\le4\theta,\qquad
 \theta=1-e^{-\Delta}(1+S)^{-2},\qquad
 \Delta=a[2e(a,c,d)-e(2a,c,d)].
 \tag{E11}
\]

Here `S=S_ev(a;(a,c,d))`, `e(B)=log lambda_0(B)`, and the
sixteen crossed weights sum to four. When `theta<1/20`,
their total distance from a four-element light group is at most
`8theta`. Cubic symmetry gives the three candidates in Theorem R.
The positive Wilson integrand excludes the diagonal candidate,
as row 778 Section 3 already shows. It leaves electric and magnetic.

**PROVED conditional selection test; no estimate of its inputs.**
On the symmetric cube, suppose the hypotheses selecting these
candidates hold. A single lower bound

\[
 Z^{v_{34}}/Z^0>64\theta
 \tag{E12}
\]

selects the magnetic candidate. To see this, rotate the basic
twist to `v_23`, a spatial `m` in frame 1 with one nonzero bit.
For an electric light group, `p_{0,m}<=8theta` by (E11).
Positivity of the temporal Fourier coefficients and of the
twisted integrals gives `Z_{chi,m}<=Z_{0,m}`. Thus

\[
 \frac{Z^m}{Z^0}
 =\frac{\sum_\chi Z_{\chi,m}}{\sum_\chi Z_{\chi,0}}
 \le8\frac{Z_{0,m}}{Z_{0,0}}\le64\theta,
\]

contrary to (E12). This uses only the prior dominance inequality
and the checked dichotomy. It does not prove (E12) or small `theta`.

**OPEN.** A constant lower bound on a twist ratio could suffice
for this *conditional phase selection*. It would not supply the
small `S` and `Delta` in (E11), an area estimate, or (FQ).
Using Theorem R to obtain those hypotheses would be circular.
No bound reducing the vacuum-energy defect to S is assumed.
The prior counterexamples to the linear (ES-1) proposal remain
in force.

## 4. What continuous flux spreading can mean exactly

### 4.1 The rank-four classical cost stays between constants

**PROVED.** Put `k_*=v_12+v_34` and
`E_k(U)=sum_p[1-eta_{k,p}s_p(U)]`, without the factor beta.
There is a fixed `c_*>0`, independent of `a,c,d`, such that

\[
 c_*\le\inf_U E_{k_*}(U)\le\frac{17\pi^2}{8}
 \quad\text{on }(a,a,c,d),\quad c,d\in\{a,2a\}.
 \tag{E13}
\]

The comparison sector `v_34` has minimum zero, by the flat
anticommuting-holonomy construction already used in row 783.
The pair `(v_34,k_*)` is required in frame 1.

*Lower bound.* Reuse the checked group obstruction from row 783
Section 1.3: no four SU(2) matrices have central commutator matrix
`k_*`. Define

\[
 d_*:=\min_{g_1,\ldots,g_4\in SU(2)}
 \max_{\mu<\nu}
 \|[g_\mu,g_\nu]-(-1)^{k_{*,\mu\nu}}I\|_{\rm op}>0.
 \tag{E14}
\]

The minimum exists by compactness. If it were zero, it would
give precisely the excluded quadruple. This is an existence
argument for a constant, not a numerical minimization.

At each vertex `y`, take the four coordinate-circle holonomies
based there. Cut each coordinate two-torus `T_mu nu(y)` to its
rectangle. Cancelling its interior edges writes its boundary
commutator as an ordered product of conjugated plaquette holonomies.
One can peel the rectangle row by row: replacing a boundary
segment by the other sides of its adjacent plaquette multiplies
the boundary word by that plaquette, conjugated by the preceding
boundary path. Each plaquette is removed once. This proves the
product identity also when the curvatures are not central.
The central signs have product `(-1)^(k_* mu nu)`. Unitary
conjugation preserves the operator norm, and
`||V_1...V_l-I||<=sum_j||V_j-I||`. Therefore

\[
 d_*^2\le
 2\sum_{\mu<\nu} n_\mu n_\nu
       \sum_{p\in T_{\mu\nu}(y)}[1-\eta_{k_*,p}s_p].
 \tag{E15}
\]

Here Cauchy–Schwarz was applied separately on each torus;
`||I-eta U||_op^2=2[1-eta tr(U)/2]` for SU(2).
The maximum squared commutator error is bounded by the sum
of these six squared bounds.

A plaquette of orientation `mu nu` belongs to exactly
`n_mu n_nu` of the tori indexed by `y`. Summing (E15), with
`V_lat=a^2cd`, yields

\[
 V_{\rm lat}d_*^2
 \le2\sum_p(n_{\mu(p)}n_{\nu(p)})^2[1-\eta_{k_*,p}s_p]
 \le2(cd)^2E_{k_*}(U).
\]

Thus `E_{k_*}>=d_*^2 a^2/(2cd)>=d_*^2/8`.
Take `c_*=d_*^2/8`.

*Upper bound.* The following explicit Cartan field supplies it.
For a plane `mu nu`, put `theta=pi/(n_mu n_nu)` and, using
coordinates `0,...,n_j-1`, set

\[
 U_\mu(x)=e^{-i\theta x_\nu\sigma_3},\qquad
 U_\nu(x)=
 \begin{cases}
 e^{i\theta n_\nu x_\mu\sigma_3},&x_\nu=n_\nu-1,\\
 I,&x_\nu\ne n_\nu-1.
 \end{cases}
 \tag{E16}
\]

All other links of this one-plane field are identity. Its
`mu nu` plaquettes equal `exp(i theta sigma_3)`, except at
`x_mu=n_mu-1,x_nu=n_nu-1`, where they have the additional
sign `-1`. This follows by multiplying the four displayed
link factors. For example at that corner their exponent is
`theta-theta n_mu n_nu=theta-pi`. All other orientations
have identity curvature.

Use (E16) for planes 12 and 34 and multiply the fields.
Their matrices commute and each field depends only on its
own two coordinates. Cross-plane curvatures remain identity.
Use the two corner stacks as `eta_{k_*}`. Then

\[
 E_{k_*}
 =a^2cd\{1-\cos(\pi/a^2)+1-\cos(\pi/(cd))\}
 \le\frac{\pi^2}{2}
       \left(\frac{cd}{a^2}+\frac{a^2}{cd}\right)
 \le\frac{17\pi^2}{8}.
 \tag{E17}
\]

We used `1-cos t<=t^2/2` and `1<=cd/a^2<=4`.
Representative changes preserve the infimum by (E3).
This completes the hand proof of (E13).

**PROVED distinction; OPEN statistical consequence.** For a finite
subgroup G containing `-I`, define
`Delta_G=min_{g!=I}(1-tr(g)/2)>0`. Row 783 gives
`E_{k_*}>=Delta_G a^2`. SU(2) replaces
that area barrier by a bounded classical cost. It does not make
the total rank-four cost tend to zero. `Delta_SU(2)=0` means
there is no fixed cost per nonidentity plaquette.

The upper construction lies in U(1) as well. Thus low classical
flux cost alone fails the Abelian test. Neither extremal action
in (E13) estimates a normalized finite-beta partition function.
Counting the volume of neighbourhoods, or comparing their full
weighted integrals, is still required. No interchange of the
large-size and zero-temperature limits is made.

### 4.2 An exact small-commutator input that passes both tests

**PROVED group input (LC).** For every integer `N>=2`, there are
`A_N,B_N in SU(2)` with

\[
 [A_N,B_N]=C_N:=e^{i\pi\sigma_3/N},\qquad C_N^N=-I,
\]
\[
 1-\tfrac12\operatorname{tr}A_N\le\frac{\pi}{2N},\qquad
 1-\tfrac12\operatorname{tr}B_N\le\frac{\pi}{2N},\qquad
 N(1-\tfrac12\operatorname{tr}C_N)\le\frac{\pi^2}{2N}.
 \tag{LC}
\]

*Proof.* Put `theta=pi/N` and choose
`alpha in (0,pi/2)` with `sin^2 alpha=sin(theta/2)`.
In quaternion notation start with
`A=cos alpha+i sin alpha`, `B=cos alpha+j sin alpha`.
Conjugation by A rotates j to `cos(2alpha)j+sin(2alpha)k`.
The scalar part of `ABA^{-1}B^{-1}` is therefore
`cos^2 alpha+sin^2 alpha cos(2alpha)=1-2sin^4 alpha=cos theta`.
Conjugate A and B together so that their commutator axis is
the chosen third axis. This gives the first line of (LC).
Finally

\[
 1-\cos\alpha
 =\frac{\sin^2\alpha}{1+\cos\alpha}
 \le\sin(\theta/2)\le\theta/2,
\]

and `1-cos theta<=theta^2/2` proves the remaining bounds.
The generators converge to identity in operator norm.

**PROVED binding tests.** In a finite subgroup with `Delta_G>0`,
the generator bounds in (LC), for sufficiently large N, force
both generators to be identity. Their commutator cannot have
Nth power `-I`. In U(1) every commutator is identity for
every N. Thus (LC) fails in both comparison groups, including
the binary icosahedral group. It uses continuity and local
noncommutativity together, beyond row 783's density flattening.

This is the precise group property available to a proposed
spreading argument. Its last bound concerns the commutator
elements only. It is not a bound on all plaquettes affected
by inserting the generators into a Wilson configuration.

### 4.3 Cheap coherent flux is not cheap independent mixing

**PROVED obstruction to one use of (LC).** Independently conjugate
each `C_N` by a Haar variable `G_j`, and multiply the N results.
Call the product law `nu_N`. Schur averaging and independence give

\[
 \mathbb E_{\nu_N}\tfrac12\operatorname{tr}g
 =(\cos(\pi/N))^N
 \ge1-\frac{\pi^2}{2N}.
 \tag{E18}
\]

Indeed each mean matrix is `cos(pi/N)I`. The lower bound is
Bernoulli's inequality with `0<=1-cos(pi/N)<=1`.
Let `nu_N^-` be its translate by `-I`, and define total variation
as `sup_A|nu_N(A)-nu_N^-(A)|`. Testing with `tr(g)/2`, which
is bounded by one and odd, gives

\[
 \|\nu_N-\nu_N^-\|_{\rm TV}\ge(\cos(\pi/N))^N\longrightarrow1.
 \tag{E19}
\]

The deterministic product in (LC) is `-I`; its independently
randomized version remains strongly biased toward `+I`.
Neither gives centre flattening.

More generally, let independent conjugation-invariant increments
have `epsilon_j=E[1-tr(C_j)/2]` in `[0,1/2]`. Their product
has fundamental mean

\[
 \prod_j(1-\epsilon_j)\ge
       \exp\{-2\sum_j\epsilon_j\}.
 \tag{E20}
\]

This uses `log(1-x)>=-2x` on that interval. Exponential
suppression `<=exp(-sigma N)` in this construction requires
`sum_j epsilon_j>=sigma N/2`. A vanishing or bounded total
increment cost cannot provide it.

**PROVED auxiliary example; GUIDE for Wilson.** Correlation can
evade (E20). A common fair coin can choose all identity
increments or all the coherent `C_N` increments. The endpoint
law is then `(delta_I+delta_{-I})/2`, while its expected sum
of commutator deficits is at most `pi^2/(4N)`. This auxiliary
construction shows why (E20) is not a no-go theorem for
correlated transports. It supplies no Wilson change of variables,
no density comparison and no control of the exterior weight.

## 5. A transport test that retains the normalization

### 5.1 The exact action-and-entropy balance

**PROVED, standard variational identity in the present variables.**
Fix an admissible pair and its representatives. Write
`mu=mu_m`, `mu'=mu_{m+v}`, `X=S_{m+v}-S_m` and `F=F_m(v)`.
For any probability `nu` absolutely continuous with respect to mu,
with finite relative entropy,

\[
 \mathbb E_\nu X+D(\nu\Vert\mu)
 =F+D(\nu\Vert\mu')\ge F.
 \tag{E21}
\]

Indeed `dmu'/dmu=exp(F-X)`; take logarithms and integrate.
Relative entropy is nonnegative by Jensen's inequality for
`-log`. The infimum over all nu is F, attained at mu'.
Thus free optimization of (E21) is equivalent to the target.
Taking the unknown twisted law as the trial law would repeat
the circularity identified in row 783 (27)–(29).

There is a concrete sufficient version for fibre-mixing maps.
Let `T_j`, for a finite index set, be Haar-preserving measurable
bijections with measurable inverses. Choose probabilities `pi_j`
independent of the field. Set

\[
 \nu_j=(T_j)_*\mu,\quad \nu=\sum_j\pi_j\nu_j,\qquad
 I_\pi=\sum_j\pi_jD(\nu_j\Vert\nu),
\]
\[
 \mathcal C(T,\pi)
 :=\sum_j\pi_j\mathbb E_\mu
       [S_{m+v}(T_jU)-S_m(U)]-I_\pi.
 \tag{E22}
\]

Then, exactly,

\[
 \boxed{\mathcal C(T,\pi)=F+D(\nu\Vert\mu')\ge F\ge0.}
 \tag{E23}
\]

*Proof.* The density of nu_j is
`exp[-S_m(T_j^{-1}U)]/Z_m`. Haar preservation gives

\[
 D(\nu_j\Vert\mu)
 =\mathbb E_\mu[S_m(T_jU)-S_m(U)].
\]

Adding `E_{nu_j}X` gives the jth action difference in (E22).
The elementary density identity

\[
 \sum_j\pi_jD(\nu_j\Vert\mu)
 =D(\nu\Vert\mu)+\sum_j\pi_jD(\nu_j\Vert\nu)
\]

follows by splitting `log(dnu_j/dmu)` through `dnu/dmu`.
Average the X term and apply (E21). This proves (E23).
All densities here are bounded above and away from zero on
the finite-lattice configuration space, so the integrals are finite.

The term `I_pi` is the information retained about the chosen
map by its output. It is not automatically the entropy of
the choice. In its defining density ratio, `Z_m` cancels.
Thus the left side of (E23) can be specified using only the
untwisted-background law and explicit maps; it does not insert
the unknown `Z^{m+v}/Z^m` into a factor.

**OPEN sufficient statement.** Construct such maps from the
Wilson variables, with a quantitative use of (LC), and prove

\[
 \mathcal C(T,\pi)\le C a^p e^{-\sigma a^2}
 \tag{TR-V}
\]

uniformly on I for every required pair and shape. This would
give (V). For (FQ), a weaker sufficient bound, on its crossed
pairs only, is

\[
 \mathcal C(T,\pi)\le
 \min\left\{\frac1{96},\frac{K(a)}4\eta_*^{a/2}\right\},
 \qquad K(a)\le C_1a^{p_1}.
 \tag{TR-F}
\]

To check the constants, `q=(1-e^{-F})/2<=F/2`, and
`sqrt(S_ev)>=eta_*^(a/2)`. Hence
\(8q\le4\mathcal C(T,\pi)\le K(a)\sqrt{S_{\rm ev}}\).
Also `F<=1/96` gives `q<1/192`. Take maxima over the
specified pairs. (TR-F) is a constructive sufficient test;
the weaker actual-model consumer remains the already known (FQ).
Neither transport test is established here.

### 5.2 Uniform averaging over all link signs fails this test

**PROVED for this particular transport family.** Take `m=0`,
all link-sign maps `T_b`, and the uniform probability on them.
Their mixture nu is invariant under every individual link flip.
Thus `E_nu s_p=0` for each plaquette: flip one of its edges.
In particular `E_nu X=0`, and (E21)–(E23) give

\[
 \mathcal C=D(\nu\Vert\mu_0).
 \tag{E24}
\]

There is a uniform polynomial lower bound on this cost.
Put `N_p=6a^2cd`, `c_0(beta)=integral exp(beta s(g)) dg`, and

\[
 \kappa_I=\min_{\beta\in I}\frac{\log c_0(\beta)}\beta>0.
\]

Strict Jensen gives `c_0(beta)>1` for beta positive, since
`E_Haar s=0` and s is not constant. Continuity and compactness
give the strictly positive minimum.

Let `f(beta)=log Z^0(beta)` in the original unshifted convention.
One has `Z^0(beta)>=c_0(beta)`. To prove this, fix the four
edges of one plaquette p and Haar-integrate all other edges.
Every other plaquette has an edge outside p, so its conditional
Haar mean is zero. Jensen's inequality bounds that conditional
integral from below by the p factor. Its remaining integral
is exactly c_0. The assumption that all sides are at least
three avoids duplicated plaquette edge sets.

Convexity, `f(0)=0`, and differentiation of the finite integral
now give, for `A(U)=N_p^{-1}sum_p s_p(U)` in `[-1,1]`,

\[
 \mathbb E_{\mu_0}A=\frac{f'(\beta)}{N_p}
 \ge\frac{f(\beta)}{\beta N_p}
 \ge\frac{\kappa_I}{N_p},\qquad \mathbb E_\nu A=0.
\]

For completeness, `D(nu||mu)>=2||nu-mu||_TV^2`: split the
integral over the set where `dnu/dmu>=1`; conditional Jensen
reduces it to Bernoulli relative entropy. At fixed second
parameter, that entropy has second derivative
`1/[t(1-t)]>=4`, and vanishes with zero first derivative
at equality. Integration twice proves the bound, including
endpoint limits. Since a test in `[-1,1]` has mean difference
at most twice total variation, (E24) implies

\[
 \mathcal C\ge\frac{\kappa_I^2}{2N_p^2}
              \ge\frac{\kappa_I^2}{1152a^8}.
 \tag{E25}
\]

This exceeds either exponential tolerance (TR-V) or (TR-F)
for all sufficiently large a and any fixed polynomial prefactor.
Thus complete, unweighted centre-orbit randomization cannot pass
this variational test. This is a statement about its trial
cost, not a lower bound on the actual F. A more selective
or field-dependent transport is not excluded.

### 5.3 Where the continuous transport attempt stops

**PROVED prior obstruction, reused without a new derivation.**
`gap-crux-restate.md:143–160`, Lemma J and Way 3, already treats
fixed smooth link multiplications. Gauge averaging reads their
corner factors, not merely the classical curvature of the added
field. Its direct first-order spreading bound grows with the
box. I read that argument and do not count it as new here.

**OPEN.** Equations (LC) and (E13) give group elements and
configurations. They do not give transformations for arbitrary
Wilson fields with the required value of (E22). To use the
coherent small commutators, one must control all neighbouring
plaquettes, the output density and its information term together.
Keeping only the cost of the commutator elements omits those
terms. Replacing `I_pi` by the entropy of the choices is also
unjustified. This is the first missing step in this transport
attempt, before any area exponent or uniformity in beta.

## 6. Source checks and the stopping point

**ARGUED source classification, not an absence theorem.** The
Sussman–Alpoge index README, matching chunk rows and neighbouring
rows, and obligations were consulted before the source excerpts.
No index hit was found for vortex, electric flux, Tomboulis,
Kanazawa, the commutator law or the binary icosahedral group.
Chunk 24 at 108–118 and obligations at 1352–1357 lead to
outline 26765–26805 and 26848–26867: ET5 assumes an energy
“serving both measures”; ET6 is conditional on it. This is
a covariance comparison, not a twisted Wilson normalizer theorem.
Chunk 01 at 65–71 and obligations at 19–27 lead to outline
565–600, separating polynomial clustering from a mass gap.
CA-I 2490–2515 and 2698–2714 state the corresponding scope
limits. These passages do not supply (26). No ultraviolet
estimate, Balaban theorem, or status from their account is imported.

The complete-account index for 4.12–4.19 was included in the
object-name search; no statement from those items is needed here.
The fetched files have the prescribed 32,992 and 166,711 lines.
The source revision is `31a47c543775` throughout.

**ARGUED literature record.** The prior searches
`prior/gap-lit-flux.md` and row 781's
`prior/gap-lit-commutator.md` were used as locators, with credit
to their Codex authors. The latter's question/answer, decimation,
commutator-loop and comparison sections were read. It locates
no Wilson supplier for the normalized comparison. Its broad
search was not repeated. Row 787's output is absent at this pin;
its literature assignment is not taken over.

The primary passages read here are Kanazawa Section 2.1 and
Section 2.2 through Theorem 2's proof, and
[Erhard Seiler, Sections 2–4 of arXiv:0901.4246v1](https://arxiv.org/html/0901.4246v1#S2).
Seiler distinguishes the needed ratio estimate from local
interpolation and records the Abelian obstruction. That warning,
and the earlier work of K. R. Ito, are credited. No published
decimation claim is used as a proved input. The binding group
tests in Section 4 are algebraic failures of (LC); they need no
unproved transfer of a phase theorem between boundary conditions.

**PROVED by the author, not independently checked:**

| Statement | What was established | What remains |
|---|---|---|
| (E3)–(E7) | Standard centre substitutions; exact covariance of disjoint insertions; pointwise failure of positive sheet averages | Their Wilson-weighted mean |
| (E9)–(E12) | Negative odd link-crossing form; conditional magnetic-group selection | A small `theta` and a quantitative twist bound |
| (E13)–(E17) | Rank-four SU(2) classical cost between two positive size-independent constants | Finite-beta free energy and entropy |
| (LC), (E18)–(E20) | Exact small commutators, failing both comparison groups; obstruction to independent low-cost isotropic mixing | A correlated Wilson transport |
| (E21)–(E25) | Exact action-and-entropy test; polynomial lower cost for complete centre-orbit randomization | A family meeting (TR-F), or the stronger (TR-V) |

**OPEN after the three routes.** Sheet averaging preserves the
unknown expectation and its common covariance. Reflection
positivity supplies inequalities that consume that expectation
or the even seed. Continuous commutator spreading supplies
the algebraic distinction, but the explicit independent and
uniform-sign randomizations fail in the stated senses.
The fixed smooth-multiplication failure is prior work.
These are limited obstructions, not a refutation of (26).

The weakest sufficient statement remains (FQ). This note makes
one possible supplier concrete as (TR-F): for each crossed pair,
construct a correlated family of Haar-preserving transformations
from the actual Wilson variables and bound the **whole** value
of (E22), with the uniformity and tolerance printed there.
An alternative direct estimate of the same weighted expectation
could bypass transport. Neither is established. The hard missing
input is the action-and-entropy balance under the Wilson law,
not existence of small group elements or another auxiliary
commutator contraction. A proof using (LC) still has to connect
it to that balance; attaching the group property to an assumption
does not prove the connection.

For a subsequent check, the load-bearing new points are the
noncentral Stokes and incidence bound (E15), the entropy sign in
(E23), and the trial-cost lower bound (E25). The present author
has supplied hand arguments, not a second-provider check.
No numerical run, enumeration, interval enclosure or machine
certificate was used. Source searches and hashes are bookkeeping.
Search records and the two source downloads remain in
`/tmp/gap-ext-astra-20261112.ib8L4G/`.

Only this research note was written. It is local and uncommitted
on `research/gap-ext-astra-3b5f2007e`; HEAD remains at the source
pin. No audit, queue, registry, prior proof or status file was
changed, and nothing was posted or pushed.

RESULT: OPEN — (26), (V) and order-one (FQ)/(F-h) remain unproved; hand proofs bound the rank-four SU(2) classical cost between constants, give the group input (LC) that fails both comparison groups, and exclude the stated averaging shortcuts; the missing input is a Wilson-weighted correlated comparison meeting (TR-F), or an equally sufficient direct estimate.
