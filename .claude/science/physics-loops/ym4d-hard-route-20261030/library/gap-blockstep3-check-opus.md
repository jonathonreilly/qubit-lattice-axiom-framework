# Check of row 1348: gap-blockstep3-astra62.md (FINISH row 1350)

Checker: Claude Opus 5.5, by hand, line by line. Each step was derived
again here. Numeric runs, where used, only guided the check.

File checked: `library/gap-blockstep3-astra62.md` (row 1348, gpt-6.2-astra).
Target: Proposition CH, Section 6.1 of `library/gap-shrink-box-fable.md`,
as corrected by `library/gap-shrink-box-check-astra.md`.

Line numbers refer to the checked file at the commit this check was made on.

The target was read at commit `21caea827`. It has 45 statements marked PROVED,
at lines 13, 23, 30, 36, 42, 55, 61, 63, 71, 77, 79, 83, 89, 91, 101, 103, 110,
116, 118, 120, 127, 129, 131, 138, 151, 163, 170, 176, 178, 186, 197, 199, 208,
217, 219, 225, 227, 229, 236, 245, 251, 257, 268, 276 and 280.
Context read: row 1345 check (`gap-blockstep2-check-opus.md`), Section 6.1 of
`gap-shrink-box-fable.md` with its check `gap-shrink-box-check-astra.md`,
the definition of the first-passage window in `cl1.md`, and the flow bound (26)
in `in1.md`. Not read: `gap-blockstep-fable.md`.
Conventions used below: $q=\operatorname{tr}/2$, $x=\beta/2$ where stated,
$r_j=I_{j+1}/I_1$, $R_n=I_{n+1}/I_n$, $A_0(x)=2I_1(x)/x$.

## 1. The minorant (13), line 186. HOLDS.

**Series.** $e^{xe^{it}}e^{xe^{-it}}=e^{2x\cos t}=e^{\beta q}$. The coefficient of
$e^{ijt}$ is $\sum_k x^{2k+j}/(k!(k+j)!)=I_j(\beta)$. So
$e^{\beta q}=I_0+2\sum_{j\ge1}I_jT_j(q)$, as stated.

**Chebyshev tail.** $(k+11)!\ge 11!\,12^k$, so $I_{11}\le x^{11}e^{x^2/12}/11!$,
and $x^2/12\le 49/432$. The term ratio from $I_j$ to $I_{j+1}$ is
$x/(k+j+1)\le x/12=7/72$ for $j\ge11$. By hand: $(7/6)^{11}\approx5.450$,
$11!=39916800$, $e^{49/432}<1.121$, so $I_{11}<1.53\cdot10^{-7}$.
Then $2\sum_{j>10}I_j\le 2I_{11}\cdot72/65<3.4\cdot10^{-7}<4\cdot10^{-7}$.

**Truncation $k\ge17$.** For $j\le10$ the first omitted term is
$x^{34+j}/(17!(17+j)!)\le(7/6)^{10}(49/36)^{17}/(17!)^2$, since $x^j\le(7/6)^{10}$
and $(17+j)!\ge17!$. Later terms have ratio at most $(49/36)/18^2<1/2$, which
gives a factor 2. The weights are 1 for $j=0$ and 2 for $1\le j\le10$, total 21.
So the bound $42(7/6)^{10}(49/36)^{17}/(17!)^2$ is right. Its value is about
$2.9\cdot10^{-25}$, far below $2^{-65}\approx2.7\cdot10^{-20}$.

**Shift and ratio.** The unshifted error is below
$4\cdot10^{-7}+3\cdot10^{-25}<2^{-21}\approx4.77\cdot10^{-7}$, since $|T_j|\le1$.
Subtracting $2^{-21}$ gives $0<e^{\beta q}-P_\beta\le2^{-20}$.
$P_\beta\ge e^{-7/3}-2^{-20}>0.0969>1/13$.
So $R=(e^{\beta q}-P_\beta)/P_\beta\in[0,13\cdot2^{-20}]$.
The coefficients are rational at rational $\beta$, and the degree is ten.
At $\beta=0$, $R=2^{-21}/(1-2^{-21})$, which is inside the bound.
Every rational tail constant in lines 191–195 is correct.

## 2. The finite-state core (15), lines 197–219. All five HOLD.

**Line 197, exact discretization. HOLDS.** A link in direction $\mu$ lies in
two plaquettes for each of three planes $(\mu,\nu)$, so in six. $q(AuB)$ is
real linear in $u$, and $u^{-1}=\bar u$ is linear. So the core has degree at
most 60 in one link. The rule: phases $e^{i\pi a/31}$, $a,b'\in\mathbb Z/62$,
$a\equiv b'\pmod 2$. This is an index-two subgroup $H$ of $(\mathbb Z/62)^2$.
A character $(m_1,m_2)$ is trivial on $H$ iff $m_1+m_2\equiv0$ and
$2m_1\equiv0\pmod{62}$, that is both $\equiv0$ or both $\equiv31$.
A nonzero such pair has $|m_1|+|m_2|\ge62$. A monomial of real degree $n$ has
$|m_1|+|m_2|\le n$. So the phase average is exact up to degree 61.
The surviving monomials are $x^\alpha(1-x)^\gamma$ with $\alpha+\gamma\le30$.
Sixteen Gauss–Legendre nodes are exact to degree 31. Under Haar, $x=|z_1|^2$
is uniform and the phases are independent and uniform. The count
$2\cdot31^2\cdot16=30752$ is right. A tensor rule exact in each variable is
exact on polynomials of bounded degree in each variable separately, by Fubini
one variable at a time. This gives the conditional exactness.

