lead: anthropic/claude-opus-5-5/max f78d8dd2-4b44-46b6-8315-b3f424cabfcd
lease_until: driver sets this

**This line is not independent of the Sussman-Alpoge repository.** It reads the public account
https://github.com/ethanwsussman/Yang--Mills-LLM-experiment at commit `c854ad8b3a42` (Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of the text; unvetted by its own statement). Anything taken
from it is credited to it. Balaban's organization is credited to Balaban. Nothing from the account is
load-bearing here until it is proved in this file or in `library/`.

## State of attack

**Current formulation.** The hard core is the account's one induction on the level (Text 1). I verify load-bearing
steps one at a time and treat the rest as open.

**First verified step: the Gaussian part of the coupling flow, (P1).** It is the only source of asymptotic freedom in
the account, it is missing from the account's index of unproved statements, and the citations given for it cannot
contain it (Text 2.1). It is exact mathematics at the trivial background, so it can be proved or refuted outright.
Text 3 proves it, by an exact decomposition at constant flux (Prop 3.6) in which every massless piece is explicit, given one remaining leaf,
`Leaf Scalar`. The value a = 11/(3 pi^2) per unit of log(1/eta) at SU(2) is derived there and agrees with c_0 = (11 N^2/12 pi^2) log L.

**Order of constants.** L first, then the block sizes, then gamma: as in the account. (P1) reads L and nothing later.

