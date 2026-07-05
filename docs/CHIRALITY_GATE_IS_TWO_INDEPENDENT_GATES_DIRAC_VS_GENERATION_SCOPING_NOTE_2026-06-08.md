# Dirac/Spinor Chirality Does Not Discharge Koide/Generation Chirality

**Date:** 2026-06-08; one-way Koide-gate scope repair 2026-06-10
**Claim type:** bounded_theorem / conditional finite algebra
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.py`](../scripts/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.txt`](../logs/runner-cache/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.txt)

**Claim boundary:** conditional tensor-product separation only. Given the
finite carrier `(generation R^3) ⊗ (L⊕R)` with `γ_5 = I_3 ⊗ σ_3`,
`β = I_3 ⊗ σ_1`, and `Γ_χ = (2/3)J-I` on the generation factor, the runner
proves that Dirac/spinor chirality and Koide/generation chirality are
independent gates. It does **not** derive this `γ_5` from the `Cl(3,1)`
extension, does **not** prove the spin-statistics use of that grading, does
not close or re-open the Koide generation-chirality gate, and does not touch the
firewalled `r=1/2`.

## Context

A recent keystone-collapse claim (the "massive Dirac field is ONE keystone" reduction
built on `cl3_to_cl31_spinor_extension`) asserts that the **chiral grading** is
discharged via a `Cl(3,0)→Cl(3,1)=M_4(ℝ)` doubling — modeled here only as the
supplied tensor-product operator `γ_5 = I_3 ⊗ σ_3` on a **separate** L/R factor — and observes (correctly) that the
`retained_bounded` `koide_z3_equivariant_anticommuting_no_go` is **narrow**: it forbids
only the *hybrid* `γ_CL = Γ_χ` on a single generation `R³`, **not** this separate-factor
`γ_5`. From this it asserts that the **Koide `Q=2/3` chiral-mass mechanism** and
**generation-ID** collapse into the same keystone.

This note bounds that inference. On the supplied tensor-product carrier,
`γ_5` is generation-blind, and the retained anti-commuting-operator route to
the Koide `Q=2/3` readout uses a generation-sector chirality that this `γ_5`
cannot supply. **"Not blocked by the narrow no-go" ≠ "supplied."** There are two
independent chirality requirements. The separate derivation of the `γ_5`
operator from `Cl(3,1)` and its spin-statistics role are outside this
restricted packet.

## The two gates

| | **Dirac/spinor chirality** | **Koide/generation chirality** |
|---|---|---|
| operator | `γ_5 = I_3 ⊗ σ_3` on `(gen R³) ⊗ (L⊕R)` | a generation mass operator `M_gen` on `R³` |
| requirement | anticommutes with the Dirac mass `β` (L↔R) | `{M_gen, Γ_χ} = 0`, `Γ_χ = (2/3)J − I` |
| source | supplied tensor-product grading in this runner; `Cl(3,1)` derivation not claimed here | the retained one-way anti-commuting-operator route: an anticommuting generation mass operator supplies the chiral Koide `Q=2/3` readout used here; no converse/completeness direction is consumed |
| needed for | Dirac/spinor L/R algebra in this restricted packet; spin-statistics use not claimed here | the charged-lepton `Q=2/3` mass spectrum |

## The separation (verified, `PASS=16`)

1. **`γ_5` is genuine for Dirac/spinor chirality.** `γ_5² = I` and `{γ_5, β} = 0` for the Dirac mass
   `β = I_3 ⊗ σ_1` — a real L↔R chiral mass coupling on the supplied finite
   tensor-product carrier.
2. **`γ_5` is generation-blind.** `γ_5 = I_3 ⊗ σ_3` acts as the **identity** on the generation
   factor, so it **commutes** with *every* generation-sector operator `G ⊗ I_2` — in particular
   `[γ_5, Γ_χ ⊗ I] = 0`. The Dirac mass `β` likewise commutes with `Γ_χ ⊗ I`. Neither
   contributes anything to `{M_gen, Γ_χ}`.
3. **Koide/generation chirality is not supplied — it needs a C₃-breaking operator.** The finite
   algebra checks the local obstruction directly: no nonzero symmetric
   generation operator both commutes with the C₃ generator `R` and anticommutes
   with `Γ_χ`. Nonzero symmetric solutions to `{M_gen, Γ_χ}=0` exist only off
   the C₃-equivariant locus, so a C₃-trivial (`I_3`) spinor grading like `γ_5`
   cannot produce the needed generation operator.

**Conclusion:** the Dirac/spinor and Koide/generation chirality requirements
are independent commuting gradings on the supplied tensor product. The supplied
`I_3 ⊗ σ_3` grading handles the Dirac/spinor L/R algebra; the
Koide/generation chirality requirement remains open on the generation `R³`
factor — a C₃-orbit-splitting `M_gen` that no spinor-factor chirality reaches.

## Relation to existing work

This sharpens, and is consistent with, the existing flavor-emergent
chirality transport note (unaudited), whose candidate table already finds
the `γ_CL = I_3 ⊗ σ_3` grading **INERT** on
the generation factor (`{G⊗σ₁, I_3⊗σ₃}=0` for every `G` → zero constraint there). The added
content here is the explicit **two-gate** framing grounded in the one-way
anti-commuting-operator algebraic input from
`koide_anticommuting_operator_derivation` (not only the unaudited transport note), and the
precise **"not blocked ≠ supplied"** scope-bound on the separate-factor `Cl(3,1)` keystone claim.

Authorities / inputs:
[`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
(retained),
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
(retained_bounded),
[`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)
(retained, cited only as context for the keystone claim; the restricted theorem
does not use it to derive `γ_5` or spin-statistics).

## Scope / verdict

- The conditional tensor-product separation is sound: the supplied
  `I_3 ⊗ σ_3` grading handles the Dirac/spinor L/R algebra while remaining
  generation-blind.
- It does **not** discharge the **Koide `Q=2/3` / generation-ID chirality**, which
  remains the open generation-`R³` C₃-breaking requirement on the retained
  one-way anti-commuting route. This note does not claim the converse that
  every `Q=2/3` realization must arise from `{M_gen, Γ_χ}=0`.
- It does **not** derive the separate L/R `γ_5` from the `Cl(3,1)` extension and
  does **not** prove spin-statistics use of that grading.
- No new axiom or import; no PDG load-bearing. The independent audit lane owns any status.
