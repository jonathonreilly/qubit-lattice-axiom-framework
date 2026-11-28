# Repo search

Research row 1616 at `4c8d60c63`. The target-specific prior file is absent. I searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134` and `pr/10141` for `PUR-io`, projected rings, six-piece comparisons, free-cap ratios, open-slab covariances and joining variation. The first 30 matches included unrelated ring terminology in the BKSF cycle-728 note, the compact-U(1) finite Hamiltonian note and the PR 8044 tube comparison, and substring matches in `gap-sc-box-check.md`, `BFT_A.md` and `YSUP.md`. None of those displayed matches states this consumer.

**ON FILE (1611, 1612, 1614).** Row 1611 gives the unprojected six-piece comparison. Check 1612 §11(4) suggests inserting the eight-twist average and predicts the projected endpoint. Row 1614 (9) already defines precisely this projected ring and proves that, for every fixed $\tau<2/3$, the integral of $|(D-D_0)'|$ on $[0,\tau]$ is exponentially small in $n$, uniformly in bulk coupling and slab depth. Its (7) controls the contribution of each fixed spin-degree truncation with the full denominators, and (10) controls the full unprojected variation on a shrinking interval. Rows 1614–1615 own the unprojected fixed-interval attack. The registry's seed entries are W-CUBE-23, R10–R12 and TWO-PER. FINISH assigns the projected consumer and its comparisons to 1616. [Original construction](gap-direction7-astra62.md) · [Check and suggestion](gap-direction7-astra62-check-fable.md) · [Fixed-interval estimates](gap-wmix-fixint-astra62.md)

A narrower pass on the same five refs over the YM research paths and TeX files found no matches for prescribed product reference, joining variation, six-piece, cap subtraction, two-slab joining or tilted collar. Row 531's November 8 digest §11 points to the soft route's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, 106–149 (PRs 10114 and 10133). **ON FILE (531, soft route (5)–(8)).** On a simple loop of length $b'$, normalized convolution has eigenvalue $(I_2/I_1)^{b'}$ on the SU(2) trace and the trace has squared Haar norm $1/4$. This gives a positive one-step correlation and leaves the length-$n/1024$ correlation open. [Repo-search digest §11](prior/repo-search-2026-11-08.md)

**ON FILE (outline index 244).** I searched the outline index for the projected ring, free cap, electric flux, neutral purity and transfer identities. The matching transfer entries and their neighbours are chunk 02 lines 87–93 and 99–103. Sussman and Alpoge, with Claude and Codex, prove GL3 and give its tensor product at outline 2195–2257, and derive the untwisted transfer trace GL8 at 2313–2335. The gap is explicitly separate at outline 588–599, 32486–32490 and CA-I 2698–2714 (index chunk 29 lines 152–153, obligations 24, 1536). The indexed searches gave no projected joining estimate. [Outline index](sa-index/README.md)

## The projected comparison

Fix one release pair $b,g_0$ as in check 1453, with odd block factor $b$, and one $\ell\in1024\mathbb N_{>0}$ throughout a subsequence. Set $n=\ell b^K$, $v=n/1024$, $u=2v$, $T=T_{\beta_K}$, $S=T^v$, $G(j)=\langle1,T^j1\rangle$, and normalize spatial Haar to mass one. Work on the vertex-gauge-invariant Hilbert space. Here $P=P_0=2^{-3}\sum_z C_z$ averages the flat centre translations. Use the normalized join $J=J_t$ of row 1611 (4), with $w(U)=\tfrac12\operatorname{tr}U$ and $z(t)=\int e^{tw(U)}dU$. Each join integrates the product of $e^{tw(X_e^{-1}g_iY_e g_j^{-1})}/z(t)$ over bonds $e=(i,j)$ against independent Haar vertex gauges. A has a two-slab ring and two open two-slab chains. B has two open three-slab chains. Each uses four joins. Write $S_+=PSP$.

**PROVED (positive realization and derivative).** The projected log ratio is
$$
 D_0(t)=\log\frac{R_0(t)\langle1,SJS1\rangle^2}
                       {\langle1,SJSJS1\rangle^2},
 \qquad R_0(t)=\operatorname{Tr}(PSJSJ).
 \tag{5+}
$$
Both $S$ and $J$ commute with $C_z$. The Wilson action and the Haar measures are invariant under a simultaneous flat flip at both ends, and the two signs on a dressed join link cancel. Also $P1=1$. Consequently **every** $S$ in both arrangements can be replaced by $S_+$. The closed ring trace restricts to $P\mathcal H$, and each open chain stays in $P\mathcal H$ from its free end onwards. The kernel of $S_+$ is the positive average $2^{-3}\sum_z S(x,C_zy)$. Equivalently $R_0$ is the arithmetic mean of eight positive twisted ring integrals. In the normalized ensemble the probabilities of the twists are proportional to those integrals. Placing the flip on a slab end keeps all four differentiated join densities ordinary. With a flip on a join one must include its sign in that join's measured $w$. Differentiating the log integral proves
$$
 D'_0(t)=\sum_{j,e}\big(\mathbb E_{A,+,t}w_{j,e}-\mathbb E_{B,t}w_{j,e}\big).
$$
Each log derivative subtracts the same four sums of the one-link normalizing derivative. At $t=0$, $J_0=|1\rangle\langle1|$ and both integrals equal $G(v)^6$.

**PROVED (endpoint and thresholds).** The proposed sufficient estimate is
$$
 V_0(K):=\int_0^\infty |D'_0(t)|\,dt\ \le\ 2\log(16/15)
 \quad\text{at infinitely many }K.                                      \tag{6+}
$$
Let $\phi=S1/\sqrt{G(2v)}$ and let $\lambda_0$ be the top neutral eigenvalue. Then
$$
 e^{-D_0(\infty)/2}
 =\frac{G(3v)}{G(2v)\sqrt{Z_+(u)}}
 =\frac{\langle\phi,S\phi\rangle}{\sqrt{Z_+(u)}}
 =\kappa_K\sqrt{w_0(u)},\quad
 \kappa_K=\frac{G(3v)}{\lambda_0^vG(2v)},\quad
 w_0(u)=\frac{\lambda_0^u}{Z_+(u)}.                                   \tag{7+}
$$
Indeed $J_t\to I$ strongly on gauge invariants by the one-link approximate identity of 1611, checked in 1612 §2. Multiplication by $J_t-I$ on the Hilbert–Schmidt slab tends to zero in Hilbert–Schmidt norm by finite-rank approximation and uniform contraction. Thus the ring tends to $\operatorname{Tr}S_+^2=Z_+(u)$, and the two open scalar factors tend to $G(2v)$ and $G(3v)$. Both $\phi$ and the free cap are neutral, and $\|\phi\|=1$, so $0<\kappa_K\le1$. Writing $p_i=\lambda_i^u/Z_+(u)$ on the neutral space gives $w_0=p_0$ and $P_K=\sum_i p_i^2\ge w_0^2$. Since $D_0(0)=0$, (6+) yields
$$
 \kappa_K^2w_0(u)\ge225/256,\qquad
 P_K\ge(15/16)^4>457/625 .
$$
The final strict inequality is the hand comparison in check 1612 §2. The side, coupling and subsequence are identical. The resulting seed-to-gap implication is **ON FILE (1468 §3.1, 1527(ii))**. In particular $\kappa_K\ge15/16$ and $w_0\ge225/256$ are necessary separately. The product is the sharp condition for the stated endpoint budget.

**PROVED (exact variation budget).** Put $N_0(K)=\int_0^\infty(-D'_0)_+\,dt$. By $|a|=a+2(-a)_+$ and (7+),
$$
 V_0(K)=-\log(\kappa_K^2w_0(u))+2N_0(K).
$$
Thus (6+) requires precisely $\kappa_K^2w_0(u)e^{-2N_0(K)}\ge225/256$. The endpoint alone suffices for the purity implication. A proof by absolute integration must pay for every decrease of $D_0$. Both quantities depend only on neutral matrix elements at every joining strength. Finite-cutoff integrability also follows from (10+) below.

## The correlation identity and the joining limits

**PROVED (11+).** Put $B=S/G(v)$, $\rho=B1$, $C=B-|\rho\rangle\langle\rho|$, and $C_+=PCP$. Positivity of $B$ and $\langle1,B1\rangle=1$ give $C\ge0$ by Cauchy–Schwarz. Both $C$ and $J$ commute with $P$, and $P\rho=\rho$. Set
$$
 A_+=J^{1/2}C_+J^{1/2},\quad x=J^{1/2}\rho,\quad s=\|x\|^2,\quad
 e=x/\sqrt{s},\quad z=\langle e,A_+e\rangle .
$$
GL3 gives $J\ge0$, and $J1=1$ gives $s\ge|\langle1,x\rangle|^2=1$. In particular $x,e$ are neutral and $z$ equals the unprojected $z$ of 1611. With $M_+=J^{1/2}PBPJ^{1/2}=A_++|x\rangle\langle x|$, the ring divided by $G(v)^2$ equals $\operatorname{Tr}M_+^2$, and the two open factors divided by $G(v)^2,G(v)^3$ equal $s,\langle x,M_+x\rangle=s(s+z)$. Expanding the square gives
$$
 e^{D_0(t)}-1=\frac{\|A_+\|_{\rm HS}^2-z^2}{(s+z)^2}\ge0 .
 \tag{11+}
$$
Indeed $z$ is the Hilbert–Schmidt inner product of $A_+$ with the unit-norm projection $|e\rangle\langle e|$. In the spin-network basis the squared norm sums $r_i(t)r_j(t)|C_{ij}|^2$ over **neutral** $i,j$ only, with $r_i=\prod_e [I_{2j_e(i)+1}(t)/I_1(t)]$ and the continuous values at zero. The matrix entries are the connected correlations of the ordinary free-ended slab against these neutral networks. For fixed $t$, $D_0(t)\le D(t)$ because the deletion from the ring is a sum of squared norms. This pointwise inequality gives no ordering of absolute variations.

**PROVED (9+ and the first coefficient affected by projection).** Let $m_p$ be the free-slab mean of the normalized plaquette trace at either end, and
$C^w_{pq}=\mathbb E_S[w_p(X)w_q(Y)]-m_pm_q$ under density $S(X,Y)/G(v)$. Then, at fixed $K$,
$$
 D_0(t)=\frac{t^8}{64^2}\sum_{p,q}(C^w_{pq})^2+O_K(t^{10}).             \tag{9+}
$$
More precisely, let $\mathcal L_i$ contain the $n^2$ straight unoriented loops around spatial direction $i$, with $\chi_h$ their fundamental characters (Haar norm one). If $D$ denotes the original log ratio, then
$$
 D(t)-D_0(t)
 =\frac{(t/4)^{2n}}{G(v)^2}
   \sum_{i=1}^{3}\sum_{h,h'\in\mathcal L_i}
        |\langle\chi_h,S\chi_{h'}\rangle|^2+O_K(t^{2n+2}).              \tag{W}
$$
The coefficient in (W) is positive for $\beta_K>0$. This locates the effect of the projection at each finite box, without a Taylor bound uniform in $K$.

To prove (W), expand the full ring in spin networks as $\sum_{\alpha,\eta} r_\alpha r_\eta |S_{\alpha\eta}|^2$. In the difference of ring traces only matching nontrivial centre characters remain. The even-degree rule at each vertex makes the half-integer edges a mod-two cycle. Its intersection parity with coordinate cuts is its centre character (**ON FILE, 860 Prop. P1, checked in 864**). For a nontrivial character choose a direction with odd parity. The cycle crosses each of its $n$ parallel cuts, so $d(\alpha)=\sum_e 2j_e(\alpha)\ge n$. Equality spends exactly one fundamental edge on each cut and leaves no transverse edges. The even-degree rule joins these edges into one straight winding loop. The valence-two invariant contraction is unique. Thus the only networks of charged degree $n$ are the $\chi_h$, and different directions have distinct characters. Their multiplier starts at $(t/4)^n$, by GL3. At finite volume the Taylor coefficient of any degree $m$ in $J$ is finite rank, and is supported on $d\le m$. A degree-$m$ bond polynomial uses at most $m$ fundamental representation factors before contraction, and scalar normalization cannot lower that minimum degree. The compact integral kernel is analytic near zero in operator norm. Coefficients in the two-join trace can therefore be taken before the trace against the Hilbert–Schmidt slab factors. Both rings are even functions of $t$ by the sublattice centre flip on the even torus. Taking the logarithm of the ratio of the rings divides the first difference by $R_0(0)=G(v)^2$ and proves (W). Each diagonal term is positive because the positive magnetic half-weight and the injective positive electric convolution (GL3) make $S$ strictly positive as a quadratic form on gauge-invariant functions. Now $2n>10$ and the checked unprojected (9) of 1611–1612 gives (9+). Equivalently all four-edge square characters that enter its proof are neutral. Its diagonal entries $C^w_{pp}=\langle w_p-m_p,S(w_p-m_p)\rangle/G(v)>0$ survive.

**PROVED (10+).** For an absolute $c$ and $L=3\beta_K$,
$$
 \int_{T_*}^{\infty}|D'_0(t)|\,dt
       \le c\,n^3(1+L)^2/T_* ,
 \qquad T_*\ge(1+L)^2 .                                                   \tag{10+}
$$
Use the positive $S_+$ realization of (5+). Absorb the vertex gauges in the slab endpoints and use $Y_e=X_eR_e$ at each join. Conditional on all other variables, one noise $R_e$ has density proportional to $e^{tw(R_e)}H(R_e)\,dR_e$. The noise enters only one end link of one slab. In each summand of $S_+$ a centre multiplication is an isometry, and the link enters four half-weight spatial plaquettes and one full temporal plaquette. The first and second derivatives of each trace along a unit-speed one-parameter subgroup have modulus at most one, also after a sign flip. Differentiating inside the positive sum and integral gives $|H'|\le LH$, $|H''|\le (L+L^2)H$. The conditional one-link estimate of **1611 (10), checked in 1612 §5**, then applies. Pairing opposite angular directions cancels the linear term, so the biased trace mean differs from its unperturbed mean by at most $c(1+L)^2t^{-2}$ for $t\ge(1+L)^2$. This is uniform in the pins and the twist. The unperturbed means cancel between arrangements. Sum over $8\cdot3n^3$ readings and integrate $t^{-2}$ to obtain (10+). Thus $T_*=(1+3\beta_K)^2n^4$ leaves an $O(n^{-1})$ tail. Near zero $|D'_0|\le8\cdot3n^3$ costs $O(n^{-1})$ up to $n^{-4}$.

## What the seed controls

**PROVED (which whole-slice affinity).** Let $k(x,y)=S_+(x,y)$, $p(x,y)=k(x,y)^2/Z_+(u)$, and give both configurations Haar reference. Its single-face marginal is $\mu(x)=\int k(x,y)^2dy/Z_+(u)$. The prescribed reference in this construction is $q(x)=\phi(x)^2=(\int k(x,y)\,dy)^2/G(2v)$. Integrating the nonnegative square root gives
$$
 \operatorname{Aff}(p,q\otimes q)
   =\langle\phi,S_+\phi\rangle/\sqrt{Z_+(u)}
   =e^{-D_0(\infty)/2}.
$$
Thus the endpoint is a bounded whole-slice affinity at exactly the target aspect. Its reference depends on how the free cap couples to the eigenfunctions. For comparison, maximizing over unit nonnegative slice vectors in place of $\phi$ gives $\lambda_0^v/\sqrt{Z_+(u)}=\sqrt{w_0}$ by the Rayleigh bound and the positive top eigenfunction. **ON FILE (1147 (26), 1600 §§2,8, 1602/1605).** The best product and the intrinsic product $\mu\otimes\mu$ are controlled by the thermal spectrum. The equivalence theorem of check 1605, Steps 2 and 6, treats the joint law against its *own* product marginal, or the stated pair of conditional laws, over admissible sides. It can enlarge $\ell$ by a fixed factor with the roots and subsequence preserved. It does not identify $q$ with $\mu$ or estimate this particular cap. The endpoint lies on the prescribed-reference side of the whole-slice comparison, as anticipated in 1612 §8.

**PROVED (strictness on positive transfer data, using the witness already on file).** In the example of row 1611, checked in 1612 §3, the range of the transfer lies in the neutral sector. Inserting $P$ therefore leaves both the endpoint and the whole path of that example unchanged. Its eigenvalues are $1,1/2$ and the squared vacuum overlap of the constant is $c=4\delta(1-\delta)$ with $\delta=2^{-8n}$. Thus $P_K=(1+2^{-2u})/(1+2^{-u})^2\to1$ while $G(j)=c+(1-c)2^{-j}$ gives $\kappa_K\sim2^{-v}\to0$. This holds for every allowed fixed side. Both (6+) and the weaker endpoint test are strictly stronger than the seed in this class. Check 1612’s second example, which added only charged levels to a single neutral level, loses its obstruction under $P$. [Check 1612 §8](gap-direction7-astra62-check-fable.md)

**ARGUED (calibrated Wilson trajectory).** The forward implication is proved on the identical boxes by (7+). A converse for the endpoint would have to control the spectral measure of the free cap at depth $v$, even after using side enlargement to improve $w_0$. A converse for (6+) would also have to bound the downward variation allowed in its exact budget. The example above changes the Wilson bulk kernel. Neither a Wilson converse nor strictness within this one calibrated theory follows. In particular, factoring every expression through $S_+$ removes the separate condition on $f_u=1-Z_+(u)/\operatorname{Tr}T^u$. [Check 1605, Step 6](gap-wmix-solve-neon-check-opus.md)

## The two coupling regimes

**PROVED, conditional on the periodic Villain input to rows 1565/1571 and 1573/1579.** In four-dimensional compact U(1) use the same three half-turns as in the seed. Their range consists of the sectors $Q\in(2\mathbb Z)^3$. Uniqueness and positivity of the top eigenfunction of the finite physical transfer imply that all flat translations fix it, so its full integer charge is zero. Row 1573, lines 131–150, gives
$$
 Z_{\rm even}(u)\ge (1+2d_\gamma^4)\,Z_{Q=0}(u),\qquad d_\gamma^4>1/2 ,
$$
at $n/u=512$ on the stated even tori. Its input is the uniform shifted-coset estimate for the charges $0,\pm2$ in one direction at sufficiently large fixed Villain parameter $\gamma$, followed by the positive offset-mixture comparison for all sufficiently large Wilson couplings. Check 1571 A2–A3 leaves the internal proofs of the periodic Villain input unchecked. Equation (7+) now gives
$$
 e^{-D_0(\infty)}\le \lambda_0^u/Z_{\rm even}(u)
       \le (1+2d_\gamma^4)^{-1}<1/2<225/256 .
$$
This is an endpoint failure for the projected ring itself. Algebra explains the survival of $\pm2$ under the half-turns. Their **thermal weights** relative to the zero-charge sector are the law-dependent step. Projection under the entire flat U(1) would change the question and remove these two sectors.

**PROVED, given the pinned small-coupling estimate of row 1573 (4), checked in 1579.** For fixed $0<\beta<2/9$ in 4D SU(2), $V_0(K)\to0$ as $n\to\infty$ at $v=n/1024$. Here $\beta$ is fixed in place of $\beta_K$. Let $N=3n^3$, $q_D=9\beta/2<1$ and
$$
 \delta_n=\pi^2\,18N\beta^2\sum_{r\ge v-2}(r+1)q_D^r .
$$
Row 1611's integration of the pinned bound gives, for a positive $f$, $e^{-\delta_n}f(x)f(y)\le S(x,y)\le e^{\delta_n}f(x)f(y)$. The reference pin defining $f$ need not be centre invariant. Averaging **both ends independently** using $PSP=S_+$ gives the same inequality with $f_+=Pf$ at both ends. With $f_+\otimes f_+$ in all six slabs, each joined pair has the same distribution, proportional to $f_+(x)J_t(x,y)f_+(y)$ including its latent variables, in A and B. Restoring the six slabs multiplies each normalized density by a factor in $[e^{-12\delta_n},e^{12\delta_n}]$. It follows that $|D'_0(t)|\le8N(e^{12\delta_n}-1)$ uniformly in $t$. Up to $T_*=(1+3\beta)^2n^4$ its integral vanishes in the limit since $\delta_n$ decays exponentially times a polynomial. Above $T_*$ use (10+). The $\beta=0$ transfer is already rank one.

**PROVED (the law test and the 5D conditional).** Row 1573 (4) with $q_D=9\beta$ gives the same two-ended rank-one comparison for 4D compact U(1) at fixed $\beta<1/9$. With $\delta_n$ now given by the U(1) pinned bound, at every $t$ the two positive partition functions lie between $e^{-6\delta_n}$ and $e^{6\delta_n}$ times the same rank-one integral. Taking $t\to\infty$ gives $D_0(\infty)\le12\delta_n\to0$. The weak-coupling obstruction changes with the law at the **same group and dimension**, as required by Lemma ALG (1553 §1.4). For 5D SU(2), if a second neutral level on the relevant boxes has $uE<\log 2$ with $E=-\log(\lambda/\lambda_0)$, then (7+) gives $e^{-D_0(\infty)}\le(1+e^{-uE})^{-1}<2/3$. **ON FILE (1573, 1612 §7.4).** The free transverse pair has $E\le4\pi/n$. **GUESSED.** Comparable interacting weak-5D levels occur on all sufficiently late boxes at each proposed side. There is no interacting 5D estimate here. The endpoint and its projection identity are valid in either dimension. An affirmative selective estimate for calibrated 4D SU(2) remains open. [Lemma ALG](gap-mech-direction4-fable.md) · [Charge and small-coupling estimates](gap-band-neutral-astra62.md)

## The first open estimate

**GUESSED (fixed interval, row 1611).** On one allowed side and infinitely many release roots, require
$$
             \int_0^{1/4}|D'_0(t)|\,dt\le\tfrac12\log(16/15).              \tag{I}
$$
The rest of the budget in (6+) includes the interval from $1/4$ to $T_*$. **ON FILE (1614 (7), (9), (10)).** The integrated absolute derivative of $D-D_0$ is $O_\tau(e^{-c_\tau n})$ on any $[0,\tau]$, $\tau<2/3$. Thus the two fixed-interval costs differ by at most that much. Every fixed total-spin contribution to the differentiated full ratio costs $O_H(\beta_K^{-2})$. Row 1614 bounds all spins together up to $Vt^4\le c\beta_K^{3/2}$, $V=n^3$. The open part of (I) includes the sum over neutral networks of increasing spin degree. Even an endpoint tending to one can leave this variation large.

**PROVED (a passing endpoint can hide an interior excess, with the actual joins).** On the same SU(2) slice spaces with the same $P$ and $J_t$, there exist positive, finite-rank, pointwise strictly positive transfers for which $e^{-D_0(\infty)}\to1$ and $P_K\to1$, but
$$
          \sup_{0\le t\le C n^{-3/4}}D_0(t)\ \ge\ \log(4/3)
                  \ >\ 2\log(16/15) .                                    \tag{O}
$$
All their nonzero modes are neutral. In particular the endpoint budget can hold while (I) fails, even as the seed purity tends to one.

Choose $m=n^3/4$ vertex-disjoint unit squares in the $12$ direction, with even first and second base coordinates. On each take the event $E_i=\{w_{p_i}>0\}$ of spatial Haar probability $a=1/2$. Write $E=\bigcap E_i$, $\delta=a^m$, $h=(\mathbf1_E-\delta)/\sqrt{\delta(1-\delta)}$. The function $h$ has mean zero and norm one. Its two values are $L=\sqrt{(1-\delta)/\delta}$ and $-1/L$. Put $p=L/4$, $\rho=1+ph$, and define the slab operator
$$
       S=|\rho\rangle\langle\rho|+2p^2|h\rangle\langle h|.
$$
It is positive and $\langle1,S1\rangle=1$. On pairs in the same indicator cell its kernel is positive. Across the two cells its value is $1+p(L-1/L)-3p^2=p^2+3/4>0$. Both cells are gauge and centre invariant. To get a one-step transfer, take $T=S^{1/v}$, zero off this two-dimensional space. If $\sigma_1>\sigma_2>0$ are its slab eigenvalues, the function $s^{1/v}$ on these two points equals $d s+b$ with $d>0,b\ge0$ by increase, concavity and its value zero at the origin. The identity on the two cells has a nonnegative kernel, the sum of the two normalized indicator projections. Hence $T$ also has a strictly positive kernel and $T^v=S$. The slab eigenvalues are distinct since the off-diagonal entry in the indicator basis is positive.

Write $r(t)=\langle h,J_t h\rangle$ and $y=p^2r/(1+p^2r)$. Here $r(0)=0$, $r(\infty)=1$. In (11+) the covariance is $2p^2|h\rangle\langle h|$. Using $\langle1,J_th\rangle=0$ gives $s=1+p^2r$, $z/s=2y^2$ and $\|A_+\|_{\rm HS}^2/s^2=4y^2$. Hence
$$
                     e^{D_0(t)}=\frac{1+8y^2}{(1+2y^2)^2}.
$$
At the endpoint $p\to\infty$, so $y\to1$ and $D_0(\infty)\to0$. Equation (7+) implies $w_0\to1$ and $P_K\to1$. At $p^2r=1$, $y=1/2$ and $e^{D_0}=4/3$.

It remains to place this value inside the claimed interval. For one square set $h_t^{(1)}=\langle\mathbf1_{E_i},J_t\mathbf1_{E_i}\rangle$. Acting on vertex invariants, $J_t$ is just the product of the one-bond convolutions. Haar and this convolution factor over disjoint edge sets, hence $\langle\mathbf1_E,J_t\mathbf1_E\rangle=(h_t^{(1)})^m$ and
$$
 p^2r(t)=\frac{(h_t^{(1)}/a^2)^m-1}{16}.
$$
The normalized network $2w_{p_i}$ is orthogonal to the constant and has strictly positive coefficient in $\mathbf1_{E_i}$ by integration on $E_i$. All join eigenvalues are nonnegative. Keeping these two terms therefore gives $h_t^{(1)}/a^2\ge1+c t^4$ for some $c>0$ at small $t$, by the one-square eigenvalue $(I_2/I_1)^4$ (row 531). Take $t=(16/(cm))^{1/4}$. Bernoulli's inequality gives $p^2r(t)\ge1$, and continuity supplies the crossing. This proves (O) and precludes a monotonicity proof from transfer positivity even on any fixed interval starting at zero. The bulk kernel in (O) is a specified change of the action. Its free face density $\rho$ is at least $3/4$ everywhere. Since the Haar mean of $1-w_p$ is one, $\mathbb E_S(1-w_p)\ge3/4$ here. This violates the actual Wilson estimate $\mathbb E(1-w_p)=O(\beta_K^{-1})$ from 1614 (2).

**PROVED (a larger interval for the actual projected Wilson comparison, given row 1614's collar estimates).** Put $\beta=\beta_K$, $V=n^3$, $\Lambda=\tau^4/64$ and $x=V\Lambda$. Uniformly for $0\le x\le\beta^{5/3}$ at late release roots,
$$
 \int_0^\tau |D'_0(t)|\,dt
 \le C\left(\frac{x}{\beta^2}+\frac{x^{3/2}}{\beta^{5/2}}
               +\frac{x^{3/2}}{\sqrt V}(1+x/\beta)\right).                \tag{I'}
$$
Consequently (I)'s numerical budget holds up to $\tau_K=(64c_*\beta_K^{5/3}/n^3)^{1/4}$ for some fixed $c_*>0$. For $x=o(\beta^{5/3})$ the cost tends to zero. The gain over the previously bounded shrinking scale in $t$ is a factor proportional to $\beta_K^{1/24}$.

Use $S_+$ on all slabs. Then at $t=0$ their six endpoint pairs are independent with common probability kernel $S_+(X,Y)/G(v)$. Averaging over $C_z$ on each end preserves every plaquette trace. The joint law of these traces is thus the ordinary free-slab one. For a marked join with ends $X,Y$, let $d_p=1-w_p$ and sum over all four joins and all end plaquettes to define
$$
 U=\sum_{j,p}(d_p(X_j)+d_p(Y_j)),\qquad W=\sum_{j,p}d_p(X_j)d_p(Y_j).
$$
We have $0\le W\le U$, since $d+d'-dd'=1-ww'\ge0$. **ON FILE (1614 (2), (11), and its collar probability).** In either base arrangement $\mathbb E_0 U\le CV/\beta$, and except on an event of probability $\le C e^{-cV/\beta^2}$ the sum of squares of all these $d_p$ is at most $CV/\beta^2$. Row 1614 obtains this probability from a simultaneous marked boundary-plaquette moment on free slabs. These are author proofs at this pin. At small $t$ the log of a pinned join is $(t^4/64)\sum_p w_p(X)w_p(Y)+E_t$, with $|E_t|+t|\partial_t E_t|\le CVt^6$ uniformly in the pins. Both inputs concern the Wilson law or join and remain applicable after the preceding positive projection.

Write $\lambda=t^4/64$. For one arrangement interpolate with $H_a=U-aW$ and $F_a(\lambda)=\log\mathbb E_0 e^{-\lambda H_a}$, $0\le a\le1$. The common constant from the leading quartic term cancels. $F_0(\lambda)$ is identical in the two arrangements because each has two independent slabs with both ends marked and four with one end marked, and the free slab is symmetric. This cancellation is already used in 1614. The estimate here interpolates the mixed term itself.

For $0\le\lambda\le\Lambda$ let $\langle\cdot\rangle_{\lambda,a}$ denote the $H_a$ tilt. Since $0\le H_a\le U$, its normalizer is at least $\exp(-Cx/\beta)$ by Jensen. On the good event $W\le CV/\beta^2$ by $2dd'\le d^2+(d')^2$. Everywhere $W\le CV$. The tilted bad probability is bounded by $C\exp(-cV/\beta^2+Cx/\beta)$. Since $\beta\to\infty$, $\beta=O(\log n)$ (check 1453), and $x\le\beta^{5/3}$, this implies
$$
 \sup_{\lambda,a}\langle W^2\rangle_{\lambda,a}^{1/2}\le CV/\beta^2.
$$
Also $\partial_\lambda\langle H_a\rangle_{\lambda,a}=-\operatorname{Var}_{\lambda,a}(H_a)$, so
$$
  \int_0^\Lambda\operatorname{Var}_{\lambda,a}(H_a)\,d\lambda
       \le\mathbb E_0H_a\le CV/\beta .
$$
All the variables are bounded at a fixed box, which justifies differentiation. The mixed derivative is
$$
 \partial_\lambda\partial_a F_a
    =\langle W\rangle_{\lambda,a}
       -\lambda\operatorname{Cov}_{\lambda,a}(W,H_a).
$$
Use Cauchy–Schwarz for the covariance, then in $d\lambda$ with
$\int_0^\Lambda\lambda^2d\lambda=\Lambda^3/3$. Integrating over $a$ gives
$$
 \int_0^\Lambda|\partial_\lambda(F_1-F_0)|\,d\lambda
 \le C\Lambda V/\beta^2
      +C(V/\beta^2)\Lambda^{3/2}\sqrt{V/\beta}
 = C\left(x/\beta^2+x^{3/2}/\beta^{5/2}\right).
$$
Sum this bound over A and B after cancelling $F_0$.

Let $\mathcal E_t$ be the sum of the four join remainders. For $t\le\tau$, $V\tau^6=64^{3/2}x^{3/2}/\sqrt V=o(1)$ on the stated range. Restoring $\mathcal E_t$ changes the normalized density under the $H_1$ tilt by a factor between $e^{-CVt^6}$ and $e^{CVt^6}$. The absolute log-derivative error is bounded by $CVt^5+\lambda'(t)(e^{CVt^6}-1)\langle H_1\rangle_{\lambda,1}$. The latter mean is at most $\mathbb E_0U\le CV/\beta$ by the variance identity. Integration costs at most $CV\tau^6(1+x/\beta)$ per arrangement. Increasing $\lambda$ preserves absolute variation, which proves (I'). At $x=c_*\beta^{5/3}$ the first and third terms tend to zero, and the middle term is $Cc_*^{3/2}$. Choose $0<c_*\le1$ so this is below $\tfrac14\log(16/15)$.

**ARGUED (where the attack stops).** At $\tau=1/4$, $x$ is a fixed positive multiple of $n^3$. The variance estimate above uses only the integrated slope $CV/\beta$ and the absolute size $CV/\beta^2$ of $W$. After Cauchy–Schwarz these give the term $Cx^{3/2}/\beta^{5/2}$, which grows without bound at any fixed positive $\tau$. The pinned remainder estimate also loses smallness there. Uniform control of the signed response of the remaining neutral networks across the physical slab on $[\tau_K,1/4]$ is open. A bound through $1/4$ alone still leaves the interval up to the tail in (10+). The estimate obtained here reads small Wilson plaquette deficits. It supplies no step selecting interacting 4D SU(2) over interacting weak 5D SU(2).

RESULT — (d), a projected consumer and a partial estimate. PROVED in (5+)–(7+), (9+)–(11+) and (W) that projection removes the charged trace throughout, leaves the plaquette coefficient intact, and gives the same-side seed from the stated budget.
PROVED strictness on positive transfer data and the interior excess (O) even with a passing prescribed-cap endpoint. Equivalence and strictness on the calibrated Wilson trajectory remain undecided.
PROVED given the cited inputs that weak 4D compact U(1) fails through the surviving even-charge weights, 4D SU(2) at fixed $\beta<2/9$ passes the full variation test, and (I') controls the actual Wilson cost up to $Vt^4=64c_*\beta_K^{5/3}$.
The interacting 5D obstruction is conditional. The fixed interval, the calibrated full budget, (PUR-io) and the mass gap remain open. Hand proofs by Codex, without a separate check or new scientific status.
