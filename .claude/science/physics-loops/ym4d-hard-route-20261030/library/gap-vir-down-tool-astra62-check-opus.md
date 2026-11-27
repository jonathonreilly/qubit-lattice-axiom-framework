# Check of row 1624 (gap-vir-down-tool-astra62.md), FINISH.md row 1625

Checker: Claude Opus 5.5, cross-provider hand check of a gpt-6.2-astra max file. Status: complete. No Lean. Two exact-rational guide runs in the session scratchpad (not in the repository, not proof steps). Nothing committed or pushed; no other file written.

## 0. Reading log

- FINISH.md rows 1624 (brief and RESULT) and 1625 (this brief): read.
- `library/gap-vir-down-tool-astra62.md` (row 1624): read in full, L1-293, line by line.
- `library/gap-direction7-fable.md` (row 1610) sections 2.3-3.8 (L106-231): read.
- `library/gap-direction7-fable-check-astra62.md` (check 1613): read in full.
- `library/gap-vir-down-astra62-check-opus.md` (check 1621) and `library/gap-vir-down-neon-check-opus.md` (check 1622): read in full. They summarise rows 1617 and 1618 line by line; I used their verified statements of row 1617 (2), (10)-(13) and row 1618 Theorem 2.
- `library/gap-mech-direction4-fable.md` (row 1553) section 1.4-1.5 (Lemma ALG, tests g1-g6): read.
- `library/open-registry.md` rows VIR-DOWN, LEV-FAIL: read.
- Not opened: `library/gap-vir-down-dom-astra62.md` (as instructed). Rows 1617, 1618, 1619 themselves were not re-read beyond what checks 1621/1622 quote; their cited results enter row 1624 only in (14) and (18).

Conventions as in row 1624: $A_\beta=P_0T/\lambda$ on Haar space, $P=U^{-1}AU$ on $L^2(\pi)$, $f_i$ eigenbasis, $S$ = density of $\sigma$ relative to $\pi\otimes\pi$, $S_k=P^kSP^k$, $h=2k+2$.

## 1. Line-by-line check of the PROVED items

All re-derivations below are by hand. No Lean.

### 1.1 Setting (1)-(3) and the centering identity (5) — HOLDS

