# Repo search

The task-specific `prior/gap-mixed-check-astra.md` is absent at the pinned
commit. The lead's November 8 digest was read. It concerns older RG
obligations, with a finite-clock Villain result on main and a local
transfer witness on PR 10114. The closer search record at
`gap-gamma2-astra.md:1–38` already covers main and PRs 10114, 10133,
10134 and 10141. This check reused those locators and opened these sources:

| Source checked | Closeness |
|---|---|
| Main `bb4ec020d5`, `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:79–94` | Finite-clock covariance, prior input behind the reused Villain obstruction; not the Wilson slice gap. |
| Same main, `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md:370–482` | Existing finite-product Dobrushin comparison with total variation and soft normalizers; not the chord slice estimate. |
| PR 10114 `f76f6c649c`, soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | Positive one-step loop correlation, not a volume-uniform gap. Credit its Codex author. |
| PR 10133 `89faef229f`, soft-route `MASS_GAP_CW_CROSSOVER_ATTACK.md:115–174` | Grok branch's prior six-staple sphere law and transverse moment; its parallel-variance bound is left open. Not this theorem. |

The soft-route paths start at
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
The reused local inputs are the Codex notes `gap-vmf-lip.md`,
`gap-gamma2-astra.md`, `gap-tu-retry.md`, and the explicitly conditional
comparison with `gap-shape-exercise-astra.md`. The comparison method is
Dobrushin's. Their named earlier checks are by Claude Opus 5.5; a source
label is not itself evidence for the present check.

Searching `open-registry.md`, `open-core.md`, and `l17c.md` for the target,
Langevin, Dobrushin, plaquette-code, forest and mixed-Hessian terms found
no competing owner of this check. The mixed box-Hessian hit H-C3a is an
RG source-budget statement, not this diffusion form. FINISH row 818 also
records a straight-line gauge/Dobrushin novelty caveat. Its external
Hexagon comparison was not checked here; this report claims no novelty.

The outline index README, matching neighbouring rows and obligations were
consulted before source excerpts. The tree-Haar identity is already proved
at outline 7660–7681; it is reused below. Outline 3712–3720 concerns the
transfer plateau and says no gap above its invariant subspace was proved.
CA-I 47602–47635, located through `ca-4.12-4.19/chunk-04.md:100–102`,
is a conditional coercivity argument at the trivial prepared background,
not a Langevin gap. Searches of the index and both downloaded texts for
Dobrushin, Langevin, Villain, mixed-Hessian, plaquette-code and von Mises
terms produced no target match. These bounded comparisons are not a claim
of exhaustive absence elsewhere in the account.

Provenance: OpenAI/Codex, gpt-6-astra, xhigh (dispatch configuration),
2026-11-12; source commit `38209f9b1f080663d354440b0c20a67ea65ad4a7`.
This is a research check of Claude Opus 5.5's `gap-mixed-opus.md`, not an
audit. It grants no status. Source line numbers below refer to that file.

## Checkpoint

Complete. Read the complete source note and checked the requested
finite-dimensional arguments by hand. The gap bounds survive. Corrections
concern the exceptional-torus constants, the domain and proof of the
forest ceiling, invariant-gradient realizability, and two influence-scope
sentences. Only this output file is edited. The order-one gap, continuum
limit, claimed numerical GUIDE runs, and the unproved sharp upper bound
on the mixed Hessian were not checked or supplied. The Villain obstruction
is reused as a named existing input; its full dependency closure is not
rechecked. Next action: the source owner may apply the corrections below.

Outline and CA-I were each downloaded once to the fresh scratch directory
`/tmp/sa-gap-mixed-check-astra.IHqdUC/`, at source revision `31a47c543775`.
Credit for those texts belongs to Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. No estimate of Tadeusz Balaban
is imported; his original papers were not needed for this check.

## Verdicts

### 1. Lemma S and the slice kernels — HOLDS

