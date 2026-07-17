# Gate-faithful FSWAP physical close — Cycle 259

**Date:** 2026-07-17

**Type:** exact finite conditional transducer plus fault-domain discriminator

**Status:** gate-faithful for deletion of one declared joint data-plus-flag
call; not an unconditional data-gate occurrence certificate

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

Companion runner:

```text
scripts/gate_faithful_fswap_physical_close_cycle259_2026_07_17.py
```

This cycle creates only this note and runner.  It changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface.

## Result up front

Cycle 259 constructs the strongest finite nondemolition close tested here for
the **actual Cycle-230 two-mode FSWAP** fixture.  It combines two bounded
diagnostic arms:

1. the declared data call is the supplied joint unitary
   `A_F = FSWAP_D tensor X_flag`; and
2. a second declared FSWAP use acts on half of a prepared four-dimensional
   maximally entangled state and is tested by the exact FSWAP Choi projector.

The named completion candidate forms only when the data-side flag is one and
the Choi test passes.  On the declared two-case **common-control fault domain**

```text
joint data-plus-flag call present: data FSWAP, flag=1, probe passes;
joint data-plus-flag call deleted: data identity, flag=0, probe passes,
```

the rule has zero deterministic false positives and zero deterministic false
negatives.  Deleting the declared physical data-plus-flag call leaves the
flag at zero, gives acceptance weight zero, and prevents the completion
candidate.  In the successful case, tracing out every flag, probe, and
candidate-Record carrier recovers the ideal FSWAP channel on an arbitrary
two-mode density matrix with residual zero.  The successful joint state
factorizes, and the two independent call orders give joint-state residual
zero.

This is a real improvement over Cycle 255's fixed completion tag.  There,
deleting FSWAP changed the data but left the same five Records.  Here, deleting
the declared joint call removes the completion.

It is not yet genuine, fault-independent evidence that the data FSWAP factor
occurred.  The decisive **split-fault** control deletes only the data FSWAP
factor while retaining `X_flag` and the successful diagnostic FSWAP replica:

```text
data = identity, flag = 1, Choi probe = FSWAP  -> completion forms.
```

That is one exact false positive.  Conversely, keeping the data FSWAP while
deleting the probe, the flag flip, or both produces three exact false
negatives.  Thus the finite construction is a **trusted shared-control** close
proxy: the flag proves that the declared call was commanded, while the Choi
arm proves that a separate diagnostic use has the FSWAP channel.  Their
conjunction does not prove that the FSWAP factor acted on this data invocation
unless a physical common-failure/link law is supplied.

There is also an exact reason to use an external carrier rather than inspect
only the final data.  The vacuum `|00>` and symmetric one-particle state
`(|01>+|10>)/sqrt(2)` are `+1` FSWAP eigenstates.  FSWAP and identity produce
identical density matrices on both.  Hence an after-the-fact data-only effect
whose sole input is the final data density cannot certify occurrence
uniformly over all lawful inputs.  This is a two-state indistinguishability
fixture, not a broad no-go for interaction monitors that access a coupling
current, environment, or syndrome.

The answer is therefore:

- **yes**, a bounded nondemolition transducer can pass the required deletion
  test exactly when “coupling omitted” means deletion of the declared joint
  data-plus-flag call;
- **no**, this finite artifact is not an unconditional occurrence certificate,
  because the omitted data FSWAP factor split-fault still produces completion;
  and
- **no broad impossibility follows**: an intrinsic interaction monitor,
  fault-tolerant verified primitive, or different physical coupling could
  close the split-fault seam.

The coherent carriers are not Records.  The close effect, actualization,
permanence, failure readout, diagnostic preparation, common-control link, and
complete law selection remain explicit supplied structure.  No axiom
pressure follows.

## 1. Foundation and source boundary

The current minimal axioms supply physical `Z^3`, nearest-neighbor adjacency,
translations, the 24 proper-cubic rotations, and `M_2(C)` at each physical
site.  Record supplies formation in the abstract, one locked admissible
possibility per occupied Record site, permanence, content-only readability,
and additive scalar readout over disjoint Records
(`MINIMAL_AXIOMS_2026-06-29.md:35-84`).

They do not select an update, a flag, a Choi preparation, a comparison effect,
an occurrence criterion, a Record-formation map, a sampling rule, a time
metric, or a rate (`:86-145`).  Three-dimensional space remains axiomatic
input.  The twelve-site motif below does not derive three spatial dimensions.

