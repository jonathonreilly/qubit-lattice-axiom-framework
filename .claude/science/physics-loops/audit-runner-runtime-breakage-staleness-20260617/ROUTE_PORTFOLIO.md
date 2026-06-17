# Route Portfolio

1. Active audited conditional repairs: already covered by open PRs for
   single-clock, Lorentz RG, R-eta, DM Schur, Koide, beta=6, and P-dep lanes.
2. Cycle-break targets: already covered by the source-edge repair PR.
3. Missing runner paths: already covered by the runner path canonicalization PR.
4. Runtime runner breakage inventory drift: selected here because 39 entries
   labelled `timeout` or `nonzero_exit` all have fresh `status=ok` caches on
   current source.

Selected route: add a lightweight guard that makes the runtime inventory drift
machine-checkable without editing audit result data.
