The runner breakage inventory reports `scripts/frontier_plaquette_self_consistency.py`
as a 60s timeout on the high-load-bearing plaquette self-consistency lane.

The terminal ledger no longer uses that runner. It uses
`scripts/frontier_plaquette_self_consistency_finite_mc_repair.py`, and the
source note is already narrowed to finite Wilson-plaquette diagnostic support.

This PR converts the old command path into a compatibility wrapper that
delegates to the repaired verifier. It does not promote the claim, rederive
the canonical `0.5934` plaquette value, or edit audit verdicts.
