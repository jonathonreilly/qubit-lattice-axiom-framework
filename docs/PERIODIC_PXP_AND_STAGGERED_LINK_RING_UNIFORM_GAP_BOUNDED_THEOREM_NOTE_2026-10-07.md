---
claim_id: periodic_pxp_and_staggered_link_ring_uniform_gap_bounded_theorem_note_2026-10-07
claim_type: bounded_theorem
claim_scope: "For H=-sum PXP on independent sets of each even periodic cycle L>=6, and for the explicitly supplied staggered height-one spin-half link ring on its entire Gauss sector with plaquette coefficient one, the ground state is unique and its spectral gap exceeds log(25/14)/4. The proof constructs a common real spatial spectrum, proves the two-purity bootstrap, certifies its finite seeds by exact integer/rational arithmetic, and proves the all-length sector dictionary."
upstream_dependencies: []
runner: scripts/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py
---

# A uniform gap for the periodic PXP chain and staggered link ring

**Date:** 2026-10-07
**Claim type:** bounded_theorem
**Status:** conditional-support for the explicitly supplied model.

For every even L>=6, the two Hamiltonian families specified below have a unique ground state and a spectral gap strictly greater than `log(25/14)/4`, approximately `0.1449546238`, in plaquette units.

The original repo target is the finite-size gap discussion in
`THE_SPIN_HALF_LINK_RING_IS_GAPPED_AND_CONFINING_THE_PHOTON_QUESTION_NEEDS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md`, at frozen main `ed04ee2736b5bddb4e9064966505e3c3dfe003de`. Its supplied model is reproduced completely here. The finite gap fit in that note is replaced, at the present even-length scope, by the proof below. This note's scope is the prescribed one-dimensional families. It makes no claim about their selection by the framework or a three-dimensional phase.

The earlier note states: “They do not prove an infinite-size gap, exponential law, correlation length, or confinement phase.” The result here supplies a positive lower bound uniform over all even finite rings of length at least six. It does not prove thermodynamic-limit ground-state uniqueness, an exponential correlation law or confinement. Thus it closes the uniform finite-volume gap obligation while only partially addressing that broader earlier discussion.

The mathematical method is adapted from OpenAI's [two-purity bootstrap](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/bootstrap.tex), released October6,2026. The necessary criterion is proved here in full. The spin-one gap theorem, its transfer representation and its initialization are not dependencies of this proof.

## Premises, imports and obligation graph

| Input or obligation | Role and disposition |
|---|---|
| Binary independent-set Hilbert space, PXP generator and unit coupling | Supplied model, defined below. |
| Height-one ladder, staggered charges, spin-half link operators and plaquette generator | Supplied model for the link-ring statement, defined below. |
| Separability of L2 on a countable standard-Borel union, Tonelli, compact self-adjoint spectral theorem, Hilbert–Schmidt norm identity | Standard mathematical tools with their needed hypotheses checked below. |
| Common real spatial trace representation | Proved by periodic paths, legal-word shuffles and the even-cycle kernel norm. |
| Purity contraction and interpolation to every even length | Proved below. |
| Finite trace inequalities | Exact executable certificate with explicit positive tail bound. |
| All-length link-sector identification | Proved by elimination of the Gauss constraints and local plaquette action. |

