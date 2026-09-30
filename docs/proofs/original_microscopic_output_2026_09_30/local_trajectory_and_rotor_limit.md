# Local trajectory compactness and the original rotor gain limit

Current supporting proof owned by the canonical microscopic-output note. All notation, law, preparation, original mark conventions and uniformity quantifiers are fixed there. This is part of the same bounded theorem, not a separately adopted premise. Constants denoted C may change between displays and depend only on the fixed supports, couplings, horizon and circuit order indicated. Equation prefixes distinguish the components.

## Local trajectory or current limit argument

## 1. Statement and the exact output carrier

Fix a finite quantum region X of matter sites and links, a finite set F of
monitored A centers, a finite horizon T, finitely many fixed time-bin
boundaries, and a fixed total count cap M. The classical register keeps the
specified original mark labels and orders in those bins until overflow;
after overflow it keeps an absorbing flag. The physical system continues
to evolve with its actual generator. This is a coarse-graining of the
output, not a stopped or altered system law. Either original resolved or
original coherent instrument is used separately.

Write Gamma_(epsilon,L)(t) for the resulting joint classical-register and
local-quantum output from bare Omega. All integer-spin field bases are
embedded by their integer E labels in the same rotor link spaces. The
matter and register spaces do not depend on spin or volume. Impose the
declared coupled scaling

 epsilon^2 S(S+1)=delta/K, with delta,K,kappa>0 fixed.

For small epsilon, all safe volumes containing the fixed enlarged geometry,
R>=1 and s,t in [0,T], the bound is

 ||Gamma_(epsilon,L)(t)-Gamma_(epsilon,L)(s)||_1
       <= C_1 epsilon+C_2/sqrt(R)+C_3(R)|t-s|.       (T1)

The constants may depend on X,F,M,T, the fixed bin structure and supplied
couplings, but not on S,L,epsilon. C_3(R) can grow with R. It suffices to
take S>=R; along the coupled limit this holds for every fixed R. Enlarging
C_2 makes the cutoff convention R versus floor R immaterial.

Consequently, for every sequence epsilon_j decreasing to zero and arbitrary
safe growing volumes, these exact outputs have a subsequence converging
uniformly on [0,T] in trace norm. The subsequential limit is continuous, positive,
trace one, and diagonal in the classical register. The local A sites are
occupied in the limit. There is no assertion of a unique limit, a particular
quantum generator, spatial boundary independence or a uniform global
trace-norm speed. A countable family of fixed output specifications admits
a common diagonal subsequence; no continuous-timestamp total variation
statement is inferred.

## 2. Joint registers and the actual normal form

Attach the classical register by the actual original jump update at each
monitored center. On a block-diagonal classical-quantum observable A, the
gain for mark mu reads j_mu* A_(updated history) j_mu and the loss is the
actual anticommutator in its current history block. Updates are contractions
in the supremum norm over history blocks. The absorbing overflow update
has the same property. Equivalently the classical update has a Kraus column
with sum V_z*V_z=I, all sharing the same physical j_mu. Its completely
bounded cross estimates are independent of the register dimension.

Extend the exact order-six physical circuit Y by identity on this register.
It leaves the observed labels and history updates unchanged, and the jumps
become J_mu=Y j_mu Y*. Use sigma=Y rho_joint Y*. The physical marginal of
rho_joint is exactly the unmonitored microscopic ensemble. Thus the proved
physical per-site hole and first-field-moment bounds apply to it unchanged.
No conditional or postselected bound is being assumed.

For every A site a, the finite circuit estimate gives

 Tr[sigma(t) w_a] <=2 Tr[rho_joint(t) w_a]+C epsilon^2
                  <=C epsilon^2(1+T), 0<=t<=T.       (T2)

Indeed, for a vector w_a Y psi=Y w_a psi+[w_a,Y]psi and
||[w_a,Y]||<=C epsilon. This norm estimate comes from the bounded cone of
Y* w_a Y-w_a; it does not say [w_a,Y] is locally supported. Convexity gives
the mixed-state inequality. It remains valid with the attached register.
Summing finitely many sites bounds any local hole union, with its explicit
support-size constant. Translation symmetry was used only in the already
proved physical bound, not in sigma or the circuit coloring.

On joint observables the exact transformed generator has the same structure
as in the defect proof:

 L'^* =i delta epsilon^-4[W,.]+epsilon^-2 B2
                                  +epsilon^-1 C1+R_epsilon,
 B2=i delta[D2,.]+kappa sum_mu D[j_mu]^*,             (T3)

