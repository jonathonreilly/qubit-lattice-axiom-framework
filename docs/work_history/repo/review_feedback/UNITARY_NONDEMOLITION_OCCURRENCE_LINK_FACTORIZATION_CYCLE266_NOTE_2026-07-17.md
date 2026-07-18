# Unitary nondemolition occurrence-link factorization — Cycle 266

**Date:** 2026-07-17

**Type:** exact finite factorization theorem plus maximal-inseparability
constructor and conditional split-fault classification

**Status:** exact on a prepared-environment input subspace for arbitrary data;
not a substrate-wide occurrence no-go

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

Companion runner:

```text
scripts/unitary_nondemolition_occurrence_link_factorization_cycle266_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit surface.

## Result up front

Cycle 266 constructs a deliberately strong finite challenge to the simple
“the environment must factor because the data is unitary” intuition. The
actual Cycle-230 two-mode FSWAP acts on two data `M_2` sites, and four more
`M_2` sites form a coherent environment/history carrier. One supplied joint
unitary `W` on this six-site block has the **maximum possible
data/environment operator-Schmidt rank, 16**. It is genuinely entangling on
unprepared environment inputs and is not a tensor product as a full joint
unitary.

Nevertheless, on the declared prepared-environment input subspace,

```text
W (|psi>_D tensor |0000>_E)
    = FSWAP |psi>_D tensor |GHZ_4>_E
```

for every two-mode data vector. The prepared-subspace factorization and target
leakage residuals are zero to exact matrix precision. Thus making the full
joint update maximally inseparable does not evade the finite Stinespring fact:
if tracing the environment gives exactly the unitary channel
`rho -> F rho F^dagger` for every input, then the corresponding pure-
environment isometry has Kraus rank one and must be

```text
V |psi> = F |psi> tensor |e>
```

for one input-independent environment state `|e>`. This claim concerns the
isometry obtained by restricting the full update to the prepared environment;
the full joint unitary need not factorize.

Cycle 266 then applies the exact Cycle-259/Cycle-262 stress test. If one admits
the **conditional adversarial split-factor fault**

```text
F |psi> tensor |e>  ->  |psi> tensor |e>,
```

then every effect or instrument confined to the environment has identical
ideal and faulty outputs. The runner gives an explicit unitary completion of
that split replacement for the displayed constructor. The data channel is
wrong on held lawful inputs while the coherent carrier and its leakage remain
unchanged.

This fault classification is conditional and critical: the replacement may
not be a lawful deletion of an indivisible substrate update. If the physical
law makes `W` one indivisible event and its verified fault domain excludes
branchwise `F -> I` replacement, a constant environment flag may be faithful
within that physical domain. The theorem does not derive the split fault from
the framework and does not rule out that route.

The exact boundary extends to a finite mixed environment by purification: an
exact unitary reduced data channel still has a constant complementary output
on environment plus reference. The runner also supplies an explicit rank-two
mixed example and nonprojective environment instruments. Conversely, a held
two-history perturbation that relaxes exact FSWAP nondemolition makes the
environment input-sensitive with the exact information/disturbance tradeoff
reported below. Irreversible actualization, an interaction-current history
with a relaxed or corrected data channel, a verified indivisible fault model,
and Record formation all remain live.

The coherent history carrier is not a Record. Projector weights are not Born
probabilities. The ordered algebra used to evaluate one update is not a
physical time metric, and no matrix coefficient is called a rate. There is no
axiom pressure.

## 1. Scope, sources, and prior-art boundary

The minimal framework supplies physical `Z^3`, nearest-neighbor adjacency,
translations, the 24 proper-cubic rotations, one `M_2(C)` possibility algebra
per site, one covariant local admissibility rule, and permanent Records when
they form. It does not select this six-site update, the prepared environment,
a fault grammar, an occurrence effect, a trace-out instruction, a Record-
formation map, a Born rule, physical time, or a rate.

The immediate repo boundary is:

- Cycle 230 supplies the actual local two-mode CAR FSWAP fixture.
- Cycle 259 shows that a joint flag plus a separate Choi arm can be spoofed by
  deleting only the data factor while auxiliaries survive.
- Cycle 262 tests same-bond, same-invocation-family, and encoded-syndrome
  routes, then leaves an intrinsic environment/history update as the next
  constructive route.
- The pointer-conservation note is only a firewall and constructive analogy:
  a controlled copy can preserve a pointer under supplied conditions, but it
  does not select this occurrence link or actualize a Record.
- The record/history/order/time/rate firewall keeps coherent order, history
  carriers, Records, time, and rates typed separately.

The finite rank-one Stinespring consequence is standard quantum-channel
mathematics, not a Cycle-266 novelty claim. Kretschmann, Schlingemann, and
Werner give the relevant information-disturbance and Stinespring-continuity
context in [*The Information-Disturbance Tradeoff and the Continuity of
Stinespring's Representation*](https://arxiv.org/abs/quant-ph/0605009).
Cycle 266 does not rederive or claim priority for that literature. Its new
repo-local content is limited to the explicit maximal-Schmidt-rank FSWAP
constructor, the exact split-fault application, the mixed/instrument and held
perturbation controls, and the dependency classification.

The repo's Kraus–Choi normalization note supplies a consistent finite-
dimensional convention but does not supply this physical update or fault
model. No Thirring engine is used or compared.

## 2. Actual FSWAP and local one-particle subspace

In occupation order `|00>,|01>,|10>,|11>`, use

```text
     [1 0 0  0]
