# Reciprocal matter, radiation and mechanical readout of a local vector model

Date: 2026-10-12.
Claim type: bounded_theorem
Status: conditional-support
Audit authority remains the independent audit lane.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: supplied linear vector action, nonrelativistic universal mass coupling and restricted mechanical readout
hypothetical_axiom_status: candidate assumptions explored, no framework premise adopted
admitted_observation_status: primary observations motivate questions; no empirical likelihood or fit enters the proof
claim_type_reason: conditional linked conservative, radiative and readout consequences with complete derivations
proposal_allowed: false
proposal_allowed_reason: relativistic matter, optical response and observational bridges remain open
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

Primary runner: [local_vector_matter_readout_2026_10_12.py](../scripts/local_vector_matter_readout_2026_10_12.py).
Paired [canonical cache](../logs/runner-cache/local_vector_matter_readout_2026_10_12.txt).
The complete supplied field action is

    L_field = [alpha |u_t|^2 - (1/N)|grad u|^2
               - (1/D-1/N)(div u)^2]/(8 pi G),
    L_source = -rho e.u,   phi=e.u,
    alpha u_tt - Delta u/N - (1/D-1/N)grad div u = -4 pi G rho e.

Here 0<D<=N, alpha>0, G>0, and e is a fixed unit vector. The local
energy density is the sum of those three positive quadratic terms divided
by8piG. For a propagating polarization s its outgoing flux is
alpha c_s |u_t,s|^2/(4piG). The two speeds are1/sqrt(alpha N) and
1/sqrt(alpha D). These formulas are supplied candidate definitions, not
observed gravitational identifications. Their causal/static construction,
including the complete retarded Green tensor, is proved in the
[local vector response note](LOCAL_VECTOR_HOMOGENEOUS_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md).
This packet does not use any fitted nonlinear response or accepted framework
primitive as a hidden premise.

The following two constituent derivations are preserved in full, including
the resolved network-rank clarification. Source ledgers and exact input/run
history are under the [recovery packet](../.claude/science/physics-loops/local-vector-matter-readout-20261012/HANDOFF.md).
The names DIRECT_MATTER_RADIATION and DIRECT_READOUT there identify their
original source paths. The original source ledgers supply primary links;
no pulsar or interferometer likelihood is transferred into this theorem.

## A minimal matter coupling makes the linear response radiatively testable

Direct parent derivation, October 12, 2026. Conditional candidate extension;
no empirical fit or relativistic gravitational theory is claimed.

### Premises and energy exchange

Take the already checked constant vector action with G>0, alpha>0,
0<D<=N, constant unit e, mu=1/N, beta=1/D-1/N and phi=e.u. Add matter
with positive inertial masses, L_m=sum m v²/2, and coupling -integral rho phi.
Smooth finite mass profiles are assumed when discussing self energy; point
centres describe exterior multipoles only. This is a new nonrelativistic
matter assumption, not something established by the static susceptibility.

Matter then obeys m a=-m grad phi. With J the mass current and
rho_t+div J=0, integration by parts gives

    dE_field/dt = -integral rho phi_t,
    dT/dt = -integral J.grad phi,
    d(integral rho phi)/dt = integral rho phi_t + integral J.grad phi.

Thus field + kinetic + interaction energy is conserved for an isolated
regularized system. The positive field energy alone does not bound the full
Hamiltonian below. In the static limit E_field=-integral rho phi/2;
eliminating the field gives the usual half-counted interaction energy.

### Conservative equatorial orbit and a vertical test

The pair potential is

    U(R) = -G m1 m2 [N+D+(N-D)(e.Rhat)²]/(2R).

It is even in R and translation invariant. Its force need not be central;
the fixed e supplies an external orientation, so full rotational invariance
is not asserted. In the plane perpendicular to e the force is central and

    G_eq = G(N+D)/2,
    Omega² = G_eq (m1+m2)/a³,
    E_orbit = -G_eq m1 m2/(2a).

For relative vertical displacement z at fixed cylindrical radius a,

    U(a,z) = -G m1 m2 (N+D)/(2a)
              +G m1 m2 (3D-N)z²/(4a³)+O(z^4).

