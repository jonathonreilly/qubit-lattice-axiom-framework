# Conjugate charges and a finite positive gauge-history measure

Author construction, provisional. The target is a finite-payload interacting
Hamiltonian and its exact positive representation, not an established phase.
No framework premise is added. Independent scientific review is pending.

## Exact finite model

Fix a finite oriented graph without self-links, incidence D with +1 at the
tail and -1 at the head, and plaquette boundaries B with DB=0. Fix an integer
N>=3 and omega=exp(2 pi i/N). Each link has basis |q>, q in Z_N, and

    Z|q>=omega^q|q>,       X|q>=|q+1>.

Then XZX^dag=omega^(-1) Z. Each vertex has m plus and m minus CAR orbitals.
Let Q_x=N_{+,x}-N_{-,x}, and define commuting local gauge transformations

    Gamma_x = product_l X_l^(D_xl) exp(2 pi i Q_x/N),
    P = N^(-|V|) sum_{s in Z_N^V} product_x Gamma_x^(s_x).

Gamma_x^N=I, so P is the orthogonal projection onto the invariant space.
It is nonzero: zero-occupation matter and all links in the X=1 state are
invariant. The constraint is div E=Q modulo N if X has eigenvalue omega^(-E).
It is not an exact integer Gauss constraint.

Let h_+(Z) be a finite-range Hermitian one-particle matrix built from onsite
Hermitian matrices v_x and nearest-neighbor directed hopping T_l Z_l, with
its Hermitian reverse. At fixed phases q it becomes h(q). Define

    H_m = c_+^dag h(Z)c_+ + c_-^dag h(Z)^* c_-.

Here star conjugates numerical coefficients AND sends each Z to Z^dag;
there is no transpose of the ordering of products. The minus onsite matrix
is v_x^*, and its directed hopping is T_l^* Z_l^dag. Each hopping and onsite
term is gauge invariant with the above Gamma. Opposite charges are necessary
for this displayed local realization of the fixed-history conjugation.

Take t_l>=0 and K_p>=0 and

    H_E = sum_l t_l(2-X_l-X_l^dag),
    H_B = sum_p K_p(1-Re product_l Z_l^(B_lp)),
    H = H_E+H_B+H_m.

All are Hermitian finite matrices, gauge invariant, bounded and local. The
full finite time evolution and the physical Gibbs operator are well-defined.
An even-CAR tensor-qubit realization, native formation law, chosen vacuum and
physical identification remain separately supplied obligations.

## Positive electric kernel

In the q basis, for tau>=0,

    exp[-tau t(2-X-X^dag)]
      =exp(-2 tau t) sum_{a,b>=0} (tau t)^(a+b)/(a! b!) X^(a-b).

All matrix entries are nonnegative. For tau t>0 they are strictly positive
because every residue is attained by a walk. The entries sum to one. The
Fourier eigenvalue is exp[-tau t(2-2 cos(2 pi n/N))]. This is a cyclic random
walk heat kernel, not the hard-truncated quadratic-electric heat kernel.
The finite link has ceil(log2 N) encoding qubits, with unused words excluded.

## Exact projected finite-slice trace

Set K_delta=exp(-delta H_E), M_delta(q)=exp(-delta V_B(q)), and
A_delta(q)=exp(-delta h(q)). A convenient nonsymmetric slice is

    T_delta=exp(-delta H_E) exp(-delta H_B) exp(-delta H_m).

Each factor commutes with P. T_delta need not be Hermitian; its projected
trace still has the positive expansion below. The finite-dimensional Lie
product formula gives Tr(P T_(beta/M)^M) -> Tr(P exp(-beta H)). A symmetric
slice can be obtained by conjugation by exp(-delta H_E/2), with the same trace
of powers since H_B and H_m commute in the q representation.

For histories q_0,...,q_(M-1) and s in Z_N^V, let d_s=D^T s modulo N and
R_s=diag_x exp(2 pi i s_x/N) tensor I_m. The precise boundary kernel orientation
is fixed by <q|X^(d_s)=<q-d_s|. With q_M=q_0-d_s, one expansion is

    Z_M = N^(-|V|) sum_s sum_(q_0,...,q_(M-1))
       [product_(j=0)^(M-1) K_delta(q_(j+1),q_j) M_delta(q_j)]
       |det(I+R_s A_delta(q_(M-1)) ... A_delta(q_0))|^2.       (1)

