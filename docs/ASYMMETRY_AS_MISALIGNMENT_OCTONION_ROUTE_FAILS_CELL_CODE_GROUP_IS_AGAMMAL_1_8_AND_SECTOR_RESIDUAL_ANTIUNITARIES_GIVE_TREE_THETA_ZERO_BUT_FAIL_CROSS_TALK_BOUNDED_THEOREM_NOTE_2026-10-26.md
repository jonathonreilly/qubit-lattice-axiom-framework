---
claim_id: asymmetry_as_misalignment_octonion_route_fails_cell_code_group_is_agammal_1_8_and_sector_residual_antiunitaries_give_tree_theta_zero_but_fail_cross_talk_bounded_theorem_note_2026-10-26
claim_type: open_gate
claim_scope: "Exact finite group and code facts for Gottesman's [[8,3,3]] code; failed searches for octonion structure over the stated families only; supplied-model mass-matrix and slab diagnostics for a sector-misalignment CP mechanism. No physical identification, candidate-law text or axiom change is proposed or adopted."
upstream_dependencies: []
runner: scripts/asymmetry_as_misalignment_2026_10_26.py
---

# Asymmetry as misalignment: the octonion route fails, the cell code's group is AΓL(1,8), and sector residual antiunitaries fix tree θ̄ but fail cross-talk

Claim type: open_gate. A record of one first-principles thread across the four walls (chirality and mirror, family count, family labels and hierarchy, CP with θ̄ ≈ 0). It is kept so the idea, its tests and its failure points are not lost.
Primary runner: `scripts/asymmetry_as_misalignment_2026_10_26.py` (driver; 16 declared helper parts, about 20 min). Labels: [T] exact, [F] finite diagnostic, [N] failed search over the stated family only, [S] reading.

## Motivating pattern

