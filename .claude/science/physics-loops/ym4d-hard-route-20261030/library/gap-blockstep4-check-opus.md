# Check of row 1351 (gap-blockstep4-astra62.md), row 1352

Checker: Claude Opus 5.5 (laptop subagent), by hand, line by line.
Author of the checked file: gpt-6.2-astra max (row 1351).
Line numbers refer to library/gap-blockstep4-astra62.md at the commit checked.

Cited rows read: 1342 (definitions of (N-phys), Lemma TP), 1349 (RESULT and the
lines on (N-phys)), 1345 ((1)-(16)), 1348 ((13), (18)-(20)). Row 1340's file was
not read. Each step below was derived again by hand. One numeric run guided item 7.
It is marked GUIDE and is not a proof step.

## 1. Exact gluing of center constraints, and the propagation bound

**Lines 26 (setup) - HOLDS.** Row 1345 (1)-(2) gives the fine mass as
$\int a_B\,\mathbb E_{\xi,h}\prod_P\exp(J_P(-1)^{D_P})$. Here the temporal twist
columns $S$ are added and $h$ is fair. Both packet values are positive. For the
polynomial core I checked the antipode step. $-U$ moves both phase indices by
$3d_K+1$. This changes their sum by an even number, so the equal-parity grid and its
weights are kept. A center split of the discrete rule is then exact.

**Line 28, (2) - HOLDS.** A function with two values is $m+(M-m)\mathbf 1_{k=\eta}$.
Expanding the product gives a sum over $A$ with nonnegative coefficients. The fraction
of $(\xi,h)$ with $D_A(\xi,h)=\eta_A$ is $2^{-\operatorname{rank}D_A}$ when
$\eta_A\in\operatorname{im}D_A$, and zero otherwise. For $A$ equal to all plaquettes
the rank is $(3v-3)+3$. The three stack columns are independent modulo coboundaries,
since they carry independent temporal periods.

**Line 41, (3) and gluing - HOLDS.** The condition $\eta-D_bb\in\operatorname{im}D_i$
is a set of linear equations on $b$, given by a basis of the left kernel of $D_i$. For
gluing I checked closure of the class. Stack the two affine systems in $(b,c)$, with
$c$ the new internal columns. The solution set is affine. Its fibres over the
projection to $b$ are cosets of one subspace, so they have equal size. The averaged
table is therefore again $2^{-r}\mathbf 1\{\text{affine set}\}$. Associativity is
finite Fubini on the fair bits.

**Line 47, sizes - HOLDS.** A box has $4b(b+1)^3$ links and $6b^2(b+1)^2$ faces. Both
are 216 at $b=2$. $4\cdot221^3\approx4.3\cdot10^7<2^{26}$. The elementary cube has 32
links and 24 faces. $2^{24}(4\cdot37^3+24)<2^{42}<2^{43}$. These are counts on
supplied inputs, as the file says.

**Line 51, (4) - HOLDS.** $\mathbb P_+(H\subseteq A^c)\le\mathbb P_+(H_i\subseteq A^c)$.
Summing all masks off $H_i$ rebuilds $w_P$ there and leaves $m_P$ on $H_i$. Here
$\max_ih_i\ge2|H|/4$. Then $m_P\le\min(e^{\beta\Sigma q},e^{-\beta\Sigma q})\le1$. For
the late core this uses $e^{-\beta}P_{K,\beta}(q)\le e^{-\beta}e^{\beta(1+q)}=e^{\beta q}$.
For (13) it uses $R\ge0$. Setting those packet factors to one gives the
twist-averaged fine mass with $B^2|H_i|$ faces deleted, all in direction $i$. Signed
deletion bounds each twist by $A_f^{-B^2|H_i|}Z_0$, and $Z_+\ge Z_0/8$. The
hypothesis $A_f\ge1$ is used, and it is stated.

