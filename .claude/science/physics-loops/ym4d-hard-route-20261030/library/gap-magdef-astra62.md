## Repo search

Row 1646, checkout `8a6b28dbd`. Author-side research. The designated prior note was absent at this pin.

**ON FILE (five-ref search).** I searched origin/main (8b11ae2bb95e), pr/10114 (f76f6c649cff), pr/10133 (89faef229ff6), pr/10134 (1e70c7211a2c) and pr/10141 (c73ad7b177d9) for magnetic action deficit or excess, plaquette excess, action sum rule, Michael near 1987, VIR-down, and Feynman–Hellmann near plaquette or Wilson transfer.

| Relevant files hit | Exact result and relation to this row |
|---|---|
| Main, research/mass-gap/ROWS.md, library/gap-skeleton-final.md and library/gap-vir-sc.md §8 | Row 710 §8 quotes its theorem $-\beta m_i'=\Delta N-\beta\Delta R-\beta\Delta V_1$ for $0<\beta<4$. Each excess is taken over the vacuum. Its volume-dependent small-coupling estimate leaves the signed magnetic difference on the band open. |
| Main, research/mass-gap/library/prior/gap-vir-lit.md and gap-fullread-1.md | Rothe's static-pair coupling derivative sums both plaquette orientations. Row 1645 subsequently located Michael's isolated-glueball identity. Neither supplies a magnetic lower bound. The target search returned no line from the four PR refs. |
| PRs 10114 and 10133, SRCCD55.md Lemma V, CODEX_REVIEW_OSLEAF.md lines 63–69 and CODEX_REVIEW_SRCCD.md §3 | A search for six staples and conditional one-link variance led to the reviewed estimate $\operatorname{Var}O_a(f)\ge c_N g_{\rm FLOW}^4a^{-4}(\lVert f\rVert_2^2-O_f(a))$ for a real smeared clover on an even torus at weak bare coupling. The proof conditions on independent links. Grok's PR 10133, MASS_GAP_CW_CROSSOVER_ATTACK.md Lemma 2.2, gives the six-staple conditional law. |
| PR 10134, parts/upper-chain.md Theorem 3 and Corollary 3.2, checks/upper-chain_criteria.md line 78 | For large $\beta$ and $\log\beta\le L/a$, Theorem 3 gives $\operatorname{Var}W\ge(u_1/4)\lvert\Lambda\rvert/\beta^2$ for the total spacetime action. Corollary 3.2 excludes a cutoff-uniform unsubtracted bulk source bound. The criteria file defines a coarse-clover covariance test. Section 2 below uses the first proof's contact term with a spatial-only source and the infinite-time vacuum. |

