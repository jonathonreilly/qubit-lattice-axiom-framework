## Repo search

**GUIDE.** Row 1236, pinned checkout `b71c9f52a`. The target-specific prior note is absent. The target is a nontrivial continuum four-dimensional SU(2) Yang–Mills theory with a positive lower spectral bound above its vacuum, in the Jaffe–Witten sense.

**GUIDE.** The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141, principally on ultraviolet questions. I checked the mass-gap passages identified by row 1218. The soft-route local-block note on PR 10114 gives a one-step plaquette witness and contraction at bare parameter at most $1/32$. Grok's crossover note on PR 10133 leaves both crossover and source transport open. PR 10134's `mass-gap-interface.md` distinguishes an excited sector, a gap and identification of the theory. The single-scale lift on PR 10141 bounds a constrained classical field. The closest main result is Theorem ZD-c, which relates a thermal bound to the finite-volume gap and a state count. None of these passages estimates the neutral spectrum at a fixed physical size along the weak-coupling tuning. [Lead's search](prior/repo-search-2026-11-08.md) · [Primary passages and revisions](prior/gap-onebound-read-sol.md) · [Main, Theorem ZD-c](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/research/mass-gap/library/gap-phys-seed.md#L311-L329)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the one-link convolution and gauge-projected transfer in GL3 and GL8. Outline lines 581–599 and 31860–31882 distinguish the action-density sector and a positive lower spectral edge. CA-I lines 2704–2712 and 3213–3222 leave the gap outside the asserted result. These are bounded source reads at `31a47c543775` from the outline index, its neighbouring rows and obligations. CA-I items 4.12–4.19 concern ultraviolet induction. [Index](sa-index/README.md) · [One-link kernel](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197-L2224) · [Transfer](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [Account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Row 1218 describes a sufficient full thermal estimate of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy, a cube-update criterion of the first four authors, and common-rate criteria of Zeng Chunping. I use their distinction between a physical transfer gap, a thermal sum and an auxiliary relaxation estimate. Their new papers have the reading limits recorded in row 1218. Row 1231, (42), leaves the thermal weight outside the observed neutral subspace uncontrolled. Row 1145, (16)–(18), already bounds every *static gauge charge* of the actual transfer. I use this last bound as an input. [Published-work reading](prior/gap-onebound-read-sol.md) · [Neutral complement](gap-solve26-astra62.md) · [Static charges](gap-solve2-astra62.md)

## Can the static-charge estimate control a physical singlet?

**GUIDE.** I will differentiate a neutral eigenfunction on a spatial link. Its derivative carries an adjoint charge at the initial vertex. The convolution commutes with that derivative. The magnetic action supplies an explicit force, so the charged resolvent can be used in the equation for a genuinely neutral eigenfunction. The registry has no matching owner for this estimate. The test is whether the vacuum-normalized force term allows a bound uniform in the spatial cube and cutoff.

**OPEN.** With $a_j\downarrow0$, $n_j=L/a_j$ and $\beta_j\to\infty$, the one-cube route needs the sum of the excited neutral eigenvalues of the vacuum-normalized transfer to the power $\lfloor n_j/K\rfloor$ to be at most $1/2$ at one admissible physical side $L$, with $K$ fixed first, for all sufficiently fine cutoffs. The alternative on a matched infinite-volume continuum state needs a common positive spectral edge on a total observable domain. The construction and full Yang–Mills identification are also required. [Neutral seed](gap-mini-branch-fable.md) · [Continuum scope](gap-en-check-astra.md)

## An exact force identity for slow singlet states

**GUIDE.** Use a periodic spatial cube of side $n\ge3$ in lattice units. The slice variable $X$ consists of its positively oriented links, with product probability Haar. Write $w(q)=\operatorname{Re}q=\operatorname{tr}(q)/2$ for unit quaternions and set
\[
 S(X)=\beta\sum_{p\ \mathrm{spatial}}(1-w(X_p)),\quad
 M=e^{-S/2},\qquad F=MCM/\lambda_0 .
\]
Here $C$ is the product of the one-link electric convolutions normalized to have mass one, and $\lambda_0$ is the Perron eigenvalue of $MCM$ before vertex projection. This kernel is smooth and strictly positive at finite $\beta>0$. Its top eigenfunction $\psi$, normalized in Haar $L^2$, is strictly positive and invariant under vertex gauges and spatial centre flips. The magnetic and electric factors commute with these symmetries. Thus the physical transfer is the restriction to invariant functions. We keep the larger operator when evolving a colour vector. This is the Osterwalder–Seiler and Lüscher transfer in a symmetric placement of the magnetic factor.

**PROVED.** At a link $e$ based at $x$, let $D^a_e$ differentiate $X_e\mapsto\exp(t\,a)X_e$ for $a$ in an orthonormal imaginary quaternion basis. Write $D_e$ for the three-component gradient and $J_e=D_eS$. For a gauge-invariant scalar $u$, $D_eu$ and $J_eu$ transform as adjoint vectors at $x$. Let $F_x$ denote $F$ acting componentwise on those equivariant functions in Haar $L^2$. Put $b=1+6\beta$, $q=\exp(-2/b)$. Then $\|F_x\|\le q$. To see the single-site constant, insert one temporal gauge matrix per vertex in a step between fixed spatial slices. The electric Boltzmann factor is a product over spatial edges. Holding all other temporal matrices fixed, the matrix at $x$ has a translated one-link density of tilt length at most $6\beta$. Its conditional adjoint mean has norm at most $q$ by row 1145 (1), with representation dimension three. Averaging the others preserves the bound. Equivariance allows the insertion of all these gauge matrices against Haar by changing the outgoing slice variables. Consequently $|F_x v|\le q F|v|$ pointwise for every equivariant $v$. On the right $|v|$ is invariant. Taking the Haar norm gives the claim since $\|F\|=1$. Iteration also gives $|F_x^s v|\le q^s F^s|v|$. This is the single-charge case of the earlier argument. [One-link bound and static charges](gap-solve2-astra62.md)

**PROVED.** Let $F\phi=r\phi$ in the scalar gauge-invariant space, $q<r\le1$. Then
\[
 D_e\phi=-K_r J_e\phi,\qquad
 K_r=\frac12(r+F_x)(r-F_x)^{-1}
     =\frac12 I+\sum_{s\ge1}r^{-s}F_x^s .                                      \tag{1}
\]
The kernel smooths, hence $\phi$ is smooth. Left translations on any one link commute with $C$ because the convolution is central. Differentiating the two magnetic factors gives
\[
 D_e(F\phi)=F_xD_e\phi-\tfrac12\{J_e F\phi+F_x(J_e\phi)\}.
\]
The inverse in (1) exists by the single-charge bound and its series converges in norm. In a term of length $s$ the three-vector at the far endpoint is transported back on the temporal line through $x$. The half weight belongs only to $s=0$.

**PROVED.** For two such states $\phi_i,\phi_j$ with eigenvalues $r_i,r_j$, respectively, and $B_e=\sum_a(D^a_e)^2 S$, one has the exact sesquilinear identity
\[
 \langle\phi_i,B_e\phi_j\rangle
   =\langle J_e\phi_i,(K_{r_i}+K_{r_j})J_e\phi_j\rangle,\qquad
 B_e=3\beta\sum_{p\ni e,\ p\ \mathrm{spatial}} w(X_p).                         \tag{2}
\]
Each $D^a_e$ is skew-adjoint in Haar measure. Integrating its derivative of $(D^a_e S)\overline{\phi_i}\phi_j$ gives (2) after using (1) on both states. There are four spatial plaquettes through $e$. In each, differentiating the link or its inverse twice in one unit direction multiplies its trace by $-1$. Thus $|B_e|\le12\beta$. The operator $F_x$ is positive, by positivity of the central convolution and the magnetic sandwich, so $K_r\ge I/2$. In particular $\|J_e\phi\|^2\le 12\beta\|\phi\|^2$ for every eigenvector in this band. This bound applies to each such eigenspace, including the vacuum, at every spatial size.

## Controlling the estimate on an entire spectral subspace

**PROVED.** For $\beta\ge1$ there is an absolute $C$ independent of $n$ such that
\[
 \|(D_e+J_e/2) F\|\le C\sqrt\beta,\qquad
 \|J_eF\|+\|D_eF\|\le C\sqrt\beta .                                          \tag{3}
\]
These are operator norms from scalar Haar $L^2$ to the three-component Haar space. In temporal gauge write $w=\operatorname{Re}(X_eY_e^{-1})$, $A=1-w$. Differentiating the electric kernel at $X_e$ produces a three-vector of length $\beta\sqrt{1-w^2}\le\beta\sqrt{2A}$. For any $u\ge0$, $\sqrt u\,e^{-u/2}$ is bounded. Hence the absolute differentiated kernel is dominated by $C\sqrt\beta$ times the original kernel with just this electric coupling halved, retaining the old one-link normalizer. The latter operator has norm at most $C$ in the original vacuum normalization. Here are the details. For normalized electric convolution at coupling $v$, its spin-$l$ multiplier is $I_{2l+1}(v)/I_1(v)$, increasing in $v$ for $l>0$. Row 1149 (16) proves this by writing each consecutive ratio as a tilted mean with derivative a variance and multiplying the ratios. Thus replacing one normalized electric factor by its half-coupling version decreases the positive product in operator order, including after the magnetic sandwich. The ratio of the required normalizers is bounded. Indeed $z_v=\int e^{-v(1-\operatorname{Re}g)}dg$ is between $c(1+v)^{-3/2}$ and $C(1+v)^{-3/2}$ by the Haar density $\sin^2\theta\,d\theta$, restricting to $\theta\le(1+v)^{-1/2}$ below and using $1-\cos\theta\ge2\theta^2/\pi^2$ above. Domination on absolute values now proves the first estimate. [One-link ordering](gap-solve4-astra62.md)

**PROVED.** For $u=Fv$ integration by parts gives
\[
 \|J_e u\|^2=\langle u,B_eu\rangle+
       2\operatorname{Re}\langle(D_e+J_e/2)u,J_eu\rangle .
\]
Use $|B_e|\le12\beta$, $\|F\|=1$, and the first estimate in (3). Solving the quadratic inequality in $\|J_eu\|$ proves the second estimate, including the bound on $D_eF$ by subtraction. Thus (3) holds for arbitrary superpositions. On the spectral projection of $F$ onto $[r_*,1]$, $r_*>0$, the corresponding norms of $J_e$ and $D_e$ are at most $C\sqrt\beta/r_*$. This conclusion does not count eigenvectors.

**PROVED.** For a normalized singlet eigenfunction $\phi$ with $r>q$, (1) and (3) give, for $0<d\le r/2$,
\[
 \big\|\mathbf1_{[r-d,r]}(F_x)J_e\phi\big\|^2
                         \le C\beta d^2/r^4 .                                \tag{4}
\]
Indeed $(D_e+J_e/2)\phi=-F_x(r-F_x)^{-1}J_e\phi$. On that spectral interval $\lambda/(r-\lambda)\ge r/(2d)$ wherever it meets the spectrum. Estimate (3) applied through $\phi=F\phi/r$ proves (4). The magnetic force has a quadratic suppression in squared norm near a possible charged eigenvalue at the scalar eigenvalue. This gives a constraint on the actual transition matrix elements in addition to the static-charge threshold.

## Eliminating the charged time interval for a local insertion

**PROVED.** Use $U$ for $F$ restricted to gauge singlets, optionally also centre neutral. Take a smooth bounded real three-vector $v(X)$ transforming in the adjoint at the base of $e$, centre even when that restriction is used. Let $V$ be multiplication by $v$ from the scalar to the vector space and let $G=\sum_aD_e^av^a$ act by multiplication. For $R\ge0$, $m=R+1$, the following formula holds as an operator between scalar states:
\[
\begin{split}
 U^m G U^m={}& U^m(v\cdot J_e)U^m\\
 &+\sum_{s=1}^R\{\, U^m V^*F_x^s J_e U^{m-s}
                 + U^{m-s}J_e^*F_x^s V U^m\,\}+\mathcal E_{e,R},\\
 \|\mathcal E_{e,R}\| &\le 2C\sqrt\beta\,q^R\,\|V U^m\| .                    \tag{5}
\end{split}
\]
In this formula $J_e$ also denotes multiplication from scalars to three-vectors. Define $A_e=(D_e+J_e/2)U$. Induction using the differentiated transfer gives
\[
 D_e U^m=-\tfrac12 J_e U^m-\sum_{s=1}^{m-1}F_x^sJ_e U^{m-s}
                            +F_x^{m-1}A_e .
\]
For $m=1$ this is the definition of $A_e$. Substitution into the formula for $D_e(U\,U^m)$ adds one term and advances the power at the endpoint. For smooth scalar $h,k$, integration of the derivative of $v^a\,\overline{U^mh}\,U^mk$ gives $U^m G U^m=-(D_e U^m)^*V U^m-(V U^m)^*D_eU^m$. The last terms in the preceding induction formula yield $\mathcal E_{e,R}=-A_e^*F_x^R VU^m-(VU^m)^*F_x^RA_e$. Equation (3) and $\|F_x^R\|\le q^R$ prove (5), which extends by continuity. In particular $v=J_e$ gives an error at most $C'\beta q^R$. No projection onto a bounded number of eigenstates is used.

**PROVED.** For an individual normalized Wilson plaquette trace $f=w(X_p)$, take one edge $e$ in its support and $v=-D_ef/3$. Then $G=f$, because $\sum_a(D_e^a)^2 f=-3f$. Also $|D_e f|\le1$. More generally, take a real gauge-invariant matrix coefficient polynomial $f$ of single spin $l>0$ in one of its links (the other link variables can enter jointly). The round-sphere Laplacian on that link has eigenvalue $-4l(l+1)$, so $v=-D_e f/[4l(l+1)]$ gives $G=f$. For the eigenvalue, realize spin $l$ as the symmetric tensor power of $2l$ fundamental spinors. On one fundamental factor the sum of squares is $-3I$. On a pair the mixed sum $\sum_a a\otimes a=I-2\,\mathrm{Swap}$ acts by $-I$ on symmetric tensors, as follows by multiplying the three imaginary quaternion matrices. The sum of squares on $d=2l$ symmetric factors is $-3d-d(d-1)=-d(d+2)$. Spin zero in every link gives a constant. Finite tensor products of single-link coefficients span a dense algebra on the compact slice by Peter–Weyl, or by Stone–Weierstrass for the quaternion coordinates followed by finite tensor-power decomposition. Gauge and centre averaging preserve the spin on every link and are norm contractions. Applying (5) term by term therefore covers each fixed polynomial in the physical algebra, including coupled loops.

**PROVED.** In the Euclidean integral, $V^*F_x^sJ_e$ places the two insertions at times $s$ apart and contracts their colours by the adjoint of the temporal parallel transport at $x$. This follows by the same changes of variables that insert the vertex averages in the one-step formula. Its spatial support as a spacetime observable is the support of $v$, the four spatial plaquettes of $J_e$ at the other time, and this one time line. If $\beta=O(\log n)$, $a=L/n$ and a precision $n^{-k}$ is prescribed, one may choose $R=\lceil(k+c)b\log n\rceil$ for a fixed sufficiently large $c$, even allowing polynomial prefactors in $n$. Then $a(R+1)\to0$. The operator error in (5) meets that precision for bounded $\|v\|_\infty$, or for a family with a specified polynomial bound by increasing $c$. A factor polynomial in $n$ from summing insertions can be included in that choice. The stated growth of $\beta$ follows on the account's first-passage data from $x_0-x_K\le B_\sharp K$, bounded $x_K$ and $a=b_0^{-K}$ at fixed blocking factor $b_0>1$. [Sussman–Alpoge, RF24–RF25](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20781-L20801)

**GUIDE.** Equation (5) is a time-dependent Haar integration-by-parts identity. The local Wilson loop equations go back to Makeenko and Migdal, with finite-lattice treatments by Sourav Chatterjee and Jafar Jafarov and the SU(2) reduction studied by Vladimir Kazakov and Zechuan Zheng. The local loop equation and its scope already appear in the repository. Here the endpoint remainder has an operator norm on the full physical space and decreases with the length of the time interval. [Earlier loop-equation work](gap-loop-eq-opus.md)

## Comparison with a pair of fundamental static charges

**GUIDE.** A neutral state can also be put directly into a sector with two static charges. This tests whether a spectral upper bound there would give the missing upper bound on neutral eigenvalues. Row 1143, (8), gives the open-line isometry and vacuum moment inequality. I use its one-link isometry on an entire spectral subspace. [Open-line transfer formula](gap-solve-astra62.md)

**PROVED.** For $e=(x,y)$ use the Hilbert space of matrix functions $A(gX)=g_x A(X)g_y^{-1}$ with fibre inner product $\operatorname{tr}(A^*B)/2$. Choose the three centre seams off $e$ and use their invariant sector. Multiplication $W_e f=X_e f$ is an isometry into that sector. Denote its transfer by $F_{xy}$ in the same vacuum units as $U$. The compression $W_e^*F_{xy}W_e$ is the scalar transfer with an extra factor $w(X_eY_e^{-1})$ in its electric kernel. This follows by taking the normalized matrix trace of $X_e^*Y_e$. Write $d=2l+1=1,2,\ldots$ for the dimension of one-link spin $l$. Its convolution multiplier is $c_d(\beta)=I_d(\beta)/I_1(\beta)$, and $p_\beta=\int w\,dC_\beta=I_2(\beta)/I_1(\beta)$. Differentiation of the probability kernel replaces it by $(w-p_\beta)dC_\beta$. The multipliers $c'_d$ are nonnegative by row 1149, (16). Consequently, as quadratic forms on the neutral space,
\[
 W_e^*F_{xy}W_e\succeq p_\beta U,\qquad r_{k,xy}\ge p_\beta r_{k,+}
                                  \quad (k=0,1,\ldots).                       \tag{6}
\]
Here the eigenvalues are in decreasing order with multiplicity and $r_{0,+}=1$. The eigenvalue comparison follows by using the isometric images of the first $k+1$ singlets in the min–max principle. In particular $\operatorname{Tr}F_{xy}^t\ge p_\beta^t\operatorname{Tr}U^t$ for positive integer $t$. [One-link multiplier order](gap-solve4-astra62.md)

**PROVED.** There is an exact expression for the excess in (6). Set $Y=C^{1/2}M/\sqrt{\lambda_0}$, $\widetilde F=YY^*$ and $H_\beta(d)=\partial_\beta\log c_d(\beta)$. For every neutral $f$,
\[
 \langle W_e f,F_{xy}W_e f\rangle-p_\beta\langle f,Uf\rangle
       =\langle Yf,H_\beta(d_e)\,Yf\rangle .                                  \tag{7}
\]
Indeed $U=Y^*Y$ on that space and the electric factor on $e$ is diagonal in $d_e$. The form on the right is defined by its nonnegative spin sum, which is finite by the bounded differentiated kernel. The identity $\widetilde F Y=YU$ transports any $U$-band away from zero into the same band of $\widetilde F$. Its norm after transport is $\|Yf\|^2=\langle f,Uf\rangle$.

**PROVED (electric spin in every high transfer state).** For an even spatial side $n\ge4$, let $P_D$ be the projection on $d_e\le D$ at a single electric cut. With $z_\beta=\int e^{-\beta(1-w)}\,dU$ there is a constant $C$ independent of the side, the link and $\beta\ge 84$ such that
\[
 \|P_D{\bf1}_{[h,1]}(\widetilde F)\|^2
       \le C h^{-2} z_\beta\sum_{d\le D}d^2,\qquad 0<h\le1,                 \tag{8}
\]
in the gauge-invariant Hilbert space, including its centre-neutral subspace. To prove this, first trace over all gauge-invariant scalars. Consider $\operatorname{Tr}(P_D\widetilde F^2P_D)^j$ in period $2j$, $j\ge2$. Cyclicity and commutation of the projection with $C$ insert one truncated convolution at the bond $e$ on each alternate electric cut. The kernel is $\sum_{d\le D}d\,c_d\chi_d$, of absolute value at most $\sum_{d\le D}d^2$. The unmodified normalized kernel on that plaquette is $z_\beta^{-1}e^{-\beta a_p}$, $a_p=1-w(U_p)$. The temporal gauge integrations are the ordinary ones. Hence the trace divided by $\operatorname{Tr}\widetilde F^{2j}$ is bounded by
\[
 (z_\beta\textstyle\sum_{d\le D}d^2)^j\,\mathbb E\exp(\beta\sum_{p\in S}a_p),
\]
where $S$ consists of the $j$ marked plaquettes. This is the spin insertion of Lemma OS in row 860, repeated on disjoint cuts. Positivity of the original operator power justifies the upper bound even when a truncated kernel changes sign. [Electric spin insertion](gap-hs-max.md)

**PROVED.** All these temporal plaquettes have the same orientation and the same parity in a perpendicular spatial coordinate. Row 1151, (23), bounds the last expectation by $e^{C_0j}$. Its rectangular-volume bound here follows from the same slice reflections on the even torus. They bound the log moment per mark by twice a per-site log partition difference. After dissemination the marked parity has been deleted. Each missing face has a five-face detour through the next unmarked layer. The cube inequality of (23) bounds the disseminated action below by $1/42$ of the original. For completeness the pressure difference at $\beta/42,\beta$ is bounded uniformly even as $j\to\infty$ at fixed $n$. The normalized one-plaquette half-coupling estimate on rectangles gives $\gamma\mathbb E_\gamma a_p\le C$ for every orientation. Summing over the $6V$ faces and integrating $d\gamma/\gamma$ costs at most $6C V\log42$. The half-coupling estimate itself uses the ordered normalized one-link multipliers and trace Hölder in a direction of the marked face, independently of the period lengths. Thus the constants in the trace ratio are uniform. At fixed side and coupling the $j$-th root of $\operatorname{Tr}\widetilde F^{2j}$ tends to one and the $j$-th root of the positive numerator tends to $\|P_D\widetilde F^2P_D\|$. Finally $\widetilde F^2\succeq h^2{\bf1}_{[h,1]}(\widetilde F)$. These facts prove (8). Restriction to a centre sector preserves the bound, since both projections commute with the flips. [Parity detour and dissemination](gap-solve5-astra62.md) · [Half-coupling moment](gap-solve7-astra62.md)

**PROVED (strict excess for slow singlets).** There are absolute $\epsilon>0,\beta_0<\infty$ such that, for even $n\ge4$, $\beta\ge\beta_0$ and $f$ in the neutral $[1/2,1]$ band,
\[
 \langle W_e f,F_{xy} W_e f\rangle
       \ge (p_\beta+\epsilon/\beta)\langle f,Uf\rangle .                    \tag{9}
\]
Indeed $z_\beta\asymp\beta^{-3/2}$ by the SU(2) angle density $(2/\pi)\sin^2\theta\,d\theta$. Choose a fixed $k_0>0$ small enough that (8) with $h=1/2$, $D=\lfloor k_0\sqrt\beta\rfloor$ is at most $1/2$. Thus at least half the squared norm of $Yf$ lies at $d>D$. Now $H_\beta(d)$ increases in $d$. Its adjacent difference is $\partial_\beta\log(I_{d+1}/I_d)>0$, since this ratio is the mean of $u$ under the density proportional to $e^{\beta u}(1-u^2)^{d-1/2}$ on $[-1,1]$ and its derivative is the variance. For $d/\sqrt\beta\to k_0$ one has
\[
 c_d(\beta)\longrightarrow e^{-k_0^2/2},\qquad
 \beta c'_d(\beta)\longrightarrow (k_0^2/2)e^{-k_0^2/2}.                   \tag{10}
\]
For the first limit integrate $\chi_d/d=\sin(d\theta)/(d\sin\theta)$ in the one-link probability law. Under it $\sqrt\beta\,\theta$ tends to the radius of a standard Gaussian $Z$ in $\mathbb R^3$. Rescale the Haar angle integral and use $1-\cos\theta\ge2\theta^2/\pi^2$ to dominate all fixed polynomial moments. The limiting character is the spherical average of $e^{ik_0\omega\cdot Z}$ over unit $\omega$, giving the first value. In the differentiated measure the extra factor is $\beta(w-p_\beta)$ and tends in the same integral to $(3-|Z|^2)/2$. Differentiating the elementary Gaussian characteristic function gives the second value. These arguments hold with $d$ fixed during differentiation, then chosen along the sequence. Therefore $H_\beta(d)\ge k_0^2/(4\beta)$ throughout $d>D$ for large $\beta$. Equation (7) gives (9). In particular $p_\beta=1-3/(2\beta)+o(\beta^{-1})$ by the same angular integral.

**PROVED.** Min–max in (9) gives $r_{k,xy}\ge(p_\beta+\epsilon/\beta)r_{k,+}$ whenever $r_{k,+}\ge1/2$. In particular if $1-r_{k,+}=o(1/\beta)$ then $r_{k,xy}>p_\beta$ eventually. This prevents a proof based on $r_{1,xy}<p_\beta$ at any physical size where an excited neutral state of bounded physical energy is already available, since such a state has $1-r_{1,+}=O(a)=o(1/\beta)$ on the stated tuning. The finite-box excited-state witness requires the rectangular source hypotheses of row 1163, (13). This conclusion keeps them as hypotheses. The absolute static-charge cost and the excess above the isolated one-link factor can coexist. [Finite-box witness](gap-solve10-astra62.md)

## A bound on the variation of an arbitrary slow neutral state

**PROVED.** Write $\nu(dX)=\psi(X)^2dX$ and $\mathcal D(f)=\langle f,(I-U)f\rangle$. For every neutral $f$ with spectral support in $[h,1]$, $h=1-\delta$, $0\le\delta\le(1-q)/2$, and every spatial link $e$,
\[
 \int |D_e(f/\psi)|^2\,d\nu
       \le C\beta^2(1-q)^{-3}\mathcal D(f).                                 \tag{11}
\]
This also covers superpositions with different eigenvalues. For the proof use the iteration preceding (5) on $U^{-m}f$ in this band and let $m\to\infty$. Its endpoint is bounded by $C\sqrt\beta q^{m-1}h^{-m}\|f\|$ and tends to zero. Subtract $(f/\psi)D_e\psi$ from $D_e f$. The instantaneous force cancels. At step $s\ge1$ the term involving $U^{-s}f-f$ has norm at most
\[
 4\beta(q/h)^s s\sqrt{\delta\mathcal D(f)},
\]
using $1-r^s\le s(1-r)$ and $|J_e|\le4\beta$. To bound the other term put $\rho=f/\psi$. The kernel domination used for (1), iterated $s$ times, also applies with the scalar multiplier $\rho(Y)-\rho(X)$ for fixed initial $X$. In the projected kernels the norm of the colour matrix is bounded by $q^s$ times the positive scalar kernel pointwise. The same holds if one uses only vertex projection and keeps all centre sectors. The scalar kernel after multiplying by $\psi(Y)/\psi(X)$ is a Markov kernel $P_s(X,dY)$ stationary for $\nu$. Therefore
\[
 \|F_x^s(J_e f)-\rho F_x^s(J_e\psi)\|_2
 \le 4\beta q^s
 \left(\int|\rho(Y)-\rho(X)|^2\,\nu(dX)P_s(X,dY)\right)^{1/2}
 \le 4\beta q^s\sqrt{2s\mathcal D(f)} .
\]
The first estimate uses conditional Cauchy–Schwarz and the second uses self-adjointness and $1-r^s\le s(1-r)$. Since $1-q/h\ge(1-q)/2$, summing both estimates costs at most $C\beta(1-q)^{-3/2}\sqrt{\mathcal D(f)}$. This proves (11).

**PROVED.** In particular, in any unit neutral state of physical energy supported in $[0,E]$ at a fixed $E$, the squared gradient of its ratio to the vacuum on each individual link is at most $C_E(1+\beta)^5 a$. This tends to zero on $\beta=O(\log(1/a))$, uniformly over the link and the chosen vector. A fixed finite set of directions obeys the sum of these bounds. The ground-state weight here is the true finite-cube Wilson vacuum.

## Which electric states does the Wilson vacuum occupy?

**GUIDE.** Inequality (8) excludes very low link spins in every slow state. For the vacuum the full scaled spin law can be recovered while keeping every modified electric kernel positive. The input from row 1231, (1)–(2), is the Wilson comparison of radii for any fixed number of plaquettes on an even $n^3\times M$ torus, uniformly for $M\ge n$, $\beta\to\infty$, $\beta\le B\log n$. It combines row 1151's weak-coupling box estimate, based on Sourav Chatterjee's free-energy method, with a coupling of free curl projections. The free exact-form covariance and its Fourier symbol are due here to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Wilson comparison](gap-solve26-astra62.md) · [Free covariance](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1673-L1695) · [Symbol](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1740-L1762)

