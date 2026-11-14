---
claim_id: qubit_lattice_gauge_mdtn_embedding_outline_note_2026-10-31
claim_type: bounded_theorem   # only for the headline lemma (§4); everything else is outline / conditional
claim_scope: >
  Outline of an embedding of qubit-regularized SU(2)/SU(3) lattice gauge theory in the
  Monomer-Dimer Tensor-Network (MDTN) basis into the Lattice / Qubit / Admissibility / Record
  framework, with one proved fixed-lattice result (truncated strong-coupling physical gap, uniform
  in volume). This is not the Clay Yang-Mills mass gap problem.
upstream_dependencies: ["minimal_axioms"]
named_bridges: ["B_H: supplied Hamiltonian / transfer operator", "B_G: records read gauge-invariant MDTN labels",
                "B_E: link register encoded in blocks of site qubits"]
companion: docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md
runner: scripts/mdtn_ed_part1_reps_and_plaquette_2026_10_31.py, scripts/mdtn_ed_part2_su2_boxes_2026_10_31.py, scripts/mdtn_ed_part3_ks_gauge_invariant_2026_10_31.py
status: proposed outline (unaudited); status authority is the independent audit lane only
---

# Qubit-lattice embedding of MDTN gauge theory: construction, axiom map, one proved gap lemma, and the continuum programme

**Date:** 2026-10-31
**Type:** outline + one bounded_theorem (proposed; unaudited)
**Status authority:** independent audit lane only.
**Scope sentence:** this is not the Clay Yang–Mills mass gap problem.
**Relation to PR #10132 (hard-constraint / Balaban route):** independent of, and complementary to. Nothing here is an
input to that route's critical path, and nothing there is used here (the interface commentary is in a separate firewalled file, see §8).

Status legend: **[MDTN]** established in arXiv:2502.14175; **[R]** proved here; **[R-cit]** proved here given a cited
published theorem; **[N]** numerical only; **[P]** proposal (definition / design choice, nothing to prove);
**[C]** conjecture; **[O]** open.

---

## 1. Abstract and scope

Chandrasekharan, Siew and Bhattacharya (MDTN; arXiv:2502.14175, PRD 111, 114502 (2025)) give a gauge-invariant
orthonormal basis for SU(N) lattice gauge theory built from dimer tensors on links and monomer tensors on sites,
a finite "ASQR" truncation, a family of sign-free plaquette Hamiltonians, and classical lattice gauge models whose
finite-temperature transitions they match to Ising / 3-state Potts universality. **[MDTN]**

This note (i) proposes how that construction sits on the repo's four axioms, with every non-axiom ingredient named as a
bridge; (ii) proves one rigorous result: on the 3-torus, for the ASQR (= KS j_max = 1/2) truncation and any bounded,
local, gauge-invariant plaquette term at small coupling δ, the Gauss-sector Hamiltonian has a unique ground state and a
gap ≥ 4(1 − c₁δ) − o(1), uniform in L (§4, full proof in the companion LEMMA file); (iii) checks it by exact
diagonalisation; (iv) lists exactly what remains between this and a continuum Yang–Mills mass gap. It does **not**
claim a continuum limit, weak-coupling control, or anything about the Clay problem beyond §7's checklist.

## 2. What the MDTN paper establishes (verified against the arXiv text)

| Item | Content | Tag |
|---|---|---|
| Link space | Peter–Weyl: H_ℓ = ⊕_λ V_λ ⊗ V_λ*; dimers on links labelled by λ | [MDTN] |
| Gauge-invariant basis | site monomer tensors labelled by singlet index α_s, D(H^g_s) = dim of the invariant space at s | [MDTN] |
| ASQR truncation | SU(2): λ ∈ {1, 2}; SU(3): λ ∈ {1, 3, 3̄} | [MDTN] |
| Hamiltonian (their Eq. 8) | H = Σ_ℓ E_ℓ − δ Σ_P (U_P + U_P†), E_ℓ = 1 − δ_{λ_ℓ,1}; U_P built from c-coefficients | [MDTN] |
| Sign-freedom | if δ ≥ 0 and c real, ≥ 0, all off-diagonal terms are ≤ 0 (QMC-amenable) | [MDTN] |
| Classical LGTs | honeycomb (d = 2) and diamond (d = 3) models; finite-T confinement–deconfinement transitions: d = 2 consistent with 2D Ising (SU(2)) / 3-state Potts (SU(3)); d = 3 SU(2) consistent with 3D Ising (β_c = 1.04530(1)); d = 3 SU(3) first order | [MDTN] |
| d = 1 chain | SU(2) string-tension-type numbers σ = 0.6805, 0.3608, 0.158, 0.055 at δ = 0.5, 1, 2, 5 | [MDTN] |
| Continuum | explicitly open; the authors write it "would indeed be surprising" if the infinite-dimensional continuum link space were recovered by the weak-coupling limit of a strictly finite-dimensional qubit-regularized theory | [MDTN] |

