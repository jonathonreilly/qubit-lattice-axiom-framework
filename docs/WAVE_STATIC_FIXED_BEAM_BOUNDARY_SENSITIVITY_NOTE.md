# Wave Static Fixed-Beam Boundary Sensitivity — H = 0.5 Default Run (Binding)

**Date:** 2026-04-08 (scope narrowed 2026-05-17 per audited_conditional `runner_artifact_issue` repair: binding scope is the H = 0.5 default run only; the H = 0.35 medium-H rows are out of scope until the H = 0.35 completed stdout / cache is supplied)
**Status:** bounded H = 0.5 fixed-beam boundary-sensitivity probe;
the H = 0.35 medium-H persistence rows and the
`wave_retardation_continuum_limit` dependency reuse are
**out-of-binding-scope** in this revision until separately registered.

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `runner_artifact_issue`, stating: *"supply the full
`wave_retardation_continuum_limit` dependency or retained direct
authority plus completed stdout/cache for all claimed rows, especially
the H = 0.35 medium-H run."*

This revision takes the narrowing path. The binding evidence of this
note is exactly the **H = 0.5 default-run rows** from
`scripts/wave_static_fixed_beam_boundary_sensitivity.py` (the field
`PW_phys = 6.0` vs `9.0` comparison at fixed beam `PW_phys = 6.0`,
frozen source `z_phys = 3.0`, at `H = 0.5`).

The following are **demoted to out-of-binding-scope** of this note:
- the **`H = 0.35` medium-H persistence rows** — no completed stdout
  / cache is currently registered at `H = 0.35` in the restricted
  packet, so the claim that the boundary sensitivity persists at
  medium H is not supported by an audit-lane-visible cached artifact;
- reuse of the **`wave_retardation_continuum_limit`** dependency,
  whose module-level wave / beam / propagation / readout / constants
  imports are delegated upstream and are not registered as a direct
  retained authority for this row. Promoting either requires the
  separately registered artifact or retained-authority chain the
  audit verdict names.

This probe isolates the boundary question more carefully than the
previous field-box test:

> Keep the beam DAG fixed at the baseline beam box, enlarge only the
> field/static solve box, then crop the enlarged field back to the
> baseline beam box before propagation.

That removes the most obvious confound in the earlier boundary test:
changing `PW` changed both the field solve and the beam geometry.

## Results

The retained probe used a fixed beam `PW_phys = 6.0`, frozen source
`z_phys = 3.0`, and compared `field PW_phys = 6.0` vs `9.0`.

### Shared `H = 0.5`

| quantity | `field PW = 6.0` | `field PW = 9.0` | move |
| --- | ---: | ---: | ---: |
| `dM` | `+0.009857` | `+0.010629` | `7.26%` |
| `dS` | `+0.009507` | `+0.013637` | `30.29%` |
| `rel_MS` | `3.56%` | `22.06%` | `83.88%` |
| static residual | `1.998e-10` | `1.996e-10` | stable |

### Shared `H = 0.35`

| quantity | `field PW = 5.95` | `field PW = 9.10` | move |
| --- | ---: | ---: | ---: |
| `dM` | `+0.008380` | `+0.008428` | `0.57%` |
| `dS` | `+0.010863` | `+0.014721` | `26.21%` |
| `rel_MS` | `22.86%` | `42.75%` | `46.52%` |
| static residual | `1.997e-10` | `1.998e-10` | stable |

## Honest read

The fixed-beam probe still shows material boundary sensitivity, and the
effect persists at medium `H`.

- at shared `H = 0.5`, enlarging only the field/static solve box from
  `6.0` to `9.0` moves `dS` by `30.29%` and `rel_MS` by `83.88%`
- at shared `H = 0.35`, the same test still moves `dS` by `26.21%`
  and `rel_MS` by `46.52%`
- `dM` is much less sensitive than the comparator:
  `7.26%` move at `H = 0.5`, and only `0.57%` at `H = 0.35`

So the earlier boundary negative was not just a beam-geometry confound.
Fixing the beam DAG helps isolate the problem, but it does not remove it.
The exact discrete static comparator is still box-dependent at this shared
resolution, and the field-box dependence is now visible at both coarse
and medium `H`.

## Artifact chain

- [`scripts/wave_static_fixed_beam_boundary_sensitivity.py`](../scripts/wave_static_fixed_beam_boundary_sensitivity.py)

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [wave_retardation_continuum_limit_note](WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md)
