# Review History

## Pre-review

- Auditor defect reproduced: the old runner imposed `G_full = u_0 G_V` while
  prose attributed the result to link factorization.
- Repair selected: narrow the no-go to a supplied common scalar map on `G`.
- Local runner after rewrite: `6/6 PASS`.
- Milestone adversarial review launched across code/runner, physics/import,
  no-go discipline, governance, and audit compatibility.

## Iteration 1

Findings:

- stale downstream wording still attributed scalar propagator scaling to CMT;
- the direct runner retained a tautological dimension-count test;
- the paired output drifted after the runner fix;
- source and pack trace/status fields disagreed;
- the first no-go checklist did not separate five mechanism classes or record
  the N3/N8 scans;
- downstream formulas still used link-like `U,V` labels;
- dispatcher guards did not survive source reseeding; and
- handoff and PR backlog lacked complete packaging details.

All findings were fixed narrowly. No audit verdict or generated audit authority
file was authored.

## Iteration 2

- Code/runner: pass. The reviewer independently checked generator
  Hermiticity, tracelessness, and `Tr(t^A t^B)=delta_AB/2` with maximum Gram
  error `1.11e-16`.
- Physics/import: pass on the scoped algebra and premise ledger. The physical
  CMT/EW-current gate remains open.
- No-go/governance: two packaging corrections requested and applied: precise
  runner coverage in the N1 record and a complete linked PR handoff.
- Audit validation: full pipeline reset the repaired row to `unaudited`, placed
  it at critical rank 40 in the regular queue, and rendered the dispatcher
  target live and ready. Generated outputs were then stripped.

## Iteration 3

Re-review of the two corrected files returned `pass`. Final milestone
review-loop disposition: `pass` for independent re-audit. This is not an audit
verdict.

## Independent math check

The load-bearing step was also checked without the runner implementation:
trace linearity gives `Tr(aG)=a Tr(G)` and
`Tr((aG)t^A)=a Tr(Gt^A)` term by term, so both absolute-square channel
functionals acquire exactly `|a|^2`. The zero-scalar and nonzero-denominator
ratio boundaries follow directly.
