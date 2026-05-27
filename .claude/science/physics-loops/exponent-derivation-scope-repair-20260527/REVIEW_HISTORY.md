# Review History

Self-review disposition: pass for bounded boundary/scope repair.

Checks:

- `python3 scripts/frontier_exponent_derivation_scope_repair.py`
- `python3 scripts/vocab_lint.py --report-only docs/EXPONENT_DERIVATION.md`

External review should check whether the demotion is narrow enough and whether
any old prediction language still reads as binding.