No arXiv discrepancy was found: 2502.14175 resolves to this paper, and the journal reference matches.

## 3. Discrete construction (proposed embedding) [P unless tagged]

**3.1 Link encoding.** Each Z³ link ℓ carries H_ℓ^{ASQR}: dim 5 (SU(2)) or 19 (SU(3)). Equivalent gauge-invariant
coordinates (MDTN): a link label λ_ℓ ∈ {1, 2} (1 bit) or {1, 3, 3̄} (3 values) plus site singlet labels α_s.

**3.2 Truncation.** The ASQR cut is gauge invariant (the projector onto ⊕_{λ∈𝓡} commutes with left/right actions),
so truncated multiplication operators Ũ^{ab} = Π U^{ab} Π are gauge covariant and the truncated KS plaquette TrŨ_P is
gauge invariant. **[R]** (one-line proof; checked: ‖[G, TrŨ_P]‖ = 0 on the 625-dim plaquette space, §5.)

**3.3 Gauss law.** P_s = ∫dg W_s(g), P_phys = Π_s P_s: commuting, local (star(s)), covariant projectors. **[R]** (Lemma 2).
Singlet multiplicities: SU(2) dim Inv(2^{⊗k}) = Catalan C_{k/2} (1, 1, 2, 5 for k = 0, 2, 4, 6); SU(3) triality ⇒ Z3
1-cycle constraint. **[R]** (Lemma 1; numerically checked.)

**3.4 Electric and plaquette terms.** E_ℓ = n_ℓ (MDTN) or (g²/2)C₂(λ_ℓ) (KS; = (3g²/8) n_ℓ for SU(2) ASQR).
Plaquette: MDTN U_P (any c) or truncated TrŨ_P. Lift Proposition **[R]**: an MDTN U_P whose coefficients depend only on
labels in the corners' stars extends to a gauge-invariant local operator on ⊗_ℓ H_ℓ with the same norm.

**3.5 Site register M₂(C) / Cl(3).** The Qubit axiom gives one qubit per site. A link register therefore needs a
block encoding (bridge B_E): ⌈log₂ 5⌉ = 3 qubits per SU(2) link, ⌈log₂ 19⌉ = 5 per SU(3) link, with unused levels
(3 resp. 13 per link) removed by an extra local penalty. This is consistent with the repo's DYNAMICS_CLAUSE … SU2 NEEDS
TWO, SU3 THREE note (a link with commuting nontrivial end actions needs ≥ 2N states: 4 resp. 6).

**3.6 Resource counts (simple ⌈log₂⌉ counting, ours).**

| Encoding | per link | per coarse site (3 forward links + site label) | qubit block per coarse site |
|---|---|---|---|
| SU(2) full truncated space | 3 | 9 | 3³ = 27 sites (18 spare) |
| SU(2) gauge-invariant (λ bit + α ≤ C₃ = 5) | 1 | 3 + 3 = 6 | 2³ = 8 sites |
| SU(3) full truncated space | 5 | 15 | 3³ = 27 sites |
| SU(3) gauge-invariant (λ ∈ 3 values + α ≤ 6) | 2 | 6 + 3 = 9 | 3³ = 27 sites (2³ = 8 too small) |