where the original register updates are included in the dissipators. C1 is
the complete first jump cross map, including its gain and loss; its physical
grades on a grade-zero input are +/-1. R_epsilon has bounded local action
strength on norm-bounded observables. The higher Hamiltonian diagonal terms
are delta D4+delta epsilon^2 D6, with no odd diagonal coefficient; the
remaining Hamiltonian is O_local(epsilon^3). The exact jump remainder after
j+epsilon j1 is O_local(epsilon^2). These facts give (T3), including all
same-mark interference, uniformly in spin and volume.

An unmonitored term disjoint from the physical support of A cancels between
gain and loss. A monitored term can act on the register even if it is far
from X, but there are only the fixed finite centers F. Their bounded circuit
cones are included in the local support count. Each register update uses its
current fixed bin; the generator may change at the finitely many bin times,
with the same bounds on every interval and almost everywhere on [0,T].

## 3. Cutoff tests and the true electric coefficient

Let O be any norm-at-most-one classical-quantum observable on the output
carrier. It need not conserve W. Let P_A fill every A site in X. Let Y_E be
the finite link set consisting of all links in X and every link incident on
any matter site in X. This contains every electric polynomial that can fail
to commute with a test on X; adding a harmless fixed neighbourhood is also
allowed. Put P_R equal to the product of |E_e|<=R projections on Y_E and

 A=P_A P_R (O tensor I_(Y_E outside X)) P_R P_A.       (T4)

All these projections commute. Then ||A||<=1, [W,A]=0, and A commutes with
each individual A-occupancy projection w_a. It may change the charge sign
at an occupied A site. Outside X its extra field action is diagonal only.
The register action is unrestricted within its given finite space.

The actual second coefficient has the exact decomposition

 D2=D_vac+Cspin^-1 D_el,  Cspin=S(S+1),
 D_vac=sum_a F_a F_a*
       +sum_a F_a*F_a(Q_a-1)
       +sum_(a!=c)[F_a,F_c*],
 D_el=sum_(a,b~a) n_a(1-n_b) E_e(E_e+k_(a,b,q)) Q_a.  (T5)

Here k is the actual orientation-dependent +/-q_a and Q_a is the original
radius-two A-occupancy gate. This is the full spin coefficient, not its
rotor replacement. Each local summand of D_vac has uniformly bounded norm,
finite support and bounded incidence, and vanishes on the subspace with
all A sites in that support occupied. The cross terms are grouped with
their adjoints where necessary. The electric part is the actual diagonal
occupation-dependent polynomial from the supplied compensation source.

For any D_vac summand h_z whose commutator with A is nonzero, choose U_z
to contain all of its A sites and those of A. The no-hole projector P_(U_z)
commutes with A and is annihilated by h_z on both sides. Consequently

 [h_z,A]=Q_(U_z)[h_z,A]Q_(U_z), Q_(U_z)=I-P_(U_z),
 |Tr sigma i[h_z,A]|<=2||h_z|| Tr sigma Q_(U_z).      (T6)

Only boundedly many h_z occur. By (T2), their full epsilon^-2 contribution
is bounded by C_(X,F,T), independently of epsilon and volume. Using only
P[h_z,A]P=0 and a square-root bound here would be insufficient; the two-sided
hole support in (T6) is essential.

The gates Q_a and n_a commute with A. An electric term can fail to commute
only through a field in X, a charge at an A site in X, or occupancy of a B
site in X. Its link is therefore in Y_E. For such an edge, both A's input
and output on that link lie in |E_e|<=R. Thus

 ||[n_a(1-n_b)E_e(E_e+k)Q_a,A]||<=2(R^2+R).

All other electric terms commute with A exactly, including the terms whose
only overlap is a diagonal auxiliary cutoff. There are finitely many
possibly noncommuting edges. Since delta/(epsilon^2 Cspin)=K exactly,

 |Tr sigma i delta epsilon^-2[Cspin^-1 D_el,A]|
                                             <=C_X K(R^2+R). (T7)

This is why a cutoff only on the original output links could fail: changing
a B occupation also changes electric coefficients on its other incident
links. No second-moment estimate is used in (T7).

## 4. Original jumps and their coherent cross terms

