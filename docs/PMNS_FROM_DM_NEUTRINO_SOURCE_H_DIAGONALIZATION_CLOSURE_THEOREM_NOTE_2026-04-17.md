# PMNS map on a supplied affine Hermitian chart

**Date:** 2026-04-17; corrected 2026-10-21
**Type:** bounded_theorem — conditional matrix map and numerical fitted candidate
**Status authority:** independent audit lane only
**Primary runner:** `scripts/frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem.py`

## Scope and correction

The supplied Hermitian chart defines mixing observables wherever its spectrum
is nondegenerate and the angle denominators below are nonzero. A numerical fit
to three supplied mixing angles gives the candidate reported below. The
multistart search is not an exhaustive proof of uniqueness, and convergence of
`fsolve` does not prove a nonsingular Jacobian. Constant inertia on a path
avoiding zero eigenvalues does not identify a unique connected component or
select a physical branch.

The earlier global uniqueness, retained PMNS promotion and downstream closure
claims are withdrawn. The inverse-sine phase `279.12°` used the wrong quadrant;
the matrix gives `260.88°`. Original text is recoverable at Git commit
`f24d17d97d372df977476e4a69674577f31af575`, at this unchanged file path.
No audit verdict is assigned by this correction.

## Supplied inputs

The calculation uses the affine chart from
[the affine point-selection boundary](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
and the chamber from
[the active half-plane construction](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md).
It separately supplies the charged-lepton eigenbasis `U_e=I` and hierarchy row
pairing `sigma_hier=(2,1,0)`. The
[charged-lepton basis construction](CHARGED_LEPTON_UE_IDENTITY_VIA_Z3_TRICHOTOMY_NOTE_2026-04-17.md)
and [Higgs-charge gauge comparison](HIGGS_Z3_CHARGE_PMNS_GAUGE_REDUNDANCY_THEOREM_NOTE_2026-04-17.md)
are provenance for those modeling choices, not independent certification here.
Physical selection of the baseline branch and the row pairing remains open.

The supplied chart is

```text
H = H_base + m T_m + delta T_delta + q_+ T_q,
H_base = [[0,E1,-E1-i gamma], [E1,0,-E2], [-E1+i gamma,-E2,0]],
T_m = [[1,0,0], [0,0,1], [0,1,0]],
T_delta = [[0,-1,1], [-1,1,0], [1,0,-1]],
T_q = [[0,1,1], [1,0,1], [1,1,0]],
gamma=1/2, E1=sqrt(8/3), E2=sqrt(8)/3,
q_+ >= sqrt(8/3)-delta.
```

All three parameters are real. The matrices are Hermitian. This establishes
Hermiticity of the chart, not its physical selection from the framework axioms.

## Conditional observable map

Let `U_nu` have orthonormal eigenvectors of `H` as columns, sorted by ascending
eigenvalue, and set `U=P_sigma U_nu` for the supplied row permutation.
Nondegeneracy makes the eigenvectors unique up to phases; the following
observables are invariant under row and column rephasing:

```text
s13² = |U_e3|²,
s12² = |U_e2|² / (1-s13²),
s23² = |U_mu3|² / (1-s13²),
J = Im(U_e1 U_e2* U_mu1* U_mu2),
sin(delta_CP) = J / (c12 s12 c23 s23 c13² s13),
cos(delta_CP) = (|U_mu1|²-s12² c23²-c12² s23² s13²)
               / (2 s12 c12 s23 c23 s13),
delta_CP = atan2(sin(delta_CP),cos(delta_CP)) mod 2pi.
```

At zero angle factors the CP phase is undefined by these formulas; at repeated
eigenvalues an arbitrary eigenspace basis need not give unique mixing angles.
No globally smooth map across such singularities is asserted.

## Numerical fitted candidate

The historical comparison inputs are

```text
s12²=0.307, s13²=0.0218, s23²=0.545.
```

The finite search and local refinement return

```text
m=0.657061342210, delta=0.933806343759, q_+=0.715042329587,
sin(delta_CP)=-0.9874, cos(delta_CP)=-0.15849,
delta_CP=260.88 degrees, |J| approximately 0.0328.
```

The chamber margin is approximately `0.0159`. The three angles are fitted
inputs, not predictions. The phase is a consequence of this supplied chart,
row pairing and fitted point. A phase disagreement would reject this candidate
under these premises, not every possible branch of the construction.

The search reports one rounded accepted candidate among its finite starts.
It does not establish that every start succeeds, that all stationary points
have been enumerated, or that this candidate is globally unique. Other sampled
basins in the earlier analysis and the
[perturbative uniqueness discussion](DM_NEUTRINO_SOURCE_SURFACE_PERTURBATIVE_UNIQUENESS_THEOREM_NOTE_2026-04-17.md)
remain historical comparisons, not an exhaustive certificate.

The runner compares nine matrix moduli with its supplied historical NuFit 5.3
normal-ordering intervals. Passing that comparison is not a current global
experimental likelihood or an independent fit of nine observables. No current
experimental confidence level for the phase or Jarlskog invariant is claimed.

## Validation and limits

The primary runner reports `PASS=43, FAIL=0` on the repaired source. The original PR phase regression checked both invariants in all four
quadrants, rephasing invariance, complex conjugation and the independent
modulus identity. Its inverse-sine implementation fails the quadrant controls.
That broader regression is historical evidence recoverable at commit
`3c90f9860c3bae63ee64949e7178290f789dd982`, path
`scripts/pmns_scoped_repair_regression_2026_10_21.py`; it is not a landed
dependency of this scoped fit repair.

The numerical checks also cover Hermiticity, sampled chamber variation,
fixed-slot comparisons and separation from the five supplied candidate points.
Those finite checks do not prove physical branch selection, global fitting
uniqueness, a solar mass splitting, an absolute mass scale, or Majorana phases.
Downstream calculations may use the fitted candidate with these same supplied
premises; this note does not promote it to a retained PMNS input or close the
DM selector gate.

```bash
PYTHONPATH=scripts python3 scripts/frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem.py
```

## Execution receipt and recovery

The current cache is `logs/runner-cache/frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem.txt`.
It records the corrected runner with a 30-second cap, not the old execution.
The original note, runner and cache are recoverable at
`f24d17d97d372df977476e4a69674577f31af575` under their unchanged paths;
the intermediate PR versions are at
`3c90f9860c3bae63ee64949e7178290f789dd982`. No audit status is assigned.