**Line 58, deletion for the cores - HOLDS.** I checked $2T_j=\chi_j-\chi_{j-2}$
($j=1,2$ directly, then in general from
$\sin(j+1)t-\sin(j-1)t=2\cos jt\sin t$). The coefficient of $\chi_k$ in (13) is
$I_k-I_{k+2}$ ($I_{11},I_{12}$ taken as 0), with $2^{-21}$ taken from $k=0$. The
termwise ratio is $x^2/((k+j+1)(k+j+2))\le(7/6)^2/2=49/72$. So every coefficient is
positive, and the constant one is at least $23/72-2^{-21}>0$. Powers of
$1+\chi_1/2$ have nonnegative character coefficients. Convolution by $\chi_j$ is
$d_j^{-1}$ times the isotypic projection, so it is positive. A twist is a central
translation. It commutes with the convolution and with the gauge average. The
operator premises of row 1345 (7) therefore hold.

**Line 60, (5) - HOLDS.** Given $(y,A)$, the bits $(\xi,h)$ are uniform on the
solutions of $D_A=\eta_A$. So $z=D(\xi,h)$ is uniform on $z_0+V_H$. Here
$\operatorname{im}D$ is the set of closed cochains with zero spatial periods. A
plaquette lies in 4 three-cubes, which gives at most 20 neighbours. The faces in $H$
of one three-cube lie in one component. So each restriction $z|_C$ is closed. Periods
of a component that fits in a box vanish by translating the 2-torus. Hence $V_H$ is
the direct sum of the small-component spaces and a remaining space for the large
components.

**Line 66, (6) - HOLDS.** On the good event the components that meet $U$ are
independent summands that miss $W$. The conditional covariance is then zero. The
number of connected $r$-sets through a root is at most
$(4\cdot20)^{r-1}=80^{r-1}$ (plane trees times the degree). Conditional
Cauchy-Schwarz gives $|\operatorname{Cov}|\le1$. With (4), (6) follows. Numbers:
$A(\beta)\ge1+\beta^2/8\ge3/2$. The core loses at most a factor $1+13\cdot2^{-20}$. Also
$(4/3)^{32}>3^8=6561>5120=80\cdot64$. Line 73 (OPEN) states the scope correctly. The
second term of total covariance is not controlled.

## 2. Removing the spatial closure test

**Line 79, (7) - HOLDS.** The temporal three-cubes give $b_{j+1}=b_j+d_se_j$. With
$b_0$ exact, every $b_j$ is exact. So all spatial cubes close and all spatial periods
vanish. Conversely, closed with zero spatial periods means $b_0$ is exact on
$\mathbb T^3$. Both counts give $3Nt$: $(3v-3)+3$ with $v=Nt$, and
$(2N-2)t+(N+2)t$, from $\operatorname{rank}d_s=2N-2$ and $\dim\ker d_s=N+2$ on
$C^1(\mathbb T^3)$. Uniformity of $D(\xi,h)$ on its image gives the prefactor
$2^{-3Nt}$.

**Line 88, (8) - HOLDS.** $d_sb_j$ and $\pi b_j$ are constant in $j$, because
$d_s^2=0$ and an exact cochain sums to zero on a closed 2-torus. The map
$b\mapsto(d_sb,\pi b)$ on $C^2/\operatorname{im}d_s$ is injective. Shifting all
slices by a static representative is a bijection onto the neutral set. The coset mass
is the twist-averaged fine mass with the static pattern on the packets. That mass is
$\le Z_0\le8Z_+$, by row 1345 (7) with no deletions, or by line 58 for the cores. The
sum over nonzero labels of length $N+3$ gives $(1+\lambda^t)^{N+3}-1$. Coset zero
gives exactly $Z_+$. The running-parity snake makes the plane factor local, with
counting measure on the deterministic bits.

**Line 99, (9) - HOLDS.** A static sign pattern commutes with the three flat flips
that carry the temporal twists, since $d\omega=0$ for a flat $\omega$. So the coset
mass is $\operatorname{Tr}(P_+T_b^{Bt})$. This is $\le Z_0(Bt)$, and the
$Bt$-th roots give $\|T_bP_+\|\le\lambda_0$. The phrase "sufficiently large" is not
needed: the bound holds for every $l$. Normalize the direct sum by $\lambda_0^B$
(coset zero attains it). Lemma TP of row 1342 then gives
$1+s(Bt)\le\operatorname{Tr}R^t\le Y(t)^2/Y(2t)$. All physical neutral eigenvalues
are kept and the vacuum eigenvalue is unchanged. So the physical sector is not
changed, as claimed.

