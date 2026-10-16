# Focused canonical count-kernel energy review

Reviewer: `/root/inertial_response_check`. Date: 2026-10-15 UTC.
Root remains the scientific author. This is a source-bound scientific and
execution-correspondence review, not a formal audit, retained-status decision,
combined landing verdict or permission to merge.

## Conclusion and reviewed unit

After the explicit clock-regularity repair, no unresolved mathematical or
implementation discrepancy was found in the scoped canonical unit. The claims
remain conditional on the reduced calibrated count model, stable frozen free
scalar operator, supplied conformal force and inertial reference. The unit
derives useful necessary energy requirements; it does not infer an actual
scalar residual, upper field-energy budget, state-selection principle or
measured-gravity test.

I read the complete canonical note, primary, all three new helper modules,
public-input manifest and inherited ODF decoder. I also read the complete
prior independent Gram, mass/error, count-kernel, affected-source and timing
reports. The previous independent inertial derivation and 66-control report
were my own, frozen before root's inertial draft/code access. Those records
remain unchanged. This canonical review is bound to `CANONICAL_FREEZE_v2.json`
and the exact source identities below, including the later timeout-only
declarations and all affected repairs.

## Mathematical correspondence and interactions

The count-to-acceleration integration by parts has the correct sign and domain.
Compact L2 vector kernels give a compact H1 primitive precisely when their
integrated vector moment vanishes. Canceling scalar weights alone does not
cancel every initial velocity under a changing direction. The required
`N^T c=0` and additional `X^T c=0` conditions are kept distinct. Empty contrast
spaces and redundant nuisance columns are interpreted through their spans.
The unequal adjacent hat and gapped plateau use the actual centroid separation;
the gap acceleration is included rather than assumed zero.

I identified a domain gap in the initial canonical prose: merely increasing
clock maps need not justify a density obtained from the inverse Jacobian.
The final note requires a known C1 map with `s'(tau)>=epsilon>0` on the finite
observation intervals. Its inverse is then absolutely continuous, so the
ordinary change of variables applies. The existing L2 premise remains. The
repair is sufficient, does not alter a tested formula, and does not derive
the physical clock map. `CLOCK_DOMAIN_REPAIR_v1.json` and the original note
preserve the finding. The existing smooth clock controls did not need a repeat
solely for this clarified mathematical domain.

The stationary Gram has factor `1/(6pi)` in time-domain derivative products,
consistent with `||h||_H^2=2E`, unitary spatial Fourier transformation and real
frequency pairing. The explicit real Riesz q,p formulas reproduce that Gram.
The raw B matrix is correctly treated as an auxiliary representation of
bounded contrasts, not proof that individual uncontrasted velocity readouts
are bounded on the full energy space. The compact L2 kernel premise makes
its entries finite.

The minimum `r^T G^+ r/2` is conditioned on `r in range(G)`. The singular
nuisance extension retains the quotient range condition and does not discard
inconsistent components. Smooth exact-constraint approximation is correctly
distinguished from attainment in the energy completion. The explicit invisible
fields and finite-dimensional nullspace argument concern this specified
linear observation map; the note does not promote them to a theory-wide
impossibility claim or an unlimited physically admissible energy assertion.

The mass enclosure is a Loewner order, not an entrywise inequality. Independent
same-normalization modes contribute squared couplings and share one joint
energy budget. The lower energy inequality avoids incorrectly inverting a
possibly singular massive Gram. Nonzero q and positive quotient denominators
are explicit. At q=0 or a zero-Gram contrast the note uses compatibility,
not division. Weighted-ball whitening requires positive-definite B; singular
B instead retains support/feasibility. Error balls and componentwise bounds
are declared deterministic sets, not fitted covariance or confidence claims.

The inertial result retains both parts of the conformal force. Its factor
`k-omega*u`, positive branch frequency, on-shell Jacobian, anisotropic
massless tensor and massive threshold `mu/gamma` match the independent
derivation. The change of momentum coordinates preserves the laboratory
energy norm; it does not identify that energy with comoving energy. Pairing
opposite angular directions proves the all-mass matrix enclosure, and the
tensor is at most `I/(6pi)` for every strictly subluminal reference. The beta=0
limit is defined continuously, while beta=1 remains excluded. Arbitrary
accelerated paths and retarded endpoint mixtures are explicitly outside this
exact result.

