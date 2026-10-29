# PRE-STATED

UTC: 2026-10-28 23:53:13 UTC. Written before reading SMALLNESS_DAG.md or its graph/checker/source constraints. Prior exposure: the user's summary of F1, F2, F3, TC and the requested attack directions. This is an independent hostile source/code/math review of the local candidate, not a retained-status audit. No git; the only file written is this report. Python checks will suppress bytecode and run in memory/stdout.

Refutation criteria, fixed before examination:

1. An encoded edge with a reversed prerequisite, wrong colliding symbol, or no supporting source constraint refutes that edge's asserted fidelity. Audit at least 40 distinct edges; report exact counts and the rational error rate, distinguishing unsupported from demonstrably false edges.
2. A source-required omitted edge that closes a directed cycle refutes the written-hierarchy acyclicity claim (as distinct from acyclicity of the supplied finite graph). A genuine omitted dependency without a proved return path remains an omission, not a fabricated cycle. In particular inspect epsilon_1, epsilon_0, the complex radius, node A's constants and n_sharp.
3. A finite directed cycle accepted by the checker, including a self-loop, disconnected cycle, duplicate-edge case or unregistered endpoint, refutes the relevant checking guarantee. Inadequate designed controls alone establish incomplete coverage, not algorithmic failure. Use an independent algorithm and exact finite tests.
4. A mismatch in the exact RLARGE substitution, the TC inequality direction, or any claimed rational factor refutes the numerical claim. Rational arithmetic and symbolic identities only; decimal labels must be justified by rational brackets.
5. A live K/volume dependence omitted or assigned to the wrong object refutes the corresponding uniformity inventory. An unproved uniformity claim is NOT-VERIFIED, not automatically REFUTED.
6. A live simultaneous feasibility condition, unsupported uniformity assumption, or required back-dependency prevents banking the unconditional retirement of the decade ledgers. Graph sorting alone cannot certify existence of jointly admissible constants.

Verdicts will be CONFIRMED / NOT-VERIFIED / REFUTED, each with file and locating string. What can be banked will be separated from unresolved proof obligations. Findings and evidence follow below as checks are completed.

## Verdict

**The encoded strict graph is acyclic, and the four TC failure factors are correct. The graph is not a complete certificate of the written hierarchy or of simultaneous feasibility. Unconditional retirement of the feasibility ledgers is REFUTED.** No new unconditional mathematical cycle is claimed here.

Here and below, filenames without a directory are relative to this report's directory, denoted `L`. Bare source stems such as FLOW, SF and PROOF mean the corresponding `.md` files. `EXISTENCE.md` means `../ym4d-existence/EXISTENCE.md`; all `dag55_*` files are under `checks/`. Edge numbers are the zero-based indices in `checks/dag55_2_graph.py`, also printed in SMALLNESS_DAG Appendix B. CONFIRMED for an edge means that its dependency and objects are supported; it does **not** prove the analytic hypothesis at either endpoint.

| Claim | Verdict | Evidence and precise scope |
|---|---|---|
| 189 nodes, 362 edges; 358 strict edges form a DAG | CONFIRMED | `dag55_2_graph.py`; `dag55_2_dag.py`, `STRICT_EXCLUDE`; independent transitive-closure check agrees with the supplied SCC routine. |
| Exactly two cyclic components after restoring the four excluded edges | CONFIRMED | `dag55_2_out.txt`, `B-all`; these are two SCCs, **not two elementary cycles**. There are ten vertex-simple directed cycles in the encoded graph. |
| The source hierarchy is completely represented and acyclic | NOT-VERIFIED | Missing cutoff-family edge `n_sharp -> SC_k`, documented below; unresolved cutoff uniformity and FI-1 remain. No additional strict source cycle was established in this review. |
| Every sampled edge is source-faithful | REFUTED | Edge 293 substitutes `N_prime` for different inputs in SF's band window. Two further sampled edges have unresolved statement/endpoint fidelity. |
| C_fun is the only tagged growth reaching g0 | CONFIRMED | `dag55_2_dag.py`, `propagate`; `V_LF` is another live growth seed, but its outgoing edge absorbs it. This is an annotation/reachability result. |
| No other live K/T growth exists in the proof | NOT-VERIFIED | The checker reads hand-entered tags; twelve live nodes even have `vol` containing `unstated` and no weak tag. No extra actual volume-divergent constant was proved here. |
| Six live weak seeds, all reaching g0 | REFUTED as originally written; corrected version CONFIRMED | SMALLNESS_DAG, `Errata`, item 1: six tags, **five** reach g0. Independent per-seed propagation reproduces that correction. Six is not an exhaustive count of outstanding uniformity proofs. |
| TC fails by the advertised rounded factors | CONFIRMED | RLARGE, `b_1 := n_P + 12κ(1 + A_d(L))²`; HIST, `η_q := min`; HW, `(TC) ε_loc/2`; exact derivation below. |
| Every live constraint is an upper bound on a later choice, so magnitudes decide nothing | REFUTED | SMALLNESS_DAG headline 8 and §8.3; TC itself, EXISTENCE's `Compatibility (K)`, and the omitted complex-width interface are feasibility conditions. |

