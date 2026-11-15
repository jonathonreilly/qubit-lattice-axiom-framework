# Independent review of the source-local connected-support construction

Review completed with one same-context correction. Original frozen source: `962f97c259d8c241df632a07e27f498f4ad33b09`, [RECOVERY_CLUSTER_ASTRA.md](RECOVERY_CLUSTER_ASTRA.md), SHA256 `2c4a9abd12082f756a82ab94999757abd2ebc64950f957ce47ab0a049da2e04f`. Methodology: `ca2bc7ddf64790da96cd43d42017d000fbfe4808`. Separate restricted reviewer context; coordinator requested gpt-6-astra/max. Same-family/fresh-context, not cross-family. No whole-PR, audit, actual Yang–Mills, or T_OS completion verdict.

Pre-stated scope and controls: [review_cluster_01_criteria.md](checks/review_cluster_01_criteria.md). This reviewer writes only this report and checks/review_cluster_*; original source, Git, shared summaries and audit authority remain untouched.

## Incremental finding record

### Cluster-domain-1 — missing sign restriction on the operator weight

First finding, retained as originally raised. Sections 1–2 introduce β without specifying β≥0. Lemma O then uses both `exp(β|union|) ≤ product exp(β|S|)` and weighted `r<1` to infer the unweighted Neumann condition. Both steps require β≥0. On a single vertex with q=1, β=−log4 and E=2, the printed hypotheses give r=b=1/2<1, but the series for (I−E)^(−1/2) diverges and K=−1 is not positive.

Precise narrow correction: declare β≥0 immediately before the norm in §1, with that restriction inherited by Lemma O and analytic composition. Every stated application already uses β>0: fixed CX-R β=μ_0+2, adjustable β=μ_0+2a_c, and both concrete regimes. Thus this is a literal domain defect in the standalone operator statement, not a counterexample to those positive-weight applications. Coordinator notified; same reviewer will confirm any scoped correction.

The following completion record preserves the original finding and adds its disposition and independent evidence.

### Cluster-domain-1 — same-context correction confirmed

The coordinator changed precisely the sentence before the §1 norm to: “Fix **β≥0** for the support norms and operator lemma below.” The complete old/new byte comparison has no other change. Corrected source SHA256: `9c9264bd4d92b60798e48ccd2eb0ff230e221c3ffd2107c0f6443ec86de563cf`. The corrected restriction repairs both inferences and leaves all applications unchanged. The counterexample above is retained as evidence of the original defect. Source-fix provenance is [full_proof_cluster_fix.json](checks/full_proof_cluster_fix.json); this review independently checked the bytes rather than relying on that receipt's pending-status text.

## Final scoped source disposition

**The complete generic construction is mathematically supported under its corrected explicit hypotheses.** In particular the corrected Lemma O, analytic composition bound (C), CX-R, adjustable-rate variant, full-factor implication, and both weak-neighbor and massive-graph sufficient regimes are confirmed. No further material mathematical defect was found in the entire frozen unit. This is a conditional mathematical source confirmation, not a whole-PR landing PASS, a formal audit, an actual Yang–Mills instantiation, or completion of the owner's full T_OS target.

| Claim | Disposition | Scope of confirmation |
|---|---|---|
| §1 original-coordinate support norm | Confirmed | β≥0; connected nonempty supports; fixed product measure; actual original-source dependence included |
| §2 connected inverse square root, both endpoint norms, incidence | Closed after correction | Explicit supplied E atoms and r<1; no inference from spectral positivity alone |
| §2 full Gaussian determinant | Closed after correction | Holomorphic branch determined at E=0; block dimension q included |
| §2 Gaussian congruence | Confirmed conditionally | K complex symmetric, real symmetric on real data; transpose/bilinear form |
| §3 all-order analytic composition | Closed | q scalar coordinates per block, bounded local vertices, A_*<a, uniform support data |
| §4 CX-R and both tree stages | Closed | Product probability reference measure and h≤1/4 at β=μ_0+2 |
| §4 adjustable rate | Closed | a_c>0, μ_0≥0, β=μ_0+2a_c, h≤min(1/4,a_c/2) |
| §4 massive-graph regime | Confirmed | Every fixed m²>0 and bounded degree; constants may deteriorate as m→0 |
| §5 full denominator formula and variation | Confirmed conditionally | Exact identity (ID) and localized nonvanishing prefactors are supplied inputs |
| §5 weak-neighbor sufficient regime | Confirmed | Actual endpoint-local operator entries on a controlled complex domain |
| §6 path/cycle example and numerical constants | Confirmed | Uniform degree-two inequalities; finite scans are corroboration only |
| §7 author checker and logs | Reproduced and sensitivity checked | Exact finite algebra; no general analytic or actual-operator certification |
| §§8–9 original-source ledger | Supported as an obligation ledger | Inspected sources do not supply the listed actual-operator/return construction; no impossibility result or independent wall count |

