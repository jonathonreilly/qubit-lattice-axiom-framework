# R* and D-totality Discharge To Landed Axiom Text (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded theorem (interpretive-premise discharge)
**Claim type:** bounded_theorem
**Status authority:** Audit status is set only by the independent audit lane.
This note carries no audit verdict and requests none; nothing here sets,
implies, or predicts the status of any row, block, wall, or pull request.
**Actual current surface status:** a bounded discharge result over landed axiom
text plus finite witnesses. Every sibling it leans on (blocks 03, 05, 16, 17;
PR #4851) is review-pending; their statuses belong to the audit lane alone.
**Primary runner:** `scripts/frontier_rstar_dtotality_axiom_discharge_2026_07_02.py`
**Runner output:** `outputs/frontier_rstar_dtotality_axiom_discharge_2026_07_02.txt`

## Firewall

This note **adjudicates nothing**. It closes no gate and **no wall is closed**
here. Blocks 03, 05, 16, and 17, and PR #4851, are cited only as
**review-pending** siblings; their statuses are the audit lane's, not this
note's. The CTX-match rung is untouched, and no axiom, policy, primitive, or
registry content is added, renamed, or moved. The result is only this: two
named interpretive premises used by review-pending siblings are shown, on
finite witnesses, to be *instances of sentences that already landed in the
axiom memo* — so where those siblings wrote "conditional on the reading," the
condition is landed axiom text plus the siblings' own finite witnesses. Whether
the siblings themselves land is the audit lane's call.

## Purpose

The carrier/kappa ladder has, at several rungs, leaned on a *reading* — an
interpretive premise flagged for audit adjudication rather than asserted as
axiom content. This note takes the two readings named by review-pending
siblings — **R\*** (registrability reading, PR #4818 block03) and **D-totality**
(PR #4820 block05) — and shows each is an instance of an already-landed
sentence in `docs/MINIMAL_AXIOMS_2026-06-29.md`. Discharging a reading to axiom
text proposes that nothing remains to adjudicate: the premise's content is a
sentence the framework already carries. Whether to de-list any adjudication
item is the audit lane's own triage call. This decides nothing about whether
the siblings' downstream results land; it removes one "conditional on a reading"
clause from each.

## Supplied Surface

Every sentence used below is quoted verbatim from the landed axiom memo
`docs/MINIMAL_AXIOMS_2026-06-29.md`. The runner guards each by
whitespace-normalized containment. **[checks 1-6]**

Record axiom (readout content and additivity):

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

Law sentence (Qualification section):

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

The two distinction clauses:

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> No possibility is privileged. Possibilities are distinguished by the supplied
> algebraic structure alone.

Lattice motion group (used by the motion-closure restatement):

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic rotations
> **about each site**.

## T1 — R\* discharges to landed Record text **[checks 7-9]**

R\* (review-pending PR #4818 block03) reads: a registrable scalar readout is
(1) additive over pairwise-disjoint records with `I(empty)=0`, and (2)
well-defined given only the supplied structure, i.e. constant on the orbit of
any unsupplied auxiliary choice; an imported basis or frame is such a choice and
its orbit is the choice set.

**Clause 1 is the Record additivity sentence's content.** "additive over
pairwise-disjoint records, with `I(empty)=0`" matches the landed sentence "For
any finite collection of pairwise-disjoint records, scalar readout `I` is
additive, with `I(empty)=0`" — block03's clause omits the sentence's "finite"
qualifier, so the axiom sentence is the stronger finite-collection form and the
discharge direction is unaffected. No new content is asserted.

**Clause 2 is an instance of content-determination.** Suppose a readout value
varies with an unsupplied auxiliary choice (an imported basis) at fixed record
content. Then the value is not determined by record content alone — excluded
directly by "A readout value is determined by record content alone." The runner
exhibits this on a fixed record content with a two-element imported-basis orbit:
the basis-dependent readout takes two distinct values over the orbit and is
flagged not content-determined **[check 7]**; the record-content-only readout is
orbit-constant and passes **[check 8]**; the orbit is a genuine choice set of
labelings **[check 9]**. Supplement: an imported basis is *not* record content,
and by the Qubit distinction clause ("Possibilities are distinguished by the
supplied algebraic structure alone") it carries no possibility distinctions — so
a distinction the readout draws only via the basis is carried by neither record
content nor supplied structure.

**Direction and scope.** The memo fixes all supplied structure (one fixed
admissibility rule, the fixed `Z^3`, the fixed shared one-site domain), so at
fixed record content only unsupplied choices can vary — the axiom sentence and
clause 2's orbit-invariance form coincide extensionally on this surface. The
discharge is of the exclusion direction only (registrable implies the clauses),
which is all that block03's C1a and block05's horn 2 consume; the converse
direction and any expressibility-from-supplied-structure claim are not
discharged.

**Consequence (stated carefully).** Block03's C1a result — no imported basis in
a scalar readout — thereby upgrades from "conditional on the reading R\*" to
"conditional on landed axiom text plus block03's own finite witnesses." The
interpretive premise is discharged. Block03 itself remains review-pending and
the audit lane owns its status; C1b (realized-state-dependent partitions)
remains open exactly as block03 left it. This note adjudicates nothing.

## T2 — D-totality discharges to the law sentence **[checks 10-11]**

D-totality (review-pending PR #4820 block05) reads, verbatim:

> A physical readout rule must be well-defined at every law-admissible realized
> state in its stated law-domain. This is a rule-domain totality constraint: a
> law-property of the rule, not a state property.

This is an instance of the law sentence "Its domain is a supplied condition, and
at every state where the condition holds it gives exactly one answer." A rule
undefined at a state where its supplied condition holds fails to give exactly one
answer there; by the law sentence it is not a law. The runner exhibits a partial
rule (undefined at one in-domain state) failing exactly-one-answer totality
**[check 10]** and a total rule passing **[check 11]**. Rule-domain totality is
therefore axiom text: it names the law sentence's own "at every state where the
condition holds" applied to the rule's supplied domain. This discharges
D-totality as stated — relativized to the stated law-domain; any use requiring
the stated domain to BE the full admissible surface is not discharged here and
lands in T3(b)'s CTX residue. A rule claiming physicality without lawhood does
not evade the gate: it is further physical structure, and the Qualification
sentence requires derivation, bridge, explicit admission, or approved primitive
registration before use as a premise.

## T3 — The pointwise escape closes; the narrowed domain relocates to context governance **[checks 12-16]**

Block05's honest T4 escape: "Without D-totality, a reviewer may say: the
physical rule only needs to be defined at the actual realized nondegenerate Y."
Two variants.

**(a) Stated domain = the realized state alone — closes for generic realized
states. [checks 12-15]** As a *law* domain, a single generic
(non-motion-invariant) realized state is a singleton whose extension is not
motion-closed. Restating the motion-closure theorem
(review-pending PR #4851): every lawful condition's selected state set is carried
onto itself by lattice translations and proper cubic rotations; contrapositively,
a condition whose extension is not motion-closed draws, in extension, a
distinction among motion-related structure-isomorphic states, carried by neither
record content nor supplied structure — barred by the two distinction clauses.
The runner's 2x2x2 wraparound miniature (sites as tuples, mod-2 translation
transporting site->possibility records) shows a generic one-record singleton is
not motion-closed **[check 12]**, while the empty-configuration singleton *is*
**[check 13]**. Motion-invariant realized states are the honest exceptions, and
not only the empty one: a uniform configuration's singleton is motion-closed
and content-specifiable, hence a lawful narrow domain — but like variant (b) it
is silent at every other admissible state, so it is no full-surface context
supplier and relocates with variant (b) **[check 14]**. "A law privileges no
states" independently bars the intensional preferred-state form.
Independently, the realized-state primitive's own interface disclaims supplying
any domain certificate: "pointwise evaluation, not a state-selection rule ... no
preferred state, default state." Pointwise **evaluation** of a lawful rule at the
realized state is untouched — the runner evaluates a motion-closed rule at the
realized state and shows this is distinct from taking the singleton as the
domain **[check 15]**: **evaluation is not a domain.**

**(b) Stated domain = "Y nondegenerate". [checks 16-17]** This is a
record-content condition — granting, per review-pending block05's account, that
it is supplied-expressible and motion-closed (its record-content form; asserted
rather than witnessed here, and concessive: were it unlawful, the escape would
close harder). The S3-class rule is total
there by block05's own account — the runner models the law-admissible surface
delta = k*pi/6 exactly (Fraction multiples of pi), degeneracy loci at
delta = m*pi/3, and confirms the rule is total on the nondegenerate narrowed
domain **[check 16]**. Variant (b) is **not** excluded as a law. What it cannot
do is serve as a readout-context supplier for the full law-admissible surface:
at the degeneracy loci it is silent, and the full-surface-supplier check finds an
admissible state with no context verdict **[check 17]**. Block05's three horns
(review-pending) show every extension across the loci either coarsens away the
S3 data, or splits arbitrarily (not R\*-registrable), or completes via Fourier
and borrows algebra-canonical provenance. The residual question — which readout
context is supplied on the full surface — is the CTX rung: supplied-content
governance, not a reading. Stated plainly: variant (b) is excluded as a
full-surface context supplier, not as a law.

## T4 — Ladder consequence (flag, do not close) **[checks 17-20]**

The carrier/kappa ladder {R\*, D-totality, w-supplier, CTX-match} compresses
as follows. R\* and D-totality discharge to axiom text (this note,
unconditionally on the landed sentences). Conditional on the review-pending
blocks 16/17 treatment of the w-supplier rung — whose classification residue,
the `W_readout_coupling` registered-number gate, is itself supplied-content
governance and not an interpretive premise — and on review-pending PR #4851's
motion-closure theorem used in T3(a), the wall's non-reading residue is
{CTX-match} together with that gate. No reading remains anywhere on this
ladder: R\* and D-totality are discharged here, and the w-supplier rung was a
missing selector, never an interpretive premise. **No wall is closed** here and
this note **adjudicates nothing**; the note's own firewall is guarded by the
boundary greps **[checks 18-21]**.

## Consequence

Two "conditional on a reading" clauses are removed from the ladder's premises:
block03's C1a and block05's rule-domain totality now rest on landed axiom text
plus each sibling's own finite witnesses, rather than on a premise flagged for
adjudication. The pointwise escape from D-totality does not reopen a reading — a generic
singleton domain draws an unsupplied distinction (variant a); a motion-invariant
singleton or a nondegeneracy-narrowed domain is lawful but supplies no
full-surface context (variant b and its invariant-singleton analog), relocating
to CTX supplied-content governance. The ladder's non-reading residue is the
CTX-match rung together with the `W_readout_coupling` registered-number gate
(review-pending block17's classification residue), with no interpretive premise
attached to either.

## Does NOT

- Does **not** adjudicate R\* or D-totality as readings — it shows each premise
  is an instance of already-landed axiom text; adjudication is the audit lane's.
- Does **not** close, reopen, or rule on C1a, C1b, or any wall or gate.
- Does **not** touch `w`, the w-supplier classification, CTX-match content, or
  any campaign pack.
- Does **not** set, imply, or predict audit status for any row, block, or PR.
- Does **not** add, rename, move, or register any axiom, policy, primitive, or
  registry content.
- Does **not** read any branch content beyond the supervisor-supplied excerpts.

## Dependencies

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — the landed axiom memo (Record additivity
  sentence; "A readout value is determined by record content alone."; the law
  sentence; the two distinction clauses; "about each site").
- Review-pending PR #4818 (block03) — R\* and the C1a/C1b result shape.
- Review-pending PR #4820 (block05) — D-totality, the degeneracy-loci
  three-horn provenance collapse, and the T4 escape.
- Review-pending PR #4851 — the reading-note retirement and the motion-closure
  theorem (restated inline in T3(a)).
- Review-pending blocks 16/17 — the w-supplier rung (forcing fork; scale
  absorption / `W_readout_coupling` residue).
- The realized-state primitive (approved framework primitive) — quoted as its
  interface: pointwise evaluation carries zero state-contingent content.

## No-Promotion Statement

This note promotes nothing. It introduces no premise, closes no gate, and
changes no registry or ledger. It records a bounded observation — two readings
are instances of landed axiom sentences — and leaves every status, every wall,
and every sibling exactly where the audit lane holds them.
