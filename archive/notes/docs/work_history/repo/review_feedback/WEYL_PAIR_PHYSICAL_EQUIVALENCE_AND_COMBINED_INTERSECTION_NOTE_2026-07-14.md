# Weyl-Pair Physical Equivalence And Combined-Intersection Probe

**Date:** 2026-07-14

**Type:** meta / Cycle 13 closest-theorem attack, primary-source audit, exact
finite probes, and N1--N8 scoped-negative gate

**Authority:** none. This is a review-feedback artifact. It is not a retained
theorem, an audit verdict, a physical-equivalence declaration, a context or
boundary choice, an axiom candidate, or an amendment. It makes **no live axiom**,
primitive, registry, audit, queue, or policy change.

Local authority surfaces checked verbatim are
`docs/MINIMAL_AXIOMS_2026-06-29.md`,
`docs/audit/data/axiom_premise_nodes.json`, and
`docs/work_history/repo/review_feedback/CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md`.

## Result Up Front

The two classified three-dimensional Weyl walks have a stronger relationship
than the previous “two-class” label exposed, but a weaker relationship than
complete same-experiment equivalence.

1. **Positive collapse in a covariant scope.** Their published transition
   matrices differ by the exact lattice character

   ```text
   chi(x)=(-i)^(x+y+z).
   ```

   If `G|x>=chi(x)|x>`, the two one-step walks obey `U_+=G U_- G^dagger`.
   Every finite transcript is therefore identical when the preparation,
   intervention, effect, phase reference, and boundary are transformed by the
   same `G`. For a localized input, every endpoint kernel differs only by the
   endpoint phase `chi(x)`, so every position-diagonal endpoint record agrees
   even without relabeling its outcome. A spatial reflection gives a second
   exact covariant identification.

2. **No collapse for every same-labeled context.** A one-step localized-input
   test that coherently compares two endpoints distinguishes the walks. With
   the effect specified below, the exact click probabilities are

   ```text
   p_+=1/4,  p_-=0.
   ```

   A plane-wave test at oriented momentum `(0,pi/4,0)` gives a perfect `0`
   versus `1` coin record. These tests require a supplied coherent intersite or
   oriented-momentum phase reference and a probability/readout bridge. The
   present axioms do not silently supply either. The pair is one covariant
   orbit only in a context category that quotients those transformed phase
   references; it is two distinguishable laws in a context category that
   holds the labeled reference fixed.

3. **The closest theorem still does not produce one complete TOE law.** The
   classification concerns a linear, homogeneous, local, unitary one-particle
   walk with a two-dimensional coin on the body-centered-cubic Cayley graph and
   a four-element binary rotation isotropy. The current foundation instead
   names cardinal nearest-neighbor adjacency on `Z^3`, the full proper cubic
   rotation group, local `M_2(C)` possibilities, and permanent records. The
   Weyl macrostep is exactly reachable by three ordered cardinal substeps, but
   the substeps do not commute. The ordered walk fails one exact 90-degree
   cubic covariance test. Generated many-particle composition leaves collision
   laws free. A finite reversible unitary cannot both create and permanently
   preserve a nontrivial record sector on the same carrier. Dirac completion
   doubles the carrier and leaves a continuous mass. Anomaly and continuum
   constraints filter supplied matter theories; they do not fill the record,
   actuality, statistics, interaction, or boundary interfaces.

The strongest defensible result is therefore positive but bounded:

> The classified free one-particle Weyl pair is one exact covariant orbit
> under a staggered lattice character or a mirrored protocol, but it is not
> one same-labeled-protocol class once coherent phase-comparison contexts are
> admitted. Intersecting the theorem with the current exact symmetry and
> permanent-record requirements is empty at the strict two-component unitary
> level; enlarging the model reopens families rather than selecting one
> complete law.

That is a `partial-attempt-with-named-untested-routes`, not a universal
impossibility result. A broad universal no-go is not shipped. In particular,
the result does not establish that a new axiom is required. It tells us what a
future derivation or carefully drafted axiom would have to identify: the exact
generated law, its physical context/equivalence category, and its record-
forming completion. Merely writing “Weyl,” “isotropic,” “causally invariant,”
or “up to reflection” would leave physical choices hidden.

## 1. The Primary Classification And Its Exact Premises

