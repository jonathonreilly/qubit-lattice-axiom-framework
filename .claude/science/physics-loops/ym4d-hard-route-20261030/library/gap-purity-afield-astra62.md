# Repo search

Row 1683, laptop Codex, pinned at `44550e2f4`. The target-specific prior was absent. The November 8 digest concerns earlier construction work. I searched Markdown and TeX on `origin/main` (8b11ae2bb), `pr/10114` (f76f6c649), `pr/10133` (89faef229), `pr/10134` (1e70c7211) and `pr/10141` (c73ad7b17). The FINISH row has no separate prior-work list.

| Terms and hits | Exact statement and proximity (ARGUED from the cited source) |
|---|---|
| `PUR-io`, `passingCutoffs`, neutral purity, purity/centre flux | Only `docs/COLOR_PURITY_DOES_NOT_REDUCE_TO_PAST_HYPOTHESIS_SLOT_NARROW_THEOREM_NOTE_2026-06-09.md` and the historic YT intake `HISTORIC_YT_PR230_NONCHUNK_CYCLE16_REOPEN_SOURCE_GUARD_NOTE_2026_05_05_INTAKE_NOTE_2026-08-05.md` appeared. Their hits concern neutrality admission and a scalar-Yukawa note. |
| Multihit, one-link convolution, perimeter suppression, staples, adjoint Laplacian, compressed transfer | On PRs 10114/10133, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/CROSSOVER_LITERATURE_BRIDGE_ASTRA.md` §4 (7)–(8) gives $(1-e^{-12\beta})^M$ for a separately Haar-centered insertion on $M$ plaquette-independent links. Its product conditioning is the precursor of (1). In the same folder, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` §2 (5)–(9) gives a *lower* one-step quadratic-form bound for one centered simple-loop character. The present question asks for an *upper* trace bound with all multiplicities. |
| Other relevant returns | On main, `docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md` near L284 diagonalizes the one-link kernel. `docs/GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md` near L176 has a nonzero off-diagonal on an anisotropic slab. `docs/FINITE_CLOCK_STATIC_CHARGE_TRANSFER_HAMILTONIAN_AND_PATH_COMPARISON_BOUNDED_THEOREM_NOTE_2026-09-15.md` (1) diagonalizes a finite cyclic convolution. The mass-gap snapshot's `gap-transfer-check.md` and `gap-seed-check-astra.md` credit GL3 and GL8. In the soft route, `REVIEW_FLOW_S10.md` §6 reduces a Cartan plane-wave ghost vertex to a scalar one. `checks/f9_criteria.md` specifies a fixed-background heat-coefficient test. These statements do not estimate the random two-color or neutral Wilson traces below. |
| Searches without a matching statement | Holonomy Gramian, observability, axis transversality, inverse moments, perimeter randomization, covariant Laplacian/frustration/Lifshitz, displaced or point-split adjoints, scalar contact, commuting valleys, and bosonic matrix Hamiltonians. The valley/Coulomb search returned the supplied noncompact Gaussian kernel in `docs/FINITE_STEP_GAUSSIAN_GAUGE_CANONICAL_LOGARITHM_AND_COULOMB_COST_BOUNDED_THEOREM_NOTE_2026-09-14.md`. Helly/sample compression, maximum-volume minor selection, private-link relative traces, and coprime/Bézout or interleaved coarse transports had no matches under the tested combinations. |

A follow-up search for local indistinguishability, Knill–Laflamme conditions, bridge insertions and overlapping transports found the Cycle 275 note `LOCALLY_MATCHED_WILSON_SECTOR_STATES_CYCLE275_NOTE_2026-07-17.md`, §11. Its statement concerns exact projectors for a supplied stabilizer code. The record-formation exercise credits quantum error correction for local-error protection. The clock notes concern two-step time normalization. A search for suffix holonomy, cross-mesh relative entropy and plaquette mutual information returned only the numerical mesh comparison in `archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md`, L2131. None supplies a Wilson energy-band or entropy bound for the observations in §8.

The duplicate derivations, portfolios, criteria and prior-work pointers in the convolution search add no separate estimate. The separate paper-title search for Bandeira–Singer–Spielman, Kenyon, Gu–Eisenstat, localized covariant eigenmodes and Laplacian gauge fixing gave no hits on these five refs. The much closer results inside this lane appear in §9.

## Plan

1. Check the target-specific prior, the crux card, owner instructions and repository evidence. Stop if another row already covers the target.
2. Work from the card and its Lean interface. Test mechanisms against weak four-dimensional compact U(1). Push the strongest candidate to a proved lemma or obstruction.
3. Compare each candidate with the registry and cited sources. Record the exact remaining estimate and questions for a reading lane.

**Result (PROVED by hand below, using the stated finite Wilson inputs).** On the calibrated cube, a family of line measurements recovers every fine link with two readings. Each list separately has negligible total overlap with the excited low-energy neutral states, by (14). At both target periods a joint adjoint plaquette test distinguishes the true lists from independent draws of their own marginals with binary relative entropy at least $c n^3\log\beta$. Projecting the actual neutral thermal state onto the accepted configurations changes its purity by a relative $O(e^{-c n^3\sqrt\beta})$, by (16)–(17). For a tighter test at the scale $1/\beta$, (18) bounds the absolute discarded trace. Compact $U(1)$ gives zero information in the same adjoint test. **ARGUED.** The eigenvalues inside the accepted subspace remain uncontrolled, so (PUR-io) stays open. The separate spatial two-color operator in (10) retains a scalar branch whose purity vanishes.

Research text for FINISH row 1683, laptop Codex. “PROVED” marks a written derivation within its stated assumptions. “CITED” gives a source and a statement locator. “ARGUED” marks an assessment and “GUESSED” a proposed link. The historical standing of the source results remains as recorded by their authors.

## Phase 1. The chosen measurement

**CITED (target and consumer).** A cutoff passes if its spatial cube of side $n=\ell L^k$, at $u=n/512$, obeys $\operatorname{Tr}(P_0T^{2u})/\operatorname{Tr}(P_0T^u)^2\ge457/625$. One admissible $L$, its calibrated $M,g_0$, one positive $\ell$ divisible by 1024 and infinitely many original cutoffs $k$ must work. Read the kernel in `Transfer.lean`, 548–563, the projection and bare coupling in `Stage0.lean`, 69–73 and 150–152, and the ratio in `Purity.lean`, 25–29. `PurIo.lean`, 389–406, gives $\beta_k/(k\log L)\to11/(3\pi^2)$ on a subsequence of every infinite set for the same calibrated witnesses. `Offset.lean`, 701–706, states the consumer. With an infinite passing set it supplies the fixed-observable gap $(2/\ell)\log(2^{18}/5041)$ and a unique vacuum at the release witnesses. The crux card reports a kernel check with `propext`, `Classical.choice` and `Quot.sound`. These are source readings. No new kernel check is claimed.

**GUESSED (direction).** Test how many color vectors can return almost unchanged around the three spatial periods. Use one straight Wilson line per period, based at one site. The positive $3\times3$ matrix of squared adjoint displacements measures this. First estimate its smallest eigenvalue under the actual conditional Wilson law. Then ask how much of the neutral trace functions of these lines can see. Adjoint rotation fixes a scalar singlet, so this last question needs its own proof.

### 1. A long Wilson line loses its boundary data in every color representation

**CITED (already on file).** Set $b=1+6\beta$. A private link is a bond used once by its path and by no other measured path. Require that no plaquette contain two selected bonds. Given the other links, the selected bonds have independent translated densities $q_\kappa(g)\propto e^{\kappa\operatorname{Re}g}$ on unit quaternions, with $\kappa\le6\beta$. For a path with $m$ such bonds, the density of its product against probability Haar obeys

$$
 \|f-1\|_\infty\le\epsilon_m=\sum_{j\ge2}j^2 e^{-(j-1)m/b}
          \le C e^{-m/b}\quad (m/b\ge1).                                \tag{1}
$$

Joint densities multiply after conditioning. Signs of plaquette terms, fixed factors along a path and reversed orientations are allowed. Codex, 2026, row 1145, §1 (1)–(3), proves the first inequality from the normalized Bessel multipliers. For the second, factor out $e^{-m/b}$ and sum the convergent series at $m/b=1$. We use this stronger prior result in place of the closed-phase estimate. The underlying convolution is Sussman and Alpoge's GL3. [Row 1145](gap-solve2-astra62.md)

### 2. Exactly which inverse moment needs three spatial periods

**PROVED.** In the interior of a Wilson cylinder take the three straight, positively oriented spatial cycles at a common site. Let $H_i$ be their holonomies, $R_i=\operatorname{Ad}H_i$ on real $\mathfrak{su}(2)\simeq\mathbb R^3$, and

$$
 D(H)=\sum_{i=1}^d(I-R_i)^*(I-R_i),\qquad X=\lambda_{\min}(D).
