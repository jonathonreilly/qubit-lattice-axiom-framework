# Repo search

Row 1480, Codex, checkout `4636d447886e`. The target-specific prior file was absent. I searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). Searches for `384[- ]contour`, `gap-k2-integrated`, `K2-STEP`, `Q2[_ -]kappa`, `pinned fluctuation law`, `mixed hot.cold`, `integrated small.field activit` returned no Q2 statement. Method searches included Wilson cubic, quartic tadpole, mixed majorant, staggered Cartan source and pinned Gaussian singleton.

- On PR 10114, `ym4d-proof/SOFTHARD.md` 350–357 permits reuse of the fine Wilson cubic tensor subject to recomputing its pullback. `BFT_B.md` 352–359 gives the soft-chain vertex $\kappa\langle r_l,\rho_l^{(2)}\rangle$. `REVIEW55_NORMS.md` 86–89 checks the fine cubic Ward identity. `UNIFORM_ONE_LOOP_COUPLING_ASTRA.md` 541–549 assigns its neutral quartic tadpole to its finite coefficient $a_n$. These address different pins or unintegrated vertices.
- `ym4d-proof/RD4.md` 448–460 derives a connected log given a mixed majorant and exact gluing under common local references. The earlier `prior/repo-search-2026-11-08.md`, sections 9 and 12, records this distinction and the restriction of the flat-fibre comparison.
- Main's `research/ym4d/library/ym4-assembly.md` 266–286 lists the extraction and nonlinear-formation imports of the hard-route step. The local `open-registry.md` row H-SF gives a formation estimate with leading error $C_f\theta^{-1/2}(\log\theta)^{p_0}$ under its presentation hypotheses. H-LF requires exact integration of each physical weight. No Q2 ownership match appeared in the registry, `open-core.md` or `l17c.md`.
- In this lane row 1460 caps a coarse-bond Hessian by the pin strength. Row 1469 bounds the log-density change on a rough staggered field by $3\kappa$ per coarse site. Row 1472 gives $72h^6/x$ for antipodal pairing on one test curve, $15/x$ for the linear-curl quartic mean, and a raw hot-block estimate. Row 1478 checks those results. Row 1479 owns the signed readout. [Step identity](gap-crux-direction-fable.md) · [Design check](gap-k2-tool-design-check-astra62.md) · [Pointwise estimate](gap-k2-t1-small-field-astra62.md)

## Result for row 1480

**Proved by hand.** A single integrated cold-block activity violates the absolute Kotecký–Preiss bound for the Gaussian reference and the fixed real plaquette cut $1/2$. It still violates the bound with the field weight of row 1468. The example uses $\kappa=x$, a periodic Cartan coarse field with angle $1/8$, and all sufficiently large $x$. It survives extraction of the full Gaussian action and of the exact vacuum and quadratic Taylor terms of the integrated singleton. At coarse angle $h/\sqrt{x}$ its first residual is $19h^4/(729x)$. The bound with a nonlinear constrained classical centre remains open. “Proved” below denotes a written argument by the author.

## Plan saved at creation

1. Check the prior-work record, the governing instructions, the registry and the index. Locate the exact contour and block-map conventions.
2. Evaluate the two specified period-two fields using the contour definition. Keep exact finite algebra distinct from any interpretation of the map.
3. Identify the pinned law and the vacuum and curvature subtraction. Compute the connected cubic-pair and quartic contributions as far as the specified data permit.
4. Test the resulting activity norm for cold, hot and mixed supports at x ≥ 100. Record a proof, a particular violating integrated activity, or the precise open estimate. End with two next rows and their decisive outcomes.

## The two fields and all 384 contours

**Proved by direct substitution.** Fix a coarse bond from $2y$ in direction $\mu$, an offset $\xi\in\{0,1\}^4$ and one of the 24 coordinate orders. Write $P$ for its offset leg and $u=2y+\xi$. The transporter is $P W_\mu(u)W_\mu(u+e_\mu)(T_{2e_\mu}P)^{-1}$. In the three-face example of row 1472 the nontrivial $(3,4)$ squares have boundary labels $e^{It},e^{Jt},e^{Kt},1$ at $(n_1,n_2)=(1,0),(0,1),(1,1)$. All positive fine bonds lift parity-cube edges, with the label inverted when the longitudinal bit is one. Successive longitudinal links therefore have mutually inverse labels. Translation by two preserves each ordered link on $P$. In the commuting example the log is $It(-1)^{n_\mu}$ times the number of odd lower coordinates. That count is independent of $n_\mu$, and translation by two preserves every link. In each case the middle product is 1 and the last leg retraces the same group factors in reverse order. This includes $\xi_\mu=1$, zero-length legs and repeated geometric paths. Every labelled contour gives 1 before averaging. This verifies the input to this row and agrees with the check in FINISH 1478. The curves have zero Haar measure and give no lower bound on an integrated activity.

## Published inputs

The outline and complete account are the supplied bundle at `31a47c543775`. Index chunks 01–02, 07 and 13 and the chunk 15 entries in `obligations.md` identify the following statements. Outline 1271–1279 and 1357–1373 prove the Kotecký–Preiss conclusion conditional on its activity inequality and require a separate large-field label estimate. QC1 at 7945–7976 uses a nearby logarithmic mean on odd blocks. At 14261–14270 the local Gaussian theorem requires a separate completeness identification. At 16344–16371 the authors specify the hypotheses on nonlinear domains and histories. [Outline index](sa-index/README.md)