The cyclic labeling may shift which q appears first; the displayed choice
will be challenged against a directly constructed operator trace. The
fermionic identity follows because second quantization obeys
Gamma(A)Gamma(B)=Gamma(AB) and Tr_Fock Gamma(C)=det(I+C), including temporal
gauge factors. The minus block has the SAME ordered product conjugated,
R_s^* A(q_(M-1))^* ... A(q_0)^*. This is not the adjoint of the plus product;
adjoint would reverse the order and is not the needed operation.

Every summand in (1) is nonnegative. The finite-slice representation is exact
for this Trotter product; M->infinity gives the physical finite-volume Gibbs
trace. Positivity does not by itself give a Coulomb or Weyl phase, a gap,
correlation decay, an efficient sampler, or an infrared-uniform expansion.

## Free four-node comparator and its actual supplier

Take m=2 and a simple two-node Wilson symbol

    h0(k)=sin kx sigma1+sin ky sigma2
         +(2+zeta-cos kx-cos ky-cos kz)sigma3,
    0<zeta<1,  0<b<pi.

Let h_+(k)=h0(k-b xhat) and h_-(k)=h_+(-k)^*. At Z=1, the plus nodes are
(b,0,+/-acos zeta) and the minus nodes (-b,0,+/-acos zeta). For b not 0 or pi
these are four distinct nodes. The local metric is diag(1,1,1-zeta^2) for all
four. Each species separately has opposite node chiralities, so its cubic
and mixed U(1) anomaly sums vanish. Their occupied-band Berry curvatures are
opposite after k->-k, hence charge-squared Hall responses cancel at equal
filling. This comparison uses the free symbol, not the interacting spectrum.

This supplied model conserves N_+ and N_- separately. The gauge symmetry
alone also allows a neutral pairing term c_+^dag Delta c_-^dag+h.c. Under
a compatible local identity pairing, the zero-field Nambu block is

    [[h_+(k), Delta I],[Delta I,-h_+(k)]],

whose square is h_+(k)^2+Delta^2 I. Thus a nonzero real Delta opens a gap in
this enlarged Hamiltonian family. Its compatibility with the proposed
antiunitary and with all chosen physical symmetries needs to be stated,
not assumed. Exact total matter-number conservation excludes this explicit
bilinear but does not exclude spontaneous pairing of its interacting ground
state. Weak-coupling stability must address that channel.

## Relation to known phase arguments

The pure finite Z_N Euclidean phase construction in Frohlich-Spencer is not
already a theorem about (1). Its action, source observables, time anisotropy
and matter hypotheses must be matched. The full source gives separate
Wilson/disorder loop bounds, and explicitly cautions that perimeter behavior
alone with dynamical light charges is not a deconfinement criterion. Even a
positive determinant can destroy a correlation inequality or obstruct a
local polymer estimate. These are the next mathematical questions.


## Finite-time rotor approximation by the positive cyclic model

This establishes which rotor is approximated; it does not replace its
magnetic cosine by a harmonic theory or supply an infrared phase theorem.
Take odd N=2S+1, representatives n=-S,...,S, and set

    t_l = g^2 w_l N^2/(8 pi^2 a).

The cyclic electric eigenvalue is

    lambda_N,l(n) = (g^2 w_l/(2a)) n^2 sinc^2(pi n/N).

For every real x, 0<=1-sinc^2 x<=x^2/3. One direct proof uses
sinc^2 x=2 integral_0^1 (1-u)cos(2xu) du and 1-cos y<=y^2/2.
Consequently, for every representative n,

    0 <= g^2 w_l n^2/(2a)-lambda_N,l(n)
       <= pi^2 g^2 w_l n^4/(6a N^2).                         (2)

The rotor comparator has identical CAR, hopping and plaquette coefficients,
untruncated integer E, unitary U|n>=|n+1>, and quadratic electric energy.
Assume normalized initial psi with every |E_l|<=M0<=S. It may be entangled
and can satisfy exact integer Gauss. Embed the cyclic Hilbert space by its
representative electric basis into the full rotor space. The embedding is
not invariant under rotor evolution and maps modulo-Gauss alias states to
nonphysical integer-Gauss sectors; their amplitudes are counted as error.

Write J_l=sum_(alpha:l in alpha)||V_alpha||, where H_interaction is the sum
of V_alpha+V_alpha^dag, each V shifts the participating E_l by +/-1, and a
link occurs at most once per monomial. For any lambda>0 and T=|t|, put

    C_l(T,lambda)=exp(lambda M0+2 J_l T sinh lambda),
    A_4(lambda)=(4/(e lambda))^4.

