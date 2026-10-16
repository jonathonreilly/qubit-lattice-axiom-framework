# From weak scalar sources to a calibrated laboratory ratio

Status: exploratory conditional support, personally derived by root. The
observation intake is LAB_OBSERVATION_INTAKE_v1.md. This calculation challenges
point-body and calibration identifications before using a laboratory exclusion.
No experimental data are fitted, and no potential or density profile is selected.
The linear Yukawa Green function and ratio algebra are standard mathematics.

## 1. Extended source and what its boundary condition supplies

In a nearly constant, weak, unscreened background with F0>0, D0=2omega+3>0
and m>=0, hold material sources fixed at leading order. The linear static
scalar equation from SCALAR_SOURCE_CLOSURE_v2.md is

 (Laplacian-m^2) deltaF = -sigma/D0,
 sigma = rho - sum_i p_i.

An isotropic material has sigma=rho-3p. Specifying decay relative to the
background at spatial infinity selects the solution

 deltaF(x)=1/(4pi D0) int sigma(y) exp(-m|x-y|)/|x-y| d^3y.       (1)

This boundary condition, uniform coefficients and the neglect of induced
material response are premises. Nearby chamber/background sources or nonlinear
screening must be solved or bounded separately. They are not removed by using
a measured mass. In the negligible-stress universal weak-body limit, (1) and
the matter coupling give the interaction

 U=-GT int int rhoA(x)rhoB(y)[1+a exp(-mr)]/r d^3x d^3y,
 GT=1/(8pi F0),  a=1/D0,  r=|x-y|.                            (2)

The laboratory Yukawa strength a is the product of two equal dimensionless
weak charges, not the single charge alpha of the source-closure note.
A nonnegligible stress trace modifies scalar source weighting and test-body
response. Equation(2) is not then automatically a density-only integral.

For a spherically symmetric sigma supported in radius R and exterior r>R,
angular integration of (1) gives

 deltaF(r)=exp(-mr) Q_m/(4pi D0 r),
 Q_m=4pi int_0^R y^2 sigma(y) sinh(my)/(my) dy.                 (3)

Indeed, with s=|x-y|, dcos(theta)=-s ds/(ry), the angular integral is
4pi exp(-mr) sinh(my)/(r my). The m=0 limit is continuous.
For nonnegative rho and 0<=sum p_i<=epsilon rho, 0<=epsilon<1,

 (1-epsilon) M <= Q_m <= M sinh(mR)/(mR).                     (4)

The weight is increasing because z cosh(z)-sinh(z) has derivative z sinh(z)
and vanishes at zero. This bound requires no selected radial density. With
zero pressure its lower endpoint can be approached by central concentration,
and its upper endpoint by a thin outer shell. For fixed positive epsilon the
lower endpoint additionally requires the maximal allowed stress trace.

These exterior bounds do not prove an interior is weak or unscreened. A
pressureless uniform core of mass M and radius epsilonR has central Newtonian
potential magnitude 3GT M/(2epsilonR), unbounded as epsilonR tends to zero,
while its exterior Q_m/M tends to one. A radius upper bound and total mass
alone cannot certify the neglected nonlinear/interior physics. Such a static
pressureless core is a source-distribution counterexample, not a self-supported
material equilibrium. An equation of state or physical support is still needed
for a real stationary body.

## 2. Actual torque geometry is a signed measurement functional

Spherical bounds cannot replace the patterned detector geometry. Rotate the
first body's coordinates about z: x_theta=R_z(theta)x, Jx=z_hat cross x.
Differentiating (2), the scalar torque per GT*a has pair kernel

 K_m(x,y)=-[(x-y) dot Jx] (1+mr)exp(-mr)/r^3.                  (5)

Let Y(theta;m) be its mass-density double integral; define N(theta)=Y(theta;0).
For a declared complex Fourier convention Y_n=(1/(2pi))int Y exp(-in theta),

 tau_n=GT[N_n+aY_n(m)].                                     (6)

If all body pairs stay separated by d>0 and |Jx|<=L, then

 |K_m| <= B_m = L(1+md)exp(-md)/d^2,
 |Y_n| <= B_m M_A M_B.                                      (7)

