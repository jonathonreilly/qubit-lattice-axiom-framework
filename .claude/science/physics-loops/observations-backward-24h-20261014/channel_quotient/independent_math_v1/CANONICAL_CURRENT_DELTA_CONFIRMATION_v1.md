# M9 narrow current-byte confirmation v1

This supplements, and does not alter, `CANONICAL_MATH_REVIEW_v1.md` (SHA256 `d33dc165fdf99b9128e4cf1e5f4c7180c64bdb213806a74102786235a0ec9395`). It checks only the requested source delta, not a fresh mathematical derivation, empirical validation, aggregate execution, or formal audit.

- **Canonical note:** current SHA256 `5bd3667c7e34646e616c82498401c8c9169604ce471aeefefd3f1b1da65f6616`. Exact text comparison confirms the sole change is the NCO paragraph: retained join residuals are unwrapped and have no fitted offset; a separate fractional diagnostic is also reported; neither selects a phase convention. All equations, proof claims, numerical values, N1–N8 scope and physical limitations are otherwise unchanged. This clarifies documentary/data reporting without broadening the mathematical claim. Actual NCO computations remain outside my validation.
- **Mathematical helper:** current SHA256 `63722a00b46a66c6b350c64a524a6d13d49bf78c3fcd038957b46c3237b37696`. The sole added line is `AUDIT_TIMEOUT_SEC = 180` immediately after the docstring. Removing that exact assignment produces an AST identical to the previously reviewed source. No formula, guard, assertion, fixture, return value or executable aggregate body changed.
- **Primary runner:** SHA256 remains `1a8fbc27920523da57e56b118f89462e35a434d610fe61ebf89c9fb5cc72a535`; its bytes match the previously reviewed snapshot exactly.

The exact current snapshots, diffs and exposure metadata are preserved in this directory. Three narrow static bindings passed: note-only replacement, helper AST identity after the timeout declaration, and primary byte equality. No aggregate was rerun. No empirical helper was opened or newly bound; the reported timeout additions there are outside this supplement's scope.

No new mathematical or scope discrepancy was found. The original complete report and its limitations apply to the current bytes above. Only new immutable reviewer-directory files were written; no shared source, Git/index, status, lock, data, cache, PR or audit record was changed.
