---
claim_id: native_weyl_canonical_metric_constraints_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For smooth supplied classical metrics and complex spinor half-densities on a three-torus, derive a configuration-space spin connection and joint constraint algebra in the stated quadratic-momentum, linear-curvature metric ansatz. Reconstruct its torsion-free ADM action and construct finite-range native shift and time-rotation sources with the corresponding smooth-test-spinor limit at the two specified Wilson nodes. Geometry, time, canonical interpretation and the metric ansatz are supplied. No quantum constraint algebra, interacting continuum theorem or axiom selection is asserted."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_weyl_canonical_metric_constraints_2026_09_13.py
---

# Native Weyl sources and classical metric constraints

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Target and premise account

Construct the joint classical metric/spinor symplectic structure, derive its
strong deformation brackets in the declared local metric ansatz, and realize
the associated supplied moving-frame matter Hamiltonian through finite-range
native source coefficients at the two specified Wilson nodes.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Analytical construction and ansatz classification, with exact algebra and finite curved-frame/native challenges."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Reciprocal geometry/matter dynamics and consistent canonical sources on the same native carrier."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Test local interactions with the fermionic algebra and a native realization of the dynamical metric variables."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the
Lattice, Qubit, Admissibility and Record ontology. Ordinary quantum tensor
composition, the selected Hamiltonian, smooth classical geometry, continuous
time and the constraint interpretation below are additional declared model
inputs. They are not inferred from that memo. The native placement uses the
conditional edge/CAR representation of the
[current-main native edge theorem](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md).
The rest of the mathematical construction is reconstructed in this note;
no unmerged sibling theorem is used as an input.

| Obligation | Input or proof here | Preserved limitation |
|---|---|---|
| Metric/spinor configuration connection | Explicit frame transformation and Darboux calculation | Classical complex spinors, not an operator-ordered quantum theory |
| Covariant Dirac variation | Normal-coordinate Koszul calculation and half-density cancellation | Smooth torsion-free metric and fixed spin structure |
| Joint spatial generator | Finite polar action, invariant potential and moment map | Metric and spinor transform together |
| Normal brackets and metric coefficients | Local operator identity, functional variation and torus witnesses | Only the stated momentum/curvature ansatz is classified |
| Four-dimensional action identification | Direct ADM connection and Legendre transform | Geometry and foliation interpretation are supplied |
| Native time, shift and spatial vertices | Node moments, protected paths and Taylor estimates | Smooth prescribed source consistency, not native canonical geometry |
| Quantum interacting constraints and source-law selection | Open | Stronger physical target, not a terminal lemma of the stated classical theorem |

Known ADM and Dirac formulas were available before this calculation. The
primary algebra checks are challenges of a written proof, not blind
predictions or independent author review. No empirical constants are fitted.

Author derivation; independent review pending. This is a
classical canonical construction on a compact oriented spin three-manifold
(or compact support), not an axiom derivation or quantum constraint theorem.
Use a three-torus to avoid bundle and boundary qualifications in the native
comparison. Fields are smooth, g is positive definite, and there is one
complex two-component spinor of each chirality. The equations below also
make sense for a single such classical spinor. Quantum interpretation,
canonical geometry, the source action and constraint interpretation are
supplied. No empirical constants are inferred. Brackets are identities of
smooth local functionals with the stated integrations by parts; no global
well-posedness theorem for the nonlinear evolution is asserted. Spatial
transformations use the identity component with a chosen spin lift, so the
fixed spin structure and its possible double cover are respected. Lapses
in the bracket identities are smooth real smearings; the spacetime action
reconstruction uses N>0. Boundary contributions are excluded by the closed
slice or compact-support hypothesis.

## The phase-space term that moving geometry adds

Write a coordinate-row orthonormal inverse frame B, so g=(BB^T)^-1.
Rotating B to B R acts on its spinor as psi -> Spin(R)^-1 psi. On the
bundle of frames over positive metrics define the matrix connection

    A_B(delta B)=anti(B^-1 delta B),   anti(X)=(X-X^T)/2,
    rho(Omega)=Omega_ab sigma_a sigma_b/4.

