# Positive orbit-normalized clock dressings — working derivation

Author working mathematics, no independent review or retained status.
This continues PR8121 provisionally. It does not establish the fixed-clock
phase estimate. The quantum state probabilities below are mathematical
matrix coefficients, not a derivation of a native measurement/Born law.

## 1. A physical charged contraction from any positive local weight

Use coordinate configurations a in Z_N^E on a finite link region X.
The membrane restriction v_X has order N; a closed loop j in X with
j.v=1 mod N ensures this. Write omega=exp(2pi i/N). Given a nonnegative
function f(a), assume its orbit sum D_f(a)=sum_k f(a+k v) is positive.
Define the diagonal operator A_f by

    A_f(a) = sum_(k=0)^(N-1) omega^(-k) f(a+k v) / D_f(a).

This is a convex combination of Nth roots, so |A_f(a)|<=1 pointwise,
without a lower bound on D_f. Reindexing gives

    A_f(a-v)=omega^(-1) A_f(a), hence V A_f V*=omega^(-1) A_f.

If f is invariant under every restricted Gauss translation a->a+d chi,
then D_f and A_f are too, since the translations commute with v. Thus
A_f is a physical charged contraction supported on X. Arbitrarily small
orbit denominators can create numerical conditioning or approximation
problems; they do not break the exact operator norm bound.

A concrete strictly positive choice is an auxiliary clock-spin partition
function on the graph of X:

    f_kappa(a)=sum_(chi in Z_N^vertices)
        product_(ell=(x,y)) exp[kappa cos(2pi(a_ell+chi_y-chi_x)/N)].

Changing a by a gauge gradient is a change of summation variable. The
auxiliary spins are a definition of an observable, not added physical
payload or a change to the clock Hamiltonian. The observable can depend
on all of X; no efficient or shallow physical implementation is claimed.
If v is a gradient on X, f is invariant under it and A_f vanishes for
charge1. A linked loop with j.v=1 rules out that trivial topology.

## 2. Exact diagonal optimum and matched-posterior identity

Let mu(a)=<a|rho_X|a> be the normalized coordinate marginal of the SAME
specified clock state. Decompose configuration space into v-orbits O, choose
one representative a_O and write a_j=a_O+jv. Let

    m_O=sum_j mu(a_j), p_O(j)=mu(a_j)/m_O,
    u_O=sum_j p_O(j) omega^j.

Ignore zero-mass orbits. A diagonal charged contraction necessarily has
A(a_j)=omega^j z_O with |z_O|<=1. Therefore its exact optimum is

    alpha_diag(mu) = sum_O m_O |u_O| <= alpha_X.

The last inequality is inclusion in the full operator optimization of
PR8121. Choosing z_O=conj(u_O)/|u_O| attains it, with zero on a vanishing
u_O. Gauss averaging preserves the objective, charge and contraction norm
when mu is physical, so this optimum is available with Gauss invariance.

Set f=mu in section1, defining A=0 on wholly zero-mass orbits. On each
nonzero orbit,

    A_mu(a_j)=omega^j conj(u_O).

Consequently

    <A_mu>_mu = r_mu := sum_O m_O |u_O|^2,
    alpha_diag(mu)^2 <= r_mu <= alpha_diag(mu).

Both inequalities follow from 0<=|u_O|<=1 and weighted Cauchy-Schwarz.
Thus the matched positive-ratio construction preserves whether the best
DIAGONAL charged expectation has subexponential cost. It can double a
positive exponential rate, but it cannot convert such a rate to zero.
This is an exact reformulation, not an estimate of the unknown mu.

## 3. Only the conditional orbit distribution needs matching

For another nonnegative f with positive orbit sums, let q_O(j)=f(a_j)/D_f,
w_O=sum_j q_O(j) omega^j. The true-state expectation is exactly

    <A_f>_mu=sum_O m_O u_O conj(w_O).

