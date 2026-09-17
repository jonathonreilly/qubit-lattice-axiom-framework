# GOAL — block 31: the sharper bad-pair budget `E ≤ 3(|S| − 1) + |A|` for block 30's extended explanation tree — prove it or refute it (2026-09-16)

**Directive.** Owner 2026-09-16 (evening): "keep going, try the sharper bad-pair budget next." Block 30 (PR #8174) proved `E ≤ 3(|S| − 1) + 2|A|` for its extended explanation tree, measured at most `2/3` of the allowed two excuse arrows per amplified node on `4290` executed trees, and named the sharper budget as its first open item: a proof would put the amplification weight at `ε₂/t` instead of `ε₂/t²` and move the region from `p ≥ 4165` to `p ≈ 500` at `(p, 1, 2)`.

**Exact target (claim type `bounded_theorem`, either sign).**
- Positive form: for every extended explanation tree of block 30's construction, `E ≤ 3(|S| − 1) + |A|`; then the region with exact certificates.
- Negative form: an explicit configuration of the two-level automaton whose tree (block 30's construction, re-executed) violates the sharper budget while satisfying block 30's; the mechanism; the largest constant refuted; the stake recorded.

**Seat plan (supervisor-run, no subagents).** Controls: the per-refinement accounting on random trees (`supervisor_control_block31_search.py`); a hand analysis of chains with three kept poles; a hill-climb on the ratio `(E − 3(|S| − 1))/|A|` (`..._climb.py`, `..._climb_wide.py`); witness verification (`..._witness.py`); the stake's certificates (`..._certify.py`). Contract with a self-run lens pass; primary; refuting pass with disjoint machinery (`..._refuter.py`); fold; mutation census; gates; independent PR against `main`.

**Stop conditions.** A proof (positive form) or an executed witness (negative form); otherwise a recorded attempt with the obstacle named. Never merge; layman update at the milestone.
