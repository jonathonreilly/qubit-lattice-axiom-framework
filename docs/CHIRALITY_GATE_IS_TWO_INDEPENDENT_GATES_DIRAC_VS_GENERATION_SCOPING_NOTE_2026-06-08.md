# Dirac/Spinor Chirality Does Not Discharge Koide/Generation Chirality

**Date:** 2026-06-08
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.py`](../scripts/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.txt`](../logs/runner-cache/chirality_gate_two_gates_dirac_vs_generation_2026_06_08.txt)

**Claim boundary:** bounds a recent keystone-collapse claim to its sound scope.
It does not close, and does not re-open, the Koide generation-chirality gate.
It does not touch the firewalled `r=1/2`.

## Context

A recent keystone-collapse claim (the "massive Dirac field is ONE keystone" reduction
built on `cl3_to_cl31_spinor_extension`) discharges the **chiral grading** via the
retained `Cl(3,0)→Cl(3,1)=M_4(ℝ)` doubling — the 4-component Dirac bispinor with
`γ_5 = I_3 ⊗ σ_3` on the **separate** L/R factor — and observes (correctly) that the
`retained_bounded` `koide_z3_equivariant_anticommuting_no_go` is **narrow**: it forbids
only the *hybrid* `γ_CL = Γ_χ` on a single generation `R³`, **not** this separate-factor
`γ_5`. From this it asserts that the **Koide `Q=2/3` chiral-mass mechanism** and
**generation-ID** collapse into the same keystone.

This note bounds that inference. The separate-factor `γ_5` is real and is exactly what
the **spin-statistics** side needs — but it is **generation-blind**, and the Koide
`Q=2/3` mechanism requires a chirality the `γ_5` provably cannot supply. **"Not blocked
by the narrow no-go" ≠ "supplied."** There are two independent chirality requirements.

## The two gates

| | **Dirac/spinor chirality** | **Koide/generation chirality** |
|---|---|---|
| operator | `γ_5 = I_3 ⊗ σ_3` on `(gen R³) ⊗ (L⊕R)` | a generation mass operator `M_gen` on `R³` |
| requirement | anticommutes with the Dirac mass `β` (L↔R) | `{M_gen, Γ_χ} = 0`, `Γ_χ = (2/3)J − I` |
| source | **supplied** by retained `cl3_to_cl31_spinor_extension` | the retained `koide_anticommuting_operator_derivation`: `Q=2/3 ⟺ {M_gen, Γ_χ}=0` |
| needed for | spin-statistics (CAR / positive-energy / microcausality) | the charged-lepton `Q=2/3` mass spectrum |

## The separation (verified, `PASS=12`)

1. **`γ_5` is genuine for Dirac/spinor chirality.** `γ_5² = I` and `{γ_5, β} = 0` for the Dirac mass
   `β = I_3 ⊗ σ_1` — a real L↔R chiral mass coupling. This is the sound half of the keystone
   claim, and it is exactly what spin-statistics consumes.
2. **`γ_5` is generation-blind.** `γ_5 = I_3 ⊗ σ_3` acts as the **identity** on the generation
   factor, so it **commutes** with *every* generation-sector operator `G ⊗ I_2` — in particular
   `[γ_5, Γ_χ ⊗ I] = 0`. The Dirac mass `β` likewise commutes with `Γ_χ ⊗ I`. Neither
   contributes anything to `{M_gen, Γ_χ}`.
3. **Koide/generation chirality is not supplied — it needs a C₃-breaking operator.** By the retained no-go,
   every C₃-equivariant (circulant) `M_gen` with `{M_gen, Γ_χ}=0` is `M_gen=0`; a nonzero
   `M_gen` anticommuting with `Γ_χ` exists only off the circulant locus (the null space of
   `M ↦ {M, Γ_χ}` over symmetric `R³` matrices is nonzero, and **every** element breaks C₃:
   `[M_gen, R] ≠ 0`). A C₃-trivial (`I_3`) spinor grading like `γ_5` cannot produce a
   C₃-breaking generation operator.

**Conclusion:** the Dirac/spinor and Koide/generation chirality requirements
are independent commuting gradings on the tensor product. The retained
`Cl(3,1)` supplies the Dirac/spinor chirality requirement; the
Koide/generation chirality requirement remains open on the generation `R³`
factor — a C₃-orbit-splitting `M_gen` that no spinor-factor chirality reaches.

## Relation to existing work

This sharpens, and is consistent with, the existing flavor-emergent
chirality transport note (unaudited), whose candidate table already finds
the `γ_CL = I_3 ⊗ σ_3` grading **INERT** on
the generation factor (`{G⊗σ₁, I_3⊗σ₃}=0` for every `G` → zero constraint there). The added
content here is the explicit **two-gate** framing grounded in the **retained**
`koide_anticommuting_operator_derivation` (not only the unaudited transport note), and the
precise **"not blocked ≠ supplied"** scope-bound on the separate-factor `Cl(3,1)` keystone claim.

The retained authorities used:
[`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
(retained),
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
(retained_bounded),
[`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)
(retained).

## Scope / verdict

- The keystone-collapse is **sound for Dirac/spinor chirality**, supplied by the
  retained `Cl(3,1)`, and that genuinely advances the spin-statistics tower.
- It does **not** discharge the **Koide `Q=2/3` / generation-ID chirality**, which
  remains the open generation-`R³` C₃-breaking requirement.
- No new axiom or import; no PDG load-bearing. The independent audit lane owns any status.