F =  [0 0 1  0]
     [0 1 0  0]
     [0 0 0 -1].
```

The runner verifies

```text
F^dagger F = I,
F^2 = I,
F = F^dagger,
[F,(-1)^N] = 0,
Tr F = 0.
```

For the complete one-particle projector

```text
P_1 = |01><01| + |10><10|,
```

it also checks `[F,P_1]=0`, `F|01>=|10>`, and `F|10>=|01>`. Hence the local
one-particle subspace is preserved before any occurrence question is asked.
This is not the framework's one-particle mass fixture, which also requires the
encoded coin/stream update. It remains a two-mode local fixture, not the
global CAR compiler.

## 3. Maximal-inseparability single-update constructor

Let the data dimension be `d=4` and the four-qubit environment dimension be
`m=16`, with computational states `|j>_E`, `j=0,...,15`. Define sixteen data
unitaries

```text
B_0 = F,
{B_1,...,B_15} = all two-qubit Paulis except I tensor Z.
```

They are linearly independent because

```text
F = (I tensor Z + X tensor X + Y tensor Y + Z tensor I)/2,
```

so replacing `I tensor Z` in the Pauli basis by `F` preserves rank 16.

Define one cyclic branch update

```text
W_shift = sum_(j=0)^15 B_j tensor |j+1 mod 16><j|.
```

Orthogonality of the environment columns and unitarity of each `B_j` give
`W_shift^dagger W_shift=I`. Let `R_hist` be the four-environment-qubit circuit

```text
X_(h3), H_(h0),
CNOT_(h0,h1), CNOT_(h0,h2), CNOT_(h0,h3),
```

so that

```text
R_hist |1> = |GHZ_4>
           = (|0000>+|1111>)/sqrt(2).
