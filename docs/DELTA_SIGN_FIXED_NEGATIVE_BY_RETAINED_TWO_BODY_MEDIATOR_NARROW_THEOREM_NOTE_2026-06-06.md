# The Sign of the Interaction Asymmetry `delta` is Fixed Negative by the Retained Two-Body Mediator; `K_C3` is Negative on the Nonresonant Branch — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem / exact-support bridge (the **sign** of
`delta` from the mediator, plus the exact nonresonant sign branch for signed
`K_C3`; the physical magnitude/gap branch remains open)
**Status:** unaudited candidate; inherits the retained mediator's **bounded**
tier and is stacked on the periodic-kernel bridge. Graph-visible only so the
independent audit lane can decide.
**Primary runner:** [`scripts/delta_sign_from_retained_mediator_runner.py`](../scripts/delta_sign_from_retained_mediator_runner.py)
**Cached output:** [`logs/runner-cache/delta_sign_from_retained_mediator_runner.txt`](../logs/runner-cache/delta_sign_from_retained_mediator_runner.txt)

## Audit context

The emergent signed `C3` coupling `K_C3` (the `J − I` double-shift on the generation triplet) is
sourced by the interaction asymmetry `delta = E_2 − 2*E_1 + E_0`, the two-excitation **mutual
energy** (the occupation curvature; `sign(K_C3) = sign(delta)`). The companion structure result
establishes that `delta` is irreducibly two-body and zero for the free single-hop dynamics, and
names the open piece as the **value** (sign and scale) of `delta`. This note fixes its **sign**:
the framework's already-**retained** two-body channel is **attractive**, so `delta < 0`.

The open `delta` was named in
[`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
(`retained_bounded`). The two-body channel used here is the retained
[`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md)
(`retained_bounded`; the partner-force channel is attractive on `15/15` rows with a near-Newton
`~d^-1.95` law), with companion
[`WILSON_TWO_BODY_OPEN_REFINED_NOTE_2026-04-11`](WILSON_TWO_BODY_OPEN_REFINED_NOTE_2026-04-11.md).
For the retained momentum-corner generation pair, this stacked repair also
uses the exact finite-periodic density-kernel bridge
[`GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE_NOTE_2026-06-07`](GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE_NOTE_2026-06-07.md),
which derives the plane-wave normalization and

```text
delta_ij = (Vq(0) - Vq(k_i-k_j)) / N,     Vq(q) = -G/(eps(q)+mu^2),
```

from the same local mediator stencil on an even periodic torus.

## Safe statement

**Theorem (sign of `delta`; nonresonant sign of `K_C3`).** Identify the two
generation excitations of the `hw=2` intermediate sector with two quanta of
the lattice matter field `psi` on the retained momentum-corner generation
surface. They source and feel the framework's retained shared scalar field by
the same universal coupling `(L + mu^2) Phi = G |psi|^2`; on the finite
periodic plane-wave surface this is exactly the density-kernel formula in the
stacked 2026-06-07 bridge. Then:

1. **The retained partner force is attractive.** Reproducing the retained observable verbatim
   (graph Laplacian `L`, `mu^2 = 0.001`, `G = 50`, `sigma = 0.80`, partner force
   `−sum_x rho(x) ∂_x Phi(x)`, "toward partner" positive), the force between the two excitations
   is attractive on every separation and side tested (`d = 3..7`, sides `12, 14, 16`), with
   `|F| ~ d^-1.94` — matching the retained note's `15/15` attractive rows and `~d^-1.95` law
   (the `side=12, d=3` value reproduces `+0.49557` exactly).

2. **The two-excitation binding energy is negative.** The corresponding binding energy
   `E_mut = −sum_x rho_A(x) Phi_B(x) < 0` on every row (attractive ⇒ bound), and `|E_mut|` is
   **bounded and monotone-decreasing** in separation (the screened-Poisson `(L + mu^2)^{-1}`
   kernel is sign-definite).

3. **The retained momentum-corner generation pair has the same negative
   `delta_ij` on each pair.** By the periodic density-kernel bridge, the
   retained `hw=1` corners satisfy `eps(k_i-k_j)=8` for every distinct pair,
   hence

   ```text
   delta_ij = ( -G/mu^2 + G/(8+mu^2) ) / N < 0
   ```

   and the equality across pairs is the exact `J - I` form. This closes the
   generation-pair-to-`psi`/kernel normalization bridge for the pure periodic
   corner surface; it does not pin the physical magnitude.

