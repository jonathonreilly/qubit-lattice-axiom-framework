## Repo search

Row 1587, research at `449931836`. I searched Markdown and TeX on `origin/main` (`8b11ae2bb`), `pr/10114` (`f76f6c649`), `pr/10133` (`89faef229`), `pr/10134` (`1e70c7211`) and `pr/10141` (`c73ad7b17`). Searches for “ambiguous arcs/bridges”, “frequency of ambiguous”, the conditional bias of the seam label, “gap-band-flux-tail” and “pinned Dobrushin” returned no matches on these refs. The target search outside the lane in the pinned checkout also returned none. Broader, capped searches used “vortex free energy”, “electric-flux confinement”, “Tomboulis–Yaffe”, “plaquette random-cluster”, “conditional seam” and common twist interpolation. The relevant hits have the following scope.

| Source | What it supplies here |
|---|---|
| Main, `research/mass-gap/library/gap-crux-restate.md`, §4.1, Theorem F and §4.4 | With transverse sides fixed and bulk-normalized odd mass below one on a tile, the odd fraction decays exponentially in the area on its multiples. The tension depends on the transverse sides. The same file splits the unpinned odd fraction into a mean over signed plaquette couplings on the adjoint field. Neither statement estimates a short pinned cylinder. |
| Main, `research/mass-gap/library/gap-skeleton-final.md`, § on the Tomboulis–Yaffe inequality, and `prior/gap-crux-lit-2.md`, Kanazawa's Theorem 1 | A rectangular Wilson loop is bounded by twice the one-axis odd fraction raised to the loop-to-plane area ratio. This consumes the flux estimate. |
| Main, `research/mass-gap/library/gap-form-exercise.md`, §2.A9, and the soft route on PRs 10114/10133, `checks/review_massgap_block_literature.md`, 111–121 | Ito and Seiler distinguish flow to strong coupling from matching the twisted and untwisted interpolation parameters. These papers give no bound on the frequency of ambiguous endpoints. |
| Main, `research/mass-gap/library/prior/gap-crux-lit-cross.md`, 73–75, and lane `gap-afield-a-max.md`, A8 | Duncan and Schweinhart's monotone plaquette random-cluster result is for finite Potts gauge theory. A8 already gives the Edwards–Sokal marking conditional on the SU(2) adjoints, with the centre lifts uniform subject to the marked constraints. |
| Lane, [row 1171, (2)](gap-solve14-astra62.md), [check 1585, §(v)](gap-band-direction5-check-astra62.md) | The first writes an equal-half twist ratio as an overlap of conditional deck-label laws. The second gives the short-arc product identity, the strong-coupling test, a sufficient conditional-indicator estimate, and a two-state example separating long-period flux decay from the count. These are inputs. |
| Lane, [row 1568, Thm E](gap-band-cut-covariance-neon.md), [check 1572](gap-band-cut-covariance-neon-check-opus.md), [weak compact U(1) check 1571](gap-band-cut-covariance-astra62-check-opus.md) | The pinned mixed row is bounded by a constant times $t q^{t-2}$ for $q=9\beta/2<1$ in 4D SU(2). Weak compact U(1) has a positive odd thermal fraction at the tested aspects. The weak interacting 5D SU(2) comparison is open. |

Follow-up searches for near-minimal winding sheets, excess-area entropy, plaquette erasure and straight winding holonomies returned only a fixed hopping-sign assignment in the five-ref search (the L4 delayed-splitting note, line 140). In the lane, [row 823, (R4)](gap-rtail-astra.md) counts closed winding sheets by excess area, [row 1167, (1)](gap-solve12-astra62.md) bounds directional plaquette deletion, and [row 1161, (23)](gap-solve9-astra62.md) controls the straight winding transports conditional on an exterior. The second and third attempts use these estimates on the specified arc law.

The target-specific prior file is absent. The [November 8 digest](prior/repo-search-2026-11-08.md) surveys earlier ultraviolet and witness work. The registry gives TWO-PER to row 1520, concerning the derivative of neutral purity. It has no row covering this short-arc probability. Row 1588 is the parallel assignment in FINISH. I used 't Hooft's electric twists and the on-disk sources only.

