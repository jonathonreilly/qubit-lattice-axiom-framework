# Repo search

Codex, row 1257, requested configuration GPT-6.2 Astra/max. Hand check of Claude Opus 5.5's row 1251 at `a52ed5a57`, 20 November 2026. Research only. This record grants no status.

The lead's 8 November digest covers main and PRs 10114, 10133, 10134 and 10141. It predates Zeng's v1 of 17 November and concerns other obligations. There is no target-specific prior file. I searched for the paper number, author and check name outside this lane in Markdown and TeX on main `8b11ae2bb` and PRs 10114, 10133, 10134, 10141 and 10144 (`f76f6c649`, `89faef229`, `1e70c7211`, `a2f6a430e`, `1f20846b8`). No matches. The registry has no competing Zeng row. FINISH 1251 names 1257 as its checker.

In this checkout, row 1218 already states the three hypotheses and the conditional rate. Row 1220 distinguishes the transfer and spatial gaps at zero coupling. Row 1234 observes the flat connections and flags the slice issue. Lemma TYP supplies the one-link staple reduction with a Chebyshev tail. Row 1201 already gives the instanton power. Row 1218, line 235, already names Proposition 13.4. The detailed check of its proof is the contribution at issue in row 1251, lines 129–131 and 229–236. [Row 1218](prior/gap-onebound-read-sol.md#c--zengs-common-rate-and-the-later-tunneling-package), [row 1220](gap-mini-solve-p-fable.md), [row 1234](gap-mini-solve-v-opus.md), [Lemma TYP](explicit-region-two-step.md), [row 1201](gap-mini-solve-j-fable.md), [row 1251](gap-mini-solve-ad-opus.md).

## Plan

1. Check the prior-work record, repository hits, task instructions and ownership.
2. Locate the primary texts and read the relevant index rows and source ranges.
3. Check the readings of (TUN) and (SPEC) against the cited statements.
4. Check Lemmas Z1 and Z2 and Corollary Z2′, including their proofs.
5. Check Lemmas Z3 and Z4 and their proofs.
6. Decide what follows for Proposition 13.4 and Remark B.15.
7. Check the tensorization argument and identify the surviving route.
8. Verify the verdicts and record the result.

## Sources checked

The primary text is Chunping Zeng, Hexagon 2611.00543v1, pp. 45–50 and 53–57. I also checked (4.1)–(4.3) for the measure, (10.1)–(10.2) for a Gaussian example, and §§10.3–10.4 for the transfer transform and the quantifiers on the gap. PDF SHA-256 `c13d37a9f00c2d4f94fe21b258e27c5205534cf2d2a59da57e44e21687e703a6`. Page and equation references below are to this version. [Primary PDF](https://hexagonmath.org/pdf/2611.00543v1).

I searched the Sussman–Alpoge outline chunks, obligations and CA-I 4.12–4.19 index for the tunneling, two-well, Muckenhoupt, transfer-form and certificate terms. In chunk 01, source lines 248–278 give the orientation-invariant plaquette action and the elementary finite Gibbs normalization. Lines 588–599 there and 31871–31882 in chunk 29 distinguish clustering from exclusion of low spectral support. CA-I 2704–2711 explicitly lists the mass gap outside its theorem. This material belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Outline at the specified revision](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L588-L599), [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2711).

## The tunneling and spectral hypotheses

**(TUN) as a description of this route — HOLDS AFTER CORRECTION** (row 1251, lines 68–77, 88–90, 114–129, 247). In (11.4) the chart covers a neighbourhood of the chosen path. It requires uniform Morse curvature bounds at the specified critical points, a bounded residual with four bounded transverse derivatives, and a uniformly bi-Lipschitz chart. The two minima of $\Phi_p$ have value zero. The lower of its two saddle heights is $\Delta=c_KB_*$. The designated well-to-saddle action rise is $\kappa_N\Delta+O(1)=\beta_N/(2b_0)+O(1)$, by (11.1) and bounded $\Psi_p$. This describes that channel. A minimax over the whole configuration space would require a separate argument. Part I uses $\beta=1/g_0^2$ in (4.3).

**(TUN) equivalent to a mass gap without qualification — FAILS** at lines 125–126 and 247. Remark 11.2 restricts the necessity of constructing these data to a proof *by Part II's route*. Remark 14.3 uses stronger equivalence language and points back to that remark and Proposition 10.26. Proposition 10.26 formulates (MG) as a common exponential rate over volumes and label words. It leaves the ultraviolet implication from (MG) to (MG2″) open and supplies no construction of wells from a gap. Even sufficiency in Theorem 14.1 invokes (COH), (SPEC) and Proposition 13.4. For a simple illustration, on a circle of circumference $2\pi$ with uniform measure take $H_N=a_N(-\partial_s^2)$ and $T_N=e^{-H_N}$. Fourier modes give physical gap one. A constant action cannot rise by $\kappa_N\Delta+O(1)$ for fixed $\Delta>0$. This distinguishes the predicates in general. A converse for Wilson SU(2) remains unestablished.

**(SPEC) for the temporal form — HOLDS** (lines 78–82, 110–112). In Lemma B.1 the normalized transfer operator has constant ground vector and $H_p=-\log T_p$. For $g=f-\mu_p f$, the variance is $\|g\|^2$ and the form is $\|H_p^{1/2}g\|^2$. The spectral theorem on $1^\perp$ bounds the quotient below by $\inf\sigma(H_p|_{1^\perp})$. Spectral vectors at that edge approach equality. Undoing the top-eigenvalue normalization gives $-\log(\lambda_2/\lambda_1)$. For an operator originally on Haar space one also conjugates by its positive ground vector to make the stationary vector constant (Lemma 10.11). The identity gives no comparison to a sum of spatial bond gradients. Appendix B.1 explicitly leaves that step open. Equality of rates is the stated (SPEC). On a common measure and variational domain, $\mathcal E^{\rm tm}\ge c\,\mathcal E^{\rm sp}$ with uniform $c>0$ would already transfer a spatial lower bound.

**(COH) as a partial reduction — HOLDS AFTER CORRECTION** (lines 83–87, 123–125). The quaternion identities and the exact current counting in B.5–B.6 survive. B.10 restricts its algebra to the one-step kernel and leaves the design bound and multi-bond transport open. B.8 supplies analytic endpoints and labels its interior constant numerical. B.13 draws its harmonic constants from percolation networks and leaves shared-link Wilson correlations outside that calculation. In (B.5) $B_N$ is a density, whereas §11.2 writes the sum. A uniform density bound alone does not control the sum as the number of bonds grows. Even B.2's universal fourth-power small-ball asymptotic needs a hypothesis on the weights. If $w_1>1/2$, the triangle inequality gives $|\sum w_xq_x|\ge 2w_1-1>0$. A blanket endorsement of all the one-bond probabilistic claims would go beyond the algebra.

## The tube and the Wilson energy

**Z1, the local obstruction — HOLDS AFTER CORRECTION** (lines 107–109, 182–195, 251). Use the gradient form integrated against the stated probability measure. For a product law its gap is the smaller of the factor gaps. Testing functions of either coordinate gives the upper inequality. For the lower one, decompose the variance into the mean conditional variance and the variance of the conditional mean. Apply each factor inequality and Jensen's inequality to the derivative of the mean.

Here is a direct check of the exponential upper bound in the toy. Around both maxima of $\chi$, let a function switch between $+1$ and $-1$ on intervals of width $\kappa^{-1/2}$. Its slope is $O(\sqrt\kappa)$ and $\chi\ge\Delta'-C/\kappa$ on those intervals. Near each quadratic minimum an interval of the same width supplies mass at least $c/\sqrt\kappa$ before normalization. The total unnormalized mass is at most $C/\sqrt\kappa$, by the local quadratic lower bounds and positivity away from the minima. Thus the variance stays above a positive constant and the energy is at most $C\kappa e^{-\kappa\Delta'}$. This proves the claimed separation of rates when $\Delta'>\Delta$, without importing Lemma 13.1.

