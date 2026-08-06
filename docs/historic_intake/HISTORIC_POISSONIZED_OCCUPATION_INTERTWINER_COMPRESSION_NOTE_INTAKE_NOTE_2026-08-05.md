# Historic intake: Exact Poissonized Occupation/Intertwiner Compression for the Plaquette Law

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_exact_resummed_state_compressed_representation
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

With a(U) = Tr(U)/3 and independent Poisson M, N of mean lambda = beta/2, E[a^M conj(a)^N] = exp[(beta/6)(Tr U + Tr U^dag) - beta], so w_beta(U) = e^beta E[...] exactly; on a finite periodic lattice the normalized partition function and anchored numerator become Poisson expectations of link-Haar amplitudes, and truncating to m + n <= K gives a finite alphabet with an explicit uniform tail bound. At beta = 6, lambda = 3.

Original verdict: Exact law closed, exact finite small low-carrier closure impossible, exact useful resummed representation closed.
Scope: Exact resummation with truncation tail bound; leaves only a faster evaluator or tighter recursion open.


## Why pulled (supervisor decision, on the record)

Exact Poissonized resummed law (the useful exact evaluator surviving the finite low-carrier no-go).

## Provenance (pinned)

- Original path: `docs/POISSONIZED_OCCUPATION_INTERTWINER_COMPRESSION_NOTE.md`
- Source commit: `60a264ba93427b648c4c01edb5b2437542b78eb5`
- git blob: `d06ea8812a57e65f55c65779309a16809a6ff571`
- sha256: `f020dde452de5b577cb3579f9a552e09542523e7a2a56c2768f75c6012e1deb9`
- Lines: 225; runners named: scripts/frontier_poissonized_occupation_intertwiner_compression.py

## Attached evidence (registered with, not as, this claim)

- `docs/POISSONIZED_LINK_CHANNEL_COMPRESSION_NOTE.md` — Finite-state existence + channel identification.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