Lines 18–40. The rooted forest gives a unique gauge transformation, with
one independent Haar coordinate per forest edge. Solving successively
along each tree proves the asserted smooth product parametrization and
measure identity. Each fixed gauge transformation is an isometry.
Restriction to the slice retains precisely the non-forest components of
the gradient. Thus

\[
 \operatorname{Var}_\mu f=\operatorname{Var}_{\mu_F}f_F,
 \qquad E(f)\ge E_F(f_F),\qquad
 \gamma_{\rm inv}(\mu)\ge\gamma(\mu_F).
\]

This last inequality is the precise comparison; the slice's unrestricted
gap is a *lower bound* for the original invariant gap. The section title
must not be read as the reverse inequality.

Lines 36–40 preserve the one-link conditional law. Every period is at
least two, as in the inherited convention, so each indexed plaquette
contains four distinct link variables. Fixing forest links to one leaves
a linear quaternion field. One moving neighbour changes each incident
staple by its chord displacement. Corollary V1 of `gap-vmf-lip.md`,
209–220, therefore gives `C_ek <= beta n^F_ek/4`, including multiplicity
two at period two. This is an upper bound, not a claim of equality for
every exterior. Fixed center signs preserve both conclusions.

The Haar decomposition is already in Sussman–Alpoge, outline 7660–7681,
Proposition 1a.3.3, located through `sa-index/chunk-07.md:116–118`.
That prior identity supplies S(i)–(ii); the Dirichlet-form comparison is
the additional step checked here. Credit Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text.

### 2. Lemma W — HOLDS

Lines 46–62. A direct continuous-time check fixes the transpose and the
constant. Put `A=sum_i(I-Pi_i)`, so `K=I-A/N`. The coordinate
seminorm estimate gives

\[
 \Delta_w(e^{-tA}f)
 =\Delta_w\!\left(e^{-Nt}\sum_{k\ge0}\frac{(Nt)^k}{k!}K^kf\right)
 \le e^{-(1-\alpha)t}\Delta_w(f).
\]

Here `delta(Kf)<=R^T delta(f)` and `Rw<=q w`; hence it is `Cw`, not
`C^T w`, that must be bounded. The chord diameter gives
`osc(g)<=2 Delta_w(g)/min w`. For centered smooth functions this bounds
the semigroup in supremum norm. Its positive spectral measure consequently
has no mass below `1-alpha` for `A`. Density of smooth functions in
`L^2(mu)` extends the form inequality to that space. Equivalently,

\[
 \sum_i\mu(\operatorname{Var}_i f)\ge(1-\alpha)\operatorname{Var}_\mu f.
\]

Integrating each conditional Poincare inequality proves W(c). The
field-uniform constant two is supplied by the conditional tensor-square
identity in `gap-gamma2-astra.md:229–259`: the Bochner form is at least
`(2/3)||Hess u||^2+2|grad u|^2`. Hence the claimed lower bound is
`2(1-alpha)`. No assumption of invariant test functions is needed on the
slice. The bracketed sharper constant three is not used by this check.

### 3. Theorem A and its constants — HOLDS AFTER CORRECTION

The theorem and its proof, lines 64–88, **HOLD** for the inherited periods
`n_mu>=2`. The forest consists of disjoint open time paths. Counting
indexed plaquettes, rather than distinct neighbours, handles period two.
For an interior spatial link the count is
`12w_t+w_(t-1)+w_(t+1)`; for an end spatial link it is
`12w_end+w_other_end+w_inner+2a`; a closing link has
`6w_0+6w_(T-1)+6a`. The displayed weights bound these by `16w_e`.

An independent hand test is the thinnest permitted exceptional case of
this construction, `(3,2,2,2)`. Its three link classes have ratios
`(12+2+2)/1=16`, `(24+2+1+5)/2=16`, and
`(12+12+15)/(5/2)=78/5<16`. Repeated spatial neighbours count twice,
exactly as required by the conditional-field estimate. For `T>=4`,
the ratios are at most `16,16,15`; for `T=4` the two interior levels
are distinct, so neither gets two end weights. Thus `alpha=4 beta`.

