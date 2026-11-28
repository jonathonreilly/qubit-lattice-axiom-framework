# Repo search

The lead's `prior/repo-search-2026-11-08.md` records earlier history,
large-field and local-witness searches. Its relevant witness is
PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166`, relative to
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
I read that passage at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
It proves local finite-energy comparison and a transfer correlation
witness. It supplies the finite-energy method used below, but no
twist transport. The same PR's
`checks/review_massgap_block_literature.md:105–130` records the
Ito–Seiler common-endpoint warning. It is not a transport bound.

The closest inputs are Codex's exact cost identity (E22)–(E23)
in `gap-ext-astra.md:574–673`, checked by Claude Opus 5.5 in
`gap-ext-check-opus.md`, and the positive plaquette mean (T5)
in `gap-trf-astra.md`. I reuse them. The latter's small-displacement
theorem does not cover the large endpoint changes studied here.
Its triangular map and its failed supplier are not reconstructed.
The target-specific `prior/gap-seam-astra.md` does not exist.
The registry, `open-core.md` and `l17c.md` have no target match;
FINISH row 796 assigns this continuation. No other row is reopened.

## Contract and checkpoint

Author: **Codex gpt-6-astra max**, FINISH row 796, 2026-11-12.
Source pin: `5bc6c1fedada0354de1b15fe36b5d8db376f94ed`.
Research text, not an audit; this grants no status.
**PROVED** means a hand proof by the author, not an independent check.
**ARGUED** marks source interpretation; **GUIDE** supplies no proof;
**OPEN** marks a missing mathematical step.

Current main for the operating rules:
`bb4ec020d5ada57c630dd89acc98a68397ade423`.
The repository's physics-loop procedure is used within this single-file
assignment. No campaign, audit, publication or status update is run.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text**, for the outline and complete account.
Both prescribed sources were fetched once at `31a47c543775`, into
the new directory `/tmp/sa-gap-seam-astra.RyaWLr/`.
Their indices were searched before source excerpts were read.
Outline 26765–26805 assumes a common normalizer in (ET5) and proves
(ET6) from it. Lines 26848–26866 explain the comparison obligation;
27060–27086 give its conditional finite-reference/state application.
Those measures are not the present untwisted/twisted pair.
No theorem from those passages supplies this transport.

**ARGUED literature context.** `prior/gap-lit-transport.md` records
Mack–Petkova's thick-vortex criterion and the missing quantitative
vortex estimate. I use that record as route context, not as a newly
verified literature theorem. No Balaban estimate is used here.

**PROVED — current checkpoint.** Theorem 3 and Corollary 4 give
`C >= c_R a^2-log(32a^2)` for a centre seam followed by any
radius-`R` Haar transport of one colour, including arbitrary
mixtures of colours and flat seam positions. `R` is fixed as
`a` grows. The proof uses conditional density concentration,
not endpoint displacement. Corollary 5 gives necessary range
bounds when `R` varies. Overlapping colour updates and the
full multiscale supplier remain **OPEN**. No independent check
of this note has been run.

## 1. Consumer, cost and the seam

**PROVED input, reused.**

Use the torus `Lambda_a=(Z/aZ)^4`, with `a>=4`. Each unoriented
link has its positive orientation as a coordinate; a reverse
traversal uses its inverse. Count each plaquette once, for each
base and each unordered pair of distinct directions.

\[
 S_\eta(U)=\beta\sum_p(1-\eta_p s_p(U)),\qquad
 s_p(U)=\tfrac12\operatorname{tr}U_p,\qquad
 d\mu_\eta=Z_\eta^{-1}e^{-S_\eta}\,dU.
 \tag{S1}
\]

It suffices to test the required pair `(0,v_13)` on the cube.
Let `Sigma_0={p_13(x):x_1=x_3=0}` and
`eta_0(p)=(-1)^(1_(p in Sigma_0))`. Here the subscript 0 on
`Sigma_0` is its position; the untwisted law is denoted `mu_+`.
Set `F=-log(Z_(eta_0)/Z_+)`.
For any finite mixture of Haar-preserving measurable bijections,
with measurable inverses and field-independent probabilities,

\[
 \nu_j=(T_j)_*\mu_+,\quad \nu=\sum_j\pi_j\nu_j,
 \quad I_\pi=\sum_j\pi_jD(\nu_j\Vert\nu),
\]
\[
 \mathcal C=\sum_j\pi_j\mathbb E_{\mu_+}
       [S_{\eta_0}(T_jU)-S_+(U)]-I_\pi
       =F+D(\nu\Vert\mu_{\eta_0}),\quad F\ge0.
 \tag{S2}
\]

These are (E22)–(E23), not new identities. The supplier must obey

\[
 \mathcal C\le\varepsilon_a
 :=\min\{1/96,\ K(a)\eta_*^{a/2}/4\},\qquad
 0<K(a)\le C_1a^{p_1},\quad C_1>0,\quad 0<\eta_*<1/16,
 \tag{S3}
\]

uniformly on `I=[beta_-,beta_+] subset (0,infinity)`.
The weakest sufficient consumer remains (FQ), as stated in
`gap-trf-astra.md` Section 1. No stronger consumer is substituted.

**PROVED consequence of (E3), reused.** A centre cochain `b` acts by
`(B_b U)_e=(-1)^(b_e) U_e`. Let `Sigma_t` be another flat
representative, with `x_1=t_1,x_3=t_3`, and choose

\[
 \delta b=1_{\Sigma_0}+1_{\Sigma_t}\pmod2.
 \tag{S4}
\]

Such a cochain exists because these sheets represent the same class;
it can also be obtained by shifting one sheet a unit at a time.
The coboundary of the intervening strip is the pair of sheets.
For `T_j=B_b R_j`, the entire cost in (S2) equals the cost for
`R_j` with target `mu_(eta_t)`. Indeed

\[
 S_{\eta_0}(B_bV)=S_{\eta_t}(V),\quad
 (B_b)_*\mu_{\eta_t}=\mu_{\eta_0},\quad
 I_\pi((B_b)_*\nu_j)=I_\pi(\nu_j).
 \tag{S5}
\]

The first identity holds on every plaquette. The second follows
by Haar substitution, including equality of the partition functions.
The third follows by substituting in the defining density ratios.
The centre seam can therefore move links by order one; no small
displacement condition has been introduced at that seam.

Until Corollary 4, `nu` denotes the mixture of `(R_j)_*mu_+`
after this reduction, with target `mu_(eta_t)`. Corollary 4
returns to the original outputs and target `mu_(eta_0)`.

## 2. The finite-range class

**Definition.** For the obstruction take `a` divisible by four.
Failure on this unbounded subsequence defeats the uniform supplier.
Fix a direction `mu` and three parities `epsilon_nu`, `nu != mu`.
Let

\[
 A=\{e_\mu(x):x_\nu\equiv\epsilon_\nu\pmod2
                      \text{ for all }\nu\ne\mu\},\qquad W=E\setminus A.
 \tag{S6}
\]

Every plaquette contains at most one link of `A`. A map `R_j`
fixes `U_W=w` and is a Haar-preserving measurable bijection of
`SU(2)^A` for almost every `w`. Its inverse is measurable.
For each `e in A`, its output reads only the updated inputs

\[
 Q_{j,e}\subseteq A\cap B_R(e),\qquad
 |Q_{j,e}|\le M_R:=(2R+1)^4,
 \tag{S7}
\]

where `R>=1` is an integer and `B_R` uses the periodic coordinate
distance between link bases. We even allow arbitrary dependence
on the fixed exterior `w`. Ordinary radius-`R` dependence on all
fields is a subclass. The inverse need not have finite range.
There is no size bound on link changes or on the number of maps.
Maps may couple different links of `A` within their allowed range.

All maps in one class share `A`, the residual sheet `Sigma_t`,
and a common seam cochain in (S4). They need not share any formula.
The cochains are deterministic: they may depend on the label,
the lattice and beta, but not on the input field.
The mixture's labels can be correlated across the entire torus.
Only their probabilities must be independent of the input field.

A seam-first map `Q_j B_b` has this form too: write it as
`B_b R_j`, with `R_j=B_b^{-1}Q_jB_b`. This conjugation preserves
the fixed exterior, Haar preservation and the input-range bound.

The class permits arbitrarily many coherent (LC) factors, provided
their final map has these properties. It excludes composition of
updates of different colours. Such compositions are a substantive
remaining escape, even at fixed finite depth.

## 3. All plaquettes, the density, and the information term

**PROVED.** Condition on `U_W=w`. Because no plaquette contains
two links of `A`, the untwisted conditional law is a product:

\[
 p_A(u\mid w)=\prod_{e\in A}p_e(u_e\mid w),\qquad
 p_e(g\mid w)=\frac{e^{\beta\ell_{H_e(w)}(g)}}
                         {\int e^{\beta\ell_{H_e(w)}(h)}dh},
 \quad \ell_H(g)=\tfrac12\operatorname{Re}\operatorname{tr}(gH).
 \tag{S8}
\]

Here `H_e` is the sum of the six oriented staples. A staple is
the product of the other three links in an incident plaquette,
with the orientation that makes its action term `ell_H(U_e)`.
SU(2) traces are real; the real part also fixes the convention.
The target conditional law is `q_A=prod_(e in A) q_e`, with
`H_e` replaced by `H_e^t`, the signed staple sum. Write
`P_A={p: boundary p meets A}`. Then exactly

\[
 S_{\eta_t}(R_ju,w)-S_+(u,w)
 =\beta\sum_{p\notin P_A}(1-\eta_{t,p})s_p(w)
  +\beta\sum_{e\in A}
       \{\ell_{H_e}(u_e)-\ell_{H_e^t}((R_{j,w}u)_e)\}.
 \tag{S9}
\]

Each affected plaquette occurs in exactly one staple sum.
Every unaffected plaquette occurs in the first sum, where its
term vanishes unless the target sign changes. No term is omitted.

Let `rho_W` be the untwisted exterior marginal density. The actual
output densities before the common centre substitution are

\[
 \rho_j(v,w)=\rho_W(w)f_j(v\mid w),\qquad
 f_j(v\mid w)=p_A(R_{j,w}^{-1}v\mid w),\quad
 f=\sum_j\pi_j f_j.
 \tag{S10}
\]

In particular the exterior marginal remains `rho_W` and

\[
 I_\pi=\int\rho_W(w)dw
       \sum_j\pi_j\int f_j(v\mid w)
                 \log\frac{f_j(v\mid w)}{f(v\mid w)}\,dv.
 \tag{S11}
\]

Formula (S10) uses the actual inverse, even if that inverse is
nonlocal. It does not assert that `f_j` or `f` factorizes.
The proof of (S10) is Haar substitution on each fixed exterior
fibre; (S11) follows by cancelling `rho_W`. Thus (S2), (S9)
and (S11) account for the entire cost together.

## 4. A local cancellation of the six staples

**Lemma 1 — PROVED.** There is a central exterior configuration
`w^*` for which `H_f(w^*)=0` for every `f in A`. If `e in A`
belongs to a sheet plaquette, then

\[
 H_e^t(w^*)=-2z_e I,\qquad z_e\in\{1,-1\}.
 \tag{S12}
\]

*Proof.* Set every link in directions other than `mu` to `I`.
For direction-`mu` links in `W`, set

\[
 w^*_{e_\mu(y)}
   =(-1)^{\sum_{\nu\ne\mu}\lfloor(y_\nu-\epsilon_\nu)/2\rfloor}I.
 \tag{S13}
\]

This is periodic: changing a coordinate by `a` changes the
exponent by `a/2`, an even integer. For `f=e_mu(x) in A`,
the parallel neighbours `e_mu(x+nu)` and `e_mu(x-nu)` are in
`W`. Their signs are opposite. Indeed, with
`x_nu-epsilon_nu=2k`, the two relevant floors are `k` and
`k-1`. The two transverse links in each staple equal identity.
Thus the two staples in each of the three transverse directions
cancel. This proves `H_f=0` without specifying any link of `A`.

A link of `A` on `Sigma_t` belongs to exactly one negative
plaquette of the target. Its other five incident plaquettes
have positive target sign. Changing the sign of that one staple,
whose value is `z_e I`, changes the zero sum to `-2z_e I`.
This proves (S12). QED.

The cancellation is a displayed central configuration, not a
machine search. Its neighbourhood, rather than this null event,
will carry the probability bound.

**Lemma 2 — PROVED.** Define

\[
 c_0(t)=\int e^{t s(g)}dg,\quad
 m(t)=\frac{\int s(g)e^{t s(g)}dg}{c_0(t)},\quad
 s(g)=\tfrac12\operatorname{tr}g,\quad m_*=m(2\beta_-)>0,
\]
\[
 \delta_R=\min\left\{\frac1{12},
       \frac{\log(1+m_*/4)}{36\beta_+M_R}\right\},\quad
 v_R=\operatorname{Haar}\{g:\|g-I\|_{\rm op}<\delta_R\}>0,
\]
\[
 p_R=e^{-216\beta_+M_R}v_R^{18M_R},\qquad
 d_R=\frac{p_Rm_*^2}{8}>0.
 \tag{S14}
\]

For each `e in A` on the sheet, there is an exterior event `E_e`
with `mu_+(E_e)>=p_R` such that, conditionally on every such
exterior outside a `mu_(+,W)`-null set, the output marginal
of `V_e` under any mixture in
Section 2 differs from `q_e` by relative entropy at least
`m_*^2/8`.

*Proof.* Haar symmetry under `g -> -g` gives
`int s e^(t s)=int s sinh(t s)>0` for `t>0`.
Differentiation gives `m'(t)=Var_t(s)>0`. Therefore
`m(2 beta)>=m_*>0` on `I`. The Haar ball has positive measure:
finitely many translates of it cover the compact group.

