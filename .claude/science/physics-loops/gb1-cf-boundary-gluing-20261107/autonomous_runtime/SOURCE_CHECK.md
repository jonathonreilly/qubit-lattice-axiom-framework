# Source-exposed check of the autonomous candidate

Checked source: `autonomous_runtime/PRIMARY.md` in the supervisor's
`gb1-cf-pair/Physics` worktree, 184 lines, SHA256
`4ee06873b3d35b11db796f0c6030eac78804e7b277688752661018b0963d6d6c`.
Science premises remain pinned at `9213a55c3636c8bdbf4a1f692e902d4d6d7ac44a`.
This pass is source-exposed. `INDEPENDENT.md` is preserved unchanged.
No code or numerical run, source edit, commit, push, or audit verdict.

## Main finding requiring repair

Section 4's inference that old records remain admissible because their quantum
factors remain eigenstates is invalid as written. Eigenstate permanence proves
unchanged contents; Admissibility support is a property of the separately
specified neighborhood probability kernel. The candidate must define that
kernel at occupied and inactive sites, not just the enabled fresh target.

A repair is available: use the radius-R neighborhood excluding the queried
site; if it is a legal pre-event configuration for formation there, use that
event's Born menu. Otherwise use the fair measure on the two prepared pointer
projectors. The apparatus's recorded reference identifies those projectors.
Because R contains the whole apparatus, equal such conditions fix the same
phase/history/seed and odds. The latest deterministic tick sees its original
pre-event menu; an older deleted record makes a hole and receives the fallback.
For simultaneous value/tick appends, deletion of either after the joint event
also gives a hole, so the fallback supports both actual pointer values. Initial
records receive the fallback. Explicitly check this case partition; a claim
about density-matrix eigenstates cannot replace it. Outside the prepared orbit,
a further covariant fallback can be specified without adding formation events.

## Two smaller implementation clarifications

The displayed jump operator has only a prefix boundary guard. That alone does
not halt on a failed herald. Include an old-record active/halt projector (or
state explicitly that K vanishes on completed-failure sectors). In the source
protocol failure halts only AFTER its completion pointer flip and completion
record; it must not halt immediately after the value-zero record. Completeness
and gamma-I intensity apply to active legal sectors, not absorbed sectors.

The adjacent external tape produces five chain components in the old
distance-five record graph, once sufficiently long. Thus the old description
"marker is the sole nontrivial component" no longer applies. The frame still
decodes uniquely: tape components have degree <=2 and are separated from the
native box by more than five, while the marker retains its unique degree-three
center and arms of lengths 1,2,3. State this adjusted decoder explicitly.

## Section 6: direct mathematical check

For every six-neighbor condition, 0<=l<=k<=6 gives

    p_a >= a/7 > 0,       1-p_a >= (1-a)/7 > 0.

Adding an I neighbor changes p by
(k+1-a-l)/[(k+1)(k+2)]>0; adding 0 changes it by
-(a+l)/[(k+1)(k+2)]<0. Thus the law varies, and every formed 0 or I stays
supported under every later neighbor condition. No neighborhood-monotonicity
assumption about records beyond one-write permanence is needed.

The full possibility measurable space is M2(C), while the law's support is
{0,I}. This is compatible with the current memo's explicit support reading:
it does not require every matrix to receive positive probability somewhere.
Zero and the multiplicative identity are definable by algebraic structure and
fixed by every algebra automorphism, so their selection privileges no basis.
The numerical parameter a is an additional MODEL CHOICE, not a consequence of
that invariance. The map X->I-X is not an algebra automorphism exchanging them.
The two a values consequently give distinct laws for the same fixed readout.

State the legal-record domain explicitly as {absent,0,I}^Z3. The kernel can be
evaluated on arbitrary M2-valued neighbor conditions, but an initial record
A outside {0,I} would not be supported by it. Therefore this is not a claim
that arbitrary existing matrix records are valid initial states. Empty-start
preparation is one allowed boundary condition. The construction also extends
to any prescribed initial configuration in the stated legal-record domain;
initial records stop ancestor recursion. No special lattice origin is needed.

The infinite-lattice construction is sound. Fix a root birth time r<=t. For
any self-avoiding path of m ancestors, their independent exponential densities
are at most one. Integrating strict decreasing times in (0,r) gives at most
r^m/m!. There are at most 6^m paths, hence the claimed bound (6t)^m/m!.
Repeated-site paths cannot be strictly decreasing. This bound tends to zero.
Finite branching then implies a finite ancestor set almost surely: an infinite
set would contain arbitrarily long ancestor paths. Countably many roots and
integer t bounds give simultaneous well-definedness for every site event.
Countable ties have probability zero; each site's exponential time is finite
almost surely. There is no need for a globally first event or finite total
lattice birth rate. Infinitely many distant events in finite time are harmless
for these finite ancestor queries.

Memorylessness really gives a record-only Markov process here. Up to time t,
no realized value can depend on an unformed site's future time or uniform mark;
that site has influenced no earlier event. Conditional on the past, every
unformed site's residual wait is independent Exp(1), with an unused independent
mark. Future conditional contents depend only on currently recorded neighbors.
Equal current configurations therefore have identical future laws. Translation
and proper-rotation covariance follow from iid clocks/marks and the unordered
six-neighbor counts. Readout is a fixed function of present content alone.

Thus section 6 supplies two consistent mathematical examples under the memo's
stated domain/support semantics. It does not select physical probability values,
derive a formation time, implement gauge data, or prove empirical adequacy.
This is a model-existence/underdetermination statement, not a universal no-go.

## Remaining clock claims

With the halt guard made explicit, exactly one boundary channel is active on
a promised prefix. Earlier raising operators annihilate recorded ones; later
predecessor projectors annihilate blank zeros. Kraus completeness gives total
intensity gamma_j I on the full reached live/work sector, so no-jump evolution
is a scalar and leaves normalized states fixed. The rate depends on a phase
decoded from records, not an external counter; phase-dependent gamma_j is still
time-homogeneous. Finitely many positive rates give the stated T/gamma_min bound.

The entire apparatus lies inside the declared loose finite R. Reconstructing
rho_R from the specified seed then makes all selected Born laws functions of
that neighborhood. Unknown reference extensions cannot be reconstructed from
system records, but the source correctly restricts extension claims or queries
only the reduced system; passive-reference instrument identities remain valid.
The rate-1/rate-2 no-event witness is correct: exp(-u)/(exp(-u)+exp(-2u))=2/3
at u=log(2). It diagnoses that model, not all possible waiting laws.

No short-range physical actuation follows from any of these checks. The atomic
joint gate/tick law, its rate and its Born interpretation remain chosen inputs.
The source makes that boundary explicit. The support completion and halt guard
are concrete repairs needed before accepting the whole candidate as written.
