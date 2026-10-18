# A native ultrasoft charged mode of large column features

**Status:** bounded-support.
**Primary runner:** [scripts/native_row_tunneling.py](../scripts/native_row_tunneling.py)

The original one-qubit Hamiltonian produces an ultrasoft finite-array mode
and its local-spin coupling without an added interaction. It is symmetry-
charged, however, and the neutral scalar diagnostic cannot excite it.
This advances native collective dynamics while leaving the scalar bridge open.

## Deriving the scale instead of assigning it

Fix an even M by M transverse torus, M>=4, and open columns of even height
L>=6. Let Jx=Jy=lambda Jz>0 and take lambda to zero at fixed dimensions.
This is a different geometry and limit from the growing periodic cubes used
in the [neutral response bound](NATIVE_STATIC_NEUTRAL_RESPONSE_NOTE_2026-10-18.md).

Two previously derived native processes supply the ingredients:

- The [plaquette interaction](NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md)
  has K=(L+14)Jz lambda^4/128 and favors signs s_xy=a_x b_y.
- [Pair-column tunneling](NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md)
  has t=Jz lambda^L/2^(L-1).

A pair flip does **not** move within the plaquette-positive manifold on a
large transverse grid: it creates plaquette defects. The direct compression
of that pair operator is zero. This rules out simply relabeling its scale as
the ground-band splitting.

Instead, n=M/2 pair events cover an entire row or column. There are two
minimal perfect matchings. An intermediate matching subset with r runs
costs 8Kr. Summing every ordering gives the first nonconstant ground operator

    H_ground = scalar - tau_M (sum_x R_x + sum_y C_y) + o(tau_M),
    tau_M = 2 binom(2n-2,n-1) t^n/(8K)^(n-1).

The [root proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/HIERARCHICAL_ROW_TUNNELING_PROOF.md)
uses two exact finite-dimensional analytic reductions, not just a truncated
column model. Native spin-flip counting bounds each aligned-block event;
small plaquette denominators are then accounted for explicitly. Grouping
events or inserting extra events is higher order. Folded terms cannot change
the first nonconstant transition. The independent [native hierarchy check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_HIERARCHICAL_NATIVE.md)
records those controls.

Row and column flips commute and their total product is identity. Their
all-plus character is the unique leading ground state; the first allowed
excitation flips two signs and costs 4tau_M. For sufficiently small lambda
at the fixed dimensions, this gives the native gap 4tau_M+o(tau_M).
For M=4,L=6,

    tau_M = Jz lambda^8/320,
    gap = Jz lambda^8/80 + o(Jz lambda^8).

The native word uses at least twelve transverse bonds, but the intervening
plaquette denominator removes four powers of lambda. A bare word count is
not a bound on the resummed splitting exponent.

## A derived coupling, with a decisive selection rule

A local physical Z_xyz becomes the column sign a_x b_y in the aligned
manifold. It toggles one row and one column character with matrix element
one. Its native spectral weight at the corresponding low line therefore
tends to one as lambda tends to zero. This follows from the same microscopic
operator; no adjustable scalar source constant has been supplied.

But Z is charged under the x and y plane symmetries. In a symmetry-invariant
state its translated correlations vanish unless the two probes lie on the
same vertical column. The neutral distance-two diagnostic Z_r Z_(r+2ez)
preserves every character and is intraband inelastic-dark. A soft charged
line is not a neutral three-dimensional scalar mediator.

The [charge proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/PLANE_CHARGE_MOBILITY_PROOF.md)
and [independent check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_CHARGE_MOBILITY.md)
give a more general restriction. A bounded Pauli template with nonempty
plane-charge patterns can correlate with its translate only along directions
that preserve those patterns. Single X, Y and Z templates allow their
respective axes; some dipoles allow a plane. This is a kinematic allowance,
not a guarantee of propagation. Neutral templates, symmetry-breaking states,
changed templates and nonlocal dressings need separate analysis.
Compass subsystem symmetry and dimensional reduction are established prior
structure; see [Nussinov and Fradkin](https://arxiv.org/abs/cond-mat/0410720).
The present contribution is the checked finite-array hierarchy and source
interpretation, not the invention of those symmetries.

## Checks and remaining assumptions

The [matching check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ROW_TUNNELING.md)
proves the all-n coefficient. The runner verifies exact rational path sums
through n=14 and diagonalizes the 16-column coefficient model in two
512-dimensional character sectors. As t/K decreases from .1 to .005, its
gap divided by 2t^2/K approaches one (1.05345 to 1.00013), while the Z
weight approaches one (.997423 to .999994). Residuals are below 7e-13.
These are development controls, not diagonalization of 96 physical qubits.

The native result is asymptotic at fixed finite dimensions. It supplies no
uniform threshold as features grow, no isotropic continuum, and no physical
unit or cosmological identification. The Hamiltonian, anisotropy, geometry,
ground-state problem and measurement interpretation remain premises. No
observation is fitted or independently tested. The large-feature scalar and
measured-gravity connection remains open.
