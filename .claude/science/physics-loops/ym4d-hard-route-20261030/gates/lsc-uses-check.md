lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T16:33Z

# lsc-uses-check: the remaining uses of CA-II 6.3:lem-last-scale-constants against frozen library/lsc.md

Queue row 368. **Moves:** T0 tree nodes AIII-b (per-ball bound, `6.4:thm-per-ball-bound` with LSC) and AIV (`8.22:thm-volume-transfer`, which P9 ports with hypothesis H-VT(d)). CA label `6.3:lem-last-scale-constants` (CA-II 63365, statement unwritten there; "stated; proof incomplete" at CA-III 110895–110898). Frozen as Lemma LSC in `library/lsc.md`.

**Provenance.** Claude Opus 5.5, max effort, Mac mini worker, repository commit 620e5d82f. Account: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, `theorem_0_complete_account_raw_{I,II,III}.tex` at 31a47c543775, fetched by URL into a scratch folder. Line numbers are TeX lines of those files (CA-I, CA-II, CA-III). Frozen `library/lsc.md` is by Codex, refereed in `gates/lsc-gate.md` and `gates/lsc2-gate.md`. The inventory `library/uses-lrb-lsc.md` is by gpt-6.1-sol. Balaban is credited for the construction the account uses. This is one check by one model. It is not an audit and grants no status. No computer-assisted step and no numeric run.

## 1. What LSC supplies, and three facts used below

LSC (lsc.md §1, (4)–(8), (21)–(23), (29)–(31)) supplies the following at fixed $g$, with the correlation theorem's omitted-step exponent fixed at $m_J=m^J_{\mathbb T}(g)$:

- **Case A** ($K_J\ge m_J$): the last lattice is level $K'=K-b$, with $b=m_J-a\in\mathcal B(g)\subset[0,m_J]$ and $N=2L^{m_1+b}$ sites per side. The normalized bounds (5b) hold with volume $\mathsf V=N^4=L^{4b}(2L^{m_1})^4$. The constants $C_+^*$ and $C_{\rm low}^*$ are each uniform in $K,g_0,m_1,a$ and positions, and so is $E_*$. The vacuum number $E_{\rm vac}$ (endpoint $H=K$) is not bounded, and cancels only in same-run quotients (30)–(31).
- **(c), (d), (e), (29):** $C^*_n$, the Case B local count $C^B_n$, a subsequence with fixed $a$, and the per-ball constant under the original floor of (iii-b).

Three facts follow from definitions the account and lsc.md already state.

