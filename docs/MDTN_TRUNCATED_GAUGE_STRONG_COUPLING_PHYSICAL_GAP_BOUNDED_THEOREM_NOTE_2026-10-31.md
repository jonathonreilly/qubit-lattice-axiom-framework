---
claim_id: mdtn_truncated_gauge_strong_coupling_physical_gap_bounded_theorem_note_2026-10-31
claim_type: bounded_theorem
claim_scope: >
  Fixed-lattice, Hamiltonian, finite-truncation (ASQR / j_max = 1/2) SU(2) and SU(3)
  lattice gauge theory on the 3-torus (Z_L)^3 at strong coupling. Uniform-in-L physical
  (Gauss-sector) spectral gap and unique gauge-invariant ground state. Not the Clay
  Yang-Mills mass gap problem.
upstream_dependencies: ["minimal_axioms"]
named_bridges: ["B_H (supplied Hamiltonian)", "B_G (Record-reads-Gauss-labels bridge)"]
external_theorems_used: ["Bravyi-Hastings-Michalakis 2010, Thm 1 + J_k paragraph (sec 1.1), Lemma 3.1 and end of proof (sec 4.4)",
                         "Nachtergaele-Sims 2006 / Hastings-Koma 2006 (corollary only)"]
runner: scripts/mdtn_ed_part1_reps_and_plaquette_2026_10_31.py, scripts/mdtn_ed_part2_su2_boxes_2026_10_31.py
status: proposed (unaudited); status authority is the independent audit lane only
---

# Physical gap of truncated (MDTN / Kogut–Susskind j_max = 1/2) gauge theory at strong coupling, uniform in volume

**Date:** 2026-10-31
**Type:** bounded_theorem (proposed; unaudited)
**Status authority:** independent audit lane only. This note does not set or predict an audit outcome.
**Scope sentence:** this is not the Clay Yang–Mills mass gap problem (see §6 for the exact distance).
**Runners:** `scripts/mdtn_ed_part1_reps_and_plaquette_2026_10_31.py` →
`logs/runner-cache/mdtn_ed_part1_reps_and_plaquette_2026_10_31.txt`;
`scripts/mdtn_ed_part2_su2_boxes_2026_10_31.py` → `logs/runner-cache/mdtn_ed_part2_su2_boxes_2026_10_31.txt`.
Requirements: Python 3, numpy, scipy (run with numpy 2.5.4, scipy 1.18.1). Run from the repo root:
`python3 scripts/<runner>.py > logs/runner-cache/<runner>.txt`.
**Repo-policy status of the citation (SCIENCE_WORKFLOW §10, "Literature lemmas are rebuilt"):** BHM Theorem 1 is
used here as a cited theorem with its hypotheses checked; it has **not** been rebuilt as a library entry. Under the
repo's policy the citation is attribution only, so the gap ≥ 4 step stays an **open obligation (rebuild BHM Thm 1 /
Lemma 3.1 in the D = 3 commuting-projector, product-ground-state case)** until that rebuild exists. The label [R-cit]
below means "rigorous given the published theorem", not "repo-established".

Status legend used below: **[R]** rigorous, complete proof given here; **[R-cit]** rigorous given a cited,
published theorem whose hypotheses are checked here; **[N]** numerical evidence only; **[C]** conjecture.

---

## 0. Provenance: what is MDTN's and what is ours

*From the MDTN paper* (Chandrasekharan, Siew, Bhattacharya, arXiv:2502.14175, Phys. Rev. D 111, 114502 (2025)):
the Peter–Weyl link basis; the gauge-invariant basis labelled by link irreps λ and site singlet indices α;
the ASQR truncation (SU(2): irreps {1, 2}; SU(3): {1, 3, 3̄}); the Hamiltonian
H = Σ_ℓ E_ℓ − δ Σ_P (U_P + U_P†) with E_ℓ = 1 − δ_{λ_ℓ,1}; the sign-free / classical (dimer–monomer) mapping and
the d = 1 chain numerics. The paper makes **no** claim about a d ≥ 2 spectral gap, infinite volume, or a continuum limit.

