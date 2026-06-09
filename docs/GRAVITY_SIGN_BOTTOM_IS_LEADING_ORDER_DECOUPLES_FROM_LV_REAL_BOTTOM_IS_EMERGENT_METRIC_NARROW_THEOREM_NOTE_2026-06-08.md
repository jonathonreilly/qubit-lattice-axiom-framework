# Attacking the Bottom: the Gravity Sign G>0 Is a Leading-Order (O(k²)) Property — the Catch-22 and the Lorentz Naturalness Gap Are Subleading (O(k⁴)); the Real Bottom Is the Emergent Dynamical Metric

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** bottom analysis (downgrades/relocates the deepest residual of the graviton-diffeomorphism chain)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_sign_bottom_leading_order_decouples_from_lv_2026_06_08.py`](../scripts/gravity_sign_bottom_leading_order_decouples_from_lv_2026_06_08.py) (PASS=4).

## The bottom, and the decisive question

R1 (graviton massless) + R2 (stress conservation Noether-derived) + R3 (the geometric Regge/EH route gives
the healthy λ=1 graviton) reduced the gravity sign `G>0` to **"emergent IR-exact Lorentz invariance,"**
which carries two walls: the **catch-22** (the spin-2 uniqueness theorems need exact Poincaré, but evading
Weinberg–Witten needs UV-broken Lorentz) and the **`LORENTZ_NATURALNESS_GAP`** (the cubic-anisotropy LV is
not RG-suppressed, 12–21 orders). The decisive question this note settles: **does the *sign* actually need
IR-*exact* Lorentz, or only leading-order isotropy?**

## Result (the walls are subleading; the sign is leading-order)

The gravity sign is the sign of the **leading O(k²) kinetic coefficient**; the naturalness-gap LV is an
**O(k⁴)** correction. These are different orders, so the LV cannot flip the sign. Verified:

- **(B1) The sign is leading-order, LV-independent.** Model the TT graviton dispersion
  `ω²(k) = c₂ k² (1 + α·A₄(k)·k²)`, with `c₂ = +½` the healthy leading kinetic coefficient (R3:
  `G^{lin}(h_TT)=½k²h_TT`; sign `+` via RP) and `α·A₄(k)·k²` the O(k⁴) cubic-anisotropy LV (the
  naturalness-gap residual). For **every** LV strength `α` (including large/UV), the `k→0` leading
  coefficient → `c₂ > 0`: the LV is a higher-order correction and **never flips the leading sign**.
- **(B2) The sign needs only leading-order SO(3) isotropy + RP.** The leading O(k²) coefficient is
  isotropic (direction-independent; the lattice dispersion's O(p²) term is `|p|²` — this session's
  ξ-isotropy result), and its **sign** is fixed by reflection positivity (no physical ghost). The cubic
  anisotropy enters only at O(k⁴). So the sign needs **leading-order SO(3)** (which the framework *has*) +
  **RP** (a framework *theorem*) — **not** IR-exact Lorentz.
- **(B3) The catch-22 and naturalness gap are subleading.** The spin-2 uniqueness theorems' exact-Poincaré
  hypothesis forbids **higher-derivative / Lorentz-violating** deformations (O(k⁴)+); the **leading**
  two-derivative kinetic term and its sign are fixed by the leading structure (R1/R2/R3) + RP. So both
  walls bound the **O(k⁴) LV corrections**, **not** the **O(k²) sign** `G>0`.
- **(B4) The real bottom is the emergent dynamical metric.** Given (i) the emergent **dynamical** metric
  (the edge-length DOF on which R3's Regge/EH action lives), (ii) leading-order emergent SO(3) (held; LV
  subleading), and (iii) RP (theorem), the sign is `G>0`. The single genuine remaining input is **(i)**:
  the bare Z³ axiom supplies the site set + adjacency + the **kinematic** emergent conformal class
  (records-derived causal structure, `MIN_TIME_STEP` / the ξ-work) + the scale primitive, but **not** the
  **dynamical edge-length metric** (the gravitational field whose fluctuation is the graviton).

## Verdict

**The gravity sign `G>0` does not require IR-exact emergent Lorentz.** It is a leading-order (O(k²),
IR) property — the long-range 1/r attraction lives at `k→0`, exactly where the leading kinetic sign is
fixed by leading-order SO(3) isotropy (held) + RP (theorem) + the emergent dynamical metric. **The
catch-22 and the `LORENTZ_NATURALNESS_GAP` live at O(k⁴) — they bound the subleading Lorentz-violating
corrections and cannot flip the leading sign.** So the deepest gravity atom bottoms out **not** at
"IR-exact Lorentz" (the scary no-go) but at the **emergent dynamical metric** — of which the framework has
the kinematic half (the records-conformal-class + scale) and lacks the dynamical half (the edge-length
DOF / dynamical Regge gravity). This **downgrades and sharpens** the bottom into a cleaner, more tractable
open frontier.

## What is and is not claimed

- **Is:** the gravity sign `G>0` is a leading-order O(k²) property, fixed by leading-order SO(3) isotropy
  (held) + RP (theorem) + the emergent dynamical metric; the LV / catch-22 / naturalness-gap are O(k⁴)
  (subleading) and cannot flip the sign (B1); so the deepest residual relocates from "IR-exact Lorentz" to
  "the emergent dynamical metric."
- **Is not:** does **not** derive the emergent dynamical (edge-length) metric — that is the genuine
  remaining open piece (the framework has the kinematic conformal class, not the dynamical metric); does
  **not** claim the LV corrections are absent (they are real, subleading, and the naturalness gap is real
  *for them*); does **not** by itself complete the chain (it removes the naturalness-gap obstruction from
  the *sign* and relocates the residual). Adds no axiom or fitted value.

## Boundaries (honest)

- **The LV is real and the naturalness gap stands — for the corrections.** This note shows the LV does not
  flip the *sign*; it does not claim the framework's emergent Lorentz is exact (it isn't — the cubic
  anisotropy survives). Lorentz-violating *predictions* remain governed by the naturalness gap.
- **The emergent dynamical metric is the honest remaining input.** The kinematic conformal class is
  records-derived; making it a *dynamical* field with the Regge/EH action (the edge-length DOF) is the open
  frontier this bottom lands on.

## Load-bearing inputs

- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  — RP ⇒ no physical ghost ⇒ the leading kinetic sign is healthy (`G>0`).
- [`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
  — the cubic-anisotropy LV (O(k⁴)); here shown subleading to the O(k²) sign.
- [`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
  — the kinematic emergent conformal class (records-derived causal structure); the dynamical metric is the open half.

Companion (in review): the R1/R2/R3 chain notes (graviton-mass gate; Noether stress conservation; geometric
Regge λ=1).

## Forbidden-imports check

No PDG / fitted value. The order-counting (sign = O(k²) coefficient; LV = O(k⁴)), the leading-coefficient
`k→0` limit, and the O(k²) isotropy are standard dispersion analysis, reproduced in the runner. RP is a
framework theorem; the naturalness gap and the emergent conformal class are cited framework results.
