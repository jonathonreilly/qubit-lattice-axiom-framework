# Local instrument-to-Record-close tournament — Cycle 279

Date: 2026-07-17

Branch: `codex/bare-metal-mvp-probes-20260713`

PR: existing draft PR #5389 only

Authority: none

Audit: unset
Constitutional effect: none

## Result up front

Cycle 279 tests three distinct operational bridges on one generic parity-even
observable supported by three ordinary physical `M_2` sites:

1. coherent pointer correlation/uncompute;
2. measure-and-forget through an explicit environment, including a fine
   archive comparator; and
3. an append-only candidate fact with a supplied causal close interface.

The first route exactly instantiates a binary Cycle-189-style conditional
instrument.  Its blank pointer dilation has Kraus blocks `Q` and `P`, its
nonselective channel is `rho -> Q rho Q + P rho P`, and omission is the
identity rather than that measure-and-forget channel.  The pointer can be
uncomputed exactly.  Reusing the same pointer erases it; fresh coherent copies
give the same reduced system channel.  This is a valid finite instrument
interface, not a Record transition.

The second route gives measure-and-forget an explicit unitary environment.
The visible pointer is reset while the environment retains the coarse value;
reconnecting that environment reverses the whole process.  A separate fine
archive has the identical visible coarse pointer for two states but orthogonal
fine archives.  It destroys within-outcome coherence that the coarse Lüders
branch retains, and its channel has a nonzero normalized Choi residual from
the coarse channel.  Thus an outcome alphabet or visible pointer does not
select the post-instrument state.

The third route computes the pointer, writes a one-hot candidate fact, clears
the pointer, appends an `UNCOMPUTED` token, and permits `CLOSE` only after the
fact and uncompute token exist.  Whole-instrument deletion creates no fact and
no close; deleting a fact writer or the uncompute token blocks the affected
close.  This is a bounded Cycle-209 causal-close pattern without timeout.
However, a Cycle-259/266-style split deletion that removes the actual data
coupling while leaving the supplied `DONE` path alive writes a false `NO` fact
and closes with unit weight.  The complete candidate state also retains both
branches coherently and is exactly erased by reconnecting the inverse.

Original facts remain stable only after imposing an explicit continuation
grammar in which fact and close rails are controls, never targets.  That is a
useful append-only candidate contract.  It is also the precise permanence
import: unrestricted lawful unitary reconnection can erase the entire packet.

The retained boundary is therefore constructive and narrow:

```text
bounded coherent dilation
  + explicit outcome effects
  + containment/forgetting convention
    = conditional finite instrument;

conditional instrument
  + supplied completion ancestry
  + candidate fact rails
    = coherent causal-close candidate;

neither line alone supplies branch actuality, fault-faithful occurrence,
unrestricted permanence, a repeated clock, or frequency semantics.
```

This is not a universal impossibility result.  A physical absorbing dynamics,
verified indivisible interaction, autonomous fresh-carrier process, or global
actual-history law remains live.  There is no route-independent obstruction
and no axiom pressure.

Pointer copying is not a Record.

## Generic physical-M2 observable

The system is three ordinary two-level sites, so

\[
 \mathcal H_S=(\mathbb C^2)^{\otimes3}.
\]

Let `Pi=Z tensor Z tensor Z` be the declared parity.  Inside each four-
dimensional parity sector, the runner chooses a fixed non-diagonal orthonormal
basis.  Two vectors from each parity sector form a rank-four projector `P`;
`Q=I-P`.  The tested observable is

\[
 O=0.73P-1.17Q,
 \qquad [O,\Pi]=0.
\]

The runner verifies that `P` is projective, `O` is non-diagonal in the
occupation basis, and `O` commutes with parity.  This is a generic parity-even
bounded local observable fixture.  It is not an encoding claim, a fermionic
global compiler, a selected pointer frame, or a candidate microscopic law.

