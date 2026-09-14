---
claim_id: finite_step_gaussian_gauge_canonical_logarithm_and_coulomb_cost_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For an explicitly supplied noncompact canonical Gaussian transfer with positive temporal and spatial coefficients and a finite-range positive semidefinite spatial quadratic form, its exact logarithm has exponentially approximable canonical coefficient matrices without a positive mass assumption. On cubic link fields this gives a volume-uniform Weyl commutator bound, two transverse oscillator branches after a declared Gauss reduction, and a static charge cost with a derived Coulomb asymptotic. A separate finite-dimensional identity gives the inverse logarithmic response and a double-commutator estimate. The finite-clock phase and native Record realization are open."
upstream_dependencies: []
runner: scripts/finite_step_gaussian_gauge_canonical_log_2026_09_14.py
---

# Finite-step Gaussian gauge transfer: canonical locality and charge cost

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The exact logarithm of the supplied Gaussian transfer below has exponentially
decaying coefficients in the original field and momentum variables even when
its transverse modes are gapless. A positive integral representation proves
this with constants independent of volume. The same model has two transverse
branches and an exactly calculated static charge cost. The result is a
noncompact comparison construction; it does not establish an interacting
finite-clock photon phase or derive a physical law from the native axioms.

## Machine status and exact target

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "The massless Gaussian comparison transfer needs a locality proof in its canonical field algebra, with zero modes and physical constraints treated explicitly."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Use the exact Gaussian coefficients as a comparison target; an interacting finite-clock transfer still needs a noncircular local-log construction and its own phase estimate."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit heat-kernel, resolvent, canonical-evolution and Fourier derivations for a supplied noncompact Gaussian model; a separate finite-matrix response identity is proved directly."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The quoted target was identified during the personal campaign at
`ed04c85c34`, started from main revision
`5deabeb698a27c2c3f68c5df685af2521ef15307`. This note re-establishes all
mathematical objects and proofs it uses. Its claim is the declared Gaussian
comparison and finite-matrix identity; the compact interacting target is
not treated as closed.

## Supplied objects and framework boundary

The canonical real fields, their CCR representation, the noncompact Gaussian
transfer, its positive couplings, and the Gauss constraint/reduction are
supplied mathematical definitions. A vacuum requires the zero-mode treatment
specified below. They are not consequences of the Lattice, Qubit,
Admissibility and Record baseline in `docs/MINIMAL_AXIOMS_2026-06-29.md`.
The approved scale-reference, kinetic-isotropy and realized-state primitives
retain their stated roles and select none of this construction's dynamics,
state, coupling, representation or physical time.

There are no observational fits or imported phase theorems. The oscillator
heat kernel, resolvent series, canonical commutator estimate and Coulomb
asymptotic are proved below. The elementary partial-fraction identity for
coth is used in the finite-matrix appendix with its convergent representation
shown. The primary runner reads no scientific repository inputs or integrity
files. All finite checks are author checks, with independent review pending.

The earlier `TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`
is context: its stated free positive-energy bilinear carrier differs from
the canonical field algebra here. A frequency function alone is insufficient
to identify the spatial coefficients of the original canonical Hamiltonian.
No claim or audit status is imported from that note.

## B. Gaussian test: keep the canonical field algebra

Let x,p be m canonical real coordinates, [x_i,p_j]=i delta_ij, and let
K be a real symmetric positive semidefinite finite-range matrix. In a
family of volumes assume a common finite range and upper bound K<=Lambda I.
Supply positive beta_t,beta_s, fixed across that family. Define the positive transfer on L2(R^m):

    T = exp(-beta_s x.K.x/4)
        exp(-p.p/(2 beta_t))
        exp(-beta_s x.K.x/4).                              (B1)

Its kernel is a product Gaussian with exponent

    -beta_t ||x-y||^2/2 - beta_s(x.K.x+y.K.y)/4.

Diagonalize K orthogonally. For eigenvalue lambda>=0, set

    r=beta_s lambda/beta_t,
    omega(r)=2 asinh(sqrt(r)/2),
    f_G(r)=omega(r)/sinh(omega(r)),  f_G(0)=1.               (B2)

Comparison with the oscillator heat kernel gives the EXACT logarithm

    -log T = (p.A(K).p + x.B(K).x)/2,
    A(K)=beta_t^-1 f_G(beta_s K/beta_t),
    B(K)=beta_s K (I+beta_s K/(4 beta_t))
                         f_G(beta_s K/beta_t).             (B3)

