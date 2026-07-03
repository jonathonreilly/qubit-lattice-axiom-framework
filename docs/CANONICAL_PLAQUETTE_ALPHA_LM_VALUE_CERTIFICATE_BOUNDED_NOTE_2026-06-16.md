# Canonical Plaquette Alpha_LM Value Certificate: Bounded Arithmetic Note

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Type:** bounded arithmetic certificate / dependency-edge support
**Source runner:** [`scripts/frontier_canonical_plaquette_alpha_lm_value_certificate_2026_06_16.py`](../scripts/frontier_canonical_plaquette_alpha_lm_value_certificate_2026_06_16.py)
**Runner cache:** [`logs/runner-cache/frontier_canonical_plaquette_alpha_lm_value_certificate_2026_06_16.txt`](../logs/runner-cache/frontier_canonical_plaquette_alpha_lm_value_certificate_2026_06_16.txt)

## Scope

This note is the narrow canonical alpha/plaquette value certificate requested
by downstream YT P1 re-audit blockers. It does not derive the Wilson
plaquette value `P = 0.5934`, and it does not upgrade the plaquette lane.
It only records the arithmetic used by `scripts/canonical_plaquette_surface.py`
from the parent [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
reuse surface:

```
P = 0.5934
u_0 = P^(1/4)
alpha_bare = 1 / (4 pi)
alpha_LM = alpha_bare / u_0
alpha_s(v) = alpha_bare / u_0^2
```

The source authority is the parent plaquette reuse surface plus the helper
module [`scripts/canonical_plaquette_surface.py`](../scripts/canonical_plaquette_surface.py).
Independent audit owns this row's effective status; this branch does not write
or predict an audit verdict.

## Result

From the helper constants:

```
P              = 0.593400000000000
u_0            = 0.877681381198684
alpha_bare     = 0.079577471545948
alpha_LM       = 0.090667836017286
alpha_LM/(4pi) = 0.007215117140798
alpha_s(v)     = 0.103303816122267
```

The only proof content is arithmetic identity checking:

- `u_0^4 = P`;
- `alpha_bare = 1/(4 pi)`;
- `alpha_LM * u_0 = alpha_bare`;
- `alpha_s(v) * u_0^2 = alpha_bare`.

## Firewalls

- No new axiom or primitive premise is introduced.
- The value `P = 0.5934` remains exactly as scoped in
  [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md).
- This note is not a Monte Carlo certificate, infinite-volume proof,
  analytic beta=6 closure, or physical coupling derivation.
- Downstream notes may cite this note only for the displayed canonical
  arithmetic and dependency edge; any physical use still inherits the parent
  plaquette scope and any lane-specific bridge requirements.

## Verification

Run:

```
PYTHONPATH=scripts python3 scripts/frontier_canonical_plaquette_alpha_lm_value_certificate_2026_06_16.py
```

Expected summary:

```
SUMMARY: PASS=25  FAIL=0
```
