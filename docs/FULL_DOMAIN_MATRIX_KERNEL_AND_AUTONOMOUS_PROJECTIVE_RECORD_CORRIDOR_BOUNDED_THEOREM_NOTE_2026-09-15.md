---
claim_id: full_domain_matrix_kernel_and_autonomous_projective_record_corridor_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied full-M2 probability kernel and smooth bounded local activation rate, a finite guarded seed generates every prescribed finite one-qubit rank-one projective history with its supplied Born weights. The generator itself determines the order, is nonexplosive for every finite initial Record configuration, and is covariant under lattice translations, proper cubic rotations and simultaneous GL2 similarity. Law, rates, seed and physical event calibration remain supplied."
upstream_dependencies:
  - minimal_axioms
  - record_projective_history_local_append_downstream_law_candidate_bounded_theorem_note_2026-08-21
runner: scripts/full_domain_matrix_kernel_and_autonomous_projective_record_corridor_2026_09_15.py
---

# Full-domain matrix kernel and autonomous projective Record corridor

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

The explicit selected local generator below implements arbitrary finite
one-qubit projective histories on a supplied guarded seed. Its conditional
content law is a probability kernel on the entire M2(C) possibility domain;
its smooth local activation determines the event order. The written proof
and personal exact checks are author proposals awaiting independent review.

## Target, premises and authority

The target is a local-carrier and formation supplier for the one-qubit
benchmark in the [provisional projective-history Law](RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md).
That source supplies the trace probabilities. The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
provide the full M2 possibility domain, nearest-neighbor conditional odds and
permanent Records; they do not select the displayed rule, seeds or rates.
This is a construction under explicit candidate data, not a complete physical
realization of the four axioms or an independently ratified law.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: record_projective_history_local_append_downstream_law_candidate_bounded_theorem_note_2026-08-21
target_blocker_text: "Supply one total local matrix kernel and a generator-derived event order for arbitrary finite one-qubit projective histories."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the total kernel and all-frontier invariant; seek physical seed, event calibration and a composite entangled-law supplier."
conditional_surface_status: "The explicit kernel, rate convention, finite guard seed and trace-probability benchmark are supplied."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A total probability/rate construction and inductive geometric proof with separately calculated exact transcript and frontier checks."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

| Input or obligation | Provenance and use | Disposition |
|---|---|---|
| Full M2 domain and permanent neighbor Records | Current axiom memo | Framework interface; physical attachment remains open |
| Rank-one trace probabilities and normalized projective update | Owner-selected provisional source above | Supplied mathematical benchmark |
| Numeric matrix tags, functions h/psi/f, local rate | Defined in sections1-2 | Selected extensional rule, not derived from the axioms |
| Initial density carrier, finite program list, scalar markers and zero guards | Section3 | Supplied finite seed |
| Probability, covariance and regularity of the content kernel | Section1 | Derived here on every fixed presence pattern |
| Finite-seed nonexplosion and unique corridor activation | Sections2-3 | Derived here |
| Transcript probabilities and dimensionless waiting-time law | Section4 | Derived from the selected generator |
| Physical event calibration, seed genesis, composite entangled coupling | Separate physical suppliers | Open; no conclusion about their impossibility |

Each neighbor is either absent or a matrix; absence is an isolated input type.
All regularity statements concern fixed presence patterns. Internal GL2
similarity covariance is an explicit stronger mathematical challenge, not a
newly asserted axiom. Physical qubit density/projector interpretation is used
only on the benchmark subset and its simultaneous similarity images. Matrix
Record content is directly readable; an experimental plus/minus label is
obtained by comparison with the separately readable program. Copying a Record
is classical content copying and makes no unknown-quantum-state cloning claim.

## 1. The program tag separates an input from an outcome

Define h(t)=exp(-1/t) for t>0 and0 otherwise, and

 psi(u)=h(1-u)/[h(1-u)+h(u-1/4)], u>=0.

The denominator is positive; psi is smooth, equals1 for u<=1/4, equals0
for u>=1, and takes values in[0,1]. Use carrier A=2I+rho. Encode a program as
B=8I+P, so its trace is17, while an outcome R has trace1. Define

 r(A)=psi(|tr A-5|^2),
 p(A)=psi(|tr A-17|^2+|det(A-8I)|^2),
 o(A)=psi(|tr A-1|^2+|det A|^2),
 k(A)=psi(|tr A-4|^2+|det A-4|^2).

Here k identifies the scalar marker2I on the benchmark, while o identifies
the benchmark rank-one outcomes. These functions are total smooth real
functions of all eight real matrix coordinates and similarity invariant.
They are all zero at the zero matrix. They are mathematical tag choices.