Let eps_O=sum_j |p_O(j)-q_O(j)| and
E2=sum_O m_O eps_O^2. Then

    Re <A_f>_mu >= r_mu - sqrt(r_mu E2).

Indeed |u_O-w_O|<=eps_O, and Cauchy-Schwarz bounds the total cross term.
If E2 <= eta^2 r_mu with eta<1, then

    alpha_X >= |<A_f>| >= (1-eta) r_mu.

The condition concerns posteriors along membrane-shift orbits, not global
partition-function normalization or total variation of entire volumes.
Changing f by any positive orbit-invariant factor does not change A_f.
A sufficient stronger condition is 2 sum_O m_O D_KL(p_O||q_O)<=eta^2 r_mu,
by the finite classical Pinsker bound. No such estimate has been established
here for an auxiliary Gibbs weight and the actual quantum ground marginal.

A small error in ordinary local observables does not supply E2. Nor does
unconditional small relative entropy in an expanding region necessarily
stay small enough compared with a decaying r_mu. A useful phase proof must
pay precisely this scale comparison, along with the boundary fidelity.

## 4. A cycle proves that positive normalization alone does not widen

For a single oriented simple cycle with P edges, all gauge-invariant
coordinate functions depend only on its holonomy h=sum_ell a_ell mod N.
With j.v=1, h shifts by one. Every charge1 diagonal contraction has the
form c omega^h with |c|<=1. Hence

    alpha_diag = |<W_cycle>|.

No diagonal construction on that cycle alone can remove a bare perimeter
cost. This says nothing about arbitrary off-diagonal operators or a tube
with additional independent cycles/plaquette fluxes.

For the auxiliary clock weight w(r)=exp[kappa cos(2pi r/N)], define
w_hat(q)=N^(-1) sum_r w(r) omega^(-q r). Expanding every edge weight and
summing all site spins enforces constant Fourier current q around the cycle:

    f_kappa(a)=N^P sum_(q=0)^(N-1) w_hat(q)^P omega^(q h).

The orbit ratio of section1 is consequently

    A_f(a)=[w_hat(1)/w_hat(0)]^P W_cycle(a).

For finite kappa>0, 0<w_hat(1)<w_hat(0). Strict upper inequality is strict
triangle inequality for a positive weight on every clock value. Positivity
follows from the positive Fourier coefficients of exp[kappa cos theta]
and their aliases modulo N; it can also be obtained from the positive
power series in shifts. Thus the one-dimensional auxiliary model adds an
exponential attenuation. It is a counterexample to treating orbit
normalization itself as proof of subperimeter cost.

## 5. Remaining collective obligation

A route to the static criterion in PR8121 would establish, at fixed N and
couplings, on separated thickened loop/boundary regions of polynomial size:

1. r_mu >= exp[-o(L)] for the actual clock ground marginal (a sufficient
   diagonal-order condition, potentially stronger than full alpha_X order);
2. for a useful explicit f, posterior mismatch E2 <= eta^2 r_mu, eta<1;
3. the complementary quantum root fidelity beta_Y >= exp[-o(L)].

Then the exact charged contraction and remote unitary dressing give the
required subperimeter product. Condition2 is unnecessary if an existence
argument may use f=mu directly. Conditions1 and3 are the substantive phase
estimates; this construction does not establish either. A classical
coordinate marginal can lower-bound alpha_X, but measuring/dephasing the
complement increases fidelity. Classical marginal overlap alone therefore
provides the wrong inequality direction for a lower bound on beta_Y.

These conditions are downstream of the stated clock carrier and Hamiltonian.
No contradiction with the TOE axioms is proved, and no axiom update is
justified by this unfinished phase route.

## 6. Quantum orbit normalization avoids the diagonal restriction

The positive construction has an operator version. Let F>=0 on X and
V_X^N=I. Set

    tau_F = (1/N) sum_k V_X^k F V_X^(-k),
    T_F   = (1/N) sum_k omega^(-k) V_X^k F V_X^(-k),
    A_F   = tau_F^(-1/2) T_F* tau_F^(-1/2).