**Line 106 - HOLDS.** With $t=\lfloor n/(512B)\rfloor$ and $N=(n/B)^3$ one has
$N2^{-t}\to0$, uniformly in $\beta$. Remark: (9) already gives the sufficient
test directly, so this accuracy statement is only needed for the converse direction.

## 3. The neutral end class (10)-(11)

**Lines 112-122 (statement and example) - HOLDS.** For the example: $e^4>42.8>40$
from six Taylor terms, so $e^{-2J}<1/40$ for $J\ge2$.

**Line 124 (expansion) - HOLDS.** Each link lies in 6 plaquettes. Hölder with six
exponents $1/6$, applied one link at a time, turns each factor into its conditional
$L^6$ norm. Fubini then gives the full norm. Hence
$|\text{coeff}|\le u^{|F|}\epsilon^{|X|}$. The constraint
$\operatorname{im}D=\{$closed$\}\cap\{\pi=0\}$ is imposed by the average of the
eight characters.

**Line 126 (count $5^{k-1}$, $k\ge6$) - HOLDS.** The true closed neighbourhood is 25
(16 edge-sharing plaquettes in a common cube, 4 coplanar, 4 opposite). The bound 41
is valid. Growth: a proper nonempty subset of a minimal closed set is not closed. Its
first odd three-cube has at most 5 other faces. For $k\ge6$ the words "square" and
"edge" are dual cells. Projecting the dual 2-cycle along the root's two directions
gives a finite 2-cycle in a plane, so it vanishes. Equivalently, the period of the
root's plane through the root is zero. So a second plaquette of the root's
orientation lies in the root's plane. It lies in none of the four three-cubes
through the root. Those cubes need four further distinct faces. Hence $k\ge6$. The
coboundary of one link attains 6.

**Line 128, (12) - HOLDS.** Pieces plus anchors determine $(F,X)$. Disjoint children
have distinct anchors. Numbers: $w\le2/(1-82/256)<2.95<3$, and
$3/4096+(3/8)^6/(5\cdot5/8)=7.32\cdot10^{-4}+8.90\cdot10^{-4}<1.953\cdot10^{-3}=1/512<H$.
So the induction closes.

**Lines 134-136, the two logarithms and (11) - HOLDS.**
$Q_D-Q_{D\setminus p}=\sum_{K\ni p}c(K)Q_{D\setminus N[K]}$. The neighbourhood
removal costs at most $e^{41k/256}$, and on $|s|\le2$ this gives $x^k$. Then
$|{\rm ratio}-1|\le1/512$ and $1-1/512>e^{-1/256}$. Cauchy on radius 2 gives a tail
of $(6v/256)2^{1-j_0}$ per torus. Truncated coefficients are $\chi$-independent and
double under the cover, since supports of degree $<j_0$ fit in boxes much smaller
than the sides. Total: $2\cdot\frac{12v}{256}+\frac{24v}{256}=\frac{48v}{256}$ times
$2^{-j_0}$. Positivity of $Q^\chi(1)$ holds because there is no zero on the disk.
Credit: the low-temperature $\mathbb Z_2$ cochain sum is due to Wegner and to Balian,
Drouffe and Itzykson. The polymer deletion method is row 1341's, as used in row 1345
(12).

## 4. The stability theorem (23)-(24)

**Line 306 (statement) - HOLDS.** The example holds: $e^{-6}<0.0025<1/128$. A window
covers $j$ slices of the $2\times3\times3$ tube, so it has $18j$ vertices. The window
range is $H<j\le\lfloor T/2\rfloor$ at both periods. This is stricter than line 295,
which would allow $j\le T$ at period $2T$. Either choice works.

