# Self-Describing Law and Foundation Selection — Cycle 49

**Date:** 2026-07-14

**Type:** authority-free foundation-selection attack, exact finite
self-description counterexample, positive singleton construction, and fresh
N1–N8 bounded no-go audit

**Authority:** none. This note does not amend an axiom, enlarge a primitive,
identify the physical law or boundary, issue an audit verdict, or authorize a
commit, push, PR, publication, or constitutional edit. It is a local exact
probe only. No live axiom, primitive, registry, audit, commit, or PR surface is
changed.

Companion runner:

```text
scripts/self_describing_law_foundation_selection_cycle49_2026_07_14.py
```

## Question

Cycle 45 proved a strong conditional result: a complete permanent corpus can
reconstruct its history, and a universal-context corpus can reconstruct a
complete deterministic local response table. Its self-describing-law
steelman left one question open:

> If the universe writes a complete description of its own rule into records,
> does the description itself remove the still-missing identity of the rule?

The distinction to test is small but constitutional:

```text
the actual corpus identifies which law generated it
```

is not automatically the same statement as

```text
the current foundation permits only that law.
```

This cycle constructs two different complete finite local response laws, gives
them the same self-description apparatus and decoder, and asks whether
self-description has one fixed point or more than one. It then states the
exact foundation-wide condition that would force one fixed point and searches
for a positive finite-class route that satisfies it.

## Result Up Front

Self-description does **not by itself** remove the law-identity atom, even in
the cleanest finite deterministic case. It changes how a law can be learned;
it does not uniquely choose which self-describing law Nature instantiates.

The runner supplies one exact conditional operational sector. A central
binary pointer value is surrounded by the six cubic nearest-neighbor pointer
values. Proper cubic rotations alone give **10** neighbor-pattern orbits and
therefore **20** contexts after the central bit is included. The probe then
supplies the stronger **totalism** condition: response depends on the six
neighbors only through their Hamming count. Totalism reduces the test domain
to the 14 count contexts

```text
(c,k),  c in {0,1},  k in {0,...,6},
```

where `k` is the number of neighboring ones. Define

```text
L_A(c,k) = c XOR (k mod 2),
L_B(c,k) = 1 XOR c XOR (k mod 2).
```

Both rules are:

- independent of lattice position;
- invariant under all 24 proper cubic rotations;
- covariant under simultaneous exchange of the two binary pointer labels;
- genuinely sensitive to nearest-neighbor conditions; and
- distinct on every one of the 14 supplied totalistic count rows.

The same universal table writer realizes every row in an actual far-separated
cubic context block and appends the response at a distinct open target whose
six-neighbor condition is explicitly checked. Fixed spatial/causal role
metadata links the output records without adding another onsite content, and
contains no law name. The same decoder reconstructs the exact 14-row table
despite storage-order scrambling, reversed schedules, or cyclic schedule
phase. Nevertheless,

```text
Decode(C_A) = L_A,
Decode(C_B) = L_B,
L_A != L_B.
```

Self-description therefore has **two fixed points** in this exact witness.
The corpus `C_A` empirically identifies `L_A`; `C_B` empirically identifies
`L_B`. Neither fact explains why the current foundation would permit only one
of those two worlds.

This is not a universal no-go. It is a bounded counterexample to the inference
“self-describing implies uniquely foundation-selected.” A stronger theorem
could still remove the constitutional law identifier with zero axiom words.
The exact self-description route needs **coverage plus foundation-wide
self-description confluence**. The complete classes reconstructed by certified
packages must cover every foundation-permitted complete record-law class, and
that covered image must contain exactly one record-faithful class. A singleton
image without coverage can merely omit an untested rival.

A positive finite route was found. In the declared eight-law
affine-totalistic class

```text
L_(a,b,d)(c,k) = a c XOR b(k mod 2) XOR d,
```

global pointer-label covariance reduces `8 -> 4`, genuine neighbor variation
reduces `4 -> 2`, and the added condition

```text
L(0,0)=0 and L(1,6)=1
```

reduces `2 -> 1`, selecting `L_A`. This is the **Affine-totalistic singleton
theorem**. In plain language, the last condition says that a completely
uniform situation persists rather than flipping merely because it is uniform.

