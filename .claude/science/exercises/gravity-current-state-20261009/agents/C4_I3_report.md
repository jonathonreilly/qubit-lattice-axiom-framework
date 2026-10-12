# Lane RI, probe I3: can the Z³ grid itself supply the band tower (coarse cells of L³ qubits)?

Worker: Claude Opus 5.5 (same family as the supervisor). Run 16:22Z–16:45Z, 2026-10-11. No repository files were edited. Nothing here is refereed.
Scratch: `.../scratchpad/C4/I3/`. Scripts and outputs: `i3_cubic_designs.py/.out`, `i3_radial_designs.py/.out`, `i3_superlattice_sumrules.py/.out`, `i3_readout.py/.out`, `i3_sunset_speed.py/.out`.

## Reading against the FIXED lines (lane RI; I3 is one leg of FAIL)

The relevant FAIL leg is: "the coarse-cell route (I3) leaves a lattice-scale anomaly or TT response that does not fall with L."

**I3 finds the anomaly leg met, and the TT leg met only in a qualified form.**

- **The C3 anomaly does not fall with L (proved).** For every finite-band periodic network, at every L and with any couplings, the zone-mean boost anomaly is exactly −1 per mode. The vacuum-weighted anomaly per mode is ≤ −1. The anomaly weighted by the TT loop measure is −0.399 in the radial coarse-cell family, independent of L.
- **The TT response falls, but only dimensionally.** The free one-loop linear-only μ falls as L⁻⁴, which is just the stress-carrying cutoff π/ℓ to the fourth power (checked to 6 digits). With the RN L1 unitary seagull, μ is exactly 0 at every L.
  - Reaching P0 by this law needs L* ≈ 6.7e24. That puts the relativistic matter cutoff at about 1 keV, which contradicts relativistic matter observed at ≥ 10 TeV (reading).
  - With the cubic per-axis flattening, the falls are slower: L⁻² (E) and L⁻³ (T2).
- **Lattice-scale modes in loops still feed Lorentz violation into the low band, without falling with L (checked at O(λ²), onsite φ⁴).**
  - With internal modes at the fine scale, the low band's speed shift is about −2.0e-5 λ², independent of L. The plain fine lattice gives −1.15e-5 λ².
  - With internal modes flattened at the coarse cutoff, the shift grows as L⁶ (strong coupling).
  - Free-level decoupling (Carroll-flat bands) exists, but interactions undo it.
- I3 alone cannot give the lane a FAIL; that also needs I1. No PASS is in sight from I3: nothing exact appears beyond the free-level constructions in §5.

## 1. What coarse cells buy (proved / checked)

**Folding is a relabelling (proved).**
- Cutting a uniform fine lattice into L³ cells and calling the fine modes "internal bands" changes nothing. The superlattice bands are the fine band folded.
- Checked: the 1D chain with J_in = J_out reproduces the fine chain (`i3_superlattice_sumrules.out`).
- The IR anomaly is still set by a, A = u″ − 1 ≈ −(ka)²/2. Coarse cells buy something only if the network is designed.

**Designed dispersions (checked).**
- Taylor-improved stencils of range r give A = O(k^{2r}) in the IR. A(π) = −2, −8/3, −16/5, −128/35, −256/63, matching the C3 referee.
  - μ grows with r: |μ_T2| = 0.0118, 0.0248, 0.0343, 0.0414, 0.0470 for r = 1–5.
  - So the anomaly moves to the UV; it is not removed.
- **Radial C^∞ coarse design.**
  - Definition: ω² = |k|² exactly for |k| ≤ κ = π/ℓ; a C^∞ step; flat for |k| ≥ 2κ.
  - Inside the ball, A ≡ 0 exactly. So the C3 anomaly operator Σ_k (u_cc − 1) ω_k n_k annihilates every state built from modes with |k| < π/ℓ. Only the c-number vacuum part of §3 remains, and a constant shift of H removes it.
  - Shell modes have ω ≥ κ. So any on-shell process with total energy below π/ℓ stays in the ball, where the C3 anomaly is zero. **The coarse-cell question therefore reduces exactly to loops (virtual shell and flat modes).**
  - Cost: the symbol is C^∞ but not analytic. Its Fourier tails fall faster than any power but not exponentially, with range ~ℓ. It is realizable only approximately by finite networks (RC C1 / RG G2 type convergence, inexact at any finite depth).

## 2. Sum rules: the anomaly can be moved, never removed (proved)

**(S1) Zone sum rule.** For any smooth periodic single band, ∫_BZ ∂_c²u = 0. For any finite-band ℓ-periodic network, Σ_n ∫_cBZ ∂²u_n = ∫ ∂²(½ Tr K(q)) = 0. This holds through band crossings, because Tr K is smooth.
- So the equipartition-weighted (high-T) band-diagonal anomaly is exactly −1 per mode, for every L.
- Checked to ≤ 1e-16 for all designs and all superlattices (L = 2–16, both weak- and strong-cell couplings, and the projector construction).