I searched the Sussman–Alpoge outline index, including its obligations, for electric flux, thermal traces, centre twists, vortex free energy and spectral gaps. For the nearby hits see chunks 03, 04 and 08. Sussman and Alpoge, with Claude and Codex, distinguish a filtered estimate from a gap at outline lines 3717–3720, require a separate spectral bound at 4629–4643, and restrict their flat covariance decay to constrained variables at 9568–9573. CA-I 2703–2710 explicitly excludes a mass-gap claim. I found no supplier of a pin-law estimate there.

## Plan and stopping test

At each $d\in\{n/512,n/256\}$ let $m=\lfloor\sqrt d\rfloor$, with the arc lengths prescribed in check 1585. Write $N$ for the number of arcs with $|b_j|\le1/2$. The target is a common bound $\Pr_{\rm ev}(N<c\log n)\le C_0n^{-\epsilon}$ for the SU(2) Wilson law throughout $2\le\beta\le3$. The separate test uses $\beta_K$ on the calibrated sequence. The stopping test is a proof, a Wilson lower bound contradicting the quantifiers, or three distinct attempts on one explicitly stated estimate. Pin probabilities must be evaluated on the full period $d$. The final step is to pass only what has been obtained to the flux and purity formulas.

## One estimate to attack

Write $A_t=(K_t+K_{t,C})/2$, $B_t=(K_t-K_{t,C})/2$, $Z_e(s)=\operatorname{Tr}(P_{\rm ev}T^s)$ and $Z_o(s)=\operatorname{Tr}(P_{\rm od}T^s)$. Haar measure on each raw slice has mass one. Gauge projection is included in $K_t$. Given the two pins on one arc, let $H=+1$ for its ordinary lift and $H=-1$ for its translated lift. Its conditional mean is $b_t=B_t/A_t$. Integrating out the complementary arcs by the even semigroup gives the actual end-pair law
$$
 Q_{d,t}(dx\,dy)=\frac{A_t(x,y)A_{d-t}(y,x)}{Z_e(d)}\,dx\,dy .
$$
For each of the two periods set
$$
 D_{d,t}=\mathbb E_{Q_{d,t}} b_t^2,\qquad
 \overline D_d=\frac1m\sum_{j=1}^m D_{d,l_j}.
$$
**Open estimate.** Do absolute constants $a>0$ and $L<\infty$ exist such that $\overline D_d\le L n^{-a}$ for large admissible $n$, at both periods uniformly in the bare band? Test the same estimate separately along the calibrated sequence. This asks how much of the square of a binary seam sign the two full pins predict. The elementary identity $\mathbb E(Hf)=\mathbb E(b_tf)$ holds for every square-integrable function of those pins.

**Implication, by hand.** The number of arcs with $|b_j|>1/2$ is at most $4\sum_j b_j^2$. Once $m\ge 2c\log n$, Markov's inequality gives
$$
 \Pr_{\rm ev}(N<c\log n)\le 8\overline D_d .
 \tag{1}
$$
Any fixed $c>0$ is allowed. In the opposite direction, check 1585 gives $Z_o(d)/Z_e(d)=\mathbb E\prod_j b_j$. For $m\ge2$, the arithmetic-geometric mean inequality gives $\prod_j|b_j|\le m^{-1}\sum_j |b_j|^m\le m^{-1}\sum_j b_j^2$. Thus $Z_o(d)/Z_e(d)\le\overline D_d$. No independence of the pins is required for either bound.

The mean-square estimate is genuinely stronger than the requested count on positive transfer data. On the two points exchanged by $C$ take the stochastic symmetric transfer with eigenvalues $1$ and $r_n=\exp(-64/\sqrt n)$. Each $|b_j|=r_n^{l_j}$ tends to $\exp(-64\sqrt{d/n})<1/2$ at both specified aspects. Eventually $N=m$ identically while $\overline D_d$ tends to a positive constant at each aspect. These data have neutral purity one. The reverse separation from the purity seed is obtained by tensoring the constant kernel with a neutral spectator of small purity, as in check 1585. These comparisons concern positive transfer data. They identify the cost of using (1) and supply no physical separation theorem within the pure Wilson family.

## First attempt · changing the period of a bridge

