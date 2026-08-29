# Goal

Source/Eta Block 17 runs the single bounded compiler scout selected `3--2` by
the post-Block16 five-physicist panel.  It asks whether the Block16 effective
writer and one exact Block15 controller step have a **table-free finite
nearest-neighbor transaction grammar**, including simultaneous-trigger
conflict handling, explicit environment accounting, and exact channel—not
sample-state—equality.

This block must also decide a carrier-type question rather than hiding it.
As a selected downstream effective carrier, Block16 acts on

```text
A_B = direct_sum over Record masks S subset B of M2(C)^(tensor B)
    ~= (M2(C) direct_sum M2(C))^(tensor B).
```

The two local summands distinguish no-Record and Record status while retaining
arbitrary `M2(C)` content in each.  The scout separately tests whether the
required channel factors through a strict single-`M2(C)` carrier after that
status is forgotten.  Neither this direct-sum carrier nor support of the
proposed `rho_f` and `rho(r_(f,b))` contents at the relevant neighboring
conditions is supplied by the minimal axioms.  A failure of this strict
factorization is not a locality or dynamics no-go: a downstream hybrid
classical-quantum law, a distributed orthogonal pointer, or a wider carrier
remain live.

## Exact target contract

| field | frozen contract |
|---|---|
| Target statement | Construct one branch-independent radius-one transaction grammar that realizes the Block16 six-way writer and one Block15 step, or identify the first exact failure inside the frozen class. |
| Quantifiers/domain | Every signed axis, proper cubic frame, translated selected center, arbitrary 43-site blank-sector quantum input entangled with an arbitrary reference, every nonblank writer mask, every Block15 outcome and five-destination obstacle mask, and every simultaneous trigger configuration reduced to its local conflict neighborhoods. |
| Allowed premises | Minimal axioms; frozen Blocks 15 and 16; one selected-center trigger or simultaneous trigger set for a single invocation; product-initialized finite local environment; exact finite-dimensional CP/instrument mathematics; exact algebraic onsite preparation gates explicitly named below. |
| Forbidden weakenings | A block-sized gate, global blank projector, absolute coordinate or parity tiling, supplied direction, six-row target table, branch dictionary, target-programmed ancilla, postselection, output-only/sample-only comparison, external winner/scheduler, partial Record write, approximate coefficient, hidden erasure, or calling circuit depth a physical rate/clock. |
| Required edge cases | Same `M2` content with and without a Record; shell-eight transaction conflicts; radius-eight nonconflicts; multiple simultaneous triggers; occupied writer sites; all 32 controller obstacle masks; arbitrary reference entanglement; STOP workspace cleanup; all rotations and translations. |
| Completion witness | A finite alphabet and port-register circuit with exact CP/TP and covariance identities, causal depth and environment bounds, branchwise channel equality, monotone Record locks, exact disjoint factorization, all-conflict STOP, and one exact Block15 step. |
| Outcomes that do not close | Generic Stinespring-plus-SWAP existence, an enumerated `43x6` program, an effective flag table, geometry generation without channel equality, a writer without its first step, or a synchronous compiler presented as occurrence/time. |

## Generated supports

Let `D` be the six signed coordinate axes.  The grammar may use only lattice
ports and the relations equality, opposite, and perpendicular.  It must derive

```text
B = {0}
    union {k f : f in D, 1 <= k <= 3}
    union {2 f + e : f,e in D, f dot e = 0},

F = {0}
    union {k f : f in D, 1 <= k <= 4}
    union {k f + e : f,e in D, f dot e = 0, k in {2,3}}.
```

`B` is the 43-site writer support.  `F` is the corrected 73-site writer plus
first-controller-step footprint.  Generate them with the finite port grammar

```text
C       -> A1(p),                    all six ports p
A1(p)   -> A2(p)
A2(p)   -> A3(p) and T2(p,q),        q perpendicular to p
A3(p)   -> A4(p) and T3(p,q),        q perpendicular to p
```

