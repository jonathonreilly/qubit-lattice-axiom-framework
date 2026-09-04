# Foundation Sort-Preserving Equivalence and Dynamical Gauge Collapse

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an assumptions exercise, first-principles semantic
probe, finite-model calculation, and bounded no-go stress test. It is not an
axiom proposal, primitive, retained theorem, law-equivalence declaration,
physical-equivalence ruling, audit verdict, or owner decision. It changes no
axiom, primitive, registry, queue, review state, or retained claim.

**Outcome class:** exact semantic resolution at the foundation-reduct level,
exact finite-history gauge-collapse result, and a downstream definitional
residual. No axiom addition is needed for the sort-preservation result. The
current prose does not supply a concrete global tensor embedding or a physical
law-equivalence category.

## Result in plain language

The apparent three-way fork in Cycle 21 becomes smaller once the words in the
actual axioms are treated as a typed specification rather than as a loose
operator-algebra picture.

The axioms say there are *sites*, each site *has* its own possibility domain,
and a record at a site locks one possibility from that site's domain. In any
faithful mathematical model, those nouns and ownership relations are types.
An isomorphism of the model must map sites to sites and each site's possibility
domain to the possibility domain of the corresponding target site. A map that
splits one site's two possibilities across two target sites is not an
isomorphism of that supplied structure. This is forced by the grammar already
present; it is not a new physics choice.

However, the axioms do **not** name one global Hilbert space or global operator
algebra, and they do not give embeddings of each abstract `M2` site domain into
such an algebra. Consequently they cannot say that an old concrete tensor
factor embedding is fixed, because that embedding is absent from the
foundation language. Conjugating every embedded factor by an entangling
`C_phi` produces a different *representation expansion* of the same abstract
site/fiber structure. Whether two such expansions are physically identical is
a downstream equivalence question, not an unresolved atom inside Lattice or
Qubit.

That distinction answers the dynamical-collapse worry too:

- if arbitrary history-dependent frames may transport an entire finite
  reversible protocol, every reversible edge can be written as identity;
- this does not erase a genuine record instrument: branch rank, effect
  spectra, Choi rank, outcome labels, and transcript multiplicity survive;
- an infinite law also retains locality invariants unless the allowed frames
  are uniformly local in time; and
- record time and scalar cost survive only when the equivalence definition is
  required to preserve them. The current axioms do not themselves supply a
  clock or a resource-cost law.

The smallest clean clarification is therefore definitional, not
constitutional:

> A framework equivalence is a sort-preserving isomorphism of the supplied structure.

For dynamics, the minimum safe statement is:

> A law equivalence is such an isomorphism at every record history, compositional and uniformly local, preserving record labels, event order, and scalar readout.

The first sentence can sit in Qualification if a foundation-level equivalence
notion is needed there. The second belongs in the law-equivalence definition
that consumes histories and updates. Neither belongs inside Lattice or Qubit:
those axioms specify objects, while these sentences specify morphisms between
objects and laws.

In placement shorthand: the clarification belongs in definitions, not inside Lattice or Qubit.

This closes a semantic seam. It does not cause the first record, supply a later
formation trigger, choose an actual branch, derive Born weights, define a time
metric, or select the final update law.

## 1. Exact source reading

The current source says:

- physical sites are the points of `Z3`, with adjacency and named lattice
  symmetries
  ([`MINIMAL_AXIOMS_2026-06-29.md`, lines 35-41](../../../MINIMAL_AXIOMS_2026-06-29.md));
- each site has a local possibility domain whose full one-site algebraic
  presentation is `M2(C)` (lines 43-53);
- one fixed nearest-neighbor rule determines each site's available
  possibilities (lines 55-61);
- a record locks one admissible local possibility, with at most one permanent
  record per site, and readout is content-only and finitely additive
  (lines 63-72); and
- a state is a configuration of records, while further choices stay
  conditional or open (lines 74-84).

