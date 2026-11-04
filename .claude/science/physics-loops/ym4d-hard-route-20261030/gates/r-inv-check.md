lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T02:48Z

# Check of `library/r-inv.md` (row 242)

Status: complete.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, branch `claude/ym4d-hard-route` at `a6369e61b`. Checks `library/r-inv.md` (Codex) line by line. One reading by one other model; not an audit. Sussman–Alpoge `YM4_sketch_500.tex` at `31a47c543775` (SA below), fetched by URL to a scratch folder (sha1 `107abaef1a08…`, 32992 lines). Balaban CMP 119 read from `~/ym4d-papers/cmp119.txt`. No numerics were run; every step below is by hand.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the operation **R**, the frame sum, the healing formula, the hard-core gas and the insertion age. T. Balaban (CMP 119, (2.32)–(2.33); CMP 122) for the partition-preserving covariance of R-terms and the frame-averaged trees. Codex for `r-inv.md`.

Kind of result (FINISH item 9): check of our own new text. The outline requires the invariance and does not prove it (SA 7581: "Both symmetries are part of the definition of 'renormalised'"; SA 20646: "The actual domain and naturality hypotheses remain part of closure"). Balaban states the covariance and defers its proof (CMP 119 p. 260: "will follow immediately from the construction of the R-terms given in the next paper").

## Verdicts, §§1–3

| Step of `r-inv.md` | Verdict |
|---|---|
| §1 (1): T_{D_H} = T_H − \|G\|^{-1} Σ_g T_H(g^{-1}P) | ADVANCE. Sum (INS) over X and reindex X ↦ gX. Invariant totals give zero. |
| §1 sources: SA 7581, SA 16057–16067 (WF10), CMP 119 (2.32)–(2.33) | CORRECT. Quotes match. Balaban's covariance is for "Euclidean transformations r, which leave the partition of the lattice ... in MR_j-cubes invariant", the same restriction as (R-inv). |
| §2: (N), (T), (F) are natural with grids and frames carried | ADVANCE. (N): the least box with faces in the carried F_i containing D_{i-1}+[−m_i,m_i]^4 is unique and maps to its image. (T): ⟨Ox+t, Ore_i⟩ = ⟨x, re_i⟩ + ⟨t, Ore_i⟩, so the frame-lexicographic order is carried. (F): equal weights on a carried set of minimal unions. |
| §2 (2): s \| L^{m+1−j} for every formation grid side | ADVANCE, via `ti-2.md` Lemma 3, which I redid. Ř_i is the least L-power ≥ (log min_{u≤i} x_u)^r (SA 17334). M is an L-power. The test-cube side M_2Ř_t has M_2 an L-power with L²M_2 ≤ M (SA 17334). Lemma 3(a) gives Ř_i ≤ L^{j−i}Ř_j. So in level-i units every side is an L-power at most MŘ_i ≤ L^{j−i}·MŘ_j ≤ L^{m+1−i}, which also covers sides finer than one level-j unit. Signed permutations about the origin fix centred partitions of odd side. Precision: SA says the test cube has side "of order" M_2Ř_t. Lemma 3 reads it as exactly M_2Ř_t on a centred grid. That is a formation choice; it is natural. |
| §3 (3): T_{H̄,L̄}(ι W) = T_{H,L}(W)^{-1} | ADVANCE. With q = q(W), θ(ιW) = θ(W) because ιW is conjugate to W^{-1}. So q̄(ιW) = L^{-1}q^{-1}L, and ιW·q̄(ιW)·L̄ = L^{-1}q^{-1}W^{-1} = (WqL)^{-1}. Also H̄ = −Ad(L^{-1})H is the principal log of B̄L̄^{-1} = L^{-1}(BL^{-1})^{-1}L, valid for small H. |
| §3: ι preserves Haar measure; ι_{H̄,L̄}∘ι_{H,L} = id | ADVANCE. In W = cos u + i sin u n·σ, ι is (u, n) ↦ (u, −R_{g(u)}n) with g(u) = (q(u)L)^{-1} and R_g ∈ SO(3). For fixed u this is orthogonal on S², so Fubini keeps sin²u du dΩ. I redid the double application; it returns W. |
| §3 (4): J_{H̄,L̄}(ιW) = J_{H,L}(W) | ADVANCE. I also checked it on the explicit Jacobian of `s210.md` (7), J = 1 − X_Hθ. With W' = ιW, θ(W'e^{isH̄}) = θ(e^{isH}q^{-1}Wq) = θ(We^{isH}). So X_{H̄}θ(ιW) = X_Hθ(W). |
| §3: θ = 0 and θ = 1 give the unshifted and fully shifted charts | CORRECT. At θ = 0, ιW = B^{-1}W^{-1}B. That is the (F2) reversal Ā = −Ad(B^{-1})A. At θ = 1, T(W) = WL. |