Take `Q_e=A cap B_R(e)`, containing every allowed `Q_(j,e)`.
Let `F_e` be the exterior edges of the six staples of all
`f in Q_e`. These are all in `W`, with `|F_e|<=18M_R`.
Let `E_e` require every edge in `F_e` to be within `delta_R`
of its prescribed value in (S13), or of identity in another
direction. Products of three unitaries telescope, so on `E_e`

\[
 \|H_f(w)\|_{\rm op}\le18\delta_R\quad(f\in Q_e),\qquad
 \|H_e^t(w)+2z_eI\|_{\rm op}\le18\delta_R.
 \tag{S15}
\]

Under (S8), the joint input density on `Q_e` lies between
`exp(-theta_R)` and `exp(theta_R)` relative to product Haar,
where

\[
 \theta_R=36\beta_+M_R\delta_R,\qquad
 e^{\theta_R}-1\le m_*/4.
 \tag{S16}
\]

This uses `|ell_H(g)|<=||H||_op` both in the numerator and
the normalizing integral, then multiplies over `Q_e`.

For fixed `w` outside the common null set of the finitely many
maps, Haar preservation of the entire fibre map makes
its one-link output Haar when all inputs in `A` are Haar.
That output only reads `Q_e`. Hence the map from the Haar inputs
in `Q_e` to its output link also has Haar law. Pushing the two
density bounds through this map preserves them. The same bounds
hold after any mixture, however many labels or correlations it
uses. With `phi_e(g)=-z_e s(g)`, Haar has mean zero, so