The closest theorem is D'Ariano, Erba, and Perinotti's complete classification
of isotropic quantum walks on lattices in dimensions one through three with
coin dimension two. Under their hypotheses, the three-dimensional admissible
Cayley graph is the BCC presentation of `Z^3`, and the only walks are two Weyl
walks. The source theorem is [arXiv:1708.00826](https://arxiv.org/abs/1708.00826).
The original construction and dispersion analysis are in D'Ariano and
Perinotti, [arXiv:1306.1934](https://arxiv.org/abs/1306.1934). The broader
informational reconstruction program and free Weyl/Dirac/Maxwell constructions
are summarized in Bisio, D'Ariano, and Perinotti,
[arXiv:1601.04832](https://arxiv.org/abs/1601.04832).

The source's positive BCC generators can be represented, without the common
`1/sqrt(3)` geometric normalization, by

```text
h1=( 1, 1, 1)   h2=( 1,-1,-1)
h3=(-1, 1,-1)   h4=(-1,-1, 1)
h1+h2+h3+h4=0.
```

Write

```text
eta_+ = (1+i)/4,    eta_- = (1-i)/4.
```

One branch uses `eta_+` on every positive generator and `eta_-` on every
negative generator; the other swaps them. The exact source matrices are

```text
A_h1 = eta  [[1,0],[ 1,0]]     A_-h1 = eta' [[0,-1],[0,1]]
A_h2 = eta  [[0,1],[ 0,1]]     A_-h2 = eta' [[1, 0],[-1,0]]
A_h3 = eta  [[0,-1],[0,1]]     A_-h3 = eta' [[1, 0],[ 1,0]]
A_h4 = eta  [[1,0],[-1,0]]     A_-h4 = eta' [[0, 1],[0,1]],
```

with `(eta,eta')=(eta_+,eta_-)` or `(eta_-,eta_+)`. The companion runner
checks both normalization identities and all displacement-resolved unitarity
sums exactly.

The same walks can be written, after the paper's momentum rescaling, as

```text
W_R(q) = exp(-i qx sigma_x) exp(-i qy sigma_y) exp(-i qz sigma_z),
W_L(q) = exp(-i qx sigma_x) exp(+i qy sigma_y) exp(-i qz sigma_z).
```

The `R/L` names here label the sign of the ordered Weyl generators; they avoid
depending on the papers' differing `+/-` conventions. The original dispersion
has the exact form

```text
omega^pm(k)=acos(cx cy cz -/+ sx sy sz),
```

where `ci=cos(ki/sqrt(3))` and `si=sin(ki/sqrt(3))`. Its low-momentum limit is
Weyl. This is an exact discrete walk first and a relativistic continuum
equation only in the stated limit.

### What the theorem supplies

- a complete classification inside its linear one-particle, Cayley-graph,
  locality, unitarity, homogeneity, isotropy, and two-dimensional-coin scope;
- a unique BCC generating graph inside that scope;
- two exact Weyl representatives and their dispersion; and
- integer-time continuation by powers of the one-step unitary.

### What it does not claim

- current six-cardinal-edge atomic adjacency;
- invariance under all 24 proper cubic rotations;
- a many-body tensor/Fock algebra or collision rule;
- interacting gauge and matter dynamics;
- a record-formation or permanent-record instrument;
- one actual outcome, a prepared-state link, Born statistics, or a trial
  corpus;
- a physical context/effect category; or
- an initial, asymptotic, phase-reference, or renewal boundary.

These are scope differences, not criticisms of the theorem.

## 2. The Strongest Exact Equivalence: A Lattice Character

Because `eta_+/eta_-=i` and `eta_-/eta_+=-i`, the branch transition matrices
obey

```text
A^+_h  =  i A^-_h       for h in {h1,h2,h3,h4},
A^+_-h = -i A^-_-h.
```

The phases define a character of the additive lattice:

```text
chi(x,y,z)=(-i)^(x+y+z),
chi(hi)=i,  chi(-hi)=-i,
product_i chi(hi)=i^4=1.
```

Let `G|x,c>=chi(x)|x,c>` on position and coin states. If `S_h` is the lattice
shift, then

```text
G S_h G^dagger = chi(h) S_h,
U_+ = G U_- G^dagger.
```

This is an exact unitary conjugacy on the infinite one-particle lattice. It is
not merely equality of dispersion or a continuum approximation.

### Complete finite-transcript proof in the covariant scope

Let a protocol consist of initial state `rho`, finite instruments
`M_1,...,M_n`, and final effect `E`. Transform the entire protocol by `G`:

```text
rho' = G rho G^dagger,
M'_j(X) = G M_j(G^dagger X G) G^dagger,
E' = G E G^dagger.
```

Substitution into the finite sequential trace and cyclicity of trace give the
same probability for every outcome string. Therefore the two walks are one
physical-equivalence class **for the declared protocol category in which all
states, instruments, effects, phase references, and boundaries are transformed
and remain admissible**.

For a localized input, the result is even more concrete. If `K^pm_n(x)` is the
sum of all `n`-step coin amplitudes ending at `x`, path-character
multiplicativity gives

```text
K^+_n(x)=chi(x) K^-_n(x).
```

Thus every single-endpoint effect and every position-diagonal endpoint record
has exactly the same probability. The runner verifies the complete endpoint
kernel identity through four steps, not a random sample of paths. The algebra
proves it for every finite `n`.

### The boundary price of the character

On a cardinal torus of side `L`, `G` is single-valued only when

```text
(-i)^L=1,
```

so each periodic length must be divisible by four. Otherwise the conjugacy
maps periodic boundary conditions to twisted boundary conditions. On an open
or infinite lattice, an externally fixed phase reference may likewise fail to
transform. Consequently, `G` identifies laws only after the boundary and
reference category are stated.

### Many-particle price of the character

Second quantization of `G` acts on an onsite vacuum/occupation pair as
`diag(1,chi(x))`. That is a valid free number-conserving Fock-space gauge
transformation after a vacuum, number operator, statistics, and composition
rule are supplied. Those structures are not consequences of a bare onsite
`M_2(C)` possibility algebra. Pairing terms, phase-locking interactions,
mass-coupled opposite chiral sectors, external phase standards, and some
boundaries need not be invariant under this transformation. The one-particle
conjugacy therefore cannot be promoted to a complete interacting-record
equivalence without a generated-law theorem.

## 3. Reflection Equivalence And The Proper-Rotation Separator

The factorized matrices satisfy exact identities

```text
W_R(qx,qy,qz)=W_L(qx,-qy,qz),
W_R(q)=conjugate(W_L(-q)),
W_R(q)=sigma_y W_L(-q) sigma_y.
```

The first is a one-axis spatial reflection. The last two express the source's
parity/complex-conjugation relationships without importing an undefined
Weyl-particle charge-conjugation convention. D'Ariano and Perinotti explicitly
state that charge conjugation is not defined for their isolated Weyl automata;
the Dirac doublet has the relevant CPT relation. Calling the two isolated
walks “CP equivalent” would therefore add a convention the cited construction
does not supply.

At a fixed Weyl node define

```text
D_i = i partial_i W(q)|_(q=0),
C = Tr(D_x D_y D_z)/(2i).
```

Then

```text
(D_x,D_y,D_z)_R=(sigma_x, sigma_y, sigma_z),   C_R=+1,
(D_x,D_y,D_z)_L=(sigma_x,-sigma_y, sigma_z),   C_L=-1.
```

Constant coin conjugations and proper spatial rotations preserve this triple
orientation; an improper reflection flips it. This is the smallest law-level
separator under the **current proper-rotation-only spatial identification at a
fixed momentum origin**. It is not a global Brillouin-zone invariant when
staggered characters and momentum-origin translations are also declared
gauge; the source contains additional node/momentum-translation relations.

The exact source isotropy group for the BCC pair is
`{I,i sigma_x,i sigma_y,i sigma_z}`, representing the three pi rotations. It
is not the full 24-element proper cubic group named by the current Lattice
axiom. The runner confirms exact pi-rotation covariance and failure of an exact
90-degree `z` rotation for both representatives at a generic momentum. Because
the primary theorem completely classifies its two-component isotropic scope,
adding that exact 90-degree requirement makes the strict two-component
intersection empty inside those hypotheses. A direct sum or larger program
carrier can reopen the problem; “empty at `s=2`” is not “no cubic QCA exists.”

## 4. Smallest Tested Same-Context Record Separator

Take a localized input at the origin with coin state

```text
|+x>=(|0>+|1>)/sqrt(2).
```

After one step, keep only endpoints `h1` and `-h1`. In one branch their coin
components are

```text
h1:   eta_+ |+x>,
-h1: -eta_- |-x>,
```

and the other branch swaps `eta_+` and `eta_-`. Use the normalized coherent
effect

```text
|E>=(|h1,+x> + i|-h1,-x>)/sqrt(2).
```

Its exact amplitudes are

```text
<E|U_+|0,+x> = (eta_+ + i eta_-)/sqrt(2),
<E|U_-|0,+x> = (eta_- + i eta_+)/sqrt(2)=0,
```

and hence `p_+=1/4` and `p_-=0`. Every one-endpoint norm in the same one-step
localized protocol agrees. This is therefore the smallest spatial-coherence
separator in the tested family: one step, one localized input, two endpoints,
and one relative phase. It is not a proof that no differently prepared
one-site coin protocol can distinguish a supplied momentum mode.

Indeed, a second exact separator uses a distributed oriented momentum state.
At `q=(0,pi/4,0)`, `W_R` sends `|+x>` to `|1>` while `W_L` sends it to `|0>`.
A `sigma_z` record distinguishes them perfectly. Reflection maps this protocol
to the opposite oriented momentum, so mirrored-protocol probabilities still
agree.

These are amplitude/effect results. Interpreting the squared effect as an
actual record frequency additionally needs the framework's missing context,
formation, prepared-state, probability, and trial-corpus links. The current
Record axiom's additivity over already formed records is not that bridge.

## 5. BCC Versus Current Cardinal `Z^3`

Every BCC generator above has cardinal Manhattan length three. The factorized
walk

```text
exp(-i qx sigma_x) exp(-i qy sigma_y) exp(-i qz sigma_z)
```

is exactly a three-substep cardinal split-step construction whose macrostep
has the eight BCC body-diagonal displacements. Thus there is no reachability
obstruction and no need to replace the set of sites `Z^3` merely to realize
the free walk.

There are, however, two exact prices:

1. Current “nearest-neighbor” means the six cardinal neighbors in one atomic
   law evaluation. A BCC macrostep is range three unless the three cardinal
   substeps, their intermediate state, and their continuation semantics are
   generated internally.
2. The `x`, `y`, and `z` coin rotations do not commute. All six generic orderings
   are distinct, and `XYZ-ZYX` is already nonzero at mixed second order.
   Update-order causal invariance cannot identify them while retaining the
   same record predictions.

One can make the schedule autonomous by storing a program/clock sector in the
state. Shepherd, Franz, and Werner show how classical control can be encoded
into an autonomous QCA's initial program state
([quant-ph/0512058](https://arxiv.org/abs/quant-ph/0512058)). That is a
representation theorem, not a selector of the program. A direct sum of all
six orderings has dimension `2*6=12`, requiring at least four qubits for an
exact binary carrier, and it splits into three even and three odd schedule
parities. The program state or boundary remains a physical input unless a
further law selects or mixes it.

Gorard's causal-invariance analysis
([arXiv:2004.14810](https://arxiv.org/abs/2004.14810)) motivates quotienting
update schedules only after a supplied rewrite rule is proved confluent. It
does not select the rewrite rule, and it does not turn noncommuting split-step
orders into one transcript law.

## 6. Generated Multi-Particle Composition And Interactions

A one-particle walk does not determine its many-particle collision law.
Farrelly and Short prove that causal fermionic dynamics can be represented by
a qubit QCA with finite overhead
([arXiv:1303.4652](https://arxiv.org/abs/1303.4652)). Mlodinow and Brun construct
multi-particle QCAs from quantum walks and then restrict to symmetric or
antisymmetric sectors
([arXiv:2011.05597](https://arxiv.org/abs/2011.05597)). These are positive
composition results. They require the statistics and composition structure;
they do not make all collision extensions unique.

The finite ablation uses four hard-core modes. Compare:

```text
C_0 = identity,
C_1 = identity except C_1|1100>=-|1100>.
```

Both are unitary, number conserving, and identical on the vacuum and entire
one-particle sector. Composed with the same free Weyl walk, they therefore have
the same classified one-particle law. On the fixed-two-particle state

```text
(|1100>+|0011>)/sqrt(2),
```

they produce orthogonal plus/minus relative-phase states, perfectly separated
by a fixed-number coherent effect. No particle-number-superselection escape is
available because both alternatives stay in the same `N=2` sector.

This does not classify all local collision extensions. It proves the narrower
point needed here: the one-particle Weyl theorem alone does not generate a
unique many-particle law.

## 7. Mass, Chirality, Anomalies, And Continuum Filters

The D'Ariano--Perinotti Dirac construction couples opposite Weyl blocks on a
four-dimensional internal carrier:

```text
E^pm_k = [[n A^pm_k,       i m I],
          [i m I,     n A^pm_k^dagger]],
n^2+m^2=1.
```

This is a strong form result, but `m` remains continuous. The two Dirac
constructions are related by the paper's CPT transformation modulo an internal
unitary. The construction does not supply interacting gauge dynamics, a mass
value, flavor multiplicity, symmetry breaking, or records.

Nielsen and Ninomiya's lattice chirality theorem
([DOI:10.1016/0370-2693(81)91026-1](https://doi.org/10.1016/0370-2693(81)91026-1))
is a necessary caution about global chiral bookkeeping under its locality,
translation, Hermiticity, and conserved-charge assumptions. Its hypotheses do
not automatically equal those of every discrete-time quantum walk, so it is
not used here as a no-go proof against the BCC pair.

Gauge-anomaly cancellation becomes constraining only after a gauge group,
representations, multiplicities, chirality map, and interaction content are
supplied. Nowakowski and Pilaftsis give a model in which anomaly cancellation
constrains hypercharges after the particle content and interactions are fixed
([hep-ph/9304312](https://arxiv.org/abs/hep-ph/9304312)). Conversely, Batra,
Dobrescu, and Spivak construct anomaly-free chiral fermion sets for broad
charge inputs ([hep-ph/0510181](https://arxiv.org/abs/hep-ph/0510181)), and
Costa, Dobrescu, and Fox parameterize general integer solutions of the `U(1)`
anomaly equations ([arXiv:1905.13729](https://arxiv.org/abs/1905.13729)). A
mirror theory can be anomaly free, and a vectorlike Dirac pair can cancel
anomalies without selecting the Standard Model's observed handed matter.
Continuum Lorentz/Weyl behavior likewise constrains the infrared expansion
while allowing distinct exact ultraviolet schedules and collisions. These are
valuable consistency filters, not substitutes for a complete generated
record law.

## 8. Permanent Records Versus Finite Reversible Evolution

The Weyl walk is reversible and unitary. It carries no record-formation
instrument. More strongly, a finite-dimensional unitary cannot produce a new
state in a forward-invariant record sector on the same carrier.

Let the finite Hilbert space split as `H=H_R direct-sum H_B`, where `H_R` is
the permanent-record sector. In record/blank block form write

```text
U = [[A,B],
     [C,D]].
```

Forward permanence `U(H_R) subset H_R` says `C=0`. Unitarity gives
`A^dagger A=I`, so square finite `A` is invertible. The other block equation is
`A^dagger B=0`, hence `B=0`. The blank sector cannot enter the record sector.
Spectator records can be preserved, but no nontrivial new record forms.

This is a finite-carrier theorem, not a universal record no-go. The open
routes are:

- a fundamental irreversible or sampled instrument;
- a reversible dilation with an environment and a restricted physical inverse
  domain;
- an infinite no-return/export sector;
- a topological or error-correcting archive; or
- a larger generated law in which “record” is relational rather than one
  invariant subspace.

The existing
[infinite reversible export probe](INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md)
constructs an isolated-event steelman but prices a blank/no-return boundary,
renewal resource, collision safety, record sufficiency, and actuality. It keeps
the infinite route open.

## 9. Actuality, Statistics, Contexts, And Boundary

A unitary amplitude law does not by itself state that exactly one outcome
becomes the public record, which prepared state enters the weight calculation,
how squared amplitudes become formation frequencies, how trials are
independently individuated, or which boundary is realized. The approved
realized-state primitive permits pointwise evaluation at a supplied lawful
state; it supplies none of those selections or weights.

The Weyl-pair question itself makes the context gap operational:

- if readable records are restricted to local position-diagonal effects that
  commute with `G`, the pair is indistinguishable in the tested free sector;
- if coherent intersite comparison records and oriented phase standards are
  admitted, the same labeled protocol separates the pair;
- if the context and boundary transform with `G` or reflection, complete
  covariant transcript equivalence follows; and
- if a torus or external phase reference is fixed rather than transformed,
  the equivalence may fail.

The framework therefore cannot declare the pair one physical law merely from
unitary conjugacy. It needs either a derivation of the allowed record-context
category or an explicit conditional theorem over each candidate category.

## 10. Every Extra Premise Priced

<!-- premise-price:start -->
| premise_id | classification_input | current_foundation_status | price_if_used |
|---|---|---|---|
| P1_BCC_GENERATORS | four positive body-diagonal generators and inverses | current atomic adjacency is six cardinal neighbors | three ordered cardinal substeps or an altered atomic neighborhood |
| P2_LINEAR_ONE_PARTICLE | state space `l2(Z3) tensor C2` and linear walk | onsite `M2(C)` possibilities do not identify a one-particle sector | vacuum excitation and sector-identification theorem |
| P3_UNITARY_HOMOGENEOUS_LOCAL | exact reversible finite-range homogeneous evolution | no update law is supplied by the four axioms | an exact atomic continuation law and its domain |
| P4_BINARY_PI_ISOTROPY | transitive four-element binary pi-rotation group | Lattice names all proper cubic rotations | weaken exact symmetry or enlarge the carrier to represent it |
| P5_REFLECTION_OR_CHARACTER_QUOTIENT | identify mirror or `G`-transformed protocols | reflection is not a declared lattice symmetry and `G` changes phase references | physical equivalence and context-boundary closure theorem |
| P6_CONTEXT_EFFECT_FAMILY | preparations interventions and effects used in transcripts | only formed records are readable | event-to-record decoder and admissible context category |
| P7_SCHEDULE_PROGRAM | one ordering or autonomous program for cardinal substeps | no scheduler or program sector is supplied | state carrier enlargement plus law or boundary selecting the program |
| P8_GENERATED_COMPOSITION | Fock or qubit composition and particle statistics | one onsite algebra does not fix finite-block composition | generated-composition statistics and locality theorem |
| P9_INTERACTION_AND_MASS | collision rule gauge coupling and Dirac mass | free walk fixes none of them | exact interaction law and parameter selection |
| P10_RECORD_FORMATION_PRESERVATION | append or invariant record instrument | Record states the result but not its dynamics | irreversible instrument infinite export or another proved completion |
| P11_ACTUALITY_STATISTICS_PREPARATION | one outcome prepared-state link weights and trials | explicitly absent from the foundation registry | formation semantics and frequency theorem or named conditionals |
| P12_BOUNDARY_PHASE_REFERENCE | initial sector torus twist reference orientation and renewal | realized-state primitive supplies only a slot | contingent data separated from universal law plus covariance proof |
<!-- premise-price:end -->

The scale-reference primitive and kinetic-isotropy primitive can later convert
units or normalize a derived kinetic form. Neither supplies any row above. The
realized-state primitive supplies only pointwise evaluation at a lawful
history-fixed state, not the state, law, boundary, phase reference, probability,
or selector.

## 11. Strongest Combined Intersection

The following is a staged intersection, not a chain in which later rows
inherit every earlier inconsistency. A row says what happens when that named
condition is imposed on the nearest relevant candidate class.

<!-- combined-intersection:start -->
| stage | added_condition | exact_result | remaining_scope_or_price |
|---|---|---|---|
| C0 | complete_s2_isotropic_classification | TWO_WEYL_WALKS | FREE_ONE_PARTICLE_BCC |
| C1 | covariant_character_or_mirror_quotient | ONE_COVARIANT_ORBIT | CONTEXT_AND_BOUNDARY_MUST_TRANSFORM |
| C2 | same_labeled_coherent_context | TWO_SEPARATED | BORN_EFFECT_AND_PHASE_REFERENCE_CONDITIONAL |
| C3 | current_full_proper_cubic_at_s2 | EMPTY_WITHIN_CLASSIFICATION_SCOPE | ENLARGE_CARRIER_OR_WEAKEN_EXACT_SYMMETRY |
| C4 | cardinal_split_step_and_autonomous_schedule | PROGRAM_FAMILY | ORDER_OR_PROGRAM_STATE_UNSELECTED |
| C5 | generated_many_particle_composition | COLLISION_FAMILY | INTERACTION_RULE_UNSELECTED |
| C6 | finite_unitary_nontrivial_permanent_formation | EMPTY | IRREVERSIBLE_INSTRUMENT_OR_INFINITE_EXPORT_NEEDED |
| C7 | infinite_or_instrument_record_completion | OPEN_FAMILY | FORMATION_ACTUALITY_STATISTICS_RENEWAL |
| C8 | dirac_mass_coupling | CONTINUOUS_MASS_DOUBLED_CARRIER | MASS_AND_INTERACTIONS_UNSELECTED |
| C9 | anomaly_and_continuum_constraints | CONSISTENCY_FILTER | GAUGE_REPRESENTATION_AND_UV_LAW_INPUTS |
| C10 | actuality_statistics_boundary | OPEN | COMPLETE_RECORD_TRANSCRIPT_LAW_NOT_SUPPLIED |
<!-- combined-intersection:end -->

Two conclusions follow.

First, adding every current exact word directly to the strict classified
`s=2` walk does not yield uniqueness; it yields an empty intersection at the
full-proper-cubic and nontrivial-permanent-formation stages. Second, making the
necessary enlargements does not currently restore uniqueness; it introduces
program, collision, mass, context, record, and boundary families. This is a
map of the nearest theorem's reach, not a proof that their intersection cannot
be selected by a stronger future theorem.

## 12. Constitutional Readout

This probe does not support inserting either Weyl representative into
[the live four axioms](../../../MINIMAL_AXIOMS_2026-06-29.md). It also does not
support inserting “up to physical equivalence” without defining the physical
protocol category: the same phrase can mean exact complete-transcript
equivalence under transformed contexts or false same-labeled-context
equivalence.

For the bare-metal record question, the important result is simpler. The best
available exact free-law theorem supplies coherent transport, not formation.
The finite reversible theorem shows why adding “records are invariant under
the walk” cannot make them form. A record-forming bare-metal law needs an
explicit physical completion—sampled/irreversible, infinitely exporting, or
another construction—and must prove its own permanent-record, actuality,
statistics, and context semantics.

If a future theorem closes those interfaces and returns one exact law or one
complete-transcript class, the existing Admissibility axiom may only need a
referent refinement, and no new Record sentence may be necessary. If the
formation content is independently shown underivable and indispensable, that
is when careful constitutional drafting becomes warranted. The present result
does not decide that owner-level question.

## 13. Primary-Source Ledger

| Source | Exact content used here | Boundary on use |
|---|---|---|
| D'Ariano, Erba, Perinotti, [arXiv:1708.00826](https://arxiv.org/abs/1708.00826) | complete `d=1,2,3`, `s=2` isotropic-walk classification; BCC graph and two 3-D Weyl walks; exact transition matrices | theorem premises are linear one-particle QW, Cayley graph, locality, unitarity, homogeneity, isotropy, and coin dimension two |
| D'Ariano, Perinotti, [arXiv:1306.1934](https://arxiv.org/abs/1306.1934) | exact BCC Weyl matrices, product form, dispersion, parity/time-reversal relationships, Dirac coupling | continuum Weyl/Dirac claims are low-wave-vector or supplied block constructions; isolated Weyl C convention is not supplied |
| Bisio, D'Ariano, Perinotti, [arXiv:1601.04832](https://arxiv.org/abs/1601.04832) | informational-principle QCA program and free Weyl/Dirac/Maxwell composition | no record formation, actuality, or interacting Standard Model completion |
| Farrelly, Short, [arXiv:1303.4652](https://arxiv.org/abs/1303.4652) | causal fermions can be represented by qubit QCA with finite overhead | representation does not select collision law or records |
| Mlodinow, Brun, [arXiv:2011.05597](https://arxiv.org/abs/2011.05597) | multi-particle QCA construction from QWs with symmetric or antisymmetric restriction | statistics/composition are supplied construction data |
| Shepherd, Franz, Werner, [quant-ph/0512058](https://arxiv.org/abs/quant-ph/0512058) | autonomous QCA can encode control in an initial program state | program becomes state/boundary data rather than being selected |
| Gorard, [arXiv:2004.14810](https://arxiv.org/abs/2004.14810) | causal invariance treats update-order choice as gauge for a supplied confluent rewrite system | does not identify the rewrite rule or equate nonconfluent schedules |
| Nielsen, Ninomiya, [DOI:10.1016/0370-2693(81)91026-1](https://doi.org/10.1016/0370-2693(81)91026-1) | lattice chirality/doubling constraint under stated assumptions | used as a global-consistency caution, not as a direct discrete-time-walk no-go |
| Nowakowski, Pilaftsis, [hep-ph/9304312](https://arxiv.org/abs/hep-ph/9304312) | anomaly-based hypercharge constraints in a supplied particle/interactions model | conditional model constraint, not exact lattice-law selection |
| Batra, Dobrescu, Spivak, [hep-ph/0510181](https://arxiv.org/abs/hep-ph/0510181) | anomaly-free chiral completions for broad charge assignments | demonstrates that anomaly freedom alone does not choose matter content |
| Costa, Dobrescu, Fox, [arXiv:1905.13729](https://arxiv.org/abs/1905.13729) | general integer solutions to `U(1)` anomaly equations | classification of supplied anomaly equations, not UV dynamics or records |

## 14. No-Go Discipline Gate

**Status:** `PASS` for the narrow statements above; overall scientific status
remains `partial-attempt-with-named-untested-routes` because the hostile
steelman and larger-carrier/infinite routes remain live.

### N1 — Alternative route enumeration

| Route | Honesty | Attack attempted | Result and authority |
|---|---|---|---|
| reflection quotient | ATTEMPTED | identify the Weyl pair by one improper spatial reflection | succeeds exactly for mirrored complete protocols; it does not prove same-labeled-context equivalence; exact product identity and [arXiv:1306.1934](https://arxiv.org/abs/1306.1934) |
| staggered-character quotient | ATTEMPTED | seek an internal lattice gauge mapping rather than treat chirality as two laws | succeeds exactly on the free infinite one-particle lattice; boundary and coherent-reference closure remain; source matrices from [arXiv:1708.00826](https://arxiv.org/abs/1708.00826) |
| fixed coherent context | ATTEMPTED | try to falsify equivalence with the same preparation and effect | one-step two-endpoint and oriented-momentum separators succeed exactly; companion runner |
| full proper-cubic intersection | ATTEMPTED | add the current 24-element proper cubic symmetry to the complete `s=2` class | both representatives fail an exact 90-degree test, so the strict classified intersection is empty; completeness from [arXiv:1708.00826](https://arxiv.org/abs/1708.00826) |
| cardinal split-step causal quotient | ATTEMPTED | embed BCC reachability into current cardinal adjacency and quotient schedules | reachability succeeds, but all six generic orders differ and mixed second-order terms separate them; companion runner and [arXiv:2004.14810](https://arxiv.org/abs/2004.14810) |
| autonomous program | ATTEMPTED | internalize the schedule as an autonomous QCA program | succeeds as a representation route, but program state/carrier is extra and unselected; [quant-ph/0512058](https://arxiv.org/abs/quant-ph/0512058) |
| generated many-particle composition | ATTEMPTED | lift the one-particle law and ask whether composition fixes interactions | two exact number-conserving collision laws share the full one-particle sector and differ at `N=2`; companion runner, [arXiv:1303.4652](https://arxiv.org/abs/1303.4652), and [arXiv:2011.05597](https://arxiv.org/abs/2011.05597) |
| permanent-record completion | ATTEMPTED | make a finite invariant subspace both receive new blank states and preserve records | exact finite-unitary block proof makes this intersection empty; irreversible and infinite routes remain open |
| Dirac/anomaly/continuum intersection | ATTEMPTED | use mass coupling, anomaly cancellation, and the continuum limit to select one complete law | Dirac doubles the carrier and retains `m`; anomaly/continuum constraints filter supplied models but do not supply record or UV completion; [arXiv:1306.1934](https://arxiv.org/abs/1306.1934) and Nielsen--Ninomiya source above |

Nine distinct routes exceed the five-route threshold. The positive character
and reflection routes are retained rather than hidden by the negative scope.

### N2 — Wall-independence audit

After collapsing downstream details, the remaining open-condition set is:

- `W1 UV_GENERATED_LAW`: lift the free BCC one-particle walk to one exact
  cardinal-domain, full-symmetry, scheduled, many-body interacting law;
- `W2 RECORD_ACTUALITY`: produce and preserve readable records and derive or
  explicitly condition one actual outcome, preparation link, and statistics;
- `W3 EQUIVALENCE_BOUNDARY`: define the physical context/equivalence category
  and separate universal law from phase-reference, orientation, initial, and
  renewal boundary data.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent after collapse? |
|---|---|---|---|
| W1-W2 | no: a unitary interacting QCA may have no record instrument | no: a sampled record law need not select Weyl interactions | yes |
| W1-W3 | no: one exact law can retain inequivalent fixed references and boundaries | no: choosing a quotient/boundary does not select collisions or schedule | yes |
| W2-W3 | no: a record instrument does not decide which coherent references are physical | no: a context quotient does not create or weight records | yes |

Mass, collision, and schedule are components of `W1`, not inflated as three
independent constitutional walls. Prepared-state and Born/frequency content
are components of `W2`. Torus twist and mirror orientation are components of
`W3`.

### N3 — Hidden-wall scan

The source and proof were searched for the required trigger phrases. The
quoted strings below occur here as audit targets; unquoted rhetorical uses
were removed or classified.

| trigger | classification |
|---|---|
| “we assume”, “by construction”, “as is standard”, “the framework provides” | no load-bearing unquoted use; every mathematical input is in the premise-price table |
| “bridge context”, “background”, “naturally”, “obviously”, “standard QFT” | no load-bearing unquoted use; no appeal substitutes for a theorem |
| “registered” | registry status appears only in N6 and the authority links; it grants only the approved primitive source text |
| “canonical” | the canonical-law contract is a target/interface definition, not proof that a Weyl or record law exists |

No hidden condition was promoted after N2. “Physical effect,” “Born
probability,” “phase reference,” “periodic boundary,” “Fock composition,” and
“program state” are already explicit in `W1`--`W3` and the premise ledger.

### N4 — Residual matching

| cited witness | residual attacked there | residual used here | match? |
|---|---|---|---|
| [isotropic-Weyl compatibility note](ISOTROPIC_WEYL_QCA_LATTICE_COMPATIBILITY_NOTE_2026-07-14.md) | BCC macrostep versus current cardinal atomic adjacency | `P1` reachability and range/schedule price | yes |
| [causal-schedule note](CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md#causal-invariance-versus-a-physical-scheduler) | schedule independence must hold at finite record-transcript level | noncommuting axis orders cannot be silently quotiented | yes |
| [infinite reversible export note](INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md#the-smallest-exact-obstruction) | finite invariant record sector cannot receive new states; infinite no-return route stays open | `C6` finite-unitary record obstruction and `C7` open infinite family | yes |
| [matter/chirality placement note](MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md#chirality-placement) | proper rotations leave mirror law/domain alternatives | fixed-orientation chirality placement | yes, but excluded as a general witness against staggered-character equivalence |
| [canonical completeness contract](CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md#the-complete-law-contract) | names interfaces a complete law must expose | used only to inventory residual interfaces | yes, but excluded as a general witness that those interfaces are impossible to derive |

The last two exclusions prevent a residual mismatch from becoming a universal
negative claim. “Open interface” is not “proved underivable.”

### N5 — Rhetoric audit

No unqualified “the pair is not one physical law” sentence is shipped. The
resolution ledger is:

| resolution | tested result | untested extension |
|---|---|---|
| per-transition | exact `+i/-i` character relation | none inside the published eight matrices |
| per-endpoint | all localized-input endpoint kernels agree up to `chi(x)` for every finite step by algebra | arbitrary nonlocal effect is not endpoint-local |
| per-protocol | covariantly transformed finite protocols agree; one fixed coherent protocol separates | a derived restriction on Nature's allowed contexts is open |
| per-block | one finite four-mode collision ablation and finite record-subspace theorem | all interacting larger-carrier blocks are not classified |
| lattice-wide | infinite-lattice character conjugacy and periodic-torus descent condition | every boundary, topological sector, and infinite archive is not classified |

Likewise, “unitarity cannot form records” is narrowed to a finite-dimensional
unitary with a forward-invariant record subspace on the same carrier. Infinite,
sampled, relational, topological, and environment-dilated versions are not
claimed closed.

### N6 — Partial-closure path scan

The required primitive registry protocol was run against
[`docs/audit/data/axiom_premise_nodes.json`](../../../audit/data/axiom_premise_nodes.json)
and the three current primitive notes.

- The **scale-reference primitive** supplies only `a^-1=M_Pl` as units
  conversion. It closes no dimensionless law, chirality, context, formation,
  or probability input here.
- The **kinetic-isotropy primitive** supplies only `c_t=c_s` in kinetic form.
  It can normalize an already derived continuum kinetic block; it does not
  select a discrete schedule, Weyl hand, interaction, or Lorentz completion.
- The **realized-state primitive** permits pointwise evaluation at a supplied
  lawful history-fixed state. It supplies no state, boundary, weight,
  typicality, preparation, or selector.

Live partial-closure paths that require no immediate new physics axiom are:

| path | status | what it could close |
|---|---|---|
| staggered-character or reflection convention | conditional theorem available in this note | collapses the free pair for a declared covariant context/boundary category |
| cardinal three-substep embedding | exact conditional construction | closes reachability while leaving order/program physical |
| autonomous program refactor | primary-source representation route | moves external schedule into state/carrier; does not select program |
| import-bearing record theorem | framework-approved workflow shape | state a sampled/infinite record completion as an explicit conditional, then attempt retirement |
| exact-law Admissibility referent | future owner-level possibility after derivation | could identify one generated law/class without a separate chirality or schedule axiom |

Because these paths remain live, this note does not say “new selector axiom
required.” Proposed unapproved primitives have zero premise weight.

### N7 — Hostile steelman

**Hostile steelman:** The negative framing may be attacking an unphysical
context category. The exact staggered character already proves the two
classified walks are unitarily conjugate, and all localized endpoint records
commute with that gauge. If the final record theory derives a number-
superselected local context algebra, transforms every phase standard with the
same relational program, and admits only boundaries in the character's
covariant orbit, the two-endpoint separator is not a legal fixed reference at
all. The pair then collapses to one complete free-law class. A larger
autonomous QCA could generate the cardinal substeps, Fock composition,
interactions, and an infinite relational archive, while anomaly and continuum
constraints remove its remaining parameters. The D'Ariano classification
([arXiv:1708.00826](https://arxiv.org/abs/1708.00826)) and programmable-QCA
construction ([quant-ph/0512058](https://arxiv.org/abs/quant-ph/0512058)) make
that route concrete enough that a universal no-go would be premature.

The steelman succeeds. Therefore the output remains
`partial-attempt-with-named-untested-routes`. Its next decisive target is a
generated context theorem: prove whether finite readable records can or cannot
carry the relative phase that separates the character-related walks.

### N8 — Cross-cycle echo

| prior similar wall | current status | retirement mechanism considered here |
|---|---|---|
| BCC versus cardinal adjacency | partially retired by exact split-step reachability | keep only atomic-range and noncommuting-schedule residue |
| chirality choice under proper rotations | partially retired by distinguishing law hand from mirror-domain boundary and now by `G` conjugacy | formulate a physical-equivalence theorem before any selector claim |
| simulator clock/schedule | partially retired when a boundary-reconstructible causal rank makes linear extensions transcript-equivalent | test the actual noncommuting substeps; autonomous program remains conditional |
| finite reversible permanence | not retired; narrowed because infinite no-return export is constructive | preserve the infinite/topological/relational routes as explicit untested alternatives |
| “one exact law” interface gap | not retired; reframed by the ten-field canonical contract | do not convert an open interface into a new-axiom conclusion; permit exact-law referent refinement |

The important echo is methodological: several earlier “missing physics” walls
became convention, boundary, or representation questions after the residual
was sharpened. This cycle applies the same retirement mechanism to the Weyl
pair. It does not apply that mechanism to formation or actuality without a
corresponding theorem.

## 15. Untested Routes And Exact Claim Boundary

Still untested or unclassified:

1. every larger-carrier, exactly full-cubic local QCA on the current cardinal
   lattice;
2. a classification of interacting, anomaly-free generated multi-particle
   completions of the BCC walk;
3. a theorem deriving the physical record-context algebra and deciding whether
   intersite phase comparisons survive;
4. infinite, topological, or error-correcting record archives with collision-
   safe renewal;
5. all global Brillouin-zone nodes and topological invariants under the full
   staggered/momentum-translation equivalence group;
6. a derivation of formation actuality and statistics from one enlarged law;
   and
7. a boundary-selection theorem.

Accordingly:

- **proved exactly here:** character conjugacy, mirrored product identity,
  endpoint-kernel relation, chiral triple sign, same-context separators,
  split-step noncommutation, finite collision nonuniqueness, and the finite
  invariant-record-subspace obstruction;
- **taken from primary theorem:** completeness of the `d=3`, `s=2` isotropic
  one-particle classification and its two Weyl representatives;
- **conditional inference:** strict `s=2` plus exact full proper-cubic
  covariance has empty intersection because both complete representatives
  fail one required group element;
- **not claimed:** no stronger exact law exists, all Weyl-pair contexts are
  physical, a new axiom is required, or the universe is a QCA.

## Reproduction

Run:

```bash
python3 scripts/weyl_pair_physical_equivalence_combined_intersection_probe_2026_07_14.py
```

The runner checks exact source transition-matrix unitarity, the lattice
character and its torus obstruction, complete finite endpoint kernels through
four steps, mirror/parity identities, chiral triple signs, pi versus 90-degree
rotation covariance, the `1/4` versus `0` separator, the perfect momentum
separator, all six split-step schedules, the fixed-number collision ablation,
the finite record-sector theorem controls, source/premise/intersection tables,
and every N1--N8 documentation contract.
