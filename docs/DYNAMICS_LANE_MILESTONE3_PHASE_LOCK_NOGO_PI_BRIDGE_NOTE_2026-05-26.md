# Dynamics Lane — Milestone 2+3 (Decisive): Fixed-Point Dynamics Cannot Make `δ=2/9`; the Value Is the Retained Variance `V(3)`, and the Residual Is the π-Bridge

**Date:** 2026-05-26
**Claim type:** no_go (bounded) + bounded_theorem (the relocation)
**Status authority:** independent audit lane only. Branch-local physics-loop result; sets no audit
status. The π-bridge arithmetic and the route table are exact; the no-go is **bounded** by the
algebraic-fixed-point assumption, explicitly flagged. Author status: **exact negative boundary +
positive relocation**, audit required before any effective status.
**Primary runner:** [`scripts/frontier_dynamics_lane_milestone3_phase_lock_nogo_pi_bridge_discriminator.py`](../scripts/frontier_dynamics_lane_milestone3_phase_lock_nogo_pi_bridge_discriminator.py)
**Authority role:** the dynamics lane's decisive milestone-3 test (does an IR fixed point lock
`arg(z)→V(N)` as a radian phase?). It resolves **NO LOCK** under standard algebraic fixed-point /
mode-locking / group-theoretic dynamics, and relocates the value to the retained combinatorial
variance, isolating the genuine residual as the kinematic π-bridge.

## Milestone 2 (the dynamical layer): setup, forced vs assumed

The forced form (Step 1, prior note) is `V(δ)=A cos3δ + B cos6δ` for the C₃ order parameter
`z=r e^{iδ}`. The dynamical layer **adds**: (D1) `z` is dynamical (kinetic term); (D2) `A,B` are
fixed by an IR fixed point (the asymptotic-safety mechanism — gravity made the top-Yukawa value a
fixed-point prediction in Eichhorn–Held); (D3, the decisive bet) the fixed point **locks**
`arg(z)→V(N)`, i.e. `A/B → −4cos(2/3)`, giving `δ=2/9`.

## Empirical anchor: `δ=2/9` is a genuine, precise radian phase

`δ=2/9` rad as the **offset** from the C₃-symmetric point reproduces the charged-lepton √-mass
vector to **~7×10⁻⁶** (fit: `4.411 rad = 4π/3 + 0.22222`). So this is not a loose proxy — `δ=2/9` is
a real, precise radian phase. That makes the milestone-3 obstruction substantive, not semantic.

## Milestone 3 (decisive): NO LOCK — five routes, one wall

| Route | Mechanism | Why it fails |
|---|---|---|
| **R1** | polynomial-truncation FRG fixed point | `β=0` has **algebraic** solutions; `−4cos(2/3)` is **transcendental** (Lindemann–Weierstrass: `cos` of nonzero algebraic is transcendental) |
| **R2** | anomalous-dim-flipped irrelevant cubic | fixed value is a **loop constant** (rationals, π, ζ); `cos(2/3)` is none of these |
| **R3** | mode-locking / Arnold tongue | locks to `2π·(p/q)`; natural value `2π/9`; `2/9 = 1/(9π)·2π` is **not** `2π·(p/q)` for small p,q |
| **R4** | C₃ group characters | `cos(2πk/3) ∈ {1,−1/2}` (**algebraic**); target needs `cos(2/3)`, a **different** (transcendental) number |
| **R5** | gravitational asymptotic safety (Eichhorn–Held shape) | same algebraic/loop wall; the cubic is **relevant** in d=4 (`dim = 4−3 = 1`) so `δ` rides a **free** direction unless `γ>1/3` |
| (R6) | canonical modular/KMS phase | `q·π`, not `2/9` — ruled out in the prior KMS note |

### The one wall, made exact — the π-bridge
```
δ = (2π/9)/π = 2/9 ,      3δ = (2π/3)/π = 2/3 .
```
Every dynamical/geometric angular mechanism produces the **`2π/9` family** with **algebraic** cosines
(the C₃ character `cos(2π/3) = −1/2`). The flavor phase is that geometric angle **divided by π** — a
bare rational. The factor of π is **transcendental**, and no algebraic fixed-point value, loop
constant `{π, ζ}`, mode-lock value `2π·(p/q)`, or C₃ character equals `cos(2/3)`. All five routes
hit this same π-wall. (Bounded: an unknown transcendental conspiracy is not excluded — only shown to
require **tuning**, i.e. `δ` would be an input, not a prediction.)

## The positive relocation (the lane's real output)

The **value** `2/9` is **not** a dynamical fixed point — it is the **retained combinatorial
variance** `V(3) = (N_gen−1)/N_gen²` (counting), already in the repo's Bernoulli family with
`V(N)=M(N)/N` and the quark analogue `V(6)=5/36 = ` the retained CKM `η²`. **Dynamics neither
supplies nor is needed for the value.**

> **The "missing dynamics" the panels kept invoking is a mirage for the VALUE.** The flavor *value*
> is **counting** (the retained variance `V(3)`), not a dynamical fixed point. What is genuinely open
> is purely **kinematic**: the **radian-bridge license** — why a counting-variance enters a cosine as
> a radian (the missing, transcendental **factor of π**). That is a geometry/kinematics question, not
> a missing dynamical principle.

This **completes the lane**: milestone 3 resolves **NO LOCK** (bounded), refined to "`δ=2/9` =
retained `V(3)` + open π-bridge." Milestone 4 (mass-scale closure) and the quark `V(6)=5/36`
prediction inherit the same relocation — combinatorial, not dynamical.

## What is and isn't claimed

- **Exact:** the π-bridge arithmetic (`δ=(2π/9)/π`, `3δ=(2π/3)/π`); `cos(2πk/3)∈{1,−1/2}`;
  `cos(2/3)` transcendental (L-W); `2/9=V(3)`, `5/36=V(6)`; the d=4 cubic mass-dimension; the
  empirical `~7×10⁻⁶` lepton-mass match at `δ=2/9`.
- **Bounded no-go:** no standard *algebraic* fixed-point / mode-locking / group-theoretic dynamics
  produces `δ=2/9` as a radian phase; achieving it requires tuning (⇒ `δ` an input). Bounded by the
  algebraic-fixed-point assumption (passes the N1–N8 no-go gate; see `NO_GO_LEDGER.md`).
- **Relocation (bounded theorem):** the value `2/9` is the retained variance `V(3)`; the residual is
  the kinematic π-bridge.
- **Not claimed:** an absolute impossibility (a transcendental conspiracy is not excluded, only shown
  to need tuning); any derivation of the π-bridge; any audit status. PDG used only as the empirical
  anchor, never as a proof input. No new axiom.

## Cross-references (plain-text, non-load-bearing)

- `DYNAMICS_LANE_CHARTER_AND_STEP1_GENERATION_ACTION_NOTE_2026-05-26.md` — milestones 0–1; this is 2–3.
- `DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md` — the `3δ=Q` reframe the
  π-bridge now explains (the factor of π between `2π/3` and `2/3`).
- `KOIDE_DELTA_MODULAR_KMS_PERIOD_NOTE_2026-05-26.md` — R6 (canonical modular phase = q·π).
- `CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md` — the retained `V(3)=2/9`,
  `V(6)=5/36`, `V(N)=M(N)/N` the value relocates onto.
- `.claude/science/physics-loops/dynamics-lane/NO_GO_LEDGER.md` — the N1–N8 discipline record.

## Command

```bash
python3 scripts/frontier_dynamics_lane_milestone3_phase_lock_nogo_pi_bridge_discriminator.py
```

Expected output: `PASS=17 FAIL=0`.
