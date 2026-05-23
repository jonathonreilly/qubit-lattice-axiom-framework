# Mirror vs Central Head-To-Head Note

**Date:** 2026-04-03 (cache-reader rescope 2026-05-23 per audit `other` repair target on hard-coded cross-lane values; unsupported `N=40, NPL_HALF=50` row and through-`N=60` strict-pocket range claim dropped).
**Status:** structural support note — records a fixed comparison summary read directly from the registered runner caches of the cited one-hop mirror and dense central-band authorities. The ranking is a structural reading of those frozen registered cache rows, not a re-derivation, and is not load-bearing for either lane's bounded status.
**Claim type:** bounded_theorem

**Primary runner (load-bearing):** [`scripts/mirror_vs_central_head_to_head.py`](../scripts/mirror_vs_central_head_to_head.py) — registered cache-reader. It opens the three cited authority caches and prints the rows verbatim; exits zero on PASS and nonzero if any required cache file is missing or any required row cannot be parsed.
**Primary runner registered cache (load-bearing):** [`logs/runner-cache/mirror_vs_central_head_to_head.txt`](../logs/runner-cache/mirror_vs_central_head_to_head.txt) — registered cached stdout (`exit_code=0`, `status=ok`) backing the comparison summary below.

**Registered one-hop dependencies (load-bearing for the underlying lane rows):**

- Dense central-band + layer norm row source: [`docs/CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md`](CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md) — bounded high-N dense central-band lane authority supplying the `N = 80, npl = 80, LN+|y|` retained row. The cache-reader pulls that row directly from [`logs/runner-cache/central_band_dense_joint_highN.txt`](../logs/runner-cache/central_band_dense_joint_highN.txt).
- Mirror strict-default lane row source: [`docs/MIRROR_CHOKEPOINT_NOTE.md`](MIRROR_CHOKEPOINT_NOTE.md) — bounded mirror chokepoint authority on the strict default `NPL_HALF=25`, `connect_radius=4.0`, `layer2_prob=0.0` card; retained scope is `mirror p2=0` rows at `N=15` and `N=25` only, with same-card FAIL markers recorded at `N=40, 60, 80, 100`. The cache-reader pulls those rows directly from [`logs/runner-cache/mirror_chokepoint_joint.txt`](../logs/runner-cache/mirror_chokepoint_joint.txt).
- Mirror dense boundary-card lane row source: [`docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md) — bounded dense-boundary mirror chokepoint authority on the `NPL_HALF=60`, `connect_radius=5.0`, `layer2_prob=0.0` card; retained pre-fit retention rows at `N=40, 60, 80, 100` and the `N=120` gravity-wall row excluded from the fit. The cache-reader pulls those rows directly from [`logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt`](../logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt).

This note compares the registered dense central-band lane retained row
against the two cited registered mirror chokepoint pockets (the strict
default card and the dense boundary card) using the already-registered
artifact chain. The 2026-05-23 cache-reader rescope replaces the previous
hard-coded summary printer with a runner that opens the cited authority
caches and prints the rows verbatim, and drops the previously-quoted
`N=40, NPL_HALF=50` mirror row and through-`N=60` strict-pocket range
claim — neither was present in any cited retained mirror authority's
cache or retained scope.

Fairness note:

- the central-band lane reports `pur_min`
- the mirror lane reports `pur_cl`
- so the ranking below should be read as a full lane comparison, not a raw
  purity-to-purity contest

Script:
[`scripts/mirror_vs_central_head_to_head.py`](../scripts/mirror_vs_central_head_to_head.py)

## Comparison

### Dense central-band + layer norm

This is the best retained joint coexistence lane on the cited high-N dense
central-band authority. The cache-reader prints this row verbatim from
[`logs/runner-cache/central_band_dense_joint_highN.txt`](../logs/runner-cache/central_band_dense_joint_highN.txt).

Retained row (from the cited cache):

- `N = 80`, `npl = 80`
- `LN + |y|`
- Born `|I3|/P = 0.000±0.000`
- `pur_min = 0.500±0.000`
- gravity `+2.799±1.612`

Narrow read:

- stronger decoherence than the mirror strict default card
- bounded retained pocket on the high-N dense central-band card
- still Born-clean on the retained row

### Mirror chokepoint / Z2-protected transfer (strict default card)

This is the bounded mirror chokepoint pocket on the cited strict default
card (`NPL_HALF=25`, `connect_radius=4.0`, `layer2_prob=0.0`). The cited
authority retains `N=15` and `N=25` only and records same-card FAIL at
`N=40, 60, 80, 100`. The cache-reader prints these rows verbatim from
[`logs/runner-cache/mirror_chokepoint_joint.txt`](../logs/runner-cache/mirror_chokepoint_joint.txt).

Retained rows (from the cited cache):

- `N = 15`, `mirror p2=0`, Born `|I3|/P = 5.75e-16`, `pur_cl = 0.5769±0.02`, gravity `+1.2927±0.691`
- `N = 25`, `mirror p2=0`, Born `|I3|/P = 6.92e-16`, `pur_cl = 0.7329±0.05`, gravity `+2.2748±0.525`

Same-card FAIL markers (recorded in the cited cache, not retained):

- `N = 40, 60, 80, 100` all FAIL on the strict default card.

Narrow read:

- strong small-`N` gravity in the retained `N=15`/`N=25` rows
- decoherence-side advantage in the retained rows
- bounded retained pocket — does **not** extend through `N=40` or higher
  on this card

### Mirror chokepoint / Z2-protected transfer (dense boundary card)

This is the separately-retained bounded mirror chokepoint pocket on the
cited dense boundary card (`NPL_HALF=60`, `connect_radius=5.0`,
`layer2_prob=0.0`). The cited authority retains pre-fit retention rows at
`N=40, 60, 80, 100` and records a gravity wall at `N=120` (excluded from
the fit). The cache-reader prints these rows verbatim from
[`logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt`](../logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt).

Pre-fit retention rows (from the cited cache):

- `N = 40`, `mirror p2=0`, Born `|I3|/P = 1.05e-15`, `pur_cl = 0.8608±0.03`, gravity `+4.7499±0.666`
- `N = 60`, `mirror p2=0`, Born `|I3|/P = 1.54e-15`, `pur_cl = 0.8440±0.03`, gravity `+3.9733±0.473`
- `N = 80`, `mirror p2=0`, Born `|I3|/P = 2.43e-15`, `pur_cl = 0.8182±0.03`, gravity `+3.0551±0.672`
- `N = 100`, `mirror p2=0`, Born `|I3|/P = 1.13e-15`, `pur_cl = 0.9043±0.02`, gravity `+1.3089±0.570`

Gravity-wall row (recorded in the cited cache, excluded from the fit):

- `N = 120`, `mirror p2=0`, gravity `+0.0000±0.000`.

Narrow read:

- bounded retained pocket through `N = 100` on the dense boundary card
- strong gravity through `N = 80`, weakening by `N = 100`, and a wall at
  `N = 120`

## Conclusion (structural, registered-row-backed)

Reading the registered runner caches directly via the cache-reader, the
structural ranking from the cited registered rows is:

1. Dense central-band + layer norm (`N=80, npl=80, LN+|y|` retained row).
2. Mirror chokepoint pockets — strict default card retains `N=15`/`N=25`
   only; dense boundary card retains `N=40..100` with an `N=120` gravity
   wall.

So the mirror lane is best described as a **bounded challenger with strong
small-`N` gravity and symmetry protection on the strict default card, plus
a separately-retained bounded dense-boundary pocket through `N=100`**, not
the new retained joint winner.

This ranking is a structural reading of the cited registered cache rows;
it is not a re-derivation of either lane's status. The underlying
row statuses are owned by their respective notes (mirror strict default via
[`MIRROR_CHOKEPOINT_NOTE.md`](MIRROR_CHOKEPOINT_NOTE.md); dense boundary
card via [`MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md);
dense central-band high-N via [`CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md`](CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md)).

