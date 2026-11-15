# LOCOP author log

2026-10-30. Executed `briefs_q/LOCOP/AUTHOR.md` under PROCESS_LIGHT.md.
Scope is LOCOP.md, this log and checks/locop_* only. No commits, axiom,
audit, ledger or coordinator-file edits. The supplied workspace has no
usable git metadata; source identity is the byte inventory in
[checks/locop_inventory_before.json](checks/locop_inventory_before.json),
covering 3,925 pre-existing non-LOCOP files. No current-main certification
is claimed. The inherited brief's commit descriptions are not independently
verified git ancestry in this snapshot.

Read the author/reviewer briefs, PROCESS_LIGHT, HANDOFF current assignments,
EXTCONT with REVIEW_EXTCONT, REALRGA, REALRGB, LINEAR_PACKAGE, and the
relevant normalization, covariance, extraction and current-status sections
of FLOW, BFT_A, BFT_B and SF. Important source locators:

| Source | Used material |
|---|---|
| EXTCONT §§2,5 | E1–E9 and E18–E19; coordinate extraction is distinct from the physical operator; EXT/COEFF remain open. |
| REVIEW_EXTCONT | Conditional LAND and re-derivation of the full Taylor bound; no actual induction certification. |
| REALRGA §§1–4 | Actual inherited density, RGA3/RGA4, complete supports, H0–H6, frozen sources and extraction requirements. |
| REALRGB §§1,6–7 | G1 norm mismatch, G33–G35 and the surviving actual extraction task. |
| LINEAR_PACKAGE §§1.2–1.3,2 | S4′ paths, normalized soft kernel, linear root covariance and scope of the abelian package. |
| FLOW §§0,3,7–9,15,19,52,96,105–110 | Beta normalization, exact signs, conditional AF bracket, FP-exact, T-tel, current-field projection and remaining UNIV list. |
| BFT_A §§7.1,8.0–8.2 | Composite gauge directions, residual fields, Qd=d ev and scope of the linear chain. |
| BFT_B §2.4 | Gauge covariance of pinned local pieces and the withdrawn general-depth extension. |
| SF §3.2 and latest outcome | Chart-Jacobian quadratic term, SF-N0, finite-pattern covariance, and the unclosed reproduction clauses. |

The installed physics-loop entry point was inspected for applicability.
This is a bounded existing author lane governed by its explicit light
process, not an unattended campaign or PR run; no campaign, loop pack or
skill-generated files were created. PROCESS_LIGHT explicitly requires
fresh hostile review, which authorizes the reviewer subagent below.

Primary-source checks used arXiv 1403.7253v2 (Brydges–Slade localization,
§1.3 Proposition 1.5/Definition 1.6 and §2.1 dual tests),
1907.05474v2 (Bauerschmidt–Brydges–Slade) and 1212.5562v2
(Dimock). They supply method attribution only. All newly used finite
lemmas are proved in LOCOP.md; no memory-only result carries weight.

## Author result

The finite construction uses local plaquette logarithms based at a common
vertex, four-orientation clover curvature, constant-curvature Hessian
tests and their tensor dual. It preserves gauge and lattice covariance
and is idempotent on its stated one-connection domain. The bulk orbit
sum reduces to the Wilson coefficient. A trace-free anisotropic tensor
is an explicit reason that the scalar projector alone cannot contract
arbitrary individual selected activities.

The exact normalized soft kernel has zero gauge defect. Its joint
fine/coarse dependence nevertheless permits relative-field quadratic
terms, and the chart Jacobian has its own quadratic term. Both are kept
distinct from a physical gluon mass in a local single-field action.

The new ideal real spatial-variation benchmark is 4/L+8/L^2. It is
20/9 at L=3, 28/25 at L=5 and 36/49 at L=7. Thus the displayed estimate
does not certify contraction at L=3 or 5. The stronger curvature-only
zero-jet benchmark remains 8/L^2. The full selected-return comparison,
coefficient estimates and E19 remain OPEN with six exact sublemmas.

## Preregistered finite checks

[Criteria](checks/locop_criteria.md) were written before the
[script](checks/locop_check.py). The sole initial run is saved in
[checks/locop_results.json](checks/locop_results.json), including their
SHA256 hashes and resource samples before/after every group.

- **PASS:** contour/mean covariance and soft exponent, maximum error
  3.343e-16 < 1e-12; the independent coarse-only negative control changes
  the exponent by 0.1224 > 1e-4.
- **PASS:** all 384 signed permutations, exact tensor reconstruction,
  18 plaquette/rectangle area tests, and the surviving anisotropic control.
- **PASS:** 72 monomial/scale cases, exact rational Taylor-bound comparisons.
- **PASS:** all 820 pairs of a synthetic 41-level flow, exact rational
  bracket and returned-term sign. No actual-model trajectory was tested.
- **PASS:** the SU(2) Haar coefficient and fixed-fine soft relative-field
  coefficient within their preregistered tolerances.

All five groups passed; no failed numerical check was suppressed. Runtime
was 0.036 seconds and peak RSS 22,724,608 bytes. The serial run used its
numeric lock, requested `nice -n 10`, and all six thread variables set to
one. Effective niceness in every saved sample was 20 (above the >=10
guard). Every recorded load was below 8 and memory-free percentage
above 30. No pools,
RLIMIT_AS or resource-guard relaxation was used. These finite regressions
are not uniform field/volume estimates or substitutes for the proofs.

## Fresh review and final verification

A fresh-context same-family Codex reviewer independently reconstructed
every substantive argument under PROCESS_LIGHT rule 3. The
[review](checks/locop_review.md) ends **VERDICT: LAND**, for this scoped
research note, with **no binding mathematical fixes**. This is not
cross-family verification or certification of actual E19 closure.
The author path restrictions place the report under checks/locop_review.md
rather than the separate reviewer lane's REVIEW_LOCOP.md; that separate
lane was not executed or edited.

The reviewer identified two nonblocking clarifications, applied in place:
effective niceness is 20, and T-tel must explicitly carry FLOW's
invertibility, zero-mode subspaces and log-absolute-determinant convention.
The latter paragraph now also defines Ytilde, Phi^T and G_gh. The reviewer
checked these affected paragraphs before issuing LAND on the final
LOCOP SHA256 `0295d071a60d0ba3abfa23e4722634c7c2ea54921423cd0451aec7381e2c9253`.
There was no numerical rerun because the script, criteria and numerical
claims did not change.

Final verification is saved in
[checks/locop_verification.json](checks/locop_verification.json): every
pre-existing inventoried file is unchanged, all newly created files are
within the allowed names, local document links resolve, the criteria
predate the script, and the receipt hashes match the criteria and script.
The reviewed document hash matches the delivered document. No commits
or modifications outside the lane's allowed files were made.