**Line 321 (expansion with windows) - HOLDS.** $\prod_W(1+(e^{\phi_W}-1))$ is expanded.
Sup norms come out of the expectation, and Hölder treats the rest as in (10). A
window that reads a surface plaquette has a support that overlaps that plaquette's
enlarged support. So any dependence of a window on $z=1_F$ stays inside one
component. Coefficients and characters factor over components.

**Line 323 (constants and tree bound) - HOLDS.** A vertex lies in
$|\{0,1\}^4|\cdot6=96$ enlarged supports. $48\theta=3.7\cdot10^{-4}$. The plaquette and
surface part is
$96[2^{-30}e^{48\theta}+(5e^{48\theta}/128)^6/(5(1-5e^{48\theta}/128))]
\approx1.34\cdot10^{-6}<2^{-19}=1.91\cdot10^{-6}$. With (23) the total is
$<2^{-18}=\theta/2$. Children: $\prod(1+w)\le\exp(\sum_{a\in{\rm supp}}\theta)\le e^{L\theta}$.
So weights times $e^{2\theta L}$ have rooted sum $\le\sum we^{3\theta L}<\theta/2$, by
induction on height.

**Line 330 (deletion, volume, topology) - HOLDS.** Removing $\operatorname{supp}K$
costs $\le e^{\theta(|{\rm supp}K|-1)}$. On $|s|\le e^\theta$ the marking costs
$e^{\theta\deg}$. With $\deg\ge|{\rm supp}|$ this gives $e^{2\theta L}$ per piece. So
$|{\rm ratio}-1|\le\theta/2$, the log is $<\theta$, and $|\log Q^\chi|\le v\theta$.
Terms of degree $<j_0$ have connected support of at most $j_0$ vertices. They fit in
a contractible box, and their windows have $18j<j_0\le T/8$, so they exist on both
covers. The tail is $v\theta e^{-\theta j_0}/(1-e^{-\theta})<2ve^{-\theta j_0}$ per
torus, and $4v$ at $2T$. Total $8ve^{-\theta j_0}$. The constants $2^{-30}$, $1/128$,
$\theta=2^{-17}$ and 96 all check.

**GUIDE (size).** With $T=\lfloor m/512\rfloor$, the bound (24) falls below
$\log(3/2)$ only near $m\approx2^{36}$ coarse sites per side. A run of the closed
formula over $m=2^x$ fails at $x=35$ and passes at $x=36$. This is consistent with
"sufficiently large" at line 319 and with $n\ge2^{70}$.

## 5. Strip elimination at order-one coupling, and the tail below 2^(-90)

**Line 198 - HOLDS.** With an even transverse sum, no spatial plaquette has two
selected links. The temporal plaquettes in the selected direction stay inside one
column. $R=e^{2\beta}$, or $(1+13\cdot2^{-20})e^{2\beta}$ for (13).

**Line 200, (17) - HOLDS.** Doob-transform the path law to end at $y_0$. Each
transition is $\ge R^{-1}\nu$, so the oscillation contracts by $1-1/R$ over $h-1$
steps. The test lies in $[1/R,R]$, and the minimum is $\ge1/R$. This gives
$1+(R^2-1)(1-1/R)^{h-1}$. Integrating the cross ratio over $x_0,y_0$ gives (17).

**Line 208 - HOLDS.** The seam rewriting is an identity. $e^{14/3}<107<256$.
$(1-1/256)^{16384}<2^{-64}$, so $\delta_h<2^{16-64}$.

**Line 210 (arithmetic) - HOLDS.** $286+220=506$. The moment formula on $S^3$ is
$\prod(2k_i-1)!!/(2^K(K+1)!)$. $1771+1540+1330=4641<4700$. The per-step total is about
$3.4\cdot10^9$, from the kernel ($\sim1.5\cdot10^9$), the moments ($\sim1.3\cdot10^9$)
and the products ($\sim5\cdot10^8$). Over 16385 steps this is about $2^{45.7}<2^{48}$.

**Line 212 - HOLDS.** "$h/R$ grows as a power of $n$" needs an intermediate exponent
$2\limsup\beta/\log n<\alpha''<\alpha$. That exponent exists because the inequality
is strict. The slope premise is named, as the file says.