The compact-window result extends continuously by H1 density. The Gaussian
windows in the inertial controls are rapidly decreasing H1 functions, so the
extension covers those controls without claiming a compact Gaussian. The
Gaussian derivative-product formula in `time_gram` has the correct sign and
normalization. The lab-momentum and boosted computations use different
integration variables and retain the same lab energy. Their numerical
truncations are controls, not interval-certified continuum proofs.

The exact moving minimum uses the anisotropic `B_u`, while `B_0` remains a
conservative upper enclosure. The count/nuisance quotient and inverse-energy
comparison use this distinction correctly. The new inertial helper actually
forms a mixed-mass, mixed-coupling sum; the stationary helper's individual-mass
controls are no longer inaccurately represented as a mixed-mode computation.

The physical conversion consistently uses positive Q_J, nonzero q and
`E_phi=2Q_J E_tot`, `G_bare=1/(8pi Q_J)`. The candidate algebra gives q=a/J
and q<1/3 within its explicitly supplied sector. Combining that ceiling with
a separately justified same-environment `G_meas>=G_bare>0` gives the displayed
physical lower bound, including coefficient `9/(4G_meas)` for nonoverlapping
unit-calibration means. The action, environmental identification and actual
energy/error values remain assumptions. Natural-unit formulas are not
silently evaluated with SI gravity and joules.

## Source adaptation and executable closure

I compared the preserved working scripts with the canonical helpers after
dedenting the new `run_checks` wrapper. The numerical count and inertial
calculations were unchanged apart from the later single normalization control.
Working-pack source/result writes were removed; the primary now owns output
and source identities. The timing helper takes explicit input paths, manifest
and output directory. Its new `weighted_moments` function extracts the same
exact rational arithmetic and adds the centered-moment fixtures.

The primary declares six input paths and a 240-second cap. The six inputs
are the note, three new helpers, the frozen decoder and public manifest; the
primary itself is hashed separately. All three new helpers now explicitly
declare the same timeout. The exact final changes from the pre-declaration
helpers are only `AUDIT_TIMEOUT_SEC = 240` plus its formatting. I verified
that removing that inserted declaration restores each recorded prior SHA256.
No equation or executable scientific check changed in this metadata repair.

The primary's only data inputs are the two manifest entries. It validates
both byte count and SHA256 for existing cache files and downloaded files,
rejecting mismatches. Its download path is restricted to the declared archive
prefix and validated bytes. The helper rechecks the same identities before
decoding. No working derivation, ancestor result, reserved product or directory
scan supplies hidden scientific data. Package-local integrity reads cover the
declared source closure. Imported numerical libraries and optional certificate
support do not introduce extra scientific observations.

The primary writes three result JSON files and a summary under its requested
output directory; the timing helper writes the chain JSONL there. Public input
downloads use the explicitly supplied input cache. The source helpers no longer
write their historical working-pack output paths. The inherited decoder is
imported only for its decode function; its CLI main does not execute on import.
Its current bytes are identical to M4 commit
`444fddc785280eb01898986edfc301bda9e8d9df`.

## Timing and centered-moment checks

The prior timing review independently decoded all 91,863 orbit rows, compared
every row with the frozen decoder, and compared the strata, chains, gaps and
selected exact moments with the author implementation. That exact unchanged
evidence is reused here, rather than rerunning the entire archive inventory
just to increase a check count. Its scopes remain 22 independent decode/invariant
checks and 114 subsequent source/result comparisons, not new physical tests.

The final canonical accounting and complete 36-chain ledger are unchanged:
91,664 Doppler rows, 199 type-37 rows, eight static strata, 36 chains, 91,628
adjacent pairs and 28 gaps, with no within-stratum overlap/duplicate in this
pinned product. Static fields include validity, and changing delays remain
diagnosed. Nothing is selected by observed value. The final ledger is still
SHA256 `cd5ba960fef413f2207056fa3cf39cf674242a51ce87081834953a0aa8a0a813`.

I additionally checked the extracted `weighted_moments` helper on seven
synthetic fixtures, including the three new canonical fixtures, unequal
durations, a singleton, and very large common frequency offsets. The independent
pairwise identity used was

```
sum_i d_i (y_i-ybar)^2 /(100*10^18)
 = sum_(i<j) d_i d_j (y_i-y_j)^2 /(100*10^18*sum_i d_i),
```