## 1. Edge sample: 72 distinct edges

This is a purposive, stratified sample, selected after the preliminary source scan, not a random sample and not a pre-registered error-rate estimator. It covers FLOW, the stage-0 chain, RLARGE/HW, N5/BR1, BFT, and the existence consumer. I checked source context rather than treating a successful substring lookup as verification. The endpoint metadata and its supplementary references were included, especially for colliding symbols and superseded constants.

**Results: 69 CONFIRMED, 1 REFUTED, 2 NOT-VERIFIED.** Definite sample error rate: **1/72** (exactly **25/18 percent**). Unresolved fidelity: **2/72 = 1/36**. Counting all edges not confirmed gives **3/72 = 1/24** (exactly **25/6 percent**). These fractions describe this sample only. The omitted edges discussed later are not hidden in this denominator.

| Edge | Dependency | Source and locating string | Verdict / reason |
|---:|---|---|---|
| 0 | beta0p → beta_m | FLOW: `Fix FIRST β_- := β_0'/2` | CONFIRMED; fixed lower bracket, not the later output β_-. |
| 1 | R0 → R | FLOW: `R := 2R_0` in Lemma F-ind | CONFIRMED. |
| 2 | beta_m → C_rho | FLOW: `then the layer-1 constants C_ρ = C_ρ(β_0'/2, 2R_0) are fixed` | CONFIRMED; explicit order. |
| 4 | C_rho → gamma | FLOW: `then γ := min{γ_0, (β_0'log L/(2C_ρ))^{1/2}}` | CONFIRMED; upper ceiling on γ. |
| 9 | gamma → g1_FLOW | FLOW: `g_1 := (γ^{-2} + R)^{-1/2}` | CONFIRMED; g1_FLOW is a threshold, not the level-1 coupling. |
| 11 | kernel_seq → stage_consts | RLARGE: `stage-k constants also use the kernel coupling g_{k+1}` | CONFIRMED as dependence; its absorbing flag is conditional on unproved Option A. |
| 12 | stage_consts → dbeta | RLARGE: `Derived at level k from data on levels [0, k] only`; `itself an output of stage k (through δβ_k)` | CONFIRMED; the second string is necessary context. |
| 13 | dbeta → eff_seq | RLARGE: `u_{k+1} contains δβ_k` | CONFIRMED. |
| 14 | eff_seq → kernel_seq | RLARGE: `The fixed point is consistent only if the kernel coupling sequence is fixed first` | CONFIRMED as the equality/fixed-point requirement, not its solution. |
| 15 | R → stage_consts | RLARGE: `bounded using only the a-priori bracket` | CONFIRMED as Option A's proposed uniform majorization; not a theorem that FI-1 is solved. |
| 19 | a_p_ac → eps_bg | SF: `ε_bg²(n_1/2 + 1.03κ_sn_K) ≤ ½min{a_p, a_c}` | CONFIRMED; destination is the permitted background ceiling, not the actual background. |
| 20 | tau_c → eps1 | SF: `(TH-ch′) ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}` | CONFIRMED. |
| 21 | C_bg → eps1 | Same SF locating string as edge 20 | CONFIRMED. |
| 22 | eps_bg → eps1 | Same SF locating string as edge 20 | CONFIRMED; ceiling/actual-background distinction prevents a spurious reverse edge. |
| 24 | eps1 → eps_loc | RLARGE, Proposition CL: `ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}` | CONFIRMED. |
| 25 | b_1 → eps_loc | Same RLARGE locating string as edge 24 | CONFIRMED. |
| 26 | kappa_RL → b_1 | RLARGE: `b_1 := n_P + 12κ(1 + A_d(L))²` | CONFIRMED; kernel stiffness κ, not either κ_0. |
| 28 | eps1 → eta_q | HIST, RS-lin: `η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }` | CONFIRMED; linear quietness threshold, not η_1. |
| 31 | eta_q → eps_loc | RLARGE: `ε_loc/2 ≥ (16N + 3)A_dη_q` | CONFIRMED, but this is a **lower** bound on ε_loc in conflict with its prescribed value. |
| 32 | eps1 → a_bad | RLARGE: `a_bad := c_pr·min{ε_1², t_pr²}` | CONFIRMED. |
| 35 | c_flat → c_pr | RLARGE: `c_pr = c_♭/C′², t_pr = C′τ_♭` | CONFIRMED; c_♭ is the SQ price constant, not PROOF's C_♭. |
| 38 | a_bad → a | RLARGE: `a := min{θa_bad, a_A}` | CONFIRMED. |
| 41 | a_A → theta | RLARGE/HW: `If a_A < θa_bad, θ is lowered to a_A/a_bad` | CONFIRMED as the stated order, conditional on a_A having been obtained independently of this θ. |
| 43 | a_ret → theta | PLD: `Without (EG), θ ≤ a_ret/a_bad` | CONFIRMED for the expressly conditional no-EG route; not an identity a_A = a_ret. |
| 45 | theta → g0 | RLARGE: `max{6θ, 24θ}(1 + 2Rg_K²) < 1` | CONFIRMED only with an initial strict θ margin; shrinking g cannot repair 24θ ≥ 1. |
| 48 | c_sf → C_fc | RLARGE: `C_fc = c_sf + 81C_Ae^{θa_bad R}` | CONFIRMED. |
| 53 | theta → lambda_star | RLARGE: `λ_* = 6θ(1 + 2Rg_K²)` | CONFIRMED for the dependency; g-independent use needs the majorant λ_* ≤ 12θ. |
| 55 | lambda_star → C_ell | RLARGE: `C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc` | CONFIRMED; unprimed value. |
| 58 | C_ell → C_ellp | HW, `PRIMED C_ℓ (with C_fc′ = 2C_fc e^{c_f})` | CONFIRMED; primed and unprimed values are distinguished. |
| 60 | c_A → c_plus | HW: `c_+ = c_A + c_U`; graph note points to REVIEW55_HWPLD F4 | CONFIRMED as dependency. The graph explicitly uses F4's no-extra-ring reading; the older ×17 formula is not an unnoticed counterexample to this edge. |
| 62 | c_A → c_U | HW: `node A's C_fc, C_A, a_A, c_A → c_U := 1` | CONFIRMED as order, not functional dependence; input 1 and output 2ε_2 differ. |
| 63 | c_plus → c_f | HW: `c_f := 531441·c_+`; graph's second string locates §35.7 | CONFIRMED as dependency. Current coefficient is C_sh·81; the first locator is superseded, explicitly acknowledged in node metadata. |
| 67 | c_LI → B_0 | HW: `B_0 := B_1 + c + 1`; nearby `allowance c_LI plus the moments' own` | CONFIRMED for this allowance route; later c_LI = 0 does not reverse the edge. |
| 68 | c_f → B_0 | RLARGE: `B_0 = c_LI + c_f + 164ε_♯` | CONFIRMED only with HW's stated replacement of the final term by 1 before the cutoff choice. |
| 70 | c_B → n_H | RLARGE: `n_H := ⌊(4 + c_B)/(aβ_-)⌋` | CONFIRMED. |
| 73 | n_H → n_sharp | RLARGE: `n_♯ ≥ max{n^J_*, n_H}` | CONFIRMED; lower bound on a later integer. |
| 75 | b_D → n_sharp | HW: `n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)}` | CONFIRMED; source's stronger displayed choice suffices. |
| 78 | n_sharp → W | RLARGE: `W := 2n_♯ + 5` | CONFIRMED. This W is not EXISTENCE's weight sum W. |
| 80 | n_sharp → eps_sharp | HW: `ε_♯ := 6400^{n_♯}` in REL-seq | CONFIRMED; ε_♯ is a coupling-dependent expression, later constrained by choosing a coupling ceiling. |
| 84 | eps_sharp → g0 | HW: `g_0(n_♯) with ε_♯ ≤ min{½, 1/164}` | CONFIRMED as admissibility order; not a definition of the bare g_0. |
| 91 | C_ellp → g0 | HW: `REL-boot's r ≤ ½, 164ε′ ≤ 1`; `PRIMED C_ℓ` | CONFIRMED; correct primed consumer. |
| 92 | a → g2_CRC | HW: `g²_CRC := a/(b_n + aR + log(12800C_ℓ))` | CONFIRMED; unprimed C_ℓ here. |
| 98 | a_A → g0 | HW: `holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A)` | CONFIRMED; (S1). |
| 102 | a → g0 | RLARGE: `g_K² < a/(8(3κ_0 + 3))` | CONFIRMED; (P5). |
| 103 | kappa0_CE → g0 | Same RLARGE locating string as edge 102 | CONFIRMED; the CE constant, not level-0 soft coupling κ_0. |
| 110 | eps1 → a_ret | PLD: `a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}` | CONFIRMED for the candidate formula on its chart, conditional on SC. |
| 114 | a_ret → gamma0 | RLARGE: `The γ_0 needed for Cg^{-p}e^{-a_ret/g²} ≤ g⁶` | CONFIRMED; any fixed positive a_ret gives a sufficiently small ceiling. |
| 118 | n_sharp → a_A | HW: `R_{S,E} := ∩_j{every *-component`; §18.1 `(SDP)^A_θ` | CONFIRMED as a **potential family-index dependence**; no numerical n_sharp dependence is proved. |
| 121 | rstar → C_Delta | PROOF: `C_Δ = 2S_*n_1/r_*` | CONFIRMED. |
| 125 | rstar → alpha_star | PROOF: `α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})}` | CONFIRMED; source fixes m strictly below m_cov. |
| 138 | alpha_star → eps_star_N5 | PROOF: `ε_* := α_*/(10p_L(4R_* + 5)L)` | CONFIRMED; N5's ε_*, not EPS-T's. |
| 141 | gamma_prime → c_inf | PROOF: `𝔠_∞ := min{8coth⁴(a/2)` | CONFIRMED; here a is the local RW decay difference, not RLARGE's defect exponent. |
| 145 | r_flat → C_flat_PR | PROOF: `C_♭ := 4S_♭n_1/r_♭` | CONFIRMED; joint-Hessian constant. |
| 147 | eps_star_N5 → eps_br | PROOF: `ε_br := min{ ε_*/(1 + 36p_L𝔠_∞)` | CONFIRMED. |
| 153 | c_inf → C_bg | SF: `C_bg := 1.011√N·max{1 + 48𝔠_∞, 36p_L𝔠_∞}` | CONFIRMED. |
| 155 | eps_br → eps1 | SF: `(TH-ch″) := (TH-ch′) ∧ ε_1 ≤ ε_br/(1.011√N)` | CONFIRMED. |
| 173 | N → eps0_BFT | REVIEW_S22: `depending only on (N, L, κ_±)` | CONFIRMED as the target's quantifier; BFT is not thereby proved. |
| 174 | N → rC_BFT | Same REVIEW_S22 locating string as edge 173 | CONFIRMED as target quantifier. |
| 190 | theta_A → BFT012 | REVIEW_S22: `level-j curvature and soft-fluctuation components are weighted` | NOT-VERIFIED as a source-faithful def edge: this string has no potential-weight clause. REVIEW55_TUNIF W6 expressly says that clause is missing and rejects one proposed literal formulation. A corrected displacement-norm formulation could supply it. |
| 192 | alpha_BFT → BFT012 | REVIEW_S22: same norm paragraph, `curvature is measured in a Hölder (X_c-type) norm`; REVIEW55_TUNIF W2, `α < θ` | CONFIRMED as norm-parameter dependence using context and the node's supplementary source; the isolated edge locator is weak. |
| 194 | eps0_BFT → BFT012 | REVIEW_S22: `there exist ε_0 > 0, r_ℂ ∈ (0, 1]` | CONFIRMED as domain data. |
| 209 | eps0_BFT → eps_N5_unif | REVIEW_S22: `max_P|log V^r_{k,P}| ≤ ε ≤ ε_0` | CONFIRMED as domain containment, with the graph's matching-units qualification. |
| 218 | eps1 → IkE | HIST: `α_E ≥ c·ε_1`; current §25.6, `𝔇_{2ε_1,α_E}(X)` | CONFIRMED dependency. The first locator belongs to the superseded single-gauge formulation; current §25.6 independently preserves dependence on ε_1. |
| 223 | IkE → a_A | RLARGE: `(SDP)^A ⇐ (I_{k-1}^E)''(d'')` | CONFIRMED as a named hypothesis, not a discharged input. |
| 284 | N_prime → a_sh | SF: `a_sh = ρ_band/(16L⁴N′)` | CONFIRMED; the right N′ for deep localization. |
| 285 | sf_chain → a_sh | SF: `R_sh = μ^{-1}ln(r_sol/a_sh)` | CONFIRMED because destination metadata bundles a_sh, R_sh and the neighborhood size; r_sol belongs to the radius chain. |
| 292 | rho_band → g_band | SF: `g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)})` | CONFIRMED; this g_0 is the bare coupling. |
| 293 | N_prime → g_band | Same SF locating string as edge 292 | REFUTED as object identification; N′ is not the denominator's norm data. See §2. |
| 299 | g_star_SF → g0 | REVIEW55_HWPLD: `the threshold must work for every K, in particular K = 1` | CONFIRMED as dependence of the uniform coarsest ceiling on the stage-0 ceiling; the F-3 shift is needed, so this is not equality of the three g_0 symbols. |
| 307 | C4 → Kcompat | EXISTENCE: `48β_b²W²C_4ρ ≤ A_*` | CONFIRMED; a compatibility condition, not an automatically satisfiable later-choice ceiling. |
| 310 | Kcompat → g_3 | EXISTENCE: `(K) is checked once`; `then g ≤ min{g_c, g_3}` | CONFIRMED as conditional order, with feasibility of K still owed. |
| 339 | RLF3dis → C4 | EXISTENCE: `a **prefactor-free** (RLF-3^dis) at g-scaled thresholds` | NOT-VERIFIED with this endpoint: the node's main definition is the fixed-threshold tail with g^{-p_d}; its metadata admits the stronger family is not stated by layer 1. A separate family-uniform tail node is needed. |

