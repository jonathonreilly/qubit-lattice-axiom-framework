# The Graviton-Mass Scale Is Record-Forced to O(√Λ) — Prediction Note

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — a **conditional / structural prediction**. It does **not** re-derive the
framework's graviton-mass identity `m_g² = 2Λ` (that is the bounded
[`GRAVITON_MASS_DERIVED_NOTE.md`](./GRAVITON_MASS_DERIVED_NOTE.md), taken as input). It establishes the new
content: under
[`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md),
a graviton mass can only arise from a **record** that pins the locally-gauge metric perturbation, and the **only
global record** is the finite universe size `R = √(3/Λ)`. So the graviton-mass **scale** is **record-forced to
O(√Λ)** — cosmological, **not Planck** and **not zero** — and the massless graviton is exactly the
**no-global-record** (`R → ∞`) limit.
**Claim scope:** **conditional.** The coefficient (`2` in `m_g² = 2Λ`) is the geometric Lichnerowicz S³ gap
(inherited, bounded), and the framework's S³ / `R = c/H₀` cosmology is a **premise**. The new content is the
**record-forcing of the scale**, not the number. A near-future detection of an exactly massless graviton below
`~10⁻³³ eV` would pressure the prediction; a graviton mass `~H₀` would confirm it.
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_graviton_mass_scale_record_forced_exact.py`](./../scripts/audit_companion_graviton_mass_scale_record_forced_exact.py)

## The prediction

`m_g ≈ 3.52 × 10⁻³³ eV` (i.e. `m_g² = 2Λ`), a **definite nonzero** graviton mass at the cosmological scale —
where General Relativity assumes exactly zero. The novel, record-native content is **why this scale is forced**.

## Why the scale is record-forced (runner 7/7)

1. **The graviton is locally unrecorded.** The metric perturbation is the diffeomorphism / relative-frame
   freedom — a connection, hence (by the Record-invariance results) gauge-variant and **not a record** locally. By
   record-durability = positive mass-curvature (#2988), a locally-unrecorded continuous degree of freedom is
   massless **unless a record pins it.**
2. **The only available record is global.** A **local** record (the lattice spacing, ~Planck) gaps UV modes
   (~`E_Planck`), but cannot pin the **IR zero mode** of the graviton. The only **global** record is the finite,
   definite universe size `R = √(3/Λ)` (the cosmological record, `Λ = 3/R²`). (Runner (3),(4).)
3. **Hence the scale is forced to O(√Λ), not Planck and not zero.** The graviton mass is the imprint of the global
   record on the otherwise-massless connection: `m_g ~ ħ/R ~ ħ√(Λ/3) ~ ħH₀ ~ 3.5 × 10⁻³³ eV`. A Planck-scale
   graviton mass is excluded (no Planck-scale **global** record), and `m_g = 0` is exactly the **no-global-record**
   limit `R → ∞`. (Runner (1),(2),(3),(4).)

So mass=recordedness does not merely *permit* `m_g² ∝ Λ` — it **forbids any other scale**. The cosmological scale
is structurally selected as the unique global record able to gap the locally-gauge graviton. This resolves the
"why is the graviton-mass scale `~H₀` and not Planck" question that is otherwise a fine-tuning coincidence.

## Placement on the falsification surface

| | value | note |
|---|---|---|
| prediction | `m_g ≈ 3.52 × 10⁻³³ eV`, `m_g² = 2Λ` | definite nonzero; GR assumes `0` |
| record-forced content | the **scale** `O(√Λ)` (the only global record); `m_g → 0` ⟺ `R → ∞` | the new, structural part |
| LIGO/Virgo GW-dispersion bound | `m_g ≲ 1.3 × 10⁻²³ eV` | prediction is `~10¹⁰` below |
| tightest cosmological/solar-system bounds | `m_g ≲ 10⁻³²` eV | prediction is `~3×` below — **on the frontier** |
| coefficient `2` | Lichnerowicz S³ gap (geometry) | inherited, bounded, not record-forced |

This is the framework's cleanest **distinguishing** gravity prediction: GR assumes a massless graviton; the
framework forces a definite nonzero `m_g` at the cosmological scale, near the current testability frontier.

## No-go discipline / steelman

**Strongest objection (the graviton is massless in GR).** GR *assumes* `m_g = 0`; experiment gives only upper
bounds (`≲ 10⁻²³` eV from GW dispersion, `≲ 10⁻³²` eV from cosmology), so the graviton's masslessness is **not
established**. A tiny mass `~H₀` is theoretically well-motivated (the IR/dark-energy scale). The framework making a
definite prediction here is a strength, not a defect. **Second objection (this just renames the existing
`m_g²=2Λ`).** The value is inherited (and bounded); the **new** content is that the *scale* is record-forced —
that a locally-gauge graviton can be pinned **only** by a global record, and the only global record is `Λ`, so the
scale is uniquely cosmological. **Third objection (conditionality).** Granted: the coefficient is geometric and the
S³ / `R = c/H₀` cosmology is a premise; the prediction inherits their bounded status. The record-forcing of the
scale (Parts 1–3) stands within that scope.

## Forbidden-import / reprove-and-cite

The scale/structural facts (`m_g² = 2Λ = 6/R²` as the cited input; the `R → ∞` massless limit; the global-record
scale `ħH₀`; the Planck/local-record exclusion of the IR mode) are reproven in the runner (numpy/sympy, 7/7).
Observational bounds (LIGO/Virgo, cosmological) are **comparators** only — used to place the prediction on the
falsification surface, never as derivation inputs. No PDG values feed the derivation; the coefficient `2` is the
geometric Lichnerowicz gap from the cited bounded note.

## Dependencies (citation-graph visible)

- [`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md)
- [`GRAVITON_MASS_DERIVED_NOTE.md`](./GRAVITON_MASS_DERIVED_NOTE.md)
- [`COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`](./COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md)
- [`COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md`](./COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
