# Gauge-Vacuum Plaquette Internal-Link Contraction Derived Narrow Theorem

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite derivation of the internal-link contraction
convention used by the two-strip environment packet at `beta = 6`, tensor
`NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`, and source
`MODE_MAX = 200`. This note decides the finite class-channel coefficient
used for the shared internal link between two compressed units in one
two-strip layer. It does not compute the full physical `3D` unmarked spatial
Wilson environment, a wider slab limit, the strip-depth direction, a `3D`
stack, an `L_perp` limit, analytic `P(6)`, or a repinning.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_internal_link_contraction_derived_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_internal_link_contraction_derived_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet inputs are restated on
their scoped surfaces.

Context pointers, not one-hop authorities:
docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md,
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py.

## One-Hop Authorities

- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the Wilson weight as a class function on a plaquette/link holonomy and
  for the matrix-coefficient convolution eigenvalue `c_lambda(beta) /
  d_lambda`.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the Schur dictionary
  `integral chi_lambda(V W^(-1)) chi_mu(W) dW =
  delta_(lambda,mu) chi_lambda(V) / d_lambda`.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the tensor-transfer construction language: expand spatial plaquette
  factors in characters and integrate shared slice links by Haar/Peter-Weyl
  decomposition.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `D_lambda = c_lambda(6)/(d_lambda c_0(6))` packet,
  the `tensor_word` construction, and the finite `SU(3)`
  fundamental/antifundamental fusion primitives on `B_4`.

## Quote-Anchored Inputs

The mixed-kernel authority writes the one-link Wilson weight as a class
function and states the character expansion:

```text
w_beta(g) = sum_lambda c_lambda(beta) chi_lambda(g).
```

It also states the matrix-coefficient convolution law:

```text
integral_G K_(x,mu)(U', U) lambda_(i,j)(U) dU
  = ( c_lambda(beta) / d_lambda ) lambda_(i,j)(U').
```

The Schur authority gives the character form of the same connected
matrix-element contraction:

```text
integral chi_lambda(V W^(-1)) chi_mu(W) dW
  = delta_(lambda,mu) chi_lambda(V) / d_lambda.
```

Equivalently, after placing the fixed neighboring holonomies into the two
traces,

```text
integral_SU(3) chi_lambda(U A) chi_mu(U^dagger B) dU
  = delta_(lambda,mu) chi_lambda(A B) / d_lambda.                         (1)
```

The spatial-environment tensor-transfer authority says that one slice step
expands every spatial plaquette factor in characters and integrates the
shared slice links. It also identifies the finite tensor ingredients as
products of Wilson coefficients and exact `SU(3)` fusion/intertwiner
multiplicities.

The finite tensor-word authority fixes the finite coefficient convention:

```text
D_lambda := c_lambda(6) / (d_lambda c_0(6)).
```

In the central boundary-character convention this same normalized class
function has coefficient `d_lambda D_lambda` in front of `chi_lambda`.
The two-strip ambiguity in the context note was whether the internal
environment-link channel should use that full central coefficient
`d_lambda D_lambda`, or the dimension-stripped coefficient `D_lambda`.

## Deciding Derivation

The Wilson Boltzmann factor is a class function of the plaquette holonomy,
not of a detached link label. For two adjacent plaquette/unit factors sharing
an internal environment link, write the shared link as `U` and absorb the
other three link factors of the two plaquette holonomies into fixed matrices
`A` and `B`. The two traces then contain the same link variable before Haar
integration:

```text
chi_lambda(U A),        chi_mu(U^dagger B).
```

So the shared link is in the connected-trace situation `(1)`, not in the
disconnected class-function identity

```text
integral_SU(3) chi_lambda(U) chi_mu(U^dagger) dU = delta_(lambda,mu).
```

Apply `(1)` to the finite central coefficient:

```text
(d_lambda D_lambda)
  * integral_SU(3) chi_lambda(U A) chi_mu(U^dagger B) dU

= (d_lambda D_lambda)
  * delta_(lambda,mu) chi_lambda(A B) / d_lambda

= D_lambda * delta_(lambda,mu) chi_lambda(A B).                           (2)
```

Thus the Haar contraction contributes exactly the inverse-dimension factor
that removes the `d_lambda` from the boundary-character class coefficient.
In the finite two-strip packet, the existing outer unit factors `D_a D_b`
are unchanged; the deciding internal-link channel weight is the scalar
`D_lambda`.

## Small Theorem

Let `a,b in B_4` be the two compressed unit labels in one two-strip layer.
Let `N_(a,b)^lambda` be the finite `SU(3)` tensor-product multiplicity used
by the two-strip runner. The internal-link factor licensed by the connected
plaquette-holonomy contraction is

```text
E_derived(a,b)
  = 1 + sum_(lambda != (0,0)) D_lambda N_(a,b)^lambda,                    (3)
```

where

```text
D_lambda = c_lambda(6) / (d_lambda c_0(6)).
```

The alternate full-character factor

```text
E_full(a,b)
  = 1 + sum_(lambda != (0,0)) d_lambda D_lambda N_(a,b)^lambda
```

is the disconnected class-coefficient reading. It omits the inverse-dimension
from the shared-link Haar step and is not the derived connected-trace reading.

## Normalization

Within this finite scalar class-channel internal-link coefficient, no
additional normalization freedom survives the quoted identities. The
normalization chain is:

```text
central boundary law coefficient = d_lambda D_lambda
connected shared-link Haar factor = 1 / d_lambda
derived internal-link coefficient = D_lambda.
```

The remaining open normalization object is narrower: a future all-link
two-strip tensor with explicit non-class intertwiner bases, non-scalar
magnetic indices, and any corresponding `6j` basis normalization. This note
does not build that object. It fixes only the finite class-channel internal
link used by the W38 two-strip packet.

## Derived Two-Strip Readout

The runner rebuilds the strip transfer with `(3)` and compares it to the two
W38 branches in scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py.

It matches the dimension-stripped branch exactly as a matrix in the same
double-precision construction:

```text
max |E_derived - E_dimension_stripped| = 0.000e+00
max |T_derived - T_dimension_stripped| = 0.000e+00
```

It is distinct from the provisional full-character branch.

The derived finite readout is therefore:

```text
P(rho_word) = 0.434215413259920
P(rho_strip derived internal-link convention) = 0.439904783618900
P(W38 full-character branch, unselected here) = 0.447034890458824
P_strip_derived - P_word = 0.005689370358980
rho_derived(1,0) = 0.573562917034962
rho_derived(1,1) = 0.204646875517536
```

This is a finite two-strip first-rung value under the derived internal-link
convention. It is not an analytic plaquette value, not a full spatial
environment computation, and not a repinning input.

## Named Residuals

- finite two-strip first rung only;
- finite dominant-weight box `B_4` only;
- finite Wilson Bessel mode support only;
- future all-link non-class `6j`/intertwiner basis normalization remains open;
- strip-depth direction remains open;
- wider slab limit remains open;
- stacking the slab to the physical `3D` environment remains open;
- `L_perp` remains open;
- analytic `P(6)` remains open;
- no repinning is supplied.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_internal_link_contraction_derived_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=32, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_internal_link_contraction_derived_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
