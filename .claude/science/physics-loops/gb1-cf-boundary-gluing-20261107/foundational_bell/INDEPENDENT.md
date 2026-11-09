# Independent check: four lattice axioms and a binary CHSH record observable

**Work state:** FROZEN original-source independent check; no supervisor
foundational-test argument was read before this version was completed.
**Claim class:** independent mathematical source/assumption check, not an audit,
retained-status change, law-selection argument, or empirical prediction.
**Date:** 2026-11-09. **Checker:** host subagent, same-family/fresh restricted
context, strongest configured model and maximum reasoning effort as specified
in the handoff; the runtime identity/effort were not separately exposed to this
checker. No cross-family independence is claimed.

## Scope and source identity

The exact question is what the four current lattice axioms constrain about
two binary setting Records and two binary outcome Records, with
`S = E00 + E01 + E10 - E11` and `Est = E[AB | s,t]`. The check must distinguish
mathematical record constructions, a selected physical law, and spacelike
experimental implementations. Existing Bell/CHSH/Tsirelson algebra is prior art.

Source checkout: `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics`.
Frozen source revision: `c50d82b2d2e01e4622a037c8f7eafb2abb24e57d`.
Referenced main revision: `1e0d3b58dcda7f83152b0bb51729260247454d65`.
The first three scientific sources below are byte-identical at those two
revisions. The autonomous-runtime result exists on the frozen source branch.
All source reads use `git show` at the frozen revision; no moving worktree
content is evidence.

