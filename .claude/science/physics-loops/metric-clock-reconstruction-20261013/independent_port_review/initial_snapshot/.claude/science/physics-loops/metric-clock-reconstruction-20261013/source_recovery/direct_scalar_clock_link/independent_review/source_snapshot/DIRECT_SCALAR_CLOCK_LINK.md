# One scalar coupling: static force, clock phase and reference geometry

Status: conditional-support. Direct parent derivation. The tensor/scalar
action is the supplied candidate in the preceding block. This extension adds
canonical quantization and a specified scalar state, source and readout. It
does not infer a quantum vacuum from gravity measurements or bound all
possible gravitational decoherence.

## Action normalization and new state assumptions

Keep G_*>0, constant positive K_AB, constant alpha_A and
a=alpha^T K^-1 alpha. At the asymptotically flat zero-scalar background the
quadratic scalar action, in physical time t, is

    S_phi=c^2/(8pi G_*) integral dt d^3x
          K_AB [phi_dot^A phi_dot^B-c^2 grad(phi^A).grad(phi^B)].

Canonical momentum is pi_A=c^2 K_AB phi_dot^B/(4pi G_*). Impose
[phi^A(x),pi_B(y)]=i hbar delta^A_B delta^3(x-y), and choose the Minkowski
Gaussian vacuum. These are explicit quantum/state assumptions. For the
dimensionless scalar seen by matter, zeta=alpha_A phi^A, quantizing each
positive harmonic mode gives

    <zeta(t,x)zeta(0,0)>=(4pi G_* hbar a/c^2)
      integral d^3k/[(2pi)^3 2ck] exp(-ickt+ik.x).

The coefficient follows from the oscillator mass matrix c^2 K/(4pi G_*),
not an independent adjustable noise amplitude. The free quantum description
must hold over the frequencies sampled by the source profile. This is not a
derived ultraviolet completion or a statement about a thermalized real field.

The normalization also fixes the classical source response. A static energy
E couples through H_I=E zeta. Varying the same action gives
Delta phi^A=(4pi G_*/c^4)v^A E delta^3(x), so
zeta=-G_*a E/(c^4 r). Two sources therefore have scalar interaction
-G_*a E1 E2/(c^4 r), counting the field energy once. Setting E_i=m_i c^2
recovers the scalar Newtonian coefficient G_*a=G_N f_scalar. For two of the
Gaussian profiles defined below, the interaction is instead
-G_*a E1 E2 erf[L/(2ell)]/(c^4 L), with finite L=0 limit obtained continuously.
This follows from the same squared Fourier profile multiplying4pi/k^2.

Let f_ell(x)=(2pi ell^2)^(-3/2)exp[-|x|^2/(2ell^2)], ell>0, and define the
smeared zeta_j(t) centered at fixed x_j. The Fourier transform is
exp(-ell^2 k^2/2); the covariance contains exp(-ell^2 k^2). A direct angular
and on-shell frequency integration gives the unsymmetrized spectrum

    S_0^+(omega)=integral dt e^(iomega t)<zeta_j(t)zeta_j(0)>
       =(2 G_* hbar a/c^5) omega exp[-(ell omega/c)^2] theta(omega).

The Gaussian profile is a test-clock idealization, not a measured atomic
energy-density form factor or a compact-support source. Tensor fluctuations,
material supports, scalar self-backreaction and a realistic optical link are
outside this leading scalar-channel calculation. In particular positivity
of this result does not justify treating the whole gravitating apparatus as
a prescribed nonconserved source for a tensor field.

## Which clock phase is defined

Supply an identical rest-clock splitting DeltaE=hbar Omega at each center.
The universal metric gtilde=exp(2zeta)g_* gives proper time
d_tau=exp(zeta)dt for a stationary weak probe at this background. Therefore
the coordinate Hamiltonian has splitting hbar Omega exp(zeta), and to first
order H_I=(hbar Omega/2) sigma_z zeta_j, up to an identity term. Omega is
the proper-frequency parameter; it is not a fluctuating dimensionless constant.

The single-clock comparison uses a supplied ideal external phase reference
unaffected by this zeta. It is useful as a mathematical contrast, but does
not follow automatically for a co-located universally coupled oscillator.

For a balanced pair instead use logical states |0_L>=|eg>, |1_L>=|ge>.
Their total unperturbed energy is equal. The branch energy difference is
hbar Omega(zeta_1-zeta_2), so the logical interaction is

    H_I,L=(hbar Omega/2) Z_L B(t),  B=zeta_1-zeta_2.

The common identity coupling does not change the visibility. In this symmetric
stationary two-center model its cross-commutator with the difference vanishes:
the equal self terms cancel, as do the reciprocal cross terms. No uncomputed
relative bath phase is being converted into a loss of visibility.

Prepare |+_L>, couple for the specified interval and measure logical X_L,Y_L.
After any known deterministic phase compensation, p_+=(1+V)/2. These are
supplied logical preparation/readout operations, not an implemented distant
clock comparison. A real causal link, transport and control apparatus must
be modelled before associating this channel with actual counts. Common-mode
cancellation below is nevertheless a property of the stated source difference,
not an assumed independent bath at each clock.

Assume initially factorized clock/field state and ideal switching y(t).
Gaussianity and the c-number commutator make the Magnus expression exact
for this linear pure-dephasing model. For either B, the coherence magnitude is

    V_y=exp(-chi_y),
    chi_y=Omega^2/2 integral dt ds y(t)y(s)<{B(t),B(s)}> /2
         =Omega^2/(4pi) integral_0^infinity S_B^+(omega)|Y(omega)|^2 d_omega,
    Y(omega)=integral y(t)exp(iomega t)dt.

