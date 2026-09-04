# First-Principles Microscopic-Law Selection Tournament

**Date:** 2026-07-14

**Type:** meta

**Scope:** bounded exact tests of symmetry, reversibility, confluence, entropy,
description length, nontriviality, efficiency, and self-consistency as
selectors of the exact record-production law

**Authority:** none. This is an exploratory selection tournament, not a
physical-law choice, axiom proposal, primitive, audit verdict, or retained
theorem. It changes no axiom, registry, primitive, or audit surface.

## Framework and Prior Result Read

This cycle used the exercise refresher already completed in the preceding
cycles: the four current axioms, all approved primitive source notes, premise
and derivation-obligation registries, current exercise/review/no-go skills, and
the controlled vocabulary. It then read the deterministic uniqueness result in
[`DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md`](DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md)
and the canonical-law field inventory in
[`CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md`](CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md).

The target is sharper than “find an elegant rule.” The question is whether an
exact, representation-invariant principle makes the physical law a theorem of
the existing framework, so that a constitutional reference to an otherwise
supplied law becomes unnecessary.

## Result in Plain Language

The tournament found genuinely unique winners. That is the important positive
result. Unfortunately, the winners expose the selection problem instead of
closing it.

- Maximum fixed points, maximum full-input entropy, full conjugation symmetry,
  and reversible permanence all select the identity/no-formation rule in the
  bounded classes. It is unique because it does nothing.
- If identity is excluded, symmetry, reversibility, confluence, and minimum
  dependency uniquely select the binary complement rule. It is nontrivial and
  exact, but it flips every record and therefore fails Record.
- In a nine-rule class built specifically for permanent records, symmetry,
  causal confluence, and minimum nonzero write support leave two rules. One
  copies two equal recorded neighbors into the open site; the other writes
  their opposite. Adding “minimize disagreement with the triggering records”
  uniquely selects the copy rule. That is a valid finite uniqueness proof and
  a useful formation kernel, but the disagreement cost is the extra physical
  principle. The rule also needs a seed boundary and closes only four of ten
  tested canonical-law fields.

The generic slogans do not survive representation attacks:

- maximum entropy changes when the input ensemble or branch refinement
  changes;
- minimum description/gate count changes with the code, gate library, and
  whether equivalent decompositions are minimized over;
- Hamiltonian norms change under clock rescaling and an identity energy shift
  even when the exact unitary is unchanged;
- storage/compute efficiency changes when the relative price of storage and
  operations changes; and
- maximum nontrivial symmetry gives an orbit of equivalent qubit axes, not one
  physical element.

The conclusion is not that exact law selection is impossible. It is this:

> A selection principle derives a law only after it fixes the candidate class,
> the physical-equivalence quotient, the score/ordering, and the target notion
> of nontrivial success. In the tested classes, those items contain the same
> kind of physical information the principle was meant to eliminate.

An exact future principle could still close all four items and prove a unique
complete law. No such principle is identified here.

## The Bounded Model Classes

### Permanent-record class

Local values are `{open,0,1}`. A radius-one rule is homogeneous, reflection
symmetric, covariant under global exchange `0 <-> 1`, and leaves every existing
record unchanged. When the center is open, reflection and label covariance
reduce the nine unordered neighbor contexts to two free values:

```text
a = output for neighbors {open,0};
b = output for neighbors {0,0}.
```

The corresponding `1` contexts follow by label exchange. Contexts
`{open,open}` and `{0,1}` must output `open`, because each is fixed by the
label exchange while neither record label is fixed. Thus `(a,b)` has only
`3*3=9` possibilities.

This is a small but physically targeted class: homogeneity, label covariance,
reflection symmetry, and site-tagged permanence are exact by construction.
It does not claim to exhaust three-dimensional qubit laws.

### Binary radius-one class

The runner also exhausts all 256 binary elementary cellular automata. Sixteen
are covariant under global label exchange, eight of those are reflection
symmetric, and six pass bijectivity on every tested ring of size three through
seven.

This class is useful for representation and simplicity tests, but it has no
open/record distinction. A unique rule in it is not automatically a formation
law.

### Reversible one-qubit family

The 24 proper-cubic rotations are used as the Bloch-sphere action of the
one-qubit Clifford channels, modulo global phase. Every element is orthogonal,
determinant one, invertible, and spectrum-preserving. The family is exact and
closed under inverses.

This is a bounded reversible family, not the space of all qubit unitaries or
all quasilocal QCA laws.

## Selector 1: Maximum Symmetry