On the symmetric period $2t$, cancellation of both factors $A_t$ gives the exact identity $\mathbb E_{Q_{2t,t}} b_t^2=Z_o(2t)/Z_e(2t)$. The right-hand side is the odd Hilbert–Schmidt norm squared divided by the even one. On the required long circle the likelihood ratio is
$$
 W=\frac{dQ_{d,t}}{dQ_{2t,t}}
   =\frac{Z_e(2t) A_{d-t}(y,x)}{Z_e(d) A_t(x,y)},\qquad
 \mathbb E_{Q_{2t,t}} W^2
   =\frac{Z_e(2t)Z_e(2d-2t)}{Z_e(d)^2}.
$$
All denominators are positive. Cauchy–Schwarz and $b_t^4\le b_t^2$ now give the finite-volume Wilson bound
$$
 D_{d,t}\le
 \frac{\sqrt{Z_o(2t)Z_e(2d-2t)}}{Z_e(d)} .
 \tag{2}
$$
This compares traces at the actual spatial volume. It gives a route if the right side decays at the two arc lengths. A neutral spectator can enlarge the second moment of $W$ while leaving $D_{d,t}$ fixed. Conditioning $W$ on $b_t^2$ before applying Cauchy–Schwarz would drop that independent factor, but I have no estimate on this conditional likelihood for Wilson pins.

**Why the short-period odd fraction alone cannot finish this attempt.** For any integer $p>0$ take $M=\lceil n^p\rceil$ auxiliary pairs of points and one distinguished pair, with $C$ exchanging each pair. On the distinguished pair use the stochastic block of eigenvalues $1,r=\exp(-1/n^2)$. On each auxiliary pair use $sP_{\rm const}$ with $s=\exp(-1/\sqrt n)$. Add $\eta P_{\rm all}$ to the block diagonal transfer, where $P_{\rm all}$ projects onto the global constant and $\eta=e^{-n^2}$. The resulting kernel is strictly positive and the transfer is positive semidefinite. Its only nonzero odd eigenvalue is $r$. In the even sector the perturbation is positive and has norm $\eta$. Min–max bounds each eigenvalue increase by $\eta$. In particular $Z_e(2t)\ge M s^{2t}$, so $Z_o(2t)/Z_e(2t)=O(n^{-p})$ for both arc lengths. At either long period,
$$
 1\le Z_e(d)\le 1+M s^d+(M+1)d\eta(1+\eta)^{d-1}=1+o(1).
$$
Here $d$ is proportional to $n$ and $t$ is of order $\sqrt n$. Hence $Z_o(d)/Z_e(d)\to1$ and $\overline D_d\to1$. In fact $\Pr(N\ge1)\le2(1-Z_o(d)/Z_e(d))\to0$ since $\prod_j |b_j|\le 1-\tfrac12 1_{\{N\ge1\}}$. This example specifically tests the change of *pin law* with period. It is different from check 1585's example of a small odd fraction at the long period. It is not a Wilson counterexample. At $2\le\beta\le3$ and separately at $\beta_K$, I do not obtain the missing long-period weighting in (2).

## Second attempt · freeing the seam sign with plaquette erasures

Use the SU(2) centre lifts of Mack and Petkova and the Edwards–Sokal marking already written in [A8](gap-afield-a-max.md). The new question is whether this extra information still permits both *arc* labels at fixed full pins. There is an area estimate for this question in the actual Wilson ensemble.

Realize the even trace by initially summing over independent fair signs, one sign for the temporal seam on each arc, then weighting by the Wilson integrand. Equivalently fix a representative of each raw pin and allow its $C$-translate at one end of that arc. These give the same integral by changes of link variables. Given the full labelled field, independently mark a plaquette with probability $1-e^{-2\beta(w_p)_+}$, where $w_p$ is its true normalized fundamental trace, including its seam sign. Spatial boundary plaquettes in the sewn torus receive their full weight once. They are fixed by both choices of the arc label. Forget the interior fundamental links, keeping their adjoint links, the marks, and the pins. The identity
$$
 e^{\beta w}=e^{-\beta|w|}\big[1+(e^{2\beta|w|}-1)1_{\{w>0\}}\big]