Every bare original j_mu acts on an input hole at its center a. Since A
commutes with w_a, both its gain and its anticommutator loss, with the
actual register update, are supported on w_a on both input sides. Therefore

 |Tr sigma D[j_mu]^*A|<=2||j_mu||^2 Tr sigma w_a.     (T8)

This holds for the complete coherent mark as well as each resolved mark;
no sign cross term is discarded. The finite relevant mark set consists of
the monitored marks and those whose physical support meets A. Equation(T2)
makes the epsilon^-2 bare dissipator contribution uniformly bounded.

For the first cross map, j1=[-F+F*,j] has grades zero and minus two. On the
grade-zero A in (T4), the full gain/loss cross operator consequently has
grades +/-1. For the finite union U of its physical A support, its
compression to the all-occupied subspace is zero. The complete cross-map
norm is bounded by a constant times ||j||||j1||||A||, including the
classical update. Cauchy on the occupied/hole blocks gives

 |Tr sigma C1 A|<=C sqrt(Tr sigma Q_U)
                                      <=C epsilon sqrt(1+T). (T9)

Multiplication by epsilon^-1 gives a uniform bound. All higher jump terms
are in the bounded local remainder of (T3); neither their gain nor loss is
removed. The Hamiltonian remainder has the same uniform local property.
The W commutator vanishes exactly on A. Combining (T6)-(T9) proves

 |d/dt Tr sigma(t) A|<=C_(X,F,M,R,T)                  (T10)

almost everywhere. This is an expectation bound in the actual joint state,
not a claim that the generator's operator norm is uniform or that the
global state has bounded trace-norm derivative.

## 5. Removing auxiliary tests and proving the trace-norm modulus

The physical hole and first-moment bounds give uniformly on [0,T]

 p_A<=C_X epsilon^2(1+T),
 p_E=Tr rho_joint(I-P_R)<=C_T |Y_E|/R.               (T11)

The gentle projection inequality, valid also on the classical-quantum
joint state, then implies

 |Tr rho_joint(t) O-Tr rho_joint(t) A|
                                      <=C epsilon+C'/sqrt(R). (T12)

Here O is extended by identity on the auxiliary links. No history-conditioned
field tail is required; the marginal supplies the joint projection tail.
The finite circuit also gives

 |Tr rho_joint(t) A-Tr sigma(t) A|<=C_(X,Y_E) epsilon. (T13)

This is an ordinary bounded-local-observable estimate with ||A||<=1.
Its constant need not depend on R, on the register matrix dimension or
on ||E||. The physical support of the test is fixed as R changes. The
register is untouched by Y.

Apply (T12)-(T13) at both endpoints and integrate (T10). The constants are
uniform over every norm-at-most-one O. Trace duality on the output carrier
therefore proves (T1). For small finite spin the restriction S>=R is
irrelevant to a limiting sequence; for each fixed R it holds on its tail.
This proof does not differentiate a cumulative mean-mark error.

## 6. Uniform-in-time subsequences and limits of the result

For any desired tolerance, first choose R so the second term of (T1) is
small, then take the tail of a sequence epsilon_j->0 so its first term is
small, and finally choose a time increment using the finite C_3(R).
Finitely many discarded paths are individually continuous. This proves
equicontinuity of the sequence in the common trace-norm carrier.

At each time, the proved first moment uniformly approximates all states
by their block on finitely many electric levels. Matter and the fixed
capped/binned register are finite dimensional. Adding a refusal state if
desired normalizes the approximation with an error tending to zero.
Thus the possible output states are totally bounded in trace norm,
uniformly in time. Diagonal extraction on a countable dense time mesh,
followed by the equicontinuity estimate, gives a uniformly Cauchy subsequence
on [0,T]. Completeness of trace class gives the asserted continuous limit.
Positivity, unit trace and classical block diagonality are closed properties.
The vanishing local hole probability gives support on occupied A sites.

The same diagonal argument works for a countable collection of fixed
regions, horizons and binned/capped output specifications. Algebraic
consistency under the corresponding fixed partial traces/coarse-grainings
is preserved. This alone is not a theorem identifying a continuum-time
instrument, and no timestamp topology has been changed silently.

