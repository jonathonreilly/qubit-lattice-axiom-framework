# Repo search

**CITED.** FINISH row 1703, Codex laptop research note at `2e718fc6f`. The target-specific prior file was absent. Two bounded five-ref searches on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134` and `pr/10141` returned no Markdown or TeX hit for the target names, two-sheet Wilson transfer, endpoint orientation bias, oriented loop triple, neutral spectator, 625/457, six-end singlet or half-slab orientation. In that order the ref heads were `8b11ae2bb95e`, `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c` and `c73ad7b177d9`. A bounded search for thermal weight or overlap of a bare loop, packet or spin network, and for a Wilson segment at a free endpoint, also returned no lines. A file-scoped search for one-link multipliers, a physical Hilbert space and off-diagonal entries found the following related results.

- **CITED.** `docs/GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md`, lines 174–182, 200–208, gives the one-link multiplier $c_\lambda/(d_\lambda c_0)$ and a nonzero off-diagonal entry in its SU(3) finite-cube compression at isotropic coupling $10^{-14}$. Its companion `GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md`, lines 37–49, identifies the one-cube physical space as $L^2(SU(3)^5)^{\rm Ad}$ and the transfer as $M_{\rm sp}CM_{\rm sp}$. Neither estimates a packet at growing time.
- **CITED.** On PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 99–119, gives a conditional block density at least $\exp(-2\beta p_B-4\beta b)$ relative to Haar and the multiplier $r_f=I_2(\beta)/I_1(\beta)$ for SU(2). The first bound deteriorates with the number of links in the block. Lines 120–130 give eigenvalue $r_f^b$ for a simple $b$-edge loop under normalized convolution. Its review uses this local witness. The 8 November search digest identifies the same primary file on PR 10133. These are one-step inputs.
- **CITED.** Within the lane, row 1689 proves its conditional sign-path and frame lemmas, equations (4)–(7). Row 1683, `gap-purity-afield-astra62.md`, equations (12)–(13), bounds the overlap of a vacuum-dressed transport space with an excited band. Measurement A uses an unweighted subspace in slice Haar. Row 1145, `gap-solve2-astra62.md`, equations (1)–(2), bounds a long straight transport relative to Haar, even with the other links fixed. That estimate will be used below.
- **CITED.** The registry assigns R10 to the covariance of a Q2 posterior score, TWO-PER to a coupling derivative, and WMIX-SLICE to distances for a specified full two-slice law. None names the private-link reflection or the translated unweighted packet. The outline index has no hit for the endpoint or packet measurement. Its chunk 02, rows for GL3 and GL8, leads to the one-link spectrum and the untwisted trace in `YM4_sketch_500.tex`, lines 2195–2231 and 2313–2335. Chunk 29 and the matching obligations row lead to lines 31870–31883, which separate polynomial decay from a spectral gap. Credit for the outline and complete account goes to Sussman and Alpoge, with Claude and Codex, on Bałaban's method. The supplied source export is attributed to `31a47c543775`. CA-I, lines 2705–2711, explicitly leaves the mass gap and vacuum uniqueness outside Theorem 0.

**PROVED — Outcome.** On each fixed path, the terminal sign becomes insensitive to the starting sign. After the interior signs are summed, the other data retained at the first cut still distinguish the two starting sheets with error tending to zero at thermal endpoints. This refutes the common-centre hypothesis of row 1689 (5) with its two terminal weights. For A, even all translates together see a thermal mass smaller than every inverse power of $n$. Their normalized local shape can therefore earn only a vanishing part of the budget. The fully integrated column angle on the isotropic law remains open.

## Plan recorded at launch

**GUESSED — Work plan.** Check the target's prior-work note and ownership. Search the five named refs for the endpoint orientation and purity estimates. Record the statements and their hypotheses here.

**GUESSED — Proof plan.** Read the crux card, row 1689 and the fixed-lattice check. Recover the exact path law, scale, sign and size from their sources. Test measurement C on that law and price any proved bound in the purity budget. If an obstruction rules out C, apply the same test to A. Check each result against every Y4 item. No status is assigned.

**ARGUED — First decision.** For C the path variable includes the temporal links and the quotient of the private link on the first interior slice. Try to distinguish the starting rows using these variables with a common pinned terminal state. For A test the entire family of translates against the Wilson probability of one plaquette close to the identity. This tests the missing intensity in (6) even if the local frame has small minors.

## Law, scale and the part of C that contracts

**CITED.** Use the spatially weighted Wilson kernel $T_s$ of `Transfer.lean`, lines 508–555, 665–685. Its time plaquette on $e=(a,b)$ compares the bottom link with $g_a U'_e g_b^{-1}$. The neutral operator uses the mean $P_0$ of the eight electric cuts, periodic space and zero magnetic twist. Set $B=P_0T_s^r,\ r=u/2=n/1024,\ A=B^*B,\ Z=\operatorname{Tr}A,\ \rho=A/Z$. The sign paths and the packet below use this particular kernel. Row 1700, “Which operator and trace enter the test,” and `Stage3.lean`, lines 1573–1587, 1718–1732 and 3332–3343, identify the release and spatially weighted transfers as the two orders of a product with its adjoint, equivariant for the cuts. This identifies the nonzero neutral spectra and the purity. It gives no identification of the two operators' individual columns or packet compressions. All such observations here are made on the spatially weighted side of that trace identity.

**CITED.** Fix an admissible blocking factor $L$ and calibration $M,g_0$ among the witnesses supplied by the theorem at `PurIo.lean`, lines 389–405. Fix $s$ beyond the weak-scale range in row 1689 and $\ell=1024bs$ with fixed integers $s>0,\ b\ge2$. Put $n=\ell L^K,\ m=sL^K,\ \beta=\beta_K$. The theorem selects a subsequence of *every* infinite set of original cutoffs on which $\beta_K/(K\log L)$ tends to $11/(3\pi^2)$, with the calibration fixed. Thus the full sequence has that limit. Otherwise the complement of one neighbourhood would give a contrary infinite set. Row 1683 already makes this last observation. In particular $\beta\to\infty,\ m/(1+6\beta)\to\infty$. These choices precede all estimates and do not use a passing set.

**CITED — The marked triple (row 1689, Parts 2 and 4).** Take three based spatial squares with $m$ links on each side, in directions $(+1,+2),(-2,+3),(-3,-1)$ at their common vertex. Their holonomies are unit quaternions $U_i=(a_i,v_i)$. The sheet sign is the sign of $\det(v_1,v_2,v_3)$. At each fine slice keep every link except the private link $e$ of the third square. In place of that link keep $a_3$ and the projection of $v_3$ into the plane of $v_1,v_2$. The two signs give the two possible private links. The magnitude of the omitted normal component at cut $i$ is $h_i\le1$. At fixed quotient history sum the internal signs to form its positive two-by-two endpoint matrix $H_h$. Use

$$
 q(H)=\tanh\!\left(\frac14\left|\log\frac{H_{++}H_{--}}{H_{+-}H_{-+}}\right|\right),
 \qquad
 l_h=\frac12\sum_{t=\pm}\log\frac{H_h(+,t)}{H_h(-,t)} .
$$

**PROVED — Contraction on every history.** On the macroscopic triple of row 1689, choose one private link $e$ of the third loop. In its equation (4), $h_i h_{i+1}\le1$. Since $11/(3\pi^2)<5/12$, eventually $\beta\le(5/12)\log n$. On every cube and every nondegenerate fine quotient history $h$,

$$
 q(H_h)\le \exp[-2r e^{-2\beta}]
          \le q_K:=\exp[-n^{1/6}/512].
 \tag{1}
$$

Each history keeps the temporal links, the quotient at every fine slice and the closing twist. The two signs at each interior slice have been summed. The same statement holds for each of the eight seam twists. Against the reference $1/16$ the signed improvement $1/16-q(H_h)$ is at least $1/16-q_K>0$ at all late cutoffs. This pays the contraction term in row 1689 (5) down to $4\operatorname{artanh}q_K$, with zero excluded mass for (1). It supplies no bound on the centres. This calculation uses the simultaneous change of coupling, side and time. The fixed-lattice limits in rows 1696 and 1700 do not give (1).

## C. A common centre for the hidden paths

**PROVED — A necessary test with the terminal weights included.** Fix an initial two-sheet orbit $z$ and a terminal slice $y=(z',t)$. Let $\mathcal P_\sigma^y$ be the probability on the retained quotient histories with density $H_h(\sigma,t)/B(x_\sigma,y)$ against their common integration measure. Constants from Haar on the two signs can be absorbed into this measure. This is also the law obtained by drawing a full Wilson bridge from $x_\sigma$ to $y$ and erasing the interior signs. Let $G$ be a proposed common good set. If the hypotheses of row 1689 (5) hold, write $a=\delta+2\operatorname{artanh}q_0$. On $G$ the unnormalized row ratio lies between $e^{l(z)-a}$ and $e^{l(z)+a}$. After normalization *on $G$* the likelihood ratio is at least $e^{-2a}$. Each row gives $G$ mass at least $1-\eta$. The common mass $\int\min(d\mathcal P_+^y,d\mathcal P_-^y)$ is therefore at least $(1-\eta)e^{-2a}$. In particular

$$
 \|\mathcal P_+^y-\mathcal P_-^y\|_{\rm TV}
 \le 1-(1-\eta)e^{-2a}. \tag{2}
$$

TV is the supremum of the probability difference over events. Even a centre allowed to depend on $y$ must pass this test. It concerns the paths retained in C. WMIX-SLICE concerns the law of two complete endpoint slices.

**PROVED — The two history laws separate at thermally sampled endpoints.** Give the oriented initial slice $x$ and the terminal slice $y$ the probability

$$
 d\omega(x,y)=B(x,y)^2\,dx\,dy/Z .
$$

Write $x^\#$ for the other initial sheet. Off null sets this changes exactly one link, $e=(a,b)$. Draw one full bridge conditional on $x,y$. Erasing its interior signs gives $\mathcal P_x^y$. For the *same* $y$, also form $\mathcal P_{x^\#}^y$, with its own normalization. Take $\beta\ge1,\ m\ge4,\ r\ge2$ and $0<\kappa\le1$. Here $d_s=3$ is the spatial dimension and $j=2d_s-1=5$ counts the other spatial edges at vertex $a$. Use the constant from row 1689, proof of (11),

$$
 b_\beta=\frac{48+4\log(6\pi)+6\log\beta+\log8}{\beta}.
$$

Let $\xi_K=\sum_{d\ge2}d^2\exp[-(d-1)(m-2)/(1+6\beta)]$ from row 1145. Then

$$
\begin{aligned}
 \int \|\mathcal P_x^y-\mathcal P_{x^\#}^y\|_{\rm TV}\,d\omega
 &\ge 1-\Delta_K,\\
 \Delta_K &=
 32j^3 b_\beta/\kappa^2 + 4(1+\xi_K)\kappa
 +6\pi e^{(j+1)/2}\beta^{3/2}
      \exp[-\beta\kappa^2/(32(j+1))].
\end{aligned}\tag{3}
$$

Choose $\kappa=\min\{1,b_\beta^{1/3}\}$. The first two errors are then $O(b_\beta^{1/3})$ at all late cutoffs. The last is smaller, since $\beta\kappa^2\ge\beta^{1/3}$ there and an exponential in $\beta^{1/3}$ dominates every power of $\beta$. Thus $\Delta_K=O((\log\beta_K/\beta_K)^{1/3})\to0$. All three errors are uniform in the cube and in the chosen private edge. It compares actual Wilson bridges including both terminal normalizers. The event in its proof uses only the first fine step and the macroscopic petals at its two cuts.

**PROVED — A test visible after the signs are summed.** The first temporal links $g$ are among the retained variables. On the first interior slice the quotient gives the unordered pair of possible links at $e$. Transport them to the bottom as $V_1,V_2$, by $U\mapsto g_a U g_b^{-1}$. Use quaternion chord distance. Place the electric twist seam away from this step or its cut away from the star. For the fixed ordered comparison $x,x^\#$, define the event $E_x$ by two tests.

1. Each of the $j$ other first temporal plaquettes at $a$ has chord distance at most $\kappa/(4j)$ from identity.
2. Both $V_i$ have distance at least $\kappa$ from both $x_e^\#$ and $-x_e^\#$.

**PROVED.** All links needed for the first test are retained in both rows. The second uses the unordered pair, so neither test requires the erased sign. The time plaquettes in the first test are the same functions of the history for the two rows. Their bottom links agree off $e$. Site gauges multiply both candidates and the corresponding bottom link by the same left and right factors. The chord tests are therefore well defined also in based gauge coordinates.

**PROVED — Probability in the row from $x$.** Under $d\omega\,d\mathcal P_x^y$ a full first bridge has the marginal from the neutral Wilson trace at period $2r=u$. Indeed $B(x,y)B(y,x)$ sews two such bridges. Expand the two cut averages. Shift all slices on one half by one of the two cuts to combine them into a single twist. This is a product-Haar change of variables. The cut can avoid the marked loops and star. Each fixed signed face has mean deficit at most $b_\beta$. Row 1689 uses convexity to bound the expected sum of signed deficits by $n^3u\, b_\beta$. The $n^3u$ translates of each orientation have the same signed expectation. Moving a temporal seam through one layer flips the spatial cut links in the intervening layer. Moving the spatial location of that cut flips the temporal links on the intervening strip at the seam. Both changes preserve Haar and carry every signed face to the corresponding signed face. This proves the translation statement for temporal faces as well as spatial ones. Since the chord squared is twice the deficit, Markov's inequality and the union bound give probability at most $32j^3 b_\beta/\kappa^2$ for failure of the first test.

**PROVED — The alternative bottom link.** On the full sewn path, condition on all links except the $m-2$ interior links of a straight side of the *bottom* third petal. Choose a side not containing $e$ and away from its star. Each selected link occurs once. No face uses two selected links. This fixes the true $x_e$, both first-slice candidates, the temporal links, and the first two bottom holonomies. Choosing the third loop holonomy in place of $x_e$ is the isometry $U\mapsto D U^{\pm1}F$ on unit quaternions. Reflection of its vector in the first two vectors' plane pulls back to a reflection of the private link in a hyperplane of $\mathbb R^4$. Thus

$$
 x_e^\#=x_e-2(x_e\cdot N)N .
$$

The unit normal $N$ is the inverse image of the fixed unit normal $(0,\widehat{v_1\times v_2})$ under the isometry. The remote product enters just one of $D,F$, multiplied by fixed quaternions. As a function of that product, $N$ is a Haar-preserving isometry, possibly with inversion. Row 1145 (2), applied in each twist, bounds its conditional density above by $1+\xi_K$ relative to uniform measure on $S^3$. Degenerate triples have zero measure at finite $\beta$ by absolute continuity in slice Haar.

**PROVED — A cap estimate.** For uniform $N$, reflection of fixed $v\in S^3$ has density $1/|w-v|^2$ relative to uniform $w\in S^3$. To see this, take the sign of $N$ with $N\cdot v\ge0$, at angle $\theta$ to $v$. Its angular density is $(4/\pi)\sin^2\theta$ and its transverse direction is uniform. The angle of $w$ to $v$ is $\alpha=\pi-2\theta$, with density $(2/\pi)\cos^2(\alpha/2)$. Divide by the uniform density $(2/\pi)\sin^2\alpha$. A ball of chord radius $\kappa$ has maximal mass when centred at $v$. Indeed each superlevel set of the density is a concentric ball, and its intersection with a ball of the given volume has mass at most the smaller of the two volumes. At that centre the probability is $\Pr(2|v\cdot N|\le\kappa)\le(2/\pi)\kappa$, using the coordinate density $(2/\pi)\sqrt{1-t^2}$. Apply the upper bound $\kappa$ to the four balls about $\pm V_i$. The conditional cost of the second test is at most $4(1+\xi_K)\kappa$. This proof does not assume independence of a petal at the two times.

**PROVED — Probability in the row from $x^\#$.** Now pin both endpoints, start from $x^\#$, and restore the true interior signs temporarily. Condition on every variable except the first temporal link $g_a$. Its conditional Haar density is proportional to

$$
 \exp[\beta\,R\cdot g_a],\qquad |R|\le j+1.
$$

Only the $j+1$ temporal plaquettes on the spatial star use this link. Each contributes a dot product with a unit quaternion. For a unit vector $w$, the tangent gradient of $w\cdot g_a$ on $S^3$ has norm $\sqrt{1-(w\cdot g_a)^2}$. Inversion and left and right multiplication give the same formula for an incoming edge. On $E_x$ each of the $j$ other gradients has norm at most $\kappa/(4j)$. For the private plaquette the true $V_i$ is at distance at least $\kappa$ from both signs of $x_e^\#$. Thus $|V_i\cdot x_e^\#|\le1-\kappa^2/2$, and its gradient has norm at least $\kappa/2$ for $0<\kappa\le1$. The reverse triangle inequality gives $|\nabla(R\cdot g_a)|\ge\kappa/4$. This is the sign-sensitive step. The same test used only small deficits for the row from $x$.

**PROVED.** If $R=0$ this event is empty. Otherwise

$$
 |R|-R\cdot g_a\ \ge\
 \frac{|R|^2-(R\cdot g_a)^2}{2|R|}
 \ \ge\ \frac{\kappa^2}{32(j+1)} .
$$

The Haar ball of angular radius $\beta^{-1/2}$ about $R/|R|$ has probability at least $\beta^{-3/2}/(6\pi)$, by $\sin t\ge t/2$ for $0\le t\le1$. On it $R\cdot g_a\ge |R|-(j+1)/(2\beta)$. Comparing the integral on $E_x$ with this ball gives the last term of (3) as an upper bound for $\mathcal P_{x^\#}^y(E_x)$. It holds at each $x,y$ and twist, including when the alternative row is very unlikely before normalization. Sum the signs back out. Subtract this probability from the lower bound for the mean of $\mathcal P_x^y(E_x)$. The definition of TV proves (3).

**PROVED — Failure at the size needed in (5).** Write $o(x,y)=1-\|\mathcal P_x^y-\mathcal P_{x^\#}^y\|_{\rm TV}$. Formula (3) gives $\int o\,d\omega\le\Delta_K\to0$. With the constants of row 1689, (2) would give $o\ge c_*=(63/64)\exp[-1/8-4\operatorname{artanh}(1/16)]>0$. The signed discrepancy from that reference satisfies $c_*-\int o\,d\omega\ge c_*-\Delta_K$ on every late cube. More generally, even with varying constants, the right side of the common-mass bound in (2) is at least $e^{-D}$ for $D$ in (5) of row 1689. A set of endpoint pairs where the hypotheses give $D\le D_*$ has thermal probability at most $e^{D_*}\Delta_K$, for *any fixed* $D_*$. Thus neither the uniform test nor its version on a thermal fraction bounded below can give the proposed $1/16$ minor estimate by (5) of row 1689. Equation (1) shows that the obstruction persists when every path contracts. It is the common centre and its two terminal-weighted exceptional fractions that fail jointly.

**PROVED — What survives after integrating the paths.** The conclusion of row 1689 (5) alone measures the angle of $B(x,\cdot)$ and $B(x^\#,\cdot)$. The preceding test concerns the hypotheses that bound this angle. Integration can erase the evidence used by $E_x$. There is, however, a direct bound on the actual term in row 1689 (1). With $\pi(dx)=A(x,x)dx/Z$, $p(z)=\pi(+\mid z)$, and $v_x=B(x,\cdot)/\|B(x,\cdot)\|_2$, the Dirichlet energy of resampling this sign is

$$
 0\le D_{\rm sign}
 =\mathbb E_z\,2p(z)(1-p(z))(1-|\langle v_+,v_-\rangle|^2)
 \ \le\ 4b_\beta/t^2+4(1+\xi_K)t \quad(0<t\le1/2).
 \tag{4}
$$

To see this, use a spatial plaquette through $e$. The other three links determine the unique value $S$ of $x_e$ for which that plaquette is identity. Guess the sheet whose candidate is closer to $S$. The true value differs from $S$ by more than $t$ with probability at most $2b_\beta/t^2$. In the other case an error requires $|x_e-x_e^\#|\le2t$. The cap estimate in the preceding proof bounds this probability by $2(1+\xi_K)t$. The optimal error $\mathbb E_z\min(p,1-p)$ is at most this rule's error. Use $p(1-p)\le\min(p,1-p)$ and the unit upper bound for the squared sine. Taking $t=b_\beta^{1/3}$ at late cutoffs proves (4) tends to zero. The reason is that the other spatial links usually identify the occupied sheet. This bound retains the thermal weighting and measures no unweighted column angle.

**PROVED — Purity accounting for C.** Write $p_* =457/625,\ H=-\log p_*$. The sign heat bath fixes every function of the quotient, including a nonconstant trace of the first petal. Its scalar Poincaré gap is exactly zero. Hence it supplies no upper bound $D_{\rm sign}/\gamma$ on $1-\operatorname{Tr}\rho^2$. The path contraction paid in (1) is spent before integration. Equation (3) rules out the hypothesis that would spend it in row 1689 (5), including the stronger proposed bound $D\le1/\sqrt{2N}$ for a family of $N$ moves. The guaranteed credit toward $H=\log(625/457)$ from C alone is zero. A direct estimate on the integrated column angle, or an estimate after averaging out fine variables before imposing a common centre, would use a different hypothesis. Equation (3) does not refute either of those inequalities.

## A. The intensity of all translates

**CITED.** Let $W_x$ be the five-dimensional bare coefficient space of the three petals based at vertex $x$, and $P_x$ its Haar-orthogonal projection. In this section $x$ indexes a vertex. Row 1689 proves the frame identity, the mutual orthogonality of the $W_x$, and translation invariance in its Part 4.2. Put $P=\sum_x P_x,\ t_K=\operatorname{Tr}(P\rho)$. Its equation (6) gives $\operatorname{Tr}(P_x\rho)=t_K/n^3$. The question it leaves is whether $t_K$ is appreciable on the calibrated cubes.

**PROVED — The full translated packet loses its thermal weight.** For every such cube at $b_\beta\le1$ and $12m<n^3$,

$$
 0<t_K\le T_K:=\frac{4 b_\beta^{3/5}}{1-12m/n^3}.
 \tag{5}
$$

In particular $\sup_{\Gamma:\,\mathrm{side}=n}t_K\to0$. Thus a lower bound $t_K\ge c>0$ fails on all sufficiently late calibrated cubes, for every fixed $c$. In particular these packets cannot supply the proposed one-copy coverage $31/32$. Other families of channels are outside this estimate.

**PROVED.** Fix one fine spatial link $f$ and one plaquette $p$ through it. At most $12m$ translates use $f$. Indeed a translated edge of the same axis can equal $f$ for only one translation of its base, and the original packet uses $12m$ edges. All other packet functions are independent of the Haar variable $U_f$. Let $P'$ sum their projections and let $a$ be their fraction among all vertices. Then $a\ge1-12m/n^3$ and $\operatorname{Tr}(P'\rho)=a t_K$. This retains nearly the entire family using a single link.

**PROVED.** For $0<v\le1$, let $F$ be the event $1-\operatorname{Re}U_p\le v$, also denoting its multiplication projection by $1_F$. Conditional on the other links in *slice Haar*, $U_p$ is uniform on $S^3$. Its real coordinate has density $(2/\pi)\sqrt{1-z^2}$. Integrating from $1-v$ to 1 gives at most $(4\sqrt2/(3\pi))v^{3/2}\le v^{3/2}$. For every vector in the range of $P'$, integrate first in $U_f$. This proves $\|1_F P'\|_{\mathrm{op}}\le v^{3/4}$. In the *Wilson thermal slice*, the plaquette deficit has mean at most $b_\beta$, so $\operatorname{Tr}(1_{F^c}\rho)\le b_\beta/v$. Both conclusions hold for the same multiplication operator. Splitting the Hilbert–Schmidt product at $F$ gives

$$
\begin{aligned}
 \sqrt{a t_K}=\|P'\rho^{1/2}\|_{\rm HS}
 &\le\|P'1_F\|_{\rm op}\|\rho^{1/2}\|_{\rm HS}
       +\|1_{F^c}\rho^{1/2}\|_{\rm HS}\\
 &\le v^{3/4}+\sqrt{b_\beta/v}.
\end{aligned}
$$

Set $v=b_\beta^{2/5}$ and square. For strict positivity, the one-link convolution has positive multipliers in every spin by GL3. Its finite tensor product has zero kernel. The spatial multiplier is strictly positive with bounded inverse at finite cutoff. Both preserve the gauge and centre symmetries. The spatially weighted transfer on the neutral physical subspace is therefore injective and positive. Every nonzero vector of $W_x$ has positive quadratic form in its positive integer powers. This proves (5).

**PROVED — Independent bound from a free end of the slab.** There is a faster rate for these particular packets,

$$
 t_K\ \le\ 320 n^3\,e^{-2(m-2)/(1+3\beta)}\,
                   \langle 1,\rho 1\rangle
 \ \le\ 320 n^3\,e^{-2(m-2)/(1+3\beta)} . \tag{5a}
$$

Fix a unit vector $f\in W_x$ and pin the far endpoint $y$. Write $Bf(y)$ as a Wilson integral with insertion $f$. The near endpoint is free. It carries the spatial half weight. Mark the $m-2$ interior links of one straight side of one petal at that endpoint. At fixed unmarked data each has one full temporal staple and four half spatial staples. The tilt has norm at most $3\beta$. Each marked link occurs exactly once in the insertion, and their conditional laws factor. For the two-dimensional fundamental representation, row 1145 (1) gives its mean matrix as a scalar at most $e^{-1/(1+3\beta)}$ times a unitary fundamental matrix. For SU(2) the unitary here is itself a group element, by the translated central form of the tilt. Inverses give adjoints. Substitution into the multilinear insertion thus gives the product of these scalars times a possible value of $f$. The same free-end integration method appears in the open-cylinder sewing of `gap-solve40-astra62.md`, lines 258–274. There its observable is a coarse cut factor.

**PROVED.** The supremum of $|f|$ is at most 8. In the Haar-orthonormal basis of triple products of normalized fundamental matrix coefficients, the sum of squared basis values at a point is $4^3$, since $\sum_{ij}|\sqrt2 U_{ij}|^2=4$. Cauchy–Schwarz gives the bound on the invariant subspace as well. Thus

$$
 |Bf(y)|\le 8 e^{-(m-2)/(1+3\beta)} (B1)(y).
$$

Sum its squared $L^2$ norm over five orthonormal vectors and $n^3$ translates and divide by $Z$. This proves (5a), including at fixed small positive coupling as $m$ grows in proportion to $n$. It gives $t_K=o(n^{-A})$ for every fixed $A>0$ on the release trajectory. Equation (5) checks the loss by a different argument using only one fine plaquette and slice Haar.

**PROVED — Local minors and the log budget.** In a basis adapted to all the $W_x$ and $P^\perp$, write the global purity as a sum of squared matrix entries. Put $C_{\rm loc}=\sum_x\operatorname{Tr}[(P_x\rho P_x)^2]$, $p_{\rm rest}=\operatorname{Tr}\rho^2-C_{\rm loc}$ and $v_K=t_K^2/n^3$. Dimension five gives $v_K/5\le C_{\rm loc}\le v_K$, by the sum and sum of squares of five nonnegative eigenvalues per vertex. Row 1689 (2), if true everywhere, strengthens the lower bound to $7v_K/8$. Indeed $\operatorname{Tr}\wedge^2 X=((\operatorname{Tr}X)^2-\operatorname{Tr}X^2)/2$ and the frame reads nine times that minor trace. Thus the exact improvement of the certified local contribution would be $27v_K/40$. The sufficient residual changes from $p_{\rm rest}\ge p_*-v_K/5$ to $p_{\rm rest}\ge p_*-7v_K/8$. For $-\log p_{\rm rest}$ the extra allowance is precisely

$$
 \log\!\left(\frac{p_*-v_K/5}{p_*-7v_K/8}\right).
 \tag{6}
$$

This tends to zero by (5). Even rank one at every site credits at most $v_K$ in purity. The bound on coverage applies to every value of the isotropic normalized minor ratio.

**PROVED — Allowing all momenta and all cross terms.** Let $Q=I-P$ and $p_\perp=\operatorname{Tr}[(Q\rho Q)^2]/(1-t_K)^2$ for $t_K<1$. With $t=t_K$, positivity gives

$$
 (1-t)^2p_\perp\ \le\ \operatorname{Tr}\rho^2
 \ \le\ (1-t)^2p_\perp+2t-t^2 . \tag{7}
$$

The contribution within $P$ is at most $t^2$. For every mixed matrix element, $|\rho_{ij}|^2\le\rho_{ii}\rho_{jj}$ by positivity on its two-dimensional span. Their sum in both orders is at most $2t(1-t)$. This accounts even for interference with configurations outside every translated packet. Consequently passing requires, for late $K$,

$$
 -\log p_\perp \le H+\log\!\left(
 \frac{p_*(1-t)^2}{p_*-2t+t^2}\right).
 \tag{8}
$$

The correction tends to zero. The complementary sector must itself meet the original log budget up to a vanishing allowance. Its one-copy omitted mass $1-t$ tends to one, while the proposed allocation for omitted mass was $1/32$. Any test on the momentum blocks in row 1689 (7) sees at most $t$ of the one-copy trace. Equations (5)–(8) obstruct this complete translated family on the actual isotropic Wilson law.

**PROVED — A Wilson comparison for the normalized minor.** Keep the calibrated electric coupling $\beta_K$, the geometry, the centre projection, and $u$. In the anisotropic Wilson comparison set the spatial plaquette coupling to zero. This is the electric axis of registry ANISO-TAIL. Normalize the one-link vacuum multiplier to one. Every function in $W_x$ has one fundamental or dual factor on each of $12m$ links and is constant on the rest. The positive fundamental one-link multiplier is $r_f=I_2(\beta)/I_1(\beta)$ in both orientations. Gauge and neutral projection fix these functions. The exact compression of the period-$u$ operator to $W_x$ is therefore $r_f^{12mu} I_5$, up to the common scalar normalization. Its normalized minor trace is $2/5$, strictly above the proposed $1/16$. All translated blocks have this same eigenvalue and no mutual matrix elements. Their nonzero-momentum trace fraction is $1-n^{-3}$, above $1/32$. These are counterexamples to the local and momentum tests in the anisotropic comparison class. The coverage estimate (5), independently, uses the isotropic Wilson spatial action. It leaves the normalized shape of an individual isotropic packet open.

**PROVED — Separation from the seed with the same time and electric coupling.** On this electric axis the seed already passes at all late cutoffs (row 1145, section 7, crediting row 863, Lemma A2). Normalize the electric convolution to fix constants. At the half time $r$ the one-link kernel lies in $[1-\epsilon,1+\epsilon]$ by row 1145 (1)–(2), with $\epsilon=\sum_{d\ge2}d^2e^{-(d-1)r/(1+\beta)}$. The independent product of $3n^3$ kernels lies between the corresponding $3n^3$-th powers. Vertex gauge averaging and centre averaging preserve these pointwise bounds, since both commute with the convolution. As $n^3\epsilon\to0$, the integrated half kernel tends to one uniformly in both endpoints. Its normalized columns therefore have squared overlap tending uniformly to one. Yet the proof of (3) still applies. It needs the first temporal plaquettes, and dropping all spatial action terms only improves the restricted partition-function lower bound and the remote-link tilt ceiling. Thus in this Wilson comparison the desired integrated angle holds even as the common-centre path test fails with probability tending to one.

**PROVED.** The frame counterexample extends to a strictly positive spatial coupling. Let $a=r_f^{12mu}$ be the electric packet eigenvalue and take $s_{\rm mag}=a/(48n^3u)>0$. Here $s_{\rm mag}$ is a comparison coupling, separate from the physical loop side $s$. The spatial action $S$ lies in $[0,6n^3]$. For $M=\exp[-s_{\rm mag} S/2]$, $\|M-I\|\le3s_{\rm mag}n^3$. The normalized electric transfer $T_e$ and $M T_e M$ are contractions. Subtract their $u$-th powers in a telescoping sum to get norm at most $6s_{\rm mag}n^3u=a/8$, also after centre projection and compression. The five packet eigenvalues then lie between $7a/8$ and $9a/8$. Their normalized minor trace is at least $10\cdot7^2/(25\cdot9^2)>1/16$. Each positive period-$t$ twist integral changes by a factor between $e^{-6s_{\rm mag}n^3t}$ and one. Hence the global purity is at least $e^{-a/4}$ times its electric value, which tends to one. Here $a\to0$ by the fundamental multiplier bound. This gives positive magnetic and electric Wilson weights, a passing seed, and a failed local frame test at the same original cutoffs. The isotropic coverage obstruction above needs no such change of coupling.

## Y4 and the comparison laws

**PROVED — Box, sign, size and use (items 1–3).** Both results pass the specified-law and common-cutoff tests. They hold on every sufficiently late original cutoff and on every cube of the stated side. For C, the signed gain against the proposed common mass is $c_*-\Delta_K$, in the direction that refutes the proposal. For A, against any fixed required intensity $c>0$, the signed deficit $c-t_K$ is at least $c-T_K$, or use (5a) in place of $T_K$. The independent references are the common mass required by (5) of row 1689 and the allocated trace coverage. Neither reference is selected from a passing set. The tests pass as measured obstructions. As positive inputs they fail the required sign or spending test. Equations (4), (6) and (8) price the residual. No positive cutoff-independent part of the log budget is secured by either measurement alone.

**PROVED — Weak four-dimensional compact $U(1)$ and its strong twin (item 4, g1 and g3).** Use the cosine action $\beta\sum_p(1-\cos\theta_p)$, the same $n,u$, zero magnetic twist and the three half-turn cuts. At large $\beta=\beta_K$, the three holonomies in a common circle have collinear quaternion vectors. C has a single sheet. The sign is absent also at small positive $\beta$. In A's fixed abelian charge routing the coefficient space is one-dimensional, so its normalized minor vanishes at both couplings. This meets the literal group-void test for the two-sheet operation. It fails to distinguish the abelian phases. Changing to the full continuous-centre projection would change the law.

**PROVED.** Even the loss of bare packet weight has an abelian version. For spacetime dimension $d$, the untwisted Haar probability of $|\theta|\le\beta^{-1/2}$ is $1/(\pi\sqrt\beta)$ per link at $\beta\ge1$. Keeping this term in the $2^{d-1}$-cut average gives a mean signed deficit per specified face of at most

$$
 b^{\rm ab}_{\beta,d}
 =\{8{\textstyle\binom d2}+d\log\pi+(d/2)\log\beta+(d-1)\log2\}/\beta .
$$

Indeed the restricted sum of plaquette deficits is at most $8\binom d2 V/\beta$ on $V$ spacetime sites. Use convexity and translations as in (3). A Haar circle plaquette has probability at most $\sqrt{v/2}$ of deficit at most $v$, since $1-\cos\theta\ge2(\theta/\pi)^2$ on $[-\pi,\pi]$. The proof of (5) then bounds $a t_K$ for the bare charge packets by $4(b^{\rm ab}_{\beta,d})^{1/3}$ at late weak cutoffs, using $v=(b^{\rm ab}_{\beta,d})^{2/3}$. At any fixed small positive coupling, the open-end argument in (5a) still loses a factor strictly below one per marked link. The modulus of the mean of a circle charge of magnitude one is strictly below one under every positive finite tilt. Its maximum over the compact interval of allowed tilts is also strictly below one. In three spacetime dimensions use the same cosine action and the two spatial half-turn cuts. There are only two spatial axes. The distinguished three-plane geometry is absent and C remains void on the circle. The Haar bound just given also applies to a translated square carrying unit charge. For the three-dimensional Villain weight $\sum_{k\in\mathbb Z}\exp[-\beta(\theta_p-2\pi k)^2/2]$ the same geometric absence holds. No comparison of mass gaps for the two actions is needed.

**PROVED — Five-dimensional $SU(2)$ and its strong twin (item 4, g2 and g3).** Embed the three petals in three of the four spatial directions of the hypercube. Use Wilson plaquettes, the same aspect and coupling sequence, and the sixteen-term projector from the four cut directions. In (3) now $j=7$, a marked interior link has eight staples, and

$$
 b_{\beta,5}=\{80+5\log(6\pi)+(15/2)\log\beta+\log16\}/\beta .
$$

The bound follows by restricting all $5V$ links in the untwisted term to the same Haar cap, bounding the deficits of $10V$ faces by $8/\beta$, and applying convexity as above. Replace $1+6\beta$ by $1+8\beta$ in $\xi_K$. These changes leave (1) and the TV limit (3) in force. In (5a) the number of translates is $n^4$ and each free-end link has six half spatial staples and one full temporal staple, so $3\beta$ becomes $4\beta$. The intensity still tends to zero. For fixed sufficiently large $\beta$ one can also make the error in (3) smaller than $c_*$ by choosing $\beta$ first, then $n$ large. The estimates read the incidence counts but yield no four-dimensional gain. They fail the dimension-selectivity test. These finite-volume comparisons hold whether or not the weak five-dimensional phase has a mass gap.

**PROVED.** At $0<\beta\le1/32$, in either four- or five-dimensional $SU(2)$, change just the starting sheet. Apart from the initial spatial half weight, one temporal plaquette is the only change in a full path. Its log ratio has modulus at most $2\beta$. This remains true relative to the same initial factor after summing over signs. Choose $l(z)$ to be the log ratio of the initial spatial half weights. Then $|l_h-l(z)|\le2\beta\le1/16$ on every history. Also $q(H_h)\le(\tanh\beta)^r<1/16$, from row 1689 (4). The common-centre test thus passes at strong coupling with $\eta=0$. Equation (3) refutes it on the weak sequence in both dimensions. The bare-packet bound (5a) applies also at fixed strong coupling. At $\beta=0$ the kernel is constant, global purity is one, and the packet has zero intensity by integration of any private fundamental link. This separates the packet-coverage premise from the global seed on an actual Wilson law.

**PROVED — Neutral spectator (item 4, g4).** Tensor the Wilson transfer with a positive neutral transfer $S_K$, with cuts acting as identity on the second factor. A sign move keeps the spectator endpoints fixed. Its two normalized history laws have the same spectator bridge as a factor. TV and the angle of the two normalized product columns are unchanged. For A lift each bare function as $f\otimes v$ with a fixed unit spectator vector $v$, the constant in a probability reference or the oscillator vacuum. The compression acquires the scalar $\langle v,\rho_{\rm sp}v\rangle\le1$. It cancels out of the normalized packet shape when it is positive and can only reduce the measured intensity. If all spectator states are included in the projection $P\otimes I$, their multiplicities enter the pair sums. No bare Wilson readout estimates those multiplicities.

**PROVED.** For an explicit comparison through the calibrated limit take $M_s\ge2$ neutral states, $J$ the orthogonal projection onto their normalized constant, and

$$
 S_K=J+2^{-1/u}(I-J).
$$

This is strictly positive as a kernel and positive as an operator. It discretizes the fixed physical energy $(512/\ell)\log2$ above one constant state. At time $u$ its eigenvalues are $1$ and $1/2$ with multiplicity $M_s-1$ for the latter. Product purity is the Wilson purity times $(M_s+3)/(M_s+1)^2$. Already $M_s=2$ adds $\log(9/5)>H$ to the deficit. For a massless example, take independent neutral oscillators of lattice frequencies $\varepsilon_p=2(\sum_i\sin^2(\pi p_i/n))^{1/2}$ over nonzero momenta of the periodic cube. Omit the zero mode. The excitation energies of each oscillator are $k\varepsilon_p$ in lattice units for $k=0,1,\ldots$. The lowest physical frequency tends to $2\pi/\ell$ as the cutoff is removed and then to zero as $\ell$ grows. At $p=(1,0,0)$ the two geometric heat traces give purity $(1-e^{-u\varepsilon_p})/(1+e^{-u\varepsilon_p})=\tanh(u\varepsilon_p/2)\le\pi/512$. The other modes have purity at most one. This cuts the product purity below $p_*$ at every cutoff with the same aspect. The sign measurement has the same value on both products as on the original Wilson factor. A's omitted mass, or the full-spectrum quantity in (7), detects it if actually bounded. Thus neither proposal passes the neutral-spectator test as a sufficient positive input. The comparison changes the theory only for this test.

**ARGUED — Scale and scope (g5 and g6).** The simultaneous scales pass g5 for the obstruction in C. An explicit sufficient size for $q\le1/16$ and $\xi_K\le1/127$ in four dimensions is $n\ge N(\beta)=\max\{512e^{2\beta}\log16,\;(\ell/s)[2+(1+6\beta)\log512]\}$. Indeed the Fourier sum is at most $4t/(1-4t)$ for $t=\exp[-(m-2)/(1+6\beta)]\le1/512$. At fixed lattice, $r e^{-2\beta}$ tends to zero and the long-line estimate of the reflected alternative loses its small error. A's open-end estimate also needs the growth of $m/(1+3\beta)$ against $\log n$. Its separate plaquette bound (5) can lose packet weight even on a fixed box. As a route to the seed A still fails g6, by (6)–(8). The exact nonabelian operation in C is the reflection between two distinct simultaneous-conjugation orbits. It reads the noncommuting holonomies and the actual Wilson staple in (3), but yields separation with the adverse sign. For $SU(3)$ the unit-quaternion reflection and the five-dimensional $SU(2)$ frame do not define these measurements. For coupled adjoint-Higgs or K7 comparison models it gives no estimate of the added action. For a discrete subgroup or $\mathrm{Pin}(2)$ the proof that the remote normal has a density on $S^3$ does not transfer. No phase conclusion about those groups follows from this argument or from the fixed-lattice limits in row 1700. A proof specific to the unmodified Wilson law could exclude a tensor product as a premise, but would still need an estimate paying for its own unobserved neutral states.

## Result

**PROVED (hand arguments in this note).** For the fixed private-edge sign disintegration of row 1689, the mean common mass of the two terminal-weighted path laws tends to zero. This rules out the common-centre estimate at the size required by (4)–(5) of that row, including on any endpoint set of thermal probability bounded below. The bounds are uniform in the choice of a fixed private edge on each cube. For measurement A, the entire translated bare packet has thermal weight smaller than any inverse power of the cube side. This rules out coverage by these packets, including all their momentum blocks. The possible payment from their local minors is (6), and the unpaid complementary log budget is (8).

**ARGUED (boundary of the result).** The bare integrated column angle and the normalized shape of a single isotropic packet remain undecided here. An enlarged family of other channels or a direct analysis of already integrated rows could have different properties. The passing cutoffs and the mass gap for the calibrated isotropic law remain open. This is a research note. The new hand proofs await independent checking and carry no status. The proofs use hand inequalities and the cited analytic and calibration inputs. No numerical calculation or new Lean check was used. The crux card reports $\mathrm{propext}$, $\mathrm{Classical.choice}$ and $\mathrm{Quot.sound}$ for the existing formal consumer.