Inverses are on the support of tau_F, with zero on its kernel. Every orbit
operator V^k F V^(-k) has support there. Define

    E_k = (1/N) tau_F^(-1/2) V^k F V^(-k) tau_F^(-1/2).

These are positive and sum to the support projector. Since
A_F=sum_k omega^k E_k, its norm is at most one: the map
psi -> direct_sum_k sqrt(E_k) psi is a contraction, and A_F is the
compression of the diagonal unitary with entries omega^k. This argument
requires no commutativity between E_k. Reindexing gives charge -1.
If F commutes with the restricted Gauss group, every object does too.

For F=rho_X, write tau=tau_rho, T=T_rho and alpha=||T||_1 from PR8121.
The exact charge projection identity yields

    <A_rho> = r_Q := Tr[T tau^(-1/2) T* tau^(-1/2)]
                   = ||tau^(-1/4) T tau^(-1/4)||_2^2 >=0.

Schatten Holder, with exponents4,2,4, gives

    ||T||_1 = ||tau^(1/4) [tau^(-1/4) T tau^(-1/4)] tau^(1/4)||_1
      <= ||tau^(1/4)||_4^2 ||tau^(-1/4) T tau^(-1/4)||_2
      = sqrt(r_Q),

using Tr tau=1. The contraction upper bound gives r_Q<=alpha. Thus

    alpha^2 <= r_Q <= alpha.

The quantum orbit ratio therefore preserves subperimeter cost of the FULL
charged optimum, without restricting to coordinate-diagonal observables.
For diagonal F, the formula reduces exactly to section1. This uses the
existing square-root/pretty-good measurement normalization of a cyclic
state ensemble. The character objective and the bound here are derived
directly; no claim of a new general measurement theorem or native
measurement primitive is made.

The phase criterion can equivalently be attacked through r_Q and beta_Y:
subperimeter alpha iff subperimeter r_Q, because their rates differ by
at most a factor of two. The inverse reduced-state powers are an analytic
obligation: finite definition and a norm bound do not produce uniform
local approximation or an efficient computation as X grows.

## 7. Positive amplitudes do not justify replacing quantum coherence by marginals

Let r be a power of two, with Q consisting of a flag qubit f and two
r-dimensional registers i,j, and Y consisting of a flag and one such
register. Define the nonnegative normalized purification

    Omega = (1/sqrt(2 r^2)) sum_(i,j)
       [|0,i,j>_Q |0,i>_Y + |1,i,j>_Q |1,j>_Y].

Let V=X_flag on Q, a fixed order2 clock shift. Both Omega and V Omega
have nonnegative coordinate amplitudes. Their Q marginals are

    rho_Q = (1/2) [|0><0| tensor (I/r tensor |+><+|)
                 +|1><1| tensor (|+><+| tensor I/r)],
    sigma_Q = V rho_Q V*.

Both coordinate diagonals are uniform, so their classical fidelity is1.
But root fidelity multiplicativity and block additivity give

    F(rho_Q,sigma_Q)=F(I/r,|+><+|)^2=1/r.

It can be arbitrarily small, despite the identical diagonals and positive
purifications. This is a finite algebraic example, not a ground state of
the geometrically local clock Hamiltonian.

Moreover every coordinate-diagonal charged operator has zero expectation,
while the unrestricted charged optimum is

    alpha_diag=0, alpha=1-1/r.

Indeed T=(rho_Q-Vrho_QV*)/2 has blocks plus/minus
[(I/r tensor |+><+|)-(|+><+| tensor I/r)]/4. The two component projectors
commute, intersect in the common |+,+> vector, and each has r-1 exclusive
eigenvectors. Their trace-norm difference is2(r-1)/r, giving the formula.
Thus even positive-amplitude fixtures can hide charged order entirely in
off-diagonal matrix entries. Section6 retains that information; a diagonal
posterior campaign alone is an additional scientific restriction.