\[
 |\mathbb E_{\nu_e(\cdot\mid w)}\phi_e|
       \le e^{\theta_R}-1\le m_*/4.
 \tag{S17}
\]

The ideal target density at (S12) is proportional to
`exp(2 beta phi_e)` and has `phi_e` mean `m(2 beta)`.
By (S15) the actual target density divided by this ideal one
lies between `exp(-36 beta_+ delta_R)` and
`exp(36 beta_+ delta_R)`. Its mean changes by at most
`exp(theta_R)-1`. Consequently

\[
 \mathbb E_{q_e(\cdot\mid w)}\phi_e\ge3m_*/4,
 \qquad
 D(\nu_e(\cdot\mid w)\Vert q_e(\cdot\mid w))
       \ge m_*^2/8.
 \tag{S18}
\]

For completeness, a test in `[-1,1]` whose means differ by
`h` gives `TV>=h/2`. Data processing to a set attaining TV
reduces entropy to Bernoulli entropy. Its second derivative
in its first argument is `1/[t(1-t)]>=4`, and its value and
first derivative vanish at equality. Thus `D>=2 TV^2>=h^2/2`.
Here `h>=m_*/2`. Approximating the maximizing set gives the
same bound if necessary.

Finally, each link in `F_e` touches six plaquettes. At most
`108M_R` plaquettes meet `F_e`. Condition on all other links
in the untwisted Wilson law. The log density on `F_e`, relative
to product Haar, has oscillation at most `216 beta_+ M_R`.
The normalized density is therefore at least its negative
exponential. The Haar probability of `E_e` is
`v_R^(|F_e|)>=v_R^(18M_R)`. This proves
`mu_+(E_e)>=p_R`. No independence between different events
`E_e` is asserted or needed. QED.