Every member of the permanent-record class already has the imposed spatial
and label symmetries, so maximum symmetry leaves nine candidates.

In the binary class, label covariance plus reflection leaves eight.
Reversibility and confluence reduce that to identity and complement, but
symmetry does not distinguish them.

In the proper-cubic qubit family, the identity commutes with all 24 channels
and is the unique maximum-symmetry element. After identity is excluded, the
largest centralizer is shared by three conjugate half-turn axes. Selecting one
axis is not invariant under a change of one-qubit frame.

Maximum symmetry therefore has two exact outcomes:

1. allow the trivial element and obtain identity uniquely; or
2. demand nontriviality and obtain a symmetry orbit, not one representative.

A relational boundary can select a representative covariantly. Then the
representative is boundary-relative rather than derived from bare symmetry.

## Selector 2: Reversibility/Extremality

All 24 qubit channels are reversible unitary channels and are extreme in the
convex set of channels. Reversibility/extremality does not select among them.

For a finite record-only state space ordered by permanent record inclusion,
strict formation and reversibility conflict. A bijection on a finite set is a
union of cycles. A strict append moves upward in the record order and cannot
return without deleting a record, so it cannot lie on a nontrivial cycle.
Therefore a reversible site-tagged permanent map on that finite state space
has no strict append event.

The nine-rule runner finds exactly that: only the no-formation rule is
injective on the tested finite ring. Every forming rule is noninjective.

This does not rule out reversible underlying qubit dynamics. It says the
append-only public archive is an irreversible quotient or an enlarged system
with fresh capacity. The exact quotient/capacity law is then additional
content.

## Selector 3: Causal Invariance/Confluence

The runner applies local site updates in both orders for every state and every
site pair on a five-site ring. Three permanent-record rules commute under this
finite asynchronous test:

1. no formation;
2. an open site between equal records writes the same record; and
3. an open site between equal records writes the opposite record.

The two forming rules have the same symmetry, write support, local dependency,
and confluence. Causal invariance determines that update order is bookkeeping.
It does not determine record content.

In the binary class, the same test leaves identity and complement. Again it
removes schedule ambiguity without choosing stasis versus change.

## Selector 4: Maximum Entropy

Maximum entropy needs a measure over the inputs or branches being counted.
That measure changes the result even in the nine-rule class.

- Under the uniform distribution on all 27 local triples, the no-formation
  rule alone has output counts `(9,9,9)` and maximal three-symbol entropy.
- Conditional on the center being open, four forming rules have output counts
  `(3,3,3)` and tie for maximum entropy. The no-formation rule has zero output
  entropy on that conditional corpus.
- Every label-covariant binary truth table has four zeros and four ones, so all
  sixteen rules tie under uniform truth-table entropy.
- Every reversible qubit channel preserves the von Neumann entropy of every
  input state, so all 24 tie.

Branch refinement is decisive. A physical distribution `(1/2,1/2)` has one
bit of Shannon entropy. Splitting the second physical outcome into two
presentation branches gives `(1/2,1/4,1/4)` and `3/2` bits without changing the
coarse physical alternatives. Entropy is representation invariant only after
the physical event quotient and input measure are fixed.

## Selector 5: Minimum Description/Gate Count

Description length is relative to a code. The runner gives identity and
complement prefix descriptions `0` and `10`; swapping those codewords reverses
the winner while keeping a valid prefix code.

Raw gate count is not invariant under equivalent gate decompositions:

```text
X = H Z H,
I = X X.
```

Counting the displayed presentation gives one versus three gates for `X` and
zero versus two for `I`. Minimizing over exact decompositions removes that
particular artifact, but only after a gate library, primitive-gate costs,
ancilla rules, approximation tolerance, and clock convention are supplied.

The exact Hamiltonian control is sharper. Let

```text
H  = diag(0,1),       t = pi;
H' = 2H,              t' = pi/2;
H''= H+2I,            t''=pi.
```

All three generate the same exact unitary `diag(1,-1)`. Their squared
Frobenius norms are `1,4,13`. A Hamiltonian-norm selector therefore changes
under clock rescaling and an identity energy shift unless it first quotients
those physical redundancies and fixes a normalization.

## Selector 6: Minimum Nontrivial Rule

“Nontrivial” is already a target choice.

In the label-covariant binary class, the one-input rules are left shift, right
shift, their complements, center identity, and center complement. After
reflection, reversibility, confluence, and minimum dependency are imposed,
identity and complement remain. Excluding identity makes complement rule 51 a
genuinely unique winner.

