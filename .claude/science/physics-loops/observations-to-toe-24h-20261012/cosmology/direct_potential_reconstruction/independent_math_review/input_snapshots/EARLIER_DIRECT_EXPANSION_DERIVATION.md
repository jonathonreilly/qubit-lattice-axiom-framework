# A physical expansion bound and a distance-ratio observable

Direct parent derivation. Type: bounded_theorem. Actual surface status:
conditional-support. The next reconstruction asks what the already supplied
local metric/scalar candidate says about observed redshift-distance relations.
No cosmological constant, dark-energy density or supernova fit is silently
added. Observational comparison has not yet been executed.

## Candidate and physical clock

Keep the positive constant scalar matrix K, constant alpha, Einstein action
and matter metric g_J=A^2 g_*, A=exp(zeta), zeta=alpha.phi. Write
a=alpha^T K^-1 alpha. Use c=1 in the cosmological derivation. Add spatially
flat homogeneous isotropic geometry, positive pressureless matter and
radiation, homogeneous scalars, no scalar potential, and H_*>0. Matter has
the universal metric coupling and the displayed ideal fluid equations of
state; constituent sensitivities and a late-time fluid closure are ignored
at this level. This is an explicit continuum/source assumption.

Let R_* denote the Einstein scale factor, and dot its proper-time derivative.
The physical scale factor and proper time are R_J=A R_* and dt_J=A dt_*.
The physical expansion rate is therefore

    H_J=(H_*+dot zeta)/A=H_*(1+y)/A,
    y=dot zeta/H_*.

The field and continuity equations from the same action are

    3H_*^2=8pi G_* (rho_m+rho_r)+K_AB dot phi^A dot phi^B,
    dot H_*=-4pi G_* (rho_m+4rho_r/3)-K_AB dot phi^A dot phi^B,
    ddot phi^A+3H_* dot phi^A=-4pi G_* (K^-1)^AB alpha_B rho_m,
    dot rho_m+3H_* rho_m=dot zeta rho_m,
    dot rho_r+4H_* rho_r=0.                                  (1)

The sign of the matter trace source follows from T_*=-rho_m and the earlier
Box phi=-4pi G_* K^-1 alpha T_* convention. The minus sign in the time
part of Box reverses it again in the acceleration equation. Radiation has
zero trace. The continuity equation also follows from m_*=A m_J and conserved
comoving particle number. These checks matter when converting frames.

Define nonnegative fractions

    Omega_m=8pi G_*rho_m/(3H_*^2),
    Omega_r=8pi G_*rho_r/(3H_*^2),
    Omega_s=dot phi^T K dot phi/(3H_*^2),
    Omega_m+Omega_r+Omega_s=1.

Then q_*=-1-dot H_*/H_*^2=Omega_m/2+Omega_r+2Omega_s, and Cauchy gives
y^2<=3a Omega_s. The homogeneous velocities orthogonal to the sourced
direction are retained in Omega_s; they are not discarded as unsourced.

Taking two physical-time derivatives of R_J gives

    (d^2 R_J/dt_J^2)/R_J
      = A^-2 [dot H_*+H_*^2+H_* dot zeta+ddot zeta].

Using ddot zeta=-3H_* dot zeta-4pi G_* a rho_m yields

    q_J = [q_*+2y+(3a/2)Omega_m]/(1+y)^2.                    (2)

Replacing q_J by q_* or omitting the trace term would compare observations
to a different model. For0<=a<1/3, Cauchy ensures |y|<1 and H_J>0 on every
permitted state. No scalar-dominated contracting physical branch is hidden
inside this stated domain.

## A quantitative bound, including the equality trajectory

For0<a<1/3, put

    q_b=(1+a)/[2(1-a)].

Substitute Omega_m=1-Omega_r-Omega_s into(2) and complete the square:

    (1+y)^2(q_J-q_b)
      = (1-3a)(y+a)^2/[2a(1-a)]
        +(3/2)(1-a)[Omega_s-y^2/(3a)]
        +(1-3a)Omega_r/2 >=0.                               (3)

Every coefficient and bracket is nonnegative. At a=0, alpha=0 and y=0,
so q_J=1/2+(3/2)Omega_s+Omega_r/2>=1/2 directly. Consequently the whole
supplied range0<=a<=1/2499 obeys q_J>=1/2, with the sharper q_b for known
nonzero a. This is an exact prediction of the stated homogeneous model, not
a global theorem about scalar theories, spatial curvature or other matter.

Equality at a>0 needs y=-a, Omega_s=a/3, Omega_r=0; all scalar velocity is
in the alpha direction. It is dynamically attainable, not just a minimizer
outside the field equations. Take N=ln R_*, x^A=dphi^A/dN. Equations(1) imply

    dx^A/dN=(q_*-2)x^A-(3/2)(K^-1)^AB alpha_B Omega_m,
    dOmega_r/dN=2(q_*-1)Omega_r,
    dln H_*/dN=-(1+q_*).

With x=-K^-1 alpha, Omega_s=a/3 and Omega_m=1-a/3, the right side of the
x equation is zero. Thus A proportional to R_*^-a and

    H_J proportional to R_J^[-(3-a)/(2(1-a))],
    R_J proportional to (t_J-t_origin)^[2(1-a)/(3-a)],
    q_J=q_b.                                                (4)

This supplies a constant-q equality curve. A full global attractor theorem
is not needed or asserted. The a=0 equality case is the ordinary flat dust
trajectory. Neither trajectory is fitted to supernova shape data here.