where d is in centiseconds and y in integer nanohertz. Exact rational equality,
the weighted mean and offset invariance all passed. The canonical five-entry
selfcheck also passed. These are arithmetic controls on a descriptive statistic;
no raw observation bytes were opened by this canonical review. The preserved
command and `AFFECTED_CHECKS_v1.json` bind the execution before later prose and
timeout metadata changes. Those changes leave the checked arithmetic untouched.

The raw variance remains Hz^2 seconds and is not a velocity residual, scalar
energy, noise model or empirical exclusion. Separate chains/stations are not
pooled as independent energy constraints. The displayed archive intervals are
nominal time tags, not a derived physical clock or retarded radio map.

## Mutation failure, affected repair and final execution binding

The first 17-variant mutation run had one survivor: doubling the equal-hat
Gram lowered the candidate energy infimum enough that existing above-infimum
and decreasing-excess controls still passed. The original helper, mutation
record and cache remain preserved. The repair adds one direct comparison
against the separately assembled finite-count overlap Gram for the same
observable. It does not change the mathematical formula or select a physical
normalization from data.

I independently extracted only `hat_gram` from the final helper and compared it
with direct signed interval-overlap integration at `(T,n)=(1,1),(.7,4),(2.3,3)`.
Errors were at most `1.12e-16`, and all three controls distinguish the doubled
normalization. The final current-source mutation record has 17 scientific
assertion rejections. I checked the source identity and matching AssertionError
record for every variant. These are finite mutation checks, not completeness
of all possible bug or physical-model exclusions.

The final cache reports exit zero, 150 count-energy controls, 81 inertial
controls and eight timing inventory aggregates. I verified every recorded
numerical error is finite and within its stored tolerance, and every Boolean
control is true. All 149 original count controls and all 81 original inertial
controls are unchanged in the final products; the one added count normalization
check accounts for 150. The largest equality errors are approximately
`1.81e-12` and `2.96e-12` respectively. The cache records approximately 2.05
seconds against 240 seconds, and empty stderr.

`verify_canonical_v2.py` checked the seven source identities, exact declared-input
fingerprint, stdout/summary equality, all product identities, invariant timing
accounting, unchanged full ledger, preserved first-run survivor, final mutation
identities and inherited decoder identity. It passed. This read-only verifier
did not execute either unchanged full author scientific suite.

The first binding verifier was started while the author added the helper timeout
declarations. It correctly rejected the now-stale `CANONICAL_FREEZE_v1.json`
identity before any scientific suite executed. Its source and stderr are
preserved, with `BINDING_FAILURE_v1.json`. The separately versioned verifier
binds the refreshed v2 freeze. The stale-source rejection is not erased,
relabelled as a scientific failure, or mistaken for a passing source receipt.

## Final identities and remaining limits

| Final source | SHA256 |
| --- | --- |
| Canonical note | `f6c0936a00c83070081797a59ef55c66ce5856c15e344d6a73b5fc496498988b` |
| Primary | `ada23f9ae989333afb0a50e2b0fe168ad50002da367758e124d2f7226fc3fa42` |
| Count-energy helper | `2b2edb9c7247dc20d2397ff67349ce7e03407915463305189a884ecd5038b07c` |
| Inertial-energy helper | `1952f032c9801e2592b71f46be7fb7f0981d7f467cf2ec7e2c09188fcb3184c2` |
| Timing helper | `288f9e8db8987ab2b9e01b980b10adfccc9a4f280f1385643b200deb7b3de14e` |
| Inherited ODF decoder | `2dfc9339ca5a962ade99df5a3270e95cff3e97501ce32f198ce51681fcb2d9c8` |
| Public-input manifest | `9b99d155442fb364df5bd32749d7f8ab2c0f355c87b4d2fc73affa1f69efe891` |

Final cache SHA256:
`83d72006b904b7b59c63b689db00a6bdee7c4c1416c48f08e4e25e5e4b3594a1`.
Declared-input fingerprint:
`4aa11d062a4b8959d1e911510633e791c911c00e9727152fee9cc1543b2a81dd`.
The identity JSON binds this report, review computations, source freeze and
the exact prior reports reused for unchanged material.

This review supports the scoped conditional theorem and faithful implementation.
It does not derive the candidate action/potential/scales, calibrate actual
spacecraft/radio dynamics, bound nonlinear or forcing effects, choose a scalar
state, supply an evidence-based error/resource budget, or certify an independent
experimental result. Formal audit and combined landing validation remain
separate. No source, ownership file, lock, branch, index or publication was
changed by this reviewer.
