# Handoff

This branch repairs the U(1) sign convention in the axiom-first lattice
Noether note. Since `(i/2) B` multiplied by `i` gives `-(1/2) B`, Step 4a now
uses `J_real := i J_imag`. Runner E5 now uses the same convention and checks a
nonzero scalar bilinear so the sign cannot be hidden by cancellation in the
free-state numerical exhibit.

## Verification

- `python3 scripts/axiom_first_lattice_noether_check.py`
- `python3 -m py_compile scripts/axiom_first_lattice_noether_check.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/axiom_first_lattice_noether_check.py --force --push-mode=none --allow-non-main --concurrency 1`

## Reviewer Notes

- No `docs/audit/**` files should be present in this PR.
- No new axiom is introduced.
- The KS-phase-form structural admission remains conditional.
- The translation density (3) remains support-only.

## PR

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2747

Initial pushed commit: `e9792b123`.
