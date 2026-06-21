# Causal Field: Canonical Bounded Chain Map

**Date:** 2026-04-06 (updated; source-firewall narrowing 2026-06-17)
**Status:** meta source-firewall chain map. No package-level retained
status is proposed here, and this note does not promote the unaudited Shapiro
phase-lag chain or the archived causal-propagating-field table.
**Type:** meta
**Claim type:** meta
**Source-firewall runner:** [`scripts/causal_field_live_packet_reference_firewall_2026_06_16.py`](../scripts/causal_field_live_packet_reference_firewall_2026_06_16.py)
**Source-firewall cache:** [`logs/runner-cache/causal_field_live_packet_reference_firewall_2026_06_16.txt`](../logs/runner-cache/causal_field_live_packet_reference_firewall_2026_06_16.txt)

## Audit-facing boundary

This note is a map of live causal-field observables and dependencies, not a
new theorem. Its audit-useful claim is only that current causal-field context
points at the live bounded packet
[`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
and no longer treats the archived
2026-04-30 causal-propagating-field note as live evidence.

The downstream lab-facing hierarchy remains dependency-limited:

| Input | Boundary tracked here | Role |
| --- | --- | --- |
| `CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md` | live bounded causal-cone replay | explicitly rejects the stale `0.45` table |
| `CAUSAL_FIELD_PORTABILITY_NOTE.md` | fixed-anchor cross-family boundary diagnostic | not a portability theorem |
| `CAUSAL_ESCAPE_WINDOW_NOTE.md` | bounded escape-window diagnostic | exposure-reduction mechanism, not an irreducible causal discriminator |
| `GRAVITOMAGNETIC_NOTE.md` | bounded antisymmetric moving-source diagnostic | portable correction packet |
| `SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md` | no-go boundary | static cone shape can reproduce the same phase curve |
| `SHAPIRO_DELAY_NOTE.md` | phase-lag candidate | not promoted by this map |

Therefore this note may be used to route re-audit and downstream review, but
it may not be cited as retained evidence for a physical field speed, a unique
causal discriminator, a cross-family portability law, or a lab-calibrated
diamond/NV prediction.

## Observable hierarchy

### Tier 1: Shapiro phase lag (strongest phase-sensitive dynamic observable)

The c-dependent phase lag is the **primary lab-facing observable**.

**Important boundary** (from `SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`):
a static field shaped like a cone (same spatial envelope as the dynamic cone)
reproduces the same phase curve exactly. A static field with uniform
scheduling does NOT. The discriminator is the spatial shape of the field,
not causality per se. The Shapiro phase is NOT a unique causal discriminator
in the strongest sense — it is a shape-sensitive phase observable that the
causal cone happens to produce naturally.

| c | Phase lag (rad) | 3-family agreement |
| ---: | ---: | ---: |
| inst | 0.000 | exact |
| 2.0 | +0.040 | 0.2% |
| 1.0 | +0.050 | 0.4% |
| 0.5 | +0.062 | 0.3% |
| 0.25 | +0.068 | 0.1% |

Scaling laws:
- **phase ~ s^1.000** (exactly linear in mass)
- **phase ~ k** (chromatic: proportional to wavenumber)
- **phase decreases with b** (weaker at larger impact parameter)

Null: c = inst → phase = 0.000 by construction.

### Tier 2: Gravitomagnetic correction (real, portable, antisymmetric)

Moving source produces antisymmetric phase shift: delta(+v) ≈ -delta(-v).

| v | Phase correction | 3-family agreement |
| ---: | ---: | ---: |
| +0.2 | +0.003 | 12% |
| -0.2 | -0.003 | 12% |

Antisymmetry residual < 10% of signal.

### Tier 3: Trapping escape (real regime, exposure-reduction mechanism)

At eta=20, s=0.004: inst trapped (0.39), dyn escapes (0.97).
Portable across 3 families to 0.2%.

**However**: exposure-matched static proxy ALSO escapes (0.987).
The mechanism is average-exposure reduction, not irreducible cone geometry.
The boundary law (eta_max ~ 1/c²) is real but not uniquely causal.

This is a useful bounded escape-window result. It is NOT the primary
discriminator.

## Lab bridge

The Shapiro phase lag is the canonical lab-facing prediction because:

1. **Observable**: phase shift in a matter-wave interferometer
2. **Null**: drive off, source removed, or source at large distance
3. **Scaling with s (mass)**: phase ∝ s^1.000 — testable by varying source mass
4. **Dependence on separation**: phase decreases with b — testable by varying
   source-detector distance
5. **Chromatic**: phase ∝ k — testable by varying beam energy
6. **c-dependence**: if the field propagates at finite c, the phase depends on c

### What is still missing for real lab numbers

- Transfer coefficient: proxy phase → NV readout units
- Lab noise floor in those units
- Geometry-specific coupling factor for a particular setup
- Signal budget: whether the predicted phase exceeds detector sensitivity
- Systematic budget: heating, strain, instrument lag controls

### Existing diamond/NV bridge notes on main

- `SHAPIRO_DIAMOND_BRIDGE_NOTE.md` — proxy bridge language
- `SHAPIRO_DIAMOND_FREQUENCY_BRIDGE_NOTE.md` — chromatic bridge
- `DIAMOND_ABSOLUTE_UNIT_BRIDGE_NOTE.md` — absolute vs relative calibration
- `DIAMOND_NV_PHASE_RAMP_SIGNAL_BUDGET_NOTE.md` — signal budget
- `DIAMOND_SENSOR_PROTOCOL_NOTE.md` — measurement protocol
- `MOONSHOT_DIAMOND_SENSOR_BRAINSTORM_NOTE.md` — experimental design

## Full artifact inventory

| Observable | Script | Log | Note |
| --- | --- | --- | --- |
| Shapiro delay | shapiro_delay_portable.py | 2026-04-06-shapiro-delay-portable.txt | SHAPIRO_DELAY_NOTE.md |
| Shapiro scaling | (inline, commit 1730b52) | — | SHAPIRO_SCALING_NOTE.md |
| Gravitomagnetic | gravitomagnetic_portable.py | 2026-04-06-gravitomagnetic-portable.txt | GRAVITOMAGNETIC_NOTE.md |
| Causal escape | causal_escape_window.py | — | CAUSAL_ESCAPE_WINDOW_NOTE.md |
| Boundary law | causal_escape_boundary_law.py | — | (in escape note) |
| Causal cone | causal_propagating_field.py | logs/runner-cache/causal_propagating_field.txt | CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md |
| Causal live-packet firewall | causal_field_live_packet_reference_firewall_2026_06_16.py | logs/runner-cache/causal_field_live_packet_reference_firewall_2026_06_16.txt | this note |
| Kernel vs gravity | complex_action_kernel_vs_gravity.py | 2026-04-06-kernel-vs-gravity.txt | KERNEL_VS_GRAVITY_NOTE.md |

## What should NOT be overclaimed

- The trapping escape is NOT uniquely causal (exposure-matched static mimic works)
- The Shapiro delay is NOT uniquely causal either: a static cone-shaped field
  reproduces the same phase curve (see SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md).
  Static SCHEDULING does not reproduce it. The discriminator is spatial shape,
  not causality per se.
- The gravitomagnetic correction needs more seeds for the 12% spread
- The lab bridge is relative, not absolute (no transfer coefficient)
- The cone speed c is a free parameter (not derived from the model)
- No observable in this chain has been shown to be irreducible to a matched
  static proxy.
- The strongest live causal-field claim used here is bounded: the live finite
  causal-cone runner produces stable configured proxy ratios, while the
  archived `0.45` positive table is stale and retired.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [causal_propagating_field_live_packet_note_2026-06-05](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
- [causal_field_portability_note](CAUSAL_FIELD_PORTABILITY_NOTE.md)
- [shapiro_delay_note](SHAPIRO_DELAY_NOTE.md)
- [shapiro_static_discriminator_note](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)
- [gravitomagnetic_note](GRAVITOMAGNETIC_NOTE.md)
- [causal_escape_window_note](CAUSAL_ESCAPE_WINDOW_NOTE.md)