On `(Z/2)^4`, there are `6*16=96` indexed plaquettes and the oscillation
of the potential is at most `192 beta`. Density comparison with the Haar
product gap three gives `3 exp(-192 beta)`. Thus the theorem's stated
minimum is uniform over all permitted tori on each compact subinterval.

The rational constants at lines 90–100 also **HOLD on tori with a period
at least three**: at `b_+=6/25`,

\[
 \lambda_*=2/25,\quad 24b_+=144/25,\quad
 \delta=1/146,\quad\theta=145/146,\quad\kappa=1/25.
\]

The rewrite has `2-kappa=49/25`, as printed. But the summary at line 248
puts these constants after the all-tori statement without its exception.
Correct it to: **The displayed constants `theta=145/146`, `kappa=1/25`
are proved when some period is at least three. For all tori use**

\[
 \lambda_*=\min\{2/25,3e^{-1152/25}\},\quad
 \delta=\frac{\lambda_*}{2(\lambda_*+144/25)},\quad
 \theta=1-\delta,\quad\kappa=\lambda_*/2.
\]

This corrects the supplied scope; it does not refute stronger constants
on the one exceptional torus. It leaves the interval `beta<1/4` intact.

### 4. Lemma P, its line structure, and Theorem B — HOLDS

Lines 106–144. The six projection rows are correct. As a separate parity
check, choose the first word in each `A_mu`. On the two coordinates
complementary to each plane, the XORs for its two participating directions
are respectively `(0,1),(0,1),(0,1),(1,0),(0,1),(1,0)`.
An antipodal pair in two bits is determined by its XOR. Thus the two
projections are complementary in every plane, proving the exact cover
without enumerating a torus. The construction is well defined for every
even period, including two.

Two selected links in different directions meeting at a vertex would
belong to one plaquette, contradicting that cover. Selection in direction
mu is invariant under translation in mu. Every selected link therefore
lies on a whole straight cycle, and different such cycles have disjoint
vertices. The directional density is `2/8`, so their total edge count is
`|V|`. Each vertex has at most one selected outgoing edge; averaging
then makes this exactly one. This proves the asserted line partition.
Every unselected link has six plaquettes with two other unselected links,
giving the occurrence count twelve.

The defect construction, lines 126–130, also **HOLDS**. The four
coefficients `1,3,9,27` are coprime to `82=2*41`. Each straight cycle
therefore meets Gamma. Removing its selected edges breaks every cycle.
For separation, let a periodic difference `z` have every coordinate at
most two in absolute value. The congruence and `2(1+3+9+27)=80<82`
force `z_1+3z_2+9z_3+27z_4=0` as an integer. Reducing modulo three
forces `z_1=0`; division by three and repetition forces all digits zero.
Thus distinct Gamma points have periodic maximum-coordinate distance
at least three. A link sharing plaquettes with two defects would put their
base points at distance at most two. They must coincide. Periods at least
82 also ensure a pair of distinct links shares at most one plaquette.

For weights `r` on defects and one elsewhere, the three ratios are

\[
 18/r,\qquad 12,\qquad 12+r.
\]

At `r=4/3`, their maximum is `27/2`; thus `alpha=27 beta/8`.
The minimum over positive `r` occurs where the decreasing and increasing
ratios meet. Solving `r^2+12r-18=0` gives

\[
 r=3\sqrt6-6,\qquad B=6+3\sqrt6,\qquad
 \beta<\frac4B=\frac23(\sqrt6-2).
\]

These are optimal for the displayed two-level row-sum estimate, not a
claim of the optimal weight vector among all possible weights. The gap
with these weights is `2(1-beta B/4)`.

The downstream constants at lines 156–160 **HOLD**: `b_+=2/7` gives
`lambda_*=1/14`, `24b_+=96/14`, `delta=1/194`, `theta=193/194`,
`kappa=1/28`, and `2-kappa=55/28`. The unoptimized endpoint is
`8/27`; the expression containing `sqrt(6)` is the optimized endpoint.
No GUIDE enumeration is needed for any of these facts.

