# Cycle 7 — Position 1 Native Irrational-Radian Source Search

**Date:** 2026-05-26 (cycle 7 of native-only campaign)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** research analysis — Position 1 of Direction γ (native source for
non-Q-algebraic radian magnitudes)
**Imports:** NONE
**Status:** **negative attack-surface finding** — the retained inventory's
non-Q-algebraic content is **algebraically independent of `π`** in the
relevant transcendence classes; no native combination produces `2/9 rad`.

## Setup

Position 1 of Direction γ asks: does the retained inventory contain a
source-class that produces a non-Q-algebraic radian magnitude of `2/9 rad`?

The Lindemann-Weierstrass blocker says: no Q-algebraic combination of
*rationals* gives `2π`. Position 1 explicitly considers **non-Q-algebraic**
retained quantities — does any of them combine with rationals to produce
`2/9 rad` natively?

## Non-Q-algebraic retained content (per the 2026-05-10 expanded inventory)

From `RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp` and
related retained sources, the non-Q-algebraic items in the retained inventory:

| Item | Class | Source |
|---|---|---|
| `⟨P⟩` (single-plaquette expectation) | numerical lattice MC, class undetermined | SU(3) lattice MC at β=6 |
| `u_0 = ⟨P⟩^{1/4}` (tadpole) | irrational from `⟨P⟩` | derived |
| `α_bare = 1/(4π)`, `α_LM`, `α_s(v)` | `π`-containing (convention import) | QED canonical normalization |
| Heat-kernel `1 - exp(-(4/3)s_t)` | transcendental in `e` | SU(3) heat-kernel closed form |
| Higher Wilson-series products `<P>_W_SU(3)(s_t)` | series in retained rationals | SU(3) NNLO/N5LO closed forms |

## Transcendence class analysis

### `α_bare = 1/(4π)` and derivatives

Trivially `1/α_bare = 4π`. But per the 2026-05-10 note (`retained` bounded):

> `α_bare = 1/(4π)` IMPORTS `π` via the period-`2π` convention, which is the
> same primitive `P` Probe 30 identified. Using `1/α_bare = 4π` to "derive"
> `π` is **structurally circular**.

So `α_bare` cannot serve as Position 1's native source — it inherits `π` from
the convention being closed.

### Heat-kernel transcendentals

`<P>_HK_SU(3)(s_t) = 1 - exp(-(4/3)s_t)` is transcendental in `e`, not `π`. By
**Nesterenko's theorem on `(e^π, π)`**, `e` and `π` are algebraically
independent for the relevant cases. Therefore:

```
Q-algebraic combinations of (rationals + e-transcendentals)
  cannot produce a non-trivial Q-multiple of π.
```

The heat-kernel route cannot supply `2/9 rad` (which is, in the framework's
target interpretation, a non-Q-multiple of `π`). **Heat-kernel route is closed
by Nesterenko's algebraic-independence theorem.**

### Lattice MC `⟨P⟩` and tadpole `u_0`

`⟨P⟩ ≈ 0.5934 ± 0.0001` is a lattice MC value. Its transcendence class is
**not known** in closed form — it's a numerical observation of an action's
path integral at a specific coupling.

The 2026-05-10 note tested whether `⟨P⟩`, `u_0`, or their powers/products
with retained rationals produce `2π` or its rational multiples within 50-dps
precision. Exact-tier matches were all via `α_bare` (convention re-entry);
non-`α_bare` near-matches bottomed out at `~10⁻⁴` relative error, consistent
with statistical near-coincidence density rather than derivation.

`u_0 = ⟨P⟩^{1/4}` doesn't have a known closed-form transcendence class either.
But the numerical search at 50-dps precision found NO non-trivial exact match
involving only `⟨P⟩`/`u_0` and rationals.

**Lattice MC values do not supply `2/9 rad` natively** (numerical search at
50 dps; no exact match within precision).

### Wilson-series partial sums at retained `s_t`

The Wilson series `<P>_W_SU(3)(s_t) = 1 + sum_n c_n β_W^n` has retained
coefficients `c_n` that are all Q-rational (per the 2026-05-10 inventory).
Partial sums at retained `s_t` are linear combinations of rationals with
rational coefficients — themselves Q-rational. **Wilson partial sums are
Q-algebraic** and do not escape L-W.

## Combined Position 1 result

The retained inventory's non-Q-algebraic ingredients fall into three classes:

1. **`π`-containing convention imports** (`α_bare` and derivatives) — circular
   for the π-bridge.
2. **e-transcendentals** (heat-kernel) — algebraically independent of `π` per
   Nesterenko; cannot produce `Q · 2π`.
3. **Lattice MC numerical values** (`⟨P⟩`, `u_0`) — transcendence class
   unknown; high-precision search found no exact match to `π`-targets.

**No native combination of retained content produces `2/9 rad` as a
non-Q-algebraic radian magnitude.**

This sharpens Position 1: the closing input must be **structurally new** —
not a clever combination of existing retained items, but a genuinely new
retained source-class. The retained inventory at the level of 2026-05-10 is
**exhausted** by Position 1's native search.

## Convergence with Direction γ

Position 1 was the "most tractable" closing route per Direction γ's
synthesis. This cycle has shown it is **also a structural gap** at the
retained level — not just "we haven't tried hard enough", but "the retained
non-Q-algebraic inventory's transcendence classes do not include the
required `Q · 2π` ingredient by Nesterenko + the lattice MC numerical
exhaustion".

The three Position closures of Direction γ:

| Position | Status (post-cycle-7) |
|---|---|
| 1 (new irrational-radian source) | **structural gap on retained inventory** (this cycle) |
| 2 (native re-expression) | **structural gap on K1-K4 substrates** (cycle 6) |
| 3 (new sector-coupling) | structural gap on verified retained dynamics (Direction α) |

**All three positions are now structural gaps.** The π-bridge primitive `P`
cannot be closed by the retained inventory at any of the three identified
positions. **Closing `P` requires structurally new content beyond the
current retained surface.**

This does **NOT** mean `P` is permanently unclosable — only that the
**existing retained inventory plus the K1-K4 substrate family** is
exhausted. New retained sources, new substrate classes (not in K1-K4), or
new mathematical structures could in principle still close `P`.

## What this cycle does NOT claim

- Does **NOT** assert `P` is undecidable or unclosable in principle.
- Does **NOT** claim a formal no-go (no N1-N8 invoked).
- Does **NOT** propose new content. Position 1's closing input remains an
  open structural question for the user's authority.

## Cited retained sources (load-bearing)

- `RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md`
  (inventory enumeration, 50-dps numerical search results)
- Lindemann-Weierstrass theorem (standard math)
- Nesterenko's theorem on `(e^π, π)` (standard math; algebraic independence
  of `e` and `π`)
- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`
  (`retained_no_go`) (Type-A vs Type-B framing)