**Lines 269-286, (21) - HOLDS.** $W_{i,r}/W_{i-1,r-1}\div g_{i,h}=\mathbb E(fg)/(\mathbb Ef\,\mathbb Eg)$
for the common path, whose endpoints are $h-2$ steps apart. The four-variable integral
of the cross-ratio bound gives both directions with $1+\delta_{h-2}$, independent of
$r$. Closing: $\operatorname{Tr}K_T^p$ lies within $(1+\delta_T)^{\pm p}$ of $s_0^p$.
The open/closed difference is $O(1)$. The telescoped increments follow by the
memory bound. $p\to\infty$ gives (21).

**Line 288 - HOLDS.** The columns are conditionally independent. With $h=C\log n$:
$n^4R^2e^{-(h-3)/R}\to0$ for $C>4R$. The cost $<2\cdot2^{48}$.

**Line 290, (22) - HOLDS.** $|\phi_{i,j}|\le\log(1+\delta_{j-3})\le2^{16}e^{4/256}e^{-j/256}<2^{17}e^{-j/256}$.
A link is read by at most $\max(4j,2(j-1))\le8(j+1)$ windows. With $d=3/1024$:
$1/(1-e^{-d})<342<2^9$, and $e^{-48.003}<2^{-64}$. The total is
$2^{20}\cdot2^{25-64}=2^{-19}<2^{-18}$. The exact value is near $2^{-26}$.

**Line 332 (tail passes (23)) - HOLDS.** $e^{14/3}<(11/4)^4\cdot2\approx114.4$, so
$R<128$ with the core factor. Then
$\|\phi\|\le2^{14}e^{4/128}e^{-j/128}<2^{15}e^{-j/128}$. At most $18j$ windows
contain a vertex. $54\theta<1/1024$ and $\|e^\phi-1\|\le2\|\phi\|$. Then
$1/(1-e^{-7/1024})<147<2^8$, and $e^{-112.007}<e^{-111}<2^{-148}$ (from $e^3>16$). This
gives $36\cdot2^{15}\cdot2^{23}\cdot2^{-148}<2^{-104}<2^{-90}$. The exact value is near
$2^{-119}$. The locality paragraph holds: center vertex signs act inside a contractible
tube, the integrated column links absorb them by Haar invariance, and a twist is a
closed cochain there. The sup-norm bound does not depend on the reference law. So
(23) holds whatever law the remaining links have. Whether the remaining short factors
fit the plaquette part of the class is a separate question, and line 338 marks it
OPEN.

## 6. The winding bound

**Lines 290-295 (winding term) - HOLDS.** Telescoping gives
$g_{i,H}\prod_{H<j\le\lfloor T/2\rfloor}e^{\phi_{i,j}}=g_{i,\lfloor T/2\rfloor}$ exactly.
(21) with $h=\lfloor T/2\rfloor\ge3$ bounds the remainder per column by
$2\log(1+\delta_T)+T\log(1+\delta_{\lfloor T/2\rfloor-2})$. Fix $R<256$ and
$T=\lfloor n/512\rfloor$. Times $n^3/2$ this is $O(n^4R^2e^{-T/(2R)})\to0$. At the
period $2T$ with the same window range, the same bound with $2T$ in front also
vanishes. Positivity carries the bound through the exterior integral.

## 7. Does (24) give a neutral seed in the form the gap clause needs?

**Verdict: yes in form, only conditionally in substance, and the file does not claim
more.** Row 1342 defines (N-phys) as follows. On one admissible physical side, for all
late $j$: $4\mid n_j$, $n_j\ge2^{70}$, and some $3\le u_j\le n_j/512$ has
$s_j(u_j;n_j^3)\le1/2$. Here $s$ is the excited neutral trace of the Wilson transfer.
Row 1349 accepts this neutral form, or its checked subsequence variant, as enough for
the matched gap clause. That clause also needs the OPEN continuum datum, (H2) and (TOT).
Lemma TP gives $1+s(u)\le Z_+(u)^2/Z_+(2u)$. So a two-period neutral defect below
$\log(3/2)$ for the **Wilson** masses gives (N-phys) at that cutoff.

