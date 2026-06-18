# Flavor — interacting-matter build: exact epsilon/C3/Q core, external dynamics still open


**Date:** 2026-05-30
**Claim type:** open_gate
**Claim boundary:** bounded-support diagnostic: executable finite-algebra core
plus external-build context. The matter-action vertex, critical coupling,
nonperturbative `b!=0` branch, and continuous `r(g)` curve are not derived by
this source packet.
**Runner:** `scripts/flavor_interacting_matter_build_2026_05_30.py` (+ cache).
**Source:** interacting-matter build (`wf_61ab5328`, 3 action candidates × 3 non-perturbative
methods) + verification.

## Source-side split (2026-06-18)

This source now separates the re-auditable executable core from the external
large-build narrative.

**Executable core.** The runner verifies only exact finite algebra:

- `epsilon(n)=(-1)^(n1+n2+n3)` is constant on the `hw=1` generation triplet;
- the same `epsilon` shift maps `hw=1` to `hw=2`, so it is not an internal
  orbit-splitting generation channel on the triplet;
- a diagonal generation operator invariant under the retained `C3` cycle is
  scalar, while a non-scalar diagonal orbit splitter necessarily breaks `C3`;
- for `F=aI+b(J-I)`, the trace ratio satisfies
  `Q(F)=Tr(F^2)/(Tr F)^2=1/3+(2/3)r` with `r=|b|^2/a^2`.

**Context only.** The reported three interacting builds, the critical coupling,
the continuous `r(g)` curve, and the `b!=0` branch are preserved as scientific
context. This note does not claim that the runner derives them from retained
framework primitives, and it does not claim a retained interacting
matter-action theorem.

The audit-relevant movement is therefore narrow but real: the previously
hard-coded `epsilon`/`C3` obstruction and `Q(r)` arithmetic are now executable
finite-algebra checks, while the nonperturbative dynamics remain an open
matter-action bridge.

## Source boundary (2026-06-12, superseded by the executable split above)

**Boundary:** bounded exploratory support, not a first-principles
interacting-dynamics theorem. Effective status is audit-derived; this source
records only the claim boundary.

The displayed algebraic values and the reported build summaries are useful
diagnostics, but the source runner does not independently compute the three
builds, the critical coupling, the continuous `r(g)` curve, or the claimed `C3`
operator obstruction from retained framework primitives. The 2026-06-18 runner
repair now computes the finite `epsilon`/`C3` obstruction, but still does not
compute the interacting branches or `r(g)`.

This note may be cited for the bounded diagnostic lesson that interactions can
move the `b=0` wall while exact `r=1/2` remains an unsupplied coupling/channel
selection. It may not be cited as a retained derivation of the interacting
matter action, a forced Koide dial, or a first-principles computation of the
displayed nonperturbative branch.

## The reframe that motivated it (and was partly vindicated)
Every prior route (kinematic/free/symmetric/RG-fixed-point) gave `b=0` or an endpoint,
because those structures reach only symmetry-enhanced/discrete couplings. **Interacting
non-perturbative dynamics is different** — it produces continuous non-enhanced numbers
(QCD: `m_p/Λ`, etc.). So this build computed `r=|b|²/a²` as a *dynamical output*.

## External build context — the reported `b=0` wall movement is not runner-certified
- **Free/single-channel `b=0` is an exact all-orders selection rule** (corner-difference
  momentum can't be supplied against the staggered phase; verified `|b|~1e-33` to H⁸).
- **Mean-field dropped the Fierz *exchange* channel — the only channel that feeds `b`.**
  Restoring it, the external build reports a self-consistent `b≠0` branch above
  a critical coupling. This is context for the open matter-action bridge, not a
  claim certified by this runner.
- `r=½` is **dynamically accessible:** Build 3's first-nucleated striped corner condensate
  is reported at `r≈0.535` (Q≈0.69, within ~7% of Koide), with huge corner
  susceptibility. The runner only converts this supplied `r` value through the
  checked `Q(r)` formula.

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

## The checked pin: C3-invariant diagonal channels do not split the orbit
**Before:** "free theory forbids `b≠0`." **After:** "interactions generate `b`, but `r` is a
continuous output of an unsupplied coupling-channel ratio, and exactly-`½` has no dynamical
symmetry in any **C₃-symmetric** contact truncation." The deeper reason: every S₃-symmetric
*idempotent* vacuum gives `Q∈{1/3,½,1}`, never `2/3`; `Q=2/3` is a non-idempotent **interior**
operator, and a **C₃-symmetric** interaction only ever makes the *circulant* `b` (which
*commutes* with `Γ_χ`) — never the orbit-splitting *anticommuting* operator the Q=2/3 readout
needs (`koide_z3_equivariant_anticommuting_no_go`, retained_bounded).

The runner-certified part is the finite diagonal statement: on the `hw=1`
triplet, a diagonal operator invariant under the `C3` cycle is scalar, and a
non-scalar diagonal generation splitter breaks `C3`. This is not a global
no-go over every possible interaction; it is the exact obstruction for the
native diagonal/`epsilon` escape tested here.

## The build's own proposed escape (ε-weighted chiral channel) is generation-blind
The natural next step would be a C₃-orbit-*splitting* vertex weighted by `ε(n)=(−1)^{n₁+n₂+n₃}`.
**Verified: it doesn't split the orbit.** On the hw=1 triplet `ε=−1` *constant* (∝ −I,
generation-blind); as a `(π,π,π)` momentum shift it maps hw=1→hw=2 (out of the triplet, the
3↔3̄ axis). So the native chiral phase `ε` **cannot** supply the generation-specific chiral
grading — the same wall as "spacetime chirality is generation-blind."

## Honest verdict
The source-side claim is narrow: exact `epsilon`/`C3` finite algebra and the
`Q(r)` trace-ratio identity are checked; the reported interacting build remains
an external context packet. The result does not derive `r=1/2`:
the value remains a continuous output of an unsupplied matter-action
coupling/channel ratio, and the native `epsilon` phase is generation-blind on
the `hw=1` triplet. A retained derivation still requires a native
generation-orbit-splitting interaction channel or a retained theorem showing
why the matter action selects the needed channel.

## Status / next path (not a closed wall)
The pin remains localized at the **interaction-channel** level: does any native
structure provide a `C3`-orbit-splitting four-fermion channel (not `epsilon`,
not a diagonal `C3`-invariant channel)? This note does not close that gate. It
queues the sharper re-audit question: after accepting only the executable
finite-algebra core, the remaining missing bridge is a first-principles
matter-action derivation for the nonperturbative branch and the channel ratio
that would set `r`.
