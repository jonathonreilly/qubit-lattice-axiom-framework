# Check of row 1341 (gap-blockstep-astra62.md), FINISH row 1344

Checked line by line by hand by Claude Opus 5.5. Target: `library/gap-blockstep-astra62.md` (row 1341, gpt-6.2-astra).
It targets the block step of Proposition CH (Section 6.1 of `library/gap-shrink-box-fable.md`, as corrected by
`library/gap-shrink-box-check-astra.md`). The independent attempt `library/gap-blockstep-fable.md` was not read.
Numeric runs, where used, only guided; no verdict rests on one.

Line numbers refer to the target file as committed at `03244fd1d`.

## Scope

The file marks 44 statements PROVED (lines 15 to 424). Items 1 to 8 cover 14 of them: lines 191, 229, 245, 256, 424, 204, 316, 322, 330, 338, 348, 365, 395 and 385.
Item 9 covers the other 30, one verdict per statement.

## 1. Exact mass-preserving cubical map, lines 191–198, (13). HOLDS.

I re-derived the geometry. A plaquette lies in 4 unit four-cells (two transverse axes, two sides each). A four-cell has $\binom42\cdot4=24$ plaquettes. So quarter weights per cell give each torus plaquette its full weight.
A link of $[-1,1]^4$ in direction $\mu$ avoids the boundary only if its three transverse coordinates are $0$. Hence the interior links are exactly the 8 spokes from the origin.
A plaquette not in the boundary has both transverse coordinates $0$. Both its intervals then meet $0$, so it has the origin as a corner. There are $8\cdot6/2=24$ such plaquettes, one per perpendicular pair $\{a,b\}$. Each lies in four cells, all inside the block, so it carries the full coefficient $\beta$.
The loop $0\to a\to a+b\to b\to0$ reads $U_aV_{ab}V_{ba}^{-1}U_b^{-1}$. This is (13) with $H_{ab}=V_{ab}V_{ba}^{-1}$, on the graph $K_{2,2,2,2}$.
Spokes of different blocks are distinct links. A spoke meets only plaquettes through its block centre. So Fubini gives the exact product over blocks, separately on each torus.
Mean one: each factor has a private far link, and Haar invariance gives $\int w_\beta=1$.
Far link $V_{ab}$ has the $a$-coordinate fixed at $\pm1$ and the $b$-coordinate in a unit interval. So it lies in the relative interior of face $a$ and outside the coarse two-skeleton. This agrees with Lemma STAR of `gap-blockcrit-opus.md` (Opus lane), line 172.

Precision (no change to the claim). The block $[-1,1]^4$ needs torus sides at least 4. On side 2 its opposite faces coincide and the 48 far links are not distinct. The CH tori have even sides $2n\ge6$, so the claim holds where it is used.

## 2. Pfaffian identity (16) and coefficient formulas (17)–(18), lines 229–254, with the checks at line 424. HOLDS.

**Spinor form, line 229.** For $x=x_1+x_2j$ and $h=h_1+h_2j$ one has $xh=(h_1x_1-\bar h_2x_2)+(h_2x_1+\bar h_1x_2)j$. So $R_h$ has columns $(h_1,h_2)^t$ and $(-\bar h_2,\bar h_1)^t$, with determinant $|h|^2=1$. The real inner product on $\mathbb R^4$ is $\operatorname{Re}$ of the Hermitian one. Hence $\beta q(U_aHU_b^{-1})=\beta\operatorname{Re}(z_b^*R_Hz_a)=z_b^*M_{ba}z_a+z_a^*M_{ab}z_b$. No factor of two is left. $R_{H^{-1}}=R_H^*$ makes $H_{ba}=H_{ab}^{-1}$ consistent with $M_{ab}=M_{ba}^*$.

**(16).** I checked $\bar RJ_2=J_2R$ by direct multiplication for $R\in SU(2)$. This is the block form of $M^tJ=JM$. $T^{-1}$ commutes with $J$. So $(J(T^{-1}-M))^t=-J(T^{-1}-M)$, and the matrix is skew.
$\operatorname{Pf}^2=\det J\det T^{-1}\det(1-TM)$ with $\det J=1$ and $\det T^{-1}=\prod t_a^{-2}$. This gives $P^2=\det(1-TM)$.
A factor $t_a^{-1}$ sits only in the $2\times2$ diagonal block of site $a$. A perfect matching uses that pair at most once. So $P$ is a multiaffine polynomial, and $P(0)=\operatorname{Pf}(J)=1$.
Expanding the Pfaffian of a block-diagonal part plus $-JM$ gives $[t^S]P=\operatorname{Pf}((-JM)_S)$, with no sign because the site pairs are adjacent indices.
The real-coefficient argument is sound: $P^2>0$ near $0$, $P(0)=1$, and continuity give $P$ real on an open set.
The subset recursion by the partner of the first index uses at most $16\cdot2^{16}$ terms.

