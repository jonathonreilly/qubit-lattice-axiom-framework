# Repo search

The target-specific prior digest is absent. The lead’s `prior/repo-search-2026-11-08.md` is a search for row 531’s RG suppliers, not for the new L3 lemmas. Its nearest hits are a strong-coupling transfer result and a noncompact covariance comparison. I checked `pr/10114` (`f76f6c649cff7dffbab664d8976e680e8f287fe9`), soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–35,106–149`: a fixed-spacing strong-coupling endpoint and a positive one-step witness, not a response-to-mixing consumer. I checked main at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`: a different noncompact Dirichlet law, not a supplier here. These results are credited to their repository authors; neither is rederived or imported. I did not repeat the lead’s searches of PRs 10133, 10134 and 10141 or read unrelated RG hits. This is bounded source verification, not an exhaustive absence theorem.

The actual prior results used below are the named local rows 691, 708, 1011, 1018, 1118, 1120, 1121 and 1122. This task checks their new assertions rather than reopening their research targets. No matching owner or completed check was found under the target and hypothesis names in `open-registry.md`.

Written by GPT-6 Astra (configured reasoning effort: xhigh). This research-text check grants no scientific or audit status and claims no mass gap.

## Plan

1. Read target prior work, GOAL, required FINISH and workflow rules, registry ownership, and the lead’s repository search; locate exact source ranges.
2. Check Proposition J(a,b), gauge randomization, concavity, and the Pbar and G_1 lower bounds.
3. Check Lemma JI, data processing, the degree remark, and Lemma TS3(a,b).
4. Check Lemma AFF and Example PROD, including extremality, observable dependence, pinned-cell covariance, and thermal-sum factorization.
5. Check Lemmas BACK, GM, TILT, the DS-W count and constants, and remark J3.
6. Assess the three-kind verdict at its stated grade, record precise scope and corrections, and finish with one RESULT line.

Every proof check is analytic and Lean-formalizable in principle; computations cannot discharge an obligation. Sources are credited where used. Only this file will be edited; no commit.

Save-protocol note: the first write attempted the repository-root library path and failed because that directory does not exist; this file is in the requested loop folder. Scratch/download directory: /tmp/sa-gap-l3-closure-check-astra.7q0q0W.

## Step 1 result — scope and sources

HEAD is the requested `14be730194ba672681713f3acff887a9596b0d75`. It is detached; only the requested output is untracked. GOAL and the required FINISH sections were read. The workflow is absent in this sparse checkout; main’s workflow map, Rules, and check procedure were read through Git. The explicit one-output/no-commit instruction controls over their normal record/commit delivery. Planning was read without checkout. No audit, launch, subagent, numerical job, commit or post was run.

Both Sussman–Alpoge sources were fetched once into the fresh scratch directory above. The outline index README, chunk 01’s theorem and spectral-example rows with neighbours, chunk 29’s scope rows, and obligations 16–30 and 1495–1500 locate SA 114–130, 588–600 and 31871–31882. Those passages discuss component clustering and explicitly separate a positive gap from polynomial decay. CA-I 2700–2715 expressly excludes clustering and a mass gap from its stated theorem. The 4.12–4.19 index was searched: its path swaps and operator Neumann series are different objects. These bounded reads supply scope, not a proof of L3. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Tadeusz Balaban for the RG method behind the account. No Balaban paper or estimate is imported here.

The row-1122 direction note has been read in full, with truncated passages recovered in bounded reads. The exact checked targets are row 1121 step 8, row 1120 §§5.2–5.3, row 1122 §§3–4, and row 691 §§3,4,6. Later entries will separate each algebraic assertion from any extrapolation beyond its hypotheses.

## Step 2 result — Proposition J and its numerical lower bounds

Source: Claude Opus 5.5, `gap-conv-in-law-check-opus.md:132–160` (row 1121), using the cell geometry of Claude Fable’s rows 1011 and 1018 and the replica construction of row 1118 (Codex/Astra). The replica-exchange method is credited there to Arka Adhikari and Sky Cao, and to Oliver Redner, Jonathan Machta and Lincoln Chayes. This check does not import a finite-group weak-coupling estimate for SU(2).

**J(a): HOLDS. J(b): HOLDS.** The state class matters: cubic periodic Gibbs laws and their local limits, with their gauge/O(4) and lattice symmetries. The sheet assertion is not asserted here for an arbitrary symmetry-broken Gibbs state.

| Source line | Verdict | Check |
|---|---|---|
| 140, 4D geometry | HOLDS | With lower-end anchors, block `c+(1,1,1,0)` owns precisely the l direction-4 links at `(l,l,l,s)`, `0<=s<l`, on this cell. For each such link there are three cell plaquettes, based at `x-e_mu`, `mu=1,2,3`. Each lies on two boundary faces, hence has weight 1/4. The other three links belong to other blocks. No integrated-core variable occurs in these plaquettes. |
| 140, sheet geometry | HOLDS | The diagonally opposite owned corner has two incident ring bonds of half weight and no core neighbour. The other admissible anchor offsets select the corresponding opposite corner. |
| 142–146, cost | HOLDS | The part of `Z_c` depending on the selected edge/corner is a multiplicative ring-only factor. Its complement cancels exactly in the log cross-difference. Thus the displayed sum, and the sheet expression `2b d_x.(d_y+d_z)`, have no hidden core term. |
| 148, gauge randomization | HOLDS | A local gauge change preserves each full Gibbs law by DLR and Haar invariance. Adjoin independent Haar frames g,h, then apply g inverse to the first hybrid. Its swapped edge has relative frames `k_x=g_x^{-1}h_x`; these are independent Haar variables, independent of the original two configurations. In each selected plaquette an endpoint frame occurs exactly once. Conditional integration of that frame gives a Haar holonomy and mean trace zero. The second hybrid is treated separately; independence between different plaquettes is neither needed nor claimed. |
| 148, mean | HOLDS | The two original plaquettes have mean Pbar each, so `E Delta=(3/2) beta l Pbar`. On the sheet, zero one-spin mean and independent replicas give `E d_x.d_y=G_1/2`, hence `E Delta=2b G_1`. |
| 150, concavity | HOLDS | `D_c>=Delta_+`, `0<=Delta_+<=M`, and the chord inequality gives `1-exp(-D_c)>=((1-exp(-M))/M)Delta_+`. Also `E Delta_+>=E Delta`. The bounds `M=3 beta l` and `M=4b` follow term by term. This proves precisely J(a,b); no concentration is used. At zero coupling take the continuous limiting interpretation. |