**(S2) Vacuum weight.** Integrating by parts on the torus:

  ∫ u_cc ω = −∫ ∂_cu ∂_cω = −∫ ω(∂_cω)² ≤ 0.

- So the zero-point-weighted mean of u_cc is ≤ 0, and the vacuum-weighted anomaly per mode is ≤ −1, for every periodic band. It vanishes only for a dispersionless (Carroll) band.
- Checked band by band on superlattices (IBP matches to all printed digits).

**(S3) The low band is itself a lattice at scale ℓ.** In every superlattice the acoustic band's own zone-mean anomaly, in units of its IR c², is −1.0000 (checked). Coarse cells move the C3 anomaly from a to ℓ.

## 3. New identity: the C3 vacuum anomaly is the vacuum's ρ + p (proved for one band; checked)

The C3 boost bracket has anomaly operator E_c − H = Σ_k (u_cc − 1)·ε_k. Write:
- ρ = ½⟨ω⟩ per site;
- p_c = ½⟨(∂_cu)²/ω⟩ = ½⟨ω(∂_cω)²⟩ per site. This is the vacuum pressure from the flow-defined linear stress coupling, in RN L1's normalization.

By (S2):

  **⟨E_c − H⟩_vac per site = −(ρ + p_c).**

- **Checked:** residual ≤ 1e-14 for NN, the improved stencils and naive bosons; ≤ 1e-11 for the C^∞ designs (numerical step derivative).
- **Meaning:**
  - The lattice vacuum's Poincaré anomaly is exactly its departure from w = −1.
  - For bosons p ≥ 0, so the vacuum is never Lorentz-invariant (ρ + p ≥ ρ > 0).
  - A cosmological-constant counterterm shifts (ρ, p) by (Λ, −Λ) and cannot remove this.
  - Removing it takes a frame-dependent ("dust") c-number counterterm, i.e. one more natural-size tuning.
- **Comparator** (recalled, not re-fetched): hard-cutoff vacua have w = 1/3 instead of −1 (Akhmedov hep-th/0204048; Koksma–Prokopec arXiv:1105.6296).
- **Multi-band:** only the band-diagonal part is checked. Interband terms of E_c are not computed.

## 4. Induced zero-momentum TT response vs L (checked)

Free scalar, one loop, linear coupling only (RN L1 normalization μ = −⅛⟨X²/ω³⟩, X = h_ij∂_iu∂_ju), per fine site, m = 0.
- **Control:** NN gives μ_E = −3.69453e-3 and μ_T2 = −1.17819e-2, reproducing RN L1 and its referee.

| Design | μ_E | μ_T2 | p_x | ρ | Loop-weighted A (T2 measure) |
|---|---|---|---|---|---|
| NN | −3.69e-3 | −1.18e-2 | 0.110 | 1.194 | −0.807 |
| Separable-flat, L = 64 | −1.21e-5 (∝ L^−2.01) | −5.74e-7 (∝ L^−3.03) | 1.5e-4 (∝ L^−2.01) | 0.064 (∝ L^−0.99) | −0.797 |
| Radial-flat, any L | −0.13473 L⁻⁴ (both channels; isotropic) | same | 0.857603 L⁻⁴ | 2.3702 L⁻¹ | **−0.399 at every L** |

- In the radial family μL⁴, p L⁴ and ρL are constant to 6–7 digits from L = 64 to 4096. The family is self-similar (ω_L(k) = κΩ(k/κ)), so every dimensionless quantity of the stress-carrying sector is exactly L-independent. **The only fall is dimensional.**
- The per-axis (cubic) flattening falls more slowly. Modes soft along one axis but flat along the others still carry stress.
- **With the RN L1 unitary seagull** (H(h) = U_h H U_h†, a complete smooth flow for every design used here), μ_E = μ_T2 = 0 exactly at every L (proved by isospectrality). At the free level, μ is completion data, not a forced number. That matches the RN L1 and G3 referees.

## 5. Can the UV modes be decoupled or cancelled? (the hard question)

**(a) Gap them, keeping dispersion.** Gapped dispersive bands carry stress, so they contribute natural-size μ, p and an induced graviton kinetic term. They also carry the full (S1) and (S2) deficit. No decoupling.

