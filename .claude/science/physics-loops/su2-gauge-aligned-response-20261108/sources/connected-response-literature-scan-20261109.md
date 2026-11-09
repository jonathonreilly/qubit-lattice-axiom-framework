# Connected-response literature scan (2026-11-09)

Scope: mathematical suppliers for a volume-uniform connected fourth cumulant \(\kappa_4(F,G,A_c,A_d)\) in the actual two-step compact SU(2) hidden chain \(q_u(U_0)K_{\kappa u}(U_1|U_0)K_{\kappa u}(I|U_1)\), with two fixed smooth gauge-invariant fine sources and distinct terminal boundary scores. This is a literature extraction, not a theorem verification. No intermediate Wilson law is substituted. No numerical jobs were run.

## Search and execution record

Read `docs/ai_methodology/SCIENCE_WORKFLOW.md`, the pack `GOAL.md`, `HANDOFF.md`, and `SOURCE_MAP.md`; no proof notes or raw ledger were opened. `python scripts/lab_ops.py preflight` could not start because `python` is absent. Retried the same preflight with `python3`: it passed (`preflight: go`), with notes that no target model floor was checked and `ulimit` was unavailable. No campaign or numeric job was started.

Queries (web search, 2026-11-09):
- “continuous spin systems low temperature cluster expansion unique nondegenerate ground state cumulant decay theorem paper”
- “Dobrushin Shlosman complete analyticity cumulant bounds smooth observables uniformly convex finite range measure theorem primary paper”
- “Brydges Kennedy forest formula cumulants decay cluster expansion continuous spin low temperature massive gaussian small field large field theorem”
- “Yang Mills lattice weak coupling cluster expansion interfaces rough islands normalized insertions compact group”
- “Helffer Sjostrand covariance decay log concave measure theorem finite range interaction”
- “Menz Otto uniform logarithmic Sobolev covariance decay finite range interactions theorem”

The existing `SOURCE_MAP.md` locators (Brydges–Guadagni–Mitter finite-range Gaussian decomposition, Bałaban, Rebeschini–van Handel) were not simply repeated as matches. Search did not find a theorem explicitly formulated for this compact SU(2) two-step hidden posterior with all layer normalizers retained and mixed four-point response. The closest actual-law route found is an adaptation target, not a matching theorem.

## Closest primary results and proof windows

### 1. Bricmont–Lebowitz–Pfister, “Low Temperature Expansion for Continuous-Spin Ising Models” (1980)