No arbitrary scalar is dropped: the Mehler prefactor equals that in
(B1), since omega/(A sinh omega)=beta_t. At lambda=0 the continuous
limit is the free-particle heat operator. Its zero mode has no normalized
L2 ground vector; any vacuum or trace statement needs an explicit zero-mode
prescription. Positive lambda modes have frequency omega and zero-point
energy omega/2.

For completeness the kernel comparison does not require an imported
reconstruction theorem. At time t>0 put

    a_t=omega coth(omega t)/A,
    c_t=omega csch(omega t)/A,
    N_t=sqrt(omega/[2 pi A sinh(omega t)]).

The kernel N_t exp[-a_t(x^2+y^2)/2+c_t xy] solves
partial_t K_t=(A partial_x^2/2-B x^2/2)K_t: use
a_t'=-A c_t^2=B-A a_t^2, c_t'=-A a_t c_t, and
N_t'/N_t=-A a_t/2. Its t->0 kernel is the Gaussian delta sequence.
This identifies the positive oscillator heat semigroup. At t=1,
a_1=beta_t+beta_s lambda/2, c_1=beta_t, and
N_1=sqrt(beta_t/(2 pi)), exactly the original kernel (B1).

The positive integral representation is

    f_G(r)= integral_0^1 du/[1+(r/4)(1-u^2)].               (B4)

It follows by elementary integration, using
atanh(sqrt(r/(4+r)))=asinh(sqrt(r)/2). In particular f_G is analytic
at r=0. Nonanalyticity of the positive frequency omega~sqrt(r) does NOT
imply nonlocality of the canonical coefficients A and B.

If 0<=K<=Lambda I and a=beta_s/(4 beta_t), then each resolvent in (B4)
has the norm-convergent shifted expansion

    (I+cK)^-1 = (1+c Lambda)^-1
        sum_{n>=0} [c(Lambda I-K)/(1+c Lambda)]^n,
    0<=c=a(1-u^2)<=a.                                     (B5)

Its truncation after n=M has norm error at most

    [a Lambda/(1+a Lambda)]^(M+1).                         (B6)

Every polynomial term has range at most M times the range of K. Integrating
gives a volume-uniform exponential approximation for A(K); multiplication
by beta_s K(I+aK) gives one for B(K), with two additional K ranges and
prefactor beta_s Lambda(1+a Lambda). This proof requires an upper spectral
bound and finite range, not a positive lower spectral bound.

For the supplied cubic Maxwell quadratic form K=curl* curl on oriented
links, a direct Fourier incidence calculation gives Lambda=12.
Its nonzero momentum transverse eigenvalues are
lambda(k)=4 sum_j sin^2(k_j/2), each twice. The longitudinal eigenvalue
is zero. Imposing the Gauss constraint and treating global zero modes
separately leaves two modes with

    omega(k)=2 asinh(sqrt((beta_s/beta_t) lambda(k))/2).

This remains a NONCOMPACT GAUSSIAN comparison model. Compact defects,
finite clock dimension, actual interacting state estimates, a native
Record map, and a selected physical time are not established by (B3).

## C. Local canonical propagation and the zero-mode distinction

Write a link as (x,j), x in Z^3 and j in {1,2,3}. In this paragraph distance
means the infinity distance between anchors x, including its periodic
version on tori. A single factor K=curl* curl changes this distance by
at most one. Set q=a Lambda/(1+a Lambda), with Lambda=12. For distinct
anchors at distance n>=1, truncating (B5) at M=n-1 gives

    |A_{(x,i),(y,j)}| <= beta_t^-1 q^n.                    (C1)

For B, use degree M+2 in its approximation. The same argument, with the
spectral norm bound at n<=2, gives

    |B_{(x,i),(y,j)}| <= C_B q^max(n-2,0),
    C_B=beta_s Lambda(1+a Lambda).                         (C2)

These also give bounds at equal anchors by taking n=0. For any mu>0
with z=q exp(mu)<1, the weighted row sums are uniformly finite:

    S(z)=3+72 z(1+z)/(1-z)^3+6z/(1-z),
    J_mu=S(z) max(beta_t^-1, C_B q^-2).                    (C3)

There are at most 3 choices of orientation at an anchor, and
3[(2n+1)^3-(2n-1)^3]=72n^2+6 entries in shell n. This proves (C3)
for every torus as well: periodic shells have no more entries than these
infinite-lattice shells. The constant is deliberately coarse.

