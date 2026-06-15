# Route Portfolio

1. Strip the single-clock edge entirely and narrow the theorem to `d_t >= 1`.
   Rejected: unnecessarily loses the bounded `d_t = 1` conclusion.

2. Keep the conclusion and localize the upper-bound input to the already declared `B-AXIS` premise.
   Chosen: preserves the theorem's honest boundary and removes the false citation cycle.

3. Prove `B-AXIS` in this PR.
   Rejected: too broad; would be a separate frontier theorem and risks hiding the open premise.
