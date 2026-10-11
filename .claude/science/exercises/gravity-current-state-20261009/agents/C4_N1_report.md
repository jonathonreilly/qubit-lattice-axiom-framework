# Lane RN2, probe N1: interacting matter that does not conserve particle number, d = 2, 3

**Provenance.** Worker: Claude Opus 5.5 (same family as the supervisor). Ran 20:23Z to about 20:45Z on 2026-10-11. Not refereed. No repository files were edited.

**Read in full first:** `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md "C4 tenth wave" / "Lane RN2"; `C4_M1_report.md` + `C4_M1_referee*.md`; `C4_B1_report.md` + `C4_B1_referee.md`; `RC_C3_referee.md`; and, because the result below hinges on it, `C4_I1_report.md` + `C4_I1_referee.md` (the folded tower).

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/N1/`

| Script | Output | What it checks |
|---|---|---|
| `n1_tower_geometry.py` | `n1_tower_geometry.out` | For the tower forced on an interacting one-particle shell (§1.4): branch touching at the zone face, embedding of the n ≠ 0 members in the two-particle continuum at fixed Q, and the T1 sum rule carried by the face kinks of the energy-sorted lowest branch (d = 2, 3; centres θ = 0 and θ = (π,…,π)). |

Notation follows C3, I1, M1 and B1. K_b is the first moment of the energy density, P_b = i[H,K_b], u = E²/2. Closure means [H,P] = 0, i[K_b,P_c] = −βδ_bc H with β > 0, plus closing rotations. T_j are the lattice translations. "First-moment covariance" means T_j K_b T_j⁻¹ = K_b − j_b H.

## Reading against the FIXED lines (lane RN2, probe N1)

**PASS: not met.** No interacting lattice theory with exact closure in d ≥ 2 was found or constructed. The only known exact realization is I1's §3a, which uses infinite-dimensional sites with unbounded terms; that is a Qubit price, not a qubit theory.

**FAIL: met only for a subclass. The lane reading for N1 is INCONCLUSIVE, leaning FAIL.**

- **What is proved (bounded FAIL for a subclass).** Take a gapped interacting lattice theory, with or without particle-number conservation. Suppose it has even one eigenband E(Q) whose eigenprojection is C¹ over the whole Brillouin torus, with u = E²/2 in W^{2,1}. This is the generic lattice situation, and it is what the lattice Haag–Ruelle isolated-shell hypothesis provides. Then exact closure is impossible (§1.5, Theorem 5 and Corollary 6; T1 of M1 carried over to joint spectral projectors).
- **Why that does not settle the stated class: the expected route is circular.** Exact closure plus a mass gap *forces* every isolated mass shell of the interacting theory to be a complete I1 tower (§1.4, Theorem 4). The tower has three features:
  - its branches touch at the zone faces;
  - all but finitely many of its members at each Q are embedded in the multi-particle continuum;
  - its energies at fixed Q are unbounded.

  So "the single-particle bands of the interacting theory are isolated Bloch bands" is not a consequence of gap plus asymptotic completeness. It is an extra hypothesis that the theory under test violates whenever it closes. The T1 route proves exactly "closure ⇒ no eigenband has a C¹ eigenprojection over the whole torus". It does not prove "closure is impossible".
- **What remains (the real open core).** Can a lattice with finite-dimensional sites and bounded local terms host an interacting one-particle tower?
  - The bounded-sector theorems (M1 T2, B1 Theorem U) do not bite, because H is unbounded on the tower.
  - The energy-density ("anti-contraction") bound gives an inequality, not a contradiction (§2.3).
  - The index route works in 1D (M1 T3, conditional). In d ≥ 2 it reduces, under the same conditions (gap, unique vacuum, asymptotic completeness, rational centres), to one named lemma: **Lemma F**, that a lattice shift on Z^d qubits is not the finite-time flow of a translation-invariant local Hamiltonian. The reduction is PROVED (conditional). Lemma F itself reduces, via a tube argument, to an index-robustness lemma (the approximate Lemma B). That lemma is ARGUED, via a dimension-free Choi-fidelity bound plus the comparator mutual-information index formula. It is not proved (§2.2).
  - **If a referee confirms the approximate Lemma B,** the gapped + asymptotically complete + rational-centre class in d ≥ 2 becomes a conditional FAIL, with exactly the status M1-T3 has in 1D. Irrational centres, failure of AC, and particle-free or massless sectors stay open (§3).