For a general mixed simple plaquette, the same argument works at any vertex where the replica label changes along its four-edge cycle. This gives a Haar holonomy marginal. It does not give independence of the holonomies of many mixed plaquettes.

**Section 8.3: HOLDS AFTER CORRECTION.** The first missing term is at source line 158. The preceding line correctly counts `3N+1` free links, but division by `6 beta N` must retain the entropy of the extra link. The corrected bound is

```math
 \bar P\ge {r^2+r^4\over2}-{\mathrm{KL}(a)\over2\beta}
       -{r^2-r^4\over2L}-{\mathrm{KL}(a)\over6\beta L^4},
 \qquad
 G_1\ge r^2-{\mathrm{KL}(a)\over2b}.
```

The finite-volume omission is a failure of the displayed derivation, not a counterexample to the bound without that term. It is unnecessary to decide whether other unused positive tree contributions could recover it.

Here are the individual checks and a fully analytic certificate for the constants used downstream.

1. **Convexity (156): HOLDS.** With normalized Haar reference, `f(beta)=log Z_N(beta)` has `f(0)=0`, `f''=Var(sum t_p)>=0`, and `beta f'(beta)>=f(beta)`. Cubic symmetry gives `f'=6N Pbar` (sheet: `2N G_1`). This uses the actual torus state, not an arbitrary DLR phase.
2. **Axial-gauge identity (157): HOLDS.** Root a spanning tree. Choose site frames recursively so each tree link becomes the identity. The remaining link variables are left/right translates of the original ones. Conditional Haar integration, starting from the leaves, has Jacobian one. Thus a gauge-invariant integral equals its tree-fixed integral with independent Haar reference on the non-tree edges. The proposed tree has `N-L^3` non-cut temporal edges and `L^3-1` edges in one spatial slice: `N-1` edges, leaving `3N+1` free links. This is the elementary compact-group tree identity; Adhikari–Cao’s finite-group version is historical credit, not its analytic justification.
3. **Product trial (157): HOLDS.** For `q_a(dU)=exp(a t(U))dU/z(a)`, conjugation and inverse symmetry give `E_q U=r I`, with `r=z'/z=I_2/I_1` and `0<=r<=1`. A simple plaquette with k free edges has mean `r^k`, including inverse edges. The `3N(1-1/L)` non-cut temporal plaquettes have at most two free edges; the remaining plaquettes have at most four. The Gibbs variational lower bound is just Jensen applied to `exp(beta sum t-log(dq/dHaar))`. Its entropy is `(3N+1) KL(a)`. This gives line 157 and the corrected display above. For the sheet, independent tilted S^3 spins have mean `r e`, so every bond mean is `r^2`; its entropy is `N KL(a)`.
4. **Bessel values (159): HOLDS AFTER CORRECTION from equalities to certified bounds.** At `a=2`, Haar integration on S^3, or its even moments, gives

```math
 z(2)=I_1(2)=\sum_{k\ge0}{1\over k!(k+1)!},\qquad
 I_2(2)=\sum_{k\ge0}{1\over k!(k+2)!}.
```

For either series retain terms `k=0,...,5`. The remainder starting at `k=6` is bounded by that first omitted term divided by `1-q`, with `q=1/56` for I1 and `q=1/63` for I2. The ratios only decrease thereafter. These rational sums give

```math
 1.59063<I_1(2)<1.59064,\quad .68894<I_2(2)<.68895,
 \quad .4331<r(2)<.4332.
```

These inequalities can be checked by multiplication of the displayed factorial denominators; no floating-point value is a premise. To bound the logarithm, put `v=(z-1)/(z+1)`. The first lower bound gives `v>.22798`, and

```math
 \log z=2\sum_{j\ge0}{v^{2j+1}\over2j+1}
 >2\left(.22798+{.22798^3\over3}+{.22798^5\over5}\right)>.464.
```

All decimals in these inequalities denote exact rationals. Therefore `KL(2)=2r-log z<.4024`. They imply `(r^2+r^4)/2>.11137`, `r^2>.18757`, and, for `L>=20`, `(r^2-r^4)/(2L)<.00382`. At `beta,b>=2.3`, `KL/(2beta)<.08748` and `KL/(6beta L^4)<.0000002`. Consequently

```math
 \bar P>.02006\quad(L\ge20),\qquad G_1>.10009.
```

For `l>=2`, the two exponential exponents are at least 13.8 and 9.2. The elementary series gives `e>8/3`, and `(8/3)^9>5000`; hence both factors `1-exp(-M)` exceed `.9998`. Thus the literal lower bounds `.010` and `.050` in J(c) survive, with strict margins. For the smallest allowed 4D tori, `10<=L<20`, the same proof with the boundary term `<.00764` gives `Pbar>.0162` and `E p_c>.008`; this still exceeds `1/1250`. The torus-limit conclusion follows either by these uniform bounds or by continuity of the finite-ring integrand.

The printed `KL(2)=.4020` also needs a genuine rounding correction. Retaining one more term, through k=6, and bounding the remaining geometric tails with ratios at most 1/72 (I1) and 1/80 (I2), gives

```math
 1.59063684<I_1(2)<1.59063686,\quad
 .68894844<I_2(2)<.68894845,\quad
 .4331274<r(2)<.4331275.
```