The proof graph has no open terminal mathematical lemma at author level. Independent checking and formal audit are separate from that statement. The dimensionless result uses no numerical observational input or fitted selector. A separately supplied positive coupling rescales its gap. The zero coupling, odd periodic lengths and other backgrounds are outside the claimed model family.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: the_spin_half_link_ring_is_gapped_and_confining_the_photon_question_needs_three_dimensions_bounded_theorem_note_2026-09-03
target_blocker_text: "They do not prove an infinite-size gap, exponential law, correlation length, or confinement phase."
source_of_blocker_text: null
blocker_source_path: "docs/THE_SPIN_HALF_LINK_RING_IS_GAPPED_AND_CONFINING_THE_PHOTON_QUESTION_NEEDS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md"
blocker_source_section: "Corollary -- finite scope and open physical questions, item 1"
blocker_source_revision: "ed04ee2736b5bddb4e9064966505e3c3dfe003de"
reachability_to_target: partially_closes
artifact_role: theorem
conditional_surface_status: "Unique ground state and uniform positive gap for the supplied even-ring families"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit model theorem; model selection is supplied."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Preserve the reviewed scope during integration; formal audit remains separate."
```

## Model and exact target
For L>=4 let C_L={z in {0,1}^L : z_i z_(i+1)=0 for every i mod L}.
The Hilbert space has orthonormal basis {|z>:z in C_L}. Let A_L have matrix
entry 1 between configurations differing at exactly one site, and zero
otherwise. Thus H_L=-A_L=-sum_i P_(i-1) X_i P_(i+1), restricted to C_L.
All matrix entries are real; adjacency is symmetric and has degree <=L.
Every configuration connects to the empty configuration by deleting its
occupied sites, so the configuration graph is connected. A_L is nonscalar.
We write Z_L(b)=Tr exp(b A_L), for b>0, with zero energy shift.

Allowed inputs: this explicit supplied model; ordinary tensor composition and
finite matrix analysis; basic measure theory, compact self-adjoint spectral
theorem, and exact integer/rational computation. The four framework axioms and
approved primitives supply no extra dynamics or state-selection premise here.
Their unchanged pinned registry/memo were read in the preceding applicability
review. No registered primitive is needed to prove this dimensionless model
theorem. Multiplication by a separately supplied positive coupling rescales the
gap in the usual way; this report fixes the coefficient to one.

Forbidden weakenings: a gap fit or positive finite-size gap is not a uniform
gap; a numerical transfer spectrum is not the all-length trace identity;
a conditional PXP theorem without an all-length dictionary does not establish
the original link-ring theorem. Required edge cases: periodic wrap, every even
L>=6 rather than a dyadic subsequence, zero-flip paths, constrained Hilbert
space, and the two frozen sectors.

## A common real spatial spectrum
Fix b>0. The one-site path space Omega_b is the disjoint union over
a in {0,1} and k in {0,2,4,...} of
  {a} x {0<t_1<...<t_k<b}.
For k=0 the simplex is one atom. A point encodes the right-continuous binary
path w(t)=a + #{j:t_j<=t} modulo 2. Its initial and final values agree.
Put counting measure on a and ordinary Lebesgue measure on each simplex;
the zero-dimensional simplex has mass one. Call the resulting measure mu_b.
It is finite, with mu_b(Omega_b)=2 sum_(k even) b^k/k! = 2 cosh b.
The space is a countable disjoint union of standard Borel spaces, so its L2
space is separable. No probability normalization or Poisson survival factor
is inserted: this is an exponential-series measure, not a Markov jump law.

Define C_b(w,v)=1 if w(t)v(t)=0 for Lebesgue-almost every t in [0,b], and
0 otherwise. This is a measurable, real, symmetric kernel bounded by one:
on fixed finite path strata the condition is a finite set of inequalities
among the jump times. Let K_b be its integral operator on L2(Omega_b,mu_b).
It is Hilbert–Schmidt since integral |C_b|^2 <=(2 cosh b)^2. It is therefore
bounded and compact; symmetry makes it self-adjoint. Its nonzero spectrum
is a finite or countable list of real eigenvalues lambda_j(b), including
multiplicity, with sum_j |lambda_j|^2 finite, hence sum_j |lambda_j|^4 finite.
The kernel need not be positive semidefinite; real eigenvalues are sufficient.

Lemma 2.1 (worldline identity). For each finite L>=4,
  Z_L(b)=integral_(Omega_b^L) product_i C_b(w_i,w_(i+1)) product_i dmu_b(w_i).

Proof. Partition the product path space by each site's initial bit and even
number of flips. Apart from a null set, all flip times at distinct sites are
different. Sorting the total m times gives a unique site word (i_1,...,i_m)
and the global ordered simplex 0<s_1<...<s_m<b. Conversely such a word with
each site's occurrence count even recovers the local ordered simplices.
This is the ordinary disjoint shuffle decomposition, with Jacobian one.

The compatibility product is one exactly when all successive configurations
are legal independent sets. On an open interval between two distinct flip
times it tests every adjacent pair; initial and final intervals also have
positive length. At a flip at i, legality before and after is equivalent to
both neighbors being zero. Hence each legal step has exactly the PXP matrix
element one. Sitewise even counts give precisely the trace's return to the
initial configuration. At zero flips the integral simply counts C_L. Events
at t=0,b or simultaneous events form a null set and add no terms. Each legal
closed word of length m has simplex volume b^m/m!, so the integral equals
sum_m b^m Tr(A_L^m)/m!=Tr exp(bA_L). All summands are nonnegative. Tonelli
therefore justifies every interchange; absolute convergence also follows
from Tr(A_L^m)<=|C_L| L^m. This pays explicitly for the noncommuting PXP
projectors: only globally ordered legal paths contribute. QED.

Lemma 2.2 (even spatial moments). For every even L>=4,
  Z_L(b)=Tr K_b^L=sum_j |lambda_j(b)|^L.

Proof. Let L=2m. Iterated integration gives the kernel C_b^(m)(w,v) of K_b^m;
it is bounded by mu_b(Omega_b)^(m-1), hence square-integrable. The symmetry
of C_b gives symmetry of this iterated kernel. The spectral theorem and the
Hilbert–Schmidt norm give
  Tr K_b^(2m)=||K_b^m||_HS^2
            =integral C_b^(m)(w,v)^2 dmu_b(w)dmu_b(v).
Expand the two copies into their m-step kernel chains. Reversing one chain
uses symmetry and gives exactly the 2m-cycle integral of Lemma 2.1. Tonelli
applies because the kernels are nonnegative and the measure finite. This
avoids any unproved claim that the diagonal of an arbitrary measurable
trace-class kernel equals its trace. Finally the real compact spectrum gives
Tr K_b^(2m)=sum_j lambda_j^(2m)=sum_j |lambda_j|^(2m). The same K_b and
spectrum work for every L; they depend only on b. QED.

This is the previously missing transfer premise. It uses no limit in L,
no positive-definiteness assumption and no guessed self-adjoint similarity.

## Two-purity bootstrap
This section re-proves the external bootstrap at the needed generality.
Suppose a nonscalar finite Hermitian family H_L, even L>=4, has
Z_L(b)=Tr e^(-b H_L)=sum_j |lambda_j(b)|^L with sum_j |lambda_j(b)|^4 finite.
Both descriptions count multiplicities. Define
  S(n,b)=Z_(2n)(b)/Z_n(b)^2,
  T(n,b)=Z_n(2b)/Z_n(b)^2.
For even n>=4 they are purities of probability distributions: normalized
spatial weights |lambda_j|^n and normalized physical Boltzmann weights.
They consequently lie in (0,1].

4a. Squaring. If nonnegative weights w_j sum to one and P=sum w_j^2, then
their normalized squares have purity P'=sum w_j^4/P^2. Exactly,
  1-P'=2 sum_(i<j) w_i^2 w_j^2 / P^2
       <=2 (sum_(i<j) w_i w_j)^2/P^2
       =(1-P)^2/(2P^2)=f(1-P),
where f(u)=u^2/[2(1-u)^2]. Nonnegative summands justify countable sums.
f is increasing on [0,1). Thus
  1-S(2n,b)<=f(1-S(n,b)),
  1-T(n,2b)<=f(1-T(n,b)).

4b. Coupling the updates. Direct cancellation, using the same Z throughout,
gives
  S(n,2b)=S(n,b)^2 T(2n,b)/T(n,b)^2,
  T(4n,b)=T(2n,b)^2 S(2n,2b)/S(2n,b)^2.
Their denominators are <=1. If S(n,b),T(2n,b)>=1-u and a number C satisfies
G(u)<=C, where
  G(u)=1/2 [(1-u)^(-1)+(1-u)^(-2)+(1-u)^(-3)]^2,
then S(n,2b)>=(1-u)^3. Spatial squaring gives
  1-S(2n,2b)<=f(1-(1-u)^3)=G(u)u^2<=C u^2.
If C u<=1, set u_+=C u^2<=u. The second cancellation then gives
T(4n,b)>=(1-u)^2(1-u_+) >=(1-u)^3. Physical squaring gives
  1-T(4n,2b)<=G(u)u^2<=u_+.
The identity for G follows by factoring 1-(1-u)^3. G is increasing because
each positive summand in its displayed expression is increasing.

4c. Dyadic induction. Suppose at even n0 and b0>0 both purities in 4b are
>=1-u0, where
  0<u0<1/6, G(u0)<=C, r=C u0<1, C(1-3u0)>3.
Let n_j=2^j n0, b_j=2^j b0, u_j=C^(-1) r^(2^j). Then
u_(j+1)=C u_j^2<u_j<=u0. Repeated 4b gives
  S(n_j,b_j),T(2n_j,b_j)>=1-u_j.

4d. Every intermediate even length. For nonnegative a_i and q>=p>0,
  sum a_i^q <= (sum a_i^p)^(q/p).
Proof: divide by the pth-power sum and use w_i^(q/p)<=w_i for probability
weights w_i; the zero-sum case is immediate. Therefore for even n<=L<=2n,
  Z_L(b)<=Z_n(b)^(L/n),
  Z_L(2b)>=Z_(2n)(2b)^(L/(2n)).
Combine to obtain
  T(L,b)>=[T(2n,b) S(n,b)^2]^(L/(2n)).
The bracket lies in (0,1] and its exponent is <=1. At (n_j,b_j) this implies
  T(L,b_j)>=(1-u_j)^3>=1-3u_j>1/2.

4e. Spectrum. The largest physical Gibbs weight w0 is at least its purity
T(L,b_j)>1/2. Two ground vectors would have equal maximal weights, impossible;
the ground state is unique. If w1 is the weight of any eigenvector at the
next distinct energy and gamma_L that energy gap, then
  exp(-b_j gamma_L)=w1/w0
    <=(1-w0)/w0 <=3u_j/(1-3u_j)
    <=[3/(C(1-3u0))] r^(2^j) < r^(2^j).
Consequently gamma_L>log(1/r)/b0. The intervals [n_j,2n_j] cover every even
L>=n0; no unexamined length subsequence remains. This completes the criterion.

The original spin-one initialization, boundary-field paper and other external
theorems are not required by this specialization. A separate reviewer checked
the complete analytic argument and independently reproduced the exact seeds;
the review record below states the scope of that check.

## Exact finite seed certificate
Use n0=6, b0=4, u0=2/25 and C=7. We need
  Z_12(4)/Z_6(4)^2 >=23/25,
  Z_12(8)/Z_12(4)^2 >=23/25.

`scripts/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py` constructs the exact independent-set graph at L=6 (18
vertices) and L=12 (322 vertices). It computes t_k=Tr A_L^k for k=0,...,256
as integer closed-walk counts. Rotation is explicitly checked as a graph
automorphism. Diagonal entries for one representative of each cyclic orbit
are multiplied by that orbit's size (5 orbits at L=6; 31 at L=12). Each
vector update is exactly v'_i=sum_(j adjacent i) v_j. This gives the complete
trace; no eigenvalues or stochastic estimate are used. Odd traces vanish by
the checked occupation-parity bipartition. Separate uncompressed explicit
walk enumeration checks t_2,t_4,t_6 via sum_ij (A^(k/2)_ij)^2.

For integer b=4 or 8 and N=256, define the rational lower sum
  Q_N=sum_(k=0)^N b^k t_k/k!.
All terms are nonnegative. Since each graph vertex has degree at most L,
  0<=Z_L(b)-Q_N <=D sum_(k=N+1)^infinity (bL)^k/k!
    <=D (bL)^(N+1)/(N+1)! / (1-bL/(N+2)) =R_N.
The last ratio bound is valid because bL/(N+2)<1 and bounds every ratio in
the remaining tail. This argument is combinatorial and needs no eigenvalue
rounding bound. Both endpoints Q_N,Q_N+R_N are exact Fractions. The lower
purity uses the lower numerator and upper denominator squared; all final
comparisons with 23/25 are exact rational comparisons.

Certificate results (decimals for legibility; full rational endpoints stored):
  S(6,4) > 0.9246630910706219618218284673832385,
  T(12,4)> 0.9365536948228503531525298145562988.
The displayed inequalities use decimals truncated downward from exact lower
bounds. The widest relative tail bound is 4.422e-23, for Z_12(8); the other
relative tails are below 5.45e-88 and 2.26e-160. These tail magnitudes are
diagnostics; the exact rational inequalities in the JSON are load-bearing.

Scalar conditions hold exactly:
  G(2/25)=1868400625/296071778 <7,
  r=7(2/25)=14/25<1,
  7(1-6/25)=133/25>3,
  0<2/25<1/6.
Thus the spatial-spectrum and bootstrap proofs plus this certificate give
  gamma_L > (1/4) log(25/14), every even L>=6.
This is a mathematical proof with a finite exact-arithmetic certificate and
selective independent checking. Formal audit status remains separate.

The primary runner prints complete integer moments, rational endpoints, graph hashes and checks into its paired cache.
Run: `python3 scripts/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py`.
It uses standard-library arithmetic; timing is not part of the theorem.

## All-length link-ring dictionary
Fix an even L>=4. The ladder has vertices v_i^T and v_i^B, with all indices
taken modulo L. Top rails T_i run from v_i^T to v_(i+1)^T, bottom rails B_i
from v_i^B to v_(i+1)^B, and upward rungs R_i from v_i^B to v_i^T. Each
oriented edge e carries a qubit with E_e=Z_e/2 and U_e=(X_e+iY_e)/2.
The full link Hilbert space is the tensor product of these 3L qubits. Its
Gauss sector is the simultaneous kernel of G_v=(div E)_v-rho_v, where
divergence is outgoing minus incoming electric field. With
W_i=U_Ti U^dag_R(i+1) U^dag_Bi U_Ri, the supplied Hamiltonian is
H_link=-sum_i(W_i+W_i^dag), restricted to this sector; its coefficient is one.
The background charges are 2rho(v_i^T)=(-1)^i and 2rho(v_i^B)=-(-1)^i.
These definitions fully specify the supplied model. Let
t_i,b_i,r_i in {-1,+1} denote twice their electric fields. Put s_i=(-1)^i.
The Gauss constraints are
  t_i-t_(i-1)-r_i=s_i,
  b_i-b_(i-1)+r_i=-s_i.
Adding gives t_i+b_i=F independent of i, F in {-2,0,2}.

For F=+/-2 all top and bottom signs equal F/2; the rungs are r_i=-s_i.
Each sector therefore has one basis vector. The oriented plaquette
W_i=U_Ti U^dag_R(i+1) U^dag_Bi U_Ri, U=(X+iY)/2, cannot act there:
top and bottom signs agree but its rail raising/lowering requirements oppose.
W_i^dag also vanishes. Each frozen vector has energy exactly zero.

For F=0, b_i=-t_i. Define z_i=(1-s_i t_i)/2. Because L is even, s_(i-1)=-s_i
also across the periodic seam. Then the first Gauss equation becomes
  r_i=s_i[1-2(z_(i-1)+z_i)].
Its requirement r_i=+/-1 is equivalent to forbidding z_(i-1)=z_i=1.
Conversely any independent-set z gives the unique allowed signs
  t_i=s_i(1-2z_i), b_i=-t_i,
  r_i=s_i[1-2(z_(i-1)+z_i)].
This is a bijection for every even L>=4, not an extrapolation of the finite
counts. Its linear extension maps orthonormal bases and is unitary.

Under this bijection, toggling z_i flips exactly T_i,B_i,R_i,R_(i+1).
It is allowed iff z_(i-1)=z_(i+1)=0. If z_i=0 with these neighbors zero,
(t_i,b_i,r_i,r_(i+1))=(s_i,-s_i,s_i,-s_i). For s_i=+1, W_i^dag acts; for
s_i=-1, W_i acts. Each coefficient is one because ordinary spin-1/2
raising/lowering matrix elements are one. Their adjoints reverse the move.
If either neighbor is occupied, the toggled independent set is illegal;
Gauss conservation then makes both plaquette terms vanish (equivalently,
one of their local raising/lowering factors annihilates that configuration).
They cannot both act on the same input because their top-rail requirements
are opposite. Consequently the exact operator identity is
  H_link|Gauss = H_PXP direct-sum 0 direct-sum 0
for all even L>=4, in the supplied normalization.

This proves the previously finite-only dictionary at all relevant lengths.
The primary runner checks it additionally by direct
Gauss reconstruction and exact local plaquette actions at even L=4,...,16.
Those finite checks are controls; the symbolic argument above is the all-L
proof. The proper statement preserves the supplied background and law.

For the full-sector partition function Z_full,L(b)=Z_L(b)+2, the common
spatial operator is K_b direct-sum I_2. It is again real self-adjoint and
Hilbert–Schmidt, and Tr(K_b direct-sum I_2)^L=Z_L(b)+2 for every even L.
The exact seed script adds 2 to both trace endpoints and verifies
  S_full(6,4)>0.9246613015940813140814104761886408,
  T_full(12,4)>0.9365536948219019879096531631200829.
The same 23/25 seed threshold and scalar choices therefore apply, proving
the same full-sector gap bound by the bootstrap. This explicitly accounts
for the frozen spectrum; no inference from the dynamic-sector gap is needed.


## Reproduction and review record

Primary runner: [periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py](../scripts/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py).
Paired result: [content-pinned cache](../logs/runner-cache/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.txt).
The runner is standard-library only and reads no external scientific inputs. It prints all integer moments and exact rational endpoints; decimal displays are secondary. The finite Gauss controls cover even L=4 through16; the written proof supplies the all-length statement.

The initial proof was checked by the author against the complete external bootstrap. A separate coordinator implementation constructed the complete L6 and L12 graphs from legal bit tuples and Hamming-distance-one edges, with no rotational reduction, and reproduced all257 integer moments and both seed bounds for both sector choices. A fresh scientific reviewer checked the complete analytic proof and independently reproduced all moments using the Hilbert–Schmidt identity, every rational endpoint, and the Gauss dictionary by exhaustive link-assignment enumeration at L4 and L6. Deliberate temporal-seam, hard-core and plaquette-orientation defects were detected. No proof-critical defect was found for the stated model. This is selective independent review, not a formal audit verdict; the final packaged note, runner and paired cache have been checked by the same independent reviewer.

The scope statement is a positive theorem for explicit Hamiltonians. No universal impossibility claim, count of independent physical walls or rejection of untested higher-dimensional models is part of this packet.
