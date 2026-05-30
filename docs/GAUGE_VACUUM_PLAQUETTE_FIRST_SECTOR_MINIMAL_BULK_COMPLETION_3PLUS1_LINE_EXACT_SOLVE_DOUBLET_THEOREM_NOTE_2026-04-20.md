# Gauge-Vacuum Plaquette First-Sector Minimal-Bulk Completion `3d+1` Empirical Dense-Search Doublet Note

**Status:** bounded - bounded or caveated result note
**Claim type:** bounded_theorem
**Date:** 2026-04-20 (originally); 2026-05-03 (review-loop repair); 2026-05-08 (certificate-source repair); 2026-05-25 (audit-repair: narrow to empirical dense-search)

## Audit-repair (2026-05-25)

Per auditor verdict, this note retains only the **empirical dense-search
claim for the two observed root clusters on the selected positive-angle
chart**. The global exact-solve theorem phrasing is dropped from the
headline claim and **deferred pending an interval-arithmetic (or
resultant) certificate** of global exhaustiveness on the bounded chart.
The "exactly two roots globally" statement is therefore not asserted
here; what is asserted is that dense Monte-Carlo + structured-grid
seeding (3660 seeds, ~20× the original) finds exactly two observed
clusters with no additional cluster emerging.

## Review-loop repair (2026-05-03; certificate-source repair 2026-05-08)

The 2026-05-03 review follow-up identified that the original
runner used 175 seeds (7×5×5) of `least_squares` to count roots in the
bounded positive-angle chart, which certifies only that two LOCAL
solutions exist with small residuals and nondegenerate Jacobians — not
that the bounded chart has no ADDITIONAL roots. The repair adds a
**dense Monte-Carlo + structured-grid root-count certificate**:

  [`scripts/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.py`](../scripts/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.py)

uses a 15×12×12 = 2160-point structured grid PLUS 1500 uniform-random
seeds (3660 seeds total, ~20× the original 175). Every converged seed
(60% of the 3660 reach |residual| < 1e-10) clusters onto exactly the
**same two distinct roots** the original runner found. No additional
cluster emerges from the dense seed bath. Per-cell volume is
~8.5e-3 rad³, vs the chart volume ~31 rad³.

The 2026-05-08 follow-up audit flagged that the certificate was not
inspectable from the audit packet (no captured stdout, no structured
output artifact). The certificate-source repair adds:

- a JSON certificate at
  [`outputs/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.json`](../outputs/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.json)
  recording the bounded chart, the two root locations (line + angles),
  per-root residual norms, finite-difference Jacobian singular values,
  per-root cluster sizes, and seed counts; and
- regenerated runner-cache stdout at
  [`logs/runner-cache/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.txt`](../logs/runner-cache/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.txt)
  and
  [`logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_exact_solve_doublet_theorem_2026_04_20.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_exact_solve_doublet_theorem_2026_04_20.txt)
  so that the audit packet sees both the dense-certificate and
  original frontier-runner stdout.

The dense certificate is **empirical** evidence (high seed density →
no missed root cluster), not a symbolic proof of global
exhaustiveness. Strict symbolic root-count via resultants or interval
arithmetic remains genuine open work for a subsequent pass — the
target equation chains hermitian linear responses and a
Perron-Frobenius live readout of the compressed `3×3` block via
`compressed_local_block_from_line`, so polynomial reduction
isn't immediate. Until then, this note records:

- Local exact-solve: original runner finds 2 nondegenerate roots
  (small residuals, well-conditioned Jacobians).
- Empirical global root-count: dense seed bath finds the same 2
  roots with no additional cluster.
- **Open**: symbolic / interval-arithmetic certificate of global
  exhaustiveness on the bounded chart.

The honest scope of the bounded theorem is therefore: **on the
selected least-positive-bulk Wilson branch, dense Monte-Carlo
exhaustion finds exactly two roots in the bounded positive-angle
chart**. The "exactly two" claim is empirically certified at much
higher confidence than the original sparse seeding, but is not yet
rigorously closed.

## Statement (narrowed 2026-05-25)

On the selected least-positive-bulk Wilson branch, dense Monte-Carlo +
structured-grid search of the bounded positive-angle chart finds exactly
**two observed root clusters** of the specified target equation. Both
clusters reduce to nondegenerate roots (small residuals, well-conditioned
finite-difference Jacobians) via local `least_squares` polish.

Those two observed chart clusters form the concrete orientation doublet
later used by the selector law. This replaces the old named-witness
import by an empirically dense-searched two-cluster result on the
selected retained ambient.

**Deferred.** A global exact-solve theorem — i.e., a rigorous certificate
that the bounded chart contains exactly two roots and no others — is
**not claimed here**. Such a certificate would require interval-arithmetic
root enclosure (or symbolic resultant reduction) on the target equation
and is deferred to subsequent work. The current dense-search evidence is
empirical, not symbolic.

No closed-form symbolic classification beyond the bounded chart is
claimed.

## Authority

- Local exact-solve runner (original):
  `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_exact_solve_doublet_theorem_2026_04_20.py`
- Dense root-count certificate runner (2026-05-03 review-loop repair):
  `scripts/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.py`
- Dense root-count JSON certificate artifact (2026-05-08 certificate-source repair):
  `outputs/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.json`
- Captured runner stdout (audit-packet sources):
  `logs/runner-cache/gauge_vacuum_plaquette_doublet_dense_root_count_certificate_2026_05_03.txt`,
  `logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_exact_solve_doublet_theorem_2026_04_20.txt`
