# Native moving-frame and shift source coefficients

Conditional extension of the supplied common-frame source; no quantum
geometry or law-selection theorem is claimed here.

Use fixed cone coordinates y=D^-1 x, D=diag(1,1,v), and a symmetric positive
E(t,y). The prior spatial source has F=E D and g_cone=E^-2. Its two
continuum Clifford triples are tau^(w)=(sigma1,sigma2,w sigma3), w=+/-1.
For an antisymmetric matrix Omega,

    rho_w(Omega)=Omega_ab tau_a^(w) tau_b^(w)/4
               =i/4 epsilon_abc Omega_ab
                            (w sigma1,w sigma2,sigma3)_c.  (T1)

Define the finite Laurent vertices

    K1=sin k1, K2=sin k2,
    K3=(zeta-cos k3) sin k3/v,
    Gamma1=(sin k3/v) sigma1,
    Gamma2=(sin k3/v) sigma2, Gamma3=sigma3.                (T2)

At k_w=(0,0,w acos zeta), every K_i is zero and
partial_j K_i=D_ii delta_ij. Gamma_c(k_w) is the matrix in T1. Thus K_i/a
acts on exp(i k_w.n) psi(D^-1 a n) as -i partial_(y_i), up to O(a) on
fixed smooth compactly supported test spinors. Gamma_c acts as its node
matrix up to O(a); anticommutators with bounded smooth coefficients preserve
that estimate by finite Taylor remainders.

For a shift beta(y), set

    K_beta=anti(E^-1 (partial beta) E)
                      -beta^i anti(E^-1 partial_i E),
    A_t=anti(E^-1 partial_t E),
    t_c=epsilon_abc (A_t+K_beta)_ab/4.                    (T3)

Let h_E,a be the spatial common-frame native operator in physical units,
including its scalar half-density spin connection. The following supplied
time-dependent Hamiltonian has the desired continuum matter limit:

    h_a[N,E,beta,partial_t E]
       ={N,h_E,a}/2 -sum_i {beta^i,K_i/a}/2
                         +sum_c {t_c,Gamma_c}/2.          (T4)

Its limit at node w is

    {N,D_g}/2-D_g[beta]-i rho_w(A_t).                     (T5)

The spin term in -D_g[beta] is -i rho_w(K_beta); T1 shows that T3/T4
has exactly that term together with -i rho_w(A_t). This is the spinor
Hamilton equation of the symplectic potential P1 and constraints P13,
when E is prescribed as a time-dependent classical geometry. Equivalently,
the time-dependent spinor action is i/2 psi^dagger <->partial_t psi
+i psi^dagger rho_w(A_t)psi-H_m[N]+psi^dagger D_g[beta]psi.

Each extra operator has bounded native range. K1 acts on same orbitals
through two x edges, K2 through a protected y edge or its three-edge detour,
and K3 through at most two z steps. Gamma1/Gamma2 flip orbitals with one
z displacement, requiring an x and a z edge; Gamma3 is the difference of
the two occupation stars. The existing even-path edge/CAR dictionary
therefore represents each term on the same protected graph. The new
operators preserve fermion parity. Periodic Fourier regulators still do
not assert a short wrap edge on a physical open box.

For fixed zeta away from merger and fixed bounded smooth E, inverse E,
N, beta and their derivatives, the test-spinor error of the new terms is
O(a). This follows from the exact zero and first moments of K_i and zero
moments of Gamma_c, with finite second or first moments respectively. The
new terms do not require a momentum-dependent continuum projection or
an independently placed matter species. Their coefficients still use a
supplied classical metric and its time derivative.

The construction does not realize g and pi as native qubit degrees of
freedom, impose the gravitational constraint subspace, prove interacting
quantum convergence or choose a physical source law. It supplies the
explicit matter source and canonical consistency bridge needed before
those questions can be posed on this carrier. A finite native Hamiltonian
source is not the full canonical continuum phase space.

## Direct spacetime reconstruction of the supplied action

This is a classical comparator with a supplied Lorentzian metric, not a
claim to reconstruct spacetime degrees of freedom from the native carrier.
Take the ADM metric and its adapted inverse tetrad

    ds^2=-N^2 dt^2+g_ij(dx^i+beta^i dt)(dx^j+beta^j dt),
    e_0=N^-1(partial_t-beta^i partial_i), e_a=E_ia partial_i.

