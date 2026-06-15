# Opportunity Queue

1. Source graph cycle removal for 20 current cycle-break targets. Completed locally; cycle inventory becomes zero after regeneration.
2. Re-check conditional/failed rows after reviewer/auditor lands queued PRs. Current uncovered conditional/fail-ish rows are zero by open PR file coverage.
3. Continue runner-breakage cleanup only for live failures. The latest scan showed existing `scripts/*.py` breakage entries have fresh caches; many remaining inventory rows are stale generated metadata.
