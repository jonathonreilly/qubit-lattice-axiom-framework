# Dynamics Lane — Charter + Step 1: the Generation-Sector Action Is Forced to `A cos3δ + B cos6δ`; the Target Is "phase = variance"

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. Steps 1–5 are forced by symmetry (exact); the
locking (Step 6 target) is the lane's open dynamical computation, explicitly flagged. Sets no audit
status.
**Primary runner:** [`scripts/frontier_dynamics_lane_step1_generation_action_phase_variance_discriminator.py`](../scripts/frontier_dynamics_lane_step1_generation_action_phase_variance_discriminator.py)
**Authority role:** charters the new **dynamics lane** (the asymptotic-safety / functional-RG route
to the gauge-singlet flavor *values*, run through the framework's forced gravity/emergent time) and
records its **Step 1** result: the generation-sector effective potential *form* is forced by the
axioms, and the decisive target is sharpened to **phase = variance** (`arg(z) = V(N)`).

## Why this lane (and why it is not betting against a theorem)

The framework derives **gauge-tied** quantities (top Yukawa, couplings, VEV, Q=2/3, the radial CKM
identities) and admits the **gauge-singlet** flavor *values* (δ, light-mass scales, mixing
orientations). Every prior route (flavon, RG, entanglement, modular/KMS) relocated the admission to
the same place: A1+A2 fix the **kinematics**, not the **state/dynamics**.

The earlier caution — "consistency conditions fix structure not values, so deriving δ is hopeless" —
is **withdrawn**: a **fixed point is dynamics, not a consistency condition**, and fixed points *do*
fix values. Asymptotic safety (Eichhorn–Held) predicted the **top-Yukawa value** and fixed the
Abelian coupling from a **gravitational** fixed point. The framework *forces* gravity + emergent
time — the asymptotic-safety ingredient — so this lane imports the one mechanism known to produce SM
Yukawa values, into a setting uniquely built to host it.

## Lane charter — milestones and exit criteria

| # | Milestone | Status |
|---|---|---|
| **0** | Reframe the target: `δ=2/9 ⟺ 3δ=Q ⟺ δ=V(3)` (rational phase-locking, not a transcendental) | **done** (`DYNAMICS_LANE_SEED_…NOTE`) |
| **1** | Derive the generation-sector effective-potential *form* from A1+A2; separate axiom vs dynamical assumption; sharpen target to **phase = variance** | **done (this note)** |
| **2** | Write the dynamical flavon kinetic term + the gravity coupling (the asymptotic-safety setup) from A1+A2 | open |
| **3** | **Decisive:** compute the generation-sector β-function (functional RG / Wetterich) and test whether the IR fixed point **locks** `arg(z) → V(N)`, i.e. `A/B → −4cos(2/3)` | open |
| **4** | If locked: derive the radius (the overall mass scale) and close the light-mass values | open |

**Exit criteria (binary, either is a result):**
- **Locks** → `δ = V(3) = 2/9` (leptons) and `V(6) = 5/36` (quarks) become *predictions* inherited
  from retained radial structure — a derived flavor value, beyond the SM.
- **Does not lock** → δ is confirmed genuine state/boundary data; the admission is proven irreducible.

The lane runs **in parallel** with the Tier-1 audit campaign (the retainable radial structure);
they are independent.

## Step 1 result — the potential form is forced (exact), the phase is the residual

From A1 (per-site complex structure / Cl(3) pseudoscalar ⇒ a genuine U(1) phase `δ=arg(z)`),
A2 (locality/analyticity), the retained C₃ generation structure (the nontrivial-character amplitude
`z = (λ₁+ω̄λ₂+ωλ₃)/√3 = r e^{iδ}`, clock acting `z→ωz`), and retained CP-evenness (`z→z̄`, real
couplings):

1. **C₃-clock invariance** ⇒ only `|z|²` and `z^{3m}` survive ⇒ `V = f₀(|z|²) + Σ_m c_{3m}(z^{3m}+c.c.)`.
2. **CP-evenness** ⇒ real `c_{3m}` ⇒ **cosines only**: `z^{3m}+z̄^{3m} = 2r^{3m}cos(3mδ)`. At fixed
   radius (on the cone): **`V(δ) = A cos(3δ) + B cos(6δ) + …`** — the flavon spontaneous-CP potential
   *derived*, not postulated; the `3` is the C₃/generation number.
3. **Relevance ordering** (locality): cubic `A` ≫ sextic `B` ≫ … ⇒ the two-harmonic truncation is
   RG-justified.
4. **The cone fixes the radius:** the retained `|z|/a₀ = 1/√2 ⟺ Q=2/3` fixes the *radial* structure
   — the mean/variance data `M(3)=Q=2/3`, `V(3)=2/9`, with the retained universal `V(N)=M(N)/N`.

> **The phase is the whole admission.** The cone fixes the radius; the residual azimuthal
> **phase `δ = arg(z)`** is exactly the quantity left open at Step 7 of the retained cone derivation
> (`TRUE_NO_PREDICTION`). Everything admitted is this one phase.

## Step 6 target, stated cleanly: **the phase equals the variance**

The spontaneous-CP minimum is `cos(3δ) = −A/(4B)`. The framework's bet `δ = 2/9` is *exactly*
`3δ = Q ⟺ δ = Q/3 = V(3)`. Stripped of the radian-bridge dressing:

> **`arg(z) = δ = V(N) = (N_gen−1)/N_gen²`** — the azimuthal **phase** locks to the radial
> **variance**. The radial structure already *contains* `V(3)=2/9` as a combinatorial fact; the open
> dynamical statement is that the phase locks onto it.

**Novel prediction (the lane's first falsifiable output).** Because `V(N)=M(N)/N` holds for all `N`,
the *same* locking on the **quark** sector (`N_quark=6`) gives the azimuthal phase `V(6)=5/36`. The
retained CKM CP structure already carries `η² = 5/36 = V(6)` as the *radial* variance; the prediction
is that the quark azimuthal CP phase (beyond the radial `cos²δ_CKM=1/n`) is `5/36 rad` at the same
fixed point. **One rule `phase = V(N)` → `2/9` (leptons) and `5/36` (quarks).**

## Axiom vs added-assumption ledger (honest)

- **Derived (A1+A2 + retained C₃ + CP):** the order parameter `z`; the potential *form*
  `A cos3δ + B cos6δ + …`; cosines-only; the relevance ordering; the cone fixing `M(3), V(3)`.
- **Added dynamical assumptions (the lane's new inputs, NOT from A1+A2):** (1) `z` is a *dynamical*
  flavon (kinetic term + RG flow) — required because static/geometric phases are `q·π`, never a bare
  rational; (2) `A,B` fixed by an **IR fixed point** (asymptotic safety via forced gravity);
  (3) **weakest link** — the fixed point *locks* `arg(z) → V(N)`.

## What is and isn't claimed

- **Exact:** the forced potential form (clock+CP); `z^{3m}+z̄^{3m}=2r^{3m}cos(3mδ)`; the retained
  Bernoulli data `M(3)=2/3, V(3)=2/9, V(6)=5/36, V(N)=M(N)/N`; `δ=2/9 ⟺ 3δ=Q ⟺ δ=V(3)`.
- **Established (reading):** the admitted quantity is exactly the phase `arg(z)`; the target is
  `phase = variance`; the quark analogue `V(6)=5/36` is a single-mechanism prediction.
- **Not claimed (the lane's open work):** that the flow *locks* the phase to the variance (milestone
  3); any derivation of δ or the mass scales. No PDG/fitted input. Sets/changes no audit status.

## Cross-references (plain-text, non-load-bearing)

- `DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md` — milestone 0 (the reframe).
- `.claude/science/derivations/generation-sector-action-and-phase-variance-target-2026-05-26.md` — the full Step-1 derivation.
- `.claude/science/derivations/charged-lepton-koide-cone-2026-04-17.md` — the retained cone (radial)
  and the open Step-7 phase this lane targets.
- `CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md` — the retained Bernoulli family
  `V(N)=M(N)/N`, `V(3)=2/9`, `V(6)=5/36`.
- `KOIDE_DELTA_MODULAR_KMS_PERIOD_NOTE_2026-05-26.md` — the modular/KMS state-selection the fixed
  point must realize; the gravity handle aligns with asymptotic safety.

## Command

```bash
python3 scripts/frontier_dynamics_lane_step1_generation_action_phase_variance_discriminator.py
```

Expected output: `PASS=15 FAIL=0`.