**(b) Make them non-propagating (flat, "Carroll").** This is the only free-level decoupling found.
- Flat bands have ∇u = 0. So they carry no momentum and no stress (T_ij's q→0 symbol is ∂_iu∂_ju). They give exactly 0 to μ (any completion), to p, and to the induced TT kinetic term.
- An explicit finite-range network exists: K = M²(1 − Π) + ΠK_cΠ, with Π the cell-uniform mode (range ~2L). Its L³ − 1 internal bands are exactly flat at M; checked.
- **But:**
  - (i) Every Carroll quantum carries the maximal boost anomaly, A = −1.
  - (ii) Its zero-point energy enters ρ with p = 0. The vacuum anomaly ρ + p is then 2.37/L per fine site if the flat modes sit at the coarse cutoff, and M/2 per mode (not falling) if they are gapped at fixed M.
  - (iii) This is a period-L superlattice. A fine-translation-covariant rule (Admissibility) gives it only as a spontaneously ordered state, or else the fine-translation-invariant radial design must be used.
  - (iv) The Carroll modes sit on the same qubits as the low band, so generic interactions couple them to it. See §6.

**(c) Remove them.** Every fine site holds a qubit, so the modes exist. "Removed" can only mean "gapped" or "flat" (cases a and b). Truly removing them is a coarse lattice, which by scaling has μ = μ_NN L⁻⁴ (identical to the radial law).

**(d) Bose–Fermi pairing (proved, at construction level).**
- Setup: one complex boson and one two-band fermion with |ε(k)| = ω(k), both coupled through the same flow.
- E₀_B(h) + E₀_F(h) = 0 for every h. So ρ, p, the vacuum anomaly and μ cancel mode by mode, for any dispersion and any L.
- Realizable on the lattice at the free level: e.g. ω² = m² + Σ sin²k_i, paired with naive or staggered fermions. The price is bosonic doublers. This is consistent with T0's +K⁴/120π² per boson and −K⁴/60π² per Weyl sea.
- **Limits:**
  - The operator anomaly Σ(u_cc − 1)ε_k n_k on real quanta has the same sign for both statistics and does not cancel.
  - Interactions break the pairing (suggested). The Kato–Sakamoto–So Leibniz no-go (0803.3121) is precisely the no-go for exact interacting lattice SUSY, the same obstruction that underlies C3.

**(e) Spectral sum rule.** (S1) is the opposite of a cancellation: it fixes the total curvature deficit at exactly one per mode. The best possible placement is in stress-free Carroll modes, which is case (b).

## 6. Interacting loops: the Carroll modes feed Lorentz violation back (checked at O(λ²))

Below π/ℓ, real processes see A = 0 exactly in the radial design (§1). The anomaly can enter only through virtual shell and flat modes, which is the Collins–Perez–Sudarsky mechanism.

**Computation** (`i3_sunset_speed.py/.out`).
- Model: onsite φ⁴ on the fine grid.
- Quantity: the O(λ²) sunset contribution to the low band's speed² at p → 0,
  δc²/λ² = (I_x − I_t)/12, with I_x = ∫dτ Σ_x x₁²D³ and I_t = ∫dτ Σ_x τ²D³.
  A Lorentz-invariant regulator gives I_x = I_t.
- Setup: self-similar mass m = κ/2; box N = 8L.

| Design | L = 4 | 6 | 8 | 12 | 16 | Law |
|---|---|---|---|---|---|---|
| NN fine lattice (m = 0.5), baseline | −1.15e-5 | | | | | |
| Radial-flat (Carroll modes at the coarse cutoff) | −4.4e-4 | −4.7e-3 | −2.6e-2 | −0.30 | **−1.67** | **∝ L^5.95** |
| Radial-gapped (Carroll modes at the fine scale, M = 2) | −2.60e-5 | −2.41e-5 | −2.29e-5 | −2.19e-5 | −2.16e-5 | → about −2.0e-5, **L-independent** |

- **Mechanism (checked).** Flat modes are local in x. So they feed the τ² moment I_t but not the x² moment I_x. I_x of the ball is exactly L-independent (1.02623e-5, self-similar). I_t matches the Carroll estimate 1/(54 ω_flat⁶) to < 1% for L ≥ 8.
- **Reading.**
  - Carroll modes placed at the coarse cutoff are soft and dense: about one per fine site, with ⟨φ²⟩ ∝ L. Fine-scale interactions make them strongly coupled, and the loop speed shift grows as L⁶.
  - Self-consistently (suggested), the interactions lift them to the fine scale λ^{1/3}. That is the gapped case.
  - There the loop-fed speed shift is natural size, L-independent, and about 2× the plain fine lattice's.
- **So no coarse-cell design reduces the loop-fed Lorentz violation of the low band.** At best it is L⁰ × natural. Decoupling would need the internal modes' couplings to the low band to be suppressed (for |δc| ≲ 1e-15, λ ≲ 1e-5 to 1e-6): a further tuning of the rule, not a consequence of the cell.
- **Also suggested:** the onsite tadpole from Carroll modes at the coarse cutoff gives δm²/κ² ∝ λL³.
- **Not computed:** the O(λ²) μ (RN L2 basketball) in the radial and projector designs; species speed splits (T1-type) in these designs.

## 7. Readout Q-RI (conditional on the linear-only completion; with the seagull there is no μ to suppress)

| Quantity | Law (relative to fine natural) | L* at 5.7e-99 (refereed) | L* at 9.0e-102 (framework) |
|---|---|---|---|
| μ, radial flat | 11.43 L⁻⁴ | **6.7e24** | 3.4e25 |
| p (vacuum pressure), radial | 7.80 L⁻⁴ | 6.1e24 | 3.1e25 |
| μ_E, separable flat | 13.4 L⁻² | 4.8e49 | 1.2e51 |
| μ_T2, separable flat | 12.8 L⁻³ | 1.3e33 | 1.1e34 |
| Vacuum anomaly incl. Carroll zero-point at the coarse cutoff | 1.99 L⁻¹ | 3.5e98 | 2.2e101 |
| Same, internal gap fixed at M | L⁰ | none | none |
| Relative (per-mode) anomaly | L⁰ (−1; −0.399 loop-weighted) | none | none |
| O(λ²) loop-fed low-band speed shift, internal modes at the fine scale | L⁰ (about −2.0e-5 λ²) | none | none |
| Same, Carroll modes at the coarse cutoff | grows as L^6 | none | none |

- **Converting L*** (reading; reduced Planck cell 8.1e-35 m): L* = 6.7e24 gives ℓ* ≈ 5.4e-10 m, a relativistic band ending at about 1.1 keV.
- **Observational cap** (reading): relativistic matter observed at ≥ 10 TeV needs L ≤ 7.7e14.
  - At that cap, the best (radial) μ is still ≥ 3.3e-59 of natural, about 40 orders above P0.
  - Separable designs give ≥ 2.3e-29 (E channel).
- This is the cosmological-constant scaling Λ⁴ applied to the TT sector. Coarse cells do not change it.

## 8. Against the supervisor's expectation

The expectation was: "the coarse-cell route is the ordinary continuum limit … lattice-scale modes in loops still carry an order-one zone-averaged anomaly, so the induced TT response does not fall with L."

- **Confirmed:** the order-one per-mode anomaly ((S1), (S2), the L-independent −0.399), and that coarse cells are a change of units for the stress-carrying sector.
- **Corrected in two places:**
  - (1) The free TT response does fall, as L⁻⁴ (dimensional). The expectation's "does not fall" holds only relative to the coarse natural scale.
  - (2) Lattice-scale modes can be decoupled exactly from the free TT sector by making them Carroll-flat. The anomaly then sits in the Carroll modes' energy (ρ + p ≠ 0) and in their interactions, not in μ.
- **Not foreseen:** the identity ⟨E_c − H⟩_vac = −(ρ + p_c). It ties C3's anomaly to the vacuum's w ≠ −1.
- **Also not foreseen:** the specific failure of the Carroll decoupling under interactions. Carroll modes are local, so they feed only the time-derivative term, and the speed shift is L⁰ or grows as L⁶ (§6).

## Labels, assumptions, scope

- **Proved** (same family, unrefereed):
  - folding is a relabelling;
  - (S1) and (S2);
  - the vacuum identity (single band);
  - exact A = 0 inside the radial ball, and the energy-confinement argument;
  - flat bands carry no stress and no momentum;
  - seagull μ = 0;
  - Bose–Fermi c-number cancellation;
  - self-similar scaling.
- **Checked:** every number in §§2–4, §6 and §7. That includes the O(λ²) sunset speed shifts and the Carroll estimate 1/(54ω_flat⁶).
- **Suggested:**
  - the L³ growth of Carroll tadpoles;
  - the self-consistent lifting of Carroll modes to the fine scale;
  - interactions breaking B–F pairing;
  - L-independence of the loop LV in the L → ∞ limit of the gapped design. The fitted limit is about −2.0e-5 λ² from L ≤ 16; this is a short extrapolation.
- **Assumptions:**
  - free real scalar;
  - C3's anomaly symbol (Hess u − δ)·ε_k, multi-band band-diagonal only;
  - the flow-defined linear stress coupling of RN L1, X = h_ij∂_iu∂_ju. For non-separable designs this is the Ward-identity coupling, not a constructed local stress.
  - P0's B and the conversion to physical units are as in PRICE_NOTE.
- **Not covered:**
  - interband anomaly terms;
  - the O(λ²) μ in the coarse designs;
  - non-perturbative or interacting Carroll couplings;
  - staggered fermions;
  - the O(q²) induced graviton kinetic term and its speed;
  - fine-translation-breaking ordered states as a legitimate realization under Admissibility.