Let omega_mu,ab be the spatial rotation part of its torsion-free spin
connection. Lowering the first coordinate Christoffel index gives

    Gamma_(i,0,j)=dot g_ij/2
                         -(partial_i beta_j-partial_j beta_i)/2.

Thus, directly from omega_t=E^T g dot E+E^T Gamma_(.,0,.) E,

    omega_t=A_t-E^T exterior(beta_lower) E,
    omega_i=the intrinsic three-dimensional rotation connection.

The first equality uses g=E^-2 and its time derivative; the symmetric part
of E^-1 dot E cancels against E^T dot g E/2. The spatial equality follows
by lowering Gamma_(i,k,j), which is precisely the three-dimensional
Christoffel expression. Neither identity assumes a constant lapse or shift.
The polar/Kosmann identity in P7 then gives

    omega_t-beta^i omega_i=A_t+K_beta.                    (T6)

To reconstruct the Weyl action, use the real symmetric first-order
Lagrangian and write its spin connection as a skew-Hermitian spatial
rotation plus a Hermitian boost. The rotation contribution is the
anticommutator of its coefficient matrix with rho(omega_mu); the boost
contribution is their commutator. The temporal coefficient is the identity,
so its boost commutator vanishes. In the spatial contraction the boost
coefficients are proportional to the second fundamental form K_ab. They
are symmetric in a,b, whereas [tau_a,tau_b] is antisymmetric. Consequently
that contraction also vanishes. This is the torsion-free condition used
here; it does not cover an independent torsion field or its four-fermion
terms. The chirality sign multiplying a boost does not change the zero.

For the ordinary spinor q set psi=g^(1/4) q. The scalar derivative of this
rescaling cancels inside every symmetric derivative. The density N sqrt(g)
then leaves the matter Lagrangian, after spatial integration, as

    i/2 int psi^dagger <->partial_t psi
    -i/2 int beta^i psi^dagger <->partial_i psi
    +i int psi^dagger rho(omega_t-beta^i omega_i) psi
    +i/2 int N [psi^dagger gamma^i <->partial_i psi
                  +psi^dagger {gamma^i,rho(omega_i)} psi].

The last line is -H_m[N] by the self-adjoint half-density Dirac formula.
The shift transport plus i rho(K_beta) is +<D_g[beta]>. Substitution of T6
therefore yields precisely Theta_m(dot g,dot psi)-H_m[N]+<D_g[beta]>,
including the last term of P1. Together with P14 this is the conventional
classical torsion-free Einstein-Hilbert plus free Weyl-pair action within
the supplied metric ansatz. This is an identification of the constructed
classical family, not a uniqueness theorem outside that ansatz, nor an
interacting quantum result.

## Recorded coarse-grid failure and its analytical diagnosis

The initial test asked that every doubling from 12 to 24 to 48 sites per
axis reduce the error by a factor below .58. Its positive-chirality errors
were .03619542019349215, .022588435781596323, .012489817586942882. The first
ratio fails that threshold even though all three predeclared bounds
error < .12 a pass. The original source and failed output are preserved
under BLOCK08_RECOVERY/coarse_native_refinement_failure. A uniformly small
ratio at the coarsest spacing does not follow from an O(a) consistency
statement; it is not being relabeled as a successful check.

The exact new-vertex Taylor coefficients are

    K3'(k_w)=v, K3''(k_w)=3 w zeta,
    Gamma_(1,2)'(k_w)=(zeta/v) sigma_(1,2).

In the sampled physical x coordinates, where y=D^-1 x, the leading error
of the extra time/shift terms on a smooth spinor is therefore a times

    (3 w zeta/4) {beta^3,partial_x3^2} psi
    -i zeta/(2v) sum_(c=1,2) {t_c,partial_x3} sigma_c psi. (T7)

The remaining error is O(a^2), by the finite third and second moments of
the displayed Laurent polynomials respectively. This gives a sharper,
separately challengeable prediction than the initial coarse-grid ratio.
The follow-up check differentiates the explicitly chosen smooth frame,
shift and time-rotation coefficients to compare the full vector error to
T7, and adds a finer 96-site sample. The recorded output, not this planned
check, determines its numerical disposition.

Follow-up disposition: the 48-to-96 positive-chirality error is
.006502129869157114 (ratio about .521), and the negative-chirality error is
.006884464995641741 (ratio about .492). Subtracting T7 gives residuals
.0003956225699688878 and .00035446006902501576 respectively. All predeclared
follow-up O(a^2) bounds and remainder refinement thresholds passed. These
are finite challenges of the Taylor proof, not its replacement.
