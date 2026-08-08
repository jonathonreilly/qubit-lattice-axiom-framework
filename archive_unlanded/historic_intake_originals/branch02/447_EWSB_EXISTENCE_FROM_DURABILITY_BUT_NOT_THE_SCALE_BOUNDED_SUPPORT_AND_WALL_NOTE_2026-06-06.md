# EWSB Existence From Durability, But Not the Scale — Bounded Support + a Named Wall

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — a **two-sided** result on whether mass=recordedness
([`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md),
#2988) helps the electroweak scale `v`. **(Support):** it re-grounds the **existence** of electroweak symmetry
breaking — the symmetric phase is not a durable record. **(Wall):** it does **not** fix the **scale** — the
hierarchy stays the separate obstructed lane.
**Claim scope:** the **existence** support is **conditional** on the Mexican-hat potential shape (the `μ²<0` input
is **not** supplied by mass=recordedness). The **scale** is an explicit **named wall**, narrow and exact: durability
fixes "a minimum," not which scale.
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_ewsb_existence_from_durability_not_scale_exact.py`](./../scripts/audit_companion_ewsb_existence_from_durability_not_scale_exact.py)

## The question

mass=recordedness leaves "why is `v ≠ 0`, and why at the electroweak scale" as its deepest residual. Does it crack
it? Tested honestly on both sides (runner 6/6).

## Support — EWSB existence from durability (conditional)

The realized vacuum is a **durable record**, hence a **positive-curvature minimum** (#2988). For a Mexican-hat
Higgs potential `V = λ(φ²−v²)²`:

1. The **symmetric point** `φ=0` has `V''(0) = −4λv² < 0` — a **maximum** (unstable, tachyonic), so it is **not a
   durable record**. (Runner (A1).)
2. The **broken minimum** `φ=v` has `V''(v) = 8λv² > 0` — a **minimum**, a durable record. (Runner (A2).)
3. So the realized vacuum (a durable record) is the **broken minimum `v ≠ 0`**, not the unrecordable symmetric
   phase: **EWSB existence is forced by durability.** (Runner (A3).) The Higgs mass² is the record-stiffness at the
   recorded vacuum, `m_H² = V''(v) = 8λv²` — mass=recordedness applied to the Higgs. (Runner (A4).)

This is **conditional on the Mexican-hat shape**: the `μ²<0` (wrong-sign mass at the origin) that makes the
symmetric point a maximum is the framework's separate EWSB-pattern input, **not** supplied by mass=recordedness.
What mass=recordedness adds is the *selection*: given an unstable symmetric point, durability forbids it as the
realized record, so `v ≠ 0` is forced.

## Wall — the scale is not fixed (narrow, exact)

Durability fixes that the vacuum is **a** minimum (positive curvature), but **not which scale**:

- `m_H² = 8λv² > 0` holds for **any** `λ > 0`, `v > 0`. Solving for `v` gives `v = √(m_H²/(8λ))` — `v` depends on
  the **free** `λ`, so `v` is **not** fixed by durability. (Runner (B1).)
- Therefore mass=recordedness gives EWSB **existence** but not the **scale**. The `v`-scale / hierarchy — the
  separate, obstructed lane (`GAUGE_VACUUM_PLAQUETTE_HIERARCHY`, the imported `M_Pl` + un-derived exponent-16) —
  remains **open and untouched**. (Runner (B2).)

This wall is narrow and specific: it is **not** "mass=recordedness fails," it is "durability is scale-free, so it
cannot fix `v`." The scale must come from the hierarchy lane, not from the record-stiffness.

## What this is, and what it is not

| | statement | status |
|---|---|---|
| EWSB existence `v ≠ 0` | the symmetric phase is not a durable record (unstable) ⟹ the realized vacuum is broken | **bounded support** (conditional on Mexican-hat) |
| `m_H² = 8λv²` = the record-stiffness | mass=recordedness applied to the Higgs vacuum | **bounded** |
| the `μ²<0` (Mexican-hat) input | the wrong-sign origin mass | **not supplied** (separate EWSB-pattern input) |
| the **scale `v`** | undetermined — durability is scale-free (`λ,v` free) | **named wall** (open hierarchy lane) |

**Net.** mass=recordedness **re-grounds the existence** of electroweak symmetry breaking — the symmetric phase
cannot be the realized vacuum because it is not a durable record — but it is **scale-free** and therefore does
**not** crack the `v`-scale. The honest answer to "does mass=recordedness help `v`?" is: **yes for existence
(conditional), no for the scale.**

## No-go discipline (the scale wall)

The wall is the narrowest correct statement: durability ⟹ positive curvature ⟹ a minimum; the minimum's curvature
`8λv²` scales with `v` but `λ` is free, so no scale is selected. Alternative routes to fix `v` (RG running /
exponent-16, the `M_Pl` import, a dynamical relaxation) are the **separate** hierarchy lane and its standing
obstructions — they are not reachable from the record-stiffness. The wall is therefore *route-specific* (it prunes
the "fix `v` from durability" route), not a claim about the hierarchy lane as a whole.

## Forbidden-import / reprove-and-cite

All facts (`V''(0)<0`, `V''(v)=8λv²>0`, the scale-indeterminacy `v=√(m_H²/(8λ))`) are reproven from the Mexican-hat
primitive in the runner (sympy, 6/6). No PDG values; the numerical `v=246` GeV and the hierarchy formula are
**not** used or reproduced here.

## Dependencies (citation-graph visible)

- [`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md)
- [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](./HIGGS_MASS_FROM_AXIOM_NOTE.md)
- [`EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md`](./EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