The SU(3) α bound uses the computed maximum dim Inv = 6 at degree 6, (a, b) = (3, 3). The gauge-invariant encodings
are not tensor-product local (the Gauss closure becomes a constraint on labels), which is exactly where Admissibility
(a nearest-neighbour rule) would carry the constraint. **Risk:** blocking breaks fine-lattice translation covariance
down to the block sublattice (Admissibility is stated covariantly on the fine lattice).

## 4. Headline result (full proof in `docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md`)

* **Lemma 1 (Gauss support / girth) [R].** Physical states with exactly k excited links vanish for k = 1, 2, 3 on
  (Z_L)³, L ≥ 4; the only k = 0 physical state is the electric vacuum.
* **Lemma 2 (Gauss projectors) [R].** The P_s commute, are local and covariant; gauge-invariant operators and e^{−τH}
  preserve H_phys; e^{−τH} ≥ 0 there.
* **Lift Proposition [R].** As in §3.4.
* **Main Theorem [R-cit, BHM 2010 Thm 1].** For H = Σ n_ℓ + δ Σ_P O_P with O_P gauge invariant, finite range,
  ‖O_P‖ ≤ 1, there are δ₀, c₁, L₀ independent of L with: unique (gauge-invariant) ground state; physical gap
  ≥ 4(1 − c₁|δ|) − 2ε_L, ε_L ≤ poly(L)e^{−c₂L^{3/8}}; full-space gap ≥ 1/2. For SU(2) KS at j_max = 1/2:
  δ = 8/(3g⁴) and gap_phys ≥ (3g²/2)(1 − 8c₁/(3g⁴)) − o(1). Proof idea: BHM bands for every s ∈ [0, 1] plus
  rank-continuity of P_phys·(Riesz projector), which transports the Gauss-sector content of bands 0–3 from δ = 0.
  BHM Thm 1 is stated for every band k ∈ spec H₀ with widths k(1 ± c₁J) ± δ_BHM and needs TQO only for the ground
  space (checked against the verbatim text; see the theorem note, Step 2). The identification "E_k-descendants sit in
  I_k" uses BHM's proof (§4.4, Lemma 3.1). Under the repo's §10 policy the BHM step is an open obligation until it is
  rebuilt as a library entry.
* **Corollary [R-cit].** Exponential clustering, uniform in L (Nachtergaele–Sims; Hastings–Koma).
* **What it is not:** constants not explicit; truncated; strong coupling; fixed lattice; no continuum (§7).

## 5. Numerical checks (exact diagonalisation) [N]

* Single SU(2) KS plaquette, full 625-dim j_max = 1/2 space: gauge invariance exact; dim H_phys = 2; the physical gap
  equals √((3g²/2)² + 4/g⁴) to 5 digits (6.02080, 3.16228, 2.50000 at g² = 4, 2, 1). Charged levels sit near 3g²/8,
  i.e. the band picture behind the proof.
* j_max = 1/2 → 10 single-plaquette scan: at g² = 4 all truncations agree within 0.1% (6.0208 vs 6.0146); at g² = 2
  within 1.6%; at g² = 0.3 the j_max = 1/2 gap (6.68) is a truncation artefact (converged 2.63). Truncation removal
  is essential at weak coupling.
* MDTN SU(2) canonical-singlet sector on open boxes up to 2¹⁷ states (1×1×4): gap(δ = 0) = 4; ED matches the
  second-order formula 4 + δ²/2 − (δ²/4)λ_max(D + A) to < 10⁻⁴ at δ = 0.05; gap at δ = 0.3 ranges 3.65–3.80 across
  boxes. Infinite-lattice PT2 prediction 4 − (11/2)δ² **[C beyond second order]**.
Full tables: LEMMA §5; logs: `logs/runner-cache/mdtn_ed_part1_reps_and_plaquette_2026_10_31.txt`, `logs/runner-cache/mdtn_ed_part2_su2_boxes_2026_10_31.txt`.

Gauge-invariant multi-plaquette KS ED (SU(2) 2×2, 3×2, cube; SU(3) 1×1, 2×1) with a second-order comparison is in theorem-note §5.5.

## 6. Axiom-mapping table

