# Scalar initial-state covariance: reconstructibility without selection

Status: conditional support; local covariance feasibility, not a selected cosmic state.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_state_covariance_check.py`.

This construction removes a chosen initial covariance from an ideal linear
feasibility problem. Its exact support condition tells which signal covariances
a specified transfer can reproduce. At one allowed event of the supplied scalar
theory, a three-readout inverse permits every sufficiently small positive
semidefinite output covariance. A bounded homogeneous, isotropic ensemble
realizes the real symmetric covariance freedom. These symmetries therefore do not select the realized
state within this local example.

The [complete supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md)
is a premise. The candidate constraint and readout definitions are written
explicitly below. Prior checked kinetic and observable context is preserved in
the [recovery evidence](work_history/physics/revised-scalar-state-covariance-20261014/README.txt),
including the exact source snapshots identified in the proof. No new claim about
a survey likelihood, complete history, arbitrary fixed observed amplitude or
unique state is made. Source corrections and failed checkers remain recoverable.

## 1. Exact covariance feasibility and candidate right inverse

Direct author /root, conditional-support, 2026-10-14. The observed E_G example
and its actual projected-estimator limitations are recorded in
the recovered source `rolling_local_response/covariance_inverse_v1/independent_v1/sources/OBSERVABLE_DERIVATION_v2.md`. Here I ask what even an ideal complete
matched covariance could determine. No new observed covariance, raw likelihood,
calibrated parameter fit or held-out empirical test is available in this block.

### Eliminate covariance as a nuisance without selecting it

For a specified background, parameters, mode, observation operator and interval,
let centered linear initial amplitudes X in C^n give readouts Y=T X in C^m.
Let P=E[XX^dagger]>=0 be finite and otherwise unrestricted. Then the exact
centered readout covariance is S=T P T^dagger. With T^+ the Moore-Penrose
inverse and Pi=T T^+ the orthogonal projector onto range(T),

    there exists P>=0 with S=T P T^dagger
    iff S=S^dagger>=0 and (I-Pi)S=0.                    (1)

Necessity follows because every column of S lies in range(T). For sufficiency,
choose

    P0=T^+ S (T^+)^dagger>=0.

Then T P0 T^dagger=Pi S Pi=S. This is a constructive covariance reconstruction,
not a dynamical state selector. Adding any N>=0 supported in ker(T) gives
another solution P0+N. That family is not asserted to list all possible
solutions: positive observed/null cross blocks can also be allowed.

If T has full row rank, Pi=I. Every finite PSD S is then algebraically feasible
for that parameter choice. One epoch's complete covariance cannot identify
parameters merely by fitting it when P is completely free and the transfer
remains surjective. Other information, such as known background constraints,
weak-amplitude bounds or state restrictions, can still constrain parameters.
The statement is about this covariance fit conditional on the supplied
background, not all possible observations or whole cosmic histories.

A PSD S has a bounded realization: take a finite square root B, let its input
coordinates be independent centered Rademacher variables, and set Y=B Z.
For a complex Fourier mode the paired negative mode can enforce reality.
That pairing alone does not establish statistical homogeneity, isotropy or
parity of an ensemble; those survey conditions must be supplied or constructed
separately. Neither Gaussianity nor an unbounded random tail is required. Common amplitude
rescaling shrinks S and every reconstructed finite state. This establishes
local weak feasibility for sufficiently small amplitudes, not realizability
of an arbitrary fixed measured amplitude within a linear theory.

### An explicit right inverse of this candidate at a regular event

Use the checked dust/radiation/scalar equations of
the recovered source `rolling_local_response/covariance_inverse_v1/independent_v1/sources/KINETIC_DERIVATION_v3.md`. Choose a regular event of the supplied
homogeneous background with phi=0 and dot(phi)=0, positive dust and radiation,
Q>0, Hv>0, 0<k<1/3 and nu>0. At that event C=A^2=1, grad U=0, U=3/2, and

    H^2=Hv^2+2(Rm+Rr)/3,
    Rm=rho_m,E/(2Q)>0, Rr=rho_r,E/(2Q)>0.

This is allowed instantaneous initial data for the background equations.
Dust gives a nonzero subsequent scalar acceleration; the background is not
being falsely held at a stationary vacuum over an interval. The selected
origin event is an explicit premise of this counterexample, not an inferred
state of our universe.

Let p>0. At this event set scalar perturbations xi=pi_scalar=0 and radiation
multipoles Theta_l=0 for l>=1. The radiation monopole Theta0, dust number
contrast n and velocity divergence theta are free subject to the Hamiltonian
constraint. The shear is zero initially, T_metric=L, and

    J=Rm theta/p^2,
    C_H=p^2 L+Rm n+4Rr Theta0+3H Rm theta/p^2=0.       (2)

The physical outputs are W=(T_J+L_J)/2=L, theta_J=theta and
Delta_m,J=n. More generally Delta_m,J=n-3 b.xi, so the last equality uses the
specified zero scalar perturbation. Thus with X=(n,theta,Theta0) and
Y=(W,theta_J,Delta_m,J), the constrained initial output map is

          [ -Rm/p^2   -3H Rm/p^4   -4Rr/p^2 ]
    T0 =  [     0          1             0   ],
          [     1          0             0   ]
    det T0=4Rr/p^2>0.                                (3)

For any proposed output triplet the explicit inverse is

    n=Delta_m,J,
    theta=theta_J,
    Theta0=-(p^2 W+Rm Delta_m,J+3H Rm theta_J/p^2)/(4Rr). (4)

The candidate therefore has a surjective instantaneous three-readout map in
this declared background class for every allowed k and nu. Constraint solving
has not selected the relative radiation/dust state. No phenomenological
single-growing-mode relation is inserted. Nonzero shear and scalar waves
are not required for this counterexample, although they supply additional
independent initial directions in the general theory.

The perturbations in (4) are initial data. The coupled evolution immediately
generates their derivatives and generally higher angular moments. They are not
an exact static or permanently perfect-radiation solution. For smooth regular
background coefficients on a finite short interval, the linear transport
integral equation coupled to the finite metric/scalar/dust equations has local
solutions by the usual bounded linear integral evolution; the initial
Hamiltonian constraint is preserved by the checked coupled identity. This
provides local compatibility, not a past-complete solution or an observed
expansion/transfer history.

When Rr is small or p is large, the reconstructed monopole can be large. The
bound |4Theta0|<<1, weak potentials, nonrelativistic velocities and positive
matter/radiation populations must be checked at fixed amplitudes. They do not
follow from PSD alone. For any fixed finite parameters with Rr>0 and p>0,
a sufficiently small common amplitude and bounded seeds satisfy these local
requirements. The neighborhood is not uniform as Rr->0, p->0 or p->infinity. At small p
the velocity contribution to Theta0 scales as theta_J/p^2 and the physical
peculiar velocity scales as theta_J/p.

### What additional observations would have to add

Several matched epochs from the same initial amplitudes have stacked transfer
Tstack=(T1;...;Tr), with full cross-time covariance

    Sstack=Tstack P Tstack^dagger.

If Tstack is rank deficient on the readout space, its left-null relations
L Tstack=0 require L Sstack=0. This condition may constrain parameters without
prescribing P. As an exact illustration, one seed with readouts (X,a X) requires
S12=a* S11 and S22=|a|^2 S11. Nonzero S11 then fixes that transfer ratio.
A PSD two-time covariance incompatible with those identities is infeasible
for that specified transfer. Replacing the one seed by two independent readout
seeds removes that restriction. It is the transfer support, not an assumed
covariance normalization, that supplies the constraint.

The full initial angular distribution in the candidate supplies many possible
modes. A finite chosen transfer truncation or arbitrary finite set of epochs
is not automatically rank deficient, so this paragraph does not promise that
more bins identify the scalar parameters. Nor do redshift bins automatically
measure a time series of the same mode or the needed cross-time covariances.
Actual projection, velocity bias, noise, light-cone geometry and selection must
be included in T before applying (1) to a survey. One must also distinguish
estimated noisy S from an exact PSD signal covariance.

### Assumption accounting

Equation(1) eliminates a chosen initial covariance from an exact feasibility
question. It does not derive or select the actual covariance, quantum state,
background, matter sector or action. Equation(4) supplies a concrete local
candidate witness that even three ideal equal-time observables can be matched
by changing allowed initial amplitudes. It does not claim agreement with the
observed universe, prohibit constraints from other observations, or show that
all parameters can fit a complete survey. The useful next target is an actual
matched observable operator and its support/rank with physical amplitude
bounds; inserting a single common seed would restore a supplied assumption.

## 2. Bounded homogeneous isotropic realization

This addendum strengthens only the local covariance counterexample, not a
cosmic history or observation fit. Use the same fixed positive-p origin event,
T0 and R0=T0^{-1} as Part I above. Let a real symmetric PSD output
matrix S0 have a real finite factor B B^T=S0. Let Z have independent centered
Rademacher coordinates with E[ZZ^T]=I, Phi be uniform on[0,2pi), and n be
uniform on the unit sphere, all independent. At physical position x define

    Y(x)=sqrt(2) epsilon B Z cos(p n.x+Phi),
    X(x)=R0 Y(x).                                      (1)

All components are real and bounded. Uniform phase gives zero mean and

    E_Phi[2 cos(p n.x+Phi)cos(p n.y+Phi)]
      =cos[p n.(x-y)].

Uniform direction then gives, for r=|x-y|,

    E[Y(x)Y(y)^T]=epsilon^2 S0 sin(pr)/(pr),            (2)

with limit1 at r=0. More than second-moment invariance holds: translating all
positions just shifts the uniform phase conditional on n; rotation or parity
changes the uniform direction. Thus the ensemble has homogeneous, isotropic,
parity-invariant finite-dimensional distributions. This supplies an explicit
allowed ensemble; it does not prove that observations select it. It is a
monochromatic-shell example, not a broadband measured spectrum or ergodicity
claim. Its special realization structure need not represent sky statistics.

The linear Hamiltonian constraint and readout map hold for every realization
because all scalar components share the same Laplacian eigenvalue -p^2 and
T0 is independent of direction. For the velocity output theta(x)=A_theta
cos(p n.x+Phi), choose physical peculiar velocity

    v(x)=A_theta n sin(p n.x+Phi)/p.

Its physical divergence is theta(x). Its amplitude is bounded by
|A_theta|/p. The scalar background still has the unselected origin event and
subsequent dust-driven acceleration; the perturbations still evolve and
produce higher radiation angular moments. This is not a permanent perfect
fluid or static metric solution.

For every realization, row l1 norms bound |BZ| and |R0 BZ|. A sufficiently
small common epsilon makes |W|, |n_m|, |4Theta0| and |theta|/p less than a
fixed small eta. In particular it keeps dust and radiation density positive.
Relative to the earlier eight-sign construction, reduce epsilon by sqrt(2)
to preserve the same1/100 worst-case margin. The target covariance then has
the correspondingly reduced amplitude; arbitrary fixed observed amplitudes
are not claimed feasible. The neighborhood remains nonuniform as radiation
vanishes or p approaches zero/infinity.

Equations(1)-(2) show that homogeneous/isotropic/parity symmetry alone does
not restore unique initial covariance or scalar couplings in this local
counterexample. A particular P, observed spectrum, ensemble statistics,
ergodicity, earlier history and physical calibration are not derived. A
real survey requires its actual windows, noise and evolution; none is fit here.

## Computation and empirical limits

The canonical runner preserves70 inverse/support controls and34 spatial-ensemble
controls. Exact source proofs, original70/0 and34/0 results, independent checks,
and altered-program controls are carried with the archive. The initial SymPy
attribute failure and the finite-wavelength/domain clarification remain explicit.

Transfer matrices and random ensembles in this note are mathematical inputs or
constructions. A covariance estimated from noisy observations is not automatically
an exact positive semidefinite signal matrix. A real measurement needs its
projection, selection, noise, velocity calibration and evolution operator; its
amplitude must satisfy the stated physical inequalities. No such data analysis
was performed. Multi-epoch support can add constraints only when the actual
stacked transfer has nontrivial left-null relations; no finite-bin guarantee is
asserted. The construction retires a compulsory Gaussian or single common growing-seed premise
for this counterexample, not the need to determine the universe's initial state.