## Verdicts, §§4–7

For each rule I read the SA lines that define it, and the adopted note where SA leaves a choice. A rule is natural when it is built from regions, grid cubes, distances, outcomes, unique solutions of transported problems, or the block-axial (contour) condition. A comb tree or a coordinate order outside the frame sum would break it. I found none outside the frame sum: SA's trees, box axial gauges and tree constraints all sit in steps (3), (4) after the frame sum (SA 17585, 7185 "Trees depend on the choice of a frame in W_4, and averaging over the 2^4 4! frames restores the symmetry"). The stage tests take a block-axial representative, and "every such element gives the same tested number" (SA 17317).

| Step of `r-inv.md` | Verdict |
|---|---|
| §4 block average, A1 orbit, Ax° slice, localized determining sets | ADVANCE. `ti-2.md` Lemma 1 (checked by Codex, row 212). For a localized problem the lift is natural: 1 inside blocks and V(c) on the bonds from block c_− into block c_+ (SA 9783). The representative is block axial, and V^bg "does not depend on which such U is chosen" (SA 9783). Precision: in the large-field box the uniqueness input is Proposition 2.4 (`ref-chart.md` Theorem 2.4), not A1. Its continuation class is defined by plaquettes within distance 1 of Λ^pr, so it is invariant. |
| §4 tower assignment by (A7) | ADVANCE. (A7) is stated for translations preserving π_p and for symmetries about a common centre. Its proof uses only aligned cubes of L-power sides dividing M, and d_∞. So it is natural with the grids carried. For a ∈ 𝔊^{(m+1)}: M ≤ MŘ_j ≤ L^{m+1−j}, so π_p is preserved. |
| §4 reversal V = e^{iA}B ↦ −Ad(B^{-1})A | ADVANCE. The Haar density σ_H(A) depends on \|A\| only. |
| §4 stage thresholds | CORRECT, with one precision. The thresholds also depend on region membership: e = (j−l−1)_+ on Ω_l∖Ω_{l+1}, c_l = 3 next to Ω_k at the last stage, and the overlap factor L_♭^{2(i−k_♯−1)_+} (SA 17624). These are geometric data too, so the claim stands. |
| §4 extension test (2), totality, hulls, collars, boxing, eligibility, (N) nest | ADVANCE. Eligibility is single boxes and size, quiet (no creation, no joining) and quarantine (SA 17575). |
| §4 (L0)–(L4) | ADVANCE. (L0): the pivot b_0(c) is the middle bond, so it maps to the middle bond of the image coarse bond. On the reversed bond, M(V)(c̄) = M(V)(c)^{-1} (`ti-2.md` §1). The chart Σ_c^h is defined by a bi-invariant distance, so it is reversal invariant. Uniqueness in Lemma G then inverts the pivot. Its value off the chart is 1 = 1^{-1}. (L1)–(L4) as written. |
| §4 Gaussian operations, carrier series, kept/rejected split | ADVANCE. Coordinates change by an orthogonal linear map. Hessians, Schur complements and inverses are conjugated by it. SA's retention rule reads only connectedness and one layer of Ω∩Z (SA 17550). |
| §5 (5) f_{c',r'}^{-1}a = f_{c,r}^{-1} | ADVANCE. r'^{-1}(ax − ac) = r^{-1}O^{-1}O(x−c). |
| §5 healing gauge u^g transports exactly | ADVANCE, as an adopted prescription. Gauges are site functions, so (a·u)(ax) = u(x), and a·(u·U) = (a·u)·(a·U). The index set {y} is carried. So the quaternion sum, its determinant and the branch of SA 17667 agree at corresponding sites. Precision: SA 17585 names only "the reference law with its denominator, the two trees, the test on B, and the last-shell test". The healing gauge is not among them. The sentence "This includes … the subsequent healing construction" reads more into SA than it says. The frame formation of û_y, χ_y is our choice. The Result says so correctly ("the transported healing choices of §5"). The choice is available: healed components have passed every test, so they carry T'_k(X) with its frame sum (SA 17642–17654). |
| §5 trees, tree constraints, last-shell test, reference law, cut-off φ_X | ADVANCE, under the same prescription: every object of SA (3), (4) is formed in coordinates f_{c,r}. A fixed rule in normalized coordinates can satisfy SA's requirements (one initial site, stability, the entrance bonds). Pushing a valid tree forward by an isometry gives a valid tree. |
| §5 drop-outs before the tree gauge have no frame; later summands keep theirs | CORRECT (SA 17585, 17654). |
| §6 (6) kernels, histories, inner islands | ADVANCE. Tests by indicators. Draws (frame, tree gauge, reference law) by the bijection r ↦ Or and the transported laws. Integrations by the changes of variables of §3–§4. Passengers are carried unchanged. The bare measure with constant scalar sources is invariant. |
| §6 erasure, hard-core gas, completed action | ADVANCE, with precision P1 below. |
| §6 (7) and the logarithm | ADVANCE. The dial argument gives a unique formal logarithm. Transport bijects connected clusters with their coefficients. Equivalently: on the normal-convergence domain, the gas over its empty family is a natural function near 1, so its principal logarithm is natural. |
| §6 never-large label; no boundary part | CORRECT. SA 17995–17996: "The part with no standing object in its domain agrees with the term formed at the never-large label and enters R^{(k)}". At that label nothing stands. |
| §6 regular inputs (re-pointed families) | ADVANCE. For Ḡ = \|𝔊\|^{-1}Σ_g g_*G, transport with the group conjugated gives Ḡ_{a𝒟}(aX, aP, az) = \|𝔊\|^{-1}Σ_g G_{a𝒟}(ag^{-1}X, ag^{-1}P, ag^{-1}z) = Ḡ_𝒟(X,P,z) when G is natural. For a ∈ 𝔊^{(m+1)} ⊂ 𝔊^{(i)}, i ≤ j, it is simpler: Ḡ is exactly 𝔊^{(i)}-covariant, polymer by polymer. |
| §6 young-remainder interpolation, vacuum subtraction, Wilson counterterms, induction | ADVANCE. At s = 0 the young terms are off. So E^{(j+1)} reads only old (inserted) R-terms, and R^{(j+1)} reads young ones only through totals inside ⟨·⟩_{s,t=0} (SA 17548). The induction over production levels has no same-level edge. Each level reads only families of earlier levels. |
| §6 complex continuation, independent currents, (DOM) kept | CORRECT. The real pair slice is a maximal totally real set, so identity on it extends to each connected domain where both sides are holomorphic. |
| §7 (R-inv) from (NAT) | ADVANCE. a ∈ 𝔊^{(m+1)} fixes every formation grid by (2). It fixes every block lattice of level ≤ m+1, since the origin is a site of every level. It normalizes each 𝔊^{(i)}, i ≤ m+1. It fixes constant sources and the scalar frame θ. The frame sum absorbs r ↦ Or. So a𝒟 = 𝒟. |
| §7 T_{D_H} = 0; vacuum subtraction | ADVANCE. a·1 = 1. |
| §7 (8): β_k = 0, d_k = 0, N_k(D) = 0 for every K | ADVANCE for complete list totals at the invariant regular specialization, which is what D1 of `gates/b4-ind-check.md` reads. With no defect in the presentation, the bracket F(S_sym + D) − F(S_sym) has D = 0. No other defect enters at constant sources. |

