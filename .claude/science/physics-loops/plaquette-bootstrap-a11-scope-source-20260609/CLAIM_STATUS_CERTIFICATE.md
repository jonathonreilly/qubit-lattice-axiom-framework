# Claim Status Certificate

## Current Claim Surface

Actual current-surface status:

```text
bounded/exact support theorem + named-obstruction stretch
```

This is not an audit verdict and does not retag the ledger.

## Closed By This Repair

- The BB1 Wilson-loop Gram PSD statement is no longer broad over arbitrary Wilson loops. It is scoped to Wilson-loop observables already proven to lie in A11's `A_+^(2)` surface.
- The Wilson-loop membership/source chain names the Gauge OS Step 1 companion theorem.
- The mixed-cumulant coefficient uses the retained `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md` authority.
- The beta=6 insertion is not theorem scope; it is a formal diagnostic showing why the small-truncation route remains weak.

## Still Open

- Full analytic `beta = 6` plaquette closure.
- Nontrivial beta=6 lower bound from higher bootstrap truncations or Migdal-Makeenko/SDP.
- Any effective status change before independent audit.

## Verification

```text
python3 scripts/frontier_plaquette_bootstrap_framework_integration.py
python3 scripts/cached_runner_output.py scripts/frontier_plaquette_bootstrap_framework_integration.py
```

Latest runner result: all checks passed.