**Against the supervisor expectation** ("one-particle bands are isolated Bloch bands, T1 applies, S-matrix inherits"):
- The expectation is **correct for the generic lattice class**, and stronger than stated: only isolation inside each momentum fibre is needed, not isolation in energy across the zone.
- It is **not correct as a proof for the stated class**. Under exact closure the one-particle shell is the tower, not a set of isolated bands. Lattice Haag–Ruelle (BDN) is then not applicable as cited, and T1 has nothing to act on.
- The cluster argument ("the S-matrix inherits") moves the question onto the one-particle shells. It adds no obstruction of its own (§1.6).

## 0. Hypotheses

- **H-loc.** Z^d (d = 2, 3) with finite-dimensional sites (M₂(C) per site, or finitely many qubits per cell), and a translation-covariant, finite-range, uniformly bounded energy density h(x), ‖h(x)‖ ≤ h₀. Particle number need not be conserved; the vacuum Ω is the interacting ground state. P_b = Σ_{x,y} ½(x_b − y_b) i[h(y),h(x)], plus any finite-range improvement, is then itself a translation-invariant, finite-range sum of bounded terms.
- **H-int.** Exact closure holds as operator identities that integrate to a strongly continuous unitary positive-energy representation U of the Poincaré group (rotations included) on the GNS space of Ω. Nelson's theorem gives this from an analytic dense domain; it is assumed, not proved (as in I1 and M1; the I1 referee flagged it).
- **H-cov.** First-moment covariance holds: T_j K_b T_j⁻¹ = K_b − j_b H, T_j L T_j⁻¹ = L − j∧P, and T_j H T_j⁻¹ = H.
- **H-gap.** Ω is the unique translation-invariant ground state, and spec(H) on Ω^⊥ lies in [m, ∞) with m > 0.
- **H-AC** (only where stated). Asymptotic completeness for the particles of the exact (H,P) spectrum, with the asymptotic Fock space carrying the tensor-product Poincaré representation.

## 1. Reduction theorems

### 1.1 Lemma 1: the vacuum is Poincaré invariant (PROVED under H-int, H-gap)

**Statement.** PΩ = 0, KΩ = 0 and LΩ = 0.

**Proof.**
1. Boost invariance of the joint spectrum of (H, P), together with H ≥ 0, puts that joint spectrum in the closed forward cone P²/β ≤ H². Then HΩ = 0 forces the (H,P) spectral measure of Ω onto the origin, so U(translations)Ω = Ω.
2. The zero-momentum spectral subspace is Lorentz invariant, because the origin is a fixed point of the Lorentz group. By uniqueness it is one-dimensional.
3. SO₀(d,1) is perfect, so it acts on that line by the trivial character. ∎

**Remark (the identity is CHECKED algebra; the O(k⁴) statement is ARGUED).** KΩ = 0 is a real constraint on the lattice vacuum. Write C(r) = ⟨h(0)h(r)⟩_c. Then ‖K_bΩ‖² per site = −½ Σ_r r_b² C(r) = ½ ∂_b² S_h(0), where S_h is the energy-density structure factor. So closure needs S_h(k) = o(k²).
- Generic lattice models: the energy current j_b is not conserved, so S_h ∝ k².
- With [H,P] = 0: the lattice Poincaré lemma (Kapustin–Sopenko, COMPARATOR from memory) makes i[H, j_b] a divergence, and S_h = O(k⁴), as in relativistic QFT.

So this is consistent with closure, and not an independent obstruction.

### 1.2 Lemma 2: the gap excludes massless sectors (PROVED)

**Statement.** Under H-gap, every irreducible component of U on Ω^⊥ has mass M ≥ m.

**Proof.** A component of mass M contains states with energy arbitrarily close to M (at p → 0). A massless component contains states with energy arbitrarily close to 0. ∎

So the mass operator 𝓜² = H² − P·P/β satisfies 𝓜 ≥ m on Ω^⊥.

### 1.3 Lemma 3: which "one-particle subspace" the boosts preserve (PROVED under H-int, H-cov)

This settles route (2)'s first loophole.