The approved primitive registry adds no hidden close:

- scale reference converts units but supplies no dimensionless dynamics;
- kinetic isotropy supplies only structural `c_t=c_s`, not an update,
  occurrence monitor, readout bridge, or Lorentz theorem; and
- realized-state evaluation supplies a pointwise evaluation slot but no
  state, preparation, selection, weighting, or probability law.

The exact predecessor boundary is:

- Cycle 230 supplies the intrinsic CAR FSWAP factor, not Record occurrence;
- Cycle 243 separates event, physical close, commit, and Record maps;
- Cycle 255 gives a nondemolishing fixed transcript whose completion survives
  gate deletion; and
- Cycle 257 records a gate-faithful nondemolition transducer as a live finite
  target, independent of the unfinished global CAR compiler.

The bounded pointer-formation theorem of 2026-06-05 is used only as a
firewall: a coherent controlled copy can preserve a pointer, but the selected
pointer, fragment preparation, actualization, and Record identification are
additional inputs.  It does not supply this close law.

## 2. Exact finite transducer

In the occupation basis `|00>,|01>,|10>,|11>`, let

```text
          [1 0 0  0]
F =       [0 0 1  0]
          [0 1 0  0]
          [0 0 0 -1].
```

The runner checks

```text
F^dagger F = I,
F^2 = I,
F = F^dagger,
[F,(-1)^N] = 0,
Tr F = 0.
```

The local Cycle-255 fixture

```text
E_local |0_L> = |00>,
E_local |1_L> = |11>
```

still obeys `F E_local = E_local Z_L`, with isometry, intertwiner, and
leakage residuals exactly zero.  This is only a two-mode fixture, not the
missing global ordinary-M2 CAR encoder.

### Data-side flagged call

Prepare one coherent flag in `|0>`.  The supplied joint call is

```text
A_F = F_D tensor X_flag.
```

Its declared deletion is

```text
A_F -> I_D tensor I_flag.
```

The tensor-product form is intentional and scientifically revealing.  It is
not derived that the two factors fail together.  Calling `A_F` one physical
call is a supplied law-domain statement, not a theorem that the flag has
measured the FSWAP action.

### Choi diagnostic arm

Let

```text
|Phi_4> = (1/2) sum_(j=0)^3 |j>_P |j>_R,
|J_V>   = (V_P tensor I_R)|Phi_4>.
```

The target effect is

```text
Q_F = |J_F><J_F|.
```

For any promised unitary `V`, its finite acceptance weight is

```text
w_F(V) = <J_V|Q_F|J_V>
       = |Tr(F^dagger V)/4|^2.
```

Therefore

```text
w_F(I) = 0,
w_F(F) = 1.
```

Within the promised unitary class, equality in Hilbert-Schmidt
Cauchy-Schwarz gives `w_F(V)=1` exactly when `V=e^(i phi)F`, which is the same
quantum channel.  This is stronger than the preparation-light sentinel
`F|10>=|01>` because the sentinel tests only one prepared input.

The Choi preparation uses four physical M2 carriers and coherent
superpositions across the supplied occupation basis.  Its preparation,
phase/reference coherence, test effect, and physical realization are inputs;
none comes from Record or from the realized-state primitive.

### Close effect and successful channel

The coherent close effect is

```text
Q_close = |1><1|_flag tensor Q_F.
```

For arbitrary data density matrix `rho`, the successful declared operation is

```text
rho
 -> F rho F^dagger tensor |1><1|_flag tensor |J_F><J_F|.
```

This state lies entirely in `Q_close`.  A Lüders support test therefore leaves
it unchanged.  The runner reports

```text
acceptance weight             = 0.9999999999999999,
data partial-trace residual   = 0,
carrier partial-trace residual= 0,
factorization residual        = 0,
scheduler joint residual      = 0.
```

After the separately supplied `R_form` appends the five successful Records,
the data-plus-transcript state also factorizes exactly; tracing the transcript
recovers `F rho F^dagger` with residual zero.

This is nondemolition of the quantum data channel.  It is not a claim that a
coherent projector or flag has already become a framework Record.

## 3. Typed physical-close surface

