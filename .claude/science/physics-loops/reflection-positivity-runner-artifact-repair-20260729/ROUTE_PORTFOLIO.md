# Route portfolio

Prior-art sweep commit: `a1e2bc70615fd8d09edd8dca3287ec054e0e9a4a`.
The matching theorem and all-order nonnegative tensor-multiplicity proof are
already present on `origin/main`; this block is an artifact repair, not a
novelty claim.

| Route | Disposition | Reason |
|---|---|---|
| Renderer opt-in marker in the independent helper | adopted | Produces the authenticated `runner_stdout_independent` role while preserving separate execution. |
| Concatenate helper stdout into primary normal mode | rejected | The combined stream would exceed 20,000 characters and could clip N1--N8 evidence. |
| Rely on SHA-pinned helper cache only | rejected | Cache is useful diagnostic evidence but does not authenticate current-cycle independent execution. |
| Change the theorem or add another derivation | rejected | The auditor already found the chain mathematically closed; this would miss the named blocker. |