That is an exact finite theorem. Rule 51 flips the center at every step. It is
homogeneous, label-covariant, reflection symmetric, reversible, confluent, and
one-input minimal. It also changes every recorded bit, so it cannot be the
public permanent-record law.

In the permanent-record class, the minimum positive write support is two local
contexts. Copy-equal and oppose-equal tie. “Nontrivial” does not decide which
fact is written.

## Selector 7: Maximum Storage/Compute Efficiency

If efficiency means “fewest permanent writes,” no formation wins. If it means
“most writes per local evaluation,” four rules tie at six of nine open-center
contexts. If it means “fewest input dependencies,” identity, complement, and
four shifts/complemented shifts tie in the binary class.

A two-resource example exposes the hidden price vector. Algorithm `A` uses one
storage unit and four compute units; `B` uses three storage units and one
compute unit. Equal unit prices favor `B`. Pricing storage three times as much
favors `A`. Neither dominates. A compute-limited or storage-limited universe
does not define an optimum until its budget, exchange rate, latency, error,
and physical utility are stated.

This is the direct answer to the simulation-resource intuition. Resource
limits can be fundamental physics, but “do not overspend” is not yet an exact
law selector.

## Selector 8: Fixed-Point/Self-Consistency

Maximum fixed-point count uniquely selects the no-formation rule on the tested
five-site permanent ring and identity rule 204 on the tested five-site
label-covariant binary ring. In the qubit family, identity uniquely fixes the
whole three-dimensional Bloch space; every nonidentity proper rotation fixes
only its axis.

Self-consistency therefore produces an exact unique winner across all three
bounded classes: identity. The selection theorem is real. The winner supplies
no formation, propagation, Bell process, clock, or matter.

A different self-consistency principle—one unique global solution rather than
maximum fixed points—remains live. It must state its global equation and
boundary class exactly.

## Selector 9: Intersection of All Constraints

There are three honest intersections.

### Literal intersection

Maximize symmetry, reversibility, entropy preservation, efficiency by minimum
work, and fixed points. Identity/no formation wins uniquely. The intersection
closes selection by deleting the target phenomenon.

### Require nontrivial reversible dynamics

In the binary class, complement rule 51 wins uniquely after identity is
excluded. The winner violates permanent records and has no open/formation
semantics.

### Require permanent formation

Reversibility must be moved to an enlarged substrate or dropped at the public
record level. Symmetry, permanence, finite causal confluence, and minimum
positive write support leave copy-equal and oppose-equal. Add the exact cost

```text
minimize disagreement with the equal triggering records.
```

Copy-equal is then the genuinely unique winner. Its disagreement score is
zero; oppose-equal's is four over the two triggered contexts and two neighbors.
This principle is invariant under spatial reflection and global exchange of
record labels. It is the tournament's strongest finite steelman.

The uniqueness proof does not make the cost free. It says precisely which new
physical atom breaks the last tie: equal neighbor records favor copying rather
than opposition.

## Representation-Invariance Audit

| Transformation | What changes without a quotient | Surviving requirement |
|---|---|---|
| global record-label recoding | a selector that names `0` or `1` changes | use equality/complement relations; all nine record rules pass |
| one-qubit basis conjugation | a selected `X`, `Y`, or `Z` axis moves | select an orbit or use a physical relational frame |
| branch refinement | entropy and path-count weights change | fix the physical event quotient before counting |
| equivalent gate decomposition | displayed gate count changes | minimize over an exact equivalence class and fixed library |
| clock rescaling | Hamiltonian magnitude and operations-per-tick change | fix physical time normalization or use invariant action data |
| identity energy shift | Hamiltonian norm/energy changes at fixed channel | quotient global phase/zero of energy |
| algorithm recoding | description length changes by code choice | specify a universal description language and accept its constant/cost |
| storage/compute repricing | efficiency ordering changes | supply the physical resource metric and utility |

Representation invariance does not forbid optimization. It defines the
quotient on which an optimization would have physical meaning.

## Genuinely Unique Winner: Canonical-Law Fields Test

The copy-equal permanent rule closes four tested fields:

1. a homogeneous bounded domain;
2. global label covariance;
3. site-tagged record preservation; and
4. finite asynchronous confluence on the tested ring.

It does not close:

1. autonomous origin/first boundary;
2. a full physical outcome repertoire;
3. Bell-capable calibrated frequencies;
4. the actual cosmological boundary;
5. a physical qubit/readout decoder; or
6. a clock/rate map.