| Label | Exact source | Git blob | SHA-256 |
|---|---|---|---|
| A | `docs/MINIMAL_AXIOMS_2026-06-29.md` | `c740addc83df1a87798ad1826f2984e98b9d5117` | `301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc` |
| P | `docs/PROJECTIVE_HISTORY_FIXED_FIRST_TARGET_LOCAL_PROGRAM_BOUNDED_THEOREM_NOTE_2026-09-13.md` | `813906f2fa9b6e45796676d5eced3ac80baeea7d` | `df478a982ec95b2c252a4e1c55c50172807486b2b5a9a901dbbf31d92cad51c5` |
| B | `docs/DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `e5d4ee2b6bc57a75df33c02bc349164729fd38e6` | `cca5ff1af963cc78b2306bd9c7087aa2c7dc52cd91e9b79ec029af79581c0684` |
| J | `.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/autonomous_runtime/RESULT.md` | `f965666ec9e84f94d60a5c0b2ad755d12b0f6de2` | `7c156869a4b8fe1a29ef5eb997fa78f2e553546c03dc812798004ac4eb104e88` |

Procedures read at the same revision: `SCIENCE_WORKFLOW.md` (SHA-256
`1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`),
`skills/workhorse/SKILL.md` (`e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8`),
and its `SKILL_FRESHNESS_CHECK.md` reference
(`b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0`).
They are byte-identical to the named main revision. No network, numerical
runner, additional scientific source, audit ledger, or supervisor
`foundational_bell` artifact has been read. The assignment expressly limits
this check to the named source snapshots, so no fresh literature search is
claimed. This is a proof/assumption check of existing statements.

## 1. Exact logical target

For four conditional expectations of products of binary values, `|Est| <= 1`
and hence `|S| <= 4`, provided all four conditioning events have positive
probability. This algebraic bound needs no physics. The following construction
shows that even operational no-signalling does not lower it under A alone,
when A is completed by an explicitly supplied preparation and formation law.
This is an existence statement about models, not a selection of nature's law.

Two distinctions are essential:

1. A fixes a local **content distribution conditional on formation**. It does
   not fix which site forms next, its rate, or the causal dependence of that
   selection. Nearest-neighbor content dependence is therefore not yet Bell
   local causality for the complete process.
2. `M2(C)` as a site's possibility domain does not supply a bipartite tensor
   product, a density operator, Born probabilities, dichotomic quantum
   observables, or a spacetime identification. Those cannot be inferred merely
   from the name “Qubit”.

## 2. A complete binary witness from the supplied program theorem

### 2.1 An explicit four-step probability tree

Take one fixed Hermitian rank-one projector `P`, use the menu `{P,I-P}` at
every program node, and let `z=0` denote content `P`, `z=1` content `I-P`.
Use the four abstract events in order

```text
z1=s, z2=t, z3=a, z4=b.
p1 = p2 = p3 = 1/2,
p4(s,t,a) = [1 + v (-1)^(a+st)] / 2,     -1 <= v <= 1,
```

where `pj` is the probability of the zero child. All four conditional
probabilities lie in `[0,1]`. The product of the four branch probabilities is

```text
P(s,t,a,b) = [1 + v (-1)^(a+b+st)] / 16.
```

Summing over `a,b` gives `P(s,t)=1/4`. Dividing by that value gives

```text
P(a,b | s,t) = [1 + v (-1)^(a+b+st)] / 4.
```

Both outcome bits are fair for every setting pair. In particular each
observable marginal is independent of the remote setting. With
`A=(-1)^a`, `B=(-1)^b`, the terms odd in `(-1)^(a+b)` cancel and

```text
Est = v (-1)^(st),       S = 4v.
```

Thus `v=0, 1/2, 1/sqrt(2), 1` give respectively `S=0, 2, 2sqrt(2), 4`.
Every signed value in `[-4,4]` is obtained. The endpoints use zero-probability
children, which are omitted from realized histories; their unused prepared
bank entries remain valid. The number `1/sqrt(2)` is deliberately supplied,
not predicted. The case `v=1` is the standard PR correlation, not a novelty.

The independent setting choices can be generated by two independent fair
uniform marks, independent also of the preparation and all non-setting
randomness. The preparation contains entries for **all** setting pairs before
either is chosen; it need not know the actual future choices. Bank selection
for the last event is subsequently permitted to depend on `s,t,a`.

### 2.2 Independent check of the actual lattice embedding

P's kernel is sufficiently explicit to check without its runner. A program
`X=(2+p)I+P` has the unique decoder `p=(Tr(X)-5)/2`,
`P=X-(2+p)I`. For general program recognition, trace-one idempotence is
enough; Hermiticity is an extra condition for the projector specialization.
The recognition set and atoms are Borel. The three kernel cases are
normalized measures, including `p=0,1`. Taking the recorded neighbor multiset
makes the rule invariant under lattice translation and proper cubic rotation.
Trace, idempotence, `0,I`, and the scalar trigger `10I` are preserved by algebra
similarities; no internal basis is singled out by this kernel.

For event `j`, the target is `cj=(20*2^j,0,0)`. Its trigger pair is
`cj+e1,cj+2e1`; bank entry `l` and its buddy are at
`cj+(-3l,3,0)` and `cj+(-3l,3,1)`. The selected route descends through
`(-3l,2,0),(-3l,1,0),(-3l,0,0)` and then moves along the x-axis to `-e1`,
all relative to `cj`.

At the first new route site, the selected source is the only recorded
nearest neighbor: its buddy is at graph distance two, and other sources
differ in x by at least three. At the next two sites only the previous route
site is recorded. Along the axis all sources remain at y=3 and the only
recorded neighbor is again the predecessor. The trigger at `+e1` is never
adjacent to a route site. Consequently every route append uses the empirical
kernel with one atom and copies `X` deterministically. At the fixed target
`cj`, the recorded neighbors are exactly the port `X` at `-e1` and trigger
`10I` at `+e1`; the kernel is precisely the specified binary draw. Target
location is fixed before the current outcome.

The x-gap from cell `j-1`'s rightmost point to cell `j`'s leftmost point is
`17*2^(j-1)-2 > 1` for `j>=2`. The first cell is far from the frame.
Thus no ignored neighboring record changes any of these conditions.

Old-record support is checked by type, not inferred merely from permanence:

- Each bank source/buddy and each copied program has a permanent adjacent
  record with exactly the same content. No trigger becomes adjacent to it.
  Even the final port only gains the data idempotent, so the empirical branch
  continues to support its program content.
- Each trigger keeps its trigger buddy; no program is its nearest neighbor.
- At a data target, its trigger/port neighbors remain unchanged. Its realized
  atom had positive mass and retains that mass under every later prefix.
- Each frame record retains its equal-content buddy and has no trigger/program
  condition. Other cells remain distant.

No record is overwritten: the routes are simple, cells are separated, and a
data target was blank. The scalar marker values `20I,21I,22I,23I` cannot be
created by any program or data branch. The unique `20I` adjacent to `21I`
fixes the frame origin; the nearest `22I` and `23I` fix the other two axes.
The prepared trigger pairs identify the horizon. The recovered banks and
already formed data determine the next route and its partial occupancy. Since
`P != I-P`, each completed data bit is unambiguous. This proves one next-step
answer on each legal prefix, determined by the record configuration itself.
Taking all translated and properly rotated copies of those states makes the
prepared domain covariant. Its selected origin and program are supplied
initial records, not privileged lattice structure.

### 2.3 A formation law, rather than an unexplained event index

P supplies a record-determined order but explicitly does not supply its
physical cadence. An exact model completion is available: at each nonterminal
legal prefix enable only the next site decoded above, with exponential rate
one, and draw its content from `F`. At the terminal prefix stop. This is one
fixed time-homogeneous pure-birth rule on the declared prepared domain. The
exponential waiting law is a chosen mathematical rule; there is no inferred
physical time unit. Because the remaining number of appends is finite, every
legal run terminates almost surely. It is unnecessary to postselect on its
outcome or eventual completion.

This completion is globally controlled: enabling the next bank route may use
old records anywhere in the finite apparatus. A does not supply or require a
causally separated implementation of that controller. No local actuator or
finite-speed propagation has been derived by specifying this formation law.
The rate choice also does not show that the initial program bank can be
prepared by the same process from an empty lattice. The preparation is a
named condition, as in P.

### 2.4 A content-only scalar readout, including the symmetry issue

On the constant-menu construction a fixed calibration `r(P)=+1`,
`r(I-P)=-1` is already a function of record content alone. It is a supplied
observable calibration, not a scalar readout selected by A. This constant-menu
choice matters: P's **general** history-dependent projectors do not by
themselves give one global bit readout. For example, menus with `P'=I-P`
assign opposite bit labels to the same possible recorded matrix. P avoids
that issue by taking identity-valued readout. One must not silently replace
its identity readout by a context-dependent sign.