## 5. The whole cost of a centre seam and one colour

**Theorem 3 — PROVED.** Fix `I` and `R` before taking `a` large.
Let `r_I=kappa_I/54>0` be (T3)–(T5) of `gap-trf-astra.md`.
Here `kappa_I=min_(beta in I) log c_0(beta)/beta`.
For every mixture of Section 2, on every cube with `4 | a`,

\[
 \boxed{\quad \mathcal C\ge c_R a^2,\qquad
 c_R=\min\{2\beta_-r_I,\ d_R/4\}>0.\quad}
 \tag{S19}
\]

The constant is independent of the seam position, the number of
maps, their probabilities, and their formulae. It can be very small.
It is uniform in `beta in I` and strictly positive for each fixed `R`.

*Proof.* Work after the common centre substitution (S5).
Suppose first that `mu` is 1 or 3. Exactly `a^2/4` links of
`A` belong to sheet plaquettes: the parities of coordinates 2
and 4 select `a/2` choices each; the remaining transverse
parity selects one of the two parallel links of each such
13-plaquette. No other link of `A` belongs to the sheet.

The relative-entropy chain rule, retaining the exterior, gives

\[
 D(\nu\Vert\mu_{\eta_t})
 =D(\mu_{+,W}\Vert\mu_{\eta_t,W})
  +\int\mu_{+,W}(dw)\,D(f(\cdot\mid w)\Vert q_A(\cdot\mid w)).
 \tag{S20}
\]

