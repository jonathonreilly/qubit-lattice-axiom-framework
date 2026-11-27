# Check of row 1611 (`library/gap-direction7-astra62.md`), FINISH.md row 1612

Checker: Claude Fable 5.2 (subagent of the lead session), 2026-11-27. One line-by-line reading; this is a check, not an audit.
Status: COMPLETE. Every PROVED item HOLDS (no failing line; remarks in section 11). Outcome (d) holds in the letter only; see RESULT.

## 0. Method

Read in full: the target (195 lines), the row 1611 brief in FINISH.md, row 1375 lines 1-207 (`gap-seed4-astra62.md`; the rest through its check), check 1376 in full, row 1573 in full (`gap-band-neutral-astra62.md`), check 1579 item 9 and its RESULT. Further sources are named where used below. Every algebraic step was redone by hand. No numerics enter a verdict. Line numbers L are lines of the target. Not read, as instructed: `gap-direction7-fable.md`, its check, and every `gap-wmix-fixint*` file.

Convention check. Row 1573 L70 fixes the transfer kernel used here: the cylinder integral with half-weight end actions and all temporal links integrated, so "temporal links implement the vertex gauge averages". Hence $S=T^v$ is invariant under separate vertex gauges at its two ends and $P_GS=S$. The target uses both facts (L101, L140). They hold.

## 1. The fixed-range trial theorem (1), L29-L75: HOLDS, given rows 1375/1376 and check 1453 (BND-1)

- **L29-L38, statement.** $p_K=k_v^2/Z_+(2v)$ is a probability density because $\int k_v^2=\operatorname{Tr}(P_0T^{2v})$. Its face marginal is the law that row 1375 treats ($w=n/1024=v$, period $2v=u$). The step to $\operatorname{Aff}(p_K,q\otimes q)$ is monotonicity of affinity under a marginal. The spatial Wilson density is in $\mathcal M_2(n)$ (opposite links of a plaquette are at link-graph distance 2). HOLDS.
- **L42-L46, (2).** This is row 1375 (2), (4) and its L73-L82, checked in 1376 S3-S5 and S14-S16. The variance formula for a finite withheld set with bounded detours is row 1375 L80-L82. On file; accurate.
- **L48, two holes.** $L_{22}(k)=\sqrt{h(h+4)}\,(1-|t_2|^2/h)$ is continuous on the torus with value 0 at $k=0$. If its Fourier coefficients vanished beyond a radius it would equal a trigonometric polynomial everywhere. On the line $(s,0,0)$ it is $\sqrt{(2-2\cos s)(6-2\cos s)}=2|s|+O(|s|^3)$, which is not differentiable at 0. So infinitely many parallel translates $f$ have $L_{ef}\ne0$. Positive definiteness of the two-hole compression is row 1375 (4). HOLDS.
- **L50-L56, (3).** The conditional variance given $S_B$ decreases in $B$ to $1/\kappa_{\{e,f\}}=(L_{ee}-|L_{ef}|^2/L_{ff})^{-1}$; given $S_B$ and $H$ it decreases to $1/L_{ee}$. Since the first limit is strictly larger than the second, and the second is approached from above, some finite $B$ has $\operatorname{Var}(E\mid S_B,H)<\operatorname{Var}(E\mid S_B)$. For Gaussians this is a nonzero conditional correlation. $|r|<1$ by the nonsingular chord covariance (row 1375 L49, check 1376 S8). HOLDS.
- **L58-L63, conditional affinity loss.** Redone: $AA^*(x,x')=\sqrt{\varphi(x)\varphi(x')}\exp[-r^2(x-x')^2/(8(1-r^2))]$, so $\operatorname{Tr}(AA^*)^2=\mathbb E\exp[-r^2(X-X')^2/(4(1-r^2))]=(1+r^2/(1-r^2))^{-1/2}=\sqrt{1-r^2}$. The affinity of $g$ to any product $a\otimes b$ is $\langle\sqrt a,A\sqrt b\rangle\le\|A\|\le(1-r^2)^{1/8}$. Three independent colours tensor. $\gamma=(1-r^2)^{3/8}<1$. HOLDS.
- **L65-L67, the graph and the trial.** The spanning tree is the patch trees plus connectors; the only chords are patch chords and the $2m$ holes. A factor of $q$ that reads a hole reads only links within link distance $R$ of it. These lie in the box and are observed, and no factor reads two holes ($f$ is beyond $R$ from $e$; patches are $D\gg B+R$ apart). Integrating the links outside the graph therefore leaves $b(S)\prod_i a_i(U_i,S)$. Given $S$ the map from $U_i$ to its based scaled chord log is its own bijection off a null set. HOLDS, including for trials that are not gauge invariant.
- **L69-L73, limits.** Each fundamental cycle lies in one patch tree, so each linear current is a translate of a one-patch current. Cross-patch covariances are Fourier coefficients of an $L^1$ function (weight $c=1/\sqrt{h(h+4)}\sim1/(2|k|)$, integrable in three dimensions) and tend to zero as $D\to\infty$. Nonsingular limits give total-variation convergence of the Gaussians. Affinity does not decrease under projection; replacing $p$ by $p'$ moves every affinity by at most $\sqrt{2\,\mathrm{TV}}$. The order $K\to\infty$, then $D\to\infty$, then $m\to\infty$ uses row 1375 only for fixed finite graphs. HOLDS.
- **L75, scope.** $\sqrt{\sum_ja_jq_j}\le\sum_j\sqrt{a_j}\sqrt{q_j}$ and $\sum_j\sqrt{a_j}\le\sqrt J$. HOLDS.

