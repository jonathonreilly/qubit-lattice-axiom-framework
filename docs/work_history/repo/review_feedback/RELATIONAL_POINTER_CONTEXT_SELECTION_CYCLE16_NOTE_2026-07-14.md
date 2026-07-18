# Relational Pointer-Context Selection From Exact Dynamics — Cycle 16

**Date:** 2026-07-14

**Type:** primary-source audit, strongest-positive conditional theorem, exact
finite paired countermodel, and N1--N8 scoped-negative gate

**Authority:** none. This review-feedback note is not a retained theorem,
audit verdict, axiom proposal, primitive, context registration, law selection,
or owner ruling. It changes no axiom, primitive, registry, audit, queue,
policy, or retained surface. It creates only this authority-free note and its
exact companion runner.

**Companion runner:**
`scripts/relational_pointer_context_selection_cycle16_2026_07_14.py`

## Result Up Front

The strongest honest answer is now two-sided and more useful than the earlier
generic context no-go.

There is a real **context-after-dynamics** theorem:

> If an exact local interaction on one system qubit has a two-dimensional
> system-side commutant, or equivalently its induced bistochastic qubit channel
> has exactly one non-scalar fixed Bloch axis, the interaction uniquely selects
> one binary pointer PVM up to swapping its two outcomes.

This is the **simple-fixed-axis theorem**. For a nontrivial controlled-copy
interaction

```text
U_A = P_A+ tensor I + P_A- tensor B,
```

where `B` is a non-scalar target involution, the **interaction-side commutant**
is exactly

```text
C_S(U_A) = span{I,A}.
```

If `B` exchanges the two target states of the same relational frame and the
target begins in the `A+` blank, tracing the target gives exact dephasing in
the `A` basis. The two spectral projectors of `A` are then the unique stable
binary context. If a record event in that context is complete, both outcomes
are attainable, and the written label is exactly repeatable, Cycle 15's
binary-qubit reduction makes its branches Lüders. In that scoped chain,
neither the projectors nor the Lüders maps need be separately supplied after
the exact interaction law is known.

That positive theorem does **not** select the exact interaction. The runner
gives a finite paired countermodel in one fixed relational Pauli frame:

```text
parallel law:   pointer A = Z_frame, target flip = X_frame
transverse law: pointer A = X_frame, target flip = Z_frame.
```

Both laws are nearest-neighbor, exact controlled copies; both have a unique
two-dimensional pointer commutant; both induce full dephasing; both admit
binary repeatable Lüders reads; both are equivariant under every common
`M_2(C)` recoding; and both fit the same translation/proper-cubic spatial
support class. They remain relationally different because common recoding
preserves the Hilbert--Schmidt relation between the pointer and the recorded
frame: parallel has `Tr(A Z_frame)/2=1`, transverse has `0`. The same framed
input operationally separates them.

The exact Cycle-13/14 interaction makes the boundary sharper still. For

```text
U_cluster = CZ_(a,b) CZ_(b,c),
```

the onsite interaction commutant at **every** site is `span{I,Z}`. Thus the
coherent interaction dynamically selects a `Z` pointer algebra. This supports
the endpoint `Z` reads, but it does not select the center `X` read. Indeed:

- center `Z` is stable under `CZ-CZ` but leaves the endpoints in a product
  state;
- center `X` is not in the stable commutant and produces a maximally entangled
  endpoint state; and
- center `Y` also produces a maximally entangled endpoint state.

Bell capability therefore selects an equatorial **class**, not `X` uniquely.
The `Z` pointer axis has a continuous stabilizer that rotates `X` into `Y`.
Consequently a one-axis reference cannot select a transverse context. The
center `X` label needs a second noncommuting reference, an oriented full Pauli
frame, a more complete apparatus interaction whose own stable algebra is `X`,
or another exact theorem.

So the route succeeds exactly where it should:

- an exact interaction with a simple commutant can derive its pointer
  `CONTEXT`;
- locality, proper-cubic covariance, common-`M_2` presentation covariance,
  repeatability, stability, and redundancy do not select which such
  interaction is Nature's law;
- the currently programmed `CZ-CZ` substep selects `Z`, not the center `X`
  context it later consumes; and
- no interaction commutant, dephasing channel, or redundant coherent imprint
  supplies `EVENT` occurrence or single-history `ACTUALITY`.

No axiom text is proposed. The next derive-first target is a complete
microscopic apparatus/program interaction whose exact commutant selects every
consumed relational context—including the transverse center read—or a theorem
showing how a full relational frame plus the law uniquely selects it.

