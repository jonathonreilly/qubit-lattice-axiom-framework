# Complex Action: Kernel-Generic vs Gravity-Specific

**Date:** 2026-04-06
**Status:** RETRACTED 2026-04-30 — audit failed; this note is archived under `archive_unlanded/kernel-gravity-conflation-2026-04-30/`. Claims below are NOT supported by current runners or current audit lane. See `## Retraction` section.

## Current-surface certificate (2026-06-12 source firewall)

**Actual current-surface status:** archived `audited_failed` / retracted
historical artifact. This file is kept only as audit history for a failed
or inconsistent route. It may not be cited as retained, bounded, conditional,
supporting, or methodological authority for any live framework chain.

## Retraction

- **Date archived:** 2026-04-30
- **Archive directory:** `archive_unlanded/kernel-gravity-conflation-2026-04-30/` (the directory name encodes the failure reason: kernel/gravity conflation in the separation observable).
- **Audit verdict_rationale (quoted verbatim from `docs/audit/data/audit_ledger.json`):**

  > Issue: the source conflates link-level imaginary-action damping with the detector escape observable. The factor exp(-k gamma L f) is below 1 for f > 0 and gamma > 0, but the runner's detector escape ratios are still above 1 for UNIFORM f=0.005 at gamma=0.1 and 0.2, UNIFORM f=0.01 at gamma=0.1 and 0.2, and GRAVITY at gamma=0.1 and 0.2. Why this blocks: the retained separation claim says kernel-generic absorption occurs under any nonzero field at gamma > 0, but the measured observable used by the note only shows suppression at sufficiently large gamma in this setup. Repair target: distinguish local per-link attenuation from total detector escape, or add a theorem/runner proving a thresholded escape-suppression criterion across gamma and field families. Claim boundary until fixed: safely claim only that gamma=0.5 suppresses detector escape for the tested nonzero fields, and that the 1/r gravity field uniquely shows the tested TOWARD -> AWAY centroid crossover by gamma=0.2.

- **Do not cite warning:** Do NOT cite the numerical results, tables, or threshold values in the original content below as live framework claims. The runners referenced in this note have been superseded or are no longer reproducible at the time of audit. If a future investigation revisits this physics, treat it as starting from scratch rather than as continuation of a "closed no-go".

## Boundary clarification (2026-06-16)

This archived packet is historical / diagnostic and retired as evidence. It is
not a live authority for kernel-generic detector-escape suppression, complex
action selectivity, gravity-specific crossover, or any retained separation
claim.

The safe surviving statement is narrower than the original text below:

- local per-link attenuation `exp(-k gamma L f) < 1` for `f > 0` and
  `gamma > 0` is only a local factor statement;
- it does not imply total detector-escape suppression for every positive
  `gamma`;
- the archived runner data safely support only that `gamma = 0.5` suppresses
  detector escape for the tested nonzero fields, and that the tested `1/r`
  gravity field uniquely shows the TOWARD -> AWAY centroid crossover by
  `gamma = 0.2`;
- any future live claim needs a fresh source note and runner that either
  proves a thresholded detector-escape suppression criterion across field
  families or explicitly separates link-level damping from detector escape.

## Executable boundary repair (2026-06-17)

The current primary runner is now a boundary verifier rather than a retained
separation proof. It checks the finite archived setup under three separate
claims:

1. **Local link statement:** for a traversed link with averaged field
   `f_ij > 0` and `gamma > 0`, the local imaginary-action multiplier
   `exp(-k gamma L f_ij)` has modulus below one. This is only a link-factor
   theorem.
2. **Detector-escape statement:** on the archived two-seed finite setup,
   `gamma = 0.5` suppresses total detector escape for the tested nonzero
   fields. The same runner explicitly checks that the historical stronger
   statement is false at the detector level: the uniform fields and the tested
   gravity field still have escape ratios above one at the small-gamma rows
   listed in the retraction boundary above.
3. **Centroid-crossover statement:** on the same finite setup, the tested
   `1/r` gravity field is TOWARD at `gamma = 0` and AWAY by `gamma = 0.2`;
   the uniform controls do not carry that TOWARD-to-AWAY crossover.

Expected runner verdict:

```text
VERDICT: THRESHOLDED DETECTOR-ESCAPE BOUNDARY VERIFIED
```

This repair does not revive the archived row as retained, does not assert
geometry independence, and does not prove a general threshold theorem. It makes
the old failed distinction auditable as a finite, thresholded diagnostic only.

## Artifact chain

- [`scripts/complex_action_kernel_vs_gravity.py`](../../scripts/complex_action_kernel_vs_gravity.py)
- [`logs/runner-cache/complex_action_kernel_vs_gravity.txt`](../../logs/runner-cache/complex_action_kernel_vs_gravity.txt)
- [`logs/2026-04-06-kernel-vs-gravity.txt`](../logs/2026-04-06-kernel-vs-gravity.txt)

## Question

The complex action S = L(1-f) + i*gamma*L*f produces both absorption
(escape < 1) and deflection direction change (TOWARD → AWAY). Are these
the same phenomenon, or two distinct effects?

## Historical result section (retracted)

The original text claimed the effects are distinct. This section is retained
only as historical context; the old detector-escape interpretation is
retracted by the audit boundary above.

### Historical kernel-generic absorption section (retracted)

| Field | gamma=0 escape | gamma=0.5 escape |
| --- | ---: | ---: |
| ZERO | 1.000 | 1.000 |
| UNIFORM (f=0.005) | 1.204 | 0.789 |
| UNIFORM (f=0.01) | 1.450 | 0.623 |
| GRAVITY (s=0.004) | 1.030 | 0.961 |

Historical local-factor mechanism: `exp(-k*gamma*L*f) < 1` whenever
`f > 0` and `gamma > 0`. This does not establish total detector-escape
suppression for every positive `gamma`.

### Historical gravity-specific crossover section (safe only at tested boundary)

| Field | gamma=0 direction | gamma=0.2 direction |
| --- | --- | --- |
| ZERO | — | — |
| UNIFORM | random (1/2) | random (1/2) |
| GRAVITY | **TOWARD (2/2)** | **AWAY (0/2)** |

Mechanism: the 1/r field gradient couples to the beam centroid.
Only the spatially structured (localized) field produces directional bias.

## Historical claim boundary (retracted and narrowed)

The archived packet may be used only as triage memory for two narrowed tested
facts:

1. `gamma = 0.5` suppresses detector escape for the tested nonzero fields.
2. The tested `1/r` gravity field uniquely shows the TOWARD -> AWAY centroid
   crossover by `gamma = 0.2`.

The stronger historical statement that any `f > 0` with any `gamma > 0`
suppresses the detector-escape observable is not supported here.