There is also an explicit extension using P's same kernel that eliminates
any chosen internal basis from the final scalar readout. Give each of the
four events a distant scalar output site `dj`. In the recovered lattice frame
choose

```text
d1=(1000,1000,0), d2=(2000,1000,0),
d3=(1020,1000,0), d4=(2020,1000,0).
```

At each `dj`, prepare content `I` at `dj+3e2` with a matching buddy at
`dj+3e2+e3`; prepare content `0` at `dj-3e2` with its buddy at
`dj-3e2+e3`. After the original event records bit `zj`, set
`epsilon=(-1)^zj` and append successively at

```text
dj+2 epsilon e2,    dj+epsilon e2,    dj.
```

Each site has exactly one already recorded neighbor of the desired scalar
content, no trigger, and no program-valued neighbor. Its empirical law copies
that scalar with probability one. Every old/new scalar retains a same-content
neighbor. These cells are mutually nonadjacent and far from the original
program and frame, so no previous support check changes. The target `dj` is
fixed for both outcomes. The final scalar readout is the single
algebra-invariant map

```text
r(C)=+1 if C=I, and -1 otherwise,
```

restricted to these four targets, whose contents are only `0,I`. Absence is
not a `0` record and is never read. This is an exact content-only binary map;
it does not consult position, the setting, another record, or the previous
history. Roles and trial membership are supplied by the prepared apparatus.
Internal comparisons with the bank's `P` use the already supplied preparation,
and commute with simultaneous algebra similarities; no fixed projector is
built into the law. The four scalar bits have exactly the joint law in 2.1.

Interleave each scalar append stage before the next original event, so both
readable setting records precede both outcome records. Future bank selection
may explicitly use those scalar setting/outcome records. The original and
scalar data are redundant, and their consistency plus partial route occupancy
determines the unique next stage from `R`. Thus the enlarged law remains
record-only and covariant on its prepared domain. With `N=4`, the preparation
has `46+16=62` records and at most `57+12=69` new records form, for a maximum
of 131. These are direct counts, not numerical execution evidence.

The scalar extension is a concrete construction checked here, not something
silently attributed to P. Its final label copies do not claim to be first
draws of the original projector probability; those draws are still the fixed
first-event sites `cj`. None of this is an experimental implementation.