## 2. Definite wrong object: edge 293

**REFUTED.** `dag55_2_graph.py`, node `N_prime`, defines

`N′ := N_r·N_μ(|Õ^{1/2}|)`.

SF §16.1, locating `Write N′ := N_r·N_μ(|Õ^{1/2}|)`, uses that product in the deep-localization threshold a_sh. The band window, locating `g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)})`, instead needs N_r and the weighted norm of the **covariance square root** 𝒞. SF's `Lemma GD` defines `𝒞 = Π_UÕ^{-1/2}Π_U`; its positive power Õ^{1/2} appears in the inverse transformation `v = Õ^{1/2}A/(g_0√N)`.

The product N′ cannot replace these two inputs. As an exact algebraic illustration, on a scalar slice take Π = 1 and Õ = t², t > 0: N_r = 1/t, N_μ(|Õ^{1/2}|) = t, hence N′ = 1 for every t, whereas the band denominator's maximum is 2/t. This illustrates the loss of information in the aggregation; it is not offered as a Yang–Mills field counterexample.

Required repair to the graph: separate `N_r`, `N_μ(|𝒞|)`, and `N_μ(|Õ^{1/2}|)`, with their own definition sites and upstream estimates. Merely finding the existing band-window string does not validate edge 293. This error does not itself establish a cycle or a divergent constant.