The rule leaves all-open unchanged and forms only when two equal boundary
records already flank an open site. It is a useful exact kernel, not a
canonical law of the universe.

The identity and complement winners do even less. Identity respects permanence
but never forms a record. Complement is dynamically nontrivial but violates
permanence. None retires the exact-law reference.

## Hidden Input by Selector

| Selector | Exact hidden input exposed by the tournament |
|---|---|
| maximum symmetry | which symmetry group; whether trivial identity is allowed; orbit versus representative |
| reversibility/extremality | public archive versus enlarged substrate; candidate channel class |
| causal invariance/confluence | local rewrite repertoire and physical content of terminal sectors |
| maximum entropy | input measure, event quotient, constraints, and coarse graining |
| minimum description/gate count | code/language, gate library, costs, ancillas, tolerance, equivalence relation |
| minimum nontrivial rule | definition of triviality and required phenomena |
| maximum storage/compute efficiency | resource metric, exchange rates, budgets, latency, error, utility |
| fixed-point/self-consistency | fixed equation, boundary class, and whether stasis is an acceptable solution |
| intersection of all constraints | priority/compatibility of constraints and the tie-breaking physical cost |

These are not all necessarily axioms. Some can be derived, measured, or placed
in the exact law's domain. They cannot be deleted by renaming the selector.

## Consequence for Bare-Metal Axiom Language

No tested slogan is ready to replace the exact-law reference in the
constitution. “Most symmetric,” “simplest,” “maximum entropy,” “most
efficient,” and “self-consistent” each need a mathematical object, quotient,
and score before they have one answer.

The finite uniqueness results do suggest the correct research shape:

1. define a representation-invariant class of complete candidate laws;
2. define the physical equivalence quotient;
3. state one exact selector on that quotient;
4. prove a unique nontrivial minimizer; and
5. verify that the minimizer fills every canonical-law field.

If all five succeed from existing framework structure, the physical referent
is derived and no new axiom sentence is needed. If step 3 must be supplied as a
new universal physical principle, that principle—not its winning rule table—is
the candidate constitutional content. The present tournament gets a unique
bounded formation kernel only by adding minimum triggered disagreement. It
does not justify elevating that cost to the axiom set.

## No-Go Discipline Gate

The licensed negative claim is bounded:

> In the tested nine-rule permanent class, all 256 binary radius-one rules, and
> the 24 proper-cubic one-qubit reversible channels, none of the generic
> selectors alone produces one representation-invariant, nontrivial,
> permanent-record, canonical-law-complete winner.

The exact identity, complement, and copy-equal uniqueness results are positive
exceptions inside narrower target definitions. No claim is made against a
future exact selector on a richer law quotient.

### N1 — Alternative-Route Enumeration

| Route | Status | Result |
|---|---|---|
| maximum symmetry | attempted | identity unique if trivial allowed; nontrivial orbit otherwise |
| reversibility/extremality | attempted | all qubit channels tie; finite permanent formation disappears |
| causal invariance/confluence | attempted | removes schedule order but copy/opposition content tie remains |
| maximum entropy | attempted under two exact ensembles | winner changes with ensemble; branch refinement changes score |
| minimum description/gate count | attempted | code/library/decomposition dependence exposed |
| minimum nontrivial rule | positive bounded theorem | complement unique in binary intersection; fails Record |
| maximum storage/compute efficiency | attempted | no-formation or multi-rule tie; resource prices reverse rankings |
| fixed-point/self-consistency | positive bounded theorem | identity unique; no physics generated |
| literal intersection of all constraints | attempted | identity/no formation unique |
| permanent-formation intersection | positive bounded theorem | copy-equal unique after explicit disagreement cost |
| exact invariant action/global consistency | live | could select a complete law on a richer quotient |

At least five independent routes were tested. Several succeed narrowly, which
prevents a universal law-selection no-go.

### N2 — Wall-Independence Audit

Four inputs remain before an optimization can derive a physical law:

- `C`: complete candidate class;
- `Q`: physical-equivalence quotient;
- `S`: exact selector/score and its measure/cost normalization; and
- `T`: nontrivial target/canonical-law field requirements.

| Pair | Closing first closes second? | Reverse? | Independent? |
|---|---:|---:|---:|
| `C,Q` | no | no | yes |
| `C,S` | no | no | yes |
| `C,T` | no | no | yes |
| `Q,S` | no | no | yes |
| `Q,T` | no | no | yes |
| `S,T` | no | no | yes |