| Map | Domain | Codomain | Status |
|---|---|---|---|
| `A_data_flag` | two data M2 modes plus fresh coherent flag | FSWAP-updated data plus flipped flag | supplied bounded joint call |
| `Q_probe` | prepared four-M2 Choi probe plus diagnostic coupling use | FSWAP-channel support weight | exact finite diagnostic; preparation/effect supplied |
| `K_close` | flag-one and FSWAP-Choi support | completion candidate or locally distinguishable failure | exact on declared common-control domain |
| `R_form` | actualized close candidate satisfying local admissibility | permanent readable Record or undefined | supplied formation/permanence law |

There is no direct arrow from a coherent flag, projector support, circuit
layer, host callback, or diagnostic gate to a framework Record.  There is
also no arrow from any of them to physical time.

## 4. Physical-M2 placement and covariance

The base event/Record dependency motif is

```text
ready (0,0,0)
  |-- data_call (1,0,0) --|
  |-- probe_test(0,1,0) --|-> join(1,1,0) -> completion(1,1,1).
```

Every parent edge has Manhattan length one.  The coherent carriers occupy

```text
data modes:       (2,0,0), (3,0,0),
actuation flag:   (2,-1,0),
probe modes:      (-1,1,0), (-2,1,0),
reference modes:  (-1,1,1), (-2,1,1).
```

The data FSWAP bond, data-to-flag bond, probe FSWAP bond, and both
probe-reference Bell-preparation bonds are nearest neighbor.  The complete
base transducer uses twelve distinct physical M2 sites: five event/Record
sites plus seven coherent data/flag/probe/reference sites.  Its support radius
about the declared origin is four.  This is constant finite overhead for the
two-mode close fixture.

The runner rotates and translates the full role grammar, not merely the data
bond.  All dependency and carrier bonds remain nearest neighbor under every
one of the 24 proper-cubic frames and translation by `(7,-11,13)`.  The matrix
test is direction-independent.  This proves covariance of the supplied finite
motif.  It does not prove autonomous unit-translation generation of its role
labels, origin, preparation, or event law.

Thus the declared audit explicitly covers **all 24 proper-cubic frames**.

## 5. Scheduler, Records, and refinements

The data-plus-flag call and diagnostic probe call have disjoint tensor
support.  They commute, so the two legal linear scheduler orders

```text
ready, data_call, probe_test, join, completion
ready, probe_test, data_call, join, completion
```

give the same joint state and the same successful Record transcript.  The
host order is a replay choice; it is not elapsed time.

Under the supplied candidate `R_form`, successful deterministic close appends
five immutable content-one Records.  Deleting the data-plus-flag call leaves a
local failure transcript with contents

```text
ready=1, data_call=0, probe_test=1
```

and neither `join` nor `completion` forms.  The failure is locally
distinguishable by Record content after `R_form` has been supplied.  Deleting
`R_form` leaves no framework Records even when `Q_close` has unit support.

The runner checks one Record per site, overwrite rejection, permanence, and
content readout in the candidate map.  Coherent carriers are not Records:
the flag, probe, reference halves, projector support, and any reversible copy
remain quantum carriers until the separate actualization law applies.

Record-visible refinements insert `r` nearest-neighbor commits after the base
completion:

```text
r = 0,1,2,5,
Record count = 5+r,
dependency depth = 4+r.
```

The `r=5` case is held out.  Every refinement has two scheduler orders and
zero nonlocal dependency edges.  This held-out refinement is a physical
candidate-transcript change, not evidence for a clock calibration.

## 6. Deletion and fault inventory

### Required declared-coupling deletion

The diagnostic probe remains a successful FSWAP calibration use while the
declared data-plus-flag call is deleted:

| data factor | flag | probe | close weight | completion |
|---:|---:|---:|---:|---:|
| FSWAP | 1 | FSWAP | 1 | yes |
| identity | 0 | FSWAP | 0 | no |

On this declared common-control fault domain:

```text
false positives = 0,
false negatives = 0.
```

This passes the requested physical-coupling deletion test exactly.

### Independent component faults

The stronger adversarial domain allows the three components to fail
independently:

| fault | data factor | flag | probe | close | classification |
|---|---:|---:|---:|---:|---|
| omitted data FSWAP factor; flag/probe survive | identity | 1 | FSWAP | yes | false positive |
| probe omitted | FSWAP | 1 | identity | no | false negative |
| flag omitted | FSWAP | 0 | FSWAP | no | false negative |
| both witness arms omitted | FSWAP | 0 | identity | no | false negative |

