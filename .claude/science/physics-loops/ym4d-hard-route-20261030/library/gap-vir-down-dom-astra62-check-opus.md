# Check 1627: cross-provider check of row 1626 (`gap-vir-down-dom-astra62.md`)

Checker: Claude Opus 5.5 (laptop subagent), 2026-11-27. Cross-provider hand check of a gpt-6.2-astra max file. No Lean. One floating-point guide line (constants of (15a) and a rate margin), not a proof step. Nothing committed or pushed; no other file written.

## 0. Reading log

- FINISH.md rows 1624, 1625, 1626 (brief and RESULT) and 1627 (this brief): read.
- `library/gap-vir-down-dom-astra62.md` (row 1626): read in full, L1-214, line by line.
- `library/gap-vir-down-tool-astra62.md` (row 1624): read in full, L1-293.
- `library/gap-vir-down-tool-astra62-check-opus.md` (check 1625): read in full; (DOM) is its section 4.
- `library/open-registry.md` row VIR-DOWN (L1028): read.
- Spot checks of cited inputs: row 1611 degree-four join coefficient (`gap-direction7-astra62.md` L126-130: $J_t=1+(t^4/64)\sum_pw_pw_p+O(t^6)$, i.e. $(t/4)^4\sum_p\chi_p\chi_p$ with $\chi_p=2w_p$); row 1617 (2) (`gap-vir-down-astra62.md` L26-32: $\beta b_\psi\log m/m\to1$); row 1161 (19) (level count giving $m_1\le C_*$); row 1171 flat-shift remark (`gap-solve14-astra62.md` L34). Not re-derived: row 1568 Theorem E / row 1573 (4) (pin decoupling) and the oscillation bound $r(\beta)$ of `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (23)-(26) on PRs 10114/10133; both enter only (15a).

Notation as in row 1626: $S=S^0+2\kappa(P-P^2)$, $\mu_k$ with kernel $P^kSP^k$, $v=\lfloor t/2\rfloor$, $j=v-k-1$, $\mathcal M_k=\int L_{j+1}d\mu_k^+-\int D_jd\mu_k^-$, $d_i=\langle\psi_i,A'\psi_i\rangle$. Diagonal of $S$ on $f_i$: $2r_i[\kappa(1-r_i)-d_i]$.

**Convention warning.** In row 1626, "small bare coupling" means small $\beta$, i.e. **strong** coupling ($g^2=4/\beta$ large). The body says so ("strong-coupling counterexample", $0<\beta<\epsilon_n$; interval $\beta\in[1/512,1/128]$). The calibrated band is the opposite end, $\beta\ge\beta_K\to\infty$. Read the RESULT and FINISH wording with this in mind.

## 1. Line-by-line check of the PROVED items

### 1.1 Buffer-independent bound (1) and identity (2) — HOLDS

- $d_{j+1}=Pd_j$ by Chapman-Kolmogorov and symmetry of $p_1$. $L_{j+1}=\|EPd_j\|^2=\langle d_j,PEPd_j\rangle$, so $D_j-L_{j+1}=\|H^{1/2}d_j\|^2$ with $H=I-PEP$, $0\le H\le I$. HOLDS.
- (2): add and subtract $\int L_{j+1}d\mu_k^-$. $N_\pm$ trace class: $\operatorname{Tr}N_\pm\le\int D_jd\mu_k^\pm<\infty$ ($D_j$ bounded for $j\ge1$ on the box). HOLDS.
- $N_--N_+=2B$: for real $f$, $\langle f,(N_--N_+)f\rangle=-\int(\phi(x)-\phi(y))^2d\mu_k$ with $\phi=P^jH^{1/2}f$; zero marginals leave $+2\langle\phi,P^kSP^k\phi\rangle$; $j+k=v-1$. HOLDS.
- $\int L_{j+1}d\mu_k=V$: sum over an orthonormal basis of range$(E)$ (the constant contributes zero), $k+j+1=v$. HOLDS.
- $2\operatorname{Tr}B_+=\operatorname{Tr}J(N_--N_+)\le\operatorname{Tr}JN_-\le\operatorname{Tr}N_-$. HOLDS. Exact form: $\mathcal M_k=V-\operatorname{Tr}N_-$.
- Scope: the right side of (1) is buffer-free ($k$ enters only through $j+k$); it depends on the observation $E$ through $V$ and $H$. "Simultaneously for all buffers" is right; "and observations" means "for each observation, with its own $V,B$".

**Corollary (PROVED here, by me, from (1)).** Let $\{f_i\}_{i\in I_h}$ be excited eigenvectors with $Ef_i=0$ (exactly hidden). Then $Hf_i=f_i$ and $\langle f_i,Bf_i\rangle=r_i^{2v-2}\langle f_i,Sf_i\rangle=2r_i^{2v-1}[\kappa(1-r_i)-d_i]$. Since $\operatorname{Tr}B_+\ge\operatorname{Tr}(\Pi B\Pi)$ for the projection $\Pi$ onto those $f_i$ with nonnegative diagonal,
$$\mathcal M_k\le V-4\sum_{i\in I_h}r_i^{2v-1}\big[\kappa(1-r_i)-d_i\big]_+ .$$
Hidden levels slower than $\kappa$ are charged in full. Hidden levels faster than $\kappa$ give no credit. This is the exact form of the warning of check 1625 §3 (one hidden zero-slope cold level costs a constant fraction of the rate).

### 1.2 Rate ceiling (3) — HOLDS

- $P^v(P-P^2)P^v=P^{2v+1}(I-P)$ (commuting); $E$ finite rank, so cyclicity is legitimate. $V=-2\operatorname{Tr}(EP^vS^0P^v)-4\kappa a_E$. HOLDS.
- $a_E>0$: a nonconstant cell function has a nonzero excited component; $0<r_i<1$ by injectivity and simplicity of the Perron level. HOLDS.
- Strictness: $\operatorname{Tr}N_-=\int(D_j-L_{j+1})d\mu_k^-$; $D_j-L_{j+1}\ge D_{j+1}-L_{j+1}>0$ a.e. (row 1624 (14)); $\mu_k^-\ne0$ for $\kappa>0$ (row 1624 (14), buffered form) and $\mu_k^-\ll\pi\otimes\pi$. So $\mathcal M_k<V$, and $\mathcal M_k\ge0$ forces (3). HOLDS.
- Note: the numerator of (3) contains off-diagonal action matrix elements weighted by the overlaps $\langle f_i,Ef_l\rangle$. It is a measurable quantity by row 1624 (5), not a diagonal sum.

### 1.3 Observed-response truncation (4) — HOLDS

- The constant direction contributes zero to $V$ and $V_F$ ($P1=1$, $S1=0$, $F1=0$). $P^vSP^v=RSR$ with $R=P^vQ$; $F$ commutes with $P$. $\|RSR-FRSRF\|\le2s_nr_1^{2v}e^{-L}$, since $\|(I-F)R\|\le r_1^ve^{-L}$. The trace over $d=\operatorname{rank}(E-|1\rangle\langle1|)$ directions gives $4ds_nr_1^{2v}e^{-L}$. HOLDS. $\|S\|\le24n^3+\kappa/2$ is row 1624 (21). HOLDS.
- Second form: coldness gives $tm_1\ge\log2$, $W_t\ge(\log2)r_1^t/t$, and $r_1^{2v-t}\le e^{2m_1}\le e^{2C_*}$ (row 1161 (19), $k=1$). HOLDS.
- Size note: $\log d\le3\cdot32^3\log16\approx2.7\times10^5$ (guide). This is independent of $K$, as claimed. The window $O((1+\log n+\log(1/\eta))/t)$ hides this constant.

### 1.4 Negative-side truncation (5)-(6) — HOLDS

- Signed density after conditioning: $(\mathbb E[A|x,y]-\bar a)q_h-(P^kg(x)+P^kg(y))\pi\otimes\pi-2\kappa q_h+2\kappa q_{h-1}$. With $0\le A,\bar a\le b_n$ and $|g|\le b_n$, $\mu_k\ge-[(b_n+2\kappa)q_h+2b_n\pi\otimes\pi]$, so $\mu_k^-$ is below that measure, whose marginals are $c_n\pi$. HOLDS.
- $(f_i(x)-f_i(y))^2\le2f_i(x)^2+2f_i(y)^2$ gives $4c_nr_i^{2j}$ per level; $\sum_{m_i\ge a}r_i^{2j}\le e^{-(2j-1)a}G(1)$. HOLDS. (6) follows from $G(1)\le e^{12\beta n^3}$ (row 1619 TRUNC) and $W_t\ge(\log2)e^{-tC_*}/t$. HOLDS.
- The threshold (6) is of order $\beta n^2$ at $t\asymp n$. The author says this leaves a far wider range than (4). Correct; (5)-(6) are accuracy bounds with no sign.

### 1.5 Strong-coupling counterexample (7)-(10) — HOLDS (fixed $n$, $\beta\downarrow0$)

- (8): the electric kernel is separately gauge invariant at each end and diagonal in spin networks. Its order-$q$ Taylor coefficient has degree at most $q$ in each slice. The lowest nonconstant neutral single-slice invariants are the fundamental plaquette characters (degree 4); terms $1\otimes\chi_p$ vanish ($C1\propto1$); cross terms $\chi_p\otimes\chi_{p'}$, $p\ne p'$, vanish by diagonality. Row 1611's coefficient $(t^4/64)\sum_pw_pw_p=(t/4)^4\sum_p\chi_p\chi_p$ (spot-checked) gives $a=(\beta/4)^4$. The exact constant is irrelevant to (7). HOLDS.
- (9): from $\lambda'\Omega=M\langle M,\Omega\rangle+O(\beta^4)$ one gets $Q_\beta M=O(\beta^4)$, so $|Q_\beta M\rangle\langle Q_\beta M|=O(\beta^8)$, and $Q_\beta F_4Q_\beta=F_4+O(\beta)$ since $F_41=0$. Also $A-\Pi=QAQ$ because $A\Omega=\Omega$. HOLDS.
- (10): $A^s=\Pi+(aJ)^s$, $p_s-1=a^s(F_4+O_{n,s}(\beta))$; orthonormality of $\chi_p$ in Haar norm gives $a^{-2s}D_s\to D^{(4)}$ uniformly. $D^{(4)}>0$ Haar-a.e. HOLDS.
- Uniformity in $\kappa$: the normalized Haar-pair density lies in the unit sphere of span$\{s_0(\beta),s_1(\beta)\}$; the analytic Gram-Schmidt basis converges uniformly; the coefficient circle is compact. Every limit has zero mean and unit norm, so its negative part is nonzero and $\int D^{(4)}s_{*,-}>0$. With $\int s_+\le\|s\|_2=1$ and $D_{j+1}\le C_{n,j}a^{2j+2}$, the ratio is at most $K_n\beta^8$. Finitely many $(j,k)$ for $t\in[u,n]$. HOLDS.
- Nonvanishing of the density: diagonal $2r_i^{2k+1}[\kappa(1-r_i)-d_i]$ with $d_i/r_i\sim m_i/(\beta\log m_i)$ (row 1617 (2), spot-checked), so $d_i\to0^+$ and the diagonal is eventually nonzero for every $\kappa\ge0$. HOLDS.
- **Quantifiers.** $\epsilon_n,K_n$ depend on $n$ (the expansions are $O_n$). Nothing here is uniform in volume. The statement is at fixed size and strong coupling, as stated.
- **Mechanism.** At $\kappa=0$ the failure is only the asymmetric times $j+1$ (positive side) and $j$ (negative side): they differ by a factor $r^2\approx a^2=(\beta/4)^8$ because every level has $m\approx4\log(4/\beta)\gg1$.

### 1.6 Thermal rate on the same boxes (11) and the second sign check — HOLDS

- $J_\beta=F_4+O_n(\beta)$, $J'_\beta=O_n(1)$ in Hilbert-Schmidt norm ($R=\sum_{q\ge5}R_q\beta^q$, so $(R/a)'=O(1)$). $J_\beta\ge0$ by positivity of the transfer. $T_t=\operatorname{Tr}J^t$ is bounded above and below at fixed $n$ on $[u,n]$. Then $\partial_\beta X/(t\bar E_t)=\partial_\beta G/(tW_t)=(4/\beta+O_n(1))/(4\log(4/\beta)+O_n(1))\to\infty$. HOLDS. Purity: $Z(2u)/Z(u)^2\ge(1+G(u))^{-2}\to1$. HOLDS.
- Second sign check: $Q\Pi'Q=0$ gives $|d_i|\le\|(aJ)'\|=O_n(\beta^3)$; $r_i\le2a$. For fixed $\kappa>0$, $d_i<\kappa(1-r_i)$ on every excited level, so the complete contrast $\sum_ir_i^{t-1}[d_i-\kappa(1-r_i)]$ (row 1624 (10)) is negative. HOLDS.
- **Mechanism at $\kappa>0$.** The test certifies the one-step secant form $d_i/r_i\ge\kappa(e^{m_i}-1)$ on average. At strong coupling $e^m-1\approx(4/\beta)^4$, far above $m\approx4\log(4/\beta)$. So (VIR-down) at rate $8/3$ holds there while its secant form fails. This is a property of the test (one removed time step), not of the band.

### 1.7 Sector test (12) — HOLDS

$\operatorname{range}E\subset\operatorname{range}J$ gives $L_{j+1}=\|Ed_{j+1}\|^2\le\|Jd_{j+1}\|^2=\sum_{I_J}r_i^{2j+2}(f_i(x)-f_i(y))^2\le D_{*,J}\le D_j$ ($2j\le t-h<2j+2$). So $\mathcal M_k\le\int D_{*,J}d\mu_k=-2\sum_{I_J}r_i^{t-h+2k}\langle f_i,Sf_i\rangle=4\sum_{I_J}r_i^{t-1}[d_i-\kappa(1-r_i)]$, which is (12). HOLDS. The bound uses only diagonal elements in an eigenbasis. These do not change if the identification of Hilbert spaces across $\beta$ is changed by a $\beta$-dependent unitary, because the diagonal of a commutator $[A,X]$ in an eigenbasis of $A$ is zero. So (12) and (13) do not depend on the rescaled comparison coordinates.

### 1.8 Compact Gaussian U(1) with contractible loops (13), zero speed, interacting cosine — HOLDS

- A flat shift preserves every spatial plaquette, so it commutes with the gradient flow (equivariance) and fixes every contractible loop value. So cell functions are flat-shift invariant, i.e. in the charge-zero sector $J$, which commutes with $P$. There $m=E_{\rm ph}$ is $\beta$-independent (row 1618 Theorem 2, check 1622), so $d_i=0$. (12) gives (13) $<0$ for every $\kappa>0$, every buffer. HOLDS. The flat-shift fact for U(1) is ON FILE (row 1171, `gap-solve14-astra62.md` L34).
- Zero speed: $\mathcal M_k\le\int D_{*,J}d\mu_k-\int(D_j-D_{*,J})d\mu_k^-$; first term $0$; $D_j-D_{*,J}\ge e^{-2jm}(f(\Phi_x)-f(\Phi_y))^2>0$ a.e. for the hidden rotor $f=\sqrt2\cos2\Phi_1$ ($m=2/(\beta n)$, $d/r=m/\beta$); $\mu_k^-\ne0$. Strict. HOLDS.
- This is the hidden-mode mechanism of check 1625 in its extreme form: every observed mode has zero slope and every rate-carrying mode (the even rotors) is invisible. The invisibility is a symmetry fact (flat shifts); the strict deficit reads the transfer law ($\beta$-independent photon spectrum, rotor response). The author says the same (L154).
- Interacting weak cosine U(1): conditional on the periodic Villain input of row 1573/check 1579. The last-crossing mean-value point and (12) on the full space give a deficit $\ge4Z\log(63/50)/(tw)$ at that point. HOLDS as a conditional statement. It sharpens row 1624 L222 (a size at the same point), with the same input.

### 1.9 Characteristic test (14) — HOLDS

- $y=-\frac1t\log G$ along $t'=\kappa t$: $y'=-\kappa y-\partial_\beta G/(tG)+\kappa\langle m\rangle=-\Delta-\kappa[\langle e^m-1-m\rangle+y]$. Re-derived. HOLDS.
- $\langle m\rangle\ge y$ (entropy of $p_i=r_i^t/G$ is $t(\langle m\rangle-y)\ge0$); Jensen for the convex $\phi(m)=e^m-1-m$ and monotonicity on $m\ge0$ give $\langle\phi\rangle\ge\phi(y)$, so $y'\le-\Delta-\kappa(e^y-1)$. Then $q'\ge q\Delta+\kappa(1-q)$ and $Y'=(\kappa t/u)(1-q)-(t/u)q'\le-(tq/u)\Delta$. HOLDS.
- $\mathcal M_k\le4G\Delta$ is (12) with $J=I$, using $Z\partial_\beta X=\partial_\beta G$. HOLDS.
- Content: (14) is the characteristic form of the secant identity (10) of row 1624. For small $y$, $Y\approx-\log G/u$, so "Y nonincreasing" is to first order "G nondecreasing along the characteristic", which TR-down already uses. The exact form adds the secant correction, of relative size $O(m)$.

### 1.10 Fixed-interval counterexample (15a) — HOLDS, given two cited inputs

- Coldness: the pin factorization $e^{-\delta_n}f\otimes f\le K_s\le e^{\delta_n}f\otimes f$ at $s=\lceil\sqrt n\rceil$ (row 1573 (4), row 1568 Theorem E; not re-derived). From it: $\lambda_0^s\ge e^{-\delta}\|f\|^2$; $\sum_{i>0}\lambda_i^{2s}\le\|K_s-f\otimes f\|_{HS}^2\le(e^\delta-1)^2\|f\|^4$ (re-derived: expand and use $\langle f,K_sf\rangle\le\lambda_0^s\|f\|^2$). So $G(2s)\le e^{2\delta}(e^\delta-1)^2\to0$, also in the neutral sector (the vacuum is neutral). $G(t)\le G(2s)$ for $t\ge2s$; $2s\le u$ eventually. HOLDS.
- Hot end: $r_1\le r(\beta)$ from PRs 10114/10133 (not re-derived; a standard volume-uniform strong-coupling spectral bound of Osterwalder-Seiler type would serve equally). The pin factorization alone would not suffice: it gives only $r_1\le G(2s)^{1/2s}$, which may tend to one. At $b_*=1/128$ the denominator is $0.906>3/4$ (guide). $\limsup q(b_*)\le r(b_*)<4b_*/3$. HOLDS.
- $Y(b_*)\ge1+\delta$ with $\delta=[e^{2b_*}(1-4b_*/3)-1]/2\approx2.58\times10^{-3}$; $Y(b_*/4)\le1$; the mean value theorem and (14) give $\mathcal M_k\le-cG$ with $c=4e^{-2b_*}\delta/(3b_*/4)\approx1.74$ (guide). $c$ and $I$ are independent of $n$. HOLDS.
- **Quantifiers.** Fixed coupling interval $[1/512,1/128]$ first, then $n\to\infty$ (also along $n=\ell b^K$). Integrated speed $2b_*=1/64$, not $\log512$. Starting coupling fixed at $1/512$, not $\beta_K$. So these boxes are large Wilson boxes at fixed strong coupling. They are not on the calibrated trajectory. The author says so (L200, L208).
- **Mechanism.** At these couplings $q\approx r_1$ is tiny, so $Y\approx t/u$ increases along every characteristic. $\Delta\approx\partial_\beta\log r_1-\kappa\langle e^m-1\rangle$ is hugely negative. This is the same one-step-secant effect as 1.6: $e^m-1\gg m$ for $m\gg1$. The bound $cG$ is far below the true deficit.

### 1.11 Endpoint inequality (16), the two-state example, purity on the sequence — HOLDS

- (16) is $Y(\beta_h)\le Y(\beta_K)$ with $n/u=512$, valid when (15) holds at every point of a window kept cold by HOT and the last-crossing argument. HOLDS.
- Two-state example: $G=e^{-a}$ is constant on the characteristic, so the $m$-form rate holds with equality and HOT holds for $a>\log(21/4)$; $t(1-e^{-a/t})$ is increasing, so (16) fails; directly $\Delta=\kappa(m-e^m+1)<0$. HOLDS. The loss is relative $O(m)=O(a/t)$.
- Purity on the (15a) sequence: $G(u;1/512)\le G(2s)\to0$. HOLDS. The extension to $t=n$ keeps the same failing point. HOLDS.

I found no failing line in any PROVED item.

## 2. Does row 1624's test (15) survive on the calibrated band?

**Undecided. Row 1626 proves neither a failure nor a success on the band.**

**The two proved SU(2) failures do not reach the calibrated trajectory.**
- (7) holds at fixed $n$ for $\beta<\epsilon_n$, with $\epsilon_n$ depending on $n$. (15a) holds for $\beta\in[1/512,1/128]$ at every large $n$. The band is $\beta\ge\beta_K\to\infty$ with a window of integrated speed $\log512$ that starts at $\beta_K$. Neither statement constrains a single calibrated point.
- Both failures act through levels with $m\approx4\log(4/\beta)\gg1$. At $\kappa=0$ the cause is the factor $e^{-2m}$ between the positive-side time $j+1$ and the negative-side time $j$. At $\kappa>0$ the cause is the one-step secant $e^m-1\gg m$ in row 1624 (10). At a cold point on the band the thermal weight sits on levels with $tm=O(1)$, so $m=O(1/t)$. For these levels both effects cost a relative $O(1/t)$. Levels at lattice energies have total weight about $n^3e^{-Ct}$ with $t\ge n/512$ (row 1161 count); this is negligible. (ARGUED.) So these two mechanisms do not threaten the band.

**The mechanism that does matter on the band is the one check 1625 warned about. Row 1626 makes it exact but does not evaluate it.**
- (1) gives $\mathcal M_k=V-\operatorname{Tr}N_-$. My corollary in 1.1 shows that every exactly hidden level slower than $\kappa$ is charged its full deficit, and hidden faster levels give no credit. Check 1625's guide case (an unobserved zero-slope cold level, failure at $\kappa=1.2$ with thermal rate near $1.5$) is the special case of this corollary.
- (13) is the extreme instance in compact Gaussian U(1). There every observed level has zero slope and every rate-carrying level is hidden, so (15) fails at every rate.
- None of row 1626's SU(2) failures uses this mechanism.

**Partial hiding is unavoidable (PROVED here, short).** Every excited neutral eigenfunction $f_i$ is real analytic and nonconstant (row 1624 (14) proof). $Ef_i$ takes finitely many values. If $Ef_i=f_i$ a.e., then $f_i$ would take finitely many values a.e. That contradicts the null level sets of a nonconstant analytic function. So $\|Ef_i\|<1$ for every excited $i$. With a fixed finite partition, no level is fully seen.

**Size on the band (ARGUED, GUIDE only).** At the constant schedule $\kappa=8/3$ the largest plausible per-level surplus is at zero-momentum levels carrying the asymptotic-freedom rate $3\pi^2/11\approx2.692$. That surplus is about $0.9\%$ of $\kappa m$ (floating-point guide). Levels with nonzero momentum or relative momentum have rate below the mass rate (row 1610 §3.3 warning; check 1625 §3), so they are deficit levels. For (15) to pass at $8/3$, the hidden part of the deficit levels must therefore cost less than this thin surplus. That needs the $3\cdot32^3$ flowed loops to see almost all of the cold thermal weight. At lower order-one rates (for example $2.3$ with a longer bare window) the margin is wider, and the question is open. No estimate on file or in row 1626 bounds the hidden fraction for Wilson.

## 3. Is registry row VIR-DOWN touched?

**No. Only row 1624's sufficient test (15) is constrained.**
- On the band, nothing in row 1626 proves or refutes the thermal (VIR-down) at an order-one rate. (11) proves the pointwise thermal inequality at strong coupling and fixed $n$. That is off the band and irrelevant to the registry row. The U(1) statements concern (15) and use on-file thermal facts (row 1618 Theorem 2).
- What is new about the test: (7) with (11) is the first **Wilson-box** separation of (15) from pointwise (VIR-down). Check 1625 had this only in abstract positive families. It holds at fixed $n$ and strong coupling, so equivalence of (DOM) with (VIR-down) on the calibrated band is still open. The two-state example after (16) separates the characteristic/secant restriction from the thermal rate.
- Relation to the seed: (7) and (15a) show that same-box purity near one does not force (15) off the trajectory. On the calibrated trajectory the converse is still open, as the author says (L160). (DOM) is not shown equivalent to (PUR-io), and is not shown inequivalent there.
- Registry status stays "open; no sign or size proved". A one-line note could record: "row 1626: test (15) fails off-band at strong coupling ((7), (15a)) and, for contractible loops, at every rate in compact Gaussian U(1) ((13)); band undecided." I have not edited the registry.

## 4. New and on file

| Statement | Standing |
|---|---|
| (1), (2), and the hidden-level corollary (1.1 here) | New. Built on row 1624 (7), (15), (16). |
| (3), rate ceiling from observed predictors | New. Uses row 1624 (5), (14). |
| (4) | New. Inputs ON FILE: row 1161 (19) ($m_1\le C_*$), row 1624 (21). |
| (5), (6) | New application of row 1619 TRUNC to the Jordan negative part. |
| (7)-(10), strong-coupling failure | New. Inputs ON FILE: row 1611 degree-four join coefficient (Sussman-Alpoge GL3), row 1617 (2) (check 1621). |
| (11), second sign check | New, standard strong-coupling expansion at fixed $n$. |
| (12), sector test | New. Generalizes row 1624 (16), (18). |
| (13), zero-speed U(1) | New. Inputs ON FILE: flat-shift observation (row 1171, `gap-solve14-astra62.md`), row 1618 Theorem 2 and check 1622. |
| Interacting cosine U(1) | ON FILE inputs (rows 1573, 1579, 1617 (13)); a deficit size at the same point is added. Same route as row 1624 L222. |
| (14), (16) and the two-state example | New, as a characteristic form of row 1624 (10). Monotone transport of $G$ is ON FILE (rows 1610, 1613). |
| (15a) | New. Inputs ON FILE: row 1568 Theorem E / row 1573 (4) (pin decoupling, checked 1572), row 1611 pin benchmark, $r(\beta)$ of PRs 10114/10133. I did not re-derive these inputs. |
| Partial hiding $\|Ef_i\|<1$ (section 2 here) | New here, short. Uses row 1624 (14) analyticity. |

## RESULT

Check 1627, Claude Opus 5.5 hand check of row 1626 (gpt-6.2-astra max). No Lean; one float guide line, not a proof step.
(1), (2), (3), (4), (5)-(6), (12), (14): HOLD. (1) gives a corollary: an exactly hidden level slower than kappa is charged its full deficit, and a faster one gives no credit.
(7) with (11): HOLDS at fixed n for beta < eps_n. Here "small bare coupling" means small beta, i.e. strong coupling. The failure comes from the j+1 versus j asymmetry and the secant e^m - 1 >> m at m ~ 4 log(4/beta).
(15a): HOLDS on [1/512, 1/128] for all large n, with c ~ 1.74 (guide), given the cited pin bound (row 1568/1573) and r(beta) (PRs 10114/10133). It uses the same large-m secant effect, at fixed strong coupling.
(13) and zero speed, compact Gaussian U(1) with contractible loops: HOLDS at every kappa >= 0. This is check 1625's hidden-mode mechanism in extreme form. The interacting cosine case is conditional on the Villain input.
GUESSED domination on the calibrated band: still GUESSED. Neither proved SU(2) failure reaches beta >= beta_K. Their mechanisms cost only O(1/t) at the cold scale.
So the test (15) is undecided on the calibrated band at every order-one rate. The live threat there is the hidden-level charge in (1). Every excited level is partly hidden (||E f_i|| < 1). At kappa = 8/3 the plausible surplus is about 1% (guide), so passing needs near-complete visibility.
VIR-DOWN itself is untouched; only row 1624's sufficient test is constrained. New: the first Wilson-box separation of (15) from pointwise VIR-down, off the band.
Overall: row 1626 holds as stated, with no failing line. Outcome (d) stands for the calibrated target. No open input moves: (DOM) on the band, (HOT), (PUR-io) and the gap remain open.