Define the pair weights by w_ij=r(A_i)p(A_j), and put
P_j=A_j-8I and x_ij=Re tr[(A_i-2I)P_j]. Sum only over present neighbors,
with the empty matrix sum defined as0. For any continuous f:R->[0,1] and
arbitrary M2 input tuples set

 S=sum_(i!=j) w_ij, b=(S-1)^2, Z=S+b>=3/4,
 K_f(eta)=[b delta_(sum_i A_i)
   +sum_(i!=j) w_ij(f(x_ij)delta_(P_j)
                    +(1-f(x_ij))delta_(I-P_j))]/Z.        (1)

The full-domain probability, weak continuity, conjugation equivariance,
simultaneous GL2 similarity covariance and neighbor-permutation invariance
proofs follow from the finite sums. Every pair weight is nonnegative, and
the total atom mass is S+b=Z. Traces, determinants and their real and
absolute values are similarity invariants; every output atom transforms by
simultaneous similarity. Summing all ordered pairs is neighbor-permutation
invariant. Integrating a bounded continuous test function gives a finite sum
of continuous terms divided by Z>=3/4. For a smooth f, smooth compactly
supported test functions give derivatives of every order. No adjoint, matrix
basis or eigenvector ordering enters this kernel. Zero-valued neighbors
contribute neither tags nor a nonzero summand and may be ignored by (1).

With f_B=clip to[0,1], a carrier and program give r(A)=p(B)=1,
r(B)=p(A)=0, hence S=1 and b=0. For positive trace-one rho and a rank-one
orthogonal P, tr(rho P) lies in[0,1]. Thus the kernel is exactly
tr(rho P) delta_P+[1-tr(rho P)] delta_(I-P), including both zero endpoints. A single outcome gives delta_R. An outcome and
marker2I give delta_(R+2I). The program by itself no longer has an outcome's
trace; its formation activity can be distinguished locally.

## 2. A smooth rate function on the entire input domain

Let c=sum_i r(A_i), q=sum_i p(A_i), u=sum_i o(A_i), v=sum_i k(A_i), and

 D_measure=(c-1)^2+(q-1)^2+u^2+v^2,
 D_copy=c^2+q^2+(u-1)^2+v^2,
 D_retag=c^2+q^2+(u-1)^2+(v-1)^2,
 a=psi(D_measure)+psi(D_copy)+psi(D_retag),
 lambda(eta)=a/[a+(a-1)^2].                             (2)

The denominator is at least3/4. Hence lambda is smooth, lies in[0,1], and
has all the same matrix and lattice covariances. In the three intended
contexts the count vectors are (1,1,0,0), (0,0,1,0), (0,0,1,1); exactly one
psi term is1 and the others are0, so lambda=1. At an empty/zero-only context,
a program alone, or a marker alone, each psi term is0 and lambda=0. These
are direct substitutions; a sharp type predicate is unnecessary.

For a finite Record configuration x, define the pure-append generator

 (L F)(x)=sum_(blank z) lambda(eta_z(x))
       integral [F(x union{(z,A)})-F(x)] K_f(eta_z(x),dA). (3)

Only sites adjacent to a Record can have a positive rate. If n Records are
present, there are at most6n such blank sites, each of rate at most1. The
jump construction is nonexplosive. To see this without relying just on a
divergent sum of mean holding times, stop at the Mth Record. The stopped
count satisfies E N(t wedge tau_M)<=n_0 exp(6t) by its rate bound and Gronwall.
Consequently Pr(tau_M<=t)<=n_0 exp(6t)/M, which tends to0 as M increases.
This supplies a total finite-seed Markov process
without a separate caller scheduler. A selected dimensionless rate is not a
derived empirical clock.

The Born version has a weakly continuous content kernel. Alternatively set

 f_S(x)=h(x)/[h(x)+h(1-x)], x in R.                     (2a)

Its denominator is positive and it is smooth, equals0 for x<=0 and1 for
x>=1, and satisfies f_S(1-x)=1-f_S(x). It gives a weakly smooth full-domain
kernel with the same smooth activation rate and the same copy/retag rules.
At tr(rho P)=1/4 its probability is1/[1+exp(8/3)], distinct from1/4. Both
are explicitly supplied members of the construction. The latter's transcript
is the product of its f_S transition probabilities; formula(6) below is for
f_B only. No probability-selection claim is made.

## 3. Finite guard seed and its literal geometry

Fix a positive finite measurement count L. The zero-length history is the
empty cylinder with probability1 and needs no formation; it is covered
separately by an absorbing zero-only seed. Let T be the3L initially blank
axis sites (x,0,0), x=0,...,3L-1. Initial nonzero Records are

 a_0=(-1,0,0), content2I+rho_0;
 p_j=(3j,-1,0), content8I+P_j, j=0,...,L-1;
 k_j=(3j+2,1,0), content2I, j=0,...,L-1.