## 3. Search for missing back-edges

### 3.1 A missing cutoff-family edge does close a return path

**CONFIRMED omission; NOT-VERIFIED cutoff uniformity.** PLD §9.0 defines the input of SC by

`𝒢_x := Σ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S/|S|`.

PLD §9.4 then states SC as

`log⟨e^{Σ_x𝒢_x}⟩_V = Σ_X𝓗^{sea}_X(V)`

with SC2's constants C, Λ, a controlling that expansion. Its definition therefore has a cutoff-indexed family upstream. There is no `n_sharp -> SC_k` edge. SC_k is effectively placed before the cutoff without a cutoff-uniform bound on its constants.

Adding this one edge **as `implicit`, using exactly the author's convention for edges 118–120**, gives the cycle

`n_sharp -> SC_k -> a_A -> a -> n_sharp`.

The last three edges already exist as strict edges 225, 40, 76:

- RLARGE, `(SDP)^A ⇐ ... + (SC)_{k-1}`;
- RLARGE, `a := min{θa_bad, a_A}`;
- HW, `n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)}`.

An in-memory addition passed the supplied schema/string audit and enlarged the cutoff SCC from 12 to 14 nodes, adding SC_k and a_ret. It did not create a third SCC. This is an additional witness of the already-known cutoff-uniformity problem, not an independent obstruction theorem.