The same rational bounds imply `.227989<v<.22799`. The first four positive terms of the log series at the lower endpoint exceed `.46413`. At the upper endpoint, bound the remaining terms by `2v^9/(9(1-v^2))`; the resulting upper sum is below `.46414`. Hence `.40211<KL(2)<.40213`: its four-decimal rounding is `.4021`, not `.4020`. These are finite rational comparisons of the displayed sums and tails, not computed Bessel values. The coarser certificate above already leaves enough margin for J(c).

The optimized trials near 9.5 and 7.5 and the claimed `.07`/`.12` refinements are not certified by this check. They are unnecessary guide values. The rounded four-digit equalities and a script’s confirmation cannot substitute for the rational argument above. No numerical job was run.

**Consequence checked:** the stated H-swap, for its stated ownership and torus/local-limit states, fails at the window at every l. This is a refutation of that hypothesis, not of clustering or of all possible exchanges.

## Step 3 result — JI, topology, and TS3

### JI and data processing

Source: Claude Opus, row 1121, line 179. **The entropy identity HOLDS**, for a finite ring block and the positive bounded finite-range specification in row 1118. Write `X=omega_z`, `Y=omega_{z^c}`, `P=law(X,Y)`, and `Q=P_X tensor P_Y`. Let `p_y(x)` and `n(x)` denote the conditional and marginal densities relative to the block reference. With `H_z=sum_{c in N_z}F_c`, the DLR identity says `H_z(x,y)=-log p_y(x)+a(y)`. Both full and recombined pairs have the same Y marginals. Directly expanding the four terms gives

```math
 E\sum_{c\in N_z}\Delta_z(c)
 =2\{E_P\log p_Y(X)-E_Q\log p_Y(X)\}
 =2\{D(P\Vert Q)+D(Q\Vert P)\}.
```

The terms `log n(X)` cancel because P and Q have the same X marginal. This also proves that the stated I and L are exactly mutual information and reverse mutual information. Compactness and bounded local energies keep these finite for a fixed finite block, even in an infinite-volume state.

**The stated one-plaquette data-processing bound HOLDS**, for a ring-only plaquette whose intersection with z is a nonempty connected proper path as specified. Orient the two complementary paths from the same endpoint to the same endpoint, with holonomies A and B. Each marginal is Haar by a gauge transformation at one endpoint. Under Q they are independent. Thus `AB^{-1}` is Haar under Q and is the plaquette holonomy under P. Conditional Jensen for the density ratio proves

```math
 I\ge D(P_{A,B}\Vert H\otimes H)
   \ge D(P_{AB^{-1}}\Vert H)
   \ge \sup_{t\in\mathbb R}\{t\bar P-\log z(t)\}.
```

For the last inequality, tilt Haar by `exp(t tr(U)/2)/z(t)` and use nonnegativity of relative entropy to that tilt. This supplies a written proof of each processing step. It does not tensorize the one-plaquette bound over many plaquettes. The `.83` value at the guide value `Pbar=.6` is not needed or certified here.

**The extrapolation “no other localized ownership helps” FAILS as a deduction from JI.** First failing sentence: line 179, “So no partition makes the mean exchange cost small at the window,” if “small” means the H-swap threshold, and the stronger ownership-independent conclusion at line 184. JI bounds a sum of signed costs. H-swap bounds bounded nonlinear functions of individual costs, with geometry-dependent incidence and path constants. No uniform conversion with those constants is supplied. The author already calls the conversion for general partitions argued; the later categorical conclusion loses that qualification.

A hand counterexample to the *mean-to-small-probability inference*, not to Wilson SU(2), is useful. On two binary variables give unnormalized weights

```math
 w_{00}=1,\quad w_{11}=s,\quad w_{01}=w_{10}=s e^{-1/s},\qquad 0<s<1.
```

Exchange the first variable of two independent samples. A positive cost occurs only on the ordered pairs `(00,11)` and `(11,00)`. Its value is `2/s-log s`; their probability is `2s/Z^2`. Hence `E(1-exp(-Delta_+))<=2s`, while

```math
 E\Delta={2(s-s^2e^{-2/s})\over Z^2}(2/s-\log s)\longrightarrow4.
```

All weights are positive, and JI still holds. A lower bound on the mean alone therefore cannot establish the required failure threshold. Proposition J’s bounded far-edge construction avoids this problem and remains valid. A new ownership needs its own explicit bound on cost, incidence, and the applicable threshold. No Wilson counterexample to every possible alternative partition has been proved here or in JI.

### The degree remark

Source: row 1121 line 180. **HOLDS for the explicitly sitewise statement; HOLDS AFTER CORRECTION for its advertised consequence.** Orient `S^3 x S^3` by the product orientation. Pullback under the swap sends `vol_1 wedge vol_2` to `vol_2 wedge vol_1=(-1)^9 vol_1 wedge vol_2`, so its degree is -1; the identity has degree +1. Degree is invariant under homotopy. Maps uniformly closer than a convexity radius are homotopic by the unique short geodesics. Therefore a finite chain of single-site homeomorphisms joining these endpoint maps has a neighbouring pair separated by at least that radius somewhere.

**Corrected consequence:** this forbids a uniformly small interpolation within that particular family of site maps. It gives no lower bound on expected Wilson action, gluing free energy, or the measure of the configurations where the jump occurs. In particular, at zero coupling a topologically forced jump has zero energy. It also does not cover arbitrary maps coupling several sites, frame-dependent exchanges, or alternative observables. The last sentence, “no smoothed exchange avoids the junction cost at the window,” is not proved by this degree argument. The spin-wave energy estimate in that paragraph is not used or verified here.

### TS3(a,b)

Source: Claude Opus, `gap-resp-in-law-sheet-check-opus.md:554–564`, row 1120. **Both HOLDS**, with the ordinary convention that the bounded observables are real, or that complex tests are allowed on both sides. Let `Y=E(F|outside)-EF=m_Omega(F)-EF`; the finite-range DLR property gives the equality with the ring conditional mean. For every outside-measurable `|G|<=1`,

```math
 |\operatorname{Cov}(F,G)|=|E(YG)|\le E|Y|.
```