- (1). The gauge- and centre-averaged kernel $K_h$ is positive, so $p_h\ge0$. $P_0$ commutes with $T$ and is idempotent, so the kernel of $(P_0T)^h$ is $K_h$ and $p_h=p_1^{*h}$ (Chapman-Kolmogorov). Both marginals of $q_h$ are $\pi$ because $\Omega$ is the Perron vector. HOLDS.
- (2). $\int B p_2\,\pi(dy)=g(x)-g(x)-\int g\,d\pi=0$. The duration term has density $-2\kappa(p_2-p_1)$, also with zero marginals. HOLDS.
- (5). $\mathbb E[(A-\bar a)F(X,Y')]=\int F(x,y)g(x)\,\pi\pi$, its mirror, and $\mathbb E[(A-\bar a)F(X',Y')]=0$. Summing gives $\int F[(a-\bar a)p_2-g(x)-g(y)]\pi\pi=\int FB\,dq_2$. HOLDS. Bound: two steps hold $6n^3$ temporal plaquettes and $3n^3+2\cdot\tfrac32n^3=6n^3$ spatial plaquettes, each in $[0,2]$; so $0\le A\le24n^3$. HOLDS.
- Spectral meaning. $U^{-1}MU$ has density $M(x,y)/(\Omega(x)\Omega(y))$ relative to $\pi$. With $(A_b^2)'=(T^2)'/\lambda^2-2(\lambda'/\lambda)T^2/\lambda^2$ and $-\partial_b K_2=aK_2$ (the averaging variables included), the density of $-U^{-1}(A^2)'U$ is $(a-\bar a)p_2$, using $\bar a=-2\lambda'/\lambda$ (Hellmann-Feynman for the simple top eigenvalue). Compression by $Q$ subtracts exactly $g(x)+g(y)$. So $Bp_2=Q[-(A^2)']Q$ in $L^2(\pi)$. HOLDS.

### 1.2 (4) implies (6); identities (7)-(10) — HOLDS

- (7). $p_k(x,\cdot)=\sum_i r_i^kf_i(x)f_i$ in $L^2(\pi)$ ($k\ge1$, bounded kernel); Parseval gives $D_k$. $L_k=\|\mathbb E_\pi[\delta_k\mid\mathcal C]\|^2_\pi$ since $P^k(x,C)=\pi(C)\mathbb E[p_k(x,\cdot)\mid C]$. So $L_k\le D_k$ and (13) is Pythagoras. HOLDS.
- (8). $2j\le t-2<2j+2$ and $0\le r_i\le1$ give $r_i^{2j+2}\le r_i^{t-2}\le r_i^{2j}$ termwise. HOLDS. Hence (4) gives $\int D_*\,d\sigma\ge\int L_{j+1}w_+dq_2-\int D_jw_-dq_2\ge0$. HOLDS.
- (9). The squared one-end terms vanish against the zero-marginal measures. The density $Bp_2$ is bounded and $\sum_{i>0}r_i^{t-2}f_i^2\le p_{2j}(x,x)$ is bounded for $j\ge1$, so termwise integration is justified. $\langle f_i,Bp_2f_i\rangle=-\langle\psi_i,(A^2)'\psi_i\rangle=-2r_id_i$. So $\tfrac12\int D_*B\,dq_2=2\sum_{i>0}r_i^{t-1}d_i=(2Z/t)\partial_\beta X$ by the trace formula $G_\beta=t\operatorname{Tr}(A^{t-1}A')$ (check 1613 (R)), with $d_0=0$. Second line: $\langle f_i,(p_2-p_1)f_i\rangle=r_i^2-r_i$, and $r^{t-1}(1-r)=r^t(e^m-1)$. HOLDS.
- (10) follows by linearity. With $e^m-1\ge m$, (6) follows. HOLDS. The identity (10) is exact; the only slack in (4) is the one-sided weights $L_{j+1}$ (positive part) and $D_j$ (negative part) in place of $D_*$.
- Integer-period field check (L107). For integer $t\ge4$ the mixed term is $-2(p_{t-2}(x,y)-1)$; the $g$-terms integrate to zero against $p_{t-2}$; closing the ring gives $Z(t)(\mathbb E_tA-\bar a)$ with $\mathbb E_tA=2A_t/t$ (translation in each twist sector) and $\bar a=2a_0$. The duration term closes to $Z(t)-Z(t-1)$. Result $Z(a_0-A_t/t)-\kappa[Z(t-1)-Z(t)]$, consistent with (10) and Lemma D1. HOLDS. This is a second route to (10) at integer $t$ (ring closure instead of the eigenbasis), so it is a genuine cross-check of the sign and factor.

### 1.3 (11)-(13) — HOLDS

$\int_A(1-p_1/p_2)\,dq_2=q_2(A)-q_1(A)$ gives (11). On $A$, coarsening $\mathcal C$ to $\{C,C^c\}$ can only lower $L_{j+1}$, and the two-cell value is $d^2/[p(1-p)]$ with $|d|\ge a$. With $\int_Aw_+\ge\sigma(A)\ge M$ this gives (12). (13) is the projection identity; $D_j=p_{2j}(x,x)+p_{2j}(y,y)-2p_{2j}(x,y)$ by symmetry and composition. HOLDS.

### 1.4 (14), strict positivity on Wilson boxes — HOLDS (qualitative only)

- $\sigma\ne0$: if $\sigma=0$, the diagonal on $f_i$ gives $d_i/r_i=\kappa(e^{m_i}-1)$ for all $i$. Row 1617 (2) (checked in 1621 §1.3) gives $(d_i/r_i)/m_i\to0$, while $\kappa(e^m-1)/m\ge\kappa>0$. Contradiction on the infinite neutral spectrum. Total mass zero and a bounded density ($p_2$ is bounded below on the fixed box) give both signs. HOLDS for $\kappa>0$, as stated.
- $L_k>0$ a.e.: the cell union {flowed loop trace $\ge0$} is a union of bins (internal endpoints go up). Gauge equivariance and centre equivariance of the spatial gradient flow (it is the flow of an invariant function for an invariant metric), and contractibility of the squares, make it neutral. The flow is a diffeomorphism onto the whole manifold, so both the set and its complement contain open sets. Injectivity of $P$ on neutral $L^2(\pi)$ (positive multipliers, invertible half-weight; check 1613 (R) item 1) and zero mean make $P^kg$ nonconstant; $P^kg$ is real analytic (entire Bessel-type integrand, compact integration, division by the positive analytic $\Omega$). The level sets of a nonconstant analytic function on the connected manifold $SU(2)^{3n^3}$ are null, so $\{P^kg(x)=P^kg(y)\}$ is $\pi\otimes\pi$-null by Fubini, and $q_h\ll\pi\otimes\pi$. HOLDS.
- $D_k-L_k>0$ a.e.: a fine plaquette trace has an atomless law under $\pi$ (Haar holonomy, positive bounded density), so it differs from its finite-valued cell conditional expectation; the difference is neutral because $\pi$ is gauge and centre invariant. Same analytic argument. HOLDS.
- Scope: these are strict signs at fixed cutoff with no size. The author says so.

### 1.5 (15)-(16), conditioning on longer slabs — HOLDS

- $b_kq_h$ has density $S_k=P^kSP^k$ by the Markov property; the duration term becomes $-2\kappa(p_h-p_{h-1})$. Zero marginals persist; conditional Jensen gives $\int|b_k|dq_h\le\int|w|dq_2$. HOLDS.
- (16): $\langle f_i,S_kf_i\rangle=r_i^{2k}\langle f_i,Sf_i\rangle$ and $t-h+2k=t-2$. $D_{*,k}$ lies between $L_{j_k+1}$ and $D_{j_k}$ because $2j_k\le t-h<2j_k+2$; $t-h\ge2$ gives $j_k\ge1$. So (15) implies $\int D_*d\sigma\ge0$, hence (6) at the same $\kappa$. HOLDS. Strictness for $b_k$ follows from $r_i^{2k}>0$. HOLDS.
- HS filter bound and (21): $\|E_{\ge m}P^k\|\le e^{-km}$; $|(a-\bar a)p_2|\le B_np_2$ pointwise gives operator norm $\le B_n$; $2\kappa\|P^2-P\|\le\kappa/2$. HOLDS. Both bounds are box-dependent, as stated.

### 1.6 Four-state family (17) — HOLDS

- In this family there is no action. $Bp_2$ is read through its spectral form $Q[-(P^2)']Q$ of §1.1. With fixed fair $\pi$ and fixed characters, $S=-\sum_v2v[v'-\kappa(1-v)]\chi_v\otimes\chi_v$, and conjugation by $P^k$ multiplies by $v^{2k}$. This is (17). HOLDS with that reading (the row says "equivalently ... by expanding the two transition probabilities").
- $r'=\tfrac32(1-r^2)$: $dr/d\beta=6q/(1+q)^2$ and $1-r^2=4q/(1+q)^2$. HOLDS.
- $q=(4096/n)e^{-3x}$; $\kappa W=\tfrac83\cdot\tfrac{27}8\log2=\log512$. HOLDS.
- $-c_r=2r(1-r)[\tfrac32(1+r)-\tfrac83]\ge\tfrac{16}9(1-r)\tfrac16\ge q/6$ for $r\ge8/9$. $|c_v|\le2(\tfrac32+\tfrac83)<9$. $2q\le-\log r\le4q$ for $q\le1/2$. $qt=8e^{-x/3}\le8$, so $r^t\ge e^{-32}$; $2k\le t/4$. $\lfloor t/8\rfloor\ge n/4096-1$ gives $18\cdot2^{-2\lfloor t/8\rfloor}\le72\cdot2^{-n/2048}$. HOLDS. So the density is positive exactly on flips of the first sign.
- Weights: $L_{j_k+1}=4r^{2(j_k+1)}\ge4e^{-32}$ ($2(j_k+1)\le t-h+2\le t$); on negative pairs $D_{j_k}\le8\cdot2^{-2j_k}$; $j_k\ge t/2-k-2\ge3t/8-2$. Equal Jordan masses. HOLDS.
- Coldness: $t(-\log r)\ge2qt\ge16\cdot2^{-9/8}=2^{23/8}>4$, so $G\le e^{-4}+2\cdot2^{-t}<4/21$. HOLDS. The observed mode has rate about 3 and the test certifies $8/3$.

### 1.7 Mode exchange — HOLDS

- The multiplier set $\{r,s,rs\}$ is unchanged, so every spectral quantity (seed, purity, thermal response, HOT) is unchanged. Initial purity $\ge1/(1+G)^2$ with $G(u)\le e^{-16}+2\cdot2^{-u}$ (at $x=0$, $qu=8$) exceeds $64/81>457/625$. HOLDS.
- Integrating (17) over the hidden pair: $c_s=2\kappa s(1-s)$ since $s'=0$, and the observed-flip event has fair mass $1/2$; so $(b_kq_h)(A)=-\kappa s^{2k+1}(1-s)<0$. $L_{j_k+1}=4s^{2j_k+2}\mathbf 1_A$, $D_{j_k}\ge4s^{2j_k}\mathbf 1_A$, so $\int(b_k)_+L\le4s^{2j_k+2}\nu_+(A)<4s^{2j_k}\nu_-(A)\le\int(b_k)_-D$. HOLDS for every $\kappa>0$ and every admissible $k$.
- $\kappa=0$: on $A$ the density is $-2rr'r^{2k}(1-s^{2k+2})\eta$ (I recomputed $c_r r^{2k}-c_{rs}(rs)^{2k}$ with $c_{rs}=-2rr's^2$), a nonzero multiple of the hidden product; so $\nu_+(A)=\nu_-(A)>0$ and the reversal is strict. HOLDS.