The required quantifier is a common bound for the needed family of cutoffs, or a construction that chooses a cutoff satisfying all conditions with its actual cutoff-dependent constants. A statement for each fixed cutoff with constants C(n_♯), a(n_♯) does not suffice. Conversely, dependence of the *input family* on n_♯ does not prove that its optimal constants vary with n_♯: a convergent sum over all sizes could provide uniform majorants. Neither conclusion may be invented.

The existing n_sharp → a_A/C_A/c_A warnings are thus correctly motivated but not a complete inventory of where cutoff uniformity must be established. The truncated sea expansion and its returned-cluster outputs belong in that obligation.

### 3.2 ε_1, ε_0 and r_ℂ: omissions found, no additional strict cycle established

**CONFIRMED for the inspected source ranges; no global completeness claim.**

- SF's actual background comes after ε_1, but graph node `eps_bg` is explicitly the **ceiling** ε_bg^(TH-bg). SF `where ε_bg^{(TH-bg)} is the largest ε_bg allowed` makes the order ceiling → ε_1 legitimate. I do not add the spurious reverse edge by identifying that ceiling with the realized background.
- PROOF `Lemma N5-an♭` gives r_♭, S_♭ depending only on (N,L,κ_±); `Lemma BR1` constructs ε_br from those and the level-0 N5 constants. These ranges supply no ε_1 → r_♭ or ε_1 → C_Δ back-edge.
- REVIEW_S22's BFT quantifier fixes ε_0 and r_ℂ from structural data, and its domain requires ε ≤ ε_0. BFT_A §3.9, `ε_0 := min(ρ_0/(2(1 + G_D)), 1/(16GC(1 + G_D)²))`, makes the analytic inputs explicit. That construction is omitted inside the graph's bundled BFT nodes; it does not supply an ε_1-dependent inverse.
- BFT_B `Proposition BB-3_k` defines its derivative constant by `C_0 := G_0S_1n_se^{mr_s}·3!(2/(r_ℂε_0/(N² - 1)^{1/2}))³`. BFT_B `Corollary BB-4c` similarly uses `ρ_c := r_ℂε_0` and `ρ_c^{-3}` in C_♭^(i). These are missing construction dependencies behind the aggregate target constants. Adding ε_0/r_ℂ → the BFT-3 C_0 creates no return path in the encoded strict graph. Distinguish that derivative bound from BFT_A's regularity C_0 = 2(1+G_D); merging all occurrences and reversing an inequality would manufacture a cycle.
- HIST `Theorem A5`, `Let ε_1 ≤ ½δ_a`, imposes a further upper bound using δ_3, η_AE, C_3, ε_R and C_♮. Its `s_5 := min` fixes the analytic width; §25.6 requires `α_E ≤ s_5/4`. These quantities are not separately represented. The inspected formulas put analytic inputs before ε_1 and α_E; they do not prove a return dependence on ε_1. The original sup-norm A5 is itself not a verified uniform construction; RLARGE §4.1 explicitly requires its corrected norm formulation.
- PLD §9.1's apparent `ε_♮ ≤ r_1(R_*)`, `R_* ∝ n_♯` loop is explicitly an **alternative** called circular; the same section replaces it with the local σ-restricted gas and extraction after averaging. It is not a new live strict cycle.

**NOT-VERIFIED:** that these checks exhaust all constraints. In particular the graph's theorem-sized nodes suppress internal choices; a topological sort of such nodes cannot certify their internal construction order.

### 3.3 FI-1 remains an obligation

