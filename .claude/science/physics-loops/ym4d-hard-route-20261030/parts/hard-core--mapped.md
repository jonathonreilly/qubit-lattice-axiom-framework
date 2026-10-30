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

**Second formulation, now the main line (Text 5).** Work with the exact density on real fields, with a constant class threshold, one uniformly convex integral per step, and non-class cells priced by an energy excess. No R, no histories, no complex tube. Deliverable: UV-LOC-R (Requests), which the upper chain's real fallback consumes.

**Hardest remaining inequality.** The Excess Lemma together with its upper bound off the class (Text 5, kill criterion (a)): for V' class and V_k in its fibre with non-class set Y, the effective action exceeds the reference by c x_k T^2 |Y| net of an entropy of order |Y| log x_k, including when the non-class cells sit over a tower of finer non-class cells. For (P1): only the high-mode write-up of `Leaf Scalar`.

**Routes tried and why they failed.**
- Direct bound of each composite diagram for Gamma_k: fails. Individual diagrams with the second jet of the k-fold average
  are of order k before gauge cancellation (Text 3.4). Hence the organisation by constant flux.
- Sum of squared weights as a growth rate for the block variance: fails as a danger signal. Sigma^2(L) > 1 for odd L >= 23
  looked like a loss of coercivity at large L; it is not, because the contour part is a coarse gradient (Text 3.2). Recorded
  so nobody repeats it.
- Holonomy bound of the account as the target: dropped. On my trace it is not consumed by clauses (0) or (i) (Text 2.2).

- Immediate conditional odds given the exterior of a hole only: not uniformly small, because an exterior at threshold forces the interior up. This is the true content of Balaban's waiting. Conditioning on the parent field on the whole shadow removes it (Text 5).
- Dobrushin uniqueness on status cells: fails at adjacency, since a wild cell can make its neighbour's non-class state as likely as its class state. Connected polymers with an absolute Peierls bound replace it.

- Dropping every box that contains a bad cell: forces an infinite ladder of thresholds (`library/critical-class-and-excess.md`).

**Next action.** `Tower bound`, as the likeliest place for a kill, including the exterior comparison with hole data at each level. Then `Taylor`, then `Rare cells` at higher derivatives. `Regularity` and `Relative chart` are next among the leaves, because several implications rest on them. `Leaf Scalar` stays frozen with its consumer.

**Numerics this session.** Moyal check PASS after a test bug was found and fixed; B_2 - B_1 = 0.4263 against c_0 = 0.4081 at L = 3, pre-registered tolerance 25 percent (Text 3.8).

**Hostile check of the newest step, recorded.** Text 3.8 for (P1), Text 5.7 for the real route.

## Obligations

