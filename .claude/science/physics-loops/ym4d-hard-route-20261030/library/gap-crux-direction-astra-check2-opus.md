lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T01:49Z

# Check of row 1461, Steps 3-6 (completion of check 1462)

Row 1465. Provenance: Claude Opus 5.5, high effort, commit 1a6b0188b, Mac mini worker 2, started 2026-11-24T13:49Z (date -u). Not an audit. Cross-provider check of `library/gap-crux-direction-astra62.md` (gpt-6.2-astra max). Steps 1-2 were checked by row 1462 (`library/gap-crux-direction-astra-check-opus.md`) and are not redone.

Credit: Balaban; Ethan Sussman and Levent Alpoge (complete account and YM4 Lean release, written with Claude and Codex).

## Plan

1. Read row 1461's Steps 3-6 and check 1462's stopping point.
2. Step 3: -R_K' = kappa_K; real analyticity, isolated critical points; change of variables at last roots and the derivative sign; measure argument for limsup of G_K; choice of r; use of the first lemma; Stieltjes identity (6) with F_K.
3. Step 4: reciprocal-slope bound, Fatou step.
4. Step 5: obstructions (R_K(0)=R_K(inf)=0; centre-neutral two-state factor, P_K -> 1/2); constants 457/625 => s_K(t) <= 4/21; deficit 168/625; (21,2,2)/25 example.
5. Step 6: log-purity derivative and its plaquette count.
6. Is (6) strictly weaker than (M-neutral-all) usefully, or only formally?
7. Verdict last.

## Status of check 1462 at this commit

At commit 1a6b0188b, `library/gap-crux-direction-astra-check-opus.md` (check 1462) is no longer cut off after Step 2. It holds Steps 3-6 and a verdict (HOLDS AFTER CORRECTION, R1-R3), finished 13:36Z. This row was queued at 13:38Z, so the brief saw an earlier relay copy. This row is a **second reading by the same model family (Claude Opus 5.5 high). It is not an independent check** in the sense of the working rules. To add something, I redo each step by my own route where one exists: the 457/625 bound through the function $f(s)=(1+s^2)/(1+s)^2$ and not through $p_0$ as in `gap-seed5-astra62.md` line 25, the change of variables through the pushforward measure, and the release normalization read directly from `Challenge.lean`. Where my reading differs from check 1462, I say so.

## Source facts used (read directly, release 3932084a9b82, `Challenge.lean` lines 81-123, local read-only copy, not built)

- `law G N β` has density $\exp(-\beta\,\mathrm{action})/Z$ with respect to product Haar. `action` $=\sum_{p}(1-\tfrac12\mathrm{Re\,tr}\,U_p)$ over all faces of the torus, and each term lies in $[0,2]$. So $A_{\rm ref}$ in (3) is exactly the release's `action` on the reference torus (`siteCount L M K`), and $\beta$ enters with coefficient exactly $-1$. **This makes $-R_K'=\kappa_K$ an identity with constant 1.** That matters because (4) is compared with $168/625$: if the weight had been $e^{-c\beta A}$, (4) would equal $c^{-1}$ times (5), and the threshold would move.
- `referenceResponse` $=$ `centeredMoment` of `![bump, translatedBump]`, i.e. $R_K=\mathrm{Cov}_\beta(X,Y)$ with $X,Y$ the two smears. `bump x = smoothTransition(2 - Σ ((80/3) x_i)^2)` is nonnegative and supported in $|x|<3\sqrt2/80\approx0.053$. `translatedBump` is shifted by $3e_0$.
- `couplingsAt` is the set $\{g>0:R_K(g^{-2})=\texttt{fixedPhysicalLevel}(g_0)\}$, and `bareCoupling` is its `sInf`. So the release's least root $g$ is the note's **largest** root $\beta=g^{-2}$, which is what the note calls the last root. `fixedPhysicalLevel` $=c_{\rm ref}g_0^4$ with $c_{\rm ref}=(9/\pi^4)\iint \mathrm{bump}\cdot\mathrm{translatedBump}/|x-y|^8>0$ (lieDim $=3$).
- The side of the reference torus is `physicalSide L M` $=2L^M$, which is even. The centres $0$ and $3e_0$ differ by an odd number along $e_0$, so modulo the period they are at distance at least 1. The supports have radius $<0.054$. So for late $K$ no link lies in a plaquette of both smears, whatever $L,M$ are. At $\beta=0$ the law is product Haar, so $X,Y$ are independent and $R_K(0)=0$. This confirms the note and check 1462. The note's "side at least eight" is not needed.

