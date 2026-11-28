# Further operator walks with component-Laplacian endpoint bounds

Ethan and Levent,

This note supplies the graph-endpoint estimates stated below for the further operator walks of Tadeusz Balaban, CMP 99b §3, after Theorem 3.9. Your list at [CA-I 166595–166596](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L166595-L166596) records these walks as printed without proof. The result follows our issue #13 on the bare covariance inverse. It supplies the displayed bounds on the PI background class; it does not supply every operator or every domain in that list.

All references to your account and outline use commit `31a47c543775`. The outline means `YM4_sketch_500.tex` at the same commit. CA-I and CA-III denote `theorem_0_complete_account_raw_I.tex` and `theorem_0_complete_account_raw_III.tex`. We use your labels `4.5:lem-free-current-operators`, `4.5:eq-higher-order-functional-a`, and `4.5:prf-chart-walk-localisation`.

## Scope and inputs

Use [Theorem PI from issue #13](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/94df5579a/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-pi.md), with its literal corner rows, no-inward row convention, compressed whole-action Hessian, local models, and normalized cutoffs. Fine field bonds touch $`\Omega_0`$; scalar sites lie in $`\Omega_0`$. Zero extensions are used. The background read includes all protruding plaquettes, on $`\Omega_0^+`$.

Write $`W=e^{i\eta\mathfrak a}U_r`$, with $`U_r`$ unitary. We require PI's (S1-loc), (S2), and (S2+) on the entire coefficient read. In (S1-loc), each prescribed box carries one unitary gauge with

```math
U_r^u=e^{i\eta A},\qquad m|A|,\ m^2|\partial A|\le L^2a_0.
```

Condition (S2) bounds the complex twist and its first covariant difference by $`a_1`$, with weights $`m,m^2`$. Condition (S2+) imposes these bounds on the additional exterior read, at scale $`\eta`$. A proper outer boundary still needs the supplied real gauges. This note does not deduce them from (S1).

The constants are chosen together with PI's constants. Before choosing the tile size $`M_t`$ and the background radii, enlarge PI's inverse, comparison, and cutoff bounds to cover all the norms used below. This does **not** assert the bounds for an arbitrary earlier numerical choice of PI's constants. The torus floor is

```math
\operatorname{side}(T_\eta)\ge
\max\{2\widehat r+2,\ t_FM_F\}\ell_k.
```

Here $`M_F,t_F`$ are the flat-model constants; $`\widehat r=(2L+2)M_t`$. Both flat and actual tower gaps must satisfy the summation floors below. The independent current obeys $`|J|_{(-3)}\le j_*`$; no derivative of $`J`$ is assumed. The ceiling $`j_*`$ is fixed before the switch radius $`e^{\kappa_1}`$. The field radius may depend on $`\kappa_1`$.

**Primitive tags.** We use your rule at [CA-I 15266–15310](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L15266-L15310), `4.5:prf-chart-walk-localisation`. Expand each primitive into its walks. Expand its defining series into concatenations with all side branches, before inserting parameters. Each primitive term receives one factor $`\sigma(\Delta)`$ per distinct cube met by its full localization domain. Form composites afterwards. Thus the factors of $`H_0(\sigma)=G_0(\sigma)Q^Tq_0(\sigma)\ell^{-1}`$ retain their own primitive tags. Balaban gives this rule in CMP 116, (1.6), and after (1.7). We include all local insertion carriers and cutoff reads in the domains. For an identity piece, use $`I=\sum_\tau h_\tau^2I`$ with the scalar-component cutoffs. Your text does not fix this identity decomposition; it is part of the choice here. It recovers $`I`$ at $`\sigma\equiv1`$.

The proof uses the following inputs which your account does not itself prove. They are stated here before the argument.

1. **Theorem PI.** We use its four mixed inverses, literal row estimates, local coefficient comparison, model geometry, and setting-compatible walk assignment. We also use its bare $`q_0`$ estimate and spare exponential factors. The linked note proves these under the hypotheses above. It supplies the input of your `4.5:rem-covariance-inverse-walks`; it does not supply the unrestricted S1–S2 assertion.

2. **Flat estimates.** For each of the four systems $`M_1,M_3,M_4,M_5`$, use the flat inverse and local periodic or bare-boundary models. Their energy expansions have the following absolute refinement: the sum of norms of all length-$`n`$ words from either endpoint patch is at most $`B_Lq^n`$, where $`q<1/2`$. Each transition has a fixed layer diameter $`D`$. These constants are uniform in mesh, volume, depth and admitted shape. We use physical row and column counts, and the free local Poisson estimate (P7), including its divergence-source and Hölder members. The flat construction precedes the main tile size. The strong inverse (P8) is derived below from these inputs. These estimates are proved in the [working note on the flat propagators](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/18d805bed/.claude/science/physics-loops/ym4d-hard-route-20261030/library/flat-port.md): §4.1 for (P7), §§8 and 9.2 for the inverse, §11 for the absolute word bounds, and §12 for the torus room $`t_FM_F`$. Codex (GPT-6) wrote it, and Claude (Opus 5.5) checked it line by line. Appendix A of the PI note prints its energy part. The free Poisson estimate (P7) and the absolute word bounds are not in the PI note. The argument rebuilds the flat method of Balaban, CMP 95, Proposition 1.1 and (1.89)–(1.90), and CMP 96, (2.95)–(2.141), Propositions 2.5–2.6. The input includes absolute individual-word bounds, not just a bound on the summed remainder.

3. **Averaging estimates in a supplied frame.** Use the literal straightened averaging map of Balaban, CMP 98, pp. 23–24, (42)–(43), as in PI. His Proposition 5, (156)–(157), bounds its first derivatives at real backgrounds. We need the analytic form at complex backgrounds, with second and third derivatives and transposes. Balaban states that extension without proof (CMP 98 §E, p. 43). Your Remark `4.5:rem-averaging-analyticity`, CA-I 13175–13196, cites it as printed. We use a written proof of it as an implication from a frame bound: the [working note on the averaging derivatives](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/18d805bed/.claude/science/physics-loops/ym4d-hard-route-20261030/library/b98p5.md), §§2.1–2.5. Codex (gpt-6-astra) wrote it. Claude (Opus 5.5) checked it line by line, and its two repairs are applied. It rebuilds Balaban's map and his real-background method, and moves the reference without a factor that grows with depth. Its constants depend only on N and L. Its first-derivative constant is larger than the leading coefficient $`1+2C'_1\alpha_0`$ of (156); no step here needs a coefficient near one. Its §3, on the frame bound for your full class, is not used. It proves the following implication. Let $`c`$ be a row of scale $`s_c`$, and let $`E_c`$ contain all bonds of its double block. If one unitary gauge gives
$`W^u=e^{i\eta B}\quad\hbox{on }E_c,\qquad s_c\|B\|_{\infty,E_c}<\rho,`$
then its dimensionless angle $`q_c(W,A)`$ and remainder
$`R_c(W,A)=q_c(W,A)-D_Aq_c(W,0)A`$ are jointly holomorphic in the reference potential and increment on a common larger ball. With $`r_A=|A|_{(-1)}`$, $`r_v=|v|_{(-1)}`$, and $`r_h=|h|_{(-1)}`$, the estimates used are
$`\begin{aligned} |R_c(W,A)|&\le Cr_A^2,\qquad R_c(W,0)=D_AR_c(W,0)=0,\\ |D_Aq_c(W,A)(b)|_{\rm den}&\le Cs_c^{-3}1_{E_c}(b),\\ |D_AR_c(W,A)(b)|_{\rm den}&\le Cr_As_c^{-3}1_{E_c}(b),\\ |D_A^2R_c(W,A)[v,\cdot](b)|_{\rm den}&\le Cr_vs_c^{-3}1_{E_c}(b),\\ |D_A^3R_c(W,A)[h,v,\cdot](b)|_{\rm den}&\le Cr_hr_vs_c^{-3}1_{E_c}(b),\\ |(D_A^2R_c(W,A)-D_A^2R_c(W,0))[v,\cdot](b)|_{\rm den} &\le Cr_Ar_vs_c^{-3}1_{E_c}(b). \end{aligned}`$
A counting-coordinate derivative is $`\eta^4`$ times this density. The same colour bounds hold for bilinear transposes. The physical transpose sums the density with row volume $`s_c^4`$. Adjacent-height carrier overlap is bounded, so it gives the corresponding weighted transpose estimates. In particular a block field of weight $`-4`$ gives a fine source of weight $`-3`$, with the marked variation in $`E_p`$. The first derivative gains $`r_A`$; the difference of second derivatives gains $`r_A`$. Cauchy estimates are applied to a density-bounded row on the larger ball, before summing fine coordinates. The remainder at height zero is zero.

**The frame bound is supplied on this PI class.** A positive-height double block lies in the (S1-loc) box $`N_\tau`$ of a tile of height $`j-1`$ or $`j`$ whose cutoff support contains its base point. PI Lemma 5.2, using (S2) and (S2+) as well, gives

```math
s_c\|B\|_{\infty,E_c}\le C_{N,L}(a_0+a_1).
```

Choose $`a_0,a_1\le a_*\le\rho/(16C_{N,L})`$, including norm conversions, and put the increment ball within the same margin. Thus the frame bound is not an additional hypothesis on this class. The averaging estimates themselves remain the input implication of item 3, proved in the linked working note. No assertion about carriers on the full account class is used.

The local Wilson estimates are proved in §7 below, including the step from real to complex backgrounds. They use Balaban's plaquette expansion, CMP 102b, (39) and (94)–(98). The kernel and current identities already proved in your account are used as such. In particular, we use your decomposition at CA-I 13811–13846, not the printed Hölder bounds cited there as a substitute for word estimates.

Your bibliography at CA-III 111519–111544 gives the following paper names. The abbreviations refer to Balaban's *Propagators and renormalization transformations for lattice gauge theories. I* (CMP **95**, 17–40), part II (CMP **96**, 223–250), *Averaging operations for lattice gauge theories* (CMP **98**, 17–51), *Propagators for lattice gauge theories in a background field* (CMP **99**, 389–434; CMP 99b), *The variational problem and background fields in renormalization group method for lattice gauge theories* (CMP **102**, 277–309; CMP 102b), and *Renormalization group approach to lattice gauge field theories. II. Cluster expansions* (CMP **116**, 1–22). The citations here use the quotations and formulas in your account and the working proofs. Balaban's original pages were not checked for this note.

**Limits.** The individual uses of these bounds in your account were not checked one by one. Admission of your account's localized and completion domains is not certified. The result does not identify a general-field response with your completion maps. It does not prove termwise lattice covariance, a boundary gauge-gluing theorem, or a graph bound for $`G_\pi^J`$ or $`G_1^J`$. It does not cover an older unspecified word assignment merely because its sum at one agrees. The stronger endpoint estimates below are not a claim that your whole walk proposition or account is complete.

Codex (gpt-6-astra) wrote the proof. Claude (Opus 5.5) checked it line by line; its repairs are applied. The flat input was written by Codex (GPT-6) and the averaging input by Codex (gpt-6-astra); Claude checked each line by line. Codex prepared this outward note from the proof.

Claude (Opus 5.5) checked this note line by line against the working proof.

This is model-checked research text, not an audit, and grants no status. No computer-assisted step discharges an assertion. The [full working note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ba4304ff6/.claude/science/physics-loops/ym4d-hard-route-20261030/library/walks-gw.md) records the proof and its source references.

## Objects and norms

Use PI's scales $`\eta=L^{-k}`$, $`\ell_j=L^j\eta`$, and put $`m=\ell`$ at each local cell. The cell includes every endpoint stencil. Use the lattice-contour distance $`d`$ of PI, extended to cell anchors; write $`d^\wedge`$ for that cell distance in weighted estimates. The weight is a positive admitted $`p`$ with

```math
p(z)\le e^{\delta d^\wedge(y,z)}p(y).
```

Only this ratio is used in the estimates. Any additional admission conditions of a consumer's weight class still apply. The constant weight is admitted. Define

```math
\begin{split}
N_y(A)&=\max\{\ell_y|A|_y,\ell_y^2|\nabla_WA|_y\},\\
N_y^\Delta(A)&=\max\{N_y(A),\ell_y^3|\Delta_WA|_y\},\\
\|A\|_p&=\sup_y N_y(A)/p(y),\quad
\|A\|_p^\Delta=\sup_y N_y^\Delta(A)/p(y),\\
|f|_{-3,p}&=\sup_y\ell_y^3|f|_y/p(y),\qquad
|b|_p=\sup_y|b|_y/p(y),\qquad N(A)=\|A\|_1.
\end{split}
```

These define $`E_p,E_p^\Delta,F_p,B_p`$, respectively: first-order fields, graph-norm fields, sources, and dimensionless block data. The Laplacian is the component covariant Laplacian, as in your outline 10246–10254, not the Wilson Hessian. Bilinear fine pairings have measure $`\eta^4`$; row pairings have measure $`\ell_j^4`$. The multiplier $`\nu`$ in PI has counting pairing. Write $`|J|_{-3}=|J|_{(-3)}`$.

Use $`M_1,M_3,M_4,M_5`$ exactly as in PI §3.1. For clarity their five-variable system is

```math
M_5=\begin{pmatrix}
B_v&-D_W&0&0&-K^T\\
-D_W^T&I&A_s&0&0\\
0&A_s&0&-Q'^T&0\\
0&0&-Q'&0&0\\
-K&0&0&0&0
\end{pmatrix},\quad
A_s=D_W^TD_W+Q'^Tm^{-2}Q',\quad
B_v=\Delta(W)+D_WD_W^T+Q^TaQ,
```

where $`K=mQ`$, $`K^T=Q^Tm^{-3}`$, $`a=m^{-2}`$, and $`\Delta(W)`$ here is the Wilson Hessian. The other systems are its indicated submatrices in PI. In proof formulas $`U`$ can denote the same background $`W`$; $`U_r`$ always denotes the unitary reference.

At $`\sigma\equiv1`$, your definitions at CA-I 13543–13798 give

```math
\begin{gathered}
G'=A_s^{-1},\quad P=G'Q'^T(Q'G'^2Q'^T)^{-1}Q'G',\quad R=I-P,\\
G_0=(\Delta(W)+D_WRD_W^T+Q^TaQ)^{-1},\quad
q_0=(QG_0Q^T)^{-1},\\
H_0=G_0Q^Tq_0\ell^{-1},\quad
B_0=G_0-G_0Q^Tq_0QG_0=\tilde{\mathfrak G}_0,\\
\Lambda=G'RD_W^T,\quad
\Theta'_J=\mathfrak k_J\Lambda+\Lambda^T\mathfrak j_J+
\Lambda^T\mathfrak m_J\Lambda,\\
G_\pi^J=(I-G_0\Theta'_J)^{-1}G_0,\quad
q_J=(QG_\pi^JQ^T)^{-1},\quad H^J=G_\pi^JQ^Tq_J\ell^{-1},\\
\langle A,\Theta_JA\rangle=2\langle H^JC^{(2)}(\ell A),J\rangle,
\qquad G=\widetilde G^J=(I-B_0\Theta_J)^{-1}B_0.
\end{gathered}
```

Here $`B_0`$ is an operator, not a norm constant. These are Balaban's operators from CMP 99b, (3.116)–(3.138), and CMP 102b, (129), (131), with your independent current. To fix the local current terms, set

```math
c^{(1)}(A,\lambda)(b)=\frac i2[\lambda(b_-)+\operatorname{Ad}(W_b)\lambda(b_+),A(b)],\qquad
c^{(2)}(\lambda,\lambda)(b)=\frac1{2i}[\lambda(b_-),D_W\lambda(b)],
```

```math
\langle\lambda,\mathfrak j_J(A)\rangle
=\langle A,\mathfrak k_J(\lambda)\rangle
=\langle c^{(1)}(A,\lambda),J\rangle,\qquad
\langle\lambda_1,\mathfrak m_J\lambda_2\rangle
=2\langle c^{(2)}(\lambda_1,\lambda_2),J\rangle.
```

The last expression uses polarization. The nonlinear average $`C`$ and its quadratic term $`C^{(2)}`$ are distinct from $`c^{(2)}`$. At switches, all symbols mean the primitive sums and composites specified above. None of the inverse identities is asserted for switched sums.

Write $`S A=\ell A`$, $`H=H^J(\sigma)`$. Define $`D(A)`$ as the small branch of

```math
D(A)=C_\sigma(SA-SHD(A)),\qquad
\mathfrak D=D_AD,\quad D_3=D-C^{(2)}(SA),\quad
\mathfrak D_3=D_AD_3,\quad \mathsf k=(q_J-a)\ell^{-1}.
```

The source is your seven-term expression `4.5:eq-higher-order-functional-a`, CA-I 14156–14375:

```math
\begin{split}
V'_\sigma(A)={}&-\mathfrak D_3^TH^TJ-Q^T\mathsf kD
-\mathfrak D^T\mathsf k^TQA+\mathfrak D^T\ell^{-1}\mathsf kD\\
&+(I-H\mathfrak D)^T\nabla V_0(A-HD)
-\Lambda^T\mathfrak j_J(HD)-\mathfrak D^TH^T\mathfrak k_J(\Lambda A).
\tag{N}
\end{split}
```

Here $`V_0`$ is the Wilson action remainder of order at least three, as at CA-I 14136–14155. The small-branch definition follows your `4.5:lem-nonlinear-correction`, CA-I 13980–14084. Its existence and the required absolute series bounds at switches are proved in §7. Balaban's sources are CMP 102b, (50)–(58), (63)–(73), (80), (85), (87)–(98). Formula (N) is used literally after switching; a symmetry or inverse identity valid only at one is not substituted.

**Theorem (endpoint walks with a common choice of PI constants).**
Fix $`SU(N)`$, odd $`L\ge3`$, and a fixed ceiling $`0<\beta_0<1`$ for the
Hölder exponents used in the current insertions. There is a choice of
PI's constants, and positive constants $`\delta_*,a_*,j_*`$, with the
following properties.

The choice retains PI's literal corner rows, no-inward convention,
compressed whole-action Hessian, tile models and normalized cutoffs.
It makes PI's flat inverse, coefficient-comparison and cutoff constants
large enough to cover the stronger norms (P1)--(P2) below **before**
choosing $`M_t`$ and the background radii. The torus has side at least

```math
\max\{\,2\widehat r+2,\ t_FM_F\,\}\ell_k.                 \tag{T1}
```

The flat-model gap and the actual tower gap satisfy the summation floors
in the proof. The background satisfies (S1-loc), (S2), (S2+) on the
entire coefficient read, with $`a_0,a_1\le a_*`$. The independent current
satisfies $`|J|_{-3}\le j_*`$. Its derivatives are unrestricted.

For every $`\kappa_1\ge0`$, choose the common decoupling-cube side,
in units of the largest scale, at least
$`\max\{4\widehat r+8L,c_\iota,64\kappa_1/\mu\}`$, where $`\mu>0`$ and the insertion range $`c_\iota`$ are fixed
in section 5, with the required grid divisibility. There are
$`C_{\kappa_1}<\infty`$ and $`r_{\kappa_1}>0`$, uniform in depth,
mesh, volume, admitted tower, background and weight, such that for
every admitted weight with rate
at most $`\delta_*`$, every $`|\sigma|\le e^{\kappa_1}`$, and every
$`N(A)\le2r\le2r_{\kappa_1}`$,

```math
\begin{split}
\|H_0(\sigma)b\|^\Delta_p
&\le C_{\kappa_1}|b|_p,\\
\|G(\sigma)\Theta_J(\sigma)u\|^\Delta_p
&\le C_{\kappa_1}|J|_{-3}\|u\|_p,\\
\|D(G(\sigma)V'_\sigma)(A)u\|^\Delta_p
&\le C_{\kappa_1}r\|u\|_p .                       \tag{T2}
\end{split}
```

Here $`G=\widetilde G^J`$, and $`V'_\sigma`$ is the seven-term function
of (N), with its inner small branch. Every line has an
absolute expansion into the indicated words and local analytic vertices.
More precisely, its endpoint graph readouts admit nonnegative cell
majorants $`k_\omega(y,z)`$, including the source measures and scale
factors, for which

```math
\sup_y\sum_{\omega,z}
|\sigma_\omega|\,k_\omega(y,z)
e^{\delta_*d^\wedge(y,z)}
\le C_{\kappa_1}(1,\ |J|_{-3},\ r),                    \tag{T3}
```

respectively. For a composite, $`\sigma_\omega`$ is the product of its
prescribed primitive tags. Each primitive tag counts every visited cube
once. The same assertion holds if a whole composite is instead tagged
by its union, without identifying that alternative with the account.
The tails have these bounds tending to zero, locally uniformly on the
analytic domain.

The words have PI's complete footprints, including the reads of the
cutoff coefficients. Restrictions to common complete footprints are
setting-compatible. The result applies to a localized or completion
domain whenever that domain supplies the stated PI hypotheses and full
reads. It does not certify admission of every domain used in your account.

The theorem uses the common constant choice just specified. It does not
assert the stronger conclusion for an arbitrary previously fixed
numerical choice that was checked only in PI's energy norms.
For the identity part of a primitive such as $`R=I-P`$, the assignment
is $`I=\sum_\tau h_\tau^2I`$, with PI's scalar-component cutoffs
and full footprints. This fixes that part of the switched operator
as well; a sharply tagged pointwise identity is not substituted.

## Proof

### 1. Strong source spaces, rather than the energy dual

For the five variables $`X=(A,h,\lambda,\mu,\nu)`$, define a norm $`Z`$
by the supremum of the following local quantities:

```math
\begin{array}{c|l}
A&m|A|,\quad m^2|\nabla A|,\quad m^3|\Delta_{\rm comp}A|\\
h&m^2|h|,\quad m^3|\nabla h|,\quad m^4|\Delta_{\rm comp}h|\\
\lambda&|\lambda|,\quad m|\nabla\lambda|,\quad
m^2|\Delta_{\rm comp}\lambda|\\
\mu&m^4|\mu|\\
\nu&|\nu|.
\end{array}                                                   \tag{P1}
```

The differences are covariant at the fixed real reference. For
$`F=(f,g_1,g_2,g_3,g_4)`$, define $`V`$ by

```math
\|F\|_V=\max\{
|m^3f|_\infty,\ |m^2g_1|_\infty,\ |m^4g_2|_\infty,\
|g_3|_\infty,\ |g_4|_\infty\}.                            \tag{P2}
```

Delete unused components for $`M_3,M_4`$. For $`M_1`$, scalar output
power $`a`$ means the three sizes
$`m^a|u|,m^{a+1}|\nabla u|,m^{a+2}|\Delta u|`$, and source size
$`m^{a+2}|f|`$. The scalar powers needed below are $`a=0,2`$.
Finite common shifts of the mixed powers are handled by the scale
summation below. The field component of $`Z`$ is the required graph
norm at the fixed real reference. If the consumer writes its full
complex background $`W`$ in that norm, the comparison in section 3
converts it with a uniform constant, including the endpoint stencil.

These are not PI's energy spaces $`X,Y=X^*`$. A general energy-dual
source need not have a bounded inverse Laplacian readout. For example,
on a flat scale-one torus, a normalized alternating fine-mesh source
has bounded $`H^{-1}`$ norm while the Laplacian of its inverse grows
like $`\eta^{-1}`$. The bare endpoint source here
is in $`F`$, not an arbitrary energy dual.

We use the energy estimate only to obtain local $`L^2`$ bounds.
The equations, with the stronger sources (P2), then give (P1).

### 2. The flat mixed inverse in these spaces

Use the flat construction stated among the inputs, following Balaban, CMP 95, Proposition 1.1, and CMP 96, Propositions 2.5–2.6.
Choose its tile size so that its **individual** energy transitions
have sum $`q<1/2`$ from either endpoint. This is the absolute refinement stated in the flat input.
The same construction covers all four mixed systems.

If a bounded source in (P2) is confined to one scale-$`s`$ cell, its
energy-dual norm is at most a constant times its normalized size.
For the first three components this follows respectively from

```math
s\|f\|_2,\qquad \|g_1\|_2,\qquad s^2\|g_2\|_2 .
```

A cell has fine volume at most $`C s^4`$. For $`g_3`$, the dual row
norm is $`\|m^{-2}g_3\|_{\rm top}`$; for $`g_4`$, it is the counting
norm. Each cell has a bounded number of these row coordinates.
These statements also hold for a cell enlarged by a fixed factor.
Here a cell is one layer block of side comparable to its local scale,
including its bounded neighboring blocks when a stencil is read.
Partition bounded sources by these cells; no difference of their
indicators occurs in this step. The component norms are maxima, so
the five source decompositions cost only a fixed factor.

Restrict the energy output norm to a cell, without multiplying a
Sobolev field by its indicator. A word that joins two cells at distance
$`d`$ has at least $`d/D-1`$ transitions, where $`D`$ is the fixed
flat footprint diameter. Sum the bounds $`Cq^n`$ from the output
endpoint. Thus a source cell at $`z`$ gives

```math
\|X\|_{X,\mathrm{loc}(y)}
\le C e^{-a d(y,z)}\|F\|_{V,z}.                    \tag{P3}
```

This argument applies to every component of the mixed inverse.
It does not use positivity of a mixed matrix.

Here is the summation needed to apply (P3) to many source cells.
Here is the shell count in PI's lattice-contour metric. It does the work of Balaban's scale summation, CMP 96, (2.59)–(2.61), which your account uses at CA-I 13420–13427. Let the gap be $`\rho\ge1`$ in local units, and fix $`y`$ of level $`i`$. A path of cost at most $`t`$ from $`y`$ that reaches level $`h>i`$ crosses every complete collar of levels $`i+1,\ldots,h-1`$. Each crossing has Euclidean length at least $`\rho\ell_q`$ at scale at most $`\ell_q`$, so it costs at least $`\rho`$. The crossings are disjoint. Hence every endpoint $`z`$ has $`|j_z-i|\le1+t/\rho`$, and the largest scale on the path is at most $`L^{1+t/\rho}m_y`$. The lifted displacement is at most $`tL^{1+t/\rho}m_y`$. At a fixed endpoint level, a cube of this radius holds at most $`(3+2tL^{2+2t/\rho})^4\le(3+2t)^4L^{8+8t/\rho}`$ grid points. There are at most $`3+2t/\rho\le5(1+t)`$ levels, and $`(m_z/m_y)^b\le L^{|b|(1+t/\rho)}`$. Together these give

```math
\sum_{d(y,z)\le t}(m_z/m_y)^b
\le 5L^{8+|b|}(1+t)(3+2t)^4
\exp\!\left((8+|b|)(\log L)t/\rho\right).          \tag{P4}
```

For a torus, count lifted paths; this only overcounts endpoints.
Choosing $`\rho\ge2(8+b_0)\log L/a'`$ and summing integer shells
proves

```math
\sup_y\sum_z(m_z/m_y)^b e^{-a'd(y,z)}<\infty
\quad (|b|\le b_0).                 \tag{P5}
```

Indeed the remaining series is bounded by a constant times
$`\sum_{n\ge0}(n+2)^5e^{-a'n/2}`$, whose tail is geometric.
Use $`b_0=8`$, enlarging it if a different finite normalization
requires this. This proves the required summation; a polynomial
volume-growth assertion is unnecessary. It also proves both weighted
Schur sums after reserving a positive part of the exponential.

Consequently a source bounded in $`V`$ gives a uniformly bounded
local energy norm everywhere. We now upgrade it to $`Z`$.
Inside an interior flat patch the mixed equations are exactly

```math
\begin{split}
\Delta_{\rm comp}h
&=g_2+Q'^T\mu-Q'^Tm^{-2}Q'h,\\
\Delta_{\rm comp}A
&=f+D h-Q^TaQA+K^T\nu,\\
\Delta_{\rm comp}\lambda
&=g_1+D^TA-h-Q'^Tm^{-2}Q'\lambda .
\end{split}                                                   \tag{P6}
```

The last term in the second equation is absent for $`M_4`$.
Signs on $`g_3,g_4`$ affect neither estimate.

The energy norm bounds a nearby row coefficient by
$`m^4|\mu|\le C\|X\|_{X,\mathrm{loc}}`$ and
$`|\nu|\le\|X\|_{X,\mathrm{loc}}`$.
The scalar row mass applied to $`h`$ is at most
$`C m^{-4}\|h\|_{2,\mathrm{loc}}`$.
These are Jensen estimates with the physical row measures.
The field mass applied to $`A`$ is at most
$`C m^{-4}\|A\|_{2,\mathrm{loc}}`$.
Finally $`K^T\nu`$ is at most $`C m^{-3}|\nu|_{\mathrm{near}}`$.
For the last assertion use the physical column sum of the straight
row, as in PI Appendix A.1, (A.1)–(A.2), from Balaban, CMP 98, (124)–(125). Only adjacent heights meet a read.

Apply the free local Poisson input (P7) first
to $`h`$. Its $`L^2`$ norm and the first equation give its value,
gradient, gradient Hölder bound, and Laplacian, with powers
$`m^{-2},m^{-3},m^{-3-\beta},m^{-4}`$.
Insert the gradient of $`h`$ in the second equation. The same
estimate gives $`A,\nabla A,\Delta_{\rm comp}A`$, with powers
$`m^{-1},m^{-2},m^{-3}`$.
Insert $`\nabla A`$ and $`h`$ in the third equation. It gives
$`\lambda,\nabla\lambda,\Delta_{\rm comp}\lambda`$, with powers
$`1,m^{-1},m^{-2}`$.

For clarity, the free estimate used here has a written kernel proof.
The density of the flat Green function and its differences of orders
$`0,1,2,3`$ are bounded by
$`C(|x|+\eta)^{-2-q}`$. Split its Fourier integral at frequency
$`|x|^{-1}`$, and integrate the complementary integral by parts
$`q+3`$ times. Radial integration gives these powers. For
$`\Delta u=D^*g+f`$, convolution on a larger cutoff cube gives

```math
\begin{split}
|u|+s^\alpha[u]_\alpha
&\le C_\alpha(s^{-2}\|u\|_2+s|g|+s^2|f|),\\
|\nabla u|+s^\beta[\nabla u]_\beta
&\le C_{\epsilon,\beta}
(s^{-3}\|u\|_2+|g|+s^\epsilon[g]_\epsilon+s|f|),
\qquad 0<\beta<\epsilon<1 .
\end{split}                                                   \tag{P7}
```

For the mixed second derivative subtract $`g`$'s value at the output.
The remaining radial integral is $`\int_\eta^{Cs}t^{\epsilon-1}dt`$.
The constant part is bounded by moving both differences onto the
cutoff. The harmonic remainder is bounded by repeated Caccioppoli
estimates on nested cubes. These are the free local estimates stated among the inputs; they include the bounded-mesh case.

Choose the local cubes in (P6) with radius a fixed small multiple
of $`m/L`$. The tower gaps put their full stencils inside the interior
domain and keep their scales comparable. If this radius has only a
bounded number of mesh steps, the pointwise $`L^2`$ inequality and
finite differences give the same powers with a fixed constant.
At an actual or artificial outer boundary the model is bare:
$`m=\eta`$. The same finite-difference argument applies to its zero
extension, for every boundary shape. There is no elliptic regularity
assumption at a nonbare reentrant Dirichlet corner.

We have proved a constant $`B_Z`$, independent of the main PI tile
size, such that

```math
\|M_r(1)^{-1}\|_{V_r\to Z_r}\le B_Z .
\tag{P8}
```

The construction also proves the needed finite power shifts and
local Hölder members. Its constants are fixed from the flat
construction before the main local-model scale is chosen.

### 3. Strong comparison of the actual coefficients

Put $`U=e^{i\eta B}`$ in one of PI's supplied local gauges, and
$`e=\sup(m|B|+m^2|\partial B|)`$.
For $`e`$ sufficiently small,

```math
\|(M_r(U)-M_r(1))X\|_V\le C_Z e\|X\|_Z .         \tag{P9}
```

Here is a verification of all block types; it is stronger than the
energy comparison in PI Lemma 5.1.

For a covariant difference,
$`(D_U-D_1)v=c\,v_{\rm shifted}`$, where
$`|c|\le Ce/m`$ and $`|\partial c|\le Ce/m^2`$.
Expanding two differences gives a sum bounded by

```math
C e\{m^{-1}|\partial v|+m^{-2}|v|\}.
```

The neighboring scales differ by at most $`L`$. This proves the
comparison for the scalar second-order and first-order blocks.

PI Lemma 4.4 gives both the row error $`Ce`$ and the physical
column error $`Ce(\eta/m)^4`$ for the literal rows.
After the physical transpose, the latter factor cancels the fine
pairing volume. For instance

```math
|(K(U)^T-K(1)^T)\nu|
\le Ce\,m^{-3}|\nu|_{\mathrm{near}}.
```

Replace both factors in each row mass. Jensen, the same column
bound, and the two-height property prove (P9) for every averaging
block. No derivative of an averaging density is required.

For the vector Hessian use the exact polarized plaquette formula in PI Lemma 5.1, from Balaban, CMP 99b, (3.10). In a common plaquette frame its curl sum has
the form

```math
X_U(v)=X_1(v)+\eta L_Bv,\qquad
|L_B|\le Ce/m,\quad |\partial L_B|\le Ce/m^2.
```

The transports defining $`L_B`$ contain at most four links, so the
last two estimates follow by telescoping their products and one
difference. Also

```math
|P-I|\le C\eta^2e/m^2,\qquad
P+P^{-1}-2=(P-I)^2P^{-1}.
```

The terms linear in $`L_B`$ are
$`d^*L_Bv`$ and $`L_B^*dv`$. The difference product rule bounds
them by the preceding first-order expression. The $`L_B^*L_B`$
term is a smaller mass term.
For the term with $`P+P^{-1}-2`$, write
$`E=(P-I)^2P^{-1}/2`$. The remaining curl form is
$`(d+L_B)^*E(d+L_B)`$. Bound the outer difference by
$`2/\eta`$, rather than differentiating the curvature. Its size
on the $`d^*Ed`$ term is at most

```math
C\eta^3e^2m^{-4}|\partial v|
\le Ce^2m^{-1}|\partial v|.
```

The terms $`d^*EL_Bv,L_B^*Edv,L_B^*EL_Bv`$ are bounded by
$`Ce^2\{m^{-1}|\partial v|+m^{-2}|v|\}`$: substitute
$`|E|\le C\eta^4e^2m^{-4}`$, $`|L_B|\le Ce/m`$,
$`\eta\le m`$ and $`e\le1`$. Shifts change these inequalities
only by fixed powers of $`L`$.
The commutator term with $`P-P^{-1}`$ is a finite-stencil
zeroth-order term bounded by $`Ce\,m^{-2}|v|`$.
These are all terms of the polarized plaquette formula.
Adding the $`D_UD_U^T`$ comparison proves (P9) for the vector block.
It uses $`B,\partial B`$, not $`\partial^2B`$ or a current derivative.

The same difference expansion compares $`Z`$ with its covariant
version at the real local potential. It also compares the consumer's
complex-background readout with the real-reference readout. Explicitly,
write $`D_W=D_{U_r}+c`$ in a local gauge. (S2), (S2+) and the
local logarithm estimate give
$`|c|\le Ce/m`$, $`|\nabla_{U_r}c|\le Ce/m^2`$, so

```math
|(\Delta_W-\Delta_{U_r})v|
\le Ce\{m^{-1}|\nabla_{U_r}v|+m^{-2}|v|\}.
```

Multiplying by $`m^3`$ gives the graph comparison; the first-
difference comparison is immediate. Interchanging the references
gives the reverse inequalities. The coefficients and stencils stay
inside the same complete footprint. The same comparisons hold with
an admitted weight, since only neighboring, comparable-scale values
occur. We include these fixed constants and the corresponding
reduction of the field radius in the constants of the theorem.
Cutoff multiplication is bounded
on $`Z,V`$ by a constant $`c_Z`$. Its graph part follows from the
exact difference product rule, with one first and one second cutoff
difference. Scalar cutoffs commute with the unitary gauge changes.

By PI Lemma 5.2 the model potential has
$`e\le C_S(L^2a_0+a_1)`$. Choose the background radii so that
$`B_ZC_Ze\le1/8`$, including the norm comparison.
The Neumann series for the finite local matrix now gives

```math
\|M_{r,\tau}(U)^{-1}\|_{V_\tau\to Z_\tau}
\le3B_Z .                          \tag{P10}
```

All models, including the graded artificial collars, use (P8).
This step is not an inference from an energy bound to a pointwise bound.

### 4. Every cutoff transition, including its coefficients

For a tile $`\tau`$, PI's cutoffs obey

```math
|\partial h_\tau|\le C/(M_t\ell_\tau),\qquad
|\partial^2h_\tau|\le C/(M_t\ell_\tau)^2 .
```

On their complete read closure $`m\le L\ell_\tau`$.
This follows from PI §5.2 and its two-height geometry.
The following commutator estimate holds:

```math
\|[M_{r,\tau}(U),h_\tau]X\|_V
\le C_{\rm com}M_t^{-1}\|X\|_Z .
\tag{P11}
```

For the flat differential blocks, the terms are
$`(\partial h)X`$, $`(\partial h)\partial X`$, and
$`(\partial^2h)X`$. Substitution of the powers in (P1)--(P2)
gives $`C/M_t`$ in each component. For example the
$`g_2`$ component has
$`m^4(\partial h)\partial h_{\rm field}`$ and
$`m^4(\partial^2h)h_{\rm field}`$; these are respectively
bounded by $`C/M_t`$ and $`C/M_t^2`$.
Here $`h_{\rm field}`$ is the scalar auxiliary variable.

For each row or transposed row, the commutator is its kernel
times the cutoff difference between the row reference point and
the fine reference point. That difference is at most $`C/M_t`$
over its double-block read. Apply the physical row and column
estimates of the previous section. For a row mass insert the
cutoff at the intermediate row; this gives the two row errors.
These cases exhaust the nonzero mixed blocks.
At a bare boundary the same conclusion follows directly from
the finite stencil and $`m=\eta`$.

Alternatively the curved remainder costs
$`2c_ZC_Ze`$ by (P9). Choosing $`e\le c/(M_t C_Zc_Z)`$,
after $`M_t`$, makes this at most the flat commutator bound.
This is precisely PI's order of choice, now for the stronger constants.

Use Balaban's local-model construction, CMP 99b, (3.87)–(3.108), in the precise form of PI:

```math
S_\tau=h_\tau M_\tau^{-1}h_\tau,\qquad
T_\tau=[M_\tau,h_\tau]M_\tau^{-1}h_\tau .
```

They obey

```math
\|S_\tau\|_{V\to Z}\le3B_Zc_Z^2,\qquad
\|T_\tau\|_{V\to V}\le
\theta_Z:=3B_Zc_Z^2C_{\rm com}/M_t .              \tag{P12}
```

Choose $`M_t`$, a permitted power of $`L`$, so that
$`\theta_Z\le(4D_*)^{-4}`$, where $`D_*=3(20L)^4`$.
Enlarge PI's $`B_F,c_h,C_C`$ and PI's flat commutator constant (also written $`C_{\rm com}`$ in PI) to cover $`B_Z,c_Z,C_Z`$ and the constant $`C_{\rm com}`$ of (P11), before applying PI's eight choices. PI's $`C_K=3C_{\rm com}`$ then covers it as well. This gives the stated common
choice without changing a coefficient or an algebraic identity.
Choose all radii afterwards. Include the flat torus room $`t_FM_F`$
in (T1); it is not inferred from the other torus floor.

The exact identity $`M\sum S_\tau=I+\sum T_\tau`$ is PI's
parametrix identity. The remainder is bounded by $`D_*\theta_Z<1`$
on $`V`$, using overlap. Hence its words

```math
W_\omega=S_{\tau_0}(-T_{\tau_1})\cdots(-T_{\tau_n})
\quad\hbox{satisfy}\quad
\|W_\omega\|_{V\to Z}\le3B_Zc_Z^2\theta_Z^n.             \tag{P13}
```

They are the actual PI local-matrix words, estimated in the stronger norms.

The transpose estimates are also needed. Since the mixed matrix
and its local matrices are bilinearly symmetric,

```math
W_\omega^T
=(-L_{\tau_n})\cdots(-L_{\tau_1})S_{\tau_0},
\qquad L_\tau=-h_\tau M_\tau^{-1}[M_\tau,h_\tau].
```

Here $`\|L_\tau\|_{Z\to Z}\le\theta_Z`$, by (P10)--(P11).
Thus the reversed words have the same $`V\to Z`$ bound.
All five variable/source powers are dual under the stated pairings;
for example $`m^4(m^{-1})(m^{-3})=1`$, and the $`\nu`$ pairing
is counting. This proves the column bounds with their measures,
not by confusing a fine transpose with a counting transpose.
No individual right-parametrix word is assumed symmetric. Its
transpose is estimated by the displayed left-parametrix word.

The derivative stencils of an endpoint enlarge its support by at
most two fine steps. They stay strictly inside PI's footprint.
The cutoff and these differences read only bumps whose supports
meet that enlarged support. Their tiles lie within
$`(1+3L/2)M_t\ell_\tau+2\eta<\widehat r\ell_\tau`$.
Thus the complete cutoff coefficients, including their derivatives,
are determined by $`F_\tau`$. PI's setting-compatibility proof
applies to these words and readouts with no additional field read.

### 5. Endpoint majorants and the spare exponentials

At most a fixed number $`N_t\le C_L(M_t+1)^4`$ of normalized source
cells meet an endpoint cutoff; their scales differ by at most $`L`$.
At most $`D_*`$ initial tiles contribute to a fixed output cell.
The same estimates cover its full endpoint difference stencils.
For each word and source cell, take the norm of its restriction from
that cell's normalized source space to the output cell's readouts;
call this number $`k_\omega(y,z)`$. This is a nonnegative **cell**
majorant, not an assertion about an arbitrarily chosen matrix norm.
It bounds each endpoint value, first difference and Laplacian. The
input restriction is applied before the word, so no sharp cutoff is
ever differentiated at the output. For a first-order input use a
smooth partition on enlarged scale cells instead; its derivative is
$`O(m^{-1})`$ and it preserves the normalized first-order size.
These enlarged cells have bounded overlap. The constants for these
partitions are included in the majorants.
For a nonzero word, PI's geometry gives

```math
d(y,z)\le D_X(n+1),\qquad
t_\omega\le17D_X(n+1),\qquad D_X=24L^2M_t ,
```

where $`t_\omega`$ is the anchored tree length for the complete
visited domains. Here is the complete-footprint tree construction. The cube floor makes each footprint smaller than a decoupling cube, so it meets at most sixteen cubes. Choose a representative in each intersection. Join those representatives, the endpoint anchors, and the consecutive-footprint joining points. At most $`17(n+1)`$ links are required. If a thin intersection contains no top, choose a top in its decoupling cube within $`\ell_{i+1}`$. It lies in the enlarged footprint $`F_\tau^+`$. PI §5.2's staircase construction then has cost at most

```math
16L(L+1)M_t+8L^2+12L\le24L^2M_t=D_X.
```

The gap floor keeps that construction within two adjacent heights. Thus the tree passes through every counted cube and has the stated length.

Set $`\mu=\log(1/\theta_Z)/(140D_X)`$.
Splitting $`\theta_Z^n`$ into two halves proves from (P13)

```math
k_\omega(y,z)
\le C\theta_Z^{n/2}
e^{-\mu d(y,z)-2\mu t_\omega}.            \tag{P14}
```

Indeed $`d+2t_\omega\le35D_X(n+1)`$, whereas the second half
supplies $`\frac12\log(1/\theta_Z)(n+1)`$; absorb
$`\theta_Z^{-1/2}`$ in $`C`$.
The cell input factors were included before taking this bound.

There are at most $`D_*^n`$ walks from an endpoint tile, and
$`D_*\theta_Z^{1/4}\le1/4`$.
Sum (P14), reserving one quarter for tails. This proves an absolute
weighted endpoint majorant for every field block of the mixed inverse.
For fixed scales and a finite lattice, applying an endpoint difference
to each term gives its actual difference. The uniform tail bound in
the graph norm then passes that identity to the sum. No unbounded
operator is applied merely to an energy-convergent series.

The $`AA`$ block of $`M_4^{-1}`$ is $`G_0`$.
The $`AA`$ block of $`M_5^{-1}`$ is $`B_0`$; this follows by the
same Schur elimination as PI Lemma 7.1.
For the prescribed account expansion of $`B_0`$, however, use
$`G_0-G_0Q^Tq_0QG_0`$, retaining its constituent words.
The direct block identity is not used to change its switched value.
PI's $`q_0`$ words, the physical row bounds, and (P14) therefore give
absolute majorants $`g_\Delta^*,h_\Delta^*,b_\Delta^*`$ for

```math
G_0:F\to E^\Delta,\quad
H_0=G_0Q^Tq_0\ell^{-1}:B\to E^\Delta,\quad
B_0:F\to E^\Delta .
```

They also give their first-order majorants $`g^*,h^*,b^*`$.
All convolutions use (P5); the transposed legs use the reversed-word
bound. Each piece and local insertion carries the spare-length weight
defined below.
The finite scale powers cancel at each matched leg. They do not
accumulate with the number of factors.

Here is the counting argument behind the decoupling factor, rather
than an invocation of its printed bound. Write the common cube side
as $`M_{\rm dec}\ell_k`$. A layer-metric tree of length $`t`$ has
ordinary axial length at most $`\ell_k t`$, since every scale is
at most $`\ell_k`$. Double its edges to obtain an Euler traversal,
of length at most $`2\ell_k t`$. Subdivide that traversal into
at most $`1+4t/M_{\rm dec}`$ consecutive arcs of length at most
$`M_{\rm dec}\ell_k/2`$. The coordinate span of each arc is at
most half a cube side. It therefore meets at most two grid intervals
per coordinate, hence at most sixteen cubes. This proves

```math
\#\{\hbox{cubes met by the tree}\}
\le16+64t/M_{\rm dec}.
```

For a primitive concatenation
$`\varpi=(\omega_0;\iota_1,\omega_1;\dots;\iota_n,\omega_n)`$, side branches included, build a tree
$`T_\varpi`$ as follows. For each piece $`\omega_i`$ take the tree just constructed: it passes through
a representative of every decoupling cube met by the complete footprint of $`\omega_i`$, and has layer
length $`t_{\omega_i}\le17D_X(|\omega_i|+1)`$. Each local insertion $`\iota_i`$ has a complete carrier:
the double blocks of its averaging rows, its plaquette reads, the reads of $`\mathfrak j_J,\mathfrak k_J`$
and its endpoint stencils. This carrier has layer diameter at most a fixed $`c_\iota=c_\iota(N,L)`$,
hence axial diameter at most $`c_\iota\ell_k`$. Impose the cube floor
$`\max\{4\widehat r+8L,\ c_\iota,\ 64\kappa_1/\mu\}`$. Then the carrier meets at most $`2^4`$ cubes. Join
the insertion point to the end anchor of $`\omega_{i-1}`$, to the start anchor of $`\omega_i`$, and to
one representative in each cube met by the carrier. Since
$`d(y'_{i-1},y_i)\le c_\iota`$ (CA-I 15357), this adds at most $`17c_\iota`$ of layer length. Attach each
side branch at its insertion point in the same way. The result is a connected graph through every cube
met by the term; prune it to a tree. So

```math
t_\varpi\le\sum_i t_{\omega_i}+17c_\iota n_\iota ,
```

and the Euler count applies to $`T_\varpi`$. Approximate
an infimum tree length from above if necessary. On a torus lift the
traversal; repeated copies of a cube only overcount it. A partition
consisting of the whole torus satisfies the bound directly.
Thus $`M_{\rm dec}\ge\max\{4\widehat r+8L,c_\iota,64\kappa_1/\mu\}`$ proves the required bound
for the actual common-grid partition. No assertion about an arbitrary
uncontrolled family of parameter sets is needed.

For a primitive concatenation $`\varpi`$, it follows that

```math
|\sigma_\varpi|
\le e^{16\kappa_1}e^{\mu t_\varpi}
\le e^{16\kappa_1}
\prod_{\omega\subset\varpi}e^{\mu t_\omega}
e^{17\mu c_\iota n_\iota}.        \tag{P15}
```

For any rate $`0<\delta_*\le\mu`$, define every first-order and graph majorant of §§5–8
with each piece weighted by its spare factor:
$`b^*:=\sup_y\sum_{\omega,z}k_\omega(y,z)e^{\mu t_\omega}e^{\delta_*d(y,z)}`$, and the same for
$`b^*_\Delta,g^*,g^*_\Delta,h^*,h^*_\Delta`$; in $`\theta^*`$ and in $`C_1,C_2,C_3`$, weight each insertion
by $`e^{17\mu c_\iota}`$. By (P14), $`k_\omega e^{\mu t_\omega}\le C\theta_Z^{n/2}e^{-\mu d-\mu t_\omega}`$,
so these sums are finite for $`\delta_*\le\mu`$. Use their common upper bounds for $`\delta_*\le\mu`$ before choosing the final rate.
They depend on $`\mu`$ but not on $`\kappa_1`$. With these
definitions, (P15) and the term-by-term product give $`|\sigma_\varpi|\prod k\le e^{16\kappa_1}\prod(\text{weighted }k)`$,
which is the form used in (P18).

Use the common smaller rate and full footprints in this inequality.
This gives the estimate needed in your CA-I 15368–15410. It follows Balaban, CMP 116, after (1.11), using the explicit Euler count above.
The size floor is chosen after $`\mu,c_\iota,\kappa_1`$.
The last factor of (P15) is charged
to the local insertion constant, before the current ceiling.
It is independent of $`\kappa_1`$.
The piece weights and the insertion costs $`e^{17\mu c_\iota}`$ pay (P15);
the remaining exponential retains weights and spatial decay. This proves the first line of (T2)--(T3), with the
appropriate finite number of primitive corner factors for $`H_0`$.

### 6. The first-order branches needed for the current insertions

The derivative allocation follows Balaban, CMP 99b, (3.42)–(3.49) and (3.116)–(3.120). The argument below supplies word bounds in the required norms.

We give the derivative allocation because $`\Theta'_J`$ is not a
bounded source insertion on arbitrary bounded $`J`$.
No graph bound for $`G_\pi^J`$ is used.

The preceding local proof also gives the following word bounds:
the scalar $`G'D^*`$ maps bounded data into local $`C^\alpha`$,
$`0<\alpha<1`$; $`G_0D`$ maps local $`C^\epsilon`$ into
first-order fields with gradient $`C^\beta`$,
$`0<\beta<\epsilon<1`$; and the $`P`$ words map bounded scalar
data to fields with a bounded first derivative.
Here are the changes to the source-space argument, to ensure that
these are word estimates.

For the vector differentiated source keep
$`f=f_0+Dg`$, with source size given by the infimum of

```math
\max\{m^3|f_0|,\ m^2|g|+m^{2+\epsilon}[g]_\epsilon\}
```

over such representations, locally with the same cell convention.
The other four source components keep (P2). Replace only the
$`A`$-Laplacian entry of $`Z`$ by
$`m^{2+\beta}[\nabla A]_\beta`$, $`0<\beta<\epsilon<1`$.
The value and first-gradient entries stay in the norm.
In a local gauge $`D_Ug=D_1g+cg`$; the extra term has bounded
source size $`Ce`$ times the displayed datum norm. The same holds
for $`D_U^*g`$. Thus using covariant rather than flat divergences
in these source spaces changes their bounds by a fixed constant.
The flat proof (P6) is unchanged for $`h`$. Apply the second line
of (P7) to $`A`$, then the third equation to $`\lambda`$.
The coefficient error (P9) requires only the first derivatives,
so it maps this state into the ordinary space $`V`$.
Every commutator in (P11) also maps it into $`V`$.
The flat inverse on ordinary $`V`$ has the same Hölder output by
(P7). Consequently both the perturbation series and each cutoff
transition are bounded in this enlarged source/output pair.
Thus (P12)--(P14) hold with this source and first-order output.
Hölder data are localized by smooth cutoffs, with their full
zero-extension Hölder norm. A sharp cell indicator is not
differentiated.

For the scalar differentiated source use
$`f=f_0+D^*g`$, $`g`$ bounded, and output norm
$`m^a|u|+m^{a+\alpha}[u]_\alpha`$, $`0<\alpha<1`$.
The source norm is the infimum of
$`\max\{m^{a+2}|f_0|,m^{a+1}|g|\}`$ over representations.
Use $`a=0,2`$, or a common finite power shift when matching a leg.
The first line of (P7), the scalar energy bound and (P5) prove
the flat inverse estimate in this pair of spaces.
Write its coefficient error as
$`D^*(B_1u)+B_2Du+C_0u`$.
Moving the difference in $`B_2Du`$ to $`B_2u`$ leaves a
zeroth-order coefficient bounded by $`Ce/m^2`$.
Thus the error has source norm at most $`Ce|u|`$, in the
undifferentiated-plus-divergence source space.
The scalar commutator has the same form with coefficients
$`C/M_t`$, by the difference product rule.
This proves the Neumann and word estimates in that source space.
Multiplying a divergence source by a cutoff is legitimate here:
the discrete product rule writes $`hD^*g`$ as the divergence of
$`g`$ times a shifted $`h`$, plus a bounded term containing
$`\nabla h\,g`$. These are the two components of the source norm.
The same rule gives the vector Hölder-source localization above.
Thus the rightmost source cutoff has a bounded norm too; it has
not been omitted from the transition estimate.
The necessary scalar energy bound is the Poincaré/mass estimate
included in the flat input, with identical literal flat rows; see PI Appendix A.1, (A.4).
Finally $`P=[M_3^{-1}]_{hh}`$, so its bounded-data first-derivative
word bound follows directly from (P1), (P13).
The reversed words prove the required transpose estimates as well.
For a differentiated scalar endpoint, the column estimate is the
ordinary-source first-derivative estimate on the reversed scalar
word. It is not inferred by dualizing a Hölder seminorm.
All the needed versions form a finite collection of spaces. Choose
$`B_Z,C_Z,c_Z,C_{\rm com}`$ to dominate this collection when making
the common choice in section 4; there is no later choice of $`M_t`$
after a current has been inserted.

Take $`\epsilon=(1-\beta_0)/2`$; when requesting exponent
$`\beta\le\beta_0`$, use exponent $`\beta+\epsilon`$ on the
divergence datum. Only this fixed positive gap enters the constants.
For the actual current form, your CA-I 13811–13846, `4.5:eq-free-current-operators-1`, gives exactly

```math
\begin{split}
\Theta'_JA&=\psi+D_U\varphi,\\
\psi&=\mathfrak k_J(\Lambda A),\\
\varphi&=RG'(\mathfrak j_J(A)+m_3)+RG'D_U^*m_4,\\
m_3&=O([D_U\Lambda A,J]),\qquad
m_4=O([\Lambda A,J]).
\end{split}
```

The identities follow by polarizing the displayed gauge-variation
commutator and moving one difference by the bilinear pairing.
In particular $`J`$ is never differentiated.
The scalar bounds just proved make $`\varphi`$ Hölder of every
fixed exponent below one. Apply the vector differentiated-source
bound to $`G_0D_U\varphi`$ and the bounded-source bound to
$`G_0\psi`$. The result is an **absolute** first-order word
majorant $`C_1|J|_{-3}`$ for $`G_0\Theta'_J`$.
Here $`C_1`$ is the sum of the weighted product majorants of these
terms per unit of current: each piece has weight $`e^{\mu t_\omega}`$,
and each local insertion has weight $`e^{17\mu c_\iota}`$, as in section 5.

Choose $`j_*`$ so that $`C_1j_*\le1/4`$.
The geometric series for $`G_\pi^J`$ now converges in this
absolute word algebra. Its $`Q`$-compression differs from the
bare compression by a term whose normalized majorant is
$`C_2|J|_{-3}`$, with $`C_2`$ defined by the same weighted products,
including the compression's local carriers. These constants depend
on $`\mu`$, not on $`\kappa_1`$. Reduce $`j_*`$ to have $`C_2j_*\le1/4`$.
The Neumann expansion of

```math
q_J=(I+q_0Q(G_\pi^J-G_0)Q^T)^{-1}q_0
```

then has a bounded majorant, as does $`H^J=G_\pi^JQ^Tq_J\ell^{-1}`$.
The same estimates on reversed chains give its physical transpose.
All these are constructions at one followed by word expansion.
They are not inversions of switched sums.
In particular $`R=I-P`$ is expanded before tagging. An identity
piece is $`h_\tau^2 I`$, a local diagonal word with its own footprint
and tag. Its value, first-difference and Hölder multiplier bounds
follow directly from the cutoff bounds. The finite overlap and the
length-zero case of the footprint estimate give its absolute
majorants. Consequently the identity part of $`R(\sigma)`$ also
has the required multiplier bounds when a derivative follows it;
there is no mesh-sized jump from a sharp parameter-cell indicator.
In particular,
no assertion $`R(\sigma)=I-P(\sigma)`$ is used. The symmetric
bilinear formula for $`\Theta'_J`$ permits the same derivative
allocation on a reversed chain. Its two mixed terms are each
other's transposes, and its $`\mathfrak m_J`$ term is symmetric
by its displayed polarization. No symmetry of an individual PI
word, or of its switched sum, is needed.
Every transpose after switching is the literal transpose of the
assigned words, with the same tags. Symbols such as $`D_URG'`$
in the unswitched allocation mean $`D_UR(\sigma)^TG'(\sigma)^T`$
when they arise as $`\Lambda(\sigma)^T`$. The reversed-word
bounds justify that use; symmetry at one is not continued to switches.

### 7. The local averaging vertices and the nonlinear source

For a positive-height row $`c`$, its complete double-block carrier
fits in the (S1-loc) box $`N_\tau`$ of a tile of height $`j-1`$ or $`j`$
whose cutoff support contains the row's base point.
The carrier meets only heights $`j-1,j`$; $`M_t\ge4L`$ leaves
room for both blocks. PI's gauge estimate therefore gives

```math
\ell_j\|B\|_{\infty,E_c}
\le C_{N,L}(a_0+a_1).
```

Require $`a_*\le\rho/(16C_{N,L})`$, in addition to the preceding
comparison ceilings, where $`\rho`$ is the radius
in the supplied-frame averaging input. Choose the increment ball with the same margin.
That input (item 3: the written proof of the analytic form of Balaban's CMP 98 Proposition 5) gives the literal averaging
remainder, its fine derivative density, its second and third
directional derivatives, and their bilinear transposes on a
common larger ball. At height zero the map is linear and its
remainder is zero. Only the implication from the supplied frame is used. No full-account carrier assertion is used.

The relevant density is $`C\ell_c^{1-4}`$, with counting
derivative $`\eta^4`$ times that density.
After transposition the coarse factor is $`\ell_c^4`$.
A fine bond is read only by the bounded number of adjacent-height
carriers. These facts give the weighted transpose bounds at every
admitted $`p`$, using its value ratio over the carrier. No
derivative or special exponential form of $`p`$ is used.

For the Wilson source estimates, use Balaban's plaquette expansion, CMP 102b, (39), (94)–(98). The local calculation, including complex backgrounds, is as follows.
In a common plaquette frame, let $`X_1,\ldots,X_4`$ be the oriented transported potentials. Set

```math
P(t)=\prod_{i=1}^4e^{i\eta tX_i},\quad S_p=\sum_iX_i=\eta D_UA(p),\quad C_p=\sum_{i<j}[X_i,X_j].
```

Multiplying the four series gives
$`\log P(t)=i\eta tS_p-\eta^2t^2C_p/2+t^3L_3+O(t^4)`$.
The identity $`\det P(t)=e^{i\eta t\operatorname{tr}S_p}`$ gives $`\operatorname{tr}L_3=0`$.
For Hermitian fields the real trace of $`(i\eta S_p)^3/6`$ vanishes. The two mixed terms have trace $`-i\eta^3\operatorname{tr}(S_pC_p)/2`$. Multiplication by $`-\eta^{-4}`$ gives the cubic Wilson coefficient

```math
\tfrac12\operatorname{tr}(D_UA)\sum_{i<j}i[X_i,X_j].
```

This polynomial identity extends to the complexification. The trace below specifies the holomorphic Wilson action there. The leading edge values are $`(-A_\mu,-A_\nu,A_\mu,A_\nu)`$; their commutator sum is $`2[A_\mu,A_\nu]`$.
For its first variation use the exact difference identity

```math
\delta[F,G]=[\delta F,G]+[F,\delta G]
+\eta[\delta F,\delta G].
```

Errors between the four transported potentials and their leading
opposite-edge values have an explicit factor $`\eta\nabla_UA`$.
A difference bounded by $`2/\eta`$ cancels that factor.
The curvature-dependent cubic remainder has the extra
$`\eta^2\ell^{-2}(a_0+a_1)`$ factor. Terms of degree at least four
are bounded by the exponential series
$`\sum_{n\ge4}(4\eta|A|)^n/n!`$.
More explicitly, summation by parts moves the variation of the curl onto the commutator. The displayed product rule and the cancellation of each error's explicit $`\eta`$ bound the result by

```math
C\bigl(|A||\nabla_UA|+\eta|\nabla_UA|^2\bigr)
\le Cr^2\ell^{-3}\quad\hbox{when }N(A)\le r.
```

A further variation replaces one field or gradient by the corresponding variation, giving $`Cr\ell^{-3}N(u)`$. The remaining local action terms have size $`C(\alpha r^3+r^4)\ell^{-4}`$, where $`|U_p-1|\le\alpha\eta^2\ell^{-2}`$. Cauchy's formula on a fixed larger four-edge ball of radius proportional to $`r/\ell`$ gives the same first and second variation bounds for $`\alpha,r\le1`$. Each bond lies in six plaquettes. The fine action measure cancels the measure in its gradient. A weight moves only across this finite stencil and is never differentiated.

At the complex background, work in the local gauge of PI Lemma 5.2 on the box $`N_\tau`$ that contains
the plaquette. There $`W=e^{i\eta B}`$ with $`m|B|+m^2|\partial B|\le e\le e_L\le1`$, and $`u`$ is unitary.
Each transport is a product of at most four factors $`e^{\pm i\eta B_b}`$. So it and its inverse have
norm at most $`e^{4\eta|B|}\le e^4`$, and each differs from the identity by at most $`C\eta e/m`$. Hence the
degree-$`n`$ words of the plaquette expansion have total norm at most $`(4e^4\eta|A|_{\partial p})^n/n!`$,
and the terms of degree at least four are bounded by $`C|A|^4_{\partial p}e^{4e^4\eta|A|_{\partial p}}`$.
The holonomy obeys $`|W_p-1|\le C\eta^2e/m^2`$ (proof of PI Lemma 5.1); this replaces
$`|U_p-1|\le\alpha\eta^2\ell^{-2}`$ with $`\alpha=Ce`$. The cubic identity and the displayed difference identity are polynomial identities in the transported fields. They therefore hold at complex transports in a common frame. The
holomorphic trace term is $`\tfrac12\operatorname{tr}\{P(t)W_p+W_p^{-1}P(t)^{-1}\}`$. The Cauchy
ball of radius proportional to $`r/\ell`$ stays inside the exponential and logarithm domain for
$`e\le1`$ and $`r`$ below a fixed constant. Conjugation by the unitary $`u`$ returns the bounds to the
original gauge and preserves the norms. Thus the order-two majorant for $`V_0'(A)`$ and
the order-one majorant for $`V_0''(A)u`$ from $`E_p`$ to $`F_p`$ hold at $`W`$ with constants depending
only on $`N,L`$.

This proves absolute local analytic majorants of order two for
$`V_0'(A)`$, and order one for $`V_0''(A)u`$, in $`F_p`$ from
$`E_p`$. Their finite plaquette reads and source measures are retained.

The paired quadratic averaging vertex therefore gives the weighted majorant
$`\theta^*\le C_3|J|_{-3}`$ for $`\Theta_J:E\to F`$:
pair its fine density with $`H^{J,T}J`$. Define $`\theta^*`$ by summing
these product majorants with the section 5 piece weights and a factor
$`e^{17\mu c_\iota}`$ for every local insertion. Let $`C_3`$ be its
uniform bound per unit of current under the preceding ceilings.
Thus $`C_3`$ depends on $`\mu`$, not on $`\kappa_1`$.
The field $`H^{J,T}J`$ has weight $`-4`$, by the reversed-chain bounds above.
Reduce $`j_*`$ once more so that $`b^*\theta^*\le1/4`$.
All these current choices precede $`\kappa_1`$.

There is no additional inverse hidden in the seven-term formula.
Its coefficient is
$`\mathsf k=(q_J-a)\ell^{-1}`$, with the diagonal $`a`$ fixed
by the operator definitions above. The $`q_J`$ bounds and the diagonal bound
therefore bound $`\mathsf k`$ and its transpose. For clarity, a
block or scalar power $`-b`$ below means the size $`m^b|\cdot|`$.
The matched legs are

```math
\begin{array}{c|c}
Q^T&\text{block }-3\longrightarrow F\\
\mathsf k&B\longrightarrow\text{block }-3\\
\mathsf k^T&\text{block }-1\longrightarrow\text{block }-4\\
\ell^{-1}\mathsf k&B\longrightarrow\text{block }-4\\
H^{J,T}&F\longrightarrow\text{block }-4\\
\Lambda&E\longrightarrow\text{scalar }0\quad
(D_U\Lambda:E\longrightarrow\text{fine power }-1)\\
\Lambda^T&\text{scalar }-4\longrightarrow F .
\end{array}
```

The last line follows by applying $`G'`$ to a bounded power-
$`-4`$ source, then $`R=I-P`$, then one derivative, before
expanding and tagging the composite. The local commutator formulas
give $`\mathfrak j_J:E\to\text{scalar }-4`$ and
$`\mathfrak k_J:\text{scalar }0\to F`$, each with factor
$`|J|_{-3}`$. The averaging derivative transpose maps block
power $`-4`$ into $`F`$, by its fine density and the coarse
pairing measure. These are all the legs used below.

For completeness, absolute nonlinear summation can be done with
one scalar majorant. After inserting the switched primitive
majorants, with the piece weights and insertion costs of section 5,
let $`H,C,s>0`$ bound respectively the lift, all local
averaging coefficients with one density leg, and their analytic
radius. Polarization/Cauchy on the larger fixed ball lets us take

```math
a(t)=\frac{Ct^2}{1-t/s}
```

as a coefficientwise majorant; increase $`C`$ and reduce $`s`$
to include the directional-to-multilinear polarization factor.
Define the formal series $`d(t)`$ by

```math
d(t)=a(t+H d(t)).
```

Its coefficients are nonnegative. Iteration from zero determines
each coefficient, since $`a`$ starts at degree two. Choose $`r>0`$
so that

```math
16r<s/2,\qquad 64HCr\le1,\qquad Ha'(16r)\le1/4.
```

For $`0\le t\le8r`$ and $`0\le x\le8Ct^2`$, these inequalities
give $`t+Hx\le2t\le s/2`$, hence
$`a(t+Hx)\le2C(2t)^2=8Ct^2`$.
The derivative in $`x`$ is at most $`Ha'(16r)\le1/4`$.
Thus the scalar iteration is increasing, bounded by $`8Ct^2`$,
and a contraction on this interval. Its coefficient sums are
nonnegative and increase to the formal series, so that series
converges at $`8r`$. If $`d(t)=\sum d_nt^n`$, the bounds
$`\sum d_n(8r)^n<\infty`$ and
$`\sup_n n^q2^{-n}<\infty`$, $`q=1,2`$, prove convergence of
its first two differentiated series on $`[0,4r]`$.

Expand the actual inner equation by these local Taylor vertices
and the assigned lift words. Taking absolute values is bounded
term by term by this scalar iteration. The same bounds make
$`X\mapsto C_\sigma(SA-SHX)`$ a contraction with constant at most
$`1/4`$ on $`|X|\le8Ct^2`$, for $`N(A)\le t\le8r`$.
Its convergent series is therefore precisely the analytic small
branch used in (N). The same argument with
one marked input leg bounds the derivative density and its
transpose by $`d'`$, and the second derivative by $`d''`$.
All unmarked field legs are bounded by $`N(A)`$; the marked leg
carries the weight $`p`$. Products multiply the row majorants.
If $`a_2`$ is the quadratic coefficient, put
$`d_3(t)=d(t)-a_2t^2`$. It starts in degree three and majorizes
the subtraction $`D-C^{(2)}(SA)`$, since the lift enters only
in degree three and above.

Let $`Q_*,K_*,L_*,H_*,c_j,c_k,J_*`$ denote the finite
absolute constants of the respective linear factors
$`Q,\mathsf k,\Lambda,H^J,\mathfrak j,\mathfrak k,J`$
in their matched norms; these names in this paragraph are
majorant constants. The independent current ceiling remains the
$`j_*`$ of the theorem; $`c_j,c_k`$ are per unit of current,
and $`J_*\le j_*`$ is its size. Let
$`w(t)=C_Wt^2/(1-t/s_W)`$ dominate the Wilson gradient.
The seven terms of the actual $`V'`$ have, in their printed order,
the following scalar majorants:

```math
\begin{split}
v(t)={}&H_*J_*d_3'(t)
+Q_*K_*d(t)+K_*Q_*\,t d'(t)+K_*d(t)d'(t)\\
&+(1+H_*d'(t))w(t+H_*d(t))\\
&+L_*c_jJ_*H_*d(t)
+H_*c_kJ_*L_*\,t d'(t).                       \tag{P16}
\end{split}
```

Use one larger constant for a factor and its required transpose.
All scale multiplications in this formula are already included
in their matched norms. Each term starts at degree two.
Differentiating the positive series marks exactly one field leg,
including both factors in each product. Consequently

```math
\|DV'_\sigma(A)\|_{E_p\to F_p}
\le v'(2r)\le C_{\kappa_1}r.           \tag{P17}
```

This proves an absolute source majorant, not only a bound for
the summed nonlinear function. Its footprints include every
branch and every local carrier. Smallness of $`r`$ may depend on
$`\kappa_1`$; smallness of the independent current does not.
More explicitly, choose an upper radius $`r_{\kappa_1}`$ satisfying
the preceding inequalities and keeping $`t+H_*d(t)`$ inside
$`w`$'s disc for $`t\le4r_{\kappa_1}`$. The positive series
$`v`$ starts in degree two and converges on that interval.
Then $`v'(t)/t`$, extended at zero by its quadratic coefficient
times two, is bounded for $`0\le t\le2r_{\kappa_1}`$.
This proves the last inequality of (P17) for every
$`r\le r_{\kappa_1}`$, with one fixed $`C_{\kappa_1}`$.

### 8. The graph endpoint of the current-corrected source inverse

Expand the primitive inverse at one as

```math
\widetilde G^J
=\sum_{n\ge0}B_0(\Theta_JB_0)^n .
```

For each term assign the graph norm to the leftmost bare word.
All other inverse factors need only their first-order majorants.
Summing nonnegative kernels in order gives

```math
g_\Delta^*
\le \frac{b_\Delta^*}{1-b^*\theta^*}.          \tag{P18}
```

This is a statement about the unre-summed concatenations, with
the multiplier branch in each $`\Theta_J`$ expanded.
All starred majorants use the piece weights $`e^{\mu t_\omega}`$.
Their insertion constants include $`e^{17\mu c_\iota}`$ per insertion,
which pays the last factor in (P15).
Apply (P15) once to each complete primitive concatenation.
Thus $`G(\sigma):F_p\to E^\Delta_p`$ has an absolute majorant
at most $`e^{16\kappa_1}g_\Delta^*`$, with remaining decay.

The second line of (T2) follows by composing this majorant with
the actual switched $`\Theta_J`$ majorant.
The third follows by composing it with (P17), since $`G`$ is
independent of the argument $`A`$. For account composites use
the product of their primitive tags. Each fixed linear composite
has only a fixed number of such corner factors.
The nonlinear repeated factors were included before choosing
the small radius in (P16). If a composite is union-tagged instead,
apply (P15) to that union, with branches through every local
carrier's cubes and the same weighted insertion costs; the same estimates suffice.
No identity between the two assignments has been claimed.

Products of absolutely summable kernels have absolutely summable
tails: truncate the number of factors, then truncate the finitely
many factor sums; the two discarded nonnegative tails tend to
zero. The same argument applies to the positive scalar series
in (P16). It proves (T3), the graph convergence and local uniform
holomorphy. Choose $`0<\delta_*\le\mu`$ below the retained common rate
and impose (P5) at every rate used. This completes the order of
constants and the proof of (T2).

At zero switches every surviving primitive footprint is connected
and lies in the retained components, as in PI. Products and
local vertices cannot connect different components. Common
complete footprints give identical coefficients and identical
index sets by PI's assignment. These statements prove the
restriction and setting clauses of the theorem. $`\square`$

## Constant order

Fix the constants in the following order. Row 0 lists the given data.
The weighted majorants use common bounds for $`\delta_*\le\mu`$,
so their definition precedes the final choice of $`\delta_*`$.

| Step | Constant | Depends on | Source |
|---|---|---|---|
| 0 | $`N,L,\beta_0`$; $`\epsilon=(1-\beta_0)/2`$; $`b_0=8`$ | given | theorem, §6 |
| 1 | flat tile $`M_F`$ with $`q<1/2`$; $`D`$, $`B_L`$; flat rate $`a=\log(1/q)/D`$, $`a'=a/2`$ | 0 | flat input; §2 |
| 2 | flat gap $`\rho_F\ge\max\{`$flat-model floors, $`2(8+b_0)\log L/a'\}`$; flat torus room $`t_FM_F`$ | 1 | flat input; (P5), (T1) |
| 3 | $`B_Z`$ (all finite source/output pairs of §§2, 6) | 1, 2 | (P8), §6 |
| 4 | $`C_Z`$ (P9), norm-comparison constants, $`c_Z`$, $`C_{\rm com}`$ (P11); PI's $`r_1,e_R,C_R,e_C,C_C,C_S`$ | 0 | PI §3.3 item 2; §§3–4 |
| 5 | enlarge $`B_F\ge B_Z`$, $`c_h\ge c_Z`$, PI's flat $`C_{\rm com}\ge`$ the $`C_{\rm com}`$ of (P11) (so $`C_K\ge C_{\rm com}`$), $`C_C\ge C_Z`$ | 3, 4 | §4 |
| 6 | $`M_t`$: power of $`L`$, multiple of $`LM_F`$, $`\ge\max\{2\rho'_F,4L\}`$, PI $`\theta\le(4D_*)^{-4}`$ (so $`\theta_Z\le(4D_*)^{-4}`$) | 2, 5 | PI item 3; (P12) |
| 7 | $`r_N,\widehat r,D_X`$; $`\delta_q`$; $`\mu=\log(1/\theta_Z)/(140D_X)`$; $`N_t`$ | 6 | PI items 4–5; (P14) |
| 8 | insertion range $`c_\iota`$ and costs $`e^{17\mu c_\iota}`$; weighted majorants $`b^*,b^*_\Delta,g^*,h^*`$ | 6, 7 | §5 |
| 9 | choose equal PI ceilings $`a_0^*=a_1^*=a_*`$: PI item 7 with enlarged constants, $`C_S(L^2+1)a_*\le e_L`$; $`e\le c/(M_tC_Zc_Z)`$; $`B_ZC_Ze\le1/8`$; $`a_*\le\rho/(16C_{N,L})`$ (averaging input); increment ball | 4–6 | PI items 7–8; §§3, 4, 7 |
| 10 | $`C_1,C_2,C_3`$ (with the §5 weights); $`j_*`$ with $`C_1j_*,C_2j_*\le1/4`$, $`b^*\theta^*\le1/4`$ | 3, 7–9 | §§6–7 |
| 11 | $`\delta_*\le\mu`$ and below every composite rate used | 7, 8 | §8 |
| 12 | tower floors: $`M_b`$, $`R_1M_b\ge\max\{`$PI item 6, $`2(8+b_0)\log L/\delta'\}`$ at every rate $`\delta'`$ used; torus side (T1) | 6, 7, 11 | PI item 6; (P5), (T1) |
| 13 | given $`\kappa_1`$: $`M_{\rm dec}\ge\max\{4\widehat r+8L,\ c_\iota,\ 64\kappa_1/\mu\}`$ with grid divisibility | 6–8 | P15; §5 |
| 14 | $`H,C,s`$ of the scalar majorant (contain $`e^{16\kappa_1}`$ tag factors); $`r_{\kappa_1}`$; $`C_{\kappa_1}`$ | 9–13 | §7 |

The bounds $`B_Z,C_Z,c_Z,C_{\rm com}`$ are uniform above the stated
geometry floors. The floors in step 12 impose those hypotheses.
The insertion costs precede $`j_*`$ and $`\kappa_1`$. The final
nonlinear radius may depend on $`\kappa_1`$; the current ceiling does not.

## Necessary linearization test

For this test define, at fixed base and switches,

```math
z=-Tj+\Gamma H_0b-GV'_\sigma(z+H_0b),\qquad
A'=z+H_0b,\qquad X=C_\sigma(SA'-SHX),
\quad T=I+\Gamma,\quad\Gamma=G\Theta_J.
```

At $`j=0`$, the first equation is your block-chart equation `4.5:eq-chart-walk-localisation-3`, CA-I 15311–15314. Its form at one is also given at CA-I 14377–14425. Here $`j\in E_p^\Delta`$ is an independent source for a necessary linearization test. The displayed general-source equation is not asserted to identify your completion maps. At weight one the local small solution exists. Fix $`r\le r_{\kappa_1}`$ with $`C_{\kappa_1}r\le1/4`$, and let $`\|j\|^\Delta_1+|b|_1\le c\,r`$ with $`c`$ small. Then $`N(H_0b)\le r/2`$ by (T2). On the ball $`\|z\|^\Delta_1\le r/2`$, every argument has $`N\le r`$. Since $`GV'_\sigma(0)=0`$, the third line of (T2) makes $`z\mapsto GV'_\sigma(z+H_0b)`$ Lipschitz with constant $`C_{\kappa_1}r\le1/4`$ on that ball, and of size at most $`r/4`$. With $`\|Tj\|^\Delta_1+\|\Gamma H_0b\|^\Delta_1\le r/4`$ from (T2), the right side maps the ball into itself and is a contraction. The inner equation for $`X`$ is the small branch of §7.

The linearization is at the zero datum with the base and switches fixed.
Because $`V'(0)=DV'(0)=0`$ and $`C(0)=DC(0)=0`$, the defining equations give

```math
D_jA'(0)=-T,\qquad D_bA'(0)=TH_0,\qquad DX(0)=0.
\tag{L}
```

Write $`h_0,h_\Delta,\gamma_\Delta`$ for the actual bounds furnished
above: $`h_0,h_\Delta\le C_{\kappa_1}`$, and $`\gamma_\Delta\le C_{\kappa_1}|J|_{-3}`$. Since $`\|u\|_p\le\|u\|^\Delta_p`$,

```math
\|Tj\|^\Delta_p\le(1+\gamma_\Delta)\|j\|^\Delta_p,\qquad
\|TH_0b\|^\Delta_p
\le(h_\Delta+\gamma_\Delta h_0)|b|_p.              \tag{P19}
```

This proves the necessary bounds in (L) with the prescribed composite convention. No inverse identity for a switched sum enters.

The theorem gives the three endpoint bounds (T2) and their absolute expansions on the PI class with the specified constants. A larger preassigned radius or a different word assignment requires its own proof.

