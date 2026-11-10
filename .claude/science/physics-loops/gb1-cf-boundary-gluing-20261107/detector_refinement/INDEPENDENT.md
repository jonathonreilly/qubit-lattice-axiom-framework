# Independent finite detector/refinement derivation

This is a hand check of the raw construction supplied in the bounded worker
brief, and an independently implemented certificate oracle. It is not an audit,
a retained result, or a derivation of this detector law from the four axioms.
The primary proof, local parser, runner, and previous reports were not read.
No numerical certificate has been executed by this worker. The mathematical
claims below concern the specified protocol; its implementation must pass the
separately supplied checker and the supervisor's mutation tests.

## Premises and exact domain

The axiom memo's SHA-256 is
`301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc`.
Its Admissibility rule supplies a neighborhood-dependent probability measure,
not a production clock, preparation protocol, detector program, or Born weights.
Record supplies permanence and content-determined readout, not finite-additive
scalar observables. The present construction separately supplies:

1. The 25-record seed, its integer matrix-content decoder, four preparation
   selectors, grouping program, and a finite 43-site patch with blank sites.
2. Radius 16 in the lattice L1 metric; the proper-frame template and exact
   predecessor matching rule; the fallback distribution on nine scalar matrices.
3. A global choice q in {1,2}, the powers n_i(s)^q, consecutive slot allocation,
   and the independent unit-rate exponential clocks for each enabled site.
4. An initially isolated patch, with all other sites absent, and permanent
   occupation after formation. No blank site is read as having value zero.

The clocks are a selected continuous-time Markov realization. Merely saying
that sites have equal rates without specifying a joint process would not prove
the race probabilities. All statements here use the independent-clock premise.
All explicit contents are central matrices vI; no local basis or unknown-qubit
measurement interpretation is used. Algebraic M2(C) membership does not make
the finitely many distinct scalar contents a quantum information capacity
theorem. The preparation and law select them as additional protocol data.

The required domain consists of each legal seed and its reachable prefixes,
including every translated and properly rotated copy. The total local kernel
is also defined outside this domain, but no invariant physical state space or
formation-completeness theorem for arbitrary record configurations is claimed.

## Local rule, covariance, and support

Write S for a seed. Its four header values occur nowhere else. The value 100
locates an origin; vectors from it to values 101,102,103 specify an ordered
orthonormal integer frame with determinant +1. On the prepared domain there
is exactly one such frame. All remaining seed contents, and the selector, are
then fixed by this frame; the seed has exactly 4+1+16+4=25 records.

The 16 pool positions, f, and c are distinct and are not seed sites. Their union
with the seed is the 43-site patch. In canonical coordinates every pair is at
L1 distance at most 15: the largest possible y separation is nine, x separation
five, and z separation one, and these bounds already sum to 15. All of it is
therefore visible from any one of its sites within radius 16, except that the
center record itself is excluded. Proper cubic motions preserve this fact.

Let m_i=n_i(s)^q and N=sum_i m_i. Since the selected column is a composition of
four, q=1 gives N=4; q=2 gives 4<=N<=16. Define b(j) by consecutive blocks of
length m_i, for 0<=j<N. Zero-length blocks contribute no j. Define global states

    R0=S,
    R1(j)=S union {z_j:1},
    R2(j)=R1(j) union {f:b(j)+1},
    R3(j)=R2(j) union {c:g_b(j)}.

At an enabled center the entire predecessor is visible. Unique marker-frame
decoding and exact matching therefore enable precisely these events:

    R0 -> R1(j), each j<N, rate 1;
    R1(j) -> R2(j), rate 1;
    R2(j) -> R3(j), rate 1;
    R3(j) -> no event.

In particular, an already recorded winner is visible to every other pool site,
so their R0 patterns fail. There is no second winner. A center outside the patch
cannot be a permitted target in the unique marked frame; missing a required
marker cannot produce a valid frame. Such centers have no enabled event.
These observations establish the event table without simulating the local parser.

For arbitrary neighborhoods, the instruction "exactly one legal predecessor
enables this center, otherwise fallback" is a single-valued rule by definition.
Its search is finite: there are finitely many visible marker positions and
proper integer frames. On the domain the preceding argument establishes
unique successful matching where an event should occur. The rate mask that
forbids forming at an occupied center is separate from the center-excluding
content distribution; old-record support uses the latter.