where `Ak(p)=k p` and `Tk(p,q)=k p+q`.  The role and reverse-path labels are
transient generated workspace.  They are not supplied site identifiers and
must be uncomputed.

## Frozen transaction phases

The prospective compiler uses finite local port registers.  An onsite scatter
writes six outgoing registers; simultaneous nearest-neighbor port swaps move
messages on disjoint subregisters of each edge; onsite collision/logic then
updates local workspace.  This is the gate-level object to verify.  Merely
asserting a synchronous cellular automaton does not pass.

### 1. Writer blank validation

Every site in `B` returns its Record-presence bit along its generated path.
Any nonblank writer mask produces exact writer STOP/identity.  The 30 sites in
`F-B` are not required to be blank: their flags belong to the later Block15
obstacle test.  No system quantum content changes before the writer commit
barrier.

### 2. Simultaneous-trigger conflict wrapper

For a simultaneous trigger field `T`, define

```text
K = F - F,
h(c) = T(c) AND OR over nonzero delta in K of T(c+delta).
```

Each trigger sends one provenance-preserving tag to every site of its
translated `F`.  A multiply claimed site returns abort along every reverse
path.  At a conflicted center `h=1`, the full transaction takes deterministic
identity/STOP before any branch coin or Record lock.  At `h=0`, it may commit.
Disjoint footprints must factorize exactly.

Finite trigger examples are only regressions.  The construction must prove
symbolically, for arbitrary centers and an arbitrary trigger field,

```text
(c+F) intersects (c'+F)
  iff c'-c belongs to (F-F) without {0},
```

and its generated tag rails must compute exactly the Boolean OR in `h(c)` for
arbitrary assignments of those local trigger variables.  This set/Boolean
identity, not enumeration of a few trigger shapes, carries the universal
simultaneous-trigger quantifier.

The protocol must derive, not embed, `K`; prove that the center decision needs
and admits eight nearest-neighbor hop layers; make every visible commit wait
until layer twelve; and restore all reusable conflict workspace by a finite
fixed layer.  These layers are compiler depth only.  The trigger batch and its
concurrency window remain supplied.

### 3. Table-free six-way writer

At one clean isolated center, one covariant scalar-to-port coin gives the six
directions with effects `I/6`.  For realized port `f`, generate roles by

```text
Record with rho_f: C, A1(f), A2(-f)
live rho_f:        A3(f)
gap/candidate:     A1(-f), A2(f)
default I/2:       every other site in B,
```

where

```text
rho_f = (I - (143/256) f dot sigma)/2.
```

Use one base purifier

```text
P_143 |00> = sqrt(113/512)|00> + sqrt(399/512)|11>
```

and cubic-spin rotations, or the equivalent exact mixture

```text
rho_f = (143/256)|-f><-f| + (113/256) I/2.
```

Default sites use a Bell purification of `I/2`.  Local staging/system SWAPs
dump the complete arbitrary input, including its reference entanglement, into
the environment.  Monotone no-Record-to-Record locks occur only at the three
generated Record roles.  Branchwise the runner must prove symbolically

```text
(Phi_f tensor id_R)(X_BR)
    = (1/6) sigma_f tensor Tr_B(X_BR)
```

for arbitrary `X_BR`, not only the displayed product inputs.

### 4. One Block15 step

After writer workspace is removed, the candidate `2f` must infer `f` from the
Record at `f` and its collinear predecessor at `0`; the writer coin may not be
reused as an orientation oracle.  The fixed `M=0` shell has fourteen outcomes:
six axis outcomes of weight `1/12` and eight corner outcomes of weight `1/16`.

For frozen unit outcome vector `s_b`, generate the new Record state without an
84-row table through

```text
r_(f,b) = -(9/16) f + (1/256) s_b,

rho(r_(f,b))
    = (144/256) rho(-f)
    + (1/256) rho(s_b)
    + (111/256) I/2.
```

