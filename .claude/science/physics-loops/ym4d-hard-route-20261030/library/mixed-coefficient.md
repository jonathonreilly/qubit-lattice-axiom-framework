State of attack

**Gap — completed; verdict undecided at (43), specifically (15) below.** The target is (43) of `library/tail-two-step.md`, with its mixed coefficient (35)–(37), marginal subtraction (41), and source insertion (44)–(46). The normalized coefficient is reduced below to connected density scores. An exactly integrable Gaussian test has a nonzero spectator-variance term after marginal subtraction, but its distance factor can pay for it; this is not an SU(2) counterexample. The outstanding step is the corresponding connected-score estimate for the actual inverse-coordinate density and its denominator.

**Discharged — procedure and provenance.** Read `GOAL.md` and `FINISH-rules.md` first, then `library/tail-two-step.md` in full. Working in the filtered directory identified by the user as commit `d8accf132`; that identifier is supplied, not independently verified. This is a written mathematical investigation by OpenAI Codex, not an audit. No numerical computation, machine enumeration, external lookup, git operation, or subagent is used. Only this file is being written.

**Discharged — test and its limit.** Write I for `parts/hard-core--independent.md`. In I:988–1010 the smoothing estimate is used when $t_\#\leq c$. Its continuation bound (43) and its Taylor remainder bound (42) are different assertions. A failure of the remainder would not, by itself, falsify the continuation bound. The test below retains the quotient, uses a three-component near variable (so the old factor can be invariant under colour rotations), and lets the far site change only the mean or the spectator covariance. Changing a near row of the strictly local matrix $P$ through a site outside its locality range would contradict I:772–801 and is not an admissible test.

**Discharged — quotient reduced to connected coefficients.** Fix one of the site states $r=0,1$, and a fixed value of the continuation parameter. On the fixed real-coordinate cut of (43) write the complete unnormalised density as $q_r(w)$, and the old factor as $E_r(w)$. This notation includes the Jacobian, the original Gaussian once, the analytic weight, and all other variables still integrated. Expand

\[
 q_r(w)=q_{r,0}\{1+wU_r+w^2V_r+O(w^3)\},\qquad
 E_r(w)=E_{r,0}+wE_{r,1}+w^2E_{r,2}+O(w^3).
 \tag{1}
\]

At a real base put $\langle H\rangle_r=(\int q_{r,0}H)/(\int q_{r,0})$. Algebraic division of the numerator by $\langle1+wU_r+w^2V_r\rangle_r$ gives exactly

\[
 [w^2]\Gamma_r
 =\langle E_{r,2}\rangle_r+
 \operatorname{Cov}_r(E_{r,1},U_r)+
 \operatorname{Cov}_r(E_{r,0},V_r)
 -\langle U_r\rangle_r\operatorname{Cov}_r(E_{r,0},U_r).
 \tag{2}
\]

Here $\operatorname{Cov}(A,B)=\langle AB\rangle-\langle A\rangle\langle B\rangle$, with bilinear products. To check (2), multiply the numerator coefficients by $1-w\langle U\rangle+w^2(\langle U\rangle^2-\langle V\rangle)$. In particular a constant old factor has zero coefficient: the apparent density term cancels against its denominator. The mixed remainder is the difference of (2) at $r=1,0$, minus the specified $[w^2h]\mathcal M$. A large absolute bound on one numerator term is not a lower bound on this expression.

**Discharged — the cut-normalization ratio is retained.** In (2), $\Gamma_r=(\int q_rE_r)/Z_r$ with $Z_r=\int q_r$. Denote the denominator actually written in (43) by $N_r=N_{\rm good}^Z(W_\zeta)$ and put $\theta_r=Z_r/N_r$. Then (43)'s integrand after integration is $\theta_r\Gamma_r$, exactly. If the denominator uses the identical new cuts, $\theta_r=1$. If it keeps the original cuts, this ratio must be bounded along with the claimed cut-replacement error; it cannot be set to one. Writing $\theta_r=\theta_{r,0}+w\theta_{r,1}+w^2\theta_{r,2}+\cdots$ gives

