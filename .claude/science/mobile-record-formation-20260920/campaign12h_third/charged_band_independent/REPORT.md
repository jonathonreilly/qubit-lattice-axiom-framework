# Blind check: relaxed charged-matter band and prepared weak packets

2026-09-22. Independent reconstruction from the supplied homogeneous target.
No new author charged-band source or result was read. This is a conditional
finite-box calculation and prepared-state theorem, not a phase result.

**The neutral-count matter band is well defined and simple near zero angle.**
Its relaxed quadratic coefficient contains a curl term and a second positive
term on cycles of the A-sublattice exchange graph. The latter gives strictly
positive stiffness to physical harmonic link angles. Removing it, or freezing
the matter vector while differentiating, gives an incorrect response.
Prepared compact-space packets follow a positive harmonic oscillator on the
full gauge quotient for fixed box and fixed time, with a sufficient norm error
O(sqrt(h)) under K=omega0 h, J=omega0/h. These oscillators are not the earlier
pure-gauge photon oscillators: an explicit transverse axis-mode family has a
nonzero zero-wavevector frequency.

## 1. Model, sector and conventions

Let D be the vertex-by-link incidence matrix, with +1 at the stored tail and
-1 at its head. E=-i partial_theta and Gauss is DE=q. Let C be the oriented
plaquette curl matrix. Write V for the number of vertices, M=dV for links,
P=V d(d-1)/2 for plaquettes, and n=V/2 for occupied A vertices. All side lengths
are even and at least six; d>=2. In particular n is even and n>=18.

The matter fiber H_m consists of the binomial(n,n/2) charge configurations on A
with n/2 plus and n/2 minus records, with B empty. “Fixed charge” in this report
means these fixed total counts and zero total charge, not a frozen charge at
each A vertex. The supplied R operators exchange charges and therefore do not
preserve an arbitrary sitewise charge assignment. No record content is changed.

For a plaquette start its oriented cycle at an A vertex a, with opposite A
vertex c. Let its four cycle-oriented link angles be y1,y2,y3,y4 and set

    u=y1+y2,  v=y3+y4,  phi=u+v,  chi=u-v.

On input charges (q,r), R has phase exp[-i(q u+r v)] and swaps the charges.
Consequently the dimensionless potential matrix in H=K sum E^2+J V(theta) is

    V_p(theta) = -2 cos(phi) P_equal
                 -2 [exp(i chi) sigma_a^+ sigma_c^-
                     + exp(-i chi) sigma_a^- sigma_c^+].                 (1)

Thus on opposite charges the two circulation directions have the same phase
and target; their amplitudes add. On equal charges the diagonal contribution
is -2 cos(phi). This follows directly from the supplied four-link shifts,
including the exchanged charges in the adjoint; treating the two directions
as unrelated paths would lose a factor of two.

Let G_A be the multigraph with A vertices and one oriented edge a->c per
plaquette, and let B be its vertex-by-plaquette incidence matrix. Define T by
chi=T theta, so C theta=phi. B here denotes an incidence matrix, not the empty
checkerboard or the earlier occupation penalty. Its Laplacian is L_A=B B^T.
Reorienting a plaquette edge changes both the relevant chi and incidence signs
and leaves the formulas below unchanged.

G_A is connected. Its allowed displacements are +/-e_i +/-e_j. They generate
the even-coordinate-sum sublattice: 2e_i=(e_i+e_j)+(e_i-e_j), and the remaining
even number of odd coordinates can be paired. Even periodic quotients preserve
this argument. This is one reason the hypotheses d>=2 and even side lengths
matter.

## 2. The simple matter band at zero

At zero angle R_p is the charge transposition P_ac and

    V(0)=-2 sum_p P_ac,
    V(0)+2P I = 2 sum_p(I-P_ac) >= 0.                                  (2)

The common kernel consists of vectors invariant under all adjacent
transpositions of G_A. Those transpositions generate every permutation of A,
and act transitively on the fixed-count configurations. The normalized
constant-amplitude neutral Dicke vector Omega is therefore the unique ground
vector, with energy e0=-2P. The excited gap delta_box is strictly positive in
every fixed finite box. No volume-uniform lower bound on that gap is assumed.

