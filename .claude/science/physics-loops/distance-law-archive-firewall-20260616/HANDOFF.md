# Handoff

## What changed

The archived `DISTANCE_LAW_NOTE.md` packet is now explicitly historical /
diagnostic and retired as evidence. Its old results, interpretations, and
conclusion headings are marked retracted. `CLAUDE_BRANCH_RETAINABILITY_NOTE.md`
now points to the current bounded wide-lattice replay instead of listing the
failed archive as part of the retained-looking distance-law chain.

## What did not change

- No audit ledger or queue files were edited.
- No effective-status table was edited.
- No new physics premise was introduced.
- No distance-law theorem or estimator-selection theorem is claimed.

## Verification

Run:

```bash
python3 scripts/distance_law_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/distance_law_archive_firewall_2026_06_16.py
git diff --check
```