For any joint probability `f` with marginals `f_e`, and a product
reference `q_A=prod q_e`, splitting the logarithm proves

\[
 D(f\Vert\textstyle\prod_e q_e)
 =D(f\Vert\textstyle\prod_e f_e)+\sum_eD(f_e\Vert q_e)
 \ge\sum_eD(f_e\Vert q_e).
 \tag{S21}
\]

All densities here are positive and bounded on each finite torus,
so this identity has no infinite-entropy subtraction. Applying
Lemma 2 to each sheet link in `A`, then integrating, gives

\[
 D(\nu\Vert\mu_{\eta_t})
       \ge\frac{a^2}{4}\,p_R\frac{m_*^2}{8}
       =\frac{d_Ra^2}{4}.
 \tag{S22}
\]

Events can overlap; (S21), not independence of events, adds the
bounds. Correlation between output links contributes a nonnegative
first term in (S21). This includes correlation from the common label.
Equation (S2), with `F>=0`, now proves this case.

If `mu` is 2 or 4, the map changes no edge of a sheet plaquette.
Thus `E_nu s_p=E_(mu_+)s_p>=r_I` on the entire sheet.
The equivalent form (E21) of the cost gives

\[
 \mathcal C
  =2\beta\sum_{p\in\Sigma_t}\mathbb E_\nu s_p
       +D(\nu\Vert\mu_+)\ge2\beta_-r_Ia^2.
 \tag{S23}
\]

This proves (S19). The information subtraction has already been
included through (S2); none of it is replaced by a guessed label
entropy. QED.

**Corollary 4 — PROVED; all flat seam positions and colours.**
Each map may choose its own one of the 32 colours (S6), its own
flat residual sheet, and any centre cochain satisfying (S4).
The radius bound is the common `R`. Then

\[
 \boxed{\quad \mathcal C\ge c_Ra^2-\log(32a^2).\quad}
 \tag{S24}
\]

In particular the class fails even the ceiling `1/96` for all
sufficiently large `a` divisible by four.
Indeed `log(32a^2)<=5+2a<=4a` for `a>=4`; taking also
`a>=8/c_R` makes (S24) at least `c_R a^2/2>1/96`.

*Proof.* Group labels by their colour and residual sheet, into
at most `32a^2` groups. Within one group fix a cochain `b_g`
satisfying (S4). Another cochain is `b_j=b_g+c_j`, with
`delta c_j=0`. The map `B_(c_j)` preserves both product Haar
and `mu_+`, since it changes no plaquette trace. Therefore

\[
 (B_{b_j}R_j)_*\mu_+
 =(B_{b_g}\widetilde R_j)_*\mu_+,\qquad
 \widetilde R_j=B_{c_j}R_jB_{c_j}^{-1}.
 \tag{S25}
\]

Conjugating in this way still fixes `W`, preserves Haar on each
fibre and retains (S7). Thus Theorem 3 applies to the actual
conditional mixture in each group, with cost `C_g>=c_Ra^2`.
Each component output law is unchanged in (S25). Its target-action
mean and all within-group density ratios are therefore unchanged.

Let `w_g` be the group probabilities and `nu_g` their output laws.
Splitting the label information through the group gives exactly

\[
 \mathcal C=\sum_g w_g\mathcal C_g-I(G;V),\qquad
 I(G;V)=\sum_gw_gD(\nu_g\Vert\nu)\le H(w)\le\log(32a^2).
 \tag{S26}
\]

The first inequality follows pointwise from
`d nu_g/d nu <= 1/w_g`; zero-weight groups are omitted.
For the second, `D(w || uniform)>=0` gives `H(w)<=log G`.
These are lower bounds on the cost, so subtracting the upper
bound on this *group* information is legitimate. Information
within each group was already handled exactly in Theorem 3.
This proves (S24). QED.

**Corollary 5 — PROVED; a necessary growing range.** The same
bounds hold when `R=R(a)` varies, with the displayed constants
evaluated at that radius. Put

\[
 k_I=\min\{1/12,\ \log(1+m_*/4)/(36\beta_+)\},\quad M=M_R,
\]
\[
 L_I=216\beta_++18\log(6\pi/k_I^3)+54
       +\log(32/m_*^2)+\max\{0,\log(1/(2\beta_-r_I))\}.
 \tag{S24a}
\]

Then `c_R>=exp[-L_I M log(e M)]`. Consequently, a family in
one fixed colour/seam class satisfying (TR-F) must obey

\[
 L_I M_R\log(eM_R)\ge 2\log a-\log\varepsilon_a
 \ge \tfrac12\log(1/\eta_*)a
        +(2-p_1)\log a+\log(4/C_1).
 \tag{S24b}
\]