### 2.5 Same initial records can also support different fixed laws

Different values of `v` in 2.1 change the prepared program bank under P's one
universal kernel. That alone rules out a universal CHSH bound smaller than
four across A-compatible prepared experiments. It does **not** mean one
fixed law gives multiple answers at the same record state.

For a stricter matching-premises comparison, hold the entire preparation and
readout fixed. Store the `v=1` tree in the bank and, for each fixed
`v in [-1,1]`, define a separate kernel `F^v` by replacing the program-case
probability `p` with

```text
q_v(p) = (1-v)/2 + v p.
```

Leave both empirical and empty-neighborhood cases unchanged. Then
`q_v(1/2)=1/2`, `q_v(0)=(1-v)/2`, `q_v(1)=(1+v)/2`. Each `F^v` is a single
fixed normalized Borel covariant rule on the full possibility space. The
same routing, old-record support and scalar-copy proof applies; at an endpoint
only supported data branches occur. The rule varies with neighborhood
conditions even at `v=0` (for example the empty and nonempty empirical cases
already differ). Thus the same initial record configuration and same binary
observable give `S=4v` under different explicitly supplied admissibility laws.
For interior values all data histories are supported under the same prepared
prefix domain. No value of `v` is selected by A. This is a witnessed freedom,
not an assertion that every future derivation of a physical law is impossible.

## 3. The precise causal-record Bell bound

### 3.1 Statement and proof using all exogenous variables

Consider a finite acyclic structural model for a trial. Include record
contents, formation/enabling decisions, relevant clock/scheduler variables,
and the rule selecting which records are called the two outputs. Each node
is a deterministic function of its parents and its exogenous random input;
stochastic finite kernels can be represented this way by independent uniform
marks. Correlated common inputs can instead be put explicitly into a shared
variable. Assume:

1. Take the two binary setting values `s,t` themselves as exogenous root
   variables, with all four pairs having positive probability. Their joint
   law is independent of **all non-setting exogenous variables**, including
   the initial preparation. This is sufficient measurement independence,
   stronger than merely `s` and `t` being mutually independent. A more detailed
   physical setting generator must be accounted for explicitly or proved to
   reduce to this representation; unused generator noise is not silently
   discarded if it has another causal output.
2. In this complete graph there is no directed path from the left setting
   source/value to the right output, nor from the right setting source/value
   to the left output. In particular all enabling and selection mechanisms
   obey that separation.
3. Every trial has the declared two binary outputs. No outcome/setting-
   dependent retention or pairing operation is subsequently imposed.

Let `lambda` collect all non-setting exogenous inputs, including the initial
preparation as a root input rather than a later setting-dependent operation.
Its distribution `rho` is independent of `(s,t)`. Recursively substituting
the structural equations along each finite ancestral graph gives

```text
A = A_s(lambda),        B = B_t(lambda).
```

The absent remote-setting paths are exactly what removes `t` from the first
function and `s` from the second. The two functions can share any amount of
setting-independent common history through `lambda`. Consequently

```text
P(A=a,B=b | s,t)
  = integral rho(dlambda) 1{A_s(lambda)=a} 1{B_t(lambda)=b}.
```

For each fixed `lambda`, write `a0,a1,b0,b1 in {-1,+1}`. Its signed CHSH
summand is

```text
C(lambda) = a0(b0+b1) + a1(b0-b1).
```

Exactly one parenthesis is zero and the other is `+2` or `-2`, so
`|C(lambda)|=2`. Averaging under the **same** `rho` for all four setting
pairs yields `|S| <= 2`. Equivalently, if local private noise is integrated
out first, the local means `ms(lambda),nt(lambda)` lie in `[-1,1]` and

```text
|m0(n0+n1)+m1(n0-n1)|
 <= |n0+n1|+|n0-n1| = 2 max(|n0|,|n1|) <= 2.
```

This proves the bound without numerical enumeration or an assumption of
deterministic physics. It applies to an infinite process too whenever the
stated well-defined measurable local response representation is established;
the existence of that representation is not supplied by this finite proof.

### 3.2 What the common-ancestor proof does and does not assume