Inputs not rechecked here: the fixed-graph total-variation limit of row 1375 L47-L55 (checked in 1376 S7-S11, itself given rows 1151, 1231, 1339, 1371), and $\beta_K\to\infty$, $\beta_K=O(\log n)$ from check 1453 (BND-1); see section 9.

Character of the result. It is a negative: it removes one family of trial references. Its proof uses the Gaussian limit of fixed graphs at $\beta_K\to\infty$. The same argument applies, with the corresponding free precision, to weak compact U(1) and to five dimensions (the integrability of $c$ only improves). It is not a selective input and the row does not claim that it is.

## 2. The consumer (6) to (7) to (PUR-io), L79-L108: HOLDS

- **L79.** $\|\phi\|^2=\langle1,T^{2v}1\rangle/G(2v)=1$. HOLDS.
- **L81-L99, (4)-(5).** $J_0=|1\rangle\langle1|$. Arrangement A has integral $\operatorname{Tr}(SJ_tSJ_t)\langle1,SJ_tS1\rangle^2$ and B has $\langle1,SJ_tSJ_tS1\rangle^2$; both have six pieces, four joins and four free ends, and both equal $G(v)^6$ at $t=0$. The derivative of each log partition function is $\sum_{j,e}\mathbb E w_{j,e}-4|E|z'/z$, and the second term cancels. HOLDS.
- **L101, the limit.** $J_t=P_GK_t=K_tP_G$ with $K_t$ the product of one-link convolutions by the class function $\pi_t\propto e^{tw}$. $K_t\to I$ strongly, so $J_t\to P_G$ strongly with $\|J_t\|\le1$. $S$ is Hilbert-Schmidt, so $J_tS\to S$ in Hilbert-Schmidt norm and the ring trace converges. HOLDS.
- **(7).** $e^{-D_K(\infty)}=G(3v)^2/(G(2v)^2\operatorname{Tr}T^{2v})$ and $\langle\phi,T^v\phi\rangle=G(3v)/G(2v)$. HOLDS. The trace is over all gauge-invariant states, all eight centre-flux sectors included.
- **L108.** $\langle\phi,T^v\phi\rangle\le\lambda_0^v$ and $Z_+(2v)\le\operatorname{Tr}T^{2v}$ (since $T^{2v}\ge0$), so $e^{-D_K(\infty)/2}\le\sqrt{w_0}$ with $w_0=\lambda_0^u/Z_+(u)$. Then $w_0^2=\lambda_0^{2u}/Z_+(u)^2\le Z_+(2u)/Z_+(u)^2=P_K$. Under (6), $D_K(\infty)=\lim_t\int_0^tD_K'\le2\log(16/15)$, so $P_K\ge(15/16)^4=50625/65536$. Exact comparison: $50625\cdot625=31640625>29949952=457\cdot65536$. Same side, same subsequence. HOLDS.
- **L108, affinity.** $k_v\ge0$ (an average of positive kernels), so $\operatorname{Aff}(p_K,\phi^2\otimes\phi^2)=\langle\phi,P_0T^v\phi\rangle/\sqrt{Z_+(2v)}=\langle\phi,T^v\phi\rangle/\sqrt{Z_+(2v)}\ge e^{-D_K(\infty)/2}$. HOLDS.

