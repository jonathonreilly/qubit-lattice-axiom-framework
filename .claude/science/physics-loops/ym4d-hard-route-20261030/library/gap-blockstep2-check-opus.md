# Check of row 1345: gap-blockstep2-astra62.md (FINISH row 1347)

Checker: Claude Opus 5.5, by hand, line by line.
File checked: `library/gap-blockstep2-astra62.md` (row 1345, by gpt-6.2-astra).
Context read: `gap-blockstep-astra62.md` (row 1341), `gap-blockstep-check-opus.md`,
`gap-shrink-box-fable.md` Section 6.1 with `gap-shrink-box-check-astra.md`,
`gap-crux-restate.md` Section 4.4.
Not read: `gap-blockstep-fable.md` (independent attempt).

Verdicts follow, one per statement, with line numbers of the checked file.
Each step was derived again here. No numeric run is used as a proof step.

Line numbers refer to the target as committed at `72df8a2ab`. The file has 29 statements marked PROVED,
at lines 11, 18, 26, 32, 34, 40, 48, 61, 63, 73, 79, 81, 89, 91, 107, 121, 123, 131, 149, 151, 153, 160,
169, 171, 173, 180, 188, 190 and 197. Items 1 to 6 cover 17 of them. Item 7 covers the other 12.
No numeric run was made for this check. All arithmetic below is by hand.

## 1. Center split (1), block map (2) and iteration (3), lines 11–30. All three HOLD.

**Line 11, (1). HOLDS.** For central signs, $U_p=(ds)_p\widetilde U_p$, so $q(U_p)=(ds)_pq(\widetilde U_p)$.
The map $(R,s)\mapsto s\,\sigma(R)$ from $SO(3)\times\{\pm1\}$ to $SU(2)$ is a bijection for a measurable section $\sigma$.
Haar is invariant under $U\mapsto-U$, so it pushes to quotient Haar times a fair sign.
$e^{\beta\sum(q-1)}=e^{-\beta|\mathcal P|}e^{\beta\sum q}$ gives $a$ and $J_p$. A change of section multiplies the lifts by signs.
This is the split of `gap-crux-restate.md` §4.4 (Claude Fable 5.2), which credits Mack and Petkova.

**Line 18, (2). HOLDS.** A bundle has $b^3$ links. The map $s\mapsto(t,\rho)$ with $t_E=s_{\rm pivot}$, $\rho_e=s_et_E$ is a bijection of finite sets, so it keeps the uniform law.
A fine $(\mu,\nu)$ plaquette at $x$ crosses the $\mu$-cut iff $x_\mu$ is the last position of its block.
If it crosses only the $\mu$-cut, its two $\mu$-links lie in one bundle, because $x$ and $x+e_\nu$ are in the same block in $\nu$. Then $t_E^2=1$.
If it crosses both cuts, its four links lie in the bundles of the four edges of one coarse plaquette $P$. So $(ds)_p=(d\rho)_p(dt)_P$.
$S(P)$ fixes the two crossing coordinates, so $|S(P)|=b^2$, and distinct $P$ give disjoint sets.
Substitution gives (1) on the coarse grid with $y'=(y,\rho)$. Each torus is treated separately. The identity is exact at every $\beta$.