That positive route is exact but not yet foundation closure. The current
foundation does not supply a binary pointer basis, totalism, or an exhaustive
affine-totalistic family; it also does not state global pointer-label
covariance as a law symmetry or uniform-state persistence.
The route is a sharply specified derivation target or candidate-law contract,
not a silently available consequence of the four axioms.

## 1. Scope: A Complete Finite Law, Not a Complete TOE

The word `complete` is resolution-sensitive here. The witness laws are
complete on the exact finite domain of supplied totalistic Boolean pointer
contexts: every one of the 14 count rows has one answer. Proper-cubic
covariance by itself has 20 contexts, which the runner independently
enumerates. The tables are not claimed to specify
the full `M_2(C)` possibility domain, coherent phases, overlapping-update
composition, stochastic records, boundary conditions, matter, gravity, or
the complete TOE interfaces.

The Boolean pointer sector is a **conditional operational sector** embedded in
the one-site qubit possibility domain. The following are supplied for the
probe and are not read out of the current axioms:

1. one binary pointer pair and its scalar record-content dictionary;
2. legal preparation of each local totalistic count context;
3. a scheduler that presents all 14 contexts;
4. an append-only table-record layout with causal headers;
5. a decoder from those records to the table; and
6. the declared affine-totalistic class for the positive selection pass.

This typing matters. The finite witness proves that the *property* of exact
self-description is not a uniqueness property. It does not prove that either
table is the physical law, that the finite pointer class is exhaustive, or
that two complete Qubit/QCA/TOE laws necessarily survive every future
constraint.

### Compatibility with the current foundation

The current Admissibility axiom supplies one fixed translation- and
proper-cubic-covariant nearest-neighbor rule in each model, while expressly
supplying no dynamics or record-production process. To make “same foundation
reduct” executable rather than rhetorical, the witness fixes one common reduct
before either downstream response table is added.

At every site the common role domain is `M_2(C)`. Four displayed rank-one
possibilities in it are

```text
P0 = |0><0|,       P1 = |1><1|,
PX = |+><+|,       PY = |+i><+i|.
```

For an arbitrary nearest-neighbor condition

```text
eta=(eta_1,...,eta_6),
```

each `eta_j` is either open or carries arbitrary `M_2(C)` record content. Let
`N(eta)` be the number of present neighboring records. Both expansions use
exactly the same total nearest-neighbor predicate

```text
Avail(eta) = M_2(C) minus {PY}  when N(eta) is even,
Avail(eta) = M_2(C) minus {PX}  when N(eta) is odd.
```

This rule is defined for every six-neighbor condition, not only for the binary
test rows. It is translation independent, proper-cubic covariant, and
genuinely varies with neighbor occupancy while ignoring the arbitrary value of
present content. It always admits both possible binary response records `P0`
and `P1`. Both expansions also use the same total one-site scalar readout

```text
i(A)=Re Tr(P1 A),
I(F)=sum_(x in F) i(A_x),
I(empty)=0,
```

for arbitrary `A in M_2(C)` and every finite pairwise-disjoint record
collection `F`. Thus readout is content-only and additive without restricting
the common reduct to four named roles; in particular `i(P0)=0` and `i(P1)=1`.

Only after that common Lattice/Qubit/Admissibility/Record reduct and the shared
test apparatus are fixed are `L_A` and `L_B` added. They are downstream
response-law expansions, not two proposed readings of Admissibility.

The apparatus gives each of the 14 rows its own far-separated cubic block. The
block center carries `P0` or `P1` for `c`; its six sites at the exact cubic
nearest-neighbor directions carry a representative arrangement of `k` copies
of `P1` and `6-k` copies of `P0`. Every such apparatus record is admissible
because `P0` and `P1` are admitted under every neighbor condition. Each row
also has a distinct initially open storage target. The target together with
its six-neighbor shell is disjoint from all context records and every other
storage block; its actual pre-write neighbor tuple is six open sites. The
writer verifies that the target is absent and that the selected `P0` or `P1`
is admitted under that actual tuple before appending it. It never changes an
old record.

