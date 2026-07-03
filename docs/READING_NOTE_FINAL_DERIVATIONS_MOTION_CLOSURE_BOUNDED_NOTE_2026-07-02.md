# Final Reading-Note Derivations: Answer, Condition, Motion Closure, And Extensional Judgment

**Date:** 2026-07-02
**Type:** bounded theorem (definitional derivations; reading-note retirement support)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note writes no audit
verdict, sets no audit status, and forecasts no audit outcome.
**Primary runner:** [`scripts/frontier_answer_condition_motion_closure_2026_07_02.py`](../scripts/frontier_answer_condition_motion_closure_2026_07_02.py)
**Runner output:** [`outputs/frontier_answer_condition_motion_closure_2026_07_02.txt`](../outputs/frontier_answer_condition_motion_closure_2026_07_02.txt)

## Purpose

The owner rule of 2026-07-02 - no rulings, only clarity - requires semantic
content to carry premise weight only as axiom text or derivation that passes
audit. Four remaining reading-note shards are theorem, bounded theorem, or
procedure-classification content of the current axiom text. This note derives
them so the historical reading-note surface can retire as load-bearing
content. Nothing here adds axiom content.

## Supplied Surface

All semantic derivations use only `docs/MINIMAL_AXIOMS_2026-06-29.md`
sentences:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.
> No site is privileged. Sites are distinguished by the supplied lattice structure alone.
> Each site has a domain of local possibilities.
> The full one-site possibility domain has algebraic presentation `M_2(C)`.
> A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and adds no further primitive structure.
> No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone.
> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.
> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.
> These axioms state only their named primitive content. Further physical
> structure requires derivation, bridge, explicit admission, or approved
> primitive registration before use as a premise.
> A state is a configuration of records.
> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

The procedural classification in T4 names only the
`docs/ai_methodology/skills/audit-loop/SKILL.md` section "Law-Domain Audit
Procedure" as a process home. It is not an axiom premise. `[checks 1-11]`

## T1 - "answer" typing is a theorem

The law sentence supplies the whole interface: at every in-domain state, the
law "gives exactly one answer." The counted item is whatever single item the
law's giving relation supplies at that state; the axioms supply no finer or
coarser individuation, and Qualification bars any unnamed one as a premise.
The sentence does not require that item to be scalar, atomic,
singleton-valued, or internally structureless.

A set-valued or distribution-valued verdict is still one answer when it is one
verdict object. Treating it as many answers would require occurrences,
weights, draws, or another outcome-individuation rule. None is named by the
supplied sentences, and Qualification bars treating unnamed structure as a
premise. Typing of the answer space can still arrive by the named supply
routes: derivation, bridge, explicit admission, or approved primitive
registration. A registered answer-domain may type verdict objects; absent such
supply, the axiom-visible count is one object per in-domain state.
`[checks 12-13]`

## T2 - "condition" as predicate on states, record absence included

The law sentence evaluates the condition only at states: "at every state where
the condition holds." Together with "A state is a configuration of records,"
this makes a condition a state predicate for axiom-visible law-domain use.

Record absence is part of that configuration data. The "When present"
conditional carries blankness: a state can include record-bearing and
record-free sites. A predicate may distinguish states by record absence so
long as the distinction is statewise, not a hidden non-state parameter.

The readability sentence does not remove that domain surface. "Only records
are readable" and "A readout value is determined by record content alone"
scope readout values. A condition holds at a state; it is not itself a readout
value. No quoted sentence types condition-evaluation as a readout - the
readability sentences mention only records and values - and extending them to
domain evaluation would itself require supply. `[checks 14-16]`

## T3 - Motion closure of lawful domains, from the two distinction clauses

Let `g` be one of the lattice motions named by the Lattice axiom: a standard
translation or a proper cubic rotation from the named family. The Qubit
axiom's definite article supplies one shared one-site domain: "The full
one-site possibility domain has algebraic presentation `M_2(C)`." The
Admissibility sentence's "one fixed nearest-neighbor admissibility rule" is
statable across sites only with that shared domain. Define `g * state` by
transporting each record from site `s` to site `g(s)`, carrying its locked
possibility as the same element of the shared one-site domain. Any rival
transport differs from this one by a site-dependent automorphism intertwiner;
no quoted sentence registers such an action, presentations add "no further
primitive structure," and Qualification bars unregistered structure as a
premise - so the shared-domain transport is the only axiom-expressible motion
action on states.

Statehood of `g * state` is not derived here. A transported lock must still
lie in the available subset at its transported site. That is exactly where the
Admissibility covariance sentence is used as a premise, read with no motion
action on the possibility domain (an intertwined action being unregistered
further structure). `[check 17]`

Toy honesty: the runner's shared possibility alphabet instantiates the quoted
shared-domain sentence, not an extra assumption. At `N = 2` the wraparound
model is degenerate - opposite neighbors coincide and sign action is trivial -
so a second family at `N = 3` (six distinct neighbors per site) exercises a
genuinely proper rotation, a sign-bearing proper rotation, and a translated
rotation on sampled low-record states. `[checks 18-19]`