*Ours (new here):* Lemma 1's use as a support/girth statement, Lemma 2 (Gauss projector structure as an
Admissibility-type local rule), the Lift Proposition, the Main Theorem (volume-uniform physical gap), the
canonical-singlet Z2 reduction used for numerics, and all numbers in §5.

---

## 1. Setting and notation

* Λ_L = (Z_L)^3, L ≥ 4, periodic; links ℓ = (x, μ); plaquettes P; star(s) = the 6 links at site s.
* Gauge group G = SU(2) or SU(3). Truncated link space H_ℓ = ⊕_{λ∈𝓡} V_λ ⊗ V_λ* with
  𝓡 = {1, 2} (SU(2), dim H_ℓ = 1 + 4 = 5) or 𝓡 = {1, 3, 3̄} (SU(3), dim H_ℓ = 1 + 9 + 9 = 19).
  Equivalently, Kogut–Susskind truncated at j_max = 1/2 for SU(2).
* H = ⊗_ℓ H_ℓ. The gauge transformation at s, W_s(g), acts by the left regular action on links leaving s and the
  right action on links entering s; W_s(g) = ⊗_{ℓ∈star(s)} (one-link unitary), so every gauge transformation is a
  product over links of one-link unitaries.
* H_phys = {ψ : W_s(g)ψ = ψ ∀ s, g} (Gauss law, no static charges).
* n_ℓ = 1 − |0⟩⟨0|_ℓ, the projector onto nontrivial irreps on ℓ (MDTN's E_ℓ). N = Σ_ℓ n_ℓ.
* E_k = eigenspace N = k (exactly k links carry a nontrivial irrep).

## 2. Lemma 1 (Gauss support / girth) — **[R]**

**Statement.** (a) For SU(2), dim Inv(2^{⊗k}) = Catalan C_{k/2} for k even and 0 for k odd.
(b) For any compact G and any nontrivial irrep λ, Inv(V_λ) = 0. Consequently, if ψ ∈ H_phys ∩ E_k with k ≥ 1, then
every basis component of ψ in the irrep basis has excited-link set S with every vertex of S of degree ≥ 2 in S.
(c) On Λ_L with L ≥ 4 every such S contains a cycle, every cycle has length ≥ 4, hence
**H_phys ∩ E_k = 0 for k = 1, 2, 3**, and H_phys ∩ E_0 = C|0⟩.

**Assumptions.** Setting §1. No dynamics is used.

**Proof.** (a) Standard: 2^{⊗k} = ⊕_j m_j V_j with m_0 given by the ballot numbers; for k = 2m one gets C_m.
(Checked numerically by Weyl integration for k ≤ 6: 1, 0, 1, 0, 2, 0, 5 — `logs/runner-cache/mdtn_ed_part1_reps_and_plaquette_2026_10_31.txt` (a).)
(b) Schur. Decompose ψ in the orthogonal sum over irrep assignments λ = (λ_ℓ). Gauge transformations preserve each
summand, so each component is itself invariant. In a summand, the action of W_s(g) on H is the action on
⊗_{ℓ∋s} V_{λ_ℓ}^{(end)} tensored with identity; invariance forces the component into Inv(⊗_{ℓ∋s} V_{λ_ℓ}^{(end)}) ⊗ (rest).
If exactly one link at s is excited, this is Inv(V_λ) ⊗ … = 0. So deg_S(s) ∈ {0} ∪ [2, 6].
(c) A finite nonempty graph with min degree ≥ 2 contains a cycle. In Λ_L, L ≥ 4, there are no 3-cycles (a closed
walk of 3 unit steps would need a coordinate to change by a nonzero multiple of L in ≤ 3 steps), and no 2-cycles
(simple graph for L ≥ 3). Hence |S| ≥ 4. For E_0: the only state is |0⟩ = ⊗|0⟩_ℓ, which is invariant. ∎

**Remarks.** For SU(3) ASQR, triality makes S a Z3 1-cycle; multiplicities Inv(3^{⊗a} ⊗ 3̄^{⊗b}) for a + b ≤ 6 are
listed in `logs/runner-cache/mdtn_ed_part1_reps_and_plaquette_2026_10_31.txt` (e.g. (1,1): 1; (3,0): 1; (2,2): 2; (3,3): 6; (6,0): 5). The binary analogue
(Z2 cycles) is the repo's COVARIANT_NN_SUPPORT_RULES … GLUED_SUPPORT note (minimal supports = cycles of length 4, 6, 8).

## 3. Lemma 2 (Gauss projector as a local covariant commuting rule) — **[R]**

**Statement.** Let P_s = ∫_G dg W_s(g) (Haar). Then (i) each P_s is an orthogonal projector supported on star(s);
(ii) [P_s, P_{s'}] = 0 for all s, s'; (iii) P_phys := Π_s P_s is the orthogonal projector onto H_phys;
(iv) the family {P_s} is covariant under lattice translations and proper cubic rotations;
(v) any operator O with [O, W_s(g)] = 0 ∀ s, g commutes with P_phys, and then e^{−τH}, τ ≥ 0, maps H_phys into itself
and is a positive operator there if H is self-adjoint and gauge invariant.

**Proof.** (i) Haar averaging of a unitary representation gives the projector onto its invariants. (ii) W_s(g) and
W_{s'}(h) commute: on a shared link they are a left and a right regular action, which commute; elsewhere they act on
disjoint factors. Averages of commuting families commute. (iii) The P_s commute, so Π P_s projects onto ∩ ranges = H_phys.
(iv) Lattice symmetries permute sites and links and intertwine the W's. (v) O commutes with every W_s(g), hence with
their averages. e^{−τH} = (e^{−τH/2})² ≥ 0 by the spectral theorem. ∎

**Remarks (axiom reading, a bridge, not a derivation).** {P_s} is a single nearest-neighbour, covariant, commuting
local rule — the shape Admissibility allows. Reading "Record locks Gauss" as "records read the gauge-invariant MDTN
labels (λ_ℓ, α_s), never a fixed occupation basis" is a *named bridge* B_G. It is not derived from Record; the repo's
A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS note shows the occupation-pattern reading fails. Only
time-direction positivity of the transfer matrix is claimed; spatial reflection positivity is **not** claimed.

## 4. Lift Proposition and Main Theorem

### 4.1 Lift Proposition — **[R]** (elementary; auditor should check against the paper's exact c-coefficient definition)

**Statement.** Let U_P be an MDTN plaquette operator, defined on the gauge-invariant basis of H_phys, that changes
only the irrep labels on the 4 links of P and the singlet labels α at the 4 corners K = ∂₀P, with matrix elements
that depend only on the labels on R = ∪_{s∈K} star(s). Then there is an operator Õ_P on H, supported on R, commuting
with every W_s(g), with Õ_P|_{H_phys} = U_P and ‖Õ_P‖ = ‖U_P^{loc}‖ (the norm of the finite local block).

**Proof.** Write H_R = ⊕_{λ_R} ⊗_{ℓ∈R} (V_{λ_ℓ} ⊗ V_{λ_ℓ}*). Two distinct corners of a plaquette in Z^3 are adjacent
only through edges of P (diagonals are not lattice links), so every link of R \ P has exactly one end in K and one
"outer" end outside K. Let Π_K = Π_{s∈K} P_s (a projector on H_R). Then
Π_K H_R ≅ ⊕_{λ_R} [⊗_{s∈K} Inv_s(λ_R)] ⊗ [⊗_{ℓ∈R\P} V^{(outer end)}_{λ_ℓ}].
Define Õ_P := (U_P^{loc} ⊗ 1_outer) on Π_K H_R and 0 on (1 − Π_K) H_R, tensored with 1 off R. It commutes with
W_s(g) for s ∈ K (it is supported on, and maps into, the invariant subspace, where W_s(g) = 1); for s ∉ K adjacent to
R it commutes because W_s(g) acts only on outer-end factors, where Õ_P is the identity, and W_s(g) commutes with Π_K;
for all other s, supports are disjoint. A global gauge-invariant basis vector is the contraction of site intertwiners;
Õ_P changes only the corner intertwiners and P-link labels exactly as U_P does, so Õ_P|_{H_phys} = U_P. Norm: the outer
factor is the identity and the complement block is 0. ∎

### 4.2 Main Theorem — **[R-cit]** (Bravyi–Hastings–Michalakis, J. Math. Phys. 51, 093512 (2010), arXiv:1001.0344, Thm 1 + J_k paragraph, §1.1; band identification via §4 proof / Lemma 3.1; D = 3 via BHM's stated generalization; audit items below)

**Statement.** Fix G ∈ {SU(2), SU(3)} with the truncation of §1 and a range r ≥ 1. Consider
  H(δ) = Σ_ℓ n_ℓ + δ Σ_P O_P   on   H = ⊗_ℓ H_ℓ over Λ_L,
where each O_P is self-adjoint, commutes with all W_s(g), is supported within distance r of P, and ‖O_P‖ ≤ 1.
There are constants δ₀ > 0, c₁ > 0, L₀ depending only on (G, r) — **not on L** — such that for |δ| ≤ δ₀ and L ≥ L₀:
1. H(δ)|_{H_phys} has a unique ground state Ω_L, and Ω_L is also the unique ground state of H(δ) on all of H;
2. the physical gap obeys  gap_phys(L) ≥ 4(1 − c₁|δ|) − 2ε_L  with ε_L → 0 as L → ∞
   (BHM: ε_L ≤ poly(L) e^{−c₂ L^{3/8}});
3. the full-space gap obeys gap_full(L) ≥ (1 − c₁|δ|) − 2ε_L ≥ 1/2 (for δ₀, L₀ suitably chosen).

**Covers:** (a) MDTN's H = Σ E_ℓ − δ_MDTN Σ (U_P + U_P†) via the Lift Proposition, with δ = 2δ_MDTN max‖U_P^{loc}‖;
(b) Kogut–Susskind SU(2) truncated at j_max = 1/2:
H_KS = (g²/2)ΣE² − (1/(2g²))Σ(TrŨ_P + h.c.) = (3g²/8)[Σ n_ℓ − (8/(3g⁴)) Σ TrŨ_P],
because E² = 3/4 on the doublet, TrŨ_P is Hermitian for SU(2) and ‖TrŨ_P‖ = 1 (computed exactly on the full
625-dim plaquette space, `logs/runner-cache/mdtn_ed_part1_reps_and_plaquette_2026_10_31.txt` (d)). So δ = 8/(3g⁴), and for g ≥ g₀ := (8/(3δ₀))^{1/4}:
  **gap_phys ≥ (3g²/2)(1 − (8c₁)/(3g⁴)) − (3g²/4)ε_L**, uniformly in L.


> **Audit items (for an independent reviewer)**
> 1. *BHM TQO-2 for a product ground state vs the verbatim definition.* **Checked here** (Step 1): BHM §2.2's kernel
>    condition holds trivially (both reduced states ∝ |0…0⟩⟨0…0|_A), and BHM §1.1 state explicitly that a
>    non-degenerate ground state satisfies TQO-1 automatically. Reviewer: confirm the coarse-graining into BHM sites
>    (dimension 5³ or 19³) does not alter the "square A / neighbourhood B" bookkeeping.
> 2. *Lift Proposition vs MDTN's exact coefficient definition.* **Open.** §4.1 assumes MDTN's U_P acts on the
>    gauge-invariant basis with matrix elements depending only on labels in R = ∪_{s∈∂P} star(s). This is how we read
>    arXiv:2502.14175 (Eq. 8 and the c-coefficient construction) but it has not been checked line by line against the
>    paper's definition of the c-coefficients. Kogut–Susskind (§4.2(b)) does not need the Lift Proposition.
> 3. *Does BHM Thm 1 give the multi-band statement?* **Yes for the statement; band identification uses the proof.**
>    Theorem 1 is stated for all k in spec H₀, with the I_k widths quoted in Step 2, and the J_k paragraph gives the
>    separation of bands 0..k for J < J_k = 1/(c₁(4k + 2)). Because of the "overall energy shift", attaching the
>    E_k-descendants to I_k uses the proof structure (relative boundedness, Lemma 3.1, eq. 4.29), as written in
>    Step 2. Further point to audit: BHM write the proof for D = 2 and say (§2.1) "A generalization to an arbitrary D
>    is straightforward"; our application is D = 3. Theorem 1's constants are stated to depend on D.

**Assumptions.** (A1) Finite truncation (dim H_ℓ = 5 or 19). (A2) Hamiltonian supplied (bridge B_H — not an axiom
output). (A3) Periodic L³ torus (BHM's setting). (A4) Gauge-invariant, finite-range, bounded plaquette terms.

**Proof.**
*Step 1 (BHM hypotheses).* Coarse-grain each site s with its 3 forward links into one "BHM site" of dimension
5³ or 19³. H₀ := Σ_ℓ n_ℓ is a sum of commuting projectors, each supported in one BHM site; it is frustration-free with
unique ground state |0⟩ = ⊗_ℓ|0⟩_ℓ (a product state) and integer spectrum {0, 1, 2, …}. TQO-1 holds because the
ground-space projector has rank one (P₀ O P₀ = ⟨0|O|0⟩ P₀ for every O); BHM say so verbatim (§1.1): "all our results
apply also to the special case when H0 has non-degenerate ground state. In this case TQO-1 is automatically satisfied
since P is a one-dimensional subspace and thus condition TQO-2 alone guarantees the gap stability." TQO-2 (BHM §2.2,
checked against the verbatim definition): for a square A and B ⊃ A the square containing A and its nearest neighbours,
ρ_A = Tr_{A^c} P and ρ_A^{(B)} = Tr_{A^c} P_B must have the same kernel, where P_B is the ground-space projector of the
terms of H₀ supported in B. Here P_B = (⊗_{ℓ⊂B}|0⟩⟨0|_ℓ) ⊗ 1_{B^c}, so ρ_A^{(B)} ∝ ⊗_{ℓ⊂A}|0⟩⟨0|_ℓ ∝ ρ_A: the kernels
coincide (both are the orthogonal complement of |0…0⟩_A). The perturbation V = δ Σ_P O_P is a sum of terms of
norm ≤ |δ| supported on balls of radius ≤ r + 1, so it satisfies BHM's decay condition ‖V_{r,A}‖ ≤ J e^{−μr} with
J = C(r)|δ| for any fixed μ > 0.

*Step 2 (bands; BHM Thm 1, verbatim).* BHM §1.1, Theorem 1: "Suppose H0 obeys TQO-1,2. Then there exist constants
J0, c1, c2 > 0 depending only on µ and the spatial dimension D such that for all J ≤ J0 the spectrum of H0 + V is
contained (up to an overall energy shift) in the union of intervals ∪_{k≥0} I_k, where k runs over the spectrum of H0
and I_k = {λ ∈ R : k(1 − c1J) − δ ≤ λ ≤ k(1 + c1J) + δ}, and δ = poly(L) exp(−c2 L^{3/8})." and immediately after:
"the perturbation V changes positive eigenvalues of H0 at most by a constant factor 1 ± c1J (neglecting the
exponentially small correction δ) while the smallest eigenvalue k = 0 is transformed into a band I0 of exponentially
small width 2δ … for any fixed k the band Ik is separated from all other bands Im, m ≠ k, by a gap at least 1/2
provided that J < Jk, where Jk = 1/(c1(4k + 2)). Thus the bands originating from eigenvalues 0, 1, . . . , k of H0 are
separated from each other and from the rest of the spectrum by a gap at least 1/2 provided that J < Jk."
Hypotheses are on H₀'s ground space only (TQO-1,2); there is no per-band hypothesis, the bands are those of H₀'s
integer spectrum, and the widths are exactly the I_k above (BHM's δ is our ε_L). Apply this to H(sδ), s ∈ [0, 1]
(the same J bounds sV), with |δ| ≤ δ₀ chosen so that J < J₃ = 1/(14c₁) and J ≤ J₀, and L ≥ L₀ so that ε_L < 1/8.
Then I₀, …, I₃ are pairwise separated and separated from ∪_{k≥4} I_k (infimum 4(1 − c₁J) − ε_L) by gaps ≥ 1/2.
*Band identification.* Theorem 1 states containment "up to an overall energy shift" λ(s); that the eigenvalues
descending from E_k (k = 0..3) sit in λ(s) + I_k (and not in some other band) follows from the proof (BHM §4.4, end of
proof of Thm 1): U(H₀ + V)U† = H₀ + W + V(n) + E(n) + λ(n)·1 with W relatively bounded by H₀ with constant b = O(J) < 1,
every local term of W having zero restriction on P, and ‖V(n)‖, ‖E(n)‖ ≤ poly(L) e^{−cL} (BHM eq. 4.29). For H₀ + tW,
t ∈ [0, 1], Lemma 3.1 (verbatim: "Suppose W is relatively bounded by H0. Then the spectrum of H0 + W is contained in the
union of intervals [λ0(1 − b), λ0(1 + b)] where λ0 runs over the spectrum of H0") puts the spectrum in disjoint
intervals k(1 ± tb); by norm-continuity of the spectral projectors in t the spectral projector on k(1 ± b) has rank
dim E_k at t = 1. Weyl's inequality then moves each eigenvalue by ≤ ‖V(n)‖ + ‖E(n)‖. Hence, for each s, H(sδ) has exactly
dim E_k eigenvalues (with multiplicity) in λ(s) + I_k for k = 0..3, the lowest being the single eigenvalue in λ(s) + I₀.
(This band-identification step uses BHM's proof, not only the statement of Theorem 1: see Audit item 3.)
*Step 3 (rank continuity in the physical sector).* Let Q_k(s) (k = 0..3) be the Riesz projector of H(sδ) onto λ(s) + I_k (equivalently, onto the eigenvalues with
indices in the k-th block of sizes dim E₀, …, dim E₃ counted from the bottom; this index description shows continuity in s
without reference to λ(s))
(contours in the uniform gaps), norm-continuous in s. Every term of H(sδ) commutes with every W_s(g) (n_ℓ by
construction, O_P by hypothesis), so H(sδ), Q_k(s) and P_phys commute (Lemma 2(v)). Therefore P_phys Q_k(s) is a
norm-continuous family of orthogonal projectors, hence of constant rank. At s = 0, Q_k(0) is the projector onto E_k, so
rank(P_phys Q_k(1)) = dim(H_phys ∩ E_k) = 1, 0, 0, 0 for k = 0, 1, 2, 3 by Lemma 1(c). Likewise rank Q₀(1) = dim E₀ = 1.
*Step 4 (conclusion).* In H_phys, H(δ) has exactly one eigenvalue in λ + I₀, none in λ + (I₁ ∪ I₂ ∪ I₃), all others ≥
λ + 4(1 − c₁J) − ε_L; the gap is ≥ 4(1 − c₁J) − 2ε_L. The unique full-space ground state lies in Q₀(1)H, which has rank one
and equals P_phys Q₀(1)H, so it is gauge invariant. The full-space gap is ≥ (1 − c₁J) − 2ε_L. Absorb C(r) into c₁. ∎

**Corollary (exponential clustering) — [R-cit].** With the uniform full-space gap ≥ 1/2 and the finite-range
interaction, the Lieb–Robinson exponential-clustering theorem (Nachtergaele–Sims, CMP 265, 119 (2006),
arXiv:math-ph/0506030; Hastings–Koma, CMP 265, 781 (2006), arXiv:math-ph/0507008) gives, for observables A, B
supported on X, Y: |⟨AB⟩ − ⟨A⟩⟨B⟩| ≤ C‖A‖‖B‖ min(|X|,|Y|) e^{−dist(X,Y)/ξ}, with C, ξ independent of L.
Applied to gauge-invariant A, B this is the Hamiltonian-side counterpart of the repo's
CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE route. (Using only the full-space gap gives a worse ξ than the physical gap would;
an improved ξ tied to gap_phys is **[C]**.)

**Remarks.**
* The Main Theorem's mechanism is exactly the Gauss/girth statement: charged states fill bands 1–3; the physical sector
  starts at 4 (the shortest closed flux loop). Without Lemma 1 one gets only the full-space gap ≈ 1.
* The constants δ₀, c₁ are **not explicit** (BHM's are not). No numerical value of δ₀ is claimed.
* Alternative citation for Step 2 (classical H₀ with unique ground state): Yarotsky, CMP 261, 799 (2006),
  arXiv:math-ph/0412040 (verified to exist; its hypotheses were not checked line-by-line here, so it is not used).
* The existing repo NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP note is a Euclidean coefficient-transfer statement on a
  source sector; this result is Hamiltonian, full-lattice, uniform in L, and truncated. They are complementary.

## 5. Numerical checks (exact diagonalization) — **[N]**

All values are copied from the runner-cache logs named in the header (run 2026-10-31).

**5.1 Gauss multiplicities.** SU(2): [1, 0, 1, 0, 2, 0, 5] for k = 0..6 = Catalan (Lemma 1a). SU(3): table in output (a).

**5.2 KS SU(2), single plaquette, full truncated space (4 links × C⁵ = 625 states, j_max = 1/2).**
‖[G_s^a, TrŨ_P]‖ = 0 exactly; dim H_phys = 2 (N = 0 and N = 4); ‖TrŨ_P‖ = 1.

| g² | full-space lowest excitations | physical gap (ED) | closed form √((3g²/2)² + 4/g⁴) |
|---|---|---|---|
| 4.0 | 1.5052 (charged, ×≥5) | 6.02080 | 6.02080 |
| 2.0 | 0.79057 (charged) | 3.16228 | 3.16228 |
| 1.0 | 0.625 (charged) | 2.50000 | 2.50000 |

(Charged levels are reported relative to E₀; e.g. g² = 4: 1.4948 − (−0.0104).) The band picture holds: the
lowest charged level sits near 3g²/8 (one excited link), the physical gap near 4 × 3g²/8 = 3g²/2.

**5.3 KS SU(2) single plaquette, gauge-invariant chain, gap vs g² for j_max = 1/2, 1, 3/2, 2, 10.**

| g² | j_max=1/2 | 1 | 3/2 | 2 | 10 | 3g²/2 |
|---|---|---|---|---|---|---|
| 4.00 | 6.02080 | 6.01456 | 6.01456 | 6.01456 | 6.01456 | 6.000 |
| 2.00 | 3.16228 | 3.11407 | 3.11386 | 3.11386 | 3.11386 | 3.000 |
| 1.50 | 2.61539 | 2.50856 | 2.50711 | 2.50711 | 2.50711 | 2.250 |
| 1.00 | 2.50000 | 2.21700 | 2.19685 | 2.19649 | 2.19649 | 1.500 |
| 0.75 | 2.89426 | 2.38986 | 2.28758 | 2.28113 | 2.28099 | 1.125 |
| 0.50 | 4.06971 | 3.08645 | 2.60931 | 2.49191 | 2.47874 | 0.750 |
| 0.30 | 6.68184 | 4.82410 | 3.59115 | 2.95096 | 2.62911 | 0.450 |

Reading: at strong coupling (g² ≳ 2) the truncation is harmless (j_max = 1/2 within 0.1% of j_max = 10 at g² = 4;
within 1.6% at g² = 2) and the gap tracks 3g²/2. At weak coupling the j_max = 1/2 gap is a **truncation artefact**
(it grows like 2/g² instead of converging); j_max must grow as g → 0. A single plaquette is quantum mechanics, not a
field theory: these numbers say nothing about a continuum gap.

**5.4 MDTN ASQR SU(2), canonical-singlet sector, open 3D boxes (δ = coefficient of X_P; δ = 2δ_MDTN).**
On this sector the model is exactly H = Σ n_ℓ − δ Σ_P X_P on the Z2 cycle space (X_P flips the four links of P).
Second-order degenerate PT (ours): gap ≈ 4 + δ²/2 − (δ²/4) λ_max(D + A), D, A = plaquette edge-adjacency degree /
adjacency matrices. On infinite Z³: λ_max = 24, so gap ≈ 4 − (11/2)δ² + O(δ⁴) **[C: series not proved to converge
here; the Main Theorem gives only gap ≥ 4 − O(δ)]**.

| box | phys dim | λ_max | δ=0.1 ED / PT2 | δ=0.2 ED / PT2 | δ=0.3 ED / PT2 | δ=0.5 ED / PT2 |
|---|---|---|---|---|---|---|
| 1×1×1 | 2⁵ | 8.000 | 3.98395 / 3.98500 | 3.92444 / 3.94000 | 3.79931 / 3.86500 | 3.37933 / 3.62500 |
| 1×1×2 | 2⁹ | 11.123 | 3.97611 / 3.97719 | 3.89263 / 3.90877 | 3.72648 / 3.79473 | 3.17757 / 3.42981 |
| 1×1×3 | 2¹³ | 12.101 | 3.97355 / 3.97475 | 3.88119 / 3.89900 | 3.69794 / 3.77274 | 3.08675 / 3.36872 |
| 2×2×1 | 2¹⁶ | 14.142 | 3.96846 / 3.96964 | 3.86088 / 3.87858 | 3.65211 / 3.72680 | 2.95605 / 3.24110 |
| 1×1×4 | 2¹⁷ | 12.514 | 3.97246 / 3.97372 | 3.87631 / 3.89486 | 3.68554 / 3.76344 | 3.04517 / 3.34288 |

At δ = 0.05 ED and PT2 agree to < 1×10⁻⁴ on every box (O(δ⁴) residual), validating the PT formula. The gap at fixed
δ depends weakly on box shape (it is lowest on 2×2×1, which has the most plaquette neighbours, and is
non-monotone along 1×1×N: 1×1×4 lies above 1×1×3); boxes are open,
not BHM tori, and too small to test L-uniformity — numerics are illustrative only. Full-space single cube (2¹²
states): lowest excitations are charged at 1.000, 0.995, 0.955 (δ = 0, 0.1, 0.3); the ground state is physical; the
physical gap is 4.000, 3.984, 3.799 — the band structure used in the proof.

## 6. Exact distance to the Clay problem

What this note proves is a **fixed-lattice, truncated, strong-coupling, 3+1D Hamiltonian** gap on tori, uniform in L.
The Clay problem needs, and this note supplies **none** of:
1. Removal of the truncation (j_max → ∞ / full L²(G) link space). The theorem uses dim H_ℓ < ∞ (BHM needs finite
   local dimension; the KS electric term is unbounded otherwise).
2. Weak coupling. The continuum limit is g → 0 (asymptotic freedom); the theorem holds for g ≥ g₀ with g₀ unknown,
   i.e. the opposite regime. Strong-coupling gaps are classical lore (Osterwalder–Seiler 1978 for the Euclidean Wilson
   action); this note adds only the truncated-Hamiltonian, volume-uniform, Gauss-sector form.
3. The absence of a phase transition between g₀ and g → 0 (open for SU(2)/SU(3) in 4D).
4. A continuum limit a → 0 with renormalized physical mass m_phys = gap/a > 0, and construction of a QFT on R⁴ obeying
   Wightman/OS axioms (including OS RP in all directions and Euclidean invariance, neither of which is shown here).
5. The gap here is in lattice units at fixed a; it diverges in physical units as a → 0 at fixed g. That is the wrong
   scaling for a continuum statement.