Event and parent identifiers are fixed spatial/causal role metadata: the event
role names the context block and the parent role names the preceding block in
the scheduled causal chain. They are not extra onsite `M_2(C)` contents. The
only onsite output content is the locked projector `P0` or `P1`; the decoder
recovers `(c,k)` from the actual center-and-neighbor apparatus records.

The scheduler's row order and its line of storage sites are contingent
apparatus/history structure. They need not be lattice-rotation invariant. The
law's response to a rotated physical context is what must be covariant, and
that is checked against all 24 proper rotations and all 128 labeled binary
neighborhoods.

Calling these expansions “foundation-compatible” means that deleting the
downstream response table leaves the same explicit, total reduct just
displayed. It does **not** mean that the foundation derives totalism, the
Boolean pointer decoder, the response/update interpretation, the apparatus,
its spatial/causal role metadata, or a strict nearest-neighbor implementation
of the table writer.

## 2. The Two Self-Describing Table Writers

### Exact local tables

Let the six neighbor slots be `+x,-x,+y,-y,+z,-z`. For labeled bits
`n_1,...,n_6`, define neighbor parity

```text
p = n_1 XOR ... XOR n_6 = k mod 2.
```

Then

```text
L_A = c XOR p,
L_B = 1 XOR c XOR p.
```

Every proper cubic rotation permutes the six neighbor slots and preserves
`p`, so both laws are exactly rotation invariant. A lattice translation does
not enter either formula. Under the simultaneous exchange

```text
c -> 1-c,  n_i -> 1-n_i,  output -> 1-output,
```

six-neighbor parity is unchanged and both laws are covariant. Thus the
obvious position, orientation, and binary-label symmetry attacks do not select
between them.

The rules disagree for every context:

```text
L_B(c,k) = 1 - L_A(c,k).
```

Under the probe's fixed preparation and scalar readout dictionary, the same
context produces opposite readable record contents. They are therefore not
identified by a record-faithful quotient that preserves context identity and
scalar readout.

### Universal corpus

For each of the 14 physical context blocks the common apparatus appends one
onsite record

```text
(fresh_site, P_outcome).
```

Separately typed fixed role metadata supplies

```text
(event_role, parent_role, context_block_center).
```

There is no `law_id` field and the role metadata is not additional onsite
record content. Event and parent roles certify one causal chain; the block
center points the decoder to the seven actual context records from which it
recovers `(c,k)`. Fresh sites enforce one-record-per-site append-only storage.
The decoder checks:

1. one genesis and one connected predecessor chain;
2. unique event roles and unique record sites;
3. each role's actual center-and-six-neighbor geometry;
4. an initially absent target with a disjoint six-neighbor storage block;
5. admissibility of the output under the target's actual neighbor tuple;
6. exactly one response for every one of the 14 contexts; and
7. no conflicting duplicate row.

It then returns the extensional table. A missing row or conflicting duplicate
is rejected. Input-list order is irrelevant; three different complete
schedules reconstruct the same table for a fixed law.

### Two-fixed-point theorem

Let `W_L` be the common writer operated under table `L`, `C_L` its resulting
corpus, and `D` the common decoder. For each complete table in the declared
domain,

```text
D(W_L) = D(C_L) = L.
```

The proof is rowwise: the universal schedule contains every context exactly
once, the outcome field is `L` evaluated on that context, and the decoder
returns precisely those rows. Applying it to `L_A` and `L_B` gives two fixed
points. The table writer is therefore an identity map on the supplied law
class, not a constant selector on that class.

This is the core conceptual result:

> A mirror can perfectly report which object is in front of it while having no
> power to decide which object is placed there.

The corpus is an exact mirror of the operative law. Its accuracy is not a
foundation-level reason for one mirror image rather than another.

## 3. Empirical Identification Versus Foundation Selection

There are three separate arrows:

```text
supplied law + scheduler/boundary -> actual self-description corpus;
certified corpus + decoder/class  -> reconstructed law;
foundation                       -> unique physical law class.
```

The witness closes the first two arrows in both directions:

```text
L_A -> C_A -> L_A,
L_B -> C_B -> L_B.
```