**CONFIRMED as a recorded fixed-point problem; NOT-VERIFIED as discharged.** RLARGE §4.4 calls Option A an `integration choice` and says `Neither option is a theorem here`. Fixing a kernel sequence with an a-priori bracket permits bounds uniform over that bracket. It does not establish that the effective sequence equals the chosen kernel sequence. FLOW F-tune proves a conditional tuning statement using the very per-level inputs whose non-circular availability FI-1 questions; its scalar continuity argument cannot simply be relabelled a proof of the missing sequence-level agreement.

The graph's absorbing flag on edge 11 is acceptable as an explicitly conditional bookkeeping choice. It cannot promote U4 to a theorem. The full graph properly retains the FI-1 SCC.

## 4. Checker audit

**CONFIRMED:** the supplied checker reproduces the binding census, SCCs, tagged growth and its seven controls. It was run with `python3 -I -B`, output to stdout only. No graph or output file was changed; the earlier dag55_1 artifacts were preserved.

I independently computed SCCs by exact bitset transitive closure (mutual reachability), rather than implementing another Tarjan traversal. I exhaustively compared all directed graphs on 0–4 labelled vertices, **including self-loops**: 1 + 2 + 16 + 512 + 65536 = **66067 graphs**, zero SCC-partition or cyclic-node disagreements. Every reported nontrivial component also yielded a cycle witness. I checked both actual graph modes, duplicating every edge, and a separate disconnected cycle/self-loop/completed-component case. No algorithmic false negative was found. Inspection of `tarjan`, `nontrivial`, and the independent real-graph result supports the finite graph verdict; the finite tests are not a proof for all possible inputs.

The controls test different things:

| Control | What it actually tests | Limit |
|---|---|---|
| C1 | Injected g0 → eps1 closes a pre-existing strict path | One connected back-edge case; no source-semantic validation. |
| C2 | Propagation from `seeds_override=[kappa_pm]` | Bypasses discovery of growth tags. |
| C3 | Schema rejects a nonexistent endpoint | Appropriate guard; adjacency alone silently drops unknown endpoints. |
| C4 | One acyclic graph with a prescribed order | Positive/null control, not a designed failure. |
| C5 | One three-cycle | Does not itself cover self-loops or disconnected SCCs. |
| C6 | Propagation stops at an `absorbs` flag | Does not prove the mathematical absorption. |
| C7 | A nonexistent locating string is rejected | Does not distinguish a correct formula from a real string attached to the wrong symbols. |

Thus they are seven controls, not seven tests capable of finding the important semantic failures. In-memory adversarial changes gave:

```text
Delete eff_seq -> kernel_seq:
  schema errors 0; string misses 0; all seven controls still pass;
  the FI-1 SCC disappears.
Erase C_fun's growth tags:
  schema errors 0; string misses 0; all seven controls still pass;
  live growth seeds become [V_LF]; g0 is no longer growth-tainted.
Replace an edge's endpoints by g0 -> beta_m, retaining the real FLOW string:
  schema and string audit both pass.
Add g0 -> eps1 as kind implicit with a real existing string:
  schema and string audit pass; B-strict still reports acyclic.
```

These are semantic/completeness blind spots, **not Tarjan bugs**. An omitted edge is unknowable to a checker given only the incomplete edge list. A discarded edge kind is excluded intentionally. `condensed_order` also validates an order of SCCs even when cycles exist; its `validity re-check PASS` alone is not a DAG certificate. `main()` prints failures but does not set a failing exit status, so exit 0 alone proves nothing.

**REFUTED as a literal fulfillment of D5's “every directed cycle”.** `report_cycles` prints `one explicit cycle` per nontrivial SCC, calling `cycle_through`. Independent canonical-start enumeration finds **nine** vertex-simple cycles in the cutoff SCC and **one** in FI-1. The nine edge-index cycles are:

```text
[69,70,73,120,361]
[69,70,73,120,62,61,63,68]
[69,70,73,120,60,63,68]
[71,73,118,40]
[71,73,118,41,39]
[76,118,40]
[76,118,41,39]
[75,120,62,61,66]
[75,120,60,66]
```

FI-1 is `[13,14,11,12]`. One witness per SCC suffices to refute acyclicity; it does not enumerate every cycle. Read the headline's “two cycles” as **two cyclic SCCs** if it is to be correct.

## 5. K and volume inventory

**CONFIRMED for the tags, NOT-VERIFIED as an exhaustive analytic inventory.** Exact rerun:

```text
live growth seeds: C_fun, V_LF
live growth-tainted nodes including seeds: 43
live weak seeds: C4, CEexp, R0, dbeta, eps_N5_unif, sigma_fl
weak seeds individually reaching g0: C4, CEexp, R0, eps_N5_unif, sigma_fl
dbeta individually reaching g0: false
```

C_fun's recorded K-growth is supported by REVIEW_BFT_B_S9_S10, `PROVEN as an implication with a constant that grows like k`, and REVIEW55_BFTB, `Not k-uniform`. Its encoded witness to g0 is the stated BFT5 → a5G → A5 → IkE → C_A path. Lemma TR was not re-reviewed here, as requested; removal of that seed remains conditional on the separate review.