$$

Here $d$ counts measured directions. Use $d=2$ or $3$. Keep all edges on each axis except the first and last as private links. Consecutive collinear edges share no plaquette. A plaquette meeting two perpendicular axes in such edges would meet them at their common base, which the deletion excludes. For $n\ge4$ we may thus take $m=n-2$ in (1). For every exterior and $\epsilon_{n-2}\le1/2$, there are absolute positive constants $a_d,A_d$ such that

$$
 a_d s^{d-1}\le {\mathbb P}(X\le s\mid{\rm exterior})
                  \le A_d s^{d-1}\qquad(0<s\le1/4).                    \tag{2}
$$

Consequently $\mathbb E(X^{-q}\mid{\rm exterior})$ is uniformly finite for $0<q<d-1$ and infinite for $q\ge d-1$.

**Proof.** The joint density lies between $2^{-d}$ and $(3/2)^d$ times product Haar. Work first with independent Haar holonomies. Conjugation by a Haar unit quaternion takes a unit imaginary quaternion to a uniform point on $S^2$ by rotational invariance. The chance to lie within chordal distance $r$ of a fixed point is $r^2/4$ for $0\le r\le2$, by the spherical cap area. A maximal $\sqrt{s}$-separated set of the sphere covers it and has at most $16/s$ points, by disjoint caps of radius $\sqrt{s}/2$. If $X\le s$, every $R_i$ moves a minimizing vector by at most $\sqrt{s}$. It moves the nearest net point by at most $3\sqrt{s}$, since $\|I-R_i\|\le2$. A union bound gives $(16/s)(9s/4)^d$. For the reverse inequality take a unit axis of $R_1$. Each of the other $d-1$ rotations moves it by at most $\sqrt{s/(d-1)}$ with probability $s/[4(d-1)]$, independently. The sum of squared displacements is then at most $s$. Multiply by the density bounds. Integration of the tail of $X^{-q}$ gives the integral of $s^{d-2-q}$ at the lower endpoint. The region $X\ge1/4$ gives a bounded contribution. This proves both endpoints of the moment claim.

**PROVED (scale and group).** Fix an admissible calibrated choice from the slope statement in `PurIo.lean`, 389–406. It gives $\beta_k=O(k)$ at least along one infinite sequence, by taking $A=\mathbb N$. In fact, if the ratio differed from its stated limit by some fixed amount on an infinite set, applying the same statement to that set would contradict convergence there. For the fixed calibrated witnesses this gives the slope on the full tail. For any fixed admissible physical side $\ell$, however large, (1) tends to zero at $n=\ell L^k$. The matrix $D$ is invariant in spectrum under gauge changes and center shifts. In four dimensions the three coordinate periods give a finite first inverse moment and a divergent second. Two periods give a divergent first moment. This dimension test uses one period per spatial direction; other collections of paths define other tests. For compact $U(1)$ every adjoint rotation is the identity, at every coupling. Then $X=0$ identically.

### 3. Local plaquette rotations and the spatial adjoint spectrum

**ARGUED (choice of the main mechanism).** Localize the color test before following it to a long line. A pair of elementary plaquettes can penalize a color vector at one site. A positive density of such sites can control **all** adjoint vectors by a scalar Poincaré estimate. Atypical boxes then control the low eigenvalue count by Neumann bracketing. This is a route from small-ball probability to a trace bound. The missing passage from an adjoint vector to a gauge singlet has a separate test below.

**CITED (earlier one-color estimates).** On a spatial Wilson slice define $\langle v,\Delta_U v\rangle=\sum_{x\to y}|v_x-\operatorname{Ad}(U_{xy})v_y|^2$ with counting measure. For any unit $w,w'$ and any translated one-link heat-bath variable $H$ above, row 1141's circle-fiber calculation gives

$$
  \Pr\{|\operatorname{Ad}(H)w-w'|\le h\mid{\rm other\ links}\}
       \le C b h^2 .                                                     \tag{3}
$$

The image density on $S^2$ is at most $4b$ times area probability. Row 1283 (2) consequently bounds the probability of a two-plaquette displacement below $v$ by $Cbv$. If a positive fraction of well-spaced sites in a spatial box of sides $R$ to $2R$ has displacement at least $v$, its Neumann form $Q_B$ satisfies

$$
 \sum_{x\in B}|s_x|^2\le C(R^2+1/v)Q_B(s).                              \tag{4}
$$

That row also bounds the expected fraction of one-color eigenvalues below $s$ by $\exp[-c s^{-3/2}\log(1/(Cbs))]$ in its specified size and energy range. This is stronger than our closed-phase counting estimate. The method uses the scalar Poincaré inequality on $|s|$ and disjoint private-link tests. We use its box argument for a different fiber in §5. [Codex, row 1141, (2)–(7)](gap-crux2-astra62.md) · [Codex, row 1283, (1)–(5)](gap-solve32-astra62.md)

**ARGUED (group, dimension and scope).** The ordinary $U(1)$ adjoint connection has an exact constant section. The volume exponent $3/2$ comes from a three-dimensional spatial box with $R\asymp s^{-1/2}$. Row 1675 already uses the one-color count to show why even a sharp dimension-dependent tail can miss the neutral transfer. The single-color spectral result belongs to those rows. [Row 1675, fixed physical wavelength example](gap-direction9-check-astra62.md)

### 4. How much of the actual transfer trace the line measurement controls

**PROVED (a compression of the Wilson transfer).** Let $A=T/\lambda_0$ on a finite cube, where $\lambda_0=\|T\|$. Write $\Omega$ for the positive unit Perron eigenfunction. At each of two distinct time slices measure the same vector $H$ of $N$ spatial loop holonomies with the private segments of §1, each of length at least $m$. Let $\mathcal V$ be the closed subspace of vectors $\Omega f(H)$ that are gauge invariant and center neutral. It contains $\Omega$. Write $\Pi$ for its orthogonal projection. If $t\ge2$ and $\eta=(1+\epsilon_m)^N-1<1$, then

$$
 0\le\operatorname{Tr}\bigl(\Pi P_0 A^t\Pi-|\Omega\rangle\langle\Omega|\bigr)
       \le \bigl(\eta/(1-\eta)\bigr)^2.                                 \tag{5}
$$

All square-integrable functions in this subspace are included, with no cap on their representation labels.

**Proof.** The real symmetric kernel is strictly positive, continuous and positive as an operator (the Wilson kernel in the card). On the compact finite product it is Hilbert–Schmidt. Compactness gives a top eigenvector. Replacing it by its absolute value increases the Rayleigh quotient strictly if a real eigenvector has both signs on sets of positive measure. The absolute value attains the top Rayleigh quotient and is a top eigenvector. Its image under the kernel is continuous and everywhere positive. This gives $\Omega$. An orthogonal second real top eigenvector would change sign. Real and imaginary parts give simplicity over the complex field too. Symmetries preserving the kernel and positivity fix the normalized $\Omega$.

Use the stationary path law on slices $-1,\ldots,t+1$. Its density with respect to product slice Haar is

$$
 \Omega(U_{-1})\Omega(U_{t+1})
       \lambda_0^{-(t+2)}\prod_{j=-1}^t T(U_j,U_{j+1}),
$$

which integrates to one by $T\Omega=\lambda_0\Omega$. Expand the gauge integrals in the kernel before conditioning. The spatial actions at slices $0,t$ occur with both half weights, and no time plaquette meets both selected slices. Conditional on the remaining links, the two observations have independent densities $f_E(x),g_E(y)$ relative to product Haar on $SU(2)^N$. Each differs from one by at most $\eta$ from (1) and the product formula. The lower bound follows also from $(1-\epsilon_m)^N\ge1-\eta$. Their common marginal $p$ is at least $1-\eta$. Their joint density $j$ satisfies

$$
 |j(x,y)-p(x)p(y)|=|\operatorname{Cov}_E(f_E(x),g_E(y))|\le\eta^2.
$$

Indeed each conditional density has variance at most $\eta^2$ about its mean, by comparison with one.

The isometry $Wf=\Omega f(H)$ from $L^2(p\,dH)$ gives $W^*A^tW$ the kernel $j/(p\otimes p)$ relative to the marginal measure. This operator is positive and fixes one. Subtract the constant projection. The result is positive, with kernel of absolute value at most $D=(\eta/(1-\eta))^2$. For a finite measurable partition, use the normalized indicators of its positive-mass cells. The diagonal element on a cell of mass $v$ is bounded by $Dv$. Their sum is at most $D$. Take refining finite partitions generating the Borel sets of the compact metric observation space. Their simple functions are dense in $L^2$. Positivity gives the full trace as the limit of the finite traces, by taking an orthonormal basis adapted to the increasing spaces. Restricting further to the gauge-invariant, center-neutral space can only decrease this positive trace. The center projection commutes with $A$, and acts as identity on $\mathcal V$. This proves (5).

**PROVED (growing measurement).** For even $n\ge4$, take every straight axis-1 period with both transverse coordinates even. There are $N=n^2/4$ such loops. None of their $n$ edges shares a plaquette with a second selected edge. For $u\ge2$, (5) holds at $t=u$ with $m=n$ and $\eta=(1+\epsilon_n)^{n^2/4}-1$. On the calibrated sequence this tends to zero faster than any inverse power of $n$, since $b=O(\log n)$. The same argument takes all functions of one based triple, with $N=3,m=n-2$. Perimeter smoothing alone has an abelian counterpart. The adjoint test (2) inside the latter observation space fails identically for $U(1)$.

**PROVED (where the measured space ends).** Even all straight spatial **period windings**, in every direction and from every starting site, miss a neutral variable. Multiply two distinct links on the same straight line by the central element $-1$. Every based full-period straight product stays fixed. The half-trace $W_p$ of a plaquette touching exactly one flipped link changes sign. It is nonzero Haar-almost everywhere because, with the other links fixed, its zero set for one free link is an equator of $S^3$. The flip preserves product Haar and its measure class for $\Omega^2\,dU$, since $\Omega>0$. Thus $W_p$ cannot be measurable with respect to the sigma algebra $\mathcal H$ of all these straight windings. The vector $\Omega(W_p-\mathbb E_{\Omega^2}[W_p\mid\mathcal H])$ has positive norm. It is orthogonal to every measured function. It is gauge invariant and center neutral because $\mathcal H$ is stable under both actions, $\Omega^2\,dU$ is invariant, and the contractible $W_p$ is invariant. In particular no positive weighted sum of the straight-line projections can give a lower frame bound on all neutral fluctuations. This says nothing about the energy of this missed vector.

**PROVED (a test for a proposed repair).** If two long paths share a return segment $B$, their words can be $AB$ and $A'B$. The half-trace of their relative product is the half-trace of $A(A')^{-1}$. A single plaquette detour can therefore restore a local neutral observable. The common segment cancels before any conditional smoothing occurs. No length of $B$ pays for this observable. This is the first estimate that a method using detoured lines has to replace.