CA-I 4023–4045 marks the unmarked-increment proof incomplete. CA-I 74067–74088 assumes the flat fluctuation theorem and summation estimates in its relative construction. CA-I 80765–80786 assumes the fluctuation-polymer theorem in the orbit-data step. CA-II 3521–3556 proves $|\Phi(X)|\le E^*e^{-\kappa d(X)}$ for analytic potentials with its stated covariance, domain, cutoff and Bałaban bounds. Bałaban's CMP 109, p. 259, and CMP 122, pp. 175, 185, as quoted in row 1470, require sufficiently small parameters. CA-III 1055–1067 quotes constants depending on $d,L$ and uniform in the shell sequence. The numerical side-two activity estimate is a separate hypothesis for Q2. [Bałaban quotations](gap-k2-floor-sizing-opus.md)

## Integrating the Wilson vertices

**Proved for the pinned quadratic fluctuation measure.** Use a finite periodic torus and fix the descending-coordinate tree in each fine block, leaving its base free. Lebesgue measure on the remaining real link logarithms is the reference in this paragraph. Let $Q$ sum the signed link logs on the 384 contours and average. Let $d$ take the oriented plaquette sum. In units $W_e=\exp(g A_e)$, $g=x^{-1/2}$, and $V_c=\exp(g b_c)$, the reference is proportional to
$$
\exp[-\|dA\|^2/2-a\|QA-b\|^2/2]\,dA,\qquad a=\kappa/x.
$$
Its covariance in each colour is $C=(d^*d+aQ^*Q)^{-1}$ on the tree slice. Its mean is $m=aC Q^*b$. To see positivity, a closed one-form has path-independent integrals on contractible loops. $QA=0$ then makes each straight coarse transport zero, since all its contours differ by contractible loops. This kills every torus period and makes the potential equal at adjacent bases. The tree edges make the potential constant throughout each block. Thus $A=0$. This argument keeps the torus holonomies as integration variables. The three colours have independent noises with the same $C$.

For one plaquette $p$, write $v_1,\ldots,v_4$ for its four signed link vectors in path order. Regard them as imaginary quaternions. Write $G_{ij}=v_i\cdot v_j$ and $D_p=\sum_{i<j<k}\det(v_i,v_j,v_k)$. Define the quadratic polynomial in Gram entries
$$
\begin{aligned}
L(G)={}&\sum_i G_{ii}^2/24+\sum_{i<j}G_{ii}G_{jj}/4\\
&+\sum_{i<j}G_{ij}\left[(G_{ii}+G_{jj})/6+
                   \tfrac12\sum_{k\ne i,j}G_{kk}\right]\\
&+G_{12}G_{34}-G_{13}G_{24}+G_{14}G_{23}.
\end{aligned}
$$
Then $x(1-\operatorname{Re}\prod_i e^{g v_i})=\frac12|\sum_i v_i|^2+gD_p-g^2 L(G)+O(g^3)$ for fixed $v_i$. Indeed $v_i^2=-G_{ii}$, $\operatorname{Re}(v_i v_j)=-G_{ij}$ and $\operatorname{Re}(v_i v_j v_k)=-\det(v_i,v_j,v_k)$. The quartic terms come from the exponent partitions $4$, $2+2$, $3+1$, $2+1+1$ and $1+1+1+1$, respectively. The last line uses $(u\times v)\cdot(w\times z)=(u\cdot w)(v\cdot z)-(u\cdot z)(v\cdot w)$. These signs use the Wilson convention $e^{-S}$.

**Proved, integrated coefficients.** At $b=0$ set $C_{ij}$ equal to the covariance of the two *signed* edges in one colour. In $L$, replace each product $G_{ij}G_{kl}$ by
$$
9C_{ij}C_{kl}+3C_{ik}C_{jl}+3C_{il}C_{jk}.
$$
This gives the whole integrated Wilson quartic. Pair the four Gaussian entries in all three ways and sum the two colour indices to get the factors $9,3,3$. For an ordered triple $I$ in $p$ and $J$ in $q$, let $C_{I,J}$ be the $3$-by-$3$ cross-covariance of their oriented edges in one colour. Then
$$
\mathbb E_0 D_p=0,\qquad
\mathbb E_0(D_pD_q)=6\sum_{I\subset p,\ J\subset q,\ |I|=|J|=3}\det C_{I,J}.
$$
Expand each determinant in colours. Each colour occurs once on each side and must pair across. The two permutation sums give six times the signed minor. No individual cubic was replaced by its absolute value.

More generally put $\Delta_C=\sum_{e,f,\alpha}C_{ef}\partial_{e\alpha}\partial_{f\alpha}$ in unsigned link coordinates. The integrated quartic at mean $m$ is $(1+\Delta_C/2+\Delta_C^2/8)L(G(m))$, with the derivatives acting on the whole link polynomial. This follows by expanding at $m$ and using the Gaussian second and fourth moments. Internal contractions of $D_p$ vanish by colour antisymmetry. Hence
$$
\operatorname{Cov}_m(D_p,D_q)
=\sum_{j=1}^3\frac1{j!}
\big\langle \nabla^jD_p(m),\,(C\otimes I_3)^{\otimes j}\nabla^jD_q(m)\big\rangle .
$$
Taylor expansion in the two cubic polynomials gives this identity. The connected product requires at least one cross-pair. For $j$ cross-pairs the two Taylor factors and the $j!$ matchings give $1/j!$.