Let C consist of T and these1+2L seed sites. Put a permanent zero-valued
Record at every site of the external vertex boundary

 G={z outside C: z is a nearest neighbor of some c in C}. (4)

This is an explicitly supplied finite seed; the guard is part of its cost.
There are at most6|C| guard sites and |C|=1+5L. The bound is deliberately
coarse and requires no runner-derived asymptotic count. Every later nonzero
Record lies in C, and every neighbor outside C is already in G. Consequently
any remaining blank site outside C sees only zero Records or no Records and
has rate0. The guard blocks locations by their being already permanent
Records, not by an unrecorded geometric mask supplied to the generator.

Initially only e_0=(0,0,0) sees carrier plus program. Every later event e_j
sees only its program, every c_j=(3j+1,0,0) sees no nonzero Record, and every
next-carrier site a_(j+1)=(3j+2,0,0) sees only its marker. Their rates are0.
When e_j forms R_j, only c_j becomes active and copies it. When c_j forms,
only a_(j+1) becomes active and writes2I+R_j. That activates e_(j+1), if it
exists. Every other adjacent site is an old permanent Record or a zero guard.

Induction gives exactly one active blank site at each unfinished stage:

 e_0,c_0,a_1,e_1,c_1,a_2,...,e_(L-1),c_(L-1),a_L.        (5)

After3L writes there is no active blank site. This is an invariant of the
local generator on the stated seed sector, not a supplied event order.

## 4. Transcript law and duration

The unique active site's rate is exactly1 at every stage, independently of
the realized branch. Its holding times are independent rate-one exponential
variables, and the total completion time has the Erlang law with shape3L.
Thus E tau=3L and Var tau=3L in the selected dimensionless units. The marked
jump construction separates these waiting times from the outcome draws.

At the measurement steps, (1) gives

 Pr(R_0,...,R_(L-1))
   =tr(R_0 rho_0) product_(j>=1) tr(R_j R_(j-1))
   =tr[R_(L-1)...R_0 rho_0 R_0...R_(L-1)],             (6)

because R rho R=tr(rho R)R for rank-one projectors. Zero branches are not
normalized. All preceding Records, including zero guards, persist. With a
supplied countable corridor/guard seed the same single active sequence can
continue indefinitely; the sum of the rate-one waiting times diverges almost
surely, so this particular infinite-seed sector is also nonexplosive. No
arbitrary infinite-configuration process is claimed by this argument.

## 5. Relation to the current source and open suppliers

The existing corrected active-cut note
`ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md` already constructs a selected local
continuous-time process and derives its order on a supplied corridor. Its
complete real Bloch/Gaussian/Haar codec and archive quotient differ from this
construction. It is prior machinery, not evidence that autonomous formation
has first been discovered here. This proposal instead gives a small direct
M2 kernel on the entire possibility domain, explicit similarity covariance,
and exact arbitrary finite one-qubit projective transcripts under supplied
trace weights. It makes no priority claim.

An external event list is replaced by consequences of the displayed selected
generator and guard seed.
The full extensional rule, rate convention, initial carrier, programs, scalar
markers, zero guards, projective event calibration and any composite entangled
history coupling remain inputs or open suppliers. No genesis from an empty
configuration occurs: its rate is0. No new axiom or primitive is requested.

The exact personal checker enumerates ALL blank sites adjacent to Records,
without receiving a target mask. Across32 five-measurement transcript branches
it checks187 complete frontier states, preserving all old Records, copy and
retag contents, and agreement with separately computed ordered matrix
products. This fixture has98 seed Records, of which87 are zero guards, and
adds15 Records per branch. Three nonunitary similarities and24 proper cubic
rotations are also executed, together with a zero-branch repeat fixture.
Actually omitting guards produces extra enabled sites; omitting program tag
separation changes the enabled frontier. The quarter-probability smooth
alternative is checked exactly. These finite author tests are not an
independent review or a numerical proof for arbitrary horizons.



## No-Go Discipline Gate

This proposal submits the affirmative construction and its explicit alternative
weights. It makes no universal no-go, physical nonselection theorem, or claim
that an axiom update is required.

### N1 — Actual construction challenges

