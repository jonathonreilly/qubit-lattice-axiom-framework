# The adoption impact manifest — the refire scope, machine-checked — Cycle 859

Date: 2026-08-01

Authority: none

Audit: unset

Status: bounded worked result (the corpus consumer classification; the
additive zero-byte invariance certificate; the scoped-refire
guarantee, corrected under adversarial check)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle859_adoption_impact_manifest_2026_07_28.py`](../scripts/frontier_cycle859_adoption_impact_manifest_2026_07_28.py)
- [`frontier_cycle859_manifest_independent_check_2026_07_28.py`](../scripts/frontier_cycle859_manifest_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. It MODELS a hypothetical adoption; it performs none.

## Result up front

If the owner adopts the E2 record-cadence sentence as a registered
primitive (the additive route), what refires? The manifest answers
with machine-checked classification of the tracked snapshot:

- **NO_CONSUMPTION: 9,320 files** — never touch record formation;
  untouched by any adoption;
- **CORPUS_IMPLICIT: 69 files** — use records only through landed
  behavior; zero content change under E2 adoption (they become exact
  rather than convention-dependent);
- **EXPLICIT_READING: 31 files** — quantify over the reading; the
  complete semantic refire list, and under E2 their re-ratification
  is confirmation-only (both readings already ran in the landed
  audits);
- **the invariance certificate**: a registry-additive adoption
  changes ZERO bytes of any pinned scripts/ or docs/ file
  (`ZERO_PINNED_SCRIPTS_DOCS_BYTES`, independently re-verified);
- **scope disclosed**: the classification is pinned to this branch's
  snapshot; the owner-lane adoption PR must re-run it on live main.

**Reversal twenty-nine, absorbed**: v1 classified 9,339 / 50 / 31;
the checker's broader needle/AST design refuted 19 NO_CONSUMPTION
rows (8 docs + 11 scripts, all genuinely corpus-implicit — named in
the v2 output with per-file evidence). v2 adopts the union sweep and
derives 9,320 / 69 / 31. The load-bearing guarantee survived the
correction unchanged: the explicit refire list is exactly 31 rows,
and the mechanical blast radius is zero.

## Supplied / derived / open

### Supplied

- the tracked snapshot; the certified E2 rule wording (Cycle 828);
  everything the cited packages declare.

### Derived

- the three-way classification with the union needle/AST design; the
  19 corrections with evidence; the invariance certificate.

### Open

- the live-main re-run at adoption time (owner lane); ledger-row
  mapping beyond in-tree surfaces (owner-lane grep per workhorse
  discipline).

## Negative-claim discipline

Classification claims are scoped to the pinned snapshot and the
declared union needle/AST design; the checker's constructive hunt is
the design's adversarial bound; nothing here asserts completeness
beyond it.

## Checker disclosure

The checker refuted v1's classification (reversal twenty-nine); v2
adopts its findings plus the union sweep. Only the checker's pinned
expectation constants were re-frozen for v2; its attack logic is
byte-identical and its v1-refutation labels are retained by design —
disclosed here and in the receipt, not edited away.

## Cache-contamination incident (v3)

The v2 scripts swept the WORKING snapshot. During the ship chain, this
block's own untracked note and receipt (which quote the E2 wording)
entered the worktree before the cache build; the cache re-execution
therefore saw a drifted tree, three certificates failed, and the
failing caches were briefly committed. v3 repairs the design defect:
both scripts now enumerate and read files exclusively from the pinned
tracked snapshot `d6a514430ac9921882017ba6424d289e2dc6b288` via git,
making the classification immune to working-tree state; both rerun
clean and reproduce 9,320 / 69 / 31 exactly. The incident and repair
are also recorded in both runners' outputs (`cache_contamination_note`)
and in the receipt. Process rule banked: repo-sweeping runners must
pin their snapshot; ship-chain guards must reject caches on nonzero
exit or any FAIL count.

## Verdict

The question "what breaks if we decide?" now has a certified answer:
nothing mechanically, thirty-one things semantically, and every one
of those thirty-one already contains its own confirmation. The
manifest was attacked, corrected, and its guarantee held — which is
the property one wants most in the document that says it is safe to
proceed. Independent audit still required.