### 5. Forest-count ceiling — HOLDS AFTER CORRECTION

The count at lines 148–150 **HOLDS for every forest**. If `x_p` counts
its edges in plaquette `p`, the ordered pairs of remaining edges number
`(4-x_p)(3-x_p)`. For integer `x_p`,

\[
 (4-x_p)(3-x_p)=12-6x_p+x_p(x_p-1)\ge12-6x_p.
\]

There are `6|V|` plaquettes, each link has six occurrences, and
`|E\setminus F|=4|V|-|F|`. Therefore

\[
 \frac{\sum_{e,k}n^F_{ek}}{4|V|-|F|}
 \ge12+\frac{24(|V|-|F|)}{4|V|-|F|}>12.
\]

For the source theorem's class (all periods at least three; no plaquette
has three forest links), its sharp-influence argument **HOLDS**.
Here is the needed independence justification: the six staples at a fixed
link have disjoint sets of the other link variables. Each retains at least
one free variable. Set all but one free variable in each staple to one,
then choose the last one to make the signed staple `+1` or `-1`.
Choose three of each. At this exterior the field is zero. Moving a shared
free neighbour has field velocity of norm beta; the linear chord test in
that direction has derivative `beta/4`, since Haar covariance is `I/4`.
Together with (A2), this identifies every nonzero optimal coefficient as
`beta/4`. The symmetric incidence matrix has spectral radius at least its
average row sum, by its Rayleigh quotient on the constant vector. Thus
for positive beta, every positive weight vector has maximum ratio
strictly larger than `3 beta`. At beta zero the ratio equals zero;
the strict assertion in line 146 needs **beta>0**.

The count by itself is not an influence lower bound. The table at line
241 and final line 261 should retain the proven domain: **all periods
at least three**, with the no-three-forest-edges condition if using only
the source's written proof. This is a limit of a worst-exterior sufficient
criterion, not a limit of the actual invariant gap.

A short completion removes that last forest condition, without any
search. A staple with all three edges in the forest is a forest path
between the endpoints of the omitted link. There can be at most one:
two distinct such paths would create a cycle. If it exists, keep its
fixed signed value and choose the other five staples to make a total
of three `+1` and three `-1`. The same disjoint-variable and derivative
argument applies to every moving neighbour. Consequently the ceiling
actually extends to **every forest when all periods are at least three**.
This supplies the justification missing from the unrestricted forest
summary and resolves the no-three-edge qualification left open at line
231. It makes no sharp-influence claim for period-two pairs.

### 6. The mixed-Hessian configuration — HOLDS

Lines 164–178. Let `a=(1,-1,-1,1)`. The listed signs are precisely
`s_(mu nu)=a_mu a_nu`. Their product construction is periodic on every
even torus and gives those six plaquette signs, including at period two.
At the central configuration the quadratic form is
`beta sum_(x,mu<nu) s_(mu nu)|(dX)_(mu nu)(x)|^2`.
For the staggered field, `dX=2(-1)^(sum x)(a_mu-a_nu)T`.

There are four unlike-sign pairs and two like-sign pairs. Thus the
signed sum of squared differences is `-4*4=-16`; the additional curl
factor four gives `-64 beta` per vertex. Since `|X|^2=4|V|`, the full
Hessian quotient is `-16 beta`. At each link, the diagonal Hessian is
`2 beta sum_(nu!=mu)s_(mu nu)=-2 beta`. Subtraction gives

\[
 \beta M_{U_c}(X,X)=-14\beta|X|^2.
\]

The divergence is, up to the harmless sign convention,
`2(-1)^(sum x)(sum_mu a_mu)T=0`. Adjoint transport at a central link
is identity, so these are exactly the gauge-orbit orthogonality equations.
The claimed horizontal vector and value both hold.

