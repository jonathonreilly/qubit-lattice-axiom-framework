# Direct Wilson-Loop Static-Potential Certificate Gate

**Date:** 2026-04-30; narrowed 2026-05-27
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_alpha_s_direct_wilson_loop_static_certificate.py`
**Historical broad runner:** `scripts/frontier_alpha_s_direct_wilson_loop.py`
**Status authority:** independent audit lane only

---

## Status

This row is narrowed to a finite certificate gate for a supplied
Wilson-loop/static-potential packet on the configured `beta = 6`
`Cl(3)/Z^3 SU(3)` Wilson surface.

The row no longer claims a closed framework derivation of the physical
`alpha_s(M_Z)` observable. The physical Sommer scale, continuum QCD running,
threshold matching, and pure-gauge-to-full-QCD sea-quark bridge are explicitly
out of scope for this note. They may appear in the historical certificate as
context fields, but the repaired runner does not use those fields as
load-bearing evidence.

## Bounded Claim

For the certificate at

```text
outputs/alpha_s_direct_wilson_loop_certificate_2026-04-30.json
```

the runner verifies the following finite claims:

1. The packet declares Wilson-loop/static-potential authority on the configured
   `beta = 6` Wilson surface.
2. It does not use `alpha_LM`, `u_0`, `alpha_bare/u_0^2`, or the plaquette
   chain as authority.
3. It contains three lattice volumes with at least `500` saved configurations
   per volume.
4. The recorded Wilson-loop means and errors pass the runner's finite
   statistics checks.
5. The recorded static-potential plateau diagnostics pass.
6. The recorded Cornell/static-force diagnostics are finite and internally
   consistent on the certificate surface.
7. The recorded local force-scheme `alpha_qq` values are finite at multiple
   lattice separations.

That is the entire proposed re-audit surface.

## Explicit Non-Claims

This note does not claim:

- a framework derivation of `g_bare = 1`;
- a framework derivation of physical units or a physical Sommer scale anchor;
- a derivation of QCD running or heavy-threshold matching;
- a derivation of a pure-gauge-to-full-QCD sea-quark bridge;
- a retained physical `alpha_s(M_Z)` theorem;
- a PDG-window numerical-match theorem;
- a promotion of downstream CKM, EW, YT/top, hierarchy, or publication rows;
- an audit verdict or direct ledger retag.

The historical broad runner and certificate still contain `alpha_s(M_Z)` and
PDG-comparator fields. In this repaired row those fields are context only and
are deliberately excluded from the primary runner's pass/fail gates.

## Relation To Existing Authorities

The finite certificate is on the graph-first `SU(3)` Wilson surface described
by [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md).
The older plaquette route
[`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md) is
not authority for this row; the certificate records the older
`alpha_LM/u_0` value only as a non-authority cross-check.

The historical broad note cited external Sommer, FLAG, and PDG references for
the physical `M_Z` bridge. Those references remain useful comparison context,
but they are not load-bearing dependencies of this narrowed row.

## Verification

Run:

```bash
python3 scripts/frontier_alpha_s_direct_wilson_loop_static_certificate.py
```

Expected result:

```text
Direct Wilson-loop static-potential certificate: PASS
PASS=16 FAIL=0
```

The historical broad runner remains available for context:

```bash
python3 scripts/frontier_alpha_s_direct_wilson_loop.py
```

Its `alpha_s(M_Z)` checks are not the source of the repaired claim.

## Audit Request

Please re-audit only the bounded finite certificate gate above. The intended
safe scope is the Wilson-loop/static-potential packet on the configured
surface. The physical `alpha_s(M_Z)` bridge remains out of scope until
separate retained bridge theorems or accepted-premise records close the scale,
running, threshold, and full-QCD steps. Any effective status is assigned only
by the independent audit lane.