Remark R1 (what (6) forces beyond the seed; the author mentions it only as "the electric sectors missed by the cap", L190). From (7), (6) implies three separate statements on the passing subsequence:
  (i) neutral purity, hence (PUR-io);
  (ii) **flux**: $\operatorname{Tr}T^u\le(16/15)^2\lambda_0^u$. Since $\lambda_0^u\le Z_+(u)=\tfrac18\sum_zZ^z(u)$ and $\operatorname{Tr}T^u=Z^0(u)$, this needs $\tfrac18\sum_zZ^z(u)/Z^0(u)\ge(15/16)^2$, that is, the mean of the seven twisted ratios $Z^z(u)/Z^0(u)$ is at least $(8\cdot225/256-1)/7=0.8616\ldots$ In words: the seven odd electric-flux sectors together carry at most $(16/15)^2-1<0.138$ of the vacuum weight at period $u$;
  (iii) **cap**: $G(3v)/G(2v)\ge(15/16)\lambda_0^v$, a statement about the spectral measure of the constant function.
Neither (ii) nor (iii) is a consequence of (PUR-io) by anything on file. See sections 7 and 8.

## 3. Strictness in a transfer class, L110: HOLDS

In the basis of normalized indicators $a,b$ the matrix of $T=|g\rangle\langle g|+\tfrac12|h\rangle\langle h|$ has diagonal entries $1-\delta/2$ and $(1+\delta)/2$ and off-diagonal entry $\tfrac12\sqrt{\delta(1-\delta)}>0$, so the kernel is strictly positive. $\langle1,g\rangle=2\sqrt{\delta(1-\delta)}$ and $\langle1,h\rangle=1-2\delta$, so $c=4\delta(1-\delta)$ and $G(j)=c+(1-c)2^{-j}$. $Z_+(j)=1+2^{-j}$, so $P\to1$. With $\delta=2^{-8n}$, $c=o(2^{-3v})$ and (7) is $(1+o(1))2^{-v}\to0$. The threshold set exists because the Haar law of one plaquette trace has density $(2/\pi)\sqrt{1-w^2}$. The set is gauge and centre invariant. HOLDS. Scope as the author states it: the kernel is not a Wilson transfer, and strictness on the Wilson trajectory is not shown.

## 4. The coefficient (9), L114-L133: HOLDS

- **One join.** Write $\prod_e(1+\varphi_e)$ with $\varphi_e=e^{tw(V_e)}/z(t)-1$, $\int\varphi_e=0$. A subset of edges with a vertex of degree one integrates to zero (leaf gauge first). The smallest subsets with all degrees at least two are the unit squares. Redone for one square: each vertex integral merges two edges with a factor $1/2$ and the last gives $\operatorname{tr}(X_p^{-1})\operatorname{tr}(Y_p)/2$, so $\int\prod_{e\in p}\operatorname{tr}V_e\,dg=\operatorname{tr}X_p\operatorname{tr}Y_p/16$ and $\int\prod_{e\in p}w(V_e)\,dg=w_p(X)w_p(Y)/64$. Evenness in $t$ holds because $n$ is even. So $J_t=1+(t^4/64)U+O_K(t^6)$. HOLDS.
- **The degree-eight term.** Independent derivation. Put $\epsilon=t^4/64$, $J=|1\rangle\langle1|+\epsilon\sum_p|w_p\rangle\langle w_p|+O(t^6)$, and note $\langle1,w_p\rangle=0$. With $\alpha=\sum_pm_p^2$: $\operatorname{Tr}(SJSJ)/G^2=1+2\epsilon\alpha+\epsilon^2\sum_{pq}(C_{pq}+m_pm_q)^2$, $\langle1,SJS1\rangle/G^2=1+\epsilon\alpha$, $\langle1,SJSJS1\rangle/G^3=1+2\epsilon\alpha+\epsilon^2(\sum_{pq}m_pC_{pq}m_q+\alpha^2)$. The order-$\epsilon$ terms of $D_K$ cancel ($2\alpha+2\alpha-4\alpha$). The order-$\epsilon^2$ terms sum to $\sum_{pq}C_{pq}^2$. The first variation of $D_K$ at $J=|1\rangle\langle1|$ vanishes for every direction $\delta J$, so the $O(t^6)$ part of $J$ enters only at $t^{10}$. This reproduces (9) by a route different from the author's covariance count. HOLDS.
- **$C_{pp}>0$.** $C_{pp}=\langle w_p-m_p,S(w_p-m_p)\rangle/G(v)$ and $S$ is strictly positive on gauge-invariant functions (positive one-link character coefficients, row 1573 L210 uses the same fact). HOLDS.
- **L175, character check.** $(I_2/I_1)^4=(t/4)^4(1+O(t^2))$; the normalized square network is $2w_p$; the entry is $4C_{pq}$; $16\cdot4^{-8}=64^{-2}$. $C1=0$ removes the constant. HOLDS and agrees with (9).