**Line 26, (3). HOLDS.** Step one: $J'_P(dt)_P=\sum_{S(P)}\beta q(\widetilde U_p)(d\rho)_p(dt)_P=\beta\sum_{S(P)}q(U_p)$.
At a second step with factor $b_2$, $J''_Q(dt')_Q=\sum_{P\in S(Q)}J'_P(dt)_P$.
A fine face in $\bigcup_{P\in S(Q)}S(P)$ has its two crossing coordinates at the last fine position of the last coarse position, which is the last position of the $B$-block.
Its transverse coordinates range over $b_2$ coarse times $b_1$ fine values, which is $B$. So the union is $S_B(Q)$ with $|S_B(Q)|=B^2$. Induction gives (3).
Faces of $S(P)$ for $P$ crossing one coarse cut go into the new environment, as stated. The class (1) is closed under (2).
So the map preserves each of the two masses exactly and iterates at every bare coupling. Positive claim 1 holds.

## 2. (4), (5), the first-passage tail and (10), lines 38–67 and 107–119. All HOLD.

**Deletion input (line 38, GUIDE).** I read row 1167, `gap-solve12-astra62.md` lines 12–19 (Codex). Its (1) is $\mathbb E_\beta e^{\beta\sum_D(1-q_p)}\le z_\beta^{-|D|}$ with $z_\beta=e^{-\beta}A(\beta)$, for distinct faces sharing one direction, sides at least four.
Multiplying out gives $\mathbb E_\beta e^{-\beta\sum_Dq_p}\le A(\beta)^{-|D|}$, as quoted. Strict Jensen gives $A(\beta)>e^{0}=1$.

**Line 40, (4). HOLDS.** Take $i$ maximizing $h_i$ and $H_i=\{P\in H:i\parallel P\}$. The event lies in $\{\sum_{H_i}X_P\le uB^2h_i\}$.
$\sum_{H_i}X_P=\beta\sum_{p\in D}q(U_p)$ with $D=\bigcup_{H_i}S_B(P)$, $|D|=B^2h_i$. Every face of $D$ contains direction $i$.
Exponential Markov and the deletion bound give $e^{uB^2h_i}A^{-B^2h_i}$. Since $\sum_ih_i=2|H|$ over four directions, $\max_ih_i\ge|H|/2$.
$H=\{P\}$, $u=0$ and a union over $6v$ plaquettes give the first corollary. On the complement of the second bad set, $X_P>uB^2>0$, so $|J_P|>uB^2$ and $\operatorname{sgn}J_P=(dt)_P$.

**Line 48, (5). HOLDS.** $\dim C^1=4v$. $\operatorname{rank}d_0=v-1$ and $\dim H^1=4$, so $\dim\ker d_1=v+3$ and $r=3v-3$.
Flat fields number $2^4\cdot2^{v-1}=2^{v+3}$. A linear surjection carries the uniform law on $C^1$ to the uniform law on $C$.
On the event $\{X_P>0\ \forall P\}$ one has $J_P\ne0$ and $\operatorname{sgn}J=dt\in C$, and the weight is $e^{\sum|J_P|}$.
Given an environment with $\operatorname{sgn}J\in C$, the event fixes $dt=\operatorname{sgn}J$, which has probability $2^{-r}$.
So $2^{-r}M_0=Z(1-p_T)$ exactly. Ties fall into $p_T$. (4) with $u=0$ gives $p_T\le6vA^{-B^2}$.

**Line 61, uniformity. HOLDS on the account's premises.** With $B=L^K$ the coarse sides are $\ell,L\ell$, so $v$ is fixed. $d_\beta$ increases with $\beta$, so $B^2d_\beta\to\infty$ uniformly.
For $B=L^j$, $v=\ell^4L^{4(K-j)}$ (and $m$ times that). The cap bound $A\ge m_\eta e^{(1-\eta)\beta}$ is correct.
With $\beta\ge g^{-2}+\lambda_\sharp K-c_5$ the exponent of the error is $4K\log L-(1-\eta)B^2\lambda_\sharp K+O(1)$. It tends to $-\infty$ when $(1-\eta)B^2\lambda_\sharp>4\log L$.
The coupling bound is from Sussman and Alpoge's complete account, CA-I 56439–56458 and 56530–56547. The check of row 1341 (`gap-blockstep-check-opus.md`, item 8) already confirmed it. Here it is restated.

**Line 107, (10). HOLDS at every $\beta>0$.** $\sum_h{\bf1}\{\operatorname{sgn}J\in h+C\}={\bf1}\{\operatorname{sgn}J\in Z^2\}$, the product of the cube closure indicators.
In sector $h$, $Z_h=\int a_B\,\mathbb E_t\exp(\sum h_PJ_P(dt)_P)$. Where all $h_PJ_P(dt)_P>0$, $dt=h\operatorname{sgn}J$ is fixed, with probability $2^{-r}$. This gives $2^{-r}M_h$.
On the bad event at $P$ the packet factor is at most one. Dropping the indicator and using (7) on $S_B(P)$ gives $A^{-B^2}Z_0$. Summing $6v$ locations gives $\epsilon Z_0$.
$(1/8)2^{-r}=2^{-3v}$, so $W-W_{\rm cube}=\tfrac18\sum_h(Z_h-2^{-r}M_h)\le8\epsilon Z_0\le64\epsilon W$, using $Z_0\le8W$. The constant 64 is safe (8 would do).
Arithmetic: $\mathbb Eq^2=1/4$ under Haar and odd moments vanish, so $A\ge1+\beta^2/8\ge3/2$ for $\beta\ge2$. $625\log_2(3/2)>365>312$.
Operation count: $6\cdot625=3750$ traces at 84 operations each is $315{,}000$. Sums, conjugations and signs add under $4\cdot10^4$. The total is below $4\cdot10^5$.
Positive claim 2 holds: (5) and (10) both have error $6vA^{-B^2}$, which tends to zero on the tail by line 61.

**Line 63, (6). HOLDS.** $\log Z=\log M_0-r\log2-\log(1-p_T)$ and $v_{L\ell}=mv_\ell$.
So $mr_\ell-r_{L\ell}=3-3m$, and $D(Z)=D(M_0)+3(m-1)\log2-[m\log(1-p_\ell)-\log(1-p_{L\ell})]$. The bracket is at most $(m+1)[-\log(1-\max p_T)]\to0$.
A per-site constant $c^v$ cancels in $D$. The conclusion about the required endpoint follows.

## 3. End class (11) and CH bound (12), lines 131–151. All three HOLD.

**Line 149, coefficients. HOLDS.** For fixed $t$, $z=y\,dt$ is a bijection on plaquette arrays, and $dz=dy$ because $d(dt)=1$.
The plaquette factor becomes $e^{-j_P(1-z_P)}$: one off $S$, $e^{-2j_P}\le e^{-2j_*}$ on $S$.
A cube with $(dz)_D=+1$ gives $g_D(+)=1$ whatever $w$ is. A cube with $(dz)_D=-1$ has a face in $S$, and each face lies in four cubes. So at most $4|S|$ factors $g_D(-)\le G$ occur.
With $G\ge1$, $|a(S,X)|\le(G^4e^{-2j_*})^{|S|}e_*^{|X|}\le b_*^{|S|+|X|}$. Zero cube weights are covered.

**Line 151, locality and estimate. HOLDS.** Sites within sup distance 6 number $13^4$, so the closed degree is at most $7\cdot13^4=d$.
Reads for fixed $(S,X)$: $j_P$ for $P\in S$ reads $y,w$ within one step, and $y$ there needs links based within two. An odd cube lies within one step of $S$ and reads within two, with links within three. $u_x$ for $x\in X$ reads within one, with links within two.
Every $z_{P'}$ read is near the component, and any $P'\in S$ that near lies in the same component, so the off-component values are $+1$. Components are at sup distance at least 7, so their reads are disjoint, and $t,w$ are product variables. So $a$ factors over components.
The recursion $Q_A=Q_{A\setminus\{x\}}+\sum_C\lambda^{|C|}a(C)Q_{A\setminus N[C]}$ is exact for this factorizing family.
$|N[C]|\le d|C|$ gives the factor $e^{|C|}$. With $b_*<1/(64d)$: $8edb_*<e/8$ and $2eb_*<e/(32d)$, so the ratio deviation is below $0.129/d<1/(2d)$. Then $e^{-1/d}\le1-1/(2d)$ closes the induction. $|\log Q|\le7v/d$ on $|\lambda|\le2$.
A connected support of $k$ labels has diameter at most $6(k-1)$, and its reads add 3. For $k<n/32$ the box of radius $6(k-1)+3$ embeds in $T_n$ with no identification. So the $m$ lifts carry the same coefficients, and degrees below $\lceil n/32\rceil$ cancel.
On $|\lambda|=2$, $|m\log Q_n-\log Q_{Ln}|\le14mn^4/d$. The Cauchy tail at $\lambda=1$ is $2\cdot14mn^4/d\cdot2^{-\lceil n/32\rceil}$, which is (12). The scalars $c^v2^{-6v}$ cancel under the cover.
$Q$ is real on $[0,1]$ and has no zero there, with $Q(0)=1$. So the analytic logarithm is the real one at $\lambda=1$.
This is the deletion proof of row 1341 ("A one-block end test", checked in `gap-blockstep-check-opus.md` item 9), carried to a new label set and new constants.

**Line 131 with line 147, (11)–(12) and the example. HOLDS.** The statement follows from lines 149 and 151. $d=199{,}927$, $64d=12{,}795{,}328$, $1/(64d)>7.8\cdot10^{-8}$.
$e^{-18}<1.53\cdot10^{-8}$ and $2^{-25}<2.99\cdot10^{-8}$, so $j_*=9$, $G=1$, $e_*=2^{-25}$ meet the strict bound.
Precision (no change to the claim): dividing out small perturbations of $g_D(+)$ also enlarges $G$ by the same small factor. The strict inequality leaves room for this.
Positive claim 3 holds. The bound needs no upper limit on $j_P$.

## 4. Weak-packet error, line 169. HOLDS.

$|J_P|\le j_*$ implies $X_P=J_P(dt)_P\le j_*$. Markov and directional deletion on $S_B(P)$ give $\Pr\{X_P\le j_*\}\le e^{j_*}A^{-B^2}$. A union over $6v$ plaquettes gives the bad fraction $6v\exp(j_*-B^2d_\beta)$ of $Z_0$, where $Z_0$ is the full Wilson mass.
Splitting the environment by an indicator keeps the sum of the two masses exact. Write $Z=Z_{\rm good}(1+f)$ with $0\le f\le\epsilon'/(1-\epsilon')$, where $\epsilon'$ is the bad fraction.
Then $D(Z)-D(Z_{\rm good})$ is at most $m\log(1+f_\ell)$ in modulus, with $f$ on both tori tending to zero under the choices of line 61. So a strict margin for the good parts survives.

## 5. The failure (14) and its constants, lines 171–184. All three HOLD.

**Line 171, private signs. HOLDS.** A selected link points along $i$ and crosses the $i$-cut. Its $j$-coordinate is $B-1$ and its two other coordinates are interior.
From the link one recovers $j$ (the only endpoint coordinate) and the packet. So different packets use disjoint links.
Plaquettes through it that cross a $k$-cut need $k$-coordinate $B-1$ (link as lower edge) or $0$ (link as upper edge). Only $k=j$ allows this, so exactly one double crossing contains it.
It has two interior transverse coordinates, so it is not a corner pivot. Sign flips commute.
Reading the coarse pivot fixes $t_E$. Reading the private pivot then fixes $y_P$. This triangular map is a bijection, and Haar invariance makes $t,y$ fair and independent.

**Line 173, (13). HOLDS.** The face shifted by $-e_j$ has $j$-range $[B-2,B-1]$ and crosses only the $i$-cut. Its upper $i$-link is the selected link.
Its lower $i$-link has every transverse coordinate interior, so it is not selected. Its $j$-links are internal and have an endpoint $i$-coordinate, so they are not selected either. Both $i$-links lie in one bundle, so $t_E$ cancels.
The interior faces of the packet hold exactly one selected link each. The $B^2-(B-2)^2=4B-4$ rim faces hold none: their lower $i$-link has two endpoint coordinates, and their other links fail the selection pattern. So $|E_P|\le(4B-4)\beta$.
Both sums of $a$ faces lie in the $(i,j)$ planes. Deletion and Markov give $\Pr\{\cdot\le ad_\beta/2\}\le e^{-ad_\beta/2}$ for each. A union over $12v$ sums gives the bound.

**Line 180, (14) and the contradiction. HOLDS.** With identity representatives, every fine link is a product of signs.
At $(t,y)=(1,1)$ every fine trace is $+1$, which is the pointwise maximum of the Wilson density.
$a-(4B-4)=B^2-8B+8>0$ for $B\ge7$, so $\operatorname{sgn}J_P=y_P$.
Flipping one coarse link $E_0$ changes the six $y_P$ on the plaquettes containing $E_0$. $y(dt)=(dl)^2=1$ and $dy=1$ hold at both points.
Each of the six adjacent sums goes from $a\beta$ to $-a\beta$. This gives the ratio at most $e^{-12a\beta}$, which is (14).
On the side of (11), plaquette and cube factors equal one at both points for every $w$. The changed variables are $t_{E_0}$ (based at $x_0$) and six $y_P$ (based at $x_0$ and at $x_0-e_\nu$). Sites within sup distance one of these four sites number $81+3\cdot27=162$. The file's $7\cdot3^4=567$ is a union bound over seven changed variables and is valid.
For $0\le x\le1/2$, $\log\frac{1+x}{1-x}\le\frac{2x}{1-x^2}\le4x$. With $e_*<1/(64d)$: $567\cdot4e_*<1.8\cdot10^{-4}$, so the ratio is above $e^{-1}$.
For $B\ge8$, $\beta\ge1$, (14) gives at most $e^{-432}$. This is a contradiction with any pointwise identification of the two densities with respect to the common product reference.
The bound on the (11) side holds for every $w$, so no continuity of $j,g,u$ is needed. The Wilson side is continuous near the identity, so the gap persists on a set of $w$ of positive measure. At $B=12$, $|J_P|\ge56\beta>9$.
Positive claim 5 holds, with 567 as a safe overcount. The scope is the specified coordinates with $w$ kept, as the file says.

## 6. Pivot-gauge integration and the residual in masses, lines 188–195. Both HOLD.

**Line 188. HOLDS.** A zero-corner pivot of the coarse edge from $c$ to $c+e_\mu$ ends at the origin $o$ of block $c+e_\mu$. The four incoming pivots form a star with leaves $o-e_\mu$.
$o-e_\mu=o'-e_\nu$ forces $o-o'=e_\mu-e_\nu$. Block origins differ by multiples of $B\ge2$, so $o=o'$ and $\mu=\nu$. So the stars are vertex-disjoint.
Star vertices have every coordinate in a two-point cut set, so they lie in four-cube components. A private pivot has two interior coordinates and lies in a square component.
In a square only the lower $i$-link can be selected: the $j$-links would need $j<i$. So distinct private pivots lie in distinct squares, and the union is a forest.
Lemma FOREST is in `gap-ps-disint-max.md` §3.4 (row 957, Claude Fable 5.2, Elitzur's argument). For gauge-invariant $F$ and any $f$, gauge invariance gives $\mathbb E[F\,f(U_{\rm forest})]=\mathbb E[F]\int f\,d{\rm Haar}$. So forest values are product Haar and independent of the gauge-invariant readings.
Their real-part signs are i.i.d. fair. $(t,y)$ is a triangular bijection of these signs, so it is fair and independent, also under any positive-probability gauge-invariant restriction. The orbit average of the constant 1 is 1, so no mass is lost.

**Line 190, (15). HOLDS.** From (5), $Z_0=2^{-r}M_0/(1-p_T)$. From the definitions, $M_0=\pi_0\sum_hM_h=\pi_02^{3v}W_{\rm cube}$.
So $Z_0=2^{3v-r}\pi_0W_{\rm cube}/(1-p_T)=8W_{\rm cube}\pi_0/(1-p_T)$ exactly.
$D(8)=(m-1)\log8$, and the $(1-p_T)$ terms give $o(1)$ as in (6). The remark that (15) is not yet derived for Wilson is a correct statement of scope.
Positive claim 6 holds.

## 7. Everything else

**Line 32, exposed orbits. HOLDS.** The links with all three transverse coordinates interior number $(B-2)^3$, so $h=B^3-(B-2)^3$.
A double crossing at a $\mu$-cut and a $\nu$-cut has its $\mu$-links at $\nu$-coordinates $B-1$ and $0$, and the same holds for its $\nu$-links. So all four links are exposed.
The corner pivot is exposed, so the representative is a function of the exposed orbit. Single crossings see $t_E^2=1$. There are $4v$ bundles of $B^3$ links in $4vB^4$ links.

**Line 34, fieldwise amplification. HOLDS.** With exposed representatives at the identity, each double crossing has $q=1$, so $J_P=B^2\beta$.
Near the identity the pivot has positive real part, so the section is the identity map there and is continuous. The Wilson density is positive and caps have positive Haar mass.

**Line 73, (7). HOLDS.** I re-derived the transfer proof. In one time layer, a sign on an electric plaquette is the central translation of one spatial link by $-1$, because $q(-g)=-q(g)$.
A deleted electric factor is the constant kernel, which is $A$ times the projection onto constants. Both commute with the class-function convolution $C\ge0$ and with vertex-gauge projection.
Cyclicity gives $\operatorname{Tr}\prod_t(C^{1/2}D_tC^{1/2})U_t$. Hölder for $s$ Schatten-$s$ factors and $\|U_t\|\le1$ give $\prod_t(\operatorname{Tr}H_t^s)^{1/s}$.
$\operatorname{Tr}H_t^s=\operatorname{Tr}(D_tC)^s$ is the mass with layer $t$ copied in time. The lost scalars are $A^{-|D|}$.
Repeating in the other coordinates with no deletions clears the remaining orientations, and an orientation with no signs stays without signs under copying.
This extends row 1167 (1), which used the order $C_0\le C_\beta$, and row 1163's $Z_B\le Z$ (`gap-solve10-astra62.md` line 24) to arbitrary sign fields. The inherited side condition (at least four) holds on the fine tori.

**Line 79, cube defects. HOLDS.** A fine cube crossing the three cuts of a coarse cube, at any of $B$ positions in the fourth direction, has its six faces in the six packets. Its face-sign product is $(d\tau)_c$.
A face lies in four cubes, so a cube meets at most 18 others. Greedy selection keeps at least $Bk/19$.

**Line 81, (8). HOLDS.** The based face holonomies of a cube multiply to 1. Central signs change the product to $-1$.
The chord $|g-1|$ is bi-invariant, so $|g_1\cdots g_6-1|\le\sum|g_i-1|$. Some $|g_i-1|\ge1/3$, and $|g-1|^2=2(1-\tau q)$ gives $\delta=1/18$.
Union over at most $6^h$ choices of bad faces. At least $h/2$ chosen faces share a direction. On the event their factors are at most $e^{(1-\delta)\beta}$. (7) gives $u_\beta^{h/2}$ when $u_\beta\le1$.
So $Z_\tau/Z_0\le(6\sqrt{u_\beta})^h\le q_B^k$ when $6\sqrt{u_\beta}<1$.

**Line 89, $|H^2|=2^6$ and the lift. HOLDS.** This is the Künneth count with mod-two Betti numbers $1,4,6,4,1$, as in Lemma SURF in `gap-shrink-box-check-astra.md` line 128.
Flipping all links of a bundle changes the lifted signs by a coarse coboundary and keeps Haar, so $Z_{\tau\,dl}=Z_\tau$.
A fine cube crossing two cuts has its two packet faces in one packet, and its other faces are single crossings with sign $+1$. So the lift of a closed $\tau$ is closed.
A fine coordinate two-torus at fixed transverse position meets each coarse packet of the matching coarse two-torus once, so the periods agree.

**Line 91, the $W_B$ identity and (9). HOLDS.** $\prod_P\cosh J_P=2^{-6v}\sum_{\sigma}e^{\sum\sigma_PJ_P}$. After (2), $Z_\tau=2^{-r}\sum_{c\in C}\int a_Be^{\sum(\tau c)_PJ_P}$.
So $W_B=2^{3v-6v+r}\sum_{[\tau]}Z_\tau=\tfrac18\sum_{[\tau]}Z_\tau$. Each syndrome has a fibre that is one coset of $H^2$, so 64 classes.
At most $\binom{4v}k$ syndromes have size $k$. (8) and $Z_0\le8W$ give $W_B-W\le8[(1+q_B)^{4v}-1]Z_0\le64[\cdots]W$.
Line 103: $\log q_B=(B/19)(\log6+\tfrac12\log u_\beta)$ and $\log u_\beta\le-\delta\beta/2-\log m_{\delta/2}$. This gives $O(B)-B\delta\beta/76$, and $vq_B\to0$ under the stated condition.

**Line 121, all sectors occur. HOLDS.** In each coordinate the crossing-link graph uses the pairs $\{B-1,0\}$ and singletons elsewhere. Products give unit $k$-cube components, whose edges are exactly the crossing links.
On a unit $k$-cube the prescribed $\eta$ is closed, since its three-faces read coarse cubes. A cube is contractible, so $\eta$ is exact there.
Single crossings may get trace $-1$ on this profile, but they only enter $a_B$, whose factors are positive. Pivot representatives change $\operatorname{sgn}J$ by $dt\in C$. So the class is $[\eta]$, $|J_P|=B^2\beta$, and open perturbations give $M_h>0$.

**Line 123, sign-only tests. HOLDS.** $(J,t)\mapsto((da)J,\,at)$ leaves $J(dt)$ and the masses unchanged. So the sign array is uniform on its coset.
On a contractible subbox $Q$, $h|_Q=d\lambda|_Q$. Extend $\lambda$ arbitrarily to $\tilde\lambda$. Then $(hc)|_Q=(d\tilde\lambda\,c)|_Q$, and $d\tilde\lambda\,c$ is uniform on $C$.

**Line 153, the normalization test. HOLDS AFTER CORRECTION (scope of the last inference).** Model 1: $(l,t)\mapsto(lt,t)$ shows $y=dl$ is uniform on $C$ under the weight. The mass is $2^{-r}\sum_Ce^{-2j|z^-|}$.
Model 2: $z=y\,dt$ gives $8^v2^{-6v}\sum_{Z^2}$, with $y$ uniform on the coset of $z$. Restrictions to contractible subboxes agree by line 123. As $j\to\infty$, $D(F_1)\to3(m-1)\log2$ and $D(F_2)\to0$.
Correction: the sentence "In particular … do not imply entry into (11)" does not follow on *any* fixed pair. At $n=64$ the bound (12) is about $28m(64^4/d)/4\approx587m$, which is above $3(m-1)\log2$. So (12) does not exclude model 1 there.
The inference holds for $n$ large enough that the right side of (12) is below $D(F_1)$. Line 160 supplies this at fixed $j=9$ as $n\to\infty$. "The second model realizes (12)" needs $e^{-2j}<1/(64d)$, that is $j>8.18$; $j=9$ works.

**Line 160, the two masses at $j=9$. HOLDS.** $F_1/F_2=2^{3v-r}\sum_C/\sum_{Z^2}=8(1-p_n)$.
I read (Z) in `gap-z2parity-astra.md` lines 397–417 (Codex). The weight per negative plaquette is $u=e^{-18}$, so $b=80u<1.3\cdot10^{-6}$. The minimum size of a nonzero class on side $n$ is $n^2$, and there are $N=6n^4$ roots. This matches the display.
So $p_n\to0$ and $D(F_1)-D(F_2)\to(m-1)\log8$. (12) with $b_*=e^{-18}$ gives $D(F_2)\to0$. Since $3(m-1)\log2>(L/2)\log(13/10)$ for $L\ge2$, the comparison holds.

**Line 197, (16). HOLDS, conditional on the stated cylinder hypothesis.** The Wilson transfer is positive, so the eigenvalues of $U$ lie in $[0,1]$ with top 1. So $\operatorname{Tr}U^{Ls}\le\operatorname{Tr}U^s$ and $\operatorname{Tr}U^s\ge1$.
$L\log\operatorname{Tr}T^s-\log\operatorname{Tr}T^{Ls}=L\log\operatorname{Tr}U^s-\log\operatorname{Tr}U^{Ls}\ge(L-1)\log\operatorname{Tr}U^s$.
$L^4F_0-F_4=L^3(LF_0-F_1)+L^2(LF_1-F_2)+L(LF_2-F_3)+(LF_3-F_4)$. Each term is nonnegative, and the first is at least $L^3(L-1)\log(1+e^{-\ell E})$, using $(\lambda_1/\lambda_0)^s\ge e^{-aEs}=e^{-\ell E}$.
If $aB\to0$ then $n\to\infty$ and (12) tends to zero. This excludes (11) on that sequence, even with $o(1)$ relative errors. The cylinder witness of row 865 is cited, not re-checked here.
The monotonicity is the one used in Lemma Z3 (`gap-shrink-box-check-astra.md` line 25). The lower bound at fixed physical scale is the new part.

**GUIDE and OPEN text.** Line 3 agrees with `gap-blockstep-check-opus.md` items 6 and 7. I did not re-open the PR and main files it names.
Line 5 matches Proposition CH and its correction (`gap-shrink-box-check-astra.md` lines 94–96). Line 38: strict Jensen gives $d_\beta>0$.
Line 105 (OPEN): the computation holds. The exact-class mass in the tilted joint law is $2^{-3v}2^rZ_0$, so the probability is $Z_0/(8W_B)$.
Line 125 (GUIDE): $4\beta\ge4>(\log80)/2$ at $B=2$. The lines 186 and 203 (OPEN) and the RESULT at line 205 agree with the verdicts above. No statement there is marked PROVED.

## Restatement of earlier rows

No main step only restates an earlier row. The block map (2) with (3), (4)–(6), (8)–(10), the class (11) with (12), the model comparison at lines 153–165, (13)–(14), (15) and (16) are new.
Some steps restate earlier rows, and the file credits each one:
- (1) is the center split of `gap-crux-restate.md` §4.4 (Claude Fable 5.2; Mack and Petkova).
- (7) extends row 1167 (1) and row 1163 (1) (Codex) from deletions and twists to general sign fields. The proof is the same transfer and Hölder argument.
- $|H^2|=2^6$ is the Betti count of Lemma SURF (row 1335).
- The proof of (12) is row 1341's deletion and short-cluster argument, applied to new labels.
- Line 160 uses the Peierls bound (Z). Line 188 uses Lemma FOREST (row 957).
- The divergence of the bare coupling at line 61 restates rows 1335 and 1344 (CA-I, Sussman and Alpoge with Claude and Codex).
- The one-direction trace monotonicity in (16) is the one used in Lemma Z3.

## Summary

| Item | Lines | Verdict |
|---|---|---|
| 1 (1), (2), (3) | 11, 18, 26 | HOLDS (3 of 3) |
| 2 (4), (5), tail, (6), (10) | 40, 48, 61, 63, 107 | HOLDS (5 of 5) |
| 3 (11), (12) | 131, 149, 151 | HOLDS (3 of 3) |
| 4 weak packets | 169 | HOLDS |
| 5 (13), (14), constants | 171, 173, 180 | HOLDS (567 is a safe overcount of 162) |
| 6 pivot gauges, (15) | 188, 190 | HOLDS (2 of 2) |
| 7 other statements | 32, 34, 73, 79, 81, 89, 91, 121, 123, 153, 160, 197 | 11 HOLD; line 153 HOLDS AFTER CORRECTION |

The file's OPEN conclusion stands. Entry of the Wilson angular measure into (11), on two tori at a block scale bounded below in physical units, is not derived. The sign theory is controlled. The scalar comparison of the integrated angular masses, $D(W_{\rm cube})$ and the $\pi_0$ term of (15), is the remaining gap.

Checked by hand by Claude Opus 5.5. No numeric run was used.

RESULT: Of 29 PROVED statements in row 1345, 28 HOLD, 1 HOLDS AFTER CORRECTION (line 153: the non-entry inference for the link-coboundary model needs n large enough that (12) is below 3(m-1)log2, as line 160 supplies; at n=64 the bound (12) is about 587m), 0 FAIL; main finding: the center-sign block map (2) is exact and iterates at every coupling, (5) and (10) hold on the first-passage tail, (11)-(12) hold, (14) refutes the pointwise Haar-sign presentation at beta>=1, and admission of the integrated Wilson angular measure into (11) stays OPEN.