For the full mixture of Corollary 4, even its constant ceiling
requires

\[
 L_I M_R\log(eM_R)
       \ge2\log a-\log\{\log(32a^2)+1/96\}.
 \tag{S24c}
\]

In particular, no uniformly bounded updated-input range can
supply (TR-F) within this architecture. These estimates do not
require a numerical value for the constants.

*Proof.* The SU(2) Haar angle density, also used in
`gap-pag-grow-astra.md:803–806`, is `(2/pi) sin^2(theta) dtheta`.
It follows from polar coordinates on the unit quaternion sphere;
`int_0^pi sin^2(theta)dtheta=pi/2` fixes its normalization.
The angle interval `0<=theta<delta_R` lies in the operator-norm
ball, since `2 sin(theta/2)<=theta`. On this interval
`sin(theta)>=theta/2`. Hence

\[
 v_R\ge\delta_R^3/(6\pi)\ge k_I^3/(6\pi M^3),
\]
\[
 d_R/4\ge(m_*^2/32)
   \exp\{-216\beta_+M-18M\log(6\pi/k_I^3)-54M\log M\}.
 \tag{S24d}
\]

Using `M log(eM)>=M` and `M log(eM)>=1` shows that (S24a)
bounds both branches in the minimum defining `c_R`. Insert
that lower bound into (S19) or (S24) and rearrange. The second
inequality in (S24b) uses `epsilon_a<=C_1 a^(p_1) eta_*^(a/2)/4`.
This proves the claims. QED.

**PROVED scope.** This exclusion permits order-one changes at
the original seam and at every updated link. It permits arbitrary
coherent accumulation and arbitrary common random labels. It is
not a consequence of the small-endpoint assumption (SD).
The new restriction is finite input range *within one fixed
plaquette-independent colour per map*, with the other links fixed
after the common seam has been removed by (S5).

**OPEN scope.** A product of two different colour layers need
not belong to this class. Nor need a map that changes a connected
block of links, a field-dependent centre cochain, or a relaxation
of unbounded radius. The theorem does not prove that every
finite-range transport fails. In particular it does not establish
that successful (TR-F) maps must be nonlocal on the whole torus.

## 6. An explicit field-dependent relaxation, and where it stops

**PROVED construction; failed supplier.** The obstruction is not
merely a restriction to fixed link multiplications. One actual
local relaxation aligns the source and target staples. A nonzero
real quaternion matrix `H` has the form `H=h V`, with
`h=||H||_op>0` and `V in SU(2)`. This follows directly from
`H^*H=h^2 I`. Write `H_e=h_e V_e` and `H_e^t=k_e W_e`.
For each link of one colour set

\[
 (R U)_e=W_e(w)^*V_e(w)U_e\quad(h_e k_e>0);
 \qquad (R U)_e=U_e\quad(h_e k_e=0).
 \tag{S27}
\]

All controls use the fixed exterior. Their inverse left
multiplications give a measurable inverse, and conditional Haar
invariance proves Haar preservation. This is an actual shear
family, with bounded range and unrestricted endpoint displacement.

For `h_e k_e>0`, its output conditional density is proportional
to `exp(t ell_(W_e)(g))`, where `t=beta h_e`. The target density
has the same axis and parameter `s=beta k_e`. Its conditional
relative entropy is exactly

\[
 d(t,s)=(t-s)m(t)-\log c_0(t)+\log c_0(s).
 \tag{S28}
\]

Strict convexity of `log c_0` makes this positive unless `t=s`.
For `h_e=0`, the output stays Haar and its conditional entropy
against a nonuniform target is `log c_0(s)>0`.

This shear does not increase expected target action. The source mean
matrix is `m(t)V_e^*`, by Haar symmetry around its quaternion
axis. The target staple term has means `k_e m(t)` after the
rotation and `k_e m(t) Re tr(V_e^*W_e)/2` before it. Their
difference is nonnegative. Summing these conditional differences
uses each affected plaquette once, as in (S9).
Nevertheless Theorem 3 bounds its *remaining* whole cost below
by `c_R a^2`. Alignment has not supplied the missing concentration.

**GUIDE, not a supplier.** Overlapping colour sweeps can move
conditional concentration from neighbouring links and evade this
proof. After the first sweep their source density is (S10), not
the original product (S8). Reusing the six-staple source formula
at the next colour would change the actual law. Exact conditional
means can instead be defined from the composed inverse density;
their local form, cost reduction and iteration have not been bounded.

## 7. What each scale must pay