The same memo expressly says Admissibility is not dynamics and supplies no
record-production process or time metric (lines 103-111). Any interpretation
that quietly obtains an update, trigger, probability, or clock from the
semantic result below would exceed the source.

Cycle 20 established exact transport of finite adaptive protocols, conditional
on closure of the physical protocol category
([`ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md`,
lines 43-111](ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md)).
Cycle 21 classified fixed factor nets, pointer-only nets, and transported nets,
then left the physical category open
([`NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md`,
lines 44-97](NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md)).
This note resolves which part follows from a faithful model of the foundation
and which part first appears in an external representation.

## 2. A faithful many-sorted foundation model

Use the following minimal signature. It is a formal unpacking of the supplied
nouns, not a proposed enlargement of their physics.

```text
S                 sort of sites
Adj(x,y)          nearest-neighbor adjacency on S
T_a, R_g          supplied translation and proper-rotation actions on S

P                 sort of local possibilities
p : P -> S        the site whose domain contains a possibility
P_x = p^{-1}(x)   an M2(C) algebraic possibility fiber

Avail(x,q,n)      q in P_x is available under neighbor condition n
Rec(x)            absent, or one q in P_x
I(q)              scalar content/readout of a record
```

One may make neighbor conditions their own sort, or encode them as finite
tuples of adjacent site data. That choice does not affect the argument. The
load-bearing typing equation is

```text
p(Rec(x)) = x                 whenever Rec(x) is present.
```

A model isomorphism `f` has a site component `f_S` and a possibility component
`f_P`. Preservation of the ownership map is the commuting square

```text
p'(f_P(q)) = f_S(p(q)).
```

It must also preserve adjacency and the supplied lattice actions, transport
the algebraic operations on each fiber, preserve Admissibility, take records
to records, and preserve or transport scalar content according to whether the
content dictionary is fixed or part of the target model.

### Theorem 1 — site objects map to site objects

Every isomorphism of this many-sorted supplied structure maps sites to sites
and a whole source fiber `P_x` to the whole target fiber `P'_{f_S(x)}`.

### Proof

Sort preservation gives a bijection `f_S:S -> S'`. If `q` is in `P_x`, then
`p(q)=x`, so the commuting square gives

```text
p'(f_P(q)) = f_S(x).
```

Thus every image of a member of `P_x` lies in one target fiber. Bijectivity of
`f_P` and the inverse commuting square give equality with that fiber, not just
inclusion. A map that distributes two members of one source fiber across two
target fibers violates the square. QED.

The algebraic `M2` presentation strengthens this result: the map on a fiber
must preserve its algebraic structure. The lattice clauses further restrict
`f_S` to structure-preserving site maps. Fixed Admissibility, Record, and
readout data can only shrink the automorphism group to their common stabilizer.

### Single-sorted robustness

The conclusion does not depend on using formal many-sorted logic. In a
single-sorted model, add a unary predicate `Site(x)` and a binary relation
`InDomain(q,x)`. Any structure isomorphism preserves predicates and relations,
so it again maps sites to sites and each owned possibility domain to one owned
possibility domain. Removing both sort and ownership preservation would no
longer formalize the sentences “physical sites” and “each site has.”

The companion runner exhausts the smallest nontrivial example. With two sites
and two possibilities per site, there are `4! = 24` arbitrary possibility
bijections. Exactly

```text
2! times 2! times 2! = 8
```

are compatible with a site bijection and preserve fibers. If the same content
dictionary must be used at both sites, only four remain. A deliberately split
fiber has no compatible site map.

## 3. Foundation reduct versus representation expansion

The formal result does **not** prove that one familiar tensor embedding is
primitive. This is the key correction to the Cycle 21 fork.

Call the structure in section 2 the foundation reduct `F`. It contains
abstract fibers `P_x ~= M2`, but no object of the form

```text
G = B(tensor_x C2),       iota_x : P_x -> G.
```