Axis states come from one axis base state and cubic rotations.  Corner states
come from one `(1,1,1)/sqrt(3)` base state and its cubic orbit.  The event
locks a Record at `2f`.  If all five branch destinations are Record-free, it
then applies the five disjoint nearest-neighbor content SWAPs

```text
3f -> 4f,
2f+q -> 3f+q,             q perpendicular to f.
```

If any destination has a Record, it leaves all ten source/destination contents
unchanged after the new Record forms.  This controller STOP is distinct from
the pre-coin transaction-conflict STOP.

Channel equality is required here as well as for the writer.  For candidate
`x=2f`, let `S` be the ten source/destination content registers, let `R` be an
arbitrary reference, let `U_m` be the product of the five disjoint SWAPs for
the clear obstacle mask and the identity for every blocked mask, and let
`w_b` be `1/12` for an axis outcome or `1/16` for a corner outcome.  The
outcome subchannel must satisfy, for every operator `X_(xSR)`,

```text
(Theta_(f,b,m) tensor id_R)(X_(xSR))
  = w_b rho(r_(f,b))_x tensor
      Tr_x[(U_m tensor I_R) X_(xSR) (U_m^dagger tensor I_R)],
```

together with the exact Record-sector lock at `x` and preservation of every
other Record flag.  Thus the 2,688 discrete geometry/outcome/mask cases are a
control census, not a substitute for equality of the CP instrument on
arbitrary contents and reference entanglement.  Summing all fourteen outcome
subchannels must be trace preserving for each fixed `f,m`.

The composed blank-sector instrument must additionally expose the product
weights rather than infer them from two separate normalizations.  Its 36
`(f,axis)` branches have effects `Pi_blank/72`, its 48 `(f,corner)` branches
have effects `Pi_blank/96`, and all 84 effects sum exactly to `Pi_blank`.
Nonblank writer masks belong to the separate deterministic pre-coin STOP
branch.

## Environment and erasure ledger

For `d=2^43`, each full-rank trace-and-prepare branch has Choi rank `d^2`, so
an instrument dilation that retains the six blank-sector outcomes in
orthogonal environment sectors has rank `6 d^2`.  The deterministic nonblank
STOP sector adds one Kraus branch, for exact rank `6 d^2 + 1`.
Any such pure-environment realization therefore has a **dilation lower
bound** of 89 environment qubits' worth: 43 input-dump qubits, 43 output-
purification qubits, and a three-qubit branch sink meet this lower bound before
reusable workspace.  The branch sink is part of those 89 environment qubits.
If the outcome is also exposed as a readable apparatus/output register, that
register is additional and is not included in the 89.  This is not a qubit
ceiling, and coarse-graining away the outcome would be a different channel.

That 89-qubit lower bound is writer-only.  For the composed six-direction,
fourteen-outcome target, each of the 84 orthogonally labeled blank-sector
branches still discards the original 43-site `B` input and prepares 43
full-rank contents; the 30 added footprint contents are transported unitarily.
The deterministic nonblank writer-STOP sector adds one Kraus branch.  The
composed Choi rank is therefore `84 * 2^86 + 1`, still giving a 93-environment-
qubit dilation lower bound.  The runner must derive its own finite realization
allocation, including all candidate dumps, purifiers, direction/outcome and
affine-mixture sinks, conflict provenance, and reusable workspace.  No upper
allocation is frozen here.  Exposed direction/outcome apparatus registers are
additional outputs.

The scout must distinguish:

- input dumps, which may retain arbitrary input/reference entanglement;
- output purifiers;
- writer and controller branch/outcome sinks;
- reusable address, role, flag, conflict, acknowledgment, and phase workspace,
  which must return to its product blank state;
- Record status, which is not to be silently counted as an `M2` qubit.

Finite but large conflict-provenance storage is acceptable if counted.  A
claim of microscopic economy is not.

## Strict-`M2` factorization subtest

Let `forget` discard the local no-Record/Record summand label while retaining
the complete `M2` content.  Test whether a channel `Psi` on strict qubit
content with the same product environment can satisfy

```text
forget o Phi = Psi o forget
```