For H in (B3), the real-time canonical equation is

    d/dt (x,p)^T = L (x,p)^T,
    L = [[0,A],[-B,0]].                                    (C4)

The weighted maximum row-sum norm is submultiplicative, by the triangle
inequality for distance. Therefore exp(tL) has weighted row norm at most
exp(J_mu |t|). For finitely supported real canonical test vectors f,g,
write W(f)=exp(i f.(x,p)). The Weyl relations then imply

    ||[tau_t(W(f)),W(g)]||
       <= ||f||_1 ||g||_1 exp(J_mu |t|-mu dist(supp f,supp g)). (C5)

Use the minimum of this bound and 2 if desired. This is a volume-uniform
propagation bound for bounded Weyl observables of the supplied Gaussian
canonical theory. It does not apply a bounded-spin Hamiltonian theorem to
unbounded oscillator terms. A direct matrix evolution and the Weyl algebra
are the proof. The energy quadratic form is nonnegative; its closure gives
the finite-system oscillator/free-particle Hamiltonian. On the infinite
lattice, take the Weyl algebra over real l1 canonical test vectors; the
bounded weighted row sums make exp(tL)^T a bounded map on l1 and hence
define its linear symplectic evolution. Local observables mean Weyl
operators with finitely supported test vectors. This does not assert
operator-norm convergence of Weyl operators under truncation of their
test vectors: Weyl operators are not norm-continuous in that parameter.
The exponential statement here is about the canonical kernels and the
commutator estimate (C5).

Let d_j(k)=exp(i k_j)-1. The three oriented curl rows are

    (-d_2,d_1,0), (-d_3,0,d_1), (0,-d_3,d_2).

Consequently K(k)=lambda(k) I-d(k)d(k)*, with lambda=sum|d_j|^2.
For k!=0 this has one longitudinal zero eigenvalue and two eigenvalues
lambda. This proves the mode count and Lambda bound for all momenta,
not just the finite grids in the runner. For small k,

    omega(k)=sqrt(beta_s/beta_t)|k|+O(|k|^3).               (C6)

The local algebra must be declared before reducing constraints. The
transverse projector contains a 1/lambda factor and is not a local
coordinate change. Equations (C1)–(C5) concern the original link canonical
algebra; gauge-invariant observables form a subalgebra. The local electric
field and curl field have local commutators there. Removing longitudinal
coordinates is not a reason to substitute a positive-frequency occupation
kernel for A and B.

There are 3 global harmonic link modes on a periodic three-torus as well
as the gradients. At finite volume the noncompact harmonic free particles
do not have normalizable zero-momentum ground vectors. One may remove the
harmonic canonical pairs by a supplied phase-space reduction, use boundary
conditions without these modes, or define the infinite-volume Gaussian
state directly on local gauge-invariant observables. One may not claim a
unique normalized finite-torus vacuum for the unreduced transfer (B1).

## D. Gaussian vacuum and static charge cost, with their premises

On any positive eigenvalue lambda, the normalized oscillator vacuum gives

    <x^2> = 1/[2 sqrt(beta_s beta_t) sqrt(lambda) sqrt(1+a lambda)],
    <p^2> = sqrt(beta_s beta_t) sqrt(lambda) sqrt(1+a lambda)/2,
    <{x,p}>/2 = 0.                                        (D1)

The two transverse polarizations have these covariances. On the infinite
cubic lattice their infrared integrals are finite for local test fields
in three dimensions. For the curl observable, multiply its position
covariance by F and F*, removing the inverse square-root singularity.
These covariances saturate the oscillator uncertainty relation in each
transverse mode. The corresponding finite reduced Gaussian characteristic
functions have limits for local gauge-invariant tests; their finite Gram
matrices remain positive in the limit. This defines the free vacuum on the
gauge-invariant Weyl algebra with the stated Gauss relations and zero-mode
prescription. It has two gapless transverse modes. This
is a property of the explicitly supplied noncompact theory, not a
finite-clock or Record-law result.

An additional exact check is a static quadratic charge-sector minimization.
Let G be the vertex-to-edge gradient, Delta=G*G, and rho be a finite-box
net-zero charge vector. Work on the range of Delta, using its inverse
there. Since K G=0, (B3) gives A G=G/beta_t. The constrained minimizer
of the electric quadratic form at G* E=rho is

    E_L = G Delta^-1 rho,
    min (E.A.E)/2 = rho.Delta^-1.rho/(2 beta_t).            (D2)

