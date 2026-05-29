# Flavor Frontier Map — form unified, values imported (Cl(3)/Z³)

**Date:** 2026-05-29
**Claim type:** frontier map / honest status synthesis (NOT a derivation, NOT
a promotion). Imports nothing as derived; sets no retained status (audit
lane decides). Conditional/mapping analysis.
**Runner:** `scripts/flavor_frontier_form_vs_value_2026_05_29.py`;
cache `logs/runner-cache/flavor_frontier_form_vs_value_2026_05_29.txt`.
**Source:** 8-lens flavor frontier panel (`wf_80271397`), 7/8
reparametrization-trap, 0/8 share the Koide import. Continuation of the
charged-lepton Koide campaign (PR #2162), which established Koide = the
flavor problem localized.

## One-line verdict
**The framework UNIFIES the FORM of the entire flavor sector on a single
shared, genuinely-derived C₃-corner scaffold, but does NOT reduce its
continuous VALUES — ~4–6 independent S₃-breaking value-imports, ~20 → ~20
continuous parameters. The Koide pattern writ large: re-parametrization,
not reduction.**

## (a) The shared C₃-corner scaffold is real and retained
All three sectors live on the *exact* C₃ coordinate-cycle symmetry of Z³,
projected onto the hw=1 corner triplet via the cyclic operator `C` (`C³=I`):
- **Koide** (`koide_circulant_character_bridge`, retained): `H=aI+bC+b̄C²`
  forces the biconditional `a₀²=2|z|² ⟺ 3a²=6|b|² ⟺ r=½`. Form forced; `r=½` free.
- **CKM** (`ckm_inverse_square_structural_sum_rule`,
  `wolfenstein_lambda_a_*`, `ckm_cp_phase_*`, all retained;
  `ckm_moduli_only_jarlskog_area_certificate`, retained_bounded): sum rules,
  magnitude closed forms, CP-phase identity, moduli-only Jarlskog certificate.
- **PMNS** (`pmns_oriented_cycle_channel_value_law`, retained): the
  forward-cycle operator `C = P_hw1† U_C3² P_hw1` is *projected from the
  exact C₃ unitary, not introduced by hand*; native edge basis E₁₂,E₂₃,E₃₁;
  plus `pmns_graph_first_residual_antiunitary` (retained CP locus).

This is a genuine, novel-in-provenance gain: a **derived** (not postulated)
residual-C₃ family-symmetry / texture scaffold — literature-comparable to an
A₄/S₄/Froggatt–Nielsen-class ansatz, but with the C₃ derived from the substrate.

## (b) But it is re-parametrization, not reduction — the import count is ~4–6
Granting the single charged-lepton chiral grading (`r=½`) does **not**
propagate to other sectors' values; the imports live on different
moduli/factors:

| Sector | Form derived (retained) | Value import | Shares Koide import? |
|---|---|---|---|
| charged-lepton (3 m) | `Q=2/3 ⟺ r=½` biconditional | `r=½` grading + scale | — (is the import) |
| CKM (4) | A²=2/3, ρ=1/6, η²=5/36, δ=arccos(1/√6), Jarlskog cert. | α_s (sources λ) + counts (2,3,6) | **NO** |
| up quarks (3 m) | RPSR → one scalar | 2 free readout exponents (p,q) | NO (`retained_no_go`) |
| down quarks (3 m) | ratio laws | 2 CKM-coupled bridges (bounded) | NO |
| PMNS (3 ang+φ) | native oriented-cycle basis; antiunitary CP | (s₁₂²,s₁₃²); c_i **unselected** | NO |
| neutrino mass | atmospheric-scale form (bounded) | abs. scale + Majorana phases | open |

`quark_c3_circulant_source_law_boundary` (retained_no_go) proves it: even
granting Koide's grading (`3a²=6|q|²`), each quark sector leaves scale,
hierarchy-phase, readout, and up/down species-map free. **A1 does not propagate.**

Honest net continuous-parameter count: **~20 → ~20.** Genuine cuts are
**discrete only**: `n_gen=3`, `n_color=3` from C₃/hw=1 geometry.

## (c) The recurring 2/3 is TWO distinct objects
- Koide `2/3 = 2/d` (d=3 gen rep) — a continuous **weight-ratio** modulus (⟺ r=½).
- CKM `A² = 2/3 = n_pair/n_color` — an integer **count ratio** (perp weight `2/n_color²=2/9`).

Numerically coincident only at `(n_pair,n_color)=(2,3)`; algebraically distinct.
There is no single "2/3 object" unifying the sectors.

## (d) The strongest single result (genuine, falsifiable)
**CKM CP angle:** `cos²δ = 1/n_quark` ⟹ `δ = arccos(1/√6) = 65.9°`,
**r²-independent**, matching PDG `γ = 65.7 ± 3.0°` to **0.07σ** with zero
continuous tuning — a pure function of one integer. A real structural
prediction of the *angle*. (Caveat: a free readout of an already-imported
(1+5) projector split, not a new continuous-parameter reduction.)

## (e) The unifying obstruction — one wall, six masks
The **counting-vs-splitting tension generalized**: the same C₃ orbit that
delivers the discrete wins (`n_gen=3`, `n_color=3`, the count tuple) forces
*circulant/equivariant* operators that **commute** with the grading and
therefore cannot pin any *continuous* modulus (`r=½`, the λ-scale via α_s,
the PMNS c_i, the quark hierarchy-phase). Every continuous flavor value sits
in the orbit-**breaking** direction the discrete structure cannot reach.

## (f) Most valuable next step
Test whether a **single product-grading** on `H = R³(gen) ⊗ taste ⊗ (H_L⊕H_R)`
— one chiral grading that breaks the C₃ orbit — *simultaneously* fixes `r=½`
(Koide), the quark hierarchy-phase, AND the PMNS active-block selection.
If ONE orbit-breaking import demonstrably fixes values in ≥2 sectors, the
framework converts from form-unification to genuine reduction. Decisive
computation: does its order-one/J-reality condition pin `b/a=1/√2` (=r=½)
*and* propagate? Until then the imports are provably independent.

## Status
Frontier map. The framework's flavor contribution is **structural**
(correlations/sum rules/native bases) and **discrete** (n_gen=3, n_color=3),
not numerical. No continuous-parameter reduction; ~4–6 independent imports +
an open quark-mass sector (`quark_mass_spectrum_koide_scheme`, open_gate).
No false closure.

## Ledger verification (this session, origin/main)
retained: `koide_circulant_character_bridge`, `ckm_inverse_square_structural_sum_rule`,
`ckm_cp_phase_*`, `wolfenstein_lambda_a_*`, `pmns_oriented_cycle_channel_value_law`,
`pmns_graph_first_residual_antiunitary`. retained_bounded:
`ckm_moduli_only_jarlskog_area_certificate`, `pmns_tm2_magnitudes_conditional`.
retained_no_go: `quark_rpsr_single_scalar_readout_underdetermination`,
`quark_c3_circulant_source_law_boundary`. open_gate:
`quark_mass_spectrum_koide_scheme`. audited_conditional (NOT retained):
`cross_sector_a_squared_koide_vcb_bridge`. The parent value-supplying notes
(`ckm_cp_phase_structural_identity`, `wolfenstein_lambda_a_structural_identities`,
`koide_circulant_character_bridge` parent, `pmns_oriented_cycle_reduced_channel_nonselection`)
are unaudited.