## 5. The tail bound (10), L135-L149: HOLDS

After absorbing the join gauges and setting $Y_e=X_eR_e$, the join weight is $\prod_e\pi_t(R_e)$ and one $R_e$ enters exactly one endpoint link of one slab: four half-weight spatial plaquettes and one temporal plaquette, so $|H'|\le3\beta_KH=LH$ and $|H''|\le(L+L^2)H$. Pairing $\pm A$ gives $|\overline H(\theta)/H(1)-1|\le(L+L^2)\theta^2e^{L\theta}/2$. For $t\ge(1+L)^2$: normalizer $\ge c_0e^tt^{-3/2}$, $\mathbb E_{\pi_t}\theta^je^{L\theta}\le c_jt^{-j/2}$ (scale $\theta=x/\sqrt t$, $e^{L\theta}\le e^x$), cap mass $\ge c_1$, and $H/H(1)\ge e^{-1}$ on the cap. The shift of the one-link mean is $\operatorname{Cov}_{\pi_t}(w,\overline H)/\mathbb E_{\pi_t}\overline H$, bounded by $c_2(L+L^2)t^{-2}$ uniformly in the other variables. Eight sums of $3n^3$ links and $\int_{T_*}^\infty t^{-2}dt$ give (10). The two end estimates ($O(1/n)$ above $T_*=(1+3\beta_K)^2n^4$ and below $n^{-4}$) follow. HOLDS. The constant 3 in $L$ is the four-dimensional count; in $d$ dimensions it is $d-1$. The estimate is not selective.

## 6. The identity (11) and the benchmark, L151-L173: HOLD

- **(11).** $C\ge0$ by Cauchy-Schwarz for $B\ge0$ with $\langle1,B1\rangle=1$. $M_t=A_t+|x_t\rangle\langle x_t|$; the three integrals are $\operatorname{Tr}M_t^2=\|A_t\|_{HS}^2+2s_tz_t+s_t^2$, $s_t$, and $\langle x_t,M_tx_t\rangle=s_t(z_t+s_t)$. Hence $e^{D_K}-1=(\|A_t\|_{HS}^2-z_t^2)/(s_t+z_t)^2$. $\langle1,x_t\rangle=\langle J_t^{1/2}1,\rho\rangle=1$ gives $s_t\ge1$. $z_t\le\|A_t\|_{op}\le\|A_t\|_{HS}$ gives $D_K\ge0$. HOLDS.
- **L173, spin weights.** The one-link multiplier on spin $j$ is $I_{2j+1}(t)/I_1(t)$; Parseval gives $\|A_t\|_{HS}^2=\sum r_\alpha r_\eta|C_{\alpha\eta}|^2$. HOLDS.
- **L151-L160, benchmark at $0<\beta<2/9$.** Row 1573 (4) with $d=4$, $m_G=4$: $q=9\beta/2$, $M\le18(3n^3)\beta^2\sum_{r\ge v-2}(r+1)q^r$, a supremum over all pins and all simultaneous unit-speed tangents, for the ordinary gauge-averaged cylinder. This is the object $S$ here (checked in 1579 item 11, given Theorem E of row 1568 as checked in 1572 Step 7). Geodesics of length at most $\pi$ give $|\log[S(x,y)S(x_*,x_*)/(S(x,x_*)S(x_*,y))]|\le\pi^2M_n$. With $f\otimes f$ in every piece both arrangements equal $\langle f,J_tf\rangle^4\langle1,f\rangle^4$ and each join has the law $\propto f(X)J_t(X,Y)f(Y)$. Restoring six kernels changes each normalized density by a factor in $[e^{-12\delta_n},e^{12\delta_n}]$, so $|D_K'(t)|\le8(3n^3)(e^{12\delta_n}-1)$ for every $t$. Times $T_*$ this is exponentially small in $n$; (10) covers the tail. HOLDS, given row 1573 (4). Not selective: row 1573 L182 gives the same benchmark for 4D compact U(1) at $\beta<1/9$ and 5D SU(2) at $\beta<1/6$.