B's qualified fixed-DAG theorem has the right Bell premise when “fresh
randomness” includes independent setting sources and the **whole** scheduler
is part of the graph. If `W` is the common inclusive causal past of the two
outcomes, its ancestry is closed, exclusive causal branches use disjoint
fresh inputs, and `P(W | s,t)=P(W)`. Here `W` must include all relevant common
variables, or one must show that its recorded values screen off any omitted
controller variables. This supplies the local-mixture factorization stated
in B.

There is a convention issue in B's displayed formula: if “ancestor” means
strict ancestor and neither outcome is included in `W`, it need not be true
under the printed hypotheses. Let `s,t` be unused independent root settings,
let `A` be a fair root outcome, and let `B=A` be its child. Then neither
setting is an ancestor of the remote outcome, but the common **strict**
record-ancestor set is empty. The claimed factorization with empty `W` would
say `P(A,B)=P(A)P(B)`, which is false. The CHSH bound is still true (`S=2`).
Use inclusive ancestral closures, include the shared exogenous input, or
add an explicit non-ancestry condition for the two outcome nodes. The proof
in 3.1 avoids this convention altogether.

### 3.3 Multi-step local influence is still causal influence

Nearest-neighbor dependence does not mean that a remote setting can never
become an outcome ancestor. Along a chain of irreversible record appends,
each site can copy information from the previously formed adjacent site.
After enough steps that information reaches any specified finite distance.
For example, with a shared fair bit `u` independent of both settings, let
`a=u`, convey `s` to the other wing through such a chain, and form
`b=u xor (s and t)`. (The shared bit can be prepared beforehand or also
conveyed.) Then `a xor b=st` and `S=4`, with fair no-signalling marginals.
This is the familiar causal communication example; the complete axiom-
compatible witness and homogeneous kernel are supplied by section 2, not
silently inferred from a drawing of this chain.

More generally, if **every** causal dependency, including site activation,
has lattice range at most `r`, a path of at most `m` dependency edges can
cover distance at most `mr`. A distance greater than `mr` therefore excludes
that path. The axioms give neither such a bound on the complete formation
mechanism nor a bound on the number of intermediate steps before readout.
Spatial separation by itself supplies no Bell separation. Using exponential
waits also supplies no strict minimum traversal time: whenever a finite
transmission chain is enabled with positive exponential rates, its waiting
times have positive probability of summing to less than any given positive
interval. The densities are positive on that interval's nonempty time
simplex. A finite interaction range is not a proven relativistic light cone
or a physical speed calibration.

### 3.4 Scheduling and selection cannot be omitted

An adaptive scheduler may choose a remote site's formation time, its program
source, which neighbor forms first, or which record is reported, based on a
setting. All are potential causal channels even when every *conditional
content kernel* sees only adjacent records. Unroll a finite adaptive process
into fixed stages, include its selection/control variables, and check the
resulting graph or prove the local-response representation directly. Checking
only a realized graph with the controls erased is insufficient. Conditioning
on a realized schedule can itself be selection; a schedule label is not
automatically a setting-independent common cause.

Setting fairness does not fix this. A common variable could contain two
independent fair preassigned setting bits and an outcome rule. The observed
settings would be independent of each other but not independent of the common
variable. Measurement independence is a relation to all relevant causes.

Nor does no-signalling fix postselection. Start with four mutually independent
fair bits `s,t,a,b` and retain precisely those trials with `a xor b=st`.
For each setting pair the retention probability is `1/2`; among retained
trials the settings remain uniform and both outcome marginals remain fair,
but `S=4`. Thus even setting-independent total detection rates do not suffice
to justify ignoring an outcome-dependent selection. An event-ready herald
formed before independent settings may safely restrict the preparation;
that is a different condition and must be established for the protocol.

### 3.5 Correct scope of the source note's prose

B's final “Causal and no-signalling qualifications” explicitly adds a fixed
DAG, independent exogenous inputs, nonzero setting probabilities, absence of
postselection, and scheduler accounting. With those qualifications and the
ancestry convention fixed, its classical Bell bound is correct.

Its summary table's first row and the sentence in “Consequence for the
supplied model” that independent settings plus neighbor-record conditioning
always stay classical omit causal separation. Read literally, that statement
is refuted both by B's own communication example and by section 2 above.
Likewise “the quantum value needs ... an unrecorded neighbour's state” is
not a necessity theorem for A: a records-only programmed model reaches that
number, or four, through a controller carrying setting information. Adding
an unrecorded state variable would not by itself defeat the Bell bound if
the same local response factorization still held. These are precise scope
corrections; no source file is edited by this check.