**(17).** For Hermitian $K<1$, $\mathbb E\exp(z^*Kz)=\det(1-K)^{-1}$. Take $K=T^{1/2}MT^{1/2}$, so $\det(1-K)=\det(1-TM)=P^2$. $|z_a|^2$ is Gamma(2,1), so $\mathbb E|z_a|^{2k}=(k+1)!$. Expand the 24 edge exponentials. Odd site degree vanishes by $\omega_a\mapsto-\omega_a$. Degree $2k_a$ supplies $t_a^{k_a}(k_a+1)!$. Summing the same spherical terms without $t$ is $Z_\square$. The edge sum is absolutely convergent by $e^{24\beta}$, so the regrouping by $\mathbf k$ is legitimate. For small $t$ the Gaussian side converges absolutely, so the coefficient identity holds.

**(18).** $P_1(0)=0$ because the site-0 block of $M$ is zero. $P^{-2}=P_0^{-2}\sum_{k_0}(k_0+1)(t_0P_1/P_0)^{k_0}$. Dividing by $(k_0+1)!$ and summing gives $G=P_0^{-2}e^{P_1/P_0}$. Each coefficient of $G$ is a finite sum, because $P_1$ has no constant term.
$C(H)$ omits exactly the multi-indices with some $k_i\ge46$, $1\le i\le7$. At that vertex the degree is at least 92.
With $|q|\le1$, the omitted absolute sum is at most $7e^{18\beta}\sum_{h\ge91}(6\beta)^h/h!$. At $\beta=7/3$: $14e/91<0.42$, ratios $14/92<1/2$, $e^{42}<2^{61}$, and $7<2^3$. The total is below $2^{-24}$, and it is monotone in $\beta$.
Jensen gives $Z_\square\ge e^0=1$, because every edge trace has Haar mean zero. Hence $C>0$, and the enclosure factor $(1-2^{-24})^{-1}$ follows. $23/10<7/3$.
The bound is on $Z_\square=A(\beta)^{24}I$. Since $A\ge1$, the same absolute bound holds for $I$.

**Line 424, first check.** One edge of strength $s$ gives $\det(1-TM)=(1-t_1t_2s^2/4)^2$, since $R^*R=1$. So $P=1-(s^2/4)t_1t_2$. $[(t_1t_2)^k]P^{-2}=(k+1)(s^2/4)^k$. Dividing by $(k+1)!^2$ gives $(s^2/4)^k/(k!(k+1)!)$, and the sum is $A(s)$. HOLDS.

**Line 424, second check.** Each Taylor order of $w_\beta(u_au_b^{-1})-1$ has zero mean in either spoke. So supports with a degree-one vertex vanish. At order $\beta^3$ only triangles survive. For one triangle, $\mathbb E(u_a\cdot u_b)(u_b\cdot u_c)(u_c\cdot u_a)=\tfrac14\mathbb E(u_a\cdot u_c)^2=1/16$. With 32 triangles, (20) starts with $2\beta^3$. Since $r=\beta/4+O(\beta^3)$, $128r^3$ has the same leading term. HOLDS.

## 3. Uniform enclosure on $0\le\beta\le7/3$ with error below $2^{-24}$ and fewer than $7\cdot10^{14}$ gates, lines 15, 245–262. HOLDS.

The error bound and uniformity over the boundary are item 2. Here I recount the gates.

**Recurrences.** $\log G=-2\log P_0+P_1/P_0$. Applying $D$ and multiplying by $P_0G$ gives $P_0DG=(DP_1-2DP_0)G-(DP_0)Y$ with $Y=P_1G/P_0$. This is line 258.
At index $\mathbf k\ne0$ the left side is $|\mathbf k|G_{\mathbf k}+\sum_{\mathbf j\ne0}(P_0)_{\mathbf j}|\mathbf k-\mathbf j|G_{\mathbf k-\mathbf j}$. $DP_0$ and $DP_1$ have no constant term. So $G_{\mathbf k}$ needs only lower indices.
Then $Y_{\mathbf k}=(P_1G)_{\mathbf k}-\sum_{\mathbf j\ne0}(P_0)_{\mathbf j}Y_{\mathbf k-\mathbf j}$, using $(P_0)_0=1$ and $(P_1)_0=0$.
Predecessors $\mathbf k-\mathbf j$ with $\mathbf j\ge0$ stay in the box $[0,45]^7$.