## Independent derivation of every load-bearing step

### 1. Weighted walk algebra and matrix branches

For each operator atom set `a(x,y,S)=exp(β|S|) sup||E_xy;S||_∞`. Both its outgoing and incoming sums are at most r, and the sum over atoms incident to a fixed source vertex is at most b. A length-n walk has a connected union because neighboring supports share their intermediate endpoint. It reads precisely a subset of that union's original coordinates. With β≥0, its union weight is at most the product of its atom weights.

Summing forward gives the outgoing bound r^n; summing backward gives the incoming bound r^n. To bound all walks whose union contains v, choose one of their steps whose support contains v. For a marked step j, summing the prefix using the **incoming** bound and the suffix using the **outgoing** bound gives `r^(j−1) b r^(n−j)`. Summing j gives `n b r^(n−1)`. Endpoint control alone would not pay source vertices inside connectors; b is exactly the needed extra hypothesis.

An independent coefficient derivation is to solve `(1−t)c(t)^2=1` with c(0)=1 recursively. It gives `c_n=binom(2n,n)/4^n`, positive, and therefore the absolutely convergent functional series gives `(I−E)C²=I`. Summing the outgoing and incoming series, including the singleton identity term, yields

`M=exp(β)+(1−r)^(−1/2)−1`.

Differentiating the scalar series and applying the marked-step bound yields

`B_C=exp(β)+(b/2)(1−r)^(−3/2)`.

The unweighted matrix infinity norm is at most r; hence `I−tE` is invertible on a disk strictly larger than |t|≤1. Define `G(t)=(1/2)Σ_(n≥1) t^n Tr(E^n)/n`. Direct differentiation and Jacobi's determinant formula give

`d/dt [det(I−tE) exp(2G(t))]=0`, with value 1 at t=0.

Thus exp G is the chosen inverse square-root determinant branch, without presupposing a logarithm of the integrated partition function. Each trace term is a closed walk. Its block trace is bounded by q times the product of block norms; marking a support through v gives `q n b r^(n−1)`. The n cancels the logarithm's 1/n, giving exactly `q b/[2(1−r)]`. The q cannot be dropped: the identity q×q block has trace q and induced infinity norm 1.

For symmetric K, every E power and hence C is symmetric. Since C commutes with K, `C^T K C=C²K=I`. For real symmetric E, spectral radius <1 puts all eigenvalues in (−1,1), so K is positive. At complex data this is a bilinear identity; replacing transpose with conjugate transpose is false. The independent q=2 exact computation detects that mutation.

### 2. Source-local analytic substitution and scalar-coordinate counting

For each block x, expand `A_x=σ Σ_(y,S) C_xy;S W_y`. Its vector supremum is bounded by p times the block infinity norm. Thus each scalar component has outgoing majorant A_* and source-incidence majorant B_* before summing component choices. A global spectator σ is a separate uniform parameter; a spatially varying coefficient must enter the support labels.

Write `n_x=q|B_x|≤Q=qs`. Cauchy's estimate gives `|v_(x,α)|≤H a^(−|α|)`. The number of scalar multi-indices of degree n is `binom(n+n_x−1,n_x−1)`, so the unmarked Taylor majorant is `H(1−A_*/a)^(−n_x)≤F(A_*)`. Zero-degree terms remain present and are supported on B_x.