The Wilson part of the second-order *log-weight* coefficient, on any specified set of plaquette insertions, is $\sum_p\mathbb E_m L_p+\frac12\sum_{p,q}\operatorname{Cov}_m(D_p,D_q)$. The first-order term is $-\sum_p D_p(m)$. These are finite Gaussian polynomial integrals, equivalently coefficients in formal insertion parameters. Exponentiating an unrestricted cubic polynomial under a Gaussian would require a separate integrability argument. In the second-order coefficient, remove its whole constant and degree-two Taylor terms in $m$. What survives is exactly
$$
\sum_p L(G_p(m))+\tfrac12\sum_{p,q}
     \langle\nabla D_p(m),(C\otimes I_3)\nabla D_q(m)\rangle .
$$
On a common Cartan axis every such gradient vanishes. Each entry is a cross product of parallel vectors. Commutation gives $L(G_p(m))=|(dm)_p|^4/24$. This cancellation includes the cubic pair at nonzero mean. The pin and Haar terms are kept exact in the activity test below. Wick's formula here evaluates the indicated vertices of the quadratic reference. The compact nonlinear posterior has its own normalization.

### The compact pinned law

**Proved, finite-volume moment formula.** The same Wilson insertions can also be integrated against the exact compact posterior. The following expression evaluates those posterior moments without a remaining integral. On the free tree-slice links use quaternion coordinates $q_e$. Let $\mathcal H$ multiply, over links, the Haar monomial values. They are zero for an odd coordinate exponent and $\prod_i(2k_i-1)!!/\prod_{j=0}^{\sum k_i-1}(4+2j)$ for exponents $2k_i$, with empty products one. Extend linearly. This is the sphere-moment functional already derived in [the two-cycle calculation, lines 110–116](gap-rg-two-cycle-astra62.md). In particular $F(v)=\sum_{j\ge0}\mathcal H(q_0^{2j})v^{2j}/(2j)!$.

For $P=1,D_p,D_pD_q,L_p$, form the following limit $T(P)$ in the principal-log coordinates used above. Write $T=x\sum_p\operatorname{Re}W_p+\kappa\sum_c\operatorname{Re}(M_cV_c^{-1})$, a polynomial in link coordinates. Replace $e^T$ by its degree-$N$ Taylor sum. In $\prod_c 1/F(\kappa\sqrt{|M_c|^2})$ replace the scalar function of $|M_c|^2\in[0,1]$ by its degree-$N$ Bernstein polynomial. In $P$ replace each rescaled link log by $\sqrt{x}\,\operatorname{Im}q_e$ times the degree-$N$ Bernstein approximation on $[-1,1]$ to
$$
v\longmapsto f(\max(v,-1+\delta)),\qquad
f(v)=\arccos(v)/\sqrt{1-v^2},\quad f(1)=1.
$$
Apply $\mathcal H$ to the *product* of these polynomials. Take $N\to\infty$ first and then $\delta\downarrow0$. The omitted Wilson constant cancels from ratios. The exact compact-posterior quartic mean is $T(L_p)/T(1)$. Its connected cubic pair is
$$
T(D_pD_q)/T(1)-T(D_p)T(D_q)/T(1)^2.
$$
Multiply by $g^2$ for the quartic insertion and by $g^2/2$ in the ordered pair sum. These are marked moments of the nonlinear law. The Gaussian minors above evaluate the coefficients of the expansion about the quadratic reference.

For fixed $\delta$, the Taylor approximation is uniform on this finite graph. Bernstein approximation to a continuous function is uniform. Its value at $v\in[0,1]$ averages the function at $K/N$ for binomial $K$ of mean $Nv$ and variance at most $N/4$. Uniform continuity and the variance bound give convergence. The clipped log vector has norm at most $\pi$ since $\theta/\sin\theta$ increases for $0\le\theta<\pi$. The point $q_e=-1$ has zero Haar mass. Dominated convergence gives the stated limits, with $T(1)>0$. If a hot or cold restriction is required, one can insert continuous ramps converging pointwise to its plaquette indicators, approximate each ramp by the same Bernstein rule, and take the ramp limit last. For the cold inequality $v<v_0$ use $\max(0,\min(1,\ell(v_0-v)))$ with $\ell\to\infty$ and $v=|1-W_p|^2/4$. This order integrates the signed polynomials before taking any absolute values. The counterexample below uses hand inequalities for the integral.

## A normalized fine-block activity

**Definition.** Take a periodic coarse $4^4$ torus and fine side $8$. The formulas also apply to larger even coarse periods in direction 1 and arbitrary other coarse periods at least four. Write $A$ now for *unscaled* fine logs in the same tree slice. Set $W_e=\exp A_e$. For coarse logs $b$, set $V_c=\exp b_c$. Assign plaquettes by their fine base site, positive fine links by their origin, and positive coarse bonds by their tail block. Put
$$
G_B(A;b)=\tfrac12\sum_{p\in B}|(dA)_p|^2+
          \tfrac a2\sum_{c\in B}|(QA)_c-b_c|^2,\qquad
G_*(b)=\min_A\sum_B G_B(A;b).
$$
Let $\gamma_{b,x}$ be the normalized Gaussian with exponent $-x\sum_B G_B$. Completing the square extracts the full coarse Gaussian action $xG_*(b)$, including its finite-momentum dependence. Write $k_c(W,V)=e^{\kappa\operatorname{Re}(M_cV_c^{-1})}/F(\kappa |M_c|)$, $F(s)=\int_{S^3}e^{s q_0}\,dq$, and $k_0=e^\kappa/F(\kappa)$. All Haar measures have mass one.

