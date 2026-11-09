# Independent check: sequential permanent records and quantum conditioning

Date: 2026-11-09. Completed independent proof check; no audit or retained status.

## Scope and provenance

Requested profile: `gpt-6-astra`, reasoning effort `max`, fresh restricted-input
context (`fork_turns=none`), as reported by the supervisor. No backend model or
effort attestation is available to this worker. This is a same-family check,
not a cross-family audit. The supervisor's new outcome-conditioning candidate
and other checker reports are excluded from the input.

Pinned main: `bf92a1d763030836ed55631d5d7a7ef3b288f284`.
Research parent supplied by the supervisor:
`8e0c276b60c16c745456f6f1036c5f7dc5eacd66`.
Checker checkout HEAD at entry: `f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
All scientific source from main is read by `git show` at the pin; the checkout
is not reset or updated. Existing untracked work is preserved.

The task is to decide, on a finite declared preparation and protocol, whether
permanent outcome records can follow a sequential quantum law without a local
instrument taking the opposite detector setting as input; determine the exact
conditioning and state-sufficiency premises; and propose precise clause edits
without adopting them. It is not a derivation of quantum physics from the
four current axioms or a physical mechanism for unique outcome selection.

Current-main workflow, workhorse, freshness and negative-claim instructions
were read. The installed workhorse copy differs, so its old model-profile
language is not used. `scripts/lab_ops.py` matches the pinned main bytes.
Worker preflight with `--role checker --model gpt-6-astra --effort max` returned
`preflight: go`: 111 GB free disk, 35% free memory, load 6.2, `nice` works,
origin reachable. No target was supplied, so no target model floor was checked;
the memory-cap probe was unavailable. No numeric job is run.

## 1. Results and premise table

There is a finite sequential, append-only record law with quantum Bell
probabilities and a representation by tensor-local quantum instruments. Each
instrument uses its own setting. Its second full-record conditional probability
depends on the first distant setting and outcome. Thus it refutes the proposed
identification of quantum operational locality with neighborhood sufficiency of
full-record conditional odds. It does not refute no-signalling.

A quantum predictor need not be an independently variable extra state on a
fixed, completely recorded preparation/protocol domain: it can be reconstructed
from the records. This claim fails for arbitrary preparations or unrecorded
operation order. A law assigning a density operator to a preparation tag is a
physical calibration premise, not a consequence of the tag's existence.

| ID | Premise | Role and status |
|---|---|---|
| R | Finite record configurations, fresh output sites, one fixed content readout, no overwriting | Retains the current Record requirements on the constructed domain |
| Q | Finite tensor quantum algebra, positive trace-one preparation, completely positive branch maps with trace-preserving sum | Supplied quantum probability/process structure; not derived from one-site `M_2(C)` |
| P | A recorded preparation code has a fixed, calibrated density operator; all causally relevant controls and their order are fixed by the recorded protocol | Supplies record sufficiency; counterexamples below test its necessity |
| LQ | Alice's operation acts on Alice's factor and uses only her setting; Bob's analogous operation acts on Bob's factor; no later control depends on a remote result | Quantum operational locality; distinct from classical factorization |
| S | Source is singlet, local binary projectors are `(I+aN)/2` for Hermitian traceless `N^2=I` | Specific Bell resource and measurement bridge, supplied rather than fitted |
| C | Settings are chosen independently of source/non-setting inputs, all four pairs occur, all trials retained | Needed to compare with the classical Bell bound; initial independent setting records are supplied below |
| Ffull | Conditional on the entire current record and on the next formation, each output distribution equals one function of its local record neighborhood | An additional precise reading of present Admissibility, tested and refuted for the sequential singlet target |
| A | One branch is actually realized, with probabilities given by the process law | A stochastic realization/registration postulate; CP maps alone do not select one actual branch |

These are implication premises, not a list of independent open walls. The
finite model supplies Q, P, LQ, S and C as conditions, satisfies R, and is
incompatible with Ffull. An amendment that keeps only locally conditioned
odds, without Q, does not select quantum physics.

## 2. A finite instrument tree gives an append-only stochastic law

Use a finite-dimensional Hilbert space and a finite rooted protocol tree. For
each history `h` and allowed next outcome `o`, specify matrices `M_(h,o,k)` with

```text
Phi_(h,o)(X) = sum_k M_(h,o,k) X M_(h,o,k)^dagger,
sum_(o,k) M_(h,o,k)^dagger M_(h,o,k) = I.
```

The maps may include initialized finite ancillas and fixed dimensions enlarged
in advance. This formula proves complete positivity directly: on any passive
reference, each term is conjugation by `M tensor I`. The second equation proves
trace preservation after summing outcomes. Locality is a separate support and
control constraint on the matrices, not a consequence of this normalization.

Supply `rho_0 >= 0`, `Tr rho_0=1`. Put `sigma_empty=rho_0` and recursively set
`sigma_ho=Phi_(h,o)(sigma_h)`. Define `w(h)=Tr sigma_h`. Positivity gives
`w(h)>=0`, and the completeness identity gives

```text
sum_o w(ho) = w(h).
```

Induction therefore gives a normalized probability measure on terminal
histories, with the displayed `w(h)` as every prefix probability. If `w(h)>0`,

```text
rho_h = sigma_h / w(h),
p(o | h) = Tr Phi_(h,o)(rho_h).
```

If `w(h)=0`, positivity and zero trace imply `sigma_h=0`; all descendants have
zero weight. Conditional probabilities there are not fixed by the law. Exclude
these states from the reachable domain or prescribe a harmless refusal rule;
never divide by zero and never claim a zero-weight outcome is realized.

Now encode the preparation and protocol in supplied records. Each transition
appends one outcome code at a fresh site. Require that the record map `R_h`
determines the protocol state and its relevant branch maps. One sufficient
condition is that `h -> R_h` is injective, with event identity and order
recoverable from recorded metadata and occupied output locations. Then

```text
K(R_h, R_ho) = Tr Phi_(h,o)(rho_h)
```

is a single time-homogeneous Markov kernel on these record maps. Terminal
states are absorbing. There is no extra hidden clock: the next protocol step
is reconstructed from `R_h`. Only blank sites are written, and old contents
are unchanged. Any finite alphabet can be injectively coded by distinct
scalar matrices in `M_2(C)` with a fixed dictionary. This is a mathematical
coding statement, not a finite-precision or preparation-genesis assertion.

The quantum predictor is the derived function `rho(R_h)=rho_h`. Introducing
it into a calculation does not by itself add an independently variable state
coordinate. Conversely this construction says nothing about whether such a
function has a neighborhood-local evaluation or a local classical physical
realization. A centralized sampler can implement any such kernel; that fact
is not a claim about detectors.

### The exact sufficiency criterion, and two failures

Let the allowed preparations, histories and future tests be fixed. A
record-only predictor for all future tests exists precisely when two histories
with the same `R` give the same future record law for every allowed continuation.
Necessity follows because a function takes one value on one input. Sufficiency
follows by choosing any representative of each record equivalence class; the
future law is independent of that choice. Consistency of the future laws gives
the corresponding sequential conditional kernels wherever the conditioning
event has positive probability. When protocol parsing is itself a function of
`R`, injectivity of `h -> R_h` is sufficient but not necessary.

For a fixed quantum future effect family `E`, the criterion is
`Tr[(rho_h-rho_h')E]=0` for every accessible future effect. If every effect on
the same finite algebra is accessible, this is equivalent to `rho_h=rho_h'`:
when their Hermitian difference `D` is nonzero, its positive or negative
spectral projector has nonzero trace pairing with `D`. For a restricted test
family only predictive equivalence is required; full matrix equality would be
an unnecessarily strong demand.

**Preparation collision.** Let the same source-tag record be used for both
`Phi_+=(|00>+|11>)/sqrt2` and `Phi_-=(|00>-|11>)/sqrt2`, with no other record
distinguishing the preparations. Both reduced states are `I/2`. A local X
measurement on each wing has correlation `+1` in the first case and `-1` in
the second: `X tensor X` fixes `Phi_+` and negates `Phi_-`. In particular the
`++` probability is `1/2` versus `0`. No unique predictor from that same
record map reproduces both preparation-conditioned laws. Local tomography of
the separate reduced states cannot repair this collision. One can instead
record which calibrated preparation occurred, supply a fixed mixture, or
enlarge the causal prestate. None is forced by record permanence alone.

**Order collision.** Start one qubit at `I/2`. In one history measure Z with
outcome `+`, then X with outcome `+`; reverse the measurements in the other
history. Each two-outcome history has probability `1/4`. If the final records
say only `Z=+` and `X=+` at fixed sites, with no order metadata or fixed
scheduler, the record configurations coincide. Their final states are
respectively `|+><+|` and `|0><0|`. A next Z result is `+` with probability
`1/2` versus `1`. Permanent records do not automatically encode birth order.
Fixed order, explicit order records, or a proof that the branch maps commute
repairs this example. The Bell wing maps below commute, so their relative
ordering need not be stored to reconstruct the state after both events.

An effect alone also does not identify an instrument. The maps
`Phi_+(X)=P_+ X P_+` and `Psi_+(X)=Tr(P_+ X)|1><1|` have the same plus-outcome
effect `P_+=|0><0|`, but yield opposite deterministic Z predictions on their
post-plus states. Here `Psi_+(X)=|1><0|X|0><1|`; completing the other outcome
in the same way makes a trace-preserving sum. Calibration must identify the
update map as well as the outcome effect.

## 3. Local instruments, conditioning and no-signalling

Take `H_A tensor H_B` and a positive trace-one `rho`. Let Alice's branch
operators be `A_(a,k)^x tensor I`, and Bob's be `I tensor B_(b,l)^y`, with
complete sums of adjoint-products at each wing. Direct multiplication shows
that every Alice branch map commutes with every Bob branch map. Thus

```text
p(a,b | x,y) = Tr[(Phi_a^x tensor Psi_b^y)(rho)]
```

is independent of the bookkeeping order. Bob's instrument parameter is `y`,
not `x` or `a`. For any Alice effect `E`, the expectation after Bob's ignored
operation is

```text
sum_(b,l) Tr[rho (E tensor (B_(b,l)^y)^dagger B_(b,l)^y)]
  = Tr[rho (E tensor I)].
```

This proves no signalling from arbitrary trace-preserving Bob operations to
Alice, including in the presence of a passive reference. It proves the other
direction by exchange of wings. Trace preservation is essential: retaining
only a selected remote outcome changes the conditional ensemble and needs a
selection record to identify that subensemble.

Let `F` denote the complete realized-history sigma-algebra immediately before
Bob's formation, and `G_B` the information available at Bob, with no Alice
setting/outcome record. Distinct
conditioning operations are related by ordinary conditional expectation:

```text
P(b | G_B) = E[ P(b | F) | G_B ].
```

The actual local instrument must be fixed on each `G_B` information cell for
this to be one experimental choice. Quantum probabilities on the right may
vary between full histories in that cell. Averaging yields Bob's local law.
In a general protocol, `G_B` contains accessible preparation and control
history; it need not be identical to the six instantaneous neighbor records.
Identifying these two information sets is another locality/sufficiency
assumption. The axiom that only records are readable does not itself say which
remote records are accessible to which detector. Our finite example below
supplies local access and makes the relevant local history visible in the local
prepared metadata.

For the singlet, set `P_a(N)=(I+aN)/2`, with `N` Hermitian, traceless and
`N^2=I`, and similarly `P_b(M)`. Write `c=Tr(NM)/2`. The singlet density is
`rho_s=(I tensor I - sum_i sigma_i tensor sigma_i)/4`. This equality follows
by applying the Pauli sum to the antisymmetric vector (eigenvalue `-3`) and
the three-dimensional symmetric subspace (eigenvalue `+1`). The Pauli trace
identities `Tr sigma_i=0`, `Tr sigma_i sigma_j=2 delta_ij` give

```text
p(a,b | N,M) = (1-ab c)/4,
p(a | N,M) = p(b | N,M) = 1/2,
p(b | a,N,M) = (1-ab c)/2.
```

Equivalently, after Alice's record, Bob's full-history conditional state is
`(I-aN)/2`. Before Alice's outcome is locally available, averaging the two
equiprobable states returns `I/2`. This algebra is a change in conditional
description. It establishes no directed physical influence from Alice's
chosen setting to Bob's locally observable statistics.

For `N=M=Z`, the two positive Alice branches require opposite deterministic
Bob outputs, while Bob's record neighborhood can be identical. Therefore
Ffull fails. Choosing `c=1/sqrt2` yields two unequal probabilities strictly
between zero and one, so the failure does not depend on excluding zero-weight
branches. No choice of a single function of that unchanged neighborhood
equals both full-record conditionals. This conclusion is about the declared
sequential experiment with Bob forming on both Alice branches and no
selection; it is not a statement about all record theories.

## 4. A literal finite sequential record instance

This section turns the history theorem into one concrete finite record model.
It is compatible with the proposed instrument/local-information reading in
section 7, not with Ffull. It is not a microscopic record-selection mechanism.

Take centers `c_A=0` and `c_B=L e_3`, `L>=6`. At each center `c`, prepare
three paired arms:

```text
c+e_1, c+2e_1 : 100I for A, 101I for B;
c+e_2, c+2e_2 : X(N)=2I+N for A, X(M)=2I+M for B;
c+e_3, c+2e_3 : 200I.
```

The two `200I` arm pairs carry the calibrated common singlet preparation code.
The centers are blank output sites. In the quantum operational
representation use data-qubit factors at `c_A-e_1` and `c_B-e_1`; they carry
no readable records. The fixed preparation dictionary assigns their singlet
state. The initial model thus has twelve records; exactly two more are formed.
The operational representation additionally uses two unrecorded data factors.
Record counts and quantum register counts are different resources.

Each center is intrinsic: it is the unique site adjacent to one record from
each of its three differently tagged arm pairs. Indeed a common neighbor of
`r_i e_i` and `r_j e_j`, with `r_i,r_j in {1,2}`, requires
`r_i+r_j<=2`, hence both are 1. The only common neighbor of `e_1,e_2,e_3`
is 0. The wing tags identify A and B. Include every translated and proper
cubic rotation of these patches in the domain. This supplies no preferred
lattice origin or external step counter. No record in one patch is adjacent to
a record in the other for `L>=6`.

Choose the two ideal directions at each wing for CHSH. Initially sample the
two setting records independently with probability `1/2` each, independently
of the fixed preparation. This is a supplied distribution over the four
prepared maps, not a derivation of setting-source genesis. One universal
projector formula governs these and any other declared ideal directions.

The sequential kernel is:

1. On a prepared map with both outputs absent, append `aI` at A with
   probability `1/2`.
2. On a map with A output `aI` and B blank, append `bI` at B with probability
   `(1-ab Tr(NM)/2)/2`.
3. With both outputs present, remain at the same record map.

Only positive-probability prefixes belong to the reached domain. The local
instrument implementing the probabilities in the supplied quantum model is
the corresponding projective branch at the adjacent data qubit, with
registration at its own output site. It depends on its own arm matrix only.
Appending the label is an extra physical registration condition: `+/-I` are
record labels, not claims that a density matrix equals `-I`. Likewise the
metadata codes are not identified with mutually orthogonal states of a
two-dimensional quantum memory. No physical one-qubit storage implementation
of that entire symbolic alphabet or resource optimum is proved here.

The record map determines the stage, settings, source code and actual past
outcome. Section 2 therefore gives `rho(R)` uniquely on this domain. At the
initial state it is `rho_s`; after one output it is the normalized branch of
the corresponding local projector; after both it is the normalized double
branch. The branch maps commute, so the final predictor and law agree if the
bookkeeping order is reversed. This proves consistency of these two orders,
not spacetime covariance or a physical time law.

For a total local-information kernel, whenever a neighborhood contains one
wing tag, the `200I` tag and exactly one valid `X(N)`, use the uniform measure
on `+/-I`. At all other nonempty neighborhoods use the empirical measure of
their recorded contents, with multiplicity; at an empty neighborhood use
`delta_0`. The validity predicate is `N=N^dagger`, `Tr N=0`, `N^2=I`.
This defines a normalized, nonconstant, covariant Borel kernel on all record
neighborhoods. Every old metadata record retains a same-content neighbor;
none of its own neighborhoods contains all three special tags. Every new
output retains the uniform local-information support. Thus one-record
uniqueness, permanence, fixed content readout, and continued support all hold.
The fixed readout is `aI -> a` at the output alphabet and fixed metadata labels
otherwise. Only actual records are read.

This uniform local-information kernel is deliberately not the second
full-record transition row. A global sampler evaluates that row using the
whole record; its computation is not a local classical detector mechanism.
The occupancy-derived schedule is a formal way to serialize the two events;
it supplies no physical nonlocal clock, propagation speed, or site-formation
rate. Preset local measurement times in the quantum operational model require
no remote setting message, but their realization is supplied. This separates
the stochastic law, the quantum operational representation, and an unproved
microscopic outcome-selection dynamics.

## 5. Two meanings of “without passing settings”

Under LQ, no remote setting is an input to a local quantum instrument. The
trace calculation above proves an operational statement for arbitrary local
quantum tests, not just for one displayed marginal. It does not prove a
classical causal factorization of the actual outcomes.

For the latter, suppose every local record update is a classical causal
operation, all relevant noise and common causes can be included in `lambda`,
`lambda` is independent of the freely selected setting pair, and no setting
has a causal path to the opposite outcome. Include scheduler and selection
variables in this accounting. Then after recursively substituting the local
updates, the outcomes have the forms `a=f_x(lambda)`, `b=g_y(lambda)`.
Stochastic responses can be included by pre-sampling their setting-independent
noise in `lambda`; equivalently use conditional means `A_x,B_y in [-1,1]`.
For each `lambda`,

```text
|A_0(B_0+B_1)+A_1(B_0-B_1)|
 <= |B_0+B_1|+|B_0-B_1|
 = 2 max(|B_0|,|B_1|) <= 2.
```

Integration gives CHSH `<=2`. Pre-choice neighborhood propagation and shared
randomness are already included; they do not change this implication. This
is the classical causal family tested, not every law on permanent records.
An observer's inability to read a remote result does not establish these
factorization hypotheses.

There is also a concrete trap in the phrase “only outcomes are propagated.”
Let bits `x,y` be independent settings and `r` a shared independent fair bit.
Alice forms outcome `a=r XOR x` and sends only that outcome bit along a
record-copy path. Bob knows `r`, so he obtains `x=a XOR r` and forms

```text
b = a XOR ((a XOR r) AND y).
```

Then `a XOR b = x AND y`, attaining the PR parity and CHSH 4. Both final
output marginals are uniform: for `y=0`, `b=a=r XOR x`; for `y=1`, `b=r`.
No message field was named “setting,” but the pair `(r,a)` reveals it
perfectly. The physical path `x -> a -> b` violates the causal separation
premise. Bob can read `r` and the relayed `a`, so the complete accessible
protocol is a signalling channel even though its designated final output
marginals conceal it. Nearest-neighbor copies do not remove this issue.

Quantum singlet conditioning is different: without Alice's classical record,
Bob's entire local quantum state remains `I/2` for every setting she chooses.
The conditional state is not a readable copy of her outcome, and the
nonorthogonal ensemble decompositions of `I/2` do not provide such a copy.
No chosen relay of her record is part of the LQ process.

### The quantum cap uses the quantum premise

An independent bound proof avoids the primary note's squared-CHSH-operator
route. Purify any finite density `rho` using its spectral decomposition.
For Hermitian local contractions `A_x,B_y`, set

```text
u_x=(A_x tensor I)|psi>,  v_y=(I tensor B_y)|psi>.
```

Their norms are at most one, and the real correlation equals
`Re <u_x,v_y>`. Cauchy-Schwarz and the parallelogram identity give

```text
|S_signed| <= ||v_0+v_1|| + ||v_0-v_1||
 <= sqrt(2(||v_0+v_1||^2+||v_0-v_1||^2))
 = 2 sqrt(||v_0||^2+||v_1||^2) <= 2 sqrt2.
```

Binary POVMs yield contractions by taking the difference of their two effects,
so this covers them without a dichotomic dilation. For the singlet choose
`N_0=Z`, `N_1=X`, `M_0=(Z+X)/sqrt2`, `M_1=(Z-X)/sqrt2`. The four correlations
are `(-1,-1,-1,+1)/sqrt2`, giving absolute CHSH `2sqrt2`. This is an exact
consequence of supplied Q and S. The maximizing settings and target quantum
value were known in advance; there is no empirical or blind prediction here.

Replacing Ffull solely by locally accessible conditional odds is insufficient
to obtain this cap. The abstract PR law
`p(a,b|x,y)=1/2` when `a XOR b=x AND y`, zero otherwise, has uniform local
conditional odds and can be serialized by a global full-history rule. It
uses exactly one permanent outcome at each wing. It cannot be implemented by
the local quantum instruments just analyzed, because 4 exceeds their proved
bound. This is a positive counterexample to the weaker proposed selection
principle, not a spacelike physical realization of the PR law.

## 6. Probability law and actual outcome selection

For any instrument the record-append channel

```text
rho -> sum_o Phi_o(rho) tensor |o><o|
```

is normalized and completely positive. In an ensemble description it assigns
weights to records. A unitary pointer implementation instead maps a vector to
`sum_o M_o|psi> tensor |o>` (with extra Kraus labels if required). If two
branch amplitudes are nonzero, this remains a superposition of two orthogonal
pointer components. Tracing an environment can remove visible off-diagonal
terms, but that operation itself does not choose one actual `o`.

A physical theory can take primitive stochastic actualization as its selection
account: at a formation event one branch is realized with the instrument's
probability, and its record is appended permanently. That is a meaningful
additional postulate, not a deduction from CP normalization, decoherence, or
the statement “records form.” With this postulate and a supplied occurrence
schedule, section 2 is a complete finite stochastic trajectory model. It
does not derive the occurrence schedule or explain a particular realized draw
by a further deterministic mechanism. Conversely, failure to derive such a
mechanism is not a mathematical inconsistency of a stochastic theory.

The current axioms already name record occurrence and unique recorded
outcomes; they do not identify their probabilities with quantum instrument
weights. An approved quantum-stochastic formation clause would make that
identification explicit. Calling the conditional density an ontic collapse
field, or claiming the proof discovers a collapse mechanism, adds a different
physical assertion not proved here.

## 7. Exact clause surfaces and proposed wording

The supplied authority is the pinned
`docs/MINIMAL_AXIOMS_2026-06-29.md`. No source file or premise registry is
edited. The owner has authorized considering an axiom revision; this worker
proposes text for review rather than adopting it.

| Current surface | What the proof requires |
|---|---|
| Qubit, lines 43 onward: one-site `M_2(C)` | Retain; add tensor composite and positive-state probability structure if the foundation is intended to select finite quantum physics |
| Admissibility, lines 60-61: neighborhood determines the distribution | Replace or explicitly qualify the conditioning if Ffull is intended; the sequential counterexample rules out Ffull for this quantum target |
| Record, lines 75 onward: one supported permanent record, content-only readout | Retain; identify quantum outcome labels with record contents and state stochastic actualization explicitly if it is to be a foundation premise |
| Qualification, line 92: state is a record configuration | Can remain on a record-sufficient preparation/protocol domain; cannot represent different future-relevant preparations at one identical complete record state under one record-only kernel |
| Non-dynamics paragraph, lines 116 onward, and open-gate list, lines 181 onward | Must be synchronized with any adopted Born/instrument clause; they currently explicitly leave Born values and update rules outside the axioms |

**Proposed finite quantum composition/probability clause.**

> For each finite set of sites, the quantum probability algebra is the tensor
> product of its one-site algebras, with consistent embeddings under inclusion.
> Preparation and record history carry a normalized positive state on these
> algebras. Probabilities of effects are its positive linear evaluation, and
> local experimental operations are represented by completely positive maps.

This is a genuine supplied quantum restriction. It is not inferred from
one-site `M_2(C)`, covariance, locality of recorded marginals, or the available
record alphabet. Finite-region consistency is stated to avoid assigning
unrelated probability states to overlapping regions. Only finite models are
proved here; no infinite-lattice dynamics is constructed.
On each finite full matrix algebra the trace pairing represents the functional
by a unique Hermitian `rho`; positivity on `|v><v|` gives `rho>=0`, and
evaluation on the identity gives `Tr rho=1`. Thus the stated positive linear
rule supplies the density/trace form used above. Interpreting all symbolic
record codes as quantum states of those same site factors would require a
separate representation and is not asserted by the record-count construction.

**Proposed replacement for the distribution sentence in Admissibility.**

> At a forming site, its neighborhood records determine the local formation
> instrument and its recorded controls. On a finite outcome menu, an instrument
> is a family of completely
> positive branch maps on a specified neighborhood algebra whose sum preserves
> normalization. Conditional on the complete preparation and realized record
> history, an outcome has probability equal to the normalization of its branch
> output; the conditional quantum state after that outcome is the normalized
> branch output. Instruments in disjoint regions act on their own factors and
> commute, and neither instrument takes the other region's setting as input.

Here “local” constrains the map and its controls. It does not assert that
conditioning on a remote outcome leaves every full-history probability
unchanged. This is a substantive amendment to Ffull, not merely a relabeling
of the same conditional kernel. A statement only about local observed
marginals would be weaker and admit the PR counterexample.

**Proposed stochastic realization addition to Record.**

> For a finite outcome menu, at each formation event exactly one supported instrument outcome is
> realized according to these probabilities and is registered permanently
> as the record's content. A fixed dictionary encodes outcome labels into
> contents; readout depends on content alone. Subsequent operations preserve
> all prior records.

This does not authorize later contextual reinterpretation of an unchanged
content. Site choice and physical rate are not selected by this wording.
These two clauses give the exact finite-menu meaning tested here. The current
axiom also permits continuous record contents. A universal amendment must
preserve that domain using a measurable instrument (a countably additive
CP-map measure with trace-preserving total map) and outcome probabilities
`mu(E)=Tr I(E)(rho)` for measurable sets `E`. Conditional states are then
specified almost everywhere by disintegration, not by dividing a zero
singleton probability. That extension is identified but not proved by this
finite-tree check; finite-site Hilbert dimension does not imply a finite
outcome menu. Do not copy the finite-menu restriction into a universal axiom
without explicitly deciding its scope.

There are two distinct state clauses, depending on the intended admitted
preparation family. They must not be silently mixed:

**Proposed record-sufficient qualification (sufficient for this finite model).**

> A state is a configuration of permanent records. On each declared
> preparation/protocol domain, the law and records determine a unique
> quantum probability state up to equivalence on all allowed future tests.
> Histories giving the same record configuration must give the same future
> record laws. The quantum probability state is a derived predictor, not an
> independently variable state coordinate.

The initial calibrated preparation map and the operation dictionary are part
of the law's supplied domain. A different name for a source tag does not
establish this sufficiency; section 2 gives both the criterion and explicit
violations. The global initial preparation could be fixed as law data or
encoded in records. Neither option proves preparation genesis.

**Alternative proposed prestate qualification (for independently variable
unrecorded preparations).**

> A readable state is a configuration of permanent records. The complete
> causal specification may additionally include a consistent positive
> quantum probability state not determined by those records. Only record
> content is readable; local formation uses the stated quantum instruments.

If identical records are required to coexist with both `Phi_+` and `Phi_-`
preparations, some distinguishing law condition or state datum is necessary.
This is one repair. It does not make the live-state option necessary for the
record-sufficient family, and by itself it does not repair Ffull. A remotely
conditioned density restriction can change while the local recorded
neighborhood does not. Both the state interpretation and the probability
conditioning must therefore be made explicit.

## 8. Prior-work search and independence record

The five named science sources were read at their recorded identities. The
current-main ontology-fork note was read in three bounded chunks through its
end. Its Block86 numerical claims are not reused as verified computational
evidence; its exact same-record/different-law logic was checked and is tested
here with different, elementary phase and noncommuting-order witnesses.
The joint-record note's atomic construction remains a distinct positive
route; its quantum-instrument implementation cannot establish Ffull.

A targeted pinned-repo filename search for record sufficiency and quantum
instruments found the supplied ontology-fork note and other existing
conditional measurement/history notes. No extra science files or ledgers were
opened. The selected detailed comparison is the supplied ontology-fork note,
whose routes A-D already preserve preparation-record and history-law escapes.
Open-PR search `"record" "quantum"` in the repository returned
[PR 10142](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10142)
and [PR 10139](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10139).
The search tool initially returned long bodies including summaries of earlier
campaign checks; these were not used as proof inputs. No new outcome-conditioning
candidate or checker report was opened. Search is bounded and does not certify
absence of all overlapping work.

The literature search located John Watrous's
[*The Theory of Quantum Information*, section 2.3.2, equations 2.258-2.262](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).
It gives finite CP instruments, normalized branch conditioning, and a
classical-output channel. Watrous credits the instrument tradition to
E. B. Davies and J. T. Lewis. The requested Davies-Lewis primary page was
inaccessible, so no claim depends on that paper's unread proof. The finite
Kraus positivity, prefix consistency, trace-preserving no-signalling and
record-sufficiency steps used here are proved above rather than accepted
from the citation. There is no novelty claim for the instrument formalism
or the Bell bounds.

The distinct checks are: a normalized instrument-tree proof; an elementary
future-effect criterion for record sufficiency; exact phase/order/instrument
counterexamples; a local-outcome-relay information counterexample; and the
vector/parallelogram quantum bound rather than the primary note's squared
operator argument. Shared source premises and model family still limit
independence. No numerical checker, mutation script, formal prover, physical
experiment or backend attestation is claimed.

## 9. Negative-claim discipline and limits

This is a bounded pure-proof research check. It contains explicit
counterexamples, not a framework-wide no-go or a ready-to-land audit packet.

| Check | Answer |
|---|---|
| N1: alternative routes | Four substantive mechanisms are considered: full-record neighborhood kernels (collision), classical causal local mechanisms (Bell bound), tensor-local quantum instruments (positive construction), and calibrated record/history reconstruction (positive criterion plus failures). Atomic joint formation in the supplied source is a further target-changing escape, not a sequential attack closed here. No five-family negative-packet PASS is claimed. |
| N2: wall independence | No count of independent physical walls is asserted. Composition, calibration, actualization and occurrence are conditions of distinct implications; reconstructing the predictor does not repair Ffull, as the positive finite model explicitly demonstrates. |
| N3: hidden conditions | The premise table and construction explicitly supply preparation, complete instruments, control order, independent settings, registration, and occurrence schedule. The quantum data factors are a conditional operational representation, not silently extra record state variables. |
| N4: residual matching | The ontology-fork comparison concerns identical records with distinct required future laws, matching the phase/order witnesses; its numerical Block86 claims are not imported. The joint-record comparison concerns Ffull at an unchanged remote neighborhood, exactly the sequential collision here. The foundational Bell comparison concerns complete classical causal factorization, not merely no-signalling. |
| N5: resolution | Proofs cover finite-dimensional instruments, finite record histories, and the explicit two-wing lattice patch. No infinite-volume process, arbitrary physical light cone, continuum field, or all-ontology impossibility is tested or claimed. |
| N6: partial closure | Recorded calibration and order reconstruct a predictor without an independent live-state variable; the main source already preserves these escapes. A quantum composition/instrument clause is proposed because it selects a probability/process class, not because a naming convention is mistaken for missing physics. No primitive-registry absence claim is made. |
| N7: steelman | The strongest challenge to a “records cannot give Bell” claim is exactly the constructed record-sufficient quantum law: full histories determine nonfactorizing joint probabilities while local instruments use local settings. It defeats that broad claim. To defeat the narrow Ffull collision while retaining its premises one must make a single function take two unequal values on the identical local input, which the explicit positive-branch witness excludes. Relaxing Ffull is an honest scope change. |
| N8: cross-cycle echo | The fully read current-main ontology-fork note already warns against inferring that a causal-prestate amendment is compulsory. Its preparation-record and law-history repairs are applied here. Search of the named sources and the bounded filename results is not an exhaustive audit of old campaigns. |

The promised output is one proof note. No source, prompt, registry, audit
status or platform instruction has been changed. No formal negative-packet
PASS, retention, local hidden-variable realization, physical collapse account,
preparation genesis, repeated-trial resource construction, relativistic
covariance, or selected event rate follows from these finite arguments.

## 10. Source identities and final verification

The source hashes below are SHA-256. Main-source bytes come from the pinned
commit. Primary working sources were rehashed after drafting and remained
unchanged. The science read set contains exactly the five supplied files.

| Source | SHA-256 |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` at pinned main | `301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc` |
| `docs/LIVE_M2_RECORD_SUFFICIENT_JOINT_LAW_STATE_ONTOLOGY_FORK_BOUNDED_THEOREM_NOTE_2026-08-14.md` at pinned main | `a0dc4fe907360e00a6d9ceb5e392066d4b09f0c3d751163010b4122244dd7199` |
| Primary `joint_record_law/RESULT.md` | `d11abd8953071b60f674c87a16c095a01478344f34b363c07a9f944b51ebd6a3` |
| Primary `joint_record_law/ASSUMPTIONS.md` | `83b5b28fc7063912a11040ace091658d71c63fbe17d58905396374b5f7c5bba8` |
| Primary `foundational_bell/RESULT.md` | `b408820a8e38f969a21f70d6d8a53c05172cddfc52dfeba2f74ecb9c964ee321` |
| Pinned `docs/ai_methodology/SCIENCE_WORKFLOW.md` | `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca` |
| Pinned `docs/ai_methodology/skills/workhorse/SKILL.md` | `e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8` |
| Pinned `docs/ai_methodology/skills/no-go-discipline/SKILL.md` | `9020ba5c2797d8f026ddb72871b13f18a18cad4e0ec326c0f4653ceb438751bc` |
| Pinned and local `scripts/lab_ops.py` | `462b66455683bf6bb11bf1dd451e789ed4a298b6cf06c9109d693cc6ea1e1fd9` |

The three primary working files are under
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/`.
The worker wrote only this file in the corresponding checker worktree.
The full proof note was read back; the final wording fixes explicitly the
pre-B conditioning sigma-algebra, local-access premise, content/readout
dictionary, separate symbolic-record versus quantum-storage resources, and
finite-menu scope. Source hashes and the unchanged checkout HEAD were checked.
No computation beyond read-only provenance/bookkeeping and worker preflight
was run. These checks establish what was examined, not an audit verdict.

Current recovery point: the finite conditional construction and exact
counterexamples are complete. The next decisions are the scope of an approved
quantum probability/instrument clause, record-sufficient versus independently
variable preparation domains, measurable-outcome extension, and any physical
actualization/occurrence model. None has been silently selected by this proof.