## A normalization-free necessary distance relation

Supply physical flat optical distances, transparency and distance duality.
For a constant comparison bound q_c>0, define

    B_qc(z)=[1-(1+z)^(-q_c)]/q_c
           =integral_0^z (1+u)^[-1-q_c] du.

For any smooth expanding history with q_J(z)>=q_c,

    dln H_J/dz=(1+q_J)/(1+z),
    j(z)=(1+z)^(1+q_c)/H_J(z)

is nonincreasing. The ratio

    T(z)=[integral_0^z du/H_J(u)]/B_qc(z)

is the weighted average of j over[0,z] with positive weight
w(u)=(1+u)^[-1-q_c]. Its derivative is

    T'(z)=w(z)[j(z)-T(z)]/B_qc(z)<=0.                        (5)

This proof requires the q bound on the whole interval from0 to the observed
redshift, not merely at today's epoch. It does not require knowing H0.

For a constant standardized absolute magnitude, the ideal corrected apparent
magnitude is an additive unknown intercept plus5log10 of luminosity distance.
Using the release's corrected expansion redshift zHD and heliocentric
prefactor zHEL gives the supplied observation map

    m_b_corr = M0+5log10[(1+zHEL) integral_0^zHD du/H_J(u)],
    r_i = m_b_corr_i-5log10[(1+zHEL_i) B_qc(zHD_i)].           (6)

Constants, units and H0 are absorbed in M0. Equation(5) says the ideal mean
r(zHD) is nonincreasing. Every high-redshift point therefore has mean at most
every lower-redshift point. The arithmetic mean of a high group minus that of
a disjoint lower group has predicted mean<=0. Nonnegative weights within
each group are essential; a generalized inverse-covariance mean can have
negative weights and would not inherit this order argument automatically.

The planned q_c=1/2 contrast applies to every a in the supplied weak-coupling
interval under the other model and observation assumptions. It is not limited
to the equality solution. For coefficient vector c with positive equal high
weights and negative equal low weights, sum c=0 removes the intercept, and
the supplied full covariance gives variance c^T C c. This is one processed-
data contrast. It is not independent of the separate transfer residuals.

## Calibration and a correlated reserved comparison

The fixed candidate curves are q=1/2, q=q_b at a=1/2499, and an explicitly
supplied flat-LambdaCDM benchmark with Omega_m=.3. For each, write its shape
prediction g_i=5log10[(1+zHEL_i) integral_0^zHD_i du/E(u)]. Fit only an
additive intercept using the frozen lower-redshift calibration subset L.
Set d_L=m_L-g_L, Q=C_LL^-1 and

    V_M=(1_L^T Q 1_L)^-1,
    Mhat=V_M 1_L^T Q d_L.

For the reserved higher-redshift subset T, retaining the full supplied
cross-covariance and using a flat intercept prior yields

    B=C_TL Q,   v=1_T-B 1_L,
    E[m_T | m_L]=g_T+B d_L+v Mhat,
    S=C_TT-B C_LT+V_M v v^T.                                (7)

Proof: at a fixed M, conditioning a joint Gaussian gives mean
g_T+M1_T+B(d_L-M1_L) and covariance C_TT-B C_LT. The calibration posterior
for M is Gaussian with mean Mhat and variance V_M. Integrating it adds
V_M v v^T. Thus the test data never recalibrate M or a cosmological shape.
The retained calibration residual may predict correlated systematics in the
test mean; suppressing it would discard the released correlations.

The resulting quadratic residual is a conditional processed-summary comparison.
The public data's nuisance training, bias corrections and systematic priors
were not newly blinded or refitted. Raw light curves, events and a new SALT2
calibration are not part of this calculation. Repeated light curves retain
their original correlations and are not counted as independent supernovae.

## Source-luminosity ambiguity is a physical assumption

Universal metric coupling does not by itself make stellar explosions standard
candles when gravitational strength evolves. A model for the standardized
absolute luminosity is therefore a new observational bridge. Under an added
term M(z)=M0+beta log10(1+z), the contrast changes by
beta c^T log10(1+zHD). Its free coefficient can absorb that single contrast.
The frozen beta sensitivity grid and the separately inferred cancelling beta
will make this degeneracy visible; neither estimates actual SN evolution.

The physical local coefficient is G_J=G_* A^2(1+a), so even a supplied
mass/luminosity scaling would need the candidate's full scalar history.
The earlier weak polytropes do not derive thermonuclear luminosities or the
SALT2 correction. No field theory is empirically excluded independently of
these source, geometry and processed-data assumptions.

The primary release README and SN-only likelihood were read in full at
c447f0fea703fcd0fff57de5000947b5ca81286b. The latter uses m_b_corr, zHD, zHEL,
the full covariance, and the luminosity prefactor in(6); this block's explicit
selection differs from its default zHD>.01 selection. The primary cosmology
paper's methodology sections were read, including the fiducial cosmology in
some redshift-error and systematic-response modeling. No raw-photometry
likelihood or independent modern data compilation is claimed.

Repository FRW kinematic and inverse-ratio notes were read as context. They
condition on a different supplied constant-density sector and leave its
normalization open. Their status claims, observational comparators and runners
are not adopted or repeated as premises of equations(1)-(7).

Next: freeze concrete numerical evolution fixtures, execute the math controls
and the already frozen data comparisons, preserve any mismatch, and decide
which additional physical input the observations actually constrain.