- gap: Leaf Scalar, high-mode expansion of the scalar remainder with a spectral cut (frozen, Text 3.7) -> Theorem P1
- implication: Theorem P1 given Leaf Scalar -> flow bounds, clause (0)
- gap: Regularity of the constrained minimiser: existence and uniqueness on D_k, fine curvature at most C_r flux(V), and flux of M^k(U_{k+1}(V')) at most C_r L^-2 flux(V') -> Geometric package, Excess Lemma
- gap: Relative chart -> Excess Lemma
- gap: Cut and Poincare, frozen leaf with statement in `library/critical-class-and-excess.md` -> Excess Lemma
- gap: Shift bound for general shapes, frozen with the previous leaf -> Excess Lemma
- implication: Excess Lemma given Regularity, Relative chart, Cut and Poincare, Shift bound, Block energy, `library/critical-class-and-excess.md` -> Prop R1
- implication: Prop R1 given the Excess Lemma, the Laplace lemma, and the Geometric package, Text 5.2 -> rare cells
- gap: Geometric package: tree-gauge chart of the fibre, convex extension, hypotheses (H1)-(H3) of `library/convex-laplace-tree-decay.md` with constants free of x_k (orders derived in Text 5.1) -> real one-step theorem
- gap: Tower bound: costs of trees of cells above T_f add, with exterior comparison at each level (design in Text 5.3) -> rare cells
- gap: rare cells: polymer sum with positive weights, first derivative derived, higher derivatives by Kirkwood-Salsburg (Text 5.4) -> real one-step theorem, (P3)
- gap: Taylor: orders <= 4 from the order >= 5 norm plus data at V = 1, with locality and Ward constraints (design in Text 5.5) -> real one-step theorem, (P2)
- gap: real one-step theorem: (I_k) and (U_k) imply (I_{k+1}) and (U_{k+1}) with contraction on order >= 5 and on the data at 1 -> UV-LOC-R
- gap: local coupling version: F_k(V; w) with real position-dependent w and derivatives in w -> UV-LOC-R
- gap: assembly: last coarse integral, cumulants in L^n of the coarse measure, UV-LOC-R and CT4 -> upper chain
- discharged: tree decay of all derivatives of a uniformly convex integral, free of the volume, `library/convex-laplace-tree-decay.md` (own proof, not reviewed) -> real one-step theorem, replaces the walk expansion and M-freeness
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

**One step.** Fix V_{k+1} in C_{k+1}. Write V_k = Exp_{V*}(g_k B), with V* the minimiser of A_k over the fibre, Q_1 B = 0, on the whole linear space. Replace the action beyond the class by a uniformly convex extension S^ext with the same derivative bounds. Then rho_{k+1} = e^{-vac_k - x_k A_{k+1}(V_{k+1})} [ T(V_{k+1}) + L-part ], where T = integral dB e^{-S^ext(B; V_{k+1})} and the L-part is supported where some level-k cell is non-class.

- *No threshold p(g), no small-field cut inside the class.* The whole class is one uniformly log-concave integral. The energy package (`library/block-poincare-energy-package.md`) supplies the gap and decay, with no M. Non-Gaussian vertices need not be small pointwise, only small in Hessian: |g D^2 V_3| <= C a_c.
- *No linear term.* D_B S(0; V) = 0 for every V, so all mixed derivatives D_V^m D_B^n S are bounded polynomially in |B| with no factor x. Hence D_V^n log T is bounded independently of x, by Helffer-Sjöstrand cumulant bounds.
- *Contraction without derivative loss.* D_V^n of R_k composed with the lift is an average of D^n R_k, not a higher derivative. The lift carries L^-1 per field, and a tree-decay l^1 norm picks up one factor L^4 per cell. So order n >= 5 contracts by C_0^n L^{4-n}. Orders <= 4 are read from Taylor data at V = 1 and gauge invariance: only the vacuum and the F^2 coefficient can survive. That coefficient is beta_{k+1}, and x_{k+1} = x_k - beta_{k+1}.

**Rare cells without live regions.** For a non-class cell under a class parent, the ratio of the L-part to T is a conditional odds. It is bounded by e^{-c x a_c^2} per cell by an energy excess: the hole keeps its own energy, and the exterior problem keeps its constraint with the hole data in it, so nothing is gained there. Derivatives in V_{k+1} cost at most a factor (C x)^n against that margin, so no oscillation budget arises. A non-class cell with a non-class parent is simply part of (U_{k+1}). So non-class cells under non-class parents form a subcritical tree, with L^4 e^{-c x a_c^2} << 1: the live count of the account's fundamental difficulty, L^{4(k-j)} e^{-p_0(g_j)}, is replaced by a convergent branching sum, because a fine cell under a class parent has been summed into R at once.

**Why the account's other devices are not needed on this route, if it holds.** Waiting and arrest protect a preparation of R over many stages: there is none. Second-class components arise when an exterior has no regular filling (non-trivial holonomy around an annulus): here the conditioning is on the parent field on the whole shadow of the cell, so no filling is asked for. Stored-term domains are real class conditions, nested automatically because a class field lifts to a field of flux L^-2 smaller. The two-threshold split served the same conditional-mean problem.

**Cost, stated plainly.** (i) The output is real. Sources are real and bounds are on derivatives of each fixed order: UV-EXT in the C^n form of the request below, not a complex disc. (ii) Each derivative bound has its own constant, with no factorial control. (iii) Taylor extraction must be done gauge-invariantly on real fields, without Cauchy. (iv) The L-part needs a Mayer expansion with real activities and an interaction across the convex exterior of size x a^2 e^{-mu d}, which forces polymers of range about log x. This is the one place a scale like Balaban's R_k returns.

**What would kill it, and the state of each.**
(a) Failure of the energy excess when a hole's data shifts the exterior constraint. Checked: `library/critical-class-and-excess.md` proves the excess given its inputs; the shift is a factor L^-3 per cell and the pairing with the multiplier is small against the cell's own energy. My first two versions failed: a bad-box rule forced an infinite ladder of thresholds, and an annular hole made the relative field multi-valued. Both are fixed there.
(b) Tree decay of cumulants. Closed: `library/convex-laplace-tree-decay.md`, by synchronous coupling, with no cumulant combinatorics and no dependence on the volume.
(c) The upper chain needing analyticity. Its Text 7 accepts the real form with a bilinear factor. Request filed.
(d) A gauge-invariant Taylor remainder. Not yet written. The design is below; I see no obstruction, but this is belief.

#### 5.1 Coordinates: exact tree gauge, no gauge-fixing integral

Fix V' in D_{k+1}, and V* the minimiser of A_k on its fibre. In each box fix a maximal tree rooted at the block centre, and fix V_k = 1 on it by the level-k gauge transformations that are trivial at centres. For a gauge-invariant integrand this is an exact identity of Haar integrals, with no Faddeev-Popov determinant and no Gribov question. Let B be the remaining bond variables, V_k(b) = e^{i g_k B(b)} V*(b), with the block constraint solved on designated bonds. The Hessian in these coordinates has a gap gamma/C(L): for B in tree gauge, the Landau representative B_L = B + D omega has omega determined along the tree within the box, so ||B||^2 <= C(L) ||B_L||^2, and on B_L Theorems 5 and 7 of the package apply. Bonds are in log coordinates, with Haar density a product of local factors. Constants here may depend on L. They enter smallness conditions on x_k^-1 and the sources, not the contraction, which is governed by the gauge-invariant main term of the lift.

The hypotheses (H1)-(H3) of the Laplace lemma for S(B; V') = x_k [A_k(Phi(V',B)) - A_{k+1}(V')] + R_k(Phi(V',B)) - log J + (extension) follow from: x_k g_k^2 = 1, so D_B^a D_V^b of the first term is g^{a-2} D^{a+b}(A_k o Phi), bounded for a >= 2; D_B S(0; V') = g D R_k(V*), since V* is critical for A_k for every V'; and D_V^b S(0; V') is D_V^b [R_k o V*]. No factor of x_k remains. The extension: below flux T_c the action is exact; beyond, replace the local quadratic form by a Huber profile psi_kappa(l_x(B)), with l_x = Delta^{1/2}(x, .), plus a small quadratic, and cut the non-Gaussian part with a cutoff eta_x at |g dB| ~ T_c. Then D_B^2 [eta (s - q)] is of order T_c, and D_B^a [eta (s-q)] of order g^{a-2} T_c^{3-a}, so it is bounded for x_k large. The gap of S^ext is kappa gamma/C(L). Status: this paragraph is a derivation of orders of magnitude; obligation `Geometric package`.

#### 5.2 Rare cells, first generation

**Prop R1.** For V' in D_{k+1} and Y a set of level-k cells, let N_Y be the fibre integral of e^{-x_k A_k - R_k} over those V_k in D_k whose cells above T_c are exactly Y. Then N_Y <= T(V') exp( -(c_b/16) x_k T_c^2 |Y| + C(L) |Y| log x_k ).

*Proof given the inputs.* Let Y-hat^+ be Y-hat with a collar of width d_1 ~ (log L)/delta_*, on which the fine curvature of U_k(V_k) decays below C T_c by Combes-Thomas, so that the exterior has R(a_*). For hole data xi on Y-hat^+, the exterior integrand is uniformly convex. Let m(xi) be its minimum and S_xi the centred action, which has (H1)-(H3) with no factor of x_k. The Excess Lemma gives m(xi) >= (c_b/8) x_k T_c^2 |Y|. For two hole data, |log Z_xi - log Z_0| <= integral_0^1 dt |<S_xi - S_0>_t| <= sum_x C e^{-mu d(x, Y-hat)} <= C |Y-hat^+|: the two centred actions differ with a tail, and the local moments are uniform in t by Step 1 of the Laplace lemma, for S_t = (1-t) S_xi + t S_0. The hole integration has volume at most (C sqrt(x_k))^{dim |Y-hat^+|}. From below, T >= the part with |xi'| <= 1, which is at least c^{|Y-hat^+|} Z_0, since m(xi') <= C |xi'|^2. Divide, and use |Y-hat^+| <= C(L) |Y|. QED