Finite matrix perturbation then gives a real-analytic simple lowest eigenvalue
e(theta) and normalized eigenvector w(theta) on a sufficiently small ball about
zero. One concrete construction is the resolvent projection around e0 followed
by normalization of its action on Omega, choosing <Omega,w(theta)> positive.
Choose the ball so that ||V(theta)-V(0)||<delta_box/4. All derivatives used below
are bounded there. This is variational minimization of the matter fiber, not
a stipulated dissipative relaxation mechanism.

Complex conjugation sends V(theta) to V(-theta), so e(theta)=e(-theta). Its
expansion has no odd total degrees:

    e(theta)=e0+Q(theta)+O_box(|theta|^4).                              (3)

Q is the coefficient of the quadratic power. The real Hessian is 2Q.

## 3. Exact relaxation term and quadratic response

The uniform neutral vector has, for a!=c,

    <q_a>=0,  <q_a q_c>=-1/(n-1),
    p_equal=(n-2)/[2(n-1)],  p_opposite=n/[2(n-1)].                      (4)

For a real zero-sum vector f on A, put q_f=sum_a f_a q_a. Then

    <q_f^2> = n ||f||^2/(n-1),
    [V(0)-e0] q_f Omega = 2 q_(L_A f) Omega.                            (5)

The second identity follows by applying each transposition to f; it does not
assume a full many-body spectral-gap formula.

In V(s theta)=V(0)+s V1+s^2 V2+..., direct differentiation of (1) gives

    V1 Omega = -i q_b Omega,    b=B chi,
    <V2> = p_equal ||phi||^2+p_opposite ||chi||^2.                       (6)

The derivative vector has zero component along Omega. Its inverse under (5)
lies entirely in the linear-charge span. Ordinary simple-eigenvalue
perturbation, with the reduced inverse at e0, therefore yields

    <V1 [V(0)-e0]^-1 V1>
        = p_opposite b^T L_A^+ b.

Writing Pi=I-B^T L_A^+ B, the orthogonal projection onto the cycle space of
G_A, the exact relaxed quadratic form is

    Q(theta) = p_equal ||C theta||^2
               + p_opposite ||Pi T theta||^2.                         (7)

The corresponding eigenvector derivative is

    w'(0;theta) = (i/2) q_(L_A^+ B T theta) Omega.                      (8)

Freezing the matter vector gives the larger direct expression in (6), not
(7). The subtraction is not optional. Our complete six-dimensional finite
matter control gives direct coefficient 15, relaxation subtraction 9 and
true coefficient 6; decreasing-angle eigenvalues approach 6. This is a direct
countercontrol to the frozen-vector calculation.

## 4. Gauge quotient, harmonic directions and positivity

A vertex gauge changes theta by D^T lambda. Along its two paths,

    C D^T lambda=0,
    T D^T lambda=2 B^T lambda_A.                                      (9)

Thus Q vanishes on every gauge gradient. In fact

    V(theta+D^T lambda)=U_lambda V(theta) U_lambda^dagger,
    U_lambda=exp(i sum_x lambda_x q_x),

and (8) reduces to the required gauge derivative i q_lambda Omega. The total
charge is zero, so constant lambda acts trivially. These signs also agree with
Gauss: physical angle wavefunctions obey
Psi(theta+D^T lambda)=U_lambda Psi(theta).

The local physical link-angle tangent space is

    U=ker D,   dim U=M-V+1.

It includes d harmonic directions. They are not gauge directions. For a
constant stored angle theta_(x,i)=a_i, curl theta=0 and B T theta=0. Counting the
half of plaquettes with each A-start orientation gives

    ||T theta||^2=4 V(d-1) sum_i a_i^2,
    T^T T theta_harm=4(d-1) theta_harm.

The second identity follows by the same edge count; mixed components cancel.
It proves that the harmonic subspace is invariant under Q, not merely that its
restricted quadratic form has the displayed value.

Consequently

    Q(theta_harm)=4 p_opposite(d-1) ||theta_harm||^2.                   (10)

The eigenvalue of the quadratic-coefficient matrix in these directions is
4 p_opposite(d-1); the Hessian eigenvalue is twice that. It stays positive
under the allowed neutrality and volume hypotheses.