$$
makes the remaining link signs and the seam bit uniform on the solutions of affine linear constraints over $\mathbb F_2$. Indeed Haar disintegration over each adjoint link gives two equally weighted lifts, and a marked face fixes the parity of the four signs including any seam sign. Unmarked factors are identical for both lifts. Thus the arc sign is either fixed or exactly fair under this disclosure. Write $F_j$ for the event that it is fair, and $p_{+,j},p_{-,j},q_j$ for the probabilities of fixed plus, fixed minus, and $F_j$, conditional on the original pins. Then
$$
 b_j=p_{+,j}-p_{-,j},\qquad 1-|b_j|=q_j+2\min(p_{+,j},p_{-,j}). \tag{3}
$$

In particular $D_{d,l_j}\le\mathbb E(1-q_j)^2\le\Pr(F_j^c)$. A high probability of freedom after this extra disclosure would suffice for the mean-square estimate. A fixed disclosed sign can still fluctuate when the interior is integrated out.

**A necessary surface for a fair sign.** Take direction 1 for the cut and 0 for time. If both signs solve the constraints, subtract their two lifts in the end-translate convention. The difference is a link cochain on the arc cylinder whose spatial restriction on one end is the cut cocycle and on the other is zero. Its coboundary vanishes on all marked faces and on the tangential faces at both ends. Extend this coboundary by zero off the arc. It is a closed plaquette cochain on the full torus, since each cube belongs to one side of either endpoint. Its sum on every $01$-torus at fixed $(x_2,x_3)$ is one modulo two by Stokes on the arc strip. The dual faces form an even two-cycle. In its decomposition into components connected by common edges, each component is closed, since all faces at a shared edge lie in the same component. At least one component has odd pairing with a $01$-torus, hence with every parallel translate by closedness. Call it $S$. It has at least $A=n^2$ faces dual to $01$ plaquettes, one above each transverse base square. Every face of $S$ is unmarked (meaning its primal plaquette is unmarked). The argument selects a witness only when the disclosed bit is fair. It says nothing about which value a fixed bit takes.

**Wilson probability of erasing a specified set.** Put $\Phi(\beta)=\int_{\mathrm{SU}(2)} e^{\beta\operatorname{tr}(g)/2}\,dg$. If all $k$ specified plaquettes contain a common direction,
$$
 \Pr_{\rm ev}(\text{all }k\text{ unmarked})\le 2\Phi(\beta)^{-k}. \tag{4}
$$
This uses the directional deletion estimate of [row 1167, (1)](gap-solve12-astra62.md) and its twisted-stack use in [row 1175, (17)–(19)](gap-solve16-astra62.md). Here is the normalization for the present law. Multiplication by the conditional failure probability replaces each selected Boltzmann weight by $e^{-\beta|w_p|}\le1$. The resulting numerator is at most the corresponding partition sum with those couplings deleted. Centre changes on time intervals move the arc seams to a single twist of their total parity, preserving the true traces and the deletion locations. The denominator is $(Z^0(d)+Z^C(d))/2\ge Z^0(d)/2$.

In the common direction as transfer time, removing an electric plaquette replaces its Wilson convolution, after division by $\Phi$, by Haar projection. This projection is below the normalized convolution in positive-operator order, by the SU(2) nonnegative character coefficients and its constant eigenvalue one. Each modified layer, with magnetic half weights and gauge projection, is therefore bounded in positive order by the homogeneous layer after extracting one factor $\Phi^{-1}$ per deletion. If the twist contains the time direction of this comparison, it can be placed in a terminal unitary. Otherwise its sheet can be taken static and the common magnetic half weights include its signs. Schatten Hölder at the period of that direction and eigenvalue ordering bound the absolute trace of the product by the homogeneous trace without a terminal unitary. With a static twist the restored trace is at most $Z^0(d)$, by switching back to direction 0 and using $|\operatorname{Tr}(CT^d)|\le\operatorname{Tr}T^d$. This proves (4) for the two parity terms with the displayed denominator. For an arbitrary $k$-face set in four dimensions, at least $k/2$ of its faces contain one coordinate direction by double counting, so (4) gives the bound $2\Phi^{-k/2}$.

**Band estimate, including field-dependent choices of nearly minimal sheets.** In the joint law, the probability that *any* such unmarked connected winding sheet has at most $A+\lfloor A/128\rfloor$ faces is at most
$$
                      2nd\,e^{-A/12},\qquad 2\le\beta\le3 . \tag{5}
