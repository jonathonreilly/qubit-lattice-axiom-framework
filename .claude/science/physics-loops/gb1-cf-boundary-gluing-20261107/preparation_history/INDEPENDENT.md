# Preparation/history sufficiency: independent finite-dimensional check

Research result; conditional mathematics, not an axiom-derived law or audit.
Scientific source revision: `40bf8ab61128cfa0ff7c2e99663300d4ee2b5c1f`.
All scientific reads used `git show REV:path`; no parent candidates or scripts
were read. Git blob identities:

| Source | Git blob |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` (complete) | `c740addc83df1a87798ad1826f2984e98b9d5117` |
| `native_records/RESULT.md` in this target (complete) | `23fb68ba678b2c24b0a92d706f69584e9dfcce72` |
| `docs/RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md` (lines 1–500; relevant §§1–6) | `ca475ec5b950d52f76ff3191371684ee24352af4` |

Process instructions read at worktree HEAD `f5af11cd0102cfd0b51aef0911f600130bf5beb1`;
workhorse scoped-worker contract used. `lab_ops.py preflight` returned `go`:
114 GB disk, 30% free memory, load 6.9; memory cap unavailable; no numerical job.
Configured inherited model retained; no model substitution. This is a separate
restricted-input proof derivation, not a cross-provider confirmation. The supplied
source restriction precludes a fresh literature search; none is claimed.

## 1. Exact theorem: the information that must factor through records

Let H be finite dimensional. A supplied finite quantum process starts with an
actually fixed density operator rho_alpha, then applies completely positive (CP)
instrument maps. Their sums are trace preserving. Controls and allowed futures
(including stopping rules) must be determined by r and a stated query/program,
never by unrecorded controller memory. The history family is closed under its
permitted continuations. Include any environment that will interact again in H;
a permanently passive environment may be traced out.

A fine history h has positive weight z_h=Tr(sigma_h), normalized rho_h=sigma_h/z_h,
and permanent ledger R(h)=r. Zero-weight histories are excluded from conditioning.
For a permitted future finite event word w, let E_(r,w) be its effect, obtained
by applying the adjoints of its CP maps to I, in reverse temporal order. Include
the empty word I. Let O_r be the real span of all these effects. A finite horizon
is enough; arbitrary finite horizons are also allowed when the supplied process
and control domain are fixed. The following are equivalent:

(a) Every permitted future-cylinder probability has one value on each ledger fibre.
(b) Tr[E_(r,w)(rho_h-rho_g)]=0 whenever R(h)=R(g)=r, for every w.
(c) Every difference rho_h-rho_g in that fibre lies in O_r's trace-orthogonal space.

Proof: the Born/instrument cylinder formula is Tr(E_(r,w) rho_h), by adjointness.
Equality of these scalars is exactly (a)⇔(b); linearity gives (b)⇔(c). Define the
record kernel by this common value. CP positivity and instrument completeness
give nonnegativity, normalization and prefix consistency. If an observed branch
a appends r' and has common nonzero probability p, its two conditional states
satisfy Tr[E_(r',w)(Phi_a(rho_h)-Phi_a(rho_g))]/p=0: the numerator is the difference
for the composite word aw. Thus the predictive classes are preserved under the
conditional updates. A zero-probability branch supplies no conditional state.

This is both a sufficiency and a necessity theorem for the declared family of
histories, controls and queries. Equal next-event probabilities alone are weaker
than (a). O_r can be characterized as the smallest family containing I and closed
under the allowed branch adjoints; with finitely many control/record states its
total dimension is at most |R| dim(H)^2. This is an exact span characterization,
not a numerical certificate or a claim that the physical family has been supplied.

Unique rho(r) is sufficient, not necessary. For Z-only future projectors and no
mixing evolution, |+><+| and |-><-| have identical future Z histories. A future X
test separates them. Arbitrary future effects force equality of density operators;
the native electric/magnetic future algebra must be checked rather than assumed
tomographically complete. Passive external states need not be uniquely fixed if
their reduced state on the future-operated system is fixed.

## 2. Complete-history reconstruction, including magnetic evolution

Suppose the permanent ledger decodes an actual preparation label alpha, the
ordered executed programs, all recorded outcomes, and every evolution parameter
not already fixed by those records and the supplied law. Let

  sigma_r = Phi_(m,y_m) o U_m o ... o Phi_(1,y_1) o U_1 (rho_alpha),
  U_j(X) = exp(-i t_j H_j) X exp(i t_j H_j),
  Phi_(j,y)(X) = sum_k K_(j,y,k) X K_(j,y,k)^dagger.

Then rho(r)=sigma_r/Tr(sigma_r) gives every permitted future probability, and
appending the next decoded event gives the corresponding normalized CP update.
Proof is induction on the number of executed maps; the cylinder weight before
normalizing is exactly Tr(sigma_r). This proves all supported prefixes of the
specified finite program, not just a list of benchmark examples. H_j may contain
the supplied magnetic terms: commutativity with old electric projectors is not
required when the actual chronological product and durations are retained.

Hidden Kraus labels k need not be recorded: sum their CP branches, not amplitudes.
This also covers the native reader's unobserved edge e. It presupposes the fixed
instrument and no later control that consults a hidden k. If a hidden controller
interacts again, its correlations must instead be included in the process model.
An actual preparation must satisfy the dictionary entry rho_alpha (or its exact
predictive class). Writing a label that merely *asserts* that preparation proves
nothing about the physical input. The preparation/calibration premise remains.

## 3. Discriminating examples and safe coarse-grainings

**A label is not preparation.** The native source's Gauss-compatible vacuum and
single occupied plaquette have the same blank ledger; at a plaquette corner the
next b=1 probabilities are 0 and 1/3. Giving both the same preparation label does
not change this. A preparation restriction or an independently correct label-to-
preparation bridge is required, not merely a new name for the inputs.

**Order can matter.** Start with rho=I/2. Perform X+ at target a and Z+ at target b,
or the reverse, recording only those two site/projector pairs. Both histories have
weight 1/4 and the identical final ledger. Their normalized data states are P_Z+
and P_X+, respectively; a future Z+ probability is 1 versus 1/2. In contrast, when
the CP maps of incomparable events commute, every linear extension gives the same
unnormalized state (adjacent swaps prove this). The compatible native electric
maps commute without interleaved evolution: all link-sector projectors commute,
and sums of their sandwich maps commute. Therefore order is not always necessary;
the sufficient test concerns the maps, including inserted evolution, not labels.

**Omission differs from forgetting an outcome.** With rho=P_X+, omitting a Z
measurement gives future X+ probability 1; performing it and forgetting the
outcome gives sum_b P_Zb rho P_Zb=I/2 and probability 1/2. If its occurrence and
position in the program are known from records or the fixed program, the latter
CP map is reconstructible without its outcome. Unknown occurrence is different.

**An unlogged specified null attempt can matter in the native construction.**
At empty r take a half-and-half mixture of compatible origins p and q, with blank
pointers and vacuum data. Attempt x in V_p. Its null branch leaves only q, still
with empty r. A further attempt at x succeeds with probability 0, compared with
1/2 before the unlogged attempt. This uses the source's allowed specified-site
instrument and orthogonal origin sectors. It does not refute uniform averaging:
with empty r, a uniform null leaves each normalized diagonal origin block unchanged
and multiplies off-diagonal origin blocks by 123/124. Coherence loss alone is
invisible to the native block-diagonal future effects; hidden evolution may still
change the diagonal data. Thus recording every null is sufficient, not necessary.

**Known null loops can be integrated out.** Let N_0 be the no-record CP map per
attempt (including its supplied evolution), and S_y the success maps, with
N_0+sum_y S_y trace preserving. If Tr[N_0^m(X)] tends to zero for every allowed
positive X, then Psi_y=sum_(m>=0) S_y o N_0^m is a next-success instrument normalized
on that domain. The partial total trace is Tr(X)-Tr[N_0^(M+1)(X)]; positivity
and finite dimension give the CP limit and normalization. Replaying these Psi_y
reconstructs the posterior from successful records alone, provided their needed
order is encoded. In the native fixed-origin sector with k<n^3 records, uniform
attempts and a fixed supplied pulse U per attempt give
N_0(X)=q U X U^dagger, q=1-(n^3-k)/|Lambda|<1, so the condition holds exactly.
At capacity there is no next success. This law concerns the next successful event
with waiting unobserved; it is not the law conditioned on an externally supplied
elapsed time or attempt count. It removes null-count storage, not successful-
order, actual-preparation, local-carrier or physical-cadence obligations.

**Unlogged evolution has an exact test.** For future effect E and a supplied
Hamiltonian H, put C=i[H,E]. If C is nonzero on the allowed invariant subspace of
dimension d, rho=I/d+epsilon C is positive for sufficiently small epsilon>0, and
the derivative of Tr(E exp(-itH)rho exp(itH)) at zero is epsilon Tr(C^2)>0.
The same permanent r then occurs at different unrecorded elapsed times with
different future odds. This is a constructive conditional witness, not a verified
commutator for the particular native H: its defining note is outside this check's
allowed scientific sources. If the entire allowed future-effect space is invariant
pointwise under the unlogged evolution, its omission is predictively harmless.

**Hidden Kraus labels are not automatically missing information.** With
K_0=I/sqrt(2), K_1=X/sqrt(2), input |0>, and one coarse recorded outcome, the
correct posterior is I/2. The hidden k need not be known for future fixed maps.
If the same unrecorded coin later applies X^k, however, the final state is |0>;
replacing this correlated controller by a second independent average gives I/2.
An external log or controller is not a physical Record merely because software
can consult it. Native e labels can be marginalized when later H/control does not
consult them; identifying the historical measured edge is a different question.

The fibre theorem quantifies allowed *conditioned inputs*, not arbitrary Kraus
decompositions of one mixed input. With a fixed hidden-history prior and endpoint,
one can instead sum all hidden-path CP weights and normalize. That gives a valid
coarse posterior. To obtain an autonomous record law, its predictive class must
be the same every time the same r recurs. A conditional probability P(Y|r) for one
fixed experimental ensemble, with an unrecorded time index or prior in the setup,
does not by itself establish this stronger assertion.

## 4. A finite native carrier using only the already-free vertices

Here is a fully specified storage/reconstruction witness for a *finite supplied
event-indexed program*. Let N=n^3, n>=7, and choose B_0 dictionary bits and T event
slots with N>=49+7(B_0+T). Work in one compatible E_p; retain all F_p sites in |0>
and all data on the original A_p edge interiors. On V_p use coarse adjacency
(native displacement five). Store seven initial marker Records at

  a, a+e_1, a+e_2, a+2e_2, a+e_3, a+2e_3, a+3e_3,

where these e_i are coarse unit displacements forming a proper oriented frame.
The marker's connected shape has one degree-three root and arms of lengths 1,2,3;
it therefore intrinsically identifies a and the three directed axes. All seven
bits may be fixed at 1. Exclude the marker and its coarse nearest neighbors,
at most 49 vertices. A greedy independent set in the remaining degree-six graph
has at least (N-49)/7 sites. Choose its deterministic order by relative coordinates
in the recorded frame. Use the first B_0+T sites; these payload/output records
stay isolated and never join the marker, so the marker remains uniquely decodable.

The initial B_0 bits select a fixed finite dictionary of actually prepared reduced
data states and programs. Each entry fixes durations for the supplied H_native
and the target order, or fixes their deterministic dependence on earlier outcome
Records. Exact real constants can belong to this fixed dictionary; continuously
variable unrecorded parameters cannot be supplied by the finite bits. The next T
sites are distinct targets y_1,...,y_T. At step j apply the specified U_j and the
source's native instrument at y_j, and record its bit b_j there. The step is the
compound CP map

  Phi_(j,b)(X) = (1/6) sum_(e incident to y_j) P_(e,b) U_j X U_j^dagger P_(e,b).

At a fresh true-phase vertex its A_y is identity on compatible states: the unused
pointer is |0>, its detector is true, and no old Record lies in its data support.
Hence this scheduled step has no null branch, and sum_b Phi_(j,b) is trace
preserving. The native H restriction acts on data tensor identity on outputs;
old marker, packet and outcome Records survive every pulse. The output slots
encode the completed prefix order spatially, without host insertion order.
Section 2 therefore reconstructs the exact state and every future cylinder for
all supported prefixes up to T. No unrecorded qubit is read by the decoder.

Allow every translation and proper rotation of this entire construction and every
p. The marker transforms, its intrinsic coordinates transform with it, and the
source instruments/code transform covariantly. No lattice origin or frame is
privileged by the family; a particular recorded boundary condition supplies the
relative frame. All carrier sites are in V_p, with no enlargement of F_p. Exactly
7+B_0+T permanent records are consumed at the terminal prefix; no erasure or
renewal is used, and 125 phase sectors do not multiply one realized phase's N
available vertices. Initial marker/packet creation and preparation calibration are
supplied boundary conditions, not mechanisms derived here or implicit new axioms.

This witness uses the source's specified-site option, not its uniform attempt
clock. It treats each pulse-plus-write as one supplied event transition. If a
physical model permits queries or formation during an unrecorded continuous pulse,
section 3's invariance test applies; the event-indexed proof does not cover those
intermediate times. A fixed binary native carrier has at most 3^N record maps per
phase (absent/0/1), so mutually future-distinguishable preparation classes encoded
there must obey that finite count. Arbitrary matrix-valued packets from the older
history note cannot silently replace these native binary pointers.

## 5. Result and exact residual

Preparation plus ordered *process* information can make finite future event
probabilities functions of permanent record configurations alone. Sections 1–2
prove the general statement; section 4 realizes a finite sufficient carrier within
the free V_p sites. The original unrestricted (rho,r) process does not thereby
factor through r; its allowed inputs must satisfy the preparation/process contract.

Global record sufficiency is separate from permitted-neighborhood sufficiency.
One must additionally prove equality of the event probabilities whenever the
records agree on that neighborhood. At any fresh V_p target, every other V_p site
is at native distance at least five. Thus a record neighborhood of radius at most
four contains no marker, packet or earlier output; for preparation families with
different electric marginals, this carrier does not establish such a local law.
No neighborhood radius, physical scheduler, preparation genesis/calibration,
continuous clock or Born-law selection is derived. These are precise bridge
obligations, not an impossibility result against preparation/history records.

Verification: proofs and examples above are exact finite-dimensional algebra;
the marker proof uses degree/arm lengths and an elementary independent-set bound.
No numerical runner, new axiom, commit, push, audit mutation or platform-prompt
edit was made. The supervisor must independently check the argument before reuse.
