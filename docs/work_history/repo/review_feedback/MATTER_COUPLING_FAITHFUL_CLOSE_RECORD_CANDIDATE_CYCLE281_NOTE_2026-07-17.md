# Matter-coupling-faithful close / Record candidate — Cycle 281

**Date:** 2026-07-17

**Type:** exact bounded same-code positive-contact close with reversible
archive, coupling-mediated reset, and split-deletion audit

**Status:** faithful to deletion of either declared `U_I` invocation on the
blank-interface lawful domain; not faithful to arbitrary factor replacement,
not occurrence, not permanence, and not Record formation

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface. It stays on the exact Cycle-278 connected edge code and same physical
pointer; it does not splice Cycle 251.

## Result up front

Cycle 281 closes the exact split deletion failure found in Cycle 279 for the
**positive contact branch** of the Cycle-278 physical instrument. The result
has bounded support and constant overhead and is audited under all 24
proper-cubic frames.

At one connected-edge-code cell let

```text
Q_x = 1_(N_x >= 2)
```

be the actual Cycle-278 contact-active projector and let the same physical
pointer `P` start in `|0>`. The exact matter-pointer interaction is

```text
U_I = (I-Q_x) tensor I_P + Q_x tensor X_P.
```

Add four ordinary physical `M_2` carriers:

```text
A       reversible archive/environment
C       positive-contact CLOSE carrier
H       reversible history export
F       one supplied fresh continuation target
```

On the declared blank interface, the base **couple–archive–recouple** order is

```text
U_I^(write)
 -> CNOT(P,A)
 -> U_I^(reset)
 -> X_C controlled by (A=1,P=0)
 -> X_H controlled by (A=1,C=1).
```

Writing ancilla states in the order `(P,A,C,H,F)`, the exact isometry is

```text
V_close = (I-Q_x) tensor |00000>
        + Q_x     tensor |01110>.
```

Consequently,

```text
V_close^dagger (I tensor 1_(C=1)) V_close = Q_x,
V_close^dagger (I tensor 1_(H=1)) V_close = Q_x,
V_close^dagger (I tensor 1_(P=1)) V_close = 0.
```

The existing pointer is reset by the **second actual matter-pointer
interaction**, not by a supplied `DONE` token. Deleting the first `U_I`, the
second `U_I`, or both, while leaving every archive, close, and history gate
alive, makes the close and history effects exactly zero. The false `NO` close
of Cycle 279 cannot occur because this construction has no silence-to-no or
pointer-zero-to-close path. Deleting the archive writer also makes close zero.

This is the strongest retained constructive claim:

```text
actual Q_x-controlled write
 + archived positive signal
 + actual Q_x-controlled reset
 + agreement close
   = deletion-faithful coherent positive-contact close
     on the declared blank-interface fault domain.
```

It is deliberately **not** a two-outcome close. Since `U_I` acts exactly as
identity on `Q_x=0`, a no-contact input is identical under the ideal coupling
and its deletion. Silence cannot certify that the coupling was present.
Therefore `Q_x=0` remains open rather than being turned into a false negative
fact.

The construction also does not pass an unrestricted replacement fault. If
one `Q_x`-controlled call is replaced by unconditional `X_P`, the positive
close effect is still `Q_x` although the full packet and final-pointer effects
are wrong. If both calls are so replaced, all seven inactive intrinsic states
falsely close. This explicit boundary prevents “deletion faithful” from being
inflated into “occurrence faithful under every fault.”

The complete construction is reversible. Reconnecting the inverse erases the
archive, close, and history exactly. A controls-only continuation can copy
`H` into fresh `F` without changing the old history effect, but the no-target
restriction and fresh capacity are supplied. The candidate is not a Record.

There is no shared obstruction and no axiom pressure.

## 1. Exact same-code constructor

Cycle 278 already represents `Q_x` as a 64-term Walsh polynomial in the six
mapped connected-edge-code occupation-parity operators

```text
B_(x,d)=(-1)^(n_(x,d)),  d=0,...,5.
```

Every term commutes with the local checks and all three Wilson operators. The
six `B` supports have an 18-M2 union, and cancellation bounds every `Q_x`
Pauli word at weight 12. Adding the carried pointer to a controlled term gives
maximum weight 13.

Cycle 281 changes none of that matter code. It adds the existing pointer plus
four scalar interface M2 carriers. Thus the declared block has:

| item | exact result |
|---|---:|
| connected-code matter support union | `18 M2` |
| complete pointer/archive/close/history/fresh interface | `5 M2` |
| total bounded neighborhood | `23 M2` |
| overhead beyond the Cycle-278 pointer | `4 M2` |
| maximum `Q_x` Pauli weight | `12` |
| maximum `U_I` polynomial-term weight | `13` |
| local-check leakage | `0` |
| Wilson transitions | `0` |

The two `U_I` uses have the same operator and same pointer. They are two
declared calls in the finite close circuit, not two independent diagnostic
replicas. Their circuit order is supplied process order; compiler order is not
physical time.

The archive/close controls are bounded M2 gates on the interface. Their exact
nearest-neighbour synthesis, placement by one homogeneous microscopic law,
blank preparation, and autonomous invocation order remain supplied. No new
auxiliary gauge code is introduced: the only code constraints tested are the
actual connected-edge local checks, while the interface uses ordinary M2
sites with a declared blank boundary.

## 2. Why the close is coupling-deletion faithful

On the active subspace, the ideal truth path is

| stage | `P` | `A` | `C` | `H` |
|---|---:|---:|---:|---:|
| blank | 0 | 0 | 0 | 0 |
| first `U_I` | 1 | 0 | 0 | 0 |
| archive | 1 | 1 | 0 | 0 |
| second `U_I` | 0 | 1 | 0 | 0 |
| close/export | 0 | 1 | 1 | 1 |

The close requires both a positive archived write and a reset pointer. This
gives the following exact deletion table while all unmentioned auxiliary
gates survive:

| fault | final active-path condition | close-effect norm | history-effect norm | isometry residual from ideal |
|---|---|---:|---:|---:|
| delete first `U_I` | no archive signal; second call leaves `P=1` | `0` | `0` | `10.677078252031311` |
| delete second `U_I` | archive is one but `P` never resets | `0` | `0` | `10.677078252031311` |
| delete both `U_I` | blank interface remains blank | `0` | `0` | `10.677078252031311` |
| delete archive writer | reset succeeds but `A=0` | `0` | `0` | `10.677078252031311` |
| delete close writer | no close/history | `0` | `0` | nonzero |
| delete history writer | close remains; no history export | `||Q_x||_F=sqrt(57)` | `0` | nonzero |

This is stronger than Cycle 279's auxiliary `DONE` path: there is no close
ancestor that can fire after both matter-pointer couplings are removed.

It is still conditional on the declared fault grammar. The following stronger
replacements are tested, not hidden:

| replacement | full-isometry residual | `||close-Q_x||_F` | final-pointer-effect norm | inactive false-close rank |
|---|---:|---:|---:|---:|
| first call becomes unconditional `X_P` | `3.7416573867739413` | `0` | `2.6457513110645907` | `0` |
| second call becomes unconditional `X_P` | `3.7416573867739413` | `0` | `2.6457513110645907` | `0` |
| both calls become unconditional `X_P` | `3.7416573867739413` | `2.6457513110645907` | `0` | `7` |

On `Q_x=1`, one controlled `X_P` and one unconditional `X_P` have the same
action. Therefore the single-replacement row cannot be promoted into an
occurrence certificate by inspecting only the positive close bit. The full
packet exposes it on the complete lawful matter domain through the residual
pointer/archive state, but no actual fault has thereby been selected by the
framework.

## 3. Contact, mass, and conditional-state controls

The close effect equals the support projector of the actual Cycle-230 contact
generator `binom(N_x,2)`. This is not called physical energy. At the intrinsic
64-dimensional cell resolution the runner obtains

```text
||[Q_x,Gamma(C_beta=-0.3)]||_F = 0,
||[Q_x,W_(g=0.37)]||_F            = 0,
||[Q_x,Gamma(A)]||_F              = 0.
```

`Q_x=0` on `N_x<=1`, so the complete blank-interface close circuit acts as
identity on the local one-particle sector and gives close weight zero there.
The Cycle-219/230 analytic-versus-numerical mass fixture remains preserved.
This does not embed the odd one-particle state into the total-even connected
code.

For the three Cycle-278 local reductions the ideal and split-deleted close
weights are:

| state family | ideal close weight | delete first `U_I` |
|---|---:|---:|
| uniform | `57/64 = 0.890625` | `0` |
| matched `B_0=+1` | `13/16 = 0.8125` | `0` |
| matched `B_0=-1` | `31/32 = 0.96875` | `0` |

These are ordinary trace diagnostics on supplied density operators. They are
not frequencies, occurrence probabilities, or a Born derivation.

For the coherent held input

```text
(|N=0> + |N=2>)/sqrt(2),
```

the joint output remains one pure coherent state, the close weight is `1/2`,
and no branch is selected. Restricting the archive gives exactly the Lüders
dephasing channel with residual zero. Reconnecting the inverse restores the
input with residual zero.

## 4. Covariance, sizes, and lawful domain

The runner rebuilds the actual connected-edge code at

```text
L=3,4,5,6,
```

with `L=6` held out. Every size has the same 18-M2 matter support, five-M2
interface, 23-M2 total neighborhood, 64 nonzero Walsh terms, and zero
local-check/Wilson leakage.

At `L=3`, every one of the 24 proper-cubic frames is combined with all 27
translations. The 648 exact tests preserve the six-`B` family at the moved
cell, the local-check family, and the Wilson center. `Q_x` is a scalar because
it depends only on total occupation. `P,A,C,H,F` are carried scalar roles, so
the supplied close rule has no preferred direction. This is covariance of the
bounded operator/interface family, not derivation of its microscopic
scheduler or physical placement law.

The lawful domain is:

1. the Cycle-278 connected edge code, its total-even matter algebra, and the
   contact projector at one declared cell;
2. one existing pointer and four additional ordinary M2 carriers, all blank;
3. two declared invocations of the exact same `U_I` and the displayed bounded
   reversible auxiliary gates;
4. even matter inputs, including arbitrary coherent superpositions across
   the `Q_x` sectors; and
5. finite periodic sizes `L>=3` for the code/covariance controls.

The runner rejects `L<3`, a non-five-M2 interface, and a nonblank interface.
Odd/full-Fock encoding, global state preparation, arbitrary nonblank
apparatus states, post-wrap whole-process equality, autonomous placement, and
arbitrary faults are outside the claim.

## 5. Correlation, read, occurrence, close, permanence, and Record

| interface | what Cycle 281 has | what remains |
|---|---|---|
| coherent correlation | exact pure `V_close` isometry | no branch is chosen |
| supplied read | mathematical effects for `C,H` and ordinary trace pairing | no selected physical reader or read law |
| occurrence | none | a law selecting one actual branch/history |
| close | exact positive-contact coupling-deletion-faithful carrier on the declared domain | no faithful negative close or arbitrary-replacement certificate |
| permanence | old `H` is unchanged by one supplied controls-only export | unrestricted inverse erases it; continuation restriction and fresh capacity are imported |
| Record | none | actualization plus framework Record-formation map and permanent content |

Coherent correlation is not a supplied read. Close is not occurrence.
Conditional archive stability is not permanence. The candidate is not a
Record.

The physical pointer reset is explicit: the second actual `U_I` returns `P`
to zero on the ideal path. Reset resources beyond that are also explicit. The
archive, close, history, and fresh carrier are consumed; reusing the complete
interface requires either inverse reconnection, which erases the candidate,
or new blank carriers. No thermodynamic erasure, absorbing dynamics, or
unbounded fresh capacity is derived.

## 6. Supplied-structure inventory

| supplied structure | role | not derived here |
|---|---|---|
| Cycle-269/271 connected edge code and local-check signs | physical matter substrate | microscopic law selecting that code |
| Cycle-278 64-term `Q_x` and same physical pointer | actual contact instrument | autonomous instrument placement |
| two uses of `U_I` | write and pointer reset | invocation schedule or indivisible event identity |
| blank `P,A,C,H,F` | dilation boundary and capacity | local preparation/reset law |
| pointer-to-archive controlled XOR | reversible environment | irreversible fact formation |
| archive/reset agreement close | positive close | occurrence or branch selection |
| history and fresh export gates | conditional append path | permanence or indefinite capacity |
| controls-only continuation grammar | keeps old history off target list | unrestricted lawful future dynamics |
| ordinary trace/effects | reports exact weights | physical read, Born law, or frequencies |
| deletion and pointer-only replacement grammar | adversarial test domain | framework-selected physical fault law |
| circuit order and one declared cell | evaluation context | physical time, rate, or homogeneous origin selection |