For a Hamiltonian with any real diagonal electric energies, including the
hard finite restrictions used below, the exponential-weight estimate is

    ||exp(lambda |E_l|) exp(-itH)psi|| <= C_l(T,lambda).       (3)

Indeed conjugate the generator by W=exp(lambda|E_l|). Its anti-Hermitian
part has norm at most 2J_l sinh lambda, because each allowed matrix element
changes |E_l| by at most one. Integrating the norm differential inequality
proves (3). The infinite rotor case follows from finite restrictions on a
common core and the bounded-interaction self-adjoint construction. This
also yields endpoint tails <=e^(-lambda S) C_l and
||E_l^4 exp(-itH)psi||<=A_4(lambda) C_l.

Compare successively the full rotor, its hard box with quadratic E, the
same hard box with lambda_N(E), and the cyclic model. The first Duhamel
comparison loses only raising/lowering matrix elements that leave the box.
The last gains only wrap matrix elements with an input at an endpoint. By
telescoping each plaquette product, either comparison has norm error at
most 2T sum_l J_l e^(-lambda S) C_l. The middle comparison uses (2)-(3).
Thus the state-norm difference, after the stated embedding, is bounded by

    epsilon_N(T) <= min{2,
       4T sum_l J_l exp[-lambda(S-M0)+2J_l T sinh lambda]
       + (pi^2 g^2 T/(6a N^2)) A_4(lambda)
                         sum_l w_l C_l(T,lambda)}.          (4)

This is uniform over the declared initial states and holds for fixed finite
spatial graphs, all T>=0 and odd N>=2M0+1. At fixed graph, T, g and initial
cap it tends to zero as O(N^-2), plus an exponential wrap/truncation bound.
The approximation is not operator-norm convergence on unrestricted states.
It does not assert a rate uniform in T->infinity or volume->infinity.
For a bounded observable A and its compressed cyclic counterpart J^dag A J,
the expectation error is at most 2||A|| epsilon_N(T). A usual cyclic word
in Z is a different observable at wrap endpoints and needs its own endpoint
estimate before it can replace this explicitly compressed observable.

The standard local Lieb-Robinson reduction remains a possible extension:
electric terms are onsite in either representation, and the bounded
interactions have N-independent norms. Do not yet claim an explicit local
volume-independent version until boundary and observable errors are derived.

## A positive weight need not have positive Fourier coefficients

For the one-orbital four-site ring with real unit hopping and total flux phi,
let x=beta t>0. Its one-species grand canonical trace is

    d(phi)=4[1+cosh(2x cos(phi/4))]
             [1+cosh(2x sin(phi/4))],  0<=phi<=2pi.

In particular d(0)=16 cosh^2 x and d(pi)=16 cosh^4(x/sqrt(2)). The Taylor
series of cosh^2(x/sqrt(2))-cosh x has vanishing constant and quadratic
terms and positive coefficients (2^(n-1)-1)/(2n)! for every x^(2n), n>=2.
Therefore d(pi)>d(0), and the positive paired weight F(phi)=d(phi)^2 also
has F(pi)>F(0). A continuous positive-type function on U(1), with nonnegative
Fourier coefficients, must satisfy |F(phi)|<=F(0). Hence F is not of positive
type. For even finite N the same two values disprove positive type on Z_N.
This is an exact counterexample to deriving positive Fourier coefficients
from nonnegative paired determinants, within the broad finite model family;
it is not a claim about every member or every proof of a Coulomb phase.
The underlying expansion gives

    log d(phi)=4 log 2+x^2-x^4(1/8+cos phi/24)+O(x^6).

This ring is a separate diagnostic from the three-dimensional two-orbital
Weyl carrier. It retires an automatic transfer of a positive-type inequality
from the mere positivity of the measure, not the entire positive-model route.


## Local approximation independent of ambient spatial volume

Here is the explicit completion of the local reduction suggested above.
Use carrier units consisting of the matter cells and link registers, with a
fixed finite-range graph metric. Let Phi(Y) be the bounded hopping and
plaquette interactions. Put all onsite terms into an interaction picture;
this changes neither their supports nor their norms. For mu>0 define

    C_mu = sup_x sum_(Y contains x) |Y| ||Phi(Y)|| exp(mu diam Y).