Adding a global algebra `G` and embeddings `iota_x` makes a representation
expansion `R=(F,G,{iota_x})`. For a global automorphism `alpha`, define

```text
iota'_x = alpha o iota_x.
```

Then `R` and `R'` have the same foundation reduct. Their embeddings differ.
The naturality equation

```text
alpha o iota_x = iota'_x
```

makes `alpha` a morphism between the two expansions. It does not make `alpha`
an automorphism of the *fixed old embedding* unless
`alpha(iota_x(P_x))=iota_pi(x)(P_pi(x))` inside that same expansion.

For two qubits and entangling `C_phi`, the transported factors

```text
A'_x = C_phi A_x C_phi^dagger
```

are each abstractly `M2`, commute with one another, intersect in the scalars,
and generate `M4`. A transported `X` from the first factor is not contained in
either old one-site factor. Therefore:

| Question | Answer forced by the current foundation |
|---|---|
| May a foundation isomorphism split one abstract site fiber among several target sites? | No. It is not sort/ownership preserving. |
| Does the foundation fix a particular global tensor embedding? | No. No global algebra or embedding is supplied. |
| Can an entangling map relate two representation expansions while carrying every fiber to one target fiber? | Yes, via transported embeddings. |
| Are those expansions physically identical laws? | Not decided until a downstream equivalence category is defined. |
| Can a transported distributed subfactor silently count as the old site's factor? | No. That conflates a morphism between expansions with an automorphism of one fixed expansion. |