**Count per index.** There are five convolutions with arrays of at most $2^7-1=127$ nonconstant multiaffine coefficients: $P_0\cdot(|\cdot|G)$, $D(P_1-2P_0)\cdot G$, $DP_0\cdot Y$, $P_1\cdot G$ and $P_0\cdot Y$. That is at most $5\cdot127\cdot2=1270$ gates.
The rest is at most 10 gates: the subtractions, one division by $|\mathbf k|$, one product to store $|\mathbf k|G_{\mathbf k}$, and one multiply-add with the constant $1/\prod(k_i+1)!$.
So 1,500 gates per index is a safe bound.

**Total.** $46^7=435{,}817{,}657{,}216<4.5\cdot10^{11}$. Then $1500\cdot46^7<6.54\cdot10^{14}$.
The Pfaffian stage has at most $16\cdot2^{16}\approx1.05\cdot10^6$ complex multiply-adds, about $10^7$ real gates. The 24 quaternion products for $H_{ab}$ and the arrays $D(P_1-2P_0)$ and $DP_0$ add fewer than $10^5$ gates.
The total stays below $6.6\cdot10^{14}<7\cdot10^{14}$.
Every division is by a nonzero integer constant, $|\mathbf k|$ or a factorial. With rational $\beta$ the circuit is straight-line with rational constants, and its inputs are the real boundary coordinates. "Rational arithmetic gates" should be read in that sense.

The file states that peak memory, bit cost and Lean replay are unmeasured, and that no circuit was run. I confirm that the count is in scalar arithmetic operations only.

## 4. Forty-nine boundary modes across one face, (14), lines 204–223. HOLDS (read at each fixed two-skeleton).

**Test families.** Face $a$ has 6 neighbours and $15-3=12$ perpendicular pairs. That gives $12\cdot4+1=49$ tests per side.
In face $a=\{x_1=1\}$, the links outside the coarse two-skeleton are exactly the six far links $V_{ad}$. So $P_{bc}=V_{ac}^{-1}V_{ab}$ is on side $a$. $Q_{bc}$ uses only links of faces $b$ and $c$.
Conjugation by $V_{ac}$ sends $H_{ab}H_{bc}H_{ca}$ to $P_{bc}Q_{bc}^{-1}$. I checked this by expanding the word.
Under reference Haar each $P$ and $Q$ is Haar. Distinct pairs share at most one index, so one test has a private link with centered coordinates. Both families are orthonormal.

**(15).** Take $S=\{a,b,c\}$. Each edge with an endpoint outside $S$ has a private far link outside $S$. That edge integrates to 1, and the face-$a$ links $V_{ad}$, $d\notin\{b,c\}$, drop out. The remaining density is $w_\beta^{*3}(PQ^{-1})$ with $P,Q$ independent Haar.
$\int w_\beta(X)X\,dX=r$, so convolution multiplies the linear coordinates by $r$. This gives $4r^3\mathbb E Q_iQ_j=r^3\delta_{ij}$.
Different pairs: take $d$ in the left pair only. Integrating $V_{da}$ removes edge $\{a,d\}$. $V_{ad}$ is then free and centers the left test. The right test does not read $V_{ad}$.
Constants: the one-face marginal is 1. For the right side, see the next paragraph.

**Norms under $I$.** Left: the one-face marginal is 1. Right: integrating face $a$ removes the six edges at $a$. The six $V_{da}$ are then free Haar. Each $Q_{bc}$ is conditionally Haar, and two pairs differ in a private $V_{xa}$. So the Gram matrix in $L^2(I)$ is the identity on both spans.

**Conclusion.** $|I-H|\le(E-1)I$ follows from $H/E\le I\le EH$. Weighted Cauchy–Schwarz bounds the pairing matrix of $I-H$ by $E-1$. Some unit vector is killed by the rank-48 pairing matrix of $H$, while (15) has least singular value $r^3$.