V_LF is explicitly extensive and K-divergent in RLARGE, `the only K-divergent quantity`, and HW, `𝒱_K^{LF}/|T| is not O(e^{-a'/g_K²})`. Its subtraction in NA-∅ is the right algebraic form. That subtraction does not prove the remainder estimate. The unrestricted phrase “nothing grows with volume” is false for the node list; the defensible version is “no other **tagged constant growth** reaches the sink after the stated conditional absorptions.” The target mostly gives this qualification in its body.

The six weak seeds are not all unresolved uniformity. The graph itself contains these **twelve live, untagged entries** whose `vol` contains `unstated`:

`C_rho, stage_consts, c_sf, c_LI, C_p_RLF0, A5, SC_k, LIF, N_prime, CEcond, g_c, MSSob`.

Locators: `dag55_2_graph.py`, the respective node keys and `vol`; `dag55_2_dag.py`, `GROWTH_WEAK` and `propagate`. Some are inherited obligations or have later source remedies, so twelve is **not** a count of twelve independent new gaps. It is a precise demonstration that the checker does not enforce the report's “unstated is its own class” rule on all metadata. SMALLNESS_DAG §5(b) itself admits broader dependence on BFT and node A's unproved hypotheses. I found no justified additional live T-growing constant; absence from a partial annotated census does not prove none exists.

## 6. TC: independent exact derivation

**CONFIRMED** on the requested domain d = 4, L = 3, N ∈ {2,3}, κ ∈ {1,1/4}, and **0 < ε_1 ≤ 2/5** (which contains the live small-threshold regime).

RLARGE, Proposition CL, `n_ℓ := 4L³(L - 1)` and `n_P := 6n_ℓ`, gives

\[
n_\ell=216,\qquad n_P=1296,\qquad A_d=9,\qquad b_1=1296+1200\kappa.
\]

HIST, Lemma PM, `δ_0 := min{1/(640N), 2/N³}`, gives δ_0 = 1/(640N) for these N. Thus 256Nδ_0 = 2/5. Since 256NA_d > 2L², throughout this interval RS-lin's active branch is

\[
\eta_q=\frac{\varepsilon_1}{256NA_d}.
\]

Both possible b_1 values have Nb_1 > 4, so CL's active branch is

\[
\varepsilon_{loc}=\frac{\varepsilon_1}{2\sqrt{Nb_1}}.
\]

HW's TC requires R_TC ≤ 1, where

\[
R_{TC}:=\frac{(16N+3)A_d\eta_q}{\varepsilon_{loc}/2}
=\frac{(16N+3)\sqrt{Nb_1}}{64N},\qquad
R_{TC}^2=\frac{(16N+3)^2 b_1}{4096N}.
\]

The independent calculation formed **squared source quantities first**, then compared rational squares. Integer square roots gave the following rational enclosures; every finite decimal endpoint is an exact rational with denominator 10^6, not floating-point output.

| N | κ | b_1 | Exact R_TC | Exact R_TC² | Rational enclosure for R_TC | Rounded to hundredths |
|---:|---:|---:|---|---|---|---:|
| 2 | 1 | 2496 | 35√78/16 | 47775/128 | [19.319476, 19.319477) | 19.32 |
| 2 | 1/4 | 1596 | 35√798/64 | 488775/2048 | [15.448613, 15.448614) | 15.45 |
| 3 | 1 | 2496 | 51√13/8 | 33813/64 | [22.985389, 22.985390) | 22.99 |
| 3 | 1/4 | 1596 | 51√133/32 | 345933/1024 | [18.380021, 18.380022) | 18.38 |

All four squared ratios exceed 1 exactly. This proves failure without rounding or numerical square-root assumptions. These values also lie inside the original dag55_3 rational square-root enclosures. Its two control values are independently reproduced: the hand threshold gives R_TC = 1; the hypothetical ε_loc = ε_1/4 gives (16N+3)/(32N), namely 35/64 and 17/32.

Execution disclosure: my first scratch calculation used an erroneous expected control identity `(16N+3)/(64N)` and stopped at that assertion after the first physical case. I corrected **my control denominator** to 32N by dividing by ε_1/8, then reran all four cases successfully. The reviewed source was unchanged. No float arithmetic was used in either review calculation. I imported and called the reviewed script's rational `point()` function; I did not use its float-based `disp()` routine.

The cancellation of ε_1 holds on this branch, not for arbitrary ε_1 after δ_0's cap becomes active. The reviewed script checks one rational ε_1; the argument above supplies the interval quantifier. Failure of TC refutes the compatibility of these **prescribed thresholds**, not W-cb's conditional implication or every possible collar construction. Reducing quietness to η ≤ η_q/R_TC repairs this inequality algebraically, but compatibility with the other consumers remains NOT-VERIFIED.

## 7. Can the decade ledgers be retired?

**REFUTED as the universal reason given in headline 8 and §8.3. CONFIRMED only for already-feasible, uniform, one-sided coupling ceilings.**

For fixed finite constants and a fixed positive exponent, constraints such as `C g^{-p} exp(-a/g²) ≤ g⁶` eventually hold as g decreases. Lower bounds on a freely chosen integer cutoff can likewise be met if the constants have already been obtained uniformly in that cutoff. A smaller numerical g_0 is not by itself a failure of an existence theorem. The graph usefully exposes that distinction.