## Exact Question And Answer Matrix

| question | strongest positive answer | exact residual |
|---|---|---|
| can a fixed exact interaction select a context? | yes, if its system-side commutant is a unique qubit MASA | why that interaction is the physical law |
| can a reduced channel select a context? | yes, if its only non-scalar fixed direction is simple | system/environment split, channel-generating interaction, and event execution |
| does a noiseless commutant always select a classical basis? | no; it may be full, scalar, or noncommutative | a unique two-dimensional MASA needs a simplicity condition |
| does the predictability sieve select a basis? | for full qubit dephasing, exactly the two pointer poles minimize entropy production | identity and isotropic noise tie all pure states; the sieve is conditional on dynamics and score |
| does covariance select the pointer? | it transports a pointer selector equivariantly | covariant instruments form a class; covariance does not choose a member or frame relation |
| does a relational axis select both `Z` and `X`? | it selects its aligned binary PVM | its `U(1)` stabilizer rotates every transverse axis |
| does a full relational frame permit both? | yes, it can name aligned and transverse relations covariantly | parallel versus transverse remains a law/program choice |
| does `CZ-CZ` select the programmed contexts? | it selects onsite `Z` at center and endpoints | center `X` is deliberately outside the stable commutant |
| does redundant imprinting make an event occur? | no | readiness, execution, and an append/persistence rule |
| does redundancy choose one branch? | no | a coherent GHZ state contains both alternatives and is exactly reversible |

## Framework Boundary

The current foundation supplies:

- sites `Z^3` with nearest-neighbor adjacency, translations, and proper cubic
  rotations;
- one unprivileged `M_2(C)` possibility algebra at each site;
- one fixed local covariant admissibility rule whose actual content is not yet
  specified; and
- formed permanent records with content-only additive scalar readout.

It explicitly withholds context selection, measurement basis, dynamics,
update law, formation rule, weights, probability, and physical persistence
dynamics. The primitive registry adds only a scale conversion, kinetic-form
isotropy, and pointwise evaluation at a supplied realized state. None selects
an interaction, pointer algebra, reference frame, event, or actual branch.

This note therefore does not infer a quantum channel from the four axioms. It
asks a conditional inverse question:

```text
if an exact local interaction is eventually derived,
how much read-context content follows from it?
```

The answer is substantial but conditional.

## 1. Interaction-Side Commutant Theorem

Let `S` be one `M_2(C)` carrier and `E` a finite neighboring carrier. For an
exact interaction unitary `U` define the system-side commutant

```text
C_S(U) = { O in M_2(C) : [U, O tensor I_E] = 0 }.
```

This is the algebra of onsite system observables preserved by the complete
interaction for every joint input state. Common internal recoding sends

```text
U -> (V tensor V_E) U (V tensor V_E)^dagger
```

and transports the commutant by `O -> V O V^dagger`. Thus the construction is
presentation-equivariant rather than tied to a matrix label.

### Controlled-copy case

Let `A=A^dagger`, `A^2=I`, and

```text
P_A+ = (I+A)/2,
P_A- = (I-A)/2.
```

For a non-scalar target involution `B`, define

```text
U_A = P_A+ tensor I + P_A- tensor B.
```

Write a general system operator in the `A` eigenbasis. Its off-diagonal block
commutes through `U_A` only if it multiplies `B-I` to zero. Since `B` is not
`I`, both off-diagonal coefficients vanish. Every diagonal operator commutes.
Therefore

```text
C_S(U_A) = span{I,A}.
```

On a qubit this is a maximal abelian algebra. Its only minimal projections are
`P_A+` and `P_A-`, up to swapping their names. The exact interaction therefore
selects one stable binary PVM without a separately supplied basis.

This is the strongest clean positive theorem in the cycle. It is stronger
than saying “the pointer is chosen by decoherence”: it states an exact finite
criterion and its uniqueness scope.

### Perfect imprint condition

The commutant selects stability, not by itself an environmental record. Add:

1. `B` anticommutes with `A` in a transported common Pauli frame;
2. the target begins in the `A+` state; and
3. the interaction executes once on a fresh target.

Then

```text
|A+>|A+> -> |A+>|A+>,
|A->|A+> -> |A->|A->.
```

The two target states are orthogonal. Tracing the target gives the exact
conditional expectation

```text
Delta_A(rho) = P_A+ rho P_A+ + P_A- rho P_A-.
```

