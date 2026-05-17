# Asymmetry Persistence Joint Card Note — Narrowed to N=80/100 Cached Card

**Date:** 2026-04-02 (scope narrowed 2026-05-17 per audited_conditional `scope_too_broad` repair: binding scope is the cached N=80 and N=100 card only; the `N=120` probe row and the central-band benchmark comparison are diagnostic-only without separately registered artifacts)
**Status:** bounded dense same-graph joint card on `N ∈ {80, 100}`;
the `N=120` probe and central-band benchmark comparisons are
diagnostic-only without separately registered cached artifacts

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"narrow the claim to the
completed N=80/100 card or supply direct N=120 and central-band
benchmark artifacts before re-audit."*

This revision takes the narrowing option. The binding evidence of
this note is exactly the **N=80 (`npl=50`) and N=100 (`npl=60`) joint
card rows** from the registered cached log
`logs/2026-04-02-asymmetry-persistence-joint-card.txt`, including
`pur_cl`, `pur_min`, gravity, and corrected Born `|I3|/P` on the
matched-seed dense 3D generated graphs.

The §"Boundary check" `N=120` probe row (`npl=70`, 4 seeds) and the
comparison to the central-band benchmark are **demoted to
diagnostic-only**, out of the binding audited scope, because the
`N=120` probe and the central-band benchmark do not have separately
registered primary-runner cached artifacts in the current ledger.
Promoting either requires registering the corresponding primary
runner with a SHA-pinned cache. The bottom-line "not yet review-safe
beyond `N=120`" honest qualifier already in the note is retained.

## Question

The generated asymmetry-persistence lane already showed improvements in
`pur_cl`, and it stacked strongly with layer norm on `pur_min`.

The missing check was a one-page same-graph card with:

- `pur_cl`
- `pur_min`
- gravity
- corrected Born metric `|I3|/P`

## Setup

Script:
[scripts/asymmetry_persistence_joint_card.py](/Users/jonreilly/Projects/Physics/scripts/asymmetry_persistence_joint_card.py)

Log:
[logs/2026-04-02-asymmetry-persistence-joint-card.txt](/Users/jonreilly/Projects/Physics/logs/2026-04-02-asymmetry-persistence-joint-card.txt)

Parameters:

- dense 3D generated graphs
- `N=80` with `npl=50`
- `N=100` with `npl=60`
- `8` matched seeds
- thresholds `0.00, 0.10, 0.20`
- linear and layer-normalized propagation both measured
- corrected Sorkin metric includes `-P(empty)`

## Results

### N = 80

| thr | keep% | pur_cl lin | pur_cl ln | pur_min lin | pur_min ln | grav lin | grav ln | Born lin | Born ln |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 100.0 | 0.998 | 0.954 | 0.998 | 0.954 | -0.862 | -0.349 | 1.73e-15 | 4.12e-16 |
| 0.10 | 97.4 | 0.982 | 0.889 | 0.981 | 0.889 | -0.344 | +0.520 | 9.21e-16 | 2.68e-16 |
| 0.20 | 97.2 | 0.981 | 0.881 | 0.981 | 0.881 | -0.297 | +0.485 | 8.78e-16 | 2.36e-16 |

### N = 100

| thr | keep% | pur_cl lin | pur_cl ln | pur_min lin | pur_min ln | grav lin | grav ln | Born lin | Born ln |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 100.0 | 0.989 | 0.944 | 0.989 | 0.943 | +0.946 | +0.784 | 1.24e-15 | 3.01e-16 |
| 0.10 | 98.0 | 0.947 | 0.871 | 0.947 | 0.869 | +1.873 | +1.126 | 9.75e-16 | 2.82e-16 |
| 0.20 | 97.7 | 0.953 | 0.862 | 0.953 | 0.860 | +1.897 | +1.357 | 1.06e-15 | 3.15e-16 |

## Safe interpretation

This lane is now a real same-graph hard-geometry decoherence aid, but the
gravity side is density-sensitive and does not stay positive in the denser
`npl=60` rerun.

What is established:

- generated hard geometry improves `pur_cl`
- generated hard geometry also improves `pur_min`
- layer norm stacks strongly on the same generated graphs
- corrected Born remains machine-clean throughout
- at dense `N=80/100`, the generated lane stays Born-clean and improves
  decoherence, but gravity is not robustly positive across the denser
  `npl=60` rerun

Important nuance:

- `N=80` is directionally encouraging but not a strong gravity
  significance point; the main retained same-graph result is decoherence
  rather than a gravity win
- `pur_cl` and `pur_min` are nearly identical on these dense generated
  graphs, suggesting the decoherence floor is doing most of the work

Boundary check:

- a denser `N=120` probe (`npl=70`, `4` seeds) keeps corrected Born
  clean and still lowers `pur_min` under layer norm (`0.986 -> 0.946`),
  but gravity stays negative on all tested rows
- the review-safe joint claim should stop at dense `N=100` for the
  decoherence lane, and at that density the gravity result is not yet
  strong enough to beat the central-band benchmark

## Bottom line

Generated asymmetry persistence has moved from “interesting mechanism
pilot” to a retained bounded hard-geometry lane.

It is still not an asymptotic rescue, but it now supports three of the
four desired features:

1. topology-generated geometry
2. improved `pur_cl`
3. improved `pur_min`
4. Born-clean coexistence with positive gravity on dense `N=100`

The fourth item is not yet review-safe on the denser rerun, so the
current asymmetry-persistence verdict is:

- strong hard-geometry decoherence aid
- Born-clean
- not yet the best gravity+decoherence joint lane

The honest range for that claim is now: **dense `N=80-100`, bounded
before `N=120`**.

---

**Re-queued for re-audit 2026-05-17:** previous `unaudited` verdict cited packet incompleteness (missing helper-script imports from the restricted packet). The audit pipeline now populates `helper_runner_paths` per [PR #1371](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1371) so the next audit pass receives the complete packet. Helpers now declared: ``. The current re-queue is mechanical — no science content changes — and is documented here so the hash drift is explicit.
