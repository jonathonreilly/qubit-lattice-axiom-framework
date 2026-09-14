# Charged loop optimization and defect-path gap discipline

Personal derivation, provisional conditional mathematics. No independent
review or phase conclusion. This develops the operator-widening route left
open by PR8120.

## 1. Exact optimization of a charged local contraction

Let Omega be a normalized vector on a finite tensor-product link Hilbert
space. Let V=V_X tensor V_Xc be a membrane product of clock shifts, V^N=I,
and omega=exp(2pi i/N). For operators A supported on a loop neighborhood X,
require V A V*=omega^-1 A and ||A||<=1. With rho_X the reduced state, define

    T_X=(1/N) sum_{k=0}^{N-1} omega^-k V_X^k rho_X V_X^-k.

Then V_X T_X V_X*=omega T_X and

    alpha_X := sup_{A charged, ||A||<=1} |<A>| = ||T_X||_1.

Proof: averaging gives Tr(rho_X A)=Tr(T_X A), hence the trace norm bounds
the objective. Write T_X=W|T_X|. Its modulus commutes with V_X and its
polar partial isometry has charge +1; A=W* has charge -1, norm<=1 and
attains Tr|T_X|. Set it zero on the missing polar subspace. A unitary
extension is unnecessary. The one-filter proof of PR8120 needs a
contraction here; unitarity was a sufficient stronger hypothesis.

For a physical Gauss-invariant vector, rho_X commutes with every restricted
site gauge transformation. These transformations commute with V_X because
the gauge group is abelian and both are products of X shifts. Consequently
T_X and its polar partial isometry are gauge invariant. The optimizer can
therefore be chosen physical without adding a gauge projection penalty.
This argument is on the full tensor carrier with a physical state; it does
not assume the constrained physical Hilbert space factorizes by region.

## 2. Exact optimal unitary boundary dressing

Let Y be a boundary neighborhood disjoint from X, phi=V Omega, and

    M_Y=Tr_Yc |phi><Omega|.

Then

    beta_Y := max_{R_Y unitary} |<R_Y V>| = ||M_Y||_1
           = F(rho_Yc, rho_Yc^V),

where F denotes root fidelity Tr sqrt(sqrt(rho) sigma sqrt(rho)). The first
identity is trace-norm duality and polar decomposition. The second is the
finite-dimensional purification identity, equivalently obtained by the
singular-value decomposition of the coefficient matrices of Omega and phi.
If Omega and phi are physical, M_Y commutes with each restricted Gauss
transformation. Its polar optimizer has a unitary completion separately in
each common gauge eigenspace, so R_Y may also be chosen physical.

Both alpha_X and beta_Y lie in [0,1] and are monotone when their permitted
regions grow. This follows by embedding a permitted optimizer in the larger
region. It is not a statement that the product tends to one in any phase.

For any such R_Y, B=R_Y V preserves the exact linking algebra with A because
[A,R_Y]=0. It also preserves the separated-deformation mechanism of PR8120:

    B H B* -H = R_Y (VHV*-H) R_Y* + (R_Y H R_Y*-H).

If VHV*-H is supported on the boundary Y0, the right side is supported on
Y0 union the interaction-range enlargement of Y. Its norm is bounded by
the old boundary cost plus twice the sum of the norms of Hamiltonian terms
meeting Y. R_Y need not be a shallow circuit. A conjugated term may span
the whole region Y, but the original-H LR estimate still applies to this
bounded operator supported away from X. Region size and total perturbation
norm must grow at most polynomially with the loop scale in that application.

## 3. Exact tradeoff for the two optimizations

For a charged contraction A and unitary B=R_Y V, put a=<A>, b=<B>. Each
ordered connected expectation is bounded by
sqrt[(1-|a|²)(1-|b|²)] using Cauchy-Schwarz and ||A||<=1. The Weyl algebra
therefore gives

    sin²(pi/N) |a|² |b|² <= (1-|a|²)(1-|b|²).

The two optimizers can be chosen simultaneously, since every R_Y commutes
with every A supported in the disjoint X. Thus

    sin²(pi/N) alpha_X² beta_Y²
        <= (1-alpha_X²)(1-beta_Y²).

This is a finite algebraic uncertainty statement, not a gap theorem. It
rules out simultaneous alpha_X->1 and beta_Y->1 at fixed N and separated
regions in any state. Ordinary perimeter expectations can be exponentially
small and satisfy it. The quantities expose a definite target for widening;
they do not assume that the target is attainable.