## Precisions (none breaks a statement)

**P1. The induction must carry polymer values, not only totals (§6).** (NAT) is stated for totals T_H. But the step reads earlier families term by term in two places. First, the completion fills each slot that disappears with "the term formed from the history with the whole treated cluster erased" (SA 17959–17965). Second, label actions sum members only over small-field domains. So a totals-only hypothesis does not give the completed action. With the polymer form

  F_{a𝒟}(aX, a·P) = F_𝒟(X, P) for every earlier family F (regular, remainder, boundary) and every domain X,  (NAT-p)

the step closes. §§2–5 prove (NAT-p), because every rule they transport is natural. One gap in the list: "Exact localization preserves these complete differences" names no rules. The localization rules the completed action reads are: SA (R10)–(R12) Möbius localization with the base as anchor (`loc-3.md` Lemma M); the decoupled response (R9), a unique solution; the regional-logarithm sums over sub-regions with block-axial top averages (`d3-local.md`, `regional-gauss.md` §3); the inverse-root walk series; the cluster expansion of (1d), which is (UM2)–(UM3) (SA 14318–14362); Definition A; (F); Lemma R. I read each. (UM2) is a Mayer sum over all selections D and failed-bond sets P_0. (UM3) has one decoupling parameter per coarse cube, and its polymers are wall-connected coarse domains. So neither depends on an ordering of cubes. Each is built from grid cubes, domains, walks, unique solutions and the block-axial condition, and none uses a coordinate order or a comb tree. So (NAT-p) holds as an implication from the same premises. **Repair (text only):** state (NAT) as (NAT-p) and add these rules to §4.

