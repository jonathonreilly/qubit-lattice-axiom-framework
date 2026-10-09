# Route agent R4: the misframing lens

**Agent:** Claude Opus 5.5, extra-high (xhigh) effort.
**Refresher read (stated):** the full axioms, the primitive registry check, `axiom_premise_nodes.json`, all three primitive source notes, the pack's K3a/K3a″/W1/W2 sections with their referee verdicts, the 09-29 misframing agent, and the landed CC, graviton-mass, Weyl-stress and proper-cubic-group notes.
**Scripts:** `scripts/R4_c1 … c5` with their outputs.

## Verdict

**The wall is not misframed in substance.** Of eight candidates examined, four fail under checks. Two framing defects are real, but fixing them leaves the wall in place.

## Item 1: granting the cosmological constant does not cover the shear tuning (ledger S6)

- **PROVED.** The CC zero-point problem is unsolved on the framework's own surface (`docs/COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md`). Read literally, the target's no-counterterm clause fails at the CC for every candidate.
- **EXACT/CHECKED (c1).** Under the 24 proper rotations, constant metrics have three quadratic invariants: trace², μ_E and μ_T. There is no trace–shear cross term (Schur). So a trace-only mechanism cannot move μ_E or μ_T.
- **EXACT (c1), the fluid lemma.** If E depends on g only through det g, the shear Hessian is identically 0 in the volume-preserving chart. Tuning the CC then tunes the shear automatically, in a fluid but not in a cubic solid.
- **EXACT (c1).** A change of chart, or any rotation-scalar term, shifts μ_E and μ_T equally. The difference δ = μ_E − μ_T is invariant.
- **CHECKED on refereed numbers.** μ_E = −0.01303 and μ_T = +0.01247 (+0.01337 with the universal rule) have opposite signs, so no common shift zeroes both. The best one leaves 0.0127·e² per cell. The O(e²) wall is about 90% cubic anisotropy, provided both channels share one normalization.
- **CHECKED (c3).**
  - The LVK shear bar is about 5e-105 per Planck cell. The CC bar is about 1e-123.
  - On the landed conditional identity m_g² = 2Λ (`GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`), the two bars are equal.
  - Only boson–fermion pairing mode by mode (SUSY-like) clears both. Pairing broken at a TeV leaves about 4.5e-65 per cell, roughly 40 orders short (ARGUED scaling).

**Route: the CC-granted shear gate.**
- **The family.** E_vac(g) on constant metrics, with invariants μ_iso and δ. Its obligation is a named mechanism that zeroes μ_E and μ_T after the tadpole is tuned.
- **First artifact.** Free-level per-species (μ_E, μ_T) vectors for K3a″'s fields.
  - **PASS:** the vectors are collinear and opposite, so some integer species count cancels both channels.
  - **FAIL:** they are not collinear.
- **Cost.** One day.
- **Gap test.** Weaker than the target. Blocked-equivalent for trace or scalar mechanisms.

## Item 2: the fixed window comes from translations, not adjacency (ledger L1, S4, S7)

- **EXACT/CHECKED (c5), a free counterexample.**
  - Relabel the Brillouin-zone torus by a volume-preserving map φ_a, and take H = σ·s(φ_a⁻¹k).
  - The sea energy is constant (to 2e-6), while the low-energy dispersion matches the strained nearest-neighbour law, whose d²E/da² is −1.17 per cell.
  - The price: hopping beyond nearest neighbours (range-3 amplitude 8e-5) and a non-additive φ.
- **EXACT, Lemma R.** Take H₀ interacting and translation-covariant on Z³, with a translation-invariant vacuum and no continuous translations, and suppose H_h = U_h H₀ U_h† is translation-covariant and continuous in h.
  - Then U_h† T_a U_h = T_{A·a} × (an internal symmetry), with A ∈ GL(3,Z), and continuity forces A = 1.
  - So U_h preserves crystal momentum and every one-particle dispersion: the strain is unfelt.
  - **So "embedding, cutoff and measure move together" cannot be an exact symmetry of an interacting law.** It exists only at the free level.
- **CHECKED (c4).** Moving the matter cutoff below the lattice scale does not help. In a dilute lattice Bose gas, the shear Hessian divided by the interaction energy stays at 0.0300, matching −U·W″/2. The imprint enters through the lattice's renormalization of the coupling.
- **PROVED.** The axioms' point group is the 24 proper rotations, with no boost (`PROPER_CUBIC_GROUP_IS_24_AND_CONTAINS_NO_BOOST_..._2026-08-13.md`). So no Lorentz Ward identity ties the shear numbers to the tadpole.

**Route: the translation-pinned window.**
- **What it changes.** L1 sharpens to "Z³ translations are unbroken by the vacuum".
- **What you would have to believe.** That some Z³-breaking realized state is shear-free. Crystals, glasses and density waves are not; smectics zero only some moduli (COMPARATOR).
- **First artifact.** A 2D toy: fermions in an incommensurate sliding density wave against a commensurate one.
  - **PASS:** μ_E and μ_T → 0 with incommensurability.
  - **FAIL:** they stay O(1) (expected).
- **Cost.** 2–3 days.
- **What it means.** Dynamical adjacency (option B) helps **only if it breaks Z³ in the vacuum**, or protects without a symmetry. **Adjacency itself is not what bears the load.**
- **Gap test.** For symmetry protection, the stiffness face is blocked-equivalent to "an interacting, translation-invariant vacuum with discrete translations".

## Item 3: candidates rejected

| Candidate | Why it fails | Label |
|---|---|---|
| P2 (a = l_P not derived) | With an independent Planck mass the grid would need a⁻¹ < 562 eV, below the electron mass. With an induced Planck mass, m_g ≈ 0.2/a at any a | CHECKED (c3) |
| The target is too strong | The same 10¹⁰¹ tuning either way | CHECKED |
| S2 (mass = TT Hessian) | Correct for an independent metric at a stationary background, and δ does not depend on the chart. **Reading: after the free part is tuned, K3a″'s axis channel is negative, which makes the graviton tachyonic in that channel** | EXACT; READING |
| S3/S4 (perturbative vacuum) | The axioms' group has no protecting symmetry: 2 invariants, no boost | EXACT count |
| S5 (gravity as a local wave mode) | Data require a propagating low-energy TT mode (GW170817, binary pulsars, tensor polarizations) | COMPARATOR |

**Prior art.** The two-number count is known (TEST_LOG; 09-29 agent 4), and the free sea's nonpositive response is landed (`NATIVE_WEYL_STRESS_..._2026-09-13.md`). The following are new: the trace closure of C3, the chart invariance of δ, Lemma R and the free counterexample, the dilute-medium imprint, and the equal-bars observation. All are unrefereed.