For a **fixed scalar coordinate i**, rather than summing an unexplained block derivative, the marked majorant is

`Σ_α α_i H a^(−|α|) A_*^(|α|−1) = (H/a)(1−A_*/a)^(−n_x−1)`.

If v lies in the base B_x, there are at most d_B choices of x and this costs `d_B exp(βs)F(A_*)`. If v lies in an attached walk, sum the marked starting vertex y first. At most d_B base neighborhoods contain y, there are q scalar choices at y, and summing all marked walks through v costs B_*. The resulting bound is actually

`d_B exp(βs) [q H B_*/a] (1−A_*/a)^(−Q−1)`.

Since q≤Q, it is no larger than the printed `d_B exp(βs) B_*F'(A_*)`. Thus (C) does pay the scalar-coordinate count; no extra factor of q is missing. This coordinatewise derivation is more explicit than the source's “subsum of F′” explanation but requires no correction. Every union consists of the connected base plus walks attached at its vertices, so both field and original-source labels stay connected. A background substituted into a bare coefficient needs its own source-support expansion; analyticity alone is not that expansion.

### 3. First connected-collection expansion

There are finitely many possible supports on each finite Γ. Therefore expanding `exp(−ΣU_S)=Π_S(1+f_S)` is initially a finite algebraic identity, where `f_S=exp(−U_S)−1`. Since `||U_S||≤h≤1/4`,

`||f_S||≤exp(h)||U_S||<2||U_S||`.

Let `q_f=sup_v Σ_(S∋v) exp((μ_0+2a_c)|S|)||f_S||`. In the fixed version a_c=1 and q_f≤2h≤1/2. In the adjustable version q_f≤2h≤a_c. A selected collection of distinct supports has unique overlap components. Disjoint components use disjoint coordinates under the fixed product probability measure, so their expectations multiply. Grouping by union produces exactly a hard-core polymer gas with activities w(P). Larger-than-necessary connector labels may merge components and overcount bounds, but do not invalidate factorization.

For clarity, define `v_S=||f_S|| exp((μ_0+a_c)|S|)`. The exponential generating function for all typed labeled trees with root S is

`T_S = v_S exp(Σ_(S'∩S≠∅) T_(S'))`.

Deleting the root partitions the remaining labeled vertices into an unordered set of rooted branches. The corresponding factorial is exactly 1/(n−1)! in the labeled-tree series. Repeated support types are permitted in this majorant; the actual first-stage collections are distinct, so enlarging to repeated types is harmless.

The vector `B_S=v_S exp(a_c|S|)` is a supersolution because

`Σ_(S'∩S≠∅)B_(S') ≤ |S| q_f ≤ a_c|S|`.

Monotone iteration from zero therefore converges below B. Every connected collection with a chosen root support has at least one spanning tree and occurs in that series with total multiplicity at least one. If its union contains v, some member contains v; choosing one only enlarges the sum. The union weight is at most the product of member weights. Consequently

`sup_v Σ_(P∋v) exp((μ_0+a_c)|P|)|w(P)| ≤ q_f`.

This proves (G) and accounts for the first a_c of entropy loss without an unstated lattice-animal constant or bounded-degree assumption.

### 4. Second connected-graph expansion and zero-freeness

For an ordered polymer tuple, let H be its overlap graph. Give H's edges a strict order. Kruskal's algorithm maps every connected spanning subgraph A to a unique tree τ. For fixed τ, an extra edge e is admissible exactly when its order exceeds the order of every edge on its τ path. If a path edge were later, Kruskal would accept e before that path was complete and would not return τ. Conversely, when every extra edge is later than its whole τ path, those path edges have already joined its endpoints and Kruskal rejects it. Hence all A mapping to τ form precisely the interval `[τ,R(τ)]`. Their alternating sum has magnitude 0 or 1, proving `|φ^T(H)|≤number_of_spanning_trees(H)`.