It transforms as A_(BR)=R^-1 A_B R+R^-1 delta R. Thus delta psi+rho(A)psi
is covariant, and i/2 psi^dagger <->(delta+rho(A)) psi is invariant and
horizontal under simultaneous frame/spin rotation. At a fixed background
coordinate change J independent of the metric variation, B -> J B leaves
B^-1 delta B unchanged. This is the appropriate configuration-space
connection; it is not the intrinsic spatial Levi-Civita connection.

In the symmetric positive section E=g^-1/2, the reduced symplectic potential is

    Theta = int pi^ij delta g_ij
          + i/2 int psi^dagger <->delta psi
          + i int psi^dagger rho(A_E(delta E)) psi.          (P1)

Here pi is the gravitational momentum. Its coordinate canonical momentum
is P=pi+a, where a(delta g)=i psi^dagger rho(A(delta g)) psi. This is an
explicit Darboux description, so nondegeneracy and the Jacobi identity
follow from the ordinary product canonical structure. Use {g_ij,P^kl}=
delta_(i^k delta_j)^l and {psi_alpha(x),psi_beta^dagger(y)}=-i delta_alpha beta
 delta(x-y). For metric coordinates q^I (the six independent components),

    {pi_I,psi}=rho(A_I)psi,
    {pi_I,pi_J}=i psi^dagger rho(F_IJ)psi,
    F_IJ=partial_I A_J-partial_J A_I+[A_I,A_J].              (P2)

These formulas follow by substituting pi=P-i psi^dagger rho(A)psi.
A product bracket for (g,pi,psi) defines a different declared model unless
the Hamiltonian and generators are transformed along with the momenta.

For E=I+S, A=-[S,delta S]/2+O(S^2 delta S). Therefore

    F_E(V,W)|_I=-[V,W],
    F_g(h,k)|_I=-[h,k]/4.                                 (P3)

The second formula uses delta E=-h/2. The connection cannot be dropped
merely because A itself vanishes at the identity: its first variation is
nonzero. This is a curvature statement of this explicit connection, not a
no-go about other phase-space descriptions. Darboux momenta absorb its
one-form while changing the form of the Hamiltonian.

## The covariant variation that removes lapse-gradient cross terms

Let D_g be the intrinsic, torsion-free, self-adjoint Dirac operator on spinor
half-densities, D_g=-i gamma^i nabla_i^hd. For a covariant metric variation
h_ij, compare spinors using A. Its configuration-covariant variation is

    delta_h^A D_g = i/2 gamma^i h_i^j nabla_j^hd
                  +i/4 gamma^i nabla^j h_ij.              (P4)

A proof can be made at an arbitrary point in background normal coordinates
and a parallel orthonormal frame, then transported using covariance. At
that point delta e_a^i=-h_ai/2, and the intrinsic connection varies by

    delta omega_iab=(partial_b h_ia-partial_a h_ib)/2.

In -i sigma_i delta omega_iab sigma_a sigma_b/4, the Pauli vector contraction
is -i sigma.(d tr h-div h)/4. Its axial contraction vanishes because h is
symmetric. The variation of the half-density correction is
+i sigma.d tr h/4; these trace-gradient terms cancel. Together with the
principal variation +i sigma_i h_ij partial_j/2 this proves P4 at the point.
The construction is covariant under the frame and coordinate changes used
in choosing those normal coordinates. For an arbitrary section, the left
side is delta D+[rho(A_h),D], not just the component derivative of D.

Define the normal matter functional by the arithmetic source

    H_m[N]=int psi^dagger {N,D_g} psi/2.

Integrating the two first-order terms in P4 by parts, on a closed slice or
compact support, gives

    delta_h^A H_m[N]
      =i/4 int N h_ij [psi^dagger gamma^i nabla_hd^j psi
                     -(nabla_hd^j psi)^dagger gamma^i psi]. (P5)

All terms with derivatives of N cancel. This cancellation is specific to
the complete spin connection, half-density identification and the declared
symmetric source. It is the useful variation identity for the constraint
calculation, rather than a numerical vanishing check on a flat background.

For any spinor bilinear H=psi^dagger h(g)psi, P2 gives

    {pi_I,H}=-psi^dagger (partial_I h+[rho(A_I),h])psi.

