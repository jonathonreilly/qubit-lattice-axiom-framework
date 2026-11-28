# Check of row 1617 (library/gap-vir-down-astra62.md), FINISH.md row 1621

Checker: Claude Opus 5.5 (row 1621). Written as I go.

## 0. What I read

- FINISH.md row 1617 (brief and RESULT text), row 1621 (this row).
- `library/gap-vir-down-astra62.md` (row 1617): in full, line by line.
- `library/gap-direction7-fable.md` (row 1610): in full.
- `library/gap-direction7-fable-check-astra62.md` (check 1613): in full.
- `library/gap-mid-max.md` (row 708): lines 50-60 ((VIR_K)), 100-147 (Lemmas 4.1, 4.2, Theorem TR, Remarks CH, LEV).
- `library/gap-mech-direction4-fable.md` (row 1553): section 1.4, Lemma ALG.
- `library/gap-band-neutral-astra62.md` (row 1573): lines 125-152 (the projected compact U(1) comparison).
- `library/open-registry.md`: the rows R11 and TWO-PER.
- `library/gap-vir-down-fable.md` (row 1619): read only after sections 1-3 below were written, for item 4.
- Not read: `library/gap-vir-down-neon.md` (as instructed). Rows 710, 860, 875, 843, 1521, 1180, 1522 are cited by row 1617 for context or for standard facts; I re-derived every fact row 1617 uses from them (Bessel series, the ratio bound, the moment identity) instead of reading them.

No computation was run. Every verification below is by hand.

Notation as in row 1617: $c_k=2e^{-\beta}I_{k+1}(\beta)/\beta$ (one-link multiplier of spin $k/2$), $\rho_k=c_k/c_0$, $g_\beta(k)=\partial_\beta\log c_k$, $T=MCM$, $L_{\rm el}=C^{1/2}M^2C^{1/2}$, $w=C^{1/2}M\psi/\sqrt\lambda$, $d=3n^3$, $V_*=6n^3$.

## 1. Line-by-line check of the PROVED items

### 1.1 Preliminaries used by every item

- Multiplier. $e^{(\beta/2)\operatorname{tr}g}=\sum_j(2j+1)\,[2I_{2j+1}(\beta)/\beta]\,\chi_j(g)$ (standard SU(2) character expansion). So convolution by $c_\beta(g)=e^{-\beta(1-\frac12\operatorname{tr}g)}$ acts on the spin-$j$ block by $c_{2j}$. Series: $c_k=e^{-\beta}\sum_h(\beta/2)^{k+2h}/(h!(k+1+h)!)$. HOLDS. $0<c_k\le c_0\le1$ because the kernel is positive and at most one. So $Y\ge0$. HOLDS.
- Label projections commute with gauge and centre actions (gauge acts by left/right multiplication inside each isotypic block; a centre flip acts on spin $j$ by $(-1)^{2j}$). HOLDS.
- Infinite dimension: characters of one contractible plaquette are gauge invariant and centre invariant (a centre flip changes 0 or 2 of its links). HOLDS.
- Bessel ratio bound $0<I_{p+1}/I_p\le\beta/[2(p+1)]$: the ratio of the $h$-th terms is $(\beta/2)/(p+1+h)$. HOLDS.
- $\rho_k\le(\beta/2)^k/(k+1)!$: termwise ratio $(\beta/2)^k(1+h)!/(k+1+h)!$ and $(k+1+h)!/(1+h)!=\prod_{j=h+2}^{h+k+1}j\ge(k+1)!$. HOLDS.
- $g_\beta(k)$: $\partial_\beta\log c_k=-1-1/\beta+I_{k+1}'/I_{k+1}$ and $\beta I_p'=pI_p+\beta I_{p+1}$ give $k/\beta+I_{k+2}/I_{k+1}-1$. HOLDS.

### 1.2 Equation (1), two tails — HOLDS

