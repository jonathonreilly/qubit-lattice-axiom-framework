# Central-Band Dense Joint Card Note

**Date:** 2026-04-02  
**Status:** complete, bounded same-graph joint card

This note records the same-graph joint card for the dense central-band pocket
that is already Born-clean on the corrected three-slit harness.

Script:
[`scripts/central_band_dense_joint_card.py`](/Users/jonreilly/Projects/Physics/scripts/central_band_dense_joint_card.py)

## Setup

- corrected dense central-band graph family
- `N = 40, 60`
- `npl = 60`
- `y_cut = 2.0`
- `yz_range = 12.0`
- `connect_radius = 3.0`
- `4` matched seeds
- `8` Monte Carlo realizations for the collapse rows

## Strongest Retained Rows

The dense pocket is Born-clean as a **bounded mean±SE statement** for both
retained LN rows: the runner prints `Born |I3|/P = 0.000±0.000` rounded to
three decimals. A high-precision per-row `max |I3|/P` threshold check is
not part of this card's output and is left as a follow-up (see the audit
repair section below).

| N | mode | Born `|I3|/P` (mean±SE) | `pur_min` / purity | gravity delta | note |
|---|---|---:|---:|---:|---|
| 40 | `LN + |y|` | `0.000±0.000` | `1.000±0.000` | `-0.529±0.497` | Born-safe (mean±SE), but not yet a positive gravity row |
| 40 | `LN + |y| + collapse` | `0.000±0.000` | `0.568±0.054` | `-0.520±0.521` | collapse helps purity, gravity still negative |
| 60 | `LN + |y|` | `0.000±0.000` | `0.875±0.125` | `+0.455±0.384` | retained joint row |
| 60 | `LN + |y| + collapse` | `0.000±0.000` | `0.552±0.081` | `+0.454±0.385` | best purity on the dense pocket |

## Narrow Read

- The dense central-band pocket is Born-clean on the corrected harness.
- `N=40` is Born-clean but not yet a retained joint gravity row.
- `N=60` is the retained same-graph joint row:
  - `LN + |y|` keeps gravity positive
  - `LN + |y| + collapse` lowers purity further while keeping gravity positive
- The collapse term improves the purity floor inside the dense pocket, but
  it does not change the gravity mean in this sample.

## Interpretation

This is the cleanest same-graph statement so far for the dense central-band
lane:

- corrected Born survives as a bounded mean±SE row (`0.000±0.000` at three
  decimals on every retained LN row); a high-precision per-row threshold
  check is a follow-up rather than a present claim
- the hard-geometry lane keeps a real decoherence improvement
- the collapse term can sit inside the pocket without breaking Born at the
  mean±SE level shown by the runner
- the retained coexistence window is still bounded, with the strongest
  positive gravity row at `N = 60`

## 2026-05-18 audit-conditional repair: claim narrowed + N=40 collapse table synced

Per the 2026-05-17 audit verdict, the note's "machine-precision Born" claim
was narrowed to the bounded mean±SE rows the runner actually prints. The
N=40 collapse table is also synced against the registered cache.

Concretely:

- The "Born-clean at machine precision" wording in **Strongest Retained
  Rows** was narrowed to "Born-clean as a bounded mean±SE statement", and
  the **Interpretation** bullet that read "corrected Born survives at
  machine precision" was narrowed to "corrected Born survives as a bounded
  mean±SE row". The runner's stdout shows
  `Born |I3|/P = 0.000±0.000` rounded to three decimals — it does not
  print a per-row high-precision `max |I3|/P` threshold check, so the
  "machine precision" wording overclaimed what this card actually shows.
- The N=40 `LN + |y| + collapse` row was synced against the cached stdout
  at `logs/runner-cache/central_band_dense_joint_card.txt`:
  - `pur_min`: `0.587±0.065` → `0.568±0.054`
  - `gravity`: `-0.554±0.493` → `-0.520±0.521`
- The N=60 `LN + |y| + collapse` row was also synced for `pur_min`:
  `0.550±0.082` → `0.552±0.081` (gravity row already matched).

A high-precision per-row `max |I3|/P` threshold assertion is left as an
open follow-up for this row rather than being a current claim.