```

The single supplied block update is

```text
W = (I_D tensor R_hist) W_shift.
```

The runner obtains:

```text
||W^dagger W-I||_F = 1.78534970688577e-15,
operator-Schmidt-rank_(D:E)(W) = 16,
maximum allowed by dim L(H_D) = 16.
```

Left multiplication by the local environment unitary does not change the
operator-Schmidt rank. Thus this is maximally non-product across the declared
data/environment cut.

On the prepared environment `|0>=|0000>`, only branch `B_0` is active:

```text
V := W (I_D tensor |0>) = F tensor |GHZ_4>.
```

The intertwiner residual is zero and leakage from
`H_D tensor span{|GHZ_4>}` is `3.79e-16`. This is roundoff zero.

The full unitary's nonfactorization is independently visible. On

```text
|01>_D tensor (|0>_E+|1>_E)/sqrt(2),
```

branches `F` and `I` produce orthogonal data outputs correlated with
orthogonal environment outputs. The reduced data purity is exactly `1/2` to
roundoff. Therefore prepared-subspace factorization has not been smuggled in
as full-unitary tensor-product structure.

The full `W` is a supplied bounded six-site block update. Its generic exact
synthesis from the one fixed framework admissibility rule is not derived here.
The explicit `R_hist` preparation uses only the declared nearest-neighbor
star, while the multiplexed block law remains supplied structure.

## 4. Finite pure-environment factorization theorem

### Statement

Let `U` be any finite joint unitary on `H_D tensor H_E`, let the environment
begin in a fixed pure state `|0>`, and define the prepared-subspace isometry

```text
V |psi> = U(|psi> tensor |0>).
```

If, for every data density matrix,

```text
Tr_E[V rho V^dagger] = F rho F^dagger,
```

then there is one normalized environment vector `|e>` such that

```text
V = F tensor |e>.
```

The conclusion is about `V`, not about `U` on other environment inputs.

### Proof

Choose an environment basis and write the isometry as

```text
V = sum_a K_a tensor |a>.
```

The reduced data channel has Kraus family `{K_a}`. Under the normalized Choi
convention used by the runner,

```text
J(V) = (1/d) sum_a |K_a>><<K_a|.
```

The target unitary channel has

```text
J(F) = (1/d)|F>><<F|,
```

which has rank one. Equality of the channels gives equality of their Choi
matrices. Since a sum of positive rank-one operators has one-dimensional
support, every vectorized Kraus operator lies in `span{|F>>}`:

```text
K_a = c_a F.
```

The isometry condition gives `sum_a |c_a|^2=1`. Therefore

```text
V = F tensor (sum_a c_a |a>) = F tensor |e>.
```

No locality, operator-Schmidt-rank, basis, or environment-size assumption
beyond finite dimensionality enters this algebraic step.

### Executable controls

For the maximal-rank constructor, all 16 Kraus operators are proportional to
`F`, the maximum proportionality residual is zero, their coefficient norm is
`0.9999999999999998`, the normalized Choi rank is one, and the Choi residual
is `2.22e-16`.

For density-matrix seeds `266,267,268,999`, the data residuals lie between
`1.16e-16` and `1.48e-16`, the environment residuals are zero, and the full
joint factorization residuals are below `8e-17`. A held dense complex
environment vector generated independently has zero maximum Kraus
proportionality residual. The theorem is an operator proof over arbitrary
lawful data; these samples are regression and held-out checks only.

## 5. Conditional split-factor fault and environment instruments

For the displayed constructor, replace only the prepared branch operator

```text
B_0=F  ->  B_0^fault=I
```

while keeping the environment shift, `R_hist`, and every other branch. The
resulting full `W_fault` is still unitary:

```text
||W_fault^dagger W_fault-I||_F
    = 1.78534970688577e-15.
```

On the prepared input it restricts to

```text
V_fault = I tensor |GHZ_4>.
```

Thus ideal and fault complementary states are identical for every data input:

```text
Tr_D[V rho V^dagger]
  = |GHZ_4><GHZ_4|
  = Tr_D[V_fault rho V_fault^dagger].
```

It follows immediately that for every environment-only effect `M`,

```text
Tr[(I tensor M)V rho V^dagger]
 = Tr[(I tensor M)V_fault rho V_fault^dagger],