### 5. Two adjoint colors at distinct sites, including all separations

**PROVED (extension toward a singlet).** Take a spatial slice of the actual Wilson torus $n^3\times N_t$, $N_t\ge4$, with periodic boundary conditions. The bounds below also hold for each fixed temporal center twist: moving the twist to plaquette signs preserves the one-link tilt bound. Uniform bounds therefore survive the positive mixture of twists in the neutral trace. For a displacement $r$ on the spatial torus and $Z_x\in\mathbb R^{3\times3}$, use the Frobenius norm and define

$$
 {\cal E}^{(r)}(Z)=\sum_{x\to y}
 \big\|Z_x-\operatorname{Ad}(U_{xy})Z_y\operatorname{Ad}(U_{x+r,y+r})^*\big\|_F^2 .
$$

Call the operator $\Delta^{(r)}$. The two ends move by the **same** lattice step. A change of site gauges rotates the two ends separately and preserves the spectrum. For every $\delta,p,q>0$, let

$$
 B'_n=b^{\,1+\delta}+(\log n)^{2/3},\qquad
 \Lambda_*=\min_{r\ne0}\lambda_{\min}(\Delta^{(r)}).
$$

There are positive constants $c,C$, depending only on $\delta,p,q$, such that for all sufficiently large $n$, every $\beta\ge0$ and $0<z\le1$,

