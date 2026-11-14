# Check of gap-pag-allcover-astra.md

- Checker: Claude Opus 5.5. Date: 2026-11-12. Cross-provider check: the author is Codex gpt-6-astra.
- Source: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-pag-allcover-astra.md`, 540 lines, read in full.
- Context read: `gap-crux-exercise-astra.md` 749-984 (8.1, cover and PA) and 1194-1354 (8.4, GC1-GC4, PA_g); `gap-pag-corner-astra.md` 54-128 (face corner); `gap-pag-grow-astra.md` 30-105 and 333-534 (scope, section 5, Lemma V, R1); `gap-pag-grow-check-opus.md` in full (190 lines).
- Method: by hand. One short numerical root search was run as a guide only (the exact range where the bound exceeds 1/160). No verdict rests on it.
- Not read: PR #10114, the SA outline and the CA-I lines cited in the "Repo search" and Section 1 paragraphs. Those reading records are not checked.
- Credit: every statement marked HOLDS is the author's result.

## Notation fixed for the check

Coordinates 1, 2. Box C has coordinate-1 interval $[0,c_1^+]$; box B has $B_1=[b_1^-,b_1^+]$ with $b_1^-<0\le b_1^+<c_1^+$. Box B has coordinate-2 interval $[0,b_2^+]$; box C has $C_2=[c_2^-,c_2^+]$ with $c_2^-<0\le c_2^+<b_2^+$. Coordinates 3, 4: common $K=[a_3,\dots]$ and $J\ni t-1,t,t+1$. Links are assigned by base. So C is right of B in coordinate 1 and below B in coordinate 2, as in GC1.

Interval facts for the 8.1 cover. Block interval $I_i=[x_i-q_{i-1},x_i+q_i]$, $q_i=\lfloor 2s_i/3\rfloor$.
- Overlap $I_i\cap I_{i+1}=[x_{i+1}-q_i,\,x_i+q_i]$. It extends $2q_i-s_i\ge s_i/3-4/3\ge 8/3$ beyond its lower endpoint, so at least 3 sites. The note's $\ge \ell/3-2\ge 2$ is looser and valid.
- Distance between lower endpoints: $s_i-q_i+q_{i-1}\ge s_i/3+(2s_{i-1}-2)/3\ge \ell-2/3$. Being an integer, it is $\ge\ell$. The note's $\ge\ell-1$ is valid.
- Hence $b_1^-\le-\ell\le-12$, $c_2^-\le-12$, $b_2^+\ge 3$, $b_1^+\ge 2$. Every site used below exists.

## Section 2. The exclusive boundary star

Membership of $z=(-1,0,a_3,t)$, $v=(0,0,a_3,t)$, $w=(0,-1,a_3,t)$, $o=(-1,-1,a_3,t)$.
- $z\in$ box B ($-1\in B_1$, $0\in B_2$), $z\notin$ box C ($-1\notin[0,c_1^+]$).
- $w\in$ box C ($0\in C_1$, $-1\in C_2$), $w\notin$ box B ($-1\notin[0,b_2^+]$).
- $o$ in neither box.
- $U=(z,1)$: base $z$, so $U\in X$. $V=(w,2)$: base $w$, so $V\in Y$. Correct.

Links incident to $z$.
- Four outgoing links have base $z$: all in $X$.
- Incoming 1: base $(-2,0,a_3,t)\in$ B only: $X$. Incoming 4: base $(-1,0,a_3,t-1)\in$ B only: $X$.
- Incoming 2: base $o$: exterior. Incoming 3: base $(-1,0,a_3-1,t)$, $a_3-1\notin K$: exterior.
- So six $X$ links, two exterior links, none in $Y$ or $Z$. HOLDS.

Boundary vertices. $z$ has exterior incident links. $v$ and $w$ have exterior incoming direction-3 links (third coordinate $a_3-1$). So all endpoints of $U,V$ are boundary vertices of $S$. HOLDS.

Plaquette $p$ at $o$. Links $(o,1)$, $(o,2)$ have base $o$: exterior. The other two are $V=(o+e_1,2)$ and $U=(o+e_2,1)$. Holonomy at identity exterior is $VU^{-1}$, and $\tfrac12\operatorname{tr}(VU^{-1})=u\cdot v'$. HOLDS.

Count of changed plaquettes. A plaquette containing $z$ contains exactly two links incident to $z$. It changes iff exactly one of them is free. Each link at $z$ lies in 6 plaquettes, all containing $z$. The two exterior links share exactly one plaquette, the $(2,3)$ plaquette in the quadrant $-e_2,-e_3$. So $6+6-1=11$ plaquettes contain an exterior link at $z$, and $11-1=10$ contain exactly one. The note's "$6+6-2$" is the same count. HOLDS.

Enumeration. I wrote out all ten.
- Through the incoming direction-2 link $E_2$, transverse $\nu$:
  - $+1$: $p$. Free links $U,V$.
  - $-1$: free $(z-e_1,1)$ [B only]; $(o-e_1,2)$, $(o-e_1,1)$ have base $(-2,-1,\cdot)$: exterior.
  - $+3$: free $(z,3)$; $(o+e_3,2)$ base $(-1,-1,a_3+1,t)$ and $(o,3)$: exterior.
  - $-3$: contains both exterior links. Unchanged.
  - $+4$: free $(z,4)$; $(o+e_4,2)$, $(o,4)$: exterior.
  - $-4$: free $(z-e_4,4)$; $(o-e_4,2)$, $(o-e_4,4)$ base $(-1,-1,a_3,t-1)$: exterior.
- Through the incoming direction-3 link $E_3$, transverse $\nu$:
  - $-2$: the same excluded plaquette.
  - $+1$: free $U$; $(v-e_3,3)$ and $(z-e_3,1)$ at third coordinate $a_3-1$: exterior. This is $p_U$.
  - $-1$: free $(z-e_1,1)$; the rest at $a_3-1$: exterior.
  - $+2$: free $(z,2)$; the rest at $a_3-1$: exterior.
  - $\pm4$: free $(z,4)$ or $(z-e_4,4)$; the rest at $a_3-1$: exterior.
- So ten changed plaquettes. Only $p$ reads a non-$X$ link, namely $V$. No changed plaquette reads $Z$. HOLDS.

Endpoint paragraph (lines 157-162). The sites at offset $-2$ in coordinate 1 (for B) and $-1$ in coordinate 2 (for C), and $+1$ in coordinate 2 (for B), exist by the interval facts above. $t\pm1\in J$ and $a_3+1\in K$ hold. HOLDS (the stated bounds are loose but valid).

The frame (3). $D_i$ is the generator of $U\mapsto e^{\theta\,i\sigma_i}U$ on the outgoing links and $L\mapsto L\,e^{-\theta\,i\sigma_i}$ on the incoming free links. In quaternions $D_iu=e_iu$ for unit imaginary $e_i$. Right multiplication by $u$ is an isometry of $\mathbb R^4$ sending $(1,e_1,e_2,e_3)$ to $(u,e_1u,e_2u,e_3u)$. So the $D_iu$ are orthonormal and orthogonal to $u$, and $\sum_i(D_iu)(D_iu)^T=I_4-uu^T$. $D_i^2u=e_i^2u=-u$, so $\Delta u=-3u$. Each $D_i$ generates a flow of left or right translations on each link, so it preserves product Haar and is skew-adjoint. HOLDS.

Action identity (4). $\rho\propto\exp(\beta\sum_q x_q)$. Only the ten changed plaquettes depend on the action. So $D_i\log\rho=\beta\sum_{q\ne p}D_ix_q+\beta(D_iu)\cdot v'$, since $D_iv'=0$. $F$ is $\beta$ times the nine $X$-only traces (with exterior fixed). HOLDS.

$\Delta x_q=-3x_q$. Each changed plaquette has exactly one transformed link. By cyclicity its trace is $x(kW)$ or $x(Wk^{-1})=x(kW^{-1})$, with $W$ independent of $k$. In quaternions this is $\operatorname{Re}(e^{\theta e_i}w)$, so $D_i^2x_q=-x_q$. HOLDS.

## Section 3. Marginal integration by parts

Marginal score (5). $D_i$ acts on $X$ only, so it commutes with $\int\cdot\,dY\,dZ$. Then $s_i=\int(D_i\rho)\,dYdZ/m_X=\mathbb E[H_i\mid X]=D_iF+\beta(D_iu)\cdot a(X)$, with $H_i=D_i\log\rho$. HOLDS.

Mean zero. $\int(L_Xf)\,m_X=\sum_i\int D_i(m_XD_if)=0$ by skew-adjointness. So $\mathbb ET_j=0$. HOLDS.

Sign and conditioning in (6).
- Joint identity: $\int\sum_iD_i(\rho\,v'_jD_iu_j)=0$, and $D_iv'_j=0$. This gives $\mathbb E[(\Delta u_j+\sum_iH_iD_iu_j)v'_j]=0$.
- Subtract: $\mathbb E[T_jv'_j]=\mathbb E[\sum_i(s_i-H_i)(D_iu_j)v'_j]$. Here $s_i-H_i=\beta(D_iu)\cdot(a-v')$, since $D_iF$ cancels.
- So $\mathbb E[T_jv'_j]=-\beta\,\mathbb E\sum_{i,k}(D_iu_j)(D_iu_k)(v'_k-a_k)v'_j$. This is line 1 of (6). Correct sign.
- Sum over $j$: $-\sum_j\mathbb E[T_jv'_j]=\beta\,\mathbb E[(v'-a)^TP_uv']$. Given $X$, $P_u$ and $a$ are fixed, and $\mathbb E[v'(v'-a)^T\mid X]=\operatorname{Cov}(v'\mid X)$. So it equals $\beta\,\mathbb E\operatorname{tr}(P_u\operatorname{Cov}(v'\mid X))$. Line 2 of (6). HOLDS.
- Sanity at first order in $\beta$: $\rho\approx1+\beta\sum x_q$ gives $\sum_j\mathbb E[-3u_jv'_j]\approx-3\beta\sum_j\mathbb E u_j^2\mathbb E v_j'^2=-3\beta/4$, and the $s_i$ terms are $O(\beta^2)$. The right side is $\beta\operatorname{tr}(P_u I/4)=3\beta/4$. Consistent.

Lemma C, (7)-(8).
- $\mathbb E\sum s_i^2\le\mathbb E\sum H_i^2$ by conditional Jensen. Correct.
- $\int D_i(H_i\rho)=0$ gives $\mathbb E\sum H_i^2=-\mathbb E\Delta\log\rho=3\beta\sum_{q\text{ changed}}\mathbb Ex_q\le30\beta$. Correct; only $x_q\le1$ is used.
- $\sum_jT_j^2=|-3u+\sum_is_iD_iu|^2=9+\sum_is_i^2$, by orthonormality and $u\perp D_iu$. Correct.
- So $\sum_j\mathbb ET_j^2\le9+30\beta$, with no volume or block-size dependence. HOLDS.

## Section 4. The one-link variance and the angle bound

(10). Given $H$ (all free links except $V$, and the fixed exterior), $V$ has density $\propto e^{\kappa h\cdot v'}$, $0\le\kappa\le6\beta$ (six plaquettes per link). The density depends only on $h\cdot v'$. So the transverse mean is zero, the transverse-longitudinal cross moment is zero (reflection fixing $h$), and the transverse block is isotropic. Lemma V (checked earlier) gives the transverse second moment $1/(4+\kappa b)\ge1/(4+6\beta)$. So $\operatorname{Cov}(v'\mid H)=T(I-hh^T)+\operatorname{Var}(h\cdot v')hh^T\succeq(I-hh^T)/(4+6\beta)$. At $\kappa=0$, $\operatorname{Cov}=I/4$, and any $h$ works. HOLDS. The note is right that this is a covariance bound only transverse to $h$; the longitudinal variance can be small.

(9). $X\subset H$, so $\operatorname{Cov}(v'\mid X)\succeq\mathbb E[\operatorname{Cov}(v'\mid H)\mid X]$ (law of total covariance). $P_u$ is $X$-measurable and positive semidefinite. $\operatorname{tr}(P_u(I-hh^T))=3-h^TP_uh=2+(u\cdot h)^2\ge2$. So $\mathbb E\operatorname{tr}(P_u\operatorname{Cov}(v'\mid X))\ge2/(4+6\beta)$. HOLDS.

Invariant test space.
- $u$, $v'$: all endpoints of $U,V$ are boundary vertices, so interior gauges do not act on them. Correct.
- $m_X$ is invariant: an interior gauge $g$ acts as a product map on $X,Y,Z$, preserves $\rho$ and product Haar; change variables in $Y,Z$. Correct.
- $D_i$ commutes with the action of $g$: $g$ acts at vertices $\ne z$, and on a link the two actions are left and right multiplications, which commute. So $s_i\circ g=D_i(\log m_X\circ g)=s_i$, and $T_j\circ g=T_j$. Correct.
- $T_j$ is a function of $X$ (with exterior fixed), so it is in $\operatorname{ran}E_C$. $v'_j$ is in $\operatorname{ran}E_B$. For centred such $f,g$, $\langle g,(E_BE_C-E_S)f\rangle=\langle g,f\rangle$. HOLDS.

(11). $|\sum_j\operatorname{Cov}(T_j,v'_j)|\le k_g\sum_j\|T_j\|\,\sigma(v'_j)\le k_g(\sum\mathbb ET_j^2)^{1/2}(\sum\operatorname{Var}v'_j)^{1/2}$ by Cauchy-Schwarz. $\sum_j\operatorname{Var}v'_j=1-|\mathbb Ev'|^2\le1$. With (6), (7), (9): $k_g\ge\frac{2\beta}{(4+6\beta)\sqrt{9+30\beta}}=\frac{\beta}{(2+3\beta)\sqrt{9+30\beta}}$. The two displayed forms (lines 43 and 99) agree. HOLDS.

Single witness pair. If every pair $(-T_j,v'_j)$ with positive variances had correlation $\le r$, then $2\beta/(4+6\beta)\le r\sqrt{9+30\beta}$, so $r\ge c(\beta)$. So one pair attains correlation $\ge c(\beta)$. HOLDS.

Arithmetic, re-derived. $\beta/(2+3\beta)$ and $\sqrt{9+30\beta}$ both increase. On each interval use the left value of the first and the right value of the second.
- $[1/16,1/4]$: $(1/16)/(35/16)=1/35$; $\sqrt{33/2}<9/2$ since $66<81$; $2/315>1/160$ since $320>315$.
- $[1/4,1]$: $1/11$; $\sqrt{39}<7$; $1/77$.
- $[1,4]$: $1/5$; $\sqrt{129}<12$; $1/60$.
- $[4,64]$: $4/14=2/7$; $\sqrt{1929}<44$ since $1936$; $2/308=1/154>1/160$.
- $\beta=1$: $1/(5\sqrt{39})>1/35$.
- HOLDS: $c(\beta)>1/160$ throughout $[1/16,64]$.

On "exactly the stated range". The interval is a conservative subset, not the exact set where $c>1/160$. A numerical root search (guide only) puts the exact set at about $(0.0426,\,93.2)$. By hand: $c(64)=\frac{64}{194\sqrt{1929}}>\frac{64}{194\cdot44}>\frac1{134}$. The note claims only the subset. This is not an error.

## Section 5. Exterior quantifiers and invariant realizations

Positive-measure exteriors.
- The selected pair is a fixed bounded smooth function of $X$ and a fixed function of $Y$. Their interior-gauge invariance is a property of the functions, not of the exterior. Correct.
- The conditional density is positive and continuous in the finitely many touching exterior links. Means, variances and the correlation (centred at each exterior) are continuous. A strict bound $>c'$ for $c'<c$ persists on an open set. That set has positive Haar measure, hence positive Wilson exterior-marginal measure. Correct.
- Supremum over $c'<c$ gives the essential-supremum bound $\ge c$. On (2), $c>1/160$ strictly, so $c'>1/160$ is available. HOLDS.

Globally invariant realization.
- Loops. As in the predecessor (checked), the three loops at third coordinate $a_3-3$ meet no touching plaquette. Touching plaquettes only contain links with base third coordinate $\ge a_3-1$. Correct.
- Covariance. With root frame $g_r$ defined by rotating the Gram-Schmidt frame of the three loop holonomies' anti-Hermitian parts to the fixed frame, and $g_b=g_rP_b$, a global gauge $h$ gives $g_b(h\cdot c)=\pm g_b(c)h_b^{-1}$. So $G(h c)\cdot(h\cdot X)$ equals $G(c)\cdot X$ up to an interior gauge and a common central sign. Correct.
- Sign. On free links, $-1$ at every boundary vertex equals $-1$ at every interior vertex: every free-link endpoint is interior or boundary, and $(-1)(-1)=1$. That is an interior gauge, so $T_j$ does not see it. Correct.
- Orientation. A negatively oriented frame has no SU(2) lift. The determinant of the three anti-Hermitian parts is conjugation invariant. So an invariant cutoff in it is available. Correct.
- One missing condition. "At the specified exterior they equal the four original functions" needs all root-to-boundary paths, and the paths to the loops, to have transport $I$ there. So they must avoid the modified loop links. The predecessor's paths did. The note does not say so here. HOLDS AFTER CORRECTION: choose the exterior paths to avoid the modified loop links (this is possible because the exterior graph stays connected after removing a few distant links; the predecessor's explicit paths do it).
- With that, the extended functions read the exterior, keep $X$-only and $Y$-only free dependence, are invariant under all vertex gauges, and their correlations are continuous near the specified exterior. HOLDS AFTER CORRECTION.

OPEN / different boundary algebra (lines 407-413). An accurate scope statement. HOLDS.

## Section 6. Broad class, other assignments, grouped unions

Theorem E (12).
- Condition 1 makes the $z$-action move $X$ only, with $U$ outgoing at $z$. If $U$ were incoming, $D_iu=-ue_i$, still an orthonormal tangent frame; not needed.
- Condition 2: $V$ is not incident to $z$ (it would then be in $X$). So $p$'s other link at $z$ is exterior, and $p$ is a changed plaquette. With a fixed exterior transport, $x_p=u\cdot v''$ with $v''=s(AVB)$. $v''$ is a $Y$-function, interior-gauge invariant, and $V\mapsto AVB$ preserves Haar, so Lemma V applies to $v''$ with the same $\kappa\le6\beta$.
- Condition 3 gives (4) with $F$ $X$-only.
- On a torus without short-period identifications each changed plaquette has exactly one transformed link, so $\Delta x_q=-3x_q$ and (8) becomes $3n\beta$.
- All other steps are unchanged. So $k_g\ge2\beta/((4+6\beta)\sqrt{9+3n\beta})$. HOLDS.
- $n\le24$: six planes times four quadrants. At $\beta=1$, $2/(10\sqrt{9+3n})\ge2/(10\cdot9)=1/45$. HOLDS.

Range for general $n$ (clarification). For $n=24$ the bound does not cover all of (2). By hand at $\beta=64$: $\frac{128}{388\sqrt{4617}}<\frac{128}{388\cdot67}<\frac1{200}<\frac1{160}$. At $\beta=2$: $\frac1{4\sqrt{153}}>\frac1{50}$. Numerical guide: for $n=24$ the bound exceeds $1/160$ on about $(0.047,\,38.0)$. Section 6 claims only $\beta=1$ for general $n$, which is correct.

Unequal intervals. Section 2 used no interval equality. Every 8.1 cover (at least twelve intervals per coordinate) has a neighbouring pair with C right of B in coordinate 1, below in coordinate 2, and equal intervals in coordinates 3, 4. So the $n=10$ pair is present in every cover, including any that avoids all $\theta$-symmetric pairs. HOLDS.

Both-endpoint assignment.
- Cover: for a link in direction $\mu$, sites $y,y+1$ lie in one block interval. If $y$ is the top of $I_i$, then $y,y+1\in I_{i+1}$ because overlaps have at least two sites. Correct.
- At $z$: the six links have other endpoints $v$, $(-1,1,a_3,t)$, $(-1,0,a_3+1,t)$, $(-1,0,a_3,t\pm1)$, $(-2,0,a_3,t)$, all in box B; none is in C since $z\notin$ box C. The incoming 2 and 3 links have an endpoint outside both boxes. Correct.
- $V$: endpoints $w,v\in$ box C; $w\notin$ box B. So $V\in Y$. Correct.
- I re-ran the ten-plaquette enumeration under this rule. Every non-free link listed above has an endpoint with $x_2=-1,x_1<0$ or with $x_3=a_3-1$, so it is exterior. Only $p$ reads $Y$. $n=10$. $v,w,z$ keep exterior direction-3 links. Correct.
- Blocks are subsets of base-assigned blocks, so the interaction degree does not increase; the pair still interacts through $p$. HOLDS.

Terminal assignment.
- $\Phi$: $(\Phi U)_{(-x-e_\mu,\mu)}=U_{(x,\mu)}^{-1}$. A link is in $Q$ under terminal assignment iff its image is in $-Q$ under base assignment.
- The reflected blocks $[-x_i-q_i,\,-x_i+q_{i-1}]$ are exactly 8.1 blocks for the partition with endpoints $-x_i$ and the same interval lengths. So $-Q$ is an 8.1 cover.
- $\Phi$ preserves Haar, plaquette traces, the identity exterior, interior vertices and the conditional projections. So Theorem A for $-Q$ pulls back. HOLDS.

Star-preserving changes and grouped unions.
- Links incident to $z$, $p$, and $v$'s exterior link all lie in plaquettes at $z$ ($v-e_3$ is a corner of $p_U$). $w$'s exterior link is covered by "endpoint boundary links of U,V". So conditions 1-3 survive. Correct.
- For a pair of unions, Theorem E applies to $X=G_1\setminus G_2$, $Y=G_2\setminus G_1$. If the local pattern is unchanged, $n=10$ and the full range (2) holds; the note claims only $\beta=1$, which is conservative. HOLDS.
- The degree and locality constants of a grouped cover are not inherited. The note says so. Correct.

OPEN / groups changing the test. Accurate. HOLDS.

## Section 7. What is claimed open versus what is proved

- "Do not rescue ... at $\beta=1$, $\beta=2$, or anywhere in (2)": true for the 8.1 covers ($n=10$) in all three assignments. For Theorem E pairs with general $n\le24$, true at $\beta=1$ and $\beta=2$ but not throughout (2) (see $n=24$, $\beta=64$). The sentence in lines 495-499 runs these together. HOLDS AFTER CORRECTION: for Theorem E pairs with $n>10$, claim $\beta=1$ (and $\beta=2$), not all of (2).
- OPEN large $\beta$: $c(\beta)\sim1/(3\sqrt{30\beta})\to0$. Correct. The predecessor's coverage is stated accurately: $\theta$-symmetric pairs for $\beta>2/47$ (R3) and every 8.1 cover for $\beta\ge H(L)^{100}$ (Theorem P). Correct.
- Not mentioned as open: nonsymmetric covers at small $\beta<1/16$. The guide root search suggests $c>1/160$ down to about $0.0426$, close to $2/47\approx0.04255$. Below that, PA_g may hold. This regime is off the weak-coupling trajectory and the note never claims it. Not an error; noted for completeness.
- The witness description (four marginal-score functions on $X$, four coordinates on $Y$; no claim about elementary traces): accurate.
- Failed route (positive-kernel argument needs a square): accurate.
- "No mass-gap conclusion follows": accurate.

## Section 1. Comparison with earlier rows

- Corner note: fixed block size, large $\beta$. Grow note: $\theta$-symmetric pairs for $\beta>2/47$, and all covers only above $H(L)^{100}$. The grow check left covers with no symmetric pair (for $N\gg\ell$) undecided.
- The present claim covers every 8.1 cover, with no symmetry, uniformly in block size, on $[1/16,64]$. This is not contained in the earlier rows. The method (exclusive boundary star, marginal score, Fisher bound) does not appear in them.
- A lane grep for "boundary star", "marginal score" and "exclusive boundary" found only this note and an unrelated Balaban action-derivative passage in `p81-crit-draft.md:547`.
- The PR #10114, SA and CA-I reading paragraphs: not checked (sources not read).
- Verdict: the claim is new relative to the lane's earlier rows. HOLDS.

## Hidden mass-gap assumption

None. Every step is an exact finite-volume identity or inequality at a fixed exterior: Haar integration by parts, conditional Jensen, total covariance, the one-link von Mises-Fisher law, and continuity in finitely many exterior links. No clustering, decay, infinite-volume limit, Wilson association or monotonicity in $\beta$ is used.

## Verdict table

| # | Statement | Verdict |
|---|---|---|
| 1 | §1 source-reading paragraphs (PR #10114, SA, CA-I) | Not checked (sources not read) |
| 2 | §1 claim is new relative to corner and grow rows | HOLDS |
| 3 | §1 Theorem A statement (1)-(2), scope | HOLDS (follows from 4-17) |
| 4 | §2 membership of $U\in X$, $V\in Y$, $p$ with only $U,V$ free, trace $u\cdot v'$ | HOLDS |
| 5 | §2 all free links at $z$ lie in $X$; two exterior | HOLDS |
| 6 | §2 exactly ten changed plaquettes; only $p$ reads $Y$, none reads $Z$ | HOLDS |
| 7 | §2 endpoint availability (lines 157-162) | HOLDS (bounds loose but valid) |
| 8 | §2 frame identities (3), skew-adjointness | HOLDS |
| 9 | §2 action identity (4), $\Delta x_q=-3x_q$ | HOLDS |
| 10 | §3 marginal score (5), $\mathbb ET_j=0$ | HOLDS |
| 11 | §3 sign and conditioning in (6) | HOLDS |
| 12 | §3 Lemma C, (7)-(8) | HOLDS |
| 13 | §4 centred transverse covariance (10) | HOLDS |
| 14 | §4 (9), total covariance, $\operatorname{tr}(P_u(I-hh^T))\ge2$ | HOLDS |
| 15 | §4 interior-gauge invariance of $s_i$, $T_j$; membership in ran $E_C$, ran $E_B$ | HOLDS |
| 16 | §4 (11) and the angle bound $\beta/((2+3\beta)\sqrt{9+30\beta})$; single witness pair | HOLDS |
| 17 | §4 $c>1/160$ on $[1/16,64]$; $c(1)>1/35$ | HOLDS (conservative: the exact set is larger, about $(0.043,93)$ by a numerical guide) |
| 18 | §5 positive-measure exteriors and essential supremum | HOLDS |
| 19 | §5 globally invariant boundary-frame extension | HOLDS AFTER CORRECTION (paths from the root must avoid the modified loop links, so that transports are $I$ at the specified exterior) |
| 20 | §5 OPEN different boundary algebra | HOLDS |
| 21 | §6 Theorem E, (12), $n\le24$, $1/45$ at $\beta=1$ | HOLDS |
| 22 | §6 every 8.1 cover, unequal intervals, $n=10$ | HOLDS |
| 23 | §6 both-endpoint assignment | HOLDS |
| 24 | §6 terminal assignment by inversion | HOLDS |
| 25 | §6 star-preserving changes and grouped unions | HOLDS (conservative: with the star unchanged, $n=10$ gives all of (2)) |
| 26 | §6 OPEN groups changing the test | HOLDS |
| 27 | §7 first paragraph, range attached to Theorem E pairs | HOLDS AFTER CORRECTION (for $n>10$ claim $\beta=1,2$ only; $n=24$ gives a bound below $1/160$ at $\beta=64$) |
| 28 | §7 OPEN large $\beta$, predecessor coverage, failed route | HOLDS |
| 29 | Hidden mass-gap assumption | None found |

RESULT: gap-pag-allcover-astra.md HOLDS (credit Codex gpt-6-astra), with two small corrections: the boundary-frame paths must avoid the modified loop links, and in §7 the full range (2) applies to $n=10$ stars, while general Theorem E pairs are covered at $\beta=1$ and $\beta=2$. Checked by hand by Claude Opus 5.5: the ten-plaquette star, the sign and conditioning of (6), Lemma C, the transverse covariance (10), invariance of $T_j$, the bound $k_g\ge\beta/((2+3\beta)\sqrt{9+30\beta})>1/160$ on $[1/16,64]$, the exterior quantifiers, both other assignments and Theorem E. So PA_g fails on every 8.1 cover, with no symmetry and uniformly in block size and torus, on positive-measure exterior sets, for $1/16\le\beta\le64$. Nonsymmetric covers at arbitrarily large $\beta$ remain OPEN. No step assumes a mass gap.
