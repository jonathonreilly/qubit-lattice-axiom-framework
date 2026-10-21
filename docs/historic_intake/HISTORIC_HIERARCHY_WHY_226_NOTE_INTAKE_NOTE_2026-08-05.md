# Historic intake: Why Did v = 226 GeV Shake Out? A Thorough Investigation

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The original claim compression below is historical. The explicit arithmetic
annotation corrects its stated computation without rewriting the pinned
original. Independent audit remains required before any effective status.

## Arithmetic correction annotation (2026-10-21)

This annotation corrects the arithmetic quoted below; it does not alter the
pinned archive or certify the historical physical model. With all masses in
GeV, the printed model is

```text
v = 2.435e18 * exp(-8*pi^2/(N_eff*y_t^2)) GeV,
N_eff = 12*Z_chi^2.
```

Direct substitution gives:

| Supplied y_t | Supplied N_eff | v (GeV) |
|---:|---:|---:|
| 0.439 | 10.64 | 46.12277 |
| 0.439 | 12 | 3623.61063 |
| 0.9369 | 10.64 | 5.18774513e14 |

Thus substituting 0.9369 does not yield 226 GeV in the displayed formula.
The historical explanation that two errors cancel to produce 226 is not a
verified computation. The historical 45 GeV and 3.6 TeV values are rough estimates; the table
evaluates the specified decimals directly, without establishing physical predictions.

For a target 246 GeV and y_t=0.439, consistent units give

```text
ln(246/2.435e18) = -36.8311468945,
N_eff = -8*pi^2/(0.439^2*ln(246/2.435e18)) = 11.12360220,
Z_chi = sqrt(N_eff/12) = 0.96279118.
```

The WHY-226 archive's literal `ln(246e9/2.435e18)` is -16.1078810575, not -22.31,
and mixes the stated mass-unit conventions. The claimed requirement
N_eff>12 or Z_chi>1 is therefore false for the printed model. The WHY-226 archive
later gives 11.12/0.963; that calculation is consistent with the corrected units; contradictory
earlier claims should not be reused. This inverse calculation merely solves
for an input and does not derive a physical normalization or rescue the model.

The coefficient mapping called Sigma_1 remains unresolved in these records.
Neither 2.48 nor 6.12 is certified as the physical self-energy coefficient by
multiplying a scalar lattice integral by a guessed prefactor. The original
negative conclusion that 226 GeV was not derived is preserved; this annotation
does not validate the separate CW/gauge-sign argument, a physical mechanism,
or an order-of-magnitude prediction. Current use of the historical compression
below is subject to this correction.

The literal `exp(-8.45)*2.435e18` is approximately 5.21e14 GeV,
not 226 GeV. The displayed y_t=0.9369 formula evaluated without rounding the
exponent gives the table value above.

## The claim (as stated by the original, supervisor-compressed)

The 226 GeV result is a coincidence from two large errors that nearly cancel: y_t = 0.9369 (the SM pole-scale value) was quietly substituted for the framework's derived y_t = 0.439, and Sigma_1 was inflated to 6.0; with the derived y_t and N_eff = 10.64 the chain gives v = 45 GeV (or 3.6 TeV at N_eff = 12). Exact integrals give I_stag(4) = 0.619734 = 4 I_Wilson(4), so Sigma_1 is 2.479 under d*I_stag or 6.117 under pi^2*I_stag.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

WHY-226 coincidence anatomy: two large errors nearly cancel, smuggled y_t identified — pairs with 696 as the era's numeric-integrity record.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_WHY_226_NOTE.md`
- Source commit: `3524a8b5c9e89bb310fbd48b590258242b374f70`
- git blob: `f756c33c24da97d54aa2566ef96df83b9752e1e5`
- sha256: `ce62ce56c2350ae983a4d677d2df73893d197011e4ad573dfef021f1d4b4d9e3`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/708_HIERARCHY_WHY_226_NOTE.md](../../archive_unlanded/historic_intake_originals/branch03/708_HIERARCHY_WHY_226_NOTE.md)
- Lines: 784; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_sigma1_exact​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The number is a coincidence but the mechanism is real — CW dimensional transmutation with the framework's structural y_t genuinely produces v in the O(0.1-10 TeV) range; the precise value cannot be extracted without resolving the matching scheme.
- Extraction scope (triage compression; may reflect later context): Full re-derivation of the original 226 GeV chain plus identification of which lattice-integral combination 'Sigma_1' denotes.
- Extraction red flags: Documents a smuggled observed input (y_t = 0.9369) in a published derivation chain; the two corrective notes disagree on the correct Sigma_1 identification.
- Supersession (as known at extraction): Erratum-grade investigation of HIERARCHY_SOLUTION_SUMMARY.md's v = 226 GeV claim; sits alongside HIERARCHY_HONEST_REVIEW.md and disputes that review's choice of Sigma_1 = 2.48 over 6.12.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