Examples make the independence exact. The same class has different entropy and
fixed-point winners; the same selector has different winners under different
input measures; one identity winner fails the nontrivial target; and a complete
target list does not define a simplicity code. A future principle may derive
or bundle several items, at which point the wall count must collapse.

### N3 — Hidden-Wall Scan

The scan promoted these conditions explicitly: finite ring sizes used for
reversibility/confluence; site-tagged permanence; uniform all-triple versus
open-center ensembles; event coarse graining; prefix code; primitive gate
library; Hamiltonian time normalization and energy zero; resource price vector;
identity exclusion; disagreement metric; supplied boundary seed; and the ten
canonical-law test fields.

“By construction” refers only to the displayed bounded classes. “Maximum,”
“minimum,” “simple,” “efficient,” and “self-consistent” are never used without
naming their score and domain.

### N4 — Exact Residual Matching

| Prior surface | Residual there | Use here | Match? |
|---|---|---|---:|
| deterministic unique-extension note | exact map/component/decoder remain after determinism | asks whether a selector derives those objects | yes |
| causal-reversible atom inventory | canonical law requires domain, update, outcomes, weights, preservation, decoder, boundary, clock | fields test for each winner | yes |
| autonomous binary nucleation note | compute/storage and relational-reference costs remain | motivates resource and recoding attacks | yes, not proof |
| complete sampled-law pair | architecture permits distinct law values | copy/opposition and identity/complement paired controls | yes as residual shape |
| homogeneous boundary-seed note | all-open symmetry does not select a finite origin | copy-equal boundary failure only | yes, limited |

No finite CA tie is cited as a theorem about all qubit QCA laws.

### N5 — Resolution and Rhetoric Audit

- The exhaustive claims cover exactly nine record rules and 256 binary
  radius-one rules; the qubit claims cover 24 proper-cubic channels.
- Finite-ring reversibility/confluence is labelled by its tested sizes; no
  thermodynamic classification is claimed.
- “Unique winner” always names identity, complement, or copy-equal and the
  conditions making it unique.
- “Representation dependence” names the exact recoding/refinement/rescaling;
  it is not a claim that invariant complexity measures cannot exist.
- “No selector closes” means the listed generic selectors in the tested
  classes, not every possible variational or global principle.

### N6 — Partial-Closure Path

The positive research path is explicit:

- enlarge from local truth tables to complete algebra-valued causal laws;
- quotient exact unitary/gate, clock, energy-zero, branch, and relational-frame
  redundancies before scoring;
- derive a physical resource/action functional rather than import arbitrary
  code length;
- require nontrivial record production, Bell causal placement, decoder,
  boundary type, and clock interface in the candidate class; and
- prove existence and uniqueness of the minimizer.

A successful theorem would retire the exact-law reference without a new axiom.
An explicitly approved universal variational principle could instead become
constitutional content. The current framework primitives supply none of the
needed score, measure, budget, or selector.

### N7 — Strongest Steelman

A hostile reviewer can define the candidate objects as complete covariant
quasilocal laws modulo operational future-record equivalence, unitary/gate
decomposition, clock rescaling, energy-zero shifts, branch refinement, and
relational frame changes. Suppose one dimensionless action/resource functional
is derived from the local algebra and lattice, is coercive on this quotient,
and has a unique nontrivial minimizer. Suppose the minimizer also generates its
own low-record boundary, uniquely extends it, is uniquely ergodic on the
record-defined trial corpus, and carries a declared Bell-global consistency
rule. That would derive the exact referent and defeat the bounded conclusion.
The finite tournament neither builds nor excludes this principle. It shows the
proof obligations that slogans usually leave implicit.

### N8 — Cross-Cycle Echo

Earlier cycles repeatedly found that covariance and architecture leave exact
law values open. This cycle does not count those pairs again as independent
evidence. It attacks the strongest retirement proposal: derive the law by an
optimization/uniqueness principle.

The new information is two-sided. Exact unique selectors do exist in bounded
classes, so “selection can never work” is false. But their winners are trivial,
Record-violating, or incomplete until a physical cost is added. This preserves
the future uniqueness route while preventing an aesthetic slogan from being
mistaken for its theorem.

**No-go-discipline status:** PASS for the bounded three-class statement. A
universal first-principles-selection no-go would fail N7 and is not made.

## Verification

Run:

```bash
python3 scripts/first_principles_law_selection_tournament_probe_2026_07_14.py
```

The PASS count is a contract and exact-control count, not a count of
independent scientific facts.