No phase is called physical energy, no generator element is called a rate,
and no archive size is called a source. No gravity response, lapse, stress,
or resource-to-geometry law is added. No Thirring engine is used or compared.

## 7. Exact residual ledger

| diagnostic | cold-run value |
|---|---:|
| isometry Gram error | `0` |
| ideal-packet intertwiner error | `0` |
| close effect minus `Q_x` | `0` |
| history effect minus `Q_x` | `0` |
| final pointer-one effect norm | `0` |
| full inverse/reconnection residual, held vector | `0` |
| held coherent reduced-dephasing residual | `0` |
| held coherent close weight | `0.4999999999999999` |
| maximum close/history effect after any declared coupling deletion | `0` |
| minimum deleted-isometry residual | `10.677078252031311` |
| single pointer-only isometry residual | `3.7416573867739413` |
| single pointer-only final-pointer-effect norm | `2.6457513110645907` |
| double pointer-only inactive false-close rank | `7` |
| `Q_x`/actual coin-contact-reversal commutators | `0` |
| local-check/Wilson leakage, `L=3,4,5,6` | `0` |
| proper-cubic/frame-translation failures | `0 / 648` |
| controls-only history-change/export residuals | `0 / 0` |

The matrix tolerance is `3e-11`. Operator statements are checked by complete
64-column isometries or exact code algebra, not inferred from random states.
The held random vector, held coherent cross-sector vector, and held-out `L=6`
are regressions in addition to those complete tests.

## 8. TOE dependency ledger

| wall | Cycle-281 effect | remaining dependency |
|---|---|---|
| `C_ref` | blank pointer/archive references and their reset costs are fully inventoried | derive their preparation, placement, fresh capacity, and continuation from one law |
| `C_num` | unchanged exact `Q_(N>=2)` close effect; one-particle sector protected | odd/full-Fock same-code embedding and lawful preparation |
| `C_wrap` | bounded local close is size independent through held-out `L=6` | global preparation and arbitrary wrapped process remain outside the theorem |
| `C_int` | real gain: the positive close vanishes if either actual matter-pointer invocation is deleted while auxiliaries survive | arbitrary-replacement faithfulness, negative close, physical read, occurrence, and law selection |
| `C_local` | 23-M2 bounded covariant block with zero connected-code leakage | selected nearest-neighbour synthesis, autonomous scheduler, and homogeneous placement |
| `C_source` | unchanged | no energy/action/stress/source/lapse/metric response is selected |

Maturity scores remain deliberately conservative:

| lane | score | Cycle-281 reason |
|---|---:|---|
| operational quantum / Records | `2/5` | deletion-faithful positive close is new, but occurrence, unrestricted permanence, and Record formation remain absent |
| causal time | `1/5` | explicit ancestry only; no duration, recurrence, comparison, or rate law |
| inertia / matter | `3/5` | actual contact support and mass fixture stay joined on the connected code; odd/full-Fock preparation remains open |
| gravity / source | `2/5` | resource carriers are counted, but no source or geometry response is derived |
| Born / probability | `1/5` | exact trace weights only; no actual member or frequency theorem |

## 9. Full no-go discipline N1–N8

The main result is constructive. The negative boundaries apply only to this
finite blank-interface constructor and its tested fault families. They do not
support an impossibility theorem, minimum-content theorem, shared substrate
obstruction, or axiom-pressure claim.

### N1 — alternative-route enumeration

| route | honesty marker | disposition |
|---|---|---|
| retain the Cycle-278 single coherent pointer | **ATTEMPTED** | exact instrument, but no close/reset/history packet |
| Cycle-279 auxiliary `DONE/fact/UNCOMPUTED` path | **ATTEMPTED** | closes after both data couplings are split-deleted; rejected for this target |
| same-pointer couple–archive–recouple echo | **ATTEMPTED** | succeeds: exact `Q_x` close, pointer reset, history export |
| delete only first actual `U_I` | **ATTEMPTED** | close/history effects become zero while auxiliaries survive |
| delete only second actual `U_I` | **ATTEMPTED** | close/history effects become zero while auxiliaries survive |
| replace one controlled call by unconditional pointer `X` | **ATTEMPTED** | positive close effect is unchanged but full packet/pointer is wrong; stronger occurrence claim rejected |
| replace both controlled calls by pointer `X` | **ATTEMPTED** | seven inactive states falsely close; arbitrary-replacement faithfulness rejected |
| controls-only fresh-carrier export | **ATTEMPTED** | preserves history effect exactly under a supplied target restriction |
| unrestricted inverse reconnection | **ATTEMPTED** | erases every candidate carrier exactly; unconditional permanence rejected |