## 7. The U(1) endpoint, the same argument for SU(2), and selectivity

### 7.1 The U(1) endpoint failure, L179-L181: HOLDS, given the Villain input

Sources read: row 1573 L131-L150; check 1579 item 9 (HOLDS, "given row 1565 / check 1571 A2-A3"); row 1565 L153-L203 (`gap-band-cut-covariance-astra62.md`, the Villain flux bound and the offset-uniform transfer); the RESULT and section list of check 1571.

- The chain. For compact U(1) the six-piece construction and (7) hold verbatim ($w=\cos\theta$, $J_t\to P_G$). So $e^{-D(\infty)}=\langle\phi,T^v\phi\rangle^2/\operatorname{Tr}T^u\le\lambda_0^u/\operatorname{Tr}T^u\le\lambda_0^u/Z_{\rm even}(u)\le(1+2d_\gamma^4)^{-1}<1/2$. The third step drops the odd sectors (all terms nonnegative). The last is row 1573 L146-L150: $Z_{\rm even}\ge(1+2d_\gamma^4)Z_{Q=0}$ and $\lambda_0^u\le Z_{Q=0}(u)$. (6) needs $e^{-D(\infty)}\ge(15/16)^2=225/256$. So the target fails at its endpoint. The aspect matches ($2v=u$, $n/u=512$, even periods). HOLDS.
- The single-square remark, L181: the Abelian vertex integral of four cosines is $\tfrac18\cos(\theta_p(Y)-\theta_p(X))$. Redone. HOLDS.
- Does it really fail for weak 4D U(1)? Yes, with these quantifiers and this standing: Villain at each sufficiently large $\gamma$ (row 1565 proves the coset bound at $\beta\ge2000$), and Wilson at all sufficiently large $\beta_W$ (existential; check 1571 calls the threshold astronomically large), at a fixed coupling, on the tori of aspect 512. The whole chain rests on equations (3.1), (4.1), (5.1)-(5.3), (6.1) of the periodic Villain note on main. Check 1571 lists the internal proofs of that note as not checked, and I did not check them either. So the status is "PROVED given that note", as the author says. The author's label is accurate.
- In the unprojected trace the even restriction is not needed: row 1565's $Z_{\rm odd}\ge d_\beta Z_{\rm even}$ already gives $\lambda_0^u/\operatorname{Tr}T^u\le(1+d_\beta)^{-1}$. The author's route through $\pm2$ is correct and uses the form checked in 1579.

### 7.2 The same argument for 4D SU(2)

**Lemma F (PROVED here; three lines).** Put $\kappa_K=G(3v)/(G(2v)\lambda_0^v)\le1$, $w_0=\lambda_0^u/Z_+(u)$ and $f_u=1-Z_+(u)/\operatorname{Tr}T^u$ (the flux-charged fraction of row 1566 Step 5). Then
$$e^{-D_K(\infty)}=\kappa_K^2\,w_0(u)\,(1-f_u).$$
Proof. By (7), $e^{-D_K(\infty)}=\langle\phi,T^v\phi\rangle^2/\operatorname{Tr}T^u$. Insert $\lambda_0^{2v}=\lambda_0^u$ and $Z_+(u)$. The vacuum is neutral, so $\lambda_0$ is the same in both traces. QED
Consequence: (6) forces $\kappa_K\ge15/16$, $w_0(u)\ge225/256$ and $f_u\le31/256$ on the passing subsequence.

So the U(1) argument, applied to SU(2), reads as follows. The ring in arrangement A carries no centre projection. Its trace contains the seven odd centre-flux sectors, exactly as the U(1) trace contains the nonzero charges. The argument therefore neither fails nor passes for SU(2) on file: it passes exactly if $f_u\le31/256$ (and the neutral and cap factors pass). An upper bound on $f_u$ is the open statement (N-flux) of row 1566 Step 5 (checked with corrections in 1570), here at a constant level and at the release couplings. Nothing on file bounds $f_u$ above at any order-one or release coupling. Nothing on file bounds it below by a constant either (row 1565 L140-L143 gives only a lower bound exponentially small in $nv$). Row 1566 L126 recalls that (N-flux) carries a bound on planar Wilson loops through the Tomboulis-Yaffe inequality (row 690, recalled there, not a proof step). So (6) contains a confinement-type demand that the seed does not contain. GUIDE only: on a physical side large enough for the seed, flux weights of order $e^{-\sigma L^2/512}$ would be negligible, so I see no reason to expect (6) to be false for this cause; it is an extra unproved statement, not a refutation.