$$
Apply the existing exploration count [row 823, (R4)–(R5)](gap-rtail-astra.md), [check 826](gap-rtail-check-opus.md), to the *dual* torus. In that count the horizontal plane here is $23$, the number of placements of its root is $nd$, and $A=n^2$. Its proof needs periods at least three, edge connectivity, even incidences and an odd covering of the horizontal base. It orders at most $2(A+K)$ inspected edges, flags at most $2K$ exceptional horizontal edges and records at most $4K$ choices from sixteen symbols. These facts hold on the present rectangle for $K=\lfloor A/128\rfloor$ regardless of its short time side. Thus the number of sheets is at most $nd\,16^{4K}256^{2K}(1+1/256)^{2(A+K)}$, using (R5). The log after removal of $nd$ is bounded by $32K\log2+(A+K)/128<A/4$, using $\log 2<3/4$. Each sheet requires erasing at least $A$ prescribed $01$ plaquettes, of cost at most $2\Phi^{-A}$ by (4). With $w=\operatorname{tr}(g)/2$, Haar symmetry on the unit three-sphere gives $\int w^2=1/4$. The even Taylor series gives $\Phi(\beta)\ge1+\beta^2/8\ge3/2$, so $\log\Phi\ge1/3$. The union bound proves (5). The count is from row 823. The probability in (5) concerns a positive marked Wilson law on the pinned-arc geometry, a different weight from row 823's dressed surface sum. Larger winding components are unrestricted by (5).

**Calibrated estimate for all sizes of sheet.** For $\beta_K\to\infty$,
$$
 \Pr_{\rm ev}(\exists j\ F_j)\le C n^3 d\,e^{-c\beta_K n^2} \tag{6}
$$
for all sufficiently late cutoffs, at both periods. A dual face has at most 20 edge neighbours. A depth-first walk of length $2(k-1)$ around a spanning tree bounds the number of rooted connected $k$-sets by $20^{2(k-1)}$ per root. There are $6n^3d$ roots. The necessary-surface argument and (4) bound the probability by $12n^3d\sum_{k\ge A}(400/\sqrt{\Phi})^k$. The Haar set $w\ge1/2$ has a fixed positive mass, so $\Phi\ge c_1 e^{\beta/2}$ and eventually $400/\sqrt\Phi\le e^{-\beta/8}\le1/2$. This gives (6). On the band $\Phi\le e^3$, so this last geometric sum gives no bound.

In particular on the calibrated sequence $\Pr_{\rm pins}(\max_j q_j>h)\le Cn^3d\,e^{-c\beta_K n^2}/h$ for every $h>0$, by conditioning the event in (6). On its complement each ambiguous arc needs $\min(p_{+,j},p_{-,j})\ge1/4-h/2$ by (3). Thus different disclosed configurations with opposite fixed signs can still give a small $|b_j|$. Even perfect determination after disclosure would allow $p_{+,j}=p_{-,j}=1/2$ at the pins. Equations (5) and (6) exclude the specified erasure mechanisms. They neither refute the lower tail in the pin law nor give an upper bound on $\overline D_d$. The whole-torus recovery of a twist from adjoints in [row 1155, (29)](gap-solve7-astra62.md) and the independent-replica double-cover erasure in [row 1131, (3)–(4)](gap-council-prob-astra.md) concern other disclosures.

## Third attempt · predicting the sign from the endpoint links

A refutation could come from a predictor of $H_j$ on the actual pins. For example, suppose some pin-measurable signs $U_j$ had $\sum_j\Pr(U_j\ne H_j)=o(\log n)$ along an unbounded sequence at one of the required periods. The minimal error on given pins is $(1-|b_j|)/2$, at least $1/4$ on an ambiguous arc. Thus $\mathbb E N\le4\sum_j\Pr(U_j\ne H_j)$, and $\Pr(N<c\log n)\to1$ for every $c>0$. This test gives the opposite tail if accomplished. It prompted the following attempt using winding transports and most of one raw pin.