## 8. All charge sectors and an entropy-based sufficient condition

A charge-one test can miss symmetry breaking that survives only in another
nontrivial character. At fixed finite N this is unnecessary for the gap
argument. Define for q=0,...,N-1

    T_q=(1/N) sum_k omega^(-qk) V^k rho_X V^(-k), tau=T_0,
    r_q=||tau^(-1/4) T_q tau^(-1/4)||_2^2.

The weighted Hilbert-Schmidt inner product makes distinct charge sectors
orthogonal, since tau commutes with V. Fourier inversion rho_X=sum_q T_q
therefore gives the exact identity

    R_X:=sum_(q!=0) r_q
       =Tr[(tau^(-1/4) rho_X tau^(-1/4))^2]-1.

Here r_0=Tr tau=1 and 0<=R_X<=N-1. For the upper bound, rho_X<=N tau,
so tau^(-1/2) rho_X tau^(-1/2)<=N on its support; multiply by rho_X and
trace. Some q!=0 has r_q>=R_X/(N-1). Section6 supplies an exactly physical
charge-q contraction with expectation r_q.

Thus under the SAME locality, growing-region, and ground-sector conditions
as PR8121, the following is sufficient to rule out a uniform positive gap:

    R_(X_L) >= exp[-o(L)], beta_(Y_L) >= exp[-o(L)].

The selected q may vary with L. This is harmless at fixed N because
|1-omega^q|>=2 sin(pi/N)>0 for every q=1,...,N-1. The one-filter proof
uses that uniform lower bound and the unchanged local deformation of B.
No claim about a simple photon pole follows merely from this gap test.

In finite dimension, let D_X=D(rho_X||tau). Since the twirl is a
trace-preserving conditional expectation,

    D_X=S(tau)-S(rho_X), 0<=D_X<=log N.

The entropy difference follows because log tau is invariant under the
twirl, so Tr rho_X log tau=Tr tau log tau. The upper bound follows from
rho_X<=N tau and operator monotonicity of log (or continuity on supports).
The standard sandwiched Renyi order monotonicity and order-one limit give

    D_X <= log(1+R_X), hence R_X >= exp(D_X)-1 >= D_X.

Accordingly D_(X_L)>=exp[-o(L)] together with the quantum fidelity condition
is a sufficient, potentially easier-to-state pair of estimates. The source
for the Renyi step is Muller-Lennert et al., arXiv1306.3142v4, Definition2,
Theorems5 and7 and the collision specialization. Logarithms here are natural.
These are finite reduced-state formulas; an infinite-region entropy or
trace is not silently assumed.

This is related to the existing entropic order parameters of Casini,
Huerta, Magan and Pontello (arXiv2008.11748), especially their group-average
conditional expectations and relative-entropy differences in section3.
Their complementary-algebra certainty relation is NOT imported without
identifying the exact algebra inclusion, dual conditional expectation and
index. Our tensor-region twirl and complementary fidelity alone do not
supply that full inclusion statement. Nor does an entropy identity prove
its value in the actual interacting clock ground state.

## 9. The fidelity optimizer is controlled by a finite transition region

Let S=supp(V), Z=Y union S, and rho_Z the actual reduced state there.
The boundary transition matrix can be obtained without constructing a
matrix on the infinite complement:

    M_Y = Tr_(Z minus Y) [V_Z rho_Z].

This follows by tracing outside Z first in |V Omega><Omega|. If another
normalized density matrix sigma_Z satisfies ||rho_Z-sigma_Z||_1<=epsilon_Z,
then

    ||M_Y(rho)-M_Y(sigma)||_1 <= epsilon_Z,
    |beta_Y(rho)-beta_Y(sigma)| <= epsilon_Z.

Left multiplication by the unitary V preserves trace norm. Partial trace
is contractive on trace norm for arbitrary operators, by duality with the
isometric map C_Y -> C_Y tensor I. This proves the first inequality; the
second is the reverse triangle inequality. The required finite region
contains the whole membrane, not merely its boundary or a fixed local cell.