The fixed Fourier/Hadamard block bases, coefficients, and binary coarse
spectral partition are supplied test data.  Their purpose is to prevent a
computational-basis copy from masquerading as a general result.

## Route 1 — coherent pointer and exact conditional instrument

With a blank two-level pointer `A`, define

\[
 U_P=Q\otimes I_A+P\otimes X_A.
\]

Because `P,Q` are orthogonal and complete, `U_P` is Hermitian, involutive, and
unitary.  Its pointer blocks are

\[
 \langle0|U_P|0\rangle=Q,
 \qquad
 \langle1|U_P|0\rangle=P.
\]

Thus the displayed branch maps are

\[
 \mathcal I_0(\rho)=Q\rho Q,
 \qquad
 \mathcal I_1(\rho)=P\rho P.
\]

They are repeatable as projective branch maps.  Summing them gives the
nonselective measure-and-forget channel

\[
 \Delta_P(\rho)=Q\rho Q+P\rho P.
\]

Omitting the slot instead inserts the identity channel.  The runner uses a
held coherent `P/Q` superposition and obtains a nonzero identity-versus-
forgetting residual.

This route is fully coherent before a pointer restriction.  `U_P^2=I`, so
reusing the same pointer uncomputes it.  Two fresh coherent pointer factors
carry redundant coarse values but induce the same reduced system channel as
one pointer.  Neither redundancy nor reduced dephasing supplies a selected
branch.

## Route 2 — explicit environment and fine-archive discriminator

### Coarse measure-and-forget dilation

The first environment construction performs:

```text
write coarse pointer A
    -> CNOT A into blank environment E
    -> uncompute A.
```

The visible pointer returns to blank.  Tracing `E` gives exactly `Delta_P`.
The complete `S+A+E` unitary is reversible, and reconnecting `E` restores the
original input.  Reduced dephasing is therefore not evidence of fundamental
irreversibility or permanence.

### Same visible pointer, different fine archives

Let the eight rank-one projectors `R_k` refine `P,Q` in the supplied parity-
adapted basis.  A fine environment records `k` while the visible pointer
records only whether `k` lies in `P` or `Q`.  Two orthogonal vectors in the
same `P` fibre both display pointer `YES`, while their fine environments are
orthogonal.  The visible pointer density matrices are identical.

Forgetting the fine environment gives

\[
 \Delta_{\rm fine}(\rho)=\sum_{k=0}^7R_k\rho R_k.
\]

The coarse and fine channels are both trace preserving, positive,
repeatable, and idempotent, but they are not the same instrument.  On a
superposition of two vectors inside `P`, the coarse conditional branch remains
pure while the fine-archived state has purity `1/2`.  The runner reports both
the normalized Choi trace distance

\[
 \tfrac12\|J(\Delta_P)-J(\Delta_{\rm fine})\|_1
\]

and a held-density output trace distance.  These are channel diagnostics, not
occurrence probabilities.

This route intentionally relaxes exact arbitrary-data unitary evolution on
the reduced system: information enters the environment and the reduced
channel dephases.  Therefore the Cycle-266 rank-one complementary-channel
factorization theorem is respected rather than contradicted.  Its hypothesis
would apply only if the reduced target were one exact unitary channel for all
inputs.

## Route 3 — append-only candidate fact and causal close

The finite ancillary interface contains:

```text
A              coherent working pointer
DONE           supplied performed-instrument token
FACT_NO/YES    one-hot coarse candidate fact
UNCOMPUTED     supplied completion token after A is cleared
CLOSE          enabled from UNCOMPUTED and one fact
ARCHIVE_NO/YES fresh append targets
```

On a blank interface the operation order is:

```text
U_P
 -> DONE
 -> conditionally write FACT_NO or FACT_YES
 -> U_P (clear A)
 -> UNCOMPUTED
 -> CLOSE from UNCOMPUTED and the written fact.
```

The exact isometry is