**Second formulation, now the main line (Text 5).** One function, F_k := -log rho_k, the exact density of a block kernel on all real level-k fields, with constant thresholds T_c < T_f. Three statements at each level. (I_k): on D_k, F_k = x_k A_k + vac_k + R_k with R_k bounded in derivative norms free of x_k. (Loc_k): the same locally, away from cells above T_f. (RP'_k), replacing the earlier (P_k): at every field, F_k at fixed far data is compared with F_k at a class reference, with coefficient x_k on a classical functional 𝔹 that carries the entropy of rough cells at all levels (`library/relative-density-bound.md`, Prop 8). Thresholds: T_c = a_*/L^2, T_f^2 = L^{1/3} T_c^2/(C_r^2 K-bar). One step is one uniformly log-concave integral (exact tree gauge, compact cut on free variables, no extension) plus a positive gas of rare sites, with exteriors made of whole boxes once d_x >= 3 L. No R, no histories, no live regions, no complex tube. Deliverable: UV-LOC-R (Requests), which the upper chain's real fallback consumes.

**Hardest remaining inequality.** *(CI), the classical inequality at fixed far data, and its one-level transfer in (RP'_k).* For V' in D_{k+1}, W_far class on the d_x neighbourhood of I, V_I labelled with core C and hull of cubes and dropped boxes: 𝔸_k(W_far, V_I) - 𝔸_k(W_far, V^0) >= (c_b/4) T_c^2 |C|, and across one level inf_{fibre} 𝔸_{k-1}(xi'', W) minus its value at V^0 passes to the same at level k, up to a tail. Everything in rarity now rests on this, with Lemma 6 as its proof at the linear level. Unproved: the non-abelian reading. The route is item (k') there: a regular exterior field and a relative Landau gauge from `Lattice Uhlenbeck` (leaf), cubic term by L^4 of F_D from (R3), absorption by T_f L^{4/3} and C_3(L) T_f. A pointwise bound on U_D is not available: by a scaling count it fails by a logarithm at nested block centres. The entropy of rough children no longer needs a rough-parent statement: Lemma T (the number of rough cells over all levels is at most 8 ||F||^2/T'^2, by the dyadic maximal function) pays it once, in one infimum over chains, with no degradation in k. For (P1): only the high-mode write-up of `Leaf Scalar`.

**Routes tried and why they failed.**
- Direct bound of each composite diagram for Gamma_k: fails. Individual diagrams with the second jet of the k-fold average
  are of order k before gauge cancellation (Text 3.4). Hence the organisation by constant flux.
- Sum of squared weights as a growth rate for the block variance: fails as a danger signal. Sigma^2(L) > 1 for odd L >= 23
  looked like a loss of coercivity at large L; it is not, because the contour part is a coarse gradient (Text 3.2). Recorded
  so nobody repeats it.
- Holonomy bound of the account as the target: dropped. On my trace it is not consumed by clauses (0) or (i) (Text 2.2).

- Pointwise (R4) at U_D, from a Green kernel bound: fails by a logarithm at nested block centres, by a scaling count. L^4 suffices.
- Immediate conditional odds given the exterior of a hole only: not uniformly small, because an exterior at threshold forces the interior up. This is the true content of Balaban's waiting. Conditioning on the parent field on the whole shadow removes it (Text 5).
- Dobrushin uniqueness on status cells: fails at adjacency, since a wild cell can make its neighbour's non-class state as likely as its class state. Connected polymers with an absolute Peierls bound replace it.

- Dropping every box that contains a bad cell: forces an infinite ladder of thresholds (`library/critical-class-and-excess.md`).

- Polymer decay by Kirkwood-Salsburg: its kernel needs mixed differences of all orders, which first-difference bounds do not give; replaced by Dobrushin-Foellmer single-site updates, which need first differences only (`library/polymer-covariance.md`, with four other failed routes).
- Tall towers by exterior comparison with live data and position-dependent weights (Mix): superseded by (P_k), which never displays a tower. Dropping plaquettes at level 0 instead loses a fine surface energy of order (s_k/eta)^3. Pointwise ratios against a filled field do not recurse. Full log in Text 5.3.
- Path derivatives of all orders in the Laplace lemma: break under a compact cut, so version 2 uses first variation only and splits cumulants at the largest spanning-tree edge.

- Dense dyadic cubes for the exterior Poincare inequality: fail. Maximal dense cubes in a non-dense Q satisfy only sum l_a^3 < l^3, so their volume fraction is at most 1/2, and a separating sheet of filled cubes is still allowed. Non-density does not give connectivity; a threshold theta l^{3-b} helps only by 2^-b.
- Pruning sets of small boundary: derived, and it gives ||f - med||_2 <= (C/h) |E|^{1/4} ||grad f||_2, but only for a scalar. At a free boundary the Hessian in tree gauge has curl energy alone on the plaquettes kept, ||dB||^2 + ||d*B||^2 = ||grad B||^2 gains boundary terms, and a non-zero H^1 of the exterior gives exact zero modes. So scalar Poincare plus "the proof of Theorem 5" does not give coercivity there (finding F1). With site data fixed and v extended by zero the whole-lattice identity holds, so (A2), the oscillation bound and Theorem OS are not affected. (P_k) step 3 and `Z_Ext` in Prop R1 are.
- Relative bound by a supremum over outer data with no exterior analysis (`library/relative-density-bound.md`, Prop 3): fails as written (finding H1). Rough xi adjacent to I leaves (Loc) unavailable. Even for class xi the plaquettes across the edge of I cost x T_f^2 per plaquette; the denominator keeps them, and the numerator's bound drops them, so bounding the two integrals separately leaves more than the cost. The interface must be cancelled by comparing the two integrals.
- Applying (RP'_{k-1}) to the whole child region J: a one-line recursion, but the entropy multiplies by L^4 per level, up to the fine count. Used on rough clusters only.
- Paying a cluster's entropy with a fraction of x 𝔸 at each level: the coefficient degrades as (1-epsilon)^k. A forced/unforced split needs (CI) at a rough parent, which has no regularity. Replaced by Lemma T and the functional 𝔹.
- Bounding cube or 3-chain as the inner fill of a large cluster: the volume outruns the cost. A tube of constant radius R_0 = (pi/T_f)^{1/2} spreads the holonomy, which also corrects the earlier claim that no small-flux filling need exist for a large hole. It relies on thresholds being constants.
- Region theorem and local densities for (P_k): a local density of R_k needs an additive decomposition of a function known only through tree-decay derivatives on a class with no global path, and an extension by a flat field fails around a core with non-trivial holonomy. A recursive free-boundary density has a surface excess growing as L^3 per level. An infimum over the hole loses the cost at atypical collars. So exterior weights were dropped: (RP'_k) in `library/relative-density-bound.md` compares F_k at fixed far field, with the fields next to the hole inside I, so no exterior function is needed.
- Kernel of Prop R1 (finding F2): it claimed no shift of the exterior constraint because lines through core cells are excluded, but lines through non-core hull cells still enter the constraint. Fix: the kernel excludes all lines through the hull, which C determines; a parent with under half of its lines left gets a Haar value. Then step 5, second case of (P_k), reads: excluded fraction at least 1/2 forces |C| of order L^2 in that box, at cost at least c x T_c^2 L^2 >= c_P x T_f^2, because T_f^2 is of order L T_c^2 after the cube rule. Not yet carried into Text 5.2, 5.3.

- Extension with a constant free of L and sharp cube shapes, by separated or dense dyadic families: failed and not needed. Merging at a distance proportional to the larger side doubles the side per cell. Merging proportional to the smaller side leaves dense arrays that break the corkscrew. Maximal dense dyadic cubes satisfy a 2-dimensional packing with constant 1, which still allows a 2-cycle of cubes. Way out: T_f^2 = L^delta T_c^2 with delta = 1/3. A box with L^delta core cells is dropped at a profit, the rest have cubes of side at most L^delta, and any polynomial extension constant fits, with delta shrunk to suit (`library/relative-density-bound.md`, Lemmas 5, 6).
- Weighted action on the hull with a uniformly convex extension, no plaquette dropped (design): the gain is then at most ((1-kappa)^2/kappa) ||F*||^2_hull with no extension constant at all. It fails pointwise: on plaquettes crossing a membrane with non-central holonomy alpha the true angle is delta B_1 - Ad(e^{i alpha}) delta B_2, which can vanish where kappa |d B|^2 does not. So S_true >= S_kappa is false in the chart B. The case is real: thin centre-vortex-like sheets are 2-cycles of the core, with flat exterior.

**Newly proved or reduced this stretch.** Exact lattice curl-Poincare by axis-parallel paths averaged over the base point (Lemma 1, `library/curl-poincare-exterior.md`; numerics PASS, sup error at most 4e-14). The classical gain from criticality of U* in one line (Lemma 6). The denominator built on U* itself, so the relaxed exterior field is never extended into the hole, with the fluctuation's line mismatch spread over exterior lines (Prop 7). The chart's centre W_0 exists by convexity on K alone, and need not be class on a single cell. All at the linear level, not reviewed.

**Next action.** `Lattice Uhlenbeck`, then the patching in step 4 of (k'); the flux bound at rough fields behind Lemma T; the general trial on a tube X; (RP'_k) with the adaptive region in full, and J against the kernel. Then the Hessian on a ball, the written Theorem OS, `Local coupling`, `Assembly`, CT4. `Leaf Scalar` stays frozen with its consumer.

**Numerics this session.** Moyal check PASS after a test bug was found and fixed; B_2 - B_1 = 0.4263 against c_0 = 0.4081 at L = 3, pre-registered tolerance 25 percent (Text 3.8).

**Derived versus believed, this stretch.** Proved outright, unreviewed: Lemma 1 of `library/curl-poincare-exterior.md` (abelian, numerics PASS), Lemma T for the linear average, Lemma 3 of `library/polymer-covariance.md`. Derived at the linear level: Lemmas 5, 6, (CI). Sketches: (RP'_k), its adaptive region, the functional 𝔹, Theorem OS as written, locality against far data. Described, not constructed in detail: the tube fill, non-abelian (CI). Believed only: that no kill hides in the kernel's exclusion of lines against the event structure of J; and the d = 2 O(N) warning of Text 5.7 stands unresolved.

**Hostile check of the newest step, recorded.** Text 3.8 for (P1), Text 5.7 for the real route; for (RP'_k), the two hostile passes in `library/relative-density-bound.md`, items (a)-(l). Newest step, proved for the linear average: Lemma T. Not derived in detail: the tube fill for a general cluster. Believed, not derived: the flux bound at rough fields, and that 𝔹 = 𝔸 on the class.

## Obligations

- gap: Leaf Scalar, high-mode expansion of the scalar remainder with a spectral cut (frozen, Text 3.7) -> Theorem P1
- implication: Theorem P1 given Leaf Scalar -> flow bounds, clause (0)
- implication: Regularity, existence, uniqueness in a ball, L^2 curvature bound, decay of the response, from the one-shot trial field and Theorem 6 by a fixed point, items (R1), (R2), Text 5.3 -> Theorems 5-7 at U_k(W), Geometric package
- implication: (R3), flux_c(M^k(U_{k+1}(V'))) <= C_r L^-1 flux(V'), from an L^4 bound by the Fourier identity and lattice Sobolev, Text 5.3 -> thresholds, Prop R1, (P_k), convexity of the fibre
- gap: the trial field (R1) in lattice detail, smooth at the box scale -> Regularity
- implication: (RP'_k) and (A1) from it, Prop 8 of `library/relative-density-bound.md`, given (CI), (Loc_{k-1}), flow bounds; sketch of the induction with an adaptive region -> rare cells. Supersedes Prop R1, Prop 3 (withdrawn) and Prop 7 (kept as record) for rarity
- gap: (CI) beyond the linear reading, the hardest remaining inequality; 𝔸_k with Haar parents -> (RP'_k), (A1)
- gap: flux bound at rough fields for log-averages with excluded lines -> Lemma T at the level of the actual kernel
- gap: Lattice Uhlenbeck, frozen leaf: below a small energy per cell there is a gauge with ||A||_{H^1(c)} <= C ||F||_{L^2(c^+)}, uniform in eta -> (CI), (R2)
- gap: general trial on a tube X of radius R_0 around a rough cluster -> inner fill in (RP'_k)
- discharged: Lemma T, tower count by the dyadic maximal function, for the linear block average, `library/relative-density-bound.md` (own proof, not reviewed) -> accounting functional 𝔹
- implication: Lemma 6 (classical gain from criticality of U*), Lemma 5 (extension with constant (1+l)^4), cube rule with T_f^2 = L^{1/3} T_c^2 / (C_r^2 K-bar), `library/relative-density-bound.md`, abelian -> (CI)
- implication: exterior coercivity by adapted tree, Corollaries 3, 4 of `library/curl-poincare-exterior.md`, abelian -> not consumed on the Prop 8 route; kept in case a free-boundary integral returns
- gap: non-abelian reading of the curl-Poincare identity in Lemma 5, by absorption at flux below T_c -> (CI)
- discharged: exact lattice curl-Poincare identity, Lemma 1 of `library/curl-poincare-exterior.md`, abelian (own proof, numerics PASS, not reviewed) -> Lemma 5, Corollary 3
- gap: Geometric package: hypotheses (H1)-(H3) of `library/convex-laplace-tree-decay.md` in the coordinates of Text 5.1, with constants free of x_k (orders derived there; Hessian lower bound from Thms 5, 7 of the energy package) -> real one-step theorem
- gap: one-step theorem on regions with free boundary, and local densities of R_k on partial fields -> (P_k), which the Prop 8 route no longer consumes
- implication: (Loc_k) and (I_k) are one statement, Theorem OS, written in Text 5.3 against the current labels, given (H1)-(H3) with sites, (A1) from (RP'_{k-1}), the polymer lemma, the Laplace lemma, Dobrushin comparison -> real one-step theorem, (RP'_k)
- discharged: two-specification comparison, Lemma 3 of `library/polymer-covariance.md` (own proof after Dobrushin, not reviewed) -> locality in Theorem OS
- implication: locality against far data, from that lemma, conditioning outside B(y, 3r/4), and the propagator; sketch -> Theorem OS, Taylor Lemma 3
- implication: (H1)-(H3) with sites, from (Loc_k) and Theorems 5, 7 on a ball by IMS localisation, Text 5.3 -> Theorem OS
- gap: Hessian on a ball in tree-gauge coordinates, with the block average as a bounded term and C(L) once -> (H1)-(H3)
- implication: (P_k) from (P_{k-1}) given (Loc_{k-1}), Prop R1 at level k-1, the one-step theorem on regions, Block energy; base k = 0 proved; Text 5.3 -> Prop R1; superseded by (RP'_k) if Prop 8 holds
- implication: Prop R1 given (P_k), Cut and Poincare, Block energy, Regularity on regions, the Laplace lemma; Text 5.2; has a known error, corrected in place, and superseded by Prop 8 -> rare cells
- implication: rare cells: decay of all derivatives of the gas, given (A1) = Prop R1, (A2), and the oscillation bound; Text 5.4, `library/polymer-covariance.md` -> real one-step theorem, (P3)
- implication: Taylor: bounded low orders from the order-5 norm and contracting divided data, `library/gauge-taylor-contraction.md`, given (Loc) and the symbol bounds of D^j V*; vanishing orders proved there, contraction at n = 2 derived at the trivial background -> real one-step theorem, (P2)
- gap: symbol bounds of the non-linear lift D^j V*, j >= 2, and of the one-step form h uniformly in k -> Taylor
- gap: real one-step theorem: (I_k), (Loc_k), (P_k) imply the same at k+1, with contraction on order >= 5 and on the coefficients -> UV-LOC-R
- gap: local coupling version: F_k(V; w) with real position-dependent w and derivatives in w -> UV-LOC-R
- gap: assembly: last coarse integral, cumulants in L^n of the coarse measure, UV-LOC-R and CT4 -> upper chain
- discharged: covariance of a rare polymer gas from first differences, `library/polymer-covariance.md` Lemmas 1, 2 (own proof after Dobrushin and Foellmer, not reviewed) -> rare cells
- discharged: tree decay of all derivatives of a uniformly log-concave integral with a compact cut independent of the parameter, free of the volume, `library/convex-laplace-tree-decay.md` version 2 (own proof, not reviewed; the shifted cut near a site in Text 5.3 is an extension still to be written) -> real one-step theorem, replaces the walk expansion and M-freeness
- discharged: coercivity, saddle isomorphism, M-free decay at R(a) on the single-level determining set, and the Lagrange term off shell with no factor of the level, `library/block-poincare-energy-package.md` Thms 5, 6, 7 (own proofs, not reviewed; Thm 7 assumes the minimiser exists) -> Geometric package
- discharged: contour part of the bond average is a coarse gradient, Lemma 3.1 -> Core
- discharged: telescoping of the Gaussian part through the composite integral, Lemma 3.2 -> Theorem P1
- discharged: constant flux reads the coefficient, Lemma 3.4 -> Theorem P1
- discharged: value of the coefficient a from the second-order Moyal formula, Prop 3.7 -> Theorem P1
- discharged: flux expansion of the composite block symbol with uniform bounds, Lemma 3.9 -> Prop 3.11
- discharged: level-k Hessian symbol in constant flux, uniform in k and t, Prop 3.11 -> Prop 3.13
- discharged: fine vector end and the constrained part, Props 3.12, 3.13 -> Theorem P1
- discharged: lattice area moments and the scalar bracket, Lemma 3.14, Prop 3.15 -> Theorem P1

## Requests

- FROM TARGET LEAD, gate on UV-CT (`git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/gates/uv-ct-upper-chain-41489e4876.md`; same-model): CT3 carries all the separated content, since in the Gaussian family only CT3 fails. E is not free: Jensen forces E close to log G in L^1. CT4 is equivalent to p_P - p_infinity <= c_F (a/a_*)^4 and, by a mode count not yet checked, fails at Gaussian order by log log(1/a) unless two-loop running of the zero-mode factor rescues it. So treat CT4 as non-Gaussian. CT1 at complex sources is the least tested clause.
- FROM TARGET LEAD, 2026-10-30: the interface is now UV-CT; see `git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/GOAL.md` and `git show origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/parts/upper-chain.md`, Requests and Text section 7. Your UV-EXT' passed the upper chain's decisive question, and Lemma 7.2 reduces the source bound to one fixed torus. Your deliverables are CT1-CT3 on that torus and CT4, which the upper chain has not checked against your clause (i-b).
- UV-EXT, target lead and upper chain: drop the non-vanishing of Z(beta + s) in a disc uniform in volume, and state the
  bound with a local counterterm and position-dependent sources. Reasons in Text 4. Proposed wording there. (Answered by UV-CT.)
- UV-CT, target lead and upper chain: this line now aims at the real form with bilinear factor of `parts/upper-chain.md` Text 7, stated on every torus directly, here called UV-LOC-R: for real w in the class W and real test sources sigma_1, ..., sigma_n with supports of measure at most v and mutual distance at least delta, |d_{sigma_1} ... d_{sigma_n} log Z_L(w)| <= K_n(v, delta) prod_i ||sigma_i||_T, n >= 2, uniformly in a, L and positions. Reason: the RG on real fields has no complex tube, and its bounds are on derivatives anyway (Text 5). Please confirm that this closes Theorems 8 and 9 for the linear field with no chessboard and no CT4; your Text 7 says the bilinear factor recovers the linear field, and I rely on that sentence. CT1 at complex w is not attempted on this route.
- CT4, answer to the gate's D2 (derived from the structure, not yet proved, since it rests on Text 5): the mode count +(3/2) log beta reads the zero-mode factor at the bare coupling. In the RG both tori carry the same vacuum numbers vac_j through level K', up to tails e^{-mu P/a_j}, and the last coarse integral reads x_{K'}, which is fixed on the trajectory at a physical scale below a_*. So the factor is (3/2) log x_{K'} per coarse cell, a constant. If Text 5 closes, CT4 is a corollary with c_F of order C log x_{K'}; no two-loop rescue enters beyond the flow itself.

## Text

### 1. The map, in my own words

Source files: `theorem_0_complete_account_raw_{I,II,III}.tex` (the "book", about 424,000 lines) and
`ym4_manuscript_zeroth_draft.pdf` (the summary, 153 pages). Chapter 4 of the book (raw I, line 3531 to the end) is clauses
(0) and (i). Chapter 11 is the assembly; chapter 12 (labelled ch:13) is the index of everything not proved.

**The account's own verdict.** "No clause of Theorem 0 is proved outright." Clauses (0) and (i) are "proved as an
implication" from counted statements and a longer list of uncounted ones. It lists 3 + 19 sentences of Balaban used as printed,
14 chapter-4 statements with proof outstanding, and 23 chapter-4 statements with proof incomplete.

**The induction (one induction on the level k, carrying the coupling and the density together).**
Given g_0, ..., g_k in (0, gamma] and the representation of rho_j for j <= k:
1. Fluctuation integral of step k+1 at coupling g_k gives the whole-lattice effective action E^(k+1), a sum of local
   gauge-invariant terms E(X), analytic on a complex neighbourhood of regular configurations on X, bounded by
   E_0 e^{-kappa d(X)}, with d(X) the tree length of X in units of the block side M.
2. Read beta_{k+1} on Z^4, as the second-variation coefficient at the trivial background of the complete regular part, read
   through the linearised map from block fields to minimal configurations. It splits as beta^0 (Gaussian normaliser) + (rest of
   the unmarked part) + beta^R (marked, descending from large-field remainders). It depends only on g_0, ..., g_k. No torus, no K.
3. x_{k+1} = x_k - beta_{k+1}. Flow bounds lambda(j-i) - c_5 <= x_i - x_j <= B(j-i) from (P1) |sum_{l<=k} beta^0_l - k c_0| <= c_2
   with c_0 = (11 N^2/12 pi^2) log L, (P2) |beta^A - beta^0| <= C_rem eps_1 and |beta^A| <= C_beta, (P3) |beta^R| <= C' g^{kappa_0-7}.
4. Then the cube size of the step and the thresholds of the decompositions of unity are fixed, and T and R of step k+1 are performed.
The trajectory is first passage: K = min{k : x_k <= g^-2 + B}. Containment g_k <= gamma is then automatic.

**The density.** rho_k dV_k = sum over histories of T_k(h)[chi_{k,h} exp A_{k,h}(g_k^-2, U_k(V_k))] dV_k, with
A_k = -A(g_k^-2(.), U_k) + E_k + R_k + B_k - E_k^const. E_k: regular localised terms. R_k: terms made by the large-field operation,
bounded by g_j^{kappa_0} e^{-kappa d_j(X)}. B_k: boundary terms by large-field regions.

**Large fields.** Thresholds eps_k = g_k p_0(g_k), p_0(g) = A_0 (log g^-2)^{p_0}. Cubes of side M R_k, R_k the least power of L above
(log g_k^-2)^r. A large-field region of level j costs e^{-p_0(g_j)} per cube of side M R_j; the logarithmic charge is O(1) log g_j^-2 per
unit cube, at most O(1) M^4 R_j^5 per big cube; choosing regions costs exp O(1)(M R_j)^-4 |Z_j|. So p_0 must beat 1 + 4r.

The fundamental difficulty in d = 4, and the reason for R: the density of level-j large cubes per level-k cube is about
L^{4(k-j)} e^{-p_0(g_j)}. With g_j^-2 ~ c_0 (K - j) the suppression is only sub-exponential in the depth, so fine large-field regions
are everywhere at physical scale and must be renormalised away. R acts on a connected component once it fits in a cube of side
100 M R_k and has waited R_k steps: it integrates out the block field inside the component, replaces it by a normalised reference
law, and expands the result in local terms bounded by O(1) c_1 e^{-(1 + beta/2) kappa d_{j,Z}(X)}, c_1 in {e^{-p_0(g_j)}, alpha^{1/3}}.
A first-class component is re-filed into the small-field format (healed). A second-class component stays live, with gauge-fixing delta
functions kept. The account adds a waiting depth, a two-threshold split at the creating step, and a device it calls arrest: a
preparation of R stopped by a new large collar field, whose terms stay frozen.

**Where UV stability enters.** (a) Containment only, in the one-step theorem. (b) Irrelevance: after extraction of the marginal part,
terms read at level k carry (L^j eta)^{4+alpha}, so the per-volume sum over levels is geometric. (c) Large fields as above.
(d) Vacuum energy: -E_k^const = l_k - r_k, with l_k = (3/2)(N^2-1)(L^4-1) sum_{j>=k} log g_j^-2 |T^(j+1)| >= 0 and |r_k| <= C |T^(k)|.
Output, clause (i-b): chi_k e^{-g_k^-2 A(U_k) - E_- N_k} dV_k <= rho_k dV_k and integral rho_k dV_k <= e^{E_+ N_k}, E_- free of g_k,
E_+ <= C(1 + log g_k^-2). The pointwise upper bound Balaban prints, [122b (0.1)], is false as printed on histories with a live
second-class component, because those carry delta functions (draft Prop 2.5; a one-line proof which I have checked).

**Sources (clause (iii-c), chapter 5).** With a constant shift zeta of g_0^-2, zeta_{k+1} = zeta_k + b_{k+1}(zeta) - b_{k+1}(0) stays
within |zeta|/3 of zeta and sum Lip b_{k+1} <= 2/3. So s of order one, as `GOAL.md` guessed.

**Statements the account marks as unproved, chapter 4.** Proof outstanding: re-blocking outside admissible boxes; uniqueness and
locality of the constrained minimiser; cube gauge condition for small pairs and real backgrounds; positivity dichotomy of the
large-field operations; volume counts in the relative small-field machine; two data bounds and a kernel-difference bound displayed as
hypotheses of that machine; geometry and counting of live large-field regions; three statements on kept terms; Combes-Thomas decay of
the block covariance; conversion of per-rate bounds to the stage norm; holonomy bound for walks across several cubes.
Stated with proof incomplete: Lemma 4.2:lem-unmarked; re-blocking inside admissible boxes; real-factor slot bounds; stage totals of kept
terms; field dependence of densities in cube gauges; oscillation of a Gaussian piece; dissolution of the arrested region; the T-step
layer; weights and heredity; cube families under a stage move; current thresholds; the one-point current probe; no index-zero margin;
ambient-domain inclusion; the arrest theorem; newborn terms; later steps on live arrested pieces; current radius at raw points;
index-zero members under maps; core-freezing; no point on both boundaries of a stratum; the cell-counting bound. Chapter 5: companion
kernel at local data (M-freeness).

**Sentences of Balaban used as printed** (draft 9.1; book ch. 13 head 3): [122b (1.11), (1.23)-(1.48)] chain bounds and
|I(U_0)| < O(1) log M |Lambda|; [122b p.375] old terms beside a new region are analytic on the new class, "it is simple to see";
[122b p.376] the resummed boundary term "satisfies the same bound with a different constant"; [122b p.379, p.390] locality of terms
produced by R; [122b p.360] an estimate with details omitted; [122a p.191] integrations interrupted by a new region; [122a pp.177-179]
admissibility of prepared data; [119 p.275] on the difference of consecutive small-field regions the next configuration is of the earlier
type; [119 pp.276-277] the analysis of [109 sections 3-5] and [116] carries over to the cover by cubes of the layers; [109 (1.17)] at
complex configurations; [109 p.279], [109 (3.26)], one sentence each of [98], [99a or 99b]: "in the same way"; [99b (3.35), (3.37)] at the
two lowest tower levels on a large-field region; [102b (190)] from an uncomputed (189).

### 2. Findings from reading the map as a stranger's draft

**2.1. The one-loop law is unlisted and unproved.** (P1) is the only source of asymptotic freedom in the account. The book's Lemma
4.2:lem-one-loop gives an "Outline" of part (b): the telescoping identity and the two comparison bounds |B_k - B^ref_k| <= C_cmp/2 and
|B^ref_k - (11 C_g/24 pi^2) log(1/eta)| <= C_det are "used as stated in [109, Theorem 3] and [116, (2.41)]". Neither can contain them:
[109 Thm 3] is conditional on containment and its author defers the flow, Theorem 2 there, to a paper "based on perturbative
calculations" that was not published (`literature/NOTES.md` section 9.4 on branch `claude/ym4d-proof-draft`). The lemma is absent from
the index of chapter 13, though a later sentence calls its proof "incomplete at one step", and the draft calls (P1) "proved in the
companion account". Consequence: not fatal for containment along a chosen trajectory, since x_0 = gamma^-2 + B K gives x_k >= gamma^-2
with no sign information; fatal for K finite at fixed g, hence for constants uniform in a. The soft-kernel program has the same wall under
the name (UIR^natural) in `FLOW55.md`.

**2.2. The holonomy bound is flagged by the account as possibly false, and on my trace it is not consumed by clauses (0) or (i).**
Prop 4.24:prop-holonomy-bound asks that the holonomy of the G-valued factor around a walk loop be close to the centre, for all pairs of the
class. Its own remarks say this cannot follow from per-cube data, that a flat pair with non-central holonomy around an annular hull
meets every per-cube clause, and that in that case only a fixed tail "small in M/M_1 but not small in gamma" remains.

Flux count (mine): on a shell of index m the plaquette bound is about M alpha_{0,m} (eta/s_m)^2, with s_m = L^{m-k}. A transversal spanning
disc crosses a shell in area about (R_m M s_m)^2, so each level contributes about M^3 R_m^2 alpha_{0,m}, and the flux through a nest of
levels from m' to j is at most about sum_m M^3 R_m^2 g_m (log g_m^-2)^{q}. Along the flow this grows like the square root of the age in the
deep ultraviolet, so it is not bounded by any fixed negative power of log g_k^-2 once the age is large. I have not exhibited a pair of the
class realising it, so I do not claim falsity.

Consumers. The clause is the second line of (4.24:eq-normalisation-constants-6). Its consumers are: the proof of Lemma
4.26:lem-stage-expansion, the display 3c_G + vartheta + 1/2 <= C_0^sharp; clause (F2) of the stage bound in Theorem
4.24:thm-survivor-block-expansion; Lemma 4.24:prf-elimination-factors(c); Lemma 4.24:prf-holomorphy-locality. In each, the size of C_G
enters through ||C_G|| <= 3 c_G, which already covers the field part at every pair of the class, and the member vartheta is the bound on
Delta W, and that bound (eq-expansion-leaves-5) does not use holonomy. The appearance of vartheta in ||C_I|| <= K_S'(N_0+8) C_0 vartheta is a
Cauchy ratio, not this clause. Hence the **edit**: delete the field-dependence clause of C_G from the stage theorem and the holonomy bound from
the inputs of (0) and (i). Standing: a reading of the consumers, not a theorem. Not checked for clause (v), which is outside the hard core.

### 3. Verification of (P1): the Gaussian part of the flow

Credit: the fluctuation structure is Balaban's. The per-step reduction of the coefficient, the regrouping Gamma = G_perp + G_gh and the
coarse-orbit average are in `FLOW55.md` for the soft kernel; I redo what I use for the hard constraint. All statements below are for SU(2), the
target. Fine lattice eta Z^4, eta = L^-k, in level-k units. tr 1 = 1, t_a = sigma_a, tr t_a t_b = delta_ab, A(U) = sum_p (1 - Re tr U(dp)).

**Definition.** beta^0_l is the coefficient of Definition 2.6 of the draft, on the functional F_{l-1} = log Z^(l-1) - log Z^(l-1)(1) read
through U_l(e^{iB}). B_k := sum_{l<=k} beta^0_l. Sign: the marginal part of F is + beta^0 A, so 1/g_{l}^2 = 1/g_{l-1}^2 - beta^0_l - ...

**Theorem P1 (target).** There is C(L) with |B_k - k c_0| <= C(L) for all k, with c_0 = a log L, a = 11/(3 pi^2).

#### 3.1 The block operator

Let Q be the linearisation at U = 1 of one step of Balaban's average [109 (0.4)]:
Q theta(c) = avg_{x in B(y)} [ avg_Gamma theta(Gamma_{y,x}) + theta([x,x']) - avg_Gamma' theta(Gamma'_{y',x'}) ], c = (y, y' = y + L e_mu).

**Lemma 3.1 (the contour part is a coarse gradient).** Put Phi(y) := avg_{x in B(y)} avg_Gamma theta(Gamma_{y,x}), a functional of theta and of the
block centre alone, and Q_path theta(c) := avg_{x in B(y)} theta([x,x']). Then Q theta(c) = Q_path theta(c) + Phi(y) - Phi(y'). So the curl of
Q theta over any coarse plaquette equals that of Q_path theta. On plane waves in component mu, Q_path acts diagonally with symbol
D_L(q_mu)^2 prod_{nu != mu} D_L(q_nu) / L^4, up to the phase of the bond midpoint, D_L(q) = sin(Lq/2)/sin(q/2).

*Proof.* The first identity is the definition read with x' = x + L e_mu, since B(y') = B(y) + L e_mu: the contour average at y' over x' in B(y') is
Phi(y'). The curl of a gradient vanishes. The symbol: theta([x,x']) sums L bonds along mu, which is D_L(q_mu); the average over x in the block is
the product of D_L(q_nu)/L over all four nu. Exact identity; `checks/hard-core--mapped_contour_gradient.py` verifies all three claims to 1e-15. QED

Composition. Since Q D_1 = D_2 r (D_j the lattice gradient at level j, r restriction to block centres), Q_path D_1 = D_2 (r - Phi D_1) is a gradient, so
the k-fold composite has the same property, and the path parts compose. D_L(q) D_L(L q) = D_{L^2}(q) makes the composite symbol explicit:
in level-k units, with ell = L^k, S_ell(q) := sin(q/2)/(ell sin(q/(2 ell))),

    tau_0,mu(q) = S_ell(q_mu)^2 prod_{nu != mu} S_ell(q_nu),   |S_ell(q)| <= min(1, pi/|q|) on the fine zone |q| <= pi ell.

So the transverse block operator at the trivial background is a plain diagonal smoothing. This is what makes everything below explicit.

*Note on a false alarm.* The exact one-step weight norm Sigma^2(L) = sum_b w_b^2 of the full Q (`checks/hard-core--mapped_sigma2.py`) is 0.98 at L = 21 and
1.06 at L = 23, about L/24 for large L. In d = 4 a norm above 1 would mean a line-like kernel with infinite Riesz 2-energy in the composite limit, hence loss of
coercivity. Lemma 3.1 removes this: the line-like part is a coarse gradient and the effective action is coarsely gauge invariant. No upper bound on L arises here.

#### 3.2 Telescoping through the composite integral

**Lemma 3.2 (composition of one-loop terms).** Fix k and a small regular V_k. Let I_g(V_k) := integral dU delta(M^k(U) V_k^-1) e^{-A(U)/g^2}. Then as g -> 0,
log I_g(V_k) = -A(U_k(V_k))/g^2 + c(g) + Gamma_k(V_k) + o(1), with c(g) free of V_k, and Gamma_k(V_k) - Gamma_k(1) = sum_{l<k} F_l(U_k(V_k)).

*Proof.* The Gaussian Laplace method on a compact manifold: I_g has this form with Gamma_k the logarithm of the explicit prefactor at the unique minimal orbit (uniqueness: Balaban
102b Theorem 1, an input of the whole program; for what follows only its validity near V = 1 is used). I_g is also the k-fold iterate of one-step integrals, because the block averages
compose and delta functions compose on Haar measure. Apply the Laplace method step by step: the one-step prefactor at level l is Z^(l) at the saddle, and the saddle at level l for prescribed
V_{l+1} is M^l(U_{l+1}(V_{l+1})), and U_l(M^l U_k) = U_k because a minimiser under a coarser constraint is a minimiser under the finer one. Asymptotics of one function are unique. The
exponential gauge-fixing of [109 (0.14)-(0.16)] is an insertion of 1 with a constant normalisation, and so changes nothing dependent on U. QED

Standing: this identifies Balaban's Z^(l) with the Laplace prefactor of a step, which holds if [109 (1.4)] is the exact linearisation. If a U-dependent factor at order g^0 were carried in E^(l+1) in his text, I take the prefactor as
my definition of beta^0 and that factor moves to (P2). No later step changes.

#### 3.3 Constant flux reads the coefficient, on shell

Let U_F = exp(i A sigma_3) with A a real bond field with constant curl: flux phi = f eta^2 per fine plaquette in the 12-plane, in level-k units a flux density f. Charged components feel theta := 2 f.

**Lemma 3.3 (on shell).** U_F is a critical point of A, so J = 0. M^k(U_F) = V_F is the level-k constant flux f. U_F = U_k(V_F). The Lagrange multiplier vanishes, and the
Hessian of A on the constraint manifold is the plain Hessian H_f of A at U_F. Also H_f D_f = 0, where D_f is the covariant gradient, and Q_f D_f = D_{k,f} r, where Q_f is the linearisation of M^k at U_F.

*Proof.* The gradient of A at U_F in the neutral direction is sum_p sin(phi_p) d(H^3)_p, a total derivative for constant phi_p; charged components do not appear at first order. So J = 0. M of an abelian configuration is abelian, and linear in the phases.
Its value has constant curl by covariance under the coarse translations and by Stokes for the averages of loops. A critical point meeting the constraint is the minimal configuration by uniqueness. H_f D_f = -[J, .] = 0 is the Ward identity of A. Q_f D_f = D_{k,f} r is the
linearisation of M^k(U^g) = g M^k(U) g^-1. QED

**Lemma 3.4 (constant flux reads beta).** Let Gamma = sum_X E(X) be gauge invariant, lattice symmetric, with E(X) analytic at U = 1 and exponentially decaying. Then the second f-derivative at f = 0 of Gamma(U_F) per level-k cell is beta[Gamma], the coefficient (2.7), times
the second f-derivative of A(U_F) per cell, namely 1.

*Proof.* The second variation of E(X) in a slowly varying potential depends at leading order only on the curl, by gauge invariance of each E(X) and evenness: E''(X)[B,B] = F(x_X) M^X F(x_X) + O(|F| |dF|). The sum of M^X over X through a point, per cell, is a single hypercubic tensor. A plane wave of small
momentum and the constant field read the same tensor, and the plane wave reads beta by (2.7) and the form of Pi-hat. QED

This is why no statement at finite flux is needed: only the Taylor coefficient at f = 0 enters, and there is no Nielsen-Olesen mode at that order.

#### 3.4 Why not plane waves

Off shell, the Lagrange multiplier lambda_1 ~ p^2 B enters through <lambda, D^2 M^k>. A naive size count gives order k per diagram, from the commutators of the k-fold average at every intermediate level, and only gauge covariance reduces it. On constant flux lambda = 0 and the covariance is carried by the twisted convolution
below, so this problem does not arise.

#### 3.5 The exact decomposition

Write Q_f = Q^o_f + D_{k,f} Phi_f, with Phi_f removing what is a gradient. For all small f, with G_f := Q^o_f K_f^-1 (Q^o_f)^T on level-k bonds, K_f := H_f + D_f D_f^* and H^o_f := G_f^-1:

**Prop 3.6.** Up to constants free of f,

    Gamma_k(f) = C_k(f) + [ log det' D_f^* D_f - log det' D_{k,f}^* D_{k,f} ] - (1/2) log det r_{k,f},
    C_k(f)  := log integral dH delta(Q^o_f H) e^{-(1/2) <H, K_f H>} = -(1/2) log det K_f - (1/2) log det G_f,
    r_{k,f} := (D_{k,f}^* D_{k,f})^-1 D_{k,f}^* H^o_f D_{k,f} (D_{k,f}^* D_{k,f})^-1.

C_k is a fully constrained Gaussian integral: it is gapped, and it is a per-cell analytic function of (f, t^2) when K_f is replaced by K_f + t^2, uniformly near (0,0), by composition of gapped one-step Gaussian integrals.

*Proof.* By Lemma 3.2, Gamma_k is the Laplace prefactor of I_g. I_g is invariant under the coarse gauge group, so average V over that group exactly (this device is `FLOW55.md` Theorem K-bar, used here at the hard constraint). The averaged kernel is invariant under all fine gauge transformations. Near the orbit of U_F:
the coarse orbit integral is integral d omega_k delta(Q H - D_k omega_k), which after the shift omega_k -> omega_k + Phi_f(H) is integral d omega_k delta(Q^o H - D_k omega_k). In the fine orbit coordinates H = H_T + D omega the measure carries det'(D^* D)^{1/2}, and the integrand depends on H_T alone by Lemma 3.3. Now on shell K_f = H_f + D D^* preserves the range of D, and acts on it as D^* D,
so a Gaussian integration in Feynman form over H with the constraint equals the integration over H_T times det'(D^*D)^{-1/2}; hence the prefactor is log det'(D^*D) + log integral dH integral d omega_k delta(Q^o H - D_k omega_k) e^{-(1/2)<H,K H>}. The inner H integral is Gaussian with a linear constraint and gives -(1/2) log det K - (1/2) log det G - (1/2)<D_k omega_k, H^o D_k omega_k>.
The omega_k integral gives -(1/2) log det(D_k^* H^o D_k). Factor D_k^* H^o D_k = (D_k^* D_k) r (D_k^* D_k). QED

At low momentum H^o_f is the level-k Feynman operator up to irrelevant terms, and D_k^* K_{k,f} D_k = (D_k^* D_k)^2 exactly on shell, so r_{k,f} = 1 + irrelevant: this is the content of `Scalar` below. All massless pieces of Gamma_k are thereby isolated in one explicit bracket.

#### 3.6 The value of the coefficient

**Twisted products.** Operators covariant under magnetic translations have kernels T(x,y) = e^{i (theta/2) x ^ y} tau(x-y), x ^ y = x_1 y_2 - x_2 y_1. Their symbols compose by the Moyal product. To second order, X * Y = X Y + (i theta/2){X,Y} - (theta^2/8) P[X,Y], with {X,Y} = d_1 X d_2 Y - d_2 X d_1 Y and P[X,Y] = d_1^2 X d_2^2 Y - 2 d_1 d_2 X d_1 d_2 Y + d_2^2 X d_1^2 Y.

**Lemma 3.5 (second order of log det; scalar symbol).** If T = T_0 + theta T_1 + theta^2 T_2 is a positive scalar symbol, the theta^2 coefficient of the per-site log det is
integral dp [ T_2/T_0 - T_1^2/(2 T_0^2) + P[T_0,T_0]/(16 T_0^2) - Ptilde[T_0]/(12 T_0^3) ], with Ptilde[T] = (d_1 T)^2 d_2^2 T - 2 d_1 T d_2 T d_1 d_2 T + (d_2 T)^2 d_1^2 T, and dp = d^4p/(2 pi)^4.

*Proof.* log det T = -integral_0^infty ds [Tr (T+s)^-1 - Tr (1+s)^-1]. With A = T_0 + s, expand the star resolvent R = A^-1 + theta R_1 + theta^2 R_2 from R * (A + theta T_1 + theta^2 T_2) = 1. Order theta: R_1 = -A^-2 T_1, since {A^-1, A} = 0. Order theta^2: the Poisson terms cancel, as {R_1, A} + {A^-1, T_1} = -A^-2{T_1,A} + A^-2{T_1,A} = 0 up to the sign bookkeeping, and
R_2 = A^-3 T_1^2 - A^-2 T_2 + (1/8) A^-1 P[A^-1, A]. Using d d A^-1 = -A^-2 d d A + 2 A^-3 d A d A gives (1/8) A^-1 P[A^-1,A] = -(1/8) A^-3 P[A,A] + (1/4) A^-4 Ptilde[A]. Integrate in s: integral A^-2 = 1/T_0, A^-3 = 1/(2 T_0^2), A^-4 = 1/(3 T_0^3). QED
Test: T_0 = p^2 + t^2 gives integral dp [1/(2 T_0^2) - (2/3) p_perp^2/T_0^3] -> (1/48 pi^2) log(Lambda/t), which matches the Mehler heat kernel (theta tau/sinh(theta tau)) per volume, namely the term +theta^2/(96 pi^2) log(Lambda^2/t^2). Checked by hand.

**Prop 3.7 (the coefficient).** With tau-regulated massless pieces, the theta^2 coefficient per complex charged component, at low momentum:
log det(-D^2 + t^2): (1/48 pi^2) log(Lambda/t). log det(-D^2 delta - 2F + t^2) on 4 components: 4/(48 pi^2) log(Lambda/t) - (1/2)(2^2 + 2^2)/(8 pi^2) log(Lambda/t) = -(5/12 pi^2) log(Lambda/t), the second term being -T_1^2/(2 T_0^2) with T_1 of eigenvalues +-2, 0, 0.
Real Gaussian integration over a complex charged field gives det_c^-1, and the ghost power is 2 per complex component: the functional -(1/2) log det K + log det D^*D of the real fields is - log det_c K_c + 2 log det_c(-D^2), so its coefficient is (5/12 pi^2 + 1/24 pi^2) theta^2 log = (11/24 pi^2) theta^2 log(Lambda/t).
With theta = 2 f this is (11/6 pi^2) f^2 log. Since A(U_F) per cell is 1 - cos f = f^2/2 + ..., the coefficient of A is a log(Lambda/t) with **a = 11/(3 pi^2)**, and 11 N^2/(12 pi^2) at N = 2 is the same number. QED

The split agrees with the known 10 : 1 between gluon and ghost.

#### 3.7 The estimates

Notation. epsilon(p) := p^2 + t^2, t in [0,1]. s_j = L^{j-k}. All functions of q are on the fine zone |q_nu| <= pi/eta. theta = 2f. dq means d^4q/(2 pi)^4. Bond variables are taken at bond midpoints, with the half-bond transport absorbed, so that lattice reflections act simply.

**Lemma 3.8 (second order of log det, diagonal zeroth symbol).** Let h = h_0 + theta h_1 + theta^2 h_2 be a matrix symbol with h_0 diagonal and positive and h_1, h_2 Hermitian. The theta^2 coefficient per site of log det is

    c_2[h] = integral dp { sum_mu [ h_2,mumu/h_0,mu + D(h_0,mu) ] - (1/2) sum_{mu,nu} |h_1,munu|^2/(h_0,mu h_0,nu) },   D(T) := P[T,T]/(16 T^2) - Ptilde[T]/(12 T^3).

*Proof.* As in Lemma 3.5, with A = h_0 + s. Since all d^alpha h_0 are diagonal, {A^-1, A} = 0, so R_1 = -R_0 h_1 R_0. In the trace only the diagonal entries of the Poisson terms enter: ({R_1,A})_mumu = -A_mu^-2 {h_1,mumu, A_mu} and ({R_0,h_1})_mumu = +A_mu^-2 {h_1,mumu, A_mu}, which cancel exactly. The remaining terms integrate in s by integral ds (a+s)^-2 (b+s)^-1 + (a <-> b) = 1/(ab). QED

**Lemma 3.9 (Leaf-Q). (a) One step.** With phi_loop the flux of a loop, xi = 2 i phi, xibar its average, X_loop = sum_{b in loop} +- Ad_transport H_b, the charged linearisation of one step of M at U_F is
Q = ((e^xibar - 1)/xibar) avg[ (xi/(e^xi - 1)) X_loop ] + e^xibar X_c.
This is an exact computation, checked against a finite difference of the true M to 1e-12 (`checks/hard-core--mapped_onshell_flux.py`, C5). With Phi the covariant contour average, Q^o := Q - D Phi has symbol, in potentials, t_j(q) = rho(s_j q) + vartheta_j a(s_j q) + vartheta_j^2 b(s_j q) + ..., vartheta_j := theta s_{j+1}^2, where rho_mu(omega) = [D_L(omega_mu)/L]^2 prod_{nu != mu} D_L(omega_nu)/L, and a, b are trigonometric polynomials depending on L only, not on j or k. Reason: on the lattice of level j the step is the same, and loop areas in units of s_{j+1}^2 are bounded by a constant.

**(b) Composition.** Q^[j] D_j = D_{j+1} r_j gives Q^(k) = Q^{o,[k-1]} ... Q^{o,[0]} + D_k (a site operator), by induction: Q^[1] Q^[0] = Q^[1] (Q^{o,[0]} + D_1 Phi^[0]) = Q^{o,[1]} Q^{o,[0]} + D_2 (Phi^[1] Q^{o,[0]} + r Phi^[0]). So tau = t_{k-1} * ... * t_0 as a twisted product in q. This formula holds for sums over intermediate lattices, because the phase of the composition is e^{i(theta/2) u ^ v} with u, v the two steps.

**(c) Bounds.** Expanding to theta^2: tau_0 = prod_j rho(s_j q), which telescopes to the product of S_ell in 3.1. Each term of tau_i is a product over j of rho(s_j q) in which at most 2i factors are replaced by a, b or derivatives d^alpha rho(s_j q), and it carries the weight sum of products of s_{j+1}^2 and of s_j s_j'. Each such weight is at most s_{m}^2 s_{m'}^{2(i-1)} over the positions used, so the total over all positions of any fixed factor type is at most C(L). For n != 0, with q_n = p + 2 pi n,

    A_i := sup_p sum_{n != 0} |d^alpha tau_i(q_n)|^2 / |q_n|^2 <= C(L),  uniformly in k.

Proof. Fix a term whose highest replaced position is j and lowest j'. The upper product R_{>j}(q) = prod_{i>j} rho(s_i q) is bounded in each direction by E(q_nu) = |sin(q_nu/2)|/(ell' |sin(s q_nu/2)|), s = s_{j+1}, ell' = 1/s. The lower product R_{<j'}(q) is bounded in each direction by min(1, pi/(s_j' |q_nu|)). The per-direction sum over n_nu in Z of E(p_nu + 2 pi n_nu)^2 min(1, pi^2/(s_j' (p_nu + 2 pi n_nu))^2) splits by residue classes: for n_nu not divisible by ell', E <= C s/dist(s n_nu, Z), which is square summable with sum O(1); for n_nu = ell' m, the min factor is at most C(L)/m^2 when j' = j, and the middle factors supply the same when j' < j. So the 4-dimensional sum is bounded by C(L)^4, and 1/|q_n|^2 <= 1 for n != 0. Derivatives of E are bounded by C s/dist(s n_nu, Z) and by a bounded function on the classes n_nu = ell' m, and derivatives of lower factors bring s_j' only. By the triangle inequality in l^2 and the summable weights, A_i <= C(L). The fine zone only truncates the sum. QED

Also tau_i is smooth on the zone |p| <= pi with uniform C^4 bounds. tau_0,mu(p)^2 >= (2/pi)^10 there. tau_0,mu = 1 + O(p^2). The mixed term in tau_1 obeys tau_1(p) = tau_1(0) + O(p^2), since d rho is odd.

**Lemma 3.10 (fine symbol).** K_f + t^2 in level-k units has symbol K = |q|_eta^2 + t^2 + theta S_eta(q) + theta^2 T_eta(q), with |q|_eta^2 := sum (2/eta)^2 sin^2(eta q_nu/2) >= (4/pi^2) |q|^2 on the fine zone, S_eta(q) = S_0 + O(|eta q|^2), and S_eta, T_eta, with their derivatives in q, bounded uniformly. S_0 is the spin matrix: in the 12-plane its eigenvalues are +-2, the other two vanish.

*Proof.* Kernel of K_f from the plaquette form S_2 = (1/2) sum_i |w_i|^2 cos phi + sum_{i<j} Re(w_i conj(w_j) e^{i phi}), checked against the true action in C3, plus D D^*. Finite range and smooth in the flux per fine plaquette theta eta^2, and the factors of eta cancel on rescaling. The explicit phi term gives eigenvalues +-1 in units of theta and the commutator of the covariant differences in the curl form gives another +-1, so the total is +-2. M2 of `checks/hard-core--mapped_moyal.py` tests the bottom eigenvalue -theta of -D^2 - 2F. QED

**Prop 3.11 (Core).** Let G^t be the level-k symbol of Q^o (K + t^2)^-1 (Q^o)^*, and h := (G^t)^{*-1}. Uniformly in k and t in (0,1]:
(a) h_0,mu = 1/g_mu is diagonal, h_0,mu = epsilon + E_mu, with |E_mu| <= C epsilon^2, |d E_mu| <= C |p| epsilon + C epsilon^2, |d^2 E_mu| <= C epsilon on the zone |p| <= pi;
(b) h_1 = S_0 + O(epsilon); h_2 = O(1);
(c) c_2[h] = integral_{|p|<=pi} dp [ 4 D(epsilon) - 4/epsilon^2 ] + O(1) = -(5/12 pi^2) log(1/t) + O(1).

*Proof.* By Poisson summation the level-k symbol is G = sum_n (tau * kappa * tau^*)(p + 2 pi n), with kappa the star inverse of K. Write G = tau * kappa * tau^* (p) + Rbar(p), the sum over n != 0. kappa's expansion at q_n, n != 0, is bounded by C/|q_n|^2 with all needed derivatives, by Lemma 3.10. So Lemma 3.9 and Cauchy-Schwarz bound Rbar_i in C^2 uniformly, and Rbar_0 = O(p^2) with derivatives, since tau_0,mu(q_n) carries a factor p_nu for each n_nu not divisible by ell. Let Y be the star inverse of tau at n = 0, which exists to order theta^2 by Lemma 3.9. Then G = tau * (kappa + W) * tau^* with W := Y * Rbar * Y^*, so

    h = Y^* * K * (1 + W * K)^{*-1} * Y.

At order zero this reads h_0,mu = Y_0,mu^2 epsilon_eta / (1 + W_0,mu epsilon_eta), and W_0 >= 0, which proves (a) after replacing epsilon_eta by epsilon, a relative O(eta^2 p^2). At order one the terms are Y_0^2 S_eta, epsilon times bounded terms, and Poisson brackets, which are O(p^2) because d Y_0 = O(p) and d epsilon = O(p); so (b) for h_1. At order two all terms are bounded. Insert in Lemma 3.8: h_2/h_0 = O(1/epsilon); |h_1|^2/(h_0 h_0) = |S_0|^2/epsilon^2 + O(1/epsilon), with sum_{mu nu} |S_0,munu|^2 = 8; and by (a), P = 8 + O(epsilon), Ptilde = 8 p_perp^2 + O(p^2 epsilon), so D(h_0,mu) = D(epsilon) + O(1/epsilon). The integral of 1/epsilon over the zone is bounded. Finally 4 D(epsilon) - 4/epsilon^2 = -2/epsilon^2 - (8/3) p_perp^2/epsilon^3, with angular average -2/epsilon^2 - (4/3) p^2/epsilon^3, whose integral is -(10/3)(1/8 pi^2) log(1/t) + O(1). QED

**Prop 3.12 (fine vector end).** v_c(tau) := c_2[log det_c(K-hat_unit + tau^2)] per fine site obeys v_c(tau) = -(5/12 pi^2) log(1/tau) + O(1) as tau -> 0. In level-k units per cell the coefficient of theta^2 is v_c(eta t).
*Proof.* Lemma 3.8 with T_0 = Qhat^2 + tau^2 scalar: the integrand is tr T_eta/T_0 + 4 D(T_0) - (1/2) tr S_eta^2/T_0^2, and by Lemma 3.10 it differs from 4 D(epsilon_Q) - 4/epsilon_Q^2 by O(1/epsilon_Q). Scaling: the flux per fine plaquette is theta eta^2 and there are eta^-4 fine sites per cell. QED

**Prop 3.13 (the constrained part).** C_k(theta) has a Taylor coefficient at theta^2, and it equals (5/12 pi^2) log(1/eta) + O(1) uniformly in k.
*Proof.* For t > 0 all operators have exponentially decaying kernels and the second order is given by the formulas above: -log det_c(K + t^2) - log det_c G^t = -log det_c(K + t^2) + log det_c h^t has coefficient -v_c(eta t) + c_2[h^t], which is (5/12 pi^2) log(1/(eta t)) - (5/12 pi^2) log(1/t) + O(1), uniformly in t. The constrained Gaussian integral is analytic in (theta, t^2) at (0,0) at fixed k, because K_0 is gapped on ker Q^o_0. For H in that kernel and p fixed, tau_0(p) Hhat(p) = -sum_{n != 0} tau_0(q_n) Hhat(q_n), so by Cauchy-Schwarz and Lemma 3.9 |Hhat(p)|^2 <= C sum_{n != 0} |q_n|^2 |Hhat(q_n)|^2, whence ||H||^2 <= C <H, K_0 H>. A gapped Gaussian with finite-range data has a per-cell logarithm analytic in the parameters, and so the coefficient at t = 0 is the limit t -> 0. QED

**Lemma 3.14 (lattice area).** Let A be the signed area of the 12-projection of the continuous-time random-walk bridge of duration tau on Z^4, with generator the lattice Laplacian. With J_0 = e^{-2 tau} I_0(2 tau) and J_1 = e^{-2 tau} I_1(2 tau): E[A^2] = (tau^2/3) (J_1/J_0)^2, exactly, and E[A^4] <= C tau^4.
*Proof.* e^{-tau D_theta^* D_theta}(0,0) = J_0^4 E[cos theta A], since the symmetric-gauge phase along a closed walk is e^{i theta A}. The symbol computation of Lemma 3.5, by inverse Laplace transform in s, gives the theta^2 coefficient integral dQ e^{-tau T} [ -(tau^2/16) P + (tau^3/24) Ptilde ] with T = Qhat^2, which is -(tau^2/2) J_1^2 J_0^2 + (tau^2/3) J_1^2 J_0^2 = -(tau^2/6) J_1^2 J_0^2, using integral (dQ/2 pi) sin^2 Q e^{-2 tau (1 - cos Q)} = J_1/(2 tau). The fourth moment: split at tau/2. On [0, tau/2] the bridge has a density at most C with respect to the free walk, by the planar heat kernel, and on the other half use time reversal. For the free walk, A_t is a martingale, with E[A_t^4] <= C E[(integral_0^t |x|^2 ds)^2] + C E[sum (jumps)^4] <= C t^4 for t >= 1, by Burkholder. For t <= 1 the walk makes few jumps, and A vanishes unless it has at least 4 jumps, so the bound holds. QED

**Prop 3.15 (the scalar bracket).** u(th) := per-site [log det(D_th^* D_th) - log det(D_0^* D_0)] for the unit lattice with flux th obeys |u(th) - th^2 (1/96 pi^2) log(1/|th|)| <= C th^2. Hence the bracket of Prop 3.6, in complex normalisation 2 [eta^-4 u(eta^2 theta) - u(theta)], is theta^2 (1/24 pi^2) log(1/eta) + O(theta^2), with O(.) uniform in k.
*Proof.* u(th) = integral_0^infty (d tau/tau) J_0^4 E[1 - cos th A] >= 0. For tau <= 1/|th|: 1 - cos y = y^2/2 + O(y^4), and th^2 integral (d tau/tau)(tau^2/6) J_1^2 J_0^2 = th^2 [(1/96 pi^2) log(1/|th|) + O(1)], since tau^2 J_1^2 J_0^2 = (1/16 pi^2)(1 + O(1/tau)) for large tau and O(tau^4) for small; the error term is th^4 integral_0^{1/|th|} d tau tau^{-1} J_0^4 tau^4 <= C th^2. For tau > 1/|th|: |1 - cos| <= 2 and integral (d tau/tau) J_0^4 <= C th^2. QED

**Leaf Scalar (not yet proved in full).** With X = D_{k,theta}^* D_{k,theta}, Y_theta := X^-1 D_k^* E_theta D_k X^-1, E_theta := h_theta - K_{k,theta}, and r = 1 + Y: the per-cell quantity log det_c r_theta - log det_c r_0 is bounded by C theta^2, uniformly in k. Consumer: Theorem P1.
What I have toward it. Density count at second order: Y_0 = O(p^2), Y_1 = O(1), Y_2 = O(1/p^2), all homogeneous in the indicated sense, so the second-order density is O(1/p^2), integrable, with a bound uniform in k by Prop 3.11(a), (b). Low modes: the Landau gap X >= c |theta| from (D_1 +- i D_2)^*(D_1 +- i D_2) >= 0 gives theta^2 <= C X^2, the moment expansion of the exponentially local E_theta gives |<D psi, E_theta D psi>| <= C <psi, X^3 psi>, so ||Y on the spectral subspace X <= Lambda |theta| || <= C Lambda |theta|. The rank per cell of that subspace is at most e J_0(1/(Lambda theta))^4 <= C Lambda^2 theta^2 by the diamagnetic inequality. So low modes contribute O(theta^3). High modes: the star expansion in theta/X has remainder density O(theta^3/p^4), whose integral is O(theta^3 log). What is missing is a clean write-up of the high-mode expansion with a sharp spectral cut.

**Theorem P1 (standing: proved given Leaf Scalar).** |B_k - k c_0| <= C(L), c_0 = (11/(3 pi^2)) log L.
*Proof.* In complex normalisation, Prop 3.6 reads Gamma_c = C_k + 2[log det_c X_fine - log det_c X_coarse] - log det_c r. By Props 3.13, 3.15 and Leaf Scalar, Gamma_c(theta) - Gamma_c(0) = (5/12 pi^2 + 1/24 pi^2) theta^2 log(1/eta) + O(theta^2) = (11/24 pi^2) theta^2 log(1/eta) + O(theta^2), uniformly in k. With theta = 2 f: (11/6 pi^2) f^2 log(1/eta) + O(f^2). The neutral sector adds f^2/8 (1 + O(eta^4)) + o(f^2) per cell: there M is linear and H_f = d^* c d, with c = cos(phi) on 12-plaquettes and 1 on the others, so the first-order change of -(1/2) log det at the fine end is (phi^2/4) times the average of (|d_1|^2 + |d_2|^2)/|q|^2, which equals 1/2 per fine site, and at the coarse end it is O(eta^4). By Lemma 3.4, Gamma has a second derivative and it equals B_k times that of A(U_F) per cell, which is f^2/2 at leading order. So B_k = (11/(3 pi^2)) log(1/eta) + O(1), and log(1/eta) = k log L. QED

Consequences. beta^0_{l+1} = c_0 + c_l - c_{l+1} with sup |c_l| < infinity: this gives the flow input (P1) of the account, with a proof. Per-step sign needs convergence of c_l, which needs convergence of the level-l symbols, and is not asserted, matching what the account says.

#### 3.8 Hostile check

1. *Are the massless pieces real at f != 0?* K_f has the negative mode -|theta| in the charged sector, so Prop 3.6 is an identity between absolute values there, with the transverse constrained form positive (C7: minimum eigenvalue 1.18 at m = 1). C_k is analytic. Prop 3.15 is proved at f != 0 with no perturbation theory in f, so no order-of-limits issue remains there. In Prop 3.13 the limit t -> 0 is taken at fixed k through analyticity. OK.
2. *Is Lemma 3.4 circular with locality?* It needs Gamma_k local at fixed k, which holds because each one-step F_l is local at the trivial background (gapped covariance, Combes-Thomas). No uniformity in k. OK.
3. *Is Y in Prop 3.11 legitimate on the whole zone?* tau_0 is bounded below on |p| <= pi, so yes. The formal star expansions to order theta^2 are Taylor coefficients of true operators only when the operators are analytic in theta: for t > 0 G^t has exponential decay and is bounded below, so its inverse is analytic. OK.
4. *The sum over j in Lemma 3.9(c).* The weights are what make it finite, and a, b are polynomials with no dependence on j. If a loop area in Lemma 3.9(a) were not bounded in units of s_{j+1}^2 this would fail. It is bounded: contours stay in two blocks. OK.
5. *What is U-dependent and possibly lost in Lemma 3.2?* See the standing note after it. It is the one place where I rely on my reading of [109 (1.4)] rather than the text. If E^(l+1) at order g^0 carried a U-dependent piece in his text, then beta^0 as printed differs from mine and the difference moves into (P2). Nothing here changes, but (P2) must then be proved for my split.
6. *Weakest point.* Leaf Scalar. Also Lemma 3.10 is verified numerically in its first-order content and only sketched in its bookkeeping.
7. *A counter-test, run.* Direct numerics of B_1 and B_2 at L = 3 in d = 4 from Prop 3.6 at small flux (`checks/hard-core--mapped_beta_numeric.py`; self tests N0 and N1 pass). Pre-registered prediction: B_2 - B_1 within 25 percent of c_0 = 0.4081. Result: B_1 = 0.6651 (n_c = 5), 0.6644 (n_c = 7); B_2 = 1.0914 (n_c = 5); B_2 - B_1 = 0.4263, which is 4.5 percent above c_0. PASS. Finite-size shift of B_1 from n_c = 5 to 7 is 0.1 percent. L = 3 is small and the check reads two levels: it tests the coefficient, not the uniformity in k.
8. *Moyal check.* `checks/hard-core--mapped_moyal.py` first reported M4 FAIL (fitted 0.650, formula -0.015), with hermiticity defect 3.3e-3. The defect located a sign error in the test's magnetic boundary condition: T(x_1+N, x_2; y_1+N, y_2) = exp(-i theta N (x_2-y_2)) T(x;y) preserves psi(y_1+N n, y_2) = exp(-i theta N n y_2) psi(y). After the fix: M1 rel 8e-7; M2 ratio 1.019; M3 difference 4e-14; M4 fitted -0.01503307, formula -0.01503316, rel 6e-6, hermiticity 6e-18. PASS. The formula was not changed.

*What is derived.* Lemmas 3.1, 3.2, 3.3, 3.4 (with the locality input), 3.5, 3.8, 3.9, 3.14; Props 3.6, 3.7, 3.11, 3.12, 3.13, 3.15. *What is only believed.* Leaf Scalar, and the identification in Lemma 3.2's standing note. Checks: `checks/hard-core--mapped_contour_gradient.py` PASS; `checks/hard-core--mapped_onshell_flux.py` PASS (C1 to C7, identity to 1e-12); `checks/hard-core--mapped_sigma2.py` table only; `checks/hard-core--mapped_moyal.py` PASS; `checks/hard-core--mapped_beta_numeric.py` PASS (item 7).

#### 3.9 Notes toward Leaf Scalar and the vacuum subtraction (derived where marked; none load-bearing yet)

(a) *Alternative form with no massless fine scalar (derived algebra, not yet used).* With A the block average on sites, Q_path D = D_k A, and C^sc := log integral d omega delta(A omega) e^{-omega^* X_f^2 omega} = -2 log det X_f + log det Z', Z' := (A X_f^-2 A^*)^-1, one has Gamma_c = C_k - C^sc - log det(Z'^-1 Z), Z = D_k^* h D_k. C^sc is gapped and is treated like Prop 3.11. Also Z^-1 = Z'^-1 + N C_T N^*, with N = (D_k^*D_k)^-1 D_k^* Q^o on T' and C_T the gapped transverse covariance.

(b) *Plan for Leaf Scalar (only believed).* Expand E_theta in covariant words D^alpha, with heat-kernel bounds |[e^{-tau X} D^alpha](0,0)| <= C tau^{-2-n/2} and difference from theta = 0 at most C theta^2 tau^{-n/2}. The linear theta term vanishes by reflection. Low modes X <= Lambda |theta| have rank per cell at most C Lambda^2 theta^2 by the diamagnetic inequality and ||Y|| <= C Lambda |theta|, contributing O(theta^3). Crude position-space moments lose a logarithm, because Y(z) ~ |z|^-6, so high modes need the Moyal cancellation.

(c) *The vacuum subtraction (derived, elementary).* -E_k[S_empty] = -sum_{j>k} vac_j = O(N_k), so the total normalisation E(beta) is the natural subtraction. A chessboard bound cannot replace the large-field operation: sum_j N_j z_j >> N_K, with z_j the rarity of a level-j region, so the vacuum values of the R-terms must sit in the subtraction E.

(d) *Fixed-point reading (only believed).* beta^0_infinity = a log L should come from pi[S_infinity](p) - pi[S_infinity](L p).

*Numeric lock, reported.* My first run of `checks/hard-core--mapped_onshell_flux.py` (about 1 second) executed while the numeric lock was held by another session, because I read a "held" reply as success. Later runs wait for actual ownership.

### 5. A second route for the core: real variables, one convex step, rare cells

Status: formulation with reasons, derived 2026-10-30 after reading the account's chapters 4.15, 4.23, 4.27. Not yet a proof. Each claim below is either marked proved with a pointer or listed as an obligation. Balaban's objects (block average, minimal configuration, running coupling, vacuum subtraction) are kept and credited; the account is the map I read. The departures are mine.

**Why look for it.** Nearly all of the account's open statements on large fields concern one thing: analyticity of stored terms on complex domains, under moves of determining sets, with oscillation budgets (Thm 4.23:thm-oscillation-theorem, Thm 4.27:thm-arrest-theorem, Rem 5.10:rem-old-terms-beside). The running radii alpha_{i,n} = g_n C_i (log g_n^-2)^q of [119 (2.28)] are forced by thresholds eps_k = g_k p_0(g_k): a cost of polylog size allows only a polylog oscillation, so a tube of size about g. Analyticity itself enters through Cauchy bounds on derivatives and through the interface. If derivatives are propagated directly on real fields, and sources are real, none of this is needed.

**The density is the object.** Let M-tilde be any total smooth extension of the block average (loops clipped where not small), so V_{k+1} = M-tilde(V_k) is defined on all fields and rho_{k+1}(V) = integral dV_k delta(M-tilde V_k, V) rho_k(V_k) holds exactly, with rho_0 = e^{-x_0 A}. No reference law, no history, no live region, no R. The hypothesis at level k is one statement about one function:

    (I_k)  on the class C_k := { V_k : flux per level-k plaquette <= a_c },  -log rho_k = x_k A_k + vac_k + R_k,

with A_k the minimal fine energy given V_k, x_k the running inverse coupling, vac_k a number per cell (a local functional of the source when there is one), and R_k a real smooth gauge-invariant function whose derivatives of order n obey a tree-decay bound, plus

    (U_k)  an upper bound on rho_k off C_k, per non-class cell.

a_c depends on d and L only. It is a constant, not g p(g). The cost of a non-class cell is e^{-c a_c^2 x_k}.

**One step.** Fix V_{k+1} in D_{k+1}. Write V_k = Exp_{V*}(g_k B), with V* the minimiser of A_k over the fibre, in the coordinates of 5.1. Insert 1 = prod_c (chi_c + (1 - chi_c)), with chi_c a compactly supported log-concave function of the variables of the cell c alone, independent of V_{k+1}, whose support lies inside the class. The term with all factors chi_c is an exact, uniformly log-concave integral T(V_{k+1}); no extension of the action is needed. Then rho_{k+1} = e^{-vac_k - x_k A_{k+1}(V_{k+1})} [ T(V_{k+1}) + sum over families of bad cells ], all terms positive.

- *No threshold p(g), no small-field cut inside the class.* The whole class is one uniformly log-concave integral. The energy package (`library/block-poincare-energy-package.md`) supplies the gap and decay, with no M. Non-Gaussian vertices need not be small pointwise, only small in Hessian: |g D^2 V_3| <= C a_c.
- *No linear term.* D_B S(0; V) = 0 for every V, so all mixed derivatives D_V^m D_B^n S are bounded polynomially in |B| with no factor x. Hence D_V^n log T is bounded independently of x, by Helffer-Sjöstrand cumulant bounds.
- *Contraction without derivative loss.* D_V^n of R_k composed with the lift is an average of D^n R_k, not a higher derivative. The lift carries L^-1 per field, and a tree-decay l^1 norm picks up one factor L^4 per cell. So order n >= 5 contracts by C_0^n L^{4-n}. Orders <= 4 are read from Taylor data at V = 1 and gauge invariance: only the vacuum and the F^2 coefficient can survive. That coefficient is beta_{k+1}, and x_{k+1} = x_k - beta_{k+1}.

**Rare cells without live regions.** For a non-class cell under a class parent, the ratio of the L-part to T is a conditional odds. It is bounded by e^{-c x a_c^2} per cell by an energy excess: the hole keeps its own energy, and the exterior problem keeps its constraint with the hole data in it, so nothing is gained there. Derivatives in V_{k+1} cost at most a factor (C x)^n against that margin, so no oscillation budget arises. A non-class cell with a non-class parent is simply part of (U_{k+1}). So non-class cells under non-class parents form a subcritical tree, with L^4 e^{-c x a_c^2} << 1: the live count of the account's fundamental difficulty, L^{4(k-j)} e^{-p_0(g_j)}, is replaced by a convergent branching sum, because a fine cell under a class parent has been summed into R at once.

**Why the account's other devices are not needed on this route, if it holds.** Waiting and arrest protect a preparation of R over many stages: there is none. Second-class components arise when an exterior has no regular filling (non-trivial holonomy around an annulus): here the conditioning is on the parent field on the whole shadow of the cell, so no filling is asked for. Stored-term domains are real class conditions, nested automatically because a class field lifts to a field of flux L^-2 smaller. The two-threshold split served the same conditional-mean problem.

**Cost, stated plainly.** (i) The output is real. Sources are real and bounds are on derivatives of each fixed order: UV-EXT in the C^n form of the request below, not a complex disc. (ii) Each derivative bound has its own constant, with no factorial control. (iii) Taylor extraction must be done gauge-invariantly on real fields, without Cauchy. (iv) The family sum needs a decay estimate for a polymer gas with many-body weights; `library/polymer-covariance.md` gives it from first differences alone, with polymers at a constant range. (An earlier version of this paragraph expected a range of order log x. That came from integrating a hole before its exterior, which makes the exterior action a mixture of wells, non-convex at switching surfaces with strength x^2 e^{-2 mu d} in the B variables. Keeping hole data fixed until the exterior is integrated removes it.)

**What would kill it, and the state of each.**
(a) Failure of the energy excess when a hole's data shifts the exterior constraint. Checked: `library/critical-class-and-excess.md` proves the excess given its inputs; the shift is a factor L^-3 per cell and the pairing with the multiplier is small against the cell's own energy. My first two versions failed: a bad-box rule forced an infinite ladder of thresholds, and an annular hole made the relative field multi-valued. Both are fixed there.
(b) Tree decay of cumulants. Closed: `library/convex-laplace-tree-decay.md`, by synchronous coupling, with no cumulant combinatorics and no dependence on the volume.
(c) The upper chain needing analyticity. Its Text 7 accepts the real form with a bilinear factor. Request filed.
(d) A gauge-invariant Taylor remainder. Not yet written. The design is below; I see no obstruction, but this is belief.

#### 5.1 Coordinates: exact tree gauge, no gauge-fixing integral

Fix V' in D_{k+1}, and V* the minimiser of A_k on its fibre. In each box fix a maximal tree rooted at the block centre, and fix V_k = 1 on it by the level-k gauge transformations that are trivial at centres. For a gauge-invariant integrand this is an exact identity of Haar integrals, with no Faddeev-Popov determinant and no Gribov question. Let B be the remaining bond variables, V_k(b) = e^{i g_k B(b)} V*(b), with the block constraint solved on designated bonds. The Hessian in these coordinates has a gap gamma/C(L): for B in tree gauge, the Landau representative B_L = B + D omega has omega determined along the tree within the box, so ||B||^2 <= C(L) ||B_L||^2, and on B_L Theorems 5 and 7 of the package apply. Bonds are in log coordinates, with Haar density a product of local factors. Constants here may depend on L. They enter smallness conditions on x_k^-1 and the sources, not the contraction, which is governed by the gauge-invariant main term of the lift.

The hypotheses (H1)-(H3) of the Laplace lemma for S(B; V') = x_k [A_k(Phi(V',B)) - A_{k+1}(V')] + R_k(Phi(V',B)) - log J + (extension) follow from: x_k g_k^2 = 1, so D_B^a D_V^b of the first term is g^{a-2} D^{a+b}(A_k o Phi), bounded for a >= 2; D_B S(0; V') = g D R_k(V*), since V* is critical for A_k for every V'; and D_V^b S(0; V') is D_V^b [R_k o V*]. No factor of x_k remains.

*Coordinates that make the cut independent of V'.* Let the free variables xi be B on the bonds that are neither tree bonds nor designated. Each constraint is solved on one designated bond at the peak of its weight rho_c, where the neighbouring constraints have vanishing weight, so the elimination has finite range and does not chain. Then the cells partition the free variables, chi_c depends on xi_c alone, and the chart depends on V' only through Phi(V', xi). If all xi_c lie in the supports, then B on the designated bonds is at most C(L) times the cut radius, so the support radius tau/g with tau = T_c/C(L) keeps V_k in C_k. The version of the Laplace lemma with cut, `library/convex-laplace-tree-decay.md`, needs exactly this: the barrier block-diagonal over cells and independent of v. Status: derived. The earlier Huber extension of the action is dropped: it needed a domination inequality between the true action and its extension, and a signed remainder. Obligation `Geometric package` keeps the bounds (H1)-(H3) in these coordinates.

#### 5.2 Labels of the rare configurations

(Derived.) Given V_k in the fibre of V', first find the core C: the cells with flux above T_c, through a smooth partition in the flux. The hull of C is C with its pockets filled, its 2-cycles spanned by 3-chains inside each box (`Cut and Poincare`), and a collar of width d_1. Outside the hull, partition by the cut chi_c on the free variables: Y' is the set of cells outside the hull that fail it. Outside the boxes meeting or adjacent to C, Y' is the set of cells failing chi_c. A site is a connected component at range d_0 of this data, labelled by (part of C, part of Y'). All fields in the hull of a site, and on Y', are integrated with no further label; fields in a box meeting C but outside the hull are in the exterior, with a chart adapted to that box after the cut. Consequences:

- The term with C and Y' empty is exactly the base integral T, since inside the cut the flux test is automatically passed. So the base term has the cut chi alone, independent of V'.
- All terms are positive, and exterior to the sites the measure is the base measure.
- A membrane spanning an annular core has low energy and bad amplitude, and it is not a label. *Correction, from a hostile check:* its location is fixed by the tree gauge of the box, not by the spanning chain I choose for the hull. A flat exterior with holonomy around a small annulus shows bad amplitude on a surface reaching far across the box. So the amplitude test must be switched off in every box that meets the core or is adjacent to one. In those boxes only the flux test is used, the fields are class, the action is exact, and the only labels are the core cells. Exact partition: 1 = sum_C prod_C (1 - chi^f) prod_{C^c} chi^f times, over boxes away from C, prod_cells (chi^a + (1 - chi^a)). The term with C and Y' empty is still T. An intermediate version asked a polymer with a membrane to pay per membrane cell, which is false; another used the chain as the location of the membrane, which is also false.

Costs. A cell of Y' pays c x_k tau^2, by convexity at fixed data, since all nearby flux is below T_c. A cell of C pays c_b x_k T_c^2 by Block energy. The entropy of a site is C(L) log x_k times (|C| + |Y'|), since |hull| <= C(L) |C| within a box, boxes with at least L^3/10 cells of C being treated whole, as in `library/critical-class-and-excess.md`.

**Prop R1 (rarity of a site, implication from the listed inputs).** For V' in D_{k+1}, F a family of sites and gamma compatible with it, N_{F u gamma}/N_F <= z^{|gamma|}, z := exp(-c x_k tau^2 + C(L) log x_k), uniformly in F and its data.

*Proof.* Fix the data of F. *Numerator.* Let Hull be the hull of gamma, Ext its complement. By (P_k) of 5.3 if a cell of gamma is above T_f, and by the formula if not, the density is at most the exterior weight e^{-x_k A^Ext - R^Ext} times the cost of gamma, with the classical energy split additively over Hull and Ext by dropping the plaquettes between them. The block average excludes lines through core cells, so the exterior's constraint carries no shift from them. *Denominator, by Jensen.* In T, for exterior B_E take the hole variables within distance 1 of a local extension of B_E. Then S <= S^Ext(B_E) + x_k (reference energy on Hull) + C |B_boundary|^2 + C |Hull|, where the term in B_boundary has no x, by x_k g_k^2 = 1. So T >= c^{|Hull|} e^{-x_k (ref. energy on Hull)} Z_Ext < e^{-C |B_boundary|^2} >_Ext >= e^{-x_k (ref. energy on Hull) - C' |Hull|} Z_Ext, by Jensen and the local moments of the Laplace lemma. *Divide.* The Gaussian normaliser of Ext cancels exactly, because Z_Ext is the same integral on both sides. The reference energy on Hull is at most (c_s/K_0^2) T_c^2 |Hull| <= (c_b/4) T_c^2 |C| with K_0^2 ~ L^{3/2}. QED.

Note. This replaces the expansion at the reference in `library/critical-class-and-excess.md` by additivity and Jensen, and with it the inputs `Relative chart` and `Shift bound`. That note keeps the arithmetic of thresholds and the geometric leaf. Its Excess Lemma remains true given its inputs, but this route does not use it.

Label: implication. Inputs: (P_k), `Cut and Poincare`, `Block energy`, `Regularity` on regions (for the local extension), the Laplace lemma on Ext.

**Corrections to the above, from later hostile checks (read this first).** (a) "The block average excludes lines through core cells, so the exterior's constraint carries no shift": wrong. Lines through non-core cells of the hull still enter. Now the kernel excludes all lines through the hull, which C determines. Then the denominator's exterior average differs from the numerator's, and T needs a shift map. So "the Gaussian normaliser of Ext cancels exactly" holds only after that map. (b) Reference energy on Hull is not all of the classical term: there is also the gain from relaxing Ext. Both are in Lemma 6 of `library/relative-density-bound.md`. (c) The hull is no longer pockets and spanning chains: it is the bounding cubes of the cube rule, and thresholds are K_0^2 = K-bar L^{5/3}, T_f ~ L^{1/6} T_c. (d) The proof of record for rarity is now Prop 8 there, (RP'_k) with (CI), and it uses neither (P_k) nor a dropped exterior. Also the exterior of a cube has zero modes unless the tree is chosen for the hole, with a chart that depends on the site; the base integral T keeps its own tree.

#### 5.3 Above the formula range

*Status note.* (P_k) below is the earlier statement. The main line for rarity is now (RP'_k), `library/relative-density-bound.md`, Prop 8. (Loc_k), Theorem OS, (H1)-(H3) with sites and `Regularity` below stay in use.

**Named, and how it now reads.** (P_k): an upper bound on the exact density rho_k at every field, with a cost per cell above T_f, an exterior weight that is smooth and uniformly convex, and the vacuum number per cell exactly right. Nothing about hole data enters, and no tower is ever displayed.

Let F_k := -log rho_k. For V_k, let Y be the cells with flux above T_f, and E the cells at distance at least d_1 from Y. Then

    (P_k)  F_k(V_k) >= vac_k |Lambda_k| + x_k A^E_k(V_k|_E) + R^E_k(V_k|_E) + c_P x_k T_f^2 |Y| - C(L) |Y| log x_k.

Here A^E_k is the minimal fine energy in the fine plaquettes of E, given the data on E, and R^E_k is the sum over cells in E of the local densities of R_k, available by (Loc_k) below. c_P does not degrade with k.

**Why (P_k) closes on itself in one level (derived, given the listed inputs).** Fix V_k. rho_k(V_k) is the fibre integral of rho_{k-1}, with the kernel excluding from each block average the lines through children above T_f. Split the children into the blocks of bonds of E, called E', and the rest, H'. Constraints do not straddle this split, so the delta functions factorise. Sum over the set Y' of children above T_f, and insert (P_{k-1}).

1. *Classical energy adds.* A^{E''}_{k-1} >= A^{E''∩E'}_{k-1} + A^{E''∩H'}_{k-1}, by dropping fine plaquettes between the two, for E'' the exterior of Y'. This drops classical energy only. The vacuum numbers vac_{k-1} stay on every cell, so no fine-level surface term is lost. (An earlier attempt dropped plaquettes at level 0 in the Wilson weight itself, which loses a surface energy of order (s_k/eta)^3. That route is dead.)
2. *R splits.* R^{E''}_{k-1} is a sum of local densities, so it splits, with a boundary error at most C per boundary cell at level k-1, a constant per cell of Y.
3. *The part over E'.* This is the one-step integral with free boundary at H': uniformly convex by the package and `Cut and Poincare`, with bad children in E' a rare gas under a parent below T_f, by Prop R1. It defines A^E_k + R^E_k and contributes the vacuum number exactly on E, up to C per boundary cell.
4. *The part over H'.* No convexity is used. Tree gauge turns the fibre integral over children into a product over independent plaquette angles, by Haar invariance: the non-tree bonds are in bijection with a maximal independent set of plaquettes, so int e^{-(x/2) c sum_p phi(theta_p)} <= prod (C x^{-3/2} + e^{-c x/2}). This matches the x-power of the vacuum number per dof, up to C(L) per cell. So the hole contributes vac on H' up to C(L) per cell.
5. *The cost.* A cell of Y at level k has either at least half of its lines not excluded, and then its children carry energy at least c_b T_f^2 by Block energy, with half of the exponent kept for it and half for the integrability in step 4; or at least L^3/2 excluded children, each paying c_P x_{k-1} T_f^2 from (P_{k-1}). In the second case the sum is far above the required cost. Each cell's cost is fresh, computed at its own level, so c_P := min(c_b/4, ...) does not degrade. Since x_{k-1} >= x_k, the factor x is fine.
6. *Sum over Y'.* In H': a factor prod (1 + e^{-c x T_f^2 + C log x}) <= e^{tiny |H'|}.

Base: k = 0, F_0 = x_0 A, E, Y by plaquette angles; additivity gives it with no entropy.

**(Loc_k).** If V_k is in D_k on a ball B(y, 2d), then |D_y^n (F_k - x_k A^{B(y,d)}_k)| <= C_n e^{-mu' tau(y)} + C_n (x_k e^{-mu d})^n. So beyond a collar d_x ~ (log x_k)/mu from the bad cells, F_k has a Hessian x_k D^2 A + O(1), hence uniformly convex in B variables. Inside that collar it may be non-convex at strength x_k e^{-2 mu d} in B variables, because of mixtures of wells of the hole beneath. That is real. So in the exact measure the fields within d_x of a site are part of the site's data (hard-core range d_0 = 2 d_x), while the rarity uses (P_k) with the classical collar d_1 alone, which is constant.

*Reduction of (Loc_k) to one statement (derived, given the inputs named).* Fix V_k, possibly wild far from y. On the fibre, make the children of Y_k(V_k)^{+d_x} one permanent site W, always present, whose data are all fields there. The other sites are the rare ones of 5.2, as Bernoulli variables. Conditional on all site data, the exterior is uniformly log-concave, by (Loc_{k-1}) beyond the collars. So F_k = -log of a mixture over site data of convex integrals. Then D_y^n F_k is a sum of joint cumulants of local functions under the exact fibre measure, and three things bound them: the cumulant split (S), the conditional covariance (C), and the polymer lemma for conditional means. The classical term: for fixed data, D_y of the minimum m(V; data) is x_{k-1} D_y A_k^{B(y,d)} up to x e^{-mu d}, by the decay of the exterior response. That is the origin of the tail term: the covariance over data of D_y m is at most (x e^{-mu d})^2. So (Loc_k), (I_k) and the one-step at a fibre are one statement:

**Theorem OS (one step with sites; target).** Given (Loc_{k-1}), (P_{k-1}) and the bounds on R_{k-1}: for every V_k and every y at distance d >= d_x from Y_k(V_k), the bound (Loc_k) holds with C_n obeying the recursion of Text 5.5, and F_k = x_k A_k + vac_k + R_k on D_k.

The recursion for C_n needs no separate work: at level k-1 the relevant points are at distance L d in level-(k-1) units, so the tail term there is smaller, and the bulk contraction applies. Status: derivation of the structure. The inputs are listed under Obligations. Not a proof until (H1)-(H3) with sites are written.

**Theorem OS, written against the current labels (derived as labelled; not a proof until the listed inputs close).** Take x_k >= x_*(L), large enough that d_x >= 3 L. Then a site's collar covers whole boxes, and *the exterior of a site is a union of whole boxes*. So no cube, hull-adapted tree, excluded line or free boundary is visible to the exterior: site data are fixed and their plaquettes retained, and a variation v is extended by zero into them. (H1) is Theorems 5, 7 by IMS, as below.

*Corrections found in writing this.* (a) The tail in (Loc_k) as stated, (x_k e^{-mu d})^n, is wrong below d_x, where x e^{-mu d} < 1: a mean field gives x e^{-mu d} at every order n, so the tail is C_n max(x e^{-mu d}, (x e^{-mu d})^n). Consumers use only d >= d_x, where it is at most C x e^{-mu d}, and (RP'_k) has this tail in its statement. (b) With V_k wild far from y there is no global V*. The chart's reference near y is U^ref: the minimiser with free boundary at the permanent site, defined by convexity on the class of boxes around y, used only classically, with no integral over a free-boundary region. Its gradient mismatch against a fixed data d is at most g x e^{-mu d}, which is (H3) at d >= d_x.

*Step 1, mixture.* On the fibre of V_k, F_k = -log sum_d Z(V_k; d), d = all site data including the permanent site. Z(V_k; d) is one uniformly log-concave integral with a cut independent of V_k. -log Z = x_{k-1} m(V_k; d) + g(V_k; d), where m is the classical minimum with data d, and g is x-free by the Laplace lemma, given (Loc_{k-1}) at distance L d in level-(k-1) units.

*Step 2, cumulants.* D_y^n F_k is a sum over partitions of joint cumulants, in the law of d, of D^{pi} (x m + g). The conditional part is (C) of the Laplace lemma. The law of d is a polymer gas with (A1) from (RP'_k) at level k-1 and (A2) with kappa_0 ~ x T_f^2. By (S) all orders reduce to covariances, and `library/polymer-covariance.md` Lemma 2 bounds these, with prefactor z.

*Step 3, classical term.* D_y^n m(V; d) = D_y^n A^{B(y,d)} + O(T_f e^{-delta r(d)}), r(d) the distance from y to the nearest site of d. So x D^n m - x D^n A^B has size x e^{-delta d} at worst, its fluctuation is carried by rare sites at r with weight z, and the permanent site contributes a shift and a variance (x e^{-mu d})^2.

*Step 4, locality against far data.* The low-order Taylor argument (Lemma 3 of `library/gauge-taylor-contraction.md`) needs: if V, V'' agree and are class on B(y, r), then |D_y^n F_k(V) - D_y^n F_k(V'')| <= C e^{-nu r} + tail. V and V'' may be connected by no path in the class, and their site structures may differ, so interpolation of actions alone is not enough. Route: Dobrushin comparison, the two-boundary form of Lemma 1 of `library/polymer-covariance.md`, namely |mu(f) - mu''(f)| <= sum_j [sum_i G_{ji} osc_i(f)] b_j, with b_j the variation of site j's conditional law between the two boundary data. b_j is at most z^{|j|} min(1, kappa_0 |j| e^{-mu_1 d(j, outside)}). Conditional means given sites: synchronous coupling with the same d, the difference being a propagator across r. Status: the comparison is Lemma 3 there, proved; its use is a sketch.

*Step 5, recursion.* C_n as in Text 5.5, with the norm read as sup over (V, y, d >= d_x) of the local derivatives of F_k - x_k A^B. The bulk contraction and the data recursion are unchanged, because they read fields near y only.

*Hostile note.* The chain (RP'_{k-1}) -> (A1) -> Theorem OS at k -> (Loc_k) -> (RP'_k) is one induction on k. Its order is sound: (RP'_k) uses (Loc_{k-1}) on children, and (A1) at level k uses (RP'_k) and (Loc_k) on level-k fields beyond the hull, for the fibre to level k+1. So (A1) at k feeds Theorem OS at k+1. In (A1)'s denominator I used (Loc_k) at distance d_x from W_far's rough parts; that is available. What I have not excluded is a bad interaction between step 3's x-factor and (A2) at pairs with kappa >= 1. That case is covered by rarity alone, as stated in 5.4, and the hard core d_0 = 2 d_x makes it empty at range unless x T_f^2 e^{-mu_1 d_0} >= 1, which fails for x large.

**Routes that failed on this inequality, in order tried.**
1. *Integrate the hole, then the exterior, with a collar d_x in the classical comparison.* The reference energy in the collar is (c_s/K_0^2) T_c^2 d_x^4 per cell, above the hole's cost for large x, which would force polylogarithmic thresholds. Replaced: collar d_x only in the data of the site; collar d_1 in the classical energy.
2. *Dropping plaquettes at level 0.* Loses the fine surface vacuum energy.
3. *Unconditional chessboard on all-bad configurations.* The recursion is clean, but it prices a probability, not the odds at fixed V'. Kept as a possible check of rates. Credit: the upper chain's Theorem 2, after Froehlich, Israel, Lieb and Simon.
4. *Pointwise ratio against a filled field.* Does not recurse: below the top of a tower the parent is bad and its lift can be above threshold, and for a large hole no small-flux filling need exist. (Corrected later: with constant thresholds a tube of radius R_0 does fill, and a fixed far field with the collar inside I repairs the recursion; (RP'_k), `library/relative-density-bound.md`.)
5. *One induction over all hole structures with live data and position-dependent weights (Mix).* I believe it can be made to work, and it is closest to Balaban's formula, but it carries weights with a jump x_o/x_l that can be large, and a family of mixed functionals. (P_k) with (Loc_k) asks for less: one function F_k on all fields. Superseded, not refuted.

**Hostile notes on (P_k).** (a) Step 3 needs, for E with arbitrary shape, the one-step theorem with free boundary, including `Regularity` on regions and uniform bounds; this is the new content, and `Cut and Poincare` is at box level there. (b) Step 2 needs local densities of R_k on partial fields; the construction by sequential local deformation to the trivial field inside balls stays in the class, so it should exist, but it is not written. (c) In step 4 the bijection between non-tree bonds and independent plaquettes must respect the constraints: the fibre removes one bond per block constraint, and the count of dof must match vac on H' to C(L) per cell, including the zero-mode factors of the gauge group, which are compact. I have checked the power of x, not the constants. (d) The kernel: excluded lines are decided by a smooth partition in the flux, so rho_k is the density of a Markov kernel, not of a map. Total mass and source derivatives are unaffected. On the class the kernel is the deterministic block average. (e) What would refute (P_k): a field at which the true density exceeds it. Test: d = 2, where the density is the exact product of heat kernels K_tau(theta_p). There (P_k) holds with c_P close to its bound, since K_tau(theta) ~ exp(-theta^2/(4 tau)) up to a power, and the block average is a holonomy. This is a consistency check in a model with no fluctuating exterior, not evidence in d = 4.

Label: step-by-step derived given inputs (Loc_{k-1}), Prop R1 at level k-1, the one-step theorem on regions. Not a theorem until those close.

**(H1)-(H3) with sites: the route tried now (derived as labelled).** Fix site data. Let H := D_xi^2 S on the exterior, in B units, so that x_k g_k^2 = 1 removes the coupling.

*Local form of the Hessian (from (Loc_k)).* For y, y' within d of each other and at distance at least d_x from the sites, H(y,y') = D^2 A^{B(y,2d)}(y,y') + E(y,y'), with |E| <= C g^2 + (x e^{-mu d})^2 g^2. The last term is x e^{-2 mu d} in B units, below any fixed constant beyond d_x. For |y - y'| > d, tree decay gives |H(y,y')| <= C e^{-mu' d}.

*IMS localisation (derived).* Let chi_b be a smooth partition on balls of radius d, with sum chi_b^2 = 1 and |grad chi_b| <= C/d. Then <v, H v> = sum_b <chi_b v, H chi_b v> - (1/2) sum_b sum_{y,y'} (chi_b(y) - chi_b(y'))^2 v(y) H(y,y') v(y'), and by the decay of H the last term is at most C d^-2 ||v||^2.

*One ball (from the package).* On a ball, chi_b v has a Landau representative H-tilde, and by Theorem 7, D^2 A^B[chi_b v, chi_b v] >= <H-tilde, K H-tilde> - C(L) Lambda ||H-tilde||^2. Its block average is not zero: Q^o (chi_b v) = chi_b Q^o v + [Q^o, chi_b] v, and the commutator is at most C (L/d) ||v||_{loc}, since Q^o has range L in level-k units, while chi_b varies at scale d. So Theorem 5 in the form ||H||^2 <= C_P ( ||grad_U H||^2 + ||Q^o H||^2 ) gives D^2 A^B[chi_b v, chi_b v] >= (gamma/C(L)) ||chi_b v||^2 - C (L/d)^2 ||v||^2_{loc}.

*Sum.* <v, H v> >= (gamma/C(L) - C d^-2 - C (L/d)^2 - C g^2 - small) ||v||^2. So d = d_2(L) makes this at least gamma/(2 C(L)), and then x_k large. The ball radius d_2 is a constant, depending on L.

*(H2), (H3).* Derivatives of S in xi and V' are read from (Loc_k) on balls of radius d_x with the x-free bound, and the chart Phi is local. The gradient at xi = 0 is g D R, plus a tail from the sites of size g x e^{-mu d}, which is small at distance d_x. So beyond d_x, (H3) holds at xi = 0 with no recentring. Within the collar there are no exterior variables, because the collar is site data. So the shifted cut is not needed: an earlier version of 5.3 recentred at B* near a hole, and with collars d_x as site data, the gradient at 0 is already of order one.

**Status.** With this, (H1)-(H3) with sites follow from (Loc_k) with its constants, and Theorem 5, with the block average as a bounded term, and Theorem 7 on a ball. This is an implication, and it uses (Loc_k) at the same level whose closure it serves. The order is not circular: F_k on the exterior at level k-1, with (Loc_{k-1}), gives the one-step integral at level k. **Still to be checked:** that D^2 A^B has the Landau reduction in tree-gauge coordinates, with the factor C(L) only once; and that the exterior variables near a site, at distance just above d_x, have a full set of constraints, which `Cut and Poincare` supplies at box level. In particular if a collar of width d_x exceeds the box side L, the site's shadow covers whole boxes, and then the boxes are simply in the site, which is simpler.

**Hostile note.** The site now has hull and collar of width d_x ~ (log x_k)/mu, as data. Its entropy is C d_x^4 log x_k per core cell, far below x_k tau^2, and the reference energy in the collar enters only in (A1)'s Jensen bound. There the classical collar is d_1, not d_x: the numerator is bounded with exterior weight including the region between d_1 and d_x by the classical energy, not by F_k. So in the (A1) estimate the variables in the collar between d_1 and d_x are integrated with the classical convex weight plus the bound C + C x e^{-mu d} on the local density of R, which is at most C x e^{-mu d_1} per cell at the inner edge. This must be below c tau^2 x. So d_1 >= (1/mu) log(C/(c tau^2)), a constant depending on L, as already assumed. Checked here.

**`Regularity`: routes tried on it.**

*Failed: a trial field by iterating a one-step lift.* Let V_{j-1} := lift(V_j) repeatedly down to level 0. If one lift has sup-norm constant C_1 on flux in its own units, the curvature in level-k units after k-j lifts is C_1^{k-j} a. It stays bounded only if C_1 = 1, and that holds for constant flux but not for a general V. So this gives no bound uniform in k.

*Not needed: Moser iteration at the fine level.* I had planned an epsilon-regularity estimate for D*F = Q*lambda. Most consumers do not need a pointwise bound, as below. It may still serve for item (R3), but the linear route there is simpler.

*Route now (labels per step).*

(R1) *Trial field, one shot (derived, standard construction).* Given W on the level-k bonds of a region with flux at most a, build U^tr on the level-k skeleton: on each level-k bond, a straight fine path carrying W uniformly; on each 2-face, the radial filling of its boundary holonomy, with curvature uniform up to C a; on 3-cells and 4-cells, the cone extension from the centre in radial gauge, whose curvature is bounded by that of the boundary times a constant, because a <= T_f is small and the cell has unit size. This is gauge covariant and local, with pointwise fine curvature at most C a and no accumulation over levels: it is built once, not level by level. It need not satisfy M^k(U^tr) = W; the residual is at most C a per bond.

(R2) *Fixed point around the trial (derived, given Theorem 6).* Solve D_U A(e^{i eta H} U^tr) = Q^{o*} lambda, N^(k)(e^{i eta H} U^tr) = W, for (H, lambda), in the norm sup over cells of the Eps norm on the cell, and the sup norm for lambda. Sad(U^tr) is invertible with exponential decay, so its inverse is bounded on these local sup norms, with no volume factor. Non-linear terms: the cubic form of A is at most ||dH||_{L^2(c)} ||H||_{L^4(c)}^2 per cell, by the lattice Sobolev inequality on a unit cell, uniform in eta. The constraint's second-order term is at most sum_j C(L) s_j ||H||^2_{L^2(c^+)}, by Step 4 of Theorem 7, with no factor of k. The data are at most C a. So the map contracts on a ball of radius 2 C a in this norm, for a <= a_*. This gives existence, uniqueness in the ball, and ||F(U)||_{L^2(c)} <= C a. Differentiating in W, Combes-Thomas gives decay of the response at rate delta_* in level-k units.

(R2') *Consequence (derived).* Theorems 5-7 at U = U_k(W) do not need pointwise R(a) at U. K(U) - K(U^tr) is bounded on Eps by C ||H||_{Eps}, by the same cubic bound. Lambda is bounded by ||F||_{L^2} (Step 5 of Theorem 7 uses only that). In Lemma 4 of the package, the transports of U differ from those of U^tr by a line sum of eta H, which enters the block average bilinearly and is bounded in L^2 by Cauchy-Schwarz over lines. So pointwise R(a) is needed at the trial field only, and there it holds by construction.

(R3) *The reference one level down (derived, given (R1) with a smooth trial and (R2); not reviewed).* The arithmetic of thresholds needs flux_c(M^k(U_{k+1}(V'))) small against flux(V'). (R2) at level k+1 gives only the L^2 norm on a box, which allows all the energy in one level-k cell. Interior regularity: work in level-(k+1) units on a box, with a cutoff zeta at box scale, in the box's axial gauge, where A^tr has |A^tr| <= C flux'. Take the trial of (R1) smoothed at box scale, by flat collars in the radial parameters, so that it is C^2 at that scale, |grad F^tr| <= C flux'. The equation for H reads K(U^tr) H = -D* F^tr + Q^{o*} lambda + N(H), with |lambda| <= C flux' and Q^{o*} lambda bounded in L^2, by Lemma 4 of the package at a background (pointwise it need not be: residual contour sums concentrate near nested block centres). So -Delta (zeta H) is, in L^2, at most C flux' + C ||H||_{Eps(box+)} + C a_* ||grad(zeta H)||_{L^2} + the non-linear term ||H||_{L^4} ||grad (zeta H)||_{L^4} + lower. On the lattice ||grad^2 f||_{L^2} <= C ||Delta f||_{L^2} is a Fourier identity, uniform in eta, and the lattice Sobolev inequality gives ||grad f||_{L^4} <= C (||grad^2 f||_{L^2} + ||grad f||_{L^2}), uniform in eta. No Calderon-Zygmund theorem is used. The non-linear term has a small factor ||H||_{L^4(box+)} <= C a_*, so it is absorbed. Hence ||F(U_{k+1}(V'))||_{L^4(box)} <= C flux', C free of k and of L.

A level-k plaquette angle is <rho_p, F> with ||rho_p||_{L^2} <= C, scale invariantly in d = 4. So |theta_p| <= C ||F||_{L^2(c)} <= C |c|^{1/4} ||F||_{L^4(c)} = C L^-1 ||F||_{L^4}. Therefore

    flux_c(M^k(U_{k+1}(V'))) <= C_r L^-1 flux(V').

This is one power of L, not the two a smooth field would have. I do not need the second: the thresholds now read T_c = a_*/L^2, K_0^2 ~ L^{3/2}, T_f := L T_c/(C_r K_0) ~ L^{1/4} T_c, still above T_c for L large. A parent in D_{k+1} lifts below T_c/K_0, which is all that is used. The earlier statement with L^-2 in `library/critical-class-and-excess.md` is corrected there. Numerical check, pre-registered, for when the numeric lock is free: d = 3, L = 3, a non-uniform V', max over level-1 cells of flux against flux'/L at k = 1, 2, with the ratio below 10 and not growing from k = 1 to 2.

**Status of `Regularity`.** Existence, uniqueness in a ball, L^2 and L^4 bounds, decay, and the lift bound with L^-1: derived from (R1), (R2), (R3), not reviewed. (R1) is a construction I have described and not written in lattice detail.

#### 5.4 Polymers and decay

**Setting (derived).** Fix V' and all hole data held in F. By positivity, with weights W(F) := N_F / T: for gamma compatible with F, (A1) N_{F u gamma}/N_F <= z^{|gamma|} uniformly in F and its data: this is Prop R1.

(A2) Fix all hole data. The mixed second difference of log Z^ext in two holes gamma, delta is the mutual information density of (xi_gamma, xi_delta) in a uniformly log-concave law, with parameter dependence bounded by the Laplace lemma, so it is at most kappa_0 |gamma| |delta| e^{-mu_1 d(gamma,delta)}, kappa_0 ~ x_k, uniformly in the rest. Only this first difference is used.

**Decay of all derivatives (implication).** By `library/polymer-covariance.md`, the covariance of two bounded functions of the family with local oscillations is at most C z A_f A_g e^{-nu d}, nu = min(mu_1/2, a/(2 d_0)). The exact fibre law is a mixture over families of convex laws. Total covariance splits into the conditional covariance, bounded by (C) of the Laplace lemma, and the covariance of conditional means, bounded by the polymer lemma, the oscillation of a conditional mean under adding gamma being at most C x^M (1 + |gamma|) e^{-mu_1 d}, by the propagator bound. The cumulant split (S) of the Laplace lemma, at the largest edge of a spanning tree, reduces all orders to two-point bounds. So D_V^n of log(rho_{k+1}/T) obeys a tree-decay bound with prefactor C_n z'' x^{M n}. The range d_0 = 2 d_x is needed only so that the exterior of a site is convex; the lattice-animal constant c_a ~ d_x^4 is absorbed by z. For pairs with kappa >= 1, the influence is bounded by the rarity alone.

**Status.** This closes `Rare cells` as an implication from (A1), (A2) and the oscillation bound. The factor x^{M n} is absorbed by z'' ~ e^{-c x tau^2}.

**Hostile notes.** (a) The states of a polymer include hole data, so its conditional law is on a continuous space; Lemma 1 there needs only bounded functions and total variation, and the oscillation of a conditional mean is taken at fixed data of the others. (b) The functions in the covariance must be bounded. A conditional mean of a local polynomial is bounded by local moments uniformly in the family, by Step 1 of the Laplace lemma, for exteriors with holes. (c) The polymer lemma gives decay at rate nu, limited by mu_1/2, not by the much larger rate of polymer chains. This is enough. (d) Failed routes on the way: Dobrushin on cell statuses, separating shells, chain orders adapted to the derivative points, Kirkwood-Salsburg with many-body weights, Langevin coupling on the exact measure. Reasons in `library/polymer-covariance.md`.

#### 5.5 Taylor on real fields, and the contraction

Norm: for n >= 5, ||R||_n := sup over V in D_k and x_1 of the sum over x_2, ..., x_n of |D_{x_1...x_n} R(V)| e^{mu tau}. Data: D^2 R(1), D^3 R(1), D^4 R(1), with moments.

*High orders.* With Ghat(x,y) the lift kernel in level-(k+1) units, sup_x sum_y |Ghat| <= C_1 and sup_y sum_x |Ghat| <= C_1' L^4 with C_1, C_1' free of L: this gives ||R o V*||_n <= C_1' C_1^{n-1} L^{4-n} ||R||_n, so contraction for n >= 5 and L > C_1^4 C_1'. The Laplace lemma adds cross terms with a factor g^2 and lower norms, by Step 4 there: its order-n bound uses orders at most n of R, so there is no derivative loss. The cut in the extension adds a factor e^{-c x_k T_c^2} on lower norms.

*Low orders from high orders, and locality.* Field differences need locality: for V, V'' equal on a ball of radius r around x and in D_k there, |D_x^n R(V) - D_x^n R(V'')| <= C e^{-mu r}. This needs no path in D_k: compare the two fibre integrals with S_t = (1-t) S_V + t S_{V''} on one coordinate space. The forcing is far from x, so the Laplace lemma gives the tail, with no factor of x_k. Then: for flux a near x, take r ~ a^{-1/2} and deform V near x to 1 inside D_k, in axial gauge with (a r^2) small. Taylor at V = 1 gives D^n R(V) up to order 4 from the data at 1 and ||R||_5, up to e^{-mu r} = o(a^m).

*Data at 1.* The recursion is exact: D^2 (R o V*)(1) = Ghat^T D^2 R(1) Ghat, and Pi-hat(p) = beta (p^2 delta - p p) + O(p^4) by gauge invariance and hypercubic symmetry; the F^2 coefficient is removed into x_{k+1}, and the rest contracts by L^-2. In detail Pi-hat_{k+1}(p) = L^2 sum_n Ghat*(p + 2 pi n) Pi-hat_k((p + 2 pi n)/L) Ghat(p + 2 pi n); the n = 0 term of a p^4 symbol gives L^-2 p^4, and the aliases, with Ghat(p + 2 pi n) = O(p) for n != 0, feed a term of size L^-2 into beta. Checked by hand, not proved. D^3, D^4 at 1 have Ward identities tying their low moments to D^2, and contract by L^-2 likewise.

*Written up in `library/gauge-taylor-contraction.md`.* Lemma 1 there (vanishing orders) is proved: from the exact identity under smooth gauge transformations of the parallel transports of a slowly varying connection, the Taylor coefficients of total weight at most 5 of D^2, D^3, D^4 at 1 are those of c A. Lemma 2 (contraction of divided symbol norms, factor L^-2) is derived at n = 2, and by scaling at n = 3, 4. No alias enters the F^2 coefficient, because the lift of constant flux is exact (Lemma 3.3). So beta_{k+1} = beta^0_{k+1} + O(C(L) g_k^2), which is (P2). Lemma 3 (low orders at a rough field from data and the order-5 norm) is derived given (Loc). An earlier version of that note wrongly fed an alias term into beta; recorded there.

*An alternative design, not used.* The data at 1 alone do not obviously organise the low orders at a rough field. Better: R_k o V* evaluates R_k only on fields smooth at level k, with |F_k| <= L^-2 |F'|, |grad F_k| <= L^-3 |grad F'|. So write Z_k := R_k - beta A_k as vac + sum_x P_x(jets of F at x) + Rem, with P_x a gauge-covariant local polynomial of dimension 6, 8, ... up to D_*, and |D^n Rem| at most C ||Z_k||_N a^{N-n}, a the local flux. The coefficients of P_x form a finite vector which contracts by L^-2 or better, with a source from the one-loop functional and O(g^2) ||R||_{<= N} from the Gaussian average of the rough part. Rough directions at the next level then enter only through the order >= 5 norm. A wrong step here would show as growth in k. Status: design; obligation `Taylor`.

*Result, if the obligations close.* R_k bounded uniformly in k; beta_{k+1} = beta^0_{k+1} + O(g_k^2) + O(e^{-c x_k T_c^2}), which is (P1)-(P3) of the account in sharper form, with no polylogarithmic thresholds.

#### 5.7 Hostile check of Text 5, recorded

1. *Does the extended exterior minimum lie in the class?* Prop R1 bounds an integral over class exteriors by the convex extension, and the Excess Lemma bounds the true action on the class. If the extended minimum sat outside the class, m(xi) would not be bounded by the excess. It does not: beyond the collar the minimiser has flux at most T_c/K_0 + C_r T_f e^{-delta d}, which is below T_c at d = d_1. Halving the action to dodge this would cost a constant per exterior degree of freedom, an extensive loss, so the collar is necessary.
2. *Why did Balaban not do this?* I do not know of an obstruction, and that is itself a warning. Part of the answer is visible: thresholds at g p(g) and radii proportional to g force live regions, by the oscillation budget, and a real-variable step removes the budget. But I have not found a place in his papers that excludes this route, and my own check is one reader. If a kill exists, I expect it in `Tower bound` or in the first use of (H2) near a hole, where (H2) is asked with constants free of x_k although the action has a large gradient near the hole. Centring removes the gradient for each fixed xi. Differences between xi are handled by interpolation, so only moments enter.
3. *Output weaker than the account's target?* Yes. There is no analyticity and no complex source. The upper chain's Text 7 says this still gives the linear field with the bilinear factor. No factorial control in n: T1 needs each n separately, so it is not on the critical path, but later targets may need it.
4. *What is not proved.* (H1)-(H3) with sites, Theorem OS as a whole, Local coupling, Assembly, the symbol bounds of the non-linear lift, local densities of R_k, and the leaves Regularity on regions, Cut and Poincare, Leaf Scalar. Proved outright (own proofs, unreviewed): the Laplace lemma version 2, the polymer covariance lemmas, vanishing orders (Taylor Lemma 1), Theorems 5-7 of the energy package at R(a), (P_0). Implications from named inputs: (P_k) from (P_{k-1}), Prop R1, decay of the gas, Taylor Lemmas 2-3 and the recursion.
5a. *Newest steps attacked, this stretch.* (i) The chain from `Taylor`: my first draft fed an alias of the irrelevant part into beta; the exact lift of constant flux forbids it, and in the quadratic form the alias symbol carries |p|^3 from the massless term of the denominator. (ii) (P_k): the danger was a lost surface vacuum. Dropping plaquettes at level 0 loses it; dropping classical energy at level k-1 only, with vac_{k-1} on every cell, does not. I checked the power of x in step 4 and not the constants. (iii) Prop R1: an extension of the exterior into the hole could leave the support of the cut, so the Jensen step must be restricted to boundary amplitudes well inside the support, which costs a factor at least (1/2) per boundary cell by sequential conditioning. Stated here, not written out. (iv) A polymer with a membrane cannot pay per membrane cell; labels by core and hull repair it. (v) I have not found a kill. What I would test next is d = 2 O(N)-type analogues: this route would apply to them too, and the ultraviolet problem there is reported open, which is a reason for suspicion and not only for hope.
5. *Older step attacked.* The Excess Lemma went through three versions in this session. The first, a Sobolev class, was unnecessary. The second, dropping bad boxes, needed an infinite ladder. The third, with |Y-hat| <= |Y|^{4/3}, ignored holonomy around annuli inside a box. The present form cuts along spanning 3-chains, and K_0^2 ~ L^{3/2} pays for them. I have not looked for a fourth failure in `Shift bound` for shapes other than the annulus, which is why it is a named input.

#### 5.6 Sources and assembly

Sources: F_k(V; w) = x_k A_k + sum_c w_k(c) A_c(U_k(V)) + vac_k(w) + R_k(V; w), with w_k(c) the source at level k, equal to w up to a summable drift, since one loop is independent of x and the two-loop change is of order g_k^4. The classical term has no mixed derivative in separated w, since A_c is local in U_k. Mixed derivatives in w at separated points therefore come only from R_k, with tree decay at level k, hence only from levels with a_k comparable to the separation. Assembly: at level K', with a_{K'} below the separation and x_{K'} fixed, the separated cumulant of log Z_L is a cumulant under the coarse measure of bounded local functions, up to the tails. Off the class those functions are controlled in L^n(mu), by the rarity of trees. Hence UV-LOC-R. Status: design; obligations `Local coupling`, `Assembly`.

### 4. The interface: what UV-EXT can and cannot say

1. *Trivial bound.* For real A, |Z(beta + s)| <= Z(beta + Re s). So the unsubtracted modulus bound is the real statement at a shifted coupling.
2. *It is not the subtracted statement.* Let S be the analytic subtraction, S(s) = sum_j N_j e_j(s). Then S(Re s) - Re S(s) is about (1/2) e_2 (Im s)^2 N_0, with e_2 > 0 the plaquette-energy variance per site, of order g^4, and N_0 ~ a^-4 Vol. So the trivial bound loses a^-4 Vol at Im s != 0. A subtracted complex bound needs the complex run of the RG, as the account does with its sourced densities.
3. *Non-vanishing is not delivered, and is not needed.* The RG gives an upper bound on |e^{-E} Z| and the lower bound Z(beta) at s = 0. Jensen then allows up to C Vol zeros in the disc. A zero-free disc uniform in the volume would be analyticity of the infinite-volume pressure in the coupling, an infrared statement beyond the reach of a UV argument.
The account's chain does not use it: the torus bound writes connected functions as polynomials in ratios of derivatives of Z-tilde at 0, and the per-ball bound uses chessboard on periodised sources with a re-centred counterterm (draft 3.4, 3.6). Its bound has the volume factor Q in that polynomial.
4. *Proposed wording (taken from the account's (3.6), for the target lead to adopt or change).* UV-EXT': for complex weights w in a class W of Lipschitz functions with sup |w| < rho, there are numbers e_j(X; w), j <= K', X in D_j, analytic in w, vanishing at w = 0, reading w only on X^+, bounded by C e^{-(1-delta) kappa d_j(X)}, such that with E(w) = sum_{j,X} e_j(X;w), |e^{-E(w)} Z(w)| <= e^{c |Lambda_{K'}|} Z(0), uniformly in a and the volume. For the constant source this is the original UV-EXT without the non-vanishing and without the lower bound on the modulus. This form is what the hard core should aim at, and it is the form to test against the decisive question in `CHARTER_UP.md`.