### 3.1 A concrete static sufficient condition for gaplessness

Choose loop neighborhoods X_L and boundary neighborhoods Y_L with a
distance at least kappa L-o(L) after enlarging Y_L by the interaction range.
Require their sizes and the deformation norm in section2 to grow at most
polynomially. All quantities are evaluated in the SAME specified ground
state of the SAME local clock Hamiltonian, at fixed N and couplings.
The displayed reduced-state fidelity uses a growing finite-volume sequence.
In an infinite-volume representation beta may instead be defined directly
as the supremum over finite-region unitaries; no density matrix on the
infinite complement is assumed in that notation.

If

    alpha_(X_L) beta_(Y_L) >= exp[-s_opt L+o(L)],

then the one-filter argument of PR8120 applies to the charged polar
contraction A_L and optimally dressed unitary B_L. A contraction has the
same upper bound1 on both ground-vector variances used in that proof, and
the exact twisted dynamical identity still holds. The locality of H^B-H
was paid in section2, even for an arbitrary many-body boundary unitary.
Consequently, for a unique ground state (or the stated scalar-compression
extension), a putative positive gap obeys

    Delta <= e mu v s_opt/(mu kappa-s_opt), when mu kappa>s_opt.

In particular, subperimeter optimized product cost s_opt=0 rules out a
positive gap. It is enough that both optimized quantities stay bounded
below by positive constants; neither must approach one. This is consistent
with the exact tradeoff above, which forbids both approaching one but
allows two nonzero constants below it.

This reformulates the missing phase estimate as two explicit reduced-state
quantities. It is not a proof that those quantities have subperimeter cost
in the interacting fixed-clock ground state. Ordinary bare-loop perimeter
bounds give only exponentially small lower bounds on the optima and do
not discharge this stronger requirement. Nor does this sufficient test
establish a simple photon pole, relativistic dispersion or native formation.

## 4. Actual local clock defect paths

Use H=t sum_l(2-X_l-X_l*)+K sum_p[1-(W_p+W_p*)/2],
W_p=product_{l in boundary p}Z_l^epsilon_pl. For a closed Wilson current j
and a membrane cochain v with j.v=1, define U=product Z_l^j_l and V=product
X_l^v_l. Let theta=2pi/N. The following paths are local and Gauss invariant:

    H_E(s)=t sum_l[2-exp(i s theta j_l)X_l-exp(-i s theta j_l)X_l*]
           +K sum_p[1-(W_p+W_p*)/2],

    H_B(s)=t sum_l(2-X_l-X_l*)
           +K sum_p[1-(exp(-i s theta(dv)_p)W_p+adjoint)/2].