Therefore the leading vertical frequency is

    nu_z² = G(m1+m2)(3D-N)/(2a³),
    nu_z²/Omega² = (3D-N)/(N+D).

An equatorial circular orbit is vertically restoring for N<3D, marginal
at N=3D at this order, and linearly unstable for N>3D. This is a statement
about this fixed-direction matter model, not all gravity completions.

### Leading radiation from the independently fixed source

Let I_ij=integral rho x_i x_j and d_i=integral rho x_i. Work with a compact
slow source, a Omega/min(c_T,c_L)<<1, weak damping and a wave zone much
larger than both wavelengths. Total source mass is conserved. The leading
conservative centre of mass is at rest, so d_i is constant at that order.
Equal-mass antipodal circular sources give an exact zero dipole by symmetry.
We do not assert exact constancy of the matter centre alone at all orders
when momentum can reside in the field.

At a nonzero fixed Fourier frequency the full Green tensor's two front
terms are O(1/r). Its intervening term is O(1/r²): its time integral has
endpoints proportional to r, divided by r³, and integration by parts costs
one nonzero frequency. The DC field is different and must retain that
intervening contribution; discarding it in a static calculation is wrong.
The radiative pieces for direction n are consequently

    u_s = -G/(2 alpha r c_s^4) P_s(n)e n_i n_j I''_ij(t-r/c_s),
    s = T,L;  c_T²=1/(alpha N), c_L²=1/(alpha D).

This follows by Taylor-expanding the retarded density integral:
integral rho(x,t-r/c+n.x/c)dx = M+n.d'/c+n_i n_j I''_ij/(2c²)+...
Its first two terms have no leading radiative time derivative under the
stated conservation assumptions. The trace of I must not be removed
without cause; its derivative vanishes for the circular example below.

The radial energy flux is

    S.n = alpha/(4 pi G) [c_T |u_t,T|²+c_L |u_t,L|²]+o(r^-2).

The two projectors are orthogonal even at different retarded times. The
leading positive, time-averaged power per solid angle is

    dP/dOmega = G/(16 pi alpha) {
      [1-(e.n)²] <(n_i n_j I'''_ij)²>/c_T^7
          +(e.n)² <(n_i n_j I'''_ij)²>/c_L^7 }.

Periodic averaging makes the separate retarded origins immaterial. This
is a leading multipole result, not the exact power at arbitrary speed or
an assumption that these fields are the observed tensor waves.

### Circular source and a fixed comparison