$$
 \mathbb P\{\Lambda_*<c z/B'_n\}\le n^{-p}z^{q+1},\qquad
 \mathbb E\,\Lambda_*^{-q}\le C (B'_n)^q.                               \tag{6}
$$

This includes nearest-neighbor separations. No lower bound on physical separation is needed.

**Proof.** Choose an integer $J>9/2$ with $(1+\delta)(J-9/2)\ge J$ and $J-9/2\ge1$. Fix $r\ne0$. One of its coordinates is nonzero modulo $n$. In the perpendicular coordinate plane based at $x$, lay out $J$ unit squares. In plane coordinates put their lower left corners at $(3i,0)$, $0\le i<J$. Go out along the bottom row, around the square, and back along the same row. Select only the top horizontal edge of each square. These pivots are absent from every handle and share no plaquette. The translated paths at $x+r$ live in a different parallel plane. Conditional on the other links, their adjoint holonomies $S_i$ are fixed. The original rotations $R_i$ are independent, each the adjoint of a translated $q_{\kappa_i}$ variable, including the fixed handle factors.

Fix a Frobenius unit matrix $Z$. Some column of $ZS_i^*$ has norm at least $1/\sqrt{3}$ because its three squared column norms sum to one. If $\|R_i ZS_i^*-Z\|_F\le h$, its rotated unit direction lies in a spherical cap of chord radius at most $2\sqrt{3}\,h$ about the corresponding normalized column of $Z$. Indeed the two column lengths differ by at most $h$ and normalizing the target costs at most another $h$ in the original units. A zero target column gives an empty event for $h<1/\sqrt3$; enlarge the bound for larger $h$. By the cap estimate in (3) the probability is $\le C b h^2$.

Let $D_x^{(r)}$ be the sum of the $J$ squared loop displacements as a quadratic form on matrices. If its least eigenvalue is $<v$, a unit matrix moves by at most $\sqrt v$ under each rotation pair. A $\sqrt v$-net of the unit sphere in $\mathbb R^9$ has at most $(1+2/\sqrt v)^9$ points: pack disjoint balls of radius $\sqrt v/2$ into the ball of radius $1+\sqrt v/2$. At a nearest point every displacement is $\le3\sqrt v$ since the pair action is orthogonal. For $0<v\le1$, independence and the union bound give

$$
 {\mathbb P}\{\lambda_{\min}(D_x^{(r)})<v\mid{\rm exterior}\}
       \le C_J b^J v^{J-9/2}.                                         \tag{7}
$$

Choose $v=a_J z b^{-(1+\delta)}$ and then $a_J>0$ so small that the right side is at most $z/16$. These choices precede the volume and coupling.

Partition each cyclic coordinate into intervals of lengths $R$ to $2R$ by merging a final short remainder, with $2R\le n$. In each resulting box choose interior anchors with the entire original finite pattern inside. This leaves at least a fixed fraction of its sites once $R\ge 20J+10$. Select a further fixed fraction as follows. Two anchors conflict if either of their two path families comes within one plaquette of the other family. The difference of their positions then belongs to a finite set of bounded size: take differences of offsets in the pattern enlarged by two sites and add one of $0,r,-r$. Its cardinal is bounded by a constant of $J$, even modulo $n$. Greedily keeping one anchor and deleting its neighbors retains at least $c_J|B|$ anchors. No translated path now reads another test's pivot. Given all other links the tests in a box are independent. In particular correlations of the two original Wilson fields at separation $r$ have not been discarded.

For a good anchor, telescoping along paths of length $\le6J+4$ gives
$v\|Z_x\|_F^2\le C_J\sum_{e\ {\rm on\ its\ paths}}|\nabla_e^{(r)} Z|_F^2$, with repetitions counted. These paths in the **base coordinate** stay in the box. The coefficient at an edge may read a translated link outside the box, which is allowed. Edge multiplicities are bounded in terms of $J$. Use $h_x=\|Z_x\|_F$ in the scalar box argument of (4). Indeed, each internal edge bounds the change of $h$ by the norm of the transported difference. The variance of $h$ in the box is bounded by $6R^2$ times the sum of those squared differences, by the scalar box estimate of row 1141. At every good root, $\bar h^2\le2h_x^2+2(h_x-\bar h)^2$ for the box mean $\bar h$. If half the anchors are good, their positive density and the telescoping estimate bound the constant mode. This gives $C_J(R^2+1/v)$ as the inverse coercivity bound. When all boxes pass, summing the bounds and restoring the nonnegative edges between boxes gives the global inequality. Finite product conditioning bounds the chance that half the $M_B\ge c_J R^3$ tests fail by $2^{M_B}(z/16)^{M_B/2}=2^{-M_B}z^{M_B/2}$. Choose the constant in $R\asymp (1+\log n)^{1/3}$ so that $R\ge20J+10$ and $c_J R^3\ge(p+6)\log_2 n+2(q+1)$. Then choose $n_0$ so $2R\le n$ for all larger $n$. At most $n^3$ boxes and fewer than $n^3$ displacements enter the union bound. For the inverse moment integrate $\Pr(c/[B_n^\prime\Lambda_*]>y)\le n^{-p}y^{-(q+1)}$ against $q y^{q-1}\,dy$ from one to infinity. The contribution is at most $q n^{-p}$. This proves (6), also conditionally on the outside of the slice.

**PROVED (trace and exact contact failure).** The total dimension for $r\ne0$ is less than $9n^6$. At $u=n/512$, the good-event trace is at most $9n^6e^{-cu/B_n^\prime}$ and its expected exceptional contribution is $\le9n^{6-p}$. Thus for every $a>0$, choosing $p>a+6$, on the calibrated trajectory,

$$
 \mathbb E\sum_{r\ne0}\operatorname{tr}e^{-u\Delta^{(r)}}=O_a(n^{-a}),      \tag{8}
$$

with constants also depending on the fixed calibration and $\ell$. At $r=0$, however, every field $Z_x=f_x I_3$ has exactly the ordinary scalar graph Laplacian on its coefficient $f$. This follows from $R I_3 R^*=I_3$ on every edge. In particular the constant matrix is parallel for every Wilson sample. For $U(1)$ the same scalar branch persists for **every** displacement. This identifies the point at which the proposed two-color estimate both distinguishes the groups and stops.

**ARGUED (what the next link must do).** An inverse of the one-color operator solves the normal equations for infinitesimal changes of gauge: $B_Uv=(v_x-\operatorname{Ad}(U_{xy})v_y)_{xy}$ has $B_U^*B_U=\Delta_U$. A differentiable physical wavefunction has zero derivative along those gauge directions. The two-end estimate also controls propagation of a matrix between different sites in the defined spatial walk. To use it for the transfer trace one needs a Wilson expansion that maps a neutral excitation to paths of this kind, bounds the scalar weights, and prices intervals on which both ends coincide or fuse. The identity-matrix sector shows exactly what unrestricted coincident transport would carry. Equations (6) and (8) give the spatial bound needed on separated ends. The Wilson expansion remains a separate input.

### 6. A separate mechanism from quantum mechanics of matrices

**CITED (on file).** The finite constant-mode Hamiltonian has kinetic energy $-\sum_i\Delta_i$ and magnetic potential $g^2\sum_{i<j}|x_i\times x_j|^2$ on three spatial Lie-algebra vectors. At fixed $x_i$ a transverse oscillator obeys $-\partial_s^2+g^2|x_i|^2s^2\ge g|x_i|$. The quartic scaling gives energies proportional to $g^{2/3}$ in the reduced Hamiltonian. For $U(1)$ the bracket vanishes and this oscillator has zero frequency. Row 1273 already proves a confining form estimate and a discrete spectrum for the model in Lemma S. Its Lemma GA shows why an amplitude estimate for an open block cannot use the same argument: a pure gauge can have arbitrary local amplitude. Row 1193 also identifies the background spin term and the distinction between an absolute lower bound and an excitation energy. We drop the duplicate calculation. [Row 1273, Lemmas S and GA](gap-owner-threeaxis-opus.md) · [Row 1193, §1.2](gap-mini-solve-d-fable.md)

**ARGUED (closed-phase stopping point).** The estimates reached the Wilson measure on a fixed physical box and a subspace of the actual neutral transfer. The hand proofs above use no numerical experiment. The next comparison checks whether these estimates or their methods already have an owner.

## Phase 2. What survived comparison and how far it goes

**ARGUED (comparison outcome).** Row 1145 already proves the joint winding density bound. Rows 1141 and 1283 already prove the one-color pinning and the low-energy tail, with a stronger counting bound than the closed-phase estimate. Row 1273 treats the transverse oscillator. The two-color estimate can be sharpened to the scale $b$, including at contact. A second refinement bounds the change in the actual two-period trace ratio when long lines are added to arbitrary exterior observations.

### 7. A maximum-volume minor gives the natural two-color scale

**PROVED (random linear equations).** Let $B_i:\mathbb R^d\to\mathbb R^d$, $1\le i\le J$, be independent random matrices, also allowing independence conditional on a fixed exterior. Suppose that for every deterministic unit vector $z$ and every $i$,
$\mathbb P(\|B_i z\|^2\le h)\le \min(1,K h)$.
For $J\ge d$, $K d^2 v\le1$, one has

$$
 \mathbb P\!\left\{\lambda_{\min}\Big(\sum_iB_i^*B_i\Big)<v\right\}
 \le \left(\sum_{j=0}^{d-1}\binom{Jd}{j}\right)(K d^2 v)^{J-d+1}.
                                                                    \tag{9}
$$

There is no angular net at resolution $\sqrt v$ in this bound.

**Proof.** Put all the rows in one array. Suppose a unit vector $y$ has squared output norm $<v$ for the array. If the rows span dimension $\ge d-1$, pick $d-1$ actual rows spanning a parallelepiped of maximum $(d-1)$-volume $V>0$. Take a unit normal $z$ to them. For any other row $w$, append $w$ and compute the absolute determinant of the resulting square array. It equals $V|w\cdot z|$. In an orthonormal basis with last vector $y$, expand along the last column. Every cofactor has absolute value $\le V$, since projection decreases the volume of the other $d-1$ rows. The squared norm of the last column is $<v$ because these are distinct rows of the original array. Hence $V|w\cdot z|\le \sqrt{d v}\,V$. This applies to every row, with zero output on the selected ones. Every block obeys $\|B_i z\|^2\le d^2 v$. If the span has dimension $<d-1$, choose a row basis of it and any unit vector orthogonal to that basis. All outputs then vanish.

For each *prescribed* subset of up to $d-1$ rows, choose the unit vector in its orthogonal complement by projecting the first standard basis vector with nonzero projection and normalizing. This is a measurable rule and is a unit normal in the maximal-volume case (its sign is immaterial). Condition only on blocks containing these prescribed rows. At least $J-d+1$ independent blocks remain, each with failure probability at most $Kd^2v$. Take the union over prescribed subsets. The event that a subset is maximal was never put into the conditioning. This proves (9).

**PROVED (all soft channels of the pair).** In (6) replace $b^{1+\delta}$ by $b$. Include at $r=0$ the full eight-dimensional traceless matrix fiber. For each $p,q>0$ the bound then holds, with $B_n=b+(\log n)^{2/3}$, on the minimum over all these spaces at once. For $r\ne0$, the fixed-matrix cap bound before (7) gives $K=C b,d=9$. Use $J=10$. Equation (9) with $v=a z/b$ and a fixed sufficiently small $a>0$ gives a bad-anchor probability at most $z/16$.

At $r=0$ a loop acts by $Z\mapsto RZR^*$. For a fixed unit traceless $Z$, its skew or its symmetric part has Frobenius norm at least $1/\sqrt2$. Both subspaces are orthogonal and invariant. A skew matrix is the cross product with an axial vector, and its Frobenius norm is $\sqrt2$ times the length of that vector. Small motion of this part puts its unit axis in a cap of chord radius $C\sqrt h$ if $\|RZR^*-Z\|_F^2\le h$. For the other case let $S$ be the symmetric traceless part. Its largest and smallest eigenvalues differ by at least $1/\sqrt6$ because one has absolute value at least $1/\sqrt6$ and trace zero puts the other extreme on the opposite side of zero. At least one end eigenvalue $\lambda$ is isolated from the other two by $1/(2\sqrt6)$. If $w$ is its unit eigenvector, $\|(S-\lambda I)Rw\|\le\sqrt h$. Project onto $w^\perp$ using this gap. The vector $Rw$ lies within $C\sqrt h$ of either $w$ or $-w$. The tilted sphere-area bound (3) gives probability $\le C b h$ in both cases. This proves the fixed-vector premise of (9) for $d=8$. Use the same ten squares, now applying conjugation to the original rotations with no second plane. The box proof in §5 applies with $v=a z/b$ to every separation, including this contact restriction, and gives the asserted simultaneous probability and inverse moments.

It follows at $t=u$ and $2u$, for every fixed power $A>0$, that

$$
 0\le
 \mathbb E\sum_r\operatorname{tr}e^{-t\Delta^{(r)}}
      -\operatorname{tr}e^{-t\Delta_{\rm scalar}}
 \le C_A n^{-A}.                                                        \tag{10}
$$

The scalar trace occurs **once**, on the fields $f_x I_3$ at contact. Its multiplicity is spatial. To prove the upper bound split into the good and bad events as in (8), with dimension $\le9n^6$ and $p>A+6$.

**PROVED (the remaining channel fails the proposed purity test).** Write $Z_t(U)=\sum_r\operatorname{tr}e^{-t\Delta^{(r)}}$. Deterministically, the ordinary scalar eigenvalues on the torus are $4\sum_i\sin^2(\pi k_i/n)$ by testing Fourier characters. For $|k_i|\le n/(10\pi\sqrt u)$ each gives $e^{-u\lambda}\ge e^{-1}$. At $u=n/512$ there are at least $c n^{3/2}$ such modes for all large $n$. Hence $Z_u\ge c n^{3/2}$ on every Wilson field. Positivity of the generators gives $Z_{2u}\le Z_u$, so $Z_{2u}/Z_u^2\le C n^{-3/2}$. A replacement of the Wilson transfer by this synchronized two-color heat operator would predict failure in four-dimensional **SU(2)** even after complete suppression away from contact. This obstruction is internal to the proposed model and does not decide the Wilson purity.

### 8. A relative bound on the actual neutral traces, with arbitrary exterior data

**PROVED.** Fix the finite Wilson transfer and its ground state as in §4. In addition to the $N$ line readings $H$ of §4 retain any standard Borel observation $S$ of the other spatial links. For example, keep the entire exterior link configuration. Use the same observations at the two endpoints. Assume the sigma algebras of $S$ and $(S,H)$ are stable under slice gauge transformations and center flips. The full raw exterior and based holonomies satisfy this. Let $\Pi_F$ be projection onto all vectors $\Omega f(F)$, and put

$$
 Z_F(t)=\operatorname{Tr}\{\Pi_F P_0 A^t\Pi_F\},\qquad
 R_F(u)=Z_F(2u)/Z_F(u)^2.
$$

Gauge averaging and $P_0$ inside this trace discard nonphysical directions. On the full slice $R_F$ is the crux-card purity. For a partial observation the numerator uses the compression of $A^{2u}$. Orthogonal projection need not commute with $A^u$.

Write $a=(1-\epsilon_m)^N$, $h=(1+\epsilon_m)^N$, with $\epsilon_m<1$, and $D=(h-a)^2/a$. Uniformly in **all** allowed $S$ and $t\ge2$,

$$
 1\le\frac{Z_{(S,H)}(t)}{Z_S(t)}\le 1+D,\qquad
 (1+D)^{-2}\le\frac{R_{(S,H)}(u)}{R_S(u)}\le 1+D .                    \tag{11}
$$

In particular this step has a small *relative* error even if $Z_S(u)$ is large or $R_S(u)$ tends to zero.

**Proof.** In the stationary path proof of (5), implement $P_0$ by an independent uniform center shift of the last measured slice. The shifted spatial law is still the stationary marginal. The raw spatial kernel already averages vertex gauge. Conditional on the remaining links and the shift, the two $H$ readings are independent with densities between $a$ and $h$ relative to product Haar $m_H$. A center flip multiplies a loop by a fixed central sign and preserves product Haar. The two values of $S$ are fixed in that conditioning. For open transported segments the same argument applies: each center shift multiplies the product by its central crossing sign, and any endpoint gauge multiplies on the left or right. These maps preserve Haar.

Take finite partitions of the values of $S,H$. For a cell $C$ of $S$ let $\mu_C=\Pr(S_0\in C)>0$, $E_C=\{S_0,S_t\in C\}$ and $p_j=\Pr(H_0\in B_j\mid S_0\in C)$ on the $H$ cells of positive Haar mass $m_j$. Let $f_j,g_j$ be the probabilities of $B_j$ at the two ends conditional on the remaining links and shift. Each of $f_j,g_j,p_j$ lies in $[a m_j,h m_j]$. On $E_C$ the contribution to the finer partition trace for this $C$ is

$$
 \frac{1}{\mu_C}\mathbb E\!\left[\mathbf1_{E_C}\sum_j f_jg_j/p_j\right].
$$

This follows by using normalized indicators of $C\times B_j$ in the trace and the path identity. For the coarser partition its contribution is $\Pr(E_C)/\mu_C$. Since each probability list sums to one,

$$
 \left|\sum_j f_jg_j/p_j-1\right|
 =\left|\sum_j(f_j-p_j)(g_j-p_j)/p_j\right|
 \le \sum_j (h-a)^2 m_j/a=D .
$$

Sum over $C$. Nested subspaces give monotonicity of trace because $P_0A^t$ is positive. Use refining finite partitions of both observations and positivity as in (5). Both traces are finite for $t\ge2$, by the Hilbert–Schmidt property of $T$, and both include the vacuum contribution one. This proves the first pair of inequalities. Apply it at the two periods, with the same projections, to prove the second pair.

**PROVED (size and obstruction).** For the $n^2/4$ lines of §4 one can take $\epsilon_m\le C e^{-n/b}$ for $n/b\ge1$ from row 1145. For $N\epsilon_m\le1/4$, $(h-a)\le 2N\epsilon_m(1+\epsilon_m)^{N-1}$ by the mean value theorem and $a\ge1-N\epsilon_m$. Thus $D=O(n^4 e^{-2n/b})$. At the calibrated cutoff this tends to zero faster than any power of $n$. Nevertheless the paired central flips in §4 fix *both* the full unselected exterior and the measured holonomies when the two flipped links are on the same selected line. A plaquette containing just one of them still changes sign. This proves that even this large choice of $(S,H)$ is incomplete in the neutral sector. The relative loss in (11) controls precisely the displayed addition of observations. It gives no bound on the neutral information left inside the selected lines after their products are known.

**PROVED (a shrinking physical mesh and the low-energy Wilson states).** Fix $p>0$. At large calibrated cutoffs choose $m$ to be the least power of $L$ at least $(p+10)b\log n$. Then $m\mid n$, $m=O_{p,L}((\log n)^2)$, and $m L^{-k}\to0$. Start a straight segment of length $m$ in each positive coordinate direction at every site with $x_1+x_2+x_3=0\bmod m$. Denote **all** their products by $F_m$. Along each fine line the selected segments partition its links. Their endpoints form $m^2$ translated cubic lattices of side $n/m$ in coarse units. Thus there are $3n^3/m$ observed products. The observable graph contains order $n^3/m$ edge-disjoint contractible plaquettes: pack a fixed positive fraction of the $12$-plaquettes in each coarse lattice by skipping adjacent starts in directions 1 and 2. Their half-traces are independent nonconstant variables in product slice Haar since the fine paths are edge disjoint. Positivity of $\Omega$ gives the same null sets in the stationary slice. The neutral observation space is therefore nontrivial even after enforcing Gauss' law.

Split the segments into twelve classes by direction and the parities of the two transverse coordinates. The fine torus side is even. Within a class, no two selected fine links belong to a common plaquette. Each segment is read once. Products in every *other* class use unselected links and qualify as $S$ in (11). Open segments transform by left and right endpoint multiplication. Both the sigma-algebras and the product Haar bound used in (11) have the required symmetry. Add the twelve classes one by one. Each has at most $3n^3/m$ segments and $\epsilon_m\le C e^{-m/b}$. The multiplicative loss per class is $1+O((n^3e^{-m/b})^2)$. Starting from the constant observation, for $t=u,2u$ one obtains

$$
 1\le Z_{F_m}(t)\le 1+O_p(n^{-p}).                                     \tag{12}
$$

Let $E_H$ be the physical center-neutral spectral projection of $A$ onto eigenvalues at least $e^{-H/u}$, excluding the vacuum, for any fixed $H>0$. On this subspace $A^u\ge e^{-H}I$. Positivity on its orthogonal complement and the vacuum term one in (12) imply

$$
 \|\Pi_{F_m} E_H\|_{\rm HS}^2
 =\operatorname{Tr}(E_H\Pi_{F_m}E_H)
 \le e^H [Z_{F_m}(u)-1]=O_{p,H}(n^{-p}).                               \tag{13}
$$

This bounds the **total** overlap of the low neutral Wilson states with every function of the measured transports, even with a cutoff-dependent choice of functions. It uses the physical transfer itself. It places no upper bound on the number of low states in the orthogonal complement. Two central flips on the same length-$m$ segment leave all of $F_m$ fixed and change a plaquette that touches just one flipped link. Thus the missing neutral data persist as the physical mesh tends to zero.

**PROVED (complete coordinates with two readings per link).** Fix any admissible calibrated $L$. Let $m$ be the least power of $L$ at least $1+b(\log n)^2$. For all large $k$ it divides $n=\ell L^k$, is $O_L((\log n)^3)$, and satisfies $mL^{-k}\to0$. For each $s\bmod m$ start the mesh at all sites with $\sum_i x_i=s\bmod m$. Call the full list of products $F_{s,0}$. Make three further lists $F_{s,i}$, $1\le i\le3$. To form $F_{s,i}$ delete the first link of each direction-$i$ segment before taking its product. Keep the other two directions whole. Every list retains order $n^3/m$ edge-disjoint contractible plaquettes in its two whole directions. Each shortened product still has $m-1$ private links within its class. Products in the other classes only use unselected links, so (11)–(13) apply to each list.

In (12) the error per class is at most $C n^6 e^{-2(\log n)^2}$. There are twelve classes per observation and $4m$ observations. Thus for every fixed $H,p>0$,

$$
 \sum_{i=0}^3\ \sum_{s\bmod m}\|\Pi_{F_{s,i}}E_H\|_{\rm HS}^2
      =O_{H,p}(n^{-p}).                                                  \tag{14}
$$

For a link $(x,i)$ choose $s=\sum x_j\bmod m$. Read the full word $W_{x,i}$ in $F_{s,0}$ and its suffix $V_{x,i}$ in $F_{s,i}$. The product $W_{x,i}V_{x,i}^{-1}=U_{x,i}$, including across a seam. Every fine link is recovered with two readings. A fine plaquette requires eight. This uses raw transports in common endpoint frames and then a single physical projection. On a single mesh, flip two links in one whole segment in one direction. Every product stays fixed and a fine plaquette touching only one flipped link changes sign. Thus each list misses a neutral observable.

**PROVED (all matrix elements in an energy band).** Let $F$ be any of the $4m$ lists and $\nu$ product Haar over its words. Put $N=3n^3/m$, $\delta_n=(1+\epsilon_{m-1})^N-1=O(n^3e^{-(\log n)^2})$. Let $M_{f(F)}$ denote multiplication by a bounded complex function of one list. Let $E_\rho$ project onto all physical neutral eigenstates of $A$ with eigenvalue at least $\rho$, including the vacuum, for $0<\rho\le1$. Then

$$
 \big\|E_\rho M_{f(F)}E_\rho-\nu(f)E_\rho\big\|
       \le \rho^{-2}\delta_n\,\nu(|f|).                                  \tag{15}
$$

Codex, row 1215 (29), uses the two-step insertion kernel to bound a vacuum-to-band vector for one commensurate grid and coarse face signs. Use that method here. Fix the two outer slices of a two-step path. At the middle slice, condition in turn on all links outside each of the twelve classes, expanding the two gauge integrals as in §4. The density of the class relative to its product Haar lies between $(1-\epsilon_{m-1})^{N_j}$ and $(1+\epsilon_{m-1})^{N_j}$ for $N_j$ words. For a nonnegative function of the whole list, replace its class argument by Haar integration with this upper bound. The resulting function depends only on the remaining classes. Integrate under the original conditional law and repeat. The lower bound follows by the same iteration. Thus the density of the *whole list* in every two-step bridge is between $(1-\epsilon_{m-1})^N$ and $(1+\epsilon_{m-1})^N$. Its distance from one is at most $\delta_n$. This also bounds each individual list marginal under any positive mixture of such bridges. [Earlier two-step insertion, row 1215, (28)–(29)](gap-solve23-astra62.md)

It follows pointwise in the outer links that the kernel of $B=A M_{f(F)}A-\nu(f)A^2$ has absolute value at most $\delta_n\nu(|f|)A^2(X,Y)$. Pair the bound against the absolute values of two test vectors. Since $\|A^2\|=1$, it gives $\|B\|\le\delta_n\nu(|f|)$. Invert $A$ on $E_\rho$ at both ends to obtain (15). For normalized states in this band, even superpositions of excited states, every event of Haar probability $v$ has probability within $\rho^{-2}\delta_n v$ of $v$. The same bound controls off-diagonal matrix elements between orthogonal band states. At physical cutoff $H$ take $\rho=e^{-H/u}$. Equation (14) separately controls the sum over vacuum-to-state overlaps, without a factor for the band dimension.

**PROVED (dependence between meshes at the two actual neutral periods).** In a spatial slice of the neutral Wilson law of period $t=u$ or $2u$, denote by $P_t$ the joint law of the $4m$ lists. Let $Q_t$ draw each list independently from its own true marginal. Use adjoint transports alone for the following event. Take the $K=n^3/4$ direction-12 plaquettes whose base has its first two coordinates even. They are edge disjoint. Reconstruct each plaquette from its eight readings as above, now in $SO(3)$. Use the adjoint trace divided by its dimension, $C_p=\operatorname{tr}(\operatorname{Ad}U_p)/3$ for $SU(2)$. Let $D$ be the event that at least $K/2$ have $1-C_p\le\beta^{-1/2}$. For all sufficiently large calibrated cutoffs and absolute positive constants,

$$
 P_t(D^c)\le e^{-cK\sqrt\beta},\qquad
 Q_t(D)\le e^{-c'K\log\beta},\qquad
 D_{\rm KL}\!\left((\mathbf1_D)_*P_t\,\middle\|\,(\mathbf1_D)_*Q_t\right)
       \ge c'' n^3\log\beta.                                             \tag{16}
$$

Here $(\mathbf1_D)_*P$ is just the distribution of the binary answer under $P$. For the first bound use Codex, row 1155 (9) and the unnormalized temporal-twist extension before its (30). For a prescribed set of $K$ spatial plaquettes, their estimates give $\mathbb E_{P_t}\exp[c_0\beta\sum_p(1-w_p)]\le8 C_0^K$, where $w_p$ is the fundamental half-trace. Indeed the temporal seam can be away from this slice, and the sum of the eight twisted masses in untwisted units is at least one. The character identity $C_p=(4w_p^2-1)/3$ gives $1-C_p\le(8/3)(1-w_p)$. On $D^c$ the sum of $1-w_p$ is at least $3K/(16\sqrt\beta)$. Exponential Markov gives the first inequality. [Marked plaquettes and the mixture of temporal twists, row 1155](gap-solve7-astra62.md)

For the second bound, the two neighbors of this slice and the fixed temporal twist give a positive mixture of two-step bridges. The seam may be put elsewhere. The whole-list density bound above therefore holds under each true marginal, also after pushing forward to the adjoint group. The product $Q_t$ has density at most $(1+\delta_n)^{4m}\le2$ relative to fully independent Haar readings for large $n$. In the eight factors of each tested plaquette and across all tested plaquettes, no coordinate **of a specified list** is used twice. This follows because the fine plaquettes have disjoint edges, and each directed fine edge uses a distinct whole word and a distinct suffix. Thus under the fully independent law the reconstructed plaquette rotations are independent Haar rotations. For Haar $SU(2)$ the angle $\theta\in[0,\pi]$ has density $(2/\pi)\sin^2\theta$, by area on $S^3$. Since $1-C_p=4\sin^2\theta/3$, its probability to be at most $v$ is $\le C v^{3/2}$ by integration near the two endpoints. A union over successful subsets costs at most $2^K(C\beta^{-3/4})^{K/2}$. Include the density factor two to obtain the second inequality. The relative entropy of a binary event is at least $P_t(D)\log(1/Q_t(D))-\log2$, which proves the last bound. The test only compares a binary gauge-invariant function with the law obtained by sampling the lists separately. It does not count exact equalities of duplicated coordinates.

For compact $U(1)$ all adjoint readings equal the identity. The same binary test then has probability one under *both* laws and relative entropy zero. Three spatial directions supply $K$ of order $n^3$ and leave two whole directions in every shortened list. At $\beta=0$ in $SU(2)$ the disjoint fine plaquettes themselves have independent Haar products. The concentration step uses their actual weak-coupling action.

**PROVED (cost in the full neutral purity).** Let $J_D$ multiply by the indicator of the joint event, evaluated on the actual slice. It commutes with center and gauge projections. Form the density matrix $\rho_D=J_D P_0 A^u J_D/\operatorname{Tr}(J_D P_0 A^u J_D)$. The projection identity of row 1149 (34) applies to this adjoint event. If $\mathcal P$ denotes the full neutral purity, then

$$
 \frac{\operatorname{Tr}\rho_D^2}{\mathcal P}
   =\frac{P_{2u}(D\text{ on slices }0,u)}{P_u(D)^2}
   =1+O\big(e^{-c n^3\sqrt{\beta}}\big).                               \tag{17}
$$

Indeed the trace of the square puts the same multiplication at both joins of the two $u$-step kernels. Commutation and $P_0^2=P_0$ leave one neutral projection. Translation in time and the first bound of (16) bound the probability of missing either join by $2e^{-cK\sqrt\beta}$. Apply (16) once in the denominator. Thus a subspace which has exponentially small probability under independently sampled mesh data carries the full neutral purity with the displayed relative accuracy. Its internal eigenvalue multiplicities still matter. [Projection identity, row 1149, (34)](gap-solve4-astra62.md)

**PROVED (absolute trace at the scale of one weak-coupling plaquette, using row 1153).** Tighten the threshold in $D$ to $\alpha/\beta$ for a sufficiently large *fixed* $\alpha$. Denote the event by $D_\alpha$, its complementary multiplication projection by $J_{\rm bad}$, and take $t=u,2u$. On a bad slice $\sum_p(1-w_p)\ge3K\alpha/(16\beta)$. The same moment bound gives $P_t(D_\alpha^c)\le8(C_0e^{-3c_0\alpha/16})^K\le e^{-c_\alpha n^3}$. The independent Haar success probability in (16) is now at most $C(\alpha/\beta)^{3/2}$. Hence $Q_t(D_\alpha)\le e^{-cK\log\beta}$ again. To convert the first probability into an *absolute* trace use Codex, row 1153 (5). In its notation, at an even lattice period $s=2\lceil\log(2+\beta)\rceil$ one has $s^3\log\operatorname{Tr} A^s/n^3\to\pi^2/15$. Its assumptions $s^4\beta^{-1/4}\log^{3/2}(2+\beta)\to0$ and $n\ge2(\lfloor\beta^{1/4}\rfloor+1)^2$ hold along the calibrated trajectory. Since $t\ge s$ eventually and $0\le A\le I$, $\log\operatorname{Tr} P_0 A^t\le\log\operatorname{Tr} A^s=o(n^3)$. Absorb this smaller term in the probability exponent. For each fixed $H>0$ this gives, with a possibly smaller $c_\alpha>0$,

$$
 \operatorname{Tr}(J_{\rm bad}P_0 A^tJ_{\rm bad})\le e^{-c_\alpha n^3},
 \qquad
 \|J_{\rm bad} E_{e^{-H/u}}\|_{\rm HS}^2\le e^H e^{-c_\alpha n^3}.        \tag{18}
$$

The second inequality follows from $P_0 A^u\ge e^{-H}E_{e^{-H/u}}$ and includes the vacuum. Equation (18) bounds the total low-band mass on the discarded set with no input on the band rank. In (17) the tighter event gives relative error $O(e^{-c_\alpha n^3})$. These absolute bounds use the cited short-period trace asymptotic. Equations (14)–(17) use the private-link and marked-plaquette bounds without that asymptotic. [Short-period thermal trace, row 1153, (5)](gap-solve6-astra62.md)

**ARGUED (implication for a transfer proof).** In the physical neutral ensemble a joint adjoint reading already detects extensive dependence at both periods, while each list has the band estimate (15). Replacing these lists by independent laws fails quantitatively on (16). The estimate is on one time slice at a time. A proof through joint readings still needs an upper bound on the total two-time weight of their *centered* fluctuations. Even its large mean at both periods can be carried by the vacuum. Equations (11) and (14) bound how much of the excited trace the single lists can see. They leave its mixed-observable complementary part open.

### 9. Ownership, sources and the campaign tests

**ARGUED (registry comparison at the pin).** I searched the crux-card families for covariant and connection Laplacians, private pivots, winding frames, point-split adjoints, inverse moments, compressed traces, common-axis tails, random matrix minors and transverse oscillators. I followed the matches to the original rows. The registry's R10, R11, R12, TWO-PER and VIR-DOWN concern a posterior covariance, a virial bound or a carry in the bare coupling. WMIX-SLICE concerns the whole slice. ANISO-TAIL concerns two ends of the spatial-coupling axis. The follow-up comparison also covered the two-step bridge, energy-band insertions, joint mesh laws and entropy against marginal products. Rows 1153, 1155 and 1215 provide inputs to §8. I found no owner for the relative-trace lemma, the simultaneous overlap and reconstruction, or the binary test (16)–(18). No entry inspected supplies the full purity bound. [Open registry, final two tables](open-registry.md)

| Candidate | Nearest phrase on file | Decision and exact difference |
|---|---|---|
| Perimeter smoothing and the axis test (1)–(2) | Row 1145, “joint density relative to product Haar”; row 1656, “small-energy volume with its angular law”. | **ARGUED — method on file.** Row 1656 estimates the pairwise commutator energy $\sum_{i<j}\vert x_i\times x_j\vert ^2$ and selects an extreme frame. (2) estimates the least **adjoint displacement of a single unit vector** and gives its exact inverse-moment endpoint for two and three spatial periods. This is a new statistic in the comparison, not a new winding method. [Row 1145](gap-solve2-astra62.md) · [Row 1656, stages 3–4](gap-newmath-astra62-max.md) |
| Pinning one adjoint field | Row 1283, “two independent directions of curvature”; row 1675, “no inequality bounding the absolute neutral trace”. | **ARGUED — on file.** The prior controls rare low modes, its count has both signs, and it already exhibits the scalar-sector obstruction. Nothing in §3 is counted as new. [Row 1283](gap-solve32-astra62.md) · [Row 1675](gap-direction9-check-astra62.md) |
| The two-color matrix field and selection of rows (6)–(10) | Row 1283 (11), “$R_e q=X_e qY_e^{-1}$”, for fundamental quaternions on adjacent time slices. | **ARGUED — new result and proof step within the existing box method.** That row bounds a Dirichlet Green function. Its single-loop angle mismatch can move *every* unit quaternion. An adjoint pair always has an exactly fixed rank-one matrix for each individual rotation pair (use its two axes). Several loops and the maximum-volume selection in (9) control these common approximate solutions at scale $1/b$. The result covers every nonzero spatial displacement and isolates the exact scalar contact spectrum. Row 1283 (12) also cautions against importing a Green bound into an interacting covariance. [Actual two-slice comparison](gap-solve32-astra62.md) |
| Relative trace under added observations (5), (11)–(14) | WMIX-SLICE, “whole-slice law”; row 1178, “exact heat trace as observable dependence”. | **ARGUED — new partial estimate, with prior compression and conditional smoothing credited.** Row 1178 identifies the compressed Doob kernel and reconstructs the neutral slice from *all* local double and triple plaquette readings. Row 1149 (34) controls the log purity cost of a high-probability sign projection. Row 1323 (5) samples an electric spin congruence class. Our partition identity bounds an added family of line variables relative to **any** permitted exterior observations. The cost is quadratic in their conditional density oscillation. Equations (13)–(14) sum overlaps with the actual low-energy projector. A paired flip proves that each individual mesh misses a neutral plaquette. A full word and its suffix from two lists reconstruct each fine link, at every admissible blocking factor. [WMIX-SLICE, Theorems 1A–2](gap-wmix-solve-neon.md) · [Row 1178](gap-solve18-astra62.md) · [Row 1149](gap-solve4-astra62.md) · [Row 1323](gap-solve39-astra62.md) |
| Band elements of one mesh (15) | Row 1215 (29), “vanishing low-energy spectral weight”; GLUE2 Lemma C2, “local total variation”. | **ARGUED — insertion method on file.** Row 1215 bounds one vector obtained by applying a centered observable to the vacuum. Its commensurate grid includes signs and straight transports at step at least $\sqrt n$. Its inserted-kernel bound already permits inversion at both ends. We use that observation on the staggered full and shortened lists, with a relative bound for rare events. GLUE2 compares the seam observation in two ensembles. [Row 1215](gap-solve23-astra62.md) · [GLUE2, C2](gap-glue2-opus.md) |
| Mixed adjoint reading and its cost in the Wilson purity (16)–(18) | Row 1155 (9), “many good blocks”; row 1149 (34), a cut on sign defects; row 1153 (5), “thermal sum”; row 1178, affinity to a product of two marginals. | **ARGUED — new combination and quantitative result.** The marked-face moment, projection identity and small-time trace are on file. Here a single binary test of overlapping adjoint lists distinguishes their joint law from independent *true* list marginals on one slice at each target period. The Haar probability of a ball near the identity is cubic in its small angle. This gives the logarithmic factor for the binary entropy. The sector accepted by this test carries the full neutral purity to the relative precision (17), and the tighter version has the absolute discarded weight (18). Row 1178 compares opposite slices of an ordinary cylinder. [Marked faces](gap-solve7-astra62.md) · [Projection](gap-solve4-astra62.md) · [Short-period trace](gap-solve6-astra62.md) · [Opposite-slice comparison](gap-solve18-astra62.md) |
| Zero-point energy of matrix valleys | Row 1193, “zero-point closing of flat valleys”; row 1273, Lemma S. | **ARGUED — on file.** The earlier work already supplies the reduced oscillator and the open-block obstruction. The missing step is a comparison of the interacting, vacuum-normalized singlet levels and their multiplicities. [Row 1193](gap-mini-solve-d-fable.md) · [Row 1273](gap-owner-threeaxis-opus.md) |

**CITED (account and its scope).** Ethan Sussman and Levent Alpoge, text with Claude and Codex, *YM4 outline* and *Theorem 0 complete account*, supplied revision 31a47c543775 (2026). I used the full-read index, the neighboring chunk entries and the obligations before reading these source ranges.

- Outline 2195–2244, GL3–GL4, computes the positive Bessel multipliers. Outline 2313–2336, GL8, gives the gauge projection, positivity and $\operatorname{Tr}L^s=Z_s(0)$ on the cubic torus. Our stationary cylinder uses the magnetic half-weight sandwich in the card's Lean kernel. The compressed traces must use that same realization and its Perron vector. [Index, chunk 02](sa-index/chunk-02.md)
- Outline 766–779 proves the free scalar block-constrained lower bound. Outline 10978–10982, PX72, uses the norm of a covariant field on a full stencil. Outline 12787–12796 defines the positive componentwise Laplacian for a *constrained background*. These are different operators or ensembles from the random two-end operator in (6). [Chunk 01](sa-index/chunk-01.md) · [Chunk 10](sa-index/chunk-10.md) · [Chunk 11](sa-index/chunk-11.md)
- Outline 2614–2618 derives finite-support gauge invariance from the conditional Haar law. Its coarse-holonomy remark, 8099–8104, controls the local logarithm of a ratio at a background field. At 28393–28401 the argument assumes convergence of centered separated moments for two state sequences. The index search for bridge laws, marked faces and relative entropy gave no bound between the mesh laws in (16). [Chunk 02](sa-index/chunk-02.md) · [Chunk 07](sa-index/chunk-07.md) · [Chunk 26](sa-index/chunk-26.md)
- Outline 20781–20805, RF24–25, stops at first passage through the weak window under its construction inputs. CA-I 3636–3653, Lemma 4.2:lem-first-passage, gives the corresponding conditional arithmetic. Outline 31870–31883 uses the spectral measure $E e^{-E}dE$ to distinguish polynomial decay from a gap. CA-I 2704–2710 expressly excludes a mass gap and vacuum uniqueness from the assertion there. Given any fixed comparison length $s_*>0$ from the weak window, choose $\ell=1024(1+\lceil s_*\rceil)$ after fixing the calibration. Then even the short physical period $\ell/512$ exceeds $s_*$. The estimate sought beyond the weak window is the neutral thermal trace at time $\ell/512$. No imported Balaban bound is used for it. The local Balaban digest identifies ultraviolet background and propagator results. [Chunk 19](sa-index/chunk-19.md) · [Chunk 29](sa-index/chunk-29.md) · [Outline obligations](sa-index/obligations.md) · [Balaban digest](lit-balaban.md)

**ARGUED (six tests of row 1553).** In (g1), the step that fails for weak 4D compact $U(1)$ is the spherical cap estimate for a moving color. Its adjoint fixes every vector, even at nonzero separation. The binary relative entropy in (16) is then exactly zero. Winding-density smoothing and the relative-trace proof by themselves survive the abelian comparison. In (g2), a fourth spatial direction changes the number of independent anchors in the proof of (6) from order $R^3$ to order $R^4$. There is no demonstrated dynamical failure of the color-pinning argument for weak 5D $SU(2)$. In (g3), the abelian adjoint also fixes its color at strong coupling and in 3D. The algebra test alone cannot distinguish the gapped twin. In (g5), (10)–(18) use a growing lattice cube $n=\ell L^k$ at fixed physical side $\ell$ and calibrated $\beta_k$, and the mesh in (12) shrinks in physical units. The local estimates themselves sample short distances. At fixed $n$ and growing $\beta$ the private-link smoothing condition fails, while (6) simply weakens. [Six tests, §1.5](gap-mech-direction4-fable.md)

**PROVED (why the statistical step survives weak compact $U(1)$).** A conditional circle link is a translate of $q_\kappa(\theta)\propto e^{\kappa\cos\theta}$ with $\kappa\le6\beta$. Put $h=(1+\kappa)^{-1/2}$. Its density is at least $c/h$ on $[-h,h]$ and at most $C/h$ everywhere. For the normalizer, integrate on $[-h,h]$ for the lower bound and use $1-\cos\theta\ge2\theta^2/\pi^2$ on $[-\pi,\pi]$ for the upper bound when $\kappa\ge1$. Bounded $\kappa$ gives both bounds directly. The Fourier coefficients are nonnegative by the product series of $\exp(\kappa e^{i\theta}/2)$ and its conjugate. For each integer $j\ne0$, integration on $[-h,h]$ gives
$1-\widehat q_\kappa(j)\ge c[1-\sin(jh)/(jh)]\ge c'\min(1,j^2 h^2)\ge c'h^2$. The middle bound follows from the quadratic Taylor limit at zero, strict positivity away from zero and the limit one at infinity. The first and last densities of a product of $m$ independent links have centered $L^2$ norm at most $C b^{1/4}$ by the sup bound. Each middle convolution has norm at most $1-c'/b$ on mean-zero $L^2$, by Fourier expansion. Cauchy–Schwarz against the translated endpoint gives sup error $\le C b^{1/2}e^{-c'(m-2)/b}$. Thus the premise of (11) is available in the photon comparison at these lengths. The nonconstant adjoint measurement and the separated-color inequalities are the parts that disappear there.

**PROVED (g4, information lost to a spectator).** Tensor the Wilson transfer with the positive two-state Markov matrix having diagonal $(1+a)/2$ and off-diagonal $(1-a)/2$, $a=e^{-1/n^2}$. Its eigenvalues are $1,a$ and its center action is trivial. All Wilson slice statistics stay fixed. When only gauge data are measured, the compressed subspace includes just the constant spectator state. The full purity is multiplied by $(1+a^{2u})/(1+a^u)^2\to1/2$ at the stated aspect. Since the purity of the original factor is at most one, the product eventually falls below $457/625$. This is the spectator comparison of row 1675, applied directly to the present observables. It proves non-equivalence on this larger transfer class. [Prior spectator test](gap-direction9-check-astra62.md)

**ARGUED (g6 and the remaining estimate).** Equation (11) gives an actual observation step and its loss, including for a base carrying a spectator. It stops before the short relative products needed to reconstruct the fine slice. For a quantitative target, let $F$ be the algebra in (12), and let $Z_\perp(u)$ be the trace of $P_0 A^u$ on its orthogonal complement, meaning the trace of the compression there. If $Z_\perp(u)\le 25/\sqrt{457}-Z_F(u)$, the vacuum term at $2u$ alone gives the target. This trace decomposition locates the remaining cost. A supplier would have to bound the two-end dependence of the **relative detour and contact readings** inside each coarse segment after conditioning on its product, with total loss below the indicated budget. The common segment cancels exactly on a closed detour. Equations (16)–(18) control one-time concentration on the accepted configurations at both periods. They leave open the absolute excited weight inside that set. The spatial two-color heat model leaves a scalar branch with diverging trace. Neither result supplies this Wilson comparison. In particular we have no full (g1)–(g6) exception or new passing cutoff.

### 10. Papers for the reading lane

**ARGUED (reading priorities).** These are questions for full reads. No theorem from these papers is used to close a step here. “UNVERIFIED” marks entries whose text or applicability could not be checked in the permitted local corpus.

| Paper | Question for the full read |
|---|---|
| M. Lüscher, *Properties and uses of the Wilson flow in lattice QCD*, Journal of High Energy Physics **08** (2010), 071, arXiv:1006.4518. | Which parts of smoothing a field at a fixed physical radius can be proved configuration by configuration? Can the resulting centered curvature observable be represented in the joint lists with a bound on its two-time insertion? [Local reading, F1](prior/gap-outside-read-opus.md) |
| J. Fröhlich and T. Spencer, *Massless phases and symmetry restoration in Abelian gauge theories and spin systems*, Communications in Mathematical Physics **83** (1982), 411–454. | Which gauge-invariant reading carries the long-range photon fluctuation? Can it be expressed through the relative products of raw abelian transports, even when the adjoint test (16) is constant? [Local bibliographic record](prior/gap-r8-lit-criterion-luna.md) |
| A. S. Bandeira, A. Singer and D. A. Spielman, *A Cheeger inequality for the graph connection Laplacian*, SIAM Journal on Matrix Analysis and Applications (2013). **UNVERIFIED here.** | Can a bound on frustration of a section control the nearly invariant subspace for a tensor representation after the scalar contact line is removed? Track the fiber-dimension dependence. |
| R. Kenyon, *Spanning forests and the vector bundle Laplacian*, Annals of Probability (2011). **UNVERIFIED here.** | Does a positive expansion survive for the real rank-nine pair, or does taking higher-rank traces reintroduce signed weights precisely at coincident paths? |
| M. Gu and S. C. Eisenstat, *Efficient algorithms for computing a strong rank-revealing QR factorization*, SIAM Journal on Scientific Computing (1996). **UNVERIFIED here.** | Can row selection reduce the dimension loss in (9) for increasing Peter–Weyl spin while leaving the unselected random blocks independent? |
| M. Lüscher, *Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories*, Communications in Mathematical Physics **54** (1977), 283–292. | What operator on the physical slice would a displaced two-color path actually insert? Does the contact contribution have a sign or a vacuum subtraction after gauge projection? [Bibliographic record in the checkout](prior/gap-lit-grok-paths.md) |
| K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Annals of Physics **110** (1978), 440–471. | In the convergent strong-coupling expansion, which connected singlet terms survive when two open color paths meet? Can their exact combinatorial weight be separated from the small-coupling estimate? [Bibliographic record in the checkout](prior/gap-lit-grok-paths.md) |

**ARGUED (disposition).** Equations (11)–(15) control individual line measurements in the actual neutral transfer. Equations (16)–(18) quantify the dependence between them and its cost in the full purity. Equations (9)–(10) give the separate two-color estimate and its scalar contact obstruction. All new proof steps are by hand. No independent proof check or Lean rebuild was performed. This note grants no audit or scientific status.
