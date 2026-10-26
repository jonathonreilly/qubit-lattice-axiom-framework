# Finite Newtonian Hartree diagnostics

**Type:** open_gate
**Status:** open; finite numerical diagnostics with unresolved convergence.
**Primary runner:** `scripts/frontier_frozen_stars_rigorous.py`

The supplied open-boundary hopping Hamiltonian and regularized Newtonian
self-potential define an exploratory single-particle Hartree iteration. Filling
its lowest orbitals is a model choice. It is not a relativistic stellar model.
A nonzero RMS width is not a fixed-point, dynamical-stability or horizon test.

## Model and finite domains

Hopping t=1; the self-potential uses distance max(r,1). Initial potential is
zero and each iteration mixes the new potential with the old. The 1D solver
defaults to 100 iterations, damping 0.5 and tolerance 1e-7. Probe 2 uses
N=100,200,500,1000, 20 occupied orbitals, G=1, 150 iterations, tolerance 1e-8;
it also samples G=3 at N=100,200,500. Its G=2 particle scan uses even counts
2 through 78, 120 iterations and a width cutoff 2.5. Absence of a crossing is
right-censoring above 78, not a missing value to discard.

The 3D solver uses sparse low eigenpairs with five extra eigenvectors. Probe 3
uses L=6,8,10,12, eight occupied orbitals, G=0.5, 40 iterations, damping 0.4,
tolerance 1e-4; L=14 uses 25 iterations and tolerance 1e-3. Its width cutoff
is 1.5. Probe 4 uses N=500, G in {0.3,0.5,1,2,3,5}, particle counts
{4,8,16,24,32,40,50}, 120 iterations and defaults otherwise. Its comparison
radius 1/(G n) and scale 2 G n are supplied diagnostic formulas. Their ratio
scales as (G n)^-2. A fit on a threshold-selected subset is not a law.

## Historical evidence and failed inferences

[Exact original source and output manifest](work_history/PR9839_original_recovery/manifest.json)
preserves the original PR head f78abbde6e5003b71d91cd31394c6f850234b8bc,
including its canonical output and original note. These compressed files are
historical evidence, not a fresh execution of this repaired runner. The prior
experiment took about 494 seconds. It has not been repeated during this repair;
the stale live cache was removed. Fresh solver execution remains pending.

The original G=1 1D table reports width about 6.8170 at all four sizes, but all
four self-consistency convergence flags are false. Agreement of those widths
cannot establish a self-consistent solution. The particle-threshold scan reports
6, 8, and >78 for N=100,200,500 respectively. The last point is censored and
must remain in the comparison. Dropping it produced the invalid independence
claim. The original 3D widths grow with L (about 2.52,3.21,3.86,4.49,5.08);
no infinite-volume width limit is demonstrated. Original cutoff labels STABLE
and COLLAPSED only classified widths; the repaired runner names them
ABOVE_WIDTH_CUT and BELOW_WIDTH_CUT, retaining convergence separately.

## Supplied scaling and withdrawn echo route

For E(R)=C_k N^(5/3)/R^2-C_g N^2/R with positive coefficients, differentiation
gives the stationary radius 2 C_k/(C_g N^(1/3)). This algebra does not establish
a relativistic equilibrium. The separate packing estimate a N^(1/3) assumes
one occupied site per particle. The runner supplies SI constants and a Planck
spacing for comparison, not a derivation of those constants or stellar physics.

A positive packing floor implies neither horizon exclusion nor nonsingular
curvature. The original echo construction crossed the Schwarzschild coordinate
singularity without a valid exterior-to-interior metric and causal matching.
Proper time along a null geodesic is zero; it cannot supply an observable round
trip delay. Changing coordinates to Eddington–Finkelstein does not remove an
event horizon. The unconditional GW150914 echo, frequency and detectability
claims are withdrawn. Their exact original code/output remain recoverable in
the archive; they are removed from the active runner. Relativistic dynamics,
boundary conditions, causal escape and a detector observable remain open.

## Repair record

PR9839 independent feedback motivated this author narrowing. No independent
approval or audit verdict is asserted here. Source-only packaging and cheap
reporting controls do not certify the pending numerical replay or any physical
claim. The original entropy and finite-algebra repairs elsewhere are unaffected.