## What this note does NOT claim

- An `N=40, NPL_HALF=50` mirror row. This row is not present in any cited
  retained mirror authority's cache or retained scope; it was previously
  quoted by the hard-coded runner and the 2026-05-23 rescope drops it.
- A through-`N=60` retained range on the strict `NPL_HALF=50` probe. The
  cited strict-default authority retains `N=15`/`N=25` only and records
  same-card FAIL at `N=40` and higher; the `NPL_HALF=50` scaling probe is
  explicitly out-of-scope of that authority.
- A re-derivation of either lane's bounded status. The note reads cited
  caches; it does not recompute lane retention.

## Audit boundary (2026-05-23 — cache-reader rescope)

This revision addresses the generated-audit repair target:

> other: replace the hard-coded mirror row/range with values from the
> cited retained mirror authorities, or add a registered one-hop authority
> and assertion-gated cache for the `NPL_HALF=50` scaling probe.

This revision takes the first branch of the repair target. The hard-coded
summary printer is replaced by a cache-reader
([`scripts/mirror_vs_central_head_to_head.py`](../scripts/mirror_vs_central_head_to_head.py))
that opens the three cited authority caches and prints the retained rows
verbatim. The previously-quoted `N=40, NPL_HALF=50` mirror row and
through-`N=60` strict-pocket range claim are dropped, because no cited
retained mirror authority contains either. The mirror lane is now
described by the two retained pockets that the cited authorities actually
own: the strict default card (`N=15`/`N=25` only) and the dense boundary
card (`N=40..100` plus the `N=120` wall row excluded from the fit). The
structural ranking is unchanged in direction: dense central-band still
ranks above the mirror pockets on joint coexistence.

## Audit boundary (2026-05-10 — registered-dependency citation tightened)

This revision was the first pass at the repair target above. It lifted
the underlying lane row sources into the note header as registered
one-hop dependencies, but left the runner as a hard-coded summary
printer and retained an unsupported `N=40, NPL_HALF=50` mirror row plus a
through-`N=60` strict-pocket range claim. The 2026-05-23 cache-reader
rescope supersedes that pass: the runner is now a cache-reader and the
unsupported row/range claims are dropped.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links for
the cited lane authorities — the dense central-band lane authority and
both mirror chokepoint authorities — that the head-to-head ranking
reads from registered cache rows. It does not promote this note or
change the audited claim scope.

- [CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md](CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md) — dense central-band + layer norm joint coexistence lane authority supplying the `N = 80, npl = 80, LN+|y|` retained row.
- [MIRROR_CHOKEPOINT_NOTE.md](MIRROR_CHOKEPOINT_NOTE.md) — mirror chokepoint strict-default lane authority supplying the retained `N=15`/`N=25` `mirror p2=0` rows and the same-card FAIL markers at `N=40, 60, 80, 100`.
- [MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md) — mirror chokepoint dense-boundary lane authority supplying the pre-fit retention `mirror p2=0` rows at `N=40, 60, 80, 100` and the `N=120` gravity-wall row excluded from the fit.
