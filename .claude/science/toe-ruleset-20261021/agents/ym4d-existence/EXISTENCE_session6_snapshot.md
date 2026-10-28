# YM4D existence from UV stability: a conditional lemma DAG (sessions 1-6, 2026-10-27)

Session 6 added §15 (compact SU(N) soft noise: no bias at O(σ²); 𝒦^S = {0} unconditionally; H-cont^S reduced; the
ASSEMBLY statement §15.6). §0-§14 are unchanged except the session-6 lines in §0 and §6. EXISTENCE_session5_snapshot.md
is the pre-session-6 copy.

Session 5 applied the binding fixes of REVIEW_X3_X4.md (each tagged **[RX34-fix]**) and added §14 (the decisive test
of the soft variables: the free Gaussian soft chain; and a time-continuity route for soft variables in the OS
seminorm). EXISTENCE_session4_snapshot.md is the pre-fix copy.

Session 3 applied the 12 binding fixes of REVIEW_X1_X2.md (each tagged **[RX12-fix]**), relabelled every hypothesis by
provenance, and added §11 (large-field localisation H-loc-LF; X-WIL literature) and §12 (current honest public
statement). Sessions 1-2 text is otherwise unchanged; EXISTENCE_session2_snapshot.md is the pre-fix copy.
Session 4 added §13 (the lanes merged on layer 1's soft-kernel variables: reflection positivity of soft blocking,
chessboard estimates, H-sg reduced). §0-§12 are unchanged except the session-4 tally lines in §0 and §6 and the
session-4 addendum to §12.

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
(sessions 1-2: H-Bal-3 in its full-law packaging, -3G, -3L, -3T, -loc; session 3, §11: H-loc-LF, H-sg, H-Bal-loc
[RX34-fix 11]; session 4, §13, soft branch: (RLF-3^dis), (PLD^mod_dis), and the soft-scheme flow (F), a *plausible
extension of H-Bal-1 (different RG scheme; layer-1 node A5, OPEN)*, not a Balaban statement [RX34-fix 11]).
The published Z-stability theorem (H-Bal-2) is not sufficient for them and is not used. The only Balaban statements used
are the small-field *form* of the effective action (H-Bal-3(3a), for the small-field RG) and the coupling flow
(H-Bal-1, SU(2), proof deferred and unseen). What compactness gives for free, and what each extra hypothesis buys:

| Part | Delivered | From |
|---|---|---|
| (a) subsequential continuum limits, finite volume | **YES**: a single limit state ω on a separable commutative C*-algebra containing every block observable (all resolutions, all L-adic shifts) and every flowed lattice Wilson loop; consistent across resolutions | compactness alone (X-ALG, X-CONS), with the **continuous** block map X-S4c |
| (b) OS structure | **RP** for every L-adic block-boundary plane, **L-adic translations**, hypercubic symmetry, gauge invariance; on R×T³: OS Hilbert space, positive contraction semigroup T(s) = T(2)^{s/2}, **Hamiltonian H ≥ 0 on (ker T)^⊥, which may be CΩ: possibly trivial without (c)-type input [RX12-fix 10]** (standard dense-lattice-time OS argument; not new) | lattice RP (Osterwalder-Seiler, re-verified) + compactness (X-RP, X-OS) |
| (b) not delivered | time continuity (ker T = 0), rotation invariance (OS1), OS0 for local fields | need H-cont, H-rot, H-src (OPEN; not in Balaban). Session 2: ker T ⊥ everything supported off the plane (X-KER); two-grid laws = one resolution's law + one two-grid step (X-2GRID); estimate proven in the free Gaussian model (X-CONT-G); interacting case ⇐ H-corr + H-lin (ARGUED). Sources: separated-support correlations of the action density bounded **| H-Bal-loc** (X-SRC-CT, X-SRC-RED) |
| (c) non-triviality | **weak form YES, given H-Bal-1 and H-Bal-3 (full-law packaging: new hypothesis; session 3: given H-loc-LF, §11)** [RX12-fix 11]: at every resolution the limit block law is neither flat nor Haar, and on small fields it has a density of Balaban's form with an analytic effective action; Taylor coefficients of order n are O(g^n) | X-ND, X-MONTEL, X-CAUCHY |
| (c) AF-type running of the block plaquette, given the flow hypothesis (session 2) [RX12-fix 11] | **given H-Bal-1, H-Bal-3L, H-Bal-3T (new hypotheses; session 3: given H-Bal-1, H-loc-LF, H-sg, §11 [RX34-fix 11]), two-sided, volume-uniform**: (δ_*/2)/(1/g² + β'm log L) ≤ ω(1 - P_{p,m}) ≤ φ(G_m), so block plaquettes approach the free value logarithmically in the scale (not dilation invariant, no power law) | X-NTAF, X-NTAF-AF **| H-Bal-1, H-Bal-3L, H-Bal-3T** (§10.1) |
| (c) not delivered | non-Gaussianity (connected 4-point ≠ 0); the sharp coefficient c_blk g_m² with g_m² ~ 1/(2b_0 m log L) | OPEN (X-NT2; X-NTAF-sharp: walls W-AF1 flow coefficient, W-AF2 = H-corr) |
| (d) infinite volume | limit points exist with all of (b)'s soft structure; non-degeneracy **| H-Bal-3G** (volume-uniform Gibbs/finite-energy form; new hypothesis); session 3: not flat and not Haar **| H-Bal-1 (M-uniform), H-loc-LF** (X-IVND', §11) [RX34-fix 11] | X-IV, X-IVND, X-IVND' |
| (d) not delivered | uniqueness, clustering (OS4), mass gap, rotation invariance via universality | OPEN (IR; need a gap or cluster expansion) |

**Tally (session 3): PROVEN-HERE 29 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 (H-Bal-1, H-Bal-2,
H-Bal-3(3a)-form) / HYPOTHESIS-NEW 3 (H-loc-LF, H-sg, H-Bal-loc) / OPEN 11.** After the 12 binding fixes alone (session 3
step 1) the tally was the review's corrected one: 24 / 1 / 3 / HYPOTHESIS-NEW 5 (H-Bal-3 full-law packaging, -3G, -3L,
-3T, -loc) / 11. §11 then adds 5 PROVEN-HERE items and replaces 4 new hypotheses by H-loc-LF + H-sg (H-sg is H-Bal-3T
restricted to the small-field window, so the reduction of H-Bal-3T is **nominal** [RX34-fix]). (Session 2 claimed
24 / 1 / 7 / 11 with the new hypotheses mislabelled as imported; session 1: 16 / 1 / 4 / 9.) Itemised in §6. Session-2
work is §9-§10; session 3 is §11; the reader's trust list is §10.4; the public statement is §12.
- **Session 4 (§13) [tally: PROVEN-HERE 36 / IMPORTED-AND-REVERIFIED 2 / IMPORTED-NOT-YET-REVERIFIED 3 /
  HYPOTHESIS-NEW 5 / OPEN 10]; corrected by REVIEW_X3_X4 to 37 / 1 / 3 / 5 / 10 (Lemma CBE relabelled PROVEN-HERE)
  [RX34-fix 3].** Soft-variable branch (layer 1's chain): (a), (b), (d)-soft structure with RP for every
  plane in P with one-sided continuum supports, no hypothesis (X-RP^S); not flat and a lower bound from the kernel alone
  (no information about the Wilson measure); not Haar, volume-uniformly, | (RLF-3^dis), (F) ((RLF-3^dis) follows under
  an unadopted reading of RLF-3, plus RLF-1, RLF-4, node A [RX34-fix 5]); the AF upper bound | (RLF-3^dis),
  (PLD^mod_dis), (F). Bridge: chessboard estimates (Theorem CB).
- **Session 5 (§14) [tally: PROVEN-HERE 40 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 /
  HYPOTHESIS-NEW 5 / OPEN 10].** The decisive test of the soft variables **passes**: in the free Gaussian (abelian,
  linear) soft chain the accumulated kernel noise at fixed resolution m **converges** as K → ∞, geometrically (noise
  injected n levels below contributes (4σ²/3)(2L^{-2n} + L^{-4n}) to the block-plaquette variance; operator norm of the
  block-curvature covariance ≤ g_0² + 16Σ_nσ²L^{-2n}); no log K in any gauge-invariant quantity (Theorem GS). The free
  Gaussian instance of (PLD^mod_dis) holds for the soft chain, unconditioned law (Corollary PLD-G^S). For time
  continuity, the false L² route is replaced by the OS-seminorm criterion H-cont^S on F̃ = E[F | fine field] ⇒ 𝒦 = {0}
  (Theorem X-KER^S); H-cont^S holds in the free Gaussian soft chain (Corollary X-CONT-G^S) and is OPEN in the
  interacting case. Compact non-abelian corrections: ARGUED only.
- **Session 6 (§15) [tally: PROVEN-HERE 46 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 /
  HYPOTHESIS-NEW 5 / OPEN 11].** Compact soft noise: exact one-step convolution, no location drift (SU(2)); no additive
  drift of any block holonomy at any depth (all N); the O(σ²) part of the compact floor is Theorem GS's damped sum
  (check x5 PASS); uniformity of the remainder named (NA-R2). 𝒦^S = {0} unconditionally (Theorem X-KER^S (iv)), so
  H-cont^S is needed only for spatial continuity; the interacting H-cont^S is reduced to (H-corr^S) + (H-lin^S = NA-R2).
  The assembled conditional theorem and its hypothesis list: §15.6.
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
**[RX34-fix 2] For the soft variables of §13 this L² form is FALSE** (REVIEW_X3_X4 §5): for a ∉ L^{-m}Z⁴ the shifted and
unshifted resolution-m soft variables lie on different branches of the class tree and, given their parents, carry
independent kernel noise, so E|F(V_a) - F(V_0)|² ≥ 2E[Var(F(V_0) | parents)] ≥ c g'_m² for a block plaquette, uniformly as
|a| → 0. H-bl in L²(ω) form fails for the same reason. The deterministic (S4c) branch is unaffected. The soft replacement
(OS seminorm via F̃ = E[F | fine field]) is §14.3.
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
| HYPOTHESIS (new; no source) | 3 | H-loc-LF (§11.2; its small-field part is the (3a)-form, the localisation, (LF-b) and (LF-P) are new), H-sg (§11.4; it is H-Bal-3T on the small-field window, so the 3T reduction is nominal [RX34-fix]), H-Bal-loc. Retired in session 3 (formulated, no longer carried by any conclusion): H-Bal-3 full-law packaging (⇐ H-loc-LF), H-Bal-3G, H-Bal-3L (⇐ H-Bal-1 + H-loc-LF), H-Bal-3T (⇐ H-loc-LF + H-sg) |
| OPEN | 11 | X-NT2 (with LAP), X-NTAF-sharp (W-AF1, W-AF2), H-src-flow, H-src'-diag (contact terms), H-loc, H-cont (X-CONT, L² two-grid form; reduced), H-corr, H-lin, X-ROT, X-IR (uniqueness/OS4/gap), Option S soft-layer transfer (X-RP^S and Markov-projective consistency, §11.5; replaces session 2's "S4c-compatibility of CMP 122's bookkeeping", which is now a named part of H-loc-LF) |
| ARGUED (uncounted) | 8 | X-RAW; the ε^{-4} variance of the action density; H-corr + H-lin ⇒ H-cont; the bare additive coupling shift as the source of the RG-invariant g_0²F²; the leading coefficient c_blk; the narrowed "local-norm" single-step finding (§10.2); RLF ⇒ RLF-loc (gaps D3, D4, §11.5); the asymptotic Wilson-plaquette lower bound from Chatterjee's free energy by convexity (§11.6). (Session 2's "H-Bal-3L/3T as the local content of H-Bal-3" is withdrawn [RX12-fix 4].) |