Under any translation/proper cubic rotation, the ordered markers, entire
template, L1 ball and exact-pattern condition transform together. Counts k,l
in the fallback are invariant. q is a scalar law parameter. Thus both kernel
and event rule are spatially covariant. A parser that tests only the canonical
orientation would violate this argument and be a software fault.

Let A={0,1,2,3,4,100,101,102,103}. In a fallback neighborhood,

    p=(1/2+l)/(1+k),  0<=l<=k,
    F(v)=1/18 + (p/2 if v=1; (1-p)/2 if v=0; 0 otherwise), v in A.

Here 0<p<1, and every used content has mass at least 1/18. Removing a seed
record from any prefix destroys a mandatory seed entry; no enabling predecessor
remains and its current content has positive fallback mass. For a non-seed
record, deleting it either leaves an expected enabling predecessor for that
same site, in which case its content is exactly the Dirac content and has
mass one, or leaves an unmatched neighborhood with positive fallback mass.
The first case occurs when deleting the winner in R1, f in R2, or c in R3.
Deleting earlier new records from later prefixes invokes fallback. Thus every
old record remains supported at every reachable prefix. This statement does
not assert monotonic support on all configurations outside the supplied domain.

## Formation, probabilities, and physical coarse writing

There are exactly 1+3N reachable record states, each R1/R2/R3 retaining its
distinct winner site. Every path makes exactly three new records and stops.
The first wait is exponential with parameter N; subsequent waits are independent
unit exponentials. All waits are finite almost surely, so completion is almost
surely finite and has mean 1/N+2. There is no deterministic finite deadline.

To derive the winner law directly, assign iid Exp(1) priorities T_j to the N
active pool sites. Ties have probability zero. Symmetry makes every j equally
likely to be the unique minimum, so its probability is 1/N. Equivalently,

    Pr(j wins) = integral_0^infinity exp(-t) exp(-(N-1)t) dt = 1/N.

Exactly m_i slots produce fine content i+1, giving

    e_i(s)=Pr(f=i+1 | s)=n_i(s)^q / sum_r n_r(s)^q.
    e_G(s)=Pr(c=1 | s)=sum_i g_i n_i(s)^q / sum_r n_r(s)^q.

The latter is not merely an analyst's relabeling: after the fine record forms,
the center c reads the recorded fine content and recorded grouping bits and
locks g_i I. Its content is a physical record in the supplied process. The
constant zero record c=0 and the absence of c are distinct states. Replacing
g with 1-g implements the complementary binary statistic.

For a fixed program, these four e_i are nonnegative functions on the four-element
preparation set and sum to the constant-one function. Grouping is ordinary
addition of probabilities of disjoint fine events. This finite operational
effect structure follows after the probability law and protocol are supplied;
it is not an extra scalar collection functional extracted from Record alone.

For q=1, e_i(s)=n_i(s)/4. Merging two rows of a program, replacing the emptied
row by zeros, preserves their grouped probability at every selector. Refining
an integer weight into nonnegative integer parts has the inverse property.
These statements concern the specified retained coarse output. Programs have
different readable seed weights, and may have different readable fine records.
They therefore need not have identical full-record distributions. In the
direct/refined examples a coupling can even keep winner and coarse times
equal for q=1, but the already-readable seeds still distinguish the protocols.
No universal equivalence under future record-sensitive extensions follows.

## Finite diagonal comparison dictionary

Supply complementary rank-one projectors P0,P1 as an external dictionary and
restrict the preparation set to s=0,1. Assign nominal labels

    E_i=(n_i(0) P0+n_i(1) P1)/4.

For q=1 these labels satisfy 0<=E_i<=I, sum_i E_i=I, and
tr(P_s E_i)=e_i(s). The binary label E_G=sum_i g_i E_i has
tr(P_s E_G)=e_G(s). The trace identity is checked from P_s P_t=delta_st P_s
and tr(P_s)=1, not used to generate the process probabilities.