```

and the same holds for all outcome probabilities and post-environment states
of an arbitrary environment-only instrument. This is the exact
environment-only spoof statement.

The runner tests held data seeds `266,267,999`. Environment-state differences
are at most `2.22e-16` and fault target leakage is `3.79e-16`, while data
residuals from the ideal FSWAP channel are

```text
0.6235586236936876,
0.7113732373742448,
0.7350726405290438.
```

A two-outcome nonprojective instrument with 16 unequal diagonal response
weights, conjugated into the history basis, gives identical ideal/fault
weights `0.2` and `0.8` and identical post-history states.

This does **not** prove that the split is a physical fault of the original
single update. The runner proves only that it is a consistent finite unitary
replacement when admitted as a counterfactual grammar. A substrate law may
declare `W` indivisible, and a verified physical fault family may contain only
whole-`W` deletion or specified local perturbations. Whether branchwise
replacement is lawful must be derived or measured rather than inferred from
the mathematical factorization.

Likewise, a joint data-plus-environment effect is outside the environment-only
statement. It may distinguish the channels for some prepared data. Uniform
after-the-fact data certification still faces FSWAP-invariant inputs, but live
interaction-current histories are not after-the-fact environment-only effects
and are not closed by this theorem.

## 6. Mixed environments and purification

The standard extension is clean. For a fixed mixed environment state
`sigma_E`, introduce a reference `R` and a purification `|Omega>_(ER)`. The
isometry

```text
V_tilde |psi>
 = (U_DE tensor I_R)(|psi> tensor |Omega>_(ER))
```

is pure. If its reduced data channel is exactly `F`, the theorem gives

```text
V_tilde = F tensor |eta>_(ER).
```

Therefore the complementary environment-plus-reference state is input-
independent. Its accessible environment marginal and every environment-only
instrument are also input-independent. This statement still does not imply
that a branchwise fault preserving the same `ER` state has a lawful unitary
implementation on `D+E` for an arbitrary physical model.

The runner supplies one explicit model where it does. Set both prepared
support branches `B_0=B_1=F` and take

```text
sigma_E = p |0><0| + (1-p)|1><1|.
```

Then

```text
W (rho tensor sigma_E) W^dagger
 = F rho F^dagger tensor tau_E(p),
```

with

```text
tau_E(p)
 = p R_hist|1><1|R_hist^dagger
   +(1-p) R_hist|2><2|R_hist^dagger.
```

Replacing both support-branch data operators by identity gives another
explicit unitary with output `rho tensor tau_E(p)`. At `p=0.37` and held
`p=0.61`, ideal and fault factorization residuals are below `6.4e-17`, the
environment differences are zero, and the faulty data residuals remain above
`0.62`.

A nonprojective instrument assigns response weights `0.8` and `0.3` to the
two occupied history branches. Its predicted outcome weight

```text
0.8 p + 0.3(1-p)
```

is `0.485` and `0.605` for the two tests. Ideal and split-fault outputs agree
to below `5e-16`, while their conditional data states remain respectively the
FSWAP and identity channels. Explicit purification at `p=0.37` returns Choi
rank one, factorization residual zero, and Choi residual `1.11e-16` on the
`D:(ER)` cut.

## 7. Held information–disturbance perturbation

The exact theorem does not say that an environment can never carry FSWAP-
sensitive information. Let `|eta_1>` and `|eta_2>` be two orthogonal history
states and define

```text
V_epsilon
 = cos(epsilon) F tensor |eta_1>
   + sin(epsilon) I tensor |eta_2>.
```

This is an exact isometry, but tracing the environment gives

```text
Phi_epsilon(rho)
 = cos^2(epsilon) F rho F^dagger
   + sin^2(epsilon) rho.
