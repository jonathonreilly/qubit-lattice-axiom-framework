# Adaptive Record-Protocol QCA Full-Abstraction Theorem

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exploratory finite-protocol theorem,
change-of-frame construction, and boundary stress test. It is not an axiom
proposal, primitive, retained theorem, physical-equivalence declaration,
record-category selection, canonical-law choice, premise registration, or
audit verdict. It changes no axiom, registry, primitive, audit, review queue,
or retained surface.

**Outcome class:** exact-positive-with-conditional-domain-and-explicit-breaks.
The adaptive finite-history transport theorem is exact. Whether it is a
physical equivalence depends on closure of the allowed record, boundary, and
cost category under the transport.

## Constitutional And Primitive Contract

The active foundation remains:

- [`MINIMAL_AXIOMS_2026-06-29.md`](../../../MINIMAL_AXIOMS_2026-06-29.md);
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](../../../KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md);
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](../../../REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md); and
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](../../../SCALE_REFERENCE_PRIMITIVE_NOTE.md).

No approved primitive defines physical equivalence, an instrument category,
an allowed boundary sector, or a QCA representative. `Records form` supplies
global occurrence but not the first-record condition, later trigger truth
tables, weights, or actual-member semantics.

This note attacks the live escape from
[`PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md`](PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md):
perhaps finite-depth-related QCA representatives are exactly the same physics
when every preparation, adaptive intervention, decoder, instrument, record,
and downstream observable is transported together.

The theorem below is deliberately broader than a fixed final measurement. It
covers finite adaptive protocol trees with arbitrary finite-outcome completely
positive instruments and history-dependent local frame changes.

## Result In Plain Language

There is a real full-abstraction theorem for finite protocols.

Take any finite experiment in which each next operation can depend on every
record written so far. At every history node, change representation by a
unitary `F_h`. Transport each branch operation by putting the old operation
between the inverse frame at its input and the new frame at its output. Then
all intermediate frame factors cancel along every history.

The result is exact, not approximate:

- every complete instrument remains complete;
- every adaptive transcript has exactly the same probability;
- every normalized post-record state is related by the endpoint frame;
- every later intervention can use the same prior labels;
- every transported future read has the same conditional statistics;
- composition and identities are preserved;
- any clock, capacity, or scalar cost that is a function only of the same
  record labels and event times is unchanged; and
- the construction works branch by branch, including zero-probability branch
  handling.

This is the strongest positive equivalence result reached in the exercise. It
shows that a finite-depth representative need not be selected if the complete
operational package forms a category closed under the frame transport.

But category closure is physical content. Three exact breaks matter.

1. **Local permanent records.** A phase frame preserves computational
   (`Z`) record projectors, so it is a legal equivalence inside a
   `Z`-record protocol category. The same frame sends a local `X` record
   projector to a two-site operator. If an `X` record is admissible and a
   record must remain one local locked possibility, the transported object is
   not a legal record. The functor then exits the physical protocol category.
2. **Boundary sectors.** The phase frame fixes an all-zero/product boundary,
   but it entangles a `|++>` boundary patch. A boundary held physically fixed
   can distinguish representatives unless it is transported too or is
   invariant under the frame.
3. **Readable implementation cost.** The theorem preserves label times and
   costs because it adds no events. If implementing a transport writes an
   extra permanent phase/schedule certificate, the wrapped protocol has an
   additional readable record, additive readout, clock tick, and capacity
   cost. It is not in the theorem's equivalence class.

For the primitive controlled-phase family from Cycle 19 the answer is now
precise.

- **If only the update changes and the record protocol is held fixed, the
  family remains separable.** The Cycle-19 Bell decoder writes different
  records after one update.
- **If the whole finite adaptive protocol is transported, the family is fully
  gauge inside every protocol category closed under the frame family.** For
  repeated phases the required time-dependent frame is itself range one and
  bounded depth at every time.
- **It is not automatically gauge in the maximal local-record category.** A
  nontrivial phase frame does not preserve every one-site record algebra.