Moreover Q is strictly positive on U. If Q(theta)=0, p_equal>0 implies
C theta=0. A real curl-free cochain on a periodic cubic lattice is a vertex
gradient plus a constant harmonic cochain (obtain the potential by path
integration after subtracting the cycle averages). The gradient is killed by
(9), and (10) kills no nonzero harmonic cochain. Thus

    ker Q = range D^T,
    rank Q = M-V+1.                                                   (11)

This establishes a positive fixed-box oscillator without dropping any physical
zero-wavevector link coordinate. It does not assert a uniform lower bound
on all box-dependent analytic constants.

The earlier pure-gauge zero-electric-flux reduction cannot be copied here.
For opposite charges a plaquette exchange changes the harmonic electric sums:
in a positively traversed ij square, each of F_i and F_j changes by r-q.
Hence the individual F_i generally do not commute with this charged target.
It would alter the model to remove all harmonic angles by selecting a conserved
zero-flux sector that the actual R dynamics does not preserve.

## 5. A decisive directional dispersion family

On a cubic box take a transverse link-angle mode with only component j nonzero,
proportional to exp(i k x_i), i!=j. Here k=2pi m/L_i. Direct incidence algebra
gives B T theta=0. The ij plaquettes contribute curl squared 4 sin^2(k/2) and
two-path squared 4 cos^2(k/2). Each of the other d-2 planes containing j adds
4 to the two-path squared norm and nothing to the curl norm. Other components
of the response cancel. Therefore this is an exact eigenvector of Q on U with

    lambda_T(k)=4[p_opposite(d-1)-sin^2(k/2)/(n-1)].                    (12)

At k=0 it agrees with (10). After the weak scaling below its oscillator
frequency is

    Omega_T(k)=2 omega0 sqrt(lambda_T(k)).                             (13)

For fixed omega0 this does not have the photon behavior c|k| near zero. In the
ordered algebraic large-box limit of these quadratic coefficients,
lambda_T tends to 2(d-1), not to a curl-square eigenvalue; the corresponding
frequency tends to 2 omega0 sqrt(2(d-1)). This statement about the computed
family is not a theorem interchanging the box limit with the dynamical weak
limit. It also does not classify all alternative states, other bands or
scalings of the supplied model. There is no universal no-go assertion here.

## 6. The physical compact-space kinetic term

Because charges are dynamical, the physical Hilbert space is locally a matter
vector bundle over the compact gauge quotient, not a scalar function space
obtained simply by discarding longitudinal derivatives. Let
L_v=D D^T be the vertex Laplacian. Orthogonally decompose a lifted angle as

    theta=alpha+D^T lambda,   alpha in U.

The Gauss equivariance above gives the exact local kinetic expression

    sum_e E_e^2 = -Delta_U + C_m,
    C_m = sum_(x,y) (L_v^+)_(x,y) q_x q_y.                            (14)

The longitudinal derivative vector is D^T L_v^+ q and is orthogonal to U, so
there is no cross term. C_m is positive and bounded on the finite matter fiber.
Equation (14) is a local trivialization statement; global section boundary
conditions carry the corresponding charge phases.

The gauge quotient is compact with period lattice
Lambda=2pi P_U Z^M. P_U is a rational projector: use an integer reduced vertex
Laplacian and its inverse. Hence Lambda is a discrete full-rank lattice in U.
There is a strictly positive fixed-box injectivity radius. An integer neutral
charge configuration always admits an integer electric flow on a connected
graph, so every matter basis label has physical states. The local bundle can
be trivialized on a ball smaller than this injectivity radius. Choose the quotient
measure with local Lebesgue normalization; a different Haar normalization changes
only a fixed factor in the embedding below.

Choose a ball also inside the simple-band neighborhood and choose a smooth
cutoff chi supported in it, equal to one in a smaller radius r0. A matter-valued
section supported in this chart extends by zero to a legitimate physical
compact state. Equivalently it can be periodized with the charge-valued
transition phases. The cutoff vanishes with its derivatives at the boundary,
so no boundary source is omitted. A global unique matter-band minimum or a
globally trivial ground-state eigenbundle is unnecessary.