It does not close the third. Observing `C_A` tells an inhabitant which table
is operative in that history, conditional on the decoder and exhaustive
class. It is a contingent empirical identification. A world containing
`C_B` would perform the same successful act and identify `L_B` instead.

The realized-state primitive does not repair this distinction. It licenses
pointwise evaluation at the supplied realized state; it does not make the
state or its corpus foundation-derived. Treating the actual corpus as the
selector would move the law identity into contingent boundary/history data,
unless a theorem proves that every foundation-permitted history writes the
same law class.

## 4. Exact Foundation-Level Collapse Condition

Let `F` denote the current supplied foundation, and let

```text
C_F = { [L]_record : L is a foundation-permitted complete predictive law }
```

be the set of all foundation-permitted complete record-faithful law classes.
The exact direct-uniqueness condition is simply `|C_F|=1`. That condition can
be proved without self-description at all. The question here is what a
self-description proof must establish in order to prove it.

Let a certified self-description package be

```text
P = (M, L, z, Pi, D, E),
```

where:

- `M` is a model/physical carrier compatible with `F`;
- `L` is its operative local response law;
- `z` is allowed boundary or scheduler phase data;
- `Pi` is a legal complete self-description protocol;
- `D` is a record decoder; and
- `E` is the proved unique extension from the decoded representation to a
  complete predictive law or record-protocol equivalence class.

Write `C_P` for the permanent corpus produced when the legal protocol is run
(or the counterfactual corpus fixed by the package) and

```text
R(P) = [ E(D(C_P)) ]_record
```

for the reconstructed record-faithful class. Decoder validity, protocol
completeness, response fidelity, soundness, and unique extension are part of
`Certified_F(P)`; they cannot be hidden inside the adjective “complete.”
Define the certified reconstructed image

```text
S_F = { R(P) : Certified_F(P) }.
```

The self-description route proves direct uniqueness only after two distinct
requirements are met.

### Coverage and complete extension

Every foundation-permitted complete class is represented by a certified
package, and every decoded representation extends to that complete class:

```text
C_F subseteq S_F.
```

Soundness gives the reverse inclusion `S_F subseteq C_F`, so the target is
`S_F=C_F`. This is coverage of law classes, not a demand that an actual
self-description corpus occur in every realized history. A legal
counterfactual self-test can cover a class even when a particular history
never runs it. Direct foundation uniqueness can also establish `|C_F|=1`
without any self-description package.

### Foundation-wide self-description confluence

```text
F proves:
  for all P,Q,
  Certified_F(P) and Certified_F(Q)  implies  R(P) = R(Q).
```

```text
|S_F| = 1.
```

Coverage/soundness plus confluence gives `S_F=C_F` and `|C_F|=1`, so it is a
sufficient and, within this complete reconstruction schema, exact proof of
foundation selection. Singleton `S_F` alone is not sufficient: a decoder can
write only `L_A`, produce a singleton observed image, and simply fail to cover
the still-permitted rival `L_B`. Conversely, coverage plus confluence is not a
necessary *method* for foundation selection because a direct uniqueness
theorem can prove `|C_F|=1` without a writer.

The quantifiers are load-bearing. Confluence must be independent of allowed
boundary, scheduler order, legal complete protocol, and faithful decoder.
Coverage must include every class in `C_F`, and `E` must cover the complete
law domain. Agreement among the corpora actually inspected, or agreement only
inside a preselected proper subclass, proves neither requirement.

In the finite witness, certified packages cover the supplied two-law test
class, scheduler and storage-order confluence hold *within* each law, but
cross-law confluence fails:

```text
R(P_A)=L_A != L_B=R(P_B).
```

Because the two tables give opposite scalar records in the same declared
contexts, a record-faithful equivalence cannot collapse them. An added
foundation condition must therefore exclude at least one table, change the
physical equivalence definition with a proved full-abstraction result, or
derive a richer unique law of which both tables are gauge presentations.

## 5. Positive Collapse Route

The finite search begins with every affine-totalistic rule

```text
L_(a,b,d)(c,k) = a c XOR b(k mod 2) XOR d,
a,b,d in {0,1}.
```

There are eight.

### Filter 1: global pointer-label covariance

