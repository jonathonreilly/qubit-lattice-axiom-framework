# Field components are not detector polarizations

Direct parent derivation, October 12, 2026. Conditional linear mechanical
readout for the vector candidate; no strain likelihood or exclusion.

## Observation first, then the required bridge

The GW170814 primary paper compares network amplitudes and phases under
pure tensor, vector and scalar antenna responses. Section VII reports
tensor preferences while explicitly retaining a GR phase model. This makes
detector geometry a useful constraint on a reconstruction, but those model
likelihoods cannot be assigned to a newly proposed force law without its
readout and propagation assumptions. The comparison is exposed development
context, not a new independent test. Source details are in SOURCE_LEDGER.md.

## The local tidal result follows from the supplied force

The preceding matter extension supplies a=-grad(phi), phi=e.u. Consider
one small plane-wave component phi_s=f_s(t-n.x/c_s), with unit propagation
direction n, constant positive c_s, and slowly varying far-field amplitude
neglected across the apparatus. For nearby freely falling masses,

    delta a_i = T_ij xi_j,
    T_ij = -partial_i partial_j phi_s
         = -n_i n_j f_s''/c_s^2.

Thus T has rank at most one. For P=I-n n^T, P T P=0 and its transverse
trace-free projection is zero. For both field speeds propagating in the
same far-zone direction, replace f_s''/c_s^2 by the sum over s; the result
is still rank at most one locally. This uses a plane-wave/leading far-zone
limit, not an arbitrary superposition of different directions.

This conclusion is independent of whether u_s is transverse or longitudinal
as a vector field. Its scalar projection has spatial gradient parallel to
n. The transverse vector direction orthogonal to e is invisible to this
source and readout at linear order. Calling u a vector therefore supplies
neither a vector nor a tensor *tidal* response. The transverse trace-free
statement is elementary tensor algebra; it does not assume a null metric
wave or assert a full relativistic polarization classification.

## Restricted mechanical arm response

Supply free, initially stationary masses and a simultaneous Euclidean
length measurement. This is an extra readout model, with no photons,
suspensions, cavities, clocks or electronics. Work to first order in phi.
Take phi=A exp(-i omega t+i omega n.x/c), omega>0. The harmonic displacement
of a test mass is

    delta x = i n phi/(omega c),

up to the freely chosen constant and linear homogeneous motions. Let an
arm of unperturbed length L point along a, and mu=n.a. The fractional
length harmonic from its two endpoints is exactly, at this linear order,

    delta L/L = -phi(x)/c^2 mu^2 exp(i z/2) sinc(z/2),
    z=omega L mu/c,    sinc(y)=sin(y)/y, sinc(0)=1.

Here phi(x) is evaluated at the common unperturbed base endpoint, and the
two endpoint displacements are compared at the same coordinate time.
The identity follows from their difference exp(i z)-1, not from truncating
the wave phase. It is not an optical round-trip transfer function.

For zero displacement and velocity at t=0, replace the harmonic factor
exp(-i omega t) by exp(-i omega t)-1+i omega t. Direct integration of the
endpoint accelerations provides an independent check of this response.

For equal arms a,b in the long-wavelength limit omega L/c << 1, define
D=a a^T-b b^T. Its trace is zero. The differential mechanical response is

    h_mech = -F(n) sum_s phi_s/c_s^2,
    F(n)=D:(n n^T)=(n.a)^2-(n.b)^2.

With the unnormalized breathing matrix B=I-n n^T, D:B=-F(n).
Longitudinal and breathing *angular patterns* are consequently degenerate
up to amplitude and sign in this restricted long-wavelength readout. Their
tidal tensors remain different. The exact endpoint factors depend on arm
direction and frequency; a frequency-independent F is not the finite-arm
response. No finite-frequency degeneracy theorem for optical or metric
polarizations is claimed.

## Network propagation prevents an unwarranted likelihood shortcut

For detector A at x_A with orientation factor F_A and arms short compared
with both wavelengths, a same-direction two-speed monochromatic wave has

    h_A(omega) = -F_A sum_s A_s exp(i omega n.x_A/c_s)/c_s^2.

At fixed direction and frequency the two column vectors are
F_A exp(i omega n.x_A/c_s)/c_s^2. One speed gives a rank-one response space;
two distinct speeds give rank at most two and generically rank two. After
aligning every site using only c_L, the c_T column retains relative phases.
If the speeds coincide, one amplitude vanishes, or the projected baselines
have appropriate degeneracies, the rank can fall to one. Local rank-one
tidal geometry does not imply a rank-one two-speed network transfer.

Consequently the published single-propagation scalar antenna comparison
is motivation for a test, not a computed Bayes factor against this model.
The previous power-calibrated candidate has c_T/c_L about .7185, so this
distinction matters unless one component is absent or outside the observed
time window. Emission history, distance and propagation determine that
window; no cosmological source history has been supplied here.

## What this block decides

Under the supplied scalar matter coupling, three causal field components
do not generate transverse trace-free plane-wave tidal forces. Promoting
the static construction to an observed-gravity candidate therefore needs
an explicit additional matter/metric readout or a demonstrated scalar
network fit with its actual propagation. Merely matching circular radiated
power does not fix this deficiency. A new coupling could change the result
and must be derived and checked, rather than silently inherited.

All checks here use synthetic geometries. No optical strain prediction,
binary merger waveform, GR-derived mass transfer, calibrated likelihood,
empirical acceptance, whole-class no-go or TOE is claimed.