**Line 199, (14). HOLDS.** Plaquettes sharing a link with $p$ number at most
$4\cdot6=24$, so the closed neighbourhood is at most $24^2=576$ (an overcount).
$R\ge0$ and $P>0$ give $z_C\ge0$. $R\le b$ gives numerator
$\le b^{|C|}\times$(the Haar denominator). The denominator is a polynomial of
degree at most 60 in each link of $E_C$, so $\nu$ and $\mu$ agree on it.
So $0\le z_C\le b^{|C|}$. Its arguments are the links of $N_C$ off $E_C$.

**Line 208, (15). HOLDS.** I re-derived it.
$Z=e^{-\beta|\mathcal P|}\sum_S\int d\mu\prod_pP(q_p)\prod_{p\in S}R(q_p)$.
Fix $S$ and $E_S=\bigcup_{p\in S}\partial p$. Off $E_S$ the integrand is
polynomial of degree at most 60 in each link, so $\mu$ may be replaced by $\nu$
there. Let $C_1,\dots,C_m$ be the components of $S$. Two facts follow from
the adjacency rule. First, $E_{C_i}\cap E_{C_j}=\emptyset$: a common link of
$p\in C_i$, $p'\in C_j$ makes $p\sim p'$ with $q=p$. Second, no plaquette meets
both $E_{C_i}$ and $E_{C_j}$: it would make $p\sim p'$. So the $E_S$ integral
factors into the numerators of (14). Each numerator is $z_{C_i}$ times its
$\nu$-denominator. The denominators and the plaquettes off $N_S$ recombine into
$\int d\nu^{E_S}\prod_pP$. The arguments of $z_{C_i}$ lie off $E_S$.
Components of $S$ are pairwise non-adjacent, and any pairwise non-adjacent
family of connected sets is the component set of its union. So the sum over
$S$ is the sum over compatible families. Nothing uses contractibility, so
winding components are included.

**Line 217, polymer bound. HOLDS.** $b=13\cdot2^{-20}\approx1.240\cdot10^{-5}$ and
$1/(64d_0)\approx2.713\cdot10^{-5}$, so $b<1/(64d_0)$.
The recursion $Q_A=Q_{A\setminus p}+\sum_{C\ni p}s^{|C|}z_CQ_{A\setminus N[C]}$
is exact. $|N[C]|\le d_0|C|$, so the quotient costs at most $e^{|C|}$.
Rooted connected sets of size $k$ number at most $(4d_0)^{k-1}$.
The deviation is at most $2eb\sum_k(8ed_0b)^{k-1}=2eb/(1-8ed_0b)$.
With $b<1/(64d_0)$ this is below $(e/32)/(1-e/8)/d_0<0.129/d_0<1/(2d_0)$.
Then $1-1/(2d_0)\ge e^{-1/d_0}$ closes the induction.
For the multivariate form, a monomial on a disconnected support factorizes
after the other variables are set to zero, so its log coefficient vanishes.
The scope sentence (this proves no bound on $D(Z)$) is correct.
This is the deletion proof of rows 1341 and 1345, with new activities.

**Line 219, Chebyshev bound. HOLDS.** Without a scalar, $0<P\le e^{\beta q}\le1$
on $[-1,0]$. (With a scalar $c$ the same proof runs with $|P|\le c$ there and
$P(1)\ge ce^\beta/(1+b)$; only the ratio matters.) Map $[-1,0]$ to $[-1,1]$ by
$y=2q+1$, so $q=1$ goes to $y=3$. If $p(3)>T_d(3)$, scale $p$ so $p(3)=T_d(3)$.
Then $|p|<1$ on $[-1,1]$, and $T_d-p$ alternates at the $d+1$ extrema of $T_d$.
That gives $d$ zeros in $(-1,1)$ and one at 3, so $T_d=p$, a contradiction.
$T_d(3)=\tfrac12[(3+\sqrt8)^d+(3-\sqrt8)^d]<(3+\sqrt8)^d$.
So $d\ge(\beta-\log(1+b))/\log(3+\sqrt8)$, as stated.

## 3. The late-datum trajectory (18) and the two-volume bound (19), lines 257–274. Both HOLD.