Take `G=sign Y` to attain equality (complex case: `G=overline Y/|Y|`, zero at Y=0, for the bilinear covariance convention). This proves (a), including that the maximizing test can be chosen on the finite ring. For an independent copy `X'=m_{Omega'}(F)` of `X=m_Omega(F)`, conditional Jensen and then the triangle inequality give

```math
 E|X-EX|\le E|X-X'|\le2E|X-EX|.
```

This proves (b). If real G alone were required for complex F, (a) would need correction; the stated real-observable application has no such issue.

**The universal wording in §5.3 needs correction.** Lines 582–586 do not follow for an arbitrary function Phi or with arbitrary interchange of supremum and expectation. The precise true statements are:

- For each fixed bounded real F, its two-sample absolute difference is within a factor two of `sup_{|G|<=1}|Cov(F,G)|`.
- The same holds after taking a supremum over a specified normalized class F *outside* the expectations.
- For an integral probability metric `d_Cl(P,Q)=sup_{F in Cl}|PF-QF|`, Jensen and the triangle inequality instead compare `E d_Cl(m_Omega,m_Omega')` with `E d_Cl(m_Omega,mbar)`, within a factor two. For full total variation this is the beta/absolute-regularity coefficient. It is not in general the one-observable covariance supremum.

For example, let Y consist of n independent fair signs, and, given Y, let X in `{1,...,2n}` have probabilities `(1+epsilon Y_i)/(2n)` and `(1-epsilon Y_i)/(2n)` on the ith pair. Here `0<epsilon<1`, so the law is strictly positive. The averaged TV from the uniform marginal is `epsilon/2`, whereas for every `|F|<=1`, orthogonality of the signs and Cauchy–Schwarz give `E|E(F|Y)-EF|<=epsilon/sqrt(n)`. No dimension-free factor two identifies these two coefficients. Likewise a squared difference gives a square-root conversion, not TS3’s factor two: `X=+/-h` has `E|X-EX|=h` but `E(X-X')^2=2h^2`.

Thus (H-two-N1) is exactly the claimed one-observable mixing condition up to factor two. Full-TV H-two is the stronger beta-mixing condition. Neither statement proves a consumer that upgrades one scale to exponential decay. The spin-wave and coexistence test assertions in §5.3 remain at their declared argued/belief grade; TS3 does not turn them into theorems or prove an exhaustive classification of all two-sample criteria.

## Step 4 result — AFF and PROD

### AFF: convexity and extremality

Source: Claude Fable, row 1122, lines 111–120. **The formal statement of Lemma AFF HOLDS.** Its interpretation as a requirement for an additional uniqueness hypothesis does not.

Here is the omitted tail argument in full. Suppose, for every pair of bounded local real functions, a state satisfies

```math
 |\operatorname{Cov}_\mu(F,G)|
 \le C\min(|\operatorname{supp}F|,|\operatorname{supp}G|)
       \|F\|_\infty\|G\|_\infty e^{-m d(\operatorname{supp}F,\operatorname{supp}G)},
 \qquad m>0.
```

Fix local F and a bounded random variable G measurable outside a box at distance D from its support. Conditional expectations onto increasing finite sets of those outside coordinates approximate G in L1 and preserve its sup norm. The displayed bound uses at most `|supp F|`, independently of the approximants’ growing supports. Passing to the limit gives the same bound for G. If G is tail measurable, this holds for every D. Hence `Cov(F,G)=0`. Approximate a tail indicator itself by local functions in L1; its variance is zero. Thus every tail event has probability zero or one.

For completeness, tail triviality implies extremality here without an unmentioned translation-invariance assumption. If `mu=t nu+(1-t)eta`, `0<t<1`, are Gibbs states of the same specification, then `h=dnu/dmu` exists and is bounded. Their common conditional kernel in every finite volume implies `h=E_mu(h|outside Lambda)` for every Lambda. For an increasing exhaustion, the reverse martingale limit makes h tail measurable. It is constant by tail triviality, and normalization gives `nu=mu`; likewise eta. Conversely, the midpoint of two distinct Gibbs states is a nontrivial convex decomposition, so is not extremal.

The constraints `mu(Phi_c)<=r` are affine, and their intersection is convex. If this set contains two different states it contains their non-extremal midpoint. It therefore cannot consist entirely of states with the stated uniform clustering bound. This proves every line of AFF’s formal statement.

**Corrected wording:** “An affine hypothesis sufficient for uniform clustering on all Gibbs states of a specification can admit at most one of those states.” It need not prove that the *specification* has only one state. Nor does AFF prove that the hypothesis cannot itself select or force an extremal state. It does not require a second, non-affine companion assumption. The inference at row 1122 line 148, that a one-sample hypothesis is never a consumer hypothesis by itself and must be supplemented by a uniqueness clause, **FAILS**. A convex sublevel set can be a singleton exposed extreme point. Even within regular specifications, the deterministic bounded observable `Phi_c=18 beta` and a fixed threshold below one encode the usual strong-coupling sufficient condition; it is formally a one-sample hypothesis. AFF says nothing against this. No contradiction to AFF’s narrower statement is involved.

For gauge theories, the application to all local observables is legitimate. Local gauge averaging determines a gauge-invariant Gibbs state. At separated supports the two averaging operations can be taken independently, so the covariance bound for the full local gauge-invariant algebra extends to arbitrary local tests. A bound on only one small subalgebra or a fixed list of observables would not suffice for this tail argument.

The finite-H coexistence example in line 120 remains **conditional on the existence of the two stated Gibbs states**. The covariance supply on its SU(2) factor is verified next. No unopened first-order-transition theorem for a specified finite H is promoted to a proved example here. Small Rbar in both phases of the connected-group weight w_p remains unproved.

### The pinned-cell covariance estimate: HOLDS

This fills the recalled covariance step using R. Dobrushin’s comparison argument, as rebuilt by Claude Fable in row 708, `gap-mid-max.md:282–296`. It applies to the actual weighted pinned cells of row 1011, not merely unpinned tori.

