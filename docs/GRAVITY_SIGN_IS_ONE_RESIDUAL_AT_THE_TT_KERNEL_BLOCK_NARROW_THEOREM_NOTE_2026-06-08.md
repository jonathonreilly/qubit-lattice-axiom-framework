# The Gravity Sign Is One Residual: Newtonian Attraction = TT Graviton Kinetic Health = sign(G), Located at the TT-Kernel Block

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** unification + residual location (collapses the gravity-sign chain to one open primitive)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.py`](../scripts/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.py) (PASS=3).

## What this resolves

The companion attraction-sign note
([`GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR...`](GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md),
in review) reduced the Newtonian attraction sign to "the healthy graviton kinetic sign." This note shows
that **reduction is an identity** — the attraction sign, the TT graviton kinetic health, and `sign(G)`
are the **same number** — and **locates** that single residual at the **TT-kernel block** (the framework's
scalar matter effective action provably cannot source the spin-2 graviton kinetic term). So the entire
gravity-sign question collapses to **one** open primitive: the sign of the geometric Einstein-Hilbert /
Regge coefficient.

## Theorem (bounded, runner-verified)

Write the linearized graviton action `S = (1/2κ) h^{TT} □ h^{TT} + ½ h_{μν} T^{μν}` with `κ = 8πG`.

- **(K1) The unification.** The TT graviton **kinetic** coefficient is `1/(2κ)` (healthy/ghost-free iff
  `κ>0`); the one-graviton-**exchange** static potential is `V ∝ −κ · P_{00,00} · (source)²` with
  `P_{00,00} = +½ > 0` (attractive iff `κ>0`). Hence
  **healthy-TT-kinetic ⟺ attraction ⟺ `κ>0` ⟺ `G>0`** — verified to flip together at `κ=±1` and to track
  `sign(κ)` across a range. The "graviton kinetic health," the "Newtonian attraction sign," and `sign(G)`
  are **one residual**, not a chain.

- **(K2) The block.** The scalar observable generator `W = log|det(D+J)|` sees the metric only through the
  `O_h`-scalar `s(q) = g_{ij} q̂_i q̂_j` (`q̂_i = 2 sin(q_i/2)`), so its per-mode metric-Hessian is the
  **rank-1 longitudinal** form `H = W''(s)·(q̂q̂)⊗(q̂q̂)`. The two actual graviton polarizations `h_+, h_×`
  (transverse to `q̂`, traceless) satisfy `q̂_i h^{ij} = 0`, so `q̂q̂ : h = 0` and
  `⟨h_TT|H|h_TT⟩ = W''(s)·(q̂q̂:h)² = 0` — the **spin-2 graviton is in the exact kernel** (verified over
  thousands of modes, `max|q̂q̂:h_TT| ~ 1e-15`). The matter effective action **provably cannot source the
  spin-2 graviton kinetic term**, hence cannot fix `sign(G)`. (Reproduces / builds on
  [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING...`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md).)

- **(K3) The open route is not trivial.** The induced `1/G` (the Seeley-DeWitt `R`-coefficient) sums over
  fields with **type-dependent signs**, so even the full-vielbein `⟨T_{μν}T_{αβ}⟩` induced-graviton route
  does not automatically give `G>0`. The sign is **content-dependent**.

**Conclusion.** The gravity sign is **one residual** = the sign of the geometric EH/Regge coefficient. The
framework's scalar matter response cannot source it (K2); so it reduces to the **geometric Regge-curvature
coefficient sign** (equivalently the full-vielbein induced-`1/G` sign, content-dependent, K3) — the single
deepest open gravity-sign primitive. This unifies the attraction sign, the graviton kinetic health, and
`sign(G)` and **locates** them all at the TT-kernel block.

## Why this is progress

- It collapses three separately-discussed "sign" statements (Newtonian attraction; healthy graviton
  kinetic term; `sign(G)`) into **one** residual — so future work targets a single object, not three.
- It shows the matter route is **provably dead** for the sign (TT in the kernel of `W`), so the sign is
  necessarily a **geometric** (Regge/EH-coefficient) datum — sharpening the search to the geometric action.
- It cleanly separates the parts that **are** settled (source positivity; the symmetric/non-vector
  mediator class — the companion note) from the **one** that is not (the EH/Regge coefficient sign).

## What is and is not claimed

- **Is:** the attraction sign, the TT graviton kinetic health, and `sign(G)` are the same residual (K1);
  the framework's scalar matter effective action cannot source the spin-2 graviton kinetic term (K2, TT in
  exact kernel); so the gravity sign reduces to the geometric EH/Regge coefficient sign, which is not
  trivially positive (K3).
- **Is not:** does **not** close the sign — the EH/Regge coefficient sign is the open frontier; does
  **not** derive the geometric gravitational action or its coefficient; does **not** import the
  Regge/Lichnerowicz machinery as load-bearing (K3's Seeley-DeWitt signs are an illustration, not a
  framework-specific computation); does **not** touch any registered scale (`G_Newton`). Form/sign level.

## Boundaries (honest)

- **A unification + location, not a closure.** The residual is real and open (the geometric coefficient
  sign / content-dependent induced-`1/G`); this note pins where it lives, not what it is.
- **K3 is illustrative.** It shows induced-`1/G` is content-dependent in general; it does not compute the
  framework's specific matter content's contribution (which, per K2, also does not arise from the scalar
  `W` route anyway).

## Load-bearing inputs

- [`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md`](GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md)
  — locates the sign residual on the retained Poisson surface (`attraction ⟺ G>0`).
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  — the scalar-`W` metric-Hessian is rank-1 longitudinal; TT graviton in its exact kernel (K2).
- [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  — the retained Poisson surface on which the sign question lives.

Companion (in review): the attraction-sign source/action note above (establishes source positivity +
symmetric-mediator class; this note supplies the identity + location).

## Forbidden-imports check

No PDG / fitted value. The `κ`-dependence of the TT kinetic coefficient and the exchange potential is
standard linearized gravity; the TT-kernel contraction is finite tensor algebra (reproduced in the
runner); the Seeley-DeWitt signs in K3 are an explicit illustration, not a load-bearing import. Form/sign
level only.