Note on x_k: the exterior integral has been compared exactly, so its Gaussian normaliser cancels. The surviving entropy is only on the hole.

#### 5.3 Towers: cells above the formula range

A level-k cell above T_f has no formula. Replace rho_k there by its fibre integral at level k-1, so the field is live one level down; repeat on any child above T_f, down to level 0 at worst, where the density is e^{-x_0 A} and the variables are Haar. The block average at each level excludes loops through children above T_f; a parent with fewer than half of its lines left is given an independent Haar value, as a Markov kernel, which leaves total mass unchanged. This keeps every small-field computation smooth, and only total mass and source derivatives are consumed.

*Ledger.* A cell above T_f pays either from its non-excluded children, whose energy is at least c_b T_f^2 by Block energy and is disjoint from the excluded children, or, when at least half of its lines are excluded, from at least L^3/2 excluded children. So the costs of a tree add without double counting: at least (c_b/16) x_j T_f^2 per cell of level j. The entropy per cell is at most C(L) log x_j. Since L^4 exp(-c x_j T_f^2) << 1, the trees form a subcritical branching process. This is the replacement of the account's fundamental difficulty: a fine cell under a parent in D is summed into R_{j+1} at once, and only a chain of cells all above T_f stays live, with a cost for each link. Status: this paragraph is the design; obligation `Tower bound`.