**(a) Mass-shell subspaces are boost invariant.** 𝓜² is the Casimir of U, so it commutes strongly with U(g) for every g. T_j commutes with H and, by H-cov, with P: T_j P T_j⁻¹ = i[H, K − jH] = P. In integrated form, T_j U(g) T_j⁻¹ = U(j)U(g)U(j)⁻¹, with U(j) = e^{−ij·P/β}. So every spectral subspace of 𝓜 is invariant under the whole Poincaré group and under the T_j.
- Define the one-particle space by an isolated eigenvalue M₁ of 𝓜 on Ω^⊥: 𝓗₁ = ker(𝓜² − M₁²).
- Then **K cannot map one-particle states into multi-particle states.** Multi-particle states have 𝓜 ≥ 2m, while K preserves 𝓜.

**(b) The lattice-band subspace is P-invariant but not K-invariant.** Let Π_E be the joint spectral projector of the commuting family (T_j, H) onto an eigenband {(Q, E(Q))}. P commutes strongly with T and H, so [P, Π_E] = 0. K does not preserve Π_E unless the band is a union of mass shells. **T1 does not need K-invariance; it needs only P-invariance** (§1.5).

### 1.4 Theorem 4: the interacting one-particle shell is a complete tower (PROVED under H-int, H-cov, H-gap)

**Statement.** Let M₁ be an isolated eigenvalue of 𝓜 on Ω^⊥. Then 𝓗₁ is a direct integral or sum of positive-energy irreducible representations of mass M₁. In lattice momentum, each component has the fibre

E_n(Q) = √(M₁² + β|Q − θ + 2πn|²), n ∈ Z^d.

The set of centres {θ} is invariant under the cubic group.

**Proof.** This is I1 Theorem 1, route (i), applied on the interacting GNS space, restricted to the invariant subspace 𝓗₁ (Lemma 3a).
1. V_j := U(j)⁻¹T_j commutes with H, P, K and L.
2. On each irreducible component, V_j acts on the multiplicity space. On a scalar irreducible it is a phase e^{iθ·j}.
3. The momentum spectrum of each component is R^d, and Q ≡ Π + θ (mod 2π).

The proof uses neither number conservation nor band labels.

**Consequences, CHECKED in `n1_tower_geometry.out`** (M₁ = β = 1; d = 2, 3; θ = 0 and θ = (π,…,π)):

1. **Touching.** The gap between the lowest member at Q and the next one falls linearly to 0 at the zone face: 5.362, 2.955, 0.599, 0.0599, 0.00599 and 0 at |Q − θ| = 0, 0.5π, 0.9π, 0.99π, 0.999π and π along the x axis. No branch is an isolated band.
2. **Embedding.**
   - At fixed Q the two-particle continuum is [thr(Q), ∞), since relative momentum is unbounded.
   - All n ≠ 0 members lie inside it, except finitely many. At every scanned point at most one member, the nearest face partner, lies below the threshold: 0 or 1 of 48 (d = 2) and 0 or 1 of 342 (d = 3).
   - The n = 0 member is never embedded.
   - Exact closure keeps the embedded members stable automatically: 𝓜 is conserved, and the continuum has 𝓜 ≥ 2M₁.
3. **Unboundedness.** E_n(Q) → ∞ at every fixed Q.
4. **T1's sum rule sits in the face kinks.** For the energy-sorted lowest branch u₀:
   - Hess u₀/β = 1.000000 on the open zone (90% of grid points in d = 2, 61% in d = 3);
   - the zone average of Hess u₀/β − 1 is −1 in every direction, carried entirely by the face kinks.

   This is the "Hilbert hotel" of I1, now for an interacting shell.

**Conclusion of §1.4.** In an exactly closed gapped theory, interacting or not, the one-particle spectrum is **never** a finite union of isolated Bloch bands.

### 1.5 Theorem 5 (T1 for interacting theories, fibre-isolated form): PROVED under H-int, H-cov, as a small extension of M1's T1

**Statement.** Let E: T^d → R be an eigenband of the interacting H with these properties:
- Π_E (joint spectral projector of (T,H), Lemma 3b) is nonzero;
- its eigenprojection Q ↦ Π_E(Q) is C¹ on the whole torus;
- u = E²/2 is in W^{2,1}(T^d).

Then closure forces Hess u = βI on T^d. That is impossible for a periodic u.