on every Block16 sector.  The decisive witness must compare a blank and a
nonblank effective input with identical qubit content.  It must also test the
algebraic center/dimension distinction between `M2 direct_sum M2` and `M2`.

A failure proves only `NO-FACTORIZATION-THROUGH-STRICT-M2` for this exact
quotient.  It must not be promoted to a Record, locality, dynamics, wider-
carrier, distributed-code, or framework no-go.  Any negative output requires
the current N1--N8 No-Go Discipline packet and landing N5 execution lines.

## Exhaustive target

The primary must derive and check:

- `|B|=43`, `|F|=73`, `|F-B|=30`, all generated-parent/path identities, and
  all rotation/translation covariance identities;
- `K=F-F`, its complete bounded-box membership, shell/orbit/multiplicity
  census, every conflicting pair, and every in-radius nonconflict;
- singleton, pair, path, triangle, isolate-plus-edge, and dense trigger
  configurations as regressions, plus the parametric overlap equivalence and
  exact arbitrary-trigger Boolean OR under the STOP-all predicate;
- prefix identity before commit, transaction STOP identity, disjoint
  factorization on arbitrary cross-footprint/spectator entanglement, commit
  barrier, and workspace cleanup as an exact reversible isometry/channel
  identity rather than deletion or reset of simulator variables;
- the six writer branches, exact physical state preparations, branch effects,
  full arbitrary-reference channel identity, and every nonblank writer mask
  symbolically rather than sampling `2^43-1` cases;
- every direction, fourteen outcomes, 32 branch-destination obstacle masks,
  exact Record state, five SWAPs/identity, Record permanence, and the full
  arbitrary-reference controller-instrument identity for the first Block15
  step;
- the strict-`M2` quotient witness, all declared resource bounds, and source/
  AST scans excluding coordinate arrays, output tables, branch dictionaries,
  target-programmed ancillas, scheduler inputs, and hidden prior-runner calls.

Source/AST scans are supplementary.  The primary must build the construction
through an allowlisted circuit DSL and canonical emitted netlist that accounts
for every register, support, algebraic constant, gate matrix or Kraus map, and
inverse/uncompute operation.  Its six-way and fourteen-way coins must be
generated from the signed-axis and axis/corner orbit grammars, never a hidden
row list.  Translation covariance must be parametric in the center rather
than sampled.  The runner must report edge-transfer communication rounds
separately from actual elementary depth, which also counts onsite scatter,
collision logic, preparation, SWAP, lock, and cleanup layers.

The structurally independent checker must not import the Block17 primary,
Block16 primary, or Block15 primary.  It must reconstruct geometry, conflict,
states, netlist semantics, and the carrier quotient by different data
structures and extend at least one trigger or reference-system axis.

## Prospective adjudication

Exactly one overall terminal must be returned:

- `NN-TRANSACTIONAL-CAP-PACKET-AND-FIRST-STEP-COMPILER`: the complete finite
  port-register circuit, hybrid Record operations, environment, writer,
  conflict wrapper, first step, cleanup, and covariance all pass with no
  hidden schedule/table import;
- `HYBRID-RECORD-SECTOR-NN-TRANSACTION-GRAMMAR`: the table-free radius-one
  grammar, exact effective channel, conflict wrapper, and first step pass, but
  microscopic Record-sense/lock or conversion of logical rounds to a lawful
  physical update remains an explicit downstream import;
- `NN-WRITER-ONLY`: the writer channel compiles but conflict, cleanup, or the
  first controller step fails;
- `SCOUT-FAILED-TO-CONSTRUCT-FROZEN-SIGNED-RAY-FAN-GRAMMAR`: the one frozen
  construction fails at a named identity or implementation boundary.  This
  terminal makes no no-member claim about the unbounded class of all finite
  alphabets, depths, environments, or exact onsite gates.

The strict-`M2` quotient result is a mandatory subcertificate and not by
itself the overall terminal.

### Pre-execution support correction

