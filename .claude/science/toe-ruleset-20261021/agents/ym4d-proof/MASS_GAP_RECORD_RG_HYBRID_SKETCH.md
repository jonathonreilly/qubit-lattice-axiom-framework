# A Record + RP + RG hybrid route to a Yang–Mills mass gap: a conditional theorem and an honest audit

**Status:** author-side working sketch; no independent audit verdict. Companion to [MASS_GAP_CROSSOVER_REDUCTION.md](MASS_GAP_CROSSOVER_REDUCTION.md), which is the self-contained statement. Closes no MG row.
**Date:** 2026-10-31 (EDT); header and §5, §7, §8 updated 2026-11-01; editorial relabelling 2026-11-01.
**Statement form.** This file is narrative background. Every mathematical statement in it is restated, with definitions, quantifiers and a status label (proved here / cited / open / conjecture / remark), in [MASS_GAP_CROSSOVER_REDUCTION.md](MASS_GAP_CROSSOVER_REDUCTION.md) §§1–5 and its dependency table §9; where the two differ, the reduction note governs. Labels used here: **[cited]**, **[repo, unaudited]**, **[open]**, **[outline]**, **Conjecture**, **Remark/Heuristic**. No statement here depends on a computation.
**Repo snapshot used:** `jonathonreilly/qubit-lattice-axiom-framework`, `main` at `d9b869b97` (2026-10-09 08:19 EDT). Every repo note cited below has `audit_status: unaudited` in `docs/audit/data/ledger/**` at this snapshot.
**PRs read (read-only, pinned heads):**
- #10114 `claude/ym4d-proof-draft` @ `f76f6c64`.
- #10132 `claude/ym4d-hard-route` @ `69154762` for the body; rechecked at `5ad46ff7` (2026-11-01). The newer commits are existence-side hard-core work (closure, interface gates, `parts/hard-core--excess.md`); they leave `parts/witness.md`, `parts/upper-chain.md` and `GOAL.md` unchanged and do not affect this sketch.
- Missed in the first pass and now cross-referenced: [CROSSOVER_LITERATURE_BRIDGE_ASTRA.md](CROSSOVER_LITERATURE_BRIDGE_ASTRA.md) (Kirk v4 handoff; Lemma 3.26 determinant inference does not follow as printed). It bears on CW: no checked import supplies CW.

**Bottom line, up front.** This is **not** a proof of the mass gap. It is a conditional theorem (Theorem H) that reduces a volume-uniform, cutoff-uniform physical gap to the proved facts listed below plus one irreducible estimate: the *crossover-window clustering estimate* (CW). Three points matter most:

1. The Record axiom, as written in the repo, implies **no** correlation decay.
2. Two scope tests (§0.6): a "Record clustering" input that used neither the non-abelian group nor d = 4 would also give a gap for compact U(1) in d = 4, which has a proved massless phase; so any such input must use group- or dimension-specific structure. This is a test, not a global no-go or route-exhaustion claim (registry rule).
3. The fixed-spacing part (A) at strong coupling is already proved, without Record: in the literature, and as a volume-uniform Doob-contraction gap for β ≤ 1/32 in #10114.

The new content consists of:

- the precise reduction, with the crossover named as the single open estimate;
- two scope tests on the naive "Record ⇒ clustering" step (Observation P, proved; the U(1) scope test, cited; the d ≥ 5 check is Heuristic);
- the observation that the effective RG actions do not need RP;
- an exact mapping onto #10114's MG0–MG5 contract.

---

## 0. CENTERPIECE: hybrid Theorem H (Record/RP fixed-spacing gap + Balaban-type RG flow to a cluster regime)

### 0.1 Setting (supplied, not derived from the axioms)

- **Lattice.** Λ = (Z/LZ)^4 with spacing a, Euclidean time as the 4th direction.
  - The repo's Lattice axiom gives only spatial `Z^3` (`docs/MINIMAL_AXIOMS_2026-06-29.md`).
  - The Euclidean time direction, the hypercubic symmetry that exchanges time and space, and the action are **supplied**.
  - The memo itself says Admissibility "does not choose a Hamiltonian or transfer operator".
- **Wilson measure.** dμ_{β,Λ}(U) = Z^{-1} exp(β/N Σ_p Re Tr U_p) Π_ℓ dU_ℓ, with U_ℓ ∈ SU(N) and β = 2N/g_0².
  - For SU(3), the group label is the one the repo motivates through `docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`.
  - However, that note produces a *taste-space* commutant su(3) ⊂ gl(3)⊕gl(1), not a link connection (§1.3). The link field is therefore also supplied.
- **Observables.** 𝔄_+ = gauge-invariant local functions (Wilson loops, plaquette polynomials) supported at t > 0.
- **Reflection.** Θ = reflection in a plane, either through links (t ↦ 1 − t) or through sites.

### 0.2 Hypotheses