Apply the same rooted-tree construction with `v_P=|w(P)|exp(μ_0|P|)` and supersolution `v_P exp(a_c|P|)`, using the first-stage bound. In the logarithmic sum the tuples are ordered and have coefficient 1/n!. Marking a polymer whose support contains v costs at most n, leaving 1/(n−1)! exactly. The rooted sum is at most q_f≤2h. Every nonzero connected graph has connected union, and all factors read sources only within that union. This proves the full norm asserted for F, including arbitrary repeated polymer types and arbitrary cluster order.

A quantitative analytic-continuation margin can be supplied directly. Replace U by tU and allow |t|≤5/4. Since |t|h≤5/16 and `exp(x)≤1/(1−x)` for 0≤x<1,

`q_f(t) ≤ |t|exp(|t|h)h ≤ (20/11)h`.

For the adjustable hypothesis this is at most `(10/11)a_c<a_c`; for the fixed version it is at most 5/11<1. Both rooted series therefore converge locally uniformly on a disk larger than |t|≤1. Near t=0 the finite hard-core gas's formal connected-graph identity gives `Z(t)=exp(ΣF_Y(t))`; both sides are holomorphic on the larger disk, so the identity theorem reaches t=1. Nonvanishing follows **after** this identity. No logarithm of Z or desired zero-freeness is used to construct F.

Uniform bounds allow parameter differentiation/integration on compact subdomains, proving holomorphy in z. A global analytic F is supplied by the series even when a separately chosen principal logarithm would have branch cuts. Empty Γ gives Z=1. On disconnected Γ all connected supports lie in individual components, so the construction factorizes. For μ_0>0 a connected support has a unit-edge spanning tree with |Y|−1 edges; the support-size norm therefore pays its actual connector length.

### 5. Full normalization and concrete sufficient domains

The identity (ID) is a genuine independent hypothesis. Given it, the specified logarithms of P and N_χ, the source-local decomposition of S_0, Lemma O's determinant series, and CX-R add to the stated logarithm. The signs are correct. Since β≥μ_0 in every application, the determinant's β norm also bounds its μ_0 norm. Triangle inequality gives (FULL) exactly. Summing a rooted norm over all roots gives at most |Γ| times that norm, and comparing two source points doubles it. Thus the nonlinear term has variation at most `4h|Γ|`, while the determinant contributes at most `q b|Γ|/(1−r)` and the other factors have their separate displayed budgets. At h=0 they do not disappear. A linear action term erased from a remainder definition must reappear in (ID) or be removed at an actual exact critical point. No contour or history identification is supplied by the algebraic Gaussian congruence.

For the weak-neighbor class each row has at most Δ atoms of weight `ε exp(2β)`, and each vertex is in at most 2Δ oriented edge atoms; this gives the displayed r,b bounds uniformly under deletion of vertices. Symmetry is transpose symmetry on the complex domain. Small σ_*p makes A_*<a, and choosing H small then makes h_loc small; no actual Yang–Mills matrix is identified by this example.

For `K=m²I+L_G`, `c=m²+Δ` and the stated diagonal/edge E satisfy `K=c(I−E)` exactly. At v of degree d_v,

`r_v=[(Δ−d_v)exp(β)+d_v exp(2β)]/c ≤ Δ exp(2β)/c`,

and the support-incidence sum is

`b_v=[(Δ−d_v)exp(β)+2d_v exp(2β)]/c ≤ 2Δ exp(2β)/c`.

Any `0<β<(1/2)log(1+m²/Δ)` therefore suffices. Taking μ_0=β/2 and a_c=β/4 gives β=μ_0+2a_c and the printed h≤min(1/4,β/8). The normalization contributes `−(|Γ|/2)log c` and C gains c^(−1/2). The Δ=0 case is diagonal, including isolated vertices and the empty graph. No uniform m→0 estimate follows.

For the degree-two explicit example, `e=1+Σ_(n≥1)1/n!<3`, since `n!≥2^(n−1)` with strict inequality at some n. Thus exp(3)<27 and exp(6)<729. The printed r<1/8 and b<1/4 follow. For u=8/7>1, `sqrt(u)≤u` and `u^(3/2)≤u²`, so the quoted bounds on (1−r)^(−1/2) and (1−r)^(−3/2) are conservative and valid. Both M and B_C are <28, giving A_*,B_*<1/4. With Q=s=d_B=1,

