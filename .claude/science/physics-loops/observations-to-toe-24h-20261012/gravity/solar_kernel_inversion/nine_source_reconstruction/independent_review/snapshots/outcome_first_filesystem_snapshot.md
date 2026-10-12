# Nine-source reconstruction: fixed-family obstruction and readout sensitivity

Direct parent authorship, October 12, 2026. The two unchanged six-source
transfers were preserved as failures in commit94f791c83d before this new fit.
The new calculation asks whether the same finite response family can fit the
combined nine sources, rather than carrying two selected responses farther.
It does not erase their failure. All90 scored bins are now exposed fit data.

The six finite LPs need a common acceleration-rectangle relaxation of about
0.556. Exact rational certificates confirm a positive lower bound for their
saved matrices. Four selected weight vectors pass the declared direct-field
checks but still miss the observational rectangles; two fail refinement.
The strongest finite obstruction uses UGC07577, whose rotation-to-force
interpretation has a documented pressure-support limitation. The result is
conditional on that interpretation and the fixed reconstructed sources.

## Declared reconstruction and full outcome

The family is N(A)=1+sum_j w_j b_j(A), with the original twenty decreasing
logarithmic ramps, knots10^(-13+j/4) m/s², w_j>=0 and sum(w)<=100.
The M cases impose these conditions; the D cases additionally impose
D=N+A N'>=0 at each ramp's upper one-sided limit. D is not strictly positive.
The original nine source reconstructions, distances, inclinations, stellar
mass ratio0.5605122519882025, geometries and score masks remain unchanged.
Every source-only operator control passed. All six weight vectors were saved
before new actual fields were evaluated on base, refined and larger domains.

For source i let A_i=V_i²/R_i, L_i=max(0,V_i-2e_i)²/R_i and
H_i=(V_i+2e_i)²/R_i. The LP minimizes t>=0 subject to
L_i-t A_i <= g_N,i+K_i w <= H_i+t A_i. A second objective minimizes sum(w)
with t<=t_min+1e-8. This is a descriptive acceleration allowance, neither a
velocity percentage nor a statistical confidence or significance measure.

For external/solar cases, E=1.4915242022774435e-10 m/s² is held fixed.
The inherited spherical parent-field conversion, external rectangle and
solar quadrupole bound remain calibration assumptions. There is no scan or
optimality claim over E. Galaxy-only cases contain no E.

| Case | Numerical LP t minimum | All9 field gates | Refined RMS log10 V | Refined bins outside |
|---|---:|---|---:|---:|
| M, galaxies | .555684948125 | fail | .1330684560* | 55* |
| M, plus external | .555684948125 | fail | .1243961806* | 37* |
| M, plus external and solar | .555684948125 | pass | .1265205367 | 41 |
| D, galaxies | .557044667733 | pass | .1233296611 | 39 |
| D, plus external | .557044667733 | pass | .1247531268 | 40 |
| D, plus external and solar | .557044667733 | pass | .1228127712 | 38 |

*These are saved diagnostics only; failed field gates prevent a qualified
whole-candidate observational comparison. M galaxies fails refinement at
NGC2976 (.01046757146) and NGC3972 (.00580254376); M plus external fails at
NGC2976 (.00578512511). The threshold was .005. No boundary check failed.
The other four candidates pass positivity, refinement and boundary gates.
Such checks are sampled convergence evidence, not uniform continuum bounds.

The largest refined t is .555688618558641 for the passing M joint candidate
and .557047614759503 for all D candidates, at UGC06667. Actual fields retain
the difference between the LP's supplied Newtonian baseline and its finite
Poisson projection. It is not forced to zero. The similar primary t values
across solar/external cases coexist with different secondary optima and RMS
scores; none was selected as an observational success.

The joint solar values slightly exceed the bound within the LP tolerance:
M has Q2=5.2000000105550184e-27 s^-2; D has
5.200000001569074e-27 s^-2, versus5.2e-27. Their scaled excesses are about
2.03e-9 and3.02e-10. These are numerical calibration outputs, not exact
feasible solar certificates, and no new direct solar validation was performed.
The D solutions also touch D=0 within floating tolerance. They cannot inherit
the earlier strictly positive constrained-energy theorem. The M solutions have
negative D and do not meet that theorem either.

The original helper saved the first optimizer status and asserted success of
the second but omitted its explicit status/message, despite the protocol's
request. SOLVER_STATUS_REPLAY_v1.json records a separate, identified replay:
both stages succeed in all six cases, and every returned weight and t matches
the original bitwise. These are replay logs, not relabelled original logs.

## A finite-matrix certificate independent of optimizer tolerances

For the saved primary program min c.x with A.x<=b and x=(w,t)>=0,
c=(0,...,0,1). Interpret every frozen binary64 coefficient as an exact
rational number. Choose rational y<=0 with (A^T y)_t<=1, and put

    delta=max(0,max_j<20 (A^T y)_j),
    L=y.b-100 delta.

Every feasible point satisfies

    t = y.A.x + (c-A^T y).x >= y.b-100 delta = L.