Every allowed E is E_L+E_T with G*E_T=0. Their cross term vanishes and
E_T.A.E_T>=0, proving the minimum. In a supplied canonically reduced
charge-sector quantization, this same constant shifts the transverse
Hamiltonian, since its coefficients are independent of rho. This does
not construct normalizable eigenvectors of the continuous Gauss operator
inside the unreduced L2 Hilbert space. Equation (D2) itself is a finite
quadratic minimization statement.

The infinite-lattice Green function is

    G(x)=integral_BZ exp(i k.x)/lambda(k) d^3k/(2 pi)^3.

Its integrable singularity in three dimensions gives a direct Coulomb
asymptotic. Take a smooth radial cutoff chi supported inside the Brillouin
zone, equal to one near zero. The remainder

    R(k)=1/lambda(k)-chi(k)/|k|^2

is smooth off zero, bounded near zero, and has second derivatives
O(|k|^-2) there. These derivatives are integrable in three dimensions;
there are no point-supported derivative terms because the boundary terms
on a small sphere vanish. Twice integrating its Fourier coefficient by
parts in a component with |x_j|>=|x|/sqrt(3) bounds it by O(|x|^-2),
uniformly in direction. The singular cutoff term has radial transform

    [1/(2 pi^2 |x|)] integral_0^infinity chi(s) sin(|x|s)/s ds.

The same integral with chi=1 is pi/2, as follows from exponential
regularization and the identity integral exp(-epsilon s) sin(r s)/s
ds=atan(r/epsilon). Its difference from the cutoff integral is O(1/r)
by one integration by parts: the derivative of (1-chi(s))/s is integrable,
and its boundary values vanish. Therefore

    G(x)=1/(4 pi |x|)+O(|x|^-2).                           (D3)

For opposite unit static charges separated by fixed x, the torus sums
in (D2) have bounded integrand (1-cos(k.x))/lambda(k), whose Riemann limit
is [G(0)-G(x)]/beta_t. After subtracting their separation-independent
self-energy, the interaction is -1/(4 pi beta_t |x|)+O(|x|^-2).
This is the electrostatic cost in the supplied Gaussian reduction.

## A. Appendix: exact finite-matrix inverse logarithmic response

Let T0 be a strictly positive finite-dimensional matrix, V=V*,
T(s)=exp(s V/2) T0 exp(s V/2), and H(s)=-log T(s). For real s,
T'(s)={V,T(s)}/2. In an eigenbasis of H(s), Duhamel differentiation gives

    T'_{ab} = -H'_{ab} (exp(-E_a)-exp(-E_b))/(E_b-E_a).

The diagonal/coincident-energy value is the continuous extension. Therefore

    H'(s) = -f(ad_H(s))(V),
    f(x) = (x/2)coth(x/2),  f(0)=1.                         (A1)

This formula is even in x and preserves Hermiticity. It has no small-s or
many-body gap hypothesis. It is a finite-dimensional identity, not yet a
local-interaction existence theorem.

The partial-fraction identity for coth gives

    f(x) = 1 + 2 sum_{n>=1} x^2/(x^2+(2 pi n)^2).           (A2)

For a direct derivation, the periodic Green kernel of -partial_t^2+x^2
on a circle of length one, for x!=0, is
cosh(x(1/2-|t|))/(2x sinh(x/2)), -1/2<=t<=1/2. Its derivative has jump
-1 at zero and is periodic at the endpoints, so its Fourier coefficients
are 1/(x^2+(2 pi n)^2). The series is absolutely convergent. Evaluate at
t=0 and multiply by x^2 to obtain (A2); x=0 follows continuously.

Writing tau_t(W)=exp(i t H) W exp(-i t H), one useful absolutely integrable
version is

    f(ad_H)V = V + integral_0^infinity q(t)
                    [tau_t(W)+tau_-t(W)] dt,
    W = [H,[H,V]],
    q(t) = -log(1-exp(-2 pi t))/(2 pi).                     (A3)

Indeed q(t)=sum_{n>=1} exp(-2 pi n t)/(2 pi n), and integrating
2 q(t) cos(tx) gives 2 sum_n 1/(x^2+(2 pi n)^2). Multiplication by x^2
recovers (A2). The kernel has only an integrable logarithmic singularity
at zero, exponential tails, and integral_0^infinity q(t) dt=1/24.
Thus a dimension-independent finite-matrix estimate is

    ||f(ad_H)V - V|| <= ||[H,[H,V]]||/12.                  (A4)