**Proof.** As in M1's T1, with one change: the spectral projector of H is replaced by the joint projector of (T, H).
1. P commutes with Π_E (Lemma 3b), so (1 − Π_E)PΠ_E = 0.
2. H-cov makes Π_E K Π_E − ½{i∂_Q, E} commute with every T_j. It is therefore a fibred multiplier f(Q), in a C¹ frame; it is matrix-valued if the band is degenerate.
3. Π_E P Π_E = ∇u, and Π_E i[K_b,P_c] Π_E = −E ∂_b∂_c u.
4. Then ∫_T Hess u = 0, which is incompatible with Hess u = βI. ∎

The functional-analytic reading is the one the M1 referee asked for: the closure identity is taken weakly, on the band's C¹ sections.

**What is new against M1-T1:**
- isolation is needed only inside each momentum fibre. The band may overlap the continuum's energy range at other Q, which is common in d ≥ 2 interacting models;
- even an embedded band is excluded, if its eigenprojection is C¹ over the torus;
- what escapes is exactly a band whose eigenprojection is discontinuous somewhere, and the tower's face is such a place.

**Corollary 6 (bounded FAIL; PROVED).** Take a gapped interacting lattice theory, of any number non-conservation, in d = 2 or 3. Suppose that in any sector it has an eigenband with a C¹ eigenprojection over the whole torus, for example a Bachmann–Dybalski–Naaijkens isolated one-particle band (COMPARATOR, arXiv:1412.2970, from memory: lattice HR assumes an isolated, smooth shell). Then the theory has no exact closure. **Dual form:** exact closure ⇒ every eigenprojection of every band is discontinuous somewhere on T^d.

### 1.6 The cluster / S-matrix argument (ARGUED; it adds no new obstruction)

**Under H-AC:**
- H and P are translation-invariant sums of local terms, so they act additively on separated wave packets (cluster property).
- K acts additively if the asymptotic Fock space carries the tensor-product Poincaré representation (part of H-AC as stated; this is standard in relativistic QFT via covariant fields, and **not proved** for the lattice).
- Then the anomaly D_bc = i[K_b,P_c] + βδ_bc H is additive over asymptotic particles. M1's free-continuum formula is the special case D = Σ_i ε_i(β − Hess u(q_i)).
- So closure on the whole asymptotically complete theory ⇔ closure on every one-particle shell.

**Consequence.** "The S-matrix inherits the obstruction" is true only when the shells are bands, i.e. when Corollary 6 already applies. For tower shells, D = 0 on every shell and there is nothing to inherit. The multi-particle sectors reduce the question to §2; they do not answer it.

## 2. Can a qubit lattice host an interacting tower? (the open core)

### 2.1 The bounded-sector theorems do not apply (PROVED, negative)

M1-T2 and B1-U need a K-invariant sector on which H and P are bounded. By Lemma 3a and Theorem 4, the only K-invariant sectors are spectral subspaces of 𝓜. Every one except {Ω} contains full mass hyperboloids, so H is unbounded on it.
- In number-conserving models the fixed-N sectors were K-invariant and bounded. That is why T2 worked there.
- Without number conservation no such sector exists.

### 2.2 Index route in d ≥ 2: a reduction to one lemma (PROVED conditional; final lemma ARGUED, not proved)

**Step 1 (PROVED, dimension-free, under H-int, H-cov, H-gap, H-AC, and rational centres θ_s ∈ (2π/q)Z^d with a common q).** This is M1-T3's argument, which never used d = 1:
1. V_j = U(j)⁻¹T_j commutes with the Poincaré group.
2. It acts on every one-particle component by e^{iθ_s·j}.
3. It acts on in-states as the product of those phases, and fixes Ω.
4. So V_j^q = 1 on a complete set. The GNS representation of a pure state of the simple algebra ⊗M₂ is faithful, so the automorphism is the identity.

Since U(j), V_j and T_j commute, this gives

**τ_{q e_b} = Ad e^{−i q P_b/β} on the quasi-local algebra of Z^d.**

In words: the shift by q along e_b equals the time-q/β flow of the translation-invariant, finite-range, bounded Hamiltonian P_b (H-loc).

**Step 2: Lemma F (ARGUED in d ≥ 2; PROVED in d = 1).** On Z^d with qubit sites, no shift τ_{q e_b} with q ≠ 0 equals the finite-time flow of a translation-invariant, finite-range (or exponentially quasi-local) Hamiltonian.