The Tsirelson bound has different supplied hypotheses. For a setting-
independent bipartite state, the Born rule, and local Hermitian dichotomic
operators `As` and `Bt` with `As^2=Bt^2=I`, the operator
`C=A0 tensor(B0+B1)+A1 tensor(B0-B1)` satisfies

```text
C^2 = 4I - [A0,A1] tensor [B0,B1],
||[A0,A1]|| <= 2,   ||[B0,B1]|| <= 2,
||C|| <= 2sqrt(2).
```

The identity follows by expanding the square; the terms involving each
observable's square give `4I`, and the cross terms give the commutator
product. These hypotheses do not follow from the one-site algebra in A.
Even a supplied quantum circuit can reach the algebraic CHSH value if it is
allowed to communicate settings: “quantum dynamics” alone is not the local
measurement hypothesis in this operator proof.

## 4. The actual autonomous jump model does not supply Bell separation

J's record clock addresses a distinct issue: its fixed initial live-state
function and logged phases reconstruct the live/work state from `R`, and
scalar total jump intensity on each legal phase makes normalized no-jump
evolution trivial. Under those declared hypotheses, changing positive
`gamma_j` changes waits but not the supplied instrument's outcome cylinders.
This is a state-sufficiency/clock argument, not a causal-separation argument.

The relevant locality facts are explicit in J and do not require its unseen
implementation files:

- Its next content distribution is reconstructed from a radius containing the
  **entire finite apparatus**, with the stated loose choice
  `R=10T+15n+30`. This is not a six-immediate-neighbor kernel. Each fixed
  `n,T` can have one finite radius under J's stated broad neighborhood
  interpretation; the family does not prove one uniform microscopic radius
  for arbitrarily large programs. If “neighborhood” is restricted to the six
  immediate neighbors, J has not established that more restrictive premise.
  Section 2 does not depend on this interpretive issue: its content kernel
  really uses six immediate neighbors.
- Its jump operator is
  `L_(j,b)=sqrt(gamma_j) |1><0|_(c_(j+1)) [K_(j,b) tensor I] Pi_j`.
  `Pi_j` checks the full legal clock prefix and header/output guards;
  adaptive `K` can depend on earlier recorded results. The support therefore
  includes these controls. A gate's data pair can be adjacent while the same
  joint jump touches a distant tape tick.
- A binary-read jump appends the value and tick together at two fixed sites.
  The axioms need not forbid this, but joint append is an extra chosen
  transition rule. It is not a proof of separate local actuators or a
  decomposition compatible with two spacelike readout regions.
- Independent exponential waits and a record-derived phase make the model
  autonomous. They do not prevent a prior setting record from affecting a
  later remote instrument through `Pi_j`, the program, state reconstruction,
  or the joint clock/gate channel. Observable no-signalling of a particular
  supplied instrument would not remove those internal dependencies.

J itself states these limits. No Bell setting/outcome identification, shared
singlet preparation, or separated two-wing measurement protocol is specified
in the allowed autonomous result. Therefore that **actual** program has no
CHSH prediction established by this check. If one later supplies local tensor-
product measurements on a setting-independent shared state, the usual quantum
probabilities may be obtained as an instrument identity; a spacelike physical
implementation of the jump clock remains a separate obligation. If one
instead supplies the causal-record hypotheses of section 3, the Bell bound
follows regardless of the operator notation used to define its kernels.

## 5. Assumption ledger and empirical meaning