## Step 3. From (4) or (6) to a gapped calibrated limit

**Verdict (3): HOLDS.** Redone by hand. I agree with check 1462 except on R1, which I read as a clarification and not as a needed repair (see below).

1. **$-R_K'=\kappa_K$.** With $\frac{d}{d\beta}\mathbb E_\beta F=-\mathrm{Cov}_\beta(F,A)$ (differentiation under a finite integral of bounded continuous integrands; $Z>0$), $R=\mathbb E XY-\mathbb EX\,\mathbb EY$ gives $R'=-\mathrm{Cov}(XY,A)+\bar y\,\mathrm{Cov}(X,A)+\bar x\,\mathrm{Cov}(Y,A)$. Expanding $\mathbb E[(X-\bar x)(Y-\bar y)(A-\bar A)]$ gives $\mathrm{Cov}(XY,A)-\bar y\,\mathrm{Cov}(X,A)-\bar x\,\mathrm{Cov}(Y,A)$. So $R'=-\kappa$, with constant 1 by the source fact above. ✓
2. **Analyticity, finitely many critical points.** $Z(\beta)$ and the numerators are entire in $\beta$, and $Z>0$ on $\mathbb R$, so $R_K$ is real analytic on all of $\mathbb R$. $R_K(0)=0$ and $R_K$ takes the value $r_+>0$ on the tail, so $R_K$ is not constant, $R_K'\not\equiv0$, and $R_K'$ has finitely many zeros in the compact window $[B^-,B^+]$. ✓
3. **Change of variables.** On each maximal decreasing piece $J$ in the window, $[\kappa]_+=-R'$ and the map $R:J\to R(J)$ is a $C^1$ bijection. So $\int_{J\cap\{r_-<R<r_+\}}\kappa(1-P)\,d\beta=\int_{R(J)\cap(r_-,r_+)}(1-P)(R|_J^{-1}(r))\,dr\ge0$, because $0\le P\le1$. Increasing pieces contribute zero. Fix $r\in I$ that is not one of the finitely many critical values and not $R(B^\pm)$, $r_\pm$. Then (2) puts $\beta_K(r)$ in the open window. $R_K<r$ on $(\beta_K(r),\infty)$, because $R_K\ne r$ there, $R_K$ is continuous and $R_K\to0<r$. With $R'(\beta_K(r))\neq0$ (non-critical value) this forces $R'(\beta_K(r))<0$. So $\beta_K(r)$ lies inside one decreasing piece, and the sum over pieces is at least $\int_I(1-P)(\beta_K(r))\,dr$. ✓
   *On R1 of check 1462.* The note's sentence begins "For every remaining $r\in I$", i.e. after the critical values were removed in the sentence before. "Simple" comes from that removal, and the sign comes from "$R_K<r$ to its right". The argument is complete as written; R1 is at most a clarity edit.