- **In d = 1** it holds:
  - the GNVW index of the shift is q·log 2;
  - every finite-time LR flow has index 0 (RWW: connected to the identity through approximately locality-preserving unitaries);
  - the index group is torsion-free (COMPARATOR: GNVW arXiv:0910.3675, RWW arXiv:2012.00741).

  This is M1-T3.
- **In d ≥ 2: tube reduction.** This is a sketch with one named gap. Take b = 1, s = q/β and G = P_1/β, so that σ_t = Ad e^{−itG} and σ_s = τ_{q e_1} on Z^d (Step 1).
  1. **The tube is invariant.** Let W = Z × B_ℓ, with B_ℓ a transverse box of side ℓ. The shift τ_{q e_1} preserves the tube algebra 𝔄_W. Since σ_s = τ_{q e_1} exactly, so does σ_s. Read W as a 1D chain with supersites B_ℓ, of dimension 2^{ℓ^{d−1}}. On this chain, τ_W has GNVW/RWW index q·ℓ^{d−1}·log 2.
  2. **The truncated flow has index zero.** Let G_W be the sum of the terms of G that lie inside W, and σ^W_t its flow on 𝔄_W. G_W is finite-range and translation-invariant along e_1, so σ^W_s is a Lieb–Robinson flow on the chain and has index 0 (RWW, COMPARATOR).
  3. **The composite carries the whole index.** Set γ := (σ^W_s)⁻¹ ∘ τ_W. It is an approximately locality-preserving unitary (ALPU) on the chain, and by additivity ind γ = q·ℓ^{d−1}·log 2.
  4. **γ is close to the identity in the interior (ARGUED; standard Duhamel plus Lieb–Robinson).** Let A be supported in the interior I = Z × B_{ℓ−2R}, on n consecutive slices. The two flows differ only by terms at the lateral boundary, at distance ≥ R from A. So ‖γ(A) − A‖ = ‖σ_s(A) − σ^W_s(A)‖ ≤ C·s·e^{vs}·n·ℓ^{d−2}·poly(R)·e^{−R/ξ}·‖A‖. Choosing R = ξ(vs + (d−1)ln ℓ + c), which is O(log ℓ), makes this ≤ ε for any fixed ε.
  5. **The index bound.**
     - *Exact version (PROVED from GNVW facts).* Suppose γ fixes 𝔄_I pointwise. Then it preserves the relative commutant 𝔄_I′ ∩ 𝔄_W = 𝔄_{W∖I}, so γ = id_I ⊗ γ_bd. Hence |ind γ| = |ind γ_bd| ≤ r·log dim(boundary supersite) ≈ r·2(d−1)·R·ℓ^{d−2}·log 2.
     - *The contradiction.* This is far below q·ℓ^{d−1}·log 2 for ℓ ≫ R, which is a contradiction.
  6. **The named gap (Lemma B, approximate version; ARGUED below, not proved).** The ε-approximate version of step 5, "ε-close to the identity on interior block algebras ⇒ the same index bound", needs an index-robustness statement with dimension-free constants.
     - The interior supersite dimension grows like 2^{ℓ^{d−1}}.
     - One block at a time, the averaging lemma for amenable algebras gives γ|_{𝔄_B} = Ad u_B with ‖u_B − 1‖ = O(ε).
     - Gluing the u_B into a global decomposition is the unproved step.

     **A route that avoids gluing (ARGUED, from comparator formulas).** It uses the Choi-state, mutual-information form of the 1D index (Gong–Sünderhauf–Schuch–Cirac 2020; RWW 2022; COMPARATOR from memory). That form is computed on a finite window of supersites around a cut, with tail corrections for an ALPU.
     1. **Dimension-free closeness of the interior Choi state.** Let B be an interior block of dimension D_B. Its Choi state has overlap with the maximally entangled projector Φ_B equal to D_B⁻² Σ_{Paulis P on B} τ(γ(P)P†), where τ is the unique tracial state, which every automorphism preserves. Each term is within ε of 1, so the fidelity is ≥ 1 − ε and the trace distance is ≤ √ε. The constants do not depend on dimension.
     2. **Interior pairs decouple.** By monogamy and Alicki–Fannes–Winter continuity, the interior pairs decouple from everything else, up to O(√ε·log D_window) + h(√ε).
     3. **The window bound.** The cut mutual informations that define the index are then bounded by the boundary layer: |ind γ| ≤ C·R·ℓ^{d−2} + C′·√ε·ℓ^{d−1} + o(ℓ^{d−1}).
     4. **The contradiction.** Against ind γ = q·ℓ^{d−1}·log 2, this fails once ℓ is large and ε is small. ε can be made small by taking R = O(log ℓ + log(1/ε)).
     5. **What a referee must check.** The exact window form of the mutual-information index formula for ALPUs, and the tail bookkeeping.