**Line 257, (18). HOLDS.** $e^{\beta(q-1)}=e^{-2\beta}e^{y}$ with
$y=\beta(1+q)\in[0,2\beta]$. The first omitted term is
$y^{d+1}/(d+1)!\le(2e\beta/(d+1))^{d+1}$, by $n!\ge(n/e)^n$.
$d_K\ge\lceil12\beta\rceil$ gives $d+1>12\beta$, so $2e\beta/(d+1)<e/6<1/2$.
Later term ratios are $y/(j+1)\le2\beta/(d+2)<1/6$. So the tail is at most
$2\cdot2^{-(d+1)}=2^{-d}$. $P_{K,\beta}\ge1$ because $y\ge0$. So
$0\le R\le2^{-d_K}$. Also $2^{\lceil\log_2L\rceil}\ge L$ gives
$2^{-d_K}\le L^{-8(K+1)}$.
Cubature: each link has degree at most $6d_K$. With phases modulo
$2(3d_K+1)$ of equal parity, a nonzero surviving pair has
$|m_1|+|m_2|\ge6d_K+2$, by the subgroup argument of item 2. The radial degree
is at most $3d_K$. $n=\lceil(3d_K+1)/2\rceil$ Gauss nodes are exact to degree
$2n-1\ge3d_K$. So the rule is exact to degree $6d_K$. The same rule on both
tori, and (14) with the new $R$, keep the masses exact. The polymer bound of
item 2 needs only $2^{-d_K}<1/(64d_0)$, which holds once $d_K\ge22$.

**Line 268, (19). HOLDS.** $1\le\prod_p(1+R)\le e^{|\mathcal P_T|2^{-d_K}}$
pointwise, and the core is positive. So
$0\le\log Z-\log Z^{\rm fin}\le|\mathcal P_T|2^{-d_K}$.
$L^4|\mathcal P_{T_\ell}|=|\mathcal P_{T_{L\ell}}|$. So $D(Z)-D(Z^{\rm fin})$ is
a difference of two numbers in $[0,M]$ with $M=|\mathcal P_{T_{L\ell}}|2^{-d_K}$,
and its modulus is at most $M$. With physical side $L\ell$ and spacing $L^{-K}$
the torus has $(L\ell L^K)^4$ sites and $6(L\ell)^4L^{4K}$ plaquettes. So
$M\le6(L\ell)^4L^{4K}L^{-8K-8}=6(L\ell)^4L^{-4K-8}$. This matches (19).
The tori are those of `gap-shrink-box-fable.md` 3.1, with
$\Phi_L=L^4F_{K,\ell}-F_{K+1,\ell}$ (row 1332), so the physical reading is right.
Both tori use the same $(K,\beta)$, so the same $d_K$. The bound tends to zero
uniformly on the window, so the uniform limsup is the same for $Z$ and
$Z^{\rm fin}$. No comparison between different $\beta$ is used.

## 4. Necessity of the cost up to constants, line 276. HOLDS in its stated scope.

**Upper side.** The flow bound (26) of `in1.md` gives
$\lambda_\sharp(j-i)-c_5\le x_i-x_j\le B_\sharp(j-i)$. With $x_0=\beta$,
$x_K\le g^{-2}+B_\sharp<x_{K-1}$, this gives
$g^{-2}+B_\sharp+\lambda_\sharp(K-1)-c_5<\beta\le g^{-2}+B_\sharp(K+1)$.
So $cK\le\beta\le CK$ for large $K$, and $d_K=O(K)$.
The alphabet has $(6d+2)^2/2\cdot\lceil(3d+1)/2\rceil=O(d^3)=O(K^3)$ points.

**Lower side.** The degree bound of line 219 needs only bounded relative
accuracy, and $\beta\ge cK$, so $d\ge c'K$. For points: polynomials of degree
at most $n$ restricted to $S^3$ span $\bigoplus_{j\le n}\mathcal H_j$, of dimension
$\sum_{j\le n}(j+1)^2$. These are the matrix entries of the spin-$j/2$
representations, independent by Peter–Weyl. With fewer nodes than this
dimension for $n=3d$, some nonzero $f$ of degree at most $3d$ vanishes at every
node. $|f|^2$ has degree at most $6d$, positive Haar integral and cubature sum
zero, whatever the weights. So at least $\sum_{j=0}^{3d}(j+1)^2\ge9d^3$ nodes are
needed. Upper and lower orders agree, so the scaling is sharp up to constants.

**Scope.** The claim is for schemes that demand both pointwise relative
accuracy and exactness on all polynomials of degree $6d$. The file says this,
and says it is not a lower bound on a symbolic proof. I agree.

## 6. The polynomial form (20) of the remaining test, line 280. HOLDS on the account's premises.

By (26), $\beta\le g^{-2}+B_\sharp(K+1)<h_0+h_1K$ on $\mathcal W_K(g)$. So the
window-wide $d_K$ still has $d_K+1>12\beta$, and (18)–(19) hold unchanged.
$P_{K,\beta}(q)=\sum_j\beta^j(1+q)^j/j!$ with $1+q\ge0$. The nodes are algebraic:
roots of a Legendre polynomial, their square roots, and roots of unity.
The weights are positive algebraic. So $F_{K,T}(\beta)=\int d\nu\prod_pP_{K,\beta}$
is a polynomial in $\beta$ with nonnegative real algebraic coefficients.
$Z^{\rm fin}(T)=e^{-2\beta|\mathcal P_T|}F_{K,T}$ and
$L^4|\mathcal P_{T_\ell}|=|\mathcal P_{T_{L\ell}}|$, so the scalars cancel in $D$.
Then (20) reads $D(Z^{\rm fin})\le\log\gamma$.
Forward: if $D(Z)\le\phi_*<(L/2)\log(13/10)$ for $K\ge K_0$, choose rational
$\gamma$ in $(e^{\phi_*},(13/10)^{L/2})$; (19) gives (20) for larger $K$.
Backward: (20) and (19) give $D(Z)\le\log\gamma+o(1)$; any $\phi_*$ strictly
between $\log\gamma$ and $(L/2)\log(13/10)$ works at late $K$.
So the equivalence holds as stated. The last sentence, that (20) still needs
whole tori and all depths, is correct.