The inequality follows from |(x-y)dot Jx|<=rL and the decreasing radial
factor. Real sine/cosine amplitudes equal twice the corresponding complex
coefficient, and need that factor in a bound. Cancellation may make a harmonic
arbitrarily small or zero: no positive lower bound follows from mass positivity.

For fixed positions, let nominal nonnegative densities have masses M_A,M_B,
and density differences have L1 norms deltaM_A,deltaM_B. The same signed-kernel
bound gives

 |deltaY_n| <= B_m[M_A deltaM_B+M_B deltaM_A+deltaM_A deltaM_B]. (8)

This is a deterministic density uncertainty bound, not a noise confidence
interval. Geometry, angle, distance, pressure and filter uncertainties need
additional certificates; (8) does not supply them. Hole-contrast descriptions
can have signed densities; use actual positive densities or total-variation
masses when applying a norm estimate.

## 3. Remove the common gain without silently declaring gravity calibration

After independently justified frequency/transfer corrections, suppose the
record in each science channel and one calibration channel obeys

 z_i=g GT (N_i+aY_i),   z_c=g GT(N_c+aY_c),   z_c!=0.          (9)

Here g is an unknown common instrument gain. Common gain and source environment
are hypotheses to check, not consequences of dividing. Measured complex ratios
r_i=z_i/z_c give, for every trial m,

 b_i=r_i N_c-N_i,  A_i=Y_i-r_i Y_c,
 b_i=a A_i.                                                 (10)

Thus a nonzero A_i determines a=b_i/A_i. All channels must give the same real
nonnegative value; equivalently the two-vectors A,b are proportional with that
sign/reality restriction. Pairwise determinants alone are insufficient when
all A_i vanish. If A=0,b!=0 there is no solution; if A=b=0 the strength is
unidentified by these ratios. At m=0, Y=N and every ratio is Newtonian for all
a>=0, so an independent absolute amplitude/gain input is necessary.

The calibration Yukawa response Y_c must be retained. If a bound on a is
available, (7) bounds |aY_c/N_c| when N_c!=0. Exponentially small interaction
at the measured calibration separations can justify its omission. Merely
calling the channel a Newtonian calibration does not justify it. Short-range
exclusion plots must retain their actual calibration and material premises.

For exact geometry and a measured ratio rhat with |rhat-r|<=e, put
Ahat=Y_i-rhat Y_c. When |Ahat|>|Y_c|e,

 |ahat-a| <= e |N_c Y_i-N_i Y_c|
              /[|Ahat|(|Ahat|-|Y_c|e)],  ahat=(rhat N_c-N_i)/Ahat. (11)

This follows by subtracting the two Mobius fractions and lower-bounding |A_i|.
It is valid for complex ratios. A zero denominator is an identifiable failure
of this inversion, not evidence for a different scalar theory. Real-nonnegative
compatibility and errors in geometry must still be tested.

Only g*GT enters (9). The transformation GT->t GT, g->g/t keeps every record
fixed within this measurement contract; ratio tests cannot recover F0. If an
independently calibrated physical torque gain and mass/geometry model are
available, GT can be inferred from (6). Identifying a long-range measured G_N
with GT requires a negligibly small scalar contribution at that calibration
range, with its own certificate. A fitted instrumental gain does not derive
an absolute gravitational normalization.

## 4. Connection to the inverse action and outstanding observation work

At a registered constant vacuum point of the earlier static action chart,

 a=1/(2omega+3),  m^2=2(W_xx-W)/(2omega+3),  W_x=W.            (12)

This maps a compatible weak laboratory response to action-shape combinations
without choosing C in F=C exp(x). It requires an actual vacuum/action
continuation and applicability of the constant-background linear regime;
Earth/chamber material cannot simply be declared that vacuum. Nor does it
establish that a laboratory body and compact binary share effective charges.

The primary controls will compare (3) to independent angular quadrature for
several positive radial distributions, check the sharp support endpoints,
compare (5) with finite differences of pair energy, detect harmonic cancellation,
verify density-norm bounds, and test exact/noisy calibration ratios including
nonzero calibration leakage and m=0 nonidentifiability. All are synthetic.
LAB_OBSERVATION_ACCESS_PLAN_v1.json keeps any subsequently obtained Lee tables
in exposed development/reproduction status. No new empirical test is claimed.
