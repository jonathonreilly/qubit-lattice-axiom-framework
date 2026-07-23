# Held second-A2-line verification — Cycle 664

Classification: **positive held finite-volume spectral confirmation; continuum,
preparation, and clock-law questions open**

Authority: **none**

Audit: **unset**

Breakthrough: **false**

## Question and evidence status

Cycle 629 found a second positive-phase zero of the Cycle-610 A2
Birman–Schwinger equation and identified the historical `+0.3136` dust-lock
feature with a contact-generated positive A2 line.  It left held size
(`L=13`), held coupling (`beta=-0.35`), isolation, and cavity corroboration
open.

Cycle 664 is a post-discovery confirmation, not a preregistered discovery.
The exact confirmation target was fixed before this runner loaded evidence,
with digest
`0a642665e049e23ae481db3fba95330a03aa2a724fd0494246ce3249c8d515ac`.
The Cycle-610, 611, 622, and 629 runners are byte-pinned.

## Strongest constructive result

The positive A2 Birman–Schwinger zero survives the full crossing of the
pre-existing train and held fixtures:

| fixture | L | beta | theta_2 | abs(b_A2) | eigen-update residual |
|---|---:|---:|---:|---:|---:|
| train | 9 | -0.30 | +0.299980793 | 1.49e-10 | 8.04e-12 |
| held size | 13 | -0.30 | +0.291998548 | 6.48e-10 | 1.21e-11 |
| held beta | 9 | -0.35 | +0.359010403 | 2.46e-11 | 2.70e-12 |
| held both | 13 | -0.35 | +0.278007146 | 1.10e-10 | 3.95e-12 |

Every null vector has A2 overlap above `0.9999999999999998`, reconstructs a
normalized eigenstate of the unchanged periodic contact update, and is
locally isolated: at both `theta_2 +/- 1e-4`, `abs(b_A2)` is at least
`3.025e-3`, compared with at most `6.48e-10` at the root.

This is stronger than merely seeing a DFT peak.  It is an exact finite-volume
eigenline of the declared periodic contact update on all four fixtures.  It
is not an infinite-volume particle pole or a linewidth theorem.

## Independent masked-cavity corroboration and deletion

The unchanged radius-2 absorber has a dominant positive interior A2 line on
all four fixtures:

| beta | contact-on phase | modulus | Ritz residual | contact-off dominant phase |
|---:|---:|---:|---:|---:|
| -0.30 | +0.306547533 | 0.999109374 | 2.36e-13 | -3.066253762 |
| -0.35 | +0.344657213 | 0.998473406 | 3.69e-14 | -3.052519907 |

Contact deletion separates the dominant interior line by at least `2.8860`
radians on every fixture.  The contact-off top-four spectrum still contains
other positive cavity modes, so the exact result is replacement of the
specific dominant contact-dressed line—not the absence of every positive
free-cavity eigenmode.

The L9 and L13 cavity values agree to `7.72e-15`.  That is a locality sanity
check, not held outer-boundary evidence: the radius-2 mask never reaches
either outer boundary.  Genuine held-size evidence comes from the periodic
Birman–Schwinger root and reconstructed L13 eigenstate above.

## What changed in the causal-time bridge

Closed from Cycle 629's immediate checklist:

- finite `L13` existence of the second A2 root;
- held `beta=-0.35` existence;
- the crossed held fixture;
- two-sided local root isolation at phase displacement `1e-4`;
- contact-on/contact-off masked-cavity corroboration.

Still open:

- an infinite-volume pole/resonance-width theorem;
- autonomous preparation or population transfer between the two A2 lines;
- a derived unequal response coefficient, winding channel, or count-edit
  mechanism; and
- a two-line clock certificate and any bridge from that clock to proper time.

The periodic phase spans `0.0810033` radians across the four fixtures.  It is
therefore not a universal calibration constant.  This is useful internal
spectroscopy and a stronger preparation target, but it does not repair the
Cycle-610 alias ceiling: two equally shifted wrapped phases remain redundant.

## Supplied / derived / open

Supplied:

- the Cycle-610 six-mode/contact update and A2 Birman–Schwinger branch;
- the Cycle-611 position-space engine and beta fixtures;
- the Cycle-622 radius-2 absorbing mask;
- the Cycle-629 positive-phase window and interior-line algorithm; and
- the post-discovery thresholds in this runner.

Derived:

- four finite-volume positive A2 roots;
- four reconstructed contact-update eigenstates and residuals;
- two-sided local isolation;
- contact-on/contact-off dominant cavity-line separation; and
- explicit finite-size and coupling sensitivity.

Open: continuum persistence/width, autonomous preparation, independent alias
information, the two-line lawful domain, and all proper-time/gravity claims.

## N1-N8 and claim firewall

- **N1:** periodic BS/eigenstate, masked-cavity contact deletion, and the
  train/held crossing are distinct attempted routes.  This is a positive
  confirmation campaign, not an impossibility claim.
- **N2:** finite-volume/continuum, preparation, and clock-law questions remain
  separate.
- **N3:** the radius-2 cavity's failure to touch the outer boundary, fixture
  phase dependence, and missing drive law are explicit hidden-wall controls.
- **N4:** the receipt carries root, eigen-update, local-isolation, Ritz,
  antisymmetry, and deletion residuals.
- **N5:** a wrapped phase is not energy; a spectral line is not a clock; a
  finite-volume eigenline is not an infinite-volume particle pole.
- **N6:** held existence and local isolation close while continuum,
  preparation, and clock law remain open.
- **N7:** the strongest alternative reading is a pole-dressed box state.  The
  exact update residual proves the box eigenline but does not defeat that
  continuum objection.
- **N8:** the result extends Cycle 629 while retaining Cycle 583's
  full-spectrum-touch/infinite-volume caveat.

All negative, minimum-content, shared-obstruction, and axiom-pressure gates
remain shut.  This cycle creates no axiom pressure.

## Cold verification

```text
9 PASS / 0 FAIL
external wall 178.34 s
maximum root residual:          6.48e-10
maximum eigen-update residual:  1.21e-11
minimum +/-1e-4 side value:     3.025e-3
minimum contact deletion shift: 2.8860 rad
```

Artifacts:

- `scripts/physical_held_a2_second_line_verification_cycle664_2026_07_23.py`
- `outputs/physical_held_a2_second_line_verification_cycle664_receipt_2026_07_23.json`
- `outputs/physical_held_a2_second_line_verification_cycle664_cold_2026_07_23.txt`

## Optimal next experiment

Use the exact primary/secondary periodic eigenvectors to freeze a two-level
population-transfer tournament.  The decisive positive target is an
autonomous local drive that prepares the previously missing bound branch and
has either unequal derived line sensitivities or an explicit count-edit
channel.  Without one of those independent-information mechanisms, more
two-line spectroscopy cannot lift the alias ceiling.
