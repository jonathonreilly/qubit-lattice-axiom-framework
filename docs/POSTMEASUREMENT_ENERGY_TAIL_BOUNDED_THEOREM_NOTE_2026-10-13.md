---
claim_id: postmeasurement_energy_tail_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
upstream_dependencies:
  - chirped_kinetic_energy_bounded_theorem_note_2026-10-13
  - multitime_kinetic_energy_bounded_theorem_note_2026-10-13
runner: scripts/energy_tail_identity_2026_10_13.py
bare_retained_allowed: false
audit_required_before_effective_retained: true
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: supports
conditional_surface_status: Explicit supplied model and provisional normal-state weak-law dependency.
hypothetical_axiom_status: No physical axiom added.
admitted_observation_status: No empirical observation imported.
claim_type_reason: Analytic bounded theorem with unchanged checked cores and declared conditional dependencies.
next_trace_action: Root publication review and regular PR; independent audit remains separate.
---

# Finite-first-energy tails after bounded energy protocols

Claim type: bounded_theorem

This note separates a uniform energy-tail theorem from a limiting-law corollary.
The tail theorem assumes the explicit common-energy graph bounds below. The
normal-state law, means and Wasserstein corollary additionally assume the
reviewed prepared-state weak-law theorem archived in this packet. That theorem
is a supplied provisional scientific dependency; the canonical vacuum
multi-time parent does not establish it. Identity tools check bytes only.

This is upstream support for possible physical-realization work. No named
downstream physical consumer is yet established, so target claim and blocker
fields are null. The user requested this energy-tail publication milestone;
physical realization and independently retained status remain outside the
supplied-model theorem.

The mathematical cores below are the complete unchanged root306, independent390
and scoped countercontrol84. Their earlier acceptance is preserved with the
subsequent required J-type precision. There is no new independent derivation,
retained audit, physical realization or operator-domain formal certificate.

## Main theorem and exact quantifiers

Let H be a nonnegative self-adjoint free energy on the common Hilbert space and
A=1+H. Let Y and its inverse range over the permitted unitary segments, with
uniform bounds on A Y A^{-1} and A Y^{-1} A^{-1}. These are bounded extensions
of maps preserving D(H), with common constants over the stated parameter
resources. The corresponding half-graph bounds follow by interpolation.
Let P_j be spectral projections of this same H and let Q be any correctly
ordered finite product of these segments and projections, with a fixed upper
bound on the number of factors. Thus Q is a contraction, and A Q A^{-1} and
A^{1/2} Q A^{-1/2} have common bounds C_2 and C_1.

For every fixed normal density rho with Tr(H rho)<infinity, put
rho_K=P_K rho P_K with P_K=1_{[0,K]}(H), and

d_E(rho,sigma)=||A^{1/2}(rho-sigma)A^{1/2}||_1.

The cutoff argument in the complete cores proves, for R>0 and K>=0,

    Tr[H 1_(R,infinity)(H) Q rho Q*]
      <= C_1^2 d_E(rho,rho_K)
         + C_2^2 (1+K) Tr[A rho]/R.

Since d_E(rho,rho_K)->0, the left side tends to zero uniformly over the allowed
Q as R tends to infinity. Only finite initial first energy is required: no
second moment, Gaussianity, parity, purity or energy-diagonal assumption.
The uniform tail assertion itself permits arbitrary spectral bins under the
common graph bounds. Regular fixed boundaries enter the weak-law corollary.

For weighted-trace-compact families of initial states, the common initial-tail
modulus yields a uniform version. For varying rho_a with d_E(rho_a,rho)->0,
the conclusion is the limiting statement

    lim_(R->infinity) limsup_(joint (a,h)->0)
      Tr[H 1_(R,infinity)(H) Q_(a,h) rho_a Q_(a,h)*] = 0.

This does not assert a supremum over every point of an arbitrary fixed
punctured continuum neighborhood. Such a supremum requires compactness or a
uniform initial-tail modulus. Fixed rho ideal and actual families satisfying
the common graph bounds do have a genuine uniform tail bound.

## Conditional normal-state law, means and W1

For the supplied massive CAR model H=dGamma(E), E>=m>0, the accepted strict-gap
chirp estimates provide the weighted one-particle inputs used in root U1-U9 and
independent T1-T19 to obtain the required graph bounds. The fixed smooth slots,
real bounded-variation envelope resources, strict carrier gap, finite horizon
and small h are those of the archived accepted premises; none is broadened.

Assume additionally the normal-state finite-protocol weak-law theorem in the
full prepared root340 and independent512, with its state-specific boundary
criterion, common H, exact Lüders ordering and finite fixed protocol. Then the
UI theorem upgrades its unnormalized output energy laws to convergence of
first moments and, after normalization on an event with limiting probability
p>0, to W1 convergence and convergence of conditional means. Uniform conditional
statements need a uniform positive lower bound on event probabilities. The
limiting representation retains the shared initial energy variable X_0 and the
accepted marked compound-Poisson increments with the stated measurement
conditioning; independent fresh initial variables cannot be substituted.

This implication does not infer weak convergence from graph bounds. It does
not add a path-space law, growing protocol length, moving-boundary limit,
feedback control or a conclusion on vanishing-probability postselection.
The complete prepared arguments, comparison, acceptance and historical open-Q25
wording remain archived. The current theorem closes their tail obligation
separately, under the hypotheses stated here. Optional compact-preparation
composition remains conditional on its accepted weighted compactness premises.

## Actual-cell transfer retained at its accepted scale

Use the exact same H and Lüders instruments through the stated embedding. The
accepted comparison supplies the graph Duhamel argument under bounded
self-adjoint controls, bounded errors ||Delta V||<=d_0 epsilon, bounded
commutator errors ||[H,Delta V]||<=d_1 epsilon, and common commutator bounds
||[H,V]||, ||[H,V_a]||<=k, with the domain/measurability hypotheses in the cores.
For b<=A_0 tau/h it gives graph error bounded by

    epsilon [(d_0+d_1)b + d_0 k b^2].

Thus epsilon=o(h^2) supplies this packet's actual-cell transfer. The independent
proof's original extra-graph reservation is resolved by the compared root
argument at precisely these hypotheses. Calibration, embedding, common H and
instruments remain assumptions. No later relative-graph sharpening or threshold
composition is imported into this publication.