Primary author manuscript: [ResearchGate-hosted author upload](https://www.researchgate.net/publication/225996466_Low_temperature_expansion_for_continuous-spin_Ising_models); journal record/DOI: [Communications in Mathematical Physics 78 (1980), 117–135](https://link.springer.com/article/10.1007/BF01941973), DOI 10.1007/BF01941973.

**Read scope:** full text was opened through the author-upload page; theorem/proof passages inspected include the abstract/introduction (printed pp. 117–119), the exponential-clustering argument (printed pp. 126–127, equations around (30)–(31)), and the contour-expansion discussion in the proof of Theorem 2 (printed pp. 132–134). The HTML/OCR obscures some formulas; exact theorem hypotheses should be checked from the PDF before reliance.

**Statement window:** abstract, printed p.117: general ferromagnetic finite-range spin systems with an even compactly supported single-site measure on \(\mathbb R\), under additional mild conditions, have an asymptotic low-temperature expansion for free energy and correlations, exponential clustering in pure phases, and analyticity for sufficiently large real part of inverse temperature. Printed pp.126–127 derive clustering by representing the truncated correlation as a sum over polymers/graphs joining the supports, with the exponential rate arising from a minimal connecting graph and a low-temperature activity estimate. The proof of Theorem 2, printed pp.132–134, uses a three-region decomposition: shrinking neighborhoods of the ± ground states and an intermediate region handled by a high-temperature expansion.

**Why close:** it does more than bound bad-event probabilities: it controls normalized pure-phase correlation functions by connected contour/polymer expansions, and its three-region scheme explicitly integrates a middle/rough region. This is the strongest potential methodological supplier found for retaining normalized insertions while summing rare rough islands.

**Mismatch:** scalar real spins, ferromagnetic Ising symmetry with two phases, prescribed pure-phase selection and reflection-positivity structure; no compact non-Abelian gauge redundancy, no rooted forest quotient, no two-layer hidden posterior with layer-dependent conditional normalizers, and no mixed fourth cumulant of two original sources and two boundary scores. Its clustering theorem cannot be transferred without reconstructing its contour/phase decomposition for this actual law. Full proof is accessible via author upload, but scan/OCR is imperfect.

### 2. Dobrushin–Shlosman, “Phases Corresponding to Minima of the Local Energy” (1987)

Primary author manuscript: [author PDF](https://www.cpt.univ-mrs.fr/~shlosman/papers/109.pdf).

**Read scope:** full text opened; inspected the setup/results around pp.323–326 and the proof machinery around pp.328–329. This is a theorem about phases and coexistence, not a direct cumulant estimate.

**Statement window:** Theorem 1 is stated in the paper’s early section (page preceding printed p.324); the proof decomposes the local spin space into neighborhoods of local-energy minima and a middle region, then establishes a low-temperature ground-state concentration statement, an entropy-state statement, a barrier estimate, and an incompatibility estimate (printed pp.324–327, equations (3.4)–(3.17)). The proof uses reflection positivity/chessboard estimates, see equations (4.1)–(4.4), printed pp.328–329.

**Why close:** the method explicitly separates phases around minima from a barrier region and controls incompatibility, which is a potential framework for deciding when rough/interface components can be integrated into normalized phase-conditioned observables.

**Mismatch:** its purpose is existence/coexistence of Gibbs states and phase separation, not exponential bounds on arbitrary smooth local-function cumulants. The configuration model is Euclidean vector spins with special reflection-positive interactions; it does not match a compact-group two-step posterior or establish the needed connected fourth coefficient. It is a methodological analogy only.

### 3. Georg Menz, “A Brascamp–Lieb Type Covariance Estimate” (2014 manuscript; Theorem 2.3 is credited to Otto & Menz)

Primary manuscript: [PDF](https://citeseerx.ist.psu.edu/document?doi=bb5b76c2558a04ac8838b9a9650237faf04d3324&repid=rep1&type=pdf).

**Read scope:** full text opened. Read Theorem 2.3 setup, its surrounding assumptions, and Corollary 3.3 (lines in extracted manuscript around 138 onward and 648–678); this is sufficient to identify scope but not an independent verification of the proof.

**Statement window:** Theorem 2.3 assumes a finite-dimensional product of Euclidean spaces and a Hamiltonian convex at infinity (a bounded perturbation of a convex function); it bounds covariance using a Gaussian comparison with a suitable matrix and gradients of the two observables. Corollary 3.3 gives exponential covariance decay when its weighted interaction/matrix criterion holds, with a distance weight, for coordinate-local functions; the text explicitly says it extends to arbitrary disjoint supports. The proof of Theorem 2.3 is in Section 2; applications to weakly interacting nonconvex continuous-spin lattice systems are in Section 3.

**Why close:** this is the most useful bounded-chart covariance supplier located: it tolerates a bounded nonconvex perturbation of a convex reference, gives spatially sensitive covariance estimates, and accepts local observables with gradient control. It is directly relevant to chart-conditioned pieces after a uniform convexity/weighted-matrix hypothesis is checked.

**Mismatch:** the paper states only a two-observable covariance theorem; it does not itself state an all-order tree/cumulant estimate. Finite-order cumulants may be assembled from local covariance and additional moment/insertion bounds, which must be checked separately. Its Euclidean chart law is not the whole compact law, and the comparison hypotheses must be checked for the chart Hessian including boundary constraints and all retained normalizers.

### 4. Helffer–Sjöstrand, “On the Correlations for Kac Like Models in the Convex Case” (1994)

Journal record: [Journal of Statistical Physics 74, 349–409, DOI 10.1007/BF02186817](https://doi.org/10.1007/BF02186817); related author/paper context: [Helffer, “Correlation Decay and Gap of the Transfer Operator” (1996), primary full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&paperid=658&what=fullt).

**Read scope:** the 1994 article itself was not opened in a primary full-text copy during this scan; its existence and scope were identified from primary citations and Helffer’s later author paper. The 1996 author paper is full-text accessible and was read at pp.192–195: it describes the earlier Helffer–Sjöstrand general approach to decay of correlations for Gaussian-like Laplace measures with convex potential, and studies a special transfer-matrix/Kac-operator class. It assumes coercivity and derivative growth conditions (equations (2.1)–(2.2), p.193).

**Candidate result window:** the 1994 paper is reported as proving equivalences between uniform functional inequalities and suitable decay of spin-spin correlations for convex Kac-like models. Exact theorem numbers and sharp hypotheses were not verified from its full text here; treat as abstract/citation-level only.

**Why close:** convex Laplace-measure correlation decay is structurally close to a local chart law whose Hessian is uniformly positive and finite range, and can potentially supplement Georg Menz’s covariance estimate when exact convexity is available.

**Mismatch/access:** no primary full-text theorem was accessed here, so no exact result is claimed. The known scope is convex Euclidean/Kac-type systems, not a compact posterior with rare complement sectors or non-Abelian gauge quotient; it is not a full-law theorem. Marked **abstract/citation-only**.

### 5. Lohmann, “Single Scale Cluster Expansions with Applications to Many Boson and Unbounded Spin Systems” (2014)

Primary author manuscript: [arXiv record and HTML](https://arxiv.org/abs/1411.1107).

**Read scope:** abstract/record only in this scan; the source map already recorded abstract/introduction-only prior exposure. The full proof and application hypotheses were not checked here.

**Candidate window:** paper develops a single-scale cluster expansion and applies it to many-boson/unbounded-spin systems. The record does not establish an application to the present compact SU(2) posterior or to its fourth mixed response.

**Why close:** possible technical method for organizing normalized local activities and connected expansions around a Gaussian reference.

**Mismatch/access:** application-specific hypotheses and exact theorem window remain unverified; no use as a supplier is justified from this scan. Marked **abstract-only**.

## Assessment for the target coefficient

No exact theorem was found for the specified actual two-step SU(2) hidden chain. In particular, none of the opened results simultaneously supplies (i) the actual joint density with both fine-field-dependent normalizers retained, (ii) the full compact complement rather than a restricted chart, (iii) two fixed invariant fine sources and two distinct terminal score insertions, and (iv) a summable connected fourth-cumulant/tree bound uniform in finite volume.

Best adaptation direction for the full law: Bricmont–Lebowitz–Pfister’s contour/three-region normalized expansion is the closest actual-law style supplier because it sums interfaces/rough regions at the level of connected correlation functions, rather than inferring cumulants from event tails. Its scalar two-phase machinery is far from a direct match and must be rebuilt for the gauge-aligned SU(2) law.

Best bounded-chart supplier: Georg Menz, Theorem 2.3 and Corollary 3.3 give coordinate-sensitive exponential covariance under convex-at-infinity and weighted interaction assumptions. The paper states a two-observable covariance estimate rather than a fourth-cumulant theorem. A finite-order fourth cumulant can in principle be bounded from suitable local-function covariance estimates together with moment and insertion control; those extra estimates are not part of Corollary 3.3.

The Bricmont–Lebowitz–Pfister full text and Georg Menz manuscript were read; Dobrushin–Shlosman was read in full relevant windows; Helffer–Sjöstrand 1994 was citation/abstract scope only; Lohmann was abstract/record only. No source is presented as proof of the target theorem.

## Addendum: higher cumulants and corrected covariance attribution

### Erratum to entry 3: Menz is sole author; exact covariance hypotheses

The earlier entry’s “Menz–Otto” author label is imprecise. The primary arXiv manuscript is [arXiv:1402.5160](https://arxiv.org/pdf/1402.5160), *A Brascamp–Lieb Type Covariance Estimate*, by **Georg Menz alone** (title page, p.1). The paper says the proof arose from discussions with Felix Otto (p.2), and labels Theorem 2.3 “Covariance estimate, Otto & Menz”; that is theorem attribution, not paper authorship.

Theorem 2.3 (pp.3–4), for \(d\mu=Z^{-1}e^{-H(x)}dx\) on a finite product of Euclidean spaces \(X=X_1\times\cdots\times X_N\), assumes: (a) each conditional law \(\mu(dx_i\mid\bar x_i)\) satisfies a Poincaré inequality uniformly in the conditioned coordinates, with constant \(\rho_i>0\); (b) the mixed Hessian obeys \(|\nabla_i\nabla_jH(x)|\leq\kappa_{ij}<\infty\) uniformly in \(x\); (c) the symmetric comparison matrix with \(A_{ii}=\rho_i\), \(A_{ij}=-\kappa_{ij}\) for \(i\ne j\), is positive definite. Then
\[
|\operatorname{cov}_\mu(f,g)|\leq\sum_{i,j}(A^{-1})_{ij}\,\|\nabla_i f\|_{L^2(\mu)}\,\|\nabla_jg\|_{L^2(\mu)}.
\]
Assumption 2.2 (p.3) separately ensures a global PI for the full law when \(H\) is convex at infinity (bounded perturbation of a convex function). Theorem 2.3’s key local inputs are the conditional PI constants and bounded cross-Hessians; positive definiteness of the comparison matrix is essential. Corollary 3.3 (pp.10–11) turns this into exponential covariance decay under a weighted matrix criterion. It remains a two-observable result, not a fourth-cumulant theorem.

### Strong higher-cumulant supplier: Abdesselam–Procacci–Scoppola (2009)

Primary author manuscript: [arXiv:0901.4756 HTML](https://arxiv.org/html/0901.4756) / [PDF](https://arxiv.org/pdf/0901.4756), *Clustering Bounds on N-Point Correlations for Unbounded Spin Systems*.

**Read scope:** full text opened. Read the model and exact assumptions (Section 1, equations (1)–(4), pp.1–3), Theorems 1–4 (pp.3–4), and tree/forest expansion setup (Sections 2.2–2.5 and 4.1–4.2). This is the strongest exact higher-cumulant/tree-decay supplier located, with an especially relevant genuinely normalized logarithmic generating function and volume-uniform cumulant estimates.

The model is a complex scalar field on arbitrary finite \(\Lambda\subset\mathbb Z^d\), free boundary, with
\[
H_\Lambda(\psi)=\sum_{x,y\in\Lambda}J(x-y)\psi^*(x)\psi(y)+\frac{\lambda}{4}\sum_x|\psi(x)|^4,
\]
where \(\lambda>0\), \(J\) has compact support, \(J(x)^*=J(-x)\), and \(0<J_{\ne}:=\sum_{x\ne0}|J(x)|<J(0)\). The positive quadratic form supplies massive Gaussian covariance; cumulants are derivatives of the logarithm of the normalized expectation (equation (1) and definition immediately after (3), p.2).

Theorem 4 (small self-interaction / near-Gaussian regime, p.4) states: for fixed \(J\) and integer \(N\geq1\), there exist \(\epsilon(J)>0\), \(c_1(N,J),c_2(J)>0\), such that for \(0<\lambda\leq\epsilon(J)\), every nonempty finite \(\Lambda\), and even \(n\geq2(N+1)\),
\[
\sum_{x_2,\dots,x_n\in\Lambda}|\langle\psi^{\sharp_1}(0),\dots,\psi^{\sharp_n}(x_n)\rangle^T_{\Lambda}|\leq c_1(N,J)c_2(J)^n\lambda^N n!.
\]
The insertions are fields \(\psi\) or \(\psi^*\); U(1) symmetry forces odd or charge-unbalanced cumulants to vanish. The paper states that the proofs also yield exponential minimal-tree decay of truncated correlations, although the displayed Theorems 1–4 focus on \(\ell^1\)-summability (p.4, paragraph after Theorem 5). Theorem 4 proof is Section 4, especially §§4.1–4.2.4; it uses Gaussian BKAR forest interpolation and a convergent polymer/Mayer expansion.

**Why close:** this is a real all-orders connected-cumulant result, handles normalized log-generators, has volume-uniform estimates, and shows that small/rare corrections can be integrated before taking the logarithm. Its near-Gaussian regime is expressly described by the authors as a “low temperature” regime after rescaling (Remark 1, p.3), but it is a massive complex Gaussian plus weak positive quartic model—not a compact spin model with a single nondegenerate minimizer, and not a compact complement/rough-island expansion. The field insertions also differ from general smooth gauge-invariant source and boundary-score insertions. Still, this is a promising structural template for the missing κ4/tree step if the actual SU(2) law can first be represented in a compatible massive Gaussian/polymer form.

The same general method is systematized in Lohmann below. The exact source paper’s useful distinction is that Theorems 1–3 control other regimes, while Theorem 4 is the low-temperature/near-Gaussian one; it does not prove clustering for arbitrary unbounded spins solely from convexity.

### Lohmann 2014 full-text result, with actual hypotheses

Primary author manuscript: [arXiv:1411.1107 HTML](https://arxiv.org/html/1411.1107) / [PDF](https://arxiv.org/pdf/1411.1107), Martin Lohmann (title page, p.1). Full text was read at Theorem 1 (pp.5–6), Theorem 4 (pp.25–26), and Theorem 6 (pp.37–38), plus the theorem’s description of support restrictions and large-field decomposition.

Theorem 1 assumes a finite metric site set \((\mathbb L,d)\), fixed field-component count, a symmetric normal (possibly complex) Gaussian covariance \(C\) with \(\lambda_{\min}(\Re C^{-1})=\mu>0\) and finite exponentially weighted covariance norm \(\|C\|_{6m,\infty}\). It allows small analytic local interactions \(V_1\) and a stable two-body polynomial interaction \(V_2\), bounded in specified exponential minimal-tree norms; the scale parameters must meet the explicit stability, small-field/large-field positivity, and smallness conditions (11)–(12), pp.4–5. For
\[
\mathcal Z(J)=\int d\mu_C(\phi)\,\chi_R(\phi)e^{V_1(\phi;J)+V_2(\phi;J)},
\]
Theorem 1 proves \(\log\mathcal Z(J)\) exists and is analytic in sources, with a finite tree-weighted norm, hence exponentially decaying truncated correlations. Crucial limitation: \(\chi_R=\prod_x\chi(|\phi(x)|\le R)\) must be a product of single-site cutoffs; Remark 2 explicitly says the result does not apply to more general, non-ultralocal characteristic functions (p.6). Theorem 4 (pp.25–26) gives the general cluster-expansion/logarithm bound under the listed stability and positivity conditions and includes an explicit large-field decomposition, but still within this Euclidean Gaussian framework.

Theorem 6 (unbounded spin application, p.38) assumes finite \(\mathbb L\), a possibly complex covariance with \(\lambda_{\min}(\Re C^{-1})\ge\mu>0\) and \(\|C\|_{6m,\infty}\le c_\infty\); a repulsive two-body interaction with \(\lambda_{\min}(v)\ge c_v\mathfrak v\) and \(\|v^{1/2}\|_{10m}\le\mathfrak v^{1/2}\); and \(c_J,\mathfrak v\) sufficiently small in terms of \(m,\mu,c_v,c_\infty\). Then source generating logarithm is analytic, and all orders of truncated correlations satisfy a volume-uniform exponentially tree-weighted sum bound (equation in Theorem 6). Remark 14 gives a more explicit \(c^n n!\mathfrak v^{n/4}\) bound, uniform in \(n>2\) and \(\mathfrak v\) (pp.38–39).

**Why close:** direct all-order connected/tree decay for normalized log-generators, with explicit small/large-field techniques and finite-volume-uniform norms. **Mismatch:** massive Gaussian reference plus weak perturbative repulsive interaction, Euclidean unbounded fields, local product cutoff in the general theorem, and no compact gauge quotient or SU(2) hidden posterior. It does not establish a cluster expansion from only “unique nondegenerate minimum”; the mass gap of the Gaussian reference is a real input. Thus useful expansion machinery after constructing an appropriate reference law, not a ready-made actual-law result.

### Single-ground-state continuous/compact low-temperature search outcome

Additional queries: “unique nondegenerate minimum low temperature expansion Gibbs measure cluster expansion continuous spins”, “unique ground state continuous spin low temperature cluster expansion theorem”, and targeted searches for compact-spin low-temperature expansions. These surfaced a classical monograph’s contents listing a chapter “Expansions Around Ground States (Low-Temperature Expansions), §2 Continuous Spin: Unique Ground State” and separate sections on semi-invariants, but no accessible primary research paper with theorem/proof matching the requested single smooth nondegenerate ground state plus normalized connected correlators was located in this scan. No theorem is inferred from the contents listing. The two-phase continuous-spin Ising result already in entry 1 is not used as a proxy for this case.

Therefore this targeted search found **no primary paper theorem within scope** proving volume-uniform normalized connected cumulant/tree decay for compact continuous spins from a unique nondegenerate minimum, nor an actual compact-SU(2) rough-complement expansion of the requested type. The new concrete higher-cumulant supplier is the massive-Gaussian/weak-interaction cluster expansion of Abdesselam–Procacci–Scoppola and Lohmann, with the precise reference-law mismatch stated above.


## Focused follow-up: one nondegenerate ground state, large fields, and higher cumulants

This follow-up narrows the question to a low-temperature finite-range continuous-spin model with one nondegenerate ground state, volume-uniform quadratic stability, and a possibly non-diagonally-dominant full Hessian. It also checks the requested normalized connected-correlation conclusion rather than inferring it from rare-event probabilities.

| Source and exact window | Actual assumptions and conclusion | Match / mismatch for the target |
|---|---|---|
| Malyshev–Minlos, *Gibbs Random Fields: Cluster Expansions* (1991), Ch. 5 §2, printed p.149; Ch. 6 §§2–3 and §5, pp.167–179, 187 onward. [Publisher book/TOC](https://link.springer.com/book/10.1007/978-94-011-3708-9); [independent TOC scan](https://www.gbv.de/dms/hbz/toc/ht003928821.pdf). | Identity of the lead is verified: both authors and Springer list “Expansions Around Ground States (Low-Temperature Expansions),” with §2 “Continuous Spin: Unique Ground State,” followed by a separate chapter on decay of correlations and semi-invariant estimates. But the actual Ch. 5 and Ch. 6 chapter text is subscription restricted here; only publisher metadata/contents were accessible. No theorem hypotheses, normalized-correlator formula, constants, or proof window can therefore be responsibly extracted. | It is the closest bibliographic lead exactly naming the requested ground-state regime. Insufficient access means **no actual theorem match established**. The contents alone cannot establish whether the interaction Hessian may be non-diagonally-dominant, whether insertions are normalized/logarithmic, or whether large fields are controlled. The monograph has a separate two-ground-state section; those methods are not assumed applicable to the unique-ground-state section. |
| Bach–Møller, “Correlation at Low Temperature: I. Exponential Decay,” *J. Funct. Anal.* 203 (2003), 93–148, DOI [10.1016/S0022-1236(03)00046-6](https://doi.org/10.1016/S0022-1236(03)00046-6); [full author manuscript PDF](https://citeseerx.ist.psu.edu/document?doi=98049e7c58f80728922d4c7a6d402fe57fee00a2&repid=rep1&type=pdf). | Full manuscript read, especially §I.2, Hypotheses 1–2, equations (I.6)–(I.16), pp.7–9; Theorem I.1, equation (I.17), p.9; proof §I.6 and technical Theorem II.1; localization Theorem I.6/§III. Hypothesis 1 permits each scalar onsite energy (f_j) to have 0 as unique nondegenerate **global minimum**, while other critical points are allowed, subject to uniform curvature, critical-value separation, derivative/growth conditions (I.8)–(I.11). Hypothesis 2 assumes pair interactions (w_{ij}) vanish on-site and at the origin, are controlled by a symmetric nonnegative exponentially summable weight matrix (a_{ij}) through (I.14)–(I.16), and enter with a fixed sufficiently small coupling λ. Theorem I.1 supplies a volume-uniform exponential bound on the **truncated coordinate-spin covariance** (E^T(x_i;x_j)), with an exponential distance weight (I.17), for sufficiently low temperature and a small exponential tilt; it does not state that estimate for arbitrary smooth local functions. Proof uses a twisted Witten Laplacian, a comparison operator, and semiclassical localization; the proof treats large fields through partition-function localization, not by restricting the theorem to a local chart. | Strongest accessible low-temperature, unique-global-minimum source located and it genuinely treats full unbounded real spins / large fields, retaining normalized expectations. But its theorem directly covers coordinate-spin covariance only, not arbitrary local-function insertions or a fourth cumulant/tree bound; suitable local covariance and moment estimates could still be combined to derive a finite-order cumulant bound. It assumes scalar Euclidean spins and weak pair coupling controlled relative to onsite potentials; “uniformly massive Hessian” alone is not shown sufficient. Its comparison is perturbative from a site-diagonal reference; it does not certify arbitrary non-diagonally-dominant stable Hessians. No compact-spin, gauge quotient, multi-layer hidden-law, or arbitrary smooth source-score insertions. It is a plausible first-covariance supplier after matching hypotheses, not the missing connected-log theorem. |
| Georg Menz, “A Brascamp–Lieb Type Covariance Estimate,” [arXiv:1402.5160](https://arxiv.org/pdf/1402.5160), title p.1; Theorem 2.3, pp.3–4; Corollary 3.3, pp.10–11. | Correct authorship: **Georg Menz alone**; p.2 says proof came from discussions with Felix Otto, while Theorem 2.3 is titled “Covariance estimate, Otto & Menz.” Theorem 2.3 requires uniform conditional single-site Poincaré constants ρ_i, globally bounded cross-Hessians κ_ij, and positive definiteness of comparison matrix (A_{ii}=ρ_i, A_{ij}=-κ_{ij}) (not merely positive definiteness of the full Hessian). Assumption 2.2 separately requires convex-at-infinity/bounded perturbation of a convex Hamiltonian to get global PI. Conclusion is a two-function covariance bound by (A^{-1})-weighted gradient norms. Corollary 3.3 gives spatial decay when the weighted matrix criterion holds. | This is not an independent answer to the current low-temperature/large-field question. It emphasizes the exact conditional-PI plus comparison-matrix criterion; full-Hessian mass by itself is not that criterion. Only second covariance, and Euclidean state space. |

### Exact applicability summary

| Requested property | Closest verified source | Status |
|---|---|---|
| Unique nondegenerate ground state; whole unbounded spin space including large fields; volume-uniform normalized correlations | Bach–Møller, Theorem I.1 | **Partly supplied:** normalized truncated coordinate-spin two-point covariance in a scalar weak-coupling model; no higher cumulant is stated directly. |
| Full Hessian massive but not diagonally dominant, without a perturbative onsite-plus-small-pair representation | None verified | **No match found.** Menz requires the conditional-Poincaré comparison matrix positive definite; Bach–Møller uses weak coupling and onsite localization. |
| Normalized connected fourth cumulant/tree decay around that unique ground state | Malyshev–Minlos Ch. 5 §2 / Ch. 6 are the exact likely source, but full text unavailable; Bach–Møller does not state this | **Unresolved / no theorem statement extracted.** Do not infer from the book contents or from its two-point coordinate-spin result; separate covariance plus moment estimates may supply a finite-order cumulant by other means. |
| Compact continuous spin or SU(2) gauge-aligned two-step posterior; rough islands integrated while retaining normalized insertions | None of these sources | **No actual-law result found.** The accessible continuous-spin theorem is on ℝ-valued spins; cluster-expansion examples already inventoried require Gaussian/polymer structure. |

Search was deliberately targeted rather than broadened: exact title/section searches for the Malyshev–Minlos unique-ground-state chapter; Bach–Møller’s citation trail to unique-minimum low-temperature analysis; and primary-source checks of the Menz hypotheses. Full text was available and read for Bach–Møller and Menz. For Malyshev–Minlos, publisher metadata and the independent scanned TOC were read, but chapter proof text was inaccessible; no theorem statement is claimed. The cited connected-correlation book chapter is the natural next retrieval target if library access is available. No proof-source files or numeric jobs were touched.

## Candidate route: central-block total-variation oscillation and finite-size mixing

Question tested: can a small total-variation oscillation of a central block marginal, uniformly over exterior boundary conditions, supply a finite-size Dobrushin–Shlosman criterion and hence volume-uniform mixing? The primary statements support a **conditional route** only when this estimate is a uniform family of finite-volume tests with the right geometry/specification; a single central marginal estimate for one box is not such a criterion.

### Dobrushin–Shlosman complete-analyticity criterion (finite-state, finite-range setting)

Primary source: R. L. Dobrushin and S. B. Shlosman, “Completely Analytical Interactions: Constructive Description,” *Journal of Statistical Physics* 46 (1987), 983–1014, [author manuscript PDF](https://www.cpt.univ-mrs.fr/~shlosman/papers/132.pdf), DOI [10.1007/BF01011153](https://doi.org/10.1007/BF01011153). Full text opened; relevant theorem/definition windows are §2, printed pp.987–990, equations (2.13)–(2.28), and §§4–6, printed pp.998–1009, especially Theorem 4.1, Proposition 5.3, and the surgery lemmas.

The setting stated at the outset is finite single-spin space and translation-invariant finite-range interactions on ℤ^v (printed pp.984–986). All tests are uniform in finite volume (V) and every boundary condition. Their Condition IIIa (equations (2.20)–(2.21), p.988) compares the conditional Gibbs distributions restricted to the shell (B(t,p,V)=\{s\in V:p<|s-t|\le p+r\}\), where (r) is interaction range, under exterior conditions differing only at a boundary site (t\in\partial V). It requires the explicit small total-variation cutoff in (2.20), uniformly over those tests. The PDF text extraction did not render the right-hand side of (2.20) reliably, so I do not transcribe its numeric cutoff here; the site-to-set output and its constants in (2.24) are legible and recorded below. Conditions IIIb–IIIc strengthen/repackage this as site-to-set influence: equation (2.24) requires, for every finite (V), interior (A\subset V), boundary site (t\in\partial V), and boundary pair differing only at (t),
\[
\operatorname{Var}(Q_{V,A}(\cdot\mid\delta_1),Q_{V,A}(\cdot\mid\delta_2))\le K e^{-\gamma\,\operatorname{dist}(t,A)}.
\]
Here “Var” is total variation (½ ℓ1), (Q_{V,A}) is the (A)-marginal of the normalized finite-volume Gibbs law, and the constants are uniform in (V,A,t,δ_1,δ_2). Thus the basic output is **a single-boundary-site influence on the whole tested marginal**, not just a one-site expectation difference.

The constructive finite-size version checks the corresponding conditions only for volumes of diameter at most (d_0); the allowed (d_0=d_\alpha(g_\alpha)) depends on the condition and its constants. Theorem 4.1 (p.998) says the main component of the resulting constructive class is the completely analytical (CA) class. The proof route (§§5–6) iterates local coupling/surgery: Proposition 5.3 yields exponentially decaying (f)-closeness between whole finite-volume conditional Gibbs distributions when the exterior conditions differ at one site, and Lemma 5.1(i) converts this coupling profile to a TV marginal estimate by summing it over the region: \(\operatorname{Var}(Q_{V,A}^1,Q_{V,A}^2)\le\sum_{s\in A} f(s)\). The local insertion estimate must therefore be summed over sites of (A); for boundary changes at many sites, telescope the single-site bounds to obtain a sum over changed boundary sites. The CA conclusion includes Condition IIc (2.18), the volume-uniform truncated/semi-invariant bound by a minimal connected hull of the supports (with constants depending on order), so it supplies more than covariance when its hypotheses hold. These are finite-state, finite-range, translation-invariant statements; periodic/toroidal systems are among typical finite lattices only if the same uniform boundary specification and finite-volume tests are established. No automatic periodic-boundary conclusion is taken here.

**Relation to the proposed observable:** if, for every relevant finite buffer (V), every boundary location (t), and every pair of exterior conditions differing only at (t), the measured block (A=A(V,t,p)) is exactly the shell/marginal required by Condition IIIa and its TV oscillation is below the explicit cutoff in equation (2.20), then it can serve as the Dobrushin–Shlosman finite-size input. A uniform estimate over *all* pairs of exterior conditions is stronger than the one-site boundary perturbation tested by DS, but only for that same marginal and geometry. A bound for one fixed center/box, or only for an observable average, does not supply tests for every (V,t,A). To turn the site-to-set conclusion into decorrelation of two local functions, one must apply it to the support of one function after conditioning/separating it from the other and sum the resulting boundary-site influence; the all-order connected bound is supplied by CA/Condition IIc, not by the central marginal estimate in isolation.

### General block-comparison theorem (measurable state spaces)

Primary source: Patrick Rebeschini and Ramon van Handel, “Comparison Theorems for Gibbs Measures,” [arXiv:1308.4117](https://arxiv.org/pdf/1308.4117). Full manuscript read at Definitions 2.2–2.3 and Theorem 2.4 (pp.5–7), Corollary 2.8/Remark 2.9 (pp.9–10), and the proof setup in §3.

This theorem applies to finite or countable site sets with measurable local spaces. It requires a cover ℐ of sites by update blocks (J), invariant local update kernels for the two laws, couplings (Q^J_{x,z}) of block updates when configurations differ at one site, and couplings \(\widehat Q_x^J\) comparing the two laws' block updates at the same configuration. With positive block weights (w_J), its influence matrix is
\[
W_{ij}=\mathbf1_{i=j}\sum_{J\ni i}w_J,\quad
R_{ij}=\sup_{x,z:\,x_{I\setminus\{j\}}=z_{I\setminus\{j\}}}\frac{1}{\eta_j(x_j,z_j)}\sum_{J\ni i}w_J Q^J_{x,z}\eta_i,
\]
and its perturbation vector is \(a_j=\sum_{J\ni j}w_J\int^*\widehat Q_x^J\eta_j\,\tilde\rho(dx)\). Under quasilocality and condition (2.1), the matrix series \(D=\sum_{n\ge0}(W^{-1}R)^n\) is defined and it bounds local-function expectation differences by \(|\rho f-\tilde\rho f|\le\sum_{i,j}\delta_i f\,D_{ij}W^{-1}_{jj}a_j\) (Theorem 2.4). Corollary 2.8 gives usable contraction conditions, including \(\|W^{-1}R\|_\infty<1\), and weighted/summable variants. For bounded site metrics, finite products are automatically tempered. Choosing a metric weight by graph distance gives exponential decay only when the corresponding weighted block-influence matrix still contracts.

This theorem is flexible enough for compact continuous single-link spaces and arbitrary finite volumes, without translation invariance, provided the actual posterior has the required block conditional kernels and a coupling influence matrix. It does **not** say that a small TV oscillation of one central marginal alone gives contraction: the whole matrix of block responses to single-site discrepancies (plus integrability of the perturbation vector) is required. The direct output is a comparison bound on expectations of local/quasilocal functions. The theorem directly gives local-function expectation comparison. Covariance and finite-order cumulants can be derived only after the relevant conditional specification, oscillation sums, and moment bounds are supplied; the paper itself does not state those connected-cumulant conclusions. The paper allows general measurable state spaces, but it is not a finite-volume criterion inferred solely from one central marginal.

### Applicability verdict

| Proposed input or desired output | Exact literature requirement | Finding |
|---|---|---|
| Small central-block TV oscillation in a buffer of radius (R) | Dobrushin–Shlosman: all finite-volume/site/boundary tests at the specified shell scale, or equivalently its uniformly verified site-to-set influence family; finite state, finite range, translation-invariant interaction in the 1987 theorem | A candidate finite-size input only if the posterior lemma is uniform over every translated buffer, every boundary site, all exterior conditions, and exactly the required full block marginal. One-box/one-center control is insufficient. |
| Conversion to exponential spatial mixing | Dobrushin–Shlosman Theorem 4.1 and Propositions 5.3 / Condition IIIc | Yes conditionally in their hypotheses; influence is TV on an arbitrary tested subset and one boundary-site perturbation. For many-site boundary disagreement, add the single-site influences. |
| Connected local correlators | Dobrushin–Shlosman CA Condition IIc (2.18) | Gives normalized truncated/semi-invariant tree/hull bounds in the finite-state finite-range CA class, uniform in finite volumes and b.c.; not transferred here. |
| Compact continuous SU(2) link state / non-translation-invariant actual two-step posterior | Rebeschini–van Handel Theorem 2.4 block comparison | General measurable-space block comparison is structurally compatible if its kernels, couplings, and contracting influence matrix are proved for the actual law. A central marginal oscillation alone is not that matrix criterion and yields no fourth cumulant by itself. |

Targeted queries this round: “Dobrushin Shlosman complete analyticity finite size criterion influence matrix arbitrary boundary conditions central block marginal”; “Dobrushin Shlosman strong mixing condition definition finite regions boundary influence theorem”; “constructive unicity criterion Dobrushin Shlosman”; and direct checks of the primary Dobrushin–Shlosman 1987 manuscript and Rebeschini–van Handel arXiv manuscript. No other repo source was changed. The nearest direct theorem is the Dobrushin–Shlosman finite-size criterion in its finite-spin/translation-invariant setting; the measurable-space block comparison result is the closest framework for compact continuous spins, but its central requirement is an explicit contracting site/block influence matrix, not just central-block TV oscillation.