The first condition gives a copying action; the second is resource/preparation
content; the third is event content. They must not be collapsed into the
commutant theorem.

This exact form is the finite version of Zurek's original interaction-Hamiltonian
criterion: pointer observables commute with the apparatus--environment
interaction. Zurek's 1981 paper explicitly framed the pointer basis as the
eigenbasis of the observable commuting with the interaction Hamiltonian. The
present theorem adds the qubit uniqueness and relational-covariance boundary.

## 2. Simple-Fixed-Axis Channel Theorem

The reduced-channel version is slightly more general. Let `Phi` be a
bistochastic channel on `M_2(C)`. Suppose its fixed-observable space is

```text
Fix(Phi^dagger) = span{I,A}
```

for one nondegenerate Hermitian `A`. Then the spectral projectors of `A` are
the unique fixed rank-one binary PVM, up to exchange.

Equivalently, in Bloch form the eigenvalue-one subspace has exactly one
non-scalar direction. This is the **simple-fixed-axis theorem**.

For full dephasing along a unit Bloch vector `n`, the transfer eigenvalues are

```text
identity: 1
n axis:   1
two transverse axes: 0,0.
```

For partial dephasing they are `1,1,eta,eta`, with `|eta|<1`. The stable
binary context is still unique, although partial dephasing does not produce a
perfect environmental record. Thus “unique pointer context” and “completed
record formation” are distinct results.

Kribs's fixed-point structure theorem and Holbrook--Kribs--Laflamme's
commutant construction place this finite calculation in the standard
operator-algebraic framework for unital noise. Blume-Kohout, Ng, Poulin, and
Viola likewise classify perfectly preserved information as matrix-algebraic
structure. Those results characterize what a supplied channel preserves; they
do not select the channel from this framework's axioms.

## 3. From Pointer PVM To Lüders Form

Cycle 15 proved the relevant special result:

```text
complete binary CP instrument on one qubit
+ both outcomes attainable
+ exact repeatability
-> complementary rank-one effects
-> Lüders branch maps.
```

Combining it with the present result gives the strongest conditional chain:

```text
exact interaction with simple system commutant
-> unique pointer PVM up to outcome swap
+ complete attainable binary record event
+ exact repeatability
-> unique Lüders branches for that PVM.
```

The context and map form are derived **after** the interaction. This does not
derive the interaction, its readiness condition, its execution, or a sampled
outcome.

## 4. Why Environment Preparation Still Matters

The interaction-side commutant can be state-independent while imprint quality
is not.

Use the same CNOT interaction twice as a comparison, changing only the target
preparation:

```text
target |0>:  reduced system channel = Delta_Z,
target |+>:  reduced system channel = identity.
```

In the second case `X|+>=|+>`, so the target does not distinguish the two
control values. The interaction still has its `Z` system commutant, but no
record is written into that target.

Accordingly, “exact interaction” must be parsed carefully:

- the bare operator can select a nondemolition algebra;
- the full open-system channel also depends on the environment state;
- perfect record formation needs distinguishable conditional environment
  states; and
- prediction across time can also depend on the system Hamiltonian, coupling
  regime, and duration.

Paz and Zurek's weak-coupling analysis is an important primary control: when
self-dynamics dominates, energy eigenstates can win the predictability sieve.
The interaction-dominated and self-Hamiltonian-dominated regimes need not
select the same states.

## 5. Decoherence-Free And Noiseless-Subsystem Commutants

Decoherence-free/noiseless-subsystem theory makes the positive theorem more
precise, not more universal.

The noise algebra and its commutant may have three qualitatively different
shapes:

1. **unique classical pointer:** one-qubit dephasing has fixed algebra
   `span{I,Z}`;
2. **no selection because everything survives:** identity dynamics fixes all
   of `M_2(C)`;
3. **no nontrivial pointer because nothing survives:** complete depolarization
   fixes only scalar multiples of `I`.

Multi-site noise adds another possibility. The exact two-qubit parity channel

```text
Phi_parity(O) = (O + (Z tensor Z) O (Z tensor Z))/2
```

has an eight-dimensional fixed algebra. It contains both `Z tensor I` and
`X tensor X`, which do not commute with each other. This is a genuine stable
noncommutative algebra/noiseless sector, not one classical pointer basis.

Zanardi and Rasetti, Lidar--Chuang--Whaley, Holbrook--Kribs--Laflamme, and the
operator-QEC literature establish exactly why protected subspaces and
subsystems are organized by interaction/noise algebras and commutants. Their
existence does not imply that a unique maximal abelian subalgebra is physically
preferred. The simple-axis hypothesis is load-bearing.