**Reading.** The rank-48 decomposition of $H$ may depend on the skeleton. A mixture over skeleton values of rank-48 pairing matrices need not have rank 48. So the argument must run at each fixed skeleton value, for almost every value, after disintegration. This works: $I$ and the tests do not read the skeleton, and the face interiors are independent Haar at every skeleton value. The statement says "after fixing the two-skeleton", so no correction is needed. The proof text should say it is applied at fixed skeleton.
The removed boundary factors are, at fixed skeleton, products of one-face functions. So they preserve the rank.
At $\beta=23/10$: $r(2)>2/5$ by hand (line 89; I checked $A'(2)\ge2/3$, $e^{1/2}<5/3$), and $r$ increases. So $r^3>8/125$.

## 5. Gluing certificate (22)–(23), lines 316–328. HOLDS.

**(22).** By Cauchy–Schwarz in the shared variables, $|(P\star Q)(x,z)|^2\le\int P(x,y)^2dy\int Q(y,z)^2dy$. Integrating gives $\|P\star Q\|_2\le\|P\|_2\|Q\|_2$.
$K_1\star K_2-A_1\star A_2=(K_1-A_1)\star A_2+A_1\star(K_2-A_2)+(K_1-A_1)\star(K_2-A_2)$. With $\|A_1\star A_2-cA'\|\le\delta$ and division by $c$, this gives (22). The contraction is exact integration, so each torus mass is kept, with $c$ carried in the scalar. No positivity is used.

**(19) and the dictionary.** $\int A(|y|)^2d\gamma_\beta=\mathbb E_{u,u'}e^{\beta|u+u'|^2/2}=e^\beta A(\beta)$. So $\lambda_\beta$ is a probability.
$\int k_y(v)k_y(v')d\lambda_\beta=e^{\beta(2+2v\cdot v')/2}/(e^\beta A(\beta))=w_\beta(vv'^{-1})$. At fixed radius, $k_y(v)$ has angular mean 1. So the Gram entries are as stated.

**(23).** $\langle J_o,\Phi_U\rangle=\int du\prod_{p\ni o}w_\beta(v_p(u)v_p(U)^{-1})$. Substituting $u_a=U_ag_a$ (or $g_aU_a$, per orientation) and using conjugation invariance of $q$ turns this into the flat integral $Z_\square(\mathbf1;\beta)/A^{24}$ for every $U$.
By (20), $\|J_o\|_2^2=Z_\square(\mathbf1)/A^{24}$, and $\sum b_i=1$. Then $\|J_o\|^2-2\langle J_o,A_0\rangle+\|A_0\|^2$ is (23). Distinct bonds are independent, so $\langle\Phi_{U_i},\Phi_{U_j}\rangle$ is the product of one-bond Gram entries.
Existence: $\|\Phi_U-\Phi_{U'}\|^2=2(e^\beta/A)^{24}-2\prod_pw_\beta(\cdot)$ is continuous and vanishes on the diagonal. $J_o$ is the Bochner average of $\Phi_U$. Rational Riemann sums approximate it. This proves existence only, with no length bound, as the file says.

**Merge formula, line 332.** $A_1\star A_2=\sum d_{ij}l_ir_j$, so $\|A_1\star A_2\|^2=\sum d_{ij}d_{i'j'}L_{ii'}B_{jj'}=\operatorname{tr}(d^tLdB)$. HOLDS.

## 6. Obstructions (24), lines 338–346, and (27), lines 365–383. Both HOLD.

**(24).** At an odd corner $o$ of an even block, with outward spoke $a$ and any other direction $\nu$, the opposite odd corner is $o+a+\nu$. Its $a$-coordinate leaves $C$. So every plaquette using an outward spoke is external, and an odd block corner exists for every even $B\ge2$.
Integrate the other external bonds (angular mean 1) and the internal bonds by (19). The three outward spokes then appear only in the three test factors. So the marginal is $m_C\,T$, where $T$ is the triangle factor. Since $\mathbb ET=1$, $m_C=\mathbb EK_C$.
At fixed radii, $\langle T-1,\chi_\triangle\rangle=2\prod_er(t_e)$. The reason: given the spokes, each angle has mean $r(t_e)v_e$, and the spoke products multiply to 1.
$\mathbb E_{\lambda}r(|y|)^2=r(\beta)$: the two conditional means give $r(|y|)^2$, and (19) gives the unconditional $\mathbb E\,v\cdot v'=r(\beta)$.
Projecting at fixed radii and then integrating gives $\|T-1\|^2\ge4r^3$.
Write $K_C/c-1=(t-1)+t(K_C/m_C-1)$ with orthogonal terms. Conditional expectation contracts. So $\|K_C/c-1\|^2\ge(t-1)^2+4r^3t^2\ge4r^3/(1+4r^3)$, with the minimum at $t=1/(1+4r^3)$. For $\beta\ge1$ this is $>4/129$. HOLDS.

**(25) and the component laws, used by (27).** A double-crossing bond at $o$ joins two outward spokes, and $D(o)$ has at most one direction per axis when $B\ge2$. Integrating single-crossing bonds sets their factors to 1. The internal plaquettes read only inward spokes. So $\int K_C\,d\lambda_{\rm single}=m_C\prod_oP_o$, and $\mathbb E P_o=1$ fixes the constant as $m_C$.
The flip components are the parity-allowed vertices of a binary $k$-cube. Their normalizer is the free unit $k$-cube Wilson integral, by (19). HOLDS.

**(27).** Under $R_C\,d\mathrm{ref}$, the factors $\prod_{o\in C}P_o$ cancel against the component densities. So $Y$ has its reference law. At fixed $Y$ and radii, the outward spokes at $o$ have density $\prod k/P_o$. The two test angles, given the spins, have means $r(t_1)u_1u_l^{-1}$ and $r(t_2)u_lu_2^{-1}$. Quaternion multiplication is bilinear, so $\mathbb E[Q\mid\cdot]=r(t_1)r(t_2)u_1u_2^{-1}$, and $u_l$ cancels.
Hence $\mathbb E_{R_C}f=r(\beta)^2\mathbb E|m|^2$. Under the reference $Q$ is Haar, so $\mathbb E_{\rm ref}f=0$ and $\|f\|^2=r(\beta)^2\mathbb E|m|^2/4$.
This gives $\|R_C-1\|_2\ge2r\sqrt{\mathbb E|m|^2}$.
In the cube reference with spokes restored, $y_{12}$ given the spokes is $N(\beta(v+v'),\beta\mathbf1_4)$. The tilt $A(|y|)^2$ cancels the $k_y$ normalizers. So $\mathbb E\,m\cdot y_{12}=\beta(1+p)$ and $\mathbb E|y_{12}|^2=4\beta+2\beta^2(1+p)$, with $0\le p\le1$ by convexity of $\log Z$.
Cauchy–Schwarz gives $\mathbb E|m|^2\ge\beta(1+p)^2/(4+2\beta(1+p))\ge\beta/(2(2+\beta))\ge\beta/(4(1+\beta))$. The file's bound is weaker than the direct one, but valid.
For $\beta\ge1$, $r>1/5$ and $\sqrt{\beta/(1+\beta)}\ge1/\sqrt2$. HOLDS.

(24) far exceeds the $L^2$ allowance $(64\cdot81)^{-1}$ of line 336. (27) far exceeds the $L^8$ allowance of (26), since $\|\cdot\|_8\ge\|\cdot\|_2$. Both obstructions hold at every even $B$, as claimed.

## 7. Sheet bound (28)–(29), lines 395–418, with $r_1<49/100$, $r_2<9/50$, $d_*<1/4$. HOLDS.

**Sources.** I read the Sussman–Alpoge outline (with Claude and Codex) at lines 2197–2239 in a copy byte-identical to the pinned `31a47c543775`. GL3 gives $c_l=2e^{-\beta}I_{2l+1}(\beta)/\beta$, so the normalized coefficient is $r_j=I_{j+1}/I_1$ with $j=2l$. GL4 gives $I_{n+1}/I_n\le\beta/(2(n+1))$.

**(28).** $w_\beta=\sum_j(j+1)r_j\chi_j$ and $\chi_j*\chi_k=\delta_{jk}\chi_j/(j+1)$. So $w_\beta^{*4}=\sum(j+1)r_j^4\chi_j$. Then $\int\chi_j(huh'^{-1}u^{-1})du=\chi_j(h)\chi_j(h')/(j+1)$. The first equality is the standard tube reduction by vertex frame changes.
$A=2I_1/\beta$ and $(I_1/\beta)'=I_2/\beta$ give $r_1=A'/A=r$. $E_w\chi_2=E_w(4q^2-1)=4a-1=3r_2$ gives $r_2=\tau$.

**Constants at $\beta=7/3$, $x=7/6$, $Y=49/36$, $z=11/8$.**
- $A\ge1+Y/2+Y^2/12+Y^3/144=1.85245\ldots>37/20$.
- $I_2/x=x\sum_kY^k/(k!(k+2)!)$. The terms are $1/2,1/6,1/48,1/720$. From $k=3$ the ratio is $Y/((k+1)(k+3))\le Y/24<1/16$. The bound evaluates to $0.90114<181/200$.
- $I_3/x=Y\sum_kY^k/(k!(k+3)!)$. The terms are $1/6,1/24,1/240,1/4320$, and the ratio is below $1/16$. The bound evaluates to $0.31966<33/100$.
- So $r_1<(181/200)(20/37)=0.4892<49/100$, and $r_2<(33/100)(20/37)=0.1784<9/50$.
- Both increase in $\beta$: $r$ by the variance of $\log A$, and $a=A''/A$ by the covariance argument at line 157. So the bounds hold on $[0,7/3]$. GL4 holds for every $\beta\le7/3$ with $\beta/2\le7/6$.
- Term ratio for $j\ge2$: $((j+2)/(j+1))^2(7/(6(j+2)))^4\le(16/9)(7/24)^4=0.01286<1/64$.
- $d_*=4(0.49)^4+(64/63)\cdot9(0.18)^4=0.2306+0.0096=0.2402<1/4$.

**Dobrushin step, line 418.** On a sheet with two near-cut axes $\mu,\nu$, the $k=2$ groups point along $\pm\rho,\pm\sigma$. That is at most four.
The ratio of the two conditional weights lies in $[a,b]=[(1-d_*)/(1+d_*),(1+d_*)/(1-d_*)]$.
The chord bound with $\mathbb E\,t=s$ gives total variation at most $(b-s)(s-a)/(s(b-a))$. This is maximized at $s=\sqrt{ab}=1$, with value $(b-1)/(b+1)=d_*$.
The row sum is at most $4d_*<0.961<1$.
This covers only the crossing-only reference with $k\le2$ groups. The file marks the $k=3,4$ groups and the interior plaquettes OPEN.

Numeric guide only (no proof step): series values $r_1(7/3)=0.4841$, $r_2(7/3)=0.1701$, and $\sum_{j\ge1}(j+1)^2r_j^4=0.2273$.

## 8. Entry obstruction from the first-passage definition, line 428 with lines 385–389. HOLDS (conditional on the account's premises, in the stated scope).

**Sources.** I read the Sussman–Alpoge texts (with Claude and Codex) in copies byte-identical to the pinned `31a47c543775`. In the outline, lines 6854–6861 set $x_0=\beta$ (the bare inverse coupling) and define the first-passage data.
CA-I 56439–56458 give $\lambda_\sharp(j-i)-c_5\le x_i-x_j$ for $0\le i\le j\le K$. CA-I 56530–56547 give $x_k>g^{-2}$ for $k\le K$. Both hold under the stated hypotheses.
So $\beta=x_0\ge g^{-2}+\lambda_\sharp K-c_5\to\infty$ on the cutoff tail. Row 1335 (line 114) reached the same divergence from CA-I 3636–3659. This part restates it.

**Fixed-rank error, lines 385–389.** In the triangle marginal under $J_o$, the radii have the reference law, because the angles integrate to 1. Tilting the Gaussian by the increasing $A(t)^2$ stochastically increases the radius. Its scale is $\sqrt\beta$, so the radii tend to infinity in probability.
The cap bound is right: $A(t)\ge e^{t(1-\eta/2)}|{\rm cap}_{\eta/2}|$. Outside the $\eta$-cap the density is at most $e^{-t\eta/2}/|{\rm cap}_{\eta/2}|$.
So $(x,z)\to(X,X)$ in law, with $X$ Haar. For bounded continuous $f_i$, the pairing matrix tends to $\delta_{ij}$.
The reference measure is a product, so a rank-$q$ approximant across the one-bond cut gives a pairing matrix of rank at most $q$. On its null space of dimension at least $m-q$, the difference matrix acts as about the identity. Bessel's inequality gives squared error at least $(m-q)(1-o(1))^2$. Since $m$ is arbitrary, the error tends to infinity. HOLDS.

**The entry claim.** A list of $R$ product atoms has separation rank at most $R$ across the one-bond cut. So a list of bounded length cannot meet a fixed absolute $L^2$ input tolerance in (22) at bare couplings tending to infinity. The deduction is valid.
Scope, as the file states: this rules out a uniform bounded-rank absolute-$L^2$ initialization in the auxiliary scheme at the bare scale. It does not rule out relative or growing-rank inputs, or entry at the account's last scale. The remaining sentences of line 428 are OPEN statements, and I make no verdict on them.

## 9. Everything else

- **Line 15 (summary).** HOLDS. It matches items 1 to 4 and 6.
- **Lines 23–29, six-staple step.** HOLDS. $\int\prod_iw_\beta(uv_i^{-1})du=\int e^{\beta u\cdot\sum v_i}du/A^6=A(\beta|\sum v_i|)/A^6$. Each plaquette holds exactly one marked link, so the marked links integrate independently. There are $6|P|$ plaquettes, and the six staples of a star are disjoint triples.
- **Lines 35–44, (1) implies (2).** HOLDS. The degree is $D\le18\cdot5=90$.
- **Lines 46–62, nonvanishing.** HOLDS. The identity for $Q_A$ follows by splitting off the component of $v$. Finner's inequality applies with exponent 6, since a link lies in at most 6 stars. There are at most $(4D)^{k-1}$ rooted connected sets. $8eDb<3/8$ and $2eb<3/(32d)$ give ratio deviation $<0.15/d<1/(2d)$. Then $e^{-1/d}\le1-1/(2d)$ closes the induction.
- **Lines 64–66, short-coefficient cancellation.** HOLDS. A cluster of $k<n/8$ stars lies in a box of side $4k-1<n$, so it lifts. Cauchy on $|z|=2$ with total bound $2(Ln)^4/d$ gives (2) exactly.
- **Lines 70–79, (3)–(4).** HOLDS. The coordinate density is $(2/\pi)\sqrt{1-x^2}$, and its even moments are the Catalan numbers over $4^k$. $\mathbb EA(t|S_j|)=A(t)^j$ follows by averaging over a direction.
- **Lines 81–83, error and count.** HOLDS AFTER CORRECTION (wording). The tail $(27/129)^{258}<2^{-516}$, the ratio $81/(130\cdot131)<1/2$, the final $2^{-280}$ and the count below $10^8$ all hold. Correction: the sentence "the attempted local predicate … is the rational upper endpoint … strictly below $(64\cdot91)^{-6}$" literally asserts an inequality that (5) refutes at $23/10$. It should read: "the predicate is the statement that this endpoint is strictly below $(64\cdot91)^{-6}$; by (5) it is false."
- **Line 85, (5).** HOLDS. The $2v_i\cdot v_j$ are orthonormal and each pairs with $F$ to $2r^2$. With $r(1)>7/32>1/5$ and $r(2)>2/5$ (checked), the normalization argument with $1/c>1-b$ is right.
- **Line 91, (6).** HOLDS. $\mathbb E(u\cdot u')^6=6!/(4^33!4!)=5/64$, so the norm is $\sqrt{320}\,r^6=8\sqrt5\,r^6$. Every function that omits a staple is orthogonal to the six-fold products of centered coordinates.
- **Line 107, table test (7)–(9).** HOLDS. It is a definition, with no hidden claim.
- **Line 126, propagation.** HOLDS. $J\in[E^{-2}B,E^2B]$ by positivity, and (9) gives $E'=E^2D_0$. The tilt $u^+u^-/b$ on each new bond, with one bond per direction per new cell, gives the scalar $s_0^2c\prod b_\mu$ and exact masses.
- **Line 134, (10) and endpoint.** HOLDS. $|h|\le\max(\eta,1-1/E_N)=\eta$. The cell graph has degree 8.
- **Line 140, size.** HOLDS. $6^{14}(3\cdot6+20)<80\cdot6^{14}$, and 100 pairs give fewer than $6.3\cdot10^{14}$ operations.
- **Lines 142–144, odd factor.** HOLDS. $E_{h+k}\le E_hE_kD_{h,k}$. The addition chain for $25$ is $1,2,4,8,16,24,25$: 6 merge types, so $6\cdot4\cdot4=96$. The tree bound is $E_{\rm in}^MD_*^{M-1}$.
- **Lines 148–162, (11).** HOLDS. $4A''-A=\sum a_k\beta^{2k}3k/(k+2)$ follows from $a_{k+1}/a_k=1/(4(k+1)(k+2))$, so $\tau$ is as displayed. $\tau(1)>7/192>1/30$ and $\tau(2)>1/10$. $\|T^2f\|\ge\tau^2$ on the 14-dimensional span. Jensen covers the averaging.
- **Line 164, multiplicative enclosure.** HOLDS. The kernel bound by $(E-1)$ times a doubly stochastic kernel gives operator norm at most $E-1$ (Schur test).
- **Line 166, (12).** HOLDS. $(27/65)^{130}<2^{-130}$, the ratio is $324/(4\cdot66\cdot67)<1/2$, and $P_{64}\ge1$.
- **Line 178, second elimination.** HOLDS. Two links share at most one plaquette, so the six stars at $x$ are distinct. $|B_j+O_jx|^2=a_j+b_j\cdot x$.
- **Lines 180–187, moment recurrence.** HOLDS. Gaussian integration by parts gives the recurrence, with $\mathbb ER^h=(h+2)\mathbb ER^{h-2}$ in dimension 4. $65^6\cdot60<4.6\cdot10^{12}$. There are 21 Gram entries.
- **Line 200, two and three faces.** HOLDS. Forests integrate to 1. The triangle density is $w_\beta^{*3}$. $\int w^{*3}\chi_1=2r^3$.
- **Line 202, face products.** HOLDS. $z f_af_bf_c\in[E^{-2},E^2]$ via $z\in[E^{-1},E]$. Then $|\langle\rho-1,\chi\rangle|\le(E^3-1)\|\chi\|_1\le E^3-1$.
- **Line 225, table architecture.** HOLDS. A $q$-valued face label gives rank at most $q$. $49^{14}>10^{21}$.
- **Lines 264–268, quadratic-spin stop.** HOLDS. There are $4b(b-1)^3$ interior links, at most $(b-1)^4$ gauge-fixable, and $6b^2(b-1)^2$ nonboundary plaquettes. The inequality reduces to $b^2-2b-1\le0$. The three-sign alternating sum is $8\beta\ne0$.
- **Lines 272–286, HS presentation.** HOLDS. This is the first identity HS1 of row 1016 (`gap-global-reform-max.md`, Claude Fable 5.2), with the even-diagonal parity choice. Each link belongs to its odd endpoint, and each bond is read by exactly two odd sites.
- **Lines 288–293, (20).** HOLDS. Two replicas with $u'_a=u_ag_a$ give the flat cube.
- **Lines 295–300, (21).** HOLDS. $\binom43 2^3=32$ triangles, each contributing $4r(\beta)^3$.
- **Lines 302–312, flat cube.** HOLDS. Completing the square gives the displayed formula. $\mathbb E|Y|^{2k}=2^k(k+1)!$. $|\sum s_i\cdot s_j|\le24$, so $56^h/h!$, and $56e/513<1/2$. The two squares need about $6\cdot10^9$ multiply-add pairs, below $10^{11}$.
- **Line 336, fixed-coupling consumer.** HOLDS. The degree is at most 80. Each bond is read by two boxes, so exponent 2 applies.
- **Lines 359–363, (26).** HOLDS. A component is read by at most 8 cells. Finner applies with exponent 8, and $d=81$.
- **Line 393, conditional integration on the cut.** HOLDS. Single-crossing plaquettes pair the two noncrossing links of one group. Groups with $k=0,1$ have mass 1.

## Restatement of earlier rows

No main step only restates an earlier row. Items 1 to 7 are new calculations: the Pfaffian formula and its seven-index circuit, the 49-mode bound, the gluing certificate and dictionary, the obstructions (24) and (27), and the sheet bound.
Some supporting steps are close to earlier rows, and the file credits each one:
- The six-staple field and its single-link integral (lines 23–29). The file cites Grok's PR 10133, §2. I did not open that PR.
- The geometry in Lemma STAR (row `gap-blockcrit-opus.md`).
- Finner's inequality (`gap-flat-check-opus.md`, §3) and the short-cluster cancellation (`gap-seed-sc.md`, §2.3). These are used in (2).
- HS1 of row 1016.
In item 8, the divergence of the bare inverse coupling restates row 1335 (line 114) with other line ranges of CA-I. The new part there is the fixed-rank obstruction.

## Summary

| Item | Lines | Verdict |
|---|---|---|
| 1 cubical map (13) | 191–198 | HOLDS (sides at least 4) |
| 2 (16)–(18), checks | 229–254, 424 | HOLDS |
| 3 enclosure and gate count | 15, 245–262 | HOLDS (recount below $6.6\cdot10^{14}$) |
| 4 (14) | 204–223 | HOLDS (applied at fixed skeleton) |
| 5 (22)–(23) | 316–334 | HOLDS |
| 6 (24), (27) | 338–383 | HOLDS |
| 7 (28)–(29) | 395–418 | HOLDS |
| 8 entry obstruction | 385–389, 428 | HOLDS (conditional, stated scope) |
| 9 other 30 PROVED statements | various | 29 HOLD, line 81 HOLDS AFTER CORRECTION (wording) |

The file's OPEN conclusion stands. There is no block step for the full Wilson action, no uniform entry from the first-passage densities, and neither SEED-L nor the mass gap.

Checked by hand by Claude Opus 5.5. A numeric series evaluation guided items 3 and 7 only.

RESULT: Of 44 PROVED statements in row 1341, 43 HOLD, 1 HOLDS AFTER CORRECTION (line 81 wording: the β=23/10 predicate is stated as if true, but (5) refutes it), 0 FAIL; main finding: the exact 2^4 cubical map, the Pfaffian identity and seven-index enclosure (error below 2^-24 on 0≤β≤7/3, recounted below 6.6·10^14 gates), the 49-mode bound, the gluing certificate, the obstructions (24) and (27), the sheet bound d_*<1/4 and the bare-scale entry obstruction all hold, so the block step of Proposition CH stays OPEN.