- **(F1)** LSC proves only $b\in\mathcal B(g)$. It does not prove $b$ independent of $K$: $a=K_J-K$ is a function of $g_0$, and nothing shows it is a function of $K$.
- **(F2)** In Case B there are no admissible correlation-theorem data. Such data need an omitted-step exponent $m\le K_J$ with $L^m\ge N_{\mathbb T}(g,m)$, and $m_J$ is the least $m$ with that floor (CA-II 711–714; lsc.md (2)). So in Case B no counterterm, no $\widetilde Z$ and no last-scale constant exists. LSC (d) is the only bound there.
- **(F3)** The identification "last lattice = unit lattice" ($K'=K$, $b=0$) is not admissible at small $g$. It needs omitted-step exponent $a\le a^\natural$ with $L^a\ge N_{\mathbb T}(g,a)\ge L^{11}MR_J(X)$, and $R_J(X)\ge(\log X)^r\to\infty$ while $a^\natural$ is fixed before $g$. So a use that states the stability bounds with unit-lattice volume $(2L^m)^4$ gets them from LSC only through $\mathsf V=L^{4b}(2L^m)^4$.

Notation warning. "$m$" is the physical torus exponent in 6.1, 6.2, 6.4, 8.22 and Theorem 0 (LSC's $m_1$). It is the omitted-step exponent in 6.3:rem-constant-dependence. "$m_{\mathbb T}(g)$" is the least admissible block exponent in Chapter 5 (CA-II 714, $=m_J$) but $11+m'+\log_LR(g)$ in Chapter 6 (CA-II 62860). Since $L^{m_J}\ge N_{\mathbb T}(g,m_J)\ge L^{11}MR_J(X)$, the Chapter 6 number is at most $m_J$.

## 2. Verdict per use

Each use was read in the account at the lines given. "Sum" means the use reads only $E_+^\sharp+C_{\rm low}$. Uses already checked in `gates/lsc2-gate.md` (II:63531, 63907–63920, 64272, 68364) are not repeated. LSC's internal proof parts (II:63371–63831) are lsc.md's own ported proof and are not rechecked.

**U1. `6.1:not-units-sources` (a), II:60354–60358.** Reads $0\le b\le b_*(g)$ with $b_*(g)$ free of $K$ and $m$, then only "finitely many $\mathcal N$". No partition-function bound is read. $E$ cancels in $Z(v)/Z(0)$ by the definition's own proof (II:60414–60422). **Covered after a stated ceiling:** $b_*(g):=m_J(g)$, since $\mathcal B(g)\subset[0,m_J]$. The literal "$b$ ... independent of $K$" is not proved by LSC (F1); the use reads only the bound.

**U2. `6.3:cor-volume-free-constant`, II:63836–63899; and the proof of `6.3:rem-per-ball-reading`, II:63936–63946.** Reads LSC (c) and (d) under floor (c) of II:63277. Sum, through $C^*_n=\max_{b}\Phi(E_*)$. $E_{\rm vac}$ cancels inside each run before the maximum over $b$ (lsc.md (30)–(31)). **Covered**, exactly: it is the constant $\max\{C^*_n,C^B_n\}$ of lsc.md §6.4, last sentence. The corollary's $C^B_n(n,R)$ is lsc.md's $C^B_n(R)$; both are free of $m_1,\mathsf d,K,g_0$ and positions.

**U3. `6.4:rem-unit-conversion` (2), II:64494–64565.** Reads $b\le b_*(g)$, $\max_{0\le b\le b_*}C^\infty_n(\mathsf dL^b;RL^b)$, and "b eventually constant along the subsequence of (ii-b)". Sum, through each $Q_\infty$. $E_{\rm vac}$ cancels inside each run. **Covered after stated ceilings:** $b_*(g):=m_J(g)$, and each $C^\infty_n(\mathsf dL^b;RL^b)$ evaluated at $E_+^\sharp+C_{\rm low}\le E_*$. The maximum over the integer interval $[0,m_J]$ dominates lsc.md (6)'s maximum over $\mathcal B(g)$ and is finite. Constancy of $b$ holds only after the (ii-b) subsequence is refined by LSC (e); the remark's bound does not use it. Case (1) of the remark ($K'=K$) has no admissible data at small $g$ (F3); only case (2) occurs.

**U4. `6.4:rem-complex-sources`, II:64285–64345.** Reads $Q_\infty$ (sum) and the chessboard quotient on one torus at complex weights. $E_{\rm vac}$ cancels (one torus; lsc.md (31)). Complex weights are inside the admitted class of lsc.md (13), (22). **Covered after a stated ceiling, Case A only:** the zero-free radius is at least $1/(2\mathfrak r(Q_*^n+1))$ with $Q_*:=\max_{b\in\mathcal B(g)}\exp[E_*\ell(n,RL^b)^4+2C_{\rm face}(RL^b)]$, free of $K,g_0,m_1$. "Independent of $m$" holds for $m=m_1$ at omitted-step exponent $m_J(g)$. It fails if $m$ is read as a free omitted-step exponent, since $x_{K'}$ then grows with $m$. In Case B there is no $\mathsf h''$ (F2). No statement cites this remark.

**U5. Unlabelled paragraph after `6.2:prop-cell-covariance`, II:62801–62823.** Reads $(E_+^\sharp+C_{\rm low})\ell^4$ (sum) in an orbit average on one torus. $E_{\rm vac}$ cancels. **Covered after the ceiling $E_*$, Case A**, with $m$ the physical exponent.

**U6. `8.22:not-partition-sources-cells` (b) and (5), II:140874–140933.** Reads $E_+^\sharp$ and $C_{\rm low}$ **each**, with unit-lattice volume $(2L^m)^4$ and counterterm levels $j\le K$. It also reads $\mathsf B$ free of $K,g_0,m$, $\mathsf B\ge0$, and $\mathsf B\le C_{\mathsf B}(1+\log g^{-2})$. Its normalization $\widetilde Z_m=e^{-E_m-\mathcal E_m}Z_m$, $E_m=\sum_{j<K}E^{(j)}_{\rm vac}$, is lsc.md (5a) with $H=K$. **Covered after a stated ceiling, Case A:** LSC gives the two bounds with $\mathsf V=L^{4b}(2L^m)^4$ (F3) and counterterm levels $j\le K'=K-b$. So per unit-lattice site one may take $E_+^\sharp:=\max\{C_+^*,0\}L^{4m_J(g)}$ and $C_{\rm low}:=C^*_{\rm low}L^{4m_J(g)}$, free of $K,g_0,m$. $\mathsf B\ge0$ follows as printed. **Not covered:** (i) Case B, where the correlation theorem supplies nothing on $\mathbb T_m$ (F2) and LSC gives no partition-function bound; (ii) the unit-site clause $\mathsf B\le C_{\mathsf B}(1+\log g^{-2})$. Every $b\in\mathcal B(g)$ has $b\ge m_J-a^\natural$, so the converted $\mathsf B$ is at least $(C_+^*+C^*_{\rm low})L^{-4a^\natural}(L^{11}MR_J(X))^4$. Here $C_+^*\ge A_J+B_J\log X$ with $B_J>0$ and $C^*_{\rm low}>0$, so this grows at least like $(\log g^{-2})^{4r+1}$ as $g\to0$. That clause comes from `8.8:lem-stability-exponent` (II:109859), which bounds $\mathsf B$ per **last-lattice** site, not per unit site. LSC's own $E_*$ satisfies the per-last-lattice-site form (Lemma M below).

**U7. `8.22:thm-volume-transfer`, II:141540–141852.** Reads $E_+^\sharp$ **alone** on $\mathbb T_{m'}$ (at the periodized weight) and $C_{\rm low}$ **alone** on $\mathbb T_m$ (zero source). The sum appears only after combining. **$E_{\rm vac}$ does not cancel:** two tori carry two vacuum numbers. The residue $\ell^4(E_{m'}/(2L^{m'})^4-E_m/(2L^m)^4)$ is bounded by `8.22:lem-vacuum-energy-density` (assumption (f); P9's H-VT(f)), an input outside LSC. LSC's convention matches it: endpoint $H=K$ on both tori, the same $K$, and the same $b$, since $a$ depends on $g_0,g$ only. **Covered after a stated ceiling, Case A:** lsc.md (13a) on $\mathbb T_{m'}$ and (21a) on $\mathbb T_m$ give (VT2) with $\mathsf B\ell^4$ replaced by $(C_+^*+C^*_{\rm low})L^{4b}\ell^4\le E_*L^{4m_J(g)}\ell^4$. In last-lattice units the per-ball part (ii) on $\mathbb T_{m'}$ uses cell side $\ell(2,RL^b)\le L^b\ell$ and $C_{\rm face}(RL^b)$, maximized over $\mathcal B(g)$. Then $C_{\rm VT}$ is still a function of $(L,\mathfrak p,g,\varrho;R)$ alone. **Case B:** (T1)–(T5) are unavailable (F2), but the conclusion holds by LSC (d): see §3, item 2.

**U8 (not in the inventory). Proof of `8.22:def-expansion-consistency`, II:142268–142295.** Reads $\mathsf B\le C_{\mathsf B}(1+\log g^{-2})$ and then the unit conversion: "$b=b(g)$ independent of $K$ and $m$", $L^b\le{\rm const}\cdot L^{11}M(\log g^{-2})^{r_{\rm pr}}$, depth floor polylogarithmic of degree at most $4r_{\rm pr}+1$. **Covered after a stated ceiling:** use $\mathsf B$ per last-lattice site, bounded by $E_*\le C_E(1+\log g^{-2})$, and $L^b\le L^{m_J(g)}\le C_JL^{11}M(\log g^{-2})^r$. Both are Lemma M below; neither is in lsc.md. The literal "$b=b(g)$" is not proved (F1); only the bound is read.

**U9. CA-III `9.98:def-prolongation-depths` (71655–71690), `9.98:prop-transfer-three-sources` (72708–72990), and III:73918–73942.** The three-source transfer has the structure of U7 at a fixed reference coupling, with hypotheses (a), (d) in unit-lattice volume $N_{m''}=2L^{m''}$ and (e) for the vacuum residue. **Covered after the same ceilings** ($L^{4b}\le L^{4m_J(g^\flat)}$, a fixed number at $\gamma_\star$). $E_{\rm vac}$ does not cancel there; hypothesis (e) carries it. Case B follows by LSC (d) at $n=3$ (difference at most $2C^B_3(R)\prod\|F_i\|_\sharp$). III:73918–73942 is a one-torus quotient: sum, $E_{\rm vac}$ cancels, covered after the same ceiling. Off our T0 path.

**U10. `6.4:rem-small-cutoffs`, II:64437–64493.** An alternative, not a use. Its claim that a separate small-$K$ treatment "is not needed" is not supported: in Case B no correlation-theorem run exists (F2), so LSC (d) is needed. Its local bound is **covered after a stated ceiling:** its "$m_{\mathbb T}(g)$, the torus floor of the correlation theorem at $g$" must be read in Chapter 5's sense, $=m_J(g)$. Then $12(2R+4)^4L^{4K}\le12(2R+4)^4L^{4m_J}$ is free of $m$. In Chapter 6's sense the ceiling would be too small. The global-count sentence at II:64467–64469 is stale (already noted in lsc.md §7).

**U11. Dependency summaries: CA-I 3168–3175, CA-III 110892–110898, CA-II 64598–64599.** No content is read. **Covered** as dependency mentions: LSC is now an implication at the account's standing (lsc2-gate), with the normalization correction. lsc.md does not use CMP122b p.355, consistent with II:63552.

**U12. CA-III 21096–21106, 73458–73540, 75692–75703.** One torus fixed by $g$, or a stopped run with other constants. No torus-uniform last-scale content is needed. **Not uses;** nothing to supply.

## 3. Findings that change what a consumer may read, ranked

1. **8.22 and 9.98 read the stability bounds in the wrong volume for LSC (U6, U7, U9).** They state $|\widetilde Z_m|\le e^{E_+^\sharp(2L^m)^4}$ and $\widetilde Z_m(0)\ge e^{-C_{\rm low}(2L^m)^4}$ with counterterm levels $j\le K$, as if the correlation theorem's last lattice were the unit lattice. At small $g$ that identification has no admissible data (F3). LSC supplies the bounds on the level-$K'$ lattice, $K'=K-b$, with $\mathsf V=L^{4b}(2L^m)^4$. Every conclusion of `8.22:thm-volume-transfer` and `9.98:prop-transfer-three-sources` survives (Case A here; Case B by item 2) with $\mathsf B$ replaced by $(C_+^*+C^*_{\rm low})L^{4b}\le E_*L^{4m_J(g)}$ and $C_{\rm face}(R)$ by $\max_{b\in\mathcal B(g)}C_{\rm face}(RL^b)$. The unit-site clause $\mathsf B\le C_{\mathsf B}(1+\log g^{-2})$ at II:140932–140933 does not survive. The one consumer that reads the size of $\mathsf B$ (U8) already makes this conversion at II:142285–142295 and stays correct with Lemma M. **For the T0 tree (node AIV):** P9's H-VT(d) (`port/p9-witness.md` 323, 388–393) keeps the printed unit-lattice form. LSC supplies H-VT(d) only in the last-lattice form above, Case A. P9's note that no automatic replacement is asserted is right; this is the replacement and its price.

2. **Case B of the volume transfer (U7, U9): repair, proved here.** For $K_J<m_J(g)$ the hypotheses (T1)–(T5) are not supplied (F2). LSC (d) at $n=2$ gives, on each torus, $|S^T_{2;K,m''}(F_1,F_2)|\le C^B_2(R)\|F_1\|_\infty\|F_2\|_\infty$ for $F_1,F_2$ supported in a ball of radius $R$, with $C^B_2(R)=2[12(2R+3)^4]^2L^{8m_J(g)}$, since $c_2=\sum_{\pi\in{\rm Part}(2)}(|\pi|-1)!=2$. LSC (d) needs no torus floor and no separation. By the triangle inequality and $\|F\|_\infty\le\|F\|_\sharp$,
   $$|S^T_{2;K,m}-S^T_{2;K,m'}|\le2C^B_2(R)\|F_1\|_\sharp\|F_2\|_\sharp .$$
   So the volume-transfer bound holds for every $g_0\in\,]0,g_-(g)]$ with constant $\max\{C_{\rm VT},2C^B_2(R)\}$, still a function of $(L,\mathfrak p,g,\varrho;R)$ alone. The same argument at $n=3$ gives $2C^B_3(R)$ for 9.98. Case B depends on $(g_0,g)$ only, so both tori are in the same case.

3. **$E_{\rm vac}$ cancels at U1–U5 and does not cancel at U7, U9 (three-source part).** At U1–U5 every bound is a quotient on one torus in one run, as in lsc.md (30)–(31). At U7 and U9 the upper bound and the floor sit on different tori. The residue is the vacuum-density difference, an input outside LSC (`8.22:lem-vacuum-energy-density`; 9.98 hypothesis (e)). LSC supplies exactly the two one-sided normalized bounds those proofs read, each individually uniform, each with its own torus's $E_{\rm vac}$ and the common endpoint $H=K$. Not checked here: that the vacuum-density lemma, whose hypothesis (a) removes the Gaussian normalizers and compares them by a determinant lemma (II:141286–141292), bounds the full difference that the theorem reads.

4. **`6.4:rem-small-cutoffs` (U10).** Its claim that no separate small-cutoff treatment is needed is not supported (F2): LSC (d) is needed in Case B. Its ceiling "$K<m_{\mathbb T}(g)$" is right only in Chapter 5's sense of $m_{\mathbb T}$ ($=m_J$).

5. **"$b$ independent of $K$" (U1, U8).** LSC proves only $b\in\mathcal B(g)\subset[0,m_J(g)]$ (F1). Every use reads only the bound or the finiteness, so nothing breaks.

None of these is a candidate contribution by itself. Items 1, 2 and 4 change constants or add a two-line case. The conclusions of the account's statements survive, and its own II:142285–142295 already makes the conversion of item 1 for the depth floor.

## 4. Lemma M: a ceiling for $m_J(g)$ and the size of $E_*$

Proved here by Claude, not yet checked by the other model. It supplies the two ceilings that U8 reads and lsc.md does not state.

**Lemma M.** Fix $L,\mathfrak p,\gamma,\varrho$, the radius exponent $r$, and the flow constants $\lambda>0$, $b_+,c_2\ge0$. There are $C_J$, $C_x$, $C_E$, fixed before $g$, such that for every admitted $g$ (so $X=g^{-2}\ge4$, lsc.md §1):

- (M1) $L^{m_J(g)}\le C_JL^{11}M(\log X)^r$; hence $L^b\le C_JL^{11}M(\log X)^r$ for every $b\in\mathcal B(g)$;
- (M2) $x^*(g)\le C_xX$ and $E_*\le C_E(1+\log X)$, with $E_*$ of lsc.md (23).

*Proof.* Step 0. If $x\ge e$ then $R_J(x)<L(\log x)^r$. Indeed let $L^j$ be the least power of $L$ with $L^j\ge y:=(\log x)^r\ge1$. If $j\ge1$ then $L^{j-1}<y$; if $j=0$ then $1\le y<Ly$.

Step 1. Put $c:=b_++4c_2$ and $Y_m:=X+c+3\lambda m$, and assume $X\ge X_1:=\max\{4,3\lambda\}$. For integers $m,u\ge0$ we have $Y_m\ge3\lambda$ and $\log Y_m\ge\log4>1$, so
$\log(Y_m+3\lambda u)\le\log Y_m+3\lambda u/Y_m\le\log Y_m+u\le(1+u)\log Y_m$. With Step 0 and the definition (CA-II 707–708),
$$N_{\mathbb T}(g,m)\le L^{12}MS(\log Y_m)^r,\qquad S:=\sup_{u\ge0}L^{-u}(1+u)^r .$$

Step 2. $S\le(1+u_1)^r$ with $u_1:=\lceil2r/\log L\rceil$. For $u\ge u_1$ the ratio of consecutive terms is $(1+\tfrac1{1+u})^r/L\le e^{r/(1+u)}/L\le L^{1/2}/L<1$, since $r/(1+u)\le\tfrac12\log L$. So the terms do not increase from $u_1$ on. Each term with $u\le u_1$ is at most $(1+u_1)^r$.

Step 3. Let $m_0(X)$ be the least integer $m\ge0$ with $L^m\ge T:=L^{12}MS(2\log X)^r$. Since $T\ge1$, $L^{m_0}<LT$ as in Step 0, so $m_0<13+\log_L(MS)+r\log_L(2\log X)$. As $L\ge3>e$ and $2\log X>1$, $\log_L(2\log X)\le\log(2\log X)\le2\log X\le2X$. Hence
$Y_{m_0}\le X+A_h+B_hX$ with $A_h:=c+3\lambda(13+\log_L(MS))\ge0$ and $B_h:=6\lambda r$. For $X\ge X_2:=\max\{X_1,1+A_h+B_h\}$ this gives $Y_{m_0}\le(1+A_h+B_h)X\le X^2$, so $\log Y_{m_0}\le2\log X$. By Step 1, $N_{\mathbb T}(g,m_0)\le T\le L^{m_0}$. So $m_0$ meets the floor, $m_J(g)\le m_0$, and $L^{m_J(g)}<2^rL^{13}MS(\log X)^r$.

Step 4. Let $4\le X<X_2$. At fixed $m$, $N_{\mathbb T}(g,m)$ is non-decreasing in $X$: $R_J$ is non-decreasing and each argument $X+c+3\lambda(m+u)$ grows with $X$. Put $m_2:=m_0(X_2)$. Step 3 at $X_2$ gives $L^{m_2}\ge N_{\mathbb T}(X_2^{-1/2},m_2)\ge N_{\mathbb T}(g,m_2)$, so $m_J(g)\le m_2$ and $L^{m_J(g)}<2^rL^{13}MS(\log X_2)^r$.

Since $\log X>1$ and $\log X_2>1$, Steps 3–4 give (M1) with $C_J:=2^rL^2S(\log X_2)^r$. Every $b\in\mathcal B(g)$ satisfies $0\le b\le m_J$.

(M2). From (M1) and $\log_L\log X\le\log X\le X$, $m_J\le\log_L(C_JL^{11}M)+rX$. So
$x^*=X+b_++3\lambda m_J+2c_2\le X+c+3\lambda\log_L(C_JL^{11}M)+3\lambda rX\le C_xX$, with $C_x:=1+3\lambda r+\tfrac14(c+3\lambda\log_L(C_JL^{11}M))$, using $X\ge4$. In (17), $p_0\ge0$ and $\log X>1$ give $\varepsilon_*\ge A_0(x^*)^{-1/2}$. Hence
$\log s_*^{-1}\le D+\tfrac12\log x^*$ with $D:=\max\{\log2,\log(8/a_1),\log(8B_3/A_0),\log(8B_3)\}>0$. Then (23) gives
$E_*\le|A_J+E_-+\tfrac34+4\log c_H^{-1}+12D|+(B_J+6)(\log C_x+\log X)\le C_E(1+\log X)$, with $C_E:=|A_J+E_-+\tfrac34+4\log c_H^{-1}+12D|+(B_J+6)(1+\log C_x)$. Every letter here is fixed before $g$ (lsc.md §7). $\square$

**Use in U8.** In last-lattice units the cell side of 8.22 is $\ell L^b<32L^{b+1}$ at $R=1$, and $\mathsf B$ per last-lattice site is at most $E_*$. By (M1)–(M2), $\log C_T(g)$ is at most a constant times $1+(\log g^{-2})^{4r+1}$. This is the account's degree bound $4r_{\rm pr}+1$ for $s_T(g)$ (II:142291–142294), with $r=r_{\rm pr}$.

The face constant at radius $L^b$ is not LSC's, but it does not spoil this degree. For $R'\ge1$ put $t_i:=R'L^i/(4M)$ in lsc.md (24). Since $R'+2\le3R'$, $\mathfrak a(R',i)\le(24t_i+6)^4$. Terms with $t_i\le3$ are at most $78^4$, and there are at most $1+\log_L(12M)$ of them, since $t_i\ge L^i/(4M)$. The terms with $t_i>3$ have indices $i_0,i_0+1,\dots$ with $t_{i_0+k}\ge3L^k$, and each is at most $\sup_{t\ge3L^k}(30t)^4e^{-c_\kappa(t-3)}$. This series in $k$ converges: once $3L^k\ge4/c_\kappa$ the function decreases on $[3L^k,\infty)$, so the supremum is its value at $3L^k$, and consecutive values have ratio $L^4e^{-3c_\kappa(L-1)L^k}\to0$. So $C_{\rm face}(R')$ is bounded by a constant fixed before $g$, uniformly in $R'\ge1$.

## Result

Frozen `library/lsc.md` supplies what each remaining use needs, in Case A, after the ceilings named above. Exceptions are listed below.

- **Covered:** U2 (`6.3:cor-volume-free-constant` and the end of `6.3:rem-per-ball-reading`), exactly; U11 (dependency mentions).
- **Covered after a stated ceiling:**
  - U1: $b_*(g):=m_J(g)$.
  - U3: $b_*(g):=m_J(g)$, $E_*$ inside each $C^\infty_n(\mathsf dL^b;RL^b)$, and the (ii-b) subsequence refined by LSC (e).
  - U4: $Q_*$ of §2.
  - U5: $E_*$.
  - U6: unit-site constants $\times L^{4m_J(g)}$.
  - U7: $\mathsf B\to(C_+^*+C^*_{\rm low})L^{4b}\le E_*L^{4m_J(g)}$ and $C_{\rm face}(RL^b)$; Case B by LSC (d) (§3, item 2).
  - U8: Lemma M.
  - U9: as U6 and U7; off our T0 path.
  - U10: ceiling $m_J(g)$, in Chapter 5's sense of $m_{\mathbb T}$.
- **Not covered:**
  - The Case B instance of 8.22's (a)–(b) (and of 9.98 (a), (d)). There the correlation theorem supplies nothing, and LSC gives no partition-function bound. The transfer theorems' conclusions are recovered from LSC (d).
  - The unit-site clause $\mathsf B\le C_{\mathsf B}(1+\log g^{-2})$ at II:140932–140933. Per last-lattice site it holds for LSC's $E_*$ (Lemma M).
- **$E_{\rm vac}$:** cancels exactly at U1–U5 and at III:73918–73942, inside one run on one torus. It does not cancel at U7 or in the three-source transfer of U9. There the residue is the cross-torus vacuum-density bound, an input outside LSC, not checked here.
- **$C_{\rm low}$ alone or the sum:** U2–U5 and III:73918–73942 read only the sum. U6, U7 and the three-source transfer of U9 read $C_{\rm low}$ and $E_+^\sharp$ separately, on different tori. LSC supplies each separately uniform ($C^*_{\rm low}$, $C^*_+$). U1 and U10 read neither.
- **For the lead (evidence for another file's owner):** P9's H-VT(d) is supplied by LSC only in last-lattice volume, Case A, with the price above, plus the Case B repair. The node AIV line of `library/t0-tree.md` should carry that reading. The account's own II:142285–142295 already makes the same conversion.

Checked line by line by Claude (Mini worker). Lemma M, the face-constant bound and the Case B repair (§3, item 2) are proved by Claude here and not yet checked by the other model. This is a check of implications at the account's standing; it grants no status.
