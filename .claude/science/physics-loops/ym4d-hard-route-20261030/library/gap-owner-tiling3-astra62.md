# Repo search

**GUIDE.** FINISH row 1301 at `523d7b288`. The lead’s November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its thirteen targets concern the existence construction. The target-specific prior file is absent. I checked the open registry, those branches and PR 10144 for this tiling. The registry assigns no competing row and the branch search returned no independent derivation of the eight-flux comparison. [Lead’s repo search](prior/repo-search-2026-11-08.md) · [Open registry](open-registry.md)

**GUIDE.** The closest PR hit, Codex’s one-step lower bound for a plaquette convolution form, gives a local transfer estimate. The main-branch thermal criterion relates the full trace on one physical cube to its doubling defect, conditional on its inputs. Two more distant main-branch hits treat a finite-clock Villain law and determinant-weighted Maxwell covariance. Both concern abelian fields. [PR 10114, lines 106–149](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L149) · [Physical thermal criterion, lines 311–321](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/research/mass-gap/library/gap-phys-seed.md#L311-L321) · [Finite-clock Villain law](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md) · [Determinant-weighted model](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md)

**GUIDE.** In this checkout row 1274 proposes trading colour for translations. Row 1215 evaluates the periodic Wilson vacuum and one elementary magnetic twist. I use its localization argument, the rectangle determinant of rows 1143–1145 and the periodic spectral bounds of rows 1147 and 1227. [Colour and translations](gap-owner-movingsites-opus.md) · [Wilson flat limit, (2)–(8)](gap-solve23-astra62.md) · [Hand check](gap-solve23-check-opus.md)

## The owner’s tiling question

**GUIDE.** The test is whether the noncommuting directions in a tile can preserve a fixed fraction of its neutral gap on the assembled cube. I use the eight spatial twists of Gerard ’t Hooft to match the doubled cube’s momenta, compare the resulting Wilson traces, and then restore the fundamental plaquettes across the interfaces. All new arguments below are by hand. They are the author’s results for row 1301, await independent checking and grant no scientific status.

**GUIDE.** Rows 1273 and 1279 give a singlet gap $\kappa_r g^{2/3}/\ell$ for $r\ge2$ freely varying colour vectors on a single reduced block of side $\ell$. For $r=1$ the free radial motion has no positive gap. This uses Barry Simon’s oscillator method and the small-volume work of Martin Lüscher, Gernot Münster, J. Koller and Pierre van Baal. For $N^3$ blocks, row 1286 and check 1287 give $\kappa_r g^{2/3}/(N\ell)$ asymptotically for tree and common-frame stiff sewing at fixed $N$. For cyclic adjoint sewing they give an upper bound and a count of soft levels. [Reduced oscillator and its check](gap-threeaxis-check-astra.md) · [Sewing check](gap-owner-tiling-check-opus.md) · [Small-volume literature](prior/gap-small-volume-lit.md)

**GUIDE.** Row 1285’s identical-tile estimate incurs a Casimir defect. Check 1292 showed that this does not close the route. In particular row 697, Lemmas K, X and E, controls the defect by the *full* trace at a shorter time, including the inequality $(b-a)\kappa(b)\le\log(1+S(a;b))$ for $a<b$. Row 1291’s unchecked argument from Lemma CR retains a vacuum term for identical tiles. Its argument leaves open the comparison between distinct magnetic fluxes tested here. [Check of the Casimir comparison](gap-owner-tiling2-check-astra.md) · [Shorter-time comparison](gap-crux-restate.md) · [Lemma CR](gap-mini-solve-ar-opus.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the positive Wilson transfer and the finite-torus slab inequality. Their flat-background argument uses adjoint character shifts for the constrained classical operator. Their outline calls the physical gap a “separate spectral estimate”. CA-I 2698–2711 explicitly excludes it from the stated conclusion. The outline index entries used here are in chunks 01–03, 08–09 and 29 and the obligations list. The CA-I 4.12–4.19 index concerns preparation and stage admission. [Outline GL3, GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197-L2335) · [AM6](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2885-L2942) · [Flat shifts](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L9558-L9573) · [Gap scope](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L4630-L4643) · [CA-I, lines 2698–2711](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2698-L2711)

**OPEN (physical conclusion).** The eight magnetic sectors reproduce the leading vacuum energy on the doubled cube. Neutral projection leaves a calculable discrepancy in its trace. The outstanding estimate for a tile of fixed positive physical width concerns the fundamental plaquettes across its faces, as expressed in (13).

## The vacuum energy of eight different blocks

**GUIDE.** Put one copy of each magnetic flux on the eight tiles of a $2\times2\times2$ cube. Throughout, spatial sides $b$ and transfer times $t$ in lattice units are integers. The initial comparison keeps $b\ge3$ fixed while $\beta\to\infty$.

**GUIDE (Wilson transfer conventions).** Haar measure has mass one. For a quaternion $U\in\mathrm{SU}(2)$ write $w(U)=\tfrac12\operatorname{Tr}U=\operatorname{Re}U$. On a spatial slice set $V_m(X)=\sum_p[1-\eta_p w(X_p)]$, where $X_p$ is the ordered plaquette product and the fixed central signs $\eta_p=\pm1$ implement the spatial flux $m$. Write $M_m=\exp(-\beta V_m/2)$. The positive transfer on gauge-invariant functions is $T_m=M_m C M_m$, where $C$ convolves each link with $I_\beta^{-1}\exp[-\beta(1-w(U))]$ and $I_\beta$ is its unnormalized Haar integral. A spatial centre flip multiplies all links crossing one periodic cut by $-1$. These three commuting flips also commute with $T_m$. A neutral state is invariant under all three. The positive vacuum is unique. [Wilson transfer and positivity](gap-solve23-check-opus.md)

**PROVED (flat colour characters).** Write $D=\mathbb F_2^3$. A magnetic flux $m\in D$ specifies the alternating form $B_m(v,w)=\det(m,v,w)$ over $\mathbb F_2$. Flat seam holonomies have central commutators $(-1)^{B_m(e_i,e_j)}$. If $m\ne0$, take independent covectors $p,q$ spanning $m^\perp$. The form $p\wedge q$ equals $B_m$, since each descends to the unique nonzero alternating form on $D/\langle m\rangle$. With imaginary quaternion units $i,j$, take $h_k=i^{p_k}j^{q_k}$. These three adjoint rotations act by signs on $i,j,ij$, with characters $q,p,p+q$, respectively.

**PROVED.** These are the characters of every flat in that flux. Take two seam words for a pair of vectors having pairing one. The words anticommute. Each is conjugate to its negative, hence is a unit imaginary quaternion. Their anticommutator forces perpendicular axes. A word for a radical vector commutes with both and must be central. Products expressing the original seams in these generators agree up to central factors because their exponent vectors agree modulo two and every generator square is central. To see the latter directly, first pick an anticommuting pair among the original seams. The third seam commutes or anticommutes with each. Multiplying it by an appropriate product of the first two makes it commute with both. The resulting seam is central. Thus the three nontrivial characters are precisely $m^\perp\setminus\{0\}$. For $m=0$ row 1215 shows that central holonomies maximize the Gaussian transfer norm. They supply three trivial characters.

**PROVED (one doubling).** Let $E_m(b,\beta)=-\log\lambda^m_0(b,\beta)$ be the actual Wilson vacuum energy. Normalize electric convolution to have integral one. The discarded constant is proportional to the number of spatial links in the energy and cancels below. Put $f(k)=2\operatorname{arsinh}\sqrt{\sum_j\sin^2(k_j/2)}$ and
\[
 S_b(\theta)=\sum_{h\in\{0,\ldots,b-1\}^3} f((2\pi h+\theta)/b).
\]
At fixed $b$,
\[
 \lim_{\beta\to\infty}
 \left[E_0(2b,\beta)-\sum_{m\in D}E_m(b,\beta)\right]=0.                 \tag{1}
\]
Here $E_0$ denotes the *periodic flux sector*, and $\lambda^m_0$ denotes the largest eigenvalue in sector $m$. A spatial magnetic twist preserves positivity of the time transfer.

**PROVED.** Use the fixed-box localization argument of row 1215, (1)–(4). Its estimates use the curvature $\log(\eta_p U_p)$ near a signed flat, compactness, the same electric Gaussian, and the singular values of the linearized curl. Changing which stacks have signs $\eta_p=-1$ preserves these estimates because multiplication by a central sign is an isometry and the seam construction above supplies its flats. In a parallel frame the two transverse polarizations per colour give one copy of $S_b$ in the ground energy. Thus the limiting energy is $3S_b(0)$ for $m=0$, and $\sum_{p\in m^\perp\setminus\{0\}}S_b(\pi p)$ for $m\ne0$. Each nonzero $p$ is orthogonal to exactly three nonzero $m$, since its annihilator has four elements. The trivial character also occurs three times. Splitting the momentum index on side $2b$ into its three parities gives $\sum_{p\in D} S_b(\pi p)=S_{2b}(0)$. This proves (1) at every fixed side, before any large-$b$ limit. The same counting works for any function of the momentum. [Wilson localization and flat phases](gap-solve23-astra62.md)

**PROVED (size of the term cancelled).** For eight periodic blocks the limiting defect is strictly positive. Each $S_b(\pi p)-S_b(0)$ for $p\ne0$ is positive by the positive heat-kernel winding formula of row 1215, (4). More explicitly, put $A=3\pi^{-2}\sum_{z\in\mathbb Z^3\setminus\{0\}}|z|^{-4}$. The Fourier coefficient in row 1215, (7), gives $3S_b(0)=3b^3\widehat f(0)-A/b+O(b^{-3})$, with $\widehat f(0)$ the mean over the momentum torus. Summing its $O(|bz|^{-6})$ remainder over $z\ne0$ justifies the error. Hence
\[
 \lim_{\beta\to\infty}[E_0(2b,\beta)-8E_0(b,\beta)]
        =\frac{15A}{2b}+O(b^{-3}).
\]
Equation (1) pays this entire defect with $\sum_{m\ne0}(E_m-E_0)$ in this order of limits. It compares the leading values of finite-lattice Perron energies. It gives no rate for the error at finite coupling.

## Does the same combination carry the neutral trace?

**PROVED (failure for the fundamental Wilson law).** Let $D_m(t;b,\beta)=\operatorname{Tr}_{+}[(T_m/\lambda^m_0)^t]$. The subscript $+$ imposes Gauss's law and all three spatial centre flips. At every fixed $b,t\ge3$ the product undercounts the large-box trace. Its limiting deficit is the factor
\[
 \lim_{\beta\to\infty}
 \frac{D_0(t;2b,\beta)}{\prod_{m\in D}D_m(t;b,\beta)}
 = 2^{9/2}\prod_{m\ne0}\frac{Q_m(t;b)}{P_m(t;b)}
 >2^{9/2}.                                                             \tag{2}
\]
The same limiting ratio holds for the unnormalized neutral partition functions by (1). This counterexample involves the actual Wilson transfer on both sides.

**PROVED (periodic factor).** For a sign covector $p\in D$ put $q_{h,p}=(2\pi h+\pi p)/b$, with $h$ in the $b^3$ momentum cell, and $x_{h,p}=\exp[-t f(q_{h,p})]$. Set $Q_0(t;b)=\prod_{h\ne0}(1-x_{h,0})^{-6}$. The checked fixed-rectangle Wilson integral of rows 1143 and 1145 gives
\[
 D_0(t;b,\beta)\ \sim\
 C\,\beta^{3/2}\log\beta\, (b/t)^{9/2}Q_0(t;b).                       \tag{3}
\]
The constant $C>0$ is independent of the fixed rectangle. To track the normalization, equation (11) of row 1145 has bulk factor $A^{b^3t}$, power $\beta^{-(9b^3t-3)/2}$, and vacuum factor $\exp[-3tS_b(0)]$. The single-link normalization $I_\beta^{3b^3t}\sim A^{b^3t}\beta^{-9b^3t/2}$ removes the bulk. Dividing by the normalized Perron eigenvalue to power $t$ removes the vacuum factor by row 1215, (4). The neutral projector contributes $1/8$ to the leading coefficient because all seven nontrivial temporal-twist ratios vanish in this limit. Equation (3) keeps the singular constant-field integral that the transverse Gaussian alone omits. [Fixed-rectangle determinant and neutral projection, §4](gap-solve2-astra62.md) · [Check of the rectangle calculation](gap-solve2-check-opus.md)

**PROVED (twisted factors).** For $m\ne0$, let $C_m=m^\perp\setminus\{0\}$. Write
\[
 Q_m(\epsilon)=\prod_{p\in C_m}\prod_h(1-\epsilon_p x_{h,p})^{-2},
 \qquad Q_m(t;b)=Q_m(+,+,+),\qquad
 P_m(t;b)=\tfrac14\sum_{\prod_{p\in C_m}\epsilon_p=1}Q_m(\epsilon).
\]
Then $D_m(t;b,\beta)\to P_m(t;b)$. Here are the hypotheses for applying the twisted trace limit (8) of row 1215 to each flux. The flat locus is one orbit under gauges and the three flips. In open-cube gauge the anticommuting pair fixes an orthonormal frame, and the third seam is its prescribed quaternion word up to a sign. Centre flips absorb all remaining signs. The combined stabilizer acts on the transverse colours by the four sign triples of product one. Indeed a constant conjugation preserving each of two perpendicular axes up to sign lies in $\{\pm1,\pm i,\pm j,\pm ij\}$. Every such conjugation can be compensated by seam flips. No colour has a zero momentum. Thus the kernel of the curl at a flat consists precisely of orbit tangents, by the longitudinal/transverse decomposition at each nonzero $q_{h,p}$. The normal curl is injective. These are exactly the inputs to the normal-coordinate Gaussian and Hilbert–Schmidt convergence at fixed $b$ in row 1215, (6), (8). The two transverse oscillators give the exponent $-2$. Projection to invariants averages the four signs, yielding $P_m$. Each summand is positive and each nonidentity term is strictly smaller than $Q_m(+,+,+)$ at finite $t$. In particular $1<Q_m/P_m<4$. [Twisted trace and its hand check](gap-solve23-check-opus.md)

**PROVED.** Resolving the nonzero momenta of side $2b$ by their three parities gives
\[
 Q_0(t;2b)=Q_0(t;b)\prod_{m\ne0}Q_m(t;b).
\]
The exponent is $-6$ in every parity, since each nonzero parity occurs three times with exponent $-2$. Insert this identity and (3) into the left side of (2). The singular factor $\beta^{3/2}\log\beta$ cancels between the two periodic boxes. Its volume prefactor leaves $2^{9/2}$. Each individual twisted block has also projected out states counted by the large-box oscillator determinant. This proves (2). For fixed $t$, both the numerator and the denominator in (2) diverge, so subtracting one from the large trace and one from the entire product leaves the same limiting ratio.

**GUIDE.** The reflection estimate for identical periodic tiles, and the shorter-time crossing of row 697, remain available with their original full traces. Equation (2) tests using the seven noncommuting twists to remove the vacuum defect and then multiplying the neutral block traces at the same time. Even after the defect in (1) has cancelled, that product misses a calculable part of the Wilson trace.

## Repeated doublings and shorter observation times

**PROVED (a hierarchy with the same vacuum cancellation).** Fix $b\ge3$, $k\ge1$, $N=2^k$, and $b_j=2^j b$. Keep one periodic block at $b$ and all seven nonzero magnetic blocks at each $b_j$, $0\le j<k$. Their volumes add to $(Nb)^3$. Summing (1) at the $k$ sizes cancels the intermediate periodic vacuum energies. Multiplying (2) cancels their periodic traces. The limiting ratio is
\[
 N^{9/2}\prod_{j<k}\prod_{m\ne0} Q_m(t;b_j)/P_m(t;b_j).                \tag{4}
\]
The limit here is still taken for each *fixed* hierarchy. Telescoping introduces no estimate uniform in $k$ or in the cutoff.

**PROVED (time needed by a coefficient-one comparison).** More generally, take any fixed integer $N\ge2$. On the right use one periodic block of side $b$ at time $s(t)$ with $s(t)/t\to\alpha>0$. Adjoin any finite collection of nonzero magnetic blocks of fixed sides, each at an integer time tending to infinity with $t$. Any fixed positive powers of those factors are allowed. Call their product with the periodic factor $B(t,\beta)$. Then
\[
 \lim_{t\to\infty}\lim_{\beta\to\infty}
 \frac{D_0(t;Nb,\beta)-1}{B(t,\beta)-1}=(N\alpha)^{9/2}.              \tag{5}
\]
For each fixed $t$, equation (3) makes both vacuum subtractions negligible. At each fixed side all nonzero-frequency factors $Q_0$ and $P_m$ tend to one as their times increase. What remains is the ratio of the two powers $(b/t)^{9/2}$. This proves (5) without interchanging limits. In particular an upper comparison $D_0-1\le C_N(B-1)$ valid for all these times and couplings requires $C_N\ge(N\alpha)^{9/2}$. With coefficient one the largest permitted asymptotic time of the periodic tile is $t/N$. A coefficient proportional to tile count $N^3$ cannot retain a fixed positive $\alpha$ for all $N$. With no periodic tile at all, the denominator is bounded at each fixed time while the large periodic trace diverges. These obstructions concern the specified trace comparisons. Prefactors of sufficiently high polynomial degree are compatible with (5).

**PROVED (a shorter-time Wilson comparison).** The time loss in (5) is attained in the fixed-box limit for the dyadic hierarchy. Take $N=2^k\ge2$, $t$ a multiple of $N$ and $t/N\ge3$. Observe the periodic tile at $t/N$, and observe *every twisted tile* at $t/2$, irrespective of its side. For the product of these normalized neutral traces, denoted by $B_N(t,\beta)$, one has
\[
 R_N(t):=\lim_{\beta\to\infty}\frac{D_0(t;Nb,\beta)}{B_N(t,\beta)}
 =\frac{Q_0(t;b)}{Q_0(t/N;b)}
   \prod_{j<k,\ m\ne0}\frac{Q_m(t;b_j)}{P_m(t/2;b_j)}
 <1 .                                                                \tag{5a}
\]
Here $R_N(t)$ increases to one along the stated times. In particular $D_0(t;Nb,\beta)-1<B_N(t,\beta)-1$ at every fixed such $b,N,t$ and all sufficiently large finite $\beta$. The threshold may depend on all three parameters.

**PROVED.** In the normal oscillator at flux $m\ne0$ choose a real basis of the transverse modes. Let $\omega_h>0$ and $\chi_h$ be the frequency and stabilizer character of mode $h$, including multiplicities. An occupation list $n_h=2v_h+\delta_h$, $\delta_h\in\{0,1\}$, is invariant exactly when $\prod_h\chi_h^{\delta_h}=1$. Summing over the $v_h$ first gives the exact identity
\[
 P_m(u)=Q_m(2u)\!
 \sum_{\substack{\delta_h\in\{0,1\}\\\prod_h\chi_h^{\delta_h}=1}}
       e^{-u\sum_h\omega_h\delta_h}.
\]
The zero mask contributes one and every other term is positive and decreasing. Equivalently, doubling each occupation at time $2u$ embeds every mode configuration into a neutral one at time $u$ with the same weight. The periodic factor $Q_0(t/N;b)/Q_0(t;b)$ is a product of finite sums $\sum_{d=0}^{N-1}e^{-d\omega_h t/N}$ over the nonconstant periodic modes, by division of occupations modulo $N$. It is strictly greater than one and decreases to one. Apply (3) to the two periodic boxes. Their factors $(Nb/t)^{9/2}$ and $(b/(t/N))^{9/2}$ agree. The parity decomposition at each doubling cancels all other oscillator factors except those in (5a). The finite sums prove the asserted monotonicity, strict inequality and limit.

**PROVED (sharpness for each twisted oscillator).** If $\omega$ is its smallest oscillator frequency, the unrestricted trace has its first term above the vacuum at energy $\omega$. Every single quantum has nontrivial character. Two quanta in a lowest mode have trivial character, so the neutral trace starts at exactly $2\omega$. At large $t$, a comparison $Q_m(t)-1\le C[P_m(s(t))-1]$ with fixed $C$ and $s(t)/t\to\alpha$ therefore requires $\alpha\le1/2$. This is sharp for the limiting oscillator by the occupation identity. At fixed $b$ the spectral convergence on the twisted normal slice also gives $\lim_{\beta\to\infty}m_{m,+}(b,\beta)=2\omega$ for the true Wilson gap. The periodic neutral gap tends to zero by row 1215, (5). Together with (5) this accounts separately for the factors $1/2$ and $1/N$ in the positive comparison. At a doubling $N=2$ the whole right side uses half the observation time. [Fixed-box spectral limits](gap-solve23-astra62.md)

**PROVED (the last level of the hierarchy).** At side $b_{k-1}=L/2$, one constituent has a single elementary spatial twist. Its neutral trace has twenty Gaussian two-quantum levels of energy $4\operatorname{arsinh}\sin(\pi/L)$ in the fixed-side weak limit, by row 1215, (6)–(8). Take $L=2^k b$ large enough that $u=\lfloor L/512\rfloor\ge3$. Since $\operatorname{arsinh} x\le x$ for $x\ge0$ and $\sin x\le x$, this block alone contributes at least $20e^{-4\pi/512}>1/2$ above its vacuum in that limit. All the other trace factors are at least one. Replacing the whole hierarchy by its independent neutral blocks thus fails the one-cube thermal test even if its periodic constant modes are discarded. This estimate uses the elementary twisted sector in the *product*. It gives no lower bound on the physical trace by a comparison outside the limit proved in (2). [Twisted neutral multiplicity](gap-solve23-astra62.md)

**GUIDE.** Time $t/N$ in the small block converts a decay factor $\exp[-m_{\rm block} t/N]$ into an inverse-total-side rate for this kind of bound. A time-independent prefactor, however large at fixed $N$, disappears when taking the spectral $t$-th root. Thus (5) alone does not compare the first excited eigenvalues of two interacting Wilson boxes. The test is stronger for the thermal count at a prescribed time.

## Two checks on the regime and the sector projection

**PROVED (joint weak-coupling counterexample to a vacuum-only test).** Write $\Delta_{\rm mix}(b,\beta)=E_0(2b,\beta)-\sum_m E_m(b,\beta)$. There are actual isotropic Wilson cubes for which $b|\Delta_{\rm mix}|\to0$ while the large cube has arbitrarily many thermally unsuppressed neutral states at time $\lfloor2b/512\rfloor$. Take $b\to\infty$ and $\beta\ge(2b)^{32}$. Equation (16) of row 1215 approximates the periodic and elementary twisted Perron energy to $o(1/b)$ uniformly there. For the other magnetic signs, the only change in its estimates (17)–(18) is the approximation of a nearly flat triple by an exact one. Here are the details.

**PROVED.** Let the three seam words satisfy their prescribed commutation signs with chord errors at most $s$. Some pair anticommutes to this accuracy. By the quaternion estimate in that proof their real parts and the dot product of their imaginary directions are $O(s)$. Orthonormalization puts them within $O(s)$ of $i,j$ in a common frame. Let $\epsilon_1,\epsilon_2$ be the two prescribed signs for the third word $h$. Then $\|(\operatorname{Ad}i-\epsilon_1)h\|+\|(\operatorname{Ad}j-\epsilon_2)h\|=O(s)$ in the real quaternion space. These commuting involutions are diagonal on $1,i,j,ij$. Their joint eigenspace for the two signs is one of the four real lines. The distance to that line is $O(s)$, by applying the two orthogonal sign projections in succession. Since $h$ has unit norm it is within $O(s)$ of one of the two unit words on the line. This supplies the exact third seam with no loss of uniformity. The cap, differential and electric estimates of (16)–(18) involve only the norms of local group derivatives and the chord errors of signed plaquettes. They apply with the same bounds to these seven sign choices. Summing the eight $o(1/b)$ errors against the exact frequency count in (1) proves the assertion about $\Delta_{\rm mix}$. Equation (19) of row 1215 gives $(2b)m_{i,+}(2b,\beta)\to0$ for every fixed excited-level index $i$ throughout this range. Keeping any finite number of levels in the trace proves divergence. The range $\beta\ge(2b)^{32}$ is much farther into weak coupling than the proposed physical logarithmic trajectory. [Uniform Wilson estimates, (16)–(19)](gap-solve23-astra62.md)

**PROVED (keeping all electric charges changes the comparison).** Denote the gauge-invariant full trace in units of its own vacuum by $D_m^{\rm all}$. At fixed $b,t\ge3$, $D_0^{\rm all}/D_0\to8$ by the temporal projection used in (3). For $m\ne0$,
\[
 D_m^{\rm all}(t;b,\beta)\longrightarrow 2Q_m(t;b).
\]
Without the centre flips there are two flat gauge orbits. Indeed the eight possible seam signs are quotiented by the four conjugation sign patterns of the quaternion frame. The stabilizer in the ordinary gauge group is just its central pair, acting trivially on the normal coordinates. The two compact orbits have positive separation. In disjoint tubes the electric kernel between them is exponentially small in $\beta$, by its Gaussian bound at positive distance. The potential is bounded away from zero off the tubes. The same fixed-box Hilbert–Schmidt limit used for $P_m$ thus gives two identical Gaussian traces without the sign projection. The Perron normalization tends to the same value on the full and neutral spaces. This proves the formula, including its multiplicity two.

**PROVED.** Consequently the full periodic trace on side $2b$, divided by the product of the eight full traces on side $b$, tends to $2^{9/2}/2^7=2^{-5/2}$ in the fixed-box limit. The unnormalized full partition functions have the same ratio there. In particular (2) cannot be used to reject the full-trace upper comparison in this regime. The factors gained by including charges come from distinct electric sectors. They do not raise the neutral energy levels inside the periodic cube.

## A positive full-trace bound and its price

**PROVED (one exact Wilson fold).** Choose a spatial transfer direction $i$ of length $2b$. The two centre flips $C_1,C_2$ in the other two *spatial* directions commute with its transfer $T$. Write $P_q$ for their four joint character projections. With the other sizes fixed, set $Z_z(b)=\operatorname{Tr}(C^zT^b)$, $z\in\mathbb F_2^2$. These are ordinary Wilson partition functions with the indicated spatial twist stacks. Then
\[
 Z_0(2b)\ \le\ \sum_q[\operatorname{Tr}(P_q T^b)]^2
        =\tfrac14\sum_z Z_z(b)^2\ \le\ Z_0(b)^2 .                       \tag{6}
\]
For the first inequality, square the nonnegative eigenvalues in each charge sector before summing. Adding all cross products within that sector only increases the sum. The equality is orthogonality of the four sign characters. The last inequality uses $|\operatorname{Tr}(C^z T^b)|\le\operatorname{Tr}T^b$. This uses the ordinary transfer and the centre-twist identity of row 697. It is an arithmetic average with an untwisted summand.

**PROVED.** The middle expression in (6) lies between $Z_0(b)^2/4$ and $Z_0(b)^2$. Its logarithm divided by the *ordinary time length* therefore has the same infinite-time limit as the untwisted bound. Any finite repetition by positive averages which retains the all-periodic choice with time-independent weight $w>0$ still has a term $w Z_0(t;b^3)^8$ for a cubic doubling. After division by the large vacuum normalization, that term has exponential rate $E_0(2b,\beta)-8E_0(b,\beta)$ in $t$. Thus the cancellation in (1) cannot be obtained in that way. This argument grants no sign to the error in a different, correlated sewing. The short-time bound of row 697 is compatible with (6).

**PROVED (test of replacing the average by the mixed product).** Reflection positivity and positive fundamental SU(2) plaquette weights alone do not imply $Z_0(t;(2b)^3)\le\prod_m Z_m(t;b^3)$ for the full traces. Retain a coupling $\gamma>0$ on $12$-plaquettes and put zero coupling on the other orientations. Each spatial $12$-torus, independently at every time and third coordinate, now has the two-dimensional Wilson law. In normalized plaquette units its partition functions with either magnetic sign are
\[
 z_\pm(A)=\sum_{d\ge1}(\pm1)^{d-1}r_d^A,\qquad
 r_d=I_d(\gamma)/I_1(\gamma),\qquad A=b^2 .
\]
Indeed the character expansion of the normalized weight has coefficient $d\,r_d$ in dimension $d$ by GL3. Schur orthogonality on each edge identifies the dimensions of the two incident faces and contributes $1/d$. Each vertex leaves one index sum contributing $d$. Connectedness fixes a common dimension, and the torus has $V-E+F=0$. A negative face supplies $(-1)^{d-1}$. Absolute convergence follows from the factorial decay in GL3. The same nonnegative character expansion gives reflection positivity across link mirrors in this anisotropic model, with constant weight on each omitted plaquette. [Sussman–Alpoge GL3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197-L2231)

**PROVED.** As $\gamma\downarrow0$, $r_2\sim\gamma/4$ and $r_3\sim\gamma^2/24$. The series for $I_d$ gives $r_d\le e^{1/4}(\gamma/2)^{d-1}/d!$ for $0<\gamma\le1$. Thus the sum of the odd dimensions is $1+r_3^A+O(\gamma^{4A})$ and the sum of the even dimensions is $r_2^A+O(\gamma^{3A})$. Their difference of squares gives
\[
 \lim_{\gamma\downarrow0}
 \frac{z_+(A)z_-(A)-1}{r_2^{\,2A}}
       =2(2/3)^A-1<0\quad(A\ge2).
\]
The full mixed product on eight blocks is $[z_+(A)z_-(A)]^{4bt}<1$ for small positive $\gamma$. The doubled periodic partition function is $z_+(4A)^{2bt}>1$. The common bulk factors cancel exactly. Strictness persists for fixed $b,t$ when all omitted couplings become sufficiently small and positive, by continuity of finite Haar integrals. This is a counterexample to the replacement based on positivity alone. A comparison using equality of all six couplings could have a different answer. This example concerns unnormalized full traces. The time transfer at zero temporal coupling has rank one.

## Can the eight blocks be replaced by independent blocks of one size?

**PROVED (obstruction for arbitrary flat SU(2) seams).** Allow any flat projective SU(2) boundary triple on a tile, any choice of axes, and positive mixtures of such triples. Its three complex adjoint-colour characters define a probability measure on the three-torus of phases, with weight $1/3$ per character. Let $H=\{0,\pi\}^3$. Every such mixture $\mu$ satisfies
\[
             \mu(\{0\})\ \ge\ \tfrac12\mu(H^{\rm c}).                  \tag{7}
\]
For a commuting triple, simultaneous diagonalization gives $0,\theta,-\theta$, so the inequality holds. For a noncommuting projectively flat triple the quaternion calculation gives three order-two characters, so the right side vanishes. Averaging preserves the inequality. This includes commuting triples held away from their preferred periodic vacuum.

**PROVED.** When the side increases by any integer $N$, the periodic large-box adjoint field resolved by translations of one small cell requires the uniform measure $\nu_N$ on the $N^3$ characters of $(\mathbb Z/N)^3$. Write $d=\gcd(N,2)$. Only $d^3$ of them belong to $H$. Since the function $\mathbf1_{\{0\}}-\frac12\mathbf1_{H^{\rm c}}$ has range of length $3/2$, (7) implies
\[
 \sup_A|\mu(A)-\nu_N(A)|\ \ge\
       \frac{N^3-d^3-2}{3N^3},\qquad N\ge3.                           \tag{8}
\]
Indeed integration of a function valued in $[0,1]$ differs by at most the displayed supremum, by integrating its superlevel sets. After shifting and scaling the test function, (8) follows. Thus one doubling admits the exact character count (1), while a single-size positive mixture misses a definite fraction of the translation-character measure at larger multipliers. A nonzero magnetic parent presents the problem already on its next halving. Each parent character is a nontrivial sign in some direction. Every square root of that character then has phase $\pm\pi/2$ in that direction. The required child measure has all its mass outside $H$ and no zero character. The same test gives distance at least $1/3$. This concerns the joint translation characters. Matching just one numerical vacuum energy imposes a weaker condition.

**PROVED (exact link multiplication).** The $N^3$ sheets of a genuine periodic cover carry a copy of $\mathrm{SU}(2)^{N^3}$ on each base link. Base translations by a period permute the sheets transitively. A local smooth invertible change of group variables preserving products and inverses, with the same group at a base vertex, would give a Lie-algebra isomorphism intertwining the seam actions. The minimal nonzero ideals of $\mathfrak{su}(2)^{N^3}$ are its individual factors. Indeed bracketing a member with support in coordinate $d$ against elements supported only there gives a nonzero pure-$d$ element whenever that component is nonzero. Further brackets generate the simple factor. Thus every isomorphism permutes the set of factors. It cannot conjugate a transitive action on that set into twists each fixing every factor, for $N>1$. Changing the local frame changes a closed-period action by conjugacy at its basepoint and preserves this test. In particular the matching linear frequencies at $N=2$ do not arise from such a factorization of the Wilson gauge law.

**PROVED (which interaction the split misses).** At $N=2$ let $s$ label a sheet and choose $p\ne0$. Write $\chi_p(s)=(-1)^{p\cdot s}$. Give two link directions of an interior plaquette constant logarithms $v\chi_p(s)i$ and $v\chi_p(s)j$ on that sheet, using the same value on opposite parallel edges. Its Wilson action without $\beta$ equals $2\sin^4 v$ on every sheet because the real part of the quaternion commutator is $1-2|\operatorname{Im}A\times\operatorname{Im}B|^2$, with $A,B$ the two exponentials. In each nonzero-flux block the $p$-space has at most one real colour axis, and in the periodic block it is absent. Under any linear splitting respecting these characters, the two $p$-components therefore commute on each separate block. Its corresponding interior plaquette has zero action. In the actual sheet algebra $[\chi_p i,\chi_p j]=[i,j]$ has trivial translation character. The interaction between two nontrivial modes acts directly in the spatially periodic channel. The example is a local action calculation, before integration over links or projection onto physical states.

**PROVED (no local sign repair).** Conversely fix a nonzero-flux block with independent characters $p,q$, and take $\eta\notin m^\perp$. In any invertible linear character splitting choose colours $u,v$ whose projections on this block's $p,q$ lines are nonzero. On the sheets take
\[
 X(s)=\chi_p(s)u+\chi_{q+\eta}(s)v,\qquad Y(s)=\chi_\eta(s)X(s).
\]
The two exponentials in directions 1 and 2 commute on each sheet. In the selected block only the $p$ term survives from $X$, and only the $q$ term from $Y$. These lie on perpendicular quaternion axes. At a sufficiently small common nonzero amplitude its plaquette action is strictly positive. Thus even the sign of the local difference between sheet action and independent-block action depends on the fields. A bound obtained after integration might still exist.

## Neutrality imposed on the assembled product

**PROVED (a soft charged state of each twisted Wilson block).** Fix $b\ge3$ and $m\ne0$. Relative to the unique vacuum of this *fundamental* Wilson transfer, there is a gauge-invariant state of electric character $m$ with energy at most $C_b e^{-c_b\beta}$ for all sufficiently large $\beta$. Here $c_b,C_b>0$ can be chosen for the seven fluxes at that fixed side. This concerns energy *above the vacuum in the same magnetic flux*. The cost $E_m-E_0$ compared with the periodic vacuum is a different quantity.

**PROVED.** Label the two flat gauge orbits $\mathcal O_\pm$ by the cosets of $m^\perp$ in the eight seam flips. A flip $z$ acts on that label by $(-1)^{m\cdot z}$. Use the bi-invariant product metric on the finite spatial link manifold. The compact orbits have separation $d>0$. Take their open $d/4$-neighbourhoods $U_\pm$ and set $s=\mathbf1_{U_+}-\mathbf1_{U_-}$. This gauge-invariant function transforms by character $m$. On the complement of $U_+\cup U_-$ the magnetic potential $V_m$ has a positive minimum $v$. The normalized positive Perron function $\psi$ of $F=M C M$, $M=e^{-\beta V_m/2}$, obeys $\|\mathbf1_{(U_+\cup U_-)^c}\psi\|_2\le e^{-\beta v/2}/\lambda^m_0$, by the eigen-equation and contractivity. The limit of $\lambda^m_0$ is positive at fixed $b$ by (1)'s proof.

**PROVED.** The stationary law of the two ends of a step has density $\psi(X)F(X,Y)\psi(Y)/\lambda^m_0$ in Haar coordinates, with marginals $\psi^2$. Its probability of an endpoint outside the two neighbourhoods is $O_b(e^{-c_b\beta})$. A jump between the two neighbourhoods has product distance at least $d/2$. The sum of the one-link electric deficits is then bounded below by a positive constant, since $1-\cos r\ge 2r^2/\pi^2$ on $[0,\pi]$. The electric density on such a pair is at most $C_b\beta^{9b^3/2}e^{-c'_b\beta}$, from the one-link cap lower bound on $I_\beta$. The magnetic factors are at most one and $\|\psi\|_1\le1$, so the probability of these jumps is also exponentially small. The Dirichlet form of $1-F/\lambda^m_0$ on $s\psi$ equals half the mean of $|s(X)-s(Y)|^2$ under this law. Its norm squared tends to one, and the form is $O_b(e^{-c_b\beta})$. The variational principle in character $m$, followed by $-\log(1-x)\le2x$ for $0\le x\le1/2$, proves the asserted energy bound. Row 1227 uses the sign trial for *periodic* winding sectors and obtains a different, square-root exponential there. The disconnected twisted flat orbits supply the stronger barrier here. [Periodic sign argument, (10)–(14)](gap-solve25-astra62.md)

**PROVED (fifteen soft neutral excitations).** Form the independent tensor product of the eight true $b^3$ Wilson blocks. Impose gauge invariance on each and the three centre flips *diagonally* on the product. Keep the periodic block in its vacuum. In each of the other seven blocks choose either its vacuum or its lowest state of electric character $m$. For a subset of chosen excitations $I$, the total charge is $\sum_{m\in I}m$ over $\mathbb F_2$. This map from seven bits onto three has kernel of size $2^4=16$. Different subsets give orthogonal product eigenstates, distinguished by individual block charges. Removing the vacuum leaves fifteen neutral excitations of energies at most $7C_b e^{-c_b\beta}$. Relabelling the global flip directions on individual blocks still gives a map of rank at most three and hence at least fifteen such excitations. The all-vacuum tensor is the product's neutral vacuum.

**PROVED (loss of the one-block gap).** The periodic Wilson block itself has neutral gap at least $\exp[-C_b\beta^{1/4}(1+\log\beta)]$ for fixed $b\ge3$, by the bounded-action path estimate (11) of row 1227. Thus the ratio of the diagonally neutral product gap to the *actual* periodic block neutral gap tends to zero as $\beta\to\infty$, already on one doubling. It also tends to zero compared with the reduced oscillator's $\kappa_r g^{2/3}/b$ under the Wilson scaling $g\asymp\beta^{-1/2}$. The symmetry used here is the electric flux of a whole Wilson block. [Fixed-box gap estimates](gap-solve25-astra62.md) · [Check of (11) and (14)](gap-solve25-check-opus.md)

**PROVED (a time window that distinguishes the products).** Fix $1/4<\gamma<1/2$ and $t_\beta=\lfloor\exp(\beta^\gamma)\rfloor$. At fixed side $b$ or $2b$, row 1227, (14), gives limiting trace one in *each* of the eight periodic electric sectors in vacuum units. In a nonzero magnetic block exactly two full levels contribute in this window, one in charge zero and one in charge $m$. Indeed the two Gaussian tube limits above each have simple top and their next eigenvalue is separated at this fixed $b$. The Hilbert–Schmidt convergence on the two tubes and exponentially small exterior error give, by min–max, a uniform positive gap above these first two levels at large $\beta$. Their charges follow from the preceding trial. The second energy times $t_\beta$ tends to zero. The trace of the remaining powers is bounded by $D_m^{\rm all}(3;b,\beta)e^{-(t_\beta-3)d_b}$ with $d_b>0$, and the first factor has a finite limit. For each of the $2^7$ choices in the twisted blocks exactly one periodic electric charge cancels the sum. Since the number of factors is fixed, contributions containing a remaining level vanish by the full trace bounds on the other factors. Consequently
\[
 D_0(t_\beta;2b,\beta)\longrightarrow1,\qquad
 \operatorname{Tr}_{\rm diagonal\ neutral}
       \bigotimes_{m\in D}(T_m/\lambda^m_0)^{t_\beta}
       \longrightarrow 128 .                                           \tag{9}
\]
If neutrality is imposed separately, the product trace tends to one in this window. Equation (2) concerned a fixed time and has a different order of limits. Thus both the projection and the time scale affect a proposed spectral sewing.

## Interactions between tiles that preserve their separate centre flips

**PROVED (the soft states persist with genuine seam interactions).** Keep the eight fixed-size link sets above and let $V=\sum_m V_m+W$, where $W$ is a nonnegative $C^2$ interaction between tiles. Require $W$ to vanish at some tuple of signed flat fields, to respect vertex gauges on each tile, and to preserve each tile's spatial centre flips separately. Give all links the usual normalized Wilson electric convolution $C$ and set $F=e^{-\beta V/2} C e^{-\beta V/2}$. The operator can couple the tiles. Its diagonally neutral sector still has at least fifteen excitations of energy at most $C_{b,W}e^{-c_{b,W}\beta}$ above its vacuum for all large $\beta$. For example, a positive multiple of the squared difference of two signed fundamental plaquette traces on opposite sides of a tile interface is an allowed interaction. Such terms need not factorize.

**PROVED.** At the common zero the smooth nonnegative potential has zero derivative and lies below a constant times squared distance in a fixed chart. On a product cap of radius $c/\sqrt\beta$, the magnetic factors are bounded below. Between any two cap points each normalized electric density has a lower bound of order $\beta^{3/2}$. Testing with the normalized indicator of the cap costs one cap volume per link, of order $\beta^{-3/2}$. Thus $\lambda_0(F)\ge c_{b,W}>0$ uniformly for large $\beta$. The strictly positive kernel has a unique positive vacuum $\psi$, invariant under all the flips. Wherever one twisted tile lies outside its two neighbourhoods from the sign proof, $V\ge V_m\ge v_b>0$. The same eigen-equation and jump-tail bounds therefore give exponentially small stationary probability of a step that exits the good neighbourhoods or changes an orbit sign on any tile. Only seven tiles enter the union bound.

**PROVED.** Take the trial $s_I\psi$, $s_I=\prod_{m\in I}s_m$, for each of the sixteen masks of zero total charge. Its norm tends to one. Its normalized Dirichlet form is $O_{b,W}(e^{-c_{b,W}\beta})$, since $s_I$ changes only on one of the exceptional steps just bounded. Distinct masks have distinct characters under the independent tile flips, which commute with $F$. Hence both their scalar products and their mixed form entries vanish exactly. Min–max on this sixteen-dimensional space proves the count. Combined with row 1227, (11), it excludes a fixed fraction of the one-block Wilson neutral gap for this class, regardless of the strength of the fixed $W$. Sewing fundamental links into a single periodic Wilson cube can break the individual tile flips. A plaquette across a seam can contain just one link of a tile’s flip while the rest are on another tile. The independent characters used for orthogonality then cease to be symmetries.

**PROVED (when locality preserves the obstruction).** Suppose a term of $W$ is invariant under the vertex gauges of every tile. On each tile suppose the subgraph of links it reads has no cycle of odd winding in any spatial direction. Then this term preserves every tile flip. Indeed the flip is a fixed edge-sign cochain. Its product around each cycle of the subgraph is one, by the winding assumption. In each connected component choose a root and give a vertex the product of signs along a path from that root. Cycle triviality makes this independent of path. The corresponding central site gauge has exactly the flip signs on the links read by the term. Extend the gauge arbitrarily to the other sites. Gauge invariance proves the assertion even when the term involves several tiles. Thus couplings of contractible observables on independently gauged tiles fall under the fifteen-state obstruction whenever the common flat minimum and positivity conditions on $W$ hold. Genuine cross-face Wilson plaquettes use a different gauge identification.

## A restriction on physical tilings with microscopic constituents

**PROVED (conditional on one finite-energy witness).** Let $a_j\downarrow0$, $n_j=L/a_j$ at a fixed admissible physical side $L$, and let $\beta_j\to\infty$ with $\beta_j=O(\log n_j)$. Suppose the periodic Wilson cylinder on that box has a centred neutral vector with positive diagonal correlations $G_j(s)$ at two integer times. Assume the later correlation divided by the earlier is at least $\rho$, where $0<\rho<1$, with the times separated by at least $\tau/a_j$ for fixed $\tau>0$. Here $G_j(s)=\langle v_j,(T_0/\lambda^0_0)^s v_j\rangle$, and $v_j$ may depend on $j$. For any fixed $B\ge3$,
\[
 \frac{m_{+,j}(n_j)}{\min_{3\le b\le B,\ m\in D}m_{m,+}(b,\beta_j)}
       \ \le\ \frac{L\log(1/\rho)}{\tau n_j}
                 \exp[C_B\beta_j^{1/4}(1+\log\beta_j)]
       = O(n_j^{-1+o(1)}).                                             \tag{10}
\]
All energies here use the same lattice time step. The estimate compares the actual Wilson spectra, independently of how a proposed assembly represents the final box.

**PROVED.** By the spectral theorem the correlation ratio is at most $\exp[-m_{+,j}(n_j)\tau/a_j]$. This gives the numerator bound from an *upper* energy witness. The periodic constituent lower bound is row 1227, (11). In each of the seven twisted sectors the neutral Gaussian limit has a unique vacuum and a strictly positive first energy at any fixed side, by the injective normal curl and the stabilizer projection above. Taking minima over finitely many sides and sectors supplies the denominator bound in (10). The exponent in (10) is $o(\log n_j)$. In particular a fixed fraction of the neutral gap on a tile of bounded lattice width cannot survive on a box with the stated nontrivial physical witness.

**GUIDE (where the hypotheses enter).** The logarithmic upper bound follows from $a_j=L_{\rm RG}^{-K_j}$ and $x_0-x_{K_j}\le B_\sharp K_j$ with $x_{K_j}$ in a fixed window, on the conditional first-passage flow of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Row 865 and its check give the needed finite-energy bound on the admitted multiples of the reference physical side under their reference two-point witness, depth, source-energy, face and volume-transfer hypotheses. In that statement $\rho=c_{\mathcal K}/(3C_{\mathcal K})$ and $\tau=3\mathsf d/2$. This note supplies neither those ultraviolet hypotheses nor a continuum construction. [RF24–RF25](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20781-L20801) · [CA-I witness](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2715-L2781) · [Conditional Wilson witness](gap-sdcyl-ca-astra.md) · [Check of its hypotheses](gap-sdcyl-ca-check-opus.md)

**PROVED (polynomial multiplicities do not repair this comparison).** Let $u_j=\lfloor n_j/512\rfloor$. Under the same witness the physical cube has
\[
 D_0(u_j;n_j,\beta_j)-1\ \ge\ \exp[-L\log(1/\rho)/(512\tau)]>0.
\]
For the microscopic neutral factors let $d_j$ be the minimum in (10). Their normalized one-step traces are bounded by $C_B(1+\beta_j)^{c_B}$. Indeed $M C M$ is a positive magnetic sandwich of the trace-class electric convolution, $\operatorname{Tr}(M C M)\le\operatorname{Tr}C$, its diagonal is bounded by $I_{\beta_j}^{-3b^3}$, and the finitely many Perron limits are positive. Projection can only lower this trace. Hence a microscopic factor's excited trace at $s\ge1$ is at most $C_B(1+\beta_j)^{c_B}\exp[-(s-1)d_j]$. If each observation time is at least $\eta u_j$ with fixed $\eta>0$, this tends to zero faster than every inverse power of $n_j$. The product of polynomially many such normalized traces minus one has the same property, using $\prod(1+x_i)\le\exp(\sum x_i)$. So does any convex mixture of them with the same uniform bounds, even after multiplication of its *vacuum-subtracted* value by a fixed power of $n_j$. This rules out a microscopic neutral-product upper estimate of that form on the physical trajectory with this witness. It does not decide whether the actual physical excited trace is below $1/2$.

## An explicit range of growing constituents

**PROVED (a uniform lower bound for the twisted neutral block).** There are absolute $c,C>0$ such that for $b\ge3$, $m\ne0$ and $\beta\ge C b^7$,
\[
 m_{m,+}(b,\beta)\ \ge\
 c\exp[-C\{b^{10}+b^3\log(2+\beta)\}].                                \tag{11}
\]
The rigid quaternion triple is important here. Small-curvature endpoints can be brought close in one electric step *in the neutral quotient*. The underlying good-set Dirichlet argument and the untwisted path estimate are from row 1147, §5. [Periodic paths and their check](gap-solve3-check-opus.md) · [Growing-box flat comparison](gap-solve23-astra62.md)

**PROVED.** Use electric normalization, let $E=3b^3$ be the number of spatial links, and write $F=M C_\beta^{\otimes E} M$. A product of caps of radius $c/\sqrt\beta$ about any signed flat gives $\lambda_0\ge e^{-C_0 b^3}$. Each of the $3b^3$ plaquettes costs at most $C/\beta$ there by the triangle inequality for four links. Each electric kernel on a pair of cap points is at least $c\beta^{3/2}$, and each cap has Haar measure at least $c\beta^{-3/2}$. These constants are independent of $b$. Let $D_*=\{\beta V_m\le H\}$ for $H=2C_0b^3+\log 32$. Every normalized eigenfunction $\phi$ with eigenvalue $\lambda\ge\lambda_0/2$ satisfies $\|\mathbf1_{D_*^c}\phi\|^2\le e^{-H}/\lambda^2\le1/8$. This is the eigen-equation and $\|C_\beta^{\otimes E}\|\le1$. The same bound holds for $\psi$, the vacuum.

**PROVED.** At an endpoint in $D_*$ every signed plaquette has chord error at most $u=\sqrt{2H/\beta}$. The comb construction at (17) of row 1215 puts each link within $C b^2 u$ of the three-seam representative built from its winding words. In the open cube the two ordered root paths to the ends of an edge differ, after appending the edge and any wrapping period, by at most $16b^2$ adjacent coordinate interchanges. An interchange incurs at most $u$. The one-edge strip never crosses two seams at once. Comparing the two orders of a pair of root periods instead tiles a $b$ by $b$ rectangle, whose central sign is the prescribed $\eta_{ij}$. This bounds the three signed commutation errors by $b^2u$. Set $r=C'b^{7/2}/\sqrt\beta$. For $\beta\ge Cb^7$ with sufficiently large $C$, $r$ is small. The joint quaternion sign projections in the proof of the uniform flat comparison move the seam triple by at most $C r$ to a flat triple. By a vertex gauge and a centre flip its flat representative is one fixed $A_m$. Hence each of two endpoints in $D_*$ can be brought within $C r$ per link of that same representative. The flips are essential here.

**PROVED.** Let $\overline F(X,Y)$ be the kernel averaged over the vertex gauges and three seam flips of $Y$. Simultaneous invariance lets us undo the change of frame at $X$. In the endpoint average, retain a successful flip and restrict each of $b^3$ site gauges to a cap of radius $c/\sqrt\beta$ about a successful choice. This has measure at least $(c\beta^{-3/2})^{b^3}/8$ and adds at most $2c/\sqrt\beta$ to each link displacement. For $X,Y\in D_*$ the two magnetic factors together are at least $e^{-H}$. The electric cost is at most $C\beta E(r+\beta^{-1/2})^2\le C b^{10}$, using $1-\cos v\le v^2/2$ and equivalence of chord and geodesic distances on the unit sphere. Thus
\[
 \overline F(X,Y)\ \ge\
 (c\beta^{3/2})^E \exp[-C\{b^{10}+b^3\log(2+\beta)\}].
\]
Also $\|\psi\|_\infty\le e^{C_0b^3}(C\beta^{3/4})^E$, by the eigen-equation, Cauchy–Schwarz on the electric row, and $\|c_\beta\|_2^2\le\|c_\beta\|_\infty\le C\beta^{3/2}$ for the normalized one-link density. Since $\lambda_0\le1$, the stationary two-end measure on $D_*^2$ therefore dominates $e^{-C\{b^{10}+b^3\log(2+\beta)\}}\,d\pi(X)d\pi(Y)$, where $d\pi=\psi^2dX$.

**PROVED.** For a real neutral eigenfunction $\phi\perp\psi$ with $\lambda\ge\lambda_0/2$ apply the Dirichlet form to $\phi/\psi$. Against $d\pi\otimes d\pi$ on $D_*^2$ its value is $\pi(D_*)\|\mathbf1_{D_*}\phi\|^2-|\int_{D_*}\phi\psi|^2$. The two tail bounds and orthogonality give a lower bound $(7/8)^2-(1/8)^2=3/4$. Against the stationary measure the full form equals $1-\lambda/\lambda_0$. The domination just proved and $-\log x\ge1-x$ give (11). Eigenvalues below $\lambda_0/2$ already have energy above $\log2$.

**PROVED (physical implication with an explicit width).** In the periodic sector row 1147, (13), already gives $m_{\rm all}(b,\beta)\ge\exp[-C(b^8+b^{11/2}\sqrt\beta)]$, and even the full trace relaxes on the physical time scale when $b=o(\beta^{1/11})$. Use that result for $m=0$ and (11) for the other seven fluxes. For any width bound $3\le B_j=o(\beta_j^{1/11})$, both exponents are $o(\beta_j)$ uniformly for $3\le b\le B_j$. The one-step trace is at most $\exp[C b^3\log(2+\beta_j)]$ by the cap lower bound on the vacuum and the electric diagonal. Thus the argument of (10) gives
\[
 \frac{m_{+,j}(n_j)}
      {\min_{3\le b\le B_j,\ m\in D}m_{m,+}(b,\beta_j)}
       \le n_j^{-1+o(1)} .
\]
The same polynomial-product obstruction follows at times at least $\eta\lfloor n_j/512\rfloor$ because the negative exponent in each excited-trace bound has magnitude at least $n_j^{1-o(1)}$. The statement about the physical cube retains the finite-energy witness. The small-block lower bound (11) itself is unconditional. [Untwisted growing-box estimate, §5](gap-solve3-astra62.md)

## Restoring the fundamental seams

**PROVED (finite-period seam test).** The remaining change of gauge identification has an exact test on compact Wilson integrals. Denote the unnormalized centre-neutral traces by $Z_{m,+}(t;b)$. Put
\[
 A_\beta(t;b)=\frac{Z_{0,+}(t;2b)}{\prod_m Z_{m,+}(t;b)},\qquad
 J_m(t;b)=\log\frac{Z_{m,+}(t;b)^2}{Z_{m,+}(2t;b)} .
\]
Suppress $\beta$ on the right. Define $K_\beta=2\log A_\beta(t;b)-\log A_\beta(2t;b)$. Then
\[
 J_0(t;2b)=\sum_m J_m(t;b)+K_\beta .
\]
No vacuum-energy estimate is needed to use this identity. At every fixed $b,t\ge3$,
\[
                 \lim_{\beta\to\infty}K_\beta>\tfrac92\log2 .           \tag{12}
\]
Indeed the limiting *unnormalized* ratios are given by (2). For each $m\ne0$, $Q_m/P_m$ decreases to one as $t$ increases. To see this, divide each sign summand by $Q_m$. Every negative-sign factor contributes $[(1-x)/(1+x)]^2$, increasing with $t$. Thus twice the log correction at $t$ exceeds the one at $2t$ for each flux. This proves (12).

**PROVED (what the seam test measures).** Label the eight small cells by $d\in D$ and their sites by $x\in(\mathbb Z/b)^3$. Keep the same Haar link variables, indexed by the starting site, in both integrals. For independent blocks wrapping in direction $i$ keeps label $d$. In the actual doubled cube it changes the label to $d+e_i$. Use magnetic sign stacks on the independent tiles with $m=d$. Implement each neutral projection by averaging a temporal twist $z_d\in D$. On the large torus use just $z_0$ on its outer cuts and average the unused labels with unit total mass. Let $B_t$ be the large Wilson action minus the small-block sum, without the factor $\beta$. Identical interior plaquettes cancel. Only plaquettes touching a change of sheet or a changed twist stack remain. In the positive finite integral with interpolating action $S_{\rm small}+sB_t$ write $\langle\cdot\rangle_{s,t}$ for the expectation, including the auxiliary twists. Differentiating its log and integrating gives
\[
 K_\beta=-\beta\int_0^1
       [\,2\langle B_t\rangle_{s,t}-\langle B_{2t}\rangle_{s,2t}\,]\,ds . \tag{13}
\]
Both endpoints are the specified gauge theories. Differentiation at intermediate $s$ uses only finite positive integrals. The signed subtraction for a spatial cut is due to earlier rows 910 and 1147. Here the endpoints use all eight different magnetic tiles and (12) evaluates a nonzero part of their discrepancy. [Earlier spatial seam identity, §2](gap-solve3-astra62.md)

**PROVED (the price of shortening time on the actual seam).** For even $t\ge6$ let $u=t/2$ and $W_m=J_m(u;b)-J_m(t;b)$. These quantities are nonnegative at every coupling. Indeed $g(x)=\log D_m(x;b)$ is convex in real $x\ge3$ by Hölder’s inequality for the spectral weights. Its derivative is increasing, so $J'_m(x;b)=2[g'(x)-g'(2x)]\le0$. The exact identity is
\[
 J_0(t;2b)-\sum_m J_m(u;b)=K_\beta-\sum_m W_m .                      \tag{14}
\]
For fixed $b,t$ its weak-coupling limit is $2\log R_2(t)-\log R_2(2t)<0$ by (5a), since $R_2(t)<R_2(2t)<1$. In particular the positive discrepancy (12) at equal times can be paid for by the shorter-time trace in this regime. This result uses separate neutral projections on the actual Wilson blocks at both endpoints.

**PROVED (sufficient comparison for a gap fraction).** Fix a finite $b,\beta$ and suppose the signed seam integral (13) satisfies $K_\beta\le\sum_m W_m$ for all sufficiently large even $t$. Then
\[
 m_{0,+}(2b,\beta)\ \ge\ \tfrac12\min_{m\in D}m_{m,+}(b,\beta).       \tag{15}
\]
For a compact positive Wilson transfer with simple vacuum, its normalized trace is $1+d_1 e^{-x m_1}+o(e^{-x m_1})$ as $x\to\infty$, with $d_1$ the finite multiplicity of its first excited level. This expansion follows by bounding the tail beyond the first eigenspace with a fixed-time trace and the next distinct energy. Thus $J(x)=2d_1 e^{-x m_1}(1+o(1))$. Take the $t$-th root of (14)’s upper bound and let $t$ increase through the even integers. The slowest of the eight exponentials on the right gives (15). At each fixed $b$ the minimum on the right is the periodic block gap for all sufficiently large $\beta$, by the fixed-box spectral limits above. At positive physical tile width, comparison to the periodic tile alone also requires a lower bound on the seven twisted neutral gaps relative to its gap. Equation (5a) keeps $t$ fixed as $\beta$ increases. The hypothesis of (15) concerns arbitrarily large $t$ at the same $\beta$.

**OPEN (physical tiles).** For one fixed positive physical side $L$, take admissible $n_j=2b_j=L/a_j$, divisible by four, and $t_j=\lfloor n_j/512\rfloor\ge3$. The neutral one-cube requirement is $D_0(t_j;n_j,\beta_j)\le3/2$ for all sufficiently fine cutoffs. Using the last allowed time loses nothing by monotonicity. Positivity gives $\log D_m(t;b)\le J_m(t;b)\le2\log D_m(t;b)$ by $1\le D_m(2t;b)\le D_m(t;b)$. Thus an upper bound $\sum_m J_m+K_{\beta_j}\le\log(3/2)$ would suffice. A necessary condition is $K_{\beta_j}\le2\log(3/2)-\sum_m J_m$. In particular the residual at the physical coupling must fall below its fixed-mesh weak endpoint by at least $\tfrac92\log2-2\log(3/2)>0$. This conclusion compares two couplings at each fixed $(b_j,t_j)$ and keeps their limits in the order stated. The vacuum cancellation, separate-block gaps and sign-definite averaging above do not bound the signed integral (13) there. The microscopic comparison (10) does not cover $b_j a_j=L/2$. For a sufficient shorter-time test let $t'_j=2\lfloor n_j/1024\rfloor$. If $K_{\beta_j}\le\sum_m W_m$ at $t'_j$ and $\sum_m J_m(t'_j/2;b_j)\le\log(3/2)$, (14) proves the required bound by monotonicity. The estimates at this physical width, the all-large-time control for (15), and the continuum construction required by Jaffe and Witten remain open. [Physical neutral trace criterion](gap-mini-neutral-fable.md)

RESULT — OPEN. The four-dimensional SU(2) Jaffe–Witten mass gap remains open. In the weak-coupling limit at fixed lattice side and time, the eight magnetic sectors cancel the leading vacuum defect. The separately neutral product undercounts the doubled trace by a factor exceeding $2^{9/2}$. With only diagonal neutrality the seven twisted tiles carry at least fifteen exponentially soft neutral excitations, also for the stated interacting class. At half the time the separate-block upper comparison holds for fixed boxes at sufficiently weak coupling. Bounding the signed seam integral for all large times in (14), which would give the fixed gap fraction (15), remains open at positive physical tile width.
