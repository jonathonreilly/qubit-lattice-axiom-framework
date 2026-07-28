# Mesoscopic Surrogate Threshold 2D Note

**Date:** 2026-04-04 (implementation-specific scope boundary and downstream
hygiene added 2026-07-28)
**Status:** bounded finite-computation note for the exact implementation below.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after independent audit.

## Artifact chain

- Script: [`scripts/mesoscopic_surrogate_threshold_2d.py`](../scripts/mesoscopic_surrogate_threshold_2d.py)
- Audit cache stdout:
  [`logs/runner-cache/mesoscopic_surrogate_threshold_2d.txt`](../logs/runner-cache/mesoscopic_surrogate_threshold_2d.txt)
- Frozen legacy log:
  [`logs/2026-04-04-mesoscopic-surrogate-threshold-2d.txt`](../logs/2026-04-04-mesoscopic-surrogate-threshold-2d.txt)

## Claim boundary

This note makes one implementation-specific finite claim. With the
source-identity-pinned bytes of the runner and its two declared helper inputs,
at their fixed constants, every requested row at

`topN = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 20, 25, 32, 40, 49, 64, 81`

satisfies both programmed stability gates:

- relative stage-1 / stage-2 response-ratio difference
  `|r2-r1| / max(|r1|, 1e-30) <= 0.01`; and
- stage-1 / stage-2 source carry
  `sum_i sqrt(src1_i * src2_i) >= 0.99`, with the sum over the union of
  profile-bin keys.

The claim is about those computed rows of this fixture, not about a retained
2D framework family or about other propagation laws, parameter choices,
boundary states, source constructions, normalizations, observables, or support
values.

## Fixed implementation

The runner imports its full construction from
[`scripts/mesoscopic_surrogate_two_stage_2d.py`](../scripts/mesoscopic_surrogate_two_stage_2d.py)
and
[`scripts/lattice_2d_continuum_distance.py`](../scripts/lattice_2d_continuum_distance.py).
The load-bearing fixture choices are:

- directed open-boundary 2D grid from `generate(PHYS_L=20, PHYS_W=12,
  MAX_D_PHYS=5, H=0.5)`;
- the implemented barrier mask at layer `nl // 3`, with transverse indices
  `iy=-5,...,5` blocked;
- angular weight parameter `BETA=0.8` and phase parameter `K=5.0`;
- point-packet launch at `PROBE_Y=5.0` and normalized detector-profile
  compression;
- distributed and centroid-matched point fields with
  `FIELD_STRENGTH=5e-5` and the implemented `1/(r+0.1)` regularization;
- link action `L * (1 - lf)`, where `lf` is the mean endpoint field, and
  transfer weight `exp(i K action) * exp(-BETA theta^2) / L`;
- stage 1 formed from the normalized top-`N` compression of the free detector
  profile and stage 2 formed from the same compression of the stage-1
  distributed-source response;
- response ratio equal to the distributed-source centroid shift divided by
  the centroid-matched point-source shift; and
- source carry equal to the overlap computed by `overlap(src1, src2)`.

None of these choices is asserted here to be derived from the framework axiom
or approved-primitive surface. They define the finite fixture on which the
reported evaluation is performed.

## Computed result

The runner recomputes every listed support row and reports:

- all 19 rows satisfy both stability gates;
- maximum relative stage-1 / stage-2 response-ratio difference
  `0.0066069 <= 0.01`, attained at `topN=12`;
- minimum source carry `0.999999997764 >= 0.99`, attained at `topN=5`; and
- `topN=1`, the smallest listed support, also satisfies both gates. This last
  row is a boundary check: its one-bin distributed source is the
  centroid-matched point source by construction.

The detector profile has 49 bins. Consequently, the 19 requested rows contain
17 distinct normalized source profiles: `topN=49`, `64`, and `81` all saturate
the same 49-bin profile. Those three requested rows are retained in the output
to make the support-list boundary explicit; they are not three independent
profile tests.

The source-identity-pinned runner cache records these finite checks with six
assertion-backed class-C pass lines:

- `frozen_topN_support_list_scanned`
- `all_scanned_topN_stable`
- `stage_ratio_relative_error_within_one_percent`
- `support_carry_floor`
- `detector_support_saturation_disclosed`
- `smallest_listed_topN_satisfies_stability_gates`

`SOURCE_Y=5.0` and `PACKET_SIGMA=1.25` remain printed fixture metadata but are
not consumed by this runner's row computation.

## Citable surface and downstream hygiene

The citable result is exactly the 19-row finite evaluation above. The word
"threshold" in the title names the scan; the computation does not establish a
threshold law or the absence of one outside the listed fixture rows.

**Downstream hygiene (2026-07-28; PR #5676):** citations in the alternate-family
scout, annular/tapered sweep, and persistent-readiness index were narrowed to
the exact finite result here. Any citation to this note may use only the fact
that all 19 requested `topN` rows pass the two programmed gates for the exact
implementation and constants above, with 17 distinct normalized source
profiles. It must not treat this note as authority that the harness is a
retained framework family, that support shrinkage is generally irrelevant, or
that the same result holds under another lattice scale, boundary state,
propagation action, field strength, source construction, normalization,
observable, stability criterion, or support value. The historical
helper/runner/log phrase "Retained 2D ordered-lattice family" is fixture-era
labeling and carries no authority in this note's claim. This dated boundary
changes the note hash so the row re-enters independent re-audit.

## What this note does not claim

- A framework derivation or physical identification of the implemented
  propagation and surrogate-source harness.
- A universal, continuum, additional-finite-case, or alternate-observable
  threshold statement.
- A persistent-mass theorem, inertial-response theorem, or localized-object
  construction.
- Any conclusion about which mechanism should replace support shrinkage in a
  downstream physics lane.