The limit's quantum evolution remains unspecified. A finite first moment
does not provide second-moment uniform integrability or control the
epsilon^-2 source-weighted tails. Uniform first count moments likewise
do not by themselves give uniform integrability of unbounded count
observables; a mean identity cannot be passed to an uncapped limiting count
law without a separate argument. Spatial boundary independence, uniqueness,
quadratic hole-weighted moment and changing-source fast feedback remain open. The result is
a local trajectory compactness prerequisite for those identification
problems, not their solution or a new physical-law selection.

## Holder refinement with all-spin compression

Every term in T10 except the diagonal electric commutator is bounded by a
constant times ||A|| and fixed support incidence. In particular the vacuum
hole part, bare jumps, grade-cross maps, circuit comparisons and bounded
remainder do not differentiate the cutoff and have no R dependence. The
support of P_R is fixed. Only T7 costs R^2+R. Hence T1 can be sharpened to

 ||Gamma(t)-Gamma(s)||_1
 <=C epsilon+C R^(-1/2)+C(1+R^2)|t-s|, R>=1.       (H1)

One may also remove the harmless S>=R restriction in the original proof.
For an arbitrary common-carrier observable O, first restrict its output
field indices to the actual spin box: O_S=P_S O P_S. This is a bounded
local observable of norm at most one, and gives exactly the original
embedded-state expectation. In T4 use O_S. Its support, A-occupancy
properties and all uniform local operator estimates are unchanged. The
cutoff P_R then bounds its fields by min(R,S); when R>=S it is the identity
on that link. T7 is still bounded by 2(R^2+R), and T11's field cutoff error
is zero on a link whose entire spin box lies inside the cutoff. No estimate
depends on an operator norm distance between P_S and the rotor identity.
Thus H1 holds for all sufficiently small epsilon in the stated coupled
family, even when the chosen R exceeds S.

For 0<h=|t-s|<=1, choose R=ceil(h^(-2/5)). Then R^(-1/2)<=h^(1/5),
R<=2h^(-2/5), and (1+R^2)h<=5h^(1/5). Therefore

 ||Gamma_(epsilon,L)(t)-Gamma_(epsilon,L)(s)||_1
                              <=C epsilon+C h^(1/5). (H2)

The value at h=0 is exactly zero. For h>1 on the fixed horizon use the
trivial trace-distance bound two and enlarge C. Every limiting trajectory
from the frozen proof is consequently Holder continuous with exponent1/5
and a constant depending only on the fixed output specification, horizon
and supplied couplings. This exponent is only a conservative consequence
of the first-moment cutoff and quadratic electric coefficient; optimality
is not asserted.

The additive C epsilon still allows small rapid microscopic oscillations.
The estimate does not provide global trace-norm speed, a common purification
of distinct times, a derivative of the limit, a second field moment or an
effective generator. Those missing consumers are unchanged.

## True rotor gain and register identification

## 1. Contract and limiting objects

Fix positive delta,K,kappa, horizon T, a finite monitored pattern F, finitely many time bins and an absorbing count cap M. Keep either the original resolved signs or original unnormalized coherent edge marks as its own instrument. Set epsilon² S(S+1)=delta/K with integer S tending to infinity. Let the even safe tori grow so every fixed finite region and its needed support eventually lie inside them. No claim of boundary independence is made.

The local carrier is the finite matter tensor product and integer-field rotor link carrier, tensored with the same finite classical history register Z. Each spin space embeds by its actual integer field labels. Write Gamma_epsilon,X,Z(t) for the exact microscopic marginal. The proved time-compactness theorem gives, after a diagonal subsequence over a nested countable exhaustion of finite X,

 sup_(t in[0,T]) ||Gamma_epsilon,X,Z(t)-Gamma_X,Z(t)||_1 ->0.       (L1)

The limit is continuous, positive, trace one, classically block diagonal and supported on occupied local A sites. It has the proved Holder1/5 time modulus. All quantum partial-trace identities survive, since partial trace is a trace-norm contraction. This fixes ONE register specification while enlarging X. No projection between different monitored sets after overflow is invented. Additional countable output specifications can be extracted together, but only genuinely existing fixed coarse-graining maps supply consistency.

For a monitored original mark mu centered at a, let

 A_epsilon,mu=sqrt(kappa) epsilon^-1 j_S,mu,
 B_S,mu=sqrt(kappa) j_S,mu F_S,a,
 B_infinity,mu=sqrt(kappa) j_infinity,mu F_infinity,a.             (L2)

These are the actual normalized spin words and their rotor words, not different outcomes. On the limiting occupied-A carrier, B_infinity is precisely the original leading formation word. The coherent mark keeps its sum of signs in all products. No process using B is evolved here.