**PROVED accounting; OPEN estimates.** Choose a centre seam first.
For a finite number `J` of later scales, choose all path labels
`alpha` with field-independent joint probabilities `Pi_alpha`.
Correlations between scales are allowed. Each specified path
composes Haar bijections. Let `U_s(alpha,U)` be its field after
scale `s`, with `U_0=B_bU`, and let `lambda_(alpha,s)` and
`lambda_s` be its component and mixed laws. Define

\[
 I_s=\sum_\alpha\Pi_\alpha
                  D(\lambda_{\alpha,s}\Vert\lambda_s),\qquad I_0=0,
\]
\[
 C_s=\mathbb E_{\Pi,\mu_+}
          [S_{\eta_0}(U_s)-S_+(U)]-I_s.
 \tag{S29}
\]

Every cumulative map preserves Haar, so (E23) gives
`C_s=F+D(lambda_s || mu_(eta_0))`. Subtracting successive
expressions gives the exact bill at scale `s`:

\[
 b_s:=C_s-C_{s-1}
   =\beta\sum_p\eta_{0,p}\,
       \mathbb E_{\Pi,\mu_+}[s_p(U_{s-1})-s_p(U_s)]
        -(I_s-I_{s-1}).
 \tag{S30}
\]

The sum includes every plaquette touched at that scale, with
zero terms on the others. It retains the current law and the
full path information. A change of scale notation is no reason
to discard the plaquettes crossing a block boundary.

For the bare seam with a flat residual sheet,

\[
 C_0=2\beta a^2\mathbb E_{\mu_+}s_p\ge2\beta_-r_Ia^2,
 \qquad C_J=C_0+\sum_{s=1}^J b_s.
 \tag{S31}
\]

Thus a sufficient scale-by-scale supplier would give explicit
upper bounds `b_s<=B_s`, on these actual laws, satisfying

\[
 C_0+\sum_{s=1}^J B_s\le\varepsilon_a.
 \tag{S32}
\]

If its cumulative map after the first relaxation is covered by
Corollary 4, all later
scales together must reduce the cost by at least
`c_R a^2-log(32a^2)-epsilon_a`. Bounds only on the squared
sizes of inserted commutators do not estimate this negative bill.

To verify the information convention, put
`H(lambda)=-int rho_lambda log rho_lambda dU`. Haar preservation
gives `H(lambda_(alpha,s))=H(mu_+)`, including the seam. Splitting
the logarithm therefore gives `I_s=H(lambda_s)-H(mu_+)`.
With correlated path labels, `I_s-I_(s-1)` can have either sign.
For example choose a fair identity/nontrivial centre substitution,
then undo the same choice: the final information is zero, while
the intermediate information is positive if the two laws differ.
If instead each stage chooses a fresh independent label and its
map depends only on that label, the entropy increase at that stage
equals its fresh-label/output mutual information. Neither version
permits replacing information by the entropy of all available labels.

**OPEN.** No bounds `B_s` satisfying (S32) are supplied here.
This is exact accounting, not a new weaker assumption than (TR-F).
The unclosed estimate concerns a concrete overlapping-colour or
block construction, on its evolving densities, that removes the
area-size initial cost and leaves the exponentially small remainder.
It must use (LC), or another stated input absent in both controls.

## 8. Binding tests and the remaining escape

**PROVED input, reused.** (LC) supplies arbitrarily small
nontrivial SU(2) commutators whose coherent product is `-I`.
It fails for U(1), where every commutator is identity. In the
binary icosahedral group the strictly positive minimum of
`1-tr(g)/2` over `g != I` forces both (LC) generators to identity
for sufficiently large `N`. These are the already checked tests
in `gap-ext-astra.md` Section 4.2.

**PROVED scope of the new negative result.** Theorem 3 did not
use (LC). Its near-Haar obstruction also applies to the analogous
colour class in U(1) and in the binary icosahedral group: both
contain the centre signs, and the relevant identity neighbourhood
has positive Haar measure. This is an exclusion, not a confinement
supplier. It makes no assertion that the groups have the same phase.
The staple-alignment construction (S27) is likewise not a successful
supplier and is not offered as a group-specific mechanism.

**OPEN, exact next step.** Allow successive changes of different
colours, or genuine connected-block maps, so that the near-Haar
input argument cannot freeze one exterior throughout. Supply the
composed inverse densities and prove (S32), uniformly on `I`,
for every crossed pair and required shape, with the two binding
failures. A lower bound covering *all* fixed-range maps would
also advance the task, but is not proved by (S19)–(S24).
Unrestricted (TR-F), the weighted exterior estimate (26), and
order-one (FQ) remain **OPEN**.

## 9. Search record and scope check