**Session-4 update (§13).** PROVEN-HERE +7 = 36: X-RP^S (with the soft-layer transfer X-ALG^S, X-CONS^S, X-SYM^S,
X-OS^S, X-IV^S, X-2GRID^S), Proposition KB (X-ND^S, X-MONTEL^S), Proposition LAP^S, Theorem CB (with Corollary X-IVND^S),
Lemma MIX, Lemma KN (with Corollary KN-step), Theorem CB-sg (with Corollary H-Bal-3T^S). IMPORTED-AND-REVERIFIED +1 = 2:
Lemma CBE (chessboard estimate; proof written out). **[RX34-fix 3] Corrected: Lemma CBE is PROVEN-HERE (standard result;
proof written out and checked; FILS/Shlosman not read, Biskup abstract only), so the session-4 tally is PROVEN-HERE 37 /
IMPORTED-AND-REVERIFIED 1 (X-LRP) / 3 / 5 / 10.** HYPOTHESIS-NEW +2 = 5: (RLF-3^dis) (would follow from layer 1's OPEN
RLF-3, together with RLF-1, RLF-4 and node A's bulk bound, under a nonnegative-ratio reading that layer 1 has not adopted
[RX34-fix 5]; ARGUED), (PLD^mod_dis) (variable-threshold form of RLF-step's input (PLD)_k (i)).
The soft-scheme flow (F) is carried as a *plausible extension of H-Bal-1 (different RG scheme; layer-1 node A5, OPEN)*
inside the H-Bal-1 entry [RX34-fix 11].
The deterministic branch keeps H-loc-LF, H-sg, H-Bal-loc. OPEN −1 = 10: "Option S soft-layer transfer" is closed.
ARGUED +2 = 10: (RLF-3^dis) ⇐ RLF-3 (+ RLF-4) under the reading; (PLD) preserved under mixtures over histories.
**Session-5 update (§14).** PROVEN-HERE +3 = 40: Theorem GS (with Lemmas GS-1, GS-2 and Corollary PLD-G^S), Theorem
X-KER^S, Corollary X-CONT-G^S. IMPORTED-AND-REVERIFIED 1 (X-LRP; Lemma CBE moved to PROVEN-HERE [RX34-fix 3]).
HYPOTHESIS-NEW 5 (unchanged). OPEN 10 (the H-cont entry now has the deterministic L² form and the soft form H-cont^S;
the L² form is false for soft variables [RX34-fix 2]). ARGUED 11 (+1: compact non-abelian injected-noise corrections are
damped as in GS-2; "D3 dissolved" withdrawn and kept as an uncounted ARGUED-reduced remark [RX34-fix 8]). DAG: GS ⇐ GS-1
(⇐ layer-1 (R)), GS-2 (⇐ layer-1 Lemma 2.4), X-CONT-G (iii), A1; PLD-G^S ⇐ GS, (F); X-KER^S ⇐ X-RP^S, X-OS^S, X-LRP;
𝒦^S = {0} ⇐ X-KER^S + H-cont^S [OPEN]; X-CONT-G^S ⇐ GS-1, X-CONT-G. Check x4 PASS (A, B, C), D CONVERGES.

**Session-6 update (§15).** PROVEN-HERE +6 = 46: Lemma NA-1, Lemma NA-2, Proposition NA-3, Theorem NA-GS1, Theorem
X-KER^S (iv), Proposition H-cont^S-red. OPEN +1 = 11: (NA-R2). ARGUED 15. DAG: NA-2 ⇐ NA-1; NA-GS1 ⇐ NA-1, GS-1, GS;
𝒦^S = {0} ⇐ X-OS^S + X-KER inclusion (no hypothesis); H-cont^S_sp ⇐ H-SYN [H-cont^S-red] ⇐ H-corr^S + H-lin^S [ARGUED];
H-lin^S ≡ NA-R2. Check x5 PASS (A, B), C as expected.

DAG additions: X-RP^S ⇐ X-LRP, (C), (L); KB, LAP^S ⇐ kernel; CB ⇐ X-RP^S, CBE; X-IVND^S ⇐ CB, (RLF-3^dis);
H-Bal-3T^S ⇐ CB-sg ⇐ CB, (RLF-3^dis), (PLD^mod_dis); X-NTAF^S ⇐ LAP^S, H-Bal-3T^S, (F). Check x3 PASS (A, C); B1
informational (site-plane RP fails for the normalised kernel in the toy).

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
  G_b as in §11.1, η_L := 2(d - 1)C_P e^{-a_P/g²} ≤ 1/4, q ≡ 1, α as in H-loc-LF, A_1 := A_bg, E_1 := E_bg + 2H_0K_0
  [RX34-fix 10: "Y ∋ b" includes polymers containing either endpoint cell of b],
all independent of K and the volume.
*Proof.* (Probability.) G_b^c ⊂ ∪_{p∈N(b)}{|V_p - 1| ≥ ε_0/3}; (LF-P) and |N(b)| = 2(d - 1) give ν(G_b^c) ≤ η_L, and
η_L ≤ 1/4 iff g² ≤ a_P/log(8(d - 1)C_P). (Ratio.) Fix V ∈ G_b, X with |X| = 1. ρ(V) > 0 since the exponent is finite.
For real |s| < α, Fact Ω gives Ω(V_s) = Ω(V) =: Ω, so in log ρ(V_s) - log ρ(V) the regular region, the polymer index
set {X ⊂ Ω} and 𝒵 do not change, and the H(Y)-terms with Y ∌ b cancel (LF-b1). Hence
  ρ(V_s)/ρ(V) = exp(-(1/g²)a(s) + e(s)),  a(s) := A^η_Ω(V_s) - A^η_Ω(V),
  e(s) := Σ_{X⊂Ω}[V(X; V_s) - V(X; V)] + Σ_{Y∋b}[H(Y; V_s) - H(Y; V)].
Each term extends holomorphically to |s| < α ((P1)-(P3), (LF-b1); the polymer sum converges uniformly by the bound of
POL-1L, so the sum is holomorphic), vanishes at s = 0, and is real on real s. |a| ≤ A_bg (BG-1L-B); |e| ≤ E_bg +
H_0Σ_{Y∋b}e^{-κd(Y)} ≤ E_bg + 2H_0K_0 (POL-1L, (LF-b1), (g4); each of the ≤ 2 endpoint cells of b contributes ≤ K_0)
[RX34-fix 10]. ∎
- **Consequence.** LAP-1, X-NTAF's lower bound, X-NTAF-AF's lower half and X-WIL's structure hold **| H-Bal-1, H-loc-LF**
  when the bare coupling satisfies g ≤ min(α/2, e^{-p_*}, g_LF) (so that g_{m,K} ≤ g by H-Bal-1; γ is H-Bal-1's constant,
  not a free choice [RX34-fix 10]); H-Bal-3L is no longer a carried hypothesis.

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
- **[RX34-fix] The reduction in (iii) is nominal.** H-sg (window bound g²/2) is H-Bal-3T restricted to the small-field
  window {g p(g) ≤ |V_p - 1| < ε_0/3}, with a factor 2. So "H-Bal-3T ⇐ H-loc-LF + H-sg" trades a hypothesis for a
  slightly sharper restriction of itself; nothing about the small-field concentration is derived here.
- **Not Haar** (X-ND (iv)) now comes from (LF-P), see X-IVND'.

**Proposition X-IVND' (infinite-volume non-degeneracy). PROVEN-HERE | H-Bal-1 (with M-uniformity), H-loc-LF.** If
the bare coupling satisfies g ≤ min(α/2, e^{-p_*}, g_LF) [RX34-fix 10], every limit point (finite or infinite volume) satisfies, for every m and coarse plaquette p:
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

### 12.1 Session-4 statement, replaced in session 5 by REVIEW_X3_X4's text word for word [RX34-fix 12]

Word for word (REVIEW_X3_X4, "Public-statement verdict"):

> For four-dimensional SU(N) lattice Yang-Mills theory with the Wilson action, we give a conditional argument, checked
> only by internal reviews and not peer reviewed, with the following content. Unconditionally, by compactness and
> Osterwalder-Seiler reflection positivity (standard arguments), along subsequences of lattice spacings L^{-K} → 0 the
> lattice measures define limit states on a separable algebra of block variables at every L-adic resolution and shift
> and of gradient-flowed lattice Wilson loops. Two kinds of block variables are treated: a continuous, gauge-covariant
> block average, and the variables of a soft renormalisation-group Markov chain with normalised Gaussian-type kernels.
> For both, the limit states are consistent across resolutions, reflection positive for every L-adic block-boundary
> hyperplane (for observables supported on one side), invariant under L-adic translations and the hypercubic group, and
> yield an Osterwalder-Schrader Hilbert space with a positive self-adjoint generator H on the orthogonal complement of
> the kernel of the transfer operator; that complement may be one-dimensional, in which case H is trivial. For the soft
> variables, the limit block laws have analytic densities and fluctuate at least at the scale of the kernel coupling;
> this is a property of the kernel alone and says nothing about the Yang-Mills measure. For the continuous block average,
> under a coupling-flow hypothesis 1/g_m² ≈ 1/g² + O(m log L), uniform in the volume, which Balaban states for SU(2)
> for his renormalisation group with its proof deferred and not seen by us, and a large-field localisation hypothesis on
> the block laws that no published work states, the limit block plaquette satisfies ⟨1 - P⟩_m ≥ c/(1/g² + β' m log L),
> uniformly in the volume, and the limit is neither flat nor Haar at any resolution. For the soft variables, under the
> analogous coupling-flow hypothesis for the soft scheme (open) and an unpublished, volume-uniform bound of order
> e^{-a/g_k²} per block on the probability that every block at a given scale is a large-field block (a bound that would
> follow from a large-field theorem our sister lane is attempting, under a normalisation that lane has not yet adopted),
> the soft limit is not Haar at any resolution, uniformly in the volume; the local bound is derived from the extensive
> one by chessboard estimates. With a second unpublished hypothesis of the same extensive kind (a moderate-deviation
> bound for the small-field measure, for which no instance is established for the soft chain, even for free fields),
> also ⟨1 - P⟩_m ≤ C (log m)^{2p}/m for the soft block plaquette. Time continuity (kernel of the transfer operator = 0),
> Euclidean invariance, the OS regularity axiom for local fields, uniqueness, clustering and a mass gap are not
> established. This is not a construction of Yang-Mills theory, and it does not rest on any published large-field
> theorem.

Changes from the session-4 lane text (as listed by the review): "unreviewed" becomes "internal reviews only"; "one sided"
is added for RP; "bounded" is dropped (the density bound is volume-dependent); the deterministic statements are spelled
out, with the flow attributed to Balaban's own RG; for the soft branch the flow is labelled open; (RLF-3^dis) is
described as conditional on a reading layer 1 has not adopted; the missing free-field instance of (PLD^mod_dis) is
stated; "so the limit is not scale invariant" is deleted, because for soft variables it rests on the kernel lower bound.
The session-4 lane text is in EXISTENCE_session4_snapshot.md §12.1. Session-5 changes, if any, are in §12.2.


### 12.2 (session 5) One change to the §12.1 statement's factual basis
The §12.1 text (REVIEW_X3_X4's, kept word for word) says the moderate-deviation hypothesis has "no instance established
for the soft chain, even for free fields". Since session 5 (Corollary PLD-G^S) the free Gaussian instance holds for the
soft chain, for the unconditioned law. The proposed amended clause, for the next review to accept or reject: "(a
moderate-deviation bound for the small-field measure, which holds for the free Gaussian soft chain but is not
established for the interacting compact one)". §12.1 itself is not edited.

---

## 13. Session 4 (2026-10-27): merging with layer 1 (soft variables), and H-sg

### 13.0 Pre-stated targets (2026-10-27 22:15 UTC; written before any derivation below, after reading §11-12, LOG session 3, REVIEW_X1_X2's binding rules, P/RLARGE.md §0-§13 and P/LINEAR_PACKAGE.md §1-§11)

**T8 (merge).** Switch the block variables to layer 1's soft-kernel Markov variables (the soft RG chain of RLARGE §0,
decision-4 kernel), with shifted grids as a tree of conditionally independent branches. Then:
- (T8a) re-check every existence item ((a)-(d), X-ND, X-MONTEL, X-NTAF, X-IVND', LAP-1/H-Bal-3L, X-KER, X-2GRID) under
  the switch: proven / changed / lost;
- (T8b) reflection positivity under soft blocking: prove it for every block-boundary plane in P, or name what breaks;
  also say what happens for planes through sites;
- (T8c) prove RLF ⇒ RLF-loc, closing gaps D3 (history sum vs exponentiated form) and D4 (probability as an output).
**Success:** the conditional existence theorem rests on RLF + (F) only, each item labelled PROVEN-HERE | RLF, (F).
**Valid failure outcomes:** a precisely named statement that RLF (§1 of RLARGE, as written) does not contain and that
the existence theorem needs, with a proof that this statement suffices.
**Not success:** an implication that silently uses the layer-1 inductive hypotheses ((SF), (PLD), (W1-ret), (HIST))
as if they were RLF; any constant depending on the volume.

**T9 (H-sg).** Attack the small-field concentration bound for one block plaquette with the soft Gaussian/linear package
(energy bounds, exponential kernels, gauge-fixing gaps) and a Brascamp-Lieb / log-concavity argument in the small-field
region. **Success:** H-sg PROVEN-HERE from stated, weaker or layer-1-native inputs. **Valid failure:** the wall named
exactly (which input is missing, and why the linear package does not supply it).

**T10.** Public statement (§12) updated conservatively if anything changes; tally; LOG session 4; snapshot.

**Check plan.** If a numerical check is run, its criteria file (checks/x3_criteria.md) is written first. Candidate:
reflection positivity of a soft-blocked toy model across a block-boundary plane (must hold) and across a site plane
(informational), and the kernel concentration bound of T9 on SU(2).

# Session 4 derivations (written after §13.0)

### 13.1 Setting S: the soft block variables (layer 1's chain)
- **Chain.** Levels k = 0 (fine, spacing ε) to K (unit lattice), as in RLARGE §0; level k is resolution K - k. U_0 ~ μ_K
  (Wilson at g_0); U_{k+1} ~ K_k(·, U_k), the normalised soft kernel K_k = Π_c k_c, k_c(V_c, M̄_c(U)) =
  exp(-(κ/g_k²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))])/𝒩_k(M̄_c(U)), M̄_c the mean of the S4' contour transporters of c
  (P, D4-norm; LINEAR_PACKAGE §1.3). ∫k_c dV_c = 1. **The kernel couplings (g_k) are a free choice of the scheme**; below
  they are taken to be the sequence of the flow hypothesis (F) of RLARGE §0 (with g_K = g), which is how RLF uses them.
  The resolution-m soft block variable is **V^{(m),S} := U_{K-m}**; its law ν^S_{K,m} has Haar density
  ρ^S_{K,m} = e^{-S_{K-m}}/Z_K. Notation: g^S_m := g_{K-m} (level coupling), g'_m := g_{K-m-1} (coupling of the kernel that
  produces resolution m). Under (F), 1/g² + β_-(m+1)log L ≤ 1/g'_m² ≤ 1/g² + β_+(m+1)log L and g'_m ≤ g^S_m ≤ g.
- **Shifted grids (class tree).** For n ≤ K and a ∈ L^{-K}Z⁴ (mod the torus) let [a]_n := a mod L^{-n}Z⁴. For each n and
  class [a]_n there is one resolution-n field U^{(n)}_{[a]_n} on the grid L^{-n}Z⁴ + a; its parent is U^{(n+1)}_{[a]_{n+1}}
  (the blocks of the shifted resolution-n grid are sets of sites of the shifted resolution-(n+1) grid, which depends only on
  [a]_{n+1}); given all parents, all fields are drawn independently from their kernels. [a]_K = 0, so the tree is rooted at
  U_0. The joint law is P_K := μ_K(dU_0) Π_{(n,[a]_n,c)} k_c(V_c, M̄_c(parent)) dV_c. This is "Option S" of §11.5.
  For a ∈ L^{-n}Z⁴ the shifted and unshifted fields coincide at resolutions ≥ n (X-2GRID (i) holds by construction).
- **Locality (L).** The kernel of a resolution-n link c = (X, X + e_μ) depends only on the parent links with both ends in
  B(X) ∪ B(X + e_μ). By nesting (L odd), the ancestors of c at every finer resolution are links with both ends among the
  descendants of the sites of B(X) ∪ B(X + e_μ), and at the fine level, fine links joining fine sites of the two cells.
- **Continuity.** M̄_c is a polynomial in the link variables and 𝒩 > 0 is continuous, so every kernel is jointly
  continuous in (V, U, g) for g in compacts of (0, ∞). **X-S4c (the log cutoff) is not needed for the soft variables.**