### 1.8 Comparison laws (18) — HOLDS

- After the $\sqrt\beta$ rescaling the vacuum and the eigenfunctions are fixed, so $Bp_2=-(p_2)'$ and its diagonal is $-2r_i^2e_Q/\beta$. Identity (10) then gives (18). Integrability: $D_{j_k}\le p_{2j_k}(x,x)+p_{2j_k}(y,y)$, whose integral against either pair law is $2\operatorname{Tr}P^{2j_k}<\infty$; the rotor factor has bounded log-derivative. HOLDS.
- Photon: $e_Q=0$, so (18) $<0$ for $\kappa>0$. Compact Gaussian: $e_Q\le m<e^m-1$, so (18) $<0$ for $\kappa\ge1/\beta$. Then $\int L\,d\mu_+-\int D\,d\mu_-\le\int D_{*,k}d\mu_k=4\cdot$(18) $<0$. HOLDS for every observation and buffer, at every point.
- Conditional interacting U(1) (L222) and the product with the light oscillator (L224): contrapositive of (15)+(16) with check 1613's mean-value argument and the on-file inputs (row 1573/check 1579; the oscillator has $um\le2\pi/512<\log2$, so $G(u)>1/2$). HOLDS as conditional statements.

### 1.9 Finite periodic replacements (19), (20), (22) — HOLDS

