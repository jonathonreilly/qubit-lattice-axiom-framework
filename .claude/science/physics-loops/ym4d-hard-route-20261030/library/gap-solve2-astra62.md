## Repo search

**GUIDE** — Row 1145, Codex, pinned at `7070c7c23`. The target-specific prior file is absent. The lead’s 8 November digest searched main and PRs 10114, 10133, 10134 and 10141 for thirteen UV problems. The gap-specific supplement `prior/gap-crux-prior-ym.md` also identifies the soft-kernel work and the hard-route snapshots. I checked the closest transfer result in PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 73–92, 119–149 and 315–339. It treats a one-step loop correlation and gives a contraction for bare coupling at most 1/32. Main’s finite-clock Villain note of 14 September specifies an abelian measure at lines 4 and 79–94. The registry’s W at line 892 points to scalar Wightman reconstruction in `t0-tree.md`, line 67. Row 1145 owns the present infrared question.

**GUIDE** — Row 1143, `gap-solve-astra62.md`, (7), (9)–(11), (16)–(17), and its check in row 1144 supply the winding observables, the fixed-side asymptotic coefficient and the bulk estimate. Row 1028 supplies the comb gauge. Row 1017’s compact-rigidity study (`gap-compact-rigidity-max.md`, § on block maps, line 330) anticipates loss of straight holonomies when a perimeter divergence is present. This note tests it directly on the Wilson trajectory. The council synthesis, §§2–4, records obstructions for positive surface sums and twists alone, and specifies the full-slice minorization still needed.

## Target and plan

**GUIDE** — Use row 720 to fix the quantifiers in (W). Test candidate estimates against the indexed ultraviolet results and the recorded infrared obstructions. The thermal seed is (22) in §7, with the sharper spectral exponent (25) in §11. Equation (24) gives the remaining test at isotropic coupling.

**OPEN** — On the common dyadic physical grid of row 720 put $n_j=L/a_j$. Let $F_\beta(n)=\log Z_\beta(n^4)$, $D_\beta(n)=F_\beta(n)-n^4 f_\beta$, $D^+(L)=\limsup_j D_{\beta_j}(n_j)$, and $z^-(L)=\liminf_j n_j\log(\lambda_0/\lambda_1)$ for the whole gauge-invariant spatial cube. The wall requires $D^+(L')\le D_0$ at every grid size $L'\ge L_0$ and $z^-(L)>256D_0+30$ at one $L\ge4L_0$. The domain and strict margin are those of Theorem ZD-c in `gap-phys-seed.md`, lines 311–320, and item 18 of `gap-zd-astra.md`.

**GUIDE** — Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the Wilson and first-passage normalization, the one-link character formula and the scope of the UV estimates. Credit Tadeusz Bałaban for the ultraviolet renormalization group. At their revision `31a47c543775`, the outline, lines 6844–6861 and 20781–20801, gives $a_j=b^{-K_j}$ and, conditionally, $\beta_j\le h+B_\sharp(1+K_j)$ at fixed reference coupling. CA-I, lines 56419–56455, specifies the conditional use of Bałaban’s step. The outline gives the source-free bounds up to a physical four-volume term at lines 23778–23797. Outline lines 9568–9577 restrict the flat estimate to constrained variables. CA-I, lines 2698–2712, explicitly excludes a mass gap from the theorem. The physical gap is an additional question posed by this lane. PROVED labels a hand argument with its displayed premises. This research note grants no status. Independent review is pending. [Pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L6844-L6869) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2698-L2712)

## 1. Straight winding holonomies at fixed physical size

**PROVED.** In the Wilson measure in four dimensions, condition on all links except a set in which no plaquette contains two selected links. The selected links are independent conditionally. Identify $SU(2)$ with unit quaternions. Each conditional density is a translate of $p_s(u)\propto\exp(s\,\operatorname{Re}u)$, with $0\le s\le6\beta$. Indeed each of the six incident plaquettes contributes one real linear functional of the quaternion, of norm $\beta$. Orientation reversal preserves this description. This is the usual conditional one-link integration.

**PROVED.** Put $b_\beta=1+6\beta$. For an irreducible representation of dimension $d$, the scalar Fourier multiplier of the normalized central density obeys
$$
 0\le \widehat p_s(d)=I_d(s)/I_1(s)\le \exp[-(d-1)/b_\beta].
 \tag{1}
$$
The identity is the normalized (GL3) of Sussman and Alpoge, outline 2197–2231. Here is the uniform bound. For $k\ge1$ the series there gives $R_k=I_{k+1}/I_k\sim s/[2(k+1)]$ at zero. Differentiating the series gives $I_k'=I_{k+1}+kI_k/s$ and $I_{k+1}'=I_k-(k+1)I_{k+1}/s$. Thus $R_k'=1-(2k+1)R_k/s-R_k^2$. The positive root in $R_k$ of the right side is $u_k(s)=\exp[-\operatorname{arsinh}((k+1/2)/s)]$. It increases strictly, and exceeds $R_k$ at small positive $s$. A first contact would give $(R_k-u_k)'=-u_k'<0$, which is impossible at a first contact from below. Since $\operatorname{arsinh}x\ge x/(1+x)$ by integration, $u_k(s)\le\exp[-1/(1+s)]$. Multiplication from $k=1$ to $d-1$ proves (1). At $s=0$ Haar measure gives the claim directly.

**PROVED.** For an ordered path containing $m$ such links, each used just once, condition on its other links and on the exterior as above. Its transport has density $p$ with respect to Haar. With $s_i$ and orientations fixed by the conditioning,
$$
  \|p-1\|_\infty\le \eta(m/b_\beta),\qquad
  \eta(x)=\sum_{d=2}^{\infty}d^2 e^{-(d-1)x}.
  \tag{2}
$$
In each representation the independent factors multiply, giving a product of scalars from (1) times a unitary matrix. Deterministic insertions and inverses preserve that norm bound. Fourier inversion contributes at most $d^2$ times it. Absolute convergence for $m>0$ justifies inversion, for example by equality of all character matrix coefficient integrals. For $x\ge1$, $\eta(x)\le C e^{-x}$ by factoring out $e^{-x}$ and summing at $x=1$.

**PROVED.** Consider $M$ straight edges of an embedded cubical coarse grid in a fine torus of sides at least three. Each edge consists of $h\ge5$ fine steps. Select its interior links, dropping the first and the last. Parallel segments on distinct coarse lines are separated by at least $h$. Collinear links cannot share a plaquette. Perpendicular segments could share a plaquette only within one fine step of a coarse vertex, where the end links were dropped. The same construction works for straight winding lines through one base point, dropping both end links of each based circuit. Thus the $M$ coarse transports are conditionally independent, and, whenever $\eta=\eta((h-2)/b_\beta)<1$, their joint density relative to product Haar lies between
$$
                   (1-\eta)^M\quad\text{and}\quad(1+\eta)^M.          \tag{3}
$$
These bounds survive averaging the conditioning. At any fixed physical mesh on a fixed commensurate torus, $h$ grows exponentially in the RG depth while $\beta_j=O(1+K_j)$. The two bounds tend to one, also for growing boards with $M\eta\to0$.

**PROVED.** In particular, the four straight based Wilson windings on a symmetric physical torus converge in density, uniformly, to four independent Haar variables. On a fixed lattice torus, row 1143, §6, proves that the same windings concentrate at the sixteen central tuples as $\beta\to\infty$. For example the expectation of the square of one normalized trace has the two limits $1/4$ and $1$, respectively. The Haar value follows from character orthogonality for the two-dimensional representation. This gives an actual Wilson observable on which transplanting the fixed-side saddle to a physical box fails.

**PROVED.** The same estimate controls the spectral information retained by a whole spatial board. Use transfer in ordinary time. Let $F$ be any bounded gauge-invariant function of the $M$ straight blocked transports on one slice, with product-Haar mean zero. Write $\nu$ for product Haar and $\delta=(1+\eta)^M-1<1$. The opposite error $1-(1-\eta)^M$ is at most $\delta$. Conditional on the unselected links, the next slice is known, and $|\mathbb E(F_0\mid{\rm exterior})|\le\delta\|F\|_{L^1(\nu)}$. The one-slice marginal gives $\mathbb E|F_1|\le(1+\delta)\|F\|_{L^1(\nu)}$ and $\mathbb E|F_0|^2\ge(1-\delta)\|F\|^2_{L^2(\nu)}$. These statements hold on arbitrarily long periodic time cylinders. The cylinder limit of row 667, §6 (Osterwalder–Seiler and Lüscher), now gives, with $T/\lambda_0=e^{-H_{\rm lat}}$,
$$
 \frac{\langle F\Omega,e^{-H_{\rm lat}}F\Omega\rangle}{\|F\Omega\|^2}
 \le \frac{\delta(1+\delta)}{1-\delta},\qquad
 \frac{\|{\bf1}_{[0,E]}(H_{\rm lat})F\Omega\|^2}{\|F\Omega\|^2}
 \le e^E\frac{\delta(1+\delta)}{1-\delta}.                            \tag{4}
$$
For complex $F$ use $\overline F_0 F_1$. The spectral bound follows termwise from $1_{[0,E]}(t)\le e^{E-t}$. Truncation and centering extend it to all $F\in L^2(\nu)$ with mean zero. At bounded physical energy take $E=a_j E_{\rm phys}$. Equation (4) tends to zero uniformly over these normalized test vectors. This includes the seven products from row 1143. At fixed $M$, even $E=(h-2)/(2b_\beta)$ in lattice units gives a vanishing bound.

**OPEN.** A small transfer compression on the straight grid therefore cannot locate the bottom of the full excited spectrum. A positive operator with an extra orthogonal eigenvector can have exactly the same compression and an extra eigenvalue anywhere in $(0,1)$. Equation (4) gives the loss of overlap for the actual Wilson vectors. Recovering the low-energy spectrum would require a different family of observables and a bound on the states it misses. The possibility of using the integrated variables through their partition function remains. The next calculation keeps their normalization.


## 2. The periodic Wilson coefficient as a scalar determinant

