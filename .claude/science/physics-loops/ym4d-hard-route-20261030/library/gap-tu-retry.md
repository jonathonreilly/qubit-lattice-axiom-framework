# Repo search

The target-specific digest `prior/gap-tu-astra.md` is absent at the pinned
checkout `aba8076b0e9d9787f28049c9ac08c528e7969001`. The lead's November 8
search record concerns other targets. Its screening section nevertheless
identifies a useful periodic Villain result on `main`:
`docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
(here **PV**). I read its mathematical argument at main revision
`bb4ec020d5ada57c630dd89acc98a68397ade423`, sections 1–10. PV proves a
periodic affine integer-curl covariance estimate and applies it to finite
clock groups. It retains winding currents. It does not state the U(1)
Langevin gap limit. I reuse its estimate and method; I do not claim them
as new. The method is credited there to Jürg Fröhlich and Thomas Spencer.

The closer local sources are Claude Fable 5.2's `gap-ac-lat.md`, section 4,
and Claude Opus 5.5's `gap-u1-audit-opus.md`, section 3 R2. The former
poses (TU); the latter identifies the missing periodic Langevin step.
`prior/gap-lit-u1.md` records the boundary and Wilson-proof limits of FS.
The permitted paper directory does not exist on this machine. Its papers
were not read. No FS proof is reconstructed from memory.

Searches of `open-registry.md`, `open-core.md`, and `l17c.md` found no owner
of this Langevin target. The registry's other TU is a rotation problem.
The Sussman–Alpoge index searches found constrained Gaussian gaps, not this
compact-model Langevin claim. The neighbouring rows for FX31 lead to
outline lines 9536–9577: the decay is for constrained nonpivot variables,
“not a physical Yang--Mills mass gap.” The outline and CA-I were each
fetched once at `31a47c543775`. Credit Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their texts, for this scope comparison.
No theorem of their text is used below.

Two further `main` hits were checked at the same revision. The statement
of `docs/FIXED_COUPLING_HAAR_VILLAIN_FULL_SCORE_GAUSSIAN_MAXWELL_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-15.md`,
sections 1–2, concerns free cubes and explicitly leaves microscopic
periodic-state matching additional. It is not a supplier here.
`docs/POSITIVE_WILSON_VILLAIN_MIXTURE_AND_WEAK_REGION_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md`
(here **WV**), sections 1–7, gives a positive mixture and weak-region bounds;
section 6 leaves the diluted gauge-phase step open. Section 4 below uses
that boundary. The other screened noncompact covariance note, lines
120–145, has a Dirichlet Maxwell law, not the compact Wilson measure.
The broad `main` content search was stopped without a result; the claims
here rest on these exact reads and the supplied prior search records,
not an assertion of exhaustive new repository coverage.

# Periodic U(1) and the retry of (TU)

Proof item, FINISH row 786. Author: Codex gpt-6-astra, max effort.
Research text, not an audit; it grants no status. No numerical or
computer-assisted proof step is used. No independent check has occurred.

## Result

(U-tor) holds for periodic Villain U(1), at every fixed $\beta\geq2^{14}$,
with the link Laplacian normalization in (2). Sections 1–2 extend PV's
written covariance argument and prove the Langevin bridge. Section 3
then refutes a group-blind (TU) continuation theorem for a fixed smooth
U(1) action. The Wilson-cosine specialization is not proved here.
Accordingly, the method-level discard is a theorem; the literal
Wilson-cosine assertion in `gap-ac-lat.md` 4.2 is not promoted to one.

## 1. The periodic Villain statement

Write $T_M=(\mathbb Z/M\mathbb Z)^4$, with $M\geq4$. Each unoriented
link has one positive orientation and one angle in $\mathbb R/2\pi\mathbb Z$.
Set

\[
 \phi_\beta(t)=\sum_{n\in\mathbb Z}e^{-n^2/(2\beta)}e^{int},\qquad
 d\mu_{\beta,M}=Z^{-1}\prod_p\phi_\beta((d_1\theta)_p)\,d\theta.
 \tag{1}
\]

Poisson summation makes $\phi_\beta$ positive. Multiplicative constants
in its equivalent Villain image formula cancel. The link metric is
$d\theta_e^2$, and time is fixed by the generator

\[
 U_{\beta,M}=-\sum_p\log\phi_\beta((d_1\theta)_p),\qquad
 L_{\beta,M}=-\Delta+\nabla U_{\beta,M}\cdot\nabla.
 \tag{2}
\]

Let $\gamma_V(\beta;M)$ be its Poincaré gap on gauge-invariant functions:

\[
 \gamma_V(\beta;M)=
 \inf_{\substack{f\text{ smooth, gauge invariant}\\\operatorname{Var}_\mu f>0}}
 \frac{\mu(|\nabla f|^2)}{\operatorname{Var}_\mu f}.
 \tag{3}
\]

**Theorem V (U-tor for Villain).** At every fixed $\beta\geq2^{14}$,

\[
                  \lim_{M\to\infty}\gamma_V(\beta;M)=0.       \tag{4}
\]

This includes odd $M$. There is no rate assertion. The proof uses PV's
written affine-coset argument, with the parity modification below. It uses
none of PV's executable evidence, OS reconstruction, or physical claims.
This is an author proof, not an independently checked result.

### 1.1 The reused estimate, and its parity extension

Use the Euclidean inner product on cochains. Let $P_e,P_c,P_h$ be the
orthogonal exact, coexact and harmonic two-form projections. Put
$K=d_1\mathbb Z^E$. The following is PV, sections 3–7, equation (7.3):
for every affine translate $z+K$, the discrete Gaussian of variance
parameter $\beta$ has

\[
 \operatorname{Cov}_{z+K}(F)\succeq
           \beta(1-\delta(\beta))P_e.                       \tag{5}
\]

PV proves (5) by a finite positive mixture of separated currents, local
Gaussian damping, and a bound on the second source derivative. Small
currents are filled. Large currents, including winding currents, use the
torus Poincaré bound. Harmonic averaging is joint. These are prior results,
not new lemmas of this note. In particular, replacing a winding current
by a plaquette boundary is not part of the argument.

Only the 32-color choice in PV section 5 uses even $M$. Here is its
replacement. Color each cycle $\mathbb Z/M\mathbb Z$ properly with at
most three colors: use alternating colors for even $M$; for odd $M$,
alternate on the first $M-1$ vertices and give the last vertex color three.
Color a link by its orientation and the three transverse vertex colors.
There are at most $4\cdot3^3=108$ colors. Two links of one color cannot
share a plaquette. Indeed, parallel edges of a plaquette differ by one
transverse step, while nonparallel edges have different orientations.

For each current, a color retains at least $1/108$ of its squared norm.
PV's exact damping identity is unchanged. Since $(d_1^*d_1)_{ee}=6$,
the exponent retained is at least $\beta\|\rho\|^2/1296$.
Every other step of sections 3–7 uses only periodic distance, support
separation, and the scalar torus gap. Those hold for odd $M$ too.
Thus (5), and its coexact Hodge image, hold for every $M\geq4$ with

\[
\begin{split}
 b_1&=\frac{107\log3+\log4}{4\pi^2},\qquad
 a=\beta/1296-b_1,\qquad q=e^{-2\pi^2a},\\
 S_j(q)&=\sum_{r\geq1}r^jq^r,\\
 c_*(\beta)&=\frac{8503056S_6(q)+262144S_5(q)}{ae},\qquad
 \delta_*(\beta)=\beta c_*(\beta).
\end{split}                                                   \tag{6}
\]

These are PV's constants, with 384 replaced by 1296. The changed
selection loses no condition on the source or affine shift. The proof's
small-current filling and large-current packing estimates are identical.

Here is a hand bound sufficient for this note. PV section 9 gives
$b_1<10/3$ and $S_5(q),S_6(q)\leq2q$ when $q\leq1/1024$.
For $\beta\geq2^{14}>8640$,

\[
 a>\beta/2592,\qquad
 q<e^{-\beta/144}<2^{-64},\qquad
 \delta_*<2592(8765200)q<2^{36}q<2^{-28}<1/2.             \tag{7}
\]

The second inequality uses $\pi>3$, $2^{14}/144>64$, and $\log2<1$.
The third uses $e>2$, $2592<2^{12}$, and $8765200<2^{24}$.
No machine evaluation enters these inequalities.

### 1.2 Continuous Haar links: the exact missing model passage

Expanding (1) and integrating each link gives the centered Gaussian
integer two-form law

\[
 \nu_{\beta,M}(n)\ \propto
 e^{-\|n\|^2/(2\beta)}\,\mathbf1_{\{d_1^*n=0\}},\qquad
 C_M=\operatorname{Cov}_{\nu_{\beta,M}}(n).                   \tag{8}
\]

Partition its lattice into cosets of $d_2^*\mathbb Z^{C^3}$.
Conditional covariance and the coexact version of (5) give the lower
bound in

\[
 \beta(1-\delta_*)P_c\preceq C_M
                         \preceq\beta(P_c+P_h).             \tag{9}
\]

For the upper bound, use PV's finite-clock identity (2.1) and sandwich
(8.2), with the just-proved parity extension. At fixed $M$, its primal
integer law has constraint $d_1^*n\in N\mathbb Z^E$. As $N\to\infty$,
this indicator converges pointwise to the indicator in (8).
The summable bound $(1+\|n\|^2)e^{-\|n\|^2/(2\beta)}$ permits convergence
of normalizers, means and second moments. The dual parameter is
$\beta_d=N^2/(4\pi^2\beta)$. Equation (6) gives
$\delta_*(\beta_d)\to0$. Passing in PV (8.2) proves (9).
This limit is at one fixed finite torus; it is not an interchange with
the thermodynamic limit. PV's bound $C_M\preceq\beta I$ also follows.

### 1.3 Every periodic local limit has a nonsummable bounded score

Define the smooth, bounded, gauge-invariant local observable

\[
 s_p=(\log\phi_\beta)'((d_1\theta)_p),\qquad
 \kappa_M=-\mu_{\beta,M}((\log\phi_\beta)''((d_1\theta)_p)).
\]

Charge conjugation gives $\mu(s_p)=0$. Isotropy makes $\kappa_M$
independent of $p$. The Fourier insertion identity from PV section 10 is

\[
              C_{s,M}(p,q)=\kappa_M\mathbf1_{p=q}-C_M(p,q).
                                                               \tag{10}
\]

For clarity, the off-diagonal derivative inserts $(in_p)(in_q)$.
On the diagonal, $\phi''/\phi=(\log\phi)''+s^2$. These two identities
prove (10) also for the continuous Haar law (1).

Take any sequence $M\to\infty$ and any local weakly convergent
subsequence. Existence follows by compactness of the countable product
of circles, after reading every fixed finite set inside each large torus.
Translation, cubic and charge-conjugation symmetries pass to this limit.
Bounded local observables give $\kappa_M\to\kappa$ and convergence in
(10). The Fourier symbols of $P_e,P_c$ converge on finitely supported
test forms by Riemann sums; they are bounded and continuous except at
zero. Local entries of $P_h$ tend to zero as $M^{-4}$.
Thus (9) passes to a positive convolution operator $C$ on infinite
lattice two-forms, with a bounded Fourier multiplier satisfying

\[
 \beta(1-\delta_*)P_c(k)\preceq\widehat C(k)
                         \preceq\beta P_c(k)\quad\text{a.e. }k.
                                                               \tag{11}
\]

For orientation $12$, put $v_i=e^{ik_i}-1$. The elementary symbol is

\[
 (P_c)_{12,12}(k)=1-\frac{|v_1|^2+|v_2|^2}{\sum_{i=1}^4|v_i|^2},
                       \qquad k\ne0.                          \tag{12}
\]

If $x\mapsto\mu(s_{12}(0)s_{12}(x))$ were absolutely summable,
(10) would give a continuous representative of $\widehat C_{12,12}$.
The scalar bounds (11) then hold everywhere away from zero, by continuity
and density of their full-measure set. On the $k_1$ axis this representative
is zero. On the $k_3$ axis it is at least $\beta(1-\delta_*)>0$.
It cannot be continuous at zero. This contradiction proves nonsummability
in **every** periodic local limit. No selection of the fixed-boundary FS
state is needed.

## 2. A uniform Langevin gap would force summability

This supplies the dynamical bridge, not the transfer-operator bridge.
Fix any smooth periodic plaquette potential $V$. On $T_M$ let
$U=\sum_pV((d_1\theta)_p)$ and $L=-\Delta+\nabla U\cdot\nabla$.
The adjacency graph has links as vertices; two links are adjacent when
they belong to a common plaquette. Write $r(X,Y)$ for graph distance.
There are six plaquettes through a link, and four links per plaquette.
Thus, with $B_{ee'}=\sup_\theta|\partial_e\partial_{e'}U|$,

\[
 B_{ee'}=0\quad\text{if }r(e,e')>1,\qquad
 \sup_e\sum_{e'}B_{ee'}\leq H:=24\|V''\|_\infty.           \tag{13}
\]

**Lemma L.** Suppose the gauge-invariant gap is at least $\varepsilon>0$.
For smooth gauge-invariant $F,G$ supported on link sets $X,Y$,

\[
\begin{split}
 |\operatorname{Cov}_\mu(F,G)|
 &\leq v^{-1}D(F)D(G)e^{-r(X,Y)/2}\\
 &\quad+\|F\|_\infty\|G\|_\infty
                  e^{-\varepsilon r(X,Y)/(2v)},\\
 D(F)&=\sum_e\|\partial_eF\|_\infty,\qquad
 v=\max(1,eH).
\end{split}                                                   \tag{14}
\]

All constants depend on the potential and the displayed observables,
not on $M$.

**Proof.** Let $P_t=e^{-tL}$. Lift the circle diffusion to Euclidean link
coordinates with periodic drift:
$d\theta_t=-\nabla U(\theta_t)dt+\sqrt2\,dW_t$.
Its smooth drift has a global Lipschitz constant in each finite volume.
The derivative $J_t$ in the initial condition solves
$\dot J_t=-\operatorname{Hess}U(\theta_t)J_t$, $J_0=I$.
Its integral equation, iterated and bounded term by term, gives
$|(J_t)_{ie}|\leq(e^{tB})_{ie}$.
Differentiating the expectation of a smooth bounded $F$ is justified by
this finite-time bound. Therefore

\[
 \|\partial_eP_tF\|_\infty
      \leq\sum_i(e^{tB})_{ie}\|\partial_iF\|_\infty.          \tag{15}
\]

Each nonzero term of $(B^k)_{ie}$ follows a path of at most $k$ steps.
Its row sum is at most $H^k$. Since $B$ is symmetric,

\[
 \sum_i e^{r(i,e)}(e^{tB})_{ie}\leq e^{eHt}\leq e^{vt}.
                                                               \tag{16}
\]

Equations (15)–(16) imply
$\|\partial_eP_tF\|_\infty\leq D(F)e^{-r(e,X)+vt}$.
The generator preserves gauge invariance, since its metric and potential
do. Integration by parts gives, for every $T\geq0$,

\[
 \operatorname{Cov}(F,G)
 =\int_0^T\mu(\nabla P_tF\cdot\nabla G)\,dt
                        +\operatorname{Cov}(P_TF,G).          \tag{17}
\]

For $r=r(X,Y)>0$ take $T=r/(2v)$. The first term is at most
$D(F)D(G)e^{-r}(e^{vT}-1)/v\leq D(F)D(G)e^{-r/2}/v$.
For the last term the spectral theorem, restricted to gauge-invariant
mean-zero functions, gives

\[
 |\operatorname{Cov}(P_TF,G)|
 \leq e^{-\varepsilon T}\sqrt{\operatorname{Var}F\operatorname{Var}G}
 \leq e^{-\varepsilon T}\|F\|_\infty\|G\|_\infty.
\]

For $r=0$ take $T=0$. This proves (14). In particular no asserted
$\sqrt\gamma$ rate, physical mass identification, or gauge fixing is needed.

**Completion of Theorem V.** If (4) failed, some sequence $M_j\to\infty$
would have $\gamma_V(\beta;M_j)\geq\varepsilon>0$.
Apply Lemma L with $V=-\log\phi_\beta$ and with two translated scores.
Their sup norms and derivative sums are fixed at this $\beta$.
Graph distance between their supports grows at least linearly with
lattice separation, up to a fixed additive constant: an adjacency step
changes each anchor coordinate by at most one, and a plaquette's links
have anchors at distance at most one from its anchor.
Pass (14) to any local limit of this sequence. It gives exponentially
decaying, hence absolutely summable, score correlations on $\mathbb Z^4$.
Section 1.3 rules this out. This proves the full limit (4), not only a
vanishing liminf. The unrestricted Langevin gap is at most the restricted
one, so it vanishes too. QED.

## 3. What this proves against a group-blind (TU) argument

There is a parameter issue in using Villain here. Its usual potential
$-\log\phi_\beta$ is not $\beta$ times one fixed function. Thus one must
not insert $\beta$ into HF4 for a fixed-action family. We instead give
an actual fixed-action counterexample to continuation by (TU).

Fix $\beta_*\geq2^{14}$ and put

\[
 A_M=\sum_pV((d_1\theta)_p),\qquad V=-\log\phi_{\beta_*},\qquad
 d\mu_{b,M}=Z_b^{-1}e^{-bA_M}\,d\theta.                       \tag{18}
\]

At $b=1$ this is Theorem V's Villain measure. Let $\gamma_M(b)$ be its
gauge-invariant Langevin gap. We next supply the uniform starting gap;
it is not taken from a recalled strong-coupling theorem.

Set $O=\max V-\min V$ and $K=\|V''\|_\infty$. Choose

\[
 b_s=\min\left(\frac12,\frac{\log2}{6(O+1)},
                         \frac1{72(K+1)}\right)>0.           \tag{19}
\]

Conditioning on all links except $e$ gives a circle law whose potential
oscillation is at most $6b_sO$. Its Poincaré gap is at least
$e^{-6b_sO}\geq1/2$. To verify this, the Haar circle gap is one by its
integer Fourier series. If $m\leq\rho\leq M_\rho$ is a probability
density relative to Haar, minimize over the centering constant and use
Haar Poincaré to get
$\operatorname{Var}_\rho f\leq(M_\rho/m)\int|f'|^2\rho$.
Here $M_\rho/m\leq e^{6b_sO}$.

Write $L_e=-\partial_e^2+b_s(\partial_eA_M)\partial_e$.
Its conditional spectral decomposition then gives
$\mu((L_ef)^2)\geq\tfrac12\mu((\partial_ef)^2)$.
Twice integrating by parts on the product of circles gives the exact
Bochner identities

\[
\begin{split}
 \mu((Lf)^2)&=\sum_{e,e'}\mu((\partial_e\partial_{e'}f)^2)
       +b_s\sum_{e,e'}\mu(A_{ee'}\partial_ef\partial_{e'}f),\\
 \mu((L_ef)^2)&=\mu((\partial_e^2f)^2)
                       +b_s\mu(A_{ee}(\partial_ef)^2).
\end{split}                                                   \tag{20}
\]

The off-diagonal Hessian has absolute row sum at most $18K$:
each link belongs to six plaquettes with three other links each.
Subtract the diagonal identities in (20), drop the nonnegative mixed
second derivatives, and use $2|xy|\leq x^2+y^2$. It follows that

\[
 \mu((Lf)^2)\geq(1/2-18b_sK)\mu(|\nabla f|^2)
                              \geq\tfrac14\mu(|\nabla f|^2).
                                                               \tag{21}
\]

Applying (21) to eigenfunctions proves $\gamma_M(b_s)\geq1/4$, uniformly
in $M$. In fact it proves the unrestricted gap bound.

Now use only the exact HF4 identity from `gap-skeleton-max.md` 1.D,
with the differentiability justification in `gap-transport-check.md`
section 2, by Claude Opus 5.5:

\[
 b\gamma_M'(b)=\gamma_M(b)
 -\frac{\mu_{b,M}(f_b(-\Delta)f_b)}{\mu_{b,M}(f_b^2)}.       \tag{22}
\]

At fixed $M$, $\log\gamma_M$ is locally Lipschitz. Comparing logarithmic
Rayleigh quotients gives Lipschitz constant $2\operatorname{osc}A_M$;
it need not be uniform in $M$. At differentiability points, any gap
mode attains the Rayleigh infimum, so (22) applies even at degeneracy.
These are the corrections already supplied by that prior check.

If (TU) held with one finite $c$, all $M$, and almost every
$b\in[b_s,1]$, (22) would give $(\log\gamma_M)'\geq-2c$.
Absolute continuity then gives

\[
 \gamma_M(1)\geq\tfrac14e^{-2c(1-b_s)}>0\quad\text{for all }M.
                                                               \tag{23}
\]

Theorem V contradicts (23). Thus, for every finite $c$, some finite $M$
has a positive-measure set of differentiability points in $[b_s,1]$
where (TU) fails. This is a theorem about a smooth compact U(1) plaquette
action in the exact fixed-action frame.

**Verdict on the method.** A proof using only compactness, smooth local
plaquette interactions, gauge invariance and HF1–HF4 cannot establish
(TU) as a continuation from a uniform strong-coupling start. That
objection is now a written theorem, not a recollection of FS.
It does not refute SU(2)'s (TU). Nor does a vanishing gap at one endpoint
refute an inequality posed only above an arbitrary $b_s$ for which no
uniform starting gap is known. The starting premise must stay attached
to the objection.

## 4. Wilson cosine: what the extension still needs

For the Wilson law, $V_b(t)=-b\cos t$ and $s_p=-b\sin((d_1\theta)_p)$,
up to an immaterial overall sign. Lemma L applies at each fixed finite
$b$. Thus it suffices to prove nonsummability of this score in every
periodic local limit at one large $b$. The fixed-boundary statement
reported in `prior/gap-lit-u1.md` does not make that assertion.

Three possible transfers were examined; none supplies it here.

1. **Density comparison.** For fixed $b,\beta$, put
   $h(t)=b\cos t-\log\phi_\beta(t)$. Its oscillation is positive: equality
   of the two normalized weights would require Gaussian Fourier
   coefficients to equal $I_n(b)/I_0(b)$ for every $n$.
   But
   $I_n(b)\geq(b/2)^n/n!\geq(b/(2n))^n$ for $n\geq1$, whereas
   $e^{-n^2/(2\beta)}$ is eventually smaller than this divided by $I_0(b)$.
   Comparing product densities by this oscillation gives factors
   $\exp(6M^4\operatorname{osc}h)$ in Poincaré comparison. This estimate
   cannot transfer the unquantified vanishing limit of Theorem V.
   It is a failure of this comparison, not a proof that Wilson has a gap.

2. **Wilson-loop monotonicity.** WV section 5 supplies monotonicity of
   cosine-character means. The required conclusion concerns centered
   score covariances, with the contact term retained. A difference
   $E(FG)-E(F)E(G)$ has no order from monotonicity of its separate terms.
   No covariance comparison with (11) is provided by that inequality.

3. **The exact positive mixture.** WV sections 2–4 represent the Wilson
   weight as a positive Hartman–Watson mixture of Villain weights.
   Partition reweighting controls specified sets of weak auxiliary
   plaquettes. Section 6 compares Wilson-loop means with Villain models
   having randomly deleted plaquettes, and explicitly leaves the
   diluted gauge-phase theorem open. The uniform fixed-stiffness affine
   Gaussian estimate (5) is not an estimate for these random laws.
   The mixture's unbounded auxiliary variances cannot simply be replaced
   by their mean; WV section 7 proves that mean infinite.

These are uses of prior work, not new claims about Fröhlich–Spencer's
published Wilson argument. Their complete original proof was unavailable
in the allowed local corpus. The report of its Wilson extension is
credited to Jürg Fröhlich and Thomas Spencer and remains a reported
literature input, not a proof of the periodic estimate in this note.
WV credits the mixture to Matsumoto and Yor, with Hariya's transform,
and its Villain monotonicity to Chevyrev and Garban; none of those
literature sources was newly fetched or silently treated as a phase theorem.

**One exact remaining Wilson statement (W-score).** For some finite
$b_*>0$, every local subsequential limit of periodic four-torus Wilson
U(1) measures at $b_*$ has

\[
 \sum_{x\in\mathbb Z^4}
 \left|\operatorname{Cov}\!\left(
 \sin((d_1\theta)_{12}(0)),\sin((d_1\theta)_{12}(x))\right)\right|
                  =\infty.                                  \tag{24}
\]

Lemma L then proves $\gamma_W(b_*;M)\to0$, with no further dynamical or
boundary-selection input. Equation (24) is not claimed here.

## 5. Final status and stop

- **Established by the written argument:** (U-tor) for Villain with
  $\beta\geq2^{14}$, all torus sizes tending to infinity; the exponential
  covariance consequence of a uniform gauge-invariant Langevin gap;
  and failure of volume-uniform (TU) continuation for the fixed U(1)
  potential (18), from the uniform start (19). The analytic input (5)
  is prior repository work. Its use and parity extension are explicit.
- **Not established:** (U-tor) for Wilson cosine, a rate such as $M^{-1}$
  or $M^{-2}$, failure or validity of SU(2)'s (TU), or (AC'-lat).
  The Villain parameter cannot be silently identified with the
  fixed-action coupling in HF4.
- **Decision:** the compact-group-blind continuation method is ruled out
  at the scope in section 3. This warrants that method-level discard.
  It does not warrant saying that the cosine-specific sentence in 4.2
  has been proved. The missing Wilson statement is exactly (24).
- **Stop:** Villain (U-tor), the first requested test, is obtained.
  Following the instruction to stop on that outcome, no SU(2) cancellation
  or tunnelling attempt is made. Those heuristics receive no new status.

No numerical runner, simulation, formal verifier, audit, or independent
proof check was run. Only this output file is changed. The note requests
one independent check of sections 1.1–3 before downstream reliance,
particularly the reuse of PV, the all-size extension, and the restricted
semigroup estimate. This request starts no checker or outward action.