The framework's current minimal premises describe realized Record
configurations and make non-Record sites unreadable.  They do not derive a
local `M2 direct_sum M2` hardware carrier with arbitrary hidden content in
both sectors, mask superselection, a QND Record-presence sensor, a microscopic
monotone lock, the proposed conditional Record contents, or the synchronous
invocation/update law used by this compiler.  Those are selected Block16
downstream effective-law imports.  Consequently the
`NN-TRANSACTIONAL-CAP-PACKET-AND-FIRST-STEP-COMPILER` terminal above is a
counterfactual completion target and **cannot be awarded in this block**.
Even if every finite circuit identity passes, the strongest honest terminal
is `HYBRID-RECORD-SECTOR-NN-TRANSACTION-GRAMMAR`, with those imports named.
This correction was frozen before either Block17 runner was executed.

The originally listed `NO-MEMBER-IN-FROZEN-COMPILER-CLASS` failure terminal
is also unavailable.  The allowed finite alphabet, environment, fixed depth,
and exact onsite gates were not capped, and no exhaustive decision procedure
over that infinite union was preregistered.  Failure of this scout can support
only the construction-specific terminal above, followed by the declared
occurrence-law pivot.

## Hard falsifiers and kill criteria

- any block-sized or non-nearest-neighbor system gate;
- any supplied direction, absolute coordinate/parity, role table, epoch,
  target state list, `sigma_f` constructor, output-programmed environment, or
  branch-visible signal before the clean commit;
- failure of exact `1/6`, `1/12`, `1/16`, `143/256`, or state positivity;
- equality on samples without the arbitrary-reference channel identity;
- a global blank projector or Record-content measurement substituted for a
  Record-presence operation;
- failure to preserve every occupied Record or restore STOP workspace;
- conflict radius seven, whole-radius-eight overblocking, one-sided/winner
  arbitration, eager writes, postselection, deadlock, or order dependence;
- reuse of the hidden writer branch as the Block15 orientation input;
- uncounted entropy disposal or reusable work that is merely traced away;
- calling the `M=0` first-step compiler a compiler for the general
  content-dependent law;
- calling invocation layers a formation hazard, physical time, or clock.

Stop the route after this one scout if it reduces to generic Stinespring plus
SWAPs, embeds the target table in gates/ancillas, cannot make the hybrid
Record operations explicit, or cannot give a branch-independent port grammar.
The immediate pivot is a pure-jump Record-configuration occurrence/joint-law
campaign; gravity remains later until a timed conserved event current exists.

## Frozen authority and accounting

- Block16 delivery `7cda8b604004d16c1becf08c503e05c54c48844a`;
- Block16 science result `71c02ab1fe5129e76263c683300304ab4ff45d19`;
- Block16 preregistration/support commits `e7d83357cbee8910e4fefd0784de6bad5d5884ef` /
  `d51484274ff001cec0e4bb6753eedaf88e3adff2`;
- observed `origin/main` `3cc632921c36aa90266c5c62e56816577ce59a0a`;
- minimal-axiom blob `bc23300becfe4e4db57153c0e94cfcdf2338da71`;
- Block16 note/primary/independent/primary-cache/independent-cache blobs
  `cff125525fcf7e1596842d4486d89604b828dfc6` /
  `014c60f3585939ca7f70c32e2f021b7bb89551cb` /
  `45f2d920490a5b333cdfb804cf4e37d2850dca33` /
  `0dd6cc7e1795eaf1da9345d1c13aee1381028e41` /
  `89eb61a4546520d88f154f22c745d55b3773e2c3`;
- latest inspected Source/Eta PR `#7787`, head
  `f5e5c140c06df6aaf6c1b76c2e165c5a49ca4a90`;
- latest inspected connection/gravity PR `#7800`, head
  `323aba2461e15409c109611f959cdc44c0d06566`.

This preregistration authorizes no minimal-axiom edit.  Even a full author-side
compiler does not set an audit verdict, retire a formal obligation, or move a
TOE percentage by itself.