Live routes include an indivisible substrate interaction with an intrinsic
syndrome, an absorbing export dynamics, a physical read/actualization map, and
a separately interacting negative-contact witness. These are unfinished
constructive routes, not evidence for a constitutional obstruction.

### N2 — wall-independence audit

The remaining conditions are collapsed to:

- `W_D`: deletion faithfulness of the positive close;
- `W_S`: stronger substitution/indivisible-invocation faithfulness;
- `W_A`: actual branch/history selection;
- `W_R`: unrestricted permanence, reset, and fresh capacity; and
- `W_B`: physical read plus repeated Born/frequency semantics.

| pair | first closes second? | second closes first? | independent here? |
|---|---:|---:|---:|
| `W_D/W_S` | no | no | yes |
| `W_D/W_A` | no | no | yes |
| `W_D/W_R` | no | no | yes |
| `W_D/W_B` | no | no | yes |
| `W_S/W_A` | no | no | yes |
| `W_S/W_R` | no | no | yes |
| `W_S/W_B` | no | no | yes |
| `W_A/W_R` | no | no | yes |
| `W_A/W_B` | no | no | yes |
| `W_R/W_B` | no | no | yes |

Examples fix the separation. Deletion fidelity does not reject a surviving
pointer-only substitute. A perfect coherent close does not choose a branch.
An actual branch can still be erased. A permanent one-shot fact supplies no
reader, recurrence, or frequency law. Archive, close, and history bits are
components of `W_D/W_R`, not independent walls multiplied by naming.

### N3 — hidden-condition scan

| phrase or condition | explicit classification |
|---|---|
| “same code” | exact Cycle-269/271/278 connected edge code, not Cycle 251 |
| “same physical pointer” | the same pointer role and `U_I`; two supplied invocations |
| “faithful” | only first/second/both `U_I` deletion on the blank interface |
| “close” | support of one coherent carrier, not occurrence or Record |
| “reset” | second `U_I` resets `P`; full interface needs inverse or fresh blanks |
| “archive/environment” | reversible orthogonal carrier, not irreversible history |
| “fresh” | one supplied blank target, not unbounded capacity |
| “permanent” | not claimed; old-history stability uses a controls-only grammar |
| “weight” | trace diagnostic, not realized probability or rate |

The required phrase scan found no load-bearing “by construction,” “as is
standard,” “the framework provides,” “canonical,” “naturally,” “obviously,”
“registered,” “background,” or “standard QFT” premise. Every blank, gate,
order, state, effect, continuation restriction, and fault rule is in the
supplied ledger.

### N4 — residual matching

| prior witness | exact residual there | Cycle-281 relation | match? |
|---|---|---|---:|
| Cycle 278 | same-code `Q_x` pointer; deletion gives zero pointer-one weight; no close/reset | uses that exact `Q_x`, code, pointer, weights, support, and covariance | yes |
| Cycle 279 | `DONE/fact` route falsely closes with unit weight after split data-coupling deletion | removes `DONE`; deletion of either coupling leg now gives zero close | yes |
| Cycle 209 | finite causal ancestry can close without timeout while Record transition stays supplied | agreement close has bounded gate ancestry and no silence-to-no path | yes for close boundary |
| Cycle 259 | a common-control flag is spoofed when data factor alone is removed | pointer-only substitution rows preserve the stronger fault warning | yes |
| Cycle 266 | exact nondemolition unitary data channel can have input-independent complementary carrier on a prepared subspace | no universal occurrence claim is inferred from the reversible archive | yes for scope |
| Cycle 251 | different physical code | no proof role or splice | excluded |

No gravity, mass, compiler, or probability residual is reused as evidence for
Record impossibility.

### N5 — resolution and rhetoric audit

