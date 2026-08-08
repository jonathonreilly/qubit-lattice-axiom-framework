# Antimatter Falls Down: g_anti = g From the CPT-Even Recorded Energy — Falsifiable Prediction

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — a **falsifiable prediction** (conditional), not a closure. Combines two existing
results: (a) the EP bounded support
[`EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS_GENERATOR_INVARIANT_BOUNDED_SUPPORT_NOTE_2026-06-06.md`](./EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS_GENERATOR_INVARIANT_BOUNDED_SUPPORT_NOTE_2026-06-06.md)
(the gravitational mass = the **recorded energy**), and (b) the CPT mass-equality
[`CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md`](./CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md)
(the recorded energy is **CPT-even**). Together: **antimatter has the same gravitational mass as matter, so it
falls *down* with `g_anti = g`** (no antigravity).
**Claim scope:** **conditional / falsifiable prediction.** Conditional on the EP bounded support (itself
conditional on #2988 + `BROAD_GRAVITY`) and the CPT mass-equality. **ALPHA-g 2023** is a **comparator** only, never
a derivation input. Not a closure.
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_antimatter_grav_mass_cpt_even_recorded_energy_exact.py`](./../scripts/audit_companion_antimatter_grav_mass_cpt_even_recorded_energy_exact.py)

## The prediction

`g_anti / g = +1` exactly — **antihydrogen falls down**, with no antigravity and no anomalous antimatter free-fall.

## Derivation (runner 5/5)

1. **The gravitational mass is the recorded energy** (EP bounded support).
2. **The recorded energy is CPT-even.** Under CPT the charge flips (`q → −q`, particle → antiparticle) but the
   mass/energy is invariant (`m → m`) — the CPT mass-equality. So `m_gravitational` (= the recorded energy) is
   **CPT-even**. (Runner (1).)
3. **Hence antimatter's gravitational mass equals matter's:** `m_grav(antimatter) = m = m_grav(matter)`.
   (Runner (2).)
4. **And the free-fall acceleration is the same.** With the WEP bounded support (`m_grav = m_inert =` the recorded
   energy for each species), `g = (m_grav/m_inert)·g₀ = g₀` for **both** matter and antimatter, so
   `g_anti / g = 1` exactly — antimatter falls down. (Runner (3).)
5. **Falsifiable, and consistent with experiment.** A measured antigravity (`g_anti < 0`) would have falsified
   this. **ALPHA-g (CERN, 2023)** measured antihydrogen free-fall with `g_anti/g` consistent with `+1`
   (antihydrogen falls down) — consistent. (Runner (4), comparator only.)

## What this is, and what it is not

| | statement | status |
|---|---|---|
| `m_grav` is CPT-even (= the recorded energy) | from the EP support + CPT mass-equality | **bounded** (combines two existing results) |
| `m_grav(antimatter) = m_grav(matter)` | CPT-even ⟹ same recorded energy | **derived** (runner) |
| `g_anti = g` (antimatter falls down) | WEP support ⟹ universal `g₀` for both species | **falsifiable prediction** |
| ALPHA-g 2023 consistency | `g_anti/g ≈ +1` | **comparator** (not a derivation input) |
| a WEP/antimatter-gravity closure | rides the EP support's conditionalities (#2988, `BROAD_GRAVITY`) | **open** |

**Net.** Combining the EP bounded support (`m_grav =` the recorded energy) with the existing CPT mass-equality (the
recorded energy is CPT-even) yields a sharp, falsifiable prediction: **antimatter falls down with `g_anti = g`** —
no antigravity. It matches the 2023 ALPHA-g result. This is a *consequence* of two existing results, conditional on
their scope; it is **not** an unconditional closure.

## No-go discipline / steelman

**Strongest objection (this is just `m_g=E` + CPT, both standard).** Granted that the ingredients are existing
results; the **new** content is their *combination into a falsifiable antimatter-gravity prediction*, which neither
parent states. **Second objection (conditional).** Granted — it inherits the EP support's conditionalities (#2988,
`BROAD_GRAVITY`) and the CPT mass-equality; it is a conditional prediction, not a closure. **Third objection (the
comparator does the work).** No — ALPHA-g is cited only to place the prediction on the falsification surface; the
prediction `g_anti=g` is derived from the CPT-even recorded energy, independent of the measurement.

## Forbidden-import / reprove-and-cite

The structural facts (CPT-even recorded energy; `m_grav(antimatter)=m_grav(matter)`; `g_anti/g=1`) are reproven
from primitives in the runner (sympy, 5/5). **ALPHA-g 2023** and the relativistic `m_grav=E` are **comparators**
only. No PDG values feed the derivation.

## Dependencies (citation-graph visible)

- [`EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS_GENERATOR_INVARIANT_BOUNDED_SUPPORT_NOTE_2026-06-06.md`](./EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS_GENERATOR_INVARIANT_BOUNDED_SUPPORT_NOTE_2026-06-06.md)
- [`CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md`](./CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md)
- [`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