**PROVED.** Let $V=n^4$, $M=3V-3$, $h_0=1/(2\pi^2)$, and let $\Delta_n$ be the scalar graph Laplacian. A prime omits its constant mode. Write $c_n$ for the coefficient of $\beta^{-(9V-3)/2}\log\beta$ in the *periodic Wilson integral* of row 1143, (11). There is a single $C_*>0$, independent of $n\ge3$, such that
$$
 c_n=C_*\,\big[h_0^3(2\pi)^{9/2}\big]^V
             \frac{V^{3/2}}{(\det{}'\Delta_n)^3}.                     \tag{5}
$$
Row 1028, §4.1, Remark 5, gives the gauge-orbit and photon count in a Gaussian abelian model. The extra issue for (5) is the nonabelian commutator source in the saddle of row 1143. Its projection is computed below.

**PROVED.** Use the variables of row 1143, §6, in one sign branch and one sector where a specified holonomy has maximal imaginary part. In its limiting integral the scaled curvature is $d_1 X+S$. Here $d_1$ is the real cubical coboundary, and $X$ vanishes on the comb tree and on the four base wrapping links. The selected face coordinates of row 1143 map to these $M$ edge coordinates with absolute linear determinant one. Each selected face has exactly one new pivot edge with coefficient $\pm1$. In orientation $ij$, $S_{ij}$ equals $2e\times(b_i w_j-b_j w_i)$ on the double seam and vanishes elsewhere. The integration variables $e,b_i,w_i$ and the radial variable $v\in(0,1/4)$ have the domains and measures of that row. They have no $n$ dependence. The matrices from varying $X$ are evaluated at the identity as all four holonomies tend to the centre within this limiting integral.

**PROVED.** Write $B$ for insertion of zeros on the fixed links. The image of $d_1B$ is the full exact two-form space. Indeed a scalar closed one-form is a gradient plus a constant one-form, as follows mode by mode from Fourier transformation. Equivalently one can prescribe any values on the tree and four base edges by a gradient plus four closed seam one-forms. Integrate on the tree with root value zero, then choose the four seam coefficients, one per base edge. This also proves injectivity of $d_1B$. The form $S$ is closed, since $S_{ij}$ depends only on $x_i,x_j$. At a nonzero wave vector the exterior differential is wedge multiplication by $v=(e^{ik_i}-1)_i$. Contraction with $\bar v/|v|^2$ is a contracting homotopy, by the exterior algebra anticommutator. Thus the orthogonal remainder of a closed two-form after subtracting its exact part is its constant mode. The mean of $S_{ij}$ is $2e\times(b_i w_j-b_j w_i)/n^2$. Its constant-mode squared norm is
$$
             \sum_{i<j}|2e\times(b_i w_j-b_j w_i)|^2 .
$$
The factor $V/n^4$ is one. Integrating $X$ in three colors therefore gives $(2\pi)^{3M/2}(\det K)^{-3/2}$ times an exponential with no dependence on $n$, where $K=(d_1B)^*(d_1B)$. The remaining integral and the finite sum of sectors give a positive finite constant by the convergence proof in row 1143. In particular the integration of the small noncommuting modes has been kept.

**PROVED.** To find $\det K$, form a square change of basis on real one-forms. Its columns are gradients of single-vertex functions with one root omitted, the four closed seam indicators, and $B$. Its determinant has modulus one, by the triangular tree, four-edge and free-edge reconstruction just described. The volume of the gradient columns is $(\det{}'\Delta_n/V)^{1/2}$. Indeed the squared volume is a diagonal cofactor. The adjugate of the connected graph Laplacian is a multiple of the projection on constants, with trace $\det{}'\Delta_n$, so each cofactor is $\det{}'\Delta_n/V$. After removing gradients, each seam indicator has only its harmonic projection, of norm $\sqrt V/n$. The four projections are orthogonal. Their joint volume is $V$. It follows that the projections of the $B$ columns normal to the closed one-forms have volume $(V\det{}'\Delta_n)^{-1/2}$. On that normal space, $d_1^*d_1$ has each nonzero Fourier eigenvalue of $\Delta_n$ three times, since at momentum $k$ it acts as $|v|^2$ on the complement of $v$. Hence
$$
                 \det K=(\det{}'\Delta_n)^2/V.
$$
Each one of the $M+4$ Haar coordinates in the saddle contributes its density factor $h_0$, with the polar Jacobians of the four holonomies already in the residual integral. Absorbing all volume-independent factors proves (5).

**OPEN.** Formula (5) determines the entire lattice-size dependence of the leading coefficient taken at each fixed $n$. The size dependence of the error in the Wilson integral remains to be compared with it.


## 3. Bulk subtraction and the size of the physical remainder

**PROVED.** Put $\lambda(\theta)=2\sum_{i=1}^4(1-\cos\theta_i)$ and $h=\int_{[-\pi,\pi]^4}\log\lambda(\theta)\,d\theta/(2\pi)^4$. There is a finite shape constant $k_\Delta$ with
$$
              \log\det{}'\Delta_n=n^4h+2\log n+k_\Delta+o(1).
              \tag{6}
$$
The bounded-error version is recalled in row 1028, Remark 5. Here is a hand proof for the scalar operator used in (5). Let $p_t(x)$ be the Fourier coefficient of $e^{-t\lambda(\theta)}$ on $\mathbb Z^4$ and $H_n(t)=\operatorname{Tr} e^{-t\Delta_n}$. These coefficients are nonnegative and sum to one by expanding each exponential in the eight unit steps. Their number of steps has the Poisson law of mean $8t$. Fourier periodization gives $H_n(t)=n^4\sum_m p_t(nm)$. Integrating $\log u=\int_0^\infty(e^{-t}-e^{-ut})\,dt/t$ for each nonzero eigenvalue and for the bulk gives
$$
 \log\det{}'\Delta_n-n^4h
  =\int_0^\infty[1-e^{-t}-H_n(t)+n^4p_t(0)]\,dt/t.
$$
The bulk interchange follows from the integrable logarithmic singularity at zero, or from $p_t(0)\le C(1+t)^{-2}$ and the bounded symbol at small $t$.

**PROVED.** For $t\le1$ the nonzero images in $H_n$ cost at least $n$ steps. Thus their contribution integrated against $dt/t$ there is at most $n^4\,8^n e^8/(n\,n!)$, tending to zero. For $1\le t\le n^2$, shift each Fourier contour by imaginary part of magnitude $1/\sqrt t$ with the sign giving spatial decay. Cauchy's theorem applies to the entire periodic integrand. Since $t(\cosh(t^{-1/2})-1)$ is bounded and $1-\cos\theta\ge 2\theta^2/\pi^2$ on $[-\pi,\pi]$,
$$
 p_t(x)\le C t^{-2}e^{-|x|_1/\sqrt t},\qquad
 0\le H_n(t)-n^4p_t(0)\le C n^4t^{-2} e^{-n/\sqrt t}.
$$
The image sum uses four convergent geometric series with $n/\sqrt t\ge1$. At $t=n^2u$, $u\ge1$, use the same lower bound on the symbol in the frequency sum to get $H_n(n^2u)-1\le C e^{-cu}$ and $n^4p_{n^2u}(0)\le C u^{-2}$. For each fixed $u>0$ the frequency sum converges to $\sum_{m\in\mathbb Z^4}e^{-4\pi^2u|m|^2}$ by domination. Rescaling $\theta$ in the bulk integral gives $n^4p_{n^2u}(0)\to(4\pi u)^{-2}$ by Gaussian domination. The bounds at $u\le1$ and $u\ge1$ are integrable against $du/u$ after the indicated subtractions. On $[0,n^2]$ the part $\int(1-e^{-t})\,dt/t-2\log n$ has a finite limit. On $[n^2,\infty)$ the term $e^{-t}$ tends to zero in the integral. This proves (6).

**PROVED.** In the Haar convention of row 1143, its bulk constant in (16) is
$$
               c_\infty=3\log h_0+\tfrac92\log(2\pi)-3h.             \tag{7}
$$
Use its open-box comparison (14)–(16), which gives $f_\beta=b^{-4}\log G_{b,\varnothing}(\beta)+O((\log\beta)/b)$ for $b=\lceil\beta^\gamma\rceil$, $0<\gamma<1/12$. In an open $b^4$ cube the kernel of curl on one-forms is the gradient space, by integrating a curl-free form along coordinate paths and interchanging successive perpendicular steps. The same determinant change of basis as above, now with only the tree fixed, gives
$$
 \det K_{\varnothing}
 = b^4\prod_{m\ne0}\lambda_m^{\,r(m)-2},\qquad
 \lambda_m=4\sum_i\sin^2(\pi m_i/(2b)),\quad 0\le m_i<b,\quad
 r(m)=\#\{i:m_i>0\}.
$$
Indeed on one interval the normalized vertex cosine modes proportional to $\cos(\pi m(x+1/2)/b)$ are orthogonal. For $m>0$ the edge differences are orthogonal sine modes of norm $2\sin(\pi m/(2b))$ relative to the vertex norm. The finite geometric series proves orthogonality, and the mode counts $b$ and $b-1$ give bases. Tensor these bases in four coordinates. At $m\ne0$ the one-form space has dimension $r(m)$, gradient rank one and curl-square eigenvalue $\lambda_m$ on the remaining $r(m)-1$ components, by the same wedge/contraction identity. Divide that nonzero determinant by the squared gradient volume $\prod_{m\ne0}\lambda_m/b^4$. This proves the formula. Modes on the coordinate faces change its logarithm from $2\sum_{m\ne0}\log\lambda_m$ by $O(b^3\log b)$. The Riemann mean of $\log\lambda_m$ converges to $h$ by evenness. Near zero, in shells $l\le |m|_\infty<l+1$, at most $C(l+1)^3$ terms have absolute log at most $C+2\log(b/l)$ for $l\ge1$ and $l/b$ small. Their normalized sum up to $\epsilon b$ is $O(\epsilon^4(1+|\log\epsilon|))$ in the limit. Thus $b^{-4}\log\det K_{\varnothing}\to2h$. The ratio of free edges to volume is $3+O(1/b)$, also in the term multiplying $\log\beta$. Substitution in row 1143's Gaussian integral proves (7). Credit Chatterjee for the bulk weak-coupling asymptotic in the $U(N)$ setting, as recorded in that row.

**PROVED.** Let $B(\beta)=\tfrac32\log\beta+\log\log\beta$ for $\beta>1$, and $C(n)=\log c_n-n^4 c_\infty$. Equations (5)–(7) give
$$
 C(n)\longrightarrow \log C_*-3k_\Delta,\qquad
 D_\beta(n)=B(\beta)+C(n)+R_\beta(n),\qquad
 \lim_{\beta\to\infty}R_\beta(n)=0\quad\text{for each fixed }n.
 \tag{8}
$$
The last assertion is exactly (17) of row 1143. The shape term stays bounded as $n$ grows. It cannot cancel either logarithm. In particular the iterated limit $\lim_{n\to\infty}\lim_{\beta\to\infty}(D_\beta(n)-B(\beta))$ exists.

**PROVED, conditional only where indicated.** On *any* sequence with $\beta_j,n_j\to\infty$ and $0\le D_{\beta_j}(n_j)\le A<\infty$, (8) forces
$$
                  R_{\beta_j}(n_j)=-B(\beta_j)+O_A(1).              \tag{9}
$$
There is an application before (W). If the account supplies one fixed admitted torus with the density comparison in row 720, §1.1.5(iii), then that torus has (APR). For any *fixed* larger physical size, use the monotonicity of the normalized log partition function in each lattice side. In one direction it is the monotonicity of $(\sum_i\lambda_i^k)^{1/k}$ in $k$, followed by rotation to treat each of the other sides. Hence $D_\beta(n)\le(n/n_*)^4 D_\beta(n_*)$ for $n\ge n_*$. This supplies $A$ in (9) for each such fixed physical size, with $A$ allowed to grow as its fourth power. Even without (APR), (9) holds at every size at which the proposed (BDD-Delta) bound holds, with an arbitrarily small eventual increase of that bound for a limsup.

**PROVED.** A finite inverse-coupling expansion for the *excess remainder* of the form
$$
       R_\beta(n)=\sum_{q=0}^Q\beta^{-q}P_q(\log n)+O(1),
                       \qquad \deg P_q\le q,
       \tag{10}
$$
with fixed coefficients and uniformly bounded error, cannot reach even the one physical torus in (9). The lower and upper passage-time bounds in (RF25) give $\log n_j=O(\beta_j)$ there. Every term of (10) is bounded while (9) diverges. This objection concerns precisely (10). A resummation singular at the terminal value of $(\log n)/\beta$, or a different nonperturbative remainder, is outside that class.

**OPEN.** A resummed estimate would need the finite physical remainder *after* the two cancellations in (9), uniformly as the physical size tends to infinity. The scalar determinant has exhausted its contribution to this question.


## 4. A three-cylinder test that cancels the running normalization

**GUIDE.** One could absorb (9) into a running coupling in the constant-mode integral and then transfer the remaining determinant to the physical box. To test this, vary the time period at one spatial size. Both a common multiplicative renormalization and the vacuum energy then cancel.

**PROVED.** Formula (5) holds with the *same* $C_*$ on every rectangle $\boldsymbol n=(n_1,n_2,n_3,n_4)$, $n_i\ge3$, $V=\prod_i n_i$, and $\Delta_{\boldsymbol n}$ in the denominator. For each fixed rectangle the comb construction and domination in row 1143, §6, use finitely many plaquettes and based loops of bounded length. Their constants may depend on all four sides. The weak-coupling limit is taken before any side varies. The product of harmonic one-form norms remains $\prod_i(\sqrt V/n_i)=V$. For the two-form term set $s_i=V^{1/4}/n_i$ so that $\prod s_i=1$. In the sector whose maximal holonomy has index $q$, take $b_q=1$, $w_q=0$ as in row 1143. The zero-mode exponent is a fixed multiple of
$$
      \sum_{i<j} s_i^2s_j^2|b_iw_j-b_jw_i|^2.
$$
Set $u_i=s_i b_i$. For each of the two perpendicular components of $w$, the $3\times3$ Gaussian matrix is
$\operatorname{diag}(s_{-q})(|u|^2 I-u_{-q}u_{-q}^{\,t})\operatorname{diag}(s_{-q})$.
Its determinant is $(\prod_{i\ne q}s_i)^2|u|^4 u_q^2=|u|^4$. Gaussian integration over both components leaves a common constant times $|u|^{-4}$. The sum of the remaining integrals over $|b_i|\le1$, $i\ne q$, equals $\int_{\mathbb R^4}e^{-\sum s_i^2 x_i^2}\,dx=\pi^2$. To see this, partition the latter integral according to the largest $|x_q|$, write $x_q=\pm r$, $x_i=\pm r b_i$ with the same sign, and integrate $2r^3e^{-r^2|u|^2}$ over $r>0$. Thus the commutator integral is shape independent, including anisotropic time periods.

**PROVED.** Write $Z_n(T)$ for the partition function on $(n,n,n,T)$. For each nonzero spatial frequency $p\in(\mathbb Z/n)^3$ set $2(\cosh\omega_p-1)=4\sum_i\sin^2(\pi p_i/n)$. The temporal product of Laplacian eigenvalues at that frequency is $e^{T\omega_p}(1-e^{-T\omega_p})^2$. Indeed the roots of $z^T-1$ give $\prod_{j=0}^{T-1}(1-re^{2\pi i j/T})=1-r^T$ at $r=e^{-\omega_p}$. At $p=0$ the product over nonconstant time modes is $T^2$, by evaluating $(z^T-1)/(z-1)$ at one and squaring the modulus. Consequently, with $A=h_0^3(2\pi)^{9/2}$, the coefficient of the fixed-rectangle Wilson integral is
$$
 c_{n,n,n,T}= C_* n^{9/2} T^{-9/2}
       \left[A^{n^3}e^{-3\sum_{p\ne0}\omega_p}\right]^T
       \prod_{p\ne0}(1-e^{-T\omega_p})^{-6}.                          \tag{11}
$$

**PROVED.** For integers $n,k\ge3$ define
$$
 {\cal K}_\beta(n,k)=\log\frac{Z_n(k)Z_n(3k)}{Z_n(2k)^2}.
$$
At fixed $n,k$, row 1143 and (11) give
$$
 \lim_{\beta\to\infty}{\cal K}_\beta(n,k)
 =\tfrac92\log(4/3)
  +6\sum_{p\ne0}\log\frac{(1+x_p)^2}{1+x_p+x_p^2}
 >\tfrac92\log(4/3),\qquad x_p=e^{-k\omega_p}.                       \tag{12}
$$
The factors exponential in time, the common $\beta^{3/2}\log\beta$, and the unknown $C_*$ cancel. The strict inequality uses $(1+x)^2>1+x+x^2$. For the actual transfer, write $g(k)=\log(1+S(k;n^3))$. Positivity and Cauchy–Schwarz on its eigenvalue list give $\mathcal K\ge0$. Since $g$ decreases,
$$
      \mathcal K=g(k)+g(3k)-2g(2k)\le g(k).                            \tag{13}
$$
At a physical seed of row 720 one can take $k=n$ and use $S(n)\le S(n/2)$. Thus the seed requires $\limsup_j\mathcal K_{\beta_j}(n_j,n_j)\le\log(1+1/1650)$. The strict margin of that row can only strengthen this bound.

**PROVED.** The effect in (12) persists within the neutral sector. For a temporal twist $w\in(\mathbb Z/2)^3$, write $Z^w_n(T)$ for the signed-plaquette partition function. If $w\ne0$, at every *fixed* rectangle,
$$
               Z^w_n(T)=O_{n,T}(\beta^{-9V/2}).
$$
For a single odd component this is row 1143, (3)–(4). For several, choose an odd component $i$. In the four-holonomy integral replace $h_l$ by $h_i^{-1}h_l$ for the other odd spatial components $l$ and keep $h_i,h_t$ fixed. This change preserves product Haar. The new commutation signs have only the $it$ minus sign. To bound the errors, commute two transformed words (length at most two) by swapping their individual letters. Each swap gives its prescribed central sign and chordal error $|h_jh_l-\epsilon_{jl}h_lh_j|$. An inverse letter has the same bound by unitary invariance. The triangle inequality and then squaring bound the total new signed action by a universal multiple of the original four-variable action. Hence its old integral at strength $s$ is at most the one-plane integral at $s/C$. Apply the upper half of row 1143, (1), at fixed shape. The periodic leading coefficient in (11) then gives $Z^w_n(T)/Z_n(T)\to0$. The standard centre projection of row 720 (TM-c) yields $Z_{n,e}(T)=2^{-3}\sum_w(-1)^{e\cdot w}Z^w_n(T)$ in flux sector $e$. This is the time-$T$ transfer trace with the sector projector inserted. Averaging the commuting centre flips against the sector character gives the projector. Every sector therefore has $Z_{n,e}(T)/Z_n(T)\to1/8$. The three-cylinder log ratio in each sector has *the same* limit (12). The floor remains if all seven nontrivial flux sectors are removed.

**PROVED.** More generally suppose a candidate for the three physical cylinders has the form
$$
 Z_n(t)=A_0e^{Bt}t^{-\nu}Q(t)e^{r(t)},\qquad t=k,2k,3k,              \tag{14}
$$
where $A_0>0,B$ may depend arbitrarily on cutoff and spatial size, and $Q(2k)^2\le Q(k)Q(3k)$. Every positive thermal trace meets the condition on $Q$, by Cauchy–Schwarz, including products of oscillators with arbitrary positive frequencies. At a seed, (13) implies
$$
 \limsup_j\big[r(k)+r(3k)-2r(2k)\big]
 \le \log(1+1/1650)-\nu\log(4/3)
 \quad (k=n_j)
 \tag{15}
$$
for fixed $\nu$. In particular a change in the running normalization, a shift of the vacuum energy and even a mass for *all* the nonzero momentum oscillators still fail this test if they keep $\nu=9/2$ from (11) and an affine or vanishing residual curvature. The same test applies to the neutral trace because its vacuum is the full vacuum and its excited sum is bounded by the full $S$. This is a sign and size constraint on an aspect-ratio correction, independent of the divergence in (9).

**OPEN.** In the full physical transfer the interacting zero modes could change the factor $t^{-9/2}$. Neither (11) nor its derivation estimates that change when $n,k$ grow with the cutoff. More generally (13) runs from a small thermal sum to small curvature. An upper bound on curvature alone leaves the multiplicity of near-vacuum levels uncontrolled.


## 5. Removing the vertex gauge projection at physical time

**GUIDE.** The straight-grid compression misses information. Instead keep *all* spatial links and test the unprojected transfer kernel. The starting identity is HAM1 of *gap-global-reform-max*, §4.5, and the temporal-gauge argument in row 667, Remark 1.8. Their character coefficients are static-charge partition functions. The following estimate controls them simultaneously, with constants independent of the spatial cube.

**PROVED.** On the periodic $n^3\times T$ lattice, $n,T\ge3$, let $H_x$ be the ordered temporal holonomy at each spatial vertex $x$. Conditional on *all* spatial links, the temporal link vectors $G_t=(g_{x,t})_x$ at different layers are independent. Each temporal plaquette uses two temporal links in a single layer, at neighboring spatial vertices. For a list of $SU(2)$ representations of dimensions $d_x$ write $\pi=\bigotimes_x\pi_{d_x}$ and $w=\sum_x(d_x-1)$. Then
$$
 \left\|\mathbb E[\pi((H_x)_x)\mid\text{spatial links}]\right\|_{\rm op}
              \le \exp[-Tw/(7 b_\beta)] .                             \tag{16}
$$
Color the spatial nearest-neighbor graph with seven colors by greedily coloring a fixed order of vertices. A vertex has at most six already colored neighbors. Select a color carrying at least $w/7$ of the weight. Within one layer, condition on all temporal links outside that color. The remaining links enter separate plaquettes and have the translated densities of §1. Conditional expectation in the tensor representation acts by a product of matrices, each of norm bounded by (1) on the chosen color and of norm one outside. Integrating the others preserves the norm upper bound. Independent layers multiply these matrices in time order, giving (16). The proof works also when adjacent spatial sites both carry charges.

**PROVED.** Put $N=n^3$ and let $\mathsf T=M C_{\mathcal E} M$ act on *all* square-integrable functions of the spatial links, with the half magnetic weight $M$ and the electric convolution of row 667. Write $P$ for vertex gauge averaging and $\lambda_0$ for the vacuum eigenvalue. The full temporal holonomy vector has a continuous density $p$ relative to product Haar and
$$
 \|p-1\|_\infty\le \big[1+\eta(T/(7b_\beta))\big]^N-1,\qquad
 1\le \frac{\operatorname{Tr}\mathsf T^T}{\operatorname{Tr}(P\mathsf T^T)}
      =p({\bf1})\le \big[1+\eta(T/(7b_\beta))\big]^N.                 \tag{17}
$$
For the first bound sum the matrix coefficient estimate (16) as in (2). Representation dimensions multiply across sites, so the sum factors into $N$ copies of $1+\eta$. In temporal gauge, at prescribed holonomies $h$ the unnormalized density is $\operatorname{Tr}(\mathsf T^T U(h))$, where $U(h)$ implements the vertex gauges up to the inverse convention. Integrating $h$ inserts $P$, and $h=\mathbf1$ inserts the identity. This follows by successively changing the spatial variables by the products of temporal links, as in the cited Remark 1.8. The continuous versions agree everywhere. The lower bound at the identity follows from commutation with $P$ and positivity of $\mathsf T$. For $n_j=L/a_j$, $T_j=t/a_j$, $L,t>0$ fixed and commensurate, $N\eta(T_j/(7b_{\beta_j}))\to0$. The relative error of removing $P$ tends to zero in the full thermal trace even as the number of spatial sites grows.

**PROVED.** Decompose the vertex gauge representation into isotypic components $\mathscr H_\pi=V_\pi\otimes\mathscr M_\pi$. On each, $\mathsf T=I\otimes T_\pi$. Taking the character coefficient in the temporal-gauge identity gives $\operatorname{Tr}T_\pi^T/\operatorname{Tr}(P\mathsf T^T)=\mathbb E\prod_x\chi_{d_x}(H_x)$. Formula (16) bounds this nonnegative ratio by $(\prod_xd_x)e^{-Tw/(7b_\beta)}$. At fixed $\beta,n$, take $T$-th roots and send $T\to\infty$. Positivity and trace class give, for every component present,
$$
             -\log(\|T_\pi\|/\lambda_0)\ \ge\ \frac{w}{7b_\beta}.     \tag{18}
$$
Thus every *local gauge charge* costs at least $1/(7a_j b_{\beta_j})\to\infty$ in physical energy. This removes an entire part of the enlarged Hilbert space at any bounded physical energy. All eight physical electric-flux sectors are in $\mathscr M_{\bf1}$ and give $w=0$ in (18). HAM1 identifies this distinction. Equations (16)–(18) give the quantitative estimate. The projection in the outline at 2315–2335 is exact at finite cutoff. Equation (17) concerns the separate unprojected operator.


**PROVED.** Test the remaining singlet problem by comparing the full kernel to the product electric kernel. Let $I(\beta)=\int e^{-\beta a(u)}\,du$, $\widehat C=C_{\mathcal E}/I(\beta)^{3N}$, and $\widehat\lambda_0=\lambda_0/I(\beta)^{3N}$. There exist absolute $c,C>0$ such that
$$
                e^{-CN}\le \widehat\lambda_0\le e^{-cN}
                \quad(n\ge3,\ \beta\ge1).                             \tag{19}
$$
For the upper bound, choose $\lfloor n/2\rfloor^2 n\ge N/9$ edge-disjoint spatial plaquettes in coordinate planes. Drop the other plaquette weights in $\widehat C M^2 {\bf1}$. The electric step resamples different links independently. With all but one link of a retained plaquette fixed, Cauchy–Schwarz for two translates of $e^{-\beta a}$ bounds the plaquette average by $I(2\beta)/I(\beta)$. This ratio is strictly below one on $[1,\infty)$ and tends to $2^{-3/2}$ by the single-link Gaussian limit (Haar angle integration), so its supremum $q$ is below one. The independent plaquettes give the row-sum bound $q^{N/9}$. The operator $M\widehat C M$ is similar to $\widehat C M^2$ at each fixed cube and coupling. Its positive continuous top eigenfunction gives the same row-sum bound on the top eigenvalue. It is invariant by uniqueness.

**PROVED.** For the lower bound take a trial function equal to the indicator that all spatial links lie in the identity ball of angular radius $\beta^{-1/2}/4$. On this set each plaquette costs at most a constant in $\beta a$, by the triangle inequality. From every point in the ball each one-link electric transition assigns the ball probability at least $c_1>0$, uniformly for $\beta\ge1$. Its Haar volume is at least $c_2\beta^{-3/2}$, the translated weight there is at least a positive constant and $I(\beta)\le C_2\beta^{-3/2}$. The product transition in the Rayleigh quotient gives the lower bound in (19), since it has $3N$ links and there are $3N$ spatial plaquettes.

**PROVED.** A bare one-step electric flux estimate loses its normalization by (19). By row 863, Lemma A1, in a nonzero centre flux direction every transverse cut of a contributing electric spin network has an odd number of half-integer crossings. This follows by applying the centre flip on the cut to a Peter–Weyl product. Moving the cut is a vertex gauge transformation on physical states. The $n$ disjoint cuts require at least $n$ nontrivial link factors. The electric norm on the physical sector whose only odd bit is the specified direction is *exactly* $r_\beta^n$, $r_\beta=I_2(\beta)/I_1(\beta)$ in Bessel notation. Indeed $I_d/I_1\le r_\beta$ for every $d\ge2$ by the ratio bound in §1, and a traced straight fundamental winding attains $r_\beta^n$. Magnetic multiplication preserves the sector and has norm at most one. Thus the estimate from this comparison is $\lambda_e/\lambda_0\le r_\beta^n/\widehat\lambda_0$. Its right side grows beyond one on every physical sequence since $r_\beta\to1$ by concentration of the single-link density, while (19) gives a factor at least $e^{c n^3}$ in the quotient. The singlet vacuum normalization must be canceled within the estimate itself to use this route.

**OPEN.** Equations (17)–(18) justify working with the unconstrained transfer at physical times. The eigenvalues still needing an estimate for (W) are in its local-gauge singlet subspace, including its centre-even excitations. A site gauge rotation acts as the identity throughout that subspace. The rigid on-link symmetry classification (CEN+ in *gap-global-reform-max*, §4.1) leaves only centre cocycles in addition to gauge rotations under its hypotheses. It offers no continuous rotation of the neutral sector to which the charge bound can be applied.


## 6. Can a temporal boundary condition pay for the magnetic term?

**PROVED.** Fix a temporal twist $w$ in plane $it$, with its minus signs at the temporal seam and the spatial cut $x_i=n-1$. Include also the periodic case $w=0$. Write $Z^w(h)$ for the spatial integral in temporal gauge, with prescribed last temporal links $h=(h_x)_x$, and $Z^w=\int Z^w(h)\,dh$. Changing a plaquette sign changes a one-link conditional staple vector but preserves the bound on its norm and the coloring argument of (16). The temporal-gauge change of variables preserves central signs. Therefore for each case separately $Z^w(h)/Z^w=1+O(\delta_T)$ uniformly in $h$, where $\delta_T=[1+\eta(T/(7b_\beta))]^{n^3}-1$. This estimate applies at the specified pins by continuity even though a single pin has Haar measure zero. On a fixed physical cylinder $\delta_T\to0$.

**PROVED.** Two deterministic pins reverse the sign of the minimal-action comparison, on the *same* physical cylinders. Let $h^0_x=1$ everywhere. Let $h^1_x=-1$ on the plane $x_i=0$, and $+1$ elsewhere. For central pins each spatial link $e=xy$ has time boundary sign $h_x h_y$ times its twist sign. If this sign is negative, its temporal contribution, with the bare factor $\beta$ omitted, is at least $T(1-\cos(\pi/T))$. In fact for unit quaternions $u_t$ on that link it is $\frac12\sum_{t=0}^{T-1}|u_{t+1}-u_t|^2$, with $u_T=-u_0$. The allowed scalar frequencies are $(2k+1)\pi/T$, so the smallest eigenvalue of the time difference squared is $2(1-\cos(\pi/T))$. Positive boundary signs cost at least zero. For these two pins every negative link is an $i$-edge and its sign depends only on $x_i$. Set it to $\exp(v\pi t/T)$ at slice $t$ for a fixed unit imaginary quaternion $v$, and set the other links to one. All spatial plaquettes are one, and every negative edge attains the lower bound. This proves the exact minima.

**PROVED.** Write $\Delta m(h)$ for the twisted minimum minus the periodic minimum, without $\beta$, and $m=n^2 T(1-\cos(\pi/T))$. At $h^0$ the numbers of negative edges are $n^2$ and zero. At $h^1$ the untwisted seam signs change on two cuts and the twist cancels one of them. Thus
$$
              \Delta m(h^0)=m,\qquad \Delta m(h^1)=-m .
$$
The *difference* between the two log partition-function comparisons, however, is $O(\delta_T)$ by the first paragraph. In particular, with $E(h)=\log[Z^w(h)/Z^0(h)]+\beta\Delta m(h)$,
$$
              E(h^0)-E(h^1)=2\beta n^2 T(1-\cos(\pi/T))+O(\delta_T).
                                                                         \tag{20}
$$
At $T=n$ this has order $\beta n$ on the actual Wilson trajectory. At least one of the two fluctuation corrections has absolute value at least $\beta m-O(\delta_T)$. Uniform control by the minimum with an $o(\beta n)$ fluctuation error is impossible, even after removing the vertex projection at a relative cost tending to zero. This conclusion uses neither (APR) nor (W).

**OPEN.** One could instead pin two centre sheets and try to factor their cost at large spatial separation. A pair bounding a slab is a vertex sign transformation, so its insertion costs $o(1)$ by (17), for any fixed physical separation with commensurate cuts. A single noncontractible sheet inserts a global centre flip $C_i$. On the physical space its normalized trace is $1-2\operatorname{Tr}_{i\text{-odd}}(\mathsf T^T)/Z^0$. Squaring the *operator* gives one for every possible odd-sector population. Thus the free pair alone puts no small upper bound on that population. For instance a positive transfer with even and odd eigenvalues $1,e^{-\epsilon}$ has the pair identity for every $\epsilon>0$, while the single trace ratio at time $T$ is $(1-e^{-\epsilon T})/(1+e^{-\epsilon T})$. Factorization would require a further estimate that resolves the odd-sector population. The neutral-sector obstruction in (12)–(15) would still apply.


## 7. Continuing from the exactly seeded electric theory

**GUIDE.** Keep the temporal coupling $\beta$ at its actual trajectory value. Turn the spatial coupling $s$ from zero to $\beta$. This is Claude Fable’s interpolation in row 863, *gap-crux-skeleton-max*, §3, Lemmas A1–A3. A1 supplies the cut bound used in §5. A2 already gives the electric seed. Here the question is whether analytic continuation in $s$ can preserve it. Work on the actual projected spatial cube. Scalar factors exponential in time have no effect on a thermal ratio.

**PROVED.** Write $K=P\widehat C$ restricted to the invariant space, $X(U)=\sum_{p\ {\rm spatial}}\tfrac12\operatorname{tr}U_p$, $N=n^3$, and $B(z)=e^{zX/2}K e^{zX/2}$. The anisotropic Wilson partition function at time $T$ differs from $Z_T(z)=\operatorname{Tr} B(z)^T$ only by a nonzero exponential of an affine function of $z$. At the electric endpoint the vacuum is the constant one, with eigenvalue one. All other eigenvalues of $K$ are at most $e^{-1/b_\beta}$ by (1). Also $1\le Z_T(0)\le[1+\eta(T/b_\beta)]^{3N}$ from the product kernel without projection. On a sequence of physical cylinders the last bound tends to one.

**PROVED.** On every such sequence the finite-volume partition function has a complex spatial-coupling zero within $C/\beta$ of the electric endpoint, for all sufficiently fine cutoffs. Here $C$ is absolute. To prove this let $Y=\sum_{t=0}^{T-1}X(U_t)$ in the electric Wilson ensemble. Its mean is zero. Flipping one spatial link and all its time translates preserves the electric action, and reverses the sign of any spatial plaquette using it once. With normalized Haar at one time, the $3N$ distinct fundamental plaquette traces, each divided by two, are mutually orthogonal and have squared norm $1/4$. An edge appearing only once makes a cross term vanish. Each trace is a four-link eigenfunction with eigenvalue $r_\beta^4$. For $0\le s<T$ the transfer trace $\operatorname{Tr}(K^{T-s}X K^s X)$ is a sum of nonnegative terms in an eigenbasis of $K$. Retaining the constant state in the first factor gives
$$
 \operatorname{Var}_0Y\ \ge\
       \frac{3NT}{4Z_T(0)}\sum_{s=0}^{T-1}r_\beta^{4s}
       \ \ge\ cNT\beta.                                               \tag{21}
$$
For the last step $1-r_\beta\le C_1/\beta$ for $\beta\ge1$. This is the one-link mean of $1-\cos\theta$ and follows by bounding its Haar-angle numerator by $C\beta^{-5/2}$ and the denominator below by $c\beta^{-3/2}$. For $s\le\beta/(8C_1)$ Bernoulli's inequality gives $r_\beta^{4s}\ge1/2$. Eventually $T$ exceeds that interval and $Z_T(0)\le2$.

**PROVED.** The entire function $\Xi(z)=\mathbb E_0 e^{zY}=Z_T(z)/Z_T(0)$ equals one at the origin and obeys $|\Xi(z)|\le e^{3NT|z|}$. On any open zero-free disk of radius $R$ let $f=\log\Xi$ with $f(0)=0$. For $r<R$ the function $3NTr-\operatorname{Re} f(re^{i\theta})$ is nonnegative with circle mean $3NTr$. Its second Fourier coefficient has modulus $r^2|f''(0)|/4$, at most that same mean. Since $f''(0)=\operatorname{Var}_0Y$, (21) forces $R\le C/\beta$. The zeros of an entire function with value one at zero are isolated, so some zero is at that distance or less. In particular one Taylor disk for the log partition function cannot reach $z=\beta$. This is a statement about spatial coupling at large temporal coupling. Row 1004 and its check 1008 use a different complex source. Zeros proved here lie off the real axis. They do not exclude a real interpolation or cancellation between two cylinder free energies.


**PROVED.** A matching positive result holds on physical cylinders. For $\beta\ge1$ there are common absolute constants $c,C,A>0$. For $H=\lceil A b_\beta\rceil$, $m=\lfloor T/H\rfloor\ge8$ and $C N m e^{-m/4}$ sufficiently small, the *projected* $Z_T(z)$ and $Z_{2T}(z)$ are zero-free on $|z|\le c/(1+\beta)$. On that disk their logarithms have branches satisfying
$$
 \left|2\log Z_T(z)-\log Z_{2T}(z)\right|\le C N m e^{-m/4}.           \tag{22}
$$
In particular, throughout the real interval $0\le s\le c/(1+\beta)$, the excited thermal sum at time $T$ tends to zero along the physical sequence. Row 863, §§3.4 and 8.2, proposed this region as (KS-ZONE). Check 879 records its status there as open. These are anisotropic Wilson measures.

**PROVED — block construction.** First prescribe the last temporal gauge $h$ as in §6 and let $Z_{T,h}(z)$ use the electric normalization of §7. Time is now a product of one-link Markov chains with the magnetic weights inserted. Divide $T$ into $m$ blocks, the first $m-1$ of length $H$, the last of length in $[H,2H)$. For $2T$ repeat this schedule twice. For each spatial link and block of length $l$, integrate its electric path given its two endpoints. Its endpoint transition is $D_l(u,v)$, the $l$-fold normalized electric convolution. At the seam the upper endpoint is $h\cdot v$. Its bridge is the probability measure on the $l-1$ interior links with density the product of transitions divided by $D_l$. This denominator is strictly positive. Regard all block endpoints as independent Haar variables. Given them, use independent normalized bridges for different spatial links and blocks. This defines a probability reference for two types of local factor.

- One factor $1+(D_l-1)$ for each spatial link and block,
- One factor $1+(\exp[z\sum_{t\ {\rm in\ block}}w_p(U_t)]-1)$ per spatial plaquette and block, with $w_p=\frac12\operatorname{tr}U_p$ and the upper time endpoint excluded.

Their product expectation is exactly $Z_{T,h}(z)$. The reference factorizes on families with disjoint endpoint and bridge variables. The estimate (2) gives $\|D_l-1\|_\infty\le\eta(H/b_\beta)$. A plaquette insertion minus one has norm at most $e^{2H|z|}-1$. Set $D=64$, choose $\sigma>0$ with $\sigma e^2\le1/(4D^3)$, then choose fixed $A$ with $\eta(A)\le\sigma$. Finally choose $c>0$ so that $2Hc/(1+\beta)\le\log(1+\sigma)$ for every $\beta\ge1$, enlarging $A$ to at least one if needed. Both types of insertion minus one are now bounded by $\sigma$ throughout the disk.

**PROVED — connected logarithm.** Join two insertion labels when their spatial link sets intersect and their blocks are equal or adjacent, cyclically. A label uses at most four links. A link belongs to its own label and four spatial plaquette labels per block. Its closed neighborhood therefore has size at most $4\cdot3\cdot5\le D$. Write $F_i$ for the full factor at label $i$. Expanding the product gives a gas of connected sets $X$ with activity $z_X=\mathbb E_{\rm ref}\prod_{i\in X}(F_i-1)$. Separated components factor by the reference construction. Two polymers are incompatible when they intersect or are adjacent. Thus $|z_X|\le\sigma^{|X|}$. At a fixed label there are at most $D^{2(r-1)}$ connected sets of size $r$. Traversing a spanning tree from the label and back gives a walk of length $2(r-1)$ whose visited labels determine the set. Consequently
$$
 \sum_{Y\not\sim X}|z_Y|e^{2|Y|}
 \le D|X|\sum_{r\ge1}D^{2(r-1)}(\sigma e^2)^r\le |X|.
$$
Use the Kotecký–Preiss criterion with $a_X=|X|$ and activities enlarged in modulus by $e^{|X|}$. The tree proof and absolute log bound are given by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, outline 1225–1269 and 1273–1347. It follows that the connected log series exists and that its absolute sum weighted by $e^{\sum|X|}$ is at most $\sum_X|z_X|e^{2|X|}\le6Nm$. The latter follows by summing the fixed-label estimate over the $6Nm$ labels. In particular all terms with $\sum |X|\ge m/4$ contribute at most $6Nm e^{-m/4}$ in absolute value. The argument applies at prescribed $h$ and for complex $z$.

**PROVED — comparison across the time seam.** A connected list with $\sum|X|<m/4$ uses a connected interval of fewer than $m/4$ time blocks, allowing cyclic adjacency. Its bridge moments and its incompatibilities agree with their lift to an ordinary time interval. To see this for a list touching the prescribed seam, change all spatial endpoints and bridge paths on one side of the seam by the vertex gauge $h$ or its inverse. Haar measure at endpoints is invariant, each electric transition and bridge is equivariant under a common vertex gauge on its two ends, and every traced spatial plaquette is invariant. The seam moves to an unused block. These short terms are thus independent of $h$. On the circle of $2m$ blocks they occur twice as often as on the circle of $m$ blocks. For ordered connected lists this follows by choosing a lift of one marked label and following neighboring labels. The time interval has length less than $m/4$, so projection creates no additional adjacencies or identifications. There are two choices of lift with the same connected coefficient. Their factorials agree as well. Equivalently one may sum over all markings and divide by the number of occurrences. Only the long terms contribute to a difference of logarithms. This proves $|\log Z_{T,h}-\log Z_{T,1}|\le C Nm e^{-m/4}$ and $|\log Z_{2T,1}-2\log Z_{T,1}|\le C Nm e^{-m/4}$, also for complex $z$. The displayed branches are the connected logarithms, real at zero. If the right side is small enough, averaging $Z_{T,h}/Z_{T,1}$ over $h$ gives a number in the disk of radius $e^{C Nm e^{-m/4}}-1$ about one. Its log is bounded by a constant times $Nm e^{-m/4}$. Applying the same argument at $2T$ proves (22) for the physical projection.

**PROVED — thermal conclusion and analytic scale.** For real spatial coupling, with normalized transfer eigenvalues $1,r_1,r_2,\ldots$, one has $\sum_i r_i^{2T}\le\sum_i r_i^T$ including the vacuum. Hence
$$
 1+S(T;n^3)\le Z_T(s)^2/Z_{2T}(s).
$$
On physical cylinders $m$ is of order $T/(1+\beta)$ and dominates $\log N$, giving the thermal conclusion of (22), also at $T=n/2$ on the seed grid. Taken together, (21) and (22) put the nearest zero of the *ordinary projected* $Z_T(z)$ at distance between $c/(1+\beta)$ and $C/\beta$. All constants are cutoff independent. The spatial coupling required by (W) is $s=\beta$.


**PROVED.** Cancel the two ordinary free energies before expanding. Put $J(z)=2\log Z_T(z)-\log Z_{2T}(z)$ using (22), and let $P_p$ denote its Taylor polynomial at zero of order $p$. Cauchy's estimate on the circle of radius $c/[2(1+\beta)]$ gives
$$
 |P_p(\beta)|\le C N m e^{-m/4}
       \sum_{q=0}^p[2\beta(1+\beta)/c]^q.                              \tag{23}
$$
Thus even orders growing with the cutoff return zero in the physical limit if $p\log[2\beta(1+\beta)/c]\le m/8$. This controls only the Taylor polynomial at the isotropic point. A remainder estimate would carry the entire inference to a physical seed. For an explicit test of that inference, take the two-level positive transfer with eigenvalues $1$ and $\exp[-1/b_\beta+(1/b_\beta-1/T)z/\beta]$. It has the same form of a positive electric transfer tilted by a bounded diagonal observable on the real segment. Near zero its impurity $J$ is $O(e^{-T/(2b_\beta)})$ on $|z|\le c/(1+\beta)$ for large $\beta,T$. Yet at $z=\beta$ its excited sum at time $T$ is $e^{-1}$. This tests an inference from endpoint smallness and small Taylor terms. It is an abstract transfer example. Equation (21) proves the separate zero obstruction in the Wilson integral itself.

## 8. A real reorganization of the electric expansion

**PROVED.** To bypass the complex zero, try a positive reference on each time block, with arbitrary endpoint factors and with corrections from individual link histories or from proper subsets of a plaquette. Let $H$ now denote the block duration. Keeping the product electric endpoint density within a fixed sup-norm error $\epsilon<1$ of Haar requires $H\ge c_\epsilon\beta$ at large $\beta$. Indeed the normalized fundamental trace has expectation $r_\beta^H$ starting at identity, and zero under Haar. The sup-norm bound implies $r_\beta^H\le\epsilon$. Use $r_\beta\ge1-C/\beta$ from (21).

**PROVED.** Fix one spatial plaquette with its four distinct edge histories. Even allowing arbitrary functions of *all* block endpoints, plus sums of arbitrary functions each missing at least one of the four interior histories, the best uniform additive error in its log weight $s\sum_{t=0}^{H-1} w_p(U_t)$ is at least $|s|(H-1)$.
Fix all endpoints to identity. On each of the four edges hold its path equal to an independently chosen central sign $\epsilon_i$ throughout the $H-1$ interior times. The fourth Walsh coefficient, obtained by averaging against $\prod_i\epsilon_i$ on the sixteen sign choices, is $s(H-1)$. Every allowed additive approximant has coefficient zero by summing one missing sign. A Walsh coefficient is bounded by the sup norm. All other plaquette terms also have zero fourth coefficient on this family. For a continuous residual at these fixed endpoints, full support of the electric bridges gives the same conditional essential supremum. This rules out uniform small log activities at $s=\beta$ in this class. It includes products of independent spatial blocks of complete histories with an uncovered plaquette. If every plaquette were internal to some block of a disjoint partition of the edges, its four edges would all be in the same block. Neighboring plaquettes sharing edges then force the entire connected spatial lattice into one block.

**PROVED.** There is also an obstruction *in the electric path law*. Use four independent stationary electric chains in one block, Haar at the initial time. For $H\ge A_0(1+\beta)$ with an absolute sufficiently large $A_0$ and $\beta\ge1$, the $L^2$ error of every additive approximation of the preceding kind is at least $c|s|\sqrt{H\beta}$. Here endpoint factors and arbitrary proper-subset history factors may all depend on the four endpoints at both times. To prove this let $Y_p=\sum_{t=0}^{H-1}w_p(U_t)$. The electric product transition sends the fundamental plaquette to $r_\beta^4$ times itself. Thus
$$
 \|Y_p\|_2^2=\tfrac14\sum_{t,u=0}^{H-1}r_\beta^{4|t-u|}
                 \ge c_0 H\beta.
$$
For the inequality sum over pairs with $|t-u|\le c_1\beta$ as in (21). On a compact range of $\beta\ge1$ the diagonal suffices, with an adjusted constant.

**PROVED.** For each oriented matrix factor $U_i(t)^{\pm1}$ in the plaquette, subtract its own conditional mean given its two endpoints. Insert the four centered factors in the same trace and sum over time to define $Y_p^\circ$. Conditional on endpoints the four bridges are independent. Each summand is centered in each path separately, so $Y_p^\circ$ is orthogonal to all the allowed approximants. Expanding the four factors shows $Y_p-Y_p^\circ$ itself is a sum of allowed terms. For a single link with endpoints $u,v$, the intermediate density is $D_t(u,g)D_{H-t}(g,v)/D_H(u,v)$ at $0<t<H$. Formula (2), and the trivial bound one on the mean of a unit quaternion, give
$$
 \|\mathbb E[U_i(t)^{\pm1}\mid u,v]\|_{\rm op}
       \le C\exp[-\min(t,H-t)/b_\beta]
$$
uniformly when $H/b_\beta$ is sufficiently large. For the middle times, subtract the constant one in the numerator before integrating the fundamental matrix against Haar, and use $D_H\ge1/2$. For times within a fixed multiple of $b_\beta$ of an end, increase $C$. The bound covers $t=0$ as well. Telescoping the four-factor difference, whose centered factors have norm at most two, and summing the geometric series at both ends give $\|Y_p-Y_p^\circ\|_\infty\le C' b_\beta$. Taking $A_0$ large enough proves $\|Y_p^\circ\|_2\ge\frac12\sqrt{c_0H\beta}$. Multiplying by $|s|$ gives the assertion. This is an error in the log weight under the stated reference law. At isotropic coupling it is large even in mean square. A genuinely interacting reference with the four histories treated jointly lies outside this obstruction.

**OPEN.** A real continuation that retains those joint magnetic interactions requires a uniform estimate on the thermal free-energy difference as $s$ runs past $c/(1+\beta)$ to $\beta$. Row 863 calls the corresponding plaquette-response bound (SHIFT). The physical obstruction (20), the zero bound (21) and the history estimates delimit three ways to try that continuation. None supplies (SHIFT).


## 9. Testing continuation on the thermal ratio itself

**PROVED, given the named UV witness.** There is an actual Wilson test of the Taylor remainder in (23). Use the cylinder floor of row 865, *gap-sdcyl-ca-astra*, Proposition W-phys-CA, checked in *gap-sdcyl-ca-check-opus*. Its hypotheses are the account's reference-witness and source-transfer estimates with their coupling and depth admissions. CA-I, lines 2715–2781, uses the reference lattice kernel, $\zeta'_{K-s}\in[2/3,4/3]$, and a half-error. Keep that kernel. On a fixed spatial cube of physical side $L$ a multiple of its admitted $\ell_\star^{\rm CA}$, take $T=n/2$, $t=a_jT=L/2\ge2d$ for its fixed witness separation $d$. That previous proposition supplies
$$
 S_{\rm even}(T;n^3)\ge \rho_{\rm CA}^{\,2t/(3d)},\qquad
       \rho_{\rm CA}=c_{\mathcal K}/(3C_{\mathcal K})>0 .
$$
Hence $J(\beta)\ge\log(1+\rho_{\rm CA}^{\,2t/(3d)})=:j_L>0$ at the isotropic endpoint. This reuses the previous even-sector result. It gives a lower bound on the *error* of transporting the electric Taylor polynomial. For every order sequence in (23), $|J(\beta)-P_p(\beta)|\ge j_L-o(1)$. The witness floor may be much smaller than the seed threshold at large $L$.

**PROVED under the same witness.** Even after all common zeros are canceled, the meromorphic thermal ratio $Z_T(z)^2/Z_{2T}(z)$ has an uncanceled zero or pole within $|z|\le\beta(1+m^{-1/2})$ for all sufficiently fine cutoffs on these cubes. This assertion concerns the Taylor disk centered at the electric endpoint. It localizes a modulus, without asserting proximity to the positive real segment.

**PROVED.** Suppose there were no such zero or pole. Set $\epsilon=m^{-1/2}$ and extend the logarithm $J$, real at zero, to $|z|<\beta(1+\epsilon)$. There is a growth bound for this logarithm even when the two ordinary partition functions have common zeros. For $k=T,2T$, the functions $V_k(z)=Z_k(z)/Z_k(0)$ satisfy $V_k(0)=1$ and $\log^+|V_k(z)|\le 3Nk|z|$. The circle mean of $\log|V_k|$ is nonnegative. Indeed, factor out its zeros inside the circle and use the harmonic mean-value property on the remaining logarithm. Each zero at $b$ contributes $\log(r/|b|)$ at radius $r$. Thus the mean of $|\log|V_k||$ is at most $6Nk r$. Take a radius $r\in[\beta(1+3\epsilon/4),\beta(1+7\epsilon/8)]$ avoiding the zeros on the boundary. The circle mean of $|\operatorname{Re}J|$ is $O(1+NT r)$. The analytic Poisson formula for a holomorphic function real at the origin, with kernel $(re^{i\theta}+z)/(re^{i\theta}-z)$, gives
$$
 \max_{|z|\le\beta(1+\epsilon/2)} |J(z)|
                   \le C(1+NT\beta)/\epsilon .
$$
The log of this upper bound is $O(\log n)$ along the physical sequence. On the inner circle of radius $c/[2(1+\beta)]$, (22) gives $|J|\le e^{-m/5}$ eventually. Interpolate the two log maxima at radius $\beta$ by applying the maximum principle to $\log|J(z)|$ minus the affine function of $\log|z|$ through the two bounds. The inner-circle weight is
$$
 \frac{\log(1+\epsilon/2)}
      {\log[2\beta(1+\epsilon/2)(1+\beta)/c]}
 \ge c'\epsilon/(1+\log\beta).
$$
Consequently $\log|J(\beta)|\le O(\log n)-c''\sqrt m/(1+\log\beta)\to-\infty$. Here $n$ grows exponentially in the RG depth, $\beta=O(\log n)$, and $m$ is of order $n/(1+\beta)$. This contradicts the fixed positive $j_L$. The analytic branch on the real segment equals the real logarithm there since the partition functions are positive. This proves the assertion.

**PROVED under the same witness.** The invariant required from a real continuation can be written without complex variables. Let $\bar w_k(s)$ be the mean normalized trace averaged over all $3Nk$ spatial plaquettes of the cylinder of time period $k$. Differentiating the finite integral gives
$$
           J'(s)=6NT[\bar w_T(s)-\bar w_{2T}(s)].
$$
Equation (22) and the physical lower bound $j_L$ force the integral of $J'$ from $c/(1+\beta)$ to $\beta$ to be at least $j_L-o(1)$. In particular, $\sup_{s_0\le s\le\beta}J'(s)\ge (j_L-o(1))/(\beta-s_0)$ for $s_0=c/(1+\beta)$. A uniform $o(1/\beta)$ upper estimate on this derivative would contradict the witness. (W) needs an *upper* bound on the integral at a sufficiently large physical size. The lower bound leaves room for that.

**PROVED.** A time rescaling alone cannot take the proven strip to the isotropic bare coupling. In the quadratic continuum action write the two coefficients as $\beta$ for $\sum_i|F_{0i}|^2$ and $s$ for $\sum_{i<j}|F_{ij}|^2$. Under $t'=u t$, the one-form convention gives $F_{0i}=u F_{0'i}$ and $dt=dt'/u$. The coefficients become $u\beta$ and $s/u$. Their product is invariant, so their common value after isotropization is $\sqrt{\beta s}$. This value is bounded on the strip (22) and tends to infinity on $s=\beta\to\infty$. At finite cutoff the account's *exact* dilation, outline 6863–6869, keeps the bare weights fixed. A flow changing the effective action would need a separate estimate.


## 10. Consequences for the wall and the remaining real integral

**PROVED.** On the isotropic trajectory the unprojected operator of §5 gives the same two functions in (W). Use its symmetric-cube thermodynamic limit for the bulk pressure. At every fixed $\beta$, (17) with $T=n\to\infty$ shows that its log partition function differs from the projected one by $o(1)$, so their bulk pressures agree. At a fixed physical $L$ their excesses again differ by $o(1)$ by (17). The unprojected vacuum is the projected vacuum by positivity and simplicity. Every extra unprojected excitation has lattice energy at least $1/(7b_\beta)$ by (18). Since $n_j/b_{\beta_j}\to\infty$, adjoining these excitations preserves $\liminf_j n_j\log(\lambda_0/\lambda_1)$, including when that liminf is infinite. This is a lossless reformulation at physical size. The comparison with the free electric kernel in (19) does not retain that normalization.

**PROVED.** For the anisotropic strip the lower bound on the *whole physical* lattice gap is $1/(4H)$, uniform in spatial volume. At fixed box use $e^{-T m_{\rm lat}}\le S(T)\le \exp(CNm e^{-m/4})-1$ from (22), then take $T$-th roots and $T\to\infty$. The same proof works on rectangular spatial boxes of sides at least four, with $N$ their site count. Only the four plaquettes per spatial link and the six neighbors of a vertex were used. In particular, for an absolute sufficiently large $C_1$, $N\le\exp(T/(C_1\beta))$ implies $S(T)\le 1/1650$ on $0\le s\le c/(1+\beta)$, $\beta\ge1$. Indeed $H\le H_0\beta$ for an absolute $H_0$. Choose $C_1$ so that $\log N\le(m+1)/16$ and $m$ is sufficiently large, using $N\ge4^3$ for the latter. Then $CNm e^{-m/4}\le C'm e^{-3m/16}$ can be made smaller than $\log(1+1/1650)$. This proves the thermal clause (ii) of row 863's proposed (KS-ZONE), after decreasing its product constant. The spectral bound here has coefficient $1/(4H)$. Section 11 obtains the proposed spectral coefficient by inserting the gauge projection into every block.

**PROVED, using row 720.** For a size $L$ in its grid, take $n=L/a_j$, $N=n^3$, $T=n/2$, and $s_0=c/(1+\beta_j)$. In this notation it suffices to prove the following real inequality.
$$
 \limsup_j\,6NT\int_{s_0}^{\beta_j}
       [\bar w_T(s)-\bar w_{2T}(s)]\,ds < \log(1+1/1650)
           \quad\text{at one fixed }L.                                \tag{24}
$$
By (22) and the derivative identity in §9, the left side equals $\limsup_j J(\beta_j)$. For $S=S(T;n^3)$ the exact eigenvalue sums give $\log(1+S)\le J\le2\log(1+S)$. Thus (24) implies the thermal seed and hence (W). Conversely the downstream estimates in Theorem ZD-c from a seed give arbitrarily small $\limsup_j S$ on sufficiently large fixed dyadic cubes. At one such cube (24) holds with strict margin. This is the finite-period version of row 863's real interpolation, combined with row 720. The new estimates supply its initial interval and describe failures of continuation from that interval.

**OPEN.** Neither a uniform upper estimate for (24) at a large physical size nor a lower estimate excluding it at every size has been obtained. In particular (9) measures the required cancellation at fixed physical volume, and (15) measures the change of cylinder shape. Neither controls the sign or size of the residual magnetic response in (24). Equations (18)–(20) locate the failure of the charge and minimum-action comparisons. Equations (21)–(23) and §8 limit the analytic and real expansions about the seeded electric theory. Beyond these routes I have no Wilson estimate for the joint spatial plaquette histories that supplies (24). No numerical run was used.

## 11. The spectral coefficient after projection at every time block

**PROVED.** Write $d_\beta=-\log r_\beta$ with $r_\beta=I_2(\beta)/I_1(\beta)$. Fix $0<\alpha<4$. There are constants $A_\alpha,c_\alpha,C_\alpha>0$ independent of the periodic spatial box with sides at least four and $N$ sites. Take $H=\lceil A_\alpha b_\beta\rceil$ and $m=\lfloor T/H\rfloor\ge8$. For temporal coupling $\beta\ge1$ and complex spatial coupling $|z|\le c_\alpha/(1+\beta)$, the gauge-invariant traces have logarithms with
$$
 \left|2\log Z_T(z)-\log Z_{2T}(z)\right|
       \le C_\alpha N m\,e^{-\alpha d_\beta T}.
 \tag{25}
$$
Consequently the whole gauge-invariant lattice gap satisfies $m_{\rm lat}\ge\alpha d_\beta$ on the real strip. With $\alpha=2$, this gives clause (i) of row 863's (KS-ZONE). Together with the thermal estimate of §10 it proves both clauses for one common positive product constant. This strengthens (22) using the same electric expansion and its exact local gauge projection.

**PROVED.** The electric convolution after $l$ steps obeys $\|D_l-1\|_\infty\le\eta(l d_\beta)$. To see this, the successive Bessel ratios $R_k$ of §1 decrease with $k$. Near zero $R_{k+1}<R_k$ by their series. At a first equality at positive argument $x$, their Riccati equations give $(R_{k+1}-R_k)'=-2R_k/x<0$, which precludes first contact. Hence $I_d(\beta)/I_1(\beta)\le r_\beta^{d-1}$, and Fourier inversion as in (2) gives the bound. There are absolute $a,B>0$ with $a\le(1+\beta)d_\beta\le B$ for all $\beta\ge1$. The lower bound follows from (1), while $1-r_\beta=O(1/\beta)$ from (21) gives the upper bound at large $\beta$. Continuity and positivity give it on the remaining compact interval.

**PROVED.** Insert a separate vertex gauge average $P$ at the upper end of *every* block of §7. On the full spatial Hilbert space the electric convolution and magnetic multiplication commute with $P$, and $P^2=P$. Thus these insertions give exactly the original projected trace at each complex $z$. In the reference of §7 take independent Haar variables $h_{x,b}$ at every spatial vertex $x$ and block $b$, also independent of the Haar endpoints $u_b$. For block $b$ run each bridge from $u_b$ to $h_b\cdot u_{b+1}$. Magnetic insertions still exclude their upper endpoint. The variables $h_{x,b}$ enter only the factors and bridges of block $b$. For independence across disjoint components, join labels when their blocks are equal or adjacent and the spatial edges they use share a vertex. This graph contains all dependencies. Its closed neighborhood size is at most $D=1024$. Each label touches at most eight vertices, each vertex meets at most six edges, and each edge belongs to at most five labels per block. Only three blocks need be counted. The connected-set expansion and the counting proof of §7 apply on this larger graph.

**PROVED.** Call a block occupied by a polymer $X$ if it contains a label of $X$. In an occupied block with no magnetic label in $X$, let $E_b$ be the set of its electric labels, one per selected edge. All normalized bridges in that block integrate to one. If $E_b$ has a vertex $x$ of degree one, the only dependence on $h_{x,b}$ is through the single factor $D_l(u,h_{x,b}v h_{y,b}^{-1})-1$ or its reversed-edge version. Its Haar integral at $x$ vanishes since $D_l$ is a normalized convolution. This holds with all endpoints and all other blocks fixed. A nonempty set of fewer than four edges on the given spatial graph has a leaf, since the graph is simple and has no triangles. Thus in a nonzero activity every occupied block either contains a magnetic label or has at least four distinct electric labels.

**PROVED.** For a polymer put $L(X)=\sum_{b\ {\rm occupied}}l_b$, where $H\le l_b<2H$ is the length of that block. Choose $\sigma e^2\le1/(4D^3)$. Enlarge the modulus of each activity by $e^{\alpha d_\beta L(X)}$. On a block with only electric labels, distribute the block's exponential among four of them. Each of the four enlarged norms is at most $C e^{-(1-\alpha/4)d_\beta l_b}$ by the electric estimate and (2). Choose $A_\alpha$ so large that this is at most $\sigma$, uniformly for all $l_b$. All further electric labels have norm at most $\sigma$ as well. In a block with a magnetic label, assign the entire exponential to one such label. Its enlarged norm is at most
$$
             e^{2\alpha d_\beta H}\big(e^{2H|z|}-1\big).
$$
Both $d_\beta H$ and $H/(1+\beta)$ are bounded in terms of $A_\alpha$. Hence $c_\alpha>0$ can be chosen to make this expression at most $\sigma$. All remaining insertions obey the unweighted bound. It follows that $|z_X|e^{\alpha d_\beta L(X)}\le\sigma^{|X|}$, including the zero activities. Applying the same Kotecký–Preiss inequality as in §7 bounds the entire absolute connected log sum, weighted by $e^{\alpha d_\beta\sum_X L(X)}$ with repetitions counted, by $C Nm$. This also proves zero-freeness directly on the projected space for every such finite box.

**PROVED.** Repeat the schedule of $m$ blocks twice for $2T$. In the two log series cancel every connected list whose occupied blocks, taken modulo $m$, omit even one block. Cutting at an omitted block leaves a line of at most $m-1$ blocks. In the double period its preimage consists of two disjoint copies, with no graph adjacency between them. A connected list in the double period with this omission therefore lies in one copy. Conversely a list with the omission in the single period has two lifts. Endpoint, gauge and bridge measures agree on either lift. Each activity, every incompatibility and each factorial in the connected coefficient agrees as well. The two lifts can be distinguished by marking any one occurrence in the ordered list. Every term left over has $\sum_X L(X)\ge T$, since it meets every residue block. The weighted absolute log bound at $T$ and $2T$ now gives (25).

**PROVED.** At fixed $\beta,s,N$, take $T$-th roots of $e^{-T m_{\rm lat}}\le S(T)\le\exp(C_\alpha Nm e^{-\alpha d_\beta T})-1$ and send $T$ to infinity. This proves the spectral bound, uniformly in spatial volume. At $s=0$ its limiting coefficient $4$ is exact. In the electric Peter–Weyl basis the support of any nonconstant gauge-invariant spin network has no degree-one vertex, since a lone nontrivial incident representation has no invariant vector. At least four nontrivial edge factors are needed, each with multiplier at most $r_\beta$. A fundamental plaquette has eigenvalue $r_\beta^4$. At positive spatial coupling the case $\alpha=2$ therefore retains at least half of the electric gap. To express both clauses of (KS-ZONE) as in row 863, choose its product constant at most half the smaller of $c_2$ here and the strip constant in §10. Then $s\beta\le c_0$ implies both strip hypotheses for $\beta\ge1$.

**OPEN.** The projection removes the one-, two- and three-edge contributions in a purely electric block. A single spatial plaquette insertion is already gauge invariant and survives the same projection. Its joint four-history contribution and the obstruction to absorbing it in proper subsets are the ones quantified in §8. At the isotropic coupling, (21) still bounds the radius of a log expansion about zero and (24) still requires the upper bound on the real magnetic response.

## 12. Real-coupling tests for two further continuations

**PROVED.** The connected series used for (25) has an obstruction on the *positive real* axis as an absolutely summed series, even after cancellation of the short time clusters. Take the schedule with $m\ge8$ and $H$ from §11 at $\alpha=2$. Let $A$ be the single magnetic label of a fixed plaquette $p$ in a block of length $l$, and write $Y_p=\sum_{t=0}^{l-1}w_p(U_t)$. Its activity at real $s$ satisfies
$$
             z_A(s)=\mathbb E_{\rm ref}e^{sY_p}-1
                         \ \ge\ c s^2 l\beta .
 \tag{26}
$$
Indeed, on these four edges the reference chooses independent Haar endpoints and independent electric bridges between them. Conditional on the gauge $h_b$, its action on the upper endpoints preserves their joint Haar law. Relative to four stationary independent electric chains, the reference path law has density $\prod_{e\subset p}D_l(u_e,v_e)^{-1}$ at the endpoints after that action. Each $D_l\le2$ by §11. The stationary second moment of $Y_p$ is $\frac14\sum_{t,u}r_\beta^{4|t-u|}\ge c l\beta$, as in §8. The second moment under the reference is at least $2^{-4}$ times that. Changing the sign of one entire edge path and its two endpoints preserves the reference and reverses $Y_p$. Thus $\mathbb E_{\rm ref}e^{sY_p}=\mathbb E_{\rm ref}\cosh(sY_p)\ge1+s^2\mathbb E_{\rm ref}Y_p^2/2$, proving (26).

**PROVED.** Consider also the one polymer $B$ containing the four *electric* labels on those same edges in every block around the time circle. It is connected and $z_B\ge r_\beta^{4T}>0$. To verify this, integrate all its endpoint and gauge variables. The resulting trace on the four-edge Hilbert space is that of the projection onto vertex invariants times the product, over blocks, of the four-link tensor convolutions $\bigotimes_{e\subset p}(C_\beta^{l_b}-P_e)$. Here $C_\beta$ is the normalized one-link electric convolution, and $P_e$ is projection to constants on edge $e$. This follows directly from the kernels $D_{l_b}-1$ and the independent vertex averages. The convolutions and the total gauge projector commute. The product is positive, and the gauge-invariant plaquette trace is its eigenfunction of eigenvalue $r_\beta^{4T}$.

**PROVED.** The labels of $A$ and $B$ are incompatible. In the connected logarithm the terms with one copy of $B$ and $k$ copies of $A$ contribute $(-1)^k z_B z_A^k$, including all orderings. This coefficient follows by giving the two activities separate formal markers $u,v$. With just those two polymers retained the gas has partition function $1+u z_A+v z_B$, whose log has the stated coefficient of $u^k v$. All these lists meet every time block by way of $B$. Therefore canceling terms which omit a time block, as in (25), leaves an absolute subseries $\sum_{k\ge0} z_B |z_A|^k$ on the single-period side. Since $l\ge A_2 b_\beta$, this diverges when $s\beta\ge C$ by (26), in particular at $s=\beta$ on fine physical cylinders. This tests the actual activities after gauge projection. Summing this family formally at positive coupling would give $z_B/(1+z_A)$. The obstruction is to absolute summation in the specified activities. It leaves room for different groupings.

**PROVED, given the UV witness of §9.** Another possible grouping is to absorb *all* joint magnetic histories of a slab into its exact boundary transfer, normalize by the vacuum, and restart with one effective boundary state on blocks of order $\beta$. There is a spectral obstruction in the interacting theory itself. Write $U_j=\mathsf T_j/\lambda_{0,j}$ on the entire gauge-invariant spatial box of an admitted fixed physical size, at isotropic coupling. Row 865's W-phys-CA, lines 218–242 of `gap-sdcyl-ca-astra.md`, gives an even excited state with lattice energy at most $a_j M_{\mathcal K}$, where $M_{\mathcal K}=2\log(3C_{\mathcal K}/c_{\mathcal K})/(3d)$. Therefore, for every integer $h\ge1$,
$$
       \inf_{\operatorname{rank} R\le 1}\| U_j^h-R\|_{\rm op}
                     \ \ge\ e^{-a_j M_{\mathcal K}h}.
 \tag{27}
$$
Indeed the span of the vacuum and this excited state contains a unit vector annihilated by $R$. On that span $U_j^h$ has smallest singular value at least the displayed exponential. The choice $R=0$ gives a matching limiting upper bound one when $a_jh\to0$. This estimate is unchanged under the unitary ground-state transform to the stationary slice Hilbert space. It also applies in the even sector alone.

**PROVED under that witness.** For the seeded strip (25), the vacuum projector approximates the normalized $H$-step transfer with operator error at most $e^{-2d_\beta H}$, uniformly below one. At the isotropic endpoint (27) forces the best rank-one error to tend to one on blocks with $H=O(1+\beta_j)$. More generally any bound by a fixed $q<1$ on that error requires $h\ge\log(1/q)/(a_j M_{\mathcal K})$ on the admitted physical cubes. Thus exact integration throughout a slab still cannot transport the strip's time scale to that endpoint with a uniform contraction. A transfer retaining two or more effective states must estimate the splitting *within* the retained even sector. The witness supplies an upper bound on this splitting. The lower bound and thermal multiplicity needed in (24) remain open.

**PROVED under that witness.** There is a quantitative loss for any direct real comparison of even gaps. On the same admitted spatial box let $m_{\rm ev}(s)$ denote the first excited even-sector lattice energy at spatial coupling $s$, with temporal coupling $\beta_j$ fixed. If a comparison gives $m_{\rm ev}(\beta_j)\ge m_{\rm ev}(s_0)/K_j$ starting at $s_0=c_2/(1+\beta_j)$, then (25) and the cited upper even gap give
$$
 K_j\ge \frac{2d_{\beta_j}}{a_j M_{\mathcal K}}
             \ge \frac{c}{a_j(1+\beta_j)} .
 \tag{28}
$$
This grows faster than every fixed polynomial in $\beta_j$ by the first-passage relation. At each finite cutoff the ordered even-sector eigenvalues and the simple vacuum eigenvalue are continuous in real $s$, since the transfer varies in operator norm and the min–max principle applies. The first excited eigenvalue is positive throughout by strict positivity of the quadratic form of the electric convolution. Hence every sequence of energy scales $\epsilon_j$ with $a_j/\epsilon_j\to0$ and $(1+\beta_j)\epsilon_j\to0$ is attained as $m_{\rm ev}(s_j)=\epsilon_j$ somewhere between $s_0$ and $\beta_j$, for sufficiently large $j$. The estimates give no location for these couplings. A comparison losing the factor in (28) can still be compatible with a positive physical mass. What it would need to control is the resulting finite physical coefficient and the thermal multiplicity at one large size. I have no estimate of those quantities beyond (24).

RESULT — PROVED. With temporal coupling $\beta\ge1$ and spatial coupling $0\le s\le c/(1+\beta)$, anisotropic Wilson SU(2) has a thermal seed on physical cylinders and a lattice gap at least $2\log[I_1(\beta)/I_2(\beta)]$, uniformly in spatial volume. This proves both clauses proposed in row 863's (KS-ZONE). The nearest complex zero of the projected partition function is at distance $\Theta(1/\beta)$ from $s=0$ on those cylinders as $\beta\to\infty$. Equation (28) gives the necessary loss in a real gap comparison under the stated UV witness. OPEN. At the isotropic point $s=\beta$, the upper bound (24), wall (W) and the Jaffe–Witten mass gap remain open. Independent review is pending.
