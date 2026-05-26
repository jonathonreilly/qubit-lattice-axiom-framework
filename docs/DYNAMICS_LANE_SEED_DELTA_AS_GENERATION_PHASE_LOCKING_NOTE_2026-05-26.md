# Dynamics-Lane Seed: the δ=2/9 Target Is a Phase-Locking `3δ = Q_Koide` (δ = Q/N_gen), Not a Transcendental

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. The algebra is exact; the "locking is a
fixed point" is the dynamics lane's *target*, explicitly flagged as a proposal, not a derivation.
Sets no audit status.
**Primary runner:** [`scripts/frontier_koide_delta_generation_locking_fixedpoint_seed_discriminator.py`](../scripts/frontier_koide_delta_generation_locking_fixedpoint_seed_discriminator.py)
**Authority role:** seeds the **dynamics lane** — the asymptotic-safety / functional-RG route to
the gauge-singlet flavor *values*. It reframes the long-standing δ target from an apparently
untouchable transcendental coupling into a tractable rational phase-locking, and states the lane's
single decisive computation precisely.

## Why a dynamics lane (the diagnosis, updated)

Traditional lattice QFT cleanly separates **kinematics** (degrees of freedom, lattice, symmetry —
what A1+A2 fix and the framework derives from) from **dynamics** (the action, supplied separately;
physical *values* set by the critical / fixed-point structure). The flavor *values* (δ, light-mass
scales, mixing orientations) are exactly the dynamical, gauge-singlet data — admitted across the
flavon, RG, entanglement, and modular/KMS routes.

The earlier caution — "consistency conditions fix structure, not values, so deriving δ is betting
against a near-theorem" — was **too strong and is withdrawn**. A **fixed point is dynamics, not a
consistency condition**, and fixed points *do* fix values: the asymptotic-safety program
(Eichhorn–Held) predicted the **top-Yukawa value** and fixed the Abelian coupling from a
**gravitational** fixed point. The framework *forces* gravity + emergent time (anomaly-forces-time)
— precisely the asymptotic-safety ingredient. So the dynamics lane bets on the one mechanism that
has already produced SM Yukawa values; it is well-founded, not quixotic.

## The reframing (exact algebra)

The C₃-clock + CP flavon potential is `V(δ) = A cos(3δ) + B cos(6δ)` (the `3δ` harmonic is forced
by the C₃ clock symmetry). Its spontaneous-CP stationarity is

```
cos(3δ) = −A/(4B).
```

The long-standing target `δ = 2/9 ⟺ A/B = −4 cos(2/3) ≈ −3.1435` is therefore **exactly**:

```
cos(3δ) = cos(2/3)   ⟺   3δ = 2/3   ⟺   3δ = Q   ⟺   δ = Q / N_gen
```

where **`Q = 2/3` is the RETAINED Koide cone** (`w_axis = w_perp = 1/2 ⟺ Q = 2/3`) and **`N_gen = 3`**
is the generation/clock number. It is a **genuine** spontaneous-CP minimum (`0 < |A/B| < 4`, `V'' > 0`).

> **The dynamics lane's target restated:** the azimuthal phase δ, **wound by the generation number 3**
> (the `cos 3δ` harmonic), **locks to the radial Koide cone Q** — a quantity the framework already
> derives and retains. δ = 2/9 is then `Q/3`, inherited from `Q = 2/3` by a **commensurability**
> (3:1 mode-locking) condition.

## Why this is the right *shape* for a dynamics computation

- A **generic transcendental** coupling is precisely what a fixed point **cannot** produce without
  tuning. A **rational phase-locking** (the azimuthal winding `3δ` commensurate with the cone `Q`,
  ratio 1:1) is exactly what nonlinear flows produce **without** tuning: **mode-locking / Arnold
  tongues**, resonant RG fixed points, and the asymptotic-safety mechanism that fixed the top
  Yukawa. The target has moved from "implausible for dynamics" to "characteristic of dynamics."
- It **collapses the admission onto a retained quantity.** If the generation-sector flow enforces
  `3δ → Q`, then δ is no longer independent data — it inherits determinacy from the already-derived
  cone `Q = 2/3`. The two-input lepton admission (δ + scale) loses its δ.

## The lane's single decisive computation

Write the generation-sector Wilsonian / functional-RG action consistent with A1+A2 (gauge
invariance, the C₃ clock symmetry, locality), compute the β-functions of the flavon self-couplings
(the operators generating `A` and `B`), and test whether the IR fixed point **locks** `3δ → Q`
— i.e. whether `A/B → −4 cos(Q)` is an attractor. Outcome is decisive either way:

- **Locks** → δ = Q/3 = 2/9 becomes a *prediction* inherited from the retained cone — the flavor
  value is derived, a result beyond the SM.
- **Does not lock** → δ is confirmed genuine boundary/state data, and the admission is irreducible.

This is the asymptotic-safety template applied to the gauge-singlet sector, through the framework's
forced gravity/emergent-time — the natural first major target of the dynamics lane.

## What is and isn't claimed

- **Exact (algebra):** the stationarity `cos 3δ = −A/4B`; `A/B = −4cos(2/3) ⟺ 3δ = Q = 2/3 ⟺
  δ = Q/N_gen` (`N_gen=3`); a genuine minimum (`0<|A/B|<4`, `V''>0`); the `3` is the C₃-clock harmonic.
- **Established (reading):** the dynamics target is a rational phase-locking of an admitted phase to
  a retained quantity — fixed-point-natural, unlike a transcendental.
- **Not claimed (the lane's open computation):** that the generation-sector flow *enforces* the
  locking. That single FRG fixed-point computation is the lane's first decisive task; it is **not**
  done here. No derivation of δ is asserted. Sets/changes no audit status; PDG/precedent only as
  context.

## Cross-references (plain-text, non-load-bearing)

- `KOIDE_DELTA_RG_RUNNING_TRANSCENDENCE_NOTE_2026-05-25.md` — why `cos 3δ` looked transcendental;
  the locking reframing dissolves that.
- `KOIDE_DELTA_RG_FIXEDPOINT_AND_LEPTONMASS_STATE_NOTE_2026-05-25.md` — the fixed-point/lepton-mass
  state this lane attacks.
- `KOIDE_DELTA_FLAVON_SPONTANEOUS_CP_BUILD_NOTE_2026-05-25.md` — the `V(δ)=A cos3δ+B cos6δ` skeleton.
- `FLAVOR_CP_RADIAL_AZIMUTHAL_GEOMETRY_NOTE_2026-05-25.md` — Q (radial, derived) vs δ (azimuthal,
  admitted); the locking ties them.
- `AXIOM_NATIVE_FLAVOR_ENTANGLEMENT_AND_EMERGENT_TIME_NOTE_2026-05-26.md` /
  `KOIDE_DELTA_MODULAR_KMS_PERIOD_NOTE_2026-05-26.md` — the state-selection / modular admission the
  lane must close; the gravity handle aligns with asymptotic safety.

## Command

```bash
python3 scripts/frontier_koide_delta_generation_locking_fixedpoint_seed_discriminator.py
```

Expected output: `PASS=13 FAIL=0`.