4. **Measurability.** $r\mapsto\beta_K(r)$ is nonincreasing on $I$ (the sandwich argument of (2), checked in check 1462 Step 2 and redone here: a level $r_1<r_2$ has a root to the right of the last root of $r_2$). $P_K$ is continuous for real $\beta$. So $P_K\circ\beta_K$ is Borel. ✓
5. **Selection.** Suppose $\liminf(4)<d_*=168/625$. Pick $\epsilon>0$ and an infinite set $S$ of late $K$ with $(4)\le d_*-\epsilon$. Then $(5)\le d_*-\epsilon$ on $S$. Let $B_K=\{r\in I:1-P_K(\beta_K(r))>d_*\}$. Then $d_*|B_K|\le\int_I(1-P)\le(d_*-\epsilon)|I|$, so $|G_K|=|I\setminus B_K|\ge\epsilon|I|/d_*$. The sets $U_N=\bigcup_{K\in S,K\ge N}G_K$ decrease, each has measure at least $\epsilon|I|/d_*$, and $|I|<\infty$. So $\limsup_{K\in S}G_K=\bigcap_NU_N$ has measure at least $\epsilon|I|/d_*>0$. ✓
6. **One level, then the first lemma.** Take $r\in\limsup G_K$ with $r\in(r_-,r_+)$. Set $g_0=(r/c_{\rm ref})^{1/4}\in(0,\delta)$, since $I\subset(0,c_{\rm ref}\delta^4)$. At infinitely many $K$ one has $P_K(\beta_K(r))\ge457/625$, hence $s_K(t)\le4/21$ with $t=2\lfloor n/1024\rfloor$, which is the seed at $w=\lfloor n/1024\rfloor$ (Step 5 below). The side is $n=\ell b^K$ in the units of level $r$, which are the units the first lemma uses. The release's `IsLeast` tail for this $g_0$ is cofinite, so infinitely many of these $K$ are least-root depths, and the first lemma applies to that infinite set. The level is chosen by the argument, and a prescribed $g_0$ is not reached; the note says so. ✓
7. **Stieltjes identity (6).** Redone. Put $M(u)=\max_{[u,B^+]}R_K$. For $r\in I$ with $r<M(u)$, some $v\ge u$ has $R_K(v)>r$, and $R_K\to0<r$ gives a root above $v$, so $\beta_K(r)>u$. For $r>M(u)$: on $[u,B^+]$, $R_K\le M(u)<r$. On $(B^+,\infty)$, $R_K<r_-\le r$, because $\beta_K(r_-)\le B^+$ by (2) and $R_K<r_-$ to the right of that last root. So $\beta_K(r)<u$. Hence $F_K(u)=|\{r\in I:\beta_K(r)>u\}|$ (the single value $r=M(u)$ is null), which is the tail function of the pushforward $\mu_K=(\beta_K)_\#(dr|_I)$. A finite Borel measure on $[B^-,B^+]$ is determined by its tail function, so $-dF_K=\mu_K$ and $\int(1-P)\,d\mu_K=\int_I(1-P)(\beta_K(r))\,dr$. So (6) $=$ (5) exactly, $L_K\in[0,1]$. Also $F_K(B^-)=|I|$, because $M(B^-)\ge R(\beta_K(r_+))=r_+$, and $F_K(B^+)=0$, because $R(B^+)\le r_-$. ✓

**Consequence to record (not a defect).** (4) $\ge$ (5) $=$ (6) for every late $K$. So (4) is never easier than (6), and the remark "needs no root finder in the integrand" is a gain in form only: the measure $-dF_K$ in (6) is carried by the last crossings and encodes the roots.

## Step 4. The reciprocal-slope bound and the Fatou step

**Verdict (4): HOLDS.** Redone by hand, by a route different from the note's.

- **Differentiability at non-critical levels.** Fix such an $r$ and $\epsilon>0$. The supremum $\sup_{v\ge\beta_K(r)+\epsilon}R_K(v)$ is $<r$: on a compact stretch it is a maximum of values $<r$, and beyond it $R_K$ is small. Near $\beta_K(r)$, $R_K$ is strictly decreasing. So for $r'$ close to $r$ the last root of $r'$ is the local inverse branch, and $\beta_K'(r)=1/R_K'(\beta_K(r))=-1/\kappa_K(\beta_K(r))$.
- **Bound.** For a monotone function, $\int_I|\beta_K'|\le\beta_K(r_-)-\beta_K(r_+)$ (Lebesgue). This is at most $2C_I$ by (2). So $\int_I dr/\kappa_K(\beta_K(r))\le2C_I$ for each $K\ge K_I$. The note's route measures the set of last-crossing points in $\beta$, which lies in $[\beta_K(r_+),\beta_K(r_-)]$. That is the same inequality by the area formula. ✓
- **Chebyshev and Fatou.** $|\{r:\kappa_K(\beta_K(r))\le\eta\}|\le\eta\int_I1/\kappa\le2C_I\eta$. By Fatou, $\int_I\liminf_K\kappa_K(\beta_K(r))^{-1}dr\le2C_I$, and $\liminf_K\kappa_K^{-1}=(\limsup_K\kappa_K)^{-1}$ in $[0,\infty]$. So $\limsup_K\kappa_K(\beta_K(r))>0$ for a.e. $r$. ✓
- **Combination with (4).** On the set $S$ of Step 3.5, $|G_K\cap\{\kappa_K(\beta_K)\ge\eta\}|\ge\epsilon|I|/d_*-2C_I\eta$. That is positive once $\eta<\epsilon|I|/(2C_Id_*)$, and the limsup argument of Step 3.5 repeats. ✓

