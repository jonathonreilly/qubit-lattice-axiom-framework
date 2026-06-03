# Flavor — the framework's record dynamics sharpens (r=1/2 is the unstable separatrix), so the time-arrow "stabilizer" for r=1/2 is realized by no framework CPTP map; r=1/2 must be a measure choice, not a dynamical attractor

**Date:** 2026-06-02
**Claim type:** a route-closure (the dynamical/time-arrow stabilizer for r=1/2 fails) — a clean negative. Not a no-go on the value; r=1/2 remains open as a measure choice.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade.
**Runner:** `scripts/flavor_record_dynamics_sharpens_arrow_stabilizer_fails_2026_06_02.py` (SCORECARD 5/5).

## Question
`r=1/2` is the unstable separatrix of the Lüders sharpening flow but the stable attractor of the
reverse thermalizing flow. Could the framework's emergent-time / decoherence arrow be the *thermalizing*
direction, making `r=1/2` a dynamical attractor (and so forcing the charged-lepton value)?

## Result — no: the physical arrow sharpens, three independent strikes
1. **The record map sharpens.** The framework's record-forming dynamics is Lüders self-composition
   `p → p²/Z`, which on the 2-sector weight is `r → 2r²`. Its fixed point `r=1/2` has multiplier `2` →
   **unstable** (verified; iterating from `r=0.49` runs to `0`). The thermalizing `g(r)=√(r/2)` (`r=1/2`
   stable, multiplier `1/2`, all seeds → 0.5) is merely the **formal time-reverse** of the sharpening
   map — record *erasure*, not a physical CPTP record channel.
2. **The einselection channel is a no-op on r.** Because `H` is C₃-invariant it is *already*
   block-diagonal in the isotype projectors `{P₀, P₁}` for **every** `(a,b)` (verified
   `max‖P₀ H P₁‖ ≈ 8e-16`). So the physical einselection/decoherence channel induces **no flow on `r`
   at all**; the thermalizing `g(r)` is hand-imposed, not realized by any framework map.
3. **Honest thermalization targets the wrong point.** The genuine Born / second-law equilibrium is the
   tracial state `I/3`, whose sector weights are dimensional `(1/3, 2/3)` → **r=1** (verified). An honest
   depolarize-toward-`I/3` drives `r → 0` (Q → 1/3), never `r=1/2`. The arrow is moreover
   conjugation-even, carrying zero selective information for `r=1/2` vs `r=1`.

## Consequence
The dynamical/time-arrow route to *force* `r=1/2` is **closed**: the framework's physical arrow
sharpens (`r=1/2` unstable), the decoherence channel is a no-op on `r`, and honest thermalization gives
`r=1` (or `r→0`). Therefore `r=1/2` cannot be a dynamical attractor of the framework's record dynamics —
it must be selected by a **measure** choice on the 2-sector partition (companion note), not by the
record flow. This prevents re-chasing the thermalizing-arrow stabilizer as a forcing mechanism.

## The next paths this opens (not closing)
- The value question is fully on the **measure** axis (uniform/block-count vs Born/dimension on the 2
  K-real sectors), not the dynamical axis.
- Open upstream check: does decoherence on the generation factor dynamically *reach* `I/3` at all
  (`koide_records_pointer_grounds_block_channel`, audited_conditional)? If the true decohered state is
  not `I/3`, the `r=1` baseline itself shifts.

## Provenance (verified 2026-06-02)
- `r→2r²` fixed point `r=1/2` multiplier 2 (unstable) with run-away iteration; `g(r)=√(r/2)` stable but
  the time-reverse; `max‖P₀ H P₁‖ ≈ 8e-16` (no-op); `I/3` sector weights `(1/3,2/3) → r=1`: verified
  directly (runner 5/5). From the record-posit workflow (`wf_f050d357`); consistent with the
  retained_bounded self-correction in `flavor_einselection_2sector_modulo_kreality`.
- This note sets no audit status; it closes the dynamical-stabilizer route and relocates the value
  question to the measure axis.