The first inequality uses y<=0, the nonnegative residual t coefficient,
w>=0 and the explicit sum(w)<=100 cap. It remains valid when rounded
solver multipliers slightly violate a weight-column dual inequality.
Positive proposed multipliers are replaced by zero; downward rescaling
enforces the t inequality exactly. The recorded rational L is then rounded
down for decimal reporting. A separate standard-library verifier reads
only frozen matrices and rational certificates, with no optimizer import.

All six certificates pass. Safe decimal lower bounds are:

    M: t >= 0.555684948124
    D: t >= 0.557044667733.

This eliminates numerical optimizer tolerance as an explanation for a t=0
fit in these finite matrices. It does not certify their discretization error,
source reconstruction or physical readout. The galaxy-only certificates
contain neither external nor solar rows, so adding constraints on E or Q2
cannot remove this finite-matrix bound. Changing the galaxy field operator,
for example by introducing galaxy external fields, would change the matrix.

The M certificate uses only UGC07577 upper bounds at .94 and1.32 kpc,
UGC06667's lower bound at3.5 kpc and the weight cap. The D certificate uses
UGC07577's upper bound at .94 kpc, UGC06667's lower bound at2.61 kpc,
UGC08837's upper bound at2.09 kpc and seven D inequalities. Although its
weight-cap multiplier is zero, the rational correction still uses the cap.
These sparse constraints identify a concrete measurement conflict.

No uniform operator-error bound has been established. If a separately proved
perturbation bound kept x>=0 and sum(w)<=100 as unchanged independent
constraints, left the t column unchanged and gave |Delta A_ij|<=epsilon
for all weight columns and |Delta b_i|<=eta, the same argument would lower
L by at most (100 epsilon+eta) sum_i |y_i|. The cap is not relaxed by
perturbing the displayed matrix row. This states what a further
certification would require; it is not supplied by the sampled field gates.

## What pressure support would have to change

The parent reread [Swaters et al., Sections3.1.2 and3.5](https://arxiv.org/html/0901.4222v1).
The reduction used an8 km/s Gaussian dispersion in its model cubes and left
asymmetric-drift corrections unapplied. UGC7577 is named as an exception to
the generally small corrections. This establishes an unresolved readout
premise, not the correction needed here. See the earlier
agents/galaxy_response/qumond_disk/DIRECT_KINEMATIC_READOUT_FINDING.md for
the source and distance mapping and its limits.

Let p_i=v_c,i²-v_phi,i² shift both squared-speed rectangle endpoints by p_i,
while holding the original A_i, radius and field matrix fixed. This is a
new explicit readout-sensitivity premise, not a fitted correction. The same
certificate gives the exact affine necessary condition

    t >= L + sum_i (y_upper,i-y_lower,i) p_i/(R_i A_i).

The exact rational coefficients are saved in PRESSURE_SENSITIVITY_v1.json.
For illustration, suppose only UGC07577's pressure readout changes and every
other bound and source remains fixed. Then a t=0 solution would require:

- M: max(p(.94),p(1.32)) >= about794.247732 (km/s)²;
- D: p(.94) >= about1113.287328 (km/s)².

These are necessary conditions only. Even satisfying them does not prove
that any response fits all bins. Nonnegative support added at the active
UGC06667 lower-bound radius would increase the certificate obstruction.
Changing UGC08837 or other nuisance/source assumptions changes the scenario.

For the steady isotropic gas model with constant height and constant sigma,
p=-sigma² d ln Sigma/d ln R. At the illustrative sigma=8 km/s, the D
requirement corresponds to a logarithmic density slope of about17.395 at
.94 kpc. Using the tabulated central rotation value10.7 km/s would give
a central circular-speed illustration35.040 km/s. Neither value is an
observed slope or measured pressure correction. The gravitational ring
reconstruction has not been validated as a local gas-pressure tracer, so
its density derivative is not silently substituted for the missing evidence.
Actual density, dispersion, height, inclination and reduction information
are needed to evaluate this escape.

## Scope and next physical route

N1: quantified result is an exact lower bound for six specified finite
matrices, and four numerically qualified selected vectors fail the supplied
rectangles. A universal theory no-go is not the conclusion.
N2: source masses/geometry, response basis/cap, nonnegative weights,
kinematic identification and uncertainty rectangles are explicit premises.
N3: the actual exposed variants are M/D and the three declared constraint
sets, with full results retained; adding similar constraints is not invented
as five independent attacks. Broad exclusion work remains a partial attempt
with named untested routes.
N4: the dual proof and exact certificate supply the finite obstruction;
full continuum coefficient certification remains absent.
N5: pressure-aware readout, source reconstruction changes, nonmonotone or
different response bases, galaxy external fields and additional matter are
distinct untested escapes. None is declared sufficient or impossible.
N6: source protocols, frozen weight vectors, field receipts, exact matrices,
certificates and original failed transfers preserve chronology and recovery.
N7: focused independent checks cover arithmetic, construction and premise
scope; source-readiness checks do not assign an audit verdict.
N8: the next observed input should discriminate the pressure/source map or
a broader physical source model, instead of repeatedly retuning these weights.
There is no TOE, empirical confidence claim or viable dynamical completion.

The output identities and all original receipts are retained in evidence_v1/;
finite_lp_certificates_v1/ is a byte-preserved copy of the runtime certificates.
Independent findings and final source identities are kept in independent_review/.
