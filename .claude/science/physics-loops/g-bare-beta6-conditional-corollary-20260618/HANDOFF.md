# Handoff

The source repair is intentionally conservative. It preserves the useful exact
algebra while preventing downstream rows from citing this parent as a retained
zero-input `g_bare=1` theorem.

Verification run:

```text
python3 scripts/frontier_g_bare_derivation.py
EXACT   : PASS = 73, FAIL = 0
BOUNDED : PASS = 0, FAIL = 0
TOTAL   : PASS = 73, FAIL = 0
```