On every wall, recent candidate-law probes (#10065–#10083) find the rule *too symmetric*. Every asymmetry the Standard Model has turns out to be chosen:
- Rules that treat families alike keep U(3) (#10071, #10075).
- The family-class tick keeps an antiunitary that forces J = 0 (#10068).
- The far-wall gap is chosen, or fragile at large L (#10076).
- Every "3" is an index someone picked (#10065, #10077).

The working hypothesis behind this note: the law is symmetric, and every asymmetry comes from a discrete structure plus a vacuum choice. Two carriers for that hypothesis were tested.

## O. Carrier 1: octonions / F₈ on the cube cell, with matter in J₃(𝕆). Fails.

The proposal:
- The 8-vertex cell carries the octonion index structure (𝕆 as a twisted group algebra of Z₂³).
- J_n(𝕆) is Jordan only for n ≤ 3, which would give the family number.
- The Standard Model group would come from F₄ (Dubois-Violette–Todorov).
- CP would come from choosing a complex structure.

An independent adversarial review, at maximum reasoning effort with its own scripts, judged every payoff overclaimed or wrong:
- The n ≤ 3 bound caps a matrix size once 𝕆 is chosen. It does not select 3.
- The three off-diagonal octonions are inequivalent 8-dimensional real slots, not 16-state families. One 27 of E₆ is one family plus 10 + 1.
- The Dubois-Violette–Todorov construction uses the same index as electroweak U(2).
- A unit imaginary u and −u are related inside G₂, so the choice has no CP-odd invariant.
- The proposed "family" Frobenius acts as a colour rotation.
- As an observable algebra, J₃(𝕆) has no composite systems (Barnum–Graydon–Wilce 2020). That excludes it independently of the Qubit axiom. ℂ⊗𝕆 is M₈(ℂ), which gives colour, not families.

Executed tests:
- **O1 [N]** No group-invariant anticommuting 7-set of logical Paulis exists (0 of 288), so the code carries no octonion (Clifford-7) structure. The single F₂₁-invariant set is forced by 288 ≡ 1 (mod 7) and does not discriminate.
- **O2 [T]** The cyclic octonion table has 1344 signed automorphisms. Its pure permutation automorphisms are i ↦ ai + b with a ∈ {1, 2, 4}: the normaliser of the 7-cycle, true of any cyclic labelling. The F₂₁ match is generic.
- **O3 [T]** Control: H_n(ℍ) satisfies the Jordan identity for n = 3, 4, 5.
- **O4 [S]** The preimage of F₂₁ in Aut(𝕆) has AΓL(1,8)'s element-order statistics, as Schur–Zassenhaus forces. It fixes the real unit, while the code group is transitive on the qubits. The match is abstract only.
- **O5 [N]** No order-7 site permutation preserves |U(K)| of CL-1's tick (ε = 0.3, 1.1) or of FREEZE. This holds with any diagonal phases and any O_h momentum map. The site-permutation groups of the two ticks are {1, one involution} and {1}.
- **O6 [N]** The second-quantised one-cell tick (Jordan–Wigner) preserves the [[8,3,3]] code space for no labelling × uniform frame (8! × 6).
  - Minimum leaks: CL-1 intra-cell 0.41 / 0.92; CL-1 at generic K 0.58; FREEZE 0.95 / 0.99; random baseline 0.99; identity control 7e-16.
  - CL-1's K = 0 block is exactly the identity, so it is excluded as a trivial pass.
  - So "logical qubit = family" (#10077 iii) has no dynamics behind it.
  - Not covered: the full local-Clifford group, the Bravyi–Kitaev encoding.

## G. A surviving exact result: the [[8,3,3]] code's symmetry group

- **G1–G4 [T]** The group of qubit permutations × uniform frames preserving Gottesman's [[8,3,3]] stabiliser group has order 168 (56 per frame id, XYZ, ZYX).
  - It is **AΓL(1,8) = 2³ ⋊ (7 ⋊ 3)** in its natural action, with an explicit F₈ labelling of the qubits.
  - Centre 1; derived series 168 > 56 > 8; element orders 1:1, 2:7, 3:56, 6:56, 7:48.
  - So it is neither PSL(2,7) (21 involutions, no elements of order 6) nor AGL(1,8) × Z₃.
  - The frame power equals the element's Galois (Frobenius) exponent: the 3-fold turn is the Frobenius x ↦ x² locked to the X→Y→Z frame cycle.
  - An independent method, with GL(S) permuting the eight subspaces K_j, gives the same 168 as the full local-Clifford × permutation group. Every element uses a uniform frame.
- **G5 [T]** The largest overlap with O_h over all 8! labellings is 24 (T_h type). It never contains a 4-fold turn.
- **G6 [T]** The X, Z and X⊕Z support projections of the stabiliser group are each the [8,4,4] extended Hamming code RM(1,3), with Aut = AGL(3,2) of order 1344. This is the common cause of the F₈, Fano and Cayley-form coincidences.
- **G7 [F] numerology control** The [[8,3,2]] cube colour code also has AGL(3,2) ⊃ O_h, and a frame-free 3-cycle of its logical qubits. 0 of 100 random [[8,3]] codes have an order-7 symmetry. Only the frame lock and the missing 4-fold turn are specific to [[8,3,3]].
- **G8 [T]** On the 63 logical classes the orbits have sizes 7, 28 and 28. The 7-orbit is a commuting Lagrangian. No splitting of the logical space into 3 qubits is invariant; the largest stabiliser has order 6.

## M. Carrier 2: sector misalignment of residual antiunitaries. Tree level works; cross-talk fails.

Principle, proposed by the reviewing agent:
- The law keeps an exact magnetic space group G: translations, cube rotations and an antiunitary T.
- Each Yukawa sector condenses into a vacuum keeping its own residual T·g_s.
- CP-odd invariants come only from the relative element g_u g_d⁻¹.
- At the momentum-π nodes, translation characters are real, so det F(g) = ±1 and θ̄_tree ∈ {0, π}.
- Families are the three X-point nodes of the adopted slab window.
- The orbit sizes 1, 3, 3, 1 at momentum π, together with "CP needs ≥ 3 families", give N_f = 3 = the number of axes, with that 3 playing one role only.

Executed tests (criteria fixed before running; reproduced in the appendix):
- **M1 [F]** At m = 3 and Ls = 8 the slab's near-wall zero modes sit exactly at the three X points, 2 states each, one hand (A1). An antiunitary C·K with k → −k commutes with the slab (A2).
- **M2 [F]** A3 fails as pre-registered: the C2 family actions carried ±i because the overall operator phase was not fixed.
  - A disclosed post-hoc spin-statistics normalisation (gⁿ = (−1)^F) makes every C2 real.
  - The translations act as diag(−1, 1, 1) and its permutations: real and non-scalar.
- **M3 [F]** Supplied 3×3 Yukawas constrained to each sector's residual, 2000 samples per pair:
  - misaligned sectors: |sin θ̄_tree| ≤ 1e-12 with median |J|/J_max ≈ 0.28;
  - aligned control: J < 1e-13;
  - genericity controls: generic complex Yukawas, Haar U(3) and incommensurate characters are θ̄-safe in under 0.5% of samples.
  - The protection comes from the real characters at momentum π, not from numerology.
- **M4 [F]** A single-site vertex gives an exactly rank-1 Yukawa. But local ε^|c| profiles give no hierarchy: median s₁/s₂ = 5.6 and s₂/s₃ = 2.9, against a pre-set ≥ 10. The democratic term is also incompatible with a non-scalar real twist. **No hierarchy mechanism.**

**X. Decisive test: cross-talk on the slab.** Ls = 40, m = 2.5. Wall-mode Yukawas are derived from the slab wavefunctions. Each sector's order also enters all species' densities at κ = 1.
- **X1** The pre-registered runner reproduces PASS = 2, FAIL = 6.
  - The on-site vertex Qᵀ(1⊗ε)X gives a scalar Yukawa ∝ 1, so J is undefined (D1).
  - D3, D6 and D7 fail on precision only: 1e-10 to 1e-11 against a 1e-12 threshold.
- **X2 (decisive, D2)** The induced θ̄ is **O(1)** (median 1.2–2.0) and **flat in the sector separation** (Δ = 1..18).
  - Separating the sectors protects nothing.
  - θ̄_ind is linear in κ, so the mechanism needs κ ≲ 1e-10. This is the Nelson–Barr quality problem in lattice form.
- **X3 (D2r)** Under a supplied restriction, the flat leak vanishes. The restriction: the shallow order's density also respects the deep sector's residual, e.g. a charged order entering only as |order|². The remainder then decays with depth and reaches 4e-10 at Δ = 18, just above the 1e-10 threshold.
- **X4 (post hoc, disclosed; corrected)** A generic on-site vertex symmetrised to each sector's residual gives θ̄_tree = 0 to working precision. But J is exactly 0, not 0.2–0.5 as first read.
  - On this slab the on-site scalar vertex always gives Y = λ·1 + antisymmetric, because the three X-node frames are quaternion units.
  - So the real down sector has a degenerate mass pair. The commutator invariant is below 1e-15 in every draw.
  - The earlier |J| reading was 0/0 noise and is withdrawn.

## R. Can a charge derive the D2r restriction? Partly. The rest needs Peccei–Quinn.

Model: as in X, plus a U(1)_H charge on both orders (hypercharge-like) and every vertex the charge allows: on-site and bond Yukawas, |φ|² densities, bond currents, φ_uφ_d. Criteria were fixed before each run; the v2 model changes were written down before v2 ran (a disclosed post-hoc step after run 1, which gave PASS 5 / FAIL 4).
- **R1 [F] (v2: PASS 8 / FAIL 1)**
  - Every density coupling linear in an order is forbidden exactly (E0).
  - Tree level: θ̄ = 0 (≤ 2e-15) with median |J|/J_max 0.09 and no degenerate draws. The bond vertices lift the degeneracy (E1).
  - Breaking the charge restores a linear leak θ̄ = c₁ε with c₁ = 9–17 (E4).
  - Aligned control: J < 1e-15 (E5). Converged in Ls from 48 to 64 (E6).
- **R2 [F]** The bilinears the charge still allows leak at second order, θ̄ = c₂ε² with c₂ = 6–84. The dominant source is the bond currents Im φ*(r)φ(r + e).
  - Quality bound: ε = v/Λ < 1–4e-6 (E7). This is a dimension-6 effective Yukawa (φ†φ)φQX/Λ².
  - A lattice-scale order (ε = 0.2) gives θ̄ ≈ 0.24 (E3h FAIL).
  - At the electroweak scale θ̄ ~ 1e-31. Caveat: there even the unprotected control passes (1.8e-15), so the real protection is v ≪ Λ. The charge only lowers the required cutoff, from about 4e13 to 2e8 GeV.
- **R3 [F]/[T] (v3: PASS 7 / FAIL 0)** The same charge leaves the wrong-sector Yukawas φ_u*QD and φ_d*QU neutral, exactly as hypercharge does.
  - They leak at dimension 4 (c_w ≈ 5 at separation 0 and 230–610 at separation 4), so θ̄ < 1e-10 needs their strength below 2e-11 to 2e-13.
  - Forbidding both with a U(1) is possible iff that U(1) has a QCD anomaly, i.e. is a Peccei–Quinn symmetry (all 13³ charge choices checked).
  - An anomaly-free Z_N (N ≤ 12) that forbids both exists iff 3 | N. Every such Z_N leaves an accidental PQ symmetry in the renormalisable order potential, i.e. an electroweak-scale Weinberg–Wilczek-type axion, which is excluded (cited).
  - A PQ- and U(1)_H-invariant bond quartic still sources a T-odd component of the down order (ratio 0.46). The vacuum response was not computed.
- **Reading.** The D2r rule is not derived by a charge. What a charge buys is a quality bound v/Λ ≲ 1e-6. Removing the remaining dimension-4 leak needs PQ, and a working axion would solve strong CP on its own, making the mechanism redundant.
  - Two candidates were reasoned only, not computed. Lattice translations cannot separate the sectors, because φ and φ* carry the same momenta. Record/Admissibility constrain states, not which neutral operators appear.
  - Costs: two independent Higgs-type orders, and in this slab light order components at Γ and the three M points (eight doublets; FCNC and naturalness untested).

## Status and what remains open

- The octonion / F₈ / J₃(𝕆) carrier is not supported: O1, O5 and O6 fail, and the review found no payoff that survives. This is a failed search over the stated constructions, not an impossibility theorem.
- The misalignment mechanism gives an exactly zero tree-level θ̄ with generic J ≠ 0, for supplied Yukawas.
- On the slab it survives only if a **supplied rule** holds: T-odd orders must not enter other species' densities linearly.
- A charge on the orders derives the linear part of that rule. It leaves a second-order leak (quality bound v/Λ ≲ 1e-6) and a dimension-4 wrong-sector leak whose removal needs Peccei–Quinn, which would make the mechanism redundant (section R). As it stands, the mechanism is a Nelson–Barr-type construction with Nelson–Barr's quality problem, not a solution of it.
- It gives no hierarchy and nothing new for the mirror.
- Open checks: the vacuum response to the PQ-invariant bond quartic; a principle outside internal charges (e.g. a geometric separation of the two orders that suppresses wrong-sector Yukawas exponentially); FCNC from the extra order components at Γ and M.
- Strongest external falsifier of the principle: a θ̄-pattern nucleon or atomic EDM at θ̄ ≳ 10⁻¹², i.e. d_n ≳ 10⁻²⁸ e·cm.
- The type-I discrete groups Δ(27) and F₂₁ (no class-inverting automorphism: 0 of 432 and 0 of 42 checked) remain an untested alternative route to calculable CP.

Literature used as comparison only, not as premises:
- Nelson 1984; Barr 1984; Babu–Mohapatra 1990; Barr–Chang–Senjanović 1991.
- Feruglio–Hagedorn–Ziegler 2013; Chen–Fallbacher–Mahanthappa–Ratz–Trautner 2014.
- Dubois-Violette–Todorov 2018; Boyle 2020; Furey 2016–2018; Barnum–Graydon–Wilce 2020.
- Wang–Wen; Razamat–Tong; García-Etxebarria–Montero (SMG and Z₁₆).
- Running masses: Xing–Zhang–Zhou 2008.

## Provenance

- Proposal of the octonion carrier: coordinating session.
- Adversarial review, the misalignment proposal and parts A–D: one review agent at maximum reasoning effort. The coordinating session re-ran every part and reproduced every reported number.
- Part O6: written by the coordinating session.
- FREEZE and CL-1's tick are rebuilt from the twist-local-single / tick-winding construction code (same seed and draw order) with a numpy stand-in for scipy. They reproduce W_F = (−2, 1, 1). This is not an independent construction.
- The criteria files of parts D and E (both versions) predate their first runs. Disclosed post-hoc items: the M2 normalisation, X4, and the v2 model changes in R. The X4 J value was withdrawn by its author after a degeneracy check, which the coordinating session reproduced.

## Appendix: criteria fixed before the runs

Parts A–C (misalignment):
- A1: near-wall zero modes at the three X points only, 2 states each, Ls = 8, m = 3.
- A2: an antiunitary C·K with k → −k commutes with the slab, residual < 1e-10.
- A3: the C2 and translation family actions are real (entries ±1 to 1e-8) and at least one is non-scalar.
- B1: misaligned sectors give |sin θ̄| < 1e-10 in 100% of samples and median |J|/J_max > 1e-2.
- B2: aligned sectors give J < 1e-13.
- B3/B4: fewer than 0.5% of generic, Haar or incommensurate samples are θ̄-safe; Z₃ characters are 100% safe.
- C1: rank-1 and degenerate Yukawas from the single-site and uniform vertices.
- C2/C3: median s₁/s₂ ≥ 10 and s₂/s₃ ≥ 10.
- C4: the democratic term is compatible with a real non-scalar twist.

Part D (cross-talk), with Ls = 40, m = 2.5, κ = 1, 12 draws:
- D1: tree |sin θ̄| < 1e-12 and median |J|/J_max > 1e-3.
- D2: min over Δ ∈ [1, 18] and both orderings of median |θ̄_ind| < 1e-10.
- D2r: the same, with the supplied restriction.
- D3: aligned sectors give |J|/J_max and |sin θ̄| < 1e-12, at tree level and first order.
- D4: a generic complex vertex gives median |sin θ̄_tree| > 0.1.
- D5: Ls = 40, 48, 56 agree to a relative change < 1e-3.
- D6: twisted reality holds to 1e-12.
- D7: self-dressing shifts θ̄ by < 1e-12.

Part E (charged orders), with Ls = 48, U(1)_H on both orders:
- E0: every model term is U(1)_H-neutral; the control adds the charged linear terms.
- E1: tree |sin θ̄| < 1e-12 and median |J|/J_max > 1e-3.
- E2: the on-site |φ_u|² channel alone gives |θ̄_ind|/ε² < 1e-10.
- E3 / E3h: θ̄_ind < 1e-10 at ε = 1.03e-16 (electroweak) / ε = 0.2 (lattice scale).
- E4: the control shows a linear leak. E5: aligned orders give J, θ̄ < 1e-12. E6: Ls 48 → 56 change < 1e-3. E7: report c₂ and ε_max.
- v3: W1 wrong-sector terms neutral; W2 median c_w > 1e-2 (the principle fails to protect at dimension 4); W3 aligned control < 1e-12; S1–S3 symbolic charge scans; P1 bond-quartic source ratio > 1e-2.

Part O (fixed before running):
- O1 passes only if a group-invariant anticommuting 7-set exists.
- O5 passes only if some order-7 site permutation preserves |U(K)|.
- O6 passes only if ‖(1 − P) G V‖ < 1e-10 for some labelling × frame.
