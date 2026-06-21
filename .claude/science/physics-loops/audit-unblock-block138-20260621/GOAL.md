# Goal

Continue the audit-unblock campaign without running independent audits and
without pushing to `main`.

Block138 refreshes the generated audit dispatch target-selection surface from
existing dispatcher sidecars. The goal is to make live re-audit sidecar targets
visible to the audit-loop selector while preserving the boundary that sidecars
are not audit evidence and no verdict is applied by this branch.

The updated local operating memory says not to spend campaign time refreshing
existing open PRs onto fast-moving `main`; the review lane will update or
cherry-pick those PRs.