## 6. Predictability Sieve And Environment-Induced Superselection

For a pure qubit with Bloch vector `r`, full dephasing along `n` gives output
Bloch vector `(n dot r)n`. Its linear-entropy production is

```text
S_L = (1 - (n dot r)^2)/2.
```

The minimum is zero exactly at the two poles `r=+/-n`. Thus for this supplied
dynamics, the predictability sieve uniquely finds the pointer PVM up to label.

The exact controls also expose the limits:

- identity dynamics gives zero entropy production for every pure state;
- complete depolarization gives the same one-half score for every pure state;
- a degenerate noiseless algebra can preserve incompatible observables; and
- changing the dynamics or competition with the self Hamiltonian changes the
  ranking problem.

Zurek's predictability-sieve program is therefore a powerful conditional
selector. It ranks states under a specified evolution and specified stability
functional. It is not a variational principle that selects the universe's
microscopic evolution from locality alone.

## 7. Covariant Instruments Do Not Choose A Member

Let a common `M_2(C)` recoding be `A -> V A V^dagger`. The controlled-copy
family obeys

```text
U_(VAV^dagger,VBV^dagger)
 = (V tensor V) U_(A,B) (V tensor V)^dagger.
```

The reduced channel and its binary Lüders instrument transform the same way.
The runner checks this for several noncommuting recoders and multiple input
states.

This is the correct role of covariance: a selector computed from physical
interaction data must transform with those data. Covariant instruments form a
class. Carmeli, Heinosaari, and Toigo's structure theorem parameterizes such
classes by systems of imprimitivity and intertwiners; it does not collapse the
class to one physical instrument.

Without any transforming non-scalar datum, a constant rank-one context would
privilege a one-site possibility presentation. Exact dynamics or a physical
reference resource supplies the datum that an equivariant selector needs.

## 8. Relational Reference Frames

A physical reference changes “which matrix?” into “which relation to the
reference?” It does not automatically select the relation.

### One-axis obstruction

Suppose a record supplies only the `Z_frame` axis. Every rotation

```text
exp(-i theta Z_frame/2)
```

leaves that axis and its two projectors unchanged. The same stabilizer rotates
all equatorial axes. In particular a quarter-turn maps `X_frame` to
`Y_frame`. Therefore:

> A one-axis reference cannot select a transverse context covariantly.

This is an exact stabilizer statement, not a probability argument. It is why
a dynamics-selected `Z` pointer alone cannot name the Cycle-13 center `X`
read.

### Full-frame sufficiency and remaining fork

An oriented full Pauli frame can name `X_frame`, `Y_frame`, and `Z_frame`.
Under common recoding the full tuple transforms together. It then supports
both of the exact local laws:

```text
U_parallel   controlled in Z_frame, flips target with X_frame;
U_transverse controlled in X_frame, flips target with Z_frame.
```

Both are relationally covariant. But they are not the same relation to the
same frame. The common-conjugation invariant

```text
kappa = Tr(A_pointer Z_frame)/2
```

is `1` for the parallel law and `0` for the transverse law. A fixed framed
preparation and decoder distinguishes them.

Bartlett, Rudolph, and Spekkens show why absent shared frames impose group
twirling/superselection restrictions and why relational encodings are physical
resources rather than notation. That primary framework supports the need to
co-transform the reference and protocol. It does not choose parallel rather
than transverse coupling for this lattice law.

## 9. Exact Application To `CZ-CZ-X-Z-Z`

Cycle 13 supplies

```text
prepare |+++>
apply CZ_(a,b) CZ_(b,c)
read center in X
read endpoints in Z.
```

Cycle 14 makes preparation and program propagation law fields but retains the
same coherent and read sequence.

### What the coherent interaction selects

`CZ-CZ` is diagonal in the transported `Z` frame. Direct commutant
calculation gives

```text
C_a(U_cluster) = span{I,Z_a},
C_b(U_cluster) = span{I,Z_b},
C_c(U_cluster) = span{I,Z_c}.
```

Thus a commutant/einselection theorem points to `Z` everywhere. With the two
endpoints prepared in `|++>`, tracing them gives full `Z` dephasing of the
center.

### Why the center uses a transverse read

The Bell front needs a noncommuting operation:

```text
center X+ -> (|00>+|11>)/sqrt(2),
center X- -> (|01>+|10>)/sqrt(2).
```

