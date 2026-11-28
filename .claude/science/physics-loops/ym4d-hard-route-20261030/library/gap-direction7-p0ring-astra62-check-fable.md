# Check of row 1616 (`library/gap-direction7-p0ring-astra62.md`), FINISH.md row 1620

Checker: Claude Fable 5.2 (single reader, line by line). File under check written by gpt-6.2-astra max.
Status: COMPLETE. Every PROVED item HOLDS; two wording corrections (section 13, items 1 and 2). One line-by-line reading; this is a check, not an audit. Date 2026-11-27.

## 0. Method

Read in full so far: the target (209 lines; line numbers L below are lines of the target), the row 1616 brief in FINISH.md, row 1611 (`gap-direction7-astra62.md`), check 1612 (`gap-direction7-astra62-check-fable.md`), row 1614 (`gap-wmix-fixint-astra62.md`). Further sources are named where used. Not read, as instructed: every `gap-vir-down*` file. Every algebraic step is redone by hand; any float run is a guide only.

Also read: FINISH.md row 1614 RESULT; row 1573 L70, L131-L150, (4), L182, L225 (`gap-band-neutral-astra62.md`); row 1553 sections 1.3-1.5 (`gap-mech-direction4-fable.md`, Lemma ALG and tests (g1)-(g6)); check 1605 Steps 0, 2, 6 and RESULT (`gap-wmix-solve-neon-check-opus.md`); row 1147 (26) (`gap-solve3-astra62.md` L303-L312); row 1600 Lemma HS (`gap-wmix-solve-fable.md` L28-L40); row 860 Proposition P1 (`gap-hs-max.md` L168).

Convention (as in check 1612 section 0): $T$ is the gauge-averaged cylinder kernel with half-weight end magnetic actions, so $S=T^v$ is invariant under separate vertex gauges at its two ends. $C_z$ multiplies by $-1$ the links that cross one coordinate plane. $w_p(C_zX)=w_p(X)$ for every plaquette.