- **Reflection covariance (C).** For a reflection θ in a plane of P (or an axis permutation), θ maps class [a]_n to
  [θa]_n (θa ∈ D since 2(j + ½)L^{-m_0} ∈ D), cells to cells, and the S4' contours of c to the contours of θc, reversed when
  θ reverses c (P's L9a' computation, used for X-S4c (iv); S4' pairing makes the far-end path a translate). So
  M̄_{θc}(θU) = M̄_c(U) or M̄_c(U)^†. With V_{θc} = V_c^{-1} in the reversed case: Re tr(VM̄^†) = Re tr(V^{-1}M̄) for unitary
  V, and 𝒩(M̄^†) = 𝒩(M̄) (substitute V ↦ V^{-1}; Haar is inversion invariant). Hence k_{θc}((θV)_{θc}, M̄_{θc}(θU)) =
  k_c(V_c, M̄_c(U)), and P_K is θ-invariant (μ_K is, X-LRP's setting).

### 13.2 The soft layer under the switch

**Theorem X-RP^S (reflection positivity of soft blocking across block-boundary planes). PROVEN-HERE | X-LRP, (C), (L).**
Let Π ∈ P_{m_0} (with its antipodal plane), θ its reflection, and 𝔉^S_+ the bounded measurable functions of finitely many
soft variables (any resolutions and classes) **whose continuum supports supp(c) := the closed union of the continuum
cubes of B(X) and B(X + e_μ) (side L^{-n}, centred at X, X + e_μ) lie in the open positive half-space** [RX34-fix 1],
together with fine links on the positive side. Then for every K above the levels involved, E_{P_K}[θ(F)^*F] ≥ 0 for
F ∈ 𝔉^S_+. (𝔄_+ for X-OS^S and X-KER is defined by the same condition; it is translation-stable.)
*Proof.* Let A_+ be the set of soft variables of F together with all their ancestors (finitely many). By (L) and nesting
(L odd maps the continuum support of a parent into the union of the continuum supports of its children's cells, i.e. an
ancestor's support lies inside its descendant's support), every variable in A_+ has its continuum support in the open
positive half-space, and its fine ancestors are positive-side fine links (fine sites never
lie on Π, a fine link mid-plane). A_- := θ(A_+) lies on the negative side, so A_+ ∩ A_- = ∅. In ∫θ(F)^*F dP_K, integrate
out every soft variable outside A_+ ∪ A_- coarsest first: each has no child among the remaining variables, and its kernel
integrates to 1. What remains is
  ∫μ_K(dU_0) [∫Π_{v∈A_-}k_v dv θ(F)^*] [∫Π_{v∈A_+}k_v dv F] = E_{μ_K}[θ(F̃)^* F̃],  F̃(U_0) := ∫Π_{v∈A_+}k_v dv F,
because the A_+-kernels depend only on A_+ ∪ {positive fine links}, and by (C) and θ-invariance of Haar the A_- integral
equals θ(F̃)^* (the kernels are real). F̃ is a bounded measurable function of the positive-side fine links, so X-LRP gives
≥ 0. ∎
- **[RX34-fix 1] Why the session-4 wording was too broad (reviewer's counterexample, recorded).** Session 4 defined
  𝔉^S_+ by "cells (all sites of B(X) ∪ B(X + e_μ)) strictly on the positive side". At L = 3, time coordinate: Π: x_0 =
  5.5/9 ∈ P_2; a resolution-0 link (X, X + e_ν) with X_0 = 1, ν spatial, has cells made of resolution-1 sites with
  x_0 ∈ {2/3, 1, 4/3}, all > Π, so it qualified; but its parent link at x_0 = 2/3 has a kernel depending on resolution-2
  sites at x_0 ∈ {5/9, 6/9, 7/9}, and 5/9 < Π. So the ancestors cross Π and the proof did not apply (the same happens for
  shifted classes). Whether RP fails for such F is not decided. Every downstream use (level-k links interior to a level-k
  cube in CBE, CB, CB-sg; τ_s of such generators in X-OS^S) satisfies the continuum-support condition.
- **What breaks: planes through sites (check x3 B).** If a plane contains sites of Λ_n, a resolution-n link c lying in the
  plane has cells straddling it, and its kernel contains 1/𝒩(M̄_c) with M̄_c = mean of positive-side, negative-side and
  in-plane contours; 1/𝒩 is not of the form G·θ(G), so the proof does not apply. In the exact toy of check x3 (a Z_3
  clock ring, blocks of 3 centred on a site plane) the site-plane Gram matrix has min/max eigenvalue -0.195 with the
  normalised kernel and is PSD (-5·10⁻¹⁶) with the unnormalised kernel exp(κRe tr V^{-1}M̄) (which, however, changes the
  fine marginal): **site-plane RP fails for the normalised soft kernel in that toy; the normalisation 𝒩 is the cause.**
  Nothing below uses site planes: X-OS uses the planes Π_0 + s/2 ∈ P only.
- **Soft-layer transfer (PROVEN-HERE, counted with X-RP^S).** With generators = coarse-gauge-invariant continuous
  functions of finitely many soft variables (the joint law is invariant under a fine gauge transformation acting on every
  level by restriction to that level's sites, since the kernels are gauge covariant at the roots), and the flowed loops
  (functions of U_0): X-ALG^S (compactness, verbatim); X-CONS^S (Markov-projective: ν^S_{K,m} = ν^S_{K,m+1}K_{K-m-1}, and
  along a subsequence with g'_m → g'_{m,*} for every m, ν^S_{*,m} = ν^S_{*,m+1}K_{g'_{m,*}} by joint continuity of the kernel;
  the gauge lift of X-CONS is unchanged); X-SYM^S (fine-lattice translations and hypercubic symmetries map the class tree
  to itself and preserve P_K by (C)); X-RP^S in the limit (weak-* limits of the finite-K inequality); X-OS^S and X-KER
  (they use only X-RP for planes in P, X-SYM and locality, so they hold verbatim); X-IV^S (bounded-support generators);
  X-2GRID^S (exact by construction: shared variables at resolutions ≥ n, conditionally independent branches below).
  **The OPEN item "Option S soft-layer transfer" (§6, §11.5) is now PROVEN-HERE.** No hypothesis is used. (All with the
  continuum-support class [RX34-fix 1].)
- **[RX34-fix 2] What "X-KER holds verbatim" leaves out.** X-KER (i) holds; (ii)-(iii) hold as implications, but for soft
  generators their hypotheses are **unsatisfiable in L²(ω) form**: shifted grids carry independent kernel noise, so
  H-cont (§4 X-CONT) and H-bl in L² form are false for soft variables (E|F(V_a) - F(V_0)|² ≥ 2E[Var(F(V_0) | parents)]
  ≥ c g'_m² for a block plaquette, uniformly as |a| → 0). X-2GRID^S's "exact by construction" is true but useless for
  H-cont. By the proof of X-RP^S, OS inner products see only F̃ := E[F | fine field]: ⟨F, G⟩_OS = E[θ(F̃)^*G̃]. So
  𝒦 = {0} for soft variables must be sought in the OS seminorm (via F̃), or taken from the deterministic branch (§14.3).

### 13.3 What the kernel gives for free (and why it carries no information about the Wilson measure)

**Proposition KB (kernel bounds on the soft block law). PROVEN-HERE | kernel only (with the sequence of (F)).** Let n_c
be the number of links of Λ_m and assume g² ≤ κ. For every K ≥ m + 1 and every V ∈ C_m,
  c_- := e^{-2κn_c/g'_m²} ≤ ρ^S_{K,m}(V) ≤ c_+ := (e c_N^{-1}(κ/g'_m²)^{N²-1})^{n_c},
and ρ^S_{K,m} extends to an entire function on SL(N, C)^{n_c}, bounded on each compact set by a constant independent of K.
Hence (X-ND^S) every limit ν^S_{*,m} satisfies c_-·Haar ≤ ν^S_{*,m} ≤ c_+·Haar (full support; not flat), and (X-MONTEL^S)
along a subsequence its density is the restriction of an entire function.
*Proof.* ρ^S_{K,m}(V) = ∫Π_c k_c(V_c, M̄_c(U))ν^S_{K,m+1}(dU). |N^{-1}tr(V^{-1}M̄)| ≤ ||M̄||_op ≤ 1, so the bracket in k_c
lies in [0, 2]: 𝒩 ≤ 1 and k_c ≥ e^{-2κ/g'²}. The upper bound is P's D4-norm (2) (as used in RLARGE Proposition CL (c)).
Complexify: k_c^C(V) := exp(-(κ/g'²)[1 - (2N)^{-1}(tr(V^{-1}M̄) + tr(M̄^†V))])/𝒩(M̄) agrees with k_c on SU(N), is entire in
V ∈ SL(N, C), and |k_c^C(V)| ≤ e^{2κ/g'²}exp((κ/g'²)(2N)^{-1}√N(||V^{-1}||_HS + ||V||_HS)), uniformly in U; dominated
convergence gives holomorphy of the integral. g'_m lies in a K-independent compact subset of (0, ∞) by (F). Riesz and
Montel as in X-ND, X-MONTEL. ∎

**Proposition LAP^S (anti-concentration of the soft block plaquette). PROVEN-HERE | kernel only.** If g'_m ≤ 1/2, then
for every coarse plaquette p of Λ_m, every K and every conditioning on the resolution-(m+1) field,
  P(|V^{(m),S}_p - 1| < r g'_m | U^{(m+1)}) ≤ 3πr e^{C^S_*}, C^S_* := (4/3)κ(e - 1)/√N (0 < r ≤ 1/(2π)),
and E_K[1 - P_p] ≥ (δ^S_*/2) g'_m², δ^S_* := e^{-2C^S_*}/(288π²N), uniformly in K and the volume; the same holds for every
limit point, finite or infinite volume (X-NTAF^S, lower half). Under (F): ≥ (δ^S_*/2)/(1/g² + β_+(m+1)log L).
*Proof.* Given U, the density of V^{(m),S} w.r.t. Haar on C_m is ρ_U(V) = Π_c k_c(V_c, M̄_c(U)). For a link b and X ∈ su(N),
|X|_HS = 1: ρ_U(T_{b,e^{sX}}V)/ρ_U(V) = exp(-(1/g'²)a(s)), a(s) := (κ/2N)[tr(V_b^{-1}(1 - e^{-sX})M̄_b) + tr(M̄_b^†(1 - e^{sX})V_b)],
entire, real on real s (the two terms are complex conjugates there), a(0) = 0, and |a(s)| ≤ (κ/N)||1 - e^{±sX}||_HS||M̄||_HS ≤
κ(e^{|s|} - 1)/√N ≤ κ(e - 1)/√N on |s| < 1. So H-Bal-3L holds for ρ_U with G_b = C_m, η_L = 0, q ≡ 1, e ≡ 0, α = 1,
A_1 = κ(e - 1)/√N, coupling g'. LAP-1 applies to ρ_U (its proof uses only these properties and Haar invariance of T_{b,u}).
Integrate over U. The expectation bound is the lower half of X-NTAF's proof with r_* = e^{-C^S_*}/(12π). Block plaquettes
are generators; pass to limits. ∎
- **Reading (important).** Both propositions are **properties of the kernel**: the soft variable carries injected noise of
  size g'/√κ per link, and any law of the finer field gives the same bounds. They are non-trivial as statements about the
  limit state, but they carry **no information about the Wilson measure**, and they must not be presented as
  non-triviality of Yang-Mills. Under the switch, the informative statements are concentration statements (not Haar, the
  upper bound), which say that the fine field's block averages are regular. The session-3 lower bound for the
  *deterministic* S4c variables (| H-Bal-1, H-loc-LF) keeps its content and is retained as the comparison branch.

### 13.4 From extensive large-field bounds to local ones: chessboard estimates for the soft chain

**Lemma CBE (chessboard estimate). PROVEN-HERE (standard result; proof written out and checked; sources not read)
[RX34-fix 3; session 4 labelled it IMPORTED-AND-REVERIFIED, which needs an exact source read]** (Fröhlich-Israel-Lieb-Simon,
CMP 62 (1978) [not-read]; Shlosman, Russian Math. Surveys 41 (1986) [not-read]; Biskup, arXiv:math-ph/0610025 [read-abs:
abstract page only; the PDF text was not extractable here]). Let T_B = Π_μ Z/(2n_μ) be a torus of
blocks; for each block t let 𝔅_t be an algebra of bounded functions ("block functions"); for each direction μ and each
pair of antipodal planes between block layers, let θ be an involutive automorphism with θ(𝔅_t) = 𝔅_{θt}, ω∘θ = ω, and
ω(θ(F)^*F) ≥ 0 for F in the algebra generated by the 𝔅_t of one half. For f ∈ 𝔅_t and s ∈ T_B let f^{[s]} ∈ 𝔅_s be its
image under any composite of reflections mapping t to s. Then for f_t ∈ 𝔅_t, f_t ≥ 0,
  ω(Π_t f_t) ≤ Π_t ω(Π_{s∈T_B} f_t^{[s]})^{1/|T_B|}.
*Proof.* (0) f^{[s]} is well defined: in one direction on Z/2n the reflections are x ↦ 2j + 1 - x; composites mapping 0 to i
are the translation by i (i even) or x ↦ i - x (i odd), one element each; directions commute. (1) *One direction.* For
layer functions G_0, …, G_{2n-1} (nonnegative, in the algebra of layer 0) put Z(G) := ω(Π_iG_i^{[i]}). RP for the plane
pair cutting the ring into {k+1-n, …, k} and its complement, and the Schwarz inequality of the form ⟨F, G⟩ := ω(θ(F)^*G),
give Z(G)² ≤ Z(G')Z(G''), where G' (resp. G'') is the tuple whose half on one side is kept and whose other half is replaced
by the mirror image of the kept half. Put z(G) := Z(G, …, G) and, after replacing each G_i by G_i + ε (ε > 0, so z > 0;
let ε → 0 at the end by continuity), R(G) := Z(G)/Π_iz(G_i)^{1/2n} over the finitely many tuples drawn from
{G_0, …, G_{2n-1}}. The denominators split exactly as the numerators, so R(G)² ≤ R(G')R(G'') and, at a maximiser, both G' and
G'' are maximisers. Among maximisers take one with a longest cyclic run of equal entries, of length ℓ. If ℓ < 2n, put the
cut at the end of the run, keep the half containing the end of the run (it contains min(ℓ, n) run entries adjacent to the
cut) and mirror it: the new maximiser has a run of length min(2ℓ, 2n) > ℓ, a contradiction. So a constant tuple is a
maximiser and max R = 1. (2) *All directions.* Apply (1) in direction 1 to F_j := Π_{t: t_1 = j}f_t; each resulting factor
ω(Π_iF_j^{[i]}) is a product of block functions constant along direction 1 (copies), to which (1) applies in direction 2,
and so on; after d steps every factor is ω(Π_sf_t^{[s]}) with exponent 1/|T_B|. Nonnegativity is preserved. ∎
- *Re-verification on our setting.* Blocks t := the level-k cubes of RLARGE (cells of the level-(k+1) sites; L⁴ level-k
  sites each), bounded by planes of P_{K-k-1}; 𝔅_t := functions of soft variables whose cells lie in t (in particular of the
  level-k links interior to t); the reflections in the planes between cubes preserve the class-[a] hierarchy at all
  resolutions ≥ K - k - 1 (computation: x ↦ 2c - x with c = a_μ + (j + ½)L^{-n} maps L^{-r}Z + a_μ to itself for r ≥ n), so
  no class change occurs; RP is X-RP^S at finite K; the torus has 4L^{M+K-k-1} cubes per direction (even). Translation
  invariance is not needed.

**Theorem CB (disseminated ⇒ local large-field bound). PROVEN-HERE | X-RP^S, Lemma CBE.** Fix k, call a level-k cube Q
*bad* if some plaquette with all four links interior to Q has ||1 - U_k(p)||_op ≥ ε_1 (RLARGE's ζ_Q = 1), and let
E_all := {every level-k cube is bad}. Then for every K, every torus and every level-k plaquette p,
  P_K(Q bad) ≤ P_K(E_all)^{1/N_k} for every cube Q, and P_K(||1 - U_k(p)||_op ≥ ε_1) ≤ P_K(E_all)^{1/N_k},
N_k := the number of level-k cubes.
*Proof.* If p is interior to a cube Q: Lemma CBE with f_Q := 1{Q bad}, f_t := 1 otherwise; f_Q^{[s]} = 1{s bad} because
reflections map interior plaquettes to interior plaquettes and ||1 - W||_op is invariant under W ↦ W^{-1} and conjugation.
Otherwise translate the cube grid by a level-k lattice vector b making p interior: the law of (U_0, …, U_k) is invariant
under τ_b (b preserves the fine lattice and all blocks at levels ≤ k; μ_K and the kernels are covariant), so the shifted
E_all has the same probability, and the shifted cube boundaries are planes of P_{K-k} on which X-RP^S holds. ∎
- The same proof works for the deterministic S4c variables with X-RP in place of X-RP^S: (LF-P) of H-loc-LF is implied by
  its disseminated form.

**The disseminated hypothesis.** (RLF-3^dis): there are a > 0, p_d ≥ 0 and C_d < ∞, independent of K, k, T and of the
coupling sequence (within (F), g_K ≤ g_RLF, RLF's threshold; renamed from "g_0" to avoid the clash with the bare
coupling [RX34-fix 5]), with P_K(E_all) ≤ (C_dg_k^{-p_d}e^{-a/g_k²})^{N_k} for every k.

**Corollary X-IVND^S (volume-uniform "not Haar" for the soft variables). PROVEN-HERE | (RLF-3^dis), (F)** [RX34-fix 4:
(F) is needed because (RLF-3^dis) is quantified within (F) and the bound needs g^S_m small]. For every m, every
coarse plaquette p and every limit point (finite or infinite volume), ν^S_{*,m}(||V_p - 1||_op > ε_1) ≤
C_d(g^S_m)^{-p_d}e^{-a/(g^S_m)²}; when this is below Haar{W : ||W - 1||_op > ε_1} the limit is not Haar, uniformly in the
volume. (Portmanteau for the open set, as in X-IVND'.) **[RX34-fix 4]** Stated separately: the soft limit is **not Haar,
given (RLF-3^dis) and (F)**; it is **not flat for every law of the fine field** (Proposition KB: kernel only, no
Yang-Mills content). The two are not to be paired as one non-triviality statement.

### 13.5 RLF against what the existence theorem needs (gaps D3, D4)

**What RLF (RLARGE §1, as written) is about.** (RLF-0)-(RLF-4) are statements about Z_K (which equals the Wilson
partition function: ∫K dV = 1), its factorisation into a c-number and Z_K^{ren}, and bounds on the terms of Z_K^{ren}
(counterterms, returned remainders, weights of unreturned histories). None of them is a statement about the law of a level
variable. A local probability bound cannot follow from extensive (partition-function) bounds alone in general (a mixture
of "all cubes small" and "all cubes large" has extensive bounds and local probabilities 1/2). **Theorem CB is the bridge:
under reflection positivity, an extensive bound on one disseminated event is a local bound.**

**(RLF-3^dis) from RLF-3 (ARGUED; reading not adopted by layer 1).** [RX34-fix 5] (RLF-3^dis) **would follow from layer
1's (OPEN) RLF-3, together with (RLF-1), (RLF-4) and node A's bulk bound, if RLF-3's weights are read as nonnegative
ratios Z_K[𝔥]/Z_K^{ref}, which RLF does not state.** It is not "an instance" of RLF-3 as written: §1A's (RLF-3) does not
say what its weights are normalised against, whether they are nonnegative, or whether the bound holds for the sum over
all finer- and coarser-level histories compatible with E_all. On E_all, the level-k R-step has
B = all cubes, one *-connected cluster with |B| = N_k > n_*, which RLF-3 keeps as an unreturned large-field region with
weight ≤ (Ce^{-a/g_k²})^{N_k}. P_K(E_all) = Z_K[E_all]/Z_K. If RLF-3's weights are nonnegative and are ratios to the
small-field partition function Z_K^{sf} (after the c-number of RLF-1), then
  P_K(E_all) ≤ (Ce^{-a/g_k²})^{N_k}·exp(C|T|e^{-(n_*+1)a/g_K²})·exp(C|T|e^{-a'/g_K²})·e^{O(N_k e^{-a/g_k²})},
using RLF-3's sum over the other histories, RLF-4 (Z^{sf} ≤ Z^{ren}e^{C|T|e^{-a'/g_K²}}) and the level-k c-numbers that
E_all does not produce; since |T| ≤ N_k, every extra factor is e^{O(N_k)} and (RLF-3^dis) follows with C_d = Ce^{O(1)},
p_d = 0. The two facts used (nonnegative weights; the normalisation by Z^{sf}) are not stated in RLF §1. **Proposed to
layer 1:** state RLF-3 as Z_K[𝔥]/Z_K ≤ Π_{Y∈𝔥}(Ce^{-a/g_k²})^{|Y|}e^{C|T|e^{-a'/g_K²}} for each history 𝔥; then (RLF-3^dis)
is a literal instance.

**Lemma MIX (D3 reduced; session 4's title "D3 is not needed" overclaimed [RX34-fix 8]). PROVEN-HERE.** If ρ = Σ_hw_hρ_h with w_h ≥ 0 and each ρ_h satisfies the pair inequality
ρ_h(T_sV)ρ_h(T_{-s}V) ≥ c(s)ρ_h(V)² on a set G, then so does ρ.
*Proof.* Cauchy-Schwarz: (Σ_hw_h√(ρ_h(T_sV)ρ_h(T_{-s}V)))² ≤ Σ_hw_hρ_h(T_sV)·Σ_hw_hρ_h(T_{-s}V), and the left side is
≥ c(s)(Σ_hw_hρ_h(V))². ∎ LAP-1 uses H-Bal-3L only through the pair inequality (its step (1)), so for the deterministic
branch a history-sum representation with per-history one-link bounds suffices; the exponentiated form of H-loc-LF is not
needed. For the soft branch D3 does not arise at all: no one-link density ratio of the full law is used (Proposition LAP^S
uses the kernel).
- **[RX34-fix 8] What MIX does and does not do.** For the deterministic branch, D3 is **reduced to: a nonnegative history
  representation ρ = Σw_hρ_h (w_h ≥ 0) with per-history pair inequalities on a common G_b (not supplied by RLF:** RLF's
  (I_k) bounds ℒ_𝔥 in modulus only and states no per-history one-link bound**)**; for the soft branch D3 does not arise.
  "D3 dissolved" is withdrawn; the reduction is ARGUED-reduced and not counted as closing anything.

**D4.** Closed by Theorem CB, modulo (RLF-3^dis), which would follow from the OPEN RLF-3 (+ RLF-1, RLF-4, node A) under
the nonnegative-ratio reading, which layer 1 has not adopted [RX34-fix 5]. The probability is now an output of
reflection positivity plus an extensive bound, not an input.

**What the merged existence theorem rests on (soft branch).**
| Conclusion | Rests on |
|---|---|
| (a), (b): limit states, consistency, symmetries, RP for every plane in P (continuum-support class), OS Hilbert space and H ≥ 0 on 𝒦^⊥, infinite-volume limit points | X-LRP (Osterwalder-Seiler), P's L9a′ contour covariance (for (C)), compactness |
| soft law has a bounded analytic density (finite volume), full support, not flat; ⟨1 - P⟩_m ≥ c g'_m² | the kernel (with the coupling sequence of (F)), P's D4-norm (2), g² ≤ κ, g'_m ≤ 1/2; **no information about the Wilson measure** |
| not Haar, uniformly in the volume | (RLF-3^dis) and (F) [RX34-fix 4]; (RLF-3^dis) would follow from the OPEN RLF-3 (+ RLF-1, RLF-4, node A) under an unadopted reading [RX34-fix 5] |
| ⟨1 - P⟩_m ≤ C g_m^S²(log 1/g_m^S)^{2p_*}, hence logarithmic approach to flat under (F) | (RLF-3^dis) + (PLD^mod_dis) (§13.6) + (F); D4-norm (2) (KN, KN-step); g ≤ g_T |
**[RX34-fix 4, 11] (F) for the soft scheme** is a property of the soft scheme's effective couplings (RLARGE §0, "OPEN as
A5"): *plausible extension of H-Bal-1 (different RG scheme; layer-1 node A5, OPEN)*, not something Balaban states. As an
inequality on a chosen sequence it is satisfiable by fiat; its content enters only through the other hypotheses holding
for that sequence. "Rests on RLF" means: rests on an OPEN layer-1 target.
So the informative non-triviality statement "not Haar, volume-uniformly" rests on (RLF-3^dis) and (F); "not flat" is a
kernel fact with no Yang-Mills content [RX34-fix 4]; the asymptotic-freedom upper bound needs, in addition, one
small-field statement of the type of RLF-step's own input (PLD)_k, at moderate thresholds. H-loc-LF, H-Bal-3(3a)-form
and H-Bal-3L/3G are not used by the soft branch.

### 13.6 T9: H-sg

**Lemma KN (kernel concentration, quadratic in the background defect). PROVEN-HERE | D4-norm (2).** Let M̄ = Σ_iw_iT_i
(probability weights), T_i = Se^{X_i} ∈ SU(N), X_i ∈ su(N), δ := max||X_i||_op ≤ 1/4, X̄ := Σw_iX_i, W' := Se^{X̄}, g² ≤ κ.
Then ||W'^{-1}M̄ - 1||_op ≤ 3δ², and for t ≥ 12√Nδ²,
  ∫_{||V - W'||_HS ≥ t} k(V, M̄) dV ≤ e c_N^{-1}(κ/g²)^{N²-1} e^{-κt²/(4Ng²)}.
*Proof.* R := W'^{-1}M̄ - 1 = Σw_i[(e^{-X̄} - 1)(e^{X_i} - 1)] + (e^{-X̄} - 1 + X̄) + Σw_i(e^{X_i} - 1 - X_i) (using ΣwX = X̄),
so ||R|| ≤ (e^δ - 1)² + δ²e^δ ≤ δ²(e^{2δ} + e^δ) ≤ 3δ². With Z := W'^{-1}V ∈ SU(N), x := ||V - W'||_HS = ||1 - Z||_HS:
Re tr((W'^{-1} - V^{-1})M̄) = Re tr((1 - Z^{-1})(1 + R)) ≥ ½x² - x√N||R||_op ≥ ½x² - 3√Nδ²x ≥ ¼x² for x ≥ 12√Nδ²
(Re tr(1 - Z^{-1}) = ½||1 - Z||²_HS; |tr(AB)| ≤ ||A||_HS||B||_HS). D4-norm (2) gives 𝒩(M̄) ≥ e^{-(κ/g²)(1 -
N^{-1}Re tr V_0^{-1}M̄)}e^{-1}c_N(g²/κ)^{N²-1} with V_0 the SU(N)-maximiser, and Re tr(V_0^{-1}M̄) ≥ Re tr(W'^{-1}M̄). So
k(V) ≤ e c_N^{-1}(κ/g²)^{N²-1}exp(-(κ/(Ng²))Re tr((W'^{-1} - V^{-1})M̄)) ≤ (same)·e^{-κx²/(4Ng²)}; Haar mass ≤ 1. ∎
(Check x3 C: ||R||/δ² ≤ 0.43 (SU(2)), 0.34 (SU(3)) on 2000 random instances each; the inequality holds in all.)
- *For layer 1.* This removes the linear δ_c loss of RLARGE Lemma RS (R4) (its §11 item 7): the kernel exponent is
  κt²/(4Ng²) once t ≥ 12√Nδ², δ ≤ (π/3)A_d(L)η by the ribbon bound (R1).
  **[RX34-fix 9] Qualification.** It does so **only together with KN-step's re-centred dichotomy**: (R4) bounds ||V_c - S_c||
  and KN bounds ||V - W'||; re-centring at W' re-introduces a linear term ||W'_c - S_c|| ≤ e^δ - 1 into the plaquette bound.
  The gain is in η_1: from min{ε_1/(2L²), ε_1²/(512NA_d)} (quadratic in ε_1) to c_1ε_1 with c_1 = 1/(2(L² + 5.5A_d))
  (linear), slightly worse than RLARGE §11 item 7's hoped-for O(ε_1/L²). The step δ ≤ (π/3)A_dη also needs A_dη ≤ 1.

**Corollary KN-step (one step does not reduce H-sg). PROVEN-HERE | Lemma KN, Lemma RS (R1)-(R2).** With c_1 :=
1/(2(L² + 5.5A_d(L))) (= 1/117 at d = 4, L = 3) and t small enough that t ≤ 1/(106√N A_d²c_1²) and (π/3)A_dc_1t ≤ 1/4:
  P(||1 - U_{k+1}(P)||_op ≥ t) ≤ P(η ≥ c_1t) + 4e c_N^{-1}(κ/g_k²)^{N²-1}e^{-κt²/(256Ng_k²)},
η := max of ||1 - U_k(p)||_op over the plaquettes of U_4(P). At t = g_{k+1}p(g_{k+1}), p(x) = (log 1/x)^{p_*}, p_* > 1/2, the
kernel term is ≤ g_{k+1}²/4 for g small.
*Proof.* ||1 - V_P|| ≤ ||1 - W'_P|| + Σ_{c∈∂P}||V_c - W'_c||, ||1 - W'_P|| ≤ ||1 - S_P|| + Σ_c||W'_c - S_c|| ≤ L²η + 4(e^δ - 1)
with δ ≤ (π/3)A_dη (ribbon bound; |θ| ≤ (π/3)||e^{iθ} - 1|| for ||·|| ≤ 1); so on {η < c_1t} the first part is < t/2, and
some ||V_c - W'_c||_op ≥ t/8 (op ≤ HS) has kernel probability bounded by Lemma KN with t/8 ≥ 12√Nδ². Conditional
independence of the four kernels and a union bound. ∎ So the kernel contributes nothing to the difficulty; the moderate
deviation of the coarse plaquette is that of the finer field at a smaller threshold, and iterating loses a factor c_1 per
level.

**Theorem CB-sg (H-sg from a disseminated small-field bound). PROVEN-HERE | X-RP^S, Lemma CBE, Theorem CB.** Group the
level-k cubes into super-blocks of 2⁴ cubes (side 2L level-k sites; their boundaries are planes of P, and the torus has an
even number of super-blocks per direction). For a level-k plaquette p, shift the super-block grid by a level-k lattice
vector so that p lies at distance ≥ 2 from the super-block boundary (possible for L ≥ 3), and let A_p be the family of the
reflected copies of p, one per super-block (their 1-neighbourhoods are pairwise disjoint). Then for every τ > 0,
  P_K(||1 - U_k(p)||_op ≥ τ) ≤ 16·P_K(E_all)^{1/N_k} + P_cut(||1 - U_k(p')||_op ≥ τ ∀p' ∈ A_p)^{1/|A_p|},
where P_cut is the true law of U_k conditioned on every (shifted) level-k cube being good; by translation invariance it
is the shift of the law conditioned on the standard cubes (the true conditional law; RLARGE's (PLD) concerns the
per-history all-cut measure of (I_k), and the passage is ARGUED: it needs nonnegative history weights, and p' ∈ A_p inside
the large-field regions of a history is not covered) [RX34-fix 6].
*Proof.* {||1 - U_p|| ≥ τ} ⊂ {some cube of p's super-block is bad} ∪ {f = 1}, f := 1{all cubes of the super-block good and
||1 - U_p|| ≥ τ}. The first event has probability ≤ 16 P(E_all)^{1/N_k} (Theorem CB). Lemma CBE with f at p's super-block
and 1 elsewhere bounds P(f = 1) by P(∩_s{f^{[s]} = 1})^{1/|A_p|} = [P(all cubes good)·P_cut(∀p' ∈ A_p: ||1 - U_{p'}|| ≥ τ)]^{1/|A_p|}.
Translation invariance under the shift as in Theorem CB. ∎

**The small-field hypothesis.** (PLD^mod_dis): there are a_m > 0, C_m < ∞ (independent of K, k, T) such that for every k,
every family A_p as above and every τ ∈ (0, ε_1], P_cut(||1 - U_k(p')||_op ≥ τ ∀p' ∈ A_p) ≤ (C_me^{-a_mτ²/g_k²})^{|A_p|}.
It is RLARGE's (PLD)_k (i) (all-cut measure, sets with disjoint 1-neighbourhoods, product bound) at **variable** threshold
τ (with Gaussian dependence τ²) instead of the fixed η_1, for the specific families A_p; that mixtures over histories preserve
it is ARGUED (it needs nonnegative history weights; see the P_cut remark [RX34-fix 6]). HYPOTHESIS (new; layer-1-native:
a strengthening of an input of RLF-step). Its Gaussian evidence: §13.6 below and §14.2 [RX34-fix 7].

**Corollary H-Bal-3T^S. PROVEN-HERE | (RLF-3^dis), (PLD^mod_dis) (and (F) for the final two-sided form).** With τ := g p(g)/√N, g := g^S_m = g_{K-m}: if g ≤ g_T
(g_T > 0 explicit from 16C_dg^{-p_d}e^{-a/g²} ≤ g²/2 and C_me^{-a_mp(g)²/N} ≤ g²/2, both true for small g when p_* > 1/2),
then ν^S_{K,m}(|V_p - 1|_HS ≥ g p(g)) ≤ g², uniformly in K and the volume (|·|_HS ≤ √N||·||_op). Hence the upper half of
X-NTAF holds for the soft variables: ω(1 - P^S_{p,m}) ≤ φ(g^S_m), and with Proposition LAP^S and (F) the soft block plaquette
is between c/(1/g² + β_+(m+1)log L) and C(log m)^{2p_*}/m. H-sg is no longer a separate hypothesis for the soft branch:
it is replaced by (PLD^mod_dis).

**The Gaussian instance and the Brascamp-Lieb route (where the wall now is).**
- *Gaussian case (PROVEN-HERE as an implication, not counted).* If the curvature vector (F_{p'})_{p'∈A} is centred Gaussian
  with covariance Σ (all N² - 1 components), ||Σ||_op ≤ σ²g², then E exp(λΣ_{p'}|F_{p'}|²) = det(1 - 2λΣ)^{-1/2} ≤ 2^{(N²-1)|A|/2}
  at λ = 1/(4σ²g²), and exponential Chebyshev on {Σ|F_{p'}|² ≥ |A|τ²} gives P(|F_{p'}| ≥ τ ∀p') ≤ (2^{(N²-1)/2}e^{-τ²/(4σ²g²)})^{|A|}.
  For the noncompact abelian model with deterministic averaging, ||Σ||_op ≤ g_0² at every depth by A1 (layer 1's Prop. 7.1
  = A2 is this statement). For the linear soft chain the crude recursion ||Σ_{k+1}|| ≤ ||Σ_k|| + 24g_k²/κ (A1 is only
  marginal in d = 4, L^{4-d} = 1) gives a log-divergent bound; the uniform bound needs the symbol-level fact that the
  injected noise has no curvature at p → 0, which is not written here.
  **[RX34-fix 7] The A2 instance is for deterministic averaging only.** At the end of session 4 no instance of
  (PLD^mod_dis) was established for the soft chain, even in the free Gaussian case, and the log-divergent crude bound was a
  falsification risk (soft block plaquettes drifting toward Haar). Session 5 settles the free case: §14.2.
- *Log-concavity route.* (PLD^mod_dis) would follow from the Gaussian case by the Caffarelli contraction / Hargé
  correlation inequality (convex functions of a log-concave perturbation of a Gaussian are dominated by their Gaussian
  value) [STANDARD, not-read here], if the all-cut level-k measure were, in a global chart, e^{-V}·γ_Σ with V convex and
  ||Σ|| ≤ σ²g_k². **Because only an extensive (disseminated) statement is now needed, the localisation problem of §11.4 (a
  Gaussian domination for one plaquette conditioned on a regular exterior) is gone.** What remains is the wall:
  **(W-lc) the all-cut measure of compact SU(N) lattice fields is not a log-concave perturbation of a Gaussian in any global
  chart:** (i) SU(N)^{links} has no global linear chart, and on the torus the holonomies around non-contractible loops
  are unconstrained; (ii) the all-cut condition constrains only cube-interior plaquettes, so the domain (crossing
  plaquettes free) is not convex in any gauge; (iii) the free Hessian (1/g²)d*d on a gauge slice has no uniform gap
  (massless), so the non-abelian Hessian corrections, of relative size O(ε_1), are not dominated globally. The
  conditional law of a finer level given the coarser one does have a uniform linear gap (LINEAR_PACKAGE Prop. 6.4,
  E_i + (κ_i/2)||QA||² ≥ min(c_E, κ_i/2)c_1||A||² on Phys), but that conditions in the wrong direction for a bound on the
  marginal law; using it requires the multiscale (RG) organisation, i.e. layer 1's small-field package (SF)_k with (DF3')
  for linear functionals (the route by which RLARGE derives (PLD)), now at variable thresholds.
- **H-sg outcome: REDUCED, not proven.** The local, sourceless H-sg is replaced by the disseminated (PLD^mod_dis), a
  variable-threshold form of a layer-1 input; the Gaussian (noncompact, **deterministic averaging**) instance holds by
  layer 1's A2, which is not the soft chain this branch uses [RX34-fix 7] (soft free instance: §14.2); the interacting
  compact case stops at (W-lc).

### 13.7 Check x3
Criteria checks/x3_criteria.md written before checks/x3_soft_rp.py; record checks/x3_time.txt; output checks/x3_out.txt.
A (block-boundary RP of a soft-blocked Z_q clock ring, q = 3, 5, nine (β, κ) pairs): min/max eigenvalue ≥ -9·10⁻¹⁶,
θ-symmetry to 7·10⁻¹⁸: PASS. B1 (site plane, normalised kernel): min/max eigenvalue -0.195: site-plane RP fails (as
pre-stated, this licenses "fails for the normalised kernel in that toy"). B2 (site plane, unnormalised): PSD. C (Lemma KN
core, SU(2) and SU(3), 2000 instances each): PASS; max ||R||/δ² = 0.43, 0.34 (≥ 0.1: discriminating for the constant).
3.5 s, 93 MB, one process, nice 10, threads 1, load 3.0, memory free 33%; `python3` without -I (user-site numpy; no
external files read). A tests the mechanism of X-RP^S on a spin toy, not gauge structure.
[RX34-fix, record] A is a one-level toy and cannot probe the X-RP^S ancestor gap (two levels or shifted classes needed). C
tested ||R|| ≤ 3δ² with δ the sampling bound, not δ := max||X_i||_op; since max||X_i|| ≤ δ this is weaker than the
lemma; the discrimination claim stands (against the true δ the ratio is larger). A re-run should compute δ as
max||X_i||_op. (Not re-run here; the review re-ran x3 byte-identically.)

### 13.8 Outcome against the pre-stated targets
- **T8a: MET.** Soft layer (a), (b), (d)-soft: all transfer, no hypothesis (X-RP^S and the transfer list, §13.2); the
  Option S OPEN item is closed. X-ND, X-MONTEL, LAP-1 and the X-NTAF lower half hold for soft variables from the kernel
  alone (Propositions KB, LAP^S) but lose their content as statements about the Wilson measure. X-CAUCHY and X-NT2 are not
  transferred (they need the polymer structure of the effective action). X-IVND^S (not Haar) | (RLF-3^dis), (F)
  [RX34-fix 4]. **[RX34-fix 2] Lost for soft variables:** H-cont and H-bl in L²(ω) form (false: independent kernel noise
  on shifted grids), so X-KER (ii)-(iii) cannot be used for soft generators; replacement in §14.3.
- **T8b: MET.** RP holds for every block-boundary plane in P (proof); it fails for site planes with the normalised kernel
  (check x3 B1), because of 𝒩; X-OS needs only the former.
- **T8c: PARTLY MET.** D3 reduced to a nonnegative history mixture with per-history pair inequalities (not supplied by
  RLF) [RX34-fix 8]; for soft variables D3 does not arise. D4 closed by Theorem CB (reflection
  positivity turns an extensive bound into a local one) modulo (RLF-3^dis), which would follow from the OPEN RLF-3
  (+ RLF-1, RLF-4, node A) under a nonnegative-ratio reading that layer 1 has not adopted [RX34-fix 5] (ARGUED; proposed
  restatement given). "Not Haar" rests on (RLF-3^dis) + (F); "not flat" is kernel-only [RX34-fix 4]. The upper (AF) bound needs (PLD^mod_dis) as well: **the theorem
  does not rest on RLF + (F) only**; the extra statement is named and is of layer-1 type.
- **T9: REDUCED.** H-sg ⇐ (RLF-3^dis) + (PLD^mod_dis) via chessboard (Theorem CB-sg). Lemma KN (unconditional) shows the
  kernel adds nothing to the difficulty. Wall: (W-lc).

### 13.9 End-of-session re-read of RLARGE §1 (layer 1 session 18 changed it during this session)
RLARGE.md changed during this session (md5 cb4a8c9c… at the start, d41ec7fb… at 18:16 local); §1 is kept verbatim and an
amended statement **§1A** was added [R1617-fix]. Changes that matter here, and their effect:
- **Name collision.** Layer 1 now uses **(RLF-5)** for "complex fields". This file never uses that label; the hypothesis
  used here is (RLF-3^dis).
- **(RLF-3) amended (two thresholds, fix R-1).** Unreturned = defect configurations 𝒟 (bad or collar-bad cubes,
  *-connected) with n(𝒟) > n_♯, weights ≤ Π(Ce^{-a_♯/g_k²})^{n(𝒟)}, exponent a = a_♯. E_all (every cube bad) is one
  defect configuration with n = N_k > n_♯, so it is still unreturned and the §13.5 reading applies with a := a_♯.
- **Z_K^{ref} defined (fix R-2).** Z_K^{ref} := exp(𝒱_K^{LF})·Z_K^{sf,ref} with exp(-E'_-|T|) ≤ Z_K/Z_K^{ref} ≤ exp(E'_+|T|)
  (given (RLF-1), (RLF-4) and node A). This removes half of the normalisation gap of §13.5: **if RLF-3's weights are
  nonnegative ratios Z_K[𝔥]/Z_K^{ref}**, then P_K(E_all) ≤ (Ce^{-a_♯/g_k²})^{N_k}·exp(C|T|e^{-(n_♯+1)a_♯/g_K²})·e^{E'_-|T|},
  and since |T| ≤ N_k this is (RLF-3^dis) with C_d = Ce^{E'_- + 1}, p_d = 0. What §1A still does not state is that the
  weights are such ratios (and nonnegative). The proposed restatement of §13.5 stands, now with Z_K^{ref} in place of
  Z^{sf}. Note that this route uses (RLF-4) and node A's bulk bound only through Z_K/Z_K^{ref} ≥ e^{-E'_-|T|}.
- **(RLF-4)** now needs (SF-last); (RLF-0)/(RLF-1) re-indexed by connected supports and finite-volume qualified. Neither
  affects §13.
- LINEAR_PACKAGE.md was frozen as v1 during the session (18:09 local); Proposition 6.4 and Proposition 7.1 (A2), the only
  items cited in §13.6, read the same as before.

---

## 14. Session 5 (2026-10-27): the decisive test of the soft variables, and time continuity for them

### 14.0 Pre-stated targets (2026-10-27 22:54 UTC; written before any derivation below, after applying the REVIEW_X3_X4 fixes and reading P/LINEAR_PACKAGE.md §1.1-§2 (frozen v1, md5 4fbf5342…))

**T11 (the decisive test).** Setting: the free Gaussian soft chain, i.e. layer 1's Setting SC (LINEAR_PACKAGE §1.3) as
a measure: one real component of the noncompact abelian field; B_0 Gaussian with action (1/(2g_0²))||dB_0||²; and, for
each level i, B_{i+1} = Q_rootB_i + ξ_i with ξ_i independent centred white noise of variance σ_i² := g_i²/κ_i per link
(the quadratic part of the decision-4 kernel exp(-(κ_i/g_i²)[1 - N^{-1}Re tr(V^{-1}M̄)])/𝒩, whose normalisation cancels
the shrinkage of M̄, so the conditional law of B_{i+1} given B_i is exactly N(Q_rootB_i, σ_i²)). At fixed physical
resolution m (level j = K - m), compute exactly, as K → ∞:
- (Q1) the variance of one block plaquette (dB_j)(P), split into the fine-field part and the accumulated kernel noise;
- (Q2) the variance of a block link in the straight and in the root (S4') representative (gauge-variant; reported only
  to locate any divergence);
- (Q3) the operator norm ||Σ_j||_op of the covariance of the block-curvature vector (what §13.6's Gaussian argument for
  (PLD^mod_dis) needs);
- (Q4) the variance of the flux through a block Wilson loop of fixed physical size.
**PASS** means: (Q1), (Q3), (Q4) are bounded uniformly in K (and the torus) and converge as K → ∞, with
||Σ_j||_op ≤ C g_j² under (F) (C independent of K, m, T). Then the soft variables are viable at the free level and the
free Gaussian instance of (PLD^mod_dis) holds for the soft chain.
**FAIL** means: (Q1) or (Q3) grows without bound in K at fixed m (any rate: log K, a power of K, …). Then state which
existence statements fail for soft variables ((RLF-3^dis), (PLD^mod_dis), Corollaries X-IVND^S, H-Bal-3T^S, the AF upper
bound) and test the repairs: noise width shrinking with depth (κ_k growing), or the hybrid (soft chain for the RG
analysis, deterministic block variables for observables), proving the repair if possible.
**INTERMEDIATE** means: (Q1) bounded but (Q3) unbounded (a low-momentum divergence): local soft laws viable, the Gaussian
route to (PLD^mod_dis) not.
Conservative rules: only gauge-invariant quantities (Q1, Q3, Q4) decide; (Q2) is diagnostic. The free test says nothing
about compact non-abelian corrections, which stay ARGUED at most.

**T12 (only if T11 passes or is repaired).** A route to ker T = 0 for soft variables that does not use the L² forms of
H-cont / H-bl (false for soft variables, [RX34-fix 2]): through the OS seminorm, via F̃ = E[F | fine field]. **Success:**
a proven implication "hypothesis ⇒ 𝒦 = {0}" for the soft OS space, with the hypothesis stated with every quantifier, and
its free Gaussian instance proven (or refuted). **Not success:** a hypothesis that is false for soft variables for the
same reason as H-cont (independent noise on two branches).

**T13.** Tally, LOG session 5, snapshot; §12.1 changed only if the results require it.

**Check plan (x4).** checks/x4_criteria.md written before checks/x4_soft_noise.py: (A) the one-step identity
dQ_root = dQ_str on random fields in d = 4 (24 orders); (B) the block-plaquette noise variance after n blocking steps,
computed in position space (iterated adjoint, n = 1, 2) and by exact finite Fourier alias sums (n ≤ 8), against any
closed form derived in §14.2; (C) the sup over momenta of the curvature-covariance symbol after n steps against the
proven bound; (D) the chain sum at fixed m for K up to m + 60 under an (F)-type sequence: converges or grows.

# Session 5 derivations (written after §14.0)

### 14.1 The free Gaussian soft chain (the model; exact)
- **Model.** Levels i = 0 (fine) … K; one real component; noncompact abelian. B_0 is the Gaussian field with action
  (1/(2g_0²))||dB_0||² (only gauge-invariant functionals are used, so no gauge fixing is needed); given B_0, …, B_i,
  **B_{i+1} = Q_rootB_i + ξ_i**, ξ_i independent centred white noise on the level-(i+1) links with variance
  σ_i² := g_i²/κ_i. This is the measure whose exponent is Setting SC's chain energy with level couplings,
  (1/(2g_0²))||dB_0||² + Σ_i(κ_i/(2g_i²))||Q_rootB_i - B_{i+1}||² (LINEAR_PACKAGE §1.3): the Gaussian kernel's normaliser
  does not depend on B_i, so the chain is Markov with exactly these conditionals (this is the linear content of
  "𝒩 cancels the shrinkage of M̄"). Level j = K - m is resolution m; s := L^n.
- **Two facts imported from layer 1 (both PROVEN there, frozen v1, re-checked here by x4 A and Lemma 2.4's proof).**
  (R) Q_root = Q_str - d∘h (LINEAR_PACKAGE §1.2) and root covariance Q_root∘d = d∘ev. (IT) the composite of n one-step
  straight averages is the straight average of side L^n (Lemma 2.4); re-derived: at two steps, y + je_μ = L²Z +
  (L(X - LZ) + u) + (Lj' + j)e_μ, and (X - LZ, u) ↦ L(X - LZ) + u, (j', j) ↦ Lj' + j are bijections onto the side-L² box
  and [0, L²).

**Lemma GS-1 (the gauge-invariant content of the soft chain is that of the straight chain). PROVEN-HERE | (R).** For
every n, Q_root^n - Q_str^n = d∘λ_n with λ_n linear, λ_0 = 0, λ_{n+1} = ev∘λ_n - h∘Q_str^n. Hence every block curvature
dB_j and every closed-loop flux of the soft chain equals, as a random variable (same B_0, same ξ), that of the straight
chain B^str_{i+1} = Q_strB^str_i + ξ_i, B^str_0 = B_0:
  dB_j = dQ_str^jB_0 + Σ_{i<j} dQ_str^{j-1-i}ξ_i.
*Proof.* Q_root(Q_str^nξ + dλ_n) = Q_str^{n+1}ξ - dhQ_str^nξ + d ev λ_n by (R). Sum over the injection levels. ∎

**Lemma GS-2 (n-step damping of injected noise; exact). PROVEN-HERE | (IT).** Let ξ be white noise of variance σ² on
the links of some level and b := Q_str^nξ (n further levels up), s = L^n. Then:
(a) b_μ(X) = s^{-4}Σ_z m_s(z_μ - sX_μ)1[z_⊥ ∈ (sX + box_s)_⊥]ξ_μ(z), m_s(t) := min(t + 1, 2s - 1 - t) on 0 ≤ t ≤ 2s - 2;
(b) Var b_μ(X) = (σ²/3)(2s^{-2} + s^{-4});
(c) components are independent, and b_μ(X), b_μ(X') are independent unless X' - X = ±e_μ or 0;
(d) for every block plaquette P, **Var(db)(P) = (4σ²/3)(2s^{-2} + s^{-4})**;
(e) the covariance of b has symbol Ĉ_μμ(P) = σ²s^{-2}Σ_{a<s}|D_s((P_μ + 2πa)/s)|⁴ ≤ σ²s^{-2} (D_s as in LINEAR_PACKAGE
§1.5), so its operator norm is ≤ σ²s^{-2}; the covariance of db has operator norm ≤ 16σ²s^{-2}.
*Proof.* (a) is (IT): the coefficient of ξ_μ(z) is s^{-4} times the number of (y, j) with y ∈ sX + box_s, j < s,
y + je_μ = z, which is m_s in the μ-coordinate and 1 or 0 transversally. (b) Σ_t m_s(t)² = Σ_{u≤s}u² + Σ_{u<s}u² =
(2s³ + s)/3, times s³ transverse positions and s^{-8}. (c) Different components use different noise; the transverse
supports of b_μ(X) and b_μ(X + e_ν), ν ≠ μ, are disjoint blocks. (d) db(P) = [b_μ(X) - b_μ(X + e_ν)] + [b_ν(X + e_μ) -
b_ν(X)]: four independent terms by (c), each with variance (b). (e) Decimation of the filter ĥ_μ(q) = sD_s(q_μ)²
Π_{α≠μ}D_s(q_α) gives Ĉ_μμ(P) = σ²s^{-4}Σ_{aliases}|ĥ_μ|² = σ²s^{-2}Σ_a|D_s|⁴·Π_{α≠μ}Σ_a|D_s|², and Σ_{a<s}|D_s((θ +
2πa)/s)|² = 1 exactly (Parseval for the box filter) while |D_s| ≤ 1. Curvature: ||dĈd^*|| ≤ sup_Pψ(P)·sup Ĉ ≤ 16σ²s^{-2}
(ψ ≤ 16 is the top of the 4D lattice Laplacian). ∎ (Check x4: B confirms (b), (d) to ≤ 1e-12 by two independent
routes; C finds s²·sup Ĉ = 1 and s²·sup of the curvature eigenvalue = 12 for n ≥ 1, below 16.)

**Theorem GS (the accumulated kernel noise converges). PROVEN-HERE | Lemmas GS-1, GS-2, X-CONT-G (iii).** In the free
Gaussian soft chain, for every K, every level j = K - m ≥ 1, every torus and every block plaquette P:
(i) Var(dB_j(P)) = g_0²w_j(P) + N_j, with 0 ≤ w_j(P) ≤ 1 and
  **N_j = (4/3)Σ_{n=0}^{j-1} σ²_{j-1-n}(2L^{-2n} + L^{-4n})**,  4σ²_{j-1} ≤ N_j ≤ (4/3)σ̄²(2L²/(L² - 1) + L⁴/(L⁴ - 1))
  (σ̄² := max_{i<j}σ_i²; the constant is 4.35 at L = 3);
(ii) the block-curvature covariance Σ_j satisfies ||Σ_j||_op ≤ g_0² + 16Σ_{n=0}^{j-1}σ²_{j-1-n}L^{-2n} ≤ g_0² +
  16σ̄²L²/(L² - 1);
(iii) the flux through a closed coarse loop C (perimeter |C|, spanning coarse surface Σ) has noise variance
  ≤ |C|Σ_nσ²_{j-1-n}L^{-2n} and fine-field variance ≤ g_0²|Σ|²;
(iv) (gauge-variant, diagnostic) the noise part of a block link has variance (1/3)Σ_nσ²_{j-1-n}(2L^{-2n} + L^{-4n}) in the
  straight representative (convergent), but ≥ 0.0042·Σ_{n=2}^{j-1}σ²_{j-1-n} in the root (S4') representative, which
  diverges like Σ_iσ_i² (pure gauge: dλ_n).
**Convergence at fixed physical resolution.** If the kernel couplings are indexed by resolution (σ²_{K-r} =: σ̂²(r), as
for any sequence satisfying (F)), then N_{K}(m) = (4/3)Σ_{n=0}^{K-m-1}σ̂²(m + 1 + n)(2L^{-2n} + L^{-4n}) is nondecreasing in
K and converges, with 0 ≤ N_∞(m) - N_K(m) ≤ 4σ̄²L^{-2(K-m)}/(1 - L^{-2}): **geometric convergence in K - m, no log K.**
*Proof.* (i) By GS-1, dB_j = dQ_str^jB_0 + Σ_i dQ_str^{j-1-i}ξ_i, independent summands. The first is X-CONT-G's
composite flux ⟨ψ_P, F⟩ with β = g_0^{-2}: variance g_0²||Π_exψ_P||² ≤ g_0² (X-CONT-G (iii)). The others are GS-2 (d).
Bounds: the n = 0 term is 4σ²_{j-1}; geometric sums. (ii) Independent summands; A1 (LINEAR_PACKAGE Lemma 2.2: the
curvature map of Q is a contraction in d = 4) bounds the first by ||Cov dB_0|| = g_0²; GS-2 (e) the others. (iii) GS-2 (e)
for the noise; Minkowski over the plaquettes of Σ and ||ψ_P|| ≤ 1 for the fine field. (iv) Straight: GS-2 (b). Root: the
noise from level i contributes Q_str^nξ_i + dλ_n, λ_n = -Σ_{l<n}ev^{n-1-l}h(Q_str^lξ_i). The l = 0 piece of dλ_n is the
difference of h(ξ_i) at two distinct sites, whose blocks are disjoint: variance 2||c||²σ_i², ||c||² = 0.142661 (exact,
x4 A2; c the coefficient vector of h). The l ≥ 1 pieces have standard deviation ≤ 2√(||c||²)σ_iL^{-l} (GS-2 (e)), the
straight part ≤ σ_iL^{-n} ≤ σ_i/9 for n ≥ 2. Minkowski: sd ≥ σ_i(0.5342 - 0.3777 - 0.1111) = 0.0654σ_i, squared 0.0042σ_i²;
contributions of different i are independent. Convergence: monotone partial sums of a series dominated by
(4/3)σ̄²Σ_n3L^{-2n}. ∎
- **Why session 4's recursion diverged.** ||Σ_{k+1}|| ≤ ||Σ_k|| + 24g_k²/κ treats the fresh noise's curvature as if it
  were smooth; A1's contraction constant 1 is attained only on smooth (low-momentum) curvature. White noise is rough: n
  further averaging steps damp its block curvature by L^{-2n} (GS-2 (d), (e)). In symbol language: in coarse units the
  injected noise at coarse momentum P sits at fine momentum P/s, where its curvature symbol is O(|P/s|²) (the
  reviewer's "curvature symbol O(p²)" is exactly this).

**Corollary PLD-G^S (the free Gaussian instance of (PLD^mod_dis) for the soft chain). PROVEN-HERE | Theorem GS, (F).**
Let the coupling sequence satisfy the two-sided form of (F) (1/g² + β_-(K - i)log L ≤ 1/g_i² ≤ 1/g² + β_+(K - i)log L for
0 ≤ i ≤ K, 0 < β_- ≤ β_+), κ_i ≥ κ_- and β̂ := β_+/β_-. Then for every K, m, torus and j = K - m:
  ||Σ_j||_op ≤ σ_*²g_j², σ_*² := β̂(1 + 16L²/((L² - 1)κ_-)),
and, by the Gaussian argument of §13.6 (all N² - 1 linearised components independent copies), for every family A of
block plaquettes at level j and every τ > 0, P(|F_{p'}| ≥ τ ∀p' ∈ A) ≤ (2^{(N²-1)/2}e^{-τ²/(4σ_*²g_j²)})^{|A|}: the form
of (PLD^mod_dis) with a_m = 1/(4σ_*²), C_m = 2^{(N²-1)/2}, for the **unconditioned** free law (the noncompact free model
has no all-cut conditioning; no claim is made for a conditioned law).
*Proof.* For i ≤ j: 1/g_i² ≥ 1/g² + β_-(K - j)log L ≥ (β_-/β_+)(1/g² + β_+(K - j)log L) ≥ (β_-/β_+)/g_j², so g_i² ≤ β̂g_j²
(including i = 0, the fine field). Theorem GS (ii). ∎
- With constant couplings (the natural free scheme: g_i ≡ g_0 = g, β = 0) the same holds with β̂ = 1.

**Verdict on T11: PASS.** The accumulated kernel noise at fixed physical resolution **converges** as K → ∞, for block
plaquettes (Q1), the curvature covariance in operator norm (Q3) and loop fluxes (Q4), uniformly in the torus, at a
geometric rate L^{-2(K-m)}; it is dominated by the last few kernels: N_∞(m) ≈ (4/3)(g'_m²/κ)(2L²/(L² - 1) + L⁴/(L⁴ - 1))
up to the slow variation of the couplings. The only divergent quantity is the gauge-variant root-representative link
variance (Q2), which is pure gauge (dλ_n) and invisible to every generator of the soft algebra (coarse-gauge-invariant
functions). No log K and no power of K appears in any gauge-invariant quantity. Check x4 D: N_K(m) is constant to
< 1e-12 from K - m = 30 to 60 for both a constant and an (F)-type sequence, while session 4's crude bound grows from 16
to 960 (constant) and from 15 to 434 (F-type) over the same range.

**Consequences (exact scope).**
- **No existence statement fails at the free level.** The falsification mechanism named in REVIEW_X3_X4 (soft block
  plaquettes drifting toward Haar through log-accumulated noise) does not occur in the free Gaussian soft chain. Decision
  4's soft variables survive this test at the existence level. No repair (κ_k growing with depth, or the hybrid scheme)
  is needed for it; both stay available but unused.
- **(PLD^mod_dis)** now has a free Gaussian instance for the soft chain itself (Corollary PLD-G^S), replacing the
  wrong-branch evidence that session 4 cited ([RX34-fix 7]). (RLF-3^dis) is a large-field statement and is not tested by
  a noncompact free model.
- **A reading the free model forces.** Under an (F)-type sequence the fine-field part g_0²w_j → 0 as K → ∞ (g_0 is the
  finest coupling), so in the free model the limiting soft block law at fixed m is pure kernel noise of size g'_m²/κ.
  This is the free model's lack of running, not a defect of the scheme (with constant couplings both parts are O(g²) and
  converge), but it confirms §13.3: the size of soft fluctuations alone carries no information about the fine measure;
  the informative statements are the concentration bounds.
- **Not shown (ARGUED, uncounted).** In the compact non-abelian chain, the nonlinear corrections to the injected noise
  (commutator terms of the contour products, the polar-part correction of M̄) are further mean-zero, local injected
  noises of relative size O(g²) per level; any local mean-zero injected noise is damped by n averaging steps exactly as
  in GS-2 (the proof of (e) uses only finite range and the box filter), so the same convergence is expected; a mean
  (bias) term would not be damped, and its absence (by charge-conjugation/reflection symmetry of the kernel) is not
  proven here. The gauge-variant drift of (iv) has a compact analogue (random gauge frames at the roots) that is exactly
  invisible to gauge-invariant generators by the kernel's root covariance.

### 14.3 T12: time continuity for soft variables through the OS seminorm

Setting: X-OS^S (§13.2) with the continuum-support class [RX34-fix 1]: Π_0 a time plane of P, 𝔄^S_+ the C*-algebra
generated by soft generators (coarse-gauge-invariant continuous functions of finitely many soft variables, any
resolutions and classes, continuum supports in {x_0 > Π_0}), T(s)[F] := [τ_sF], s ∈ 2D_+, ω a limit point along
(K_j). For a bounded measurable F of finitely many soft variables let **F̃_K := E_{P_K}[F | U_0]**.

**Theorem X-KER^S (the OS form sees only F̃; a time-continuity criterion that survives kernel noise). PROVEN-HERE |
X-RP^S, X-OS^S, X-LRP.**
(i) For F, G in the *-algebra generated by soft generators of 𝔄^S_+ and every K above their levels,
E_{P_K}[θ(F)^*G] = E_{μ_K}[θ(F̃_K)^*G̃_K].
(ii) ||[F]||²_OS ≤ liminf_j E_{μ_{K_j}}|F̃_{K_j}|² ≤ ||F||²_∞.
(iii) Suppose **H-cont^S**: there is a set 𝒟 of such F whose linear span is uniformly dense in 𝔄^S_+ such that for every
F ∈ 𝒟,
  lim_{s→0, s∈2D_+} limsup_{K→∞} E_{μ_K}|E_{P_K}[τ_sF - F | U_0]|² = 0.
Then lim_{s→0}ω(θ(F)^*τ_sF) = ω(θ(F)^*F) for every F ∈ 𝔄^S_+, and hence (X-OS (iv)) **𝒦 = {0}**: the Hamiltonian acts
on all of the soft OS space.
*Proof.* (i) Let A_+ be the variables of F and G with all their ancestors; it is closed under ancestry and its variables
have continuum supports in the open positive half-space (proof of X-RP^S). Given U_0, the joint law of A_+ is
Π_{v∈A_+}k_v (integrate out the other variables coarsest first, ∫k = 1), so ∫Π_{A_+}k_v dv F = E[F | U_0] = F̃_K, and the
X-RP^S computation (with G in place of the second F) gives E_{μ_K}[θ(F̃_K)^*G̃_K]. (ii) θ(F)^*F is in the algebra, so
ω(θ(F)^*F) = lim_j E_{P_{K_j}}[θ(F)^*F] = lim_j E_μ[θ(F̃)^*F̃] ≤ liminf_j ||θ(F̃)||_{L²(μ)}||F̃||_{L²(μ)} =
liminf_j||F̃||²_{L²(μ)} (θ preserves μ_K, X-LRP's setting); Jensen gives ≤ ||F||²_∞. (iii) For F ∈ 𝒟, τ_sF - F is in the
algebra (X-OS^S: τ_s, s > 0, preserves 𝔄^S_+), so by (ii) ||[τ_sF] - [F]||_OS → 0, and |⟨F, T(s)F⟩ - ⟨F, F⟩| ≤
||[F]||_OS||[τ_sF] - [F]||_OS → 0. Linear combinations: triangle inequality. General F: ||[F] - [F_ε]||_OS ≤ ||F - F_ε||_∞
and ||T(s)|| ≤ 1. X-OS (iv). ∎
- **Why this is not false for the reason H-cont is.** The conditional expectation given the fine field integrates out
  the kernel noise on both branches; what remains is a function of the fine field alone, translated. The obstruction of
  [RX34-fix 2] (2E[Var(F | parents)]) is exactly the part removed. The doubled-chain form, E_μ|E[G | U_0]|² = E[G^*G']
  with G' a conditionally independent copy of G given U_0, shows that H-cont^S is a statement about the joint law of two
  soft chains driven by one fine field, tested on functions with one variable from each chain.

**Corollary X-CONT-G^S (H-cont^S in the free Gaussian soft chain). PROVEN-HERE | Theorem GS's setting, X-CONT-G.** In
the free Gaussian soft chain (any g_0, any noise variances σ_i), let f be Lipschitz (constant Λ, Euclidean metric) in the
block curvatures of a finite set X of resolution-m plaquettes, ℓ the block side in fine units and t e_a a fine shift
(0 ≤ t ≤ ℓ, w := t/ℓ = L^m|a|). Then, uniformly in K, the torus and the kernel couplings,
  E|E[f(F^S_{t}|_X) - f(F^S_0|_X) | B_0]|² ≤ Λ²|X|(4g_0²)w.
*Proof.* By GS-1, F^S_t|_X = D_t(B_0) + η_t with D_t the deterministic composite curvatures of X-CONT-G on the
t-shifted grid and η_t the accumulated noise curvature, independent of B_0, centred Gaussian, with a law independent of
t (the shifted class tree is the translate of the unshifted one, and white noise is translation invariant). So
E[f(F^S_t|_X) | B_0] = f_η(D_t(B_0)), f_η(x) := E f(x + η_0), which is Λ-Lipschitz. Hence the left side is
≤ Λ²Σ_{P∈X}E|D_t(P) - D_0(P)|² ≤ Λ²|X|(4/β)w with β = g_0^{-2} (X-CONT-G (ii)). ∎
- Several resolutions: the same proof with w the largest relative shift. The noise does not enter the bound at all.
  RP and the OS structure of the noncompact free model are not re-derived here; only the estimate is claimed.
- **Interacting case: H-cont^S is OPEN.** F̃ = (K_0 ⋯ K_{j-1}f)(U_0) is a kernel-smoothed function of the fine field; it
  is not a function of the deterministic block variables, so H-cont^S is not implied by the deterministic H-cont. The
  natural route is the one of §10.2 (H-corr + H-lin, ARGUED there for the deterministic branch) applied to the doubled
  chain; not attempted. The OPEN entry "H-cont" now carries two forms: L² two-grid (deterministic branch) and H-cont^S
  (soft branch).

### 14.4 Check x4
Criteria checks/x4_criteria.md written before checks/x4_soft_noise.py; record checks/x4_time.txt; output
checks/x4_out.txt. A (one-step identity with literal S4' contours, 24 orders, 81 offsets, fine torus 9⁴, three random
fields): max|Q_root - (Q_str - dh)| = 1.6e-14, max|dQ_root - dQ_str| = 2.6e-14: PASS; A2 ||c||² = 0.142661. B (plaquette and
link noise variances against GS-2 (b), (d)): position space by iterated adjoints (n = 1, 2), relative error ≤ 2.2e-16;
exact finite Fourier alias sums (n = 1..8), ≤ 1.1e-12: PASS. C (symbol bounds, 16⁴ momenta, n = 0..6): s²·sup Ĉ = 1,
s²·sup curvature eigenvalue = 16 (n = 0), 12 (n ≥ 1): PASS. D (chain sums, m ∈ {0, 2, 5}, K - m up to 60, constant and
(F)-type couplings): N_60 - N_30 = 0 to machine precision, the independent per-depth route agrees with the closed form to
≤ 2.7e-15: CONVERGES; crude bound 16 → 960 (constant), 15 → 434 (F-type). 12.3 s wall, 230 MB peak, one process, nice 10,
threads 1, load 2.0, memory free 42%, numeric lock held; `python3` without -I (user-site numpy; no external files read).
The script tests the abelian linear model only.

### 14.5 Outcome against the pre-stated targets
- **T11: PASS** (Theorem GS, Corollary PLD-G^S; x4 PASS/CONVERGES). Exact rate: the noise injected n levels below
  resolution m contributes (4σ²/3)(2L^{-2n} + L^{-4n}) to the block-plaquette variance; the K-dependence at fixed m is
  a tail ≤ 4σ̄²L^{-2(K-m)}/(1 - L^{-2}). The free Gaussian instance of (PLD^mod_dis) holds for the soft chain
  (unconditioned law). Not tested: compact non-abelian corrections (ARGUED), (RLF-3^dis) (large-field).
- **T12: MET in the pre-stated sense.** Proven implication H-cont^S ⇒ 𝒦 = {0} for the soft OS space (Theorem X-KER^S),
  with a hypothesis that is not false for the kernel-noise reason and holds in the free Gaussian soft chain (Corollary
  X-CONT-G^S). In the interacting case H-cont^S is OPEN; it is still the lane's largest gap toward a non-vacuous OS
  reconstruction.
- **T13:** tally below; §12.1 unchanged (the reviewer's text already states that no instance of (PLD^mod_dis) was
  established for the soft chain; that sentence is now out of date in one respect, recorded in §12.2).


---

## 15. Session 6 (2026-10-27): non-abelian soft noise, interacting H-cont^S, and the assembled conditional theorem

### 15.0 Pre-stated targets (2026-10-27 23:21 UTC; written before any derivation below, after reading §12-§14, LOG session 5, REVIEW_X3_X4's binding fixes and strategic verdict, checks/x4*, P/PLD.md (lane E session 1: targets only, no derivations yet) and P/RLARGE.md §0, §1A, §8. checks/x5_criteria.md was written a few minutes earlier, after the targets were fixed in the session brief and before any derivation here or any script)

**T14 (non-abelian soft noise; the bias question).** Extend Theorem GS from the free Gaussian chain to the compact
SU(N) soft chain in the small-field regime. Specifically: (a) write the per-level soft step on gauge-invariant block
quantities as a heat-kernel-type convolution, exactly where possible; (b) decide whether a **bias** term exists, i.e. a
noise-induced drift of the block plaquette that is not damped by L^{-2n} and could accumulate over K levels; (c) if an
O(σ²) background-dependent term exists, decide whether it is damped, or renormalises the coupling (then say precisely
how it is absorbed into (F)). **Success:** an exact one-step statement plus a proof that no undamped O(σ_i²) term
exists, with the K-uniformity of the remainder either proven or named. **Valid failure:** an explicit undamped term
(with its coefficient), and which existence statements it breaks. **Not success:** a symmetry argument that silently
assumes centrality of the kernel where it does not hold.

**T15 (interacting H-cont^S).** Given layer-1 hypotheses (named, with owners), prove lim_{s→0} limsup_K
E|E[τ_sF - F | U_0]|² = 0 on a dense set, or name the wall exactly. Also re-examine what H-cont^S is needed for.
**Success:** a proven implication from named hypotheses. **Valid failure:** the precise missing estimate, with the
reductions that are proven. **Not success:** an L²(ω) statement about soft variables (false, [RX34-fix 2]).

**T16.** Review §12.2's proposed amended clause; keep it conservative. Then **ASSEMBLY**: the full conditional existence
theorem as it now stands, one statement, with the exact hypothesis list (each with provenance and the layer-1 file
that owns it).

**Check plan (x5).** checks/x5_criteria.md: A (exact SU(2) one-step identities), B (one literal S4' step on compact
noise: the small-noise coefficient against the linear-response value 38/81; BIAS if > 1.0), C (two steps,
informational).

# Session 6 derivations (written after §15.0)

### 15.1 T14 (a): the compact soft step as a heat-kernel-type convolution

Setting: Setting S (§13.1). One step k → k + 1, conditioned on U_k ("the parents"). For a level-(k+1) link c the kernel is
k_c(V) = exp(-(κ/g_k²)[1 - N^{-1}Re tr(V^{-1}M̄_c)])/𝒩_k(M̄_c), M̄_c the S4' contour mean of U_k (a point of the convex hull
of SU(N)). Given U_k the V_c are independent.

**Lemma NA-1 (symmetry of the soft kernel; exact centrality for SU(2)). PROVEN-HERE.**
(a) Let V_0 maximise Re tr(V^{-1}M̄) over SU(N) and A := V_0^{-1}M̄. Then A = H + ic·1 with H Hermitian, c ∈ R.
(b) Put V = V_0Z. Under k_c the law of Z has Haar density ∝ exp((κ/(Ng_k²))Re tr(Z^{-1}A)). It is invariant under
Z ↦ Z^{-1} if c = 0, and under all conjugations Z ↦ hZh^{-1} if A is a real multiple of 1.
(c) **SU(2).** M̄ = rW with W ∈ SU(2) and r := |M̄| ∈ [0, 1] (quaternion norm). If r > 0, V_0 = W, A = r·1, and the law of
Z := W^{-1}V is μ_t, t := κr/g_k², the central, inversion-symmetric law with Haar density exp(t cos θ)/c(t) (Z has
eigenvalues e^{±iθ}). If r = 0 the kernel is Haar.
(d) a(t) := ∫(tr Z/2)dμ_t = I_2(t)/I_1(t), more generally d_j^{-1}∫χ_jdμ_t = I_{2j+1}(t)/I_1(t) (spin j), and
  0 ≤ 1 - a(t) ≤ 3/(2t)  for all t > 0.
*Proof.* (a) For Y ∈ su(N), d/dε Re tr(e^{-εY}A)|_0 = -Re tr(YA) = 0. Write A = H + S (Hermitian + anti-Hermitian parts);
tr(YH) is imaginary and tr(YS) real, so tr(YS) = 0 for every traceless anti-Hermitian Y, i.e. S ∈ iR·1. (b) Re tr(V^{-1}M̄)
= Re tr(Z^{-1}A); Haar is invariant under V ↦ V_0Z. For A Hermitian, tr(Z^{-1}A) = tr(Z^†A) is the complex conjugate of
tr(AZ) = tr(ZA), so the density is inversion invariant; for A = a·1 it is a class function. (c) The real span of SU(2)
in M_2(C) is the quaternion algebra, on which the matrix average is the quaternion average and det = |·|²; a quaternion
of norm r > 0 is r times a unit quaternion. With A = r1, Re tr(Z^{-1}A)/2 = r cos θ, so the exponent is
-(κ/g²)(1 - r cos θ) and the Z-law is μ_t. (d) The character expansion e^{t cos θ} = (2/t)Σ_j(2j + 1)I_{2j+1}(t)χ_j
[STANDARD] and orthonormality of characters give ∫χ_j e^{t cos θ}dZ = (2/t)(2j + 1)I_{2j+1}(t) and c(t) = (2/t)I_1(t).
For the bound put u := 1 - cos θ ∈ [0, 2]; Haar's θ-density (2/π)sin²θ becomes ∝ u^{1/2}(2 - u)^{1/2}du, so
1 - a(t) = E_{hν}[u] with ν(du) ∝ u^{1/2}e^{-tu}1_{[0,2]}du and h(u) = (2 - u)^{1/2}. h is decreasing and u increasing, so
Cov_ν(u, h) ≤ 0 (Chebyshev's association inequality) and E_{hν}[u] ≤ E_ν[u]; ν is the Gamma(3/2, t) law conditioned on
{u ≤ 2}, and conditioning on a lower set lowers the mean of an increasing function: E_ν[u] ≤ 3/(2t). ∎
- For N ≥ 3 the kernel is in general **not** central: A = H + ic1 with H non-scalar at order δ² (δ the contour spread of
  Lemma KN, which gives ||W'^{-1}M̄ - 1|| ≤ 3δ²), and c ≠ 0 at order δ³ (the phase of det M̄ starts at third order:
  the second-order part of W'^{-1}M̄ - 1 is (Σw_iX_i² - X̄²)/2, Hermitian). These orders are ARGUED here (uncounted); the
  exact statements below are for SU(2), or for SU(N) when every V_{0,c}^{-1}M̄_c is a real scalar (e.g. a flat parent field).

**Lemma NA-2 (one-step convolution form; no drift of the location). PROVEN-HERE | Lemma NA-1.** Suppose that, given U_k,
V_c = W_cZ_c for every level-(k+1) link c, with W_c a function of U_k and the Z_c conditionally independent with central,
inversion-symmetric laws μ_c (SU(2): W_c = M̄_c/|M̄_c|, μ_c = μ_{t_c}, t_c = κ|M̄_c|/g_k²). Let C = c_1^{ε_1}⋯c_ℓ^{ε_ℓ} be a closed
level-(k+1) loop with **distinct** links, W_C the same product of the W's. Then:
(i) V_C = W_C·Ỹ_C, where, given U_k, Ỹ_C has the law μ_{c_1} * ⋯ * μ_{c_ℓ} (convolution), central and inversion-symmetric;
(ii) for every irreducible ρ, E[χ_ρ(V_C) | U_k] = Π_iμ̂_{c_i}(ρ)·χ_ρ(W_C), μ̂(ρ) := d_ρ^{-1}∫χ_ρdμ ∈ [-1, 1] (real);
(iii) the conditional law of V_C is invariant under the geodesic symmetry V ↦ W_CV^{-1}W_C about W_C, and the law of
W_C^{-1}V_C is central: **the step moves no block holonomy's location**; only its spread changes;
(iv) (SU(2)) E[1 - tr V_C/2 | U_k] = (1 - Π_ia(t_{c_i})) + Π_ia(t_{c_i})·(1 - tr W_C/2), with
  0 ≤ 1 - Π_ia(t_{c_i}) ≤ Σ_i 3g_k²/(2κ|M̄_{c_i}|).
*Proof.* (i) V_c^{-1} = W_c^{-1}(W_cZ_c^{-1}W_c^{-1}) and W_cZ_c^{-1}W_c^{-1} ~ μ_c (inversion and conjugation invariance), so
V_{c_i}^{ε_i} = A_iY_i with A_i = W_{c_i}^{ε_i} and Y_i ~ μ_{c_i} independent. Then A_1Y_1⋯A_ℓY_ℓ = (A_1⋯A_ℓ)Π_i(B_i^{-1}Y_iB_i)
with B_i := A_{i+1}⋯A_ℓ (induction on ℓ: A_1Y_1A_2 = A_1A_2(A_2^{-1}Y_1A_2)). Conjugation by fixed B_i preserves μ_{c_i};
a product of independent central factors has the convolution law, which is central; central measures commute under
convolution, so Ỹ^{-1} (the reversed product of inverses) has the same law. (ii) For central μ, ∫ρ(y)dμ(y) commutes with
ρ(G), so equals μ̂(ρ)·1 (Schur), and E[χ_ρ(W_CỸ)] = tr(ρ(W_C)Π_iμ̂_i(ρ)) by independence; real by inversion symmetry.
(iii) W_CỸ ↦ W_CỸ^{-1}, and law(Ỹ^{-1}) = law(Ỹ). (iv) (ii) with ρ the fundamental; 1 - Πa ≤ Σ(1 - a_i) for
a_i ∈ [0, 1] (a(t) ≥ 0: a = E cos θ and the density is increasing in cos θ, so Cov(cos θ, e^{t cos θ}) ≥ 0 under Haar,
whose mean of cos θ is 0), and Lemma NA-1 (d). ∎
- **Reading.** For gauge-invariant block quantities the soft step is exactly a convolution with a central heat-kernel-
  type law ("contraction plus floor"): characters are multiplied by Πμ̂ ≤ 1, and 1 - tr/2 acquires the additive floor
  1 - Πa ≈ Σ_c 3g_k²/(2κ), the compact form of the n = 0 term 4σ² of Theorem GS (three components, 1 - cos θ ≈ θ²/2:
  (3/2)·4σ² = 6σ², σ² = g²/κ). The "contraction" is not a drift: the location is exactly W_C (iii). In the Lie chart at
  1 the mean of log V_C is (1 - O(σ²))log W_C (BCH: E[ad_η²] ≤ 0), which is a property of the chart, not of the law.
- **Abelian sanity anchor.** For U(1) the same lemma says E[e^{iθ_{k+1}} | ·] = e^{-σ²/2}e^{iθ^{det}}: the factor is the floor,
  and the injected angle noise is then averaged by later steps exactly as in GS-2. The non-abelian question is only
  whether the commutator terms of later averaging steps create something that is not of this type; §15.2.

**Proposition NA-3 (flat background: no additive drift at any depth, any N). PROVEN-HERE | gauge covariance of the
kernels, (C).** Let U_0 be pure gauge. Gauge-transform so that U_0 = 1. Then for every level j, every class and every
closed level-j loop C (based at a level-j site, in that site's frame), the conditional law of V_C given U_0 = 1 is central
and inversion-symmetric. Hence E[V_C | U_0 = 1] = α_C·1 with α_C ∈ [-1, 1] real, and E[log V_C | U_0 = 1] = 0 (log taken
with spectrum in (-π, π), defined almost surely).
*Proof.* The joint law of all levels given U_0 is covariant under fine gauge transformations acting on each level by
restriction to that level's sites (§13.2 soft-layer transfer); a constant transformation h fixes U_0 = 1, so the
conditional law is h-invariant and V_C ↦ hV_Ch^{-1}. Complex conjugation U ↦ Ū (on every level) fixes U_0 = 1, maps
M̄_c(U) to M̄_c(Ū) = conj(M̄_c(U)), and leaves k_c invariant (Re tr is real; 𝒩(M̄̄) = 𝒩(M̄) by V ↦ V̄, which preserves Haar);
so law(V̄_C) = law(V_C). V̄ = (V^{-1})^T has the eigenvalues of V^{-1}, and a central law on SU(N) is determined by the law
of the eigenvalues (Weyl), so law(V_C^{-1}) = law(V̄_C) = law(V_C). Schur and inversion give E[V_C] = α1, α = conj(α). The
law of log V_C is invariant under X ↦ -X. ∎
- So the **noise alone produces no su(N)-valued drift of any block holonomy at any depth**, for every N; what it produces is
  the floor 1 - α_P (C = P), the compact analogue of N_j. Whether the floor converges as K → ∞ is the remaining question
  (§15.2).

### 15.2 T14 (b), (c): the floor at depth, and what could renormalise

**Theorem NA-GS1 (the small-noise coefficient of the compact floor is Theorem GS). PROVEN-HERE | Lemmas NA-1, NA-2,
GS-1, Theorem GS.** SU(2), U_0 = 1, kernel couplings εg_i² (ε > 0 a common scale; g_i, κ fixed), K, j, P fixed. Let
f(ε) := E[1 - tr V_P^{(j)}/2 | U_0 = 1] (level-j block plaquette) and φ(ε) := E[1 - tr W_P^{(j)}/2 | U_0 = 1] (its parent's
deterministic block plaquette, before the last kernel). With σ_i² := g_i²/κ and N_j as in Theorem GS (i),
  lim_{ε→0} f(ε)/ε = (3/2)N_j,   lim_{ε→0} φ(ε)/ε = (3/2)(N_j - 4σ²_{j-1}),
and N_j converges geometrically as K → ∞ at fixed resolution m = K - j (Theorem GS).
*Proof.* K is fixed, so only finitely many links (the ancestor cone of P) enter. (1) *Concentration.* μ_t(θ > ρ) ≤
C(t)e^{-t(1 - cos ρ)} with C(t) polynomial; t = κr/(εg²) with r ≥ 1/2 on the event below. Take ρ = ε^{1/3}: by induction
over levels, on the event G that every Z in the cone has θ ≤ ε^{1/3}, every contour spread is O(ε^{1/3}) (constants
depending on K), so every M̄ has r ≥ 1/2 and the polar map is real-analytic there; P(G^c) ≤ C_Ke^{-cε^{-1/3}} = o(ε), and
the integrand is ≤ 2. (2) *Linearisation.* Use Lie coordinates φ ∈ R³, Z = exp(iΣ_aφ^aσ_a) (σ_a the
Pauli matrices, so θ = |φ|). The contour product is exp(Σ±φ_b + O(φ²)), the contour mean is 1 + Q_rootφ + O(φ²) with
Q_rootφ anti-Hermitian, and its polar part is exp(Q_rootφ + O(φ²)); so the chain is, componentwise, the linear soft chain
B_{i+1} = Q_rootB_i + φ_i of §14.1 plus O(φ²) corrections, and the block-plaquette logarithm is Φ_P = dB_j(P) + q + O(|φ|³)
with q quadratic. 1 - cos|Φ| = |Φ|²/2 + O(|Φ|⁴). (3) *Moments.* Given the earlier levels, φ_i has the law of μ_{t}: centred,
symmetric under φ ↦ -φ, E[φ^aφ^b | past] = δ^{ab}t^{-1}(1 + O(t^{-1})), E|φ|⁴ = O(t^{-2}); t^{-1} = εσ_i²/r with
r = 1 - O(ε) on G. (4) *Expectation.* E|Φ_P|²/2 = E|dB_j(P)|²/2 + E⟨dB_j(P), q⟩ + O(ε²). The cross term is a sum of
expectations of cubic monomials in the φ's; take the latest level i* occurring in a monomial: if it occurs once or three
times the conditional expectation given the past vanishes by symmetry; if twice, it is E[φ_e·E[φ_{i*}φ_{i*} | past]] =
E[φ_e·εσ²/r(past)](1 + O(ε)), and r(past) = 1 - (even quadratic) + O(φ³), so this is O(ε²). Hence f(ε) =
(ε/2)Σ_{a=1}^{3}Var(dB^a_j(P))|_{σ²} + O_K(ε²), and Var(dB^a_j(P)) = N_j per component for a flat fine field (Theorem GS (i)
with g_0 = 0). For φ(ε) drop the last injection (the n = 0 term 4σ²_{j-1}). ∎
- **The constant in O_K(ε²) depends on K.** The theorem fixes the O(σ²) part of the floor exactly; it does not prove that
  the remainder is uniformly small in K. That uniformity is named below as (NA-R2).
- Check x5 B tests the one-step coefficient (3/2)(4/3)(2L^{-2} + L^{-4}) = 38/81 with the literal S4' contours.

**Bias verdict (T14 (b)).**
1. **No additive bias exists** (Proposition NA-3, exact, every N, every depth): the noise induces no su(N)-valued drift of
   any block holonomy; at one step and any background (SU(2)) the location of every block loop's conditional law is
   exactly the parent's deterministic W_C (Lemma NA-2 (iii)).
2. **The O(σ²) part of the floor is damped exactly as in the free chain** (Theorem NA-GS1): noise injected n levels below
   contributes (3/2)(4/3)σ²(2L^{-2n} + L^{-4n}) to the block-plaquette floor at order σ². So no undamped O(σ_i²) term exists,
   and the O(σ²) part converges geometrically in K - m.
3. **Anything undamped is O(σ_i⁴) or smaller, and is summable under (F).** The lower half of (F) gives
   g_r² ≤ 1/(1/g² + β_-r log L), so Σ_{r>m}σ̂⁴(r) ≤ κ^{-2}Σ_r(1/g² + β_-r log L)^{-2} < ∞, uniformly in K. With constant
   couplings (no running) an undamped σ⁴ term would grow linearly in K; under (F) it cannot. Cross terms of two deep
   injections are products of two damped images, and the commutator of a level-i injection with the accumulated field at
   level i is a new local injection of size σ_iσ̄, damped thereafter (σ_i²σ̄²L^{-2n}); summable. (ARGUED, uncounted.)
4. **What is not proven.** The uniformity in K of the remainder of Theorem NA-GS1:
   **(NA-R2) (uniform second-order remainder of the compact soft chain; OPEN, new, this lane).** There is C, independent
   of K, m, the torus and the coupling sequence within (F), such that in the flat-background SU(N) soft chain,
   |E[1 - N^{-1}Re tr V_P^{(j)}] - c_NN_j| ≤ C Σ_{n=0}^{j-1}(σ⁴_{j-1-n} + σ²_{j-1-n}σ̄²(n + 1)L^{-2n}),
   with c_N the normalisation constant of the quadratic part (c_2 = 3/2 in the coordinates of Theorem NA-GS1; the left
   side is then |E[1 - N^{-1}Re tr V_P^{(j)}] - c_NN_j|), σ̄² := max_iσ_i². Under (F) the right side is bounded uniformly
   in K, so (NA-R2) ⇒ the compact noise floor at fixed m is bounded uniformly in K, with its O(σ²) part convergent
   (Theorem GS). (Full convergence of the floor would need the same bound for the K-dependence of the remainder; it is
   not claimed. For the existence theorem, uniform boundedness is what is used: limits along subsequences exist by
   compactness.) The difficulty is not entropy: a large
   field at one ancestor link enters the block plaquette with an influence weight O(L^{-3n}), so a union bound over the
   L^{4n} ancestors is not needed; but the weighted (Efron-Stein-type) influence bound for the polar averages, uniform in
   the depth, is not written.
- **(N ≥ 3).** Proposition NA-3 holds as stated; Lemma NA-2 holds only where the kernels are central. The non-central part
  of the kernel (order δ² anisotropy, order δ³ inversion-asymmetry, Lemma NA-1 remark) enters the floor at order σ²δ² and
  is part of (NA-R2)'s remainder (ARGUED).

**Background-dependent O(σ²) terms (T14 (c)): damped, or the coupling? ARGUED (uncounted), with an exact core.**
- Exact core: Lemma NA-2 (iii) — at the step where the noise is injected the location does not move. A background-
  dependent drift can appear only at the *next* averaging step (the polar part of the mean of noisy transporters is not
  the polar part of the mean of the deterministic ones), as a gauge-covariant su(N)-valued functional Δ_c of the background
  on the link's support, of order σ².
- Parity count: under the reflection R_μ through the link's midpoint (perpendicular to its direction μ) the link is
  reversed, so Δ_c is odd; under each transverse reflection R_ν (ν ≠ μ, through the link's line) the link and the contour
  set are fixed, so Δ_c is even. A monomial in the curvature components F_{αβ} with no derivatives has an even total number
  of index slots; R_μ-oddness needs an odd number of μ-slots and R_ν-evenness an even number of ν-slots for every ν ≠ μ,
  whose total is odd. So **no zero-derivative (marginal or relevant) drift exists at any order in F**; the first allowed
  term has one covariant derivative, D^νF_{νμ}, which is irrelevant (it contributes to the block curvature at relative order
  (block size)², i.e. damped like L^{-2n} on smooth fields). For a background that is locally a constant abelian field
  the drift vanishes exactly (R_μ and the product of all R_ν act identically on constant F, while Δ_c is odd under one and
  even under the other). (Formal gradient expansion; uncounted.)
- **What does renormalise, and where it goes.** The only marginal object the kernel noise can affect is the coefficient
  of the Wilson term in the effective action of U_{k+1}, i.e. the soft scheme's flow. In the free chain it does not (the
  injected noise's curvature symbol vanishes at zero momentum, GS-2 (e)); in the interacting chain its effect is part of
  the one-loop flow coefficient of the soft scheme, whose per-level 1/g² shift is b_0 log L + O(g²) by one-loop
  universality [STANDARD perturbative fact; not re-derived]. **It is absorbed into (F) by the definition of (F) for the
  soft scheme** (RLARGE §0 / (I_k): (F) is a statement about the effective couplings g̃_k of the soft chain, i.e. node A5,
  whose computation must include the kernel's contribution). No new hypothesis is needed, and no existing statement of
  this file changes: every use of (F) here already takes the kernel couplings equal to the (F) sequence.

**T14 outcome.** (a) MET (exact for SU(2) and for central kernels; Lemma NA-2). (b) **No bias: PROVEN** in the two
senses that admit an exact statement (no additive drift, Proposition NA-3; the O(σ²) part damped, Theorem NA-GS1);
uniformity of the remainder named as (NA-R2) (OPEN), with an ARGUED reason why it is summable under (F) even if undamped
at order σ⁴. (c) Background-dependent drift: none at the injection step (exact); at the next step no zero-derivative term
by parity (ARGUED); the marginal (coupling) effect is inside (F) by definition (ARGUED; universality not re-derived).

### 15.3 T15: what H-cont^S is needed for, and the interacting case

**Theorem X-KER^S (iv) (the soft transfer semigroup has trivial kernel; unconditional). PROVEN-HERE | X-OS^S, the proof of
X-KER's inclusion [𝔄_{++}] ⊂ 𝒦^⊥ (§10.2).** In the setting of §14.3 (𝔄^S_+ = the C*-algebra generated by soft generators
whose continuum supports lie in the **open** half-space {x_0 > Π_0} [RX34-fix 1]), 𝒦^S := ker T(2) = {0}. Hence
T(s) = e^{-sH} for every s ∈ 2D_+, with H ≥ 0 self-adjoint on **all** of H^S_ω, and s ↦ e^{-sH} is strongly continuous
for real s ≥ 0.
*Proof.* A soft generator G depends on finitely many soft variables of fixed (K-independent) resolutions; its continuum
support is a finite union of closed cubes, hence compact, and lies in the open half-space, so it has distance d > 0 from
Π_0. A product of finitely many generators has the union of their supports, again at positive distance. Pick s ∈ 2D_+
with s < d (2D_+ = {2jL^{-m}} has arbitrarily small elements). Then τ_{-s}G is a soft generator (a translation by -s ∈ D
maps the class tree to itself and translates continuum supports) with support still in the open half-space, and
T(s)[τ_{-s}G] = [G]. So [G] ∈ Ran T(s) ⊂ (ker T(s))^⊥ = 𝒦^⊥ (T(s) bounded self-adjoint, ker T(s) = 𝒦 by X-OS (iii)). The
same holds for every element of the *-algebra generated by the generators (linear combinations; adjoints have the same
support). That *-algebra is norm-dense in 𝔄^S_+, and ||[F]||_OS ≤ ||F||_∞ (X-KER^S (ii)), so its classes are dense in
H^S_ω. A closed subspace containing a dense set is everything: 𝒦^⊥ = H^S_ω. The rest is X-OS (iii). ∎
- **Why this was missed, and what it does not say.** X-KER (§10.2) was written for the deterministic branch, whose 𝔄_+
  contains block generators touching Π_0; there 𝒦^⊥ = closure[𝔄_{++}] (X-KER (i)) and H-bl was needed to reach the
  plane-touching ones. [RX34-fix 1] redefined the soft class by **open** continuum supports (for RP), which removes every
  plane-touching generator; X-KER (i) then gives 𝒦 = {0} at once. Session 5's X-KER^S (iii) (H-cont^S ⇒ 𝒦 = {0}) is
  correct but its hypothesis is not needed. Equally for the deterministic branch: the OS space built from 𝔄_{++} alone has
  trivial kernel (this is X-KER (i) read differently); H-bl / H-cont matter only if plane-touching block observables are
  to be included. **This does not touch non-triviality:** H^S_ω may still be CΩ ([RX12-fix 10]); 𝒦 = {0} on CΩ is
  vacuous. What the theorem removes is the separate "time continuity" gap, not the triviality gap.
- **What H-cont^S is still for: spatial translations.** The spatial L-adic translations act on H^S_ω as a unitary
  representation U of D³ commuting with e^{-sH} (X-SYM^S, translation invariance of ω, τ_a preserving 𝔄^S_+). Positivity
  gives continuity in time; nothing gives it in space: a unitary representation of D = Z[1/L] need not be continuous in
  the real topology (its dual group, the L-adic solenoid, has characters that are discontinuous on D ⊂ R). The spatial
  form of H-cont^S,
  **(H-cont^S_sp)**: lim_{a→0, a∈D³} limsup_K E_{μ_K}|E_{P_K}[τ_aF - F | U_0]|² = 0 for F in a set whose span is dense in 𝔄^S_+,
  gives ||U(a)[F] - [F]||_OS → 0 (X-KER^S (ii)), hence strong continuity of U and its extension to a strongly continuous
  unitary representation of R³ (the translation half of OS1 for the reconstructed theory). Temporal H-cont^S is no longer
  needed for anything stated in this file.

**Proposition H-cont^S-red (the K → ∞ limit can be taken first; reduction to single loops). PROVEN-HERE | Setting S
(the class tree), X-CONS^S, joint continuity of the kernels.** Let F be a bounded function of finitely many soft variables
of resolutions ≤ m, a ∈ D⁴ with level n := n(a) := min{n : a ∈ L^{-n}Z⁴} > m, and K ≥ n.
(i) E_{P_K}[τ_aF | all variables of resolution ≥ n] = F̂(τ_aU^{(n)}), where U^{(n)} is the (shared) resolution-n field and
F̂ := E[F | U^{(n)}] is a continuous function of finitely many resolution-n variables (it depends on K only through the
kernel couplings of resolutions m…n, and converges along the subsequence).
(ii) E_{μ_K}|E_{P_K}[τ_aF - F | U_0]|² ≤ E_{ν^S_{K,n}}|F̂∘τ_a - F̂|², and limsup_K of the left side along the subsequence is
≤ E_{ν^S_{*,n}}|F̂∘τ_a - F̂|², a quantity of the **limit** resolution-n law and n - m kernels only.
(iii) For F = Π_iW_{C_i} (products of block Wilson-loop traces, W_C := N^{-1}tr V_C) and any coupling (𝒮(U, ω), 𝒮(U', ω)) of
the n → m soft chains started at U and U' (e.g. synchronous: the same driving variables ω),
  E_ν|F̂∘τ_a - F̂|² ≤ 2Σ_iE_νE_ω|W_{C_i}(𝒮(τ_aU, ω)) - W_{C_i}(𝒮(U, ω))|.
(iv) Products of Wilson-loop traces (loops of the union graph of finitely many resolutions and classes) span a norm-dense
subalgebra of the coarse-gauge-invariant continuous functions of finitely many soft variables.
Hence (H-cont^S_sp) (and its temporal analogue) ⇐ **(H-SYN)**: for every m, every block loop C and a → 0 in D³,
E_{ν^S_{*,n(a)}}E_ω|W_C(𝒮(τ_aU, ω)) - W_C(𝒮(U, ω))| → 0 for some coupling ω.
*Proof.* (i) For r ≥ n, [a]_r = 0, so the shifted and unshifted trees share every variable of resolution ≥ n; below
resolution n the shifted tree is the translate of the unshifted one, driven by the shared U^{(n)} (§13.1, X-2GRID^S).
By the Markov property of the tree, given all variables of resolution ≥ n the coarser variables depend only on U^{(n)}.
Continuity: the kernels are jointly continuous and bounded (§13.1 "Continuity"), and F̂ is a finite iterated integral of
them against F. (ii) U_0 is a variable of resolution K ≥ n, so E[G | U_0] = E[E[G | res ≥ n] | U_0] for G := τ_aF - F;
conditional Jensen gives the first inequality. |F̂∘τ_a - F̂|² is a bounded continuous function of finitely many
resolution-n variables, so its ν_{K,n}-expectation converges along the subsequence to its ν_{*,n}-expectation (X-ALG^S;
the kernel couplings converge along the subsequence, X-CONS^S). (iii) F̂(U) = E_ωF(𝒮(U, ω)) for any coupling, and
|ΠW_i - ΠW'_i| ≤ Σ|W_i - W'_i| for |W_i|, |W'_i| ≤ 1; then |x|² ≤ 2|x| for |x| ≤ 2 and Jensen. (iv) Gauge orbits of
finitely many links on a connected graph correspond to holonomy representations of the graph's fundamental group up to
conjugation; a unitary representation is determined up to unitary equivalence by its character, and U(N)-conjugation
equals SU(N)-conjugation up to scalars (which act trivially), so fundamental Wilson-loop traces separate gauge orbits
(disconnected graphs: componentwise). The span of their products is a unital *-algebra (tr V^{-1} = conj tr V) of
continuous functions on the compact orbit space; Stone-Weierstrass. ∎
- **Free instance.** In the free Gaussian soft chain the synchronous difference is deterministic (Lemma GS-1: the noise
  cancels exactly), and (H-SYN) is X-CONT-G (ii); this re-derives Corollary X-CONT-G^S.

**The interacting case: the wall (named).** (H-SYN) in the interacting chain needs two estimates on the limit soft laws:
- **(H-corr^S) (curvature-covariance domination, every resolution; OPEN).** Uniformly in n and the volume, for the
  resolution-n limit soft law on the small-field event (transported block-plaquette logarithms 𝔉^{(n)} in a small-field
  gauge) and every test 2-form χ: E|⟨χ, 𝔉^{(n)}⟩|² ≤ C_cg_n²||χ||²_{ℓ²}. This is H-corr (§10.2) for the soft variables, and
  it is the same operator-norm input as (PLD^mod_dis)'s Gaussian route; its free instance is Theorem GS (ii) / Corollary
  PLD-G^S. Layer-1 sources it would come from: the small-field package (SF)_k with node N5's covariance bounds (PROOF;
  RLARGE §8.2 (SF)), (PLD)_k to restrict to the small-field event (owner PLD.md, lane E), and (F).
- **(H-lin^S) (linearisation of the composite soft map under synchronous coupling; OPEN).** The synchronous difference
  W_C(𝒮(τ_aU, ω)) - W_C(𝒮(U, ω)) equals the linear composite difference ⟨τ_aψ_C - ψ_C, 𝔉^{(n)}⟩ (ψ_C the composite test
  form of a spanning surface of C, X-CONT-G (i)) up to o(1) in L¹ as n → ∞. At linear order the noise cancels exactly
  (Lemma GS-1); the second-order remainder is the object of (NA-R2): commutator terms of the averaging, injected at each
  intermediate resolution and damped thereafter. (NA-R2) and (H-lin^S) are two readings of one estimate: the uniform-in-
  depth second-order remainder of the compact soft map.
- (H-corr^S) + (H-lin^S) ⇒ (H-SYN): ARGUED (uncounted), by X-CONT-G's proof with β^{-1} → C_cg_n² (it uses only an
  ℓ²-domination of the curvature covariance) and the L¹-smallness of the remainder; the large-field event is handled by
  (PLD)-type local probabilities via Theorem CB, which costs a term that is small uniformly in n only if the large-field
  influence on W_C is weighted (same influence bound as in (NA-R2)). Not written as a proof.

**T15 outcome.** The pre-stated target (H-cont^S in the interacting case) is **not proven**; the wall is named: (H-corr^S)
+ (H-lin^S), with (H-lin^S) = the depth-uniform second-order remainder (NA-R2) that also limits T14. Proven along the way:
(1) **𝒦^S = {0} unconditionally** (Theorem X-KER^S (iv)): the purpose for which H-cont^S was introduced is met without it;
(2) the K → ∞ limit in H-cont^S can be taken first (Proposition H-cont^S-red (ii)), and products of loops reduce to single
loops under any coupling of the kernel noise ((iii), (iv)). H-cont^S's remaining role is spatial continuity (H-cont^S_sp).

### 15.4 Check x5
Criteria checks/x5_criteria.md written before checks/x5_su2_soft.py; output checks/x5_out.txt; record checks/x5_time.txt.
- **A: PASS.** A1: quaternion average = matrix average and M̄^†M̄ = det(M̄)·1 to 2.2e-16 (Lemma NA-1 (c)). A2: the μ_t sampler
  matches I_2/I_1 at t = 5, 20, 100 (0.81, 0.41, 0.02 SE); 1 - a(t) ∈ [1.5e-4, …] and max (1 - a)/(3/(2t)) = 0.999975 on
  t ∈ [0.1, 10⁴] (the bound of Lemma NA-1 (d) is sharp as t → ∞). A3: one plaquette, random background, t_c ∈ {8, 15, 30,
  60}, 4·10⁶ samples: E[tr V_P/2] = -0.013513 ± 2.0e-4 vs Πa·tr W_P/2 = -0.013751 (1.19 SE); location (vector part of
  W_P^{-1}V_P) 1.33, 1.25, 0.11 SE (Lemma NA-2 (ii), (iii)). The normalised kernel by an independent route (rejection
  from Haar, r = 0.32, t = 6): mean Re(W^{-1}V) at 1.02 SE from a(6); vector components -3.8, +1.0, -1.3 SE (within the
  pre-stated 4 SE, the first marginally). **Post-hoc, not pre-registered:** the same test with three new seeds and 10⁶
  accepted samples each gives all vector components within 1.8 SE (checks/x5_posthoc_kernel.py, x5_posthoc_out.txt); the
  -3.8 SE is read as a fluctuation (Lemma NA-1 (c) is exact algebra).
- **B: PASS** (pre-stated criterion; no BIAS). One literal S4' polar step of iid compact noise, flat background, 2000
  samples per t: R(t) = t·E[1 - tr W_P/2] = 0.6935, 0.5656, 0.5140, 0.4907, 0.4796 (± ≤ 0.0009) at t = 25, 50, 100, 200, 400;
  weighted fit R_∞ = 0.4611 ± 0.0004 vs 38/81 = 0.4691 (|diff| 0.008 ≤ 0.015) and R(400) within 2.2% of 38/81. Depth-0
  value 6. **Caveat on the fit:** χ²/dof = 101, so R_∞ + b/t is not an adequate model over t ∈ [25, 400] (curvature in 1/t);
  the statistical SE of R_∞ understates its error, and the PASS rests on the tolerance 0.015 and on R(400). NA-3
  sub-check PASS (all W_P vector-part means within 2.9 SE).
- **Finding (informational): the O(σ⁴) term is not damped at the step that creates it.** b ≈ +5.6 at depth 1 against
  b_0 ≈ -15 at depth 0: the depth-1 second-order coefficient is about a third of the depth-0 one in size (opposite sign),
  not L^{-2} smaller. This is the expected commutator noise: BCH commutators of the noisy contour products are a fresh,
  mean-zero coarse-level noise of variance O(σ⁴), injected at the averaging step. It is the term Σσ⁴_{j-1-n} (no L^{-2n})
  kept in (NA-R2)'s bound; §15.2 item 3 had it as ARGUED.
- **C (informational): as expected.** Two literal steps on (Z/27)⁴, t = 100, 24 samples: one-step value 0.5142 ± 0.0006
  (agrees with B's 0.5140), two-step R2 = 0.0546 ± 0.0005 vs linear response 0.0497 (+10%), and R2/R(100) = 0.1062 vs the
  linear ratio 0.1059. So the second step damps the total depth-1 floor, including its O(σ⁴) excess, by the linear factor:
  the excess created at one step is damped afterwards like injected noise, not carried undamped. (One t only; no σ-scan
  at depth 2.)
- Resources: 289 s wall, peak RSS 922 MB (< 1 GB), one process, nice 10, BLAS threads 1, load 2.7, memory free 42%,
  numeric lock held; `python3` without -I (user-site numpy/scipy; the script reads no external files). Post-hoc re-run under
  the lock, same settings.

### 15.5 T16: review of §12.2's proposed clause (conservative)

§12.2 proposed replacing, in §12.1, "(a moderate-deviation bound for the small-field measure, for which no instance is
established for the soft chain, even for free fields)" by "(a moderate-deviation bound for the small-field measure, which
holds for the free Gaussian soft chain but is not established for the interacting compact one)".
- **Verdict: REJECT the proposed wording; a narrower replacement is proposed.** Two overstatements: (i) (PLD^mod_dis) is a
  statement about P_cut, the law conditioned on every cube being small-field; Corollary PLD-G^S is for the
  **unconditioned** law of the noncompact abelian model, which has no cut, so "holds for the free Gaussian soft chain"
  attaches a conditioned hypothesis to an unconditioned fact; (ii) "free Gaussian soft chain" can be read as the
  linearisation of the compact chain, for which nothing beyond the O(σ²) coefficient (Theorem NA-GS1, flat background) is
  shown.
- **Proposed replacement (for the next independent review; §12.1 is not edited):** "(a moderate-deviation bound for the
  small-field measure; for the soft chain only an analogue for the unconditioned law of the free, noncompact abelian
  model is established, and the compact interacting case is open)".
- **A second clause, proposed but not recommended for adoption before review.** §12.1 lists "Time continuity (kernel of the
  transfer operator = 0)" among the facts not established. For the soft variables, Theorem X-KER^S (iv) gives 𝒦 = {0}
  unconditionally. The conservative course is to leave §12.1 as is until an independent review checks X-KER^S (iv) (the
  risk to check: that the algebra on which T(s) acts in X-OS^S is the open-support class, so that no plane-touching soft
  generator exists). If confirmed, the candidate text is: "For the soft variables, whose positive-time observables are
  supported at positive distance from the reflection plane, the transfer semigroup is strongly continuous with trivial
  kernel; this is a Hilbert-space consequence of reflection positivity and says nothing about whether the Hilbert space is
  more than one-dimensional. Continuity of spatial translations, Euclidean invariance, ..." (the rest of the list
  unchanged, with "Time continuity" replaced by "continuity of spatial translations"). §12.1 as written is not false after
  session 6 (the deterministic branch's plane-touching algebra still lacks time continuity), only incomplete.

### 15.6 ASSEMBLY: the conditional existence theorem as it now stands

**Theorem ASSEMBLY (soft branch, session 6).** Let G = SU(N), N ≥ 2, d = 4, L ≥ 3 odd; μ_K the Wilson measure at bare
coupling g_0 on the fine torus of spacing L^{-K} (§1, ES1-ES2); the decision-4 soft RG chain with kernel couplings (g_k)
taken equal to the sequence of (F), κ > 0, and the class tree of L-adic shifted grids (Setting S, §13.1); 𝔄^S_+ the
open-continuum-support algebra (§13.2, [RX34-fix 1]).
(I) **Unconditionally.** Along subsequences K_j → ∞ (fixed torus; or jointly with the torus side → ∞), the joint laws
converge to a state ω on the separable C*-algebra generated by all soft block variables (all resolutions and classes) and
flowed lattice Wilson loops. ω is Markov-projective across resolutions; invariant under L-adic translations, the
hypercubic group, gauge transformations and charge conjugation; reflection positive in every plane of P on the
open-support class. The OS construction gives a Hilbert space H^S_ω, a self-adjoint H ≥ 0 such that s ↦ e^{-sH} is
strongly continuous on **all** of H^S_ω (𝒦^S = {0}), and a unitary representation of the L-adic spatial translations
commuting with e^{-sH}. [X-ALG^S, X-CONS^S, X-SYM^S, X-RP^S, X-OS^S, X-IV^S, X-KER^S (iv); NA-3 for C-invariance of the
chain.] Kernel-only facts, with no Yang-Mills content: full support and analytic densities of the limit block laws
(finite volume), ⟨1 - P⟩_m ≥ (δ^S_*/2)g'_m² (KB, LAP^S); SU(2): exact one-step convolution form with no location drift
(NA-2); every N: no additive drift of any block holonomy in a flat background (NA-3); the O(σ²) part of the noise floor
is GS-damped (NA-GS1).
(II) **Given (F) and (RLF-3^dis)** (and g^S_m small): for every m, every limit point (finite or infinite volume),
ν^S_{*,m}(||V_p - 1||_op > ε_1) ≤ C_d(g^S_m)^{-p_d}e^{-a/(g^S_m)²}, uniformly in the volume; in particular the soft limit is
not Haar at any resolution where this is below the Haar value. [CB, X-IVND^S]
(III) **Given in addition (PLD^mod_dis)** and g ≤ g_T: ω(1 - P^S_{p,m}) ≤ φ(g^S_m), so with (F) and LAP^S,
c/(1/g² + β_+(m + 1)log L) ≤ ω(1 - P^S_{p,m}) ≤ C(log m)^{2p_*}/m (the lower bound is kernel-only). [CB-sg, H-Bal-3T^S,
X-NTAF^S]
(IV) **Given in addition (H-cont^S_sp)** the spatial representation is strongly continuous and extends to a unitary
representation of R³ commuting with e^{-sH}. [X-KER^S (ii), Proposition H-cont^S-red]
**Not delivered:** dim H^S_ω > 1 (the OS space may be CΩ), OS0 for local fields, rotation invariance, uniqueness,
clustering, a mass gap, non-Gaussianity. This is not a construction of Yang-Mills theory.

**Hypothesis list (every input of (I)-(IV); provenance; owner).**
| Label | Content (pointer) | Status / provenance | Owner |
|---|---|---|---|
| X-LRP | Osterwalder-Seiler RP of the Wilson action for bounded measurable functions (§3) | IMPORTED-AND-REVERIFIED | PROOF (layer 1's re-derivation, L9a), re-read here |
| (C), (L), D4-norm (2) | contour covariance L9a′ of the S4' contours; kernel normalisation bounds | PROVEN in layer 1 | PROOF (L9a′, D4-norm; LINEAR_PACKAGE §1.3) |
| (F) | two-sided soft-scheme flow β_-(k - j)log L ≤ 1/g_j² - 1/g_k² ≤ β_+(k - j)log L | *plausible extension of H-Bal-1* (different RG scheme); OPEN as node A5 / L4a-flow; includes the kernel-noise contribution to the soft one-loop flow (§15.2) | RLARGE §0 (statement); PROOF L4a; P/FLOW.md (lane C, node A5 / L4a-flow; it appeared during this session and was not read here) |
| (RLF-3^dis) | P_K(E_all) ≤ (C_dg_k^{-p_d}e^{-a/g_k²})^{N_k}, uniform in K, k, T (§13.4) | HYPOTHESIS-NEW (this lane); would follow from RLF-3 with RLF-1, RLF-4 and node A's bulk bound under the nonnegative-ratio reading, which layer 1 has not adopted (ARGUED) | RLARGE §1A (RLF), itself reduced to (F), (SF), (H-pos), (H-Mayer), (PLD), (W1-ret'), (HIST), (SF-last) (RLARGE §8.2-§8.5); (H-pos), (HIST): P/HIST.md (lane D; appeared during this session, not read here); (PLD): PLD.md |
| (PLD^mod_dis) | variable-threshold product bound for P_cut on the families A_p (§13.6) | HYPOTHESIS-NEW, layer-1-native (strengthening of (PLD)_k (i)); only an unconditioned noncompact free analogue is proven (PLD-G^S) | PLD.md (lane E, target T1 (PLD-mod)); RLARGE §8.2 |
| smallness | g ≤ g_T; g'_m ≤ 1/2; g² ≤ κ; g_K ≤ g_RLF | explicit conditions | this lane (§13.3-§13.6) |
| (H-cont^S_sp) | spatial OS-seminorm continuity (§15.3) | OPEN (this lane) ⇐ (H-corr^S) + (H-lin^S) (ARGUED) | (H-corr^S): small-field package (SF)_k with N5 covariance bounds (PROOF; RLARGE §8.2), (PLD)_k (PLD.md), (F); (H-lin^S) = (NA-R2): this lane |
Not used by the soft theorem: H-Bal-1, H-Bal-2, H-Bal-3(3a)-form, H-loc-LF, H-sg, H-Bal-loc (deterministic branch only).
STANDARD tools used: Banach-Alaoglu/Riesz, spectral theorem and positive roots, Stone-Weierstrass, Schur's lemma, the SU(2)
character expansion, Chebyshev's association inequality.

### 15.7 Outcome against the pre-stated targets, and tally
- **T14: MET in the exact parts; remainder named.** No additive bias (Proposition NA-3, every N, every depth); one-step
  convolution with no location drift (Lemma NA-2, SU(2) and central kernels); the O(σ²) part of the compact floor is
  exactly the GS-damped linear one (Theorem NA-GS1; x5 B PASS, 38/81 at one step; x5 C, linear ratio 0.106 at two steps).
  An O(σ⁴) term is created undamped at each averaging step (x5 B finding) and damped thereafter (x5 C); with or without
  that damping it is summable under (F). Uniformity in K of the remainder: **(NA-R2), OPEN**. No background-dependent
  drift at the injection step (exact); no zero-derivative drift at the next step (parity, ARGUED); the marginal (coupling)
  effect of the kernel noise is part of the soft one-loop flow and sits inside (F) (ARGUED; universality not
  re-derived). Nothing needs to be added to (F).
- **T15: NOT PROVEN; wall named; one gap removed.** 𝒦^S = {0} unconditionally (Theorem X-KER^S (iv)): temporal H-cont^S is
  not needed. Its remaining role is spatial continuity (H-cont^S_sp). Proven reductions: K → ∞ first, single loops under
  any noise coupling (Proposition H-cont^S-red). Wall: (H-corr^S) + (H-lin^S), with (H-lin^S) = (NA-R2).
- **T16:** §12.2's wording rejected as too broad; narrower clause proposed; a time-continuity clause proposed for review,
  not adopted (§15.5). §12.1 unedited.
- **Tally (session 6): PROVEN-HERE 46 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 /
  OPEN 11.** PROVEN-HERE +6: Lemma NA-1, Lemma NA-2, Proposition NA-3, Theorem NA-GS1, Theorem X-KER^S (iv), Proposition
  H-cont^S-red. OPEN +1: (NA-R2) (with (H-lin^S) as its second reading); the H-cont entry now reads: deterministic L² form
  (needed only for plane-touching block observables) and soft spatial form H-cont^S_sp (with H-corr^S under the H-corr
  entry). ARGUED 15 (+5: N ≥ 3 non-centrality orders; undamped part O(σ⁴) and summable under (F); parity count; kernel
  noise inside (F); H-corr^S + H-lin^S ⇒ H-SYN; −1: session 5's "compact corrections damped as in GS-2", replaced by
  NA-GS1 + (NA-R2)). §15 is unreviewed.