| resolution | tested statement | forbidden inflation |
|---|---|---|
| intrinsic six-mode cell | complete 64-column close isometry and fault effects | all matter interactions |
| one connected physical-code cell | 18 matter plus five interface M2 | globally selected apparatus law |
| declared coupling deletion | either/both actual call omissions | arbitrary factor replacement or every physical fault |
| all proper-cubic frames | scalar operator/interface covariance | derived scheduler or preferred-origin removal |
| finite sizes | `L=3,4,5,6`, with held-out `L=6` | arbitrary global preparation/wrapped histories |
| one fresh export | exact history preservation under controls-only rule | unlimited capacity or thermodynamic arrow |
| occurrence/Record | not tested or claimed | universal Record no-go |

“Matter-coupling faithful” therefore means deletion faithful on the declared
positive-contact close domain. It does not mean that one close bit proves the
microscopic invocation against arbitrary replacements.

### N6 — partial-closure path scan

This cycle is itself a partial closure: it keeps every Cycle-278 matter/code
fixture fixed, removes the independent `DONE` path, and makes the pointer
reset part of the actual coupling ancestry. Further constructive paths are:

1. synthesize the bounded interface and both calls from one covariant local
   admissibility rule;
2. make the matter action and close syndrome one verified indivisible update;
3. supply a physical negative-contact probe rather than treating identity as
   evidence;
4. export into an absorbing but resource-accounted local carrier process;
5. derive branch actualization and Record formation separately; and
6. add recurrence/readout before asking for clock or frequency semantics.

None of these paths automatically requires a new axiom.

### N7 — steelman

> A hostile reviewer should say the result is a useful deletion detector but
> not yet an occurrence link. The constructor queries the same controlled
> involution twice. On the active subspace, replacing either query by an
> unconditional pointer flip is observationally identical to the intended
> query at the close bit, so the positive close can authenticate its declared
> omission grammar but not the physical factorization of the invocation. The
> author also supplies blank carriers, call order, archive gates, and a
> controls-only future. A homogeneous indivisible local update could do
> better by generating matter action and syndrome in one physical transition,
> while an absorbing export or actual-history law could address permanence
> and actuality. Nothing here rules those routes out.

The steelman is accepted. The result is retained as an exact constructive
deletion-faithful close and the replacement, actuality, and permanence seams
remain open.

### N8 — cross-cycle echo

Cycles 223–226 repeatedly showed that coherent copies, reduced dephasing,
fine archives, and permanent Records are distinct. Cycles 259/262/266 showed
that auxiliary evidence can survive a data-factor split and that this is not
a substrate-wide no-go when physical indivisibility remains open. Cycle 278
then produced the first exact same-code contact pointer, and Cycle 279 exposed
its false auxiliary close.

Cycle 281 follows the campaign's productive pattern: preserve the proven
substrate, place the missing dependency in the actual interaction ancestry,
test the stronger fault that still survives, and keep every residual import
named. Earlier walls were narrowed by explicit constructors rather than
constitutional edits. The same evidence argues against axiom pressure here.

**N1–N8 status: PASS for the narrow constructive and negative boundaries.**

## 10. Disposition and optimal next campaign

Retain:

- the exact same-code `Q_x` close isometry;
- reset of the same Cycle-278 pointer by a second actual `U_I` use;
- zero close/history support under deletion of first, second, or both coupling
  legs with all auxiliaries alive;
- exact `57/64`, `13/16`, and `31/32` close weights;
- bounded 23-M2 support, zero code leakage, held-out `L=6`, and all-24/full-27
  covariance;
- reversible archive/reconnection and explicit fresh-export resource; and
- the pointer-only replacement countercontrol.

Do not claim:

- a faithful no-contact close;
- arbitrary-fault or invocation-independent occurrence certification;
- an autonomous read, actual branch, permanent Record, repeated clock, or
  Born-frequency law;
- a selected nearest-neighbour microscopic apparatus law;
- physical energy, rate, gravity source, or metric response; or
- a shared obstruction, minimum-content theorem, or axiom pressure.

The optimal next campaign is an **indivisible contact-action/syndrome
tournament on this same connected code**. Candidate local updates should make
the matter action and close syndrome one verified block, audit whether the
pointer-only replacement is a lawful factor deletion, and compare an
absorbing fresh-carrier export against complete reversible reconnection. The
actuality/Record map must remain a separate lane.

## Verification

Run:

```bash
python3 scripts/matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17.py
```

The runner must finish with zero failures. PASS totals are regression
assertions, not counts of independent physical predictions.