\[
 [w^2](\theta_r\Gamma_r)
 =\theta_{r,0}\Gamma_{r,2}+\theta_{r,1}\Gamma_{r,1}
                           +\theta_{r,2}\Gamma_{r,0}.
 \tag{2a}
\]

**Implication — use at complex continuation parameter.** The same formulas apply algebraically when $Z_r(0)$ and $N_r(0)$ are nonzero; the bracket is then a normalized complex functional, not a probability expectation. The estimates establishing their nonvanishing uniformly in the full coefficient algebra, and controlling $\theta_r$, are not assumed proved here.

**Discharged — a legitimate local old factor.** Fix a plaquette $p\subset P$, put $\varepsilon=cc_j\omega_P$, and choose

\[
 e_P(V)=\varepsilon\left(1-\exp\left\{-\frac{|V_p-1|^2}{2g^2}\right\}\right).
 \tag{3}
\]

It is bounded, measurable, gauge invariant, and has no far-field or far-site coefficients at fixed near data. For $u\geq0$, $1-e^{-u}=\int_0^u e^{-s}ds\leq u$. Hence $|e_P|\leq\varepsilon |V_p-1|^2/(2g^2)\leq\varepsilon t_P^2/2$, since $D_P^+\geq1$ and $p$ belongs to the support. Thus it satisfies the stated C-factor bound, including (TAIL), at every real base. This is a permitted input to the claimed smoothing lemma; it is not asserted to be an activity actually produced by a preceding RG step.

**Discharged — smallest explicitly integrable test.** The following calculation is a Gaussian test of the mechanism, not an evaluation of the SU(2) chart. Let $h^2=h$, $r=h\in\{0,1\}$, $\xi,\eta$ be independent standard three-component Gaussians, and

\[
 X=(aw+rb)\mathbf e_1+\xi+r\sqrt\delta\,\eta,
 \qquad e(X)=\varepsilon(1-e^{-|X|^2/2}),\qquad 0\leq\delta\leq1.
 \tag{4}
\]

The local noise coefficient is identical in both states. The site changes a spectator coefficient and a mean. $X$ represents a linearized plaquette flux divided by $g$; (4) is the quadratic-density version of (3). No identification of its constants with an actual lattice covariance is being made. At fixed $X=x$ the old factor has no $w$ dependence, so this is precisely a density-coefficient test. Put $d_r=2+r\delta$, $m_r=aw+rb$. Completing the square in each real Gaussian component gives

\[
 \Gamma_r(w)=\varepsilon\left[1-d_r^{-3/2}
        e^{-m_r^2/(2d_r)}\right],\qquad
 [w^2]\Gamma_r=
 \frac{\varepsilon a^2}{2d_r^{5/2}}
 e^{-r b^2/(2d_r)}\left(1-\frac{r b^2}{d_r}\right).
 \tag{5}
\]

For verification, if $Z$ has variance $\sigma^2$, the exponent in its one-dimensional integral is

\[
 -\frac{(x-m)^2}{2\sigma^2}-\frac{x^2}{2}
 =-\frac{1+\sigma^2}{2\sigma^2}
       \left(x-\frac{m}{1+\sigma^2}\right)^2
       -\frac{m^2}{2(1+\sigma^2)}.
\]

Changing the integration variable therefore gives $(1+\sigma^2)^{-1/2}e^{-m^2/(2(1+\sigma^2))}$. The sum $\xi+r\sqrt\delta\eta$ has variance $1+r\delta$: the orthogonal change $(\xi,\eta)\mapsto((\xi+\sqrt\delta\eta)/\sqrt{1+\delta},(\eta-\sqrt\delta\xi)/\sqrt{1+\delta})$ preserves the product Gaussian. Multiplying the three component integrals proves (5). The denominator is exactly one, rather than an omitted normalization.

