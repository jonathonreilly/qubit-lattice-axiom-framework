# The Gravity Sign (Attraction) Is Not Forced by the Arrow, Energy-Stability, or Spectral Routes — the Records Give the Poisson Law + Magnitude, the Sign Is the Residual (No-Go Sharpening)

**Date:** 2026-06-08
**Claim type:** no_go (sharpening; closes three "broader selector" routes for the gravity sign and locates it)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/gravity_sign_not_forced_by_arrow_stability_spectral_runner.py`](../scripts/gravity_sign_not_forced_by_arrow_stability_spectral_runner.py)
**Cached output:** [`logs/runner-cache/gravity_sign_not_forced_by_arrow_stability_spectral_runner.txt`](../logs/runner-cache/gravity_sign_not_forced_by_arrow_stability_spectral_runner.txt)

## Audit context

The emergent-gravity arc this session derived the metric's conformal class (lensing) from records and
located the scale (Shapiro) as the clock-rate no-go. The remaining source-curvature object is the
**sign** (attraction): the Poisson **law** is retained
([`SELF_CONSISTENCY_FORCES_POISSON`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md), `retained_bounded`:
`Lφ=−Gρ`), but the sign of the coupling is open —
[`SIGNED_GRAVITY_CHI_SELECTOR`](SIGNED_GRAVITY_CHI_SELECTOR_THEOREM_OR_NOGO_NOTE.md) (`unaudited`)
found the **local/taste-cell** selector fails, leaving *"broader selector constructions"* open. This
note closes three of those broader routes — including the **global arrow/entropy** route the session's
emergent-time work suggested — as **not** forcing the sign, and so **locates** it.

## Safe statement

**Theorem (three records-native routes do not force the gravity sign).** On the retained Poisson
surface `Lφ=−Gρ` (`L`=graph Laplacian), attraction ⟺ `G>0`. None of the following force `G>0`:

1. **Spectral route — magnitude only.** The massive graph Green's function `(L+μ²)⁻¹` has **all
   positive entries** (heat-kernel positivity), so the two-body energy `E=−G·ρ_A^⊤(L+μ²)⁻¹ρ_B` has
   `|E|` fixed but **sign `E` = −sign `G`**: the Green's function is **blind to `sign(G)`**. The
   spectral structure gives the *magnitude*, not the sign.
2. **Energy-stability route — favors the WRONG sign.** For `G>0` (attraction) the self-energy
   **decreases as the configuration clumps** (`σ→0`) — **unbounded below**, no ground state (the
   physically-correct gravitational instability). For `G<0` (repulsion) it is **bounded** (the
   spread-out minimum). So demanding a bounded-below ground state would select **repulsion** — the
   stability argument **cannot force attraction**.
3. **Arrow/entropy route — sign-agnostic.** Clumping **lowers** the matter configurational entropy
   (`S(clumped)<S(uniform)`, verified); entropy rises only via *other* channels (gravitational/kinetic
   dof, à la Penrose) **and** cosmic **expansion** also raises entropy. So "entropy increases" does
   **not** uniquely pick attraction — the records' **arrow fixes the time-direction, not the spatial
   force sign.** (This **refutes** the Penrose-arrow candidate the session's arrow work suggested.)

**Conclusion.** The records derive the Poisson **law** and the positive Green's-function **magnitude**;
the coupling **sign** is a separate **residual**, consistent with the conformal-factor **records-clock-rate boundary**
([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md), `retained_no_go`)
and the local χ-selector no-go. The sign is a **single located residual**, not three open routes.

## What this contributes

- It **closes three "broader selector" routes** the local χ-selector note left open (global/arrow,
  energy-stability, spectral) — narrowing the sign search.
- It **self-corrects** the session's natural conjecture (the arrow fixes the sign): the arrow is
  sign-agnostic; entropy increase is compatible with both clumping and expansion.
- It surfaces the precise reason energy-stability fails: **attraction is the no-ground-state
  direction**, so stability selects the wrong sign — a structural fact, not a tuning accident.

## No-go gate (N1–N8)

- **N1 (alternatives).** Five sign routes are separated: spectral magnitude, energy-stability,
  arrow/entropy, the prior local χ-selector, and explicit source/action orientation. This note closes
  only the first three; the local χ-selector already failed, and the source/action orientation route
  remains open rather than silently counted as closed.
- **N2 (wall-independence).** Each failure is structural: heat-kernel positivity (magnitude-only),
  gravitational instability (no ground state), entropy sign-agnosticism — independent of the lattice
  size (verified at `L=4`, the mechanism is `L`-independent).
- **N3 (hidden-wall scan).** The wall is the **sign of the coupling**, located precisely; not a
  circularity (the routes are computed without presupposing the sign — both signs are run).
- **N4 (residual matching).** The residual is the coupling sign. It sits beside the
  records-clock-rate boundary and the χ-selector no-go, but is not the approved scale primitive and
  is not a Planck import.
- **N5 (rhetoric).** No "closes/last/only-route." It bounds three routes and **opens** the sign as a
  located residual; the framework reproduces gravitational phenomenology, so a derivation may exist —
  the next path is *not* arrow/stability/spectral.
- **N6 (partial-closure).** The law + magnitude **are** derived; only the sign is residual — a partial
  closure, not a global block.
- **N7 (steelman).** The strongest pro-arrow case (Penrose gravitational entropy) is granted and shown
  sign-agnostic at the configurational level (entropy rises both ways).
- **N8 (cross-cycle echo).** Consistent with the `unaudited` χ-selector no-go and the `retained_no_go`
  records-clock-rate interface; the sign remains a separate located residual.

## Boundary (honest)

- A **negative/sharpening** result: it rules out three routes and locates the sign; it does **not**
  derive the sign or claim it is *underivable* (broader routes beyond these three remain open).
- The energy-stability "wrong sign" is the correct physics (gravity has no ground state); the point is
  only that *stability cannot be used to select attraction*.
- r=½ and the carrier sectors are untouched.

## Forbidden imports check

No new axiom. A_min + the retained Poisson law + standard finite computations (graph Green's function,
self-energy, Shannon entropy), all at `L=4`. Memory-safe (≤64×64 matrices). The Penrose/entropic-gravity
ideas are *tested*, not imported as authority.

## Runner check breakdown

Class A: (A1) spectral route gives positive magnitude but is `sign(G)`-blind; (A2) energy-stability
favors repulsion (attraction is unbounded-below); (A3) the arrow/entropy is sign-agnostic (clumping
lowers configurational `S`); (A4) the sign is the located residual. Expected `runner_check_breakdown =
{A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

On the retained Poisson surface, attraction ⟺ `G>0`. The massive graph Green's function is entrywise
positive (so the two-body magnitude is fixed but the sign tracks `sign(G)`); the self-energy is
unbounded below for attraction and bounded for repulsion (so stability selects the wrong sign); and
clumping lowers the configurational entropy while expansion raises it (so the arrow is sign-agnostic).
Three records-native routes therefore fail to force attraction, each structurally, and the sign is
located beside the records-clock-rate boundary and the χ-selector no-go. The sign is not equated with
the approved scale-reference primitive. The note is an honest
negative sharpening — it self-corrects the session's arrow conjecture and does not claim the sign is
underivable. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/gravity_sign_not_forced_by_arrow_stability_spectral_runner.py
```