Fix `0<beta_1<1/18`, set `alpha=18 beta_1<1`, and fix any pins. All cell plaquette coefficients lie in `[0,beta_1]`. Changing one other free link changes a one-link log density by a function of oscillation at most `4 beta_1`; at most eighteen links share its plaquettes. To check the influence constant, interpolate the log density by `t h`. Its density derivative is `q_t(h-E_t h)`, and

```math
 {1\over2}E_t|h-E_t h|\le {1\over4}\operatorname{osc}(h)\le\beta_1.
```

Integration over `0<=t<=1` gives one-link TV influence at most beta_1. Pinning removes variables and cannot increase this bound. Thus every row sum is at most alpha, uniformly in cell size and pins.

The comparison estimate used here has a short constructive proof. For a function f, write `delta_i(f)` for its oscillation in coordinate i. A one-link heat bath removes the oscillation at its updated link and transfers at most `C(i,j)delta_i(f)` to j. Label transferred mass by the number of transfers. Total mass created at level n is at most `alpha^n sum_i delta_i(f)`, and it travels at most n plaquette-adjacency steps. Repeated full sweeps send the total remaining mass to zero. Comparing the telescoping heat-bath expectations under the original law and a law with changed kernels only on B, only mass reaching B contributes. Summing the geometric series gives

```math
 |\mu'(f)-\mu(f)|\le\Big(\sum_i\delta_i(f)\Big){\alpha^{d(\operatorname{supp}f,B)}\over1-\alpha}.
```

This is row 708’s comparison lemma, with its stated mass-accounting correction; it is reused, not counted as a new general comparison theorem. Conditional laws obtained by fixing B have the same kernels off B, so the estimate applies to them as well.

For a component f of `N_e`, `|f|<=6 beta_1`, it reads at most eighteen free links, and `sum_i delta_i(f)<=216 beta_1`. For a component g of `N_f`, `|g|<=6 beta_1`. When e and f lie on opposite faces of a cell of side l, their free-link supports have plaquette-adjacency distance at least `l-2`. Condition on the support of g and apply the comparison bound. For `l>=4`,

```math
 |\operatorname{Cov}(N_e^a,N_f^b)|
 \le A_\beta\alpha^{l-2},\qquad
 A_\beta={1296\beta_1^2\over1-\alpha}.
```

A face has `3l(l+1)^2<=12l^3` links. There are nine entries in K, so the actual row-1018 normalization obeys

```math
 R_c^2\le1296 A_\beta^2 l^8\alpha^{2(l-2)},\qquad
 \bar R(l)\le36 A_\beta l^4\alpha^{l-2}\longrightarrow0.
```

Every inequality is uniform in the pins. Polynomial times a geometric sequence tends to zero, for example by the ratio test on `l^4 alpha^l`. No run is used.

### PROD: factor dependence and the periodic seed

Source: row 1122 lines 123–132. **HOLDS AFTER CORRECTION**, for the full *periodic fixed-magnetic-sector transfer trace including all electric sectors*, and for `beta_2>(log 80)/2`, not the rounded endpoint “above 2.191.” It is a counterexample in the product-group class. It is not a counterexample inside Wilson SU(2).

**Rbar reads only SU(2): HOLDS.** For `G=SU(2) x H` with H finite and the explicitly product plaquette weight, pinned integration factorizes:

```math
 Z_c(\omega_1,\omega_2)=Z_{1,c}(\omega_1)Z_{2,c}(\omega_2),\qquad
 \mathfrak g=\mathfrak{su}(2)\oplus\{0\}.
```

Lie derivatives of `-log Z_c` therefore differentiate only the first factor. The pinned force and its covariance are those of SU(2), independent of the H pin. Thus the natural Lie-derivative extension of Rbar is exactly Rbar_1. This extension must be stated: a criterion defined only on connected simple SU(2) has not thereby been refuted. The preceding uniform pinned estimate proves Rbar tends to zero at beta_1 below 1/18 for this product.

**`1+S=(1+S_1)(1+S_2)`: HOLDS.** This is prior work, Claude Fable’s Lemma PT, `gap-crux-exercise3-max.md:690–713`, using row 708’s product device. Haar reference, magnetic multiplication, electric convolution, and gauge projection all factor. Hence on the product physical slice Hilbert space `T=T_1 tensor T_2`, with top eigenvalue `lambda_01 lambda_02`. Taking the trace of a positive integer power and dividing by that top eigenvalue to the same power gives the formula. Positivity yields `S>=S_i`. Factoring Z alone would not establish this normalization; the transfer factorization does. No projection onto a diagonal centre or deletion of electric sectors is allowed in this formula.

**The Z2 no-periodic-seed input is verified against its actual source.** It is not just the test-table label. Sources: Claude Opus, `gap-es1-opus.md:129–152` (cocycle identity and minimal area); Codex/Astra, `gap-z2parity-astra.md:384–442` (component bound); and Theorem SH’s existing recursion, Claude Fable, `gap-seed-shape.md:87–110`. The checked identity is

```math
 Z^k=\text{common factor}\sum_{D\in k+B^2}u^{|D|},\qquad u=e^{-2\beta_2}.
```

In the all-class surface ensemble, a component of nonzero class has at least `a^2` plaquettes, where a is the smallest torus side. A plaquette has at most twenty edge-neighbours. The plane-tree encoding gives at most `80^{n-1}` rooted connected sets of size n. Deleting a specified closed component is injective and removes exactly its energy. With N plaquettes and `b=80e^{-2beta_2}<1`, this yields the prior bound

```math
 \epsilon_a={N\over80}{b^{a^2}\over1-b},\qquad
 {Z^v\over Z^0}\le{\epsilon_a\over1-\epsilon_a}\longrightarrow0
```

on every fixed-aspect family. The odd electric fraction is `(1-Z^v/Z^0)/2`, and tends to 1/2. The positive transfer ground state is centre even. Therefore this fraction is at most `S(t;B)/(1+S(t;B))`. A periodic seed of Theorem S or SH at any size would, by that theorem’s existing recursion, give `S(j^k t;j^k B)->0`, a contradiction on that fixed-aspect family. This is the precise bridge from the Peierls result to “no seed at any size.” It reuses the seed engine as an input and does not claim a new proof of that engine.