Likewise ||rho_X-sigma_X||_1<=epsilon_X implies
|alpha_X(rho)-alpha_X(sigma)|<=epsilon_X, directly by the supremum over
charged contractions. Polar optimizers built from sigma_X and M_Y(sigma_Z)
therefore obey in the actual state

    |<A_sigma>| >= max(alpha_X(sigma)-epsilon_X,0),
    |<R_sigma V>| >= max(beta_Y(sigma)-epsilon_Z,0).

For a physical choice, gauge-average the approximants first. This does not
increase their distance from the true physical reduced states. The clock
shift commutes with Gauss products, so the polar constructions are physical.
The two supplied approximants need not be asserted to define a global
state: certified distance bounds to the SAME actual ground state suffice.

This gives a precise local-state approximation contract for a controlled
reference phase. It needs trace norm on regions growing with the loop,
including a membrane. Fixed-region convergence, matching covariances alone,
or pointwise low-defect density does not imply the required bounds.

## 10. A bounded boundary contraction also suffices for the filter estimate

Let R_Y be any contraction, not necessarily unitary, disjoint from X and
remote from its Hamiltonian-range enlargement. Put B=R_Y V. Then B is a
contraction and AB=omega^q BA for an exactly charge-q contraction A_X.
For the original local Hamiltonian H,

    tau_t(A) B - omega^q B tau_t(A)
      =[tau_t(A),R_Y] V
        + R_Y [tau_t(A) V - omega^q V tau_t(A)].

The first term is controlled by the usual LR estimate between X and Y.
The second is bounded by the membrane deformation Duhamel estimate of
PR8120, because VHV*-H is confined to its distant boundary. This proves
an exponential-in-separation bound with polynomial support prefactors
without introducing H^B or asserting B is unitary. The ground-vector
spectral-filter estimate needs only norms at most one on both operators,
so its one-filter conclusion remains valid.

The finite supremum over boundary contractions still equals the unitary
supremum ||M_Y||_1 by polar decomposition. Allowing contractions therefore
adds no optimum value, but makes controlled channel pullbacks easier.

## 11. A precise coarse-graining gate for the two static diagnostics

Let Lambda take a fine state to a coarse state, with unital completely
positive Heisenberg adjoint Lambda*. Suppose the following EXACT operator
and locality conditions hold for the chosen loop construction:

1. A coarse unitary V_c with V_c^N=I has Lambda*(V_c)=V_f, the actual
   fine membrane unitary.
2. Lambda* sends operators in the chosen coarse loop/boundary regions to
   the corresponding separated fine regions, up to a stated block radius.

A unitary sent to a unitary lies in the multiplicative domain: Schwarz
inequality is saturated for both V_c*V_c and V_cV_c*. Hence

    Lambda*(C V_c)=Lambda*(C) V_f,
    Lambda*(V_c C)=V_f Lambda*(C)

for every C. One can check this directly from a finite Stinespring
isometry W: Lambda*(C)=W* pi(C) W. Unitarity of Lambda*(V_c)=V_f
forces pi(V_c)W=WV_f, since the squared norm of their difference is zero.
Insert this equality on either side of pi(C) to get the two identities.
Therefore a coarse charged contraction A_c pulls back to a
fine charged contraction, and a coarse boundary contraction R_c gives

    Lambda*(R_c V_c)=R_f V_f, ||R_f||<=1.

Its expectation in the actual fine state equals the coarse expectation.
Section10 supplies the original-H filter bound even when R_f is not
unitary. No assumption that a coarse logarithmic Hamiltonian is local is
required. If the pulled-back operators are not Gauss invariant, average
them over fine site Gauss transformations. In a physical state this
preserves their expectation, charge and norm, with at most the fine
Gauss-support enlargement of the regions; V_f commutes with those Gauss
transformations. The enlarged regions must still be separated.

