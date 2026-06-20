# Goal

Continue the audit-unblock campaign without running independent audits and
without pushing to `main`.

Block123 targets a systemic packet-completeness failure: primary runners that
load helper scripts through `_frontier_loader.load_frontier(..., "X.py")`
were visible to the runtime but not to `helper_runner_paths` in the citation
graph. That omission can leave audit packets without load-bearing helper
sources and force class-C missing-helper failures.

This block repairs the graph/parser layer only. It does not add a source
science claim, apply an audit verdict, or promote any effective status.