Reading center `Z` instead leaves endpoint product states. So the useful center
read is deliberately not the interaction's stable onsite pointer.

But Bell production alone is not enough to choose `X`. A center `Y` read also
produces maximally entangled endpoints, with different phases. `X` versus `Y`
is the azimuthal choice left open by the `Z`-axis stabilizer. A full relational
frame, phase convention made physical by records, or a more complete
measurement-apparatus interaction can select it.

### Reclassification of the programmed contexts

The minimum honest ledger is:

| programmed field | current derivation pressure |
|---|---|
| endpoint `Z` PVM | aligned with the `CZ-CZ` stable commutant; plausible theorem after full event dynamics is stated |
| center equatorial class | selected by Bell-fusion capability relative to `Z` |
| center `X` rather than `Y` | still a full-frame/program/apparatus relation |
| Lüders branch form | derivable from binary completeness, attainability, and repeatability once context/event exists |

This is a genuine reduction. “All `X/Z` reads are supplied” is now too coarse.
Endpoint `Z` and the center equatorial class have different derivation routes;
only the azimuthal member and the physical interaction/program selection remain
unclosed on this route.

## 10. Translation And Proper-Cubic Covariance

The interaction probe uses one nearest-neighbor system--fragment edge and no
absolute spatial axis. Apply the same relational rule at every ready oriented
motif. Translations move the motif, and every one of the 24 proper cubic
rotations maps its edge to another cardinal edge.

The runner enumerates the full proper cubic group and verifies nearest-neighbor
support preservation. Both the parallel and transverse internal laws occupy
the same spatial support class. Proper-cubic covariance therefore does not
distinguish them.

This is not a claim that spatial and internal frames are already physically
identified. The full frame is explicit relational program data in the finite
countermodel. A future exact connection law could derive its transport.

## 11. CONTEXT / EVENT / ACTUALITY Map

| interface | closed conditionally in this cycle | exact remaining content |
|---|---|---|
| `CONTEXT` | a supplied exact interaction with a two-dimensional system commutant uniquely fixes its binary pointer PVM; a simple fixed reduced axis gives the same result | select the exact physical interaction; for Cycle 13, select `X` versus `Y` inside the transverse class or derive a fuller apparatus interaction |
| `EVENT` | a supplied fresh blank plus one execution of the controlled copy creates orthogonal conditional fragments | readiness, why/when execution occurs, fresh-target preparation, append-only irreversibility, and future operation scope |
| `ACTUALITY` | none; the interaction enumerates coherent correlated alternatives | why one branch alone is the realized continuation |

The separations are exact:

- the same CNOT with a `|0>` blank writes a `Z` imprint, while with a `|+>`
  blank it writes none;
- zero executions and one execution produce different physical states, so the
  operator does not schedule itself;
- two executions of the same CNOT erase the imprint, so permanence needs an
  append/decoupling rule; and
- one execution on `|+>|0>` gives a Bell state, not either single outcome.

Redundancy is not occurrence. Two fresh CNOTs produce exact GHZ redundancy,
but the unitary can be inverted. Redundancy is not actuality. The pure global
GHZ state contains both record alternatives even though every fragment has a
classical marginal.

## 12. Primary-Source Ledger