Consequently P5 is exactly the derivative entering the mixed geometry/matter
Poisson bracket.

## Spatial generator and the normal matter bracket

For a spatial vector field a let D_g[a] be the half-density Kosmann operator

    D_g[a]=-i(a^i nabla_i^hd+div_g(a)/2
                 +gamma^i gamma^j nabla_[i a_j]/4),        (P6)

where antisymmetrization has weight 1/2. In flat coordinates this is
-i(a.partial+partial.a/2)+sigma.curl(a)/4. Set

    D_total[a]=int pi^ij (L_a g)_ij-int psi^dagger D_g[a]psi. (P7)

To check its origin without assuming a fixed-frame Lie algebra, consider
the active push of the coordinate-row symmetric frame. If J_a=partial a,
its polar rotation is the antisymmetric solution

    E Omega_a+Omega_a E=J_a E-E J_a^T,
    V_a E=-a.partial E+J_a E-E Omega_a,
    V_a psi=-(a.partial+partial.a/2)psi+rho(Omega_a)psi.

The geometric variation is V_a g=-L_a g. Evaluation of P1 on V_a is the
negative of P7. Indeed, the rotation coefficient from its two matter
terms is

    Omega_a+A_E(V_a E)=anti(E^-1 J_a E)-a^i A_E(partial_i E).

This is the component expression for the spin term in P6, with the stated
sign convention. It is also obtained by substituting the intrinsic
Levi-Civita connection and cancelling its coordinate Christoffel terms.
Invariance of P1 under the finite polar action gives an equivariant moment
map. In particular {D_total[a],D_total[b]}=D_total[[a,b]]. This statement
concerns the joint metric/spinor action; it does not assert that the
fixed-background spinor operators alone have that bracket.

For a fixed g the first-order operator identity is

    i[{N,D_g}/2,{M,D_g}/2]=D_g[a],
    a^i=g^ij(N partial_j M-M partial_j N).                 (P8)

At background normal coordinates, the common NM second-order and curvature
terms cancel. The remaining vector term is -i(a.partial+div(a)/2), and
the Pauli commutator is the spin term in P6, since
nabla_[i a_j]=(partial_i N)(partial_j M)-(partial_i M)(partial_j N).
This local calculation is covariant, proving P8 globally on the common
smooth domain. The classical bilinear Poisson convention then gives

    {H_m[N],H_m[M]}=-int psi^dagger D_g[a]psi.              (P9)

The minus sign follows from -i psi^dagger[h_N,h_M]psi and should not be
changed to i times the operator commutator.

## The local metric ansatz and its coefficient selection

In d>=2 dimensions temporarily, consider exactly the time-reversal-even
local scalar family

    H_g[N]=int N [alpha/sqrt(g)(pi^ij pi_ij-lambda pi^2)
                              +beta sqrt(g) R+gamma sqrt(g)],
    D_g^can[a]=int pi^ij L_a g_ij,
    pi=g_ij pi^ij.                                      (P10)

The pi here is a density of weight one. Coefficients are real constants.
There are no momentum derivatives, additional canonical fields or higher
curvature terms in this ansatz. We do not derive those exclusions from
native admissibility or matter propagation.

With an ordinary metric bracket, the terms ultralocal in the lapse cancel
between N,M. The only surviving functional derivative is the second-lapse-
derivative part of delta int N sqrt(g) R/delta g_ij:
sqrt(g)(nabla^i nabla^j N-g^ij Delta N). Contracting it with
2 alpha M(pi_ij-lambda pi g_ij)/sqrt(g) and integrating by parts yields

    {H_g[N],H_g[M]}
     =-alpha beta D_g^can[a]
       +2 alpha beta [(d-1)lambda-1] int a^j nabla_j pi.   (P11)

Here a^i=g^ij(N partial_j M-M partial_j N), and the derivative of the
density is its density-covariant derivative. The coefficient follows from
(pi_ij-lambda pi g_ij)(Hess^ij N-g^ij Delta N)
=pi_ij Hess^ij N+[(d-1)lambda-1]pi Delta N.

Strong equality to D_g^can[a] for every field in this ansatz gives

    alpha beta=-1,  lambda=1/(d-1),  gamma arbitrary.       (P12)