Simultaneously complementing the central bit and all six neighbor bits leaves
neighbor parity unchanged. Requiring the output to complement therefore
forces

```text
a=1.
```

Four laws remain.

### Filter 2: genuine neighbor variation

Requiring some one-neighbor change to change the response forces

```text
b=1.
```

Two laws remain: `L_A` with `d=0` and `L_B` with `d=1`. This reproduces the
two-fixed-point witness after the symmetry and nearest-neighbor clauses have
done all the work they can do in this class.

### Filter 3: uniform-state persistence

Require a completely uniform zero context to answer zero and a completely
uniform one context to answer one:

```text
L(0,0)=0,
L(1,6)=1.
```

Because six ones have even parity, this forces

```text
d=0.
```

Exactly `L_A` remains. Its universal corpus still reconstructs it exactly, so
the restricted self-description image is now a singleton.

### What the positive result does and does not buy

The result is a genuine mathematical selection theorem:

> In the declared affine-totalistic Boolean pointer class, global label
> covariance, genuine neighbor sensitivity, and uniform-state persistence
> uniquely select `L_A`.

It also exposes the exact physical price. The current foundation does not
derive that finite class as exhaustive, and the persistence sentence is not
already present. It is tempting bare-metal language—“nothing locally
distinguishes a uniform state from itself, so it stays itself”—but that is a
dynamical persistence law, not a logical consequence of cubic covariance.
`L_B` is just as homogeneous and covariant while uniformly flipping.

The positive route can mature in either of two ways:

1. derive the affine-totalistic class and uniform persistence from a deeper
   exact law or foundation theorem, yielding a zero-edit selection; or
2. use the singleton theorem as a falsifiable field of a proposed exact law,
   without pretending self-description supplied it.

The route does not yet license axiom language.

## 6. Consequence for the Constitutional Question

Cycle 45's self-description idea remains valuable. It can turn law identity
from an externally named formula into a record-accessible empirical fact for
observers inside the universe. It can provide an exact checksum, detect a
changed rule, and make the operative law reconstructible without privileged
external notation.

What it cannot do alone is make the image of the self-description map a
singleton. The constitutional alternatives remain exactly those already
allowed by the canonical law contract:

1. derive foundation-wide confluence/uniqueness and add zero words;
2. identify one complete predictive law or one exact record-faithful class in
   the foundation; or
3. prove every apparently different self-describing law is physically
   equivalent under every legal record protocol.

The finite counterexample does not force option 2. It tells us what a claimed
option-1 proof must defeat. Merely adding “the law describes itself” would not
do so, because both witness laws satisfy that sentence.

## 7. Fresh No-Go Discipline Audit

### N1 — Alternative-route enumeration

Every route below was actively tested rather than listed as a rhetorical
possibility.

| Route | Status | Exact test | Outcome |
|---|---|---|---|
| Self-description alone | ATTEMPTED | apply the same complete writer/decoder to `L_A` and `L_B` | fails as selector; two exact fixed points |
| Lattice symmetry and covariance | ATTEMPTED | enumerate 10 neighbor/20 central-bit proper-cubic contexts, all 24 rotations, translations, and all 128 labeled contexts | both totalistic laws survive |
| Record-faithful quotient | ATTEMPTED | same physical context blocks and same total scalar readout `i(A)=Re Tr(P1 A)` | all 14 outcomes differ, so the quotient does not identify them |
| Description-length selection | ATTEMPTED | common three-bit affine encoding `(a,b,d)` | both descriptions have equal length; no selector in this encoding |
| Canonical decoder fixed point | ATTEMPTED | one record schema and one decoder, with no `law_id` field | the same decoder has two fixed points |
| Empirical corpus selection | ATTEMPTED | decode `C_A` and `C_B` separately | succeeds conditionally for the actual corpus, not as foundation selection |
| Affine uniform-persistence filter | ATTEMPTED | exhaustive `8 -> 4 -> 2 -> 1` finite search | positive: uniquely selects `L_A` in the declared class |
| Coverage plus foundation-wide confluence | ATTEMPTED | require the certified complete image to cover the permitted complete-law class and then be singleton | positive sufficient reconstruction route; not proved by the current foundation |
| Direct foundation uniqueness | ATTEMPTED | compare present Admissibility wording with both model expansions | remains open; present wording permits the finite pair |