## Required precision and preserved controls

Independent390 lines79-80 call J antiunitary. Read J=Gamma C as linear, unitary
and energy intertwining: Gamma and C are separately antilinear, so their
composition is linear. The original sentence remains unchanged below. The
T5 Hilbert-Schmidt inequalities use its energy-isometry property and retain
the same formulas and bounds. The subsequent inverse, domain and positive-column
arguments use Gamma directly and do not change. The accepted precision addendum,
author check and root corroboration supersede only the earlier no-correction
wording. See [precision](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989/.claude/science/physics-loops/toe-energy-tail-20261013/J_PRECISION.md).

The high-rank countercontrol preserves a failure of inference from weak energy
convergence and one-particle operator smallness alone to uniform first tails.
It lies outside the fixed-slot family. The single-pair control separates graph
norm requirements and itself has UI. Neither is a universal impossibility
claim. The N1-N8 packet remains FAIL / partial-narrowing; no five route families,
wall independence or negative certificate is invented.

## Evidence and publication boundaries

The canonical direct parents are the
[strict-gap chirped kinetic-energy theorem](CHIRPED_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and the [vacuum finite-multi-time energy theorem](MULTITIME_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md),
at the existing regular PR9521 base. Initial-state PR9518 remains sibling
provenance. No combined ancestry or canonical edge to the unpublished prepared
sources is asserted. [Dependency bindings](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989/.claude/science/physics-loops/toe-energy-tail-20261013/IMPORTS.json)
and the complete archive identify every supplied source and scope.

The finite-Fock diagnostic is archived only as finite algebra evidence, with
its actual recorded execution; it cannot certify continuum domains or limits.
A separate Lean run compiled only the final scalar common-modulus cutoff
implication. Its actual axiom receipt lists propext, Classical.choice and
Quot.sound. It formalizes no CAR, unbounded-operator domain, trace inequality,
physical embedding or law/W1 passage. Historical pre-compilation source prose
is preserved alongside the later compiler receipt. See
[scalar evidence](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989/.claude/science/physics-loops/toe-energy-tail-20261013/LEAN_SCOPE.md).

All source archives, exact extraction maps and raw diffs are available through
[the archive guide](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989/.claude/science/physics-loops/toe-energy-tail-20261013/ARCHIVE_GUIDE.md).
Raw unified diffs are compressed without rewriting their literal context
markers. The proposed runner evaluates zero mathematical predicates and supplies
no independent scientific review. Root execution and publication remain pending.

## Unchanged root proof (306 lines)


Review-loop integration: exact current main a3ccb945b1543e31361f1c6fefd2cc7ab7d31d5f plus this batch supplies the live parent sources. Immutable mathematical bodies and original archives are unchanged. Live parent hashes and core coordinates are refreshed, with original identities preserved. Historical acceptance and pending labels are provenance, not audit authority.

# Energy tails after fixed finite measurement protocols

Status: provisional conditional root derivation, following the sealed plan.
No independent solution to this new target has been opened. This proof uses
already checked strict-gap chirp estimates and addresses Q25 of prepared512.
It changes no frozen parent and makes no retained, numerical or Lean claim.
Section5 explicitly depends on the prepared-multitime probability theorem;
its newly frozen exposed comparison still awaits root reading. The tail bound
U3 itself does not depend on those limiting-probability assertions.

## 1. Exact setting and target

Use the supplied massive free CAR model and notation of initial-state407
and strict-gap chirp515V2/850. On K let D be the real signed generator,
E=|D|>=m>0, P its positive spectral projection and P_-=I-P. The conjugation
Gamma exchanges P and P_- and commutes with E. On fermionic Fock over PK,
H=dGamma(E), N=dGamma(I), A=I+H and S=A^(1/2). Thus N<=H/m.
The controls are the fixed real compact smooth slots; BV amplitude/frequency,
positive strict gap above2m and finite kinetic horizon retain all parent
hypotheses. No threshold-crossing extension is used here.

For each small h and prefix tau, the Fock interaction implementer is Y and
the real unitary one-particle map is Z. Use the convention
Y*b(k)Y=b(Z*k). Put u=PZP, beta=PZP_-, gamma=P_-ZP and d=P_-ZP_-.
The parents supply, uniformly over the fixed resources and prefixes,

  ||Z-I||<=C eta_h, ||E(Z-I)||<=C eta_h,
  ||E(Z-I-K1)||_HS<=C eta_h,
  eta_h=sqrt(h log(2+h^(-2))).                         (U1)

Weighted products in U1 are their already justified bounded extensions.
We will also justify from the parent spectral kernel

  ||E beta||_HS<=C.                                   (U2)

The target is a uniform integrability assertion for finitely many fixed
Lueders projections P_j=Y_j* 1_(B_j)(H) Y_j and C_h=P_n...P_1. Bins
are arbitrary Borel sets for the tail bound; regularity is required only
when invoking the checked limiting probability theorem. For a final prefix
tau_f and any fixed normal rho with Tr(rho H)<infinity, prove

 lim_(R->infinity) sup_(h small, allowed drives)
 Tr[H 1_(R,infinity)(H) Y_f C_h rho C_h* Y_f*]=0.       (U3)

This is Q25, since A_h(tau_f)=Y_f* H Y_f. The number n is fixed. These
are coarse projective instruments, not a claim about a continuous-spectrum
fine measurement channel, infinitely many observations, or arbitrary Kraus
operators. The constants may grow with n.

## 2. Second one-particle weight and inverse implementer

The exact pair amplitude in chirp H21 gives the output-weight bound

 ||E beta1||_HS^2
   <=2h^2 integral e^2 r(e)|I_(h,T)(e)|^2 de.           (U4)

Indeed the output particle energy squared is bounded by the total pair
energy squared in the nonnegative kernel integral. No exact factor for
this second moment is being inferred from the first-moment identity.
For b(e)=e^2 r(e), extended by zero, the general-control parent threshold
analysis gives an integrable correlation kernel C_b(t)=integral b(e)e^(ite)de.
Multiplication by the fixed polynomial preserves the smooth rapidly decaying
interior and the linear threshold vanishing that produced O((1+|t|)^(-2))
in the parent argument. In particular ||C_b||_1<infinity. Exact finite-time
Fubini, followed by the absolute kernel bound, yields

 integral b(e)|I_(h,T)(e)|^2de <= A_star^2 T ||C_b||_1.

Together with T<=tau_star/h^2 and the q=2 remainder U1 this proves U2.
This uses no independence of emissions and no already assumed Fock H^2
moment. It is a weighted one-particle Hilbert--Schmidt estimate.

For Z*=Z^(-1),

 E(Z*-I)=-E(Z-I)Z*,

so the full left weighted operator bound is also O(eta_h). For sufficiently
small h, d is invertible with ||d^-1||<=2. Unitarity gives
  u* beta+gamma* d=0.
Equivalently, gamma*=-u* beta d^-1. Hence the off-diagonal block of Z* obeys

 ||E gamma*||_HS
 <=2(||E beta||_HS+||E(u*-I)|| ||beta||_HS)<=C.          (U5)

The second term is legitimate because beta is HS, ||beta||_HS<=||E beta||_HS/m,
and E(u*-I) is bounded by the full inverse operator bound. This step avoids
incorrectly identifying left- and right-weighted Hilbert--Schmidt norms.
The weighted operator and off-diagonal HS hypotheses needed below therefore
hold for the inverse implementer Y*. No inverse Born remainder is asserted.
They hold also for full-picture propagators after a free factor, since all
powers of A commute with that free unitary.

## 3. Uniform D(H) graph bound

We prove a Fock graph estimate that is stronger than the previously used
form estimate Y*HY<=C(H+I):

 ||A Y A^-1||<=C_G, ||A Y* A^-1||<=C_G.               (U6)

First, for each fixed h and finite T, Y and Y* preserve D(H). The fixed
bounded quadratic V preserves D(H) and has bounded [H,V]. On a domain
core, Duhamel gives ||[H,W(t,s)]||<=k integral_s^t |lambda c(v)|dv;
closure then proves domain preservation. This bound is finite for each h,
although its O(h^-1) size is not used as the uniform bound U6.

Choose an orthonormal basis (e_i) of PK lying in D(E), and use Gamma e_i
on P_-K. Finite-particle vectors formed from D(E) are a graph core of H.
Normal ordering the exact transformed energy, or polarizing initial407 I14,
gives on this core

 Y* H Y = H+dGamma(C_0)+Pi_B+Pi_B*+c_0 I,             (U7)

 c_0=Tr(E beta beta*),
 C_0=u* E u-E-Gamma(beta* E beta)Gamma,
 B=beta* E u=(E beta)* u,
 Pi_B=-sum_(i,j) B_(j,i) a(e_i)a(e_j),
 B_(j,i)=<Gamma e_j,B e_i>.

The antiunitary conjugations in C_0 map the negative band to the positive
band. Pi_B uses the matrix of B between the stated bases. Its skew part
alone contributes. With inner products linear in the second slot, the
anomalous block has kappa_(i,j)=Tr(rho a(e_i)a(e_j)); thus Pi_B+Pi_B* has
expectation -2 Re Tr(B kappa), exactly the two anomalous terms in I16.
The normal term and c_0 likewise reproduce I14/I16 with their signs.

Here C_0 is bounded, despite the individual unbounded E terms. Set L=u-I.
On D(E),

 u* E u-E=L*E+EL+L*EL,

where EL is bounded O(eta_h) and L*E=(EL)*. The hole term beta*E beta
is bounded by ||beta|| ||E beta||, using the small weighted operator bound
for E beta as well. Consequently ||C_0||<=C, uniformly (in fact it vanishes).
Also ||B||_HS<=||E beta||_HS and c_0<=||E beta||_HS||beta||_HS are bounded.
All displayed products are thereby defined before their estimates are used.

For clarity, the pair estimate needed for U7 does not assume a finite rank.
For a finite skew coefficient array, group i<j. Its two-particle coefficient
norm is at most sqrt(2)||B||_HS. Exterior multiplication and its adjoint on
the n-particle sector have norms at most sqrt(binomial(n+2,2)) and
sqrt(binomial(n,2)) times that coefficient norm. This follows directly by
antisymmetrizing a tensor product: the antisymmetric projection is a
contraction and the Fock normalization supplies the binomial factor.
Approximate an arbitrary HS array in HS norm, first on each finite sector;
the same inequalities then give a limit on D(N) and

 ||Pi_B psi||<=||B||_HS ||N psi||,
 ||Pi_B* psi||<=||B||_HS ||(N+2)psi||.                 (U8)

Likewise ||dGamma(C_0)psi||<=||C_0|| ||N psi||. These are operator-norm
bounds on vectors, not merely expectation bounds. Since N<=H/m, U7/U8
imply ||Y* H Y psi||<=C||(H+I)psi|| on the graph core.

One can justify U7 without presupposing a uniform domain theorem: for each
fixed h the finite-time domain statement above permits Y*HY on that core.
The exact finite-energy covariance identity I14, its convergent normal and
HS anomalous traces, and polarization identify its matrix elements with U7.
The HS limit in U8 defines the right side on the core. Equality against
every core vector identifies the two vectors. Finally approximate any
psi in D(H) by core vectors in the H graph norm; the uniform right-side
bound makes H Y psi_k Cauchy. Closedness of H proves U6 for Y. Apply the
same reasoning using U5 to Y*. This is not an appeal to an unproved
many-body moment bound or to vacuum Gaussianity of the initial state.

Interpolation supplies the corresponding half-graph bound

 ||S Y S^-1||, ||S Y* S^-1|| <= C_G^(1/2).            (U9)

For example, apply the three-lines theorem to matrix elements of
A^z Y A^(-z) on spectral cutoff vectors for 0<=Re z<=1; unitaries A^(it)
give boundary norms1 and C_G. Let cutoffs increase using the bounds.
The same result follows from the Hilbert scale interpolation inequality.
No interpolation of the target tail conclusion is used.

## 4. Projector chains and energy tails

For every Borel B, spectral P_B=1_B(H) commutes with A and is a contraction
on each of the H and half-H graph spaces. Therefore

 ||A (Y*P_B Y) A^-1||<=C_G^2,
 ||S (Y*P_B Y) S^-1||<=C_G.                          (U10)

For L_h=Y_f P_n...P_1, both graph bounds are uniform with constants depending
on the fixed n. These estimates hold without a bin-boundary hypothesis and
without asserting convergence of the moving postmeasurement states.

Here is the abstract tail lemma actually needed. Suppose a family L has
bounded ordinary norm, ||S L S^-1||<=C_1 and ||A L A^-1||<=C_2. For any
positive finite-energy trace-class rho, define

 G_(L,R)=L* H 1_(R,infinity)(H) L.

It is a nonnegative form and 0<=G_(L,R)<=C_1^2 A. Thus S^-1 G_(L,R) S^-1
is a bounded operator, uniformly in L and R. Take Q_K=1_[0,K](H) and
rho_K=Q_K rho Q_K, without renormalization. Since Q_K commutes with S,

 d_E(rho,rho_K):=||S(rho-rho_K)S||_1 ->0.             (U11)

This follows from strong Q_K->I acting on the trace-class operator S rho S;
Q_K need not have finite rank. Weighted trace duality gives

 |Tr G_(L,R)(rho-rho_K)|<=C_1^2 d_E(rho,rho_K).

On the other hand H 1_(R,infinity)(H)<=H^2/R, so

 Tr G_(L,R)rho_K <=C_2^2 Tr(A^2 rho_K)/R.             (U12)

The right side is finite for each K, since
Tr(A^2 rho_K)<=(1+K) Tr(A rho). Choose K first and then R. Equations U11/U12
prove uniform integrability of every such family L, and in particular U3.
No second moment of rho is assumed. Replacing rho by another finite-energy
state changes every tail integral by at most C_1^2 d_E; hence a finite-net
argument makes U3 uniform over every d_E-compact family of finite-energy
density matrices. An energy cap alone does not supply that compactness.

## 5. Consequences for the already checked finite protocols

The prepared multi-time theorem supplies weak convergence of the finite
positive measure of the final energy with a preceding regular coarse-bin
history held fixed. This is a bounded spectral-test assertion; it does not
supply U3 on its own. U3 is the additional tail argument now proved.
Together they imply convergence of the unnormalized first moment for every
such history, including histories whose limiting mass is zero.

In the auxiliary limit the final energy is E_0 plus the marked compound-
Poisson increments, with the earlier coarse-bin events imposed on the same
shared E_0 and partial sums. Therefore the limiting unnormalized mean is
exactly the expectation of that final energy times the history indicator.
E_0 has the initial spectral law; its first moment is finite here. Bounded
jump sizes and uniformly bounded jump intensity give integrable added energy.
If the history has positive limiting probability, normalize the finite
measures. Their masses and first moments converge, so the conditional final
energy laws converge in Wasserstein-one. Uniform conditional conclusions
require a common positive lower bound on success probability.

Regular boundaries and fixed protocols have exactly the meaning in the
prepared theorem; U3 does not repair an atomic-boundary failure. For a fixed
profile and protocol, d_E-compact finite-energy initial families inherit
uniform unnormalized means and uniform conditional W1 wherever all histories
are regular and the success probabilities have a common positive bound.
Uniformity over moving bin families or protocols requires additional boundary
control. No rate for conditional W1 is inferred. No conditional quantum-state
trace norm convergence or infinitely frequent observation follows.

## 6. Sufficient actual common-energy transfer

Retain common H, common measured spectral projections, common Fock/vacuum
identification and the parent bounded-control calibration hypotheses

 ||V_a-V||<=d0 epsilon, ||[H,V_a-V]||<=d1 epsilon,
 ||[H,V_a]||,||[H,V]||<=k.

For each fixed h define b(T)=integral_0^T |lambda c(t)|dt<=C/h. Duhamel and
the bounded commutator identity give, with deltaW=W_a-W,

 ||deltaW||<=d0 epsilon b,
 ||[H,deltaW]||<=epsilon(d1 b+d0 k b^2).              (U13)

To check the second bound, commute H through the three factors of
-integral i W_a(T,s) lambda c(s)(V_a-V) W(s,0) ds.
The middle factor contributes d1 epsilon b. The two outside factors
contribute d0 epsilon k integral |lambda c(s)|(b(T)-b(s)+b(s))ds
=d0 epsilon k b(T)^2. Approximation by bounded energy resolvents or the
common invariant domain justifies the identity before the norm estimate.
No derivative of the scalar drive or instantaneous kick is inserted.

Free conjugation leaves these norms unchanged. Since
A deltaY A^-1=deltaY+[H,deltaY]A^-1, U13 yields

 ||A(Y_a-Y)A^-1||,
 ||A(Y_a*-Y*)A^-1|| <=C epsilon(b+b^2).              (U14)

For the adjoint, commutator norms are equal and the same identity applies.
Thus epsilon=o(h^2) supplies uniform full graph bounds for actual Y_a and
Y_a*, using the ideal U6. This is a stronger graph comparison derived here
from the stated bounded commutators, not an assertion that an unweighted
operator error can simply be multiplied by H.

Actual projector chains consequently satisfy the same U3 tail bound. If
initial rho_a converges to a fixed finite-energy rho in d_E, weighted trace
duality makes their tails differ uniformly by o(1). The previously checked
bounded-protocol probability comparison uses trace convergence and
epsilon=o(h), which are implied by these stronger assumptions. Combining
that weak comparison with the new tail control transfers unnormalized
means and positive-probability conditional W1 as above. Paired approximation
to a d_E-compact reference family gives its uniform version. The compact
preparation theorem is one sufficient source of such families and weighted
approximation; it does not construct a physical instrument or embedding.

## 7. Failure checks, premises and scope

A uniform first-energy cap on the output would not prove U3. The proof
instead derives D(H) bounds on dense energy-cutoff inputs, then uses the
uniform half-graph bound to extend tails to each finite-energy rho. The
cutoff Q_K is not presumed finite rank. Left-weighted HS bounds cannot be
transposed without U5. A moving arbitrary HS test is not used in a weak
pairing argument. No Wick identity is imposed on rho.

The gap m>0 is used in N<=H/m. Weighted q=2 one-particle estimates and fixed
smooth spatial resources are used in U2/U6; an unweighted kinetic law alone
is insufficient. Bounded commutator error is used in actual U13/U14. The
number of observations remains fixed; graph constants are not uniform as
it diverges. Rare-event normalized means are not inferred from small absolute
errors. Regular boundary exclusions of the preceding theorem remain intact.
The old Q25 statement is preserved as the earlier open obligation; it is not
rewritten to pretend that its author had already established this result.

## Unchanged independent proof (390 lines)

Required current reading: the historical J adjective at original line80 is corrected by the publication wrapper and J_PRECISION.md. All original formulas and domain arguments below are unchanged.

# Energy tails after finitely many Lüders measurements

Status: new target-root-excluded conditional analytic derivation, pending a
separate mathematical check. The accepted strict-gap chirped free CAR model
is supplied. No new physical axiom, apparatus calibration, numerical result,
formal proof or retained audit is claimed. This targets Q25 of prepared512;
the earlier comparison correctly left that obligation open.

The conclusion of the argument below is affirmative for every fixed normal
initial density of finite first free energy and a fixed finite measurement
count. The additional step is a uniform D(H) bound for both directions of
the Bogoliubov implementer, derived from the accepted q=2 weighted inputs.
It is not obtained by squaring a first-energy form inequality. The initial
state itself needs no second moment.

## 1. Sources, setting and precise assertion

Use prepared_multitime_energy_independent/DERIVATION.md512 at SHA
48f329cf8795f7f222b091c5152899809199566898b32f2aa310b338dbc9e4d8,
initial407 at SHA20c9f7cba4ea75cfad431e067f676aae54b15e031005a04dd9b4c63d37423086,
strict-gap chirp V2/515 at SHA87011c662344ed684a7251f5067bb8193d156837a50a23e71fa29ccff38e92f6,
and chirp independent850 at SHA279a96bc07b495a59b829cac70586ae8e115f0ddefca0d405bb15f0a7de6e95c.
Their chirp acceptance is9918f46bbf900e35241aae0ad51f92ba6164df21081ec6f75f97ff8576cc895c.
Exact full snapshots and the direct source manifest accompany this note.
The previously checked bounded prepared-protocol result is used at its
explicit chirped-input scope; it is not inferred from a one-time law.

Let E>=m>0 be the supplied one-particle energy, P the positive polarization,
Gamma the real conjugation, and H=dGamma(E|PK) on fermionic Fock space.
Gamma exchanges P and P_- and commutes with E. The real unitary Z commutes
with Gamma. Its implementer obeys

 Y*b(k)Y=b(Z*k), b(k)=a*(Pk)+a(P Gamma k).             (T1)

All profiles and the massive smooth-slot model are as in accepted chirp
H1--H2: bounded BV amplitude and frequency, with a fixed positive distance
between the carrier frequencies and2m. Write h=|lambda|,
Y_h(tau)=Y(tau/h^2), A_h(tau)=Y_h(tau)*HY_h(tau),
G=I+H and S=G^(1/2). Fix a finite slow-time horizon. Tail constants
are uniform over the stated drive resource bounds. All limiting-law and
conditional-moment assertions below instead keep the profiles a,varpi
and the finite observation protocol fixed, as in the supplied parents.

For any n preceding observations in the ordered slow-time list
0<=tau_1<...<tau_n<=tau<=tau_star, set

 P_(h,j)=Y_h(tau_j)*1_(B_j)(H)Y_h(tau_j),
 C_h=P_(h,n)...P_(h,1),
 T_h=Y_h(tau) C_h.                                  (T2)

For the energy-tail assertion, the B_j may be arbitrary Borel sets; its
bound does not depend on their endpoints. For the limiting probability
and conditional-mean conclusions, observations and bins are fixed and
satisfy the exact regular-bin hypotheses of prepared512: finite interval
partitions, unbounded end intervals allowed, finite boundaries satisfying
Q14--Q15 or the separately justified common zero-gap condition.

For every fixed normalized normal rho with M_rho=Tr(Hrho)<infinity,
with no quasifree, parity or energy-diagonality assumption,

 lim_(R->infinity) sup_(0<h<h0)
  || H^(1/2)1_(H>R) T_h rho^(1/2) ||_HS^2 =0.        (T3)

Here h0 is a sufficiently small resource-dependent constant. The supremum
can also cover all times in the fixed horizon and all choices of B_j with
the same bound on n. By unitary spectral calculus, the squared norm in T3
is exactly Q25. Thus T3 is stronger than its required limsup as h->0.
It supplies no uniformity over the unrestricted first-energy ball.

## 2. The one-particle second-energy inputs and inverse blocks

Write Z=[[alpha,beta],[gamma,delta]]. Accepted V2 H6 gives, for q=1,2,

 ||E^(q/2)(Z-I)||<=C_q eta_h,
 ||E^(q/2)(Z-I-K1)||_HS<=C_q eta_h,
 eta_h=sqrt(h log(2+h^-2)).                           (T4)

These are bounded extensions with the stated graph-domain meaning.
Let beta1=PK1P_-. In the accepted scalar band frame beta1 J has kernel
lambda Delta(p,q) I_h,T(E(p)+E(q)), with J an antiunitary energy isometry.
The pair density r satisfies sup_e e^2 r(e)<infinity by its checked smooth
threshold behavior and rapid decay. Since E(p)<=E(p)+E(q),

 ||E beta1||_HS^2
  <=2h^2 integral e^2 r(e)|I_h,T(e)|^2de
  <=4pi A_*^2 tau_* ||e^2 r(e)||_infinity.            (T5)

The last inequality is temporal Plancherel, using
integral|I_h,T|^2=2pi integral_0^T|c_h(t)|^2dt and h^2T<=tau_*.
No second-moment secular limit is needed. The q=2 remainder in T4 yields

 ||E beta||_HS<=B_2,  ||E^(1/2)beta||_HS<=B_1,        (T6)

uniformly for small h and the fixed resources. The mass gap also bounds
||beta||_HS by B_2/m. This is an actual second-energy Hilbert-Schmidt
bound; a first-energy estimate alone would not establish it.

Unitarity gives the exact bounded-extension identity

 E^(q/2)(Z*-I)=-E^(q/2)(Z-I)Z*.                      (T7)

Indeed Z*-I=-(Z-I)Z*, so its range is in the same graph domain before
applying the closed energy multiplier. Thus T4's weighted operator bound
also holds for Z*. In particular alpha* preserves D(E).

For h0 small, delta is invertible with ||delta^-1||<=2. The off-diagonal
unitarity equation and the real structure give

 gamma*=-alpha* beta delta^-1,
 gamma*=Gamma beta* Gamma.                           (T8)

Consequently, using E alpha* beta=E beta+E(alpha*-I)beta,

 ||E gamma*||_HS
 <=2[||E beta||_HS+||E(alpha*-I)|| ||beta||_HS] <=B'_2. (T9)

This multiplication is legitimate: beta maps into D(E), and alpha*
preserves that domain. T9 controls the weighted off-diagonal block of
the inverse implementer Y*. It also bounds ||E beta*||_HS by real
conjugation, hence ||beta E||_HS by adjunction. No skew-symmetry of the
bare beta is assumed; its exact alpha/delta factors are retained.

Finally put Q=E^(1/2). Spectral calculus on the Hilbert-Schmidt class gives

 ||Q beta* Q||_HS^2
 <=(1/2)(||E beta*||_HS^2+||beta* E||_HS^2)<=B_x^2.   (T10)

One can verify this with bounded spectral cutoffs and the scalar inequality
xy<=(x^2+y^2)/2 for the commuting left/right energy variables, then pass
monotonically. The same statements hold for the inverse blocks: its beta
is gamma*, already controlled by T9, while its weighted full operator
bound follows from T7. All constants below may take the maximum for Y
and Y*. Only the q=1,2 instances and the supplied mass gap are needed.

## 3. A Fock energy graph lemma with all CAR terms

This section proves uniform constants c1,c2 such that, for U=Y or Y*,

 ||S U psi||<=c1||S psi||, psi in D(H^(1/2)),
 ||G U psi||<=c2||G psi||, psi in D(H).                (T11)

The domain conclusions are part of these estimates. They are not
assumed in order to take an unbounded energy trace.

For the forward direction, T1 gives for xi in the positive one-particle
space

 Y*a(xi)Y=a(alpha*xi)+a*(Gamma beta*xi).              (T12)

The star and the side of beta in this formula are important. For Y*
apply the same proof with the inverse block map.

Let E_L=min(E,L), and let (e_i) be any orthonormal basis. The CAR imply
the positive-form identities

 <z,dGamma(E_L)z>=sum_i ||a(E_L^(1/2)e_i)z||^2,

 ||dGamma(E_L)z||^2
  =sum_i ||a(E_L e_i)z||^2
    +sum_(i,j)||a(E_L^(1/2)e_j)a(E_L^(1/2)e_i)z||^2. (T13)

The second term is the ordered distinct-particle contribution; on each
particle sector the identity is
(sum E_i)^2=sum E_i^2+sum_(i!=j)E_i E_j.
Positive sums, finite particle truncations and then monotone limits make
T13 an extended positive-form identity for every Fock vector. No
finite-rank projection commuting with the continuous-spectrum E is used.

Set k_q=||E^(q/2)(alpha-I)|| and
a_q=(1+k_q/m^(q/2))^2, q=1,2. On the relevant graph domains,

 alpha* E^q alpha<=a_q E^q.                          (T14)

This follows by the triangle inequality for E^(q/2)alpha, not by
squaring the q=1 operator inequality. For u_i=E_L^(1/2)e_i write
f_i=alpha*u_i and g_i=Gamma beta*u_i. Then

 sum_i |f_i><f_i|=alpha*E_L alpha<=a_1 E,
 sum_i||g_i||^2<=B_1^2,
 sum_i||E^(1/2)g_i||^2<=B_x^2.                       (T15)

The last estimate uses T10 and Gamma E=E Gamma. The maps involving
Gamma may be antilinear; their squared column norms have the same
Hilbert-Schmidt interpretation. The bounded extension in T10 ensures
that the g_i appearing here have the needed form domain.

Applying T12 to the first identity in T13 and bounding the two column
vectors by the sum-of-squares inequality gives

 <Ypsi,H Ypsi><=2a_1<psi,Hpsi>+2B_1^2||psi||^2.      (T16)

First do this with E_L, then let L increase. This proves the first
domain assertion in T11 by monotone convergence.

For the first sum in the second identity T13, T14 with q=2 and T6 give

 sum_i||Y*a(E_L e_i)Y psi||^2
          <=2a_2||Hpsi||^2+2B_2^2||psi||^2.           (T17)

For the double sum expand
(a(f_j)+a*(g_j))(a(f_i)+a*(g_i)) into its four terms. Their squared
column norms obey the following bounds for psi in D(H):

 AA <=a_1^2||Hpsi||^2,
 CA <=a_1 B_1^2 <psi,Hpsi>,
 AC <=2a_1 B_x^2||psi||^2+2a_1 B_1^2<psi,Hpsi>,
 CC <=B_1^4||psi||^2.                                (T18)

For AA, the ordered two-particle operator is bounded by a_1^2 times
sum_(r!=s)E_r E_s, using T15 on each distinct tensor factor. It is
therefore bounded by a_1^2 H^2. This argument does not incorrectly
square noncommuting one-particle form inequalities.
For CA and CC use ||a*(g)||<=||g|| and sum the column norms.
For AC use the CAR
a(f_j)a*(g_i)=<f_j,g_i>-a*(g_i)a(f_j). Parseval and T14 give

 sum_(i,j)|<f_j,g_i>|^2
   =sum_i ||E_L^(1/2)alpha g_i||^2
   <=a_1 sum_i||E^(1/2)g_i||^2<=a_1 B_x^2.

These estimates include the scalar contraction term; dropping it would
leave the graph proof incomplete. Every bound is uniform in L and in
the number of basis columns retained.

Using ||v1+v2+v3+v4||^2<=4sum||v_i||^2 in T18, and then T17,

 ||H Ypsi||^2
 <=(2a_2+4a_1^2)||Hpsi||^2
    +12a_1 B_1^2<psi,Hpsi>
    +(2B_2^2+8a_1 B_x^2+4B_1^4)||psi||^2.           (T19)

To justify the left side, bound T13 on Ypsi first, where it is permitted
to be infinite. The transformed finite products in T12 are bounded CAR
operators, so the estimates apply without a prior domain assumption on
Ypsi. Pass through the positive basis sums and E_L cutoffs. Sectorwise
dGamma(E_L)^2 increases to H^2. Monotone convergence proves finiteness
and Ypsi in D(H), as well as T19. Since
<psi,Hpsi><=||psi||||Hpsi||, T19 and unitarity imply the second estimate
in T11. T7--T10 give the identical proof for Y*. All c1,c2 are uniform
on the accepted kinetic window and fixed drive resources.

## 4. Projection chains and the fixed-state tail estimate

Every spectral projection Pi=1_B(H) is a contraction in both the S and
G graph norms because it commutes with H. T11 therefore gives, for
each Heisenberg projection P_h=Y_h*Pi Y_h,

 ||S P_h S^-1||<=c1^2,  ||G P_h G^-1||<=c2^2.         (T20)

For n preceding projections in T2,

 ||S T_h S^-1||<=L1=c1^(2n+1),
 ||G T_h G^-1||<=L2=c2^(2n+1).                       (T21)

The bounds concern the graph-space extensions of these expressions.
They are independent of the bins and require a fixed finite n.

Let F_L=1_[0,L](H). For fixed finite-energy rho,
S rho^(1/2) is Hilbert-Schmidt and

 t_rho(L):=||S(I-F_L)rho^(1/2)||_HS^2
          =Tr[rho(I+H)1_(H>L)] ->0.                 (T22)

Apply T21 first to the high-energy part of the initial square-root density.
For its complementary part, H1_(H>R)<=R^-1 H^2 gives

 ||H^(1/2)1_(H>R) T_h rho^(1/2)||_HS^2
 <=2L1^2 t_rho(L)
       +(2L2^2/R)||G F_L rho^(1/2)||_HS^2
 <=2L1^2 t_rho(L)
       +(2L2^2/R)(1+L)(1+M_rho).                   (T23)

These are inequalities between Hilbert-Schmidt norms of graph-bounded
maps; no unbounded trace is cycled. They can also be checked column by
column and then summed positively. Taking L=sqrt(R) for R>=1 proves T3.
The proof uses the initial first-energy tail, not an initial second moment.

By functional calculus,

 ||A_h(tau)^(1/2)1_(A_h(tau)>R) C_h rho^(1/2)||_HS
       =||H^(1/2)1_(H>R) T_h rho^(1/2)||_HS.          (T24)

Thus Q25 follows with its correct Heisenberg ordering. In particular all
the unnormalized history states have finite final first energy. A bounded
first moment by itself would not imply this uniform-integrability result;
the uniform D(H) bound was used only on the truncated initial part.

## 5. Limiting postselected means and final-energy laws

Let E_tau=X0+S_tau be the already checked classical comparison variables:
X0 has initial law mu_rho, and S has the marked compound-Poisson increment
law of the accepted strict-gap chirp measure M, independent of X0. The
same X0 is used at every observation. Let F be a fixed preceding regular
coarse-bin history and define the positive subprobability measure

 nu_h^F(B)=Tr[C_h rho C_h* 1_B(A_h(tau))].            (T25)

The prepared512 bounded-test/projection passage gives

 nu_h^F => nu^F,  nu^F(B)=E[1_F 1_(E_tau in B)].     (T26)

T3 gives uniform integrability of its energy. Hence bounded truncation
followed by R->infinity proves

 integral x nu_h^F(dx) -> E[E_tau 1_F].              (T27)

The target is finite because E[E_tau]=M_rho+integral e dM_(u<=tau).
This does not apply the fixed-initial-state mean theorem to a moving
collapsed state. It uses the new tail estimate on that state.

A regular final bin, including an unbounded one, may also be imposed.
The bounded-protocol theorem gives its restricted weak limit and success
probability; its energy tails are bounded by those in T3. Therefore, for
any such fixed full history F with limiting success probability p_F>0,

 conditional final mean -> E[E_tau 1_F]/p_F,
 conditional final-energy law -> Law(E_tau | F) in W1. (T28)

This is the physical final free-energy mean of the postmeasurement state:
the final spectral projection commutes with A_h(tau), and the full final
propagator transports the Heisenberg history to the actual Lüders chain.
Its extra free rotation commutes with H, so using Y or the full propagator
gives the same energy. Division is justified only after success
probabilities converge to a positive value. Weak convergence and the
separately proved finite means give the stated one-dimensional W1 limit.

Finite unions of recorded histories are covered by summing their positive
subprobability measures. The number of recorded histories is fixed and
finite, so the tail bound survives that sum. In particular, summing a
complete finite partition gives the nonselective final mean limit
M_rho+integral e dM_(u<=tau). No limiting conditional quantum-state trace
norm or instrument-independent continuous-energy path law is asserted.
Vanishing-success-probability histories remain outside T28.

## 6. Optional compact-family uniformity and exact boundaries

If C_E is compact in weighted trace norm within normalized finite-energy
densities, its initial tails T22 vanish uniformly. Indeed the positive
operators Q_rho=S rho S form a trace-norm compact family, and the bounded
spectral projections 1_(H>L) converge strongly to zero. Their traces tend
uniformly to zero on that compact family by finite-rank approximation and
a finite trace-norm net. Also sup_(rho in C_E)(1+M_rho)<infinity.
Thus T23 proves Q25 uniformly over C_E.

For fixed regular bins satisfying prepared512's condition for every member,
its bounded history convergence is uniform over C_E. Truncating the energy
and using the uniform tails proves uniform unnormalized mean convergence.
If the relevant limiting success probabilities are bounded below by a
positive common number, division gives uniform conditional means.
Uniform conditional W1 follows by the same compact-subsequence argument:
along rho_h->rho_* in weighted trace, target bounded tests converge by
trace duality and target means converge because their positive energy
kernel is bounded above by H+constant. The exact laws have the same weak
limit and mean, so W1 follows. No boundary-density rate is required.

The mass gap, fixed higher weighted drive resources and bounded observation
count enter the constants. The initial-tail modulus enters T23. This is
not a bound uniform over an unrestricted first-energy ball, and it does
not contradict the previously preserved moving-state counterexamples.
The proof gives no growing-observation, shrinking-bin, feedback, massless,
threshold-crossing or arbitrary actual-Hamiltonian result. Actual-cell
transfer of these new tails would need corresponding uniform forward and
inverse graph bounds and the exact common energy instrument; it is not
claimed from a norm-close propagator or a first-commutator estimate alone.

## 7. Failed shortcuts, independent checks and exposure

The direct first-energy-form route was insufficient: a uniform bound on
the means of moving history states does not prove their uniform tails.
Likewise, squaring a form inequality would be invalid for noncommuting
one-particle energies. The proof instead uses the q=2 input and the exact
single- and double-annihilation decomposition T13. Assuming beta itself
skew would also give an unjustified inverse-weight shortcut; T8 retains
the actual block factors.

Separate analytic evidence checks the particle-count factors, the scalar
CAR contraction in AC, a high-energy pair family that separates first
weighted bounds from the required second-energy graph input, and the
cutoff tail estimate. No proposed-science numerical command is run.

Earlier complete prepared512/root340 and their source-exposed comparison,
initial407, compact-preparation and vacuum multi-time work are conceptual
exposures. The accepted chirp weighted statements were already exposed and
are used as premises. This new target's root plans/proofs/findings,
POSTMEASUREMENT_ENERGY_UI_ROOT files and future root folder, all threshold
sources, root checkpoints and opportunity notes were not opened. The
neutral plan records the pre-plan dense-core idea. No model diversity or
absence of prior relevant ideas is claimed. Selected model and effort are
unchanged; no extra agent, other chat, Git/CW mutation, prompt edit, audit
action, scientific runtime or Lean certificate supports this derivation.

## Unchanged scoped countercontrol (84 lines)

# A high-energy tail control for the graph-bound argument

Provisional root analytic control, separate from the frozen306-line target.
This controls an invalid inference; it is not a counterexample to the fixed
smooth-slot drive theorem, a proof of necessity of all its assumptions, or
an independently checked/retained result. No numerical execution is used.

Use the same massive continuum one-particle E and Fock energy H=dGamma(E).
For integers R>2m, the spectral shell [R/2,R/2+1] has infinite rank. Choose
2N_R orthonormal vectors xi_j,eta_j in that shell, N_R=R^2. The vectors may
be chosen smooth with compact momentum support inside the shell, hence in
all domains of E. No assertion that they are exact energy eigenvectors is
needed. Put p_R=R^(-3), theta_R=arcsin(sqrt(p_R)), and

 Y_R=product_(j=1)^N_R exp(theta_R(a*(xi_j)a*(eta_j)-a(eta_j)a(xi_j))).

Each exponent is bounded and skew-adjoint. Distinct even pair generators
commute. Acting on vacuum, up to an irrelevant common phase,

 Y_R Omega=product_j (sqrt(1-p_R)+sqrt(p_R)a*(xi_j)a*(eta_j))Omega.

Its particle-number pair count is Binomial(N_R,p_R). The empty-sector mass
is (1-p_R)^N_R and its complement is at most N_R p_R=1/R. Thus the state
converges to vacuum in trace norm, with distance at most2/sqrt(R), and the
free-energy law converges weakly to delta_0. Every nonempty particle-number
sector has spectral free energy at least R, because each occupied particle
belongs to the shell. These spectral statements remain true for arbitrary
orthonormal shell vectors and do not assume shell invariance of their span.

The one-body occupation covariance is p_R Q_R, where Q_R is projection onto
these2N_R vectors. Thus its exact energy mean is

 M_R=p_R sum_j (<xi_j,E xi_j>+<eta_j,E eta_j>),
                         1<=M_R<=1+2/R.

For every fixed cutoff L and R>L, the entire mean lies above L:

 <Y_R Omega,H 1_(H>L)Y_R Omega>=M_R>=1.

Consequently weak convergence plus bounded means does not give energy
uniform integrability. Mean convergence to the mean of the weak limit
would be needed; it fails here by the displayed exact calculation.

In the standard Nambu block notation the pair block beta_R has singular
value sqrt(p_R) on these2N_R modes. Its weighted Hilbert--Schmidt norms obey

 ||E^(1/2)beta_R||_HS^2=M_R in[1,1+2/R],
 ||E beta_R||_HS^2>=2N_R p_R(R/2)^2=R/2.

The Nambu change Z_R-I is supported in the signed shell and its operator
norm is at most2sin(theta_R)=2R^(-3/2). Therefore

 ||E(Z_R-I)||<=(R/2+1)2R^(-3/2)=O(R^(-1/2)).

Here E on Nambu space is the positive signed-band energy weight. Its range
is shell-supported; invariance of the finite-dimensional Q_R under E is
unnecessary for this norm bound. The same statements hold for the inverse.
In particular small weighted one-particle operator change and bounded
vacuum first mean can coexist with the displayed nonintegrable tail.

The fixed-state relative first-energy form estimate from initial407(I16)
and(I19)--(I20) applies to these transformations: the required quantities
||E^(1/2)(u_R-I)|| and ||E^(1/2)beta_R|| are uniformly bounded, and the
weighted pair HS norm ||E^(1/2)beta_R||_HS is uniformly bounded. Hence

 Y_R*H Y_R<=C(H+I), and Y_R H Y_R*<=C(H+I),

with C independent of R. This form inequality alone therefore also does
not ensure first-energy uniform integrability even on the fixed vacuum.
By contrast, ||(H+I)Y_R Omega||^2>=<Y_R Omega,H^2Y_R Omega>
>=R M_R>=R. The full H-graph bound used by root306 fails, consistently
with the divergence of ||E beta_R||_HS above.

The family changes its rank, slots and energies with R and is outside the
fixed spatial/control-resource hypotheses of the proposed kinetic result.
The purpose is to isolate why the q=2 weighted pair HS/domain step must be
proved and cannot be replaced by a first-moment or one-particle norm bound.
There is no claim that the full H-graph criterion is the only possible UI
criterion or that arbitrary different controls cannot have a kinetic limit.

Source reused: FINITE_INITIAL_ENERGY_KINETIC_ROOT_PROBE.md407,
SHA20c9f7cba4ea75cfad431e067f676aae54b15e031005a04dd9b4c63d37423086,
I16/I19--20 freshly reread. All new algebra above is a root derivation and
awaits a focused check; no frozen target proof is edited by this addendum.