For complex $m$ the same integral formula needs no assumed contour shift. Let $F(m)$ be its one-dimensional integral. On a compact set of $m$, every differentiated integrand is bounded by a polynomial in $|x|$ times $e^{-c x^2+C|x|}$, with $c>0$, so differentiation under the integral is valid. Integration of the derivative of the integrand in $x$ gives $\int x\,(\text{integrand})\,dx=mF(m)/(1+\sigma^2)$. Hence $F'(m)=-mF(m)/(1+\sigma^2)$, and differentiation shows $e^{m^2/(2(1+\sigma^2))}F(m)$ is constant. Its value at zero is the real Gaussian integral just evaluated. This proves (5) also for the complex continuation used below.

**Discharged — marginal subtraction in the test.** The flat-state quadratic form is

\[
 \mathcal M_r(w)=\frac{\varepsilon}{2\,2^{5/2}}(aw+rb)^2.
\]

Its mixed coefficient $[w^2h]\mathcal M$ is zero, because the coefficient of $w^2$ is the same in both states. Thus the explicit remainder is

\[
 \boxed{\mathcal R_{2,S}^{\rm G}=
 \frac{\varepsilon a^2}{2}
 \left[(2+\delta)^{-5/2}e^{-b^2/(2(2+\delta))}
       \left(1-\frac{b^2}{2+\delta}\right)-2^{-5/2}\right].}
 \tag{6}
\]

The superscript G marks the Gaussian test. In particular the spectator term survives even at zero site mean. Integrating the derivative of $u^{-5/2}$ gives, for $b=0$,

\[
 \frac{5\varepsilon a^2\delta}{4\,3^{7/2}}
 \leq |\mathcal R_{2,S}^{\rm G}|
 \leq\frac{5\varepsilon a^2\delta}{4\,2^{7/2}}.
 \tag{7}
\]

For $\delta=0$ and $|b|\leq1$, (6) instead equals

\[
 \frac{\varepsilon a^2}{2\,2^{5/2}}
       \{e^{-b^2/4}(1-b^2/2)-1\}.
\]

The expression in braces has absolute value between $b^2/2$ and $3b^2/4$: use $e^{-b^2/4}\leq1$ for the lower bound and $1-e^{-b^2/4}\leq b^2/4$ for the upper bound. For simultaneous $\delta,b$, subtract the value at $b=0$ first; the same estimate with $b^2/(2+\delta)$ gives

\[
 |\mathcal R_{2,S}^{\rm G}|\leq C\varepsilon a^2(\delta+b^2),
 \qquad 0\leq\delta\leq1,\quad |b|\leq1,
 \tag{8}
\]

with an absolute constant (for example $C=1$). This term is linear in the old activity. There is no second activity to multiply into it.

**Implication — its $g,L$, and distance count.** To compare (8) with the frozen norm, take a collinear geometry: anchor at 0, the far link at distance $d$, the site at distance $R\geq d$; then the connecting tree has length $R$. Write $d_R(c)$ for the link's distance from the new rough set, so $d_R(c)\leq d$, and use the uncapped radius $\rho=c'g e^{c_1d_R(c)}$. Suppose, solely for this comparison,

\[
 |a|\leq A L^{-2}g^{-1}e^{-\lambda d},\qquad
 \delta\leq B e^{-\mu R},\qquad
 |b|\leq B\epsilon_0 L^{-2}g^{-1}e^{-\lambda R}.
 \tag{9}
\]

Then (8), without suppressing a power of $g$, gives

\[
 \rho^2e^{c_3R}|\mathcal R_{2,S}^{\rm G}|
 \leq C\varepsilon A^2c'^2L^{-4}
 e^{-2\lambda d+2c_1d_R(c)}
 \left[B e^{-(\mu-c_3)R}
 +B^2\epsilon_0^2L^{-4}g^{-2}e^{-(2\lambda-c_3)R}\right].
 \tag{10}
\]