| Ingredient | Axiom or bridge | Lemma / status |
|---|---|---|
| Z³ sites, links, plaquettes, covariance | Lattice | — (axiom content) |
| Link Hilbert space H_ℓ^{ASQR} | Qubit + bridge B_E (block encoding) | §3.5 [P]; ≥ 2N-state floor: repo DYNAMICS note |
| Gauss projectors P_s as one covariant NN rule | Admissibility (shape only) | Lemma 2 [R] for the algebra; identification [P] |
| "Records lock Gauss": readable content = (λ_ℓ, α_s) | Record + bridge B_G | [P]; occupation-pattern reading refuted by repo note A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS |
| Singlet multiplicities / girth | none (group theory) | Lemma 1 [R] |
| Hamiltonian H, transfer matrix e^{−τH} | bridge B_H (not axiom content: Admissibility "does not choose a Hamiltonian or transfer operator") | supplied |
| Time-direction positivity | follows from B_H + self-adjointness | Lemma 2(v) [R] |
| Spatial / Euclidean RP | not available here | [O] |
| Strong-coupling physical gap, uniform in L | B_H + truncation | Main Theorem [R-cit] |
| Exponential clustering | B_H | Corollary [R-cit] |
| Weights / Born rule / formation rate | outside axioms (memo: downstream supplier content) | not used |

## 7. Spectral gap via Record, and continuum lift

**7.1 Transfer matrix.** With B_H, T = e^{−aH} is positive and gauge invariant on H_phys [R]. A Euclidean MDTN
transfer matrix (Wilson-type) would need its own positivity proof; the repo's AXIOM_FIRST_REFLECTION_POSITIVITY note
shows that positivity can fail at one step and needs blocking (2-step) — expect the same care here. [O]

**7.2 Reflection positivity.** Time-direction: from positivity of T [R]. Spatial RP for MDTN Hamiltonians with general
c: [O]; plausible for KS-type terms (they come from a Wilson action) [C].

**7.3 Clustering.** Strong coupling: exponential clustering [R-cit]. Weak coupling: [O].

**7.4 Provable now vs open.**
Provable now (done): physical gap + clustering at strong coupling, truncated, uniform in L.
Plausible next [C]: (a) explicit δ₀ via a cluster/polymer expansion around the product vacuum (Kennedy–Tasaki /
Yarotsky-style), giving numbers instead of BHM constants; (b) the same theorem for any finite truncation
j_max (still strong coupling; the band gap becomes the lowest closed-loop electric energy); (c) SU(3) numerics.
Open [O]: anything at weak coupling.

**7.5 Continuum lift — checklist.**
1. *Critical tuning.* Find a line of couplings along which correlation length ξ/a → ∞. For KS that is g → 0
   (asymptotic freedom). For MDTN with finite truncation, no such point with YM universality is known; the paper's
   transitions are finite-T deconfinement transitions (Ising/Potts universality or first order, Svetitsky–Yaffe-type),
   not the YM UV fixed point (our reading; the paper leaves the continuum question open). [O]
