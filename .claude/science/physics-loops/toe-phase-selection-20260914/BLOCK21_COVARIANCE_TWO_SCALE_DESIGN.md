# Covariance homogenization by the stationary preconditioned response

Personal exploratory design, 2026-09-15. No independent review or retained
status. The finite-volume Gaussian remainder is developed separately in
BLOCK21_PRECONDITIONED_GRADIENT_GAUSSIANITY.md. This file attacks the missing
covariance, and keeps the infinite-state identification as a distinct proof
obligation. Nothing here changes a framework axiom.

## Target and source boundary

For the compact-U(1), continuous Haar-link Villain law on free four-cubes,
at a sufficiently large but fixed beta, identify the scaling covariance of

 omega_first=beta^(-1/2) d_2* phi

under the positive auxiliary measure from block21. The desired form is

 Cov(omega_first(J_a f),omega_first(J_a g))
   -> kappa (f,R_cont g), 0<kappa<=1,

where R_cont=d* Delta^(-1)d on two-forms. The exact full-flux identity then
gives I-kappa R_cont. The block13 score/image decomposition further needs a
matched ergodic angle state to identify a constant contact term. A finite
clock retains electric aliases and is not covered by Haar unfolding.

Inputs under development are the block15/17 carrier expansion, the block21
preconditioned response and reflection estimates, and a fixed translation-
covariant extension of the carrier potential to ambient gradient variables.
All are author proposals on explicit branches, not audited premises.

## 1. A stationary response representation to establish

On the infinite lattice write

 Dcal phi=(d_2*phi,d_3 phi),
 K=Dcal(Delta^(-1)-cI)Dcal*, c=1/32.

Its Fourier multiplier m(k) is a bounded, positive, seven-component matrix;
its norm is at most1. At nonzero k it is smooth. At k=0 it has a directional
degree-zero limit m_0(p), coming from Dcal Delta^(-1)Dcal*; the local c-term
vanishes in this limit. On the first six components m_0(p)=R_cont(p).
The first-six/final-one off-diagonal blocks are zero by d squared=0.

Suppose omega_t is an actual stationary auxiliary gradient process with
drift -omega+K R'(omega), noise sqrt(2K)dB, and spatially ergodic path law.
Let A_t=R''(omega_t), with deterministic Schur norm at most delta<1 and
uniformly summable spatial range tails. For a deterministic source h,
the stationary first variation should solve

 v_t=K h+integral_0^infinity exp(-s) K A_(t-s) v_(t-s) ds.       (1)

It is the unique bounded-in-time response in an appropriate L2 space by
contraction. Let S_t be time translation on the stationary path probability
space, and define

 B=integral_0^infinity exp(-s) S_(-s) A_0 ds, ||B||<=delta.      (2)

Then v_0=(I-KB)^(-1)K h, where K commutes with time translation.
The needed fluctuation-response identity is

 Cov(omega(h),omega(g))=E (g,(I-KB)^(-1)K h).                   (3)

Equation(3) follows in finite dimension by source differentiation of the
Gibbs density and the finite-time response. Its infinite-volume version
must be proved for the selected thermodynamic state, not postulated as
an identity for any stationary solution of an infinite SDE. Although B is
causal and need not be self-adjoint, the expression in(3), when correctly
matched, is a symmetric positive covariance.

## 2. Spatial spectral decomposition of the response

Let (Omega,P,tau_x) be the stationary path probability space. Use the
Hilbert space H=L2(Omega;C^7). Spatial translations U_x are commuting
unitaries; P projects onto invariant vectors and Q=I-P. Ergodicity makes
P the projection onto constant random vectors. Time translations preserve
P and commute with U_x.

After conjugating random lattice fields to the environment seen from the
current site, and taking Fourier transform in that site, deterministic K
becomes an operator K(k) on H, defined by joint spectral calculus as

 K(k)=m(k+theta),                                            (4)

where theta denotes the joint spectrum of U. The sign depends on the
chosen Fourier convention; use one convention consistently in a proof.
Boundedness gives ||K(k)||<=1. For fixed p!=0, dominated convergence in the
spectral measure gives the strong limit

 K(ap) -> K_env Q + m_0(p)P, a decreases to0,                 (5)

where K_env=m(theta) with its zero spectral mode assigned zero. The only
exceptional theta for pointwise multiplier convergence is theta=0; its
spectral projection is precisely P. No spectral gap, quantitative mixing
rate or absolutely continuous environment spectrum is required by this
argument. Ergodicity is required to make this projection finite-dimensional.

The local or summably extended random Hessian similarly becomes A(k).
Spatial range summability should give A(k)->A(0) in operator norm; the
time integral then gives B(k)->B(0). Uniform contraction allows the
Neumann expansion of (I-K(k)B(k))^(-1)K(k) to pass strongly to the limit.
This would give a direct homogenization proof for(3), without importing a
scalar nearest-neighbor homogenization theorem into this vector problem.

