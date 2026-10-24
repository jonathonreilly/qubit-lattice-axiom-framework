# Hierarchy dimensional compression: supplied finite diagnostic

**Date:** 2026-06-18
**Type:** open_gate
**Claim type:** open_gate
**Scope:** finite supplied-matrix numerical diagnostic
**Primary runner:** [finite diagnostic](../scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py)

```yaml
proposal_allowed: false
bare_retained_allowed: false
```

## Supplied fixture and arithmetic

Use the runner's staggered nearest-neighbor matrix on a finite APBC box with
`Ls=2`, `Lt=2` or `10`, `u0=0.9`, and diagonal mass `m=0.01`. Its site index is
`(((x0*Ls+x1)*Ls+x2)*Lt+t)`; each coordinate wraps modulo its extent. A hop
crossing either boundary acquires a minus sign. Forward and backward matrix
increments are respectively `u0*eta/2` and `-u0*eta/2`, including that boundary
sign. The directional phases are `1`, `(-1)^x0`, `(-1)^(x0+x1)` and
`(-1)^(x0+x1+x2)`. Coincident neighbors accumulate; they are not overwritten.
This fully specifies the finite complex matrix used by the runner.

For each invertible fixture define `c(Lt)=Re tr(D^(-1))/(Ls^3 Lt)` and
`R=c(10)/c(2)`. The root calculations require `c(2) != 0` and `R>0`.
This note offers a numerical diagnostic at these supplied fixtures, not a
proof of invertibility or positivity for arbitrary boxes or parameters.
The runner retains its original numerical failures and exceptions.

It evaluates direct and inverse roots for `d=3,4,8,16`. Four numerical gates
compare the power and log forms of `R^(-1/4)` at `1e-12`, require separation
from `R^(-1/16)` greater than `0.02`, check `1/4=4/2^4` at `1e-12`, and check
the inequality `1/d != 4/2^d` at `1e-9` only for `d=1,2,3,5,6,8`.
These finite arithmetic checks do not determine a physical dimension or taste
multiplicity. In particular, `4/2^4` is supplied arithmetic, not a derivation of
a physical taste count. The previous retained-grade taste-authority contract
is withdrawn from the current argument; its complete source remains historical.

## Conditional coefficient interpretation

The [fixed-density coefficient-to-scale bridge](HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md) proves from the
supplied positive quartic law that a coefficient ratio maps to an inverse
fourth root. This still does not identify the electroweak VEV, and it does not
identify the computed condensate ratio `R` with that coefficient ratio.
The [EW neutral order-parameter coordinate bridge](HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md) defines a formal
vector and quartic readout. It does not derive that the hierarchy Matsubara
endpoint coefficient is the physical Higgs density. The endpoint-selection
residual remains open, including endpoint coefficient-to-physical-Higgs-density
selection and absolute scale. Neither bridge supplies a physical selector here.
The [restricted algebraic family](HIERARCHY_FIXED_DENSITY_PHYSICAL_SELECTOR_NO_GO_NOTE_2026-06-18.md) concerns only its supplied equations.

## Printed external context and thermal boundary

The runner preserves the historical printed comparison
`M_Pl=1.2209e19`, `alpha_bare=1/(4*pi)`, `u0=0.5934^(1/4)`,
`alpha_LM=alpha_bare/u0`, `v_pred=M_Pl*alpha_LM^16`, `v_obs=246.22`, and
`C_obs=v_obs/v_pred`. These imported numbers are not numerical pass predicates
and do not select the exponent or establish an EW prediction. The assertion
about absence of target imports is unscored narration, not an extra PASS.

The finite heat/determinant statistic is a supplied readout. A finite spectrum
has a saturating counting function and supplies no Weyl continuum asymptotic or
Stefan radiation law. Its fourth root is not a physical mass/density bridge.
The earlier thermal attribution is withdrawn, not replaced by a negative
proof against a future continuum construction.

## Recovery and execution boundary

The complete preceding argument, runner and cache are preserved at Git commit
`6919e7f72cc95c3df7d6a4e9aa1f43ab6d449dff` and in the external original-source
inventory `repair-9849-dimensional-readers/original-identities.json`. Historical
ledger assertions are not current scientific premises; no ledger is substituted
or restamped. The old cache is historical until a bounded execution binds the
revised source and its actual inputs. This source checkpoint claims no fresh run
or independent audit verdict.