Let $D_B$ impose $|A_e|<\pi$ on the free links used by that block's contours, assigned plaquettes and assigned links. Overlapping copies of these chart indicators multiply to the same indicator. Put $J_B=\prod_{e\ {\rm assigned,\ free}}(\sin|A_e|/|A_e|)^2$, with value one for a zero log, and $S_B(W)=\sum_{p\in B}(1-\operatorname{Re}W_p)$. Let $C_B$ require that every assigned plaquette has chord $|1-W_p|<1/2$. Define the two factors
$$
f_B={\bf1}_{D_B}J_B\,e^{xG_B(A;b)-xS_B(W)}
              \prod_{c\in B} k_c(W,V)/k_0,\quad
f_{B,C}=f_B{\bf1}_{C_B},\quad f_{B,H}=f_B{\bf1}_{C_B^c}.
$$
These factors are bounded at fixed volume and $x$ since their chart covers every variable they read.

**Proved, exact normalization.** Fixing the internal trees uses base-identity gauge transformations. Order the nonbase sites by tree distance and change each tree variable to its site transport. Left and right Haar invariance give unit Jacobian and each unused site variable integrates to one. In exponential coordinates normalized Haar is $(2\pi^2)^{-1}(\sin |A|/|A|)^2 d^3A$. Completion of the square now gives the exact Q2 image
$$
Z(V)=c_\Lambda(x)e^{-xG_*(b)}
  \mathbb E_{\gamma_{b,x}}\prod_B[1+(f_{B,C}-1)+f_{B,H}],
\tag{1}
$$
where $c_\Lambda(x)$ consists of the flat bond factors, the Haar constants and the Gaussian determinant. It is independent of $b$. The tree has 15 edges per block and the same 49 free links per block contribute on both sides.

Give $f_{B,C}-1$ and $f_{B,H}$ separate indeterminates for every $B$ inside this expectation. The coefficient of the cold mark for $B$ alone, in either the partition function or its connected logarithm at zero marks, is
$$
J_{B,x}(b)-1,\qquad J_{B,x}(b)=\mathbb E_{\gamma_{b,x}} f_{B,C}.
\tag{2}
$$
The mark belongs to a single *fine block*. Its integrated value can depend on exterior coarse data through the Gaussian mean. Its coefficient already includes all the fluctuations of the normalized pinned Gaussian, with the exact local Wilson, Haar and 384-contour pin corrections. A hot mark has coefficient $\mathbb E_\gamma f_{B,H}$ in the same expansion. Higher mixed coefficients use their joint moments under the same law. This construction specifies the activity convention even for correlated Gaussian blocks.

For the counterexample give the singleton its exact vacuum and entire quadratic Taylor term. On the ray $b(t)$ below put
$$
j_x(t)=J_{B,x}(b(t)),\quad
P_x(t)=\log j_x(0)+\tfrac12t^2(\log j_x)''(0),\qquad
z_{B,C}(t)=e^{-P_x(t)}j_x(t)-1.
\tag{3}
$$
Conjugation by a quaternion perpendicular to the chosen Cartan axis takes $t$ to $-t$, so the linear term vanishes. This is an exact extraction in (1). Divide both $f_{B,C}$ and $f_{B,H}$ by $e^{P_x}$ and take the product of the extracted factors outside. On general coarse logs the corresponding prescription is the constant and full Hessian at zero of $\log J_{B,x}$. It gives (3) on this ray. The degree-two subtraction includes every curvature coefficient that a local quadratic Taylor projection could keep here.

**Norm being tested.** Use star-touching incompatibility as in row 1472. An absolute KP estimate at fixed real $V$ has $\sum_{Y\not\sim X}|z_Y(V)|e^{u_Y}\le u_X$ for nonnegative weights $u$. Already the self term requires $|z_{B,C}(V)|\le u_B e^{-u_B}\le 1/e$. For a weighted test, divide the singleton by $1+\theta x E_{\widehat B}(V)$, $0<\theta\le1$, with $E_{\widehat B}$ the sum of $1-\operatorname{Re}V_p$ in the fixed enlarged support. The same necessary inequality then holds for this normalized activity. Any exponential size weight only increases its numerator. Even using every plaquette of the fixed torus in the denominator costs at most $1+12x|\Lambda_{\rm coarse}|$. The counterexample below violates both tests.

## The staggered Cartan source

**Proved.** Fix an imaginary unit $I$, put $\epsilon_y=(-1)^{y_1}$, and take $b_2(y)=It\epsilon_y$, $b_\mu(y)=0$ for $\mu\ne2$. The direction-1 coarse period is even. For the moment work before imposing tree gauge. On both fine layers $n_1=2y_1,2y_1+1$ take the direction-2 link log to be $Iu\epsilon_y$. Put the direction-1 log equal to zero on an even layer and $-Iu\epsilon_y$ on an odd layer. Set the other logs to zero. The direction-1 part is a periodic gradient since successive block signs alternate. Transform by a Cartan site potential vanishing at all block bases to set the trees to zero. Explicitly, the potential added by forward difference is $-Iu\epsilon_y\,\xi_2$ on $2y+\xi$. This sets all interior links to zero and leaves every contour transporter and curl unchanged. The resulting free logs have length at most $2|u|$.