It is finite on the fixed-degree cubic carrier graph and independent of N,
including the N-dependent onsite electric energy. Assume A is even, bounded
and supported on a fixed finite carrier set X. Define R containing X and

    W_R(mu) = sum_(Y crosses R) ||Phi(Y)|| exp[-mu dist(X,Y)],
    B_R(T) = ||A|| |X| [(exp(2 C_mu T)-1)/C_mu] W_R(mu),     (5)

with the continuous limiting expression if C_mu=0. Only interactions crossing
R enter; onsite terms outside R commute with the restricted evolved A.
For either dynamics, full or restricted to terms wholly inside R,

    ||tau_T(A)-tau_T^R(A)|| <= B_R(T).                       (6)

A direct derivation avoids any ground-gap assumption. Set
M_xy=sum_(Y contains x,y)||Phi(Y)||. The usual commutator integral inequality,
iterated in the interaction picture, bounds the commutator with a local B by
2||A||||B|| sum_(x in X,y in supp B) [exp(2T M)]_xy. Weighted row sums of
M are <=C_mu. The triangle inequality for distances then bounds this sum by
|X| exp(2C_mu T-mu dist(X,supp B)). Duhamel's formula for deleting crossing
terms and time integration gives exactly (5)-(6). This applies to even CAR
observables because disjoint even observables commute. Projection onto a
Gauss sector does not enlarge the full-Hilbert-space norm bound.

For cubic boxes R expanding about fixed X, W_R(mu)->0: the number of crossing
finite-range terms grows polynomially while their distance from X grows
linearly. This statement uses the declared finite-range graph and coefficients,
not a volume-dependent interaction norm.

Take any initial density matrix with all links supported in |E_l|<=M0 and
embed it into the cyclic model, N>=2M0+1. Its restriction to R has the same
support bound; arbitrary entanglement with the exterior is allowed by
purification. For the local compression A_N=J_N^dag A J_N and the cyclic
counterpart rho_N, (4)-(6) give

    |Tr rho tau_T(A)-Tr rho_N tau_T^N(A_N)|
       <= 2 B_R(T)+2||A|| epsilon_(N,R)(T),                 (7)

where (4) is evaluated only on links and interactions of R. The bound holds
uniformly in every finite ambient box containing R and its crossing terms.
Thus for each fixed T, finite X, initial cap and tolerance, first choosing R
and then one finite N gives the tolerance independently of the ambient volume.
No independent-cell, product-state or gauge-fixed ground-state hypothesis is
used. It still does not control a fixed N at arbitrarily large times or prove
vacuum convergence or phase stability. The observable is the explicit local
compression; a cyclic word that wraps requires its additional endpoint bound.

For completeness, the untruncated rotor dynamics in this proof can be built
in the interaction picture of the diagonal electric terms. At finite volume
the interaction is bounded, so its Dyson series converges in norm. Starting
from a finite electric cap, its nth term changes each electric number by at
most n. Hard-box approximants therefore converge on that dense initial domain.
This justifies passage from the finite weighted estimate to (3) without an
unproved interchange of an infinite weighted operator and its dynamics.

## Additional local charge interaction

The positive representation also allows the genuine quartic interaction

    H_U = (1/2) sum_x u_x Q_x^2,  u_x>=0.

For each site and slice,

    exp(-delta u Q^2/2)
       = integral dphi exp(-phi^2/2)/sqrt(2pi)
                         exp(i sqrt(delta u) phi Q).        (8)

The plus and minus one-particle factors are conjugate unitary diagonal
matrices. Insert them in the same relative position in the ordered products
in (1); their determinants remain conjugate for each real auxiliary history.
The Gaussian measure is positive and the integrand is bounded by a finite
volume exponential in beta||h||, so the finite-slice integral is well-defined.
Lie product convergence supplies the exact finite-volume physical Gibbs trace
with H_U. H_U is onsite and commutes with every E_l, so it does not increase
J_l or the hopping/plaquette C_mu used in (3)-(7).

For one orbital per species per site, Q is -1,0,1. There is also an exact
two-point decomposition with cos(theta)=exp(-delta u/2):

    exp(-delta u Q^2/2)=(exp(i theta Q)+exp(-i theta Q))/2.

This last finite sum does not apply unchanged to the two-orbital Weyl cell,
where |Q| can reach 2. Equation (8) covers that cell without this restriction.