- (20). $\mathbb E[A-\bar a\mid X_{-k}=x]=P^kg(x)$, and the Markov property turns $\mathbb E[(A-\bar a)F(X,Y)]$ into $\int F\,P^k((a-\bar a)p_2)P^k\,\pi\pi$. HOLDS.
- (19). Ring minus stationary expectation of a reading $|H|\le1$ is $[\operatorname{Tr}((A^M-\Pi)J_H)-\operatorname{Tr}(\Pi J_H)G(M+s)]/(1+G(M+s))$, of size at most $G(M)+G(M+s)\le2G(M)$, using $\|A^M-\Pi\|_1=G(M)$ and $\|J_H\|\le1$. Three draws at sup norm $4B_n$ cost $24B_nG(M)$; the centering mean costs $4\cdot2B_nG(M)$; the two duration expectations cost $8\kappa G(M)$. Total $(32B_n+8\kappa)G(M)$. $G(M)\le2^{1-M/t}G(t)$ and $\bar E_t\ge\tfrac23(\log2)G(t)/t$ give the second form. HOLDS. The flip/gauge insertion at every cut reproduces $(P_0T)^{M+s}$ since $P_0$ is idempotent and commutes with $T$. HOLDS.
- (22). I re-derived: $d\le K_1\le1$ with $d=e^{-12\beta n^3}$; $d\le\Omega\le d^{-1}$; $p_s\le C=d^{-3}$; $|p_M-1|\le Cr_1^{M-2}=\delta$ (pairing through $P^{M-2}$ on mean-zero neutral functions); $\delta\le1/32$ from (22); $d\hat\pi/d\pi=p_M(x,x)/(1+G(M))$ and the ring formula for $\hat p_s/p_s$; $|\log v|\le3\delta$, $|\log(\hat p_s/p_s)|\le9\delta$; the weight changes $36C\delta$, $60C\delta$, $360C^2\delta$, $96C^2\delta$, total $\le500C^2\delta$; Jordan parts are 1-Lipschitz in total variation, and (19) is a total-variation bound; $|\widehat{\mathcal M}-\mathcal M|\le[500\cdot4+8\cdot32]C^2(B_n+\kappa)\delta\le10^4C^2(B_n+\kappa)\delta$; $r_1^{M-2}\le2^{1-(M-2)/t}G(t)$. Finally $\mathcal M\le\int D_{*,k}d\mu_k=4[Z\partial_\beta X/t-\kappa\sum r_i^t(e^{m_i}-1)]$, so $\widehat{\mathcal M}\ge0$ gives $\partial_\beta X/t\ge(\kappa-\eta/(4Z))\bar E_t\ge(\kappa-\eta/4)\bar E_t$. HOLDS. All constants are generous; none is wrong in the direction used.