The Z2 transfer assumptions are elementary here: the two character coefficients of `exp(beta_2 z)` are `cosh beta_2` and `sinh beta_2`, both positive. The electric kernel is positive, magnetic multiplication preserves operator positivity, and gauge projection restricts to the physical subspace. Its integral kernel is strictly positive, so the top eigenvalue is simple. Together with coordinate symmetry these meet the engine’s premises. The term “frozen” here means a finite coupling in this explicitly proved range, not an infinite-coupling delta measure.

It follows that for every positive threshold r_0 there are cells with `Rbar(l)<=r_0` in the product while the specified periodic seed fails at every size. This validates PROD’s product-class refutation. It says nothing by itself against the centre-even seed or an alternative trace summing magnetic sectors; the lane’s “full seed” terminology elsewhere refers to such a different object.

**The last inference in line 132 FAILS as a deduction.** The centre of SU(2) is not a disconnected factor of SU(2); there is a continuous path from I to -I. Derivatives of a function on connected SU(2) can encode differences between centre-related configurations. The direct-product blindness just proved cannot establish that no SU(2) response consumer can ever read flux, or that a separately assumed flux clause is mandatory. No such consumer is supplied here; its impossibility is not supplied either.

## Step 5 result — BACK, GM, TILT, the count, and J3

### BACK and its constants

Source: row 1122 lines 134–140. **HOLDS**, for the stated uniform exponential covariance bound, with the scale enlargement made explicit. A closed four-dimensional cube of integer side r has

```math
 4r\{(r+1)^3-(r-1)^3\}=24r^3+8r\le32r^3
```

boundary-face links. For a core at distance at least `r/3` from this ring, TS3(a) gives

```math
 \alpha_F\le32C r^3 e^{-cr/(3l)}\|F\|_\infty,
 \qquad
 E|m_\Omega(F)-m_{\Omega'}(F)|
 \le64C r^3 e^{-cr/(3l)}\|F\|_\infty.
```

The ring need not literally be the smaller support: `min(|supp F|,|ring|)<=|ring|` is enough. If the chosen discrete core has depth only `floor(r/3)`, replace the exponential by `exp(-c floor(r/3)/l)` or shrink the core by one layer. This is a geometry convention, not an unrecorded loss of rate.

For any desired `eta_0>0`, an explicit sufficient integer r is

```math
 r\ge\max\left(7,{3l\over c}
     \max\left[18,\ 2\log_+\!\left({1728C(l/c)^3\over\eta_0}\right)\right]\right),
 \qquad \log_+x=\max(0,\log x).
```

Indeed, with `t=cr/(3l)`, the coefficient is `1728C(l/c)^3 t^3 e^{-t}`. For `t>=18`, `t^3<=e^{t/2}`: it holds at 18 since `e^9>(8/3)^9>18^3`, and the logarithmic difference is increasing thereafter. The displayed choice bounds the coefficient by eta_0. For fixed C,c,eta_0 this is `O(l log l)` as `l>=2` grows. “Small” without a specified eta_0 is replaced by this statement.