The description-length result is deliberately narrow. Equal length in one
symmetric exact code does not prove equal Kolmogorov complexity under every
universal machine. It only blocks an unannounced “pick the shorter of these
two formulas” move in the tested encoding.

### N2 — Wall-independence audit

The initial list was reduced to four nonduplicative walls:

| Wall | Exact missing statement |
|---|---|
| `W_C` | the foundation derives the admissible candidate category and proves it exhaustive |
| `W_P` | the foundation derives a legal complete self-description protocol, faithful record decoder, and response certification |
| `W_I` | decoded results are invariant across every foundation-permitted candidate, boundary, protocol, and faithful decoder |
| `W_E` | each decoded local representation has one complete counterfactual extension or one exact record-faithful class |

Pairwise independence was checked explicitly:

| Pair | Separator |
|---|---|
| `W_C`, `W_P` | an exact class can be stated without any physical table-writer; a writer can reconstruct rows without proving its class exhaustive |
| `W_C`, `W_I` | the eight-law class is exact while its self-description image is non-singleton; an abstract singleton claim does not define the candidate category |
| `W_C`, `W_E` | a finite table class can be exhaustive at its own resolution while leaving multiple global/off-sector extensions; an extension map does not prove the starting class exhaustive |
| `W_P`, `W_I` | the common writer/decoder reconstructs both `L_A` and `L_B`, so protocol completeness does not imply cross-law invariance; invariance alone does not build a physical decoder |
| `W_P`, `W_E` | a complete local table can be decoded without a full Qubit/QCA extension; a unique-extension theorem does not make a corpus or certify its records |
| `W_I`, `W_E` | every decoded finite table could agree while two off-domain global extensions differ; unique extension within each candidate does not make different candidates converge |

No wall is only a renamed version of another. The collapsed wall set is
`{W_C,W_P,W_I,W_E}`.

### N3 — Hidden-wall scan

| Trigger phrase | Explicit classification |
|---|---|
| “foundation-compatible” | consistency of a downstream model expansion with the current reduct; not foundation derivation or physical actuality |
| “self-describing” | the checked equation `D(C_L)=L` on the declared table domain |
| “complete” | all 14 supplied totalistic count rows; never all 20 proper-cubic contexts or the full TOE |
| “same apparatus” | the same 14 far-separated center-plus-six-neighbor `P0/P1` blocks, open storage blocks, scheduler, typed spatial/causal roles, and decoder used for both laws |
| “totalism” | explicit downstream condition identifying neighbor patterns with equal Hamming count; stronger than proper-cubic covariance and not foundation-derived |
| “common reduct” | the displayed shared `M_2(C)` role domain, total occupancy-parity `Avail` predicate on every open/arbitrary-content neighbor tuple, total readout `i(A)=Re Tr(P1 A)`, and fresh append-only storage; `L_A/L_B` are added only afterward |
| “neighbor condition” | an explicit six-tuple whose entries are open or carry arbitrary `M_2(C)` content; only presence parity enters `Avail` |
| “event and parent identifiers” | fixed spatial/causal role metadata derived from block identity and scheduled predecessor; not extra onsite content and not a hidden law label |
| “fresh storage” | each target is checked absent; its target-plus-neighbor shell is disjoint from all context records and prior storage blocks; admissibility uses its actual six-open-neighbor tuple |
| “canonical” | used only in the title of the cited contract; no canonical physical law or decoder is selected here |
| “uniform-state persistence” | an explicit extra selection condition in the positive route, not current axiom content |
| “record-faithful” | preserves prepared context identity and scalar record content under every declared protocol |
| “Boolean pointer” | supplied conditional operational sector; not derived from bare `M_2(C)` alone |
| “affine-totalistic” | exhaustively enumerated eight-law theorem domain; not a claim about every local rule |

The proof uses no load-bearing “obvious,” “natural,” “standard,” “by
construction,” “the framework provides,” or “bare metal requires” shortcut.
**Unresolved hidden conditions: 0.**