| Marker | Attempted shortcut | Executed outcome |
|---|---|---|
| ATTEMPTED | Change the trace transition weight while retaining the projective transcript claim | Squaring the actual probability changes the transcript relative to separately ordered matrix products. |
| ATTEMPTED | Replace the full neighbor stencil by five directional inputs | The actual rate omits one direction and fails the rotated all-frontier check. |
| ATTEMPTED | Remove the permanent zero guard while retaining a single active site | All-frontier enumeration finds extra enabled blank sites. |
| ATTEMPTED | Use an untagged program as though it were distinct from an outcome | The actually changed seed enables a different frontier. |
| ATTEMPTED | Transpose the matrix output inside the similarity-covariant kernel | A nonunitary transformed fixture detects the altered output. |

These finite witnesses delimit shortcuts to this construction. They do not
rule out other compilers, initial states, probability laws or physical phases.
Endpoint-repeat, smooth-weight and off-code-normalization mutations provide
three additional finite sensitivity checks in the author packet.

### N2 — Dependency relations

The transcript proof depends jointly on the chosen probability rule and the
single-active-site induction. The latter follows from this generator and
seed, so it is not counted as an independent physical wall. Genesis,
calibration and composite coupling are explicit unproved suppliers; their
pairwise independence is not asserted and no wall count is assigned.

### N3 — Explicit premises

The input table names the selected functions, tags, rate, seed and trace
benchmark. Simultaneous GL2 covariance is a property proved for the candidate,
not an additional unannounced axiom. Positive density and orthogonal projector
typing is used only on the benchmark and its similarity images. The full
kernel remains defined on every matrix tuple. The Markov jump construction
supplies its own probability composition; physical realization is separate.

### N4 — Evidence matching

The local kernel is evaluated on the actual neighbors discovered from the
Record configuration, and direct ordered matrix products use the same
preparation and projectors. Omitted guard and tag controls change those
actual data. No prior no-go or differently typed matter theory is a witness
for this theorem. Prior compiler notes are context, not proof inputs for a
negative claim.

### N5 — Resolution

Exact matrix operations, individual target frontiers and finite transcript
branches are executed. Arbitrary-horizon induction, nonexplosion and the
special countable-seed extension are written arguments. The cache's five
resolution lines distinguish those scopes. No finite run executes an entire
infinite lattice or establishes a physical field or matter theory.

### N6 — Remaining constructive paths

The displayed construction supplies a kernel and event-order mechanism under
selected data. The smooth alternative probability rule is another explicit
choice. Physical preparation and calibration could change which choices are
relevant; neither is assumed absent from the framework. No approved primitive
is demoted to a wall, and no new-axiom request is made.

### N7 — Strongest scope challenge

A reviewer should insist that the Born weights and the prepared corridor
already encode substantial operational structure. The positive theorem
shows that a particular full-domain local rule can carry that structure; it
does not explain why nature chooses it. A physical derivation must still
supply or identify the initial Records, event calibration and entangled
composition. Those are concrete future obligations, not consequences of the
compiler's covariance or its count of successful checks.

### N8 — Earlier mechanisms

The corrected active-cut and random-axis notes already derive local ordering
under their own selected codecs and generators. The current proposal keeps
that prior success explicit and supplies a different full-domain matrix
kernel. The provisional projective-history source's Born and composite
cylinder choices remain supplied. No earlier physical wall is declared
retired merely by replacing its terminology or by reusing this constructor.

## Author review and reproduction

The declared primary runner is self-contained and reads only its own source
for an integrity hash. Its canonical cache is emitted by runner_cache with
the declared300-second timeout. The primary tests two five-measurement
programs with different transition probabilities, exact copy and retag
contents, all frontier sites, zero branches, three nonunitary similarities,
24 proper cubic rotations, and actual guard/program-tag omission controls.
Sixty-four additional floating contexts outside the prepared code exercise
normalization, bounded rates, similarity and complex-conjugation covariance,
neighbor permutations, and local continuity. Their finite floating errors
are not interval certificates or proofs of differentiability.

The exact transcript comparison evaluates ordered matrix products separately
from the literal local generator. The frontier finder receives the whole
Record set and no intended target mask. The geometric induction and stopped
count proof carry the arbitrary-horizon and finite-seed existence statements.
Eight executed source mutations are recorded in the author packet; their
failures test sensitivity of actual operands and geometry, not labels.

Earlier local generators and repeat instruments are prior machinery. The
corrected random-axis source
`ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md`
explicitly distinguishes its encoded role/frame action from conjugation of
the full matrix payload. The present direct kernel has simultaneous GL2
similarity covariance by its trace/determinant construction. No novelty is
claimed for the Born formula, projective update, local jump processes or
nonexplosion criterion in isolation.

The note's mathematical construction, its finite evidence and any future
physical attachment require independent review. Formal authority belongs
to the independent audit path. No audit verdict, axiom, primitive, editable
prompt or main-branch science change is made by this author proposal.
