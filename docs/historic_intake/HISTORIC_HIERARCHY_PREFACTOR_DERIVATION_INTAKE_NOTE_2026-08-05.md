# Historic intake: The Prefactor Problem: Can C = 1 Be Derived Analytically?

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

C = 1 cannot be derived from the Coleman-Weinberg mechanism: CW gives v = M_Pl exp(-pi/alpha_LM) whereas the taste formula gives M_Pl alpha^16, structurally different functions (1/alpha vs 16 ln alpha); the two CW routes bracket the taste result (bare Yukawa route A gives 87 GeV, improved route B gives 10834 GeV) and neither reproduces 254 GeV, with exp(-pi/alpha)/alpha^16 = 3.3 at alpha_LM = 0.0906.

Original verdict: NEGATIVE RESULT — v = M_Pl alpha_LM^16 is a numerically accurate approximation to a deeper structure, not an exact CW identity, and no analytic cancellation of O(1) factors produces C = 1.
Scope: 1-loop CW effective potential with rooted staggered tastes (N_eff = 12) versus the L_t = 2 taste-determinant power law.
Escape conditions (negative claims): The negative rests on the taste formula arising from the multiplicative taste-determinant structure rather than the logarithmic effective potential; internal route verdicts name the escapes — the eigenvalue-prefactor route fails because the prefactor is an O(1) number, and one route is graded PROMISING STRUCTURE blocked only because the O(1) coefficients c_k are not computed.

## Why pulled (supervisor decision, on the record)

CW no-go: exp(-C/alpha) vs alpha^16 structurally different — C=1 not derivable from Coleman-Weinberg; route killed with the near-agreement caveat noted.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_PREFACTOR_DERIVATION.md`
- Source commit: `feebdff7b41775e54b63a550d7cd526f1257a8c1`
- git blob: `9cd9813c359939ef088446f55d8cf38a4083d7ad`
- sha256: `6e2155840f03875b7bce09eacce847aa131152ba47610db121b02103d0541a3a`
- Lines: 381; runners named: none

## Attached evidence (registered with, not as, this claim)

- `docs/HIERARCHY_QUBIT_DETERMINANT.md` — Route survey companion; multiple routes graded REJECTED/CIRCULAR.

## Flags carried

Notes the near-agreement of the taste exponent -38.41 with -4 pi^2 = -39.48 (2.7%) is coincidental, i.e. the headline match may be numerological.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