Thus the charged optimum and the TRANSITION-NORM boundary optimum of a
coarse state provide lower bounds on the respective fine optima when the
operator/locality gates hold. Covariance alone is weaker than the exact
unitary pullback and does not automatically supply the multiplicative
identities. A channel which simply dephases or erases the membrane variable
can increase a marginal fidelity and fails this gate.

Crucial mixed-state distinction: the coarse state after discarding fine
registers is generally mixed. Its boundary quantity is

    beta_c = ||Tr_(coarse outside Y_c) [V_c rho_c]||_1.

It is NOT generally F(rho_(Y_c complement),rho_(Y_c complement)^V).
That latter purification formula needs the entire purifier, including
all discarded fine registers. For example rho_c=I_4/4, V_c=X tensor X,
Y_c=the first qubit, gives beta_c=0, whereas the second-qubit marginal is
maximally mixed and has fidelity1 with its conjugate. This prevents an
incorrect use of fidelity monotonicity to declare successful widening.

A simple exact example of the operator gate is unitary blocking followed
by discarding internal factors. In a block of m qubits, take the product
of CNOTs from qubit0 to every other qubit. It sends X_0 to product_i X_i
and leaves Z_0 fixed. Keeping qubit0 in the encoded basis therefore pulls
a coarse shift back to a product of fine shifts. Tensor products of such
block maps preserve support up to the block diameter. This is only an
operator construction; no claim is made that its coarse state has the
required nonzero diagnostics in the interacting clock phase. More suitable
block maps may need to retain additional flux information.

## 12. A positive boundary observable after controlled finite blocking

Assume a chosen block channel obeys section11, is a permutation-unitary
encoding followed by tracing internal registers, and the fine state has
nonnegative coordinate amplitudes. Its coarse density matrix then has
nonnegative coordinate entries. If V_c is a clock-shift permutation,
M_(Y_c)=Tr_(outside Y_c)(V_c rho_c) also has nonnegative entries.
Let d_Y be the dimension of the retained coarse boundary space and
P_+=|+><+| there, with |+> the normalized uniform vector. Then

    b_+ := Tr(P_+ M) = (1/d_Y) sum_(i,j) M_ij >=0,
    b_+ <= beta_c=||M||_1 <= d_Y b_+.

The lower inequality is trace-norm duality with the contraction P_+.
For the upper inequality, expand M=sum_ij M_ij |i><j| and use the triangle
inequality and || |i><j| ||_1=1. Thus if d_Y is fixed, or grows only as
exp[o(L)], b_+ has subperimeter cost exactly when beta_c does.

This substitutes one explicit positive boundary contraction for a polar
optimizer, under the stated positivity and dimension conditions. Its
fine pullback is covered by section10. In a finite clock Hamiltonian with
strictly positive electric hopping t and no signful matter, nonnegative
coordinate ground amplitudes follow from irreducible Perron-Frobenius;
a global ground state can be chosen physical by Gauss invariance and
uniqueness. It remains to control the same state's large-scale coarse
matrix. A signful charged-matter theory requires a separate argument.

Applying P_+ directly on every fine boundary link would introduce
1/d_Y=N^(-|Y|), potentially an exponential volume cost. The controlled
coarse dimension and exact membrane pullback are essential, and are not
replaced by an informal smoothing picture. The contraction is a
mathematical observable in a static gap proof, not a newly approved
physical postselection or native formation primitive.

A sufficient concrete endpoint for a renormalization argument is now:
a sequence of geometrically controlled block maps preserving V exactly,
with coarse states converging on a fixed finite set of retained registers
to a state whose charged contraction has nonzero expectation and whose
positive b_+ is nonzero. Trace-norm continuity then gives two positive
constants in the actual fine state, and the original-H filter excludes a
uniform positive gap. Proving this convergence for the fixed-N interacting
clock Hamiltonian remains open. A finite numerical blocking experiment
would at most falsify a proposed map or identify a candidate fixed state.