- **Alternative comparator.** For d = 2 there is the Freedman–Hastings classification of 2D QCAs and their flow across a line (arXiv:1902.10285, from memory). It is stated for strict QCAs; the flow here has Lieb–Robinson tails.

**Status.**
- Under H-AC with rational centres, exact closure in d ≥ 2 ⇒ Lemma F fails.
- Lemma F reduces to the approximate Lemma B. The exact version is proved; the approximate version is standard folklore ("a shift is not a Hamiltonian flow"; information flow through an interior that is close to the identity is bounded by the boundary).
- With it, the unrestricted gapped + AC + rational-centre class would be a FAIL. That is not proved here.

**Not covered by Step 1:**
- irrational centres;
- failure of AC;
- theories with no isolated mass eigenvalue in any sector (§3c).

### 2.3 The energy-density (anti-contraction) bound gives an inequality, not a contradiction (CHECKED as an estimate)

**The estimate:**
1. Let ψ₀ = BΩ be a shell state made by a local B of radius R₀. Since KΩ = 0, its boost is e^{iηK}ψ₀ = B_ηΩ, with B_η = Ad e^{iηK}(B) and the same norms.
2. K's couplings grow like |x_b|, so the Lieb–Robinson support of B_η grows like R₀e^{vη}, where v is the Lieb–Robinson velocity of H.
3. The energy of B_ηΩ is at most 2h₀(R₀e^{vη})^d‖B‖/‖BΩ‖.
4. The shell needs energy growing like M₁cosh(√β η).

**What it shows.** These are compatible whenever √β ≤ d·v. The group-velocity bound already requires √β ≤ v, so the condition holds. So the lattice forces the tower members to spread, the "anti-contraction" of M1 §3.4 and I1 §2c. It does not forbid them.

**Why the local version also fails.** Exact global closure does not constrain the energy-density form factors at finite k: only h_{k=0} = H and ∂_k h_k|₀ ∝ K enter the algebra. Lattice energy density is also not positive. So no local-contraction argument follows from the global algebra (READING, consistent with M1).

### 2.4 Bisognano–Wichmann / type argument (SUGGESTED; side remark)

**What would give a contradiction.** If BW held, the half-space modular group would be the boost. That forces the half-space algebra to be type III₁, because massive boosts have absolutely continuous spectrum on Ω^⊥.
- **1D.** A gapped ground state has the split property (Matsui; COMPARATOR from memory), so the half-chain algebra is type I. BW would then be contradictory.
- **d ≥ 2.** Half-space algebras of entangled lattice ground states are generically non-type-I. ITPFI across an infinite cut can be type III₁. So no obstruction follows.

**Why it does not apply anyway.** BW is not derivable here: first-moment boosts do not preserve half-space algebras exactly (terms straddle the cut).

## 3. Loopholes (route (2))

**(a) "K maps one-particle into multi-particle."** Impossible for the mass-defined one-particle space: 𝓜 is a Casimir (Lemma 3a). Possible for the lattice-band subspace, but T1 needs only P-invariance there (Lemma 3b, Theorem 5). **Closed.**

**(b) Massless sectors (no gap).** These need two separate statements.
- A point spectrum at 𝓜 = 0, if present, is again a tower: I1's massless cone without its tip, by the same representation argument.
- But 𝓜 = 0 is not isolated (two-particle mass starts at 0). So there is no isolated band for T1, and Haag–Ruelle is replaced by Buchholz's massless scattering.

**Open; excluded by H-gap.**

**(c) Infraparticles and theories without particles.** These have no point spectrum of 𝓜. They have neither a tower nor a band, so neither Theorem 4 nor Theorem 5 acts.
- A gapped vacuum sector can also lack isolated shells, as in topological order, where the local excitations are anyon pairs in a continuum. The particles then live in superselection sectors.
- Theorem 4 repeats in any sector that carries a covariant positive-energy representation with an isolated mass. Covariance of lattice anyon sectors under the Poincaré group is an extra assumption (Naaijkens; Ogata cone sectors; COMPARATOR from memory).