For separation a, reduced mass m_red and an orbit in the xy plane with e=z,

    <(n_i n_j I'''_ij)²> = 8 m_red² a^4 Omega^6 sin^4(theta).

The two exact angular integrals are
integral sin^6(theta)dOmega=64 pi/35 and
integral cos²(theta)sin^4(theta)dOmega=32 pi/105. Therefore

    P_vec = G m_red² a^4 Omega^6/alpha
                [32/(35 c_T^7)+16/(105 c_L^7)].

In this adiabatic circular approximation, P_orb dot/P_orb=-3P_vec/(2|E_orbit|).
This energy-balance relation uses the explicitly supplied matter/clock
model; a pulsar arrival-time prediction requires much more.

For a comparison only, supply the usual leading GR circular quadrupole
formula for the same trajectory, inertial masses and equatorial static
calibration: P_GR=(32/5)G_eq m_red² a^4 Omega^6/c_EM^5. This formula is
not used to derive P_vec. Put q=N/D>=1; then

    P_vec/P_GR = (c_EM/c_L)^5 (6q^(7/2)+1)/(21(q+1)).

If the extra calibration c_L=c_EM is made, the isotropic q=1 result is1/6.
Equality with the GR comparator requires 6q^(7/2)+1=21(q+1), with a
unique q>1: its ratio has positive derivative for q>=1. The runner brackets
the root using the exact polynomial 6x^7-21x²-20 with x=sqrt(q). Matching
this one comparator consumes a calibration; it is not a successful test.
It also fixes unequal wave speeds, a polar/equatorial static-potential
ratio 2q/(q+1), and vertical-frequency ratio (3-q)/(1+q).

### Observational boundary

Binary-pulsar timing motivates radiation as an independent constraint on a
static reconstruction. The 2016 primary analysis of PSR B1913+16 reports
an orbital-decay comparison close to its GR prediction, but the masses,
timing delays and Galactic correction are part of that interpretation.
See the source ledger. No published mass or corrected ratio is fitted or
tested here; that binary is eccentric and strongly self-gravitating, while
this calculation uses a weak circular example. No sigma exclusion follows.

The model still lacks relativistic matter, clock and light propagation,
strong-body sensitivities, a dynamical background direction, nonlinear
response, lensing and a tensor-radiation identification. Those are explicit
targets. The useful gain is a linked set of conservative and radiative
predictions from one new matter coupling, rather than separate fitted laws.

## Field components are not detector polarizations

Direct parent derivation, October 12, 2026. Conditional linear mechanical
readout for the vector candidate; no strain likelihood or exclusion.

### Observation first, then the required bridge

The GW170814 primary paper compares network amplitudes and phases under
pure tensor, vector and scalar antenna responses. Section VII reports
tensor preferences while explicitly retaining a GR phase model. This makes
detector geometry a useful constraint on a reconstruction, but those model
likelihoods cannot be assigned to a newly proposed force law without its
readout and propagation assumptions. The comparison is exposed development
context, not a new independent test. The corresponding source ledger is preserved in the recovery packet.

### The local tidal result follows from the supplied force

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

### Restricted mechanical arm response

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

### Network propagation prevents an unwarranted likelihood shortcut

For detector A at x_A with orientation factor F_A and arms short compared
with both wavelengths, a same-direction two-speed monochromatic wave has

    h_A(omega) = -F_A sum_s A_s exp(i omega n.x_A/c_s)/c_s^2.

At fixed direction and frequency the two column vectors are
F_A exp(i omega n.x_A/c_s)/c_s^2. One speed gives rank at most one, with
rank zero if every F_A vanishes. Two distinct speeds give rank at most two
and generically rank two. After
aligning every site using only c_L, the c_T column retains relative phases.
If the speeds coincide or the projected baselines have appropriate phase
degeneracies, the two-column rank can fall to one (or zero for an entirely
blind network). Setting one amplitude to zero restricts the active signal
family to one column; it does not change the full two-column matrix rank.
Local rank-at-most-one
tidal geometry does not imply a rank-one two-speed network transfer.

Consequently the published single-propagation scalar antenna comparison
is motivation for a test, not a computed Bayes factor against this model.
The previous power-calibrated candidate has c_T/c_L about .7185, so this
distinction matters unless one component is absent or outside the observed
time window. Emission history, distance and propagation determine that
window; no cosmological source history has been supplied here.

### What this block decides

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

## Checked resolution and limits of the controls

The independent matter check uses a separate Bessel/adaptive-quadrature
route for16 finite harmonic controls. Its full report distinguishes the
prescribed trajectories from self-consistent weak circular bodies. In
particular, q=5 is a vertically unstable prescribed source, not a stable
binary prediction. The companion weak self-consistent fixture and harmonic
tail estimate belong to the reviewer supplement; they are not relabelled
as author executions. False-formula controls are not source-mutated runs.

The independent readout check uses a13-state two-body matrix exponential,
direct acceleration differentiation and80-digit Gram/minor identities.
It checks53 endpoint cases, including blind and phase-node fixtures. The
original executed note and its later two-part rank clarification remain
separate snapshots. The reviewer's original absolute/relative normalization
mistake and corrected control are both preserved. No failed run is erased.

This canonical runner repeats the author mathematics and controls, without
writing into the original evidence directories. Six radiation/conservative
and five readout families are counted explicitly. Its normal stdout is
repeatable; --json reports the complete same-run result, and an optional
--output-json writes to a new exclusive path. The cache binds source hashes.
Controls supplement the complete displayed proofs; synthetic sampling is
not a continuum proof, a physical calibration or a new observation test.

The linked prediction now has a useful observation-driven consequence:
matching one circular radiated-power comparator leaves a specific static
anisotropy, speed split and longitudinal mechanical tide. A relativistic
matter/metric/optical completion could change these consequences and must
be derived explicitly. Lensing, strong bodies, background formation,
nonlinear galaxy response, quantum interactions and cosmology remain open.
This is a reviewable conditional theorem, not a TOE or audit verdict.
