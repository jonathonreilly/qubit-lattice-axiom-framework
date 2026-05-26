# Direction γ — Native Isolation of the π-Bridge Gap

**Date:** 2026-05-26 (cycle 3 of native-only campaign)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** research analysis — sharpened residual statement
**Imports:** NONE (uses only retained content + standard math)
**Status:** **not a closure**, **not a no-go theorem**, **not a theorem note**;
a precise characterization of what new content would close the π-bridge primitive
`P`, derived from the retained no-go inventory + Lindemann-Weierstrass.

## The π-bridge primitive `P` (recap from retained content)

`P` = the open identification of the dimensionless rational `2/9` (the
Plancherel-Frobenius rational `2/d²` at `d = 3`, retained per Probe 24) with
the literal radian value `2/9 rad`.

Six retained no-gos confirm `P` is not derivable from the existing retained
inventory (per `retained_no_go` audit verdicts on `origin/main`):

- `koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24` (`retained_no_go`)
- `koide_a1_physical_bridge_attempt_2026-04-22` (`retained_no_go`)
- Probes 20, 24 (Z₃-qubit Pancharatnam-Berry, native-angle exhaustion)
- Selected-line local Berry no-go
- Dimensional-inventory exhaustion (Probe 30)
- Expanded-dimensionless-inventory exhaustion (2026-05-10)

## Lindemann-Weierstrass on the retained Q-algebraic basis

**Theorem (Lindemann 1882, Weierstrass 1885):** `π` is transcendental over `ℚ`.
Equivalently, `π` is not algebraic over `ℚ`; no finite polynomial equation with
rational coefficients has `π` as a root.

**Corollary on the retained framework basis.** The retained dimensionless
inventory (per `RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp`
on `origin/main`) consists of rational numbers `q ∈ ℚ` plus `π`-containing items
that themselves trace back to the QED-convention `α_bare = 1/(4π)` — which IMPORTS
`π` via the period-`2π` convention rather than deriving it.

Therefore:

```
The Q-algebraic span of the retained inventory does not contain 2π
(or any non-Q-multiple of π).
```

This is a tight blocker on any derivation chain of the form
`δ = (rational from retained) × (2π) = 2π · p/q`.

## Type-A vs Type-B (retained from the irreducibility audit)

From `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md` (`retained_no_go`):

- **Type A** (periodic phase quanta from retained sources): APBC Matsubara,
  Brillouin-zone momenta, Z₃ characters, Wilson monodromies, closed-orbit Berry.
  All of the form `q·π` for `q ∈ ℚ`.
- **Type B** (combinatorial / representation-counting rationals): dimension
  counts, Plancherel weights, Casimir ratios, charge products. Pure rationals
  in `ℚ`.

The two numerical sets are disjoint away from zero:

```
{q·π : q ∈ ℚ} ∩ ℚ  =  {0}.
```

The target `δ = 2/9 rad` is **a nonzero element of `ℚ` read as a radian**.
It is Type-B (a pure rational) appearing in a Type-A slot (a radian).
**The bridge gap = the unit-mismatch: a Type-B number being read as a Type-A
literal-radian quantity.**

## Sharpened gap statement

The π-bridge gap is precisely:

> **`P` requires a retained source-class that produces a non-Q-algebraic radian
> value of magnitude `2/9 rad`, OR a retained re-expression of the lepton mass
> observable that does not interpret `2/9` as a radian at all.**

Equivalently, the gap is at one of three logical positions:

**Position 1 — A native irrational-radian source.**

The framework needs a retained native construction whose output is a
non-Q-algebraic angle of magnitude exactly `2/9 rad`. Such a source must:

- Not be a Q-algebraic combination of existing retained rationals (blocked by L-W).
- Not be `q·π` for any `q ∈ ℚ` (blocked by `{q·π} ∩ ℚ = {0}`).
- Therefore: must come from a structural primitive currently outside A1+A2 +
  retained inventory.

**This position is currently empty** in the retained framework. The closing
input would be either a NEW STRUCTURE that yields irrational radians natively,
OR a derivation that produces `2/9 rad` from a continuous limit of retained
discrete structures.

**Position 2 — A native re-expression of the Brannen circulant.**

The Brannen formula `cos(2πk/3 + δ)` interprets `δ` as a radian. If the lepton
mass observable can be re-expressed in a form `m_k² = F(Q, k)` where:

- `Q = 2/3` is the retained Koide ratio (dimensionless).
- `k ∈ {0,1,2}` is the C₃ irrep label.
- `F` is a function that does not internally use `δ` as a radian (e.g. a polynomial
  in `Q`, or a determinantal identity, or a character-algebra contraction).

then the literal radian interpretation `δ = 2/9 rad` becomes a coordinate
artifact of the cosine parameterization, not a structural claim.

**This position is at the L-W boundary**: any such `F(Q, k)` that REPRODUCES the
Brannen eigenvalue triplet must either (a) be algebraically equivalent to
`cos(2πk/3 + Q/3)` and therefore still contain the radian implicitly, OR
(b) be inequivalent (giving different eigenvalues) and therefore not the same
observable. The four candidate substrates (K1-K4 from the closed scoping
PR #1942) each face this: any `Q`-rational re-expression that matches the
Brannen triplet at first order in `Q` returns to the radian interpretation at
higher order.

**Position 3 — A native dynamics that produces `δ` as an output without going
through `2π·(rational)`.**

Per the sector-mismatch finding (`DIRECTION_ALPHA_FIRST_CYCLE_*` and
`CHAIN5_VERIFICATION_EXPANDED_*`), the verified retained native dynamics
(decoherence, self-gravity, cycle-battery, retarded-propagation, staggered)
all operate in sectors orthogonal to the C₃ generation-sector. A
sector-coupling result is what's missing.

**This position requires either** (a) a retained sector-coupling result not
yet located (an active locate task), OR (b) a new derivation that produces
such a coupling natively. The retained no-gos (physical-bridge, radian-bridge
irreducibility) don't prove this position is unreachable, only that the routes
attempted so far don't reach it.

## What the lane has therefore established

This cycle's contribution is a **precise structural diagnosis of the π-bridge
gap**:

- The gap is not a missing dynamics (M-work attempted this, retained no-gos
  confirm dynamics-only-style attacks hit walls).
- The gap is not a missing import (refusing imports doesn't make the gap
  bigger or smaller — the gap is in the retained content's structural reach,
  not in what's been excluded).
- The gap is **a missing source-class for non-Q-algebraic radian magnitudes**,
  OR equivalently a missing native re-expression of the Brannen observable
  that doesn't pass through `δ`-as-radian.

This is sharper than "the π-bridge is open" — it names the exact class of
structural input that would close it.

## What this cycle does NOT claim

- Does **not** assert that `P` is closable. The diagnosis sharpens the gap;
  it does not propose how to fill it.
- Does **not** assert a new no-go beyond what's already retained.
- Does **not** propose a new axiom or import.
- Does **not** open a source PR.
- Does **not** assert any audit status. Branch-local research-lane analysis.

## What's available as a candidate small-PR

The Type-B-vs-Type-A unit-mismatch statement (the `{q·π} ∩ ℚ = {0}` formal
consequence) is already in `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`
on `origin/main` as `retained_no_go`. So a "Type-A vs Type-B sharpened-residual"
PR would be redundant.

The **three-position framing** here (Position 1: irrational-radian source;
Position 2: re-expression; Position 3: sector-coupling) is **a new structural
diagnosis** that decomposes the open `P` into three mutually-exclusive closing
routes. This may be a candidate small-PR if the user wants a no-go decomposition
note landed.

**Decision deferred to user.** This research-lane cycle records the diagnosis;
no PR is opened.

## Next cycle

Direction δ — boundary-condition reading of C₃ + Cl(3) without dynamics. Test
whether a boundary condition (e.g. C₃-orbit closure matching, Cl(3) eigenstate
selection rule) can bind `δ` natively without invoking any dynamics.

## Cited retained sources (load-bearing)

- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md` (`retained_no_go`):
  Type-A vs Type-B distinction; `{q·π} ∩ ℚ = {0}`.
- `KOIDE_A1_PHYSICAL_BRIDGE_ATTEMPT_2026-04-22` (`retained_no_go`): physical-bridge
  obstruction.
- `RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp` (per the
  irreducibility audit's cross-references): retained-inventory L-W blocker.
- `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`: Brannen circulant
  kinematic shape (provenance for the `cos(2πk/3 + δ)` formula being analyzed).
- Lindemann-Weierstrass theorem (standard math, not a framework import).
