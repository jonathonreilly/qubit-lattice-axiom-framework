# Scalar endpoint registration from waves: what the observation must supply

Status: exploratory conditional-support. Personally derived by root after the
preparation bridge; no raw GW data, empirical fit or new action is introduced.
This returns to the scalar normalization gap in BLOCK01_DERIVATION_v5.md.
Known standard-siren transport is prior art. The purpose is to test whether it
actually supplies the missing registration, rather than assume that it does.

## 1. A supplied scalar class implies a leading tensor transport law

Keep the candidate, signature(-+++), c=1,

 S=int sqrt(-g)[F R/2-omega(F)(partial F)^2/(2F)-V(F)]+S_m[g,psi].

Assume smooth F>0, 2omega+3>0 on the propagation region. F_star>0 is a
reference constant, not an inferred scale. The conformal transformation

 gE=(F/F_star)g,
 (dphi/dF)^2=F_star(2omega+3)/(2F^2),
 VE=F_star^2 V/F^2                                           (1)

gives Einstein gravity plus a canonical scalar there. Matter couples to
(F_star/F)gE; neither a physical frame change nor a measurement identification
is implied. The scalar potential and boundary solution remain unknown.

Consider weak waves about a slowly varying, on-shell background, away from
material high-frequency stresses, caustics and singular F charts. Their
frequency must dominate curvature, background-gradient and relevant mass
scales. Work through geometric-optics amplitude order only. In Einstein
variables the derivative-order scalar source in the perturbed stress is

 i A_phi [b_mu k_nu+b_nu k_mu-gE_mu_nu(b dot k)], b=dphi.      (2)

A tensor polarization e^{mu nu} obeys e^{mu nu}k_nu=0 and
e^{mu nu}gE_mu_nu=0, so its contraction with(2) vanishes. In harmonic gauge
the derivative-of-metric term in delta(box phi) also vanishes; the remaining
metric/scalar mixing involves background second derivatives and is lower
order. Thus in this specific class a propagating scalar need not be set to
zero to obtain the leading tensor transport. This statement is not valid
for arbitrary derivative-coupled scalar actions or beyond this expansion.
It also does not eliminate scalar radiation energy from the binary source.

The Einstein tensor amplitude A is the dimensionless transverse strain; the
conformal perturbation adds a trace and does not change this amplitude.
Its ray current obeys div_E(A^2 kE)=0. Let O^2=F/F_star, with the same phase
covector and kE^mu=O^-2 k^mu. The four-dimensional divergence transformation
div_E X=O^-4 div_g(O^4 X) therefore gives

 div_g(F A^2 k)=0,
 d/dlambda log A=-[div k+d/dlambda log F]/2.                 (3)

With beam geometry separately known, propagation multiplies the amplitude
relative to geometric dilution by sqrt(F_source/F_observer). Only local
endpoint values enter at this order; an assumed homogeneous cosmological
F(t) may not replace the actual emitting/receiving environments. Equal
endpoint values cancel this effect even if F varies in the interior. This
is a conditional statement, not a derivation that screening enforces equality.

## 2. Frequency evolution does not automatically calibrate source amplitude

Derive a deliberately restricted source contract before using a distance
posterior. A circular, slowly evolving Newtonian binary has fixed masses
M=m1+m2, mu=m1*m2/M and a constant attractive orbital coupling Gc. Permit
Gc to differ from the local tensor coupling GT=1/(8pi F_source). Write

 r^3 Omega^2=Gc M,
 E=-mu(Gc M)^(2/3) Omega^(2/3)/2,
 K=GT mu(Gc M)^(2/3).                                      (4)

The leading tensor quadrupole has Iij=mu(ri rj-deltaij r^2/3).
Direct differentiation gives I'''ij I'''ij=32mu^2 r^4 Omega^6.
The linear spin-two flux GT I'''ij I'''ij/5 and transverse wave
2GT I''ij/R then give

 PT=(32/5)GT mu^2(Gc M)^(4/3) Omega^(10/3),
 H_local=4K Omega^(2/3)/R.                                  (5)

H is the intrinsic amplitude after inclination/polarization projection is
removed; a detector strain is not automatically H. These are leading source
approximations, not a derivation of strong-body sensitivities or full waveforms.
Let additional positive orbital-energy loss be PX=eta(Omega)PT, eta>=0,
with no energy injection and no unmodelled changing binding energy. Energy
balance, including PX, gives

 dotOmega=(96/5)K Omega^(11/3)(1+eta).                       (6)

Thus a local scalar channel can change the chirp even when(2) shows that
propagating scalar waves do not mix into tensor amplitudes at leading order.
Setting eta=0 would be a source assumption, not a consequence of(3).

For constant redshift z, Omega_o=Omega/(1+z), Kz=K(1+z)^(5/3),
and independently calibrated electromagnetic luminosity distance DL, the
ideal tensor quantities satisfy

 H_o=4Kz Omega_o^(2/3) sqrt(rho)/DL,
 dotOmega_o=(96/5)Kz Omega_o^(11/3)(1+eta), rho=Fs/Fo.
 D_chirp=(5/24)dotOmega_o/(H_o Omega_o^3)
        =DL(1+eta)/sqrt(rho).                              (7)

Geometric lensing/beam, photon conservation, time, inclination and detector
calibration enter this mapping. Evolution of the redshift during a chirp,
eccentricity, tides, higher-order terms, absorption, variable sensitivities
and environmental energy exchange require their own correction/bound.