## 5a. The eight-link face-integral enclosure, lines 163–178. All four HOLD.

**Line 163, cubature. HOLDS.** At $B=2$ each site of $F=\{0,1\}^3$ has three
neighbours in $F$ (single cuts, field $\le\beta$ each) and, for each transverse
direction, exactly one double cut (field $\le\beta$). So $|b|\le6\beta\le14$.
The phase subgroup argument of item 2 with modulus 22 gives exactness up to
real degree 21. Surviving radial degree is at most 10, and six Gauss nodes are
exact to degree 11. Gauss weights are positive. $d=242\cdot6=1452$.

**Line 170, relative accuracy. HOLDS.** For SU(2) with Haar,
$\int e^{xq}\chi_j=I_j(x)-I_{j+2}(x)=2(j+1)I_{j+1}(x)/x$. So
$e^{xq}/A_0(x)=\sum_j(j+1)r_j(x)\chi_j$, and the $j$-th translated summand has
sup at most $(j+1)^2r_j$. Terms with $j\le21$ are integrated exactly, and Haar
kills $j\ge1$. So the relative error is at most $\sum_{j\ge22}(j+1)^2r_j(|b|)$,
and $r_j(|b|)\le r_j(14)$ by monotonicity (line 127).
$r_j(14)=I_{j+1}(14)/(7A_0(14))$ and $I_{j+1}(14)\le7^{j+1}e^{49/(j+2)}/(j+1)!$
give the displayed bound. By hand: $7^{22}/23!\approx1.512\cdot10^{-4}<1/6500$;
$e^{49/24}\approx7.70<8$; the series terms of $A_0(14)=\sum49^k/(k!(k+1)!)$ at
$k=4,5,6$ are about $2001.7$, $3269.4$, $3814.3$, sum $9085>8192$.
$R_{j+1}(14)\le7/(j+2)$ gives the term ratio $7(j+2)/(j+1)^2$, which is
$168/529<1/3$ at $j=22$ and decreasing. So the sum is at most
$(3/2)\cdot529\cdot8/(6500\cdot8192)\approx1.192\cdot10^{-4}<2^{-13}\approx1.221\cdot10^{-4}$.
Each conditional weight is again of the form $e^{b\cdot u}$, $|b|\le14$, when the
others sit at nodes, since nodes are unit quaternions. Positivity lets the
eight replacements be made one at a time. $(1+2^{-13})^8-1\le e^{1/1024}-1\le1/1023$
and $1-(1-2^{-13})^8\le1/1024$. Uniform in all endpoints and fields.

**Line 176, operation count. HOLDS.** Black sites (even parity) each see three
of the four white sites. Per tile and black site: $242^3$ entries at $2d$ each.
Over $6^4$ tiles this is $12d^4$ per black site, $48d^4$ for four. The final
sum adds $4d^4$. So $52d^4\approx2.31\cdot10^{14}$. Pair preparations:
$4\cdot6^4\cdot242^2\cdot d\cdot2=288d^3\approx8.8\cdot10^{11}$, which is the
stated $8\cdot6^2d^3$. Doubling it keeps the total below $2.5\cdot10^{14}$.