Every grid effect (aP0+bP1)/4 with a,b in {0,...,4} is realizable by a binary
group: use columns (a,4-a,0,0), (b,4-b,0,0), and group the first outcome.
There are 25 such labels. Complements stay on this grid. Two labels with
coordinate vectors a/4,b/4 are summable precisely when a_t+b_t<=4 for t=0,1.
They have a joint menu with columns (a_t,b_t,4-a_t-b_t,0), and their group label
is their matrix sum. There are 15 choices for an ordered nonnegative integer
pair with sum<=4 in each coordinate, hence 225 ordered summable pairs.
Commutativity and defined associativity follow coordinatewise; the partial sum
is not defined beyond I. This is a finite diagonal structure, not the full
continuum of qubit effects, arbitrary POVMs, or noncommuting refinements.

For q=2, the same nominal labels generally cease to represent the response.
Take constant columns (2,2,0,0), group the first outcome: N=8 and e_G=4/8=1/2.
Refine to constant columns (1,1,2,0), group the first two outcomes: N=6 and
e_G=(1+1)/6=1/3. Their nominal grouped diagonal labels both equal I/2, while
their operational probabilities differ. Both are well-defined conditional
models with the same support/covariance proof; q=2 is not a software defect.
The two first-wait means also differ, 1/8 versus 1/6.

## What merge invariance actually forces on a general response weight

Suppose each four-slot composition n of total four has normalized response
w(n_i)/sum_j w(n_j), for nonnegative w(0),...,w(4), and the denominator is
positive for every legal menu. A merge replaces (a,b,c,d) by (a+b,0,c,d).
Require that the probability of the first two outcomes before the merge equal
the probability of the first outcome after it whenever an unmerged positive
integer spectator is present. Zero slots remain explicit slots in this statement.

Put u=w(1)>0, t=w(0)>=0; u>0 follows from the menu (1,1,1,1). Merging its first
two entries forces w(2)=2u+t. The same merge in (1,1,2,0) forces

    2u/(2u+w(2)+t) = w(2)/(2w(2)+2t).

Substitution gives (2u+t)^2=4u(u+t), hence t^2=0 and t=0. Thus w(2)=2u.
Merging 1 and 2 in (1,2,1,0) next gives 3/4=w(3)/(w(3)+u), so w(3)=3u.
These tests all have genuine positive-weight spectators after the deductions.

Conversely, w(0)=0, w(k)=ku for k=1,2,3, u>0, and arbitrary w(4)>0 satisfy
every such spectator merge. A merge with a nonzero spectator has a+b<=3,
so only the already-linear range is tested. A weight four can occur alone,
where normalization makes its outcome probability one. Therefore normalized
merge invariance on this domain leaves the endpoint w(4) undetermined.
If zero slots are deleted rather than retained, w(0) is outside that alternative
domain; it must not be inferred from unobservable padding. If only a selected
subset of merges is required, the conclusions may likewise weaken.

A response formula alone says nothing about waiting times. If one additionally
uses independent outcome clocks of rates w(n_i), then the total first-event
rate is sum_i w(n_i). Spectator merges preserve it in the above linear range.
Merging (1,3,0,0) to (4,0,0,0) preserves the deterministic coarse outcome for
every positive w(4), but preserves the first-wait distribution only if w(4)=4u.
Normalized outcome equality cannot impose this timing condition on its own.

## Failure of the extra four-preparation dictionary

Choose columns (4,0,0,0), (4,0,0,0), (0,4,0,0), (0,4,0,0), and grouping
(1,0,0,0). The first-group response is (1,1,0,0) for both q values. Now try
the additional identification s=0,1,2,3 with Pz+,Pz-,Px+,Py+ respectively.
The unique Hermitian matrix giving those four trace pairings is

    E = I - sigma_x - sigma_y,

because the first two pairings fix the I coefficient to one and the z
coefficient to zero, while the remaining two fix the x,y coefficients to -1.
Its eigenvalues are 1+sqrt(2) and 1-sqrt(2), so it is not positive. Alternatively,
an effect 0<=E<=I with unit expectation on both orthogonal z states must equal I,
which has unit, not zero, expectation on the other two states.