I found no failing line in any PROVED item.

## 2. Does (15)-(16) give (VIR-down) in the form TR-down with (HOT) accepts?

**Yes, with no loss of rate.** (16) gives $\int D_{*,k}d\mu_k=\int D_*d\sigma$ exactly, and (10) gives $\tfrac14\int D_*d\sigma=Z\partial_\beta X/t-\kappa\sum_{i>0}r_i^t(e^{m_i}-1)$. So (15) at rate $\kappa$ gives $\partial_\beta X/t\ge\kappa\bar E_t$, which is (VIR-down) at the same $\kappa$ with the fixed-time partial derivative that check 1613 says TR-down uses ($\partial_\beta G=(1+G)\partial_\beta X$, $-tG_t=(1+G)t\bar E_t$). The real time $t$ is allowed because $D_*$ is frozen and the trace formula holds at real $t$ (check 1613 (R)). The last-crossing argument (check 1621 §1.12) needs (15) only where $G\le1/2$. With (HOT) at $\beta_h$, TR-down gives the thermal seed at $K$, and check 1613's enlargement gives (PUR-io). The constant schedule $\kappa=8/3$, $\beta_h=\beta_K+\tfrac38\log512$, $t_h=n$ is an admissible order-one schedule over a bare width $2.34$, consistent with the registry's 2.3-2.7.