**Invariant gradients (line 180): HOLDS AFTER CORRECTION of the argument.**
The path printed there lies in a common circle subgroup and need not
be generic. Horizontalness alone at its singular endpoint does not
establish realizability by invariant gradients. The following direct
test supplies the missing justification, with no genericity assumption.
Put `A(U)=sum_p(1-q_p)`, a smooth invariant function, and
`U(t)=U_c exp(tX)` link by link. In the staggered Fourier subspace, for
any real direction vector `b`, the signed quadratic form is

\[
 4\sum_{\mu<\nu}a_\mu a_\nu(b_\mu-b_\nu)^2
 =-4(a\cdot b)^2,
\]

using `sum a_mu=0`. Thus `Hess A(U_c)X=-16X`, and `grad A(U_c)=0`.
In smooth parallel coordinates along this path,

\[
 \nabla A(U(t))=-16tX+O(t^2),\qquad
 \frac{M_{U(t)}(\nabla A,\nabla A)}{|\nabla A|^2}
 \longrightarrow -14.
\]

The denominator is nonzero for all sufficiently small nonzero `t`.
Therefore no pointwise bound with coefficient below fourteen can hold
even when restricted to invariant gradients. This explicit invariant
test replaces the unsupported generic-point sentence. It does not
give a small Rayleigh quotient or disprove an integrated inequality.

**Route C consequence, line 182: HOLDS as the stated conditional ceiling.**
Keeping only its reserves `3E` and `(9/8)E` and a uniform pointwise
bound `C_m>=-c beta E` gives coefficient `33/8-c beta`, where
`c>=14`. Its positivity cannot extend beyond `33/112` by improving
that pointwise constant alone. The endpoint comparison is exact:
`8/27-33/112=5/3024>0`. This is conditional on D1 and C4 as the source
says; those stronger inputs are not independently checked here.

### 7. Villain binding test — HOLDS AFTER CORRECTION

The implication at lines 190–197 **HOLDS**, using the existing Theorem V
of `gap-tu-retry.md:61–101,333–345`. This check reads its model and
conclusion; it does not re-prove its underlying covariance theorem.
Its conclusion is the full limit `gamma_V(beta;M)->0` at each fixed
`beta>=2^14`, including odd `M`.

Tree gauge fixing works for circles. On any forest slice each one-link
conditional potential has oscillation at most
`6 osc(log phi_beta)`. The Haar circle gap one and density comparison
give the exterior- and volume-independent constant

\[
 c_V(\beta)=\exp[-6\operatorname{osc}(\log\phi_\beta)]>0.
\]

The same diameter-two weighted Lipschitz argument proves Lemma W on
circles. If a fixed `alpha<1` worked along infinitely many cubic sizes,
then S and W would give `gamma_V>=c_V(beta)(1-alpha)>0` on that
subsequence, contradicting the full limit. This identifies S4, a
**uniform strict row-sum margin**, as a required failure. It does not
identify S1 or the single-link Poincare inequality as a failure.

Two sentences need the precise scope:

- Line 251 must say: **For each fixed `alpha<1`, only finitely many
  cubic sizes admit forests and weights with maximum row sum at most
  that alpha.** The argument does not exclude contraction factors
  `alpha_M<1` approaching one on arbitrarily large individual tori.
- Line 199 must replace “`beta/4` per neighbour for every exterior” by
  **a uniform upper bound `beta/4` per plaquette occurrence, attained
  at suitable zero-field exteriors in the class proved above**.
  At nonzero field, Theorem V supplies the smaller local constant
  `a(|h|)<1/4`. For example, use the untwisted law, empty forest and
  all-identity exterior on `(Z/4)^4`. For beta positive, a moving
  neighbour has derivative bounded by
  `beta a(6 beta)<beta/4`. The strict inequality follows because the
  tilt strictly increases the longitudinal second moment above `1/4`.

The Villain Gaussian-response discussion is labelled ARGUED and is not
used to prove the binding test. Its heuristic weighted-count estimate
does not replace the preceding contradiction argument.

### 8. Exact block identity and its conditional use — HOLDS

Lines 207–213. All off-block sums in (A8) are over **ordered** pairs.
For distinct links, product geometry gives commuting derivatives and