$\|w\|^2=\langle\psi,T\psi\rangle/\lambda=1$. $\mathbb E_we^Y=\sum_{\mathbf k}|w_{\mathbf k}|^2/c_{\mathbf k}=\|M\psi\|^2/\lambda\le e^L$ ($M\le1$ as $V\ge0$). $C^{1/2}M^2C^{1/2}w=C^{1/2}M\,T\psi/\sqrt\lambda=\lambda w$. With $M^2\ge e^{-\beta V_*}$: $\lambda=\langle w,L_{\rm el}w\rangle\ge e^{-\beta V_*}\mathbb E_we^{-Y}$. Markov on $e^{Y}$ and $e^{-Y}$ gives both tails exactly as printed. Valid for every unit vector of an eigenspace. $V_*=6n^3$ is correct (3n^3 spatial plaquettes, each in $[0,2]$).

### 1.3 Equation (2), the high-level slope — HOLDS

- $Y=N\log(1+N)+O_{I,d}(N+1)$: per link $-\log c_k=\beta+\log((k+1)!)-k\log(\beta/2)-\log(\text{factor in }[1,e^{\beta^2/4}])$; $\log((k+1)!)=k\log(1+k)+O(k+1)$; Jensen for the convex $x\log(1+x)$ and the trivial upper bound give the printed sandwich, and $N\log(1+N/d)=N\log(1+N)+O_d(N)$. HOLDS.
- Inversion $N/(Y/\log Y)\to1$: $Y\to\infty$ forces $N\to\infty$, and $\log Y=\log N+O(\log\log N)$. HOLDS.
- Averaging in the eigenstate. Lower tail of (1) with $x=\delta L-\beta V_*$ gives $\Pr(Y<(1-\delta)L)\le e^{\beta V_*-\delta L}$. Upper tail: $\mathbb E[N;Y>(1+\delta)L]\le C\,\mathbb E[(1+Y);Y>(1+\delta)L]\le C(2+(1+\delta)L)e^{-\delta L}$ by integrating the tail. Middle event: $Y\in[(1\pm\delta)L]$, $Y\to\infty$ uniformly. So $\mathbb E_wN\sim L/\log L$. HOLDS.
- Derivative. $T'=M'CM+MC'M+MCM'$, $M'=-\tfrac12VM$, $[V,M]=0$; the two outer terms give $-\tfrac12(\langle V\psi,T\psi\rangle+\langle T\psi,V\psi\rangle)=-\lambda\langle V\rangle_\psi$. The middle term is $\lambda\,\mathbb E_w\sum_e g_\beta(k_e)$. Multiplying by $\beta$ gives the printed $\beta D_\psi$. HOLDS. Error bound: $|I_{k+2}/I_{k+1}-1|\le1+\beta/4$. HOLDS.
- With $m=L+\log\lambda_0$, $D_\Omega=O(1)$ on $I$ (continuity of the simple $\lambda_0$): $\beta b_\psi=\mathbb E_wN+O(1)\sim m/\log m$. HOLDS uniformly on compact $I$ and in the eigenspace.
- Consistency with the trace formula. With $A=R/\lambda_0$, $G_\beta=t\operatorname{Tr}(A^{t-1}A')=t\sum_{i>0}r_i^tb_i$ for any orthonormal eigenbasis (the $i=0$ term vanishes). So $b_i$ is the right object even at crossings. HOLDS.

### 1.4 Equation (3) — HOLDS

From (2), $b_i\sim m_i/(\beta\log m_i)$, so $0<b_i\le\kappa m_i/2$ above some $\Lambda(\beta,n,\kappa)$. Both sides of (3) follow termwise; the strict signs need one term, and there are infinitely many. $t\sum(b_i-\kappa m_i)r_i^t$ is the tail part of $G_\beta+\kappa tG_t$. HOLDS. Note (row 1617 says it): $\Lambda$ depends on the box, so (3) gives no uniform statement.

### 1.5 Equation (4), joint electric labels — HOLDS

- The unprojected $T$ has a strictly positive continuous kernel; Jentzsch gives a simple positive top vector; gauge and centre unitaries commute with $T$ and preserve positivity, so they fix it. So the full norm equals the neutral $\lambda_0$. $\|L_{\rm el}\|=\|BB^*\|=\|B^*B\|=\|T\|$, $B=C^{1/2}M$. HOLDS.
- Deletion: in 3D each spatial link lies in exactly 4 spatial plaquettes, each costing at most 2, so $0\le V-V_{\rm out}\le8|S|$ and $L_{\rm el}\le L_{\rm el}^S\le e^{8\beta|S|}L_{\rm el}$ (sandwich of multiplication operators). HOLDS.
- Factorization $L^S_{\rm el}=(\bigotimes_{e\in S}C_e)\otimes L_{\rm out}$ and $\|PL^SP\|=\|L^S\|\prod\rho_{k_e}$ with $\|C_e\|=c_0$. HOLDS.
- Compression: take $\phi=Pw_i/\|Pw_i\|$. $\langle\phi,L_{\rm el}\phi\rangle\ge\lambda_i|\langle w_i,\phi\rangle|^2=\lambda_i\|Pw_i\|^2$, and $\langle\phi,L_{\rm el}\phi\rangle\le\langle\phi,PL^SP\phi\rangle\le e^{8\beta|S|}\lambda_0\prod\rho_{k_e}$. This is (4) with one factor $e^{m_i}$. HOLDS.

### 1.6 Equations (5)-(6), cost of the cut — HOLDS

- For $k>J\ge e^2\beta$: $k\ge\beta$ and $I_{k+2}/I_{k+1}\le\beta/[2(k+2)]\le1$, so $0\le k/\beta-1\le g_\beta(k)\le k/\beta$. HOLDS.
- Expansion of $e^{U_J}=\prod_e[1+(e^{k_e}-1)\mathbf1_{k_e>J}]$ over subsets $S$; (4) summed over labels $k_e>J$ on $S$ gives $e^{m_i}A^{|S|}$; summing nonempty $S$ gives $e^{m_i}((1+A)^d-1)$. Jensen: $\mathbb E U_J\le m_i+d\log(1+A)\le m_i+dA$. Vacuum: $m_0=0$. HOLDS.
- $e^k\rho_k\le e^k(\beta/2)^k(e/k)^k=(e^2\beta/(2k))^k\le2^{-k}$ for $k>J\ge e^2\beta$. $A\le e^{8\beta}2^{-J}$; the second entry of (5) gives $dA\le a\delta/t$. HOLDS.
- Omitted scores $O_i\in[0,(m_i+dA)/\beta]$, $O_0\in[0,dA/\beta]$, $b_i-b_i^J=O_i-O_0$. Cold: $e^{-tm_i}\le G(t)\le c$ gives $m_i\ge a/t$, so $dA\le\delta m_i$. This is (6). HOLDS. Injectivity gives $r_i>0$, so every excited level is covered.

### 1.7 Equation (7) — HOLDS

Multiply (6) by $r_i^t/(1+G)\ge0$, sum, use $G_\beta/(t(1+G))=\sum_{i>0}b_ir_i^t/(1+G)$. The sum of $d_i^J$ over a degenerate eigenspace is a trace of a compressed bounded form, so basis independent. HOLDS in both directions.

### 1.8 The field check (8) of the lower error — HOLDS (at $\beta\ge1$, as stated)

- $\operatorname{Tr}_0(P_{e,k}L_{\rm el}^s)=\sum_i\lambda_i^s\Pr_{w_i}(k_e=k)$. Cyclicity puts $C_eP_{e,k}$ in place of one temporal convolution. $P_{e,k}$ is convolution by $(k+1)\chi_{k/2}$, so $C_eP_{e,k}$ has kernel $(k+1)c_k\chi_{k/2}$. The ratio to the original temporal weight gives (8). The neutral projection is the twist average in numerator and denominator. HOLDS.
- $|(8)|\le e^{2\beta}(k+1)^2c_k\le e^{2\beta}(k+1)^2\rho_k$ ($c_\beta\ge e^{-2\beta}$, $|\chi_{k/2}|\le k+1$, $c_0\le1$). HOLDS.
- $k(k+1)^2=k^3+2k^2+k\le6e^k\le11e^k$ (from $e^k\ge k^3/6+k^2/2+k$). $11e^{2\beta}\le e^{8\beta}$ needs $\beta\ge(\log11)/6$; $\beta\ge1$ suffices. Then $O_0\le(d/\beta)e^{8\beta}2^{-J}\le a\delta/(\beta t)$. With $O_i\ge0$ this gives the lower side of (6). HOLDS. This route uses only the one-link vacuum marginal, so it is a genuinely different derivation from the deletion argument.

### 1.9 The kernel check of both errors — HOLDS (at $\beta\ge1$)

- $\widetilde c=c_\beta+\sum_{k>J}(e^k-1)(k+1)c_k\chi_{k/2}$, so $|\widetilde c|\le c_\beta+\sum_{k>J}(e^k-1)(k+1)^2c_k\le(1+A')c_\beta$. HOLDS.
- $(k+1)^2e^kc_k\le(k+1)e^k(\beta/2)^k/k!\le(k+1)(e^2\beta/k)^k2^{-k}\le\frac{k+1}{k}e^2\beta\,2^{-k}\le2e^2\beta\,2^{-k}$, using $e^2\beta/k<1$. With $2e^2\beta\le e^{6\beta}$ ($\beta\ge1$): $A'\le e^{8\beta}2^{-J}$. HOLDS.
- $\mathbb E_{w_i}e^{U_J}=\langle M\psi_i,\widetilde CM\psi_i\rangle/\lambda_i$; absolute values in the full Haar kernel and $|M\psi|=M|\psi|$ give $\le(1+A')^d\langle|\psi_i|,T|\psi_i|\rangle/\lambda_i\le(1+A')^de^{m_i}$ (full norm $=\lambda_0$, $\||\psi_i|\|=1$). HOLDS. Jensen as before. This checks (6) at the same $J$ by a route that does not delete plaquettes. HOLDS.

### 1.10 Equation (9), ordered limit — HOLDS

- Per link $|Y_{\beta_1}(k)-Y_{\beta_2}(k)|\le|\beta_1-\beta_2|+k|\log(\beta_2/\beta_1)|+\beta_2^2/4$, so the label energies differ by $O(1+N)$; with $Y\sim N\log N$, $|Y_1-Y_2|\le\xi Y_2+C_\xi$. HOLDS.
- $C(\beta)$ restricted to the neutral space is diagonal in the same label blocks at both couplings, so the operator inequalities between $C(\beta_1)$ and $C(\beta_2)^{1\pm\xi}$ hold, and min-max transfers them to ordered eigenvalues (monotone functions of commuting operators). $e^{-\beta V_*}C\le L_{\rm el}\le C$ gives $m_i=Y_{(i)}+O(1)$ at each endpoint. Ratio limits in $[1-\xi,1+\xi]$; $\xi\downarrow0$. HOLDS.
- Consequence: for every $E>1$, infinitely many ordered levels violate $m_i(\beta_K)\ge Em_i(\beta_h)$, on every finite box, at every pair of couplings. So (LEV-down) of row 1610 §3.3 fails for every $E>1$ on every Wilson box. HOLDS. It leaves $E=1$ (zero speed) and the thermal form untouched, as printed.

### 1.11 Equation (10), the finite-period form — HOLDS

- $d_i^J\in[-V_*-d,\ d(J/\beta+\beta/4)]$: for $k\le J$, $g_\beta(k)\in(-1,J/\beta+\beta/4-1]$. So $|d_i^J-d_0^J|\le B_J$. HOLDS.
- $G(v)\le G(t)\max_ir_i^{v-t}\le G(t)e^{-a(v/t-1)}$ (from $r_i\le c^{1/t}$). $\bar E_t\ge aG(t)/(t(1+G(t)))$. The choice of $v$ gives $B_JG(t)e^{-a(v/t-1)}\le\eta aG(t)/(t(1+c))\le\eta\bar E_t$; the $\log^+$ case is consistent. HOLDS.
- $\sum_{i>0}b_i^Jr_i^t/(1+G(t))=\bar d^J(t)-d_0^J$ (the $i=0$ term is zero). Substitution in (7) gives both sides of (10). HOLDS. At integer $t\ge3$ the middle term is $a_0-A_t/t$ by Lemma D1. HOLDS.

### 1.12 Sufficiency of (11) with HOT — HOLDS

(11) and the lower side of (10) give $X_\beta\ge\kappa t\bar E_t=-\kappa tX_t$, so $X(t(\beta);\beta)$ is non-decreasing on the part where $G\le1/2$. If $G$ reached $1/2$ on the characteristic, take the last such point $\beta^*$; on $(\beta^*,\beta_h]$ the curve is cold and $X$ rises from $\log(3/2)$ to at most $\log(25/21)<\log(3/2)$: contradiction. So the curve stays below $1/2$, (VIR-down) holds along it, and TR-down applies. (R) on the Wilson box is check 1613. HOLDS.

### 1.13 Equation (12), the clamped signed observable — HOLDS

- $h_q=g_\beta(q)-g_\beta(q-1)=\partial_\beta\log(I_{q+1}/I_q)$ (the $e^{-\beta}/\beta$ factors cancel). With $I_q(\beta)\propto\beta^q\int_{-1}^1e^{\beta x}(1-x^2)^{q-1/2}dx$ and $(I_q/\beta^q)'=I_{q+1}/\beta^q$: $I_{q+1}/I_q=\mathbb E_qx$ and $\partial_\beta\mathbb E_qx=\operatorname{Var}_q(x)>0$. HOLDS for every $q\ge1$.
- $g_\beta(\min(k,J))=g_\beta(0)+\sum_{q=1}^Jh_q\mathbf1_{k\ge q}$; the constant cancels between the two periods; the spatial term enters with the printed sign. HOLDS.
- For $k>J$ the clamped omission $g(k)-g(J)\in[0,k/\beta]$ since $g$ is increasing and $g(J)\ge J/\beta-1\ge0$. Hence (6), (7), (10), the field check and the kernel check carry over unchanged. HOLDS.

### 1.14 Equation (14), integrated speed — HOLDS

VIR-down at a cold point reads $\kappa\sum m_ir_i^t\le\sum b_ir_i^t$; the upper side of (6) gives $\kappa\le R_J+(1+\delta)/\beta$. With $t'=\kappa t$ integrate. $J(\beta)$ takes finitely many integer values on a compact window, and for fixed $J$ the retained sum is a continuous trace, so $R_J$ is bounded and piecewise continuous. HOLDS. Reading: the discarded spins supply at most $(1+\delta)\log(\omega/\alpha)$ of $\log(t(\omega)/t(\alpha))$. This is small only when $\omega/\alpha\to1$. On a window with $\beta_h/\beta_K$ of order $e^7$ (the "near 7" budget of row 1610, GUIDE) the bound (14) does not exclude that the discarded spins supply all of it. Row 1617 states the width assumption; I add that HOT does not fix the width (check 1613), so (14) restricts a mechanism only once a width is fixed.

### 1.15 The comparison statements labelled PROVED — HOLD

- Compact U(1) transfer of (1)-(10), (12): multiplier $e^{-\beta}I_{|j|}$, $\rho_k=I_k/I_0\le(\beta/2)^k/k!$, score $k/\beta+I_{k+1}/I_k-1$, four spatial plaquettes per link, positive kernel. Each step above goes through. HOLDS.
- (13): given row 1573's $G_{\rm even}(u)>1$ on the U(1) boxes (I read row 1573 lines 125-152; it is checked by 1579), the last point with $G=1/2$, the mean value theorem and the lower side of (10) with the stated $\eta,\delta$ give $t(H_J-\kappa\bar E_t)\le-D/(2w)$. Arithmetic: $(\eta+\delta/\beta)t\bar E_t\le2\cdot D/(4w)$. HOLDS.
- 5D constants $d=4n^4$, $V_*=12n^4$, deletion $12\beta$ (six spatial plaquettes per link in four spatial dimensions). HOLDS (the cutoff (5) then uses $12\beta$; the field and kernel checks need $\beta$ bounded below by a constant, which $\beta\ge1$ gives).
- Product with a coupling-independent oscillator: $G_{\rm prod}\ge G_W$, the oscillator does not change $b$, energies only grow, the oscillator purity is $(1-x)/(1+x)<1/3$ for $x>1/2$, purities multiply and each is at most 1. HOLDS.

### 1.16 Verdict on the three PROVED items

- Item A ((6)-(7) with the field and kernel derivations): HOLDS.
- Item B ((10), (12), (14)): HOLDS. Scope of (14): only informative on windows with $\omega/\alpha\to1$.
- Item C ((2), (9)): HOLDS. Scope: the level form with $E>1$ only.

I found no failing line. One wording point, not a correction: row 1617 line 13 says (14) "bounds how much transport the discarded spins can supply across a moving interval". The bound is $(1+\delta)\log(\omega/\alpha)$, which is not small on a window of fixed bare-coupling ratio.

## 2. Selectivity

**The component is not selective, and row 1617 does not claim it is.** I checked each of its lines for the comparison laws.

- Weak 4D compact U(1) (Wilson cosine). (1)-(2), (4)-(7), (9), (10), (12), (14) hold with the multiplier $e^{-\beta}I_{|j|}$, the same deletion count and the same $J$ (row 1617 §"What the comparison theories decide"; checked in 1.15). So the component holds equally for U(1). The level obstruction (9) also holds for U(1): it is a property of every compact Wilson heat kernel (factorial tail), not of SU(2).
- 5D SU(2). Every proof goes through with $d=4n^4$, $V_*=12n^4$, deletion cost $12\beta$. The component holds equally. Only constants read the dimension.
- Free photon. The component has no literal analogue: the noncompact Gaussian magnetic term has no $V_*$, and the Gaussian electric multiplier has no factorial tail, so (1), (2), (5) do not apply. The full hypothesis fails for the photon at (11) itself: the normalized spectrum is $\beta$-independent, so every $b_i=0$, $X_\beta=0$ and (11) would need $0\ge(\kappa+\eta+\delta/\beta)\bar E_t>0$. It fails again at HOT through the transverse mode with $m\le2\pi/n$ (rows 929, 988, check 1613). Both failures read properties of the photon law (coupling rescaling and dispersion), not the algebra or the dimension.
- Where U(1) fails. Given row 1573's input ($G_{\rm even}(u)>1$ for the three half-turns at weak coupling; a measure statement on the thermal weight of the $\pm2e_1$ flux cosets, checked by 1579), (13) places a deficit in the retained observable (12). This reads a property of the law. Two limits: (i) (13) is a contrapositive. It is obtained from the known failure of the conclusion by the mean value theorem, not from any step of the component. It locates the failure; it does not detect it. (ii) It depends on the projection by the three half-turns, which keeps even charges. Under the full continuous centre it is open (row 1573, check 1613).
- Lemma ALG (row 1553). The component holds for the product of the Wilson theory with a coupling-independent light oscillator, which fails (PUR-io) at every side (row 1617, checked in 1.15). So the component is compatible with seed failure in the class with a 4D SU(2) Wilson factor, and by Lemma ALG it cannot be the selective input. It reads neither the algebra nor the dimension beyond constants. It also reads no property of the law that separates SU(2) from U(1).

Verdict: the component holds for weak 4D compact U(1) and for 5D SU(2) (proved); it does not apply literally to the free photon, whose failure of the full hypothesis sits in (11) and HOT and reads the law. All selectivity of the route sits in (11) (and HOT). Row 1617's own statement of this (lines 205, 235, 239) is correct.

## 3. The retained SU(2) response (11)

**Exact statement.** Fix the release witnesses, $\ell$, $K$, a window $[\beta_K,\beta_h]$, continuous $\kappa\ge0$ and $t(\beta)=u\exp\int_{\beta_K}^\beta\kappa$. At each $\beta$ with $G(t(\beta);\beta)\le1/2$ there are $\eta>0$, $0<\delta\le1$ such that, with $c=1/2$, $J$ from (5) and $v$ from (10),
$$
H_J(t,v)=\sum_{e=1}^d\sum_{q=1}^Jh_q\,[p_{e,t}(q)-p_{e,v}(q)]+\langle V\rangle_v-\langle V\rangle_t\ \ge\ (\kappa+\eta+\delta/\beta)\,\bar E_t .
$$
(clamped form (12); $h_q>0$; $p_{e,s}(q)$ the electric-placement probability of $k_e\ge q$ at period $s$; $\langle V\rangle_s$ the magnetic-placement spatial action mean.)

**It carries the whole band difficulty (PROVED here from (10)).** The lower side of (10) gives (11) at rate $\kappa$ $\Rightarrow$ (VIR-down) at rate $\kappa$. The upper side of (10) gives (VIR-down) at rate $\kappa'$ $\Rightarrow$ $H_J\ge(\kappa'-\eta-(1+\delta)/\beta)\bar E_t$, which is (11) at rate $\kappa=\kappa'-2\eta-(1+2\delta)/\beta$. So (11) is (VIR-down) up to a shift of the rate by at most $2\eta+(1+2\delta)/\beta$. On the calibrated trajectory $\beta\ge\beta_K\to\infty$, so the shift is $O(1/\beta_K)$ pointwise; integrated over the window it is at most $2\eta(\beta_h-\beta_K)+(1+2\delta)\log(\beta_h/\beta_K)$. Nothing of the band difficulty is removed: only the large-spin tail and the infinite-time vacuum are replaced by controlled errors.

**Where it is on file.** (11) is C4 of row 1610 §2.6 ((VIR-down) where the box coupling is of order one), in the finite-period truncated form. At integer $t$, $H_J$ equals $a_0-A_t/t$ up to $(\eta+(1+\delta)/\beta)\bar E_t$, so (11) is the trigger of row 1610 §4 item 1 ("a lower bound for $t a_0-A_t$ against $\kappa t\bar E_t$ on cold neutral tori at late bare couplings"). It is the lower mirror of registry row R11 (upper relative transport, row 708 (VIR-log) at one coupling). (VIR-down) has no registry row (grep of `library/open-registry.md` for VIR-down and T-down: no hit).

**Is it equivalent to (PUR-io)?** Not shown either way, and I cannot decide it.
- (11) with HOT $\Rightarrow$ (T-down) $\Rightarrow$ the thermal seed $M$ at $K$ (TR-down) $\Rightarrow$ (PUR-io) after the fixed enlargement of check 1613. ON FILE (check 1613) plus 1.12 above.
- The converse is open, as it is for (T-down) (check 1613).
- A caution that row 1617 does not state. Check 1613 showed that with an existential $\beta_h$ the target at $K$ is the thermal seed $M$ at $K$ plus a one-sided sign of $F(\beta)=G(u;\beta)$ near $\beta_K$. The same holds for (11)+HOT: on a short window with $\kappa=0$, HOT is essentially $M$ at $K$ (with a collar), and (11) is a strict positive rate of the action deficit, of order $1/\beta$, near $\beta_K$. So "(11) with HOT" contains the seed in its HOT clause unless HOT is supplied separately at a hot box on a long window (C2 of row 1610). The sign statement (11) alone has no small number in it, so it is not the seed. Whether (11) on a long window is implied by the seed is open.

So (11) is equivalent, up to an $O(1/\beta)$ rate shift, to the on-file open estimate C4 of row 1610 (its §4 trigger). It is not shown equivalent to (PUR-io).

## 4. Comparison with Corollary LEV-FAIL of row 1619

Read after sections 1-3 were written: row 1619 §2.1-2.3 (setting, Proposition UV-LEV, Corollary LEV-FAIL, its consequences and selectivity paragraph). I read §2.4-3.0 only as far as they sit in the same range of lines; I use nothing from them.

**They agree.** Both prove, on every finite Wilson box and for every pair $\beta_1<\beta_2$, that $m_i(\beta_1)/m_i(\beta_2)\to1$ along the ordered neutral levels, hence (LEV-down) fails for every $E>1$, and the pointwise form fails for every $\kappa\ge0$ with positive integral. Both leave $E=1$ (zero speed) and the thermal form untouched. Both say the obstruction holds for every compact group and dimension, so it is a negative and not an input.

**The proofs are the same skeleton with different label estimates.**
- Common: $T=X^*X$, $XX^*=C^{1/2}M^2C^{1/2}$, $e^{-\beta V_*}C\le XX^*\le C$ on the neutral space, min-max, so $m_i$ equals the $i$-th ordered electric energy up to a box constant.
- Row 1619: a per-link two-sided inequality $\eta_j(\beta_2)-C_a\le\eta_j(\beta_1)\le(1+\varepsilon)\eta_j(\beta_2)+C_b$ from the Bessel series, then a rearrangement lemma for ordered lists with equal multiplicities. I checked Steps 3-6: the bound $U_j-\beta^2/4\le\eta_j\le U_j$, the lower difference $(\beta_2-\beta_1)+(1-\nu)\log(\beta_2/\beta_1)+\beta_1^2/4\le C_a$, and the case split at $\nu_*$. They HOLD.
- Row 1617: a label-wise estimate via $Y\sim N\log N$ and $|Y_{\beta_1}-Y_{\beta_2}|=O(1+N)$, then the operator inequality $C(\beta_1)\lessgtr e^{\pm C_\xi}C(\beta_2)^{1\mp\xi}$ for commuting diagonal operators. HOLDS (1.10).
- Row 1619's lower side ($m_i(\beta_1)\ge m_i(\beta_2)-A_0$, no $\varepsilon$) is slightly sharper than row 1617's $(1-\xi)$ form. Neither needs it for the obstruction.

**Difference in content.** Row 1617 also proves the differential asymptotic (2), $\beta b_\psi\log m/m\to1$: the high levels do fall with $\beta$, at a relative rate $1/(\beta\log m)\to0$. Row 1619 has the endpoint statement only. (2) is consistent with LEV-FAIL and with (9).

**Is either wrong?** I found no wrong line in either proof of the level obstruction. Row 1619's remark that (LEV_K) of row 708 (the upper mirror) is not touched is correct, and also applies to row 1617's (9).

## 5. New and on file

| Statement | Standing |
|---|---|
| (1) two-tail Markov bounds for the electric energy in an eigenstate | New in this form as far as I can tell. Builds on row 710 (Lemmas J, C, Theorem U), ON FILE. |
| (2) high-level slope asymptotic | New. The derivative formula is row 710 Theorem U(ii), ON FILE. |
| (3) tail sign in the thermal test | New, elementary. |
| (4) joint label bound with one factor $e^{m_i}$; (5)-(7) cut cost | New. |
| (8) field check | The one-link insertion is row 860 Lemma OS (ON FILE, cited by row 1617; not re-read by me). The use for the vacuum omitted score is new. |
| Kernel check of (6) | New; row 875's spin-boost caution is respected (absolute bound only). |
| (9) ordered limit, level obstruction | New on 2026-11-27, proved independently by rows 1617 and 1619 (Corollary LEV-FAIL). It turns the ARGUED warning of row 1610 §3.3 into a theorem. No earlier file in `library/` uses (LEV-down) (grep). |
| (10) finite-period replacement of the vacuum | New. |
| (11) sufficiency with HOT | New as a statement. Its content is C4 of row 1610 (§2.6) and the trigger of row 1610 §4, up to an $O(1/\beta)$ rate shift (section 3 above). |
| (12) clamped signed observable, $h_q>0$ | New. The moment identity is row 843 Lemma 3.1 (`library/gap-q8test-opus.md`), ON FILE. |
| (13) U(1) deficit in the retained observable | New; a strengthening of check 1613's mean-value test. Input row 1573 (checked by 1579), ON FILE. |
| (14) integrated speed of the discarded spins | New. |
| Product-with-oscillator test | Method ON FILE (rows 998, 1553, 1573); applied to new estimates. |
| Free photon failure | ON FILE (rows 929, 988, check 1613). |
| Sufficiency (T-down) ⇒ (PUR-io) | ON FILE (check 1613). |

## RESULT

Row 1621, Claude Opus 5.5, cross-provider hand check of row 1617 (gpt-6.2-astra max). No computation, no Lean.
Item A, (6)-(7) with the deletion, field (8) and kernel derivations: HOLDS. Every constant re-derived; field and kernel checks need beta >= 1, as stated.
Item B, (10), (11)-sufficiency, (12), (14): HOLDS. (14) is informative only on windows with omega/alpha -> 1; HOT fixes no width.
Item C, (2) and (9): HOLDS, level form with E > 1 only. (1), (3), (4), (13), the 5D and product tests also HOLD.
Selectivity: the component holds equally for weak 4D compact U(1) and 5D SU(2) (proved in row 1617, checked here) and has no literal photon analogue.
It reads neither algebra nor dimension beyond constants and passes the Lemma ALG product test, so it is error control, not a selective input. Row 1617 says so.
The photon fails at (11) and HOT; U(1) fails at (11) via (13), given row 1573, by contrapositive. Both read the law; the U(1) case needs the three half-turn projection.
(11) carries the whole band difficulty. It is (VIR-down) up to a rate shift of at most 2 eta + (1 + 2 delta)/beta: C4 and the §4 trigger of row 1610.
It is not shown equivalent to (PUR-io). With an existential beta_h, (11) + HOT contains the thermal seed in its HOT clause (check 1613's short-window remark).
Row 1619's Corollary LEV-FAIL agrees with (2), (9). Both proofs hold. Row 1617 adds the slope asymptotic (2).
Overall: outcome (d) HOLDS as a first component of thermal (VIR-down). It moves no open input: (11), HOT, (PUR-io) and the gap remain open.
