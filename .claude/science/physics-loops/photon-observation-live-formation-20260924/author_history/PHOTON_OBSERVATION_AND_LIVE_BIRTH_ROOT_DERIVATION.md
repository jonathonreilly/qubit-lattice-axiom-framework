# Photon observations and the response to actual live formation

Root personal derivation, fifth campaign, 2026-09-24. Conditional candidate;
not independently checked at authorship. Source identities are in SOURCE_PINS.
The two parts below have different scopes. Part I translates the supplied
harmonic dispersion into an observational hypothesis. Part II derives exact
initial responses of the full compensated rotor matter/field generator. Neither
identifies its modes with observed photons, selects its parameters, or replaces
the full process by a field-only postbirth law.

## I. A definite observable if the harmonic modes are photons

The pinned weak-field note gives two equal transverse frequencies

    omega(q) = (c/a) sqrt(D(aq)),
    D(k) = 4 sum_(i=1)^3 sin^2(k_i/2).

Here c,a and the weak-field coupling are supplied. q is the physical spatial
wavevector only after an additional length identification. c is a frequency-
length conversion supplied by the chosen Hamiltonian/time interpretation.
Use a narrow packet centered at q != 0 away from a Brillouin boundary.
Differentiating this formula, rather than using phase velocity, gives

    v_i/c = sin(a q_i)/sqrt(D(aq)),
    |v|^2/c^2 = sum_i sin^2(aq_i)/D(aq) <= 1.             (1)

The inequality is exact since sin^2(k_i)=4 sin^2(k_i/2)cos^2(k_i/2).
It is a statement about these harmonic lattice modes, not every signal speed
of the original microscopic theory. The two polarizations have the same
dispersion; no polarization splitting follows from this quadratic model.

Let x=a|q|, n=q/|q|, A4=sum_i n_i^4 and A6=sum_i n_i^6. Then

    1/3 <= A4 <= 1,
    omega/(c|q|)=1-A4 x^2/24
                   +(A6/720-A4^2/1152)x^4+O(x^6),
    (n dot v)/c=1-A4 x^2/8+O(x^4),
    |v|/c=1-A4 x^2/8+O(x^4),
    (v-(n dot v)n)/c=-(x^2/6)(n^3-A4 n)+O(x^4).       (2)

The direction of the packet velocity is generally not n. Replacing n by
the ray direction in the leading A4 term changes only the fourth-order
remainder. The anisotropy cannot be dropped or advertised as birefringence.

A sufficient explicit small-x control is, for 0<x<=1,

    |(n dot v)/c -(1-A4 x^2/8)| <= x^4/40,
    ||v|/c -(1-A4 x^2/8)| <= x^4/20.                   (3)

Proof: d=D(xn)/x^2=1-A4 x^2/12+r_d with 0<=r_d<=x^4/360;
b=sum n_i sin(xn_i)/x=1-A4 x^2/6+r_b with 0<=r_b<=x^4/120.
Also 11/12<=d<=1. Taylor's theorem gives
|(1+u)^(-1/2)-(1-u/2)|<=u^2/2 on -1/12<=u<=0.
Thus |d^(-1/2)-(1+A4x^2/24)|<=7x^4/1440. Multiplying b
gives an error at most (1/144+7/1440+1/110)x^4 < x^4/40.
The transverse component is at most (21/110)x^2, and n dot v/c>=5/6.
The difference between speed and its radial component is at most
(3/5)(21/110)^2 x^4; adding x^4/40 is less than x^4/20.
This proves (3) in wavevector units. Replacing q by measured energy adds
another controlled asymptotic conversion, not an unchanged bound constant.

Supply the further photon identification E= hbar omega and the low-energy
calibration c=c_observed. Then (2) becomes

    v_ray(E)/c = 1 - [a^2 A4(n)/(8 hbar^2 c^2)] E^2
                    +O((a E/(hbar c))^4).              (4)

For the convention used by the cited timing analyses,

    v(E)/c = 1 - (3/2)(E/E_QG,2)^2,
    E_QG,2(n) = sqrt(12) hbar c/[a sqrt(A4(n))].         (5)

This is a parameter conversion into an existing likelihood, not a new fit.
With a constant lattice orientation and spacing in an approximately static
laboratory/galactic path of length L, the leading delay is

    Delta t = (L/c) [a^2 A4/(8 hbar^2 c^2)](E_h^2-E_l^2). (6)

Three energies would give equal Delta t/(E_h^2-E_l^2) if the compared emission
times and other propagation effects are controlled. The sign, quadratic
energy power, shared polarization dispersion and cubic directional factor
are restrictions of this hypothesis. Its overall size is not predicted:
the present framework does not select a, the orientation, the time conversion,
or a photon source/detector identification. Making a smaller always hides
this effect beneath any finite timing bound. Agreement with a bound therefore
does not favor this model over ordinary electromagnetism.

