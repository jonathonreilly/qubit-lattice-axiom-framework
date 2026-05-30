# Flavor — the Koide problem *is* a spontaneous translation-breaking problem

**Date:** 2026-05-29
**Claim type:** session capstone / native reframing (NOT a derivation of 2/3).
Imports nothing.
**Runner:** `scripts/flavor_translation_breaking_reframing_2026_05_29.py` (+ cache).
Synthesizes the entire 2026-05-29 dynamical arc into one crisp native statement.

## The reframing
Generations = the three hw=1 momentum (BZ) corners (retained taste=momentum
identification). The generation Yukawa is `Y = aI + bC + b̄C²` with
`Q = 1/3 + (2/3)r`, `r = |b|²/a²`, where `a` is the **diagonal** corner mass and
`b` the **off-diagonal** corner↔corner coupling. The two corners differ by the
momentum `Q* = (π,π,0)`.

**Two native facts collide:**
1. **Translation invariance (axiom A2)** makes any translation-invariant
   mass/vacuum **diagonal in the momentum basis** → `b = 0` *exactly* (momentum
   conservation). Verified for a generic translation-invariant kernel.
2. The Koide relation `Q = 1/3 + (2/3)r` is a structural prediction *of* the
   circulant (`b≠0`) form — 2 parameters `(a,b)` generate the constrained 3-mass
   spectrum. With `b=0` you have **3 independent diagonal masses**: `Q=2/3` is
   then only a *tuned coincidence* (3 free numbers hitting one value), **not the
   Koide relation**.

**Therefore:** the *predictive* Koide relation (`Q=2/3` to 1e-5, a relation not a
coincidence) requires `b≠0`, which requires the vacuum to carry a condensate at
`Q*=(π,π,0)` — i.e. **spontaneous translation-symmetry breaking by exactly the
corner-connecting (staggered) momentum, at strength `b/a = 1/√2`.**

## Why this is the right capstone
The fermion vacuum does **not** spontaneously break translation — three
independent computations this session (coupled gap equation, competing-orders
scan, fermion effective potential) all show the uniform condensate wins, `b→0`,
`Q=1/3`. So:

> **The Koide value problem == a spontaneous translation-symmetry-breaking
> problem**, unsupplied by the native fermion-vacuum dynamics.

This single statement unifies the whole arc:
- *"flat direction" (retracted)* → the isolated-sector artifact;
- *nonperturbative vacuum output* → it lives in the vacuum, not the operator;
- *native Jahn-Teller instability* → a translation-invariant (diagonal,
  S₃-breaking) order, which gives `b=0` and only the `1+2` degenerate spectrum,
  capped — **not** the circulant relation;
- *value = off-diagonal/diagonal ratio `r=½`* → `b/a=1/√2`;
- *multicritical coexistence* → the staggered order competes with the uniform
  one and loses;
- *heat-kernel frame* → diagonal in the physical (momentum) basis → `b=0`;
- **all of it is the one statement** that `b≠0` needs translation breaking at
  `(π,π,0)` that the dynamics does not spontaneously produce.

## Status (open gate, sharply named — not a wall)
This is **not** a claim that `Q=2/3` is underivable. It is the cleanest possible
statement of *what must happen and where it must come from*:
- **What:** the vacuum must carry a **staggered scalar condensate at
  `(π,π,0)`** (the corner-connecting momentum) at strength **`b/a = 1/√2`**.
- **Where:** since the fermion determinant won't supply it (3 computations), it
  must come from **structure outside the fermion determinant** — the derived
  `g_bare=1` (bridge-gap) action's channel structure, or a non-fermionic
  (gauge/link) vacuum sector.

No false closure: the gate is now named in the most physical, native terms the
campaign has reached — a spontaneous translation-breaking order parameter — which
is a *concrete, computable* target for the bridge-gap action, not an abstract
modulus.
