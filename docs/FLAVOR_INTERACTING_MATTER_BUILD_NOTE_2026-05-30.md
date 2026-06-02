# Flavor — large build: interacting dynamics generates b≠0 (wall moved), but r=½ stays pinned to a chiral input

> **Status authority:** independent audit lane only. (packaging fix 2026-06-02)

**Date:** 2026-05-30
**Claim type:** large build / honest partial advance. The matter-action vertex is an
admitted bridge-gap input (user-authorized for this build, flagged); kinematics derived.
**Runner:** `scripts/flavor_interacting_matter_build_2026_05_30.py` (+ cache).
**Source:** interacting-matter build (`wf_61ab5328`, 3 action candidates × 3 non-perturbative
methods) + verification.

## The reframe that motivated it (and was partly vindicated)
Every prior route (kinematic/free/symmetric/RG-fixed-point) gave `b=0` or an endpoint,
because those structures reach only symmetry-enhanced/discrete couplings. **Interacting
non-perturbative dynamics is different** — it produces continuous non-enhanced numbers
(QCD: `m_p/Λ`, etc.). So this build computed `r=|b|²/a²` as a *dynamical output*.

## Genuine positive — the `b=0` wall MOVED
- **Free/single-channel `b=0` is an exact all-orders selection rule** (corner-difference
  momentum can't be supplied against the staggered phase; verified `|b|~1e-33` to H⁸).
- **Mean-field dropped the Fierz *exchange* channel — the only channel that feeds `b`.**
  Restoring it, a **self-consistent `b≠0` branch exists** above a critical coupling. So
  `b` is genuinely a non-perturbative dynamical output — *not* protected to zero once
  interactions are honest. **The reframe (dynamics ≠ kinematics) is correct.**
- `r=½` is **dynamically accessible:** Build 3's first-nucleated striped corner condensate
  lands at `r≈0.535` (Q≈0.69, within ~7% of Koide), with huge corner susceptibility.

## But r=½ is NOT forced — it's a continuous output of an unsupplied coupling
The three builds **disagree** on `r`, because it's set by the matter-action coupling ratio:
| build | natural coupling | off-self-dual |
|---|---|---|
| scalar NJL | r=0 (Q=1/3) | runaway |
| SD/Fierz | r=0 (Q=1/3) | r=2/5 (Q=3/5) — *regulator artifact* |
| two-channel | r=0 (Q=1/3) | onset r≈0.535 (Q≈0.69), then continuous |

At the **natural (C₃-symmetric, Fierz-self-dual) coupling, all three give `r=0` (Q=1/3,
democratic).** No dynamical symmetry forces exactly `½`: `r` crosses `½` with nonzero slope
(`dr/dg≈−1.77`); `½` appears at no kernel. The *only* exact reason for `½` that surfaced is
algebraic — `Tr(I²)/Tr((J−I)²)=3/6` (the HS-equipartition / block-count measure) — which the
dynamics does **not** select.

## The pin relocated, and converges on the chiral gate
**Before:** "free theory forbids `b≠0`." **After:** "interactions generate `b`, but `r` is a
continuous output of an unsupplied coupling-channel ratio, and exactly-`½` has no dynamical
symmetry in any **C₃-symmetric** contact truncation." The deeper reason: every S₃-symmetric
*idempotent* vacuum gives `Q∈{1/3,½,1}`, never `2/3`; `Q=2/3` is a non-idempotent **interior**
operator, and a **C₃-symmetric** interaction only ever makes the *circulant* `b` (which
*commutes* with `Γ_χ`) — never the orbit-splitting *anticommuting* operator the Q=2/3 readout
needs (`koide_z3_equivariant_anticommuting_no_go`, retained_bounded). **A C₃-symmetric
interaction provably cannot supply it.**

## The build's own proposed escape (ε-weighted chiral channel) is generation-blind
The natural next step would be a C₃-orbit-*splitting* vertex weighted by `ε(n)=(−1)^{n₁+n₂+n₃}`.
**Verified: it doesn't split the orbit.** On the hw=1 triplet `ε=−1` *constant* (∝ −I,
generation-blind); as a `(π,π,π)` momentum shift it maps hw=1→hw=2 (out of the triplet, the
3↔3̄ axis). So the native chiral phase `ε` **cannot** supply the generation-specific chiral
grading — the same wall as "spacetime chirality is generation-blind."

## Honest verdict
The build is a **real advance** (interacting dynamics generates `b≠0`; `r=½` is dynamically
accessible at ~0.535) — your "build more dynamics" instinct correctly moved the `b=0` wall that
all kinematic analysis hit. **But it does not derive `r=½`:** the value is a continuous output
of the matter-action coupling ratio (an admitted bridge-gap input), the natural coupling gives
`r=0` (Q=1/3), no dynamical symmetry forces exactly `½`, and the only orbit-splitting that gives
Q=2/3 requires a **generation-specific chiral interaction** that the native structures
(C₃-symmetric vertex, the `ε` phase) provably do not provide. So even the deepest dynamical
build **converges on the same generation-specific chiral input** — now understood as
"the matter interaction channel must itself be C₃-orbit-splitting (chiral)," which is not native.

## Status / next path (not a closed wall)
The pin is now localized at the **interaction-channel** level: does any *native* structure
provide a C₃-orbit-splitting (chiral) four-fermion channel (not `ε`, not C₃-symmetric)? The
retained no-gos say no (the chiral grading is non-native). The framework reduces all
charged-lepton flavor to that one chiral channel + Planck. No false closure: a derivation
requires a native generation-orbit-splitting interaction, which — across kinematics *and* now
dynamics — the framework's content does not contain. The honest physics reading: this chiral
input is generation-specific, in the same category as the SM's hand-put-in flavor chirality.