Thus the phrase “finite-depth circuits are gauge” is incomplete. The correct
statement is:

> A representative change is gauge relative to a named protocol category
> only when it induces a local, label-preserving autoequivalence of that
> category and preserves its record, boundary, clock, and resource
> structures.

The theorem retires the representative phase only conditionally. It does not
select the allowed record category, cause the first record, choose an actual
branch, or derive probability.

## 1. Primary-Source Boundary

The external comparison uses only primary sources. They are not framework
authority.

| Primary source | Use here | Boundary |
|---|---|---|
| [Schumacher and Werner, *Reversible quantum cellular automata*](https://arxiv.org/abs/quant-ph/0405174) | QCA evolution is a finite-propagation automorphism, so local operators remain supported in bounded neighborhoods. | This does not say which local record subalgebras are physically allowed. |
| [Haah, *Clifford Quantum Cellular Automata: Trivial group in 2D and Witt group in 3D*](https://arxiv.org/abs/1907.02075) | Circuit/shift/stabilization equivalence is an exact QCA-class relation in the stated Clifford setting. | Its quotient does not automatically preserve a fixed external record protocol. |
| [Yang, *Categorifying Clifford QCA*](https://arxiv.org/abs/2504.14811) | The categorical viewpoint classifies stabilized Clifford QCAs modulo the named trivial morphisms. | A mathematical quotient becomes physical equivalence only after the operational object class is specified. |
| [Sun et al., *Clifford quantum cellular automata from topological quantum field theories and invertible subalgebras*](https://arxiv.org/abs/2509.07099) | Current explicit anomalous constructions confirm that nontrivial bulk classes and boundary algebras can be handled constructively. | They do not prove closure of this framework's permanent-record protocol category under all representative changes. |

The adaptive theorem itself is elementary finite-dimensional operator algebra
and is proved below and in the companion runner.

## 2. Finite Adaptive Protocol Category

Fix a finite horizon `T`. A record history at depth `t` is

```text
h=(r_1,...,r_t).
```

At node `h`, let the unnormalized branch state be `sigma_h`. The next adaptive
instrument may depend on the complete history. Its branch `r` has one or more
Kraus operators

```text
K_(r,a)^h,
```

with finite outcome label `r` and internal Kraus label `a`, satisfying

```text
sum_(r,a) (K_(r,a)^h)^dagger K_(r,a)^h = I.
```

The branch recursion is

```text
sigma_(hr)
 = sum_a K_(r,a)^h sigma_h (K_(r,a)^h)^dagger.
```

Every update, adaptive intervention, decoder, and record-writing operation can
be included in the relevant `K`. Separating a unitary update `U_h` merely
writes `K_(r,a)^h=M_(r,a)^h U_h`.

The transcript probability and normalized branch state are

```text
p(h)=Tr(sigma_h),
rho_h=sigma_h/p(h)  when p(h)>0.
```

An allowed future read at `h` is a local effect or observable `O_h`. A
record-defined clock/resource functional is any declared function

```text
c(h; tau_1,...,tau_t)
```

of record contents and their event times. This definition is deliberately
wide: it includes adaptive protocols, feed-forward, repeat reads, and record
count/capacity observables.

## 3. Adaptive Frame-Transport Theorem

Choose a unitary frame `F_h` at every history node. It may depend on all prior
records. Define

```text
sigma'_empty = F_empty sigma_empty F_empty^dagger,

K'_(r,a)^h
 = F_(hr) K_(r,a)^h F_h^dagger.
```

Keep the classical outcome label `r` unchanged.

### Theorem

For every finite adaptive protocol tree:

1. every transported node instrument is complete;
2. for every history `h`,

   ```text
   sigma'_h=F_h sigma_h F_h^dagger;
   ```

3. `p'(h)=p(h)`;
4. when `p(h)>0`, `rho'_h=F_h rho_h F_h^dagger`;
5. a future observable transported as

   ```text
   O'_h=F_h O_h F_h^dagger
   ```

   has identical conditional expectations; and
6. every label/time functional `c(h;tau_1,...,tau_t)` is identical.

### Proof

Completeness at node `h` is

```text
sum_(r,a) (K'_(r,a)^h)^dagger K'_(r,a)^h
 =F_h [sum_(r,a) (K_(r,a)^h)^dagger K_(r,a)^h] F_h^dagger
 =I.
```

Assume inductively that `sigma'_h=F_h sigma_h F_h^dagger`. Then

```text
sigma'_(hr)
 =sum_a F_(hr) K_(r,a)^h F_h^dagger
        F_h sigma_h F_h^dagger
        F_h (K_(r,a)^h)^dagger F_(hr)^dagger
 =F_(hr) sigma_(hr) F_(hr)^dagger.
```

The base case is the transported preparation. Trace invariance gives the
probabilities; normalization gives the conditional states. Observable
expectations follow by cyclicity of trace. The history labels and their times
were not changed, so every declared label/time cost is equal.

Adaptivity needs no extra proof. Both trees arrive at the same classical
history label with the same probability, so they select corresponding
history-indexed instruments at the next node.

## 4. Functor And Natural-Isomorphism Data

The theorem has an exact category form.

Let `P_T` have:

- objects: history-labelled time-slice algebras/states together with their
  local record and boundary structures;
- morphisms: outcome-labelled local completely positive maps;
- composition: ordinary CP-map composition along a fixed history; and
- classical branching: concatenation `h -> hr`.

The frame family defines a candidate functor `T_F`:

```text
T_F(A_h)=F_h A_h F_h^dagger,

T_F(M_(h->hr))
 =Ad_(F_hr) o M_(h->hr) o Ad_(F_h^dagger).
```

It preserves identities and composition exactly:

```text
T_F(N o M)=T_F(N) o T_F(M).
```

The components

```text
eta_h=Ad_(F_h)
```

give the natural isomorphism; every branch square commutes:

```text
eta_(hr) o M_(h->hr)
 =T_F(M_(h->hr)) o eta_h.
```

Inverse frames `F_h^dagger` define the inverse functor. Thus `T_F` is an
equivalence of the *mathematical* finite protocol categories.

It is an autoequivalence of the *physical allowed* protocol category only if
it preserves the extra structures defining allowed objects and morphisms:

- locality and a uniform support bound;
- one-site record algebras and their content labels;
- permanence of already formed records;
- allowed preparation and boundary sectors;
- allowed intervention/decoder class;
- record event times and additive costs; and
- any clock, capacity, matter, or gravity observable claimed physical.

This is the exact point where bare category theory meets physics.

## 5. Locality And Infinite-Time Qualification

For a finite horizon, if every `F_h` is locality preserving and every original
morphism is local, every transported morphism has finite enlarged support.
A QCA maps a finite local algebra into a bounded neighborhood; conjugating a
bounded-depth circuit by a QCA remains bounded depth after a finite recoloring
of the enlarged gates.

For an infinite-time equivalence, finite support at each fixed time is not
enough. The frame family needs a uniform locality/range bound, otherwise a
later “local” record may spread over an ever-growing region. The theorem is
finite-horizon without that extra uniformity.

The primitive phase family below passes the stronger test: its frame has range
one and the same six-layer depth bound at every time.

## 6. Multi-Time Primitive Phase Family

Let

```text
U_1=C_(phi_1),
U_2=C_(phi_2),
delta=phi_2-phi_1,
```

where each `C_phi` is the unit-translation/proper-cubic all-edge phase circuit
from Cycle 19. For repeated updates choose

```text
F_t=C_(t delta),
F_0=I.
```

All phase circuits commute and their angles add, so

```text
F_(t+1) U_1 F_t^dagger
 =C_((t+1)delta) C_(phi_1) C_(-t delta)
 =C_(phi_2)
 =U_2
```

at every time. `F_t` remains an all-edge range-one commuting circuit with the
same six-layer depth bound, independent of `t`. Therefore every finite
adaptive protocol for `U_1` has an exact transported protocol for `U_2`, and
the locality overhead does not grow with time.

This proves full gauge equivalence for the phase family relative to any
protocol category closed under all `F_t`.

It does not identify the two laws when only `U` changes. Holding the Cycle-19
Bell decoder fixed gives different first-step records. The paired
counterprotocol remains legal whenever that preparation and decoder are
allowed.

## 7. Permanent Local Record Normalizer Test

Let

```text
P_Z+=(I+Z)/2,
P_X+=(I+X)/2.
```

For a two-site controlled phase `C_delta`:

```text
C_delta (P_Z+ tensor I) C_delta^dagger
 =P_Z+ tensor I.
```

So `Z` records remain one-site records with unchanged content. The frame
functor is label-preserving on this record algebra.

For nontrivial `delta`, however,

```text
Q_X=C_delta (P_X+ tensor I) C_delta^dagger
```

generically acts on both sites. The companion runner verifies that `Q_X` fails
to commute with a neighboring `X`, which every operator of the form
`A tensor I` would commute with. It is not one local locked possibility at the
original record site.

At `delta=pi`, applying `CZ` to `|++>` makes the first site's reduced state
maximally mixed. A fixed pre-existing `X+` record would no longer return `X+`
with certainty. Thus the frame is not in the normalizer of that local record
algebra.

There are three honest responses:

1. prove the exact law only admits a `C_phi`-normalized pointer/record algebra;
2. transport the record encoding to a distributed algebra and prove that such
   an encoding still satisfies the one-site Record axiom; or
3. accept that the representatives are physically distinct in a protocol
   category containing fixed local `X` records.

The four axioms do not choose among these. Qubit says no possibility is
privileged; Admissibility may still select a context-specific subset, so this
is a conditional break, not a universal contradiction.

## 8. Boundary-Sector Test

A frame equivalence between boundary-conditioned theories requires

```text
F_h B_h = B'_h
```

for the allowed boundary sector `B_h`.

The phase frames fix the computational vacuum:

```text
C_phi |0...0>=|0...0>.
```

They therefore preserve a strict all-zero exterior. But on an adjacent
`|++>` boundary patch, `CZ` creates an entangled graph-state edge and changes
the one-site purity from one to one half. A product-coherent boundary held
fixed is not invariant.

Transporting the boundary state restores mathematical equivalence. Holding
the same physical boundary in both descriptions can select or distinguish a
representative. The realized-state primitive permits pointwise reference to a
realized boundary but neither chooses it nor declares boundaries equivalent.

## 9. Additive Record, Clock, And Resource Cost

Inside the theorem, histories and event times are identical. Therefore any
cost of the form

```text
C(h)=sum_j c(r_j,t_j)
```

is exactly preserved. This includes record count, content-additive scalar
readout, a clock defined by record-event count, and any capacity debit assigned
to those same events.

The result does not license a physical implementation wrapper for free.
Compare:

```text
direct:   input -> output record,
wrapped:  input -> phase certificate record -> output record.
```

They may have the same decoded output, but the wrapped history contains one
extra permanent readable event. Its record count, additive cost, causal depth,
and capacity use differ. No label-preserving functor of the theorem maps a
one-event history to a two-event history.

Thus a finite-depth frame can be treated as a passive mathematical change of
description at no record cost. If the exact substrate must *execute* the frame
through additional record-writing schedule steps, those steps are physical
and must be included. Gate count alone is not currently a framework
observable; record-writing overhead is.

## 10. Adaptivity, Future Reads, And Actuality

Because the theorem is branchwise, an operation selected after records
`(r_1,r_2)` transports to the corresponding operation after the same labels.
Normalized post-record states are related by `F_h`, so every transported later
read agrees. The companion runner uses a depth-three binary tree in which the
second and third instruments genuinely depend on prior labels and verifies all
eight terminal branches.

This is operational distribution equivalence, not actual-history selection.
If one branch is ontically realized, the theorem maps its label and conditional
state, but it does not say why that branch rather than another is actual. It
also assumes the first instrument fires. First-record nucleation and
actual-member semantics remain separate.

## 11. Exactly Derived Clauses

| ID | Exact clause | Scope |
|---|---|---|
| D1 | History-dependent unitary frames transport every finite adaptive CP-instrument tree with identical transcript probabilities. | Finite horizon, finite outcomes. |
| D2 | Completeness, normalized post-record states, future reads, composition, identities, and adaptivity are preserved. | Exact operator identities. |
| D3 | Label/time-defined additive record, clock, and resource costs are preserved without extra events. | Costs are functions of the same history. |
| D4 | The transport is a functor with inverse and natural-isomorphism components `Ad(F_h)`. | Mathematical protocol category. |
| D5 | It is a physical autoequivalence only if allowed local records, boundaries, interventions, and observables are closed under the frames. | Conditional physical interpretation. |
| D6 | Repeated primitive phase laws have uniform range-one frames `F_t=C_(t delta)`. | All-edge commuting `C_phi` family. |
| D7 | With complete protocol transport, the phase family is fully gauge in every closed category. | Does not select the category. |
| D8 | With only the update changed, a fixed legal Bell decoder separates the family. | Cycle-19 counterprotocol. |
| D9 | `C_phi` frames preserve local `Z` record projectors but not generic local `X` record projectors. | Exact two-site normalizer test. |
| D10 | Vacuum boundaries are preserved; coherent product boundary patches need not be. | Exact finite boundary fixtures. |
| D11 | Adding a readable implementation certificate changes additive record/clock/capacity cost and lies outside the label-preserving theorem. | Exact direct/wrapped histories. |
| D12 | Neither frame transport nor full abstraction causes the first record or selects one actual member. | Logical separation. |

No axiom sentence follows from D1-D12.

## 12. Collapsed Survivor Set

The representative field `X` can now be retired under an explicit conditional:

```text
E = the allowed physical protocol category is closed under a uniformly local,
    record/boundary/cost-preserving frame autoequivalence.
```

The collapsed open set is:

```text
P  = primitive anomalous one-M2 QCA existence/compiler,
E  = selection and proof of the full allowed protocol-category equivalence,
O0 = first-record nucleation/domain,
O1 = subsequent formation-trigger domain,
A  = actual-member and weight semantics.
```

Record-algebra normalizer, boundary preservation, and additive cost are
sub-obligations of `E`, not three independent axiom walls. If any fails for an
allowed protocol, `X` remains a physical representative field for that
category.

The clock, tensor, and species equations from prior cycles are not solved by
this categorical theorem. `E` can remove representational dependence from
them only after their physical observable maps are supplied.

## 13. Bare-Metal And Axiom Consequence

The strongest zero-edit path is clearer now. A final TOE need not choose one
microscopic circuit spelling if it proves a complete local operational
equivalence class. But “same bulk index” is too weak. The equivalence must
preserve the universe's actual commit interface and every observable defined
from it.

A useful framework-level criterion is:

> A microscopic representation change is physically inert exactly on the
> domain of allowed protocols for which it preserves local record identity,
> permanent history, boundary sector, and every record-defined observable.

That is a theorem/definition target, not proposed axiom text. Adopting it
without identifying the allowed record category could silently erase legal
record differences. Requiring it as a proof obligation can reduce the exact
law without adding physics.

No verbatim axiom addition is recommended. The cycle instead sharpens the
object that formation language must eventually accompany: not a bare update,
but an update-plus-record protocol modulo a proved full operational
equivalence.

## No-Go Discipline Gate

**Gate status:** PASS for the exact finite adaptive theorem and the scoped
record/boundary/cost breaks. A universal obstruction to full operational
equivalence would FAIL N7. Outcome remains
`exact-positive-with-conditional-domain-and-explicit-breaks`.

### N1 — Alternative-Route Enumeration

1. **ATTEMPTED — fixed final instrument transport.** Generalized successfully
   to arbitrary finite adaptive instrument trees.
2. **ATTEMPTED — history-dependent frames.** Exact branchwise transport works
   even when `F_h` depends on prior records.
3. **ATTEMPTED — future read and normalized-state transport.** Both follow
   exactly from the endpoint conjugation.
4. **ATTEMPTED — composition/functor route.** Identities, composition, inverse
   frames, and the natural squares are exact.
5. **ATTEMPTED — repeated primitive phase law.** Uniform-local frames close the
   full multi-time family in a frame-closed category.
6. **ATTEMPTED — fixed protocol counterexample.** Changing only the phase
   update leaves the Cycle-19 readable transcript separator intact.
7. **ATTEMPTED — permanent local-record normalizer.** `Z` records survive;
   generic `X` records leave the one-site record algebra.
8. **ATTEMPTED — boundary transport.** Vacuum is invariant while a coherent
   product patch is not.
9. **ATTEMPTED — additive cost.** Label-preserving transport preserves it;
   adding a readable implementation certificate does not.
10. **ATTEMPTED — first-record route.** Every construction presupposes the
    preparation/protocol tree; no nucleation result follows.

The broad finite theorem is positive. The breaks license only conditional
domain statements, not a universal no-go.

### N2 — Wall-Independence Audit

After absorbing record normalizer, boundary, and cost preservation into `E`,
the five fields are `P,E,O0,O1,A`. Every entry is `N/N`.

| Pair | Row implies column? / column implies row? | Witness |
|---|---|---|
| P-E | N/N | a primitive anomalous update does not select its physical protocol category; a category equivalence does not construct the update |
| P-O0 | N/N | reversible update existence does not make the first record; a seed does not choose the anomaly |
| P-O1 | N/N | QCA class does not select the later event truth table |
| P-A | N/N | automorphism construction and actual-member semantics are distinct |
| E-O0 | N/N | frame transport presupposes a protocol; first occurrence does not prove category closure |
| E-O1 | N/N | equivalence transports a supplied trigger/instrument but does not select when it fires |
| E-A | N/N | equal branch laws do not choose one ontically actual branch |
| O0-O1 | N/N | a supplied or uniform seed does not determine later propagation triggers |
| O0-A | N/N | first formation and actual-member selection are separate |
| O1-A | N/N | firing an instrument does not explain one realized member |

No standalone representative phase is counted in addition to `E`.

### N3 — Hidden-Wall Scan

| Phrase or close variant | Classification |
|---|---|
| “finite protocol” | Explicit theorem domain; infinite time needs uniform locality. |
| “allowed protocol category” | Explicit physical input inside `E`; not derived from the axioms. |
| “local record” | One-site Record-axiom requirement; context admissibility remains conditional. |
| “boundary sector” | Explicit object structure; realized-state primitive does not select it. |
| “record-defined cost” | Explicit functional of labels/times; gate cost is not silently identified with it. |
| “complete transport” | Exact functor data, not mere update conjugacy. |
| “canonical-law choice” | Appears only in the authority disclaimer and states what the note is not. |

The proof contains no load-bearing “we assume,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,” “obviously,”
or “standard QFT” shortcut. The primitive registry was inspected before the
collapsed set.

### N4 — Exact Residual Matching

| Witness | Witness residual | Present residual | Match? |
|---|---|---|---|
| Cycle-19 primitive protocol note | one-step full transport succeeds; multi-time/full category remains live | adaptive theorem and `E` | yes |
| Cycle-19 fixed decoder | update-only change yields readable transcript difference | D8 fixed-protocol separator | yes |
| Intrinsic-simulation observer-equivalence note, authority-free | extra readable certificates defeat decoded equivalence | additive-cost break | yes in shape; echo only |
| Record-instrument audit, authority-free | context remains after rank-one repeatability | allowed local record algebra inside `E` | partial; echo only |
| Minimal axioms | local permanent records, global occurrence; no protocol quotient/formation rule | `E/O0/O1/A` | yes |
| Realized-state primitive | pointwise history without boundary/selection | boundary and actuality remain explicit | yes |

Authority-free echoes are not used as retained support.

### N5 — Resolution And Rhetoric Audit

Tested resolutions:

- **per branch:** Kraus-map transport;
- **per adaptive node:** instrument completeness;
- **per finite history:** unnormalized/normalized state and cost;
- **per finite protocol tree:** functor, inverse, composition, adaptivity;
- **per primitive lattice update:** repeated `C_phi` uniform-local frame;
- **per local record:** `Z` and `X` normalizer fixtures;
- **per boundary patch:** vacuum and `|++>` controls; and
- **all infinite protocols/all record contexts:** not proved.

Allowed wording:

- “the finite adaptive theorem is exact”;
- “the phase family is gauge inside a frame-closed protocol category”;
- “a fixed allowed `X` record can break that closure”; and
- “update-only changes remain distinguishable by the fixed decoder.”

Disallowed wording:

- “all finite-depth representatives are physically equivalent”;
- “the Record axiom forbids phase frames”;
- “every local possibility can become an `X` record in every context”;
- “full abstraction fails universally”; and
- “actuality follows from natural isomorphism.”

The note uses only the tested forms.

### N6 — Partial-Closure Paths And Primitive Registry

The primitive registry was checked directly. Existing closure routes are:

1. Prove the exact law selects a pointer/record algebra normalized by the frame
   family; then the `X`-record break is outside the allowed category.
2. Prove transported distributed record encodings are operationally one local
   record with unchanged additive cost; then the apparent locality break may
   retire.
3. Treat the frame as passive representation, adding no record events; then
   label/time costs are exactly preserved by D3.
4. If implementation requires schedule records, include them and test a larger
   cost-preserving functor rather than calling them free.
5. Transport a supplied physical boundary as part of the representation; if
   the boundary is fixed empirical data, require it to be invariant instead.
6. Introduce `E` as a verbatim conditional import in bounded downstream
   theorems and run an import-retirement audit after the exact law is known.
7. `Records form` already closes global occurrence. The theorem creates no new
   axiom need for `O0/O1` merely because it does not derive them.

The result is a conditional reduction path, not “new axiom required.”

### N7 — Strongest Surviving Steelman

A hostile reviewer should reject the `X`-record break as representation
fixing. The transformed two-site projector may be the same physical one-site
record expressed in a different tensor-factor presentation; locality itself
could be transported by the QCA. A complete algebraic net equivalence might
map sites, record subalgebras, and boundary sectors together while preserving
all operational inclusion and additive-readout relations. If the primitive
exact law defines records only through such relational subalgebras, demanding
that `F` fix the original `P_X tensor I` is no more physical than demanding a
coordinate transformation fix a coordinate component. The adaptive theorem
already supplies the necessary natural isomorphism at every history.

This is convincing. The present framework, however, explicitly names sites
and one-site local possibilities, so a successful steelman must prove that the
transported net still satisfies that ontology and does not change record
cost. The route remains live; a universal obstruction is not licensed.

### N8 — Cross-Cycle Echo

1. Cycle 19 found exact one-step equivalence only after decoder/instrument
   transport. This cycle closes finite adaptivity and exposes the physical
   object-category condition.
2. The intrinsic-simulation note found extra readable phase certificates break
   equivalence. Here label-preserving functorial transport proves precisely why
   no-extra-record frames avoid that break.
3. The record-instrument audit left context selection open after deriving
   repeatable rank-one form. Here the allowed record algebra is the same
   context input at category scale.
4. The dynamic-boundary cycles separated post-record geometry from first
   nucleation. Frame transport remains post-protocol and does not alter that
   separation.

Prior walls narrowed by full transport, convention, or category restriction
are carried into N6. No authority-free cycle is treated as retained proof.

## Companion Runner

Run:

```bash
python3 scripts/adaptive_record_protocol_qca_full_abstraction_probe_2026_07_14.py
```

It verifies a depth-three adaptive binary protocol tree, history-dependent
frames, completeness at every node, branch probabilities, normalized states,
future reads, costs, composition/naturality, repeated `C_phi` frame recurrence,
update-only separation, `Z/X` record normalizers, boundary fixtures,
direct/wrapped record costs, collapsed residuals, N1-N8 visibility, and local
links.