Only eight of the 96 assigned fine plaquettes carry curvature in each block. They are the $(1,2)$ plaquettes on its odd direction-1 layer. Their angles are $-2u\epsilon_y$. Along a direction-2 contour the two offset legs cancel and the straight part has angle $2u\epsilon_y$, for every order and offset. Along a direction-1 contour the two offset legs together have angle $2u\epsilon_y\xi_2$ and the middle contributes $-u\epsilon_y$. Thus exactly half its transporters have angle $u\epsilon_y$ and half $-u\epsilon_y$. The order of axes is immaterial since the direction-2 field has the same value on both layers of a block. The two other coarse means equal one. Consequently
$$
M_1=\cos u,\quad M_2=\exp(2Iu\epsilon_y),\quad (QA)_1=0,\quad (QA)_2=2Iu\epsilon_y.
\tag{4}
$$

The quadratic action per block on this field is $16u^2+\frac a2(2u-t)^2$. Its minimizer is also the minimizer in the *whole tree slice*. To check the normal equation, vary arbitrary fine links before tree fixing. The Wilson gradient $d^*dA$ is $2Iu\epsilon_y$ on each direction-2 fine bond and zero on all other bonds. Indeed the one-dimensional second difference sees one equal and one opposite neighbour. In $\sum_y\epsilon_y(Q\,\delta A)_2(y)$ the offset legs cancel under translation by $2e_2$. Both straight steps contribute the same sum because $\epsilon_y$ is independent of direction 2. Their total is $\frac18\sum_n\epsilon_{\lfloor n/2\rfloor}\delta A_2(n)$, componentwise. The full gradient therefore vanishes at
$$
\alpha=\frac{a}{8+a},\qquad 2u=\alpha t .
$$
Internal gauge fixing preserves the quadratic action, and the precision is positive on that slice. This proves that the displayed field is the mean $m(t)$ of $\gamma_{b(t),x}$ for **every** $x$.

**Proved, a positive rate for the integrated singleton.** For $|t|<1/4$, the mean lies in the interior of $D_B\cap C_B$. The local Haar Jacobian there is positive. The large-$x$ rate of $f_{B,C}$ at the mean equals the local quadratic energy minus the exact Wilson and pin energies. By (4) it is
$$
\begin{aligned}
\Delta_a(t)
={}&8\,[\,(\alpha t)^2/2-1+\cos(\alpha t)\,]\\
 &+a\,[\,((1-\alpha)t)^2/2-1+\cos((1-\alpha)t)\,].
\end{aligned}
\tag{5}
$$
The direction-1 mean has positive real part and its pin phase costs zero. Its nonunit norm remains in the normalized kernel. To account for that factor at all nearby fields, put $h(s)=e^{-s}F(s)$. For $r=|M_c|$,
$$
k_c/k_0=e^{-\kappa(r-\operatorname{Re}(M_cV_c^{-1}))}
            \,h(\kappa)/h(\kappa r).
$$
The last ratio is at most one since $h$ is decreasing. For $0<\delta<1$ it is at least $m_\delta e^{-\kappa\delta}$, where $m_\delta>0$ is the Haar mass of $q_0>1-\delta$. This proves uniform convergence of the log of that ratio divided by $x$ to zero, including $r=0$.

Take a fixed ball about $m(t)$ contained in $D_B\cap C_B$. By continuity its Wilson and pin discrepancy can be bounded below by $\Delta_a(t)-\varepsilon$ by reducing the radius, and $J_B$ is bounded below there. Its $\gamma_{b(t),x}$ probability tends to one since the covariance is $(C\otimes I_3)/x$ on this finite torus. Integrating this ball with the *normalized* Gaussian and then letting $\varepsilon,\delta$ decrease proves
$$
\liminf_{x\to\infty}x^{-1}\log j_x(t)\ \ge\ \Delta_a(t)
\ \ge\ \frac{8\alpha^4+a(1-\alpha)^4}{25}\,t^4>0
\quad(0<|t|<1/4).
\tag{6}
$$
For $|v|\le1$, the alternating cosine series gives $v^2/2-1+\cos v\ge v^4(1/24-1/720)>v^4/25$ for $v\ne0$. The integration uses a set of probability tending to one. No value on a single field supplies (6) by itself.

## Exact vacuum and curvature extraction

**Proved.** The hybrid integral defining the marked block has the same quadratic Taylor energy at its unique zero as the reference Gaussian. Here are the localization details needed to subtract its *integrated* Hessian.

After canceling the marked quadratic in the Gaussian density, its real phase is
$$
H_t(A)=\sum_{D\ne B}G_D(A;b(t))+S_B(W)
          +a\sum_{c\in B}\bigl(|M_c|-\operatorname{Re}(M_cV_c^{-1})\bigr).
$$
The integral for $j_x(t)$ is a fixed Gaussian normalization constant times $x^{n/2}e^{xG_*(b(t))}\int e^{-xH_t(A)}\,w_x(A)\,dA$, where $n$ is the real dimension of the slice. The amplitude $w_x$ is the two indicators in $f_{B,C}$ times $J_B$ and the ratios $h(\kappa)/h(\kappa |M_c|)$. It is independent of $t$ and lies in $[0,1]$.