The bound (24) is about the end-class model's own twist-averaged mass. Its sum over
$z\in\operatorname{im}D$ is exactly the eight-temporal-twist average, by (7). So it has
the right sector. With $T=\lfloor m/512\rfloor$ the fine period is $u=BT\le n/512$.
It feeds (N-phys) only if all of the following hold:
(i) mass-preserving block maps carry the Wilson masses at $u$ and $2u$, exactly or with
$o(1)$ error in the defect, into one model obeying the strict (10) bounds and (23);
(ii) all scalar normalizers are field-independent per site and double under the cover;
(iii) this happens at one fixed physical coarse mesh with coarse side about $2^{36}$
or more, uniformly for all late cutoffs.
The end model has no transfer operator of its own here. Lemma TP must be applied to
the Wilson masses, as line 122 says. Items (i) to (iii) are the OPEN step at lines
338 and 351. (24) gives no periodic (SEED-L). The file says this at line 353.

## 8. Everything else

**Line 11, (1) - HOLDS.** $P_{K,\beta}(\pm q)\ge1$ and $0\le R(\pm q)\le2^{-d_K}$ hold on
$[-1,1]$. Each link has degree $\le6d_K$, so the cubature is exact. The eight
two-sided inequalities add, and $T_t$ has $6tn^3$ plaquettes. The errors at $u$ and
$2u$ are one-sided with the same sign, so $|2a-b|\le12un^3\varepsilon$. Also
$12un^3L^{-8(K+1)}\le(12/512)\ell^4L^{-4K-8}\to0$. **Line 20** HOLDS: with Lemma TP,
$D^{\rm fin}_+<\log(3/2)-\eta$ gives $D_+<\log(3/2)$ eventually, hence $s<1/2$.

**Line 140 - HOLDS.** $6\cdot32\cdot2^{40}\approx2.1\cdot10^{14}<10^{15}$.

**Lines 142-146, (13) - HOLDS.** $C_s$ commutes with right translations. It has
Hilbert-Schmidt norm 1 and kills even functions. $R_iR_j=R_k=-R_jR_i$ on odd
functions, and $I,J,IJ$ are skew. So $v,Iv,Jv,IJv$ are orthonormal, the top singular
value has multiplicity $\ge4$, and $\|C_s\|\le1/2$. The orbit mean is
$s_1*s_2*s_3*s_4(H)$, with modulus $\le1/4$. So each sign has probability
$\ge3/8$. In (13), $\|w(1)/a\|_6\ge\|\mathbf 1_E\|_6-\epsilon=(3/8)^{1/6}-\epsilon\approx0.849>1/40$.

**Line 157, (14) - HOLDS.** Zero-cut plaquettes lie in one box, so the box laws are
independent. Absorbing $L_E$ into the conditional law of the crossing links is exact.

**Line 163, (15) - HOLDS.** A box variable is read by $8+24=32$ labels, and a bond
seed by 6 plaquettes. So Hölder with exponent 32 applies. Neighbourhood
$\le4\cdot32+20$. $w\le2e^{320/1024}<2.74$.
$3\cdot2^{-14}+(5/16)^6/(5\cdot11/16)=1.83\cdot10^{-4}+2.71\cdot10^{-4}<1/2048$. $10v$
labels. Tail $2\cdot20v/1024+40v/1024$.

**Lines 175-192, (16) - HOLDS.** Each selected tangential link lies in exactly one
single-cut plaquette of the face. So the other factors give a measure on $u$ that
does not depend on the eight links. Integrating each $A_b$ against $\pi(A_b)$ gives
$r_1\pi(M_b^{-1})$. The $u$'s telescope to a conjugate of the $D$-loop, and the $D$
integral is 1. So the coefficient is $b_*r_1^4$, and the infimum is
$r_1^8/(1+r_1^8)$. The incidence count is $(3+4)\cdot2-3=11$. The density is
$\ge e^{-22\beta}$ per box. $r_1=\beta/(4+\beta I_3/I_2)\ge3/7>2/5$ at $\beta=2$, and it
increases on the band. The final number is $2.1\cdot10^{-4}>2^{-14}$. The Bessel
facts are standard. The one-link multipliers are those of Sussman and Alpoge, with
Claude and Codex.