**Open.**

**(d) Irrational centres.** Step 1 of §2.2 needs V^q = 1. **Open**, as in M1.

**(e) Direct integrals and infinite multiplicity** (the I1 referee's point). Theorem 4 holds component-wise and does not need a discrete union. **Closed.**

**(f) Non-first-moment generators.** H-cov is the first-moment property. B1's Theorem S shows a lapse smearing forces it, so it is the gravity-relevant class. Other generators are outside this probe.

## 4. Q-RN2 readouts

- **Exact closure + gap ⇒ the interacting one-particle shell is a complete tower:** branches touch at the faces, all but finitely many members per Q are embedded, and energies are unbounded. PROVED; geometry CHECKED.
- **Any C¹-projection eigenband, embedded or not, in any interacting theory ⇒ no closure:** PROVED (Theorem 5). This is the generic lattice class.
- **Bounded-sector theorems:** inapplicable without number conservation. PROVED.
- **Index route, d ≥ 2:** reduces to Lemma F under AC and rational centres, and Lemma F reduces to the approximate Lemma B (a tube of cross-section ℓ^{d−1}: index q·ℓ^{d−1}·log 2 against a boundary bound O(ℓ^{d−2}·log ℓ)). The reductions are PROVED or ARGUED. The approximate Lemma B is ARGUED via comparator formulas and is the item a referee must settle.
- **Energy-density bound:** an inequality √β ≤ d·v, not a contradiction.

**Reading for N1: INCONCLUSIVE, leaning FAIL.**
- FAIL (bounded) is PROVED for the subclass of Corollary 6.
- For the gapped + AC class in d ≥ 2, FAIL follows from rational centres plus the approximate Lemma B. The lemma is ARGUED, not proved. If a referee confirms it, this class becomes a conditional FAIL with M1-T3's status.
- Irrational centres, non-AC theories, particle-free sectors and massless sectors remain open.

## Labels

**PROVED (same family, unrefereed):**
- Lemmas 1–3;
- Theorem 4, under H-int (as I1 route (i));
- Theorem 5 and Corollary 6 (M1-T1 extended to joint projectors, with the weak-form reading);
- §2.1;
- §2.2 Step 1, conditional on H-AC, rational centres, faithful GNS and HR covariance, exactly as M1-T3 but in any d.

**CHECKED:**
- `n1_tower_geometry.out`: touching gaps, embedding counts, sorted-branch sum rule −1.000000, bulk Hessian 1.000000;
- the ‖KΩ‖² structure-factor identity (algebra).

**ARGUED:**
- §1.6 additivity of K on asymptotic states;
- §2.2 step 4 (Duhamel plus Lieb–Robinson interior closeness);
- §2.3 estimate;
- Lemma F in d ≥ 2 (tube route: the exact Lemma B is PROVED from GNVW facts; the approximate Lemma B is ARGUED via Choi fidelity plus the comparator mutual-information index formula, and it is the named gap).

**SUGGESTED:**
- §2.4.

**READING:**
- "Hilbert hotel" at the face for interacting shells;
- the S-matrix inherits nothing beyond the shells.

**COMPARATOR (from memory, not re-fetched this run):**
- Bachmann–Dybalski–Naaijkens arXiv:1412.2970; GNVW arXiv:0910.3675; RWW arXiv:2012.00741;
- Freedman–Hastings arXiv:1902.10285; Kapustin–Sopenko (lattice Noether/Poincaré lemma);
- Christensen (near inclusions); Matsui (split property); Gong–Sünderhauf–Schuch–Cirac (Choi/mutual-information index); Alicki–Fannes–Winter continuity;
- Buchholz (massless scattering); Naaijkens/Ogata (lattice superselection sectors).

**Scope of "impossible":**
- Corollary 6 only: gapped lattice theories, first-moment generators, H-int, and at least one eigenband with a C¹ eigenprojection on the whole torus.

**Not claimed:**
- impossibility for gapped theories whose shells are all towers, in d ≥ 2;
- irrational centres; massless or infraparticle sectors; theories without isolated shells; non-first-moment generators.