## 13. A restricted Pauli-blocking limitation to keep the next route honest

Suppose a proposed Clifford block map retains m_L boundary clock qudits,
with d_L=N^(m_L), and pulls every coarse generalized Pauli P_a back to a
fine Pauli. Suppose, separately and UNPROVED here for the actual phase,
that the same-state uniform bound

    |<Lambda*(P_a) V_f>| <= exp[-c L+o(L)]

holds for every one of those boundary Pauli dressings, with c>0 and the
remainder uniform in a. A boundary contraction has an orthogonal Pauli
expansion R=sum_a c_a P_a. With Tr(P_a*P_b)=d_L delta_ab,

    sum_a |c_a|^2 = Tr(R*R)/d_L <=1,
    sum_a |c_a| <= d_L.

Therefore its expectation obeys

    |<Lambda*(R)V_f>| <= exp[m_L log N-c L+o(L)].

For m_L=o(L), this proposed restricted blocking cannot provide a
subperimeter boundary expectation under that supplied uniform bound.
For a convex average of bare membrane translations, the stronger direct
bound has no dimension factor, since the coefficients sum to one.

This is an algebraic conditional restriction, not a proof that all bare
Paulis in the physical clock model satisfy the premise. A non-Clifford
block map, more retained data, a state-dependent decoder, or a failure of
the uniform bare upper bound can evade it. In particular the CNOT example
of section11 establishes only an exact operator map; it does not by itself
supply an effective renormalization of perimeter fluctuations. No axiom
conclusion follows. This private working note is not submitted as a
five-family no-go packet or a retained negative claim.

## 14. Approximate membrane preservation has a quantified penalty

The exact gate of section11 can be relaxed if its error is actually proved
in operator norm. Keep the support condition, but assume

    ||Lambda*(V_c)-V_f|| <= epsilon,

with both V_c and the actual product membrane V_f unitary and of order N.
In a Stinespring representation Lambda*(C)=W* pi(C) W, put
D=pi(V_c)W-WV_f. Then

    D*D=2I-Lambda*(V_c)* V_f-V_f* Lambda*(V_c),
    ||D||<=sqrt(2 epsilon).

It follows for every contraction C that

    ||Lambda*(C V_c)-Lambda*(C)V_f||<=sqrt(2 epsilon),
    ||Lambda*(V_c C V_c*)-V_f Lambda*(C)V_f*||
       <=2 sqrt(2 epsilon).

The second identity follows by inserting the analogous relation for V_c*
on the two sides; no inverse channel or approximate multiplicative-domain
claim is needed. Let A_c have charge -q under V_c and norm<=1. The fine
operator C=Lambda*(A_c) is almost charged. Project it exactly by

    A_f=(1/N) sum_k omega^(qk) V_f^k C V_f^(-k).

Telescoping the one-step charge error and averaging k=0,...,N-1 gives

    ||A_f-C|| <= (N-1) sqrt(2 epsilon).

The projection is contractive, so ||A_f||<=1. Because V_f is a tensor
product of clock shifts, its conjugation preserves the support of C;
the exact projection does not spread A_f over the full membrane. The
usual fine Gauss average can also be applied without expectation loss.
For a coarse boundary contraction R_c, take R_f=Lambda*(R_c). Then

    |<A_f>| >= max(|<A_c>_coarse|-(N-1)sqrt(2 epsilon),0),
    |<R_f V_f>| >= max(|<R_c V_c>_coarse|-sqrt(2 epsilon),0).

Under the original locality and ground-sector hypotheses, these lower
bounds feed the filter of section10. If the two coarse expectations tend
to positive constants and epsilon->0, the sufficient gap test survives.
For subexponentially small coarse expectations the error must be smaller
than those expectations; mere epsilon->0 is insufficient. This is another
explicit proof obligation for a proposed renormalization map, not an
estimate that has been established for the physical clock ground state.
