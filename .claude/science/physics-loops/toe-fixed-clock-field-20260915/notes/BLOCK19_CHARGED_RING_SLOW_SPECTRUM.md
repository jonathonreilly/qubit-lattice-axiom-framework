# The charged ring: proved slow levels and the Gauss-connection correction

Personal derivation, 2026-09-15. PROVISIONAL; personal checks and review complete.
No independent audit. This closes a finite-ring asymptotic obligation,
not the periodic three-dimensional charged phase.

## 1. Exact model and result

Use the four-site, two-spinless-fermion ring from main revision
e0ef7cf4633034a8c1e6d57f5812cc4275bf1349,
FLAT_HOLONOMY_MINIMIZATION_AND_PERIODIC_SPECTRAL_FLOOR, dated2026-09-13.
That431-line source has been read fully. It proves the rate-free floor and
holonomy concentration, but labels its slow-gap coefficient as formal.

There is NO magnetic plaquette on this ring. Its loop is a global flat
coordinate. With reference eta=(0,1,0,1), occupations f of two particles,
rho=N-eta, and integer cycle flux n, the exact physical fields are

 E_l=n+E0_l(f), E0=(rho0,rho0+rho1,rho0+rho1+rho2,0).

The rotor Hamiltonian is

 H_g=(g^2/2)sum_l E_l^2+sum_(j mod4)(c_j^dag U_j c_(j+1)+h.c.). (1)

At hard cutoff S keep precisely |n+E0_l(f)|<=S for all four links.
In angle coordinates n=-i partial_theta, theta modulo2pi, the closing
hop has exp(i theta). The six-state matter Hamiltonian is H_m(theta).
Its lowest eigenvalue on0<=theta<=2pi is

 e(theta)=-2sqrt2 cos((theta-pi)/4), e_*=-2sqrt2.

Set Omega=2^(-1/4). For the UNTRUNCATED physical rotor, and every fixed
j=0,1,2,... counted from zero, the new expansion is

 E_j(g)=e_*+Omega(j+1/2)g
               +[5/16-(2j^2+2j+1)/128]g^2+O_j(g^3).   (2)

In particular

 E0=e_*+2^(-5/4)g+(39/128)g^2+O(g^3),
 E1-E0=2^(-1/4)g-g^2/32+O(g^3).                       (3)

For the exact hard cutoff, the leading fixed-index statement

 (E_j(g,S)-e_*)/g ->Omega(j+1/2)                       (4)

holds whenever S sqrt(g)->infinity. To retain the O(g^3) remainder in(2),
a sufficient stronger condition is S>=g^(-1/2-epsilon) for any fixed
epsilon>0. Constants may depend on j,epsilon. Merely S sqrt(g)->infinity
does not by itself supply a g^2-accurate cutoff error.

## 2. An exact local change of frame removes derivative band coupling

Complete the electric square with the diagonal six-state matrices

 A_f=(1/4)sum_l E0_l(f),
 C_f=(1/2)sum_l E0_l(f)^2-2A_f^2>=0.

Then H_E=2g^2(-i partial_theta+A)^2+g^2 C. If
X_f=sum_(j=0)^3 j N_j, the fixed two-particle/reference choice gives

                       A_f=1-X_f/4.                   (5)

Put delta=theta-pi and use the local diagonal unitary
U(delta)=exp(-i A delta). Its connection exactly cancels:

 U^*(-i partial_theta+A)U=-i partial_theta.             (6)

The transformed matter forward hopping matrix is exp(i delta/4) times
its value at theta=pi. Its adjoint gets the conjugate phase. The one-particle
forward matrix is a unitary signed cyclic permutation; hence this entire
family is diagonalized by ONE constant momentum basis, including its
two-particle exterior power. In that basis, on a neighborhood of pi,

 H_g= -2g^2 partial_delta^2 I+diag(e_a(delta))+g^2 C',    (7)

where C' is a constant Hermitian matrix. The ground label is simple and
fixed throughout this neighborhood. Its gap to the other matter labels is
bounded away from zero there; for |delta|<=pi/2 one may use a positive
constant smaller than4 sin(pi/8).

The frame U need not be periodic around the whole circle. Equation(7)
is used on a simply connected chart around the unique minimum, with
localized vectors. No global Berry/boundary twist is discarded.

In occupation masks(3,5,6,9,10,12), a normalized real ground vector at pi is

 u=(sqrt2/4,-1/2,sqrt2/4,sqrt2/4,-1/2,sqrt2/4)^T.

The corresponding E0 rows are

 (1,1,1,0), (1,0,1,0), (0,0,1,0),
 (1,0,0,0), (0,0,0,0), (0,-1,0,0).

They give C=diag(3/8,1/2,3/8,3/8,0,3/8), and therefore

                         C'00=u^* C u=5/16.           (8)