#### 5.4 Polymers and decay

With N_Y and the trees bounded, write rho_{k+1}/T = sum over families of connected polymers gamma at range d_0 ~ C log x_k. Separated polymers factorise up to e^{epsilon}, |epsilon| <= kappa (|gamma_1| + ...), kappa <= x_k^M e^{-mu d_0}, uniformly in the family, by the propagator bound (J) applied to the two boundary perturbations; this is a pair-sum bound with no many-body growth, because the contraction in (J) does not depend on the other perturbations. All weights are positive. So log(rho_{k+1}/T) has a telescoping expansion with terms bounded by the activity, by monotonicity in the allowed set. Its first derivative at y is a difference of two conditional expectations of a local function, bounded by C x_k (density of polymers near y) plus a tail. Higher derivatives need truncated polymer correlations; the route is Kirkwood-Salsburg with conditional energies bounded as above. The factor x_k^n in the n-th derivative is absorbed by the margin e^{-c x_k T_c^2}. Status: first derivative derived; higher ones route only; obligation `Rare cells`.

#### 5.5 Taylor on real fields, and the contraction

Norm: for n >= 5, ||R||_n := sup over V in D_k and x_1 of the sum over x_2, ..., x_n of |D_{x_1...x_n} R(V)| e^{mu tau}. Data: D^2 R(1), D^3 R(1), D^4 R(1), with moments.

*High orders.* With Ghat(x,y) the lift kernel in level-(k+1) units, sup_x sum_y |Ghat| <= C_1 and sup_y sum_x |Ghat| <= C_1' L^4 with C_1, C_1' free of L: this gives ||R o V*||_n <= C_1' C_1^{n-1} L^{4-n} ||R||_n, so contraction for n >= 5 and L > C_1^4 C_1'. The Laplace lemma adds cross terms with a factor g^2 and lower norms, by Step 4 there: its order-n bound uses orders at most n of R, so there is no derivative loss. The cut in the extension adds a factor e^{-c x_k T_c^2} on lower norms.

*Low orders from high orders, and locality.* Field differences need locality: for V, V'' equal on a ball of radius r around x and in D_k there, |D_x^n R(V) - D_x^n R(V'')| <= C e^{-mu r}. This needs no path in D_k: compare the two fibre integrals with S_t = (1-t) S_V + t S_{V''} on one coordinate space. The forcing is far from x, so the Laplace lemma gives the tail, with no factor of x_k. Then: for flux a near x, take r ~ a^{-1/2} and deform V near x to 1 inside D_k, in axial gauge with (a r^2) small. Taylor at V = 1 gives D^n R(V) up to order 4 from the data at 1 and ||R||_5, up to e^{-mu r} = o(a^m).

*Data at 1.* The recursion is exact: D^2 (R o V*)(1) = Ghat^T D^2 R(1) Ghat, and Pi-hat(p) = beta (p^2 delta - p p) + O(p^4) by gauge invariance and hypercubic symmetry; the F^2 coefficient is removed into x_{k+1}, and the rest contracts by L^-2. D^3, D^4 at 1 have Ward identities tying their low moments to D^2, and contract by L^-2 likewise. Status: design; obligation `Taylor`.

*Result, if the obligations close.* R_k bounded uniformly in k; beta_{k+1} = beta^0_{k+1} + O(g_k^2) + O(e^{-c x_k T_c^2}), which is (P1)-(P3) of the account in sharper form, with no polylogarithmic thresholds.

#### 5.7 Hostile check of Text 5, recorded