This refutes the proposed universal matrix dictionary for these uncalibrated
selectors. It does not refute quantum theory, prove a quantum no-go theorem,
or show that the selectors physically prepare the stated quantum states.
It exposes the missing calibration/compatibility premise that such an
identification would need. Arbitrary finite record programs already allow
response patterns outside that supplied qubit dictionary.

## Calibration-free dimension bound for the four-selector interface

There is also a stronger, narrowly scoped general-program corollary that needs
no Pauli dictionary. Fix one program with n_i(s)=4 delta_is for i,s in {0,1,2,3}.
For either q the selected column has exactly one nonzero block, so the fine
response is e_i(s)=delta_is. Thus one fixed detector distinguishes all four
selectors with certainty. Its grouping bits may be chosen arbitrarily; this
argument uses only the four-outcome fine record.

Suppose this interface admitted density matrices rho_s on a d-dimensional
Hilbert space and a single POVM {E_i}, with rho_s>=0, tr(rho_s)=1, E_i>=0,
sum_i E_i=I_d, and tr(rho_s E_i)=delta_is. Since a density matrix satisfies
rho_s<=I_d and the trace of a product of positive matrices is nonnegative,

    1=tr(rho_s E_s) <= tr(E_s).

Summing over s gives 4<=sum_s tr(E_s)=d. For d=2 this is a contradiction.
The trace inequality is elementary: tr((I_d-rho_s)E_s) equals the trace of
E_s^(1/2)(I_d-rho_s)E_s^(1/2), a positive matrix. The bound applies to mixed
states and arbitrary positive effects; it does not rely on projective
measurements, pure preparations, orthogonality guesses, or a chosen basis.

Consequently this selected four-state operational interface requires dimension
at least four in any faithful finite-dimensional density-matrix/POVM
representation. Calling the local possibility algebra M2(C) alone does not
force this scalar-record interface to be a one-qubit statistical interface.
Its literal scalar labels 0I,I,2I,3I are distinct record contents, not supplied
normalized density matrices. This does not assign Hilbert dimension two to
the entire 43-site apparatus, exclude quantum representations with larger
dimension, or establish a contradiction in quantum theory. Allowing the
measurement operator to depend on s abandons the stipulated single-POVM
representation of this fixed-program interface. No additional numerical
coverage is claimed for this corollary; it follows for the legal program above
from the all-program hand derivation.

## Oracle contract and verification limits

`reference_check.py CERTIFICATE --source-sha256 HASH` independently decodes the
global seed, reconstructs all 1+3N states, compares exact events/rates, and
checks every old record by deleting it and consulting the global predecessor
table; unmatched deletions use the explicit fallback mass. It propagates
terminal probabilities through that DAG and separately counts uniform-priority
winners. It does not parse local neighborhoods or import any primary code.
The external source hash pins the primary source expected by the supervisor;
it is not the axiom hash and cannot prove the certificate was honestly emitted.

Strict parsing rejects extra/missing keys, duplicate JSON keys, booleans in
integer fields, invalid rational masses, duplicate states/sites, wrong frames,
missing prefixes, extra events, and changed contents. Complete-bank coverage
is checked from seed semantics, not names: all 35 selected compositions for
both q, all 24 proper frames at both specified translations for both q, both
direct/refined menus, and all four selectors of one dictionary-test program
for both q. `--allow-partial-bank` relaxes only coverage for defect probes.
This finite bank is diagnostic, not an exhaustive test of all 35^4 programs.

The file also independently enumerates the 25 diagonal labels and all 225
summable pairs. The hand proof covers all legal programs under the stated
semantics. Neither the checker nor this note proves that primary source code
implements those semantics outside its emitted, checked certificate cases.

One targeted literature search found the standard competing-clock calculation
in [MIT OCW's 6.041SC worked example](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/d90c8084580501f7b8b246c5aa878e33_MIT6_041SCF13_Competing_Exponentials_300k.pdf)
and the positive-operator effect interval in
[The Range of a Module Measure Defined on an Effect Algebra](https://www.mdpi.com/2073-8994/14/9/1819).
These are orientation references; the required finite arguments are given above.
No novelty, full literature coverage, retained status, or cross-family checking
is claimed. The supervisor must execute certificates and mutation/tamper probes
before reporting any computational agreement.