2. *Truncation removal.* j_max → ∞ jointly with g → 0 (needed by §5's numbers), or a mechanism by which a finite
   truncation flows to YM (the paper calls this surprising; [C], low prior).
3. *Uniformity.* Gap/a must stay ≥ m > 0 in physical units while a → 0: the opposite of what strong coupling gives.
4. *OS axioms* for the limiting Schwinger functions: OS0 regularity/temperedness, OS1 Euclidean invariance
   (hypercubic → O(4) restoration), OS2 reflection positivity, OS3 symmetry, OS4 clustering.
   Then OS reconstruction (Osterwalder–Schrader 1973/1975) yields Wightman fields, a Hilbert space and a Hamiltonian;
   the mass gap is spec H ∩ (0, m) = ∅.
5. *Non-triviality.* The limit must not be Gaussian (cf. PR #10132's NT1/NT2 discussion).
Status: items 1–5 all [O]; this note supplies only the fixed-lattice strong-coupling end.

## 8. Interface with the Balaban / hard-constraint route (removed)

An interface note was removed from this PR because writing it required reading both sides of PR #10132's firewall.
Nothing in this note depends on it.

## 9. Open questions and risks

1. Is the canonical-singlet reduction (SU(2) data only in multiplicities; dynamical sector = Z2 gauge theory) generic
   for sign-free MDTN Hamiltonians? If so, sign-free MDTN models may sit in Z2-like universality classes. [O]
2. Explicit δ₀ (cluster expansion). [O] SU(3) small-system ED now done: gap ≈ 4 − κ/2 (theorem note §5.5). [N]
3. Does any finite-truncation MDTN family have a quantum critical point with YM-like universality? [O; the paper is sceptical]
4. Bridge B_G: can Record content be the (λ, α) labels without importing a readout context the memo forbids? [O]
5. Block encoding vs fine-lattice covariance (§3.6 risk). [O]
6. Spatial RP for MDTN Hamiltonians with general c. [O]
7. Risk: overclaiming. The result is classical-lore-adjacent (strong-coupling gaps: Osterwalder–Seiler 1978, Euclidean);
   the novelty is narrow (truncated Hamiltonian, Gauss sector, uniform in L, via BHM).

## 10. PR placement and audit items

* **New draft PR**, not #10132 (that PR is a firewalled hard-route target; adding unrelated notes would muddy its
  obligation count, and its GOAL says "notes written are not progress").
* Files: `docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md` (theorem note);
  `docs/QUBIT_LATTICE_GAUGE_MDTN_EMBEDDING_OUTLINE_NOTE_2026-10-31.md` (this note);
  runners `scripts/mdtn_ed_part{1,2}_*_2026_10_31.py` with logs in `logs/runner-cache/`.
* Upstream dependency `minimal_axioms` only; bridges B_H, B_G, B_E named as conditionals.

> **Audit items**
> 1. *BHM TQO-2 for a product ground state vs the verbatim definition* — checked in the theorem note (Step 1): the
>    kernel condition of BHM §2.2 holds trivially; BHM §1.1 state that a non-degenerate ground state satisfies TQO-1
>    automatically.
> 2. *Lift Proposition vs MDTN's exact coefficient definition* — **open**; KS j_max = 1/2 does not need it.
> 3. *Does BHM Thm 1 give the multi-band statement?* — yes as stated (all k ∈ spec H₀, J_k = 1/(c₁(4k+2)));
>    attaching E_k-descendants to I_k under the "overall energy shift" uses BHM's proof (§4.4, Lemma 3.1). Also to
>    audit: BHM prove D = 2 and call the general-D case "straightforward"; we use D = 3.

## 11. References (each verified on arXiv / journal on 2026-10-31)

* S. Chandrasekharan, R. Siew, T. Bhattacharya, "Monomer-dimer tensor-network basis for qubit-regularized lattice gauge
  theories", arXiv:2502.14175; Phys. Rev. D 111, 114502 (2025).
* S. Bravyi, M. B. Hastings, S. Michalakis, "Topological quantum order: stability under local perturbations",
  J. Math. Phys. 51, 093512 (2010), arXiv:1001.0344.
* S. Michalakis, J. P. Zwolak, "Stability of frustration-free Hamiltonians", Commun. Math. Phys. 322, 277 (2013),
  arXiv:1109.1588.
* B. Nachtergaele, R. Sims, "Lieb–Robinson bounds and the exponential clustering theorem", Commun. Math. Phys. 265,
  119 (2006), arXiv:math-ph/0506030.
* M. B. Hastings, T. Koma, "Spectral gap and exponential decay of correlations", Commun. Math. Phys. 265, 781 (2006),
  arXiv:math-ph/0507008.
* D. A. Yarotsky, "Ground states in relatively bounded quantum perturbations of classical lattice systems",
  Commun. Math. Phys. 261, 799 (2006), arXiv:math-ph/0412040 (mentioned, not used).
* J. Kogut, L. Susskind, Phys. Rev. D 11, 395 (1975) (Hamiltonian lattice gauge theory).
* K. Osterwalder, E. Seiler, "Gauge field theories on a lattice", Ann. Phys. 110, 440 (1978) (no arXiv).
* K. Osterwalder, R. Schrader, Commun. Math. Phys. 31, 83 (1973); 42, 281 (1975) (no arXiv).