**P2. The result is stronger than stated (§7).** For a ∈ 𝔊^{(m+1)}, (NAT-p) with a𝒟 = 𝒟 gives H(aX, a·P) = H(X, P) for each domain X. Then g_*H = H for every g in the group, so 𝓡_{m+1}H = H and D_H = 0 term by term, not only in total. So the last caveat of §7, "Restricted domain sums still require their prescribed boundary pieces", is not needed. Plain insertion and (INS) give the same family, and restricted sums at labels need no new boundary piece. The totals-only statement in the note is true but understates what its proof gives. This term-by-term form is Balaban's (2.32). SA claims less: "An individual R^{(j)}(X,·) is covariant under the translations that preserve the MŘ_j-cubes", and covariance under all isometries only for totals (SA 7477). So the term-by-term form is a property of our adopted specification, (N) included. It does not hold for every rule that SA's bounds allow (`ti-cov.md` (4)).

**P3. Scope of the adopted data.** (NAT) is proved for the construction with our adopted formation data: (N), (T), (F), Definition A with (A7), the half-cell profile, Definition D, [RED], the carrier series, Definition R, and §5's frame formation of û_y and χ_y. SA leaves these to "the formation data" (SA 6052–6070: "Listing the names of tests does not define them"). So the theorem is about our specification. It is not about every specification SA's words allow. A specification that forms û_y in fixed lattice coordinates outside the frame (allowed by SA 17664's "there are local gauges") would not give the transport identity of §5.

**P4. Premises the note keeps, correctly.** Existence and uniqueness inputs (A1, Proposition 2.4, Lemma G, SA Theorem 6(c), (R9)), existence and bounds of the local gauges, (DOM) for physical reads, and admission (D4). The transport identities need these only where the objects are defined. "Undefined objects remain undefined" is right, because every defining problem is carried bijectively.

## Kill attempt

Before confirming, I looked for one rule outside the frame sum that reads a fixed coordinate order: a comb tree, a lexicographic tie-break, a "first" bond, or a fixed axial gauge. I searched SA's large-field section, L17259–18300, for these words and read every hit. There are six. Two are block-axial representatives, which are natural: the stage tests (SA 17317) and the rarity remark (SA 17709). One is the frame-r tree of step (3) (SA 17598). Three are proof devices, not constructions: the axial gauge that shows test (2) has an extension (SA 17585), the axial-gauge Hessian bound in Proposition 2.4 (SA 17656), and the comb gauge in a curvature estimate (SA 18216). The pivot rule, Lemma G's chart and the strip cut-off are natural too, by §3 and (L0). No candidate defect survived.

## Result

**Check of our own new text (`r-inv.md`, Codex): checked line by line by Claude, first failing step none.** Every step of §§1–7 ADVANCES as an implication, or is CORRECT, from the named premises.

- (1), (2), (3), (4) and (5) are redone above and hold. That includes the Haar-measure and Jacobian identities for the reversed strip map.
- (NAT) holds for every remainder that (INS) inserts, at constant scalar sources, under (N), (T), (F), SA's frame sum and §5's frame formation of the healing choices. With P1's repair, the induction carries the polymer form (NAT-p).
- (R-inv) follows for every a ∈ 𝔊^{(m+1)}. Every (INS) defect has zero total. The bracket is β_k = 0, and the defect budget d_k = N_k(D) = 0 for every run length. This closes D1 of `gates/b4-ind-check.md` for constant sources, by repair (a). By P2, D_H = 0 term by term, so restricted sums need no extra boundary piece.

**What this does not show.** It gives no admission (D4), no (DOM), no existence of the local gauges, and no nonconstant-source closure (D2 of `b4-ind-check.md`; `src-array.md`, row 241). It does not cover any specification of the formation data other than ours (P3).

**Evidence for the owner of `r-inv.md` (not edited here).** Restate (NAT) as (NAT-p), list the localization rules of P1 in §4, and replace the restricted-sum caveat of §7 by P2. Also: §5's "This includes … the subsequent healing construction" should say the healing choices are formed in the frame by our prescription. SA 17585 does not list them.