Why the neutral part differs between the groups. After the three order-two projections U(1) keeps the charges in $2\mathbb Z^3$, and SU(2) keeps only zero, because the centre is $\mathbb Z_2$. That difference is algebra. In the neutral sector the U(1) failure of row 1573 therefore has no SU(2) counterpart for an algebraic reason, and by Lemma ALG (row 1553, section 1.4, read) an algebra-decided property is never an input.

### 7.3 Selectivity verdict

- What the U(1) failure is. It is the contrapositive of the consumer (section 2, which holds for every compact group and dimension) applied to an on-file failure of the full-trace vacuum weight. It is a failure of the target's conclusion. It is not the failure of a step of a proof, because no step toward (6) at order-one coupling exists in the row.
- Test (g3) of row 1553. The failing line ("nonzero flux sectors carry weight at least $2d_\gamma^4$") does not fire at the gapped twin: for U(1) at $\beta<1/9$ the benchmark argument of section 6 with row 1573 L182 gives $D(\infty)\to0$, hence a vanishing flux weight. So the failure reads the law, not the algebra alone. What it reads is the flux weight (Coulomb against confined), which is check 1571's judgement on (B): "what it reads is electric-flux confinement (N-flux), not the gap or purity".
- Every PROVED item is non-selective. Theorem (1), (5), (7), (9), (10), (11) and the benchmark hold, with the obvious changes of constants, for weak 4D U(1) and for 5D SU(2). The row says so for (4), (9), (11) at L188. This is the pattern of row 1386 Proposition NEG: identities, lattice-local estimates and a negative.
- The next component is not placed where either comparison fails. The row puts both failures at the endpoint and says the interval from $1/4$ to $T_*$ "is the step for which I have no four-dimensional estimate" (L190). ARGUED by me, not proved: on $[0,1/4]$ a flux-carrying network has join weight at most $(I_1/I_0)^n\le8^{-n}$ in U(1), so the mechanism that kills U(1) at the endpoint is damped there, and I expect the fixed-interval bound to hold or fail alike in the gapless comparisons. A neutral spectator leaves the Wilson factor of the fixed-interval quantity unchanged.

Verdict: target (6) is selective only through its endpoint, where it inherits the seed's selectivity (neutral part) and the selectivity of (N-flux) (flux part). The row supplies no selective step and no selective component. It does not claim one ("This calculation establishes no dimension-selective infrared estimate", L188).

### 7.4 The 5D item, L183-L188: HOLDS as a conditional

$e^{-D(\infty)}\le w_0(u)\le(1+e^{-uE})^{-1}$ with $uE\le(4\pi+o(1))/512$ gives a value below $2/3<225/256$. The free-pair realization is row 1573 L225, on file. The premise for the interacting model is GUESSED, as labelled.

## 8. Is (6), with the fixed-interval target and the remaining budget, equivalent to (PUR-io)?

**Answer: strictly stronger in form; proved strictly stronger on the consumer's class of positive transfer data; not known to be equivalent or strictly stronger on the Wilson trajectory. It is not an equivalent rewriting.**

- (6) implies (PUR-io) on the same side and subsequence (section 2). PROVED.
- (6) implies more. By Lemma F it forces $\kappa_K\ge15/16$ and $f_u\le31/256$, and $w_0(u)\ge225/256$, which is above the $21/25$ that the seed threshold gives. It also bounds the total variation of $t\mapsto D_K(t)$, which is at least $D_K(\infty)$, with equality only if $D_K$ is monotone. Monotonicity is not shown; I have no proof either way.
- Strictness on transfer data, two independent ways. (a) The author's example (section 3): purity tends to one and $\kappa\to0$. (b) Seven nearly degenerate charged levels (check 1550's example, used in row 1566 Step 7 L149): $P_K=1$ and $f=7/8$, so $e^{-D(\infty)}\le1/8$ by Lemma F.
- On the Wilson trajectory the converse would need (N-flux) at level 31/256 and the cap bound at the release roots, possibly on an enlarged side. Neither is on file. The enlargement chain of rows 1161/1355 (used in check 1376 S57 and in row 1602 Theorem 1B) makes $s$ small on a larger side; it says nothing about $f$ or $\kappa$.
- The decomposition into the fixed interval and the budget from $1/4$ to $T_*$ changes none of this: the three pieces of the integral are jointly sufficient and no piece alone has a consumer.