The exact count is one false positive and three false negatives.  A bare flag
with both FSWAP uses absent is rejected because the Choi arm has weight zero;
the combined transducer is strictly stronger than a flag alone.  But the
surviving split false positive proves that the tag is not direct evidence of
the data interaction.

### Other deletions

- Delete `probe_test` as a required parent: the declared join contract fails.
- Delete `completion`: no named close is assigned.
- Move completion from `(1,1,1)` to `(1,1,3)`: the join edge becomes nonlocal.
- Delete `R_form`: coherent close support remains, but no Record exists.
- Read data occupation directly before/with FSWAP: the deterministic test
  density has demolition residual `0.25225913414177675`.
- Delete the diagnostic FSWAP while keeping data and flag: completion is a
  false negative, not silently repaired by scheduling.

### Data-only indistinguishability control

For each explicit `+1` eigenstate

```text
|v_0> = |00>,
|v_+> = (|01>+|10>)/sqrt(2),
```

the runner checks

```text
||F |v><v| F^dagger - |v><v||| = 0.
```

Every after-the-fact rule that receives only the final data density therefore
receives the same mathematical input after FSWAP and after identity on these
states.  No such data-only rule can distinguish the two cases on every lawful
input.  The statement is deliberately scoped to final-data-only effects.  A
monitor of an interaction carrier, environment, current, or verified gate
syndrome has extra input and is not ruled out.

## 7. Continuous unitary control and held parameter

For the exact unitary interpolation

```text
V(theta) = cos(theta) I - i sin(theta) F,
```

the Choi acceptance weight is

```text
w_F(V(theta)) = sin(theta)^2.
```

The runner verifies exact agreement at

```text
theta = 0, pi/12, pi/6, pi/4, pi/3, pi/2,
```

and held-out `theta=pi/7`, where

```text
w = 0.18825509907063323.
```

This is an algebraic projector expectation.  **Projector weight is not a Born
probability.**  Turning it into realized frequencies requires a selected
instrument, actualization rule, preparation ensemble, normalization, and
repeated process.  No such probability or rate conclusion is made here.

## 8. Supplied structure and open conditions

The finite witness supplies explicitly:

1. the actual Cycle-230 two-mode FSWAP matrix;
2. a fresh data-side flag and the joint call `F tensor X`;
3. the rule that deleting the declared call deletes both factors;
4. a second diagnostic use of the same named gate;
5. a maximally entangled four-dimensional Choi preparation;
6. the target Choi effect and flag/Choi conjunction;
7. the twelve physical-M2 role sites and five dependency roles;
8. the event parents, origin, orientation convention, and translations;
9. the candidate failure contents and completion condition;
10. the candidate `R_form` actualization, one-site locking, permanence, and
    readout behavior; and
11. the finite fault grammar and unitary interpolation family.

The three collapsed open conditions are:

- `K_link`: derive a physical link making the data interaction, actuation
  flag, and diagnostic evidence fail together strongly enough to exclude the
  split false positive;
- `K_prep`: derive or lawfully supply the local Choi preparation, gate replica,
  comparison effect, and their resetting/availability; and
- `K_form`: derive the event actualization, admissibility, permanent Record
  formation, failure readout, and any repeated-use process.

`K_law` is the umbrella task of selecting one complete physical update and
close law; it is not counted as a fourth independent wall.  The unfinished
global CAR compiler is outside this two-mode close fixture rather than being
used as evidence against the transducer.

## 9. Three-dimensional, time, rate, and Record firewall

Three-dimensional space remains axiomatic input.  Proper-cubic covariance is
spatial covariance only; it is not Lorentz covariance, a boost theorem, or a
four-dimensional spacetime construction.

**Compiler layers are not physical time.**  The two scheduler orders, flag
flip, Choi call, effect evaluation, and Record refinement depth are not
seconds, proper time, a tick rate, a continuous generator, energy, lapse, or
a gravity source.  The record-history time/rate firewall remains intact.

Wrapped phase is not physical energy.  A generator element is not a rate.  A
coherent pointer is not a Record.  A Choi overlap is not an occurrence
frequency.  Nothing here selects a Born rule, state preparation frequency,
source/action, stress tensor, gravity response, or realized cosmological
history.

## 10. TOE dependency ledger after Cycle 259