\[
 V=Q\otimes|D,U,F_0,C\rangle
   +P\otimes|D,U,F_1,C\rangle.
\]

Every path to `CLOSE` has a fact and `UNCOMPUTED` in its declared circuit
ancestry.  Deleting `UNCOMPUTED` produces no close; deleting one fact writer
blocks that branch.  No timeout or silence creates `FACT_NO`.

Whole-instrument deletion also deletes `DONE`, so neither fact nor close
forms.  Under the adversarial split test, both data-pointer couplings are
deleted while `DONE` and the auxiliary schedule survive.  The pointer stays
zero, the interface writes `FACT_NO`, and `CLOSE` forms with unit weight.  The
candidate therefore certifies its supplied control grammar, not unconditional
occurrence of the physical data coupling.

For a coherent `P/Q` input, both one-hot fact branches remain in one pure
state.  The diagonal fact weights are `1/2,1/2`, but no branch has been chosen.
Applying the inverse reconnects and erases all facts and close exactly.

The append-only continuation control copies `FACT_NO/YES` to fresh archive
rails while preserving the original fact and close marginals.  This succeeds
because the allowed continuation grammar forbids the original fact and close
rails as targets.  XOR writers and their inverses remain reversible; the
restriction, fresh capacity, and continued availability of blank targets are
supplied.

## Exact Cycle-189 and Cycle-209 clause audit

| clause | instantiated here | exact status |
|---|---:|---|
| finite composition (`Q-COMP`) | yes | three system M2 factors plus finite pointer/environment/fact factors are supplied |
| blank boundary (`B0`) | yes | pointer, environments, and candidate fact rails start in declared zero states |
| context/effect family (`C`) | yes, one binary member | supplied generic even `P,Q`; no framework selection theorem |
| intervention coupling (`U`) | yes | `U_P` is an exact unitary dilation with Kraus blocks `Q,P` |
| measure pairing (`M`) | mathematical only | trace effects and Choi matrices compute conditional weights; no physical Born/frequency selection |
| identity containment (`ID`) | yes | omission is identity; performed-and-forgotten is `Delta_P` |
| instrument status | yes in route 3 | `DONE` distinguishes a performed candidate from whole omission, but is supplied and split-spoofable |
| Record decoder (`R`) | no | fact rails are coherent candidates; permanence follows only after a supplied continuation restriction |
| actual branch/repeated process (`A/T`) | no | no branch selection, trial ensemble, frequency law, or recurrence law |
| preparation interface | arbitrary mathematical input | no physical preparation law is selected |

Cycle 209's causal-close clause is instantiated only at bounded circuit
resolution: `CLOSE` depends on declared completion and fact ancestors, and
deletion never turns elapsed opportunity count into `NO`.  It fails to supply
Cycle 209's remaining Record requirements because `DONE`, loading, and
uncompute completion are not generated autonomously; the fact remains
coherent; the split fault can spoof it; and unrestricted continuation can
erase it.

Thus the exact finite quantum-instrument clauses are stronger than pointer
copying but weaker than an occurring permanent Record.

## Test and deletion ledger

The runner tests:

- projector, parity, non-diagonality, unitarity, and held-density controls;
- exact pointer Kraus blocks and trace preservation;
- identity containment versus performed-and-forgotten intervention;
- same-pointer uncompute and fresh-pointer reduced-channel equivalence;
- explicit coarse-environment dilation and complete reconnection;
- identical visible pointer with orthogonal fine archives;
- coarse/fine Choi and held-output residuals;
- coarse and fine channel repeatability/idempotence;
- within-fibre purity loss under fine archival;
- exact candidate-fact isometry and coherent two-branch retention;
- whole-instrument, split data-coupling, fact-writer, and uncompute-token
  deletions;
- unrestricted fact erasure versus restricted append-only continuation; and
- semantic firewalls and bounded disposition.

The script prints the exact Choi, held-state, archive, split-close, and
isometry residuals.  Numerical tolerance is `3e-11`.