At $t=0$ all terms in $H_0$ are nonnegative. On the closure of the local chart, $H_0=0$ forces $A=0$. On each unmarked block the linear curl vanishes. Internal paths can be interchanged across elementary squares, so the internal tree with zero logs forces all internal logs to vanish. On $B$ the same square interchanges use the flat *group* plaquettes and the identity tree. Every internal group link is then one, whose only log of length at most $\pi$ is zero. For each outgoing face, the plaquette crossing that face and one internal transverse edge equates crossing links at adjacent transverse positions. These equalities are additive on an unmarked block and group equalities on $B$. The two internal transverse links are zero or identity by the preceding argument. All eight crossing links on that face therefore agree in the relevant sense. Every contour uses one such link, with all remaining links internal. The linear pins force each unmarked face value to vanish. The marked pin has a unit group mean and zero phase cost, forcing each marked face value to be one. The chart again forces zero logs there.

On $D_B$, $G_B(A;0)$ is bounded, and the full precision is positive. Hence $H_0(A)\ge c\|A\|^2-K$ for some $c>0$, $K<\infty$ on this fixed torus. Continuity and the unique zero give a positive gap on the complement of each neighbourhood of zero in a bounded portion of the closed chart. At zero write $M_cV_c^{-1}=s+v$ with $v$ imaginary. The identity $|M_c|-s=|v|^2/(|M_c|+s)$ gives quadratic term $\frac12|(QA)_c-b_c|^2$. The Wilson term has quadratic term $\frac12|(dA)_p|^2$. Thus near zero,
$$
H_t(A)=\sum_D G_D(A;b(t))+O((\|A\|+|t|)^3).
$$
All constants in this paragraph may depend on the fixed test torus.

For clarity, rescale $A=Y/\sqrt x$, $t=s/\sqrt x$ at fixed bounded $s$. At bounded $Y$ all chart and cold indicators equal one eventually, $J_B\to1$ and $1-|M_c|=O(\|Y\|^2/x)$. Also $(\log h)'(v)=\mathbb E_v(q_0-1)\to0$ under the sphere density proportional to $e^{v q_0}$. For any $\eta>0$, the mass at $q_0\le1-\eta$ is bounded by $e^{-v\eta/2}/m_{\eta/2}$, which proves this limit. The mean value theorem now gives $h(\kappa)/h(\kappa|M_c|)\to1$. The limiting scaled integrand is the reference Gaussian with that source, including exactly its completing-square normalization.

The same limit holds through two derivatives in $s$. In a fixed small ball, positivity of the Hessian in $A$ and the Taylor expansion give $H_t(A)\ge c'\|A\|^2-K't^2$ by completing a scalar square. The first derivative in $s$ of the exponent there is bounded by $K'(1+\|Y\|)$ and the second by a constant, using the analytic real Wilson and pin phases near the identity. The rescaled integrands and both derivatives thus have an integrable polynomial times Gaussian majorant. Outside the ball, the positive gap and the quadratic tail just proved make the contribution tend to zero even after polynomial factors in $x$ and $\|A\|$ from the derivatives. Indeed the change in the outside quadratic terms is bounded by $K''(|t|\|A\|+t^2)$ and the change in the marked pin phase by $4a|t|$. All the factors depending on $s$ can be differentiated at fixed indicators. Dominated convergence gives
$$
j_x(0)\longrightarrow1,\qquad
x^{-1}(\log j_x)''(0)
=\left.\partial_s^2\log j_x(s/\sqrt x)\right|_{s=0}\longrightarrow0.
\tag{7}
$$
The limiting normalized Gaussian integral is identically one in $s$. The proof works along every fixed coarse direction. In particular a fixed finite linear projection of the residual Hessian has coefficient $o(x)$ on this torus. Replacing its quadratic Taylor monomial by a fixed smooth curvature representative with the same coefficient also changes the log at fixed $t$ by $o(x)$.

## The integrated quartic at fluctuation scale

**Proved.** For each fixed real $h$, the same renormalized singleton has the limit
$$
\lim_{x\to\infty}x\,z_{B,C}(h/\sqrt{x})
=\frac{8\alpha^4+a(1-\alpha)^4}{24}\,h^4 .
\tag{8}
$$
This computes the first residual coefficient where the external field itself is on the Gaussian fluctuation scale.

Here are the expansion and its error control. Write $g=x^{-1/2}$, $A=gY$, $t=gs$ with $s$ in a fixed compact interval. Under $\gamma_{b(gs),x}$, $Y=s\,m(1)+\eta$ with centred covariance $C\otimes I_3$. The symbol $m(1)$ here denotes the linear mean map evaluated on the unit source. Let $U_3(Y,s)$ and $U_4(Y,s)$ be the degree-three and degree-four Taylor polynomials (homogeneous components) of
$$
G_B(A;b(t))-S_B(W)-a\sum_{c\in B}(|M_c|-\operatorname{Re}(M_cV_c^{-1}))
$$
evaluated on $(Y,s)$. Its constant, linear and quadratic components vanish. In the exponent the two displayed degrees occur as $gU_3+g^2U_4$. The log Haar and pin amplitudes contribute at order $g^2$ a polynomial $A_2(Y)$ of degree at most two. For the pin amplitude this follows from $(\log h_0)'(k)=-3/(2k)+O(k^{-2})$, where $h_0(k)=e^{-k}F(k)$. Indeed its log derivative times $-k$ is the ratio of the integrals of $e^{-w}w^{3/2}\sqrt{2-w/k}$ and $e^{-w}w^{1/2}\sqrt{2-w/k}$ on $[0,2k]$, by the substitution $w=k(1-q_0)$ in sphere measure. Replacing the square root by $\sqrt 2$ costs $O(k^{-1})$ in each integral by rationalizing the difference. The tails beyond $2k$ are exponentially small times a power of $k$. Integration by parts gives ratio $3/2$ in the limit. Thus $\log[h_0(\kappa)/h_0(\kappa r)]=(3/2)\log r+O((1-r)/\kappa)$ for $r$ near one, and $r=1+O(g^2\|Y\|^2)$. The Haar Taylor term follows directly from $\sin v/v$.