| Item | In A or checked here? | Consequence / remaining obligation |
|---|---|---|
| Actual `Z3`, full one-site `M2(C)`, permanent supported records, content-only readout | Primitive content of A; geometry/support/readout checked explicitly in section 2 | Does not select probabilities, formation dynamics, or a physical Bell observable |
| One fixed covariant content kernel | Required by A; P's kernel and the explicitly defined `F^v` each satisfy it on their stated models | The numerical rule is chosen, not derived |
| Prepared frame, bank, source records, legal-prefix domain | Supplied condition in P and section 2; all translated/properly rotated copies included | No preparation from an empty lattice or empirical calibration is proved |
| Formation controller and cadence | Supplied completion, with record-only reconstruction and exponential rate one | Global dependencies are allowed here; no short-range actuator or speed law follows |
| Binary settings and outcomes | Fixed constant menu, or fully content-only scalar `0/I` registers, constructed here | Role assignment and trial membership are supplied; the generic varying-menu theorem alone has no single sign map |
| Setting independence | Mathematical independent random sources supplied in the witness | Physical independence from preparation, hidden causes, and scheduling is additional; marginal setting fairness is weaker |
| Bell causal separation | Added hypothesis of section 3, explicitly absent from the communicating witness | Must hold for the complete formation, control, clock, readout and selection mechanism |
| Complete trial sample | Added hypothesis of section 3; finite witness terminates almost surely without outcome selection | Real detection, heralding and trial-pairing rules need the corresponding justification |
| Tensor product, quantum state, Born rule, local dichotomic observables | Supplied quantum hypotheses, not A; operator bound checked in 3.5 | Gives `2sqrt(2)` as a conditional upper bound, not a foundational selection |
| Autonomous joint jumps | Chosen dynamics in J, with apparatus-scale support and fixed seed/domain | Autonomy does not prove Bell-locality, uniform microscopic range, or spacelike implementation |
| Physical spacetime and observable bridge | Not supplied in these sources | Needed to identify sites/ticks with apparatus locations/times, settings with controllable choices, and records with locally accessible detector results |
| Repeated-trial comparison | Not supplied or tested here | Requires a stated stationary/repeatable preparation and sampling or memory model, treatment of failures, uncertainty, and a predeclared empirical comparison |

For an **empirical Bell interpretation**, the last obligations are concrete:
select and physically justify the preparation and transition law; identify
and calibrate the two setting choices, two outcomes and trial protocol; show
the settings are independent of relevant common causes; establish the claimed
spacetime separation for the *whole* realization; account for detection,
heralding and record pairing; and provide a valid repeated-trial statistical
comparison with measured data. A finite probability table matching a familiar
CHSH number supplies none of those bridges automatically. No such experiment
or empirical adequacy result is claimed here.

## 6. Check result and verification limits

The explicit construction closes the requested logical test: on a supplied
prepared domain, the four axioms admit a binary content-only CHSH observable
with every signed value in `[-4,4]`, including fair no-signalling witnesses.
It checks formation, covariance, old-record support, fixed output sites,
settings and readout rather than relying only on an abstract table. It also
exhibits distinct fixed laws on the same initial record state. This establishes
neither empirical adequacy nor a preferred physical law.

The causal-record theorem closes under the stated complete-model premises
and gives `|S|<=2`. Multi-step communication, scheduler control, dependence
of the relevant common causes on the settings, or postselection are outside
those premises. J's declared apparatus-scale joint jumps do not discharge
the required spacelike causal realization. Two precise source qualifications
are recorded in 3.2 and 3.5; the classical bound itself survives them.

This checker independently reconstructed the relevant geometry, support,
probability products, scalar transduction, exact CHSH algebra, complete-cause
factorization proof, and the support of J's displayed jump operators. It did
not run or inspect numerical runners, verify B's static-chain rational number,
reconstruct the unseen companion Heisenberg/field premises, audit all of J's
gauge implementation, compare empirical data, or grant retained status. The
new scalar transduction and fixed-preparation `F^v` variant have this checker's
explicit proofs but still require supervisor scrutiny before downstream use.

The original-source check was completed before any supervisor `PRIMARY.md`
content was read. The supervisor communicated only its frozen hash while this
artifact was being written; that hash supplied no mathematical premise. Any
later source-exposed comparison must be distinguished from this independent
phase. No source, prompt, instruction file, commit, or remote was modified;
the single authorized deliverable is this file.

## Recovery checkpoint

All four scientific sources were read in full, and the complete deliverable
was inspected after the incremental writes. An initially truncated aggregate
result was replaced by separate complete reads where necessary. The source
identities above are the recovery authority, not a moving checkout. The
original-source mathematical check is complete; the next authorized step is
supervisor scrutiny and, if requested, a separately labelled source-exposed
comparison. No physical-law selection or empirical Bell claim is pending as
an implied accomplishment of this check.