These conditions are sufficient by P11. Necessity does not presume that
the two structures are independent: at g=I on a torus, use N=1,M=cos x1.
A momentum with only pi^22=cos x1 has zero divergence but a nonzero integral
of a.partial pi, forcing the second coefficient to vanish. Then only
pi^11=cos x1 fixes -alpha beta=1. Thus neither alpha nor beta is zero.
The degenerate cases with one zero have zero pure normal bracket and do
not satisfy the displayed nonzero strong target for all momenta. This is
an ansatz classification, not a classification of every gravitational law.

For d=3, the inverse kinetic trace coefficient is lambda=1/2. Its Legendre
inverse has the familiar covariant kinetic trace coefficient 1; these are
different coefficients and should not be compared as equal numbers.

## Full classical closure in this declared family

Use P1/P2, d=3 and H[N]=H_g[N]+H_m[N]. The configuration-curvature addition
to {H_g[N],H_g[M]} is zero: both momentum gradients at the same point are
the same vector times N or M, and F is antisymmetric. The connection-
covariant mixed bracket vanishes after antisymmetrization in N,M by P5:
each factor is ultralocal in its lapse. Thus P11 and P9 give, at P12,

    {H[N],H[M]}=D_total[g^-1(N dM-M dN)],
    {D_total[a],H[N]}=H[L_a N],
    {D_total[a],D_total[b]}=D_total[[a,b]].                (P13)

The latter two follow from the invariant symplectic potential, scalar
Hamiltonian density and equivariant spatial action. This is strong
classical closure on the stated smooth phase space. It is not an
operator-ordered quantum algebra or a proof of its anomaly cancellation.
Necessity of P12 for this combined ansatz follows already on psi=0.
The coefficient gamma and nonzero alpha remain free; this construction
alone supplies no value for Newton's constant or the cosmological term.

The metric equation is dot g-L_shift g=2N alpha(pi_ij-pi g_ij/2)/sqrt(g).
Writing K_ij=(dot g-L_shift g)_ij/(2N), Legendre inversion gives
pi^ij=sqrt(g)(K^ij-Kg^ij)/alpha and the metric Lagrangian

    L_g=N sqrt(g)/alpha [K_ij K^ij-K^2+R-alpha gamma].      (P14)

Hence it is the ADM Einstein-Hilbert family with 16 pi G=alpha and
2 Lambda=alpha gamma, provided those conventional identifications are
chosen. A healthy TT kinetic branch asks alpha>0; that sign is an added
physical requirement, not selected by the algebra. Matter contributes the
last term of P1 to the Lagrangian and the H_m/D_m source terms. Dropping
that term changes the canonical structure used to establish P13.

## Two explicit checks of the omitted-connection model

These compare two declared models, not every possible canonical formulation.
If one uses a product bracket for (g,pi,psi) while leaving P7/P10 unchanged,
the connection terms in P2 are missing. Two local witnesses isolate their
effect; compactly supported smearings can reproduce these jets in an open
coordinate patch.

At g=I, take linear vector fields with symmetric Jacobians X and Y.
Their bracket has Jacobian -[X,Y]. The two metric/matter cross variations
of the product-bracket spatial generators give 2i rho([X,Y]); the bare
matter bracket gives i times the half-density transport of [a,b]. P7 asks
for only i rho([X,Y]) in addition to that transport. Thus the product-
bracket defect is i rho([X,Y]). The missing curvature contribution is
-i rho([X,Y]), from F_g(2X,2Y), and cancels it. With
X=diag(1,0,0) and Y_12=Y_21=1, the defect is -sigma3/2. It can have a
nonzero expectation in a spin-polarized test field. The natural connection
is zero at the flat frame, yet its curvature matters in this test.

A normal-bracket witness uses E=diag(2,3,4), zero spatial frame jets and a
metric velocity whose corresponding E velocity V has V_12=V_21=1.
Use N=1 and M=x3 at the chosen point x=0. The bare mixed bracket reduces
to the variation of the scalar spin connection with partial_3 delta E=V:

    delta C=-1/4 epsilon_abc E_3a V_jb (E^-1)_cj=1/6.