\[
 \mu(L_e f\,L_j f)
 =\mu\langle\nabla_e f,\nabla_e L_j f\rangle
 =\mu\|\nabla_j\nabla_e f\|_{\rm HS}^2
   +\mu\,\operatorname{Hess}_{ej}S(\nabla_e f,\nabla_j f).
\]

The first equality uses the positive-generator convention. In the second,
the commutator of `grad_e` with `L_j` differentiates the j-drift,
giving the **positive** mixed-Hessian term. Expanding
`||sum_B L_B f||_2^2` now gives (A8). A one-block partition returns
`Q=mu((Lf)^2)`; a singleton partition returns the previously stated C5.
These checks fix both the sign and the absence of an extra factor two.

Condition on the exterior of B. If the block gap is bounded below by
`gamma_B`, conditional spectral expansion gives
`mu((L_B f)^2)>=gamma_B mu(|grad_B f|^2)` after integration.
This pays for the internal terms. It leaves the cross-block terms in
(A8) untouched. The source supplies no order-one estimate for them;
the identity alone is not such an estimate.

### 9. Remaining consequences and summary scope

The specific-heat consequence at lines 217–221 **HOLDS** for the ordinary
Wilson measure, `0<beta<1/4`, and a period at least three. With
`A=sum(1-q_p)`, integration of `L_beta A` and `Delta A=12 sum q_p`
give `E(A)=12|P|p'/beta` and `Var(A)=|P|p''`. Applying Theorem A
therefore gives exactly `p''<=6p'/(beta(1-4 beta))`.

The sufficient-criterion statement at line 227 **HOLDS**, with the
finite exceptional torus handled separately as in Theorem A. The limits
at line 229 **HOLD** with the domains and fixed-reserve restriction in
Sections 5–6 above. The assertion that the order-one estimate and a slow
mode remain unconstructed is faithful to the written arguments.

The claims of optimal mixed-Hessian constant fourteen, approach to
`beta=1/3`, arbitrary-even-torus defect construction, and bulk-transition
literature context remain outside the proved conclusions. GUIDE runs were
not reproduced or used as proof. No assertion of a continuum mass gap,
physical identification, or retained scientific status follows here.

## Disposition

| Statement | Verdict |
|---|---|
| S(i)–(iv), slice conditional laws, influence upper bound | HOLDS |
| W(a)–(c), including the constant `2(1-alpha)` | HOLDS |
| Theorem A, axial weights, exceptional-torus comparison | HOLDS |
| A's explicit curvature constants in the all-tori summary | HOLDS AFTER CORRECTION: retain the exceptional-torus minimum |
| P, straight-line structure, mod-82 defects, Theorem B and both endpoints | HOLDS |
| Theorem B's curvature constants | HOLDS |
| Average forest count strictly above twelve | HOLDS |
| Sharp-influence ceiling and its unrestricted summary | HOLDS AFTER CORRECTION: positive beta, periods at least three, and the unique-path argument above |
| Central configuration, horizontal field, mixed quotient `-14 beta` | HOLDS |
| Extension to invariant gradients | HOLDS AFTER CORRECTION: use the explicit invariant action gradient |
| `33/112` ceiling with Route C's specified reserves | HOLDS, conditional on those reserves |
| Villain binding test and its summary | HOLDS AFTER CORRECTION: keep one fixed contraction margin |
| Wilson `beta/4` assertion at every exterior, line 199 | FAILS as an equality; the corrected uniform upper bound HOLDS |
| Block identity and conditional block-gap implication | HOLDS |
| Specific-heat consequence | HOLDS |

No numerical proof, audit, source edit, registry edit, or external post was
performed. This report is local and uncommitted on
`codex/gap-mixed-check-astra-20261112`; no push was requested.

RESULT: The stated gap ranges HOLD, with the scope and proof corrections above; the universal-exterior equality at line 199 FAILS; the forest ceiling holds for all forests with periods at least three, the -14 beta obstruction and block identity hold, and the Villain obstruction excludes a uniform contraction margin; order one remains OPEN.