**Does the route escape the two closures?**
- Rows 1602/1605 (bounded whole-slice forms at the target aspect equal the seed): **not escaped.** The endpoint is such a form. $e^{-D_K(\infty)}=\operatorname{Aff}(p_K,\phi^2\otimes\phi^2)^2(1-f_u)$, a bounded whole-slice affinity of the neutral two-slice law at the target aspect, with the reference fixed in advance, times the flux factor. Its neutral content is Lemma M1 (rows 1356/1359, Lean; row 1600 section 8 fact 2), whose best case is the seed (row 1147 (26); Lemma HS of row 1600). So the route lies on the stronger side of that closure. Any proof of (6) proves the seed with margin and an (N-flux) bound on the way.
- Rows 1603/1607 (fixed-lattice-size two-sample forms; whole-face mixing at half-periods up to $\beta_K^\alpha$): **escaped.** (6) is a whole-face statement at half-period $n/1024$. The observables in (9) and (11) are lattice-scale loops, but at separation $v$ and summed over the face. The lower bound of row 1603 (a fixed-size core, in the order $\liminf_R\liminf_K$) does not bound them.
- The fixed-interval target lies outside both closures. It is a statement about the two ends of an open slab under a weak join. ARGUED: by (11) it is a join-smoothed second-moment (unbounded, chi-square type) dependence between the two ends of a slab of thickness $v$, summed over the whole face, so it is itself a physical-scale mixing estimate, for the open slab. Row 1602 Theorem 2 places unbounded tests on the stronger side.

## 9. Inputs used and not rechecked

- Row 1375 L47-L55 (fixed-graph total-variation limit), as checked in 1376 S7-S11, given rows 1151, 1231, 1339, 1371. Read, not redone.
- Check 1453: "BND-2 puts $\beta_K\in[\beta_0,B_0\log(\ell/a_K)]$ eventually" for every fixed $\beta_0$ (L107, read). This gives the hypotheses $\beta_K\to\infty$, $\beta_K=O(\log n)$ of row 1375.
- Row 1573 (4), as checked in 1579 item 11, given Theorem E (2.15) of row 1568 as checked in 1572 Step 7. I read (4) and its proof paragraph; I did not open row 1568.
- The periodic Villain note on main (section 7.1). Not read.
- Fact PUR (row 1468 section 3.1, read) and check 1527 (ii) (located, not redone).
- GL3 (positive one-link character coefficients): standard; used as in row 1573 L210.

## 10. What is new and what is on file

| Item | Standing |
|---|---|
| Theorem (1), fixed-range trials | New. Inputs on file: row 1375 (2), (4), L47-L55, L73-L84; check 1376. Bounded greps of `library/` and `parts/` for fixed-range or Gibbs trial laws found only the unrelated excess-lane files. Row 1600 Attack 8 and row 1496 hold the verdict "extensive overlap deficit for every explicit trial" as ARGUED; this theorem proves it for one class |
| Six-piece ratio $D_K(t)$, (4)-(5), the join $J_t$ | New (greps for six pieces, free cap, joining strength: no prior construction). Row 1147 section 9 treats joining costs of open spatial boxes, a different object |
| Endpoint (7) and the consumer | The inequality is on file: Lemma M1 (rows 1356/1359, Lean) and row 1600 Attack 8, "$1+S(2w)\le\operatorname{Tr}T^{2w}/\langle\phi,T^w\phi\rangle^2$". The best product affinity $\lambda_0^h/\sqrt{\operatorname{Tr}PF^{2h}}$ is row 1147 (26). New: the reference $\phi=T^v1/\|T^v1\|$ and the partition-function form $G(3v)^2/(G(2v)^2\operatorname{Tr}T^{2v})$ |
| Strictness example | New instance (cap overlap). The pattern is on file: check 1527 (vi), row 1573 L117-L123 |
| (9) | New |
| (10) | New, elementary |
| (11) and the spin weights | New identity. The simple-loop eigenvalue is on file (soft route, row 531 digest) |
| Benchmark at $\beta<2/9$ | New conclusion for this quantity. Input and pattern on file: row 1573 (4), L182 |
| U(1) endpoint | On file in substance: row 1573 L131-L150 with check 1579 item 9. New: one line applying it to (7) |
| 5D conditional | On file: row 1573 L225 |
| Lemma F and the flux demand (this check) | One line. (N-flux) and "purity does not imply (N-flux)" are on file: row 1566 Step 5 and Step 7, check 1570, check 1571 |