| Tag | Hypothesis | Status |
|---|---|---|
| **H1 (RP)** | μ_{β,Λ} is reflection positive for Θ (link and site planes, periodic Λ, all β ≥ 0) | **Proved, literature:** Osterwalder–Seiler, Ann. Phys. 110 (1978) 440. **Repo, partial (unaudited):** two-slice temporal-gauge Gram PSD (`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`); one-link kernel PSD, c_λ(β) ≥ 0 (`WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md`). Lemma A1 below closes the multi-slice gap at the lattice level using those two repo facts plus elementary operator theory. |
| **H2 (transfer matrix)** | T = P_G M^{1/2} K M^{1/2} P_G is bounded, self-adjoint, positive and compact on L²(SU(N)^{E_spatial})^{G}, with a simple top eigenvalue | **Proved, literature:** Lüscher, CMP 54 (1977) 283; Osterwalder–Seiler 1978. **Repo:** finite-dimensional packets only. Sketch: Lemma A1. |
| **H3 (lattice gap ⇔ clustering)** | On the RP-reconstructed space, uniform decay of reflected correlations for a dense family ⇔ spec(H_a) ⊂ {0} ∪ [m_lat,∞) | **⇒ direction (gap ⇒ clustering):** repo, finite block (`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`). **⇐ direction:** the standard spectral-measure argument, written as #10114 `MASS_GAP_TARGET.md` §2. Lemma A2. |
| **H4 (strong-coupling cluster regime)** | For β ≤ β_sc, truncated correlations of local gauge-invariant observables decay as e^{−m_sc(β) d}, uniformly in Λ, with m_sc(β) ≥ −log(c·β) | **Proved, literature:** Osterwalder–Seiler 1978 (cluster expansion). **#10114, scoped, same-family review:** SU(2) Doob contraction r(β) ≤ 18/359 for 0 < β ≤ 1/32, uniform in spatial volume and slab depth (`MASS_GAP_LOCAL_BLOCK_ASTRA.md`). **Repo:** packet bound λ_1/λ_0 ≤ (2/3)β for β ≤ 1 (`NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md`), and Yarotsky-import electric-dominated Hamiltonian gap (`GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md`). |
| **H5 (UV stability, finite volume)** | Balaban block-spin RG with scale factor L_b: for g_0 small, the effective actions S_k on the spacing-L_b^k·a lattice exist in a fixed finite physical torus. They take the form (1/g_k²)·(Wilson-like) + polymer remainder, with small-field analyticity, large-field suppression and running g_k following asymptotic freedom, **as long as g_k ≤ ḡ** (ḡ small) | **Proved, literature, in finite volume, for partition-function/effective-action bounds:** Balaban, CMP 95–122 (1984–89), as listed in #10132; Dimock's expositions. **Not proved:** infinite volume, gauge-invariant correlation functions in general, mass gap (§3). |
| **H6 (flow reaches ḡ)** | For g_0 → 0 there is k_1(a) with g_{k_1} ≈ ḡ and L_b^{k_1}·a → ℓ_1 = c_1/Λ_L (lattice Λ-parameter) | Plausible; follows from H5 plus asymptotic-freedom bookkeeping in the controlled region. Not written in the repo or the PRs. |
| **CW (crossover-window clustering)** | There exist ḡ ≤ g_*, a fixed number n_* of further RG steps (or a direct estimate), and μ_* > 0 such that the effective measure at scale ℓ_* = L_b^{n_*} ℓ_1 has truncated gauge-invariant correlations decaying as e^{−μ_* d/ℓ_*}. This must hold uniformly in the volume and in a, and transport back to the *original* observables (with sources) without losing the rate | **OPEN. Irreducible.** This is the gap at intermediate coupling. Balaban control stops at ḡ, the cluster expansion starts only at β ≤ β_sc (g² ≳ 2N/β_sc, e.g. g² ≳ 128 for N=2 at β_sc = 1/32), and no theorem covers the window. |
| **H-Rec** | Any "Record clustering" input | **Conjecture (not adopted; not used).** The axiom text supplies nothing (§0.5). If H-Rec is stated strongly enough to give CW, it is CW. |

### 0.3 Theorem H (conditional)

*Status: conditional on H1–H6 and CW (and MG2 via Step B4); proof outline in §0.4; restated precisely in MASS_GAP_CROSSOVER_REDUCTION §4.*

> **Theorem H.** Assume H1–H6 and CW for SU(N), N ≥ 2, in d = 4. Let g_0(a) → 0 along the asymptotic-freedom trajectory (fixed Λ_L). Then for every a small enough and every volume, the RP-reconstructed lattice Hamiltonian H_a = −a^{−1} log(T/‖T‖) satisfies
>
> spec(H_a) ⊂ {0} ∪ [m_*, ∞),  ker H_a = span{Ω_a},  m_* := c·Λ_L with c = μ_*/(c_1 L_b^{n_*}) > 0 independent of a and of volume.
>
> If, in addition, MG0 (existence and OS reconstruction of the a → 0 limit along this trajectory) holds, then the continuum Hamiltonian H satisfies spec(H) ⊂ {0} ∪ [m_*,∞) with unique vacuum. If MG4 also holds, the excited sector is non-empty. Both are taken from #10114's ledger.
>
> **Without CW** the theorem is empty for a → 0. With β ≤ β_sc fixed, the proved part (H1–H4) gives only the fixed-spacing statement spec(H_a) ⊂ {0}∪[−a^{−1}log(cβ),∞). That is Osterwalder–Seiler-level and is already in #10114 for SU(2).

### 0.4 Step list (proof outline of Theorem H from its hypotheses)