**Lines 218-220 - HOLDS.** Grouped links of different boxes are at sup distance $\ge3$.
$k\le3(b+1)^3$. At most $36(b+1)^2(n/b)^3\le144n^3/b$ kept links per slice.
$R^k\le n^{1/4}$ and the error is $n^{1/2}e^{-(h-1)n^{-1/4}}$.

**Line 222 - HOLDS.** The mixed derivative is
$\beta^2\|K^{d/2}XK^{(t-d)/2}\|_{\rm HS}^2/\operatorname{Tr}K^t$. It is nonzero because
$C_\beta$ is injective (all $I_{j+1}>0$) and $X\neq0$. The one-point mean vanishes by
reflection.

**Line 232, (18) - HOLDS.** $(1/8)2^{-(3v-3)}=2^{-3v}$ and $\sum_z\prod w=2^{6v}\prod c_P$.
The three planes have disjoint plaquettes. $P(\text{parity }0)=(1+\prod h)/2$. The
$-3\log2$ in the defect is correct: $2(3v-3)-(6v-3)=-3$.

**Line 246, (19) - HOLDS.** The fibre over a syndrome is an $H^2$-torsor (64
cosets). $\pi$ restricted to $H^2$ is onto $\mathbb F_2^3$, which gives 8 cosets.
$\binom{4v}{k}$ cube sets. With row 1345 (8) and $Z_0\le8Z_+$:
$\mathcal A_\pi\le Z_+ +Z_0[(1+q_B)^{4v}-1]$. The cap bound and $\beta\to\infty$ on the
tail follow row 1345.

**Line 257, (20) - HOLDS.** Combine the comparison of (1) for every $\tau$ with (19)
at both periods.

**Lines 340-347, (25) - HOLDS.** The zero-field prefix leaves Haar at $i-1$, so
$W_{i-1,H-1}=A(\beta)^{H-2}A(4\beta)$. The ratio is (25). $r_j(b)=I_{j+1}(b)/I_1(b)$.
$I_3/I_2\ge\beta/(6+\beta^2/8)>2/7$, $r_2(\beta)>4/35$, and $r_2(4\beta)=1-4r_1/(4\beta)>1/2$.
So the spin-2 multiplier is $>1/35$ with multiplicity 9. A rank-$\le9$ kernel
vanishes on a unit vector of the 10-dimensional space, which gives the operator gap.
The Schur test turns a pointwise relative error into an operator error.

**OPEN and GUIDE lines 7, 73, 194, 214, 228, 338, 351, 353, 355.** These agree with the
verdicts above. None is labelled PROVED.

**Restatement.** No main step only restates an earlier row. Three are close
adaptations. (1) is the argument of row 1348 (19), applied to the neutral two-period
test with Lemma TP. (4) is the directional-deletion estimate of row 1345 (4) and (7),
applied to the hole law of (2). (19) is row 1345 (9) with the plane filter, which
gives the constant 8 in place of 64. (11) and (24) reuse the polymer method of rows
1341 and 1345 (12). Their end class, its $L^6$ test and the window extension are new.
The new content is (2)-(3), (5)-(6), (8)-(9), (13), (14)-(16), (17), (21)-(22) and
(25).

RESULT: Of 51 PROVED statements in row 1351, 51 HOLD, 0 need correction, 0 FAIL. Main finding: the exact affine gluing (2)-(3), the hole and covariance bounds (4)-(6), the closure-free enlargement (7)-(9), the neutral end class (11), the stability theorem (24) with 2^(-30), 1/128, theta=2^(-17) and 96 supports, the strip contraction (17) and (21), the tail bound (well below 2^(-90)) and the winding bound all hold; (24) has the (N-phys) form but needs coarse side about 2^36 and an exact mass-preserving entry of the Wilson short factors, which stays OPEN, so this row gives no (N-phys), SEED-L or mass gap.