**Standing of row 1614 (matters for item (I')).** FINISH.md row 1614 RESULT reads: "STOPPED by the lead at 16:18:28Z ... Partial file pushed by the runner at 474e31c8f (unchecked, not to be cited)". The target cites that file as "ON FILE" in four places (L5, L134, L161, L173). No PROVED item except (I') uses it. I read the file in full; my reading of the three inputs that (I') uses is in section 7.

## 1. (5+), (6+), (7+) and the budget identity, L15-L53: HOLD

- **L22, replacement of $S$ by $S_+$.** $J_t(C_zX,C_zY)=J_t(X,Y)$ because the two signs on a dressed link $X_e^{-1}g_iY_eg_j^{-1}$ cancel. So $J$ commutes with $C_z$ and with $P$. $S$ commutes with $C_z$. $P1=1$. Hence $\operatorname{Tr}(PSJSJ)=\operatorname{Tr}(S_+JS_+J)$, and each open chain is unchanged when $S$ is replaced by $S_+=PSP$. The kernel of $S_+$ is $2^{-3}\sum_zS(x,C_zy)\ge0$. HOLDS.
- **L22, mixture.** $\operatorname{Tr}(C_zSJSJ)=\int S(C_z^{-1}x_1,x_2)J(x_2,x_3)S(x_3,x_4)J(x_4,x_1)$ is a positive integral; $R_0$ is the mean of the eight. $(\log R_0)'=\sum_z(R_z/\sum_{z'}R_{z'})(\log R_z)'$, a mixture expectation. With the flip on a slab end the four joins are ordinary. HOLDS.
- **L24-L26, derivative and $t=0$.** A has $2+1+1$ joins, B has $2+2$; the four terms $|E|z'/z$ cancel. $R_0(0)=\langle1,S1\rangle\langle1,PS1\rangle=G(v)^2$; both arrangements equal $G(v)^6$. $D_0(0)=0$. HOLDS.
- **L33-L42, (7+).** $J_t\to I$ strongly on gauge invariants and $\|J_t\|\le1$ (check 1612 section 2); $S$ is Hilbert-Schmidt, so $\operatorname{Tr}(PSJ_tSJ_t)\to\operatorname{Tr}(PS^2)=Z_+(2v)=Z_+(u)$. The open factors tend to $G(2v)$, $G(3v)$. So $e^{-D_0(\infty)/2}=G(3v)/(G(2v)\sqrt{Z_+(u)})=\langle\phi,S\phi\rangle/\sqrt{Z_+(u)}=\kappa_K\sqrt{w_0(u)}$ (use $\lambda_0^{u/2}=\lambda_0^v$). $\phi$ is neutral with norm one, so $\langle\phi,S\phi\rangle\le\lambda_0^v$ and $0<\kappa_K\le1$. HOLDS. This is Lemma F of check 1612 with the factor $(1-f_u)$ removed, as that check predicted.
- **L42-L47, thresholds.** $D_0(\infty)=\int_0^\infty D_0'\le V_0(K)$. Under (6+): $\kappa_K^2w_0\ge225/256$, so $w_0\ge225/256$ and $\kappa_K\ge15/16$ separately, and $P_K=\sum_ip_i^2\ge w_0^2\ge(15/16)^4=50625/65536$. $50625\cdot625=31640625>29949952=457\cdot65536$. Same side $\ell$, same couplings, same subsequence. HOLDS.
- **L49-L53, budget.** $|a|=a+2(-a)_+$ gives $V_0=D_0(\infty)+2N_0=-\log(\kappa_K^2w_0)+2N_0$. So (6+) is exactly $\kappa_K^2\,w_0(u)\,e^{-2N_0(K)}\ge225/256$. $V_0<\infty$ at each cutoff by $|D_0'|\le8\cdot3n^3$ and (10+). HOLDS.

So the suggestion of check 1612 section 11(4) is decided: with $P_0$ in the ring the flux fraction $f_u$ leaves the consumer, and the consumer still implies (PUR-io) on the same side.

## 2. (11+), (9+), (W), (10+), L57-L91: HOLD

- **(11+).** $C\ge0$ (Cauchy-Schwarz for $B\ge0$, $\langle1,B1\rangle=1$). $\rho=B1$ is neutral, so $C$ commutes with $P$. $J^{1/2}1=1$ gives $\langle1,x\rangle=1$, $s\ge1$. $x$ is neutral, so $z=\langle e,J^{1/2}CJ^{1/2}e\rangle$ is the unprojected $z$. $M_+=A_++|x\rangle\langle x|$. Ring$/G(v)^2=\operatorname{Tr}(PBJBJ)=\operatorname{Tr}M_+^2=\|A_+\|_{HS}^2+2sz+s^2$; open factors $s$ and $\langle x,M_+x\rangle=s(s+z)$. So $e^{D_0}-1=(\|A_+\|_{HS}^2-z^2)/(s+z)^2\ge0$. Spin networks diagonalize $J$ and every $C_z$ together (both depend only on the edge spins), so $\|A_+\|_{HS}^2=\sum_{i,j\ \rm neutral}r_ir_j|C_{ij}|^2$. $D-D_0=\log(R/R_0)\ge0$ since $R-R_0=G(v)^2\sum_{\chi\ne1}\|A_\chi\|_{HS}^2$. HOLDS. (Float guide in section 9 agrees to 13 digits.)
- **(W).** Redone. (i) A network has an invariant at a vertex only if the number of half-integer edge ends there is even, so the half-integer edges form a mod-two cycle; its parity on a coordinate cut is the centre character (row 860 P1: $\Theta_\omega=(-1)^{N_h({\rm cut})}$) and is the same on all $n$ parallel cuts. (ii) Odd parity in direction $i$ puts at least one half-integer edge on each of the $n$ cuts; these are $n$ distinct direction-$i$ edges, so $d(\alpha)\ge n$. Equality: one spin-$1/2$ edge per cut and no other edge. Evenness at the vertices forces a common transverse position: a straight winding loop, with a unique contraction. A character odd in two directions needs $d\ge2n$. (iii) The degree-$m$ Taylor coefficient of $J_t$ is a polynomial of degree at most $m$ in the dressed links, so it is finite rank and supported on $d\le m$; a charged pair first appears at $t^n\cdot t^n$ with multiplier $(I_2/I_1)^n=(t/4)^n(1+O(t^2))$ on each $\chi_h$. $SJ_tS$ is analytic in trace norm near $t=0$, so coefficients may be taken inside the trace. (iv) $R_0(t)=G(v)^2(1+O_K(t^4))$ and both rings are even in $t$ ($n$ even). This gives (W) with error $O_K(t^{2n+2})$. The diagonal terms $\langle\chi_h,S\chi_h\rangle$ are positive because $S$ is strictly positive on gauge-invariant functions. HOLDS.
- **(9+).** The neutral nonconstant networks of least degree are the fundamental squares (degree 4); the next have degree 6. The degree-eight term of (11+) is $16\cdot4^{-8}\sum_{pq}(C^w_{pq})^2$; $z=O_K(t^8)$, $s-1=O_K(t^4)$. Also follows from (9) of row 1611 and (W), since $2n>10$. HOLDS.
- **(10+).** With the twist sum inside the kernel, the extra weight of one noise is $H=\sum_zH_z$, each $H_z$ a slab integral in which $R_e$ enters one end link, possibly with a sign. A sign is an isometry of the group, so $|H_z'|\le LH_z$, $|H_z''|\le(L+L^2)H_z$, and the bounds survive the positive sum. The one-link estimate of row 1611 (10) (check 1612 section 5) then applies unchanged; $8\cdot3n^3$ readings. HOLDS.

None of these items is selective. Each holds verbatim for compact U(1) with its three half-turns and in five dimensions (with $n^2\to n^3$ loops per direction and four directions in (W), and $L=4\beta$ in (10+)).

## 3. Whole-slice affinity and strictness on positive transfer data, L95-L103: HOLD

- **L95-L101.** $\int k^2=\operatorname{Tr}(S_+^2)=Z_+(u)$; $\phi=S_+1/\sqrt{G(2v)}\ge0$; $\operatorname{Aff}(p,q\otimes q)=\langle\phi,S_+\phi\rangle/\sqrt{Z_+(u)}=e^{-D_0(\infty)/2}$. The supremum over unit nonnegative vectors is $\lambda_0^v/\sqrt{Z_+(u)}=\sqrt{w_0}$ (row 1147 (26), read: "$\sup_{p,q}\int\sqrt{dQ_h\,p\,q}=\lambda_0^h/\sqrt{\operatorname{Tr}(PF^{2h})}$"). The description of check 1605 is accurate: its class (Step 6, read) has $\Phi$ one of $d_{TV}^{\rm two}$, $H_{\rm two}^2$, $\beta_{\rm mix}$, $H^2(p,m)$, $D_f$, all against the law's own marginal or its own conditional laws. HOLDS.
- **L103, strictness.** In the example of row 1611 L110 both $g$ and $h$ are functions of one contractible plaquette trace, so the range of $T$ is neutral and $P$ acts as the identity on it: $D_0=D$ on the whole path. $Z_+(j)=1+2^{-j}$, $P_K\to1$; $G(j)=c+(1-c)2^{-j}$ with $c=4\delta(1-\delta)=o(2^{-3v})$, so $\kappa_K=(1+o(1))2^{-v}\to0$. The endpoint fails while the purity tends to one, on every allowed side. HOLDS. The remark on check 1612's second example is right: seven charged levels are removed by $P$ and leave $\kappa=w_0=1$.

## 4. The weak 4D U(1) endpoint, L109-L118: HOLDS given the periodic Villain input

Sections 1-2 hold verbatim for compact U(1) with the three half-turns: the range of $P$ is $Q\in(2\mathbb Z)^3$, and (7+) reads $e^{-D_0(\infty)}=\kappa^2\lambda_0^u/Z_{\rm even}(u)$. The vacuum has $Q=0$, so $\lambda_0^u\le Z_{Q=0}(u)$. Row 1573 L146-L150 (read; aspect $n/u=512$, even tori) gives $Z_{\rm even}(u)\ge(1+2d_\gamma^4)Z_{Q=0}(u)$ with $d_\gamma^4>1/2$. So $e^{-D_0(\infty)}<1/2<225/256$. The chain is the one checked in 1579 item 9 and in check 1612 section 7.1, now without the step that dropped the odd sectors. Standing as there: Villain at each sufficiently large $\gamma$, Wilson at all sufficiently large $\beta_W$, conditional on the periodic Villain note behind rows 1565/1571, whose internal proofs neither check 1571 nor I checked. The author's label is accurate.

## 5. Fixed $\beta<2/9$, the law test, 5D, L120-L126: HOLD (given row 1573 (4)); one wording correction

- **L120-L124.** Row 1573 (4) at $d=4$, $m_G=4$: $q=9\beta/2$, $M\le18N\beta^2\sum_{r\ge v-2}(r+1)q^r$, $\delta_n=\pi^2M$. $e^{-\delta_n}f(x)f(y)\le S(x,y)\le e^{\delta_n}f(x)f(y)$ averaged over both ends gives the same bounds for $S_+$ with $f_+=Pf$. With $f_+\otimes f_+$ in all six slabs, A and B both equal $\langle f_+,J_tf_+\rangle^4\langle1,f_+\rangle^4$ and each join has the law $\propto f_+(x)J_t(x,y)f_+(y)$. Restoring the slabs changes each normalized density by a factor in $[e^{-12\delta_n},e^{12\delta_n}]$; for $|w|\le1$ each mean moves by at most $e^{12\delta_n}-1$. So $|D_0'|\le8N(e^{12\delta_n}-1)$, the integral to $T_*=(1+3\beta)^2n^4$ tends to zero, and (10+) covers the tail. HOLDS given (4) (checked in 1579 item 11, given row 1568 Theorem E as checked in 1572 Step 7; not reopened here).
- **L126, U(1) at $\beta<1/9$.** $q=9\beta$; $D_0(\infty)\le12\delta_n\to0$. HOLDS. So the failing line of section 4 does not fire at the gapped twin of the same group and dimension. This is test (g3) of row 1553 section 1.5. **Correction of wording:** the target says "as required by Lemma ALG (1553 section 1.4)". The test it has passed is (g3). Lemma ALG is the statement about properties that are constant on the SU(2) subclass; its bearing here is on the SU(2) side and is adverse (section 10).
- **L126, 5D.** $w_0\le(1+e^{-uE})^{-1}<2/3<225/256$ if $uE<\log2$. HOLDS as a conditional; the premise for the interacting model is GUESSED, as labelled (row 1573 L225, check 1612 section 7.4).

## 6. The interior excess (O), L136-L159: HOLDS

- **The kernel.** $m=n^3/4$ vertex-disjoint (hence edge-disjoint) squares; the $E_i$ are Haar-independent with probability $1/2$; $\delta=2^{-m}$. $h$ takes the values $L=\sqrt{(1-\delta)/\delta}$ on $E$ and $-1/L$ off $E$; mean zero, norm one. With $p=L/4$: $S(x,y)=1+p(h(x)+h(y))+3p^2h(x)h(y)$. On $E\times E$: $1+2pL+3p^2L^2>0$. Off, off: $1-\tfrac12+\tfrac3{16}=\tfrac{11}{16}$. Across: $1+p(L-1/L)-3p^2=p^2+\tfrac34$. $\langle1,S1\rangle=1$, $S1=\rho$, $C=2p^2|h\rangle\langle h|$. $E$ is gauge and centre invariant, so every nonzero mode is neutral and $C_+=C$.
- **The one-step transfer.** On the two-dimensional range, $S^{1/v}=dS+b\,I_2$ with $d>0$ and $b\ge0$ (a chord of a concave function with $f(0)=0$ lies above the graph to the left of both nodes). $I_2$ has the nonnegative kernel of the two indicator projections. So $T=S^{1/v}$ has a strictly positive kernel and $T^v=S$.
- **The formula.** $s=1+p^2r$ (since $\langle1,J_th\rangle=0$), $\|A_+\|_{HS}^2=4p^4r^2$, $z=2p^4r^2/s$. With $y=p^2r/s$: $e^{D_0}=1+(4y^2-4y^4)/(1+2y^2)^2=(1+8y^2)/(1+2y^2)^2$. Its maximum over $y\in[0,1]$ is $4/3$ at $y=1/2$ (derivative in $y^2$ changes sign at $1/4$). At $t=\infty$, $r=1$ and $y=p^2/(1+p^2)\to1$, so $e^{D_0(\infty)}\to1$; then $\kappa^2w_0\to1$, $w_0\to1$, $P_K\to1$. Direct check: the eigenvalues of $S$ have sum $1+3p^2$ and product $2p^2$, so their ratio tends to zero.
- **Placing the excess.** $J_t$ acts on gauge-invariant functions as the product of one-link convolutions; the squares are edge-disjoint; so $\langle1_E,J_t1_E\rangle=(h^{(1)}_t)^m$ and $p^2r=((h^{(1)}_t/a^2)^m-1)/16$. Keeping the constant and $2w_p$ (coefficient $2\int_{w>0}w>0$, eigenvalue $(I_2/I_1)^4$; all eigenvalues nonnegative) gives $h^{(1)}_t/a^2\ge1+ct^4$. At $t=(16/(cm))^{1/4}=Cn^{-3/4}$ Bernoulli gives $p^2r\ge1$; by continuity $p^2r=1$, $y=1/2$, $D_0=\log(4/3)$ at some earlier $t$. $\log(4/3)=0.2877>0.1291=2\log(16/15)$. HOLDS. (Float guide in section 9 agrees with the formula.)

Bearing. On positive transfer data $D_0$ is not monotone, and the endpoint can pass while (6+) and (I) fail. This settles, for that class, the monotonicity question left open in check 1612 section 8. The author's caveat is right: $\rho\ge3/4$ everywhere, so $\mathbb E_S(1-w_p)\ge3/4$, far from the Wilson law at $\beta_K$. Nothing follows for the Wilson trajectory.

## 7. (I'), L161-L202: HOLDS given three lemmas of row 1614 (stopped run, unchecked)

**The derivation in the target, given the inputs.** Redone line by line.
- $0\le W\le U$ ($d+d'-dd'=1-ww'\ge0$), so $0\le H_a=U-aW\le U$. The leading four-join weight is $e^{12V\lambda-\lambda H_1}$; the scalar is common to A and B.
- $F_0$ is the same function of $\lambda$ in A and B: $U$ is a sum of one-end functions, both arrangements have two slabs with two marked ends and four with one, and the slabs are independent at $t=0$. Plaquette traces are invariant under $C_z$, so their law under $S_+$ is the free-slab law.
- $\partial_\lambda F_a=-\langle H_a\rangle$, $\partial_a\partial_\lambda F_a=\langle W\rangle-\lambda\operatorname{Cov}(W,H_a)$. Correct.
- Normalizer $\ge e^{-\lambda\mathbb E_0U}\ge e^{-Cx/\beta}$ (Jensen). Tilted bad probability $\le Ce^{-cV/\beta^2+Cx/\beta}$. On the good event $W\le\frac12\sum(d^2+d'^2)\le CV/\beta^2$; everywhere $W\le CV$. With $\beta=O(\log n)$ and $x\le\beta^{5/3}$ the bad part is negligible, so $\langle W^2\rangle^{1/2}\le CV/\beta^2$.
- $\int_0^\Lambda\operatorname{Var}(H_a)\,d\lambda=\langle H_a\rangle_0-\langle H_a\rangle_\Lambda\le\mathbb E_0U\le CV/\beta$.
- Cauchy-Schwarz twice: $\int_0^\Lambda|\partial_\lambda(F_1-F_0)|\le C\Lambda V/\beta^2+(CV/\beta^2)(\Lambda^3/3)^{1/2}(CV/\beta)^{1/2}=C(x/\beta^2+x^{3/2}/\beta^{5/2})$.
- Remainder: the density ratio is in $[e^{-CVt^6},e^{CVt^6}]$; the error in the log derivative is at most $CVt^5+\lambda'(t)(e^{CVt^6}-1)\langle H_1\rangle$ with $\langle H_1\rangle\le CV/\beta$; integrated, $CV\tau^6(1+x/\beta)$, and $V\tau^6=512\,x^{3/2}/\sqrt V$.
- At $x=c_*\beta^{5/3}$: the terms are $c_*\beta^{-1/3}$, $Cc_*^{3/2}$, $o(1)$. Against row 1614 (10) ($x\le c\beta^{3/2}$) the gain in $t$ is $\beta^{(5/3-3/2)/4}=\beta^{1/24}$. Correct.
No failing line.

**The three inputs (row 1614 (2), the collar probability, (11)).** One reading each; main steps redone.
- (2): the tilt $e^{\beta d_p/4}$ halves the coupling $\kappa=\beta/2$ of one boundary plaquette. After rotating an axis of $p$ into the transfer direction, $p$ is one electric bond factor in one layer. Mass-normalized multipliers $I_{2j+1}(q)/I_1(q)$ increase in $q$, so the changed layer is below the original in operator order; $\operatorname{Tr}(F'F^{n-1})\le\operatorname{Tr}F^n$; the scalar is $z_-(\kappa/2)/z_-(\kappa)\le C_0$. I find no failing line.
- Collar: many marks give layers $0\le F_i\le F$; $|\operatorname{Tr}\prod F_i|\le\prod(\operatorname{Tr}F_i^n)^{1/n}\le\operatorname{Tr}F^n$; so $\mathbb Ee^{(\beta/4)\sum_Ad_p}\le C_0^{|A|}$, then $\mathbb Ee^{\sum d_p^2}\le(1+C/\beta^2)^V$ and exponential Markov. I find no failing line.
- (11): polymer recursion on edge sets (activity $\le(e^{|z|}-1)^{|A|}$, at most $10^{2k}$ connected sets, deletion ratios within $1/2$ of one), $|\log J|\le CV$ on a fixed disc, Cauchy from degree six. The low coefficients are those of row 1611 (checked in 1612 section 4). Standard; I did not redo the constants.
These are author-only proofs from a stopped run that FINISH.md marks "not to be cited". So the standing of (I') is: correct derivation, conditional on three lemmas that have had this one reading and no check row.

## 8. Is the projected consumer equivalent to (PUR-io)?

**Answer: strictly stronger in form; proved strictly stronger on positive transfer data; on the Wilson trajectory neither equivalence nor strictness is known.**

- Exact content (sections 1, 3): (6+) $\iff\kappa_K^2\,w_0(u)\,e^{-2N_0(K)}\ge225/256$. Three factors:
  (i) $w_0(u)\ge225/256$: the seed with margin. $\sqrt{w_0}$ is the best product affinity (row 1147 (26)); by Lemma HS of row 1600 and Theorem 1B of row 1602 (check 1605 Steps 2, 6) a threshold on it is equivalent to (PUR-io) up to a fixed enlargement of the side.
  (ii) $\kappa_K\ge15/16$: with $c_i=|\langle1,\psi_i\rangle|^2$ and $r_i=\lambda_i/\lambda_0$, $\kappa_K=\sum_ic_ir_i^{3v}/\sum_ic_ir_i^{2v}$, the mean of $r^v$ in the cap state $\phi$. It reads only states that the constant function overlaps (zero momentum, fully symmetric). $w_0$ reads all neutral states. Neither controls the other on transfer data: row 1611's example has $w_0\to1$, $\kappa\to0$; conversely (PROVED here, two lines) take $N$ neutral gauge-invariant cells of equal Haar mass, $\Pi_N$ the projection on functions constant on the cells, and $T=|1\rangle\langle1|+\epsilon(\Pi_N-|1\rangle\langle1|)$, $0<\epsilon<1$: the kernel is $1-\epsilon+\epsilon N1_{\rm same\ cell}>0$, every excited level is orthogonal to the constant, so $\kappa=1$, while $w_0(u)=(1+(N-1)\epsilon^u)^{-1}$ is as small as one likes.
  (iii) $N_0(K)$: the downward variation of $D_0$. By (O) it is not controlled by the endpoint on transfer data.
- So (6+) implies (PUR-io) (PROVED), and on positive transfer data the converse fails in two independent ways (cap: L103; variation: (O)).
- On the Wilson trajectory a converse needs (ii) and (iii) at the release roots, possibly on an enlarged side. Nothing on file bounds $\kappa_K$ or $N_0$. The enlargement chain (rows 1161/1355, 1527 Handoff) improves $w_0$ only. Strictness on the trajectory would need a Wilson box where the seed holds and (ii) or (iii) fails; none is on file. GUIDE only, not a claim: for a gapped theory $1-\kappa_K$ is a boundary-to-boundary term of the same kind as $1-w_0$ (area times $e^{-Mu}$), so I see no reason to expect (ii) to fail where the seed holds; it is an extra unproved statement.
- **Rows 1602/1605.** The projected endpoint is not one of the closed forms. That class tests the two-slice law against its own marginal or its own conditional laws. The endpoint is $\operatorname{Aff}(p,q\otimes q)=\kappa_K\sqrt{w_0}$ with the prescribed reference $q=\phi^2$: a bounded whole-slice affinity at the target aspect, equal to a closed-class quantity times $\kappa_K$. It is on the stronger side: it implies the closed forms (so the seed), and they do not imply it. The route does not escape that closure; it adds the cap to it. This is as check 1612 section 8 said for the unprojected endpoint, now without the factor $(1-f_u)$.
- By the lane rule: a proof of (6+) must prove the seed with margin on the way, plus two further statements. The projection removes one extra demand of row 1611, the flux bound. It does not make the consumer weaker than, or different in kind from, the seed.

## 9. Guide run (float, not a proof step)

One inline numpy process, dimension 12, a $\mathbb Z_2$-symmetric positive matrix for $S$ and a commuting positive $J$ with $J1=1$; no file written. Identity (11+) agrees with the direct ratio to 13 digits at three values of $t$. The formula $e^{D_0}=(1+8y^2)/(1+2y^2)^2$ agrees with the direct ratio at six $(p,t)$ pairs. The verdicts rest on the hand derivations only.

## 10. Selectivity

**10.1 What the surviving U(1) failure reads.** The failing line is "the sectors $Q=(\pm2,0,0)$ carry thermal weight at least $2d_\gamma^4$ times that of $Q=0$ at period $u=n/512$" (row 1573 L146-L150). It is a property of the weak U(1) law (reading, not a proof step: in the Coulomb phase a flux $Q$ costs an energy of order $Q^2/(\beta n)$, so its weight at period $n/512$ stays of order one). It does not fire at the gapped twin of the same group and dimension: section 5 gives $D_0(\infty)\to0$ at $\beta<1/9$, hence $Z_{\pm2}/Z_0\to0$ there. So by test (g3) of row 1553 the U(1) failure reads the law, not the algebra and not the dimension. The author's sentence at L118 is correct on this point.

**10.2 Why 4D SU(2) passes the same step.** Only because it has no such sectors. The range of $P_0$ for SU(2) is the trivial character of $\mathbb Z_2^3$; "even and nonzero" is empty because the centre is $\mathbb Z_2$. The step "no surviving flux sector carries weight" is therefore true for SU(2) at every $\beta$, on every torus and in every dimension. It is decided by the group. It holds in the product of the Wilson theory with a massless neutral factor, which has no seed. By Lemma ALG (row 1553 section 1.4) it is never an input. The U(1)/SU(2) contrast that survives the projection is thus the size of the centre, as check 1612 section 7.2 already said.

**10.3 The like-for-like comparison.** The analogue of the SU(2) projection for U(1) is the projection under the whole flat $U(1)^3$, onto $Q=0$. Then the two shifted sectors are gone (the author says so at L118; row 1573 L150 says the same) and the proof of the U(1) failure is gone with them. A failure of weak U(1) would then have to come from neutral photon levels in $w_0$. On file that is the free transverse-oscillator comparison only (row 1573), not a finite-box bound for the interacting model. So with the algebra matched, no proved U(1) failure of the projected consumer is on file.

**10.4 5D SU(2).** The projection (now over $\mathbb Z_2^4$) removes the charged trace exactly as in 4D; (5+)-(11+), (W), (10+) hold with changed counts. The step is blind to the dimension. The endpoint fails in 5D only if $w_0$ (or $\kappa$) fails, which is the conditional of L126 on a GUESSED spectrum, and is the seed's own content.

**10.5 What the projection removed.** For SU(2) the unprojected consumer contained $f_u\le31/256$, an (N-flux) bound, which is a law-reading (confinement-type) demand. The projection removes it. What remains is the seed's neutral content $w_0$, the cap $\kappa_K$ and the variation $N_0$.

**Verdict.** The U(1) failure reads the U(1) law. It gives no selective step for SU(2), because SU(2) passes that line by algebra alone, in 4D and in 5D. Every PROVED item of the row holds, with the obvious changes, for weak 4D U(1) and for 5D SU(2) (for (I') see section 11). The projected target is selective only where the seed is, through $w_0$. The row claims no more: "An affirmative selective estimate for calibrated 4D SU(2) remains open" (L126) and "It supplies no step selecting interacting 4D SU(2) over interacting weak 5D SU(2)" (L204).

## 11. Is (I') ultraviolet in kind? What reaches physical time?

**(I') is ultraviolet in kind. PROVED from its own proof:**
- It is blind to the slab depth. Its inputs are one-end plaquette moments ((2), "uniformly in $n,v$"), the one-end collar bound, and the pin-uniform expansion of one join. The two ends of a slab are coupled only through Cauchy-Schwarz. So (I') holds as stated for every depth $v\ge1$. That includes depths at which the full target is false: for $1\le v\le\lfloor\beta_K^\alpha\rfloor$, $0<\alpha<1/16$, row 1603 L107-L111 (read; checked in 1607, given row 1375 L144) gives $s(2v)\to\infty$ on the same calibrated tori, so $w_0(2v)=(1+s(2v))^{-1}\to0$ and by (7+) the endpoint of the six-piece comparison built from slabs of that depth tends to zero. An estimate that holds unchanged where the target fails cannot carry the target's content.
- It is blind to the dimension: for 5D SU(2) at large $\beta$ the same three inputs and the same algebra hold with changed constants. The step that gives the exponent $5/3$ is $1-w_pw_p'=d+d'-dd'$ with $dd'\ge0$ of size $\beta^{-2}$; this uses the product of two real characters in the SU(2) square integral (row 1611 L181), which is algebra. ARGUED, not done here: for compact U(1) the mixed term is $dd'+\sin\theta_p\sin\theta_p'$, of size $\beta^{-1}$ with no sign, and the same proof gives a smaller power of $\beta$.
- Its range is $Vt^4\le64c_*\beta_K^{5/3}$, so $t_K\to0$ like $n^{-3/4}$ up to a power of $\log n$. A range that is a power of $\beta$ fails the scale test (g5) of row 1553. The wall is the Cauchy-Schwarz term $x^{3/2}/\beta^{5/2}$, as L204 says. A variance bound for $W$ in place of the second moment would move the range by a power of $V$ at most and would still leave $t\to0$ (ARGUED).

**No estimate in the row reaches order-one physical time at the calibrated couplings.**
- (10+) is a one-link estimate, uniform in $v\ge1$, so the remark above applies to it too. (I') is uniform in $v$. Row 1614 (9), cited for the charged part, is uniform in $\beta$ and in $v\ge1$.
- (5+), (7+), (9+), (11+), (W) are identities. (7+) and (9+) name quantities at separation $v=n/1024$ ($w_0$, $\kappa_K$, $C^w_{pq}$) and bound none of them.
- The two statements that do read the period, the U(1) endpoint and the benchmark, are at a fixed weak U(1) coupling (on file) and at a fixed strong coupling $\beta<2/9$, not on the trajectory.

**What is missing.**
- Fixed interval, $t\in[\tau_K,1/4]$. Here $x=Vt^4/64$ grows to a multiple of $n^3$. Each arrangement's log partition function is of order $x$; (I) needs the difference of their derivatives to be $O(1)$ after integration. By (11+) and row 1614 (1) this is a bound on $\sum_{i,j\ \rm neutral}(r_ir_j/s^2)|C_{ij}|^2$ and on the cap term, with the signs kept, over all spin degrees. In words: the connected correlation between the two faces of the open slab at depth $v$, for sums over the whole face of local neutral networks, must be $O(1)$ and not $O(V)$. The first instance is $\sum_{p,q}(C^w_{pq})^2$ in (9+). Nothing on file bounds a correlation at separation $n/1024$ at $\beta_K$. ARGUED: this estimate is of power-counting type (a weak join couples the faces through local plaquette operators), and I expect it to hold or fail alike for the gapless comparisons, as check 1612 section 7.3 expected. If so it is not where a selective step can enter.
- From $1/4$ to $T_*=(1+3\beta_K)^2n^4$: no estimate at all. This interval contains the passage from two nearly independent faces to identified faces, hence the whole endpoint: $w_0\ge225/256$ (the seed with margin), $\kappa_K\ge15/16$, and the bound on $N_0$. A loop of length $R$ has join weight $(I_2/I_1)^{R}$, so loops of physical size enter only at $t$ of order $n$ (ARGUED).
- So the full budget needs the seed itself, a cap estimate, and a non-monotonicity bound, all at physical scale, and none is attacked.

## 12. New and on file

| Item | Standing |
|---|---|
| $P_0$ in the ring; (5+), (6+), (7+) | Suggested in check 1612 section 11(4), which predicted the endpoint $\kappa_K^2w_0$ and the surviving U(1) failure. The projected ring $R_0$, $D_0$ and "eight positive path integrals" are also in the stopped row 1614 (9). New here: the written proof and the mixture form of $D_0'$ |
| Budget identity $V_0=-\log(\kappa_K^2w_0)+2N_0$ | New, one line |
| (11+), (9+), (10+) | Rows 1611 (11), (9), (10) (checked in 1612 sections 4-6) with $P$ inserted; one line each |
| (W) | New as a leading coefficient. Centre character as cut parity: row 860 P1, check 864. The smallness of $D-D_0$ on $[0,\tau]$, $\tau<2/3$: stopped row 1614 (9), from row 785 (14) |
| Endpoint as $\operatorname{Aff}(p,q\otimes q)$; best product $\sqrt{w_0}$ | On file: check 1612 section 8; row 1147 (26); Lemma HS of row 1600 (read); Lemma M1 (rows 1356/1359, as cited in check 1612 section 10; not opened here) |
| Strictness (cap example) | On file: row 1611 L110, check 1612 section 3. New: one line, "$P$ leaves it unchanged" |
| U(1) endpoint | On file: row 1573 L131-L150, check 1579 item 9, check 1612 section 7.1. New: it survives the projection (predicted in 1612) |
| Benchmark at $\beta<2/9$; U(1) at $\beta<1/9$ | On file: row 1611 L151-L160, row 1573 (4) and L182, check 1612 sections 6, 7.3. New: both-end averaging, one line |
| 5D conditional | On file: row 1573 L225, check 1612 section 7.4 |
| (O) | New. Pattern on file: row 1573 L117-L123 (purity to one, another cost unbounded) |
| (I') | New improvement of stopped row 1614 (10)/(12) from $\beta^{3/2}$ to $\beta^{5/3}$. Method: rows 1149/1151 through row 1614 |
| Section 8 (ii) converse example, sections 10.2-10.3, 11 (this check) | A few lines each. Lemma ALG and (g3), (g5): row 1553 |

## 13. Remarks on the row's wording (none breaks a proof)

1. L5, L134, L161, L173 cite row 1614 as "ON FILE". FINISH.md marks that file as the partial output of a stopped run, "unchecked, not to be cited". (I') should be labelled "PROVED given three author-only lemmas of row 1614".
2. L126, "as required by Lemma ALG": the test passed is (g3). Lemma ALG applies to the SU(2) side and says the surviving contrast (the size of the centre) is not an input (section 10.2).
3. L118, "Their thermal weights ... are the law-dependent step": true for U(1). The row should add that SU(2) has no counterpart of this step at any coupling or dimension, so the U(1) failure is no evidence that the projected consumer is selective.
4. L167, "The gain ... is a factor proportional to $\beta_K^{1/24}$": correct, and it is a gain inside a range that shrinks like $n^{-3/4}$.
5. RESULT, "(d), a projected consumer and a partial estimate": the consumer is the seed with margin times the cap times the variation (section 8); the partial estimate is depth-blind (section 11).

## 14. Inputs used and not rechecked

- The periodic Villain note behind rows 1565/1571 (section 4). Not read.
- Row 1573 (4), as checked in 1579 item 11, given row 1568 Theorem E as checked in 1572 Step 7. Statement and proof paragraph read; row 1568 not opened.
- Check 1453: $\beta_K\to\infty$, $\beta_K=O(\log n)$ (taken as quoted in check 1612 section 9).
- Row 1614 (2), collar probability, (11): read and redone in outline (section 7); no check row exists.
- Row 785 (14) behind row 1614 (9): not opened; no PROVED item of the target uses it.
- Fact PUR and the seed-to-gap step (row 1468 section 3.1, check 1527 (ii)): as in check 1612.
- GL3 (positive one-link character coefficients) and the monotonicity of $I_{h+1}/I_h$: standard.

RESULT — Row 1616 (`gap-direction7-p0ring-astra62.md`, gpt-6.2-astra max) checked line by line by hand by Claude Fable 5.2 (row 1620; cross-provider; a check, not an audit; one float guide, no Lean).
(5+), (6+), (7+), the budget identity, (9+), (10+), (11+), (W): HOLD. With $P_0$ in the ring the endpoint is $\kappa_K^2w_0(u)$; the flux fraction is gone; (6+) gives $P_K\ge(15/16)^4>457/625$ on the same side.
Strictness on positive transfer data: HOLDS. (O): HOLDS; on such data $D_0$ is not monotone and a passing endpoint can hide an excess $\log(4/3)$ at $t\le Cn^{-3/4}$.
U(1) endpoint failure: HOLDS given the periodic Villain note (unchecked). $\beta<2/9$ benchmark and the U(1) twin at $\beta<1/9$: HOLD given row 1573 (4). 5D: HOLDS as a conditional on a GUESSED spectrum.
(I'): HOLDS given row 1614 (2), (11) and its collar bound. Correction: those are author-only lemmas of a stopped run that FINISH.md marks "not to be cited"; I read them and found no failing line. Correction: "as required by Lemma ALG" should read "test (g3)".
Selectivity: none supplied. The surviving U(1) failure reads the U(1) law (it does not fire at $\beta<1/9$), but 4D SU(2) passes that line only because the centre $\mathbb Z_2$ leaves no even nonzero sector, at every coupling and also in 5D; by Lemma ALG that is never an input. With the algebra matched (U(1) projected to $Q=0$) no proved U(1) failure is on file.
Equivalence: (6+) $\iff\kappa_K^2w_0e^{-2N_0}\ge225/256$, the seed with margin times a cap factor times a variation factor. Strictly stronger than (PUR-io) on positive transfer data (two independent ways); on the Wilson trajectory neither equivalence nor strictness is known. The endpoint is not one of the forms closed by rows 1602/1605; it is such a form times $\kappa_K$, on the stronger side.
(I') is ultraviolet in kind: blind to the slab depth (it holds at depths $\le\beta_K^\alpha$ where the target fails, row 1603) and to the dimension, with a range that is a power of $\beta_K$ and $t_K\to0$. No estimate in the row reaches order-one physical time on the trajectory. Missing: the face-to-face connected correlations of the open slab on $[\tau_K,1/4]$, and everything on $[1/4,T_*]$ (seed, cap, $N_0$).
New: the written projected consumer, the budget identity, (W), (O), (I'). On file: the suggestion and endpoint (check 1612), (9)-(11) and the benchmark (row 1611), the U(1) and 5D comparisons (row 1573), the affinity reading (rows 1147, 1600).
Overall: outcome (d) holds in the letter. Check 1612's suggestion is decided: it removes the (N-flux) demand and U(1) still fails. It moves no input: no selective step, a target at least as strong as the seed, and a partial estimate that is ultraviolet. Open: (6+), $\kappa_K$, $N_0$, the fixed interval, (PUR-io), the gap.