The four files cited for PRs 10114 and 10133 are under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` on their respective refs. The two PR 10134 paths are relative to this lane. PR 10141 supplied no corresponding method hit.

**ON FILE (local scope).** The registry places this reopen condition in VIR-DOWN. LEV-FAIL concerns all ordered levels. Row 1641 records the stop in FINISH. It has no separate file, and no numbered row or file for 1643 is present at this pin. Rows 1642 and 1644 concern a flowed winding measurement at the hot endpoint. The November 8 digest (row 531) covers earlier ultraviolet constructions. The Sussman–Alpoge index (row 244, chunks 02 and 29, obligations lines 24 and 1498) points to outline lines 2197–2214, 2315–2335, 2475–2498 and 31871–31882. GL3, GL8 and GL14 give the one-link multipliers, the positive transfer trace and the exact two-neighbour conditional layer density. CA-I lines 2704–2713 exclude the gap from Theorem 0. CA-I §4.18, from line 56123, concerns the large-field induction. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex, for the outline and account at the supplied revision 31a47c543775.

**ON FILE (related methods).** Row 1236 (17), using row 1151 (21)–(22b), concentrates scaled spatial actions by a magnetic tilt on a transfer spectral band. Row 1619 §3.3 gives a squared-force identity. Row 773 §4.3 treats optimal scalar coupling for a different plaquette comparison. Further five-ref searches for magnetic secants or susceptibility floors, cold-state magnetic anti-concentration, compensated two-step insertions and magnetic or excited-state quantile pairing located no matching theorem. The estimates below concern the signed response in genuine low-energy states.

## 1. A magnetic source on the actual growing torus

**ON FILE (rows 710 §8, 1639–1641, 1645).** For $V=\sum_{p\ {\rm spatial}}(1-\tfrac12{\rm tr}\,U_p)$ the favourable magnetic sign is **vacuum action minus excited-state action**, equivalently excited plaquette trace minus vacuum plaquette trace. Check 1640 §1 identifies the operator on an eigenspace as $F_r(\langle V\rangle_0-V)F_r$. Michael's sum rule fixes the sum of the electric and magnetic insertions. The sign of the magnetic part remains open. Check 1639 §1.2 also allows a large electric excess.

ON FILE (checks 1613, 1630, 1639, 1640). Fix the temporal coupling $B$ and write $T_s=e^{-sV/2}C_Be^{-sV/2}$ on the neutral physical space. Set $N=n^3$, $a(s)=\log\lambda_0(T_s)$ and $p_t(s)=t^{-1}\log\operatorname{Tr}_+T_s^t$. Write $D_t(s)=p_t'(s)-a'(s)=\langle V\rangle_0-\langle V\rangle_t$ for the vacuum action minus the thermal action, and $D_t$ at the isotropic point $s=B$. Multiplying $D_t$ by $1+G$ cancels the vacuum term and gives the unnormalized excited sum. Time is held fixed in both derivatives. Use the temporal Wilson weight $e^{-B(1-\operatorname{tr}U/2)}$. Any scalar normalization depending on $B$ alone cancels from the level ratios and spatial derivatives. On these fixed late windows $B\asymp\log n$ is the bare coupling (checks 1453, 1630). Here $r_i=\lambda_i/\lambda_0$, $m_i=-\log r_i$, $G=\sum_{i>0}r_i^t$ and $W_t=\sum_{i>0}m_i r_i^t$.

**PROVED below (partial result).** At every cold point a separate finite-difference estimate of the two pressures loses the sign for $h\gg(1+B)/n^2$. An exact integration removes one source of magnetic fluctuations before the two states are compared. The remaining finite-width test can fail even when the magnetic rate holds in a positive transfer family. Its sign for the Wilson fields is open.


## 2. The vacuum curvature discarded by a pressure comparison

**PROVED (uniform magnetic susceptibility).** There are absolute $c>0$ and $B_*<\infty$ such that, for every even $n\ge4$, $B\ge B_*$ and $B/2\le s\le2B$, the function
\[
 a(s)-\tfrac12\gamma s^2\quad\text{is convex},\qquad
 \gamma=\frac{c\,n^3}{(1+B)^2}.                                      \tag{1}
\]
The curvature is in the **spatial** coupling, with the temporal coupling fixed. This is an extensive contribution on the actual isotropic boxes, including sides $n=\ell b^K$.

*Proof.* Take an untwisted ordinary Wilson torus $n^3\times M$, $M\ge4$ even. Write $S$ and $E$ for its sums of spatial and temporal plaquette actions, with normalized Haar measures. Each kind has $3NM$ plaquettes. Put $F(x)=\log\int\exp[-x(sS+BE)]$. Restrict every link to a ball of radius $B^{-1/2}$ about the identity. Each ball has Haar mass at least $c_1B^{-3/2}$ by its radial density $\sin^2\theta$, and every plaquette has action at most $8/B$ by the triangle inequality. There are $4NM$ links. Hence $F(1)\ge-CNM(1+\log B)$. Convexity and $F(0)=0$ give $-\mathbb E(sS+BE)=F'(1)\ge F(1)$. Translation and spatial rotation invariance now yield
\[
 \mathbb E(1-\tfrac12\operatorname{tr} U_p)
 \le C'(1+\log B)/B                                                   \tag{2}
\]
for each spatial plaquette. The same bound holds for a temporal plaquette using the $BE$ term. The constants are uniform in the periods and in $s$ in the displayed interval.

ON FILE (rows 1173 (8), 1178 (15), 1298, 1315 and 1341). Use the conditional one-link variance bound from the mixed-twist work and the two-neighbour-slice conditional Wilson law from the resampling work. The former was applied to a ribbon with a *unit* marked staple. Here the source on a link is the **sum of four** magnetic staples, which can vanish. Equation (2) supplies the additional estimate.

PROVED (continued). Select positive direction-1 links whose base has $x_2+x_3+x_4$ even, with $x_4$ the time coordinate. No plaquette meets two selected links. Given the complement, the selected unit quaternions $X_e$ are independent, with densities proportional to $\exp(q_e\cdot X_e)$ on $S^3$. Write $H_e$ for the sum of the four oriented spatial staples and $U_e$ for the sum of the two temporal staples, so $q_e=sH_e+BU_e$ and $|q_e|\le10B$. In $S$ each selected link enters as $-H_e\cdot X_e$ plus a term independent of the selected links. Pointwise, $4-X_e\cdot H_e$ is the sum of the four incident spatial plaquette actions. Thus $\Pr(|H_e|<3)\le4C'(1+\log B)/B$, which is at most $1/2$ for a fixed sufficiently large $B_*$. This statement is about the Wilson law of the surroundings.

For clarity, the one-link estimate used here is $\operatorname{Var}_q(v\cdot X)\ge c_2|v|^2/(1+|q|)^2$. At $|q|\le4$, the density is bounded below by $e^{-8}$ times Haar, so use the infimum over constants in the variance. At $k=|q|\ge4$, let $z=X\cdot q/k$. The variable $y=k(1-z)$ has density proportional to $e^{-y}y^{1/2}(2-y/k)^{1/2}$ on $[0,2k]$. Its masses on $[1/4,1/2]$ and $[2,3]$ are bounded below uniformly, since its normalizer is at most $\sqrt2\int_0^\infty e^{-y}\sqrt y\,dy$. Two independent draws give $\operatorname{Var}(z)\ge c_3/k^2$. Each transverse variance is $\mathbb E(1-z^2)/3\ge c_4/k$ by the first interval. Symmetry makes the covariance diagonal in these directions.

Consequently
\[
 \partial_s^2\big(M^{-1}\log Z_M\big)
  = M^{-1}\operatorname{Var}(S)
  \ge M^{-1}\sum_{e\ {\rm selected}}\mathbb E\operatorname{Var}_{q_e}(H_e\cdot X_e)
  \ge \gamma .
\]
There are $NM/2$ selected links. At fixed $n,B,s$, $M^{-1}\log Z_M\to a(s)$. Indeed the ordinary gauge-projected positive trace-class transfer has a simple positive top eigenvector, which is centre invariant by uniqueness. Its top eigenvalue is therefore also the neutral one. For eigenvalues $\lambda_i$, the trace lies between $\lambda_0^M$ and $\lambda_0^{M-1}\sum_i\lambda_i$. Subtract $\gamma s^2/2$ before passing to the limit in the convexity inequality. This proves (1) without interchanging derivatives and limits.

**PROVED (obstruction to separate pressure secants).** For every real $t\ge1$ and $s,s\pm h$ in the interval of (1), put
\[
 L_h=\frac{p_t(s)-p_t(s-h)}{h}-\frac{a(s+h)-a(s)}{h},\qquad h>0 .
\]
Then
\[
 L_h\ \le\ D_t,\qquad
 L_h\ \le\ \frac{\log(1+G(t;s))}{th}-\gamma h.                       \tag{3}
\]
In particular at **every** cold point $G\le c_{\rm col}$,
\[
 h^2>\frac{(1+B)^2\log(1+c_{\rm col})}{c\,n^3t}
 \quad\Longrightarrow\quad L_h<0 .
\]
At $s=B$ and $t\ge n/512$, any fixed admissible absolute step $h>0$ eventually fails to certify even a positive deficit, whenever a cold point is present. More generally the failure holds if $h n^2/(1+B)\to\infty$. This excludes this specific way of bounding the two derivatives separately.

*Proof.* $p_t$ is convex for real $t\ge1$. A direct tangent check avoids an assumption about fractional-time Wilson path measures. Let $\psi_i$ be an eigenbasis at $s$, $v_i=\langle\psi_i,V\psi_i\rangle$. The positive spectra of $T_{s+d}$ and $T_s^{1/2}e^{-dV}T_s^{1/2}$ agree by the two placements of $D^*D$ and $DD^*$. For a positive operator $K$, $\operatorname{Tr}K^t\ge\sum_i\langle\psi_i,K\psi_i\rangle^t$ by scalar Jensen on each spectral measure. Apply it here, then Jensen first in each state and then in the weights $\lambda_i^t/\sum_j\lambda_j^t$. This gives $p_t(s+d)\ge p_t(s)-d\langle V\rangle_t$, a supporting affine function at every $s$. Its slope is continuous. Indeed $T_{s+d}\to T_s$ in trace norm by bounded multiplication. In $T_s^t=T_s^{(t-1)/2}T_s T_s^{(t-1)/2}$ the outer factors are norm-continuous by the continuous functional calculus (the identity at $t=1$), so $T_s^t$ is trace-norm continuous. This proves continuity of the normalized expectation of bounded $V$. Using the supporting inequality at both $s$ and $s+d$ now gives $p_t'=-\langle V\rangle_t$. Convexity and the simple vacuum eigenvalue derivative $a'=-\langle V\rangle_0$ give the first inequality in (3). For the second, $p_t(s)-a(s)=t^{-1}\log(1+G(t;s))\ge0$. Substitute this difference at $s$ and at $s-h$ in $hL_h$, drop the subtracted nonnegative difference at $s-h$, and use the centred second difference of (1), at least $\gamma h^2$. This also checks the sign in (3).


## 3. An action fluctuation inside each cold level

**PROVED (interval estimate).** Let $X_-,X_0,X_+$ be three successive vacuum slices in temporal gauge. Expose $X_-,X_+$ and all of $X_0$ except the positive direction-1 links with $x_2+x_3$ even. Denote this information by $\mathcal F$. Write $\Omega$ for the positive normalized vacuum wavefunction. Let $\psi$ be **any** normalized neutral eigenvector, including any vector in a degenerate visible eigenspace, with multiplier $r=e^{-m}$ relative to the vacuum. Give the three-slice vacuum law the density $|f(X_0)|^2$, where $f=\psi/\Omega$, and call the resulting probability $\mathbb P_\psi$. Its middle marginal is exactly $|\psi|^2\,d{\rm Haar}$. For any real $\mathcal F$-measurable $z$ and any $w\ge0$,
\[
 \mathbb P_\psi\{|V(X_0)-z|\le w\}
 \le C\left(\frac{1+\log B}{B}+\frac{m}{BN}
             +\frac{(1+w)(1+B)}{\sqrt N}\right)
             +\sqrt{1-e^{-2m}} .                                      \tag{4}
\]
The constants and coupling range are those of §2, with enlargement of $C$ if necessary. For any $A<\infty$, at $t\ge n/512$, this probability tends to zero **uniformly** over $tm\le A$, exterior-dependent centres and $w=o(n^{3/2}/(1+B))$ along the calibrated late windows. In fact $m=o(1)$ suffices. This tests fluctuations in the bulk of the low-level field distribution.

*Proof.* Use the Wilson convolution with kernel $e^{-B(1-w)}$ per temporal plaquette. Then $\|C_B\|\le1$. The ball estimate in §2 and the time limit give $-a(s)\le CN(1+\log B)$. In operator order $T_s\ge\lambda|\psi\rangle\langle\psi|$, $\lambda=\lambda_0e^{-m}$. Conjugation by $e^{sV/4}$ gives
\[
 \lambda \langle\psi,e^{sV/2}\psi\rangle
 \le \|T_{s/2}\|\le1,\qquad
 \mathbb E_{\psi}V(X_0)\le \frac{2}{s}\{CN(1+\log B)+m\}.              \tag{5}
\]
This step uses the magnetic tilt and rank-one argument of gap-solve27-astra62.md (17). It holds for vectors without any spatial symmetry beyond the physical projections. There are $N/2$ selected central links. Every spatial plaquette meets at most one of them, so $\sum_{e\ {\rm selected}}(4-X_e\cdot H_e)\le V(X_0)$. Each $|H_e|<3$ contributes more than one to this sum. By (5), the $\mathbb P_\psi$-probability that fewer than $N/4$ have $|H_e|\ge3$ is at most $C[(1+\log B)/B+m/(BN)]$.

Keep the same vacuum path reference and weight it instead by $|f(X_-)|^2$. This is a probability $\mathbb Q_\psi$ and its density is $\mathcal F$-measurable. In the unprojected temporal-gauge representation the transition kernel is $T_s(x,y)\Omega(y)/[\lambda_0\Omega(x)]$. The positive unprojected kernel has the same vacuum, since uniqueness makes its positive top eigenvector invariant under gauge and centre transformations. Its restriction in vacuum variables to neutral physical functions is the specified normalized transfer. In particular $\mathbb E[\overline{f(X_-)}f(X_0)]=r$. The affinity of the two weighted probabilities is $\mathbb E|f(X_-)f(X_0)|\ge r$. Factoring the difference of their square roots in the total variation integral and using Cauchy–Schwarz gives $\|\mathbb P_\psi-\mathbb Q_\psi\|_{\rm TV}\le\sqrt{1-r^2}$. This is where the small energy of the **actual state** enters.

Under $\mathbb Q_\psi$, conditional on $\mathcal F$, the selected links have exactly the independent Wilson laws of §2. The two temporal-gauge neighbours give the two temporal staples. Write $Y_e=-H_e\cdot X_e$. Then $|Y_e|\le4$ and $V(X_0)$ is their sum plus an exposed constant. On the good exterior event above the total conditional variance $\sigma^2$ of this sum is at least $cN/(1+B)^2$.

Here is a direct concentration-function estimate. With $Y_e'$ a conditionally independent copy, $|\mathbb E e^{iuY_e}|^2=\mathbb E\cos(u(Y_e-Y_e'))\le1-c'u^2\operatorname{Var}Y_e$ for $|u|\le1/8$, using $1-\cos v\ge v^2/4$ for $|v|\le1$. Independence bounds the modulus of the characteristic function of the sum by $e^{-c''u^2\sigma^2}$ there. Take $d=\max(8,w)$. The nonnegative function
\[
 k(y)=\int_{-1}^1(1-|v|)e^{ivy}\,dv
      =\left(\frac{\sin(y/2)}{y/2}\right)^2
\]
is bounded below by a positive constant on $[-1,1]$. Integrate $k((V-z)/d)$ under the conditional law. Its expectation is at most $C\int_{-1}^1e^{-c''v^2\sigma^2/d^2}\,dv\le C'd/\sigma$, uniformly in the exposed centre. Apply this on the good event under $\mathbb Q_\psi$, pay total variation once there, and bound the bad event directly under $\mathbb P_\psi$ by (5). This proves (4).

**PROVED (visible thermal mixture).** For a fixed box take any nonzero $J=\bigoplus_{r<1}J_r$ with $J_r\le F_r$ an orthogonal projector, transported to Haar space. In particular take the delay-visible $J_r$ of row 1628. Put $G_J=\sum r^t\operatorname{rank}J_r$ and $\bar m_J=G_J^{-1}\sum m r^t\operatorname{rank}J_r$. For the mixture of the preceding central laws with weights $r^t/G_J$ per basis vector in $J_r$, (4) holds with $m$ replaced in its linear term by $\bar m_J$ and its last term by $\sqrt{2\bar m_J}$. Average the bound and use $\sqrt{1-e^{-2m}}\le\sqrt{2m}$ and Jensen. Equivalently one may restrict $J$ to $tm\le A$ before averaging. The mixture is basis independent. No claim that $G\le c_{\rm col}$ by itself puts all the thermal energy in this range is needed.

**PROVED (check on scale and sign).** Fix a sufficiently small absolute $\delta>0$ and set $w_0=\delta\sqrt N/(1+B)$. For all sufficiently late boxes with $tm\le A$ the right side of (4) is at most $1/2$ at $w_0$, uniformly in the state. With $v_\psi=\langle V\rangle_\psi$, it follows that
\[
 \operatorname{Var}_\psi V\ge w_0^2/2,\qquad
 \mathbb E_\psi[(\pm(V-v_\psi))_+]\ge w_0/4 .                         \tag{6}
\]
For the second inequality the two positive-part means coincide since the variable is centred and sum to its mean absolute deviation. Both estimates also hold for the vacuum. Even a uniform order-$m$ difference of means is compatible with (6). For independent state and vacuum samples, the probability of a difference of order $m$ tends to zero. Condition on the independent vacuum sample and apply (4) at its action as a deterministic centre. This last statement concerns independent sampling or exterior-only prediction, and imposes no restriction on a coupling that pairs the microscopic fluctuations.


## 4. A lower bound with the local fluctuation subtracted

**PROVED (a positive correction for a fixed visible subspace).** Fix $s=B$, $t\ge1$, and freeze $J$ as in §3 at this coupling. Write $v_0=\langle V\rangle_0$, $v_J=\operatorname{Tr}(J T_s^t V)/\operatorname{Tr}(J T_s^t)$, $D_J=v_0-v_J$. The required visible magnetic numerator is $G_JD_J$. For $0<h\le B/2$ define the finite change
\[
 q_J(h)=\frac1t\log
 \frac{\operatorname{Tr}_{J}\!\left[(J T_s^{1/2}e^{hV}T_s^{1/2}J)^t\right]}
      {\operatorname{Tr}_{J}\!\left[(J T_s J)^t\right]} .
\]
All traces here are on $\operatorname{ran}J$. Let $\Phi(q)=\log\int_{S^3}e^{q\cdot x}\,dx$ with Haar probability. On one central slice use the selected links of §3 and the unperturbed three-slice vacuum. Put
\[
 R_h=\mathbb E_0\sum_e
 \big[\Phi(q_e+hH_e)-\Phi(q_e)-h H_e\cdot\nabla\Phi(q_e)\big].
\]
Then
\[
 D_J\ \ge\
 \frac{a(s)-a(s+h)-q_J(h)+R_h}{h},\qquad
 R_h\ge c_5 N h^2/(1+B)^2 .                                           \tag{7}
\]
All terms on the right have definitions without the sought magnetic difference. For $J$ restricted to $tm\le A$ and all sufficiently late boxes (fixed $A$), the numerator on the right of (7) can further be **increased** by
\[
                  \log(1+h^2w_0^2/32).                                \tag{8}
\]
Thus part of a one-sided bound on the true signed insertion is available even for selectively observed, degenerate levels. Its two positive corrections measure fluctuations at the base coupling. A remaining difference of finite-source measurements still needs a sign.

*Proof.* The vacuum Rayleigh test on $T_s^{1/2}e^{-hV}T_s^{1/2}$ gives $a(s+h)-a(s)\ge\log\mathbb E_0e^{-hV}$. On the middle slice, condition on $\mathcal F$. The part of $V$ depending on the selected links is $-\sum_e H_e\cdot X_e$. Independence shows exactly
\[
 \log\mathbb E_0[e^{-hV}\mid\mathcal F]
    =-h\,\mathbb E_0[V\mid\mathcal F]+R_h(\mathcal F),                \tag{9}
\]
where $R_h(\mathcal F)$ is the random sum inside $R_h$. Jensen for the outer logarithm gives $a(s+h)-a(s)\ge -h v_0+R_h$. The conditional log normalizer's Hessian is $\operatorname{Cov}_q X$. Each summand of $R_h$ is its quadratic form on $H_e$, integrated from $0$ to $h$ with weight $h-u$ at $q_e+uH_e$. The norm of this parameter is at most $10B$. The variance bound, the vacuum version of (2) (time limit on the fixed lattice), and $N/2$ selected links give the second assertion in (7).

Choose an orthonormal eigenbasis within $J$. Jensen on the diagonal elements of the positive compressed operator, as in (3), gives
\[
 q_J(h)\ge h v_J+
 \sum_{\psi\in J}\frac{r_\psi^t}{G_J}
       \log\mathbb E_\psi e^{h(V-v_\psi)} .
\]
Here the sum is over the chosen basis, with $\mathbb E_\psi$ the middle marginal. Jensen gives this formula also at $t=1$. Every summand in the correction is nonnegative. In the stated low-energy range, $e^x\ge1+x+(x_+)^2/2$ and (6) give $\mathbb E_\psi e^{h(V-v_\psi)}\ge1+h^2w_0^2/32$. This proves (7) and (8), without differentiating a moving visibility projector.

**PROVED (removal in the transfer insertion itself).** Equation (9) also gives a source with exactly its conditional fluctuation removed. Multiply the usual middle-slice insertion $e^{-hV}$ by $e^{-R_h(\mathcal F)}$. Its conditional integral is exactly $e^{-h\bar V}$, where $\bar V=\mathbb E_0[V\mid\mathcal F]$. The correcting factor has zero first derivative at $h=0$ and is positive. This replacement works between arbitrary fixed end slices: conditional on the ends and the exposed middle links, the factors outside the middle slice cancel from the conditional law. In particular, in the integral kernel of $T_s V T_s$ one may replace $V$ by $\bar V$. Contracting the end variables with any unit eigenvector gives $\lambda_\psi^2 v_\psi$ in both cases. Signed or complex eigenvector weights at the ends cause no change in this equality. Thus the local part of the magnetic perturbation can be eliminated **before** taking the state–vacuum difference. The resulting $\bar V$ is measurable in the surroundings. Giving those surroundings the same law in the vacuum and in a cold level would discard the very term being sought.

**PROVED (limit of the correction).** Even granting the exact vacuum tangent, the backward full thermal secant has the bound
\[
 \frac{p_t(s)-p_t(s-h)}h-a'(s)
 \le \frac{\log(1+G(t;s))}{th}-\frac{\gamma h}{2}.                    \tag{10}
\]
Use $p_t-a\ge0$ at $s-h$ and the supporting quadratic of (1) there based at $s$. This checks that granting the exact vacuum tangent alone leaves the same obstruction as (3). Equation (9) removes an explicit conditional fluctuation at a middle slice. The residual lower bound in (7) remains open.


## 5. Pairing two positive exterior laws

**PROVED (a finite-source lower test after the subtraction).** There is a way to keep the vacuum and excited-state fluctuations together which avoids the separate secants in (3). Use the same exposed links $\mathcal F$ as in (4). Their vacuum law is $\mu$. The real exposed observable $\bar V$ is the untouched spatial action plus $\sum_e(4-H_e\cdot\nabla\Phi(q_e))$. For each unit eigenvector, with $f_\pm=f(X_\pm)$, give the exposed variables two probability laws:
\[
 d\mu_{+,\psi}=\left(r^2+\tfrac12|f_--f_+|^2\right)d\mu,\qquad
 d\mu_{-,\psi}=\tfrac12(|f_-|^2+|f_+|^2)\,d\mu .
\]
Both densities are nonnegative. Their integrals equal one since $\mathbb E_\mu\overline f_- f_+=r^2$. Their difference has density $r^2-\operatorname{Re}(\overline f_- f_+)$. Conditional on $X_0$, the two neighbours are independent in the reversible vacuum chain, and each conditional mean of $f_\pm$ is $rf(X_0)$. Conditional instead on $\mathcal F$, the central action has mean $\bar V$. Hence
\[
    \mathbb E_{\mu_{+,\psi}}\bar V-\mathbb E_{\mu_{-,\psi}}\bar V
           =r^2(v_0-v_\psi).
\]
This normalization can also be checked by inserting $T_sVT_s$ from (9).

For $t\ge3$ mix each family of measures with weights $r^{t-2}/G_{J,t-2}$ per visible basis vector, where $G_{J,t-2}=\sum_{r<1}r^{t-2}\operatorname{rank}J_r>0$. The resulting laws are independent of the basis, by the sums of squared moduli on each subspace. Write $Q_+,Q_-$ for the scalar quantile functions of $\bar V$ under the two mixtures. Then for each fixed $h>0$
\[
 G_J D_J\ \ge\
 -\frac{G_{J,t-2}}{h}\log\int_0^1
                \exp[-h(Q_+(u)-Q_-(u))]\,du .                         \tag{11}
\]
There is no separate bulk variance in this inequality. In particular, if the two exterior-score laws are translates, (11) is exact regardless of the variance within each law.

*Proof and cost.* The preceding mean identity gives $G_JD_J=G_{J,t-2}\int_0^1 (Q_+-Q_-)\,du$ (here $G_J=G_{J,t}$). Jensen proves (11). The common quantile minimizes $\mathbb E e^{-h(X-Y)}$ over all couplings of these two score laws: in the double layer-cake integral for $e^{-hX}e^{hY}$ each intersection probability is at least the positive part of the sum of its two marginal probabilities minus one. Under the common uniform parameter the threshold events are opposite end intervals, so that lower bound is attained. This remains true at atoms. With $\Delta=Q_+-Q_-$ and $d=\Delta-\int_0^1\Delta$, the loss per $G_{J,t-2}$ in (11) lies between zero and $h e^{h\|d\|_\infty}\int_0^1 d^2/2$. This follows from $e^x\le 1+x+x^2e^{|x|}/2$ and $\log(1+x)\le x$ for $x\ge0$. This cost uses the unmatched part of the two exterior-score distributions. The coupling uses only the scalar marginals. ON FILE (row 773 §4.3) is an optimal scalar pairing for a squared-difference cost on one plaquette.

### 5.1 A transfer family that separates the test from the magnetic rate

**PROVED (strictness at every fixed width).** There are entrywise strictly positive, positive-definite three-state transfer matrices with full visibility, satisfying the positive order-one thermal and magnetic rates throughout a fixed window and the numerical purity seed at its left endpoint, for which the right side of (11) is strictly negative at every point of all sufficiently late windows for each fixed $h>0$. Here time, energy and the source derivative have the conventions of §§1 and 5. The example concerns the logical strength of the test on positive transfer families. Whether strictness also holds within the calibrated Wilson family is open.

*Proof.* Let $u=n/512\to\infty$. On $x=B-\beta_K\in[0,d_0]$ with fixed $d_0>0$, put $t(B)=u e^{3x}$, $m(B)=\log(32)/t(B)$, $r=e^{-m}$. For any fixed integer hot aspect $\alpha_h\ge1$ choose $d_0=\log(512\alpha_h)/3$, so $t(\beta_K+d_0)=\alpha_h n$ exactly. With counting measure on three states take
\[
 V=\operatorname{diag}(0,1,2),\qquad
 \pi=(2/5-m/2,\,1/5,\,2/5+m/2),\qquad g_i=\sqrt{\pi_i},
 \qquad T(B)=rI+(1-r)|g\rangle\langle g|.
\]
Use all sufficiently large $n$ so that $\min_i\pi_i\ge1/5$. Extend the diagonal family to independent temporal and spatial parameters by $T(B,s)=e^{-(s-B)V/2}T(B)e^{-(s-B)V/2}$. This gives the magnetic derivative with the same two insertions as the Wilson family. At $s=B$ the top eigenvalue is one and $J=I-|g\rangle\langle g|$ contains both excited states. Their common energy satisfies $-m'=3m$. Along the curve $G=2r^t=1/16$ and $W_t=mG$, hence (HOT) and (VIR-down) hold with rate $3$, and $P_K\ge(16/17)^2>457/625$. Also $v_0=1+m$, $v_J=(\operatorname{Tr}V-v_0)/2=1-m/2$. Thus $G_JD_J/W_t=3/2$ throughout, and the traced isotropic slope minus twice the magnetic slope is zero. ON FILE (rows 1626, 1628, 1638–1640) are related two-state and spectator comparisons. Here neither a hidden level nor a traced anisotropy accounts for the failure.

In vacuum variables the transition from $i$ is $r\delta_i+(1-r)\pi$. Expose the two end states, with any chosen additional middle-state information, and let $\bar V$ be the conditional mean of $V(X_0)$ given that information. By conditional Jensen, $\mathbb E|\bar V-V(X_-)|\le2(1-r)$. All eigenvector endpoint densities in §5 are uniformly bounded since $|f(i)|^2\le1/\pi_i$. Thus replacing $\bar V$ by $V(X_-)$ changes its mean absolute error by $o(1)$ under either law. The plus law has distance at most $1-r^2$ in total variation from the vacuum law, by its defining density. For the minus mixture the two endpoint weights agree when $X_-=X_+$. Their disagreement event has vacuum probability at most $2(1-r)$. Using the endpoint at $X_-$ alone therefore changes the minus law by $O(1-r)$ in total variation. For any orthonormal basis $\{\psi_1,\psi_2\}$ of the excited subspace, the resulting masses on the three states are exactly $(1-\pi_i)/2$, by the diagonal of $J$.

It follows that the two score laws converge weakly on $[0,2]$ to the masses $(2/5,1/5,2/5)$ and $(3/10,2/5,3/10)$ respectively, at scores $0,1,2$. Their limiting common-quantile differences are $-1$ and $+1$ each on an interval of length $1/10$, and zero elsewhere. Away from the finitely many jump parameters, weak convergence gives convergence of these quantiles by bounding the distribution functions on both sides of each limiting atom. Bounded convergence now gives
\[
 \int_0^1 e^{-h(Q_+-Q_-)}\,du\ \longrightarrow\
 \tfrac45+\tfrac15\cosh h>1 \qquad (h>0).
\]
The calculation holds for every sequence of points on the windows since $m\to0$ uniformly. This proves the quantified failure. Allowing an arbitrarily small width chosen afresh at each box would recover the mean by differentiation and give no separation.

**GUESSED (the missing Wilson estimate).** Fix a single $h>0$ and a constant $\eta>0$. The open field comparison would bound the integral in (11) by $\exp[-h\eta W_t/G_{J,t-2}]$ at every required cold point on infinitely many of the same cutoff windows. It tests how the measured distributions of the *exposed* spatial action differ under two specified positive laws. The one-link integration and interval estimates prove neither direction for this comparison. In particular, knowing that both distributions have large fluctuations gives no sign for their quantile displacements.


## 6. The sum rule, the controls and the remaining sign

**ON FILE (rows 710, 1610/1613, 1628–1630, 1635, 1639–1640, 1645).** On an isolated level Michael's isotropic derivative is $-\partial_B m=b^E+b^M$ along the diagonal. In a degenerate block the full trace of the compressed insertion contributes to the fixed-time thermal derivative. Its traces against $J_r$ and $F_r-J_r$ split that contribution without differentiating either projector. For the anisotropy $(B_t,B_s)=(B\xi,B/\xi)$, write $a^{\rm an}=B(b^E-b^M)$. The full slope is $2b^M+a^{\rm an}/B$. For clarity, one set of sufficient *additional* bounds is
\[
  2G_JD_J\ge(\kappa_0+2\epsilon)W_t,\qquad
  \sum_{r<1}r^t\operatorname{Tr}(J_r a^{\rm an}_r)\ge-CW_t,\qquad
  \sum_{r<1}r^t\operatorname{Tr}((F_r-J_r)b_r)\ge-\epsilon W_t .
\]
Indeed $C/B\le\epsilon$ eventually. Adding the three terms then gives the thermal inequality $\partial_B G/t\ge \kappa_0 W_t$ at fixed $t$. The choice $J_r=F_r$ counts all excitations and removes the last condition. A bound for a small visible set must pay the missing contribution. With full visibility and bounded anisotropy, a uniform positive magnetic rate and a uniform positive isotropic rate imply one another after reducing the rate by a fixed margin. That equivalence is already check 1640. The three-state family in §5.1 satisfies both rates, the endpoint bound and the numerical seed, while failing the conjectured fixed-width test on the whole window. This separates the test from (VIR-down) and (PUR-io) in positive transfer families. Logical strictness within the calibrated Wilson law is open.

**ON FILE (checks 1613 and 1630, row 1642 §3 and check 1644 §1.1).** Fix $\ell=L_h b^d\in1024\mathbb N$ and $d$ before $K$, large enough for the prescribed budget at the chosen $\kappa_0>0$. The missing estimates must hold on the cold part of $t(B)=(n/512)e^{\kappa_0(B-\beta_K)}$ throughout $[\beta_K,\beta_{K+d}]$, on the same infinitely many cutoffs as (HOT). On this curve $dG/dB=\partial_B G-\kappa_0 t W_t$. For example, with (HOT) giving $G\le1/10$ at the right end and the rate whenever $G\le4/21$, the last-crossing argument gives $G(n/512;\beta_K)\le1/10$. Then $P_K\ge(1+1/10)^{-2}=100/121>457/625$. No estimate above proves (HOT) or the required positive residual on the curve.

**ON FILE (checks 1639 §5, 1640 §2, 1644 §§1.6 and 3).** For the Gaussian photon at the isotropic point the magnetic insertion on excitation numbers $n_k$ is $b^M=-B^{-1}\sum_k n_k\tanh(\omega_k/2)$. Exciting a nonzero oscillator increases the spatial field variance. In the zero-monopole compact Gaussian the electric flux rotor adds zero magnetic insertion. Hence the right side of (11) is nonpositive for any nonempty collection of these states. With the full continuous centre projection only the photons remain. With the half-turn projection the $\pm2$ fluxes survive and the late bounded-aspect compact Gaussian windows have no cold points. In interacting weak Wilson $U(1)$ the on-file periodic Villain input gives $G(\alpha n)>1$ at sufficiently large bare coupling for each fixed integer $\alpha\ge1$. For fixed $d$, the window widths are bounded above (check 1630 §1.2). Taking an integer $\alpha\ge\sup t(B)/n$ and using time monotonicity gives the same empty-cold-set qualification on those windows. The failure of (HOT) here reads the Coulomb cost of the fluxes. I cannot prove the magnetic sign for interacting weak Wilson $U(1)$ with full centre projection, or exhibit a violation at a cold point of its half-turn window.

**PROVED (scope of the fluctuation estimate).** The local method in §§2–4 also works for interacting cosine $U(1)$: the conditional variable is on $S^1$. For $k\ge4$ its $y=k(1-z)$ density is proportional to $e^{-y}y^{-1/2}(2-y/k)^{-1/2}$. Its integral up to $k$ is uniformly bounded, and above $k$ it is at most $C\sqrt k\,e^{-k}$ by rescaling $y/k$. The same two intervals as in §2 have positive lower mass, and the transverse variance is $\mathbb E(1-z^2)$. The remaining proof uses only this variance, bounded local terms and the actual Wilson conditional product law. In five-dimensional $SU(2)$ use $N=n^4$, six spatial staples per spatial link and two temporal staples. Choose the even parity of the other spatial coordinates on a slice, also including time parity for the all-time computation. Each selected link still meets every incident plaquette alone within its selected class. In the good-staple proof replace $4,3$ by $6,5$. The number of links and plaquettes per site changes by fixed factors. Thus the fluctuation and secant estimates persist in both control models. A variance floor cannot supply the selective step of Lemma ALG (row 1553).

**ARGUED/GUESSED (five-dimensional control).** In the linearized five-dimensional transverse-field theory the Gaussian magnetic formula above holds mode by mode, including after colour-singlet projection: pair creation and annihilation in each oscillator change its energy by $2\omega_k$, so only the number term survives compression. The interacting five-dimensional sign is open. If its actual lowest neutral energy has $nm_1\to0$ along the proposed boxes, then $G(t)\ge e^{-tm_1}$ gives $\liminf G(t)\ge1$ at bounded $t/n$, ruling out (HOT). This spectral premise is GUESSED (checks 1613 and 1644), and would be a statement about the law. Merely counting spatial directions or colour generators cannot establish it.

**PROVED (spectator check).** In a product with an independent spectator, choose an excitation in the spectator alone. The endpoint factors $f_\pm$ then depend only on the spectator, so both positive laws in (11) have the identical Wilson magnetic-score marginal. The matched test is zero although the excitation has positive energy. If the observer misses this sector it enters the hidden-state obligation instead. ON FILE (rows 1553, 1628, 1638/1640): the spectator and the electric-only comparisons already separate numerical purity from the required slope on general transfer families. In particular check 1639's electric-only example has purity tending to one with zero spatial-source response. These comparisons do not decide an implication restricted to the calibrated isotropic Wilson law.

RESULT (d), a partial magnetic-source estimate on the actual Wilson boxes, proved by hand.
PROVED in (3) and (10) that separate pressure secants at any width $h\gg(1+B)/n^2$ cannot certify a positive deficit at a cold point.
PROVED in (4)–(6) that in each state with $tm$ bounded the total magnetic action escapes every exterior-predicted interval of width $o(n^{3/2}/(1+B))$, uniformly on late windows.
PROVED in (7)–(9) that the visible-state lower bound recovers positive fluctuation terms, and one middle-slice conditional term can be removed exactly before vacuum subtraction.
PROVED (11) gives a lower bound from two positive exterior laws. Section 5.1 proves it can fail at every fixed width despite a positive magnetic rate, (VIR-down) and the numerical seed in a three-state family.
The reopen condition, thermal VIR-down, PUR-io and the mass gap remain open. No numerical proof step or Lean computation. Author check only.