### N4 — Source-residual matching

| Source | Residual there | Cycle-49 use | Match? |
|---|---|---|---|
| `REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md`, §1 “Pointwise State Versus Complete History,” lines 99–118, and §5, lines 205–235 | an actual history needs separating coverage and exact class/decoder to identify a law | distinguishes actual-corpus identification from foundation selection | yes; direct predecessor |
| `COMPLETE_HISTORY_RECONSTRUCTION_CYCLE45_NOTE_2026-07-14.md`, “Result Up Front,” lines 95–113, and N7, lines 518–535 | a self-testing corpus reconstructs a supplied law class, but zero edit needs derived architecture or foundation-wide invariance | constructs the missing cross-law fixed-point test | yes; exact target residual |
| `CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md`, “Why An Exact Predictive Specification Is Unavoidable,” lines 13–26 | exact law identity, unique derivation, or proved physical-equivalence class | supplies the constitutional completion alternatives | yes; same identity residue |
| `DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md`, “Theorem 3: Unique Continuation Still Contains the Choice,” lines 175–195 | a selected deterministic law can generate one history but determinism does not select the law | separates `L -> C` from selection of `L` | **positive comparator, not negative evidence** |
| `FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md`, “Result in plain language,” lines 61–69 | law equivalence must preserve record labels, order, scalar readout, composition, and locality | defines why opposite same-context scalar records are not silently gauge | yes at the declared record protocol |
| `FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md`, “Result Up Front,” lines 19–48 | one exact law referent remains unless uniqueness reduces the update to zero | tests one proposed uniqueness mechanism | yes; no new second atom introduced |

No positive unique-extension result is counted as evidence that selection is
impossible.

### N5 — Resolution and rhetoric audit

| Resolution | Tested? | Licensed statement |
|---|---:|---|
| one totalistic count row | yes | the pair gives opposite same-context record responses |
| complete 14-row totalistic table | yes | both laws exactly self-describe under the common writer/decoder |
| all 20 genuine proper-cubic contexts | enumerated but not independently parameterized | totalism identifies some distinct proper-cubic contexts, so no 20-row selection theorem is claimed |
| eight-law affine-totalistic class | yes, exhaustive | added symmetry, variation, and uniform persistence select one member |
| all proper-cubic Boolean local rules | **NOT TESTED / OPEN** | no uniqueness or nonuniqueness theorem is claimed |
| full Qubit/QCA law space | **NOT TESTED / OPEN** | finite pointer tables do not classify coherent or composed laws |
| complete TOE law | **NOT TESTED / OPEN** | no claim about all operational, clock, matter, gravity, continuum, or boundary fields |

The licensed negative is only:

> In the tested finite class, exact self-description plus the checked
> symmetries has at least two record-distinguishable fixed points.

This is not a universal no-go for self-selection, fixed-point uniqueness,
algorithmic-law selection, or zero-edit foundation closure.

### N6 — Partial-closure paths

| Path | Current result | What remains |
|---|---|---|
| Self-testing corpus | exact positive identification | identifies the operative table from actual records, conditional on class and decoder |
| Affine-totalistic singleton theorem | exact positive finite selection | derive or justify class exhaustiveness and uniform persistence physically |
| Coverage plus foundation-wide confluence | sufficient and exact within the complete reconstruction schema | prove `S_F=C_F`, complete extension, and `|S_F|=1`; no actual corpus is required in every history |
| Direct foundation uniqueness | open zero-edit route | derive the complete law without using the actual corpus as hidden selector |
| Record-protocol equivalence | open zero-edit quotient route | prove all surviving self-describing representatives agree under every physical record protocol |
| Richer-law embedding | open constructive route | show `L_A` and `L_B` are gauge projections of one uniquely derived complete law |

The failure of self-description *alone* does not force a new axiom. The
positive theorem can be strengthened, a physical quotient can collapse the
pair, or a complete law can be uniquely derived by another mechanism.

### N7 — Strongest hostile steelman