## 11. Remarks on the row's wording (none breaks a proof)

1. L101-L108 should say that the trace in (7) is unprojected, and that (6) therefore forces $f_u\le31/256$. The row mentions "the electric sectors missed by the cap" only at L190.
2. L173, "including multiplicities and charged sectors": the space is the gauge-invariant one, so "charged" can only mean centre flux.
3. L190, "first component of a method": the fixed-interval target is ARGUED, has no proof step, and by the row's own account is followed by an interval with no estimate. The proved components are the consumer, the two end estimates in $t$, the benchmark and the negative (1).
4. A repair worth one line, unproved suggestion: put $P_0$ in the ring of arrangement A, $\operatorname{Tr}(P_0SJ_tSJ_t)=\tfrac18\sum_z\operatorname{Tr}(C_zSJ_tSJ_t)$, a positive mixture of eight twisted Wilson integrals. The endpoint becomes $\kappa_K^2w_0(u)$ and the flux demand drops out. The U(1) failure through $Z_{\rm even}$ survives unchanged. (5) becomes a difference of plaquette means in a twist mixture. I did not check (9)-(11) in that form.

## 12. Guide run (float, not a proof step)

One inline numpy process, a 9-dimensional random positive matrix in place of $S$, no file written. It agrees with the hand results: $D(\epsilon)/\epsilon^2\to\sum C_{pq}^2$ (0.23392 at $\epsilon=10^{-3}$ against 0.23402), identity (11) to 15 digits, and the Gaussian trace $\sqrt{1-r^2}$ (0.8002 against 0.8 at $r=0.6$, Monte Carlo). The verdicts above rest on the hand derivations only.

RESULT — Row 1611 (`gap-direction7-astra62.md`, gpt-6.2-astra max) checked line by line by hand by Claude Fable 5.2 (row 1612; cross-provider; a check, not an audit; one float guide, no Lean).
Every PROVED item HOLDS, no failing line: the fixed-range trial theorem (1) (given rows 1375/1376 and check 1453); the consumer (6) to (7) to $P_K\ge(15/16)^4>457/625$; strictness on a positive transfer class; the coefficient (9) (re-derived a second way); the tail (10); the identity (11) with its spin weights; the benchmark at $0<\beta<2/9$ (given row 1573 (4)).
The U(1) endpoint failure HOLDS given the periodic Villain note behind rows 1565/1571, whose internal proofs remain unchecked. The 5D item HOLDS as a conditional on a GUESSED excitation.
New in this check, Lemma F: $e^{-D_K(\infty)}=\kappa_K^2\,w_0(u)\,(1-f_u)$, cap ratio times neutral vacuum weight times one minus the flux-charged fraction. So (6) forces $f_u\le31/256$, an (N-flux) bound (row 1566, open), and $\kappa_K\ge15/16$, besides the seed.
For 4D SU(2) the U(1) argument neither fails nor passes on file: it passes exactly if the seven odd flux sectors are that small. In the neutral sector the U(1)/SU(2) difference is the centre, which is algebra (Lemma ALG).
Equivalence: (6) is strictly stronger than (PUR-io) on positive transfer data (two examples: cap, and seven charged levels); on the Wilson trajectory neither equivalence nor strictness is known. It does not escape rows 1602/1605 (its endpoint is a bounded whole-slice affinity with a fixed reference, on the stronger side); it does escape rows 1603/1607.
Selectivity: none supplied. Every proved step also holds for weak 4D U(1) and 5D SU(2); the target fails there only through its endpoint, that is, through the seed's own content and (N-flux). The fixed-interval target is ARGUED, has no consumer alone, and is not where the comparisons fail.
Outcome (d): holds in the letter (correct proved components, next component named). It moves no input: no estimate at order-one coupling, a target stronger than the seed, no selective step. New: (1), the six-piece ratio with the free-cap reference, (9), (10), (11), the benchmark. On file: the consumer inequality (Lemma M1; row 1147 (26)), the U(1) and 5D comparisons (row 1573), (N-flux) (row 1566).
Open: (6), the fixed-interval bound, (N-flux), (PUR-io), the gap.