**The rate loss in (19) and (22) does not eat the margin.**
- (19) is not used in the implication. It is a total-variation error bound for the signed measure. It cannot certify (15) alone, because $D_{j_k}$ has a box-dependent sup norm (the row says so, L251).
- (22) costs a rate $\eta/4$ for any prescribed $\eta>0$, for example $\eta=10^{-2}$. Its price is the period, $M=O(t[\beta n^3+\log(nt/\eta)])$, because of $C=e^{36\beta n^3}$. So the finite-periodic test is a finite object for each box, but a very long one. It is a way to pose (15) on finite periodic laws, not an estimate. The real loss of the method is elsewhere: in replacing $D_*$ by the one-sided weights $L_{j+1}$ and $D_j$ (section 4).

## 3. Selectivity

**Photon and compact Gaussian U(1): the failures read the law, but they are the target's own failures.** The failure line is (18), which is the exact identity (10) evaluated in the model. Any statement $S$ with $S\Rightarrow$(VIR-down at rate $\kappa$) fails wherever (VIR-down) at rate $\kappa$ fails. In the photon $G_\beta=0$ (rescalability of the oscillator law), so every $\kappa>0$ fails. In the compact Gaussian model $R<1/\beta$ (row 1618 Theorem 2, check 1622), so every $\kappa\ge1/\beta$ fails. (18) adds only that the failure is pointwise and holds for every observation and buffer. These failures read the $\beta$-scaling of the law, not the Lie bracket or the dimension. But no step of the method produces them; they are inherited from the target through (10). The row's sentence at L220 is correct in what it says, and should be read with this scope.

**Order-one rate or $1/\beta$?** The proved failure for compact Gaussian U(1) is at $\kappa\ge1/\beta$ only. For rates $\kappa<9/(10\beta)$ the test is undecided there (it is stronger than VIR-down, which holds there). On the band $\beta\ge\beta_K\to\infty$, so every order-one $\kappa$ (e.g. $8/3$) exceeds $1/\beta$ at late cutoffs, and the test fails for the Gaussian model at the needed rate. So the test separates at an order-one rate in the sense required by the registry. The separation is the target's separation ($R<1/\beta$ versus a needed rate near 2.3-2.7). The SU(2) side of the separation is the GUESSED domination, so no separation has been proved.

**Lemma ALG (row 1553).** (15) on a HOT window implies the seed, so it is false on the product of 4D SU(2) Wilson with a light neutral oscillator (L224, HOLDS). Hence it is not decided by "su(2) and $d=4$", as Lemma ALG requires of any input; again this is automatic for any sufficient condition of the seed. Test (g2), weak 5D SU(2): open, and the row says so. Test (g3), the gapped twins, is not addressed; the photon/Gaussian failure line has no strong-coupling analogue in the row.

**Mode exchange: the test is not a function of the spectral data.** The seed, the purity, (VIR-down) and (HOT) are functions of the eigenvalue curves $\beta\mapsto r_i(\beta)$. The mode exchange keeps all of them and flips the test. So (15) with a fixed observation is **strictly stronger** than pointwise (VIR-down) in the class of positive transfer families, and it cannot be equivalent to the seed there.
- Strength: it escapes "equivalent is not progress" in that class, and it reads a property of the law that the spectrum does not see (which observables carry the rate). This is the kind of input Lemma ALG and Proposition NEG (row 1386) ask for.
- Flaw: it is a stronger hypothesis. Its failure on Wilson would refute nothing. Its truth needs an a priori choice of observation that sees the rate-carrying modes. The row labels the adequacy of the flowed-loop partition GUESSED (L47). For pure Wilson there is no exchange freedom, so the exchange is not evidence against Wilson; it shows only that the test can lose the whole rate.