`h_loc < (27/1024)[4/3+(1/4)(16/9)] = 3/64`,

so the F norm is <3/32. The determinant bound is `<(1/4)/(2·7/8)=1/7`. These are uniform degree-based proofs, not extrapolations from the finite path scan.

## Executed evidence and controls

[review_cluster_01.py](checks/review_cluster_01.py) uses an independent implementation and exact rational/Gaussian-rational arithmetic under Python 3.12.8 and SymPy 1.14.0. It exits 0 with empty stderr. Its 17 named checks and 11 explicit mutation/edge controls all passed. Full output is [review_cluster_01_out.json](checks/review_cluster_01_out.json).

- Exhaustive simple host graphs through five vertices: 1,099 graphs, 772 connected hosts, and 16,272 Kruskal tree intervals checked under forward and reverse edge orders. The comparison spanning-tree count uses the Laplacian cofactor determinant, while the alternating connected-subgraph sum uses direct subsets.
- Rooted-tree coefficients through five vertices agree between implicit exponential-series recursion and 132,308 direct typed Prüfer-tree assignments, including the factorial normalization.
- A three-site biased product-spin model with complex rational coefficients has 30 partition monomials. Direct spin summation and independent moment/connected-support grouping agree. Differential-recurrence logarithm coefficients and the full Ursell multiset expansion agree on all 165 monomials through degree five. Clusters of size five and 193 repeated-type contributions are exercised, extending beyond the author's one-/two-polymer truncation.
- A q=2 block model with an actual long connector verifies both endpoint and support-incidence bounds through six steps, with envelope r=7/250 and b=9/125. The inverse-square-root coefficients are independently recovered through degree ten. Complex symmetric bilinear congruence and characteristic-polynomial versus trace logarithm agree through degree five; substituting a Hermitian transpose fails.
- Scalar Taylor counts are exhaustively enumerated for Q=1,2,4,6 and degrees zero through eight; omitting q is detected. The massive-graph formula is checked on 76 graphs through four vertices, including empty, disconnected, and diagonal cases.
- The negative-β counterexample is checked explicitly and retained, despite the source repair.

The [author-controls driver](checks/review_cluster_author_controls.py) reconstructs the exact author script from the frozen Git object into reviewer-owned evidence paths. Its unmodified replay has byte-identical stdout and exits 0. Six separately saved mutants exit 1 at the intended gates: determinant half-factor, trace sign, long connector, source coefficient target, row majorant, and missing self-polymer term. Their failed outputs remain on disk; [review_cluster_author_controls_out.json](checks/review_cluster_author_controls_out.json) records each script hash, exact mutation, failed predicate and exit code. These are intentional negative controls, not hidden failed science runs. No unintentional execution failure or unresolved control failure occurred.

The author checker remains finite evidence. It does not itself validate the general tree majorants, scalar-coordinate analytic bound, arbitrary complex domains, or actual Yang–Mills inputs. Those mathematical implications were assessed by the complete derivations above. The finite tests do not establish cutoff, scale, infinite-volume, massless, or continuum limits.

## Actual Yang–Mills hypotheses that remain separate

The following are producer obligations, with possible overlap; this list does not claim pairwise independence or an impossibility theorem.