All these expansions can be integrated through two derivatives in $s$. In the region $\|Y\|\le g^{-1/20}$, the analytic Taylor remainder in the exponent is bounded by $K g^3(1+\|Y\|)^5$ on the fixed $s$ interval, also through two $s$ derivatives. Here $g(1+\|Y\|)^3$ tends uniformly to zero. Expanding the exponential and the smooth amplitudes consequently costs at most $K' g^3$ times an integrable polynomial times Gaussian after including the reference density. The chart and cold cuts equal one in this region for small $g$. Outside it, the quadratic domination, positive gap and tail estimates in the proof of (7) bound the hybrid integrals and these derivatives by less than any power of $g$. The Taylor polynomials against the reference Gaussian have the same tail property. One may differentiate the reference density with $Y$ fixed, so its derivatives introduce only polynomials and the indicators stay fixed.

It follows that the log of $j_x(gs)$ has the coefficients
$$
g\,\mathbb E U_3+
g^2\{\mathbb E U_4+\mathbb E A_2+\tfrac12\operatorname{Var}(U_3)\}
+O(g^3).
$$
The expectation uses the shifted normalized Gaussian above. The error is uniform through two derivatives. In particular $\operatorname{Var}(U_3)$ includes the Wilson–pin cross term as well as both cubic pairs. Before restricting the source to its ray, the cubic is invariant under simultaneous rotations of all fine and coarse colour vectors. It vanishes on a collinear tuple because a rotation reverses every vector and the polynomial has odd degree. Its gradient also vanishes there. Each vector derivative must be parallel to the common axis by the residual rotations, and its parallel component vanishes by differentiation within the collinear tuples. Consequently $U_3(s\,m(1)+\eta,s)$ has degree at most one in $s$ for every $\eta$. Its variance has degree at most two. The only possible $s^4$ term in the log is from $\mathbb E U_4$. Its coefficient is $U_4(m(1),1)$ because only the four mean factors can contribute. This is the degree-four coefficient of (5). All odd powers vanish by conjugation symmetry of $j_x(gs)$. Subtraction (3) removes the remaining constant and quadratic terms, including those arising from the cubic pairs. Exponentiating the residual gives (8).

For $a=1$ the coefficient is $4104/(24\cdot9^4)=19/729$. On this stripe only the $(1,2)$ coarse plaquettes are nonflat, so $xE_{\rm whole}(V(h/\sqrt{x}))\le 2N_b h^2$. Thus no finite $c_1$ gives the field-weighted singleton bound $c_1/x$ uniformly over all fixed Gaussian-scale multiples $h$. First take $x\to\infty$ for each fixed $h$ and then let $h$ increase. The size of the bound on a prescribed bounded interval of $h$ is a separate question.

## The violating activity and the hot sectors

**Proved, counterexample.** Take $B$ at the origin, $a=1$ and $t=1/8$. Every coarse plaquette has chord at most $2\sin(1/8)<1/4$. At the Gaussian mean every nonflat fine plaquette has angle of magnitude $1/72$. Equations (3), (6) and (7) give the explicit bound
$$
\liminf_{x\to\infty}\frac1x\log(1+z_{B,C}(1/8))
\ \ge\ \frac{4104}{25\cdot9^4\cdot8^4}>0 .
\tag{9}
$$
Here $4104=8+8^4$. Thus for every sufficiently large $x\ge100$ the necessary singleton inequality fails, even after division by $1+\theta xE_{\widehat B}$. One periodic test volume suffices to disprove a uniform estimate. Equation (9) also gives a counterexample on every fixed torus with the indicated even direction-1 period. The proof supplies an asymptotic violation for the fully quadratic subtraction. The first failing $x$ for this activity is undetermined.

The surviving rate comes from evaluating the Wilson and pin actions on the conditional **mean** chosen by the coarse field. On this Cartan background the integrated Wilson cubic pair has zero degree-four remainder. The real normalized Wilson and pin factors together give the positive rate in (5). A bound confined to a fixed ball in $\sqrt{x}$ times the coarse curvature tests a smaller set of fields. A centre that carries the nonlinear constrained classical action removes a different function of the external field.

**Proved, exact hot and mixed normalization.** For any exact hot set $H$, its posterior probability at $V$ is
$$
\frac{\mathbb E_{\gamma_{b,x}}\big[\prod_{B\in H} f_{B,H}\prod_{B\notin H} f_{B,C}\big]}
     {\mathbb E_{\gamma_{b,x}}\big[\prod_B(f_{B,C}+f_{B,H})\big]} .
\tag{10}
$$
Here the second subscript $H$ on $f$ is the hot label. Vacuum or curvature extractions of the form (3) cancel in this ratio. All label choices are integrated against the same correlated law. At flat $V$ and fixed volume, if $k$ specified blocks are hot, their joint posterior probability satisfies $\limsup_{x\to\infty}x^{-1}\log\Pr\le-k/8$. To see this, divide the physical integral above and below by the flat pin constants. Each pin ratio is at most one. Each hot block pays $x(1/2)^2/2$ on a distinct assigned plaquette. The denominator has log rate zero. Identity is in its support, all phase costs vanish there, and each fixed neighbourhood has positive Haar measure. The bounds for $h$ above give the lower rate by shrinking that neighbourhood. The same argument also bounds the normalized probability with additional cold restrictions on the same fixed torus. Its denominator estimate gives no uniform finite-volume threshold for hot probabilities at 100.