**Line 178, exact arithmetic. HOLDS.** Shifted Gauss weight
$1/[(1-t^2)P_6'(t)^2]$; $16P_6'=1386t^5-1260t^3+210t$, so $|P_6'|\le178.5<180$.
Then the unary is above $2^{-15}\cdot2^{-8}\cdot2^{-11}=2^{-34}$, using
$1/32400>2^{-15}$, $1/242>2^{-8}$, $e^{-7}>2^{-11}$.
Per-factor relative error is at most $2^{-44}$ (unary) and $2^{-74}$ (bond),
so a 20-factor product has relative error near $2^{-41}<2^{-37}$.
Root brackets: $16P_6$ is $-5$ at 0, about $3.09$ at $1/3$, about $5.17$ at
$1/2$, about $-4.50$ at $3/4$, about $-5.58$ at $7/8$, and 16 at 1. So the
three intervals are right. Taylor remainder: $e^8(8e/129)^{129}\approx2^{-320}<2^{-300}$.
Integer size: numerators below $2^{84}$, and $84+20\cdot92<2000$ bits.
$12d^2\approx2.53\cdot10^7<3\cdot10^7$ exponentials.
Total enclosure $1/1023+2^{-37}<1/1000$. The file states that no table was
made and nothing was checked in Lean. This is a cost bound, not a computation.

## 5b. Loss of Wilson mass under separate neutral gluing. All thirteen HOLD.

**Line 116, the spin law. HOLDS.** $C\ge0$ since every $r_j(\beta)>0$. $P$
commutes with $C$ and $M$. So $T=M(CP)M\ge0$. With $P'=PP'=P'P$ commuting with
$C$, $\operatorname{Tr}(T^{s-1}MCP'M)=\operatorname{Tr}(PC^{1/2}MT^{s-1}MC^{1/2}P\,P')$
by cyclicity. $P'=P$ gives the full mass. An edge spin projection $Q$ preserves
each vertex action and commutes with $C$, so $P'=PQ$ is a projection below $P$.

**Line 118, $P_{\rm split}$. HOLDS.** The diagonal subgroup is inside the product,
so the range is inside $P$. A rim site with one endpoint coordinate has five
neighbours in $F$ and one outside. The outside copy of the gauge acts on one end
of that bond only, so invariance forces spin zero there. So
$P_{\rm split}\le\prod Q_{0,e}$ over any set of such bonds. Marked sites
$(0,y,z)$ with $y,z\in\{1,4,\dots\}\cap[1,B-3]$ are interior in $y,z$. Each cube
lies in the hyperplane of its own $z$ and spans $[y,y+1]$ in $y$. So different
cubes have disjoint faces, and $y+1\not\equiv1\pmod3$ gives one marked face each.

**Line 120, lower bound in (9). HOLDS.** The class average of $V_i$ is
$\cos\theta_i\cdot1$, and $q(U_pV)$ is linear in $V$. Jensen gives a factor at
least $e^{\beta q(U_p)(\cos\theta_i-1)}\ge e^{-\beta a_i}$, pointwise in the rest.

**Line 127, multipliers and monotonicity. HOLDS.** A class rotation multiplies the
spin-$j/2$ coefficient by $\chi_j(\theta)/(j+1)\in[-1,1]$. For monotonicity:
$x^{-n}I_n(x)=c_n\int_{-1}^1e^{xu}(1-u^2)^{n-1/2}du$ and
$(x^{-n}I_n)'=x^{-n}I_{n+1}$. So $R_n$ is a tilted mean, with derivative equal to
a variance. Each $R_n$ increases in $x$, and so does $r_j=\prod_{n=1}^jR_n$.

**Line 129, Hölder comparison. HOLDS.** Only the half-coupling set $D$ must share
a direction. Rotated faces not parallel to the chosen time are spatial. Their
class averages are positive class functions, hence gauge invariant. Then
$|\operatorname{Tr}\prod_t H_tV_t|\le\prod_t\|H_t\|_s$ with $\|V_t\|\le1$.
$\operatorname{Tr}H_t^s$ is the mass with layer $t$ copied. Copied rotated
spatial faces are electric in a later direction and are absorbed there.
After at most four directions only the ordinary mass is left. The unnormalized
cost is $[A_0(\beta/2)/A_0(\beta)]^{|D|}$.

**Line 131, frustration and the upper bound in (9). HOLDS.** The face holonomies
of a cube, conjugated to one base, multiply to 1. The chord is bi-invariant.
So $|1-U_p|\le\sum_{5}|1-U_{p'}|$ and
$|1-V_i|\le|1-U_pV_i|+|1-U_p|$. One of six terms is at least $|1-V_i|/6$.
$|1-g|^2=2(1-q(g))$ gives $1-q\ge a_i/36$. Each face has two directions, so
some direction carries at least $\tfrac12\sum a_i$. On the event,
$e^{\beta q}\le e^{(\beta/2)(1-a_i/36)}e^{(\beta/2)q}$. The comparison then gives a
factor $[e^{\beta/2}A_0(\beta/2)/A_0(\beta)]e^{-\beta a_i/72}$ per face, and
$e^{\beta/2}A_0(\beta/2)/A_0(\beta)=z(\beta/2)/z(\beta)$.
The substitution $u=x(1-\cos\theta)$ gives the displayed $z(x)$, and
$x^{3/2}z(x)$ increases, so the ratio is at most $2^{3/2}$. With $6^r$ choices
this is (9).

**Line 138, (10) and (11). HOLDS.** Haar on $V_i$ replaces the electric kernel of
the marked bond by its constant part, which is $Q_{0,e}$. So $p_0$ is the Haar
average of $W$. $\int e^{-\beta a}\,d{\rm Haar}=z(\beta)$ gives the lower bound;
the upper one integrates (9). $z(x)\le\sqrt{2/\pi}\,x^{-3/2}$ follows from
$2-u/x\le2$ and $\int_0^\infty e^{-u}u^{1/2}=\sqrt\pi/2$.
$z(\beta)\ge c\beta^{-3/2}$ for $\beta\ge1$ uses $2-u/x\ge1$ on $[0,1]$.
The kernel $\sum_{j\le J}(j+1)\chi_j$ has multiplier ${\bf1}\{k\le J\}$ and modulus
at most $d(J)$, and $W\ge0$, which gives (11). The even projection is
$2^{-r}\sum_S$ of central rotations; each term is a positive mass ratio and the
empty term is 1, so $\Pr(\text{even})\ge2^{-r}$. Since
$\operatorname{Tr}(\rho P_{\rm split})\le p_0\le[C\beta^{-3/2}]^r$, the separate
neutral projection keeps a vanishing fraction of the mass as $\beta\to\infty$.

**Line 151, (12). HOLDS.** On $S^3$, $\Delta f(x_0)=(1-x_0^2)f''-3x_0f'$, which
gives the identity. $-\Delta$ is $j(j+2)$ on spin $j/2$. Then
$\mathbb E_\rho[j(j+2)]=\mathbb E[3\beta q_p-\beta^2(1-q_p^2)]\le3\beta$.
$d(J)\le C(J+1)^3$ with (11) gives $C(u+\beta^{-1/2})^3$. Markov gives $3/v^2$.
I did not locate the cited Laplacian source by a text search. The step is
re-derived here and does not depend on it.

**Line 227, setup. HOLDS.** $M$ and $C$ commute with $P$, so $L_e$ does. Separate
averages at every interface give $\operatorname{Tr}(C^{1/2}M^2C^{1/2}Q)^n=\operatorname{Tr}A^n$
by $Q^2=Q$, $[Q,C]=0$ and cyclicity. The claim is proved at lines 229–243.

**Line 229, (16). HOLDS.** $f\chi_k(U_\square)$ is an isometric image: integrate
$U_e$ first, with $\int|\chi_k|^2=1$. Images for different $k$, and for
orthonormal $f$, are orthonormal by the same integration. Labels change by at
most $k$ on four edges. $R_n\ge x/(2(n+1)+x)$, since $R_{n+1}\le1$, gives
$r_{j+a}/r_j\ge c_{k,\beta}(1+j)^{-k}$. On labels at most $t^{-2}$ the loss is
at most $(c(1+t^{-2})^{-k})^{4t}\to1$. The high-label part of the trace is
$o(1)$: $r_j$ decays faster than $e^{-j}$, so $\sum_{j>t^{-2}}(j+1)^2r_j^t$ is
super-polynomially small, and the other edge sums are $O(t^{-3})$.
$\operatorname{Tr}Q_{0,e}C^t\ge1$. So the reciprocal ratio has liminf at least
$k_0+1$ for every $k_0$.

**Line 236, failure of a period-independent scalar. HOLDS.**
$d_-C\le L_e\le d_+C$; $QL_eQ\le d_+CQ$; $CQ\le CQ_{0,e}$ as commuting positive
operators. Min–max gives the eigenvalue comparisons, and powers $t>0$ keep order.
So the ratio is at most $(d_+/d_-)^t$ times (16), which tends to 0. If the traces
agreed at all large multiples of $h$, the weighted counting measures would have
equal moments on a compact interval and would coincide. Then
$\operatorname{Tr}A^t=c^t\operatorname{Tr}L_e^t$ for all $t>0$, and the ratio would
tend to 1. This is a contradiction.

**Line 245, (17). HOLDS.** With open boundaries there are no double cuts, so
$K_0=C_\beta P\ge0$ is (5) at $h=0$. The joined mass is
$z_2^2A_0^{12}\langle f,K_0f\rangle$. In one temporal layer of the $2^4$ box,
$Z(u)/A_0(u)=\langle PD,C_uPD\rangle$ is a sum of nonnegative weights times
$r_{j_e}(u)$, so it does not decrease. Then
$\mathbb E_{\rm open}q_p=(\log Z)'\ge(\log A_0)'=r_1$. So
$\langle\chi_\square,f\rangle=2\mathbb E_{\rm open}q_p\ge2r_1$. The six face
characters are orthonormal eigenvectors with eigenvalue $r_1^4$; two distinct
faces of the cube graph differ in an edge, which gives orthogonality. So
$J\ge1+6r_1^4(2r_1)^2=1+24r_1^6$. At $\beta=7/3$, $r_1>4/9$ (line 79) gives
$24(4/9)^6\approx0.185>1/6$.

**Line 251, the scalar changes at every doubling. HOLDS.**
$Z_s=A_0^{12(s-1)}\langle\sqrt D,(\sqrt DCP\sqrt D)^{s-1}\sqrt D\rangle$ is the
transfer form. $CD\propto1$ would force $D$ constant, since $C$ is injective and
$C1=1$. So the spectral measure of $f_0$ has at least two positive points, and
strict Cauchy–Schwarz makes $\rho_j=m_{j+1}/m_j$ strictly increasing.
$J_s=m_{2s-1}/m_{s-1}^2$; the powers of $A_0$ cancel. Then
$J_{s+1}/J_s=\rho_{2s}\rho_{2s-1}/\rho_{s-1}^2>1$ for $s\ge1$.

## 7. Everything else. All eighteen HOLD.

**Line 13, (1). HOLDS.** $(u_e)\mapsto(v_E,r_e=v_E^{-1}u_e)$ keeps product Haar,
by left invariance given the pivot. $|\mathcal P|=6vB^4$ gives $c_B$. A plaquette
that is not internal contains a crossing link. A single cut holds two links of one
bundle. A double cut at the corner position holds one link from each of the four
bundles of one coarse square, and there are $B^2$ such. No plaquette crosses three
cuts. $c_B$ depends only on $B,\beta$.

**Line 23, (2). HOLDS.** The trace is quadratic (single cut) or four-linear
(double cut) in the quaternion columns. A symmetric form has operator norm equal
to its sup on the sphere, at most $\beta$ per plaquette. There are $3(B-1)B^2$
single cuts per interface and $B^2$ double cuts per coarse square.

**Line 30, iteration. HOLDS.** Right multiplication by a unit quaternion and
inversion are orthogonal linear maps. So an old quadratic on a crossing edge stays
quadratic in the new pivot, and an old four-linear tensor becomes a constant, a
quadratic or a four-linear tensor by its number of cuts. The counts 10 and $4^4$
are right.

**Line 36, (3). HOLDS.** A coarse link lies in six coarse squares, each linear in
it. At $B=2$, $\|Q\|\le12\beta$ and $|h|\le24\beta$, so the bound is
$36\cdot7/3=84$. Edges in no common square factor conditionally.

**Line 42, (4). HOLDS.** For a standard Gaussian $Y$ in $\mathbb R^4$,
$\mathbb Ee^{tY^tQY+sh\cdot Y}=D(t)^{-1/2}\exp(s^2P(t)/(2D(t)))$. Matching
$t^ks^{2j}$ and using $\mathbb ER^{2n}=2^n(n+1)!$ (chi with four degrees) gives
$H_M$ as the integral of the degree-$M$ Taylor polynomial. The remainder is at most
$e^{84}84^{513}/513!$; dividing by $H\ge e^{-84}$ and using $n!\ge e(n/e)^n$ gives
about $2^{-357}$, below $2^{-261}$.

**Line 55, count. HOLDS.** $2D C_0'=-D'C_0$ and $2jDC_j=PC_{j-1}$ are right. Each
new coefficient uses at most $4+4$ earlier terms. The pairs with $k+2j\le512$
number $257^2=66049$, fewer than the stated $513\cdot257$. The total is far below
the stated budget. The bound is an arithmetic-circuit count, as the file says.

**Lines 61 and 63, (5). HOLD.** A double cut at $s$ holds $u_s$ and three crossing
links of other interfaces, so $h_s$ does not depend on $A,D$. Each transverse
coordinate gives at most one double cut, so $\kappa_s\le3\beta$. $h\cdot u=\kappa
q(ua^{-1})$. Both marginals integrate to one. The change of variables
$B_b=u_sD_bu_t^{-1}$ gives $K=C_\beta U_{\nu_h}$, and centrality gives commutation.

**Line 71, (6). HOLDS.** $\int\pi(u)w(ua^{-1})du=(\int\pi w)\pi(a)$, and the
first factor is $r_\ell(\kappa)$ on spin $\ell/2$. Different vertices act on
different tensor factors, so the isotypic splittings commute. With the edge
scalars this gives the singular values (6). The outline citation
(Sussman and Alpoge, with Claude and Codex) was not re-opened here.

**Line 77, invariant norm $r_1^4$. HOLDS.** A degree-one support vertex has no
invariant vector, so a nonempty invariant support contains a cycle, of length at
least 4. $r_j\le r_1<1$, so the norm is at most $r_1^4$, attained by one square.
$r_1(7/3)<49/100$ is row 1341's bound, checked in `gap-blockstep-check-opus.md`
item 7; my own series gives $r_1(7/3)\approx1.0469/2.1627\approx0.484$.
$R_{j+1}\le(x/2)/(j+2)\le(7/6)/(j+2)$. I did not find the cited girth argument in
`gap-solve2-astra62.md` by a text search; the step is re-derived here.

**Line 79, a discarded charged mode. HOLDS.** With outside crossing links at the
identity each double cut contributes $\beta\cdot1$, so $\kappa_s=7$, $a_s=1$.
The recurrence $R_n=x/(2(n+1)+xR_{n+1})$ follows from
$I_n-I_{n+2}=(2(n+1)/x)I_{n+1}$. Then $R_1(7/3)\ge(7/3)/(4+49/54)\approx0.476>4/9$.
At $x=7$: $R_4\le7/10$, $R_3\ge70/129$, $R_2\le7/(6+490/129)\approx0.714<16/21$,
$R_1>7/(4+16/3)=3/4$. So $r_1(7/3)r_1(7)^2>(4/9)(9/16)=1/4$.

**Line 83, (7) set-up. HOLDS.** $\dim{\rm Inv}(V_a\otimes V_b\otimes V_c)$ is 1 under
the triangle and parity rules and 0 otherwise. So $\|K^{\rm inv}-\Pi\|_{\rm HS}^2$
is the sum of $\prod_br_{j_b}^2$ over nonzero admissible labellings.

**Line 89, circuit majorant. HOLDS.** $r_j^2\le4^{-j}$. Strands connect different
edges at each vertex, so circuits are cyclically nonbacktracking. Edge counts
recover the labelling, so the map is injective. $\log\det(I-tH)^{-1}=\sum_kt^k
\operatorname{tr}H^k/k$ counts primitive oriented classes. A reflection of a
cyclic word fixes an edge (reversed) or a vertex (backtrack), so no class equals
its reverse. This gives $\det(I-tH)^{-1/2}$.

**Line 91, Ihara–Bass. HOLDS.** $\det(I-tH)=(1-t^2)^{|E|-|V|}\det(I-tA+t^2(D-I))$
with $D=3I$. At $t=1/4$: factors $3/8,7/8,11/8,15/8$, with multiplicities
$1,3,3,1$. So the value is $(15/16)^4(45/64)(77/64)^3\approx0.9459>(32/33)^2\approx0.9403$.
The six faces are the only 4-cycles of the cube graph, and $6/256$ is removed
from the majorant correctly: $1/32-6/256=1/128$.

**Line 101, truncation. HOLDS.** $\prod r_{j_b}<2^{-\sum j_b}\le2^{-25}$ beyond 24.
$\binom{36}{12}=1{,}251{,}677{,}700<2\cdot10^9$. The series ratio bound is right.

**Line 103, (8). HOLDS.** $p=B\lfloor B/2\rfloor^2$ disjoint squares. Their loop
characters are orthonormal, invariant eigenvectors with eigenvalue $r_1^{4|S|}$,
whatever $h$. A bistochastic positive kernel is an $L^2$ contraction, so
$\|(I-\Pi_R)K\|^2\ge\|K\|^2-R$, which gives $R\ge(1-\eta^2)\|K\|^2$.

**Line 110, rank growth. HOLDS.** $p=65536$; $(4/9)^8\approx1.52\cdot10^{-3}>1/1024$;
$(1+1/1024)^{65536}>2^{64}$, so $R>10^{15}$. The tilted law of
$x=\beta(1-q)$ is Gamma$(3/2)$ times a decreasing factor, so $\mathbb Ex\le3/2$.
$1-y\ge e^{-2y}$ on $[0,1/2]$ gives $r_1\ge e^{-3/\beta}$ for $\beta\ge3$.
Then $r_1^{4k}\ge e^{-1/2}$ for $k\le\beta/24$. With $B=L^K$ and
$cK\le\beta\le CK$ (item 4), $\binom pk\ge e^{c'K^2}$.

**Line 225, degree $60B^3$. HOLDS.** $20\cdot3(B-1)B^2+10\cdot6B^2=60B^3$.
With $A=D={\bf j}$ and $v=e^{{\bf i}\theta}$, ${\bf j}v{\bf j}^{-1}=\bar v$, so the
single-cut trace is $q(\bar v^2)=\cos2\theta$. The double cuts give $\cos\theta$.
The top Fourier coefficient is a product of nonzero top coefficients,
since $2I_{10}^{[16]}>0$.

**GUIDE and OPEN text.** No statement there is marked PROVED. Line 32, 57, 149,
180, 221 and 278 (OPEN) state scope correctly; each agrees with the verdicts
above. Lines 3, 5, 7 (GUIDE) name prior files and the outline; I did not re-open
the PRs or the outline. Line 290 (RESULT: OPEN) agrees with this check.

## Restatement of earlier rows

No main step only restates an earlier row. The block map (1)–(2) for continuous
coarse links, (3)–(4), (5)–(8), (9)–(11), (13)–(15), (16)–(17), the doubling
calibration, (18)–(19) and (20) are new here.
Parts reuse earlier work, and the file credits each:
- The deletion and short-cluster proof at line 217 is that of rows 1341 and 1345, with new activities (14).
- The Hölder transfer comparison at line 129 extends row 1345's (7) from central signs to class rotations and half couplings.
- $r_1(7/3)<49/100$ is row 1341's bound. GL3, GL4 and the one-link coefficients are Sussman and Alpoge's outline (with Claude and Codex).
- The Laplacian identity at line 151 and Lemmas OS and DS are cited as prior work; the girth step at line 77 is cited to row 1145. I re-derived both here.
- Classical tools are named in the file: Peter–Weyl, Clebsch–Gordan, Gauss–Legendre, Chebyshev's extremal bound, the Ihara–Bass determinant, Machin's formula.

## Summary

| Item | Lines | Verdict |
|---|---|---|
| 1 minorant (13) | 186 | HOLDS; all tail constants correct |
| 2 core (14)–(15), polymer bound, degree bound | 197, 199, 208, 217, 219 | HOLDS (5 of 5) |
| 3 trajectory (18), bound (19) | 257, 268 | HOLDS (2 of 2) |
| 4 cost necessary up to constants | 276 | HOLDS in its stated scheme class |
| 5a eight-link enclosure | 163, 170, 176, 178 | HOLDS (4 of 4) |
| 5b neutral-gluing loss (9)–(12), (16)–(17), calibration | 116, 118, 120, 127, 129, 131, 138, 151, 227, 229, 236, 245, 251 | HOLDS (13 of 13) |
| 6 polynomial form (20) | 280 | HOLDS on the flow bound (26) |
| 7 other statements | 13, 23, 30, 36, 42, 55, 61, 63, 71, 77, 79, 83, 89, 91, 101, 103, 110, 225 | HOLDS (18 of 18) |

Precisions that change no verdict: line 55 overcounts the needed coefficients
($257^2$ suffice). Line 219 states $|P|\le1$ on $[-1,0]$ without the optional
scalar; with a scalar the same ratio argument runs. Two cited prior arguments
(lines 77 and 151) were not found by a text search and are re-derived here.

The file's OPEN conclusion stands. The angular discretization error is now
controlled uniformly on late data by (18)–(19). The remaining step is a block
bound for the interacting finite-state core, with its charged channels, into
CH's end class. Separate neutral gluing is excluded as a route by (10), (16)
and (17).

Checked by hand by Claude Opus 5.5. No numeric run was used as a proof step.

RESULT: Of 45 PROVED statements in row 1348, 45 HOLD, 0 need correction, 0 FAIL; main finding: the minorant (13) and its tail constants, the exact finite-state core (15), the late-datum trajectory (18) with the two-volume bound (19), and the polynomial test (20) all hold, so the angular discretization error leaves CH; the eight-link enclosure holds at relative error 1/1000, separate neutral gluing loses Wilson mass by (10), (16) and (17), and the block step for the interacting core stays OPEN.