4. **Second-order sign propagation is exact on the nonresonant branch.** For
   the native one-hop model with gap `eps_gap > 0`, pair curvature `delta`,
   and one-hop amplitude `t`, eliminating the `hw=0` and `hw=2` intermediate
   states gives the off-diagonal `C3` coupling

   ```text
   K_C3 = t^2 * delta / (eps_gap * (eps_gap + delta)).                  (1)
   ```

   Therefore `sign(K_C3)=sign(delta)` exactly when the nonresonant branch
   condition `eps_gap > 0 and eps_gap + delta > 0` holds:

   ```text
   eps_gap > 0,     eps_gap + delta > 0.                                (2)
   ```

   Combining (1)-(2) with the retained mediator sign gives `K_C3 < 0` on the
   nonresonant attractive branch. A counterfactual repulsive channel gives
   `K_C3 > 0` on the same branch, while a strong-curvature/resonant branch
   `eps_gap + delta < 0` flips the denominator sign and is explicitly outside
   this sign theorem.

So the **sign of the interaction curvature** is fixed by the retained mediator:
`delta < 0`. The signed emergent `C3` coupling is negative on the explicitly
stated nonresonant branch: `K_C3 < 0` if `eps_gap > 0` and
`eps_gap + delta > 0`. The physical magnitude and branch verification remain
open IR/gap data rather than a flavor-value assertion.

## The genuine open piece (and the route this opens)

The **magnitude** `|delta| = |E_mut|` is **bounded/routed** by the mediator
kernel but **not pinned**. The periodic-corner bridge removes the old
"generation-pair separation" ambiguity for the pure plane-wave surface and
replaces it with explicit IR/gap data `(G, mu^2, N, eps_gap)`. This note moves
`delta` from "sign and scale both open" to "**sign fixed (attractive), kernel
normalization explicit, sign propagation branch exact**." The remaining
artifact is not another localization ansatz; it is the physical IR/gap
closure proving that the realized branch satisfies `eps_gap + delta > 0`.

## Boundary (honest)

- **A sign + branch theorem, not a value.** It fixes `delta < 0` on the retained
  mediator surfaces and proves `K_C3 < 0` only on the nonresonant branch
  `eps_gap > 0`, `eps_gap + delta > 0`; it does not pin the physical magnitude
  or prove that the physical branch is nonresonant.
- **Inherits the retained channel's bounded tier.** The attraction is established on the
  retained note's **clean partner-force** observable; that note is `retained_bounded` because
  its staggered trajectory channel is noisier and full Newton on the primary architecture is not
  closed. This note is no stronger than that surface.
- **Load-bearing identification (now bridged on the periodic corner surface).** The result
  rests on identifying the two generation excitations with two quanta of the
  same matter field `psi` that sources the mediator. The stacked periodic
  plane-wave bridge supplies the finite-volume density-kernel normalization
  for the retained `hw=1` momentum-corner generations. This is an application
  of a retained channel, **not** a new field, species, or coupling, but the
  physical IR/gap branch remains open.
- **Forces no flavor value.** This is one overall **sign** of the `C3` coupling; it does **not**
  force `r`, `Q`, or any mixing value (no overreach). `r` remains the registered dial.

## Forbidden imports check

No new axiom and no new import. The mediator `(L + mu^2) Phi = G|psi|^2` and
its attractive partner force are the **retained** (`retained_bounded`)
two-body channel, reproduced verbatim; applying it to two `psi`-quanta on the
retained momentum-corner surface uses the stacked periodic density-kernel
bridge. The occupation-curvature identity `delta = E_mut` and the
nonresonant sign propagation formula
`K_C3 = t^2 * delta / (eps_gap * (eps_gap + delta))` are arithmetic. The
magnitude/gap branch is named open, not asserted.

## Runner check breakdown

Class A: (1) the retained partner force is attractive on `d = 3..7`, sides
`12, 14, 16` (reproducing the published `+0.49557` and the `~d^-1.95` law)
and the binding energy `E_mut < 0` on every row; (2) `|E_mut|` is bounded and
monotone in separation; (3) the stacked periodic kernel gives equal negative
`delta_ij` for the three retained `hw=1` corner pairs and `eps(Delta k)=8`;
(4) the exact formula `K_C3 = t^2 * delta / (eps_gap * (eps_gap + delta))`
gives `K_C3 < 0` on `eps_gap > 0`, `eps_gap + delta > 0`, detects the
resonant branch as excluded, and preserves the exact `J - I` form. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content reproduces the retained two-body channel's exact
attractive partner-force observable (verbatim conventions and published
value), shows the corresponding two-excitation binding energy is negative and
bounded, uses the stacked periodic plane-wave bridge to put the retained
momentum-corner generation pair on the same density-kernel surface, and proves
the second-order sign formula rather than sampling a single `delta`. The result
is a **mediator sign + nonresonant branch theorem**: `delta < 0`, and
`K_C3 < 0` when `eps_gap > 0` and `eps_gap + delta > 0`. It inherits the
mediator's bounded tier, forces no flavor value, and leaves the physical
IR/gap branch for later audit. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/delta_sign_from_retained_mediator_runner.py
```
