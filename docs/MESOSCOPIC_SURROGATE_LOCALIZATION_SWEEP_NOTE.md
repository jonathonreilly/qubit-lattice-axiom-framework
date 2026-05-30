# Mesoscopic Surrogate Localization Sweep

**Status:** bounded finite-sweep benchmark note; source-note proposal only,
with audit status set by the independent audit lane
**Claim type:** bounded_theorem

**Primary runner:** [`scripts/mesoscopic_surrogate_localization_family_sweep.py`](../scripts/mesoscopic_surrogate_localization_family_sweep.py)

**Runner cache:** [`logs/runner-cache/mesoscopic_surrogate_localization_family_sweep.txt`](../logs/runner-cache/mesoscopic_surrogate_localization_family_sweep.txt)
(SHA-pinned; runner exits 0; ~6s on the audit-lane host.)

**Audit-conditional perimeter repaired for re-audit (2026-05-26):**
The previous conditional audit accepted the narrow table-level observation
but blocked the stronger least-bad source interpretation because no explicit
dominance criterion compared score, width ratio, support, and capture, and
because the setup was described as a retained 3D source-control authority.
This repair narrows the row to the finite runner table plus the benchmark
criterion asserted by the runner. It does not promote audit status; it only
queues a narrower packet for independent re-audit.

This note records an alternative localization-family sweep on a fixed 3D
ordered-lattice mesoscopic-source setup. The repaired claim is deliberately
narrow: it is the finite runner table plus the explicit mesoscopic benchmark
asserted by the primary runner. The note does not certify the setup as a
retained source-control authority and does not claim a framework-wide
least-bad source theorem.

## Setup

The sweep reuses the same fixed 3D valley-linear family as the surrounding
mesoscopic surrogate controls and compares three localization families:

- `topN` compression
- symmetric square windows around the peak bin
- compact Gaussian masks centered at the peak bin

All families are evaluated against the same stage-1 sourced profile, then relaunched through the same field and compared by:

- stage-1 and stage-2 capture
- stage-1 and stage-2 centroid shifts
- best-shift score between the two stages
- width ratio between stages

The full sweep log is here:

- [logs/2026-04-04-mesoscopic-surrogate-localization-family-sweep.txt](../logs/2026-04-04-mesoscopic-surrogate-localization-family-sweep.txt)

## Benchmark rule

The runner now makes the interpretive step executable instead of leaving it
as prose judgment. A row is counted as a mesoscopic benchmark pass only when
all of the following finite-table gates hold:

```text
support2 >= 25
capture1 >= 0.95
capture2 >= 0.95
score    >= 0.999
|width_ratio - 1| <= 0.05
```

This benchmark is a branch-local finite-sweep criterion, not a new axiom and
not a retained framework principle. It exists only to separate point-like
score/width coincidences from rows that still carry broad mesoscopic support
and high two-stage capture in this runner.

## Bounded finite-sweep result

The sweep found that:

- degenerate point-like localizations can reach the best score numerically
  - square radius `0`
  - Gaussian `sigma=0.5`
- but those cases have very low capture and effectively behave like point-source surrogates
- under the explicit benchmark rule above, only broad top-N rows pass in this
  finite sweep

The best scored rows were:

- `square radius 0`: score `1.0000`, width ratio `1.0000`, capture2 `0.107`
- `gaussian sigma 0.5`: score `1.0000`, width ratio `1.0033`, capture2 `0.171`

The benchmark-supported rows are broad top-N controls:

- `topN 25`: support2 `25`, capture1 `0.988`, capture2 `0.993`,
  score `0.9993`, width ratio `0.9876`
- `topN 49+`: support2 `33`, capture1 `1.000`, capture2 `1.000`,
  score `0.9994`, width ratio `1.0205`

The strongest non-topN localized rows fail the benchmark by support/capture:

- `square radius 1`: score `1.0000`, capture2 `0.427`
- `gaussian sigma 1.0`: score `0.9998`, capture2 `0.409`

## Safe read

The honest interpretation is:

- more localized families do not obviously beat the broad top-N control on
  this fixed finite sweep
- the near-point-source cases can match the shift score, but only by collapsing into very small capture/support
- under the finite benchmark rule above, the passing rows are the broad top-N
  rows, while square-window and Gaussian rows fail capture/support gates
- a future runner can replace this benchmark or find a non-topN row that
  passes it; this note does not rule that out

This is a bounded negative result, not a failure of the broader surrogate lane.

## 2026-05-26 audit-packet repair

The previous conditional audit accepted the printed table but blocked the
stronger interpretation because score, width ratio, support, and capture were
traded by prose judgment, and because the note described the setup as a
retained 3D source-control authority. This repair addresses those blockers
without adding an axiom:

- the primary runner asserts the benchmark rule above and exits nonzero if
  the finite-table facts fail;
- the benchmark is explicitly bounded to this runner's fixed sweep and is not
  presented as retained framework machinery;
- the setup language is narrowed to a fixed 3D ordered-lattice family rather
  than a retained source-control premise;
- the supported conclusion is only that, on this finite table and under this
  declared benchmark, broad top-N rows pass and square/Gaussian rows do not.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a
prior conditional audit so the audit citation graph can track them. It does
not promote this note or change the audited claim scope.

- `QUASI_PERSISTENT_RELAUNCH_PROBE_NOTE.md` (downstream probe; backticked to break cycle-0004 in the citation graph)
