# Calibrated force signals and a conditional scalar branch bound

Status: conditional support; observational bridge premises remain explicit.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_calibration_branch_check.py`.

A common laboratory calibration removes a truly long-range scalar enhancement
from the normalized torque ratio. Light propagation compared with matter dynamics
can distinguish that enhancement. The exact negative-field branch inequality below
then bounds what density-driven changes could accomplish, provided the Solar
matching, range and error assumptions actually hold. These statements establish
requirements for a measured comparison; they do not replace its likelihood or
environmental boundary problem.

Premises are the [complete supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[local force/light normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md),
and [environment branch definitions](EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md).
The publications below are exposed development context. No observational sample is
reserved or reused as an independent test, and no measured parameter is fitted.

## Reconstructing the calibrated laboratory signal before importing a force limit

Personally derived by /root. This is a conditional forward-model result, not a new laboratory exclusion or a fit to measured torques. It is motivated by the calibration and nuisance treatment in Lee et al., Phys. Rev. Lett. 124,101101 (2020), https://arxiv.org/abs/2002.11761. The primary PDF is preserved; the unavailable numerical supplement has not been acquired.

### Observational input and exposure

The paper reports torsion torques at 52 micrometres to 3 mm, calibrated with separate macroscopic spheres. It fits geometry and calibration nuisance parameters and reports a 95% single-Yukawa gravitational-strength range limit of 38.6 micrometres. This does not directly give the limit for the present q<1/3 candidate. We use these published statements to determine the required forward operator, not to claim an independent replication of its likelihood. These statements are now exposed development context. No measured torque table or covariance is used below.

### 1. A common local Yukawa model and the instrument calibration

Assume an unscreened linear scalar with constant physical range lambda=1/mu, positive weight q and a single frozen background shared by calibration and science configurations. Take rigid density distributions, a weak quasistatic metric, pressure-negligible rest sources, and a linear torque readout. These are strong bridge premises, not consequences of the current environmental stationary family.

For a given geometry j and measured harmonic define Newtonian and Yukawa unit-G torque functionals N_j and Y_j(mu), computed from the complete mass geometry and the SAME demodulation functional. The energy kernels are 1/r and exp(-mu r)/r. Both functionals can have signs and cancellations. Suppose N_j and N_c are nonzero, where c denotes the calibration configuration, and put y_j=Y_j/N_j. The actual torques are

    tau_j=Gbare [N_j+q Y_j],
    tau_c=Gbare [N_c+q Y_c].                         (1)

If an instrumental multiplicative gain is calibrated by the Newtonian expectation for c, its same-gain normalized science prediction is

    R_j=(tau_j/N_j)/(tau_c/N_c)
       =(1+q y_j)/(1+q y_c),                        (2)

provided 1+q y_c is nonzero. Thus an exact measured R_j and known geometry/range would yield

    q=(R_j-1)/(y_j-R_j y_c),                        (3)

when the denominator is nonzero. When y_j=y_c, the normalized ratio is 1 for every q; a calibrated ratio does not then identify q. Noise, correlations and nuisance parameters are not removed by this algebra.

The standard short-range approximation y_c~0 permits R_j~1+q y_j. It must be justified at the calibration geometry, not assumed for every mu. If backgrounds differ, the ratio instead carries Gbare,j/Gbare,c and separate q_j,q_c,mu_j,mu_c. An environmental screening boundary problem cannot be replaced by (2) without proving the common-background approximation.

### 2. The massless calibration degeneracy and its leading correction

At mu=0 the Yukawa and Newtonian kernels coincide, so y_j=y_c=1 and R_j=1 exactly, even for finite q. Gbare(1+q) is then the common force normalization. This is a laboratory torque degeneracy, not equivalence to general relativity: lensing, relativistic bodies, time dependence or independent background information can distinguish the models.

For compact rigid bodies with a positive minimum separation and a fixed bounded linear torque/harmonic functional, the uniform kernel expansion is

    exp(-mu r)/r = 1/r - mu + mu^2 r/2 - mu^3 r^2/6 + O(mu^4).

The constant -mu times the product of total masses has zero orientation derivative, so it produces no torque. Let L_j be the ratio of the torque functional applied to r to that applied to 1/r. Then

    y_j = 1+mu^2 L_j/2+O(mu^3),
    R_j = 1+[q/(1+q)] mu^2 (L_j-L_c)/2+O(mu^3).      (4)

There is no universal positive sign or universal length for L_j in a signed torque geometry. The leading calibration-subtracted signal is quadratic in inverse range. The remainder is uniform on each fixed compact geometry with N_j,N_c bounded away from zero; it is not uniform near a Newtonian torque null or as geometry parameters diverge. Equation(4) does not justify extrapolating a published finite-range confidence contour to arbitrarily large lambda.

### 3. A direct geometric control, not the experiment

For two rings of n identical point masses at radii R and r, plane separation z, and relative angle theta, use all n^2 distances

    d_ij^2=R^2+r^2+z^2-2Rr cos(theta+2pi(j-i)/n).

After removing the common G m M, the torque is

    N(theta)=-sum_ij Rr sin(Delta_ij)/d_ij^3,
    Y(theta,mu)=-sum_ij Rr sin(Delta_ij)
                         (1+mu d_ij) exp(-mu d_ij)/d_ij^3.   (5)

Use the coefficient (1/pi) integral_0^(2pi) torque sin(n theta)dtheta. The corresponding r-kernel torque is +sum Rr sin(Delta)/d. Direct differentiation of the potential, periodic quadrature, and the massless/long-range limits independently check (5).

The calibration illustration uses the paper's reported radii R=0.1905 m and r=0.01648 m and n=3, but ASSUMES z=0 and ideal point masses. The science illustration instead uses n=3,R=0.001 m,r=0.0005 m,z=0.00007 m. It is not the paper's 18/120-fold wedge apparatus. No result from these toy geometries is a numerical reinterpretation of that experiment or its bounds. The prescribed synthetic q=0.2 does not estimate the theory's coupling.

### 4. Frozen checks and limits

Freeze q=0.2, the two toy geometries above, and inverse ranges mu={0,0.01,0.1,1,10,100,1000,10000,100000} per metre. Independently integrate each actual torque harmonic and its r-kernel coefficient. Check exact ratio inversion, massless nonidentification, leading mu^2 coefficient, point-force derivative and actual changed-code controls. Save every result and any numerical cancellation failure before repairs. No observational significance threshold is selected or fitted. A measured-theory comparison still needs the actual geometry, torque data/covariance, nuisance likelihood and environmental solution.

## Negative-branch coupling floor and a conditional light-time benchmark

Personally derived by /root. Complete candidate action and the existing weak-source/environment derivations remain premises. This is a new exact branch inequality plus a transparent comparison with an exposed published parameter estimate. It is not a reconstructed Cassini likelihood, a derived Solar environmental solution, or a global exclusion of the scalar theory.

### 1. The observation fixes what a bridge must deliver

Bertotti, Iess and Tortora (Nature425,374-376,2003; DOI10.1038/nature01997) report gamma-1=(2.1+/-2.3) times10^-5. The primary publisher's indexed abstract supplies this value; the full article/likelihood was not acquired in this block. We use the explicit central-value plus/minus two reported-error interval [-2.5,6.7] times10^-5 as a compatibility benchmark. We do not equate that construction to a new confidence analysis or independent empirical test. This observation is now exposed development information.

The frozen weak, unscreened, long-range source calculation already gives

    gamma_model-1=-2q/(1+q), q=|d ln A|_K^2.             (1)

Its application to light time requires the same weak potential normalization from matter dynamics and photons, negligible scalar mass/mixing over the relevant Solar-System distances, negligible background evolution and source pressure/strong-field corrections, and a correctly matched ambient field. An actual solar solution was not derived. Introduce a separately established absolute bridge-error bound epsilon_gamma>=0:

    gamma_prediction-1=-2q/(1+q)+delta_gamma,
    |delta_gamma|<=epsilon_gamma.                        (2)

If the predicted value is to intersect an observed interval with lower endpoint L, a necessary condition is

    2q/(1+q)<=epsilon_gamma-L=:eta.

For 0<=eta<2 this gives q<=eta/(2-eta). If eta<0, no nonnegative q works; if eta>=2 this inequality supplies no finite bound. Unknown bridge error does not yield a bound. We do not absorb an arbitrarily large correction into a claim that the weak approximation worked.

### 2. Exact coupling on the already studied branch

For 0<k<1/3, define a=(1-k)(1+3k)/4 and s=(1+k)/[k(1-3k)]. On the negative-u branch z=A in(0,1], let D=1+s-s z^2. The supplied field metric gives

    q(z)=a D/[1+s-3a s z^2].                             (3)

The denominator is positive. Direct differentiation gives

    dq/dz=2a s(1+s)(3a-1)z/[1+s-3a s z^2]^2<0,
    q(1)=k, lim_(z->0)q(z)=a,
    a-k=(1-3k)(1+k)/4>0.                                (4)

Thus k<=q<a on this branch, with the left equality only at z=1. This is independent of nu and of the prescribed density value. Moving to denser negative-u stationary configurations cannot suppress the local coupling norm below its vacuum value. It can change the range and the body's nonlinear scalar charge; neither is determined by this norm statement. We do not assert (4) for positive u or for every possible stationary branch.

Solving(3) yields the exact conformal change

    1-A^2=(1-3k)(q-k)/[(1+k)(1-3q)].                      (5)

For any supplied bound k<=q<=qmax<1/3,

    0<=1-A^2<=(1-3k)(qmax-k)/[(1+k)(1-3qmax)]
              <=qmax/(1-3qmax).                         (6)

At fixed Q, Gbare/Gvac=A^2, where Gvac=1/(8piQ) is a theoretical reference, not an independently measured cosmic G. A controlled light long-range Solar matching to this branch therefore also bounds the local-to-reference conformal change. It does not calibrate Gvac or select a physical cosmology.

### 3. Transparent conditional numbers and failures

With epsilon_gamma=0 and the stated benchmark lower endpoint, eta=2.5e-5 and qmax=eta/(2-eta)=1/79999, approximately1.2500156e-5. Necessarily k<=qmax. The k-independent conformal ceiling is1/79996, approximately1.2500625e-5. These are conditional benchmark transformations, not newly fitted parameter posteriors.

Freeze additional bridge-error examples epsilon_gamma=1e-5 and1e-4 to show how the bound depends on the error premise. Also freeze synthetic couplings k=1e-6,1e-5,0.01,0.1,0.3 and z=1,0.9,0.5,0.01 for exact branch tests. These choices are exposed model-development inputs. No value is selected by the data here.

For a trial q, the smallest bridge-error allowance that can reach the lower observation edge is max(0,L+2q/(1+q)). Moderate q therefore cannot be reconciled by a small unspecified correction within this long-range weak-source class. Finite range, nonlinear source screening, positive-u matching or a different action must instead be explicitly solved and tested if used; their names are not derivations or automatic loopholes. A theory with sufficiently small k is not ruled out by this conditional argument, and no state-preparation or vacuum-energy assumption is eliminated.

### 4. Frozen checks

Check all branch identities, denominator and derivative signs, exact inverse relation, endpoint restrictions and numeric interval transformation. Use independent substitutions in original E=e^(2sqrt(a)u) coordinates, negative/positive-u counterexamples to overbroad claims, and actual altered-program controls for the coupling denominator, gamma coefficient and bound sign. Preserve full computations, sources, failures and source versions. Do not rerun or rewrite older sealed units.

## Source access, validation and surviving assumptions

The preserved public Nature HTML was subsequently inspected: its abstract confirms
the quoted gamma value and explicitly labels the rest a subscription preview.
Thus the source now includes direct public-abstract access, beyond the earlier
indexed-abstract check recorded in the original hand derivation. The full article
and likelihood were not acquired. The Lee primary PDF was read; actual torque
data, covariance and its numerical supplement were not acquired. No subscription,
credit purchase or access-control workaround was used.

The light-time inequality uses the lower interval edge as a necessary condition.
For a general interval, the upper edge supplies a separate intersection condition;
the chosen positive upper edge makes that additional condition automatic for
q>=0 and a symmetric nonnegative bridge-error allowance. An unbounded or unknown
bridge error supplies no useful coupling bound. Gvac is a theoretical bare
reference, distinct from the force normalization Gbare(1+q).

The canonical runner preserves the checked original proof bodies with function
renaming and an output wrapper. It executes40 calibration controls and134 branch
controls. The original laboratory39/1 failure arose from subtracting a synthetic
ratio from1 at a signal around4.16e-23; increasing arithmetic from50 to75 digits
resolved it with the same cases and acceptance threshold. The first failure,
repair diff, original programs, full outputs, actual damaged programs, primary
sources and the synthetic geometry plot remain in the
[recovery archive](work_history/physics/revised-scalar-calibration-branch-20261014/README.txt).

An independent geometric route uses potential Fourier coefficients, full pair
forces and signed near-null examples; its79 controls and five actual damages
support the conditional calibration algebra. Independent branch checks are
preserved separately and challenge the original-coordinate contraction, endpoints,
conformal inverse and error-budget transformation. These are mathematical controls,
not extra observations or a formal audit grade.

The negative-u coupling floor does not constrain positive-u backgrounds, nonlinear
body charges or scalar ranges. The common-background and same-gain laboratory
assumptions, real apparatus geometry and nuisance likelihood, actual Solar
matching and approximation error, initial state, supplied action and scales all
remain separate tasks. No theory-wide observational exclusion is asserted.