The covariance term has power $g^0L^{-4}$; the mean term has power $g^{-2}L^{-8}$, each with the displayed distance decay. If $R\geq A_S\log(1/g)$, $\lambda\geq c_1$, $(\mu-c_3)A_S\geq\eta$, and $(2\lambda-c_3)A_S\geq2+\eta$, the bracket is at most $(B+B^2\epsilon_0^2L^{-4})g^\eta$. Here $A_S$ is a comparison parameter, not a redefinition of the draft's locality constant. Thus this explicit term can fit the born-error budget of (42). A capped radius only reduces this calculation. These are implications under (9), not lower bounds or decay estimates established for the actual SU(2) covariance. Consequently (7) does not refute (42) or (43).

**Implication — the whole one-link, one-site norm in the Gaussian test.** This model also permits a direct continuation check. Replace $a$ by $\zeta a$, put $B_\zeta=\rho|\zeta a|$, and denote the ordinary power-series coefficient sum at radius $\rho$ by $\|\cdot\|_\rho$. For $d_*=2+u$, $0\leq u\leq\delta$, and $|v|\leq|b|$, the exponential series gives

\[
 \left\|d_*^{-3/2}
   e^{-(\zeta aw+v)^2/(2d_*)}\right\|_\rho
 \leq d_*^{-3/2}e^{(B_\zeta+|v|)^2/(2d_*)}.
\]

Its derivatives in $u$ and $v$ multiply it respectively by
$-3/(2d_*)+(\zeta aw+v)^2/(2d_*^2)$ and $-(\zeta aw+v)/d_*$. Integrating these derivatives along the real $u,v$ intervals and using the triangle inequality proves, when $B_\zeta,|b|\leq1$,

\[
 \|\Gamma_1-\Gamma_0\|_\rho
 \leq C\varepsilon\{\delta+B_\zeta|b|+b^2\}.
 \tag{10a}
\]

The site-free nonconstant coefficient sum is exactly
$\varepsilon2^{-3/2}(e^{B_\zeta^2/4}-1)\leq C\varepsilon B_\zeta^2$.
In the collinear geometry, the full anchored norm is therefore at most

\[
 C\varepsilon\left[
 1+e^{c_3d}B_\zeta^2+
 e^{c_3R}\{\delta+B_\zeta|b|+b^2\}\right].
 \tag{10b}
\]

There is no uncounted set of coefficients in this one-link, one-site algebra. At a flat base, the frozen floor is $t_{\rm fl}=C_sL^{-2}c'(D_P^+)^2$. Under (9), on $|\zeta|\leq c/t_{\rm fl}$,

\[
 B_\zeta\leq
 \frac{cA}{C_s(D_P^+)^2}e^{-\lambda d+c_1d_R(c)}.
\]

Thus, for example, if $cA/C_s\leq1$, $2(\lambda-c_1)\geq c_3$, and the site parameters satisfy $e^{c_3R}(\delta+|b|)\leq1$, (10b) is at most $C\varepsilon$. These are sufficient conditions for this test's entire continuation norm, not verified bounds on the lattice inverse coordinate. They exhibit why neither a naked $g^{-2}$ nor a naked spectator-variance defect alone kills the proposed estimate. Holding a site at fixed distance while taking $g\to0$ would also eventually violate the draft's far-site threshold $r_2=C\log(1/g)$.

**Discharged — what the actual density coefficient contains.** At fixed real integration coordinates in (43), expand the actual functions as

\[
 \Xi_r(w)=\Xi_{r,0}+w\Xi_{r,1}+w^2\Xi_{r,2}+\cdots,
 \quad \log J_r(w)=\ell_{r,0}+w\ell_{r,1}+w^2\ell_{r,2}+\cdots,
 \quad \Psi_r(w)=\Psi_{r,0}+w\Psi_{r,1}+w^2\Psi_{r,2}+\cdots.
\]