**A further loss, not in the row (ARGUED; exact-rational GUIDE).** The buffer removes only modes with $m\gg1/t$: the factor is $e^{-2km}$ with $k\approx t/8$. In the passing four-state family the hidden mode has $m=\log2$, far above the cold scale $1/t$. So that example does not test the case that matters on a cold Wilson box, where many unobserved levels sit at energies of order $1/t$. A minimal case: two independent signs with the **same** multiplier $r=e^{-m}$ at the test point, the observed one with $r'=\tfrac32(1-r^2)$ (rate about 3), the hidden one with zero slope, observation of the first sign only. To first order in $m$, ignoring buffer factors, the density on the four pair classes is proportional to $(-c_r)(-\epsilon)+c_s\eta+c_{rs}\epsilon\eta$ with $-c_r\approx2m(3-\kappa)$, $c_s\approx2\kappa m$, $c_{rs}\approx-2m(3-2\kappa)$. The negative pairs with observed sign agreeing and hidden sign flipped carry full $D$ weight but zero $L$ weight. At $\kappa=1.2$ this gives positive side $7.2$ against negative side $9.6$ (same units), so (15) fails, while the thermal rate is about $1.5$. Guide: exact rational arithmetic (Python `fractions`, one process, a few kB, not Lean-checked, not a proof step) at $r=1-1/400$, $t=400$, $k=50$ gives LHS-RHS of (15) equal to $+4.8\times10^{-4}$ at $\kappa=1.1$ and $-3.0\times10^{-4}$ at $\kappa=1.2$. The exact identity (10) is positive up to $\kappa=1.4$ (value $+2.5\times10^{-4}$). So one unobserved level at the cold scale whose rate is below $\kappa$ costs a constant fraction of the certifiable rate, even when the observed mode carries rate 3. Many levels with the same law and rate 3 pass trivially (same guide, $N$ identical observed-type signs, one observed: for $N=3$ the density is negative only on the no-flip class, where $D=0$; for $N\le6$ the value LHS-RHS equals the $N=1$ value). On a cold SU(2) box the momentum levels have rate (mass rate)$\times M^2/E^2$ (row 1610 §3.3 warning, ARGUED), below the mass rate. With a needed $\kappa$ near the mass rate $3\pi^2/11\approx2.69$ (GUIDE), such levels play the role of the hidden zero-slope sign. Whether the flowed loops at side $n/32$ see them is the open question.

## 4. The GUESSED domination, stated exactly

**Statement (DOM).** Fix the release witnesses $b,g_0$ and one $\ell\in1024\mathbb N$. For infinitely many $K$: with $n=\ell b^K$, $u=n/512$, $\kappa=8/3$ (or another prescribed order-one schedule), $\beta_h=\beta_K+\tfrac38\log512$, $t(\beta)=u\,e^{\kappa(\beta-\beta_K)}$, at every $\beta\in[\beta_K,\beta_h]$ with $G(t(\beta);\beta)\le1/2$, with $k=\lfloor t/8\rfloor$, $h=2k+2$, $j_k=\lfloor(t-h)/2\rfloor$ and the flowed-loop partition $\mathcal C$ of L45,
$$\int(b_k)_+L_{j_k+1}\,dq_h\ \ge\ \int(b_k)_-D_{j_k}\,dq_h .$$

