# Historic intake: beta=6 SU(3) Wilson Plaquette - Consolidated No-Go / Ruled-Out Ledger

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: no_go
Stratum: pack_science_family
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The most thorough no-go inventory in the stratum: the single missing object is rho_{p,q}(6), the boundary character measure / Perron eigenvector of the unmarked 3D spatial Wilson environment, and it is DOUBLY WALLED with no route escaping both - W-ALG, local character plus intertwiner data plus any one-parameter rho-family leave a combined Perron spread >= 0.1937 straddling 0.5934; and W-COMP, exact L_s>=3 contraction has treewidth >= 29 giving 8^30 intermediates (~1e19 GB, about 20 orders over budget) while naive Haar Monte Carlo is sign-problem-bound with integrand ~1e-100 needing ~1e200 samples. Twenty routes are catalogued with their exact numbers (M1 0.4225, M2 0.3333, M4 0.8740, M5 0.9259, L_s=2 variants 0.4291, K-tube 0.5888 at a 0.78% near-miss), and all five analytic routes are dead.

Original verdict: Adds one new finite-geometry no-go from cycle 1: of all 5966 connected leaf-free distinct supports of total size 6, ZERO are SU(3) color-closable, so d_6 receives contributions only from the four order-5 cube shells via order-6 multiplicity.
Scope: beta = 6 SU(3) Wilson plaquette closure; statuses are 2026-05-29 read-offs from docs/audit/data/audit_ledger.json and are flagged for re-verification before citing.
Escape conditions (negative claims): Route 1 (d-log-Pade / conformal resummation of the connected-shell series) is the one long-shot the loop attacks; and the observable-bridge no-go's escape needs a NEW independently-audited primitive. Target-fit exponent closures for the 0.78% gap are explicitly rejected as importing an unproved correction.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The beta6/plaquette attack-surface no-go inventory: the single missing object is rho_{p,q}(6) (boundary character measure / Perron eigenvector of the unmodified transfer operator); adds the cycle-1 finite-geometry no-go over all 5966 connected leaf-free graphs; flags the 0.78% K-tube near-miss (0.5888 vs target) as noise with ranked escape routes. Harness companions attached; cross-linked to the exhausted-routes terminal 10289.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/beta6-plaquette-closure/NO_GO_LEDGER.md`
- Source commit: `549efbd7ce20c5b78dceb84b44093ca1047bdcf5`
- git blob: `8b26afeeb8547faab55c40ca94cd6a1ff8b5c40c`
- sha256: `adb53833e470e7eefd322b53fb60308c94d33f1787be99b7a05048146cc92f2e`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci01/10275_NO_GO_LEDGER.md](../../archive_unlanded/historic_intake_originals/packsci01/10275_NO_GO_LEDGER.md)
- Lines: 104; runners named: none

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/beta6-coefficient-source-packet-20260608/CLAIM_STATUS_CERTIFICATE.md` — Harness-provenance repair; the repaired claim is harness arithmetic over a visibility set, not a closure.
- `.claude/science/physics-loops/beta6-coefficient-source-packet-20260608/NO_GO_LEDGER.md` — Four rules incl. do not read the harness as a beta=6 closure proof and do not treat the d11 cache check as independent.

## Cross-stratum flags

- Attaches across strata to [idx 10289](HISTORIC_NO_GO_LEDGER_B10289_INTAKE_NOTE_2026-08-05.md) (`.claude/science/physics-loops/bridge-gap-new-physics-20260506/NO_GO_LEDGER.md`, stratum packsci01) — The beta6/plaquette attack-surface no-go inventory: the single missing object is rho_{p,q}(6) (boundary character measure / Perron eigenvector of the unmodified transfer operator); adds the cycle-1 finite-geometry no-go over all 5966 connected leaf-free graphs; flags the 0.78% K-tube near-miss (0.5888 vs target) as noise with ranked escape routes. Harness companions attached; cross-linked to the exhausted-routes terminal 10289.
- Cross-stratum reference from packsci01 [idx 10289](HISTORIC_NO_GO_LEDGER_B10289_INTAKE_NOTE_2026-08-05.md) (`.claude/science/physics-loops/bridge-gap-new-physics-20260506/NO_GO_LEDGER.md`, decision PULL) — TERMINAL of the Resolution-A programme: seven routes formally exhausted (V>=2 Picard-Fuchs lift, APBC Z_3 twist needing L~17, SDP plus Migdal-Makeenko needing L_s>=4, Cl(3) heat-kernel route, et al.); the live attack lever is the gauge action functional itself - the disclosure that the entire plaquette programme rests on Wilson as an import is the strategic content. Cross-linked to 10275.
- Cross-stratum reference from packsci03 [idx 10824](HISTORIC_NO_GO_LEDGER_B10824_INTAKE_NOTE_2026-08-05.md) (`.claude/science/physics-loops/reflection-positivity-bounded-inputs-repair-20260527/NO_GO_LEDGER.md`, decision PULL) — MAJOR DEMOTION of a load-bearing authority: the full staggered-only reflection-positivity theorem is WITHDRAWN from A11 - the attempted rescue via gauge Cauchy-Schwarz + determinant positivity fails, the auditor was right, and the two missing physical-action bridges are named as the only reopen path. A11 is cited elsewhere in this stratum as the basis of the plaquette-bootstrap lemmas - every A11 consumer inherits this. Narrowing companions attached.

## Flags carried

Records that a 0.78% near-miss (K-tube 0.5888 vs 0.5934) was at risk of being closed by fitting exponents to the gap - explicitly rejected. Also records that importance-sampled Wilson MC at L_s=3 is FORBIDDEN because it would import the target value 0.5934.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