```

The normalized Choi trace distance from the ideal FSWAP Choi state is exactly
`sin^2(epsilon)`, and leakage from the ideal history subspace has operator norm
`|sin(epsilon)|`.

For the `+1` and `-1` FSWAP eigenstates `|00>` and `|11>`, the corresponding
environment states have trace distance

```text
|sin(2 epsilon)|.
```

Thus the new history branch becomes sensitive precisely when the exact
arbitrary-data unitary channel is relaxed. The runner checks `epsilon=pi/20`
and held `epsilon=pi/7`. For the held case:

```text
Choi trace distance       = 0.18825509907063326,
history leakage norm      = 0.4338837391175581,
eigenspace distinguishability = 0.7818314824680298.
```

All analytic residuals are below `3e-15`. This is a constructive live route,
not a failure: an interaction-current or correctable history monitor may trade
small disturbance for information, then use a verified correction or
fault-tolerant model. Cycle 266 does not determine that physical tradeoff.

## 8. Bounded ordinary-M2 placement and covariance

The support graph uses seven ordinary `M_2` sites:

```text
data_0            ( 0,0,0)
data_1            ( 1,0,0)
history_center    ( 0,1,0)
history_xminus    (-1,1,0)
history_yplus     ( 0,2,0)
history_zplus     ( 0,1,1)
close_candidate   ( 0,1,2)
```

The data bond, data-to-history attachment, three GHZ-star preparation edges,
and history-to-close-candidate edge all have Manhattan length one. Sites are
collision-free, overhead is constant, and the base support radius is three.

The runner enumerates every determinant-`+1` signed permutation matrix,
obtains exactly 24 proper-cubic frames, applies each plus the held translation
`(13,-11,7)`, and rechecks all sites and declared edges. There are no failures.
Thus the declared placement passes all 24 proper-cubic frames.

This is covariance of a supplied finite block and its role grammar. It does
not select the multiplexed `W` from the nearest-neighbor admissibility rule or
derive a host-free autonomous schedule. The full block update is deliberately
treated as one candidate physical event; the local synthesis and law-selection
problem remains explicit.

## 9. Supplied-structure and fault inventory

| supplied item | role | not derived here |
|---|---|---|
| `Z^3`, adjacency, translations, cubic frames | placement | spatial dimensionality |
| one `M_2(C)` per site | data and history carriers | preferred state or basis |
| occupation basis and actual FSWAP | target channel | global CAR compiler |
| pure `|0000>` or rank-two `sigma_E` | prepared environment | autonomous reset/preparation |
| Pauli completion and multiplexed `W` | maximal-rank constructor | substrate update selection/synthesis |
| `R_hist` and GHZ target | coherent history carrier | actualized history or Record |
| partial trace, Kraus, Choi, purification | finite channel analysis | physical discard/readout law |
| environment effects/instruments | spoof tests | selected measurement or Born rule |
| branchwise `F -> I` replacement | adversarial split test | lawful fault of indivisible `W` |
| `V_epsilon` | relaxed-channel control | physical perturbation strength or correction |
| close-candidate role | typed destination | actualization, permanence, Record formation |

The exact occurrence route has three open conditions at this resolution:

- `K_update`: derive/select the bounded single update and lawful environment
  preparation from the substrate rule;
- `K_fault`: derive a physical fault domain and decide whether the branchwise
  split replacement is allowed or whether the update is verified indivisible;
  and
- `K_form`: map a faithful coherent close to actualized permanent Record
  content.

The relaxed-channel route adds an alternative engineering question—how much
disturbance is allowed or corrected—but that is not counted as a fourth wall
required by the exact route.

## 10. Exact test ledger

The companion runner has 22 assertions:

- source and note contracts: `2`;
- FSWAP and local one-particle-subspace controls: `2`;
- maximal-rank update, prepared subspace, and global entanglement: `4`;
- pure factorization/Kraus theorem controls: `2`;
- split replacement, arbitrary effects, and nonprojective instrument: `3`;
- mixed environment, mixed instrument, and purification: `3`;
- exact/held information-disturbance perturbations: `3`;
- bounded placement and all-frame covariance: `2`; and
- scoped disposition: `1`.

Held controls include density seeds `999`, a dense complex environment state,
mixed weight `0.61`, perturbation `pi/7`, nonprojective instruments, an
unprepared environment-superposition entanglement witness, and translation
`(13,-11,7)` in all proper-cubic frames. Operator identities, not samples,
support every arbitrary-data statement.

Ideal prepared-subspace leakage is zero to roundoff, the admitted split fault
also has zero target leakage, and the perturbation leakage follows
`|sin(epsilon)|`. Thus leakage, wrong logical action, and occurrence evidence
remain separately reported.

## 11. TOE dependency ledger after Cycle 266

| wall | Cycle-266 state | exact remaining dependency |
|---|---|---|
| `C_ref` | explicit pure, mixed, and purified local history references; unchanged/open | derive lawful fresh environment/reference preparation without a privileged hidden state |
| `C_num` | unchanged: the two-mode occupation/parity and one-particle fixture is a supplied finite code | construct the same-encoding full-Fock number/parity realization and lawful preparation |
| `C_wrap` | unchanged: the coherent carrier is not a wrapped phase or realized-history coordinate | derive any physical unwrapping/history relation separately; one update is not such a relation |
| `C_int` | sharpened: maximal global update inseparability still gives a constant complement under exact unitary data action | select the update and verified fault domain; decide whether occurrence is indivisible or split-factor testable |
| `C_local` | seven-site bounded support and all-frame covariance constructed; still open | compile/synthesize the multiplexed block and preparation under the one local substrate law |
| `C_source` | no source/gravity law introduced; unchanged/open | derive resource/source coupling and physical observable identification |

Maturity scores remain:

| lane | score | reason |
|---|---:|---|
| operational quantum / records | `2/5` | exact channel theorem and carriers; no verified occurrence-faithful actualized Record |
| time | `1/5` | one update and coherent history carrier do not supply physical time |
| inertia / matter | `3/5` | local one-particle FSWAP subspace preserved; the mass fixture and global matter compiler remain open |
| gravity / source | `2/5` | no new source or lapse response |
| Born / probability | `1/5` | effect weights are finite diagnostics only |

## 12. No-go discipline gate: full N1–N8

The only negative theorem retained is narrow: under exact arbitrary-data
unitary reduction and an admitted split-factor replacement that preserves the
factorized environment state, no environment-only instrument distinguishes
ideal from that replacement. The following audit blocks every broader no-go.

### N1 — alternative-route enumeration

At least five materially different attacks were executed:

| marker | attack route | executable result |
|---|---|---|
| `ATTEMPTED-1` | hide the occurrence link in a globally maximally inseparable single update | full `W` reaches operator-Schmidt rank 16 and entangles unprepared inputs, but its exact prepared branch still factorizes |
| `ATTEMPTED-2` | enlarge and delocalize the pure environment carrier | four environment qubits, GHZ output, and a held dense complex carrier retain rank-one Kraus factorization |
| `ATTEMPTED-3` | use a mixed initial environment | explicit rank-two mixture and its purification retain constant complementary output for the exact unitary data channel |
| `ATTEMPTED-4` | use general environment processing rather than one projector | unequal-response nonprojective instruments have identical ideal/split outcomes and post-environment states |
| `ATTEMPTED-5` | relax exact nondemolition through a coherent alternate history | succeeds outside the theorem: environment sensitivity becomes `|sin 2 epsilon|` while Choi disturbance is `sin^2 epsilon` |
| `ATTEMPTED-6` | demand a full unitary completion of the split map rather than an isolated isometry | explicit pure and mixed controlled-shift completions are unitary, but their physical status remains a fault-grammar condition |

All are evidenced by the companion runner, which has authority none and audit
unset like this note; none is laundered as a prior retained verdict. The live
routes that were not closed—indivisible substrate faults, irreversible
actualization, continuously exported interaction current, active correction,
and Record formation—force the narrow claim.

### N2 — condition-independence audit

The exact route's collapsed open-condition set is `K_update`, `K_fault`, and
`K_form`.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `K_update`, `K_fault` | no: selecting `W` need not specify counterfactual faults | no: a fault grammar need not derive `W` or preparation | yes |
| `K_update`, `K_form` | no: reversible coherent evolution need not actualize | no: Record formation does not select this update | yes |
| `K_fault`, `K_form` | no: verified occurrence evidence need not become permanent | no: actualizing a carrier does not make its occurrence claim faithful | yes |

Fresh-state preparation and exact block synthesis are parts of `K_update`, not
inflated into extra walls. The perturbative correction problem belongs to an
alternative relaxed route, not the conjunction required by the exact route.

### N3 — hidden-condition scan

The proof and note were searched for the no-go skill's trigger phrases and
close variants. Load-bearing conditions are explicit:

- **“Prepared”:** the environment input is fixed pure or supplied mixed data;
  autonomous preparation is in `K_update`.
- **“Single update”:** `W` is one supplied bounded block; NN synthesis is not
  silently claimed.
- **“Exact”:** the data channel equals FSWAP for every density matrix, not
  merely the held samples.
- **“Environment-only”:** joint data/environment, live-current, and external
  actualization instruments are outside the conclusion.
- **“Split”:** `F -> I` with `|e>` preserved is admitted adversarial grammar;
  it is not inferred to be a lawful substrate fault.
- **Dimension/background:** `Z^3`, four environment qubits, basis, FSWAP,
  gates, partial trace, and instruments are inventoried.
- **Boundary/size:** finite support only; no thermodynamic or lattice-wide
  limit is used.
- **Stochasticity:** none; effect weights are not probabilities.
- **Record/actualization:** no coherent state is promoted to a Record.

The words “standard” and “prior art” refer only to finite channel mathematics
and are accompanied by the KSW and repo Kraus–Choi boundaries. They do not
hide a physical occurrence law.

### N4 — residual matching

| cited witness | witness residual | Cycle-266 residual | match and use |
|---|---|---|---|
| Cycle 259, lines `59–93` | data FSWAP deleted while flag and diagnostic replica survive | data factor replaced while environment carrier survives | yes for split-fault topology; not evidence that the split is a physical fault of `W` |
| Cycle 262, lines `59–65,631–634` | intrinsic environment/history route left live after three factorable carriers | exact pure/mixed environment dilation tested here | yes as campaign handoff; Cycle 266 partially closes only the exact-unitary environment-only branch |
| pointer-conservation theorem | supplied controlled copy can carry pointer content and has separate preparation/formation imports | occurrence of the named FSWAP invocation | no exact residual match; retained only as a firewall/constructive analogy |
| repo Kraus–Choi normalization note | consistent finite Choi/Kraus representation | rank-one mathematical step | matches the algebraic representation only, not the physical occurrence residual |
| KSW `quant-ph/0605009` | continuity and information-disturbance for Stinespring representations | exact FSWAP split-fault classification | adjacent prior art, not a split-fault witness and not counted as one |

Dropping the nonmatching physical citations does not weaken the theorem: its
factorization proof is self-contained finite linear algebra, and its fault
conclusion is explicitly conditional.

### N5 — rhetoric and resolution audit

The phrase “an environment-only close cannot distinguish” is resolved as:

| resolution | tested? | result |
|---|---|---|
| per environment effect | yes, algebraically arbitrary | identical because reduced environment states coincide |
| per environment instrument | yes, algebraic consequence plus explicit nonprojective tests | identical outcome weights and post-environment states |
| per site within the four-site carrier | yes as a subset of arbitrary environment effects | identical |
| per two-mode data block | yes | data channel differs under the split on noninvariant inputs |
| full six-site joint block | no negative claim | joint data/environment access is outside the theorem |
| full joint unitary on unprepared environment inputs | explicitly tested against factorization | `W` does not factor and entangles |
| lattice-wide or thermodynamic | not tested | no claim |
| actualized permanent Record | not tested | no claim |

Therefore “the environment cannot record occurrence” is forbidden. The
accurate statement is only that the prepared-branch complementary state is
constant under an exact unitary data channel, and an admitted replacement
preserving that state spoofs environment-only processing.

### N6 — partial-closure and primitive scan

Several live closures do not require a new axiom:

- **Indivisible-event reframe:** define and derive the physical event as the
  full local `W`, then admit only whole-event deletion or a verified local
  noise family. The branchwise replacement may simply lie outside the lawful
  fault domain. This is a fault-model/definition audit, not automatically new
  constitutional content.
- **Relaxed-channel constructor:** `V_epsilon` already exports FSWAP-sensitive
  history at quantified disturbance; correction or tolerated error could make
  it useful.
- **Irreversible interface:** a supplied open-system or actualization channel
  can make a carrier persistent, with its entropy/export ledger explicit.
- **Verified encoding:** a stronger gadget can couple syndrome production to
  a declared physical fault family rather than to independent flags.

The primitive registry and the current source notes were reread. Scale
reference supplies units only; kinetic isotropy supplies only `c_t=c_s` form;
realized-state evaluation supplies only a pointwise slot. None is stretched
into dynamics, fault selection, occurrence, measurement, probability, or
formation, and none is misclassified as a wall. A convention that merely
names `W` indivisible can narrow the deletion test, but empirical or derived
fault faithfulness remains separate.

### N7 — steelman

A hostile reviewer should object: “Your most important fault is not a deletion
of the single physical update you claim to test. You replace one algebraic
factor on one prepared branch while preserving the rest of a multiplexed
unitary. Stinespring factorization proves only that an exact unitary channel
leaks no input information to the complement; it does not prove that a
constant environment flag cannot faithfully indicate application of an
indivisible `W` under the actual fault family. Your own `V_epsilon` shows that
live history sensitivity returns immediately when exact nondemolition is
relaxed, and irreversible actualization or correction was never tested.”

That objection is convincing and defeats a broad occurrence no-go. The result
is therefore retained only as a theorem conditional on exact arbitrary-data
nondemolition, environment-only processing, and an admitted split-factor
fault. The optimal next route is the reviewer's verified indivisible-update
fault model.

### N8 — cross-cycle echo

Cycle 259's flag and Cycle 262's same-bond/encoded carriers show the same
logical danger: an auxiliary can survive a data-factor fault. Cycle 266 does
not count those repetitions as independent constitutional evidence. It
instead identifies the rank-one channel mechanism for the exact-unitary
environment branch and makes the fault-domain caveat stronger.

The repo's open-system reset interface is an instructive opposite echo: when
the reduced system channel is nonunitary reset, the environment carries the
old state exactly. That route retired an overly closed-system picture by
naming the environment/export interface, not by adding an axiom. The same
lesson applies here: relaxing exact FSWAP or changing the verified interface
can reopen occurrence information. Record-instrument notes likewise show that
instrument selection and actualization are real physical inputs, not automatic
consequences of a dilation.

The searched `NO_GO_LEDGER.md` corpus contains many examples where a negative
route was narrowed by a new interface, convention audit, or explicit bounded
construction. No ledger is used as authority for this theorem, and no similar
retired wall is ignored. Cross-cycle verdict: narrow conditional theorem,
live constructive escapes, no substrate-wide obstruction, and no axiom
pressure.

**No-go discipline status: PASS for the narrow theorem; FAIL for any broader
claim that local occurrence evidence is impossible.**

## 13. Disposition and next campaign

Retain:

- the maximal-rank full-unitary constructor;
- the exact prepared-subspace Stinespring factorization proof;
- pure and mixed environment/instrument controls;
- the explicit unitary split replacements as conditional adversarial tests;
- the quantified relaxed-channel information/disturbance route; and
- the bounded seven-site/all-frame placement.

Do not retain:

- full-joint-unitary factorization;
- physical lawfulness of branchwise `F -> I` deletion;
- a no-go for interaction-current, corrected, irreversible, or actualized
  occurrence histories;
- identification of a coherent environment carrier with a Record; or
- any time, rate, Born, source, gravity, or constitutional claim.

The optimal next campaign is a verified indivisible-update fault tournament.
Specify one local substrate update and its physically generated fault family,
test whole-update deletion and all local component perturbations, and ask
whether the history carrier is faithful without admitting an artificial
branchwise replacement. Separately test an irreversible actualization map;
even a faithful coherent occurrence flag is not yet permanent Record content.