For an output region X, choose Xprime containing X and the full support of every word in(L2) under consideration. The exact pre-append original quantum gain current is

 J_epsilon,mu,X,Z(t)=Tr_(Xprime outside X)
       [A_epsilon,mu Gamma_epsilon,Xprime,Z(t) A_epsilon,mu*].   (L3)

It is a positive trace-class current, with an integrable trace, not a normalized state. Define its limit by

 J_mu,X,Z(t)=Tr_(Xprime outside X)
       [B_infinity,mu Gamma_Xprime,Z(t) B_infinity,mu*].         (L4)

The definition is independent of the chosen sufficiently large Xprime by the compatible quantum partial traces in(L1). The statement is

 integral_0^T ||J_epsilon,mu,X,Z(t)-J_mu,X,Z(t)||_1 dt ->0,        (L5)

also after the exact original history append, and in a direct sum over finitely many original labels. It is strong convergence of currents along the same subsequence as the states. It is not convergence of an independently evolved effective process.

## 2. Uniform local spin-to-rotor word bound

A normalized elementary spin shift, extended by zero outside its spin box, has coefficient

 g_S(m,s)=sqrt(1-m(m+s)/[S(S+1)]), s=+/-1,

for an allowed input/output, and zero otherwise. For integer |m|<=S the expression lies in[0,1], including the correctly blocked boundary step. Its rotor counterpart has coefficient one. Since(1-sqrt(1-x))²<=x for0<=x<=1,

 |g_S(m,s)-1|² <=m(m+s)/[S(S+1)]<=|m|/S.                       (L6)

If |m|>S, the zero extension obeys the same final bound because |m|/S>1. Thus the bound holds on the entire common integer carrier; no operator-norm convergence of spin projections is asserted. Matter vacancy/charge factors are identical conditional partial permutations for both words. Orientation reversal merely exchanges the two signs.

Consider one fixed branch word of length k, consisting of such shifts and the actual matter factors. Telescope its spin/rotor difference with spin factors to the left and rotor factors to the right of each changed letter. All left products have norm at most one. Each right branch is a partial permutation that changes each relevant field by at most k. Applying(L6) to that input, and then squared triangle to the k summands, gives a quadratic-form bound

 (W_S-W_infinity)*(W_S-W_infinity)
       <=(C_k/S)(1+sum_(e in support W)|E_e|).                  (L7)

One can see this directly on a vector: the square norm of each telescoping term is bounded by its shifted diagonal first-field form; the deterministic right partial permutation pulls that form back to at most the original form plus k. Summing finitely many branch words uses squared triangle again. No branch is measured or decohered. Therefore the complete original source word obeys

 (B_S,mu-B_infinity,mu)*(B_S,mu-B_infinity,mu)
                   <=(C_mu/S) Q_mu,
 Q_mu=1+sum_(e in the actual source support)|E_e|.               (L8)

The operators B_S and B_infinity have a uniform finite norm: F_a has six elementary paths, and the original j has one or two signs with their true normalization. This is a local finite-word inequality, not a full spin response expansion.

The proved actual microscopic first-field theorem gives

 sup_(t<=T) Tr[Gamma_epsilon,Xprime,Z(t) Q_mu]<=C_(T,mu).        (L9)

Only the unconditioned physical marginal is used. The history and arbitrary quantum spectators do not change that marginal. Factoring the Hermitian gain difference and applying Hilbert-Schmidt Holder now gives

 sup_(t<=T) ||B_S Gamma_epsilon B_S*
                   -B_infinity Gamma_epsilon B_infinity*||_1
                                               <=C_(T,mu)/sqrt(S). (L10)

This includes spin-boundary amplitudes exactly. It needs only the first absolute field moment, not quadratic-field uniform integrability. The elementary shift inequality is proved above and the finite-word telescoping is explicit; no convergence theorem for an independently evolved process is imported.

## 3. Actual gain-current limit

The original gain and history appendix gives, for ANY extension eta(t) of the actual microscopic ensemble,

 integral_0^T ||A_epsilon,mu eta(t) A_epsilon,mu*
                         -B_S,mu eta(t) B_S,mu*||_1dt
                                             <=C epsilon(1+T)². (L11)