If H is a sum of uniformly bounded finite-range terms on a bounded-degree
lattice and V is bounded with fixed support, the double commutator has
bounded nearby support and norm. A volume-uniform Lieb-Robinson bound
can then localize (A3).
But using this observation as a proof that the unknown H(s) is local is
circular. A volume-uniform interaction-space flow, or another noncircular
construction, remains necessary. This is the explicit stop condition for
the interacting route, unless such a construction is found.

The alternative singular kernel

    k(t)=2 pi exp(-2 pi t)/(1-exp(-2 pi t))^2

acts on 2V-tau_t(V)-tau_-t(V); its apparent t^-2 singularity cancels.
Equation (A3) is preferable for norm estimates and numerical checks.


## Proof obligations and verification

| Obligation | Argument | Scope |
|---|---|---|
| Exact transfer logarithm, including its scalar | Gaussian heat equation and kernel normalization | Finite real canonical system |
| Coefficient locality | Positive resolvent integral and finite-range polynomial approximation | Uniform in volume, including zero mass |
| Propagation | Weighted matrix norm and Weyl relations | Local Weyl commutators; no norm-continuity claim for Weyl smearing |
| Gauge modes and vacuum | Cubic incidence and oscillator covariances | Supplied Gauss reduction and stated zero-mode prescription |
| Static charge response | Quadratic constrained minimization and Fourier asymptotic | Noncompact Gaussian charge sector |
| Inverse log response | Duhamel differentiation and integrable kernel | Finite-dimensional strictly positive matrices |

The Gaussian and finite-matrix claims have the hypotheses explicitly displayed
above. For a non-Gaussian transfer, the locality of an unknown logarithm does
not follow merely from the appendix: inserting its own locality as a premise
would be circular. Compact defects, finite clock dimension, its actual
interacting vacuum and phase, native carrier/resource compilation, and law
selection remain separate research obligations.

The primary runner performs five finite families. It compares the inverse
response with both a resolvent Frechet integral and matrix-log differences;
checks the real-time kernel and an incorrect reciprocal multiplier; integrates
the ORIGINAL Gaussian transfer kernel against oscillator eigenfunctions and
checks two-step convolution; builds cubic gradient/curl incidence and checks
its full spectra on two tori; checks a separate canonical matrix product,
polynomial tails and spatial kernel bounds; solves charge-constrained KKT
systems; and computes the Green function through a separate Bessel heat
kernel. Its finite asymptotic samples test, but do not prove, (D3).

Reproduce with:

```bash
python3 scripts/finite_step_gaussian_gauge_canonical_log_2026_09_14.py
```

The paired canonical output is
[the runner cache](../logs/runner-cache/finite_step_gaussian_gauge_canonical_log_2026_09_14.txt).

## Proof-pattern references

The inverse response is the reciprocal of the anticommutator multiplier in
section 10.1.1 of [Capel, Moscolari, Teufel and Wessel,
From Decay of Correlations to Locality and Stability of the Gibbs State](https://link.springer.com/article/10.1007/s00220-024-05198-x).
[Hastings, Quantum Belief Propagation](https://arxiv.org/html/0706.4094)
is earlier context for a real-time representation of an exponential response.
Their local-Hamiltonian hypotheses do not establish locality of an arbitrary
positive transfer's logarithm. The identities used here are derived in the
appendix; no interacting locality or phase theorem is imported.

## Review record

Personal author mathematical and scope review; independent review and audit
pending. The review corrected an overly broad infinite-volume Weyl-algebra
sentence: the dynamics is defined on l1 test vectors, and the stated locality
conclusion is a kernel and commutator bound. Truncating a Weyl test vector
does not give operator-norm convergence of the Weyl operators. The finite
noncompact harmonic zero modes are also kept explicit.

Nine source mutations against primary SHA-256
`f5a46907dadbc10e944e62bbad1f565879083cde2b3af05249095fe5c2e193be`
all terminated with relevant assertion failures: the inverse-response
reciprocal; half the real-time kernel; an omitted magnetic coefficient;
the omitted vacuum scalar; a reversed curl sign; a conjugated Fourier
orientation; a falsely faster polynomial tail; incorrect temporal
normalization of the charge cost; and a halved heat-kernel clock. These
are checks by the author, not independent review. The canonical cache
binds the final runner and its execution envelope.
