# K-Z SU(3) beta=6 Convention Split Note

Date: 2026-06-06

Status: no-go

actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This artifact prunes one source/convention route; it does not derive a beta=6 bracket."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Summary

This block sharpens the remaining K-Z external-lift blocker from PR484/PR
#2804. The old shortcut was:

```text
use W_lift ~= 0.05 as the SU(3), Wilson beta=6 plaquette bracket width.
```

That shortcut does not survive the source convention check. In the finite
SU(3) bootstrap paper, the Wilson-action coefficient is written in the paper
coordinate `lambda`, while the framework target uses the standard Wilson
`beta` convention. Equating the coefficients gives

```text
N / (2 lambda) = beta / (2 N)
lambda = N^2 / beta.
```

For `N = 3` and Wilson `beta = 6`, the paper coordinate is therefore
`lambda = 9 / 6 = 1.5`.

The vector extraction from the source-bundle figure reproduces the old narrow
width near `0.05` at plotted `lambda = 3.0`, not at the Wilson beta=6
coordinate `lambda = 1.5`.

## Source Bridge

Primary source:

- Zhengxuan Guo, Xizhi Han Li, Junyu Liu Yang, and Jinming Zhu,
  "Bootstrapping SU(3) lattice Yang-Mills theory," JHEP 12 (2025) 033,
  arXiv:2502.14421.
- Springer PDF:
  `https://link.springer.com/content/pdf/10.1007/JHEP12%282025%29033.pdf`
- arXiv source bundle:
  `https://arxiv.org/e-print/2502.14421`

The runner uses vector coordinates from source-bundle file
`figures/4Dsu3plotcd.eps`. This is an image/vector-derived audit aid, not a
table-derived numeric source. It is sufficient to diagnose the convention
split because it shows which plotted coordinate reproduces the old `W_lift`
width. It is not sufficient to certify a new theorem-grade beta=6 bracket.

## Runner Result

Runner:

```text
scripts/frontier_kz_su3_beta6_convention_split_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_kz_su3_beta6_convention_split_2026_06_06.txt
```

Scorecard:

```text
PASS=13 FAIL=0
```

Key computed brackets:

| coordinate | image-derived lower | image-derived upper | width |
| --- | ---: | ---: | ---: |
| plotted `lambda = 1.5` (`SU(3)`, Wilson `beta=6`) | 0.412899 | 0.658094 | 0.245195 |
| plotted `lambda = 3.0` | 0.851571 | 0.900296 | 0.048725 |

Thus the old `W_lift ~= 0.05` width is consistent with the plotted
`lambda=3.0` figure slice, while Wilson `beta=6` maps to the much wider
image-derived slice at `lambda=1.5`.

## No-Go Boundary

This block prunes only this route:

```text
old W_lift ~= 0.05
  -> source-certified finite SU(3), Wilson beta=6 bracket
```

The implication is invalid unless a separate convention bridge shows that the
framework beta target was intended to be the paper's plotted `lambda=3.0`
coordinate, or unless a direct beta=6 source table/reproduction supplies the
bracket.

This block does not rule out:

- a repo-owned finite SU(3), Wilson beta=6 SDP reproduction;
- a primary source table or source-data extraction at the correct coordinate;
- a revised K-Z lift with explicit beta/lambda conventions;
- non-K-Z gauge-scalar routes.

## Claim Boundary

This is negative route pruning, not a positive theorem. It does not certify
`W_lift`, does not derive a beta=6 plaquette bracket, and does not close the
K-Z external-lift package. The remaining acceptable paths are a direct
source-data/table extraction at `lambda=1.5` or a repo-owned finite SU(3),
Wilson beta=6 reproduction with cutoff, solver, and tolerance recorded.