The first-order variation of gamma3 vanishes. Hence the product-bracket
mixed term is +(psi^dagger psi)/6 at that point. Any metric velocity V can
be attained by a suitable pi when lambda=1/2 and alpha is nonzero.
The general omitted term is

    -i/2 psi^dagger {gamma^j,rho(A_u)} psi
                                (N partial_j M-M partial_j N),

where u is the gravitational metric velocity for unit lapse. The natural
connection in P2 cancels this term by P5. The statement is about the
explicit single-chirality or unequal-density pair; an imposed cancellation
between equal opposite-chirality densities would not test every phase-space
field required by the strong bracket.

## Finite native placement

The current-main source
[native edge/CAR theorem](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
at b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf, Theorem 1, supplies the
conditional ordinary-tensor edge-qubit cycle code. Its dictionary is

    B_v=product_(e incident v) Z_e=1-2 c_v^* c_v,
    A_vw=-i gamma_(2v) gamma_(2w),
    gamma_(2v)=c_v+c_v^*.

For an ordered simple path p from v to w of length l, canceling the internal
Majoranas gives A_p=i^(l-1) product_p A_e=-i gamma_(2v) gamma_(2w). Thus

    T_p=i A_p(B_v-B_w)/2=c_v^*c_w+c_w^*c_v,
    J_p=-A_p(1-B_v B_w)/2=i(c_v^*c_w-c_w^*c_v).

Both real and imaginary hopping coefficients are therefore finite physical
operators. A cell's n_x is the sum of its two bounded-star occupation
projectors. It is not a single physical edge-Z event. The unaugmented finite
code represents even total fermion parity; choose an even number of cells
for a half-filled state. No filled-state response is used here; finite parity-preserving operators
act in the code, and smooth-test-spinor consistency is a one-particle
coefficient statement, not an encoded odd-parity physical state.

Place orbital r in {0,1} of cell x at virtual v=(2x1+r,x2,x3), with actual
edge qubits at doubled virtual-edge centers as in the source. Protect every
x,z edge and the y edges whose lower-y tail has even x+y. Each unprotected
y edge has a protected x-plaquette detour. The spatial frame vertices below have these path types:

| Symbol contribution | Orbital action | Protected path length |
|---|---|---|
| sigma1 or sigma2 times sin k1 | Flip orbital, one x cell | At most 3 |
| sigma1 or sigma2 times sin k2 | Flip orbital, one y cell | 2, choosing the x/y ordering |
| sigma1 or sigma2 times sin k3 or sin 2k3 | Flip orbital, one or two z cells | At most 3 |
| sigma3 sin k3 sin k1 | Same orbital, x and z cell displacement | 3 |
| sigma3 sin k3 sin k2 | Same orbital, y and z displacement | At most 4, with an x detour if needed |
| sigma3 cos k3, scalar sin k3, or on-site terms | Same orbital | At most 1, or the occupation star |

The flat Wilson cos k1 term uses two x edges; cos k2 uses either one
protected y edge or a three-edge x detour; cos k3 uses one z edge. These
statements hold on the infinite graph and on open boxes with enough x width
to take an inward detour. A periodic Fourier regulator is an auxiliary
operator computation, not a short physical wrap edge in an open box.

Record compatibility is only the current-main conditional one: on a
surviving cycle the physical Z projector has a fair isometric restriction,
and every surviving even word intertwines it. A prepared initial code,
ordinary quantum composition, Hamiltonian, state and Born interpretation
remain supplied. Those source-selection and autonomous-formation questions remain open.


## Spatial native source needed by the moving-frame construction

For fixed zeta in [1/2,1), put v=sqrt(1-zeta^2), D=diag(1,1,v),
x=a n and y=D^-1 x. Let E(t,y) be symmetric positive, with E and E^-1
and the required derivatives bounded. Use frame-row coordinates F=E D,
so the inverse Clifford coefficient in x coordinates is F_ai. In cone y
coordinates it is E_ia. This distinction fixes the constant rescaling.

The free symbol is

    d=(sin k1,sin k2,2+zeta-cos k1-cos k2-cos k3).

Its only zeros are k_w=(0,0,w acos zeta): d1=d2=0 forces k1,k2 to 0
or pi; either pi gives d3>=1+zeta, while both zero gives zeta-cos k3.
Use the nine finite Laurent vertices (indices 1 through 3)

    V_aj=sin k_j                          (a<3,j<3),
    V_a3=(zeta-cos k3) sin k3/v^2          (a<3),
    V_3j=sin k3 sin k_j/v                 (j<3),
    V_33=(zeta-cos k3)/v,
    B0=sin k3/v.

Set C(F)=-epsilon_abc F_ai (partial_xi F_bj)(F^-1)_jc/4 and

    h_E,a=d.sigma/a
          +sum_aj {(E-I)_aj D_jj,sigma_a V_aj}/(2a)
          +{C(F),B0} I2/2.

Every V vanishes at each specified node, with derivative
partial_i V_aj(k_w)=(1 if a<3 else w) delta_ij. Hence the principal
node coefficient is tau_a E_aj in cone coordinates. The scalar C formula
is reconstructed by the Koszul and Pauli identities: for
c_ab^c=(F_ai partial_i F_bj-F_bi partial_i F_aj)(F^-1)_jc,
epsilon_abc omega_abc=-epsilon_abc c_ab^c/2. The scalar part of
-i sigma_a omega_abc sigma_b sigma_c/4 is epsilon_abc omega_abc/4,
which gives C. The vector part is -i sigma_c div_g(e_c)/2; the
half-density correction cancels its Christoffel trace, leaving
-i sigma_a(F_ai partial_i+partial_i F_ai/2). At chirality w the scalar
is w C, precisely the value of B0 at the node. This proves the intrinsic
half-density Dirac coefficient and its scalar term.

For a fixed smooth compact test spinor, modulate the sample by exp(i k_w.n).
A finite translation by ell samples psi(y+a D^-1 ell). Taylor expansion
through first order gives the Dirac operator, and the second-moment bound
on the finite vertices gives O(a) error in the normalized lattice L2 norm.
The zeroth-order C source has O(a) error by its finite first moment. Products
with the fixed smooth source coefficients preserve those bounds. This is
consistency on fixed smooth fields at either specified node. It does not
assert operator-norm convergence on all lattice states, interacting many-
body convergence, or absence of further zeros for arbitrary large constant
E. The classical metric theorem above covers all smooth positive g;
its native comparison has the more limited test-spinor interpretation.


## Moving-frame time and shift sources

Conditional extension of the supplied common-frame source; no quantum
geometry or law-selection theorem is claimed here.

Use fixed cone coordinates y=D^-1 x, D=diag(1,1,v), and a symmetric positive
E(t,y). The prior spatial source has F=E D and g_cone=E^-2. Its two
continuum Clifford triples are tau^(w)=(sigma1,sigma2,w sigma3), w=+/-1.
For an antisymmetric matrix Omega,

    rho_w(Omega)=Omega_ab tau_a^(w) tau_b^(w)/4
               =i/4 epsilon_abc Omega_ab
                            (w sigma1,w sigma2,sigma3)_c.  (T1)

The second chirality follows without a new geometric assumption:
rho_-(Omega)=sigma3 rho_+(Omega) sigma3 and
D_-=-sigma3 D_+ sigma3. Thus the covariant variation, normal commutator
and joint connection formulas transform consistently. For a pair, sum its
two matter symplectic terms and Hamiltonians. Their Poisson cross terms
vanish in the Darboux chart, and the metric-connection argument is unchanged.

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
under the committed recovery/coarse_native_refinement_failure folder. A uniformly small
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
T7, and adds a finer 96-site sample. Its finite numerical disposition is recorded below.

Follow-up disposition: the 48-to-96 positive-chirality error is
.006502129869157114 (ratio about .521), and the negative-chirality error is
.006884464995641741 (ratio about .492). Subtracting T7 gives residuals
.0003956225699688878 and .00035446006902501576 respectively. All predeclared
follow-up O(a^2) bounds and remainder refinement thresholds passed. These
are finite challenges of the Taylor proof, not its replacement.

## Literature comparison and source-read disclosure

These sources supply checked mathematical context, not the selection of a
native law. Their cited formulas are compared with the explicit calculations
above; their unexamined hypotheses and conclusions are not imported.

| Primary source | Portion actually read | Role and fit |
|---|---|---|
| [Clayton, canonical gravity and matter in a general linear frame](https://arxiv.org/pdf/gr-qc/9808005) | Introduction and section IV through IV A; in particular equations 61–75 | Comparator for the spin contribution to frame momentum, classical complex-spinor bracket and Dirac constraints. It starts with gravitational and matter actions; it does not select them from these axioms. |
| [Bär, Gauduchon and Moroianu, generalized cylinders in semi-Riemannian and spin geometry](https://arxiv.org/pdf/math/0303095) | Introduction and the metric-path spinor identification and variation in section 5, including Theorem 5.1 | Comparator for the metric-covariant Dirac variation. The half-density trace-gradient cancellation is derived here. The paper's earlier curvature proofs were not imported. |
| [Müller and Nowaczyk, the universal spinor bundle](https://arxiv.org/pdf/1504.01034) | Section 2.1 and section 2.2 through Definition 2.9; later relevant theorem statements only | Comparator for skew vertical and symmetric horizontal frame directions. The connection, its curvature and moment map used here are proved explicitly. No global nonexistence theorem is inherited. |
| [Düll, Schuller, Stritzelberger and Wolz, gravitational closure](https://arxiv.org/pdf/1611.08878) | Selected construction/embedding passages and the Klein-Gordon metric example in section V A, equations 104–106 | Comparator for metric closure leaving two constants. Its matter/geometry hypotheses are not silently transferred to derivative-dependent spinor geometry; the latter is handled through P1–P5 here. |
| [Kouletsis, classical histories and the canonical form of general relativity](https://arxiv.org/pdf/gr-qc/9801019) | Abstract/introduction and selected section 2 assumptions and Hamiltonian family | Scope warning: constraint algebra and additional locality/geometric hypotheses must be separated. No uniqueness theorem outside P10 is imported. |

Current-main `UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md` was read in full.
Its selected logdet Hessian is a different object from the canonical metric
kinetic form P10. Current-main
`GRAVITY_SIGN_FROM_REFLECTION_POSITIVITY_UNITARITY_REDUCES_TO_EMERGENT_DIFFEOMORPHISM_NARROW_THEOREM_NOTE_2026-06-08.md`
was read in full; it conditions a sign argument on an emergent physical
metric interpretation. Neither provides a native quantum realization of
P1. These are provenance-only comparisons, not additional proof premises.
No claim about their effective audit status is inferred from their titles.

## No-Go Discipline Gate

This note submits an explicit positive construction, an exact classification
inside P10, and two existence witnesses comparing explicitly different
brackets. It submits no axiom-wide impossibility or route-exhaustion result.
The following records the stress test; it does not assert a negative-packet
PASS or fabricate five failed routes.

N1 — The configuration-bundle route was attempted and gives P1–P3. Direct
functional variation was attempted and gives P4–P13. The spacetime-action
route was attempted and gives T6 and the reconstructed action. Native
finite-Laurent matching was attempted and gives T1–T7 with the recorded
coarse-grid failure and analytical repair. An unreduced independent triad
constraint derivation was considered through the Clayton comparator, but
was not completed here. The Darboux reformulation is an explicit successful
alternative to retaining the connection in the Poisson tensor: transform
H_g to H_g(P-a). These are not five failed approaches, and are not labeled
as such. No exhaustion conclusion follows.

N2 — The supplied inputs are separated rather than counted as independent
walls. Native composition/encoding underlies the operator placement; a
chosen Hamiltonian and time underlie its test-spinor limit. Classical
metric phase space and its source interpretation underlie P1–P13. The
quadratic-momentum/linear-curvature ansatz restricts coefficient selection
within that phase space. An interacting quantum constraint theorem would
need additional work beyond all of these. Their dependence prevents a
numerical count of independent axiom obstructions.

N3 — The explicit premise table and domain paragraphs expose ordinary
composition, selected Wilson symbol, classical smooth g, torsion-free spin
connection, spin structure, boundary conditions, source arithmetic, local
metric ansatz and geometric constraint interpretation. The term canonical
refers to the supplied symplectic action, not an axiom-derived entitlement.
Healthy TT sign and the conventional names G and Lambda are also identified
as extra choices. The smooth consistency result is not promoted to a
many-body limit or a microscopic realization of g and pi.

N4 — The framework memo supplies the ontology distinction; the linked
September 5 native theorem supplies only its conditional edge/CAR code.
The literature table specifies exactly which mathematical comparison each
citation supports. None supports native metric dynamics, an occurrence law,
quantum anomaly cancellation or selection of a gravitational constant.
The coefficient classification and native vertex formulas are derived here.

N5 — At element resolution, Pauli, frame-curvature and metric-coefficient
identities are challenged. At site resolution the finite even-path CAR
operators and protected placement are checked. At mode resolution both
specified node jets and spin representations are checked. At finite-block
resolution the periodic differential-operator witness and smooth source
samples are checked. At lattice-wide resolution the written Taylor proof
and smooth classical local-functional identities carry the claim; finite
samples do not establish quantum gravity or a physical occurrence law.
The primary emits the matching five resolution statements.

N6 — No axiom update is requested. A Darboux change moves connection terms
into the Hamiltonian without changing the physical classical family.
Choosing units can fix a convention for alpha but does not predict its
relation to another measured scale. An unreduced triad description is
another plausible equivalent formulation. None needs a new framework
primitive to be studied as a conditional mathematical model. Proposed
primitives have not been assigned premise weight.

N7 — A hostile reviewer can grant every classical equation and still demand
a native realization of canonical metric variables and a fermionic quantum
constraint algebra. The finite source coefficients do not provide either.
A promising concrete continuation is to classify the actual native local
fermion interactions by their boost transformation and then seek a controlled
joint geometry/matter continuum. That remains an open mechanism, not a
reason to declare the axioms inconsistent.

N8 — The current-main logdet and gravity-sign comparisons above do not close
this canonical construction. Earlier same-author frame and stress proposals
addressed prescribed sources; their conclusions are not imported into this
PR. The connection identified here retires the explicit product-bracket
mismatch for this construction, illustrating why a missing term must be
investigated before treating a previous mismatch as an axiom obstruction.
No all-lane search or claim of global exhaustion was performed.

## Review record and remaining proof obligations

This is an author proposal. Independent scientific review and formal audit
remain pending. The source, primary and preserved failures are included in
the proposed tree. The primary declares a 60-second timeout and this note
as its sole source input; it reads its own bytes for an integrity hash and
reads no external scientific data. Raw author runs and preserved variants
are not canonical cache receipts.

The classical smooth identities are supported by their written derivation.
The checks separately challenge exact Darboux curvature, metric variation,
curved normal brackets, polar generators, four-dimensional Christoffel
coefficients, direct scalar-curvature Euler variation, Legendre inversion,
periodic mismatch witnesses, native path placement, both node jets and
smooth-source Taylor remainders. Deliberate mutations are recorded in the
committed author packet. They test sensitivity, not scientific independence.

The original coarse ratio failure is retained with its failed source and
stderr; the associated JSON from an earlier successful run is explicitly
marked stale in its recovery manifest. The initial symbol-index harness
failure is also retained. Neither is rewritten as a canonical success.
An initial factor-two temporal-source mutation also survived its finite-grid
check because that target reused the source coefficient. Its original
source, full output and ineffective disposition are retained. The repaired
primary uses one source-coefficient function in both native constructions
and compares it with independently computed four-dimensional Christoffels.
That mutation now fails in the spacetime comparison, rather than being
counted as effective on the basis of the old output.

The strongest missing physical lemma remains a native dynamical metric and
interacting quantum constraint system with a selected source law. It is
stronger than the conditional classical theorem proved here. The theorem
therefore does not terminate at that lemma or claim it nearly solved.
There is also no global nonlinear well-posedness theorem in this note.

Before any effective retained status, the independent path must examine the
proof, run the primary at the exact proposed source, and apply the current
shared landing validation. A zero-row changed-evidence report alone does
not certify this new claim's audit reachability. No helper runner registry,
audit verdict, live queue, primitive registry or publication surface is
changed by this proposal.