## 3. Eliminate the zero-mean environment fluctuations

For the limiting response decompose v=bar_v+tilde_v using P and Q. Put
B_0=B(0). The equations become

 bar_v=m_0(p)[h+P B_0 P bar_v+P B_0 Q tilde_v],
 tilde_v=K_env Q B_0 P bar_v+K_env Q B_0 Q tilde_v.

The second has the unique solution

 tilde_v=(I-K_env Q B_0 Q)^(-1)K_env Q B_0 P bar_v.

Define the constant seven-by-seven effective response matrix

 B_eff=P B_0 P
       +P B_0 Q(I-K_env Q B_0 Q)^(-1)K_env Q B_0 P.           (6)

Its norm is at most delta/(1-delta). Then

 bar_v=m_0(p)[h+B_eff bar_v].                               (7)

All appearances of P in(6) are essential. Replacing the random Hessian by
its expectation drops the second term and is generally false. A finite
periodic-coefficient quadratic example should challenge that shortcut.

The carrier extension R depends only on the first six coordinates, so
B_eff vanishes on its seventh row and column. If the chosen state and
extension respect the full signed permutation symmetry of the cubic
lattice, the six-by-six block commutes with the action on two-forms.
Coordinate reflections first force it to be diagonal; permutations of
axes make every diagonal entry equal. This argument also excludes an
antisymmetric commutant and does not require assuming B_eff symmetric.
Thus B_eff=b I on the first block and(7) gives

 Cov_limit(omega_first)=kappa R_cont, kappa=(1-b)^(-1).        (8)

The symmetry of the extension requires an explicit choice. A local
integer filling chosen by an axis order need not respect reflections or
permutations away from the compatible-gradient subspace. In infinite
volume choose a translation-covariant filling first (a finite carrier's
lexicographic anchor can be translated consistently), then average its
extended potential over the finite signed permutation group. On the
compatible subspace every summand equals the same physical potential, so
the average leaves the auxiliary law and projected drift unchanged.
Signed permutations preserve the Schur and third-influence bounds, hence
the average preserves them too. The resulting extension has the symmetry
needed above. Boundary carriers of a free box require separate treatment:
a charge closed in the free complex need not remain closed after zero
extension across its boundary.

For delta<1/2 the bound on B_eff makes the denominator positive. The exact
centered auxiliary MGF domination, if preserved by the matched state
limit, supplies kappa<=1. The Hessian/score lower bound from the full-flux
note supplies kappa>0. These inequalities should be checked against the
direct response bound; they are not an excuse to select b by hand.

## 4. Constructing and matching an infinite state: still open

One possible construction uses a stationary Gaussian OU field zeta with
covariance E zeta_t zeta_s*=exp(-|t-s|)K. Solve the causal equation

 omega_t=zeta_t+integral_0^infinity exp(-s)K R'(omega_(t-s))ds. (9)

In the Hilbert space of stationary random fields with finite per-site
second moment, the intended map is a contraction with norm delta. This
requires a precise definition of K on the environment spectrum and a
fixed extension R'; an arbitrary nonlocal pointwise convolution is not
defined merely by K being bounded on deterministic ell2. An equivariant
factor of an ergodic Gaussian path field would be ergodic, but the
Gaussian ergodicity and the contraction space must both be checked.

To show that(9) is the auxiliary Gibbs thermodynamic limit, a potential
route is to average translates of finite free-box stationary processes.
The explicit reflection representation controls the bulk Gaussian K.
Strong convexity yields concentration bounds for local R' observables;
these may permit nonlocal K tails to be controlled in ell2. Pointwise
tail summation in ell1 is not available for the massless projection.
Any limiting process would then solve(9); uniqueness in the stationary
class would identify it. A proof has to control boundaries, source
response, and the order of the thermodynamic and continuum limits.

Take the thermodynamic limit first for each compactly supported h_a,
then a->0, unless a separate uniform macroscopic boundary result is
proved. Finite periodic approximations are another route, but their
harmonic and winding charges cannot be dropped without estimates.

Even a unique ergodic auxiliary gradient law does not immediately make
the original angle law ergodic. The angle/image state must be matched
separately for a constant conditional image variance and the physical
score reconstruction. Preserve this distinction in every conclusion.

## 5. Decisive checks and current decision

1. Derive the spatial conjugation and fiber conventions exactly; verify
   them on a finite periodic random-phase environment.
2. Challenge(6) against exact Gaussian covariance inversion with periodic
   Hessians. Include a case where the mean-Hessian shortcut fails.
3. Establish the stationary response identity and boundary/state match,
   or retain them as explicit conditional hypotheses.
4. Only then combine(8) with the finite-volume Gaussian remainder and
   the exact physical flux/score maps. No finite-clock conclusion follows.

This is an exploratory proof design. Its value is a specific possible
mechanism for covariance homogenization and a finite effective matrix,
not a declaration that the fixed-law photon theorem is complete.