**What it is.**
- (DOM) $\Rightarrow$ (VIR-down) at rate $\kappa$ at those points (section 2). With (HOT) at $(t_h,\beta_h)=(n,\beta_K+\tfrac38\log512)$ it gives the thermal seed at $K$ and (PUR-io) after the fixed enlargement (check 1613).
- (DOM) is **not weaker** than pointwise (VIR-down): it implies it at the same point and the same rate.
- In positive transfer families it is **strictly stronger** (mode exchange; section 3's hidden-mode case). For Wilson, equivalence with (VIR-down) is open.
- It is not equivalent to (PUR-io) in any proved sense. It has no small number, and (HOT) is a separate clause. Its truth is not a function of the spectrum, so it cannot be a rewrite of the seed in the class of positive transfer families.

**Is it the whole remaining difficulty?** For the band part (C4 of row 1610) yes, and more: (DOM) contains all of thermal (VIR-down) on the cold collar (C4, which check 1621 showed is the retained response (11) of row 1617 up to an $O(1/\beta)$ shift), plus the extra requirement that one fixed coarse observation sees enough of the rate. For the seed through TR-down, (HOT) at $t_h=n$ (C2 of row 1610) is also open and separate. The finite-box facts (14) give signs, not sizes, and (19), (22) give accuracy, not sign. So nothing in row 1624 bounds any part of (DOM).

## 5. New and on file

| Statement | Standing |
|---|---|
| (5), two-end centering of the marked action, and its spectral form $Bp_2=Q[-(A^2)']Q$ | New in this form. Neighbours ON FILE: row 1132 §2, row 1215 (24), row 1220, Sussman-Alpoge outline 29991-29998 (cited by the row; not re-read by me). |
| (7)-(10), the frozen interpolation $D_*$ and the identity (10) | New as a kernel identity. Its content is Lemma D1 / Remark FIELD of row 1610 (check 1613) and the real-time trace formula of check 1613 (R). The integer field check reproduces D1. |
| The test (4)/(15) with a fixed coarse observation | New. |
| (11)-(13) | New, elementary. |
| (14) | New. Uses row 1617 (2) (check 1621 §1.3) and check 1613 (R) item 1 (injectivity). |
| (16), HS filter bound, (21) | New, elementary Markov and norm bounds. |
| Four-state family and mode exchange | New. Same style as Example NE (row 1610 §3.6) and check 1613's three-state and two-state families. |
| (18), photon and compact Gaussian | New computation. Content ON FILE: photon $G_\beta=0$ (row 1610 §2.5, check 1613); $R<1/\beta$ (row 1618 Theorem 2, check 1622). |
| Interacting U(1), product with oscillator | ON FILE inputs (row 1573, check 1579; rows 998, 1553, 1617 (13), check 1621) applied to (15). |
| (19), (20) | New; extend row 1617 (10). Marked-segment trace ON FILE (row 667 §8, row 671). |
| (22) | New. Ring gluing ON FILE (rows 1173, 1174). |

## RESULT

Row 1625, Claude Opus 5.5 hand check of row 1624 (gpt-6.2-astra max). No Lean; two exact-rational guide runs outside the repo, not proof steps.
Item 1, (5), (15)-(16), (19), (22): HOLDS. (15) gives (VIR-down) at the same rate kappa (with the secant e^m-1). (22) costs only eta/4, at period O(t(beta n^3 + log(nt/eta))).
Item 2, strict positivity (14) of both signed parts and of the within-cell cost: HOLDS, qualitative only, no size uniform in K.
Item 3, four-state family at rate 8/3 over integrated speed log 512: HOLDS (with Bp_2 read spectrally). Its hidden mode sits at energy log 2, far above the cold scale.
Item 4, mode exchange: HOLDS. Photon (all kappa > 0) and compact Gaussian U(1) (kappa >= 1/beta): HOLD, via the identity (10) = (18).
Selectivity: the U(1) and photon failures read the law, but they are the target's own failures inherited through (10), not a step of the method.
The proved U(1) failure is at kappa >= 1/beta only. This covers every order-one rate at late cutoffs, but the SU(2) side is unproved.
The mode exchange shows the test is not a function of the spectrum. So it is strictly stronger than (VIR-down) for positive transfer families: not a seed rewrite (a strength), but a harder hypothesis (a flaw).
New (ARGUED, guide): one unobserved cold-scale level with rate below kappa costs a constant fraction of the certifiable rate (fails at 1.2 with thermal rate 1.5).
Item 5, GUESSED domination (DOM, section 4): it implies pointwise (VIR-down) and is strictly stronger in abstract families. It contains all of C4, and (HOT) is separate. It is not shown equivalent to (PUR-io).
Overall: outcome (d) HOLDS as a first component. No PROVED line fails. No open input moves: (DOM), (HOT), (PUR-io) and the gap remain open.
