# Historic intake: No-Go Discipline Checklist: Koide Frobenius Isotype Split

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pack_science_family
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

On Herm(3) the family B_{alpha,beta}(A,B) = alpha*Tr(AB) + beta*tr(A)*tr(B) is positive-definite exactly on the open cone alpha > 0, alpha + 3*beta > 0, every member is Ad-invariant, and the mixed scalar/traceless blocks vanish for ALL alpha,beta — so orthogonality fixes block shape but not relative weight. The scale-invariant ratio is (alpha + 3*beta)/alpha spanning the continuum 1 + 3*lambda for lambda > -1/3, and the circulant AM-GM extremum gives kappa(lambda) = 2/(1 + 3*lambda), which is unique only AFTER lambda is supplied and does not select lambda = 0.

Original verdict: PASS on all eight checks; there is exactly one recovery condition (a premise fixing the relative isotype-weight ratio), and beta = 0, equal block weights, and the Frobenius point are three names for it, not three walls.
Scope: Bilinear forms on Herm(3) plus the Herm_circ(3) restriction for AM-GM; no per-site, per-mode, or lattice-wide claim.
Escape conditions (negative claims): Strengthening 'Ad-invariant positive inner product' to 'the Hilbert-Schmidt form inherited from the ambient matrix algebra with its trace normalization' fixes beta = 0 immediately and restores kappa = 2 — that inheritance with fixed relative normalization is precisely the missing premise.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Structural negative on the kappa parameter: on Herm(3) the family alpha*Tr(AB) + beta*tr(A)tr(B) is positive-definite on an open CONE, so kappa = 2 (the value the r=1/2 story leans on) is not selected by positivity - it is a free parameter; N8 finds later Koide notes reusing the same free isotypic weighting. Adjudication-set member.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/koide-frobenius-isotype-split-repair-20260727/NO_GO_DISCIPLINE_CHECKLIST.md`
- Source commit: `b7a202dfb096e317abcebb26883b6a4d3a78ba00`
- git blob: `2275bdafc72036a1a1b66af0acdd9ad98c3dc078`
- sha256: `a39fcf00c3bb2815531851af1ac40485bc828cab9d84e675e5ae89d52355803e`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci02/10553_NO_GO_DISCIPLINE_CHECKLIST.md](../../archive_unlanded/historic_intake_originals/packsci02/10553_NO_GO_DISCIPLINE_CHECKLIST.md)
- Lines: 93; runners named: none
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/koide-frobenius-isotype-split-repair-20260727/NO_GO_LEDGER.md` — Companion: Frobenius uniqueness does not follow from positive-definiteness + Ad-invariance + scalar/trace conditions; the live route is left open.

## Cross-stratum flags (inert text; machine-readable relations in the audit fields)

- Attaches across strata to idx 10562 (`.claude/science/physics-loops/koide-mode-content-campaign-20260724/wave2_defend_ex2.md`, stratum packsci02) — Structural negative on the kappa parameter: on Herm(3) the family alpha*Tr(AB) + beta*tr(A)tr(B) is positive-definite on an open CONE, so kappa = 2 (the value the r=1/2 story leans on) is not selected by positivity - it is a free parameter; N8 finds later Koide notes reusing the same free isotypic weighting. Adjudication-set member.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: kappa = 2 (the value the r = 1/2 story needs) turns out to require a normalization premise that is not implied by positivity, Ad-invariance, and block orthogonality — a load-bearing hidden input in the Koide chain.
- Supersession (as known at extraction): N8 finds later Koide notes reusing the same free isotype-weight ratio — docs/KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md and docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md — which expose selector inputs but do not invalidate the counterexample.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
cross_reference:
- "HISTORIC_WAVE2_DEFEND_EX2_INTAKE_NOTE_2026-08-05.md"
```

Independent audit still required.
