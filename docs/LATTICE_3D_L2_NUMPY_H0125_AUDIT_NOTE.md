# 3D 1/L^2 + h^2 Numpy h=0.125 Audit

**Date:** 2026-04-05 (rerun 2026-05-23 with on-lattice active source)
**Status:** bounded positive on the reduced numpy audit family

**Audit-lane runner update (2026-05-09):** The primary runner `scripts/lattice_3d_l2_numpy_h0125_audit.py` now carries explicit assertion checks (`assert math.isclose(...)`, `assert abs(...) < EPS`, etc.) mirroring its existing PASS-condition booleans. This makes the runner's class-A invariants visible to `docs/audit/scripts/classify_runner_passes.py`. The runner output and pass/fail semantics are unchanged.

**Off-lattice source repair (2026-05-23):** The original 2026-04-05 audit
used the helper default `z_mass_phys = 3` for the active gravity / F~M
probes. With this reduced family's `phys_w = 1.5`, `make_field` requires a
node at `(2nl//3, 0, round(3/h))` which lies outside the transverse half-width
`hw = int(phys_w/h)` at every `h` in the ladder, so `make_field` returned
identically zero and the "active" gravity readout collapsed to a
free-vs-free comparison. The repair adds a `z_mass_active` parameter to
`run_card` and sets it to `1.0` in the audit runner so the source node lies
inside the reduced lattice at every spacing. The frozen result below
reports the on-lattice readouts; Born, `d_TV`, decoherence, and MI are
unchanged because they do not depend on `field_m`.

## Artifact chain

- [`scripts/lattice_3d_l2_numpy_h0125_audit.py`](/Users/jonreilly/Projects/Physics/scripts/lattice_3d_l2_numpy_h0125_audit.py)
- [`logs/runner-cache/lattice_3d_l2_numpy_h0125_audit.txt`](/Users/jonreilly/Projects/Physics/logs/runner-cache/lattice_3d_l2_numpy_h0125_audit.txt) (SHA-pinned audit-lane cache for the on-lattice rerun)
- prior off-lattice log: [`logs/2026-04-05-lattice-3d-l2-numpy-h0125-audit.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-05-lattice-3d-l2-numpy-h0125-audit.txt) (transient; kept for cross-reference, not version-controlled)

## Question

Can the retained 3D dense `1/L^2 + h^2` numpy lane complete a smaller fixed-family
continuum audit through `h = 0.125` without losing the basic weak-field physics?

This probe stays deliberately narrow:

- same dense 3D architecture class
- same `1/L^2` kernel and `h^2` measure
- reduced but fixed physical family for tractability
- one h ladder: `1.0, 0.5, 0.25, 0.125`
- on-lattice active source at `z_mass_active = 1.0` (inside `phys_w = 1.5`)

## Frozen result

The audit completes numerically on the reduced family:

- `h = 1.0`: 45 nodes, 5 layers, 324 edges
- `h = 0.5`: 441 nodes, 9 layers, 19,208 edges
- `h = 0.25`: 2,873 nodes, 17 layers, 456,976 edges
- `h = 0.125`: 20,625 nodes, 33 layers, 12,500,000 edges

The frozen observables (on-lattice active source at `z = 1.0`) are:

| h | Born `|I3|/P` | `d_TV` | `k=0` | Gravity `z=1.0` | `F~M alpha` | Decoherence | MI |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1.0 | `nan` | `0.2605` | `0` | `-0.009319 (AWAY)` | too few TOWARD points | `38.3%` | `0.1248` |
| 0.5 | `1.39e-15` | `0.6586` | `0` | `+0.003047 (TOWARD)` | `0.49` | `49.9%` | `0.4985` |
| 0.25 | `2.50e-15` | `0.6994` | `0` | `+0.005376 (TOWARD)` | `0.50` | `49.9%` | `0.4699` |
| 0.125 | `4.23e-15` | `0.6725` | `0` | `+0.006997 (TOWARD)` | `0.50` | `49.0%` | `0.3787` |

## Safe read

The numpy bridge is real:

- the reduced family runs through `h = 0.125`
- Born stays machine-clean for `h = 0.5, 0.25, 0.125`

With the source placed inside the reduced lattice, the weak-field gravity
lane **does** recover from `h = 0.5` onward:

- the gravity sign at `z = 1.0` is `TOWARD` (positive) for `h = 0.5, 0.25, 0.125`
- the active `F~M` fit gives `alpha approx 0.5` at every finer spacing
- the `h = 1.0` baseline is too coarse (`hw = 1`, single transverse ring) to
  resolve a `TOWARD` deflection, but Born is also `nan` there, so the
  coarsest row is the documented coarse-grid limitation rather than a
  failure of the finer-grid bounded readout

So the narrowest safe conclusion is:

- the reduced `3D 1/L^2 + h^2` numpy lane completes numerically through `h = 0.125`
- it preserves Born from `h = 0.5` down
- it preserves the bounded weak-field gravity sign/slope readout
  (TOWARD sign and positive `F~M` slope) on this audit family once the
  source is placed inside the reduced lattice

## Honest limitation

This is a credibility audit, not a full continuum theorem:

- the family is reduced for tractability
- the gravity readout is a single-axis weak-field probe at one active z
- the on-lattice source `z = 1.0` is closer to the slits than the original
  `z = 3` probe, so the readout tests the weak-field response at a smaller
  separation only
- the distance-law sweep stays empty on this reduced family because
  `max_z = int(phys_w * 0.9) = 1`; a full distance-law fit requires a
  wider transverse box (already exercised by the companion bridge runner
  at `phys_w = 3`)
- the result should not be overread as full 3D closure

## Branch verdict

Treat this as a bounded positive for the reduced `h = 0.125` credibility lane:

- the computation reaches `h = 0.125`
- the linear quantum bookkeeping survives
- the Newtonian weak-field lane reappears once the active source is placed
  inside the reduced lattice, with `F~M alpha approx 0.5` at every finer
  spacing

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/lattice_3d_l2_numpy.py`
- `scripts/numpy_replay_bootstrap.py`
