# Document Authority And Citation Policy

**Date:** 2026-07-04
**Type:** process policy (audit-lane enforcement surface)
**Status:** active repo policy. This document assigns premise weight to
document classes and fixes citation discipline. It is itself Class E below:
process authority only, never a physics premise.
**Machine registry:** `docs/audit/data/doc_authority_registry.json`
**Primary runner:** `scripts/audit_companion_doc_authority_registry.py`
**Owner rule this implements:** supplied structure enters as a premise only as
an axiom, an approved primitive, or retained-grade derived/bridged content
(the axiom memo's Qualification). Prose guidance is never a premise channel,
no matter who wrote it or how often it is cited.

## Why this policy exists

On 2026-07-04 a program memo was nearly installed as "the doc all future
worker specs cite." A guidance document with no claim type, no runner, and no
audit row, cited as standing authority, is a **shadow premise channel**: its
sentences begin functioning as premises while nothing guards them — no
needles, no premise hash, no claim scope, no audit verdict. This policy makes
that failure structural rather than a matter of vigilance: every document
falls in a class, every class has a defined premise weight, and the companion
runner mechanically checks the invariants.

## Document classes

- **Class A — foundational notes.** The current axiom memo and explicitly
  approved primitive notes, mirrored by their stable ids in
  `docs/audit/data/axiom_premise_nodes.json`. These are the only two supplied
  premise types: **axioms** and **approved primitives**. Changes are
  owner-approved, logged in `docs/audit/AXIOM_MINIMALITY_POLICY.md`, and guarded
  by the clean-base runner. Cite the stable registry id and exact landed text.

- **Class C — runner-carried claim notes.** Bounded/no-go/bridge notes with a
  primary runner and a claim type. Premise weight: none until audit
  ratification; after ratification, exactly the audited `claim_scope`,
  nothing broader; prose outside the scope is not citable.
  Cite note + scope; never cite a title or a summary. Disambiguation
  (2026-07-04): the genre name `bounded_theorem` means SCOPE-PINNED — the
  claim is bounded to its quoted sentences. It is unrelated to the audit
  status `retained_bounded`, which marks an audited scope-bounded theorem.
  A Class C note whose premises are axiom sentences or approved primitives
  alone audits toward plain retained — unbounded theory; conditional notes
  audit as clean conditionals and convert to unbounded theory when their
  named premise is supplied or derived.

- **Class D — proposals.** Drafted axiom text, primitive drafts, owner
  one-pagers. Premise weight: none. An owner decision can authorize a reviewed
  Class-A registry/policy change, but the proposal never becomes a premise by
  itself. Cite only as "proposed."

- **Class E — process policies.** This document, the axiom-minimality policy,
  skills, methodology-lane operating notes. Premise weight: none for physics;
  process authority only. A Class E document may compel how work is done,
  never what is physically true.

- **Class F — orientation memos (thinking banks).** Program memos, criterion
  memos, synthesis prose. Premise weight: **none — no premise or interpretive
  weight.** Every Class F document must carry the exact formula sentence
  below in its header. Worker specs may cite Class F for orientation and
  scope discipline only; any premise in worker output must cite the owning
  Class A or audited Class C channel directly. The escalation paths out of Class F are: a
  derivation note (Class C) proving the content from landed sentences, or
  promotion to axiom-clarity text via the blind-panel pipeline (Class A,
  owner-approved).

- **Class G — operational surfaces.** Sweeps, work lists, queues, status
  boards, impact inventories, generated dashboards. Premise weight: none;
  operational content only. May be cited to explain what work was done or
  remains, never why a claim is true.

## The Class F header formula

Every Class F document must contain, verbatim, the phrase:

```text
no premise or interpretive weight
```

inside a header block that states the memo is citable for orientation and
scope discipline only. The formula matches the axiom-minimality policy's
retired-reading-notes discipline; Class F generalizes it to whole documents.

## Citation discipline (all classes)

1. A supplied premise cites a Class A axiom or approved primitive. Derived
   authority cites a Class C audited scope. Nothing else is a premise citation.
2. Class C prose broader than its audited scope is treated as Class F prose:
   no weight.
3. Titles, headlines, and summaries are never citable; quote the sentence.
4. A document's class is fixed by the machine registry, not by its own
   self-description; conflicts are registry bugs to fix, and the registry
   wins until fixed.
5. New guidance-shaped documents (PROGRAM, MEMO, CRITERION, SYNTHESIS,
   PRINCIPLES, PLAYBOOK and similar) land with a registry row in the same PR.

## Machine registry

`docs/audit/data/doc_authority_registry.json` holds one row per registered
document: `path`, `class` (one of A, C, D, E, F, or G), `status` (`landed` or
`in_flight_pr`), optional `pr`, `note`. The registry is seeded with the
documents that motivated this policy and the front-door surfaces; a
classification sweep of the remaining guidance-shaped documents is queued as
follow-up registry expansion. Registration is deliberately additive: an
unregistered document has whatever weight its class rules would give it once
registered, and zero premise weight in the meantime.

## Runner

`scripts/audit_companion_doc_authority_registry.py` mechanically checks: the
class definitions above are present; the registry parses, uses only the listed
classes, and carries `pr` on in-flight rows; every landed Class F document
contains the formula phrase; no Class F or G path appears inside
`axiom_premise_nodes.json`; and the reciprocal front-door links exist. The
runner is Class E infrastructure and proves nothing about physics.

## Links

- Axiom-channel policy: [`AXIOM_MINIMALITY_POLICY.md`](AXIOM_MINIMALITY_POLICY.md)
- Methodology front door: [`../ai_methodology/README.md`](../ai_methodology/README.md)
- Qualification (premise channels): `docs/MINIMAL_AXIOMS_2026-06-29.md`