For a cosmological path, (6) needs an additional transport law. Only if proper
a and the relevant orientation coefficient stay constant, photons redshift
as E(z)=E_observed(1+z), and the supplied FLRW propagation law applies, replace
L/c by integral_0^z (1+z')^2/H(z') dz'. An expanding comoving lattice with
different a(z) gives a different integrand. None of these cosmological premises
has been derived in this campaign.

### Primary observational comparison, without a raw-data reanalysis

The MAGIC collaboration's Crab pulsar analysis (arXiv:1709.00346, equation 1
and Table 6, including systematic uncertainties) reports the quadratic
subluminal bound E_QG,2>5.9e10 GeV at 95% confidence. Its profile likelihood
uses a pulse/spectrum and detector-response model with nuisance parameters;
this is not an assumption-free bound on arbitrary intrinsic emission lags.
Under those observational and the preceding physical identifications, (5)
gives a sqrt(A4)<sqrt(12) hbar c/(5.9e10 GeV). This is an archival primary
benchmark, not a claim to the strongest currently available limit.
https://arxiv.org/pdf/1709.00346

The LHAASO collaboration's GRB221009A analysis (arXiv:2402.06009v2, equations
1-8, Table 1 and sections III-IV) reports 6.9e11 GeV for the quadratic
subluminal ML/MINOS limit, with 7.2e11 for its calibrated variant and 4.7e11
for CCF. We use the stated 6.9e11 benchmark, without mixing these analyses.
It uses z=.151, a supplied flat cosmology, a fitted evolving afterglow,
background/detector response and EBL treatment. Conditional on that analysis
and the cosmological extension just stated, substitute 6.9e11 in the same
conversion. No new statistical confidence coverage is claimed.
https://arxiv.org/html/2402.06009v2

For one fixed sightline the anisotropic theory has a constant A4 and can use
the corresponding one-parameter timing coefficient. This does not import an
isotropic multi-source bound or marginalize over unknown lattice orientation.
The orientation-independent necessary upper bound on a is sqrt(3) times the
bound on a sqrt(A4). Numerical conversions are separate root controls.

## II. What the original formation instrument actually does initially

Use the pinned common compensated rotor model on a fixed finite simple
bipartite graph. Orient every edge from A to B; changing stored orientations
is a coordinate change. All A sites are initially plus, all B sites vacant,
and div E=0. Denote that entire matter sector by P0, allowing arbitrary field
coherences. The full generator is

    L rho=-i[h,rho]+kappa sum_j D[B_j]rho,
    h=K D(q,E)+delta H4^C,
    D(q,E)=sum_(a,b~a) 1_(q_b=0) [E_ab^2-q_a E_ab],
    B_(ab,sigma)=P j_(ab,sigma) F_a P.                  (7)

The coherent version sums sigma=+/- for a fixed edge. The full instruments
are different. We retain the stated one and never replace its postbirth
matter state or its Hamiltonian by the initial field Hamiltonian.

For each a, a birth target b and a distinct outward-hop destination c,
the initial path moves the original plus record from a to c and then creates
(sigma,-sigma) at (a,b). Its rotor field kick is

    d_(a,b,c,sigma)=sigma e_ab-e_ac.                    (8)

Each unit-shift path has amplitude one. For a fixed resolved mark, different
c give orthogonal final charge words; the two sigma words are also orthogonal.
Consequently tracing out matter after ONE infinitesimal formation source
gives the same field map for resolved and coherent marks:

    Tr_m D_form(P0 rho_field)
       = kappa sum_(a,b,c!=b,sigma)
           [U_d rho_field U_d^* - rho_field].           (9)

Equation (9) is an exact initial derivative of the full process, not a closed
field semigroup at later times. In particular it does not erase actual output
coherences in the complete matter-field density.

The initial loss is the scalar

    lambda = 2 kappa sum_a z_a(z_a-1),
    Pr(no first birth by t)=exp(-lambda t).             (10)

The Hamiltonian conserves number; the initial-number P sector fixes exactly
this matter word. The no-event block is therefore exp(-lambda t) times its
unitary field evolution. All other number sectors are orthogonal. Relative
to that unitary trajectory, the full trace-one state's trace distance is
exactly 2(1-exp(-lambda t)). This global distinguishability is not a photon
absorption probability or an observable-local error estimate.

### Magnetic observables, electric drift and noise

Every rotor field shift commutes with every other such shift. Hence every
bounded function of the link angles (in particular a Wilson loop W_v)
commutes with B_j and B_j^*, on the full matter-field space. Therefore

    D_form^*(W_v)=0.                                  (11)

The same holds for bounded periodic angle functions. H4^C contains finite
words of field shifts and matter operators and also commutes with W_v, so
L^*W_v=iK[D,W_v]. This identity keeps the q-dependent electric term.