**ARGUED source classification.** A targeted search was run on
main and PRs 10114, 10133, 10134 and 10141, outside this lane.
It searched staple cancellation, near-Haar laws, conditional
concentration, colour transports and finite-range transports.
The complete query and outputs are in `search-record.json` and
the five `*.search.txt` files in the scratch directory above.
The exact revisions were:

| Ref | Commit |
|---|---|
| main | `bb4ec020d5ada57c630dd89acc98a68397ade423` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `fb99b4dddc7254e6124ac124887d58eeb3a77802` |

The read concentration hits were main's
`docs/FINITE_ENERGY_SECTOR_SELECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md:1–90`
(a supplied Fock-space energy bound) and PR 10114's
`CODEX_REVIEW_NODEA.md:1–35` in the directory named at the top
(a conditional column-energy obstruction). Neither is this
transport theorem. Other hits were triaged as colour-matrix
transport, operator response or unrelated finite-range operators;
no claim about all their proofs is made. In this lane,
`gap-pag-grow-astra.md:780–806` already uses the six-plaquette
finite-energy bound for a different correlation witness. That
bound is credited; the new steps are the simultaneous cancellation
(S13), its propagation through a finite-input Haar map, and (S22).
This search supplies no exhaustive absence theorem.

The outline index's conditional-density hit leads to GL14,
lines 2475–2498: a conditional layer density retaining every
incident plaquette. Its Haar/seam hit leads to line 7913:
contour Haar coordinates and a gauge delta integral. Both passages
were read after their neighbouring index rows; neither treats a
centre-twist transport. The CA-I index's seam hit at 53358–53380
was likewise read at source: it imposes local background gauges
on a seam-enlarged cube class, a different object. The searches
for vortex/twisted-partition/centre-twist transports found no
target entry in the supplied outline and CA-I indices. No
proof is being ported from these passages.

**ARGUED author scope check, not an independent check.**

- **N1, family.** Equations (S4), (S6) and (S7), with fixed `R`,
  finite field-independent mixtures and `4 | a`, quantify the
  excluded family. Lemma 2 treats every map in each class;
  Corollary 4 treats every mixture of those classes.
- **N2, dependencies.** The fixed exterior and single-colour
  product conditional law form one restriction. They are not
  advertised as independent barriers.
- **N3, premises.** Compact SU(2), normalized product Haar,
  the finite Wilson law, the pure twist and `I` are explicit.
  No decay-of-correlation hypothesis, phase assumption, map
  regularity or computational certificate enters. The prior
  positive plaquette mean is used only for
  directions 2 and 4.
- **N4, prior scope.** (E22)–(E23) supply the identical cost.
  (T5) supplies the identical untwisted cube mean. (T7)/(T9)
  concern small displacement and are context, not a proof of
  the new exclusion. No rank-four classical bound is imported.
- **N5, resolution.** The local conditional mismatch is (S18).
  The lattice cost follows through (S20)–(S22), without assuming
  independent events. No assertion is made for all local circuits.
- **N6, assumptions.** No axiom, interpretation or new physical
  identification is proposed. This is a statement about the
  explicitly supplied Wilson measures.
- **N7, strongest escape.** An overlapping colour sweep can
  change the exterior which made the first fibre nearly Haar;
  a connected block can draw on nonuniform plaquette variables
  inside that block. Those maps can have fixed finite range and
  fall outside this theorem. They still owe the signed bill
  (S30) on the composed density, with (S32) and both binding tests.
- **N8, earlier exclusions.** Coherent large displacements evade
  row 793's small-endpoint bound, but not this single-colour
  theorem. A composition of colours is a different escape;
  it is preserved, not counted as another failed route.

No audit packet or status is generated. The next useful independent
check is Lemmas 1–2, the conditional entropy sum in Theorem 3,
the cochain grouping in Corollary 4, and the radius constants
in Corollary 5.
The new proof rests on no numerical run, machine enumeration,
symbolic calculation or computer-assisted certificate.

**Recovery.** Only this note was written in the checkout.
The downloads have 32,992 and 166,711 lines; their hashes are in
the scratch directory's `source-manifest.json`. Search and hash
scripts performed bookkeeping only. The note is local and
uncommitted on `research/gap-seam-astra-5bc6c1fed`; nothing was
posted or pushed. No queue, registry, previous proof or audit
file was changed.

RESULT: PROVED by hand, not independently checked — a centre seam followed by a fixed-range Haar transport of one plaquette-independent link colour, with arbitrary field dependence allowed on its fixed exterior and arbitrary mixtures of colours and flat seam positions, has whole cost at least c_R a^2-log(32a^2) and fails (TR-F) for large a divisible by four; overlapping-colour and general block transports, unrestricted (TR-F), (26) and order-one (FQ) remain OPEN.
