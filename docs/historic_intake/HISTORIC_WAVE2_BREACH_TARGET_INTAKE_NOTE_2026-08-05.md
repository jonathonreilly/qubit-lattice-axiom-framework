# Historic intake: Wave 2 — the breach target: verify and sharpen the positivity obstruction

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

## The claim (as stated by the original, supervisor-compressed)

The EX3 positivity obstruction is arithmetically correct and STRUCTURALLY VOID: its identification of that algebra with the campaign's r silently drops the Gram factors (3, 6) of the generation coefficient surface — a factor of exactly 2, which IS the counting bit. What EX3 computed is the per-real-dimension isotypic weight ratio w_triv/w_nontriv, which equals r only in the det_R (count-twice) reading, so 'no positive weight reaches r = 1/2' is a statement made AFTER the counting bit has already been set to count-twice.

Original verdict: In the campaign's own det_C reading the same positive weights give r(t) = (S + 2F)/(2(S - F)), the breach is F/S = 0, and it is attained exactly by a nonnegative spectral function of the landed lattice Laplacian — no grading is needed and none is missing.
Scope: The EX3 obstruction and its breach condition; probe TOTAL: PASS=123 FAIL=0 with every number written from runner output.
Escape conditions (negative claims): Even in the det_R reading, F/S = -1/5 is attained exactly by a positive-semidefinite C_3-covariant weight, so the obstruction's true scope is the strictly narrower class {f(Delta) : f >= 0}, not 'any positive weight'; F/S = -1/5 names the ordinary cone point diag(1,4,4).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The EX3 positivity obstruction is arithmetically correct and STRUCTURALLY VOID: its identification silently drops the Gram factor 2 - the counting bit itself - and in the campaign's own det_C reading the same positive weights give r(t)=(S+2...)/...; even in the det_R reading F/S = -1/5 is attained. Retraction of the obstruction that framed the campaign. Companion pinpointing the operator-vs-form confusion attached.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/koide-mode-content-campaign-20260724/wave2_breach_target.md`
- Source commit: `e26664d20fcc050daa8feaa47a0e4c4b7259a23e`
- git blob: `35c651dc41adaa969b759765d9dcdcc382b07c3e`
- sha256: `54e97f8651818eea4c8a1649893706cb23e6803a4332237c1a41ef644985165f`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci02/10560_wave2_breach_target.md](../../archive_unlanded/historic_intake_originals/packsci02/10560_wave2_breach_target.md)
- Lines: 865; runners named: historic runner (unpinned, not in this packet): `wave2_breach_probe​.py (scratch, 123 gates)`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/koide-mode-content-campaign-20260724/wave3_reconcile_positivity.md` — Pinpoints the operator-versus-form matrix confusion exactly: (P2) e_2 = 3(a^2-|b|^2) is correct and elementary; as stated the two claims are jointly inconsistent - corrected, they are about different objects; exactly two of nine cited surfaces are retained-grade; one live escape from excluding count-twice named.

## Cross-stratum flags (inert text; machine-readable relations in the audit fields)

- Attaches across strata to idx 10046 (`.claude/science/exercises/koide-counting-bit-20260724/ex3_literature_templates.md`, stratum packsci01) — The EX3 positivity obstruction is arithmetically correct and STRUCTURALLY VOID: its identification silently drops the Gram factor 2 - the counting bit itself - and in the campaign's own det_C reading the same positive weights give r(t)=(S+2...)/...; even in the det_R reading F/S = -1/5 is attained. Retraction of the obstruction that framed the campaign. Companion pinpointing the operator-vs-form confusion attached.
- Named non-pulled evidence (provenance only): idx 10046 `.claude/science/exercises/koide-counting-bit-20260724/ex3_literature_templates.md` — archived byte-exact at `archive_unlanded/historic_intake_originals/packsci01/10046_ex3_literature_templates.md`, sha256 `3b59146cddcf9eb46abc88d1285864da446d4f8788224ff4113f9adec29f84a3`

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: A quantitative obstruction that framed the campaign was invalidated by a dropped Gram factor of exactly 2 — the very quantity under dispute. Also carries forward the Wave-1 stale-status flag.
- Supersession (as known at extraction): Only one leaned-on surface is retained-grade (docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md, retained_bounded/audited_clean); the heat-trace identity is RE-DERIVED not cited. Corrects EX3's weights 'w_triv = 3S/5, w_nontriv = 6S/5' as off by 3x (correct values S/5, 2S/5) and corrects its limit reading.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_retraction
intake_directive: owner_2026-08-05
cross_reference:
- "idx 10046 (not pulled; packsci01) .claude/science/exercises/koide-counting-bit-20260724/ex3_literature_templates.md"
```

Independent audit still required.