In compact control language, the ledger includes gate deletion and explicit
erasure/reconnection tests for every route where those operations are lawful.

The retained cold-run values are:

| diagnostic | value |
|---|---:|
| identity versus measure-and-forget Frobenius residual | `0.7071067811865474` |
| coherent visible-pointer purity | `0.4999999999999999` |
| coarse/fine normalized Choi trace distance | `0.7500000000000009` |
| held coarse/fine output trace distance | `0.2709901536950477` |
| same-pointer fine-archive trace distance | `1.0000000000000002` |
| fine-archived within-fibre system purity | `0.4999999999999998` |
| route-3 candidate-fact isometry Gram error | `2.1559098391794522e-16` |
| split data-coupling false-close weight | `0.9999999999999998` |
| full candidate-fact inverse residual | `1.0729191427466821e-16` |

## Supplied-structure ledger

| supplied structure | role | not derived |
|---|---|---|
| three local M2 sites and tensor composition | system block | microscopic law or preferred state |
| parity operator and non-diagonal basis | even-observable fixture | physical parity selection or global CAR encoding |
| coefficients `0.73,-1.17` and binary `P/Q` partition | observable spectrum | physical calibration or energy |
| blank pointer/environment/fact states | dilation boundary | autonomous reset or preparation |
| controlled `U_P` | candidate intervention | selection by the framework law |
| partial trace and pointer effects | channel analysis | physical discard, readout, or branch actuality |
| fine eigenlabel archive | instrument comparator | environmental dynamics or thermodynamic arrow |
| `DONE`, `UNCOMPUTED`, and circuit order | causal-close grammar | autonomous completion facts or clock |
| fact and close rails | coherent candidate packets | framework Record formation |
| append-only continuation restriction | permanence test domain | unrestricted permanence or fresh capacity law |
| split-factor deletion | adversarial fault grammar | lawful fault of every indivisible physical update |
| mathematical branch weights | normalized finite diagnostics | Born rule, occurrence, or frequency |

No physical energy, generator rate, source, stress tensor, gravity response,
metric duration, preparation frequency, outcome selection, or actual-history
law is supplied or derived.

## All-five-lane bridge consequences

### Operational quantum / Records

Gain: a generic bounded even observable has an exact conditional pointer
instrument, two explicit environment realizations, and a causal-close
candidate with deletion tests.  Boundary: instrument, coherent fact, selected
branch, and permanent Record are four distinct interfaces.  Pointer copying
is not a Record.

### Time

Gain: `DONE -> fact -> UNCOMPUTED -> CLOSE` is an explicit causal dependency
order and no timeout creates a negative outcome.  Boundary: circuit layer,
opportunity count, and close ancestry are not metric duration, a clock tick,
clock comparison, or rate.  There is no clock law.

### Inertia / matter

Gain: the instrument acts on a generic parity-even local physical-M2
observable and the fine archive quantifies disturbance invisible to its
coarse pointer.  Boundary: no mass fixture, dispersion, recoil, post-event
packet, or inertia law follows.  Observable eigenvalues are not physical
energy by naming.

### Gravity / source

The environment and archive have explicit finite Hilbert support, but no
resource cost, action, stress tensor, source law, lapse, or gravitational
response is selected.  Copy count and archive size are not gravity sources.

### Born / probability

Finite trace weights are positive and normalized conditional diagnostics.
The unitary state retains both branches, and no occurrence map chooses one.
No Born law, repeated-trial ensemble, frequency theorem, or rate is derived.

## Fresh N1–N8 no-go discipline

The gate applies to the narrow negative boundary: none of the three displayed
finite routes, with only the tested clauses, establishes an occurring
permanent framework Record.  It does not support a universal Record no-go,
minimum-content theorem, shared substrate obstruction, or axiom claim.

### N1 — Alternative-route enumeration