However, three concrete interfaces prevent the claimed generalization:

1. **TC has no feasible value under the prescribed definitions.** It is ε_1-free on the live branch, so lowering ε_1 or g does nothing. The target acknowledges this exception.
2. **EXISTENCE's K is another compatibility window.** At `ρ := (u_+/u'_-)²` the source states ρ ≥ 1 and ρ → 1 as g → 0. Therefore necessary conditions include `48β_b²W²C_4 ≤ A_*` and `16β_aW√C_4 ≤ A_*`. The graph already includes Kcompat but does not verify these conditions. As a logical counterexample to “order implies feasibility,” positive scalar data β_a = β_b = W = C_4 = A_* = 1 fail for every ρ ≥ 1. This is **not** a claim that the actual physical constants take those values. It shows why the source's instruction `(K) is checked once` cannot be replaced by “take g smaller.”
3. **The complex-width interface is absent.** RLARGE §4.1/§4.3, `Until node A chooses one, steps 3 and 5 cannot both use their stated complex domains`, and HIST §25.7, `(I_k^E)''(b'') needs either (RLF-5) at width α_E ... or a second polymer class at width O(g/√κ)`, explicitly leave U2 unresolved. A fixed positive g-independent width cannot be supplied merely by a width proportional to g for all arbitrarily small g. The proposed second class may work, but the graph neither places nor verifies it.

There is also the stronger tail-family demand behind edge 339. SMALLNESS_DAG §8.2 explicitly says it is `not encoded`. A fixed-threshold RLF estimate is not a uniform estimate down to t comparable to g; substituting such thresholds changes a, n_♯ and the subsequent coupling ceilings. A direct moment argument could bypass that route. Until one is supplied, it is an open interface, not a verified free choice in a DAG.

Thus decade-by-decade comparisons may be relegated to diagnostics **after** their role is reduced to a positive, finite, uniform ceiling. A replacement ledger must retain feasibility windows, norm/domain matching, strict positivity margins, FI-1 and cutoff uniformity. There is no basis here for retiring those obligations or for changing the theorem's truth status.

## 8. Provenance and limits

One independent review pass, with adaptive source checks and in-memory exact tests; no source fixes, no git, no commits, no PR actions, no additional written files. The only durable output is this report. The review used the local candidate and its current corrections; no main-branch or repository-retained status was inferred. The review-loop source/claim/checker lenses were applied within the user's narrower output contract; landing and audit machinery were not invoked. Lemma TR, the full BFT proof and the full Yang–Mills construction were not re-reviewed.

Files examined by string-located ranges: SMALLNESS_DAG; dag55_2 graph/checker/output; dag55_3 checker/output; RLARGE, HW, HIST, FLOW, SF, PROOF, PLD, REVIEW_S22, BFT_A, BFT_B, REVIEW55_TUNIF, REVIEW55_HWPLD, and the adjacent EXISTENCE. dag55_1 was retained untouched. Mathematical evidence here is local source analysis, integer/rational calculations and explicitly scoped conditional arguments; no external empirical input or new physical axiom was introduced.

Primary source SHA-256 values recorded during review:

```text
SMALLNESS_DAG.md
18828990921bf3f11e13a55094ed7d6113d8cb8ccf855b61ad03cd866647d2f0
checks/dag55_2_graph.py
2d199d3de1c75ff7713a9918ea5702cb373b67e53b9b06c97e6a90742d517c71
checks/dag55_2_dag.py
e948914882f4e4aad39fd60d0c78abc490db382fcc35ec7e1c63688dbd9a749a
checks/dag55_3_tc.py
1108e45978072266e553d54b32447ad6cd0bdbc0a80633235adcc145e052cfb6
```

## What may be banked

Review completed: 2026-10-29 00:13:04 UTC. The four primary source hashes above were rechecked unchanged. The report's sample table was independently counted: 72 distinct edge IDs, 69 CONFIRMED, 1 REFUTED, 2 NOT-VERIFIED.

- **CONFIRMED:** the exact supplied 358-edge strict graph is a DAG; the full supplied graph has two nontrivial SCCs and ten vertex-simple cycles. The SCC algorithm and graph census reproduce independently.
- **CONFIRMED:** the four TC incompatibility factors, with the exact domain and ratios above. U3 is negative for the prescribed pair of thresholds.
- **CONFIRMED:** the annotated graph has one non-vacuum growth seed reaching g0, and five of six weak seeds reaching it, conditional on the encoded absorptions. These are bookkeeping facts, not uniformity theorems.
- **CONFIRMED:** cutoff independence must cover the sea expansion as well as its node-A consumers; the missing `n_sharp -> SC_k` family edge exhibits an existing return path. This is a quantified proof obligation, not proof that uniform constants cannot exist.
- **NOT-VERIFIED:** source completeness, an unconditional acyclic choice hierarchy, exhaustive K/T uniformity, FI-1, the stronger moment-tail input, and the analytic-width matching.
- **REFUTED:** perfect sampled source fidelity (edge 293), literal enumeration of every cycle by this checker, and the claim that all live feasibility questions disappear by choosing later constants smaller or larger. No constructive 4D Yang–Mills closure may be banked from this DAG.