A local logarithm of $J$ suffices for these algebraic coefficients wherever $J_0\ne0$. The fixed cuts have no derivative. Since the Gaussian exponent is $-\Xi\cdot\Xi/2$, its logarithmic coefficients are exactly

\[
 A_{r,1}=\ell_{r,1}+\Psi_{r,1}-\Xi_{r,0}\cdot\Xi_{r,1},\qquad
 A_{r,2}=\ell_{r,2}+\Psi_{r,2}-\Xi_{r,0}\cdot\Xi_{r,2}
                    -\tfrac12\Xi_{r,1}\cdot\Xi_{r,1}.
 \tag{11}
\]

Thus $U=A_1$, $V=A_2+A_1^2/2$. Substitution into (2) yields

\[
 [w^2]\Gamma_r=\langle E_{r,2}\rangle_r+
 \operatorname{Cov}_r(E_{r,1},A_{r,1})+
 \operatorname{Cov}_r(E_{r,0},A_{r,2})+
 \tfrac12\kappa_{3,r}(E_{r,0},A_{r,1},A_{r,1}),
 \tag{12}
\]

where

\[
 \kappa_3(E,A,A)=\langle EA^2\rangle-\langle E\rangle\langle A^2\rangle
 -2\langle EA\rangle\langle A\rangle+2\langle E\rangle\langle A\rangle^2.
\]

This is an expansion of the quotient, not an additional hypothesis on decay. For the local factor (3), the coordinates $v$ hold all its plaquette links fixed, so $E_1=E_2=0$. The actual one-factor term left to estimate is therefore the difference between site states of

\[
 \boxed{K_r(e)=\operatorname{Cov}_r(e,A_{r,2})
       +\tfrac12\kappa_{3,r}(e,A_{r,1},A_{r,1}).}
 \tag{13}
\]

The functions in (11) are those of (43), and the expectation in (13) normalizes their density on the specified cuts. To retain its original denominator as well, define

\[
 \mathscr K_r(e)=\theta_{r,0}K_r(e)
    +\theta_{r,1}\operatorname{Cov}_r(e,A_{r,1})
    +\theta_{r,2}\langle e\rangle_r.
 \tag{13a}
\]

This is the exact coefficient of (43) for the local factor (3). For a pure translated Gaussian, $\Xi=x-s_0-wa-w^2b$, (11) reduces to $A_1=(x-s_0)\cdot a$, $A_2=(x-s_0)\cdot b-|a|^2/2$. With identical numerator and denominator cuts, $\theta=1$, and this recovers (35)–(37), including every denominator subtraction.

**Gap — the specific missing estimate.** With the notation and prescribed marginal form of the question, even for (3) the required remainder bound is

