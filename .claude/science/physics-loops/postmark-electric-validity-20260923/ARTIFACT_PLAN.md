# Artifact plan

| Artifact | Role | Current location | Audit/review use |
|---|---|---|---|
| `POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_NOTE_2026-09-23.md` | Bounded theorem and exact open obligation | `.claude/science/postmark-electric-validity-20260923/` | Main scientific statement |
| `TARGET.md` | Frozen observable, parameters, times, and outcome rules | Same evidence directory | Prevents post hoc target drift |
| `core_derivation.py`, `CORE_D_RESULTS.json`, `D_RESIDUE_POLYNOMIALS.json` | Ordered path expansion and exact coefficient table | Same evidence directory | Reproduce the finite-support correction |
| `finite_spin_jacobi_coefficients.py`, `FINITE_SPIN_JACOBI_COEFFICIENTS.json`, `MACROSCOPIC_FLUX_SYMBOL.json` | Exact finite-spin and residue factors | Same evidence directory | Reproduce the interior coefficient limit |
| `boundary_form_verifier.py` and `full_sector_crosscheck.py` plus outputs | Form-bound identities and independent finite-sector assembly | Same evidence directory | Check exact residues, boundary sequence, and small finite-spin matrices |
| `spectral_fixed_time_probe.py`, `SPECTRAL_FIXED_TIME_HIGH_SPIN.json`, `.stdout` | Finite double-precision spectral diagnostics | Same evidence directory | Numerical diagnostic only, no certified status |
| `SHORT_TIME_SCALING_NOTE_2026-09-23.md` | Conditional strong-operator limit and exact Bessel curve at `t=tau/C` | Same evidence directory | Derived theorem; explicitly does not close fixed laboratory times |
| `scaled_time_limit_probe.py`, `SCALED_TIME_LIMIT_CHECK.json`, `.stdout` | Finite-spin check of the shrinking-time limit and initial curvature | Same evidence directory | Double-precision corroboration only; proof is in the note |
| `exact_high_spin_scan.py`, `EXACT_HIGH_SPIN_SCAN*.json`, `.stdout` | Exact-only fixed-time scan through S=1280 | Same evidence directory | Values remain near one third but fluctuate; no limit inference or candidate comparison above S=384 |
| `postmark_fixed_time_flux_tails_20260923/` | Assumption and route-selection exercise packet | `.claude/science/exercises/` | Route reasoning and literature search; not proof authority |
| This loop pack | Resume state, premises, routes, claims, and handoff | `.claude/science/physics-loops/postmark-electric-validity-20260923/` | Required discovery-loop packet |

No `docs/**/*.md` note is added, removed, or rewired by this block; the citation-graph manifest is not in scope. No audit row, cache, receipt, generated ledger, queue, publication status, or repo-wide authority surface is changed. The branch's raw stdout files are raw logs, not runner caches.