On finite electric words, (9) also gives exactly

    P0 D_form^* E_ab P0=-2 kappa (z_a-1) P0,
    d Cov(E_e,E_f)/dt |_formation,t=0
             =4 kappa (z_a-1) delta_ef.               (12)

The covariance identity includes subtraction of the evolving mean and is
valid for any initial field state with the required moments. In counting,
the birth-target kicks cancel in the first moment; the outward kicks do not.
Each edge occurs 2(z_a-1) times in either role in the second moment. Every
off-diagonal product has a sigma factor whose two signs cancel.

The drift vector in (12) is a graph gradient: assign potential
-2 kappa(z_a-1) at a and zero at B. Its projection onto cycles is zero.
On a z-regular graph let P_T be any orthogonal transverse field projection,
for example with harmonic windings removed. Then

    d Cov(P_T E)/dt |_formation,0=4 kappa(z-1)P_T,
    d <K |P_T E|^2>/dt |_formation,0
                           =4 kappa K(z-1) rank(P_T). (13)

Adding any bounded periodic magnetic potential to this test observable
does not change (13). It is an exact field-observable injection rate. It is
NOT the change of the actual full Hamiltonian h, whose q-dependent D and
matter-field H4 also change at a birth. Previous full-system energy results
must not be replaced by this field diagnostic.

For the prepared harmonic description a real normalized transverse oscillator
has H_mode=K E_mode^2+J lambda_k A_mode^2 and omega_k=2sqrt(KJ lambda_k).
Its instantaneous formation contribution to the harmonic number diagnostic
is 4 kappa K(z-1)/omega_k. This interpretation presupposes the chart and
oscillator identification; it is not an established measured photon count,
stationary radiation spectrum, long-time heating law or background bound.

### Initial change in the wave response, including the new matter

There is also an exact initial acceleration identity. Let G^* O=i[h,O]
and let W_v be a divergence-free integer loop shift. On a regular graph,

    P0 (L^*)^2 W_v P0
       = P0 (G^*)^2 W_v P0 - r_B P0 G^*W_v P0,
    r_B=4 kappa z(z-1).                               (14)

Thus r_B=24kappa for the cube and 120kappa for a simple three-dimensional
cubic torus of degree six. The common rotor Hamiltonian, not an initial-sector
postbirth substitute, is essential in this calculation.

Proof: [D,W_v]=W_v sum_e 1_(q_b=0)(2v_e E_e+v_e^2-q_a v_e).
After a path (8), both B destinations b,c are occupied. The kick is supported
only on edges incident to those B sites, so 1_(q'_b=0)d_e=0. The total rate
at which a given B vertex becomes occupied is r_B: every adjacent A supplies
4(z-1) paths counting both signs and the two destination roles. For a fixed
edge, the initial derivative of 1_(q_b=0)q_a is
-r_B-2kappa(z-1)(z-2); the second term counts sigma-minus events at a with
both B destinations different from this edge's B endpoint. The extra scalar
linear term vanishes when summed against v, since div v=0 implies sum_e v_e=0.
Equation (9) applied to this q-diagonal expression therefore gives
P0 D_form^*[D,W_v]P0=-r_B P0[D,W_v]P0. Now use (11):
(L^*)^2W_v=(G^*)^2W_v+D_form^*G^*W_v. This proves (14).
The proof is on finite electric words, with extension to densities only when
the moments required for these derivatives exist. It is not a uniform bound
on an unbounded observable over every trace-class initial state.

The first two Taylor derivatives around the initial background resemble a
damped wave response. Equation (14) does NOT prove a damped Maxwell equation
for finite duration, an exponential attenuation coefficient, a photon mass,
or permission to constrain kappa by an astronomical flight time. Further
derivatives include the born matter sectors and their Hamiltonians.

## What the actual observational bridge still requires

The old weak-field source suppresses microscopic formation via beta~epsilon^6.
The current common compensated law instead keeps kappa fixed and retains
matter after births. The two limits cannot be identified by matching their
pre-first Hamiltonians. Equations (9)-(14) expose concrete response terms that
any simultaneous photon theorem must handle. The pre-first torus Hamiltonian
has J=2delta and c=2a sqrt(2Kdelta) in hbar=1 frequency units, but this does not
calibrate physical distance/time or establish that finite-g, finite-spin and
formation errors are smaller than the very small O(a^2 q^2) timing effect.

The next physical obligation is a controlled source-to-detector response for
the full dynamics in a specified matter state over a specified duration,
including scattering/noise and identification of measured energy and clocks.
After that, a prediction needs independent parameter selection/calibration
and comparison with an observational likelihood retaining source effects.
Until then Part I is a conditional constraint on a photon hypothesis, and
Part II is model mathematics that helps test that hypothesis. Neither is
empirical confirmation of this framework or a TOE completion.
