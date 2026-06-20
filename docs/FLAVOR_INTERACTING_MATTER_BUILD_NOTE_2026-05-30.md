# Flavor — interacting-matter build: exact epsilon/C3/Q core, external dynamics still open


**Date:** 2026-05-30
**Claim type:** open_gate
**Claim boundary:** open matter-action gate with an executable finite-algebra
diagnostic core. The matter-action vertex, critical coupling,
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
- a diagonal generation operator invariant under the fixed `C3` cycle is
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

This note may be cited for the executable `epsilon`/`C3`/`Q(r)` finite-algebra
diagnostic and for the open gate it isolates. It may not be cited as a retained
derivation of the interacting matter action, a forced Koide dial, or a
first-principles computation of the displayed nonperturbative branch.

## The reframe that motivated it (and was partly vindicated)
Every prior route (kinematic/free/symmetric/RG-fixed-point) gave `b=0` or an endpoint,
because those structures reach only symmetry-enhanced/discrete couplings. The
motivating hypothesis was that **interacting non-perturbative dynamics is
different**: it can produce continuous non-enhanced numbers (QCD: `m_p/Λ`,
etc.). The external build therefore treated `r=|b|²/a²` as a dynamical output.

## External build context — the reported `b=0` wall movement is not runner-certified
- The external build reports that free/single-channel `b=0` is an all-orders
  selection rule in that build context (corner-difference momentum is not
  supplied against the staggered phase; verified there as `|b|~1e-33` to H^8).
- The external build reports that mean-field dropped the Fierz exchange
  channel, the channel that feeds `b` in that model. Restoring it, the build
  reports a self-consistent `b!=0` branch above a critical coupling. This is
  context for the open matter-action bridge, not a claim certified by this
  runner.
- `r=½` is **dynamically accessible:** Build 3's first-nucleated striped corner condensate
  is reported at `r≈0.535` (Q≈0.69, within ~7% of Koide), with huge corner
  susceptibility. The runner only converts this supplied `r` value through the
  checked `Q(r)` formula.

## But r=½ is NOT forced — it's a continuous output of an unsupplied coupling
In the reported build summaries, the three builds disagree on `r`, because it
is set by the matter-action coupling ratio:
| build | natural coupling | off-self-dual |
|---|---|---|
| scalar NJL | r=0 (Q=1/3) | runaway |
| SD/Fierz | r=0 (Q=1/3) | r=2/5 (Q=3/5) — *regulator artifact* |
| two-channel | r=0 (Q=1/3) | onset r≈0.535 (Q≈0.69), then continuous |

In that supplied context, the natural (C3-symmetric, Fierz-self-dual) coupling
gives `r=0` (Q=1/3, democratic) in all three builds. No forcing symmetry is
supplied there for exactly `1/2`: `r` crosses `1/2` with nonzero slope
(`dr/dg≈-1.77`), and `1/2` appears at no kernel. The exact reason for `1/2`
inside this packet is algebraic, `Tr(I^2)/Tr((J-I)^2)=3/6` (the
HS-equipartition / block-count measure), and the supplied dynamics does not
select it.

## The checked pin: C3-invariant diagonal channels do not split the orbit
**Before:** "free theory forbids `b!=0`." **After:** in the reported
interacting context, `b` can move, but `r` remains a continuous output of an
unsupplied coupling-channel ratio, and no supplied C3-symmetric contact
truncation pins exactly `1/2`. The finite-algebra reason checked here is
narrow: a C3-invariant diagonal channel on the triplet is scalar, while the
orbit-splitting diagonal channel required for a generation split breaks C3.

The runner-certified part is the finite diagonal statement: on the `hw=1`
triplet, a diagonal operator invariant under the `C3` cycle is scalar, and a
non-scalar diagonal generation splitter breaks `C3`. This is not a global
no-go over every possible interaction; it is the exact obstruction for the
native diagonal/`epsilon` escape tested here.

## The build's own proposed escape (ε-weighted chiral channel) is generation-blind
The natural next step would be a C3-orbit-splitting vertex weighted by
`epsilon(n)=(-1)^(n1+n2+n3)`. The runner verifies that it does not split the
orbit: on the `hw=1` triplet, `epsilon=-1` is constant, and as a `(pi,pi,pi)`
momentum shift it maps `hw=1` to `hw=2` outside the triplet. The native chiral
phase `epsilon` therefore cannot supply this tested generation-specific
grading.

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