| Workstream | Cycle-259 effect | Remaining dependency |
|---|---|---|
| `C_ref` | diagnostic reference and phase-coherent Choi preparation are explicit | derive/prepare the reference without silently selecting a global number/phase frame |
| `C_num` | unchanged; the diagnostic uses a supplied full four-dimensional maximally entangled state | physical number-reference/superselection and global CAR state map remain open |
| `C_wrap` | unchanged | no phase-unwrapping, winding history, or physical-energy coordinate |
| `C_int` | gain: actual FSWAP has a bounded nondemolition common-domain deletion-sensitive close proxy | close `K_link`, formation, law selection, full coin/A-B/contact process, and repeated instrument |
| `C_local` | gain: twelve-site M2 motif, NN bonds/dependencies, scheduler and all-frame covariance, held refinement | autonomous role generation, unit-translation law, genuine data-occurrence monitor, and full compiler remain open |
| `C_source` | unchanged | no energy/action/stress/source/gravity-response law |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
Cycle 259 sharpens `C_int`/`C_local`; it does not close physical Record
formation or raise the time/probability lanes.

## 11. Prior-art and novelty boundary

The FSWAP matrix, maximally entangled process-state test, Choi overlap, Lüders
support test, and redundant/controlled-pointer ideas are standard quantum
information machinery.  Local fermionic-gate simulation is also prior art.
Bravyi and Kitaev, *Fermionic quantum computation*, Annals of Physics 298
(2002), 210–226, [arXiv:quant-ph/0003137](https://arxiv.org/abs/quant-ph/0003137),
show bounded-degree nearest-neighbor fermionic gates can be simulated at
constant cost and separate local gate simulation from code-state preparation
in their construction.  That work does not supply this framework's Record
formation or a data-gate occurrence certificate.  Cycle 259 does not claim
novelty for local simulation, Choi testing, or controlled flags.

The fixture-specific contribution is narrower: place the actual Cycle-230
FSWAP inside one executable flag-plus-process-witness close grammar, verify
arbitrary-data nondemolition and all spatial/scheduler controls, and then use
the data-factor-only deletion to classify exactly what its completion does
and does not evidence.  Global priority is not claimed.

## 12. No-go discipline gate

The fresh `origin/main` no-go-discipline text, primitive registry, all current
primitive sources, required phrase search, and relevant no-go ledgers were
checked before fixing the claim boundary.

> **N1-N8 result: PASS for the narrow artifact statement that this displayed
> flag-plus-Choi transducer is not an unconditional certificate of the data
> FSWAP occurrence, because one explicit split fault has unit acceptance.
> FAIL for a universal nondemolition occurrence no-go, minimum physical
> content, shared substrate obstruction, or axiom pressure.**

### N1 — alternative-route enumeration

| Route | Honesty marker | Attempt and disposition |
|---|---|---|
| Cycle-255 fixed completion tag | **ATTEMPTED** | deleting FSWAP leaves its transcript unchanged; Cycle 255 `:319-326` is the exact predecessor failure |
| data-side shared flag alone | **ATTEMPTED** | declared joint-call deletion works, but `I_D tensor X_flag` gives a false positive if the data factor fails independently |
| prepared one-particle sentinel | **ATTEMPTED** | `F|10>=|01>` distinguishes `F` from identity without touching data, but certifies only the replica on one input |
| full Choi process witness | **ATTEMPTED** | `Tr F=0` gives exact identity rejection and unit target acceptance, but it certifies the diagnostic invocation, not the data invocation |
| combined flag plus Choi witness | **ATTEMPTED** | closes the declared common-control deletion test; the explicit data-factor-only split fault still passes |
| direct data occupation/readout | **ATTEMPTED** | produces nonzero demolition residual `0.25225913414177675`; moreover FSWAP and identity have identical final data on `|00>` and the symmetric one-particle state, so final-data-only certification cannot cover every input |
| deterministic unitary under-rotation diagnostic | **ATTEMPTED** | the Choi weight follows `sin^2(theta)` and resolves the probe channel, but still inherits the data/probe link condition |

The intrinsic interaction-monitor route in N7 remains untested and is not
misreported as an N1 attempt or prior no-go.  Its viability makes the
universal negative fail, while the exact split-fault classification of this
artifact stands.

### N2 — condition-independence audit

The collapsed component conditions are `K_link`, `K_prep`, and `K_form`.
`K_law` is their possible joint supplier and is not an independent wall.

| Pair | First closes second? | Second closes first? | Independent in fixtures? |
|---|---:|---:|---:|
| `K_link`,`K_prep` | no: a common-failure interaction need not prepare a Choi state | no: a Choi state does not couple a data invocation to its flag | yes |
| `K_link`,`K_form` | no: correlated coherent dynamics need not actualize Records | no: a Record law can actualize an unfaithful flag | yes |
| `K_prep`,`K_form` | no: a prepared diagnostic can remain coherent and unread | no: a formation law does not prepare the target process state | yes |

The flag, Choi effect, and common-control declaration are not counted as three
separate walls inside `K_link/K_prep`; their component deletions are acceptance
tests.  Actualization, permanence, and failure readout stay folded into
`K_form`.

### N3 — hidden-condition scan

| Phrase or possible hidden condition | Classification |
|---|---|
| “physical call” | supplied joint law `F_D tensor X_flag`; factor-failure correlation remains `K_link` |
| “same gate” | named FSWAP on data and probe; device identity and common-mode behavior are supplied |
| “Choi witness” | prepared four-M2 process test with supplied effect; not a foundation primitive |
| “completion” | deterministic candidate after `Q_close`; Record only after `R_form` |
| “failure” | supplied actualized local content zero; not inferred from an unread coherent flag |
| “nondemolition” | exact reduced-data and factorization residuals for arbitrary finite density input |
| “local” | twelve explicit sites, NN declared bonds, radius four; no homogeneous-law theorem |
| “gate-faithful” | exact only on the two-case common-control fault domain |
| “weight” | Hilbert projector expectation; not probability or frequency |
| “three-dimensional” | direct Lattice-axiom input, not a result |

The mandatory phrases “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,” “obviously,”
“standard QFT,” “registered,” and “canonical” were scanned.  Any audit-list
occurrence is non-load-bearing.  Every scientific input is in the supplied
inventory.

### N4 — residual matching

| Witness | Exact residual there | Cycle-259 use | Match? |
|---|---|---|---:|
| Minimal Axioms `:63-115` | Records/permanence supplied; formation choice, dynamics, measurement, probability, and time metric absent | types `R_form` while keeping its selection open | yes |
| pointer-formation theorem `:41-137,181-225` | controlled copies are sufficient only under supplied pointer/fragment/readout conditions and may remain reversible | prevents coherent flag/Choi carriers from being renamed Records | yes |
| Cycle 230 `:323-350` | coherent interaction does not prepare, occur, write Records, or yield a rate | restricts the close to the two-mode gate fixture | yes |
| Cycle 243 `:162-186` | event, physical close, commit, and Record are separate maps | supplies the exact typed seam targeted here | yes |
| Cycle 255 `:298-326,448-477` | fixed nondemolition tag survives FSWAP deletion | replaced by a deletion-sensitive joint-call tag; split-fault seam retained | yes |
| Cycle 257 `:48-52,435-496` | faithful nondemolition transducer is a live target | executes that finite target independently of compiler closure | yes |
| Bravyi–Kitaev 2002 | local fermionic simulation and preparation resources | prior-art boundary only; no occurrence/Record evidence | no as negative witness; not used as one |

No compiler failure, mass residual, gravity wall, or Born wall is used as
evidence against occurrence certification.

### N5 — rhetoric and resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| one two-mode FSWAP matrix | exact gate, Choi, local-code, arbitrary-density demolition, and two invariant-state data-only controls | full Cycle-230 coin/contact update |
| one declared joint data-plus-flag call | present/deleted truth table, zero false positives/negatives | arbitrary internal component faults |
| one diagnostic replica | full promised-unitary channel effect | identity of every physical invocation |
| one twelve-site motif | NN bonds/dependencies, scheduler, translation, all 24 frames | autonomous homogeneous full-lattice law |
| one split-fault family | one false positive, three false negatives | all noise, correlated faults, or fault-tolerant schemes |
| refinement family `0,1,2,5` | exact Record count/depth and locality | metric time or indefinite renewal |
| full spatial lattice | not tested as a process | universal occurrence no-go, Lorentz closure, continuum limit |

“Not genuine occurrence evidence” is always narrowed to this displayed
transducer on the independent-component fault grammar.  The note does not say
that nondemolition occurrence evidence is impossible in general.

### N6 — partial-closure and primitive scan

The current primitive registry and all three current primitive sources were
read.  None supplies a gate monitor, Choi preparation, common-failure theorem,
formation map, sampling law, or probability interpretation.  These remain
construction targets rather than proposed axioms.

| Constructive path | Status | Could close |
|---|---|---|
| derive an intrinsic pointer coupled to the same interaction term rather than a tensor-product actuation flag | live finite Hamiltonian route | `K_link` split false positive |
| route data and Choi probe through the same physical bond with invocation-level fault audit | untested finite comb | strengthen device identity; invocation-specific faults remain to test |
| verified/fault-tolerant FSWAP gadget with syndrome tied to the logical data action | live coding route | bounded fault family under an explicit noise model |
| multiple independent sentinels and majority/consistency Record | finite redundancy route | selected fault tolerance, not universal faithfulness |
| derive local Choi/sentinel preparation from a lawful recurrent apparatus | live preparation route | `K_prep` |
| construct absorbing actualization and failure Records under one local admissibility law | live Record route | `K_form` |
| generate the role grammar autonomously under translations and frames | open lattice-law route | remove supplied origin/role marker |

These are import-retirement paths.  None automatically requires a new axiom.

### N7 — steelman

> A hostile reviewer should reject any general occurrence no-go.  The present
> false positive exists because the author chose a separable call
> `F_D tensor X_flag` and a spatially distinct diagnostic invocation.  A
> physical Hamiltonian could couple a pointer to an interaction-current or
> ancilla syndrome that is generated only by the same data transition; a
> verified gate gadget could then prove, for a declared local noise family,
> that acceptance implies the logical FSWAP channel.  Alternatively, route a
> known Choi probe and the unknown data through the same reusable bond and
> audit invocation faults with redundant checks.  Cycle 243 leaves exactly
> this physical-close law open, and the 2026-06-05 pointer theorem shows that
> nontrivial local nondemolishing imprint channels exist under explicit
> hypotheses.  Cycle 259 has not exhausted those constructions.

This steelman is convincing.  The broad no-go fails.  Only the exact
split-fault classification of the displayed transducer is retained.

### N8 — cross-cycle echo

The required repository phrase search and physics-loop `NO_GO_LEDGER.md`
surfaces were checked.  The closest echoes are:

| Earlier boundary | Later/live mechanism | Cycle-259 response |
|---|---|---|
| coherent pointer copy is not automatically a Record | supply actualization, permanence, and readout bridge | keeps `R_form` explicit |
| Cycle-243 event is not physical close | attach a separate local close transducer | constructs one bounded conditional instance |
| Cycle-255 fixed tag survives gate deletion | make completion depend on a coupling-sensitive carrier | flag/Choi conjunction passes joint-call deletion |
| compiler depth is not physical time | use only physical Records after formation | preserves the time/rate firewall; makes no clock claim |
| earlier reference/sign walls retired by coherent enlargement | add coherent diagnostic resources, then audit their preparation | uses Choi resources without pretending they are free or actualized |
| apparent local compiler closures failed under wider fault/sector tests | expand the lawful domain before claiming closure | common-control success is immediately retested under split faults |

The same “change representation, then expose the new resource” mechanism that
retired earlier walls remains live.  Cross-cycle evidence therefore argues
against axiom pressure.

## 13. Disposition and optimal next probe

**Retain:** the exact FSWAP Choi orthogonality, arbitrary-data nondemolition,
joint-call deletion sensitivity, zero common-domain false positive/negative
counts, bounded twelve-M2 placement, scheduler and all-frame covariance,
held-out refinement, local failure transcript, and explicit split-fault
counterexample.

**Do not claim:** unconditional evidence that the data FSWAP occurred, a
selected physical formation law, autonomous role generation, a global CAR
compiler, physical time, a rate, energy, Born frequency, source, gravity
response, or axiom consequence.

The optimal next probe is an intrinsic-link tournament.  Compare at least:

1. a Hamiltonian interaction-current pointer coupled to the actual FSWAP
   bond;
2. a same-bond two-query Choi/data comb with invocation-specific deletions;
3. a verified local FSWAP gadget with an explicit bounded fault family; and
4. a fully local absorbing `R_form` continuation that turns only the verified
   syndrome into a permanent Record.

Demand the same data-factor-only deletion used here.  If a candidate accepts,
the data reduced channel must remain exactly FSWAP; if the data interaction is
omitted while every auxiliary control survives, completion must still fail.
Only that stronger test can upgrade the close from trusted shared-control to
genuine occurrence evidence on the declared fault family.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/gate_faithful_fswap_physical_close_cycle259_2026_07_17.py

SUMMARY PASS 22 FAIL 0
```
