# Historic intake: The general-n census law, the composite-ring table, and the spf selection floor - Cycle 870

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Proves N(n,k) = 4(n/k)C(n-k-1,k-1) = 4n/(n-k) C(n-k,k) by two routes (transfer matrix / Lucas polynomial and an origin-marking double count) that agree symbolically, reproduces the landed n = 11 row 44/176/308/220/44 exactly, and derives a stabilizer lemma giving the smallest C_n-covariant selection size as spf(n) (4 spf(n) under C_n x Z_4), with singleton covariant selection impossible for every n >= 3.

Original verdict: The census law is not an n = 11 accident, and the free-selection no-go's dependence on primality is now priced exactly - the floor a composite ring buys is its smallest prime factor, never one.
Scope: Brute-verified n = 3..18, symbolic n = 3..14, Moebius extension to n <= 40; the selection statement is scoped to C_n-covariant selections, where the floor argument is a complete classification rather than a search.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The census law N(n,k) proved by two independent routes AND refuting an external math-report prediction at its declared k.

## Provenance (pinned)

- Original path: `docs/GENERAL_N_CENSUS_LAW_CYCLE870_BOUNDED_THEOREM_NOTE_2026-07-28.md`
- Source commit: `81aa497ba886619ae3569f4cea432c7b7124eef2`
- git blob: `ec31a00b57707c25ef944366f751ea3a10409acd`
- sha256: `c8a80f35d48056396a10477d501da898275c950c2a6001e9dbccad207b26931f`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/604_GENERAL_N_CENSUS_LAW_CYCLE870_BOUNDED_THEOREM_NOTE_2026-07-28.md](../../archive_unlanded/historic_intake_originals/branch02/604_GENERAL_N_CENSUS_LAW_CYCLE870_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- Lines: 164; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_cycle870_general_n_census_2026_07_28(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_cycle870_census_independent_check_2026_07_28(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Checker independence is cross-context but not cross-model (both scripts share an authoring model family); a no-hardcoded-answer probe fired mid-block on a sweep-bound collision with a derived value.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