**PROVED (joint electric spin law).** Fix finitely many distinct spatial links $e_i$ on a single electric cut, with fixed lattice offsets and arbitrary orientations. Let $\widetilde\psi=Y\psi$ be the normalized electric-placement vacuum. Measure their commuting spin dimensions $d_i$ in this state. Let $\Gamma$ be the restriction of the infinite unit-lattice exact-curl projection to the temporal plaquettes over those oriented links. Then
\[
 (d_i/\sqrt\beta)_i \ \Longrightarrow\ (|G_i|)_i,\qquad
 \mathbb E G_i^a G_j^b=\delta_{ab}(I-\Gamma)_{ij},                           \tag{12}
\]
where $G$ is a centred real Gaussian array. This allows a singular covariance. At one link the limiting density on $k>0$ is $4k^2 e^{-k^2}/\sqrt\pi$.

**PROVED.** For $\tau\ge0$ put $\beta'=\beta/(1+\tau)$ and $L_{\tau,e}(d)=c_d(\beta')/c_d(\beta)$. This is a positive contraction. At a marked electric cut, insertion of $L_{\tau,e}$ changes exactly the normalized convolution on its link from $C_\beta$ to $C_{\beta'}$. This follows by cyclicity, or by joining the two adjacent $C^{1/2}$ factors there. Put $u_i=\tau_i/(1+\tau_i)$. The thermal expectation of the product on distinct marked plaquettes, time ordered if there are multiple cuts, is therefore
\[
 \prod_i(z_\beta/z_{\beta'_i})\
     \mathbb E_W\exp\!\left(\tfrac12\sum_i u_i R_i^2\right),
       \qquad R_i=\sqrt{2\beta(1-w(U_{p_i}))}.                               \tag{13}
\]
Take initially $\max_i u_i<1/16$. Row 1155, (9), with exponent $1/8$ gives uniform integrability of this exponential on the actual rectangles. The Gaussian exponential has the same property because its covariance has norm at most one. Clip the exponential at a fixed large value, use the bounded Lipschitz comparison of row 1231, (2), and then remove the clipping. The clipped function is Lipschitz in the active radii since $\sum u_i R_i^2$ is bounded before the clipping level. The finite-period trace converges at fixed $n,\beta$ to the vacuum expression as the unmarked time interval tends to infinity. The normalized transfer has a simple Perron eigenvalue, its first power is trace class, and all the inserted multipliers are bounded. All the preceding error estimates are uniform in that period. The free covariance tends to the cylinder one by Fourier summation, then to $\Gamma$ for fixed offsets as $n\to\infty$. The bounded projection symbol is continuous away from zero, which suffices for these limits by discarding arbitrarily small frequency neighbourhoods of zero. Finally $z_\beta/z_{\beta'_i}\to(1+\tau_i)^{-3/2}$ by the Haar angle integral. Gaussian integration in three independent colours now gives
\[
 \lim (13)=
 \left[\prod_i(1+\tau_i)\det(I-\Gamma\,\operatorname{diag}(u_i))\right]^{-3/2}
 =\det\!\left[I+(I-\Gamma)\operatorname{diag}(\tau_i)\right]^{-3/2}.         \tag{14}
\]
The last equality follows by multiplying the matrix inside the first determinant on the right by $\operatorname{diag}(1+\tau_i)$.

**PROVED.** At a single cut the joint spectral projections of the $d_i$ are an ordinary probability measure in $\widetilde\psi$. By (10) the single multiplier $L_{\tau,e}(d)$ converges uniformly for $d/\sqrt\beta$ in compact sets to $\exp[-\tau(d/\sqrt\beta)^2/2]$ in the sense that their sup difference goes to zero. The underlying character argument applies to every convergent sequence of scaled dimensions, including limit zero. Also $L_{\tau,e}(d)$ decreases in $d$, by the adjacent Bessel-ratio monotonicity used in (9). For each single coordinate the probability of $d/\sqrt\beta>K$ is bounded by $(1-\langle L_{\tau,e}\rangle)/(1-L_{\tau,e}(\lfloor K\sqrt\beta\rfloor))$ when the denominator is positive. Let $K\to\infty$ in the limiting upper bound, then $\tau\downarrow0$ in (14). This gives tightness jointly for the finite list. Every subsequential limit has the joint Laplace transform (14) for a neighbourhood in the positive orthant. To see uniqueness for probabilities on nonnegative squared radii, first use analyticity in each right half-plane to extend equality to positive arguments. Polynomials in the coordinate exponentials are dense on their compactified cube. Formula (14) is exactly the transform of the Gaussian radii in (12). Each diagonal of $\Gamma$ is $1/2$, by hypercubic symmetry and projection rank three on six orientations almost everywhere. This proves the stated one-link law.

**PROVED.** The covariance in (12) includes the linear Gauss constraint. For spatial momentum $k$, let $t_i=e^{ik_i}-1$, $s=\sum_{i=1}^3|t_i|^2$, and $\omega=2\operatorname{arsinh}(\sqrt s/2)$. The equal-time spatial symbol of $I-\Gamma$ before restriction to the selected links is
\[
 \frac{sI-t t^*}{2\sinh\omega}\qquad (s>0).                                \tag{15}
\]
Indeed the temporal–temporal block of the full projection has numerator $|t_0|^2I+tt^*$ over $|t_0|^2+s$. Subtract it from the identity and integrate over the time frequency. The integral of $1/(s+2-2\cos k_0)$ is $1/(2\sinh\omega)$, by the decaying solution of the one-dimensional difference equation. Thus the limiting Gaussian array has zero discrete divergence, including for a joint list covering a full star. Statement (12) identifies the measured radii of this array. It does not assign simultaneous quantum measurements to noncommuting colour components.

**PROVED (return of an electric scalar).** At two distinct cuts use the same link and the same fixed $\tau>0$ small enough for (13). Let $b(s)$ be the unit-lattice free covariance between two plaquettes of the complementary spatial orientation separated by $s\ge1$ time steps, at zero spatial displacement. In the infinite-grid limit the off-diagonal temporal entry of $I-P_{\rm ex}$ there is $b(s)$. Its full frequency symbol is $(|\widehat k_j|^2+|\widehat k_k|^2)/\sum_{\mu=0}^3|\widehat k_\mu|^2$, with $j,k$ the two complementary axes, also the symbol of the spatial projection entry. Thus the connected limit of the actual electric-cut vacuum return is
\[
 C_\tau(s)=
 \big[(1+\tau/2)^2-\tau^2 b(s)^2\big]^{-3/2}-(1+\tau/2)^{-3}.               \tag{16}
\]
Here the left-hand observable before taking the limit is $\langle L_{\tau,e}\widetilde\psi,(\widetilde F^s-|\widetilde\psi\rangle\langle\widetilde\psi|)L_{\tau,e}\widetilde\psi\rangle$. Equation (13) at distinct marked cuts yields (16) by the two-dimensional determinant. Formula (15) Fourier-transformed for time $s$ gives a spatial integral with $e^{-s\omega}$. On putting $k=v/s$, dominated convergence gives $b(s)\sim1/(\pi^2s^4)$ as in row 1231, (4)–(5). In this calculation the angular average of $(v_j^2+v_k^2)/(2|v|)$ is $|v|/3$ and $\int_0^\infty r^3e^{-r}dr=6$. Therefore
\[
 C_\tau(s)\sim \frac{3\tau^2}{2\pi^4(1+\tau/2)^5}s^{-8}.
\]
For every sequence $u_j\to\infty$, the vacuum spectral weight of the centred $L_{\tau,e}$ on transfer eigenvalues $r\ge e^{-1/u_j}$ tends to zero. Indeed its limsup is at most $C_\tau(s)$ for each fixed $s$, by positivity of the spectral measure and $r^s\ge e^{-s/u_j}$ on that band. Now send $s\to\infty$. This conclusion controls the *weight in this vector*. The time asymptotic in (16) takes the cutoff limit first at fixed integer $s$.

## Resolving a slow state by its spatial magnetic energy

**GUIDE.** The concentration needed for a gap is in the full transfer space. A bound under the vacuum state alone can miss an orthogonal almost-invariant state. A local magnetic source and the variational principle give a uniform test on the full high spectral band, for sets of plaquettes of arbitrary spatial size.

**PROVED.** Under the growing-cube hypotheses of (12), fix $0<\eta<1/24$. Let $S$ be any set of $N\ge1$ distinct spatial plaquettes of one orientation on one slice, and $A_S=N^{-1}\sum_{p\in S}\beta(1-w_p)$. For every $0<h\le1$ and every $\varepsilon>0$ in a fixed sufficiently small interval with $\varepsilon\ge C_\eta\beta^{-\eta}$,
\[
 \big\|{\bf1}_{\{|A_S-3/4|\ge\varepsilon\}}\,
                   {\bf1}_{[h,1]}(U)\big\|^2
 \le 2 h^{-1/2}\exp(-c_\eta N\varepsilon^2).                               \tag{17}
\]
Constants may depend on the fixed tuning bound $B$. In this formula $A_S$ is a multiplication operator in magnetic placement. For large fixed deviations one can keep the bound at the upper end of the stated interval.

**PROVED.** Put $U_t=e^{tN A_S/2} U e^{tN A_S/2}$ for $|t|\le1/4$. The trace in an ordinary time circle changes the coupling from $\beta$ to $\beta(1-t)$ on these $N$ spatial plaquettes at each time. The whole invariant-space trace tends in $M$-th roots to the top eigenvalue in each model. The vacuum is in the neutral space for both by positivity and centre symmetry. By the one-orientation dissemination and homogeneous pressure derivative of row 1151, (21)–(22b),
\[
 \log\|U_t\|\le N\big[\tfrac34t+C_\eta(|t|^2+\beta^{-\eta}|t|)\big].
\]
The upper trace Hölder proof of (21) works also at $t<0$, where all the couplings are positive. For the $M\to\infty$ limit use even $M\ge n$. The cube-comparison error in (22b) is uniform here. The boundary and leftover fractions are $O(1/b+b/n)$ since $M\ge n$, the open-cube determinant is independent of $M$, and the secant step in (22a) is unchanged. This is precisely the aspect-ratio extension used for (2) of row 1231. [Orientation pressure and its proof](gap-solve5-astra62.md)

**PROVED.** For any unit $f$ in the $[h,1]$ band, $U\succeq h|f\rangle\langle f|$. Consequently $\|U_t\|\ge h\|e^{tNA_S/2} f\|^2=h\langle f,e^{tN A_S} f\rangle$. In fact this yields the stronger prefactor $h^{-1}$ with a stronger exponent than one gets by testing $U_t$ on $f$. To obtain exactly (17), use the same rank-one inequality at $2t$, and Cauchy–Schwarz to get $\langle f,e^{tNA_S} f\rangle\le h^{-1/2}\|U_{2t}\|^{1/2}$. Applying exponential Markov bounds separately with $t$ and $-t$, choosing $|t|=c_\eta'\varepsilon$, proves (17) uniformly in $f$. In particular any near-vacuum states at a fixed physical energy have the same limiting empirical plaquette deficit on every prescribed one-orientation set with $N\to\infty$, in the sense of convergence in probability for fixed tolerances. No assumption on the number of such states went into the argument.

## Short colour pairs at physical separation

**PROVED (replacement of the complete action insertion).** Take the transfer slab for a bounded scalar test $f$ of fixed physical support and write its one-insertion operator as $A(f)$, of width $w$ lattice steps, in magnetic placement. The account's observable is a sum of $1-w_p$ over all six orientations with the test evaluated at each barycentre. Thus $A(f)$ is the sum of single-plaquette operators at the appropriate times, with the ordinary transfers on their two sides. The sum $D_f$ of the absolute coefficients is $O_f(n^4)$ on a fixed physical cube. The result also holds with any specified polynomial bound on $D_f$. For temporal plaquettes the insertion for $w_p$ is *exactly* $W_e^*F_{xy}W_e$ from (6). For spatial plaquettes use (5). More precisely, pad the whole slab by $m=R+1$ ordinary steps on both sides. Each spatial summand then contains $U^m w_p U^m$ with nonnegative remaining transfer powers on its sides. Replace that factor by the displayed terms of (5) with $v=-D_e w_p/3$, retaining the signs for $1-w_p$. The resulting slab operator $A_R(f)$ satisfies
\[
 \|A_R(f)-U^mA(f)U^m\|\le C D_f\sqrt\beta\,q^R .                           \tag{18}
\]
All nonconstant insertions now consist of either a single electric transfer between fundamental endpoint pairs, or two adjoint insertions returning their colour in at most $R$ steps, including coincident insertions $v\cdot J_e$. The fundamental static endpoints persist for one time step. Ordinary transfers pad the resulting neutral operators. Constants are retained exactly. This covers the temporal orientations without differentiating a temporal link in a spatial-slice Hilbert space. [Definition of the smeared density](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L6844-L6852)

**PROVED (conditional physical overlap on the Wilson cylinder).** Assume precisely the rectangular source comparison for the fixed small tent of row 1163, (13)–(14). In its notation let $v$ be the centred slab vector $A(f)\psi-\langle\psi,A(f)\psi\rangle\psi$, with slab orientation chosen as in its reflection pairing. Let $H$ be the spatial averaging contraction of that row. Its estimate gives $G=\langle Hv,U^{u_2}Hv\rangle\ge g_d>0$ at a fixed physical scale $d$, and at most $G/16$ of that weight has $-a^{-1}\log r>E_*$, with $E_*$ independent of the cutoff. Hence for the projection $Q$ on the *excited* neutral states of physical energy at most $E_*$ one has $\|QHv\|^2\ge15g_d/16$. Define $v_R$ by acting on the vacuum with the correspondingly oriented $A_R(f)$ and centring. Equation (18) gives $\|v_R-U^m v\|\le2C D_f\sqrt\beta\,q^R$, also for the adjoint orientation. Since $H$ commutes with the transfer and the vacuum projection,
\[
 \|QH v_R\|\ \ge\
 e^{-a m E_*}\sqrt{15g_d/16}-2C D_f\sqrt\beta\,q^R .                       \tag{19}
\]
Take $R=O((1+\beta)\log n)$ large enough in (18). The second term tends to zero and $am\to0$. In particular the covariance of these centred, spatially averaged paired insertions at any additional fixed positive physical separation $T$ has liminf at least $(15g_d/16)e^{-T E_*}$ under the same hypotheses, by the positive spectral theorem. The sources in this statement are the same fixed physical test at each cutoff. Normalization of the observable and the conditional short-distance input are those of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Cylinder source port](gap-sdcyl-ca-astra.md) · [Spectral extraction from the two times](gap-solve10-astra62.md)

**ARGUED.** Equations (18)–(19) locate a specific loss in an attempted mass proof by static screening. Colour can return inside a time interval whose physical length tends to zero, while the resulting scalar has a component propagating over a fixed physical separation. To bound the bottom of that component one needs a connected estimate *between* neutral insertions. The static charged resolvent controls the return inside each insertion.

## The one-step static-pair cost on the whole slow band

**PROVED.** Put $Q_h={\bf1}_{[h,1]}(U)$ and $h=1-\delta$, $0\le\delta\le1/4$. In the same growing cube as (17), for every $\eta<1/24$ with $\eta>0$ and every spatial edge $e$,
\[
 \left\|Q_h\left[\beta(U-W_e^*F_{xy}W_e)-\tfrac34 I\right]Q_h\right\|
 \le C_{\eta,B}\big(\sqrt\delta+\beta^{-\eta}\big).                         \tag{20}
\]
The same bound holds for multiplication by $\beta(1-w_p)-3/4$ for each spatial plaquette $p$. Here the cost is for insertion of the one-link state on either side of a *single* transfer.

**PROVED.** In temporal orientation let $T_g$ be one transfer step with the multiplier $g(X)$ on the marked temporal plaquette, where here $X=\beta(1-w_p)\ge0$. In particular $T_1=U$, $T_X=\beta(U-W_e^*F_{xy}W_e)$. The kernel is self-adjoint for real $g$. By (21)–(22a) of row 1151 and the same even-rectangle limit as in (17), the norm of $T_{\exp(tX)}$ is at most $\exp[3t/4+C_\eta(t^2+|t|\beta^{-\eta})]$ for $|t|\le1/4$. Its repeated-step trace is the Wilson integral with the temporal plaquette over that link at every time tilted by $t$. For both signs the modified one-link kernel is a positive convolution at coupling $(1-t)\beta$ times a positive constant. Also
\[
 \|T_{\exp(tX)}-U-tT_X\|\le C t^2 .
\]
In fact $|e^{tX}-1-tX|\le Ct^2e^{X/2}$ for the stated $t$, and $T_{\exp(X/2)}$ is bounded in norm by $z_{\beta/2}/z_\beta\le C$ by the normalized convolution ordering. Vertex projection and restriction preserve the kernel-domination estimate, by taking absolute values on the full slice. For unit $f\in Q_h$, compare its Rayleigh quotient in the Taylor expansion to the upper norm at positive and negative $t$, using $\langle f,U f\rangle\ge1-\delta$. This gives an error $C(\delta/|t|+|t|+\beta^{-\eta})$ in its expectation of $T_X$. Choose $|t|$ of order $\sqrt\delta$ capped at $1/4$, or let it tend to zero if $\delta=0$. For a spatial plaquette use $U_t=e^{tX/2}Ue^{tX/2}$. The rank-one argument in (17) gives $t\langle f,Xf\rangle\le\log\|U_t\|-\log h$ directly by Jensen. Both assertions follow by the variational characterization of the norm of a self-adjoint compression.

**PROVED.** Thus on any band with $1-h\to0$ the Rayleigh quotient of an adjacent fundamental dipole under one step is that of the corresponding singlet minus $(3/4+o(1))/\beta$, uniformly throughout the band. The mean plaquette calculation of row 1151 already gives this coefficient in the vacuum. Equation (20) controls off-diagonal matrix elements and all the other vectors in the band. Its absolute error as an approximation of the transfer is $O(\beta^{-1}(\sqrt\delta+\beta^{-\eta}))$. At $\delta=O(1/n)$, multiplying this error bound by a time of order $n$ does not give a vanishing physical-time error. Also $(W_e^*F_{xy}W_e)^t$ inserts the projection $W_eW_e^*$ between successive charged steps. The unrestricted charged return in time $t$ uses $W_e^*F_{xy}^tW_e$.

**PROVED (which one-link distributions a slow vector can change).** Let $h_j\uparrow1$ on the growing cubes above. For every bounded Lipschitz $g:[0,\infty)\to\mathbb R$, put $\mu_g=\mathbb E g(|Z|/\sqrt2)$ for a standard three-colour Gaussian $Z$. Uniformly in the location and in unit vectors in the $[h_j,1]$ band, the following hold:
\[
 \begin{split}
 &\|Q_{h_j}\,[g(R_{p_{\rm sp}})-\mu_g I]\,Q_{h_j}\|\longrightarrow0,\\
 &\|Q_{h_j}\,[T_{g(R_{p_{\rm tm}})}-\mu_g I]\,Q_{h_j}\|\longrightarrow0,\\
 &\left\|\widetilde Q_{h_j}
       [g(d_e/\sqrt\beta)-\mu_g I]\widetilde Q_{h_j}\right\|
                                                        \longrightarrow0,     \tag{21}
 \end{split}
\]
where $\widetilde Q_h={\bf1}_{[h,1]}(\widetilde F)$. The first reading is on a spatial plaquette. The second is a one-step insertion on a temporal plaquette. The last is a measurement of a single electric spin, with the Maxwell density in (12). The limit allows every unit vector in the band to depend on the cutoff.

**PROVED (pressure for the radial probe).** Write $H=\|g\|_\infty$, $D=\operatorname{Lip}g$, and let $p(t)-p(0)$ be the per-site log moment of $t\sum_{p\ \mathrm{of\ one\ orientation}}g(R_p)$ on the even $n^3\times M$ torus. Uniformly over even $M\ge n$, for each fixed $|t|\le 1$,
\[
 \limsup_{j\to\infty}\{p(t)-p(0)-t\mu_g\}\le C_g t^2 .                    \tag{22}
\]
Here are details preserving the normalization needed in a spectral bound. Use the disjoint open boxes of row 1151, (22b) and (24), with $b=\lceil\beta^\gamma\rceil$, $0<\gamma<1/12$. The unperturbed Wilson density relative to their independent normalized open-box measures and the remaining Haar links is bounded pointwise by $e^{CV\Delta_b}$, $\Delta_b=(\log\beta)(1/b+b/n)$, $V=n^3M$. This follows by dropping the nonnegative crossing action and binding the ratio of normalizers by the open-box upper and gluing lower comparisons. The omitted readings cost at most $H|t|\,O(V(1/b+b/n))$ in the exponent. It suffices to bound independent one-box exponential moments.

**PROVED.** In a good box the comb-tree coordinates are in the chart of radius $b^{-7/2}$. Its density is bounded by $e^{Cb^3}$ times the Gaussian with precision $(1-C_1/b)\beta D_1^*D_1$ on each colour, where $D_1$ is the tree-gauge curl. For its linear curvatures $\ell=\sqrt\beta D_1 X_{\rm tree}$, the sum of squared radius-replacement errors is at most $Cb^{-2}\|\ell\|^2$. This uses the Taylor estimate in row 1151, (24), and the comparison of quadratic and Wilson actions on the same chart. If $N_b\le Cb^4$ terms are read, their contribution to the exponent changes by at most $C_g|t|b^{-1}(b^4+\|\ell\|^2)$ by Cauchy–Schwarz. The map from independent standard normals to $\ell$ has norm at most $(1-C_1/b)^{-1/2}$. Thus $\sum g(|\ell_p|)$ is $C D\sqrt{N_b}$-Lipschitz in those normals. The Gaussian exponential bound proved by rotation in (24) yields a log moment at most its linear mean plus $C D^2 t^2N_b$. The extra quadratic exponential has log moment $O_g(|t|b^3)$, since the rank is $O(b^4)$ and the covariance norm is bounded. Applying Cauchy–Schwarz to the two exponentials, each with twice its parameter, gives both bounds together.

**PROVED.** Under the normalized open-box Wilson measure the bad chart has probability at most $\exp[-c\beta/b^8+C b^4\log\beta]$. The tree shelling requires action at least $c/b^8$ outside the chart, and restricting the $O(b^4)$ links to radius $\beta^{-1}$ gives the stated lower bound on the normalizer. Even after multiplication by $e^{|t|H N_b}$ this contribution is negligible relative to $e^{-|t|H N_b}$ because $\beta/b^{12}\gg\log\beta$. Summing the box log bounds therefore costs $O_g(1/b+\Delta_b)$ per site beyond the linear Gaussian mean and $C_g t^2$. The difference of the averaged linear-radius Gaussian mean and $\mu_g$ tends to zero. Indeed couple the box curls to the periodic curl by the nested-projection trace estimate in (1) of row 1231, at mean squared error per coordinate $O(1/b+b/n)$, including the dilution and omitted coordinates as there. The diagonal of the periodic projection tends to $1/2$ uniformly for $M\ge n$ by bounded Fourier summation. This proves (22). The box estimates and coupling used here are due to the earlier rows. The exponential pressure bound is needed to pass from a single vacuum to the entire spectral band. [Open-box comparison](gap-solve5-astra62.md) · [Coupling of the curl projections](gap-solve26-astra62.md)

**PROVED.** For a source on one plaquette repeated at all times, trace Hölder along the four axes bounds log norm of the modified one-step transfer by the homogeneous per-site pressure difference, after sending the even time period to infinity. In a direction of the plaquette the modified one-link kernel is real and central, giving a self-adjoint layer sandwich. The even period gives $\operatorname{Tr}|F_i|^{n_i}=\operatorname{Tr}F_i^{n_i}$ in the Hölder step even for a radial weight that lacks positive Fourier multipliers. Other directions use positive magnetic layers. The uniformly repeated integrals have positive Boltzmann weights. This gives the same dissemination as (21) of row 1151. In the physical time direction an even trace root gives the operator norm also for a self-adjoint layer. For the spatial reading use $t\langle f,g f\rangle\le\log\|U_t\|-\log h_j$. For the temporal reading the operator-norm Taylor remainder for $T_{\exp(tg)}-U-tT_g$ is $O_H(t^2)$ by kernel domination. Use (22) with both signs, let $j\to\infty$ at fixed $t$, then $t\to0$. This proves the first two norm limits in (21).

**PROVED.** To obtain the last assertion, set $0<u<1$, $\tau=u/(1-u)$ and use the temporal probe $e^{uR^2/2}$. Truncating it at $R^2/2=K$ costs $C_{u'}e^{-(u'-u)K}$ in one-step operator norm for $u<u'<1$, by domination with $T_{\exp(u'R^2/2)}$ of norm at most $z_{(1-u')\beta}/z_\beta$. The Gaussian expectation has a vanishing tail as well. The exact marked transfer after multiplying by $z_\beta/z_{(1-u)\beta}$ is $Y^* L_{\tau,e}Y$. The unitary correspondence between the two high spectral bands is $YU^{-1/2}$, whose extra factor $U^{-1/2}$ differs from identity there by at most $h_j^{-1/2}-1$. Therefore every unit vector on the electric band has expectation of $L_{\tau,e}$ tending uniformly to $(1+\tau/2)^{-3/2}$. Along any sequence of such vectors, use monotonicity, tightness and uniqueness of the Laplace transform exactly as for (12). This gives weak convergence of its measured $d_e/\sqrt\beta$ to $|Z|/\sqrt2$. A sequence of Rayleigh quotients witnessing failure of the last operator-norm limit in (21) would contradict this convergence.

## Removing the intermediate projection in the static return

**GUIDE.** Equation (20) concerns repeated projection onto $W_e$'s range. To test what is lost in that projection, consider the true Perron value $r_{xy}=\|F_{xy}\|$ of the two-charge transfer. The gauge integral in each electric layer is a three-dimensional SU(2) spin integral with prescribed bond matrices. A score inequality on a finite spatial neighbourhood allows the colour disturbances to spread over its vertices. The comparison energy is its electrical resistance.

**PROVED (finite-patch score inequality).** Fix distinct interior vertices $x,y$ of a finite spatial cube $B$ in lattice units. Allow gauges at the vertices of $B$ to vary, extending every variation by zero outside $B$. Let $L_B$ be the graph Laplacian with this Dirichlet convention, with quadratic form $\sum_{\langle i,j\rangle}|v_i-v_j|^2$ over unoriented nearest-neighbour bonds meeting $B$. Conditional on two spatial slices $X,Y$, give the temporal vertex matrices $g_i$ their Wilson density proportional to
\[
 \exp\{\beta\sum_{e=(i,j)}w(H_e)\},\qquad H_e=X_e g_j Y_e^{-1}g_i^{-1}.
\]
The expectation below integrates *all* the $g_i$. Suppose a gauge on $X$ makes its internal $B$-links within $\epsilon$ of identity and $\mathbb E_{g|X,Y}|1-H_e|\le\epsilon$ on those links. Put $G_B^\epsilon=(L_B+C_B\epsilon I)^{-1}$ and $\mathcal R_B^\epsilon=G_{xx}^\epsilon+G_{yy}^\epsilon-2G_{xy}^\epsilon$. For sufficiently small $\epsilon$,
\[
 \big\|\mathbb E_{g|X,Y}\,[A\mapsto g_x A g_y^{-1}]\big\|
             \le (1+3\mathcal R_B^\epsilon/\beta)^{-1/2}.                    \tag{23}
\]
Independent changes of frame at the two slices multiply this matrix on each side by unitaries, preserving its norm and the individual holonomy deficits.

**PROVED.** For a real array of imaginary quaternions $v=(v_i)_{i\in B}$ denote by $D_v$ the derivative of $g_i\mapsto e^{t v_i}g_i$ simultaneously. The real score $s_v=D_v\log p(g)$ has mean zero. Haar integration by parts gives $\mathbb E s_v^2=-\mathbb E D_v^2\log p$. On the bond $e=(i,j)$ the varied trace is $w(e^{-t v_i}e^{t b_j}H_e)$, with $b_j=\operatorname{Ad}_{X_e}v_j$. The negative second derivative at zero is $|v_i-b_j|^2w(H_e)+2 w((v_i\times b_j)H_e)$, where the imaginary product convention is $ab=-a\cdot b+a\times b$. The second summand has absolute value at most $2|v_i||v_j||1-H_e|$. On internal edges $\operatorname{Ad}_{X_e}=I+O(\epsilon)$ in the chosen frame. On boundary edges one vector is zero and the first term is bounded by the squared difference with zero. Thus the covariance matrix of all $3|B|$ real scores is bounded above by $\beta (L_B+C_B\epsilon I)\otimes I_3$ in quadratic-form order. No lower bound on that covariance is needed.

**PROVED.** For unit $A$ in the matrix fibre put $Z(g)=g_x A g_y^{-1}$ and $m=\mathbb E Z$. Then $\mathbb E\|Z-m\|^2=1-\|m\|^2$. The covariances of $Z-m$ against the scores are $-\mathbb E D_v Z=-v_x m+m v_y$. For any mean-zero real score vector $s$ with $\mathbb E ss^\top\preceq J$ and $J>0$, the squared norm of its vector of covariances with $Z$, after multiplying by $J^{-1/2}$ on the score index, is at most $\mathbb E\|Z-m\|^2$. Indeed the components of $J^{-1/2}s$ have Gram operator at most identity, so Bessel's inequality in operator form applies to each real or complex fibre coordinate. Use the preceding score bound. All entries of $G_B^\epsilon$ are nonnegative by the discrete maximum principle. For the orthonormal quaternion generators $a$, $\sum_a\operatorname{Re}\langle a m,m a\rangle\le3\|m\|^2$ by Cauchy–Schwarz. The two diagonal terms in Bessel's inequality contribute $3(G^\epsilon_{xx}+G^\epsilon_{yy})\|m\|^2/\beta$. The cross term is at least $-6G^\epsilon_{xy}\|m\|^2/\beta$. This gives $1-\|m\|^2\ge3\mathcal R_B^\epsilon\|m\|^2/\beta$, proving (23). The estimate holds for every colour matrix, including its traceless component.

**PROVED (lower bound on the true static energy).** Fix the displacement $z=y-x\ne0$ in lattice units on the growing even cubes. Choose seams away from a fixed path $\gamma$ joining them, and use the corresponding centre-invariant matrix space. One has
\[
 \liminf_{j\to\infty}-\beta_j\log r_{xy}\ \ge\ \tfrac32\mathcal R(z),\qquad
 \mathcal R(z)=\int_{[-\pi,\pi]^3}
       \frac{|1-e^{ik\cdot z}|^2}{\sum_{i=1}^3|e^{ik_i}-1|^2}\,
                              \frac{d^3k}{(2\pi)^3}.                         \tag{24}
\]
First $r_{xy}\ge1-O_z(1/\beta)$. Test the one-step compression on $X(\gamma)\psi$. Its Rayleigh quotient is the vacuum Wilson ribbon of height one, by row 1143, (8). Shell its fixed finite disk, writing the boundary holonomy as a product of conjugated face holonomies with orientations. By the invariant quaternion distance and Cauchy–Schwarz its deficit is at most $|\gamma|\sum_{p\ \rm in\ ribbon}(1-w_p)$. The mean of each summand is $O(1/\beta)$ by the half-tilt bound. The estimate is uniform in the growing cubes.

**PROVED.** Take a unit top eigenvector $A$ of $F_{xy}$, and $f(X)=\|A(X)\|$. Then $f$ is invariant, centre neutral and $\langle f,U f\rangle\ge r_{xy}$ by kernel domination. Its norm outside $Q_{1-\beta^{-1/2}}$ is $O_z(\beta^{-1/4})$. For the part in this band, (20) bounds the expectation of each spatial $\beta a_p$ by a constant times its squared norm. Markov's inequality and the norm bound on the discarded part imply $\|{\bf1}_{\{|1-X_p|>\beta^{-1/8}\}} f\|\to0$ on any prescribed finite list of plaquettes. On a fixed cube $B$, tree gauge then makes all internal spatial links $O_B(\beta^{-1/8})$ from identity off a set of vanishing $f^2$ mass. Each tree-gauge link is a loop in the cube with a filling by a bounded number of conjugated elementary faces, since the full cube with its plaquettes is simply connected.

**PROVED.** Write $k_0(X,Y)$ for the positive vertex-averaged scalar kernel in vacuum normalization and $d\omega=f(X)k_0(X,Y)f(Y)\,dX\,dY$. Its total mass is between $r_{xy}$ and one. A bad $X$ as above costs $o(1)$ in $\omega$ by Cauchy–Schwarz and $\|Uf\|\le1$. For each internal temporal bond integral,
\[
 \int\mathbb E_{g|X,Y}|1-H_e|\,d\omega\le C/\sqrt\beta .
\]
Indeed $\sqrt\beta|1-H_e|=\sqrt{2X_p}$ with $X_p=\beta(1-w(H_e))$ and its positive insertion kernel is dominated by $C T_{\exp(X_p/2)}$, bounded in (20). Markov's inequality at threshold $\beta^{-1/8}$ makes the second exceptional set in (23) also $o(1)$ in $\omega$ for fixed $B$. On the good set use (23), on its complement use unitarity. The charged Rayleigh quotient is bounded by the integral against $\omega$ of the conditional colour-matrix norm. Thus
\[
 1-r_{xy}\ge
 [1-(1+3\mathcal R_B^\epsilon/\beta)^{-1/2}]\,\omega(\mathrm{good}),
 \qquad\epsilon=C_B'\beta^{-1/8},\qquad\omega(\mathrm{good})\to1 .
\]
The fact that the exceptional mass merely tends to zero suffices because it multiplies the $1/\beta$ gain. This yields the lower bound first with $\mathcal R_B^0$ in (24).

**PROVED.** Exhaust $\mathbb Z^3$ by cubes $B$. The resistance $\mathcal R_B^0$ is the supremum over real $v$ supported in $B$ of $2(v_x-v_y)-\sum_{\langle i,j\rangle}(v_i-v_j)^2$, by completing the square. Its increasing limit is (24). Fourier transform and complete the square again, now in the space with squared norm $\int |\widehat v|^2\sum_i|e^{ik_i}-1|^2\,dk/(2\pi)^3$. The representing vector for $v_x-v_y$ is in that space by the finite integral in (24). Trigonometric polynomials are dense there, by first truncating away from the single zero and approximating continuous functions. This proves the equality of the supremum and the integral, including the choice of boundary conditions.

**PROVED (matching upper bound from finite-height Wilson ribbons).** In the same setting,
\[
 \lim_{j\to\infty}-\beta_j\log r_{xy}=\tfrac32\mathcal R(z).
 \quad\text{In particular at a nearest neighbour this limit is }1/2.         \tag{25}
\]
Fix a simple lattice path $\gamma$ from $x$ to $y$ of bounded length and fix an integer height $s\ge1$. Its temporal ribbon $D_s$ has an oriented face indicator $j_s$. The vacuum expectation of its half-trace $W(\gamma,s)$ satisfies
\[
 \lim_{j\to\infty}\beta_j[1-W(\gamma,s)]
                      =\tfrac32\langle j_s,P_{\rm ex} j_s\rangle .           \tag{26}
\]
Here $P_{\rm ex}$ is on the infinite four-dimensional unit lattice. The following argument checks the interacting comparison for this fixed ribbon. Shell the disk to express its boundary holonomy as the product of its oriented, transported plaquettes at one anchor. In $\sqrt\beta(1-U_{\partial D_s})$, the product differs, up to an overall sign, from the sum of their scaled transported imaginary parts by $o_{L^2}(1)$. Indeed the real defects contribute $O_{D_s}(\beta^{-1/2})$ in $L^2$, and the higher product terms have that bound by Hölder using all fixed moments of $\sqrt{\beta}|1-U_p|$ from row 1155, (9). Reversed faces give the negative imaginary part. The squared norm of the whole scaled boundary deficit is uniformly integrable because it is bounded by $|D_s|\sum_{D_s}2\beta a_p$.

**PROVED.** The norm of the transported sum converges in law to the norm of the three independent Gaussian sums $\langle j_s,P_{\rm ex}Z^a\rangle$. To see this for a folded spacetime ribbon, translate its fixed finite window on the four-torus. Except on a fraction $O_{D_s}(1/b+b/n)$ of translations it and every transport path fit into one open box. On a good box use its comb-tree gauge. For each path of fixed length dropping the adjoint transport changes a scaled curvature by at most $C_{D_s}b^{-7/2}\sqrt\beta|1-U_p|$. The mean-square sum of the errors of replacing the imaginary parts by the linear curls, per translated face, is $O(b^{-2})$ on good boxes by the Taylor bound in row 1231, (8)–(9). The bad-box probability is $O(e^{-c\beta/b^8})$. For a bounded Lipschitz radial test of the sum, the translation-averaged linear test on the product Gaussian has Lipschitz constant $O_{D_s}(V^{-1/2})$ because the signed coefficient array has fixed finite $\ell^1$ norm. The density/entropy bound $CV\Delta_b$ of row 1151, (24), and its Gaussian rotation estimate give error $O_{D_s}(\sqrt{\Delta_b})$. Finally the nested-projection comparison replaces box curls by $PZ$ at mean error $o(1)$, as in (12). This is the fixed-window transported-curvature argument of row 1231 with a signed list of temporal faces. Each bound uses only the finite window, and the test is invariant under a common rotation at its anchor. They are uniform in the even time period $M\ge n$, so passage to the vacuum and then the infinite-grid Gaussian is justified as in (13). Taking second moments by the stated uniform integrability and using $1-w(U)=|1-U|^2/2$ proves (26). [Transported-curvature comparison](gap-solve26-astra62.md)

**PROVED.** The vacuum open-line formula gives $W(\gamma,s)\le r_{xy}^s$. Take $\limsup_j$ in $-\beta_j\log r_{xy}\le-(\beta_j/s)\log W(\gamma,s)$, then take $s\to\infty$. The time Fourier factor of $j_s$ is $\sum_{u=0}^{s-1}e^{ik_0u}$. Its squared norm divided by $s$ is the Fejér kernel of integral one. For every spatial momentum $k\ne0$ the projection block in the integrand is continuous at $k_0=0$. The time average there converges to $tt^*/|t|^2$, where $t_i=e^{ik_i}-1$. It is bounded in norm by one, so dominated convergence applies in spatial momentum. The lattice divergence of the oriented spatial path is its pair of endpoints. Consequently $|t^*\widehat j_\gamma(k)|^2=|1-e^{ik\cdot z}|^2$, and $\langle j_s,P_{\rm ex}j_s\rangle/s\to\mathcal R(z)$. Combining with (24) proves (25). For a nearest-neighbour $z$ the three integrands for the three coordinate directions sum to one and have equal integrals, giving $\mathcal R(z)=1/3$.

**PROVED (cost of projecting after every step).** For a nearest-neighbour edge,
\[
 -\beta\log\|W_e^*F_{xy}W_e\|\longrightarrow3/4 .
\]
The vacuum trial and (20) give the lower bound $1-(3/4+o(1))/\beta$ on the norm. A unit optimizing vector then has $\langle f,U f\rangle\ge1-O(1/\beta)$ because $\|T_X\|\le C$. Its component outside $Q_{1-\beta^{-1/2}}$ has norm $O(\beta^{-1/4})$. Boundedness of $T_X$ and (20) give $\langle f,T_X f\rangle=3/4+o(1)$, proving the matching upper bound. Consequently the ratio of the $u$-th powers of the compressed and the true charged spectral radii is $\exp[-(1/4+o(1))u/\beta]$. For $u$ of order $n$ the relative error from the intermediate projection is exponential.

## Multiplicity at the charged threshold

**PROVED.** Fix a finite simple spatial path $\gamma$, a spatial cell of integer side $\ell\ge2$ containing it in its interior, and a cofinal grid with $2\ell\mid n$. Keep the preceding weak-coupling and physical-size assumptions. If $k=k_j\ge0$ is any sequence of indices with $1-r_{k,+}=o(\beta_j^{-1})$, then the eigenvalue with the same index in the charged sector of its endpoints satisfies
\[
             -\beta_j\log r_{k,xy}\ \longrightarrow\ \tfrac32\mathcal R(y-x).
                                                                            \tag{27}
\]
The index is counted with multiplicity. The cell size depends on the spatial path alone. Its divisibility can, for instance, be obtained on compatible tori with a fixed blocking-power cell. Equation (27) includes every index at bounded physical energy. It makes no assumption that the number of those indices stays bounded.

**PROVED (a ribbon estimate in every slow state).** Write $S_s(g)$ for the width-$s$ transfer with scalar insertion $g$ on the ribbon $D_s$ and ordinary Wilson weights on the slab. With $X_D=\beta(1-w(U_{\partial D_s}))$, $S_s(1)=U^s$ and $S_s(X_D)=\beta(U^s-W_\gamma^*F_{xy}^sW_\gamma)$. At each fixed positive integer $s$, for every band $h_j\to1$,
\[
 \big\|Q_{h_j}[S_s(X_D)-c_s I]Q_{h_j}\big\|\to0,\qquad
                       c_s=\tfrac32\langle j_s,P_{\rm ex}j_s\rangle .        \tag{28}
\]
To prove it first use $g_K=\min(X_D,K)$ for fixed $K$. Reversal in time reverses the orientation of the ribbon boundary up to choice of base, preserving its half-trace. Thus $S_s(e^{t g_K})$ is self-adjoint for real $t$. Its even trace powers repeat the ribbon source at time spacing $s$. In each spatial axis the source lies inside one slab of width $\ell$. Disseminate to every such slab by alternating reflection. The log partition ratio before dissemination is at most the final log partition ratio times $(\ell/n)^3$. Indeed group the original transfer in that spatial direction into the $n/\ell$ slab kernels $B_i$ with magnetic half weights on the two boundaries. The absolute trace of their product is bounded by $\prod_i\{\operatorname{Tr}[(B_i^*B_i)^{n/(2\ell)}]\}^{\ell/n}$ by Schatten Hölder. The kernel $B_i^*$ is the reflected slab, so each trace is the completely repeated or unperturbed integral for that slab. Repeat in the other two spatial directions. This is also the slab inequality AM6 of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Slab reflections](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2887-L2905)

**PROVED.** The final periodic array of ribbons has density $\alpha=(s\ell^3)^{-1}$ per spacetime site. Its per-site log moment has limiting upper bound
\[
 t\alpha\,\mathbb E\min\!\left(\tfrac12\big|\textstyle\sum_p(j_s)_p
             (P_{\rm ex} Z)_p\big|^2,K\right)+C_{s,\ell,K}t^2 .
\]
For details apply the box upper bound in (22) to this fixed array, using the three independent colours. At most $O_{s,\ell}(1/b+b/n)$ of its readings per site meet an omitted region or cross a box boundary. In a good box each link in tree gauge is within $Cb^{-7/2}$ of identity. Shelling as in (26) shows that the error in the scaled ribbon chord from dropping transports, dropping real parts and taking only the linear term in the product is at most $C_s b^{-7/2}$ times the sum of its scaled face chords, with the constant also depending on $\gamma$. Each fixed face belongs to a bounded number of windows in this array. The sum of squared errors, including linearization of the face curls, is therefore at most $C_{s,\gamma} b^{-2}\|\ell_{\rm curl}\|^2$ per box, where $\ell_{\rm curl}$ is its complete scaled linear-curl array. The clipped half-square has Lipschitz constant $\sqrt{2K}$ as a function of the vector. This gives the same $O_{s,\ell,K}(|t|b^{-1})(b^4+\|\ell_{\rm curl}\|^2)$ error per good box as in (22). The bad-box estimate there uses only boundedness of $g_K$ and the number of windows per box. The map from all curls to their signed window sums has norm bounded by a constant depending only on the fixed ribbon, by finite row and column sums. The linear-array Gaussian log moment thus has the claimed quadratic error per site. The mean replacement by the global projection costs $o(1)$ per site by the normalized trace of the nested-projection difference and bounded overlap of the array. Every reflected copy has the same free expectation by lattice isometry. These estimates hold for even numbers of time slabs and $M\ge n$.

**PROVED.** After the time trace root, the per-site bound is divided by $\alpha$. The dominating operator estimate $\|S_s(e^{t g_K})-U^s-tS_s(g_K)\|\le C_K t^2$ holds for $|t|\le1$, since $g_K$ is bounded and kernels without insertions give $U^s$. Test on $Q_{h_j}$, use $\langle f,U^s f\rangle\ge h_j^s$, and send $j\to\infty$ and then $t\to0$ from both sides as in (21). This proves (28) with the clipped free mean. To remove $K$, the exact shelling bound gives $X_D\le |D_s|\sum_{p\in D_s}\beta a_p$. Choose $v>0$ with $v|D_s|\le1/2$. The norm of $S_s(e^{vX_D})$ is bounded by a fixed constant by kernel domination. The larger positive insertion with exponent $\sum_{p\in D_s}\beta a_p/2$ just halves fixed temporal-link couplings in each of the $s$ layers. On each layer the normalized positive convolution decreases in operator order and the finite product of the normalizer ratios is bounded. The scalar tail $X_D{\bf1}_{X_D>K}\le C_v e^{-vK/2}e^{vX_D}$ now gives a uniform operator tail. The fixed free Gaussian mean also converges to the unclipped mean. This proves (28).

**PROVED.** On the span of the first $k_j+1$ neutral eigenvectors the infimum of the Rayleigh quotient of $W_\gamma^*F_{xy}^sW_\gamma$ is at least $r_{k_j,+}^s-(c_s+o(1))/\beta$ by (28). The open-line isometry and min–max give this as a lower bound on $r_{k_j,xy}^s$. Under the hypothesis of (27), taking $\limsup_j$ gives $\limsup_j[-\beta\log r_{k_j,xy}]\le c_s/s$. Let $s\to\infty$ using the path-divergence calculation after (26). The reverse bound follows from $r_{k_j,xy}\le r_{xy}$ and (24). This proves (27) with the same charged self-energy for all the indicated states.

## Separating the triplet and the neutral part of the external pair

**PROVED (a positive separation inside the charged comparison).** At each $X$ decompose the matrix fibre into the one-dimensional span of $X(\gamma)$ and its orthogonal complement. Write $\Pi_0=W_\gamma W_\gamma^*$, $\Pi_1=I-\Pi_0$ and $D=\Pi_1 F_{xy}\Pi_1$ on the second space. Put $c=\tfrac32\mathcal R(z)$ and
\[
 G(z)=\int_{[-\pi,\pi]^3}\frac{\cos(k\cdot z)}{\sum_i|e^{ik_i}-1|^2}
                                   \frac{d^3k}{(2\pi)^3} >0 .
\]
For any normalized sequence of matrix vectors $A$ with $\beta(1-\langle A,F_{xy}A\rangle)$ bounded one has
\[
 \liminf_j\left[\beta(1-\langle A,F_{xy}A\rangle)
                         -4G(z)\|\Pi_1 A\|^2\right]\ge c .                  \tag{29}
\]
In particular $\liminf_j\beta(1-\|D\|)\ge c+4G(z)$, and every sequence with charged cost $c+o(1)$ in (29)'s units has $\|\Pi_1 A\|\to0$. This is a separation *within the comparison with two fixed external charges*.

**PROVED.** In the proof of (23) take the tree on $B$ to contain the simple path $\gamma$, so $X(\gamma)=I$ exactly in its gauge. Decompose $m=m_0+m_1$ into scalar and traceless matrices. Quaternion multiplication gives $\sum_a(-a)m a=3m_0-m_1$ on the complex matrix fibre. Hence the exact cross term gives the stronger pointwise inequality on the good set,
\[
 \beta(1-\|m\|^2)\ge3\mathcal R_B^\epsilon\|m\|^2+
                                  8(G_B^\epsilon)_{xy}\|m_1\|^2 .
\]
In arbitrary frames $\|m_1\|=\|\Pi_1(X)m\|$. Use $f=\|A\|$, $a(X)=A(X)/f(X)$ on $f>0$, and $m=\mathbb E[g_x a(Y)g_y^{-1}\mid X,Y]$. The definitions on zero fibres are immaterial to $\omega$. Write $r_A=\langle A,F_{xy}A\rangle$. The argument for (24) uses only $1-r_A=O(1/\beta)$, so $\omega(\mathrm{good})\to1$. The identity $2(1-\operatorname{Re}\langle a,m\rangle)=\|a-m\|^2+1-\|m\|^2$ shows that both terms on the right have $\omega$-integrals $O(1/\beta)$. Also $\|(I-U)f\|^2\le1-\langle f,Uf\rangle=O(1/\beta)$. Therefore integration of $\|\Pi_1 a(X)\|^2$ against the $X$ marginal of $\omega$ differs from $\|\Pi_1 A\|^2$ by $o(1)$. These facts give (29) first with the fixed-box Green function, letting $\epsilon\to0$. For its limit use polarization of the Dirichlet variational formula for point sources at $x,y$ as in (24). The representing single-source energy $\int |t|^{-2}\,dk/(2\pi)^3$ is finite in three dimensions. Positivity of the limiting cross Green function follows also by the killed-walk series $L_B^{-1}=\tfrac16\sum_{j\ge0}P_B^j$, with $P_B$ the killed nearest-neighbour walk. A fixed path inside $B$ gives a strictly positive term independent of larger cubes. This proves (29), including the triplet norm bound by taking optimizing vectors on that subspace.

**PROVED (an exact neutral operator at the charged threshold).** Use the block decomposition with
\[
 A=W_\gamma^*F_{xy}W_\gamma,\qquad B_1=\Pi_1 F_{xy}W_\gamma .
\]
For real $r>\|D\|$ define $H(r)=A+B_1^*(r-D)^{-1}B_1$ on the neutral space. Completing the square in the quadratic form of $F_{xy}-r$ gives
\[
 \#\{\lambda(F_{xy})>r\}=\#\{\lambda(H(r))>r\},\qquad
 H(r_{xy})\preceq r_{xy}I .                                                 \tag{30}
\]
The second assertion holds for all sufficiently fine cutoffs by (25) and (29). The eliminated coordinate of an eigenvector is $(r-D)^{-1}B_1 f$ when $f$ is its neutral coordinate. Compactness makes the counts finite for $r>0$. The matrix levels here have the same centre restriction as (25). Moreover $\|B_1\|\le C_\gamma/\sqrt\beta$. Projected perpendicular to $X(\gamma)$, the outgoing colour $g_xY(\gamma)g_y^{-1}$ has norm bounded by its chord distance from $X(\gamma)$, the chord of the one-step ribbon. Shelling and the one-plaquette half-tilt estimate of (20) bound the corresponding positive kernel by $C_\gamma/\sqrt\beta$ in operator norm. These are statements about the actual Wilson kernel.

**PROVED (the contributions at individual return times).** On the compatible grid of (27), let $h_j\to1$ and $Q=Q_{h_j}$. Put $c_0=0$ and keep $c_s$ from (28). For every fixed $l\ge0$,
\[
 \left\|\beta Q B_1^*D^l B_1 Q-d_l Q\right\|\to0,\qquad
                 d_l=2c_{l+1}-c_{l+2}-c_l\ge0 .                            \tag{31}
\]
Expand $W_\gamma^*F_{xy}^sW_\gamma$ by recording which of the $s-1$ intermediate fibres lie in $\Pi_1$. Paths with at least two distinct excursions have norm $O_s(\beta^{-2})$ together by the bound on $B_1$, since all diagonal components are contractions. The term with no excursion is $A^s$. Those with one excursion are $A^i B_1^*D^lB_1 A^{s-l-2-i}$ for $0\le l\le s-2$, $0\le i\le s-l-2$. Globally $A=U-S_1(X_D)/\beta$ with $\|S_1(X_D)\|\le C_\gamma$ by the one-step shelling bound. Expanding $A^s$ to first order therefore has norm error $O_s(\beta^{-2})$. In the first-order terms each fixed power of $U$ on $Q$ differs from identity by $o(1)$. Using (28) at times $1,s$ gives
\[
 \left\|\beta\sum_{l=0}^{s-2}(s-1-l)QB_1^*D^l B_1 Q
                              -(s c_1-c_s)Q\right\|\to0 .
\]
Its second finite difference, including the trivial cases $s=0,1$, proves (31). Positivity comes from $D\succeq0$. The sequence $c_s$ is concave and $c_s/s\to c$ by (26), so $c_{s+1}-c_s\to c$ and
\[
                        \sum_{l=0}^\infty d_l=c_1-c .
\]
For a nearest-neighbour pair $d_l=3 b(l+1)$ by the temporal–spatial complement used in (16). The sum then equals $1/4$.

**PROVED (the entire leading self-energy correction).** Now assume $1-h_j=o(1/\beta_j)$ as in (27), put $r=r_{xy}$, and retain $Q=Q_{h_j}$. Then
\[
 \begin{split}
 &\left\|\beta Q B_1^*(r-D)^{-1}B_1 Q-(c_1-c)Q\right\|\to0,\\
 &\|(r-D)^{-1}B_1 Q\|\to0 .                                                 \tag{32}
 \end{split}
\]
Indeed (30) gives the upper form bound $Q B_1^*(r-D)^{-1} B_1 Q\preceq Q(r-A)Q$. By (25), (28) and $\beta(1-h_j)\to0$, its right side is $[(c_1-c)Q+o(1)]/\beta$ in operator norm. For a lower bound use the positive terms of the inverse series through $l=K-1$. After multiplication by $\beta$ their sum tends in compressed norm to $\sum_{l<K}d_l$ times $Q$ for each fixed $K$, since $r\to1$. The sum over all limiting coefficients attains the upper bound. This proves the first limit, and yields
\[
 \limsup_j\ \beta\|Q B_1^*(D/r)^K(r-D)^{-1}B_1Q\|
                    \le \sum_{l\ge K}d_l .
\]
This controls the possible loss of weight from return times growing with the cutoff. By (29) the distance $r-\|D\|$ is at least $c_z/\beta$ with $c_z>0$ for large $j$. For $0\le x\le\|D\|$ use
\[
 (r-x)^{-2}\le (K/r)(r-x)^{-1}
                +(r-\|D\|)^{-1}(x/r)^K(r-x)^{-1}.
\]
After compression by $B_1 Q$, the first term has norm $O(K/\beta)$ and the limsup of the second is bounded by $c_z^{-1}\sum_{l\ge K}d_l$. Sending $K\to\infty$ proves the second assertion of (32). In particular the derivative of the compressed Schur correction has vanishing norm at $r=r_{xy}$. The common one-step correction at order $1/\beta$ is thus exhausted by the individual return-time coefficients, even if the physical band has growing rank.

## What survives at physical energy resolution

**PROVED.** Let $r=r_{xy}$ and let $Q$ project on any neutral band $[h_j,1]$ with $1-h_j=o(1/\beta_j)$. For every fixed $E_0<\infty$ the energy dependence in the neutral operator (30) satisfies
\[
 \sup_{|E|\le E_0}\frac{\|Q[H(r-a_j E)-H(r)]Q\|}{a_j}\longrightarrow0 .     \tag{33}
\]
In fact $\operatorname{dist}(r,\sigma(D))\ge c_z/\beta$, and $a_j\beta_j\to0$. Thus $\|(r-a_jE-D)^{-1}B_1 Q\|\le (1-a_j E_0\beta/c_z)^{-1}\|(r-D)^{-1}B_1 Q\|$ by functional calculus, uniformly on the indicated interval. The resolvent identity and (32) prove (33). This conclusion is at physical resolution and is uniform over the whole specified band.

**PROVED.** At the central parameter, (25), (28) and (32) give only
\[
 \left\|Q\big[(rI-H(r))-(I-U)\big]Q\right\|=o(\beta_j^{-1}).               \tag{34}
\]
Indeed the three leading terms in the difference are $-c$, $c_1$ and $-(c_1-c)$ in units $1/\beta$. For a neighbouring pair they are $-1/2$, $3/4$ and $-1/4$. Equation (33) controls variation with the external spectral parameter. Improving (34) to $o(a_j)$ would require control of the residual that varies across neutral states at the *fixed* parameter. Even such a comparison would still require a bound on the spectrum or trace of one of the two resulting neutral operators.

**PROVED (subtracting the exact charged ground energy).** There is also an exact physical-energy comparison without a weak-coupling subtraction. Choose a top charged vector $A_*$ real in the quaternionic coordinates. This is possible since the transfer and the equivariance conditions preserve the real quaternion four-plane and its complexification is the whole matrix fibre. Define the real signed measure
\[
 d\zeta_*=k_0(X,Y)\,
  \operatorname{Re}\langle A_*(X),
    \mathbb E[g_x A_*(Y)g_y^{-1}\mid X,Y]\rangle\,dX\,dY .
\]
It is symmetric by reversal of the transfer. Its marginal is $r\|A_*(X)\|^2dX$ by the eigenvalue equation. For every bounded invariant scalar $\rho$, centre neutral in the restricted sector,
\[
 \langle \rho A_*,(rI-F_{xy})\rho A_*\rangle
        =\tfrac12\int|\rho(X)-\rho(Y)|^2\,d\zeta_* .                        \tag{35}
\]
Expanding the square gives the two diagonal terms from the marginal and the two conjugate off-diagonal terms from the charged kernel. The corresponding exact neutral form for $\rho\psi$ uses $k_0(X,Y)\psi(X)\psi(Y)dX\,dY$ and $r=1$. The total variation of $\zeta_*$ is dominated by the positive scalar pair measure with both $\psi$ factors replaced by $\|A_*\|$. Retaining $1-\omega(\mathrm{all})$ in the proof of (29) yields $\beta[1-\langle\|A_*\|,U\|A_*\|\rangle]\to0$ because this nonnegative contribution adds to the resistance lower bound attained in (25). Thus the modulus is itself almost invariant in these units. Equations (29) and (35) give no uniform comparison of the two forms on centred tests with energies of order $a$.

**OPEN.** On a fixed admissible cube the missing estimate is still a bound on the entire neutral excited trace at time $\lfloor n/K\rfloor$. For the continuum alternative one needs a common positive lower edge on a total gauge-invariant observable domain in a constructed, identified nontrivial four-dimensional theory. The estimates above determine the static self-energy and its colour dependence and control the spectral-parameter error in (33). They leave the state-dependent neutral spectrum at physical resolution undetermined. Row 1231's transported-curvature argument is used in its stated finite-window scope. This research note has no independent check or status consequence.

RESULT: OPEN for the Jaffe–Witten mass gap. The finite-lattice argument gives the static-pair threshold (25), its multiplicity comparison (27) and the physical-energy estimate (33). The neutral excited trace and the continuum mass bound remain open.