## 7. A sufficient prepared weak-packet theorem

Set K=omega0 h, J=omega0/h, omega0>0 fixed, and subtract the scalar
omega0 e0/h. In the chart the exact physical Hamiltonian is

    H_h-omega0 e0/h
      =omega0[-h Delta_U+h C_m+(V(alpha)-e0)/h].                       (15)

Let Q_U be (7) restricted to U. It is a positive real symmetric matrix. The
comparison oscillator on L2(U) is

    H_osc=-Delta_x+x^T Q_U x,
    phi_t=exp(-i omega0 t H_osc) phi.

Take a normalized fixed Schwartz packet phi, such as a finite Hermite
superposition or displaced oscillator Gaussian. Its weighted derivative norms
are bounded for every fixed interval 0<=t<=T. Define the prepared embedding

    I_h phi(alpha)=chi(alpha) h^(-dim(U)/4)
                   w(alpha) phi(alpha/sqrt(h)),                      (16)

in the chart and extend it as just described. It is in the physical kinetic
domain, satisfies Gauss exactly and is a normalized state after division by
its norm. Its matter state follows the local lowest band; arbitrary fixed
matter states are not covered by this construction.

Here is an explicit sufficient residual estimate. On the cutoff support let

    A1=sup (sum_i ||partial_i w||^2)^(1/2),
    A2=sup ||Delta_U w||,
    A4=sup |e(alpha)-e0-Q(alpha)|/|alpha|^4,
    A0=||C_m||,   M1=||grad chi||_infinity,
    MDelta=||Delta chi||_infinity.

The ratio defining A4 extends boundedly at zero by (3). These are finite
fixed-box constants, computable from the finite matrices and the chosen chart.
For the oscillator packets write

    Mg(T)=sup ||grad phi_t||,
    M4(T)=sup || |x|^4 phi_t||,
    M31(T)=sup || |x|^3 grad phi_t||.

Then the norm of
[(H_h-omega0 e0/h)I_h-I_h omega0 H_osc]phi_t is at most

    omega0 { 2 A1 sqrt(h) Mg
             +h [A2+A0+A4 M4]
             +2 M1 h^2 M31/r0^3
             +h^3 (MDelta+2 M1 A1) M4/r0^4 }.                        (17)

To obtain (17), use V w=e w exactly, Taylor-expand only e, and differentiate
(16). The cross derivative of w and the scaled packet is O(sqrt(h)); it is not
silently discarded as an adiabatic identity. The term h C_m is also retained.
The two cutoff derivatives have support |x|>=r0/sqrt(h), on which
||phi_t||_tail<=h^2 M4/r0^4 and
||grad phi_t||_tail<=h^(3/2) M31/r0^3. These estimates give the last two terms.
The derivatives of w on that annulus are included in the last coefficient.

The exact embedding norm is

    ||I_h phi_t||^2=integral chi(sqrt(h)x)^2 |phi_t(x)|^2 dx,

so it is 1-O(h^4) uniformly on the fixed time interval. Duhamel and normalization
now give

    sup_(0<=t<=T) || exp[-it(H_h-omega0 e0/h)] Phi_h(0)-Phi_h(t) ||
         <= C_(box,phi,T,omega0) sqrt(h),                             (18)

where Phi_h(t)=I_h phi_t/||I_h phi_t||. This is a constructive fixed-box
prepared-wavepacket result. It requires neither actual instantaneous matter
relaxation nor an unproved finite-time Born-Oppenheimer theorem. The controlled
residual proves the needed statement directly. Improving the O(sqrt(h)) rate
would require additional correctors; none is claimed.

The normal frequencies are 2 omega0 sqrt(lambda_j(Q_U)), including the d
harmonic coordinates. Norm convergence controls all bounded observables under
this specified embedding. Convergence of arbitrary unbounded moments, a
continuum field algebra, long times or arbitrary initial states does not follow
just from (18).

One may compose this with the previously checked microscopic homogeneous
large-spin construction in an ordered way: hold box and h>0 fixed, take its
spin/dressing/small-birth limit, and then take h->0. The packet's electric
moments grow as h decreases, and the matter-band gap and chart constants depend
on the box. A simultaneous volume/spin/weak limit needs additional estimates.
No uniform such limit is inferred by composition.