The row correctly retracts its first chart as an example meeting all the local bounds. In $t$ the second derivative is $\kappa\chi''$ at the minimum. The inverse Lipschitz constant diverges in the rescaled coordinate. One can satisfy both local bounds in a slight variant. On a fixed transverse circle choose smooth $0\le h\le D$, zero on intervals about $0,\pi$, and equal to $D>\Delta$ on two strips separating them. Take the product action

$$
 S_\kappa(s,t)=\kappa\Phi(s)+\kappa h(t)+1-\cos(2t).
$$

In the first zero interval the identity chart is isometric and $\Psi=1-\cos(2t)$ has bounded derivatives. Both low intervals have probability bounded below independently of $\kappa$. A function of $t$ taking opposite signs there can make both transitions inside the high strips at fixed slope. Its quotient is $O(e^{-\kappa D})$. This is a counterexample to deriving a global lower bound from the local geometry alone. It makes no claim about the Wilson-specific (COH). The upper-bound claim in lines 108–109 requires extending the proposed tube test with controlled global energy and variance. Also, (TUN) puts no lower bound on the width of $Y_p$. A uniformly parametrized interval can shrink with $p$. One cannot deduce the asserted incompatibility with bond concentration from these chart bounds.

**Z2 — HOLDS** (lines 135–162, 249). Write $q$ for the number of incident plaquettes, $r$ for the norm of their staple sum and $x=\kappa' c r$. Cyclicity and invariance of the real SU(2) trace under inversion handle both link orientations. Since each plaquette uses the link once, its staple is fixed by conditioning. The quaternion sum has $0\le r\le q$. At $r=0$ choose any frame. Under Haar the framed angle has density proportional to $\sin^2\phi$, and conditioning multiplies it by $e^{x\cos\phi}$. Integrating the derivative of $\sin^3\phi\,e^{x\cos\phi}$ gives $3R=x\mathbb E\sin^2\phi\le 2x(1-R)$, where $R=\mathbb E\cos\phi$.

