# Assumptions And Imports

- The audit ledger is read-only input for scanners. The branch checks the
  ledger hash before and after scans and does not edit `docs/audit/**`.
- Row buckets are current-snapshot certificates, not stable mathematical
  constants. Updated counts are exact for the current ledger snapshot only.
- Helper scripts are load-bearing when a runner imports them to compute a row
  bucket. This branch names those helper sources and caches in downstream notes.
- Supplied finite laws, selectors, weights, rules, clocks, kernels, and
  orientation bridges remain supplied inputs. No Record-derived physical
  selector, measure, Born law, production dynamics, clock/rate, or arrow is
  derived here.