The positive discrepancy also appears in the **full compact integral**. Write $N_b$ for the number of coarse sites. In (1) restrict the numerator at $b(t)$ to a neighbourhood of the periodic mean $m(t)$ where all blocks are cold. Its normalized Gaussian mass tends to one. Each of the finitely many factors has the log-rate lower bound used in (6), uniformly as the neighbourhood shrinks. At $b=0$, the log rate of $Z(1)/c_\Lambda(x)$ is zero by the preceding flat argument. The Gaussian determinant in $c_\Lambda$ contributes only a power of $x$ on a fixed torus. Positivity permits restoring every hot and mixed sector in the numerator. It follows that
$$
\liminf_{x\to\infty}\frac1{xN_b}\log
   \frac{e^{xG_*(b(t))} Z(V(t))}{Z(1)}\ \ge\ \Delta_a(t).
\tag{11}
$$
Subtracting the sum of the local extractions $P_x(t)-P_x(0)$ preserves (11) by (7) and block translations followed, when needed, by a global colour rotation. The same trial region tests the entire physical free energy. One can also subtract the Hessian of that full free energy after Gaussian extraction. At $b=0$, replace each unmarked quadratic in the proof of (7) by its exact Wilson and pin terms. Flat internal plaquettes and the fixed trees give identity internal links on every block. Flat face plaquettes then make the crossing group links equal on each face, and each exact pin forces that face value to one. The chart closure is now compact, the zero is unique, and the full quadratic Taylor energy is again $\sum_D G_D$. The rescaled dominated-convergence argument of (7) gives an $o(x)$ residual Hessian in each fixed direction. In particular a volume-uniform, field-weighted **log-rule** bound $C/x$ for the remainder would also contradict (11). On this fixed torus the weighted sum of local terms would be $O(1)$ in $x$ at both fields since every energy weight is at most $1+12xN_b$. A separate error with positive log rate would have to be carried explicitly. The hot probabilities themselves need not be large for (9) or (11).

**Proved, finite-$x$ check for a Wilson curvature centre.** There is a shorter test when one extracts $x\sum_p(1-\operatorname{Re}V_p)$ in place of the full Gaussian action. Set $a=1$, $x=100$ and vary just one coarse link to $e^{It}$ with $1-\cos t=1/100$. All six affected plaquettes have chord $\sqrt{2/100}$. Let $M_c=m_0+\mathbf m$ and $m_I=\mathbf m\cdot I$. Taking the *exact normalized* posterior at the flat coarse field in the numerator ratio gives
$$
\frac{Z(V)}{Z(1)}
=\mathbb E_{\Pi_1}\exp\{x[(\cos t-1)m_0+\sin t\,m_I]\}
\ \ge\ e^{-x(1-\cos t)} .
$$
Global conjugation flips $m_I$ and preserves $m_0$ and the measure. Averaging the signs gives a factor $\cosh(x\sin t\,m_I)\ge1$ and $m_0\le1$. This also holds for any nonempty fixed hot/cold sector of positive probability, with its own exact normalizer at $1$. The vacuum-normalized, curvature-subtracted **external bond** activity therefore obeys $e^{6x(1-\cos t)}Z(V)/Z(1)-1\ge e^5-1$. Even division by $1+6\theta$ leaves more than $1/e$. This finite-$x$ check extends the local stiffness identity of row 1460 and the rough-field Wilson-centre test of row 1469 to a small external field. It is a different activity from the fine-block singleton (9).

The proofs and hand arithmetic are by Codex and await a separate reader. No numerical quadrature, Monte Carlo or Lean kernel run enters the result. Credit Tadeusz Bałaban for the small-field and large-field RG construction, Roman Kotecký and David Preiss for the polymer criterion, and Ethan Sussman and Levent Alpoge, with Claude and Codex, for the outline, complete account and contour-kernel construction behind Q2. The findings concern the stated expansion and grant no scientific or audit status.

## Next two rows and their decisive outcomes

1. **Nonlinear background for the side-two pin (sketched row).** On the staggered Cartan source minimize the exact Wilson plus pin phase in a gauge-fixed block neighbourhood, including transverse colour variations. Within the Cartan stripe ansatz the minimum per block is $8+a-\sqrt{64+a^2+16a\cos t}$. Indeed one maximizes $\operatorname{Re}[(8+a e^{-it})e^{iv}]$ over $v=2u$. The coefficient of $-t^4$ at $a=1$ is again $19/729$. A decisive positive outcome is a minimizing branch with a volume-independent Hessian lower bound and a local background term that absorbs (5). A competing field or a vanishing transverse Hessian eigenvalue would identify the missing branch or stability condition. This concerns the centre, independently of the signed long-wavelength readout of row 1479.
2. **Normalized activities about that background (sketched row).** Form the all-cold and one-hot marked integrals with the nonlinear centre extracted. For $x\ge100$ either establish one common rooted KP majorant for cold, hot and mixed marks under their joint pin, or exhibit a remaining normalized activity above its singleton or rooted budget. In either case retain the readout, the allowed coarse-field domain and the hot denominator explicitly. Equation (10) specifies the denominator for this test.
