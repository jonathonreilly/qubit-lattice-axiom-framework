# Local adapter review — PASS

The change is exactly `hint[0]` → `hint[1]` relative to `prepare_candidate.py`. The extractor returns raw text first and normalized known Type second. Actual8061 includes a Status suffix in the raw value, so only the normalized value is the correct category test.

Six actual predicate controls passed: actual8061, actual8059 and ordinary bounded Type accepted; unknown, meta and missing Type rejected. The tested assertion AST is taken directly from the adapter; no integration/cherry-pick code or scientific runner was executed.

This does not replace the distinct `prepare_candidate_typed.py` variant or remove its extra explicit metadata checks. No scientific source, premise, cache or verdict changed.
