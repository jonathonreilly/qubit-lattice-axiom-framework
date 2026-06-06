# The Sign of the Interaction Asymmetry `delta` is Fixed Negative (Attractive) by the Retained Two-Body Mediator — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (the **sign** of `delta` / `|K|`; the magnitude bounded, not pinned)
**Status:** unaudited candidate; inherits the retained mediator's **bounded** tier. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/delta_sign_from_retained_mediator_runner.py`](../scripts/delta_sign_from_retained_mediator_runner.py)
**Cached output:** [`logs/runner-cache/delta_sign_from_retained_mediator_runner.txt`](../logs/runner-cache/delta_sign_from_retained_mediator_runner.txt)

## Audit context

The emergent `C3` coupling `|K|` (the `J − I` double-shift on the generation triplet) is
sourced by the interaction asymmetry `delta = E_2 − 2*E_1 + E_0`, the two-excitation **mutual
energy** (the occupation curvature; `sign(|K|) = sign(delta)`). The companion structure result
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

## Safe statement

**Theorem (sign of `delta`).** Identify the two generation excitations of the `hw=2`
intermediate sector with two quanta of the lattice matter field `psi` (a generation is a `hw=1`
excitation of `psi`). They source and feel the framework's retained shared scalar field by the
same universal coupling `(L + mu^2) Phi = G |psi|^2`. Then:

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

3. **Hence `delta < 0` and `sign(|K|) < 0`.** Since `delta = E_2 − 2*E_1 + E_0` is exactly this
   two-excitation mutual energy, `delta = E_mut < 0`. Propagating into the second-order
   effective operator on `C^8` gives the `C3` coupling with `sign(|K|) < 0` and the exact
   `J − I` form. A (counterfactual) repulsive channel `delta > 0` would flip `sign(|K|) > 0`, so
   the sign law is genuine, not an artifact.

So the **sign** of the emergent `C3` coupling is fixed by a retained surface: `delta < 0`,
`|K| < 0`.

## The genuine open piece (and the route this opens)

The **magnitude** `|delta| = |E_mut|` at the generation-pair separation is **bounded** by the
screened-Poisson propagator (sign-definite, monotone) but **not pinned**: it depends on the
generation-pair localization and on extension beyond the retained channel's calibrated
open-cubic surface (the retained note lists "extension beyond the open cubic calibration
surface" and a clean trajectory channel as still missing). So this note moves `delta` from
"sign and scale both open" to "**sign fixed (attractive), scale bounded**." The next artifact is
the generation-pair separation/localization that converts the bound into a value.

## Boundary (honest)

- **A sign + bound, not a value.** It fixes `sign(delta) = sign(|K|) < 0` and bounds `|delta|`;
  it does not pin the magnitude.
- **Inherits the retained channel's bounded tier.** The attraction is established on the
  retained note's **clean partner-force** observable; that note is `retained_bounded` because
  its staggered trajectory channel is noisier and full Newton on the primary architecture is not
  closed. This note is no stronger than that surface.
- **Load-bearing identification (native, but named).** The result rests on identifying the two
  generation excitations with two quanta of the same matter field `psi` that sources the
  mediator. This is the framework's own definition of generations (the `hw=1` sector of the
  lattice matter field) and the mediator's universal `G|psi|^2` coupling — an application of a
  retained channel, **not** a new field, species, or coupling. It is flagged here so the audit
  lane can weigh it.
- **Forces no flavor value.** This is one overall **sign** of the `C3` coupling; it does **not**
  force `r`, `Q`, or any mixing value (no overreach). `r` remains the registered dial.

## Forbidden imports check

No new axiom and no new import. The mediator `(L + mu^2) Phi = G|psi|^2` and its attractive
partner force are the **retained** (`retained_bounded`) two-body channel, reproduced verbatim;
applying it to two `psi`-quanta (the generation pair) uses the same universal coupling. The
occupation-curvature identity `delta = E_mut` and the sign propagation `sign(|K|) = sign(delta)`
are arithmetic. The magnitude is named open, not asserted.

## Runner check breakdown

Class A: (1) the retained partner force is attractive on `d = 3..7`, sides `12, 14, 16`
(reproducing the published `+0.49557` and the `~d^-1.95` law) and the binding energy
`E_mut < 0` on every row; (2) `|E_mut|` is bounded and monotone in separation; (3) `delta < 0`
yields `sign(|K|) < 0` with the exact `J − I` form, and a counterfactual `delta > 0` flips the
sign. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content reproduces the retained two-body channel's exact attractive partner-force
observable (verbatim conventions and published value), shows the corresponding two-excitation
binding energy is negative and bounded, and propagates `delta = E_mut < 0` into `sign(|K|) < 0`
with the `J − I` form. The result is the **sign** of `delta`/`|K|` plus a magnitude bound,
obtained from a `retained_bounded` surface with no import; it inherits that surface's bounded
tier and forces no flavor value. The one judgement the auditor must weigh is the (native, flagged)
identification of the generation pair with two `psi`-quanta sourcing the universal mediator.
Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/delta_sign_from_retained_mediator_runner.py
```