1. *Does the extended exterior minimum lie in the class?* Prop R1 bounds an integral over class exteriors by the convex extension, and the Excess Lemma bounds the true action on the class. If the extended minimum sat outside the class, m(xi) would not be bounded by the excess. It does not: beyond the collar the minimiser has flux at most T_c/K_0 + C_r T_f e^{-delta d}, which is below T_c at d = d_1. Halving the action to dodge this would cost a constant per exterior degree of freedom, an extensive loss, so the collar is necessary.
2. *Why did Balaban not do this?* I do not know of an obstruction, and that is itself a warning. Part of the answer is visible: thresholds at g p(g) and radii proportional to g force live regions, by the oscillation budget, and a real-variable step removes the budget. But I have not found a place in his papers that excludes this route, and my own check is one reader. If a kill exists, I expect it in `Tower bound` or in the first use of (H2) near a hole, where (H2) is asked with constants free of x_k although the action has a large gradient near the hole. Centring removes the gradient for each fixed xi. Differences between xi are handled by interpolation, so only moments enter.
3. *Output weaker than the account's target?* Yes. There is no analyticity and no complex source. The upper chain's Text 7 says this still gives the linear field with the bilinear factor. No factorial control in n: T1 needs each n separately, so it is not on the critical path, but later targets may need it.
4. *What is not proved.* Everything marked design or route: Geometric package, Tower bound, the higher derivatives in Rare cells, Taylor, Local coupling, Assembly, and the leaves Regularity, Relative chart, Cut and Poincare, Shift bound. Proved here: the Laplace lemma; Theorems 5, 6, 7 of the energy package at R(a); the Excess Lemma and Prop R1, each as an implication from named inputs.
5. *Newest step attacked.* The Excess Lemma went through three versions in this session. The first, a Sobolev class, was unnecessary. The second, dropping bad boxes, needed an infinite ladder. The third, with |Y-hat| <= |Y|^{4/3}, ignored holonomy around annuli inside a box. The present form cuts along spanning 3-chains, and K_0^2 ~ L^{3/2} pays for them. I have not looked for a fourth failure in `Shift bound` for shapes other than the annulus, which is why it is a named input.

#### 5.6 Sources and assembly

Sources: F_k(V; w) = x_k A_k + sum_c w_k(c) A_c(U_k(V)) + vac_k(w) + R_k(V; w), with w_k(c) the source at level k, equal to w up to a summable drift, since one loop is independent of x and the two-loop change is of order g_k^4. The classical term has no mixed derivative in separated w, since A_c is local in U_k. Mixed derivatives in w at separated points therefore come only from R_k, with tree decay at level k, hence only from levels with a_k comparable to the separation. Assembly: at level K', with a_{K'} below the separation and x_{K'} fixed, the separated cumulant of log Z_L is a cumulant under the coarse measure of bounded local functions, up to the tails. Off the class those functions are controlled in L^n(mu), by the rarity of trees. Hence UV-LOC-R. Status: design; obligations `Local coupling`, `Assembly`.

### 4. The interface: what UV-EXT can and cannot say

1. *Trivial bound.* For real A, |Z(beta + s)| <= Z(beta + Re s). So the unsubtracted modulus bound is the real statement at a shifted coupling.
2. *It is not the subtracted statement.* Let S be the analytic subtraction, S(s) = sum_j N_j e_j(s). Then S(Re s) - Re S(s) is about (1/2) e_2 (Im s)^2 N_0, with e_2 > 0 the plaquette-energy variance per site, of order g^4, and N_0 ~ a^-4 Vol. So the trivial bound loses a^-4 Vol at Im s != 0. A subtracted complex bound needs the complex run of the RG, as the account does with its sourced densities.
3. *Non-vanishing is not delivered, and is not needed.* The RG gives an upper bound on |e^{-E} Z| and the lower bound Z(beta) at s = 0. Jensen then allows up to C Vol zeros in the disc. A zero-free disc uniform in the volume would be analyticity of the infinite-volume pressure in the coupling, an infrared statement beyond the reach of a UV argument.
The account's chain does not use it: the torus bound writes connected functions as polynomials in ratios of derivatives of Z-tilde at 0, and the per-ball bound uses chessboard on periodised sources with a re-centred counterterm (draft 3.4, 3.6). Its bound has the volume factor Q in that polynomial.
4. *Proposed wording (taken from the account's (3.6), for the target lead to adopt or change).* UV-EXT': for complex weights w in a class W of Lipschitz functions with sup |w| < rho, there are numbers e_j(X; w), j <= K', X in D_j, analytic in w, vanishing at w = 0, reading w only on X^+, bounded by C e^{-(1-delta) kappa d_j(X)}, such that with E(w) = sum_{j,X} e_j(X;w), |e^{-E(w)} Z(w)| <= e^{c |Lambda_{K'}|} Z(0), uniformly in a and the volume. For the constant source this is the original UV-EXT without the non-vanishing and without the lower bound on the modulus. This form is what the hard core should aim at, and it is the form to test against the decisive question in `CHARTER_UP.md`.