| route | honesty marker | disposition |
|---|---|---|
| coherent pointer correlation and same-pointer uncompute | ATTEMPTED | exact conditional instrument; exact reversal prevents intrinsic permanence, matching [Cycle 223:138–176](./LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md) |
| fresh redundant coherent pointers | ATTEMPTED | same reduced channel and higher erasure burden, but still one reversible pure state, matching [Cycle 225:70–96](./LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md) |
| coarse measure-and-forget environment | ATTEMPTED | realizes dephasing after environment restriction; full reconnection reverses it, preserving the reduced/global distinction in [Cycle 223:160–176](./LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md) |
| fine environment archive | ATTEMPTED | distinguishes hidden poststates and produces nonzero Choi residual but selects no actual branch, directly extending [Cycle 226:21–60](./COARSE_OUTCOME_UNCOMPUTE_MASS_CYCLE226_NOTE_2026-07-17.md) |
| candidate fact plus causal close | ATTEMPTED | passes whole-deletion and ancestry tests but is split-spoofable and coherently erasable, matching [Cycle 259:55–95](./GATE_FAITHFUL_FSWAP_PHYSICAL_CLOSE_CYCLE259_NOTE_2026-07-17.md) |
| restricted append-only continuation | ATTEMPTED | preserves original facts by an explicit controls-only grammar; permanence remains conditional on that import and fresh capacity, the residual stated at [Cycle 226:129–158](./COARSE_OUTCOME_UNCOMPUTE_MASS_CYCLE226_NOTE_2026-07-17.md) |

Two further routes remain live rather than being misclassified as failed N1
attempts: absorbing autonomous dynamics could make reconnection dynamically
inaccessible, and a global actual-history functional could select one branch.
Because those routes are untested, the broad no-go fails.  The retained claim
is only the exact disposition of the six displayed ATTEMPTED constructions.

### N2 — Wall-independence audit

The collapsed open interfaces are:

- `W_I`: select/prepare the physical instrument and its environment;
- `W_L`: make the close faithful to the data interaction on a declared fault
  domain;
- `W_A`: select one actual branch/history;
- `W_R`: establish permanence and fresh append capacity under physical
  continuations;
- `W_T`: generate recurrence and metric clock/rate comparison; and
- `W_B`: connect one-shot weights to Born frequencies.

| pair | first closes second? | second closes first? | independent here? |
|---|---:|---:|---:|
| `W_I/W_L` | no | no | yes |
| `W_I/W_A` | no | no | yes |
| `W_I/W_R` | no | no | yes |
| `W_I/W_T` | no | no | yes |
| `W_I/W_B` | no | no | yes |
| `W_L/W_A` | no | no | yes |
| `W_L/W_R` | no | no | yes |
| `W_L/W_T` | no | no | yes |
| `W_L/W_B` | no | no | yes |
| `W_A/W_R` | no | no | yes |
| `W_A/W_T` | no | no | yes |
| `W_A/W_B` | no | no | yes |
| `W_R/W_T` | no | no | yes |
| `W_R/W_B` | no | no | yes |
| `W_T/W_B` | no | no | yes |

Examples fix the meaning: an exact instrument does not make its auxiliary
flag faithful; a faithful flag need not actualize; an actual branch can later
reconnect; a permanent one-shot fact supplies no clock; and normalized weights
supply neither occurrence nor frequencies.  `DONE`, facts, and `CLOSE` are
components of `W_L/W_R`, not three inflated independent walls.

### N3 — Hidden-condition scan

| phrase/condition | classification |
|---|---|
| “generic” | generic within one declared non-diagonal parity-even rank-four binary fixture; no all-observable theorem |
| “physical M2” | finite three-site matrix representation; not selection by the microscopic law |
| “measurement” | exact CP instrument after supplied effect, blank, and trace pairing; not an occurrence claim |
| “forget” | restriction/partial trace of an explicit environment; not destruction of global information |
| “fine archive” | orthogonal environment labels; not an observer, selected history, or Record |
| “DONE/UNCOMPUTED” | supplied causal tokens; not elapsed time or derived completion |
| “append-only” | controls-only continuation grammar with fresh targets; unrestricted inverse remains available outside it |
| “permanent” | tested only under that grammar; framework-wide all-continuation permanence is not claimed |
| “weight” | trace diagnostic; no Born frequency or rate |