Prong 1: carried distinctions are equivariant. By T2, a lawful condition is a
predicate on states. By the Lattice and Qubit distinction clauses, the
condition's distinctions among sites and possibilities can be carried only by
record content and the supplied lattice and algebraic structures. The supplied
lattice structure names adjacency, translations, and proper cubic rotations
about each site. It does not supply a bare coordinate name, a chosen origin,
preferred axes, or coordinate order as independent distinguishers.

Translations act transitively on lattice sites, and the rotation family is
named about each site. Thus no site is privileged by the named structure
alone. For any named motion `g`, a state and `g * state` present the same
record-content-relative-to-supplied-structure description. A lawful condition
therefore holds at one iff it holds at the other. The runner checks structural
conditions by full enumeration of the finite motion group: some record, a
record with a record-free neighbor, a unique record with possibility `p`, and
a per-site universally quantified structural rule. `[checks 20-23]`

Prong 2: anchored selections are the contrapositive, judged in extension. By
prong 1, every condition whose distinctions are carried by record content and
supplied structure has a motion-closed extension. Contrapositively, a
condition whose extension is not motion-closed draws, in extension, a
distinction among motion-related, structure-isomorphic states - a site or
possibility distinction carried by neither record content nor supplied
structure, which is what the two distinction clauses bar. The anchor
vocabulary (a bare coordinate, chosen origin, enumerated site or state list)
is the diagnostic, not the offense: a mention that is eliminable - a condition
co-extensional with a lawful one - is acquitted, exactly as T4 requires, while
a genuine anchor is recoverable from the extension itself (for "site `s0`
carries a record," `s0` is the unique site recorded in every selected state).
The runner exhibits the anchored condition's extension failing motion closure
with its anchor recovered from the extension, and checks both a rigid
singleton state list and the invariant empty-configuration singleton.
`[checks 24-25]`

Named escape: any explicitly admitted or registered enlargement - an anchor,
or an equivariance datum such as a registered possibility action - would
enlarge the supplied structure by owner action. The theorem's premise would then update
with that enlarged structure, and closure would be judged relative to the new
surface. The conclusion is surface-relative by construction, not absolute.

Thus the old reading-note statement that a readout-encoded state list
generically fails the law-domain motion test is recovered as theorem content.
Rigid lists fail prong 2. Motion-invariant selections, such as the
empty-configuration singleton, are the honest exceptions; hence
"generically."

## T4 - The extensional-judgment shard: derive-and-classify

Derivation prong. The supplied axiom interface gives a condition one visible
attribute: its extension, the state set at which it holds. The law sentence
uses only "at every state where the condition holds." It supplies no hook for
judging a law domain by wording, nickname, presentation order, or source-file
spelling.

Judging by anything other than the selected state set would judge by an
attribute no axiom sentence supplies; the interface inspection itself carries
the load, with the two distinction clauses reinforcing it on their carriers.
Hence privilege judgment on lawful domains can attach only to selected state
sets - extensionally.

Ceiling: this is an interface/parsimony argument. It is one step softer than
T1-T3's direct derivations because it identifies the only supplied condition
interface rather than quoting a sentence that literally says "judge
extensionally." The bounded theorem claim is limited to that interface
ceiling. The interface is also surface-indexed: extension is the only
axiom-visible semantic attribute of a condition at a fixed supplied surface;
supply pedigree gates premise use under Qualification rather than privilege,
and a registered condition-attribute would enlarge the interface, re-indexing
this ceiling exactly as T3's escape re-indexes closure. `[checks 26-27]`

Classification prong. Whatever residue remains about how an auditor goes
about judging a condition - inspect the selected set, do not judge by wording
alone - is audit procedure. It is the same class as certificate demand and
covariance transport already housed in the audit-loop skill section
"Law-Domain Audit Procedure." No axiom sentence is proposed.

## Consequence

The remaining reading-note shards can be removed as load-bearing semantic
surface: answer typing, condition-as-state-predicate typing, motion closure
from the two distinction clauses, and extensional domain judgment now live here
as bounded theorem or procedure-classification content. The runner's toy checks
are witnesses only; the premises are the quoted axiom sentences.

## Does NOT

- Does not edit axiom text or propose sentences.
- Does not adjudicate any reading; the theorems cite landed clauses.
- Does not cite policy section entries as premises.
- Does not touch `R*/D-totality`, `CTX-match`, `w`, or any campaign surface.
- Does not touch pack files, registries, audit data, or `.claude/`.
- Does not set audit status; the independent audit lane is the only status
  authority.

## Dependencies

- [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`docs/ai_methodology/skills/audit-loop/SKILL.md`](ai_methodology/skills/audit-loop/SKILL.md)
  section "Law-Domain Audit Procedure" only, as procedural classification
  home and not as semantic premise.

## No-Promotion Statement

This note does not promote, demote, or set the audit status of any dependency.
The independent audit lane is the only status authority.