The exact history/system state is one such extension. Partial trace gives the same estimate for(L3) with its local B_S comparison. Combine(L10), multiplied by T, with(L1) and the bounded-operator estimate

 ||B_infinity(Gamma_epsilon-Gamma)B_infinity*||_1
                   <=||B_infinity||² ||Gamma_epsilon-Gamma||_1.

This proves(L5), with an upper bound of the form

 C epsilon(1+T)²+C_T/sqrt(S)
       +T||B_infinity||² sup_t||Gamma_epsilon,Xprime,Z-Gamma_Xprime,Z||_1.

Under the coupled scaling the explicit spin term is O(sqrt(epsilon)); the subsequence state-convergence term has no claimed rate. The pre-append limit current is continuous in trace norm because Gamma is. The append map at time t is the true deterministic CP map on Z with the appropriate fixed bin label. It contracts the Hermitian difference pointwise, so(L5) remains true after append even across finitely many bin switches. A finite direct sum over the actual labels has trace norm equal to the sum, preserving exactly the original label set and coherent within-label payload.

The time integral of the trace is the actual expected monitored mark count, including marks after the register has overflowed. Thus the associated cumulative mean-gain curves converge uniformly in their upper time endpoint to the integral of the trace of(L4). This statement follows directly from the integrated current estimate. It is not a passage of an unbounded count function through weak history convergence, and it does not by itself assert a law for an uncapped limiting count variable.

## 4. Exact limiting register identity

Let tau(t)=Tr_quantum Gamma_X,Z(t), independent of X. For each original mark define the nonnegative finite register vector

 nu_mu(t;z)=Tr_quantum[B_infinity,mu Gamma_Xprime,z(t)
                                             B_infinity,mu*]. (L12)

Let App_mu,t be the true deterministic append on register probability vectors, with its absorbing overflow outcome. Before taking a limit the exact original process has

 tau_epsilon(t)-tau_epsilon(0)
       =integral_0^t sum_mu (App_mu,s-I)
                            Tr_quantum J_epsilon,mu,X,Z(s) ds. (L13)

Hamiltonian and unmonitored terms have zero classical marginal, and the monitored complete gain/loss pair gives this exact identity. There is no grade measurement. The actual integrability of the gain traces follows from D3; at finite volume the finite-spin law and finite classical extension also give the usual piecewise generator identity directly.

By(L1),(L5) and ||App-I||<=2, the limit satisfies

 tau(t)-tau(0)=integral_0^t sum_mu (App_mu,s-I) nu_mu(s) ds       (L14)

uniformly in the upper endpoint t. The stronger proved register theorem gives a separate epsilon² integrated same-state comparison and is consistent with this argument; it is not needed to replace the quantum state here.

Since0<=nu_mu(t;z)<=||B_infinity,mu||² tau(t;z), the limiting register marginal is Lipschitz with constant at most2 sum_mu||B_infinity,mu||². Its forward identity holds almost everywhere within the bins and in integrated form across them. The pre-append nu are continuous, while the deterministic bin-tag map may switch. This stronger regularity concerns the classical marginal only; the quantum trajectory is presently only Holder1/5 controlled.

The coefficients in(L12) depend on the limiting JOINT quantum/history state. Equation(L14) is not a closed classical Markov law and does not identify finite-epsilon conditional intensities. It also does not determine the limiting quantum trajectory. The initial microscopic rates vanish at Omega whereas the B rates need not; the vanishing integrated initial layer in(L11) is compatible with this distinction.

## 5. Exact scope and remaining dynamics

The result establishes a compatible local-quantum subsequential limit at one fixed finite history specification, identifies its original post-mark gain current strongly in time-integrated trace norm, and gives its exact finite-register balance. It retires a need for an artificial record substitution in these specific consumers. Existing effective thermodynamic proofs remain distinct: no effective state was substituted into any microscopic formula.

The complete quantum generator and uniqueness remain open. In particular the anticommutator/no-event loss and fast Hamiltonian require a combined argument; gain matching alone cannot replace them. Dark-hole holding and field-weighted response, multiple-hole feedback, spatial boundary independence, weighted energy/W1 convergence and physical source/clock selection remain unresolved. No continuous-timestamp total-variation theorem or uncapped count uniform-integrability theorem is inferred. The supplied law is a conditional model under the current axiom boundaries, not a newly adopted foundation or a completed TOE.

Finite controls are described in the canonical note and its evidence packet; the analytic argument, rather than a finite test, establishes the stated quantifiers.