**An estimate on almost all the links of the pin.** Fix $A_0>0$ and $k=\lceil(A_0+6)(1+6\beta)\log n\rceil$. For large $n$ in both regimes $2k<n$. At the starting pin $x$ of the tested arc withhold the direction-1 links based at $x_1=0$. From each parallel line also withhold the $k$ positive direction-1 links with $1\le x_1\le2k$ and $x_1\equiv x_2+x_3\pmod 2$. Reveal all remaining raw links of this pin, all other pins in full, and the complete group-valued transport along every straight spatial winding line of $x$ in the three positive directions (one fixed base per line). Denote these observations by $\mathcal G_j$. They omit only $(k+1)n^2$ individual links of $x$, out of $3n^3$, and retain all its straight winding traces. In the physical Wilson pin law, for all sufficiently large $n$,
$$
               |\mathbb E(H_j\mid\mathcal G_j)|\le n^{-A_0}
                   \quad\text{almost surely}.                         \tag{7}
$$
The estimate is uniform on $[2,3]$ and holds separately at $\beta_K=O(\log n)$. It also holds after applying this omission at every pin, by conditioning again.

For the proof, first withhold the transports too. Conditional on these preliminary data the two signs have equal probabilities. Indeed $x\mapsto Cx$ is invisible there. In the pin-and-label law, flipping $x$ and toggling both incident seam bits preserves every factor $K_{l_i}(C^{h_i}x_i,x_{i+1})$, where $h_i$ is the bit for $H_i$. This follows from diagonal centre invariance, and the cut at $x_1=0$ contains all links changed by the flip. The two incident arcs are distinct for large $n$.

Use the conditional path estimate of [row 1145, (1)–(2)](gap-solve2-astra62.md) and the straight-line product argument of [row 1161, (23)](gap-solve9-astra62.md). The one-link identity is (GL3) of Sussman and Alpoge with Claude and Codex, outline 2197–2231, indexed in chunk 02. Condition on the seam labels and on every Wilson link except the extra $k$ selected links per line. In particular the curtain at $x_1=0$ can be fixed in this intermediate calculation. No action plaquette contains two of the selected links. Parallel neighbours in the same longitudinal layer have opposite transverse parities, also across the periodic boundary since $n$ is even. The selected links are conditionally independent, each with a translated one-link density of tilt length at most $6\beta$ in the signed Wilson action. For every fixed exterior the transport on one line therefore has density differing from one by at most
$$
   \eta\big(k/(1+6\beta)\big),\qquad
   \eta(s)=\sum_{h\ge2}h^2 e^{-(h-1)s} ,
$$
against Haar. This is the Fourier bound from (1)–(2) of row 1145 with the fixed intervening matrices left in the product. The $n^2$ parallel line transports are independent under this conditioning. The other two directions are already visible. Consequently the joint density of the newly revealed transports differs from one by at most $\delta=(1+\eta)^{n^2}-1$ relative to product Haar, even after conditioning back down to the preliminary data and either value of $H_j$. Since $\eta(s)\le C e^{-s}$ for $s\ge1$, the choice of $k$ gives $\delta=O(n^{-A_0-4})$. Bayes' formula with the equal sign priors gives $|\mathbb E(H_j\mid\mathcal G_j)|\le\delta/(1-\delta)$ when $\delta<1$. This proves (7). Every predictor using these measurements has error at least $(1-n^{-A_0})/2$ on the tested arc.

The small error in (7) bounds the orthogonal projection of the full bias onto the observed data. Indeed, with all pins denoted by $\mathcal P$, $b_j=\mathbb E(H_j\mid\mathcal P)$, and
$$
 D_{d,l_j}=\mathbb E\,\operatorname{Var}(b_j\mid\mathcal G_j)
             +\mathbb E\big[\mathbb E(H_j\mid\mathcal G_j)^2\big].       \tag{8}
$$
The variance on restoring the omitted links can be order one, even when their fraction tends to zero and all straight windings are known. For an explicit test on the same raw slice space with Haar reference, choose one straight direction-1 circuit and detour around one of its $k$ selected links along the other three edges of an elementary spatial square. Let $f(x)$ be the sign of the normalized trace of this closed detoured circuit. It is gauge invariant, $C$-odd, and has unit square almost surely. Multiplying the link at $x_1=0$ and the bypassed link on the original line by $-1$ preserves Haar and *every* observed datum of $x$ in (7), including the original winding matrix. Exactly one changed link occurs on the detour circuit, so $f$ changes sign. Define a comparison transfer with kernel $1+r f(x)f(y)$, $r=e^{-1/n^2}$. Its two nonzero eigenvalues are $1,r$ by Haar balance, its kernel is strictly positive, and its even pin law is product Haar. Here $b_j=r^{l_j} f(x_j)f(x_{j+1})$. Every projected bias in (7) vanishes, yet $|b_j|\to1$ on every arc. The comparison transfer is artificial. For Wilson I have no estimate on the first term of (8), or a successful predictor from the complete pins. Replacing the open estimate by that conditional variance would rephrase the same missing upper bound.

