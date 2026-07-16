# Gauge-Vacuum Plaquette Supplied-Rho Interface Conditional Theorem

**Date:** 2026-06-12; supplied-input repin 2026-07-16
**Claim type:** positive_theorem
**Claim scope:** source-sector readouts of a finite factorized marked-plaquette
kernel after a residual operator is explicitly supplied as character-diagonal.
Within that declared diagonal class, its coefficient vector `rho_(p,q)` is a
complete interface. This note does not prove that the physical stripped Wilson
residual belongs to that class.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit verdict or effective status.
**Runner:** `scripts/gauge_vacuum_plaquette_compression_scope_rho_complete_interface_narrow_2026_06_12.py`
**Runner cache:** `logs/runner-cache/gauge_vacuum_plaquette_compression_scope_rho_complete_interface_narrow_2026_06_12.txt`

## Scope correction

An earlier version claimed that the three-dimensional Wilson environment
reached the marked readout only through diagonal coefficients `rho_(p,q)`.
That statement imported the now-retracted inference that the stripped Wilson
residual is character-diagonal. It is replaced by the following conditional
statement:

> If the residual source operator is supplied as
> `R[rho]=diag(rho_(p,q))`, then every readout defined only from
> `T[rho]=M_beta D_beta^loc R[rho] M_beta` and `J` depends on that supplied
> residual through `rho` alone.

This is an exact interface theorem inside the supplied diagonal class. It is
not a theorem that the physical environment has no off-diagonal character
data.

## One-hop authorities

- [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
  supplies the conditional finite-dimensional `T=M D M` algebra for an
  explicitly supplied diagonal middle operator.
- [GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md)
  supplies the explicit finite local packet
  `D_beta^loc chi_(p,q)=a_(p,q)(beta)^4 chi_(p,q)` while leaving the actual
  mixed-kernel compression bridge open.
- [GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md)
  supplies only formal quotient/convolution packaging after diagonal inputs
  have been supplied.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  supplies bounded tensor-word packets and names the physical boundary-data
  target; it does not identify that target with the stripped residual.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies a conditional linkwise local factorization used by finite packets.

The temporal-gauge linkwise factorization note remains relevant to local
finite packets, but its trivial-channel statement applies when the function
being integrated is independent of the non-marked links. Unmarked spatial
plaquette weights in the actual environment violate that independence
hypothesis, so it cannot establish the physical diagonal interface by itself.

Context pointers, not one-hop authorities:
docs/GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md,
docs/GAUGE_VACUUM_PLAQUETTE_WIDTH_REDUCTION_MAP_DERIVED_COUPLED_LIFT_BOUNDED_NOTE_2026-06-12.md.

## Conditional theorem

On a finite character box, supply

`M_beta=exp[(beta/2)J]`,

`D_beta^loc chi_(p,q)=a_(p,q)(beta)^4 chi_(p,q)`,

and a residual diagonal sequence

`R[rho] chi_(p,q)=rho_(p,q)(beta) chi_(p,q)`.

Define

`T[rho](beta)=M_beta D_beta^loc R[rho] M_beta`.

Let `F` be any deterministic readout whose only operator inputs are
`T[rho](beta)` and `J`. If `rho^(1)=rho^(2)` entry by entry on the same finite
box and normalization convention, then

`R[rho^(1)]=R[rho^(2)]`,

`T[rho^(1)]=T[rho^(2)]`,

and therefore

`F(T[rho^(1)],J)=F(T[rho^(2)],J)`.

Thus `rho` is a complete interface for this explicitly declared diagonal
model class. The conclusion follows from equality of the supplied operators;
it does not discard any data from a more general operator.

## Hostile control: diagonal projection is not a physical completeness proof

Let `C` be a general environment operator and define the lossy helper

`rho_diag(C):=diag(C)`.

If `E` is any nonzero off-diagonal matrix, then

`rho_diag(C+E)=rho_diag(C)`

even though `C+E != C`. A readout implementation that first calls
`rho_diag` will therefore return the same answer for both raw operators by
construction. That equality demonstrates information loss in the helper, not
physical irrelevance of off-diagonal character mixing.

The runner includes exactly this control. The primary source-sector runner
strengthens it with a strictly positive self-adjoint swap-symmetric mixing
operator and rejects a guarded `kappa`-only helper when off-diagonal entries
are present.

## Preserved finite packet results

The existing runner independently supplies finite diagonal `rho` vectors for
its reference calculations. Those calculations remain valid inside the
conditional class:

- `rho=delta_(0,0)` reproduces the finite `P_triv` reference;
- the one-word finite packet reproduces its declared composed readout;
- two identical supplied `rho` vectors give identical projected readouts.

No claim is made that these supplied vectors are the physical Wilson residual
or that the raw physical operator is diagonal.

## What this covers

- source-sector readouts of the factorized marked plaquette kernel
  `T[rho]=M_beta D_beta^loc diag(rho) M_beta`;
- finite packet calculations that explicitly define their own diagonal
  `rho` input;
- exact equality of readouts for equal supplied diagonal operators.

## What this does not cover

- Wilson-derived character diagonality or central-convolution structure;
- completeness of `diag(C)` for a general positive swap-symmetric operator;
- identification of static spatial-environment coefficients with the
  algebraically stripped two-slice residual;
- the physical `rho_(p,q)(6)`, the full tensor-transfer limit, or analytic
  `P(6)`;
- observables outside the marked source-sector kernel.

## Command

```bash
python3 scripts/gauge_vacuum_plaquette_compression_scope_rho_complete_interface_narrow_2026_06_12.py
```