This is a standard reduct/expansion distinction. Goguen and Burstall's
institution framework is useful background for keeping signatures, models,
and invariance under change of notation separate, but it is not framework
authority and supplies none of the physics here:
[primary report](https://www.lfcs.inf.ed.ac.uk/reports/86/ECS-LFCS-86-10/).

## 4. How broad equivalence can trivialize dynamics

The danger is real if equivalence is defined too broadly.

Take a deterministic reversible edge from history `h` to its child `h'`, with
unitary update `U_h`. Under history frames `F_h`, the transported edge is

```text
U'_h = F_h' U_h F_h^dagger.
```

Set `F_empty=1` and recursively choose

```text
F_h' = F_h U_h^dagger.
```

Then `U'_h=1` on every edge of any finite history tree. Since a tree gives
every child a unique parent history, there is no consistency obstruction.

### Theorem 2 — finite reversible history collapse

If arbitrary history-dependent frames are allowed and the complete site net,
preparations, interventions, decoders, and future reads are transported, every
finite deterministic reversible protocol is isomorphic to an identity-edge
protocol with the same labeled history tree.

This is a representation theorem, not the claim that nothing happened. The
history labels and endpoint decoding were transported too. It says that bare
unitary edge symbols have no invariant content under that maximally broad
category.

The companion runner verifies the recursion exactly for `H`, controlled phase,
and `CNOT` edges, and independently for a six-edge branching history tree.

Time-dependent picture changes are familiar in quantum mechanics; Slagle's
gauge-picture construction is useful external precedent for local
time-dependent representations, but it neither defines this framework's
records nor licenses arbitrary physical equivalence:
[primary paper](https://arxiv.org/abs/2210.09314).

## 5. Why records do not disappear

For an outcome-labeled record branch with Kraus operator `K_r`, transported
branches have the form

```text
K'_r = F_hr K_r F_h^dagger.
```

Left and right multiplication by unitaries preserves matrix rank and singular
values. The effect `E_r=K_r^dagger K_r` changes only by input-frame
conjugation. For a whole channel, unitary pre/post composition preserves Choi
rank. These are exact invariants.

Polar decomposition makes the limit transparent:

```text
K_r = V_r sqrt(E_r).
```

A branch-dependent output frame can remove `V_r`, but it leaves
`sqrt(E_r)`. A nontrivial measurement effect cannot become identity.

The exact probe uses

```text
K_0 = |0><+|,       K_1 = |1><-|.
```

Both branches have rank one, their effects are the two `X` projectors, and the
resulting channel has Choi rank two. A unitary identity channel has Choi rank
one. Applying `H` at each output removes the partial isometry and leaves the
positive projectors. The record has been simplified, not erased.

The following survive every label-preserving unitary frame transport:

- the number of outcome branches and transcript labels;
- branch-effect spectra and ranks;
- channel Choi rank;
- all transcript probabilities when states and later reads are transported;
- record event order, if histories include it; and
- scalar readout and a cost derived from it, if the equivalence is required to
  preserve it.

A branch proportional to a unitary can become a scalar multiple of identity,
but the scalar probability and outcome label remain. A two-outcome record tree
cannot be bijected to a one-outcome identity tree while labels are preserved.

There is also a passive/active distinction. A passive representation change
writes no new record. A physical wrapper that writes a frame certificate adds
a permanent event, a readout contribution, and any associated clock/capacity
cost. It is not the same protocol under a cost-preserving equivalence.

## 6. Uniform locality blocks total infinite-law collapse

Finite-horizon trivialization alone is too weak for a physical law. The frame
family must have a locality bound uniform over arbitrary time and history.

Repeated controlled phase is an important exact exception. If
`U=C_phi`, then

```text
F_t = C_-tphi
```

trivializes every step, and every `F_t` is still one two-site diagonal gate.
Its range and depth do not grow. Thus the bare reversible phase really is
gauge inside a transported-net category that admits those frames and carries
all records and decoders with them.

A lattice shift behaves differently. The inverse cumulative frame after `t`
steps maps support at `x` to support at `x-t`. Its propagation range is `t`,
so no time-independent bound exists. A definition that requires uniformly
local frames does not gauge the shift to identity.

This is the elementary shadow of established QCA index theory. Schumacher and
Werner define reversible QCA using translation covariance and strictly finite
propagation ([primary paper](https://arxiv.org/abs/quant-ph/0405174)). Gross,
Nesme, Vogts, and Werner construct a one-dimensional index whose nontrivial
prototype is the shift and whose trivial class is locally implementable
([primary paper](https://arxiv.org/abs/0910.3675)). Those sources justify the
external comparison; they do not choose the framework's update or equivalence
category.

Therefore arbitrary net transport does **not** make every update-plus-record
law trivial. It removes all finite-horizon reversible edge content and some
uniformly local reversible families such as repeated `C_phi`. Nonunitary
record instruments, history structure, readable costs, and nontrivial
uniform-locality/QCA classes remain.

## 7. Minimum clarification and placement

There are two different clarification jobs.

### Foundation morphism

> A framework equivalence is a sort-preserving isomorphism of the supplied structure.

This says no more than “preserve every named sort, operation, relation, and
functional.” It makes explicit what a faithful formalization already does.
If the public axiom memo needs the definition, place it in **Qualification**
after the sentence that choices not fixed by supplied structure remain open.
It is a semantic definition, not a fifth axiom and not extra physical content.

An optional non-load-bearing gloss is:

> It maps sites by lattice-structure automorphisms and preserves each site's possibility domain, Admissibility, records, and readout.

### Law morphism

> A law equivalence is such an isomorphism at every record history, compositional and uniformly local, preserving record labels, event order, and scalar readout.

This belongs in the downstream **law-equivalence definition**, where histories,
updates, and composition are actually defined. It should not be inserted into
Qualification until those objects are supplied, because the current
foundation does not contain an event-order or update sort.

If representation expansions are used, one more downstream sentence can make
their boundary explicit:

> A representation equivalence may transport a concrete embedding only together with every named site fiber, admissibility relation, record instrument, boundary, decoder, and readout.

Do not place any of these sentences inside Lattice or Qubit. Lattice already
names sites and their spatial structure; Qubit already names the owned `M2`
fibers. Adding morphism rules there would mix specification of an object with
specification of when two objects or laws count as equivalent.

## Clause-deletion pass

The two recommended sentences survived the following deletion test.

| Candidate words | Keep/delete | Reason |
|---|---|---|
| `framework equivalence` | Keep | Names the relation being defined. |
| `sort-preserving` | Keep | Blocks site/fiber erasure and split-fiber maps. |
| `isomorphism` | Keep | Supplies bijection plus preservation/reflection of the structure. |
| `of the supplied structure` | Keep | Prevents importing an unsupplied global embedding and requires every supplied relation/function to travel. |
| `physical` | Delete | Undefined at this layer and would make the definition look like a physics ruling. |
| `exactly` | Delete | Already contained in isomorphism; no work remains. |
| `one-site` before every object | Delete | Redundant once sorts and the ownership projection are preserved. |
| explicit list of translations, rotations, adjacency, algebra, records, permanence, and additivity | Delete from the load-bearing sentence | All are part of “supplied structure”; an optional gloss can enumerate them. |
| `up to symmetry` | Delete | Ambiguous; an isomorphism explicitly carries the named structure. |
| `at every record history` | Keep in law equivalence | Prevents endpoint-only matching and supports adaptive composition. |
| `compositional` | Keep | Prevents a family of unrelated experiment-by-experiment coincidences. |
| `uniformly local` | Keep | Prevents the cumulative inverse frame from growing without bound and erasing shifts. |
| `record labels, event order, and scalar readout` | Keep | Prevents record, clock, and readable-cost collapse. |
| `probabilities` | Delete from this sentence | Transported instruments already preserve them when supplied; adding the word could look like a Born import. |
| `capacity` or `gravity` | Delete | Neither is foundation structure; a later resource law may add its own invariant. |

The first sentence is the irreducible semantic core. The second is the
irreducible safety boundary for a history-dependent law quotient.

## 8. Exact finite-probe ledger

The companion runner is
[`foundation_sort_preserving_equivalence_dynamical_gauge_collapse_probe_2026_07_14.py`](../../../../scripts/foundation_sort_preserving_equivalence_dynamical_gauge_collapse_probe_2026_07_14.py).

| Probe | Exact result | Scope |
|---|---|---|
| Two sites, two possibilities each | `8/24` possibility bijections preserve a site map and fibers; `4` also share one content dictionary | Finite semantic model |
| Split-fiber map | No compatible site map exists | Exact countermodel to arbitrary transport inside the reduct |
| Single-sorted encoding | Same eight maps preserve `Site` and `InDomain` | Encoding robustness |
| Entangling `C_pi/2` | Transported factors are commuting `M2`s generating `M4`, but transported `X0` is not old-site local | Reduct/expansion distinction |
| Reversible history frames | Every tested linear and branching unitary edge becomes identity | Finite-history collapse |
| Repeated `C_phi` | Trivializing frame stays two-site/range-one | Uniformly local gauge example |
| Repeated shift | Cumulative inverse frame has range `t` | Infinite-law locality residual |
| Two-outcome `X` record | Rank-one branch effects and Choi rank two survive; identity channel has Choi rank one | Record non-collapse |
| Record transcript | Labels, event order, and additive cost survive relabeling; active wrapper adds one event/cost | Operational residual |

These calculations are exact symbolic identities or exhaustive finite
enumerations. The shift statement uses the analytic support formula; the
finite loop checks its first twelve values and is not presented as an
infinite proof by sampling.

## 9. TOE-lane consequence map

| Lane | What this closes | What remains open |
|---|---|---|
| Foundation semantics | Abstract sites and their fibers are preserved by faithful model isomorphism. | Whether different concrete representation expansions are physically equivalent. |
| Update law | Exposes which reversible content is pure history-frame choice. | Exact update selection, existence, uniqueness, and nontrivial locality class. |
| Record formation | Proves a nonunitary record cannot be gauged to identity. | First record, later formation trigger, branch actualization, rate. |
| Probability | Preserves whatever instrument probabilities a supplied protocol has. | Born rule, preparation-to-weight bridge, actual branch. |
| Time | Event order/ticks can be invariants of law equivalence. | Why events occur, metric time, lapse/rate. |
| Capacity/gravity | A readable frame wrapper cannot be free if cost is record-derived. | A capacity law, saturation dynamics, geometric/gravity bridge. |
| Matter/mass/chirality | Prevents an entangling representation change from silently becoming an old-site local symmetry. | Exact law, particle content, mass ratios, mirror/conjugate counting. |
| Locality/QCA | Uniform locality preserves nontrivial shift/index-type classes. | The framework's actual QCA class and three-dimensional invariant. |

The semantic clarification is useful across all lanes because it prevents
representation choices from masquerading as derived physics. It does not fill
the substantive physics gaps.

## 10. Assumption ledger and first-principles cut

The exercise strips the problem to five assumptions, only two of which are
already implicit in a faithful reading of the foundation.

| ID | Assumption | Status after this probe |
|---|---|---|
| `S1` | The nouns “site,” “possibility,” and “record” denote typed objects with the stated ownership relation. | Required to formalize the actual sentences; deleting it destroys their meaning. |
| `S2` | An equivalence of the supplied foundation preserves its named structure. | Definition of structure isomorphism; no new physics. |
| `S3` | Concrete global embeddings may be compared as physical representations. | Not supplied; downstream definition required. |
| `S4` | A law equivalence is compositional, history-preserving, and uniformly local. | Not supplied; necessary safety condition for a useful gauge quotient. |
| `S5` | Event order and scalar readout are part of the compared law object. | Readout is supplied; event order appears only when a history/update law is supplied. |

The Elon-style first-principles answer is blunt: do not choose between “fixed
old tensor net” and “arbitrarily transported net” before asking which of those
objects the foundation actually bought. It bought abstract sites, abstract
site domains, adjacency, Admissibility, records, and readout. It did not buy a
global tensor coordinate system. Protect the things actually bought; treat the
rest as representation until a downstream experiment or theorem gives it
physical standing.

The killer tests for any proposed equivalence are correspondingly concrete:

1. Can it split one source site's domain across multiple target sites?
2. Can it turn a two-outcome nonunitary record into a one-outcome identity?
3. Can its cumulative frame range grow without bound?
4. Does it change record labels, their order, or scalar readout?
5. Does implementing it write an extra permanent certificate?

Failure of any named requirement means the map is not an equivalence in that
category. Passing them does not make the equivalence axiom-grade; it only
qualifies the downstream quotient.

## 11. No-go discipline N1-N8

The bounded negative claim under test is:

> The current four axioms do not select a concrete global site embedding or a physical law-equivalence category, and arbitrary history-dependent equivalence without locality/history restrictions collapses too much reversible dynamics.

The positive companion claim is that any faithful foundation isomorphism does
preserve abstract sites and fibers.

### N1 — alternative-route enumeration

Nine routes were checked rather than treating one obstruction as universal.

1. **Many-sorted syntax:** `p' f_P = f_S p` forces whole-fiber transport.
2. **Single-sorted syntax:** preserving `Site` and `InDomain` gives the same
   conclusion.
3. **Fixed global embedding:** factor-normalizer rigidity from Cycle 21
   excludes entangling maps.
4. **Transported representation expansion:** entangling maps can relate two
   expansions with the same reduct.
5. **Selected pointer quotient:** a diagonal phase can preserve the selected
   readable algebra while changing unread possibilities.
6. **Finite reversible history gauge:** arbitrary node frames trivialize every
   unitary edge.
7. **Uniform-local infinite law:** a shift resists trivialization because the
   inverse frame range grows.
8. **Nonunitary instrument route:** rank/effect/Choi invariants prevent record
   collapse.
9. **Record/time/cost route:** history labels and costs survive only under an
   explicitly structure-preserving law equivalence.

No route derives the first record, an actual branch, Born weights, or a unique
update.

### N2 — wall-independence audit

Use four residuals:

```text
E   physical law-equivalence definition, including uniform locality
O0  occurrence of the first record
O1  trigger/rate for later record formation
A   actuality and probability/weight selection
```

| Route | `E` | `O0` | `O1` | `A` |
|---|---:|---:|---:|---:|
| Sort-preserving foundation isomorphism | partially constrains | no | no | no |
| Representation expansion transport | exposes need | no | no | no |
| Reversible history trivialization | constrains | no | no | no |
| Uniform-locality/QCA index | constrains | no | no | no |
| Instrument rank/Choi invariants | constrains | no | no | no |
| Permanent record axiom | no | asserts only that records form | no rule | no |
| Hypothetical formation trigger | no | need not seed | may close | no |
| Hypothetical Born/actuality bridge | no | no | no | may close |

Pairwise independence has explicit witnesses. Two models can share the same
foundation reduct and records but choose different representation-equivalence
categories (`E`). A model can stipulate one boundary record while leaving all
later triggers absent (`O0` without `O1`). A later conditional trigger can be
defined on nonempty histories without causing an empty-history seed (`O1`
without `O0`). Identical event histories can carry different probability
bridges or no actual-branch selector (`A`). None of these walls is a renamed
version of another.

### N3 — hidden-wall scan

Potentially smuggling phrases were classified explicitly.

| Phrase | Hidden risk | Treatment |
|---|---|---|
| `physical equivalence` | Assumes the very category being sought | Replaced by formal structure/law isomorphism. |
| `same site` | Conflates an abstract site with one concrete tensor factor | Split into reduct and embedding expansion. |
| `transport everything` | Can hide records, boundaries, clocks, and costs | Enumerate the transported structure. |
| `finite-depth is gauge` | Ignores cumulative time-dependent range | Require uniform locality. |
| `identity dynamics` | Can erase notation while retaining labeled histories/effects | Distinguish unitary edges from instruments. |
| `record-preserving` | May mean endpoint statistics only | Require labels, order, content, and composition. |
| `clock/cost preserved` | Imports an unsupplied clock/cost | State it conditionally on those fields being in the law object. |
| `M2 at each site` | May be read as a fixed global tensor embedding | Treat `M2` as an abstract owned fiber unless embeddings are separately supplied. |

No hidden formation, probability, or resource law is used in the exact
results.

### N4 — residual matching

The result matches, rather than overclaims past, the named residuals:

- Cycle 20 lines 70-111 left physical category closure, local records,
  boundary sectors, and readable implementation cost open. Sections 4-6 here
  identify exact invariants and the uniform-local condition.
- Cycle 21 lines 44-97 left fixed versus transported site-net semantics open.
  Sections 2-3 here show that the abstract fiber is fixed by faithful syntax,
  while a concrete embedding is absent and therefore belongs to an expansion.
- The current axioms lines 76-84 require unsupplied choices to remain open;
  the proposed text is a definition and does not promote a global embedding.
- The current axioms lines 103-111 deny a supplied dynamics, time metric, and
  record-production process; all four remain residual here.

The conclusion is bounded to model isomorphism, representation expansion,
finite-dimensional instruments, and uniform-locality diagnostics. It is not a
classification of every conceivable physical duality.

### N5 — rhetoric audit

Prohibited overstatements and their bounded replacements:

| Do not say | Bounded statement |
|---|---|
| `The axioms force the old tensor factors.` | They force abstract site fibers; no concrete embedding is supplied. |
| `Transported nets are unphysical.` | Split-fiber maps are not foundation isomorphisms; whole-expansion transport remains a downstream category option. |
| `All dynamics is gauge.` | Finite reversible edges collapse under arbitrary history frames; instruments and locality classes need not. |
| `Records solve gauge selection.` | Record invariants constrain equivalence but do not select a unique reversible representative. |
| `The shift is absolutely nontrivial.` | It is nontrivial under uniformly local frame equivalence; a nonlocal coordinate change can erase it. |
| `No axiom change can ever be needed.` | No axiom addition is needed for this semantic result; future physics may still require a carefully approved law atom. |

No words such as “impossible,” “unique,” “derived TOE,” or “proved physical”
are used outside their exact finite/formal scopes.

### N6 — partial-closure paths

Useful closures do not require solving every wall at once.

1. Add the one-sentence framework-equivalence definition to Qualification as
   non-axiom semantic prose, if needed.
2. Define the downstream law category with uniform locality, composition, and
   record-history preservation.
3. Re-run Cycle 19-21 update candidates inside that category; quotient only
   the representatives admitted by it.
4. Treat nonunitary record effects and readable wrapper cost as invariants,
   not as gauge artifacts.
5. Continue the separate first-record, later-trigger, probability, and time
   probes without pretending this semantic closure solved them.

Even if the final physical category remains undecided, the reduct/expansion
distinction already prevents a false constitutional fork.

### N7 — strongest steelman

The strongest objection is persuasive in part: the axiom memo is English, not
a published many-sorted signature. “Each site has a domain” could be intended
only up to a representation, and a sophisticated physical duality may map
microscopic sites to distributed subalgebras while preserving every observable
fact. Therefore the prose alone cannot establish the final *physical*
equivalence category.

That objection does not defeat the narrower result. Any formalization that
allows a single owned domain to split while claiming to preserve the same site
and ownership structure is not an isomorphism of the stated structure. A dual
description may still be physically equivalent, but then “physical
equivalence” is a broader downstream relation between representation
expansions, not the foundation's internal model isomorphism. The minimum
definition makes this level distinction explicit without ruling out duality.

### N8 — cross-cycle echo

The result echoes rather than silently revises the preceding exercise chain:

- Cycle 19 showed that a fixed decoder can operationally distinguish primitive
  phase updates.
- Cycle 20 showed that complete protocol transport restores exact finite
  full abstraction, conditional on category closure.
- Cycle 21 classified the fixed-net, pointer-only, and transported-net
  algebraic cases.
- This cycle identifies the supplied foundation as the abstract site/fiber
  reduct, locates concrete nets in representation expansions, and shows why a
  useful dynamic quotient must retain uniform locality and record histories.

The recurring wall is not “we have not chosen the prettiest representation.”
It is that law equivalence, first occurrence, later formation, and actuality
are distinct missing interfaces. The semantic interface can now be closed by
definition without spending an axiom. The three physical interfaces remain
science work.

## 12. Final bounded conclusion

The exact answer is two-level:

1. **Inside the supplied foundation:** site objects must map to site objects,
   and each abstract `M2` possibility fiber must map as a whole to one target
   site's fiber. This follows from a faithful model of the existing language.
2. **Between concrete realizations or laws:** the foundation has not supplied
   a global tensor embedding or physical equivalence category. Transported
   distributed subfactors can be legal only as morphisms between expanded
   representations, subject to a downstream definition that preserves the
   named operational structure.

An unconstrained history-frame quotient is too broad: it gauges every finite
reversible edge to identity. The smallest non-destructive law quotient is
compositional, uniformly local, and record-history/readout preserving. Even
then, nonunitary record effects, transcript structure, readable cost, and QCA
locality invariants survive.

So the current axiom add for this issue is **none**. If clarity is wanted, add
one definitional sentence to Qualification and one stronger sentence to the
downstream law-equivalence definition. Keep the constitutional budget for
physics the framework truly cannot derive: occurrence/trigger, actuality and
weights, and any exact update atom that survives the completed quotient.