1. **Identify the actual one-step action and operator.** [STEP55 §3.1](STEP55.md) includes the centered soft-kernel normalizer in S_eff. [PROOF's N5-sf_i](PROOF.md) explicitly uses a Hessian of a minimum-defined E_i^NA and qualifies the critical-branch result. [B2_55 J7](B2_55.md) separately identifies the critical-value/minimum-action bridge. The operator used in the actual density must be matched, or the whole construction must be derived for the critical-value action without silently changing the consumer.
2. **Construct original-source operator atoms with both endpoint and incidence bounds.** The complete [PROOF Theorem RW](PROOF.md) gives kernel/walk bounds from RW1/RW2 and geometric support only under its finite-range condition. Its dependence on entries of K is not an all-order expansion of those entries in the original varied coefficient field after background substitution. A source-local resolvent/parametrix construction could discharge this obligation without the near-identity Lemma O, provided it proves the same C bounds and treats logdet separately.
3. **Localize every substituted coefficient, gauge/slice map, bare interaction and inherited activity.** [BFT34_55 §1.2](BFT34_55.md) states a weighted first-derivative consequence from explicit hypotheses; its §2.2 distinguishes this from all-order support summability. [SRC2_55 E11](SRC2_55.md) explicitly leaves strict relocalization inside its representation input. A nonlocal slice basis does not become a vertex-local product reference measure merely because its coordinate Gaussian is a product.
4. **Supply a uniform complex domain for the actual choices.** [PROOF N5-sf0](PROOF.md) chooses chart and torus thresholds using R_*. Enlarging the compression scale requires new matching thresholds or another compression argument. [STEP55 Lemma NZ](STEP55.md) is uniform for real t>0 and complex fields; it does not provide uniform holomorphy/zero-freeness for an independently varied complex local coupling.
5. **Establish the full actual return identity.** The proposed history-dependent return denominator must equal (ID) with matching collars, cut indicators, contour, product coordinates, gauge Jacobian, reference normalization, and all linear/main/determinant terms. [STEP55 §5.4 and S9](STEP55.md) assume the relevant identification and then restore factors; [CODEX_REVIEW_STEP R11](CODEX_REVIEW_STEP.md) gives the actual normalization diagnostic. Single-kernel zero-freeness and a conditional cluster identity do not perform this identification.
6. **Prove the induction and history/source bounds needed downstream.** [SRC2_55 §3.5](SRC2_55.md) makes its exact bookkeeping conditional on a stepwise factorization and separately lists closure and flow bounds. The frozen/top decomposition still needs V-independent frozen terms and a uniformly bounded top remainder at every required V, with actual return/large-field estimates. A smaller large-field producer estimate cannot be replaced by a hypothesis already asserting the whole representation.

This reviewer did not read or use the evolving SOURCE_LOCAL_RETURN_ASTRA.md. Later constructions elsewhere in the active branch are neither certified nor rejected by this frozen-unit report. No claim is made that these obligations are unsolvable or that all possible routes have been exhausted.

## Review lenses, boundaries, and execution receipt

- Code / Runner: finite evidence reproduced; independent algebra and six actual failing mutants recorded. General proof confirmation comes from the derivation, not from PASS text.
- Physics Claim Boundary: conditional mathematical support only; actual T_OS remains outside this unit's proved conclusion.
- Proof Obligations: **CLOSED for the corrected generic implication; CONDITIONAL for (FULL) on (ID) and the specified prefactor data; actual Yang–Mills application unestablished by this unit.**
- Imports / Support: no empirical inputs or fits. Product measure, operator atoms, complex-domain bounds, local vertices, exact denominator identity and prefactor decompositions are explicit mathematical hypotheses. The examples are supplied model instances. No registered physical primitive is used as a substitute for them.
- Nature Retention: no Nature-readiness or retained-status determination.
- No-Go Discipline: scope inspected against the current-main skill. The original-domain counterexample rejects one literal implication and is repaired by a stated hypothesis; §§8–9 give source coverage and remaining tasks. No global no-go, route-exhaustion, independent-wall count, or five-family packet PASS is claimed.
- Labeling Convention: the result is an algebraic/analytic implication, not a convention theorem.
- Repo Governance / Audit Compatibility: reviewer-owned files only; no verdict/status authority, source-edit by this reviewer, PR action or Git mutation. Source-fix authorship belongs to the coordinator. Whole-PR packaging, source-preservation, combined pipeline, strict lint, changed-evidence and landing gates belong to the coordinator and were not run by this restricted reviewer.

One coherent scientific review and one affected-domain-fix confirmation were performed. Material findings: one, now corrected and confirmed; unresolved mathematical findings in this generic unit: zero. Commits and pushes by this reviewer: zero. Full pipeline executions: zero. No formal-verification certificate is claimed. The exact source hashes, read ranges, evidence hashes, and corrected-source binding are recorded in [review_cluster_receipt.json](checks/review_cluster_receipt.json). This same reviewer context remains available for further scoped fixes or genuinely changed inputs.
