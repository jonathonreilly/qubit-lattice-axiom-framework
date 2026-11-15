# YM4D existence from UV stability: a conditional lemma DAG (sessions 1-3, 2026-10-27)

Session 3 applied the 12 binding fixes of REVIEW_X1_X2.md (each tagged **[RX12-fix]**), relabelled every hypothesis by
provenance, and added §11 (large-field localisation H-loc-LF; X-WIL literature) and §12 (current honest public
statement). Sessions 1-2 text is otherwise unchanged; EXISTENCE_session2_snapshot.md is the pre-fix copy.

Lane: layer 2 of the 4D Yang-Mills construction. Layer 1 (UV stability, Balaban's RG) is the sister lane
`../ym4d-proof/` (read-only here; cited as **P**, with P's lemma names). Nothing here is a PR, a CL entry or an axiom
edit. Literature tags are in NOTES.md. The session record is in LOG.md.

**Status legend** (same as P):
- **PROVEN-HERE**: the complete argument is written in this file. "PROVEN-HERE | H" means it is a proven implication
  from the named hypothesis H.
- **IMPORTED-AND-REVERIFIED**: exact source; the load-bearing step re-derived or re-checked on our setting.
- **IMPORTED-NOT-YET-REVERIFIED**: a named obligation that a source states. It never supports a PROVEN claim except as
  an explicit hypothesis. **[RX12-fix 1]** Reserved for statements a source states.
- **HYPOTHESIS (new; no source)** **[RX12-fix 1]**: a hypothesis this lane formulates and no read or cited paper states.
  It supports PROVEN claims only as "PROVEN-HERE | H".
- **Provenance labels [RX12-fix 1]** (on every hypothesis, as REVIEW_X1_X2 §1 classifies them):
  *Balaban states it* (a read or cited Balaban text states it; proof possibly unseen) / *plausible extension of
  Balaban* (not stated; a natural extension of what is stated) / *new hypothesis* (no source states it).
- **OPEN**: the missing estimate is stated.
- **ARGUED**: a heuristic or perturbative reason, uncounted.
- **STANDARD**: a textbook theorem of analysis/topology used as a tool (Banach-Alaoglu, Riesz, Montel, Minlos,
  continuous mapping theorem, uniqueness of positive roots). Uncounted; named where used.

---

## 0. Summary

**Structural remark [RX12-fix 11].** Every non-soft conclusion rests on hypotheses that no published paper states
(sessions 1-2: H-Bal-3 in its full-law packaging, -3G, -3L, -3T, -loc; session 3, §11: H-loc-LF, H-Bal-3T, H-Bal-loc).
The published Z-stability theorem (H-Bal-2) is not sufficient for them and is not used. The only Balaban statements used
are the small-field *form* of the effective action (H-Bal-3(3a), for the small-field RG) and the coupling flow
(H-Bal-1, SU(2), proof deferred and unseen). What compactness gives for free, and what each extra hypothesis buys:

| Part | Delivered | From |
|---|---|---|
| (a) subsequential continuum limits, finite volume | **YES**: a single limit state ω on a separable commutative C*-algebra containing every block observable (all resolutions, all L-adic shifts) and every flowed lattice Wilson loop; consistent across resolutions | compactness alone (X-ALG, X-CONS), with the **continuous** block map X-S4c |
| (b) OS structure | **RP** for every L-adic block-boundary plane, **L-adic translations**, hypercubic symmetry, gauge invariance; on R×T³: OS Hilbert space, positive contraction semigroup T(s) = T(2)^{s/2}, **Hamiltonian H ≥ 0 on (ker T)^⊥, which may be CΩ: possibly trivial without (c)-type input [RX12-fix 10]** (standard dense-lattice-time OS argument; not new) | lattice RP (Osterwalder-Seiler, re-verified) + compactness (X-RP, X-OS) |
| (b) not delivered | time continuity (ker T = 0), rotation invariance (OS1), OS0 for local fields | need H-cont, H-rot, H-src (OPEN; not in Balaban). Session 2: ker T ⊥ everything supported off the plane (X-KER); two-grid laws = one resolution's law + one two-grid step (X-2GRID); estimate proven in the free Gaussian model (X-CONT-G); interacting case ⇐ H-corr + H-lin (ARGUED). Sources: separated-support correlations of the action density bounded **| H-Bal-loc** (X-SRC-CT, X-SRC-RED) |
| (c) non-triviality | **weak form YES, given H-Bal-1 and H-Bal-3 (full-law packaging: new hypothesis; session 3: given H-loc-LF, §11)** [RX12-fix 11]: at every resolution the limit block law is neither flat nor Haar, and on small fields it has a density of Balaban's form with an analytic effective action; Taylor coefficients of order n are O(g^n) | X-ND, X-MONTEL, X-CAUCHY |
| (c) AF-type running of the block plaquette, given the flow hypothesis (session 2) [RX12-fix 11] | **given H-Bal-1, H-Bal-3L, H-Bal-3T (new hypotheses; session 3: given H-Bal-1, H-loc-LF, H-Bal-3T, §11), two-sided, volume-uniform**: (δ_*/2)/(1/g² + β'm log L) ≤ ω(1 - P_{p,m}) ≤ φ(G_m), so block plaquettes approach the free value logarithmically in the scale (not dilation invariant, no power law) | X-NTAF, X-NTAF-AF **| H-Bal-1, H-Bal-3L, H-Bal-3T** (§10.1) |
| (c) not delivered | non-Gaussianity (connected 4-point ≠ 0); the sharp coefficient c_blk g_m² with g_m² ~ 1/(2b_0 m log L) | OPEN (X-NT2; X-NTAF-sharp: walls W-AF1 flow coefficient, W-AF2 = H-corr) |
| (d) infinite volume | limit points exist with all of (b)'s soft structure; non-degeneracy **| H-Bal-3G** (volume-uniform Gibbs/finite-energy form; new hypothesis); session 3: not flat and not Haar **| H-loc-LF** (X-IVND', §11) | X-IV, X-IVND, X-IVND' |
| (d) not delivered | uniqueness, clustering (OS4), mass gap, rotation invariance via universality | OPEN (IR; need a gap or cluster expansion) |

**Tally (session 3): PROVEN-HERE 29 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 (H-Bal-1, H-Bal-2,
H-Bal-3(3a)-form) / HYPOTHESIS-NEW 3 (H-loc-LF, H-sg, H-Bal-loc) / OPEN 11.** After the 12 binding fixes alone (session 3
step 1) the tally was the review's corrected one: 24 / 1 / 3 / HYPOTHESIS-NEW 5 (H-Bal-3 full-law packaging, -3G, -3L,
-3T, -loc) / 11. §11 then adds 5 PROVEN-HERE items and replaces 4 new hypotheses by H-loc-LF + H-sg. (Session 2 claimed
24 / 1 / 7 / 11 with the new hypotheses mislabelled as imported; session 1: 16 / 1 / 4 / 9.) Itemised in §6. Session-2
work is §9-§10; session 3 is §11; the reader's trust list is §10.4; the public statement is §12.
- **Session-3 rows of the table:** (c) weak form and the lower bound of (c)-AF, (d) non-degeneracy: given H-Bal-1 and
  H-loc-LF (§11.3-11.4); the upper bound of (c)-AF additionally given H-sg.

---

## 1. Setting (fixed)

- **ES1 (lattice).** L odd (CMP 109 (0.1) takes L odd and large; P transcribes "> 11"). K ∈ N, ε = L^{-K}.
  Physical units: the resolution-0 (unit) lattice has spacing 1. Fine torus Λ_K = (εZ / ℓZ)^4 with ℓ = 4L^M
  (time side ℓ_0 may differ, also a multiple of 4; P's convention [S4]). Resolution-m coarse lattice
  Λ_m = (L^{-m}Z / ℓZ)^4 for 0 ≤ m ≤ K. **For fixed m and fixed ℓ, Λ_m is a finite lattice independent of K.**
  Balaban's step index is k = K - m (k counts steps from the fine lattice; CMP 109 p.255-256).
- **ES2 (measure).** G = SU(N), N ≥ 2. μ_K = Z_K^{-1} exp(-(2N/g_0²) Σ_p (1 - N^{-1} Re tr U_p)) Π_b dU_b (Haar).
  Config space Ω_K = G^{links(Λ_K)}, compact.
- **ES3 (tuning).** g_0 = g_0(ε, g), the bare coupling of H-Bal-1 with renormalised coupling g at the unit scale.
  (Not P's S5' renormalisation condition; the tuning is part of the hypothesis.)
- **ES4 (block map).** The continuous averaging map S4c of Lemma X-S4c, iterated: V^(m)_K := A^{K-m}(U) ∈
  C_m := G^{links(Λ_m)}. On small fields it equals P's S4', a **diagonal-pairing variant of Balaban's (0.4)** (P, B-avg,
  check c17(B); the two differ at second order; Balaban p.254: "we may use many other definitions") [RX12-fix 3]. Shifted grids: for a ∈ D := ∪_m L^{-m}Z^4 (the L-adic translations), V^(m)_{K,a} is the same map on
  the grid translated by a (defined for K ≥ m(a), the level of a).
- **ES5 (observables).**
  - **O^blk** (block observables): f(V^(m)_{K,a}|_X), f ∈ C(C_m(X)) gauge-invariant under coarse gauge
    transformations, X a finite union of resolution-m blocks. Includes Wilson loops *of the block variables*
    ("smoothed Wilson loops" in the sense of Magnen-Rivasseau-Sénéor, NOTES §2).
  - **O^flow** (flowed lattice Wilson loops): W_{t,γ}(U) = N^{-1} Re tr Hol_{V_τ(U)}(γ), γ a closed loop of the
    resolution-m coarse graph (refined to fine straight segments), V_τ the Wilson flow (Lüscher (1.4), NOTES §4) at
    lattice flow time τ = t/ε², t ∈ Q_{>0} physical.
  - **O^raw** (raw lattice Wilson loops of physical size): excluded, see X-RAW.
  - **Unbounded fields** (smeared composites, flowed energy density): only in §4 (OS0).
- **ES6 = Lemma X-PLANES (reflections; PROVEN-HERE).** P_m := {x_μ = (j + ½)L^{-m}} (resolution-m block-boundary hyperplanes; link mid-planes of
  every finer lattice). Since L is odd, (j + ½)L^{-m} = ((jL + (L-1)/2) + ½)L^{-m-1}, so **P_m ⊂ P_{m+1}**;
  P := ∪_m P_m is dense in each coordinate.

---

## 2. The hypothesis H-Bal (exact form used; every quantifier explicit)

Sources: CMP 109 [read by P, NOTES §1 here]; CMP 102, 116, 119, 122 I-II [not-read; abstracts/Crossref only].
Everything below is **[unverified-exact-statement]** except where marked as transcribed from CMP 109.

**H-Bal-1 (coupling flow). IMPORTED-NOT-YET-REVERIFIED.** (CMP 109 Theorem 2 and (0.31), transcribed by P; stated
for SU(2), "superficial" for SU(N); its proof is deferred by Balaban to "a separate paper".)
**Provenance [RX12-fix 1, 2]:** for SU(2), *Balaban states it*; **the proof was never seen by either lane** (Balaban
defers it to a separate paper, P NOTES §9.4). For SU(N), N ≥ 3: *plausible extension* (Balaban calls the restriction
"superficial", which is not a proof). **Volume uniformity [unverified; plausible extension]:** the uses "uniformly in
the volume" (X-NTAF) and the infinite-volume reading of X-IV need g_0(ε, g), γ, β, β' to be **independent of the torus
side M** (and of the time side). This is plausible because β_j is defined after T → Z^d (CMP 109 (1.22)), but CMP 109
Theorem 2 does not state it. It is added here as part of H-Bal-1.
There are γ > 0, g_1 > 0 and 0 < β ≤ β' such that for every g ∈ (0, g_1] and every K ≥ 0 there is a bare coupling
g_0(ε, g) for which the effective couplings satisfy g_k ∈ (0, γ] for k = 0, ..., K, g_K = g, and
1/g² + β(K - k) log L ≤ 1/g_k² ≤ 1/g² + β'(K - k) log L.
- Consequence used below: at a fixed physical resolution m (k = K - m), g_{m,K} := g_{K-m} lies in
  [(1/g² + β' m log L)^{-1/2}, γ], a compact subinterval of (0, γ], **independent of K**.

**H-Bal-2 (UV stability of Z). IMPORTED-NOT-YET-REVERIFIED.** (CMP 122 II, per its OSTI abstract "completing the
proof of the ultraviolet stability of four-dimensional pure gauge field theories" [read-abs, via P].)
**Provenance [RX12-fix 1]:** *Balaban states it* (in some form; the two-sided e^{±E|T|} form below is the standard
reading, not a transcription). Unused.
For g ≤ g_1 and g_0 = g_0(ε, g): there are E_± = E_±(g, L, N) < ∞, **independent of K and of M**, such that
e^{-E_-|T|} ≤ Z_K / 𝒩_K ≤ e^{E_+|T|}, |T| = ℓ^4 the physical volume, 𝒩_K an explicit normalisation (products of
the Gaussian and Faddeev-Popov normalisations of the steps (0.17); exact form unverified).
- Quantifier status: CMP 109 (0.1) allows the torus side 2L^m (any m) in unit-lattice units, so nothing in the
  small-field theorem restricts the physical volume (P, L6 [S6]); whether the full theorem is uniform in M is
  unverified.

**H-Bal-3 (block-variable laws at every scale; the inductive content). Split by provenance [RX12-fix 1, 3]:**
- **H-Bal-3(3a)-form**, the small-field form of the effective action *for the small-field-restricted RG* (0.17)-(0.20)
  (background action plus localised polymers with the (0.28)-(0.30) bounds, analytic, gauge invariant):
  IMPORTED-NOT-YET-REVERIFIED, *Balaban states it* (CMP 109 Theorems 1/3; induction completed in CMP 116, unread).
- **H-Bal-3 full-law packaging** ((3a) as the density of the law of the block variables of the **full** Wilson measure,
  with the multiplicative remainder (1 + R), for the S4c map; and (3b)): HYPOTHESIS (new; no source). (3a) for the
  full law with (1 + R), for S4c: *plausible extension*; (3b): *new hypothesis*. Balaban never states a representation
  of the full block law in any paper read by either lane; the abstract of CMP 109 says "The analysis is restricted to
  small field approximation" (P §9.1).
(Small-field form: CMP 109 Theorems 1/3, (0.22)-(0.29), (1.18), transcribed by P; its inductive step is completed in
CMP 116 [not-read]. Large-field part: the R-operation of CMP 122 I-II [abstracts only]. Background field: CMP 102
Theorem 1 [second-hand].) Fix m and put k = K - m, η = L^{-k}. Let ν_{K,m} be the law of V^(m)_K on C_m (finite
dimensional), ρ_{K,m} its density with respect to Haar measure on C_m, and
R_m(ε_0) := {V ∈ C_m : |V(∂p') - 1| < ε_0 for every coarse plaquette p'} (Balaban's coarse regularity condition,
CMP 109 p.259). There are ε_0, E_0, κ > 0, α > 0, η_0 ∈ (0,1), C_R < ∞ and C_A < ∞, **independent of K** (η_0 = η_0(m, ℓ)
may depend on m and the physical side ℓ: ν(R_m) decays exponentially in |Λ_m| [RX12-fix 3]), such that for all
K ≥ m:
- **(3a) small-field density.** On R_m(ε_0):
  ρ_{K,m}(V) = 𝒵_{K,m}^{-1} exp(-(1/g_{m,K}²) A^η(U_k(V)) + E_{K,m}(V)) (1 + R_{K,m}(V)),
  where U_k(V) is the regular background minimiser (CMP 102), E_{K,m} = Σ_X E_{K,m}(X) over polymers X (connected
  unions of coarse M-cubes) with E_{K,m}(X) gauge invariant; V ↦ A^η(U_k(V)) and every E_{K,m}(X) extend
  holomorphically to a complex neighbourhood R^c_m of R_m(ε_0) (fixed in coarse units; it contains, in a coarse
  axial or Landau gauge, all V = exp(iX)·V_flat with complex ||X||_∞ < α), with
  |E_{K,m}(X)| ≤ E_0 e^{-κ d(X)} and |A^η(U_k(V))| ≤ C_A |Λ_m| on R^c_m; R_{K,m} is the contribution of large-field
  histories at finer scales after the R-operation, with
  e^{-C_R|Λ_m|} ≤ 1 + R_{K,m} ≤ e^{C_R|Λ_m|} on R_m(ε_0)  **[RX12-fix 3; replaces session 2's |R| ≤ 1/2]**.
  - **Source of the polymer bound [RX12-fix 3].** The cumulative E_k = Σ_j[-β_jA^η + E^{(j)}] (CMP 109 (0.23)) is
    controlled only after the β-subtraction, by **(0.28)-(0.30)**: -β_j A^η + E^{(j)} = Σ_{X∈D_j}V^{(j)}(X) with
    |V^{(j)}(X)| ≤ O(1)(L^jη)^{4+α}e^{-κd_j(X)}, summing to |E_k| ≤ O(1)(1 - L^{-α})^{-1}M^{-4}|T_1^{(k)}|. Session 2 cited
    (1.18), which bounds the **single-step** terms E^{(j)}(X) only; k copies of (1.18) give kE_0, which is not K-uniform.
    Two parts of the polymer statement used here are **[unverified]** and belong to the hypothesis: (i) the regrouping of
    the fine-scale polymers X ∈ D_j (j ≤ k) into coarse polymers at resolution m with a single bound E_0e^{-κd(X)};
    (ii) the analytic extension of (0.29) from the regular domain to R^c_m with the same constant ((0.29) is given on
    the regular domain).
  - **Why |R| ≤ 1/2 was dropped [RX12-fix 3].** The naive count of fine large-field cubes diverges in 4D (P's
    Proposition LF-count). The large-field histories must be resummed into polymer activities, and the natural output
    is |log(1 + R)| ≤ C_R|Λ_m|. X-ND and X-MONTEL need only K-uniform two-sided bounds.
- **(3b) large-field mass.** ν_{K,m}(C_m \ R_m(ε_0)) ≤ η_0 = η_0(m, ℓ). *New hypothesis*: no read source bounds
  probabilities of the full measure; it is consistent only at fixed m and fixed volume. (Session 3: (3b) is no longer
  used; X-ND is re-proven from H-loc-LF without it, §11.4.)

**H-Bal-3G (volume-uniform Gibbs form; needed only for (d)). HYPOTHESIS (new; no source) [RX12-fix 1]** (no source
states it; it is what a Balaban-type representation with local polymers should give, and it is the content of P's E8*
at depth k). Session 3: superseded for (d) by X-IVND' | H-loc-LF (§11.4).
For every finite set Y of coarse links there are a non-empty open set O_Y ⊂ G^Y of regular local configurations and
c_Y > 0, **independent of K and M**, such that, outside an event of ν_{K,m}-probability ≤ η_0 |Y|, the conditional
density of V^(m)|_Y given V^(m)|_{Y^c} is ≥ c_Y on O_Y; and the Peierls bound
ν_{K,m}(|V(∂p'_i) - 1| ≥ ε_0 for i = 1..r) ≤ η_0^r for coarse plaquettes at mutual distance ≥ R_0.

**What H-Bal does not contain** (each named because a part of the theorem needs it):
- **H-src**: bounds on generating functionals with sources (unbounded fields), §4.
- **H-cont**: comparison of block variables on grids shifted by small a, uniformly in K, §4.
- **H-rot**: comparison of differently oriented lattices / universality, §4.
- **H-uniq**: uniqueness / decay of correlations in infinite volume, §5.

---

## 3. The soft layer and the (a), (b), (c) conclusions

### X-S4c. A continuous, gauge- and lattice-covariant block map with a diagonal-pairing variant of Balaban's small-field averaging exists. PROVEN-HERE
**Statement.** Fix 0 < r_0 < r_1 < 2π/N and a smooth φ: [0,∞) → [0,1] with φ = 1 on [0, r_0], φ = 0 on [r_1, ∞).
Put ψ(X) := φ(||X||_op) X on su(N), and λ(Z) := ψ(log Z) for Z ∈ SU(N) with no eigenvalue -1 (principal log),
λ(Z) := 0 otherwise. Define (notation of P's S4')
U'(X, X + e_μ) := S_{c_X} exp( (1/d!) Σ_σ L^{-d} Σ_{y∈B(X)} λ(S_{c_X}^{-1} T^σ_y) ).
Then: (i) λ: SU(N) → su(N) is continuous, so U' is a continuous function of the fine links; (ii) U' ∈ SU(N);
(iii) U' is gauge covariant; (iv) U' is covariant under block-aligned reflections and axis permutations; (v) U'
equals S4' (a diagonal-pairing variant of Balaban's (0.4), not (0.4) itself [RX12-fix 3]) whenever every ||log(S^{-1}T^σ_y)||_op ≤ r_0; (vi) it is
local (uses only links of B(X) ∪ B(X + e_μ) and the crossing links), as P's L0.
**Proof.** (i) The set C = {Z : -1 ∈ spec Z} is closed and conjugation invariant; on its complement the principal log
is continuous, so λ is continuous there. If Z_n → Z ∈ C with Z_n ∉ C, some eigenphase of Z_n tends to ±π, so
||log Z_n||_op > r_1 eventually and λ(Z_n) = 0 = λ(Z). Hence λ is continuous everywhere.
(ii) If λ(Z) ≠ 0 then ||log Z||_op < r_1 < 2π/N, so the eigenphases θ_j lie in (-2π/N, 2π/N); Σθ_j ∈ 2πZ and
|Σθ_j| < 2π force Σθ_j = 0: log Z, hence λ(Z), is traceless anti-Hermitian. An average of such is such, so the
exponential is in SU(N).
(iii) Under a fine gauge transformation h, S_{c_X} ↦ h(c_X)S h(c_Y)^{-1}, T^σ_y ↦ h(c_X)T^σ_y h(c_Y)^{-1}, so every
S^{-1}T ↦ h(c_Y)S^{-1}T h(c_Y)^{-1}. The principal log is conjugation equivariant off C, C is conjugation invariant,
and ||·||_op is unitarily invariant, so λ is conjugation equivariant and U' ↦ h(c_X)U'h(c_Y)^{-1}.
(iv) P's L9a' reversal computation uses only log(Z^{-1}) = -log Z and conjugation equivariance. Off C,
log(Z^{-1}) = -log Z (eigenphases negate inside (-π, π)); ψ is odd; Z^{-1} ∈ C iff Z ∈ C. So λ(Z^{-1}) = -λ(Z)
everywhere and the computation goes through verbatim. Axis permutations: P's S4' re-check (order set and reference are
permutation invariant) uses no property of log. (v), (vi): immediate. ∎
- **Consequence.** With S4c, every block observable at every resolution and every shift is a **continuous** function
  on Ω_K, and A: C_{m+1} → C_m is continuous. **P's branch-set discontinuity (S4'' with the odd branch rule) is a
  choice, not a necessity**, and the "price" P records under S5' (E8* needed to pass A through limits) disappears.
- **Caveat (load-bearing for H-Bal-3).** Balaban's papers define the averaging on regular configurations; which
  everywhere-defined extension his large-field analysis uses is [not-read]. H-Bal-3 is assumed **for S4c**. Since S4c
  agrees with (0.4) on regular configurations, only the large-field bookkeeping (CMP 122) could depend on the choice.

### X-ALG. A single limit state exists on a separable algebra of all block and flowed observables. PROVEN-HERE
**Statement.** Let I be the countable index set of generators (m, a, X, f) (f from a countable dense subset of the
gauge-invariant part of C(C_m(X)), a ∈ D) and (t, γ) (t ∈ Q_{>0}, γ a coarse lattice loop). For each K let π_K(i) ∈
C(Ω_K) be the corresponding observable (and the constant 1 for the finitely many K below the level of i). Let 𝔄 be
the C*-subalgebra of the ℓ^∞-product Π_K C(Ω_K) generated by the sequences (π_K(i))_K. Then 𝔄 is a separable,
unital, commutative C*-algebra; ω_K(F) := E_{μ_K}[F_K] are states on 𝔄; and there is a subsequence K_j with
ω_{K_j} → ω weak-*, for a state ω. By Gelfand duality, ω is a Radon probability measure on the compact metrizable
space 𝒳 := Spec 𝔄 (the "continuum configuration space").
**Proof.** Polynomials with rational complex coefficients in the generators are countable and dense, so 𝔄 is separable.
ω_K is positive and ω_K(1) = 1. The state space of a separable unital C*-algebra is weak-* compact (Banach-Alaoglu) and
metrizable (separability), hence sequentially compact [STANDARD]. ∎
- Every element of 𝔄 has well-defined Schwinger "functions": ω(F_1⋯F_n) = lim_j E_{K_j}[F_{1,K_j}⋯F_{n,K_j}]. This is
  part **(a)** for bounded gauge-invariant observables, in finite volume, with **no hypothesis at all**.
- Content-free alone (P's L7a remark stands): ω could be degenerate. (c) is where content enters.
- [RX12-fix 5] ω vanishes on the null-sequence ideal 𝔍, so it is a state on 𝔄_∞ = 𝔄/𝔍; the "continuum configuration
  space" used from X-CONS on is 𝒳 := Spec 𝔄_∞ (see X-CONS).

### X-CONS. The limit is consistent across resolutions; the block laws form a projective family. PROVEN-HERE
**[RX12-fix 5] Corrected setting.** Two corrections to the session-2 text. (1) *Quotient by null sequences.* With the
convention "constant 1 below the level", f ↦ F_f is not multiplicative or additive in 𝔄 itself (F_{f+g} - F_f - F_g =
(-1)_{K<m} ≠ 0), and F_{f∘A} - F_f ≠ 0 at K = m. Put 𝔍 := 𝔄 ∩ c_0(Π_K C(Ω_K)) (sequences whose sup norm tends to 0; a
closed two-sided ideal of 𝔄), **𝔄_∞ := 𝔄/𝔍**, and **𝒳 := Spec 𝔄_∞** (compact metrizable, a closed subset of Spec 𝔄).
ω factors through 𝔄_∞, because ω(F) = lim_j ω_{K_j}(F) and |ω_{K}(F)| ≤ ||F_K||_∞ → 0 on 𝔍. (2) *Coarse gauge lift.*
F_f is a generator only for **coarse-gauge-invariant** f. For general f ∈ C(C_m) put f̄ := ∫_{𝒢_m} f(h·V)dh (Haar
average over the compact coarse gauge group 𝒢_m = G^{Λ_m}) and define ν_{*,m} on C_m by ν_{*,m}(f) := ω([F_{f̄}]). This
is legitimate because each ν_{K,m} is coarse-gauge invariant: fine gauge transformations at the block centres act on
V^(m)_K as arbitrary coarse gauge transformations (X-S4c (iii)) and preserve μ_K, so ν_{K,m}(f) = ν_{K,m}(f̄) =
ω_K(F_{f̄}). Hence ν_{*,m} is the weak-* limit of the ν_{K_j,m} on all of C(C_m), and it is coarse-gauge invariant.
X-ND, X-MONTEL, X-IVND and §10-§11 use this lift; it is written once here.
**Statement.** For coarse-gauge-invariant f ∈ C(C_m)^{𝒢_m}, let F_f := [(f ∘ V^(m)_K)_K] ∈ 𝔄_∞. f ↦ F_f is a unital
*-homomorphism C(C_m)^{𝒢_m} = C(C_m/𝒢_m) → 𝔄_∞; let p_m: 𝒳 → C_m/𝒢_m be its dual map. Then A ∘ p_{m+1} = p_m
(A descends to orbit spaces by gauge covariance), (p_m)_*ω = ν_{*,m} on C(C_m/𝒢_m), and A_*ν_{*,m+1} = ν_{*,m} on all
of C(C_m).
**Proof.** In 𝔄_∞ the convention below the level is invisible (finitely many components lie in 𝔍), so f ↦ F_f is a
unital *-homomorphism. f∘A ∈ C(C_{m+1}) by X-S4c and is coarse-gauge invariant at resolution m+1 when f is at
resolution m (gauge covariance of A). (f∘A)∘V^(m+1)_K = f∘V^(m)_K as functions on Ω_K for all K ≥ m+1, so F_{f∘A} = F_f
in 𝔄_∞ exactly. Dualising gives A∘p_{m+1} = p_m and the push-forward identity on invariant functions. For general f,
(f∘A)‾ = f̄∘A (A intertwines the coarse gauge actions and the Haar averages), so A_*ν_{*,m+1}(f) = ω(F_{(f∘A)‾}) =
ω(F_{f̄∘A}) = ω(F_{f̄}) = ν_{*,m}(f). ∎
- **Comparison with P (L7a, §0 finding 1, S5' "Price").** P states that without E8* the per-resolution limits need not
  be consistent. That is true for the discontinuous S4''. With S4c, consistency is automatic. Even with S4'', the
  *state* ω on 𝔄 is automatically consistent (F_f is one element, whatever level represents it); only its
  representation by measures on C_{m+1} can fail, by the continuous mapping theorem exactly on ν_{*,m+1}(Disc A) > 0.
  So **E8* is not needed for existence of a consistent limit state**; it is a regularity statement.

### X-SYM. Symmetries of ω. PROVEN-HERE (using P's covariance computations, re-checked in X-S4c)
**Statement.** ω is invariant under the L-adic translations a ∈ D (mod ℓ), under the hypercubic group about a
resolution-0 block centre (on a torus with equal sides; on R×T³ the spatial hypercubic group and time reflections),
and every element of 𝔄 is gauge invariant (by construction).
**Proof.** μ_K is invariant under εZ^4 translations and the lattice hypercubic group. A translation by a ∈ L^{-m'}Z^4,
K ≥ m', maps the generator (m, b, X, f) to (m, a + b, X, f) and flowed loops to translated flowed loops (the flow
commutes with lattice symmetries, X-FLOW). Hypercubic covariance of S4c is X-S4c (iv). Hence ω_K∘α = ω_K for these
automorphisms α of 𝔄 for all large K, and the identity passes to the weak-* limit. ∎

### X-LRP. Lattice reflection positivity of the Wilson action, for bounded measurable functions. IMPORTED-AND-REVERIFIED
**Statement.** For a fine link mid-plane Π of Λ_K (and its antipodal plane), with θ the reflection and 𝔉_+ the bounded
measurable functions of the links strictly on the positive side, ω_K(θ(F)^* F) ≥ 0 for F ∈ 𝔉_+, when β ≥ 0.
**Source.** Osterwalder-Seiler, Ann. Phys. 110 (1978) [not-read here]; re-derived in P, L9a (scope extended to bounded
measurable F in [R4-fix]); mixed reflection L9a-m; exact Z2 check c4.
**Re-verification (this session).** I re-read P's proof (P l.4249-4266 at session 15): gauge-fix the crossing links to
1 by a positive-side gauge transformation; e^{-S} = e^{A_+}θ(e^{A_+}) Π_{crossing p} exp((β/N) Re tr(W_pθ(W_p)^†));
expand the crossing factors into Σ_α c_α G_α θ(Ḡ_α) with c_α ≥ 0; Haar factorises; θ preserves Haar. The argument
uses no continuity of F, so it covers 𝔉_+. Correct. On the torus, ℓ_0/2 = 2L^M ∈ εZ, and Π ∈ P_0 implies the antipodal
plane Π + ℓ_0/2 ∈ P_0 ⊂ P_K: both are link mid-planes, as required.

### X-RP. Reflection positivity of ω for every plane in P. PROVEN-HERE | X-LRP
**Statement.** For Π ∈ P and 𝔄_+(Π) the C*-subalgebra generated by the block generators all of whose blocks lie on the
positive side of Π (all resolutions and all shifts), ω(θ(F)^*F) ≥ 0 for F ∈ 𝔄_+(Π).
**Proof.** Let Π ∈ P_{m_0}. For K ≥ m_0 and K above the levels of the finitely many generators in F, every block
generator in F is a function of fine links in blocks on the positive side (locality, X-S4c (vi)), so F_K ∈ 𝔉_+;
θ maps grids shifted by a to grids shifted by θ_lin a, so θ(F)_K = θ(F_K). Hence ω_K(θ(F)^*F) ≥ 0 by X-LRP, and
the inequality is preserved by the weak-* limit. Elements of 𝔄_+ are norm limits of such polynomials. ∎
- **Flowed observables are not in 𝔄_+** (X-FLOW-NL); RP is not asserted for them.

### X-FLOW. Flowed lattice Wilson loops are bounded continuous gauge-invariant observables. PROVEN-HERE
**Statement.** The Wilson flow V_τ(U) exists for all τ ∈ R, is smooth in (τ, U), commutes with gauge transformations
and lattice symmetries; W_{t,γ} ∈ C(Ω_K), |W_{t,γ}| ≤ 1, gauge invariant.
**Proof.** The flow is the gradient flow of a smooth function on the compact manifold Ω_K; a smooth vector field on a
compact manifold is complete and its flow is smooth (Lüscher states the same, NOTES §4 [read]). The Wilson action is
gauge and lattice-symmetry invariant, so the gradient vector field is equivariant, and by uniqueness of solutions the
flow commutes with these actions. The holonomy is a continuous function of V_τ; its normalised trace is bounded by 1
and gauge invariant (closed loop). ∎

### X-FLOW-NL. At every positive flow time a flowed loop depends on links arbitrarily far away. PROVEN-HERE (+ check x1)
**Statement.** Around the flat configuration U = 1, the first variation of the flowed curvature F(τ) with respect to a
fine link b is Σ_{p'} K_τ(p - p')(dδA_b)(p') componentwise, with K_τ(x) = e^{-8τ} Π_{i=1}^4 I_{x_i}(2τ) > 0 (I_n the
modified Bessel function); on Z^4 it is non-zero for links b at any distance, and on the torus for all but the
antipodal-symmetric offsets (the periodised kernel is symmetric under x_μ ↦ n - x_μ, so K_τ(x) - K_τ(x - e_μ) = 0 at
x_μ = (n+1)/2 for odd n) [RX12-fix 8]. Hence for a coarse loop γ, the second variation
∂²W_{t,γ}/∂A_b∂A_b at U = 1 is non-zero for links b arbitrarily far from γ, and W_{t,γ} is not a function of the links
in any half-space not containing all of them.
**Proof.** U = 1 is a stationary point of the flow, so the derivative of V_τ at U = 1 is the linearised flow
Ȧ = -d^*dA (lattice units). For F = dA: Ḟ = -dd^*F = -Δ_2 F (since dF = 0, Δ_2F = dd^*F). On the cubical lattice the
Hodge Laplacian on 2-forms acts componentwise as the scalar lattice Laplacian (check x1 A2: exact, side 4 and 5), whose
heat kernel is the stated product of Bessel functions, strictly positive. The response of a plaquette (μν) to a link b in
direction ν at transverse offset x is K_τ(x) - K_τ(x - e_μ) up to sign; since n ↦ I_n(z) is strictly decreasing for
n ≥ 0 and z > 0, this is non-zero for x_μ ≥ 1. W = 1 - (1/2N)tr(Φ_γ²) + O(Φ³) with Φ_γ the (linear-order) flux, so the
second variation is -(1/N)·(response)² ≠ 0. Check x1 B2: response 2.96e-5 (τ = 0.5), 1.62e-4 (τ = 2) for a link at
distance 2 in every coordinate on side 5. ∎
- Physical reading: in physical units the kernel width is of order √t; the dependence is Gaussian-small beyond √t but never
  zero. Therefore **X-RP does not apply to flowed loops** [RX12-fix 8] (non-locality does not prove that RP fails), and
  approximate RP needs a locality estimate (H-loc, §4). (Check x1 B2 uses offset (2,2,2,2) on side 5, which avoids the
  symmetric zero; it does not probe the torus caveat.)

### X-OS. OS reconstruction on R×T³: a Hamiltonian H ≥ 0 exists on (ker T)^⊥ with no estimate. PROVEN-HERE | X-RP, X-SYM
**Setting.** Take the time side ℓ_0 → ∞ jointly with K → ∞ (X-IV below, with the spatial torus fixed). Let Π_0 ∈ P_0
be a time plane, θ its reflection, τ_s time translation, 𝔄_+ as in X-RP. On 𝔄_+ put ⟨F, G⟩ := ω(θ(F)^*G); let H_ω be
the Hilbert completion modulo null vectors, Ω the class of 1. For s ∈ 2D_+ := {2jL^{-m} : j ≥ 1, m ≥ 0}
define T(s)[F] := [τ_s F].
**Statement.** (i) T(s) is a well-defined self-adjoint contraction with T(s) ≥ 0, T(s)T(s') = T(s + s'), T(s)Ω = Ω.
(ii) T(s) = T(2)^{s/2} for all s ∈ 2D_+ (functional calculus). (iii) With 𝒦 := ker T(2) = ker T(s) for every s,
H := -½ log T(2) is a self-adjoint operator ≥ 0 on 𝒦^⊥ with HΩ = 0, T(s) = e^{-sH} ⊕ 0 on 𝒦^⊥ ⊕ 𝒦, and
s ↦ e^{-sH} extends to a strongly continuous semigroup on 𝒦^⊥ for real s ≥ 0. (iv) 𝒦 = {0} iff the time-continuity
condition holds: lim_{s→0, s∈2D} ω(θ(F)^*τ_sF) = ω(θ(F)^*F) for every F ∈ 𝔄_+.
**Proof.** (i) τ_s maps 𝔄_+ into 𝔄_+ (s > 0; shifted grids are generators). θτ_s = τ_{-s}θ and τ-invariance of ω give
⟨F, T(s)G⟩ = ⟨T(s)F, G⟩ and ⟨T(s)F, T(s)F⟩ = ⟨F, T(2s)F⟩. Positivity: ⟨F, T(s)F⟩ = ω(τ_{-s/2}θ(F)^* τ_{s/2}F) =
ω(θ'(G)^*G) with G = τ_{s/2}F and θ' the reflection in Π_0 + s/2. For s = 2jL^{-m}, s/2 = jL^{-m}, and
Π_0 + s/2 ∈ P_m by X-PLANES [Π_0 = i + ½, and i + ½ + jL^{-m} = ((i + ½)L^m + j)L^{-m} with
(i + ½)L^m = iL^m + (L^m - 1)/2 + ½, L^m - 1 even]; G lies on its positive side; X-RP gives ≥ 0. Contraction: by
Cauchy-Schwarz iterated, ⟨F, T(s)F⟩ ≤ ⟨F, F⟩^{1-2^{-n}} ⟨F, T(2^n s)F⟩^{2^{-n}} ≤ ⟨F, F⟩^{1-2^{-n}}||F||_∞^{2^{1-n}} →
⟨F, F⟩, using |ω(·)| ≤ ||·||. Null vectors map to null vectors by Cauchy-Schwarz, so T(s) is well defined; it is
bounded, symmetric and positive on a dense set, hence self-adjoint positive with ||T(s)|| ≤ 1. The semigroup law and
T(s)Ω = Ω are immediate. (ii) T(2L^{-m}) ≥ 0 and T(2L^{-m})^{L^m} = T(2); positive operators have unique positive roots
[STANDARD], so T(2L^{-m}) = T(2)^{L^{-m}} and T(2jL^{-m}) = T(2)^{jL^{-m}}. (iii) Functional calculus for the positive
contraction T(2): ker T(2)^r = ker T(2) for r > 0; on 𝒦^⊥, T(2) is injective with spectrum in (0, 1], so log T(2) is
self-adjoint ≤ 0; e^{-sH} = T(2)^{s/2} is strongly continuous on 𝒦^⊥ by dominated convergence in the spectral
representation. (iv) T(s) → P_{𝒦^⊥} strongly as s → 0 (spectral theorem), so ⟨F, T(s)F⟩ → ||P_{𝒦^⊥}F||²; this equals
||F||² for all F in a dense set iff 𝒦 = {0}. ∎
- **Meaning.** The OS Hilbert space and a positive Hamiltonian exist for **every** limit point, from RP alone. The
  only OS-structural estimate on the time axis is (iv): **H-cont-time** (OPEN, X-CONT).
- **Possibly trivial [RX12-fix 10].** Nothing here excludes 𝒦^⊥ = CΩ (a state that decorrelates across Π_0), in which
  case H = 0 on a one-dimensional space. "A Hamiltonian H ≥ 0 exists for every limit point" is true but possibly
  vacuous, and it must not be presented as a non-trivial OS reconstruction. The construction is the textbook
  dense-lattice-time OS argument; it is correct, not new.
- On the torus (finite ℓ_0) the same holds with the usual finite-temperature restrictions (supports in
  (0, ℓ_0/2)); not written out.

### X-IV. Infinite-volume limit points exist with all soft structure. PROVEN-HERE
**Statement.** Along any sequence (K_j, ℓ_j) → (∞, ∞) (ℓ_j ∈ 4L^N), there is a subsequence and a state ω on the
quasi-local algebra 𝔄^loc (generators supported in bounded regions of R^4, defined on all tori large enough) with:
X-CONS, X-SYM (D-translations of R^4, hypercubic group), X-RP for all planes in P, and X-OS on R^4.
**Proof.** Same as X-ALG with the countable generator set of bounded support; each generator is defined for all large
j; X-CONS, X-SYM, X-RP pass to the limit as before (for X-RP, a bounded-support F lies in the positive slab for ℓ_j
large). ∎ (This is P's L8a/L8b/L8c in the state formulation.)
- [RX12-fix 2] Without the M-uniformity of H-Bal-1 the bare coupling may depend on ℓ_j; the soft structure above does not
  care, but reading the limit as one theory does.

### X-ND. Non-triviality, weak form: the limit block laws are neither flat nor Haar. PROVEN-HERE | H-Bal-1, H-Bal-3 (finite volume)
**Statement.** For every m and every limit point: (i) on int R_m(ε_0), ν_{*,m} ≥ c_m · Haar with c_m > 0;
(ii) ν_{*,m}(closure of R_m(ε_0)) ≥ 1 - η_0; hence (iii) ν_{*,m} gives zero mass to no non-empty open subset of
int R_m(ε_0), so it is not supported on the flat configurations (a Haar-null closed set), and (iv) ν_{*,m} ≠ Haar
whenever 1 - η_0 > Haar(R̄_m(ε_0)) (true for small ε_0: a single coarse plaquette is Haar distributed under Haar
measure, so Haar(R̄_m) ≤ Haar{|W - 1| ≤ ε_0} = O(ε_0^{N²-1})).
**Proof.** By (3a), on R := R_m(ε_0): ρ_K = 𝒵_K^{-1} w_K e^{E_K}(1 + R_K) with w_K := exp(-(1/g_{m,K}²)A^η(U_k(V))).
Put Ē := E_0 Σ_X e^{-κd(X)} over polymers in the finite torus (< ∞, at most C_κ E_0 |Λ_m|). Then
[RX12-fix 4, with the weakened remainder] e^{-Ē - C_R|Λ_m|} ≤ e^{E_K}(1 + R_K) ≤ e^{Ē + C_R|Λ_m|} and
e^{-C_A|Λ_m|/g_{min}²} ≤ w_K ≤ e^{C_A|Λ_m|/g_{min}²} with g_min the K-uniform lower bound of H-Bal-1 (A^η is real on
real configurations; the modulus bound of (3a) is used). Put c' := e^{-Ē - C_R|Λ_m| - C_A|Λ_m|/g_min²} and
c'' := e^{Ē + C_R|Λ_m| + C_A|Λ_m|/g_min²}, so c' ≤ w_K e^{E_K}(1 + R_K) ≤ c'' on R.
Normalisation: 1 ≥ ν_K(R) = 𝒵_K^{-1}∫_R w_K e^{E_K}(1 + R_K) dHaar ≥ 𝒵_K^{-1} c' Haar(R), so
𝒵_K^{-1} ≤ (c' Haar(R))^{-1}; and ν_K(R) ≥ 1 - η_0 gives 𝒵_K^{-1} ≥ (1 - η_0)/(c'' Haar(R)). Hence
ρ_K ≥ c_m := c'(1 - η_0)/(c'' Haar(R)) > 0 on R, uniformly in K. For continuous f ≥ 0 supported in int R, ∫f dν_{*} = lim ∫ f ρ_K dHaar ≥ c_m ∫ f dHaar; Riesz on
the open set int R gives (i). (ii) is the Portmanteau inequality for the closed set R̄. (iii), (iv) follow. ∎
- H-Bal-2 is not used. The constants degrade like e^{-C|Λ_m|} with the number of coarse cells: this is a
  finite-volume statement at each fixed m; X-IVND is the volume-uniform version.
- [RX12-fix 4, 5] ν_{*} here is the gauge-lifted limit of X-CONS (the ν_{K,m} are coarse-gauge invariant, so ∫f dν_{K,m}
  = ∫f̄ dν_{K,m} and the limit exists for all continuous f). The proof is otherwise unchanged.
- **Weak non-triviality only [RX12-fix 4].** The block laws at fixed resolution are neither flat nor Haar. With g fixed
  at the unit scale *by hypothesis* (g_K = g), this is close to built in. It is not non-Gaussianity.

### X-MONTEL. The limit block law has a density of Balaban's form with an analytic effective action. PROVEN-HERE | H-Bal-1, H-Bal-3
**Statement.** Along a further subsequence, g_{m,K} → g_{m,*} ∈ (0, γ], and E_{K,m}(X) → E_{*,m}(X),
A^η(U_k(·)) → 𝒜_*(·) locally uniformly on R^c_m, holomorphically, with |E_{*,m}(X)| ≤ E_0 e^{-κd(X)}; and on
int R_m(ε_0), dν_{*,m}/dHaar = 𝒵_*^{-1} exp(-(1/g_{m,*}²)𝒜_* + E_{*,m}) (1 + R_*) with R_* a weak-* limit point of the
R_{K,m} (e^{-C_R|Λ_m|} ≤ 1 + R_* ≤ e^{C_R|Λ_m|} a.e. [RX12-fix 3]).
**Proof.** H-Bal-1 gives g_{m,K} in a compact subinterval of (0, γ]. In finite volume there are finitely many polymers;
each E_{K,m}(X) and A^η(U_k(·)) is holomorphic on R^c_m and bounded uniformly in K, so Montel's theorem (several
complex variables) [STANDARD] gives locally uniformly convergent subsequences with holomorphic limits; the bounds pass
to the limit. The R_{K,m} are bounded in L^∞ by e^{C_R|Λ_m|}, K-uniformly, so a further subsequence converges weak-* in L^∞(Haar|_R);
𝒵_K converges along a subsequence by the bounds in X-ND. For continuous f supported in int R, ∫ f ρ_K dHaar converges
to the integral against the stated limit (uniform convergence times weak-* convergence). ∎
- This is the precise sense in which "the effective action on the unit lattice remains bounded, and the existence of a
  UV limit for gauge-invariant observables such as smoothed Wilson loops follows by compactness, without uniqueness"
  (Magnen-Rivasseau-Sénéor's description of Balaban's result, NOTES §2 [read]).

### X-CAUCHY. In the limit effective action, the order-n Taylor term in the rescaled field is O(g^n). PROVEN-HERE | H-Bal-3
**Statement.** In a coarse gauge where V = exp(iX)V_flat and R^c_m ⊃ {||X||_∞ < α}, write X = g_{m,*}B. For every
polymer X_0, the homogeneous degree-n Taylor term T_n of B ↦ E_{*,m}(X_0; exp(ig B)V_flat) satisfies
|T_n(B)| ≤ E_0 e^{-κd(X_0)} (g||B||_∞/α)^n.
**Proof.** For fixed real B ≠ 0, f(z) := E_{*,m}(X_0; exp(izgB/||B||_∞)V_flat) is holomorphic for |z| < α/g and bounded by
E_0e^{-κd(X_0)}; T_n(B) = f^{(n)}(0)||B||_∞^n/n!, and Cauchy's estimate on |z| = r < α/g, r → α/g, gives the bound. ∎
- **Reading.** The effective-action corrections perturb the Gaussian quadratic form ½⟨B, QB⟩ by relative O(g²) and
  contribute O(g⁴) to quartic vertices, while the explicit term (1/g²)𝒜_* contributes cubic vertices O(g) and quartic
  O(g²). This is the structure X-NT2 needs.
- Caveat (review): O(g^n) depends entirely on the analyticity radius α being g-independent in coarse units. Balaban's
  domains (α_0, α_1, ε_0 fixed constants) support this for the small-field RG; for the full law it is [unverified].

### X-NT2. Non-triviality, strong form: the limit is not Gaussian. OPEN (reduced)
**Statement (target).** For some m, small g and some coarse loops (or linearised block fields), the connected 4-point
cumulant of the rescaled linearised block field B = g^{-1}Π_0 log V^(m) under ν_{*,m} is c g² + O(g³) with c ≠ 0
determined by the tree-level vertices of (1/g²)𝒜_*.
**Reduction.** Given X-MONTEL and X-CAUCHY, what is missing is a finite-dimensional Laplace-method lemma (LAP) for the
integral over C_m with density ∝ exp(-(1/g²)𝒜_* + E_*), uniformly in the large-field remainder (3b) and on a torus
whose flat connections are not isolated (commuting holonomies: the moduli must be integrated, not expanded). Also
needed: the cubic coefficient of 𝒜_* is the non-abelian YM vertex smeared by the block constraint, which requires the
second-order expansion of the background minimiser (CMP 102 [not-read]).

### X-NTAF. Non-triviality via asymptotic freedom: the block laws approach flat logarithmically as m → ∞. (Session 1: OPEN; session 2: PROVEN-HERE in two-sided form, §10.1)
**Statement (target).** For a coarse plaquette p at resolution m, c_1 g_{m,*}² ≤ ∫ (1 - N^{-1}Re tr V_p) dν_{*,m} ≤
c_2 g_{m,*}², with g_{m,*}² ≍ 1/(m log L) by H-Bal-1. A massless Gaussian field gives m-independent block laws, a
massive one m-independent laws as m → ∞, so this excludes free fields with canonical scaling.
**Needs.** H-Bal-3G (finite-volume constants e^{±C|Λ_m|} grow with m and are useless here) plus a one-link Laplace lemma
(LAP-1) for the conditional law of a coarse link given a regular environment.

### X-IVND. Infinite-volume non-degeneracy. PROVEN-HERE | H-Bal-3G
**[RX12-fix 9] Two corrections.** (1) A function f on G^Y lies in 𝔄 only if it is coarse-gauge invariant. Read the
statement for the **gauge-averaged marginal** ν_{*,m}|_Y (X-CONS lift); equivalently take O_Y invariant under the
coarse gauge transformations acting on Y (conjugation-type action at the endpoints), which H-Bal-3G is then assumed
for. (2) "Not Haar" needs η_0 below the Haar probability of an irregular plaquette, which is 1 - O(ε_0^{N²-1}):
**assume η_0 < Haar{|W - 1| ≥ ε_0}** for "not Haar"; "not flat" needs only c_Y > 0 and η_0|Y| < 1.
**Statement.** Under H-Bal-3G, every infinite-volume limit point (X-IV) has gauge-averaged marginals on any finite
coarse link set Y with ν_{*,m}|_Y ≥ c_Y(1 - η_0|Y|)·Haar on O_Y, and ν_{*,m}(r given coarse plaquettes at mutual
distance ≥ R_0 are all irregular) ≤ η_0^r. Hence the infinite-volume limit is not flat, and (when η_0 < Haar{|W - 1| ≥
ε_0}) not Haar, uniformly in the volume.
**Proof.** For continuous f ≥ 0 supported in O_Y: E_K[f(V_Y)] = E_K[E_K[f(V_Y) | V_{Y^c}]] ≥ c_Y (∫ f dHaar)
(1 - η_0|Y|), uniformly in K and M; pass to the limit. The Peierls bound is a bound on the probability of a closed set
of coarse configurations; Portmanteau for closed sets passes it to the limit. ∎

### X-RAW. Raw lattice Wilson loops of fixed physical size degenerate. ARGUED (uncounted)
At one loop, a straight lattice line of physical length ℓ_γ costs exp(-c g_0² C_F ℓ_γ/ε) (lattice self-energy;
c involves the 3D lattice Green's function at the origin), with g_0² ≍ 1/(2b_0 log(1/ε)); so ⟨W_γ⟩ → 0 like
exp(-c' ℓ_γ/(ε log(1/ε))), with extra cusp factors at every lattice corner. Chatterjee's Problem 5.2 (NOTES §3 [read])
formulates the continuum limit of raw loops *with* a divergent perimeter subtraction c(β)(R + T). Raw loops are
therefore excluded from 𝔄; the block loops (O^blk) and flowed loops (O^flow) replace them. Not proven here.

---

## 4. What needs more than stability: OS0, time continuity, rotations, sources

### X-MOM. Exponential-moment bounds imply convergent Schwinger functions, distributional bounds and OS0. PROVEN-HERE (implication)
**Hypothesis H-src(Φ).** Φ_K(f) are real random variables on Ω_K, linear in f ∈ 𝒯 (a separable space of test
functions with a continuous norm N, e.g. C^∞(T^4) with N(f) = ||f||_{L^1} + ||f||_{L^p}), and there are C, c_0 > 0 with
E_K[exp Φ_K(f)] ≤ exp(C N(f)) for all K and all f with N(f) ≤ c_0.
**Statement.** Then (i) E_K|Φ_K(f)|^n ≤ 2e^{Cc_0} n! (N(f)/c_0)^n for all f, n, K; (ii) along a subsequence, all
S^K_n(f_1, ..., f_n) := E_K[Φ_K(f_1)⋯Φ_K(f_n)] converge, for all n and all f_i ∈ 𝒯, to multilinear S_n with
|S_n(f_1..f_n)| ≤ 2e^{Cc_0} n! c_0^{-n} Π N(f_i); for 𝒯 = C^∞(T^4) each S_n is a distribution on T^{4n} (kernel
theorem); (iii) the limits are the moments of a probability measure on 𝒯' (Minlos, 𝒯 nuclear), with
E[e^{Φ(f)}] ≤ e^{CN(f)} for N(f) ≤ c_0/2 (an exponential OS0-type bound for small f; Glimm-Jaffe's form holds for all
f); (iv) if moreover each Φ_K(f) with f supported in a positive half-space is measurable with respect to the
positive-half links, and θΦ_K(f) = Φ_K(θf), the limit is reflection positive on the
polynomial algebra and on exponentials.
**Proof.** (i) For N(f) ≤ c_0 put h := c_0 f/N(f): E e^{±Φ(h)} ≤ e^{Cc_0}, so E e^{|Φ(h)|} ≤ 2e^{Cc_0}, and
|x|^n/n! ≤ e^{|x|} gives E|Φ(h)|^n ≤ 2e^{Cc_0}n!; scale back by linearity (any f). (ii) Hölder gives the multilinear
bound for S^K_n. For f_i in a countable dense 𝒟 ⊂ 𝒯 the S^K_n are bounded, so a diagonal subsequence converges for
all finite tuples from 𝒟; the uniform multilinear bound gives |S^K_n(f) - S^K_n(f')| ≤ C_n Σ_i N(f_i - f'_i)Π_{j≠i}
max(N(f_j), N(f'_j)), so convergence extends to all of 𝒯, with the same bound. Continuity in N (continuous on C^∞)
plus multilinearity gives distributions by the Schwartz kernel theorem [STANDARD]. (iii) Moments with n!c^n growth
determine the finite-dimensional laws, which therefore converge weakly (tightness from (i), method of moments);
|1 - E e^{iΦ(f)}| ≤ E|Φ(f)| ≤ C'N(f) gives continuity of the characteristic functional, and Minlos [STANDARD] gives the
measure on 𝒯'. e^{Φ_K(f)} is uniformly integrable when N(2f) ≤ c_0 (bounded second moment by H-src), so the exponential
bound passes to the limit (for N(f) ≤ c_0/2; the constant is unchanged); general f by the form of the bound is not
claimed. (iv) Each RP inequality for polynomials is a finite combination of moments, which converge; exponentials are
limits of polynomials in L² by (i). ∎

### X-SRC-GAP. H-src is not in Balaban, and the obvious fields violate its naive form. OPEN (the gap), with ARGUED sub-points (session 2: separated-support form reduced, §10.3)
- **Bounded block fields** satisfy H-src trivially at fixed resolution (|Φ| ≤ C(m)N(f)); the content of OS0 is the
  limit m → ∞ (point-like fields), where the constants must not grow.
- **Local composite fields of dimension 4** (the lattice action density Σ_p f(x_p)β_0 w_p, i.e. tr F² smeared at
  the lattice scale): ARGUED, its variance diverges like ε^{-4}∫f² (conditional on all other links, the
  single-link action has O(1) equipartition fluctuations, and there are ε^{-4} independent such links per unit
  volume), so H-src in exponential form fails. For dimension-4 composites the Schwinger functions must be bounded at
  **non-coincident** supports and extended (H-src', OPEN): this is a statement about generating functionals with
  local counterterm polynomials in the sources, i.e. **UV stability with a position-dependent bare coupling g_0(x)**
  (a source for tr F² is a variation of the coupling) with explicit counterterms. Balaban's machinery is local, so this
  is a natural extension; it is not in the published papers.
- **Flowed fields at fixed t > 0** (energy density E_t(x)): perturbatively finite with no further renormalisation
  (Lüscher-Weisz, NOTES §4 [read]); H-src(E_t) is plausible but OPEN, and it needs fine-scale control (the flow
  reaches the cutoff scale), i.e. H-Bal-3 at every scale, not just at m.
- **Statement of H-src-flow (OPEN):** for each t > 0 there are C_t, c_t with E_K[exp(Σ_x ε^4 f(x)(E_t(x) - ⟨E_t⟩_K))]
  ≤ exp(C_t N(f)) for N(f) ≤ c_t, uniformly in K. With X-MOM it gives OS0 for flowed fields at fixed t; RP for them
  still needs H-loc.

### X-ARP. Approximate RP for approximately local observables. PROVEN-HERE (implication)
**Statement.** If F ∈ L²(ω) (e.g. a flowed observable, via X-ALG) and G ∈ 𝔄_+ with ||F - G||_{L²(ω)} ≤ δ and
||θF - θG||_{L²(ω)} ≤ δ, then ω(θ(F)^*F) ≥ -2δ||G||_{L²(ω)} - δ².
**Proof.** ω(θ(F)^*F) = ω(θ(G)^*G) + ω(θ(F - G)^*G) + ω(θ(F)^*(F - G)); the first is ≥ 0 by X-RP; Cauchy-Schwarz bounds
the others. ∎
- **H-loc (OPEN):** for a flowed loop at distance d from Π, inf_{G∈𝔄_+} ||W_{t,γ} - G||_{L²(ω)} ≤ C e^{-c d²/t},
  uniformly along the subsequence. X-FLOW-NL shows exact locality fails, so H-loc is the needed estimate. With H-loc,
  flowed and block observables generate a common RP structure in the limit t → 0 at fixed distance (P's route γ2).

### X-CONT. Time (and space) continuity: ker T = 0. OPEN (session 2 reductions: X-KER, X-2GRID, X-CONT-G, §10.2)
**Statement H-cont (needed) [RX12-fix 7: joint L² two-grid form].** There are γ > 0 and C such that for every block
observable F ∈ O_m(X) with Lipschitz constant 1 and every a ∈ D with |a| ≤ L^{-m}:
  sup_{K ≥ level(a)} E_K|F(V^(m)_{K,a}) - F(V^(m)_{K,0})|² ≤ C|X|_m (L^m|a|)^γ.
(Session 2 stated the single-expectation form |E_K[F(V_{K,a})] - E_K[F(V_{K,0})]| ≤ ...; that form is **vacuous**: for
a ∈ D and K ≥ level(a), μ_K is invariant under translation by a, so the difference is identically 0. It is deleted.)
|F_a - F_0|² is an element of 𝔄 (a polynomial in generators), so the K-uniform bound passes to ω: ||τ_aF - F||²_{L²(ω)}
≤ C|X|_m(L^m|a|)^γ. By X-KER (iii) (L²(ω)-continuity of time translations on generators) and X-OS (iv), H-cont implies
𝒦 = {0}, i.e. the Hamiltonian on all of H_ω, and with X-SYM, exact R^4 translation invariance of the limit (P's
L9b(β)). This is exactly the form that X-2GRID's reading and X-CONT-G use.
**Why it is not soft and not in H-Bal-3 at one scale.** V^(m)_{K,a} and V^(m)_{K,0} are averages over blocks that
differ in a boundary layer of physical width |a|; comparing them needs control of the fine fields at all scales between
|a| and L^{-m} *in the same configuration*. H-Bal-3 at each scale separately gives the law of each block variable, not
the joint law of two grids. Large-field regions at fine scales are dense (P, E8.3), so the estimate must use the
R-operation's resummation, not their absence.

### X-ROT. Euclidean invariance (OS1). OPEN
On the torus false by geometry. On R^4: averaging limit points over SO(4) destroys RP (P, remark R9.1). Needs either
H-rot (orientation independence of the limit, a universality statement requiring E7-type convergence and, in infinite
volume, probably H-uniq) or the two-family route (rotation-covariant flowed fields + H-loc). Hypercubic symmetry allows
dimension-6 rotation-breaking operators (e.g. Σ_μ tr(D_μF_μν)²), so rotation invariance requires that their
coefficients vanish in the limit: a rate statement (cutoff effects O(ε^κ)), not a compactness statement.

---

## 5. Infinite volume: what needs a gap or a cluster expansion

### X-IR. Uniqueness, clustering (OS4), mass gap. OPEN
- **Not needed for existence of limit points** (X-IV) or for RP, L-adic translations, hypercubic symmetry, the OS
  Hilbert space and H ≥ 0 on 𝒦^⊥ (X-OS).
- **Needed for:** uniqueness of the state (independence of the subsequence and of the torus shapes); clustering OS4
  (and hence the vacuum's uniqueness in H_ω); the mass gap; the universality route to rotation invariance; and any
  identification of the limit with "the" YM theory.
- **Why H-Bal does not reach it.** At the unit scale g = g_K is small but the coarse theory on the unit lattice is a
  weakly coupled lattice gauge theory in a large volume, whose own RG flows to strong coupling at larger scales.
  Balaban stops at the unit scale; H-Bal-2's bulk bounds e^{±E|T|} are crude at that scale and say nothing about decay.
  H-Bal-3G gives volume-uniform *local* bounds (X-IVND), not decay of correlations.
- Remark: OS4 for a translation-invariant RP limit point can in principle be sought by ergodic decomposition; whether
  RP survives it is [unverified] (P, L9d).

---

## 6. DAG and tally (updated session 3)

```
(a) X-ALG ⇐ X-S4c (continuity) ; X-CONS ⇐ X-S4c, X-ALG ; X-FLOW
(b) X-RP ⇐ X-LRP [IMP-REV], X-S4c(iv,vi), X-ALG ; X-SYM ⇐ X-S4c, X-FLOW ; X-OS ⇐ X-RP, X-SYM, X-IV(time)
    time continuity: 𝒦 = {0} ⇐ H-bl ⇐ H-cont-time (X-KER) ; X-2GRID (exact) ;
        H-cont ⇐ H-corr + H-lin [OPEN; implication ARGUED] ; free Gaussian model: X-CONT-G (proven)
    OS1: X-ROT [OPEN] ⇐ H-rot or (X-ARP + H-loc [OPEN])
    OS0 (fields): X-MOM [implication] ⇐ H-src-flow / H-src' [OPEN, X-SRC-GAP]
        separated supports: X-SRC-CT ⇐ H-src' ⇐ H-Bal-loc (X-SRC-RED) ; diagonal: H-src'-diag [OPEN]
(c) X-ND ⇐ H-Bal-1, H-Bal-3 ; X-MONTEL ⇐ H-Bal-1, H-Bal-3 ; X-CAUCHY ⇐ X-MONTEL
    X-NT2 [OPEN] ⇐ X-MONTEL, X-CAUCHY, LAP (moduli)
    LAP-1 ⇐ H-Bal-3L, C2 ; X-NTAF, X-NTAF-AF ⇐ H-Bal-1, LAP-1, H-Bal-3T ; X-WIL ⇐ LAP-1 (exact for Wilson)
    X-NTAF-sharp [OPEN] ⇐ W-AF1 (flow coefficient) + W-AF2 (= H-corr)
(d) X-IV ; X-IVND ⇐ H-Bal-3G ; X-IR [OPEN]
H-Bal-2 : used by no node.
Session 3 (§11): LAP-1 ⇐ H-Bal-3L ⇐ [Theorem LF⇒3L] H-Bal-1, H-loc-LF (via BG-1L-B, POL-1L; soft linear instance
    BG-1L-lin ⇐ P's N2-E, N2-lin, N2-exp) ; X-ND (no (3b)), X-MONTEL ⇐ Corollary LF⇒3 ⇐ H-loc-LF ;
    X-IVND' ⇐ LF⇒3L, X-NTAF (lower), (LF-P) ; H-Bal-3T ⇐ H-loc-LF + H-sg ; H-Bal-3G retired (no carried conclusion).
```

| Status | Count | Items |
|---|---|---|
| PROVEN-HERE | 29 | session 1 (16): X-S4c, X-ALG, X-CONS, X-SYM, X-RP, X-FLOW, X-FLOW-NL, X-OS, X-IV, X-ARP, X-MOM, X-ND, X-MONTEL, X-CAUCHY, X-IVND, X-PLANES. Session 2 (8): LAP-1 (with C2), X-NTAF (with corollary X-NTAF-AF), X-WIL, X-KER, X-2GRID, X-CONT-G, X-SRC-CT, X-SRC-RED. Session 3 (5): BG-1L-lin, BG-1L-B, POL-1L, Theorem LF⇒3L, Corollary LF⇒3 with X-IVND' (X-IVND' counted with LF⇒3: 29 = 24 + 5). 7 of the 24 carry [RX12-fix] corrections (X-S4c, X-CONS, X-FLOW-NL, X-ND, X-IVND, X-NTAF, X-KER) |
| IMPORTED-AND-REVERIFIED | 1 | X-LRP (Osterwalder-Seiler lattice RP, via P's re-derivation, re-read here) |
| IMPORTED-NOT-YET-REVERIFIED | 3 | H-Bal-1 (*Balaban states it* for SU(2), proof unseen; SU(N) and M-uniformity: *plausible extension*), H-Bal-2 (*Balaban states it*, exact form unverified; unused), H-Bal-3(3a)-form (*Balaban states it*, small-field RG; background field and response decay [second-hand]) |
| HYPOTHESIS (new; no source) | 3 | H-loc-LF (§11.2; its small-field part is the (3a)-form, the localisation, (LF-b) and (LF-P) are new), H-sg (§11.4), H-Bal-loc. Retired in session 3 (formulated, no longer carried by any conclusion): H-Bal-3 full-law packaging (⇐ H-loc-LF), H-Bal-3G, H-Bal-3L (⇐ H-Bal-1 + H-loc-LF), H-Bal-3T (⇐ H-loc-LF + H-sg) |
| OPEN | 11 | X-NT2 (with LAP), X-NTAF-sharp (W-AF1, W-AF2), H-src-flow, H-src'-diag (contact terms), H-loc, H-cont (X-CONT, L² two-grid form; reduced), H-corr, H-lin, X-ROT, X-IR (uniqueness/OS4/gap), Option S soft-layer transfer (X-RP^S and Markov-projective consistency, §11.5; replaces session 2's "S4c-compatibility of CMP 122's bookkeeping", which is now a named part of H-loc-LF) |
| ARGUED (uncounted) | 8 | X-RAW; the ε^{-4} variance of the action density; H-corr + H-lin ⇒ H-cont; the bare additive coupling shift as the source of the RG-invariant g_0²F²; the leading coefficient c_blk; the narrowed "local-norm" single-step finding (§10.2); RLF ⇒ RLF-loc (gaps D3, D4, §11.5); the asymptotic Wilson-plaquette lower bound from Chatterjee's free energy by convexity (§11.6). (Session 2's "H-Bal-3L/3T as the local content of H-Bal-3" is withdrawn [RX12-fix 4].) |

Conditional items: X-ND, X-MONTEL, X-CAUCHY | H-Bal-1 + H-Bal-3 (session 3: + H-loc-LF in place of the packaging); X-IVND | H-Bal-3G; X-IVND' | H-Bal-1, H-loc-LF; LAP-1, X-NTAF | H-Bal-1/3L/3T (session 3: lower bound | H-Bal-1, H-loc-LF; upper bound + H-sg); X-SRC-RED | H-Bal-loc.
Implications from OPEN hypotheses: X-MOM, X-ARP, X-SRC-CT. Unconditional: X-WIL, X-KER, X-2GRID, X-CONT-G (free model).
Session 1 counted X-NTAF as OPEN; it is now PROVEN-HERE in the two-sided form and its sharp form is the OPEN
X-NTAF-sharp. Session 1's OPEN "H-src' (composites)" is split into X-SRC-RED (proven | H-Bal-loc) and H-src'-diag (OPEN).
Sessions 1-2 were reviewed independently in REVIEW_X1_X2 (its 12 binding fixes are applied, tagged [RX12-fix]). §11 (session 3) is unreviewed.

**Check x1** (checks/x1_criteria.md written before checks/x1_hodge_flow.py): A1-A3 exact (0.0 differences on sides 4
and 5); B1 min heat-kernel entry 1.14e-5 (τ = 0.5), 1.04e-3 (τ = 2); B2 far-link responses 2.96e-5, 1.62e-4. PASS.
0.5 s, 67 MB, one process, nice 10, threads 1. Run as `python3` without -I (numpy is in the user site); the script reads
no external files.

**Check x2** (checks/x2_criteria.md written before checks/x2_lap_gauss.py): A (LAP-1 in the exact 2D SU(2) Wilson model)
PASS; B (Gaussian two-grid variances, exact Fourier symbol) PASS; all pre-registered expectations met (A3, B3 a-c).
0.6 s wall, 162 MB peak, nice 10, threads 1, load 1.7, memory free 37%. Run as `python3` without -I (same reason as x1).

---

## 7. Relation to layer 1 (P) — which parts of H-Bal P re-derives

- **H-Bal-1 (flow):** P L4a is IMPORTED-NOT-YET-REVERIFIED; P re-derived the polarisation-tensor structure that
  defines β_j (L4a-Π, check c17(A)) and one-loop data from the D4 kernel. The flow bounds (0.31) themselves: not
  re-derived.
- **H-Bal-2 (Z-stability):** P L6 IMPORTED-NOT-YET-REVERIFIED.
- **H-Bal-3 (block laws):** P's ingredients — background field (L2, reduced via B-NA-red), propagators (L3s proven in
  a weaker scalar form; L3g imported), polymer expansion (Theorem CE, a d = 4 re-proof of Dimock's abstract theorem),
  the linear abelian package (N2-lin, N2-exp, PG, PG^(k), FP-ab, G♯_0-soft, F-df_0), the isolated-cube R-step
  (R4D-iso). **Caution:** under P's decision 4 these are proven for P's *soft* (Gaussian-constraint) kernel, not
  Balaban's δ-function constraint (0.17); they are analogues of H-Bal-3's ingredients, not re-derivations of H-Bal-3.
  H-Bal-3(3b)/3G ↔ P's E8* (fixed-depth cases proven, general OPEN) and L6loc.
  Session 3: H-loc-LF ↔ P's target RLF (RLARGE §1) and its inductive form (I_k); they differ by (D1)-(D6) of §11.5, and
  could coincide as RLF-loc under Option S. P's N2-E, N2-lin, N2-exp give the soft linear background increment
  (BG-1L-lin).
- **Soft layer overlap:** P's L7a, L8a, L8b, L8c, L9a, L9a', L9a-m are the measure-form versions of X-ALG, X-IV,
  X-SYM, X-RP, X-LRP. New here: the continuous block map X-S4c (removing P's need for E8* for consistency),
  the state formulation X-CONS, the transfer-operator lemma X-OS, the flowed-observable lemmas, and the
  hypothesis-to-conclusion map of §0.

---

## 8. Next targets (updated session 2; recommended order)

**Session-3 update (supersedes the order below, per REVIEW_X1_X2's strategic verdict).** Done in session 3: fixes 1-12,
H-Bal-3L/3G ⇐ H-loc-LF (§11). Next, in order: (1) **review of §11** (BG-1L-B, POL-1L, LF⇒3L, LF⇒3, X-IVND') before any
use; (2) **decide Option S** with layer 1: write X-RP^S and the Markov-projective X-CONS, so that the lanes share RLF-loc;
then the two gaps RLF ⇒ RLF-loc (D3: Theorem CE on the history gas at a fixed level field; D4: (PLD) for the true law at
level K - m); (3) H-bl from H-loc-LF-type local bounds (item 2 below); (4) H-sg (the small-field concentration wall;
shares its input with W-AF2/H-corr). Do not spend a session on X-NTAF-sharp (W-AF1 is Balaban's unseen flow paper).
Item 1 below (compact U(1) H-corr) is deprioritised.

1. **H-corr in the simplest non-trivial setting.** Prove the ℓ²-domination E|⟨χ, F^{(n)}⟩|² ≤ C||χ||² for the block
   curvature of the compact U(1) (Villain or Wilson) model at weak coupling in a small-field event, where the composite
   averaging is exactly linear on regular configurations (fluxes add); this would give H-cont there via X-2GRID and the
   proof of X-CONT-G, and test whether H-corr is the right interface to P's N5.
2. **H-bl directly.** X-KER needs only boundary-layer insensitivity; test whether H-bl follows from H-Bal-3L-type local
   bounds plus X-CONT-G-type counting without a full two-point bound.
3. **X-NTAF-sharp, W-AF2 side:** a Gaussian comparison for the single block-plaquette law in the small-field region,
   given H-Bal-3G; W-AF1 waits for Balaban's flow theorem.
4. **H-src'-diag:** identify the contact-term structure of ΔΨ as the supports merge (counterterm polynomials in h and
   its derivatives up to dimension 4).
5. **Review:** an independent read of §10 (LAP-1, X-KER, X-2GRID, X-CONT-G, X-SRC-RED) before any of it is used.

---

## 9. Session 2 (2026-10-27): pre-stated targets (written before any proof below)

Norm convention for this section: |·| is the Hilbert-Schmidt norm on N×N matrices, so for U ∈ SU(N)
**1 - N^{-1}Re tr U = |U - 1|²/(2N)** exactly (|U - 1|² = Σ_j |e^{iθ_j} - 1|² = Σ_j 4 sin²(θ_j/2)). Regularity sets
R_m(ε) use this norm.

**T1 (X-NTAF, target).** For a coarse plaquette p at resolution m, under hypotheses to be stated in local form
(one-link density ratios on a local regular event, and a per-plaquette tail bound), prove
c_- g_{m,K}² ≤ E_{K}[1 - N^{-1}Re tr V^{(m)}_p] ≤ c_+ g_{m,K}² p(g_{m,K})² uniformly in K and in the volume, with
explicit c_±, and pass it to every limit point; then read off the asymptotic-freedom signature through H-Bal-1. If the
sharp form (coefficient (N²-1)/(8N)-type and the 2b_0 rate) is not reachable, name the wall.

**T2 (H-cont, target).** (i) Reduce ker T = 0 to a condition weaker than translation continuity, if one exists.
(ii) Prove an exact identity reducing the two-grid comparison at sub-block shift s = jL^{-n} to the law of ONE
resolution n and a single averaging step applied on two grids offset by j/L of a block. (iii) Prove the resulting
estimate in the free abelian Gaussian model with the linearised S4' averaging (layer-1 linear package), uniformly in the
cutoff and the volume. (iv) Say what the interacting case needs.

**T3 (H-src, target).** State H-src for the action density as UV stability with a position-dependent bare coupling, in a
form where the divergent local counterterms drop out exactly; prove that it bounds the connected Schwinger functions of
the action density at separated supports; reduce it to a multiscale local polymer representation of log Z.

**T4.** A section "What a reader needs to trust".

Check x2 criteria are in checks/x2_criteria.md (written before checks/x2_*.py).

---

## 10. Session 2 results

### 10.1 T1: asymptotic-freedom form of non-triviality

Notation. For a coarse link b of Λ_m and u ∈ SU(N), T_{b,u}: C_m → C_m multiplies V_b on the left by u and fixes every
other link; it preserves Haar measure on C_m. For a coarse plaquette p with b ∈ ∂p, oriented to start with b,
V_p = V_bY with Y independent of V_b, so (T_{b,u}V)_p = uV_p. P_p := N^{-1}Re tr V_p, so 1 - P_p = |V_p - 1|²/(2N).

**H-Bal-3L (one-link density ratios on a local regular event). HYPOTHESIS (new; no source) [RX12-fix 1]** (*new
hypothesis*: no source states it in this form; session 3 derives it from H-loc-LF, Theorem LF⇒3L in §11.3). There are α ∈ (0, 1], A_1, E_1 < ∞ and η_L ∈ [0, 1/4], **independent of K and of the volume**, such that
for every m, every K ≥ m and every coarse link b: ν_{K,m} has a density ρ w.r.t. Haar on C_m, and there is a Borel set
G_b ⊂ C_m with ν_{K,m}(C_m \ G_b) ≤ η_L such that for every V ∈ G_b, ρ(V) > 0, and for every X ∈ su(N) with |X| = 1 and
real |s| < α:
  ρ(T_{b,e^{sX}}V)/ρ(V) = q(s) exp(-(1/g_{m,K}²) a(s) + e(s)),
with q(s) ∈ [1/3, 3], and a, e (depending on V, b, X) real on real s, extending holomorphically to the complex disc
|s| < α, with a(0) = e(0) = 0, |a| ≤ A_1 and |e| ≤ E_1 there.
- *Relation to H-Bal-3 [RX12-fix 4; session-2 remark corrected].* Session 2 read off q ∈ [1/3, 3] from |R| ≤ 1/2 with
  G_b = R_m(ε_0/2). Both steps fail: (i) |R| ≤ 1/2 is withdrawn (fix 3); under e^{±C_R|Λ_m|} the one-link ratio of
  (1 + R) has no volume-uniform bound; (ii) R_m is a **global** event and ν(R_m(ε_0/2)) → 0 in large volume, so it
  cannot serve as G_b with ν(G_b^c) ≤ 1/4. H-Bal-3 does not give H-Bal-3L; H-Bal-3L is a new local hypothesis. What
  would give it: volume-uniform decay of the dependence of the background U_k(V) and of the polymers on V_b away from b
  (CMP 102 Proposition 9, (190) [via P NOTES §9.7]) and a localised large-field remainder (CMP 122 [not-read]); this is
  §11's H-loc-LF.
- *Domain fix [RX12-fix 9].* With a local event of the form {|V_p - 1| < ε_0/3 near b}, take **α ≤ ε_0/3** (not ε_0/2):
  a shift e^{sX} with |s| close to ε_0/2 can push |V_p - 1| past ε_0, since e^{|s|} - 1 > |s|.

**H-Bal-3T (per-plaquette tail). HYPOTHESIS (new; no source) [RX12-fix 1]** (*new hypothesis*; Dimock-analogue
plausibility only: CMP 109 uses the fixed threshold ε_0, the g p(g) thresholds come from Dimock's φ⁴_3). There is
p_* > 1/2 such that, with
p(x) := (log(1/x))^{p_*}, for every coarse plaquette p, every m and K ≥ m, uniformly in the volume:
ν_{K,m}(|V_p - 1| ≥ g_{m,K} p(g_{m,K})) ≤ g_{m,K}².
- *Source analogue (ARGUED).* Dimock's φ⁴_3 large-field split uses thresholds p_k = (-log λ_k)^p on rescaled fields
  with a factor e^{-O(1)p_k²} per large-field cube (Dimock II, eqs. 9-12 [via P NOTES §2]); e^{-c p²} ≤ x² for small x
  when 2p_* > 1. The YM transposition (field = g × rescaled field) is [unverified].

**Lemma C2 (second difference from a holomorphic bound). PROVEN-HERE.** If f is holomorphic on |z| < α, f(0) = 0 and
|f| ≤ A there, then |f(s) + f(-s)| ≤ (8/3)A s²/α² for real |s| ≤ α/2.
*Proof.* f(s) + f(-s) = 2Σ_{k≥1}c_{2k}s^{2k} with |c_n| ≤ A/α^n (Cauchy), so |f(s) + f(-s)| ≤ 2A x/(1 - x) with
x = (s/α)² ≤ 1/4, and 2x/(1 - x) ≤ (8/3)x. ∎

**Lemma LAP-1 (one-link anti-concentration). PROVEN-HERE | H-Bal-3L.** Put C_* := (4/3)(A_1 + γ²E_1)/α². If
g := g_{m,K} ≤ α/2 and 0 < r ≤ 1/(2π), then for every coarse plaquette p:
  ν_{K,m}(|V_p - 1| < r g) ≤ η_L + 3π r e^{C_*}.
*Proof.* Fix b ∈ ∂p and X ∈ su(N), |X| = 1. Let ρ_0 := rg and S := G_b ∩ {|V_p - 1| < ρ_0}.
(1) *Pair inequality.* For V ∈ S and real |s| ≤ g (so |s| ≤ α/2), H-Bal-3L and Lemma C2 give
ρ(T_{e^{sX}}V)ρ(T_{e^{-sX}}V)/ρ(V)² = q(s)q(-s)exp(-(a(s) + a(-s))/g² + e(s) + e(-s)) ≥ (1/9)exp(-(8/3)(A_1/g² + E_1)s²/α²),
so by AM-GM ρ(T_{e^{sX}}V) + ρ(T_{e^{-sX}}V) ≥ 2c ρ(V) with c := (1/3)e^{-C_*} (using s² ≤ g², g ≤ γ). Haar invariance of
T gives ν(T_uS) = ∫_S ρ(T_uV)dV, hence ν(T_{e^{sX}}S) + ν(T_{e^{-sX}}S) ≥ 2c ν(S).
(2) *Disjointness.* If W ∈ T_uS ∩ T_{u'}S then W_p = uV_p = u'V'_p with V, V' ∈ S, and by unitary invariance of |·|,
|u - u'| ≤ |1 - V_p| + |V'_p - 1| < 2ρ_0. So T_uS and T_{u'}S are disjoint when |u - u'| ≥ 2ρ_0.
(3) *A packing on one one-parameter subgroup.* Let iθ_k be the eigenvalues of X (Σθ_k² = 1, |θ_k| ≤ 1). For real
|σ| ≤ π, |e^{σX} - 1|² = Σ_k 4 sin²(σθ_k/2) ≥ (4/π²)σ². Put t := πρ_0, J := ⌊1/(πr)⌋ ≥ 1/(2πr), u_i := e^{itX} for
0 < |i| ≤ J. Then |i - i'|t ≤ 2Jt ≤ 2g ≤ π, so |u_i - u_{i'}| = |e^{(i-i')tX} - 1| ≥ (2/π)|i - i'|t ≥ 2ρ_0 for i ≠ i', and
every |it| ≤ Jt ≤ g. By (2) the 2J sets T_{u_i}S are disjoint, so 1 ≥ Σ_{i=1}^J [ν(T_{u_i}S) + ν(T_{u_{-i}}S)] ≥ 2Jc ν(S).
Hence ν(S) ≤ 1/(2Jc) ≤ πr/c = 3πr e^{C_*}, and ν(|V_p - 1| < ρ_0) ≤ ν(S) + ν(G_b^c). ∎

**Theorem X-NTAF (two-sided bound on the block plaquette with AF-type running, given the flow hypothesis). PROVEN-HERE |
H-Bal-1, H-Bal-3L, H-Bal-3T** (H-Bal-3L, -3T: new hypotheses; "uniformly in the volume" uses the M-uniformity of
H-Bal-1 [RX12-fix 2, 11]).
Put δ_* := e^{-2C_*}/(288π²N). Assume γ ≤ min(α/2, e^{-p_*}). Then for every m, every coarse plaquette p of Λ_m, and
every limit point ω (finite volume, X-ALG, or infinite volume, X-IV), writing P_{p,m} := N^{-1}Re tr V^{(m)}_p:
  (δ_*/2) / (1/g² + β' m log L) ≤ ω(1 - P_{p,m}) ≤ φ(G_m),  G_m := (1/g² + β m log L)^{-1/2},
  φ(x) := x²(p(x)²/(2N) + 2).
The same two bounds hold for E_K[1 - P_{p,m}] at every K ≥ m, uniformly in K and in the volume.
*Proof.* Lower: with r_* := e^{-C_*}/(12π) (≤ 1/(2π)) and δ_* = r_*²/(2N), {1 - P_p < δ_*g²} = {|V_p - 1| < r_*g}; LAP-1
gives probability ≤ η_L + 1/4 ≤ 1/2, so E_K[1 - P_p] ≥ (δ_*/2)g_{m,K}² ≥ (δ_*/2)/(1/g² + β'm log L) by H-Bal-1.
Upper: on {|V_p - 1| < g_{m,K}p(g_{m,K})}, 1 - P_p < g²p(g)²/(2N); elsewhere 1 - P_p ≤ 2, on probability ≤ g² (H-Bal-3T).
So E_K[1 - P_p] ≤ φ(g_{m,K}). φ is increasing on (0, e^{-p_*}] (d/dx[x² log(1/x)^{2p_*}] = 2x log(1/x)^{2p_*-1}(log(1/x) - p_*)),
and g_{m,K} ≤ G_m by H-Bal-1. 1 - P_{p,m} is a block generator (bounded, continuous, gauge invariant), so ω(1 - P_{p,m})
is the limit of E_{K_j}[1 - P_{p,m}] along the defining subsequence, and both bounds pass. ∎

**Corollary X-NTAF-AF (AF-type running of the block plaquette, given H-Bal-1, -3L, -3T). PROVEN-HERE | same.**
[RX12-fix 11] The asymptotic-freedom behaviour is an **input** (H-Bal-1); the corollary converts it into a statement
about the state. As m → ∞ at fixed g:
  δ_*/(2β' log L) ≤ liminf m·ω(1 - P_{p,m}),  ω(1 - P_{p,m}) ≤ (1 + o(1)) (½ log m)^{2p_*}/(2Nβ m log L).
So the block plaquette at physical scale μ = L^m tends to its free (flat) value 1 and the deviation decays
**logarithmically in μ** (between 1/log μ and (log log μ)^{2p_*}/log μ). Consequences: (i) in infinite volume the
projective family (ν_{*,m})_m is not dilation invariant (a dilation-invariant family has m-independent ω(1 - P_{p,m}), but ω(1 - P_{p,0}) > 0
and ω(1 - P_{p,m}) → 0); (ii) no power-law approach ω(1 - P_{p,m}) ≤ C L^{-θm}, θ > 0, is possible (lower bound);
(iii) at every finite resolution the limit is not flat. This excludes massless free fields with canonical scaling
(m-independent block laws) and any theory whose block plaquettes approach the free value with a power (anomalous
dimension) — both by statements about the constructed state under these hypotheses only, not about perturbation
theory.

**Corollary X-WIL (unconditional instance). PROVEN-HERE; novelty unverified [RX12-fix 12].** An elementary rigorous
lower bound; not to be headlined (δ_W ≈ 2·10⁻³⁴ in d = 4, N = 2, against the true ≈ 3/8 in x2 A3). Literature status:
§11.6. For the Wilson SU(N) lattice gauge theory in any dimension d
on any finite periodic lattice with β = 2N/g² and g ≤ 1/2: 1 - ⟨P_p⟩ ≥ δ_W g²/2 with δ_W := e^{-2C_W}/(288π²N),
C_W := (16/3)(d - 1)√N(e - 1).
*Proof.* Density exp(-(1/g²)Σ_p|U_p - 1|²) with respect to Haar, so H-Bal-3L holds with G_b = everything, η_L = 0, q ≡ 1,
e ≡ 0, α = 1, and a(s) = Σ_{p∋b}(|e^{sX}U'_p - 1|² - |U'_p - 1|²) (each plaquette rotated, and inverted if needed, to begin
with b; |W - 1| = |W^{-1} - 1| and is conjugation invariant). For real s, |W - 1|² = 2N - tr W - tr W^*; the holomorphic
extension of each term is -tr((e^{sX} - 1)U') - tr(U'^*(e^{-sX} - 1)), of modulus ≤ 2√N|e^{sX} - 1| ≤ 2√N(e^{|s|} - 1),
and there are 2(d - 1) plaquettes per link, so A_1 = 4(d - 1)√N(e - 1). Apply LAP-1 and the lower half of X-NTAF at
fixed g (no H-Bal-1 needed). ∎ (Constants are far from sharp: check x2 A.)

**Check x2 A (criteria first, PASS).** 2D open-boundary SU(2) Wilson model (plaquettes i.i.d.), where H-Bal-3L holds
exactly with A_1 = 9.72, C_* = 12.96, δ_* = 9.7e-16. A1, A2: the lemma's bounds hold at g = 0.05-0.5 (trivially, the
constants being lossy). A3 (expectation): E[1 - P]/g² = 0.37494 at g = 0.05 against the Gaussian value 3/8. A4: the
core pair inequality ν(T_uS) ≥ c_s ν(S) holds in all 12 cases; the measured ratio is 0.37-0.94 against c_s = 2e-6 to 0.44.
- **Discrimination [RX12-fix, review §7].** A1 and A2 are **not discriminating**: the bound is ~10⁻¹⁸ against a
  measured ~10⁻³, so no plausible error in LAP-1 could fail them. A4 is the real test and passes with margin. The script
  checks the one-sided ν(T_uS) ≥ c_sν(S), while the criterion states the ± sum; they are equivalent here by the
  u ↔ u^{-1} symmetry of the model (the plaquette law is conjugation- and inversion-invariant), which should have been
  stated in the criterion. No load-bearing PROVEN claim rests on x2 that the written proof does not carry.

**X-NTAF-sharp (OPEN; the wall named).** Target: ω(1 - P_{p,m}) = c_blk g_m²(1 + o(1)) with g_m² ~ 1/(2b_0 m log L)
and c_blk := (N² - 1)κ_blk/(4N), κ_blk := lim_r ||Π_ex ψ^{(r)}||² the Gaussian block-plaquette constant of §10.2
(0.105 at depth 3 on a coarse 2⁴ torus, check x2 B2; finite-volume, informational). Two separate walls:
- **W-AF1 (flow coefficient):** β = β' = 2b_0 log L + o(1) in H-Bal-1. CMP 109 Theorem 2 gives only some 0 < β ≤ β',
  with the proof deferred by Balaban (P NOTES §9.4; "no statement β_j → 2b_0 log L appears in CMP 109").
- **W-AF2 (= H-corr, §10.2):** a Gaussian comparison for block observables in the small-field region, uniform in the
  depth: it would replace p(g)² by O(1) in the upper bound and give the coefficient c_blk. LAP-1 uses only one-link
  density ratios; the upper bound needs the joint fluctuation of the whole block, which is a correlation-function
  statement (Dimock III: "can be adapted to treat correlation functions as well", not done [via P]).

### 10.2 T2: time continuity (ker T = 0)

**Lemma X-KER (the kernel sees only the reflection plane). PROVEN-HERE | X-OS.** In the setting of X-OS, let
𝔄_{++}(d) ⊂ 𝔄_+ be the C*-subalgebra generated by the block generators all of whose blocks lie in {x_0 ≥ Π_0 + d},
d ∈ 2D_+, and 𝔄_{++} := ∪_d 𝔄_{++}(d). Then [𝔄_{++}] ⊂ 𝒦^⊥. Hence: (i) 𝒦 = {0} iff [𝔄_{++}] is dense in H_ω; (ii) it
suffices (**H-bl**, boundary-layer approximation) that every element F of the *-algebra generated by the block
generators of 𝔄_+ be an L²(ω)-limit of elements of 𝔄_{++}; (iii) H-cont-time (L²(ω)-continuity of time translations on generators) implies H-bl.
*Proof.* For G ∈ 𝔄_{++}(d) and s := d: τ_{-s}G ∈ 𝔄_+ (its blocks are translated by -s ∈ D and stay on the positive side;
translated generators are generators), and T(s)[τ_{-s}G] = [G]. So [G] ∈ Ran T(s). T(s) is bounded self-adjoint with
ker T(s) = 𝒦 (X-OS (iii)), so closure(Ran T(s)) = 𝒦^⊥. **Reverse inclusion [RX12-fix 6].** For F ∈ 𝔄_+ and s ∈ 2D_+,
τ_sF ∈ 𝔄_{++}(s) (proof of (iii)), so T(s)[𝔄_+] ⊂ [𝔄_{++}(s)] ⊂ [𝔄_{++}]; and T(s)[𝔄_+] is dense in
closure(Ran T(s)) = 𝒦^⊥ ([𝔄_+] is dense in H_ω and T(s) is bounded). Hence **closure[𝔄_{++}] = 𝒦^⊥ exactly**, and
(i) follows: 𝒦 = {0} iff [𝔄_{++}] is dense. (ii): ||[F] - [G]||²_OS = ω(θ(F - G)^*(F - G)) ≤
||θ(F - G)||_{L²(ω)}||F - G||_{L²(ω)} = ||F - G||²_{L²(ω)} (θ preserves ω), so L²-approximation gives OS-approximation
and [F] ∈ 𝒦^⊥ for every such F; these F are norm-dense in 𝔄_+, hence [·]-dense in H_ω. (iii): τ_sF ∈ 𝔄_{++}(s) for F ∈ 𝔄_+. ∎
- H-bl involves no translation: it asks that block observables touching Π_0 be insensitive, in L²(ω), to the block
  variables in a thin layer at Π_0. It is weaker than H-cont-time.

**Lemma X-2GRID (two-grid comparison = one resolution's law + one two-grid step). PROVEN-HERE.** Let n > m, K ≥ n,
s = jL^{-n}e (e a coordinate vector, j ∈ Z), and let W := V^{(n)}_{K,0} ~ ν_{K,n}. Then (i) V^{(r)}_{K,s} = V^{(r)}_{K,0}
for every r ≥ n (as functions on Ω_K); (ii) after identifying the s-translated resolution-r lattice (r < n) with Λ_r
by translation, V^{(n-1)}_{K,s} = A(τ_{-j}W) where (τ_{-j}W)(b) := W(b + je), and V^{(m)}_{K,s} = A^{n-1-m}(A(τ_{-j}W));
(iii) therefore for every block generator F = f(V^{(m)}|_X):
  F(V^{(m)}_{K,s}) - F(V^{(m)}_{K,0}) = Φ(A(τ_{-j}W)) - Φ(A(W)),  Φ := f ∘ A^{n-1-m}(·)|_X,
and the joint law of (V^{(m)}_{K,0}|_X, V^{(m)}_{K,s}|_X) is the push-forward of the single-resolution law ν_{K,n} under
the deterministic map W ↦ (Φ̃(A(W)), Φ̃(A(τ_{-j}W))), Φ̃ := A^{n-1-m}(·)|_X.
*Proof.* (i) For r ≥ n, s ∈ L^{-r}Z^4, so the s-translated tilings at all resolutions ≥ r coincide with the standard ones
(the tiling by cubes of side L^{-r'} is invariant under translations in L^{-r'}Z^4 ⊃ L^{-r}Z^4), and the block maps are
defined by the tilings. (ii) The s-translated resolution-(n-1) tiling is the standard one translated by j resolution-n
sites; the averaging formula is translation covariant, so its output on the translated blocks equals A applied to the
translated input. Coarser levels: the s-translated hierarchy is the translate of the standard one. (iii) is (i)-(ii). ∎
- **Reading.** "Uniform control of joint laws on two grids" is a statement about the law of ONE resolution n, tested on
  functions of the form Φ∘A∘τ_{-j} - Φ∘A. The two hierarchies differ in exactly one averaging step, on two grids offset by
  j/L of a block. With X-KER and X-OS, 𝒦 = {0} ⇐ for every m, f, X: sup_K E_{ν_{K,n}}|Φ(A(τ_{-j}W)) - Φ(A(W))|² → 0 as
  n → ∞ with j = 2 (s_n = 2L^{-n} ∈ 2D_+).

**Lemma X-CONT-G (the two-grid estimate in the free abelian Gaussian model). PROVEN-HERE.**
Setting: fine torus (Z/nZ)^4 in fine units; the field strength F = dA of the noncompact abelian model with action
(β/2)||dA||², i.e. the Gaussian measure on 2-forms with covariance β^{-1}Π_ex (Π_ex the orthogonal projector onto exact
2-forms); the linearised S4' averaging (P's Q_root) iterated r times; block side ℓ := L^r ≤ n/2. For a level-r plaquette P
(plane μν) let F^{(r)}_s(P) be the curvature of the level-r block field on the grid translated by s ∈ Z^4 (fine units).
(i) (composite flux) F^{(r)}_0(P) = ⟨ψ_P, F⟩ with ψ_P := ℓ^{-4}Σ_{y∈B(P)} 1_{Sq_y}, Sq_y the straight ℓ × ℓ square of fine
plaquettes in the μν plane with corner y, B(P) the level-r block of the base point of P (side ℓ); F^{(r)}_s(P) = ⟨τ_sψ_P, F⟩.
(ii) For s = je_a, 0 ≤ j ≤ ℓ, w := j/ℓ: E|F^{(r)}_s(P) - F^{(r)}_0(P)|² ≤ (4/β)w if a ∉ {μ, ν}, ≤ (4/β)w² if a ∈ {μ, ν}.
(iii) E|F^{(r)}_0(P)|² ≤ 1/β (scale invariance), uniformly in r, n.
*Proof.* (i) One step is P's Lemma 2.2(i) (LINEAR_PACKAGE §2), re-derived here: in dA'(P) = A'(X, μ) + A'(X + e_μ, ν)
- A'(X + e_ν, μ) - A'(X, ν), pair the four contour averages by the common (σ, offset u = y - LX); the axial legs at the
shared roots cancel, leaving the boundary of the straight L × L square at LX + u; averaging over (σ, u) gives
avg_{u}Φ_A(sq_{LX+u}). Induction: if the level-q curvature is avg_{y∈B_q}Φ_A(Sq^{(q)}_y), then the level-(q+1) curvature is
avg_{y'}Σ_{P' ∈ sq'_{y'}} avg_{u}Φ_A(Sq^{(q)}_{c_{P'} + u}) = avg_{y', u}Φ_A(Sq^{(q+1)}_{L^q y' + u}) (fluxes add; the
squares with a common offset u tile the big square), and (y', u) ↦ L^q y' + u is a bijection onto B_{q+1}. Translation
covariance of the linear map gives the shifted statement. (ii) Var⟨φ, F⟩ = β^{-1}||Π_exφ||² ≤ β^{-1}||φ||². With
(B + s) \ B and B \ (B + s) slabs of jℓ³ sites, τ_sψ - ψ = w(ψ_top - ψ_bot), ψ_slab := (jℓ³)^{-1}Σ_{y∈slab}1_{Sq_y}, so
||τ_sψ - ψ||² ≤ 4w² max||ψ_slab||² and ||ψ_slab||² ≤ ||ψ_slab||_∞||ψ_slab||_1 with ||ψ_slab||_1 = ℓ². A plaquette p lies
in Sq_y only if y agrees with p in the two directions transverse to the plane and lies in an ℓ × ℓ window in the plane:
if a ∉ {μ, ν} the slab condition fixes one transverse coordinate, so the count is ≤ ℓ² and ||ψ_slab||_∞ ≤ 1/(jℓ),
||ψ_slab||² ≤ ℓ/j, giving 4w²ℓ/j = 4w; if a ∈ {μ, ν} the count is ≤ jℓ, ||ψ_slab||_∞ ≤ ℓ^{-2}, ||ψ_slab||² ≤ 1, giving 4w².
(iii) ||ψ||² ≤ ||ψ||_∞||ψ||_1 ≤ ℓ^{-2}·ℓ². ∎
- Consequence: for f Lipschitz (constant Λ) in the block curvatures of finitely many coarse plaquettes X,
  E|f(F_s|_X) - f(F_0|_X)|² ≤ Λ²|X|(4/β)w: H-cont with exponent 1/2 (in L²) in this model, uniformly in the cutoff and the
  volume. (RP of this model is not re-derived here; only the estimate is claimed.)
- Caveats (review): (i) the composite-flux formula is P's Lemma 2.2(i), re-derived above; check x2 B **does not test
  (i)** (it builds ψ from (i) and checks the norm bounds), so (i)'s check status is that of P's check of Lemma 2.2(i).
  (ii) x2 B1 tests only 4w for both orientations; the in-plane 4w² claim is proven but untested by x2. The data show
  V ∝ w² for both orientations, so the proven w is not sharp.

**Check x2 B (criteria first, PASS).** Exact variances from the Fourier symbol of Π_ex at L = 3, r = 1, 2, 3 (fine sides
6, 18, 54), both orientations, all j: B1 holds with max V/(4w) ≤ 0.093; B2 ||Π_exψ||² = 0.144, 0.109, 0.105. B3 (all
expectations met): (a) the **one-step** discrepancy (r = 1, j = 1) is 42% (perpendicular shift) and 67% (in-plane) of the
plaquette variance itself; (b) at fixed j = 1, V falls by a factor ≈ 9 per level (V ∝ w², sharper than the proven 4w);
(c) at fixed w = 1/3, V(r = 3)/V(r = 2) = 0.94, 0.95 (cutoff independence).

**Finding (from X-2GRID + x2 B3), narrowed [RX12-fix 10]. ARGUED (uncounted).** The single-step two-grid discrepancy is
O(w) = O(1) in every per-plaquette (local) norm: offsetting one averaging step by j/L of a block changes the next-level
plaquettes by O(1) of their own fluctuation (x2 B3(a): 42-67% in the Gaussian model; at one step the relative shift
w = j/L is not small). Smallness is visible only in a **dual norm of the composite test form**: X-CONT-G's own proof
is a single-resolution bound ⟨τ_sψ - ψ, Π_ex(τ_sψ - ψ)⟩, an H^{-1}-type norm of the one-step difference. So the
session-2 sentence "no single-step norm bound can give H-cont" was too broad: it holds for local norms only, and the
H^{-1}-type dual norm is a single-step route that is not excluded (a counterexample route to the overbroad claim).
The reducible form remains X-2GRID's: a single-resolution law tested on composite functions, or equivalently a
dual-norm bound on the one-step difference.

**What the interacting case needs (OPEN; implication ARGUED).**
- **H-corr (two-point domination of block curvature, every resolution).** Uniformly in K ≥ n, n and the volume, for the
  level-n block plaquette logarithms 𝔉^{(n)} parallel-transported to a common coarse root (small-field gauge) and every
  test 2-form χ: E_{ν_{K,n}}|⟨χ, 𝔉^{(n)}⟩|² ≤ C_c g_n²||χ||²_{ℓ²}, on the small-field event.
- **H-lin (linearisation of the composite averaging).** The level-m block plaquette log of A^{n-m}(W) (either grid) equals
  the transported linear average ⟨ψ, 𝔉^{(n)}⟩ up to an error o(1) in L²(ν_{K,n}) as n → ∞, uniformly in K.
- ARGUED: H-corr + H-lin ⇒ H-cont-time, by X-2GRID and the proof of X-CONT-G (which uses only ||Π_exφ|| ≤ ||φ||, i.e.
  exactly an ℓ²-domination, so β^{-1} → C_c g_n²). Then 𝒦 = {0} by X-KER.
- **Why the single-step small-field statement is not provable with the current layer-1 package.** In Balaban's step
  (CMP 109 (2.13) [via P NOTES §9.5]) the δ-constraint fixes A(W) on one grid; the other grid's A(τ_{-j}W) is an
  unconstrained functional of the fluctuation field, and its law needs the fluctuation covariance C^{(k)} =
  (C*Δ^{(k)}C)^{-1} at general backgrounds (Balaban CMP 99 propagators [not-read]; P's node N5, OPEN). P's linear package
  controls background-response kernels (B_k ↦ r, f_0; exponentially local, N2-exp), not that covariance
  (LINEAR_PACKAGE §9 "Not the fluctuation covariance"). H-corr is the same correlation input as W-AF2: one wall.

### 10.3 T3: sources for the action density

Put Y_K(h) := -Σ_p h(x_p)|U_p - 1|² (x_p the plaquette centre, h real, bounded, Borel). Then
E_K[e^{zY_K(h)}] = Z_K[1/g_0² + zh]/Z_K[1/g_0²], the ratio of Wilson partition functions with the **position-dependent
bare inverse coupling** 1/g_0(x)² = 1/g_0² + zh(x) (density exp(-Σ_p (1/g_0(x_p)²)|U_p - 1|²)). An additive O(1) shift of
1/g_0² is, to leading order, the same shift of the renormalised 1/g² (∂(1/g_0²)/∂(1/g²) → 1 under H-Bal-1-type flows;
ARGUED), so this is the source conjugate to the RG-invariant combination g_0²tr F²_can (ARGUED; at separated points
⟨g_0²F²(x) g_0²F²(y)⟩_c ~ g(|x - y|)⁴/|x - y|⁸, finite and non-zero).

**H-src' (n, δ, r_0): stability with a position-dependent coupling, separated supports** (hypothesis form; implied by
H-Bal-loc, Lemma X-SRC-RED below; n ≥ 2).
For real h_1, ..., h_n with |h_i| ≤ 1 and pairwise distances of supports ≥ δ > 0, put
Ψ_K(z) := log E_K[exp(Σ_i z_iY_K(h_i))], z ∈ C^n. Require: E_K[exp Σ z_iY_K(h_i)] ≠ 0 on the polydisc D := {|z_i| < r_0},
and the inclusion-exclusion
  ΔΨ_K(z) := Σ_{S⊂{1..n}} (-1)^{n-|S|} Ψ_K(z_S)  (z_S: z_i for i ∈ S, 0 otherwise)
obeys |ΔΨ_K| ≤ C_s on D, uniformly in K.

**Lemma X-SRC-CT (counterterms drop out; connected functions at separated points). PROVEN-HERE (implication).**
Under H-src'(n, δ, r_0): (i) every functional of the form Σ_x c_K(x; η|_{B(x,ρ)}) with ρ < δ/2 (a local counterterm of
range < δ/2 in the coupling field η = Σz_ih_i) contributes 0 to ΔΨ_K; (ii) the joint cumulant (connected n-point
function) of Y_K(h_1), ..., Y_K(h_n) obeys |κ_K(Y_K(h_1), ..., Y_K(h_n))| ≤ C_s r_0^{-n}, uniformly in K; (iii) along a
subsequence these cumulants converge for every tuple from a countable family of such (h_i).
*Proof.* (i) A ball of radius ρ < δ/2 meets at most one supp h_i, so each term depends on at most one z_i; for a function
independent of z_i the terms S and S ∪ {i} cancel in pairs. (ii) Ψ_K is analytic on D (finite-dimensional integral,
non-vanishing). κ_K = ∂^nΨ_K/∂z_1⋯∂z_n(0) = ∂^nΔΨ_K/∂z_1⋯∂z_n(0), since every other term of ΔΨ_K is independent of some
z_i; Cauchy's estimate on polydiscs of radii → r_0 gives the bound. (iii) Bounded sequences in C, diagonal argument. ∎
- H-src' says nothing at coincident points: the diagonal contact terms (needed for OS0 in the X-MOM sense and for
  distributions on all of T^{4n}) are **H-src'-diag, OPEN**.

**H-Bal-loc (multiscale local representation of log Z with a coupling field). HYPOTHESIS (new; no source) [RX12-fix 1]**
(*new hypothesis*; "plausible extension" in spirit only: every part of it is unstated anywhere: position-dependent
complex coupling, O(1) polymer activities at every scale, and non-vanishing of Z_K on a complex polydisc of coupling
fields). **Named part of the hypothesis (review):** Z_K[1/g_0² + η] ≠ 0 for complex ||η||_∞ < r_0, uniformly in K, is
itself a Lee-Yang/Fisher-zero-type statement for a system with ε^{-4} degrees of freedom per unit volume. In finite physical volume |T|,
for every complex coupling field η with ||η||_∞ < r_0:
  log Z_K[1/g_0² + η] - log Z_K[1/g_0²] = CT_K[η] + Σ_{r=1}^{K} Σ_{X∈𝒫_r} a_{K,r}(X; η) + R_K[η],
where 𝒫_r is the set of polymers (connected unions of cubes of physical side ML^{-r}), a_{K,r}(X; η) depends only on η|_X
with |a_{K,r}(X; η)| ≤ a_0e^{-κ d_r(X)} (d_r = tree length in units of the cube side), κ ≥ 2κ_0 (P's κ_0 ≈ 151.3), CT_K is
a local counterterm of range ρ_K ≤ ML^{-K}·O(1), and |R_K[η]| ≤ C_IR (the unit-scale remainder), all uniformly in K.

**Lemma X-SRC-RED. PROVEN-HERE | H-Bal-loc.** H-Bal-loc implies H-src'(n, δ, r_0) for every n ≥ 2, δ (with K large enough
that ρ_K < δ/2), with
  C_s ≤ 2^n [ a_0 K_0 e^{4(κ-κ_0)} |T| M^{-4} Σ_{r≥1} L^{4r} e^{-(κ-κ_0)δL^r/M} + C_IR ]   (n ≥ 2),
K_0 = e^{κ_0}/6400 the polymer-sum constant of P's Theorem CE ((g4): Σ_{X∋□}e^{-κ_0 d(X)} ≤ K_0, with Lemma CE-geo').
*Proof.* Ψ_K(z_S) = log Z_K[1/g_0² + Σ_{i∈S}z_ih_i] - log Z_K[1/g_0²] (disjoint supports: ||Σz_ih_i||_∞ < r_0). In ΔΨ_K:
CT_K drops by X-SRC-CT (i); a polymer term a(X; ·) not meeting some supp h_i is independent of that z_i and drops;
the R_K terms contribute ≤ 2^n C_IR (2^n terms, each |R_K[η_S]| ≤ C_IR). A polymer meeting
supp h_1 and supp h_2 contains a connected union of segments joining two cubes at distance ≥ δ - 4ML^{-r} (cube diameter
2ML^{-r} in d = 4), so d_r(X) ≥ δL^r/M - 4. The cubes of resolution r number ≤ |T|L^{4r}/M^4. Hence
Σ_{X meets all supports}|a(X)| ≤ |T|L^{4r}M^{-4} a_0 e^{-(κ-κ_0)(δL^r/M - 4)} Σ_{X∋□}e^{-κ_0 d(X)}, and (g4) bounds the last sum
by K_0. Each surviving polymer appears in 2^n terms of ΔΨ. Sum over r. ∎
- **Reading.** "UV stability with a position-dependent coupling" in this form gives K-uniform bounds on all connected
  correlations of the action density at separated supports; the divergent self-energies of each coupling defect (the
  ε^{-4} pieces of X-SRC-GAP) are local and cancel exactly in ΔΨ. Balaban's published theorems (constant coupling,
  Z only) do not contain H-Bal-loc.

### 10.4 What a reader needs to trust (rewritten session 3 [RX12-fix 11])

The conditional existence theorem (§0 table, §10, §11) rests on the following. **Every non-soft conclusion rests on
hypotheses that no published paper states** (items 5-7).
1. **Standard analysis** (named where used): Banach-Alaoglu and metrizability of the state space of a separable C*-algebra;
   Gelfand duality; Riesz representation; Portmanteau; Montel in several variables; Cauchy estimates; the spectral theorem
   and uniqueness of positive roots of positive operators; Minlos and the Schwartz kernel theorem (only for X-MOM).
2. **Lattice reflection positivity of the Wilson action** (Osterwalder-Seiler; re-derived in P and re-read here).
3. **H-Bal-1** (coupling flow): bare couplings g_0(ε, g) exist with 1/g² + β m log L ≤ 1/g_{m,K}² ≤ 1/g² + β' m log L and
   g_{m,K} ≤ γ, for some 0 < β ≤ β', **with all constants independent of the torus side M** (M-uniformity: unverified,
   needed for every "uniformly in the volume" and for reading X-IV as one theory). *Balaban states it* for SU(2), proof
   deferred and unseen; SU(N) and M-uniformity: *plausible extension*. Used only for (c), (d).
4. **H-Bal-3(3a)-form** (*Balaban states it*, for the small-field RG): the background action plus localised polymers
   with the (0.28)-(0.30) bounds, analytic on Balaban's domains; background field and response decay [second-hand].
5. **H-loc-LF** (§11.2, new): the full block law has the (3a)-form on the regular region of every configuration, with the
   large-field remainder a sum of local polymer activities and per-plaquette large-field probability ≤ C_Pe^{-a_P/g²}.
   It is assumed **for the S4c map** (the S4c-compatibility of the large-field bookkeeping is part of it). It replaces
   session 2's H-Bal-3 full-law packaging, H-Bal-3G and H-Bal-3L. Used for (c) weak form, the lower bound of (c)-AF, (d).
6. **H-sg** (§11.4, new): small-field moderate deviations of one block plaquette. Used only for the upper bound of (c)-AF.
7. **For sources:** H-Bal-loc (new; multiscale local representation of log Z with a complex coupling field, including a
   Lee-Yang-type non-vanishing of Z_K on a polydisc of coupling fields).
Not used anywhere: **H-Bal-2** (Balaban's published Z-stability bound). Unconditional (no hypothesis beyond 1-2): part
(a) (a consistent limit state on all block and flowed observables, finite and infinite volume), RP for all L-adic
planes, L-adic translation and hypercubic invariance, the OS Hilbert space with H ≥ 0 on 𝒦^⊥ (possibly 𝒦^⊥ = CΩ), X-KER,
X-2GRID, X-WIL. **These are standard compactness and RP arguments**; Magnen-Rivasseau-Sénéor already describe this layer
(NOTES §2); new in substance are only X-S4c, X-CONS and X-KER [RX12-fix 11]. Not delivered under any of the above:
𝒦 = {0} (needs H-corr + H-lin, OPEN), rotation invariance, OS0 at coincident points, uniqueness, clustering, mass gap.

---

## 11. Session 3 (2026-10-27): large-field localisation

### 11.0 Pre-stated targets (written before any derivation below, after reading RLARGE.md §0-§12 and LINEAR_PACKAGE §1-§5)

**T5 (main).** State ONE named large-field localisation hypothesis **H-loc-LF** for the law ν_{K,m} of the S4c block
variables, aligned as closely as possible with the layer-1 target RLF (RLARGE.md §1: large-field remainders as polymer
activities with e^{-κd} decay and per-cube weight C e^{-a/g_k²}), and prove
  **H-Bal-3L ⇐ H-Bal-3(3a)-form [Balaban states it] + H-loc-LF**,
with every constant independent of K and the volume, using the one-link increment analysis of the background action
via P's linear package (N2-E, N2-lin, N2-exp). Then, if possible, derive H-Bal-3G (or what it is used for, X-IVND) and
H-Bal-3T from the same H-loc-LF; otherwise name exactly what is missing.
**Success:** the number of new hypotheses carried by the theorem goes down; each derived item is PROVEN-HERE | H-loc-LF
(+ named Balaban-stated items). **Valid failure outcomes:** a precisely named wall (which part of H-loc-LF is not
enough, and why).
**Alignment deliverable:** say whether H-loc-LF = RLF, and if not, exactly where they differ (soft kernel vs Balaban's
averaging; what RLF states vs what H-loc-LF needs).
**Not success:** a hypothesis that restates H-Bal-3L; constants that depend on the volume.

**T6.** Literature status of X-WIL (open access only; tag what is read).

**T7.** A word-for-word, conservative public statement (§12).

No numerical check is planned for T5 (all steps are inequalities on stated hypotheses); if one is run, its criteria
file is written first.

# Session 3 derivations (written after §11.0)

### 11.1 Notation
Resolution m, Balaban step index k = K - m, g := g_{m,K} (H-Bal-1), |·| the HS norm (§9). Coarse M-cubes ("cells") Q of
Λ_m; polymers X are connected unions of cells. For a coarse link b, N(b) := the 2(d - 1) coarse plaquettes containing
b. For V ∈ C_m, a cell is **regular** if every coarse plaquette meeting it has |V_p - 1| < ε_0; Ω(V) := the union of the
regular cells (a local function of V). **G_b := {V : |V_p - 1| < ε_0/3 for every p ∈ N(b)}.** For X ∈ su(N), |X| = 1,
and s ∈ C, V_s := T_{b,e^{sX}}V (complexified at the link b only).
- (Fact Ω) If V ∈ G_b and s is real with |s| < α ≤ ε_0/3, then Ω(V_s) = Ω(V). *Proof.* Only the plaquettes p ∈ N(b)
  change; after rotating/inverting p to begin with b (|W - 1| = |W^{-1} - 1|, conjugation invariant) the new value is
  e^{sX}W with |e^{sX}W - 1| ≤ |e^{sX} - 1| + |W - 1| < |s| + ε_0/3 < ε_0, using |e^{sX} - 1|² = Σ_k|e^{isθ_k} - 1|² ≤
  s²Σθ_k² = s² for real s. These plaquettes were regular before and are after; no other plaquette changes. ∎

### 11.2 The hypothesis H-loc-LF (stated once; every quantifier explicit)

**H-loc-LF (large-field localisation of the block law). HYPOTHESIS (new; no source).** There are ε_0 ∈ (0, 1],
α ∈ (0, ε_0/3], δ_0 > 0, κ ≥ κ_0 + 1 (κ_0 := P's Theorem CE constant), and C_bg, C_a, c_V, α_1, H_0, C_+, C_R, E_+, C_P,
a_P < ∞ (> 0 where needed), **all independent of K, of the torus sides and of m** (for g ≤ γ), such that for every m,
every K ≥ m and every V ∈ C_m:
  ρ_{K,m}(V) = 𝒵^{-1} exp( -(1/g²)A^η_{Ω(V)}(V) + E_{Ω(V)}(V) + Σ_Y H(Y; V) ),
with the three parts below.
- **(LF-a) Small-field part = Balaban's (3a)-form, localised to the regular region.** A^η_Ω(V) ≥ 0 is the background
  action of the region Ω with background U_{k,Ω}(V), and E_Ω = Σ_{j≤k}Σ_{X∈D_j, X⊂Ω}V^{(j)}(X; V) Balaban's
  renormalised polymers, with: (P1) V^{(j)}(X; V) = f_X(H_X(V)), H_X the background on X in Balaban's local (Landau)
  coordinates, f_X holomorphic on the polydisc ||H||_∞ < α_1 with |f_X| ≤ c_V(L^jη)^{4+α_B}e^{-κd_j(X)} (α_B > 0
  Balaban's exponent); (P2) for V ∈ G_b, s ↦ H_X(V_s) is holomorphic on |s| < α, ||H_X(V_s)||_∞ ≤ α_1/2 and
  ||H_X(V_s) - H_X(V)||_∞ ≤ C_bg e^{-δ_0 dist(X, b)} (dist in coarse units); (P3) A^η_Ω = Σ_cells a_c(H_c), a_c
  holomorphic on the same polydisc with |a_c| ≤ C_a; (P4) Σ_X|V^{(j)}| summed over all j and X ⊂ Ω is ≤ E_+|Λ_m|.
  *Provenance:* for Ω = everything (V ∈ R_m(ε_0)) this is H-Bal-3(3a)-form (*Balaban states it*: (0.28)-(0.30) on the
  regular domain; the background field and the decay of its response, CMP 102 Theorem 1 and Proposition 9 (190), cited
  in CMP 109 p.263, 271 [second-hand]); the extension of (0.29) to the complex polydisc with the same constant is a
  *plausible extension*; **the localisation to regions Ω(V) with large-field complement is new** (CMP 116/122, unread).
- **(LF-b) Large-field remainder = local polymer activities (the RLF-aligned part).** H(Y; V) depends only on V on the
  links of Y. (b1) For V ∈ G_b, s ↦ H(Y; V_s) (Ω(V) frozen) is holomorphic on |s| < α for every Y ∋ b, real on real s,
  with sup_{|s|<α}|H(Y; V_s) - H(Y; V)| ≤ H_0 e^{-κd(Y)}; for Y ∌ b, H(Y; V_s) = H(Y; V). (b2) Σ_{Y∋Q} sup_V H(Y; V)^+ ≤
  C_+ for every cell Q. (b3) On R_m(ε_0), |Σ_Y H(Y; V)| ≤ C_R|Λ_m|.
- **(LF-P) Large-field probability with RLF's per-cube weight.** For every coarse plaquette p,
  ν_{K,m}(|V_p - 1| ≥ ε_0/3) ≤ C_P e^{-a_P/g²}.
*Reading.* (LF-b) is "the remainder after the R-operation factorises into polymer activities with an e^{-κd} bound"
(Dimock II's large-field polymers; RLF-2/RLF-3), stated at a fixed coarse field. (LF-P) is the probability form of
RLF-3's per-cube weight C e^{-a/g_k²}. Nothing in H-loc-LF is a one-link density-ratio statement: the one-link content
is derived below.

### 11.3 The one-link reduction

**Lemma BG-1L-lin (one-link increment of the background energy, linear soft model). PROVEN-HERE | P's N2-E (Theorem
2.6), N2-lin (Theorem 3.8), N2-exp (Theorem 4.2'), Lemma 2.5 (all reviewed in P).** In P's Setting SC (linearised soft
chain, one real component, κ_- ≤ κ_i ≤ κ_+), let E_k(B) := min over (B_0, …, B_{k-1}) of the chain energy, b a coarse
link, e_b its indicator 1-form. For every B and every s ∈ C:
  E_k(B + s e_b) - E_k(B) = -κ_{k-1} r_{k-1}(b) s + E_k(e_b) s²,
where r_{k-1} is the top residual at any minimiser for B; moreover 0 ≤ E_k(e_b) ≤ 2(d - 1)C_E(1 + κ_+),
|r_{k-1}(b)| ≤ C_R sup|dB|, and |r_{k-1}(b)| ≤ M Σ_P e^{-m'|P - b|_1}|dB(P)| for every m' < m_*'. Hence on |s| < α the
increment is a polynomial bounded by κ_+C_R sup|dB| α + 2(d - 1)C_E(1 + κ_+)α², uniformly in k and the torus, and the
field far from b enters only with weight e^{-m'·dist}.
*Proof.* E_k is the minimum of a positive semidefinite quadratic form over a subspace of its variables, hence a
positive semidefinite quadratic form in B: E_k(B + se_b) = E_k(B) + 2s𝔅(B, e_b) + s²E_k(e_b). Let (B*_i) minimise at B.
q(s) := E(B*_0, …, B*_{k-1}; B + se_b) - E_k(B + se_b) is a real quadratic in real s, ≥ 0, with q(0) = 0, so q'(0) = 0;
B_k enters E only through (κ_{k-1}/2)||QB_{k-1} - B_k||², so 2𝔅(B, e_b) = d/ds E(B*; B + se_b)|_0 =
κ_{k-1}⟨QB*_{k-1} - B, -e_b⟩ = -κ_{k-1}r_{k-1}(b) (r_{k-1} is the same at every minimiser, Lemma 2.5). Extend to complex s
by polynomial identity. E_k(e_b) ≤ C_E(1 + κ_+)||de_b||² (N2-E) and de_b = ±1 on the 2(d - 1) plaquettes containing b.
The sup bound is N2-lin (H2); the weighted bound is N2-exp (ii) for the kernel 𝓡 (F ↦ r_{k-1} on all 2-forms). ∎
- *Scope.* This is the soft-kernel, abelian, linearised background. Balaban's δ-constraint background is the hard limit
  κ → ∞, where C_E(1 + κ_+) and C_R(L, κ_±) are not uniform; the hard-constraint linear instance is **not** covered by
  P's package. The nonabelian Balaban-form bound used below is Lemma BG-1L-B, from (P2)-(P3).

**Lemma BG-1L-B (one-link increment of Balaban's background action). PROVEN-HERE | (LF-a) (P2), (P3).** For V ∈ G_b
and |s| < α (Ω = Ω(V) frozen): |A^η_Ω(V_s) - A^η_Ω(V)| ≤ A_bg := 2C_aC_bgC_4(δ_0)/α_1, C_4(δ) := Σ_{r≥0}c_d(r + 1)^{d-1}e^{-δr}
(c_d(r + 1)^{d-1} bounds the number of cells at coarse distance in [r, r + 1) from b).
*Proof.* For h, h' in the polydisc of radius α_1/2, a function f holomorphic on radius α_1 with |f| ≤ S obeys
|f(h') - f(h)| ≤ 2S||h' - h||_∞/α_1 (Cauchy on the one-variable slice z ↦ f(h + z(h' - h)/||h' - h||) at every point of the
segment, which stays in the convex polydisc of radius α_1/2). Apply it to each a_c with (P2): |Δa_c| ≤ 2C_aC_bg
e^{-δ_0 dist(c,b)}/α_1. Sum over cells. ∎

**Lemma POL-1L (one-link increment of Balaban's polymer sum). PROVEN-HERE | (LF-a) (P1), (P2).** For V ∈ G_b and
|s| < α: Σ_jΣ_{X∈D_j, X⊂Ω}|V^{(j)}(X; V_s) - V^{(j)}(X; V)| ≤ E_bg := 2c_V(C_bg/α_1)K_0C_4(δ_0)M^{-4}/(1 - L^{-α_B}),
uniformly in K and the volume.
*Proof.* By the slice estimate and (P1)-(P2), each term is ≤ 2c_V(L^jη)^{4+α_B}e^{-κd_j(X)}(C_bg/α_1)e^{-δ_0 dist(X,b)}.
Assign each X to a cell □ ∈ X nearest to b (dist(□, b) = dist(X, b)); Σ_{X∋□}e^{-κd_j(X)} ≤ K_0 (P's (g4), κ ≥ κ_0).
Scale-j cells have coarse side ML^{j-k} = ML^jη, so there are ≤ c_d(r + 1)^{d-1}(ML^jη)^{-4} of them at coarse distance in
[r, r + 1) from b, and Σ_□e^{-δ_0 dist(□,b)} ≤ C_4(δ_0)(ML^jη)^{-4}. The j-th level contributes ≤ 2c_V(C_bg/α_1)K_0C_4
M^{-4}(L^jη)^{α_B}, and Σ_{j≤k}(L^{j-k})^{α_B} ≤ (1 - L^{-α_B})^{-1}. ∎
- This is the mechanism of Balaban's (0.30) ("bulk dependence only"), applied to one-link increments.

**Theorem LF⇒3L. PROVEN-HERE | H-Bal-1, H-loc-LF.** Put g_LF := (a_P/log(8(d - 1)C_P))^{1/2} (any g_LF > 0 if
8(d - 1)C_P ≤ 1). If g_{m,K} ≤ g_LF, then H-Bal-3L holds with
  G_b as in §11.1, η_L := 2(d - 1)C_P e^{-a_P/g²} ≤ 1/4, q ≡ 1, α as in H-loc-LF, A_1 := A_bg, E_1 := E_bg + H_0K_0,
all independent of K and the volume.
*Proof.* (Probability.) G_b^c ⊂ ∪_{p∈N(b)}{|V_p - 1| ≥ ε_0/3}; (LF-P) and |N(b)| = 2(d - 1) give ν(G_b^c) ≤ η_L, and
η_L ≤ 1/4 iff g² ≤ a_P/log(8(d - 1)C_P). (Ratio.) Fix V ∈ G_b, X with |X| = 1. ρ(V) > 0 since the exponent is finite.
For real |s| < α, Fact Ω gives Ω(V_s) = Ω(V) =: Ω, so in log ρ(V_s) - log ρ(V) the regular region, the polymer index
set {X ⊂ Ω} and 𝒵 do not change, and the H(Y)-terms with Y ∌ b cancel (LF-b1). Hence
  ρ(V_s)/ρ(V) = exp(-(1/g²)a(s) + e(s)),  a(s) := A^η_Ω(V_s) - A^η_Ω(V),
  e(s) := Σ_{X⊂Ω}[V(X; V_s) - V(X; V)] + Σ_{Y∋b}[H(Y; V_s) - H(Y; V)].
Each term extends holomorphically to |s| < α ((P1)-(P3), (LF-b1); the polymer sum converges uniformly by the bound of
POL-1L, so the sum is holomorphic), vanishes at s = 0, and is real on real s. |a| ≤ A_bg (BG-1L-B); |e| ≤ E_bg +
H_0Σ_{Y∋b}e^{-κd(Y)} ≤ E_bg + H_0K_0 (POL-1L, (LF-b1), (g4)). ∎
- **Consequence.** LAP-1, X-NTAF's lower bound, X-NTAF-AF's lower half and X-WIL's structure hold **| H-Bal-1, H-loc-LF**
  with γ ≤ min(α/2, e^{-p_*}, g_LF); H-Bal-3L is no longer a carried hypothesis.

### 11.4 What else H-loc-LF gives

**Corollary LF⇒3 (full-law packaging; X-ND without (3b); the fixed-threshold part of 3T). PROVEN-HERE | H-Bal-1,
H-loc-LF.**
(i) On R_m(ε_0), ρ_{K,m} has H-Bal-3(3a)'s full-law form with 1 + R := exp(Σ_YH(Y; V)) ∈ [e^{-C_R|Λ_m|}, e^{C_R|Λ_m|}].
(ii) X-ND (i), (iii) hold without (3b): on int R_m(ε_0), ν_{*,m} ≥ c_m·Haar with c_m := e^{-(E_+ + C_+)|Λ_m|}c', c' of X-ND.
(iii) For every coarse plaquette p and g ≤ g_T (g_T > 0 with C_Pe^{-a_P/g_T²} ≤ g_T²/2 and x ↦ C_Pe^{-a_P/x²}/x² increasing
on (0, g_T]): H-Bal-3T holds if **H-sg** holds, where
  **H-sg (small-field moderate deviations). HYPOTHESIS (new; no source).** ν_{K,m}(g p(g) ≤ |V_p - 1| < ε_0/3) ≤ g²/2,
  uniformly in K and the volume (g = g_{m,K}, p as in H-Bal-3T).
*Proof.* (i) On R_m(ε_0) every cell is regular, Ω = everything, A^η_Ω = A^η(U_k(V)) and E_Ω = E_{K,m} ((LF-a) with
Ω = everything is the (3a)-form); (LF-b3). (ii) 𝒵 = ∫exp(-(1/g²)A^η_Ω + E_Ω + Σ_YH) dHaar ≤ exp(E_+|Λ_m| + C_+|Λ_m|),
using A^η_Ω ≥ 0, (P4) and (LF-b2) (each Y meets a cell; sum over cells), and Haar(C_m) = 1. On R the integrand is ≥ c'
as in X-ND (with (i)). So ρ ≥ c'e^{-(E_+ + C_+)|Λ_m|} on R; Riesz as in X-ND. No lower bound on ν(R) is used. (iii) The
event splits into {|V_p - 1| ≥ ε_0/3} (probability ≤ C_Pe^{-a_P/g²} ≤ g²/2 by (LF-P)) and the H-sg window. ∎
- **Not Haar** (X-ND (iv)) now comes from (LF-P), see X-IVND'.

**Proposition X-IVND' (infinite-volume non-degeneracy). PROVEN-HERE | H-Bal-1 (with M-uniformity), H-loc-LF.** If
γ ≤ min(α/2, e^{-p_*}, g_LF), every limit point (finite or infinite volume) satisfies, for every m and coarse plaquette p:
(i) ω(1 - P_{p,m}) ≥ (δ_*/2)/(1/g² + β'm log L) > 0 (not flat), and (ii) ν_{*,m}(|V_p - 1| > ε_0/3) ≤ C_Pe^{-a_P/γ²}.
If C_Pe^{-a_P/γ²} < Haar{W ∈ SU(N) : |W - 1| > ε_0/3} (= 1 - O(ε_0^{N²-1})), the limit is not Haar, uniformly in the volume.
*Proof.* (i) Theorem LF⇒3L and X-NTAF's lower half. (ii) The set is open and |V_p - 1| is a coarse-gauge-invariant
continuous function of block generators, so Portmanteau gives ν_* ≤ liminf ν_{K_j}, and (LF-P) with g_{m,K} ≤ γ. A
single coarse plaquette is Haar distributed under Haar measure on C_m, so ν_* = Haar would violate the inequality. ∎
- X-IVND | H-Bal-3G (§3) remains a proven implication; H-Bal-3G is no longer carried by any conclusion.

**Where 3T stops (the wall, named).** H-sg is a *concentration* statement at the Gaussian scale g p(g) inside the
small-field region. One-link density ratios with holomorphic increments give anti-concentration (LAP-1) but not
concentration: the bound |a| ≤ A_1 on a disc controls a(s) + a(-s) only to ±(8/3)A_1s²/α², and concentration needs
a(s) + a(-s) ≥ +c s² with c of order 1 in the 1/g² units for *all* configurations, plus control of the staples
(a one-link move changes 2(d - 1) plaquettes at once). H-sg is a Gaussian-domination input for one block plaquette,
the same kind of input as W-AF2/H-corr (§10.1-10.2), and also the variable-threshold form of RLARGE's (PLD) (i).
(LF-P) at the fixed threshold ε_0/3 does not imply it.

### 11.5 H-loc-LF against RLF (RLARGE.md §1, read this session)

**They are not the same statement.** Exact differences:
- **(D1) The random variable (soft kernel vs Balaban's averaging).** RLF is for the soft normalised-kernel chain
  (decision 4): the level-k variable U_k is drawn from K_k(·, U_{k-1}), a Markov chain with noise of size ~g/√κ per
  link. H-loc-LF is for the deterministic S4c block average V^(m) = A^{K-m}(U) (a diagonal-pairing variant of Balaban's
  δ-function constraint (0.17)). No comparison theorem between the two laws exists in either lane.
- **(D2) The leading action.** RLF's representation (I_k) (RLARGE §8.1) carries the local Wilson action
  (1/g̃_k²)Σs(U_p) of the level variable (coupling shifted by δβ); its one-link increment is exact and local
  (A_1 = 4(d - 1)√N(e - 1), as in X-WIL). H-loc-LF carries Balaban's background action A^η_Ω (nonlocal); its one-link
  increment needs the response decay (P2): BG-1L-B, whose soft linear analogue is BG-1L-lin (N2-E, N2-lin, N2-exp),
  with the hard-constraint limit not covered.
- **(D3) Form.** (I_k) is a sum over histories with RLF-3 weights; H-loc-LF is exponentiated at a fixed coarse field.
  Passing from one to the other needs Theorem CE applied to the history gas at a fixed level field; RLARGE (P5) does
  this only for the level-K vacuum. ARGUED (session-scale).
- **(D4) Probability.** (LF-P) is a bound for the true law at level K - m. In RLARGE the multi-point Peierls bound is the
  hypothesis (PLD)_k for the all-cut measure, an *input* to Proposition RLF-step, not an output of RLF.
- **(D5) Regularity.** H-loc-LF needs holomorphy in each regular coarse link on a disc of fixed radius α (increments of
  size O(1/g²) allowed). RLF / Proposition CL (d) state C³ bounds (Λ_1/g²)^q. The frozen activities r_Y are real-analytic
  in the data (the indicators do not depend on the data), but analyticity on a fixed radius is not stated.
- **(D6) Thresholds.** Op-norm ε_1 on level-k interior plaquettes (RLF) vs HS-norm ε_0 on coarse plaquettes; equivalent
  up to √N (inequality (B)).
- **Shared:** the per-cube weight C e^{-a/g²} with a ∝ ε²/(4N) (Proposition CL (c)); polymer activities with e^{-κd}
  tails; the coupling flow (F) = H-Bal-1.

**Where the lanes can meet: RLF-loc.** Let **H-loc-LF^S (= "RLF-loc")** be H-loc-LF with (D1)-(D2) switched to the soft
side: the variable is the soft-chain level variable at level K - m, and A^η_Ω is replaced by (1/g̃²)Σ_{p}s(U_p)
(BG-1L-B is then not needed). Then:
- RLF + (I_{K-m}) + [CE at fixed field] + (PLD)_{K-m} for the true law ⇒ RLF-loc: **ARGUED** (D3, D4 are the gaps).
- Theorem LF⇒3L, Corollary LF⇒3 and X-IVND' hold verbatim for RLF-loc, with A_1 = 4(d - 1)√N(e - 1) + (polymer part).
- The soft layer transfers to soft block variables (**"Option S"**, ARGUED, uncounted): RP (X-RP^S) holds because, for a
  positive-side observable, every coarse variable whose kernel crosses the reflection plane is unobserved and
  integrates out exactly (∫K_k dV = 1), top level first; the remaining kernels are local, positive and reflection
  covariant (S4' family B_4-symmetric), so ω(θ(F)F) = E_Wilson[θ(F̃)F̃] with F̃ a bounded measurable function of the
  positive-side fine links, and X-LRP applies. Consistency across resolutions holds for the Markov-projective family;
  shifted grids use independent kernels. Not written out; listed OPEN.
So **H-loc-LF ≠ RLF**. With Option S, the two lanes meet at one hypothesis, RLF-loc, which differs from RLF only by
(D3) and (D4). Without Option S, they differ also by (D1)-(D2), and the δ-constraint version needs its own large-field
analysis (CMP 116/122, unread).

### 11.6 X-WIL: literature status (T6; open access only)
Searches (two web searches, 2026-10-27) for a rigorous lower bound 1 - ⟨P⟩ ≥ c/β, c > 0, for Wilson lattice gauge theory
at weak coupling found no paper stating it. Sources:
- **Chatterjee, "The leading term of the Yang-Mills free energy", arXiv:1602.01222 (J. Funct. Anal. 2016)** [read-skim:
  abstract and HTML text via a page summariser, sections 1-16; not read line by line]. Theorem 2.1 gives the leading
  term of the free energy of U(N) lattice gauge theory on boxes B_n = {0, …, n-1}^d, as n → ∞ and g_0 → 0 with no
  relation between them: the free energy per site minus ½(d - 1 - d/n + 1/n^d)N² log(g_0²) tends to an explicit
  constant. The page summary reports Theorem 8.1, a tail bound for the action: P(βS > Cn^d log β + t) ≤ e^{-t} for
  β ≥ 2 (an upper bound of order log β/β per plaquette). I found no statement about the mean plaquette or a lower bound
  on 1 - ⟨P⟩.
  - *Consequence (my derivation, ARGUED; not stated in the paper).* log Z is convex in β, so E_β[S]/n^d ≥
    (f(β) - f(2β))/β with f the free energy per site; Theorem 2.1 gives f(β) - f(2β) → ½(d - 1)N² log 2. So, for U(N)
    on boxes, an asymptotic lower bound E[S] ≥ (½(d - 1)N² log 2 - o(1))n^d/β follows, with a far better constant than
    δ_W but with an unquantified o(1), on boxes (not tori), and for U(N) (not SU(N)). X-WIL is explicit, finite-volume,
    any β with g ≤ 1/2, SU(N), periodic. Its type of result is therefore close to, but not stated in, this work.
- **Brennecke, arXiv:2511.07297** [read-abs]: an explicit characterisation of Chatterjee's constant K_d; no plaquette
  bound in the abstract.
- **Kazakov-Zheng, arXiv:2203.11360; Li-Zhou, arXiv:2404.17071; Guo et al., arXiv:2502.14421** [read-abs via search
  summaries]: rigorous two-sided *numerical* bootstrap bounds on the plaquette at given couplings (positivity plus
  loop equations), not an analytic c/β bound.
- Seiler's 1982 lecture notes and the chessboard/Peierls literature [not-read].
**Status:** no prior statement of X-WIL found; novelty **unverified** (one-link Laplace / convexity arguments of this
type may be folklore); the convexity route above shows an asymptotic version follows from a published free-energy
theorem. Do not headline it.

### 11.7 Outcome against the pre-stated targets
- **T5: MET in part.** H-loc-LF is one named hypothesis. H-Bal-3L ⇐ H-Bal-1 + H-loc-LF (Theorem LF⇒3L), the H-Bal-3
  full-law packaging ⇐ H-loc-LF (Corollary LF⇒3 (i)), and (3b) is no longer needed (X-ND re-proven). H-Bal-3G is no
  longer needed (X-IVND'). H-Bal-3T ⇐ H-loc-LF + H-sg: **not reduced**; the wall is the small-field concentration
  statement H-sg (§11.4). The small-field part of H-loc-LF is Balaban's (3a)-form; its localisation to regions and the
  remainder/probability parts are new. N2-exp enters through BG-1L-lin (the soft linear instance of the background
  increment); the nonabelian increment uses the response decay (P2) that Balaban cites from CMP 102.
- **Alignment:** H-loc-LF ≠ RLF (D1-D6). Via Option S the lanes can meet at RLF-loc (ARGUED, gaps D3, D4).
- **T6:** §11.6. **T7:** §12.
- New hypotheses carried by the theorem: 5 → 3 (H-loc-LF, H-sg, H-Bal-loc).

---

## 12. Current honest public statement (session 3; supersedes the review's draft only by the §11 changes)

Word for word:

> For four-dimensional SU(N) lattice Yang-Mills theory with the Wilson action, we give an unreviewed conditional
> argument with the following content. Unconditionally, by compactness and Osterwalder-Seiler reflection positivity
> (standard arguments), along subsequences of lattice spacings L^{-K} → 0 the lattice measures define limit states on
> a separable algebra of block-averaged variables (a continuous, gauge-covariant averaging map at every L-adic
> resolution and shift) and of gradient-flowed lattice Wilson loops. These states are consistent across resolutions,
> reflection positive for every L-adic block-boundary hyperplane, invariant under L-adic translations and the
> hypercubic group, and yield an Osterwalder-Schrader Hilbert space with a positive self-adjoint generator H on the
> orthogonal complement of the kernel of the transfer operator; that complement may be one-dimensional, in which case
> H is trivial. Under two additional hypotheses, (1) a coupling flow 1/g_m² ≈ 1/g² + O(m log L), uniform in the volume,
> which Balaban states for SU(2) with its proof deferred and not seen by us, and (2) a large-field localisation
> hypothesis on the laws of the block variables (on regular regions they have the form of Balaban's published
> small-field effective action, the large-field remainder is a sum of local polymer activities, and a block plaquette
> is far from 1 with probability at most C e^{-a/g²}), which no published work states, the limit block plaquette at
> resolution L^{-m} satisfies ⟨1 - P⟩_m ≥ c/(1/g² + β' m log L), uniformly in the volume; so the limit is neither
> flat nor Haar at any resolution. With a third hypothesis that no published work states either, a moderate-deviation
> bound for a single block plaquette in the small-field region, also ⟨1 - P⟩_m ≤ C (log m)^{2p}/m, so the limit is not
> scale invariant. Time continuity (kernel of the transfer operator = 0), Euclidean invariance, the OS regularity
> axiom for local fields, uniqueness, clustering and a mass gap are not established. This is not a construction of
> Yang-Mills theory, and it does not rest on any published large-field theorem.

Changes from the review's draft (REVIEW_X1_X2, public-claim audit): the three local hypotheses (one-link ratios, tail,
Gibbs form) are replaced by one large-field localisation hypothesis plus one small-field moderate-deviation
hypothesis; the lower and upper bounds are now stated with their separate hypotheses; "possibly trivial" is spelled
out. The elementary Wilson-action bound X-WIL is not part of the public statement (novelty unverified, §11.6).