The phrases “we assume,” “by construction,” “as is standard,” “the framework
provides,” “bridge context,” “background,” “naturally,” “obviously,”
“standard QFT,” “registered,” and “canonical” carry no hidden scientific
premise in the retained claim.  All load-bearing inputs appear in the supplied
ledger.

### N4 — Residual matching

| witness | exact residual there | Cycle-279 use | match? |
|---|---|---|---:|
| [Cycle 189:214–292, 505–523](./PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md) | conditional pointer instrument, omission/forgetting, and complete record-fibre fields are distinct; actuality/frequency open | instantiate finite `U`, Kraus, `ID`, and forgetting while keeping `R,A/T` open | yes |
| [Cycle 209:118–179](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | coherent comparison can close causally without timeout; final Record transition remains supplied | fact/uncompute ancestry and deletion-sensitive close at bounded circuit resolution | yes |
| [Cycle 223:138–176](./LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md) | coherent copies share a reduced channel; explicit dephasing differs from copying and is not a Record | one/two-pointer and explicit-environment controls | yes |
| [Cycle 224:19–89, 113–176](./STATIONARY_LOCAL_FIRST_EVENT_HISTORY_CYCLE224_NOTE_2026-07-17.md) | normalized first-event branches retain all histories and select none | branch-weight versus occurrence firewall only | yes |
| [Cycle 225:70–96](./LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md) | pointer copies and independent matter interactions are different channels | avoid counting redundant copies as independent physical evidence | yes |
| [Cycle 226:21–60, 115–158](./COARSE_OUTCOME_UNCOMPUTE_MASS_CYCLE226_NOTE_2026-07-17.md) | identical coarse labels can conceal fine archives with different poststates; uncompute ordering matters | direct fine/coarse archive and Choi comparator | yes |
| [Cycle 259:55–95, 376–394](./GATE_FAITHFUL_FSWAP_PHYSICAL_CLOSE_CYCLE259_NOTE_2026-07-17.md) | joint-control close is spoofed by a data-factor-only split deletion | exact split-fault test of candidate `DONE/fact` route | yes |
| [Cycle 266:19–69, 221–283](./UNITARY_NONDEMOLITION_OCCURRENCE_LINK_FACTORIZATION_CYCLE266_NOTE_2026-07-17.md) | exact arbitrary-data unitary reduced channel has input-independent complement | scope route 1; route 2 deliberately changes the reduced channel | yes for boundary, not a no-go witness |

No mass, compiler, gravity, or Born residual is cited as evidence that Record
formation is impossible.

### N5 — Resolution and rhetoric audit

| resolution | tested | not tested / forbidden broader wording |
|---|---|---|
| one generic three-M2 even projector | exact dilation, channels, Choi, held state | all local observables or a homogeneous lattice law |
| one pointer | exact write/uncompute | physical pointer selection or thermodynamic irreversibility |
| two fresh pointer factors | exact reduced-channel equality | spatial independence, autonomous preparation, or permanence |
| one coarse and one fine environment | exact archive distinguishability and reconnection | infinite bath, decoherence limit, or universal environment |
| one eight-rail candidate interface | exact ancestry/deletions/inverse | autonomous Record formation or arbitrary fault tolerance |
| restricted continuation family | fact controls and fresh archive targets | all lawful continuations or indefinite capacity |
| actual history / full lattice | not tested | no universal negative statement retained |

Accordingly, “pointer copying is not a Record” means that the displayed
coherent copy operation alone does not instantiate the framework's occurring
permanent Record clauses.  It does not say no pointer architecture can ever
participate in Record formation.

### N6 — Partial-closure path scan

| constructive path | what it could close | remaining audit |
|---|---|---|
| derive `U_P` and blanks from one local apparatus law | `W_I` | preparation/reset and observable selection |
| verified indivisible interaction or syndrome | `W_L` | explicit physical fault family |
| absorbing fresh-carrier export | part of `W_R` | recurrence, capacity, and all-continuation permanence |
| irreversible thermodynamic environment model | practical reconnection suppression | microscopic selection and one-history actuality |
| global actual-history process | `W_A` | localization, normalized law, and empirical selection |
| Record-triggered count plus independent comparison | part of `W_T` | metric normalization and cross-clock theorem |
| explicit repeated preparation/occurrence law | part of `W_B` | frequency convergence and testability |

These are import-retirement routes.  None is automatically a new axiom.

### N7 — Steelman

> A hostile reviewer should reject any universal boundary.  The author has
> deliberately modeled every route by a finite reversible dilation and then
> complained that its inverse exists.  A homogeneous local rule could export
> the coarse fact into a growing light cone of fresh carriers, dynamically
> forbid reconnection on the lawful sector, and make the same indivisible
> interaction generate both the data transformation and its close syndrome.
> A separate actual-history functional could select one consistent branch,
> after which the framework's already-declared permanent Record type could
> apply without a new state atom.  The exact coarse/fine instrument freedom is
> not evidence against that combined route; it merely says the complete
> instrument and continuation law must be specified.

The steelman is convincing.  The broad no-go is premature.  Cycle 279 retains
only the clause-by-clause finite boundary and queues the combined absorbing,
faithful-link route.

### N8 — Cross-cycle echo

Earlier reversible-pointer and export cycles repeatedly showed that changing
representation can retire a local copying wall while exposing preparation,
actuality, or capacity.  The conditional process cycle then closed finite
instrument composition by explicitly pricing its process fields.  The causal
detector cycle closed timeout-free comparison but left formation supplied.
The cadence and coarse/fine cycles separated copy, dephasing, fine archive,
and uncompute.  The gate-close and nondemolition cycles then exposed the
split-factor fault and indivisible-update escape.

Cycle 279 follows the same pattern: it closes the generic finite-instrument
algebra, makes the environment and close explicit, and exposes the remaining
faithfulness/actuality/permanence imports.  Similar prior walls were retired
by enlarged coherent constructions plus explicit resource ledgers, so the
same mechanism argues against axiom pressure here.

## Disposition and next tournament

Retain:

- exact generic parity-even pointer instrument;
- exact identity-versus-forgetting distinction;
- same-pointer uncompute and fresh-pointer equivalence;
- explicit coarse and fine environment dilations;
- same-visible-pointer/different-archive and Choi residual;
- repeatability and reconnection controls;
- bounded causal-close candidate and deletion ledger; and
- exact identification of the controls-only continuation restriction as the
  permanence import.

Do not claim:

- pointer copying is a Record;
- reduced dephasing is fundamental irreversibility;
- a visible outcome selects the fine instrument;
- `DONE` or `CLOSE` proves the data coupling occurred on an unrestricted fault
  domain;
- a coherent branch weight is occurrence or Born frequency;
- circuit order is physical time or rate;
- an observable coefficient is energy;
- archive size is a source or gravity law; or
- any axiom or universal obstruction.

The optimal next tournament combines rather than renames the missing pieces:
derive one indivisible local interaction whose logical data action and close
syndrome share a verified fault domain, export its coarse fact through fresh
carriers under an autonomous continuation, and separately test an explicit
actual-history rule.  Repeatability, reconnection, fine-archive disturbance,
capacity, and clock/frequency clauses must remain independent tests.

There is no occurrence law, no clock law, and no Born law in Cycle 279.  No
matrix coefficient is called physical energy, no compiler layer is called a
rate, and no environment marginal is renamed a source.