This constant is part of the actual Gauss-constrained electric energy.
It is not an adjustable zero-energy subtraction introduced for the expansion.
In a parallel phase for the ground vector, its covariant derivative has
zero component into the other matter bands. Thus there is no additional
derivative Born-Huang term hidden in(8).

## 3. Leading spectral stability before extracting higher coefficients

The global pointwise matter lower bound is H_m(theta)>=e(theta)I>=e_*I,
and the electric form is positive. A localized ground-band Hermite trial
at delta of width sqrt(g) gives E_j-e_*=O_j(g). Since e-e_* is bounded
below by a positive multiple of the squared distance to pi, these low states
are tight in xi=delta/sqrt(g). Away from a fixed chart about pi their
probability tends to zero. The electric form bounds the scaled derivative.

Inside that chart use(7). The other matter components have squared norm
O(g), from their fixed positive gap and the bounded g^2 C' term. The ground
component has an H^1 bound in xi and a bounded second moment. Rellich on
fixed intervals plus that moment gives strong L^2 compactness. The limiting
scalar form is

 H_slow=-2 partial_xi^2+(sqrt2/16)xi^2,                 (9)

whose eigenvalues are Omega(j+1/2), all simple. Lower semicontinuity of
the derivative and potential forms gives the min-max lower bound. Sampling
cutoff Hermite functions in the exact local ground band gives the matching
upper bound. Orthogonality survives strong compactness, so no hidden
multiplicity or extra low eigenvalue is inserted. This proves leading
fixed-index stability and the spectral windows of width O(g) used below.

For an explicit localization implementation, use a smooth scalar partition
equal to one near pi. Its IMS error is O(g^2), hence o(g), and the outside
piece has a fixed matter-energy gap. The local frame's derivative is bounded.
These estimates suffice for the leading compactness argument; an exponentially
small global boundary error is not needed for the higher-order proof below.

## 4. Higher coefficients from controlled quasimodes

Expand the actual ground-band energy, with a uniform Taylor remainder on
the fixed chart:

 e(pi+delta)=e_*+(sqrt2/16)delta^2
                         -(sqrt2/3072)delta^4+O(delta^6).

After delta=sqrt(g)xi, the scalar quartic perturbation enters at g^2.
For the jth eigenfunction of(9),

 <xi^4>_j=12sqrt2(2j^2+2j+1),
 -(sqrt2/3072)<xi^4>_j=-(2j^2+2j+1)/128.               (10)

Adding(8) gives the coefficient in(2). To control the remainder, take the
Hermite function plus its ordinary first quartic wavefunction correction,
with coefficient g. This correction is a finite sum of Hermite functions
because xi^4 connects finitely many levels. Multiply by a fixed smooth
chart cutoff. Derivatives of that cutoff act only on Gaussian tails and
are smaller than any power of g in all required norms.

In(7), let P be the constant ground matter label and Q=1-P. Its only
off-diagonal coupling is g^2 Q C' P. Add the Q-component

 -g^2 [Q(diag(e_a(delta))-e(delta))Q]^(-1)Q C' u phi_g. (11)

The inverse and all its fixed derivatives are bounded on the chart.
Its matter potential cancels the order-g^2 off-diagonal residual. Acting
with -2g^2 partial_delta^2 on(11) costs O(g^3), since the oscillator
wavefunction has two derivatives of size O(g^-1). First derivatives of
the inverse give smaller powers, and its second derivatives remain bounded.
The difference between the trial energy and e(delta) on this localized
state is O(g) in the needed weighted norms, giving another O(g^3) residual.
Coupling back through g^2 C' costs O(g^4). The scalar sixth-order Taylor
remainder and quartic/correction products are O_j(g^3).

Thus these normalized physical quasimodes have residual O_j(g^3) at the
energy in(2). Leading stability from section3 identifies one eigenvalue
in each separated O(g) window. The elementary spectral-distance inequality
then proves(2), rather than assuming that a formal power series converges.