| primary source | content used | boundary here |
|---|---|---|
| Zurek, [*Pointer basis of quantum apparatus*](https://doi.org/10.1103/PhysRevD.24.1516) | interaction Hamiltonian/commuting pointer criterion and nondemolition reading | begins with an apparatus--environment interaction; does not select this framework's interaction law |
| Zurek, [*Preferred Observables, Predictability, Classicality, and the Environment-Induced Decoherence*](https://arxiv.org/abs/gr-qc/9402011) | predictability sieve and persistence of correlations | ranking is conditional on evolution, split, and predictability functional |
| Paz and Zurek, [*Quantum limit of decoherence*](https://arxiv.org/abs/quant-ph/9811026) | self-Hamiltonian-dominated weak-coupling regime can select energy eigenstates | demonstrates regime dependence rather than a universal interaction-only basis |
| Kribs, [*Quantum Channels, Wavelets, Dilations and Representations of O_n*](https://arxiv.org/abs/math/0309390) | fixed-point structure theorem for unital quantum channels | characterizes a supplied channel; no microscopic-law selector |
| Holbrook, Kribs, and Laflamme, [*Noiseless subsystems and the structure of the commutant*](https://arxiv.org/abs/quant-ph/0402056) | noiseless subsystems from the commutant of unital-noise generators | commutants can be noncommutative and need not pick one classical MASA |
| Zanardi and Rasetti, [*Noiseless Quantum Codes*](https://arxiv.org/abs/quant-ph/9705044) and [*Error Avoiding Quantum Codes*](https://arxiv.org/abs/quant-ph/9710041) | dynamically decoupled/noiseless subspaces | preservation does not imply pointer uniqueness or record formation |
| Lidar, Chuang, and Whaley, [*Decoherence Free Subspaces for Quantum Computation*](https://arxiv.org/abs/quant-ph/9807004) | error-generator algebra and decoherence-free subspaces | protected coherent sectors can be larger than a classical pointer algebra |
| Kribs, Laflamme, Poulin, and Lesosky, [*Operator quantum error correction*](https://arxiv.org/abs/quant-ph/0504189) | general subsystem preservation framework | supplies classification after a quantum operation, not law selection |
| Blume-Kohout, Ng, Poulin, and Viola, [*Information preserving structures*](https://arxiv.org/abs/1006.1358) | perfectly preserved information has matrix-algebra structure | preserved algebra may encode quantum as well as classical information |
| Carmeli, Heinosaari, and Toigo, [*Covariant quantum instruments*](https://arxiv.org/abs/0805.3917) | covariant-instrument structure and measurement-model realization | covariance parameterizes a class and does not select one member |
| Bartlett, Rudolph, and Spekkens, [*Reference frames, superselection rules, and quantum information*](https://arxiv.org/abs/quant-ph/0610030) | absent frames, group twirling, and relational encodings | reference resources make relations physical but do not select the interaction relation |

## 13. Exact Runner Coverage

The companion runner checks:

1. authority and current foundation/primitive boundaries;
2. full and partial dephasing fixed spaces on all three Pauli axes;
3. the simple fixed-axis dimension and unique rank-one binary projectors;
4. exact controlled-copy unitaries and their system-side commutants;
5. orthogonal conditional fragment states and nondemolition pointer states;
6. the same CNOT with two target preparations, producing dephasing versus the
   identity channel;
7. the actual `CZ-CZ` three-site commutants;
8. center `X` and `Y` Bell production versus center `Z` product output;
9. two-fragment GHZ redundancy, exact reversibility, and coherent nonactuality;
10. identity, depolarizing, one-axis, and noncommutative parity fixed algebras;
11. predictability-sieve uniqueness and exact tie controls;
12. common-`M_2` covariance of interaction, channel, and binary instrument;
13. the parallel/transverse relational invariant and operational separator;
14. the one-axis stabilizer obstruction to a transverse selector;
15. all 24 proper cubic rotations on nearest-neighbor support; and
16. the formal `CONTEXT/EVENT/ACTUALITY` and N1--N8 contracts.

## No-Go Discipline Gate

**No-go discipline status: `PASS`** for the narrow claim established by the
finite paired countermodel:

> Locality, translation/proper-cubic covariance, common-`M_2` presentation
> covariance, binary repeatability, and the requirement that each chosen
> dynamics have a unique stable pointer algebra do not select parallel rather
> than transverse coupling to one fixed full relational frame.

This is not a universal no-go against deriving context. The positive theorem
in this note is the explicit counterroute: a uniquely derived complete
microscopic interaction can select its context. The overall scientific result
therefore remains
`partial-attempt-with-named-untested-routes`.

### N1 — Alternative-route enumeration

| route | honesty | attempted closure | result |
|---|---|---|---|
| interaction-side commutant | ATTEMPTED | derive pointer directly from exact `U` | succeeds uniquely when the qubit commutant has dimension two; does not select `U` |
| reduced-channel fixed algebra | ATTEMPTED | use a simple eigenvalue-one Bloch axis | succeeds for full/partial dephasing; identity, depolarizing, and degenerate channels expose the boundary |
| predictability sieve | ATTEMPTED | minimize one-step entropy production | uniquely recovers poles for dephasing; exact identity/depolarizing ties show dynamics dependence |
| noiseless/DFS commutant | ATTEMPTED | treat all preserved information as a pointer | two-qubit parity channel has incompatible fixed observables; unique classical MASA is not automatic |
| covariant instrument classification | ATTEMPTED | use covariance to select one instrument | both paired instruments are exactly covariant; primary structure theorem describes a family |
| relational reference frame | ATTEMPTED | use a physical frame rather than absolute `X/Z` labels | full frame names both relations; one axis cannot name transverse azimuth; parallel/transverse fork remains |
| Darwinist redundancy | ATTEMPTED | let many imprints select context/event | each paired interaction redundantly copies its own axis; GHZ remains reversible and coherent |
| actual `CZ-CZ` commutant | ATTEMPTED | derive Cycle-13 `X/Z` contexts from coherent dynamics | derives onsite `Z`; center Bell read lies outside commutant, and both `X/Y` work |
| Bell-capability target | ATTEMPTED | select the center basis by endpoint entanglement | selects equatorial class but not `X` versus `Y` |
| full apparatus interaction | UNTESTED POSITIVE ROUTE | include read device/program in the exact `U`, not only `CZ-CZ` | could select center `X`; this is the strongest surviving route and N7 target |

Nine routes were executed and one stronger route is preserved explicitly. The
narrow paired-countermodel claim does not require closing that positive route.

### N2 — Wall-independence audit

After collapsing environment blankness, execution timing, and future
decoupling into the event implementation, the remaining interface set is:

- `C`: select/derive one complete physical relational interaction and its
  pointer relation;
- `E`: derive its readiness, occurrence, append, and persistence semantics;
- `A`: derive which one outcome is actual.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `C,E` | no; an interaction and commutant do not execute themselves | no; an occurrence rule can execute either paired interaction | yes |
| `C,A` | no; a context still has two attainable branches | no; a global selector can choose a branch without deriving the local context | yes |
| `E,A` | no; a coherent executed interaction retains both alternatives | no; a selected history does not derive when the event is ready or why records persist | yes |

Pointer-PVM and Lüders-form residuals are not separate walls after `C` plus
binary repeatability: the positive theorems retire them. Environment state is
part of `E` when the claim is record imprint rather than stable commutant.

### N3 — Hidden-wall scan

| trigger | classification |
|---|---|
| “we assume” / “by construction” | no proof substitute; all finite operators, blanks, and frame relations are displayed and tested |
| “as is standard” / “standard QFT” | absent from inferential steps |
| “the framework provides” | foundation content is quoted from the live memo and registry only |
| “bridge context” / “background” | no hidden use; system/environment split, blank, frame, and decoder are explicit conditions |
| “naturally” / “obviously” | absent from load-bearing proof language |
| “registered” | used only for the approved primitive inventory; no primitive is enlarged |
| “canonical” | no context is called canonical; unique means unique under the displayed simple-commutant hypotheses |

The hidden conditions most likely to be smuggled by decoherence prose—split,
environment preparation, coupling regime, duration, frame resource,
predictability score, readiness, and branch semantics—are explicit.

### N4 — Residual matching

| prior witness | residual there | residual used here | match? |
|---|---|---|---|
| `RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md:654-724` | final microscopic interaction may derive pointer context; named N7 route | exact target attacked in this cycle | yes |
| `RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md:79-153` | pointer was supplied; commutation/persistence did not select it generally | simple-commutant condition and controlled-copy boundary | yes |
| `RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md:79-123` | projective algebra plus state does not choose `X/Y/Z` or generator | context before dynamics versus context after dynamics | yes, but used only as the superseded generic boundary |
| `APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md:260-296` | exact `CZ-CZ-X-Z-Z` law fields | direct commutant application to those fields | yes |
| `SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md:293-309` | same coherent/read package after law-generated preparation | same context residual | yes |
| `FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md:198-286` | common recoding must transport complete frame/protocol; local frames need a connection | relational covariance and fixed-frame separator | yes |

No prior broad no-go is used as a proof that future dynamics cannot select a
context. The present positive theorem explicitly narrows that older rhetoric.

### N5 — Rhetoric and resolution audit

| resolution | exactly tested | untested extension and resulting wording limit |
|---|---|---|
| one system qubit + one target | controlled-copy commutant, reduced channel, repeatability, covariance | not a classification of every finite interaction |
| three-site programmed cluster | all onsite commutants and `X/Y/Z` center projections | not the full builder/reset/apparatus dynamics |
| two-qubit noiseless block | noncommutative parity fixed algebra | not every many-body noiseless subsystem |
| relational one-axis frame | exact `U(1)` stabilizer obstruction | a larger physical frame can close azimuth |
| full relational Pauli frame | exact parallel/transverse paired laws and common-recoding invariant | another action or admissibility theorem may select one |
| lattice support | all 24 proper rotations of cardinal edges | no full classification of all proper-cubic local Hamiltonians |
| global branch | exact Bell/GHZ coherence and reversibility | no universal interpretation no-go |

Accordingly the note says “the tested generic conditions do not select the
paired law,” not “context is not a dynamics fact.” Context **is** a dynamics
fact under the simple-commutant theorem once the dynamics is selected.

### N6 — Partial-closure paths and primitive scan

The current registry contains only `minimal_axioms`,
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive`. The latter three supply no interaction, frame,
context, event, or actuality selector.

Real import-retirement paths are:

1. derive one unique exact interaction from the final nearest-neighbor
   admissibility rule, then compute its commutant;
2. enlarge `CZ-CZ` to a full center-apparatus interaction whose simple
   commutant is the relational `X` algebra;
3. derive a full oriented Pauli reference from permanent program records and a
   connection law, then prove the decoder chooses one equatorial relation;
4. add a physical objective—beyond generic Bell capability—that separates
   center `X` from `Y`;
5. prove an admissible-operation theorem that makes the selected pointer
   algebra permanent and retires the event-persistence import; and
6. pursue actuality separately via a boundary/superselection/global-solution
   theorem.

None is a naming convention disguised as physics. Conversely, none presently
forces new axiom text. The legitimate path remains conditional law, bounded
theorem, and import-retirement audit. No unapproved primitive receives premise
weight.

### N7 — Strongest hostile steelman

**Hostile steelman:** This probe may be stopping the interaction too early.
`CZ-CZ` is only the coherent resource substep, not the complete physical
measurement interaction. The final nearest-neighbor law could couple the
center to a program/apparatus fragment through an `X_frame`-controlled copy
immediately after the cluster gates. Its complete system-side commutant could
then be exactly `span{I,X_frame}`. The header and builder records could carry a
full transported Pauli frame, while a phase-sensitive continuation or
interference requirement could distinguish `X` from `Y`. Under the theorem in
this very note, that completed interaction would derive the center context and
Cycle 15 would derive the Lüders branches. The parallel/transverse pair only
shows that symmetry adjectives do not choose the completed interaction; it
does not show that the final admissibility law cannot.

The steelman succeeds. Therefore the broad negative remains a
`partial-attempt-with-named-untested-routes`. The narrow finite paired
countermodel still passes: both displayed laws satisfy all tested generic
conditions, so those conditions alone do not select one.

### N8 — Cross-cycle echo

The prescribed negative-phrase search and all physics-loop `NO_GO_LEDGER.md`
files were checked. The relevant cross-cycle mechanisms are:

- the older `X/Y/Z` nonidentifiability result held the dynamics fixed only at
  the abstract projective level; this cycle retires part of it by adding an
  exact interaction commutant;
- Cycle 15 retired “Lüders must be supplied” in the binary repeatable case;
  this cycle moves the retirement one level earlier by deriving the PVM from a
  simple interaction commutant;
- prior pointer-conservation work warned that a commuting interaction may
  write nothing; the CNOT blank-state separator preserves that warning;
- prior Darwinism work separated redundancy from local observability and
  actuality; the reversible GHZ control preserves that boundary;
- the foundation-equivalence cycle showed that common recoding must transport
  the reference and decoder; the parallel/transverse invariant applies that
  mechanism rather than holding labels fixed silently; and
- prior frame residuals sometimes retire by adding relational records rather
  than an axiom. The full-frame route is kept open here.

The cross-cycle lesson is positive: a previously supplied context can become a
theorem when a complete interaction has a simple stable algebra. It is not
retired merely by calling a basis stable or covariant.

## Bottom Line

Bare-metal context selection is possible in principle and exact in a useful
finite class:

```text
unique exact interaction
+ simple qubit interaction commutant
-> unique pointer PVM
+ binary attainability and repeatability
-> Lüders record form.
```

The currently programmed cluster interaction already provides half of the
story. It selects `Z` as the stable onsite algebra, which aligns with the
endpoint reads. It does not select the center `X` read. Bell fusion requires a
transverse read, but both `X` and `Y` work; the remaining azimuth is genuinely
relational-frame/apparatus content.

So the next scientific target is not a new Record adjective. It is the exact
center-apparatus/program interaction, plus a theorem that its relational
commutant is uniquely `X_frame`. Even if that lands, event occurrence and
single-history actuality remain separate interfaces.

## Verification

Run:

```bash
python3 scripts/relational_pointer_context_selection_cycle16_2026_07_14.py
```