**What the bound does not give (recorded for the open estimate).** It is a *lower* bound on $\kappa$ at last roots. To pass from a statement in $\beta$-measure (for example "$1-P_K\le d$ except on a set $E_K$ of $\beta$-length $\le\eta$") to (6), one needs an *upper* bound: $L_K\le d+|I|^{-1}\mu_K(E_K)\le d+|I|^{-1}\eta\sup_{E_K\cap\{\text{last crossings}\}}\kappa_K$. No upper bound on $\kappa_K$ at last roots is on file. A priori $\kappa_K$ is a third cumulant that includes the whole reference action, whose variance grows with the number of plaquettes. So an estimate for $P_K$ that holds for most $\beta$ in the window does not give (6) without that extra input.

## Step 5. Obstructions and constants

**Verdict (5): HOLDS.** Redone by hand.

- **457/625 ⇒ $s_K(t)\le4/21$.** Here $t$ is even, so $p_i=(\lambda_i/\lambda_0)^t\in[0,1]$ for any real spectrum with $|\lambda_i|\le\lambda_0$. Write $P=Z_{2t}/Z_t^2=(1+\sum p_i^2)/(1+s)^2$. If $s\le1$: $\sum p_i^2\le s^2$, and $f(s)=(1+s^2)/(1+s)^2$ has $f'(s)=2(s-1)/(1+s)^3\le0$, so $P\le f(s)$ and $f(4/21)=\frac{457/441}{625/441}=457/625$. If $s>1$: $\sum p_i^2\le s$, so $P\le1/(1+s)<1/2$. So $P\ge457/625$ forces $s\le4/21$. This derivation is independent of `gap-seed5-astra62.md` line 25, which argues through $p_0\le1/2$ or $P\le p_0^2+(1-p_0)^2$; both give the same constant. $1-457/625=168/625$. ✓ Converse direction (for Step 6): $P\ge1/(1+s)^2$, so $s\le\sqrt{625/457}-1=0.16947\ldots$ implies $P\ge457/625$.
- **HS form of the seed (read, recomputed).** $\min_c\|c^{-1}D-e_0e_0^{\!\top}\|_{\rm HS}^2$ with $D=\mathrm{diag}(\lambda_i^w)$ equals $s(2w)/(1+s(2w))$. This is $\le4/25$ iff $s(2w)\le4/21$. This matches `gap-mini-mneutral-fable.md` line 109. ✓
- **$(21,2,2)/25$.** $s=2/21+2/21=4/21$ (the seed holds, with equality allowed), and $P=(441+4+4)/625=449/625<457/625$, so $1-P=176/625>168/625$. ✓
- **Signed endpoint cancellation.** $R_K(0)=0$ (source fact above), $R_K(\infty)=0$ (check 1462 Step 2, redone there). With $\Phi(u)=\min(\max(u-r_-,0),|I|)$ (Lipschitz) and $R$ of class $C^1$, $\int_0^\infty\mathbf1_I(R)(-R')\,d\beta=\Phi(R(0))-\Phi(R(\infty))=0$, while the descending variation inside $I$ is at least $|I|$. ✓ So a signed weight in place of $[\kappa]_+$ would cancel exactly the descents that carry the last roots.
- **Two-state factor.** Take $Q=\begin{pmatrix}a&b\\b&a\end{pmatrix}$ with $a=(1+u)/2$, $b=(1-u)/2$: eigenvalues $1,u$, entries positive. Neutral traces multiply by $1+u^{m}$, so $P$ is multiplied by $(1+u^{2t})/(1+u^t)^2$. With $u=e^{-1/n^2}$ and $t\le n/512$, $u^t\ge e^{-1/(512n)}\to1$, so the factor tends to $1/2$, and $\liminf(5)\ge1/2>168/625$. The reference law is unchanged. ✓ Scope, as check 1462 says: this shows that reference-flow facts plus transfer positivity cannot give (4). It is not a statement about the Wilson model.
- **Log-purity derivative and plaquette count.** Write $Z_u^0=\frac18\sum_zZ_u^{(z)}$, with each $Z_u^{(z)}=\int e^{-\beta A_u^{(z)}}>0$, where the twisted plaquettes have terms $1\pm\frac12\mathrm{tr}\in[0,2]$ (taken from rows 1356/1373, read only). Then $(\log Z_u^0)'=-\langle A_u\rangle_{u,0}$ in the mixture with weights $\propto Z_u^{(z)}$, and $(\log P)'=2\langle A_t\rangle-\langle A_{2t}\rangle$. ✓ An $n^3\times u$ periodic lattice has $\binom42=6$ plaquettes per site, $6un^3$ in all. So $0\le\langle A_u\rangle\le12un^3$, both $2\langle A_t\rangle$ and $\langle A_{2t}\rangle$ lie in $[0,24tn^3]$, and $|(\log P)'|\le24tn^3$. ✓ A mesh $\eta/(24tn^3)$ over a window of width $2C_I$ needs $48C_Itn^3/\eta\sim n^4$ points, since $t\sim n/512$. ✓ The note's conclusion (no strict bound from the action range alone) is right.

## Step 6. Log-purity derivative and plaquette count

Checked in the last bullet of Step 5: the formula $(\log P_K)'=2\langle A_t\rangle_{t,0}-\langle A_{2t}\rangle_{2t,0}$, the count of $6un^3$ plaquettes, the bound $24tn^3$, and the $n^4$ growth of the mesh. **Verdict (6): HOLDS.** One note: $P_K$ does not depend on the additive normalization of the action. Replacing $1-\frac12\mathrm{tr}$ by $-\frac12\mathrm{tr}$ multiplies $Z_u$ by $e^{6un^3\beta}$, and that factor cancels in $Z_{2t}/Z_t^2$. So the formula holds in either convention.

## Step 7. Is (6) weaker than (M-neutral-all) in a way a proof could use?

Notation, at fixed release witnesses $b,M,\delta$ and fixed side $\ell\in4\mathbb N_{>0}$:

- (M-all; $g_0$) is (M-neutral-all) of check 1453: the seed $s_K(t_K)\le4/21$ at $\beta_K(g_0)$ for **all** late $K$.
- (M-io; $g_0$) is the seed at $\beta_K(g_0)$ for **infinitely many** least-root depths $K$. Row 1450 line 93 states this on the extracted sequence, and the first lemma of row 1461 (checked by 1462) makes it sufficient on any infinite set of depths.
- (M-io∃) is $\exists g_0\in(0,\delta)$ with (M-io; $g_0$).
- (6<) is $\liminf_KL_K<168/625$ for some compact $I\subset(0,c_{\rm ref}\delta^4)$.

Since the Wilson model is one fixed model, "strictly weaker" can only mean that the implication fails in a class of models that shares every property the proofs use: positive neutral transfer operators and the release's reference flow. The toy models of Step 5 belong to that class.

1. **(6<) ⇒ (M-io∃).** This is Step 3. Strict: the $(21,2,2)/25$ spectrum at every level satisfies (M-all; $g_0$) for every $g_0$, and so also (M-io∃). But it has $L_K=176/625$ for all $K$, so (6<) fails.
2. **(M-all; $g_0$) ⇏ (6<).** The same example. It also fails if (M-all) holds at a single level only, since (6) averages over a set of levels of positive length.
3. **(6<) ⇏ (M-all; $g_0$)** for any prescribed $g_0$. Toy: at every level, $s_K=0$ (purity 1) at even $K$ and $s_K=1$ (purity at most $1/2$) at odd $K$. Then $L_K=0$ at even $K$, so (6<) holds, and the seed fails at every odd $K$ at every level.
4. **What does imply (6<).** Suppose (M-all) holds with a margin at almost every level of $I$: $\limsup_Ks_K(t_K)$ at $\beta_K(r)$ is at most $\sigma(r)$, with $|I|^{-1}\int_I[1-(1+\sigma(r))^{-2}]\,dr<168/625$. Then (6<) holds, by $P\ge(1+s)^{-2}$ and reverse Fatou (the integrand is bounded by 1). A uniform margin $\sigma<\sqrt{625/457}-1=0.16947$ suffices.

**Answer. Only formally weaker, and in quantifiers only.** (6<) is incomparable with (M-all; $g_0$). Against it, (6<) relaxes three quantifiers: the cutoffs (infinitely many instead of all late), the level (existential instead of prescribed), and the level average. It tightens the test from $s\le4/21=0.1905$ to $P\ge457/625$, which lies between $s\le0.1695$ and $s\le0.1905$. The useful relaxation of the cutoff and level quantifiers already comes from the first lemma: (M-io∃) is sufficient on its own, and (6<) is **strictly stronger** than (M-io∃) (item 1). So (6<) gives a proof something beyond (M-io∃) only if the proof's natural output is an $L^1$ bound over levels of the purity deficit at last roots. I found no such method on file (grep of `open-core.md` and the FINISH rows for infinitely-often or level-averaged seed forms: only row 1450 line 93 and row 1461 itself). Step 4 shows that a bound holding for most $\beta$ in the window does not convert to (6) without an upper bound on $\kappa_K$ at last roots, which is also open. So (6) does not move the wall named in row 1461 Phase 2: one still has to bound the neutral multiplicity on a fixed physical side at calibrated couplings, at one level, along an infinite set of cutoffs. By the lead rule of 2026-11-22, (6<) is not equivalent to (M-all), but its gain over the already sufficient (M-io∃) is nil. A lane should target (M-io; $g_0$) or (M-io∃) directly, with the $P$-test as one way to certify a single cutoff.

## Defects and repairs (Steps 3-6), ranked

None breaks a statement. All three are wording only.

- **N1** (note line 142): "side at least eight" is not needed and is not shown from the release. Disjointness holds for every $L,M$, because the period $2L^M$ is even and the offset 3 is odd.
- **N2** (note line 123, "needs no root finder in the integrand"): true of (4) as written, but (4) $\ge$ (5) $=$ (6), so the form gives no analytic saving. The measure in (6) is carried by the last crossings.
- **N3** (on check 1462 R1): the note's sentence at line 125 is complete when read with "remaining"; R1 is optional.

## Verdict

**HOLDS** for Steps 3-6 of row 1461, checked line by line by hand (Claude Opus 5.5 high). The first failing step: none. With check 1462's wording repairs R2 and R3 for Steps 1-2, the note as a whole **HOLDS AFTER CORRECTION** (R2, R3; optionally R1, N1, N2).

Established, as hand proofs checked here: $-R_K'=\kappa_K$ with constant 1 in the release's normalization; (4) $\ge$ (5) $=$ (6) for each late $K$; $\liminf$ (4) or (6) $<168/625$ gives a calibrated gapped limit at some level chosen by the argument, with $m_{\rm phys}\ge(2/\ell)\log(2^{18}/5041)$ (rate from Step 1, check 1462); the reciprocal-slope bound $\int_Idr/\kappa_K(\beta_K(r))\le2C_I$ and $\limsup_K\kappa_K(\beta_K(r))>0$ for a.e. level; $P\ge457/625\Rightarrow s\le4/21$ and the threshold $168/625$; the $(21,2,2)/25$ example; $R_K(0)=R_K(\infty)=0$ and the signed cancellation; the two-state factor $\to1/2$; the log-purity derivative and the bound $24tn^3$.

Read only, not redone: rows 1356/1373 (neutral trace as the mean of eight twisted Wilson integrals, positivity), row 1450 (gap implication), check 1453 (BND, BND-2). Nothing was built or run, and no numerics were done.

Step 7: (6) is incomparable with (M-neutral-all). It is weaker only in quantifiers, and strictly stronger than the infinitely-often form (M-io∃), which the first lemma already makes sufficient. So (6) adds nothing a proof could use, unless the proof naturally yields level-averaged bounds on the purity deficit; none is on file. Open: (4)/(6) itself, (M-io∃), the seed, (M-neutral-all), and a gap at a prescribed $g_0$. A further open input surfaced here: an upper bound on $\kappa_K$ at last roots, needed to turn $\beta$-a.e. purity bounds into (6).

Provenance caveat: same model family as check 1462, so not independent.

Credit: Balaban (RG series behind the release's flow); Ethan Sussman and Levent Alpoge, with Claude and Codex (YM4 Lean release 3932084a9b82, `Challenge.lean` definitions read here, and the complete account); gpt-6.2-astra (row 1461); check 1462.

Finished 2026-11-24T13:55Z (date -u).