The orbital coupling and unknown mass combination cancel from(7); equality
Gc=GT is not required. But the energy-loss fraction does not cancel.
For constant unknown eta, the entire leading tensor waveform is invariant
under

 Kz -> Kz/a, 1+eta -> a(1+eta), rho -> a^2 rho,              (8)

for positive a with the new eta nonnegative. Initial frequency/phase and DL
are held fixed. This is nonidentifiability in the stated leading observable
contract. It is not a proof that every transformed triple extends to a
globally consistent scalar action or that higher-order/other observations
cannot break it. No finite dataset is needed to exhibit this ambiguity.

Even a dipole-shaped term does not fix the constant ambiguity: if
eta=eta0+b(Omega/Omega_ref)^(-2/3), transformation(8) extends by b->a b.
Frequency shape can constrain b/(1+eta0); it does not alone identify eta0.
No particular scalar-charge or sensitivity law has been selected here.

## 3. A bounded observation can register relative scalar charts

If a separate argument or observation certifies eta in [eta_lo,eta_hi], and
DL/D_chirp is in [q_lo,q_hi] with all bounds positive, then

 (q_lo(1+eta_lo))^2 <=rho<=(q_hi(1+eta_hi))^2.               (9)

For eta>=0 without a finite upper bound, the lower bound rho>=q_lo^2
survives but no finite upper bound follows. These are deterministic interval
bounds, not confidence intervals. They require every error in(7), including
source/travel/readout corrections, to be in the stated intervals.

In the static inverse, Fi=Ci exp(xi). If endpoints are genuinely identified
with chart positions xs,xo, then

 log(Cs/Co)=log rho-xs+xo.                                 (10)

Equations(9)-(10) can therefore constrain overlap without choosing the
integration constants equal. Uncertain endpoint registration adds its own
interval widths. They do not fix a common absolute normalization: a common
positive rescaling of all F leaves the ratios invariant, unless a separately
calibrated source/matter response supplies the dimensional anchor.

This is a route contract, not an observed registration. We have not obtained
the needed independently calibrated quantities. A GR distance posterior has
already selected a source/propagation model and cannot be reused as a
model-independent primitive to test those same assumptions.

## 4. Finite wavelength: a controlled proxy prevents overextending(3)

The exact one-dimensional positive-coefficient wave action

 S_h=int dt dx F(x)(h_t^2-h_x^2)/2

is a propagation proxy, not a claim that arbitrary F(x) on Minkowski space
solves the coupled gravitational background equations. For a monochromatic
wave of frequency k>0, let u=sqrt(F)h and L=log F. Then

 u''+[k^2-Q(x)]u=0, Q=(sqrt F)''/sqrt F=L''/2+L'^2/4.       (11)

Assume real F>0, C2 and constant outside [0,l], so Q has compact support.
For a unit outgoing Jost solution f_+(x)=exp(ikx) on the right,

 f_+(x)=exp(ikx)+int_x^l sin(k(y-x)) Q(y)f_+(y)dy/k.        (12)

With J=int|Q|, Gronwall gives |f_+|<=exp(J/k). On the left write
f_+=A exp(ikx)+B exp(-ikx). The integral then implies

 |A-1|,|B| <=m=J exp(J/k)/(2k).                            (13)

The real-potential Wronskian gives |A|^2-|B|^2=1. Unit incidence has
t=1/A, r=B/A, hence |t-1|<=m, |r|<=min(m,1) and
|t|>=1/sqrt(1+m^2). Physical strain transmission is

 t_h=sqrt(F_left/F_right)t.                               (14)

This supplies an explicit finite-frequency deviation bound for the proxy
only if J is bounded. Endpoint values alone do not bound J. Different smooth
interiors with the same endpoints can reflect differently; global F scaling
leaves Q and t_h unchanged. The proxy is a necessary caution about neglecting
gradient scales, not a finite-wavelength error certificate for a real siren.

## 5. Sources, tests and next discriminating measurement

Known prior art was inspected before this block: Dalang, Fleury and Lombriser,
https://arxiv.org/html/1912.06117v3, sectionsIII.3.3andIII.4, establish endpoint
transport in geometric optics. Dalang and Lombriser,
https://arxiv.org/html/1906.12333, section5.1, analyze how screened endpoint
values affect this inference. These results are not campaign discoveries.

Dalang, Fleury and Lombriser, https://arxiv.org/html/2009.11827v3,
sectionIV.2.1, display the vanishing scalar-to-tensor transverse projection
for the luminal scalar class; this agrees with the direct Einstein-frame
calculation above. Bernard, Blanchet and Trestini,
https://arxiv.org/html/2201.10924, abstract and sectionsIII.3/IV through the
source moments, provide primary background for separate scalar radiation and
source sensitivities. Their full post-Newtonian calculation was not reproduced.
Read scopes and source identities are in SCALAR_SIREN_INTAKE_v1.json.

The frozen synthetic controls check polarization projection, quadrupole
normalization, redshift/source ambiguity, interval registration and exact
proxy scattering against a separate direct h equation. No measured data are
accessed. Successful controls do not validate the supplied scalar class.

Next useful physical obligation: bound source energy loss or its scalar-charge
law with independent information, and establish a geometric distance and
calibrated tensor amplitude. First challenge whether a weak-field material
response or additional polarization can supply that missing bound without
assuming the desired potential, compact-body state or cosmological history.
Do not open a GW posterior and count its built-in GR source law as derivation.