For a single reference use B=zeta_j. For the pair, separation L=|x1-x2|
inserts the exact angular form factor

    S_pair^+=2[1-sinc(omega L/c)] S_0^+.

Here sinc(z)=sin(z)/z. The factor is the angular average of
|exp(ik.x1)-exp(ik.x2)|^2. At low frequency it is
(omega L/c)^2/3+O(omega^4), not2. Treating the baths as independent would
erase this cancellation. The resulting kernel is a unitary-environment
Gram kernel, so this supplied dephasing channel is completely positive.

## Exact time and separation functions

Set x=cT/ell, d=L/ell and

    kappa=G_* a hbar Omega^2/(pi c^5)
         =G_N f_scalar hbar Omega^2/(pi c^5)
         =2 G_N h f_scalar nu^2/c^5,   Omega=2pi nu.

The second equality uses the preceding weak universal static map
G_N=G_*(1+a), f_scalar=a/(1+a). It is conditional on the same action and
source-identification assumptions, not on an arbitrary fitted force kernel.
Define the nonnegative even function

    F(x)=integral_0^infinity e^(-u^2)(1-cos xu)/u du.

Its derivative is Dawson(x/2), with Dawson(z)=e^(-z^2)integral_0^z e^(t^2)dt.
Equivalently

    F(x)=x^2/4 * hypergeom([1,1],[3/2,2],-x^2/4).

Direct cosine expansion gives F=x^2/4-x^4/48+O(x^6). At large |x|,
F=ln|x|+gamma_E/2-1/x^2+O(x^-4). One derivation of the constant uses
the regulated difference of Mellin integrals at s=0:
Gamma(s/2)/2-Gamma(s)cos(pi s/2)|x|^-s. The poles cancel, leaving
ln|x|+gamma_E/2. The asymptotic inverse-power terms follow by integrating
the large-x Dawson derivative. These are asymptotic expansions, not global
finite-error bounds.

For a single-clock Ramsey interval, chi_R,1=kappa F(x). For one ideal sign
reversal at T/2,

    chi_E,1=kappa[4F(x/2)-F(x)].

The single-reference vacuum thus has logarithmically growing chi_R,1 and
power-law visibility at long time, while chi_R,1/T tends to zero. The earlier
continuous-mass bath had a different infrared measure and need not share
this behavior. A massless spectral atom cannot be silently identified with
that previous continuum.

For the pair define

    J(d)=integral_0^infinity e^(-u^2)[1-sinc(du)]/u du
        =integral_0^1 F(dt)dt
        =F(d)-1+2Dawson(d/2)/d,
    H(z)=z F(z)-z+2Dawson(z/2),  H'(z)=F(z),
    D(x,d)=integral_0^infinity e^(-u^2)
                  [1-sinc(du)](1-cos xu)/u du
          =F(x)+J(d)-[H(x+d)-H(x-d)]/(2d).

The d=0 limits of J,D are zero. The closed finite-time formula follows by
writing sinc(du)=integral_0^1 cos(dut)dt and using the cosine product rule.
The antiderivative follows from Dawson'(z)=1-2zDawson(z). No fit is involved.
The two pair exponents are

    chi_R,pair=2kappa D(x,d),
    chi_E,pair=2kappa[4D(x/2,d)-D(x,d)].

At fixed finite d, the integrable weight defining J permits the
Riemann-Lebesgue lemma. Consequently

    chi_R,pair -> 2kappa J(d),
    chi_E,pair -> 6kappa J(d).

The balanced reference removes the single-reference infrared logarithm.
The order of limits matters: d tending to infinity first gives two independent
single-clock exponents at each fixed finite x; fixed finite d followed by
x tending to infinity instead gives a finite plateau. At d=0 the difference
source vanishes identically, including at finite time.

For small d, J=d^2/12-d^4/240+O(d^6). For large d,
J=ln d+gamma_E/2-1+1/d^2+O(d^-4). This is separation dependence of the
specified clock channel, not an observed decoherence law.

## A conservative bound and its proper physical scope

The exact integral shows0<=D(x,d)<=2J(d) at any x. The echo numerator is
3-4cos(xu/2)+cos(xu)=2[1-cos(xu/2)]^2<=8, so

    0<=chi_R,pair<=4kappa J(d),
    0<=chi_E,pair<=16kappa J(d).

For d>0, use 1-sinc(du)<=d^2 u^2/6 to get J<=d^2/12. Alternatively
split the positive integral at u=1/d, use the same quadratic inequality below
the split and1-sinc<=2 above it. With E1(z)=integral_z^infinity e^-t dt/t,

    J(d)<=min[d^2/12, 1/12+E1(1/d^2)].

These are analytic inequalities for the supplied Gaussian model. They do not
depend on an asymptotic series at the large SI separation ratios. Also
1-V<=chi. Inserting f_scalar<=1/2500 from the earlier illustrative working
rectangle bounds this scalar vacuum channel only. G_N uses the stated
CODATA central value, with no claim of a new confidence interval.

The small scale of this result, if obtained, would not explain an observed
large decoherence rate by default. Thermal occupation, squeezed states,
initial dressing/correlations, other fields or nonuniversal couplings can
change the symmetric covariance while preserving the static response.
Switching and pulses can supply work and make branch-dependent dressing;
this is not a claim that an isolated dressed energy eigenstate loses
coherence without a preparation/control history.

Finally, a real classical Gaussian field with the same symmetric two-center
covariance produces these same longitudinal visibilities. The calculation
does not establish quantum rather than classical noise. An independently
available noncommuting probe and its full source/control response would be
needed for that different question. No real clock, neutrino or interferometer
observation is fitted or excluded by the synthetic controls below.