\[
 \boxed{\rho^2e^{c_3\tau(Y';\{c\},S)}
 \left|K_1(e)-K_0(e)-[w^2h]\mathcal M\right|
 \leq Ccc_j\omega_PP_P
       \{t_\#^3+t_\#^2(D_P^+/L)^a\}+\mathcal B_j(P).}
 \tag{14}
\]

For (43) itself a necessary coefficient bound, without marginal subtraction, is

\[
 \boxed{\sup_{|\zeta|\leq c/t_\#}\rho^2
 e^{c_3\tau(Y';\{c\},S)}
 |\mathscr K_{1,\zeta}(e)-\mathscr K_{0,\zeta}(e)|
 \leq Ccc_j\omega_PP_P.}
 \tag{15}
\]

In (14) use $K$ on the original normalized cuts; passage to the new cuts requires its stated error bound. Neither (14) nor (15) is established here for the actual density. The elementary Gaussian computation evaluates the corresponding expressions only after replacing that density by (4). In particular no value, sign, or lower bound for the actual $\Psi$, $J$, $\Xi$, or $\theta$ coefficient has been computed. At general old factors the first two terms of (12) must also be retained; at general multi-indices and site sets the counterparts of (15) must be summed, not merely checked one coefficient at a time.

**Discharged — why the fixed-shift estimate does not supply (15).** The proof of (40) in the preceding report applies to coefficient vectors $y_m$ independent of the Gaussian being integrated. In (43), $\Xi$ is the inverse coordinate evaluated at $(v,\chi)$. Its changes, the Jacobian, and the interacting weight must be controlled together; a form-norm bound on a shift alone does not do this. The distinction can be checked without any lattice input. In three dimensions set

\[
 \Xi_w(x)=(1-\alpha w)x,\qquad J_w=(1-\alpha w)^3.
\]

The normalized density $J_w\phi_3(\Xi_w(x))dx$ has integral one for real $w$ with $1-\alpha w>0$, by substitution. Its shift coefficient is $y_1(x)=-\alpha x$. The expression $x\cdot y_1=-\alpha|x|^2$ has mean $-3\alpha$; it is not a centered Gaussian of variance $|y_1|^2$. The actual log-density coefficients are

\[
 A_1=\alpha(|x|^2-3),\qquad A_2=-\frac{\alpha^2}{2}(|x|^2+3).
 \tag{16}
\]

Here $\langle|x|^2\rangle=3$, $\operatorname{Var}(|x|^2)=6$: in one component integration of $(x\phi)'$ and $(x^3\phi)'$ gives $\langle x^2\rangle=1$, $\langle x^4\rangle=3$, and the components are independent. Boundary terms vanish because a fixed polynomial times $e^{-x^2/2}$ tends to zero. Consequently $\langle A_2+A_1^2/2\rangle=-3\alpha^2+3\alpha^2=0$, as normalization requires. Discarding the Jacobian or treating $y_1(x)$ as a fixed vector would miss this cancellation. This example refutes that substitution in the argument, not (43). It does not assert that the actual inverse coordinate is this dilation, or that another choice of coordinates cannot give a usable majorant.

**Gap — scope of a possible repair.** A coordinate choice that makes the far-variable shift independent of the integrated near Gaussian would repair this particular use of (40); its exact Jacobian, cuts, and normalized interacting weight would still have to yield (15), uniformly in region, depth, and radius. I have not constructed such a choice for the full continuation disc. Recentering at the exact saddle moves the fixed $x$-cuts to $\mathbf1_{|\xi+s(W)|\leq p_2}$; this follows by substituting $x=\xi+s(W)$, and it restores a sharp $W$-dependence. Enlarging the rough set to swallow every far site would remove the tested site coefficient, but sites have no fixed maximum distance in a growing region, so that change would lose the stated radius bound independent of volume. Replacing the coefficient norm by real-state suprema would not imply (15): even the polynomial $T_n$ defined by $T_0=1,T_1=x,T_{n+1}=2xT_n-T_{n-1}$ obeys $|T_n(x)|\leq1$ on $[-1,1]$, since the cosine addition identity gives $T_n(\cos\theta)=\cos(n\theta)$, whereas its leading coefficient is $2^{n-1}$ for $n\geq1$ by induction in the same recurrence. Thus its coefficient sum at radius one is unbounded. None of these changes has been made, and none is an established repair of (43).

**Discharged — the source in the same coefficient.** Write the first source insertion as $I(w)=I_0+wI_1+w^2I_2+\cdots$; the chart and cuts are source independent by I:1170–1175. Differentiating a normalized integral gives

\[
 D_f\langle E\rangle=\langle\dot E\rangle+
             \operatorname{Cov}(E,I).
 \tag{17}
\]

This follows by differentiating its numerator and denominator. To track further products without suppressing normalization, define

\[
 \kappa_n(X_1,\ldots,X_n)
 =[t_1\cdots t_n]\log\langle\exp(\textstyle\sum_i t_iX_i)\rangle.
\]

This is a formal coefficient definition; at finite cuts all the moments being used are finite. For fixed $X_i$, differentiating with respect to a density perturbation $e^{fI_0}$ adds one argument $I_0$ to $\kappa_n$: expand
$\log\langle e^{fI_0+\sum t_iX_i}\rangle-\log\langle e^{fI_0}\rangle$
and take the coefficient of $f t_1\cdots t_n$. When an $X_i$ depends on $f$, the ordinary product rule supplies its derivative too. This proves the identity used next, rather than importing a cumulant lemma.

**Discharged — source counterpart of (13).** For the source-independent local factor (3), differentiating (13), using $\dot A_1=I_1$, $\dot A_2=I_2$, gives exactly

\[
 \boxed{\dot K_r(e)=
 \operatorname{Cov}_r(e,I_{r,2})
 +\kappa_{3,r}(e,A_{r,1},I_{r,1})
 +\kappa_{3,r}(e,A_{r,2},I_{r,0})
 +\tfrac12\kappa_{4,r}(e,A_{r,1},A_{r,1},I_{r,0}).}
 \tag{18}
\]

If the old local factor has a source derivative $\dot e$, add $K_r(\dot e)$. For a general old factor with far coefficients $E_1,E_2$, additionally differentiate the first two terms of (12); they give

\[
 \langle\dot E_2\rangle+\operatorname{Cov}(E_2,I_0)
 +\operatorname{Cov}(\dot E_1,A_1)+\operatorname{Cov}(E_1,I_1)
 +\kappa_3(E_1,A_1,I_0).
 \tag{19}
\]

The $\dot E_0$ contribution is the $K(\dot E_0)$ just described. For the exact denominator of (43), differentiate all three products in (13a) as well:

\[
 \dot{\mathscr K}
 =\dot\theta_0K+\theta_0\dot K
 +\dot\theta_1\operatorname{Cov}(e,A_1)
 +\theta_1\{\operatorname{Cov}(\dot e,A_1)
             +\operatorname{Cov}(e,I_1)+\kappa_3(e,A_1,I_0)\}
 +\dot\theta_2\langle e\rangle
 +\theta_2\{\langle\dot e\rangle+\operatorname{Cov}(e,I_0)\}.
 \tag{20}
\]

Take the site difference after these operations, and subtract $[w^2h]\dot{\mathcal M}$ for the remainder. In particular the last term of (18) is the normalized counterpart of the insertion multiplying the squared first-density score in (46). It is a fourth connected moment with one old factor, not a product of two old activities.

**Discharged — hand source check in the Gaussian test.** Set $\delta=0$ in (4) and insert the particular quadratic source $I=g^2|\xi|^2/2$, with $e$ source independent. This is a test insertion, not an identification of the full lattice source. Its normalized tilted Gaussian has variance $\sigma_f^2=(1-fg^2)^{-1}$ and unchanged mean $m=aw+rb$: complete the square in the density and divide by its integral. Consequently (5) holds with $d=1+\sigma_f^2$. Differentiating at $f=0$ yields

\[
 \dot\Gamma_r(w)=\varepsilon g^2\,2^{-3/2}
 e^{-m^2/4}\left(\frac34-\frac{m^2}{8}\right).
\]

Its quadratic marginal coefficient is $-5\varepsilon g^2\,2^{-3/2}/16$ times $m^2$; again its $w^2h$ coefficient vanishes. Two derivatives with respect to $m$, divided by two, therefore give

\[
 \dot{\mathcal R}_{2,S}^{\rm G}
 =\varepsilon g^2\,2^{-3/2}a^2
 \left[e^{-b^2/4}
       \left(-\frac5{16}+\frac{b^2}{4}-\frac{b^4}{64}\right)
       +\frac5{16}\right].
 \tag{21}
\]

For $|b|\leq1$, the bracket has absolute value at most $11b^2/32$: bound its three terms by $5b^2/64$, $b^2/4$, and $b^4/64$, using $1-e^{-b^2/4}\leq b^2/4$. Thus this source example has the mean term's size in (10) with an additional $g^2$. The product $\langle e\rangle\langle I\rangle$ is subtracted through the denominator in (17); leaving that denominator undifferentiated would give a different expression. Neither (21) nor its bound establishes the lattice-source estimate (18).

**Discharged — both successive levels.** Let $j=0,1$ denote the two successive RG levels, with one labelled branch fixed at each level; sum the resulting formulas over branches when required. Keep separate the near-factor normalizations $N_j^Z$ and the good normalizations $N_j$. Define

\[
 T_jH=E_j^Z[H],\qquad r_j=N_j^Z/N_j,\qquad
 U_jH=r_jT_jH,\qquad
 \Delta_j=E_j^Z[I_j]-E_j^{\rm good}[I_j].
\]

By differentiating each quotient,

\[
 D_f(U_jH)=U_j(D_fH)+V_j(H),\qquad
 V_j(H):=r_j\operatorname{Cov}_j^Z(H,I_j)
                +r_j\Delta_jT_jH.
 \tag{22}
\]

These equalities assume the displayed denominators are nonzero; they make no assertion that the needed complex norm bounds have been proved. Applying (22) twice gives the unextracted two-level coefficient's insertion:

\[
 D_f(U_1U_0e)=U_1U_0\dot e+U_1V_0(e)+V_1(U_0e).
 \tag{23}
\]

This follows simply by substituting $H=U_0e$ into the first formula and then differentiating $U_0e$. Each $V_j$ includes its own normalization difference; no normalization from one level serves the other. To retain extraction, put $H_0=U_0e-v_0-\mathcal M_0$, where $v_0$ is the vacuum subtraction actually prescribed at level 0. Then

\[
 D_f(U_1H_0-v_1-\mathcal M_1)
 =U_1\{U_0\dot e+V_0(e)-\dot v_0-\dot{\mathcal M}_0\}
   +V_1(H_0)-\dot v_1-\dot{\mathcal M}_1.
 \tag{24}
\]

Thus (18)–(20), with level 0's density, occur inside the first term of (24); with level 1's density they occur in its second term, now with the full first output as old factor and with (19) when it has tails. The marginal derivatives are explicit. This supplies the algebra of (44)–(46) at both levels, without asserting the estimates at either.

**Gap — source estimate remaining at each level.** The counterpart of (15) is the same weighted bound with $\mathscr K_{r,\zeta}$ replaced by $\dot{\mathscr K}_{r,\zeta}$ of (20), with the allowed source-direction factor. In particular it needs the site difference of $\kappa_4(e,A_1,A_1,I_0)$ in (18), together with its other connected terms and the normalization-ratio derivatives. A scalar Gaussian moment estimate does not bound this sum in the actual coefficient algebra. No uniform bound for it is established here, at level 0 or at level 1.

**Discharged — scope and final status.** Read the two required rule files and library/tail-two-step.md in full, and the located passages of parts/hard-core--independent.md on (TAIL), the chart, (BANACH), its Gaussian weights, and its source. Text searches also exposed other passages in that permitted main file. No other proof account, git history, outside-directory file, numerical output as evidence, or external source was used. The Gaussian and source formulas above are hand derivations. The exact SU(2) connected coefficients have been identified but not evaluated or bounded. Only this report was changed.

**Gap — verdict: undecided at (43), specifically (15) with the actual coefficient (13a) and density scores (11).** The explicit surviving Gaussian term is the spectator-variance term (7), of weighted size $cc_j\omega_P c'^2L^{-4}$ times its distance decay; it is not a counterexample because that decay can fit the born error. No proof of (43), no actual SU(2) violating coefficient, and no general source estimate at either level has been established.