**Hostile steelman:** the existing foundation might uniquely derive a
universal interpreter, a legal dovetail scheduler, a record decoder, and a
canonical self-description corpus. A recursion/fixed-point theorem might then
show that every permitted complete program writes the same record-protocol
law class, even if many source strings or finite table projections differ.
Alternatively, a full-abstraction theorem might prove that all fixed points
are gauge presentations of one physical process. Under either result,
`S_F=C_F` and `|S_F|=1`, or directly `|C_F|=1`; the exact law is a theorem and
the constitutional edit is zero.

The finite `L_A/L_B` pair does not refute that program because it does not
classify all complete physical programs or their full equivalence category.
It does make the steelman pay its exact price: the interpreter, protocol,
decoder, exhaustive domain, complete extension, and singleton/full-abstraction
theorem must all be foundation-derived rather than selected by the corpus.

**Strongest outcome:** the broad negative is not licensed. The bounded
two-fixed-point result survives: self-description is not *itself* a uniqueness
principle, and the current four axioms do not yet contain the additional
coverage-plus-confluence theorem.

### N8 — Cross-cycle echo

The required docs phrase scan was run with

```text
rg -l -i "structurally undecidable|no retained primitive|requires new axiom|cannot be derived from a_min" docs
```

and returned 31 files. The repository walk inspected 67
`NO_GO_LEDGER.md` files, followed by searches for `self-description`, `law
identity`, `canonical law`, and foundation uniqueness. There was no prior
ledger entry with the exact self-description/foundation-selection residual.

| Prior source | Earlier disposition | Mechanism carried forward | Cycle-49 update |
|---|---|---|---|
| Cycle 42 | separating complete-history route left live | actual data can identify only with complete protocols/class | actual-corpus success is retained but retyped away from foundation selection |
| Cycle 45 | broad history nonidentifiability defeated | universal table corpus and self-describing dovetail | exact two-fixed-point test shows reconstruction is not singleton selection |
| Canonical law contract | exact identity/equivalence/uniqueness trichotomy | one complete law residue | coverage plus confluence is the self-description proof schema; direct uniqueness remains separate |
| Deterministic unique extension probe | uniqueness of history does not select map/boundary | direction-of-inference control | no direction reversal is used as negative evidence |
| Foundation equivalence probe | record labels/order/readout survive safe law equivalence | record-faithful quotient | opposite scalar responses remain distinct at the tested protocol resolution |

No cross-cycle echo licenses a universal impossibility statement. The new
mechanism is the explicit multiplicity of exact self-description fixed points,
paired with an executable positive singleton filter.

**Gate result: PASS for the bounded two-fixed-point counterexample and the
finite positive singleton theorem; PASS for no broader no-go.**

## Bottom Line

The self-description idea survives, but with its job stated correctly.

```text
self-description = exact internal identification of the operative law;
foundation selection = proof that the certified image covers every permitted
                       complete class and contains exactly one class.
```

The first is constructively achieved twice. In the supplied two-law class the
certified image has coverage but is not confluent. A singleton observed image
without coverage would not suffice. Uniform-state persistence closes the pair
inside one declared eight-law class, where the certified image both covers the
restricted candidate class and is singleton. That remains a concrete positive
path, not a consequence of the current foundation.

Therefore Cycle 45 self-description does not presently delete the law-identity
atom. It gives a strong way for the law to be readable from within the world.
To make it eliminate constitutional law identity, the next proof must show
that the foundation permits only one complete readable answer, not merely
that whichever answer occurs can read itself back accurately.

## Verification

```bash
python3 scripts/self_describing_law_foundation_selection_cycle49_2026_07_14.py
```

The runner independently enumerates 10 neighbor/20 central-bit proper-cubic
contexts, checks the separate 14-row supplied-totalism domain, all 24 proper
cubic rotations, all 128 labeled Boolean neighborhoods, the total common
`M_2(C)` / occupancy-parity `Avail` / `i(A)=Re Tr(P1 A)` Record reduct, every
open/present-neighbor mask with arbitrary `M_2(C)` content, all 14 explicit
far-separated cubic context blocks, actual open storage targets and neighbor
tuples, typed spatial/causal role metadata, both self-description fixed points,
coverage versus singleton-image failure, the exact `8 -> 4 -> 2 -> 1` positive
filter, and the complete fresh N1–N8 structure.