If row 691’s literal bound (C') is the starting point, it includes `(2D+1)^4`. First absorb that polynomial by reducing the exponential rate and enlarging C, as row 691 itself does. BACK does not erase that polynomial while preserving the original rate and prefactor. No implication is claimed from merely pair-dependent clustering constants to a uniform bound over every core observable.

### GM

Source: row 1122 line 196. **HOLDS.** At a box site with precisely one coordinate at an endpoint, exactly one of its eight incident links is exterior-normal and seven belong to V. Left/right multiplication at this site acts transitively on the normal-link pin. It changes no other boundary pin. Gauge invariance of every plaquette and Haar measure sends the first conditional law exactly to the second. Pairing each configuration with its image changes at most seven internal links. Thus `k_z<=7`, for every coupling and every R, for this face-interior type of normal link. At edges/corners several normal pins meet the site, so the same one-pin argument is not applied there.

### TILT

Source: row 1122 line 198. **HOLDS AFTER CORRECTION.** A layer link belongs to exactly one plaquette meeting V, and that plaquette contains exactly one V link. A normal link has at most six relevant plaquettes, each containing one V link. Thus changing the pin multiplies the density by `exp(h(U_A))`, where `|A|=m<=6` and

```math
 |h|\le2m\beta,\quad \operatorname{osc}h\le4m\beta,
 \qquad {d\mu'\over d\mu}={e^h\over\mu(e^h)}.
```

**First incorrect phrase:** “a density ... with logarithm between -2 beta and 2 beta,” for a layer link, if it refers to the normalized Radon–Nikodym density. Those are bounds on the *unnormalized energy difference*. For the normalized density the valid absolute bound is `4 beta` (in general `4m beta`); its log oscillation is still at most `4m beta`. For example, tilting Haar by `exp(2 beta t(U))` gives log density `2 beta t(U)-log z(2 beta)`, which is less than `-2 beta` at `U=-I`. Normalization cannot simply be omitted.

The finite-marginal TV distance t satisfies the useful uniform bound `t<=tanh(m beta)<1`. To see the usual bounded-tilt estimate, let the unnormalized likelihood w lie in `[a,b]` and let `c=Ew`. The chord bound on `|w-c|` gives

```math
 \operatorname{TV}\le{(b-c)(c-a)\over c(b-a)}
 \le{\sqrt b-\sqrt a\over\sqrt b+\sqrt a}
 =\tanh\!\left({\log(b/a)\over4}\right).
```

Use `log(b/a)<=4m beta`. This applies directly to the A marginals since h depends only on A.

The coupling step also holds with a precise definition of I. Let

```math
 I_*:=\sup_{a,a'} W_{\rm Ham}
       \bigl(\mu(\,\cdot\mid U_A=a),\mu(\,\cdot\mid U_A=a')\bigr)
```

for the remaining V\A variables, at the fixed other boundary pins. The conditional law of those remaining variables is the same under mu and mu' when A is fixed. Maximally couple the A marginals. On equality use the identical conditional sample; on inequality couple the remaining conditionals with expected Hamming cost at most I_* (or first I_*+epsilon and pass to the infimum). The resulting bound is

```math
 k_z\le t(m+I_*).
```

Equivalently I can be the average conditional coupling cost under the *residual mismatch coupling*. An unqualified mean under the original law cannot replace either of these quantities. The trivial finite-box estimate `I_*<=|V|-m` proves finiteness only. A bound uniform in R and all wall pins remains the open content of INF-L.

### Boundary count and DS-W

Source: row 1122 lines 200–204. **HOLDS.** Fix a link direction i. There are `2(R+1)^3` normal boundary links and `6R(R+1)^2` layer links. Of the normal links, `2(R-1)^3` have an endpoint in a face interior and admit GM. The remaining normal count is `12R^2+4`. If K bounds every other one-pin Hamming cost uniformly over pins, then

```math
 \sum_{z\parallel i}k_z
 \le14(R-1)^3+K\{12R^2+4+6R(R+1)^2\}
 \le(R+1)^3\{14+6K(1+1/R)\}.
```

For the second inequality the difference in the K coefficients is exactly `30R+20+6/R>=0`; the non-K inequality is immediate. For `R>=6`, `6(1+1/R)<=7`. Dividing by `N_R=R(R+1)^3` proves

```math
 R\ge\max\{6,(14+7K)/\delta\}\quad\Longrightarrow\quad(DS\hbox{-}W)(R,\delta).
```

All counts are for the source’s V and boundary, not row 1011’s different cell-ring convention. R is an integer and the displayed lower bound is rounded upward when choosing it. The same sufficient condition works with K(R) when `14+7K(R)<=delta R`.

**Scope correction:** this is a sufficient reduction using the maximum of the residual costs. It is not an equivalence between DS-W and a uniform-in-R bound on K. DS-W controls a sum and can tolerate large exceptional k_z. Nothing in the count supplies K at the window, nor makes INF-L a strictly necessary first lemma.

### J3

Source: row 1122 line 214. **FAILS as stated beyond its last, proof-scheme-only warning.** First failing step: identifying the hybrids in row 691’s Lemma 1 with Proposition J’s independently sampled replicas. Lemma 1 takes two deterministic boundary configurations. In Lemma 3 those configurations come from an *arbitrary coupling*, not the product law. Gauge invariance of each marginal does not make the coupling invariant under independent gauge changes. Independent Haar relative frames cannot be inserted while preserving that coupling or its low disagreement cost.

A counterexample to the asserted universal Haar-random seam is immediate within Wilson SU(2). Draw U from its torus law and set `V=g.U` for a fixed local gauge transformation g close to the identity. Both marginals have the required law. A partial swap changes a plaquette trace continuously by an arbitrarily small amount, so its mean stays positive by Step 2’s Pbar bound. It is not Haar. More strongly, take gauge transformations at many disjoint, well-separated stars and order the changed links star by star. At every intermediate stage consisting of completed stars, the hybrid is another gauge transform of U and has exactly the original law, density one. There can be arbitrarily many mixed-replica plaquettes and changed links. The joint coupling carries the correlations that cancel their apparent seam costs.

The further claim of no density bound uniform in seam size has not been proved for the actual hybrid laws used in row 691. Even for independent replicas, JI gives a sum of forward and reverse relative entropies. Its one-plaquette forward data-processing bound is not a lower bound on reverse relative entropy per plaquette, and cannot be added over plaquettes without additional structure. A claimed relative-entropy density estimate would require its own quantified law and proof.

**Corrected J3:** “Row 691’s deterministic telescoping proof needs a one-pin coupling bound at every intermediate hybrid boundary. An estimate averaged over the original Gibbs boundary law does not, by itself, provide bounds under the hybrid laws generated by that proof. An in-law replacement must control those laws or change the construction. Proposition J proves an additional obstruction for the specific independent-replica swaps to which it applies.” This is a genuine missing input in that proof scheme. It is not a refutation of all in-law cube criteria or of all possible coupled interpolations.

## Step 6 result — the L3 verdict and its exact scope

**Row 1122’s sentence HOLDS AFTER CORRECTION as a bounded inventory and a necessary-content statement. It FAILS as a general exclusion of response consumers, or as a reason to call L3 closed.** Calling an argument “argued” permits an unchecked argument; it does not repair its invalid inferences. The decisive failures are the extension of AFF to a mandatory extra uniqueness clause, the transfer of PROD from a disconnected product to SU(2)’s centre, the ownership-independent use of JI, and the independent-replica assumption in J3. The technical corrections to the trial estimate, TILT, and the Z2 threshold do not overturn the valid narrow results.

A precise replacement is:

> In the named rows checked here, no consumer has been supplied from small Rbar or from (H-two-N1)/(H-two-col) to the requested uniform exponential clustering or periodic seed. The specified H-swap consumer is valid but its hypothesis fails at the window for its stated ownership. A one-sample affine criterion valid for every Gibbs state cannot admit two distinct Gibbs states if it is to imply the uniform clustering bound. The Lie-response Rbar criterion fails for the stated product-group periodic seed. The specified two-sample absolute-difference/TV criteria contain one-scale mixing of their tested classes. DS-W has a sufficient uniform-boundary consumer but its window hypothesis is unproved. None of these statements excludes a Wilson-SU(2)-specific Rbar consumer or every possible averaged criterion.

There is also a simple logical statement, independent of the three-part taxonomy. Let `M(r,eta)` denote the uniform one-observable core–ring covariance bound for all bounded singlet F and bounded outside G. If a hypothesis H gives the uniform clustering bound with specified constants C,c,l, BACK proves `H => M(r,eta)` at the explicitly enlarged scale r of Step 5. Therefore H cannot be *strictly weaker in logical implication* than that particular enlarged-scale necessary consequence. This is not a comparison of difficulty of proof. It is not an equivalence, and it does not show that a proof of H must assume M as a separate input. At the original scale l, or with uncontrolled state-dependent constants, the asserted comparison is not established.

The exact boundaries of this conclusion are:

1. **State class.** AFF concerns all Gibbs states of one fixed specification and a fixed bounded function Phi_c. Its contradiction needs two states satisfying the same constraints. It does not apply to a nonconvex selection of periodic limit states without showing that its midpoint is admitted. Nor does it cover a quantity whose defining function itself changes nonlinearly with the state.
2. **Observable class and uniformity.** Tail triviality and BACK need bounds uniform over all bounded local tests with the stated support dependence. Pair-by-pair clustering of a total family is weaker. TS3 gives the exact coefficient only for its specified tests and order of supremum/expectation. Charged-only or fixed-local-neutral tests do not become full singlet mixing by renaming them.
3. **Group and action.** PROD concerns the direct product with an independent finite group, product weights, and a response defined by Lie derivatives. It does not refute a theorem restricted to the connected simple group SU(2) and its Wilson weight. The required small-Rbar statement in both phases of w_p has not been proved. Describing it as a belief is accurate; using it to close the connected-group case is not.
4. **Scale and cutoff.** The estimates here are at a fixed lattice coupling. The enlarged scale in BACK depends on the actual constants. A fixed-coupling periodic seed and the physical-cutoff-uniform wall (W) are different assertions. No carry along the Sussman–Alpoge trajectory is provided.
5. **Hypothesis families.** The checked identities cover the displayed affine constraints, the displayed two-sample metrics, and the stated sufficient supremum criterion. They do not classify all scalar criteria, nonlinear functionals, weights with bad-set terms, multi-time path sums, or coupled interpolation schemes. “Supremum” by itself does not imply mixing; only a proved sufficient condition does. Strictness of a sufficient boundary condition relative to a gap in one Wilson state is not proved merely because no converse is known.

The earlier lane check is consistent with these limits. I verified `gap-glue-check-astra.md:273–279` (Codex/Astra, row 896): FIB and MC do not rule out averaged scalar estimates, weighted estimates with a bad-set term, or exterior-independent tests. I also verified `gap-annealed-check-astra.md:65–88,173–181` (Codex/Astra, row 852, checking Claude Opus): literal AN1 is worst-case conditional control, but the surviving-path-sum replacement is already a sufficient alternative, with no model-specific supplier. These are prior results, not re-proved here. The three newer kinds do not turn that earlier non-exhaustive record into an impossibility theorem.

The practical conclusion is narrower than row 1122’s stop recommendation. The present H-swap at the window is excluded. Small Rbar alone cannot be a product-class periodic-seed criterion. The fixed-group Rbar consumer, a consumer for H-two-N1/H-two-col, and law-stable coupled alternatives remain open. This check supplies no new supplier for them and gives no evidence that they are easy. It also supplies no theorem that a proof of FL/DEC would have no possible downstream use.

### Final statement table

| Requested item | Verdict and retained content |
|---|---|
| J(a), J(b); gauge randomization; concavity | **HOLDS**, for the stated independent replicas, ownership and symmetric state class. |
| 8.3 convexity, tree gauge, product trial | **HOLDS**; the resulting finite-volume Pbar display **HOLDS AFTER CORRECTION** by retaining `-KL/(6 beta L^4)`. |
| Bessel values and `.010`/`.050` conclusions | **HOLDS AFTER CORRECTION** to the rational-series certificate in Step 2. Optimized guide refinements are not certified. |
| JI and the one-plaquette data-processing bound | **HOLDS**; its universal ownership exclusion **FAILS** as a deduction. |
| Degree remark | **HOLDS** for sitewise maps; its cost/exchange exclusion **HOLDS AFTER CORRECTION** to the limited topological conclusion. |
| TS3(a,b) | **HOLDS**; the unrestricted “any two-sample form, factor two” reading **FAILS**. |
| AFF, including uniform clustering implies extremality | **HOLDS**; the mandatory separate uniqueness-clause inference **FAILS**. |
| PROD, Rbar factor dependence, pinned-cell covariance, product thermal trace | **HOLDS AFTER CORRECTION** to the exact Z2 range and periodic trace scope. The connected-SU(2) inference **FAILS**. |
| BACK and constants | **HOLDS**, with the explicit enlarged scale and geometric convention in Step 5. |
| GM | **HOLDS**, `k_z<=7` for face-interior normal links. |
| TILT | **HOLDS AFTER CORRECTION** of normalized density bounds and the law/supremum defining I. |
| Count giving DS-W | **HOLDS** as a sufficient condition, `R>=max(6,(14+7K)/delta)`, not as an equivalence. |
| J3 | **FAILS** as a universal independent-frame/density claim; the proof-scheme warning holds in the corrected form. |
| Row 1122’s overall sentence | **HOLDS AFTER CORRECTION** to the bounded inventory and enlarged-scale necessary consequence above; no general L3 closure. |

This is a check of the repository’s new research text. It is not a correction of a claimed Sussman–Alpoge theorem. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban for the account’s RG ancestry. The source lemmas checked here remain credited to Claude Fable 5.2 and Claude Opus 5.5; prior Codex/Astra arguments and their named literature sources are identified at their use sites. No second provider has checked the corrections written in this file. They are written mathematical arguments, not formal Lean proofs or status grants.

Only `library/gap-l3-closure-check-astra.md` was edited. No numerical job or computer-assisted proof step was run. No source, registry, FINISH row, audit record, commit, push or external post was changed. The report remains uncommitted in the pinned checkout, as requested.

RESULT: HOLDS AFTER CORRECTION for the scoped lemmas and bounded inventory; J(a,b), TS3, formal AFF, BACK, GM and the DS-W count hold, PROD holds for the specified product and exact Z2 range, while the universal ownership, mandatory uniqueness/flux-clause, and J3 hybrid-law exclusions fail as deductions; L3 for Wilson SU(2) remains OPEN, no mass gap is claimed, and no scientific or audit status is granted.