Statuses: A1 [outline; cited Lüscher 1977]; A2 [proved; = #10114 MASS_GAP_TARGET §2]; A3 [outline]; A4 = H4 [cited]; B0 Definition; B1 = H5 [cited, finite volume]; B2 = H6 [open]; B3 = CW [open]; B4 = MG2 [open]; B5 [follows from A2, B2–B4].

**Step A1 (RP ⇒ positive compact transfer matrix; repo facts suffice at fixed Λ).**

- Work in temporal gauge, which is exact on a periodic lattice up to one Polyakov holonomy per spatial site. That holonomy is absorbed by the Gauss projector P_G = ∫ Π_x dg_x.
- The Wilson weight factorizes as Π_t M(U_t)^{1/2} K(U_t,U_{t+1}) M(U_{t+1})^{1/2}, where:
  - K = ⊗_{spatial ℓ} k_β(U_ℓ V_ℓ^†), with k_β(W) = exp[(β/N) Re Tr W];
  - M = exp(magnetic plaquettes in one slice).
- The repo's c_λ(β) ≥ 0 (`WILSON_SU3_…KERNEL_POSITIVITY…`) means k_β is a positive-definite class function, so convolution by k_β is a positive operator. It is Hilbert–Schmidt because k_β ∈ L² of a compact group.
- A tensor product of positive compact operators is positive and compact. Sandwiching by the bounded positive multiplication operator M^{1/2} and projecting by P_G, which commutes with K and M by gauge invariance, keeps it positive and compact.
- k_β > 0 pointwise, so Jentzsch/Krein–Rutman gives a simple top eigenvalue with a positive eigenfunction.
- Z = Tr(P_G T^{L_t}). Multi-slice RP is then ⟨Θ(F) F⟩ = ‖T^{t_F/2}-weighted vector‖² ≥ 0 for F ∈ 𝔄_+.
- *This is standard (Lüscher 1977). The only new point is that the repo's two unaudited facts are exactly the inputs it needs.* What the repo is missing is this assembly, not a new idea.

**Step A2 (uniform reflected decay ⇔ gap; lattice version of #10114 §2).**

- For F ∈ 𝔄_+ with ⟨F⟩ = 0, set v_F = [F] in the OS space ℋ_a = closure(𝔄_+/null). Then C_F(n) = ⟨Θ(F) τ_n F⟩ = ⟨v_F, T̂^n v_F⟩ = ∫ λ^n dν_F(λ).
- If C_F(n) ≤ A_F e^{−m n a} for n ≥ n_F, then ν_F is supported in [0, e^{−ma}]. Otherwise the mass of ν_F near 1 would beat the exponential bound as n → ∞.
- {v_F} is dense in ℋ_a by construction, so spec(T̂|Ω^⊥) ⊂ [0, e^{−ma}], i.e. H_a ≥ m on Ω^⊥.
- A_F and n_F may depend on F. m may not.
- The converse is the repo's 2026-05-09 bridge.

**Step A3 (volume uniformity and thermodynamic limit at fixed a).**

- If the decay in A2 holds with m independent of Λ, take a translation-invariant weak limit point of μ_{β,Λ} (compactness of SU(N)^{links}). RP and the fixed-n decay bounds are closed under weak limits.
- Reconstruct ℋ_a^∞ and apply A2 there. The same m works.
- Cluster expansion gives uniqueness of the limit at β ≤ β_sc. In the crossover window it does not; CW must supply it.
- This is #10114 §3's "fixed-t limit first" discipline: bounds are taken at fixed n before any n → ∞.

**Step A4 (strong coupling ⇒ A2's hypothesis).** H4 gives m_sc(β) ≥ −log(cβ) in lattice units, uniformly in Λ. **Part (A) is proved here, but only for β ≤ β_sc.** Record plays no role.

**Step B0 (inductive hypothesis IH(k) on effective actions; Balaban-type).** On the lattice of spacing a_k = L_b^k·a in a fixed physical box, the measure on block variables V is ∝ exp(−S_k(V)) with:

- (i) **small-field analyticity:** S_k = (1/g_k²) S_W(V) + Σ_{X polymer} E_k(X;V) on the small-field set {|V_p − 1| ≤ p(g_k)}. Each E_k(X) is gauge invariant and analytic in a complex neighbourhood, with |E_k(X)| ≤ g_k^{κ_0} e^{−κ|X|} (κ independent of k).
- (ii) **large-field suppression:** large-field regions R carry weight ≤ e^{−c p(g_k)² |R| / g_k²}.
- (iii) **coupling flow:** g_{k+1}^{−2} = g_k^{−2} + b_0 log L_b² + O(g_k²).
- (iv) **"Record-derived" decay in block units, as asked:** |⟨A;B⟩_k| ≤ C e^{−μ_k dist_k(A,B)}.

*Heuristic (adversarial note on (iv)).* For g_k ≤ ḡ, (iv) does **not** hold with μ_k bounded below. In the weak-coupling region, correlations of the effective theory are those of a nearly massless gauge field at scale a_k ≪ 1/Λ, with polynomial decay up to distance ~ 1/(Λ a_k) block units. So μ_k ≈ a_k·m_phys → 0 as k decreases. Imposing (iv) uniformly at every scale would be false at small k, or equivalent to assuming the answer.

The correct inductive hypothesis keeps only (i)–(iii) through the controlled region, and requires decay **only at the terminal scale**. Balaban's polymer decay e^{−κ|X|} is *locality of the action*, not clustering of the measure. Conflating them is the main circularity trap (§0.7, C1).

**Step B1 (what one RG step must preserve).** Going from IH(k) to IH(k+1) with the same κ and p(·), the step must preserve:

- gauge invariance, by covariant block averaging (axial/Landau gauge fixing inside blocks, as Balaban does);
- small-field analyticity domains, which shrink by at most a fixed factor per step;
- polymer bounds, with a sum over steps that converges because of the factor g_k^{κ_0};
- large-field suppression;
- the renormalization of the coupling only, since the action is marginal in d = 4 (repo cross-check: `YANG_MILLS_COUPLING_MARGINALITY_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`, unaudited).

**RP of S_k is NOT needed.** The spectral argument (A1–A2) uses RP of the *original* Wilson measure, which holds by H1. RG enters only as a device for estimating the original C_F(n). This removes a known difficulty: block-spin kernels generally break RP. That is the content of B1, and it is H5. Proved by Balaban in finite volume.

**Step B2 (flow to ḡ).** H6: after k_1(a) steps, g_{k_1} ≈ ḡ and a_{k_1} ≈ ℓ_1 = c_1/Λ_L. The number of steps k_1(a) → ∞ as a → 0, but the physical scale ℓ_1 is fixed. *Plausible, bookkeeping.*

**Step B3 (crossover: THE OPEN STEP).** From the effective theory at (ℓ_1, ḡ), with a non-Wilson action plus polymers plus large-field regions, show a decay rate μ_* at scale ℓ_* = L_b^{n_*} ℓ_1, uniformly in the volume. Possible ways:

- (a) Continue RG beyond ḡ until the effective theory enters a cluster-expansion regime. No small parameter controls these steps.
- (b) Prove a Dobrushin/Doob contraction (as in #10114's local-block note) directly for the effective kernel at scale ℓ_1. This needs a quantitative bound on the effective one-block conditional laws that no one has.
- (c) Feed in a hypothesis (H-Rec). See §0.5–0.6 for the scope tests a generic input must pass.

**Step B4 (transport back to original observables, #10114 MG2).**

- For F ∈ 𝔄_+ at original spacing, write ⟨Θ(F) τ_n F⟩ as an effective-theory expectation of a source-dependent block functional. That requires an RG with sources, which Balaban's papers do not provide in general.
- The decay at rate μ_*/ℓ_* in physical distance n·a transfers with an F-dependent prefactor A_F and onset t_F. That is allowed by MG1.
- *Open in general; plausible for smeared observables of physical size ≥ ℓ_*.*

**Step B5 (conclude).**

- By A2, H_a ≥ μ_*/ℓ_* = m_* on Ω^⊥, uniformly in a and volume.
- Since ℓ_* = const/Λ_L, we get m_* = c·Λ_L.
- Passage to the continuum needs MG0: an a → 0 limit point along the trajectory, with OS axioms and reconstruction. Then, by the fixed-t-first rule, the bound C_F(t) ≤ A_F e^{−m_* t} passes to the limit at each fixed t ≥ t_F, and the spectral argument applies to the continuum H.
- Rotation invariance (O(4) recovery) is not needed for the gap itself, but it is needed for the full Clay statement and is open (#10132 lists O(4) as a later target).

### 0.5 What the Record axiom actually says, and what it can and cannot contribute

Verbatim, `docs/MINIMAL_AXIOMS_2026-06-29.md`:

> "### Record / Fixed Reality — Records form. When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

- **No decay, mixing or dynamics clause.** The axiom says nothing about correlations, locality of the measure, or time evolution. The memo lists record-production dynamics, persistence dynamics, the time metric, the source/action and `g_bare = 1` as open gates outside the axioms.
  - The closest repo item, `DYNAMICS_CLAUSE_RECORD_FREQUENCIES_FOLLOW_THE_ONE_SHOT_ODDS_EXACTLY_WHEN_CORRELATIONS_CLUSTER_BOUNDED_THEOREM_NOTE_2026-09-24.md`, runs the other way. It *assumes* clustering and imports the standard theorem "unique gapped ground state ⇒ exponential clustering" for frequencies to follow the odds.
  - It also uses a *supplied* dynamics clause. It is not Record ⇒ clustering.
- **Permanence obstructs temporal clustering of record observables (Observation P; proved: MASS_GAP_CROSSOVER_REDUCTION Lemma 5.5).**
  - If R is a record readout at a site, permanence means R is invariant under the later evolution: τ_n R = R. Then ⟨R; τ_n R⟩ = Var(R) for all n.
  - Equivalently, [R] lies in the commutant of T̂. Either R is a.s. constant on the physical space, or ker H ⊋ span{Ω}.
  - So record readouts must be **superselection labels** (central, conditioned on) and *cannot* be the dense family in A2.
  - Any "clustering of permanent records" can therefore only mean *spatial* clustering of the record configuration, or clustering of non-record gauge observables *conditioned on* a record configuration.
  - Converting spatial clustering into temporal clustering needs the supplied space–time hypercubic symmetry, which the Lattice axiom (spatial Z^3) does not provide.
- **Remark (structural parallel, not an estimate).** "Locks exactly one admissible local possibility" parallels a *hard constraint* on a block variable (δ-function blocking, the approach #10132 takes). "Permanent" parallels the RG convention that coarse variables, once fixed, are conditioned on while fine ones are integrated out. This motivates reading records as RG block variables, but it supplies none of the bounds in IH(k).

### 0.6 Two scope tests on any "Record ⇒ CW" input (tests, not no-go theorems)

These are scope tests a candidate input must pass. They are not global no-go or route-exhaustion claims (APPROACH_REGISTRY policy).

1. **Gauge-group agnosticism.**
   - Record (and the other three axioms) never mentions the gauge group. A mechanism deriving CW from Record without using non-abelian structure would apply equally to compact U(1) Wilson theory in d = 4.
   - That theory has a proved massless (non-confining) weak-coupling phase: Guth, Phys. Rev. D 21 (1980) 2291; Fröhlich–Spencer, CMP 83 (1982) 411. Such a mechanism would therefore prove a false statement for U(1); the test is that a correct mechanism must use structure U(1) lacks.
   - Repo support: `docs/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_DECONFINED_AND_UNORDERED_AT_L_12_…_BOUNDED_NOTE_2026-09-04.md` reports, by its title, a framework-native spin-½ link model that is gapless and deconfined at L = 12. That is finite-size evidence, not a theorem, and I read the title only.
   - **Scope consequence:** a correct H-Rec must use input that fails for U(1) in d = 4 (e.g. non-abelian, asymptotically free structure). Record as written, which never mentions the group, does not by itself supply such input.
2. **Dimension agnosticism (Heuristic).** A d-independent mechanism would also give a gap for SU(N) Wilson theory at weak coupling in d ≥ 5. There, a bulk transition and a weak-coupling Coulomb-like phase are expected. Expected only: this is supported by numerics, not proved, so it is a heuristic check. The Lattice axiom fixes Z^3 spatial, so this check is weaker than the first, and it only suggests that CW must use d = 4 marginality.

### 0.7 Circularity flags

- **C1.** Imposing block-unit decay (iv) at every RG scale is false in the weak-coupling region, or, if weakened to hold in physical units, is MG1 itself.
- **C2.** "Record clustering uniformly in a" in physical units *is* MG1 + MG3. Stating it as an axiom would be adopting the mass gap as an axiom. That violates the repo's own firewall convention of adopting no premise.
- **C3.** Using a lattice gap at β ≤ β_sc for the continuum is the wrong end of the trajectory. m_lat(β) = −log(cβ) is large in lattice units at strong coupling, while the continuum limit needs β → ∞ (§2(e)).
- **C4.** The repo's `SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md` reduces a fixed-lattice β = 6 gap to "No second-order bulk critical point … in 0 < β ≤ 6". It is honest that this premise "remains the open Balaban-class / RG-control problem". CW contains that premise, extended uniformly along the trajectory. Do not cite the β = 6 note as evidence for CW.
- **C5.** Both ASTRA mass-gap notes in #10114 are "same-family" reviewed. Treat them as supported only, not as independently verified.

### 0.8 Mapping onto PR #10114's physical gap obligation

Quoted from #10114 `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_TARGET.md` @ `f76f6c64`:

> Target: "Prove a number m_*>0, in fixed physical units, such that ker H = span{Ω}, spec(H) ⊂ {0} ∪ [m_*,∞), with a nonzero excited sector".
> §2 (MG1): "0 ≤ C_F(t) ≤ A_F exp(-m_* t), t≥t_F" … "A_F and t_F may depend on F; m_* must not."
> §3: constants independent of UV cutoff and volume for t_F ≤ t ≤ T_safe(volume); "No interchange of an uncontrolled t→∞ limit with cutoff removal is allowed."
> Ledger rows: MG0 existence and reconstruction (Open); MG1 infrared estimate — "Uniform exponential reflected-correlation decay for a dense observable family, or an equivalent physical transfer-operator gap" (Not constructed); MG2 source transport (Open); MG3 cutoff/volume passage — "Uniform physical rate, prefactors and onset time on the same trajectory" (Open); MG4 non-trivial excited sector (Open); MG5 final theorem scope (Open).
> Suggested mechanism (§3): continue the effective action to a fixed physical coarse scale reaching "a provable strong-coupling cluster regime; this needs a quantitative crossover theorem".

| #10114 row | What Theorem H does | Discharged? |
|---|---|---|
| MG0 existence/reconstruction | Uses it as a hypothesis for the continuum statement. Supplies lattice-level OS reconstruction (A1, A3) at each a | **No** (lattice level only, already standard) |
| MG1 infrared estimate | Reduces it to CW + B4 via A2. A2 is exactly #10114 §2 | **No.** Reduced to the single estimate CW |
| MG2 source transport | Names it as Step B4. Notes RP of S_k is not needed | **No.** Open, sharpened |
| MG3 cutoff/volume passage | m_* = μ_*/ℓ_* is a-independent *if* CW holds. A3 gives the fixed-t-first volume passage | **Conditionally.** Follows from CW + H5–H6 |
| MG4 excited sector | Not addressed. See #10132 NT1 (§6) | **No** |
| MG5 scope | Theorem H is stated with hypotheses as a conditional reduction | Draft text below |
| (fixed-spacing endpoint, already in #10114) | A1–A4 reproduce it for all N at β ≤ β_sc. A1 adds the assembly from the repo's kernel-positivity facts | Already supported in #10114 |

**Net:** the hybrid discharges no open MG row unconditionally. It gives a precise reduction MG1 + MG3 ⇐ CW + B4 (+H5, H6). It also records three points that #10114 does not yet state: Observation P (proved), the U(1) scope test on group-agnostic inputs (cited; the d≥5 version is Heuristic), and the fact that effective-action RP is unnecessary.

### 0.9 The single biggest open step

**CW, the quantitative weak-to-strong crossover.** It requires a uniform-in-volume exponential clustering bound, with rate μ_* > 0 in physical units, for the effective gauge theory at the fixed physical scale ℓ_1 ~ 1/Λ where Balaban's small-coupling control ends. Equivalently, it requires a provable Dobrushin/cluster regime reached after finitely many further RG steps.

This is the mass gap at intermediate coupling: absence of a bulk transition plus a finite correlation length, made quantitative. Record as written does not supply it (§0.5), and a group- or dimension-agnostic input would fail the scope tests of §0.6.

---

## 1. Setup

### 1.1 Axioms (verbatim excerpts, `docs/MINIMAL_AXIOMS_2026-06-29.md`)

- **Lattice:** "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site. No site is privileged…"
- **Qubit:** "Each site has a domain of local possibilities. The full one-site possibility domain has algebraic presentation `M_2(C)`. A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently…"
- **Admissibility:** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations. For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
- **Record:** quoted in §0.5.
- The memo also says "A state is a configuration of records." It lists dynamics, the time metric, the source/action and `g_bare = 1` as open, outside the axioms.

### 1.2 Discrete YM model

This is the Wilson model of §0.1. Supplied items:

- the action;
- β (the repo's `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` treats g_bare = 1, i.e. β = 6 for SU(3), as a convention, and the memo says it is an open gate);
- the 4th (time) direction;
- link variables.

A qubit-regularized alternative exists in the literature (Chandrasekharan–Siew–Bhattacharya, arXiv:2502.14175). *Heuristic:* there, a finite link Hilbert space generally changes the universality class. The repo's spin-½ link model note is an instance. A qubit-native route would therefore need its own asymptotic-freedom argument rather than Balaban's (Heuristic).

### 1.3 SU(3) from GRAPH_FIRST_SU3

`docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` (2026-04-12, "BOUNDED-proposed_retained"; ledger: unaudited) works as follows:

- On the taste cube {0,1}^3 with a selected axis, there are 2-point fibres (giving weak su(2)) and a 4-point base that the swap splits as 3⊕1.
- The commutant is gl(3)⊕gl(1), with compact part su(3).
- This is an **internal/taste** symmetry algebra. It is not a dynamical link connection and does not produce the Wilson action.
- Repo firewalls: `archive/notes/docs/QUARK_ROUTE2_GRAPH_FIRST_SU3_SPATIAL_COLOR_BRIDGE_GATE_NO_GO_NOTE_2026-06-21.md` and the associated functor-firewall note.
- Its runner `frontier_non_abelian_gauge.py` is recorded with FAIL=4 (audit-tier pins) in `physics-campaign/ISSUES_REPORT.md` (around line 509).

Conclusion: GRAPH_FIRST fixes *which* group to put on links. The step "internal su(3) ⇒ SU(3) link gauge field with Wilson action" is an open bridge. Theorem H is stated for general SU(N) and does not depend on it.

## 2. Lemmas

**(a) Record ⇒ exponential clustering.**

- *Not available.* The axiom contains no clustering, mixing or dynamics content (§0.5).
- Observation P (proved; MASS_GAP_CROSSOVER_REDUCTION Lemma 5.5) shows that a non-constant time-invariant record readout cannot have decaying reflected correlations, so record readouts are superselection labels.
- What would be needed is a new hypothesis H-Rec: exponential decay of truncated correlations of gauge-invariant (non-record) local observables, conditioned on any record configuration, with rate and constants uniform in the volume and the configuration.
- At fixed β ≤ β_sc this is true and known (H4), with Record playing no role. Along the continuum trajectory it is CW.

**(b) Reflection positivity.**

- *What the repo proves (unaudited):*
  - the two-slice temporal-gauge Wilson Gram is PSD for β ≥ 0 (06-05 bridge, repaired 07-16);
  - the SU(3) one-link kernel character coefficients are c_λ(β) ≥ 0 (05-30);
  - staggered fermion two-step RP: T̂² = B†B in the free case, with single-step spin-basis RP non-PSD (min eigenvalue −0.80) (04-29). The 04-29 gauge case is only a "reduction target".
- *The "half" note* (`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`) proves ⟨Θ(F)F⟩ = ‖ψ²F‖² ≥ 0 under the assumption that S_+ is Θ-invariant. It is an identity with no half-space decomposition, and the note itself disclaims the Osterwalder–Seiler theorem.
- *Missing in the repo:* multi-slice/periodic RP, the transfer-matrix construction, site-reflection RP, the infinite-volume limit, and any RP statement for a record-modified measure.
- Lemma A1 (§0.4) shows the multi-slice lattice statement follows from the two repo facts plus standard operator theory (Lüscher 1977). It is a small, honest addition.

**(c) Transfer matrix T = e^{−aH}: gap ⇔ exponential decay.**

- ⇒ is the repo's 05-09 bridge on finite blocks.
- ⇐ is A2 (#10114 §2). It needs a dense family, which OS reconstruction supplies at fixed a.
- In finite volume, a simple top eigenvalue comes from k_β > 0 (Jentzsch).
- `OSTERWALDER_SCHRADER_FROM_FRAMEWORK_NARROW_THEOREM_NOTE_2026-05-27.md` is only the finite-dimensional spectral identity T̂^n = e^{−n a_τ H}. It is conditional on unaudited parents.

**(d) Uniformity in volume.**

- Holds at β ≤ β_sc: by cluster expansion; in #10114's Doob contraction (SU(2), β ≤ 1/32); and for the repo's Yarotsky-import Hamiltonian gap (av small, unspecified constants).
- Thermodynamic passage by A3 (fixed-n bounds first).
- In the crossover window: open, and part of CW. Uniqueness of the infinite-volume state is not known there either.

**(e) Continuum.**

- The critical tuning is g_0(a) → 0 with g_0^{−2} ≈ b_0 log(1/(aΛ)) + …. Then m_phys = m_lat(β(a))/a.
- We need m_lat(β(a)) ≥ m_*·a, i.e. a lattice correlation length ξ(β(a)) ≤ 1/(m_* a). That means the *correct* (asymptotic-freedom) divergence of ξ, not more.
- Strong-coupling clustering says nothing here, because it only holds at β ≤ β_sc, while the trajectory has β → ∞.
- OS axioms needed for the limit: OS0 (regularity/temperedness), OS1 (Euclidean invariance; only hypercubic invariance is automatic), OS2 (RP; closed under limits), OS3 (symmetry), OS4 (clustering, which follows from the gap).
- Reconstruction (Osterwalder–Schrader, CMP 31 (1973) 83 and CMP 42 (1975) 281) then gives (ℋ, H, Ω).
- **This is the Millennium-level obstruction.** For Record to help, it would have to supply scale-uniform clustering in physical units, i.e. CW. §0.5 shows the axiom as stated contains no such clause, and §0.6 gives the scope tests any strengthening must pass.

## 3. Assumptions (tagged)

| # | Assumption | Tag |
|---|---|---|
| 1 | Wilson SU(N) action, 4th dimension, β trajectory supplied | supplied (outside axioms; memo lists as open gates) |
| 2 | Two-slice RP Gram PSD, c_λ(β) ≥ 0 | proved-in-repo (unaudited) |
| 3 | Full lattice RP, positive transfer matrix | standard-literature (Osterwalder–Seiler 1978; Lüscher 1977). Assembly from repo facts in A1 |
| 4 | Gap ⇒ clustering (finite block) | proved-in-repo (unaudited, 05-09) |
| 5 | Clustering on a dense family ⇒ gap | standard (spectral theorem). Written in #10114 §2 |
| 6 | Strong-coupling volume-uniform gap | standard-literature (Osterwalder–Seiler). #10114 local-block note (same-family review). Repo packet bound |
| 7 | Balaban UV stability, finite volume, g_k ≤ ḡ | standard-literature (Balaban CMP 95–122; credited in #10132) |
| 8 | Flow reaches ḡ at physical ℓ_1 ~ 1/Λ | plausible, unwritten |
| 9 | Source transport (B4, MG2) | plausible, unproved |
| 10 | Infinite-volume limit of Balaban's control | open (not in Balaban) |
| 11 | **CW crossover clustering** | **irreducible open** |
| 12 | H-Rec (Record clustering) | conjecture, not adopted. Must pass the scope tests of §0.6 |
| 13 | Continuum existence MG0, O(4), non-triviality MG4 | open (#10132 targets T1, NT1/NT2 for SU(2)) |
| 14 | GRAPH_FIRST su(3) ⇒ link SU(3) | open bridge, with repo no-go notes |

## 4. Blockers (ranked) and next steps — Remarks

1. **CW crossover (decisive).** There is no small parameter between Balaban's ḡ and the cluster regime β_sc. *Next:* quantify the window, i.e. compute what ḡ Balaban-type bounds could at best reach versus what effective one-block Dobrushin condition (#10114's r(β) < 1 test) would be needed. That turns "the window" into a number, even if closing it is out of reach.
2. **Infinite volume plus gauge-invariant correlators in RG (MG2, MG3).** Balaban works on a finite torus and controls the partition function and effective actions, not general correlation functions. *Next:* a source-carrying version of B1 for smeared Wilson loops of physical size ≥ ℓ_*.
3. **Uniformity in a.** Even granting a gap at each a, prefactors and onset times must be uniform along the trajectory (MG3). Strong-coupling bounds have the wrong scaling.
4. **Non-triviality and excited sector (MG4).** A gap with an empty Ω^⊥ is vacuous. This is the job of #10132's witness part (NT1/NT2).
5. **Rotation invariance.** This is needed for Clay-level OS1, not for the gap bound. It is open.
6. **Osterwalder–Seiler already gives the lattice gap at strong coupling.** Any claim that Record "induces" it is redundant. State it as known.
7. **Circularity** (§0.7). Any axiom-level clustering in physical units is MG1.

## 5. PR contribution

The note drafted here is committed as [MASS_GAP_CROSSOVER_REDUCTION.md](MASS_GAP_CROSSOVER_REDUCTION.md), with an [APPROACH_REGISTRY.md](APPROACH_REGISTRY.md) row. The registry wording follows its policy: the U(1)/d ≥ 5 point is recorded as a scope test for CW producers, not as a global no-go. The #10132 interface note is `library/mass-gap-interface.md` on branch `claude/ym4d-hard-route`.

## 6. Hybrid routes (beyond Theorem H) — Remarks/Heuristics only

- **Record → Balaban small/large-field control.**
  - Record's "one record per site, locked" can be read as a hard constraint on block variables, the same structural choice as #10132's hard-constraint route.
  - It supplies none of the analytic bounds (polymer decay, large-field suppression). Those are Balaban's theorems.
  - *Closes:* none of Balaban's gaps (infinite volume, gauge-invariant correlators, mass gap).
- **Record → uniform polymer bounds.** Polymer bounds are locality of the action. Record says nothing about the action, so this closes nothing.
- **Record → scale-uniform clustering at each RG step.** False at weak coupling, or circular (§0.4 B0, C1).
- **Record → final strong-coupling cluster expansion.** Once a cluster regime is reached, standard expansions apply with no Record input. The problem is *reaching* it (CW).
- **Record + RP + chessboard estimates.**
  - RP gives chessboard bounds (Fröhlich–Israel–Lieb–Simon 1978). These bound the probability of many simultaneous large-field plaquettes by a product of single-plaquette quantities.
  - Useful for large-field suppression at the bare level, and for Peierls-type arguments, which prove *ordering* rather than decay.
  - Chessboard needs RP of the measure being estimated. That holds for the original Wilson measure, but not generally for Balaban's effective measures.
  - *Closes:* none of the main gaps. A possible technical aid inside B1.
- **Record + Magnen–Rivasseau–Sénéor.**
  - MRS (CMP 155 (1993)) construct SU(2) YM_4 with an infrared cutoff, in a continuum-regularized, gauge-fixed (non-lattice) setting.
  - Their framework handles correlation functions in finite volume, where Balaban does not.
  - It has no RP from a lattice, gauge-fixing issues (Gribov copies, handled by their cutoff), and the IR cutoff is exactly where the mass gap lives.
  - A hybrid "MRS in finite volume plus an IR clustering input" again needs CW. Record adds nothing specific.
- **Record + Hamiltonian stability (repo-native).**
  - The repo's Yarotsky-import note gives a volume-uniform gap in the electric-dominated (strong-coupling Hamiltonian) regime, with unspecified constants. That is the Hamiltonian twin of H4.
  - Same limitation: the wrong end of the trajectory.

## 7. Relation to PR #10114 and #10132

**#10114** "[physics-loop] ym4d open_gate — existence and mass-gap proof work".

- Head `f76f6c64`, created 2026-10-28 07:46 EDT. Soft-kernel route, SU(N), currently paused.
- Mass-gap material:
  - `MASS_GAP_TARGET.md`: MG contract, quoted in §0.8.
  - `MASS_GAP_LOCAL_BLOCK_ASTRA.md`: for 0 < β ≤ 1/32, Doob contraction r(β) = β/[1−Q(β)] with Q = 12β + β²/(1−14β), r ≤ 18/359. Gives |Cov_π(F,P_0^n F)| ≤ (1/4)[Σ_e δ_e F]² r^n, so spec(H_Γ) ⊂ {0}∪[−log r(β)/a,∞), uniform in spatial volume and slab depth. Self-stated: "Its cutoff dependence prevents using it as the requested continuum theorem."
  - `MASS_GAP_CONSTRUCTION_ASTRA.md`: a finite-volume gap that loses volume uniformity.
  - Both ASTRA notes have same-family reviews.
- **Relation:**
  - *parallels* it on step (A), which is already there for SU(2) and needs no Record;
  - *strengthens* it by turning §3's crossover mechanism into a theorem-with-hypotheses with a single open estimate CW, plus the three scope points of §0.8;
  - *no conflict.*
- **Recommend** the file in §5.

**#10132** "docs(ym4d): hard-constraint route to SU(2) existence (working draft)".

- Head `69154762` when read, created 2026-10-30 16:31 EDT; rechecked at `5ad46ff7`, with no change to the witness material.
- Witness part (`parts/witness.md`, as of the pinned head):
  - NT1: H ≠ 0 on Ω^⊥.
  - NT2: correlators match leading perturbative order, including the three-gluon vertex, with g_r running at the one-loop rate.
  - Settled: odd test T = ½Tr(W1W2W3) − ½Tr(W1W3W2) with non-vanishing tree coefficient (K_total = 0.6157, of which K_vert = 0.2188); no translation-invariant Gaussian potential reproduces the Wilson tree values in d = 4 (Thm 3.8); Thm 3.16 on a box of side 23; Monte Carlo at β = 16 with blocked separation 4.8σ.
  - Open: (RANK-U), colour-mixing gauge parts, link variance above g^{4/3}, hard-core inputs uniform in j.
- **Relation:**
  - *parallel/complementary.* #10132 targets existence and non-triviality (MG0/MG4 territory for SU(2)); this sketch targets MG1/MG3.
  - Gap plus a non-empty Ω^⊥ ⇒ NT1, and the NT1/NT2 witnesses supply that non-emptiness (MG4). This holds only on a common trajectory and observable family.
  - *No conflict.* The witness charter's warning against dimension-independent strategies for NT2 is consistent with the scope tests of §0.6.
- **Recommend** a short interface note (§5).

## 8. Material found / not found

- **Found:**
  - the axioms memo;
  - GRAPH_FIRST_SU3 (taste su(3) only), plus its no-go/firewall notes;
  - the RP notes (two-slice Wilson Gram, kernel positivity, staggered two-step, trivial "half" note);
  - the gap ⇒ clustering bridge;
  - the native strong-coupling packet gap;
  - the β = 6 bulk-criticality reduction;
  - the Yarotsky-import Hamiltonian gap;
  - the finite-dimensional OS spectral bridge;
  - records-only OS on a two-slice Grassmann toy;
  - both PRs' mass-gap and witness material at their pinned heads.
- **Not found:**
  - any Record ⇒ clustering result;
  - multi-slice interacting RP or a transfer matrix on the full lattice in the repo;
  - any link-gauge SU(3) derived from GRAPH_FIRST;
  - any RG/Balaban-type estimate in the repo;
- **Not read in detail:** #10132 hard-core commits after `69154762` (checked for relevance only). The pure spin-½ link model note was read by title only.