## Model tests and consequence for the seed

Below $\beta=2/9$ the pinned mixed-row bound of row 1568 already makes the full bias small. More precisely, on any fixed subinterval with $q=9\beta/2\le q_*<1$, check 1585 bounds the log ratio by $C n^2 t q_*^{t-2}$. Since $b_t$ is the hyperbolic tangent of half this log ratio and $t\asymp\sqrt n$, even the stronger mean-square estimate holds there. In the opposite direction, at sufficiently weak fixed 4D compact U(1) Wilson coupling, rows 1565/1571 give a positive lower bound on the one-axis odd thermal fraction. Thus $\rho_d=Z_o(d)/Z_e(d)$ is bounded away from zero. The inequality $\rho_d\le\overline D_d$ locates the failure of the proposed sufficient estimate. For the original count one even has
$$
 \Pr_{\rm ev}(N<c\log n)\ge
 \frac{\rho_d-n^{-c\log2}}{1-n^{-c\log2}},
$$
by splitting the signed-product bound of check 1585 on that event. This uses the compact theory's flux estimate at the actual aspect. For interacting weak-coupling 5D SU(2) I cannot establish failure of the count or of the sufficient estimate. The number of transverse plaquettes and the geometry of the dual cycle in (5) depend on dimension. That dependence gives no sign balance for 4D and supplies no selective step separating the two SU(2) laws.

If the requested estimate held, put $R_n=C_0n^{-\epsilon}+n^{-c\log2}$. Check 1585 would give $Z_o(d)/Z_e(d)\le R_n$ on each spatial axis by cubic symmetry. In 't Hooft's character decomposition the probability that electric character $e$ has $e_i=1$ is $Z_{o,i}(d)/(Z_{e,i}(d)+Z_{o,i}(d))$. The union bound gives
$$
 f(v):=1-\frac{Z_+(2v)}{Z^0(2v)}
       =\Pr(e\ne0)\le\frac{3R_n}{1+R_n},\qquad 2v\in\{u,2u\}.
$$
This would be (N-flux) at the tested coupling. The band results (5) and (7) are about different observations from the full pair of pins. Equations (3) and (8) show why neither establishes this conclusion.

With $\Pi=Z^0(2u)/Z^0(u)^2$, the exact purity identity is $P_K=\Pi[1-f(u)]/[1-f(u/2)]^2$ at a release root, with the same algebra for the band analogue. In the notation of row 1566 the sandwich is $(1-21\delta_u/8)\Pi\le P_K\le\Pi/(1-21\delta_{u/2}/8)^2$ when $21\delta_{u/2}/8<1$. A flux bound shrinking to zero makes the multiplicative correction tend to one. A positive margin in $\Pi$ sufficient to reach $457/625$ is still required, or control of the signed correction at a borderline value. A neutral tensor factor cancels from every $b_j$ and multiplies $\Pi$ by its own purity. The present arguments give no estimate for $\Pi$ and no carry from the band to the calibrated roots. The use of $\beta_K\to\infty$ in (6) and of $\beta_K=O(\log n)$ in (7) applies those estimates directly at the roots. Neither transfers sign balance across couplings. [Purity consumer, §3.1](gap-k2-tool-design-fable.md) · [Sandwich and denominator check](gap-band-cut-covariance-fable-check-astra62.md)

The derivations here are by hand, with the on-file lemmas identified above. No numerical calculation, Lean certificate, independent check or audit was used for the new estimates.

RESULT — OPEN for the full-pin lower tail in 4D SU(2) Wilson, both on $[2,3]$ and along the calibrated trajectory. Three attacks on $\overline D_d$ give the period comparison (2), the Wilson erasure bounds (5)–(6), and the partial-pin bound (7). The balance of opposite signs at fixed full pins remains uncontrolled. Neither (N-flux) nor a bound on $\Pi$ or (PUR-io) follows.