For a separate check of the constants put $u=\kappa'cq$ and $h(x)=3x/(3+2x)$. Then $0\le h'\le1$. The weighted conditional local energy is

$$
 u-x+x(1-R)\ \ge\ u-x+h(x)\ \ge\ h(u)\ \ge\ \tfrac12
$$

when $q\ge4$ and $\kappa' c\ge3/8$. This includes $x=0$ and confirms the two cases in lines 155–157. Counting the four links of each plaquette gives $\mathbb E_{\kappa'} S_{\kappa'}\ge |E|/8$. For $F(v)=\log Z(v)$, the bounded finite-lattice energy $W=S_v/v$ gives $F'=-\mathbb E_vW$, $F''=\operatorname{Var}_v W\ge0$. Hence

$$
 F(2\kappa)-F(\kappa)\le\kappa F'(2\kappa)
 =-\tfrac12\mathbb E_{2\kappa} S_{2\kappa}\le-|E|/16 .
$$

On $S_\kappa\le t$ one has $1\le e^{t-S_\kappa}$. Integration gives the stated bound $e^{t-|E|/16}$ for every real $t$ and $\kappa c\ge3/16$. The one-link law is the prior Lemma TYP's input. The partition-function ratio gives the exponential tail.

**Z2′, conditional inequality — HOLDS** (lines 164–174, 250). Assume the three-dimensional periodic product-Haar Gibbs law, the same unshifted action $S=\kappa_N c\sum_\square(1-\tfrac12\operatorname{tr}U_\square)$, and uniform $\sup_{N_p}\Phi_p\le M$, $\sup_{N_p}\Psi_p\le C_0$. Then $N_p\subseteq\{S\le\kappa_N M+C_0\}$. Z2 bounds its mass by $\exp(\kappa_N M+C_0-|E_p|/16)$. At fixed physical $L>0$, $|E_p|=3(L/a_N)^3$ and $\kappa_N=O(\log(1/a_N))$. The exponential beats every power of $a_N$.

**Z2′, identification of its Gibbs law from §12 — FAILS** at lines 165–167. Equation (4.3) is a four-dimensional law. Integrating out the other links leaves an integral over mixed and off-slice plaquettes multiplying the spatial plaquette weight. One would have to show that this factor is constant, or that it reduces to the stipulated change of plaquette coupling. For the normalized transfer description, the stationary measure in Lemma 10.11 is $h^2 dm/\int h^2dm$, where $h$ is the Perron vector for the original reference measure $m$. Neither description identifies this density with the three-dimensional Gibbs law above. Section 12 uses a weighted average $Q_b$ of transported quaternions in a *conditional block cost*. Its angular dependence also occurs for a staple sum. This fact specifies neither the slice joint law nor the absolute additive constant of the action in (11.4). Proposition 10.14 discusses a reference-layer kernel, which does not make this identification for all fine layers.

The uniform $M$ is also extra. (TUN) fixes the lower saddle and local curvatures. On the other arc one can add $K\eta(\Phi)$ with $\eta$ smooth, nondecreasing, zero near the minima and one near that higher saddle. This retains the critical points and their curvatures while the upper height grows with $K$. The ground-state mean estimate suggested at lines 178–180 also leaves the tail uncontrolled. Partition a reference probability space into sets of sizes $1/(1+e^{2n})$ and $e^{2n}/(1+e^{2n})$ and put stationary probability $1/2$ on each set, with constant density there. The log-density deficit from its maximum is $0$ or $2n$, with mean $n$ and probability $1/2$ at zero. Transferring the exponential tail requires control of the low-action event itself.

## Barrier scaling and the Gaussian statistic

**Z3, fixed-barrier calculation — HOLDS** (lines 197–203). Under its stated two-sided bounds on $C_N$,

$$
 \frac{\rho_N}{a_N}=C_N e^{-\bar\beta S_{\rm cl}}a_N^{2b_0 S_{\rm cl}-1}.
$$

A positive exponent gives zero in the limit and a negative exponent gives divergence. At exponent zero the rate stays bounded above and away from zero. Convergence would require control of $C_N$ beyond these bounds. With $2b_0=11/(12\pi^2)$ the critical action is $12\pi^2/11$. Actions $8\pi^2$ and $4\pi^2$ give exponents $22/3-1=19/3$ and $11/3-1=8/3$. These are computations for the stipulated actions and prefactors. Identifying either action with a Wilson slice barrier is a further premise.

**Z3, a running barrier is necessary — FAILS** at lines 203–205 and in the gloss at 270–272. The fixed $S_{\rm cl}=12\pi^2/11$, $C_N=1$ gives a positive constant physical rate. Zeng's choice $c_K\kappa_* B_*=1/(2b_0)$ gives precisely this exponent. It supplies no microscopic realization. In lines 252 and 274 the appropriate condition is *bounded above and bounded away from zero*. Zero is itself a finite limit, and at the critical action an oscillating bounded prefactor need not converge.

**Z4, the autocorrelation inequality — HOLDS** (lines 209–225, 253), for a normalized spectral autocorrelation with $V>0$ and $G(V)<1$. For $X=e^{-V\lambda}$ under the unit-mass spectral measure set $g=\mathbb E X$. Then

$$
 0\le \alpha_V=\frac{\operatorname{Var}(X)}{1-g^2}
 \le \frac{g-g^2}{1-g^2}=\frac{g}{1+g}<\tfrac12 .
$$

Here $X^2\le X$. Positivity of the numerator uses the spectral-measure interpretation. Monotonicity alone in line 214 suffices for the upper estimate. The pure vacuum has $g=1$ and an undefined quotient. Nonzero centered field vectors in a simple-vacuum model avoid this case. The same $1/2$ bounds the supremum for every volume and every such word.

The natural autocorrelation has direct support in Zeng's text. Proposition 10.15 uses the Laplace transform of a field-vector spectral measure. In (10.1)–(10.2) the centered Gaussian field has

$$
 G(V)=\sum_{j\ge1}2^{-j}e^{-V2^{-j}},\qquad
 \widetilde\rho=\sum_{j\ge1}2^{-j}\delta_{2^{-j}},\qquad \rho=\delta_0+\widetilde\rho .
$$

In particular $G(0)=1$ and $\rho((0,\varepsilon))>0$ for every $\varepsilon>0$. One can realize this single fixed example with independent centered Gaussian modes of covariance $e^{-m|t-u|}$, $m=2^{-j}$, weighted in variance by $2^{-j}$. The covariance is positive since it is the Gram kernel of $\sqrt{2m}\,e^{-m(t-v)}\mathbf1_{v\le t}$ in $L^2(dv)$. On positive times its reflected kernel is $e^{-mt}e^{-mu}$. Taking sums preserves positivity and the Gaussian field exists by its consistent finite-dimensional laws. The low-energy atoms are already visible to the linear field. This checks the counterexample using the paper's own two-point data, independently of any assertion about its full multiparticle spectrum.

## Consequences for the two disputed statements

**Proposition 13.4, lower bound unproved by the displayed argument — HOLDS AFTER CORRECTION** (lines 92–112, 174–180, 248–250). The first missing inference is from the neighbourhood in (11.4) to (13.1) for the full form and the full variational domain in (11.3). Coarea on a chart computes the chart contribution. A uniform Poincaré lower bound must control the variance of every admissible global test, including variation in the exterior and differences between the two regions. The hypotheses give no full-measure covering, exterior inequality or comparison that accomplishes this.

Under the extra raw-action assumptions of Z2′, for fine lattices the open set $\{S>\kappa_N M+C_0\}$ has positive measure. A smooth nonconstant function of the action can vanish on the tube and vary on that open set. Its local contribution is zero and its global spatial-gradient energy is positive. On the paper's actual slice law the size of the tube remains undetermined. The passage from local to global is still missing. Small tube mass by itself would never disprove a lower bound for the true gap. The counterexample in Z1 tests the local argument outside the Wilson family. No Wilson counterexample to (13.4) or Theorem 14.1 follows here.

**Remark B.15, upper-bound test implies a gap — FAILS as printed. Row 1251's refutation of this direction — HOLDS** (lines 209–226). This is the right-to-left implication in the printed display. Take $\delta=1/2$ and any $V_0>0$. Z4 supplies its right side for every normalized nonconstant spectral autocorrelation. The single Gaussian example (10.1)–(10.2) violates its left side. Taking the same spectral data at all indices suffices. Row 1251 gives a second counterexample. A normalized free spatial zero mode of mass $1/p$ has $G_p(V)=e^{-V/p}$ and $\alpha_V^{(p)}=0$ for every $p,V>0$. No common interval above zero is empty. Even a fixed single mass $m<\log 2/V_0$ contradicts the advertised numerical threshold. The forward implication is automatic on this domain.

There is a second equality in the first display of B.15, omitted at lines 211–215. It gives $\int e^{-V\lambda}\,d\widetilde\rho_p/\int(1+e^{-2V\lambda})\,d\rho_p$. B.15 asserts the equality for free models and supplies no new definition of the tilde. With the vacuum subtraction used in (10.2), $0\le\widetilde\rho_p\le\rho_p$, and $2x\le1+x^2$ for $x=e^{-V\lambda}$. This second ratio also always passes the same upper test. The two ratios differ already for $\rho=\delta_0+\delta_m$ and $\widetilde\rho=\delta_m$. The first gives zero and the second gives $x/(3+x^2)>0$. Thus the omitted formula offers no rescue on the paper's exhibited spectral convention. The false equivalence is the one asserted for Gaussian models. B.15 itself treats the extension to non-Gaussian mixing as a strategy. Neither use of the statistic is a premise of Theorem 14.1. [Remark B.15, p. 57](https://hexagonmath.org/pdf/2611.00543v1#page=57).

## Tensorization and the surviving conditional argument

**The ARGUED objection to tensorization — HOLDS** (lines 94–106, 248). Section 12 conditions or frames one bond. In §13 the transverse fibre at fixed $s$ carries a joint law. B.3 concerns correlations under a Haar prior. B.7–B.10 concern moments or path flows. None gives a product decomposition or a uniform inequality bounding the joint variance by the sum of conditional bond energies for the Wilson fibre.

The SU(2) ring illustration in lines 101–105 can be justified without assuming the disputed radial asymptotic. For a framed one-site density $q_x(\phi)\propto\sin^2\phi\, e^{x\cos\phi}$, $x\ge0$, the mode $m$ solves $2\cos m=x\sin^2m$. The density increases up to $m$ and decreases afterwards. On the right, integrate $|g(t)-g(m)|^2\le\pi\int_m^t|g'(r)|^2dr$ against $q_x(t)$. For $m\le r\le t$ use $q_x(t)\le q_x(r)$. The same integration on the left gives $\operatorname{Var}_{q_x}(g)\le\pi^2\int |g'|^2q_x$. Angular conditional variance is bounded by half the angular gradient energy on the unit two-sphere. The spherical metric weights that energy by $1/\sin^2\phi\ge1$. Variance decomposition and Jensen therefore give a full one-site gap at least $1/\pi^2$ for every concentration, including zero.

For the interacting ring take density proportional to $\exp[-K\sum_i(1-u_i\cdot u_{i+1})]$ on $(S^3)^n$. Every one-site conditional is of that framed type. Each site is Haar by common rotations. For fixed $n$, the energy has its minimum exactly on aligned configurations. On the complement of any neighbourhood of the diagonal it has a positive minimum $d$, and $\{E<d/2\}$ has positive Haar mass. The probability of that complement tends to zero as $K\to\infty$. For a smooth, nonconstant, Haar-centered $g$, the average $f=n^{-1}\sum_i g(u_i)$ consequently has variance tending to $\int g^2\,dHaar$ for fixed $n$. Choose $K=K_n$ large enough for at least half this variance. Its product-metric gradient energy is at most $\|\nabla g\|_\infty^2/n$. Thus all one-site gaps stay positive uniformly while the joint gap is at most $C/n$. This checks the example along a chosen sequence and disproves the proposed general tensorization inference. A Wilson-specific joint estimate remains possible.

Even a supplied uniform fibre gap controls only the conditional-variance term. When the conditional density $r_s(y)$ is differentiable in $s$, the derivative of $\int f r_s\,dy$ includes $\int(f-\mathbb E_s f)\,\partial_s r_s\,dy$. The longitudinal marginal also contains the integrated fibre weight. To conclude that a minimizer is a function of $s$ alone or to compare the full quotient uniformly, §13 must handle this dependence and the global configuration space.

**The endorsement of Lemmas 12.1 and 13.1 as written — FAILS** at lines 97–98 and 123–125. Two narrower one-dimensional results survive.

* **Lemma 12.1 — HOLDS AFTER CORRECTION.** The Haar formula (12.2), uniform conditional angles and the unit-sphere angular gap $2$ hold. Equation (12.3) prints a leading radial coefficient of $1$. The proof uses the limiting Maxwell generator and obtains $2$. The rescaled density is only asymptotically Maxwell. A factor of two cannot be absorbed in a relative error tending to zero. In fact the radial gradient form printed on p. 48 has gap $2\lambda+O(1)$, as the hand bounds below show.
* **Lemma 13.1 — HOLDS AFTER CORRECTION.** For fixed smooth Morse data, on the arc through the lower saddle a well integral has order $\kappa^{-1/2}$ and an inverse-density saddle integral has order $e^{\kappa\Delta}\kappa^{-1/2}$. Taylor's two-sided quadratic bounds give these orders within fixed small neighbourhoods. Compactness gives exponential improvement outside them. Normalizing constants cancel in (13.2). Taking the split after the well and before the saddle gives the lower product bound. Extending each factor to the whole arc gives the upper. This proves the logarithmic order (13.3) on that arc. A Morse circle with two minima needs two maxima, as Remark 13.2 recognizes. A well-to-split integral beginning at the minimum has a half-well Gaussian contribution. The log-order estimate and a two-sided comparison do not identify a universal sharp prefactor in (13.5).

The lower saddle controls the ordinary one-dimensional gap even if the two saddles differ. Divide the circle into the two basins ending at the maxima. The anchored variance estimate just used for a unimodal density bounds $\int_{\mathrm{basin}}|f-f(w)|^2d\sigma$ by a fixed constant times its gradient energy. Cauchy–Schwarz along the lower-saddle arc bounds the squared difference of the two well values by the energy times $Z_\kappa\int_{\rm arc}e^{\kappa\Phi}ds=O(e^{\kappa\Delta}/\kappa)$. Combining the two estimates bounds the full variance. The switching test in Z1 gives the opposite inequality for the gap. Hence the unscaled one-dimensional gap is of order $\kappa e^{-\kappa\Delta}$ for a fixed potential. Passing this estimate uniformly through a family requires uniform control of the relevant neighbourhoods. Curvatures at the critical points alone give no uniform Taylor error.

<details>
<summary>Hand check of the coefficient in (12.3)</summary>

For the upper bound set $X=\lambda(1-\cos\phi)$. Its density is proportional to $x^{1/2}e^{-x}\sqrt{(1-x/(2\lambda))_+}$. The square-root factor differs from $1$ by at most $x/(2\lambda)$ everywhere. Integration by parts for the first two gamma moments gives $\mathbb E X=3/2+O(1/\lambda)$ and $\mathbb E X^2=15/4+O(1/\lambda)$. Thus $\operatorname{Var}X=3/2+O(1/\lambda)$ and its gradient energy is $\mathbb E(2\lambda X-X^2)=3\lambda+O(1)$. Its quotient is $2\lambda+O(1)$.

For the lower bound use $q=q_\lambda$, $b=q'/q=2\cot\phi-\lambda\sin\phi$ and $D v=-v''-bv'-b'v$. For smooth centered $g$ put $v=q^{-1}\int_0^\phi q g$. Then $(qv)'=qg$ and $v=O(\sin\phi)$ at both ends. For the positive interior weight $w=\sin\phi\,e^{\lambda(1-\cos\phi)^2/4}$, two integrations by parts give

$$
 \int g^2 q=\int (v'^2-b'v^2)q
 =\int w^2|(v/w)'|^2 q+\int (Dw/w)v^2 q .
$$

The boundary terms vanish because $q$ vanishes quadratically. Writing $z=\cos\phi$, direct differentiation gives

$$
 Dw/w=3+\lambda(3z^2-z/2-1/2)+\tfrac14\lambda^2(1-z^2)^2
 \ \ge\ 2\lambda-6 .
$$

Indeed for $t=1-z^2$, the right side before the bound is at least $3+2\lambda-3\lambda t+\lambda^2t^2/4$, and completing the square gives the inequality. Also $\int g^2q=-\int g'vq$. Cauchy–Schwarz now gives $(2\lambda-6)\int g^2q\le\int g'^2q$ for $\lambda>3$. Closure gives the same inequality on the form domain. The upper and lower bounds settle the coefficient for the form used in the paper.

</details>

**The passage from a spatial rate to Theorem 14.1 — HOLDS AFTER CORRECTION** (lines 43–46, 92–94, 110–112, 123–131). The proof of Proposition 13.4 explicitly divides the unscaled one-dimensional rate by $\kappa_N$ on p. 49. Such a division rescales a Dirichlet form. Identifying that normalized form, or its gap, with the physical transfer log-gap remains an input. A valid *unscaled* lower bound stronger by $\kappa_N$ could still suffice for a fine-layer lower bound, given the matching (SPEC). This factor alone does not defeat that one-sided implication.

Given a full, correctly normalized slice bound $\rho_{\rm latt}\ge c\,e^{-\kappa_N c_K B_*}$ uniformly on fine lattices and (SPEC) for that rate, (11.2) gives $\|T_p|_{\Omega^\perp}\|\le e^{-c A a_N}$ for the normalized operator. In (13.4)–(13.6) one could take $c=\Lambda_-/2$ once the uniform error is small. With the spectral convergence used by Theorem 10.17, an interval excluded from all sufficiently fine measures stays empty in the subsequential limit. Each continuous test compactly supported in that interval has zero integral in the limit. Density of the field-word vectors then gives the exclusion for the Hamiltonian. To assert (MG2″) at *every* cutoff, p. 50 also takes a minimum over the coarser layers. There are finitely many such $N$ but infinitely many spatial volumes at each $N$ by (4.1). Pointwise positive gaps can tend to zero with volume. A uniform coarse-layer bound would be needed for that stronger assertion. The fine-cutoff limiting argument has no such requirement.

## Verdict for the route

**Row 1251's conclusion about what can be used — HOLDS AFTER CORRECTION** (lines 126–131, 267–274). Zeng supplies the scale match, the one-bond reduction, the fixed-potential barrier order with the corrections above, and the log-transfer variational identity. The conditional step from a full, volume-uniform transfer bound to spectral exclusion survives. The derivation of that bound for Wilson SU(2) still needs control outside the tube, a joint transverse variance bound and a comparison with the transfer form at the claimed normalization. As Remark B.14 explains, using a reference-layer strong-coupling estimate at the fine layers would still require cross-layer control. The failure of B.15 removes the proposed Gaussian certificate. These findings identify an unfinished route. They provide no exclusion of future tunneling proofs or of mechanisms outside the texts examined. Row 1251's stronger literature-wide conclusion exceeds its evidence. The one-coupling seed, (N-phys) and (NS-gap) remain open.

RESULT: Row 1257 checked row 1251 by hand. Z1 holds with the chart correction, Z2 and Z3's scaling hold, and Z2′ holds for its extra Gibbs law. Proposition 13.4's global lower bound and interacting tensorization remain unproved. Z4 refutes the upper-bound-to-gap direction of Remark B.15 for Gaussian models. The downstream transfer implication survives conditionally. The four-dimensional SU(2) Yang–Mills mass gap remains open.