For 0<=s<=1, H_E(0)=H_B(0)=H, H_E(1)=UHU*, H_B(1)=VHV*.
Their derivatives are confined to C=supp j and Y0=supp dv respectively,
with sums of local derivative norms at most2t theta sum|j_l| and
K theta sum|(dv)_p|. The interaction strengths and LR velocities are
uniform in s and loop size for fixed N,t,K. Also

    [H_E'(s),V]=0,
    V H_E(s) V* - H_E(s) = VHV*-H,

whose support is Y0. These are the conditions that allow the electric
spectral flow to be approximately neutral under the distant membrane
boundary. The paths are not defined using fractional powers of clock
operators; those powers would introduce wrap terms or violate the desired
Gauss/local-source conditions between the integer endpoints.

## 5. Conditional obstruction to two uniformly gapped defect paths

Consider the large separated Hopf loops of PR8120, fixed N and fixed local
couplings, and sufficiently large finite boxes. Assume H has a unique
physical ground state and that BOTH paths in section4 have a unique physical
ground state separated from the rest of the physical spectrum by a common
positive gap gamma, independent of loop size and volume. These path gaps
are extra hypotheses, not consequences of a bulk gap at s=0.

The spectral-flow construction of Bachmann et al. gives unitaries S_E,S_B
mapping the initial ground vector to U Omega and V Omega, respectively,
up to scalar phases. Its generator is an integral

    D(s)=integral W_gamma(r) tau_r^{H(s)}(H'(s)) dr,

where W_gamma has an integrable tail decreasing faster than any power.
An exact compact-Fourier-support smooth filter suffices. LR truncation at
r of order the spatial separation supplies local approximants R_E,R_B
supported on disjoint loop/boundary neighborhoods of width cL, with

    ||S_E-R_E||+||S_B-R_B|| = o(1).

The total derivative norms and support counts grow polynomially in L.
For fixed gamma the filter tail can beat every such polynomial. This
uniform prefactor accounting is necessary; a theorem for one fixed-size
impurity alone would not suffice for the growing loop.

Moreover, the two exact identities at the end of section4 and the Duhamel
estimate from PR8120 imply

    ||[tau_r^{H_E(s)}(H_E'(s)), V]||
       <= polynomial(L) exp[-mu d_L+mu v |r|].

Integrating against W_gamma, splitting at |r| proportional to L, and then
integrating the flow parameter gives ||[S_E,V]||=o(1). Norm-preserving
unitary evolution in s avoids an exponential in the extensive derivative
norm here. Since R_B is remote from U and R_E, it also follows that
||[U,S_B]||=o(1) and ||[S_E,S_B]||=o(1).

Define A=S_E* U and B=S_B* V. Both act by a phase on Omega, exactly.
Commuting the three pairs just estimated and using UV=omega VU gives

    ||AB-omega BA||
      <= ||[U,S_B]||+||[S_E,S_B]||+||[S_E,V]|| = o(1).

More explicitly, if epsilon_E=||S_E-R_E||,
epsilon_B=||S_B-R_B|| and eta_E=||[S_E,V]||, then

    |1-omega| <= 2 epsilon_E+4 epsilon_B+eta_E.

But its expectation on Omega has magnitude |1-omega|>0, a contradiction.
Therefore the two physical defect paths cannot both maintain a uniform
positive gap and a unique ground state as the loop size grows. A closing
defect-path gap, a change in its ground multiplicity, or failure of another
stated premise is required. No claim of a zero bulk gap at s=0 follows.
With a degenerate ground sector, A and B may act nontrivially on that
sector; the scalar-vector contradiction requires replacement and is not
silently retained.

Primary source scope: Bachmann-Michalakis-Nachtergaele-Sims,
arXiv1102.0842, Assumptions2.1-2.2, Proposition2.4 and its proof,
Corollary2.8, and Theorem3.4 with proof; the inspected material is pp3-11.
The finite-clock paths, growing-loop prefactor audit and Weyl contradiction
above are derived here. De Roeck-Schütz1501.04571v2 pp1-4 explicitly warn
that their exponentially local transformations need not be unitary and
their constants depend on the bounded impurity size; that stronger-sounding
result is not imported for an extensive loop.

## 6. A concrete gauge-strip mechanism for a closing defect gap

Take an open planar strip of L square Z2 gauge plaquettes, with no holes,
and impose Gauss constraints. In the electric basis, each physical current
is uniquely a mod2 sum of plaquette boundaries, labeled by n_i in Z2.
This gives L dual qubits. The shared internal edges carry n_i+n_(i+1);
each external edge carries its adjacent n_i. The outer Wilson loop is
U=product_i X_i in these dual variables.

Twist the electric phases along this outer boundary by s pi. Up to a scalar,
the exact physical strip Hamiltonian is

    H_strip(s)=-2t sum_(i=1)^(L-1) Z_i Z_(i+1)
       -2t cos(pi s)[2 sum_i Z_i+Z_1+Z_L]-K sum_i X_i.

For L=1 the repeated endpoint term gives the correct four boundary edges.
At s=1/2 this is an open transverse-field Ising chain with J=2t, h=K.
For 0<g=h/J<1 define Majorana strings

    a_i=(product_(k<i) X_k) Z_i,
    Gamma=c_L sum_(i=1)^L g^(i-1) a_i,
    c_L=sqrt[(1-g²)/(1-g^(2L))].

The a_i anticommute and square to one, so Gamma²=I. It anticommutes with
P=product X_i. Direct cancellation in [H_strip(1/2),Gamma] leaves only
the last end term, giving norm2J c_L g^L. The finite h>0 chain has a
unique ground state by irreducible stoquastic positivity, and it is a
P eigenvector. Therefore Gamma Omega is orthogonal to Omega and has
Rayleigh energy at most2J c_L g^L above it. Hence

    gap(H_strip(1/2)) <= 2J c_L g^L.

This is a fully explicit mechanism for an exponentially closing inserted
defect-path gap. It does not establish gaplessness of H_strip(0), of a
three-dimensional bulk clock theory, or of the TOE. The strip is a check
of the path-gap premise, not the separated three-dimensional Hopf geometry.
At K=0 the untwisted strip has a unique classical product ground state and
a uniform gap, while the midpoint is exactly degenerate. A claim of
uniform endpoint stability at K>0 requires a paid stability theorem.