Semiclassical stability and quasimode expansions are established machinery;
see [Simon1983](https://www.numdam.org/item/AIHPA_1983__38_3_295_0.pdf),
sections1-4. The paper's [1984 correction](https://www.numdam.org/item/AIHPA_1984__40_2_224_0.pdf)
requires care with parity in DEGENERATE harmonic levels. The slow ladder
here is one-dimensional and simple, and the coefficients/residual are
constructed explicitly above. No degenerate all-order theorem is imported.
The scalar coefficients also match the independently normalized large-q
Mathieu expansion: the auxiliary cosine-well operator has
q=-32sqrt2/g^2 and energy factor g^2/32. Global periodicity of that auxiliary
problem is not identified with the original matter bundle.

## 5. Why the hard cutoff scales as g^(-1/2) for this slow mode

The leading ground band in angle space is U(delta)u times a width-sqrt(g)
envelope. In electric space this means a shifted common envelope in

                         p=sqrt(g)(n+A_f).             (12)

For a smooth compactly supported p-envelope F, use the actual discrete
amplitudes

 psi_f(n)=(-1)^n g^(1/4)u_f F(sqrt(g)(n+A_f)).          (13)

Fixed Fourier conventions only change the common normalization. Riemann
sums give its norm limit. Taylor expansion of the finite hopping shifts,
or Poisson summation in the local frame, gives the scalar dual form
2p^2-(e''(pi)/2)partial_p^2. Compact p-envelopes approximate the oscillator
Hermite functions in that form domain. For every such envelope the exact
affine electric cutoff contains its support once S sqrt(g) is sufficiently
large. Min-max and the untruncated compression lower bound prove(4).
This uses a SMOOTH flux envelope; sharply cutting a Gaussian at its last
nonzero lattice point can create an uncontrolled boundary hopping cost.

For the stronger cutoff statement following(4), the constructed quasimodes
and their needed Fourier/weighted derivatives have uniform Schwartz bounds
in the scaled p coordinate. Projection inside |n|<=S-1 then has graph-norm
error bounded by C_M(S sqrt(g))^(-M), up to harmless fixed powers of g.
If S sqrt(g)>=g^(-epsilon), choose M large enough to make that error O(g^3).
The exact offsets are at most one, so this inner cap is physically allowed.
Applying min-max to the first j+1 projected quasimodes gives the upper bound;
compression gives the matching lower bound. This is a sufficient cutoff
condition, not a claimed optimal subleading error rate.

There is also an exact useful lower bound. On the whole angle circle,

 e(theta)-e_*>=c0(1+cos theta), c0=sqrt2/8.              (14)

It follows from |sin(4x)|<=4|sin x| with x=(theta-pi)/8.
Every physical finite-S component has |n|<=S because the chord field equals n.
The minimum of the compressed scalar1+cos(theta) on that Fourier chain is
1-cos(pi/(2S+2)). Positivity of electric energy and compression of(14) give

 E_j(g,S)-e_*>=c0[1-cos(pi/(2S+2))].                   (15)

Consequently if S sqrt(g)->0, even the normalized ground excess
(E0-e_*)/g diverges. A cutoff growing arbitrarily slowly can recover the
parent's rate-free floor while completely missing its slow spectral scale.

Full Gaussian electric-state recovery requires S sqrt(g)->infinity: any
finite limit leaves bounded p support, whereas the limiting oscillator
has a nonzero Gaussian tail outside every finite interval. This state
necessity is distinct from a complete classification of finite-support
spectral limits, which is not claimed here.

## 6. Observable meaning and scope

For the untruncated ground state, the scaled angle and flux distributions
converge to the ground oscillator in(9). Convergence of the positive kinetic
and potential energies follows from their separate lower bounds and equality
of the limiting total energy. It yields

 (1+<Re W_loop>)/g ->1/Omega=2^(1/4),
 g<E_l^2> ->Omega/8 for each of the four links.         (16)

The charge offsets change the next energy coefficient even though they
vanish at the leading flux scale. If they are wrongly deleted from the
electric Hamiltonian, the ordinary ground-band derivative term would be
3/16 instead of the correct5/16, giving23/128 in place of39/128 in(3).
That is an adverse comparator, not an alternative representation of(1).

This proves a slow GLOBAL holonomy gap of order g in one supplied charged
ring. It is not a bulk photon gap, a charged particle mass, a thermodynamic
dispersion, or a proof for the mixed four-orbital cubic model. In a cubic
weak-coupling box the normal photon-like oscillator directions have their
different electric scale1/g; this slow-loop result does not remove that
regulator requirement. The supplied Hamiltonian and reference charges remain
conditional choices, and no axiom update is forced.

## 7. Personal verification

Exact six-state CAR algebra verifies the whole Laurent-polynomial frame
identity U^-1 H_m U=z F+z^-1 F^T, z=exp(i delta/4), and [F,F^T]=0.
It gives C'00=5/16 and the first four g^2 coefficients39,35,27,15 divided
by128. Oscillator creation/annihilation matrices independently supply
the quartic moments. Full electric-field enumeration followed by integer
Gauss projection agrees exactly with reduced-coordinate matrices at S=1,2.

Five physical finite-cutoff spectra at g=.16,.08,.04,.02,.01 challenge
the expansion, with residuals below6.2e-15. At g=.01 the extracted ground
g^2 coefficient is approximately.30468487, approaching39/128=.3046875;
the gap's g^2 coefficient is approximately-.03126163, approaching-1/32.
The loop and electric observables approach(16). These finite comparisons
are not the proof of the remainder and do not certify an infinite cutoff.

Four deliberately insufficient cutoffs obey(15); their normalized ground
excess rises from about1.26 to65.5 while the unnormalized energy still
approaches the rate-free floor. Removing the charge offsets instead drives
the g^2 coefficient toward23/128, rejecting that wrong-model shortcut.
The adverse comparator is retained in the evidence. No scientific check
failed. All proof review and checks remain personal, pending independent
mathematical review before retention.