## 8. Independent controls and preserved failures

`band_algebra_check.py` builds the entire neutral four-site matter fiber on a
connected five-edge exchange graph, directly from the local phases in (1).
The dimension is six. It verifies the unique ground, the exact derivative
vector, factor-two Laplacian action, and reduced-resolvent formula. For the
selected integer phi/chi direction, the direct coefficient is 15 and the
relaxed coefficient is exactly 6. Ground-energy finite differences at angles
0.1,0.05,0.025,0.0125 tend to 6 with the expected quadratic error; the last is
5.999004055661316. A finite pure gauge rotation preserves the ground and has
matrix covariance error below 4e-16. This tests the complete local matter-band
algebra; it is not falsely described as a full small cubic torus.

`torus_response_check.py` independently assembles actual allowed 6x6 and 6x6x6
periodic geometries, all positive-axis links, plaquettes, their A-start paths
and both incidence matrices. The gauge identities are exact integer identities.
The 2D rational calculation checks the harmonic/axis eigenvalues exactly.
It certifies rank with nonzero minors modulo prime 1000003, together with
matching exact nullspace upper bounds. It finds rank Q=37 and rank C=35,
harmonic eigenvalue 36/17, and axis eigenvalues 35/17,33/17,32/17. The 3D controls check the same formulas by numerical residuals, without
a symbolic full 648x648 rank computation. The finite Gauss/Coulomb decomposition
is separately checked on a selected neutral charge vector. Full values and
execution limits are in the results and complete streams.

The first algebra execution failed at a NumPy exponential because a SymPy
Integer was passed through as an object scalar. The exact band/resolvent checks
and finite-angle threshold had already passed. Its source and complete streams
and receipt are preserved. The only repair converts that explicitly numerical
phase coefficient to float; no mathematical coefficient or tolerance changed.
The initial torus execution was deliberately stopped after 360 seconds inside
SymPy's dense rational 72x72 rank elimination. Its source, traceback and receipt
are preserved. Replacing only that costly rank method by the modular certificate
just described completed the same controls successfully; it did not change any
rank, coefficient or tolerance. The second checker's 3D residuals are below
1.3e-14. The complete output and actual limits remain separate from the analytic
all-size proof.

## 9. Conclusions and boundaries

The supplied neutral-count model has a simple relaxed matter ground band near
zero. Formula (7), including the matter-relaxation subtraction, is the complete
quadratic response. Gauge directions vanish, all directions of the physical
finite-box quotient are positive, and the harmonic stiffness is (10).

The finite-box weak limit exists for the stated prepared packets and has the
oscillator spectrum just calculated. The explicit transverse family (12)-(13)
does not yield the light-like dispersion of the earlier neutral pure-gauge
packet. This conclusion is confined to this lowest neutral matter band,
preparation and scaling. It is not a theorem excluding other phases or sectors
of the charged Hamiltonian.

There is no assertion of thermodynamic phase selection, a uniform matter gap,
spontaneous symmetry breaking, a full QFT limit, native-site realization or
finite-rate formation. The exact finite controls test the algebra; the
all-size fixed-box arguments and packet estimate are given above. The PRE seal
records exactly which sources and artifacts were accessed before comparison.

## 10. Source identities and reproducibility

The exact seven permitted dependency identities are recorded in
`SOURCE_READ_BOUNDARY.json` and reauthenticated by the PRE seal. They comprise
the already completed homogeneous and weak-packet independent reports, their
comparisons and final seals, and the already checked homogeneous target note.
No new external literature or author band argument was imported.

The two current scientific scripts import only standard numerical/symbolic
libraries. Complete outputs and timed receipts are retained for both successful
runs and both earlier failed/interrupted attempts. The archived earlier source
bytes match those attempts' receipts. Scripts refuse to overwrite their named
results; preserve old results before any reproduction. Exact symbolic checks,
floating residual checks and the modular certificate are identified separately.
`PRE_COMPARISON_SEAL.json` freezes this entire reconstruction before any new
author comparison.
