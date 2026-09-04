# Hard Geometry Head-To-Head Note

**Date:** 2026-04-03
**Claim type:** meta
**Status:** support - structural or confirmatory support note
**Primary runner:** `scripts/hard_geometry_head_to_head.py`


This note compares the retained hard-geometry and symmetry lanes that the
head-to-head runner currently emits as a review-safe ranking layer:

- dense central-band hard geometry + layer norm
- mirror chokepoint / Z2-protected transfer geometry
- generated asymmetry-persistence hard geometry + layer norm

The comparison is intentionally narrow. It uses only the retained metrics
that are already supported on `main`:

- corrected Born `|I3|/P`
- `pur_min` / `pur_cl`
- gravity centroid delta
- narrow range statements

## 1. Dense Central-Band + Layer Norm

This is the strongest retained same-graph joint lane.

Best retained high-N row:

- `N = 80`, `npl = 80`
- `LN + |y|`
- Born: `0.000±0.000`
- `pur_min = 0.500±0.000`
- gravity: `+2.799±1.612`

With collapse included, the same pocket keeps Born clean and lowers the
purity floor further:

- `LN + |y| + collapse`
- purity: `0.374±0.057`
- gravity: `+2.929±1.467`

Narrow read:

- this is the best joint coexistence pocket
- it is Born-clean
- it is still bounded and narrows by `N = 100`

## 2. Mirror Chokepoint / Z2-Protected Transfer

This is the strongest symmetry-protected bounded challenger that the runner
currently ranks.

Runner-output retained row (strict chokepoint pocket):

- `N = 40`, `NPL_HALF = 50`
- strict chokepoint mirror
- Born-clean through `N = 60` on this strict pocket
- `pur_cl = 0.8764±0.03`
- gravity: `+4.6161±0.721`

Narrow read:

- stronger retained gravity than the dense central-band row at `N = 40/60`
- weaker decoherence than the dense central-band row
- still Born-clean in the retained pocket

## 3. Generated Asymmetry-Persistence + Layer Norm

This remains the strongest retained gravity-side lane.

Best retained direct gravity row:

- `N = 100`
- threshold `0.20`
- Born: `2.31e-16`
- `pur_cl = 0.921±0.043`
- gravity: `+2.102±0.825`

Mass-side follow-up:

- threshold `0.10`, LN: `delta ~= 0.4032 * M^0.420`, `R^2 = 0.970`
- threshold `0.20`, LN: `delta ~= 0.5332 * M^0.262`, `R^2 = 0.892`

Narrow read:

- this lane is Born-clean on the dense probe
- it carries the stronger direct gravity-side signal
- it is the best gravity side alone
- it is not the best joint coexistence lane because the gravity sign is
  density-sensitive and not uniformly positive across the dense scan

## Head-To-Head Ranking

1. Best joint coexistence: dense central-band + layer norm
2. Best symmetry-protected bounded challenger: mirror chokepoint / Z2-protected transfer
3. Best gravity side alone: generated asymmetry-persistence + layer norm

## Bottom Line

Hard geometry remains the shared enabler. The cleanest retained joint lane is
dense central-band + layer norm. The strongest symmetry-protected bounded
challenger is mirror chokepoint / Z2-protected transfer, Born-clean through
`N = 60` on the strict `NPL_HALF = 50` pocket. The strongest retained
gravity-side-alone lane is generated asymmetry-persistence + layer norm.

## 2026-05-18 audit-conditional repair: narrowed to runner-actual outputs

Per the 2026-05-17 audit verdict, two upstream authorities are missing:
the grown-graph density-optimum authority and the upstream Z2 x Z2
Born/decoherence joint-validator authority. This revision narrows the
meta-comparison to constants the current head-to-head runner actually
outputs, removing rows that depended on the unregistered upstreams.
Those rows are queued as out-of-scope follow-ups awaiting upstream
retained-grade registration.

Specifically narrowed out of this revision:

- Section 3 "Higher-Symmetry `Z2 x Z2`" — depended on the upstream
  `Z2 x Z2` Born/decoherence joint-validator authority that the
  supplied gravity-probe authority explicitly does not check.
- Section 5 "Grown-Graph Density Optimum near `npl≈30`" — depended on
  the retained grown-graph density-optimum authority, which is not
  registered as a retained source on `main`.
- Mirror chokepoint section: the dense boundary-scan row (`N = 100`,
  `NPL_HALF = 60`, canonical boundary fit `R² = 0.126`) is dropped from
  this revision because the head-to-head runner emits only the strict
  `N = 40` / `NPL_HALF = 50` pocket. The dense boundary scan remains
  upstream-retained on `MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md` and can
  be re-ingested once the runner is refreshed to emit it.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links for
the underlying hard-geometry / mirror / asymmetry-persistence lane
authorities consumed by the runner-actual head-to-head ranking. It does
not promote this note or change the audited claim scope.

- [CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md](CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md) — dense central-band + layer norm joint coexistence lane authority.
- [MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md) — mirror chokepoint / Z2-protected transfer strict-pocket authority (dense boundary scan held upstream pending runner refresh).
- [ASYMMETRY_PERSISTENCE_JOINT_CARD_NOTE.md](ASYMMETRY_PERSISTENCE_JOINT_CARD_NOTE.md) — generated asymmetry-persistence + layer norm gravity-side lane authority.
- [ASYMMETRY_PERSISTENCE_MASS_SCALING_NOTE.md](ASYMMETRY_PERSISTENCE_MASS_SCALING_NOTE.md) — asymmetry-persistence mass-side `delta ~ M^alpha` follow-up.
