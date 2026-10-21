# Finite PMNS Basin Searches with an Imposed Inertia Filter

**Date:** 2026-04-17; scope correction 2026-10-21

**Type:** open_gate
**Status:** conditional finite diagnostics; no global basin-uniqueness theorem or physical selector is established.

**Primary runner:** `scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py`

## Supplied finite construction

Let `gamma=1/2`, `e1=sqrt(8/3)`, `e2=sqrt(8)/3`, and supply

```text
D = [[0,e1,-e1-i/2], [e1,0,-e2], [-e1+i/2,-e2,0]]
Tm = [[1,0,0], [0,0,1], [0,1,0]]
Td = [[0,-1,1], [-1,1,0], [1,0,-1]]
Tq = [[0,1,1], [1,0,1], [1,1,0]]
J(m,d,q)=m Tm+d Td+q Tq, H=D+J.
```

The imposed chamber is `d+q>=e1`. Order the eigenvalues of `H` increasingly,
choose an orthonormal eigenbasis, and permute its rows by `sigma`. The runner
uses the resulting matrix `P` to compute

```text
s13^2=|P[0,2]|^2
s12^2=|P[0,1]|^2/(1-s13^2)
s23^2=|P[1,2]|^2/(1-s13^2).
```

It extracts `sin(delta_CP)` from a Jarlskog-type imaginary product divided by
the usual angle factors, with numerical clipping. It does not determine the
full phase quadrant from that sine alone. Targets `(0.307,0.0218,0.545)` are
supplied historical comparison values; no current experimental fit or
covariance is claimed. The objective called `chi2` is an unweighted sum of
three squared residuals, not a statistically calibrated chi-squared.

These matrix, chamber, readout and target choices are assumptions. Source
context is the [affine point-selection note](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md),
[half-plane note](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md),
and [PMNS closure note](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md).
Their labels do not establish independent audit authority for this diagnostic.

## Inertia, connectedness and norm cuts

For this baseline, `det D=32 sqrt(2)/9>0`, `Tr(D^dagger D)=233/18`, and its
inertia is `(2,0,1)` in negative/zero/positive order. Positive determinant
and zero trace imply two negative and one positive eigenvalue here; positive
determinant alone does not fix inertia for a general Hermitian matrix.
For example, `I3` and `diag(-1,-1,1)` both have positive determinant and
different inertia.

The implemented filter requires `inertia(H)=inertia(D)` (and redundantly
`det H>0`). It is imposed, not derived as a physical admissibility rule.
Inertia is constant on every nonsingular continuous path. In the full space
of Hermitian matrices, each fixed-inertia set is connected, but intersection
with a restricted affine surface need not be. For example, the affine line
`diag(x,-x,1)` has the same inertia at `x=1` and `x=-1`, while every path
within that line between them crosses the singular matrix at `x=0`.
Thus this runner's inertia comparison does not certify a path from `J=0`
to a fitted point within the supplied three-parameter surface.

The scale diagnostics compare `||J||F` and `||J||op` against the corresponding
baseline norms. The exact Frobenius Gram matrix of `(Tm,Td,Tq)` is

```text
[[3,0,2],[0,6,0],[2,0,6]],
||J||F^2=3m^2+6d^2+6q^2+4mq.
```

The old diagonal ellipsoid comments were incorrect. The optimizer already
uses the actual matrix norm, so this correction does not alter its cuts.

For invertible `D`, `rho(D^-1 J)<1` suffices for the matrix-log Taylor series
at source amplitude one. The real scalar difference
`log|det(D+J)|-log|det D|` remains defined whenever `D+J` is nonsingular,
even outside that Taylor domain. Norm-ratio cuts are neither necessary nor
sufficient for convergence: with `D=diag(1/100,1)`, `J=diag(1/50,0)`, the
source norm is smaller but `rho(D^-1 J)=2`; with `D=diag(1,-1)` and
`J=10*ones(2)`, the source norm is larger but `(D^-1 J)^2=0` and the series
terminates. These examples refute the original necessary-scale claim.

## What the search can establish

Part 2 uses 60 starts per permutation across all six row permutations.
The initial box is `[-5,10]^3`; Nelder-Mead iterates are not constrained to
stay in that box. Accepted points satisfy the chamber tolerance and residual
sum below `1e-8`, and are clustered by Euclidean distance below `0.5`.
A numerical cluster representative is not an exact root or an isolated-basin
certificate. Part 3 compares the inertia and scale diagnostics of the found
clusters. Part 4 locally refines three supplied seeds, approximately
`(0.657061,0.933806,0.715042)`, `(28,20.7,5)`, `(21,12.68,2.089)`;
convergence flags and residuals must be considered before treating an output
as a solution. The original predicates do not certify all of those conditions.
The old note's incompatible eigenvalue and norm tables are withdrawn rather
than treated as verified data.

Part 5 probes four supplied `s23^2` values and bisects a finite-search success
indicator between `0.540` and `0.545`. Failed searches do not establish
nonexistence; no monotonicity or global exclusion theorem is proved.
Accordingly its roughly `0.541` transition is a numerical search observation,
not a certified threshold, rigorous error interval, or physical lower-octant
exclusion. Part 8 repeats a norm-cut search using 120 starts per permutation.
It cannot exclude solutions missed by those starts or merged by clustering.

Part 6 exactly enumerates the finite neutrality rule
`qL[i]+qH+qR[j]=0 mod3` for supplied charges `qL=(0,1,-1)`, `qR=(0,-1,1)`.
It yields diagonal, forward-cycle and backward-cycle support for `qH=0,+1,-1`.
Given a diagonal Yukawa matrix, `Ye Ye^dagger` is diagonal and a left basis
without mixing can be chosen (with phase, ordering and degeneracy freedoms).
The sampled diagonal example is not a derivation of physical charges,
nondegenerate masses, or equivalence of full theories under relabeling.
See the [support trichotomy](NEUTRINO_DIRAC_Z3_SUPPORT_TRICHOTOMY_NOTE.md)
for the conditional construction; no missing physical bridge is closed here.

Part 7 numerically estimates a `4x3` Jacobian of the three angles and
`sin(delta_CP)` at one refined point. Rank three there is local numerical
evidence. It does not establish a global embedded manifold or global
injectivity. If an exact smooth eigenvector branch has a nonsingular
three-angle Jacobian, the inverse-function theorem gives local angle
coordinates and a local fourth readout. The finite-difference test does not
prove those hypotheses with certified bounds.

## Reproduction and recovery

```bash
python3 scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py
```

Use the declared 1800-second cap and preserve stdout, stderr, exit status and
source identity. The old note inconsistently advertised both 43 and 46 passes.
The unmodified f24 runner was actually executed on 2026-10-21 with the
1800-second cap: `PASS = 46`, `FAIL = 0`, exit status0, approximately646seconds.
Its source identity remained unchanged. This resolves the historical count
discrepancy in favor of46 for that execution, not the scientific scope claims.
The corrected runner must report its own actual outcome, including any failure
or timeout. The corrected runner preserves every numerical predicate,
threshold, start budget and seed; output and comments are narrowed to what
those computations establish. An all-PASS run would still not prove global
uniqueness, a physical selector, or a retained scientific result.

Original source and claims are recoverable at main revision
`f24d17d97d372df977476e4a69674577f31af575`. No earlier failure is erased.
Open work includes rigorous root/exhaustion bounds, restricted-surface path
certificates, physical selection premises, uncertainty propagation, and
independent audit. This note does not close the DM flagship, absolute neutrino
mass scale, Majorana phases, or effective Yukawa normalization.
